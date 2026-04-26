---
title: >-
  [论文解读] CORAL: Disentangling Latent Representations in Long-Tailed Diffusion
description: >-
  [NeurIPS 2025][图像生成][扩散模型] 本文发现扩散模型在长尾数据上训练时，U-Net 瓶颈层的潜在表征出现"表征纠缠"——尾部类别与头部类别特征空间严重重叠，并提出 CORAL 方法通过在瓶颈层添加投影头和监督对比损失，促进类别间潜在表征分离，显著提升尾部类别生成质量和多样性。
tags:
  - NeurIPS 2025
  - 图像生成
  - 扩散模型
  - 长尾分布
  - 对比学习
  - 潜在空间解耦
  - U-Net瓶颈层
---

# CORAL: Disentangling Latent Representations in Long-Tailed Diffusion

**会议**: NeurIPS 2025  
**arXiv**: [2506.15933](https://arxiv.org/abs/2506.15933)  
**代码**: [GitHub](https://github.com/SankarLab/coral-lt-diffusion)  
**领域**: 图像生成  
**关键词**: 扩散模型, 长尾分布, 对比学习, 潜在空间解耦, U-Net瓶颈层

## 一句话总结
本文发现扩散模型在长尾数据上训练时，U-Net 瓶颈层的潜在表征出现"表征纠缠"——尾部类别与头部类别特征空间严重重叠，并提出 CORAL 方法通过在瓶颈层添加投影头和监督对比损失，促进类别间潜在表征分离，显著提升尾部类别生成质量和多样性。

## 研究背景与动机

1. **领域现状**: 扩散模型在类别平衡数据上表现出色，但真实世界数据常呈长尾分布。

2. **现有痛点**: 长尾分布下扩散模型对尾部类别生成质量差、多样性低，存在"特征借用"问题（尾部样本显示头部类别特征）。

3. **核心矛盾**: 现有方法（CBDM、T2H、DiffROP）主要在图像空间或外部潜在空间操作，未关注去噪网络内部潜在空间的类别纠缠问题。

4. **本文目标**: 识别并解决扩散模型内部潜在空间中的表征纠缠。

5. **切入角度**: U-Net 瓶颈层输出承载语义信息，是表征纠缠发生的关键位置。

6. **核心 idea**: 在 U-Net 瓶颈层添加轻量投影头，用监督对比损失促进类别分离——在表征纠缠发生的位置直接干预。

## 方法详解

### 整体框架
在标准 DDPM + CFG 训练流程基础上，增加两个组件：(1) 瓶颈层后的投影头 MLP；(2) 投影嵌入上的监督对比损失。总损失 $\mathcal{L}_{CORAL} = \mathcal{L}_{diff} + \lambda(t) \cdot \mathcal{L}_{con}$。投影头为单层全连接+归一化，训练后丢弃，零推理开销。在 CIFAR10-LT（ρ=0.01和0.001）、CIFAR100-LT（ρ=0.01）、CelebA-5（64×64）和 ImageNet-LT（64×64, 1000类）五个设置上评估。

### 关键设计

1. **投影头设计**:
    - 功能: 解耦对比目标与扩散特征
    - 核心思路: 在 U-Net 编码器瓶颈输出后添加单层全连接 + 归一化的投影头 $f_\phi$
    - 设计动机: 投影头防止对比损失直接坍缩瓶颈层的类内多样性；训练后丢弃投影头，零额外推理开销

2. **时间依赖权重函数**:
    - 功能: 动态调节对比损失在不同去噪时间步的影响
    - 核心思路: $\lambda(t) = w \cdot \exp(\frac{1-t/T}{\tau_r})$，在早期时间步（低噪声、$t \approx 0$）赋予更大权重
    - 设计动机: 语义结构在低噪声阶段更可恢复，高噪声阶段噪声主导无法有效学习类别分离

3. **监督对比损失（SupCon）**:
    - 功能: 促进同类聚集、异类分离
    - 核心思路: 对投影瓶颈特征 $\mathbf{z}$ 应用 SupCon 损失，使用原始（未 mask 的）类别标签
    - 设计动机: 在表征纠缠发生的瓶颈层直接施加类别分离约束，比图像空间方法更直接

### 损失函数 / 训练策略
- 基础: DDPM 噪声预测损失 + CFG（$p_{uncond}$ 概率丢弃标签）
- 附加: SupCon 损失，$\tau_{SC} \in [0.5, 1.0]$
- 推理时完全标准，投影头不参与

## 实验关键数据

### 主实验

| 数据集 | 方法 | FID ↓ | IS ↑ | Recall ↑ |
|--------|------|-------|------|----------|
| CIFAR10-LT (ρ=0.01) | DDPM | 6.17 | 9.43 | 0.52 |
| CIFAR10-LT (ρ=0.01) | CBDM | 5.62 | 9.28 | 0.57 |
| CIFAR10-LT (ρ=0.01) | **CORAL** | **5.32** | **9.69** | **0.59** |
| CIFAR100-LT (ρ=0.01) | DDPM | 7.70 | 13.20 | 0.50 |
| CIFAR100-LT (ρ=0.01) | **CORAL** | **5.37** | **13.53** | **0.59** |
| ImageNet-LT | DDPM | 17.08 | 21.03 | 0.39 |
| ImageNet-LT | **CORAL** | **16.11** | **24.17** | **0.48** |

### 关键发现
- 表征纠缠是长尾扩散失败的根因，而非简单的数据不足
- t-SNE 可视化清晰展示 CORAL 前后的类别分离效果
- Per-class FID 分析显示 CORAL 在尾部类别上改善最显著
- 潜在空间干预优于图像空间干预（DiffROP 风格）
- ImageNet-LT（1000 类）上优势最明显（FID 16.11 vs DDPM 17.08, IS 24.17 vs 21.03, Recall 0.48 vs 0.39），说明方法可扩展
- CelebA-5（64×64）上也有效：FID 8.12 vs DDPM 10.28，Recall 0.59 vs 0.52
- CBDM 在 ImageNet-LT 上 FID 反而恶化（22.66 vs 17.08），因为图像空间正则化在类别数多时失效；CORAL 的潜在空间干预不受类别数影响
- 生成样本可视化分析：CBDM 的郁金香类出现模式坍缩（小花+过多草地背景，借自头部动物类），T2H 的郁金香形似其他花类，CORAL 则保持了正确的尺度和结构

## 亮点与洞察
- 首次识别并命名扩散模型中的"表征纠缠"现象
- 巧妙利用投影头的"信息瓶颈"效应保护瓶颈层类内多样性
- 推理时零额外开销，完全兼容标准扩散采样
- 方法简洁但效果显著，实现投入产出比高
- 时间依赖权重函数$\lambda(t) = w \cdot \exp(\frac{1-t/T}{\tau_r})$在低噪声阶段（$t \approx 0$）赋予更大权重，因为语义结构在此阶段更可恢复，高噪声阶段噪声主导无法有效学习类别分离

## 局限与展望
- 仅在 U-Net 架构上验证，未扩展到 DiT 等新架构
- 未验证在文本到图像生成等更复杂场景
- 与 LoRA 微调等参数高效方法的结合有待探索
- 对比温度参数需要调整
- 数据集分辨率有限（32×32、64×64），高分辨率场景效果待验证
- 投影头的架构选择（层数、维度）对性能的影响需更多分析
- 平衡数据集上的可视化实验证实表征纠缠主要源于类别不平衡而非数据不足，为CORAL的设计动机提供了实验支撑
- 未来可探索将CORAL应用于LoRA微调的预训练扩散模型，在数据不平衡的专业领域（如医学影像、科学可视化）中确保稀有概念不被常见概念纠缠

## 相关工作与启发
- **vs CBDM**: CBDM 在图像空间正则化平衡采样，CORAL 在潜在空间直接解耦。CBDM 在 ImageNet-LT 上 FID 恶化至 22.66（DDPM 17.08），CORAL 降至 16.11。
- **vs T2H**: T2H 用贝叶斯门控机制从头部到尾部迁移知识，CORAL 更直接且表现更稳定（ImageNet-LT IS: CORAL 24.17 vs T2H 19.15）。
- **vs DiffROP**: DiffROP 在图像空间用 KL 对比，CORAL 在瓶颈层用 SupCon，作用位置更精准

## 评分

### 实现细节
基于DDPM+CFG训练流程，投影头为单层FC+归一化，训练后丢弃。
SupCon温度$tau_{SC} in [0.5, 1.0]$，权重函数温度$tau_r$控制时间依赖。
在CIFAR10/100-LT、CelebA-5、ImageNet-LT（64×64）上评估。
- 新颖性: ⭐⭐⭐⭐ 表征纠缠的发现和潜在空间干预方案有新意
- 实验充分度: ⭐⭐⭐⭐ 4 个数据集、多指标、消融完整
- 写作质量: ⭐⭐⭐⭐ 分析清晰，可视化丰富
- 价值: ⭐⭐⭐⭐ 对长尾生成和扩散模型训练有实际价值

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge](towards_general_modality_translation_with_contrastive_and_predictive_latent_diff.md)
- [\[NeurIPS 2025\] A Gradient Flow Approach to Solving Inverse Problems with Latent Diffusion Models](a_gradient_flow_approach_to_solving_inverse_problems_with_latent_diffusion_model.md)
- [\[NeurIPS 2025\] BlurDM: A Blur Diffusion Model for Image Deblurring](blurdm_a_blur_diffusion_model_for_image_deblurring.md)
- [\[NeurIPS 2025\] Encoder-Decoder Diffusion Language Models for Efficient Training and Inference](encoder-decoder_diffusion_language_models_for_efficient_training_and_inference.md)
- [\[NeurIPS 2025\] When Are Concepts Erased From Diffusion Models?](when_are_concepts_erased_from_diffusion_models.md)

<!-- RELATED:END -->
