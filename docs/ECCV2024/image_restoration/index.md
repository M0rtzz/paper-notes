---
title: >-
  ECCV2024 图像恢复方向 3篇论文解读
description: >-
  3篇ECCV2024 图像恢复方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**🎞️ ECCV2024** · 共 **3** 篇

**[Accelerating Image Super-Resolution Networks With Pixel-Level Classification](accelerating_image_super-resolution_networks_with_pixel-level_classification.md)**

:   提出PCSR——首个像素级计算资源分配的超分方法，用轻量MLP分类器逐像素判断恢复难度并分配到不同容量的上采样器，在PSNR几乎不掉的情况下将FLOPs压低至原始模型的18%~57%，大幅优于现有patch级方法ClassSR和ARM。

**[Asymmetric Mask Scheme For Self-Supervised Real Image Denoising](asymmetric_mask_scheme_for_self-supervised_real_image_denoising.md)**

:   提出非对称掩码方案 AMSNet，训练时用单掩码、推理时用多掩码互补，突破了 blind spot network 对网络感受野的结构限制，在真实图像自监督去噪任务上取得 SOTA。

**[Bamm Bidirectional Autoregressive Motion Model](bamm_bidirectional_autoregressive_motion_model.md)**

:   提出 BAMM（双向自回归运动模型），通过统一生成掩码建模和自回归建模的混合注意力掩码策略，在一个框架中同时实现高质量运动生成、自适应长度预测和零样本运动编辑，在 HumanML3D 和 KIT-ML 上全面超越 SOTA。
