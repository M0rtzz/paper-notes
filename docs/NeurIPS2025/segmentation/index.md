<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🧠 NeurIPS2025** · 共 **14** 篇

**[Alligat0R: Pre-Training through Covisibility Segmentation for Relative Camera Pose Regression](alligat0r_pre-training_through_co-visibility_segmentation_for_relative_camera_po.md)**

:   用共视性分割（covisibility segmentation）替代 CroCo 的跨视图补全作为双目视觉预训练任务，对每个像素预测"共视/遮挡/视野外"三类标签，在低重叠场景下显著超越 CroCo，RUBIK 基准总体成功率 60.3% 排第一。

**[ARGenSeg: Image Segmentation with Autoregressive Image Generation Model](argenseg_image_segmentation_with_autoregressive_image_generation_model.md)**

:   提出ARGenSeg——首个利用自回归图像生成范式实现图像分割的统一MLLM框架，让模型直接输出visual tokens并通过VQ-VAE解码为分割mask，无需额外分割头，搭配next-scale prediction并行生成策略实现4×加速，在RefCOCO/+/g上以更少训练数据超越SOTA。

**[Attention (as Discrete-Time Markov) Chains](attention_as_discrete-time_markov_chains.md)**

:   将 softmax 归一化后的注意力矩阵重新解读为离散时间 Markov 链（DTMC）的转移概率矩阵，提出多跳注意力（Multi-Bounce）和 TokenRank（稳态分布，类似 PageRank）来捕获间接注意力路径和全局 token 重要性，在 ImageNet 分割上达 94.29% mAP，并增强 Self-Attention Guidance 的图像生成质量。

**[Broken Tokens: Your Language Model Can Secretly Handle Non-Canonical Tokenization](broken_tokens_your_language_model_can_secretly_handle_non-canonical_tokenization.md)**

:   揭示 LLM 能秘密处理非标准分词（如将"Hello"拆为"He"+"llo"而非标准的"Hello"整词token）——即使输入的 token 序列与训练时不同，模型表现出惊人的鲁棒性，且这种能力来自嵌入空间中子词嵌入的线性组合近似整词嵌入的特性。

**[COS3D: Collaborative Open-Vocabulary 3D Segmentation](cos3d_collaborative_open-vocabulary_3d_segmentation.md)**

:   提出COS3D协作式开放词汇3D分割框架，在3D Gaussian Splatting中同时维护instance field（学习清晰边界）和language field（学习语义），通过两阶段训练实现Ins2Lang映射，推理时Language→Instance prompt精化实现互补协作，在LeRF数据集上mIoU达50.76%，大幅超越Dr.Splat（43.58%）。

**[Fast Foreground-Aware Diffusion With Accelerated Sampling Trajectory For Segment](fast_foreground-aware_diffusion_with_accelerated_sampling_trajectory_for_segment.md)**

:   提出 FAST，一个面向分割的工业异常合成框架，通过前景感知重建模块（FARM）和异常感知加速采样（AIAS）在仅 10 步去噪下生成高质量合成异常，在 MVTec-AD 上 mIoU 达 76.72%，超越所有先前方法。

**[Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks](mars-bench_a_benchmark_for_evaluating_foundation_models_for_mars_science_tasks.md)**

:   本文提出 Mars-Bench——首个面向火星科学任务的综合基准，涵盖20个数据集（分类/分割/目标检测三大任务类型），系统评估了 ImageNet 预训练模型、地球观测基础模型和视觉语言模型在火星数据上的表现，发现当前通用模型在火星领域仍有明显不足，呼吁开发火星专用基础模型。

**[OmniSegmentor: A Flexible Multi-Modal Learning Framework for Semantic Segmentation](omnisegmentor_a_flexible_multi-modal_learning_framework_for_semantic_segmentatio.md)**

:   OmniSegmentor 构建了含 5 种视觉模态的大规模 ImageNeXt 数据集（1.2M 样本），提出随机选择补充模态与 RGB 对齐的高效预训练策略，首次实现灵活的多模态预训练-微调流水线，在 6 个多模态语义分割基准上刷新 SOTA。

**[Panoptic Captioning An Equivalence Bridge For Image And Text](panoptic_captioning_an_equivalence_bridge_for_image_and_text.md)**

:   提出 Panoptic Captioning 新任务，追求图像的"最小文本等价"——生成包含所有实体、位置、属性、关系和全局状态的全面描述，13B 模型配合解耦学习即超越 78B 开源和 GPT-4o 等商业模型。

**[PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding](partonomy_large_multimodal_models_with_part-level_visual_understanding.md)**

:   提出 Partonomy 部件级分割 benchmark（862 部件标签/534 物体标签）和 Plum 模型（用 span 标记替代 [SEG] token + mask 反馈循环），发现 SOTA 分割 LMM 在部件理解上仅 5.9% gIoU，Plum 通过避免分布偏移和利用历史预测显著提升。

**[HCLFuse: Revisiting Generative Infrared and Visible Image Fusion Based on Human Cognitive Laws](revisiting_generative_infrared_and_visible_image_fusion_based_on_human_cognitive.md)**

:   HCLFuse 基于信息瓶颈原理和最优传输理论进行模态对齐，设计变分瓶颈编码器（VBE）+ 物理引导条件扩散模型，融合热传导/结构保持/物理一致性三种约束到扩散过程中，在 MSRS 数据集上梯度指标 AG 提升 69.87%，空间频率 SF 提升 39.41%。

**[Robust Ego-Exo Correspondence with Long-Term Memory](robust_ego-exo_correspondence_with_long-term_memory.md)**

:   提出LM-EEC，基于SAM 2的自中心-外中心(ego-exo)视频跨视角目标分割框架，通过Memory-View MoE自适应融合记忆特征与跨视角特征，配合双记忆库压缩策略保持长期信息，在EgoExo4D基准上大幅超越现有方法（Ego2Exo IoU 54.98 vs 38.26）。

**[Robust Egocentric Referring Video Object Segmentation Via Dual-Modal Causal Inte](robust_egocentric_referring_video_object_segmentation_via_dual-modal_causal_inte.md)**

:   提出CERES框架，通过双模态因果干预解决自中心指代视频分割(Ego-RVOS)中的鲁棒性问题：对语言偏见用后门调整（消除目标-动作频率偏差），对视觉混淆用前门调整（以深度信息引导视觉中介变量聚合），在VISOR/VOST/VSCOS上达到SOTA。

**[Towards Robust Pseudo-Label Learning In Semantic Segmentation An Encoding Perspe](towards_robust_pseudo-label_learning_in_semantic_segmentation_an_encoding_perspe.md)**

:   提出 ECOCSeg，用纠错输出码（ECOC）替代 one-hot 编码来表示伪标签，将 N 类分类分解为 K 个二分类子任务，通过 bit 级去噪和可靠位挖掘生成更鲁棒的伪标签，在 UDA 和 SSL 分割任务上一致提升。
