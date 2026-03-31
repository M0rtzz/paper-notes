<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🎞️ ECCV2024** · 共 **19** 篇

**[A Semantic Space is Worth 256 Language Descriptions: Make Stronger Segmentation Models with Descriptive Properties](a_semantic_space_is_worth_256_language_descriptions_make_str.md)**

:   ProLab 用 LLM 生成类别的常识性描述，通过句子嵌入和 K-Means 聚类将其压缩为 256 个可解释的描述性属性，构建属性级多热标签空间替代传统 one-hot 类别标签来监督分割模型，在五个经典基准上一致超越类别级监督且涌现出域外泛化能力。

**[A Simple Latent Diffusion Approach for Panoptic Segmentation and Mask Inpainting](a_simple_latent_diffusion_approach_for_panoptic_segmentation_and_mask_inpainting.md)**

:   基于Stable Diffusion构建了一个极简的潜在扩散分割框架LDMSeg，通过浅层自编码器将分割mask压缩到潜空间、再训练图像条件扩散模型来生成全景分割结果，避免了传统方法中的目标检测模块、匈牙利匹配和复杂后处理，并天然支持mask inpainting和多任务扩展。

**[ActionVOS: Actions as Prompts for Video Object Segmentation](actionvos_actions_as_prompts_for_video_object_segmentation.md)**

:   提出ActionVOS——一种以人类动作叙述作为额外语言提示的Referring Video Object Segmentation新设定，通过无参数的动作感知标注模块生成伪标签，并设计动作引导的focal loss来抑制假阳性，在VISOR上将非活跃物体的误分割降低35.6% mIoU，同时在VOST/VSCOS上对状态变化物体的分割提升3.0% mIoU。

**[Active Coarse-to-Fine Segmentation of Moveable Parts from Real Images](active_coarsetofine_segmentation_of_moveable_parts_from_real.md)**

:   提出首个面向真实室内场景RGB图像中可运动部件实例分割的主动学习框架，通过姿态感知masked attention网络实现由粗到细的分割，仅需人工标注11.45%的图像即可获得全量验证的高质量分割结果，相比最优非AL方法节省60%人工时间。

**[AdaLog: Post-Training Quantization for Vision Transformers with Adaptive Logarithm Quantizer](adalog_post-training_quantization_for_vision_transformers_with_adaptive_logarith.md)**

:   提出自适应对数底量化器AdaLog，通过可搜索的对数底替代固定log₂/log√2量化器来处理ViT中post-Softmax和post-GELU激活的幂律分布，并设计快速渐进组合搜索(FPCS)策略高效确定量化超参，在极低比特(3/4-bit)下显著优于现有ViT PTQ方法。

**[BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion](brushnet_a_plug-and-play_image_inpainting_model_with_decomposed_dual-branch_diff.md)**

:   提出 BrushNet，一种即插即用的双分支扩散模型图像修复架构，通过将遮罩图像特征提取与图像生成解耦到独立分支，实现逐层像素级特征注入，在图像质量、遮罩区域保持和文本对齐三方面全面超越已有方法。

**[CoLA: Conditional Dropout and Language-Driven Robust Dual-Modal Salient Object Detection](cola_conditional_dropout_and_language-driven_robust_dual-modal_salient_object_de.md)**

:   提出 CoLA 框架，通过语言驱动的质量评估（LQA）和条件性 Dropout（CD）两个核心模块，首次在双模态显著性目标检测中同时解决噪声输入和模态缺失两大鲁棒性问题。

**[ColorMAE: Exploring Data-Independent Masking Strategies in Masked AutoEncoders](colormae_exploring_data-independent_masking_strategies_in_masked_autoencoders.md)**

:   提出 ColorMAE，通过对随机噪声施加不同频域滤波器生成具有空间与语义先验的数据无关遮罩模式，在不增加任何参数和计算开销的前提下，显著提升 MAE 的下游任务表现，尤其在语义分割任务上相比随机遮罩提升 2.72 mIoU。

**[ControlNet++: Improving Conditional Controls with Efficient Consistency Feedback](controlnet_improving_conditional_controls_with_efficien.md)**

:   提出 ControlNet++，通过预训练判别模型提取生成图像的条件并优化像素级循环一致性损失来显式提升可控生成的精度，同时提出高效单步去噪奖励策略避免多步采样的巨大开销。

**[ControlNet++: Improving Conditional Controls with Efficient Consistency Feedback](controlnet_improving_conditional_controls_with_efficient_consistency_feedback.md)**

