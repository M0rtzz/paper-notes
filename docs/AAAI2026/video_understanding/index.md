<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🤖 AAAI2026** · 共 **16** 篇

**[3D4D: An Interactive Editable 4D World Model via 3D Video Generation](3d4d_an_interactive_editable_4d_world_model_via_3d_video_generation.md)**

:   提出 3D4D，一个集成 WebGL 和 Supersplat 渲染的交互式 4D 可视化框架，通过四个后端模块（3D重建、图像生视频、视频分帧、4D场景生成）将静态图片和文本转化为可实时交互的 4D 场景，并引入 VLM 引导的注视点渲染策略在保持语义一致性的同时实现 60fps 实时交互。

**[APVR: Hour-Level Long Video Understanding with Adaptive Pivot Visual Information Retrieval](apvr_hour-level_long_video_understanding_with_adaptive_pivot.md)**

:   提出APVR，一个训练免费的双粒度视觉信息检索框架：帧级别通过查询扩展+时空语义置信度打分迭代检索关键帧（最多1024帧），token级别通过查询感知的注意力驱动选择压缩视觉token，突破内存墙限制处理小时级长视频，在LongVideoBench/VideoMME/MLVU上分别提升最高9.5%/4.6%/9.7%。

**[Balancing Multimodal Domain Generalization via Gradient Modulation and Projection](balancing_multimodal_domain_generalization_via_gradient_modulation_and_projectio.md)**

:   提出 Gradient Modulation Projection (GMP) 策略，通过解耦分类与域不变梯度的调制（IGDM）以及冲突自适应梯度投影（CAGP），解决多模态域泛化中模态间优化不平衡和任务间梯度冲突问题，在多个基准上达到 SOTA。

**[BAT: Learning Event-based Optical Flow with Bidirectional Adaptive Temporal Correlation](bat_learning_event-based_optical_flow_with_bidirectional_adaptive_temporal_corre.md)**

:   提出双向自适应时序相关性（BAT）框架，将事件相机的时序密集运动线索转化为空间密集线索，实现高精度事件光流估计，在 DSEC-Flow 基准上排名第一。

**[Causality Matters: How Temporal Information Emerges in Video Language Models](causality_matters_how_temporal_information_emerges_in_video_language_models.md)**

:   通过系统性消融实验揭示VideoLM的时序理解能力并非来源于位置编码(PE)，而是由因果注意力掩码的序列敏感性产生——时序信息沿"帧间交互→末帧聚合→query融合"的因果路径逐层构建，并据此提出两种无损推理加速策略。

**[Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy](coordinated_humanoid_robot_locomotion_with_symmetry_equivariant_reinforcement_le.md)**

:   提出 SE-Policy，将严格的对称等变性（actor）和对称不变性（critic）直接嵌入神经网络架构，无需额外超参数即可使人形机器人产生时空协调的自然运动，速度跟踪误差相比 DreamWaQ 降低 40%，并成功部署到 Unitree G1 实体机器人。

**[Decomposition and Preprocessing of Ternary Constraint Networks](decomposition_and_preprocessing_of_ternary_constraint_networks.md)**

:   提出将任意离散约束网络形式化分解为三元约束网络(TCN)的完整理论框架，并通过七项预处理技术（传播、代数简化、公共子表达式消除等）将分解引入的变量/约束膨胀从中位数8x/6x降至4.8x/4.3x，为GPU硬件上的高效约束求解提供规则化数据布局。

**[Distillation Dynamics: Towards Understanding Feature-Based Distillation in Vision Transformers](distillation_dynamics_towards_understanding_feature-based_di.md)**

:   提出"蒸馏动力学"分析框架（频谱分析+信息熵+激活幅值），揭示ViT具有独特的U型信息处理模式（先压缩后扩展），证明feature-based蒸馏在ViT中失败的根本原因是teacher后层的分布式高维编码范式与student有限通道容量之间的表征范式不匹配，而非简单的容量差距。

