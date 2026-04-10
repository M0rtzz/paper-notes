<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📹 ICCV2025 论文笔记

共 **313** 篇笔记，覆盖 **26** 个领域。

## 领域概览

| 领域 | 篇数 |
|:-----|-----:|
| 🧊 [3D 视觉](#3d_vision) | 99 |
| 🎨 [图像生成](#image_generation) | 39 |
| 🧩 [多模态 VLM](#multimodal_vlm) | 34 |
| 🚗 [自动驾驶](#autonomous_driving) | 25 |
| ✂️ [语义分割](#segmentation) | 17 |
| 🏥 [医学图像](#medical_imaging) | 10 |
| 🎯 [目标检测](#object_detection) | 10 |
| 🧑 [人体理解](#human_understanding) | 8 |
| 🖼️ [图像恢复](#image_restoration) | 7 |
| 📦 [模型压缩](#model_compression) | 7 |
| 🔄 [自监督/表示学习](#self_supervised) | 7 |
| 🎬 [视频理解](#video_understanding) | 7 |
| 🛡️ [AI 安全](#ai_safety) | 4 |
| 🤖 [机器人/具身智能](#robotics) | 4 |
| 🎵 [音频/语音](#audio_speech) | 3 |
| ⚡ [LLM 效率](#llm_efficiency) | 3 |
| 🛰️ [遥感](#remote_sensing) | 3 |
| 💬 [LLM / NLP](#llm_nlp) | 2 |
| 📐 [优化/理论](#optimization) | 2 |
| 🔗 [因果推理](#causal_inference) | 1 |
| 🦾 [LLM Agent](#llm_agent) | 1 |
| 💡 [LLM 推理](#llm_reasoning) | 1 |
| ✍️ [文本生成](#nlp_generation) | 1 |
| 🎮 [强化学习](#reinforcement_learning) | 1 |
| 📡 [信号/通信](#signal_comm) | 1 |
| 📂 [其他](#others) | 16 |

---

## 🧊 3D 视觉 { #3d_vision }

**[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth Reconstruction via Physics Simulation for Scene Update](3d_vision/2d_gaussian_splattingbased_sparseview_transparent_object_dep.md)**

:   提出TRAN-D，一种基于2D Gaussian Splatting的稀疏视角透明物体深度重建方法，通过分割引导的object-aware损失优化遮挡区域Gaussian分布，并利用物理仿真（MPM）实现物体移除后的场景动态更新，仅需单张图像即可完成场景刷新。

**[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](3d_vision/3d_gaussian_map_with_openset_semantic_grouping_for_visionlan.md)**

:   提出基于3D高斯溅射的场景地图表示（3D Gaussian Map），结合开放集语义分组机制，为视觉-语言导航（VLN）构建兼顾几何结构与丰富语义的3D环境表示，并设计多层级动作预测策略（Multi-Level Action Prediction）融合多粒度空间-语义线索辅助导航决策。

**[3D Mesh Editing using Masked LRMs](3d_vision/3d_mesh_editing_using_masked_lrms.md)**

:   提出MaskedLRM，将3D形状编辑重构为条件重建问题——训练时随机生成3D遮挡物遮盖多视角输入，用一张干净条件视图引导被遮挡区域的补全；推理时用户定义编辑区域并提供单张编辑图像，模型在**<3秒单次前传**中完成3D网格编辑，比优化方法快2-10倍，能执行拓扑变化编辑（加孔/加把手），重建质量与SOTA持平。

**[3D Test-time Adaptation via Graph Spectral Driven Point Shift](3d_vision/3d_test-time_adaptation_via_graph_spectral_driven_point_shift.md)**

:   提出 GSDTTA，将3D点云测试时自适应从空间域转移到图谱域，仅优化最低10%频率分量即可适配点云的全局结构，配合特征图引导的自训练策略，在 ModelNet40-C 和 ScanObjectNN-C 上达到 SOTA。

**[3D Test-time Adaptation via Graph Spectral Driven Point Shift](3d_vision/3d_testtime_adaptation_via_graph_spectral_driven_point_shift.md)**

:   提出GSDTTA，首次将3D点云的测试时适应从空间域转移到图谱域，通过仅优化最低10%频率分量（减少约90%参数）实现全局结构调整，并结合特征图引导的自训练策略生成伪标签，在ModelNet40-C和ScanObjectNN-C上显著超越现有3D TTA方法。

**[3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding](3d_vision/3dgraphllm_combining_semantic_graphs_and_large_language_mode.md)**

:   提出3DGraphLLM，首个将**3D语义场景图的可学习表示**直接输入LLM的方法——通过k近邻子图+三元组(object1, relation, object2)编码物体间语义关系，然后投影到LLM的token嵌入空间。在ScanRefer上Acc@0.5提升+6.4%（vs无语义关系的Chat-Scene），在Multi3DRefer上F1@0.5提升+7.5%，推理速度比GPT4Scene-HDM快5倍。

**[3DGS-LM: Faster Gaussian-Splatting Optimization with Levenberg-Marquardt](3d_vision/3dgslm_faster_gaussiansplatting_optimization_with_levenbergm.md)**

:   将3D Gaussian Splatting的ADAM优化器替换为定制化的Levenberg-Marquardt（LM）二阶优化器，通过高效CUDA并行化的PCG算法和梯度缓存结构实现Jacobian-向量积加速，在保持相同重建质量的前提下将优化时间缩短约20%。

**[4D Gaussian Splatting SLAM](3d_vision/4d_gaussian_splatting_slam.md)**

:   提出首个完整的4D Gaussian Splatting SLAM系统，在动态场景中同时进行相机位姿跟踪和4D高斯辐射场重建——将高斯原语分为静态/动态集合，通过稀疏控制点+MLP建模动态物体运动，并创新性地设计2D光流图渲染算法来监督动态高斯的运动学习。

**[4D Visual Pre-training for Robot Learning](3d_vision/4d_visual_pretraining_for_robot_learning.md)**

:   FVP提出将3D视觉预训练建模为"下一帧点云预测"问题，用条件扩散模型从历史帧点云预测未来帧点云来学习3D视觉表示，在12个真实世界操作任务中将DP3的平均成功率提升28%，达到SOTA水平。

**[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](3d_vision/7dgs_unified_spatial-temporal-angular_gaussian_splatting.md)**

:   将3DGS扩展到7维（空间3D+时间1D+方向3D），通过条件切片机制将7D高斯投影为与3DGS管线兼容的3D高斯，在具有视角依赖效果的动态场景上PSNR提升最高7.36dB，同时维持401 FPS实时渲染。

**[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](3d_vision/7dgs_unified_spatialtemporalangular_gaussian_splatting.md)**

:   提出7DGS，将场景元素建模为**7维高斯分布**（3D空间+1D时间+3D视角方向），通过条件切片机制将7D高斯转换为与时间和视角相关的条件3D高斯，统一处理动态场景+视角依赖效果，在自定义7DGS-PBR数据集上比4DGS PSNR提升高达7.36dB，仅用15.3%的高斯点数，401FPS实时渲染。

**[A3GS: Arbitrary Artistic Style into Arbitrary 3D Gaussian Splatting](3d_vision/a3gs_arbitrary_artistic_style_into_arbitrary_3d_gaussian_spl.md)**

:   提出A³GS，首个**前馈式零样本3DGS风格迁移**网络——使用图卷积网络(GCN)自编码器将3DGS场景编码到潜在空间，通过AdaIN注入任意风格图像特征，仅需**10秒**即可将任意风格迁移到任意3D场景，无需逐风格优化，可处理大规模3DGS场景。

**[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](3d_vision/a_lesson_in_splats_teacherguided_diffusion_for_3d_gaussian_s.md)**

:   提出一种用2D图像监督训练3D扩散模型的框架：利用预训练的确定性3D重建模型作为"噪声教师"生成3D噪声样本，通过多步去噪策略和渲染损失实现跨模态（3D去噪+2D监督）训练，在用更小模型的情况下超越教师模型0.5-0.85 PSNR。

**[A Recipe for Generating 3D Worlds from a Single Image](3d_vision/a_recipe_for_generating_3d_worlds_from_a_single_image.md)**

:   将单图到3D世界生成分解为两个更简单的子问题——全景合成（无训练in-context learning）和点云条件修复（仅5k步微调ControlNet），结合3DGS重建出可在VR中2米立方体范围内导航的沉浸式3D环境，在图像质量指标上全面超越WonderJourney和DimensionX等SOTA方法。

**[A Simple yet Mighty Hartley Diffusion Versatilist for Generalizable Dense Vision Tasks](3d_vision/a_simple_yet_mighty_hartley_diffusion_versatilist_for_genera.md)**

:   提出HarDiff——基于离散Hartley变换的频域学习策略，通过低频训练（从源域提取结构先验）和高频采样（利用目标域细节引导）增强扩散模型在稠密视觉任务上的跨域泛化能力，在语义分割、深度估计和去雾等12个基准上取得SOTA。

**[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](3d_vision/aaagaussians_antialiased_and_artifactfree_3d_gaussian_render.md)**

:   通过在3DGS渲染管线的所有环节中融入完整的3D评估（而非2D splat近似），提出自适应3D平滑滤波器、视空间边界计算和基于视锥的tile剔除，统一解决了3DGS中的锯齿、投影伪影和弹出伪影（popping），在OOD视角下大幅优于现有方法，同时保持实时渲染（>100 FPS）。

**[Accelerate 3D Object Detection Models via Zero-Shot Attention Key Pruning](3d_vision/accelerate_3d_object_detection_models_via_zero-shot_attention_key_pruning.md)**

:   提出 tgGBC（trim keys gradually Guided By Classification scores），一种零样本运行时剪枝方法，利用分类分数与注意力图的乘积计算键重要性，逐层剪除不重要的键，在多个3D检测器上实现Transformer解码器近2×加速且性能损失<1%。

**[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](3d_vision/adahuman_animatable_detailed_3d_human_generation_with_compos.md)**

:   提出AdaHuman框架，通过姿态条件的联合3D扩散模型（在扩散过程中同步进行多视角图像生成与3DGS重建以保证3D一致性）和组合式3DGS细化模块（利用crop-aware camera ray map融合局部精细细节），从单张野外图片生成高保真可动画的3D人体avatar，在重建和重姿态任务上全面超越现有SOTA。

**[Adversarial Exploitation of Data Diversity Improves Visual Localization](3d_vision/adversarial_exploitation_of_data_diversity_improves_visual_l.md)**

:   提出RAP（Robust Absolute Pose regression）——基于外观感知3DGS的双分支联合训练框架，通过对抗判别器弥合合成-真实域差距+外观/位姿增强数据作为额外监督，在Cambridge Landmarks上平移/旋转误差分别降低38-50%/41-44%，在日夜场景和驾驶场景中表现尤为突出。

**[AJAHR: Amputated Joint Aware 3D Human Mesh Recovery](3d_vision/ajahr_amputated_joint_aware_3d_human_mesh_recovery.md)**

:   首个面向截肢者的3D人体网格恢复框架——通过合成100万+截肢者图像(A3D)、设计BPAC-Net截肢分类器区分截肢与遮挡、以及双Tokenizer切换策略分别编码截肢/正常位姿先验，在截肢者数据上大幅领先(ITW-amputee上MVE比TokenHMR低16.87)，非截肢者数据上也保持竞争力。

**[Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images](3d_vision/amodal3r_amodal_3d_reconstruction_from_occluded_2d_images.md)**

:   提出Amodal3R，一个端到端的遮挡感知3D重建模型，通过在TRELLIS基础上引入mask加权交叉注意力和遮挡感知注意力层，直接在3D潜空间中从部分遮挡的2D图像重建完整的3D物体形状和外观，大幅超越先前"2D补全→3D重建"的两阶段方法。

**[Amodal Depth Anything: Amodal Depth Estimation in the Wild](3d_vision/amodal_depth_anything_amodal_depth_estimation_in_the_wild.md)**

:   提出非模态相对深度估计新范式，构建大规模真实数据集ADIW（564K），基于Depth Anything V2和DepthFM设计两个互补框架（Amodal-DAV2和Amodal-DepthFM），通过最小化修改预训练模型实现遮挡区域深度预测，在ADIW上RMSE比之前SOTA提升27.4%。

**[AnimateAnyMesh: A Feed-Forward 4D Foundation Model for Text-Driven Universal Mesh Animation](3d_vision/animateanymesh_a_feedforward_4d_foundation_model_for_textdri.md)**

:   提出AnimateAnyMesh，首个前馈式文本驱动通用Mesh动画框架：通过DyMeshVAE将动态Mesh分解为初始位置和相对轨迹并压缩到潜空间，再用基于Rectified Flow的MMDiT模型学习文本条件下的轨迹分布，配合4M+规模的DyMesh数据集训练，在6秒内即可为任意拓扑Mesh生成高质量动画，全面碾压DG4D、L4GM和Animate3D。

**[AnyI2V: Animating Any Conditional Image with Motion Control](3d_vision/anyi2v_animating_any_conditional_image_with_motion_control.md)**

:   提出AnyI2V，一个无需训练的框架，可接受任意模态图像（mesh、点云、深度图、骨架等）作为首帧条件，结合用户定义的轨迹实现运动控制的视频生成，在FID/FVD/ObjMC指标上优于现有training-free方法并与训练方法竞争。

**[AR-1-to-3: Single Image to Consistent 3D Object Generation via Next-View Prediction](3d_vision/ar1to3_single_image_to_consistent_3d_object_via_nextview_pre.md)**

:   提出AR-1-to-3，一种基于扩散模型的自回归下一视角预测框架，通过"先近后远"的渐进式生成策略，配合Stacked-LE（堆叠局部特征编码）和LSTM-GE（全局特征编码）两种条件注入机制，显著提升了单图到多视角生成的一致性，在GSO数据集上PSNR达13.18（相比InstantMesh的10.67提升23.5%），Chamfer Distance降至0.063（InstantMesh为0.117）。

**[Articulate3D: Holistic Understanding of 3D Scenes as Universal Scene Description](3d_vision/articulate3d_holistic_understanding_of_3d_scenes_as_universa.md)**

:   提出Articulate3D（280个真实室内场景、8类铰接标注的大规模数据集）和USDNet（基于Mask3D扩展的统一框架），通过密集逐点预测机制同时完成可动零件分割和运动参数估计，在铰接参数预测上比Mask3D†提升5.7%，并支持LLM场景编辑和机器人策略训练。

**[ATLAS: Decoupling Skeletal and Shape Parameters for Expressive Parametric Human Modeling](3d_vision/atlas_decoupling_skeletal_and_shape_parameters_for_expressiv.md)**

:   提出ATLAS参数化人体模型，通过显式解耦外部表面形状和内部骨骼参数，并引入稀疏非线性姿态校正变形，在60万高分辨率扫描数据上训练，实现了比SMPL-X更精确、更可控的3D人体建模。

**[Auto-Regressively Generating Multi-View Consistent Images](3d_vision/auto-regressively_generating_multi-view_consistent_images.md)**

:   提出 MV-AR，首次将自回归模型引入多视图图像生成，利用所有先前视图作为条件逐步生成后续视图，配合统一的多模态条件注入模块和 Shuffle View 数据增强，在文本/图像/形状条件下均达到与扩散模型可比的一致性。

**[AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting](3d_vision/autoocc_automatic_openended_semantic_occupancy_annotation_vi.md)**

:   提出AutoOcc，一个以视觉为中心的全自动开放式语义占据标注流水线，通过视觉-语言模型引导的可微高斯泼溅（VL-GS）实现无需人工标签的3D语义占据生成，在Occ3D-nuScenes上以纯视觉输入就达到IoU 83.01/mIoU 20.92，大幅超越现有自动标注方法。

**[Back on Track: Bundle Adjustment for Dynamic Scene Reconstruction](3d_vision/back_on_track_bundle_adjustment_for_dynamic_scene_reconstruc.md)**

:   提出BA-Track框架，通过学习型3D点追踪器将观测到的运动解耦为相机引起的运动和物体自身运动，使传统束调整(BA)能够无差别地处理静态和动态点，在相机位姿估计(ATE在Sintel上达到0.034，较SOTA降低一半以上)和稠密3D重建上取得显著提升。

**[Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction](3d_vision/baking_gaussian_splatting_into_diffusion_denoiser_for_fast_a.md)**

:   提出DiffusionGS，将3D高斯点云直接嵌入扩散模型的去噪器中，通过单阶段3D扩散实现从单张图片到3D物体生成和场景重建，在ABO/GSO上PSNR超越SOTA 2.20/1.25 dB，RealEstate10K上超1.34 dB，推理速度约6秒（A100）。

**[BANet: Bilateral Aggregation Network for Mobile Stereo Matching](3d_vision/banet_bilateral_aggregation_network_for_mobile_stereo_matchi.md)**

:   提出双边聚合网络BANet，通过将代价体分离为高频细节体和低频平滑体分别聚合再融合，仅使用2D卷积即可在移动设备上实现实时高精度立体匹配（骁龙8 Gen 3上45ms，KITTI 2015 D1-all=1.83%，比MobileStereoNet-2D精度高35.3%）。

**[Benchmarking and Learning Multi-Dimensional Quality Evaluator for Text-to-3D Generation](3d_vision/benchmarking_and_learning_multidimensional_quality_evaluator.md)**

:   构建MATE-3D基准（8类prompt×8种方法=1280个textured mesh，4维度×21人主观评分=107520标注）并提出HyperScore多维质量评估器：通过可学习条件特征+条件特征融合(模拟注意力转移)+超网络生成维度自适应映射函数(模拟决策过程变化)，在语义对齐、几何、纹理、整体4个维度上全面超越现有指标。

**[Benchmarking Egocentric Visual-Inertial SLAM at City Scale](3d_vision/benchmarking_egocentric_visualinertial_slam_at_city_scale.md)**

:   提出 LaMAria——首个城市尺度的第一人称多传感器 VIO/SLAM 基准数据集，利用测绘级控制点提供厘米精度的地面真值，系统评估了学术界主流 SLAM 方案在真实第一人称场景下的表现，揭示了现有方法与商业系统之间的巨大差距。

**[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve Gaussian Splatting](3d_vision/beziergs_dynamic_urban_scene_reconstruction_with_bezier_curv.md)**

:   用可学习的Bézier曲线显式建模动态物体的运动轨迹，替代传统依赖精确bbox标注的范式，实现了对自动驾驶街景中动/静态成分的准确分离与高保真重建。

**[BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis](3d_vision/billboard_splatting_bbsplat_learnable_textured_primitives_fo.md)**

:   提出BBSplat——用可学习的RGB纹理和alpha贴图替代2D Gaussian Splatting中的高斯分布不透明度，使每个平面基元具有任意形状和逐像素颜色控制，在用更少基元的情况下弥补2DGS与3DGS之间的渲染质量差距，同时保留精确网格提取能力并实现最高×17的存储压缩。

**[Blended Point Cloud Diffusion for Localized Text-guided Shape Editing](3d_vision/blended_point_cloud_diffusion_for_localized_textguided_shape.md)**

:   提出 BlendedPC，将局部文本引导的3D形状编辑重新定义为语义inpainting问题，通过在Point·E基础上训练Inpaint-E模型，并在推理时引入无需反演(inversion-free)的坐标混合(coordinate blending)机制，在保持原始形状身份的同时实现精准局部编辑，在ShapeTalk数据集上全面超越现有方法。

**[Bolt3D: Generating 3D Scenes in Seconds](3d_vision/bolt3d_generating_3d_scenes_in_seconds.md)**

:   提出一种基于潜在扩散模型的前馈式3D场景生成方法，通过将3D场景表示为多组Splatter Image并使用专门训练的几何VAE，**在单GPU上7秒内生成完整3D场景**，推理成本比优化式方法（CAT3D）降低300倍。

**[Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration](3d_vision/boost_3d_reconstruction_using_diffusion-based_monocular_camera_calibration.md)**

:   提出 DM-Calib，利用 Stable Diffusion 先验进行单目相机内参估计，设计了 Camera Image 表示将内参无损编码为图像，结合 RANSAC 解算焦距和光心，在5个零样本数据集上大幅超越现有标定方法，并推进了度量深度估计、位姿估计和稀疏视图重建等下游任务。

**[Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration](3d_vision/boost_3d_reconstruction_using_diffusionbased_monocular_camer.md)**

:   提出DM-Calib——基于扩散模型的单目相机内参估计方法：设计Camera Image表示（将内参无损编码为3通道图像=方位角+仰角+灰度图），微调Stable Diffusion生成Camera Image，用RANSAC提取内参，在5个零样本数据集上超越所有基线，并将相机标定扩展到度量深度估计、位姿估计和稀疏视角3D重建。

**[Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](3d_vision/boosting_multi-view_indoor_3d_object_detection_via_adaptive_3d_volume.md)**

:   提出SGCDet框架，通过几何与上下文感知聚合模块（自适应特征提升）和稀疏体素构建策略（粗到细的自适应体素选择），在不依赖GT场景几何的前提下，实现了高效且高精度的多视图室内3D目标检测。

**[SGCDet: Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](3d_vision/boosting_multi-view_indoor_3d_object_detection_via_adaptive_3d_volume_constructi.md)**

:   SGCDet 通过自适应稀疏3D体素构建和几何-上下文感知聚合，实现了高效精准的多视图室内3D目标检测，无需真实几何监督即超越现有方法。

**[Boosting Multi-View Indoor 3D Object Detection via Adaptive 3D Volume Construction](3d_vision/boosting_multiview_indoor_3d_object_detection_via_adaptive_3.md)**

:   SGCDet通过几何与上下文感知的聚合模块（3D可变形注意力+多视角注意力融合）和基于占据概率的稀疏体素构建策略，在无需ground-truth几何监督的情况下，实现了多视角室内3D目标检测的SOTA性能，同时大幅降低计算开销。

**[Bootstrap3D: Improving Multi-view Diffusion Model with Synthetic Data](3d_vision/bootstrap3d_improving_multiview_diffusion_model_with_synthet.md)**

:   提出Bootstrap3D框架，利用视频扩散模型生成合成多视图数据，并通过微调的MV-LLaVA进行质量过滤与密集描述重写，结合Training Timestep Reschedule (TTR)策略训练多视图扩散模型，在不牺牲视图一致性的前提下大幅提升图像质量和文本对齐能力。

**[BoxDreamer: Dreaming Box Corners for Generalizable Object Pose Estimation](3d_vision/boxdreamer_dreaming_box_corners_for_generalizable_object_pos.md)**

:   提出以3D包围盒角点作为中间表示，通过Transformer解码器预测查询视图中角点的2D投影热图，结合PnP算法实现可泛化的稀疏视角6DoF物体位姿估计，在遮挡和稀疏视角场景下显著优于现有方法。

**[PASDF: Bridging 3D Anomaly Localization and Repair via High-Quality Continuous Geometric Representation](3d_vision/bridging_3d_anomaly_localization_and_repair_via_highquality.md)**

:   提出PASDF框架，通过姿态对齐模块(PAM)将点云对齐到标准姿态 + 神经SDF网络学习连续几何表示 + 基于SDF偏差的异常评分，统一实现3D点云异常检测与异常修复(Marching Cubes提取零等值面作为修复模板)，在Real3D-AD上O-AUROC 80.2%、Anomaly-ShapeNet上90.0%均达SOTA。

**[3DSR: Bridging Diffusion Models and 3D Representations for 3D Consistent Super-Resolution](3d_vision/bridging_diffusion_models_and_3d_representations_a_3d_consis.md)**

:   提出3DSR——将扩散超分模型与3DGS表示交替迭代实现3D一致超分：每步去噪后将SR图像训练到3DGS中获得3D一致渲染→重编码回潜在空间引导下一步去噪，无需微调任何模型即显式保证跨视角一致性，在LLFF上PSNR提升1.16dB+FID降低50%(vs StableSR)。

**[Bring Your Rear Cameras for Egocentric 3D Human Pose Estimation](3d_vision/bring_your_rear_cameras_for_egocentric_3d_human_pose_estimat.md)**

:   首次研究HMD后置相机对全身姿态追踪的价值，提出Transformer-based多视角热力图精炼模块(利用可变形注意力+不确定性感知遮罩)，解决后视角2D关节检测不可靠的问题，并发布两个大规模数据集(Ego4View-Syn/RW)，在Ego4View-RW上MPJPE比SOTA EgoPoseFormer提升>10%(63.38→56.94mm)。

**[BUFFER-X: Towards Zero-Shot Point Cloud Registration in Diverse Scenes](3d_vision/bufferx_towards_zeroshot_point_cloud_registration_in_diverse.md)**

:   通过几何自适应bootstrapping确定体素大小/搜索半径、用FPS替代学习型关键点检测器、以及patch级坐标归一化，构建了一个无需人工调参即可在11个跨域数据集上实现零样本点云配准的pipeline BUFFER-X，在室内外多传感器多场景下取得了平均排名第一的成功率。

**[CAD-Recode: Reverse Engineering CAD Code from Point Clouds](3d_vision/cad-recode_reverse_engineering_cad_code_from_point_clouds.md)**

:   提出 CAD-Recode，将点云翻译为可执行的 Python CadQuery 代码来重建 CAD 模型，利用预训练 LLM（Qwen2-1.5B）作为解码器配合轻量级点云编码器，在 DeepCAD、Fusion360 和 CC3D 三个基准上实现了 10 倍以上的 Chamfer Distance 降低。

**[CAD-Recode: Reverse Engineering CAD Code from Point Clouds](3d_vision/cadrecode_reverse_engineering_cad_code_from_point_clouds.md)**

:   将CAD sketch-extrude序列表示为Python代码，利用轻量级点云投影器 + 预训练LLM解码器将点云翻译为可执行Python代码来重建CAD模型，在DeepCAD/Fusion360/真实世界CC3D数据集上显著超越现有方法，且输出代码可被通用LLM理解用于CAD编辑和问答。

**[Can3Tok: Canonical 3D Tokenization and Latent Modeling of Scene-Level 3D Gaussians](3d_vision/can3tok_canonical_3d_tokenization_and_latent_modeling_of_sce.md)**

:   提出Can3Tok——首个场景级3DGS VAE：通过cross-attention将大量(40K)无序3D Gaussian压缩到低维canonical token(256×768→64×64×4) + 3DGS归一化解决跨场景尺度不一致 + 语义感知过滤去除floater噪声，在DL3DV-10K上唯一成功的场景级3DGS潜在建模方法(L2=30.1, 失败率2.5%)，支持text-to-3DGS和image-to-3DGS前馈生成。

**[CATSplat: Context-Aware Transformer with Spatial Guidance for Generalizable 3D Gaussian Splatting from A Single-View Image](3d_vision/catsplat_contextaware_transformer_with_spatial_guidance_for.md)**

:   提出CATSplat——单视图前馈3DGS重建的泛化Transformer框架：利用VLM文本嵌入（上下文先验）和3D点云特征（空间先验）通过双重cross-attention增强图像特征，在RE10K等数据集上在PSNR/SSIM/LPIPS全面超越Flash3D，且跨数据集泛化性优异。

**[CHARM3R: Towards Unseen Camera Height Robust Monocular 3D Detector](3d_vision/charm3r_towards_unseen_camera_height_robust_monocular_3d_det.md)**

:   通过数学推导发现回归深度和地面深度在相机高度变化时呈现方向相反的误差趋势，CHARM3R 直接在模型内对两种深度做简单平均来抵消趋势，从而大幅提升单目3D检测器对未见相机高度的泛化能力（CARLA 上提升超过 45%）。

**[CHARM3R: Towards Unseen Camera Height Robust Monocular 3D Detector](3d_vision/charm3r_towards_unseen_camera_height_robust_monocular_3d_detector.md)**

:   通过数学证明回归深度和地平面深度在相机高度变化时具有相反的外推趋势，提出CHARM3R在模型内简单平均两种深度估计来抵消趋势，实现Mono3D对未见相机高度的鲁棒泛化，AP3D提升超过45%。

**[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](3d_vision/comogaussian_continuous_motionaware_gaussian_splatting_from.md)**

:   用Neural ODE建模曝光时间内的连续相机运动轨迹，结合刚体变换和可学习的连续运动修正(CMR)变换，从运动模糊图像重建清晰3D高斯场景，在所有benchmark上大幅超越SOTA。

**[DAP-MAE: Domain-Adaptive Point Cloud Masked Autoencoder for Effective Cross-Domain Learning](3d_vision/dapmae_domainadaptive_point_cloud_masked_autoencoder_for_eff.md)**

:   提出一种域自适应点云MAE框架（DAP-MAE），通过异构域适配器（HDA）和域特征生成器（DFG）两个模块，让一次跨域预训练即可在物体分类、人脸表情识别、部件分割、目标检测等多个不同域的下游任务上都达到SOTA。

**[Diorama: Unleashing Zero-shot Single-view 3D Indoor Scene Modeling](3d_vision/diorama_unleashing_zero-shot_single-view_3d_indoor_scene_modeling.md)**

:   提出Diorama，首个零样本开放世界系统，从单张RGB图像通过模块化管线（开放世界感知+基于CAD的场景建模）生成完整的3D室内场景，包含建筑结构和物体摆放，无需端到端训练或人工标注。

**[Diorama: Unleashing Zero-shot Single-view 3D Indoor Scene Modeling](3d_vision/diorama_unleashing_zeroshot_singleview_3d_indoor_scene_model.md)**

:   提出首个零样本开放世界系统 Diorama，通过模块化地组合 foundation model（GPT-4o、SAM、DinoV2、Metric3D 等），将单张 RGB 图像转化为包含建筑结构和 CAD 物体的完整可组合 3D 室内场景，无需任何端到端训练或人工标注。

**[Easi3R: Estimating Disentangled Motion from DUSt3R Without Training](3d_vision/easi3r_estimating_disentangled_motion_from_dust3r_without_training.md)**

:   提出 Easi3R，一种无需训练的即插即用方法，通过解耦 DUSt3R 注意力层中隐含编码的相机运动与物体运动信息，实现动态视频的4D重建、运动分割和相机位姿估计。

**[EgoM2P: Egocentric Multimodal Multitask Pretraining](3d_vision/egom2p_egocentric_multimodal_multitask_pretraining.md)**

:   EgoM2P 是首个面向自我中心(egocentric)4D理解的多模态多任务大模型，通过时序感知的掩码建模框架统一处理 RGB 视频、深度、注视和相机轨迹四种模态，在多个下游任务上匹配或超越专用模型且快一个数量级。

**[EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images](3d_vision/evagaussians_event_stream_assisted_gaussian_splatting_from_blurry_images.md)**

:   提出EvaGaussians框架，利用事件相机的高时间分辨率事件流辅助3D高斯泼溅从运动模糊图像中学习，通过事件辅助初始化、模糊/事件联合重建损失和事件辅助几何正则化，实现高保真新视图合成并保持实时渲染效率。

**[FaceLift: Learning Generalizable Single Image 3D Face Reconstruction from Synthetic Heads](3d_vision/facelift_learning_generalizable_single_image_3d_face_reconstruction_from_synthet.md)**

:   提出 FaceLift，一种仅在合成数据上训练但能良好泛化到真实图像的单图360度高质量3D人头重建方法，通过多视图潜扩散模型生成身份一致的多视角图像，再用基于 Transformer 的重建器生成像素对齐的3D高斯表示。

**[Fish2Mesh Transformer: 3D Human Mesh Recovery from Egocentric Vision](3d_vision/fish2mesh_transformer_3d_human_mesh_recovery_from_egocentric_vision.md)**

:   提出 Fish2Mesh，一种鱼眼感知的 Transformer 模型，通过新颖的自我中心位置编码（EPE）将等距柱状投影的3D球面信息嵌入 Swin Transformer，实现从头戴式鱼眼相机图像精确恢复3D人体网格。

**[FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images](3d_vision/fross_faster-than-real-time_online_3d_semantic_scene_graph_generation_from_rgb-d.md)**

:   提出FROSS方法，通过将2D场景图直接提升到3D空间并用高斯分布表示物体，实现了超实时（144 FPS）的在线3D语义场景图生成，无需精确点云重建。

**[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](3d_vision/guava_generalizable_upper_body_3d_gaussian_avatar.md)**

:   提出 GUAVA，首个从单张图像通过前馈推理快速重建可动画上半身3D高斯虚拟人的框架，结合模板高斯和 UV 高斯表示，支持丰富面部表情和手势驱动，约0.1s完成重建并实时渲染。

**[Hierarchical Material Recognition from Local Appearance](3d_vision/hierarchical_material_recognition_from_local_appearance.md)**

:   提出面向视觉应用的层级式材质分类学体系(taxonomy)与野外数据集 Matador（含深度图的 ~7200 张材质图像，57类），并基于图注意力网络(GAT)利用分类学的层级亲缘关系进行材质识别，在多个基准数据集上达到 SOTA，同时支持新材质的小样本学习和场景中任意点的材质探测。

**[Image-Guided Shape-from-Template Using Mesh Inextensibility Constraints](3d_vision/image-guided_shape-from-template_using_mesh_inextensibility_constraints.md)**

:   提出一种纯图像引导的无监督 Shape-from-Template (SfT) 方法，仅利用颜色、梯度和轮廓等视觉线索配合网格不可伸展性约束来重建变形物体 3D 形状，比最优无监督方法快 400 倍且精度大幅领先。

**[Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models](3d_vision/learning_3d_object_spatial_relationships_from_pre-trained_2d_diffusion_models.md)**

:   提出从预训练 2D 扩散模型合成图像中学习物体间 3D 空间关系（OOR），通过 3D 提升管线构建配对数据集，训练文本条件化的 score-based 扩散模型对物体对的相对位姿和尺度分布建模，并扩展至多物体场景布局和场景编辑。

**[TesserAct: Learning 4D Embodied World Models](3d_vision/learning_4d_embodied_world_models.md)**

:   提出 TesserAct——一种 4D 具身世界模型，通过训练视频生成模型联合预测 RGB、深度和法线视频，再转换为高质量 4D 场景，实现空间-时间一致的 3D 世界动态模拟和机器人动作规划。

**[LocalDyGS: Multi-view Global Dynamic Scene Modeling via Adaptive Local Implicit Feature Decoupling](3d_vision/localdygs_multi-view_global_dynamic_scene_modeling_via_adaptive_local_implicit_f.md)**

:   提出 LocalDyGS——将全局复杂动态场景分解为种子点定义的局部空间、并通过静态-动态特征解耦生成时序高斯来建模各局部运动的框架，首次实现了大尺度复杂动态场景的高质量重建。

**[LONG3R: Long Sequence Streaming 3D Reconstruction](3d_vision/long3r_long_sequence_streaming_3d_reconstruction.md)**

:   提出 LONG3R，一种基于循环记忆机制的流式多视图3D重建模型，通过记忆门控、双源精炼解码器和3D时空记忆三大创新，在保持实时推理速度的同时显著提升长序列重建质量。

**[MaterialMVP: Illumination-Invariant Material Generation via Multi-view PBR Diffusion](3d_vision/materialmvp_illumination-invariant_material_generation_via_multi-view_pbr_diffus.md)**

:   MaterialMVP 是一个端到端的多视图 PBR 纹理生成模型，通过参考注意力、一致性正则化训练和双通道材质生成框架，从3D网格和图像提示生成光照不变且多视图一致的高质量 PBR 材质。

**[Monocular Semantic Scene Completion via Masked Recurrent Networks](3d_vision/monocular_semantic_scene_completion_via_masked_recurrent_networks.md)**

:   提出 MonoMRN，一个两阶段单目语义场景补全框架：先做粗粒度预测，再用 Masked Sparse GRU（MS-GRU）循环精炼被遮挡区域，并引入距离注意力投影减少深度投影误差，在 NYUv2 和 SemanticKITTI 上均达到 SOTA。

**[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](3d_vision/monomobility_zero-shot_3d_mobility_analysis_from_monocular_videos.md)**

:   MonoMobility 提出首个从单目视频零样本分析关节物体运动部件及运动属性（运动轴、运动类型）的框架，通过2D高斯泼溅场景表示和端到端动态场景优化算法，无需标注数据即可处理旋转、平移及复合运动。

**[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](3d_vision/mugs_multi-baseline_generalizable_gaussian_splatting_reconstruction.md)**

:   MuGS 是首个支持多基线设置（小基线到大基线）的泛化3D高斯泼溅方法，通过融合 MVS 和 MDE 特征、投影-采样深度一致性网络和参考视图损失，在不同基线数据集上均达到 SOTA。

**[Multi-View 3D Point Tracking](3d_vision/multi-view_3d_point_tracking.md)**

:   提出 MVTracker——首个数据驱动的多视角3D点跟踪器，通过将多视图深度图反投影为统一的3D特征点云，利用 kNN 关联和 Transformer 迭代优化，在仅需4个相机的实用配置下实现鲁棒的长程3D点轨迹估计，在 Panoptic Studio 和 DexYCB 上分别达到 3.1 cm 和 2.0 cm 的中位轨迹误差。

**[MV-Adapter: Multi-view Consistent Image Generation Made Easy](3d_vision/mv-adapter_multi-view_consistent_image_generation_made_easy.md)**

:   提出首个基于Adapter的多视角图像生成方案MV-Adapter，通过复制self-attention层+并行注意力架构实现即插即用的多视角生成，在SDXL上达到768分辨率，兼容各种T2I衍生模型。

**[Online Language Splatting](3d_vision/online_language_splatting.md)**

:   首个在 3DGS-SLAM 系统中实现**在线、近实时、开放词汇**语言建图的框架，通过高分辨率 CLIP 嵌入、两阶段在线自编码器压缩和颜色-语言解耦优化三项创新，在精度超越离线 SOTA 的同时实现 40×–200× 的效率提升。

**[PanSt3R: Multi-view Consistent Panoptic Segmentation](3d_vision/panst3r_multi-view_consistent_panoptic_segmentation.md)**

:   基于MUSt3R构建PanSt3R，在**单次前向传播**中同时完成3D重建和多视角全景分割，无需相机参数、无需测试时优化，比现有方法快数个量级。

**[PCR-GS: COLMAP-Free 3D Gaussian Splatting via Pose Co-Regularizations](3d_vision/pcr-gs_colmap-free_3d_gaussian_splatting_via_pose_co-regularizations.md)**

:   提出 PCR-GS，通过 DINO 特征重投影正则化和基于小波变换的频率正则化对相机位姿进行协同约束，在无需 COLMAP 先验的条件下实现了复杂相机轨迹场景的高质量 3D-GS 重建与位姿估计。

**[PolarAnything: Diffusion-based Polarimetric Image Synthesis](3d_vision/polaranything_diffusion-based_polarimetric_image_synthesis.md)**

:   提出 PolarAnything，首个基于单张 RGB 图像生成偏振图像的扩散模型框架，通过对编码后的 AoLP 和 DoLP 进行去噪扩散，实现了物理准确且逼真的偏振属性合成，无需 3D 资产或偏振相机。

**[PseudoMapTrainer: Learning Online Mapping without HD Maps](3d_vision/pseudomaptrainer_learning_online_mapping_without_hd_maps.md)**

:   提出 PseudoMapTrainer，首次实现**完全不依赖 GT HD Map** 训练在线建图模型：利用 2D Gaussian Splatting（RoGS）从多视角相机图像重建道路表面并结合预训练语义分割（Mask2Former）生成矢量化伪标签，同时设计 mask-aware 匹配算法与损失函数处理部分遮挡的伪标签，支持单次行程和多次行程（众包数据）两种模式。

**[RobuSTereo: Robust Zero-Shot Stereo Matching under Adverse Weather](3d_vision/robustereo_robust_zero-shot_stereo_matching_under_adverse_weather.md)**

:   提出 RobuSTereo 框架，通过基于扩散模型的立体数据生成管线和结合去噪 ViT 与 VGG19 的鲁棒特征编码器，大幅提升立体匹配模型在雨、雾、雪等恶劣天气下的零样本泛化能力。

**[RoCo-Sim: Enhancing Roadside Collaborative Perception through Foreground Simulation](3d_vision/roco-sim_enhancing_roadside_collaborative_perception_through_foreground_simulati.md)**

:   RoCo-Sim 是首个面向路侧协同感知的仿真框架，通过相机外参优化、多视图遮挡感知采样、DepthSAM 深度渲染和可扩展后处理工具包，从单张图像生成多样且多视图一致的路侧仿真数据，将路侧3D检测性能提升 83%+。

**[Scene Coordinate Reconstruction Priors](3d_vision/scene_coordinate_reconstruction_priors.md)**

:   提出场景坐标回归(SCR)的概率化训练框架，引入手工设计的深度分布先验和基于3D点云扩散模型的学习先验，在多视角约束不足时显著改善场景重建质量、相机位姿估计和下游任务表现。

**[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian Bracketing](3d_vision/sehdr_single-exposure_hdr_novel_view_synthesis_via_3d_gaussian_bracketing.md)**

:   SeHDR 是首个从单曝光多视图 LDR 图像生成 HDR 新视角的3DGS框架，通过在3D空间扩展包围曝光原理（Bracketed 3D Gaussians）并设计可微分神经曝光融合（NeEF）在球谐空间融合，无需 HDR 监督即超越现有方法 14.3dB。

**[SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians](3d_vision/sheap_self-supervised_head_geometry_predictor_learned_via_2d_gaussians.md)**

:   提出SHeaP，利用2D Gaussian Splatting替代传统可微mesh渲染进行自监督3DMM预测训练，通过将Gaussians绑定到3DMM mesh上实现重动画，并设计graph卷积Gaussians生成器和几何一致性正则化，在NoW和Nersemble基准上超越所有自监督方法。

**[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](3d_vision/sparfels_fast_reconstruction_from_sparse_unposed_imagery.md)**

:   提出Sparfels方法，将3D基础模型（MASt3R）与高效的测试时优化（2DGS）相结合，通过MASt3R提供初始化点云/相机和对应关系引导优化，并创新性地引入泼溅色彩方差损失，在3分钟内从稀疏无位姿图像实现SOTA几何重建。

**[Spatial-Temporal Aware Visuomotor Diffusion Policy Learning](3d_vision/spatial-temporal_aware_visuomotor_diffusion_policy_learning.md)**

:   提出 4D Diffusion Policy（DP4），通过动态高斯世界模型为扩散策略注入3D空间和4D时空感知能力，在17个仿真任务和3个真实机器人任务上大幅超越基线（Adroit +16.4%, DexArt +14%, RLBench +6.45%, 真实任务 +8.6%）。

**[SpinMeRound: Consistent Multi-View Identity Generation Using Diffusion Models](3d_vision/spinmeround_consistent_multi-view_identity_generation_using_diffusion_models.md)**

:   提出 SpinMeRound，一种基于身份嵌入的多视角扩散模型，能从单张或少量人脸图像生成 360° 全头部一致性肖像及对应法线图，在人脸新视角合成任务上超越现有多视角扩散方法。

**[Stable Score Distillation](3d_vision/stable_score_distillation.md)**

:   提出 Stable Score Distillation (SSD)，通过单分类器跨提示词引导和 null-text 分支的跨轨迹正则化，实现更稳定精准的文本引导 2D/3D 编辑，在保持源内容结构的同时提升编辑对齐度。

**[StealthAttack: Robust 3D Gaussian Splatting Poisoning via Density-Guided Illusions](3d_vision/stealthattack_robust_3d_gaussian_splatting_poisoning_via_density-guided_illusion.md)**

:   首次针对3D高斯泼溅(3DGS)提出密度引导的投毒攻击方法，通过在低密度区域注入幻觉物体的高斯点并引入自适应噪声破坏多视角一致性，实现从目标视角清晰可见而不干扰其余视角的隐蔽攻击。

**[Stereo Any Video: Temporally Consistent Stereo Matching](3d_vision/stereo_any_video_temporally_consistent_stereo_matching.md)**

:   提出Stereo Any Video框架，通过融合单目视频深度基础模型先验(Video Depth Anything)、全对全配对相关(all-to-all-pair correlation)和时序凸上采样(temporal convex upsampling)三大核心模块，在不依赖相机位姿或光流的前提下实现空间精确且时序一致的视频立体匹配，在多个数据集零样本设定下达到SOTA。

**[TAR3D: Creating High-Quality 3D Assets via Next-Part Prediction](3d_vision/tar3d_creating_high-quality_3d_assets_via_next-part_prediction.md)**

:   提出TAR3D框架——首次将三平面表示量化为离散几何部件并用GPT自回归生成，通过3D VQ-VAE编码任意面数网格为固定长度序列+TriPE位置编码保留3D空间信息，在文本/图像→3D任务上全面超越现有方法。

**[Trace3D: Consistent Segmentation Lifting via Gaussian Instance Tracing](3d_vision/trace3d_consistent_segmentation_lifting_via_gaussian_instance_tracing.md)**

:   提出Gaussian Instance Tracing (GIT)机制，通过反向光栅化为每个高斯核维护跨视角的实例权重矩阵，统一解决2D分割多视角不一致和边界高斯模糊两大问题，在离线对比学习和在线自提示两种设定下均显著提升3D分割质量。

**[TRACE: Learning 3D Gaussian Physical Dynamics from Multi-view Videos](3d_vision/trace_learning_3d_gaussian_physical_dynamics_from_multi-view_videos.md)**

:   提出TRACE框架，将每个3D高斯核视为刚性粒子并为其学习独立的平移-旋转动力学系统（包含速度、加速度、角速度、角加速度等完整物理参数），无需任何人工标注即可从多视角动态视频中学习3D场景的物理运动规律并准确外推未来帧。

**[VoluMe: Authentic 3D Video Calls from Live Gaussian Splat Prediction](3d_vision/volume_-_authentic_3d_video_calls_from_live_gaussian_splat_prediction.md)**

:   微软提出首个从单目2D摄像头实时预测3D高斯泼溅重建的方法，实现真实感、保真性、实时性和时序稳定性四项要求的统一，使任何人仅用标准笔记本摄像头即可进行体积3D视频通话。

**[ZeroStereo: Zero-shot Stereo Matching from Single Images](3d_vision/zerostereo_zero-shot_stereo_matching_from_single_images.md)**

:   提出 ZeroStereo 管线：从任意单张图像出发，利用单目深度估计生成伪视差，再用微调的扩散修复模型合成高质量右视图，实现只需 35K 合成数据即达到 SOTA 零样本立体匹配泛化性能。

---

## 🎨 图像生成 { #image_generation }

**[Accelerating Diffusion Sampling via Exploiting Local Transition Coherence](image_generation/accelerating_diffusion_sampling_via_exploiting_local_transition_coherence.md)**

:   提出 LTC-Accel，一种基于"局部转移一致性"(Local Transition Coherence) 现象的免训练扩散采样加速方法，通过利用相邻去噪步之间转移算子的强相关性来近似替代当前步的计算，在 Stable Diffusion v2 上实现 1.67× 加速，与蒸馏模型结合可在视频生成中达到 10× 加速。

**[Aether: Geometric-Aware Unified World Modeling](image_generation/aether_geometric-aware_unified_world_modeling.md)**

:   Aether 提出一个几何感知的统一世界模型框架，通过在合成 4D 数据上联合训练重建、预测和规划三大能力，基于 CogVideoX 后训练实现零样本泛化到真实场景。

**[Aether: Geometric-Aware Unified World Modeling](image_generation/aether_geometricaware_unified_world_modeling.md)**

:   提出Aether统一框架，通过任务交错特征学习联合优化4D动态重建、动作条件视频预测和目标条件视觉规划三个核心能力，实现geometry-aware的世界建模，纯合成数据训练即可零样本泛化到真实世界。

**[AnyPortal: Zero-Shot Consistent Video Background Replacement](image_generation/anyportal_zero-shot_consistent_video_background_replacement.md)**

:   AnyPortal 提出了一个零样本、免训练的视频背景替换框架，通过协同利用 IC-Light 的重光照能力和视频扩散模型（CogVideoX）的时序先验，配合新提出的 Refinement Projection Algorithm (RPA) 实现像素级前景保持，在单张 24GB GPU 上即可高效运行。

**[Cns-Bench Benchmarking Image Classifier Robustness Under Continuous Nuisance Shi](image_generation/cns-bench_benchmarking_image_classifier_robustness_under_continuous_nuisance_shi.md)**

:   提出 CNS-Bench，首个利用 LoRA 适配器对扩散模型施加**连续**且**逼真**的干扰偏移（nuisance shift）来系统评估图像分类器 OOD 鲁棒性的基准，覆盖 14 种偏移类型、5 个严重度级别和 40+ 分类器。

**[CompleteMe: Reference-based Human Image Completion](image_generation/completeme_reference-based_human_image_completion.md)**

:   提出CompleteMe框架，通过双U-Net架构和Region-focused Attention（RFA）Block，利用参考图像中的细粒度人物细节（衣物纹理、纹身等），实现高保真的参考引导人体图像补全。

**[Cycle Consistency as Reward: Learning Image-Text Alignment without Human Preferences](image_generation/cycle_consistency_as_reward_learning_imagetext_alignment_wit.md)**

:   提出CycleReward，利用cycle consistency作为自监督信号替代人工偏好标注——将caption用T2I模型重建为图像再比较相似度来排序，构建866K偏好对数据集CyclePrefDB，训练的奖励模型在detailed captioning上比HPSv2/PickScore/ImageReward高6%+，且DPO训练后提升VLM在多个VL任务上的性能，无需任何人工标注。

**[Deeply Supervised Flow-Based Generative Models](image_generation/deeply_supervised_flow-based_generative_models.md)**

:   DeepFlow 通过在 flow-based 模型的 Transformer 层间引入深度监督和 VeRA（Velocity Refiner with Acceleration）模块，利用二阶 ODE 动力学对齐中间层速度特征，在不依赖外部预训练模型的情况下实现 8 倍训练加速和显著 FID 提升。

**[Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation](image_generation/dense2moe_restructuring_diffusion_transformer_to_moe_for_eff.md)**

:   首次将预训练的dense DiT（如FLUX.1）转换为Mixture-of-Experts结构实现结构化稀疏推理，通过Taylor度量专家初始化+知识蒸馏+Mixture-of-Blocks进一步稀疏化，在激活参数减少60%的同时保持原始生成质量，全面超越剪枝方法。

**[Domain Generalizable Portrait Style Transfer](image_generation/domain_generalizable_portrait_style_transfer.md)**

:   DGPST 提出了一个基于扩散模型的人像风格迁移框架，通过 semantic adapter 建立跨域稠密语义对应来扭曲参考图像，配合 AdaIN-Wavelet Transform 进行潜空间初始化以平衡风格化与内容保持，结合 ControlNet（高频结构引导）和 style adapter（风格引导）的双条件扩散模型生成最终结果，仅在 30K 真实肖像照片上训练即可泛化到照片、卡通、素描、动漫等多种域。

**[Efficient Autoregressive Shape Generation via Octree-Based Adaptive Tokenization](image_generation/efficient_autoregressive_shape_generation_via_octree-based_adaptive_tokenization.md)**

:   OAT 提出基于二次误差度量（quadric error）的自适应八叉树 tokenization，根据局部几何复杂度动态分配 token 预算，在减少 50% token 的同时保持重建质量，并在此基础上构建 OctreeGPT 实现高质量文本到 3D 生成。

**[FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](image_generation/flowedit_inversion-free_text-based_editing_using_pre-trained_flow_models.md)**

:   FlowEdit 提出一种无需反转（inversion-free）、无需优化、模型无关的文本编辑方法，直接在预训练 Flow 模型的源/目标分布之间构建 ODE 路径，实现比 inversion 更低传输代价的结构保持编辑。

**[HPSv3: Towards Wide-Spectrum Human Preference Score](image_generation/hpsv3_towards_wide-spectrum_human_preference_score.md)**

:   HPSv3 构建了首个宽谱人类偏好数据集 HPDv3（1.08M 图文对、1.17M 标注对），采用 VLM 骨干（Qwen2-VL）+ 不确定性感知排序损失训练偏好模型，并提出 CoHP 链式思维迭代生成方法，显著提升图像生成评估的准确性和覆盖范围。

**[InfiniDreamer: Arbitrarily Long Human Motion Generation via Segment Score Distillation](image_generation/infinidreamer_arbitrarily_long_human_motion_generation_via_segment_score_distill.md)**

:   InfiniDreamer 通过将预训练的短序列运动扩散模型作为先验，提出 Segment Score Distillation (SSD) 优化方法，对粗初始化的长运动序列中的重叠短片段进行迭代优化，实现了无需额外长序列训练数据的任意长度人体运动生成。

**[IntroStyle: Training-Free Introspective Style Attribution using Diffusion Features](image_generation/introstyle_training-free_introspective_style_attribution_using_diffusion_feature.md)**

:   提出 IntroStyle，一种无需训练的风格归因方法，仅利用扩散模型自身中间层特征的通道级均值和方差统计量，通过 2-Wasserstein 距离度量图像间的风格相似性，在 WikiArt 和 DomainNet 上大幅超越需要专门训练的 SOTA 方法。

**[LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching](image_generation/lazymar_accelerating_masked_autoregressive_models_via_feature_caching.md)**

:   LazyMAR针对Masked Autoregressive（MAR）模型的推理效率瓶颈，利用两种冗余——token冗余（相邻解码步中大部分token特征高度相似）和条件冗余（classifier-free guidance中条件/无条件输出的残差在相邻步间变化极小），设计了token cache和condition cache两种缓存机制，实现2.83×加速且几乎不损失生成质量。

**[LD-RPS: Zero-Shot Unified Image Restoration via Latent Diffusion Recurrent Posterior Sampling](image_generation/ld-rps_zero-shot_unified_image_restoration_via_latent_diffusion_recurrent_poster.md)**

:   LD-RPS 提出一种零样本、无数据集的统一图像复原方法，利用预训练潜在扩散模型进行循环后验采样，通过多模态大模型提供语义先验、可学习 F-PAM 模块对齐退化域，实现多种退化类型的高质量盲复原。

**[Long-Context State-Space Video World Models](image_generation/long-context_state-space_video_world_models.md)**

:   本文提出将状态空间模型（SSM/Mamba）引入视频世界模型，通过 block-wise SSM 扫描方案在空间一致性和时序记忆之间权衡，配合局部帧注意力，实现了线性训练复杂度、常数推理开销下的长期空间记忆保持，在 Memory Maze 和 Minecraft 数据集上大幅超越有限上下文的 Transformer 基线。

**[Make Me Happier: Evoking Emotions Through Image Diffusion Models](image_generation/make_me_happier_evoking_emotions_through_image_diffusion_models.md)**

:   EmoEditor 提出首个系统性的**情感驱动图像生成**框架，通过双分支扩散模型（全局情感条件 + 局部语义特征）实现仅输入源图和目标情感即可生成具有目标情感的图像，无需手工文本指令或参考图，并构建了 340K 情感标注图对的 EmoPair 数据集。

**[MotionAgent: Fine-grained Controllable Video Generation via Motion Field Agent](image_generation/motionagent_fine-grained_controllable_video_generation_via_motion_field_agent.md)**

:   提出 MotionAgent，通过运动场代理（Motion Field Agent）将文本中的运动描述转化为物体轨迹和相机外参，再经解析式光流合成模块统一为光流图，实现仅凭文本输入即可对 I2V 生成中的物体运动和相机运动进行细粒度精确控制。

**[MotionDiff: Training-Free Zero-Shot Interactive Motion Editing via Flow-Assisted Multi-View Diffusion](image_generation/motiondiff_training-free_zero-shot_interactive_motion_editing_via_flow-assisted_.md)**

:   MotionDiff 提出一种免训练、零样本的多视图运动编辑方法，通过点运动学模型（PKM）从静态场景估计多视图光流，再利用解耦运动表示引导 Stable Diffusion 生成高质量、多视图一致的运动编辑结果。

**[MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion](image_generation/motionfollower_editing_video_motion_via_score-guided_diffusion.md)**

:   提出 MotionFollower，通过两个轻量卷积控制器（姿态+外观）和基于分数函数正则化的一致性引导机制，实现视频运动编辑，在 GPU 显存消耗减少约 80% 的同时超越 MotionEditor 等强基线。

**[Multi-turn Consistent Image Editing](image_generation/multi-turn_consistent_image_editing.md)**

:   提出基于 flow matching 的多轮图像编辑框架，通过双目标 LQR 引导和自适应注意力机制，有效抑制多轮编辑中的误差累积，在保持内容一致性的同时实现灵活可控的迭代编辑。

**[MUNBa: Machine Unlearning via Nash Bargaining](image_generation/munba_machine_unlearning_via_nash_bargaining.md)**

:   将机器遗忘（Machine Unlearning）建模为双玩家合作博弈问题，利用 Nash 讨价还价理论推导闭式解来同时解决遗忘目标与保留目标之间的梯度冲突和梯度支配问题，在分类和生成任务上实现遗忘与保留的最优平衡。

**[Music-Aligned Holistic 3D Dance Generation via Hierarchical Motion Modeling](image_generation/music-aligned_holistic_3d_dance_generation_via_hierarchical_motion_modeling.md)**

:   提出 SoulDance 数据集（首个含身体+手部+面部的高质量3D舞蹈数据集）和 SoulNet 框架（层次化残差向量量化 + 音乐对齐生成模型 + 跨模态检索），实现首个面部表情与身体手部动作协调一致、与音乐节奏情感对齐的全身3D舞蹈生成。

**[NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors](image_generation/normalcrafter_learning_temporally_consistent_normals_from_video_diffusion_priors.md)**

:   NormalCrafter 基于视频扩散模型（SVD）提出视频法线估计方法，通过语义特征正则化（SFR）和两阶段训练策略，生成具有精细细节和时序一致性的法线序列，在视频基准上大幅超越现有单帧方法。

**[NullSwap: Proactive Identity Cloaking Against Deepfake Face Swapping](image_generation/nullswap_proactive_identity_cloaking_against_deepfake_face_swapping.md)**

:   提出 NullSwap，通过在源图像中嵌入身份引导的不可见扰动来伪装面部身份信息，使 Deepfake 换脸模型无法提取正确身份，从而在纯黑盒场景下主动防御换脸攻击。

**[OmniPaint: Mastering Object-Oriented Editing via Disentangled Insertion-Removal Inpainting](image_generation/omnipaint_mastering_object-oriented_editing_via_disentangled_insertion-removal_i.md)**

:   提出 OmniPaint 统一框架，将物体移除与插入重新定义为互逆互补的关联任务，基于 FLUX 扩散先验并引入 CycleFlow 无配对训练机制和 CFD 无参考评估指标，仅用 3K 真实配对样本即可实现高保真的物体编辑，尤其擅长处理阴影、反射等复杂物理效果。

**[Randomized Autoregressive Visual Generation](image_generation/randomized_autoregressive_visual_generation.md)**

:   提出 Randomized AutoRegressive modeling (RAR)：在标准自回归训练中以随机排列输入序列并逐步退火回光栅扫描顺序，使模型学习双向上下文，在 ImageNet-256 上以 FID 1.48 刷新自回归图像生成 SOTA，同时保持与语言模型框架的完全兼容。

**[REDUCIO! Generating 1K Video within 16 Seconds using Extremely Compressed Motion Latents](image_generation/reducio_generating_1k_video_within_16_seconds_using_extremely_compressed_motion_.md)**

:   提出 Reducio-VAE，一种以内容帧为条件的 3D 视频自编码器，将视频压缩至比标准 2D VAE 小 64 倍的运动潜空间，配合 Reducio-DiT 在单张 A100 上 15.5 秒内生成 16 帧 1024x1024 视频，训练仅需 3200 A100 GPU 小时。

**[REPA-E: Unlocking VAE for End-to-End Tuning of Latent Diffusion Transformers](image_generation/repae_unlocking_vae_for_endtoend_tuning_of_latent_diffusion.md)**

:   回答了"潜空间扩散模型能否与VAE端到端联合训练"的基础问题——发现标准扩散loss无法端到端训练但表示对齐（REPA）loss可以，提出REPA-E实现VAE+DiT联合训练，训练速度比REPA快17倍、比vanilla快45倍，在ImageNet 256×256上达到1.12 FID（w/ CFG）的新SOTA。

**[SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation](image_generation/sanasprint_onestep_diffusion_with_continuoustime_consistency.md)**

:   将预训练的SANA flow matching模型通过无损数学变换转化为TrigFlow，结合连续时间一致性蒸馏（sCM）和潜空间对抗蒸馏（LADD）的混合策略，实现统一的1-4步自适应高质量图像生成，1步生成1024×1024图像仅需0.1s（H100），以7.59 FID和0.74 GenEval超越FLUX-schnell且速度快10倍。

**[ShortFT: Diffusion Model Alignment via Shortcut-based Fine-Tuning](image_generation/shortft_diffusion_model_alignment_via_shortcut-based_fine-tuning.md)**

:   提出 ShortFT，利用轨迹保持少步扩散模型构建去噪捷径（shortcut），将原本冗长的去噪链大幅缩短，从而实现完整的端到端奖励梯度反向传播，高效且有效地将扩散模型与奖励函数对齐。

**[SMGDiff: Soccer Motion Generation using Diffusion Probabilistic Models](image_generation/smgdiff_soccer_motion_generation_using_diffusion_probabilistic_models.md)**

:   提出 SMGDiff，一个两阶段扩散模型框架，能够根据用户控制信号实时生成高质量、多样化的足球运动动画，同时通过接触引导模块优化球-脚交互细节。

**[Spectral Image Tokenizer](image_generation/spectral_image_tokenizer.md)**

:   提出 Spectral Image Tokenizer (SIT)，用离散小波变换 (DWT) 将图像从空域转换到频域后再进行 token 化，使 token 序列天然地按"粗到细"排列，从而支持多分辨率重建、渐进式生成、文本引导上采样与编辑等传统 raster-scan tokenizer 无法实现的能力。

**[StyleKeeper: Prevent Content Leakage using Negative Visual Query Guidance](image_generation/stylekeeper_prevent_content_leakage_using_negative_visual_query_guidance.md)**

:   提出 **负视觉查询引导（NVQG）** 方法，通过在 self-attention 层中将参考图的 query 注入作为负向引导来抑制内容泄漏，实现了无需训练的高质量视觉风格提示，在风格相似度和文本对齐上均优于现有方法。

**[TeRA: Rethinking Text-guided Realistic 3D Avatar Generation](image_generation/tera_rethinking_text-guided_realistic_3d_avatar_generation.md)**

:   提出TeRA，首个基于隐空间扩散模型的文本引导3D真人头像生成框架，通过蒸馏大规模人体重建模型构建结构化隐空间，12秒生成写实3D人物，比SDS方法快两个数量级。

**[Video Color Grading via Look-Up Table Generation](image_generation/video_color_grading_via_look-up_table_generation.md)**

:   提出基于扩散模型显式生成 LUT 的视频调色框架：通过 GS-Extractor 提取参考场景的高层风格特征，用 L-Diffuser 生成色彩查找表（LUT），一次生成即可无损应用于全部视频帧，并支持文本 prompt 进行亮度/对比度等细粒度调整。

**[VisualCloze: A Universal Image Generation Framework via Visual In-Context Learning](image_generation/visualcloze_a_universal_image_generation_framework_via_visua.md)**

:   提出VisualCloze，将多种图像生成任务（编辑、翻译、超分、风格化等）统一为"视觉完形填空"范式——用视觉示例（而非文本指令）定义任务，通过图像infilling模型实现统一生成，并构建Graph200K数据集增强任务间知识迁移，支持域内任务、未见任务泛化、多任务组合和反向生成。

---

## 🧩 多模态 VLM { #multimodal_vlm }

**[AdvDreamer Unveils: Are Vision-Language Models Truly Ready for Real-World 3D Variations?](multimodal_vlm/advdreamer_unveils_are_visionlanguage_models_truly_ready_for.md)**

:   提出AdvDreamer框架从单张图像生成物理可复现的对抗性3D变换(Adv-3DT)样本，通过零样本单目姿态操作+自然度奖励模型+逆语义概率损失，揭示当前VLM（包括GPT-4o）在3D变化下性能下降高达50-80%，并建立首个3D变化鲁棒性VQA基准MM3DTBench。

**[CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](multimodal_vlm/coavla_improving_visionlanguageaction_models_via_visualtext.md)**

:   提出Chain-of-Affordance（CoA-VLA）框架，将四类机器人affordance（物体、抓取、空间、运动）以文本和视觉双模态形式注入VLA模型的策略网络，在真实机器人7任务多任务学习中达到85.54%成功率，比OpenVLA高30.65%，并展现出对未见物体姿态和障碍物的泛化能力。

**[Controlling Multimodal LLMs via Reward-guided Decoding](multimodal_vlm/controlling_multimodal_llms_via_reward-guided_decoding.md)**

:   提出多模态奖励引导解码 (MRGD)，通过构建两个奖励模型分别控制物体精度和召回率，在推理时实现对 MLLM 输出的细粒度可控性，同时显著降低物体幻觉。

**[Controlling Multimodal LLMs via Reward-guided Decoding](multimodal_vlm/controlling_multimodal_llms_via_rewardguided_decoding.md)**

:   提出MRGD（Multimodal Reward-Guided Decoding），通过训练一个基于PaliGemma的物体幻觉奖励模型和一个基于OWLv2的物体召回奖励模型，在MLLM推理时通过线性加权组合两个奖励来逐句搜索最优候选输出，在CHAIR上将LLaVA-1.5的CHAIRi从15.05降至4.53（降70%）且支持精度-召回率的动态可控权衡。

**[CVPT: Cross Visual Prompt Tuning](multimodal_vlm/cvpt_cross_visual_prompt_tuning.md)**

:   针对 Visual Prompt Tuning (VPT) 中 prompt token 参与 self-attention 导致的计算冗余和注意力破坏问题，提出 CVPT，通过 cross-attention 解耦 prompt 与 image token 的交互，并利用权重共享机制初始化 cross-attention，在 25 个数据集上显著超越 VPT，性能媲美主流 adapter 方法。

**[Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](multimodal_vlm/dita_scaling_diffusion_transformer_for_generalist_visionlang.md)**

:   提出Dita，用Transformer架构进行统一的多模态扩散过程直接去噪连续动作序列，通过in-context conditioning实现去噪动作与历史视觉观察的细粒度对齐，在跨embodiment数据集上scaling后实现SOTA仿真性能和10-shot真实世界长horizon任务适应。

**[DocThinker: Explainable Multimodal Large Language Models with Rule-based Reinforcement Learning for Document Understanding](multimodal_vlm/docthinker_explainable_multimodal_large_language_models_with.md)**

:   提出DocThinker，首个将GRPO（Group Relative Policy Optimization）强化学习应用于文档理解的框架，通过四目标规则奖励（格式、答案准确度、RoI IoU、问题改写质量）训练MLLM自主生成可解释的推理过程，仅用4K训练数据在DocVQA上将Qwen2.5-VL-7B从0.355提升到0.579（RL vs SFT: 0.579 vs 0.355），并在视觉定位任务上达到82.4%精度。

**[Dynamic Group Detection using VLM-augmented Temporal Groupness Graph](multimodal_vlm/dynamic_group_detection_using_vlm-augmented_temporal_groupness_graph.md)**

:   本文提出基于VLM增强的时序群组图（temporal groupness graph）进行视频中的动态人群群组检测，核心创新是用CLIP提取包含人对和背景的groupness-augmented特征来估计成组概率，并通过全帧时序图的Louvain聚类实现动态变化群组的检测。

**[EVEv2: Improved Baselines for Encoder-Free Vision-Language Models](multimodal_vlm/evev2_improved_baselines_for_encoderfree_visionlanguage_mode.md)**

:   系统性地探索无视觉编码器VLM的最优架构和训练策略，提出Divide-and-Conquer架构将transformer完全分解为模态专用组件（attention/FFN/LayerNorm各模态独立），在仅100M公开数据下超越所有encoder-free同类并接近encoder-based VLM性能。

**[FALCON: Resolving Visual Redundancy and Fragmentation in High-resolution Multimodal Large Language Models via Visual Registers](multimodal_vlm/falcon_resolving_visual_redundancy_and_fragmentation_in_high.md)**

:   针对高分辨率MLLM中裁切子图导致的视觉编码分裂和token冗余问题，提出可学习的Visual Registers在encoder内部自适应聚合关键信息（ReCompact）并跨子图交互（ReAtten），实现9倍视觉token压缩且性能更优。

**[Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration](multimodal_vlm/feather_the_throttle_revisiting_visual_token_pruning_for_vis.md)**

:   揭示了VLM中视觉token剪枝方法（如FastV）因RoPE的长程衰减特性导致系统性地保留图像底部token的严重缺陷，并提出FEATHER方法通过去除RoPE+均匀采样+两阶段剪枝修复该问题，在定位任务上实现5倍以上的性能提升。

**[Harmonizing Visual Representations for Unified Multimodal Understanding and Generation](multimodal_vlm/harmonizing_visual_representations_for_unified_multimodal_un.md)**

:   发现Masked Autoregressive (MAR)模型的编码器同时具备优秀的语义理解能力和生成能力，基于此提出Harmon框架——用共享的MAR编码器统一视觉理解和生成任务，通过三阶段渐进训练在生成benchmark上达SOTA同时在理解benchmark上匹配专用语义编码器方法。

**[IDEATOR: Jailbreaking and Benchmarking Large Vision-Language Models Using Themselves](multimodal_vlm/ideator_jailbreaking_and_benchmarking_large_visionlanguage_m.md)**

:   提出IDEATOR，首个用VLM自身做红队攻击VLM的黑盒越狱框架——利用一个弱安全对齐的VLM（MiniGPT-4）作为攻击者，结合Stable Diffusion生成语义丰富的图文越狱对，通过breadth-depth探索策略迭代优化，在MiniGPT-4上达94%攻击成功率（平均5.34次查询），迁移到LLaVA/InstructBLIP/Chameleon达75-88%，并构建VLJailbreakBench（3654样本）揭示11个VLM的安全漏洞。

**[Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency](multimodal_vlm/jailbreaking_multimodal_large_language_models_via_shuffle_inconsistency.md)**

:   发现多模态大语言模型(MLLMs)在理解能力和安全能力之间存在**打乱不一致性(Shuffle Inconsistency)**——模型能理解打乱后的有害指令，但安全机制却无法防御；据此提出基于查询的黑盒越狱攻击方法 SI-Attack，在开源和闭源商用模型上均显著提升攻击成功率。

**[LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](multimodal_vlm/llavacot_let_vision_language_models_reason_stepbystep.md)**

:   通过构建包含结构化推理标注的LLaVA-CoT-100k数据集，训练VLM自主执行"总结→视觉解读→逻辑推理→结论"四阶段推理，配合测试时SWIRES搜索策略，11B模型超越GPT-4o-mini和Gemini-1.5-pro等大模型。

**[LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models](multimodal_vlm/llavaprumerge_adaptive_token_reduction_for_efficient_large_m.md)**

:   利用CLIP-ViT中[CLS] token与视觉token之间注意力分数的稀疏特性，通过IQR异常值检测自适应选择重要视觉token，再用k-近邻聚类将被剪除token的信息合并回保留token，实现视觉token 14倍压缩且性能几乎不降。

**[MAVias: Mitigate Any Visual Bias](multimodal_vlm/mavias_mitigate_any_visual_bias.md)**

:   提出 MAVias，一个开放集视觉偏差缓解框架：利用图像标注基础模型提取视觉属性标签，用 LLM 筛选与目标类别无关的标签作为潜在偏差，再通过 vision-language embedding 编码偏差并融入训练过程以学习偏差不变表示，在 CelebA、Waterbirds、UrbanCars 和 ImageNet9 上大幅超越现有方法。

**[MetaMorph: Multimodal Understanding and Generation via Instruction Tuning](multimodal_vlm/metamorph_multimodal_understanding_and_generation_via_instru.md)**

:   提出Visual-Predictive Instruction Tuning (VPiT)——一种简单有效的视觉指令微调扩展，让预训练LLM同时预测离散文本token和连续视觉token，发现视觉生成能力是视觉理解能力提升的自然副产物，少量生成数据即可解锁，LLM的预训练知识可以迁移到视觉生成中克服常见失败模式。

**[Mitigating Object Hallucinations via Sentence-Level Early Intervention](multimodal_vlm/mitigating_object_hallucinations_via_sentence-level_early_intervention.md)**

:   提出 SENTINEL 框架，通过句子级早期干预和域内偏好学习有效缓解 MLLM 的物体幻觉，在 Object HalBench 上将幻觉率降低超过 90%，同时保持甚至提升通用能力。

**[MM-IFEngine: Towards Multimodal Instruction Following](multimodal_vlm/mm-ifengine_towards_multimodal_instruction_following.md)**

:   提出 MM-IFEngine 管线，系统性地生成高质量的图像-指令对数据（含 SFT 和 DPO 版本），并构建 MM-IFEval 基准，显著提升 MLLM 在多模态指令遵循任务上的表现。

**[MMAT-1M: A Large Reasoning Dataset for Multimodal Agent Tuning](multimodal_vlm/mmat1m_a_large_reasoning_dataset_for_multimodal_agent_tuning.md)**

:   提出首个百万规模的多模态agent调优数据集MMAT-1M，通过四阶段数据引擎（基础数据→推理轨迹生成→反思纠错→格式整合）为MLLM注入CoT推理、工具调用和反思能力，在InternVL2.5-8B上平均提升2.7%，RAG任务上提升8.8%。

**[MUSE-VL: Modeling Unified VLM through Semantic Discrete Encoding](multimodal_vlm/muse-vl_modeling_unified_vlm_through_semantic_discrete_encoding.md)**

:   提出语义离散编码 (SDE)，通过在视觉 tokenizer 的量化过程中融入预训练 CLIP 语义特征，使离散视觉 token 与语言 token 天然对齐，在仅用 24M 图文对的情况下实现了统一理解与生成的 SOTA 性能。

**[MUSE-VL: Modeling Unified VLM through Semantic Discrete Encoding](multimodal_vlm/musevl_modeling_unified_vlm_through_semantic_discrete_encodi.md)**

:   提出语义离散编码（SDE）视觉tokenizer，在VQGAN基础上加入SigLIP语义特征约束，使离散视觉token与语言token语义对齐，构建统一的自回归VLM（MUSE-VL），在仅用24M数据的条件下理解性能比Emu3提升4.8%，超过LLaVA-NeXT 34B专用理解模型3.7%，同时支持图像生成。

**[ONLY: One-Layer Intervention Sufficiently Mitigates Hallucinations in Large Vision-Language Models](multimodal_vlm/only_onelayer_intervention_sufficiently_mitigates_hallucinat.md)**

:   提出ONLY，一种training-free的单层干预解码方法——通过Text-to-Visual Entropy Ratio（TVER）选择偏向文本的attention head生成textually-enhanced logits，然后与原始logits做自适应对比/协作解码，仅增加1.07×推理时间就在POPE上比VCD/M3ID高3.14%，在CHAIR上降低CHAIR_S 6.2个点。

**[PRO-VPT: Distribution-Adaptive Visual Prompt Tuning via Prompt Relocation](multimodal_vlm/pro-vpt_distribution-adaptive_visual_prompt_tuning_via_prompt_relocation.md)**

:   提出 PRO-VPT 框架，通过嵌套优化将提示分布优化 (ADO) 与视觉提示调优 (VPT) 协同设计，利用闲置分数剪枝和强化学习分配策略迭代重定位提示，在 VTAB-1k 和 FGVC 上较 VPT 分别提升 1.6pp 和 2.0pp。

**[Scaling Inference-Time Search with Vision Value Model for Improved Visual Comprehension](multimodal_vlm/scaling_inferencetime_search_with_vision_value_model_for_imp.md)**

:   提出Vision Value Model（VisVM），用TD learning训练一个能预测VLM生成句子长期价值的价值网络，指导推理时逐句搜索生成更少幻觉、更丰富细节的图像描述，并进一步将VisVM生成的高质量caption用于自训练，在9个benchmark上平均提升LLaVA-Next 10.8%。

**[Scaling Laws for Native Multimodal Models](multimodal_vlm/scaling_laws_for_native_multimodal_models.md)**

:   通过训练457个不同架构和训练配比的模型进行系统性scaling law研究，发现Native Multimodal Models（NMM）的early-fusion架构（不依赖视觉编码器/tokenizer）在小参数量时优于late-fusion，训练更高效且部署更简单，结合MoE可进一步显著提升性能。

**[ShortV: Efficient Multimodal Large Language Models by Freezing Visual Tokens in Ineffective Layers](multimodal_vlm/shortv_efficient_multimodal_large_language_models_by_freezin.md)**

:   发现MLLM中约60%的层对视觉token的变换几乎不影响模型输出（Layer Contribution极低），提出ShortV方法在这些"ineffective layers"中冻结视觉token（不参与attention query和FFN），在LLaVA-NeXT-13B上实现50% FLOPs降低且性能几乎不变，且与token剪枝方法（如FastV）正交可叠加。

**[SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs](multimodal_vlm/sparsemm_head_sparsity_emerges_from_visual_concept_responses.md)**

:   发现MLLM中仅约5%的attention head主动参与视觉理解（称为"visual heads"），提出基于OCR任务的training-free识别方法量化每个head的视觉相关性，并设计SparseMM——按visual score非对称分配KV-Cache预算的策略，在DocVQA上仅用5.3%的cache（256/4830）即可维持Qwen2-VL的性能，实现1.87×加速和50%内存减少。

**[SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference](multimodal_vlm/sparsevila_decoupling_visual_sparsity_for_efficient_vlm_infe.md)**

:   提出SparseVILA，将VLM推理时的视觉token稀疏化解耦为两个阶段——prefill阶段做query-agnostic剪枝（去冗余）、decode阶段做query-aware检索（精选相关token），在长视频任务上实现4.0×prefill加速、2.5×decode加速、2.6×端到端加速，同时在视频理解benchmark上精度不降反升。

**[ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools](multimodal_vlm/toolvqa_a_dataset_for_multistep_reasoning_vqa_with_external.md)**

:   提出ToolVQA，一个23K样本的多模态工具使用VQA数据集，通过ToolEngine数据生成pipeline（图像引导DFS + LCS示例匹配）从真实图像中构造隐式多步推理问题（平均2.78步），在该数据上微调LLaVA-7B后在5个OOD benchmark上超过GPT-3.5-Turbo，并揭示了当前LFM在参数预测和答案总结方面的瓶颈。

**[Unified Multimodal Understanding via Byte-Pair Visual Encoding](multimodal_vlm/unified_multimodal_understanding_via_byte-pair_visual_encoding.md)**

:   将 NLP 中的 Byte-Pair Encoding (BPE) 策略应用于视觉 token 化，提出优先级引导的编码方案（融合频率和空间一致性）、课程式数据混合和渐进式参数解冻三阶段训练策略，构建的 Being-VL-0.5（8B）在离散 token 路线上接近连续 embedding 方法的主流水平。

**[Visual Interestingness Decoded: How GPT-4o Mirrors Human Interests](multimodal_vlm/visual_interestingness_decoded_how_gpt-4o_mirrors_human_interests.md)**

:   系统性研究了 GPT-4o 等大型多模态模型对"图像有趣性"这一主观视觉概念的理解程度，发现 GPT-4o 与人类评判有中等正相关（配对图像一致率 73.8%），并提出利用 GPT-4o 自动标注图像对训练 learning-to-rank 模型来预测图像有趣性，超越了所有现有方法。

**[WikiAutoGen: Towards Multi-Modal Wikipedia-Style Article Generation](multimodal_vlm/wikiautogen_towards_multi-modal_wikipedia-style_article_generation.md)**

:   提出 WikiAutoGen 多智能体框架，通过整合文本和图像的多模态检索与多视角自反思机制，自动生成高质量的多模态 Wikipedia 风格文章，在自建基准 WikiSeek 上相比已有方法提升 8%–29%。

---

## 🚗 自动驾驶 { #autonomous_driving }

**[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](autonomous_driving/3d_gaussian_splatting_driven_multi-view_robust_physical_adversarial_camouflage_g.md)**

:   提出PGA，首个基于3DGS的物理对抗攻击框架，通过快速准确重建目标+解决Gaussians互/自遮挡问题+min-max背景对抗优化策略，生成跨视角鲁棒的物理对抗迷彩，在数字和物理域均超越SOTA方法。

**[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial Camouflage Generation](autonomous_driving/3d_gaussian_splatting_driven_multiview_robust_physical_adver.md)**

:   提出首个基于3D高斯体（3DGS）的物理对抗攻击框架PGA，通过解决高斯体的互遮挡和自遮挡问题保证跨视角一致性，并设计min-max优化策略过滤非鲁棒对抗特征，在数字域和物理域均大幅超越SOTA方法。

**[3DRealCar: An In-the-wild RGB-D Car Dataset with 360-degree Views](autonomous_driving/3drealcar_an_inthewild_rgbd_car_dataset_with_360degree_views.md)**

:   提出首个大规模3D真实汽车数据集3DRealCar，包含2,500辆真实汽车的高分辨率（1920×1440）360度RGB-D扫描（平均每辆200张视角），覆盖100+品牌和三种光照条件（标准/高反光/暗光），提供点云、解析图等丰富标注，并基准测试了多种3D重建方法，揭示了反光和暗光条件下的重建挑战。

**[4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads](autonomous_driving/4dsegstreamer_streaming_4d_panoptic_segmentation_via_dual_th.md)**

:   提出4DSegStreamer，一种通用的**双线程**流式4D全景分割框架——预测线程维护几何和运动记忆并预测未来动态，推理线程通过自我位姿对齐和逆向前向流迭代实现对新到帧的实时查询，可即插即用地集成到现有3D/4D分割方法中，在SemanticKITTI上sLSTQ比PTv3高7.7-15.2%，在高FPS场景下性能鲁棒性远超现有方法。

**[4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads](autonomous_driving/4dsegstreamer_streaming_4d_panoptic_segmentation_via_dual_threads.md)**

:   提出4DSegStreamer，一种基于双线程系统（预测线程+推理线程）的流式4D全景分割框架，通过几何与运动记忆维护、自车位姿预测和逆向前向光流迭代实现实时高质量4D全景分割。

**[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](autonomous_driving/6dope-gs_online_6d_object_pose_estimation_using_gaussian_splatting.md)**

:   提出6DOPE-GS，一种利用2D高斯溅射（2DGS）联合优化6D物体位姿和3D重建的model-free在线追踪方法，通过动态关键帧选择和基于透明度百分位的密度控制实现5倍加速，同时保持SOTA精度。

**[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](autonomous_driving/6dopegs_online_6d_object_pose_estimation_using_gaussian_spla.md)**

:   利用2D Gaussian Splatting的高效可微渲染能力，提出一种无需CAD模型的在线6D物体位姿估计与跟踪方法，通过联合优化高斯物体场和关键帧位姿，实现比BundleSDF快约5倍的速度同时保持可比精度。

**[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy LiDAR Point Clouds](autonomous_driving/a_constrained_optimization_approach_for_gaussian_splatting_f.md)**

:   提出一种**无需SfM**的约束优化方法，同时估计相机位姿和做3DGS重建——将相机位姿分解为相机-设备中心和设备中心-世界两步优化，设计参数敏感性条件约束和几何约束，从粗糙位姿和噪声LiDAR点云直接重建3D场景，显著优于COLMAP辅助的3DGS基线。

**[Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts](autonomous_driving/adaptive_dual_uncertainty_optimization_boosting_monocular_3d.md)**

:   提出DUO（Dual Uncertainty Optimization），首个面向单目3D检测（M3OD）的测试时自适应框架，通过共轭焦点损失减少语义不确定性和法线场一致性约束减少几何不确定性，形成互补优化闭环。

**[Adaptive Dual Uncertainty Optimization: Boosting Monocular 3D Object Detection under Test-Time Shifts](autonomous_driving/adaptive_dual_uncertainty_optimization_boosting_monocular_3d_object_detection_un.md)**

:   提出 DUO（Dual Uncertainty Optimization），首个联合最小化语义不确定性和几何不确定性的测试时自适应框架，通过共轭焦点损失和法向场约束实现鲁棒的单目3D目标检测。

**[AGO: Adaptive Grounding for Open World 3D Occupancy Prediction](autonomous_driving/ago_adaptive_grounding_for_open_world_3d_occupancy_predictio.md)**

:   提出AGO框架，通过噪声增强的接地训练(grounding training)处理已知类别 + 模态适配器的自适应对齐处理未知类别，并用基于信息熵的开放世界识别器在推理时动态选择最佳特征，在Occ3D-nuScenes自监督基准上超越VEON 4.09 mIoU，同时具备开放世界零样本/少样本迁移能力。

**[Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis](autonomous_driving/causal-entity_reflected_egocentric_traffic_accident_video_synthesis.md)**

:   提出 Causal-VidSyn 扩散模型，通过事故原因问答（ArA）和驾驶员注视引导的因果 token 选择（CTS&CTG）机制，实现对自车视角交通事故视频中因果实体的精确定位与生成，同时构建了最大规模驾驶员注视数据集 Drive-Gaze（154 万帧）。

**[CoLMDriver: LLM-based Negotiation Benefits Cooperative Autonomous Driving](autonomous_driving/colmdriver_llm-based_negotiation_benefits_cooperative_autonomous_driving.md)**

:   首个全流程 LLM 驱动的协作驾驶系统，通过 Actor-Critic 范式的语言协商模块和意图引导的轨迹生成器，在多种 V2V 交互场景中实现比现有方法高 11% 的成功率。

**[Controllable 3D Outdoor Scene Generation via Scene Graphs](autonomous_driving/controllable_3d_outdoor_scene_generation_via_scene_graphs.md)**

:   首次提出以场景图（Scene Graph）作为控制信号生成大规模3D室外场景的方法——通过GNN将稀疏场景图编码为BEV嵌入图，再经2D→3D级联离散扩散模型生成语义3D场景，并配套交互系统让用户直接编辑场景图来控制生成。

**[Counting Stacked Objects](autonomous_driving/counting_stacked_objects.md)**

:   将堆叠物体计数问题分解为"体积估计"和"占空比估计"两个子问题，前者用多视角3D重建解决，后者用深度图驱动的神经网络从可见表面推断，首次实现了对不可见堆叠物体的准确计数，性能远超人类。

**[Decoupled Diffusion Sparks Adaptive Scene Generation](autonomous_driving/decoupled_diffusion_sparks_adaptive_scene_generation.md)**

:   提出 Nexus，一个基于解耦扩散的自适应驾驶场景生成框架，通过独立噪声状态实现目标导向与实时响应的统一，将位移误差降低 40%，并构建了包含 540 小时安全关键驾驶数据的 Nexus-Data。

**[DuET: Dual Incremental Object Detection via Exemplar-Free Task Arithmetic](autonomous_driving/duet_dual_incremental_object_detection_via_exemplar-free_task_arithmetic.md)**

:   提出 DuET 框架，首次以无样本（exemplar-free）的任务算术（Task Arithmetic）模型合并方式，同时解决目标检测中的类别增量和域增量问题（Dual Incremental Object Detection, DuIOD），并引入方向一致性损失（Directional Consistency Loss）缓解符号冲突，在 Pascal Series 和 Diverse Weather Series 上大幅超越现有方法。

**[Extrapolated Urban View Synthesis Benchmark](autonomous_driving/extrapolated_urban_view_synthesis_benchmark.md)**

:   提出首个外推式城市视图合成（EUVS）基准，利用多遍历/多车辆/多相机公开数据集系统评估外推场景下 3DGS 及 NeRF 方法的泛化能力，揭示当前方法严重过拟合训练视角。

**[Language Driven Occupancy Prediction (LOcc)](autonomous_driving/language_driven_occupancy_prediction.md)**

:   提出LOcc，一个有效且可泛化的开放词汇占据(OVO)预测框架，核心是设计了语义传递标注管线（LVLM+OV-Seg→LiDAR→voxel），生成密集细粒度的3D语言占据伪GT，替代了噪声大且稀疏的传统中间特征蒸馏，在Occ3D-nuScenes上全面超越SOTA。

**[LookOut: Real-World Humanoid Egocentric Navigation](autonomous_driving/lookout_real-world_humanoid_egocentric_navigation.md)**

:   提出LookOut，从自我中心视频预测未来6D头部姿态轨迹（包含平移+旋转），通过时序聚合3D DINO特征理解场景几何/语义约束，并贡献了基于Project Aria眼镜采集的4小时真实世界导航数据集AND。

**[MGSfM: Multi-Camera Geometry Driven Global Structure-from-Motion](autonomous_driving/mgsfm_multi-camera_geometry_driven_global_structure-from-motion.md)**

:   提出 MGSfM，一个面向多相机系统的全局 Structure-from-Motion (SfM) 框架，通过**解耦旋转平均 (DMRA)** 和**混合平移平均 (MGP)** 两个核心模块，充分利用多相机刚性约束，在大规模场景中实现与增量式 SfM 媲美甚至更优的精度，同时速度提升约 10 倍。

**[MonoSOWA: Scalable Monocular 3D Object Detector Without Human Annotations](autonomous_driving/monosowa_scalable_monocular_3d_object_detector_without_human_annotations.md)**

:   提出首个完全不依赖人工标注（包括 2D 和 3D）的单目 3D 物体检测方法，通过新提出的局部目标运动模型（LOMM）解耦帧间运动来源，自动标注速度比前人快 700 倍，并通过规范目标空间（COS）融合不同相机设置的多数据集训练。

**[RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case](autonomous_driving/robotron-sim_improving_real-world_driving_via_simulated_hard-case.md)**

:   提出RoboTron-Sim框架，通过构建困难场景仿真数据集HASS、场景感知提示工程SPE和图像到自车编码器I2E，使MLLM有效利用仿真困难案例提升真实世界自动驾驶性能，在nuScenes困难场景下L2距离降低~48%、碰撞率降低~46%，达到开环规划SOTA。

**[Robust 3D Object Detection using Probabilistic Point Clouds from Single-Photon LiDARs](autonomous_driving/robust_3d_object_detection_using_probabilistic_point_clouds_from_single-photon_l.md)**

:   提出概率点云(PPC)表示——将单光子LiDAR原始时间直方图中的测量置信度作为概率属性附加到每个3D点上，配合轻量级NPD滤波和FPPS采样方法，实现低信噪比(SBR)下鲁棒的3D目标检测，在SUN RGB-D和KITTI上大幅超越点云去噪基线，且几乎不增加计算开销。

**[TARS: Traffic-Aware Radar Scene Flow Estimation](autonomous_driving/tars_traffic-aware_radar_scene_flow_estimation.md)**

:   提出 TARS，一种交通感知的雷达场景流估计方法，通过联合目标检测构建交通向量场（TVF），在交通层面而非实例层面捕获刚体运动，在 VOD 和专有数据集上分别超越 SOTA 15% 和 23%。

---

## ✂️ 语义分割 { #segmentation }

**[2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos](segmentation/2handedafforder_learning_precise_actionable_bimanual_affordances_from_human_vide.md)**

:   本文提出从人类活动视频中自动提取精确的双手可操作区域(affordance)数据集 2HANDS，并训练基于 VLM 的 2HandedAfforder 模型，实现根据文本提示预测双手抓握的精确物体区域分割，在新提出的 ActAffordance 基准上显著优于现有方法。

**[A Plug-and-Play Physical Motion Restoration Approach for In-the-Wild High-Difficulty Motions](segmentation/a_plugandplay_physical_motion_restoration_approach_for_inthe.md)**

:   提出即插即用的物理运动修复框架，通过Mask条件运动校正模块（MCM）修复视频运动捕捉中的缺陷帧，结合基于RL测试时适应的物理运动传输模块（PTM），首次实现对野外高难度运动（如体操、武术后空翻）的物理仿真修复。

**[Auto-Vocabulary Semantic Segmentation](segmentation/auto-vocabulary_semantic_segmentation.md)**

:   本文提出 Auto-Vocabulary Semantic Segmentation (AVS) 新任务，通过 AutoSeg 框架自动从图像中发现目标类别并分割，无需人为指定词汇表，在 PASCAL VOC 上达到 87.1 mIoU，远超唯一同类方法 ZeroSeg (20.1)，甚至超越部分需要指定类别的开放词汇方法。

**[Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection](segmentation/beyond_single_images_retrieval_self-augmented_unsupervised_camouflaged_object_de.md)**

:   本文提出 RISE——一种检索自增强的无监督伪装目标检测范式，通过从训练集本身构建前景/背景原型库并利用 KNN 检索生成伪标签，在无任何标注的条件下大幅超越现有无监督和基于提示的方法。

**[CAVIS: Context-Aware Video Instance Segmentation](segmentation/cavis_context-aware_video_instance_segmentation.md)**

:   提出CAVIS，通过引入上下文感知实例追踪器（CAIT）融合物体边界周围的上下文信息来增强实例关联，并设计原型化跨帧对比损失（PCC）保证跨帧特征一致性，在VIS和VPS任务上全面刷新SOTA。

**[CorrCLIP: Reconstructing Patch Correlations in CLIP for Open-Vocabulary Semantic Segmentation](segmentation/corrclip_reconstructing_patch_correlations_in_clip_for_openv.md)**

:   揭示CLIP用于分割时patch间"类间相关性"是性能瓶颈的根本原因，提出CorrCLIP通过SAM限制patch交互范围（scope reconstruction）+DINO计算更一致的相似度值（value reconstruction）+空间/语义特征增强+SAM mask后处理，在8个benchmark上training-free方法平均mIoU从48.6%提升到53.6%。

**[Correspondence as Video: Test-Time Adaption on SAM2 for Reference Segmentation in the Wild](segmentation/correspondence_as_video_testtime_adaption_on_sam2_for_refere.md)**

:   将reference-target图像对之间的对应关系表示为用扩散模型生成的伪视频序列，利用SAM2的iVOS能力进行分割，结合test-time轻量微调对齐几何变化，在跨域few-shot分割上比SOTA方法提升约5% mIoU，且无需meta-training。

**[E-SAM: Training-Free Segment Every Entity Model](segmentation/e-sam_training-free_segment_every_entity_model.md)**

:   E-SAM 是一个无需额外训练的框架，通过三个级联模块——多层级掩码生成（MMG）、实体级掩码精炼（EMR）和欠分割修复（USR）——系统性地解决 SAM 自动掩码生成（AMG）中的过分割和欠分割问题，在基准指标上超越现有实体分割方法 **+30.1 分**。

**[FLOSS: Free Lunch in Open-vocabulary Semantic Segmentation](segmentation/floss_free_lunch_in_openvocabulary_semantic_segmentation.md)**

:   挑战OVSS中"平均80个模板"的默认做法，发现每个类别存在特定的"专家模板"（class-expert）远优于平均分类器，提出用预测熵无监督选择专家模板+融合专家预测的FLOSS方法，在不需要标签和训练的情况下一致提升现有OVSS方法。

**[Hybrid-TTA: Continual Test-time Adaptation via Dynamic Domain Shift Detection](segmentation/hybrid-tta_continual_test-time_adaptation_via_dynamic_domain_shift_detection.md)**

:   Hybrid-TTA 提出一种持续测试时自适应（CTTA）框架，通过动态域偏移检测（DDSD）模块判断当前输入是否来自新域，自适应地在全参数微调（Full Tuning）和高效微调（Adapter Tuning）之间切换；同时引入掩码图像建模自适应（MIMA）作为辅助任务增强模型稳定性，在 Cityscapes-to-ACDC 基准上达到 62.2% mIoU，且推理速度比可比方法快约 **20 倍**。

**[LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation](segmentation/lawdis_language-window-based_controllable_dichotomous_image_segmentati.md)**

:   提出LawDIS，一种基于Stable Diffusion的语言-窗口双控可控二分图像分割框架，在宏观模式下通过语言提示指导目标分割，在微观模式下通过可变尺寸窗口精细化局部细节，在DIS5K上全面超越11种SOTA方法。

**[LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation](segmentation/lawdis_language-window-based_controllable_dichotomous_image_segmentation.md)**

:   提出 LawDIS，一个基于潜在扩散模型的可控二分图像分割框架，通过宏观语言控制（LS）和微观窗口细化（WR）两种模式的协同，实现高质量前景目标掩码生成，在 DIS5K 基准上全面超越 11 种 SOTA 方法。

**[MOVE: Motion-Guided Few-Shot Video Object Segmentation](segmentation/move_motion-guided_few-shot_video_object_segmentation.md)**

:   本文提出运动引导的少样本视频目标分割新任务及大规模数据集 MOVE（224 类运动、4300 视频、314K mask），并设计解耦运动-外观网络 DMA，通过帧差提取运动原型+外观原型的双分支架构，在新基准上显著优于现有 FSVOS 方法。

**[Online Generic Event Boundary Detection](segmentation/online_generic_event_boundary_detection.md)**

:   本文提出在线通用事件边界检测（On-GEBD）这一新任务——在流式视频中实时检测事件边界，并设计了基于认知科学事件分割理论（EST）的 ESTimator 框架，通过一致事件预测器（CEA）和在线边界判别器（OBD）的协同，在 Kinetics-GEBD 上 Avg F1 达到 0.748，超越所有在线基线且接近离线方法的性能。

**[RAGNet: Large-scale Reasoning-based Affordance Segmentation Benchmark towards General Grasping](segmentation/ragnet_large-scale_reasoning-based_affordance_segmentation_benchmark_towards_gen.md)**

:   构建了首个大规模推理式 affordance 分割基准 RAGNet（273k 图像、180 类别、26k 推理指令），并提出 AffordanceNet 框架，将 VLM 预训练的 affordance 预测与抓取姿态生成相结合，展现出强大的开放世界泛化和推理能力。

**[SAM2Long: Enhancing SAM 2 for Long Video Segmentation with a Training-Free Memory Tree](segmentation/sam2long_enhancing_sam_2_for_long_video_segmentation_with_a.md)**

:   针对SAM 2在长视频中因贪心选择策略导致的错误累积问题，提出一种training-free的约束树搜索记忆策略，维护多条分割路径并在视频级别选择最优结果，在9个VOS和3个VOT benchmark上平均提升3.7 J&F，长视频场景最高提升5.3。

**[SCORE: Scene Context Matters in Open-Vocabulary Remote Sensing Instance Segmentation](segmentation/score_scene_context_matters_in_openvocabulary_remote_sensing.md)**

:   提出SCORE框架，通过引入区域上下文（RAI）和全局上下文适配（GCA）两个模块，将遥感专用CLIP的多粒度场景知识注入到开放词汇实例分割pipeline中，在多个遥感数据集上的跨数据集评估中平均mAP超越前SOTA 5.53%。

---

## 🏥 医学图像 { #medical_imaging }

**[AcZeroTS: Active Learning for Zero-shot Tissue Segmentation in Pathology Images](medical_imaging/aczerots_active_learning_for_zeroshot_tissue_segmentation_in.md)**

:   提出AcZeroTS框架，将主动学习与基于VLM的原型引导零样本分割模型ProZS结合，通过同时考虑不确定性、多样性和原型覆盖unseen类的能力来选择最有价值的标注样本，以最少标注实现seen和unseen组织类型的高质量分割。

**[An OpenMind for 3D Medical Vision Self-supervised Learning](medical_imaging/an_openmind_for_3d_medical_vision_selfsupervised_learning.md)**

:   发布了最大的公开3D医学影像预训练数据集OpenMind（114k脑MRI体积），并在该数据集上系统性benchmark了现有3D SSL方法在最先进CNN（ResEnc-L）和Transformer（Primus-M）架构上的表现，明确了3D医学图像SSL的当前SOTA。

**[Beyond Brain Decoding: Visual-Semantic Reconstructions to Mental Creation Extension Based on fMRI](medical_imaging/beyond_brain_decoding_visualsemantic_reconstructions_to_ment.md)**

:   提出NeuroCreat——一种结合LLM视觉与文本能力的脑多模态架构，将fMRI解码从单一的视觉刺激重建扩展到**图像重建 + 文本描述（captioning）+ 心理创造（creation）**三个层次，通过Prompt Variant Alignment模块有效弥合fMRI低分辨率信号与高级语义表征之间的鸿沟。

**[Boosting Vision Semantic Density with Anatomy Normality Modeling for Medical Vision-language Pre-training](medical_imaging/boosting_vision_semantic_density_with_anatomy_normality_mode.md)**

:   提出 ViSD-Boost，通过疾病级视觉对比学习增强视觉语义 + VQ-VAE 建模解剖正常性分布来放大异常信号，解决医学 VLP 中视觉语义密度低导致的对齐偏差，在腹部 CT 54 种疾病零样本诊断达到 84.9% AUC。

**[CryoFastAR: Fast Cryo-EM Ab initio Reconstruction Made Easy](medical_imaging/cryofastar_fast_cryoem_ab_initio_reconstruction_made_easy.md)**

:   首个将DUSt3R式的几何基础模型范式引入冷冻电镜(cryo-EM)领域的工作，通过ViT编码器+跨视图注意力解码器直接从大量含噪粒子图像前馈预测姿态（无需迭代优化），实现了比传统方法快10-33倍的ab initio蛋白质三维重建。

**[CuMPerLay: Learning Cubical Multiparameter Persistence Vectorizations](medical_imaging/cumperlay_learning_cubical_multiparameter_persistence_vectorizations.md)**

:   提出 CuMPerLay，一个可微的立方多参数持久同调 (Cubical Multiparameter Persistence, CMP) 向量化层，将 CMP 分解为多条可学习的单参数持久同调线，通过联合学习双滤过 (bifiltration) 函数实现端到端训练，嵌入 Swin Transformer 后在医学图像分类和语义分割任务上（尤其小数据场景）取得显著提升。

**[RadGPT: Constructing 3D Image-Text Tumor Datasets](medical_imaging/radgpt_constructing_3d_image-text_tumor_datasets.md)**

:   本文提出 RadGPT——一个解剖感知的 VL AI 管线，通过将放射科医师修订的肿瘤分割 mask 经由确定性算法转化为结构化报告、再由 LLM 适配为叙述性报告，构建了首个大规模公开腹部 CT 图文肿瘤数据集 AbdomenAtlas 3.0（9,262 例 CT、每体素标注 + 报告），并证明分割辅助可显著提升 AI 报告中的肿瘤检测率。

**[SegAnyPET: Universal Promptable Segmentation from Positron Emission Tomography Images](medical_imaging/seganypet_universal_promptable_segmentation_from_positron_emission_tomography_im.md)**

:   本文构建了迄今最大的PET分割数据集PETS-5k（5731例3D全身PET图像，超130万张2D切片），并提出SegAnyPET——首个针对PET影像的3D可提示分割基础模型，通过跨提示置信学习（CPCL）策略处理标注质量不一致问题，在已见和未见目标上均大幅超越现有基础模型和任务专用模型。

**[Toward Long-Tailed Online Anomaly Detection through Class-Agnostic Concepts](medical_imaging/toward_long-tailed_online_anomaly_detection_through_class-agnostic_concepts.md)**

:   本文提出长尾在线异常检测（LTOAD）新任务和benchmark，核心创新是用可学习的"类无关概念集"替代传统的类标签依赖，结合Concept VQ-VAE和综合prompt学习框架，在不需要类标签的情况下于offline和online场景下均达到SOTA。

**[Visual Surface Wave Elastography: Revealing Subsurface Physical Properties via Visible Surface Waves](medical_imaging/visual_surface_wave_elastography_revealing_subsurface_physical_properties_via_vi.md)**

:   本文提出 VSWE（Visual Surface Wave Elastography），仅通过一段表面波传播的视频，提取色散关系并结合基于物理的有限元优化，推断介质的亚表面厚度和刚度参数，在模拟和真实明胶实验中均实现了高精度的参数恢复，为居家健康监测提供了概念验证。

---

## 🎯 目标检测 { #object_detection }

**[3D-MOOD: Lifting 2D to 3D for Monocular Open-Set Object Detection](object_detection/3dmood_lifting_2d_to_3d_for_monocular_openset_object_detecti.md)**

:   提出首个端到端的单目开放集3D目标检测器3D-MOOD，通过将开放集2D检测"提升"到3D空间，结合几何感知3D query生成与canonical image space设计，在Omni3D闭集和Argoverse 2/ScanNet开集基准上均达到SOTA。

**[Augmenting Moment Retrieval: Zero-Dependency Two-Stage Learning](object_detection/augmenting_moment_retrieval_zero-dependency_two-stage_learning.md)**

:   提出 AMR 框架，通过 Splice-and-Boost 数据增强策略和冷启动-蒸馏两阶段训练，在不依赖任何外部数据/预训练模型的前提下，大幅提升视频时刻检索的边界感知能力和语义辨别力，在 QVHighlights 上超越 SOTA +5%。

**[DiffDoctor: Diagnosing Image Diffusion Models Before Treating](object_detection/diffdoctor_diagnosing_image_diffusion_models_before_treating.md)**

:   提出 DiffDoctor，首个利用像素级反馈微调扩散模型的方法：先训练鲁棒的 artifact 检测器（1M+ 样本，类别平衡策略），再通过最小化合成图中每个像素的 artifact 置信度反向传播梯度到扩散模型，使其在未见 prompt 上也能显著减少 artifact 生成。

**[Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-time Open-Vocabulary Object Detection](object_detection/dynamicdino_finegrained_mixture_of_experts_tuning_for_realti.md)**

:   首次将Mixture of Experts引入实时开放词汇目标检测器，通过MoE-Tuning将Grounding DINO 1.5 Edge从dense模型扩展为动态推理框架，提出细粒度专家分解和预训练权重分配策略，仅用1.56M开源数据超越使用20M私有数据训练的原版模型。

**[EA-KD: Entropy-based Adaptive Knowledge Distillation](object_detection/ea-kd_entropy-based_adaptive_knowledge_distillation.md)**

:   提出 EA-KD，一种基于信息熵的即插即用知识蒸馏方法：通过结合 teacher 和 student 输出的熵值动态重加权蒸馏损失，优先学习高熵（高信息量）样本，在图像分类、目标检测和 LLM 蒸馏任务上均一致提升多种 KD 框架的性能，且计算开销可忽略。

**[SFUOD: Source-Free Unknown Object Detection](object_detection/sfuod_source-free_unknown_object_detection.md)**

:   提出 Source-Free Unknown Object Detection (SFUOD) 新场景，并设计 CollaPAUL 框架，通过协作调优融合源域和目标域知识 + 基于主轴的未知物体伪标签分配，在无源数据条件下同时检测已知和未知物体。

**[ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition](object_detection/viewsrd_3d_visual_grounding_via_structured_multi-view_decomposition.md)**

:   提出 ViewSRD 框架，将 3D 视觉定位建模为结构化多视角分解过程：通过 SRD 模块将复杂多锚点查询解耦为简单单锚点查询，并引入跨模态一致视角 token (CCVT) 解决视角变化导致的空间描述不一致问题。

**[VisRL: Intention-Driven Visual Perception via Reinforced Reasoning](object_detection/visrl_intention-driven_visual_perception_via_reinforced_reasoning.md)**

:   VisRL是首个将强化学习应用于意图驱动视觉感知的框架，通过迭代DPO训练让大多模态模型学会根据查询意图自主选择关注区域（预测bounding box），无需昂贵的中间bounding box标注即可实现比SFT更强的视觉推理能力。

**[Visual-RFT: Visual Reinforcement Fine-Tuning](object_detection/visual-rft_visual_reinforcement_fine-tuning.md)**

:   Visual-RFT将DeepSeek R1的强化学习+可验证奖励(RLVR)范式从数学/代码领域扩展到视觉感知任务，设计了IoU奖励（目标检测）和CLS奖励（分类）等任务特异的可验证奖励函数，在细粒度分类、少样本检测、推理定位等任务上以极少数据大幅超越SFT。

**[YOLOE: Real-Time Seeing Anything](object_detection/yoloe_realtime_seeing_anything.md)**

:   提出YOLOE，在YOLO架构中统一支持文本提示、视觉提示和无提示三种开放场景的检测和分割，通过RepRTA（可重参数化区域-文本对齐）、SAVPE（语义激活视觉提示编码器）和LRPC（懒惰区域-提示对比）三个设计实现高效率高性能，以3x更少的训练成本在LVIS上超越YOLO-World v2。

---

## 🧑 人体理解 { #human_understanding }

**[A Quality-Guided Mixture of Score-Fusion Experts Framework for Human Recognition](human_understanding/a_qualityguided_mixture_of_scorefusion_experts_framework_for.md)**

:   提出 Quality-guided Mixture of score-fusion Experts (QME) 框架，通过质量引导的 MoE 策略对来自不同生物特征模态（人脸、步态、身体）的相似度分数进行可学习融合，配合伪质量损失和分数三元组损失，在多个全身生物特征识别基准上达到 SOTA。

**[Avat3r: Large Animatable Gaussian Reconstruction Model for High-fidelity 3D Head Avatars](human_understanding/avat3r_large_animatable_gaussian_reconstruction_model_for_hi.md)**

:   提出Avat3r——首个可动画的大型3D重建模型(LRM)，仅需4张输入图像即可在前馈方式下回归出高质量可驱动的3D高斯头部头像，通过整合DUSt3R位置图和Sapiens语义特征作为先验、并用简单的cross-attention建模表情动画，在Ava256和NeRSemble数据集上大幅超越现有方法。

**[CarGait: Cross-Attention based Re-ranking for Gait Recognition](human_understanding/cargait_crossattention_based_reranking_for_gait_recognition.md)**

:   提出CarGait——基于cross-attention的步态识别重排序方法：对任意单阶段步态模型的top-K检索结果，通过probe与候选间步态条带(gait strip)的cross-attention学习细粒度pair-wise交互，生成新的条件化表征并重新计算距离进行重排序。在Gait3D/GREW/OU-MVLP三个数据集、7种基线模型上一致提升Rank-1/5准确率，推理速度6.5ms/probe远超现有重排序方法。

**[Hi3DGen: High-fidelity 3D Geometry Generation from Images via Normal Bridging](human_understanding/hi3dgen_high-fidelity_3d_geometry_generation_from_images_via_normal_bridging.md)**

:   提出 Hi3DGen 框架，以法线图作为中间表示桥接 2D 图像到 3D 几何的映射，通过噪声注入回归式法线估计器（NiRNE）和法线正则化潜在扩散（NoRLD）两大核心组件，显著提升生成 3D 模型的几何细节保真度。

**[Multi-view Gaze Target Estimation](human_understanding/multi-view_gaze_target_estimation.md)**

:   本文首次将注视目标估计（GTE）从单视角扩展到多视角，通过头部信息聚合（HIA）、基于不确定性的注视选择（UGS）和基于极线的场景注意力（ESA）三个模块融合多相机信息，在自建 MVGT 数据集上显著超越单视角 SOTA，并实现了单视角方法无法处理的跨视角估计。

**[NegRefine: Refining Negative Label-Based Zero-Shot OOD Detection](human_understanding/negrefine_refining_negative_label-based_zero-shot_ood_detection.md)**

:   本文提出 NegRefine，通过 LLM 过滤负标签集中的专有名词和子类别标签，并设计多标签匹配评分函数来处理图像同时匹配分布内和负标签的情况，在 ImageNet-1K 基准上平均 AUROC 提升 1.82%、FPR95 降低 4.35%，刷新了零样本 OOD 检测 SOTA。

**[Neural Multi-View Self-Calibrated Photometric Stereo without Photometric Stereo Cues](human_understanding/neural_multi-view_self-calibrated_photometric_stereo_without_photometric_stereo_.md)**

:   提出一种端到端的神经逆渲染框架，从多视图变化光照图像中联合恢复几何、空间变化反射率和光照参数，无需光源标定或中间光度立体线索（如法线图），超越了现有的分阶段 MVPS 方法。

**[SignRep: Enhancing Self-Supervised Sign Representations](human_understanding/signrep_enhancing_self-supervised_sign_representations.md)**

:   提出 SignRep，一个可扩展的自监督手语表征学习框架，通过在 Masked Autoencoder 预训练中利用手语骨架先验、特征正则化和对抗式风格无关损失，仅用单一 RGB 模态即超越了复杂的多模态/多分支方法，在手语识别、字典检索和手语翻译三大任务上均取得 SOTA。

---

## 🖼️ 图像恢复 { #image_restoration }

**[ALOcc: Adaptive Lifting-Based 3D Semantic Occupancy and Cost Volume-Based Flow Predictions](image_restoration/alocc_adaptive_liftingbased_3d_semantic_occupancy_and_cost_v.md)**

:   提出ALOcc框架，通过遮挡感知的自适应提升机制、语义原型对齐和BEV代价体flow预测三个改进，在多个占据预测基准上取得SOTA，同时保持较高推理速度。

**[Benchmarking Burst Super-Resolution for Polarization Images: Noise Dataset and Analysis](image_restoration/benchmarking_burst_superresolution_for_polarization_images_n.md)**

:   针对偏振相机"光效低、分辨率低、噪声大"的硬件瓶颈，构建了两个专用数据集（PolarNS用于噪声统计分析，PolarBurstSR用于burst超分的训练/评测），提出偏振噪声传播分析模型，并将5种SOTA burst超分方法适配到偏振域，证明偏振专用训练在强度图(s0)和偏振角(AoLP)重建上显著优于RGB通用训练。

**[Blind2Sound: Self-Supervised Image Denoising without Residual Noise](image_restoration/blind2sound_self-supervised_image_denoising_without_residual_noise.md)**

:   提出 Blind2Sound 框架，通过自适应重可见损失（adaptive re-visible loss）感知噪声水平并实现个性化去噪，配合 Cramer Gaussian 损失提升噪声参数估计精度，在自监督盲去噪中消除残余噪声，性能超越同期所有自监督方法甚至部分有监督基线。

**[Blind Noisy Image Deblurring Using Residual Guidance Strategy](image_restoration/blind_noisy_image_deblurring_using_residual_guidance_strateg.md)**

:   提出残差引导策略（RGS），在图像金字塔的粗到细估计过程中，利用相邻粗尺度的卷积残差经 guided filter 去噪后校正当前尺度的模糊图像，从而在高噪声（σ=0.1）下显著提升盲去模糊的核估计精度和恢复质量，无需训练即超越多种深度学习方法。

**[Generic Event Boundary Detection via Denoising Diffusion (DiffGEBD)](image_restoration/generic_event_boundary_detection_via_denoising_diffusion.md)**

:   DiffGEBD 首次将扩散模型引入通用事件边界检测（GEBD），通过将边界预测建模为从随机噪声到合理边界分布的去噪过程，利用 Classifier-Free Guidance 控制预测多样性，并提出了对称 F1 和 Diversity Score 两项新评估指标来衡量多预测场景下的质量与多样性。

**[Low-Light Image Enhancement using Event-Based Illumination Estimation (RetinEV)](image_restoration/low-light_image_enhancement_using_event-based_illumination_estimation.md)**

:   RetinEV 提出利用事件相机的"时间映射事件"（temporal-mapping events，由透射率调制触发）而非传统"运动事件"进行光照估计，结合 Retinex 理论将低光照图像分解为光照和反射率分量，通过光照辅助反射率增强（IRE）模块实现高质量低光照图像增强，在 640×480 分辨率下达到 35.6 FPS 实时速度。

**[Robust Adverse Weather Removal via Spectral-based Spatial Grouping (SSGformer)](image_restoration/robust_adverse_weather_removal_via_spectral-based_spatial_grouping.md)**

:   SSGformer 提出一种基于光谱分解和分组注意力的 All-in-One 恶劣天气图像复原方法：利用 Sobel 算子提取高频边缘信息和 SVD 分析低频退化纹理，将二者融合后生成空间分组掩码（grouping-mask），在组内执行通道和空间注意力以实现对多种天气退化（雨、雪、雾、雨滴）的鲁棒去除。

---

## 📦 模型压缩 { #model_compression }

**[A Good Teacher Adapts Their Knowledge for Distillation](model_compression/a_good_teacher_adapts_their_knowledge_for_distillation.md)**

:   本文揭示了知识蒸馏中教师-学生容量差距问题的本质原因在于**输出分布的类内分布不匹配**，并提出 AID（Adapted Intra-class Distribution）方法，在蒸馏前对教师模型进行微调以优化其类内分布使之更符合学生的学习能力，在多种架构组合上取得了SOTA性能。

**[TokenBridge: Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation](model_compression/bridging_continuous_and_discrete_tokens_for_autoregressive_v.md)**

:   TokenBridge提出对预训练VAE连续特征进行后训练维度级量化，将连续token无损转化为离散token，再通过轻量级维度级自回归头高效建模指数级大词表空间，在ImageNet 256×256上用标准交叉熵损失达到了与连续token方法（如MAR）相当的生成质量（FID=1.55），且推理快5.94倍。

**[CIARD: Cyclic Iterative Adversarial Robustness Distillation](model_compression/ciard_cyclic_iterative_adversarial_robustness_distillation.md)**

:   提出CIARD，通过对比推离损失（Contrastive Push Loss）解决双教师ARD框架中clean teacher和robust teacher的优化目标冲突，并设计迭代教师训练（ITT）策略持续更新robust teacher以防止性能退化，在CIFAR-10/100和Tiny-ImageNet上同时提升对抗鲁棒性+3.53%和干净准确率+5.87%。

**[Color Matching Using Hypernetwork-Based Kolmogorov-Arnold Networks (cmKAN)](model_compression/color_matching_using_hypernetwork-based_kolmogorov-arnold_networks.md)**

:   提出cmKAN，利用超网络驱动的Kolmogorov-Arnold Network进行颜色匹配，通过生成器预测空间变化的KAN样条参数，支持有监督/无监督/配对优化三种场景和raw-to-raw/raw-to-sRGB/sRGB-to-sRGB三种任务，在所有任务上平均超越现有方法37.3%且极轻量（76.4K参数）。

**[FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning](model_compression/fastvar_linear_visual_autoregressive_modeling_via_cached_token_pruning.md)**

:   FastVAR 提出一种无需训练的后处理加速方法，通过观察 VAR 模型中大尺度步骤主要建模高频纹理且对剪枝鲁棒的特性，利用频域引导的关键 token 选择（PTS）仅保留高频 token 参与前向，并用缓存的早期尺度 token 恢复被剪枝的位置（CTR），在 FlashAttention 基础上实现额外 2.7× 加速且性能损失 <1%，并首次实现单张 3090 GPU 上 1.5 秒生成 2K 图像。

**[MSQ: Memory-Efficient Bit Sparsification Quantization](model_compression/msq_memory-efficient_bit_sparsification_quantization.md)**

:   提出MSQ，通过RoundClamp量化器从权重直接计算最低有效位(LSB)并施加L1正则化诱导稀疏性，无需显式创建bit-level可训练参数即可实现混合精度量化发现，训练参数减少8倍、训练时间减少86%，同时保持竞争性的精度-压缩权衡。

**[StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data](model_compression/stolenlora_exploring_lora_extraction_attacks_via_synthetic_data.md)**

:   StolenLoRA 首次提出针对 LoRA 自适应模型的模型提取攻击方向，利用 LLM 驱动的 Stable Diffusion 生成高质量合成数据替代真实数据集搜索，并设计基于分歧的半监督学习（DSL）策略通过选择性查询最大化信息增益，仅需 10k 次查询即可达到高达 96.60% 的攻击成功率，揭示了 LoRA 适配模型的严重安全漏洞。

---

## 🔄 自监督/表示学习 { #self_supervised }

**[A Token-level Text Image Foundation Model for Document Understanding (TokenFD/TokenVL)](self_supervised/a_tokenlevel_text_image_foundation_model_for_document_unders.md)**

:   提出首个 token 级别文本图像基础模型 TokenFD，通过在 2000 万图像、18 亿 BPE token-mask 对上进行 token 级视觉-语言对齐预训练，实现 image-as-text 语义能力，并基于此构建文档理解 MLLM TokenVL，在 OCRBench 上得分 860（8B 组最高），在 DocVQA 等十项 VQA 任务上平均提升 8.8%。

**[AIM: Amending Inherent Interpretability via Self-Supervised Masking](self_supervised/aim_amending_inherent_interpretability_via_self-supervised_masking.md)**

:   本文提出 AIM，一种基于自监督二值掩码的 top-down 特征选择机制，无需额外标注即可引导 CNN 聚焦真实判别特征、抑制虚假相关，同时获得内在可解释性和更强的 OOD 泛化能力。

**[Always Skip Attention](self_supervised/always_skip_attention.md)**

:   本文从理论上证明了 Vision Transformer 中的自注意力机制是本质上病态的（ill-conditioned），在无 skip connection 时会导致训练崩溃，并提出 Token Graying（TG）方法通过改善输入 token 的条件数来进一步增强 ViT 的训练稳定性和性能。

**[CObL: Toward Zero-Shot Ordinal Layering without User Prompting](self_supervised/cobl_toward_zero-shot_ordinal_layering_without_user_prompting.md)**

:   本文提出 CObL，一种基于多个冻结 Stable Diffusion UNet 并行生成的架构，能在无需用户提示、不知物体数量的前提下，从单张图像推断出遮挡排序的物体层叠表示（每层一个 amodal 完整物体），并且仅用数千张合成桌面场景就能零样本泛化到真实世界照片。

**[LoftUp: Learning a Coordinate-Based Feature Upsampler for Vision Foundation Models](self_supervised/loftup_learning_a_coordinatebased_feature_upsampler_for_visi.md)**

:   提出LoftUp，通过坐标-cross-attention架构直接将低分辨率VFM特征映射到任意高分辨率，并用class-agnostic mask精炼+自蒸馏构建全分辨率伪GT进行训练，在6个下游任务上平均提升10-20%且在视频目标分割上提升近50%。

**[Manual-PA: Learning 3D Part Assembly from Instruction Diagrams](self_supervised/manual-pa_learning_3d_part_assembly_from_instruction_diagrams.md)**

:   提出 Manual-PA，一个基于 Transformer 的说明书引导 3D 零件组装框架：通过对比学习将 3D 零件与说明书步骤图对齐来推断组装顺序，再以学到的顺序作为位置编码的软引导进行 6DoF 位姿预测，在 PartNet 上显著超越现有方法。

**[Scaling Language-Free Visual Representation Learning](self_supervised/scaling_languagefree_visual_representation_learning.md)**

:   通过在MetaCLIP的20亿web图像上训练DINOv2/MAE系列模型（1B-7B参数），系统性地证明纯视觉自监督学习在模型和数据规模上展现优于CLIP的scaling behavior，5B+参数时在VQA平均性能上超越CLIP——包括传统认为需要语言监督的OCR/Chart任务。

---

## 🎬 视频理解 { #video_understanding }

**[4D-Bench: Benchmarking Multi-modal Large Language Models for 4D Object Understanding](video_understanding/4dbench_benchmarking_multimodal_large_language_models_for_4d.md)**

:   提出 4D-Bench，首个评估多模态大语言模型对4D物体（具有时间演化的3D物体）理解能力的基准，包含4D物体问答（751 QA对）和4D物体描述（580物体×5标注）两大任务，发现即使SOTA的GPT-4o也仅达63%准确率（人类91%），揭示了MLLM在多视角时空理解上的巨大差距。

**[D3: Training-Free AI-Generated Video Detection Using Second-Order Features](video_understanding/d3_training-free_ai-generated_video_detection_using_second-order_features.md)**

:   本文从牛顿力学的二阶控制系统出发，发现真实视频和 AI 生成视频在二阶时序特征（"加速度"）上存在本质差异——真实视频波动大而生成视频平坦，据此提出 D3，一种完全免训练的 AI 生成视频检测方法，仅需计算帧间特征的二阶差分标准差即可判别，在 40 个测试子集上达到 SOTA。

**[DOLLAR: Few-Step Video Generation via Distillation and Latent Reward Optimization](video_understanding/dollar_fewstep_video_generation_via_distillation_and_latent.md)**

:   结合变分分数蒸馏（VSD）和一致性蒸馏实现few-step视频生成，同时提出潜空间奖励模型微调方法进一步优化生成质量，4步生成的10秒视频（128帧@12FPS）在VBench上达82.57分超越teacher模型和Gen-3/Kling等基线，1步蒸馏实现278.6倍加速。

**[DreamRelation: Relation-Centric Video Customization](video_understanding/dreamrelation_relation-centric_video_customization.md)**

:   提出 DreamRelation，首个关系中心的视频定制方法，通过 Relation LoRA Triplet + Hybrid Mask Training 实现关系与外观的解耦，并通过时空关系对比损失增强关系动态学习，使动物能模仿人类交互。

**[Flow4Agent: Long-form Video Understanding via Motion Prior from Optical Flow](video_understanding/flow4agent_long-form_video_understanding_via_motion_prior_from_optical_flow.md)**

:   Flow4Agent 首次将光流运动先验引入 LLM-based 视频理解，通过时域粒度优化（TGO）利用粗粒度光流聚类视频事件并用语义先验过滤冗余场景，通过运动 Token 剪枝（MTP）利用细粒度光流去除帧内静态冗余 token，在 VideoMME/MLVU/LongVideoBench 等长视频基准上取得领先表现。

**[UMDATrack: Unified Multi-Domain Adaptive Tracking Under Adverse Weather Conditions](video_understanding/umdatrack_unified_multi-domain_adaptive_tracking_under_adverse_weather_condition.md)**

:   UMDATrack 提出了首个统一多域自适应跟踪框架，利用文本引导扩散模型合成少量（<2% 帧）多天气条件无标注视频，通过域定制适配器（DCA）高效迁移目标表征到不同天气域，并引入基于最优传输的目标感知置信度对齐（TCA）增强跨域定位一致性，在夜间/雾天/雨天等场景中大幅超越现有 SOTA 跟踪器。

**[VACE: All-in-One Video Creation and Editing](video_understanding/vace_allinone_video_creation_and_editing.md)**

:   提出VACE统一视频生成和编辑框架，通过Video Condition Unit（VCU）将参考图→视频生成、视频→视频编辑、mask视频编辑等多种任务的输入统一为标准接口，配合Context Adapter注入时空条件信息，单一模型在各子任务上达到专用模型水平并支持灵活的任务组合。

---

## 🛡️ AI 安全 { #ai_safety }

**[A Framework for Double-Blind Federated Adaptation of Foundation Models](ai_safety/a_framework_for_doubleblind_federated_adaptation_of_foundati.md)**

:   BlindFed提出了双盲联邦基础模型适配框架：通过FHE友好的架构重设计（多项式近似非线性操作）+ 两阶段分割学习（离线知识蒸馏 + 在线加密推理）+ 隐私增强（样本置换 + 随机块采样），在数据方看不到模型、模型方看不到数据的约束下实现了接近LoRA的适配精度。

**[Active Membership Inference Test (aMINT): Enhancing Model Auditability with Multi-Task Learning](ai_safety/active_membership_inference_test_amint_enhancing_model_audit.md)**

:   提出Active MINT（aMINT），将成员推断检测作为训练时的优化目标，通过多任务学习让被审计模型与MINT模型联合训练、共享早期特征层，在不显著损失主任务性能的前提下，将训练数据的识别准确率从被动MINT的~60%大幅提升至80%以上。

**[SpecGuard: Spectral Projection-based Advanced Invisible Watermarking](ai_safety/specguard_spectral_projection-based_advanced_invisible_watermarking.md)**

:   SpecGuard 提出将水印信息嵌入到小波分解后的高频子带的频谱域中（通过 FFT 近似的频谱投影），编码端用强度因子增强鲁棒性，解码端利用 Parseval 定理设计可学习阈值进行比特恢复，在保持高图像质量（PSNR>42dB）的同时实现了对畸变、再生成和对抗攻击的全面鲁棒性，超越了现有 SOTA 方法。

**[Towards Adversarial Robustness via Debiased High-Confidence Logit Alignment](ai_safety/towards_adversarial_robustness_via_debiased_high-confidence_logit_alignment.md)**

:   揭示了逆向对抗攻击（inverse adversarial attack）在对抗训练中导致模型注意力偏移至背景特征的虚假相关性问题，提出 DHAT 方法通过去偏高置信度 logit 正则化（DHLR）和前景 logit 正交增强（FLOE）两个组件来消除这种偏差，在 CIFAR-10/100 和 ImageNet-1K 上取得了 SOTA 的对抗鲁棒性。

---

## 🤖 机器人/具身智能 { #robotics }

**[Certifiably Optimal Anisotropic Rotation Averaging](robotics/certifiably_optimal_anisotropic_rotation_averaging.md)**

:   提出了一种新的SDP松弛方法，通过强制解落在SO(3)的凸包conv(SO(3))内，首次实现了各向异性代价下的可证明全局最优旋转平均，解决了传统O(3)松弛在各向异性场景下完全失效的问题。

**[EvolvingGrasp: Evolutionary Grasp Generation via Efficient Preference Alignment](robotics/evolvinggrasp_evolutionary_grasp_generation_via_efficient_preference_alignment.md)**

:   提出 EvolvingGrasp，通过 Handpose-wise Preference Optimization (HPO) 和 Physics-Aware Consistency Model (PCM) 实现灵巧抓取姿态的高效进化式生成与人类偏好对齐，在四个基准数据集上取得 SOTA，并实现 30 倍加速。

**[SITE: towards Spatial Intelligence Thorough Evaluation](robotics/site_towards_spatial_intelligence_thorough_evaluation.md)**

:   本文提出 SITE，一个基于认知科学三重分类体系的空间智能综合基准，涵盖 8,068 个多选 VQA 任务（覆盖 31 个数据集、图像+视频），评估结果显示当前最强 VLM（GPT-4o）在整体空间推理上仍落后人类专家约 32%，且 VLM 的空间智能与机器人操控任务的成功率呈高度正相关（Pearson $r=0.902$）。

**[VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](robotics/vq-vla_improving_vision-language-action_models_via_scaling_vector-quantized_acti.md)**

:   本文提出基于卷积残差 VQ-VAE 的动作 tokenizer，在比先前方法多 100 倍的训练数据（含大量合成数据）上训练后可零样本迁移到各种下游 VLA 任务，在真实机器人上将长时域任务成功率提升最高 30%，推理速度提升近 3 倍。

---

## 🎵 音频/语音 { #audio_speech }

**[2.5 Years in Class: A Multimodal Textbook for Vision-Language Pretraining](audio_speech/25_years_in_class_a_multimodal_textbook_for_visionlanguage_p.md)**

:   从YouTube收集2.5年(22,000课时)的教学视频，通过LLM驱动的多级抽取与过滤管线构建高质量交错图文"多模态教科书"语料(6.5M关键帧 + 0.75B文本token)，显著提升VLM在知识密集型和推理任务上的预训练效果，尤其在ScienceQA和MathVista上带来大幅提升。

**[Lyra: An Efficient and Speech-Centric Framework for Omni-Cognition](audio_speech/lyra_an_efficient_and_speechcentric_framework_for_omnicognit.md)**

:   提出Lyra，一个以语音为中心的全模态MLLM框架，通过三大核心组件（DTW-based跨模态正则化器、多模态LoRA、Latent多模态提取器）和首个12K长语音SFT数据集，在仅用2.7M数据和少量训练的情况下，同时在视觉-语言、视觉-语音、语音-语言benchmark上达到SOTA，并能处理长达2小时的语音输入。

**[MemoryTalker: Personalized Speech-Driven 3D Facial Animation via Audio-Guided Stylization](audio_speech/memorytalker_personalized_speech-driven_3d_facial_animation_via_audio-guided_sty.md)**

:   提出 MemoryTalker，通过两阶段训练策略（Memorizing + Animating）利用键值记忆网络存储通用面部运动，并通过音频驱动的风格化记忆实现仅凭音频即可生成个性化 3D 面部动画，无需任何额外先验信息。

---

## ⚡ LLM 效率 { #llm_efficiency }

**[ArgoTweak: Towards Self-Updating HD Maps through Structured Priors](llm_efficiency/argotweak_towards_self-updating_hd_maps_through_structured_priors.md)**

:   提出 ArgoTweak，首个提供"旧地图先验 + 当前传感器数据 + 最新真值地图"完整三元组的 HD 地图数据集，通过双射映射框架将大规模地图修改分解为元素级原子变化，并引入可解释的评测指标（mAPC/mACC），将模型在 ArgoTweak 上训练后的 sim2real 差距降低 10 倍以上。

**[LayerTracer: Cognitive-Aligned Layered SVG Synthesis via Diffusion Transformer](llm_efficiency/layertracer_cognitive-aligned_layered_svg_synthesis_via_diffusion_transformer.md)**

:   LayerTracer 提出首个基于 Diffusion Transformer（DiT）的认知对齐分层 SVG 生成框架：通过构建 2 万+ 设计师操作序列数据集，训练 DiT 生成模拟设计师工作流程的多阶段光栅化蓝图，再通过逐层矢量化和路径去重转换为干净可编辑的分层 SVG；同时支持文本驱动生成和图像到分层 SVG 的转换。

**[StreamMind: Unlocking Full Frame Rate Streaming Video Dialogue through Event-Gated Cognition](llm_efficiency/streammind_unlocking_full_frame_rate_streaming_video_dialogue_through_event-gate.md)**

:   StreamMind 提出"事件门控 LLM 调用"范式替代现有的"逐帧 LLM 调用"，通过在视频编码器和 LLM 之间插入认知门控网络（Cognition Gate），仅在查询相关事件发生时才调用 LLM，配合基于状态空间方法的事件保持特征提取器（EPFE）实现常量感知成本，在单张 A100 上达到 **100 fps** 的流式视频处理速度。

---

## 🛰️ 遥感 { #remote_sensing }

**[RS-vHeat: Heat Conduction Guided Efficient Remote Sensing Foundation Model](remote_sensing/rs-vheat_heat_conduction_guided_efficient_remote_sensing_foundation_model.md)**

:   首次将物理热传导过程引入遥感基础模型，提出 RS-vHeat，用热传导算子（HCO）替代注意力机制来建模遥感图像中的局部区域相关性，在 4 个任务 10 个数据集上取得优异性能的同时，相比注意力基线减少 84% 显存、24% FLOPs、提升 2.7 倍吞吐量。

**[Towards a Unified Copernicus Foundation Model for Earth Vision](remote_sensing/towards_a_unified_copernicus_foundation_model_for_earth_visi.md)**

:   提出由Copernicus-Pretrain（1870万张覆盖全部Sentinel任务的对齐图像）、Copernicus-FM（通过扩展动态超网络和Fourier元数据编码处理任意光谱/非光谱传感器的统一基础模型）、Copernicus-Bench（15个分层下游任务基准）三位一体的完整EO基础模型体系，首次实现从地表到大气的跨模态联合预训练，在15个下游任务中11个以冻结编码器超越全参数监督训练。

**[WildSAT: Learning Satellite Image Representations from Wildlife Observations](remote_sensing/wildsat_learning_satellite_image_representations_from_wildlife_observations.md)**

:   提出 WildSAT，利用公民科学平台上的数百万地理标记野生动物观测数据，通过对比学习将卫星图像、物种位置和文本描述对齐，显著提升遥感图像表征质量，并支持零样本文本检索。

---

## 💬 LLM / NLP { #llm_nlp }

**[A Conditional Probability Framework for Compositional Zero-shot Learning](llm_nlp/a_conditional_probability_framework_for_compositional_zerosh.md)**

:   提出条件概率框架（CPF），将组合识别概率分解为对象似然 p(o|x) 和属性条件似然 p(a|o,x) 两部分，通过文本增强对象学习和对象引导属性学习两个模块显式建模属性-对象依赖关系，在三个 CZSL 基准上全面超越 SOTA。

**[Make Your Training Flexible: Towards Deployment-Efficient Video Models](llm_nlp/make_your_training_flexible_towards_deployment-efficient_video_models.md)**

:   本文提出Flux——一种使视频模型训练灵活化的数据增强工具，通过灵活采样网格+组动态token选择，使单一模型在不同计算预算下都能高效工作；并提出Token Optimization新测试范式，在1/4 token下即可匹配前SOTA性能，节省约90%计算。

---

## 📐 优化/理论 { #optimization }

**[Federated Continual Instruction Tuning](optimization/federated_continual_instruction_tuning.md)**

:   首次提出联邦持续指令微调（FCIT）基准，涵盖 2 种场景、4 种设置和 12 个数据集，并设计 DISCO 框架通过动态知识组织（DKO）和子空间选择性激活（SSA）有效解决数据异构性和灾难性遗忘。

**[Memory-Efficient 4-bit Preconditioned Stochastic Optimization](optimization/memory-efficient_4-bit_preconditioned_stochastic_optimization.md)**

:   提出基于 Cholesky 分解 + 误差反馈的 4-bit 量化方案，将 Shampoo 优化器的预条件矩阵压缩至 4-bit 精度，在大幅降低 GPU 显存的同时保持与 32-bit Shampoo 接近的训练性能，并给出了光滑与非光滑两种场景下的收敛性证明。

---

## 🔗 因果推理 { #causal_inference }

**[A Visual Leap in CLIP Compositionality Reasoning through Generation of Counterfactual Sets](causal_inference/a_visual_leap_in_clip_compositionality_reasoning_through_gen.md)**

:   提出基于LLM+扩散模型的block-based diffusion方法自动生成高质量反事实图文对数据集，配套设计set-aware损失函数，无需人工标注即可显著提升CLIP的组合推理能力，在ARO/VL-Checklist等benchmark上以更少数据超越SOTA。

---

## 🦾 LLM Agent { #llm_agent }

**[GTR: Guided Thought Reinforcement Prevents Thought Collapse in RL-based VLM Agent Training](llm_agent/gtr_guided_thought_reinforcement_prevents_thought_collapse_i.md)**

:   发现VLM agent在仅基于结果奖励的RL训练中会出现"思维坍塌"（thought collapse）——推理多样性急剧丧失、生成无关推理和无效动作。提出GTR框架通过自动纠正器在每步RL中评估和精炼agent推理，无需人工标注，LLaVA-7b在多种视觉环境中任务成功率提升3-5倍。

---

## 💡 LLM 推理 { #llm_reasoning }

**[Corvid: Improving Multimodal Large Language Models Towards Chain-of-Thought Reasoning](llm_reasoning/corvid_improving_multimodal_large_language_models_towards_ch.md)**

:   提出Corvid，通过混合视觉编码器+GateMixer连接器增强视觉表示、MCoT-Instruct-287K高质量CoT指令数据集+两阶段CoT训练增强推理能力、以及推理时自验证策略避免过度/不足推理，在数学推理和科学问题解决上超越同规模o1-like MLLM。

---

## ✍️ 文本生成 { #nlp_generation }

**[TikZero: Zero-Shot Text-Guided Graphics Program Synthesis](nlp_generation/tikzero_zero-shot_text-guided_graphics_program_synthesis.md)**

:   提出 TikZero，通过将图像表示作为中间桥梁，将图形程序生成与文本理解解耦，实现零样本文本引导的 TikZ 图形程序合成，在无需文本对齐训练数据的情况下大幅超越基线方法，经端到端微调后的 TikZero+ 达到甚至超越 GPT-4o 等大型商业模型的性能。

---

## 🎮 强化学习 { #reinforcement_learning }

**[RL-Selector: Reinforcement Learning-Guided Data Selection via Redundancy Assessment](reinforcement_learning/reinforcement_learning-guided_data_selection_via_redundancy_assessment.md)**

:   提出 RL-Selector，引入 ε-sample cover 概念量化样本冗余度，将数据选择建模为强化学习过程，通过轻量 A2C 策略网络自适应优化选择策略，在多个基准数据集上以更少数据达到接近甚至超越全量训练的泛化性能。

---

## 📡 信号/通信 { #signal_comm }

**[Boosting Multimodal Learning via Disentangled Gradient Learning](signal_comm/boosting_multimodal_learning_via_disentangled_gradient_learning.md)**

:   本文揭示了多模态学习中模态编码器和融合模块之间的优化冲突——融合模块会抑制回传到各模态编码器的梯度，导致即使是优势模态也比单模态模型表现差，并提出解耦梯度学习（DGL）框架通过截断融合模块到编码器的梯度并用独立的单模态损失替代来解决此问题。

---

## 📂 其他 { #others }

**[3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark](others/3dsrbench_a_comprehensive_3d_spatial_reasoning_benchmark.md)**

:   提出首个全面的3D空间推理基准3DSRBench，包含2,772个人工标注的VQA对（12种问题类型），通过平衡数据分布和新型FlipEval策略实现鲁棒评估，揭示SOTA LMM（包括GPT-4o、Gemini）在3D空间推理上远落后于人类水平（≈52% vs 95.7%），且在非常规视角下性能显著退化。

**[A Hidden Stumbling Block in Generalized Category Discovery: Distracted Attention](others/a_hidden_stumbling_block_in_generalized_category_discovery_d.md)**

:   发现GCD中未标注数据（尤其是未知类别）的ViT注意力会分散到背景区域（distracted attention），提出Attention Focusing（AF）模块通过多尺度token重要性度量+自适应剪枝来纠正注意力，作为即插即用模块在SimGCD上最高带来15.4%的性能提升。

**[A Real-world Display Inverse Rendering Dataset](others/a_realworld_display_inverse_rendering_dataset.md)**

:   构建了首个基于LCD显示器-相机系统的真实世界逆渲染数据集，包含16个物体的OLAT（逐像素点亮）采集图像、偏振信息和GT几何，并提出简单有效的基线方法（基于Cook-Torrance BRDF的可微渲染优化），在150秒内超越现有逆渲染方法。

**[ACE-G: Improving Generalization of Scene Coordinate Regression Through Query Pre-Training](others/aceg_improving_generalization_of_scene_coordinate_regression.md)**

:   将场景坐标回归器拆分为「场景无关的Transformer」和「场景特定的map code」，通过在数万场景上进行交替的mapping/query预训练，显著提升SCR方法在光照、视角变化下的泛化能力，同时保持轻量化的计算开销。

**[AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes](others/adaptiveae_an_adaptive_exposure_strategy_for_hdr_capturing_i.md)**

:   本文提出AdaptiveAE，利用深度强化学习将HDR曝光包围拍摄建模为马尔可夫决策过程（MDP），同时优化ISO和快门速度的组合，在用户定义的时间预算内自适应地为动态场景选择最优曝光参数，在HDRV数据集上达到PSNR 39.70，比之前最好的方法Hasinoff et al. (37.59) 高出2.1 dB。

**[Adversarial Robust Memory-Based Continual Learner](others/adversarial_robust_memory-based_continual_learner.md)**

:   揭示持续学习与对抗训练结合时的双重挑战（加速遗忘 + 梯度混淆），提出抗遗忘 Logit 校准（AFLC）和鲁棒感知经验回放（RAER）两个即插即用模块，在 Split-CIFAR10/100 和 Split-Tiny-ImageNet 上有效提升对抗鲁棒性达 8.13%。

**[AFUNet: Cross-Iterative Alignment-Fusion Synergy for HDR Reconstruction via Deep Unfolding Paradigm](others/afunet_crossiterative_alignmentfusion_synergy_for_hdr_recons.md)**

:   将多曝光HDR重建从MAP估计视角建模，通过空间对应先验将问题分解为对齐和融合两个交替子问题，再展开为端到端可训练的AFUNet（含SAM空间对齐+CFM通道融合+DCM数据一致性模块），在三个HDR基准上取得SOTA，PSNR-μ达44.91dB（Kalantari数据集）。

**[Auto-Regressively Generating Multi-View Consistent Images (MV-AR)](others/autoregressively_generating_multiview_consistent_images.md)**

:   首次将自回归（AR）模型引入多视角图像生成任务，通过逐视角生成利用所有前序视角信息来增强远距离视角间的一致性，同时设计了统一的多模态条件注入架构和Shuffle Views数据增强策略，使单一模型可同时处理文本/图像/几何形状条件。

**[C4D: 4D Made from 3D through Dual Correspondences](others/c4d_4d_made_from_3d_through_dual_correspondences.md)**

:   提出C4D框架，通过在DUSt3R的3D pointmap预测基础上联合捕获双重时序对应(短时光流+动态感知长时点跟踪DynPT)，生成运动掩码分离动静区域，并引入相机运动对齐/相机轨迹平滑/点轨迹平滑三个优化目标，将现有3D重建范式升级为完整4D重建(逐帧点云+相机参数+2D/3D轨迹)，在深度/位姿/跟踪多个下游任务上达competitive性能。

**[Despite Exploring Contrastive Deep Skeletonpointcloudimutext](others/despite_exploring_contrastive_deep_skeletonpointcloudimutext.md)**

:   提出 DeSPITE，一个将 LiDAR 点云、骨架姿态、IMU 信号和文本四种模态对齐到联合嵌入空间的对比学习框架，首次以 LiDAR（而非 RGB）作为核心视觉模态，实现了跨模态匹配/检索等此前不可能的任务，同时作为有效的 HAR 预训练策略在 MSR-Action3D 和 HMPEAR 上取得 SOTA。

**[Doodle Your Keypoints: Sketch-Based Few-Shot Keypoint Detection](others/doodle_your_keypoints_sketch-based_few-shot_keypoint_detection.md)**

:   提出首个基于草图的跨模态少样本关键点检测框架，利用原型网络、网格定位器、原型域适应和去风格化网络，仅需少量带标注草图即可在真实照片中检测新类别的新关键点。

**[Forgetting Through Transforming: Enabling Federated Unlearning via Class-Aware Representation Transformation](others/forgetting_through_transforming_enabling_federated_unlearning_via_class-aware_re.md)**

:   提出 FUCRT 方法，通过类感知表征变换实现联邦遗忘：将遗忘类的表征“变换”到语义最近的保留类，而非直接消除，配合双重对比学习对齐跨客户端的变换一致性，在四个数据集上实现 100% 遗忘保障的同时保持甚至提升剩余类性能。

**[LaCoOT: Layer Collapse through Optimal Transport](others/lacoot_layer_collapse_through_optimal_transport.md)**

:   提出 LaCoOT，一种基于最优传输的正则化策略，通过最小化网络内部中间特征分布之间的 Max-Sliced Wasserstein 距离，使得训练后可以直接移除整个网络层，在保持性能的同时显著减少模型深度和推理时间。

**[Thermal Polarimetric Multi-view Stereo](others/thermal_polarimetric_multi-view_stereo.md)**

:   提出利用热偏振（长波红外偏振）线索进行精细三维形状重建的方法，理论证明 LWIR 偏振观测不受光照环境和材质光学属性的影响，从而实现对透明、半透明和异质材料物体的高精度三维重建，显著优于可见光偏振方法。

**[Toward Material-Agnostic System Identification from Videos](others/toward_material-agnostic_system_identification_from_videos.md)**

:   提出 MASIV，首个无需预定义材质先验的视觉系统辨识框架：采用可学习的神经本构模型替代手工设计的弹性/塑性方程，通过重建连续体粒子轨迹提供时间密集的几何约束，从多视角视频中推断物体的内在动力学特性。

**[You Share Beliefs, I Adapt: Progressive Heterogeneous Collaborative Perception](others/you_share_beliefs_i_adapt_progressive_heterogeneous_collaborative_perception.md)**

:   提出PHCP框架，首次在推理阶段解决异构协同感知的域差距问题——通过agent的伪标签做few-shot无监督域适应，自训练适配器对齐特征空间，无需联合训练即在OPV2V上仅用少量无标注数据达到接近SOTA(HEAL)的性能。
