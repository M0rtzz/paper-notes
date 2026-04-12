---
title: >-
  ECCV2024 3D视觉方向 51篇论文解读
description: >-
  51篇ECCV2024 3D视觉方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D视觉

**🎞️ ECCV2024** · 共 **51** 篇

**[3D Congealing 3D-Aware Image Alignment In The Wild](3d_congealing_3d-aware_image_alignment_in_the_wild.md)**

:   3D Congealing将一组语义相似的无标注互联网图像对齐到共享的3D canonical空间，通过结合预训练扩散模型的SDS指导获得3D形状 + DINO语义特征匹配估计位姿和坐标映射，无需模板、位姿标注或相机参数。

**[3D Reconstruction Of Objects In Hands Without Real World 3D](3d_reconstruction_of_objects_in_hands_without_real_world_3d.md)**

:   提出HORSE框架，通过从野外视频中提取多视角2D mask监督（以手部姿态作为物体姿态代理）和从合成3D形状集合中学习2D切片对抗形状先验，训练occupancy网络从单张RGB图像重建手持物体3D形状，在不使用任何真实世界3D标注的情况下，在MOW数据集上超越使用3D监督的方法11.6%。

**[3D Single-Object Tracking In Point Clouds With High Temporal Variation](3d_single-object_tracking_in_point_clouds_with_high_temporal_variation.md)**

:   HVTrack首次探索高时间变化场景下的3D单目标跟踪，通过相对位姿感知记忆模块(RPM)、基础-扩展特征交叉注意力(BEA)和上下文点引导自注意力(CPA)三个模块，分别解决点云形状剧变、相似物体干扰和背景噪声问题，在KITTI-HV 5帧间隔下比SOTA提升11.3%/15.7% Success/Precision。

**[3Dego 3D Editing On The Go](3dego_3d_editing_on_the_go.md)**

:   3DEgo将传统三阶段3D编辑流程（COLMAP位姿估计→未编辑场景初始化→迭代编辑更新）压缩为单阶段框架：先用自回归噪声混合模块对视频帧进行多视角一致的2D编辑，再用COLMAP-free的3DGS从编辑后帧直接重建3D场景，速度提升约10倍且支持任意来源视频。

**[3Igs Factorised Tensorial Illumination For 3D Gaussian Splatting](3igs_factorised_tensorial_illumination_for_3d_gaussian_splatting.md)**

:   3iGS 用基于张量分解的连续入射光照场替代 3DGS 中每个高斯体独立优化的球谐系数，结合可学习 BRDF 特征和轻量神经渲染器来建模出射辐射，在保持实时渲染速度的同时显著提升了镜面反射等视角依赖效果的渲染质量。

**[3X2 3D Object Part Segmentation By 2D Semantic Correspondenc](3x2_3d_object_part_segmentation_by_2d_semantic_correspondenc.md)**

:   提出了一种无需训练的3D物体部件分割方法3-By-2，利用扩散模型(DIFT)的2D语义对应关系从已标注2D数据集或少量3D标注对象中迁移部件标签到3D，在zero-shot和few-shot设置下均达到SOTA。

**[6Dgs 6D Pose Estimation From A Single Image And A 3D Gaussia](6dgs_6d_pose_estimation_from_a_single_image_and_a_3d_gaussia.md)**

:   提出6DGS，通过反转3DGS渲染流程——从椭球体表面均匀发射光线（Ellicell），利用注意力机制将光线与目标图像像素绑定，再用加权最小二乘闭式求解相机位姿，无需迭代和初始位姿，在真实场景上旋转精度提升12%、平移精度提升22%，达到15fps近实时性能。

**[A Compact Dynamic 3D Gaussian Representation For Realtime Dy](a_compact_dynamic_3d_gaussian_representation_for_realtime_dy.md)**

