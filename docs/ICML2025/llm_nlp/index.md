<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**🧪 ICML2025** · 共 **59** 篇

**[Adaptive Multi-prompt Contrastive Network for Few-shot Out-of-distribution Detection](adaptive_multi-prompt_contrastive_network_for_few-shot_out-of-distribution_detec.md)**

:   提出 AMCN（Adaptive Multi-prompt Contrastive Network），通过生成三类自适应文本 prompt（可学习 ID prompt、标签固定 OOD prompt、标签自适应 OOD prompt）并结合类别自适应阈值，在仅有少量 ID 标注样本的条件下实现高质量 OOD 检测，显著超越现有 few-shot OOD 检测方法。

**[Are LLM Belief Updates Consistent with Bayes' Theorem?](are_llm_belief_updates_consistent_with_bayes_theorem.md)**

:   本文提出贝叶斯一致性系数（BCC）来量化 LLM 的信念更新是否符合贝叶斯定理，发现更大、更强的预训练模型在给定新证据时，其信念更新与贝叶斯定理更一致。

**[B-score: Detecting biases in large language models using response history](b-score_detecting_biases_in_large_language_models_using_response_history.md)**

:   提出B-score指标，通过比较LLM在单轮(single-turn)与多轮(multi-turn)对话中的回答概率差异来检测偏见，发现LLM在多轮对话中能"自我去偏"，并利用B-score提升答案验证准确率。

**[Bayesian Neural Scaling Law Extrapolation with Prior-Data Fitted Networks](bayesian_neural_scaling_law_extrapolation_with_prior-data_fitted_networks.md)**

:   首个面向神经缩放定律(Neural Scaling Law)的贝叶斯外推方法，通过设计专门的先验分布（覆盖Down/Down-Down/Down-Up-Down三种功能族），利用PFN (Prior-data Fitted Networks) meta-learn外推能力，在点估计精度和不确定性质量上均优于现有方法。

**[Benign Overfitting in Token Selection of Attention Mechanism](benign_overfitting_in_token_selection_of_attention_mechanism.md)**

:   本文首次从理论上证明了注意力机制中 token 选择的良性过拟合现象，表明一层注意力网络通过梯度下降可以完美拟合含噪标签的训练数据，同时在信号学习与噪声记忆之间保持平衡时仍能泛化。

**[BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](best-route_adaptive_llm_routing_with_test-time_optimal_compute.md)**

:   提出 BEST-Route（Best-of-n Enhanced Sampling and Test-time Route Optimization），在传统查询路由的基础上引入 best-of-n 采样策略，使路由器不仅选择模型，还自适应决定采样数量 n，通过小模型多次采样+选优替代大模型单次调用，在不到 1% 性能损失下降低高达 60% 的推理成本。

**[Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](beyond_induction_heads_in-context_meta_learning_induces_multi-phase_circuit_emer.md)**

:   本文通过设计 In-Context Meta-Learning (ICML) 实验环境，揭示了 Transformer 在获得上下文元学习能力的训练过程中，内部电路经历了三个截然不同的阶段性涌现（Bigram → Label Attention → Chunk Example），而非 induction head 研究中观察到的单阶段跃变，从而为理解 ICL 的深层机制提供了新视角。

**[Binary Hypothesis Testing for Softmax Models and Leverage Score Models](binary_hypothesis_testing_for_softmax_models_and_leverage_score_models.md)**

:   从理论角度研究Softmax模型和Leverage Score模型的二元假设检验问题，建立了在能量约束下区分两个参数化模型所需的查询次数的紧界，与理解LLM不同能力域的区分性问题相关。

**[Build Agent Advocates, Not Platform Agents](build_agent_advocates_not_platform_agents.md)**

:   Position paper，指出LMA（语言模型代理）若被平台公司控制将成为加剧监控、锁定和注意力操控的"platform agents"，提出应发展用户控制的"agent advocates"来保护个人自主权，并给出三大干预措施：开放模型/算力、互操作性标准、市场监管。

**[Chameleon: A Flexible Data-mixing Framework for LM Pretraining and Finetuning](chameleon_a_flexible_data-mixing_framework_for_language_model_pretraining_and_fi.md)**

:   提出Chameleon框架，用kernel ridge leverage scores在学习的嵌入空间中量化域重要性，实现高效的数据混合权重计算，可在预训练/微调/域变化三种场景下工作，且无需重新训练代理模型。

**[Communicating Activations Between Language Model Agents](communicating_activations_between_language_model_agents.md)**

:   提出让 LLM 智能体通过中间层激活（而非自然语言）进行通信的方法——在模型 B 的前向传播中间层注入模型 A 的激活向量，无需额外参数和数据，在多项推理基准上比自然语言通信提升 27%，计算量仅为 1/4。

**[Correlated Errors in Large Language Models](correlated_errors_in_large_language_models.md)**

:   本文通过对超过350个LLM的大规模实证分析，发现不同LLM之间存在高度相关的错误模式——在两个模型都出错时约60%的情况下会选择同一个错误答案，且越准确的模型相关性越高；进而研究了这种相关性对LLM-as-Judge评估和招聘市场的下游影响。

**[DipLLM: Fine-Tuning LLM for Strategic Decision-Making in Diplomacy](dipllm_fine-tuning_llm_for_strategic_decision-making_in_diplomacy.md)**

:   提出 DipLLM，通过自回归分解框架将外交博弈的指数级组合动作空间分解为单元级决策序列，并微调 LLM 学习均衡策略，仅用 Cicero 1.5% 的训练数据即超越其性能。

**[Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](disentangling_and_integrating_relational_and_sensory_information_in_transformer_.md)**

:   本文提出了 Dual Attention Transformer（DAT），通过在标准注意力机制中引入"关系注意力"头，将感知信息和关系信息解耦后并行处理再整合，在关系推理基准、数学问题求解、图像识别和语言建模等任务上均展现出显著的数据效率和参数效率提升。

**[Does Data Scaling Lead to Visual Compositional Generalization?](does_data_scaling_lead_to_visual_compositional_generalization.md)**

:   本文通过受控实验系统研究了数据规模与数据多样性对视觉模型组合泛化能力的影响，发现组合泛化的关键驱动力是数据多样性而非数据量，并证明当表示呈线性分解结构时仅需每个概念值2个组合样本即可完美泛化。

**[DyCodeEval: Dynamic Benchmarking of Reasoning in Code LLMs Under Data Contamination](dynamic_benchmarking_of_reasoning_capabilities_in_code_large_language_models_und.md)**

:   提出DyCodeEval——用多Agent系统自动生成编程问题的语义等价变体来动态评估Code LLM，修改问题的上下文描述（不改变核心算法逻辑）以避免记忆化，在18个Code LLM上验证其有效反映真实推理能力。

**[Dynamical Phases of Short-Term Memory Mechanisms in RNNs](dynamical_phases_of_short-term_memory_mechanisms_in_rnns.md)**

:   本文发现了支持RNN短时记忆的两种不同潜在动力学机制——慢点流形（slow-point manifolds）和极限环（limit cycles），通过解析 toy 模型推导出各自最大可学习率的幂律缩放定律（SP: beta 约4-5 vs LC: beta 约2-3），并通过训练约80,000个RNN进行了大规模实证验证。

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](emergent_symbolic_mechanisms_support_abstract_reasoning_in_large_language_models.md)**

