---
title: >-
  ACL2026 因果推理方向 7篇论文解读
description: >-
  7篇ACL2026 因果推理论文解读，主题涵盖：本文首次为"上下文夹带效应"（contextual、CausalDetox 使用"必要性和充分性概率"、ClimateCause 构建了首个针对气候报告中等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔗 因果推理

**💬 ACL2026** · **7** 篇论文解读

**[Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size](better_and_worse_with_scale_how_contextual_entrainment_diverges_with_model_size.md)**

:   本文首次为"上下文夹带效应"（contextual entrainment）建立缩放定律，发现更大的模型在语义上下文中更能抵抗虚假信息（负指数），但在非语义上下文中更容易复制无关 token（正指数），揭示了语义过滤和机械复制两种功能的对立缩放行为。

**[CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification](causaldetox_causal_head_selection_and_intervention_for_language_model_detoxifica.md)**

:   CausalDetox 使用"必要性和充分性概率"（PNS）作为因果准则来精确定位产生有毒内容的注意力头，并通过局部推理时干预和 PNS 引导的微调两种互补策略进行去毒化，在多个模型上实现最高 5.34% 的毒性降低，同时保持语言流畅性。

**[ClimateCause: Complex and Implicit Causal Structures in Climate Reports](climatecause_complex_and_implicit_causal_structures_in_climate_reports.md)**

:   ClimateCause 构建了首个针对气候报告中复杂和隐式因果结构的专家标注数据集（874 条因果关系），支持嵌套因果、多事件拆解、相关性方向和时空语境标注，并提出基于因果图语义复杂度的可读性度量，LLM 基准测试显示因果链推理仍是重要挑战。

**[Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](dialectic-med_mitigating_diagnostic_hallucinations_via_counterfactual_adversaria.md)**

:   提出 Dialectic-Med，一个受波普尔证伪主义启发的多智能体医学诊断框架，通过提议者（诊断假设）、反对者（视觉证伪模块主动检索矛盾视觉证据）和调解者（加权共识图决策）的对抗辩证推理，在 MIMIC-CXR-VQA、VQA-RAD 和 PathVQA 上取得 SOTA，解释忠实度提升 12.5%，显著缓解诊断幻觉。

**[Imperfectly Cooperative Human-AI Interactions: Comparing the Impacts of Human and AI Attributes in Simulated and User Studies](imperfectly_cooperative_human-ai_interactions_comparing_the_impacts_of_human_and.md)**

:   通过 2000 次 LLM 模拟和 290 人用户研究的双框架实验，比较了人类个性特质和 AI 设计属性在不完全合作场景（招聘谈判、部分诚实交易）中的影响，发现模拟中个性特质主导而真人实验中 AI 透明度才是关键驱动因素。

**[iTAG: Inverse Design for Natural Text Generation with Accurate Causal Graph Annotations](itag_inverse_design_for_natural_text_generation_with_accurate_causal_graph_annot.md)**

:   提出 iTAG 框架，通过逆向设计的三阶段流程（参数化因果图构建→基于 CoT 的概念赋值→结构保持的文本生成）生成同时具有极高因果图标注准确率和文本自然度的数据，可作为真实标注数据的实用替代品进行文本因果发现算法基准测试。

**[Parallel Universes, Parallel Languages: A Comprehensive Study on LLM-based Multilingual Counterfactual Example Generation](parallel_universes_parallel_languages_a_comprehensive_study_on_llm-based_multili.md)**

:   本文系统研究了 LLM 在六种语言上的多语言反事实样本生成能力，通过直接生成和翻译两种路径对比，发现翻译路径的标签翻转率更高但需要更多编辑，识别出四类常见错误模式，并验证多语言反事实数据增强优于跨语言增强，尤其对低资源语言更有效。