:   提出 ControlNet++，通过像素级循环一致性损失显式优化条件可控生成质量：用预训练判别模型从生成图像中提取条件并与输入条件对齐，并设计高效单步去噪 reward 策略避免多步采样的巨大显存开销，在分割掩码、边缘、深度等多种条件控制下显著提升可控性（如分割 mIoU +11.1%）。

**[CoReS: Orchestrating the Dance of Reasoning and Segmentation](cores_orchestrating_the_dance_of_reasoning_and_segmentation.md)**

:   提出 CoReS（Chains of Reasoning and Segmenting），一种双链结构的多模态思维链框架，通过推理链和分割链的层次化协作，结合 in-context 引导策略，实现对复杂推理文本中目标物体的渐进式精确分割，在 ReasonSeg 数据集上超越 LISA 6.5%。

**[CPM: Class-Conditional Prompting Machine for Audio-Visual Segmentation](cpm_class-conditional_prompting_machine_for_audio-visual_segmentation.md)**

:   提出 CPM（Class-conditional Prompting Machine），通过结合类无关查询与基于 GMM 采样的类条件查询来增强 Mask2Former 在音视频分割中的二部图匹配稳定性和跨模态注意力效力，同时设计音频条件提示（ACP）、视觉条件提示（VCP）和提示对比学习（PCL）三个辅助任务，在 AVSBench 和 VPO 基准上达到 SOTA。

**[Cs2K: Class-Specific and Class-Shared Knowledge Guidance for Incremental Semantic Segmentation](cs2k_class-specific_and_class-shared_knowledge_guidance_for_incremental_semantic.md)**

:   提出 Cs2K 框架，从类别特有知识（原型引导伪标签 + 原型引导类别适应）和类别共享知识（权重引导选择性整合）两个方面协同缓解增量语义分割中的灾难性遗忘与新类欠拟合问题。

**[DenseNets Reloaded: Paradigm Shift Beyond ResNets and ViTs](densenets_reloaded_paradigm_shift_beyond_resnets_and_vits.md)**

:   重新审视 DenseNet 的密集拼接连接（concatenation shortcut），通过系统性现代化改造（加宽减深、现代化 block、扩大中间维度、更多 transition 层等），提出 RDNet（Revitalized DenseNet），在 ImageNet-1K 上超越 Swin Transformer、ConvNeXt、DeiT-III，证明了拼接连接作为一种被低估的范式具有强大潜力。

**[Exploring Pre-trained Text-to-Video Diffusion Models for Referring Video Object Segmentation](exploring_pretrained_texttovideo_diffusion_models_for_referr.md)**

:   VD-IT首次探索预训练T2V扩散模型（ModelScopeT2V）在视频理解任务中的应用，通过Text-Guided Image Projection和Video-specific Noise Prediction设计，从固定T2V模型中提取语义对齐、时序一致的视频特征，在Referring VOS任务上超越传统判别式backbone。

**[OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models](openpsg_openset_panoptic_scene_graph_generation_via_large_mu.md)**

:   本文首次提出开放集全景场景图生成任务（OpenPSG），利用大型多模态模型（BLIP-2）以自回归方式预测物体间的开放集关系，通过关系查询Transformer高效提取物体对特征并过滤无关对，在闭集和开放集设置下均取得SOTA。

**[Rotary Position Embedding for Vision Transformer](rotary_position_embedding_for_vision_transformer.md)**

:   本文系统研究了将 RoPE（Rotary Position Embedding）从1D语言模型扩展到2D视觉任务的方法，提出 RoPE-Mixed（混合可学习频率）替代传统的 Axial 频率分配，在 ViT 和 Swin Transformer 上实现了显著的分辨率外推性能提升，在 ImageNet 分类、COCO 检测和 ADE20k 分割上均带来一致增益。

**[SCLIP: Rethinking Self-Attention for Dense Vision-Language Inference](sclip_rethinking_selfattention_for_dense_visionlanguage_infe.md)**

:   发现CLIP在密集预测中失败的根因是自注意力机制导致的空间位置错配（spatial-invariant features），提出Correlative Self-Attention(CSA)机制——仅用一个投影矩阵计算token间相关性作为注意力分数，无需任何训练/额外参数即可将CLIP的零样本语义分割mIoU从14.1%提升至38.2%（8个基准平均），大幅超越现有SOTA的33.9%。

**[VISA: Reasoning Video Object Segmentation via Large Language Models](visa_reasoning_video_object_segmentation_via_large_language_models.md)**

:   提出 ReasonVOS 新任务和 VISA 模型，利用多模态 LLM 的世界知识推理能力实现基于隐式文本查询的视频目标分割与跟踪。
