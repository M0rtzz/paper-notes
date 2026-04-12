---
title: >-
  CVPR2026 模型压缩方向 34篇论文解读
description: >-
  34篇CVPR2026 模型压缩方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**📷 CVPR2026** · 共 **34** 篇

**[A Paradigm Shift Fully End-To-End Training For Temporal Sentence Grounding In Vi](a_paradigm_shift_fully_end-to-end_training_for_temporal_sentence_grounding_in_vi.md)**

:   提出首个完全端到端的时序语句定位(TSGV)框架，通过语句条件适配器(SCADA)将语句嵌入注入视频backbone的中间层来动态调制视觉特征，配合视频中心学习策略加速训练，在Charades-STA和ActivityNet上超越SOTA。

**[An Fpga Implementation Of Displacement Vector Sear](an_fpga_implementation_of_displacement_vector_sear.md)**

:   首次提出JPEG XS帧内模式复制(IPC)中位移矢量(DV)搜索模块的FPGA实现方案，采用四级流水线架构和IPC Group对齐的内存组织策略，在Xilinx Artix-7上实现38.3 Mpixels/s吞吐和277 mW功耗。

**[An Fpga Implementation Of Displacement Vector Search For Intra Pattern Copy In J](an_fpga_implementation_of_displacement_vector_search_for_intra_pattern_copy_in_j.md)**

:   针对 JPEG XS 屏幕内容编码中 Intra Pattern Copy（IPC）模块的位移向量（DV）搜索计算瓶颈，首次提出四级流水线 FPGA 架构并设计基于 IPC Group 对齐的内存组织方式，在 Xilinx Artix-7 上实现 38.3 Mpixels/s 吞吐量和 277 mW 功耗，为 IPC 的实际硬件部署提供了可行方案。

**[Arche Autoregressive Residual Compression With Hyp](arche_autoregressive_residual_compression_with_hyp.md)**

:   在全卷积架构内统一层级超先验、Masked PixelCNN空间自回归、通道条件建模和SE通道激励，不使用Transformer或循环组件，以95M参数和222ms解码时间实现相对Ballé基线48% BD-Rate降低并超越VVC Intra 5.6%。

**[Arche Autoregressive Residual Compression With Hyperprior And Excitation](arche_autoregressive_residual_compression_with_hyperprior_and_excitation.md)**

:   提出 ARCHE 端到端图像压缩框架，在无 Transformer 和循环模块的纯卷积架构下，通过统一层级超先验、Masked PixelCNN 空间自回归上下文、通道条件化、SE 通道重标定和潜在残差预测五个互补组件，在 Kodak 上相对 Balle 基线降低 48% BD-Rate、相对 VVC Intra 降低 5.6%，同时仅需 95M 参数和 222ms 解码时间。

**[Beyond Loss Values Robust Dynamic Pruning Via Loss Trajectory Alignment](beyond_loss_values_robust_dynamic_pruning_via_loss_trajectory_alignment.md)**

:   提出AlignPrune——一个基于损失轨迹对齐的即插即用模块，通过Dynamic Alignment Score（DAS）替代传统损失值排序，使动态数据剪枝在噪声标签场景下准确率提升最高6.3%。

**[Binaryattention One-Bit Qk-Attention For Vision And Diffusion Transformers](binaryattention_one-bit_qk-attention_for_vision_and_diffusion_transformers.md)**

:   提出 BinaryAttention，将 Transformer 注意力中的 Query 和 Key 量化为 1-bit 二值表示，通过 XNOR + popcount 位运算替代浮点点积，在 A100 上实现比 FlashAttention2 快 2 倍以上的加速，同时在视觉分类/检测/分割/扩散生成等任务上性能持平甚至超越全精度注意力。

**[Cheem Continual Learning By Reuse New Adapt And Skip -- A Hierarchical Explorati](cheem_continual_learning_by_reuse_new_adapt_and_skip_--_a_hierarchical_explorati.md)**

:   提出 CHEEM 框架，通过分层探索-利用采样的 NAS 自动学习任务感知的动态 ViT 骨干——在每一层选择 Reuse/New/Adapt/Skip 四种操作——在 MTIL 和 VDD 两个挑战性持续学习基准上显著超越提示类方法，接近全量微调上界。