:   本文通过因果分析、表征分析和注意力分析等方法，在13个开源LLM中识别出支持抽象推理的三阶段涌现符号架构——符号抽象头将输入token转化为抽象变量、符号归纳头在抽象变量层面进行序列归纳、检索头根据预测的抽象变量检索对应值来完成下一token预测。

**[EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](enigma_interactive_tools_substantially_assist_lm_agents_in_finding_security_vuln.md)**

:   EnIGMA 是一个用于自主解决 Capture The Flag (CTF) 挑战的 LM agent，通过引入新型交互式 Agent 工具（调试器和服务器连接工具），首次使 LM agent 能够运行交互式终端程序，在 4 个基准的 390 个 CTF 挑战上取得 SOTA，并发现了 "soliloquizing" 这一新的幻觉现象。

**[Evaluating Morphological Alignment of Tokenizers in 70 Languages](evaluating_morphological_alignment_of_tokenizers_in_70_languages.md)**

:   扩展 MorphScore 评估框架至 70 种语言，系统研究分词器的形态边界对齐程度与下游任务性能之间的相关性，发现形态对齐仅能解释极少量的性能方差，且呈负相关，挑战了"形态对齐分词有利于模型性能"的主流假设。

**[Function-to-Style Guidance of LLMs for Code Translation](function-to-style_guidance_of_llms_for_code_translation.md)**

