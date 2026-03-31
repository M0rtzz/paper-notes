<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**📷 CVPR2026** · 共 **29** 篇

**[An FPGA Implementation of Displacement Vector Search for Intra Pattern Copy in JPEG XS](an_fpga_implementation_of_displacement_vector_sear.md)**

:   首次提出JPEG XS帧内模式复制(IPC)中位移矢量(DV)搜索模块的FPGA实现方案，采用四级流水线架构和IPC Group对齐的内存组织策略，在Xilinx Artix-7上实现38.3 Mpixels/s吞吐和277 mW功耗。

**[An FPGA Implementation of Displacement Vector Search for Intra Pattern Copy in JPEG XS](an_fpga_implementation_of_displacement_vector_search_for_intra_pattern_copy_in_j.md)**

:   针对 JPEG XS 屏幕内容编码中 Intra Pattern Copy（IPC）模块的位移向量（DV）搜索计算瓶颈，首次提出四级流水线 FPGA 架构并设计基于 IPC Group 对齐的内存组织方式，在 Xilinx Artix-7 上实现 38.3 Mpixels/s 吞吐量和 277 mW 功耗，为 IPC 的实际硬件部署提供了可行方案。

**[ARCHE: Autoregressive Residual Compression with Hyperprior and Excitation](arche_autoregressive_residual_compression_with_hyp.md)**

:   在全卷积架构内统一层级超先验、Masked PixelCNN空间自回归、通道条件建模和SE通道激励，不使用Transformer或循环组件，以95M参数和222ms解码时间实现相对Ballé基线48% BD-Rate降低并超越VVC Intra 5.6%。

**[ARCHE: Autoregressive Residual Compression with Hyperprior and Excitation](arche_autoregressive_residual_compression_with_hyperprior_and_excitation.md)**

:   提出 ARCHE 端到端图像压缩框架，在无 Transformer 和循环模块的纯卷积架构下，通过统一层级超先验、Masked PixelCNN 空间自回归上下文、通道条件化、SE 通道重标定和潜在残差预测五个互补组件，在 Kodak 上相对 Balle 基线降低 48% BD-Rate、相对 VVC Intra 降低 5.6%，同时仅需 95M 参数和 222ms 解码时间。

**[BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers](binaryattention_one-bit_qk-attention_for_vision_and_diffusion_transformers.md)**

:   提出 BinaryAttention，将 Transformer 注意力中的 Query 和 Key 量化为 1-bit 二值表示，通过 XNOR + popcount 位运算替代浮点点积，在 A100 上实现比 FlashAttention2 快 2 倍以上的加速，同时在视觉分类/检测/分割/扩散生成等任务上性能持平甚至超越全精度注意力。

**[DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation](dage_dual-stream_architecture_for_efficient_and_fine-grained_geometry_estimation.md)**

:   提出 DAGE 双流 Transformer 架构，将全局一致性建模（低分辨率流）与细粒度细节保持（高分辨率流）解耦，通过轻量 Cross-Attention Adapter 融合，实现 2K 分辨率和 1000 帧长序列上的高质量深度/点图估计和位姿预测，速度比 Pi3 快 2-28 倍，视频几何估计取得新 SOTA。

**[DisCa: Accelerating Video Diffusion Transformers with Distillation-Compatible Learnable Feature Caching](disca_accelerating_video_diffusion_transformers_wi.md)**

:   DisCa 首次提出"可学习特征缓存 + 步蒸馏"兼容的加速方案：用轻量神经预测器替代传统手工缓存策略，并通过 Restricted MeanFlow 稳定大规模视频模型的蒸馏，在 HunyuanVideo 上实现 11.8× 近无损加速。

**[Disca Accelerating Video Diffusion Transformers With Distillation-Compatible Lea](disca_accelerating_video_diffusion_transformers_with_distillation-compatible_lea.md)**

:   提出 DisCa，首次将**可学习特征缓存**与**步骤蒸馏**相结合，通过轻量级神经预测器替代手工缓存策略，并设计 Restricted MeanFlow 稳定大规模视频模型蒸馏，在 HunyuanVideo 上实现 11.8× 加速且几乎无质量损失。

**[Distilling Balanced Knowledge from a Biased Teacher](distilling_balanced_knowledge_from_a_biased_teacher.md)**

:   针对长尾分布下知识蒸馏中教师模型向头部类偏斜的问题，将传统 KL 散度损失分解为跨组损失和组内损失两个组件，通过重平衡跨组损失校准教师的组级预测、重加权组内损失保证各组等贡献，在 CIFAR-100-LT/TinyImageNet-LT/ImageNet-LT 上全面超越现有方法，甚至超过教师模型自身表现。

