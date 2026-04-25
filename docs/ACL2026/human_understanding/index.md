---
title: >-
  ACL2026 人体理解方向 39篇论文解读
description: >-
  39篇ACL2026 人体理解论文解读，主题涵盖：提出ConvAgent，通过将RL训练奖励分解为结、提出 Plan-RewardBench、提出 DYPO（Dynamic Policy等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**💬 ACL2026** · **39** 篇论文解读

**[Agentic Conversational Search with Contextualized Reasoning via Reinforcement Learning](agentic_conversational_search_with_contextualized_reasoning_via_reinforcement_le.md)**

:   提出ConvAgent，通过将RL训练奖励分解为结果奖励、信息增益奖励和混合主动行为奖励三个互补组件，训练对话式搜索智能体在多轮交互中交替进行搜索和推理。

**[Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling](aligning_agents_via_planning_a_benchmark_for_trajectory-level_reward_modeling.md)**

:   提出 Plan-RewardBench，一个面向复杂工具增强场景的轨迹级偏好基准，用于评估奖励模型在多步规划、工具使用和错误恢复等场景下区分优劣智能体轨迹的能力。

**[Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning](bridging_sft_and_rl_dynamic_policy_optimization_for_robust_reasoning.md)**

:   提出 DYPO（Dynamic Policy Optimization），通过动态难度分级将样本路由到不同优化路径——Hard样本用多教师蒸馏降低SFT偏差、Mid样本用Group Alignment Loss降低RL方差，在数学推理benchmark上平均提升4.8%，OOD任务提升13.3%。

**[CAP: Controllable Alignment Prompting for Unlearning in LLMs](cap_controllable_alignment_prompting_for_unlearning_in_llms.md)**

:   提出 CAP 框架，通过训练轻量 SLM 生成可控的提示前缀来引导冻结的 LLM 选择性遗忘目标知识，无需修改模型参数，实现了可逆、可迁移的 LLM 知识遗忘。

**[ChipSeek: Optimizing Verilog Generation via EDA-Integrated Reinforcement Learning](chipseek_optimizing_verilog_generation_via_eda-integrated_reinforcement_learning.md)**

:   ChipSeek 提出了一个将 EDA 工具链直接集成到训练循环中的分层奖励 RL 框架，通过课程引导的动态策略优化（CDPO）使 LLM 能够生成同时满足功能正确性和 PPA（功耗-性能-面积）优化的 RTL 代码，在标准基准上达到 SOTA。

**[Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors](compiling_activation_steering_into_weights_via_null-space_constraints_for_stealt.md)**

:   本文提出 STEEREDIT，将动态激活转向编译为静态权重修改的后门注入框架，通过提取顺从方向并利用零空间约束确保仅在触发词存在时激活，在多个安全对齐 LLM 上实现高攻击成功率同时保持非触发场景下的安全性和通用性。

**[ConsistRM: Improving Generative Reward Models via Consistency-Aware Self-Training](consistrm_improving_generative_reward_models_via_consistency-aware_self-training.md)**

:   ConsistRM 提出基于一致性感知的自训练框架，通过时序一致性伪标签（融合在线状态和历史记忆的偏好一致性）和语义一致性批评奖励（衡量多次生成批评的语义相似度）两个模块，在无需人工标注的条件下将生成式奖励模型的五个基准平均性能提升 1.5%，同时显著缓解了位置偏差问题。

**[Cross-Modal Taxonomic Generalization in (Vision-) Language Models](cross-modal_taxonomic_generalization_in_vision-_language_models.md)**

:   本文系统研究 VLM 中语言模型是否能将纯文本习得的分类学知识（上位词关系）跨模态泛化到视觉输入，发现即使训练时完全不提供上位词标签，预训练 LM 仍能在图像中识别上位词类别，但这种泛化需要类别成员在视觉上的一致性。

**[Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views](discovering_a_shared_logical_subspace_steering_llm_logical_reasoning_via_alignme.md)**

:   发现 LLM 内部存在一个共享的逻辑子空间，可同时对齐自然语言和符号逻辑两种推理表示，通过在推理时沿该子空间引导激活可无训练提升逻辑推理准确率最高达 11 个百分点。

**[Dynamics of Cognitive Heterogeneity: Investigating Behavioral Biases in Multi-Stage Supply Chains with LLM-Based Simulation](dynamics_of_cognitive_heterogeneity_investigating_behavioral_biases_in_multi-sta.md)**

:   使用LLM智能体（DeepSeek/GPT系列）在经典啤酒分销博弈中模拟多阶段供应链，系统研究认知异质性（推理能力差异）对系统行为的影响，发现LLM智能体能复现人类的牛鞭效应和短视行为，且信息共享能有效缓解这些不良效应。

