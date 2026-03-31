<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🧠 NeurIPS2025** · 共 **36** 篇

**[A Little Depth Goes a Long Way: The Expressive Power of Log-Depth Transformers](a_little_depth_goes_a_long_way_the_expressive_power_of_logde.md)**

:   本文证明了将 Transformer 的深度从常数增长到 Θ(log n) 就能解锁识别正则语言和图连通性这两类固定深度 Transformer 无法表达的问题，且深度扩展比宽度（需超多项式增长）和 CoT 步数（需超对数增长）都更高效。

**[AdaVideoRAG: Omni-Contextual Adaptive Retrieval-Augmented Efficient Long Video Understanding](adavideorag_omnicontextual_adaptive_retrievalaugmented_effic.md)**

:   提出 AdaVideoRAG，通过轻量级意图分类器将查询按难度路由到三级检索路径（无检索/朴素检索/图检索），结合全知识索引模块（caption+ASR+OCR+视觉+知识图谱）实现长视频理解的效率-精度最优平衡，在 MLVU 上为 Qwen2.5-VL-7B 带来 39.8% 提升。

**[Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](adversarial_locomotion_and_motion_imitation_for_humanoid_policy_learning.md)**

:   ALMI提出上下半身对抗训练框架：下半身策略在上半身动作干扰下学习鲁棒运动，上半身策略在下半身运动干扰下学习精确动作模仿，通过迭代对抗训练收敛到Nash均衡，实现Unitree H1-2真实机器人的稳定全身协调控制。

**[Agentic Persona Control and Task State Tracking for Realistic User Simulation](agentic_persona_control_and_task_state_tracking_for_realistic_user_simulation_in.md)**

:   提出三 agent 协作框架用于逼真的用户模拟——User Agent（协调）+ State Tracking Agent（结构化任务状态）+ Message Attributes Generation Agent（基于 persona 和状态的行为属性控制），在餐厅点餐场景中综合仿真质量（CRRS）提升 102.6%，persona 保持度 +19.9%，行为自然度 +284.5%，且核心发现：无状态感知的行为控制导致 BVS=0（完全刚性）。

**[CleverBirds: A Multiple-Choice Benchmark for Fine-grained Human Knowledge Tracing](cleverbirds_a_multiple-choice_benchmark_for_fine-grained_human_knowledge_tracing.md)**

:   发布 CleverBirds——超大规模细粒度视觉知识追踪基准，包含 4万+用户的 1700万+多选题交互（覆盖 10000+鸟类物种），展示了追踪细粒度视觉专家技能发展的挑战性，为 KT 方法提供了前所未有的视觉领域评测平台。

**[Cloud4D: Estimating Cloud Properties at a High Spatial and Temporal Resolution](cloud4d_estimating_cloud_properties_at_a_high_spatial_and_temporal_resolution.md)**

:   首个基于地面多视角相机的学习框架，通过单应性引导的2D-to-3D Transformer重建四维（3D空间+时间）云液态水含量分布，在25m空间/5s时间分辨率下实现了相对雷达<10%的误差，比卫星观测提升了一个数量级的时空分辨率。

**[ConViS-Bench: Estimating Video Similarity Through Semantic Concepts](convis-bench_estimating_video_similarity_through_semantic_concepts.md)**

:   提出基于语义概念的视频相似度估计任务 ConViS 及配套 benchmark ConViS-Bench（610对视频、16领域、5概念），系统评测了10+主流模型在概念条件下的视频比较能力，揭示当前模型在时序结构和空间语境理解上的显著短板。

**[Deceptron Learned Local Inverses For Fast And Stable Physics Inversion](deceptron_learned_local_inverses_for_fast_and_stable_physics_inversion.md)**

:   提出 Deceptron 双向模块，通过学习可微分前向代理的局部逆映射并引入 Jacobian Composition Penalty (JCP)，在求解物理逆问题时将输出空间的残差拉回输入空间，实现类 Gauss-Newton 的预条件梯度更新，迭代次数大幅减少（Heat-1D 约 20 倍加速）。

**[DeltaProduct: Improving State-Tracking in Linear RNNs via Householder Products](deltaproduct_improving_state-tracking_in_linear_rnns_via_householder_products.md)**

