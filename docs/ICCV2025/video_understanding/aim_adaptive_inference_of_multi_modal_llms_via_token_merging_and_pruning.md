---
title: >-
  [论文解读] AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning
description: >-
  [ICCV 2025][视频理解][token merging] 提出无需训练的自适应推理方法AIM，通过LLM前的迭代token合并（基于嵌入相似度）和LLM层内的渐进式token剪枝（基于PageRank重要性），实现多模态LLM 6.8倍FLOPs降低且几乎不损失性能，在长视频理解上甚至超越SOTA。
tags:
  - ICCV 2025
  - 视频理解
  - token merging
  - 剪枝
  - adaptive inference
  - 多模态
  - training-free
---

# AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning

**会议**: ICCV 2025  
**arXiv**: 无  
**代码**: [GitHub](https://github.com/LaVi-Lab/AIM)  
**领域**: 视频理解  
**关键词**: token merging, token pruning, adaptive inference, multi-modal LLM, training-free

## 一句话总结

提出无需训练的自适应推理方法AIM，通过LLM前的迭代token合并（基于嵌入相似度）和LLM层内的渐进式token剪枝（基于PageRank重要性），实现多模态LLM 6.8倍FLOPs降低且几乎不损失性能，在长视频理解上甚至超越SOTA。

## 研究背景与动机

多模态LLM（如LLaVA-OneVision）依赖大量视觉token（视频可达数千个），导致计算开销巨大，限制了资源受限环境和长视频任务的应用。核心洞察在于视觉数据存在大量固有冗余——保留仅25%的视觉token就能维持接近完整的性能。此外，通过减少每帧token数，LLM可以处理更多帧，弥补长视频中的信息丢失。现有方法（FastV、PDrop、LLaVA-Prumerge）仅在单一位置剪枝或需要微调，缺乏灵活的自适应推理能力。

## 方法详解

### 整体框架

AIM由两个阶段组成：(1) LLM前token合并——基于视觉token间的余弦相似度迭代合并高相似度的token对；(2) LLM层内token剪枝——在每层使用PageRank算法基于注意力权重评估token重要性，按调度器控制的保留比例逐层移除不重要的视觉token。两阶段的参数可调，实现从2.5%到100%的FLOPs的自适应推理。

### 关键设计

1. **迭代Token合并（LLM前）**: 将相邻视觉token分为A、B两组，计算组间成对余弦相似度，找到A中每个token在B中最相似的配对，合并相似度最高的token对（取平均嵌入）。每次迭代最多减半，可迭代多次达到目标保留率。视频中仅在帧内合并——跨帧合并会破坏时序信息。

2. **基于PageRank的渐进式Token剪枝（LLM层内）**: 在每个Transformer层，以注意力权重作为邻接矩阵运行PageRank算法计算每个token的重要性分数。仅剪枝视觉token，保留所有文本token不变（剪枝文本token会严重降低性能）。采用分段线性调度器控制保留比例：l<l₁时保留全部，l₁≤l≤l₂线性递减，l>l₂保留0%视觉token。

3. **关键发现指导的设计原则**: (1) 早期层剪枝视觉token严重影响性能，后期层大量剪枝仍可保持性能——表明LLM在早期层进行跨模态融合，后期层侧重文本推理；(2) 文本token在任何层都不可剪枝；(3) 减少每帧token后可输入更多帧，有利于长视频理解。

### 损失函数 / 训练策略

完全无需训练。基于预训练模型LLaVA-OV-7B（Qwen2 28层）和LLaVA-1.5-7B（Vicuna 32层）直接推理。视频设置：合并保留率25%，l₁=14，l₂=22。图像设置：合并保留率12.5%，l₁=13，l₂=21。

## 实验关键数据

### 主实验

| 方法 | FLOPs(TB) | Prefill时间(ms) | VideoMME | MLVU | EgoSchema |
|------|-----------|----------------|----------|------|-----------|
| LLaVA-OV-7B基线 | 99.63 | 439.58 | 58.2 | 64.7 | 60.1 |
| FastV | 21.24 | 79.56 | 55.9 | 61.1 | 57.5 |
| LLaVA-Prumerge | 23.65 | 86.89 | 57.0 | 60.6 | 61.0 |
| **AIM** | **14.76** | **55.03** | **58.2** | **63.7** | **59.6** |
| AIM(192帧) | 99.27 | 471.20 | 59.2 | **69.3** | 60.8 |

FLOPs降低6.8×，prefill时间降低8.0×，性能几乎无损。192帧时MLVU达69.3(+4.6超基线)。

### 消融实验

- 25%视觉token保留率即可维持接近100%的性能
- 帧内合并优于跨帧合并
- 早期层(l₁=14前)必须保留全部视觉token
- 文本token不可剪枝

### 关键发现

- 多模态LLM的视觉token冗余极高，仅需25%即可
- LLM早期层负责跨模态融合，后期层转向纯文本推理
- token节省可转化为更多帧输入，特别有利于长视频

## 亮点与洞察

- 极简设计（合并+PageRank剪枝）即实现SOTA效率
- 无需训练，即插即用，适配各种多模态LLM
- 自适应推理能力——一个方法覆盖2.5%到100%的FLOPs范围
- 关于LLM层行为的分析（早融合晚推理）对未来MLLM设计有指导意义

## 局限与展望

- PageRank计算本身引入少量额外开销
- 合并策略较简单（仅余弦相似度），可能丢失视觉细节
- 仅在LLaVA系列上验证，对其他架构（如InternVL）的适用性待确认
- 调度器参数(l₁, l₂)需根据不同模型手动调整

## 相关工作与启发

- ToMe（Token Merging）在ViT中的成功被扩展到多模态LLM场景
- FastV、PDrop等视觉token剪枝方法是直接对比基线
- 自适应推理的思路可扩展到3D、音频等更多模态

## 评分

- 新颖性: ⭐⭐⭐ — 合并+剪枝组合的思路较直观
- 技术深度: ⭐⭐⭐⭐ — PageRank应用和调度器设计有创新
- 实验充分性: ⭐⭐⭐⭐⭐ — 视频+图像、6基准、自适应曲线、深入分析
- 写作质量: ⭐⭐⭐⭐ — 条理清晰，发现总结到位
- 实用价值: ⭐⭐⭐⭐⭐ — 无需训练、即插即用、效果显著

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] Multi-modal Multi-platform Person Re-Identification: Benchmark and Method](multi-modal_multi-platform_person_re-identification_benchmark_and_method.md)
- [\[ICCV 2025\] VTimeCoT: Thinking by Drawing for Video Temporal Grounding and Reasoning](vtimecot_thinking_by_drawing_for_video_temporal_grounding_and_reasoning.md)
- [\[ICCV 2025\] Beyond Label Semantics: Language-Guided Action Anatomy for Few-shot Action Recognition](beyond_label_semantics_language-guided_action_anatomy_for_few-shot_action_recogn.md)
- [\[ICCV 2025\] Breaking the Encoder Barrier for Seamless Video-Language Understanding](breaking_the_encoder_barrier_for_seamless_video-language_understanding.md)
- [\[ICCV 2025\] Q-Frame: Query-aware Frame Selection and Multi-Resolution Adaptation for Video-LLMs](q-frame_query-aware_frame_selection_and_multi-resolution_adaptation_for_video-ll.md)

</div>

<!-- RELATED:END -->