:   提出 F2STrans，通过功能学习（正确性）和风格学习（可读性）两阶段渐进式微调 LLM，使 Qwen-1.5B 在 20 种代码翻译场景中平均超越 prompt 增强的 Qwen-32B 和 GPT-4。

**[G-Sim: Generative Simulations with Large Language Models and Gradient-Free Calibration](g-sim_generative_simulations_with_large_language_models_and_gradient-free_calibr.md)**

:   提出 G-Sim 混合框架，利用 LLM 自动设计仿真器的因果结构（子模块与连接关系），再通过无梯度优化（GFO）或仿真推断（SBI）对数值参数进行经验校准，在迭代循环中不断改进，生成可靠、可干预的通用仿真器。

**[How Much Can We Forget about Data Contamination?](how_much_can_we_forget_about_data_contamination.md)**

:   通过受控实验系统量化数据污染对 LLM benchmark 评估的影响，发现在超过 Chinchilla 最优五倍以上的训练数据量下，即使 144 次重复的污染数据也能被完全遗忘；进一步证明权重衰减是遗忘的关键机制，并据此推断 Llama 3 405B 等大型模型已遗忘训练早期的数据。

**[How to Synthesize Text Data without Model Collapse?](how_to_synthesize_text_data_without_model_collapse.md)**

:   提出 Token-level Editing (ToEdit)，通过对人类数据进行 token 级别的局部重采样（而非完全生成合成数据），在理论上证明测试误差存在有限上界，从而避免 model collapse，并在预训练、持续预训练和微调三个阶段验证了有效性。

**[Hyperband-based Bayesian Optimization for Black-box Prompt Selection](hyperband-based_bayesian_optimization_for_black-box_prompt_selection.md)**

:   提出 HbBoPs 方法，结合结构感知深度核高斯过程（对 instruction 和 few-shot exemplar 分别编码）与 Hyperband 多保真度调度器，在黑盒 LLM 的 prompt 选择问题上同时实现样本高效和查询高效，在十个基准和三个 LLM 上超越所有 SOTA 方法。

**[Interchangeable Token Embeddings for Extendable Vocabulary and Alpha-Equivalence](interchangeable_token_embeddings_for_extendable_vocabulary_and_alpha-equivalence.md)**

:   提出双部分 token 嵌入策略（共享可学习部分 + 随机区分部分），使语言模型能在训练后泛化到更大词表，并对 alpha-等价变换具有天然鲁棒性。

**[Investigating Non-Transitivity in LLM-as-a-Judge](investigating_non-transitivity_in_llm-as-a-judge.md)**

:   揭示了 LLM-as-a-Judge 框架中评判偏好的**非传递性**问题（A>B, B>C 不能推出 A>C），证明固定基线模型的排名方式不可靠，提出基于循环赛 + Bradley-Terry 模型的排名方法及高效的 Swim 锦标赛策略。

**[Is Your LLM-Based Multi-Agent a Reliable Real-World Planner? Exploring Fraud Detection in Travel Planning](is_your_llm-based_multi-agent_a_reliable_real-world_planner_exploring_fraud_dete.md)**

:   提出 WandaPlan 评估环境，在旅行规划场景中注入三种递进式欺诈内容，揭示现有 LLM 多智能体规划系统在应对欺诈时的严重漏洞，并提出反欺诈 agent 作为缓解方案。

**[Language Model Developers Should Report Train-Test Overlap](language_model_developers_should_report_train-test_overlap.md)**

:   本文系统性地调研了30个语言模型开发者在训练-测试重叠（train-test overlap）方面的报告实践，发现仅9个模型提供了足够的重叠信息，并呼吁所有开发者在发布评估结果时必须同时报告训练-测试重叠统计数据或公开训练数据。

**[Language Models over Canonical Byte-Pair Encodings](language_models_over_canonical_byte-pair_encodings.md)**

