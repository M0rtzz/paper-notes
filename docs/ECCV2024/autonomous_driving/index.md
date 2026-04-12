---
title: >-
  ECCV2024 自动驾驶方向 14篇论文解读
description: >-
  14篇ECCV2024 自动驾驶方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**🎞️ ECCV2024** · 共 **14** 篇

**[4D Contrastive Superflows Are Dense 3D Representation Learners](4d_contrastive_superflows_are_dense_3d_representation_learners.md)**

:   提出SuperFlow框架，通过视图一致性对齐、稠密-稀疏一致性正则化、和基于流的时空对比学习三个模块，利用连续LiDAR-相机对建立4D预训练目标，在11个异构LiDAR数据集上全面超越了之前的Image-to-LiDAR预训练方法。

**[Accelerating Online Mapping And Behavior Prediction Via Dire](accelerating_online_mapping_and_behavior_prediction_via_dire.md)**

:   提出直接将在线地图估计模型内部的BEV特征暴露给下游轨迹预测模型（而非仅传递解码后的矢量化地图），通过三种BEV特征注入策略实现推理加速最高73%、预测精度提升最高29%。

**[Adaptive Human Trajectory Prediction Via Latent Corridors](adaptive_human_trajectory_prediction_via_latent_corridors.md)**

:   将prompt tuning思想引入行人轨迹预测，通过在预训练轨迹预测器的输入端添加可学习的低秩图像prompt（称为latent corridors），以不到0.1%的额外参数实现对部署场景特定行为模式的高效自适应，在合成和真实数据上分别取得最高23.9%和26.8%的ADE提升。

**[Approaching Outside Scaling Unsupervised 3D Object Detection From 2D Scene](approaching_outside_scaling_unsupervised_3d_object_detection_from_2d_scene.md)**

:   提出 LiSe 方法，将 2D 图像信息引入无监督 3D 目标检测，通过自步学习（self-paced learning）中的自适应采样和弱模型聚合策略，大幅提升远距离和小目标的检测能力。

**[Carformer Self-Driving With Learned Object-Centric Representations](carformer_self-driving_with_learned_object-centric_representations.md)**

:   提出 CarFormer，首次将自监督 slot attention 学到的 object-centric 表征用于自动驾驶，在 CARLA Longest6 基准上超越了使用精确物体属性的 PlanT，同时具备世界模型预测未来状态的能力。

**[Dvlo Deep Visual-Lidar Odometry With Local-To-Global Feature Fusion And Bi-Direc](dvlo_deep_visual-lidar_odometry_with_local-to-global_feature_fusion_and_bi-direc.md)**

:   提出基于聚类的 Local-to-Global 融合网络 DVLO，通过双向结构对齐（图像→伪点云 + 点云→伪图像）解决视觉与 LiDAR 的数据结构不一致问题，在 KITTI 里程计和 FlyingThings3D 场景流任务上均取得 SOTA。

**[Enhancing Vectorized Map Perception With Historical Rasterized Maps](enhancing_vectorized_map_perception_with_historical_rasterized_maps.md)**

:   提出 HRMapNet，通过维护一张低成本的全局历史栅格化地图（historical rasterized map），为在线矢量化地图感知提供互补先验信息，在 BEV 特征聚合和 query 初始化两个层面增强现有方法，在 nuScenes 和 Argoverse 2 上取得显著提升。

**[Equivariant Spatio-Temporal Self-Supervision For Lidar Object Detection](equivariant_spatio-temporal_self-supervision_for_lidar_object_detection.md)**

:   E-SSL3D 提出一种时空联合等变自监督预训练框架，通过空间等变（对旋转用分类目标、对平移/缩放/翻转用对比目标）和时间等变（用 3D 场景流约束相邻帧特征变换一致性）联合训练 3D 特征编码器，在低数据场景下仅用 20% 标注数据就能达到接近 100% 数据从头训练的检测性能。

**[Fsd-Bev Foreground Self-Distillation For Multi-View 3D Object Detection](fsd-bev_foreground_self-distillation_for_multi-view_3d_object_detection.md)**

:   提出前景自蒸馏（FSD）框架，在同一模型内构建教师-学生分支共享图像特征，避免跨模态蒸馏中的分布差异问题，配合点云增强和多尺度前景增强模块，在 nuScenes 上取得 SOTA 性能。

**[Fully Sparse 3D Occupancy Prediction](fully_sparse_3d_occupancy_prediction.md)**

:   提出 SparseOcc，首个完全稀疏的 3D 占用预测网络，通过稀疏体素解码器和掩码引导的 Mask Transformer 实现高效占用预测，并设计了 RayIoU 评价指标解决传统 mIoU 的深度方向不一致惩罚问题。

**[Gaussianformer Scene As Gaussians For Vision-Based 3D Semantic Occupancy Predict](gaussianformer_scene_as_gaussians_for_vision-based_3d_semantic_occupancy_predict.md)**

:   提出以物体为中心的 3D 语义高斯表示替代传统密集体素，用一组稀疏的 3D 语义高斯描述场景并通过高斯到体素的 splatting 生成占用预测，在性能可比的情况下将内存消耗降低 75%-82%。

**[Graphbev Towards Robust Bev Feature Alignment For Multi-Modal 3D Object Detectio](graphbev_towards_robust_bev_feature_alignment_for_multi-modal_3d_object_detectio.md)**

:   针对多模态BEV融合中LiDAR与相机标定误差导致的特征错位问题，提出GraphBEV框架，通过LocalAlign（基于KD-Tree的邻域深度图匹配）和GlobalAlign（可学习偏移量全局对齐）两个模块，在nuScenes上达到70.1% mAP（超BEVFusion 1.6%），在噪声错位场景下超BEVFusion 8.3%。

**[Hierarchical Temporal Context Learning For Camera-Based Semantic Scene Completio](hierarchical_temporal_context_learning_for_camera-based_semantic_scene_completio.md)**

:   针对相机语义场景补全（SSC）中时序信息利用粗糙的问题，提出层级式时序上下文学习（HTCL）范式：先通过跨帧模式亲和度（CPA）度量当前帧与历史帧的细粒度对应关系，再通过基于亲和度的动态精炼（ADR）自适应采样补偿不完整观测，在SemanticKITTI上排名第1，甚至在OpenOccupancy上mIoU超过LiDAR方法。

**[Ittakestwo Leveraging Peer Representations For Semi-Supervised Lidar Semantic Se](ittakestwo_leveraging_peer_representations_for_semi-supervised_lidar_semantic_se.md)**

:   提出IT2框架，通过利用LiDAR数据的对等表示（range image + voxel grid）之间的一致性学习作为新型扰动形式，并引入基于高斯混合模型的跨分布对比学习，大幅提升半监督LiDAR语义分割性能。
