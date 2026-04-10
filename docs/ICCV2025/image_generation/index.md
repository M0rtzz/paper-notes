<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**📹 ICCV2025** · 共 **39** 篇

**[Accelerating Diffusion Sampling via Exploiting Local Transition Coherence](accelerating_diffusion_sampling_via_exploiting_local_transition_coherence.md)**

:   提出 LTC-Accel，一种基于"局部转移一致性"(Local Transition Coherence) 现象的免训练扩散采样加速方法，通过利用相邻去噪步之间转移算子的强相关性来近似替代当前步的计算，在 Stable Diffusion v2 上实现 1.67× 加速，与蒸馏模型结合可在视频生成中达到 10× 加速。

**[Aether: Geometric-Aware Unified World Modeling](aether_geometric-aware_unified_world_modeling.md)**

:   Aether 提出一个几何感知的统一世界模型框架，通过在合成 4D 数据上联合训练重建、预测和规划三大能力，基于 CogVideoX 后训练实现零样本泛化到真实场景。

**[Aether: Geometric-Aware Unified World Modeling](aether_geometricaware_unified_world_modeling.md)**

:   提出Aether统一框架，通过任务交错特征学习联合优化4D动态重建、动作条件视频预测和目标条件视觉规划三个核心能力，实现geometry-aware的世界建模，纯合成数据训练即可零样本泛化到真实世界。

**[AnyPortal: Zero-Shot Consistent Video Background Replacement](anyportal_zero-shot_consistent_video_background_replacement.md)**

:   AnyPortal 提出了一个零样本、免训练的视频背景替换框架，通过协同利用 IC-Light 的重光照能力和视频扩散模型（CogVideoX）的时序先验，配合新提出的 Refinement Projection Algorithm (RPA) 实现像素级前景保持，在单张 24GB GPU 上即可高效运行。

**[Cns-Bench Benchmarking Image Classifier Robustness Under Continuous Nuisance Shi](cns-bench_benchmarking_image_classifier_robustness_under_continuous_nuisance_shi.md)**

:   提出 CNS-Bench，首个利用 LoRA 适配器对扩散模型施加**连续**且**逼真**的干扰偏移（nuisance shift）来系统评估图像分类器 OOD 鲁棒性的基准，覆盖 14 种偏移类型、5 个严重度级别和 40+ 分类器。

**[CompleteMe: Reference-based Human Image Completion](completeme_reference-based_human_image_completion.md)**

:   提出CompleteMe框架，通过双U-Net架构和Region-focused Attention（RFA）Block，利用参考图像中的细粒度人物细节（衣物纹理、纹身等），实现高保真的参考引导人体图像补全。

**[Cycle Consistency as Reward: Learning Image-Text Alignment without Human Preferences](cycle_consistency_as_reward_learning_imagetext_alignment_wit.md)**

:   提出CycleReward，利用cycle consistency作为自监督信号替代人工偏好标注——将caption用T2I模型重建为图像再比较相似度来排序，构建866K偏好对数据集CyclePrefDB，训练的奖励模型在detailed captioning上比HPSv2/PickScore/ImageReward高6%+，且DPO训练后提升VLM在多个VL任务上的性能，无需任何人工标注。

**[Deeply Supervised Flow-Based Generative Models](deeply_supervised_flow-based_generative_models.md)**

:   DeepFlow 通过在 flow-based 模型的 Transformer 层间引入深度监督和 VeRA（Velocity Refiner with Acceleration）模块，利用二阶 ODE 动力学对齐中间层速度特征，在不依赖外部预训练模型的情况下实现 8 倍训练加速和显著 FID 提升。

**[Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation](dense2moe_restructuring_diffusion_transformer_to_moe_for_eff.md)**

:   首次将预训练的dense DiT（如FLUX.1）转换为Mixture-of-Experts结构实现结构化稀疏推理，通过Taylor度量专家初始化+知识蒸馏+Mixture-of-Blocks进一步稀疏化，在激活参数减少60%的同时保持原始生成质量，全面超越剪枝方法。

**[Domain Generalizable Portrait Style Transfer](domain_generalizable_portrait_style_transfer.md)**

:   DGPST 提出了一个基于扩散模型的人像风格迁移框架，通过 semantic adapter 建立跨域稠密语义对应来扭曲参考图像，配合 AdaIN-Wavelet Transform 进行潜空间初始化以平衡风格化与内容保持，结合 ControlNet（高频结构引导）和 style adapter（风格引导）的双条件扩散模型生成最终结果，仅在 30K 真实肖像照片上训练即可泛化到照片、卡通、素描、动漫等多种域。

