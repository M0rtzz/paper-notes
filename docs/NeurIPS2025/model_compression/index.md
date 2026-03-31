<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🧠 NeurIPS2025** · 共 **90** 篇

**[3DID: Direct 3D Inverse Design for Aerodynamics with Physics-Aware Optimization](3did_direct_3d_inverse_design_for_aerodynamics_with_physics-aware_optimization.md)**

:   提出 3DID 框架，通过学习物理-几何统一的三平面隐空间表示 + 目标梯度引导扩散采样 + 拓扑保持精炼的两阶段策略，从随机噪声开始直接在完整 3D 空间中进行逆向设计，在车辆气动外形优化上，模拟阻力（Sim-Drag）相比最优基线降低 13.6%。

**[4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming](4dgcpro_efficient_hierarchical_4d_gaussian_compression_for_p.md)**

:   提出层级化的4D高斯压缩框架4DGCPro，通过感知加权的层级高斯表示、运动感知自适应分组和端到端熵优化训练，在单一模型内实现多码率渐进式体积视频流媒体，可在移动设备上实时解码和渲染，RD性能超越现有SOTA。

**[A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](a-thought_efficient_reasoning_via_bidirectional_compression_for_low-resource_set.md)**

:   提出 A*-Thought——基于 A* 搜索算法的 CoT 压缩框架，通过双向重要性评分（BIS）衡量每个推理步骤对问题和答案的相关性，结合路径级 A* 搜索在指数级搜索空间中高效找到最紧凑的推理路径，在 512 token 预算下将 QwQ-32B 准确率提升 2.39 倍，在 4096 token 预算下减少约 50% 输出 token 且几乎不损失准确率。

**[A Granular Study of Safety Pretraining under Model Abliteration](a_granular_study_of_safety_pretraining_under_model_abliteration.md)**

:   本文系统地研究了 model abliteration（一种推理时激活空间编辑攻击）对不同数据驱动安全预训练阶段的影响，发现仅依赖 refusal 训练的安全机制极易被攻破，而 **组合多种安全信号**（safe-only 过滤 + 改写 + metatag + refusal）可使安全行为分散到更广泛的表征空间、从而更难被单一方向投影移除。

**[A is for Absorption: Studying Feature Splitting and Absorption in Sparse Autoencoders](a_is_for_absorption_studying_feature_splitting_and_absorption_in_sparse_autoenco.md)**

:   发现并系统研究了 SAE 中的"特征吸收"现象：看似单义的 SAE latent 会在特定 token 上不激活，其特征方向被更具体的子 latent "吸收"，这是层级特征+稀疏性损失的必然结果，对 SAE 用于可靠解释 LLM 构成根本挑战。

**[A Partition Cover Approach for Tokenization](a_partition_cover_approach_to_tokenization.md)**

:   将分词（tokenization）问题重新建模为**分区覆盖（partition cover）**优化问题，证明其为NP-hard，并提出多项式时间的贪心算法GreedTok，在压缩率和1B参数LLM预训练下游任务上均优于BPE。

**[A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone](a_token_is_worth_over_1000_tokens_efficient_knowledge_distillation_through_low-r.md)**

:   提出 Low-Rank Clone (LRC)，通过可学习低秩投影矩阵将 teacher 权重压缩为 student 权重（软剪枝），同时对齐 attention 和 FFN 的中间激活（激活克隆），仅用 20B tokens 训练的 1.7B 模型即超过用 36T tokens 训练的 Qwen3-1.7B（64.98 vs 63.17），实现 **1000 倍训练效率提升**。

**[Accurate and Efficient Low-Rank Model Merging in Core Space](accurate_and_efficient_low-rank_model_merging_in_core_space.md)**

:   提出 Core Space Merging 框架——通过在低秩 LoRA 矩阵的公共参考基空间中进行模型合并，**无信息损失**地将合并操作从 $m \times n$ 全尺寸空间压缩到 $Tr \times Tr$ 紧凑空间（$T$ 为任务数，$r$ 为 LoRA 秩），在 Llama 3 8B 上达到 SOTA 合并精度同时计算成本降低数个数量级。

**[Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs](adaptive_kernel_design_for_bayesian_optimization_is_a_piece_of_cake_with_llms.md)**

:   提出 CAKE (Context-Aware Kernel Evolution)，利用 LLM 作为遗传算法的交叉和变异算子，在贝叶斯优化过程中自适应地生成和进化 GP 核函数表达式，结合 BAKER 排序机制平衡模型拟合（BIC）与期望改进（EI），在超参数优化、控制器调参和光子芯片设计等任务上持续超越固定核和自适应核基线。

**[Adaptive Originality Filtering: Rejection-Based Prompting and RiddleScore for Culturally Grounded Multilingual Riddle Generation](adaptive_originality_filtering_rejection_based_prompting_and_riddlescore_for_cul.md)**

:   提出 Adaptive Originality Filtering (AOF)——一种基于语义拒绝采样的提示策略，通过 MiniLM 嵌入的余弦相似度过滤重复/模板化输出，强制 LLM 生成更新颖、多样且文化匹配的多语言谜语；同时提出 RiddleScore 复合评估指标（Novelty + Diversity + Fluency + Alignment），与人类评分相关性达 $\rho=0.83$。

**[Adaptive Prediction-Powered AutoEval with Reliability and Efficiency Guarantees](adaptive_predictionpowered_autoeval_with_reliability_and_eff.md)**

