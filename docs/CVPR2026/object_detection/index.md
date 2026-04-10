<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**📷 CVPR2026** · 共 **55** 篇

**[A Closer Look at Cross-Domain Few-Shot Object Detection: Fine-Tuning Matters and Parallel Decoder Helps](a_closer_look_at_cross-domain_few-shot_object_detection_fine-tuning_matters_and_.md)**

:   提出混合集成解码器(HED)和渐进微调策略用于跨域少样本目标检测，通过并行化部分解码层并随机初始化去噪查询引入预测多样性，在CD-FSOD/ODinW-13/RF100-VL三个基准上达到SOTA，不引入额外参数。

**[ABRA: Teleporting Fine-Tuned Knowledge Across Domains for Open-Vocabulary Object Detection](abra_teleporting_fine-tuned_knowledge_across_domains_for_open-vocabulary_object_.md)**

:   提出 ABRA 方法，将域知识与类别知识解耦，通过 Objectification 构建类无关域专家、SVFT 提取轻量类别残差、Orthogonal Procrustes 旋转对齐实现权重空间"传送"，在目标域完全无某些类别数据时仍可迁移这些类别的检测能力。

**[ABRA: Teleporting Fine-Tuned Knowledge Across Domains for Open-Vocabulary Object Detection](abra_teleporting_finetuned_knowledge_across_domain.md)**

:   将域适应建模为权重空间的SVD旋转对齐问题：分解域与类知识，通过闭式正交Procrustes解将源域类特定残差"传送"到无标注的目标域，实现零样本跨域类别检测。

**[Adaptive Auxiliary Prompt Blending for Target-Faithful Diffusion Generation](adaptive_auxiliary_prompt_blending_for_target-faithful_diffusion_generation.md)**

:   提出 Adaptive Auxiliary Prompt Blending (AAPB)，通过 Tweedie 公式推导闭式自适应混合系数，在每个去噪步动态平衡辅助锚定提示与目标提示的贡献，无需训练即可显著改善稀有概念生成和零样本图像编辑的语义准确性与结构保真度。

**[Anchoring and Rescaling Attention for Semantically Coherent Inbetweening](anchoring_and_rescaling_attention_for_semantically_coherent_inbetweening.md)**

:   提出 KAB（Keyframe-Anchored Attention Bias）和 ReTRo（Rescaled Temporal RoPE）两个无需训练的推理时方法，基于 Wan2.1 视频扩散模型解决稀疏关键帧下大运动生成式帧插值（GI）中的语义不忠、帧不一致和节奏不稳问题，并构建首个文本条件 GI 评估基准 TGI-Bench。

**[AR²-4FV: Anchored Referring and Re-identification for Long-Term Grounding in Fixed-View Videos](ar2-4fv_anchored_referring_and_re-identification_for_long-term_grounding_in_fixe.md)**

:   利用固定视角视频中背景结构的时不变性，构建离线 Anchor Bank + 在线 Anchor Map 作为语言-场景持久记忆，配合锚点引导的重入先验和 ReID-Gating 身份验证机制，实现目标遮挡/离场后的鲁棒重捕获，RCR 提升 10.3%、RCL 降低 24.2%。

**[Beautygrpo Aesthetic Alignment For Face Retouching Via Dynamic Path Guidance And](beautygrpo_aesthetic_alignment_for_face_retouching_via_dynamic_path_guidance_and.md)**

:   提出 BeautyGRPO，一个基于强化学习的人脸修图框架，通过构建细粒度偏好数据集 FRPref-10K 训练专用奖励模型，并设计动态路径引导（DPG）机制在随机探索与高保真之间取得平衡，实现与人类美学偏好对齐的自然修图效果。

**[Beyond Caption-Based Queries for Video Moment Retrieval](beyond_caption-based_queries_for_video_moment_retrieval.md)**

:   揭示了VMR中caption-based查询与真实用户搜索查询之间的巨大鸿沟，提出了三个搜索查询基准，并通过移除自注意力+查询Dropout两项架构修改来缓解DETR中的解码器查询坍塌问题，在多时刻搜索查询上提升高达21.83% mAPm。

**[Beyond Prompt Degradation: Prototype-Guided Dual-Pool Prompting for Incremental Object Detection](beyond_prompt_degradation_prototype-guided_dual-pool_prompting_for_incremental_o.md)**