:   提出 DeltaProduct，通过将 DeltaNet 的单步梯度下降扩展至每个 token 的多步梯度下降，使状态转移矩阵成为 $n_h$ 个广义 Householder 变换的乘积，实现了表达力与效率之间的可调平衡，显著提升了状态跟踪能力和长度外推性能。

**[Dense SAE Latents Are Features, Not Bugs](dense_sae_latents_are_features_not_bugs.md)**

:   本文系统研究了稀疏自编码器(SAE)中频繁激活的"dense latents"，证明它们不是训练噪声，而是语言模型残差流中固有的密集子空间的反映，并提出了一套包含位置追踪、上下文绑定、零空间、字母、词性和PCA等六类dense latent的分类体系。

**[DSAS: A Universal Plug-and-Play Framework for Attention Optimization in Multi-Document Question Answering](dsas_a_universal_plug-and-play_framework_for_attention_optimization_in_multi-doc.md)**

:   提出Dual-Stage Adaptive Sharpening (DSAS)，一个无需训练的即插即用注意力优化框架，通过Contextual Gate Weighting (CGW)增强关键段落对问题和目标位置的注意力、通过Reciprocal Attention Suppression (RAS)抑制关键与无关段落间的信息交换，在多文档QA上平均F1提升达4.2%。

**[egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-World Tasks](egoemotion_egocentric_vision_and_physiological_signals_for_emotion_and_personali.md)**

:   提出egoEMOTION——首个结合第一人称视觉（Meta Project Aria眼镜）与生理信号的情感与人格识别数据集，涵盖43名被试、50+小时录制、16种任务，发现第一人称视觉信号（尤其眼动特征）在真实场景情感预测中优于传统生理信号。

**[Empower Words: DualGround for Structured Phrase and Sentence-Level Temporal Grounding](empower_words_dualground_for_structured_phrase_and_sentencel.md)**

:   论文指出现有视频时序定位模型在跨模态注意力中往往过度依赖句末 [EOS] token 的全局语义、忽视词级局部信号，提出 DualGround 双分支架构，将句子级全局语义与短语级局部语义显式解耦建模，在 QVHighlights 和 Charades-STA 上实现 Moment Retrieval 与 Highlight Detection 的 SOTA。

**[Enhancing Temporal Understanding in Video-LLMs through Stacked Temporal Attention in Vision Encoders](enhancing_temporal_understanding_in_videollms_through_stacke.md)**

:   提出 STAVEQ2，在 Vision Encoder 中堆叠参数高效的时序注意力模块（STA），解决现有 Video-LLM 在细粒度时序理解（如区分"从左到右拉"和"从右到左拉"）上的根本性架构缺陷，在 VITATECS/MVBench/Video-MME 上提升最高 5.5%。

**[FastVID: Dynamic Density Pruning for Fast Video Large Language Models](fastvid_dynamic_density_pruning_for_fast_video_large_languag.md)**

:   提出 FastVID，通过动态时序分割 (DySeg) + 密度空时剪枝 (STPrune) 从时间和视觉两个维度系统性消除视频 token 冗余，在 LLaVA-OneVision-7B 上剪掉 90.3% 视频 token 后仍保留 98% 精度，LLM prefill 阶段加速 7.1×。

**[Fixed-Point RNNs: Interpolating from Diagonal to Dense](fixed-point_rnns_interpolating_from_diagonal_to_dense.md)**

:   提出 Fixed-Point RNN 框架，将稠密线性 RNN 参数化为对角线性 RNN 的不动点，通过迭代次数在对角（高效）与稠密（表达力强）之间动态插值，首次在状态跟踪（$A_5$/$S_5$）和拷贝任务上同时取得最优结果。

**[Force Prompting: Video Generation Models Can Learn and Generalize Physics-based Control Signals](force_prompting_video_generation_models_can_learn_and_generalize_physics-based_c.md)**

:   提出Force Prompting，将物理力（局部点力和全局风力）作为视频生成模型的控制信号，仅用~15K合成训练视频（Blender旗帜和滚球）和单日4xA100训练，即可在多样真实场景图像上展现跨物体/材质/几何的惊人泛化，包括初步的质量理解能力。

