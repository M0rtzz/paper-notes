<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🔬 ICLR2026** · 共 **126** 篇

**[A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA](a_fano-style_accuracy_upper_bound_for_llm_single-pass_reasoning_in_multi-hop_qa.md)**

:   用信息论推导出 LLM 单次推理在多跳 QA 中的 Fano 式准确率上界，揭示当任务信息需求超过模型输出容量时准确率会"悬崖式"骤降的现象，并据此设计多轮推理框架 InfoQA，通过容量感知分解、依赖显式工作流和迭代查询压缩来突破单次推理瓶颈。

**[A Recovery Guarantee for Sparse Neural Networks](a_recovery_guarantee_for_sparse_neural_networks.md)**

:   证明了 ReLU 神经网络的首个稀疏恢复保证：对两层标量输出网络，当训练数据为高斯随机采样时，基于凸重构的迭代硬阈值 (IHT) 算法可精确恢复稀疏网络权重，且内存需求仅与非零权重数线性增长。

**[A State-Transition Framework for Efficient LLM Reasoning](a_state-transition_framework_for_efficient_llm_reasoning.md)**

:   提出将 LLM 推理过程建模为状态转移过程的高效推理框架，用 Linear Attention 将历史推理步骤的信息压缩为状态矩阵，使注意力复杂度从 $O(C^2)$ 降为 $O(C)$、KV cache 从 $O(C)$ 降为 $O(1)$，同时不缩短 CoT 序列，保持推理能力。额外的动量 momentum 策略缓解了噪声推理步导致的 overthinking 问题。

**[A universal compression theory for lottery ticket hypothesis and neural scaling laws](a_universal_compression_theory_for_lottery_ticket_hypothesis_and_neural_scaling_.md)**

:   本文证明了一个通用压缩定理：任意置换不变函数可以被渐近压缩至 polylog(d) 规模且误差趋近于零（这是最优压缩率），由此直接推导出动态彩票假说的证明——任何网络可被压缩至多对数宽度同时保持学习动力学不变，以及数据集可被压缩至多对数大小同时保持损失景观不变，并且幂律缩放定律可被加速至任意快的衰减率。

**[ABBA-Adapters: Efficient and Expressive Fine-Tuning of Foundation Models](abba-adapters_efficient_and_expressive_fine-tuning_of_foundation_models.md)**

:   提出 ABBA 适配器，将权重更新参数化为两个独立可学习的低秩矩阵的 Hadamard 积 $\Delta W = s(B_1A_1) \odot (B_2A_2)$，在相同参数预算下实现远高于 LoRA 的有效秩（$r_1 \cdot r_2$ vs $r$），并通过 Khatri-Rao 重构实现与 LoRA 相当的内存效率，在算术和常识推理任务上显著超越现有 PEFT 方法。

**[ACPBench Hard: Unrestrained Reasoning about Action, Change, and Planning](acpbench_hard_unrestrained_reasoning_about_action_change_and_planning.md)**

:   构建 ACPBench Hard，一个基于 PDDL 规划的 8 类开放式生成推理 benchmark（1040 题），要求 LLM 生成可适用动作集、状态转移、可达性判断、里程碑识别、计划验证等，配备精确的符号验证器，测试发现即使最强的推理模型（o1）在多数任务上也低于 65%，暴露了 LLM 在规划推理方面的根本不足。

**[ActivationReasoning: Logical Reasoning in Latent Activation Spaces](activationreasoning_logical_reasoning_in_latent_activation_spaces.md)**

:   提出 ActivationReasoning (AR) 框架，在 LLM 的潜在激活空间（通过 SAE 提取的特征）上嵌入显式逻辑推理，通过三阶段流程（发现概念表征→检测激活命题→逻辑规则推理）实现多跳推理、概念组合和安全控制，在 PrOntoQA 上 8B 模型达到 95%+ 准确率超越 GPT-4o。

**[Adaptive Width Neural Networks](adaptive_width_neural_networks.md)**

:   提出AWN框架，通过变分推断在训练过程中自动学习每层的无上界宽度（神经元数量），利用单调递减的重要性函数对神经元施加软排序，实现宽度自适应于任务难度，并支持零成本的训练后截断压缩。

**[AMiD: Knowledge Distillation for LLMs with α-mixture Assistant Distribution](amid_knowledge_distillation_for_llms_with_α-mixture_assistant_distribution.md)**

:   提出α-mixture assistant distribution及统一蒸馏框架AMiD，通过引入新设计变量α（控制教师-学生分布插值路径的几何形状）泛化了现有辅助分布方法（m-mixture和e-mixture为α=±1的特例），并证明了在任意散度和α下的最优性保证，在多个LLM蒸馏基准上取得SOTA性能。

**[AnyBCQ: Hardware Efficient Flexible Binary-Coded Quantization for Multi-Precision LLMs](anybcq_hardware_efficient_flexible_binary-coded_quantization_for_multi-precision.md)**

:   提出AnyBCQ，基于二进制编码量化(BCQ)的多精度LLM量化框架，通过渐进式精度扩展（冻结已有bit-plane+添加残差bit-plane）支持单个模型在2-4bit之间动态切换，专设CUDA内核直接在bit-plane级别计算避免查表/转置开销，在2-bit下准确率大幅超越Any-Precision LLM（MMLU 35.3% vs 24.7%），吞吐量最高达到FP16的3.0x。

**[Beyond Linear Probes: Dynamic Safety Monitoring for Language Models](beyond_linear_probes_dynamic_safety_monitoring_for_language_models.md)**

:   提出截断多项式分类器（TPC），通过对 LLM 激活空间中的多项式逐阶训练和截断评估，实现动态安全监控——在简单输入上用低阶（≈线性探针）快速决策，在困难输入上增加高阶项提供更强防护，在 WildGuardMix 和 BeaverTails 两个数据集上匹敌或超越 MLP 基线且具备内置可解释性。

**[BeyondBench: Contamination-Resistant Evaluation of Reasoning in Language Models](beyondbench_contamination-resistant_evaluation_of_reasoning_in_language_models.md)**

:   提出BeyondBench评估框架，通过算法化动态生成数学问题（44个任务/117个变体/3个难度级别），确保每次测试不被训练数据污染，评估了101个语言模型（0.5B-141B参数），发现即使最强模型在Hard Suite上也仅达56%准确率，且不使用工具时性能大幅下降。

**[BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](biasscope_towards_automated_detection_of_bias_in_llm-as-a-judge_evaluation.md)**

:   提出 BiasScope，一个完全由 LLM 驱动的迭代式框架，能自动、大规模地发现 LLM-as-a-Judge 中的潜在未知偏差，并基于此构建了更具挑战性的 JudgeBench-Pro 基准，在其上即使强大的 LLM 评估器错误率也超过 50%。

