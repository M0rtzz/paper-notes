<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**🎞️ ECCV2024** · 共 **39** 篇

**[2S-ODIS: Two-Stage Omni-Directional Image Synthesis by Geometric Distortion Correction](2s-odis_two-stage_omni-directional_image_synthesis_by_geometric_distortion_corre.md)**

:   2S-ODIS通过两阶段结构利用预训练VQGAN（无需微调）合成全景图像：第一阶段生成低分辨率粗略ERP图，第二阶段通过生成26个NFoV局部图像并融合来校正几何畸变，训练时间从14天缩短到4天且图像质量更优。

**[A Diffusion Model for Simulation Ready Coronary Anatomy with Morpho-skeletal Control](a_diffusion_model_for_simulation_ready_coronary_anatomy_with.md)**

:   用潜在扩散模型（LDM）可控生成3D多组织冠状动脉分割图，通过拓扑交互损失保证解剖合理性，通过形态-骨架双通道条件化实现对截面形态和分支结构的解耦控制，并提出自适应空条件引导（ANG）以非可微回归器高效增强条件保真度，最终支持面向有限元仿真的反事实解剖结构编辑。

**[AccDiffusion: An Accurate Method for Higher-Resolution Image Generation](accdiffusion_an_accurate_method_for_higher-resolution_image_generation.md)**

:   提出AccDiffusion，通过将全局文本prompt解耦为patch级别的内容感知prompt（利用cross-attention map判断每个词汇是否属于某patch），并引入带窗口交互的膨胀采样来改善全局一致性，在无需额外训练的情况下有效解决patch-wise高分辨率图像生成中的目标重复问题，在SDXL上实现了从2K到4K分辨率的无重复高质量图像外推。

**[AdaDiffSR: Adaptive Region-Aware Dynamic Acceleration Diffusion Model for Real-World Image Super-Resolution](adadiffsr_adaptive_region-aware_dynamic_acceleration_diffusion_model_for_real-wo.md)**

:   观察到扩散模型超分中不同图像区域所需去噪步数差异巨大（背景区域早已收敛而前景纹理仍需迭代），提出基于多指标潜在熵（MMLE）感知信息增益来动态跳步的策略，将子区域分为稳定/增长/饱和三类给予不同步长，并通过渐进特征注入（PFJ）平衡保真度与真实感，在DRealSR等数据集上取得与StableSR可比的质量但推理时间和FLOPs分别减少1.5×和2.7×。

**[AdaGen: Learning Adaptive Policy for Image Synthesis](adagen_learning_adaptive_policy_for_image_synthesis.md)**

:   将多步生成模型（MaskGIT/AR/Diffusion/Rectified Flow）的步级参数调度（温度、mask ratio、CFG scale、timestep等）统一建模为MDP，用轻量RL策略网络实现样本自适应调度，并提出对抗奖励设计防止策略过拟合，在四种生成范式上一致提升性能（VAR FID 1.92→1.59，DiT-XL推理成本降3倍同时性能更优）。

**[AdaNAT: Exploring Adaptive Policy for Token-Based Image Generation](adanat_exploring_adaptive_policy_for_token-based_image_generation.md)**

:   提出AdaNAT，将非自回归Transformer（NAT）的生成策略配置建模为MDP，通过轻量策略网络+PPO强化学习+对抗奖励模型自动为每个样本定制生成策略（重掩码比例、采样温度、CFG权重等），在ImageNet-256上仅用8步达到FID 2.86，相比手工策略实现约40%的相对提升。

**[AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation](anycontrol_create_your_artwork_with_versatile_control_on_tex.md)**

:   AnyControl提出Multi-Control Encoder，通过交替执行多控制融合块和多控制对齐块，从任意组合的多种空间控制信号中提取统一的多模态embedding，实现高质量、语义对齐的多条件可控图像生成。

**[AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation](anycontrol_create_your_artwork_with_versatile_control_on_text-to-image_generatio.md)**

