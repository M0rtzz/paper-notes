<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**🔬 ICLR2026** · 共 **36** 篇

**[3DGEER: 3D Gaussian Rendering Made Exact and Efficient for Generic Cameras](3dgeer_3d_gaussian_rendering_made_exact_and_efficient_for_generic_cameras.md)**

:   提出 3DGEER 框架，通过推导沿光线积分高斯密度的闭式解、设计粒子包围截锥体 (PBF) 进行精确高效的光线-粒子关联、以及引入双极等角投影 (BEAP) 统一宽视场相机表示，在任意相机模型下实现了几何精确且实时高效的 3D 高斯渲染，在鱼眼和针孔数据集上全面超越现有方法。

**[A Genetic Algorithm for Navigating Synthesizable Molecular Spaces](a_genetic_algorithm_for_navigating_synthesizable_molecular_spaces.md)**

:   提出 SynGA，一种直接在合成路线（合成树）上操作的遗传算法，通过自定义的交叉和变异算子将搜索严格约束在可合成分子空间内，结合 ML 驱动的构建块过滤实现 SOTA 的可合成类似物搜索和属性优化性能。

**[A Step to Decouple Optimization in 3DGS](a_step_to_decouple_optimization_in_3dgs.md)**

:   深入分析 3DGS 优化中被忽视的更新步耦合（不可见视点下的隐式更新和动量重缩放）和梯度耦合（正则化与光度损失在 Adam 动量中的耦合），通过解耦和重组提出 AdamW-GS 优化器，在不引入额外剪枝操作的情况下同时提升重建质量和减少冗余原语。

**[Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting](augmented_radiance_field_a_general_framework_for_enhanced_gaussian_splatting.md)**

:   提出增强辐射场 (Augmented Radiance Field) 框架，通过设计具有视角相关不透明度的增强高斯核来显式建模高光分量，并引入误差驱动的补偿策略（2D 高斯初始化 → 逆投影至 3D → 联合优化），作为后处理即插即用地增强现有 3DGS 场景，在多个数据集上超越 SOTA NeRF 方法，同时仅需二阶球谐即可捕获复杂光照。

**[cadrille: Multi-modal CAD Reconstruction with Reinforcement Learning](cadrille_multi-modal_cad_reconstruction_with_reinforcement_learning.md)**

:   cadrille 是首个同时处理点云、多视角图像和文本输入的多模态 CAD 重建模型，通过 VLM 基础架构 + SFT + RL 微调的三阶段训练范式，在 10 个 CAD 重建基准上达到 SOTA，尤其是 RL 微调将无效率降至接近 0%。

**[CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions](clods_visual-only_unsupervised_cloth_dynamics_learning_in_unknown_conditions.md)**

:   CloDS 提出首个从多视角视频中无监督学习布料动力学的框架，通过 Spatial Mapping Gaussian Splatting 建立 2D 图像到 3D 网格的可微映射，结合双位置不透明度调制解决自遮挡问题，使 GNN 在无物理参数监督下就能学到接近全监督水平的布料动力学。

**[Color3D: Controllable and Consistent 3D Colorization with Personalized Colorizer](color3d_controllable_and_consistent_3d_colorization_with_personalized_colorizer.md)**

:   Color3D 提出"只上色一张关键视角→微调个性化 colorizer→传播颜色到所有视角和时间步"的范式，将复杂的 3D 上色问题转化为单图上色+颜色传播问题，在静态和动态 3D 场景上都实现了丰富色彩、跨视角一致性和用户可控性的统一。

**[COOPERTRIM: Adaptive Data Selection for Uncertainty-Aware Cooperative Perception](coopertrim_adaptive_data_selection_for_uncertainty-aware_cooperative_perception.md)**

:   提出 CooperTrim 自适应特征选择框架，通过共形时序不确定性度量评估特征相关性，并用数据驱动机制动态决定共享数量，在协同语义分割中实现 80.28% 带宽降低且性能可比，首次将选择性共享应用于协同分割任务。

**[CORE-3D: Context-aware Open-vocabulary Retrieval by Embeddings in 3D](core-3d_context-aware_open-vocabulary_retrieval_by_embeddings_in_3d.md)**

