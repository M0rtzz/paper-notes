<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**📷 CVPR2026** · 共 **54** 篇

**[Adaradar Rate Adaptive Spectral Compression For Radar-Based Perception](adaradar_rate_adaptive_spectral_compression_for_radar-based_perception.md)**

:   提出 AdaRadar——基于 DCT 频谱剪枝与零阶代理梯度的在线自适应雷达数据压缩框架，在 100× 以上压缩率下仅损失 ~1%p 检测/分割性能，有效缓解雷达传感器到计算端的带宽瓶颈。

**[BEV-SLD: Self-Supervised Scene Landmark Detection for Global Localization with LiDAR Bird's-Eye View Images](bev-sld_self-supervised_scene_landmark_detection_for_global_localization_with_li.md)**

:   提出BEV-SLD，一种基于自监督场景地标检测(Scene Landmark Detection)的LiDAR全局定位方法，将检测与对应关系预测解耦，仅需20MB即可在多种场景下实现高精度(x, y, azimuth)位姿估计。

**[BuildAnyPoint: 3D Building Structured Abstraction from Diverse Point Clouds](buildanypoint_3d_building_structured_abstraction_from_diverse_point_clouds.md)**

:   提出BuildAnyPoint，通过**松耦合级联扩散Transformer(Loca-DiT)**实现从多样分布的点云（机载LiDAR、SfM、稀疏噪声点云）到结构化3D建筑Mesh的统一重建——先用分层潜在扩散恢复底层点云分布，再用自回归Transformer生成紧凑多边形Mesh。

**[Causalvad De-Confounding End-To-End Autonomous Driving Via Causal Intervention](causalvad_de-confounding_end-to-end_autonomous_driving_via_causal_intervention.md)**

:   提出 CausalVAD，通过将 Pearl 后门调整理论参数化为即插即用模块（SCIS），在 VAD 架构的感知-预测-规划三个阶段进行多级因果干预，消除虚假关联，实现更安全、更鲁棒的端到端自动驾驶。

**[Coin3D Revisiting Configuration-Invariant Multi-Camera 3D Object Detection](coin3d_revisiting_configuration-invariant_multi-camera_3d_object_detection.md)**

:   提出 CoIn3D 框架，通过空间感知特征调制（SFM）和相机感知数据增强（CDA）两个模块，显式建模相机内参/外参/阵列布局的空间先验差异，实现多相机3D检测模型从源配置到未见目标配置的强泛化迁移，适用于 BEVDepth / BEVFormer / PETR 三大主流范式。

**[ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving](colavla_leveraging_cognitive_latent_reasoning_for_hierarchical_parallel_trajecto.md)**

:   ColaVLA 提出统一的视觉-语言-动作(VLA)框架，将 VLM 的推理从文本链式思考迁移到潜空间，通过认知潜空间推理器(Cognitive Latent Reasoner)和层次化并行规划器(Hierarchical Parallel Planner)，仅需两次 VLM 前向传播即可高效完成场景理解与轨迹解码，在 nuScenes 开环和闭环评测上均达到 SOTA。

**[CoLC: Communication-Efficient Collaborative Perception with LiDAR Completion](colc_communication-efficient_collaborative_perception_with_lidar_completion.md)**

:   CoLC 提出一种通信高效的早期协同感知框架，通过前景感知点采样(FAPS)减少传输量，结合 VQ-based LiDAR 补全(CEEF)在 ego 端恢复稠密 pillar 表示，并用稠密引导双对齐(DGDA)保证语义和几何一致性，在大幅降低通信带宽的同时保持甚至超越早期融合的检测性能。

**[Composing Driving Worlds through Disentangled Control for Adversarial Scenario Generation](composing_driving_worlds_through_disentangled_cont.md)**

:   提出 CompoSIA，一个基于 Wan2.1 DiT 的组合式驾驶视频模拟器，通过对场景结构（3D bbox）、物体身份（单张参考图）和自车动作（相机轨迹）三因素的显式解耦注入，实现对抗性驾驶场景的细粒度可控生成，碰撞率提升 173%。

**[CompoSIA: Composing Driving Worlds through Disentangled Control for Adversarial Scenario Generation](composing_driving_worlds_through_disentangled_control_for_adversarial_scenario_g.md)**

:   提出CompoSIA框架，通过对结构(Structure)、身份(Identity)、动作(Action)三因素的解耦控制，基于视频扩散模型生成可组合的对抗驾驶场景，实现身份编辑FVD降低17%、下游planner碰撞率提升173%，有效暴露自动驾驶系统的隐藏失败模式。

**[Cyclebev Regularizing View Transformation Networks Via View Cycle Consistency Fo](cyclebev_regularizing_view_transformation_networks_via_view_cycle_consistency_fo.md)**

:   提出 CycleBEV 正则化框架：训练时引入逆视角变换（IVT）网络将 BEV 分割图映射回透视图（PV）分割图，通过循环一致性损失及高度感知几何正则化、跨视角隐空间对齐两项新目标来增强现有 BEV 语义分割模型，推理时不增加任何开销。

**[Dr.Occ: Depth- and Region-Guided 3D Occupancy from Surround-View Cameras for Autonomous Driving](drocc_depth-_and_region-guided_3d_occupancy_from_surround-view_cameras_for_auton.md)**

:   Dr.Occ 提出深度引导与区域引导的统一 3D 占用预测框架，通过 D2-VFormer 利用 MoGe-2 的高质量深度先验实现精确的 2D→3D 几何映射，并通过 R/R2-EFormer 借鉴 MoE/MoR 思想自适应分配区域专家处理空间语义各向异性，在 BEVDet4D 基线上提升 7.43% mIoU。

**[Dr.Occ: Depth- and Region-Guided 3D Occupancy from Surround-View Cameras](drocc_depth_region_guided_3d_occupancy.md)**

:   针对视角变换几何不对齐和语义类别空间各向异性不平衡，提出深度引导双投影视角变换器（D²-VFormer）利用MoGe-2构建非空体素掩码，和区域引导专家Transformer（R/R²-EFormer）自适应分配空间模型容量，BEVDet4D上提升7.43% mIoU。

**[EMDUL: Expanding mmWave Datasets for Human Pose Estimation with Unlabeled Data and LiDAR Datasets](expanding_mmwave_datasets_for_human_pose_estimation_with_unlabeled_data_and_lida.md)**

:   提出 EMDUL 管线，通过伪标签标注无标注毫米波数据（含新设计的无监督时序一致性损失 UTCL）和闭式 LiDAR→mmWave 点云转换器（含基于流的点过滤 FPF），大幅扩展毫米波 HPE 数据集的规模与多样性，域内误差降低 15.1%、跨域误差降低 18.9%。

**[FoSS: Modeling Long-Range Dependencies and Multimodal Uncertainty in Trajectory Prediction via Fourier–State Space Integration](foss_modeling_long_range_dependencies_and_multimodal_uncertainty_in_trajectory_p.md)**

:   FoSS 提出一种频域-时域双分支框架，通过渐进螺旋重排序（HelixSort）将傅里叶频谱有序化后输入选择性状态空间模型（SSM），结合时域动态 SSM 和交叉注意力融合，在 Argoverse 1/2 上取得 SOTA 轨迹预测精度，同时参数量减少 40%+、推理延迟降低 22%。

**[Generalizing Visual Geometry Priors to Sparse Gaussian Occupancy Prediction](generalizing_visual_geometry_priors_to_sparse_gaussian_occupancy_prediction.md)**

:   GPOcc 提出利用可泛化的视觉几何先验（如 VGGT、DepthAnything）进行单目 3D 占据预测，通过沿相机射线向内延伸表面点生成体积采样，以稀疏高斯基元进行概率占据推断，并设计免训练增量更新策略处理流式输入，在 Occ-ScanNet 上单目 mIoU 提升 +9.99、流式提升 +11.79 超越前 SOTA，同时在相同深度先验下速度快 2.65 倍。

**[HG-Lane: High-Fidelity Generation of Lane Scenes under Adverse Weather and Lighting Conditions without Re-annotation](hg-lane_high-fidelity_generation_of_lane_scenes_under_adverse_weather_and_lighti.md)**

:   针对车道检测数据集（CULane/TuSimple）极端天气样本严重不足的问题，提出HG-Lane——一个无需重标注的两阶段扩散生成框架：Stage-I通过Control Information Fusion+Structure-aware Reverse Diffusion保留车道几何结构，Stage-II通过Appearance-aware Refinement调整光照风格，生成snow/rain/fog/night/dusk共30K图。CLRNet整体mF1提升+20.87%，snow场景+38.8%。

**[Horizonforge Driving Scene Editing With Any Trajectories And Any Vehicles](horizonforge_driving_scene_editing_with_any_trajectories_and_any_vehicles.md)**

:   HorizonForge 提出一个统一框架，将驾驶场景重建为可编辑的 Gaussian Splats + Mesh 表示，通过轨迹控制实现精细 3D 操控和语言驱动的车辆插入，再经视频扩散模型渲染生成时空一致的高质量驾驶视频，在用户偏好率上以 91.02% 碾压所有对比方法。

**[KnowVal: A Knowledge-Augmented and Value-Guided Autonomous Driving System](knowval_a_knowledge-augmented_and_value-guided_autonomous_driving_system.md)**

:   提出KnowVal端到端自驾系统，通过三大核心解决知识推理和价值对齐缺失：(1)Retrieval-guided Open-world Perception融合标准3D检测+VL-SAMv2长尾物体+VLM场景理解；(2)Perception-guided Knowledge Retrieval从驾驶知识图谱（交通法/防御驾驶/道德规范）检索相关知识；(3)World Model预测未来状态+Value Model（human-preference训练）评估轨迹价值，实现可解释决策。nuScenes最低碰撞率，Bench2Drive/NVISIM SOTA。

**[Learnability-Driven Submodular Optimization for Active Roadside 3D Detection](learnability-driven_submodular_optimization_for_active_roadside_3d_detection.md)**

:   提出 LH3D 框架，通过「深度置信度→语义平衡→几何多样性」三阶段子模优化的主动学习策略，抑制路侧单目 3D 检测中固有歧义样本的选取，仅用 20% 标注预算即显著优于传统不确定性/多样性 AL 方法。

**[Learning Geometric and Photometric Features from Panoramic LiDAR Scans for Outdoor Place Categorization](learning_geometric_and_photometric_features_from_p.md)**

:   构建大规模室外场景数据集MPO（含Velodyne稀疏和FARO稠密两种LiDAR点云），提出结合水平循环卷积(HCC)和行级最大池化(RWMP)的CNN架构，利用全景深度图和反射率图的多模态融合（Softmax Average），在6类室外场景分类上达97.87%准确率，显著超越传统手工特征方法。

**[Learning Geometric and Photometric Features from Panoramic LiDAR Scans for Outdoor Place Categorization](learning_geometric_and_photometric_features_from_panoramic_lidar_scans_for_outdo.md)**

:   提出利用LiDAR全景深度图和反射率图作为CNN输入进行室外场景分类的方法，构建了MPO大规模室外3D数据集（6类场景，34200帧），通过水平循环卷积(HCC)和行级最大池化(RWMP)处理全景图的环状结构，在多模态融合下达到97.47%分类准确率。

**[Learning Mutual View Information Graph for Adaptive Adversarial Collaborative Perception](learning_mutual_view_information_graph_for_adaptive_adversarial_collaborative_pe.md)**

:   提出 MVIG 攻击框架，通过将不同防御型协作感知系统的脆弱性统一建模为互视图信息图(Mutual View Information Graph)，结合时序图学习与熵感知漏洞搜索，实现自适应的伪造攻击，使防御成功率最高下降 62%。

**[Learning to Drive is a Free Gift: Large-Scale Label-Free Autonomy Pretraining from Unposed In-The-Wild Videos](learning_to_drive_is_a_free_gift_large-scale_label-free_autonomy_pretraining_fro.md)**

:   提出LFG（Learning to drive is a Free Gift），一个完全无标签、教师引导的自动驾驶预训练框架，从大规模无姿态YouTube驾驶视频中学习几何、语义和运动感知的统一伪4D表示，在NAVSIM基准上仅用单目前视相机即超越多相机+LiDAR的BEV方法（PDMS 85.2），并展示了出色的数据效率（10%标签即达81.4 PDMS）。

**[LiREC-Net: A Target-Free and Learning-Based Network for LiDAR, RGB, and Event Calibration](lirec-net_a_target-free_and_learning-based_network_for_lidar_rgb_and_event_calib.md)**

:   提出LiREC-Net，首个统一框架同时完成LiDAR-RGB和LiDAR-Event相机的无靶标外参标定，通过共享LiDAR表示（融合3D点特征和投影深度特征）和成对代价体积实现跨模态对齐，在KITTI上达到1.80cm/0.11°、DSEC上达到2.51cm/0.14°（LiDAR-RGB）和1.18cm/0.07°（LiDAR-Event）的标定精度。

**[Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection](look_before_you_fuse_2d-guided_cross-modal_alignment_for_robust_3d_detection.md)**

:   揭示了LiDAR-Camera融合中特征不对齐主要集中在**前景-背景深度突变边界**，提出PGDC（2D先验引导深度校准）+DAGF（不连续感知几何融合）+SGDM（结构引导深度调制器）三个协同模块，在融合前主动修正不对齐问题，在nuScenes验证集达到mAP 71.5%、NDS 73.6%的SOTA。

**[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](lr-sgs_robust_lidar-reflectance-guided_salient_gaussian_splatting_for_self-drivi.md)**

:   LR-SGS 提出利用 LiDAR 反射率引导的结构感知 Salient Gaussian 表示，通过将 LiDAR 强度校准为光照不变的反射率通道附加到每个 Gaussian、从几何与反射率特征点初始化结构化 Salient Gaussian、以及 RGB-反射率跨模态梯度一致性约束，在 Waymo 数据集的复杂光照场景中以更少 Gaussian 数量和更短训练时间超越 OmniRe 达 1.18 dB PSNR。

**[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](lrsgs_robust_lidarreflectanceguided_salient_gaussi.md)**

:   提出LR-SGS，将LiDAR强度校准为光照不变的反射率通道附加到3D高斯体上，并设计结构感知的Salient Gaussian表示（从LiDAR几何和反射率特征点初始化）配合改进的密度控制和显著变换策略，在Waymo自动驾驶复杂场景中实现优于OmniRe的高保真重建，且高斯体更少、训练更快。

**[M²-Occ: Resilient 3D Semantic Occupancy Prediction for Autonomous Driving with Incomplete Camera Inputs](m2occ_resilient_3d_semantic_occupancy_prediction_f.md)**

:   针对自动驾驶中相机故障导致的不完整输入问题，提出M²-Occ框架，通过多视角掩码重建（MMR）利用相邻相机重叠视场恢复缺失特征，并引入特征记忆模块（FMM）用类级语义原型精化体素表示，在缺失后视摄像头时IoU提升4.93%，不影响全视角性能。

**[MetaDAT: Generalizable Trajectory Prediction via Meta Pre-training and Data-Adaptive Test-Time Updating](metadat_generalizable_trajectory_prediction_via_me.md)**

:   提出MetaDAT框架，通过元学习预训练获得适合在线适应的模型初始化，并在测试时采用动态学习率优化和困难样本驱动更新来实现跨数据集分布偏移下的轨迹预测自适应，在nuScenes/Lyft/Waymo多种跨域配置下全面超越现有TTT方法。

**[MetaDAT: Generalizable Trajectory Prediction via Meta Pre-training and Data-Adaptive Test-Time Updating](metadat_generalizable_trajectory_prediction_via_meta_pre-training_and_data-adapt.md)**

:   提出 MetaDAT 框架，通过元预训练获得适合在线自适应的模型初始化，并在测试时利用动态学习率优化和难样本驱动更新实现数据自适应的模型调整，在 nuScenes/Lyft/Waymo 跨数据集分布偏移场景下超越所有 TTT 方法。

**[MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving](minddriver_introducing_progressive_multimodal_reasoning_for_autonomous_driving.md)**

:   提出渐进式多模态推理框架 MindDriver，模仿人类"感知→想象→行动"机制——先文本语义理解，再想象未来场景图像（桥接语义和物理空间），最后预测轨迹，配合反馈引导数据标注和渐进式强化微调，在 nuScenes 开环和 Bench2Drive 闭环评估上均取得最优表现。

**[Monocular Open Vocabulary Occupancy Prediction for Indoor Scenes (LegoOcc)](monocular_open_vocabulary_occupancy_prediction_for_indoor_scenes.md)**

:   提出 LegoOcc，利用语言嵌入高斯（LE-Gaussians）作为统一的几何-语义中间表示，结合基于 Poisson 过程的高斯到占用（G2O）算子和渐进温度衰减策略，在仅使用二值占用标签（无语义标注）的情况下实现室内场景的单目开放词汇占用预测，在 Occ-ScanNet 上达到 59.50 IoU / 21.05 mIoU。

**[MoVieDrive: Urban Scene Synthesis with Multi-Modal Multi-View Video Diffusion Transformer](moviedrive_multimodal_multiview_video_diffusion.md)**

:   提出 MoVieDrive，首个在统一框架下实现多模态（RGB+深度+语义）多视图自动驾驶场景视频生成的扩散 Transformer 方法，通过模态共享层+模态特定层的设计和多样化条件编码，在 nuScenes 上 FVD 达到 46.8（领先 SOTA 22%），同时生成高质量的深度图和语义图。

**[MoVieDrive: Urban Scene Synthesis with Multi-Modal Multi-View Video Diffusion Transformer](moviedrive_urban_scene_synthesis_with_multi-modal_multi-view_video_diffusion_tra.md)**

:   MoVieDrive 提出统一的多模态多视图视频扩散 Transformer，通过 modal-shared + modal-specific 的双层架构设计，在单一模型中同时生成 RGB 视频、深度图和语义图，配合多样的条件输入（文本、布局、上下文参考），在 nuScenes 上取得 FVD 46.8（SOTA），同时实现跨模态一致的高质量驾驶场景合成。

**[NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning](nord_a_data-efficient_vision-language-action_model_that_drives_without_reasoning.md)**

:   NoRD 证明自动驾驶 VLA 不需要大规模推理标注和海量数据：通过识别 GRPO 在弱 SFT 策略上失败的根因是 **difficulty bias**（高方差 rollout 组的学习信号被压制），采用 Dr. GRPO 替代标准 GRPO 做 RL 后训练，仅用 <60% 数据、无推理标注、3× 更少 token，在 NAVSIM（85.6 PDMS）和 WaymoE2E（7.709 RFS）上达到与推理型 VLA 竞争的性能。

**[O3N: Omnidirectional Open-Vocabulary Occupancy Prediction](o3n_omnidirectional_open-vocabulary_occupancy_prediction.md)**

:   O3N 首次提出全向开放词汇占用预测任务，设计纯视觉端到端框架：Polar-spiral Mamba (PsM) 在极坐标空间以螺旋扫描建模全景几何连续性；Occupancy Cost Aggregation (OCA) 构建 voxel-text 匹配代价体积避免直接特征对齐的过拟合；Natural Modality Alignment (NMA) 通过无梯度随机游走对齐 pixel-voxel-text 三模态嵌入。在 QuadOcc 上达 16.54 mIoU / 21.16 Novel mIoU（SOTA），大幅超越 OVO 基线。

**[O3N: Omnidirectional Open-Vocabulary Occupancy Prediction](o3n_omnidirectional_openvocabulary_occupancy_predi.md)**

:   提出O3N——首个纯视觉端到端全向开放词汇占用预测框架，通过极坐标螺旋Mamba（PsM）、占用代价聚合（OCA）和无梯度自然模态对齐（NMA）三大模块，在QuadOcc和Human360Occ上实现SOTA。

**[On the Feasibility and Opportunity of Autoregressive 3D Object Detection](on_the_feasibility_and_opportunity_of_autoregressive_3d_object_detection.md)**

:   提出 AutoReg3D，首个将 LiDAR 3D 目标检测建模为自回归序列生成的框架，利用近到远排序和参数特定词表将 bounding box 离散为 token 序列，无需 anchor/NMS 即可达到与主流方法竞争的性能，并解锁 RL 微调和级联精炼等新能力。

**[OneOcc: Semantic Occupancy Prediction for Legged Robots with a Single Panoramic Camera](oneocc_semantic_occupancy_prediction_for_legged_robots_with_a_single_panoramic_c.md)**

:   提出 OneOcc，一个面向足式/人形机器人的纯视觉全景语义占用预测框架，通过双投影融合、双网格体素化、步态位移补偿和层级混合专家解码器，仅用单个全景相机即可实现 360° 语义场景补全，在真实四足和仿真人形数据集上超越 LiDAR 基线。

**[Panoramic Multimodal Semantic Occupancy Prediction for Quadruped Robots](panoramic_multimodal_semantic_occupancy_prediction.md)**

:   面向四足机器人构建首个全景多模态（RGB+热成像+偏振+LiDAR）语义占据数据集PanoMMOcc，并提出VoxelHound框架，通过垂直抖动补偿（VJC）和多模态信息提示融合（MIPF）模块实现鲁棒的3D占据预测，达到23.34% mIoU（+4.16%）。

**[Panoramic Multimodal Semantic Occupancy Prediction For Quadruped Robots](panoramic_multimodal_semantic_occupancy_prediction_for_quadruped_robots.md)**

:   提出首个面向四足机器人的全景多模态语义占据预测数据集 PanoMMOcc 及框架 VoxelHound，通过垂直抖动补偿（VJC）和多模态信息提示融合（MIPF）模块，在全景 RGB+热成像+偏振+LiDAR 四模态下达到 23.34% mIoU，超越已有方法 +4.16%。

**[Perception Characteristics Distance Measuring Stability And Robustness Of Percep](perception_characteristics_distance_measuring_stability_and_robustness_of_percep.md)**

:   提出 Perception Characteristics Distance (PCD)，一种量化感知系统在不同距离下可靠检测能力的新指标，通过统计建模检测置信度随距离的均值和方差变化，定义感知系统的最大可靠检测距离，弥补传统 AP/IoU 等静态指标无法反映距离依赖性和随机性的不足。

**[Points-to-3D: Structure-Aware 3D Generation with Point Cloud Priors](points-to-3d_structure-aware_3d_generation_with_point_cloud_priors.md)**

:   提出 Points-to-3D，将可见区域点云编码为 TRELLIS 的稀疏结构潜变量（SS latent）并用 mask-aware inpainting 网络补全不可见区域，结合结构补全+边界精炼两阶段采样策略，实现几何可控的高保真 3D 资产/场景生成，在 Toys4K 上 F-Score 达 0.964（可见区域 0.998）。

**[R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection](r4det_4d_radar-camera_fusion_for_high-performance_3d_object_detection.md)**

:   提出 R4Det，通过三个即插即用 BEV 模块——全景深度融合（PDF）、可变形门控时序融合（DGTF）、实例引导动态精炼（IGDR）——系统性解决 4D 雷达-相机融合中的深度估计不准、无位姿时序融合以及小目标检测三大难题，在 TJ4DRadSet 上 3D mAP 达 47.29%（+5.47%），VoD 上 mAP 66.69%。

**[Recover To Predict Progressive Retrospective Learning For Variable-Length Trajec](recover_to_predict_progressive_retrospective_learning_for_variable-length_trajec.md)**

:   提出渐进式回溯框架 PRF，通过级联回溯单元逐步将不完整观测的特征对齐到完整观测，大幅提升变长轨迹预测性能，且即插即用兼容现有方法。

**[RESBev: Making BEV Perception More Robust](resbev_making_bev_perception_more_robust.md)**

:   提出RESBev——一个即插即用的BEV感知鲁棒性增强框架，通过隐空间世界模型从历史干净帧预测当前BEV语义先验，再与被损坏的当前观测融合，在nuScenes上显著提升四种LSS模型在10种干扰下的平均IoU（+15~20个点）。

**[Saber Spatially Consistent 3D Universal Adversarial Objects For Bev Detectors](saber_spatially_consistent_3d_universal_adversarial_objects_for_bev_detectors.md)**

:   提出首个面向BEV 3D检测器的非侵入式、3D一致的通用对抗物体生成框架SABER，通过在场景中放置优化后的3D mesh来干扰多视角多帧检测，揭示BEV模型对环境上下文先验的过度依赖。

**[SG-NLF: Spectral-Geometric Neural Fields for Pose-Free LiDAR View Synthesis](sgnlf_spectralgeometric_neural_fields_for_posefre.md)**

:   SG-NLF提出一种无需精确位姿的LiDAR NeRF框架，通过谱-几何混合表示解决LiDAR稀疏数据导致的几何空洞问题，利用置信感知图实现全局位姿优化，并引入对抗学习强化跨帧一致性，在nuScenes上重建质量和位姿精度分别比SOTA提升35.8%和68.8%。

**[Single Pixel Image Classification using an Ultrafast Digital Light Projector](single_pixel_image_classification_using_an_ultrafa.md)**

:   利用microLED-on-CMOS超快光投影器(330kfps)进行单像素成像(SPI)，以12×12 Hadamard pattern照明MNIST数字并用单像素检测器采集时间序列，完全跳过图像重建，直接用ELM/DNN分类实测光信号，实现1.2kfps下>90%分类精度，二分类(异常检测)精度>99%。

**[TT-Occ: Test-Time 3D Occupancy Prediction](test-time_3d_occupancy_prediction.md)**

:   提出 TT-Occ，一种无需预训练的测试时3D占用预测框架，通过在推理时集成视觉基础模型（VFMs）来增量构建、优化和体素化时间感知的3D高斯，在 Occ3D-nuScenes 和 nuCraft 上超越了所有需要大量训练的自监督方法。

**[Towards Balanced Multi-Modal Learning in 3D Human Pose Estimation](towards_balanced_multimodal_learning_in_3d_human_p.md)**

:   提出基于Shapley值的模态贡献评估+Fisher信息矩阵引导的自适应权重约束(AWC)正则化方法，解决RGB/LiDAR/mmWave/WiFi四模态融合中的模态不平衡问题，在MM-Fi数据集上MPJPE比naive fusion降低2.71mm，比最佳balancing方法降低约5mm，且不引入额外可学参数。

**[U4D: Uncertainty-Aware 4D World Modeling from LiDAR Sequences](u4d_uncertainty-aware_4d_world_modeling_from_lidar_sequences.md)**

:   提出 U4D，首个不确定性感知的 4D LiDAR 世界建模框架，通过"先难后易"的两阶段扩散生成策略，先重建高不确定性区域再条件补全整个场景，并设计 MoST 模块自适应融合时空特征以保证时序一致性。

**[VIRD: View-Invariant Representation through Dual-Axis Transformation for Cross-View Pose Estimation](vird_view-invariant_representation_through_dual-axis_transformation_for_cross-vi.md)**

:   提出 VIRD，通过双轴变换（极坐标变换 + 上下文增强位置注意力）构建视图不变表示，在无方向先验条件下实现 SOTA 的跨视角位姿估计，在 KITTI 上位置和方向误差分别降低 50.7% 和 76.5%。

**[Walkgpt Grounded Vision-Language Conversation With Depth-Aware Segmentation For ](walkgpt_grounded_vision-language_conversation_with_depth-aware_segmentation_for_.md)**

:   提出 WalkGPT——首个面向行人无障碍导航的像素定位大视觉语言模型，统一对话推理、分割掩码与深度估计于单一架构中，并构建了 41k 规模的 PAVE 数据集。
