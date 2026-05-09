---
title: >-
  [论文解读] FALIP: Visual Prompt as Foveal Attention Boosts CLIP Zero-Shot Performance
description: >-
  [ECCV 2024][3D视觉][CLIP] 提出 FALIP（Foveal-Attention CLIP），通过在 CLIP 的多头自注意力模块中插入类似人眼中央凹的注意力掩码，在不修改原始图像内容的前提下引导模型关注特定区域，显著提升指代表达理解、图像分类和 3D 点云识别等零样本任务的性能。
tags:
  - ECCV 2024
  - 3D视觉
  - CLIP
  - 零样本学习
  - 视觉提示
  - 注意力机制
  - 区域感知
---

# FALIP: Visual Prompt as Foveal Attention Boosts CLIP Zero-Shot Performance

**会议**: ECCV 2024  
**arXiv**: [2407.05578](https://arxiv.org/abs/2407.05578)  
**代码**: [https://pumpkin805.github.io/FALIP/](https://pumpkin805.github.io/FALIP/)  
**领域**: 3D视觉  
**关键词**: CLIP, 零样本学习, 视觉提示, 注意力机制, 区域感知

## 一句话总结

提出 FALIP（Foveal-Attention CLIP），通过在 CLIP 的多头自注意力模块中插入类似人眼中央凹的注意力掩码，在不修改原始图像内容的前提下引导模型关注特定区域，显著提升指代表达理解、图像分类和 3D 点云识别等零样本任务的性能。

## 研究背景与动机

### 核心矛盾

**核心矛盾**：视觉提示的悖论**：红圈、模糊等视觉提示能引导 CLIP 注意力到特定区域，但不可避免地破坏了图像原始信息

### 领域现状

**领域现状**：RedCircle 引入额外红色元素 → 影响细粒度分类

### 现有痛点

**现有痛点**：Blur mask 模糊大部分背景 → 丢弃关键细节

### 解决思路

**解决思路**：在图像分类任务上，视觉提示反而降低了零样本准确率

### 补充说明

**补充说明**：核心发现**：视觉提示的有效性本质上源于其改变了模型注意力，而非修改图像内容

### 补充说明

**补充说明**：核心问题**：能否在不改变图像内容的情况下，获得视觉提示引导注意力的好处？

## 方法详解

### 整体框架

FALIP = 原始 CLIP + 注意力掩码注入。输入原始图像和注意力区域（ROA），生成 foveal attention mask，注入 ViT 的多头自注意力层。

### 关键设计

**1. Foveal Attention Mask 生成**
- 对 ROA 区域生成高斯加权的注意力掩码：
  $R_{i,j} = e^{-\frac{[i-(H'-1)/2]^2 + [j-(W'-1)/2]^2}{2\sigma^2}}$
- 归一化并缩放：$R^{norm} = \alpha \times \frac{R - \text{Min}(R) + \epsilon}{\text{Max}(R) - \text{Min}(R) + \epsilon}$
- 仅对 [CLS] token 的行赋非零值（第一行），其余行为零

**2. 注意力注入机制**
- 将掩码 M 加到注意力分数上：
  $\text{Foveal-Attention}(Q,K,V) = \text{Softmax}(\frac{QK^T}{\sqrt{d}} + M) V$
- 核心直觉：模拟人眼中央凹视觉特征——对焦区域高分辨率感知，周围区域衰减

**3. 仅修改 [CLS] 行的设计选择**
- CLIP 最终使用 [CLS] token 进行图像-文本匹配
- 只需引导 [CLS] token 更关注 ROA 区域即可，无需改变其他 token 之间的交互

### 损失函数 / 训练策略

- **完全免训练（train-free）**：不引入任何可学习参数
- 无额外计算开销（仅增加掩码加法操作）
- 即插即用，可与现有视觉提示方法叠加使用

## 实验关键数据

### 主实验（指代表达理解 RefCOCO/+/g）

| 方法 | RefCOCO TestA | RefCOCO TestB | RefCOCO+ TestA | RefCOCOg Test |
|------|---------------|---------------|----------------|---------------|
| RedCircle(gold) | 41.6 | 36.2 | 44.7 | 45.4 |
| PASTA(gold) | 41.7 | 37.6 | 43.2 | 49.2 |
| **FALIP(gold)** | **44.2** | **39.4** | **46.8** | **51.5** |

With Ensemble + Post-processing：FALIP 超越现有方法约 3%。

### 图像分类（零样本）

| 方法 | StanfordDogs | CUB-200 | ImageNet-S | Waterbirds |
|------|-------------|---------|------------|------------|
| Original CLIP | 56.5 | 54.2 | 64.9 | 78.2 |
| RedCircle | 52.4 | 44.2 | 62.8 | 77.5 |
| Blur | 51.9 | 39.1 | 53.8 | 78.1 |
| **FALIP** | **58.3** | **54.3** | **67.3** | **79.7** |

### 关键发现

- **FALIP 在分类任务上提升准确率**（+1.8~+2.4%），而 RedCircle 和 Blur 均降低准确率
- 在 REC 任务上，FALIP 可与 RedCircle 叠加使用进一步提升性能
- 3D 点云识别上也有 +1.4% 的平均提升
- 不同注意力头对视觉提示的敏感度差异显著，调整特定头可"释放"视觉提示潜力

## 亮点与洞察

1. **深入揭示视觉提示的工作机制**——其成功本质是改变注意力，而非图像编辑
2. **训练免费+即插即用**：不修改图像、不增加模型参数、不需要训练
3. 发现 CLIP 不同注意力头对视觉提示的敏感性差异（可调整头以增强效果）
4. 类人视觉的 foveal attention 设计直觉清晰且具有生物学基础

## 局限与展望 / 可改进方向

- 高斯掩码的 σ 和 α 参数需要手动调整，不同任务可能需要不同设置
- 仅实验了 ViT-B/16 架构，更大模型和不同架构的效果待验证
- ROA 的获取仍依赖外部检测器或标注框
- 在 Waterbirds 等特殊分类任务上提升有限（该数据集分类依赖背景）

## 相关工作与启发

- RedCircle、CPT 等视觉提示方法开创了该方向，但存在图像污染问题
- Alpha-CLIP、RegionCLIP 等方法需要额外训练数据，本方法完全免训练
- 可启发：将 foveal attention 扩展到视频理解中的时空注意力引导

## 评分

- 新颖性：⭐⭐⭐⭐（免训练注意力注入思路新颖）
- 技术深度：⭐⭐⭐
- 实验充分度：⭐⭐⭐⭐（REC + 分类 + 3D + 消融）
- 写作质量：⭐⭐⭐⭐
- 综合推荐：⭐⭐⭐⭐

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Zero-Shot Multi-Object Scene Completion](zero-shot_multi-object_scene_completion.md)
- [\[ECCV 2024\] ZeST: Zero-Shot Material Transfer from a Single Image](zest_zero-shot_material_transfer_from_a_single_image.md)
- [\[ECCV 2024\] TPA3D: Triplane Attention for Fast Text-to-3D Generation](tpa3d_triplane_attention_for_fast_text-to-3d_generation.md)
- [\[ECCV 2024\] NGP-RT: Fusing Multi-Level Hash Features with Lightweight Attention for Real-Time Novel View Synthesis](ngp-rt_fusing_multi-level_hash_features_with_lightweight_attention_for_real-time.md)
- [\[ECCV 2024\] Track Everything Everywhere Fast and Robustly](track_everything_everywhere_fast_and_robustly.md)

</div>

<!-- RELATED:END -->