**[Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization](enhancing_llm-based_search_agents_via_contribution_weighted_group_relative_polic.md)**

:   CW-GRPO 将过程监督重新定义为"优势重分配"：用 LLM 判断器评估每轮搜索的检索有用性和推理正确性，计算贡献分数来缩放基于结果的优势，实现轮级别信用分配而不引入不稳定的价值函数，在 Qwen3-8B 上超越标准 GRPO 5.0%。

**[FACTS: Table Summarization via Offline Template Generation with Agentic Workflows](facts_table_summarization_via_offline_template_generation_with_agentic_workflows.md)**

:   本文提出 FACTS（Fast, Accurate, and Privacy-Compliant Table Summarization），通过三阶段 Agentic 工作流自动生成可复用的离线模板（SQL 查询 + Jinja2 模板），实现快速、准确、隐私合规的查询聚焦表格摘要，在 FeTaQA、QTSumm 和 QFMTS 三个基准上全面超越基线。

**[From Weights to Activations: Is Steering the Next Frontier of Adaptation?](from_weights_to_activations_is_steering_the_next_frontier_of_adaptation.md)**

:   本文系统性地论证 steering（推理时激活空间干预）应被视为一种独立的模型适配范式，提出八项功能性评估标准对比 steering 与微调、PEFT、提示工程等传统方法，将 steering 定位为基于激活空间的局部可逆行为修改方法，具有计算高效、数据高效和可逆性等独特优势。

**[HistLens: Mapping Idea Change across Concepts and Corpora](histlens_mapping_idea_change_across_concepts_and_corpora.md)**

:   提出 HistLens 框架，基于稀疏自编码器（SAE）将概念表示分解为可解释的语义基向量，在共享坐标系中追踪多概念、多语料的历时演化轨迹，支持隐式概念计算，为数字人文和概念史研究提供可量化、可比较的分析工具。

**[IndoTabVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents](indotabvqa_a_benchmark_for_cross-lingual_table_understanding_in_bahasa_indonesia.md)**

:   提出 IndoTabVQA，一个针对印尼语（Bahasa Indonesia）文档表格的跨语言视觉问答基准，包含 1593 张文档图像和四种语言（印尼语/英语/印地语/阿拉伯语）的 QA 标注，揭示了 VLM 在低资源语言和跨语言表格理解上的显著性能差距，微调+空间先验可带来最高 48.5% 的 In-Match 准确率。

**[LaMI: Augmenting Large Language Models via Late Multi-Image Fusion](lami_augmenting_large_language_models_via_late_multi-image_fusion.md)**

:   提出 LaMI，通过后融合架构在预测最后阶段融合视觉特征与 LLM 输出，并在推理时从文本生成多张图像进行基于置信度的聚合，在不损害文本推理能力的前提下显著提升 LLM 的视觉常识推理能力。

**[Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality](language_on_demand_knowledge_at_core_composing_llms_with_encoder-decoder_transla.md)**

:   本文提出 XBridge，一种将预训练多语言编码器-解码器翻译模型（如 NLLB）与英语为中心的 LLM 组合的架构——编码器负责多语言理解、LLM 负责知识推理、解码器负责多语言生成，通过轻量级映射层和最优传输对齐实现跨模型语义桥接，在低资源和未见语言上显著优于基线。

**[MathAgent: Adversarial Evolution of Constraint Graphs for Mathematical Reasoning Data Synthesis](mathagent_adversarial_evolution_of_constraint_graphs_for_mathematical_reasoning_.md)**

:   提出基于约束图对抗进化的分层数据合成框架 MathAgent，将数据合成从文本生成任务重构为约束图的无监督优化问题，通过 Legislator 三Agent系统进化问题骨架再由 Executor 实例化为自然语言，仅 1K 合成样本即超越 LIMO 和 s1K 在八个数学基准上的表现。

**[MCGA: A Multi-task Classical Chinese Literary Genre Audio Corpus](mcga_a_multi-task_classical_chinese_literary_genre_audio_corpus.md)**

:   本文构建了首个面向中国古典文学的大规模（119小时、22000条样本）全版权音频语料库 MCGA，涵盖赋、诗、文、词、曲五大文体和六项语音任务（ASR/S2TT/SEC/SQA/SU/SR），并通过评测 10 个多模态大模型揭示了当前模型在古典文学语音理解上的显著不足。

**[MTR-DuplexBench: Towards a Comprehensive Evaluation of Multi-Round Conversations for Full-Duplex Speech Language Models](mtr-duplexbench_towards_a_comprehensive_evaluation_of_multi-round_conversations_.md)**

