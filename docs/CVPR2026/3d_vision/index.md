<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**📷 CVPR2026** · 共 **88** 篇

**[4DEquine: Disentangling Motion and Appearance for 4D Equine Reconstruction from Monocular Video](4dequine_disentangling_motion_and_appearance_for_4.md)**

:   将马科动物4D重建解耦为运动估计(AniMoFormer时空Transformer+后优化)和外观重建(EquineGS前馈3DGS)两个子任务，用VAREN参数化模型做桥梁，仅在合成数据(VarenPoser+VarenTex)上训练即在真实数据APT-36K和AiM上达到SOTA，并能零样本泛化到斑马和驴。

**[A Prediction-as-Perception Framework for 3D Object Detection](a_prediction-as-perception_framework_for_3d_object_detection.md)**

:   受人脑"预测性感知"机制启发，提出 PAP 框架——将历史帧的轨迹预测结果作为 query 注入当前帧的感知模块，在 UniAD 上实现跟踪精度提升 10%、推理速度提升 15%。

**[A Prediction-as-Perception Framework for 3D Object Detection](a_predictionasperception_framework_for_3d_object_d.md)**

:   借鉴人类"预判目标位置再聚焦观察"的认知模式，将前一帧的轨迹预测结果转化为当前帧的检测query，形成预测-感知迭代闭环，在UniAD上实现跟踪精度+10%和推理速度+15%的同步提升。

**[GAP: Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation](action-geometry_prediction_with_3d_geometric_prior_for_bimanual_manipulation.md)**

:   GAP利用预训练3D几何基础模型（π³）提取3D特征，融合2D语义和本体感知，通过条件扩散联合预测未来动作序列和未来3D pointmap，在RoboTwin 2.0和真实双臂实验中达到SOTA。

**[AnyPcc: Compressing Any Point Cloud with a Single Universal Model](anypcc_compressing_any_point_cloud_with_a_single_universal_model.md)**

:   提出 AnyPcc，通过 Universal Context Model（融合空间+通道双粒度先验）和 Instance-Adaptive Fine-Tuning（实例自适应微调）策略，用单一模型在 15 个多样化数据集上实现 SOTA 点云几何压缩，相比 G-PCC v23 获得 ~12% 的码率增益。

**[AVA-Bench: Atomic Visual Ability Benchmark for Vision Foundation Models](ava-bench_atomic_visual_ability_benchmark_for_vision_foundation_models.md)**

:   提出 AVA-Bench，首个将视觉基础模型（VFM）的能力解耦为 14 种原子视觉能力（AVA）的系统性评测基准，通过训练-测试分布对齐和单一能力隔离测试，精准定位 VFM 的强项与短板，并发现 0.5B 小模型即可保持与 7B 模型相当的 VFM 排名一致性。

**[AVA-Bench: Atomic Visual Ability Benchmark for Vision Foundation Models](ava_bench_atomic_visual_ability_vfm.md)**

:   提出 AVA-Bench，将视觉基础模型(VFM)的评估分解为14种"原子视觉能力"(AVA)，通过训练/测试分布对齐和单能力隔离测试，精确定位 VFM 的优势和短板，发现0.5B的LLM就能保持与7B相同的VFM排名，评估成本降低8倍。

**[BRepGaussian: CAD Reconstruction from Multi-View Images with Gaussian Splatting](brepgaussian_cad_reconstruction_from_multi-view_images_with_gaussian_splatting.md)**

:   BRepGaussian 首次实现了从多视图图像直接重建完整 B-rep CAD 模型，通过两阶段的 2D 高斯泼溅学习边缘和面片特征，再经参数化拟合生成水密的边界表示，无需点云监督。

**[Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](catalyst4d_high-fidelity_3d-to-4d_scene_editing_via_dynamic_propagation.md)**

:   提出Catalyst4D框架，将高质量的3D静态编辑结果通过锚点运动引导（AMG）和颜色不确定性外观精炼（CUAR）两个模块传播到4D动态高斯场景中，实现时空一致的高保真动态场景编辑。

**[Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](catalyst4d_highfidelity_3dto4d_scene_editing_via_d.md)**

:   提出Catalyst4D框架，通过锚点运动引导(AMG)和颜色不确定性外观精炼(CUAR)两个模块，将高质量的3D静态编辑结果传播到动态4D高斯场景中，避免了直接4D编辑的运动伪影和时间不一致问题。

**[Changes in Real Time: Online Scene Change Detection with Multi-View Fusion](changes_in_real_time_online_scene_change_detection_with_multi-view_fusion.md)**

:   提出首个同时具备在线、姿态无关、无标注、多视角一致性的场景变化检测（SCD）方法，通过自监督融合损失将像素级和特征级变化线索集成到 3DGS 变化表示中，在超过 10 FPS 的实时速率下超越了所有已有离线方法的检测精度。

**[CLIPoint3D: Language-Grounded Few-Shot Unsupervised 3D Point Cloud Domain Adaptation](clipoint3d_language-grounded_few-shot_unsupervised_3d_point_cloud_domain_adaptat.md)**