**[DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression](dit-ic_aligned_diffusion_transformer_for_efficient_image_compression.md)**

:   提出 DiT-IC，将预训练T2I扩散Transformer通过三种对齐机制（方差引导重建流、自蒸馏对齐、潜表示条件引导）适配为单步图像压缩重建模型，在32×下采样的深层潜空间执行扩散，实现SOTA感知质量且解码速度比现有扩散压缩编解码器快30×。

**[DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression](ditic_aligned_diffusion_transformer_for_efficient.md)**

:   将预训练文生图 DiT 适配为高效单步图像压缩解码器，通过方差引导重建流、自蒸馏对齐和潜空间条件引导三种对齐机制，在 32× 下采样的深层潜空间中实现 SOTA 感知质量，同时比现有扩散压缩方法解码快 30 倍。

**[FAIR-Pruner: Leveraging Tolerance of Difference for Flexible Automatic Layer-Wise Neural Network Pruning](fair-pruner_leveraging_tolerance_of_difference_for_flexible_automatic_layer-wise.md)**

:   提出 FAIR-Pruner 结构化剪枝框架，通过 Tolerance of Differences（ToD）指标协调两个互补视角：基于类条件可分性的 Wasserstein Utilization Score（识别冗余单元）和基于 Taylor 展开的 Reconstruction Score（保护关键单元），自动确定逐层非均匀剪枝率且支持免搜索灵活调整压缩比，在 CIFAR-10/SVHN/ImageNet 上取得 SOTA。

**[From Fewer Samples To Fewer Bits Reframing Dataset Distillation As Joint Optimiz](from_fewer_samples_to_fewer_bits_reframing_dataset_distillation_as_joint_optimiz.md)**

:   提出 QuADD 框架，将可微量化模块嵌入数据集蒸馏循环中，联合优化合成数据与量化参数，实现在固定比特预算下"更少样本 + 更低精度"的帕累托最优压缩。

**[Generative Neural Video Compression via Video Diffusion Prior](generative_neural_video_compression_via_video_diffusion_prior.md)**

:   提出 GNVC-VD，首个基于 DiT 视频扩散模型（Wan2.1）的生成式神经视频压缩框架，通过 flow-matching 在时空潜变量上进行序列级生成式精炼，在极低码率（<0.03 bpp）下实现感知质量 SOTA 并显著减少闪烁伪影。

**[Generative Video Compression with One-Dimensional Latent Representation](generative_video_compression_with_one-dimensional_latent_representation.md)**

:   提出 GVC1D，首次将视频压缩的潜在表示从2D网格替换为紧凑的1D token序列，结合1D记忆模块建模长期时序上下文，在感知质量指标上实现 60%+ 的码率节省。

**[GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration](geochemad_benchmarking_unsupervised_geochemical_an.md)**

:   发布首个开源多区域多元素地球化学异常检测基准 GeoChemAD（8 子集，覆盖沉积物/岩屑/土壤三类采样源和 Au/Cu/Ni/W 四种目标元素），并提出 GeoChemFormer——两阶段 Transformer 框架，先学空间上下文再做元素依赖建模，平均 AUC 达 0.7712 超越所有基线。

**[GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration](geochemad_benchmarking_unsupervised_geochemical_anomaly_detection_for_mineral_ex.md)**

:   提出 GeoChemAD 开源基准数据集和 GeoChemFormer 框架，通过空间上下文学习与元素依赖建模实现无监督地球化学异常检测，在8个子集上平均 AUC 达到 0.7712。

**[HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers](hiap_a_multigranular_stochastic_autopruning_framew.md)**

:   提出HiAP——统一宏观（整头/FFN块）和微观（头内维度/FFN神经元）的层级Gumbel-Sigmoid门控框架，在单次端到端训练中自动发现满足算力预算的高效ViT子网络，无需手动重要性排序或多阶段流程。

**[Hieramp Coarse-To-Fine Autoregressive Amplification For Generative Dataset Disti](hieramp_coarse-to-fine_autoregressive_amplification_for_generative_dataset_disti.md)**

:   提出 HierAmp，在视觉自回归（VAR）模型的粗到细生成过程中，向每个尺度注入可学习的类别 token 识别语义显著区域，并通过正 logit 偏置放大这些区域的注意力，使蒸馏数据在粗尺度获得更丰富多样的布局、在细尺度聚焦于类别相关细节，在多个数据集蒸馏基准上达到 SOTA。

