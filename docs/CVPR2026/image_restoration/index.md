<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**📷 CVPR2026** · 共 **30** 篇

**[Beyond Ground-Truth: Leveraging Image Quality Priors for Real-World Image Restoration](beyond_ground-truth_leveraging_image_quality_priors_for_real-world_image_restora.md)**

:   提出IQPIR框架，引入预训练NR-IQA模型的图像质量先验(IQP)作为条件信号，通过质量条件化Transformer、双Codebook结构和离散表示空间质量优化三个机制，引导图像修复过程趋向最高感知质量，在盲人脸修复等任务上全面超越SOTA。

**[Beyond the Ground Truth: Enhanced Supervision for Image Restoration](beyond_the_ground_truth_enhanced_supervision_for_image_restoration.md)**

:   提出通过超分辨率+频域自适应混合来增强现有数据集中次优GT图像的感知质量，并训练轻量级ORNet精修模块，无需修改预训练修复模型即可提升输出的感知质量。

**[BHCast: Unlocking Black Hole Plasma Dynamics from a Single Blurry Image with Long-Term Forecasting](bhcast_unlocking_black_hole_plasma_dynamics_from_a_single_blurry_image_with_long.md)**

:   BHCast从单张模糊的EHT黑洞图像出发，通过U-Net动力学代理模型进行超分辨率+长期自回归预测（100步稳定），从预测的等离子体动力学中提取物理特征（旋转速度、螺旋角等），再通过XGBoost推断黑洞自旋和倾角，在真实M87*观测图像上也展示了有效性。

**[Blink: Dynamic Visual Token Resolution for Enhanced Multimodal Understanding](blink_dynamic_visual_token_resolution_for_enhanced_multimodal_understanding.md)**

:   提出 Blink 框架，通过在 MLLM 不同 Transformer 层动态扩展和丢弃视觉 token（模拟人类"快速眨眼"式扫描），在单次前向传播中自适应增强视觉感知能力，在多个多模态基准上提升 LLaVA-1.5 性能。

**[BluRef: Unsupervised Image Deblurring with Dense-Matching References](bluref_unsupervised_image_deblurring_with_dense-matching_references.md)**

:   提出 BluRef，首个利用非配对参考清晰图像通过稠密匹配生成伪 ground truth 来训练去模糊网络的无监督框架，性能逼近甚至超越有监督方法。

**[Bridging the Perception Gap in Image Super-Resolution Evaluation](bridging_the_perception_gap_in_image_super-resolution_evaluation.md)**

:   通过大规模用户研究揭示现有 SR 评估指标（PSNR、SSIM、LPIPS 等）与人类感知严重不一致，分析其内在缺陷后提出极简但有效的 RQI（Relative Quality Index）框架，通过学习图像对之间的相对质量差异实现更可靠的 SR 评估，且可作为损失函数指导 SR 训练。

**[CDA-VSR: Compressed-Domain-Aware Online Video Super-Resolution](compressed-domain-aware_online_video_super-resolution.md)**

:   CDA-VSR利用视频比特流中免费可得的压缩域信息（运动向量、残差图、帧类型）来分别指导帧对齐、特征融合和自适应重建，在REDS4数据集上比SOTA方法TMP提升PSNR达0.13dB的同时实现>2倍推理速度（~93 FPS@320×180，RTX 3090）。

**[PNG: Diffusion-Based sRGB Real Noise Generation via Prompt-Driven Noise Representation Learning](diffusion-based_srgb_real_noise_generation_via_prompt-driven_noise_representatio.md)**

:   PNG提出用可学习的Global/Local Prompt组件从真实噪声中自动提取噪声特征（替代ISO/相机型号等metadata），通过Prompt AutoEncoder编码噪声到latent空间+Prompt DiT（基于一致性模型）一步生成latent code，实现无需任何metadata的真实sRGB噪声合成，下游DnCNN去噪在SIDD上仅落后真实数据0.08dB。

**[Disentangled Textual Priors for Diffusion-based Image Super-Resolution](disentangled_textual_priors_for_diffusion-based_image_super-resolution.md)**

:   提出 DTPSR，通过将文本先验沿空间层级（全局/局部）和频率语义（低频/高频）两个维度解耦，构建解耦的跨注意力注入管线和多分支 CFG 策略，实现感知质量优越的扩散超分辨率。

**[Empowering Semantic-Sensitive Underwater Image Enhancement with VLM](empowering_semantic-sensitive_underwater_image_enhancement_with_vlm.md)**

:   提出一种利用 VLM 生成语义引导图的即插即用策略（-SS），通过交叉注意力注入和语义对齐损失的双重引导机制，使水下图像增强模型在恢复时聚焦语义关键区域，显著提升感知质量和下游检测/分割性能。

**[Empowering Semantic-Sensitive Underwater Image Enhancement with VLM](empowering_semanticsensitive_underwater_image_enha.md)**