**[Boomerang Distillation Enables Zero-Shot Model Size Interpolation](boomerang_distillation_enables_zero-shot_model_size_interpolation.md)**

:   发现并系统研究"回旋蒸馏"现象：从大模型（teacher）蒸馏出小模型（student）后，将教师的层块重新插回学生模型，无需任何额外训练即可构建任意中间尺寸的模型，其性能在 student 和 teacher 之间平滑插值，匹配甚至超越同等尺寸的独立蒸馏模型。

**[Boosting Entropy with Bell Box Quantization](boosting_entropy_with_bell_box_quantization.md)**

:   提出 Bell Box Quantization (BBQ)，首个同时满足"信息论最优"(ITO) 和"计算高效"(compute-efficient) 的量化方法，核心洞察是学习的域无关性——量化器输出域不必与输入域相同，由此在输入域做 ITO 量化以最大化熵，在输出域映射到硬件可加速的数据类型，在 1-4 bit QAPT 场景下全面超越 QuEST 和 LSQ。

**[BOTS: A Unified Framework for Bayesian Online Task Selection in LLM Reinforcement Finetuning](bots_a_unified_framework_for_bayesian_online_task_selection_in_llm_reinforcement.md)**

:   提出 BOTS 框架，将 LLM 强化微调中的在线任务选择建模为贝叶斯推断问题，通过融合显式证据（直接评估）和隐式证据（跨任务推断）来自适应估计任务难度，并利用 Thompson 采样平衡探索与利用，显著提升训练效率。

**[Bridging Kolmogorov Complexity and Deep Learning: Asymptotically Optimal Description Length Objectives for Transformers](bridging_kolmogorov_complexity_and_deep_learning_asymptotically_optimal_descript.md)**

:   从柯尔莫哥洛夫复杂度理论出发，提出了"渐近最优描述长度目标"的理论框架，证明了 Transformer 存在这样的目标函数（基于其计算通用性的新证明），并通过构造基于自适应高斯混合先验的可微变分目标进行了实证验证，揭示了重要的优化挑战。

**[COMI: Coarse-to-fine Context Compression via Marginal Information Gain](comi_coarse-to-fine_context_compression_via_marginal_information_gain.md)**

:   提出 COMI，一种基于边际信息增益（MIG = 查询相关性 - 语义冗余度）的粗到细自适应上下文压缩框架，在 32x 压缩率下 NaturalQuestions EM 比次优方法提高约 25 分，核心在于同时优化保留信息的相关性和多样性。

**[Compute-Optimal Quantization-Aware Training](compute-optimal_quantization-aware_training.md)**

:   本文通过 757 组 QAT 实验（86M-2.2B 参数，1-6 bit）发现：QAT 的最优训练比例随总计算量增长而增大（与先前认为固定 10% 的结论相反），并提出 tokens-per-parameter-byte 统计量和新的 loss scaling law 来精确预测最优 QAT 分配策略和最终损失。

**[Cross-Domain Lossy Compression via Rate- and Classification-Constrained Optimal Transport](cross_domain_lossy_compression_optimal_transport.md)**

:   将跨域有损压缩（编码器看退化源、解码器重建不同目标分布）形式化为带压缩率和分类损失双重约束的最优传输问题，推导出 Bernoulli/Gaussian 源的闭式 DRC（失真-率-分类）和 DRPC（失真-率-感知-分类）权衡曲线，在 KODAK 去噪上实现 PSNR 27.90 / SSIM 0.80 的竞争性能，审稿人给出 10/10 评分。

**[Cut Less, Fold More: Model Compression through the Lens of Projection Geometry](cut_less_fold_more_model_compression_through_the_lens_of_projection_geometry.md)**

:   从投影几何视角统一分析结构化剪枝（轴对齐投影）与模型折叠（低秩聚类投影），证明在秩差 1 的条件下折叠重建误差严格更小，并在超过 1000 个 checkpoint 上验证折叠在中高压缩率下通常优于剪枝。

**[Dataset Color Quantization: A Training-Oriented Framework for Dataset-Level Compression](dataset_color_quantization_a_training-oriented_framework_for_dataset-level_compr.md)**

:   提出 Dataset Color Quantization（DCQ）框架，通过色度感知聚类、注意力引导调色板分配和纹理保持优化三个机制，在数据集层面减少颜色冗余实现存储压缩，同时保持训练效果。

**[Dataset Distillation as Pushforward Optimal Quantization](dataset_distillation_as_pushforward_optimal_quantization.md)**

:   将解耦式数据集蒸馏重新形式化为最优量化问题，证明通过扩散先验的潜空间聚类+权重可收敛逼近真实数据分布，提出 DDOQ 算法在 ImageNet-1K 上以极低额外计算量超越 D4M 等基线。

**[DiaBlo: Diagonal Blocks Are Sufficient For Finetuning](diablo_diagonal_blocks_are_sufficient_for_finetuning.md)**

:   提出 DiaBlo，仅微调权重矩阵的对角块作为参数高效微调方法：避免了 LoRA 低秩矩阵乘积的优化难题，zero 初始化即可稳定收敛，GPU 友好的 batched 矩阵乘法实现，理论证明在参数预算相同时表达力严格优于 LoRA，在常识推理/算术推理/代码生成/安全对齐上全面优于 LoRA 及其变体。

**[Discount Model Search for Quality Diversity Optimization in High-Dimensional Measure Spaces](discount_model_search_for_quality_diversity_optimization_in_high-dimensional_mea.md)**

:   提出 Discount Model Search (DMS)，用神经网络拟合连续平滑的 discount 函数替代 CMA-MAE 中基于直方图的离散表示，解决高维 measure space 下 distortion 导致搜索停滞的问题，并首次实现以图像数据集直接定义 measure space（QDDM 范式）。

**[Distillation of Large Language Models via Concrete Score Matching](distillation_of_large_language_models_via_concrete_score_matching.md)**

:   提出 Concrete Score Distillation (CSD)，一种基于离散 score matching 的 LLM 知识蒸馏损失，通过匹配 student 和 teacher 在所有词表对之间的相对 logit 差异，同时克服了 softmax 平滑和直接 logit 蒸馏的解空间限制问题。

**[Draft-based Approximate Inference for LLMs](draft-based_approximate_inference_for_llms.md)**

:   提出 Draft-based Approximate Inference 框架，利用小型 draft 模型的前瞻（lookahead）预测来更准确地估计 token/KV pair 重要性，包含 SpecKV（KV cache dropping）、SpecPC（prompt 压缩）和 SpecKV-PC（级联压缩）三种方法，在长上下文 benchmark 上一致优于现有基线。

**[Efficient Reasoning with Balanced Thinking](efficient_reasoning_with_balanced_thinking.md)**

:   提出 ReBalance，一个无需训练的框架，通过基于置信度的动态隐状态导向（steering vector），同时缓解大推理模型（LRM）的过度思考和欠思考问题，实现推理效率与准确率的双重提升。