:   提出 AnyControl，通过 Multi-Control Encoder（fusion + alignment 交替块结构）支持任意组合的多种空间控制信号（深度、边缘、分割、姿态），在 COCO 多控制基准上 FID 44.28 全面超越现有方法。

**[Bridging the Gap: Studio-Like Avatar Creation from a Monocular Phone Capture](bridging_the_gap_studio-like_avatar_creation_from_a_monocular_phone_capture.md)**

:   提出从单目手机视频生成类似影棚级质量的面部纹理贴图的方法，结合 StyleGAN2 的 W+ 空间参数化与扩散模型超分辨率，实现从手机扫描到高质量 3D 头像的跨越。

**[ByteEdit: Boost, Comply and Accelerate Generative Image Editing](byteedit_boost_comply_and_accelerate_generative_image_editing.md)**

:   提出 ByteEdit，一个将人类反馈学习引入生成式图像编辑（inpainting/outpainting）的框架，通过美学、对齐、一致性三个奖励模型提升编辑质量，并利用对抗训练和渐进策略加速推理。

**[Challenging Forgets: Unveiling the Worst-Case Forget Sets in Machine Unlearning](challenging_forgets_unveiling_the_worst-case_forget_sets_in_machine_unlearning.md)**

:   提出从对抗视角识别"最坏情况遗忘集"的方法，通过双层优化框架找到最难被遗忘的数据子集，利用 SignSGD 将二阶 BLO 简化为一阶问题，从而更可靠地评估机器遗忘方法的真实效能。

**[COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation](coin_control-inpainting_diffusion_prior_for_human_and_camera_motion_estimation.md)**

:   提出COIN方法，通过控制-补绘（Control-Inpainting）的改进版Score Distillation Sampling，结合人-场景关系损失，从单目动态相机视频中同时估计高质量的全局人体运动和相机运动。

**[ColorPeel: Color Prompt Learning with Diffusion Models via Color and Shape Disentanglement](colorpeel_color_prompt_learning_with_diffusion_models_v.md)**

:   提出 ColorPeel，通过在目标颜色的基础几何体上联合学习颜色和形状 token 来实现颜色与形状解耦，使 T2I 扩散模型能精确生成用户指定 RGB 颜色的物体。

**[Controlling the World by Sleight of Hand](controlling_the_world_by_sleight_of_hand.md)**

:   提出 CosHand，通过手部二值掩码作为动作条件，在预训练 Stable Diffusion 上微调，预测手-物交互后的未来图像，并可零样本泛化到机器人末端执行器。

**[Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers](difftracker_texttoimage_diffusion_models_are_unsupervised_tr.md)**

:   Diff-Tracker利用预训练T2I扩散模型知识进行无监督跟踪，学习prompt在cross-attention上激活目标区域。

**[EMDM: Efficient Motion Diffusion Model for Fast and High-Quality Motion Generation](emdm_efficient_motion_diffusion_model_for_fast_and_high.md)**

:   提出 EMDM，通过条件去噪扩散 GAN 捕获大步长采样时的复杂多模态去噪分布，结合几何损失约束，实现 T≤10 步的实时人体运动生成，推理速度提升 60-240 倍，同时保持高质量。

**[FineMatch: Aspect-Based Fine-Grained Image and Text Mismatch Detection and Correction](finematch_aspectbased_finegrained_image_and_text_mismat.md)**

:   提出 FineMatch benchmark，要求模型识别图文对中不匹配的方面短语（Entity/Relation/Attribute/Number）、确定类别并提出修正，构建了 49,906 个人工标注样本，并提出 ITM-IoU 评估指标和 AutoAlign 文生图幻觉检测校正系统。

**[FreeDiff: Progressive Frequency Truncation for Image Editing with Diffusion Models](freediff_progressive_frequency_truncation_for_image_edi.md)**

:   提出 FreeDiff，通过渐进式频率截断从频域精化扩散模型的编辑引导信号，无需微调或修改网络结构，实现覆盖多种编辑类型的通用图像编辑方法。

**[FreeInit: Bridging Initialization Gap in Video Diffusion Models](freeinit_bridging_initialization_gap_in_video_diffusion.md)**

