---
title: >-
  [论文解读] SemGrasp: Semantic Grasp Generation via Language Aligned Discretization
description: >-
  [ECCV 2024][机器人][semantic grasp generation] 提出 SemGrasp，通过层次化 VQ-VAE 将抓取姿态离散化为三个语义对齐的 token（方向/方式/精修），并微调多模态大语言模型实现基于语言指令的语义抓取生成。
tags:
  - ECCV 2024
  - 机器人
  - semantic grasp generation
  - VQ-VAE
  - MLLM
  - hand-object interaction
  - discrete representation
---

# SemGrasp: Semantic Grasp Generation via Language Aligned Discretization

**会议**: ECCV 2024  
**arXiv**: [2404.03590](https://arxiv.org/abs/2404.03590)  
**代码**: [https://kailinli.github.io/SemGrasp](https://kailinli.github.io/SemGrasp)  
**领域**: 机器人  
**关键词**: semantic grasp generation, VQ-VAE, MLLM, hand-object interaction, discrete representation

## 一句话总结

提出 SemGrasp，通过层次化 VQ-VAE 将抓取姿态离散化为三个语义对齐的 token（方向/方式/精修），并微调多模态大语言模型实现基于语言指令的语义抓取生成。

## 研究背景与动机

- 抓取生成不仅需要考虑物体几何，更需要融入语义信息（如避开热水杯柄的哪一侧）
- 现有方法将抓取表示为连续参数（MANO 模型参数/接触区域），难以嵌入语义信息
- 少数尝试语义抓取的工作仅使用粗粒度的 affordance 向量或视觉语言模型过滤采样
- 人类抓取规划过程：先确定方向 → 再决定方式 → 最后精修细节
- 缺乏大规模的抓取-语言对齐数据集

## 方法详解

### 整体框架

两个核心组件：
1. **抓取离散化**：层次化 VQ-VAE 将抓取编码为三个 token <o, m, r>
2. **抓取感知语言模型**：基于 Vicuna-7B 微调 MLLM，统一物体、抓取和语言三个模态

### 关键设计

**1. 层次化抓取离散化（Hierarchical VQ-VAE）**

- 将抓取 G = (T, θ, β) 分解为三个层次化 token：
    - **方向 token <o>**：编码手的全局变换 T（旋转+平移），反映物体功能和意图
    - **方式 token <m>**：编码局部手姿态 θ 和形状 β，对应抓取分类法中的 33 种类型
    - **精修 token <r>**：编码残差参数 ΔT, Δθ, Δβ，确保物理合理性
- 条件依赖：<o> 独立 → <m> 条件于 <o> → <r> 条件于 <o, m>
- 码本 B 含 K=512 个条目，每个维度 d_B=256
- 编码器用 PointBERT 提取手和物体点云特征
- 解码器使用 6D 旋转表示

**2. 抓取感知语言模型**

- 输入三个模态：
    - 抓取模态：VQ-VAE 编码的 <grasp> token（<SG>, o, m, r, <EG>）
    - 物体模态：PointBERT 提取物体特征 → 线性投影层映射到语言空间
    - 语言模态：SentencePiece 分词的文本
- 两阶段训练：
  1. 多模态对齐：训练预测 grasp token，更新物体投影层和嵌入层
  2. 指令微调：优化复杂输出的生成质量，冻结投影层
- 使用 LoRA（rank=64）微调约 6% 参数

**3. CapGrasp 数据集**

- 基于 OakInk 数据集扩展，约 1.8K 物体模型、50K 抓取对
- 三层标注：
    - 低级：手指-物体部件接触状态（距离阈值 3mm）
    - 高级：操作意图和抓取力（GPT-4/GPT-4V 生成）
    - 对话：GPT-4 生成的多轮对话标注
- 每对平均 5 条详细描述

### 损失函数 / 训练策略

- VQ-VAE 损失：L_rec（手顶点重建）+ L_emb（嵌入损失）+ L_com（承诺损失）
- MLLM 损失：负对数似然 L_NLL = -Σ log p(x̂_i | x̂_{<i}, x)
- 学习率：多模态对齐阶段 5e-4，指令微调阶段 3e-5
- 4×A100 80GB GPU，batch size 128，训练 20 epoch

## 实验关键数据

### 主实验

| 方法 | MPVPE ↓ | PD ↓ | SIV ↓ | SD mean ↓ |
|------|---------|------|-------|-----------|
| GrabNet | 27.49 | 0.54 | 3.45 | 1.77 |
| GrabNet w/ TTA | 27.16 | 0.49 | 2.16 | 1.35 |
| **Ours** | **14.97** | **0.46** | **2.72** | 2.14 |
| **Ours w/ TTA** | 23.61 | **0.37** | **1.27** | 1.90 |

MPVPE 降低 45%，渗透深度降低 15%。

### 消融实验

| 变体 | MPVPE ↓ |
|------|---------|
| w/o refinement token | 20.36 |
| w/ refinement token | **14.97** |

精修 token 带来 26% 的 MPVPE 改善和 9% 的 SIV 改善。

### 关键发现

- 离散表示的可控性：固定 <o, m> token 可在不同形状的杯子上生成一致的抓取方向和方式
- 对比 cVAE（GrabNet）：固定采样向量 z=0 生成不可解释的结果
- GPT-4 辅助语义一致性评分：SemGrasp 显著优于 BERT baseline
- 语义一致性感知评分（PS）4.2/5.0，证明生成抓取的自然性

## 亮点与洞察

1. **语义-几何统一**：三个 token 的层次化设计完美模拟人类抓取规划过程
2. **离散化的多重优势**：与语言空间对齐、可控可解释、降低学习复杂度
3. **首个语义抓取大数据集 CapGrasp**：涵盖低级到高级的完整标注体系
4. 将 MLLM 引入抓取生成是新颖的交叉研究思路
5. 层次化 VQ-VAE 的设计理念可推广到其他手-物交互任务

## 局限性 / 可改进方向

- 仅支持 MANO 手模型的抓取生成，不支持灵巧手/机器人手爪
- 码本大小 K=512 可能不足以表示所有抓取变化
- GPT-4 生成的高级标注存在幻觉问题，需手动审核
- 物理仿真中的稳定性（SD 指标）仍有改进空间

## 相关工作与启发

- **GrabNet**: cVAE 基线方法
- **LLaVA**: MLLM 架构设计的参考
- **MotionGPT**: 将运动序列 token 化融入 LLM 的先驱
- 启发：离散化+LLM 是统一多模态理解和生成的通用范式

## 评分

| 维度 | 分数 (1-10) |
|------|-----------|
| 新颖性 | 9 |
| 技术深度 | 9 |
| 实验充分性 | 8 |
| 实用价值 | 8 |
| 写作质量 | 8 |
| 总体评分 | 8.4 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Decomposed Vector-Quantized Variational Autoencoder for Human Grasp Generation](decomposed_vector-quantized_variational_autoencoder_for_human_grasp_generation.md)
- [\[ECCV 2024\] An Economic Framework for 6-DoF Grasp Detection](an_economic_framework_for_6-dof_grasp_detection.md)
- [\[ECCV 2024\] Prioritized Semantic Learning for Zero-Shot Instance Navigation](prioritized_semantic_learning_for_zeroshot_instance_navigation.md)
- [\[ECCV 2024\] Octopus: Embodied Vision-Language Programmer from Environmental Feedback](octopus_embodied_visionlanguage_programmer_from_environmental_feedback.md)
- [\[ECCV 2024\] LLM as Copilot for Coarse-Grained Vision-and-Language Navigation](llm_as_copilot_for_coarse-grained_vision-and-language_navigation.md)

</div>

<!-- RELATED:END -->