:   首个基于 CLIP 的少样本无监督 3D 点云域自适应框架，通过知识驱动的 prompt tuning、参数高效微调、熵引导视图选取和不确定性感知对齐损失，在 PointDA-10 和 GraspNetPC-10 上以仅 ~11M 可训练参数取得 3-16% 的一致性精度提升。

**[Cmhanet A Cross-Modal Hybrid Attention Network For Point Cloud Registration](cmhanet_a_cross-modal_hybrid_attention_network_for_point_cloud_registration.md)**

:   提出 CMHANet，通过跨模态混合注意力机制将 2D 图像纹理语义特征与 3D 点云几何特征深度融合，结合对比学习优化函数，在 3DMatch/3DLoMatch 上实现 SOTA 点云配准性能。

**[CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration](cmhanet_a_crossmodal_hybrid_attention_network_for.md)**

:   提出CMHANet，通过三阶段混合注意力（几何self-attention→图像aggregation-attention→源-目标cross-attention）融合2D图像纹理语义与3D点云几何信息，并引入跨模态对比损失，在3DMatch/3DLoMatch上达到最优配准性能。

**[Coherent Human-Scene Reconstruction from Multi-Person Multi-View Video in a Single Pass](coherent_human-scene_reconstruction_from_multi-person_multi-view_video_in_a_sing.md)**

:   提出CHROMM统一框架，从多人多视图视频中一次性联合估计相机参数、场景点云和人体网格（SMPL-X），无需外部模块或预处理数据，在全局人体运动估计和多视图位姿估计任务上取得竞争力性能，且比优化方法快8倍以上。

**[Coherent Human-Scene Reconstruction from Multi-Person Multi-View Video in a Single Pass](coherent_humanscene_reconstruction_from_multiperso.md)**

:   提出 CHROMM 统一框架，从多人多视图视频中一次性联合估计相机参数、场景点云和人体网格，无需外部模块或预处理数据，在 RICH 上 WA-MPJPE 达 53.1mm 且比优化方法快 8 倍以上。

**[Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation](context-nav_context-driven_exploration_and_viewpoint-aware_3d_spatial_reasoning_.md)**

:   Context-Nav 将长文本描述的上下文信息从后验验证信号提升为前驱探索先验——通过上下文驱动的 value map 引导前沿选择，并在候选目标处执行视点感知的 3D 空间关系验证，在 InstanceNav 和 CoIN-Bench 上无需任何训练即取得 SOTA。

**[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](crowdgaussian_reconstructing_high-fidelity_3d_gaussians_for_human_crowd_from_a_s.md)**

:   CrowdGaussian 提出了从单张图像重建多人 3D 高斯泼溅表示的统一框架，通过自监督适配的大型遮挡人体重建模型（LORM）恢复被遮挡区域的完整几何，再通过自校准学习（SCL）训练的单步扩散精炼器（CrowdRefiner）提升纹理细节质量。

**[CustomTex: High-fidelity Indoor Scene Texturing via Multi-Reference Customization](customtex_high-fidelity_indoor_scene_texturing_via_multi-reference_customization.md)**

:   提出CustomTex框架，通过实例级的多参考图像驱动和双蒸馏训练策略（语义级VSD蒸馏+像素级超分蒸馏），实现3D室内场景的高保真、实例可控纹理生成，在语义一致性、纹理清晰度和减少"烘焙阴影"方面全面超越现有方法。

**[Dark3R Learning Structure From Motion In The Dark](dark3r_learning_structure_from_motion_in_the_dark.md)**

:   提出 Dark3R 框架，通过教师-学生蒸馏将 MASt3R 的3D先验迁移到极端低光照（SNR < −4 dB）原始图像上，实现了传统方法完全失败的暗光环境下的运动恢复结构（SfM）和新视角合成。

**[DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis](dmaligner_enhancing_image_alignment_via_diffusion_model_based_view_synthesis.md)**

:   提出 DMAligner，将图像对齐问题从传统的光流 warp 范式转化为"对齐导向的视图合成"任务，利用条件扩散模型直接生成对齐后的完整图像，配合专门构建的 DSIA 合成数据集和动态感知掩码模块（DMP），有效避免了 warp 方法固有的 ghosting 和遮挡伪影，在多个基准上全面超越现有方法。

**[DROID-W: DROID-SLAM in the Wild](droid-slam_in_the_wild.md)**

:   提出 DROID-W，通过将不确定性估计引入可微分 Bundle Adjustment（Uncertainty-aware BA），结合 DINOv2 特征驱动的动态不确定性更新机制和单目深度正则化，使 DROID-SLAM 在高度动态的野外（in-the-wild）场景中实现鲁棒的相机位姿估计和场景重建，约 10 FPS 实时运行。

**[Dropping Anchor And Spherical Harmonics For Sparse-View Gaussian Splatting](dropping_anchor_and_spherical_harmonics_for_sparse-view_gaussian_splatting.md)**

