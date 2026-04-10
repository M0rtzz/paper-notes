<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🧪 ICML2025** · 共 **84** 篇

**[A Mathematical Framework for AI-Human Integration in Work](a_mathematical_framework_for_ai-human_integration_in_work.md)**

:   本文提出了一个评估 AI-人类工作集成的数学框架，将技能分解为决策层和执行层两类子技能，理论证明了工作成功概率存在相变效应、互补技能融合可带来超加性收益，并解释了 GenAI 辅助中低技能工人获益更大的"生产力压缩"现象，通过 O*NET 和 Big-bench Lite 数据验证了框架的实用性。

**[ABKD: Pursuing a Proper Allocation of the Probability Mass in Knowledge Distillation via α-β-Divergence](abkd_pursuing_a_proper_allocation_of_the_probability_mass_in_knowledge_distillat.md)**

:   本文深入分析了知识蒸馏中 FKLD 和 RKLD 的概率质量分配缺陷，发现它们在 Hardness-Concentration 和 Confidence-Concentration 两种效应上分别处于极端，提出基于 α-β-divergence 的 ABKD 框架，通过调节 α 和 β 灵活平衡两种效应，在 17 个语言/视觉数据集、12 种师生配置上取得了 SOTA 性能。

**[Agent WARPP: Workflow Adherence via Runtime Parallel Personalization](agent_warpp_workflow_adherence_via_runtime_parallel_personalization.md)**

:   提出 WARPP，一个无需训练的多智能体框架，在运行时根据用户属性动态剪枝条件分支工作流，并通过并行化的 Personalizer 智能体与模块化域特定智能体协同执行，在提升工具调用精度和参数保真度的同时减少 token 消耗。

**[An Efficient Matrix Multiplication Algorithm for Accelerating Inference in Binary and Ternary Neural Networks](an_efficient_matrix_multiplication_algorithm_for_accelerating_inference_in_binar.md)**

:   提出 RSR/RSR++ 算法——通过预处理固定的二值/三值权重矩阵构建分桶排列索引，实现 $O(n^2/\log n)$ 复杂度的向量-矩阵乘法，比标准 $O(n^2)$ 方法快最高 29× 的矩阵乘法、6× 的内存节省，并在 1.58-bit LLM 推理中实现 5.24× 加速。

**[any4: Learned 4-bit Numeric Representation for LLMs](any4_learned_4-bit_numeric_representation_for_llms.md)**

:   提出 any4——一种通过 k-means 聚类学习每行权重矩阵的最优 4-bit 非均匀量化码本的方法，无需权重/激活预处理，在 Llama 2/3、Mistral、Mixtral 上均优于 int4/fp4/nf4，且仅用单个校准样本即可。

**[Best Subset Selection: Optimal Pursuit for Feature Selection and Elimination](best_subset_selection_optimal_pursuit_for_feature_selection_and_elimination.md)**

:   本文从优化视角重新审视经典最优子集选择中的特征选择/消除准则，发现传统准则（相关性选择 + Wald-T 消除）仅捕获了目标函数的"一步变化"而忽视了特征交互，从而提出了"目标函数感知"的最优选择和消除准则，将其作为元替换（Meta-Substitution）即插即用地增强 OMP/CoSaMP/(A)BESS 等经典算法，在压缩感知和稀疏回归任务上实现显著性能提升且不增加计算复杂度。

**[Beyond Communication Overhead: A Multilevel Monte Carlo Approach for Mitigating Compression Bias in Distributed Learning](beyond_communication_overhead_a_multilevel_monte_carlo_approach_for_mitigating_c.md)**

:   本文提出了一种基于多级蒙特卡洛（MLMC）的梯度压缩方案，利用有偏压缩器构造统计无偏的梯度估计，将压缩偏差转化为可控方差，从而在保持有偏压缩器经验效率的同时享受无偏方法的理论保证，结合自适应概率优化在 BERT 微调和 CIFAR-10 上验证了优越性。

**[Beyond Zero Initialization: Investigating the Impact of Non-Zero Initialization on LoRA Fine-Tuning Dynamics](beyond_zero_initialization_investigating_the_impact_of_non-zero_initialization_o.md)**

:   从无限宽度视角理论分析并实验验证：LoRA 的 A、B 矩阵同时非零初始化（Init[AB]）相比传统零初始化（Init[A]）能显著提升对次优学习率的鲁棒性，且引入的随机噪声不影响微调性能——即微调不必严格从预训练模型出发。

**[BlockDialect: Block-wise Fine-grained Mixed Format Quantization for Energy-Efficient LLM Inference](blockdialect_block-wise_fine-grained_mixed_format_quantization_for_energy-effici.md)**