:   提出CORE-3D，一个无需训练的开放词汇3D语义分割与自然语言目标检索流水线，通过渐进式粒度掩码生成、上下文感知CLIP编码和多视角3D融合，在Replica和ScanNet上超越现有方法。

**[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](ctrlshift_high-quality_geometry-aware_object_manipulation_in_visual_generation.md)**

:   提出Ctrl&Shift，一个端到端扩散框架，通过将物体操纵分解为物体移除+参考引导修复，并注入相对相机位姿控制，首次在不依赖显式3D重建的情况下实现几何一致的细粒度物体操纵。

**[D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](d-rex_differentiable_real-to-sim-to-real_engine_for_learning_dexterous_grasping.md)**

:   提出D-REX，一个基于高斯表示的可微real-to-sim-to-real引擎，通过视觉观测和机器人控制信号进行端到端物体质量辨识，并利用辨识的质量进行力感知的灵巧抓取策略学习，有效缩小了sim-to-real差距。

**[Dissecting Chronos: Sparse Autoencoders Reveal Causal Feature Hierarchies in Time Series Foundation Models](dissecting_chronos_sparse_autoencoders_reveal_causal_feature_hierarchies_in_time.md)**

:   首次将稀疏自编码器 (SAE) 应用于时间序列基础模型 Chronos-T5-Large，通过 392 次因果消融实验揭示了深度依赖的特征层级：中层编码器集中了因果关键的突变检测特征，而语义最丰富的末层编码器反而因果重要性最低。

**[Dynamic Novel View Synthesis in High Dynamic Range](dynamic_novel_view_synthesis_in_high_dynamic_range.md)**

:   首次提出 HDR 动态新视角合成 (HDR DNVS) 问题，并设计 HDR-4DGS 框架，通过动态色调映射模块在时变场景中实现时序一致的 HDR 辐射场重建，在合成和真实数据集上均超越现有方法。

**[Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention](efficient-lvsm_faster_cheaper_and_better_large_view_synthesis_model_via_decouple.md)**

:   提出 Efficient-LVSM，通过解耦输入视图编码与目标视图生成的双流架构，将新视图合成的复杂度从 $O(N_{in}^2)$ 降至 $O(N_{in})$，在 RealEstate10K 上以 50% 训练时间达到 SOTA（29.86 dB PSNR），推理速度提升 4.4 倍。

**[EgoNight: Towards Egocentric Vision Understanding at Night with a Challenging Benchmark](egonight_towards_egocentric_vision_understanding_at_night_with_a_challenging_ben.md)**

:   构建首个系统性夜间第一人称视觉基准 EgoNight，包含日夜对齐的合成/真实视频和 3658 个 QA 对（12种类型，300+小时人工标注），揭示所有 SOTA MLLM 在日夜转换中的显著性能下降。

**[EgoWorld: Translating Exocentric View to Egocentric View using Rich Exocentric Observations](egoworld_translating_exocentric_view_to_egocentric_view_using_rich_exocentric_ob.md)**

:   提出 EgoWorld 框架，通过从外部视角提取点云、3D 手部姿态和文本描述等多模态观测，利用两阶段管线将单张第三人称图像转换为高质量的第一人称视图。

**[Fast Estimation of Wasserstein Distances via Regression on Sliced Wasserstein Distances](fast_estimation_of_wasserstein_distances_via_regression_on_sliced_wasserstein_di.md)**

:   提出通过将 Wasserstein 距离回归到 Sliced Wasserstein (SW) 距离的线性模型（RG 框架），实现对 Wasserstein 距离的快速高效估计，在低数据场景下显著优于深度学习方法 Wasserstein Wormhole。

**[FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation](fastgha_generalized_few-shot_3d_gaussian_head_avatars_with_real-time_animation.md)**

:   提出 FastGHA，一个前馈式少样本 3D 高斯头部化身生成框架，从 4 张任意表情/视角的输入图像在 ~1 秒内重建可动画的 3D 高斯头部，支持 62 FPS 实时动画，在 Ava-256 上 PSNR 达到 22.5 dB（超越 Avat3r 的 20.7，且快 7.75 倍）。