**[Einstein Fields: A Neural Perspective To Computational General Relativity](einstein_fields_a_neural_perspective_to_computational_general_relativity.md)**

:   提出EinFields，首个将神经隐式表示应用于四维广义相对论模拟压缩的框架，通过将度量张量场编码为紧凑神经网络权重，实现4000倍存储压缩、5-7位数值精度，且通过自动微分获得的张量导数比有限差分精度高5个数量级。

**[Embedding-Based Context-Aware Reranker](embedding-based_context-aware_reranker.md)**

:   提出 EBCAR，一个基于嵌入空间的轻量级重排序框架，通过文档 ID 嵌入和段落位置编码引入结构信息，结合共享全注意力 + 专用掩码注意力的混合机制实现跨段落推理，在 ConTEB 基准上以 126M 参数达到最优平均 nDCG@10，推理速度比 LLM 重排器快 150 倍以上。

**[Embedding Compression via Spherical Coordinates](embedding_compression_via_spherical_coordinates.md)**

:   提出一种基于球坐标变换的嵌入向量压缩方法，利用高维单位向量的球坐标角度集中在 $\pi/2$ 附近的数学性质，使 IEEE 754 浮点数的指数位和高阶尾数位熵大幅降低，实现 1.5× 压缩率，比最优无损方法提升 25%，重建误差低于 float32 机器精度。

**[Energy-Regularized Sequential Model Editing on Hyperspheres](energy-regularized_sequential_model_editing_on_hyperspheres.md)**

:   从超球面均匀性（Hyperspherical Energy）视角理解序列模型编辑中的性能退化，提出 SPHERE 方法：通过将编辑扰动投影到预训练权重主超球方向的正交补空间，实现稳定的大规模序列编辑，在 LLaMA3-8B 上平均超越最强基线 16.41%。

**[ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping](es-dllm_efficient_inference_for_diffusion_large_language_models_by_early-skippin.md)**

:   针对扩散大语言模型（dLLM）推理中大量 token 计算冗余的问题，提出无需训练的 Early-Skipping 加速框架 ES-dLLM，通过估计 token 重要性并在早期层跳过低重要性位置，在 LLaDA-8B 和 Dream-7B 上实现 5.6×–16.8× 加速且不损失生成质量。

**[Evolution and compression in LLMs: On the emergence of human-aligned categorization](evolution_and_compression_in_llms_on_the_emergence_of_human-aligned_categorizati.md)**

:   通过 Information Bottleneck (IB) 框架和迭代上下文语言学习 (IICLL) 范式，证明 LLM 能够在未经 IB 目标训练的情况下，自发涌现出与人类语义分类系统高度对齐的、近最优压缩效率的类别结构。

**[ExGRPO: Learning to Reason from Experience](exgrpo_learning_to_reason_from_experience.md)**

:   首次系统研究什么样的推理经验对RLVR最有价值，发现中等难度问题+低熵轨迹最有效，据此提出ExGRPO框架进行经验管理和混合策略优化，在数学推理上平均+3.5分，通用推理+7.6分。

**[Fine-tuning Quantized Neural Networks with Zeroth-order Optimization](fine-tuning_quantized_neural_networks_with_zeroth-order_optimization.md)**

:   提出QZO方法，通过对量化缩放因子（而非离散权重）做零阶扰动来估计梯度，配合方向导数裁剪稳定训练，实现4-bit/2-bit LLM的极致内存高效微调，总内存降低18倍以上。

**[Fine-tuning with RAG for Improving LLM Learning of New Skills](fine-tuning_with_rag_for_improving_llm_learning_of_new_skills.md)**

:   提出将 RAG 从推理时的永久依赖转化为训练时的教师信号：从 agent 失败中提取 hint、用 hint 增强的教师生成更优轨迹、然后移除 hint 蒸馏到学生模型，使学生内化检索增益而无需运行时 RAG，在 ALFWorld 达到 91% 成功率（基线 79%），WebShop 分数达 72（基线 61）。

**[Flow of Spans: Generalizing Language Models to Dynamic Span-Vocabulary via GFlowNets](flow_of_spans_generalizing_language_models_to_dynamic_span-vocabulary_via_gflown.md)**

:   提出 FoSS，首次将 GFlowNets 引入 span 级别语言模型，通过构建 DAG 结构的状态空间代替传统 token-by-token 的树形结构，实现更灵活多样的文本生成，MAUVE 分数最高提升 12.5%。

**[FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning](flyprompt_brain-inspired_random-expanded_routing.md)**

:   受果蝇蘑菇体稀疏扩展和模块化集成的神经生物学启发，提出 FlyPrompt 框架用于通用持续学习（GCL），通过随机扩展解析路由器（REAR）实现非迭代的专家选择，结合多时间尺度 EMA 输出头的时序集成（TE²）提升专家能力，在 CIFAR-100/ImageNet-R/CUB-200 上分别取得最高 11.23%/12.43%/7.62% 的增益。

**[FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning](flyprompt_brain-inspired_random-expanded_routing_with_temporal-ensemble_experts_.md)**

:   受果蝇蘑菇体神经系统启发，提出 FlyPrompt 框架将通用持续学习（GCL）分解为专家路由和专家能力提升两个子问题，通过随机扩展解析路由器（REAR）和时序集成专家（TE2）分别解决，在 CIFAR-100/ImageNet-R/CUB-200 上分别提升 11.23%/12.43%/7.62%。

**[FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](freqkv_key-value_compression_in_frequency_domain_for_context_window_extension.md)**

:   提出 FreqKV，一种无参数、架构无关的 KV 缓存压缩方法，通过在频域中迭代压缩 KV 状态（保留低频丢弃高频），仅需 8K 长度的少量微调即可将 LLaMA-2-7B 的上下文窗口扩展至 256K，同时保持稳定的困惑度。

**[FutureMind: Equipping Small Language Models with Strategic Thinking-Pattern Priors via Adaptive Knowledge Distillation](futuremind_equipping_small_language_models_with_strategic_thinking-pattern_prior.md)**

:   提出FutureMind无训练框架，将LLM的结构化推理和检索策略蒸馏为可复用的思维模式先验，通过四阶段pipeline（问题分析→逻辑推理→策略规划→检索指导）和三种检索范式，使SLM在多跳QA上达到SOTA。

**[GASP: Guided Asymmetric Self-Play For Coding LLMs](gasp_guided_asymmetric_self-play_for_coding_llms.md)**

:   提出GASP框架，在非对称自博弈中引入"goalpost"（硬目标题）引导教师生成有针对性的训练问题，通过lemma（简化变体）→lift（加难变体）的课程结构逐步逼近困难目标，在LiveCodeBench上超越无引导自博弈2.5%且解决了所有baseline无法解决的难题。