:   揭示基于 BPE 的语言模型会给指数多个"非规范"编码分配非零概率导致浪费，提出条件化（推理时约束）和构造化（新模型参数化）两种方法强制规范性，改善 held-out 似然。

**[Large Language Models are Demonstration Pre-Selectors for Themselves](large_language_models_are_demonstration_pre-selectors_for_themselves.md)**

:   提出 FEEDER（FEw yet Essential Demonstration prE-selectoR），一个基于"充分性"和"必要性"度量的示例预选框架，利用 LLM 自身能力从训练数据中识别代表性子集，在 ICL 和微调两个场景下均可减少 20%+ 数据量同时保持甚至提升性能。

**[LASER: Attention with Exponential Transformation](laser_attention_with_exponential_transformation.md)**

:   通过分析注意力机制中 softmax 的梯度反向传播瓶颈，提出 LASER 注意力——在指数变换的 Value 空间中做注意力计算（即对 exp(V) 做 attention 再取 log），从而获得更大的 Jacobian 信号，改善参数学习效率。

**[Learning Distribution-Wise Control in Representation Space for Language Models](learning_distribution-wise_control_in_representation_space_for_language_models.md)**

:   将表示微调（Representation Fine-tuning）中的确定性节点替换为随机节点，通过重参数化技巧学习潜在分布而非单点变换，在常识推理和数学推理任务上取得了一致性能提升，尤其在早期层的干预效果最为显著。

**[Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](leveraging_online_olympiad-level_math_problems_for_llms_training_and_contaminati.md)**

:   利用 Art of Problem Solving (AoPS) 论坛的社区内容，构建了 652K 奥赛级数学 QA 对的训练集 AoPS-Instruct 和带时间戳的抗污染评估集 LiveAoPSBench，揭示了 LLM 在旧数据上的高表现可能源于预训练数据泄露而非真正推理能力。

**[LLM-SRBench: A New Benchmark for Scientific Equation Discovery with LLMs](llm-srbench_a_new_benchmark_for_scientific_equation_discovery_with_large_languag.md)**

:   提出LLM-SRBench基准（239题/4个科学领域），通过方程变换(LSR-Transform)和合成问题(LSR-Synth)防止LLM的记忆化，当前最好方法仅达31.5%符号准确率。

**[LLM Data Selection and Utilization via Dynamic Bi-level Optimization](llm_data_selection_and_utilization_via_dynamic_bi-level_optimization.md)**

:   提出动态数据加权模型(DWM)，通过双层优化在LLM训练过程中实时调整每批数据的权重，捕捉模型动态变化的数据偏好，比静态数据选择方法一致提升性能且可迁移到不同模型规模。

**[Metadata Conditioning Accelerates Language Model Pre-training](metadata_conditioning_accelerates_language_model_pre-training.md)**

:   提出 MeCo（Metadata Conditioning then Cooldown），在预训练时将文档的 URL 等元数据前置拼接到文本中，帮助模型区分异质数据源，最后 10% 训练用标准数据做 cooldown，使 1.6B 模型用 **33% 更少的数据**即可达到同等下游性能，同时解锁了通过条件推理引导生成的能力。

**[On Expressive Power of Looped Transformers: Theoretical Analysis and Enhancement via Timestep Encoding](on_expressive_power_of_looped_transformers_theoretical_analysis_and_enhancement_.md)**

:   本文首次建立了 Looped Transformer 关于循环次数和目标函数连续性模的逼近速率理论，揭示了循环架构特有的逼近误差来源（上下文连续性与 token 连续性），并提出 Timestep-Modulated Looped Transformer (TMLT) 通过时间步编码消除该限制，在推理、上下文学习和语言建模任务上取得一致提升。

**[On the Effect of Uncertainty on Layer-wise Inference Dynamics](on_the_effect_of_uncertainty_on_layer-wise_inference_dynamics.md)**

:   利用 Tuned Lens 分析 5 个 LLM 在 11 个数据集上各层的 token 概率演化轨迹，发现确定性和不确定性预测的推理动力学高度对齐，挑战了基于简单层间特征检测不确定性的可行性。

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](phantomwiki_on-demand_datasets_for_reasoning_and_retrieval_evaluation.md)**

