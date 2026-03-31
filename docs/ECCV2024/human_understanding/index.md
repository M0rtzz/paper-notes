<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🎞️ ECCV2024** · 共 **19** 篇

**[3D Hand Pose Estimation in Everyday Egocentric Images](3d_hand_pose_estimation_in_everyday_egocentric_images.md)**

:   通过系统研究裁剪输入、相机内参感知位置编码(KPE)、辅助监督(手部分割+抓握标签)和多数据集联合训练这四个实践，提出WildHands系统，在仅用ResNet50和少量数据的条件下，实现了对野外第一人称图像中3D手部姿态的鲁棒估计，零样本泛化超过FrankMocap全部指标且与10倍大的HaMeR竞争。

**[3DGazeNet: Generalizing 3D Gaze Estimation with Weak-Supervision from Synthetic Views](3dgazenet_generalizing_3d_gaze_estimation_with_weak-supervision_from_synthetic_v.md)**

:   提出将视线估计重新表述为密集3D眼球网格回归，并通过从大规模野外人脸图像中自动提取伪标签+HeadGAN合成多视图进行弱监督训练，在跨域场景下比SOTA提升最多30%。

**[A Probability-guided Sampler for Neural Implicit Surface Rendering](a_probabilityguided_sampler_for_neural_implicit_surface_rend.md)**

:   提出一种概率引导的光线采样器（Probability-guided Sampler），在3D图像投影空间中建模概率密度函数来指导光线采样朝向感兴趣区域，同时设计了包含近表面和空白空间两个分量的新型表面重建损失，可作为插件集成到现有神经隐式表面渲染器中，显著提升重建精度和渲染质量。

**[A Simple Baseline for Spoken Language to Sign Language Translation with 3D Avatars](a_simple_baseline_for_spoken_language_to_sign_language_trans.md)**

:   提出首个基于3D Avatar输出的Spoken2Sign翻译基线系统，通过三步流程（字典构建→SMPLSign-X 3D手语估计→检索-连接-渲染翻译）将口语文本翻译为3D手语动画，在Phoenix-2014T上back-translation BLEU-4达25.46，同时其3D手语副产品（关键点增强和多视角理解）显著提升了手语理解任务性能。

**[AdaDistill: Adaptive Knowledge Distillation for Deep Face Recognition](adadistill_adaptive_knowledge_distillation_for_deep_face_rec.md)**

:   提出AdaDistill，将知识蒸馏概念嵌入margin penalty softmax loss中，通过基于EMA的自适应类中心（早期用sample-sample简单知识、后期用sample-center复杂知识）和困难样本感知机制，无需额外超参数即可提升轻量级人脸识别模型的判别能力，在IJB-B/C和ICCV21-MFR等挑战性基准上超越SOTA蒸馏方法。

**[ADen: Adaptive Density Representations for Sparse-view Camera Pose Estimation](aden_adaptive_density_representations_for_sparseview_camera.md)**

:   ADen提出生成器-判别器框架统一位姿回归和概率位姿估计：生成器输出多个6DoF位姿假设来建模多模态分布（处理对称歧义），判别器选出最佳假设，在稀疏视角位姿估计上同时实现了更高精度和更低运行时间。

**[Alignist: CAD-Informed Orientation Distribution Estimation by Fusing Shape and Correspondences](alignist_cad-informed_orientation_distribution_estimation_by_fusing_shape_and_co.md)**

:   提出 Alignist，首个利用 CAD 模型信息（SDF + SurfEmb 对应特征）训练隐式分布网络来推断 SO(3) 上姿态分布的方法，通过 product of experts 融合几何和特征对齐，在低数据场景下显著优于对比学习方法。

**[Audio-Driven Talking Face Generation with Stabilized Synchronization Loss](audio-driven_talking_face_generation_with_stabilized_synchronization_loss.md)**

:   提出 AVSyncNet、stabilized synchronization loss 和 silent-lip generator 三项改进，系统性地解决音频驱动说话人脸生成中 SyncNet 不稳定和嘴唇泄漏两大核心问题，在唇形同步和视觉质量上均达到 SOTA。

**[Bi-TTA: Bidirectional Test-Time Adapter for Remote Physiological Measurement](bi-tta_bidirectional_test-time_adapter_for_remote_physiological_measurement.md)**