:   提出 BlockDialect——对权重和激活进行块级细粒度混合格式量化，为每个 block 从 FP4 变体（方言）格式书中选择最优数值格式，在 LLaMA3-8B 上比 MXFP4 准确率提升 10.78%，仅比全精度低 5.45%。

**[BoA: Attention-aware Post-training Quantization without Backpropagation](boa_attention-aware_post-training_quantization_without_backpropagation.md)**

:   提出 BoA——首个在训练后量化中考虑跨层依赖性的无反向传播算法，通过构建注意力感知 Hessian 矩阵捕捉注意力模块内的层间交互，在低位宽（INT2）下显著超越现有 PTQ 方法。

**[Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](come_together_but_not_right_now_a_progressive_strategy_to_boost_low-rank_adaptat.md)**

:   > 提出 CoTo（Come Together），一种渐进式训练策略：在微调早期随机关闭 LoRA adapter，激活概率从 0 线性增长至 1，促使梯度在各层间均匀分布；理论上保证了 dropout 稳定性与线性模式连通性，实验表明可同时提升单任务泛化、多任务合并、剪枝鲁棒性并降低训练开销。

**[Context Tuning for In-Context Optimization](context_tuning_for_in-context_optimization.md)**

:   提出 Context Tuning，用少样本示例初始化可训练的 prompt/KV 前缀，通过梯度优化上下文表示（而非模型参数）来增强 LLM 的 few-shot 适应能力，CT-KV 变体在线性时间复杂度下达到与 TTT 竞争的精度。

**[Core Context Aware Transformers for Long Context Language Modeling](core_context_aware_transformers_for_long_context_language_modeling.md)**

:   提出 Core Context Aware (CCA) Attention，通过全局感知池化将输入 token 动态压缩为少量核心 token，结合局部保持模块捕获邻近细粒度信息，实现即插即用地替换标准自注意力，在 128K 上下文下获得 7.9× 加速和 46% 显存节省，同时保持建模性能。

**[DataDecide: How to Predict Best Pretraining Data with Small Experiments](datadecide_how_to_predict_best_pretraining_data_with_small_experiments.md)**

:   > 本文构建了 DataDecide——迄今最大规模的开放模型套件（25 种数据配方 × 14 种模型规模 × 3 个随机种子），系统研究如何用小规模实验预测最佳预训练数据，发现单一小规模排名（如 150M 参数）即可达到约 80% 的成对决策准确率，且连续似然代理指标仅需目标计算量 0.01% 即可让多个基准任务的预测准确率超过 80%。

**[Distilling Tool Knowledge into Language Models via Back-Translated Traces](distilling_tool_knowledge_into_language_models_via_back-translated_traces.md)**

:   本文提出一个多智能体回译流水线，先用 Solver Agent 调用工具（代码解释器）解数学题生成 TIR trace，再用 Translator Agent + Rephrase Agent 将工具调用轨迹转化为纯自然语言推理链，最终用这些合成数据微调小模型，使其在无需工具访问的情况下内化工具知识和结构化推理能力。

**[DLP: Dynamic Layerwise Pruning in Large Language Models](dlp_dynamic_layerwise_pruning_in_large_language_models.md)**

:   提出动态层级剪枝方法 DLP，利用权重与激活值的中位数自适应计算每层的相对重要性，按"越重要稀疏率越低"的原则进行非均匀剪枝，在 70% 高稀疏率下将 LLaMA2-7B 的困惑度降低 7.79、平均零样本准确率提升 2.7%。

**[Do Sparse Autoencoders Generalize? A Case Study of Answerability](do_sparse_autoencoders_generalize_a_case_study_of_answerability.md)**

:   本文系统评估了稀疏自编码器（SAE）提取的特征在"可回答性"（answerability）任务上的跨域泛化能力，发现 SAE 特征的域外迁移表现极不一致——在某些数据集上优于残差流线性探针，但在另一些上接近随机，揭示了当前 SAE 可解释性方法在捕获抽象概念方面的根本局限。

**[DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning](dragon_guard_llm_unlearning_in_context_via_negative_detection_and_reasoning.md)**

:   提出 DRAGON，一种无需微调的 LLM 遗忘框架，通过双层检测模块识别需遗忘的 prompt，再由 CoT guard 模型生成推理指令做上下文干预，在不修改模型参数的前提下实现高效遗忘。

**[Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective](evolving_prompts_in-context_an_open-ended_self-replicating_perspective.md)**

:   提出 PromptQuine 框架，通过进化搜索对 ICL prompt 进行 token 级剪枝，发现将清晰示例剪成看似"乱码"的子序列反而能提升 LLM 性能，且匹配或超越 SOTA prompt 优化方法。

**[Expert Evaluation of LLM World Models: A High-Tc Superconductivity Case Study](expert_evaluation_of_llm_world_models_a_high-t_c_superconductivity_case_study.md)**

