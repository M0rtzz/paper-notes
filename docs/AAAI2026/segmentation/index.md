<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🤖 AAAI2026** · 共 **20** 篇

**[3DTeethSAM: Taming SAM2 for 3D Teeth Segmentation](3dteethsam_taming_sam2_for_3d_teeth_segmentation.md)**

:   将SAM2基础模型迁移到3D牙齿分割任务，通过多视角渲染将3D mesh转为2D图像、设计三个轻量适配器（Prompt生成器、Mask精化器、Mask分类器）和可变形全局注意力插件（DGAP）来解决自动提示、边界精化和语义分类问题，在Teeth3DS上以91.90% T-mIoU刷新SOTA。

**[A²LC: Active and Automated Label Correction for Semantic Segmentation](a2lc_active_and_automated_label_correction_for_semantic_segm.md)**

:   提出 A²LC 框架，在传统主动标签校正（人工逐一纠错）的基础上增加一个自动校正阶段（Label Correction Module），利用标注员的反馈自动修正相似的错误mask，并设计自适应平衡采集函数缓解类别不平衡，在 Cityscapes 上仅用 20% 预算即超越前 SOTA，同等预算下 mIoU 提升 27.23%。

**[Adaptive Morph-Patch Transformer for Aortic Vessel Segmentation](adaptive_morph-patch_transformer_for_aortic_vessel_segmentat.md)**

:   提出 Morph-Patch Transformer (MPT)，通过基于速度场的自适应 patch 划分策略生成形态感知 patch（保持血管拓扑完整性），并引入语义聚类注意力（SCA）动态聚合语义相似 patch 的特征，在 AVT、AortaSeg24 和 TBAD 三个主动脉分割数据集上均达 SOTA。

**[Breaking the Stealth-Potency Trade-off in Clean-Image Backdoors with Generative Trigger Optimization](breaking_the_stealth-potency_trade-off_in_clean-image_backdoors_with_generative_.md)**

:   提出 Generative Clean-Image Backdoors (GCB)，通过 Conditional InfoGAN (C-InfoGAN) 自动发现图像中天然存在且与分类任务无关的特征作为后门触发器，以极低投毒率（≤0.5%）实现高攻击成功率（≥90% ASR）且几乎不损伤干净准确率（CA drop ≤1%），首次打破了 clean-image backdoor 中隐蔽性与攻击力的固有矛盾。

**[Bridging Granularity Gaps: Hierarchical Semantic Learning for Cross-Domain Few-Shot Segmentation](bridging_granularity_gaps_hierarchical_semantic_learning_for_cross-domain_few-sh.md)**

:   提出 HSL 框架，通过双重风格随机化 (DSR)、层次语义挖掘 (HSM) 和原型置信度调制阈值 (PCMT) 三个模块，解决跨域少样本分割中源域和目标域之间的**分割粒度差异**问题，在四个目标域数据集上达到 SOTA。

**[Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation](causal-tune_mining_causal_factors_from_vision_foundation_mod.md)**

:   提出Causal-Tune，从因果视角分析VFM特征中的artifacts，利用DCT频域分解+高斯带通滤波分离因果/非因果因素，结合因果感知可学习token在频域精化特征，在Cityscapes→ACDC跨域分割中平均提升+2.4% mIoU（Snow场景+4.8%），仅需单卡RTX3090/14GB训练。

**[Do We Need Perfect Data? Leveraging Noise for Domain Generalized Segmentation](do_we_need_perfect_data_leveraging_noise_for_domain_generalized_segmentation.md)**

:   提出 FLEX-Seg 框架，将扩散模型合成数据中图像与语义掩码之间固有的**边界不对齐**(misalignment)转化为学习鲁棒表示的机会，通过粒度自适应原型 (GAP)、不确定性边界强调 (UBE) 和难度感知采样 (HAS) 三个模块，在域泛化语义分割任务上取得 SOTA。

**[EAGLE: Episodic Appearance- and Geometry-Aware Memory for Unified 2D-3D Visual Query Localization](eagle_episodic_appearance-_and_geometry-aware_memory_for_unified_2d-3d_visual_qu.md)**

:   提出 EAGLE 框架，借鉴鸟类记忆巩固机制，通过外观感知元学习记忆 (AMM) 驱动的分割分支与几何感知定位记忆 (GLM) 驱动的跟踪分支协同工作，结合 VGGT 实现高效的 2D-3D 统一视觉查询定位，在 Ego4D-VQ 基准上达到 SOTA。

**[Empowering DINO Representations for Underwater Instance Segmentation via Aligner and Prompter](empowering_dino_representations_for_underwater_instance_segmentation_via_aligner.md)**

:   首次将 DINOv2 引入水下实例分割任务，通过 AquaStyle Aligner（傅里叶频域风格注入）和 ObjectPrior Prompter（二值掩码先验提示）两个模块实现高效领域适配，在 UIIS 和 USIS10K 数据集上以更少参数大幅超越 SAM 基方法。

**[Empowering Semantic-Sensitive Underwater Image Enhancement with VLM](empowering_semantic-sensitive_underwater_image_enhancement_with_vlm.md)**

