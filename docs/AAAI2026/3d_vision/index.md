<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**🤖 AAAI2026** · 共 **37** 篇

**[3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition](3d-anc_adaptive_neural_collapse_for_robust_3d_point_cloud_re.md)**

:   将Neural Collapse(NC)机制引入3D点云对抗鲁棒性，用固定的ETF分类头+自适应训练框架(RBL+FDL)构建解耦的特征空间，在ModelNet40上将DGCNN的对抗准确率从27.2%提升到80.9%，超出最佳baseline 34个点。

**[3D-Free Meets 3D Priors: Novel View Synthesis from a Single Image with Pretrained Diffusion Guidance](3d-free_meets_3d_priors_novel_view_synthesis_from_a_single_image_with_pretrained.md)**

:   提出将 3D-free 方法（HawkI 风格的 test-time optimization）与 3D-based 先验（Zero123++ 的弱引导图）结合的框架，无需额外 3D 数据或训练即可从单张图片生成指定仰角/方位角的相机控制视图，在复杂场景下 LPIPS、CLIP-Score 等指标全面超越 Zero123++、HawkI 和 Stable Zero123。

**[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](4dstr_advancing_generative_4d_gaussians_with_spatial-tempora.md)**

:   提出4DSTR框架，通过基于Mamba的时序关联校正（修正高斯点的尺度和旋转）以及逐帧自适应稠密化与裁剪策略，显著提升4D高斯生成的时空一致性和对快速时序变化的适应能力。

**[Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models](adapt-as-you-walk_through_the_clouds_training-free_online_te.md)**

:   提出 Uni-Adapter，一种面向3D视觉-语言基础模型(VLFM)的无训练在线测试时适应框架，通过基于聚类的动态原型缓存和图正则化标签平滑来应对分布偏移，在多个3D损坏基准上取得SOTA。

**[AnchorDS: Anchoring Dynamic Sources for Semantically Consistent Text-to-3D Generation](anchords_anchoring_dynamic_sources_for_semantically_consiste.md)**

:   揭示 SDS 中源分布是动态演化而非静态的关键问题，提出 AnchorDS，通过将当前渲染图像作为图像条件输入双条件扩散模型来锚定源分布，解决了 SDS 的语义过度平滑和多视角不一致问题，在 T3Bench 上全面超越 SDS/VSD/SDS-Bridge。

**[AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation](anchorhoi_zero-shot_generation_of_4d_human-object_interactio.md)**

:   提出 AnchorHOI，通过锚点NeRF和锚点关键点两种中间桥梁，分别从图像/视频扩散模型中蒸馏交互先验和运动先验，实现零样本的文本驱动4D人物-物体交互生成，在静态3D和动态4D HOI生成上均超越已有方法。

**[Arbitrary-Scale 3D Gaussian Super-Resolution](arbitrary-scale_3d_gaussian_super-resolution.md)**

:   提出一个集成框架实现3D高斯溅射(3DGS)的任意倍率超分辨率渲染，通过尺度感知渲染、生成先验引导优化和渐进超分机制，用单个3D模型支持整数和非整数倍率的HR渲染，PSNR提升6.59dB同时保持85 FPS实时速度。

**[ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation](assist-3d_adapted_scene_synthesis_for_class-agnostic_3d_instance_segmentation.md)**

:   提出 ASSIST-3D 合成数据流水线，通过异构物体选择、LLM 引导的场景布局生成和仿真实点云构建三个阶段，为 class-agnostic 3D 实例分割生成高质量标注数据，显著提升模型泛化能力。

**[Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?](can_protective_watermarking_safeguard_the_copyright_of_3d_gaussian_splatting.md)**

:   首次系统性地揭示了 3DGS 水印框架的脆弱性，提出 GSPure 框架通过视角感知权重累积和几何特征聚类精准分离并去除水印相关的 Gaussian 原语，在水印 PSNR 最高降低 16.34dB 的同时保持原始场景损失不足 1dB。

**[CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection](casl_curvature-augmented_self-supervised_learning_for_3d_anomaly_detection.md)**

:   发现点云曲率本身就是强大的异常检测线索，提出曲率增强的自监督学习框架 CASL，通过多尺度曲率提示引导坐标重建来学习通用 3D 表征，无需任何异常检测专用机制即可在 Real3D-AD 上以 5.6% O-AUROC 优势刷新 SOTA。