**[Efficient Autoregressive Shape Generation via Octree-Based Adaptive Tokenization](efficient_autoregressive_shape_generation_via_octree-based_adaptive_tokenization.md)**

:   OAT 提出基于二次误差度量（quadric error）的自适应八叉树 tokenization，根据局部几何复杂度动态分配 token 预算，在减少 50% token 的同时保持重建质量，并在此基础上构建 OctreeGPT 实现高质量文本到 3D 生成。

**[FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](flowedit_inversion-free_text-based_editing_using_pre-trained_flow_models.md)**

:   FlowEdit 提出一种无需反转（inversion-free）、无需优化、模型无关的文本编辑方法，直接在预训练 Flow 模型的源/目标分布之间构建 ODE 路径，实现比 inversion 更低传输代价的结构保持编辑。

**[HPSv3: Towards Wide-Spectrum Human Preference Score](hpsv3_towards_wide-spectrum_human_preference_score.md)**

:   HPSv3 构建了首个宽谱人类偏好数据集 HPDv3（1.08M 图文对、1.17M 标注对），采用 VLM 骨干（Qwen2-VL）+ 不确定性感知排序损失训练偏好模型，并提出 CoHP 链式思维迭代生成方法，显著提升图像生成评估的准确性和覆盖范围。

**[InfiniDreamer: Arbitrarily Long Human Motion Generation via Segment Score Distillation](infinidreamer_arbitrarily_long_human_motion_generation_via_segment_score_distill.md)**

:   InfiniDreamer 通过将预训练的短序列运动扩散模型作为先验，提出 Segment Score Distillation (SSD) 优化方法，对粗初始化的长运动序列中的重叠短片段进行迭代优化，实现了无需额外长序列训练数据的任意长度人体运动生成。

**[IntroStyle: Training-Free Introspective Style Attribution using Diffusion Features](introstyle_training-free_introspective_style_attribution_using_diffusion_feature.md)**

:   提出 IntroStyle，一种无需训练的风格归因方法，仅利用扩散模型自身中间层特征的通道级均值和方差统计量，通过 2-Wasserstein 距离度量图像间的风格相似性，在 WikiArt 和 DomainNet 上大幅超越需要专门训练的 SOTA 方法。

**[LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching](lazymar_accelerating_masked_autoregressive_models_via_feature_caching.md)**

:   LazyMAR针对Masked Autoregressive（MAR）模型的推理效率瓶颈，利用两种冗余——token冗余（相邻解码步中大部分token特征高度相似）和条件冗余（classifier-free guidance中条件/无条件输出的残差在相邻步间变化极小），设计了token cache和condition cache两种缓存机制，实现2.83×加速且几乎不损失生成质量。

**[LD-RPS: Zero-Shot Unified Image Restoration via Latent Diffusion Recurrent Posterior Sampling](ld-rps_zero-shot_unified_image_restoration_via_latent_diffusion_recurrent_poster.md)**

:   LD-RPS 提出一种零样本、无数据集的统一图像复原方法，利用预训练潜在扩散模型进行循环后验采样，通过多模态大模型提供语义先验、可学习 F-PAM 模块对齐退化域，实现多种退化类型的高质量盲复原。

**[Long-Context State-Space Video World Models](long-context_state-space_video_world_models.md)**

:   本文提出将状态空间模型（SSM/Mamba）引入视频世界模型，通过 block-wise SSM 扫描方案在空间一致性和时序记忆之间权衡，配合局部帧注意力，实现了线性训练复杂度、常数推理开销下的长期空间记忆保持，在 Memory Maze 和 Minecraft 数据集上大幅超越有限上下文的 Transformer 基线。

**[Make Me Happier: Evoking Emotions Through Image Diffusion Models](make_me_happier_evoking_emotions_through_image_diffusion_models.md)**

:   EmoEditor 提出首个系统性的**情感驱动图像生成**框架，通过双分支扩散模型（全局情感条件 + 局部语义特征）实现仅输入源图和目标情感即可生成具有目标情感的图像，无需手工文本指令或参考图，并构建了 340K 情感标注图对的 EmoPair 数据集。

