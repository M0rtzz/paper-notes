---
title: >-
  AAAI2026 视频理解方向 37篇论文解读
description: >-
  37篇AAAI2026 视频理解方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🤖 AAAI2026** · 共 **37** 篇

**[3D4D An Interactive Editable 4D World Model Via 3D Video Generation](3d4d_an_interactive_editable_4d_world_model_via_3d_video_generation.md)**

:   提出 3D4D，一个集成 WebGL 和 Supersplat 渲染的交互式 4D 可视化框架，通过四个后端模块（3D重建、图像生视频、视频分帧、4D场景生成）将静态图片和文本转化为可实时交互的 4D 场景，并引入 VLM 引导的注视点渲染策略在保持语义一致性的同时实现 60fps 实时交互。

**[Apvr Hour-Level Long Video Understanding With Adaptive Pivot](apvr_hour-level_long_video_understanding_with_adaptive_pivot.md)**

:   提出APVR，一个训练免费的双粒度视觉信息检索框架：帧级别通过查询扩展+时空语义置信度打分迭代检索关键帧（最多1024帧），token级别通过查询感知的注意力驱动选择压缩视觉token，突破内存墙限制处理小时级长视频，在LongVideoBench/VideoMME/MLVU上分别提升最高9.5%/4.6%/9.7%。

**[Balancing Multimodal Domain Generalization Via Gradient Modulation And Projectio](balancing_multimodal_domain_generalization_via_gradient_modulation_and_projectio.md)**

:   提出 Gradient Modulation Projection (GMP) 策略，通过解耦分类与域不变梯度的调制（IGDM）以及冲突自适应梯度投影（CAGP），解决多模态域泛化中模态间优化不平衡和任务间梯度冲突问题，在多个基准上达到 SOTA。

**[Bat Learning Event-Based Optical Flow With Bidirectional Adaptive Temporal Corre](bat_learning_event-based_optical_flow_with_bidirectional_adaptive_temporal_corre.md)**

:   提出双向自适应时序相关性（BAT）框架，将事件相机的时序密集运动线索转化为空间密集线索，实现高精度事件光流估计，在 DSEC-Flow 基准上排名第一。

**[Causality Matters How Temporal Information Emerges In Video Language Models](causality_matters_how_temporal_information_emerges_in_video_language_models.md)**

:   通过系统性消融实验揭示VideoLM的时序理解能力并非来源于位置编码(PE)，而是由因果注意力掩码的序列敏感性产生——时序信息沿"帧间交互→末帧聚合→query融合"的因果路径逐层构建，并据此提出两种无损推理加速策略。

**[Coordinated Humanoid Robot Locomotion With Symmetry Equivariant Reinforcement Le](coordinated_humanoid_robot_locomotion_with_symmetry_equivariant_reinforcement_le.md)**

:   提出 SE-Policy，将严格的对称等变性（actor）和对称不变性（critic）直接嵌入神经网络架构，无需额外超参数即可使人形机器人产生时空协调的自然运动，速度跟踪误差相比 DreamWaQ 降低 40%，并成功部署到 Unitree G1 实体机器人。

**[Decomposition And Preprocessing Of Ternary Constraint Networks](decomposition_and_preprocessing_of_ternary_constraint_networks.md)**

:   提出将任意离散约束网络形式化分解为三元约束网络(TCN)的完整理论框架，并通过七项预处理技术（传播、代数简化、公共子表达式消除等）将分解引入的变量/约束膨胀从中位数8x/6x降至4.8x/4.3x，为GPU硬件上的高效约束求解提供规则化数据布局。

**[Distillation Dynamics Towards Understanding Feature-Based Di](distillation_dynamics_towards_understanding_feature-based_di.md)**

:   提出"蒸馏动力学"分析框架（频谱分析+信息熵+激活幅值），揭示ViT具有独特的U型信息处理模式（先压缩后扩展），证明feature-based蒸馏在ViT中失败的根本原因是teacher后层的分布式高维编码范式与student有限通道容量之间的表征范式不匹配，而非简单的容量差距。

**[Dreamrunner Fine-Grained Compositional Story-To-Video Genera](dreamrunner_fine-grained_compositional_story-to-video_genera.md)**

:   提出 DreamRunner 框架，通过 LLM 双层规划 + 检索增强运动先验学习 + 时空区域3D注意力模块(SR3AI)，实现细粒度可控的多角色多事件故事视频生成。