:   提出 PhantomWiki——一个按需生成虚构世界语料库和 QA 对的评测框架，通过上下文无关文法（CFG）控制推理难度、调节宇宙规模控制检索难度，实现对 LLM 推理与检索能力的解耦评估，同时天然抵抗数据泄漏。

**[POQD: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](poqd_performance-oriented_query_decomposer_for_multi-vector_retrieval.md)**

:   提出 POQD，一个面向性能的查询分解框架，利用 LLM-based Prompt Optimizer 迭代优化查询分解 prompt，并通过交替训练算法联合优化 prompt 和下游 RAG 模型参数，在检索和端到端 QA 任务上大幅超越现有方法。

**[Position: We Need An Algorithmic Understanding of Generative AI](position_we_need_an_algorithmic_understanding_of_generative_ai.md)**

:   提出 AlgEval 框架，倡导系统性地研究生成式 AI 学习和使用的算法——包括算法原语（vocabulary）及其组合（grammar）——作为替代纯粹规模扩展的理解路径，并通过图导航任务的案例研究展示了 top-down 假说与 bottom-up 验证相结合的方法论。

**[Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](product_of_experts_with_llms_boosting_performance_on_arc_is_a_matter_of_perspect.md)**

:   将 LLM 同时用作候选解生成器和评分器，通过基于 DFS 的搜索算法生成高概率候选解，再利用多视角增强下的 Product of Experts (PoE) 打分选出最优答案，在 ARC-AGI 公开评估集上以 71.6% 的准确率达到开源 SOTA，超越人类平均水平（60.2%），且单任务推理成本仅约 $0.02。

**[QuEst: Enhancing Estimates of Quantile-Based Distributional Measures Using Model Predictions](quest_enhancing_estimates_of_quantile-based_distributional_measures_using_model_.md)**

:   提出 QuEst 框架，将少量高质量观测数据与大量模型预测（imputed）数据相结合，对分位数相关的分布度量（QBDM）给出更精确的点估计和严格的置信区间，覆盖 CVaR、Interval-VaR 等经典指标。

**[Random Registers for Cross-Domain Few-Shot Learning](random_registers_for_cross-domain_few-shot_learning.md)**

:   在跨域小样本学习（CDFSL）中发现可学习 prompt 会损害目标域泛化性能，而用随机噪声替代（即随机寄存器）反而能持续提升性能，并基于此提出 REAP 方法，通过在图像语义区域添加随机寄存器来增强注意力扰动，实现高效的域无关特征学习。

**[ResearchTown: Simulator of Human Research Community](researchtown_simulator_of_human_research_community.md)**

:   提出 ResearchTown，一个基于 agent-data 图和 TextGNN（文本空间消息传递）的多智能体框架，将人类科研社区建模为异构图，统一模拟论文阅读、论文写作和审稿三大核心研究活动，并通过节点掩码预测任务 (ResearchBench) 进行可扩展、客观的仿真质量评估。

**[Revisiting Continuity of Image Tokens for Cross-Domain Few-Shot Learning](revisiting_continuity_of_image_tokens_for_cross-domain_few-shot_learning.md)**

:   发现破坏 ViT 图像 token 的连续性（使相邻 patch 像素不再平滑过渡）在源域性能显著下降但在目标域仅略降，揭示连续性帮助学习的大空间模式更难跨域迁移，据此提出简单有效的 ReCIT 方法来缩小域差距。