**[Grounding and Enhancing Informativeness and Utility in Dataset Distillation](grounding_and_enhancing_informativeness_and_utility_in_dataset_distillation.md)**

:   提出InfoUtil框架，用博弈论Shapley Value最大化样本信息量（找到最重要的patch），用梯度范数最大化样本效用（选择对训练最有价值的样本），在ImageNet-1K上比前SOTA提升6.1%。

**[GuidedSampling: Steering LLMs Towards Diverse Candidate Solutions at Inference-Time](guidedsampling_steering_llms_towards_diverse_candidate_solutions_at_inference-ti.md)**

:   提出 GuidedSampling 推理算法，将重复采样（RS）的隐式探索和生成过程显式解耦为两阶段：先迭代生成多样化的解题概念/定理，再基于各概念分别生成候选解。在 pass@50 上平均提升约 21.6%，微调后 pass@5 提升约 9.7%。

**[HeurekaBench: A Benchmarking Framework for AI Co-scientist](heurekabench_a_benchmarking_framework_for_ai_co-scientist.md)**

:   提出 HeurekaBench，一个基于真实科学工作流构建评测基准的框架，通过多LLM流水线从论文中提取可验证的科学洞见并生成开放式研究问题，用于评估AI co-scientist在数据驱动科学发现中的端到端能力。

**[HiFo-Prompt: Prompting with Hindsight and Foresight for LLM-based Automatic Heuristic Design](hifo-prompt_prompting_with_hindsight_and_foresight_for_llm-based_automatic_heuri.md)**

:   提出 HiFo-Prompt 框架，通过 Hindsight（回顾式知识池）和 Foresight（前瞻式进化导航器）两个协同模块提升 LLM 驱动的自动启发式设计（AHD），在 TSP 和 FSSP 等任务上显著超越现有方法。

**[Highly Efficient and Effective LLMs with Multi-Boolean Architectures](highly_efficient_and_effective_llms_with_multi-boolean_architectures.md)**

:   提出一种用多核布尔参数（multi-kernel Boolean parameters）表示 LLM 权重的新框架，首次实现在布尔域中直接微调大语言模型，无需全精度潜在权重，在表征能力和计算效率上同时超越现有超低比特量化和二值化方法。

**[Human-LLM Collaborative Feature Engineering for Tabular Data](human-llm_collaborative_feature_engineering_for_tabular_data.md)**

:   提出人-LLM协作特征工程框架——解耦LLM的特征操作提议和选择过程：LLM仅负责生成候选操作→贝叶斯优化(建模效用+不确定性)引导选择→当效用估计不可靠时(早期轮次)→选择性征询人类偏好反馈(成对比较)→合成研究和真实用户研究均证明提升性能+降低认知负担。

**[IDER: IDempotent Experience Replay for Reliable Continual Learning](ider_idempotent_experience_replay_for_reliable_continual_learning.md)**

:   将幂等性（idempotence）引入持续学习，通过标准幂等模块和幂等蒸馏模块两个组件强制模型在学习新任务时保持输出自一致性，在提升预测可靠性（降低校准误差）的同时显著减少灾难性遗忘。

**[In-Context Learning for Pure Exploration](in-context_learning_for_pure_exploration.md)**

:   提出 ICPE（In-Context Pure Exploration），一种结合监督学习和强化学习的上下文学习框架，使用 Transformer 从经验中直接学习探索策略，在主动序列假设检验/纯探索问题中实现接近最优的实例自适应算法性能，无需显式建模信息结构。

**[Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning](incentivizing_agentic_reasoning_in_llm_judges_via_tool-integrated_reinforcement_.md)**

:   提出 TIR-Judge，一个端到端的 RL 框架，训练 LLM 评判模型在评估过程中交替使用推理和代码执行工具，在7个公开基准上以 8B 参数超越 32B 推理奖励模型，且无需蒸馏的 TIR-Judge-Zero 可自举提升。

**[Information Shapes Koopman Representation](information_shapes_koopman_representation.md)**

**[InftyThink: Breaking the Length Limits of Long-Context Reasoning in Large Language Models](inftythink_breaking_the_length_limits_of_long-context_reasoning_in_large_languag.md)**

:   提出 InftyThink，一种将整体式长推理转化为迭代式短推理+中间摘要的新范式，在不修改模型架构的前提下实现理论上无界的推理深度、显著降低计算成本，Qwen2.5-Math-7B 在 AIME24 上提升11%。

**[Internal Planning in Language Models: Characterizing Horizon and Branch Awareness](internal_planning_in_language_models_characterizing_horizon_and_branch_awareness.md)**

:   提出基于VQ-VAE的信息论框架来分析语言模型内部的规划行为，发现规划视野是任务依赖的、模型隐式保留未选择的正确路径信息、下一token决策主要依赖最近的计算。

**[Is Finer Better? The Limits of Microscaling Formats in Large Language Models](is_finer_better_the_limits_of_microscaling_formats_in_large_language_models.md)**

:   发现并解释了微缩放（microscaling）量化中"更细粒度反而更差"的反直觉异常——当block size减小到阈值以下时，FP8 UE4M3 scale的有限动态范围导致窄分布张量的量化误差反而增大，并提出 FP8 UE5M3 scale格式作为硬件友好的解决方案。

**[Is the Reversal Curse a Binding Problem? Uncovering Limitations of Transformers from a Basic Generalization Failure](is_the_reversal_curse_a_binding_problem_uncovering_limitations_of_transformers_f.md)**

:   提出反转诅咒（Reversal Curse）是认知科学中"绑定问题"在Transformer中的表现——源于概念表示的不一致性和纠缠性，并首次设计出基于JEPA和记忆层的架构真正突破反转诅咒（非绕过）。

**[IterResearch: Rethinking Long-Horizon Agents with Interaction Scaling](iterresearch_rethinking_long-horizon_agents_with_interaction_scaling.md)**

:   提出 IterResearch，一种基于MDP的迭代深度研究范式，通过周期性工作区重构替代单上下文线性累积，使Agent在40K上下文长度下扩展到2048次交互（性能从3.5%提升至42.5%），在6个benchmark上平均超出开源Agent 14.5个百分点。

**[KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE Large Language Models](kbvq-moe_klt-guided_svd_with_bias-corrected_vector_quantization_for_moe_large_la.md)**

:   提出 KBVQ-MoE，首个专为MoE架构设计的向量量化框架，通过KLT引导的SVD消除专家间冗余共享（IDRE），以及偏差校正的输出稳定化（BCOS），在2-bit量化下比现有方法提升10%+准确率。

**[Knowledge Fusion of Large Language Models Via Modular Skillpacks](knowledge_fusion_of_large_language_models_via_modular_skillpacks.md)**

:   提出GraftLLM——将异构源模型的能力提取为紧凑可迁移的"SkillPack"（模块化技能包），通过模块感知自适应压缩策略存储参数增量，支持知识迁移、异构模型融合和无遗忘持续学习，在多个场景下显著优于现有PEFT和参数融合方法。

