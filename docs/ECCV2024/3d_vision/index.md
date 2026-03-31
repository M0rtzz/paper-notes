<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**🎞️ ECCV2024** · 共 **43** 篇

**[3D Congealing: 3D-Aware Image Alignment in the Wild](3d_congealing_3d-aware_image_alignment_in_the_wild.md)**

:   3D Congealing将一组语义相似的无标注互联网图像对齐到共享的3D canonical空间，通过结合预训练扩散模型的SDS指导获得3D形状 + DINO语义特征匹配估计位姿和坐标映射，无需模板、位姿标注或相机参数。

**[3D Reconstruction of Objects in Hands without Real World 3D Supervision](3d_reconstruction_of_objects_in_hands_without_real_world_3d.md)**

:   提出HORSE框架，通过从野外视频中提取多视角2D mask监督（以手部姿态作为物体姿态代理）和从合成3D形状集合中学习2D切片对抗形状先验，训练occupancy网络从单张RGB图像重建手持物体3D形状，在不使用任何真实世界3D标注的情况下，在MOW数据集上超越使用3D监督的方法11.6%。

**[3D Single-Object Tracking in Point Clouds with High Temporal Variation](3d_single-object_tracking_in_point_clouds_with_high_temporal_variation.md)**

:   HVTrack首次探索高时间变化场景下的3D单目标跟踪，通过相对位姿感知记忆模块(RPM)、基础-扩展特征交叉注意力(BEA)和上下文点引导自注意力(CPA)三个模块，分别解决点云形状剧变、相似物体干扰和背景噪声问题，在KITTI-HV 5帧间隔下比SOTA提升11.3%/15.7% Success/Precision。

**[3DEgo: 3D Editing on the Go!](3dego_3d_editing_on_the_go.md)**

:   3DEgo将传统三阶段3D编辑流程（COLMAP位姿估计→未编辑场景初始化→迭代编辑更新）压缩为单阶段框架：先用自回归噪声混合模块对视频帧进行多视角一致的2D编辑，再用COLMAP-free的3DGS从编辑后帧直接重建3D场景，速度提升约10倍且支持任意来源视频。

**[3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting](3igs_factorised_tensorial_illumination_for_3d_gaussian_splatting.md)**

:   3iGS 用基于张量分解的连续入射光照场替代 3DGS 中每个高斯体独立优化的球谐系数，结合可学习 BRDF 特征和轻量神经渲染器来建模出射辐射，在保持实时渲染速度的同时显著提升了镜面反射等视角依赖效果的渲染质量。

**[3×2: 3D Object Part Segmentation by 2D Semantic Correspondences](3x2_3d_object_part_segmentation_by_2d_semantic_correspondenc.md)**

:   提出了一种无需训练的3D物体部件分割方法3-By-2，利用扩散模型(DIFT)的2D语义对应关系从已标注2D数据集或少量3D标注对象中迁移部件标签到3D，在zero-shot和few-shot设置下均达到SOTA。

**[6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model](6dgs_6d_pose_estimation_from_a_single_image_and_a_3d_gaussia.md)**

:   提出6DGS，通过反转3DGS渲染流程——从椭球体表面均匀发射光线（Ellicell），利用注意力机制将光线与目标图像像素绑定，再用加权最小二乘闭式求解相机位姿，无需迭代和初始位姿，在真实场景上旋转精度提升12%、平移精度提升22%，达到15fps近实时性能。

**[A Compact Dynamic 3D Gaussian Representation for Real-Time Dynamic View Synthesis](a_compact_dynamic_3d_gaussian_representation_for_realtime_dy.md)**

:   将3DGS中的位置和旋转参数建模为时间的函数（位置用Fourier逼近、旋转用线性逼近），使动态场景的存储复杂度从O(TN)降低到O(LN)，在D-NeRF/DyNeRF/HyperNeRF三个数据集上实现了与NeRF方法匹敌的渲染质量，同时保持118+ FPS的实时渲染速度。

