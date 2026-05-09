---
title: >-
  [论文解读] Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in VDU
description: >-
  [CVPR 2026][多模态][LVLM] 通过逐层线性探测分析发现 LVLM 在视觉文档理解中存在内部表示与生成响应之间的显著差距，且中间层比最终层编码了更线性可访问的任务信息，微调中间层可同时提升准确率和缩小差距。
tags:
  - CVPR 2026
  - 多模态
  - LVLM
  - visual document understanding
  - 多模态VLM
  - internal representations
  - intermediate layers
---

# Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in VDU

**会议**: CVPR 2026  
**arXiv**: [2604.04411](https://arxiv.org/abs/2604.04411)  
**代码**: 无  
**领域**: 多模态大模型 / 文档理解  
**关键词**: LVLM, visual document understanding, linear probing, internal representations, intermediate layers

## 一句话总结

通过逐层线性探测分析发现 LVLM 在视觉文档理解中存在内部表示与生成响应之间的显著差距，且中间层比最终层编码了更线性可访问的任务信息，微调中间层可同时提升准确率和缩小差距。

## 研究背景与动机

大型视觉语言模型（LVLMs）在视觉文档理解（VDU）任务上取得了进展，但其性能评估主要依赖生成响应的正确性。然而，响应准确性可能并不完全反映模型是否在内部真正捕获了回答问题所需的信息。

先前研究已暗示内部表示可能包含比生成响应更丰富的信息，但在 LVLM 中逐层分析这一现象以及最具信息量的表示是否出现在最终层还是更早层，都尚未被充分探索。VDU 因需整合多模态和结构化推理，提供了分析多模态信息如何在 LVLM 中表示的理想测试平台。

## 方法详解

### 整体框架

在 LVLM（Qwen2.5-VL 32B、Gemma3 27B、LLaVA-NeXT 13B）的每一层构建线性分类器，评估信息在各层的线性可编码程度，并与模型文本响应准确率对比。

### 关键设计

1. **逐层线性探测**：在每层 LLM 上构建四种分类器（image-token、text-token、all-token、last-token），使用单层线性变换 $\mathbf{z} = W\mathbf{h} + \mathbf{b}$ 将隐藏状态映射到二分类输出，评估各层信息的线性可分性。覆盖四种任务：视觉属性识别（easy-VQA）、文字识别（MJSynth）、结构理解（PubLayNet）、图表理解（FigureQA）。数据集专门选择模型原始生成错误答案的样本（78% 被过滤），确保分析非平凡情况。每个任务 10万训练样本 + 1万测试样本。

2. **差距量化**：系统比较线性探测准确率（衡量内部信息）与文本响应准确率（衡量输出行为），揭示两者之间的差距。发现信息可以被内部线性编码但不一定反映在响应中。

3. **中间层微调策略**：基于线性探测发现，选择性微调中间层而非全部层。实验表明全层微调不足以完全弥合差距，而中间层微调更高效地同时提升线性探测准确率和响应准确率。

### 损失函数 / 训练策略

线性探测使用交叉熵损失训练，LVLM 参数冻结。微调时使用标准 VQA 训练损失。数据集专门选择模型原始生成错误答案的样本，确保分析非平凡情况（78% 的样本被过滤）。

## 实验关键数据

### 主实验

| 模型 | 任务 | 线性探测最优层 | 最优准确率 | 响应准确率 | 差距 |
|------|------|-------------|----------|----------|------|
| Qwen2.5-VL 32B | 图表理解 | 中间层 | ~85% | ~50% | ~35% |
| Gemma3 27B | 结构理解 | 中间层 | ~80% | ~50% | ~30% |

### 关键发现

- 内部表示与生成响应之间存在显著差距：信息已被编码但未被利用
- VDU 任务所需信息在中间层比最终层更线性可访问
- 全层微调不足以弥合差距，中间层微调更有效
- 图像 token 在早中期层包含丰富的任务相关信息

## 亮点与洞察

- 首次在 VDU 领域进行系统的逐层线性探测分析
- "模型知道但不说"的发现具有深刻意义，暗示改善生成策略的潜在方向
- 中间层微调比全层微调更高效的发现有实用价值
- 为理解 LVLM 内部工作机制提供了新视角
- 分析中专门选择模型生成错误答案的样本（78% 被过滤），确保研究非平凡场景
- image-token 在早中期层包含丰富任务相关信息，但在深层被语言先验压制
- 实验覆盖 Qwen2.5-VL 32B、Gemma3 27B、LLaVA-NeXT 13B 三种主流 LVLM

## 局限与展望

- 线性探测仅捕获线性可编码的信息，可能低估非线性编码的信息量
- 微调策略需要先进行探测分析来确定目标层，增加了使用成本
- 差距的根本原因（解码偏差？注意力分配？）需要进一步研究
- 数据构建中仅保留模型生成错误答案的样本，可能引入选择偏差
- 对更复杂的 VDU 任务（如多页文档、表格推理）的扩展性待验证

## 评分

- 新颖性：⭐⭐⭐⭐ — VDU 领域首次逐层分析，揭示内部表示与生成响应的差距
- 技术深度：⭐⭐⭐⭐ — 分析方法系统全面，覆盖 4 种任务、多种 token 类型
- 实验充分度：⭐⭐⭐⭐ — 多模型多任务验证
- 实用价值：⭐⭐⭐ — 中间层微调策略有实用参考，但需先进行探测分析

分析中使用了 10 万训练 + 1 万测试的大规模二分类数据集，确保结果的统计显著性。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] SciPostGen: Bridging the Gap between Scientific Papers and Poster Layouts](scipostgen_bridging_the_gap_between_scientific_papers_and_poster_layouts.md)
- [\[CVPR 2026\] Circuit Tracing in Vision-Language Models: Understanding the Internal Mechanisms of Multimodal Thinking](circuit_tracing_in_vision-language_models_understanding_the_internal_mechanisms_.md)
- [\[ACL 2025\] iNews: A Multimodal Dataset for Modeling Personalized Affective Responses to News](../../ACL2025/multimodal_vlm/inews_a_multimodal_dataset_for_modeling_personalized_affective_responses_to_news.md)
- [\[ICCV 2025\] Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context](../../ICCV2025/multimodal_vlm/why_lvlms_are_more_prone_to_hallucinations_in_longer_responses_the_role_of_conte.md)
- [\[ICCV 2025\] SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs](../../ICCV2025/multimodal_vlm/sparsemm_head_sparsity_emerges_from_visual_concept_responses_in_mllms.md)

</div>

<!-- RELATED:END -->
