---
title: >-
  CVPR2025 AIGC检测方向 2篇论文解读
description: >-
  2篇CVPR2025 AIGC检测论文解读，主题涵盖：提出 BiMC（Bi-level、提出 ProAPO，一种基于进化算法的渐进式自动提等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔎 AIGC检测

**📷 CVPR2025** · **2** 篇论文解读

**[Enhancing Few-Shot Class-Incremental Learning via Training-Free Bi-Level Modality Calibration](enhancing_few-shot_class-incremental_learning_via_training-free_bi-level_modalit.md)**

:   提出 BiMC（Bi-level Modality Calibration）框架，基于冻结 CLIP 模型，通过模态内校准（结合 LLM 生成的细粒度类别描述与视觉原型）和模态间校准（融合预训练语言知识与任务特定视觉先验），在无需任何参数训练的情况下实现 FSCIL SOTA，在 CIFAR-100 上超越最优对比方法 4.25%。

**[ProAPO: Progressively Automatic Prompt Optimization for Visual Classification](proapo_progressively_automatic_prompt_optimization_for_visual_classification.md)**

:   提出 ProAPO，一种基于进化算法的渐进式自动提示优化方法，在仅需 one-shot 监督且无需人工参与的条件下，从任务级模板逐步优化到类别级描述，解决 LLM 生成描述中的幻觉和缺乏区分度问题，在 13 个数据集上超越现有文本提示方法。