**[Critical Patch-Aware Sparse Prompting With Decoupled Training For Continual Lear](critical_patch-aware_sparse_prompting_with_decoupled_training_for_continual_lear.md)**

:   提出 CPS-Prompt 框架，通过任务感知的关键 patch 采样（CPS）和解耦 prompt-分类器训练（DPCT）两个模块，在边缘设备上实现 Prompt-based 持续学习的训练时内存和计算效率提升约 1.6 倍，同时准确率仅下降约 2%。

**[Dage Dual-Stream Architecture For Efficient And Fine-Grained Geometry Estimation](dage_dual-stream_architecture_for_efficient_and_fine-grained_geometry_estimation.md)**

:   提出 DAGE 双流 Transformer 架构，将全局一致性建模（低分辨率流）与细粒度细节保持（高分辨率流）解耦，通过轻量 Cross-Attention Adapter 融合，实现 2K 分辨率和 1000 帧长序列上的高质量深度/点图估计和位姿预测，速度比 Pi3 快 2-28 倍，视频几何估计取得新 SOTA。

**[Distilling Balanced Knowledge From A Biased Teacher](distilling_balanced_knowledge_from_a_biased_teacher.md)**

:   针对长尾分布下知识蒸馏中教师模型向头部类偏斜的问题，将传统 KL 散度损失分解为跨组损失和组内损失两个组件，通过重平衡跨组损失校准教师的组级预测、重加权组内损失保证各组等贡献，在 CIFAR-100-LT/TinyImageNet-LT/ImageNet-LT 上全面超越现有方法，甚至超过教师模型自身表现。

**[Fair-Pruner Leveraging Tolerance Of Difference For Flexible Automatic Layer-Wise](fair-pruner_leveraging_tolerance_of_difference_for_flexible_automatic_layer-wise.md)**

:   提出 FAIR-Pruner 结构化剪枝框架，通过 Tolerance of Differences（ToD）指标协调两个互补视角：基于类条件可分性的 Wasserstein Utilization Score（识别冗余单元）和基于 Taylor 展开的 Reconstruction Score（保护关键单元），自动确定逐层非均匀剪枝率且支持免搜索灵活调整压缩比，在 CIFAR-10/SVHN/ImageNet 上取得 SOTA。

**[From Fewer Samples To Fewer Bits Reframing Dataset Distillation As Joint Optimiz](from_fewer_samples_to_fewer_bits_reframing_dataset_distillation_as_joint_optimiz.md)**

:   提出 QuADD 框架，将可微量化模块嵌入数据集蒸馏循环中，联合优化合成数据与量化参数，实现在固定比特预算下"更少样本 + 更低精度"的帕累托最优压缩。

**[Generative Video Compression With One-Dimensional Latent Representation](generative_video_compression_with_one-dimensional_latent_representation.md)**

:   提出 GVC1D，首次将视频压缩的潜在表示从2D网格替换为紧凑的1D token序列，结合1D记忆模块建模长期时序上下文，在感知质量指标上实现 60%+ 的码率节省。

**[Geochemad Benchmarking Unsupervised Geochemical An](geochemad_benchmarking_unsupervised_geochemical_an.md)**

:   发布首个开源多区域多元素地球化学异常检测基准 GeoChemAD（8 子集，覆盖沉积物/岩屑/土壤三类采样源和 Au/Cu/Ni/W 四种目标元素），并提出 GeoChemFormer——两阶段 Transformer 框架，先学空间上下文再做元素依赖建模，平均 AUC 达 0.7712 超越所有基线。

**[Geochemad Benchmarking Unsupervised Geochemical Anomaly Detection For Mineral Ex](geochemad_benchmarking_unsupervised_geochemical_anomaly_detection_for_mineral_ex.md)**

:   提出 GeoChemAD 开源基准数据集和 GeoChemFormer 框架，通过空间上下文学习与元素依赖建模实现无监督地球化学异常检测，在8个子集上平均 AUC 达到 0.7712。

**[Hiap A Multi-Granular Stochastic Auto-Pruning Framework For Vision Transformers](hiap_a_multi-granular_stochastic_auto-pruning_framework_for_vision_transformers.md)**