:   提出 FreeInit，一种无需额外训练的推理采样策略，通过迭代精炼初始噪声的时空低频分量来弥合视频扩散模型训练与推理之间的初始化差距，显著提升生成视频的时序一致性。

**[Getting it Right: Improving Spatial Consistency in Text-to-Image Models](getting_it_right_improving_spatial_consistency_in_texttoimag.md)**

:   发现现有VL数据集严重缺乏空间关系描述（如left/right/above/behind出现率极低），构建了首个空间聚焦的大规模数据集SPRIGHT（600万张图像重描述），仅用0.25%数据微调即可提升22%空间一致性得分，用<500张多物体图像微调达到T2I-CompBench空间SOTA 0.2133。

**[HybridBooth: Hybrid Prompt Inversion for Efficient Subject-Driven Generation](hybridbooth_hybrid_prompt_inversion_for_efficient_subje.md)**

:   提出 HybridBooth，融合优化方法和直接回归方法的优势——先用预训练编码器（Word Embedding Probe）生成初始 word embedding，再通过残差精细化（仅 3-5 步）快速适配特定主体，实现高效高保真的 subject-driven 生成。

**[Infinite-ID: Identity-Preserved Personalization via ID-Semantics Decoupling Paradigm](infiniteid_identitypreserved_personalization_via_idsema.md)**

:   提出 Infinite-ID，通过 ID-语义解耦范式将身份信息和文本语义信息分离训练，再通过混合注意力机制和 AdaIN-mean 操作在推理时融合，实现高保真身份保持与精确语义控制的平衡。

**[∞-Brush: Controllable Large Image Synthesis with Diffusion Models in Infinite Dimensions](inftybrush_controllable_large_image_synthesis_with_diffusion.md)**

:   提出首个在无限维函数空间中的条件扩散模型 ∞-Brush，通过交叉注意力神经算子实现可控条件生成，仅用 0.4% 像素训练即可在任意分辨率（最高 4096×4096）上生成保持全局结构的大图像。

**[Latent Guard: A Safety Framework for Text-to-Image Generation](latent_guard_a_safety_framework_for_texttoimage_generation.md)**

:   Latent Guard在T2I文本编码器上学习潜在空间检测黑名单概念。

**[LCM-Lookahead for Encoder-Based Text-to-Image Personalization](lcmlookahead_for_encoderbased_texttoimage_personalization.md)**

:   本文提出利用LCM（Latent Consistency Model）作为"快捷通道"，在扩散模型encoder训练中实现图像空间损失（如身份识别loss）的反向传播，配合自注意力特征共享和一致性数据生成，显著提升encoder-based人脸个性化的身份保持和prompt对齐能力。

**[Learning Trimodal Relation for Audio-Visual Question Answering with Missing Modality](learning_trimodal_relation_for_audiovisual_question_answerin.md)**

:   提出面向音视觉问答（AVQA）的缺失模态处理框架，通过Relation-aware Missing Modal生成器利用三模态关系召回缺失信息，再通过Audio-Visual Relation-aware扩散模型增强特征表示，即使缺少一个模态也能准确回答问题。

**[LEGO: Learning EGOcentric Action Frame Generation via Visual Instruction Tuning](lego_learning_egocentric_action_frame_generation_via_vi.md)**

:   提出 LEGO 模型，通过视觉指令微调增强 VLLM 的动作描述能力，并将 VLLM 的图像/文本嵌入作为额外条件注入扩散模型，实现从第一人称视角生成动作执行帧。

**[MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed-Precision Quantization](mixdq_memoryefficient_fewstep_texttoimage_diffusion_models_w.md)**

:   针对少步扩散模型（如SDXL-turbo 1-step）比多步模型更难量化的问题，提出MixDQ混合精度量化方法，包含BOS-aware文本嵌入量化、指标解耦敏感度分析和整数规划比特分配，在W4A8下仅增加0.5 FID，实现3倍模型压缩和1.5倍加速。

**[MotionChain: Conversational Motion Controllers via Multimodal Prompts](motionchain_conversational_motion_controllers_via_multimodal.md)**