:   针对 3DGS 在稀疏视角下的过拟合问题，提出 DropAnSH-GS：用 Anchor-based Dropout（丢弃锚点及其邻域的 Gaussian 簇）替代独立随机 Dropout 来破坏局部冗余补偿效应，同时引入球谐函数（SH）Dropout 抑制高阶 SH 过拟合并支持训练后无损压缩。

**[DuoMo: Dual Motion Diffusion for World-Space Human Reconstruction](duomo_dual_motion_diffusion_for_world-space_human_reconstruction.md)**

:   提出 DuoMo，将世界空间人体运动重建分解为两个独立的扩散模型：camera-space 模型从视频提取泛化性强的相机坐标运动估计，world-space 模型将 lifting 后的噪声提案精炼为全局一致的世界坐标运动。直接生成 mesh 顶点运动而非 SMPL 参数，在 EMDB 上 W-MPJPE 降低 16%，RICH 上降低 30%。

**[Dynamic Black-Hole Emission Tomography With Physics-Informed Neural Fields](dynamic_black-hole_emission_tomography_with_physics-informed_neural_fields.md)**

:   提出 PI-DEF，利用物理信息约束的坐标神经网络同时重建黑洞附近气体的 4D（时间+3D）发射率场和 3D 速度场，在稀疏 EHT 测量下显著优于硬约束 Keplerian 动力学的 BH-NeRF。

**[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](e2egs_event-to-edge_gaussian_splatting_for_pose-free_3d_reconstruction.md)**

:   提出 E2EGS，一个完全基于事件流的无位姿 3D 重建框架：通过 patch-based 时间一致性分析从事件流中提取抗噪边缘图，利用边缘信息指导高斯初始化和加权损失优化，在无需深度模型或 RGB 输入的情况下实现了高质量的轨迹估计和 3D 重建。

**[Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow](easy3e_feed-forward_3d_asset_editing_via_rectified_voxel_flow.md)**

:   提出基于 TRELLIS 3D 生成骨干的前馈式 3D 资产编辑框架，通过 Voxel FlowEdit 在稀疏体素潜空间中实现全局一致的几何形变，并结合法线引导的多视角纹理精修恢复高频细节。

**[Ego-1K: A Large-Scale Multiview Video Dataset for Egocentric Vision](ego-1k_--_a_large-scale_multiview_video_dataset_for_egocentric_vision.md)**

:   提出 Ego-1K，一个包含 956 段短视频的大规模时间同步第一人称多视角视频数据集（12+4 相机、60Hz），填补了第一人称动态 3D 重建领域的数据空白，并展示立体深度引导可大幅提升 4D 新视角合成质量。

**[Embodiedsplat Online Feed-Forward Semantic 3Dgs For Open-Vocabulary 3D Scene Und](embodiedsplat_online_feed-forward_semantic_3dgs_for_open-vocabulary_3d_scene_und.md)**

:   提出 EmbodiedSplat，首个在线前馈式语义 3DGS 框架，通过稀疏系数场+CLIP全局码本实现内存高效的逐高斯语义表示，结合3D几何感知特征，在300+帧流式输入下以5-6 FPS实现全场景开放词汇3D理解。

**[EMGauss: Continuous Slice-to-3D Reconstruction via Dynamic Gaussian Modeling in Volume Electron Microscopy](emgauss_continuous_slice-to-3d_reconstruction_via_dynamic_gaussian_modeling_in_v.md)**

:   将体电子显微镜(vEM)的各向异性切片重建问题重新建模为基于可变形2D高斯溅射的动态3D场景渲染任务，通过Teacher-Student伪标签机制在数据稀疏条件下实现高保真连续切片合成。

**[Enhancing Hands in 3D Whole-Body Pose Estimation with Conditional Hands Modulator](enhancing_hands_in_3d_whole-body_pose_estimation_with_conditional_hands_modulato.md)**

:   提出Hand4Whole++模块化框架，通过轻量级CHAM模块将预训练手部估计器的特征注入冻结的全身姿态估计器中，实现手腕方向的精准预测，并通过可微刚性对齐从手部模型迁移精细手指关节和手部形状。

**[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](facecam_portrait_video_camera_control_via_scale-aware_conditioning.md)**

:   提出FaceCam系统，通过面部地标(facial landmarks)作为尺度感知的相机表示来解决单目人像视频的相机控制问题，避免了传统相机外参表示的尺度歧义，并设计了合成相机运动和多镜头拼接两种数据增强策略支持连续相机轨迹推理。

**[FastGS: Training 3D Gaussian Splatting in 100 Seconds](fastgs_training_3d_gaussian_splatting_in_100_seconds.md)**

:   提出 FastGS，一个基于多视角一致性的 3DGS 加速框架，通过多视角一致性密集化（VCD）和多视角一致性剪枝（VCP）策略精准控制 Gaussian 数量，在 Mip-NeRF 360 等数据集上实现约 100 秒完成场景训练，相比 vanilla 3DGS 加速 15× 以上，且渲染质量可比。

