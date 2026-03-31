<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🔬 ICLR2026** · 共 **41** 篇

**[A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA](a_fano-style_accuracy_upper_bound_for_llm_single-pass_reasoning_in_multi-hop_qa.md)**

:   用信息论推导出 LLM 单次推理在多跳 QA 中的 Fano 式准确率上界，揭示当任务信息需求超过模型输出容量时准确率会"悬崖式"骤降的现象，并据此设计多轮推理框架 InfoQA，通过容量感知分解、依赖显式工作流和迭代查询压缩来突破单次推理瓶颈。

**[A Recovery Guarantee for Sparse Neural Networks](a_recovery_guarantee_for_sparse_neural_networks.md)**

:   证明了 ReLU 神经网络的首个稀疏恢复保证：对两层标量输出网络，当训练数据为高斯随机采样时，基于凸重构的迭代硬阈值 (IHT) 算法可精确恢复稀疏网络权重，且内存需求仅与非零权重数线性增长。

**[A State-Transition Framework for Efficient LLM Reasoning](a_state-transition_framework_for_efficient_llm_reasoning.md)**

:   提出将 LLM 推理过程建模为状态转移过程的高效推理框架，用 Linear Attention 将历史推理步骤的信息压缩为状态矩阵，使注意力复杂度从 $O(C^2)$ 降为 $O(C)$、KV cache 从 $O(C)$ 降为 $O(1)$，同时不缩短 CoT 序列，保持推理能力。额外的动量 momentum 策略缓解了噪声推理步导致的 overthinking 问题。

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

**[BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](biasscope_towards_automated_detection_of_bias_in_llm-as-a-judge_evaluation.md)**

:   提出 BiasScope，一个完全由 LLM 驱动的迭代式框架，能自动、大规模地发现 LLM-as-a-Judge 中的潜在未知偏差，并基于此构建了更具挑战性的 JudgeBench-Pro 基准，在其上即使强大的 LLM 评估器错误率也超过 50%。

**[Boomerang Distillation Enables Zero-Shot Model Size Interpolation](boomerang_distillation_enables_zero-shot_model_size_interpolation.md)**

:   发现并系统研究"回旋蒸馏"现象：从大模型（teacher）蒸馏出小模型（student）后，将教师的层块重新插回学生模型，无需任何额外训练即可构建任意中间尺寸的模型，其性能在 student 和 teacher 之间平滑插值，匹配甚至超越同等尺寸的独立蒸馏模型。

**[Boosting Entropy with Bell Box Quantization](boosting_entropy_with_bell_box_quantization.md)**

:   提出 Bell Box Quantization (BBQ)，首个同时满足"信息论最优"(ITO) 和"计算高效"(compute-efficient) 的量化方法，核心洞察是学习的域无关性——量化器输出域不必与输入域相同，由此在输入域做 ITO 量化以最大化熵，在输出域映射到硬件可加速的数据类型，在 1-4 bit QAPT 场景下全面超越 QuEST 和 LSQ。

**[BOTS: A Unified Framework for Bayesian Online Task Selection in LLM Reinforcement Finetuning](bots_a_unified_framework_for_bayesian_online_task_selection_in_llm_reinforcement.md)**

:   提出 BOTS 框架，将 LLM 强化微调中的在线任务选择建模为贝叶斯推断问题，通过融合显式证据（直接评估）和隐式证据（跨任务推断）来自适应估计任务难度，并利用 Thompson 采样平衡探索与利用，显著提升训练效率。

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

**[Flow of Spans: Generalizing Language Models to Dynamic Span-Vocabulary via GFlowNets](flow_of_spans_generalizing_language_models_to_dynamic_span-vocabulary_via_gflown.md)**

:   提出 FoSS，首次将 GFlowNets 引入 span 级别语言模型，通过构建 DAG 结构的状态空间代替传统 token-by-token 的树形结构，实现更灵活多样的文本生成，MAUVE 分数最高提升 12.5%。

