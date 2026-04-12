---
title: >-
  CVPR2026 医学图像方向 130篇论文解读
description: >-
  130篇CVPR2026 医学图像方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**📷 CVPR2026** · 共 **130** 篇

**[A Protocol For Evaluating Robustness To He Stainin](a_protocol_for_evaluating_robustness_to_he_stainin.md)**

:   提出三步评估协议（选参考染色条件→表征测试集染色属性→模拟染色条件推理），系统量化306个MSI分类模型对H&E染色差异的鲁棒性，发现鲁棒性与分类性能呈弱负相关(r=-0.28)，高性能不代表高鲁棒性。

**[A Semi-Supervised Framework For Breast Ultrasound Segmentation With Training-Fre](a_semi-supervised_framework_for_breast_ultrasound_segmentation_with_training-fre.md)**

:   提出面向乳腺超声（BUS）图像分割的半监督框架，利用 GPT-5 生成外观描述 + Grounding DINO + SAM 免训练生成伪标签（APPG），结合双教师框架（静态+动态）通过不确定性-熵加权融合（UEWF）和自适应不确定性引导反向对比学习（AURCL）精炼标签，仅用 2.5% 标注即接近全监督性能。

**[A Semisupervised Framework For Breast Ultrasound S](a_semisupervised_framework_for_breast_ultrasound_s.md)**

:   通过外观描述驱动VLM免训练生成伪标签，再由双教师不确定性融合+反向对比学习细化，仅2.5%标注即可逼近全监督性能。

**[Accelerating Stroke Mri With Diffusion Probabilist](accelerating_stroke_mri_with_diffusion_probabilist.md)**

:   借鉴基础模型范式，先在约4000例fastMRI多对比度脑MRI上预训练扩散模型，再用20例目标域数据微调，实现临床中风MRI的高质量加速重建，盲审读片证明2×加速下非劣于标准诊疗。

**[Accelerating Stroke Mri With Diffusion Probabilistic Models Through Large-Scale ](accelerating_stroke_mri_with_diffusion_probabilistic_models_through_large-scale_.md)**

:   借鉴基础模型的"预训练+微调"范式，在 ~4000 名 fastMRI 受试者（多对比度）上大规模预训练扩散概率模型（DPM），然后用极少目标域数据（20名受试者）低学习率微调，实现跨对比度、跨采集协议的 MRI 加速重建；临床中风验证中 2× 加速图像质量经神经放射科医生盲法评估 non-inferior 于标准全采样图像。

**[Act Like A Pathologist Tissue-Aware Whole Slide Image Reasoning](act_like_a_pathologist_tissue-aware_whole_slide_image_reasoning.md)**

:   提出 HistoSelect 框架，模拟病理学家从粗到细的推理过程，通过组织分割→Group Sampler→Patch Selector 的三级筛选机制，基于信息瓶颈(IB)理论压缩无关视觉token，在减少约70%计算量的同时实现三个数据集上的SOTA。

**[Active Inference For Micro-Gesture Recognition Efe-Guided Temporal Sampling And ](active_inference_for_micro-gesture_recognition_efe-guided_temporal_sampling_and_.md)**

:   提出 UAAI 框架，首次将主动推理(Active Inference)引入微手势识别，通过 EFE 引导的时间帧选择 + 空间注意力 + UMIX不确定性感知增强，在SMG数据集RGB模态上达到63.47%，大幅超越传统RGB方法。

**[Adaptation Of Weakly Supervised Localization In Hi](adaptation_of_weakly_supervised_localization_in_hi.md)**

:   提出SFDA-DeP方法，受机器遗忘启发，将源自由域适应建模为迭代识别过度预测类的不确定样本并选择性降低其置信度的过程，同时联合训练像素级分类器恢复定位判别力，在跨器官/跨中心病理基准上显著优于SFDA baselines。

**[Adaptation Of Weakly Supervised Localization In Histopathology By Debiasing Pred](adaptation_of_weakly_supervised_localization_in_histopathology_by_debiasing_pred.md)**

:   提出 SFDA-DeP，受机器遗忘启发，将 SFDA 重新定义为"识别并纠正预测偏差"的迭代过程：对 dominant class 中高熵不确定样本执行"遗忘"操作迫使模型放弃偏向性预测，对可靠样本保持自训练，同时用像素级分类器锚定定位能力，在跨器官/跨中心病理基准上持续优于现有 SFDA 方法。

**[Adaptive Confidence Regularization For Multimodal Failure Detection](adaptive_confidence_regularization_for_multimodal_failure_detection.md)**

:   提出 ACR 框架，通过自适应置信度损失（惩罚多模态融合置信度低于单模态的"置信度退化"现象）和多模态特征交换（在特征空间合成失败样本）两个互补模块，首次系统解决多模态场景下的误分类检测问题，在四个数据集上全面超越已有方法。

**[Addressing Data Scarcity In 3D Trauma Detection Th](addressing_data_scarcity_in_3d_trauma_detection_th.md)**

:   在仅206例标注CT中，通过patch-based MIM预训练3D U-Net + VDETR顶点RPE + 半监督一致性正则化的两阶段框架，将3D创伤检测mAP@0.50从26.36%提升至56.57%（验证集），同时冻结编码器的7类分类达94.07%准确率。

**[Addressing Data Scarcity In 3D Trauma Detection Through Self-Supervised And Semi](addressing_data_scarcity_in_3d_trauma_detection_through_self-supervised_and_semi.md)**

:   提出两阶段标签高效框架：先用 patch-based MIM 在1,206个无标注CT上自监督预训练3D U-Net编码器，再用VDETR+3D顶点相对位置编码做3D损伤检测，配合Mean Teacher半监督一致性正则化利用2,000个无标注体数据，仅用144个有标注样本即实现56.57% val mAP@0.50（比纯监督提升115%）。

**[Are General-Purpose Vision Models All We Need For 2D Medical Image Segmentation ](are_general-purpose_vision_models_all_we_need_for_2d_medical_image_segmentation_.md)**

:   通过统一实验协议对比 11 个专用医学分割架构（SMAs）与通用视觉模型（GP-VMs），发现 GP-VMs 在三个异构医学数据集上优于大多数 SMAs，且 Grad-CAM 分析表明 GP-VMs 无需领域特定设计即可捕捉临床相关结构。

**[Are Generalpurpose Vision Models All We Need For 2](are_generalpurpose_vision_models_all_we_need_for_2.md)**

:   在统一训练和评估协议下对比11个专用医学分割架构(SMA)和通用视觉模型(GP-VM)，发现GP-VM在三个异质医学数据集上超越大多数SMA，且Grad-CAM分析表明GP-VM无需领域特定设计即可捕获临床相关结构。

**[Association Of Radiologic Ppfe Change With Mortali](association_of_radiologic_ppfe_change_with_mortali.md)**

:   在 NLST（n=7980）和 SUMMIT（n=8561）两个大规模肺癌筛查队列中，利用深度学习自动分割量化低剂量 CT 上 PPFE 的纵向变化（dPPFE），验证其与全因死亡率（HR=1.25/3.14）和呼吸系统发病率的独立关联。

**[Association Of Radiologic Ppfe Change With Mortality In Lung Cancer Screening Co](association_of_radiologic_ppfe_change_with_mortality_in_lung_cancer_screening_co.md)**

:   在两个大规模肺癌筛查队列（NLST n=7980, SUMMIT n=8561）上，利用深度学习自动分割 PPFE 体积并定义"进展性 PPFE"，通过 Cox 比例风险模型证明 PPFE 进展是全因死亡率的独立预测因子（NLST HR=1.25, SUMMIT HR=3.14），并与呼吸入院率、抗生素/类固醇使用等临床终点显著关联。