:   提出 PDP 框架，通过双池提示解耦（共享池 + 私有池）和原型引导伪标签生成（PPG），解决增量目标检测中提示耦合与提示漂移导致的提示退化问题，在 COCO 和 VOC 上取得 SOTA。

**[Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval](beyond_semantic_search_towards_referential_anchoring_in_composed_image_retrieval.md)**

:   提出Object-Anchored Composed Image Retrieval（OACIR）新任务和OACIRR大规模基准（160K+四元组），以及AdaFocal框架通过上下文感知注意力调制器自适应地增强对锚定实例区域的关注，在实例级检索保真度上大幅超越现有方法。

**[Bridging Pixels and Words: Mask-Aware Local Semantic Fusion for Multimodal Media Verification](bridging_pixels_and_words_mask-aware_local_semantic_fusion_for_multimodal_media_.md)**

:   提出 MaLSF 框架，利用掩码-标签对作为语义锚点，通过双向跨模态验证（BCV）和层级语义聚合（HSA）模块实现主动式局部语义冲突检测，在 DGM4 和假新闻检测任务上取得 SOTA。

**[CD-Buffer: Complementary Dual-Buffer Framework for Test-Time Adaptation in Adverse Weather Object Detection](cd-buffer_complementary_dual-buffer_framework_for_test-time_adaptation_in_advers.md)**

:   提出 CD-Buffer 框架，通过统一的域差异度量驱动减性缓冲（通道抑制）和加性缓冲（轻量适配器补偿）的互补协作，实现跨不同严重程度恶劣天气条件下的鲁棒测试时目标检测适应。

**[CineSRD: Leveraging Visual, Acoustic, and Linguistic Cues for Open-World Visual Media Speaker Diarization](cinesrd_leveraging_visual_acoustic_and_linguistic_cues_for_open-world_visual_med.md)**

:   提出 CineSRD，一个免训练的多模态说话人分离框架，通过视觉锚点聚类进行说话人注册，结合音频语言模型进行说话人转换检测，解决影视作品中长视频、大量角色、音视频不同步等开放世界挑战。

**[CLCR: Cross-Level Semantic Collaborative Representation for Multimodal Learning](clcr_cross-level_semantic_collaborative_representation_for_multimodal_learning.md)**

:   提出 CLCR 框架，将每个模态特征组织为三层语义层级（浅/中/深），通过层内受控交换域（IntraCED）限制跨模态交互仅在共享子空间进行，通过层间协同聚合域（InterCAD）实现跨层自适应融合，解决多模态学习中的跨层语义不同步问题。

**[CompAgent: An Agentic Framework for Visual Compliance Verification](compagent_an_agentic_framework_for_visual_compliance_verification.md)**

:   提出 CompAgent，首个用于视觉合规验证的智能体框架——Planning Agent 根据合规策略动态选择视觉工具（目标检测、人脸分析、NSFW 检测等），Compliance Verification Agent 整合图像、工具输出和策略上下文进行多模态推理，无需训练即在 UnsafeBench 上超越 SOTA 10% 达 76% F1。

**[Da-Mamba Learning Domain-Aware State Space Model For Global-Local Alignment In D](da-mamba_learning_domain-aware_state_space_model_for_global-local_alignment_in_d.md)**

:   提出 DA-Mamba，一种 CNN-SSM 混合架构，通过 Image-Aware SSM（IA-SSM）和 Object-Aware SSM（OA-SSM）两个模块，以线性复杂度实现图像级和实例级的全局-局部域不变特征对齐，在四个域自适应检测基准上达到 SOTA。

**[Decoupling Vision and Language: Codebook Anchored Visual Adaptation](decoupling_vision_and_language_codebook_anchored_visual_adaptation.md)**

:   提出 CRAFT，通过离散 codebook 将视觉编码器与语言模型解耦，仅微调视觉编码器即可实现领域适配，且适配后的编码器可跨 LLM 架构无缝复用，在 10 个领域基准上平均提升 13.51%。

**[Detecting Unknown Objects via Energy-Based Separation for Open World Object Detection](detecting_unknown_objects_via_energy-based_separation.md)**