**[Emovid A Multimodal Emotion Video Dataset For Emotion-Centric Video Understandin](emovid_a_multimodal_emotion_video_dataset_for_emotion-centric_video_understandin.md)**

:   提出 EmoVid，首个面向艺术化/非写实内容的大规模多模态情绪视频数据集（22,758 个视频片段），覆盖动画、电影和表情贴纸三种类型，并通过微调 Wan2.1 模型展示了情绪条件化视频生成的有效性，在情绪准确率指标上显著优于基线。

**[Explicit Temporal-Semantic Modeling For Dense Video Captioning Via Context-Aware](explicit_temporal-semantic_modeling_for_dense_video_captioning_via_context-aware.md)**

:   本文提出 CACMI 框架，通过显式时序-语义建模解决密集视频描述任务中的两个基本限制（时序建模不足和模态鸿沟），使用跨模态帧聚合（CFA）提取时序一致的事件语义，再用上下文感知特征增强（CFE）桥接视觉-文本模态差距，在 ActivityNet Captions 和 YouCook2 上达到 SOTA。

**[Filmweaver Weaving Consistent Multi-Shot Videos With Cache-Guided Autoregressive](filmweaver_weaving_consistent_multi-shot_videos_with_cache-guided_autoregressive.md)**

:   提出 FilmWeaver 框架，通过双层缓存（Shot Cache + Temporal Cache）引导自回归扩散模型，实现任意长度、跨镜头一致性的多镜头视频生成。

**[Finetec Fine-Grained Action Recognition Under Temporal Corruption Via Skeleton D](finetec_fine-grained_action_recognition_under_temporal_corruption_via_skeleton_d.md)**

:   提出 FineTec 框架，通过上下文感知序列补全、基于生物先验的骨架空间分解、物理驱动的加速度建模三个模块，在时序损坏条件下实现鲁棒的细粒度骨架动作识别。

**[Genvidbench A 6-Million Benchmark For Ai-Generated Video Detection](genvidbench_a_6-million_benchmark_for_ai-generated_video_detection.md)**

:   提出 GenVidBench——首个 678 万级 AI 生成视频检测数据集，具备跨源（cross-source）和跨生成器（cross-generator）特性，覆盖 11 种 SOTA 视频生成器，并提供丰富的语义标注。

**[Group Orthogonal Low-Rank Adaptation For Rgb-T Tracking](group_orthogonal_low-rank_adaptation_for_rgb-t_tracking.md)**

:   提出 GOLA 框架，通过 SVD 分解量化 LoRA 秩重要性、冻结关键秩保留预训练先验、将冗余秩分组并施加组间正交约束，实现更高效的 RGB-T 跟踪适配。

**[Kinest A Kinematics-Guided Spatiotemporal State Space Model For Human Motion Tra](kinest_a_kinematics-guided_spatiotemporal_state_space_model_for_human_motion_tra.md)**

:   提出 KineST，一种运动学引导的状态空间模型，通过运动学树双向扫描策略和混合时空表征学习，从头显稀疏信号高效重建全身运动，在精度和时序一致性上均超越 SOTA。

**[Learning Topology-Driven Multi-Subspace Fusion For Grassmannian Deep Network](learning_topology-driven_multi-subspace_fusion_for_grassmannian_deep_network.md)**

:   提出拓扑驱动的 Grassmann 流形多子空间融合网络 GMSF-Net，通过自适应多子空间构建和基于 Fréchet 均值的子空间交互机制，将欧氏空间中多通道交互的思想成功迁移到非欧几何域，在 3D 动作识别、EEG 分类和图任务上取得 SOTA 性能。

**[Lifelong Domain Adaptive 3D Human Pose Estimation](lifelong_domain_adaptive_3d_human_pose_estimation.md)**

:   提出 lifelong domain adaptive 3D HPE 新任务，设计包含 pose-aware、temporal-aware 和 domain-aware 编码的 GAN 框架，利用 diffusion sampler 生成 domain-aware prior 缓解灾难性遗忘，在多个跨场景/跨数据集适应任务上显著超越现有方法。

**[Listening Between The Frames Bridging Temporal Gaps In Large Audio-Language Mode](listening_between_the_frames_bridging_temporal_gaps_in_large_audio-language_mode.md)**

:   提出 TimeAudio，通过时间标记（Temporal Markers）、绝对时间编码（Absolute Time-aware Encoding）和段级 Token 合并（Segment-level Token Merging）三个关键模块，赋予大型音频语言模型（LALM）精确的时间定位能力和端到端长音频理解能力，并构建了 FTAR 数据集用于细粒度时间推理的指令微调。