:   提出 MTR-DuplexBench，一个针对全双工语音语言模型（FD-SLM）的多轮综合评估基准，通过创新的轮次分割方法解决了全双工对话中轮次边界模糊和上下文不一致的挑战，涵盖对话特性、对话质量、指令遵循和安全性四个维度，实验揭示了现有 FD-SLM 在多轮交互中性能持续衰退的问题。

**[Multilingual Language Models Encode Script Over Linguistic Structure](multilingual_language_models_encode_script_over_linguistic_structure.md)**

:   本文通过 LAPE 指标和稀疏自编码器系统分析多语言 LM 中的语言关联单元，发现这些单元主要由正字法（书写系统）驱动而非抽象语言结构：罗马化转写激活几乎完全不重叠的神经元集合，词序打乱影响甚微，类型学信息仅在深层逐渐可访问，因果干预表明功能重要性与表面形式不变性相关。

**[Native Hybrid Attention for Efficient Sequence Modeling](native_hybrid_attention_for_efficient_sequence_modeling.md)**

:   本文提出 Native Hybrid Attention (NHA)，将线性 RNN 的长期记忆槽与滑动窗口的短期精确 token 拼接后通过单次 softmax 注意力统一处理，实现层内和层间混合的原生统一——无需额外融合参数即可动态分配长短期注意力权重，在 recall 密集和常识推理任务上超越 Transformer 和其他混合基线。

**[ODUTQA-MDC: A Task for Open-Domain Underspecified Tabular QA with Multi-turn Dialogue-based Clarification](odutqa-mdc_a_task_for_open-domain_underspecified_tabular_qa_with_multi-turn_dial.md)**

:   本文提出 ODUTQA-MDC 任务和基准，首次系统研究开放域场景下用户查询模糊性的检测与多轮对话澄清问题，构建了包含 25,105 个 QA 对的大规模数据集，并设计了 MAIC-TQA 多智能体框架来完成"检测-澄清-推理"的端到端表格问答。

**[Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation](planning_beyond_text_graph-based_reasoning_for_complex_narrative_generation.md)**

:   本文提出 PLOTTER 框架，首次将叙事规划从文本表示转移到图结构表示（事件图+角色图），通过多 agent 的 Evaluate-Plan-Revise 迭代循环在图拓扑上诊断和修复叙事缺陷，在叙事性、角色塑造、戏剧张力等维度上显著优于现有方法。

**[Region-R1: Reinforcing Query-Side Region Cropping for Multi-Modal Re-Ranking](region-r1_reinforcing_query-side_region_cropping_for_multi-modal_re-ranking.md)**

:   本文提出 Region-R1，将多模态重排序中的查询图像区域裁剪建模为决策问题，通过强化学习（r-GRPO）学习何时以及如何裁剪查询图像中与问题相关的区域，在 E-VQA 和 InfoSeek 上将 CondRecall@1 分别提升 20% 和 8%。

**[ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning](rerec_reasoning-augmented_llm-based_recommendation_assistant_via_reinforcement_f.md)**

:   本文提出 ReRec，一个基于强化微调（RFT）的推荐助手框架，通过双图增强的奖励塑形提供细粒度奖励信号、推理感知的优势估计对推理步骤进行差异化监督、以及在线课程调度器动态调整训练难度，使 LLM 能处理复杂的多步推理推荐查询，在 RecBench+ 基准上显著超越现有方法。

**[ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](researchbench_benchmarking_llms_in_scientific_discovery_via_inspiration-based_ta.md)**

:   提出 ResearchBench，首个大规模评估LLM科学发现能力的基准，基于"灵感驱动假设生成"的理论分解，覆盖12个学科1386篇论文，将科学发现分解为灵感检索、假设组合、假设排序三个充分子任务，发现LLM在跨学科灵感检索上表现出色。

**[Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](revisiting_non-verbatim_memorization_in_large_language_models_the_role_of_entity.md)**

:   本文通过构建 RedirectQA 数据集（利用 Wikipedia 重定向信息将同一实体关联到多种表面形式），系统研究了 LLM 的非逐字记忆如何受实体命名变体的影响，发现事实记忆既非纯粹依赖特定表面形式也非完全表面无关，且实体级频率在表面频率之外仍有独立贡献。

**[SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning](samora_semantic-aware_mixture_of_lora_experts_for_task-adaptive_learning.md)**

:   SAMoRA 通过语义感知路由器和任务自适应缩放机制，解决了现有 MoE-LoRA 方法中路由不精确和权重融合缺乏灵活性的问题，在多任务基准上以最少可训练参数（0.15%）达到 SOTA。

**[SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration](specbound_adaptive_bounded_self-speculation_with_layer-wise_confidence_calibrati.md)**