:   将3DGS中的位置和旋转参数建模为时间的函数（位置用Fourier逼近、旋转用线性逼近），使动态场景的存储复杂度从O(TN)降低到O(LN)，在D-NeRF/DyNeRF/HyperNeRF三个数据集上实现了与NeRF方法匹敌的渲染质量，同时保持118+ FPS的实时渲染速度。

**[Analytic-Splatting Anti-Aliased 3D Gaussian Splatting Via Analytic Integration](analytic-splatting_anti-aliased_3d_gaussian_splatting_via_analytic_integration.md)**

:   通过使用条件 logistic 函数解析近似高斯信号在像素窗口上的积分，替代 3DGS 的像素中心点采样，实现无混叠的 3D 高斯泼溅，在多尺度渲染上超越 Mip-Splatting。

**[Animatabledreamer Text-Guided Non-Rigid 3D Model Generation And Reconstruction W](animatabledreamer_text-guided_non-rigid_3d_model_generation_and_reconstruction_w.md)**

:   提出 AnimatableDreamer，通过 Canonical Score Distillation (CSD) 技术，从单目视频提取骨骼和运动后生成文本引导的可动画化 3D 非刚体模型，在生成质量和时序一致性上全面超越现有方法。

**[Bad-Gaussians Bundle Adjusted Deblur Gaussian Splatting](bad-gaussians_bundle_adjusted_deblur_gaussian_splatting.md)**

:   首次将运动模糊物理成像模型引入 3D Gaussian Splatting 框架，联合优化场景 Gaussian 参数与曝光时间内的相机运动轨迹，从模糊图像中恢复清晰 3D 场景并实现实时渲染。

**[Benerf Neural Radiance Fields From A Single Blurry Image And Event Stream](benerf_neural_radiance_fields_from_a_single_blurry_image_and_event_stream.md)**

:   提出 BeNeRF，仅从**单张模糊图像**及其对应的事件流（event stream）联合恢复神经辐射场与相机运动轨迹，无需多视角输入或已知位姿，即可实现高质量去模糊与新视角合成。

**[Bi-Directional Contextual Attention For 3D Dense Captioning](bi-directional_contextual_attention_for_3d_dense_captioning.md)**

:   提出 BiCA，通过双向上下文注意力机制将 instance query 和 context query 解耦并行解码，解决了 3D 密集描述中定位与描述生成之间的目标冲突，在 ScanRefer 和 Nr3D 两个基准上取得 SOTA。

**[Binomial Self-Compensation For Motion Error In Dynamic 3D Scanning](binomial_self-compensation_for_motion_error_in_dynamic_3d_scanning.md)**

:   提出二项式自补偿(BSC)算法,通过对运动受影响的相位序列按二项式系数加权求和,无需任何中间变量即可指数级消除四步相位移轮廓术中的运动误差,实现与相机帧率相同的高精度动态3D扫描。

**[Caesarnerf Calibrated Semantic Representation For Few-Shot Generalizable Neural ](caesarnerf_calibrated_semantic_representation_for_few-shot_generalizable_neural_.md)**

:   提出 CaesarNeRF，在可泛化 NeRF（GNT）基础上引入场景级语义表征，通过相机位姿校准（特征旋转对齐到目标视角）和序列细化（跨 Transformer 层逐步更新全局特征），在 1-view 设置下 PSNR 比 GNT 提升 1.74dB（LLFF），且可即插即用地增强 IBRNet、MatchNeRF 等其他基线。

**[Camera Height Doesnapost Change Unsupervised Training For Metric Monocular Road-](camera_height_doesnapost_change_unsupervised_training_for_metric_monocular_road-.md)**

:   提出FUMET训练框架,利用道路上检测到的车辆尺寸先验聚合为相机高度估计,并利用相机高度在同一视频序列中不变的事实作为度量尺度监督,使任意单目深度网络无需辅助传感器即可学习绝对尺度。

**[Canonicalfusion Generating Drivable 3D Human Avatars From Multiple Images](canonicalfusion_generating_drivable_3d_human_avatars_from_multiple_images.md)**