**[Automated Detection Of Malignant Lesions In The Ov](automated_detection_of_malignant_lesions_in_the_ov.md)**

:   系统对比 15 种 CNN 变体在卵巢癌组织病理图像五分类上的表现，选出 InceptionV3-A（ReLU）达 94% 综合指标后，用 LIME/SHAP/Integrated Gradients 三种 XAI 方法解释其决策。

**[Automated Detection Of Malignant Lesions In The Ovary Using Deep Learning Models](automated_detection_of_malignant_lesions_in_the_ovary_using_deep_learning_models.md)**

:   系统地比较了 LeNet/ResNet/VGG/Inception 四大CNN架构的15个变体在卵巢癌组织病理学图像分类上的表现，最终选择 InceptionV3-ReLU 作为基础模型(平均指标~94%)，并结合 LIME、SHAP、Integrated Gradients 三种 XAI 方法对分类结果进行可解释性分析。

**[Benchmarking Endoscopic Surgical Image Restoration And Beyond](benchmarking_endoscopic_surgical_image_restoration_and_beyond.md)**

:   构建了首个多源真实世界内窥镜手术图像复原数据集 SurgClean（3,113张图像，覆盖去烟/去雾/去飞溅三种退化类型），在其上系统评测了22种代表性图像复原方法（12种通用+10种任务特定），揭示现有方法与临床需求间仍存在显著差距，并进一步分析了手术场景退化与自然场景退化的本质差异。

**[Better Than Average Spatially-Aware Aggregation Of Segmentation Uncertainty Impr](better_than_average_spatially-aware_aggregation_of_segmentation_uncertainty_impr.md)**

:   首次系统研究分割任务中像素级不确定性到图像级分数的聚合策略，提出融合空间结构信息的聚合方法（基于Moran's I、Edge Density、Shannon Entropy的空间质量比SMR），以及GMM元聚合器，在10个数据集的OoD和故障检测任务上验证了空间感知聚合显著优于全局平均。

**[Beyond Pixel Simulation Pathology Image Generation Via Diagnostic Semantic Token](beyond_pixel_simulation_pathology_image_generation_via_diagnostic_semantic_token.md)**

:   UniPath提出语义驱动的病理图像生成框架，通过多流控制（原始文本 + 从冻结病理MLLM蒸馏的诊断语义Token + 原型库形态控制）实现诊断级可控生成，Patho-FID达80.9，比第二名优51%。

**[Biclip Bidirectional And Consistent Language-Image Processing For Robust Medical](biclip_bidirectional_and_consistent_language-image_processing_for_robust_medical.md)**

:   提出 BiCLIP 框架，通过双向多模态融合（BMF）实现视觉信息反向精炼文本表示，并通过图像增强一致性（IAC）约束中间特征的扰动不变性，在 COVID-19 CT 分割上超越 SOTA，仅 1% 标注数据仍保持鲁棒。

**[Biclip Bidirectional And Consistent Languageimage](biclip_bidirectional_and_consistent_languageimage.md)**

:   提出双向视觉-语言融合（BMF）和增强一致性（IAC）两个模块，让文本和图像特征可以相互修正，在标注极度稀缺（1%）和图像退化（低剂量CT噪声/运动模糊）场景下仍保持分割鲁棒性。

**[Bidirectional Multimodal Prompt Learning With Scale-Aware Training For Few-Shot ](bidirectional_multimodal_prompt_learning_with_scale-aware_training_for_few-shot_.md)**

:   提出AnoPLe——一个轻量级多模态双向提示学习框架，无需手工异常描述或外部辅助模块，通过文本-视觉提示双向交互和尺度感知前缀实现少样本多类别异常检测，在MVTec-AD/VisA/Real-IAD上取得强竞争力的同时保持高效推理（~28 FPS）。

**[Bridging The Skill Gap In Clinical Cbct Interpreta](bridging_the_skill_gap_in_clinical_cbct_interpreta.md)**

:   构建了覆盖55种口腔疾病的7,408例大规模配对CBCT-报告数据集，开发双语报告生成系统CBCTRepD，并通过多层级临床评估证明其可帮助不同经验水平的放射科医生提升报告质量。

**[Bridging The Skill Gap In Clinical Cbct Interpretation With Cbctrepd](bridging_the_skill_gap_in_clinical_cbct_interpretation_with_cbctrepd.md)**

:   提出 CBCTRepD——面向口腔颌面 CBCT 的双语报告生成系统，基于 7,408 例高质量配对数据集训练，通过放射科医生-AI 协作工作流，帮助不同经验水平的放射科医生系统性提升报告质量：初级→中级、中级→高级、高级减少遗漏。

**[Can Natural Image Autoencoders Compactly Tokenize Fmri Volumes For Long-Range Dy](can_natural_image_autoencoders_compactly_tokenize_fmri_volumes_for_long-range_dy.md)**

:   提出 TABLeT，利用预训练的 2D 自然图像自编码器（DCAE）将 3D fMRI 体积压缩为仅 27 个连续 token，配合简单 Transformer 编码器实现前所未有的长时序建模（256 帧），在 UKB、HCP、ADHD-200 上多任务超越 SOTA 体素方法，且计算效率大幅提升。

**[Care A Molecular-Guided Foundation Model With Adaptive Region Modeling For Whole](care_a_molecular-guided_foundation_model_with_adaptive_region_modeling_for_whole.md)**

:   提出 CARE，一种病理学 slide-level 基础模型，通过自适应区域生成器（ARG）将 WSI 划分为形态学相关的不规则区域（类似 NLP 中的词级 token），并结合 RNA/蛋白质表达谱的跨模态对齐进行两阶段预训练，仅用主流模型约 1/10 的数据即在 33 个下游任务上取得最优平均性能。

**[Cell-Type Prototype-Informed Neural Network For Gene Expression Estimation From ](cell-type_prototype-informed_neural_network_for_gene_expression_estimation_from_.md)**

:   提出 CPNN，利用公开单细胞 RNA-seq 数据构建细胞类型原型（cell-type prototype），将 slide/patch 级基因表达建模为原型的加权组合，在基因表达估计任务上取得 SOTA 并提供可解释性。

**[Chips Clip Adaptation Curvature Data Selection](chips_clip_adaptation_curvature_data_selection.md)**

:   从数据中心视角重新审视 CLIP 领域适配，提出 CHIPS，为每个图文对计算融合曲率感知牛顿对齐（忠实性）、JL sketching压缩曲率估计（可扩展性）、可学习性+领域相关性权重（保留性）三因素的效用分数，用30%数据匹配全数据集CPT、10%数据超越50%数据CPT，在17个医学+31个通用基准上达到选择SOTA。

**[Chips Efficient Clip Adaptation Via Curvature-Aware Hybrid Influence-Based Data ](chips_efficient_clip_adaptation_via_curvature-aware_hybrid_influence-based_data_.md)**

:   提出 CHIPS，一种基于曲率感知混合影响力的数据选择方法，在 CLIP 端点子空间中计算 Newton 风格对齐分数并结合可学习性与领域相关性权重，仅用 30% 数据即可匹配全量数据集持续预训练效果，在 17 个医学基准上达到 SOTA。

**[Cloe Expert Consistency Learning For Missing Modal](cloe_expert_consistency_learning_for_missing_modal.md)**

:   将缺失模态下的鲁棒性问题重新定义为决策级专家一致性控制，提出双分支一致性学习（全局MEC+区域REC），并通过轻量门网络将一致性分数转化为模态可靠性权重用于融合。

**[Cloe Expert Consistency Learning For Missing Modality Segmentation](cloe_expert_consistency_learning_for_missing_modality_segmentation.md)**