:   以高温超导（HTS）领域为案例，构建了专家级数据集（1,726篇论文 + 67道专家问题），系统评估6种LLM系统的科学文献理解能力，发现基于精选文献的RAG系统在事实完整性和证据支持方面显著优于通用闭源模型。

**[FGFP: A Fractional Gaussian Filter and Pruning for Deep Neural Networks Compression](fgfp_a_fractional_gaussian_filter_and_pruning_for_deep_neural_networks_compressi.md)**

:   提出 FGFP 框架，将分数阶微积分与高斯函数结合构建分数阶高斯滤波器（FGF），每个卷积核仅需 7 个参数，配合自适应非结构化剪枝（AUP），在 CIFAR-10 上 ResNet-20 精度仅降 1.52% 即实现 85.2% 的模型压缩率，在 ImageNet 上 ResNet-50 精度降 1.63% 实现 69.1% 压缩率。

**[FGFP: A Fractional Gaussian Filter and Pruning for DNN Compression](fgfp_a_fractional_gaussian_filter_and_pruning_for_deep_neural_networks_compression.md)**

:   提出FGFP框架，将分数阶微积分与高斯函数结合构建分数阶高斯滤波器(FGF)替代标准卷积核，每个核仅需7个参数，配合自适应非结构化剪枝达到极高压缩比（ResNet-20 85.2%压缩仅降1.52%精度）。

**[FlatQuant: Flatness Matters for LLM Quantization](flatquant_flatness_matters_for_llm_quantization.md)**

:   提出 FlatQuant，通过可学习仿射变换（Kronecker 分解）使权重和激活分布更平坦，在 W4A4 量化下首次在 LLaMA-3-70B 上实现 ≤1% 精度损失，同时 prefill 加速 2.3×、decoding 加速 1.7×。

**[Fleet of Agents: Coordinated Problem Solving with Large Language Models](fleet_of_agents_coordinated_problem_solving_with_large_language_models.md)**

:   提出Fleet of Agents(FoA)——用遗传粒子滤波思想协调多Agent的LLM推理：生成多个Agent各自探索→基于启发式价值函数重采样→动态分支适应发现的方案，平均比SOTA方法提升5%质量同时仅需40%的成本。

**[FloE: On-the-Fly MoE Inference on Memory-constrained GPU](floe_on-the-fly_moe_inference_on_memory-constrained_gpu.md)**

:   提出 FloE，一个面向消费级 GPU 的 MoE 即时推理系统，通过专家内部混合压缩（上下文稀疏化 + 超低比特量化）和双预测器实现计算-传输流水线化，在 RTX 3090 上仅 11GB 显存即可部署 Mixtral-8×7B，相比 DeepSpeed-MII 加速 48.7 倍，性能仅下降 4.4%~7.6%。

**[From Language Models over Tokens to Language Models over Characters](from_language_models_over_tokens_to_language_models_over_characters.md)**

:   提出将 token 级语言模型精确转换为字符级语言模型的算法框架，通过定义 covering（最小前缀编码集合）并基于 beam search 近似求解，解决了 prompt boundary 等 token 化导致的用户端问题，同时改善了压缩率（bits/byte）。

**[From Low Rank Gradient Subspace Stabilization To Low-Rank Weights Observations T](from_low_rank_gradient_subspace_stabilization_to_low-rank_weights_observations_t.md)**

:   通过 Hessian 谱分析揭示 LLM 不同权重矩阵的低秩收敛差异，据此提出 WeLore——同时统一模型压缩与参数高效微调的非均匀低秩分解方法。

**[Function-Space Learning Rates](function-space_learning_rates.md)**

:   提出**逐层函数空间学习率**的高效蒙特卡洛估计方法，并基于此设计 **FLeRM**（Function-space Learning Rate Matching），在小模型上记录函数空间学习率，自动调整大模型的参数空间学习率，实现跨宽度、深度、初始化尺度和 LoRA rank 的超参数迁移。

**[Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks](generalization_bounds_via_meta-learned_model_representations_pac-bayes_and_sampl.md)**

:   本文提出了一种基于 hypernetwork 的 meta-learning 框架来获取神经网络的紧泛化界，设计了三种 encoder-decoder 架构（PAC-Bayes 编码器、样本压缩编码器、混合编码器），其中混合方法基于一个新的 PAC-Bayes 样本压缩定理支持连续消息，通过信息瓶颈显式度量模型复杂度，在合成和真实数据集上获得了非空洞的泛化保证。

**[Generalized Interpolating Discrete Diffusion](generalized_interpolating_discrete_diffusion.md)**

:   提出广义插值离散扩散框架 GIDD，将掩码扩散 (MDM) 推广为支持任意时变混合分布的扩散族，通过结合掩码与均匀噪声赋予模型自纠错能力，在扩散语言建模中取得 compute-matched SOTA。