**[Class-Partitioned VQ-VAE and Latent Flow Matching for Point Cloud Scene Generation](class-partitioned_vq-vae_and_latent_flow_matching_for_point_cloud_scene_generati.md)**

:   提出类别分区的 VQ-VAE（CPVQ-VAE）和潜空间流匹配模型（LFMM），实现了首个无需外部数据库检索的纯点云场景生成方法，在复杂客厅场景上将 Chamfer 距离降低了 70.4%。

**[CtrlFuse: Mask-Prompt Guided Controllable Infrared and Visible Image Fusion](ctrlfuse_mask-prompt_guided_controllable_infrared_and_visible_image_fusion.md)**

:   提出 CtrlFuse，通过 mask prompt 引导 SAM 微调，实现红外-可见光图像的交互式可控融合，在融合质量和下游分割/检测任务上同时取得提升。

**[DANCE: Density-Agnostic and Class-Aware Network for Point Cloud Completion](dance_density-agnostic_and_class-aware_network_for_point_cloud_completion.md)**

:   提出 DANCE 框架，通过基于射线的候选点采样和 opacity 预测机制实现密度无关的点云补全，并引入分类头提供语义先验，在 PCN 和 MVP 基准上取得 SOTA。

**[DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion](dapointmamba_domain_adaptive_point_mamba_for_point_cloud_completion.md)**

:   首次将 Mamba（SSM）引入无监督域自适应点云补全（UDA PCC），提出 DAPointMamba 框架，通过跨域 Patch 级扫描、空间 SSM 对齐和通道 SSM 对齐三个模块，在保持线性复杂度和全局感受野的同时实现了跨域高质量点云补全。

**[Debiasing Diffusion Priors via 3D Attention for Consistent Gaussian Splatting](debiasing_diffusion_priors_via_3d_attention_for_consistent_gaussian_splatting.md)**

:   提出 TD-Attn 框架，通过 3D 感知注意力引导（3D-AAG）和层级注意力调制（HAM）两个模块，解决 T2I 扩散模型中先验视角偏差导致的 3D 生成/编辑多视图不一致问题（Janus problem），可作为通用插件集成到现有 3DGS 框架。

**[DeepRAHT: Learning Predictive RAHT for Point Cloud Attribute Compression](deepraht_learning_predictive_raht_for_point_cloud_attribute_compression.md)**

:   提出首个端到端可微的 RAHT（Region Adaptive Hierarchical Transform）框架 DeepRAHT，用于有损点云属性压缩，通过可学习的预测模型和基于 Laplace 分布的码率代理实现了超越 G-PCC 标准和现有深度学习方法的压缩性能。

**[Distilling Future Temporal Knowledge with Masked Feature Reconstruction for 3D Object Detection](distilling_future_temporal_knowledge_with_masked_feature_reconstruction_for_3d_o.md)**

:   提出 FTKD（Future Temporal Knowledge Distillation）框架，通过未来感知特征重建（FFR）和未来引导 logit 蒸馏（FLD）两个策略，将离线教师模型中的未来帧知识有效迁移到在线学生模型，在 nuScenes 上取得 1.3 mAP/1.3 NDS 提升且不增加推理开销。

**[Domain Generalized Stereo Matching with Uncertainty-guided Data Augmentation](domain_generalized_stereo_matching_with_uncertainty-guided_data_augmentation.md)**

:   提出 UgDA-Stereo，通过对 RGB 图像逐通道均值和标准差施加基于批次统计量的高斯不确定性扰动来模拟多种未知域的视觉风格，并结合特征一致性约束，以即插即用方式显著提升立体匹配模型的跨域泛化能力。

**[Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos](dynamic_gaussian_scene_reconstruction_from_unsynchronized_videos.md)**

:   提出了一个粗到精（coarse-to-fine）的时间对齐模块，可插入到现有 4D Gaussian Splatting 框架中，解决多视角视频时间不同步导致的动态场景重建质量退化问题，在 DyNeRF 数据集上显著提升了多个基线方法的 PSNR/SSIM/LPIPS。

**[Enhancing Generalization of Depth Estimation Foundation Model via Weakly-Supervised Adaptation with Regularization](enhancing_generalization_of_depth_estimation_foundation_model_via_weakly-supervi.md)**

