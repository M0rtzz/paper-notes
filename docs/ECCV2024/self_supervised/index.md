---
title: >-
  ECCV2024 自监督/表示学习方向 4篇论文解读
description: >-
  4篇ECCV2024 自监督/表示学习方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**🎞️ ECCV2024** · 共 **4** 篇

**[Adaptive Multihead Contrastive Learning](adaptive_multihead_contrastive_learning.md)**

:   AMCL提出使用多个投影头（各自产生不同特征）+ 对每个样本对和每个头自适应学习温度参数，从最大似然估计推导出损失函数，作为通用插件在SimCLR/MoCo/Barlow Twins/CAN/LGP上一致提升1-5%性能。

**[Coho Context-Sensitive City-Scale Hierarchical Urban Layout Generation](coho_context-sensitive_city-scale_hierarchical_urban_layout_generation.md)**

:   提出基于图掩码自编码器 (GMAE) 的城市级 2.5D 布局生成方法，通过规范图表示捕获建筑-街区-社区的多层语义上下文，结合优先级调度的迭代采样，在 330 个美国城市上实现了兼具真实感、语义一致性和正确性的大规模城市布局生成。

**[Efficient Image Pre-Training With Siamese Cropped Masked Autoencoders](efficient_image_pre-training_with_siamese_cropped_masked_autoencoders.md)**

:   提出CropMAE——用同一图像的两个随机裁剪视图替代视频帧对来训练孪生掩码自编码器，在98.5%的极高掩码率下仅用2个可见patch即可学习物体边界感知表征，训练速度比SiamMAE提升最高23.8倍，同时在视频传播任务上达到竞争性能。

**[Flowcon Out-Of-Distribution Detection Using Flow-Based Contrastive Learning](flowcon_out-of-distribution_detection_using_flow-based_contrastive_learning.md)**

:   提出FlowCon，一种基于密度估计的OOD检测方法，创新性地将正规化流（normalizing flow）与监督对比学习结合——在流模型的潜在空间中使用基于Bhattacharyya系数的对比损失学习类别条件高斯分布，无需外部OOD数据或重训分类器即可实现高效的OOD检测。
