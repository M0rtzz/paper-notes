<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**📷 CVPR2026** · 共 **80** 篇

**[3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion](3m-ti_high-quality_mobile_thermal_imaging_via_calibration-free_multi-camera_cros.md)**

:   提出 3M-TI，一个**无需标定**的多相机跨模态扩散框架，通过在 VAE 潜空间中用跨模态自注意力（CSM）自动对齐并融合未标定的 RGB-热红外图像对，结合错位增强策略，在移动端热成像超分辨率任务上达到 SOTA，并显著提升下游目标检测与语义分割性能。

**[MEDISEG: 药物图像实例分割数据集——预防不良药物事件](a_dataset_of_medication_images_with_instance_segme.md)**

:   构建了MEDISEG药物图像实例分割数据集（8262张图像，32类药片，含遮挡/重叠的真实场景），用YOLOv8/v9验证在3类上达99.5% mAP@0.5、32类达80.1%，并通过FsDet few-shot协议证明MEDISEG预训练比CURE数据集在遮挡场景中显著提升未见药片类别的识别（1-shot准确率0.406 vs 0.131）。

**[MEDISEG: A Dataset of Medication Images with Instance Segmentation Masks for Preventing Adverse Drug Events](a_dataset_of_medication_images_with_instance_segmentation_masks_for_preventing_a.md)**

:   提出MEDISEG数据集——32种药片类型共8262张真实多药丸场景图像（含dosette box中重叠/遮挡/不同光照），提供实例分割标注，YOLOv8/v9在3-Pills子集mAP@50达99.5%、32-Pills达80.1%，few-shot实验证明MEDISEG作为base训练集显著优于CURE数据集。

**[A Mixed Diet Makes Dino An Omnivorous Vision Encoder](a_mixed_diet_makes_dino_an_omnivorous_vision_encoder.md)**

:   提出 Omnivorous Vision Encoder，通过轻量级 adapter 在冻结的 DINOv2 之上进行跨模态对齐蒸馏训练（RGB/Depth/Segmentation），使单一编码器对不同视觉模态产生一致嵌入，同时保留原始判别语义。

**[AFRO: Bootstrap Dynamic-Aware 3D Visual Representation for Scalable Robot Learning](bootstrap_dynamic-aware_3d_visual_representation_for_scalable_robot_learning.md)**

:   提出AFRO自监督3D视觉预训练框架，通过逆动力学模型（IDM）推断潜在动作、扩散Transformer前向动力学模型（FDM）预测未来特征、逆一致性约束保证时序对称性，在RH20T大规模数据上预训练后，MetaWorld 14任务平均成功率76.0%（vs DynaMo-3D 64.9%、PointMAE 63.9%），4个real-world任务也取得最优。

**[Brewing Stronger Features: Dual-Teacher Distillation for Multispectral Earth Observation](brewing_stronger_features_dual-teacher_distillation_for_multispectral_earth_obse.md)**

:   提出**DEO(Distillation for Earth Observation)**，一种双教师对比蒸馏框架——用多光谱自蒸馏教师学习光谱表示、用光学VFM教师（DINOv3）注入高级语义先验，使单一学生网络同时擅长光学和多光谱遥感任务，在语义分割、变化检测和分类上全面达到SOTA。

**[CA-LoRA: Concept-Aware LoRA for Domain-Aligned Segmentation Dataset Generation](ca-lora_concept-aware_lora_for_domain-aligned_segmentation_dataset_generation.md)**

:   提出Concept-Aware LoRA (CA-LoRA)，通过自动识别T2I模型中与特定概念（如视角、风格）相关的权重层，仅对这些层施加LoRA微调，实现对目标域的选择性对齐，同时保留预训练模型的多样化生成能力，用于生成高质量的城市场景分割数据集。

**[ClimaOoD: Improving Anomaly Segmentation via Physically Realistic Synthetic Data](climaood_improving_anomaly_segmentation_via_physically_realistic_synthetic_data.md)**

:   提出ClimaDrive数据生成框架和ClimaOoD基准数据集，通过语义引导的多天气场景生成+透视感知的异常物体放置，构建10K+训练集覆盖6种天气×93类异常，训练后四个SOTA方法平均AP提升3.25%。

**[Clip Is Shortsighted Paying Attention Beyond The First Sentence](clip_is_shortsighted_paying_attention_beyond_the_first_sentence.md)**

:   揭示 CLIP 系列模型对长文本中首句摘要和早期 token 的系统性偏差，提出 DeBias-CLIP 通过去除摘要句、句子子采样和 token 填充三种文本增强策略消除该偏差，在不引入额外参数的条件下实现长/短文本检索 SOTA。

**[CLIP Is Shortsighted: Paying Attention Beyond the First Sentence](clip_shortsighted_beyond_first_sentence.md)**