:   提出 SpecBound 自草稿推测解码框架，通过逐层温度退火抑制浅层虚假高置信度预测，并设计有界推测算法自适应控制草稿的深度和宽度，在保持输出无损的同时实现最高 2.33× 的推理加速。

**[Splits! Flexible Sociocultural Linguistic Investigation at Scale](splits_flexible_sociocultural_linguistic_investigation_at_scale.md)**

:   提出构建社会语言学"沙盒"的方法，从 Reddit 构建了按人口统计群体和讨论话题双重切分的 970 万帖子数据集 Splits!，并设计了基于 lift 和 triviality 的两阶段过滤流程，从 2.3 万条 LLM 生成的候选假设中高效筛选出值得深入研究的社会文化语言现象。

**[StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference](structkv_preserving_the_structural_skeleton_for_scalable_long-context_inference.md)**

:   本文提出 StructKV，一个结构感知的 KV Cache 压缩框架，通过全局入度中心性（Global In-Degree Centrality）跨层累积注意力模式识别全局信息枢纽，动态枢纽层检测（Dynamic Pivot Detection）自适应定位最优压缩层，以及结构传播与解耦（Structural Propagation & Decoupling）分离计算预算和存储预算，在 LongBench 和 RULER 上以 60% prefill + 10% KV 实现了接近全上下文的性能。

**[The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models](the_gaoyao_benchmark_a_comprehensive_framework_for_evaluating_multilingual_and_m.md)**

:   本文提出GaoYao基准，包含182.3K样本、26种语言和51个国家/地区，通过三层文化评估框架（通用多语言/跨文化/单文化）和九个认知子层，结合人工本地化的主观测试集和专家验证的跨文化合成数据集SuperBLEnD，深度诊断20+旗舰与紧凑型LLM的多语言能力，揭示了显著的地理数字鸿沟和任务能力分层。

**[The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models](the_model_agreed_but_didn39t_learn_diagnosing_surface_compliance_in_large_langua.md)**

:   提出 SA-MCQ 诊断框架揭示知识编辑中的"表面合规"现象——编辑器在标准基准上达到高分但并未真正覆写内部信念，模型在判别式自评中会回退到原始参数记忆，递归编辑还会累积表征残留导致认知不稳定。

**[The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination](the_reasoning_trap_how_enhancing_llm_reasoning_amplifies_tool_hallucination.md)**

:   系统性揭示了"推理陷阱"悖论：增强LLM推理能力（无论通过RL、蒸馏还是可切换推理模式）会系统性地放大工具幻觉，且这一效应与推理本身而非RL训练相关联，现有缓解策略（提示工程、DPO）面临不可避免的可靠性-能力权衡。

**[ThreadSumm: Summarization of Nested Discourse Threads Using Tree of Thoughts](threadsumm_summarization_of_nested_discourse_threads_using_tree_of_thoughts.md)**

:   本文提出 ThreadSumm，一个多阶段 LLM 管道框架，将嵌套话语线程摘要建模为层次推理问题——先提取方面和原子内容单元进行内容规划，再通过句子排序构建线程感知序列，最后用 Tree of Thoughts 搜索生成和评分多个段落候选，在 Reddit/StackExchange 数据集上优于基线。

**[Vocab Diet: Reshaping the Vocabulary of LLMs via Vector Arithmetic](vocab_diet_reshaping_the_vocabulary_of_llms_via_vector_arithmetic.md)**

:   本文发现 LLM 在嵌入空间中将词形变化（如 walk→walked）编码为线性方向，基于此提出组合式词表设计：用基础词+变换向量的加法组合替代为每个表面形式分配独立 token，在冻结预训练骨干的前提下仅训练小型适配模块，释放 10-40% 的词表槽位用于多语言扩展，同时几乎不影响下游性能。

**[Who Gets Which Message? Auditing Demographic Bias in LLM-Generated Targeted Text](who_gets_which_message_auditing_demographic_bias_in_llm-generated_targeted_text.md)**

:   本文首次系统分析 LLM 在人口统计条件下生成定向消息时的偏见行为，提出 Persuasion Bias Index (PBI) 指标，发现 GPT-4o/Llama/Mistral 在气候传播中对男性和年轻人使用更强势的说服策略，且上下文提示会系统性地放大这些差异。

**[XMark: Reliable Multi-Bit Watermarking for LLM-Generated Texts](xmark_reliable_multi-bit_watermarking_for_llm-generated_texts.md)**

:   提出 XMark，一种基于 Leave-one-Shard-out（LoSo）策略和 evergreen list 的多比特文本水印方法，通过跨多个词表排列的绿色列表交集和约束 token-shard 映射矩阵，在保持文本质量的同时显著提升了有限 token 条件下的解码准确率。