**[GPTAQ: Efficient Finetuning-Free Quantization for Asymmetric Calibration](gptaq_efficient_finetuning-free_quantization_for_asymmetric_calibration.md)**

:   GPTAQ 提出了一种非对称校准（asymmetric calibration）的无微调量化方法，通过将量化层输出与全精度模型的精确输出对齐（而非仅当前层输出），并利用最优脑压缩框架推导闭式解来同时最小化量化误差和累积非对称误差，仅增加约 20 行代码即显著提升 GPTQ 在低比特量化下的性能。

**[GuidedQuant: Large Language Model Quantization via Exploiting End Loss Guidance](guidedquant_large_language_model_quantization_via_exploiting_end_loss_guidance.md)**

:   提出 GuidedQuant，通过将端到端损失的梯度信息融入逐层量化目标（保留输出通道内的权重交互），作为即插即用模块显著提升现有 SOTA PTQ 方法在标量/向量/权重-激活量化上的性能；同时提出 LNQ 算法用于非均匀标量量化，实现 2-bit 下 Llama-2-7B perplexity 从 39.58 降至 8.83。

**[Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](gumiho_a_hybrid_architecture_to_prioritize_early_tokens_in_speculative_decoding.md)**

:   提出 Gumiho，一种用于推测解码的混合 draft 模型架构：前两个 token 使用串行 Transformer 以确保精度，后续 token 使用并行 MLP heads 以提升效率，并通过 Full Tree Attention 机制进一步增加接受长度，在 Vicuna/LLaMA 上实现了最高 3.65x 加速。

**[Improved Exploration in GFlowNets via Enhanced Epistemic Neural Networks](improved_exploration_in_gflownets_via_enhanced_epistemic_neural_networks.md)**

:   将 Epistemic Neural Networks (ENN/epinet) 集成到 GFlowNets 中实现不确定性驱动的探索，提出 ENN-GFN-Enhanced 算法，在 HyperGrid 和序列生成任务上显著改善模式发现效率和分布学习质量。

**[Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](inference-time_decomposition_of_activations_itda_a_scalable_approach_to_interpre.md)**

:   提出 ITDA，一种基于匹配追踪（Matching Pursuit）的推理时激活分解方法，以仅 1% 的 SAE 训练成本实现可比的重构性能，可扩展到 405B 参数模型，并天然支持跨模型表示比较。

**[Instruction-Following Pruning for Large Language Models](instruction-following_pruning_for_large_language_models.md)**

:   提出 IFPruning：用一个小型稀疏预测器根据用户指令动态生成剪枝掩码，将 FFN 中间维度按需裁减，使 9B 模型仅激活 3B 参数即可在编程/数学上超越同规模 dense 模型 5-8 个百分点，且推理延迟与 3B dense 模型持平。

**[Joker: Joint Optimization Framework for Lightweight Kernel Machines](joker_joint_optimization_framework_for_lightweight_kernel_machines.md)**

:   提出 Joker 框架，通过对偶块坐标下降 + 信赖域 (DBCD-TR) 和随机傅里叶特征近似，以 ~2GB 内存实现多种大规模核模型（KRR / KLR / SVM 等）的统一高效训练，内存节省高达 90% 且性能不降。

**[KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search](kbqa-o1_agentic_knowledge_base_question_answering_with_monte_carlo_tree_search.md)**

:   提出 KBQA-o1，将 ReAct Agent 与蒙特卡洛树搜索（MCTS）结合，通过策略模型和奖励模型驱动的启发式搜索实现知识库问答，在低资源设置下以 Llama-3.1-8B 将 GrailQA F1 从 48.5%（GPT-3.5-turbo SOTA）提升至 78.5%。

**[Lacache Ladder-Shaped Kv Caching For Efficient Long-Context Modeling Of Large La](lacache_ladder-shaped_kv_caching_for_efficient_long-context_modeling_of_large_la.md)**

:   提出梯形（ladder-shaped）KV 缓存模式，在不同层保留不同 token 范围的 KV 状态，从而在固定缓存预算下扩展可捕获的上下文跨度，并通过迭代压缩机制支持无限长度的连续生成。

**[Lego Sketch A Scalable Memory-Augmented Neural Network For Sketching Data Stream](lego_sketch_a_scalable_memory-augmented_neural_network_for_sketching_data_stream.md)**

:   提出 Lego Sketch，一种基于模块化"记忆积木"的可扩展记忆增强神经网络（MANN），通过 normalized multi-hash embedding、可扩展内存和自引导加权损失，解决了现有 neural sketch 在跨数据域和不同空间预算下需要重新训练的可扩展性难题，并首次给出了 neural sketch 的误差上界。

**[LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reliable Model Merging](lift_the_veil_for_the_truth_principal_weights_emerge_after_rank_reduction_for_re.md)**

