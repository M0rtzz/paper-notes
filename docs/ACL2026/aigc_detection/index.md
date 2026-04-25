---
title: >-
  ACL2026 AIGC检测方向 8篇论文解读
description: >-
  8篇ACL2026 AIGC检测论文解读，主题涵盖：提出 RACE（Rhetorical、BiasedTales-ML 构建了约 35、CiteGuard 提出了一个检索增强的智能体框架等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔎 AIGC检测

**💬 ACL2026** · **8** 篇论文解读

**[Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection](beyond_the_final_actor_modeling_the_dual_roles_of_creator_and_editor_for_fine-gr.md)**

:   提出 RACE（Rhetorical Analysis for Creator-Editor Modeling），利用修辞结构理论(RST)构建逻辑图来建模文本"创作者"的思维架构，同时提取篇章单元级特征捕获"编辑者"的语言风格，实现四类细粒度 LLM 生成文本检测（人写/LLM写/LLM润色人文/人改写LLM文）。

**[BIASEDTALES-ML: A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories](biasedtales-ml_a_multilingual_dataset_for_analyzing_narrative_attribute_distribu.md)**

:   BiasedTales-ML 构建了约 35 万篇覆盖 8 种语言的 LLM 生成儿童故事语料库，通过全排列提示设计和分布分析框架，揭示了**叙事中社会属性分布在不同语言间存在显著差异**，英语中心的评估无法反映多语言场景下的偏见模式。

**[CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation](citeguard_faithful_citation_attribution_for_llms_via_retrieval-augmented_validat.md)**

:   CiteGuard 提出了一个检索增强的智能体框架，通过扩展的检索动作（包括全文搜索和上下文检索）为科学引用归属提供更忠实的基础，在 CiteME 基准上相对基线提升 10 个百分点，达到 68.1% 准确率，接近人类表现（69.2%）。

**[DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects](dia-harm_dialectal_disparities_in_harmful_content_detection_across_50_english_di.md)**

:   本文构建 DIA-HARM，首个跨 50 种英语方言评估虚假信息检测鲁棒性的基准，揭示人类撰写的方言内容导致检测性能下降 1.4-3.6% F1，微调 Transformer 大幅优于零样本 LLM（96.6% vs 78.3%），且部分模型在混合内容上出现超过 33% 的灾难性退化。

**[FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation](flexguard_continuous_risk_scoring_for_strictness-adaptive_llm_content_moderation.md)**

:   FlexGuard 提出了一种输出连续风险评分（0-100）而非二元安全/不安全判断的 LLM 审核模型，通过基于评分准则的蒸馏和 GRPO 风险对齐训练，在不同严格度部署场景下实现了 SOTA 的鲁棒性和准确率。

**[Reasoning-Based Refinement of Unsupervised Text Clusters with LLMs](reasoning-based_refinement_of_unsupervised_text_clusters_with_llms.md)**

:   提出基于推理的聚类精炼框架，将 LLM 作为语义判官（而非嵌入生成器）验证和重构无监督聚类的输出，通过一致性验证、冗余裁决和标签接地三个推理阶段，在社交媒体语料上显著提升聚类一致性和人类对齐的标注质量。

**[Temporal Flattening in LLM-Generated Text: Comparing Human and LLM Writing Trajectories](temporal_flattening_in_llm-generated_text_comparing_human_and_llm_writing_trajec.md)**

:   本文通过构建跨12年的纵向写作数据集，发现LLM生成文本存在"时间扁平化"现象——虽然词汇多样性高，但在语义和认知情感维度上的时间漂移显著低于人类，仅凭时间变异模式就能以94%准确率区分人类与LLM文本。

**[Who Wrote This Line? Evaluating the Detection of LLM-Generated Classical Chinese Poetry](who_wrote_this_line_evaluating_the_detection_of_llm-generated_classical_chinese_.md)**

:   本文构建了首个面向LLM生成古典中文诗词的检测基准ChangAn（含30,664首诗），系统评估了12种AI检测方法在不同文本粒度和生成策略下的表现，揭示了当前中文文本检测器在古典诗词领域的严重局限性。