:   发现CLIP对长描述"只看第一句"的根本原因在于训练数据中长caption普遍以摘要句开头形成捷径，提出DeBias-CLIP通过去除摘要句+句子子采样+token填充来分散监督信号，实现长短文本检索双SOTA。

**[CLoE: Expert Consistency Learning for Missing Modality Segmentation](cloe_expert_consistency_learning_for_missing_modal.md)**

:   将缺失模态下的鲁棒性问题重新定义为决策级专家一致性控制，提出双分支一致性学习（全局MEC+区域REC），并通过轻量门网络将一致性分数转化为模态可靠性权重用于融合。

**[CLoE: Expert Consistency Learning for Missing Modality Segmentation](cloe_expert_consistency_learning_for_missing_modality_segmentation.md)**

:   提出 CLoE（Consistency Learning of Experts），将缺失模态鲁棒性问题建模为决策层面的专家一致性控制，通过模态专家一致性（MEC）和区域专家一致性（REC）双分支约束减少专家漂移，并用一致性分数驱动的门控网络实现可靠性加权融合。

**[Comparative Evaluation of Traditional Methods and Deep Learning for Brain Glioma Imaging. Review Paper](comparative_evaluation_of_traditional_methods_and.md)**

:   系统综述脑胶质瘤 MRI 分割与分类方法，比较传统方法（阈值、区域生长、聚类等）与深度学习方法（CNN 架构），结论是 CNN 在分割和分类任务上全面优于传统技术，但半自动方法因可控性更受放射科医生青睐。

**[Comparative Evaluation of Traditional Methods and Deep Learning for Brain Glioma Imaging](comparative_evaluation_of_traditional_methods_and_deep_learning_for_brain_glioma.md)**

:   一篇系统性综述论文，全面对比传统方法（阈值分割、区域生长、模糊聚类等）和深度学习方法（CNN、U-Net、SegNet 等）在脑胶质瘤 MRI 分割与分类任务上的表现，结论指出 CNN 架构在准确性和自动化程度上全面优于传统技术。

**[Concept-Guided Fine-Tuning Steering Vits Away From Spurious Correlations To Impr](concept-guided_fine-tuning_steering_vits_away_from_spurious_correlations_to_impr.md)**

:   提出 CFT（Concept-Guided Fine-Tuning），利用 LLM 生成类别级语义概念并通过 GroundedSAM 零样本分割获取概念掩码，再以 AttnLRP 的 relevance map 与概念区域对齐为目标微调 ViT，仅用 1500 张图即可显著提升 5 个 OOD 基准上的鲁棒性。

**[Conceptprism Concept Disentanglement In Personalized Diffusion Models Via Residu](conceptprism_concept_disentanglement_in_personalized_diffusion_models_via_residu.md)**

:   提出 ConceptPrism，通过引入图像级残余 token 和跨图像排斥损失，在个性化 T2I 扩散模型中自动将共享目标概念与图像特有的残余信息解耦，在 DreamBench 上 CLIP-T/DINO/CLIP-I 全面最优。

**[Crossearth-Sar A Sar-Centric And Billion-Scale Geospatial Foundation Model For D](crossearth-sar_a_sar-centric_and_billion-scale_geospatial_foundation_model_for_d.md)**

:   提出首个十亿参数级SAR视觉基础模型CrossEarth-SAR，通过物理引导的稀疏MoE架构结合SAR物理描述子，在22个跨域语义分割基准中的20个取得SOTA，部分multi-gap场景超越已有方法10%+ mIoU。

**[CrossEarth-SAR: A SAR-Centric and Billion-Scale Geospatial Foundation Model for Domain Generalizable Semantic Segmentation](crossearthsar_a_sarcentric_and_billionscale_geospa.md)**

:   提出首个十亿参数级 SAR 视觉基础模型 CrossEarth-SAR，在 DINOv2 基础上引入物理引导的稀疏 MoE 架构（用方向熵、等效视数、局部粗糙度三个 SAR 物理描述符引导路由），配套 200K 级预训练数据集和 22 个子基准，在 20/22 个跨域分割任务上达到 SOTA。

**[CTFS: Collaborative Teacher Framework for Forward-Looking Sonar Image Semantic Segmentation with Extremely Limited Labels](ctfs_collaborative_teacher_framework_for_forward-looking_sonar_image_semantic_se.md)**

:   提出CTFS，首个专为前视声呐图像设计的半监督语义分割框架，引入多教师协作机制（1个通用教师+2个声呐特异教师，分别模拟声学阴影和能量衰减物理特性），配合多视角伪标签可靠性评估（单教师内稳定性+跨教师间一致性），在仅2%标注下达62.32% mIoU，超越SOTA 5.08个百分点。

**[Data Warmup: Complexity-Aware Curricula for Efficient Diffusion Training](data_warmup_complexity-aware_curricula_for_efficient_diffusion_training.md)**