:   发现低秩近似后幅值最大的权重（Principal Weights）是微调关键参数，提出 LIFT——仅更新 top 5% 的 Principal Weights 就在推理任务上超越全参数微调，同时保持 LoRA 级别的内存效率。

**[Liger: Linearizing Large Language Models to Gated Recurrent Structures](liger_linearizing_large_language_models_to_gated_recurrent_structures.md)**

:   Liger 将预训练 Transformer LLM 无额外参数地转换为门控线性循环结构，利用 Key 投影矩阵复用构建门控机制，仅需 0.02% 预训练 token 即可恢复原模型 93% 的性能，同时获得线性时间推理和恒定显存开销。

**[Position: LLM Social Simulations Are a Promising Research Method](llm_social_simulations_are_a_promising_research_method.md)**

:   这篇立场论文（position paper）主张 LLM 社会模拟是一种有前途的研究方法，通过综述实证比较和相关评论，识别了五个可解决的挑战，并提出方向性建议，认为 LLM 社会模拟已可用于试点和探索性研究。

**[LoRA Fine-Tuning Without GPUs: A CPU-Efficient Meta-Generation Framework for LLMs](lora_fine-tuning_without_gpus_a_cpu-efficient_meta-generation_framework_for_llms.md)**

:   提出无 GPU 的 LoRA 微调方法：学习元算子将数据集概率分布映射到 LoRA 权重，利用预训练 adapter 库在 CPU 上通过轻量组合生成新 adapter，性能虽不及 GPU 训练但持续优于基座模型。

**[Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](make_lora_great_again_boosting_lora_with_adaptive_singular_values_and_mixture-of.md)**

:   GOAT 通过“按 SVD 分段初始化的 LoRA-MoE + 理论推导的缩放对齐”，在不改训练算法和主体架构的前提下显著提升 LoRA 表现，并在 25 个任务上达到 SOTA、明显缩小与 Full FT 的差距。

**[MARGE: Improving Math Reasoning for LLMs with Guided Exploration](marge_improving_math_reasoning_for_llms_with_guided_exploration.md)**

:   MARGE 提出了一种基于"命中引导探索"（hit-guided exploration）的方法来增强 LLM 的数学推理能力，通过系统地探索自生成解答中的中间推理状态，实现充分探索和更好的信用分配，无需外部标注或额外价值模型，同时提升了单次准确率和探索多样性。

**[MIB: A Mechanistic Interpretability Benchmark](mib_a_mechanistic_interpretability_benchmark.md)**

:   提出 MIB（Mechanistic Interpretability Benchmark），包含电路定位和因果变量定位两个赛道、四个任务、五个模型，通过标准化的反事实干预评估和新指标（CPR/CMD）系统比较 MI 方法，发现 attribution + mask optimization 方法在电路定位中最优，而 SAE 特征在因果变量定位中并不优于原始神经元。

**[Mind the Gap: A Practical Attack on GGUF Quantization](mind_the_gap_a_practical_attack_on_gguf_quantization.md)**

:   首次提出针对 GGUF 量化格式的攻击：利用量化误差作为"自由度"训练恶意量化模型，全精度下正常但量化后注入后门，在不安全代码生成（Δ=88.7%）、定向内容注入（Δ=85.0%）和良性拒绝（Δ=30.1%）上有效。

**[MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning](mka_memory-keyed_attention_for_efficient_long-context_reasoning.md)**

:   提出 Memory-Keyed Attention (MKA)，将 KV 缓存组织为三级分层记忆（局部/会话/长期），通过可学习路由门动态分配注意力；加速版 FastMKA 在注意力计算前融合记忆源，实现训练吞吐量达 MLA 的 5 倍、解码延迟降至 MLA 的 54%，perplexity 仅损失约 1%。

**[Moragent Parameter Efficient Agent Tuning With Mixture-Of-Roles](moragent_parameter_efficient_agent_tuning_with_mixture-of-roles.md)**

:   提出 Mixture-of-Roles (MoR) 框架，将 Agent 能力分解为推理者、执行者、总结者三个角色，每个角色分配专门的 LoRA 组，以极少额外参数（0.16B–0.36B）实现接近甚至超越全参数微调的 Agent 性能。

**[Neutral Residues: Revisiting Adapters for Model Extension](neutral_residues_revisiting_adapters_for_model_extension.md)**

:   提出 **Neutral Residues**，通过在 adapter 中引入 ReLU 门控 + $\ell_1$ 稀疏局部损失 + 低方差初始化，使新增残差块在原始分布上输出近零值，在 Gemma-2B 上实现新语言学习与英语保持的最佳权衡。

**[Olica Efficient Structured Pruning Of Large Language Models Without Retraining](olica_efficient_structured_pruning_of_large_language_models_without_retraining.md)**

