---
title: >-
  ICML2025 图像恢复方向 6篇论文解读
description: >-
  6篇ICML2025 图像恢复方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**🧪 ICML2025** · 共 **6** 篇

**[Adaptive Estimation And Learning Under Temporal Distribution Shift](adaptive_estimation_and_learning_under_temporal_distribution_shift.md)**

:   提出基于小波软阈值的估计算法，在无需先验知识的情况下实现时间分布偏移下的最优逐点估计误差界，将序列非平稳性与小波域稀疏性建立联系，并应用于分布偏移下的二分类和全变分去噪问题。

**[Asymrnr Video Diffusion Transformers Acceleration With Asymmetric Reduction And ](asymrnr_video_diffusion_transformers_acceleration_with_asymmetric_reduction_and_.md)**

:   提出 AsymRnR——一种免训练的视频 DiT 加速方法，基于注意力中不同组件（Q/K/V）、不同层、不同去噪步骤的冗余程度不同的观察，非对称地削减 token 以实现无损加速。

**[Epsilon-Vae Denoising As Visual Decoding](epsilon-vae_denoising_as_visual_decoding.md)**

:   提出 ε-VAE，将传统自编码器中的单步确定性解码器替换为扩散/去噪过程，实现"去噪即解码"（Denoising as Decoding），在相同压缩率下重建质量提升 40%、下游生成质量提升 22%，或在保持生成质量的同时通过提高压缩率实现 2.3 倍推理加速。

**[Evaluating Deepfake Detectors In The Wild](evaluating_deepfake_detectors_in_the_wild.md)**

:   用SOTA生成方法创建50万+高质量深伪图像，在模拟真实场景的测试流程下评估现有深伪检测器，发现不到一半的检测器AUC超过60%（最低50%=随机），且基本图像操作（JPEG压缩/增强）即可显著降低检测性能。

**[Harmonica Harmonizing Training And Inference For Better Feature Caching In Diffu](harmonica_harmonizing_training_and_inference_for_better_feature_caching_in_diffu.md)**

:   提出 HarmoniCa 框架，通过 Step-Wise Denoising Training (SDT) 和 Image Error Proxy-Guided Objective (IEPO) 两大设计解决现有学习型特征缓存方法中训练与推理不对齐的问题，在 PixArt-α 等 8 种模型上实现超 40% 延迟降低（2.07× 理论加速）且不损失生成质量。

**[Timedart A Diffusion Autoregressive Transformer For Self-Supervised Time Series ](timedart_a_diffusion_autoregressive_transformer_for_self-supervised_time_series_.md)**

:   提出 TimeDART，将自回归建模与去噪扩散过程统一在一个自监督预训练框架中，通过因果 Transformer 编码器捕获长期动态演化、patch 级扩散去噪捕获细粒度局部模式，在预测和分类任务上均超越现有方法。
