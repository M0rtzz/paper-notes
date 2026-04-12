---
title: >-
  ECCV2024 视频理解方向 13篇论文解读
description: >-
  13篇ECCV2024 视频理解方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🎞️ ECCV2024** · 共 **13** 篇

**[Actionswitch Class-Agnostic Detection Of Simultaneous Actions In Streaming Video](actionswitch_class-agnostic_detection_of_simultaneous_actions_in_streaming_video.md)**

:   提出 ActionSwitch——首个无需类别信息即可检测流式视频中重叠动作实例的在线时序动作定位（On-TAL）框架，核心将多动作检测建模为有限状态机的状态分类问题，并辅以 conservativeness loss 减少碎片化误检，在 THUMOS14、FineAction、Epic-Kitchens 100 等数据集上在 OAD 扩展方法中达到 SOTA。

**[Adapt2Reward Adapting Videolanguage Models To Generalizable](adapt2reward_adapting_videolanguage_models_to_generalizable.md)**

:   提出 Adapt2Reward，通过可学习的失败提示（failure prompts）将预训练视频语言模型适配为可泛化的语言条件奖励函数，仅需少量单一环境的机器人数据即可泛化到新环境和新任务，在 MetaWorld 上比前方法高出约 28%。

**[Amego Active Memory From Long Egocentric Videos](amego_active_memory_from_long_egocentric_videos.md)**

:   提出 AMEGO，一种从长第一人称视频中在线构建结构化"活跃记忆"的方法，通过 HOI tracklet + 位置分段 + 语义无关的视觉查询，在新提出的 AMB benchmark 上超越 Video QA baselines 12.7%。

**[Benchmarks And Challenges In Pose Estimation For Egocentric Hand Interactions Wi](benchmarks_and_challenges_in_pose_estimation_for_egocentric_hand_interactions_wi.md)**

:   基于 HANDS23 挑战赛（AssemblyHands + ARCTIC 数据集），系统性地对第一人称视角下手-物体交互的 3D 姿态估计方法进行了基准测试和深入分析，揭示了畸变校正、高容量 Transformer 和多视角融合的有效性，以及快速运动、遮挡和窄视角下物体重建等仍未解决的挑战。

**[Blazebvd Make Scale-Time Equalization Great Again For Blind Video Deflickering](blazebvd_make_scale-time_equalization_great_again_for_blind_video_deflickering.md)**

:   提出 BlazeBVD，利用经典 Scale-Time Equalization (STE) 在光照直方图空间提取 deflickering 先验（滤波光照图、曝光图、闪烁帧索引），将复杂的视频时空学习简化为 2D 空间网络逐帧处理 + 轻量 3D 时序一致性网络，在盲视频去闪烁任务上实现 SOTA 质量且推理速度比基线快 10 倍以上。

**[Classification Matters Improving Video Action Detection With Class-Specific Atte](classification_matters_improving_video_action_detection_with_class-specific_atte.md)**

:   提出类别专属查询（class queries）机制，通过为每个动作类别分配独立的可学习查询，让模型动态关注与各类别相关的上下文区域，显著提升视频动作检测中的分类性能。

**[Crossglg Llm Guides One-Shot Skeleton-Based 3D Action Recognition In A Cross-Lev](crossglg_llm_guides_one-shot_skeleton-based_3d_action_recognition_in_a_cross-lev.md)**

:   提出CrossGLG框架，利用LLM生成的文本描述以"全局→局部→全局"的方式引导骨架特征学习，在单样本3D动作识别中以仅2.8%的SOTA模型参数量大幅超越对手。

**[Data Collection-Free Masked Video Modeling](data_collection-free_masked_video_modeling.md)**

:   提出基于伪运动生成器（PMG）从静态图像递归生成伪运动视频，结合掩码视频建模（VideoMAE）进行自监督预训练，完全摆脱真实视频数据的采集成本和隐私/版权顾虑，甚至可用合成图像实现有效的视频Transformer预训练。

**[Dino-Tracker Taming Dino For Self-Supervised Point Tracking In A Single Video](dino-tracker_taming_dino_for_self-supervised_point_tracking_in_a_single_video.md)**

:   提出DINO-Tracker，将预训练DINOv2的语义特征与测试时单视频优化相结合，通过Delta-DINO残差微调和多源自监督损失实现长程稠密点追踪，在自监督方法中达到SOTA且可媲美有监督追踪器，尤其在长期遮挡场景中大幅领先。

**[Draganything Motion Control For Anything Using Entity Representation](draganything_motion_control_for_anything_using_entity_representation.md)**

:   提出DragAnything，利用扩散模型的隐空间特征作为实体表征（Entity Representation）来实现实体级运动控制，解决了现有轨迹驱动方法仅拖拽像素而无法精确控制目标对象运动的问题，在VIPSeg上实现SOTA的FVD/FID指标，用户研究中运动控制投票超出DragNUWA 26%。

**[Egoposer Robust Real-Time Egocentric Pose Estimation From Sparse And Intermitten](egoposer_robust_real-time_egocentric_pose_estimation_from_sparse_and_intermitten.md)**

:   提出 EgoPoser，仅从头显设备的头部和手部稀疏且间歇性追踪信号中，鲁棒地估计全身姿态，通过全局运动分解、真实视野建模、SlowFast时序融合和体型感知优化四大核心设计，在大规模真实场景中实现SOTA性能，推理速度超600fps。

**[On The Utility Of 3D Hand Poses For Action Recognition](on_the_utility_of_3d_hand_poses_for_action_recognition.md)**

:   提出 HandFormer，一种轻量级多模态 Transformer，将密集采样的 3D 手部姿态（捕捉细粒度动作）与稀疏采样的 RGB 帧（提供场景语义）结合，通过 micro-action 时序分解和 trajectory 编码高效建模手-物交互，在 Assembly101 和 H2O 上达到 SOTA，且纯 pose 模型以 5× 更少 FLOPs 超越已有骨架方法。

**[R2Tuning Efficient Imagetovideo Transfer Learning For Video](r2tuning_efficient_imagetovideo_transfer_learning_for_video.md)**

:   R²-Tuning提出了一个仅需1.5%参数的轻量R²Block，通过从CLIP后层向前层的逆向递归方式聚合多层空间特征并精化时序关联，在6个VTG基准上以2.7M参数超越了使用额外时序骨干的4倍大方法。
