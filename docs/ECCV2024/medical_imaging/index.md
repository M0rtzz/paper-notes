---
title: >-
  ECCV2024 医学图像方向 8篇论文解读
description: >-
  8篇ECCV2024 医学图像方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🎞️ ECCV2024** · 共 **8** 篇

**[Adaptive Correspondence Scoring For Unsupervised Medical Ima](adaptive_correspondence_scoring_for_unsupervised_medical_ima.md)**

:   针对医学图像无监督配准中噪声、遮挡等干扰因素导致的虚假重建误差问题，提出了一个自适应对应关系评分框架（AdaCS），通过学习像素级的对应置信度图来重新加权误差残差，以即插即用方式一致提升三种主流配准架构在三个数据集上的性能。

**[Alternate Diverse Teaching For Semi-Supervised Medical Image Segmentation](alternate_diverse_teaching_for_semi-supervised_medical_image_segmentation.md)**

:   提出 AD-MT（Alternate Diverse Mean Teacher），通过随机周期性交替更新两个教师模型 + 基于熵的冲突调和策略，在半监督医学分割中解决 confirmation bias 问题，在 ACDC/LA/Pancreas 上全面超越 SOTA。

**[Architecture-Agnostic Untrained Network Priors For Image Reconstruction With Fre](architecture-agnostic_untrained_network_priors_for_image_reconstruction_with_fre.md)**

:   提出三种与架构无关的频率正则化技术（带宽受限输入、带宽可控上采样、Lipschitz 正则化卷积层），统一解决 untrained network prior 的架构敏感性、过拟合和运行效率问题，在 MRI 重建任务中显著缩小不同架构间的性能差距。

**[Cardiacnet Learning To Reconstruct Abnormalities For Cardiac Disease Assessment ](cardiacnet_learning_to_reconstruct_abnormalities_for_cardiac_disease_assessment_.md)**

:   提出基于重建的心脏疾病评估框架 CardiacNet，通过 Consistency Deformation Codebook (CDC) 和 Consistency Deformation Discriminator (CDD) 学习正常与异常心脏超声视频之间的结构和运动差异，在射血分数预测、肺动脉高压和房间隔缺损分类三个任务上达到 SOTA。

**[Chameleon A Data-Efficient Generalist For Dense Visual Prediction In The Wild](chameleon_a_data-efficient_generalist_for_dense_visual_prediction_in_the_wild.md)**

:   提出 Chameleon，一个基于 meta-learning 和 token matching 的数据高效视觉通才模型，仅需几十张标注图像即可适应全新的密集预测任务（包括医学图像、视频、3D 等），在六个下游基准上显著超越现有通才方法。

**[Chex Interactive Localization And Region Description In Chest X-Rays](chex_interactive_localization_and_region_description_in_chest_x-rays.md)**

:   提出ChEX——一个同时支持文本提示和边界框查询的交互式胸部X光解释模型，通过DETR风格的prompt检测器和多任务联合训练，在9个胸部X光任务上与SOTA竞争，同时提供独特的定位可解释性和用户交互能力。

**[Co-Synthesis Of Histopathology Nuclei Image-Label Pairs Using A Context-Conditio](co-synthesis_of_histopathology_nuclei_image-label_pairs_using_a_context-conditio.md)**

:   提出一种上下文条件化的联合扩散模型，能够同时合成组织病理学细胞核图像、语义标签和距离图，通过点图（centroid layout）和文本提示两种条件实现对合成过程的精确控制，并生成高质量的实例级标签用于下游核分割和分类任务。

**[Textttnephi Neural Deformation Fields For Approximately Diff](textttnephi_neural_deformation_fields_for_approximately_diff.md)**

:   NePhi用隐式神经网络（SIREN）替代传统的体素化形变场来表示配准变换，通过编码器预测latent code + 可选的测试时优化实现快速且近似微分同胚的医学图像配准，在多分辨率设置下与SOTA精度相当但内存降低5倍。