:   提出 CLoE（Consistency Learning of Experts），将缺失模态鲁棒性问题建模为决策层面的专家一致性控制，通过模态专家一致性（MEC）和区域专家一致性（REC）双分支约束减少专家漂移，并用一致性分数驱动的门控网络实现可靠性加权融合。

**[Crft Consistent-Recurrent Feature Flow Transformer For Cross-Modal Image Registr](crft_consistent-recurrent_feature_flow_transformer_for_cross-modal_image_registr.md)**

:   提出CRFT，统一的粗到精跨模态图像配准框架——在Transformer架构中学习模态无关的特征流表示，粗阶段1/8分辨率全局对应+精阶段1/2-1/4多尺度局部细化，配合迭代差异引导注意力和空间几何变换(SGT)递归精化流场捕捉微妙空间不一致，在光学/红外/SAR/多光谱等多种跨模态数据集上超越RAFT/GMFlow/LoFTR等SOTA。

**[Cross-Slice Knowledge Transfer Via Masked Multi-Modal Heterogeneous Graph Contra](cross-slice_knowledge_transfer_via_masked_multi-modal_heterogeneous_graph_contra.md)**

:   提出 SpaHGC，一种基于多模态异构图的框架，通过构建目标切片内、跨切片和参考切片内三种子图，结合 masked graph 对比学习和跨节点双注意力机制，实现从 H&E 病理图像预测空间基因表达，在七个数据集上 PCC 指标提升 7.3%-27.1%。

**[Cryosense Compressive Sensing Enables High-Throughput Microscopy With Sparse And](cryosense_compressive_sensing_enables_high-throughput_microscopy_with_sparse_and.md)**

:   提出 cryoSENSE，首个冷冻电镜压缩成像的计算框架，证明蛋白质 cryo-EM 图像在稀疏先验（DCT/小波/TV）和生成先验（扩散模型）下均可从欠采样测量中高保真重建，在保持 3D 分辨率的同时实现最高 2.5× 通量提升。

**[Cure Curriculum-Guided Multi-Task Training For Reliable Anatomy Grounded Report ](cure_curriculum-guided_multi-task_training_for_reliable_anatomy_grounded_report_.md)**

:   提出 CURE——一种基于误差感知课程学习的多任务训练框架，在不引入额外数据的前提下，通过动态调节采样分布重点训练困难样本，将医学 VLM 的视觉定位精度提升 +0.37 IoU，幻觉率降低 18.6%。

**[Decoding Matters Efficient Mamba-Based Decoder With Distribution-Aware Deep Supe](decoding_matters_efficient_mamba-based_decoder_with_distribution-aware_deep_supe.md)**

:   提出 Deco-Mamba，一种以解码器为中心的 Transformer-CNN-Mamba 混合架构，通过 Co-Attention Gate、视觉状态空间模块（VSSM）和可变形卷积增强解码过程，同时引入基于窗口化 KL 散度的分布感知深度监督策略，在 7 个医学图像分割基准上取得 SOTA。

**[Decoding Matters Efficient Mambabased Decoder With](decoding_matters_efficient_mambabased_decoder_with.md)**

:   提出以解码器为核心的 Deco-Mamba 网络，用 Co-Attention Gate 双向融合编解码器特征、视觉状态空间模块（VSSM）建模长程依赖、可变形卷积恢复细节，并引入窗口化分布感知 KL 散度深度监督，在 7 个医学分割基准上以中等复杂度达到 SOTA。

**[Decoupling Vision And Language Codebook Anchored Visual Adaptation](decoupling_vision_and_language_codebook_anchored_visual_adaptation.md)**

:   提出 CRAFT，通过离散 codebook 将视觉编码器与语言模型解耦，仅微调视觉编码器即可实现领域适配，且适配后的编码器可跨 LLM 架构无缝复用，在 10 个领域基准上平均提升 13.51%。

**[Deep Learning-Based Assessment Of The Relation Between The Third Molar And Mandi](deep_learning-based_assessment_of_the_relation_between_the_third_molar_and_mandi.md)**

:   在全景X光片上比较本地学习(LL)、联邦学习(FL)和集中学习(CL)三种范式对第三磨牙与下颌管重叠关系的二分类性能，发现集中学习最优(AUC 0.831)，联邦学习作为隐私保护替代方案(AUC 0.757)显著优于本地学习(AUC均值 0.672)。

**[Deep Learning Based Estimation Of Blood Glucose Le](deep_learning_based_estimation_of_blood_glucose_le.md)**

:   提出 ScleraGluNet 框架，通过五个注视方向的巩膜血管图像，结合多分支 CNN + MRFO 特征优化 + Transformer 跨视角融合，实现 93.8% 三分类精度和 MAE=6.42 mg/dL 的空腹血糖估计。

**[Deep Learning Based Estimation Of Blood Glucose Levels From Multidirectional Scl](deep_learning_based_estimation_of_blood_glucose_levels_from_multidirectional_scl.md)**

:   提出 ScleraGluNet，通过多方向巩膜血管图像（5 个注视方向）结合多分支 CNN + MRFO 特征优化 + Transformer 跨视角融合，实现三类代谢状态分类（93.8% 准确率）和连续血糖估计（MAE=6.42 mg/dL, r=0.983）。

**[Deep Learningbased Assessment Of The Relation Betw](deep_learningbased_assessment_of_the_relation_betw.md)**

:   在 8 个标注者划分的全景口腔 X 光裁剪片上，系统对比本地学习（LL）、联邦学习（FL）和集中学习（CL）在第三磨牙-下颌管重叠二分类任务上的表现，验证 FL 作为隐私保护替代方案的可行性。

**[Developing Foundation Models For Universal Segment](developing_foundation_models_for_universal_segment.md)**

:   构建迄今最大的全身 PET 分割数据集 PETWB-Seg11K（11041 例扫描、59831 个掩模），并提出 SegAnyPET 基础模型，实现基于 prompt 的 3D 全身 PET 通用可交互分割，在多中心、多示踪剂、多疾病场景下展现强 zero-shot 泛化能力。

**[Developing Foundation Models For Universal Segmentation From 3D Whole-Body Posit](developing_foundation_models_for_universal_segmentation_from_3d_whole-body_posit.md)**

:   构建迄今最大的全身 PET 分割数据集 PETWB-Seg11K（11,041 例 3D PET + 59,831 masks），并提出 SegAnyPET——首个面向功能性 PET 影像的 3D 可提示分割基础模型，在多中心、多示踪剂、多疾病场景下实现了强零样本泛化能力。

**[Diffusion-Based Feature Denoising And Using Nnmf For Robust Brain Tumor Classifi](diffusion-based_feature_denoising_and_using_nnmf_for_robust_brain_tumor_classifi.md)**

:   本文提出 NNMF+CNN+扩散防御框架用于脑肿瘤 MRI 分类：先用 NNMF 将图像分解为紧凑可解释的低秩特征，通过 AUC/Cohen's d/p-value 统计指标筛选最强判别组件，再用轻量 CNN 分类；推理时引入前向扩散加噪 + 学习去噪器的特征空间净化模块，在 AutoAttack ($L_\infty$, $\epsilon=0.10$) 下将鲁棒准确率从 0.47% 提升至 59.53%。

**[Diffusionbased Feature Denoising And Using Nnmf Fo](diffusionbased_feature_denoising_and_using_nnmf_fo.md)**

:   将 MRI 脑肿瘤分类任务分解为 NNMF 特征提取 → 统计特征筛选 → 轻量 CNN 分类 → 特征空间扩散净化四阶段流水线，在 AutoAttack 下将鲁棒精度从基线 0.5% 提升到 59.5%。

