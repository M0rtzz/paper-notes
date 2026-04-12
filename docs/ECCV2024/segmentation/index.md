---
title: >-
  ECCV2024 语义分割方向 19篇论文解读
description: >-
  19篇ECCV2024 语义分割方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🎞️ ECCV2024** · 共 **19** 篇

**[A Semantic Space Is Worth 256 Language Descriptions Make Str](a_semantic_space_is_worth_256_language_descriptions_make_str.md)**

:   ProLab 用 LLM 生成类别的常识性描述，通过句子嵌入和 K-Means 聚类将其压缩为 256 个可解释的描述性属性，构建属性级多热标签空间替代传统 one-hot 类别标签来监督分割模型，在五个经典基准上一致超越类别级监督且涌现出域外泛化能力。

**[A Simple Latent Diffusion Approach For Panoptic Segmentation And Mask Inpainting](a_simple_latent_diffusion_approach_for_panoptic_segmentation_and_mask_inpainting.md)**

:   基于Stable Diffusion构建了一个极简的潜在扩散分割框架LDMSeg，通过浅层自编码器将分割mask压缩到潜空间、再训练图像条件扩散模型来生成全景分割结果，避免了传统方法中的目标检测模块、匈牙利匹配和复杂后处理，并天然支持mask inpainting和多任务扩展。

**[Actionvos Actions As Prompts For Video Object Segmentation](actionvos_actions_as_prompts_for_video_object_segmentation.md)**

:   提出ActionVOS——一种以人类动作叙述作为额外语言提示的Referring Video Object Segmentation新设定，通过无参数的动作感知标注模块生成伪标签，并设计动作引导的focal loss来抑制假阳性，在VISOR上将非活跃物体的误分割降低35.6% mIoU，同时在VOST/VSCOS上对状态变化物体的分割提升3.0% mIoU。

**[Active Coarsetofine Segmentation Of Moveable Parts From Real](active_coarsetofine_segmentation_of_moveable_parts_from_real.md)**

:   提出首个面向真实室内场景RGB图像中可运动部件实例分割的主动学习框架，通过姿态感知masked attention网络实现由粗到细的分割，仅需人工标注11.45%的图像即可获得全量验证的高质量分割结果，相比最优非AL方法节省60%人工时间。

**[Adalog Post-Training Quantization For Vision Transformers With Adaptive Logarith](adalog_post-training_quantization_for_vision_transformers_with_adaptive_logarith.md)**

:   提出自适应对数底量化器AdaLog，通过可搜索的对数底替代固定log₂/log√2量化器来处理ViT中post-Softmax和post-GELU激活的幂律分布，并设计快速渐进组合搜索(FPCS)策略高效确定量化超参，在极低比特(3/4-bit)下显著优于现有ViT PTQ方法。

**[Brushnet A Plug-And-Play Image Inpainting Model With Decomposed Dual-Branch Diff](brushnet_a_plug-and-play_image_inpainting_model_with_decomposed_dual-branch_diff.md)**

:   提出 BrushNet，一种即插即用的双分支扩散模型图像修复架构，通过将遮罩图像特征提取与图像生成解耦到独立分支，实现逐层像素级特征注入，在图像质量、遮罩区域保持和文本对齐三方面全面超越已有方法。

**[Cola Conditional Dropout And Language-Driven Robust Dual-Modal Salient Object De](cola_conditional_dropout_and_language-driven_robust_dual-modal_salient_object_de.md)**

:   提出 CoLA 框架，通过语言驱动的质量评估（LQA）和条件性 Dropout（CD）两个核心模块，首次在双模态显著性目标检测中同时解决噪声输入和模态缺失两大鲁棒性问题。

**[Colormae Exploring Data-Independent Masking Strategies In Masked Autoencoders](colormae_exploring_data-independent_masking_strategies_in_masked_autoencoders.md)**

:   提出 ColorMAE，通过对随机噪声施加不同频域滤波器生成具有空间与语义先验的数据无关遮罩模式，在不增加任何参数和计算开销的前提下，显著提升 MAE 的下游任务表现，尤其在语义分割任务上相比随机遮罩提升 2.72 mIoU。

**[Controlnet Improving Conditional Controls With Efficient Consistency Feedback](controlnet_improving_conditional_controls_with_efficient_consistency_feedback.md)**

:   提出 ControlNet++，通过像素级循环一致性损失显式优化条件可控生成质量：用预训练判别模型从生成图像中提取条件并与输入条件对齐，并设计高效单步去噪 reward 策略避免多步采样的巨大显存开销，在分割掩码、边缘、深度等多种条件控制下显著提升可控性（如分割 mIoU +11.1%）。