:   提出Data Warmup，一种不修改模型或损失函数的课程学习策略，通过语义感知图像复杂度度量（前景显著度×前景典型性）按从简到繁顺序调度训练图像，在ImageNet 256×256上为SiT系列带来IS最高+6.11、FID最低-3.41的改进，且反转课程（先难后简）反而低于均匀基线——证明排序本身是关键机制。

**[DeDelayed: Deleting Remote Inference Delay via On-Device Correction](dedelayed_deleting_remote_inference_delay_via_on-device_correction.md)**

:   提出 DeDelayed 端云协同推理框架，将轻量本地图像模型与延迟感知的云端时序预测视频模型结合，通过时序预测训练补偿网络延迟，在 100ms 延迟下比纯本地推理提升 6.4 mIoU、比纯远程推理提升 9.8 mIoU。

**[Detecting AI-Generated Forgeries via Iterative Manifold Deviation Amplification](detecting_ai-generated_forgeries_via_iterative_manifold_deviation_amplification.md)**

:   提出 IFA-Net，从"建模什么是真"而非"学什么是假"的角度检测 AI 伪造：利用冻结 MAE 重建输入产生残差暴露偏离自然图像流形的区域，再通过两阶段闭环——粗检测→任务自适应先验注入→放大残差→精细化——迭代放大流形偏差，在 diffusion inpainting 和传统篡改检测上均取得 SOTA。

**[Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](developing_foundation_models_for_universal_segment.md)**

:   构建迄今最大的全身 PET 分割数据集 PETWB-Seg11K（11041 例扫描、59831 个掩模），并提出 SegAnyPET 基础模型，实现基于 prompt 的 3D 全身 PET 通用可交互分割，在多中心、多示踪剂、多疾病场景下展现强 zero-shot 泛化能力。

**[Developing Foundation Models For Universal Segmentation From 3D Whole-Body Posit](developing_foundation_models_for_universal_segmentation_from_3d_whole-body_posit.md)**

:   构建迄今最大的全身 PET 分割数据集 PETWB-Seg11K（11,041 例 3D PET + 59,831 masks），并提出 SegAnyPET——首个面向功能性 PET 影像的 3D 可提示分割基础模型，在多中心、多示踪剂、多疾病场景下实现了强零样本泛化能力。

**[Direct Segmentation without Logits Optimization for Training-Free Open-Vocabulary Semantic Segmentation](direct_segmentation_without_logits_optimization_for_training-free_open-vocabular.md)**

:   提出一种跳过logits优化过程的开放词汇语义分割方法，基于"同类区域的logits到退化分布的分布差异一致"这一假设，直接通过最优传输路径或最大传输速度的解析解来构造分割图，在8个基准上达到SOTA且无需训练或模型特定调制。

**[DSS: Discover, Segment, and Select for Zero-shot Camouflaged Object Segmentation](discover_segment_and_select_a_progressive_mechanism_for_zero-shot_camouflaged_ob.md)**

:   提出DSS三阶段渐进式pipeline(Discover→Segment→Select)，通过自监督视觉编码器+Leiden聚类发现前景(FOD)、SAM生成候选mask、启发式评分+MLLM成对比较选择最优mask，实现零样本无训练的伪装目标分割，尤其在多实例场景上显著优于现有方法。

**[DPAD: Discriminative Perception via Anchored Description for Reasoning Segmentation](discriminative_perception_via_anchored_description_for_reasoning_segmentation.md)**

:   针对推理分割(RS)中RL+GRPO训练的geometric reward无法约束reasoning chain是否聚焦目标unique attributes的问题，提出DPAD方法：MLLM生成reasoning chain+geometric localization+anchored description，引入基于CLIP的Discriminative Perception Reward比较description与ROI/AOI的相似度差异，迫使caption更具判别性从而间接约束推理链聚焦目标，ReasonSeg上cIoU提升3.09%且推理链长度减少42%。

**[DSFlash: Comprehensive Panoptic Scene Graph Generation in Realtime](dsflash_comprehensive_panoptic_scene_graph_generation_in_realtime.md)**

:   提出 DSFlash，一个低延迟全景场景图生成模型，通过统一 backbone、双向关系预测和 mask 动态剪枝等设计，在 RTX 3090 上实现 56 FPS 的实时推理，同时保持 SOTA 性能（mR@50=30.9）。

**[DSFlash: Comprehensive Panoptic Scene Graph Generation in Realtime](dsflash_panoptic_scene_graph_realtime.md)**

:   DSFlash 通过合并分割与关系预测 backbone、双向关系预测头、动态 patch 剪枝等策略，将全景场景图生成速度提升至 RTX 3090 上 56 FPS，同时在 PSG 数据集上达到 mR@50=30.9 的 SOTA 性能。

**[DSS: Discover, Segment, and Select - A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation](dss_discover_segment_select_zero_shot_cos.md)**