**[Echoagent Towards Reliable Echocardiography Interpretation With Eyeshands And Mi](echoagent_towards_reliable_echocardiography_interpretation_with_eyeshands_and_mi.md)**

:   提出 EchoAgent，一个模拟心脏超声医师"眼-手-脑"协同工作流程的 Agent 系统，通过专业知识引擎（mind）、分层工具箱（eyes+hands）和编排推理中枢（reasoning hub）三阶段实现端到端超声心动图可靠解读，在多个基准上达到 SOTA。

**[Eda Arbitrary Noise Diffusion Design Space](eda_arbitrary_noise_diffusion_design_space.md)**

:   提出 EDA 框架，将 EDM 的设计空间从纯高斯噪声扩展至任意噪声模式，通过多元高斯分布和多独立维纳过程驱动的 SDE 实现灵活噪声扩散，且证明噪声复杂度的提升不引入额外采样开销；仅用 5 步采样即可在 MRI 偏置场矫正、CT 金属伪影去除和自然图像阴影去除三项任务上取得媲美或优于百步 Refusion 和专用方法的效果。

**[Ei Early Intervention For Multimodal Imaging Based Disease Recognition](ei_early_intervention_for_multimodal_imaging_based_disease_recognition.md)**

:   EI 提出在单模态嵌入（UIE）**之前**就注入跨模态语义引导（[INT] token），模拟临床医生"先看一个模态形成初步判断再指导另一个模态检查"的工作流程，同时设计 MoR（多种秩 LoRA + 带旁路的松弛路由器）实现参数高效的 VFM 医学域适配，在视网膜/皮肤/膝关节三个数据集上以 <9M 可训练参数超越所有全参微调和 prompt learning 基线。

**[Elucidating The Design Space Of Arbitrary-Noise-Based Diffusion Models](elucidating_the_design_space_of_arbitrary-noise-based_diffusion_models.md)**

:   提出 EDA 框架，将 EDM 的设计空间从高斯噪声扩展到任意噪声模式，通过多元高斯分布参数化协方差矩阵实现灵活的噪声扩散，在 MRI 偏置场校正、CT 金属伪影去除和自然图像阴影去除三个任务上仅用 5 步采样即达到或超越 100 步 EDM 方法和专用方法。

**[Emad Evidence-Centric Grounded Multimodal Diagnosis For Alzheimers Disease](emad_evidence-centric_grounded_multimodal_diagnosis_for_alzheimers_disease.md)**

:   提出 EMAD，一个端到端多模态视觉-语言框架，为 AD 诊断生成结构化报告，通过分层 Sentence–Evidence–Anatomy (SEA) Grounding 将每个诊断声明显式关联到临床证据和 3D 脑部解剖，并用可执行规则驱动的 GRPO 强化微调确保临床一致性。

**[Equivania A Spectral Method For Rotation-Equivariant Anisotropic Image Analysis](equivania_a_spectral_method_for_rotation-equivariant_anisotropic_image_analysis.md)**

:   提出 EquivAnIA，一种基于 cake wavelets 和 ridge filters 的频谱方法，用于对数值旋转鲁棒的各向异性图像分析，在合成和真实图像（含 CT 扫描）上显著优于传统 angular binning 基线，并成功应用于角度图像配准任务。

**[Equivania A Spectral Method For Rotationequivarian](equivania_a_spectral_method_for_rotationequivarian.md)**

:   提出EquivAnIA——基于Cake小波和Ridge滤波器的频谱方法，通过方向滤波器在傅里叶域计算角度能量分布，实现对数值旋转严格等变的各向异性图像分析，在合成和真实图像上一致优于传统角度功率谱密度方法。

**[Every Error Has Its Magnitude Asymmetric Mistake Severity Training For Multiclas](every_error_has_its_magnitude_asymmetric_mistake_severity_training_for_multiclas.md)**

:   提出 PAMS（Priority-Aware Mistake Severity）方法，通过非对称严重性感知的交叉熵损失（MSCE）、语义特征混合（SFR）和非对称 Mikel's Wheel 指标，在多分类 MIL WSI 诊断中显著降低严重误诊风险。

**[Extending Zach-Vit To Robust Medical Imaging Corruption And Adversarial Stress T](extending_zach-vit_to_robust_medical_imaging_corruption_and_adversarial_stress_t.md)**

:   在低数据医学影像场景下，对置换不变的紧凑型 ViT 架构 ZACH-ViT 进行首次鲁棒性评估，发现其在常见图像损坏下保持最佳综合表现，在对抗攻击下仍具竞争力。

**[Fair Lung Disease Diagnosis From Chest Ct Via Gend](fair_lung_disease_diagnosis_from_chest_ct_via_gend.md)**

:   在 ConvNeXt 骨干上构建注意力 MIL 模型，并通过梯度反转层（GRL）对抗性地消除扫描表征中的性别信息，再配合 focal loss、子群过采样和 5-fold 集成，实现胸部 CT 四类肺疾病的公平诊断。

**[Fair Lung Disease Diagnosis From Chest Ct Via Gender-Adversarial Attention Multi](fair_lung_disease_diagnosis_from_chest_ct_via_gender-adversarial_attention_multi.md)**

:   提出基于注意力 MIL 和梯度反转层（GRL）的公平性框架，从胸部 CT 体积中进行多类肺部疾病诊断，在保证诊断准确性的同时消除性别偏差。

**[Federated Modality-Specific Encoders And Partially Personalized Fusion Decoder F](federated_modality-specific_encoders_and_partially_personalized_fusion_decoder_f.md)**

:   提出 FedMEPD 框架，通过模态专属编码器 + 部分个性化融合解码器 + 多锚点跨注意力校准，同时解决联邦学习中多模态 MRI 的模态间异质性和客户端个性化需求。

**[Federated Modalityspecific Encoders And Partially](federated_modalityspecific_encoders_and_partially.md)**

:   提出 FedMEPD 联邦学习框架，通过模态专属编码器、部分个性化融合解码器和多锚点交叉注意力校准，同时获得最优全模态全局模型和各客户端缺失模态个性化模型。

**[Fedvg Gradient-Guided Aggregation For Enhanced Federated Learning](fedvg_gradient-guided_aggregation_for_enhanced_federated_learning.md)**

:   FedVG 提出利用全局验证集上的逐层梯度范数为各客户端打分，梯度越平坦（范数越小）的客户端获得越高聚合权重，从而在高度数据异质性场景下显著提升联邦学习的泛化性能。

**[Focus-To-Perceive Representation Learning A Cognition-Inspired Hierarchical Fram](focus-to-perceive_representation_learning_a_cognition-inspired_hierarchical_fram.md)**

:   提出 FPRL，一个受临床认知启发的层次化自监督框架，通过先"聚焦"帧内病灶关键静态语义、再"感知"帧间上下文演化来缓解运动偏差，在 11 个内窥镜数据集上取得 SOTA。

**[Forecasting Epileptic Seizures From Contactless Ca](forecasting_epileptic_seizures_from_contactless_ca.md)**

:   首次系统定义基于视频的癫痫发作预测任务，提出两阶段跨物种迁移学习框架——先在啮齿类癫痫视频上自监督预训练 VideoMAE，再在人类发作前视频上少样本微调——在纯视频设定下实现超过 72% 的均衡准确率。

**[Forecasting Epileptic Seizures From Contactless Camera Via Cross-Species Transfe](forecasting_epileptic_seizures_from_contactless_camera_via_cross-species_transfe.md)**

:   首次提出纯视频的癫痫发作预测任务，利用大规模啮齿动物癫痫视频进行跨物种自监督预训练，通过 VideoMAE 框架实现 3-10 秒预测窗口内 >70% 的发作预测准确率。