:   提出 DEUS 框架，通过 ETF 子空间未知目标分离（EUS）在几何正交的已知/未知子空间中利用能量分数有效分离已知、未知和背景提案，并设计能量基已知区分损失（EKD）减少增量学习中新旧类的交叉干扰，在 OWOD 基准上大幅提升未知目标召回率。

**[Detecting Unknown Objects via Energy-based Separation for Open World Object Detection](detecting_unknown_objects_via_energy-based_separation_for_open_world_object_dete.md)**

:   提出 DEUS 框架，通过 Simplex ETF 构建正交的已知/未知子空间并用能量分数引导特征分离（EUS），同时用能量区分损失（EKD）缓解新旧类别间的干扰，在 OWOD 基准上取得了大幅领先的未知目标召回率。

**[Does YOLO Really Need to See Every Training Image in Every Epoch?](does_yolo_really_need_to_see_every_training_image_in_every_epoch.md)**

:   提出 Anti-Forgetting Sampling Strategy (AFSS)，根据每张训练图像的学习充分度（min(Precision, Recall)）动态决定哪些图像参与训练、哪些可以跳过，实现 YOLO 系列检测器 1.43× 以上的训练加速同时保持甚至提升检测精度。

**[Drift-Resilient Temporal Priors for Visual Tracking](drift-resilient_temporal_priors_for_visual_tracking.md)**

:   提出 DTPTrack——一个轻量即插即用的时序建模模块，通过时序可靠性校准器（TRC）为历史帧分配可靠性分数过滤噪声，并通过时序引导合成器（TGS）将校准后的历史信息合成为动态先验 token 抑制跟踪漂移，在多个基准上达到 SOTA。

**[DualReg: Dual-Space Filtering and Reinforcement for Rigid Registration](dualreg_dual-space_filtering_and_reinforcement_for_rigid_registration.md)**

:   DualReg提出双空间配准范式，先用轻量级1-point RANSAC + 3-point RANSAC渐进过滤特征空间对应点，再基于过滤后的锚点构建几何代理点集进行双空间联合优化，在3DMatch上实现SOTA精度的同时比MAC快32倍。

**[Evaluating Few-Shot Pill Recognition Under Visual Domain Shift](evaluating_few-shot_pill_recognition_under_visual_domain_shift.md)**

:   本文从部署视角系统评估药丸识别在跨域few-shot条件下的泛化能力，揭示语义分类1-shot即饱和但定位/recall在重叠遮挡下急剧下降的解耦现象，并证明训练数据的视觉真实性远比数据量或shot数更关键。

**[Evaluating Few-Shot Pill Recognition Under Visual Domain Shift](evaluating_fewshot_pill_recognition_under_visual_d.md)**

:   从部署导向视角系统评估了小样本药丸识别在跨数据集域偏移下的表现，发现语义分类1-shot即可饱和(准确率>0.989)，但遮挡重叠场景下定位和召回急剧退化，训练数据的视觉真实性(多药丸、杂乱场景)是决定小样本泛化鲁棒性的主要因素。

**[Ew-Detr Evolving World Object Detection Via Incremental Low-Rank Detection Trans](ew-detr_evolving_world_object_detection_via_incremental_low-rank_detection_trans.md)**

:   提出 Evolving World Object Detection (EWOD) 范式及 EW-DETR 框架，通过增量 LoRA 适配器、查询范数物体性适配器和熵感知未知混合三个协同模块，在无样本回放条件下同时解决类别增量学习、域迁移适应和未知目标检测问题，FOGS 指标提升 57.24%。

**[EW-DETR: Evolving World Object Detection via Incremental Low-Rank DEtection TRansformer](ewdetr_evolving_world_object_detection.md)**

:   提出Evolving World Object Detection (EWOD)范式和EW-DETR框架，通过增量LoRA适配器、查询范数物体性适配器和熵感知未知混合三个模块，在无需存储旧数据的条件下同时解决类别增量学习、域迁移自适应和未知目标检测，FOGS指标较现有方法提升57.24%。

**[Falcon False-Negative Aware Learning Of Contrastive Negatives In Vision-Language](falcon_false-negative_aware_learning_of_contrastive_negatives_in_vision-language.md)**