:   提出 Bi-TTA 框架，首次将 Test-Time Adaptation 引入远程光电容积脉搏波 (rPPG) 任务，通过时空一致性自监督先验和前瞻-回溯双向适应策略，在推理时仅用无标注单实例数据即可完成模型域适应。

**[Combining Generative And Geometry Priors For Wide-Angle Portrait Correction](combining_generative_and_geometry_priors_for_wide-angle_portrait_correction.md)**

:   提出结合 StyleGAN 生成式先验（用于人脸矫正）和几何对称先验（用于背景直线矫正）的双模块框架，大幅提升广角人像畸变校正的视觉质量和定量指标。

**[CoMo: Controllable Motion Generation Through Language Guided Pose Code Editing](como_controllable_motion_generation_through_language_guided_pose_code_editing.md)**

:   提出 CoMo，通过将动作序列分解为语义明确的 pose code（如"左膝微弯"），实现基于文本的可控动作生成与基于 LLM 的零样本动作编辑。

**[Decomposed Vector-Quantized Variational Autoencoder for Human Grasp Generation](decomposed_vector-quantized_variational_autoencoder_for_human_grasp_generation.md)**

:   提出 Decomposed VQ-VAE (DVQ-VAE)，通过将手部分解为六个部分分别编码到独立码本，并设计双阶段解码策略（先姿态后位置），在四个基准数据集上质量指标相对提升约14.1%。

**[Domain Reduction Strategy for Non-Line-of-Sight Imaging](domain_reduction_strategy_for_non-line-of-sight_imaging.md)**

:   提出一种面向非视线成像（NLOS）的优化方法，通过将瞬态信号建模为逐点光传播函数的叠加，并设计由粗到细的域缩减策略剪除空白区域，在通用NLOS场景下实现约20倍加速且同时重建反射率和表面法线。

**[EgoExo-Fitness: Towards Egocentric and Exocentric Full-Body Action Understanding](egoexo-fitness_towards_egocentric_and_exocentric_full-body_action_understanding.md)**

:   提出 EgoExo-Fitness 数据集，包含同步的第一人称和第三人称健身视频，提供两级时间边界标注和创新性的可解释动作评判标注（技术关键点验证、自然语言评论、质量评分），并构建五个基准任务。

**[EvSign: Sign Language Recognition and Translation with Streaming Events](evsign_sign_language_recognition_and_translation_with_streaming_events.md)**

:   首次构建面向连续手语识别（CSLR）和手语翻译（SLT）任务的事件相机基准数据集 EvSign，并提出基于稀疏Transformer的高效框架，在仅0.34% FLOPs和44.2%参数量下达到与SOTA RGB方法可比或更优的性能。

**[Large Motion Model for Unified Multi-Modal Motion Generation](large_motion_model_for_unified_multimodal_motion_generation.md)**

:   LMM是首个多模态通用人体动作生成模型，统一了文本/动作/音乐/语音等10种任务、16个数据集（320K序列/1亿帧），通过身体部位感知的ArtAttention机制和可变帧率+随机遮掩的预训练策略，在多个标准benchmark上与专家模型竞争甚至超越。

**[QUAR-VLA: Vision-Language-Action Model for Quadruped Robots](quarvla_visionlanguageaction_model_for_quadruped_robots.md)**

:   提出 QUAR-VLA 范式，首次将视觉、语言指令和动作生成统一到四足机器人中，构建了大规模多任务数据集 QUARD（259K episodes），训练 QUART 模型（基于 8B VLM）实现感知、导航、全身操控等多种任务，并展示了从仿真到真实的迁移能力。

**[Self-supervised Feature Adaptation for 3D Industrial Anomaly Detection](selfsupervised_feature_adaptation_for_3d_industrial_ano.md)**

:   提出 LSFA（Local-to-global Self-supervised Feature Adaptation），通过模态内特征紧致化（IFC）和跨模态局部到全局一致性对齐（CLC）微调适配器，学习面向异常检测的任务导向表示，在 MVTec-3D AD 上达到 97.1% I-AUROC（+3.4%）。

**[WordRobe: Text-Guided Generation of Textured 3D Garments](wordrobe_textguided_generation_of_textured_3d_garments.md)**

:   提出 WordRobe 框架，通过学习 3D 服装潜在空间并与 CLIP 嵌入对齐，实现文本驱动的带纹理 3D 服装网格生成，并利用 ControlNet 的单步前向推理实现高效视角一致的纹理合成。