**[KV Cache Transform Coding for Compact Storage in LLM Inference](kv_cache_transform_coding_for_compact_storage_in_llm_inference.md)**

:   提出 KVTC，一种借鉴经典媒体压缩技术（PCA 特征去相关 + 自适应量化 + 熵编码）的 KV 缓存压缩方法，在 Llama 3、Mistral NeMo、R1-Qwen 2.5 等模型上实现最高 20× 压缩（特定场景下 40×+），优于 token 驱逐、量化、SVD 等基线方法。

**[Landscape of Thoughts: Visualizing the Reasoning Process of Large Language Models](landscape_of_thoughts_visualizing_the_reasoning_process_of_large_language_models.md)**

:   提出 Landscape of Thoughts (LoT)，首个将LLM推理轨迹可视化为二维地形图的工具，通过困惑度特征和t-SNE投影揭示推理行为模式，并可适配为轻量验证器提升推理准确率和测试时扩展效果。

**[LD-MoLE: Learnable Dynamic Routing for Mixture of LoRA Experts](ld-mole_learnable_dynamic_routing_for_mixture_of_lora_experts.md)**

:   提出 LD-MoLE，用 Sparsegen 闭合形式投影替代传统 TopK 路由，实现可微分、动态、token自适应的 LoRA 专家分配，配合轻量 MLP 预测稀疏因子和解析稀疏损失，在多个基准上超越固定路由和 ReLU 路由基线。

**[LightMem: Lightweight and Efficient Memory-Augmented Generation](lightmem_lightweight_and_efficient_memory-augmented_generation.md)**

:   提出 LightMem，一个受人类 Atkinson-Shiffrin 记忆模型启发的三阶段轻量记忆系统，通过认知感觉记忆预压缩、主题感知短期记忆整合、睡眠时离线更新三个模块，在 LongMemEval 上准确率提升最高7.7%，同时 token 消耗降低高达38倍。

**[LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference](lightretriever_a_llm-based_text_retrieval_architecture_with_extremely_faster_que.md)**

:   提出 LightRetriever，一种极端不对称的LLM检索架构：文档端保留完整LLM编码器，查询端完全去除深度建模——稠密检索仅需嵌入查表+平均，稀疏检索仅需token计数——实现查询编码1000倍加速、端到端10倍吞吐提升，同时保持95%的检索性能。

**[LLM DNA: Tracing Model Evolution via Functional Representations](llm_dna_tracing_model_evolution_via_functional_representations.md)**

:   从生物学 DNA 类比出发，将 LLM DNA 数学定义为模型功能行为的低维双 Lipschitz 表示，证明其满足遗传和基因决定性属性，并设计了无需训练的 RepTrace 管道在 305 个 LLM 上提取 DNA、构建进化树。

**[LoFT: Low-Rank Adaptation That Behaves Like Full Fine-Tuning](loft_low-rank_adaptation_that_behaves_like_full_fine-tuning.md)**

:   提出 LoFT，一种通过对齐优化器内部动态（动量和二阶矩）与全参微调行为一致的低秩适配方法，由六个构建模块组成，在全秩极限下可精确恢复 AdamW，在多项基准上显著缩小 LoRA 与全参微调的性能差距。

**[LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](lookaheadkv_fast_and_accurate_kv_cache_eviction_by_glimpsing_into_the_future_wit.md)**

:   提出 LookaheadKV，通过可学习的前瞻token和选择性激活的LoRA模块预测真实响应的注意力重要性分数，实现无需生成草稿的快速精确KV缓存淘汰，在多个长上下文基准上超越现有方法，驱逐开销降低最高14.5倍。

**[Memba: Membrane-driven Parameter-Efficient Fine-Tuning for Mamba](memba_membrane-driven_parameter-efficient_fine-tuning_for_mamba.md)**

:   提出 Memba，一种受生物神经元膜电位启发的参数高效微调方法，通过在 Mamba 门控分支引入泄漏积分膜（LIM）神经元实现时序自适应，结合 LoRA 放置优化和跨层膜传递，以极少参数在语言和视觉任务上超越现有 Mamba PEFT 方法。

**[MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes](mobilellm-r1_exploring_the_limits_of_sub-billion_language_model_reasoners_with_o.md)**

:   通过精心的数据筛选和自适应混合策略，仅用4.2T token（Qwen3的11.7%）预训练出亿级参数的推理模型 MobileLLM-R1-950M，在AIME等推理基准上匹配或超越 Qwen3-0.6B，同时完全开源数据源和训练配方。

**[Modality-free Graph In-context Alignment](modality-free_graph_in-context_alignment.md)**

:   提出 MF-GIA，首个同时满足无后训练、跨域对齐和模态无关三个条件的图上下文学习框架，通过梯度指纹捕获域特征、FiLM条件化变换对齐特征和标签，在多个图域的few-shot任务上实现SOTA性能。

**[MoNE: Replacing Redundant Experts with Lightweight Novices for Structured Pruning of MoE](mone_replacing_redundant_experts_with_lightweight_novices_for_structured_pruning.md)**

:   提出 MoNE（Mixture-of-Novices-and-Experts），通过联合评估专家的访问频率和输出方差来识别冗余专家，并用其输出均值（"新手"常量向量）替换之，在5种MoE模型上实现比现有剪枝方法更有效且更鲁棒的压缩，25%剪枝率下平均准确率下降仅0.14。

**[Multi-View Encoders for Performance Prediction in LLM-Based Agentic Workflows](multi-view_encoders_for_performance_prediction_in_llm-based_agentic_workflows.md)**

:   提出 Agentic Predictor，一种多视图工作流编码框架，通过联合建模图结构、代码语义和提示信息来预测 LLM Agent 工作流的性能，显著减少昂贵的试错评估。

**[Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity](null-space_filtering_for_data-free_continual_model_merging_preserving_stability_.md)**

:   提出 NUFILT 框架，通过零空间滤波和投影感知 LoRA 适配，在不访问任何任务数据的条件下实现持续模型合并，同时保持稳定性和可塑性。

**[Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search](obscure_but_effective_classical_chinese_jailbreak_prompt_optimization_via_bio-in.md)**

:   提出 CC-BOS 框架，利用文言文的语义压缩和模糊性特征，结合果蝇优化算法在八维策略空间中搜索最优越狱提示，在六个主流 LLM 上实现近 100% 的攻击成功率。

**[Parallel Token Prediction for Language Models](parallel_token_prediction_for_language_models.md)**

:   提出 Parallel Token Prediction (PTP)，通过将采样随机性从后处理移至模型输入（辅助变量），使未来 token 成为确定性函数，从而在单次前向传播中联合预测多个 token。