:   提出三阶段零样本伪装目标分割框架DSS：先用DINOv2特征聚类+部件组合发现候选区域（Discover），再用SAM分割（Segment），最后用MLLM逐对比较选最优mask（Select），无需任何训练即在四个COD基准上全面超越先前零样本方法，尤其在多实例场景中优势显著。

**[Efficient RGB-D Scene Understanding via Multi-task Adaptive Learning and Cross-dimensional Feature Guidance](efficient_rgb-d_scene_understanding_via_multi-task_adaptive_learning_and_cross-d.md)**

:   提出一种高效 RGB-D 多任务场景理解网络，通过改进的融合编码器利用通道冗余加速特征提取，设计归一化聚焦通道层（NFCL）和上下文特征交互层（CFIL）进行跨维度特征引导，并引入批级别多任务自适应损失函数动态调整各任务学习权重，在 NYUv2/SUN RGB-D/Cityscapes 上同时完成语义分割、实例分割、朝向估计、全景分割和场景分类五项任务，取得精度与速度的双重优势。

**[Efficient RGB-D Scene Understanding via Multi-task Adaptive Learning and Cross-dimensional Feature Guidance](efficient_rgbd_scene_understanding_via_multitask_a.md)**

:   提出一种高效 RGB-D 多任务场景理解网络，通过部分通道卷积融合编码器、归一化焦点通道层(NFCL)、上下文特征交互层(CFIL)和多任务自适应损失，在 NYUv2 上以 20+ FPS 同时完成语义/实例/全景分割、方向估计和场景分类。

**[ELVIS: Enhance Low-Light for Video Instance Segmentation in the Dark](elvis_enhance_low-light_for_video_instance_segmentation_in_the_dark.md)**

:   ELVIS 提出了首个低光视频实例分割（VIS）框架，通过物理驱动的合成低光视频管线（含运动模糊建模）、无标定退化参数估计网络 VDP-Net、以及将增强解码器集成到 VIS 架构中实现退化与内容解耦，在合成和真实低光视频上分别实现 +3.7AP 和 +2.8AP 的提升。

**[EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection](erecu_pseudo-label_evolution_fusion_and_refinement_with_multi-cue_learning_for_u.md)**

:   提出统一的无监督伪装目标检测框架 EReCu，通过多线索原生感知(MNP)、伪标签进化融合(PEF)和局部伪标签精炼(LPR)三个协同模块，在不依赖人工标注的情况下实现了边界精确、细节丰富的伪装目标分割。

**[EReCu: Pseudo-label Evolution Fusion and Refinement with Multi-Cue Learning for Unsupervised Camouflage Detection](erecu_pseudolabel_evolution_unsupervised_camouflage.md)**

:   提出EReCu框架，在DINO师生架构上通过多线索原生感知(MNP)提取纹理+语义先验来引导伪标签进化融合(PEF)和局部伪标签精修(LPR)，实现无标注下的伪装目标检测，在4个COD数据集上达到UCOD SOTA。

**[FCL-COD: Weakly Supervised Camouflaged Object Detection with Frequency-aware and Contrastive Learning](fcl-cod_weakly_supervised_camouflaged_object_detection_with_frequency-aware_and_.md)**

:   提出 FCL-COD 框架，通过频率感知低秩适配（FoRA）将伪装场景知识注入 SAM、梯度感知对比学习（GCL）增强前背景特征分离、多尺度频率注意力（MSFA）提炼边界敏感特征，在仅使用边界框标注的弱监督设定下超越了全监督 SOTA 方法。

**[Follow the Saliency: Supervised Saliency for Retrieval-augmented Dense Video Captioning](follow_the_saliency_supervised_saliency_for_retrieval-augmented_dense_video_capt.md)**

:   提出 STaRC 框架，通过有监督的帧级显著性学习统一驱动检索（显著性引导分割+检索）和描述生成（显著性提示注入解码器），显著提升密集视频描述(DVC)任务中的时序对齐和字幕质量。

**[FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting](fov-net_rotation-invariant_cad_b-rep_learning_via_field-of-view_ray_casting.md)**

:   提出 FoV-Net，首个在 CAD B-rep 学习中同时捕获局部表面几何和全局结构上下文的旋转不变框架，通过局部参考系 UV 网格(LRF UV)和视场光线投射(FoV)描述子实现了在任意 $\mathbf{SO}(3)$ 旋转下的鲁棒分类和分割。

**[A2P: From 2D Alignment to 3D Plausibility for Occlusion-Robust Two-Hand Reconstruction](from_2d_alignment_to_3d_plausibility_unifying_hete.md)**

:   解耦双手重建为2D结构对齐+3D空间交互对齐：Stage 1用Fusion Alignment Encoder隐式蒸馏Sapiens的关键点/分割/深度三种2D先验(推理时免基础模型)，Stage 2用穿透感知扩散模型+碰撞梯度引导将穿透姿态映射到物理合理配置——InterHand2.6M上MPJPE降至5.36mm(超SOTA 4DHands 2.13mm)，穿透体积降7倍。