:   提出CanonicalFusion框架,通过联合预测深度图和压缩LBS权重映射图实现直接规范化,并利用前向蒙皮可微渲染融合多张图像信息,从多张输入图像生成可驱动的3D人体Avatar。

**[Cg-Slam Efficient Dense Rgb-D Slam In A Consistent Uncertainty-Aware 3D Gaussian](cg-slam_efficient_dense_rgb-d_slam_in_a_consistent_uncertainty-aware_3d_gaussian.md)**

:   提出CG-SLAM,基于一致性和几何稳定性优化的不确定性感知3D高斯场,实现高效稠密RGB-D SLAM,在定位精度和建图质量上均达到SOTA,跟踪速度最高15Hz。

**[Citygaussian Real-Time High-Quality Large-Scale Scene Rendering With Gaussians](citygaussian_real-time_high-quality_large-scale_scene_rendering_with_gaussians.md)**

:   提出 CityGaussian (CityGS)，通过分治训练策略和 block-wise Level-of-Detail 机制，首次实现了城市级大规模场景（>1.5 km²）的高质量 3D Gaussian Splatting 训练与跨尺度实时渲染。

**[Click-Gaussian Interactive Segmentation To Any 3D Gaussians](click-gaussian_interactive_segmentation_to_any_3d_gaussians.md)**

:   提出Click-Gaussian，通过学习两级粒度（粗/细）的可区分3D特征场，结合全局特征引导学习(GFL)解决跨视角mask不一致问题，实现每次点击仅需10ms的实时3D高斯交互式分割，速度比现有方法快15-130倍，同时显著提升分割精度。

**[Coherentgs Sparse Novel View Synthesis With Coherent 3D Gaussians](coherentgs_sparse_novel_view_synthesis_with_coherent_3d_gaussians.md)**

:   提出CoherentGS，通过为3DGS引入结构化表示（每像素一个高斯）并利用隐式卷积解码器和全变差损失构建单视图和多视图一致性约束，结合基于单目深度的初始化策略，在极稀疏输入（如3张图像）下实现高质量新视角合成，LPIPS指标显著优于现有NeRF方法。

**[Comboverse Compositional 3D Assets Creation Using Spatially-Aware Diffusion Guid](comboverse_compositional_3d_assets_creation_using_spatially-aware_diffusion_guid.md)**

:   提出ComboVerse，一个组合式3D资产生成框架：先将包含多个物体的输入图像分解并独立重建为单物体3D模型，再通过空间感知的Score Distillation Sampling (SSDS)引导物体的位置、缩放和旋转参数优化，实现高质量多物体组合3D资产创建，在CLIP Score和人类评估中均显著优于现有方法。

**[Compress3D A Compressed Latent Space For 3D Generation From A Single Image](compress3d_a_compressed_latent_space_for_3d_generation_from_a_single_image.md)**

:   提出一种高度压缩的 triplane 潜空间自编码器，配合两阶段扩散模型（先生成 shape embedding 再生成 triplane latent），仅需 7 秒即可从单张图像生成高质量 3D 资产，且训练数据和时间远少于同类方法。

**[Cor-Gs Sparse-View 3D Gaussian Splatting Via Co-Regularization](cor-gs_sparse-view_3d_gaussian_splatting_via_co-regularization.md)**

:   发现同时训练两个 3DGS 辐射场时它们在高斯位置和渲染结果上的差异（disagreement）与重建质量负相关，据此提出 CoR-GS 通过协同剪枝和伪视角协同正则化来抑制不准确重建，在稀疏视角下实现 SOTA 新视角合成。

**[Crm Single Image To 3D Textured Mesh With Convolutional Reconstruction Model](crm_single_image_to_3d_textured_mesh_with_convolutional_reconstruction_model.md)**

:   提出卷积重建模型 CRM，利用 triplane 与六个正交视图之间的空间对齐先验，用 U-Net 替代 Transformer 直接从六视图映射到 triplane，结合 FlexiCubes 端到端训练，10 秒内从单张图像生成高保真纹理网格，训练成本仅为 LRM 的 1/8。

