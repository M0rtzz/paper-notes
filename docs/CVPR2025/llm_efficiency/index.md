---
title: >-
  CVPR2025 LLM效率方向 1篇论文解读
description: >-
  1篇CVPR2025 LLM效率方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM效率

**📷 CVPR2025** · 共 **1** 篇

**[Efficient Data Driven Mixture-Of-Expert Extraction From Trained Networks](efficient_data_driven_mixture-of-expert_extraction_from_trained_networks.md)**

:   提出一种从预训练 ViT 中自动提取 MoE（Mixture-of-Experts）变体的方法：先聚类 MLP 层的输出激活模式，再据此抽取对应的子网络作为专家，无需从头训练 MoE，在 ImageNet-1k 上仅需少量微调即可恢复 98% 原始性能，同时将 FLOPs 和模型大小分别减少 36% 和 32%。
