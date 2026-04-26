---
title: >-
  [论文解读] How Should Video LLMs Output Time? An Analysis of Efficient Temporal Grounding Paradigms
description: >-
  [CVPR 2026][视频理解][视频时序定位] 本文在统一框架下对比了视频时序定位的三种主流时间输出范式（文本数字生成、时间token生成、连续时间解码），发现连续分布范式在效率-精度帕累托前沿上始终表现最优。
tags:
  - CVPR 2026
  - 视频理解
  - 视频时序定位
  - 多模态大语言模型
  - 时间输出范式
  - 效率分析
  - 紧凑模型
---

# How Should Video LLMs Output Time? An Analysis of Efficient Temporal Grounding Paradigms

**会议**: CVPR 2026  
**arXiv**: [2604.08966](https://arxiv.org/abs/2604.08966)  
**代码**: https://tg-paradigms.github.io/  
**领域**: 视频理解  
**关键词**: 视频时序定位, 多模态大语言模型, 时间输出范式, 效率分析, 紧凑模型

## 一句话总结

本文在统一框架下对比了视频时序定位的三种主流时间输出范式（文本数字生成、时间token生成、连续时间解码），发现连续分布范式在效率-精度帕累托前沿上始终表现最优。

## 研究背景与动机

**领域现状**：视频时序定位（VTG）是连接语言查询与视频时间片段的核心任务。多模态大语言模型（MLLM）已成为该任务的主流骨干，但各种方法在时间输出设计上分歧巨大——有的直接生成文本时间戳，有的引入专用时间token，有的通过连续解码预测时间分布。

**现有痛点**：每种范式都使用自己的骨干、数据集和训练协议，导致无法将性能差异归因于输出设计本身。此外，随着VTG系统向资源受限的边缘设备部署，缺乏系统性的效率-精度权衡分析。

**核心矛盾**：输出范式的选择对定位精度和计算成本的影响尚不明确，特别是在紧凑模型（0.5B-8B）上。

**本文目标**：在相同骨干、数据和训练协议下公平对比三种范式的精度和效率。

**切入角度**：选择SmolVLM2（0.5B/2.2B）、FastVLM（1.5B）和Molmo2（4B/8B）作为紧凑骨干，确保唯一变量是输出范式。

**核心idea**：连续分布范式在帕累托前沿上实现了最优的效率-精度权衡，具有最低的延迟开销和鲁棒的定位精度。

## 方法详解

### 整体框架

本文实现了三种代表性范式：TRACE风格的时间token生成（Gen）、DisTime风格的连续分布解码（Cont）和VTimeLLM风格的文本数字生成（Text），在1.2M训练样本和三个评测基准上进行统一比较。

### 关键设计

1. **文本数字生成范式（Text）**:

    - 功能：将时间边界作为纯文本数字生成，直接复用LLM的原生词表
    - 核心思路：将目标时间格式化为自然语言模板（如"from 52.0 to 63.0 seconds"），使用标准下一token预测损失 $\mathcal{L}_{text} = -\sum_j \log P(w_j | w_{<j}, I, F)$
    - 设计动机：无需架构修改，但时间语义与通用数字token纠缠，可能限制精度

2. **时间token生成范式（Gen）**:

    - 功能：引入专用时间token创建独立的时间表示空间
    - 核心思路：采用TRACE的因果事件建模框架，每个事件 $e_k=(t_k, s_k, c_k)$ 包含时间戳、显著性分数和描述。使用13个字符级token的独立tokenizer和任务特定交叉熵损失
    - 设计动机：显式解耦时间坐标与自然语言，保留视频事件的内在结构

3. **连续时间解码范式（Cont）**:

    - 功能：将时间定位建模为概率分布估计
    - 核心思路：引入可学习的⟨TIME_STAMP⟩token，通过轻量MLP将其隐状态解码为时间分布。将连续时间空间离散为 $reg_{max}+1$ 个bin，最终时间预测为加权期望：$\hat{t}_s = \sum_i e_{st}^{(i)} \cdot a_i$
    - 设计动机：自然建模预测不确定性，缓解主观边界标注的歧义性，参数开销最小

### 损失函数 / 训练策略

所有范式使用相同的LoRA微调协议（r=32），相同的1.2M训练数据。Gen范式使用任务特定交叉熵，Cont范式使用1D-IoU回归损失+分布焦点损失，Text范式使用标准语言建模损失。

## 实验关键数据

### 主实验

| 基准/范式 | 指标 | Text | Gen | Cont |
|--------|------|------|------|------|
| Charades-STA (SmolVLM2-2.2B) | R1@0.5 | 中等 | 较高 | 最高 |
| QVHighlights (SmolVLM2-2.2B) | R1@0.5 | 中等 | 较高 | 最高 |
| YouCook2 (SmolVLM2-2.2B) | CIDEr | 最高 | 较高 | - |

### 消融实验

| 配置 | 推理延迟 | 参数开销 | 说明 |
|------|---------|------|------|
| Text范式 | 高（自回归） | 无额外 | 多步生成增加延迟 |
| Gen范式 | 中（结构化解码） | 中等 | 额外encoder-decoder对 |
| Cont范式 | 最低 | 最小（3层MLP） | 单步解码，无自回归 |

### 关键发现

- 连续分布范式在大多数骨干和任务组合上实现最优精度-效率权衡
- Text范式受限于自回归生成，推理延迟显著高于其他范式
- Gen范式在需要同时输出时间和显著性分数的任务上有独特优势（如QVHighlights的mAP指标）
- 输出范式的选择对紧凑模型的影响被放大，强调了在资源受限场景下选择正确范式的重要性

## 亮点与洞察

- **首次公平的跨范式对比**：通过严格控制除输出范式外的所有变量，首次隔离了输出设计对VTG性能的因果影响
- **紧凑模型的放大效应**：在小模型上架构选择的影响更为显著，为边缘部署提供了关键的设计指导
- **连续分布范式的效率优势**：单步解码避免了自回归的累积延迟，参数开销仅为3层MLP，且自然处理边界歧义

## 局限与展望

- 仅评估了0.5B-8B的紧凑模型，未包含7B+的大规模骨干
- 训练数据格式化不可避免地存在范式特异性，可能引入微妙的偏差
- 未探索范式组合或混合策略的可能性

## 相关工作与启发

- **vs TRACE**: 本文在统一框架下复现了TRACE的因果事件建模，证明其结构化解码在某些任务上有优势但效率偏低
- **vs DisTime**: 分布解码范式在效率和精度上的双重优势得到了跨骨干的验证

## 评分

- 新颖性: ⭐⭐⭐ 实证研究为主，方法设计沿用已有工作
- 实验充分度: ⭐⭐⭐⭐⭐ 5个骨干×3种范式×3个基准，非常全面
- 写作质量: ⭐⭐⭐⭐ 结构清晰，实验设计严谨
- 价值: ⭐⭐⭐⭐ 为VTG系统设计提供了客观的经验指导

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] CVA: Context-aware Video-text Alignment for Video Temporal Grounding](cva_context-aware_video-text_alignment_for_video_temporal_grounding.md)
- [\[CVPR 2026\] SlotVTG: Object-Centric Adapter for Generalizable Video Temporal Grounding](slotvtg_object-centric_adapter_for_generalizable_video_temporal_grounding.md)
- [\[CVPR 2026\] Cluster-Wise Spatio-Temporal Masking for Efficient Video-Language Pretraining](cluster-wise_spatio-temporal_masking_for_efficient_video-language_pretraining.md)
- [\[ACL 2026\] ArrowGEV: Grounding Events in Video via Learning the Arrow of Time](../../ACL2026/video_understanding/arrowgev_grounding_events_in_video_via_learning_the_arrow_of_time.md)
- [\[CVPR 2026\] LensWalk: Agentic Video Understanding by Planning How You See in Videos](lenswalk_agentic_video_understanding_by_planning_how_you_see_in_videos.md)

<!-- RELATED:END -->