:   提出 WeSTAR 框架，通过语义感知的分层归一化自训练 + 稀疏成对序数弱监督 + LoRA 权重正则化三者协同，以参数高效的方式提升深度估计基础模型（Depth Anything V2）在未见域和损坏数据上的泛化能力，在多个 OOD 基准上达到 SOTA。

**[Enhancing Rotation-Invariant 3D Learning with Global Pose Awareness and Attention Mechanisms](enhancing_rotation-invariant_3d_learning_with_global_pose_awareness_and_attentio.md)**

:   提出 Shadow-informed Pose Feature (SiPF) 和 RIAttnConv 算子，通过引入基于 Bingham 分布学习的全局"影子"参考点来增强局部旋转不变特征的全局姿态感知能力，解决对称结构（如飞机左右机翼）无法区分的"Wing-tip Feature Collapse"问题，在 ModelNet40 分类和 ShapeNetPart 分割上达到 SOTA。

**[EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios](epsegfz_efficient_point_cloud_semantic_segmentation_for_few-_and_zero-shot_scena.md)**

:   提出 EPSegFZ，一个无需预训练的3D点云少样本/零样本语义分割框架，通过 ProERA 提取高频特征、LGPE 融合文本信息更新原型、DRPE 建立精确的查询-原型对应关系，在 S3DIS 和 ScanNet 上分别超越 SOTA 5.68% 和 3.82%。

**[Exploring Surround-View Fisheye Camera 3D Object Detection](exploring_surround-view_fisheye_camera_3d_object_detection.md)**

:   本文系统研究了环视鱼眼相机的3D目标检测问题：构建了同时包含针孔和鱼眼相机数据的Fisheye3DOD基准数据集，并提出FisheyeBEVDet和FisheyePETR两个框架，通过球面特征表征将鱼眼几何建模嵌入主流检测范式，相比矫正baseline提升最高6.2个FDS点。

**[FoundationSLAM: 释放深度基础模型在端到端稠密视觉SLAM中的潜力](foundationslam_unleashing_the_power_of_depth_foundation_models_for.md)**

:   将深度基础模型的几何先验注入光流式SLAM系统，通过混合光流网络、双向一致BA层和可靠性感知精炼三个模块形成闭环，在TUM/EuRoC/7Scenes/ETH3D四大数据集取得SOTA轨迹精度和稠密重建质量，18 FPS实时运行。

**[Free-Form Scene Editor: Enabling Multi-Round Object Manipulation like in a 3D Engine](free-form_scene_editor_enabling_multi-round_object_manipulation_like_in_a_3d_eng.md)**

:   提出FFSE——一个基于视频扩散模型的自回归3D感知图像编辑框架，配合混合数据集3DObjectEditor（真实+合成），能像3D引擎一样在真实图像上执行多轮物体平移/缩放/旋转操作，同时生成逼真的阴影/反射/遮挡等背景效果并保持跨轮编辑一致性，在单轮和多轮编辑中均大幅超越现有方法。

**[Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting](gaussian_blending_rethinking_alpha_blending_in_3d_gaussian_splatting.md)**

:   重新审视3DGS中的标量alpha blending，指出其忽略像素内空间变化是多尺度渲染伪影（放大erosion/缩小dilation）的根源，提出Gaussian Blending——将alpha和transmittance建模为像素内的空间分布（2D uniform window），实现实时抗锯齿且无需重训练，在多尺度Blender上PSNR从31.59→35.80。

**[Hierarchical Direction Perception Via Atomic Dot-Product Operators For Rotation-](hierarchical_direction_perception_via_atomic_dot-product_operators_for_rotation-.md)**

:   提出 DiPVNet，基于 atomic dot-product operator 的双重属性（方向选择性 + 旋转不变性），构建局部 L2DP 算子和全局 DASFT 模块，实现层次化方向感知的旋转不变点云学习。

**[Mobgs Motion Deblurring Dynamic 3D Gaussian Splatting For Blurry Monocular Video](mobgs_motion_deblurring_dynamic_3d_gaussian_splatting_for_blurry_monocular_video.md)**

:   MoBGS 提出了一种端到端的动态去模糊 3D Gaussian Splatting 框架，通过 Blur-adaptive Latent Camera Estimation (BLCE) 和 Latent Camera-induced Exposure Estimation (LCEE) 两个核心模块，从模糊单目视频中重建清晰的时空新视角，在 Stereo Blur 数据集上大幅超越现有 SOTA 方法。