**[Cores Orchestrating The Dance Of Reasoning And Segmentation](cores_orchestrating_the_dance_of_reasoning_and_segmentation.md)**

:   提出 CoReS（Chains of Reasoning and Segmenting），一种双链结构的多模态思维链框架，通过推理链和分割链的层次化协作，结合 in-context 引导策略，实现对复杂推理文本中目标物体的渐进式精确分割，在 ReasonSeg 数据集上超越 LISA 6.5%。

**[Cpm Class-Conditional Prompting Machine For Audio-Visual Segmentation](cpm_class-conditional_prompting_machine_for_audio-visual_segmentation.md)**

:   提出 CPM（Class-conditional Prompting Machine），通过结合类无关查询与基于 GMM 采样的类条件查询来增强 Mask2Former 在音视频分割中的二部图匹配稳定性和跨模态注意力效力，同时设计音频条件提示（ACP）、视觉条件提示（VCP）和提示对比学习（PCL）三个辅助任务，在 AVSBench 和 VPO 基准上达到 SOTA。

**[Cs2K Class-Specific And Class-Shared Knowledge Guidance For Incremental Semantic](cs2k_class-specific_and_class-shared_knowledge_guidance_for_incremental_semantic.md)**

:   提出 Cs2K 框架，从类别特有知识（原型引导伪标签 + 原型引导类别适应）和类别共享知识（权重引导选择性整合）两个方面协同缓解增量语义分割中的灾难性遗忘与新类欠拟合问题。

**[Dataset Enhancement With Instance-Level Augmentations](dataset_enhancement_with_instance-level_augmentations.md)**

:   提出一种基于预训练扩散模型的实例级数据增强方法，通过在保持原始标注不变的前提下逐个重绘图像中的目标实例，显著提升了显著性目标检测、语义分割和目标检测的性能，同时支持数据匿名化。

**[Deep Nets With Subsampling Layers Unwittingly Discard Useful Activations At Test](deep_nets_with_subsampling_layers_unwittingly_discard_useful_activations_at_test.md)**

:   发现深度网络中下采样层在默认前向传播中丢弃了大量有用激活，提出一个搜索+聚合框架在测试时利用这些被丢弃的激活图来提升分类和分割性能，与传统TTA方法正交互补。

**[Densenets Reloaded Paradigm Shift Beyond Resnets And Vits](densenets_reloaded_paradigm_shift_beyond_resnets_and_vits.md)**

:   重新审视 DenseNet 的密集拼接连接（concatenation shortcut），通过系统性现代化改造（加宽减深、现代化 block、扩大中间维度、更多 transition 层等），提出 RDNet（Revitalized DenseNet），在 ImageNet-1K 上超越 Swin Transformer、ConvNeXt、DeiT-III，证明了拼接连接作为一种被低估的范式具有强大潜力。

**[Eaformer Scene Text Segmentation With Edge-Aware Transformers](eaformer_scene_text_segmentation_with_edge-aware_transformers.md)**

:   提出边缘感知Transformer（EAFormer），通过文本边缘提取器过滤非文本区域边缘、对称交叉注意力在编码器中融合文本边缘信息，显著提升文字边缘区域的分割精度，并重标注COCO_TS和MLT_S数据集以实现更公平评估。

**[Early Preparation Pays Off New Classifier Pre-Tuning For Class Incremental Seman](early_preparation_pays_off_new_classifier_pre-tuning_for_class_incremental_seman.md)**

:   提出NeST（New claSsifier pre-Tuning）方法，在正式训练前通过学习从所有旧分类器到新分类器的线性变换来初始化新分类器权重，并设计基于跨任务类别相似性的变换矩阵初始化策略，在Pascal VOC和ADE20K上显著提升多种CISS方法的性能。

**[Rotary Position Embedding For Vision Transformer](rotary_position_embedding_for_vision_transformer.md)**

:   本文系统研究了将 RoPE（Rotary Position Embedding）从1D语言模型扩展到2D视觉任务的方法，提出 RoPE-Mixed（混合可学习频率）替代传统的 Axial 频率分配，在 ViT 和 Swin Transformer 上实现了显著的分辨率外推性能提升，在 ImageNet 分类、COCO 检测和 ADE20k 分割上均带来一致增益。

**[Visa Reasoning Video Object Segmentation Via Large Language Models](visa_reasoning_video_object_segmentation_via_large_language_models.md)**

:   提出 ReasonVOS 新任务和 VISA 模型，利用多模态 LLM 的世界知识推理能力实现基于隐式文本查询的视频目标分割与跟踪。