**[MotionAgent: Fine-grained Controllable Video Generation via Motion Field Agent](motionagent_fine-grained_controllable_video_generation_via_motion_field_agent.md)**

:   提出 MotionAgent，通过运动场代理（Motion Field Agent）将文本中的运动描述转化为物体轨迹和相机外参，再经解析式光流合成模块统一为光流图，实现仅凭文本输入即可对 I2V 生成中的物体运动和相机运动进行细粒度精确控制。

**[MotionDiff: Training-Free Zero-Shot Interactive Motion Editing via Flow-Assisted Multi-View Diffusion](motiondiff_training-free_zero-shot_interactive_motion_editing_via_flow-assisted_.md)**

:   MotionDiff 提出一种免训练、零样本的多视图运动编辑方法，通过点运动学模型（PKM）从静态场景估计多视图光流，再利用解耦运动表示引导 Stable Diffusion 生成高质量、多视图一致的运动编辑结果。

**[MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion](motionfollower_editing_video_motion_via_score-guided_diffusion.md)**

:   提出 MotionFollower，通过两个轻量卷积控制器（姿态+外观）和基于分数函数正则化的一致性引导机制，实现视频运动编辑，在 GPU 显存消耗减少约 80% 的同时超越 MotionEditor 等强基线。

**[Multi-turn Consistent Image Editing](multi-turn_consistent_image_editing.md)**

:   提出基于 flow matching 的多轮图像编辑框架，通过双目标 LQR 引导和自适应注意力机制，有效抑制多轮编辑中的误差累积，在保持内容一致性的同时实现灵活可控的迭代编辑。

**[MUNBa: Machine Unlearning via Nash Bargaining](munba_machine_unlearning_via_nash_bargaining.md)**

:   将机器遗忘（Machine Unlearning）建模为双玩家合作博弈问题，利用 Nash 讨价还价理论推导闭式解来同时解决遗忘目标与保留目标之间的梯度冲突和梯度支配问题，在分类和生成任务上实现遗忘与保留的最优平衡。

**[Music-Aligned Holistic 3D Dance Generation via Hierarchical Motion Modeling](music-aligned_holistic_3d_dance_generation_via_hierarchical_motion_modeling.md)**

:   提出 SoulDance 数据集（首个含身体+手部+面部的高质量3D舞蹈数据集）和 SoulNet 框架（层次化残差向量量化 + 音乐对齐生成模型 + 跨模态检索），实现首个面部表情与身体手部动作协调一致、与音乐节奏情感对齐的全身3D舞蹈生成。

**[NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors](normalcrafter_learning_temporally_consistent_normals_from_video_diffusion_priors.md)**

:   NormalCrafter 基于视频扩散模型（SVD）提出视频法线估计方法，通过语义特征正则化（SFR）和两阶段训练策略，生成具有精细细节和时序一致性的法线序列，在视频基准上大幅超越现有单帧方法。

**[NullSwap: Proactive Identity Cloaking Against Deepfake Face Swapping](nullswap_proactive_identity_cloaking_against_deepfake_face_swapping.md)**

:   提出 NullSwap，通过在源图像中嵌入身份引导的不可见扰动来伪装面部身份信息，使 Deepfake 换脸模型无法提取正确身份，从而在纯黑盒场景下主动防御换脸攻击。

**[OmniPaint: Mastering Object-Oriented Editing via Disentangled Insertion-Removal Inpainting](omnipaint_mastering_object-oriented_editing_via_disentangled_insertion-removal_i.md)**

:   提出 OmniPaint 统一框架，将物体移除与插入重新定义为互逆互补的关联任务，基于 FLUX 扩散先验并引入 CycleFlow 无配对训练机制和 CFD 无参考评估指标，仅用 3K 真实配对样本即可实现高保真的物体编辑，尤其擅长处理阴影、反射等复杂物理效果。

**[Randomized Autoregressive Visual Generation](randomized_autoregressive_visual_generation.md)**

:   提出 Randomized AutoRegressive modeling (RAR)：在标准自回归训练中以随机排列输入序列并逐步退火回光栅扫描顺序，使模型学习双向上下文，在 ImageNet-256 上以 FID 1.48 刷新自回归图像生成 SOTA，同时保持与语言模型框架的完全兼容。

**[REDUCIO! Generating 1K Video within 16 Seconds using Extremely Compressed Motion Latents](reducio_generating_1k_video_within_16_seconds_using_extremely_compressed_motion_.md)**

