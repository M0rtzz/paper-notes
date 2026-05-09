---
title: >-
  [论文解读] VSI: Visual-Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding
description: >-
  [CVPR 2026][视频理解][长视频理解] VSI 提出双分支协作检索框架（视频搜索 + 字幕匹配），通过融合视觉和文本信息实现精确的关键帧定位，在文本相关任务中将搜索准确率从29.48提升至45.00，是首个跨模态关键帧检索方法。
tags:
  - CVPR 2026
  - 视频理解
  - 长视频理解
  - 关键帧检索
  - 多模态融合
  - 视频问答
  - 字幕匹配
---

# VSI: Visual-Subtitle Integration for Keyframe Selection to Enhance Long Video Understanding

**会议**: CVPR 2026  
**arXiv**: [2508.06869](https://arxiv.org/abs/2508.06869)  
**代码**: [https://github.com/Jacksonha7/Visual-Subtitle-Integration.git](https://github.com/Jacksonha7/Visual-Subtitle-Integration.git)  
**领域**: 视频理解  
**关键词**: 长视频理解, 关键帧检索, 多模态融合, 视频问答, 字幕匹配

## 一句话总结
VSI 提出双分支协作检索框架（视频搜索 + 字幕匹配），通过融合视觉和文本信息实现精确的关键帧定位，在文本相关任务中将搜索准确率从29.48提升至45.00，是首个跨模态关键帧检索方法。

## 研究背景与动机
1. **领域现状**：多模态大语言模型在视觉-语言任务中表现优异，但处理长视频时受限于输入上下文长度和高计算成本，稀疏帧采样成为必要的预处理步骤。
2. **现有痛点**：（i）现有关键帧搜索算法仅能有效提升视觉强子任务的性能，对文本强子任务改进甚微；（ii）现有方法仅依赖视觉单模态检索，缺乏文本模态的针对性引导，导致关键帧过度聚焦于视觉密集区域而偏离核心语义。
3. **核心矛盾**：VideoQA任务本质上是多模态的（视觉+文本），但现有关键帧检索仅利用视觉模态，存在模态信息利用不充分的问题。
4. **本文目标**：设计多模态关键帧检索框架，使其在文本相关任务上也能有效工作，同时保持视觉任务的性能。
5. **切入角度**：将视频字幕作为互补的文本线索，通过双分支设计融合视觉和文本信息。
6. **核心idea**：视频搜索分支处理视觉特征+目标检测，字幕匹配分支处理语义相似度计算，两者通过动态融合策略更新帧级采样概率。

## 方法详解

### 整体框架
输入视频和查询后，框架初始化帧权重，然后在多次迭代中：（1）视频搜索分支通过目标检测和视觉特征提取进行初步关键帧采样；（2）字幕匹配分支通过查询与字幕的语义相似度计算获取互补文本信息；（3）两个分支的置信度分数通过样条插值融合更新帧级相关概率。迭代结束后，选择得分最高的K帧传递给下游QA任务。

### 关键设计

1. **视频搜索分支（Video Search）**:
    - 功能：基于视觉特征和目标检测进行查询相关的关键帧筛选
    - 核心思路：首先用VLM分析查询识别两类目标——直接相关的Target Objects和提供间接线索的Cue Objects。然后使用YOLO-World高效检测器对采样帧进行检测，计算每帧中检测到的目标与预定义目标集的重叠，得到基于目标的帧分数 $S_{\text{obj}}(t) = \max_{o \in \mathcal{O}_t \cap \mathcal{T}}(s_o \cdot w_o)$。
    - 设计动机：纯视觉特征匹配可能忽略查询的语义意图，通过目标检测可以更精确地定位查询相关的视觉内容。Cue Objects的引入增加了鲁棒性。

2. **字幕匹配分支（Subtitle Match）**:
    - 功能：通过语义相似度检索与查询匹配的字幕片段
    - 核心思路：利用对比学习的文本嵌入模型计算查询与视频字幕之间的语义相似度，将高相似度字幕对应的时间段映射到帧权重。这为文本相关任务提供了视觉搜索无法捕获的信息。
    - 设计动机：许多VideoQA任务的答案隐含在对话或旁白中，纯视觉搜索无法触及这些信息。字幕作为显式的文本模态是天然的互补线索。

3. **动态分数融合**:
    - 功能：融合视觉和文本两个分支的置信度分数
    - 核心思路：对两个分支输出的帧级分数进行归一化后，通过样条插值平滑时间维度上的置信度，然后加权融合更新帧采样概率分布。多轮迭代使分布逐渐聚焦于语义密集区域。
    - 设计动机：简单的分数相加可能导致时间分布不平滑，样条插值保证了时间连续性。

### 损失函数 / 训练策略
即插即用的免训练方法，无需额外训练。搜索模型和编码模型可根据需要灵活替换。

## 实验关键数据

### 主实验

| 数据集/设置 | 指标 | VSI | Uniform Sampling | VSLS | 提升 |
|------------|------|-----|-----------------|------|------|
| LongVideoBench (8帧) | 搜索准确率 | 73.89% | baseline | 次优 | 显著 |
| LongVideoBench 文本任务 (8帧) | Acc | 45.00 | - | 29.48 | +15.52 |
| GPT-4o Long split | Score | 69.57 | 53.76 | - | +15.81 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| Full VSI | 最优 | 双分支完整模型 |
| 仅Video Search | 视觉任务好，文本任务差 | 缺少文本信息 |
| 仅Subtitle Match | 文本任务好，视觉任务差 | 缺少视觉信息 |
| w/o 动态融合 | 下降 | 简单拼接效果不如样条融合 |

### 关键发现
- 在文本相关任务上的提升最为显著（29.48→45.00），证明了字幕匹配分支的价值。
- VSI对不同下游模型（GPT-4o、LLaVA-Video-7B、Qwen2.5-VL-7B）都有一致提升。
- 即使在视觉为主的任务上，双分支融合也优于单独的视觉搜索。

## 亮点与洞察
- **首次将关键帧检索从单模态扩展到多模态**，开辟了新的研究方向。
- **即插即用设计**使得搜索模型和编码模型可灵活替换，通用性强。
- Cue Objects的概念巧妙——提供上下文线索而非直接答案，增加了检索的鲁棒性。

## 局限与展望
- 字幕匹配依赖字幕的可用性和质量，对无字幕视频不适用。
- 多轮迭代的计算开销随视频长度增加。
- 未来可探索更精细的视觉-文本交互机制。

## 相关工作与启发
- **vs TStar**: TStar仅使用视觉目标检测，本文增加了字幕匹配分支，在文本任务上显著更优。
- **vs VSLS**: VSLS建模帧间关系但仍是纯视觉方法，本文引入文本模态实现了跨模态优势。

## 评分
- 新颖性: ⭐⭐⭐⭐ 多模态关键帧检索是新方向，但技术手段相对直接
- 实验充分度: ⭐⭐⭐⭐ 多数据集多模型验证充分
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰，实验分析到位
- 价值: ⭐⭐⭐⭐ 实用价值高，即插即用设计便于落地

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] DIvide, then Ground: Adapting Frame Selection to Query Types for Long-Form Video Understanding](divide_then_ground_adapting_frame_selection_to_query_types_for_long-form_video_u.md)
- [\[CVPR 2026\] Wavelet-based Frame Selection by Detecting Semantic Boundary for Long Video Understanding](wavelet-based_frame_selection_by_detecting_semantic_boundary_for_long_video_unde.md)
- [\[CVPR 2026\] HERBench: A Benchmark for Multi-Evidence Integration in Video Question Answering](herbench_a_benchmark_for_multi-evidence_integration_in_video_question_answering.md)
- [\[CVPR 2026\] Question-guided Visual Compression with Memory Feedback for Long-Term Video Understanding](question-guided_visual_compression_with_memory_feedback_for_long-term_video_unde.md)
- [\[AAAI 2026\] APVR: Hour-Level Long Video Understanding with Adaptive Pivot Visual Information Retrieval](../../AAAI2026/video_understanding/apvr_hour-level_long_video_understanding_with_adaptive_pivot.md)

</div>

<!-- RELATED:END -->