**[Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration](analytic-splatting_anti-aliased_3d_gaussian_splatting_via_analytic_integration.md)**

:   通过使用条件 logistic 函数解析近似高斯信号在像素窗口上的积分，替代 3DGS 的像素中心点采样，实现无混叠的 3D 高斯泼溅，在多尺度渲染上超越 Mip-Splatting。

**[AnimatableDreamer: Text-Guided Non-rigid 3D Model Generation and Reconstruction with Canonical Score Distillation](animatabledreamer_text-guided_non-rigid_3d_model_generation_and_reconstruction_w.md)**

:   提出 AnimatableDreamer，通过 Canonical Score Distillation (CSD) 技术，从单目视频提取骨骼和运动后生成文本引导的可动画化 3D 非刚体模型，在生成质量和时序一致性上全面超越现有方法。

**[BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting](bad-gaussians_bundle_adjusted_deblur_gaussian_splatting.md)**

:   首次将运动模糊物理成像模型引入 3D Gaussian Splatting 框架，联合优化场景 Gaussian 参数与曝光时间内的相机运动轨迹，从模糊图像中恢复清晰 3D 场景并实现实时渲染。

**[BeNeRF: Neural Radiance Fields from a Single Blurry Image and Event Stream](benerf_neural_radiance_fields_from_a_single_blurry_image_and_event_stream.md)**

:   提出 BeNeRF，仅从**单张模糊图像**及其对应的事件流（event stream）联合恢复神经辐射场与相机运动轨迹，无需多视角输入或已知位姿，即可实现高质量去模糊与新视角合成。

**[Bi-directional Contextual Attention for 3D Dense Captioning](bi-directional_contextual_attention_for_3d_dense_captioning.md)**

:   提出 BiCA，通过双向上下文注意力机制将 instance query 和 context query 解耦并行解码，解决了 3D 密集描述中定位与描述生成之间的目标冲突，在 ScanRefer 和 Nr3D 两个基准上取得 SOTA。

**[Binomial Self-compensation for Motion Error in Dynamic 3D Scanning](binomial_self-compensation_for_motion_error_in_dynamic_3d_scanning.md)**

:   提出二项式自补偿(BSC)算法,通过对运动受影响的相位序列按二项式系数加权求和,无需任何中间变量即可指数级消除四步相位移轮廓术中的运动误差,实现与相机帧率相同的高精度动态3D扫描。

**[CaesarNeRF: Calibrated Semantic Representation for Few-Shot Generalizable Neural Rendering](caesarnerf_calibrated_semantic_representation_for_few-shot_generalizable_neural_.md)**

:   提出 CaesarNeRF，在可泛化 NeRF（GNT）基础上引入场景级语义表征，通过相机位姿校准（特征旋转对齐到目标视角）和序列细化（跨 Transformer 层逐步更新全局特征），在 1-view 设置下 PSNR 比 GNT 提升 1.74dB（LLFF），且可即插即用地增强 IBRNet、MatchNeRF 等其他基线。

