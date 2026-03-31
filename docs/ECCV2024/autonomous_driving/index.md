<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**🎞️ ECCV2024** · 共 **17** 篇

**[4D Contrastive Superflows are Dense 3D Representation Learners](4d_contrastive_superflows_are_dense_3d_representation_learners.md)**

:   提出SuperFlow框架，通过视图一致性对齐、稠密-稀疏一致性正则化、和基于流的时空对比学习三个模块，利用连续LiDAR-相机对建立4D预训练目标，在11个异构LiDAR数据集上全面超越了之前的Image-to-LiDAR预训练方法。

**[Accelerating Online Mapping and Behavior Prediction via Direct BEV Feature Attention](accelerating_online_mapping_and_behavior_prediction_via_dire.md)**

:   提出直接将在线地图估计模型内部的BEV特征暴露给下游轨迹预测模型（而非仅传递解码后的矢量化地图），通过三种BEV特征注入策略实现推理加速最高73%、预测精度提升最高29%。

**[Adaptive Human Trajectory Prediction via Latent Corridors](adaptive_human_trajectory_prediction_via_latent_corridors.md)**

:   将prompt tuning思想引入行人轨迹预测，通过在预训练轨迹预测器的输入端添加可学习的低秩图像prompt（称为latent corridors），以不到0.1%的额外参数实现对部署场景特定行为模式的高效自适应，在合成和真实数据上分别取得最高23.9%和26.8%的ADE提升。

**[Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene](approaching_outside_scaling_unsupervised_3d_object_detection_from_2d_scene.md)**

:   提出 LiSe 方法，将 2D 图像信息引入无监督 3D 目标检测，通过自步学习（self-paced learning）中的自适应采样和弱模型聚合策略，大幅提升远距离和小目标的检测能力。

**[CarFormer: Self-Driving with Learned Object-Centric Representations](carformer_self-driving_with_learned_object-centric_representations.md)**

:   提出 CarFormer，首次将自监督 slot attention 学到的 object-centric 表征用于自动驾驶，在 CARLA Longest6 基准上超越了使用精确物体属性的 PlanT，同时具备世界模型预测未来状态的能力。

**[DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion and Bi-directional Structure Alignment](dvlo_deep_visual-lidar_odometry_with_local-to-global_feature_fusion_and_bi-direc.md)**

:   提出基于聚类的 Local-to-Global 融合网络 DVLO，通过双向结构对齐（图像→伪点云 + 点云→伪图像）解决视觉与 LiDAR 的数据结构不一致问题，在 KITTI 里程计和 FlyingThings3D 场景流任务上均取得 SOTA。

**[DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion and Bi-Directional Structure Alignment](dvlo_deep_visuallidar_odometry_with_localtoglobal_featu.md)**

:   提出 DVLO——基于从局部到全局融合 + 双向结构对齐的视觉-LiDAR 里程计网络，通过将图像视为伪点云进行局部聚类融合、将点云投影为伪图像进行全局自适应融合，解决了两种模态间固有的数据结构不一致问题。

**[Enhancing Vectorized Map Perception with Historical Rasterized Maps](enhancing_vectorized_map_perception_with_historical_rasterized_maps.md)**

:   提出 HRMapNet，通过维护一张低成本的全局历史栅格化地图（historical rasterized map），为在线矢量化地图感知提供互补先验信息，在 BEV 特征聚合和 query 初始化两个层面增强现有方法，在 nuScenes 和 Argoverse 2 上取得显著提升。

**[Equivariant Spatio-Temporal Self-Supervision for LiDAR Object Detection](equivariant_spatio-temporal_self-supervision_for_lidar_object_detection.md)**

:   E-SSL3D 提出一种时空联合等变自监督预训练框架，通过空间等变（对旋转用分类目标、对平移/缩放/翻转用对比目标）和时间等变（用 3D 场景流约束相邻帧特征变换一致性）联合训练 3D 特征编码器，在低数据场景下仅用 20% 标注数据就能达到接近 100% 数据从头训练的检测性能。

**[FSD-BEV: Foreground Self-Distillation for Multi-View 3D Object Detection](fsd-bev_foreground_self-distillation_for_multi-view_3d_object_detection.md)**

:   提出前景自蒸馏（FSD）框架，在同一模型内构建教师-学生分支共享图像特征，避免跨模态蒸馏中的分布差异问题，配合点云增强和多尺度前景增强模块，在 nuScenes 上取得 SOTA 性能。

**[Fully Sparse 3D Occupancy Prediction](fully_sparse_3d_occupancy_prediction.md)**

:   提出 SparseOcc，首个完全稀疏的 3D 占用预测网络，通过稀疏体素解码器和掩码引导的 Mask Transformer 实现高效占用预测，并设计了 RayIoU 评价指标解决传统 mIoU 的深度方向不一致惩罚问题。

**[GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction](gaussianformer_scene_as_gaussians_for_vision-based_3d_semantic_occupancy_predict.md)**

:   提出以物体为中心的 3D 语义高斯表示替代传统密集体素，用一组稀疏的 3D 语义高斯描述场景并通过高斯到体素的 splatting 生成占用预测，在性能可比的情况下将内存消耗降低 75%-82%。

**[LiDAR-Event Stereo Fusion with Hallucinations](lidarevent_stereo_fusion_with_hallucinations.md)**

:   首次探索 LiDAR 与事件立体相机的融合，提出虚拟堆叠幻觉（VSH）和回溯时间幻觉（BTH）两种策略，通过在事件流/堆叠中注入虚拟事件来增强匹配可辨别性，大幅提升事件立体匹配精度。

**[Navigation Instruction Generation with BEV Perception and Large Language Models](navigation_instruction_generation_with_bev.md)**

:   提出 BEVInstructor，将鸟瞰图 (BEV) 特征融入多模态大语言模型 (MLLM) 用于导航指令生成，通过 Perspective-BEV 视觉编码、参数高效 prompt tuning 和实例引导的迭代精化，在室内外多个数据集上全面超越 SOTA。

**[OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving](occgen_generative_multimodal_3d_occupancy_prediction_for_aut.md)**

:   提出OccGen，首次将扩散模型的"噪声到占据"生成范式引入3D语义占据预测任务，通过条件编码器+渐进式精炼解码器实现由粗到精的占据图生成，在nuScenes-Occupancy上多模态/纯LiDAR/纯相机设置下分别提升mIoU 9.5%/6.3%/13.3%。

**[Reason2Drive: Towards Interpretable and Chain-Based Reasoning for Autonomous Driving](reason2drive_towards_interpretable_and_chainbased_reasoning.md)**

:   构建 Reason2Drive 基准数据集（600K+ 视频-文本对，覆盖感知-预测-推理链式任务），提出 ADRScore 评估链式推理正确性的新指标，并设计 Prior Tokenizer + Instructed Vision Decoder 框架增强 VLM 的目标级感知和推理能力，在自动驾驶推理任务上显著超越所有基线。

**[VisionTrap: Vision-Augmented Trajectory Prediction Guided by Textual Descriptions](visiontrap_visionaugmented_trajectory_prediction_guided.md)**

:   提出 VisionTrap，利用环视相机视觉输入和 VLM/LLM 生成的文本描述作为训练监督，增强自动驾驶场景下的多智能体轨迹预测，同时保持 53ms 实时推理速度。
