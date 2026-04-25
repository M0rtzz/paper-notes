---
title: >-
  ACL2026 LLM安全方向 7篇论文解读
description: >-
  7篇ACL2026 LLM安全论文解读，主题涵盖：AGSC 提出了一个针对长文本生成的不确定性量化框、本文提出利用采样生成的"未来上下文"（后续句子）来、提出知识坐标条件化预训练（KoCo）等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔒 LLM安全

**💬 ACL2026** · **7** 篇论文解读

**[AGSC: Adaptive Granularity and Semantic Clustering for Uncertainty Quantification in Long-text Generation](agsc_adaptive_granularity_and_semantic_clustering_for_uncertainty_quantification.md)**

:   AGSC 提出了一个针对长文本生成的不确定性量化框架，通过 NLI 中立概率触发自适应粒度分解（减少 60% 推理时间），并使用 GMM 软聚类捕捉潜在语义主题进行主题感知的加权聚合，在 BIO 和 LongFact 基准上达到 SOTA 的事实性相关性。

**[Enhancing Hallucination Detection via Future Context](enhancing_hallucination_detection_via_future_context.md)**

:   本文提出利用采样生成的"未来上下文"（后续句子）来增强黑盒场景下的幻觉检测，利用幻觉一旦出现就倾向于持续传播的"滚雪球效应"，在 SelfCheckGPT 和 SC 等多种采样方法上一致提升检测性能。

**[KoCo: Conditioning Language Model Pre-training on Knowledge Coordinates](koco_conditioning_language_model_pre-training_on_knowledge_coordinates.md)**

:   提出知识坐标条件化预训练（KoCo），将每个文档映射为三维语义坐标（来源、内容、稳定性），作为文本前缀注入预训练，使模型获得显式的上下文感知能力，在 10 个下游任务上提升性能、加速收敛约 30%，并有效缓解幻觉。

**[Masked by Consensus: Disentangling Privileged Knowledge in LLM Correctness](masked_by_consensus_disentangling_privileged_knowledge_in_llm_correctness.md)**

:   本文通过对比自探针（使用模型自身隐藏状态）和外部探针（使用其他模型隐藏状态）预测正确性的能力，发现"模型间一致性"是掩盖特权知识的关键混淆因子，在消除一致性后揭示了领域特异性的特权知识：事实性任务中存在但数学推理中不存在。

**[Maximizing Local Entropy Where It Matters: Prefix-Aware Localized LLM Unlearning](maximizing_local_entropy_where_it_matters_prefix-aware_localized_llm_unlearning.md)**

:   本文提出 PALU（Prefix-Aware Localized Unlearning），从时间和词表两个维度实现局部化的熵最大化遗忘：在时间维度仅对敏感前缀 token 施加遗忘目标，在词表维度仅对 top-K logits 进行平坦化，以最小的参数扰动实现高效遗忘并保持模型通用能力。

**[MeasHalu: Mitigation of Scientific Measurement Hallucinations for LLMs](meashalu_mitigation_of_scientific_measurement_hallucinations_for_large_language_.md)**

:   本文提出MeasHalu框架，通过细粒度测量幻觉分类法和两阶段优化（推理感知SFT+幻觉靶向GRPO奖励）缓解LLM在科学测量抽取中的幻觉，在MeasEval上显著超越基线。

**[Why Supervised Fine-Tuning Fails to Learn: A Systematic Study of Incomplete Learning in Large Language Models](why_supervised_fine-tuning_fails_to_learn_a_systematic_study_of_incomplete_learn.md)**

:   本文首次系统研究了 SFT 中的"不完全学习现象"（ILP）——即模型收敛后仍无法正确复现部分训练数据，识别了五种反复出现的原因（知识缺失、知识冲突、数据内部矛盾、左侧遗忘、不充分优化），并提出诊断框架和针对性缓解策略。
