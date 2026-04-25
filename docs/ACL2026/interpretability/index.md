---
title: >-
  ACL2026 可解释性方向 9篇论文解读
description: >-
  9篇ACL2026 可解释性论文解读，主题涵盖：提出一个从大规模新闻语料中自动归纳媒体叙事模式的框、提出 ChemVLR，首个化学领域推理型 VLM、提出 CVA（Context-Value-Acti等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔬 可解释性

**💬 ACL2026** · **9** 篇论文解读

**[A Structured Clustering Approach for Inducing Media Narratives](a_structured_clustering_approach_for_inducing_media_narratives.md)**

:   提出一个从大规模新闻语料中自动归纳媒体叙事模式的框架，通过联合建模事件因果链和角色（英雄/威胁/受害者）信息，使用角色约束的聚类算法将叙事链组织成语义连贯的叙事模式，在移民和枪支控制两个领域生成了可解释且与框架理论一致的叙事模式。

**[ChemVLR: Prioritizing Reasoning in Perception for Chemical Vision-Language Understanding](chemvlr_prioritizing_reasoning_in_perception_for_chemical_vision-language_unders.md)**

:   提出 ChemVLR，首个化学领域推理型 VLM，通过跨模态逆向工程策略构建 760K 推理数据集，结合持续预训练-SFT-RL 三阶段训练流程，在分子识别和反应预测任务上显著超越专有模型和领域专家 VLM。

**[Context-Value-Action Architecture for Value-Driven Large Language Model Agents](context-value-action_architecture_for_value-driven_large_language_model_agents.md)**

:   提出 CVA（Context-Value-Action）架构，基于 S-O-R 心理学模型和 Schwartz 价值理论，通过训练在真实人类数据上的 Value Verifier 解耦行为生成与认知推理，有效缓解 LLM 智能体的行为极化问题，在超过 110 万真实交互轨迹的 CVABench 上显著优于基线。

**[Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations](do_llms_know_tool_irrelevance_demystifying_structural_alignment_bias_in_tool_inv.md)**

:   发现并形式化了 LLM 工具调用中的"结构对齐偏差"——当查询属性可以有效映射到工具参数时（即使工具功能与用户目标无关），LLM 仍倾向调用该工具。构建 SABEval 数据集解耦结构对齐和语义相关性，用对比注意力归因揭示内部存在语义检查和结构匹配两条竞争路径，提出再平衡策略实现 80% 的相对错误减少。

**[Evian: Towards Explainable Visual Instruction-tuning Data Auditing](evian_towards_explainable_visual_instruction-tuning_data_auditing.md)**

:   提出"分解-再评估"（Decomposition-then-Evaluation）范式和 EVIAN 框架，将视觉指令微调数据的回答分解为视觉描述、主观推理和事实声明三个组件，沿图文一致性、逻辑连贯性和事实准确性三个正交维度评估，发现用其筛选的少量高质量数据训练的模型优于大规模数据集训练的模型。

**[Experiments or Outcomes? Probing Scientific Feasibility in Large Language Models](experiments_or_outcomes_probing_scientific_feasibility_in_large_language_models.md)**

:   构建控制知识框架系统研究LLM在科学可行性评估中如何利用实验描述和结果证据，发现提供结果证据比实验描述更可靠，部分实验信息常导致性能低于仅用参数知识的基线，揭示了LLM推理的脆弱性。

**[From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization](from_signal_degradation_to_computation_collapse_uncovering_the_two_failure_modes.md)**

:   本文通过系统的机械可解释性分析，揭示LLM量化存在两种质性不同的失败模式：4-bit的信号退化（Signal Degradation，计算模式完整但精度受损，可局部修复）和2-bit的计算崩溃（Computation Collapse，关键组件功能性破坏，需结构重建）。

**[SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks](spence_a_syntactic_probe_for_detecting_contamination_in_nl2sql_benchmarks.md)**

:   SPENCE 通过对 NL2SQL 基准查询进行系统性句法改写并测量执行准确率随句法距离的衰减程度，检测和量化 LLM 在 NL2SQL 基准上的数据污染行为，发现越老的基准（如 Spider）污染信号越强，而较新的 BIRD 基准几乎不受影响。

**[Tracing Relational Knowledge Recall in Large Language Models](tracing_relational_knowledge_recall_in_large_language_models.md)**

:   本文系统研究LLM在文本生成过程中回忆关系知识的内部机制，发现注意力头对残差流的逐头贡献（$\Delta_{att,h}$）是线性关系分类的最强特征（准确率达91%），并提出HeadScore和TokenScore两种探针归因方法来分解预测到注意力头和源token级别，揭示了探针精度与关系特异性、实体连通度及探针信号集中度之间的明确相关性。
