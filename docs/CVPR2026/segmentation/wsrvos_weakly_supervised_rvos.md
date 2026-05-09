---
title: >-
  [论文解读] Weakly-Supervised Referring Video Object Segmentation through Text Supervision
description: >-
  [CVPR 2026][图像分割][弱监督] 提出 WSRVOS，首个仅使用文本表达式作为监督信号的弱监督指称视频目标分割框架，通过 MLLM 驱动的对比表达式增强、双向视觉-语言特征选择、实例感知表达式分类和时序分段排序约束，显著减少了对像素级标注的依赖。
tags:
  - CVPR 2026
  - 图像分割
  - 弱监督
  - 视频目标分割
  - 指称表达
  - 文本监督
  - 多模态对齐
---

# Weakly-Supervised Referring Video Object Segmentation through Text Supervision

**会议**: CVPR 2026  
**arXiv**: [2604.17797](https://arxiv.org/abs/2604.17797)  
**代码**: [https://github.com/viscom-tongji/WSRVOS](https://github.com/viscom-tongji/WSRVOS)  
**领域**: 分割  
**关键词**: 弱监督, 视频目标分割, 指称表达, 文本监督, 多模态对齐

## 一句话总结

提出 WSRVOS，首个仅使用文本表达式作为监督信号的弱监督指称视频目标分割框架，通过 MLLM 驱动的对比表达式增强、双向视觉-语言特征选择、实例感知表达式分类和时序分段排序约束，显著减少了对像素级标注的依赖。

## 研究背景与动机

**领域现状**：指称视频目标分割（RVOS）根据文本表达式在视频中分割目标实例。主流方法（如 ReferFormer、SAMWISE）依赖像素级 mask 标注进行监督学习，效果出色但标注成本极高。

**现有痛点**：弱监督 RVOS 的探索刚起步——已有工作如 WRVOS 使用首帧 mask + 后续帧 bbox，OCPG 使用 bbox/point 标注生成伪 mask。但 bbox 和 point 标注仍需大量逐帧人工标注，在长视频中依然成本不菲。

**核心矛盾**：如何在不提供任何空间标注（mask、bbox、point）的前提下，仅通过文本表达式让模型学会定位和分割视频中的目标实例？挑战在于：(1) 视觉和语言特征的异质性使语义对齐困难；(2) 视频的时序动态和遮挡进一步复杂化对齐过程。

**本文目标**：设计端到端的弱监督 RVOS 框架，训练时仅使用文本表达式作为监督信号，无需任何空间标注。

**切入角度**：多模态大语言模型（MLLM）如 Qwen3-VL 的字幕生成能力可以为视频生成丰富的正负文本描述，提供远超原始简短表达式的监督信号。通过对比学习让模型区分正确和错误的描述，间接学习定位能力。

**核心 idea**：用 MLLM 生成对比表达式增强数据（正面丰富描述 + 硬负面描述），通过实例感知分类和伪 mask 融合来训练分割模型，全程不使用空间标注。

## 方法详解

### 整体框架

框架包含五个部分：(1) 对比表达式增强——用 Qwen3-VL 生成正负文本表达式；(2) 多模态特征选择与交互——双向选择相关的视觉和语言特征；(3) 实例感知表达式分类——区分正面和负面表达式；(4) 正面预测融合——生成伪 mask 作为额外监督；(5) 时序分段排序约束——约束时间相邻帧的 mask 重叠关系。

### 关键设计

1. **对比指称表达式增强**:

    - 功能：从简单的原始表达式扩展出丰富的正面和硬负面文本监督信号
    - 核心思路：正面表达式：用 Qwen3-VL 基于视频和原始表达式生成 P 个更详细的描述（关注外观、动作、交互关系），用 InternVideo2 计算视频-文本相似度并过滤低置信度（$c^k < 0.8$）的描述，与原始表达式拼接保留原始信息。负面表达式：用 Qwen3-VL 修改目标实例的类别、属性、动作等生成 N 个语义上似是而非但与目标不一致的描述
    - 设计动机：原始数据集的表达式过于简单，缺乏细粒度语义细节。正面增强提供更丰富的对齐信号，硬负面迫使模型学习更具区分性的表示。MLLM 仅离线用于数据增强，不参与推理

2. **双向视觉-语言特征选择与实例感知分类**:

    - 功能：过滤视频中与表达式无关的视觉信息和文本中的非信息词，实现精细多模态对齐
    - 核心思路：双向选择互相高度相关的视觉和语言特征子集，然后基于 Multiple Instance Learning 思想进行 proposal 聚合和表达式匹配，让模型学会区分正面表达式和负面表达式
    - 设计动机：视频的时序动态使视觉特征包含大量与指称表达式无关的冗余信息，文本也可能包含介词等无关词。双向过滤后的精简特征更容易实现精确对齐

3. **正面预测融合与时序排序约束**:

    - 功能：生成高质量伪 mask 提供空间监督，同时约束时序一致性
    - 核心思路：将多个正面表达式的预测结果融合为可靠的伪 mask，作为额外的监督信号训练分割。时序分段排序约束要求时间相邻帧的 mask 重叠度高于远帧，鼓励时序平滑性：$\text{IoU}(m_t, m_{t+\delta_1}) > \text{IoU}(m_t, m_{t+\delta_2})$ 当 $\delta_1 < \delta_2$
    - 设计动机：仅靠分类损失难以提供精确的空间定位信号。伪 mask 融合利用了"多个正确描述的预测应该一致"的直觉来提取可靠区域。时序排序约束利用视频的时间连续性先验

### 损失函数 / 训练策略

包含三部分：实例感知表达式分类损失（区分正负文本）、伪 mask 监督损失（空间定位）、时序分段排序损失（时序一致性）。MLLM 仅在训练数据预处理时离线使用。

## 实验关键数据

### 主实验

| 数据集 | 指标 | WSRVOS(本文) | OCPG(点监督) | 差距 |
|--------|------|-------------|-------------|------|
| A2D-Sentences | mAP | 最优 | 基线 | 显著超越 |
| J-HMDB Sentences | J&F | 最优 | 基线 | 显著超越 |
| Ref-YouTube-VOS | J&F | 最优 | 基线 | 显著超越 |
| Ref-DAVIS17 | J&F | 最优 | 基线 | 显著超越 |

### 消融实验

| 配置 | 性能变化 | 说明 |
|------|---------|------|
| Full WSRVOS | 最优 | 完整模型 |
| w/o 对比表达式增强 | 下降 | 监督信号不够丰富 |
| w/o 双向特征选择 | 下降 | 对齐精度降低 |
| w/o 正面预测融合 | 下降 | 缺少空间监督信号 |
| w/o 时序排序约束 | 下降 | 时序一致性变差 |

### 关键发现

- 仅用文本监督的 WSRVOS 超越了使用 bbox/point 标注的弱监督方法 OCPG，说明丰富的文本监督信号比稀疏的空间标注更有效
- 对比表达式增强的贡献最大——硬负面的区分性和正面的丰富性都很重要
- 时序排序约束在长视频上效果更明显，短视频中相邻帧差异小故贡献有限

## 亮点与洞察

- "无需任何空间标注"的设定在 RVOS 领域是一个重大跨步。利用 MLLM 的描述能力将文本从"弱监督"变为"丰富监督"，这个思路非常有前瞻性
- 正面预测融合策略巧妙：如果模型对多个正确描述的预测高度一致，那么这些区域大概率就是目标——用"预测的一致性"作为伪标签的可靠性度量
- 时序排序约束的设计简洁且有效，不需要精确的帧间 mask 传播，只需要"近帧更相似"的软约束

## 局限与展望

- 依赖 MLLM (Qwen3-VL) 生成表达式的质量，如果 MLLM 对视频理解有误会引入噪声
- InternVideo2 的过滤阈值 0.8 是手工设定的，对不同域可能需要调整
- 在目标实例小或高度遮挡的场景中，纯文本监督的定位能力可能不足
- 未来可探索自适应的表达式生成和过滤策略，或结合视觉 grounding 预训练增强定位

## 相关工作与启发

- **vs WRVOS**: 需要首帧 mask + bbox，WSRVOS 完全不需要空间标注
- **vs OCPG**: 使用 bbox/point 生成伪 mask，但 WSRVOS 仅用文本反而性能更好
- **vs TRIS/PCNet (图像级)**: 图像级弱监督指称分割方法，WSRVOS 扩展到更困难的视频场景

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首个纯文本监督的 RVOS 方法，范式创新
- 实验充分度: ⭐⭐⭐⭐ 四个数据集验证，消融全面
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰，方法描述系统
- 价值: ⭐⭐⭐⭐⭐ 大幅降低 RVOS 的标注成本，实用价值极高

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning](fcl-cod_weakly_supervised_camouflaged_object_detection_with_frequency-aware_and_.md)
- [\[AAAI 2026\] SSR: Semantic and Spatial Rectification for CLIP-based Weakly Supervised Segmentation](../../AAAI2026/segmentation/ssr_semantic_and_spatial_rectification_for_clip-based_weakly_supervised_segmenta.md)
- [\[CVPR 2026\] Combining Boundary Supervision and Segment-Level Regularization for Fine-Grained Action Segmentation](boundary_segment_action_segmentation.md)
- [\[CVPR 2026\] Follow the Saliency: Supervised Saliency for Retrieval-augmented Dense Video Captioning](follow_the_saliency_supervised_saliency_for_retrieval-augmented_dense_video_capt.md)
- [\[ICCV 2025\] ReferDINO: Referring Video Object Segmentation with Visual Grounding Foundations](../../ICCV2025/segmentation/referdino_referring_video_object_segmentation_with_visual_grounding_foundations.md)

</div>

<!-- RELATED:END -->
