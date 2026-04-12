---
title: >-
  ECCV2024 模型压缩方向 7篇论文解读
description: >-
  7篇ECCV2024 模型压缩方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🎞️ ECCV2024** · 共 **7** 篇

**[A Simple Lowbit Quantization Framework For Video Snapshot Co](a_simple_lowbit_quantization_framework_for_video_snapshot_co.md)**

:   首个面向视频快照压缩成像（Video SCI）重建任务的低比特量化框架Q-SCI，通过高质量特征提取模块、精确视频重建模块和Transformer分支的query/key分布偏移操作，在4-bit量化下实现7.8倍理论加速且性能仅下降2.3%。

**[Adaptive Compressed Sensing With Diffusionbased Posterior Sa](adaptive_compressed_sensing_with_diffusionbased_posterior_sa.md)**

:   提出AdaSense，利用预训练扩散模型的零样本后验采样来量化重建不确定性，从而自适应地选择最优测量矩阵，无需额外训练即可在人脸图像、MRI和CT等多领域实现优于非自适应方法的压缩感知重建。

**[Adaptive Selection Of Samplingreconstruction In Fourier Comp](adaptive_selection_of_samplingreconstruction_in_fourier_comp.md)**

:   提出ℋ1.5框架：为每个输入数据自适应选择最佳采样mask-重建网络对（J=3对），利用超分辨率空间生成模型量化高频贝叶斯不确定性来决定采样策略，理论证明优于联合优化ℋ1（非自适应）和自适应采样ℋ2（Pareto次优）。

**[Anytime Continual Learning For Open Vocabulary Classification](anytime_continual_learning_for_open_vocabulary_classification.md)**

:   提出 AnytimeCL 框架，通过部分微调 CLIP 最后一个 transformer block 并动态加权融合微调模型与原始模型的预测，实现任意时刻接收样本、任意标签集推理的开放词汇持续学习。

**[Bidirectional Stereo Image Compression With Cross-Dimensional Entropy Model](bidirectional_stereo_image_compression_with_cross-dimensional_entropy_model.md)**

:   提出双向对称的立体图像压缩框架 BiSIC，采用 3D 卷积联合编解码器和跨维度熵模型，在 PSNR 和 MS-SSIM 上均超越传统标准和已有学习方法，同时消除了单向方法中左右视图压缩质量不平衡的问题。

**[Category Adaptation Meets Projected Distillation In Generalized Continual Catego](category_adaptation_meets_projected_distillation_in_generalized_continual_catego.md)**

:   提出 CAMP 方法，通过可学习投影器蒸馏与类别中心适应网络的协同组合，在广义持续类别发现（GCCD）场景中显著提升了新类别学习与旧知识保持之间的平衡。

**[Freestyleret Retrieving Images From Style-Diversified Queries](freestyleret_retrieving_images_from_style-diversified_queries.md)**

:   提出首个风格多样化查询图像检索（Style-Diversified QBIR）任务及数据集DSR，设计了轻量即插即用的FreestyleRet框架，通过Gram矩阵提取查询的纹理/风格特征，构建风格空间并以此初始化prompt token，使冻结的视觉编码器能适配文本、草图、低分辨率、艺术画等多种查询风格的检索。