**[Crossscore Towards Multi-View Image Evaluation And Scoring](crossscore_towards_multi-view_image_evaluation_and_scoring.md)**

:   提出 Cross-Reference（CR）图像质量评估新范式，通过对比查询图像与多个不同视角参考图像，利用 cross-attention 神经网络预测与 SSIM 高度相关的像素级质量分数，无需 ground truth 参考图像即可评估新视角合成质量。

**[D-Sco Dual-Stream Conditional Diffusion For Monocular Hand-Held Object Reconstru](d-sco_dual-stream_conditional_diffusion_for_monocular_hand-held_object_reconstru.md)**

:   提出双流条件扩散模型 D-SCo 从单张 RGB 图像重建手持物体点云，通过统一手-物语义嵌入和手关节几何嵌入两个分支分别提供语义和几何先验，配合手约束质心固定策略稳定扩散过程，在 ObMan 上 F-5 达 0.61（超 DDF-HO 10.9%），真实数据集 HO3D/MOW 上也大幅领先。

**[Datenerf Depth-Aware Text-Based Editing Of Nerfs](datenerf_depth-aware_text-based_editing_of_nerfs.md)**

:   利用NeRF重建的场景深度信息来引导基于文本的2D图像编辑（通过深度条件化的ControlNet + 投影修复方案），从而实现多视角一致的高质量NeRF场景编辑。

**[Deblur E-Nerf Nerf From Motion-Blurred Events Under High-Speed Or Low-Light Cond](deblur_e-nerf_nerf_from_motion-blurred_events_under_high-speed_or_low-light_cond.md)**

:   提出 Deblur e-NeRF，通过物理精确的像素带宽模型来建模事件相机的运动模糊，首次实现从运动模糊的事件流中直接有效地重建无模糊 NeRF。

**[Deceptive-Nerf3Dgs Diffusion-Generated Pseudo-Observations For High-Quality Spar](deceptive-nerf3dgs_diffusion-generated_pseudo-observations_for_high-quality_spar.md)**

:   利用微调的 Stable Diffusion + ControlNet 将粗糙 NeRF/3DGS 渲染结果转化为高质量伪观测图像，将稀疏输入视图增密 5-10 倍后重新训练，在 Hypersim/LLFF/ScanNet 等数据集上超越 FreeNeRF 等方法 1-2dB PSNR，训练速度比扩散正则化方法快约 10 倍。

**[Deep Patch Visual Slam](deep_patch_visual_slam.md)**

:   基于 DPVO 视觉里程计系统，通过高效的邻近回环检测和经典回环检测机制，将其扩展为完整的 SLAM 系统 DPV-SLAM，在单 GPU 上实现实时、高精度、低显存的单目视觉 SLAM。

**[Dg-Pic Domain Generalized Point-In-Context Learning For Point Cloud Understandin](dg-pic_domain_generalized_point-in-context_learning_for_point_cloud_understandin.md)**

:   提出 DG-PIC，首个在统一模型中同时处理多领域多任务的点云理解框架，通过双层次源域原型估计和测试时特征平移机制，在不更新模型的情况下提升对未知域的泛化能力。

**[Differentiable Convex Polyhedra Optimization From Multi-View Images](differentiable_convex_polyhedra_optimization_from_multi-view_images.md)**

:   提出一种基于对偶变换和三平面交点求解的可微凸多面体构造方法，绕过隐式场监督，直接利用多视角图像损失进行梯度优化，实现高保真的凸多面体形状表示。

**[Diffusion Model Is A Good Pose Estimator From 3D Rf-Vision](diffusion_model_is_a_good_pose_estimator_from_3d_rf-vision.md)**

:   提出mmDiff，一种基于扩散模型的毫米波雷达人体姿态估计框架，通过全局-局部雷达上下文提取和结构-运动一致性约束，有效应对雷达点云稀疏、噪声大和信号不一致的挑战，显著超越现有SOTA。