**[ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph](forgedreamer_industrial_text-to-3d_generation_with_multi-expert_lora_and_cross-v.md)**

:   提出 ForgeDreamer 框架，通过多专家 LoRA 师生蒸馏解决工业领域语义适配问题，结合跨视角超图几何增强实现高阶几何一致性约束，在工业文本到3D生成任务上超越现有方法。

**[From Pairs to Sequences: Track-Aware Policy Gradients for Keypoint Detection](from_pairs_to_sequences_track-aware_policy_gradients_for_keypoint_detection.md)**

:   将关键点检测从「图像对匹配」范式转变为「序列级可追踪性优化」，通过强化学习框架 TraqPoint 在图像序列上直接优化关键点的长期追踪质量，在位姿估计、视觉定位、视觉里程计和三维重建任务上均超越 SOTA。

**[GeodesicNVS: Probability Density Geodesic Flow Matching for Novel View Synthesis](geodesicnvs_flow_matching_novel_view_synthesis.md)**

:   提出Data-to-Data Flow Matching直接学习视角间确定性变换，并引入概率密度测地线正则化使流路径沿数据流形高密度区域传播，在NVS中实现更好的跨视角一致性和几何保真度。

**[GeodesicNVS: Probability Density Geodesic Flow Matching for Novel View Synthesis](geodesicnvs_probability_density_geodesic_flow_matching_for_novel_view_synthesis.md)**

:   提出概率密度测地线 Flow Matching (PDG-FM) 框架，通过数据到数据的确定性流匹配替代噪声到数据的扩散过程，并利用基于概率密度的测地线优化使插值路径沿数据流形高密度区域行进，实现更几何一致的新视角合成。

**[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](geometry-as-context_modulating_explicit_3d_in_scene-consistent_video_generation_.md)**

:   提出 Geometry-as-Context (GaC) 框架，将基于重建的场景视频生成中的不可微算子（3D重建+渲染）替换为统一的自回归视频生成模型，通过将几何信息（深度图）作为交错上下文嵌入生成序列，实现端到端训练并缓解累积误差。

**[GGPT: Geometry Grounded Point Transformer](ggpt_geometry_grounded_point_transformer.md)**

:   提出 GGPT 框架，通过改进的轻量 SfM 管线获取几何一致但稀疏的 3D 点云，再用 3D Point Transformer 在三维空间中直接融合稀疏几何引导与稠密前馈预测，实现跨架构、跨数据集的显著泛化提升。

**[Global-Aware Edge Prioritization for Pose Graph Initialization](global-aware_edge_prioritization_for_pose_graph_initialization.md)**

:   提出基于GNN的全局边优先级排序方法，将位姿图初始化从独立的逐对图像检索升级为全局结构感知的边排序+多最小生成树构建，在极稀疏设置下显著提升SfM重建精度。

**[GS-CLIP: Zero-shot 3D Anomaly Detection by Geometry-Aware Prompt and Synergistic View Representation Learning](gs-clip_zero-shot_3d_anomaly_detection_by_geometry-aware_prompt_and_synergistic_.md)**

:   提出GS-CLIP两阶段框架，通过几何缺陷蒸馏模块将3D点云的全局形状和局部缺陷信息注入文本提示，并用LoRA双流架构协同融合渲染图和深度图，在四个大规模数据集上实现零样本3D异常检测SOTA。

**[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](humanorbit_3d_human_reconstruction_as_360_orbit_generation.md)**

:   将单图3D人体重建转化为360°轨道视频生成问题，用仅500个3D扫描数据LoRA微调视频扩散模型（Wan 2.1）生成81帧环绕视频，再通过VGGT+Mesh Carving重建高质量纹理网格，无需位姿标注且在多视图一致性和身份保持上超越现有方法。

**[Hybrid eTFCE–GRF: Exact Cluster-Size Retrieval with Analytical p-Values for Voxel-Based Morphometry](hybrid_etfce-grf_exact_cluster-size_retrieval_with_analytical_p-values_for_voxel.md)**

:   提出将 eTFCE 的 union-find 精确聚类大小检索与 pTFCE 的 GRF 解析推断相结合的混合方法，首次同时实现精确聚类大小查询与无需置换检验的分析型 $p$ 值计算，比 R pTFCE 快 $4.6\times$–$75\times$。

**[Hybrid eTFCE–GRF: Exact Cluster-Size Retrieval with Analytical p-Values for Voxel-Based Morphometry](hybrid_etfcegrf_exact_clustersize_retrieval_with_a.md)**

:   将 eTFCE 的并查集精确聚类大小提取与 pTFCE 的解析 GRF 推断相结合，首次同时实现精确聚类大小查询和无置换检验的解析 p 值，在全脑 VBM 分析上比 R pTFCE 快 4.6–75 倍，比置换 TFCE 快三个数量级。

**[HyperMVP: Hyperbolic Multiview Pretraining for Robotic Manipulation](hyperbolic_multiview_pretraining_for_robotic_manipulation.md)**