**[FeDaL: Federated Dataset Learning for General Time Series Foundation Models](fedal_federated_dataset_learning_for_general_time_series_foundation_models.md)**

:   提出 FeDaL 联邦框架从头训练通用时序基础模型（TSFM），通过客户端域偏差消除（DBE）和服务器全局偏差消除（GBE）处理数据集级异质性，在8个任务上超越54个baseline。

**[Fused-Planes: Why Train a Thousand Tri-Planes When You Can Share?](fused-planes_why_train_a_thousand_tri-planes_when_you_can_share.md)**

:   提出 Fused-Planes，通过宏观-微观分解将 Tri-Plane 表示分为共享的类级基平面（macro）和对象特有的细节平面（micro），结合潜空间渲染，实现 7× 训练加速、3× 内存压缩，同时保持甚至超越独立 Tri-Plane 的重建质量。

**[Geometry-aware 4D Video Generation for Robot Manipulation](geometry-aware_4d_video_generation_for_robot_manipulation.md)**

:   提出几何感知的4D视频生成框架，通过跨视角 pointmap 对齐监督在视频扩散模型中强制多视角3D一致性，无需相机位姿输入即可从新视角生成时空对齐的未来 RGB-D 序列，并可直接用 FoundationPose 从生成视频中恢复机器人末端执行器轨迹。

**[GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation](geopurify_a_data-efficient_geometric_distillation_framework_for_open-vocabulary_.md)**

:   提出 GeoPurify 框架，通过从 3D 自监督教师模型蒸馏几何先验来净化 2D VLM 投影到 3D 的噪声特征，仅用约 1.5% 的训练数据即可达到或超越全量训练的 SOTA 开放词汇 3D 分割性能。

**[GIQ: Benchmarking 3D Geometric Reasoning of Vision Foundation Models with Simulated and Real Polyhedra](giq_benchmarking_3d_geometric_reasoning_of_vision_foundation_models_with_simulat.md)**

:   提出 GIQ 基准数据集，包含 224 种合成和真实多面体，通过单目 3D 重建、对称性检测、心理旋转测试和零样本分类四项任务系统评估视觉基础模型的几何推理能力，揭示了当前模型在基本几何理解上的显著不足。

**[HDR-NSFF: High Dynamic Range Neural Scene Flow Fields](hdr-nsff_high_dynamic_range_neural_scene_flow_fields.md)**

:   提出 HDR-NSFF，将 HDR 视频重建从传统的 2D 像素级融合范式转变为 4D 时空建模，从交替曝光单目视频中联合重建 HDR 辐射场、3D 场景流、几何和色调映射，实现了时空一致的动态 HDR 新视角合成。

**[Into The Rabbit Hull From Task-Relevant Concepts](into_the_rabbit_hull_from_task-relevant_concepts.md)**

:   本文通过稀疏自编码器（SAE）从 DINOv2 中提取 32,000 个视觉概念字典，系统研究了不同下游任务（分类/分割/深度估计）如何选择性地使用这些概念，揭示了表示空间的几何结构超越了线性稀疏编码假说（LRH），并提出了基于 Minkowski 和的新表示假说（MRH），认为 token 是多个凸混合的叠加。

**[Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry](into_the_rabbit_hull_from_task-relevant_concepts_in_dino_to_minkowski_geometry.md)**

:   通过在 DINOv2 上训练 32,000 单元的 Sparse Autoencoder 字典，系统分析了下游任务如何招募不同概念，发现表征几何偏离线性稀疏假说（LRH），进而提出 Minkowski Representation Hypothesis（MRH），认为 token 表征是多个凸多面体的 Minkowski 和，概念由原型点的邻近性而非线性方向定义。

**[Joint Shadow Generation and Relighting via Light-Geometry Interaction Maps](joint_shadow_generation_and_relighting_via_light-geometry_interaction_maps.md)**

:   提出 Light-Geometry Interaction (LGI) maps，一种从单目深度估计中编码光照-遮挡关系的 2.5D 表示，嵌入 bridge matching 生成框架中实现阴影生成与物体重光照的联合建模，在合成和真实图像上均取得 SOTA 效果。

**[MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](moe-gs_mixture_of_experts_for_dynamic_gaussian_splatting.md)**

