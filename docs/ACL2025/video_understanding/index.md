---
title: >-
  ACL2025 视频理解方向 7篇论文解读
description: >-
  7篇ACL2025 视频理解方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📹 视频理解

**💬 ACL2025** · **7** 篇论文解读

**[Addressing Blind Guessing Calibration Of Selection Bias In Multiple-Choice Quest](addressing_blind_guessing_calibration_of_selection_bias_in_multiple-choice_quest.md)**

:   首次系统性研究视频语言模型（VLM）在多选题回答中的选项选择偏差问题，通过任务分解分析偏差来源，提出BOLD后处理校准技术，在减少偏差的同时提升模型性能。

**[From Teacher To Student Tracking Memorization Through Model Distillation](from_teacher_to_student_tracking_memorization_through_model_distillation.md)**

:   系统研究了知识蒸馏（KD）对大语言模型记忆化行为的影响，发现蒸馏不仅能压缩模型，还能显著降低对训练数据的逐字记忆风险——其中反向 KL 蒸馏（RKLD/MiniLLM）将记忆化比例从 SFT 的 65.4% 降至最低 6.0%。

**[Generative Frame Sampler For Long Video Understanding](generative_frame_sampler_for_long_video_understanding.md)**

:   提出 GenS，一个基于 VideoLLM 的生成式帧采样模块，用自然语言输出question-aware的相关帧时间段和置信度分数，作为即插即用模块在 LongVideoBench/MLVU/HourVideo 上为多种 VideoLLM 带来 2-4 个点的一致提升。

**[Icr Probe Tracking Hidden State Dynamics For Reliable Hallucination Detection In](icr_probe_tracking_hidden_state_dynamics_for_reliable_hallucination_detection_in.md)**

:   提出 ICR Score（Information Contribution to Residual Stream），通过测量 MHSA 和 FFN 模块对隐状态更新的贡献一致性来量化残差流动态，构建仅 16K 参数的 ICR Probe，在 4 个数据集 × 3 个 LLM 上幻觉检测 AUROC 全面超越基线。

**[Improving Dialogue State Tracking Through Combinatorial Search For In-Context Ex](improving_dialogue_state_tracking_through_combinatorial_search_for_in-context_ex.md)**

:   提出 CombiSearch 方法，通过组合式评分为对话状态追踪（DST）选择最优 in-context 示例组合，在仅用 5% 训练数据的情况下超越所有使用 100% 数据的 baseline，理想设置下 JGA 上界比传统方法高 12%。

**[Raven Robust Advertisement Video Violation Temporal Grounding Via Reinforcement ](raven_robust_advertisement_video_violation_temporal_grounding_via_reinforcement_.md)**

:   本文提出RAVEN框架，将课程强化学习与多模态LLM结合，通过分层奖励机制和渐进式训练策略，实现广告视频违规内容的精确时序定位和类别预测，无需显式推理标注数据即可激发涌现推理能力。

**[Sparse-To-Dense A Free Lunch For Lossless Acceleration Of Video Understanding In](sparse-to-dense_a_free_lunch_for_lossless_acceleration_of_video_understanding_in.md)**

:   基于Video-LLM中注意力分数的稀疏性观察，提出Sparse-to-Dense (StD)解码策略，用top-K稀疏注意力模型作为draft model快速生成候选token，再用全注意力模型并行验证，实现最高1.94倍的无损加速，且无需额外训练或架构修改。