:   HiAP 把 ViT 剪枝写成一个端到端的预算感知学习问题，同时对整头/整块和头内维度/FFN 神经元两种粒度做随机可微门控，在一次训练里自动长出满足算力预算的稠密子网络，省掉了常见的排序、阈值搜索和额外微调流程。

**[Hiap A Multigranular Stochastic Autopruning Framew](hiap_a_multigranular_stochastic_autopruning_framew.md)**

:   提出HiAP——统一宏观（整头/FFN块）和微观（头内维度/FFN神经元）的层级Gumbel-Sigmoid门控框架，在单次端到端训练中自动发现满足算力预算的高效ViT子网络，无需手动重要性排序或多阶段流程。

**[Hieramp Coarse-To-Fine Autoregressive Amplification For Generative Dataset Disti](hieramp_coarse-to-fine_autoregressive_amplification_for_generative_dataset_disti.md)**

:   提出 HierAmp，在视觉自回归（VAR）模型的粗到细生成过程中，向每个尺度注入可学习的类别 token 识别语义显著区域，并通过正 logit 偏置放大这些区域的注意力，使蒸馏数据在粗尺度获得更丰富多样的布局、在细尺度聚焦于类别相关细节，在多个数据集蒸馏基准上达到 SOTA。

**[Learning Through Creation A Hash-Free Framework For On-The-Fly Category Discover](learning_through_creation_a_hash-free_framework_for_on-the-fly_category_discover.md)**

:   提出 LTC 框架，通过在训练阶段利用 MKEE（最小化核能量+最大化熵）在线生成伪未知类样本，配合双最大间隔损失和自适应阈值，在7个数据集上实现1.5%–13.1%的全类精度提升，彻底摆脱了哈希编码对细粒度语义的损害。

**[Markovian Scale Prediction A New Era Of Visual Autoregressive Generation](markovian_scale_prediction_a_new_era_of_visual_autoregressive_generation.md)**

:   将视觉自回归模型 (VAR) 从全上下文依赖的 next-scale prediction 重构为基于马尔可夫过程的 Markovian scale prediction，通过滑动窗口历史补偿机制实现非全上下文建模，在 ImageNet 上 FID 降低 10.5%、峰值内存减少 83.8%。

**[Marvo Marine-Adaptive Radiance-Aware Visual Odometry](marvo_marine-adaptive_radiance-aware_visual_odometry.md)**

:   提出 MARVO 水下视觉里程计框架，将物理感知辐射适配器 (PARA) 嵌入 LoFTR 特征匹配器补偿水下波长衰减、结合 GTSAM 多传感器因子图融合和强化学习位姿图优化 (RL-PGO)，在水下场景实现鲁棒定位。

**[Mine-Jepa In-Domain Self-Supervised Learning For Mine-Like Object Classification](mine-jepa_in-domain_self-supervised_learning_for_mine-like_object_classification.md)**

:   提出 Mine-JEPA，首个面向侧扫声纳（SSS）水雷分类的域内自监督学习流水线——基于 SIGReg 正则化损失、声纳适配增强策略和 ImageNet 初始化，仅用 1,170 张未标注声纳图像预训练即超越了在 17 亿图像上预训练的 DINOv3 基础模型。

**[Parallax To Align Them All An Omniparallax Attention Mechanism For Distributed M](parallax_to_align_them_all_an_omniparallax_attention_mechanism_for_distributed_m.md)**

:   提出 OmniParallax Attention Mechanism (OPAM) 用于分布式多视角图像压缩（DMIC），通过两阶段视差注意力显式建模任意视角对之间的相关性和对齐特征，构建的 ParaHydra 框架首次让 DMIC 方法显著超越 SOTA MIC 编码器，同时大幅降低计算开销。

**[Planning In 8 Tokens A Compact Discrete Tokenizer For Latent World Model](planning_in_8_tokens_a_compact_discrete_tokenizer_for_latent_world_model.md)**

:   提出 CompACT，将每张图像压缩至仅 8 个离散 token（约 128 bits），通过冻结预训练视觉编码器保留规划关键语义信息、生成式解码补充感知细节，使基于世界模型的规划速度提升约 40 倍且精度不降。