:   提出 Reducio-VAE，一种以内容帧为条件的 3D 视频自编码器，将视频压缩至比标准 2D VAE 小 64 倍的运动潜空间，配合 Reducio-DiT 在单张 A100 上 15.5 秒内生成 16 帧 1024x1024 视频，训练仅需 3200 A100 GPU 小时。

**[REPA-E: Unlocking VAE for End-to-End Tuning of Latent Diffusion Transformers](repae_unlocking_vae_for_endtoend_tuning_of_latent_diffusion.md)**

:   回答了"潜空间扩散模型能否与VAE端到端联合训练"的基础问题——发现标准扩散loss无法端到端训练但表示对齐（REPA）loss可以，提出REPA-E实现VAE+DiT联合训练，训练速度比REPA快17倍、比vanilla快45倍，在ImageNet 256×256上达到1.12 FID（w/ CFG）的新SOTA。

**[SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation](sanasprint_onestep_diffusion_with_continuoustime_consistency.md)**

:   将预训练的SANA flow matching模型通过无损数学变换转化为TrigFlow，结合连续时间一致性蒸馏（sCM）和潜空间对抗蒸馏（LADD）的混合策略，实现统一的1-4步自适应高质量图像生成，1步生成1024×1024图像仅需0.1s（H100），以7.59 FID和0.74 GenEval超越FLUX-schnell且速度快10倍。

**[ShortFT: Diffusion Model Alignment via Shortcut-based Fine-Tuning](shortft_diffusion_model_alignment_via_shortcut-based_fine-tuning.md)**

:   提出 ShortFT，利用轨迹保持少步扩散模型构建去噪捷径（shortcut），将原本冗长的去噪链大幅缩短，从而实现完整的端到端奖励梯度反向传播，高效且有效地将扩散模型与奖励函数对齐。

**[SMGDiff: Soccer Motion Generation using Diffusion Probabilistic Models](smgdiff_soccer_motion_generation_using_diffusion_probabilistic_models.md)**

:   提出 SMGDiff，一个两阶段扩散模型框架，能够根据用户控制信号实时生成高质量、多样化的足球运动动画，同时通过接触引导模块优化球-脚交互细节。

**[Spectral Image Tokenizer](spectral_image_tokenizer.md)**

:   提出 Spectral Image Tokenizer (SIT)，用离散小波变换 (DWT) 将图像从空域转换到频域后再进行 token 化，使 token 序列天然地按"粗到细"排列，从而支持多分辨率重建、渐进式生成、文本引导上采样与编辑等传统 raster-scan tokenizer 无法实现的能力。

**[StyleKeeper: Prevent Content Leakage using Negative Visual Query Guidance](stylekeeper_prevent_content_leakage_using_negative_visual_query_guidance.md)**

:   提出 **负视觉查询引导（NVQG）** 方法，通过在 self-attention 层中将参考图的 query 注入作为负向引导来抑制内容泄漏，实现了无需训练的高质量视觉风格提示，在风格相似度和文本对齐上均优于现有方法。

**[TeRA: Rethinking Text-guided Realistic 3D Avatar Generation](tera_rethinking_text-guided_realistic_3d_avatar_generation.md)**

:   提出TeRA，首个基于隐空间扩散模型的文本引导3D真人头像生成框架，通过蒸馏大规模人体重建模型构建结构化隐空间，12秒生成写实3D人物，比SDS方法快两个数量级。

**[Video Color Grading via Look-Up Table Generation](video_color_grading_via_look-up_table_generation.md)**

:   提出基于扩散模型显式生成 LUT 的视频调色框架：通过 GS-Extractor 提取参考场景的高层风格特征，用 L-Diffuser 生成色彩查找表（LUT），一次生成即可无损应用于全部视频帧，并支持文本 prompt 进行亮度/对比度等细粒度调整。

**[VisualCloze: A Universal Image Generation Framework via Visual In-Context Learning](visualcloze_a_universal_image_generation_framework_via_visua.md)**

:   提出VisualCloze，将多种图像生成任务（编辑、翻译、超分、风格化等）统一为"视觉完形填空"范式——用视觉示例（而非文本指令）定义任务，通过图像infilling模型实现统一生成，并构建Graph200K数据集增强任务间知识迁移，支持域内任务、未见任务泛化、多任务组合和反向生成。