:   MotionChain构建视觉-运动语言模型，通过VQ-VAE将动作token化支持多轮对话运动生成。

**[Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization](pixelaware_stable_diffusion_for_realistic_image_superre.md)**

:   提出像素感知稳定扩散（PASD）网络，通过像素感知交叉注意力（PACA）在潜空间中实现像素级结构保持，配合退化移除模块和可调噪声调度，统一解决真实图像超分辨率和个性化风格迁移两大任务。

**[Ponymation: Learning Articulated 3D Animal Motions from Unlabeled Online Videos](ponymation_learning_articulated_3d_animal_motions_from_.md)**

:   提出从原始、无标签的互联网视频中学习动物 3D 关节运动生成模型的方法，核心是一个视频光几何自编码框架，将训练视频分解为静止姿态形状、关节姿态序列和纹理，实现无需姿态标注的 3D 运动 VAE 学习。

**[Powerful and Flexible: Personalized Text-to-Image Generation via Reinforcement Learning](powerful_and_flexible_personalized_texttoimage_generation_vi.md)**

:   将个性化T2I建模为DPG框架，引入Q函数和向前看机制捕获长期视觉一致性。

**[Removing Distributional Discrepancies in Captions Improves Image-Text Alignment](removing_distributional_discrepancies_in_captions_improves_i.md)**

:   发现训练图文对齐模型时正负caption之间存在被忽视的数据集级别分布偏差（如GPT生成负样本时倾向用elephant替换giraffe），提出用纯文本分类器过滤高置信样本来消除偏差，结合替换型+交换型两类负样本微调LLaVA-1.5，在Winoground、SeeTRUE等多个基准上大幅超越现有方法。

**[ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation](scaledreamer_scalable_textto3d_synthesis_with_asynchronous_s.md)**

:   提出异步分数蒸馏(ASD)，通过将扩散时间步前移（而非微调扩散模型）来减小噪声预测误差，实现稳定的3D生成器训练并可扩展到100K文本提示，保持扩散模型的文本理解能力不受损。

**[Soft Prompt Generation for Domain Generalization](soft_prompt_generation_for_domain_generalization.md)**

:   提出 SPG（Soft Prompt Generation），首次将生成模型引入 VLM 的 prompt learning，通过 CGAN 从图像动态生成实例特定的软提示，将域知识存储在生成模型中而非提示向量中，实现更好的领域泛化性能。

**[Text2Place: Affordance-Aware Text Guided Human Placement](text2place_affordanceaware_text_guided_human_placement.md)**

:   提出 Text2Place，通过 SDS 损失优化 Gaussian blob 参数化的语义掩码学习场景中的人体 affordance，再结合主体条件修复实现逼真的文本引导人物放置，无需大规模训练。

**[TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering](textdiffuser2_unleashing_the_power_of_language_models_f.md)**

:   TextDiffuser-2 利用两个语言模型（一个用于布局规划、一个用于布局编码）实现灵活自动的文本渲染，克服了现有方法在灵活性、布局能力和样式多样性方面的局限。

**[Towards Reliable Advertising Image Generation Using Human Feedback](towards_reliable_advertising_image_generation_using_human_fe.md)**

:   针对电商广告图像生成中大量不可用图像（空间不匹配、尺寸不匹配、不显著、形状幻觉）的问题，构建了百万级RF1M数据集训练多模态检测网络RFNet，并提出基于RFNet反馈微调扩散模型的RFFT方法（含Consistent Condition正则化），将可用率从约50%提升至接近100%且不损失美观性。

**[XPSR: Cross-modal Priors for Diffusion-based Image Super-Resolution](xpsr_crossmodal_priors_for_diffusionbased_image_superresolut.md)**

:   XPSR提出将多模态大语言模型（LLaVA）生成的高层与低层语义描述作为跨模态先验，通过Semantic-Fusion Attention融合到扩散模型中，并设计Degradation-Free Constraint提取语义保留特征，实现高保真高真实感的图像超分辨率。
