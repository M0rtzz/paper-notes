---
title: >-
  ACL2026 LLM效率方向 7篇论文解读
description: >-
  7篇ACL2026 LLM效率论文解读，主题涵盖：Abstain-R1 提出一种**澄清感知的、提出 BOSCH，一种免训练的注意力头级别、提出 Entropy-guided Token等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM效率

**💬 ACL2026** · **7** 篇论文解读

**[Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL](abstain-r1_calibrated_abstention_and_post-refusal_clarification_via_verifiable_r.md)**

:   Abstain-R1 提出一种**澄清感知的 RLVR 奖励**，在不可回答查询上联合优化"明确拒答"和"拒答后给出有用澄清（指出缺失信息）"，使 3B 模型在拒答和澄清质量上接近甚至超越 DeepSeek-R1 等大模型。

**[BOSCH: Black-Box Binary Optimization for Short-Context Attention-Head Selection in LLMs](bosch_black-box_binary_optimization_for_short-context_attention-head_selection_i.md)**

:   提出 BOSCH，一种免训练的注意力头级别 SWA 混合方法，将 SWA 头选择建模为大邻域搜索问题并分解为三阶段优化（层重要性探测→自适应比例分配→分组头选择），在 4 个模型 4 种比例设置下系统性超越层级启发式和 6 种静态头级别方法。

**[Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens](forget_what_matters_keep_the_rest_selective_unlearning_of_informative_tokens.md)**

:   提出 Entropy-guided Token Weighting (ETW)，利用预测分布的熵值作为 token 信息量的代理指标，选择性地对信息性 token 施加更强的遗忘惩罚，在有效遗忘目标知识的同时更好地保持模型通用能力。

**[HumanLLM: Benchmarking and Improving LLM Anthropomorphism via Human Cognitive Patterns](humanllm_benchmarking_and_improving_llm_anthropomorphism_via_human_cognitive_pat.md)**

:   本文提出 HumanLLM 框架，将 244 个心理学模式（100 个人格特质 + 144 个社会认知模式）建模为相互作用的因果力而非孤立标签，构建了 11,359 个包含 2-5 个模式交互的场景和多轮对话数据集，通过双层 checklist 评估实现与人类判断的高对齐（$r=0.90$），HumanLLM-8B 在多模式动态上以 4 倍小的参数量超越 Qwen3-32B。

**[Multi-Drafter Speculative Decoding with Alignment Feedback](multi-drafter_speculative_decoding_with_alignment_feedback.md)**

:   本文提出 MetaSD，一个将多个异构草稿器整合到推测解码中的统一框架，将草稿器选择建模为多臂赌博机问题，通过块散度（Block Divergence）奖励信号动态选择与目标 LLM 最对齐的草稿器，在黑盒和白盒配置下一致优于单草稿器方法。

**[SciCoQA: Quality Assurance for Scientific Paper–Code Alignment](scicoqa_quality_assurance_for_scientific_paper--code_alignment.md)**

:   本文提出 SciCoQA，首个用于检测科学论文与其代码实现之间差异的基准数据集，包含 635 个差异实例（92 个真实 + 543 个合成），评测 22 个 LLM 后发现最强模型仅能检测 46.7% 的真实差异，揭示了自动化科学质量保证中的关键能力缺口。

**[Speculative Verification: Exploiting Information Gain to Refine Speculative Decoding](speculative_verification_exploiting_information_gain_to_refine_speculative_decod.md)**

:   提出推测验证（Speculative Verification, SV），通过引入与草稿模型同等规模的伴随模型（companion model），利用草稿-伴随分布的相似性预测推测准确率，动态调整验证长度以最大化有效吞吐量，在大批量推理中实现相对标准推测解码平均1.4×、最高1.9×的加速。
