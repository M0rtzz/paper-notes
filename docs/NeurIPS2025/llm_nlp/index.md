<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**🧠 NeurIPS2025** · 共 **132** 篇

**[AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play](acesearcher_bootstrapping_reasoning_and_search_for_llms_via_reinforced_self-play.md)**

:   提出 AceSearcher——一种协作式自我博弈框架，让单个 LLM 同时扮演**问题分解者**（将复杂查询拆解为子问题引导检索）和**求解者**（整合检索上下文生成答案），通过 SFT + 迭代 DPO 两阶段训练，仅用最终答案作为奖励信号，在 10 个数据集上平均 EM 提升 7.6%，32B 模型匹配 DeepSeek-V3（<5% 参数）。

**[Active Slice Discovery in Large Language Models](active_slice_discovery_in_large_language_models.md)**

:   提出 **Active Slice Discovery** 问题框架，将主动学习引入 LLM 错误切片发现，利用不确定性采样 + LLM 内部表征（原始 embedding 或 SAE 特征）在仅使用 2-10% 标注的情况下达到接近全标注的切片检测精度。

**[AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners](adastar_adaptive_data_sampling_for_training_self-taught_reasoners.md)**

:   发现 STaR（自我教学推理器）的随机数据采样导致观测训练频率严重不平衡（简单题过度训练、难题训练不足），提出 AdaSTaR——通过自适应多样性采样（优先欠训练样本）和自适应课程采样（根据模型强度调节难度），在 6 个基准上全部取得最高准确率同时减少 58.6% 训练 FLOPs。

**[AI Progress Should Be Measured by Capability-Per-Resource, Not Scale Alone: A Framework for Gradient-Guided Resource Allocation in LLMs](ai_progress_should_be_measured_by_capability-per-resource_not_scale_alone_a_fram.md)**

:   本文以 position paper 的形式挑战"规模至上主义"，提出以**能力-每-资源（Capability-Per-Resource, CPR）**取代单纯的规模扩张来衡量 AI 进步，并给出一套基于梯度引导的资源分配理论框架——通过发布"梯度蓝图"元数据，使下游适配者仅微调高影响力参数子集即可在资源占用大幅降低的同时保持接近全参数微调的性能。

**[Are Language Models Efficient Reasoners? A Perspective from Logic Programming](are_language_models_efficient_reasoners_a_perspective_from_logic_programming.md)**

:   从逻辑编程角度提出评估 LLM 推理效率（而非仅正确性）的框架——通过 verbalized logic program 将自然语言证明映射到逻辑程序证明，发现当前 LLM 在含无关公理的数学题中不仅准确率下降，且推理过程严重低效（超过一半的推理步骤是不必要的）。

**[ARECHO: Autoregressive Evaluation via Chain-Based Hypothesis Optimization for Speech Multi-Metric Estimation](arecho_autoregressive_evaluation_via_chain-based_hypothesis_optimization_for_spe.md)**

:   ARECHO 将语音多指标评估建模为链式自回归 token 预测任务——设计统一的语音信息 token 化管线处理 87 个异质指标（数值/类别/有界/无界），通过动态分类链显式捕捉指标间依赖关系（如可懂度-自然度相关性），配合两步置信度导向解码减少误差传播，在增强/生成/噪声三类语音评估中全面超越 UniVERSA 基线（Avg Test MSE 23.26 vs 96.99，-76%）。

**[AstroVisBench: A Code Benchmark for Scientific Computing and Visualization in Astronomy](astrovisbench_a_code_benchmark_for_scientific_computing_and_visualization_in_ast.md)**

:   AstroVisBench 构建了首个评估 LLM 天文科学计算和可视化能力的代码基准——从 110 个 Jupyter Notebook 提取 864 个任务（处理+可视化），设计双重评估管线（执行式变量检查 + VLM-as-Judge 可视化评分，与专家 Spearman ρ=0.822），评测 8 个 SOTA 模型后发现 Gemini 2.5 Pro 最佳但无错误率仅 15.7%，FileNotFoundError 占 43% 错误。

**[ARC-JSD: Attributing Response to Context via Jensen-Shannon Divergence Driven Mechanistic Study](attributing_response_to_context_a_jensen-shannon_divergence_driven_mechanistic_s.md)**

:   ARC-JSD 提出基于 Jensen-Shannon 散度的 RAG 上下文归因方法——通过比较有/无特定上下文句子时模型输出分布的 JSD 差异，无需微调/梯度计算即可定位回答所依赖的上下文，计算效率比 baseline 快 3 倍，Top-1 归因准确率平均提升 10.7%，并通过 Logit Lens 揭示归因相关的注意力头集中在高层。

**[Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in LLMs](auto-search_and_refinement_an_automated_framework_for_gender_bias_mitigation_in_.md)**

:   提出 FaIRMaker 框架，通过"自动搜索+精化"范式先用梯度优化找到去偏见触发词（Fairwords），再训练 seq2seq 模型将其转化为可读指令，在开源和闭源 LLM 上有效缓解性别偏见同时保持甚至提升任务性能。

**[Belief-Calibrated Multi-Agent Consensus Seeking for Complex NLP Tasks](belief-calibrated_multi-agent_consensus_seeking_for_complex_nlp_tasks.md)**

:   提出 Belief-Calibrated Consensus Seeking (BCCS) 框架，通过引入信念（belief）校准的共识判断、冲突感知的协作者分配和领导者选择三个模块，让多智能体系统在复杂NLP任务上达成更稳定的共识，在 MATH 和 MMLU 上的困难任务分别提升 2.23% 和 3.95%。

**[Benchmarking Large Language Models for Zero-Shot and Few-Shot Phishing URL Detection](benchmarking_large_language_models_for_zero-shot_and_few-shot_phishing_url_detec.md)**

:   在统一的零样本和少样本 prompt 框架下系统评估 GPT-4o、Claude-3.7 和 Grok-3-Beta 三个商用 LLM 在钓鱼 URL 检测任务上的表现，发现少样本 prompt 可显著提升所有模型性能，Grok-3-Beta 在平衡数据集上取得最佳 F1（0.9399），但不同模型在精度-召回率权衡上呈现差异化行为模式。

**[Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits](beyond_components_singular_vector-based_interpretability_of_transformer_circuits.md)**

:   提出基于SVD奇异向量的方向级可解释性框架，通过对注意力头和MLP的增广矩阵统一SVD分解+可学习对角掩码（KL+L₁），发现单组件内存在正交低秩子函数叠加——IOI任务仅需~9%方向即可KLD=0.21复现模型行为。

**[Beyond the Singular: Revealing the Value of Multiple Generations in Benchmark Evaluation](beyond_the_singular_revealing_the_value_of_multiple_generations_in_benchmark_eva.md)**

:   将LLM基准评测形式化为层级统计模型，理论证明多次随机生成（k>1）能降低benchmark分数估计方差，并引入prompt级难度指标$\mathbb{P}(\text{correct})$和数据地图用于基准质量控制。

**[Beyond The Surface Enhancing Llm-As-A-Judge Alignment With Human Via Internal Re](beyond_the_surface_enhancing_llm-as-a-judge_alignment_with_human_via_internal_re.md)**

:   提出LAGER框架，通过聚合LLM中间层到最终层的score token logits并计算期望分数，无需微调模型即可将LLM评判与人类评分的对齐度提升最高7.5%，且不需要思维链推理步骤就能匹配或超过推理类方法。

**[Beyond Token Probes Hallucination Detection Via Activation Tensors With Act-Vit](beyond_token_probes_hallucination_detection_via_activation_tensors_with_act-vit.md)**