**[Giim Graph-Based Learning Of Inter- And Intra-View Dependencies For Multi-View M](giim_graph-based_learning_of_inter-_and_intra-view_dependencies_for_multi-view_m.md)**

:   提出 GIIM 框架，基于多异构图（MHG）同时建模多视图医学影像中病变间的视图内（intra-view）和视图间（inter-view）依赖关系，并通过四种缺失视图表示策略实现对不完整数据的鲁棒诊断。

**[Giim Graphbased Learning Of Inter And Intraview De](giim_graphbased_learning_of_inter_and_intraview_de.md)**

:   提出基于多异构图 (MHG) 的 GIIM 框架，通过四类边关系建模同一病灶跨视图动态变化和不同病灶间空间关联，并设计四种缺失视图填充策略，在 CT/MRI/乳腺 X 光三种模态上均显著优于现有方法。

**[Gleam A Multimodal Imaging Dataset And Hamm For Gl](gleam_a_multimodal_imaging_dataset_and_hamm_for_gl.md)**

:   提出首个公开三模态青光眼数据集 GLEAM（SLO 眼底图 + 环乳头 OCT + 视野偏差图，标注四个疾病阶段），以及层级注意力掩码建模 (HAMM) 框架，将跨模态自监督表示学习聚焦在编码器端，实现多模态青光眼精准分类。

**[Gleam A Multimodal Imaging Dataset And Hamm For Glaucoma Classification](gleam_a_multimodal_imaging_dataset_and_hamm_for_glaucoma_classification.md)**

:   提出首个公开的三模态青光眼数据集 GLEAM（SLO 眼底图像 + 环视盘 OCT + 视野偏差图）并设计层级注意力掩码建模框架 HAMM，通过层级注意力编码器与轻量解码器将跨模态表征学习聚焦于编码器端，实现四阶段青光眼精确分类。

**[Human Knowledge Integrated Multi-Modal Learning For Single Source Domain General](human_knowledge_integrated_multi-modal_learning_for_single_source_domain_general.md)**

:   提出 GenEval，通过域共形界（DCB）量化因果覆盖差距，并将人类专家知识量化精炼后与医学 VLM（MedGemma-4B）融合，以 LoRA 微调实现单源域泛化，在 DR 分级和癫痫灶检测上显著超越基线。

**[Human Knowledge Integrated Multimodal Learning For](human_knowledge_integrated_multimodal_learning_for.md)**

:   提出域保形界(DCB)理论框架量化域间因果因子差异，并据此设计GenEval——通过知识精炼+MedGemma-4B LoRA微调，将人类专家领域知识整合到VLM中实现单源域泛化，在8个DR和2个SOZ数据集上显著超越SOTA。

**[Interpretable Cross-Domain Few-Shot Learning With Rectified Target-Domain Local ](interpretable_cross-domain_few-shot_learning_with_rectified_target-domain_local_.md)**

:   发现并解决了 CLIP 在跨域少样本学习（CDFSL）中的局部特征对齐退化问题，提出基于循环一致性的 CC-CDFSL 框架，通过 T-I-T 和 I-T-I 双向循环路径和语义锚点机制改善 patch 级视觉-语言对齐，同时增强模型的可解释性。

**[Invad Inversion-Based Reconstruction-Free Anomaly Detection With Diffusion Model](invad_inversion-based_reconstruction-free_anomaly_detection_with_diffusion_model.md)**

:   提出 InvAD，将扩散模型异常检测从"RGB 空间去噪重建"范式转变为"潜空间加噪反演"范式，通过 DDIM 反演直接推断最终潜变量并在先验分布下度量偏差来检测异常，仅需 3 步反演即达 SOTA 性能且推理速度提升约 2 倍。

**[Invad Inversionbased Reconstructionfree Anomaly De](invad_inversionbased_reconstructionfree_anomaly_de.md)**

:   提出"检测即加噪"范式取代传统"检测即去噪"——通过DDIM反转将图像映射到潜在噪声空间，仅用3步推理判断偏离先验分布的程度作为异常分数，无需重建，实现SOTA精度的同时推理速度达88 FPS（比OmiAD快2倍+）。

**[Learning Generalizable 3D Medical Image Representations From Mask-Guided Self-Su](learning_generalizable_3d_medical_image_representations_from_mask-guided_self-su.md)**

:   提出 MASS（MAsk-guided Self-Supervised learning），利用 SAM2 自动生成的类别无关 mask 作为伪标注，以 in-context 分割为 pretext task 进行自监督预训练，无需任何人工标注即可学到语义丰富、泛化性强的 3D 医学图像表征，在 few-shot 分割和冻结编码器分类上均取得优异表现。

**[Lumina A Multi-Vendor Mammography Benchmark With Energy Harmonization Protocol](lumina_a_multi-vendor_mammography_benchmark_with_energy_harmonization_protocol.md)**

:   提出 LUMINA 多厂商乳腺 FFDM 数据集（468 例患者、1824 张图像），附带前景像素直方图匹配的能量协调预处理方法，在诊断/BI-RADS/密度三任务上系统评估了 CNN 与 Transformer 模型。

**[Marker-Based 3D Reconstruction Of Aggregates With A Comparative Analysis Of 2D A](marker-based_3d_reconstruction_of_aggregates_with_a_comparative_analysis_of_2d_a.md)**

:   提出基于标记物（marker）的低成本摄影测量方法，实现骨料颗粒的高质量 3D 重建，并通过 2D 与 3D 形态学指标的系统对比分析，揭示 2D 投影分析对真实 3D 形态的显著偏差。

**[Markerbased 3D Reconstruction Of Aggregates With A](markerbased_3d_reconstruction_of_aggregates_with_a.md)**

:   提出一种基于标记物（marker）的低成本摄影测量方法，实现骨料（aggregate）颗粒的高质量三维重建，并通过 2D 与 3D 形态学指标的系统对比分析，揭示了仅依赖 2D 图像进行骨料形态评估的显著局限性。

**[Medclipseg Probabilistic Vision-Language Adaptation For Data-Efficient And Gener](medclipseg_probabilistic_vision-language_adaptation_for_data-efficient_and_gener.md)**

:   在冻结CLIP编码器的基础上，通过概率交叉模态注意力（PVL）实现图文双向交互与预测不确定性建模，配合软patch级对比损失，在16个医学分割数据集上兼顾数据效率、域泛化能力和可解释性。

**[Medgen-Bench Contextually Entangled Benchmark For Open-Ended Multimodal Medical ](medgen-bench_contextually_entangled_benchmark_for_open-ended_multimodal_medical_.md)**

:   提出 MedGEN-Bench，首个面向开放式多模态医学生成的综合基准，包含 6,422 个专家验证的图文对、6 种成像模态、16 个临床任务，配套三层评估框架，揭示了组合框架优于统一模型的跨模态一致性问题。

**[Medkco Medical Vision-Language Pretraining Via Knowledge-Driven Cognitive Orches](medkco_medical_vision-language_pretraining_via_knowledge-driven_cognitive_orches.md)**

:   提出 MedKCO，一种知识驱动的认知编排策略用于医学视觉-语言预训练：通过分层课程（label-level 按诊断敏感度排序 + description-level 按样本代表性排序）和自步非对称对比损失，让模型从简单到复杂渐进学习，在三种医学模态的零样本和下游任务上显著超越基线。

**[Mil-Pf Multiple Instance Learning On Precomputed Features For Mammography Classi](mil-pf_multiple_instance_learning_on_precomputed_features_for_mammography_classi.md)**