:   提出 VLM 驱动的语义敏感学习策略，通过 VLM 生成目标物体描述、BLIP 构建空间语义引导图、双重引导机制（cross-attention + 语义对齐损失）注入 UIE decoder，使增强结果在感知质量和检测/分割下游任务上同时提升。

**[FiDeSR: High-Fidelity and Detail-Preserving One-Step Diffusion Super-Resolution](fidesr_high-fidelity_and_detail-preserving_one-step_diffusion_super-resolution.md)**

:   提出 FiDeSR，一种高保真和细节保持的单步扩散超分框架，通过细节感知加权（DAW）、隐空间残差精炼块（LRRB）和潜在频率注入模块（LFIM）三个互补组件，同时解决单步扩散超分中的结构保真度退化和高频细节恢复不足问题。

**[Fractals made Practical: Denoising Diffusion as Partitioned Iterated Function Systems](fractals_made_practical_denoising_diffusion_as_par.md)**

:   证明 DDIM 确定性反向链等价于分区迭代函数系统（PIFS），从分形几何推导出三个可计算量（收缩阈值 $L_t^*$、对角膨胀函数 $f_t(\lambda)$、全局膨胀阈值 $\lambda^{**}$），统一解释了余弦调度偏移、分辨率 logSNR 偏移、Min-SNR 损失加权和 Align Your Steps 采样调度四种经验设计选择。

**[Fractals made Practical: Denoising Diffusion as Partitioned Iterated Function Systems](fractals_made_practical_denoising_diffusion_as_partitioned_iterated_function_sys.md)**

:   证明了DDIM确定性反向链本质上是一个分区迭代函数系统(PIFS)，并从该框架推导出三个无需模型评估的可计算几何量，从第一性原理统一解释了扩散模型的双阶段去噪动力学、自注意力的有效性，以及四种经验设计选择（cosine schedule offset、分辨率相关logSNR偏移、Min-SNR损失加权、Align Your Steps采样）。

**[Flickerformer: A Duet of Periodicity and Directionality for Burst Flicker Removal](it_takes_two_a_duet_of_periodicity_and_directionality_for_burst_flicker_removal.md)**

:   揭示闪烁伪影的两个内在物理特性——**周期性**(空间-时间重复的亮暗条纹模式)和**方向性**(沿行式曝光方向传播)——提出Flickerformer Transformer架构：基于相位的融合模块(PFM)利用帧间相位相关自适应聚合burst特征、自相关前馈网络(AFFN)利用帧内结构规律、小波方向注意力模块(WDAM)用高频方向信息引导低频暗区修复，在burst闪烁去除上全面超越SOTA。

**[Learning Latent Transmission and Glare Maps for Lens Veiling Glare Removal](learning_latent_transmission_and_glare_maps_for_lens_veiling_glare_removal.md)**

:   提出 VeilGen + DeVeiler 框架，通过物理引导的 Stable Diffusion 生成模型学习潜在透射率和眩光图以合成逼真的复合退化训练数据，并用可逆约束训练修复网络，实现简化光学系统中像差与雾化眩光的联合去除。

**[Learning to Translate Noise for Robust Image Denoising](learning_to_translate_noise_for_robust_image_denoising.md)**

:   提出噪声翻译框架，通过轻量级噪声翻译网络将未知真实噪声转换为高斯噪声，再由预训练的高斯去噪网络处理，在 OOD 真实噪声基准上平均 PSNR 提升 1.5dB 以上，且翻译网络仅 0.29M 参数、可跨去噪器迁移。

**[MAD-Avatar: Motion-Aware Animatable Gaussian Avatars Deblurring](motionaware_animatable_gaussian_avatars_deblurring.md)**

:   首次实现从模糊视频直接重建清晰可驱动3D高斯人体avatar：提出3D感知的物理模糊形成模型(将模糊分解为子帧SMPL运动+canonical 3DGS)，用B-spline插值+位姿变形网络建模子帧运动，帧间正则化解决运动方向歧义，在合成和真实数据集上大幅超越"2D去模糊+3DGS"两阶段方案(PSNR提升约2.5dB)。

**[OARS: Process-Aware Online Alignment for Generative Real-World Image Super-Resolution](oars_processaware_online_alignment_for_generative.md)**

:   提出了OARS框架，通过基于MLLM的过程感知奖励模型COMPASS和渐进式在线强化学习，将生成式真实世界超分辨率模型与人类视觉偏好对齐，在感知质量和保真度之间实现自适应平衡。