:   将LLM的全部隐层激活组织为"激活张量"（层×token×隐维度），类比图像用ViT处理，设计ACT-ViT架构支持跨LLM联合训练，在15个LLM-数据集组合上一致超越传统probing方法，并展现出对未见数据集和未见LLM的强零样本/少样本迁移能力。

**[Bigram Subnetworks Mapping To Next Tokens In Transformer Language Models](bigram_subnetworks_mapping_to_next_tokens_in_transformer_language_models.md)**

:   通过连续稀疏化在Transformer语言模型中找到仅包含~10M参数的bigram子网络，它们集中在第一个MLP层，足以复现bigram预测（$r>0.95$），且被消融后模型性能大幅下降，证明这些子网络是语言模型中既必要又充分的最小next-token预测电路。

**[Born a Transformer – Always a Transformer? On the Effect of Pretraining on Architectural Abilities](born_a_transformer_--_always_a_transformer_on_the_effect_of_pretraining_on_archi.md)**

:   通过系统性地研究检索和复制任务家族，揭示了大规模预训练会为Transformer引入方向性偏置（右/前向优于左/后向），但无法克服非唯一任务上的根本架构限制；微调可消除方向偏置但不能突破架构表达力边界。

**[Breaking The Frozen Subspace Importance Sampling For Low-Rank Optimization In Ll](breaking_the_frozen_subspace_importance_sampling_for_low-rank_optimization_in_ll.md)**

:   发现GaLore等低秩优化方法的主导子空间在预训练中会"冻结"（相邻子空间重叠度趋近1），导致权重更新卡在固定低秩子空间中；提出SARA（重要性采样子空间选择），按奇异值权重随机采样奇异向量构建子空间，证明收敛性的同时将低秩优化器与全秩Adam的性能差距缩小最高46%。

**[Bridging Human And Llm Judgments Understanding And Narrowing The Gap](bridging_human_and_llm_judgments_understanding_and_narrowing_the_gap.md)**

:   提出Bridge统计框架，通过序数logistic回归建模人类和LLM评判之间的潜在关系，以少量人类标签改善LLM评判的校准和对齐，同时支持对系统性偏差的正式统计检验。

**[Broken Tokens: Your Language Model Can Secretly Handle Non-Canonical Tokenization](broken_tokens_your_language_model_can_secretly_handle_non-canonical_tokenization.md)**

:   揭示 LLM 能秘密处理非标准分词（如将"Hello"拆为"He"+"llo"而非标准的"Hello"整词token）——即使输入的 token 序列与训练时不同，模型表现出惊人的鲁棒性，且这种能力来自嵌入空间中子词嵌入的线性组合近似整词嵌入的特性。

**[C²Prompt: Class-aware Client Knowledge Interaction for Federated Continual Learning](c2prompt_class-aware_client_knowledge_interaction_for_federated_continual_learni.md)**

:   针对联邦持续学习中prompt通信时的类级知识不一致问题，提出C²Prompt方法，通过局部类分布补偿（LCDC）和类感知prompt聚合（CPA）两个机制显式增强跨客户端的类级知识一致性，在ImageNet-R上Avg准确率达87.20%，超出SOTA Powder 2.51%。

**[Can Large Language Models Master Complex Card Games?](can_large_language_models_master_complex_card_games.md)**

:   系统评估LLM在8种复杂卡牌游戏上的学习能力，发现通过高质量游戏数据的SFT，LLM可以接近强游戏AI的水平，并能同时掌握多个游戏，但通用能力会下降（可通过混入通用指令数据缓解）。

**[CAT: Circular-Convolutional Attention for Sub-Quadratic Transformers](cat_circular-convolutional_attention_for_sub-quadratic_transformers.md)**

:   本文提出CAT（Circular-convolutional Attention），通过FFT计算循环卷积将Self-Attention复杂度从O(N²)降至O(N log N)，同时保持完整的softmax机制和全局注意力。

**[CBMAS: Cognitive Behavioral Modeling via Activation Steering](cbmas_cognitive_behavioral_modeling_via_activation_steering.md)**

:   CBMAS 提出一个连续激活干预诊断框架，将传统“前后对比式”认知偏差分析扩展为可解释的干预轨迹分析，通过 alpha 强度扫描、logit-lens 偏置曲线与层位敏感性分析，揭示 LLM 行为翻转临界点与跨层演化机制。

**[Characterizing the Expressivity of Fixed-Precision Transformer Language Models](characterizing_the_expressivity_of_fixed-precision_transformer_language_models.md)**

:   精确刻画了固定精度、严格未来掩码、软注意力、无位置编码的 Transformer 的表达能力——恰好等价于仅含过去算子的线性时态逻辑 LTL[P]，并将其与偏序确定有限自动机 (PODFA)、$\mathcal{R}$-trivial 幺半群统一起来。

**[CodeAssistBench (CAB): Dataset & Benchmarking for Multi-turn Chat-Based Code Assistance](codeassistbench_cab_dataset_benchmarking_for_multi-turn_chat-based_code_assistan.md)**

:   提出 CodeAssistBench (CAB)，第一个评估多轮、项目级编程辅助的全自动 Benchmark，从 GitHub Issues 自动构建 3,286 个真实编程求助场景，涵盖 7 种语言 214 个仓库，揭示 SOTA 模型在 StackOverflow 问题上 70-83% 但在 post-cutoff 仓库上仅 7-16% 的巨大鸿沟。

**[ComPO: Preference Alignment via Comparison Oracles](compo_preference_alignment_via_comparison_oracles.md)**

:   针对DPO中噪声偏好对（preferred和dispreferred响应相似）导致的似然位移和冗长问题，提出基于比较oracle的零阶偏好对齐方法ComPO，将数据分为干净/噪声子集，用DPO处理干净数据、用ComPO提取噪声数据中的信号，在AlpacaEval 2等benchmark上持续提升LC win rate。

**[Composing Linear Layers from Irreducibles](composing_linear_layers_from_irreducibles.md)**

:   利用Clifford代数，将线性层表示为二向量（bivector）的组合——即旋量（rotor）的三明治乘积——仅需 $O(\log^2 d)$ 参数即可替代 $d \times d$ 密集矩阵，应用于LLM注意力层的Q/K/V投影时性能接近原始模型和强基线。

**[ConfTuner: Training Large Language Models to Express Their Confidence Verbally](conftuner_training_large_language_models_to_express_their_confidence_verbally.md)**

:   ConfTuner 提出 tokenized Brier score 损失函数（理论证明为 proper scoring rule），仅需 2000 个样本 + 4 分钟 LoRA 微调即可让 LLM 输出校准的语言化置信度（如"我80%确定"），ECE 最大降低 60.9%，支持自我纠错和模型级联等下游应用。

