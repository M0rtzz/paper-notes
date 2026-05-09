---
title: >-
  [论文解读] GenQ: Quantization in Low Data Regimes with Generative Synthetic Data
description: >-
  [ECCV 2024][模型压缩][量化] 提出 GenQ，首次利用 Stable Diffusion 生成的高质量合成数据进行神经网络量化，通过能量分数过滤和BN分布过滤两种机制确保合成数据的分布对齐，在无数据和少数据量化场景下大幅超越现有方法，4-bit QAT ResNet-50 在ImageNet上达到76.10%准确率。
tags:
  - ECCV 2024
  - 模型压缩
  - 量化
  - 合成数据
  - 扩散模型
  - 数据无关量化
  - 低数据量化
---

# GenQ: Quantization in Low Data Regimes with Generative Synthetic Data

**会议**: ECCV 2024  
**arXiv**: [2312.05272](https://arxiv.org/abs/2312.05272)  
**代码**: [https://github.com/Intelligent-Computing-Lab-Yale/GenQ](https://github.com/Intelligent-Computing-Lab-Yale/GenQ)  
**领域**: 模型压缩  
**关键词**: 量化, 合成数据, Stable Diffusion, 数据无关量化, 低数据量化

## 一句话总结
提出 GenQ，首次利用 Stable Diffusion 生成的高质量合成数据进行神经网络量化，通过能量分数过滤和BN分布过滤两种机制确保合成数据的分布对齐，在无数据和少数据量化场景下大幅超越现有方法，4-bit QAT ResNet-50 在ImageNet上达到76.10%准确率。

## 研究背景与动机

**领域现状**：低比特量化是模型压缩的重要手段，但通常需要原始训练数据来缓解量化误差。隐私和版权限制使得数据获取困难。

**现有痛点**：现有无数据量化方法通过反转预训练模型生成合成数据，但面临从低维到高维的逆映射困难（1000维→224×224×3），生成质量差且速度慢。

**核心 idea**：利用 Stable Diffusion 的强大生成能力产生逼真合成数据，通过两层过滤确保生成数据与真实数据分布对齐。

## 方法详解

### 关键设计

1. **标签提示数据生成**:

    - 功能：在无数据场景下生成高质量合成训练图像
    - 核心思路：用类别名+CLIP模板形容词生成提示（"A photo of a small hamster"），由 Stable Diffusion v1-5 生成图像。guidance scale设为3.5平衡质量与多样性
    - 设计动机：相比从预训练模型反转图像（低维→高维映射困难），文本到图像模型直接在高维空间生成，避开了维度映射问题

2. **双重过滤机制**:

    - 功能：确保合成数据与真实数据分布对齐
    - 核心思路：
        - 能量分数过滤：用预训练模型的输出logits计算能量分数 $E(\mathbf{x}, f) = -\alpha\sum_{i=1}^C e^{-f_i(\mathbf{x})/\alpha}$，低能量样本更可能是分布内数据。设定阈值筛选
        - BN敏感度过滤（CNN专用）：定义BN敏感度 $S(\mathbf{x}_i) = D_{BN}(\{全批次\}) - D_{BN}(\{去除x_i的批次\})$，移除导致批次BN距离增大的异常图片。关键改进是度量单张图片对整个批次的影响而非单独评估
        - Patch相似性过滤（ViT专用）：计算patch间余弦相似性矩阵的差异熵，选择具有高patch多样性的图像
    - 设计动机：将OOD检测反过来用——筛选分布内(ID)样本，利用预训练模型已有的分布知识

3. **少数据提示优化（Data-Scarce GenQ）**:

    - 功能：有少量真实数据时进一步提升合成质量
    - 核心思路：优化可学习token embedding {S}，提示为"A photo of a {C} in the style of {S}"。将每个类名与对应真实图像配对，通过DDPM损失优化 {S} 使其捕捉整个数据集的风格特征
    - 设计动机：即使只有1-shot真实数据，学到的token也能引导SD生成风格更贴近真实分布的图像

### 损失函数 / 训练策略
PTQ采用逐层重建+学习舍入优化（AdaRound/BRECQ/QDrop风格）。QAT在PTQ基础上引入附加变量 $\mathbf{u}$ 并冻结先前学到的权重和舍入参数，通过STE微调。这种"PTQ→QAT"级联策略从良好初始化出发，稳定训练过程。

## 实验关键数据

### 主实验

| 方法 | 类型 | 4-bit W/A ResNet-50 | 4-bit W/A MBV2 | 说明 |
|------|------|-------------------|---------------|------|
| GenQ (QAT) | Text-to-Image | **76.10%** | **68.53%** | 最优 |
| TexQ (QAT) | GAN | 70.70% | - | 不可跨架构复用 |
| Genie (QAT) | 反转 | 63.10% | - | 生成慢且质量差 |
| Real Data | - | 76.30% | - | 上限 |

### 消融实验

| 过滤策略 | 4-bit Acc | 说明 |
|---------|----------|------|
| 无过滤 | 较低 | 分布偏移严重 |
| 仅能量过滤 | 中等 | 去除明显OOD |
| 能量+BN过滤 | **最优** | 双重保障 |

### 关键发现
- GenQ的4-bit QAT性能(76.10%)几乎追平真实数据(76.30%)，超越现有最强方法5.4%
- 合成数据生成速度比图像反转快15倍，且数据可跨模型架构复用
- 1-shot数据引导的prompt tuning进一步提升数据质量，少量真实数据的引导价值远超预期
- ViT上也有效，BN-free架构使用patch相似性过滤作为替代

## 亮点与洞察
- 开辟了"文本到图像合成→量化"的第三类范式，与现有的"图像反转"和"GAN生成"并列。核心优势是生成质量高、速度快、且数据可复用
- 过滤机制将OOD检测反过来用——筛选分布内样本，思路简洁有效。BN敏感度设计考虑了批次内的交互效应，比逐样本评估更合理
- 从PTQ到QAT的级联初始化策略值得借鉴：好的起点让后续微调更稳定

## 局限与展望
- 依赖 Stable Diffusion 的生成质量，对其未覆盖的类别可能效果不佳
- BN敏感度过滤假设有BN层，不适用于所有架构

## 评分
- 新颖性: ⭐⭐⭐⭐ 首次将扩散模型引入量化数据生成
- 实验充分度: ⭐⭐⭐⭐⭐ PTQ+QAT+CNN+ViT全面覆盖
- 写作质量: ⭐⭐⭐⭐ 方法清晰，消融充分
- 价值: ⭐⭐⭐⭐ 实际部署中数据受限场景非常常见

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] MetaAug: Meta-Data Augmentation for Post-Training Quantization](metaaug_meta-data_augmentation_for_post-training_quantization.md)
- [\[ICCV 2025\] StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data](../../ICCV2025/model_compression/stolenlora_exploring_lora_extraction_attacks_via_synthetic_data.md)
- [\[ICML 2025\] WildChat-50m: A Deep Dive Into the Role of Synthetic Data in Post-Training](../../ICML2025/model_compression/wildchat-50m_a_deep_dive_into_the_role_of_synthetic_data_in_post-training.md)
- [\[ICCV 2025\] Beyond Low-Rank Tuning: Model Prior-Guided Rank Allocation for Effective Transfer in Low-Data and Large-Gap Regimes](../../ICCV2025/model_compression/beyond_low-rank_tuning_model_prior-guided_rank_allocation_for_effective_transfer.md)
- [\[ICCV 2025\] OuroMamba: A Data-Free Quantization Framework for Vision Mamba](../../ICCV2025/model_compression/ouromamba_a_data-free_quantization_framework_for_vision_mamba.md)

</div>

<!-- RELATED:END -->