:   提出 MIL-PF，利用冻结的基础视觉编码器（DINOv2/MedSigLIP）预计算特征，再用仅约 40K 参数的轻量 MIL 头进行乳腺 X 线分类，在大规模 EMBED 数据集上达到 SOTA 性能，同时大幅降低训练成本。

**[Milpf Multiple Instance Learning On Precomputed Fe](milpf_multiple_instance_learning_on_precomputed_fe.md)**

:   提出MIL-PF框架，将冻结的基础视觉编码器（DINOv2/MedSigLIP）与仅40k参数的轻量级MIL聚合头结合，通过预计算特征+双流（全局组织上下文+局部病变注意力）聚合，在大规模乳腺X线分类任务上以极低训练成本达到SOTA性能。

**[Mind The Discriminability Trap In Source-Free Cross-Domain Few-Shot Learning](mind_the_discriminability_trap_in_source-free_cross-domain_few-shot_learning.md)**

:   揭示了在 VLM 的跨域小样本微调中，增强视觉判别性反而损害跨模态对齐（"判别性陷阱"），提出 SVL + RA 两个即插即用模块来抑制视觉学习捷径并引导跨模态对齐，在 4 个 CDFSL 数据集和 11 个 FSL 数据集上取得 SOTA。

**[Moeclip Patch-Specialized Experts For Zero-Shot Anomaly Detection](moeclip_patch-specialized_experts_for_zero-shot_anomaly_detection.md)**

:   提出 MoECLIP，将 Mixture-of-Experts 引入零样本异常检测（ZSAD），通过冻结正交特征分离（FOFS）和等角紧框架（ETF）损失实现 patch 级别的动态专家路由与特化，在14个工业/医学基准上达到 SOTA。

**[Momentum Memory For Knowledge Distillation In Computational Pathology](momentum_memory_for_knowledge_distillation_in_computational_pathology.md)**

:   提出 MoMKD，用动量更新的类条件记忆库替代传统 batch-local 特征对齐，实现基因组→病理切片的跨模态知识蒸馏，仅用 H&E 切片推理即可获得基因组级预测能力。

**[Mri Contrast Enhancement Kinetics World Model](mri_contrast_enhancement_kinetics_world_model.md)**

:   首次提出 MRI 造影增强动力学世界模型（MRI CEKWorld），通过时空一致性学习（STCL）在稀疏采样数据上实现从无造影 MRI 到连续高保真造影增强序列的生成，解决了内容失真和时序不连续两大难题。

**[Multimodal Classification Of Radiation-Induced Contrast Enhancements And Tumor R](multimodal_classification_of_radiation-induced_contrast_enhancements_and_tumor_r.md)**

:   提出 RICE-NET，一个多模态 3D ResNet-18 模型，整合纵向 MRI 数据与放疗剂量分布图，用于自动区分胶质母细胞瘤术后放射诱导对比增强（RICE）与肿瘤复发，在独立测试集上达到 F1=0.92。

**[Multimodal Classification Of Radiationinduced Cont](multimodal_classification_of_radiationinduced_cont.md)**

:   提出RICE-NET，一种多模态3D ResNet-18模型，融合纵向T1加权MRI数据与放射治疗剂量分布图，在92例胶质母细胞瘤患者队列上实现F1=0.92的RICE vs 肿瘤复发自动分类，消融实验揭示放疗剂量图是最具信息量的单模态输入。

**[Multimodal Protein Language Models For Enzyme Kine](multimodal_protein_language_models_for_enzyme_kine.md)**

:   提出ERBA（Enzyme-Reaction Bridging Adapter），将酶动力学参数预测重新建模为与催化机制对齐的分阶段条件化问题——先通过MRCA注入底物信息捕捉分子识别，再通过G-MoE融合活性位点3D几何信息建模构象适应，并用ESDA做分布对齐保持PLM先验——在三个动力学指标上全面超越现有SOTA。

**[Multimodal Protein Language Models For Enzyme Kinetic Parameters From Substrate ](multimodal_protein_language_models_for_enzyme_kinetic_parameters_from_substrate_.md)**

:   提出**ERBA(Enzyme-Reaction Bridging Adapter)**，将酶动力学参数预测重新建模为**分阶段多模态条件生成问题**——先通过MRCA注入底物信息捕获底物识别特异性，再通过G-MoE整合活性位点3D结构捕获构象适应，配合ESDA分布对齐保持PLM语义先验。

**[Multimodalpfn Extending Prior-Data Fitted Networks For Multimodal Tabular Learni](multimodalpfn_extending_prior-data_fitted_networks_for_multimodal_tabular_learni.md)**

:   提出 MMPFN，首次将预训练表格基础模型 TabPFN 扩展到多模态（表格+图像/文本）场景，通过多头门控 MLP（MGM）和交叉注意力池化器（CAP）解决非表格嵌入过压缩和 token 数量不平衡问题，在医学和通用数据集上超越 SOTA。

**[Multiscale Structure-Guided Latent Diffusion For Multimodal Mri Translation](multiscale_structure-guided_latent_diffusion_for_multimodal_mri_translation.md)**

:   提出 MSG-LDM，在潜在扩散模型中引入多尺度结构-风格解耦机制，通过高频注入、多模态结构特征融合和结构感知损失，实现缺失模态场景下保留解剖结构和精细细节的多模态 MRI 合成。

**[Multiscale Structureguided Latent Diffusion For Mu](multiscale_structureguided_latent_diffusion_for_mu.md)**

:   提出MSG-LDM，一个基于潜在扩散模型的多模态MRI翻译框架，通过在潜空间中显式解耦风格和结构信息，结合高频注入（HFIB）、多模态结构特征融合（MMSF）和多尺度结构增强（MSSE）模块提取模态无关的完整结构先验来引导扩散去噪，在BraTS2020和WMH数据集上超越现有方法。

**[Muse Harnessing Precise And Diverse Semantics For Few-Shot Whole Slide Image Cla](muse_harnessing_precise_and_diverse_semantics_for_few-shot_whole_slide_image_cla.md)**

:   提出 MUSE 框架，通过 MoE 驱动的样本级细粒度语义增强（SFSE）和基于 LLM 知识库的随机多视角语义优化（SMMO），在少样本全切片图像分类任务上显著提升泛化能力。

**[Muvit Multi-Resolution Vision Transformers For Learning Across Scales In Microsc](muvit_multi-resolution_vision_transformers_for_learning_across_scales_in_microsc.md)**

:   提出 MuViT，一种基于世界坐标 RoPE 位置编码的多分辨率 Vision Transformer，能在单一编码器中联合处理同一场景不同物理分辨率的裁剪图，在显微镜图像分割任务上显著优于单分辨率基线。

**[Novel Architecture Of Rpa In Oral Cancer Lesion De](novel_architecture_of_rpa_in_oral_cancer_lesion_de.md)**

:   将软件设计模式（Singleton + Batch Processing）融入Python自动化流程，使口腔癌病变检测的推理速度相比传统RPA平台（UiPath/Automation Anywhere）提升60-100倍。

**[Novel Architecture Of Rpa In Oral Cancer Lesion Detection](novel_architecture_of_rpa_in_oral_cancer_lesion_detection.md)**

:   将软件设计模式（Singleton + Batch Processing）集成到基于 EfficientNetV2B1 的口腔癌病变检测 Python 流水线中，相比传统 RPA 平台（UiPath/Automation Anywhere）实现 60-100 倍的推理加速，同时保持诊断准确性。

**[Orapo Oracle-Educated Reinforcement Learning For Data-Efficient And Factual Radi](orapo_oracle-educated_reinforcement_learning_for_data-efficient_and_factual_radi.md)**