**[CoRe: Benchmarking LLMs' Code Reasoning Capabilities through Static Analysis Tasks](core_benchmarking_llms_code_reasoning_capabilities_through_static_analysis_tasks.md)**

:   提出 CoRe，一个包含 12,553 个人工验证任务实例的高质量 benchmark，通过数据依赖、控制依赖和信息流三类静态分析基础任务，直接评估 LLM 的代码语义推理能力，揭示模型在 trace 生成和源枚举等需要多步推理的任务上仍严重不足。

**[Cultural Alien Sampler: Open-ended Art Generation Balancing Originality and Coherence](cultural_alien_sampler_open-ended_art_generation_balancing_originality_and_coher.md)**

:   提出Cultural Alien Sampler (CAS)——用两个GPT-2模型分别建模"概念一致性"和"文化典型性"，通过选择高一致性但低文化典型性的概念组合来生成原创且和谐的艺术创意，在人类评估中接近艺术专业学生水平并远超GPT-4o。

**[DATE-LM: Benchmarking Data Attribution Evaluation for Large Language Models](date-lm_benchmarking_data_attribution_evaluation_for_large_language_models.md)**

:   DATE-LM是首个统一、应用驱动的LLM数据归因基准，涵盖数据选择、毒性过滤、事实归因三大应用，通过公开排行榜促进可复现和公平的方法比较。

**[DCAD-2000: A Multilingual Dataset across 2000+ Languages with Data Cleaning as Anomaly Detection](dcad-2000_a_multilingual_dataset_across_2000_languages_with_data_cleaning_as_ano.md)**

:   构建覆盖2282种语言、46.72TB文本的多语言数据集DCAD-2000，提出将数据清洗重构为异常检测问题的语言无关框架，通过8维统计特征+Isolation Forest动态过滤噪声数据，在多个多语言benchmark上验证效果，尤其对低资源语言提升显著。

**[Decoupled Entropy Minimization](decoupled_entropy_minimization.md)**

:   将经典熵最小化（EM）解耦为两个对立部分——Cluster Aggregation Driving Factor (CADF，奖励主导类别)和 Gradient Mitigation Calibrator (GMC，惩罚高置信类别)，揭示了经典 EM 的两个固有缺陷（reward collapse 和 easy-class bias），提出 AdaDEM 通过归一化奖励和边际熵校准来修复这些问题，在半监督学习、域适应、强化学习等多任务上显著提升。

**[Deep Learning for Continuous-Time Stochastic Control with Jumps](deep_learning_for_continuous-time_stochastic_control_with_jumps.md)**

:   提出两种基于模型的深度学习算法（GPI-PINN 和 GPI-CBU）来求解含跳跃的有限时域连续时间随机控制问题，通过迭代训练策略网络和价值网络，避免了状态动力学的离散化和模拟，在高维场景中表现出色。

**[Demystifying Language Model Forgetting With Low-Rank Example Associations](demystifying_language_model_forgetting_with_low-rank_example_associations.md)**

:   发现LLM微调后上游样本遗忘与新学任务之间的关联矩阵具有低秩结构（rank-3即$R^2>0.69$），利用矩阵补全预测未见任务导致的遗忘，指导选择性回放以减轻遗忘。

**[Detecting High-Stakes Interactions with Activation Probes](detecting_high-stakes_interactions_with_activation_probes.md)**

:   用线性激活探针（在 LLM 内部表示上训练的轻量分类器）检测用户的"高风险交互"，在合成数据上训练后跨 6 个真实数据集 AUROC 达 0.88-0.92，匹敌 8-12B 微调 LLM但计算成本低 6 个数量级，级联架构（探针初筛+LLM 精判）进一步超越单独使用任一方法。

**[Disaggregation Reveals Hidden Training Dynamics: The Case of Agreement Attraction](disaggregation_reveals_hidden_training_dynamics_the_case_of_agreement_attraction.md)**

:   通过将聚合的语法评测指标**分解**到实验条件层面并追踪训练过程中的变化，发现语言模型的语法学习并非渐进单调的，而是经历了一系列**隐藏的突破阶段**——先学习词频偏好、再学习局部上下文（n-gram），最后逐步掌握更远距离的语法依赖关系。

**[Do Different Prompting Methods Yield a Common Task Representation in Language Models?](do_different_prompting_methods_yield_a_common_task_representation_in_language_mo.md)**

:   本文扩展函数向量方法至指令提示，发现演示和指令诱发的任务表示主要不同，仅部分重叠，解释了为何结合两者效果更优。

**[Do Language Models Use Their Depth Efficiently?](do_language_models_use_their_depth_efficiently.md)**

:   通过因果干预、残差流分析和跨模型线性映射，证明当前 LLM 后半部分层不参与组合式计算，仅迭代细化输出概率分布，深层模型只是把浅层模型的计算"展延"到更多层。

**[Does Object Binding Naturally Emerge in Large Pretrained Vision Transformers?](does_object_binding_naturally_emerge_in_large_pretrained_vision_transformers.md)**

:   通过定义 IsSameObject 谓词并设计二次探针，证明大规模预训练 ViT（尤其是 DINO、CLIP）自然涌现了目标绑定能力，该信号编码在低维子空间中并主动引导注意力机制，挑战了认知科学界认为 ViT 缺乏绑定能力的观点。

**[Don't Be Lazy: CompleteP Enables Compute-Efficient Deep Transformers](dont_be_lazy_completep_enables_compute-efficient_deep_transformers.md)**

:   CompleteP 参数化（α=1）是唯一同时实现深度方向超参转移和完全特征学习的方案，在深模型上相比 μP 节省 12-34% FLOPs。

**[Emergence of Linear Truth Encodings in Language Models](emergence_of_linear_truth_encodings_in_language_models.md)**

:   提出 **Truth Co-occurrence Hypothesis (TCH)**——真实陈述倾向于与其他真实陈述共现——并通过一个最简单的单层 Transformer 玩具模型，端到端地展示了线性真值子空间如何通过两阶段训练动态（先记忆 → 后编码真值）自然涌现，为理解 LLM 中广泛报告的线性真值表示提供了首个机制性解释。

**[EnCompass: Enhancing Agent Programming with Search Over Program Execution Paths](encompass_enhancing_agent_programming_with_search_over_program_execution_paths.md)**

:   提出 Probabilistic Angelic Nondeterminism (PAN) 编程模型及 EnCompass Python 框架，将 agent 的核心工作流逻辑与推理时搜索策略解耦，程序员只需在 LLM 调用处加 `branchpoint()` 标记，即可用几行参数切换 best-of-N、beam search、tree search 等策略，代码修改量减少 3-6x。

**[Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](enhancing_multilingual_llm_pretraining_with_model-based_data_selection.md)**

:   提出一套透明、简洁、高效的多语言模型驱动数据筛选框架，利用 FastText 和 Transformer（XLM-RoBERTa）嵌入分类器识别结构化且知识丰富的样本，在 FineWeb-2 数据集上仅用 15% 的 token 即可匹配基线 MMLU 分数，并将该框架扩展至 20 种语言并公开发布了精炼的预训练数据集。

**[Enhancing Training Data Attribution with Representational Optimization](enhancing_training_data_attribution_with_representational_optimization.md)**

:   提出 AirRep（Attentive Influence Ranking Representation），一种基于表示学习的训练数据归因方法，通过可训练编码器和注意力池化机制，在推理效率比梯度方法快约 80 倍的同时，达到甚至超越 SOTA 梯度方法的归因精度。

**[EvaLearn: Quantifying the Learning Capability and Efficiency of LLMs via Sequential Problem Solving](evalearn_quantifying_the_learning_capability_and_efficiency_of_llms_via_sequenti.md)**

:   提出 EvaLearn 基准，通过**序列化问题求解**范式评估 LLM 的学习能力和学习效率，揭示静态能力强的模型不一定具备更强的学习潜力。

**[Evaluating Multiple Models Using Labeled and Unlabeled Data](evaluating_multiple_models_using_labeled_and_unlabeled_data.md)**

:   提出 **SSME (Semi-Supervised Model Evaluation)**，利用少量标注数据和大量未标注数据，通过半监督混合模型估计多个分类器联合分布 $P(y, \mathbf{s})$，实现精确的分类器性能评估，误差降低至仅用标注数据的 1/5。

**[EvoRefuse: Evolutionary Prompt Optimization for Evaluation and Mitigation of LLM Over-Refusal](evorefuse_evolutionary_prompt_optimization_for_evaluation_and_mitigation_of_llm_.md)**

:   提出 EvoRefuse——用进化搜索（变异/重组 + ELBO 适应度 + 模拟退火）生成语义无害但能可靠触发 LLM 拒绝的"伪恶意"指令，比最强基线的拒绝触发率高 85.34%，并用生成的数据进行 SFT/DPO 微调，将过度拒绝降低 29.85%-45.96%。

**[Exploiting Vocabulary Frequency Imbalance in Language Model Pre-training](exploiting_vocabulary_frequency_imbalance_in_language_model_pre-training.md)**

:   通过控制实验揭示大词表提升语言模型性能的根本机制：**扩大词表降低分词文本的 Kolmogorov 复杂度，利用词频不平衡让高频词损失大幅下降，驱动全局交叉熵下降和下游任务提升**。

**[Gemstones: A Model Suite for Multi-Faceted Scaling Laws](gemstones_a_model_suite_for_multi-faceted_scaling_laws.md)**

:   Gemstones开源4000+检查点数据集（至2B参数），系统研究宽度-深度-训练代币在缩放律中的影响，揭示缩放律对设计选择的高度敏感性。

**[GeoCAD: Local Geometry-Controllable CAD Generation with Large Language Models](geocad_local_geometry-controllable_cad_generation_with_large_language_models.md)**

:   提出 GeoCAD，首个实现局部几何可控 CAD 生成的方法，通过互补标注策略为局部零件生成几何指令，并微调 LLM 实现根据用户文本指令精确修改 CAD 模型的局部部分。

**[Global Minimizers of Sigmoid Contrastive Loss](global_minimizers_of_sigmoid_contrastive_loss.md)**

:   首次在实践相关的 N≫d 区间严格刻画了 Sigmoid 对比损失（SigLIP）在可训练温度和偏置下的全局最小值几何结构，提出了 (m, b_rel)-Constellation 这一新型组合对象，并用其解释了 SigLIP 的检索成功、模态间隙现象，以及提出了显式 relative bias 参数化改进训练动态。

**[Hierarchical Retrieval: The Geometry and a Pretrain-Finetune Recipe](hierarchical_retrieval_the_geometry_and_a_pretrain-finetune_recipe.md)**

:   研究双编码器（Dual Encoder）在层次化检索（Hierarchical Retrieval）中的可行性，理论证明嵌入维度只需与层次深度线性、文档数对数增长即可求解，并发现"远距离丢失"现象后提出预训练-微调策略，在 WordNet 上将远距离召回率从 19% 提升至 76%。

**[How Do Transformers Learn Implicit Reasoning?](how_do_transformers_learn_implicit_reasoning.md)**

:   通过符号环境的精细控制研究，本文发现多跳隐式推理会经历记忆→分布内泛化→跨分布泛化三阶段，关键机制是中间实体表示在余弦空间的聚类。

**[HybridNorm: Towards Stable and Efficient Transformer Training via Hybrid Normalization](hybridnorm_towards_stable_and_efficient_transformer_training_via_hybrid_normaliz.md)**

:   提出 HybridNorm 混合归一化策略——注意力模块用 QKV 归一化解耦梯度、FFN 用 Post-Norm 增强正则化，在 550M-7B 规模上同时获得 Pre-Norm 的训练稳定性和 Post-Norm 的泛化性能，7B 模型下游任务平均提升 2.45%。

**[Hyperparameter Transfer Enables Consistent Gains Of Matrix-Preconditioned Optimi](hyperparameter_transfer_enables_consistent_gains_of_matrix-preconditioned_optimi.md)**

:   研究矩阵预条件优化器（Shampoo/SOAP/Muon）的超参数随模型宽度和深度的缩放规则（基于 μP），发现正确的超参缩放是实现一致加速的关键：使用 μP + 1/width weight decay，三者在 190M 到 1.4B 参数的 Llama 模型上一致实现约 1.4× 加速。

**[In-Context Learning of Linear Dynamical Systems with Transformers: Approximation Bounds and Depth-Separation](in-context_learning_of_linear_dynamical_systems_with_transformers_approximation_.md)**

:   分析了线性 Transformer 在噪声线性动力系统上的 ICL 近似能力：$O(\log T)$ 深度可达到 $O(\log T / T)$ 测试误差（接近最小二乘估计器），而单层线性 Transformer 存在不可消除的下界——揭示了非 IID 数据下的深度分离现象。

**[Ineq-Comp: Benchmarking Human-Intuitive Compositional Reasoning in Automated Theorem Proving on Inequalities](ineq-comp_benchmarking_human-intuitive_compositional_reasoning_in_automated_theo.md)**

:   提出 Ineq-Comp 基准，通过对简单不等式种子问题施加人类直觉可轻松处理的组合变换（变量复制、代数重写），揭示当前 LLM 形式化定理证明器在组合推理上的根本性缺陷——即使 DeepSeek-Prover-V2-7B 也有 20%+ 的性能下降。

**[Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale](language_model_behavioral_phases_are_consistent_across_archi.md)**

:   论文在 Transformer、Mamba、RWKV，不同数据集与参数规模（14M 到 12B）上系统分析 1400+ checkpoints，发现语言模型预训练中存在高度一致的行为阶段；词级行为变化最多可由 unigram 频率、n-gram 概率、语义相似度三类简单启发式解释（最高约 98% 方差）。

**[Large Language Models Miss the Multi-Agent Mark](large_language_models_miss_the_multi-agent_mark.md)**

:   Position paper 指出当前 MAS LLMs 在四个方面违背了传统多智能体系统（MAS）的基本原则：LLM 缺乏原生社会行为、环境设计以 LLM 为中心、缺少异步协调和标准通信协议、涌现行为缺乏量化评估，并为每个问题提出研究方向。

**[LCDB 1.1: A Database Illustrating Learning Curves Are More Ill-Behaved Than Previously Thought](lcdb_11_a_database_illustrating_learning_curves_are_more_ill-behaved_than_previo.md)**

:   构建了大规模高分辨率学习曲线数据库 LCDB 1.1，证明样本学习曲线的"病态行为"（非单调、非凸）比此前认为的普遍两倍，约 15% 的曲线显著不良，且特征缩放难以修复。

**[Learning the Wrong Lessons: Syntactic-Domain Spurious Correlations in Language Models](learning_the_wrong_lessons_syntactic-domain_spurious_correlations_in_language_mo.md)**

:   揭示 LLM 学会了句法模板（PoS n-gram）与领域之间的虚假关联，导致跨域性能骤降，甚至可利用此关联绕过安全拒绝机制（refusal bypass），在 OLMo-2 上将拒绝率从 40% 降至 2.5%。

**[Leveraging Importance Sampling to Detach Alignment Modules from Large Language Models](leveraging_importance_sampling_to_detach_alignment_modules_from_large_language_m.md)**

:   提出 Residual Alignment Model (RAM)，将 LLM 对齐过程形式化为重要性采样，将大模型分解为冻结的 Proposal Module 和可训练的小型 Residual Aligner，以不到 1/8 参数实现可比甚至超越全参数 SFT/DPO 的对齐效果，同时解决了首 token 延迟问题。

**[Leveraging Robust Optimization for LLM Alignment under Distribution Shifts](leveraging_robust_optimization_for_llm_alignment_under_distribution_shifts.md)**

:   提出 DoRA（Distribution-aware optimization for Robust Alignment），通过训练分布分类器为每个样本分配校准权重，结合 KL-DRO 框架最小化最坏情况损失，以模型无关的即插即用方式提升多种对齐算法在分布偏移下的鲁棒性，在 DPO/RRHF/LIRE 等基线上一致提升性能。

**[Linear Transformers Implicitly Discover Unified Numerical Algorithms](linear_transformers_implicitly_discover_unified_numerical_algorithms.md)**

:   训练线性 Transformer 执行矩阵块补全任务后，通过权重代数分析发现模型在三种完全不同的计算约束（集中式、分布式、计算受限）下隐式收敛到同一个双行迭代更新规则 EAGLE，该规则具有二阶收敛性且依赖条件数仅为对数级别。

**[LLM Probing with Contrastive Eigenproblems: Improving Understanding and Applicability of CCS](llm_probing_with_contrastive_eigenproblems_improving_understanding_and_applicabi.md)**

:   本文对无监督探测方法 CCS（Contrast-Consistent Search）进行了深入分析，提出将 CCS 重新表述为特征值问题（Contrastive Eigenproblems），获得闭式解和可解释的特征值，避免了 CCS 对随机初始化的敏感性，并自然扩展到多变量设置。

**[LTD-Bench: Evaluating Large Language Models by Letting Them Draw](ltd-bench_evaluating_large_language_models_by_letting_them_draw.md)**

:   LTD-Bench 通过让 LLM 画画（生成点阵或代码绘图）来评估其空间推理能力，将抽象的评分指标转化为直观可视的输出，揭示了当前先进 LLM 在建立语言与空间概念双向映射方面的严重不足。

**[Memory Mosaics at Scale](memory_mosaics_at_scale.md)**

:   Memory Mosaics v2 将关联存储网络扩展至 10B 参数、1T token 训练规模，在新任务学习和上下文学习上显著超越同规模甚至 8T token 训练的 Transformer。

**[MergeBench: A Benchmark for Merging Domain-Specialized LLMs](mergebench_a_benchmark_for_merging_domain-specialized_llms.md)**

:   MergeBench 是首个全面评估大规模领域特化 LLM 合并的基准套件，覆盖 Llama 和 Gemma 系列最大 9B 模型、五大任务领域和八种合并方法，从多任务性能、遗忘、运行效率三个维度提供系统化评估和实用指南。

**[MetaMind: Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems](metamind_modeling_human_social_thoughts_with_metacognitive_multi-agent_systems.md)**

:   提出 MetaMind——一个受心理学元认知理论启发的多智能体框架，通过 ToM Agent（心理状态假设生成）、Moral Agent（社会规范约束精炼）和 Response Agent（响应生成与自我验证）三阶段协作，显著提升 LLM 的社会推理能力，在多个社会智能基准上达到 SOTA 并首次接近人类水平。

**[Mind the Gap: Removing the Discretization Gap in Differentiable Logic Gate Networks](mind_the_gap_removing_the_discretization_gap_in_differentiable_logic_gate_networ.md)**

:   提出 Gumbel Logic Gate Networks (Gumbel LGNs)，通过在逻辑门选择中注入 Gumbel 噪声并使用直通估计器 (ST estimator)，将可微逻辑门网络的离散化差距减少 98%，训练速度提升 4.5 倍，未使用神经元比例降为 0%。

**[MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](mitra_an_ai_assistant_for_knowledge_retrieval_in_physics_collaborations.md)**

:   提出 MITRA，一个面向大型物理实验协作（如 CERN CMS）的本地化 RAG 系统，采用两层向量数据库架构（摘要库 + 全文库）和完全本地部署策略，在语义检索任务上显著优于传统关键词搜索（BM25），Precision@1 从 0.13 提升至 0.75。

**[MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research](mlr-bench_evaluating_ai_agents_on_open-ended_machine_learning_research.md)**

:   提出 MLR-Bench，一个包含 201 个开放式 ML 研究任务的综合基准，配套 MLR-Judge（LLM 评审框架）和 MLR-Agent（模块化研究代理），发现当前最先进的编码代理在约 80% 的情况下会生成伪造或未验证的实验结果，揭示了 AI 自动化科学研究的核心瓶颈。

**[MonarchAttention: Zero-Shot Conversion to Fast, Hardware-Aware Structured Attention](monarchattention_zero-shot_conversion_to_fast_hardware-aware_structured_attentio.md)**

:   提出 MonarchAttention，利用 Monarch 矩阵的结构化特性，通过 softmax 变分形式的交替优化，实现 $\Theta(N\sqrt{N}d)$ 复杂度的注意力近似，无需额外训练即可零样本替换预训练 Transformer 的注意力层，同时在 GPU 上相比 FlashAttention-2 实现 1.4×–8.2× 的加速。

**[Monte Carlo Expected Threat (MOCET) Scoring](monte_carlo_expected_threat_mocet_scoring.md)**

:   提出 MOCET（Monte Carlo Expected Threat）评分框架，通过将 LLM 生成的生物武器制造协议分解为逐步 Bernoulli 试验，结合 k-NN 语义嵌入的成功概率估计和蒙特卡洛模拟，生成可解释的、可自动化的威胁量化指标，用于衡量 LLM 在生物安全领域的真实世界风险。

**[MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery](moose-chem2_exploring_llm_limits_in_fine-grained_scientific_hypothesis_discovery.md)**

:   将细粒度科学假设生成形式化为组合优化问题，提出层次启发式搜索（HHS）——利用 LLM 的成对比较作为梯度信号在假设空间中导航，层次化抽象平滑奖励景观减少局部最优陷阱，在 2024 年后化学论文 51 篇的专家标注 benchmark 上 Soft Recall 从 19.99% 提升到 40.35%。

**[msf-CNN: Patch-based Multi-Stage Fusion with Convolutional Neural Networks for TinyML](msf-cnn_patch-based_multi-stage_fusion_with_convolutional_neural_networks_for_ti.md)**

:   提出 msf-CNN，一种基于有向无环图（DAG）最短路径算法的多阶段 patch-based 融合优化技术，通过高效搜索 CNN 的最优融合配置，在各种微控制器（ARM Cortex-M、RISC-V、ESP32）上实现比现有方法（MCUNetV2、StreamNet）减少 50%–87% 的峰值 RAM 使用，同时保持可控的计算开销。

**[MuRating: A High Quality Data Selecting Approach to Multilingual Large Language Model Pretraining](murating_a_high_quality_data_selecting_approach_to_multilingual_large_language_m.md)**

:   提出 MuRating，一个可扩展的多语言数据选择框架：先通过配对比较聚合多个英文数据质量评分器，再借助翻译将质量信号迁移到 17 种语言，训练出语言无关的多语言质量评估模型，在 1.2B 和 7B 规模 LLM 预训练中取得了持续的性能提升。

**[Nemotron-CLIMB: CLustering-based Iterative Data Mixture Bootstrapping for Language Model Pre-training](nemotron-climb_clustering-based_iterative_data_mixture_bootstrapping_for_languag.md)**

:   NVIDIA 提出 CLIMB 框架，通过嵌入聚类 + 迭代自举搜索自动发现最优预训练数据混合比例，在 1B 模型上超过 Llama-3.2-1B 达 2.0%，并发布了 1.2T token 的 ClimbLab 语料库和 400B token 的 ClimbMix 高质量数据集。

**[Nemotron-Flash: Towards Latency-Optimal Hybrid Small Language Models](nemotron-flash_towards_latency-optimal_hybrid_small_language_models.md)**

:   Nemotron-Flash 通过系统优化深宽比、进化搜索混合算子组合（DeltaNet+Mamba2+Attention）以及权重归一化训练，构建延迟最优的小语言模型家族，相比 Qwen3-1.7B/0.6B 分别实现 1.3×/1.9× 延迟下降与 +5.5% 平均准确率提升。

**[On Evaluating LLM Alignment by Evaluating LLMs as Judges](on_evaluating_llm_alignment_by_evaluating_llms_as_judges.md)**

:   本文系统研究了 LLM 的生成能力与评估能力之间的一致性（GE-consistency），发现两者在强偏好预言机下高度相关（Spearman ρ=0.96），据此提出 AlignEval 基准——通过评估 LLM 作为评判者的能力来衡量其对齐水平，无需 LLM-as-Judge 直接评估模型输出，与 AlpacaEval/Arena-Hard 相当甚至更优。

**[On the Role of Hidden States of Modern Hopfield Network in Transformer](on_the_role_of_hidden_states_of_modern_hopfield_network_in_transformer.md)**

:   本文突破现代 Hopfield 网络（MHN）与 Transformer 对应关系的绝热近似限制，发现保留 MHN 的隐状态动力学会在自注意力层中引入跨层注意力分数传播机制（Modern Hopfield Attention, MHA），不增加训练参数即可系统性改善 ViT 和 GPT-2 的性能，并从理论和实验上证明 MHA 有效缓解了深层 Transformer 的 rank collapse 问题。

**[Opinion Maximization in Social Networks by Modifying Internal Opinions](opinion_maximization_in_social_networks_by_modifying_internal_opinions.md)**

:   本文研究社交网络中通过修改 k 个关键节点的内部意见来最大化整体意见的优化问题，提出了两种基于采样的近似算法（随机游走和森林采样）以及一种基于异步更新的精确算法 MIS，后者在理论上保证收敛到最优解，并在数千万节点的真实网络上展示了卓越的效率与精度。

**[OptiTree: Hierarchical Thoughts Generation with Tree Search for LLM Optimization Modeling](optitree_hierarchical_thoughts_generation_with_tree_search_for_llm_optimization_.md)**

:   提出 OptiTree，通过构建建模树（modeling tree）组织运筹优化问题的层次化分类与建模思维，利用树搜索将复杂问题自适应分解为更简单的子问题序列，显著提升 LLM 在优化建模任务上的准确率（在多个困难基准上提升超过 10%）。

**[PaTH Attention: Position Encoding via Accumulating Householder Transformations](path_attention_position_encoding_via_accumulating_householder_transformations.md)**

:   提出 PaTH（Position encoding via accumulating Householder Transformations），一种数据依赖的乘法位置编码方案，通过累积 Householder 变换替代 RoPE 的静态旋转矩阵，在理论表达力和实际语言建模性能上均优于 RoPE。

**[PluralisticBehaviorSuite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies](pluralistic_behavior_suite_stress-testing_multi-turn_adherence_to_custom_behavio.md)**

:   提出 PBSuite，一个包含 300 个行业定制行为策略和动态多轮对抗评估框架的评测套件，揭示了主流 LLM 在单轮设置下合规率高（违规 <4%），但在多轮对抗交互中合规性急剧下降（违规高达 84%）。

**[Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity](polar_sparsity_high_throughput_batched_llm_inferencing_with_scalable_contextual_.md)**

:   揭示了 LLM 推理中稀疏性的"极性转移"现象——MLP 层稀疏性随 batch 增大而消失，而 attention head 稀疏性保持稳定且与 batch 无关，据此设计了 Selective Head Attention 及对应 GPU kernel，在大 batch 推理中实现高达 2.2x 的端到端加速。

**[Post Hoc Regression Refinement via Pairwise Rankings](post_hoc_regression_refinement_via_pairwise_rankings.md)**

:   提出 RankRefine，一种模型无关的后处理回归改进方法，通过将基础回归器的预测与基于成对排序的估计进行逆方差加权融合，在无需重训练的情况下显著降低预测误差，仅需 20 次成对比较和通用 LLM 即可实现分子性质预测中高达 10% 的 MAE 相对减少。

**[Power Lines: Scaling Laws for Weight Decay and Batch Size in LLM Pre-training](power_lines_scaling_laws_for_weight_decay_and_batch_size_in_llm_pre-training.md)**

:   提出了一套针对 LLM 预训练中权重衰减 $\lambda$ 和批大小 $B$ 的幂律缩放定律（power laws），通过 AdamW 时间尺度 $\tau$ 的概念统一了超参数缩放关系，使得在大规模训练前即可准确预测最优超参数。

**[PRESTO: Preimage-Informed Instruction Optimization for Prompting Black-Box LLMs](presto_preimage-informed_instruction_optimization_for_prompting_black-box_llms.md)**

:   提出 PRESTO 框架，利用白盒 LLM 中 soft prompt 到 instruction 的 many-to-one 映射关系（preimage 结构），通过 score sharing、preimage-based initialization 和 score consistency regularization 三大组件，在相同查询预算下等效获得 14 倍的标注数据量，显著提升黑盒 LLM 的指令优化效率。

**[Probabilistic Token Alignment for Large Language Model Fusion](probabilistic_token_alignment_for_large_language_model_fusion.md)**

:   将 LLM 融合中的 token 对齐问题重新建模为最优传输（Optimal Transport）问题，用动态 token 配对 + Sinkhorn 算法实现"软"概率对齐取代传统硬映射，在 6 大基准 78 个任务上相比 FuseLLM 平均提升 +1.72%，同时在困难任务上大幅缓解性能退化（从 -13.04% 降至 -4.07%）。

**[Quantifying Climate Policy Action and Its Links to Development Outcomes: A Cross-National Data-Driven Analysis](quantifying_climate_policy_action_and_its_links_to_development_outcomes_a_cross-.md)**

:   构建了从 NLP 文本分类到计量经济分析的跨国气候政策分析框架：利用多语言 DistilBERT 对气候政策文档自动分类（Mitigation / Adaptation / DRM / Loss & Damage），再与世界银行发展指标做固定效应面板回归，揭示不同类型气候政策与发展结果的关联。

**[Reliable Decision Making via Calibration Oriented Retrieval Augmented Generation](reliable_decision_making_via_calibration_oriented_retrieval_augmented_generation.md)**

:   提出 CalibRAG 框架，通过训练一个温度条件化的 forecasting function 来确保 RAG 辅助决策过程中的置信度校准，不仅改善校准质量还提升了准确率。

**[Reparameterized LLM Training via Orthogonal Equivalence Transformation](reparameterized_llm_training_via_orthogonal_equivalence_transformation.md)**

:   提出 POET 训练框架，通过将权重矩阵重参数化为"两个可学习正交矩阵 × 固定随机权重"的形式来保持谱性质不变，实现更稳定的训练和更好的泛化，且比 AdamW 更节省参数。

**[Rethinking Residual Distribution in Locate-then-Edit Model Editing](rethinking_residual_distribution_in_locate-then-edit_model_editing.md)**

:   揭示 locate-then-edit 模型编辑中残差分配（residual distribution）机制引入的权重偏移误差会随分配距离、batch 大小和编辑序列长度增长，提出 BLUE（Boundary Layer UpdatE）策略仅更新首尾关键层，平均提升 35.59%。

**[Retrieval is Not Enough: Enhancing RAG Reasoning through Test-Time Critique and Optimization](retrieval_is_not_enough_enhancing_rag_reasoning_through_test-time_critique_and_o.md)**

:   提出 AlignRAG 框架，将 RAG 重新定义为"检索增强推理"，通过训练专用 Critic Language Model (CLM) 在测试时迭代批评和修正推理过程，解决推理与检索证据之间的错位问题，8B CLM 在 OOD 任务上超越 72B 标准 CLM。

**[Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models](retrospective_incontext_learning_for_temporal_credit_assignm.md)**

:   论文提出 RICL（Retrospective In-Context Learning），利用 LLM 的预训练知识把环境中的稀疏奖励回溯性转化为稠密 advantage supervision，再结合在线策略迭代框架 RICOL，在 BabyAI 四个场景中以更高样本效率达到与传统在线 RL 相当的收敛表现，展示了 LLM 在 temporal credit assignment 上的潜力。

**[Scalable Fingerprinting of Large Language Models](scalable_fingerprinting_of_large_language_models.md)**

:   提出 Perinucleus 采样方法生成可扩展的 LLM 指纹，能在 Llama-3.1-8B 上嵌入 24,576 个指纹（比现有方法多两个数量级）且不损害模型能力，并通过理论和实验证明大规模指纹是抵御共谋攻击的关键。

**[Scaling Embedding Layers in Language Models](scaling_embedding_layers_in_language_models.md)**

:   提出Scone方法，通过为高频n-gram学习上下文化的嵌入（用独立Transformer模型训练），在推理时将这些嵌入卸载到主存/SSD，实现"训练时用更多计算但推理时不增加加速器资源"的新缩放范式，1B参数模型超越1.9B基线。

**[Scaling Up Active Testing to Large Language Models](scaling_up_active_testing_to_large_language_models.md)**

:   通过三项关键简化——用 in-context learning 构建固定代理模型、使用小代理模型评估大目标模型、无需目标模型预测进行数据采集——将 active testing 扩展到 LLM，风险估计误差比随机采样降低 25%-80%。

**[SIMU: Selective Influence Machine Unlearning](simu_selective_influence_machine_unlearning.md)**

:   提出 SIMU 两阶段框架：先通过梯度聚合识别编码遗忘集信息的关键 MLP 神经元，再仅对这些神经元进行二阶（Sophia）优化遗忘，在保持遗忘效果的同时大幅提升模型原有能力的保留。

**[Sloth: Scaling Laws for LLM Skills to Predict Multi-Benchmark Performance Across Families](sloth_scaling_laws_for_llm_skills_to_predict_multi-benchmark_performance_across_.md)**

:   提出Skills Scaling Laws (Sloth)，通过假设LLM性能由低维潜在技能（如推理、指令遵循）驱动，利用benchmark间的相关性构建跨模型家族的缩放定律，用少量家族数据即可预测大模型在多个benchmark上的表现。

**[Small Language Models as Compiler Experts: Auto-Parallelization for Heterogeneous Systems](small_language_models_as_compiler_experts_auto-parallelization_for_heterogeneous.md)**

:   系统评估了三个小于 1.5B 参数的语言模型（gemma3、llama3.2、qwen2.5）在编译器自动并行化任务上的能力，使用六种推理策略在 11 个真实世界内核上实现平均 6.81x 加速、峰值 43.25x，证明小模型可作为强大的编译器优化推理引擎。

**[Solving Inequality Proofs with Large Language Models](solving_inequality_proofs_with_large_language_models.md)**

:   提出 IneqMath（首个大规模奥林匹克级不等式 benchmark），将不等式证明定义为两个可自动验证的子任务（界估计与关系预测），并开发五模块 LLM-as-Judge 框架，发现即便 o1 在逐步推理审查下整体准确率也不到 10%。

**[SPACE: Noise Contrastive Estimation Stabilizes Self-Play Fine-Tuning for Large Language Models](space_noise_contrastive_estimation_stabilizes_self-play_fine-tuning_for_large_la.md)**

:   提出 Space（Self-PlAy via Noise Contrastive Estimation），将噪声对比估计引入自对弈微调，通过独立优化真实和合成样本的绝对奖励值（而非相对差距），从根本上解决了 SPIN 等方法的不稳定收敛问题，并提供可证明的稳定收敛保证。

**[Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning](sparse_mezo_less_parameters_for_better_performance_in_zeroth-order_llm_fine-tuni.md)**

:   提出 Sparse MeZO（S-MeZO），通过观察到零阶梯度噪声对大权重影响更严重，选择性地仅对小权重进行零阶优化扰动和更新，在不增加内存开销的前提下实现了显著的性能提升（RTE 上 +9%）和收敛加速（3.5x）。

**[Spectral Conditioning of Attention Improves Transformer Performance](spectral_conditioning_of_attention_improves_transformer_performance.md)**

:   理论分析了 Transformer 注意力层 Jacobian 的条件数受 Query/Key/Value 矩阵条件数控制，提出谱调节注意力（Spectral Conditioned Attention），通过向 Q/K/V 矩阵添加固定校正项降低条件数，作为即插即用模块在图像分类、目标检测、NLP 等多任务上一致提升性能。

**[Stop DDoS Attacking the Research Community with AI-Generated Survey Papers](stop_ddos_attacking_the_research_community_with_ai-generated_survey_papers.md)**

:   这篇立场论文以"综述论文 DDoS 攻击"为隐喻，通过定量分析 arXiv 2020-2024 年间 10,063 篇 CS 综述论文，揭示 AI 生成综述的爆炸式增长趋势和质量问题，提出规范 AI 辅助综述写作和建设"动态活综述"的愿景。

**[Strassen Attention, Split VC Dimension and Compositionality in Transformers](strassen_attention_split_vc_dimension_and_compositionality_in_transformers.md)**

:   提出 Splitting VC 维度理论工具证明了单层 softmax Transformer（即使无限精度）在组合推理任务上的根本限制，并设计了具有亚立方时间复杂度的 Strassen 注意力机制来突破这些限制。

**[Superposition Yields Robust Neural Scaling](superposition_yields_robust_neural_scaling.md)**

:   揭示表示叠加（superposition）是神经缩放定律的核心驱动力：在强叠加区间，损失**通用地**与模型维度成反比（$L \propto 1/m$），且该行为与数据频率分布的具体形式无关，这与实际 LLM 的缩放行为一致。

**[Synergy over Discrepancy: A Partition-Based Approach to Multi-Domain LLM Fine-Tuning](synergy_over_discrepancy_a_partition-based_approach_to_multi-domain_llm_fine-tun.md)**

:   提出基于分区的多阶段微调框架，通过策略性地将多个域划分为子集（阶段），在最大化域间协同的同时最小化负迁移，并推导了新的泛化界来理论支撑该分区策略。

**[System Prompt Optimization with Meta-Learning](system_prompt_optimization_with_meta-learning.md)**

:   提出双层系统提示优化问题并设计 MetaSPO 元学习框架，通过外循环优化跨任务泛化的系统提示、内循环优化任务特定的用户提示，使优化后的系统提示在 14 个未见任务上显著超越基线。

**[Teaming LLMs to Detect and Mitigate Hallucinations](teaming_llms_to_detect_and_mitigate_hallucinations.md)**

:   提出 Consortium Consistency 方法，将单模型一致性方法（Self-Consistency 和 Semantic Entropy）扩展到多模型协作设置，通过聚合多个异构 LLM 的响应来实现更可靠的幻觉检测和缓解，同时降低推理成本。

**[The Curse of Depth in Large Language Models](the_curse_of_depth_in_large_language_models.md)**

:   揭示 Pre-LN Transformer 中输出方差指数增长导致深层退化为恒等映射的根本原因，提出无参数的 LayerNorm Scaling（LNS）策略——仅在 LayerNorm 后乘以 $1/\sqrt{\ell}$，将方差从指数增长压缩为多项式增长，在 130M-7B 全规模上稳定改进困惑度 5-8%。

**[The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?](the_non-linear_representation_dilemma_is_causal_abstraction_enough_for_mechanist.md)**

:   证明了当因果抽象（causal abstraction）中的对齐映射不受线性约束时，任意神经网络都可以被映射到任意算法，使得因果抽象变得平凡而无信息量，由此提出"非线性表示困境"——在对齐映射的复杂度与准确度之间缺乏原则性的权衡方式。

**[The Rise of Parameter Specialization for Knowledge Storage in Large Language Models](the_rise_of_parameter_specialization_for_knowledge_storage_in_large_language_mod.md)**

:   系统分析 20 个开源 LLM，发现更强的模型在 MLP 参数向量中展现出更高的知识特化程度（Parameter Specialization），即相似知识倾向于集中编码到少数参数向量中，并通过因果实验验证该特化程度与模型知识任务性能之间存在因果关系。

**[The Trilemma of Truth in Large Language Models](the_trilemma_of_truth_in_large_language_models.md)**

:   提出 sAwMIL（稀疏感知多实例学习）三类探测框架，结合 MIL 和保形预测，将 LLM 内部激活分类为 true/false/neither，揭示真假信号并非简单的双向对称编码，而是跨越多维子空间的分布式表征。

**[Thought Communication in Multiagent Collaboration](thought_communication_in_multiagent_collaboration.md)**

:   提出 ThoughtComm 框架，通过建立隐变量生成模型并提供可辨识性理论保证，让多个 LLM 智能体直接交换潜在"思想"（latent thoughts）而非自然语言，实现超越语言瓶颈的"心灵感应"式协作。

**[Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training](through_the_river_understanding_the_benefit_of_schedule-free_methods_for_languag.md)**

:   从 River-Valley 损失景观的几何视角深入分析 Schedule-Free (SF) 优化器，揭示 SF-AdamW 在不需要学习率衰减或权重平均的情况下自动沿"河流"方向优化，并提出改进变体解决动量敏感性和大批量训练的局限性。

**[Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs](triplets_better_than_pairs_towards_stable_and_effective_self-play_fine-tuning_fo.md)**

:   提出 T-SPIN（三元组自博弈微调），在 SPIN 基础上引入"历史优势"（proto-synthetic 响应作为锚点）和熵约束实现无参考策略训练，解决了 SPIN 迭代中的优化不稳定和训练-生成不对齐两大问题，仅用 25% 标注数据即可媲美全量 SFT。

**[Understanding And Enhancing Mask-Based Pretraining Towards Universal Representat](understanding_and_enhancing_mask-based_pretraining_towards_universal_representat.md)**

:   用高维线性回归理论精确刻画了 mask-based pretraining 中掩码率对测试风险的影响（偏差-方差分解），揭示了最优掩码率依赖于任务和模型大小，并据此提出 R2MAE（随机随机掩码），在视觉、语言、DNA、单细胞模型上一致超越固定掩码率。

**[Unifying Attention Heads and Task Vectors via Hidden State Geometry in In-Context Learning](unifying_attention_heads_and_task_vectors_via_hidden_state_geometry_in_in-contex.md)**

:   本文提出基于隐状态几何（可分离性+对齐性）的统一框架，将ICL的两大解释路线——注意力头（PTH/IH）和任务向量——联系起来，揭示ICL在分类任务中的两阶段机制：早期层通过PTH建立可分离性，后期层通过IH改善与标签unembedding方向的对齐性。

**[Valid Inference with Imperfect Synthetic Data](valid_inference_with_imperfect_synthetic_data.md)**

:   提出基于广义矩估计（GMM）的无超参数框架，将 LLM 生成的不完美合成数据与真实数据结合进行统计有效推断，当合成数据残差与真实数据残差相关时可显著降低估计方差，且在最坏情况下（合成数据完全无信息）也不会损害估计质量。

**[ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making](valuepilot_a_two-phase_framework_for_value-driven_decision-making.md)**

:   提出 ValuePilot 两阶段框架，通过数据集生成工具包（DGT）构建价值标注场景，再用决策模块（DMM）结合用户个性化价值偏好进行多准则决策，在与人类决策对齐方面超过 GPT-5 等强基线。

**[What Happens During the Loss Plateau? Understanding Abrupt Learning in Transformers](what_happens_during_the_loss_plateau_understanding_abrupt_learning_in_transforme.md)**

:   系统研究 Transformer 训练中的"突变学习"现象，揭示 loss 平台期内模型已学会部分解、同时表现出输出重复偏差和表示坍缩，并证明注意力图的缓慢学习是关键瓶颈，相关发现在 Pythia/OLMo 等 LLM 预训练早期也得到验证。

**[What One Cannot, Two Can: Two-Layer Transformers Provably Represent Induction Heads on Any-Order Markov Chains](what_one_cannot_two_can_two-layer_transformers_provably_represent_induction_head.md)**

:   理论证明两层单头 Transformer 足以表示任意 $k$ 阶马尔可夫过程的条件 $k$-gram 模型（即 $k$ 阶 induction head），给出了 Transformer 深度与马尔可夫阶数关系的最紧已知刻画，关键在于利用 MLP 中的 ReLU 和 LayerNorm 非线性来补偿减少的层数。

**[Worse than Zero-shot? A Fact-Checking Dataset for Evaluating the Robustness of RAG Against Misleading Retrievals](worse_than_zero-shot_a_fact-checking_dataset_for_evaluating_the_robustness_of_ra.md)**

:   提出 RAGuard 基准数据集，首次系统评估 RAG 系统对误导性检索内容的鲁棒性。通过从 Reddit 构建包含支持性、误导性和无关文档的真实检索语料库，揭示所有测试的 LLM-RAG 系统在面对误导性检索时表现**比零样本基线更差**，而人类标注者能保持一致判断。

**[Writing in Symbiosis: Mapping Human Creative Agency in the AI Era](writing_in_symbiosis_mapping_human_creative_agency_in_the_ai_era.md)**

:   通过对 5 万+文档的纵向语料分析，提出"双轨演化"假说——LLM 时代人类写作在主题上趋同、风格上结构性分化，并发现三种作者适应策略原型（Adopters/Resistors/Pragmatists）。

**[Yggdrasil: 桥接动态投机和静态运行时的延迟最优树型LLM解码](yggdrasil_bridging_dynamic_speculation_and_static_runtime_for_latency-optimal_tr.md)**

:   通过等增长树(EGT)草稿算法和延迟感知目标，实现动态投机与静态图编译的兼容，配合前向执行阶段重叠，在A100上达3.98×加速。

**[Your Pre-trained LLM is Secretly an Unsupervised Confidence Calibrator](your_pre-trained_llm_is_secretly_an_unsupervised_confidence_calibrator.md)**

:   发现 LLM 后训练（SFT/RLHF/DPO）破坏了预训练模型的置信度校准，提出 DACA 方法利用预训练模型的良好校准性，仅在预测一致样本上对齐置信度，实现无标签的后训练模型校准，ECE 最高改善 15.08%。

**[Zero-Shot Performance Prediction for Probabilistic Scaling Laws](zero-shot_performance_prediction_for_probabilistic_scaling_laws.md)**

:   将 NLP 学习曲线预测建模为多任务学习问题，利用潜变量多输出高斯过程（MaGP）捕捉数据集中的双层层次结构和任务间相关性，实现学习曲线的零样本预测，并通过蒙特卡洛模拟推导概率化的 Scaling Laws。