:   利用 VLM 生成空间语义引导图，通过 cross-attention 注入和语义对齐损失的双重引导机制，赋予水下图像增强网络语义感知能力，使增强结果同时有利于人类感知和下游检测/分割任务。

**[From Attribution to Action: Jointly ALIGNing Predictions and Explanations](from_attribution_to_action_jointly_aligning_predictions_and_explanations.md)**

:   提出 ALIGN 框架，通过联合训练可学习掩码生成器（masker）和分类器，迭代对齐模型归因图与任务相关区域掩码，同时提升预测准确性和可解释性，在 VLCS 和 Terra Incognita 域泛化基准上超越 6 个强基线。

**[Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts](generalizable_slum_detection_from_satellite_imagery_with_mixture-of-experts.md)**

:   提出 GRAM（Generalized Region-Aware Mixture-of-Experts），一个两阶段测试时自适应框架：第一阶段用 MoE 架构在12个城市的百万级卫星图像上训练区域特化专家，第二阶段通过跨区域预测一致性筛选可靠伪标签进行自训练，实现对未见非洲城市的贫民窟分割泛化。

**[Guideline-Consistent Segmentation via Multi-Agent Refinement](guideline-consistent_segmentation_via_multi-agent_refinement.md)**

:   提出一个免训练的多智能体框架，通过 Worker（分割执行）和 Supervisor（指南验证）的迭代循环，配合 RL 自适应停止策略，实现严格遵循复杂文本指南的语义分割，在 Waymo 和 ReasonSeg 上分别超越 SOTA 8.61 和 5.5 gIoU。

**[InfoCLIP: Bridging Vision-Language Pretraining and Open-Vocabulary Semantic Segmentation via Information-Theoretic Alignment Transfer](infoclip_bridging_vision-language_pretraining_and_open-vocab.md)**

:   提出InfoCLIP，基于信息论视角设计信息瓶颈压缩和互信息蒸馏两个目标，在CLIP微调过程中去除预训练pixel-text对齐中的噪声并保留语义对齐知识，在6个开放词汇语义分割测试集上全面超越SOTA（A-847: 16.6, A-150: 38.5, PC-59: 63.5 mIoU），且仅增加0.53M参数和极少计算开销。

**[JoDiffusion: Jointly Diffusing Image with Pixel-Level Annotations for Semantic Segmentation Promotion](jodiffusion_jointly_diffusing_image_with_pixel-level_annotations_for_semantic_se.md)**

:   提出JoDiffusion框架，通过在潜在空间中联合扩散图像与像素级标注掩码，首次实现仅基于文本提示同时生成语义一致的图像-标注对，在Pascal VOC、COCO和ADE20K上显著超越现有Image2Mask和Mask2Image方法。

**[LWGANet: Addressing Spatial and Channel Redundancy in Remote Sensing Visual Tasks with Light-Weight Grouped Attention](lwganet_addressing_spatial_and_channel_redundancy_in_remote_sensing_visual_tasks.md)**

:   针对遥感图像中的空间冗余（大面积均质背景）和通道冗余（极端尺度变化导致单一特征空间低效）问题，提出 LWGANet 轻量化骨干，通过 Top-K 稀疏全局特征交互（TGFI）和异构分组注意力（LWGA）模块实现高效多尺度特征表示，在 12 个数据集 4 类遥感任务上达到 SOTA。

**[Multigranular Evaluation for Brain Visual Decoding](multigranular_evaluation_for_brain_visual_decoding.md)**

:   提出 BASIC 多粒度评估框架，从结构（分割 mask 匹配）、推理（对象/属性/关系语义图）和上下文（场景叙事一致性）三个维度统一评估脑视觉解码质量，解决现有指标饱和、缺乏神经科学基础、无法区分模型差异的问题。

**[OmniVDiff: Omni Controllable Video Diffusion for Generation and Understanding](omnivdiff_omni_controllable_video_diffusion_for_generation_and_understanding.md)**

:   提出 OmniVDiff，一个统一的可控视频扩散框架，通过将多种视觉模态（RGB、深度、分割、Canny）在颜色空间中联合建模，并引入自适应模态控制策略（AMCS），在单一扩散模型中同时支持文本条件生成、X 条件生成和视频理解三种任务，在 VBench 上达到 SOTA。

**[Otter: Mitigating Background Distractions of Wide-Angle Few-Shot Action Recognition with Enhanced RWKV](otter_mitigating_background_distractions_of_wide-angle_few-shot_action_recogniti.md)**

:   针对广角视频中小样本动作识别的背景干扰问题（主体占比小、时序关系退化），提出基于增强 RWKV 的 Otter 框架，通过复合分割模块（CSM）突出主体和时序重建模块（TRM）恢复时序关系，在 SSv2/Kinetics/UCF101/HMDB51 等基准上达到 SOTA。

**[Segment and Matte Anything in a Unified Model (SAMA)](segment_and_matte_anything_in_a_unified_model.md)**

:   提出SAMA——一种SAM的轻量级扩展框架，通过多视图局部编码器(MVLE)捕获细粒度局部特征、局部化适配器(Local-Adapter)将局部细节注入解码过程，以及双任务预测头，仅增加1.8%参数即可在统一模型中同时实现高质量交互式分割和Alpha Matting，在DIS-5K和多个Matting基准上达到SOTA。