:   提出 HyperMVP，首个在双曲空间中进行3D多视角自监督预训练的框架，通过 GeoLink 编码器学习双曲多视角表征并迁移到机器人操作任务，在 COLOSSEUM 最困难的 All Perturbations 设置下实现 2.1× 性能提升。

**[Igasa Integrated Geometry-Aware And Skip-Attention Modules For Enhanced Point Cl](igasa_integrated_geometry-aware_and_skip-attention_modules_for_enhanced_point_cl.md)**

:   提出 IGASA 框架，通过分层金字塔架构 (HPA) + 分层跨层注意力 (HCLA) + 迭代几何感知精修 (IGAR) 三级流水线，弥合多尺度特征的语义鸿沟并动态抑制离群点，在 3D(Lo)Match、KITTI、nuScenes 四大基准上全面超越 SOTA。

**[IGASA: Integrated Geometry-Aware and Skip-Attention Modules for Enhanced Point Cloud Registration](igasa_integrated_geometryaware_and_skipattention_m.md)**

:   提出 IGASA 点云配准框架，通过层级金字塔架构 (HPA) + 层级跨层注意力 (HCLA) 的跳跃注意力融合 + 迭代几何感知精细化 (IGAR) 的动态一致性加权，在 3DMatch 上达到 94.6% Registration Recall（SOTA），在 KITTI 上达到 100% RR，总推理时间仅 2.763s。

**[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](instanthdr_single-forward_gaussian_splatting_for_high_dynamic_range_3d_reconstru.md)**

:   提出 InstantHDR，首个前馈式 HDR 新视角合成方法，通过几何引导的外观建模实现多曝光融合，配合元网络学习场景自适应色调映射器，在单次前向传播中从未校准的多曝光 LDR 图像重建 HDR 3D 场景，比优化方法快 ~700×（前馈）/ ~20×（后优化）。

**[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](instanthdr_singleforward_gaussian_splatting_for_hi.md)**

:   提出首个前馈HDR新视角合成方法InstantHDR，通过几何引导的外观建模和色调映射元网络，从未标定多曝光LDR图像中单次前向重建HDR 3D高斯场景，速度比优化方法快~700×，后优化版本快~20×且质量可比。

**[JOPP-3D: Joint Open Vocabulary Semantic Segmentation on Point Clouds and Panoramas](jopp-3d_joint_open_vocabulary_semantic_segmentation_on_point_clouds_and_panorama.md)**

:   提出 JOPP-3D，首个联合处理3D点云和全景图像的开放词汇语义分割框架，通过切向分解将全景图映射到正二十面体面、用 SAM+CLIP 提取语义对齐的3D实例嵌入，在 S3DIS 上以弱监督达到 80.9% mIoU 超越所有封闭词汇方法。

**[JOPP-3D: Joint Open Vocabulary Semantic Segmentation on Point Clouds and Panoramas](jopp3d_joint_open_vocabulary_semantic_segmentation.md)**

:   提出JOPP-3D——首个联合处理点云和全景图的开放词汇语义分割框架，通过正二十面体切向分解将全景图转为透视图后利用SAM+CLIP提取实例级语义嵌入，再经深度对应实现3D→全景语义回投，在S3DIS上以80.9% mIoU超越所有监督/无监督方法（含PointTransformerV3的73.4%），全景分割70.1% mIoU大幅领先。

**[ECKConv: Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant Point Cloud Analysis](learning_coordinate-based_convolutional_kernels_for_continuous_se3_equivariant_a.md)**

:   提出ECKConv，在intertwiner框架下将卷积核定义在双陪集空间 $\text{SO(2)}\backslash\text{SE(3)}/\text{SO(2)}$ 上，通过坐标网络显式参数化核函数，首次实现连续SE(3)等变性与大规模可扩展性的兼得，在分类、配准、分割四类任务上全面验证。

**[Let It Snow Animating 3D Gaussian Scenes With Dynamic Weather Effects Via Physic](let_it_snow_animating_3d_gaussian_scenes_with_dynamic_weather_effects_via_physic.md)**

:   提出 Physics-Guided Score Distillation 框架，利用物理仿真（MPM）作为运动先验引导 Video-SDS 优化，在静态 3DGS 场景中生成具有物理合理运动和真实感外观的动态天气效果（降雪、降雨、雾、沙尘暴）。

**[Lite Any Stereo: Efficient Zero-Shot Stereo Matching](lite_any_stereo_efficient_zero-shot_stereo_matching.md)**

:   提出Lite Any Stereo，通过混合2D-3D代价聚合模块和三阶段百万级数据训练策略（监督→自蒸馏→真实数据知识蒸馏），以不到SOTA精确方法1%的计算量（33G MACs），在四个real-world benchmark上ranking 1st，首次证明超轻量模型可具备强零样本泛化能力。

**[LongStream: Long-Sequence Streaming Autoregressive Visual Geometry](longstream_long-sequence_streaming_autoregressive_visual_geometry.md)**

