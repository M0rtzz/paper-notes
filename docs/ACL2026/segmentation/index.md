---
title: >-
  ACL2026 语义分割方向 4篇论文解读
description: >-
  4篇ACL2026 语义分割论文解读，主题涵盖：提出AnchorSeg，将推理分割重构为基于语言引、BoundRL 将结构化文本分割重新定义为边界生成、本文提出 Hierarchical Policy等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**💬 ACL2026** · **4** 篇论文解读

**[AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation](anchorseg_language_grounded_query_banks_for_reasoning_segmentation.md)**

:   提出AnchorSeg，将推理分割重构为基于语言引导查询库的结构化条件生成过程，通过锚点查询显式解耦空间定位与语义推理，配合Token-Mask循环一致性训练目标，在ReasonSeg上达到SOTA（67.7% gIoU, 68.1% cIoU）。

**[BoundRL: Efficient Structured Text Segmentation through Reinforced Boundary Generation](boundrl_efficient_structured_text_segmentation_through_reinforced_boundary_gener.md)**

:   BoundRL 将结构化文本分割重新定义为边界生成任务——仅生成每个片段的起始 token 而非完整文本，减少 90% 的输出 token 并消除幻觉风险，结合双目标奖励函数和选择性扰动策略的 RLVR 训练，使 1.7B 小模型超越了 Claude-4 Sonnet 的 few-shot 表现。

**[Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](hierarchical_policy_optimization_for_simultaneous_translation_of_unbounded_speec.md)**

:   本文提出 Hierarchical Policy Optimization (HPO)，通过层级奖励设计对基于 LLM 的同声传译模型进行后训练，在翻译质量未达阈值时抑制延迟优化，从而在 1.5 秒延迟下实现 +7 COMET 的翻译质量提升。

**[TemporalVLM: Video LLMs for Temporal Reasoning in Long Videos](temporalvlm_video_llms_for_temporal_reasoning_in_long_videos.md)**

:   本文提出 TemporalVLM，通过时间感知的片段编码器（重叠滑动 Video Q-Former + 融合模块）提取局部细粒度时间特征，再用 BiLSTM 聚合全局长程依赖，首次在 Video LLM 中引入 LSTM，在密集视频描述、时序定位、高光检测和动作分割四项任务上超越先前方法。