**[Diffusion Models For Monocular Depth Estimation Overcoming Challenging Condition](diffusion_models_for_monocular_depth_estimation_overcoming_challenging_condition.md)**

:   利用text-to-image扩散模型（ControlNet/T2I-Adapter）将简单场景图像转化为保持同一3D结构的恶劣条件图像，通过自蒸馏微调现有单目深度估计网络，统一解决恶劣天气和非朗伯表面等分布外挑战。

**[Divide And Fuse Body Part Mesh Recovery From Partially Visible Human Images](divide_and_fuse_body_part_mesh_recovery_from_partially_visible_human_images.md)**

:   提出"分而治之"的自底向上人体网格重建方法，通过独立重建各身体部位后融合，有效解决人体大面积不可见时传统自顶向下方法（如SMPL）失效的问题。

**[Dreamdissector Learning Disentangled Text-To-3D Generation From 2D Diffusion Pri](dreamdissector_learning_disentangled_text-to-3d_generation_from_2d_diffusion_pri.md)**

:   提出DreamDissector框架，通过Neural Category Field和Deep Concept Mining将包含多物体交互的text-to-3D NeRF解耦为独立的带纹理网格，实现物体级别的3D编辑控制。

**[Dreamdrone Text-To-Image Diffusion Models Are Zero-Shot Perpetual View Generator](dreamdrone_text-to-image_diffusion_models_are_zero-shot_perpetual_view_generator.md)**

:   提出DreamDrone——一个零样本、无需训练的无限飞行场景生成管线，通过直接对预训练扩散模型的中间latent code进行warping（而非图像级warping），结合特征对应引导和高通滤波策略，实现高质量、几何一致的无界场景生成。

**[Dreamscene360 Unconstrained Text-To-3D Scene Generation With Panoramic Gaussian ](dreamscene360_unconstrained_text-to-3d_scene_generation_with_panoramic_gaussian_.md)**

:   提出DreamScene360，利用全景图像作为中间表示，结合GPT-4V自精炼机制和全景3D高斯溅射技术，实现从文本到沉浸式360°3D场景的快速生成。

**[Dreamview Injecting View-Specific Text Guidance Into Text-To-3D Generation](dreamview_injecting_view-specific_text_guidance_into_text-to-3d_generation.md)**

:   提出DreamView，通过自适应文本引导注入模块，将视角特定的文本描述和全局文本描述协同注入扩散模型，实现可定制化且多视角一致的文本到3D生成。

**[Dspdet3D 3D Small Object Detection With Dynamic Spatial Pruning](dspdet3d_3d_small_object_detection_with_dynamic_spatial_pruning.md)**

:   提出动态空间剪枝（DSP）策略，在多级 3D 检测器的解码器中逐级移除已检测到大物体区域的体素特征，使检测器能以高空间分辨率处理场景、大幅提升小目标检测精度（ScanNet 小目标 mAP@0.25 从 27.5% 提升到 44.8%），同时通过剪枝将显存降低为同分辨率方法的 1/5。

**[Dual-Level Adaptive Self-Labeling For Novel Class Discovery In Point Cloud Segme](dual-level_adaptive_self-labeling_for_novel_class_discovery_in_point_cloud_segme.md)**

:   提出双层自适应自标注方法，通过半松弛最优传输处理类别不平衡问题，并结合区域级表示增强点级分类器的学习，在点云分割中实现高效的新类发现。

**[Gaussian Grouping Segment And Edit Anything In 3D Scenes](gaussian_grouping_segment_and_edit_anything_in_3d_scenes.md)**

:   为 3D Gaussian Splatting 中的每个高斯学习 16 维 Identity Encoding 实现实例级分组，使用 SAM + DEVA 视频跟踪生成多视图一致的 2D 伪标签做监督，在 LERF-Mask 开放词汇分割上 mIoU 达 69-77%（超 LERF 2 倍+），全景分割超 Panoptic Lifting 4.9% mIoU 且 14× 更快，同时支持 3D 物体移除/修复/着色/风格迁移等多种编辑。