:   提出LongStream，一种gauge-decoupled的流式视觉几何模型，通过关键帧相对位姿预测、正交尺度学习和缓存一致性训练，实现千帧级别稳定的度量尺度实时（18 FPS）场景重建。

**[LoST: Level of Semantics Tokenization for 3D Shapes](lost_level_of_semantics_tokenization_for_3d_shapes.md)**

:   提出Level-of-Semantics Tokenization (LoST)，按语义显著性排序3D形状token，使短前缀即可解码出完整且语义合理的形状，配合RIDA语义对齐损失和GPT式自回归生成，仅用128个token即显著超越现有需数万token的3D AR方法。

**[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](ltgs_long-term_gaussian_scene_chronology_from_sparse_view_updates.md)**

:   提出 LTGS 框架，通过构建可复用的物体级高斯模板，从时空稀疏的观测图像中高效更新 3DGS 场景重建，实现长期环境演化的时序建模。

**[M3DLayout: A Multi-Source Dataset of 3D Indoor Layouts and Structured Descriptions for 3D Generation](m3dlayout_a_multi-source_dataset_of_3d_indoor_layouts_and_structured_description.md)**

:   构建了多源大规模 3D 室内布局数据集 M3DLayout（21,367 布局、433k+ 物体实例），融合真实扫描、专业设计和程序化生成三种来源，配以结构化文本描述，为文本驱动的 3D 场景生成提供高质量训练基础。

**[MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer](more_motion-aware_feed-forward_4d_reconstruction_transformer.md)**

:   提出 MoRe，一种前馈式运动感知 4D 重建 Transformer，通过注意力强制策略在训练时解耦动态运动与静态结构，结合分组因果注意力实现高效流式推理，在动态场景的相机位姿估计和深度预测上达到 SOTA。

**[Motion-Aware Animatable Gaussian Avatars Deblurring](motion-aware_animatable_gaussian_avatars_deblurring.md)**

:   提出首个从模糊视频直接重建清晰可动画3D人体高斯Avatar的方法，通过3D感知的物理模糊形成模型和基于SMPL的人体运动模型，联合优化Avatar表示和运动参数。

**[MotionAnymesh: Physics-Grounded Articulation for Simulation-Ready Digital Twins](motionanymesh_physics-grounded_articulation_for_simulation-ready_digital_twins.md)**

:   提出MotionAnymesh，一个零样本自动框架，通过运动感知分割（SP4D先验+VLM推理）和几何-物理联合优化关节估计，将静态3D网格转化为无碰撞的仿真就绪铰接数字孪生，在PartNet-Mobility和Objaverse上物理可执行性达87%。

**[MotionAnymesh: Physics-Grounded Articulation for Simulation-Ready Digital Twins](motionanymesh_physicsgrounded_articulation_for_sim.md)**

:   提出MotionAnymesh零样本框架，通过SP4D运动学先验引导VLM消除运动学幻觉，并用物理约束轨迹优化保证无碰撞铰接，将静态3D网格自动转换为可在SAPIEN等物理引擎中直接使用的URDF数字孪生，物理可执行率达87%，远超现有方法。

**[MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation](msgnav_multimodal_3d_scene_embodied_navigation.md)**

:   提出多模态 3D 场景图（M3DSG）——用动态分配的图像替代纯文本关系边保留视觉线索，基于此构建 MSGNav 零样本导航系统，包含关键子图选择、自适应词汇更新、闭环推理和基于可见性的视角决策模块，在 GOAT-Bench 和 HM3D-ObjNav 上取得 SOTA。

**[Nanosd Edge Efficient Foundation Model For Real Time Image Restoration](nanosd_edge_efficient_foundation_model_for_real_time_image_restoration.md)**

:   提出 NanoSD，通过对 SD 1.5 进行硬件感知的 U-Net 分解、逐块特征蒸馏和多目标贝叶斯优化，构建了一族 Pareto 最优的轻量扩散基础模型（130M–315M 参数，最快 12ms 推理），可作为 drop-in backbone 在超分、人脸修复、去模糊、单目深度估计等多任务上达到 SOTA 级表现。

**[NERFIFY: 多智能体框架将NeRF论文自动转化为可运行代码](nerfify_multiagent_nerf_paper_to_code.md)**

:   提出NERFIFY——通过6项关键创新（CFG约束、GoT代码合成、引用链组件恢复、视觉反馈修复、知识增强、系统评测），将NeRF论文可靠转化为可训练的Nerfstudio插件，在无公开实现的论文上达到±0.5dB PSNR的专家级复现质量，实现时间从数周降至数分钟。

**[Node-RF: Learning Generalized Continuous Space-Time Scene Dynamics with Neural ODE-based NeRFs](noderf_neural_ode_nerf_continuous_spacetime_dynam.md)**

:   Node-RF 将 Neural ODE 与 NeRF 紧密耦合，通过在隐空间中用微分方程建模场景动态演化，实现了超越训练时间范围的长程外推、跨序列泛化以及动态系统行为分析。

**[Openvo Open-World Visual Odometry With Temporal Dynamics Awareness](openvo_open-world_visual_odometry_with_temporal_dynamics_awareness.md)**