**[OpenScan: A Benchmark for Generalized Open-Vocabulary 3D Scene Understanding](openscan_a_benchmark_for_generalized_open-vocabulary_3d_scene_understanding.md)**

:   本文提出了广义开放词汇 3D 场景理解任务（GOV-3D）及对应的 OpenScan 基准，将 3D 场景理解从物体类别扩展到八种语言学属性维度，揭示了现有 OV-3D 方法在理解抽象物体属性方面的严重不足。

**[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](physics-informed_deformable_gaussian_splatting_towards_unified_constitutive_laws.md)**

:   将每个3D Gaussian视为拉格朗日物质点，引入时变材料场预测粒子速度和本构应力张量，通过Cauchy动量残差作为物理约束 + 拉格朗日粒子流匹配作为数据拟合项，在单目动态视图合成中实现了物理一致性和跨场景泛化能力，在自建物理驱动数据集和HyperNeRF真实数据集上均达到SOTA。

**[Point-Sra Self-Representation Alignment For 3D Representation Learning](point-sra_self-representation_alignment_for_3d_representation_learning.md)**

:   提出 Point-SRA，通过 Dual Self-Representation Alignment（MAE 层 + MFT 层）和 MeanFlow 概率建模，利用不同 mask ratio 下表征的互补性来增强 3D 点云表征学习，在 ScanObjectNN 上超越 Point-MAE 达 5.59%。

**[Probfm Probabilistic Time Series Foundation Model With Uncertainty Decomposition](probfm_probabilistic_time_series_foundation_model_with_uncertainty_decomposition.md)**

:   首次将 Deep Evidential Regression (DER) 与 Normal-Inverse-Gamma 先验引入时序基础模型架构，实现单次前向传播即可进行 epistemic-aleatoric 不确定性分解，并在加密货币预测中验证了不确定性感知交易策略的实用价值。

**[Real-Time 3D Object Detection with Inference-Aligned Learning](real-time_3d_object_detection_with_inference-aligned_learning.md)**

:   提出 SR3D 框架，通过空间优先最优传输标签分配（SPOTA）和排序感知自适应自蒸馏（RAS）两个训练阶段组件，弥合室内密集 3D 目标检测中训练与推理行为的不一致性，在 ScanNet V2 和 SUN RGB-D 上以 42ms 实时速度刷新密集检测器 SOTA。

**[Redundant Queries In Detr-Based 3D Detection Methods Unnecessary And Prunable](redundant_queries_in_detr-based_3d_detection_methods_unnecessary_and_prunable.md)**

:   提出 GPQ（Gradually Pruning Queries），通过分类分数逐步裁剪 DETR 系 3D 检测器中大量冗余的 object queries，无需额外可学习参数，可直接在预训练 checkpoint 上微调完成，在边缘设备上最高实现 67.86% FLOPs 减少和 65.16% 推理时间下降。

**[S5 Scalable Semi-Supervised Semantic Segmentation In Remote Sensing](s5_scalable_semi-supervised_semantic_segmentation_in_remote_sensing.md)**

:   提出 S5 框架，首次将半监督语义分割 (S4) 从小规模数据扩展为大规模预训练范式 (S4P)，构建百万级 RS4P-1M 数据集预训练遥感基础模型，并通过 MoE-based 多数据集微调实现 SOTA 性能。

**[Smartsplat Feature-Smart Gaussians For Scalable Compression Of Ultra-High-Resolu](smartsplat_feature-smart_gaussians_for_scalable_compression_of_ultra-high-resolu.md)**

:   提出SmartSplat，一种基于特征感知的2D Gaussian Splatting图像压缩框架，通过梯度-颜色引导的变分采样、排斥均匀采样和尺度自适应颜色初始化三大策略，首次实现了8K/16K超高分辨率图像在极端压缩比（最高5000×）下的高质量重建。

**[Surface-Based Visibility-Guided Uncertainty for Continuous Active 3D Neural Reconstruction](surface-based_visibility-guided_uncertainty_for_continuous_active_3d_neural_reco.md)**

:   提出基于表面的可见性场(SBV)，通过SDF推导的表面置信度和体素网格更新机制在连续主动学习过程中准确估计不确定性的可见性，指导Next-Best View选择，在DTU/Blender/TanksAndTemples/BlendedMVS四个基准上图像渲染质量提升最高11.6%。
