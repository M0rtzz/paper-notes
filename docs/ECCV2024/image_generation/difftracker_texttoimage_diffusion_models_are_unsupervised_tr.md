---
title: >-
  [论文解读] Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers
description: >-
  [ECCV 2024][图像生成][unsupervised tracking] 首次将预训练T2I扩散模型（Stable Diffusion）应用于无监督视觉跟踪，通过初始提示学习器在cross-attention图上激活目标区域、在线提示更新器融合长短期运动信息动态适应目标运动，在5个基准上全面超越此前最优无监督跟踪器（TrackingNet Success 0.675, VOT2018 EAO 0.365）。
tags:
  - ECCV 2024
  - 图像生成
  - unsupervised tracking
  - 扩散模型
  - 提示学习
  - 注意力机制
  - motion information
---

# Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers

**会议**: ECCV 2024  
**arXiv**: [2407.08394](https://arxiv.org/abs/2407.08394)  
**代码**: 无  
**领域**: 视觉目标跟踪 / 扩散模型应用  
**关键词**: unsupervised tracking, diffusion model, prompt learning, cross-attention, motion information

## 一句话总结

首次将预训练T2I扩散模型（Stable Diffusion）应用于无监督视觉跟踪，通过初始提示学习器在cross-attention图上激活目标区域、在线提示更新器融合长短期运动信息动态适应目标运动，在5个基准上全面超越此前最优无监督跟踪器（TrackingNet Success 0.675, VOT2018 EAO 0.365）。

## 研究背景与动机

**领域现状**：深度学习跟踪器依赖大量标注数据进行监督训练。无监督跟踪方法（UDT、s²siamfc、USOT、ULAST）基于Siamese结构，利用前向-后向一致性或对抗掩码进行自监督学习。

**现有痛点**：(1) 无监督方法难以充分利用视频帧的**语义信息和空间结构**；(2) 视频帧间**上下文关系**利用不足；(3) 目标运动过程中外观变化大，固定跟踪模板难以适应。

**核心矛盾**：T2I扩散模型拥有丰富的视觉语义理解能力，但其设计目标是图像生成而非目标跟踪。

**本文要解决什么？** 利用T2I扩散模型中蕴含的语义和结构知识进行无监督视觉跟踪。

**切入角度**：cross-attention图能激活与文本prompt语义相关的区域——学到代表跟踪目标的prompt embedding就能定位目标。

**核心idea一句话**：学习可优化prompt embedding使其在SD的cross-attention图上激活目标区域，通过融合长短期运动信息在线更新prompt适应目标运动。

## 方法详解

### 整体框架

第一帧+目标框 → 初始提示学习器（冻结SD + 可优化prompt + attention harmonization → 初始prompt $p_1$）→ 后续帧：在线提示更新器（运动信息提取 + blend head → 更新prompt $p_k$）→ cross-attention图 → 最小包围框。

### 关键设计

1. **初始提示学习器 + Attention Harmonization**

    - 将第一帧编码加噪送入UNet，学习prompt $p_1$ 使cross-attention图 $M_c$ 激活目标区域
    - self-attention增强：$M_c'(:,:) = \sum_i \sum_j M_c(i,j) \cdot M_s(i,j,:,:)$
    - 融合：$\mathcal{M} = (1-\alpha) \cdot M_c' + \alpha \cdot M_c$，$\alpha=0.5$
    - 损失：$L = \|\mathcal{M} - \mathcal{F}_1\|_2^2 + L_{DM}$，GT map为bbox内均匀激活
    - 设计动机：self-attention编码像素间语义关系（目标-背景关系），有助遮挡/形变场景

2. **在线提示更新器**

    - **运动信息提取**：两个ResNet18+Conv3D编码器分别提取短期（2帧）和长期（T帧）运动信息
    - cross-attention融合目标外观与运动信息：$l_k^L = \text{Cross-Attn}(Q_k, m_k^L)$，$l_k^S = \text{Cross-Attn}(Q_k, m_k^S)$
    - MLP融合长短期信息：$l_k = \text{MLP}(l_k^L, l_k^S)$
    - 残差更新：$p_k = (1-\beta) \cdot \mathcal{H}_b(p_{k-1} + l_k) + \beta \cdot p_{k-1}$，$\beta=0.7$
    - 设计动机：短期运动可能因遮挡/光照变化而不可靠，长期信息提供鲁棒时空连续性

### 损失函数 / 训练策略

- 伪标签：光流模型在GOT-10k、ImageNet VID、LaSOT、YouTube-VOS上生成
- 扩散模型全程冻结，仅学prompt embedding和更新器参数
- 初始prompt：Adam，lr=5e-3，3 epochs
- 在线更新器：Adam，lr=5e-4，35 epochs；输入512×512，attention map 64×64

## 实验关键数据

### 主实验

在5个跟踪基准上的对比（Ours均为无监督）：

| 方法 | 类型 | TrackingNet Suc↑ | Pre↑ | NPre↑ | VOT2016 EAO↑ | VOT2018 EAO↑ |
|------|------|-----------------|------|-------|-------------|-------------|
| SiamFC | 有监督 | 0.571 | 0.533 | 0.663 | 0.235 | 0.188 |
| SiamRPN++ | 有监督 | 0.733 | 0.694 | 0.800 | - | 0.414 |
| DiMP | 有监督 | 0.740 | 0.687 | 0.801 | - | 0.440 |
| USOT* | 无监督 | 0.616 | 0.566 | 0.691 | 0.402 | 0.344 |
| ULAST*-on | 无监督 | 0.654 | 0.592 | 0.732 | 0.417 | 0.355 |
| **Diff-Tracker** | **无监督** | **0.675** | **0.614** | **0.751** | **0.430** | **0.365** |

VOT2016/2018详细指标：

| 方法 | VOT2016 Acc↑ | Rob↓ | VOT2018 Acc↑ | Rob↓ |
|------|-------------|------|-------------|------|
| ULAST*-on | 0.603 | 0.214 | 0.571 | 0.286 |
| **Diff-Tracker** | **0.605** | **0.206** | **0.580** | **0.273** |

### 消融实验

| 组件 | 效果描述 |
|------|---------|
| 仅cross-attention $M_c$ | 基线 |
| + attention harmonization | 编码目标-背景关系，提升遮挡鲁棒性 |
| + 仅短期运动更新 | 提升prompt适应性，但遮挡场景不稳定 |
| + 长短期运动融合 | 最优，增强时空连续性 |

### 关键发现

- 5个基准上全面超越此前最优无监督跟踪器ULAST
- TrackingNet Success +2.1%（0.654→0.675），VOT2018 EAO +1.0%（0.355→0.365）
- 部分指标接近有监督方法（VOT2016 EAO 0.430接近DaSiamRPN的0.411）
- 扩散模型在未经视频数据训练的情况下展现视频上下文理解能力

## 亮点与洞察

- 首次将T2I扩散模型的cross-attention用于无监督目标跟踪，开创新范式
- attention harmonization融合self/cross-attention，用像素关系丰富跟踪线索
- 长短期运动融合的在线更新设计合理，适应目标外观动态变化
- 证明扩散模型内化的视觉语义知识可迁移到非生成任务

## 局限性 / 可改进方向

- 跟踪速度受限于扩散模型推理开销，实时性不足（论文未报告FPS）
- GT attention map为简单bbox激活，未利用更精细的目标掩码
- 在长时间跟踪（LaSOT）上与有监督方法差距仍较大（0.405 vs 0.495）
- 与同期扩散特征跟踪方法（DiffusionTrack）缺乏对比

## 相关工作与启发

- **vs ULAST/USOT**：Siamese无监督跟踪器，Diff-Tracker用扩散模型替代Siamese作为特征骨干
- **vs prompt learning**：类似textual inversion思路，但用于定位而非生成
- **vs 扩散模型分割**：与VPD等用扩散特征做分割的工作思路一致，扩展到视频跟踪
- 启发：cross-attention是强大的语义定位工具，可迁移到更多定位任务

## 评分

- 新颖性: ⭐⭐⭐⭐ 首次将T2I扩散模型用于无监督跟踪
- 实验充分度: ⭐⭐⭐⭐ 5个基准数据集全面评测
- 写作质量: ⭐⭐⭐⭐ 方法动机和设计逻辑清晰
- 价值: ⭐⭐⭐ 概念验证有意义，但受限于扩散模型推理速度

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] UDiffText: A Unified Framework for High-quality Text Synthesis in Arbitrary Images via Character-aware Diffusion Models](udifftext_a_unified_framework_for_high-quality_text_synthesis_in_arbitrary_image.md)
- [\[ECCV 2024\] Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](be_yourself_bounded_attention_for_multisubject_texttoimage_g.md)
- [\[ECCV 2024\] ColorPeel: Color Prompt Learning with Diffusion Models via Color and Shape Disentanglement](colorpeel_color_prompt_learning_with_diffusion_models_v.md)
- [\[ECCV 2024\] ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation](scaledreamer_scalable_textto3d_synthesis_with_asynchronous_s.md)
- [\[ECCV 2024\] Prompting Future Driven Diffusion Model for Hand Motion Prediction](prompting_future_driven_diffusion_model_for_hand_motion_prediction.md)

</div>

<!-- RELATED:END -->
