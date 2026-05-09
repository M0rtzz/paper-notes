---
title: >-
  [论文解读] CORDIAL: Can Multimodal Large Language Models Effectively Understand Coherence Relationships?
description: >-
  [ACL 2025][多模态][多模态话语分析] 本文提出 CORDIAL 基准，评估多模态大语言模型在多模态话语分析中理解连贯关系（Coherence Relations）的能力，发现即使顶级模型如 Gemini 1.5 Pro 和 GPT-4o 也无法匹配简单 CLIP 分类器的表现，尤其在语用类关系上差距显著。
tags:
  - ACL 2025
  - 多模态
  - 多模态话语分析
  - 连贯关系
  - 图文关系
  - VLM评估
  - 多模态VLM
---

# CORDIAL: Can Multimodal Large Language Models Effectively Understand Coherence Relationships?

**会议**: ACL 2025  
**arXiv**: [2502.11300](https://arxiv.org/abs/2502.11300)  
**代码**: [https://aashish2000.github.io/CORDIAL/](https://aashish2000.github.io/CORDIAL/)  
**领域**: 多模态VLM  
**关键词**: 多模态话语分析, 连贯关系, 图文关系, VLM评估, 语用推理

## 一句话总结

本文提出 CORDIAL 基准，评估多模态大语言模型在多模态话语分析中理解连贯关系（Coherence Relations）的能力，发现即使顶级模型如 Gemini 1.5 Pro 和 GPT-4o 也无法匹配简单 CLIP 分类器的表现，尤其在语用类关系上差距显著。

## 研究背景与动机

1. **领域现状**：MLLM 在各种下游任务上表现出色，但现有基准主要评估事实和逻辑正确性，缺乏对模态间语用关系和隐含意义的评估。
2. **现有痛点**：现有图文对齐评估使用相似度分数，只关注字面重叠关系，忽略了图文之间更丰富的语用关系（如隐喻、补充、延伸等），无法全面评估 MLLM 的模态间推理能力。
3. **核心矛盾**：人类在日常交流中大量使用跨模态的语用线索（图片与文字各自传达部分信息），但 MLLM 是否能理解这些非字面关系尚不清楚。
4. **本文目标**：系统评估 MLLM 在预测和验证图文连贯关系方面的能力。
5. **切入角度**：借鉴话语连贯理论（Coherence Relations），将图文关系形式化为有限的连贯关系类型。
6. **核心 idea**：用连贯关系预测和验证作为诊断任务，跨三种话语领域评估 MLLM 的模态间推理。

## 方法详解

### 整体框架

CORDIAL 包含三个话语域的数据集（灾害管理 DisRel、社交媒体 Tweet Subtitles、在线文章 CLUE），提供从二分类到多标签的不同粒度连贯关系标注。评估分为预测（给定图文对预测关系）和验证（给定图文对+关系判断正确性）两个任务。

### 关键设计

1. **三层次话语域设计**:

    - 功能：提供不同复杂度的连贯关系评估场景
    - 核心思路：DisRel（二分类：Similar/Complementary）→ Tweet Subtitles（五分类：Insertion/Concretization/Projection/Restatement/Extension）→ CLUE（多标签：Visible/Action/Meta/Subjective/Story），难度递增。
    - 设计动机：不同话语域的连贯关系分类法不同，多域评估可以测试 MLLM 的泛化能力。

2. **CLIP 分类器基线**:

    - 功能：提供基于简单特征的性能参考点
    - 核心思路：使用 CLIP 文本和图像编码器零样本提取多模态嵌入，训练 MLP 分类器预测连贯关系。
    - 设计动机：如果简单分类器就能超越 MLLM，说明数据中有清晰的视觉和文本特征信号，但 MLLM 无法有效利用。

3. **多提示策略评估**:

    - 功能：测试不同提示方法能否帮助 MLLM 更好理解连贯关系
    - 核心思路：评估零样本、少样本和 CoT 三种提示策略，以及微调 Llama 3.2 Vision 模型。
    - 设计动机：了解连贯关系理解是否可以通过提示或微调来改善。

### 损失函数 / 训练策略

基线分类器使用 CLIP 嵌入 + MLP。微调实验使用 Llama 3.2 11B Instruct。

## 实验关键数据

### 主实验

| 方法 | DisRel F1 | Tweet Subtitles F1 | CLUE SL F1 | CLUE ML F1 |
|------|-----------|--------------------|-----------|-----------| 
| CLIP 分类器 | **0.733** | **0.519** | **0.427** | - |
| Claude 3.5 Sonnet | 0.669 | 0.316 | 0.309 | - |
| Gemini 1.5 Pro | 0.699 | 0.271 | 0.296 | - |
| GPT-4o | 0.346 | 0.234 | 0.239 | - |

### 消融实验（微调效果）

| 配置 | DisRel | Tweet Subtitles | CLUE SL | CLUE ML |
|------|--------|----------------|---------|---------|
| Llama 3.2-V 原始 | 0.512 | 0.175 | 0.159 | - |
| 微调后 | +18.42% | 提升 | 提升 | 提升 |

### 关键发现

- MLLM 在所有设置下的 Macro F1 都低于简单 CLIP 分类器
- 语用关系（如 Insertion、Projection、Extension）对 MLLM 特别困难
- 字面关系（Similar、Complementary）的性能差距较小
- 提示策略的效果不一致——没有通用有效的提示方法
- 微调可以缓解模型偏见并提升性能

## 亮点与洞察

- 揭示了 MLLM 的一个重要盲点：它们擅长字面理解但对语用关系把握不足。这对需要深层图文理解的应用有重要启示。
- 简单分类器大幅超越 MLLM 的发现具有警示意义，说明当前 MLLM 的"理解"可能更多是表面的。
- 基准设计跨越三个话语域和多种复杂度，具有较好的系统性。

## 局限与展望

- 目前仅限英语和单轮话语
- 各数据集的连贯关系分类法不同，难以直接跨域比较
- 未来可探索统一的跨域连贯关系分类体系

## 相关工作与启发

- **vs Winoground**: 关注视觉-语言组合性，CORDIAL 更关注语用和话语级的模态间关系
- **vs VLM 对齐基准**: 使用相似度分数，CORDIAL 提供了更细粒度的关系类型评估

## 评分

- 新颖性: ⭐⭐⭐⭐ 首个将连贯关系用于 MLLM 评估的基准
- 实验充分度: ⭐⭐⭐⭐ 12个模型 + 3种提示策略 + 微调实验
- 写作质量: ⭐⭐⭐⭐ 理论背景清晰
- 价值: ⭐⭐⭐⭐ 揭示MLLM语用理解的不足，有启发意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] CORDIAL: Can Multimodal Large Language Models Effectively Understand Coherence Relations?](cordial_can_multimodal_large_language_models_effectively_understand_coherence_re.md)
- [\[ACL 2025\] NegVQA: Can Vision Language Models Understand Negation?](negvqa_can_vision_language_models_understand_negation.md)
- [\[ACL 2025\] Can MLLMs Understand the Deep Implication Behind Chinese Images?](can_mllms_understand_the_deep_implication_behind_chinese_images.md)
- [\[ACL 2025\] Can Multimodal Large Language Models Understand Spatial Relations?](spatialmqa_mllm_spatial_relations.md)
- [\[ACL 2025\] MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](mmmupro_a_more_robust_multidiscipline_multimodal.md)

</div>

<!-- RELATED:END -->