**[Milliflow Scene Flow Estimation On Mmwave Radar Point Cloud For Human Motion Sen](milliflow_scene_flow_estimation_on_mmwave_radar_point_cloud_for_human_motion_sen.md)**

:   提出首个毫米波雷达点云场景流估计方法 milliFlow，通过多尺度特征提取、全局聚合、GRU 时序传播和约束回归，在自建数据集上将 EPE3D 从次优 0.107m 降至 0.046m（cm 级精度），并展示场景流特征对人体活动识别（+7.9%）、人体部位解析（+3.6%）、人体追踪等下游任务的增强效果。

**[Mvsgaussian Fast Generalizable Gaussian Splatting Reconstruction From Multi-View](mvsgaussian_fast_generalizable_gaussian_splatting_reconstruction_from_multi-view.md)**

:   将MVS的代价体深度估计与3D高斯溅射结合，通过混合渲染(splatting+volume rendering)提升泛化性，并提出基于多视图几何一致性的点云聚合策略，使per-scene优化仅需45秒就超越3D-GS的10分钟效果。

**[Novum Neural Object Volumes For Robust Object Classification](novum_neural_object_volumes_for_robust_object_classification.md)**

:   提出 NOVUM 架构，为每个物体类别维护一个由 3D 高斯组成的神经体积表征，通过将图像特征与各类别的高斯特征匹配实现分类，在遮挡/损坏/真实 OOD 场景下相比 ResNet/ViT/Swin 等标准架构分类准确率提升 6-33%，同时支持 3D 位姿估计和可解释性可视化。

**[Pointllm Empowering Large Language Models To Understand Point Clouds](pointllm_empowering_large_language_models_to_understand_point_clouds.md)**

:   将点云编码器（Point-BERT）通过 MLP 投影层对接 LLaMA 大语言模型，构建 PointLLM；利用 730K 指令数据（660K 简述 + 70K 复杂指令）两阶段训练后，在 3D 物体分类上达到 53.4% 生成式准确率（超越 LLaVA-13B 的 44.2%），在物体描述任务上人类评估胜率 55%（超越人工标注）。

**[Progressive Classifier And Feature Extractor Adaptation For Unsupervised Domain ](progressive_classifier_and_feature_extractor_adaptation_for_unsupervised_domain_.md)**

:   提出 PCFEA 方法用于点云无监督域自适应，通过渐进构建从源域到目标域的中间域，在宏观层面用目标风格特征增强训练分类器（PTFA），微观层面引导特征提取器向中间域对齐（IDFA），在 PointDA-10 上均值准确率达 76.5%（超 SOTA +2.9%），GraspNetPC-10 上达 87.6%（超 SOTA +13.7%）。

**[Scanreason Empowering 3D Visual Grounding With Reasoning Capabilities](scanreason_empowering_3d_visual_grounding_with_reasoning_capabilities.md)**

:   提出 3D reasoning grounding 新任务和 ScanReason 基准（10K+ QA-location pairs，5种推理类型），设计 ReGround3D 框架将 MLLM 推理与 3D grounding 模块通过 Chain-of-Grounding 机制协同，在隐式指令下实现准确的 3D 目标定位。

**[View Selection For 3D Captioning Via Diffusion Ranking](view_selection_for_3d_captioning_via_diffusion_ranking.md)**

:   DiffuRank用预训练text-to-3D扩散模型评估视角对齐度选择最佳视角减少幻觉。

**[When Do We Not Need Larger Vision Models](when_do_we_not_need_larger_vision_models.md)**

:   提出 Scaling on Scales (S2) 策略：冻结小模型（如 ViT-B）在多个图像尺度上运行并拼接特征，无需增加参数即可在分类、分割、深度估计、MLLM 等任务上匹敌甚至超越大模型（ViT-H/G），并从理论和实验上论证了大模型学到的表征大部分可由多尺度小模型线性近似。