:   提出 Olica 框架，通过对 MHA 层矩阵乘积做正交分解（PCA/SVD）并对 FFN 层做线性校准（岭回归闭式解 + 低秩近似），实现 LLM 结构化剪枝无需重训练，仅需 256 样本、3GB 显存、7 分钟即可完成 LLaMA-7B 剪枝且性能优于需要重训练的方法。

**[OrthoRank: Token Selection via Sink Token Orthogonality for Efficient LLM Inference](orthorank_token_selection_via_sink_token_orthogonality_for_efficient_llm_inferen.md)**

:   提出 OrthoRank，一种**无需额外训练**的动态 token 选择方法：利用 sink token 与其他 token 在隐藏状态空间中的正交性来衡量 token 重要性，在每层选出 Top-K 重要 token 进行完整计算，其余 token 仅参与 KV 计算，在相同稀疏率下实现比层剪枝更低的困惑度和更高的零样本准确率。

**[ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](parallelcomp_parallel_long-context_compressor_for_length_extrapolation.md)**

:   提出 ParallelComp，一种免训练的并行长上下文压缩方法，通过并行 KV cache 驱逐和注意力校准策略，使 8B 参数 LLM 在单块 A100 GPU 上从 8K 外推至 128K tokens。

**[Parameter-Efficient Fine-Tuning of State Space Models](parameter-efficient_fine-tuning_of_state_space_models.md)**

:   本文系统性地评估了现有 PEFT 方法在 SSM（如 Mamba）模型上的效果，发现 LoRA 虽在线性投影层表现最优但无法有效调优 SSM 模块，进而提出 Sparse Dimension Tuning（SDT）——一种专为 SSM 模块设计的 PEFT 方法，结合 LoRA 用于线性层，在多个基准上达到 SOTA 性能。

**[Persistent Topological Features in Large Language Models](persistent_topological_features_in_large_language_models.md)**

:   将拓扑数据分析中的 zigzag persistence 引入 LLM 内部表征分析，通过追踪 prompt 在各层表示空间中拓扑特征的持续演化，识别出四个处理阶段，并基于拓扑描述子提出了一种层剪枝准则，效果可比肩 SOTA 方法。

**[Predictive Data Selection: The Data That Predicts Is the Data That Teaches](predictive_data_selection_the_data_that_predicts_is_the_data_that_teaches.md)**

:   提出 PreSelect 方法，基于"能预测模型能力的数据就是能教会模型的数据"这一假设，利用多模型损失排名相关性量化文档预测强度，训练 fastText 分类器实现高效数据选择，在 1B 模型上用 30B tokens 超越随机选取 300B tokens 的性能，实现 10 倍计算节省。

**[Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](putnam-axiom_a_functional_and_static_benchmark_for_measuring_higher_level_mathem.md)**

:   提出 Putnam-AXIOM —— 522 道大学级 Putnam 竞赛数学题 + 100 道程序化功能变体，揭示 LLM 数学推理中的记忆依赖，并引入 Teacher-Forced Accuracy (TFA) 作为超越最终答案的推理质量评估指标。

**[Q-resafe: Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](q-resafe_assessing_safety_risks_and_quantization-aware_safety_patching_for_quant.md)**

:   系统评估了主流量化方法（AWQ、AQLM、LLM-QAT、QLoRA）在不同校准数据集和位宽下对LLM安全性的影响，发现所有量化方法均导致ASR大幅上升（0.3%→85%），并提出Q-resafe框架通过安全补丁数据构建+DPO对齐+选择性安全关键权重更新，以极低计算开销高效恢复量化模型的安全能力。

**[RADIO: Rate-Distortion Optimization for Large Language Model Compression](radio_rate-distortion_optimization_for_large_language_model_compression.md)**

:   RADIO 从信息论中的率失真理论（Rate-Distortion Theory）出发，为 LLM 量化建立了理论基础，并提出了一种基于率失真优化的简洁量化技术，可扩展至数千亿参数模型，且允许用户灵活指定目标模型大小或精度进行后训练压缩。

**[Random Initialization of Gated Sparse Adapters (RIGSA)](random_initialization_of_gated_sparse_adapters.md)**

:   提出 RIGSA，一种基于随机初始化全秩适配器 + ReZero 门控 + 迭代幅度剪枝的稀疏微调方法，在学习新任务的同时比 QLoRA 更好地保留源任务性能。

