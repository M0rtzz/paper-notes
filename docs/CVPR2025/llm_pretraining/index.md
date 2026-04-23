---
title: >-
  CVPR2025 预训练方向 12篇论文解读
description: >-
  12篇CVPR2025 预训练论文解读，主题涵盖：提出跨任务少样本2D视线估计——利用预训练3D视线、提出异构半监督学习(HSSL)新问题设定——标记数、首次提出"系统差距"（System等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📚 预训练

**📷 CVPR2025** · **12** 篇论文解读

**[3D Prior is All You Need: Cross-Task Few-shot 2D Gaze Estimation](3d_prior_is_all_you_need_cross-task_few-shot_2d_gaze_estimation.md)**

:   提出跨任务少样本2D视线估计——利用预训练3D视线模型作为先验，通过**基于物理的可微投影模块**（6个可学习屏幕参数）将3D视线方向投影到2D屏幕坐标，仅需10张标注图像即可在未知设备上适配2D视线估计，在MPIIGaze/EVE/GazeCapture上比EFE和IVGaze提升超25%。

**[A Unified Framework for Heterogeneous Semi-supervised Learning](a_unified_framework_for_heterogeneous_semi-supervised_learning.md)**

:   提出异构半监督学习(HSSL)新问题设定——标记数据和无标记数据来自不同分布的域，目标是训练能在两个域上都泛化的模型；通过将C类问题扩展为2C类分类（每个域的同一语义类视为不同类），结合WMA伪标签、跨域原型对齐和渐进式跨域Mixup三个组件统一解决。

**[Bridging the Vision-Brain Gap with an Uncertainty-Aware Blur Prior](bridging_the_vision-brain_gap_with_an_uncertainty-aware_blur_prior.md)**

:   首次提出"系统差距"（System GAP）和"随机差距"（Random GAP）的概念来描述脑信号与视觉刺激之间的信息不匹配，通过不确定性感知的模糊先验（UBP）动态调整图像模糊程度来缓解训练中的过拟合，在 200-way 零样本脑-图像检索任务上实现 50.9% top-1 准确率，超越前 SOTA 13.7 个百分点。

**[DreamText: High Fidelity Scene Text Synthesis](dreamtext_high_fidelity_scene_text_synthesis.md)**

:   DreamText重构扩散模型训练流程，引入字符级别的均衡监督(balanced supervision)和启发式交替优化策略来校正字符注意力，结合文本编码器与生成器的联合训练学习多样化字体风格，在场景文字合成任务上大幅超越SOTA方法（SeqAcc从UDiffText的0.763提升至0.940）。

**[HSEmotion Team at ABAW-10 Competition: Facial Expression Recognition, Valence-Arousal Estimation, Action Unit Detection and Fine-Grained Violence Classification](hsemotion_team_at_abaw-10_competition_facial_expression_recognition_valence-arou.md)**

:   HSEmotion 团队在 ABAW-10 竞赛中提出了一个轻量级 pipeline：用预训练 EfficientNet 提取面部 embedding，结合 MLP + GLA（Generalized Logit Adjustment）+ 滑窗平滑，在四项任务（EXPR/VA/AU/VD）上均大幅超过官方 baseline，其中暴力检测任务使用 ConvNeXt-T + TCN 达到 0.783 macro F1。

**[Improving Autoregressive Visual Generation with Cluster-Oriented Token Prediction](improving_autoregressive_visual_generation_with_cluster-oriented_token_predictio.md)**

:   提出 IAR，通过平衡 K-means 重排 VQGAN 码本使相似 embedding 具有相邻索引，配合簇导向交叉熵损失引导模型正确预测目标 token 所在的语义簇，在 LlamaGen 100M-1.4B 各规模上将训练时间减半且提升生成质量。

**[Lost in Translation, Found in Context: Sign Language Translation with Contextual Cues](lost_in_translation_found_in_context_sign_language_translation_with_contextual_c.md)**

:   通过引入背景视频描述、历史翻译和伪词汇表三种上下文线索，结合Llama3-8B的LoRA微调，实现了连续手语到文本的精确翻译，在BOBSL数据集上相比SOTA提升40%以上。

**[MXNorm: Reusing MXFP block scales for efficient tensor normalisation](mxnorm_reusing_mxfp_block_scales_for_efficient_tensor_normalisation.md)**

:   MXNorm 提出复用 MXFP 量化过程中已计算的 block absmax 来近似 RMS，将归一化与 MX 量化融合为单次统计收集操作，实现 RMSNorm 的 drop-in 替换，在 Llama 3 8B 预训练中保持训练精度的同时获得最高 2.4× 的 kernel 加速。

**[Precise Event Spotting in Sports Videos: Solving Long-Range Dependency and Class Imbalance](precise_event_spotting_in_sports_videos_solving_long-range_dependency_and_class_.md)**

:   提出端到端可训练的精确事件定位框架，通过自适应时空精炼模块（ASTRM）增强特征的时空信息，并引入Soft Instance Contrastive（SoftIC）损失解决类别不平衡问题，在SoccerNet V2 tight设置上以73.74 mAP超越SOTA。

**[ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model](scamo_exploring_the_scaling_law_in_autoregressive_motion_generation_model.md)**

:   首次在人类动作生成领域系统验证缩放律，提出包含Motion FSQ-VAE（解决codebook collapse）、260小时MotionUnion数据集和文本前缀自回归Transformer的可扩展系统ScaMo，发现归一化测试损失与FLOPs的对数律以及词汇参数/模型参数/数据量与FLOPs的幂律关系，并在$1\times 10^{18}$FLOPs预算下成功预测最优配置。

**[SoftShadow: Leveraging Soft Masks for Penumbra-Aware Shadow Removal](softshadow_leveraging_soft_masks_for_penumbra-aware_shadow_removal.md)**

:   提出SoftShadow框架，用连续灰度软掩码替代传统二值硬掩码来表示阴影区域，通过SAM+LoRA预测软掩码并引入半影形成约束损失联合训练检测与去阴影网络，在SRD/ISTD+/LRSS/UIUC四个数据集上达到SOTA且无需外部掩码输入。

**[The Scene Language: Representing Scenes with Programs, Words, and Embeddings](the_scene_language_representing_scenes_with_programs_words_and_embeddings.md)**

:   提出 Scene Language——一种用程序（P, 编码层级结构）+ 词语（W, 语义类别）+ 嵌入（Z, 视觉身份）三元组 $\Phi(s)=(W,P,Z)$ 表示视觉场景的新范式，通过 Claude 3.5 Sonnet 的 training-free 推理从文本/图像输入生成场景表示，支持传统/神经/混合渲染，在 3D/4D 场景生成质量和可控编辑上超越场景图等现有表示。