**[Learning Through Creation A Hash-Free Framework For On-The-Fly Category Discover](learning_through_creation_a_hash-free_framework_for_on-the-fly_category_discover.md)**

:   提出 LTC 框架，通过在训练阶段利用 MKEE（最小化核能量+最大化熵）在线生成伪未知类样本，配合双最大间隔损失和自适应阈值，在7个数据集上实现1.5%–13.1%的全类精度提升，彻底摆脱了哈希编码对细粒度语义的损害。

**[MXNorm: Reusing MXFP block scales for efficient tensor normalisation](mxnorm_reusing_mxfp_block_scales_for_efficient_ten.md)**

:   MXNorm 提出将 RMSNorm 与 MXFP 量化融合：利用 MXFP 量化过程中已经计算好的 block absmax 来近似 RMS 值，从而省掉单独的归一化 reduction 操作，在 Llama 3 最高 8B 参数的预训练中保持训练精度，同时在 GB200 上实现最高 2.4 倍的 kernel 加速。

**[OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport](otprune_distribution-aligned_visual_token_pruning_via_optimal_transport.md)**

:   将视觉 token 裁剪建模为最优传输（OT）下的分布对齐问题，通过最小化完整与裁剪后 token 集合间的 2-Wasserstein 距离，以 Gaussian 代理 + log-det 子模目标 + 贪心 Cholesky 选择实现 training-free、$O(mk^2)$ 复杂度的高效裁剪，在 11 个多模态基准上取得 SOTA 精度-效率折中。

**[Pixel2Phys: Distilling Governing Laws from Visual Dynamics](pixel2phys_distilling_governing_laws_from_visual_dynamics.md)**

:   提出 Pixel2Phys，一个基于 MLLM 的多智能体协作框架，通过 Plan-Variable-Equation-Experiment 四个 Agent 的迭代假设-验证-精化循环，从原始视频中自动发现可解释的物理控制方程，外推精度比基线提升 45.35%。

**[Planning In 8 Tokens A Compact Discrete Tokenizer For Latent World Model](planning_in_8_tokens_a_compact_discrete_tokenizer_for_latent_world_model.md)**

:   提出 CompACT，将每张图像压缩至仅 8 个离散 token（约 128 bits），通过冻结预训练视觉编码器保留规划关键语义信息、生成式解码补充感知细节，使基于世界模型的规划速度提升约 40 倍且精度不降。

**[PPCL: Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers](ppcl_pluggable_pruning_dit_distillation.md)**

:   提出 PPCL 框架对大型扩散 Transformer (DiT, 8-20B 参数) 进行结构化剪枝: 通过线性探针+CKA 一阶差分识别连续冗余层区间, 深度方向+宽度方向联合剪枝, 搭配即插即用交替蒸馏, 在 Qwen-Image 20B 上实现 50% 参数缩减, 仅 3% 生成质量下降.

**[QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models](quantvla_scale-calibrated_post-training_quantization_for_vision-language-action_.md)**

:   提出 QuantVLA，首个面向 Vision-Language-Action (VLA) 模型的免训练后量化框架，通过选择性量化布局和两个轻量级标定机制（注意力温度匹配 ATM 和输出头平衡 OHB），在 W4A8 精度下实现约 70% 的内存节省，同时任务成功率超过全精度基线。

**[Rl-Scaniqa Reinforcement-Learned Scanpaths For Blind 360Image Quality Assessment](rl-scaniqa_reinforcement-learned_scanpaths_for_blind_360image_quality_assessment.md)**

**[Soda Sensitivity-Oriented Dynamic Acceleration For Diffusion Transformer](soda_sensitivity-oriented_dynamic_acceleration_for_diffusion_transformer.md)**

:   提出 SODA，通过离线细粒度敏感度建模 + 动态规划优化缓存间隔 + 统一自适应剪枝策略，在无需训练的条件下对 Diffusion Transformer 实现可控加速比下的高保真生成。

**[Talon Test-Time Adaptive Learning For On-The-Fly Category Discovery](talon_test-time_adaptive_learning_for_on-the-fly_category_discovery.md)**

:   提出首个面向 on-the-fly 类别发现（OCD）的测试时自适应框架 TALON，通过语义感知原型更新 + 稳定编码器适应 + 边距感知 logit 校准，摒弃哈希编码在连续特征空间直接建模，大幅缓解类别爆炸并显著提升新类发现精度。