**[From 2D Alignment to 3D Plausibility: Unifying Heterogeneous 2D Priors and Penetration-Free Diffusion for Occlusion-Robust Two-Hand Reconstruction](from_2d_alignment_to_3d_plausibility_unifying_heterogeneous_2d_priors_and_penetr.md)**

:   将双手重建解耦为 2D 结构对齐（融合关键点/分割/深度先验）和 3D 空间交互对齐（穿透消除扩散模型），在 InterHand2.6M 上 MPJPE 达到 5.36mm，大幅超越 SOTA。

**[Generalizable Knowledge Distillation from Vision Foundation Models for Semantic Segmentation](generalizable_knowledge_distillation_from_vision_foundation_models_for_semantic_.md)**

:   提出 Generalizable Knowledge Distillation (GKD)，通过解耦表示学习与任务学习的多阶段蒸馏，以及基于 query 的软蒸馏机制，将 VFM 的跨域泛化能力有效转移到轻量学生模型，F2L 设置下平均提升 +10.6% mIoU。

**[GKD: Generalizable Knowledge Distillation from Vision Foundation Models for Semantic Segmentation](gkd_generalizable_knowledge_distillation_vfm.md)**

:   提出GKD框架，通过将表示学习与任务学习解耦的多阶段蒸馏策略和查询式软蒸馏机制，从VFM（如DINOv2）中蒸馏出具有跨域泛化能力的轻量学生模型，在F2L设置下平均mIoU提升+10.6%，F2F设置下+1.9%。