:   提出 FALCON，一种**基于学习的 mini-batch 构造策略**，通过负样本挖掘调度器自适应平衡硬负样本与假负样本之间的权衡，显著提升视觉语言预训练的跨模态对齐质量。

**[Fixed Anchors Are Not Enough: Dynamic Retrieval and Persistent Homology for Dataset Distillation](fixed_anchors_are_not_enough_dynamic_retrieval_and_persistent_homology_for_datas.md)**

:   RETA解耦数据蒸馏中残差匹配的两个失败模式（fit-complexity gap和pull-to-anchor effect），通过动态检索连接（DRC）自适应选择real patch anchor并用持久同调拓扑对齐（PTA）保持类内多样性，在ImageNet-1K ResNet-18 IPC=50上达到64.3%（+3.1% vs FADRM）。

**[Foundation Model Priors Enhance Object Focus In Feature Space For Source-Free Ob](foundation_model_priors_enhance_object_focus_in_feature_space_for_source-free_ob.md)**

:   提出 FALCON-SFOD 框架，通过基础模型（OV-SAM）生成的类别无关二值掩码正则化检测器特征空间（SPAR），结合不平衡感知的噪声鲁棒伪标签损失（IRPL），在无源域目标检测中增强目标聚焦表征，多个基准上达到 SOTA。

**[Fourier Angle Alignment for Oriented Object Detection in Remote Sensing](fourier_angle_alignment_for_oriented_object_detection_in_remote_sensing.md)**

:   利用傅里叶旋转等变性在频域估计并对齐目标方向，提出 FAAFusion（解决 Neck 层方向不一致）和 FAA Head（解决检测头分类-回归任务冲突）两个即插即用模块，在 DOTA 和 HRSC2016 上达到新 SOTA。

**[Just-In-Time Training-Free Spatial Acceleration For Diffusion Transformers](just-in-time_training-free_spatial_acceleration_for_diffusion_transformers.md)**

:   提出 Just-in-Time (JiT) 框架，通过在空间域动态选择稀疏 anchor token 驱动生成 ODE 演化，并设计确定性 micro-flow 保证新 token 无缝激活，在 FLUX.1-dev 上实现最高 7× 加速且几乎无损。

**[Learning Multi-Modal Prototypes for Cross-Domain Few-Shot Object Detection](learning_multi-modal_prototypes_for_cross-domain_few-shot_object_detection.md)**

:   提出双分支框架 LMP，在 GroundingDINO 基础上引入视觉原型分支（正类原型+硬负原型），与文本分支联合训练并集成推理，在跨域少样本目标检测中取得 SOTA。

**[MoKus: Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization](mokus_leveraging_cross-modal_knowledge_transfer_for_knowledge-aware_concept_cust.md)**

:   发现并利用跨模态知识迁移现象——修改 LLM 文本编码器中的知识可自然迁移到视觉生成，提出 MoKus 两阶段框架（视觉概念学习 + 文本知识更新）实现知识感知的概念定制。

**[MoKus: Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization](mokus_leveraging_crossmodal_knowledge_transfer_for.md)**

:   提出"知识感知概念定制"新任务，发现LLM文本编码器中的知识编辑可以自然迁移到视觉生成模态（跨模态知识迁移），基于此提出MoKus框架：先用LoRA微调将稀有token绑定为视觉概念的锚表征，再通过知识编辑技术将多条自然语言知识高效映射到锚表征上，每条知识更新仅需约7秒。

**[MRD: Multi-resolution Retrieval-Detection Fusion for High-Resolution Image Understanding](mrd_multi-resolution_retrieval-detection_fusion_for_high-resolution_image_unders.md)**

:   提出 MRD，一个 training-free 的多分辨率检索-检测融合框架，通过多分辨率语义融合缓解目标碎片化，结合开放词汇检测器抑制背景干扰，显著提升 MLLM 对高分辨率图像的理解能力。

**[Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models](neighbor_grpo_contrastive_ode_policy_optimization_aligns_flow_models.md)**

:   重新解释 SDE-based GRPO 为距离优化/对比学习，提出 Neighbor GRPO——完全绕过 SDE 转换，通过扰动 ODE 初始噪声构建邻域候选轨迹 + softmax 距离代理策略实现策略梯度优化，保留确定性 ODE 采样的所有优势。