**[DreamRunner: Fine-Grained Compositional Story-to-Video Generation with Retrieval-Augmented Motion Adaptation](dreamrunner_fine-grained_compositional_story-to-video_genera.md)**

:   提出 DreamRunner 框架，通过 LLM 双层规划 + 检索增强运动先验学习 + 时空区域3D注意力模块(SR3AI)，实现细粒度可控的多角色多事件故事视频生成。

**[Explicit Temporal-Semantic Modeling for Dense Video Captioning via Context-Aware Cross-Modal Interaction](explicit_temporal-semantic_modeling_for_dense_video_captioning_via_context-aware.md)**

:   本文提出 CACMI 框架，通过显式时序-语义建模解决密集视频描述任务中的两个基本限制（时序建模不足和模态鸿沟），使用跨模态帧聚合（CFA）提取时序一致的事件语义，再用上下文感知特征增强（CFE）桥接视觉-文本模态差距，在 ActivityNet Captions 和 YouCook2 上达到 SOTA。

**[Learning Topology-Driven Multi-Subspace Fusion For Grassmannian Deep Network](learning_topology-driven_multi-subspace_fusion_for_grassmannian_deep_network.md)**

:   提出拓扑驱动的 Grassmann 流形多子空间融合网络 GMSF-Net，通过自适应多子空间构建和基于 Fréchet 均值的子空间交互机制，将欧氏空间中多通道交互的思想成功迁移到非欧几何域，在 3D 动作识别、EEG 分类和图任务上取得 SOTA 性能。

**[Lifelong Domain Adaptive 3D Human Pose Estimation](lifelong_domain_adaptive_3d_human_pose_estimation.md)**

:   提出 lifelong domain adaptive 3D HPE 新任务，设计包含 pose-aware、temporal-aware 和 domain-aware 编码的 GAN 框架，利用 diffusion sampler 生成 domain-aware prior 缓解灾难性遗忘，在多个跨场景/跨数据集适应任务上显著超越现有方法。

**[MambaMia: State-Space Hierarchical Compression for Hour-Long Video Understanding in Large Multimodal Models](state-space_hierarchical_compression_with_gated_attention_an.md)**

:   MambaMia 提出了基于双向 Mamba 的两阶段层次化视频 Token 压缩框架：门控 Patch 聚合（GPA）做空间-时间局部压缩 + 时间轴聚合器（TAA）利用 Mamba 的自适应步长 $\Delta_t$ 做数据驱动的关键帧采样，将小时级视频压缩到仅 4.7K Token，在 LVBench 上达到 44.6 分超越 Qwen2-VL 和 mPLUG-Owl3。

**[Stegavar Privacy-Preserving Video Action Recognition Via Steganographic Domain A](stegavar_privacy-preserving_video_action_recognition_via_steganographic_domain_a.md)**

:   提出 StegaVAR 框架，首次将视频隐写术与动作识别结合，将隐私视频嵌入自然 cover 视频后直接在隐写域做分类，通过 STeP（secret 视频引导的时空特征学习）和 CroDA（跨频带差分注意力）实现接近原始视频的识别精度，同时提供优于匿名化方法的隐私保护。

**[Uvlm Benchmarking Video Language Model For Underwater World Understanding](uvlm_benchmarking_video_language_model_for_underwater_world_understanding.md)**

:   提出首个水下视频语言理解基准 UVLM，涵盖 2109 段视频、419 类海洋生物、20 种子任务和约 4 万 video-text pairs，通过 human-AI 协同标注注入海洋领域知识，微调后 7B VidLM 性能接近 GPT-4o。

**[VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction](vir-bench_evaluating_geospatial_and_temporal_understanding_of_mllms_via_travel_v.md)**

:   提出VIR-Bench——一个基于200个日本旅行vlog视频的benchmark，通过行程重建任务（visiting order graph构建）评估MLLM的地理空间和时间理解能力，发现SOTA模型（包括GPT-4.1和Gemini-2.5）在POI识别和时间转移推理上仍困难重重。
