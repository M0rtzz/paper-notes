<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🧠 NeurIPS2025** · 共 **23** 篇

**[Alligat0R: Pre-Training through Covisibility Segmentation for Relative Camera Pose Regression](alligat0r_pre-training_through_co-visibility_segmentation_for_relative_camera_po.md)**

:   用共视性分割（covisibility segmentation）替代 CroCo 的跨视图补全作为双目视觉预训练任务，对每个像素预测"共视/遮挡/视野外"三类标签，在低重叠场景下显著超越 CroCo，RUBIK 基准总体成功率 60.3% 排第一。

**[ARGenSeg: Image Segmentation with Autoregressive Image Generation Model](argenseg_image_segmentation_with_autoregressive_image_generation_model.md)**

:   提出ARGenSeg——首个利用自回归图像生成范式实现图像分割的统一MLLM框架，让模型直接输出visual tokens并通过VQ-VAE解码为分割mask，无需额外分割头，搭配next-scale prediction并行生成策略实现4×加速，在RefCOCO/+/g上以更少训练数据超越SOTA。

**[Attention (as Discrete-Time Markov) Chains](attention_as_discrete-time_markov_chains.md)**

:   将 softmax 归一化后的注意力矩阵重新解读为离散时间 Markov 链（DTMC）的转移概率矩阵，提出多跳注意力（Multi-Bounce）和 TokenRank（稳态分布，类似 PageRank）来捕获间接注意力路径和全局 token 重要性，在 ImageNet 分割上达 94.29% mAP，并增强 Self-Attention Guidance 的图像生成质量。

**[ConnectomeBench: Can LLMs Proofread the Connectome?](connectomebench_can_llms_proofread_the_connectome.md)**

:   提出 ConnectomeBench，首个评估多模态 LLM 在连接组校对（片段识别、分裂错误修正、合并错误检测）三项关键任务上能力的标准化基准；o4-mini 在分裂修正多选任务达 85%，但合并错误检测仍显著落后于人类专家。

**[COS3D: Collaborative Open-Vocabulary 3D Segmentation](cos3d_collaborative_open-vocabulary_3d_segmentation.md)**

:   提出COS3D协作式开放词汇3D分割框架，在3D Gaussian Splatting中同时维护instance field（学习清晰边界）和language field（学习语义），通过两阶段训练实现Ins2Lang映射，推理时Language→Instance prompt精化实现互补协作，在LeRF数据集上mIoU达50.76%，大幅超越Dr.Splat（43.58%）。

**[Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning](fast_and_fluent_diffusion_language_models_via_convolutional_decoding_and_rejecti.md)**

:   通过卷积解码归一化（替代硬半自回归分块）和基于规则的拒绝微调 R2FT，在 128 步推理下实现与 512+ 步相当的扩散语言模型生成质量，达到 DLM 领域 SOTA。

**[Fast Foreground-Aware Diffusion With Accelerated Sampling Trajectory For Segment](fast_foreground-aware_diffusion_with_accelerated_sampling_trajectory_for_segment.md)**

:   提出 FAST，一个面向分割的工业异常合成框架，通过前景感知重建模块（FARM）和异常感知加速采样（AIAS）在仅 10 步去噪下生成高质量合成异常，在 MVTec-AD 上 mIoU 达 76.72%，超越所有先前方法。

**[FineRS: Fine-grained Reasoning and Segmentation of Small Objects with Reinforcement Learning](finers_fine-grained_reasoning_and_segmentation_of_small_objects_with_reinforceme.md)**

:   提出 FineRS 两阶段 MLLM 强化学习框架（全局语义探索 GSE → 局部感知精化 LPR），通过 locate-informed retrospective reward 耦合两阶段，在自建 FineRS-4k UAV 高分辨率数据集上实现超小目标的推理与分割，gIoU 达 55.1%（超 Seg-Zero† 8.5%），同时支持 VQA（MVQA 83.3%）。

**[GTPBD: A Fine-Grained Global Terraced Parcel and Boundary Dataset](gtpbd_a_fine-grained_global_terraced_parcel_and_boundary_dataset.md)**

:   构建首个全球性细粒度梯田地块与边界数据集GTPBD，包含47,537张高分辨率影像（0.5-0.7m）和超20万个人工标注地块，提供三级标签支持语义分割、边缘检测、地块提取和无监督域适应四项任务，并在20种方法上进行全面基准评测。

**[HAODiff: Human-Aware One-Step Diffusion via Dual-Prompt Guidance](haodiff_human-aware_one-step_diffusion_via_dual-prompt_guidance.md)**

:   提出HAODiff，一种人体感知的单步扩散模型，通过三分支双提示引导（DPG）生成自适应正负提示对，结合显式人体运动模糊（HMB）退化管线和分类器自由引导（CFG），在人体图像复原任务上大幅超越现有SOTA方法。

**[HopaDIFF: Holistic-Partial Aware Fourier Conditioned Diffusion for Referring Human Action Segmentation in Multi-Person Scenarios](hopadiff_holistic-partial_aware_fourier_conditioned_diffusion_for_referring_huma.md)**

:   首次提出指称人体动作分割(RHAS)任务——通过文本描述定位多人视频中特定个体并做帧级动作分割。构建了包含133部电影、137个动作类别、33小时视频的RHAS133数据集，并提出基于全局-局部感知傅里叶条件扩散的HopaDIFF框架，在多种评估设置下显著超越现有基线。

**[HumanCrafter: Synergizing Generalizable Human Reconstruction and Semantic 3D Segmentation](humancrafter_synergizing_generalizable_human_reconstruction_and_semantic_3d_segm.md)**

:   提出HumanCrafter——首个统一单图3D人体重建与人体部位语义分割的前馈框架，通过人体几何先验引导的Transformer聚合多视角特征，结合DINOv2自监督语义先验构建3D特征场，在2K2K和THuman2.1上同时超越现有3D重建和分割SOTA。

**[InstructSAM: A Training-Free Framework for Instruction-Oriented Remote Sensing Object Recognition](instructsam_a_training-free_framework_for_instruction-oriented_remote_sensing_ob.md)**

:   定义指令导向目标计数/检测/分割(InstructCDS)新任务，构建EarthInstruct遥感基准（覆盖开放词汇/开放端/开放子类三种设置），提出InstructSAM——无需训练的框架：LVLM解析指令+计数、SAM2生成掩码提议、CLIP计算相似度，通过二进制整数规划(BIP)在计数约束下实现掩码-标签最优匹配，推理时间近乎恒定且优于专用基线。

**[Interpreting ResNet-based CLIP via Neuron-Attention Decomposition](interpreting_resnet-based_clip_via_neuron-attention_decomposition.md)**

:   提出神经元-注意力分解方法解释CLIP-ResNet：将模型输出分解为神经元与注意力池化头的成对贡献路径，发现这些neuron-head对可用单一方向近似、具有稀疏性且捕获子概念，并将其应用于免训练语义分割（PASCAL Context上mIoU 26.2%，超MaskCLIP 15%）和数据集分布偏移监测。

**[LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation](langhops_language_grounded_hierarchical_open-vocabulary_part_segmentation.md)**

:   提出LangHOPS，首个基于多模态大语言模型（MLLM）的开放词汇物体-部件实例分割框架，在语言空间中建立object-part层次关系，利用MLLM的知识和推理能力链接多粒度概念，在PartImageNet上以56.9% AP超越SOTA 5.5%，跨数据集设置超4.8%。

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