**[Livibench An Omnimodal Benchmark For Interactive Livestream Video Understanding](livibench_an_omnimodal_benchmark_for_interactive_livestream_video_understanding.md)**

:   提出首个面向交互式直播视频的全模态基准 LiViBench（3168 个视频、3175 道 MCQ、24 个任务），设计了多智能体种子问题驱动的半自动标注流程，并构建了 LiVi-LLM-7B 模型（含 Video-to-Comment Retrieval 模块和两阶段指令微调），在 7B 规模下超越了 72B 开源模型。

**[Loom Personalized Learning Informed By Daily Llm Conversations Toward Long-Term ](loom_personalized_learning_informed_by_daily_llm_conversations_toward_long-term_.md)**

:   提出 LOOM，一个智能体管线系统，通过观察用户日常 LLM 对话、推断学习需求、维护动态学习者记忆图（Learner Memory Graph），自动生成个性化的迷你课程，统一了学习的**连续性**（长期进度追踪）和**主动性**（即时响应新兴趣）。

**[Mask2Iv Interaction-Centric Video Generation Via Mask Trajectories](mask2iv_interaction-centric_video_generation_via_mask_trajectories.md)**

:   提出 Mask2IV，一个两阶段解耦框架——先预测交互者和物体的 mask 运动轨迹，再基于轨迹生成视频——实现了无需密集 mask 标注的、以交互为中心的可控视频生成，支持人-物交互和机器人操作两个场景。

**[Mofu Scale-Aware Modulation And Fourier Fusion For Multi-Subject Video Generatio](mofu_scale-aware_modulation_and_fourier_fusion_for_multi-subject_video_generatio.md)**

:   提出 MoFu，通过 Scale-Aware Modulation（LLM 引导的尺度感知调制）和 Fourier Fusion（基于 FFT 的排列不变特征融合）两个核心模块，同时解决多主体视频生成中的**尺度不一致**和**排列敏感性**两大挑战，并构建了 MoFu-1M 训练数据集和 MoFu-Bench 评测基准。

**[Motioncharacter Fine-Grained Motion Controllable Human Video Generation](motioncharacter_fine-grained_motion_controllable_human_video_generation.md)**

:   提出 MotionCharacter 框架，通过将运动解耦为动作类型和运动强度两个独立可控维度，实现高保真人体视频生成中的细粒度运动控制和身份一致性保持。

**[Plugtrack Multi-Perceptive Motion Analysis For Adaptive Fusion In Multi-Object T](plugtrack_multi-perceptive_motion_analysis_for_adaptive_fusion_in_multi-object_t.md)**

:   提出 PlugTrack 框架，通过多感知运动分析（CME）和自适应混合因子生成（ABG），首次实现卡尔曼滤波器与数据驱动运动预测器的自适应融合，在线性和非线性运动场景中均取得显著提升。

**[Pragworld A Benchmark Evaluating Llms Local World Model Under Minimal Linguistic](pragworld_a_benchmark_evaluating_llms_local_world_model_under_minimal_linguistic.md)**

:   提出 PragWorld 基准测试，通过对对话施加 7 种最小语言学扰动来评估 LLM 内隐世界模型的可塑性和鲁棒性，并设计双视角可解释性框架定位有害/有用层，提出层正则化微调策略提升鲁棒性。

**[Predicting Video Slot Attention Queries From Random Slot-Feature Pairs](predicting_video_slot_attention_queries_from_random_slot-feature_pairs.md)**

:   提出 RandSF.Q，通过利用下一帧特征进行信息性查询预测，以及从随机采样的 slot-feature 对学习过渡动力学，显著提升视频物体中心学习（OCL）的查询预测质量，在目标发现任务上超越 SOTA 最多 10 个点。

**[Quantifying Conversational Reliability Of Large Language Models Under Multi-Turn](quantifying_conversational_reliability_of_large_language_models_under_multi-turn.md)**

:   通过三个可确定性评估的代表性任务（指令遵循、工具选择、实体抽取），系统量化 LLM 在多轮对话中的可靠性退化程度，揭示模型在扩展对话中出现指令漂移、意图混淆和上下文覆写等失败模式。

**[R-Avst Empowering Video-Llms With Fine-Grained Spatio-Temporal Reasoning In Comp](r-avst_empowering_video-llms_with_fine-grained_spatio-temporal_reasoning_in_comp.md)**