:   提出 OpenVO，一个面向开放世界的单目视觉里程计框架，通过时间感知流编码器和几何感知上下文编码器，在无相机标定、帧率变化的条件下实现鲁棒的真实尺度自车运动估计，跨数据集 ATE 提升超 20%，变帧率场景误差降低 46%-92%。

**[Pano360: Perspective to Panoramic Vision with Geometric Consistency](pano360_perspective_to_panoramic_vision_with_geome.md)**

:   提出Pano360，将全景拼接从传统的2D成对对齐扩展到3D摄影测量空间，利用基于Transformer的架构实现多视图全局几何一致性，在弱纹理、大视差和重复纹理等挑战场景中成功率达97.8%，并构建了包含200个真实场景的大规模数据集。

**[Phygap Physically-Grounded Gaussians With Polarization Cues](phygap_physically-grounded_gaussians_with_polarization_cues.md)**

:   提出 PhyGaP，通过偏振延迟渲染（PolarDR）将偏振线索融入 2DGS 优化，并设计自遮挡感知的 GridMap 环境图技术，实现光泽物体的精确反射分解与真实重光照。

**[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](physgm_large_physical_gaussian_4d_synthesis.md)**

:   首个从单张图像前馈预测3DGS+物理属性（材质类别/杨氏模量/泊松比）的框架，两阶段训练（监督预训练+DPO偏好微调）完全绕过SDS和可微物理引擎，配合50K+ PhysAssets数据集，1分钟内生成高保真4D物理仿真，CLIP_sim和人类偏好率均超越逐场景优化方法。

**[Physgm Large Physical Gaussian Model For Feed-Forward 4D Synthesis](physgm_large_physical_gaussian_model_for_feed-forward_4d_synthesis.md)**

:   PhysGM 提出首个前馈式框架，从单张图像一次推理即可同时预测 3D 高斯表示和物理属性（刚度、质量等），结合 MPM 仿真在一分钟内生成高保真的物理合理 4D 动画，无需任何逐场景优化。

**[QuadSync: Quadrifocal Tensor Synchronization via Tucker Decomposition](quadsync_quadrifocal_tensor_synchronization_via_tucker_decomposition.md)**

:   首次提出四焦张量(quadrifocal tensor)的全局同步算法 QuadSync，通过构造块四焦张量并证明其承认多线性秩为 (4,4,4,4) 的 Tucker 分解，利用 ADMM-IRLS 优化框架从四视图测量中恢复相机位姿，在密集视图场景下取得优于两视图/三视图方法的同步精度。