**[POLISH'ing the Sky: Wide-Field and High-Dynamic Range Interferometric Image Reconstruction](polishing_the_sky_wide-field_and_high-dynamic_range_interferometric_image_recons.md)**

:   在 POLISH 框架基础上提出 POLISH+ 和 POLISH++，通过分块训练-拼接策略和基于 arcsinh 的非线性变换，实现宽视场（12,960×12,960 像素）和高动态范围（$\sim 10^6$）条件下的射电干涉图像重建与超分辨率，并首次展示深度学习方法可超分辨强引力透镜系统。

**[RAW-Domain Degradation Models for Realistic Smartphone Super-Resolution](raw-domain_degradation_models_for_realistic_smartphone_super-resolution.md)**

:   提出基于标定的 RAW 域退化建模框架，通过为多款智能手机相机精确标定 SR 模糊核与传感器噪声模型，将公开 sRGB 图像"反处理"为逼真的 LR RAW 数据用于训练，在相机特定和跨相机盲超分辨率场景中均显著超越基于通用退化池的基线方法。

**[RAW-Domain Degradation Models for Realistic Smartphone Super-Resolution](rawdomain_degradation_models_smartphone_sr.md)**

:   通过对不同智能手机传感器进行设备特定的退化标定（模糊PSF和噪声模型），将公开渲染图像逆处理（unprocess）到各手机的RAW域来生成逼真的训练对，训练的RAW-to-RGB SR模型在未见设备上的真实数据上显著优于使用任意退化参数的基线。

**[ShiftLUT: Spatial Shift Enhanced Look-Up Tables for Efficient Image Restoration](shiftlut_spatial_shift_enhanced_look-up_tables_for_efficient_image_restoration.md)**

:   提出 ShiftLUT，通过可学习空间偏移模块（LSS）实现 LUT 方法中最大感受野（65×65），配合非对称双分支架构和误差有界自适应采样（EAS），在存储 104KB + 推理 84ms 的条件下超越所有现有 LUT 方法。

**[Spectral Super-Resolution via Adversarial Unfolding and Data-Driven Spectrum Regularization](spectral_super-resolution_via_adversarial_unfolding_and_data-driven_spectrum_reg.md)**

:   提出 UALNet，通过将数据驱动的光谱先验（PriorNet）和对抗学习项同时嵌入深度展开框架，实现从 Sentinel-2 多光谱数据（12 波段）到 NASA AVIRIS 高光谱图像（186 波段）的光谱超分辨率，性能超越 Transformer 的同时仅需 15% 计算量和 1/20 参数。

**[Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging](statistical_characteristic-guided_denoising_for_rapid_high-resolution_transmissi.md)**

:   提出统计特征引导去噪网络 SCGN，利用空间域的窗口标准差加权和频域的频带引导加权，分别在空间和频率两个域自适应地增强信号、抑制噪声，结合 HRTEM 专用噪声标定方法生成含无序结构的真实噪声数据集，实现毫秒级高分辨率透射电子显微镜图像的高质量去噪。

**[Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset](toward_real-world_infrared_image_super-resolution_a_unified_autoregressive_frame.md)**

:   提出 Real-IISR，一个基于热-结构引导的视觉自回归框架，通过条件自适应码本和热序一致性损失实现真实世界红外图像超分辨率，并构建首个真实红外超分数据集 FLIR-IISR。

**[Towards Universal Computational Aberration Correction in Photographic Cameras: A Comprehensive Benchmark Analysis](towards_universal_computational_aberration_correction_in_photographic_cameras_a_.md)**

:   构建首个面向消费级相机的通用计算像差校正基准 UniCAC，提出光学退化评估器 ODE 量化像差难度，系统评测 24 种图像恢复/CAC 方法，揭示影响 CAC 性能的三大关键因素。

**[UCAN: Unified Convolutional Attention Network for Expansive Receptive Fields in Lightweight Super-Resolution](ucan_unified_convolutional_attention_network_for_expansive_receptive_fields_in_l.md)**

:   提出 UCAN，一种统一卷积与注意力的轻量级超分网络，通过 Hedgehog Attention 突破线性注意力的低秩瓶颈，结合 Flash Attention 大窗口建模、大核蒸馏模块和跨层参数共享，在极低计算量下实现了与大模型可比的超分性能。

**[UniRain: Unified Image Deraining with RAG-based Dataset Distillation and Multi-objective Reweighted Optimization](unirain_unified_image_deraining_with_rag-based_dataset_distillation_and_multi-ob.md)**

:   提出 UniRain，一个统一的去雨框架，通过 RAG 驱动的数据集蒸馏从 200 万+ 公开图像对中筛选高质量训练样本，结合非对称 MoE 架构和多目标自适应重加权优化策略，首次在单一模型中同时处理白天/夜晚的雨条纹和雨滴四种退化。

**[Variational Garrote for Sparse Inverse Problems](variational_garrote_for_sparse_inverse_problems.md)**

:   在统一的稀疏逆问题框架下，系统比较 $\ell_1$ 正则化（LASSO）与 Variational Garrote（VG，一种变分 $\ell_0$ 近似方法），通过信号重采样、去噪和稀疏视角 CT 重建三个任务，证明 VG 在强欠定场景下能更准确地恢复稀疏支撑集，获得更低的泛化误差。