**[Flyprompt Brain-Inspired Random-Expanded Routing](flyprompt_brain-inspired_random-expanded_routing.md)**

:   受果蝇蘑菇体稀疏扩展和模块化集成的神经生物学启发，提出 FlyPrompt 框架用于通用持续学习（GCL），通过随机扩展解析路由器（REAR）实现非迭代的专家选择，结合多时间尺度 EMA 输出头的时序集成（TE²）提升专家能力，在 CIFAR-100/ImageNet-R/CUB-200 上分别取得最高 11.23%/12.43%/7.62% 的增益。

**[FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning](flyprompt_brain-inspired_random-expanded_routing_with_temporal-ensemble_experts_.md)**

:   受果蝇蘑菇体神经系统启发，提出 FlyPrompt 框架将通用持续学习（GCL）分解为专家路由和专家能力提升两个子问题，通过随机扩展解析路由器（REAR）和时序集成专家（TE2）分别解决，在 CIFAR-100/ImageNet-R/CUB-200 上分别提升 11.23%/12.43%/7.62%。

**[FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](freqkv_key-value_compression_in_frequency_domain_for_context_window_extension.md)**

:   提出 FreqKV，一种无参数、架构无关的 KV 缓存压缩方法，通过在频域中迭代压缩 KV 状态（保留低频丢弃高频），仅需 8K 长度的少量微调即可将 LLaMA-2-7B 的上下文窗口扩展至 256K，同时保持稳定的困惑度。

**[GuidedSampling: Steering LLMs Towards Diverse Candidate Solutions at Inference-Time](guidedsampling_steering_llms_towards_diverse_candidate_solutions_at_inference-ti.md)**

:   提出 GuidedSampling 推理算法，将重复采样（RS）的隐式探索和生成过程显式解耦为两阶段：先迭代生成多样化的解题概念/定理，再基于各概念分别生成候选解。在 pass@50 上平均提升约 21.6%，微调后 pass@5 提升约 9.7%。

**[Information Shapes Koopman Representation](information_shapes_koopman_representation.md)**

**[PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery](paser_post-training_data_selection_for_efficient_pruned_large_language_model_rec.md)**

:   提出PASER，一种针对剪枝LLM恢复的后训练数据选择方法，通过流形学习+谱聚类识别能力相关指令集，按能力退化程度自适应分配数据预算，仅用4%-20%原始数据即可显著超越全量数据恢复效果。

**[Scalable Multi-Task Low-Rank Model Adaptation](scalable_multi-task_low-rank_model_adaptation.md)**

:   系统分析多任务 LoRA 在任务数量增大时崩溃的根因（均匀正则化破坏共享知识 + 组件级 LoRA 放大梯度冲突），提出 mtLoRA：谱感知正则化 + 块级适配 + 细粒度路由，在 15-25 个任务上平均超越 SOTA 2.3%，同时减少 47% 参数和 24% 训练时间。

**[SFT Doesn't Always Hurt General Capabilities: Revisiting Domain-Specific Fine-Tuning in LLMs](sft_doesnt_always_hurt_general_capabilities_revisiting_domain-specific_fine-tuni.md)**

:   本文系统性地重新审视了领域特定SFT对LLM通用能力的影响，发现**使用较小学习率即可大幅缓解通用能力退化**，并提出Token-Adaptive Loss Reweighting (TALR)方法通过自适应下调低概率token的损失权重进一步优化领域适配与通用能力之间的权衡。

**[Stress-Testing Alignment Audits With Prompt-Level Strategic Deception](stress-testing_alignment_audits_with_prompt-level_strategic_deception.md)**

:   构建自动 prompt 级红队流水线，对"保守秘密"的模型有机体进行压力测试，发现能诱导黑盒和白盒对齐审计方法产生高置信错误猜测的欺骗策略，首次记录了基于激活的策略性欺骗现象。