**[Ppcl Pluggable Pruning Dit Distillation](ppcl_pluggable_pruning_dit_distillation.md)**

:   提出 PPCL 框架对大型扩散 Transformer (DiT, 8-20B 参数) 进行结构化剪枝: 通过线性探针+CKA 一阶差分识别连续冗余层区间, 深度方向+宽度方向联合剪枝, 搭配即插即用交替蒸馏, 在 Qwen-Image 20B 上实现 50% 参数缩减, 仅 3% 生成质量下降.

**[Quantvla Scale-Calibrated Post-Training Quantization For Vision-Language-Action ](quantvla_scale-calibrated_post-training_quantization_for_vision-language-action_.md)**

:   提出 QuantVLA，首个面向 Vision-Language-Action (VLA) 模型的免训练后量化框架，通过选择性量化布局和两个轻量级标定机制（注意力温度匹配 ATM 和输出头平衡 OHB），在 W4A8 精度下实现约 70% 的内存节省，同时任务成功率超过全精度基线。

**[RL-ScanIQA: Reinforcement-Learned Scanpaths for Blind 360° Image Quality Assessment](rl-scaniqa_reinforcement-learned_scanpaths_for_blind_360image_quality_assessment.md)**

**[Soda Sensitivity-Oriented Dynamic Acceleration For Diffusion Transformer](soda_sensitivity-oriented_dynamic_acceleration_for_diffusion_transformer.md)**

:   提出 SODA，通过离线细粒度敏感度建模 + 动态规划优化缓存间隔 + 统一自适应剪枝策略，在无需训练的条件下对 Diffusion Transformer 实现可控加速比下的高保真生成。

**[Talon Test-Time Adaptive Learning For On-The-Fly Category Discovery](talon_test-time_adaptive_learning_for_on-the-fly_category_discovery.md)**

:   提出首个面向 on-the-fly 类别发现（OCD）的测试时自适应框架 TALON，通过语义感知原型更新 + 稳定编码器适应 + 边距感知 logit 校准，摒弃哈希编码在连续特征空间直接建模，大幅缓解类别爆炸并显著提升新类发现精度。

**[Textf2Texthdr Two-Stage Hdr Video Reconstruction Via Flow Adapter And Physical M](textf2texthdr_two-stage_hdr_video_reconstruction_via_flow_adapter_and_physical_m.md)**

:   提出 F²HDR，一个两阶段 HDR 视频重建框架，通过 Flow Adapter 将通用预训练光流适配到交替曝光场景以实现鲁棒对齐，并利用物理运动建模从光流中提取连续运动掩码来引导第二阶段的伪影消除，在真实 HDR 视频基准上达到 SOTA。

**[Towards Generalizable Ai-Generated Image Detection Via Image-Adaptive Prompt Lea](towards_generalizable_ai-generated_image_detection_via_image-adaptive_prompt_lea.md)**

:   提出 Image-Adaptive Prompt Learning (IAPL)，在推理时根据每张测试图像动态调整 CLIP 编码器的 prompt，通过测试时 token 调优和条件信息学习器实现对未见生成器的强泛化，在 UniversalFakeDetect 和 GenImage 上分别达到 95.61% 和 96.7% 平均准确率的 SOTA 性能。

**[Unicomp Rethinking Video Compression Through Informational Uniqueness](unicomp_rethinking_video_compression_through_informational_uniqueness.md)**

:   提出基于信息唯一性（而非注意力）的视频 token 压缩框架 UniComp，通过帧组融合、token 分配和空间动态压缩三个模块在时序-空间-全局维度上最大化保留唯一信息，在仅保留 10% token 时仍能超越未压缩基线性能。

**[Unlocking Imagenets Multi-Object Nature Automated Large-Scale Multilabel Annotat](unlocking_imagenets_multi-object_nature_automated_large-scale_multilabel_annotat.md)**

:   提出全自动流水线，利用自监督 ViT 特征进行无监督目标发现，为 ImageNet-1K 全部 128 万训练图像生成带空间定位的多标签标注，无需人工标注，模型在域内和下游多标签任务上均获一致提升（ReaL +2.0 top-1, COCO +4.2 mAP）。