**[ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](paroquant_pairwise_rotation_quantization_for_efficient_reasoning_llm_inference.md)**

:   提出 ParoQuant，通过硬件高效且可优化的独立 Givens 旋转与通道缩放相结合来消除权重异常值，在推理 LLM 上实现高精度低开销的 4-bit 权重量化。

**[PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery](paser_post-training_data_selection_for_efficient_pruned_large_language_model_rec.md)**

:   提出PASER，一种针对剪枝LLM恢复的后训练数据选择方法，通过流形学习+谱聚类识别能力相关指令集，按能力退化程度自适应分配数据预算，仅用4%-20%原始数据即可显著超越全量数据恢复效果。

**[Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation](pedagogically-inspired_data_synthesis_for_language_model_knowledge_distillation.md)**

:   提出 IOA（Identifier-Organizer-Adapter）框架，借鉴 Bloom 掌握学习原则和 Vygotsky 最近发展区理论，通过诊断知识缺陷、设计渐进课程、适配认知水平三个阶段，实现教育学驱动的 LLM 知识蒸馏。

**[Propaganda AI: An Analysis of Semantic Divergence in Large Language Models](propaganda_ai_an_analysis_of_semantic_divergence_in_large_language_models.md)**

:   提出 RAVEN 审计框架，通过结合模型内语义熵和跨模型分歧来检测 LLM 中的概念条件语义分歧——一种类似宣传的行为模式，即高层概念线索（意识形态、公众人物）触发异常一致的立场响应。

**[PT2-LLM: Post-Training Ternarization for Large Language Models](pt2-llm_post-training_ternarization_for_large_language_models.md)**

:   提出 PT2-LLM，首个针对 LLM 的后训练三值化框架，通过非对称三值量化器（含迭代三值拟合和激活感知网格对齐）与结构相似性重排序策略，在 1.58-bit 下实现优于 2-bit PTQ 方法的性能。

**[PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models](ptq4arvg_post-training_quantization_for_autoregressive_visual_generation_models.md)**

:   提出 PTQ4ARVG，首个针对自回归视觉生成（ARVG）模型的系统化 PTQ 框架，通过增益投影缩放（GPS）、静态 Token 级量化（STWQ）和分布引导校准（DGC）解决 ARVG 特有的三大量化挑战。

**[QKV Projections Require a Fraction of Their Memory](qkv_projections_require_a_fraction_of_their_memory.md)**

:   提出 PAMM（Point-Approximate Matrix Multiplication），一种激活压缩技术，通过随机选取少量代表性 token 来近似 QKV 投影层激活，实现高达 512× 压缩率且不影响模型性能。

**[RAEE: A Robust Retrieval-Augmented Early Exit Framework for Efficient Inference](raee_a_robust_retrieval-augmented_early_exit_framework_for_efficient_inference.md)**

:   提出 RAEE，一种无需训练分类器的检索增强早退框架，通过检索语义相似样本的退出信息来动态确定最优退出层，不仅加速推理还能纠正模型错误预测，实现加速与性能提升的双赢。

**[Rectified Decoupled Dataset Distillation: A Closer Look for Fair and Comprehensive Evaluation](rectified_decoupled_dataset_distillation_a_closer_look_for_fair_and_comprehensiv.md)**

:   提出 RD3（Rectified Decoupled Dataset Distillation），系统揭示现有解耦数据集蒸馏方法的性能差异主要源于不一致的后评估设置而非蒸馏质量差异，建立了统一公平的评估框架，将报告的 27.3% 性能差距校正为 6.7%。

**[Reference-Guided Machine Unlearning](reference-guided_machine_unlearning.md)**

:   提出 ReGUn（Reference-Guided Unlearning），利用独立留出数据集作为"未见行为"的参考标准，通过类别条件蒸馏将遗忘数据上的模型行为对齐到真正未见数据的行为，实现更优的遗忘-效用权衡。

**[Rethinking Continual Learning with Progressive Neural Collapse](rethinking_continual_learning_with_progressive_neural_collapse.md)**

:   提出 ProNC 框架，通过渐进式扩展等角紧框架（ETF）目标替代固定预定义 ETF，在持续学习中实现最大类间分离与最小遗忘的平衡。

**[Revisiting Weight Regularization for Low-Rank Continual Learning](revisiting_weight_regularization_for_low-rank_continual_learning.md)**

:   在低秩持续学习中重新引入弹性权重巩固（EWC），通过在全维空间估计 Fisher 信息矩阵来正则化共享 LoRA 模块，实现恒定存储开销下的有效遗忘缓解。

**[S2R-HDR: A Large-Scale Rendered Dataset for HDR Fusion](s2r-hdr_a_large-scale_rendered_dataset_for_hdr_fusion.md)**

:   提出 S2R-HDR，首个大规模高质量合成 HDR 融合数据集（24,000 样本），并设计 S2R-Adapter 域适应方法弥合合成-真实域差距，在真实数据集上达到 SOTA HDR 融合性能。

**[SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs](sasft_sparse_autoencoder-guided_supervised_finetuning_to_mitigate_unexpected_cod.md)**

:   利用稀疏自编码器（SAE）发现 LLM 中意外语言切换与目标语言特征异常高预激活值相关，提出 SASFT 方法在 SFT 训练中约束语言特征预激活值，将意外代码切换降低 50% 以上。

**[Scalable Multi-Task Low-Rank Model Adaptation](scalable_multi-task_low-rank_model_adaptation.md)**

:   系统分析多任务 LoRA 在任务数量增大时崩溃的根因（均匀正则化破坏共享知识 + 组件级 LoRA 放大梯度冲突），提出 mtLoRA：谱感知正则化 + 块级适配 + 细粒度路由，在 15-25 个任务上平均超越 SOTA 2.3%，同时减少 47% 参数和 24% 训练时间。

**[Scaling Reasoning Hop Exposes Weaknesses: Demystifying and Improving Hop Generalization in Large Language Models](scaling_reasoning_hop_exposes_weaknesses_demystifying_and_improving_hop_generali.md)**

:   系统性揭示了 LLM 在推理跳步泛化（reasoning hop generalization）中失败的内部机制——正确与错误推理轨迹间的注意力头竞争，并提出 TCR（Test-time Correction of Reasoning），通过动态识别和停用错误处理头（ep heads）在测试时纠正推理错误，平均提升 5-7% 准确率。

**[SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing](seed-set_scalable_evolving_experimental_design_for_system-level_ethical_testing.md)**

:   提出 SEED-SET 框架，将自主系统的伦理评估建模为层次化贝叶斯实验设计问题，同时整合客观指标和主观价值判断，在有限预算下高效生成高伦理对齐度的测试用例。

**[SeeDNorm: Self-Rescaled Dynamic Normalization](seednorm_self-rescaled_dynamic_normalization.md)**

