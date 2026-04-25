---
title: >-
  ACL2026 因果推理方向 4篇论文解读
description: >-
  4篇ACL2026 因果推理论文解读，主题涵盖：本文首次为"上下文夹带效应"（contextual、CausalDetox 使用"必要性和充分性概率"、ClimateCause 构建了首个针对气候报告中等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔗 因果推理

**💬 ACL2026** · **4** 篇论文解读

**[Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size](better_and_worse_with_scale_how_contextual_entrainment_diverges_with_model_size.md)**

:   本文首次为"上下文夹带效应"（contextual entrainment）建立缩放定律，发现更大的模型在语义上下文中更能抵抗虚假信息（负指数），但在非语义上下文中更容易复制无关 token（正指数），揭示了语义过滤和机械复制两种功能的对立缩放行为。

**[CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification](causaldetox_causal_head_selection_and_intervention_for_language_model_detoxifica.md)**

:   CausalDetox 使用"必要性和充分性概率"（PNS）作为因果准则来精确定位产生有毒内容的注意力头，并通过局部推理时干预和 PNS 引导的微调两种互补策略进行去毒化，在多个模型上实现最高 5.34% 的毒性降低，同时保持语言流畅性。

**[ClimateCause: Complex and Implicit Causal Structures in Climate Reports](climatecause_complex_and_implicit_causal_structures_in_climate_reports.md)**

:   ClimateCause 构建了首个针对气候报告中复杂和隐式因果结构的专家标注数据集（874 条因果关系），支持嵌套因果、多事件拆解、相关性方向和时空语境标注，并提出基于因果图语义复杂度的可读性度量，LLM 基准测试显示因果链推理仍是重要挑战。

**[Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](dialectic-med_mitigating_diagnostic_hallucinations_via_counterfactual_adversaria.md)**

:   提出 Dialectic-Med，一个受波普尔证伪主义启发的多智能体医学诊断框架，通过提议者（诊断假设）、反对者（视觉证伪模块主动检索矛盾视觉证据）和调解者（加权共识图决策）的对抗辩证推理，在 MIMIC-CXR-VQA、VQA-RAD 和 PathVQA 上取得 SOTA，解释忠实度提升 12.5%，显著缓解诊断幻觉。