**[Regress, Don't Guess — A Regression-like Loss on Number Tokens for Language Models](regress_dont_guess_--_a_regression-like_loss_on_number_tokens_for_language_model.md)**

:   提出 Number Token Loss (NTL)，一种纯 token 级别的回归式损失函数，通过最小化数值 token 之间的 $L_p$ 范数或 Wasserstein 距离，为 LLM 注入数值邻近性归纳偏置。

**[Rethinking Addressing in Language Models via Contextualized Equivariant Positional Encoding](rethinking_addressing_in_language_models_via_contexualized_equivariant_positiona.md)**

:   本文提出 TAPE（contexTualized equivariAnt Position Encoding），通过在各层动态地根据序列内容更新位置编码来取代传统的固定位置模式，同时强制排列和正交等变性以保证稳定性，在语言建模、算术推理和长上下文检索任务上显著超越现有位置编码方法。

**[Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective](rethinking_the_stability-plasticity_trade-off_in_continual_learning_from_an_arch.md)**

:   揭示了持续学习中稳定性与可塑性之间在**架构层面**的固有冲突——宽浅网络稳定性好、深窄网络可塑性强——并提出 Dual-Arch 框架，用两个专用轻量架构分别负责稳定性和可塑性，通过知识蒸馏协同，实现参数量减少最高 87% 的同时提升 CL 性能。

**[RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](rocketkv_accelerating_long-context_llm_inference_via_two-stage_kv_cache_compress.md)**

:   提出 RocketKV，一种无需训练的两阶段 KV 缓存压缩方法：第一阶段用 SnapKV 做粗粒度永久驱逐，第二阶段用混合稀疏注意力（HSA）做细粒度动态 top-k 选择，在 Mistral-7B 等模型上实现高达 400× 压缩比、3.7× 端到端加速和 32.6% 峰值内存节省，精度损失可忽略。

**[SAFE: Finding Sparse and Flat Minima to Improve Pruning](safe_finding_sparse_and_flat_minima_to_improve_pruning.md)**

:   将剪枝问题建模为稀疏约束下的锐度感知优化问题，通过增广拉格朗日对偶法（ADMM）求解，同时实现稀疏性和平坦极小值，提升剪枝后网络的泛化性能和鲁棒性。

**[SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior](safetyanalyst_interpretable_transparent_and_steerable_safety_moderation_for_ai_b.md)**

:   提出 SafetyAnalyst 框架，通过链式思维推理生成可解释的"危害-收益树"（枚举 AI 行为可能导致的有害和有益效果及其可能性/严重性/即时性），再用 28 个全可解释参数聚合为危害分数，在 prompt 安全分类上以平均 F1=0.81 超越现有审核系统（F1<0.72），同时提供可解释性、透明性和可操控性。

**[Sample Efficient Demonstration Selection for In-Context Learning](sample_efficient_demonstration_selection_for_in-context_learning.md)**

:   本文提出了一种样本高效的上下文学习(ICL)示例选择方法，能够在有限的标注预算下高效地选择最佳示例组合，显著提升 LLM 的 ICL 性能，同时大幅减少所需的标注数据量。

**[Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](sketch_to_adapt_fine-tunable_sketches_for_efficient_llm_adaptation.md)**

:   SpaLLM 提出了一种基于 sketching 的参数共享方法来统一 LLM 的压缩和微调过程，将预训练权重压缩为查找表（LUT）后直接在表值上微调，避免了 QLoRA 等双塔架构的低秩假设和实现复杂性，在多项基准上以更少的训练参数取得了优于 QLoRA/LoftQ 的性能。

**[SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression](slim_one-shot_quantization_and_sparsity_with_low-rank_approximation_for_llm_weig.md)**

:   提出 SLiM，一种一次性压缩框架，将硬件友好的均匀量化、半结构化稀疏和基于显著性的低秩适配器无缝整合，在 4-bit + 2:4 稀疏条件下准确率提升最高 5.66%。

**[Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](soft_reasoning_navigating_solution_spaces_in_large_language_models_through_contr.md)**

:   本文提出 Soft Reasoning，通过在首个生成 token 的 embedding 空间注入高斯扰动并用贝叶斯优化搜索最优扰动向量，以黑盒方式引导 LLM 在推理过程中探索更优的解空间，无需访问模型参数或额外验证器，在数学推理等任务上以极低计算开销超越 temperature scaling 和 Best-of-N 等基线。

**[SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](sparselora_accelerating_llm_fine-tuning_with_contextual_sparsity.md)**

:   提出 SparseLoRA，通过**上下文稀疏性 (contextual sparsity)** 动态选择权重子集进行前向/梯度计算，首次将推理时的稀疏加速思路迁移到 LLM 微调阶段，实现最高 2.2× FLOPs 降低和 1.6× 实测加速，同时保持精度。

**[Speculative Decoding in Decentralized LLM Inference: Turning Communication Latency into Computation Throughput](speculative_decoding_in_decentralized_llm_inference_turning_communication_latenc.md)**

:   提出 Decentralized Speculative Decoding (DSD)，一种即插即用的去中心化LLM推理加速框架，通过将跨节点通信等待时间转化为有效计算，结合基于语义重要性的自适应验证策略，在无需重训练的前提下实现最高 2.59× 的端到端加速。

**[Steer LLM Latents for Hallucination Detection](steer_llm_latents_for_hallucination_detection.md)**

:   提出 Truthfulness Separator Vector (TSV)，一种轻量级 steering vector，在推理时重塑 LLM 表示空间以增强真实与幻觉输出的分离，仅需 32 个标注样本即可接近全监督性能。

**[Strategic Fusion Optimizes Transformer Compression](strategic_fusion_optimizes_transformer_compression.md)**

:   本文提出 Strategic Fusion 框架，将 12 种基于激活值/互信息/梯度/权重/注意力的层剪枝信号通过线性回归和随机森林进行融合，在 BERT 模型和 9 个文本分类数据集上验证了多信号融合剪枝优于单信号策略，结合知识蒸馏后准确率-模型大小比平均提升 18.84 倍。

**[Text-to-LoRA: Instant Transformer Adaption](text-to-lora_instant_transformer_adaption.md)**

:   Text-to-LoRA (T2L) 训练了一个超网络（hypernetwork），仅凭自然语言任务描述就能在单次前向传播中为 LLM 生成任务特定的 LoRA 适配器，在 9 个训练任务上匹配专门微调的 LoRA 性能，并能零样本泛化到未见过的任务，实现了语言驱动的即时模型适配。

**[Towards an Optimal Control Perspective of ResNet Training](towards_an_optimal_control_perspective_of_resnet_training.md)**

:   将 ResNet 训练形式化为最优控制问题，通过在中间层添加阶段成本 (stage cost) 损失实现自正则化，证明多余的深层权重渐近趋零，为理论驱动的层剪枝奠定基础。

**[Towards Flexible Perception With Visual Memory](towards_flexible_perception_with_visual_memory.md)**

:   将深度视觉模型的知识表示从"刻在权重里"转变为"存在外部数据库里"，用预训练编码器 + kNN 检索构建灵活的 Visual Memory，实现数据的即插即拔（添加/删除/扩展）和可解释分类，ImageNet 上达到 88.5% top-1 准确率。

**[Training a Generally Curious Agent (Paprika)](training_a_generally_curious_agent.md)**

:   提出 Paprika 框架，通过在多种文本决策任务上微调 LLM，使模型学会通用的信息收集和决策能力，并能零样本迁移到完全未见的任务。

**[TreeLoRA: Efficient Continual Learning via Layer-wise LoRAs Guided by Hierarchical Gradient-Similarity Tree](treelora_efficient_continual_learning_via_layer-wise_loras_guided_by_a_hierarchi.md)**

:   提出TreeLoRA——用K-D树组织的层级任务结构指导层级LoRA适配器分配：用bandit-based下置信界算法高效探索任务结构+稀疏梯度更新优化参数，在ViT和LLM上都有效，理论保证学习收敛。

**[VocabTrim: Vocabulary Pruning for Efficient Speculative Decoding in LLMs](vocabtrim_vocabulary_pruning_for_efficient_speculative_decoding_in_llms.md)**

:   提出 VocabTrim，一种免训练方法，通过剪枝 draft 模型的 LM head 词汇表来减少推测解码中的 draft 延迟，在 Llama-3 上实现 16% 的内存受限加速提升。

**[Weak-to-Strong Jailbreaking on Large Language Models](weak-to-strong_jailbreaking_on_large_language_models.md)**

:   本文提出 weak-to-strong 越狱攻击：利用两个小模型（一个安全、一个不安全）在推理时通过对数概率代数修改大模型的解码分布，仅需一次前向传播即可将对齐大模型的恶意回复率提升至 99% 以上，揭示了 LLM 对齐中一个此前未被注意的高效攻击面。

**[When Data-Free Knowledge Distillation Meets Non-Transferable Teacher: Escaping Out-of-Distribution](when_data-free_knowledge_distillation_meets_non-transferable_teacher_escaping_ou.md)**

:   本文研究了在教师模型为"不可迁移"（non-transferable）设计时无数据知识蒸馏面临的挑战——合成样本容易落入分布外区域导致蒸馏失败，提出了逃逸分布外区域（escaping OOD）的方法来实现有效蒸馏。

**[WildChat-50m: A Deep Dive Into the Role of Synthetic Data in Post-Training](wildchat-50m_a_deep_dive_into_the_role_of_synthetic_data_in_post-training.md)**

:   构建迄今最大的公开聊天数据集 WildChat-50m（50+ 开源模型 × 100万+ 对话 = 1.25 亿条转录），系统研究不同数据生成模型（DGM）的合成数据质量，并设计 Re-Wild SFT 混合方案，仅用 Tulu-3 SFT 数据量的 40% 即在多项基准上超越其表现。