**[Supernova Event Dataset: Interpreting Large Language Models' Personality through Critical Event Analysis](supernova_event_dataset_interpreting_large_language_models_personality_through_c.md)**

:   提出 Supernova Event Dataset（包含传记、历史事件、新闻、科学发现的 Wikipedia 文章），通过让 LLM 从长文本中抽取并排序关键事件，再由另一个 LLM 作为评判者推断目标模型的"人格特质"，揭示不同 LLM 在主观决策中的一致性行为模式差异。

**[Taming Knowledge Conflicts in Language Models](taming_knowledge_conflicts_in_language_models.md)**

:   揭示了语言模型注意力头中"上下文信息与参数记忆的叠加"（CP Superposition）现象，提出 JuICE（Just Run Twice）方法，通过双次推理的注意力干预策略，在不微调的前提下灵活引导模型偏向参数知识或上下文知识，在 11 个数据集 × 6 种模型架构上达到 SOTA。

**[The Best of Both Worlds: Bridging Quality and Diversity in Data Selection with Bipartite Graph](the_best_of_both_worlds_bridging_quality_and_diversity_in_data_selection_with_bi.md)**

:   提出 GraphFilter 方法，将 SFT 数据集建模为句子-n-gram 的二部图，通过乘法优先级函数同时优化数据质量和多样性，在 3 个模型 6 个基准上全面超越 9 种基线方法。

**[The Lock-in Hypothesis: Stagnation by Algorithm](the_lock-in_hypothesis_stagnation_by_algorithm.md)**

:   本文提出并形式化了"锁定假说"（Lock-in Hypothesis）：LLM 训练与部署过程中形成的人类-AI 反馈循环会固化用户的现有信念，导致群体观点多样性不可逆地丧失，甚至锁定在错误信念上。

**[The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](the_sharpness_disparity_principle_in_transformers_for_accelerating_language_mode.md)**

:   揭示了 Transformer 中不同类型模块（Emb、QK、FFN、VO、Norm）存在显著且持久的**锐度差异**（sharpness disparity），并据此提出 Blockwise LR 策略，为低锐度模块分配更大学习率，在不损失稳定性的前提下实现 LLM 预训练近 **2× 加速**。

**[Theoretical Limitations of Ensembles in the Age of Overparameterization](theoretical_limitations_of_ensembles_in_the_age_of_overparameterization.md)**

:   在过参数化条件下，无限集成模型与单个无穷宽模型逐点等价，集成方差不再反映传统贝叶斯不确定性而是衡量增加模型容量的预期效果，从理论上解释了深度集成相比大模型无本质泛化优势的经验观察。

**[To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](to_steer_or_not_to_steer_mechanistic_error_reduction_with_abstention_for_languag.md)**

:   提出 MERA（Mechanistic Error Reduction with Abstention），一个基于线性error estimator的原则性activation steering框架，通过约束优化推导闭式最优steering强度，并引入校准步骤确保仅在可证明有效时才进行干预，解决了传统固定steering强度导致的过度/不足steering问题。

**[Tokenized Bandit for LLM Decoding and Alignment](tokenized_bandit_for_llm_decoding_and_alignment.md)**

:   将 LLM 解码与对齐问题形式化为 **tokenized bandit**（token化老虎机）问题，提出 DDMC（Diminishing Distance with More Commons）假设，证明在该假设下贪心解码近似最优，并设计了具有次线性遗憾的在线学习算法 EOFUL 和 GreedyETC。

**[Towards Universal Offline Black-Box Optimization via Learning Language Model Embeddings](towards_universal_offline_black-box_optimization_via_learning_language_model_emb.md)**

:   探索用语言模型嵌入实现通用离线黑盒优化(BBO)：将异构数值参数token化为字符串后用LM编码，提出端到端(next-token prediction)和潜在空间学习两种范式，在多域离线BBO任务上验证了跨域泛化能力。

**[Unlocking Post-hoc Dataset Inference with Synthetic Data](unlocking_post-hoc_dataset_inference_with_synthetic_data.md)**

:   提出通过合成生成held-out数据集并结合后校准（post-hoc calibration）来实现无需真实held-out集的数据集推断（Dataset Inference），通过suffix completion生成高质量合成数据、双分类器校准解耦生成偏移与成员信号，在15个多样化文本数据集上实现高置信度版权检测且低误报率。

**[When Can In-Context Learning Generalize Out of Task Distribution?](when_can_in-context_learning_generalize_out_of_task_distribution.md)**

:   通过在线性回归ICL任务上系统改变训练任务分布的覆盖范围（超球面帽的半角 $\phi$），发现transformer存在从"专用解"到"通用解"的sharp phase transition：当任务多样性超过临界阈值（$\phi \gtrsim 120°$）时，模型能泛化到整个任务空间，甚至超越贝叶斯最优估计器的OOD性能。

**[WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs](wikibigedit_understanding_the_limits_of_lifelong_knowledge_editing_in_llms.md)**

:   本文提出 WikiBigEdit，一个包含 50 万+ 真实 Wikidata 知识编辑的大规模终身知识编辑基准，揭示了现有知识编辑方法在实际规模下的严重局限性——检索增强和持续微调+模型合并等通用方法反而表现更优。