:   提出R-AutoEval+，通过e-value赌注算法自适应调整对合成数据（LLM评判器）的依赖权重，首次同时提供有限样本可靠性保证和可证明的采样效率改善，在GSM8K上比纯真实数据方法节省87个token。

**[Adaptive Stochastic Coefficients for Accelerating Diffusion Sampling](adaptive_stochastic_coefficients_for_accelerating_diffusion_sampling.md)**

:   通过理论分析 ODE 和 SDE 求解器的互补弱点（ODE 积累不可消除的梯度误差，SDE 在少步时离散化误差放大），提出 AdaSDE——在每个去噪步引入可学习随机系数 $\gamma_i$ 控制噪声注入强度，通过轻量蒸馏优化，在 5 NFE 下实现 CIFAR-10 FID 4.18、FFHQ FID 8.05 的 SOTA。

**[AdmTree: Compressing Lengthy Context with Adaptive Semantic Trees](admtree_compressing_lengthy_context_with_adaptive_semantic_trees.md)**

:   提出 AdmTree——一种自适应层次化上下文压缩框架,通过信息密度驱动的动态分段构建叶 gist token，再用二叉语义树底向上聚合实现多粒度语义保留，解决了显式方法丢失局部细节和隐式方法位置偏差的双重问题,在 LongBench 上比 SOTA 基线 Activation Beacon 高 10%+。

**[AI-Generated Video Detection via Perceptual Straightening](ai-generated_video_detection_via_perceptual_straightening.md)**

:   提出 ReStraV 方法，基于"感知拉直"假说（真实视频在神经表示空间形成更直的轨迹），利用 DINOv2 特征空间中的时间曲率和步距统计量训练轻量分类器检测 AI 生成视频，在 VidProM 上达到 97.17% 准确率和 98.63% AUROC，推理仅需 ~48ms。

**[AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise](autodiscovery_open-ended_scientific_discovery_via_bayesian_surprise.md)**

:   AutoDiscovery 提出用贝叶斯惊奇度（Bayesian Surprise）作为开放式科学发现的客观奖励信号——通过 LLM 采样估计先验/后验信念分布的 KL 散度，配合 MCTS+渐进展宽在假设空间中探索，在 21 个真实数据集上比贪心/束搜索产生 5-29% 更多的惊奇发现，人类评估确认贝叶斯惊奇度与专家"惊讶感"的一致性（0.67）远超 LLM 自身评估的"新颖性"和"有用性"。

**[AutoJudge: Judge Decoding Without Manual Annotation](autojudge_judge_decoding_without_manual_annotation.md)**

:   AutoJudge 自动化了 Judge Decoding 中"重要 token"的标注——通过半贪心搜索替换不匹配 token 并检查答案是否改变来标注重要性，训练逻辑回归分类器预测 token 重要性，使投机解码每轮接受 40+ token（vs 标准 ~20），在 GSM8K 上加速 1.5× 且准确率损失 <1%。

**[BaRISTA: Brain-Scale Informed Spatiotemporal Representation of Human Intracranial EEG](barista_brain_scale_informed_spatiotemporal_representation_of_human_intracranial.md)**

:   BaRISTA 系统探索 iEEG Transformer 的空间编码尺度（电极/脑区/脑叶），发现脑区级编码 + 空间掩码重建在语言任务解码上达 86.2% AUC（vs PopT 79.5%），编码尺度选择的影响 > 掩码策略选择，且跨被试泛化性好。