:   提出 OraPO（Oracle-educated GRPO），在 GRPO 探索失败时注入轻量 DPO 监督将失败 rollout 转化为偏好样本，配合 FactScore 奖励实现仅用 1K 样本、3B 小模型在 CheXpert Plus 和 MIMIC-CXR 上达到放射报告生成 SOTA（F1=0.341/0.357），训练数据量比前最优减少 2-3 个数量级。

**[Orapo Oracle Rl Radiology Report Generation](orapo_oracle_rl_radiology_report_generation.md)**

:   提出 OraPO, 一种结合 GRPO 和 DPO 的自适应混合 RL 框架, 用于数据高效的放射学报告生成: 通过 Zero-Reward Rate 检测动态切换 GRPO 和 DPO, 加上 FactScore-based 临床事实级奖励, 仅用 1K 样本 (对比基线 227K) 在 CheXpert Plus 和 MIMIC-CXR 上取得 SOTA 的临床 F1 (0.341/0.357).

**[Prototype-Based Knowledge Guidance For Fine-Grained Structured Radiology Reporti](prototype-based_knowledge_guidance_for_fine-grained_structured_radiology_reporti.md)**

:   提出 ProtoSR，通过 LLM 从大规模自由文本放射学报告中挖掘模板对齐的视觉原型知识库，并以原型条件化残差（late fusion）方式注入结构化报告生成模型，在 Rad-ReStruct 基准上取得 SOTA，尤其显著提升细粒度属性问题的性能。

**[Prototypebased Knowledge Guidance For Finegrained](prototypebased_knowledge_guidance_for_finegrained.md)**

:   提出ProtoSR，通过LLM驱动的管道从22.7万篇MIMIC-CXR自由文本报告中挖掘模板对齐的视觉原型知识库，并设计原型条件化迟融合模块将检索到的原型证据作为logit残差注入层级式结构化报告模型，在Rad-ReStruct基准上达到SOTA，在细粒度属性问题（L3）上提升最为显著（+72.1%相对提升）。

**[Reclaiming Lost Text Layers For Source-Free Cross-Domain Few-Shot Learning](reclaiming_lost_text_layers_for_source-free_cross-domain_few-shot_learning.md)**

:   发现 CLIP 文本编码器中存在"Lost Layers"——在 Source-Free Cross-Domain Few-Shot Learning (SF-CDFSL) 中移除某些中间层反而提升性能；论文证明这些层并非冗余而是因视觉域偏移未被充分利用，提出 VtT 模型在层级和编码器级别重新利用这些信息，取得 SOTA。

**[Reinforcing The Weakest Links Modernizing Siena Wi](reinforcing_the_weakest_links_modernizing_siena_wi.md)**

:   通过将SIENA纵向脑萎缩管线中的经典颅骨剥离(BET2)和组织分割(FAST)模块替换为深度学习方案(SynthStrip/SynthSeg)，在ADNI和PPMI两个大队列上显著增强了脑体积变化百分比(PBVC)与临床疾病进展的关联性，并将扫描顺序误差降低高达99.1%。

**[Reinforcing The Weakest Links Modernizing Siena With Targeted Deep Learning Inte](reinforcing_the_weakest_links_modernizing_siena_with_targeted_deep_learning_inte.md)**

:   通过将 SIENA 脑萎缩管线中经典的颅骨剥离（BET2）和组织分割（FAST）模块替换为深度学习方案（SynthStrip、SynthSeg），在保留管线可解释性的前提下显著提升了 PBVC 估计的临床敏感度和鲁棒性。

**[Residual Sodap Residual Self-Organizing Domain-Adaptive Prompting With Structura](residual_sodap_residual_self-organizing_domain-adaptive_prompting_with_structura.md)**

:   提出 Residual SODAP 框架，通过 α-entmax 稀疏提示选择+残差聚合、无数据统计蒸馏+伪特征回放、提示使用模式漂移检测，以及不确定性加权多损失平衡，联合解决提示端表征适应和分类器端知识保持问题，在医学域增量学习上达到 SOTA。

**[Residual Sodap Residual Selforganizing Domainadapt](residual_sodap_residual_selforganizing_domainadapt.md)**

:   提出Residual SODAP框架，在无任务ID、无数据存储的域增量学习中，联合解决表示适应（α-entmax稀疏prompt选择+残差聚合）和分类器保持（统计伪特征重放+知识蒸馏），在DR、皮肤癌和CORe50三个基准上达到SOTA。

**[Semantic Class Distribution Learning For Debiasing](semantic_class_distribution_learning_for_debiasing.md)**

:   提出即插即用的SCDL框架，通过学习类条件代理分布(双向对齐CDBA)+语义锚约束(SAC)来消除半监督医学图像分割中的长尾偏差，在AMOS 5%标签下DSC提升+11.62%。

**[Semantic Class Distribution Learning For Debiasing Semi-Supervised Medical Image](semantic_class_distribution_learning_for_debiasing_semi-supervised_medical_image.md)**

:   提出 SCDL 即插即用框架，通过可学习类别代理分布的双向对齐（CDBA）和标注数据构建的语义锚约束（SAC），在嵌入空间中学习结构化的类条件特征分布，解决半监督医学图像分割中的监督偏置和表征不平衡问题，尤其在尾类分割上取得显著提升。

**[Semitooth A Generalizable Semi-Supervised Framework For Multi-Source Tooth Segme](semitooth_a_generalizable_semi-supervised_framework_for_multi-source_tooth_segme.md)**

:   提出 SemiTooth 框架，通过多教师多学生架构和严格加权置信度约束（SWC），解决多源 CBCT 牙齿分割中的标注稀缺和跨源域间差异问题，同时构建了首个多源半监督牙齿数据集 MS3Toothset。

**[Semitooth A Generalizable Semisupervised Framework](semitooth_a_generalizable_semisupervised_framework.md)**

:   提出SemiTooth——多教师多学生半监督框架+更严格加权置信度约束(SWC)，用于多源CBCT牙齿分割，在新构建的MS3Toothset上mIoU达76.67%、Dice 85.69%，超越SOTA CMT(76.14%)。

**[Similarity-As-Evidence Calibrating Overconfident Vlms For Interpretable And Labe](similarity-as-evidence_calibrating_overconfident_vlms_for_interpretable_and_labe.md)**

:   提出 Similarity-as-Evidence (SaE) 框架，将 VLM 的文本-图像相似度重新解释为 Dirichlet 证据，通过 Similarity Evidence Head (SEH) 校准过度自信的 softmax 输出，并基于 vacuity（知识空缺）和 dissonance（证据冲突）的双因子采集策略实现可解释、高效的医学主动学习，在 10 个数据集上以 20% 标注预算达到 82.57% 的 SOTA 宏平均准确率。

**[Solving A Nonlinear Blind Inverse Problem For Tagged Mri With Physics And Deep G](solving_a_nonlinear_blind_inverse_problem_for_tagged_mri_with_physics_and_deep_g.md)**

:   提出 InvTag 框架，首次将 MR 物理前向模型与预训练扩散生成先验结合，统一解决 3D Tagged MRI 的解剖恢复、Cine 合成和运动估计三大子任务，且无需任何额外训练数据。

**[Sparse Task Vector Mixup With Hypernetworks For Efficient Knowledge Transfer In ](sparse_task_vector_mixup_with_hypernetworks_for_efficient_knowledge_transfer_in_.md)**

:   提出 STEPH，通过任务向量混合 (Task Vector Mixup) 与超网络驱动的稀疏聚合，将多个癌种预后模型的可泛化知识高效迁移到目标癌种，在 13 个 TCGA 数据集上平均 C-Index 提升 5.14%，且无需大规模联合训练或多模型推理。

