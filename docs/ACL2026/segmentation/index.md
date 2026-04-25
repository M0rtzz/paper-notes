---
title: >-
  ACL2026 语义分割方向 2篇论文解读
description: >-
  2篇ACL2026 语义分割论文解读，主题涵盖：提出AnchorSeg，将推理分割重构为基于语言引、本文提出 Hierarchical Policy等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**💬 ACL2026** · **2** 篇论文解读

**[AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation](anchorseg_language_grounded_query_banks_for_reasoning_segmentation.md)**

:   提出AnchorSeg，将推理分割重构为基于语言引导查询库的结构化条件生成过程，通过锚点查询显式解耦空间定位与语义推理，配合Token-Mask循环一致性训练目标，在ReasonSeg上达到SOTA（67.7% gIoU, 68.1% cIoU）。

**[Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](hierarchical_policy_optimization_for_simultaneous_translation_of_unbounded_speec.md)**

:   本文提出 Hierarchical Policy Optimization (HPO)，通过层级奖励设计对基于 LLM 的同声传译模型进行后训练，在翻译质量未达阈值时抑制延迟优化，从而在 1.5 秒延迟下实现 +7 COMET 的翻译质量提升。