**[PHAC: Promptable Human Amodal Completion](phac_promptable_human_amodal_completion.md)**

:   提出可提示人体非模态补全（PHAC）新任务，通过基于点的用户提示（姿态/边界框）配合 ControlNet 注入条件信号，并设计基于修复的精炼模块保留可见区域外观，实现高质量、可控的遮挡人体图像补全。

**[Pixels Don't Lie (But Your Detector Might): Bootstrapping MLLM-as-a-Judge for Trustworthy Deepfake Detection and Reasoning Supervision](pixels_dont_lie_but_your_detector_might_bootstrapping_mllm-as-a-judge_for_trustw.md)**

:   提出 DeepfakeJudge 框架，通过 bootstrapped generator-evaluator 流程将人类标注的推理监督扩展为大规模结构化评分数据，训练出 3B/7B 视觉语言模型作为 deepfake 检测推理质量的自动评判者，在 pointwise 和 pairwise 评估上均达到与人类高度一致的水平。

**[Prompt-Free Universal Region Proposal Network](prompt-free_universal_region_proposal_network.md)**

:   无需文本/图像提示的通用区域提案网络，用5% COCO数据训练零样本泛化到19个跨域数据集

**[RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset](radar_closed-loop_robotic_data_generation_via_semantic_planning_and_autonomous_c.md)**

:   提出 RADAR 全自动闭环机器人数据采集框架，通过 VLM 语义规划、GNN 策略执行、VQA 成功评估和 LIFO 因果环境重置四模块协同，仅需 2-5 个人类演示即可在无人干预下持续生成高质量操作数据，在仿真长序列任务上达 90% 成功率。

**[ReHARK: Refined Hybrid Adaptive RBF Kernels for Robust One-Shot Vision-Language Adaptation](rehark_refined_hybrid_adaptive_rbf_kernels_for_robust_one-shot_vision-language_a.md)**

:   提出 ReHARK 框架，通过混合语义-视觉先验构建、支撑集增强、自适应分布校正和多尺度 RBF 核集成四阶段精炼管道，在 11 个基准上实现 65.83% 的单样本适应 SOTA 准确率，显著超越 Tip-Adapter 和 ProKeR。

**[Remedying Target-Domain Astigmatism for Cross-Domain Few-Shot Object Detection](remedying_target-domain_astigmatism_for_cross-domain_few-shot_object_detection.md)**

:   发现跨域少样本检测中的散光现象，受中央凹视觉启发提出PPR+NCM+TSA三模块矫正，6个基准SOTA

**[Sdf-Net Structure-Aware Disentangled Feature Learning For Opticall-Sar Ship Re-I](sdf-net_structure-aware_disentangled_feature_learning_for_opticall-sar_ship_re-i.md)**

:   提出 SDF-Net，利用船舶刚体几何结构作为跨模态不变锚点，在中间层提取梯度能量强制结构一致性，在终端层解耦模态共享/特定特征并通过加法残差融合，在 HOSS-ReID 上取得 SOTA（All mAP 60.9%，超 TransOSS 3.5%）。

**[Shape-Of-You Fused Gromov-Wasserstein Optimal Transport For Semantic Corresponde](shape-of-you_fused_gromov-wasserstein_optimal_transport_for_semantic_corresponde.md)**

:   将语义对应问题重新建模为 Fused Gromov-Wasserstein (FGW) 最优传输问题，利用 3D 基础模型提供的几何结构约束来生成全局一致的伪标签，解决了传统最近邻匹配因局部性和 2D 外观歧义导致的几何不一致问题。

**[Show, Don't Tell: Detecting Novel Objects by Watching Human Videos](show_dont_tell_detecting_novel_objects_by_watching.md)**

:   提出"Show, Don't Tell"范式：通过观看人类演示视频，自动构建新物体标注数据集（SODC），训练轻量级定制检测器（MOD），完全绕过语言描述和prompt engineering，在真实机器人分拣任务上成功部署。

**[Show, Don't Tell: Detecting Novel Objects by Watching Human Videos](show_dont_tell_detecting_novel_objects_by_watching_human_videos.md)**

:   提出 "Show, Don't Tell" 范式：通过观看人类演示视频自动创建训练数据集，以自监督方式训练定制化（bespoke）目标检测器来识别新颖物体，完全绕过语言描述和提示工程，在真实机器人操作任务中显著优于 SOTA 检测方法。

**[SLICE: Semantic Latent Injection via Compartmentalized Embedding for Image Watermarking](slice_semantic_latent_injection_via_compartmentalized_embedding_for_image_waterm.md)**

:   提出 SLICE 语义水印框架，将图像语义分解为主体/环境/动作/细节四个因子并绑定到初始高斯噪声的不同空间分区，实现不仅可检测水印存在还可定位语义篡改的三状态验证机制，对最强 CSI 攻击的攻击成功率仅 19%（SEAL 为 81%）。

**[Small Target Detection Based on Mask-Enhanced Attention Fusion of Visible and Infrared Remote Sensing Images](small_target_detection_based_on_mask-enhanced_attention_fusion_of_visible_and_in.md)**

:   提出 ESM-YOLO+，一个轻量级可见光-红外融合小目标检测网络，通过 Mask-Enhanced Attention Fusion (MEAF) 模块实现像素级跨模态自适应融合，并引入训练时结构表示增强提升空间判别力，在 VEDAI 上达 84.71% mAP 同时参数量减少 93.6%。

**[Specificity-Aware Reinforcement Learning For Fine-Grained Open-World Classificat](specificity-aware_reinforcement_learning_for_fine-grained_open-world_classificat.md)**

:   提出 SpeciaRL——一种特异性感知的强化学习框架，通过基于在线 rollout 最佳预测的动态奖励信号，引导推理型大型多模态模型在开放世界细粒度图像分类中同时提升预测的特异性和正确性。

**[Spiraldiff Spiral Diffusion With Lora For Rgb-To-Raw Conversion Across Cameras](spiraldiff_spiral_diffusion_with_lora_for_rgb-to-raw_conversion_across_cameras.md)**

:   提出 SpiralDiff，一种面向 RGB-to-RAW 转换的扩散框架，通过信号依赖的噪声加权策略适应不同像素强度区域的重建难度，并引入 CamLoRA 模块实现单一模型跨多相机的轻量适配。

**[Stake the Points: Structure-Faithful Instance Unlearning](stake_the_points_structure-faithful_instance_unlearning.md)**

:   提出 Structguard，通过语义锚点（semantic anchors）保持遗忘过程中保留实例间的语义关系结构，避免结构性崩塌，在图像分类/人脸识别/检索三任务上平均提升 32.9%/19.3%/22.5%。

**[The Cote Score A Decomposable Framework For Evaluating Document Layout Analysis ](the_cote_score_a_decomposable_framework_for_evaluating_document_layout_analysis_.md)**

:   提出面向文档布局分析（DLA）的可分解评估框架 COTe（Coverage, Overlap, Trespass, Excess），以及结构语义单元 SSU，相比传统 IoU/mAP/F1 能更准确地反映页面解析质量，并揭示不同模型的特异性失败模式。

**[TIACam: Text-Anchored Invariant Feature Learning with Auto-Augmentation for Camera-Robust Zero-Watermarking](tiacam_text-anchored_invariant_feature_learning_with_auto-augmentation_for_camer.md)**

:   提出 TIACam 框架，通过可学习自动增强器模拟相机失真、文本锚定跨模态对抗训练学习不变特征、零水印头在特征空间绑定消息，实现无需修改图像像素的相机鲁棒零水印方案，在屏幕翻拍/打印翻拍/截图三种真实场景下均达到 SOTA 提取精度。

**[Token Reduction Via Local And Global Contexts Optimization For Efficient Video L](token_reduction_via_local_and_global_contexts_optimization_for_efficient_video_l.md)**

:   提出 AOT 框架，通过建立局部-全局 token anchors 并利用最优传输（Optimal Transport）在帧内和帧间两级聚合被裁剪/合并 token 的语义信息，实现 training-free 的视频 token 压缩，在裁剪 90% token 的情况下仍保留 97.6% 的原始性能。

**[Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods](training-free_detection_of_generated_videos_via_spatial-temporal_likelihoods.md)**

:   提出 STALL，一种无需训练的零样本生成视频检测器，通过在白化嵌入空间中联合建模逐帧空间似然和帧间时序似然，仅依赖真实视频校准即可实现对多种生成模型的鲁棒检测。