**[Sparse Task Vector Mixup Wsi Prognosis](sparse_task_vector_mixup_wsi_prognosis.md)**

:   STEPH 将跨癌种预后模型的任务向量进行超网络驱动的混合（TVM）+ 稀疏聚合，在单一模型内完成知识迁移，13 个 TCGA 数据集上 C-Index 平均 0.6949（+5.14% vs 癌种特定学习，+2.01% vs ROUPKT），且推理开销远低于表示迁移方案。

**[Spegc Continual Test-Time Adaptation Via Semantic-Prompt-Enhanced Graph Clusteri](spegc_continual_test-time_adaptation_via_semantic-prompt-enhanced_graph_clusteri.md)**

:   提出 SPEGC 框架，通过语义提示增强特征 + 可微分图聚类求解器，将原始相似度矩阵精炼为高阶结构表示，用于指导医学图像分割模型在持续变化的目标域上自适应，有效缓解误差累积与灾难性遗忘。

**[Synergistic Bleeding Region And Point Detection In Laparoscopic Surgical Videos](synergistic_bleeding_region_and_point_detection_in_laparoscopic_surgical_videos.md)**

:   构建首个腹腔镜手术出血区域+出血点标注数据集 SurgBlood，并提出基于 SAM2 的双分支双向引导在线检测器 BlooDet，通过 Mask/Point 分支协同优化实现出血区域分割与出血点定位的联合检测。

**[Tell2Adapt A Unified Framework For Source Free Unsupervised Domain Adaptation Vi](tell2adapt_a_unified_framework_for_source_free_unsupervised_domain_adaptation_vi.md)**

:   提出 Tell2Adapt 统一框架，利用视觉基础模型（BiomedParse）的泛化知识，通过上下文感知提示正则化（CAPR）生成高质量伪标签，再经视觉合理性精炼（VPR）去除解剖学不合理预测，实现跨 10 个域迁移方向、22 个解剖目标的统一无源域自适应医学图像分割。

**[The Invisible Gorilla Effect In Out-Of-Distribution Detection](the_invisible_gorilla_effect_in_out-of-distribution_detection.md)**

:   揭示了OOD检测中一个此前未被报告的偏差——"隐形大猩猩效应"：当OOD伪影与模型关注区域（ROI）视觉外观相似时检测性能显著更好，不相似时则大幅下降，尤其影响基于特征的OOD方法。

**[Towards Efficient Medical Reasoning With Minimal Fine-Tuning Data](towards_efficient_medical_reasoning_with_minimal_fine-tuning_data.md)**

:   提出 Difficulty-Influence Quadrant (DIQ) 数据选择策略，联合考量样本难度和梯度影响力，使 VLM 语言骨干仅用 1% 精选数据即可匹配全量 SFT 性能，10% 数据则可超越全量训练。

**[Transformer-Based Multi-Region Segmentation And Radiomic Analysis Of Hr-Pqct Ima](transformer-based_multi-region_segmentation_and_radiomic_analysis_of_hr-pqct_ima.md)**

:   提出基于 SegFormer 的全自动多区域 HR-pQCT 分割框架，结合影像组学特征与机器学习实现骨质疏松二分类，发现软组织（肌腱/脂肪）特征的诊断价值优于传统骨骼特征。

**[Uncertainty-Aware Concept And Motion Segmentation For Semi-Supervised Angiograph](uncertainty-aware_concept_and_motion_segmentation_for_semi-supervised_angiograph.md)**

:   提出 SMART 框架，基于 SAM3 的概念提示分割构建 Teacher-Student 半监督模型，结合渐进置信度正则化和双流时序一致性策略，仅用极少标注在 X 射线冠脉造影视频中实现 SOTA 血管分割。

**[Unistainnet Foundation-Model-Guided Virtual Staining Of He To Ihc](unistainnet_foundation-model-guided_virtual_staining_of_he_to_ihc.md)**

:   提出 UNIStainNet，首次将冻结的病理基础模型 UNI 的密集空间 token 作为 SPADE 调制信号直接注入生成器，配合错位感知损失和可学习染色嵌入，用单一模型同时生成 HER2/Ki67/ER/PR 四种 IHC 染色，在 MIST 和 BCI 基准上取得 SOTA 分布式指标。

**[Unleashing Video Language Models For Fine-Grained Hrct Report Generation](unleashing_video_language_models_for_fine-grained_hrct_report_generation.md)**

:   提出 AbSteering 框架，通过异常中心的 Chain-of-Thought 训练和基于 DPO 的细粒度异常辨别，将通用视频语言模型（如 Qwen2.5-VL、InternVL3）适配到 HRCT 报告生成任务，以低成本超越专门的 CT 基础模型。

**[Unsupervised Domain Adaptation With Target-Only Margin Disparity Discrepancy](unsupervised_domain_adaptation_with_target-only_margin_disparity_discrepancy.md)**

:   针对 CT→CBCT 肝脏分割的无监督域自适应问题，发现经典 MDD 优化目标中存在矛盾项（源域上特征提取器被优化为最大化 $f$ 和 $f'$ 的差异），提出 Target-Only MDD 改进，去除矛盾项并在两域上统一最小化预测差异，在 2D 和 3D 实验中均取得 UDA SOTA。

**[Virtual Full-Stack Scanning Of Brain Mri Via Imputing Any Quantised Code](virtual_full-stack_scanning_of_brain_mri_via_imputing_any_quantised_code.md)**

:   提出 CodeBrain，将脑 MRI 任意到任意模态补全问题重新表述为区域级全栈量化码预测任务，通过两阶段流程（标量量化重建 + 分级损失码预测）实现统一的缺失模态合成，超越五种 SOTA 方法。

**[Virtual Fullstack Scanning Of Brain Mri Via Imputi](virtual_fullstack_scanning_of_brain_mri_via_imputi.md)**

:   CodeBrain将脑MRI多模态补全(any-to-any imputation)重新定义为区域级全栈量化码预测问题：Stage I用有限标量量化(FSQ)将完整MRI集编码为紧凑code map + 模态无关公共特征，Stage II从不完整模态预测code map(用grading loss保持量化空间平滑性)，在IXI和BraTS 2023上超越5种SOTA方法，生成的模态可接近真实数据的脑肿瘤分割性能。

**[Visualad Language-Free Zero-Shot Anomaly Detection Via Vision Transformer](visualad_language-free_zero-shot_anomaly_detection_via_vision_transformer.md)**

:   重新审视零样本异常检测（ZSAD）中文本分支的必要性，提出 VisualAD——一个纯视觉框架：在冻结 ViT 中插入两个可学习 token（anomaly/normal），配合 Spatial-Aware Cross-Attention 和 Self-Alignment Function，去掉文本编码器仍在 13 个工业+医学基准上取得 SOTA。

**[Weakly Supervised Teacher-Student Framework With Progressive Pseudo-Mask Refinem](weakly_supervised_teacher-student_framework_with_progressive_pseudo-mask_refinem.md)**

:   提出弱监督教师-学生框架，利用稀疏病理标注和 EMA 稳定的教师网络生成渐进式精炼伪掩码，结合置信度过滤、自适应融合和课程引导精炼策略，实现结直肠癌病理图像中腺体结构的高效分割。

**[X-Win Building Chest Radiograph World Model Via Predictive Sensing](x-win_building_chest_radiograph_world_model_via_predictive_sensing.md)**

:   提出 X-WIN 胸片世界模型，首次将 3D CT 空间知识融入 CXR 表征学习：通过学习预测 CT 在不同旋转角度下的 2D 投影来内化 3D 解剖结构，配合亲和力引导的对比对齐和结构保持域自适应，在 6 个 CXR 基准上通过线性探测取得 SOTA。