**[I'm a Map! Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers](interpretable_motion-attentive_maps_spatio-temporally_localizing_concepts_in_vid.md)**

:   提出 GramCol 和 IMAP 两种无需训练/梯度的方法，利用 Video DiT 内部特征为任意文本概念（尤其是运动概念）生成可解释的时空显著性图，并在运动定位和零样本视频语义分割上取得 SOTA。

**[Learning Cross-View Object Correspondence via Cycle-Consistent Mask Prediction](learning_cross-view_object_correspondence_via_cycle-consistent_mask_prediction.md)**

:   提出基于条件二值分割的跨视角物体对应框架 CCMP，通过循环一致性约束提供自监督信号并支持测试时训练 (TTT)，在 Ego-Exo4D 上达到 44.57% mIoU 的 SOTA 性能。

**[Making Training-Free Diffusion Segmentors Scale with the Generative Power](making_training-free_diffusion_segmentors_scale_with_the_generative_power.md)**

:   揭示现有无训练扩散分割方法无法随生成模型能力增强而提升的根本原因——交叉注意力图到语义相关性之间存在两个gap（聚合gap和分数不平衡gap），提出自动聚合（auto aggregation）和逐像素重缩放（per-pixel rescaling）两项技术组成GoCA框架，首次使更强的扩散模型（SDXL、PixArt-Sigma、Flux）在无训练语义分割中显著超越旧模型。

**[Masked Representation Modeling for Domain-Adaptive Segmentation](masked_representation_modeling_for_domain-adaptive_segmentation.md)**

:   提出 Masked Representation Modeling (MRM)，在潜在空间而非像素空间进行掩码与重建，作为 UDA 分割的即插即用辅助任务，在 GTA→Cityscapes 上平均为 4 种 baseline 带来 +2.3 mIoU 提升。

**[Matanyone 2 Scaling Video Matting Via A Learned Quality Evaluator](matanyone_2_scaling_video_matting_via_a_learned_quality_evaluator.md)**

:   提出学习型 Matting Quality Evaluator (MQE)，在无 ground-truth 条件下逐像素评估 alpha 质量，既作为在线训练引导又作为离线数据筛选器，构建了 28K 片段 / 240 万帧的真实世界视频抠图数据集 VMReal，配合参考帧训练策略，显著超越所有现有方法。

**[A Mixed Diet Makes DINO An Omnivorous Vision Encoder](mixed_diet_dino_omnivorous_encoder.md)**

:   发现DINOv2的特征在不同模态间几乎零对齐（同一场景RGB和深度图的特征相似度≈随机图像对），提出Omnivorous Vision Encoder通过跨模态对齐+冻结教师蒸馏的双目标训练，让单一编码器产出模态无关的统一特征空间。

**[MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention](mixercseg_an_efficient_mixer_architecture_for_crack_segmentation_via_decoupled_m.md)**

:   提出 MixerCSeg，通过解析 Mamba 的隐式注意力机制将通道解耦为全局/局部分支，分别用 Self-Attention 和 CNN 增强，配合方向引导边缘门控卷积，以 2.05 GFLOPs / 2.54M 参数实现裂缝分割 SOTA。

**[Masked Representation Modeling for Domain-Adaptive Segmentation](mrm_masked_representation_modeling_domain_adaptive.md)**

:   提出在潜在空间而非输入空间做掩码建模的辅助任务MRM，通过轻量级Rebuilder模块对编码器特征做掩码-重建并用分割损失监督，在GTA→Cityscapes上为四种UDA基线平均带来+2.3 mIoU提升，推理时零额外开销。

**[Open-Vocabulary Domain Generalization in Urban-Scene Segmentation](open-vocabulary_domain_generalization_in_urban-scene_segmentation.md)**

:   提出 OVDG-SS 新设定，统一处理语义分割中的未见域和未见类别问题，并设计基于状态空间模型的 S2-Corr 模块来修复域偏移导致的文本-图像相关性退化，在自动驾驶场景中实现高效且鲁棒的跨域开放词汇分割。

**[Pointer-Cad Unifying B-Rep And Command Sequences Via Pointer-Based Edges Faces S](pointer-cad_unifying_b-rep_and_command_sequences_via_pointer-based_edges_faces_s.md)**

:   提出基于指针 (Pointer) 机制的命令序列表示，将 B-Rep 几何实体（边/面）显式引入自回归 CAD 生成，首次在命令序列方法中支持 chamfer/fillet 操作，同时大幅降低量化误差导致的拓扑错误。

**[Prompt-Driven Lightweight Foundation Model for Instance Segmentation-Based Fault Detection in Freight Trains](prompt-driven_lightweight_foundation_model_for_instance_segmentation-based_fault.md)**

:   提出 SAM FTI-FDet，通过自动提示生成模块和自适应特征调度器将 SAM 的通用分割能力迁移至货运列车故障检测领域，以 TinyViT 轻量骨干实现 74.6 AP^box / 74.2 AP^mask，在精度和效率上均超越现有方法。

**[Prompt-Driven Lightweight Foundation Model for Instance Segmentation-Based Fault Detection in Freight Trains](promptdriven_lightweight_foundation_model_for_inst.md)**

:   提出SAM FTI-FDet，通过设计一个基于Transformer decoder的自提示生成器（Prompt Generator），让轻量化的TinyViT-SAM自动生成任务相关的query prompt，无需人工交互即可完成货运列车部件的实例级故障检测，在自建数据集上达到74.6 AP_box / 74.2 AP_mask。

**[Rdnet Region Proportion-Aware Dynamic Adaptive Salient Object Detection Network ](rdnet_region_proportion-aware_dynamic_adaptive_salient_object_detection_network_.md)**

:   针对遥感图像中目标尺度变化大的难题，提出区域比例感知的动态自适应显著性目标检测网络 RDNet，通过 Proportion Guidance 动态选择不同大小卷积核组合，结合小波频域交互与交叉注意力定位模块，在三个 ORSI-SOD 数据集上全面超越 SOTA。

**[RDNet: Region Proportion-Aware Dynamic Adaptive Salient Object Detection Network in Optical Remote Sensing Images](rdnet_region_proportionaware_dynamic_adaptive_sali.md)**

:   提出RDNet，通过区域比例感知机制动态选择不同大小卷积核组合，结合小波域频率匹配上下文增强和跨注意力定位模块，在遥感图像显著性检测三个数据集上全面超越SOTA。

**[Realvlg-R1 A Large-Scale Real-World Visual-Language Grounding Benchmark For Robo](realvlg-r1_a_large-scale_real-world_visual-language_grounding_benchmark_for_robo.md)**

:   提出 RealVLG 框架，包含 11B 级真实世界多粒度标注数据集 RealVLG-11B 和基于强化学习微调的统一模型 RealVLG-R1，首次将视觉语言定位（VLG）与机器人抓取统一到同一范式中，实现从自然语言指令到 bounding box、分割掩码、抓取姿态和接触点的端到端预测，并展现出零样本泛化能力。

**[Reasoning with Pixel-level Precision: QVLM Architecture and SQuID Dataset for Quantitative Geospatial Analytics](reasoning_with_pixel-level_precision_qvlm_architecture_and_squid_dataset_for_qua.md)**

:   提出 QVLM 架构和 SQuID 数据集，通过代码生成+分割模型的解耦设计，在卫星图像上实现像素级精度的定量空间推理，克服了传统 VLM 因 patch embedding 压缩而丢失空间索引的根本限制。

**[REL-SF4PASS: Panoramic Semantic Segmentation with REL Depth Representation and Spherical Fusion](rel-sf4pass_panoramic_semantic_segmentation_with_rel_depth_representation_and_sp.md)**

:   提出 REL 深度表示（基于柱面坐标系的 Rectified Depth + EGVIA + LOA 三通道）和球面动态多模态融合（SMMF），用于全景语义分割，在 Stanford2D3D 上实现 63.06% 平均 mIoU（比 HHA 基线提升 2.35%），并将面对 3D 扰动时的性能方差降低约 70%。

**[Rewis3D Reconstruction Improves Weakly-Supervised Semantic Segmentation](rewis3d_reconstruction_improves_weakly-supervised_semantic_segmentation.md)**

:   Rewis3d 利用前馈式多视图3D重建生成的点云作为辅助监督信号，通过双师生架构实现2D图像与3D点云之间的双向跨模态一致性学习，在稀疏标注（点/涂鸦/粗标注）下将弱监督语义分割性能提升2-7% mIoU，推理时仅需2D图像。

**[Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation](rewis3d_reconstruction_improves_weaklysupervised_s.md)**

:   首次将前馈3D重建(MapAnything)的几何信息作为辅助监督信号引入弱监督2D语义分割，通过双Student-Teacher架构和置信度加权的跨模态一致性损失，在4个数据集上以2-7% mIoU大幅超越SOTA——且推理时仅需2D模型。

**[Rsonet Region-Guided Selective Optimization Network For Rgb-T Salient Object Det](rsonet_region-guided_selective_optimization_network_for_rgb-t_salient_object_det.md)**

:   提出两阶段 RGB-T 显著性检测网络 RSONet：先通过区域引导阶段计算 RGB/热红外引导图与联合引导图的相似度，选出更可靠的模态；再在显著性生成阶段利用选择性优化融合双模态特征，配合密集细节增强和互信息语义模块生成高质量显著图，在三个 RGB-T 基准上取得 SOTA 性能。

**[RSONet: Region-guided Selective Optimization Network for RGB-T Salient Object Detection](rsonet_regionguided_selective_optimization_network.md)**

:   提出RSONet两阶段RGB-T显著性检测框架：先通过三分支并行编码器生成区域引导图并基于相似度比较选择主导模态，再通过选择性优化模块融合双模态特征，在VT5000/VT1000/VT821上MAE达0.020/0.014/0.021，超越27个SOTA方法。

**[SAP: Segment Any 4K Panorama](sap_segment_any_4k_panorama.md)**

:   将全景分割重构为拓扑-记忆对齐问题，通过列优先锯齿扫描将ERP全景图转为透视伪视频序列，完美复用SAM2的流式记忆机制，在零样本4K全景分割上比vanilla SAM2平均提升+17.2 mIoU。

**[Sarmae Masked Autoencoder For Sar Representation Learning](sarmae_masked_autoencoder_for_sar_representation_learning.md)**

:   提出 SARMAE 框架，通过百万级 SAR 数据集 SAR-1M、散斑感知表征增强 (SARE) 和光学语义锚约束 (SARC)，实现噪声鲁棒的 SAR 自监督预训练，在分类、检测和分割多个下游任务上取得 SOTA。

**[Seeing Beyond: Extrapolative Domain Adaptive Panoramic Segmentation](seeing_beyond_extrapolative_domain_adaptive_panoramic_segmentation.md)**

:   提出 EDA-PSeg 框架，通过图匹配适配器（GMA）和欧拉-边际注意力（EMA）两个核心模块，首次实现从针孔视图到 360° 全景图像的开放集无监督域自适应语义分割，同时处理几何视场角畸变和未知类别发现。

**[SemiTooth: a Generalizable Semi-supervised Framework for Multi-Source Tooth Segmentation](semitooth_a_generalizable_semi-supervised_framework_for_multi-source_tooth_segme.md)**

:   提出 SemiTooth 框架，通过多教师多学生架构和严格加权置信度约束（SWC），解决多源 CBCT 牙齿分割中的标注稀缺和跨源域间差异问题，同时构建了首个多源半监督牙齿数据集 MS3Toothset。

**[SemiTooth: a Generalizable Semi-supervised Framework for Multi-Source Tooth Segmentation](semitooth_a_generalizable_semisupervised_framework.md)**

:   提出SemiTooth——多教师多学生半监督框架+更严格加权置信度约束(SWC)，用于多源CBCT牙齿分割，在新构建的MS3Toothset上mIoU达76.67%、Dice 85.69%，超越SOTA CMT(76.14%)。

**[SGMA: Semantic-Guided Modality-Aware Segmentation for Remote Sensing with Incomplete Multimodal Data](sgma_semantic-guided_modality-aware_segmentation_for_remote_sensing_with_incompl.md)**

:   提出 SGMA 框架，通过语义引导融合（SGF）模块构建全局语义原型实现自适应跨模态融合，并通过模态感知采样（MAS）模块动态提升脆弱模态的训练频率，解决遥感场景下不完整多模态语义分割中的模态不平衡、类内方差大和跨模态异质性三大挑战。

**[SGMA: Semantic-Guided Modality-Aware Segmentation for Remote Sensing with Incomplete Multimodal Data](sgma_semanticguided_modalityaware_segmentation_for.md)**

:   提出SGMA——语义引导模态感知分割框架，通过语义引导融合(SGF)降低类内变异和协调跨模态冲突，模态感知采样(MAS)平衡脆弱模态训练，在ISPRS上Average mIoU +9.20%且弱模态Last-1 mIoU +18.26%(vs SOTA IMLT)。

**[SPARROW: Learning Spatial Precision and Temporal Referential Consistency in Pixel-Grounded Video MLLMs](sparrow_learning_spatial_precision_and_temporal_re.md)**

:   SPARROW通过目标特定跟踪特征(TSF)和双提示[BOX]+[SEG]定位机制增强视频MLLM的时空一致性，在MeViS上J&F +8.9、VidSTG上mIoU +5.49，可即插即用到三种backbone上。

**[SPARROW: Learning Spatial Precision and Temporal Referential Consistency in Pixel-Grounded Video MLLMs](sparrow_learning_spatial_precision_and_temporal_referential_consistency_in_pixel.md)**

:   提出 SPARROW 框架，通过 **目标特定追踪特征（TSF）** 注入时间一致性监督、**双提示（[BOX]+[SEG]）粗到细解码** 稳定首帧初始化，以即插即用方式集成到现有视频 MLLM 上，在 6 个基准 3 个任务上取得一致提升。

**[Spatio-Semantic Expert Routing Architecture with Mixture-of-Experts for Referring Image Segmentation](spatio-semantic_expert_routing_architecture_with_mixture-of-experts_for_referrin.md)**

:   提出 SERA 框架，在冻结的视觉-语言骨干网络中引入两阶段轻量级 MoE 专家精炼（骨干级 SERA-Adapter + 融合级 SERA-Fusion），通过表达式引导的自适应路由实现参考图像分割中的空间一致性和边界精度提升，仅更新不到 1% 的骨干参数。

**[Towards High-Quality Image Segmentation Improving Topology Accuracy By Penalizin](towards_high-quality_image_segmentation_improving_topology_accuracy_by_penalizin.md)**

:   提出 Same Class Neighbor Penalization (SCNP)，通过在训练时将每个像素的 logit 替换为其同类邻域中最差预测，迫使模型优先修复邻域中的弱分类像素，从而以极低代价（仅 3 行代码、几毫秒/迭代）显著提升分割的拓扑精度。

**[Transformer-Based Multi-Region Segmentation And Radiomic Analysis Of Hr-Pqct Ima](transformer-based_multi-region_segmentation_and_radiomic_analysis_of_hr-pqct_ima.md)**

:   提出基于 SegFormer 的全自动多区域 HR-pQCT 分割框架，结合影像组学特征与机器学习实现骨质疏松二分类，发现软组织（肌腱/脂肪）特征的诊断价值优于传统骨骼特征。

**[Uncertainty-Aware Concept and Motion Segmentation for Semi-Supervised Angiography Videos](uncertainty-aware_concept_and_motion_segmentation_for_semi-supervised_angiograph.md)**

:   提出 SMART 框架，基于 SAM3 的概念提示分割构建 Teacher-Student 半监督模型，结合渐进置信度正则化和双流时序一致性策略，仅用极少标注在 X 射线冠脉造影视频中实现 SOTA 血管分割。

**[Universal 3D Shape Matching via Coarse-to-Fine Language Guidance](universal_3d_shape_matching_via_coarse-to-fine_language_guidance.md)**

:   提出 UniMatch，一个语义感知的粗到细 3D 形状匹配框架：粗阶段通过类别无关 3D 分割 + MLLM 命名 + FG-CLIP 语言嵌入建立部件级对应；细阶段通过组级排序对比损失(Group-wise RnC Loss)在扩展的函数映射框架中学习稠密对应，实现跨类别、非等距形状的通用匹配。

**[UnrealPose: Leveraging Game Engine Kinematics for Large-Scale Synthetic Human Pose Data](unrealpose_leveraging_game_engine_kinematics_for_large-scale_synthetic_human_pos.md)**

:   提出 UnrealPose-Gen，一个基于 Unreal Engine 5 的合成人体姿态数据生成管线，利用游戏引擎原生骨骼运动学（而非 SMPL）生成百万级标注数据集 UnrealPose-1M，提供 3D 关节、2D 关键点、遮挡标志、实例分割掩码和相机参数等完整标注。

**[VidEoMT: Your ViT is Secretly Also a Video Segmentation Model](videomt_encoder_only_video_segmentation.md)**

:   提出encoder-only视频分割模型VidEoMT，通过查询传播和查询融合将分割与时序关联统一在单个ViT编码器中，消除所有专用追踪模块，在YouTube-VIS 2019上达到160 FPS（比CAVIS快10×+），同时AP仅差0.3。

**[Videomt Your Vit Is Secretly Also A Video Segmentation Model](videomt_your_vit_is_secretly_also_a_video_segmentation_model.md)**

:   提出 VidEoMT，一种纯编码器（encoder-only）视频分割架构，通过 query propagation 和 query fusion 将分割与时序关联统一在单个 ViT 编码器中，在保持与 SOTA 可比精度的同时实现 5×–10× 加速（ViT-L 达 160 FPS）。