**[R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection# R4Det: 4D Radar-Camera Fusion for High-Performance 3D Object Detection](r4det_4d_radar_camera_fusion_3d_detection.md)**

:   提出R4Det，通过全景深度融合（PDF）、可变形门控时序融合（DGTF）和实例引导动态精炼（IGDR）三个即插即用模块，解决4D雷达-相机融合中深度估计不准、时序融合依赖ego pose、小目标检测困难的问题，在TJ4DRadSet和VoD上取得SOTA。

**[Regularizing INR with Diffusion Prior for Self-Supervised 3D Reconstruction of Neutron Computed Tomography Data](regularizing_inr_with_diffusion_prior_selfsupervis.md)**

:   将扩散模型先验作为正则化项引入隐式神经表示(INR)的损失函数中，构建DINR框架用于稀疏视图中子CT重建，在仅5个视角的极端稀疏条件下仍能保持混凝土微结构的高质量重建。

**[ReLaGS: Relational Language Gaussian Splatting](relags_relational_language_gaussian_splatting.md)**

:   提出首个统一多层级语言高斯场与开放词汇3D场景图的无训练框架 ReLaGS，通过最大权重剪枝和鲁棒异常值感知特征聚合改进场景表示，结合GNN关系预测实现高效的结构化3D场景理解。

**[Reparameterized Tensor Ring Functional Decomposition for Multi-Dimensional Data Recovery](reparameterized_tensor_ring_functional_decomposition_for_multi-dimensional_data_.md)**

:   提出 RepTRFD：通过将 Tensor Ring 因子重参数化为"可学习隐张量 × 固定基"的形式，解决 INR 参数化 TR 因子的频谱偏置问题，在图像修复/去噪/超分/点云恢复等任务上全面超越 SOTA。

**[Rethinking Pose Refinement In 3D Gaussian Splatting Under Pose Prior And Geometr](rethinking_pose_refinement_in_3d_gaussian_splatting_under_pose_prior_and_geometr.md)**

:   提出 UGS-Loc 框架，通过蒙特卡洛位姿采样和 Fisher 信息引导的 PnP 优化，联合建模位姿先验不确定性和几何不确定性，在无需重训练的条件下显著提升 3DGS 场景中的相机位姿精化鲁棒性。

**[RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting](retimegs_continuous_time_4d_gaussian.md)**

:   提出 RetimeGS, 通过 Catmull-Rom 样条轨迹建模高斯基元的时间行为, 结合双向光流监督和正则化时间不透明度, 解决 4DGS 帧插值时的时间混叠问题, 在 Stage-Capture 数据集上达到 30.08 dB PSNR (比前 SOTA +1.29 dB).

**[Scaling View Synthesis Transformers (SVSM)](scaling_view_synthesis_transformers.md)**

:   首次为无几何先验的 NVS Transformer 建立缩放定律：提出有效批量大小假设（B_eff = B·V_T）揭示 encoder-decoder 被低估的根因，设计单向 encoder-decoder 架构 SVSM，在 RealEstate10K 上以不到一半训练 FLOPs 达到新 SOTA（30.01 PSNR），Pareto 前沿比 LVSM decoder-only 左移 3×。

**[SCOPE: Scene-Contextualized Incremental Few-Shot 3D Segmentation](scope_scenecontextualized_incremental_fewshot_3d_s.md)**

:   提出即插即用的背景引导原型增强框架SCOPE，从背景区域挖掘伪实例原型丰富新类原型表示，在ScanNet上5-shot新类IoU达23.86%(vs GW 16.88%，+6.98%)，且几乎无额外计算开销(<1MB, 0.02s)。

**[Seethrough3D Occlusion Aware 3D Control In Text-To-Image Generation](seethrough3d_occlusion_aware_3d_control_in_text-to-image_generation.md)**

:   提出 SeeThrough3D，通过半透明 3D 包围盒渲染的遮挡感知场景表示（OSCR）来条件化 FLUX 模型，实现了精确的 3D 布局控制与遮挡一致的文本到图像生成。

**[SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection](span_spatial-projection_alignment_for_monocular_3d_object_detection.md)**

:   提出 Spatial-Projection Alignment (SPAN)，通过3D角点空间对齐和3D-2D投影对齐两个几何协同约束，配合分层任务学习策略，作为即插即用模块提升任意单目3D检测器的定位精度。

**[SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection](span_spatial_projection_alignment_mono3d.md)**

:   提出SPAN即插即用几何协同约束框架，通过3D角点空间对齐和3D-2D投影对齐两个可微损失，强制解耦预测的各属性满足全局几何一致性，配合层级任务学习策略稳定训练，在KITTI上将MonoDGP的Car Moderate AP3D提升0.92%达到新SOTA。

**[Spectral Defense Against Resource-Targeting Attack In 3D Gaussian Splatting](spectral_defense_against_resource-targeting_attack_in_3d_gaussian_splatting.md)**

:   提出首个针对 3DGS 资源耗尽攻击的频域防御框架，通过 3D 频率滤波器选择性剪枝异常高频高斯 + 2D 频谱正则化约束渲染图像的各向异性噪声，在攻击下将高斯过生长抑制最高 5.92×、显存降低最高 3.66×、渲染加速最高 4.34×，同时保持重建质量。

**[Spectral Defense Against Resource-Targeting Attack in 3D Gaussian Splatting](spectral_defense_against_resourcetargeting_attack.md)**

:   提出首个针对3DGS资源瞄准攻击的频域防御框架——联合3D频率感知高斯剪枝与2D角度各向异性正则化，将投毒导致的高斯过增长最多抑制5.92×、峰值显存降3.66×、渲染速度提升4.34×，同时渲染质量反而提升(PSNR +1.93dB)。

**[Using Gaussian Splats To Create High-Fidelity Facial Geometry And Texture](using_gaussian_splats_to_create_high-fidelity_facial_geometry_and_texture.md)**

:   提出一套基于改进 Gaussian Splatting 的人脸重建管线：通过软约束和语义分割监督将高斯与三角网格紧耦合，从仅 11 张未标定图像重建高精度三角面片几何，并利用 PCA 先验 + 可重光照高斯模型分离光照获取去光照 albedo 纹理，最终兼容标准图形管线（MetaHuman）。

**[VGG-T3: Offline Feed-Forward 3D Reconstruction at Scale](vgg-t3_offline_feed-forward_3d_reconstruction_at_scale.md)**

:   提出VGG-T3，通过**测试时训练(TTT)**将VGGT中全局注意力层的变长KV表示压缩为固定大小MLP，将离线前馈三维重建的计算复杂度从 $O(n^2)$ 降至 $O(n)$，实现了千张图片级别的大规模场景重建（1k张图仅需58秒）。

**[WMGStereo: What Makes Good Synthetic Training Data for Zero-Shot Stereo Matching?](what_makes_good_synthetic_training_data_for_zerosh.md)**

:   系统研究合成立体数据集的设计空间——变换Infinigen过程化生成参数(浮动物体密度/背景/材质/相机baseline/光照等)分析其对零样本立体匹配的影响，发现"真实室内场景+浮动物体"的组合最有效；据此构建WMGStereo-150k数据集，仅用此单一数据集训练超越SceneFlow+CREStereo+TartanAir+IRS四合一(Middlebury降28%，Booster降25%)，与FoundationStereo竞争力相当。
