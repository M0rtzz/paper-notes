<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**📷 CVPR2026** · 共 **8** 篇

**[Anticipatory Planning for Multimodal AI Agents](anticipatory_planning_for_multimodal_ai_agents.md)**

:   提出 TraceR1，一个两阶段 RL 框架：第一阶段通过轨迹级奖励优化让智能体学会"向前看几步"的前瞻性规划，第二阶段通过工具执行反馈做 grounded fine-tuning 来提升单步精度，在 7 个 GUI 和工具使用 benchmark 上取得了开源 SOTA。

**[CCCaption: Dual-Reward Reinforcement Learning for Complete and Correct Image Captioning](cccaption_dual-reward_reinforcement_learning_for_complete_and_correct_image_capt.md)**

:   提出 CCCaption 双奖励强化学习框架，通过 completeness reward（基于多 MLLM 生成的视觉 query 集）和 correctness reward（基于 caption 分解后的子 query 幻觉检测）联合优化图像描述的完整性和正确性，2B 模型超越 32B 基线。

**[Cross-modal Identity Mapping: Minimizing Information Loss in Modality Conversion via Reinforcement Learning](cross-modal_identity_mapping_minimizing_information_loss_in_modality_conversion_.md)**

:   提出 Cross-modal Identity Mapping (CIM)，通过分析用 caption 检索到的图像的表示一致性（GRC）和与源图像的相关性（QIR）来量化图像描述中的信息损失，将其作为 RL 奖励信号训练 LVLM 生成细粒度且精确的描述，无需额外标注。

**[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](dreamvideo-omni_omni-motion_controlled_multi-subject_video_customization_with_la.md)**

:   提出 DreamVideo-Omni，通过两阶段渐进训练范式（全运动身份监督微调 + 潜空间身份奖励反馈学习），在单一 DiT 架构中首次统一实现多主体定制与全粒度运动控制（全局包围盒 + 局部轨迹 + 相机运动）。

**[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](dreamvideoomni_omnimotion_controlled_multisubject.md)**

:   统一框架同时实现多主体身份定制和全运动控制（全局运动 + 局部运动 + 相机运动），通过渐进式两阶段训练（有监督微调 + 潜空间身份奖励反馈学习）解决身份保持与运动控制之间的固有冲突。

**[GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion](graspldp_towards_generalizable_grasping_policy_via_latent_diffusion.md)**

:   提出 GraspLDP，将预训练抓取检测器的 grasp pose 先验和 graspness map 视觉线索注入潜在扩散策略框架，通过 VAE 编码的动作潜空间引导和自监督重建目标，显著提升抓取精度和泛化能力。

**[Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment](lifelong_imitation_learning_multimodal_latent_rep.md)**

:   提出终身模仿学习框架，通过多模态潜在回放（MLR）在冻结编码器的特征空间中存储和回放紧凑表示，并引入增量特征调整（IFA）机制用角距离约束维持任务间可分性，在LIBERO基准上AUC提升10-17点、遗忘降低最多65%。

**[Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment](lifelong_imitation_learning_with_multimodal_latent_replay_and_incremental_adjust.md)**

:   提出终身模仿学习框架，通过 Multimodal Latent Replay（在冻结编码器的潜空间中存储和回放紧凑多模态特征）和 Incremental Feature Adjustment（基于角距离的自适应间隔约束防止任务间表示漂移），在 LIBERO 基准上实现 AUC 提升 10-17 点、遗忘减少 65%。