**[Camera Height Doesn't Change: Unsupervised Training for Metric Monocular Road-Scene Depth Estimation](camera_height_doesnapost_change_unsupervised_training_for_metric_monocular_road-.md)**

:   提出FUMET训练框架,利用道路上检测到的车辆尺寸先验聚合为相机高度估计,并利用相机高度在同一视频序列中不变的事实作为度量尺度监督,使任意单目深度网络无需辅助传感器即可学习绝对尺度。

**[CanonicalFusion: Generating Drivable 3D Human Avatars from Multiple Images](canonicalfusion_generating_drivable_3d_human_avatars_from_multiple_images.md)**

:   提出CanonicalFusion框架,通过联合预测深度图和压缩LBS权重映射图实现直接规范化,并利用前向蒙皮可微渲染融合多张图像信息,从多张输入图像生成可驱动的3D人体Avatar。

**[CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-Aware 3D Gaussian Field](cg-slam_efficient_dense_rgb-d_slam_in_a_consistent_uncertainty-aware_3d_gaussian.md)**

:   提出CG-SLAM,基于一致性和几何稳定性优化的不确定性感知3D高斯场,实现高效稠密RGB-D SLAM,在定位精度和建图质量上均达到SOTA,跟踪速度最高15Hz。

**[CityGaussian: Real-Time High-Quality Large-Scale Scene Rendering with Gaussians](citygaussian_real-time_high-quality_large-scale_scene_rendering_with_gaussians.md)**

:   提出 CityGaussian (CityGS)，通过分治训练策略和 block-wise Level-of-Detail 机制，首次实现了城市级大规模场景（>1.5 km²）的高质量 3D Gaussian Splatting 训练与跨尺度实时渲染。

**[Compress3D: a Compressed Latent Space for 3D Generation from a Single Image](compress3d_a_compressed_latent_space_for_3d_generation_from_a_single_image.md)**

:   提出一种高度压缩的 triplane 潜空间自编码器，配合两阶段扩散模型（先生成 shape embedding 再生成 triplane latent），仅需 7 秒即可从单张图像生成高质量 3D 资产，且训练数据和时间远少于同类方法。

**[CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization](cor-gs_sparse-view_3d_gaussian_splatting_via_co-regularization.md)**

:   发现同时训练两个 3DGS 辐射场时它们在高斯位置和渲染结果上的差异（disagreement）与重建质量负相关，据此提出 CoR-GS 通过协同剪枝和伪视角协同正则化来抑制不准确重建，在稀疏视角下实现 SOTA 新视角合成。

**[CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model](crm_single_image_to_3d_textured_mesh_with_convolutional_reconstruction_model.md)**

:   提出卷积重建模型 CRM，利用 triplane 与六个正交视图之间的空间对齐先验，用 U-Net 替代 Transformer 直接从六视图映射到 triplane，结合 FlexiCubes 端到端训练，10 秒内从单张图像生成高保真纹理网格，训练成本仅为 LRM 的 1/8。

**[CrossScore: Towards Multi-View Image Evaluation and Scoring](crossscore_towards_multi-view_image_evaluation_and_scoring.md)**

:   提出 Cross-Reference（CR）图像质量评估新范式，通过对比查询图像与多个不同视角参考图像，利用 cross-attention 神经网络预测与 SSIM 高度相关的像素级质量分数，无需 ground truth 参考图像即可评估新视角合成质量。

**[CrossScore: Towards Multi-View Image Evaluation and Scoring](crossscore_towards_multiview_image_evaluation_and_scori.md)**

:   提出 CrossScore——一种新型的交叉参考图像质量评估方法，利用多视角参考图像替代真实参考图，通过 cross-attention 机制预测 SSIM 分数图，在无需 ground truth 的条件下实现接近全参考指标的评估精度。

**[D-SCo: Dual-Stream Conditional Diffusion for Monocular Hand-Held Object Reconstruction](d-sco_dual-stream_conditional_diffusion_for_monocular_hand-held_object_reconstru.md)**

:   提出双流条件扩散模型 D-SCo 从单张 RGB 图像重建手持物体点云，通过统一手-物语义嵌入和手关节几何嵌入两个分支分别提供语义和几何先验，配合手约束质心固定策略稳定扩散过程，在 ObMan 上 F-5 达 0.61（超 DDF-HO 10.9%），真实数据集 HO3D/MOW 上也大幅领先。

**[Deceptive-NeRF/3DGS: Diffusion-Generated Pseudo-observations for High-Quality Sparse-View Reconstruction](deceptive-nerf3dgs_diffusion-generated_pseudo-observations_for_high-quality_spar.md)**

:   利用微调的 Stable Diffusion + ControlNet 将粗糙 NeRF/3DGS 渲染结果转化为高质量伪观测图像，将稀疏输入视图增密 5-10 倍后重新训练，在 Hypersim/LLFF/ScanNet 等数据集上超越 FreeNeRF 等方法 1-2dB PSNR，训练速度比扩散正则化方法快约 10 倍。

**[DG-PIC: Domain Generalized Point-In-Context Learning for Point Cloud Understanding](dgpic_domain_generalized_pointincontext_learning_for_po.md)**

:   提出 DG-PIC，首个在统一模型中同时处理多域多任务点云理解的方法，通过双层源域原型估计和双层测试时特征平移机制，在无需模型更新的情况下提升对未见域的泛化能力。

**[DreamDrone: Text-to-Image Diffusion Models Are Zero-Shot Perpetual View Generators](dreamdrone_texttoimage_diffusion_models_are_zeroshot_perpetu.md)**

:   DreamDrone提出零样本、免训练的无限场景飞越生成pipeline，核心创新是在扩散模型的latent空间进行视角变换（而非像素空间），并通过特征对应引导和高通滤波策略保证帧间的几何一致性和高频细节一致性。

**[DreamView: Injecting View-Specific Text Guidance Into Text-to-3D Generation](dreamview_injecting_viewspecific_text_guidance_into_textto3d.md)**

:   DreamView通过自适应引导注入模块协调全局和视角特定文本实现3D定制化生成。

**[DSPDet3D: 3D Small Object Detection with Dynamic Spatial Pruning](dspdet3d_3d_small_object_detection_with_dynamic_spatial_pruning.md)**

:   提出动态空间剪枝（DSP）策略，在多级 3D 检测器的解码器中逐级移除已检测到大物体区域的体素特征，使检测器能以高空间分辨率处理场景、大幅提升小目标检测精度（ScanNet 小目标 mAP@0.25 从 27.5% 提升到 44.8%），同时通过剪枝将显存降低为同分辨率方法的 1/5。

**[FALIP: Visual Prompt as Foveal Attention Boosts CLIP Zero-Shot Performance](falip_visual_prompt_as_foveal_attention_boosts_clip_zer.md)**

:   提出 FALIP（Foveal-Attention CLIP），通过在 CLIP 的多头自注意力模块中插入类似人眼中央凹的注意力掩码，在不修改原始图像内容的前提下引导模型关注特定区域，显著提升指代表达理解、图像分类和 3D 点云识别等零样本任务的性能。

**[Gaussian Grouping: Segment and Edit Anything in 3D Scenes](gaussian_grouping_segment_and_edit_anything_in_3d_scenes.md)**

:   为 3D Gaussian Splatting 中的每个高斯学习 16 维 Identity Encoding 实现实例级分组，使用 SAM + DEVA 视频跟踪生成多视图一致的 2D 伪标签做监督，在 LERF-Mask 开放词汇分割上 mIoU 达 69-77%（超 LERF 2 倍+），全景分割超 Panoptic Lifting 4.9% mIoU 且 14× 更快，同时支持 3D 物体移除/修复/着色/风格迁移等多种编辑。

**[JointDreamer: Ensuring Geometry Consistency and Text Congruence in Text-to-3D Generation](jointdreamer_ensuring_geometry_consistency_and_text_congruen.md)**

:   JointDreamer提出JSD通过能量函数建模多视角联合分布确保3D一致性。

**[milliFlow: Scene Flow Estimation on mmWave Radar Point Cloud for Human Motion Sensing](milliflow_scene_flow_estimation_on_mmwave_radar_point_cloud_for_human_motion_sen.md)**

:   提出首个毫米波雷达点云场景流估计方法 milliFlow，通过多尺度特征提取、全局聚合、GRU 时序传播和约束回归，在自建数据集上将 EPE3D 从次优 0.107m 降至 0.046m（cm 级精度），并展示场景流特征对人体活动识别（+7.9%）、人体部位解析（+3.6%）、人体追踪等下游任务的增强效果。

**[MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo](mvsgaussian_fast_generalizable_gaussian_splatting_reconstruction_from_multi-view.md)**

:   将MVS的代价体深度估计与3D高斯溅射结合，通过混合渲染(splatting+volume rendering)提升泛化性，并提出基于多视图几何一致性的点云聚合策略，使per-scene优化仅需45秒就超越3D-GS的10分钟效果。

**[NOVUM: Neural Object Volumes for Robust Object Classification](novum_neural_object_volumes_for_robust_object_classification.md)**

:   提出 NOVUM 架构，为每个物体类别维护一个由 3D 高斯组成的神经体积表征，通过将图像特征与各类别的高斯特征匹配实现分类，在遮挡/损坏/真实 OOD 场景下相比 ResNet/ViT/Swin 等标准架构分类准确率提升 6-33%，同时支持 3D 位姿估计和可解释性可视化。

**[PointLLM: Empowering Large Language Models to Understand Point Clouds](pointllm_empowering_large_language_models_to_understand_point_clouds.md)**

:   将点云编码器（Point-BERT）通过 MLP 投影层对接 LLaMA 大语言模型，构建 PointLLM；利用 730K 指令数据（660K 简述 + 70K 复杂指令）两阶段训练后，在 3D 物体分类上达到 53.4% 生成式准确率（超越 LLaVA-13B 的 44.2%），在物体描述任务上人类评估胜率 55%（超越人工标注）。

**[Progressive Classifier and Feature Extractor Adaptation for Unsupervised Domain Adaptation on Point Clouds](progressive_classifier_and_feature_extractor_adaptation_for_unsupervised_domain_.md)**

:   提出 PCFEA 方法用于点云无监督域自适应，通过渐进构建从源域到目标域的中间域，在宏观层面用目标风格特征增强训练分类器（PTFA），微观层面引导特征提取器向中间域对齐（IDFA），在 PointDA-10 上均值准确率达 76.5%（超 SOTA +2.9%），GraspNetPC-10 上达 87.6%（超 SOTA +13.7%）。

**[ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities](scanreason_empowering_3d_visual_grounding_with_reasoning_capabilities.md)**

:   提出 3D reasoning grounding 新任务和 ScanReason 基准（10K+ QA-location pairs，5种推理类型），设计 ReGround3D 框架将 MLLM 推理与 3D grounding 模块通过 Chain-of-Grounding 机制协同，在隐式指令下实现准确的 3D 目标定位。

**[SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs](scenegraphloc_crossmodal_coarse_visual_localization_on_3d_sc.md)**

:   提出SceneGraphLoc，首次将queryimage在多模态3D场景图数据库中进行粗定位，通过学习场景图节点和图像patch的统一嵌入空间，在存储效率提升1000倍的同时接近图像检索方法的定位精度。

**[SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](sceneverse_scaling_3d_visionlanguage_learning_for_grounded_s.md)**

:   提出SceneVerse——首个百万级3D视觉语言数据集（68K场景+250万语言描述），通过结合人工标注和基于场景图的自动生成pipeline构建多粒度描述，并设计GPS预训练框架实现多层次场景-文本对齐，在3D grounding和QA基准上达到SOTA。

**[View Selection for 3D Captioning via Diffusion Ranking](view_selection_for_3d_captioning_via_diffusion_ranking.md)**

:   DiffuRank用预训练text-to-3D扩散模型评估视角对齐度选择最佳视角减少幻觉。

**[When Do We Not Need Larger Vision Models?](when_do_we_not_need_larger_vision_models.md)**

:   提出 Scaling on Scales (S2) 策略：冻结小模型（如 ViT-B）在多个图像尺度上运行并拼接特征，无需增加参数即可在分类、分割、深度估计、MLLM 等任务上匹敌甚至超越大模型（ViT-H/G），并从理论和实验上论证了大模型学到的表征大部分可由多尺度小模型线性近似。