:   提出 MoE-GS，首个将混合专家架构引入动态高斯泼溅的框架，通过 Volume-aware Pixel Router 自适应融合多种异构变形先验（HexPlane/逐高斯/多项式/插值），在 N3V 和 Technicolor 数据集上一致超越 SOTA，并通过单次渲染、门控剪枝和知识蒸馏保持效率。

**[Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos](mono4dgs-hdr_high_dynamic_range_4d_gaussian_splatting_from_alternating-exposure_.md)**

:   首次解决从无位姿交替曝光单目视频重建可渲染 4D HDR 场景的问题，通过两阶段优化（正交视频空间 → 世界空间）、Video-to-World 高斯变换策略和时间亮度正则化，在合成数据上达到 37.64 dB HDR PSNR、161 FPS，全面超越现有方法。

**[Omni-View: Unlocking How Generation Facilitates Understanding in Unified 3D Model based on Multiview images](omni-view_unlocking_how_generation_facilitates_understanding_in_unified_3d_model.md)**

:   构建统一的3D场景理解与生成模型 Omni-View，通过纹理模块（新视角合成）和几何模块（深度/位姿估计）的生成能力增强理解性能，在 VSI-Bench 上达到 55.4 分超越所有现有专用3D理解模型。

**[One2Scene Geometric Consistent Explorable 3D Scene Generation From A Single Ima](one2scene_geometric_consistent_explorable_3d_scene_generation_from_a_single_ima.md)**

:   提出 One2Scene 三阶段框架，将单图生成可探索 3D 场景分解为全景生成→前馈 3D 高斯溅射构建几何支架→支架引导的新视角合成，通过将全景深度估计重新表述为多视图立体匹配问题，实现几何一致且可自由探索的 3D 场景生成。

**[PartSAM: A Scalable Promptable Part Segmentation Model Trained on Native 3D Data](partsam_a_scalable_promptable_part_segmentation_model_trained_on_native_3d_data.md)**

:   提出首个在大规模原生 3D 数据上训练的可提示部件分割模型 PartSAM，采用 triplane 双分支编码器（冻结 SAM 先验 + 可学习 3D 分支）和 SAM 风格解码器，通过模型在环标注流程构建 500 万+形状-部件对，在开放世界设置下单次点击即超越 Point-SAM 90%+。

**[PD²GS: Part-Level Decoupling and Continuous Deformation of Articulated Objects via Gaussian Splatting](pd2gs_part-level_decoupling_and_continuous_deformation_of_articulated_objects_vi.md)**

:   提出 PD²GS 框架，通过学习共享的 canonical 高斯场并将每个交互状态建模为其连续形变，实现铰接物体的部件级解耦、重建和连续控制，采用粗到细的运动轨迹聚类 + SAM 引导的边界细化，无需手动监督。

**[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](peering_into_the_unknown_active_view_selection_with_neural_uncertainty_maps_for_.md)**

:   提出 PUN 方法，通过轻量级 UPNet（ViT）从单张图像预测神经不确定性图（球面坐标系下所有候选视点的不确定性分布），避免迭代 NeRF 重训练，仅用一半视点达到全视点上界的重建质量，实现 400 倍加速和 50%+ 计算节省。

**[Quantized Visual Geometry Grounded Transformer](quantized_visual_geometry_grounded_transformer.md)**

:   针对十亿级 3D 重建模型 VGGT 的部署需求，提出首个专用 PTQ 框架 QuantVGGT，通过双重平滑细粒度量化（Hadamard 旋转 + 通道平滑）解决特殊 token 导致的重尾分布，以及噪声过滤多样化采样解决校准不稳定问题，4-bit 量化实现 3.7× 内存压缩和 2.5× 加速，保持 98%+ 精度。

**[Weight Space Representation Learning on Diverse NeRF Architectures](weight_space_representation_learning_on_diverse_nerf_architectures.md)**

:   提出首个能处理多种 NeRF 架构（MLP/tri-plane/hash table）权重的表示学习框架，通过 Graph Meta-Network 编码器 + SigLIP 对比损失构建架构无关的潜在空间，在 13 种 NeRF 架构上实现分类、检索和语言任务，并能泛化到训练时未见的架构。