**[Benford's Curse: Tracing Digit Bias to Numerical Hallucination in LLMs](benfords_curse_tracing_digit_bias_to_numerical_hallucination_in_llms.md)**

:   本文发现 LLM 的数值幻觉根源于预训练语料中符合 Benford 定律的数字频率分布——数字 1 出现概率 ~30% 而数字 9 仅 ~5%，这种偏差被 FFN 后期层的特定"数字选择性神经元"内化，提出数字选择性分数（DSC）定位偏差神经元并通过剪枝 0.01% 的神经元修正 1.36-3.49% 的错误预测。

**[Better Estimation of the Kullback-Leibler Divergence Between Language Models](better_estimation_of_the_kullback--leibler_divergence_between_language_models.md)**

:   提出 KL 散度的 Rao-Blackwell 化 Monte Carlo 估计器——在每个位置对下一个 token 的分布求精确 KL（而非只用采样的 token），理论证明无偏且方差严格不超过标准 MC 估计器，零额外计算开销，在 RLHF 情感控制任务中使训练更稳定、模型更频繁出现在 Pareto 前沿（78%）。

**[Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning](beyond_accuracy_dissecting_mathematical_reasoning_for_llms_u.md)**

:   提出 SPARKLE 三轴分析框架（计划执行、知识整合、子问题分解）细粒度剖析 RL 如何改变 LLM 推理行为，发现 RL 主要增强了知识整合能力和计划灵活性而非计划执行能力，并提出 SparkleRL-PSS 多阶段 RL 训练 pipeline 通过 partial step scaffolding 有效利用难题数据。

**[Beyond Higher Rank: Token-wise Input-Output Projections for Efficient Low-Rank Adaptation](beyond_higher_rank_token-wise_input-output_projections_for_efficient_low-rank_ad.md)**

:   TopLoRA 从输入-输出投影角度分析 LoRA 的表达能力，发现所有 token 共享同一投影矩阵是关键瓶颈，提出通过可学习的 token 级对角矩阵 $\Sigma_X$ 动态调整 LoRA 权重（$\Delta W_X = B\Sigma_X A$），在不增加秩的前提下实现细粒度适配，跨任务一致优于 LoRA 2-3%。

**[Beyond Random: Automatic Inner-Loop Optimization in Dataset Distillation](beyond_random_automatic_inner-loop_optimization_in_dataset_distillation.md)**

:   提出 AT-BPTT（自适应截断 BPTT），将 DNN 训练分为早/中/晚三阶段并自适应调整截断策略和窗口大小，在 CIFAR-10/100/Tiny-ImageNet/ImageNet-1K 上平均提升 3-17%，同时实现 3.9× 加速和 63% 内存节省。

**[Bézier Splatting for Fast and Differentiable Vector Graphics Rendering](bezier_splatting_for_fast_and_differentiable_vector_graphics_rendering.md)**

:   Bézier Splatting 将 Gaussian Splatting 框架与 Bézier 曲线结合，沿曲线均匀采样 2D Gaussian 点，通过 α-blending 渲染实现可微矢量图形，前向 30× / 反向 150× 加速（相比 DiffVG），同时保持或超越 LIVE 等方法的图像质量。

**[Binary Quadratic Quantization: Beyond First-Order Quantization for Real-Valued Matrix Compression](binary_quadratic_quantization_beyond_first-order_quantization_for_real-valued_ma.md)**

:   BQQ 提出二次二值量化——用二值矩阵的乘积（而非线性组合）表示权重矩阵，突破传统一阶量化的表达能力限制，通过扩展 AMFD（退火均场下降）到 PUBO 问题求解混合整数优化，在 2-bit 无数据 ViT 量化上实现从 10.83% 到 58.25% 的准确率飞跃。

**[BioBench: A Blueprint to Move Beyond ImageNet for Scientific ML Benchmarks](biobench_a_blueprint_to_move_beyond_imagenet_for_scientific_ml_benchmarks.md)**

:   提出 BioBench——一个统一 9 个生态视觉任务、4 个分类界、6 种图像模态、310 万张图像的基准，证明 ImageNet top-1 准确率仅解释 34% 的生态任务方差，在 >75% 精度的前沿模型中 30% 的排名是错误的。

**[C-LoRA: Contextual Low-Rank Adaptation for Uncertainty Estimation in Large Language Models](c-lora_contextual_low-rank_adaptation_for_uncertainty_estimation_in_large_langua.md)**

:   提出 C-LoRA，通过引入轻量级上下文模块使 LoRA 低秩矩阵的分布依赖于输入数据，实现样本级的异方差不确定性估计，在少样本微调场景中显著改善校准质量。

**[CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs](casspec_cascade_adaptive_selfspeculative_decoding_for_onthef.md)**

:   CAS-Spec 通过 Dynamically Switchable Inference Acceleration (DSIA) 策略（如不同程度的 layer sparsity）从目标模型自身构建多级 draft 模型层级，配合 Dynamic Tree Cascade (DyTC) 算法基于在线 acceptance rate 和延迟预测自适应路由 draft 模型和分配 draft 长度，在完全 training-free 的条件下实现 1.1×-2.3× 的无损推理加速，DyTC 比 cascade 和 tree baseline 分别提升 47% 和 48%。

**[ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](chunkkv_semanticpreserving_kv_cache_compression_for_efficien.md)**

:   ChunkKV 将 KV cache 压缩的基本单元从离散 token 提升为语义 chunk（连续 token 组），通过 chunk 级 attention score 聚合来选择保留哪些语义完整的片段，并利用 chunk 带来的高跨层索引相似性实现 layer-wise index reuse，在 10% 压缩率下比 SnapKV/PyramidKV 提升最高 8.7%，吞吐量提升 26.5%。

**[CodeGEMM: A Codebook-Centric Approach to Efficient GEMM in Quantized LLMs](codegemm_a_codebook-centric_approach_to_efficient_gemm_in_quantized_llms.md)**

:   提出 CodeGEMM，一种以 codebook 为中心的 GEMM kernel，通过预计算 centroid 与 activation 的内积并缓存为 Psumbook，替代传统反量化流程，在 2-bit 量化 LLM 上实现 1.83×（8B）到 8.93×（70B）的端到端加速。

**[Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers](compress_gather_and_recompute_reforming_long-context_processing_in_transformers.md)**

:   提出 REFORM 推理框架，通过"压缩—检索—重算"三阶段流水线高效处理超长上下文（百万级 token），在 RULER 和 BABILong 上相比最强基线分别提升 52% 和 34%，同时降低 30% 推理时间和 5% 峰值显存。

**[ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts](conceptscope_characterizing_dataset_bias_via_disentangled_visual_concepts.md)**

:   提出 ConceptScope 框架，利用在视觉基础模型表征上训练的稀疏自编码器（SAE）自动发现和量化数据集中的视觉概念偏差，无需人工标注即可将概念分类为 target / context / bias 三类。

**[Conditional Distribution Compression via the Kernel Conditional Mean Embedding](conditional_distribution_compression_via_the_kernel_conditional_mean_embedding.md)**

:   首次提出针对**条件分布**（而非联合分布）的压缩算法，利用核条件均值嵌入（KCME）定义新度量 AMCMD，并设计线性时间算法 ACKIP 构建保留条件分布统计特性的压缩数据集。

**[Correlation Dimension of Auto-Regressive Large Language Models](correlation_dimension_of_auto-regressive_large_language_models.md)**

:   引入源于分形几何的**相关维数（correlation dimension）**作为衡量自回归语言模型感知文本复杂度的指标，揭示了传统 perplexity 无法捕捉的长程结构特性，可检测幻觉和退化文本。

**[Curiosity-driven RL for Symbolic Equation Solving](curiosity-driven_rl_for_symbolic_equation_solving.md)**

:   将好奇心驱动探索（RND、ICM 等）与基于表达式树的图动作空间结合，使 PPO 智能体能够求解包含根号、指数和三角函数的非线性方程，超越了此前仅限于线性方程的 RL 方法。

**[Curvature Tuning: Provable Training-free Model Steering From a Single Parameter](curvature_tuning_provable_training-free_model_steering_from_a_single_parameter.md)**

:   提出 Curvature Tuning（CT），通过在激活函数中注入单个超参数 $\beta$ 来可证明地调节模型决策边界的曲率，无需修改权重即可提升泛化和鲁棒性，同时作为微调方法参数量远少于 LoRA rank 1。

**[Data Efficient Adaptation in Large Language Models via Continuous Low-Rank Fine-Tuning](data_efficient_adaptation_in_large_language_models_via_continuous_low-rank_fine-.md)**

:   提出 DEAL 框架，通过小波核特征过滤保留 LoRA 低秩矩阵中的历史知识核心特征，结合受控知识更新模块和非对称正则化，实现 LLM 在小样本持续微调中学新不忘旧。

**[Dataset Distillation for Pre-Trained Self-Supervised Vision Models](dataset_distillation_for_pre-trained_self-supervised_vision_models.md)**

:   提出 Linear Gradient Matching 方法，为预训练自监督视觉模型蒸馏合成数据集：每类仅需一张合成图就能训练出接近全数据集表现的线性分类器，且蒸馏图像可跨模型架构迁移。

**[DeepTraverse: A Depth-First Search Inspired Network for Algorithmic Visual Understanding](deeptraverse_a_depth-first_search_inspired_network_for_algorithmic_visual_unders.md)**

:   受深度优先搜索（DFS）算法启发，设计了 DeepTraverse 视觉骨干网络，通过参数共享的递归探索模块和自适应通道校准模块，在极少参数下实现高竞争力的图像分类性能。

**[DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method](deltaflow_an_efficient_multi-frame_scene_flow_estimation_method.md)**

:   提出 DeltaFlow (ΔFlow)，通过体素帧间差分（Δ scheme）提取运动线索，实现特征尺寸不随帧数增长的多帧场景流估计，在 Argoverse 2/Waymo/nuScenes 上达到 SOTA 且比次优多帧方法快 2 倍。

**[Dense Backpropagation Improves Training for Sparse Mixture-of-Experts](dense_backpropagation_improves_training_for_sparse_mixture-of-experts.md)**

:   提出 Default MoE 方法，用指数移动平均（EMA）近似非激活 expert 的输出，使 MoE router 获得稠密梯度更新，在不显著增加计算开销的情况下提升稀疏 MoE 的训练性能。

**[Dependency Parsing is More Parameter-Efficient with Normalization](dependency_parsing_is_more_parameter-efficient_with_normalization.md)**

:   揭示依存句法/语义分析中 biaffine scoring 缺乏归一化导致模型过参数化，通过简单的 $1/\sqrt{d}$ 缩放即可在减少高达 85% BiLSTM 参数的同时匹配甚至超越原始性能。

**[Deterministic Continuous Replacement: Fast and Stable Module Replacement in Pretrained Transformers](deterministic_continuous_replacement_fast_and_stable_module_replacement_in_pretr.md)**

:   DCR 通过确定性退火权重 α(t) 混合 teacher 和 student 模块输出，消除了随机门控（如 BERT-of-Theseus）带来的梯度方差，在冷启动模块替换场景下实现更快收敛和更强的特征对齐。

**[Disentangling Latent Shifts of In-Context Learning with Weak Supervision](disentangling_latent_shifts_of_in-context_learning_with_weak_supervision.md)**

:   WILDA 将 ICL 视为弱监督信号，用 teacher-student 框架将示例引发的潜在偏移编码进轻量 LoRA 适配器，实现无需重复 prompting 的高效推理，且 student 通过伪标签修正和覆盖扩展超越 teacher（弱到强泛化）。

**[DisMo: Disentangled Motion Representations for Open-World Motion Transfer](dismo_disentangled_motion_representations_for_openworld_moti.md)**

:   DisMo 通过双流架构（运动提取器 + 帧生成器）和图像空间重建目标，从原始视频中学习与外观、姿态、类别无关的抽象运动表征，实现跨类别/跨视角的开放世界运动迁移，并在零样本动作分类上大幅超越 V-JEPA 等视频表征模型。

**[DP-LLM: Runtime Model Adaptation with Dynamic Layer-wise Precision Assignment](dp-llm_runtime_model_adaptation_with_dynamic_layer-wise_precision_assignment.md)**

:   DP-LLM 发现每层的量化敏感度在解码步间动态变化，提出基于 relative error 的动态逐层精度选择机制，在运行时根据输入为每层分配精度（h-bit 或 l-bit），实现了优于静态混合精度的性能-延迟权衡。

**[DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning](dragon_guard_llm_unlearning_in_context_via_negative_detection_and_reasoning.md)**

:   DRAGON 提出无需微调基座模型的系统性 LLM 遗忘框架：通过双层检测模块识别需遗忘的 prompt，再由专门微调的 guard 模型生成 CoT 推理指令实现上下文干预，在保持模型通用能力的同时有效删除隐私/有害知识。

**[DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs](duogpt_training-free_dual_sparsity_through_activation-aware_pruning_in_llms.md)**

:   提出 DuoGPT，一种将激活稀疏（activation sparsity）重新解释为动态结构化权重稀疏、并与非结构化权重剪枝相结合的双稀疏（dual-sparse）框架，通过扩展 OBC 框架引入激活感知校准和稠密模型输出残差修正项，在不需要重训练的情况下实现 LLM 解码阶段的显著加速与内存节省。

**[Elastic ViTs from Pretrained Models without Retraining](elastic_vits_from_pretrained_models_without_retraining.md)**

:   SnapViT 提出一种后训练结构化剪枝方法：结合自监督梯度的局部 Hessian 和进化算法估计的全局跨模块相关性，无需重训练或标签即可在一次运行中生成连续稀疏度的弹性 ViT 子网络，在 A100 上仅需不到 5 分钟。

**[EMLoC: Emulator-based Memory-efficient Fine-tuning with LoRA Correction](emloc_emulator-based_memory-efficient_fine-tuning_with_lora_correction.md)**

:   EMLoC 通过对原始模型做 activation-aware SVD 构建轻量级 emulator 进行 LoRA 微调，并提出 LoRA 校正算法弥补 emulator 与原模型的不对齐，使得微调内存开销降至与推理持平，在单张 24GB GPU 上即可微调 38B 模型。

**[Enhancing Semi-supervised Learning with Zero-shot Pseudolabels](enhancing_semi-supervised_learning_with_zero-shot_pseudolabels.md)**

:   ZeroMatch 提出两阶段框架将基础模型的零样本伪标签与半监督学习相结合：先用知识蒸馏初始化学生模型，再以辅助 KD loss 防止灾难性遗忘的方式执行 SSL 训练，在 6 个视觉/NLP 基准上一致超越标准 SSL 和零样本增强方法。

**[Exact Expressive Power of Transformers with Padding](exact_expressive_power_of_transformers_with_padding.md)**

:   本文精确刻画了带 padding 的 Transformer 的表达能力：固定深度 + 多项式 padding 恰好等于 $\mathsf{FO}$-uniform $\mathsf{TC}^0$，进一步结合 $O(\log^d n)$ looping 恰好等于 $\mathsf{FO}$-uniform $\mathsf{TC}^d$，polylog looping 收敛到 $\mathsf{NC}$，为 padding/looping 作为可并行推理时计算提供了完整理论基础。

**[ExPO: Unlocking Hard Reasoning with Self-Explanation-Guided Reinforcement Learning](expo_unlocking_hard_reasoning_with_self-explanation-guided_reinforcement_learnin.md)**

:   提出 Self-Explanation Policy Optimization (ExPO)，一种通过让模型在给定正确答案条件下自主生成推理链（self-explanation）作为正样本的模块化框架，解决 GRPO 等 RL 后训练方法在困难推理任务上因缺乏有效正样本而无法学习（分布锐化）的根本问题——ExPO 生成的自解释样本既在当前策略分布内（in-distribution），又能提供正向学习信号，可无缝集成到 DPO 和 GRPO 中。

**[Eyes Wide Open: Ego Proactive Video-LLM for Streaming Video](eyes_wide_open_ego_proactive_videollm_for_streaming_video.md)**

:   定义"第一视角流式视频主动理解"新任务——给定ego-streaming视频，AI助手在恰当时机主动回答多样化、随事件演变的问题，同时保持感知与推理的同步。提出ESTP-Bench评估框架、ESTP-F1指标，以及含数据引擎、多阶段训练和主动动态压缩的完整技术pipeline（VideoLLM-EyeWO），在ESTP-Bench上比最强baseline MiniCPM-V高11.8%。

**[FALQON: Accelerating LoRA Fine-tuning with Low-Bit Floating-Point Arithmetic](falqon_accelerating_lora_fine-tuning_with_low-bit_floating-point_arithmetic.md)**

:   FALQON 通过将 LoRA 适配器直接融合 (meld) 到 FP8 量化的骨干权重中，消除了单独 LoRA 路径引入的小矩阵量化开销，结合高效梯度计算和行级代理更新机制，实现了相比现有量化 LoRA 方法约 3 倍的训练加速。

**[Fantastic Features and Where to Find Them: A Probing Method to Combine Features from Multiple Foundation Models](fantastic_features_and_where_to_find_them_a_probing_method_to_combine_features_f.md)**

:   提出 ComBo，一种基于 probing 的轻量级 adapter，通过仿射投影压缩多个冻结基础模型多层激活，再用小型 transformer 融合，无需反向传播即可高效整合多模型互补表征，在 VTAB-1k 上超越先前 probing 方法并匹配蒸馏方法。

**[FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed](fastdinov2_frequency_based_curriculum_learning_improves_robustness_and_training_.md)**

:   提出 FastDINOv2，一种两阶段频率课程学习策略：先用低分辨率图像训练 75% epochs 学习低频特征以加速收敛，再用全分辨率+高斯噪声 patching 训练 25% epochs 平衡频率偏置，实现 1.6× 加速、2.25× FLOPs 节省，同时增强鲁棒性。

**[FastLongSpeech: Enhancing Large Speech-Language Models for Efficient Long-Speech Processing](fastlongspeech_enhancing_large_speech-language_models_for_efficient_long-speech_.md)**

:   提出 FastLongSpeech，通过迭代融合策略压缩冗余语音表征和动态压缩训练转移短语音能力到长语音场景，使 LSLM 无需长语音训练数据即可高效处理长语音，在长语音 QA 上实现最优性能且推理效率提升 70%。

**[FiRA: Can We Achieve Full-Rank Training of LLMs Under Low-Rank Constraint?](fira_can_we_achieve_full-rank_training_of_llms_under_low-rank_constraint.md)**

:   提出 Fira，首个在低秩约束下实现全秩训练（全秩梯度+全秩权重）的 LLM 训练框架，通过观察到低秩与全秩训练中优化器的缩放因子高度相似，用低秩缩放因子近似校正子空间外梯度，配合 norm-growth limiter 防止 loss spike，在预训练和微调中均超越 LoRA 和 GaLore。

**[FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts](flylora_boosting_task_decoupling_and_parameter_efficiency_via_implicit_rank-wise.md)**

:   FlyLoRA 受飞蝇嗅觉回路启发，将 LoRA 的下投影矩阵 $A$ 替换为冻结的稀疏随机投影，通过 top-$k$ 激活值选择实现隐式 rank-wise MoE 路由，在消除路由参数的同时减少任务内干扰，并利用随机投影的近正交性天然支持多任务模型合并。

**[Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models](gated_integration_of_low-rank_adaptation_for_continual_learning_of_large_languag.md)**

:   提出 GainLoRA，为持续学习中每个新任务的 LoRA 分支引入**门控模块**生成自适应集成系数，通过正交约束使新分支对旧任务的输出趋近于零，从而有效缓解灾难性遗忘。

**[Geometric Data Valuation via Leverage Scores](geometric_data_valuation_via_leverage_scores.md)**

:   提出基于**统计杠杆分数（leverage scores）**的几何数据估值方法，作为 Data Shapley 值的高效代理，满足对称性、效率性和虚拟玩家等公理，并通过 ridge leverage 扩展解决维度饱和问题，提供 $O(\varepsilon)$ 近似最优的理论保证。

**[GoRA: Gradient-Driven Adaptive Low Rank Adaptation](gora_gradient-driven_adaptive_low_rank_adaptation.md)**

:   提出 GoRA，利用**预计算梯度信息**在训练前同时完成自适应秩分配和权重初始化——基于参数敏感度分配各层 rank，用梯度伪逆初始化 $B$ 矩阵使初始输出近似一步梯度下降，统一解决 LoRA 的两大瓶颈。

**[Graph Your Own Prompt](graph_your_own_prompt.md)**

:   提出图一致性正则化（GCR）框架，通过在网络任意深度插入无参数的图一致性层（GCL），将中间特征的关系图与基于预测的类感知语义图对齐，以自我提示的方式促进语义一致的特征学习，在不修改架构和不增加参数的前提下提升分类泛化性能。

**[GraphKeeper: Graph Domain-Incremental Learning via Knowledge Disentanglement and Preservation](graphkeeper_graph_domain-incremental_learning_via_knowledge_disentanglement_and_.md)**

:   提出 GraphKeeper 框架应对**图域增量学习（Graph Domain-IL）**中的灾难性遗忘，通过域特异性 LoRA 参数隔离 + 领域内/间解耦 + 基于岭回归的无偏差知识保存三组件，比次优方法提升 6.5%-16.6%，且可无缝集成图基础模型。

**[GraSS: Scalable Data Attribution with Gradient Sparsification and Sparse Projection](grass_scalable_data_attribution_with_gradient_sparsification_and_sparse_projecti.md)**

:   提出 GraSS 与 FactGraSS 两阶段梯度压缩算法，利用逐样本梯度的固有稀疏性实现**亚线性**时间与空间复杂度（$O(k')$），在十亿参数模型上比 SOTA 基线 LoGra 快 **165%**，同时保持数据归因质量。

**[Graver: Generative Graph Vocabularies for Robust Graph Foundation Models Fine-tuning](graver_generative_graph_vocabularies_for_robust_graph_foundation_models_fine-tun.md)**

:   提出 Graver 框架，通过 ego-graph 解耦提取可迁移子图词汇、graphon 专家建模词汇分布、MoE-CoE 路由选择性增强 support 样本，解决 GFM 少样本微调中因结构不匹配导致的不稳定性问题。

**[H-SPLID: HSIC-based Saliency Preserving Latent Information Decomposition](h-splid_hsic-based_saliency_preserving_latent_information_decomposition.md)**

:   提出 H-SPLID，通过将隐空间显式分解为**显著（任务相关）**和**非显著（任务无关）**两个子空间，结合 HSIC 正则化实现信息压缩，证明预测偏差上界受显著子空间维度和 HSIC 控制，在无对抗训练条件下显著提升对非显著区域扰动的鲁棒性。

**[Hankel Singular Value Regularization for Highly Compressible State Space Models](hankel_singular_value_regularization_for_highly_compressible_state_space_models.md)**

:   通过在训练中正则化 SSM 层的 **Hankel 奇异值核范数**促使其快速衰减，使训练后模型可用平衡截断压缩至原始阶数的 **10%** 而保持精度，并利用旋转矩阵块对角参数化将 Gramian 计算从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(n^2)$。

**[Heterogeneous Adversarial Play in Interactive Environments](heterogeneous_adversarial_play_in_interactive_environments.md)**

:   提出 **HAP（Heterogeneous Adversarial Play）**，将教师-学生交互形式化为极小极大博弈：教师网络自动生成针对学生弱点的挑战任务，学生策略不断适应进化，形成无需手工设计的自适应课程——在多任务 RL 环境中超越 SOTA 基线，且生成的课程对人类学习者同样有效。

**[Homogeneous Keys, Heterogeneous Values: Exploiting Local KV Cache Asymmetry for Long-Context LLMs](homogeneous_keys_heterogeneous_values_exploiting_local_kv_cache_asymmetry_for_lo.md)**

:   发现 LLM 注意力机制中一个被忽视的**局部 Key-Value 不对称性**——相邻 Key 具有同质性（相似注意力权重），而相邻 Value 呈异质分布——据此提出 **AsymKV** 无训练压缩框架：基于同质性合并 Key + 基于基数归一化的**无损** Value 表示，在 LongBench 上超越 H2O 达 **5 分**。

**[Hyperbolic Dataset Distillation](hyperbolic_dataset_distillation.md)**

:   提出 HDD 方法，首次将双曲空间引入数据集蒸馏，通过在 Lorentz 双曲空间中匹配原始和合成数据的 Riemannian 质心来替代欧氏空间的分布匹配，利用双曲几何的层级加权特性让"更具代表性"的底层样本获得更高权重，在多个数据集上持续提升 DM/IDM 基线准确率。

**[Hyperbolic Fine-Tuning for Large Language Models](hyperbolic_fine-tuning_for_large_language_models.md)**

:   发现 LLM token 嵌入具有幂律分布和树状双曲结构，据此提出 HypLoRA——在 Lorentz 双曲流形上直接执行低秩适配（避免切空间映射的相消效应），在算术推理和常识推理任务上相比标准 LoRA 取得显著提升（如 Qwen2.5-7B 上 M.AVG +7.5%）。

**[Infrequent Exploration in Linear Bandits](infrequent_exploration_in_linear_bandits.md)**

:   提出 INFEX 框架，按给定调度表在探索步执行基线算法（如 LinUCB/LinTS）、其余时刻贪心选臂，证明只要探索次数超过 $\omega(\log T)$ 即可达到与全时刻探索相同的多项对数 regret，同时大幅降低计算开销（80%-99% 时间步为贪心）。

**[Jet-Nemotron: Efficient Language Model with Post Neural Architecture Search](jet-nemotron_efficient_language_model_with_post_neural_architecture_search.md)**

:   NVIDIA 提出 PostNAS 流水线——从预训练全注意力模型出发，冻结 MLP 权重，通过四步搜索（全注意力层放置→线性注意力块选择→新注意力块 JetBlock 设计→硬件感知超参搜索）得到混合架构 Jet-Nemotron，2B 模型在 MMLU-Pro 上超越 Qwen3-1.7B 同时生成吞吐提升 47×。

**[KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments](keydiff_key_similarity-based_kv_cache_eviction_for_long-context_llm_inference_in.md)**

:   提出 KeyDiff——一种无需注意力分数的 KV cache 驱逐策略，通过保留与其他 key 余弦相似度最低（即几何上最独特）的 key 来维护 cache，在严格内存约束的逐块推理场景下以 8K cache 在 LongBench 上仅损失 ≤0.04% 精度，同时端到端推理延迟减少最高 30%。

**[KINDLE: Knowledge-Guided Distillation for Prior-Free Gene Regulatory Network Inference](kindle_knowledge-guided_distillation_for_prior-free_gene_regulatory_network_infe.md)**

:   提出 KINDLE 三阶段框架，通过知识蒸馏将先验引导的教师模型中学到的基因调控知识迁移到无先验的学生模型，在不依赖任何外部先验知识的情况下实现了基因调控网络（GRN）推断的 SOTA 性能。

**[Knowing When to Stop: Efficient Context Processing via Latent Sufficiency Signals](knowing_when_to_stop_efficient_context_processing_via_latent_sufficiency_signals.md)**

:   本文提出 dynamic context cutoff，通过探测 Transformer 特定注意力头中编码的"信息充分性信号"，训练轻量分类器判断模型何时已获取足够上下文，实现提前终止处理，在6个QA数据集上平均提高3.4%准确率同时减少1.33×token消耗。

**[KTAE: A Model-Free Algorithm to Key-Tokens Advantage Estimation in Mathematical Reasoning](ktae_a_model-free_algorithm_to_key-tokens_advantage_estimation_in_mathematical_r.md)**

:   KTAE 提出了一种不依赖额外模型的 token 级优势估计算法，通过 Fisher 精确检验和信息增益量化每个 token 与正确推理结果的统计关联，将细粒度 token 重要性叠加到 GRPO/DAPO 的 rollout 级优势上，在5个数学推理基准上超越基线并显著缩短生成长度。

**[Latent Principle Discovery for Language Model Self-Improvement](latent_principle_discovery_for_language_model_self-improvement.md)**

:   STaPLe 提出后验正则化的蒙特卡洛 EM 算法，让 7-8B 小模型自行发现指导自我修正的"原则"（latent principle），通过迭代发现-学习循环实现自我改进，在 AlpacaEval 上提升 8-10% 胜率、MT-Bench 平均提升 +0.3，并可通过聚类压缩至可解释的 constitution。

**[LayerIF: Estimating Layer Quality for Large Language Models using Influence Functions](layerif_estimating_layer_quality_for_large_language_models_using_influence_funct.md)**

:   LayerIF 提出用影响函数（Influence Functions）逐层量化 LLM 的训练质量，通过聚合各层的正向影响分数得到数据驱动的层重要性估计，并将其应用于 LoRA-MoE 专家分配和层级稀疏剪枝两个下游任务，在 Mistral-7B 和 Gemma-7B 上分别获得 1.61% 和 0.90% 的准确率提升。

**[Learning Grouped Lattice Vector Quantizers for Low-Bit LLM Compression](learning_grouped_lattice_vector_quantizers_for_low-bit_llm_compression.md)**

:   GLVQ 提出为 LLM 权重的每个分组学习专属的格（lattice）码本（由可学习生成矩阵定义），配合分组特异的 μ-law companding 变换适应重尾分布，在 2-bit 量化下 Llama-2-70B 的 Wikitext-2 困惑度达到 3.36，大幅领先 QuIP#（3.91）和 QTIP（3.78）。

**[Learning Task-Agnostic Representations Through Multi-Teacher Distillation](learning_task-agnostic_representations_through_multi-teacher_distillation.md)**

:   提出基于互信息最大化的任务无关多教师蒸馏框架，通过高斯核估计教师嵌入的条件分布来训练学生模型，使其在不依赖任何下游任务标签的情况下学到高信息密度的通用表示，在文本、视觉和分子建模三个领域均取得了同体量最优性能。

**[Linear Attention for Efficient Bidirectional Sequence Modeling](linear_attention_for_efficient_bidirectional_sequence_modeling.md)**

:   提出 Lion 框架，首次系统地将线性 Transformer 扩展到双向序列建模，统一了全线性注意力、双向 RNN 和分块并行三种等价表示，在图像分类和 MLM 任务上训练速度比 SSM 快达 10 倍且性能可比 softmax Transformer。

**[Multi-Task Vehicle Routing Solver Via Mixture Of Specialized Experts Under State](multi-task_vehicle_routing_solver_via_mixture_of_specialized_experts_under_state.md)**

:   提出 **State-Decomposable MDP (SDMDP)** 框架将多种 VRP 变体重新表述为基础状态空间的笛卡尔积，再通过 **Mixture-of-Specialized-Experts Solver (MoSES)** 用专用 LoRA 专家实现基础策略的潜在空间复用，高效处理 16 种 VRP 变体。

**[Rccda Adaptive Model Updates In The Presence Of Concept Drift Under A Constraine](rccda_adaptive_model_updates_in_the_presence_of_concept_drift_under_a_constraine.md)**

:   提出 RCCDA，一种基于 Lyapunov 漂移惩罚框架的轻量级模型更新策略，在数据分布随时间漂移（concept drift）场景下，仅利用历史推理损失信息和可调阈值，就能贪心最优地决定何时重训模型，同时可证明地满足严格资源预算约束。

**[RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models](reflora_refactored_low-rank_adaptation_for_efficient_fine-tuning_of_large_models.md)**

:   RefLoRA 通过在每次迭代中选择最优的低秩分解形式（最小化损失上界），解决了 LoRA 因分解不唯一性导致的权重更新不一致和不平衡问题，在几乎不增加计算开销的前提下加速收敛并提升微调性能。

**[Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA](robust_federated_finetuning_of_llms_via_alternating_optimization_of_lora.md)**

:   提出 RoLoRA，通过交替优化 LoRA 的 down-projection (A) 和 up-projection (B) 矩阵，解决联邦学习中 LoRA 聚合不精确和表达力受限的问题，在 RoBERTa-Large 和 Llama-2-7B 上显著优于 FedAVG of LoRA 和 FFA-LoRA。

**[SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism](shap_meets_tensor_networks_provably_tractable_explanations_with_parallelism.md)**

:   本文首次为张量网络（Tensor Networks）提供可证明精确的 SHAP 解释计算框架，证明张量列车（Tensor Train）结构下 SHAP 可在多对数时间内并行计算（NC² 复杂度），并通过归约揭示二值化神经网络中**宽度而非深度**才是 SHAP 计算的核心瓶颈。

**[The Graphon Limit Hypothesis: Understanding Neural Network Pruning via Infinite Width Analysis](the_graphon_limit_hypothesis_understanding_neural_network_pruning_via_infinite_w.md)**

:   提出"Graphon极限假说"：当网络宽度趋于无穷时，不同剪枝方法产生的二值掩码序列在cut距离下收敛到各自独特的graphon极限，并在此基础上推导出Graphon NTK来分析稀疏网络训练动态，从理论层面解释了为什么不同剪枝方法在相同稀疏度下表现迥异。

**[Tighter CMI-Based Generalization Bounds via Stochastic Projection and Quantization](tighter_cmi-based_generalization_bounds_via_stochastic_projection_and_quantizati.md)**

:   通过在 CMI（条件互信息）框架中引入**随机投影**和**有损压缩**，推导出更紧的泛化界，解决了经典 CMI 界在 SCO 反例上失效的问题，并证明记忆化对良好泛化并非必要。