**[Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation](foresight_adaptive_layer_reuse_for_accelerated_and_highquali.md)**

:   提出 Foresight，一种训练无关的自适应层复用框架，通过动态 MSE 阈值决策在 DiT 去噪过程中哪些层可复用缓存、哪些需重新计算，在 OpenSora/Latte/CogVideoX 上实现最高 1.63× 端到端加速且保持视频质量。

**[GeoDynamics: A Geometric State-Space Neural Network for Understanding Brain Dynamics on Riemannian Manifolds](geodynamics_a_geometric_state-space_neural_network_for_understanding_brain_dynam.md)**

:   提出GeoDynamics，将经典状态空间模型(SSM)从欧几里得空间推广到对称正定(SPD)流形，通过加权Frechet均值聚合和正交群平移实现流形上的状态演化，在脑连接组（AD/PD/ASD早期诊断）和人体动作识别上均取得SOTA。

**[Grounding Foundational Vision Models with 3D Human Poses for Robust Action Recognition](grounding_foundational_vision_models_with_3d_human_poses_for_robust_action_recog.md)**

:   提出一种融合 V-JEPA 2 视觉上下文特征与 CoMotion 3D 骨骼姿态数据的 cross-attention 多模态架构，在标准及高遮挡动作识别基准上优于单模态基线。

**[In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting](in_the_eye_of_mllm_benchmarking_egocentric_video_intent_understanding_with_gaze-.md)**

:   提出 EgoGazeVQA——首个利用注视（gaze）信号评估 MLLM 对第一人称视频中用户意图理解能力的基准，并设计三种 gaze-guided prompting 策略显著提升模型表现。

**[InFlux: A Benchmark for Self-Calibration of Dynamic Intrinsics of Video Cameras](influx_a_benchmark_for_self-calibration_of_dynamic_intrinsics_of_video_cameras.md)**

:   提出首个包含逐帧动态相机内参真值的真实视频基准 InFlux（386 视频、143K+ 标注帧），通过镜头元数据到内参的查找表（LUT）实现精确标注，并揭示现有内参预测方法在动态内参场景下表现不佳。

**[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](kungfubot_physics-based_humanoid_whole-body_control_for_learning_highly-dynamic_.md)**

:   提出 PBHC 框架，通过物理感知运动处理流水线和自适应跟踪因子的双层优化，使人形机器人（Unitree G1）学会功夫、舞蹈等高动态全身动作，跟踪误差显著优于现有方法并成功实机部署。

**[Lattice Boltzmann Model for Learning Real-World Pixel Dynamicity](lattice_boltzmann_model_for_learning_real-world_pixel_dynamicity.md)**

:   受流体力学中格子玻尔兹曼方法启发，提出 LBM（Lattice Boltzmann Model）用于在线实时像素跟踪，将视频像素建模为流体格子并通过碰撞-流式过程求解运动状态，以 18M 参数实现 SOTA 在线跟踪性能且可在边缘设备上实时运行。

**[LeMiCa: Lexicographic Minimax Path Caching for Efficient Diffusion-Based Video Generation](lemica_lexicographic_minimax_path_caching_for_efficient_diffusion-based_video_ge.md)**

:   提出 LeMiCa，一种免训练的扩散视频生成加速框架，将缓存调度建模为有向无环图上的字典序极小极大路径优化问题，通过全局误差控制实现速度和质量的双重提升（Latte 上 2.9× 加速，Open-Sora 上 LPIPS 低至 0.05）。

**[Less Is More But Where Dynamic Token Compression Via Llm-Guided Keyframe Prior](less_is_more_but_where_dynamic_token_compression_via_llm-guided_keyframe_prior.md)**

:   提出 DyToK，一种无需训练的视频 token 动态压缩方法，利用 VLLM 深层注意力中固有的 query 条件关键帧先验，为不同帧自适应分配 token 预算，实现即插即用式的效率-精度最优权衡。

**[Less is More: Local Intrinsic Dimensions of Contextual Language Models](less_is_more_local_intrinsic_dimensions_of_contextual_language_models.md)**