:   提出首个面向复杂音视频场景的细粒度时空推理数据集 R-AVST（5K+未裁剪视频、27K物体、100类音视频事件），定义三个核心推理任务，并基于 GRPO 训练 AVST-Zero 模型，通过多维奖励函数直接优化音视频时空推理能力。

**[Reason Reinforced Causal Search With Information Bottleneck For Video Understand](reason_reinforced_causal_search_with_information_bottleneck_for_video_understand.md)**

:   提出因果信息瓶颈（CIB）理论框架，将关键帧选择形式化为同时优化"预测充分性"和"因果必要性"的信息论问题，并基于此设计 ReaSon 强化学习框架，通过三种 CIB 对齐的奖励（答案奖励、循环一致性奖励、反事实奖励）训练选择策略，在限定帧数设置下显著超越已有方法。

**[Rectom A Benchmark For Evaluating Machine Theory Of Mind In Llm-Based Conversati](rectom_a_benchmark_for_evaluating_machine_theory_of_mind_in_llm-based_conversati.md)**

:   提出 RecToM，首个用于评估 LLM 在对话推荐系统中心智理论（Theory of Mind）推理能力的人工标注基准，涵盖认知推理（欲望/意图/信念）和行为预测（策略预测/策略判断）两个维度共 10 种问题类型、20,524 个 QA 对，揭示了当前 LLM 在细粒度意图推断和策略判断中的系统性缺陷。

**[Rethinking Progression Of Memory State In Robotic Manipulation An Object-Centric](rethinking_progression_of_memory_state_in_robotic_manipulation_an_object-centric.md)**

:   提出 LIBERO-Mem 基准（10 个非马尔可夫机器人操控任务）和 Embodied-SlotSSM 框架（结合 Slot Attention 和状态空间模型的物体中心记忆 VLA），解决视觉运动策略在部分可观测、需要物体级历史推理的长期任务中的失败问题。

**[State-Space Hierarchical Compression With Gated Attention An](state-space_hierarchical_compression_with_gated_attention_an.md)**

:   MambaMia 提出了基于双向 Mamba 的两阶段层次化视频 Token 压缩框架：门控 Patch 聚合（GPA）做空间-时间局部压缩 + 时间轴聚合器（TAA）利用 Mamba 的自适应步长 $\Delta_t$ 做数据驱动的关键帧采样，将小时级视频压缩到仅 4.7K Token，在 LVBench 上达到 44.6 分超越 Qwen2-VL 和 mPLUG-Owl3。

**[Stegavar Privacy-Preserving Video Action Recognition Via Steganographic Domain A](stegavar_privacy-preserving_video_action_recognition_via_steganographic_domain_a.md)**

:   提出 StegaVAR 框架，首次将视频隐写术与动作识别结合，将隐私视频嵌入自然 cover 视频后直接在隐写域做分类，通过 STeP（secret 视频引导的时空特征学习）和 CroDA（跨频带差分注意力）实现接近原始视频的识别精度，同时提供优于匿名化方法的隐私保护。

**[Sugar Learning Skeleton Representation With Visual-Motion Knowledge For Action R](sugar_learning_skeleton_representation_with_visual-motion_knowledge_for_action_r.md)**

:   提出 SUGAR 范式，利用 GPT 生成的**运动描述**和**视觉描述**作为先验知识，通过对比学习监督骨骼编码器学习更离散的表示，再用 LLM（LLaMA2-7B）的未触及预训练权重作为识别器，配合新设计的 Temporal Query Projection（TQP）模块实现高效的骨骼动作分类和零样本推理。

**[Uvlm Benchmarking Video Language Model For Underwater World Understanding](uvlm_benchmarking_video_language_model_for_underwater_world_understanding.md)**

:   提出首个水下视频语言理解基准 UVLM，涵盖 2109 段视频、419 类海洋生物、20 种子任务和约 4 万 video-text pairs，通过 human-AI 协同标注注入海洋领域知识，微调后 7B VidLM 性能接近 GPT-4o。

**[Vir-Bench Evaluating Geospatial And Temporal Understanding Of Mllms Via Travel V](vir-bench_evaluating_geospatial_and_temporal_understanding_of_mllms_via_travel_v.md)**

:   提出VIR-Bench——一个基于200个日本旅行vlog视频的benchmark，通过行程重建任务（visiting order graph构建）评估MLLM的地理空间和时间理解能力，发现SOTA模型（包括GPT-4.1和Gemini-2.5）在POI识别和时间转移推理上仍困难重重。