:   提出 SeeDNorm，一种自适应动态归一化层，通过将输入自身作为条件来动态调整缩放系数，从而在前向传播中保留输入范数信息，同时在反向传播中保持类似 RMSNorm 的自适应梯度调整能力，以极少额外参数在语言建模和视觉任务上全面超越 RMSNorm、LayerNorm 和 DyT。

**[SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models](sere_similarity-based_expert_re-routing_for_efficient_batch_decoding_in_moe_mode.md)**

:   提出 SERE 方法，通过预计算专家相似度矩阵，在批量解码时将次要专家动态重路由到最相似的主要专家，实现最高 2.0 倍加速且质量损失极小，并提供即插即用的 vLLM CUDA 内核。

**[SFT Doesn't Always Hurt General Capabilities: Revisiting Domain-Specific Fine-Tuning in LLMs](sft_doesnt_always_hurt_general_capabilities_revisiting_domain-specific_fine-tuni.md)**

:   本文系统性地重新审视了领域特定SFT对LLM通用能力的影响，发现**使用较小学习率即可大幅缓解通用能力退化**，并提出Token-Adaptive Loss Reweighting (TALR)方法通过自适应下调低概率token的损失权重进一步优化领域适配与通用能力之间的权衡。

**[Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning](slow-fast_policy_optimization_reposition-before-update_for_llm_reasoning.md)**

:   提出 SFPO（Slow-Fast Policy Optimization），通过将每个训练步分解为"快速轨迹—重定位—慢速校正"三阶段结构，在不修改目标函数和 rollout 过程的前提下即插即用地增强 GRPO 的稳定性和样本效率，在数学推理基准上平均提升最高 2.80 分，rollout 减少最多 4.93 倍。

**[SPARTA: Scalable and Principled Benchmark of Tree-Structured Multi-hop QA over Text and Tables](sparta_scalable_and_principled_benchmark_of_tree-structured_multi-hop_qa_over_te.md)**

:   提出 SPARTA，一个端到端自动构建大规模表格-文本多跳问答基准的框架，通过参考事实数据库、来源引导的修复和现实结构约束生成高质量嵌套 SQL 查询，SOTA 模型在 SPARTA 上 F1 下降超过 30 分。

**[Specialization after Generalization: Towards Understanding Test-Time Training in Foundation Models](specialization_after_generalization_towards_understanding_test-time_training_in_.md)**

:   从线性表示假说（LRH）出发，提出"泛化后特化"机制来解释 TTT（Test-Time Training）为何有效：基础模型全局欠参数化时，TTT 通过在测试点邻域内特化来释放模型容量，理论证明 TTT 在概念空间维度远大于特征空间时仍能泛化。

**[STAR: Similarity-guided Teacher-Assisted Refinement for Super-Tiny Function Calling Models](star_similarity-guided_teacher-assisted_refinement_for_super-tiny_function_calli.md)**

:   提出 STAR 框架，通过约束知识蒸馏（CKD）和相似度引导的强化学习（Sim-RL）协同工作，将大模型的 function calling 能力有效迁移到 0.6B 级别的超小模型，在 BFCL 和 ACEBench 上大幅超越基线。

**[Steering MoE LLMs via Expert (De)Activation](steering_moe_llms_via_expert_deactivation.md)**

:   提出 SteerMoE，通过对比配对输入检测行为关联专家，在推理时通过激活/去激活特定专家来引导 MoE LLM 的行为（安全性提升 +20%，忠实性提升 +27%），同时揭示 MoE 模型的安全对齐脆弱性（安全下降 -100%）。

**[Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems](stop_wasting_your_tokens_towards_efficient_runtime_multi-agent_systems.md)**

:   提出 SupervisorAgent，一个轻量级的实时自适应监督框架，通过无 LLM 的自适应过滤器在关键交互节点主动干预（纠错、指导、观察净化），在 GAIA 基准上将 Smolagent 的 token 消耗降低 29.68% 而不损失成功率。

**[Stress-Testing Alignment Audits With Prompt-Level Strategic Deception](stress-testing_alignment_audits_with_prompt-level_strategic_deception.md)**

:   构建自动 prompt 级红队流水线，对"保守秘密"的模型有机体进行压力测试，发现能诱导黑盒和白盒对齐审计方法产生高置信错误猜测的欺骗策略，首次记录了基于激活的策略性欺骗现象。

**[Summaries as Centroids for Interpretable and Scalable Text Clustering](summaries_as_centroids_for_interpretable_and_scalable_text_clustering.md)**

:   提出 k-NLPmeans 和 k-LLMmeans，通过在 k-means 迭代中周期性地用文本摘要替换数值质心（summary-as-centroid），在保持 k-means 标准目标的同时实现可解释的聚类原型，且 LLM 调用量与数据集大小无关。

**[SwiReasoning: Switch-Thinking in Latent and Explicit for Pareto-Superior Reasoning](swireasoning_switch-thinking_in_latent_and_explicit_for_pareto-superior_reasonin.md)**

:   提出 SwiReasoning，一种免训练的 LLM 推理框架，通过基于熵趋势的块级置信度估计，动态切换显式（chain-of-thought）和隐式（latent space）推理模式，在 Pareto 意义上同时改善准确率（+1.8%~3.1%）和 Token 效率（+57%~79%）。

**[Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation](taming_momentum_rethinking_optimizer_states_through_low-rank_approximation.md)**

:   揭示动量 EMA 更新等价于在线线性回归的梯度下降，基于此提出 LoRA-Pre，通过低秩分解压缩优化器动量，实现显存高效的 LLM 预训练和微调，在所有模型尺度上达到最优性能且仅需基线方法 1/8 的秩。

**[Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning](temperature_as_a_meta-policy_adaptive_temperature_in_llm_reinforcement_learning.md)**

:   提出 TAMPO（Temperature Adaptive Meta Policy Optimization），将采样温度重新定义为可学习的元策略，通过双层循环在内环做 LLM 策略优化、外环根据轨迹优势信号自适应更新温度分布，无需额外 rollout，在数学推理基准上一致超越固定温度基线。

**[Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability](temporal_sparse_autoencoders_leveraging_the_sequential_nature_of_language_for_in.md)**

:   提出 Temporal SAEs (T-SAEs)，通过引入时间对比损失鼓励高层特征在相邻 token 间保持一致激活，在无显式语义信号的自监督训练下实现语义与句法特征的解耦，恢复更平滑、连贯的语义概念且不牺牲重构质量。

**[Textual Equilibrium Propagation for Deep Compound AI Systems](textual_equilibrium_propagation_for_deep_compound_ai_systems.md)**

:   提出文本平衡传播（TEP），一种基于局部学习原理的复合AI系统优化方法，通过自由阶段和微扰阶段的两阶段设计，避免全局文本反向传播中的梯度爆炸/消失问题，在深层工作流上显著优于 TextGrad。

**[The Geometry of LLM Quantization: GPTQ as Babai's Nearest Plane Algorithm](the_geometry_of_llm_quantization_gptq_as_babais_nearest_plane_algorithm.md)**

:   首次证明 GPTQ（从后向前执行时）在数学上等价于经典格理论中的 Babai 最近平面算法，由此获得几何解释和层级误差上界，并基于此设计了无裁剪的改进量化方法。

**[The Lattice Geometry of Neural Network Quantization -- A Short Equivalence Proof of GPTQ and Babai's Algorithm](the_lattice_geometry_of_neural_network_quantization_--_a_short_equivalence_proof.md)**

:   独立于 Chen et al. (2026)，以更简洁优雅的方式证明 GPTQ 等价于 Babai 最近平面算法，并阐明格基约减可能改进神经网络量化的前景。

**[The Unseen Frontier: Pushing the Limits of LLM Sparsity with Surrogate-Free ADMM](the_unseen_frontier_pushing_the_limits_of_llm_sparsity_with_surrogate-free_admm.md)**

:   提出 Elsa 方法，通过无代理目标的 ADMM 约束优化直接求解稀疏性约束问题，突破 LLM 剪枝 50-60% 的"稀疏墙"瓶颈，在 90% 稀疏度下仍保持高模型保真度。

**[TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA](titok_transfer_token-level_knowledge_via_contrastive_excess_to_transplant_lora.md)**

:   提出 TiTok 框架，通过 token 级对比超额分数（contrastive excess）实现 LoRA 适配器跨模型高效迁移，无需额外判别器模型，在推理和个性化任务上一致超越 TransLoRA 和知识蒸馏基线。

**[Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding](token-guard_towards_token-level_hallucination_control_via_self-checking_decoding.md)**

:   提出 Token-Guard，一种基于自检验解码的 token 级幻觉控制方法，通过隐空间中的 token 级/段级评分和迭代修正机制，在解码过程中检测并抑制幻觉生成，F1 平均提升 16.3%。

**[Token Distillation: Attention-Aware Input Embeddings for New Tokens](token_distillation_attention-aware_input_embeddings_for_new_tokens.md)**

:   提出 Token Distillation 方法，通过蒸馏 Transformer 各层编码的多子词交互信息到单一 token 嵌入中，实现高质量的新 token 嵌入初始化，无需预训练超网络且优于现有方法。

**[Tokenizing Single-Channel EEG with Time-Frequency Motif Learning](tokenizing_single-channel_eeg_with_time-frequency_motif_learning.md)**

:   提出 TFM-Tokenizer，首个从单通道 EEG 学习时频 motif 词表并编码为离散 token 的框架，在事件分类、癫痫检测等任务上一致提升性能，且可作为即插即用组件增强现有 EEG 基础模型。

**[TokMem: One-Token Procedural Memory for Large Language Models](tokmem_one-token_procedural_memory_for_large_language_models.md)**

:   提出 TokMem，将可复用的任务程序编译为单个可训练记忆 token，既作为程序索引又作为生成控制信号，无需长 prompt 即可高效调用 1000+ 任务程序，且支持无遗忘的持续扩展。

**[Topology and Geometry of the Learning Space of ReLU Networks: Connectivity and Size](topology_and_geometry_of_the_learning_space_of_relu_networks_connectivity_and_si.md)**

:   从代数几何和代数拓扑的视角，系统研究了基于一般 DAG 架构的前馈 ReLU 网络参数空间的连通性和奇异性，揭示了瓶颈节点和平衡条件在决定参数空间拓扑结构中的关键作用，并建立了奇异性与可微剪枝的理论联系。

**[Towards Efficient Constraint Handling in Neural Solvers for Routing Problems](towards_efficient_constraint_handling_in_neural_solvers_for_routing_problems.md)**

:   提出 Construct-and-Refine (CaR) 框架，通过联合训练构造模块和轻量改进模块实现高效的可行性修复，首次为硬约束路径问题提供通用、高效的神经约束处理方案，在 TSPTW 和 CVRPBLTW 上大幅超越经典和神经 SOTA 求解器。

**[Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer](towards_understanding_subliminal_learning_when_and_how_hidden_biases_transfer.md)**

:   本文通过受控实验和机制分析揭示了潜意识学习（subliminal learning）的本质——教师模型的隐藏偏好通过少量"分歧token"（divergence tokens）传递给学生模型，且早期层是关键，同时发现该现象非常脆弱，简单的同义改写即可抑制。

**[TurboBoA: Faster and Exact Attention-aware Quantization without Backpropagation](turboboa_faster_and_exact_attention-aware_quantization_without_backpropagation.md)**

:   TurboBoA 提出了一种无需反向传播的 LLM 后训练量化方法，通过多 out-channel 联合量化、前层误差补偿和自适应网格选择三大创新，在保留 BoA 精度优势的同时实现了 3 倍以上加速。

**[Understanding Dataset Distillation via Spectral Filtering](understanding_dataset_distillation_via_spectral_filtering.md)**

:   本文提出 UniDD 谱滤波框架，将多种数据集蒸馏方法统一为在特征-特征相关矩阵（FFC）上应用不同滤波函数来匹配特征-标签相关矩阵（FLC）的频率信息，并基于此洞见提出了课程频率匹配（CFM）方法。

**[Unveiling Super Experts in Mixture-of-Experts Large Language Models](unveiling_super_experts_in_mixture-of-experts_large_language_models.md)**

:   本文首次发现并系统研究了 MoE LLM 中的"超级专家"（Super Experts）——数量极少但对模型推理至关重要的专家子集，它们通过 down_proj 中的极端激活异常值驱动 massive activations 和 attention sinks 机制。

**[Why Attention Patterns Exist: A Unifying Temporal Perspective Analysis](why_attention_patterns_exist_a_unifying_temporal_perspective_analysis.md)**

:   本文提出 TAPPA 框架，从时间连续性视角统一解释了 LLM 中多种注意力模式（attention sink、对角线、周期性等）的形成机制，并通过 query 自相似性（q-similarity）指标指导 KV cache 压缩和模型剪枝任务。

**[Your Language Model Secretly Contains Personality Subnetworks](your_language_model_secretly_contains_personality_subnetworks.md)**

:   本文提出通过激活引导的剪枝（activation-guided pruning）从预训练 LLM 中提取人格专用子网络，无需任何训练即可实现高效的人格切换，并引入对比剪枝策略增强对立人格间的参数分离。

**[ZeroTuning: Unlocking the Initial Token's Power to Enhance Large Language Models Without Training](zerotuning_unlocking_the_initial_tokens_power_to_enhance_large_language_models_w.md)**

:   提出 ZeroTuning，仅需对初始 token（如 `<BOS>`）的注意力分数进行头部特异性缩放，即可在无训练情况下提升 LLM 在 15 个数据集上的表现，仅需修改 4 行代码。