:   提出利用上下文 token 嵌入的局部内在维度（Local Intrinsic Dimension, LID）来无监督监测 LLM 训练动态——维度下降预示泛化改善，维度上升预示过拟合——在对话状态跟踪、grokking、情感识别等任务上验证了这一几何信号的实用性。

**[LiveStar: Live Streaming Assistant for Real-World Online Video Understanding](livestar_live_streaming_assistant_for_real-world_online_video_understanding.md)**

:   提出 LiveStar，一个始终在线的直播流视频理解助手，通过 Streaming Causal Attention Masks (SCAM) 训练策略和 Streaming Verification Decoding (SVeD) 推理框架，实现自适应响应时机判断，在 OmniStar 基准上语义正确性提升 19.5%，时间偏差降低 18.1%。

**[Neural Stochastic Flows: Solver-Free Modelling and Inference for SDE Solutions](neural_stochastic_flows_solver-free_modelling_and_inference_for_sde_solutions.md)**

:   提出 Neural Stochastic Flows（NSF），通过条件归一化流直接学习 SDE 的转移分布 $p(x_t \mid x_s)$，在架构上约束满足随机流性质（恒等、Markov、Chapman-Kolmogorov），实现了无需数值求解器的单步采样，在远距时间点上加速高达两个数量级。

**[Open-World Drone Active Tracking with Goal-Centered Rewards](open-world_drone_active_tracking_with_goal-centered_rewards.md)**

:   提出首个开放世界无人机主动跟踪基准 DAT（24 个城市级场景、高保真动力学仿真），以及基于目标中心奖励函数和课程学习的强化学习跟踪方法 GC-VAT，在仿真器上达到约 72% 的跟踪成功率。

**[Revisiting Bi-Linear State Transitions in Recurrent Neural Networks](revisiting_bi-linear_state_transitions_in_recurrent_neural_networks.md)**

:   系统性地重新审视 RNN 中的双线性状态转移（隐状态与输入的乘法交互），理论证明双线性 RNN 可模拟任意有限状态机，并展示其在去除加性项后形成了一个从对角到全结构的自然表达力层次，揭示了 Mamba 等流行线性 RNN 处于该层次最低端。

**[Structured Sparse Transition Matrices To Enable State Tracking In State-Space Mo](structured_sparse_transition_matrices_to_enable_state_tracking_in_state-space_mo.md)**

**[TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs](tempsampr1_effective_temporal_sampling_with_reinforcement_fi.md)**

:   提出 TempSamp-R1，针对视频时序定位任务改进 GRPO 强化微调框架，通过 off-policy 时间精确引导 + 非线性软优势计算 + 混合 CoT 训练，在 Charades-STA/ActivityNet/QVHighlights 上分别提升 +2.7%/+5.3%/+3.0%。

**[Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task](toolaugmented_spatiotemporal_reasoning_for_streamlining_vide.md)**

:   论文为复杂 VideoQA 提出一套轻量但可扩展的 Video Toolkit，并设计 STAR（Spatiotemporal Reasoning Framework）来调度时间工具与空间工具的调用顺序，逐步定位视频关键区域，显著增强 GPT-4o 的时空推理能力，在 VideoMME 上提升 8.2%，在 LongVideoBench 上提升 4.6%。

**[Two Causally Related Needles in a Video Haystack](two_causally_related_needles_in_a_video_haystack.md)**

:   提出CAUSAL2NEEDLES benchmark评估VLM的长视频双针(2-needle)因果推理能力：需要从视频两个不同位置提取因果关联的事件信息并联合推理，利用"桥接实体"迫使模型先理解结果再追溯原因，揭示即使GPT-4o在2-needle因果问题上仅达13.4%的Both准确率（vs人类79.3%）。

**[VMDT: Decoding the Trustworthiness of Video Foundation Models](vmdt_decoding_the_trustworthiness_of_video_foundation_models.md)**

:   提出 VMDT（Video-Modal DecodingTrust），首个统一评估 T2V 和 V2T 视频基础模型在安全、幻觉、公平、隐私和对抗鲁棒性五个维度上可信度的基准平台，涵盖 7 个 T2V 和 19 个 V2T 模型的大规模评测，揭示了模型规模与可信度之间的复杂关系。
