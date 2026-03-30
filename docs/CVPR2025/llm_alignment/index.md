<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚖️ 对齐 / RLHF

**📷 CVPR2025** · 共 **5** 篇

**[Bases of Steerable Kernels for Equivariant CNNs: From 2D Rotations to the Lorentz Group](bases_of_steerable_kernels_for_equivariant_cnns_from_2d_rotations_to_the_lorentz.md)**

:   提出一种求解可转向等变 CNN 核约束方程的替代方法，通过在不动点处求解更简单的不变性条件再"转向"到任意点，绕过了计算 Clebsch-Gordan 系数的需要，为 SO(2)、O(2)、SO(3)、O(3) 及 Lorentz 群给出了显式的核基底公式。

**[Boost Your Human Image Generation Model via Direct Preference Optimization](boost_your_human_image_generation_model_via_direct_preference_optimization.md)**

:   提出 HG-DPO，以真实人像作为 DPO 的 winning image（而非生成图像对）+ 三阶段课程学习（Easy/Normal/Hard）渐进弥合生成-真实图像分布 gap + 统计匹配损失解决色偏，FID 从 37.34 降至 29.41（-21.4%），CI-Q 0.906→0.934，win-rate 超越 Diffusion-DPO 达 99.97%。

**[Continual SFT Matches Multimodal RLHF with Negative Supervision](continual_sft_matches_multimodal_rlhf_with_negative_supervision.md)**

:   通过梯度分析发现多模态 RLHF 相比持续 SFT 的核心优势在于 rejected response 中的负监督信号，据此提出 nSFT 方法，用 LLM 从拒绝回复中提取错误信息并构造纠正性对话数据，仅用 SFT loss 就能匹配甚至超越 DPO/PPO 等 RLHF 方法，且只需 1 个模型，显存效率大幅提升。

**[PhysMoDPO: Physically-Plausible Humanoid Motion with Preference Optimization](physmodpo_physically-plausible_humanoid_motion_with_preference_optimization.md)**

:   提出 PhysMoDPO，将 Direct Preference Optimization 应用于文本驱动的人体运动生成，通过将全身控制器（WBC）集成到训练 pipeline 中计算基于物理的奖励来构造偏好数据，使生成运动同时满足物理约束和文本指令，并在 Unitree G1 机器人上实现零样本部署。

**[Task Preference Optimization: Improving Multimodal Large Language Models with Vision Task Alignment](task_preference_optimization_improving_multimodal_large_language_models_with_vis.md)**

:   提出 Task Preference Optimization（TPO），通过可学习的任务 token 将视觉任务专用头（区域定位/时序定位/分割）接入 MLLM，利用视觉任务标注作为"任务偏好"反向优化 MLLM，在不损害对话能力的前提下大幅提升细粒度视觉理解，VideoChat 基线上平均提升 14.6%。
