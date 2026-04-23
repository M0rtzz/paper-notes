---
title: >-
  CVPR2025 LLM安全方向 1篇论文解读
description: >-
  1篇CVPR2025 LLM安全论文解读，主题涵盖：提出 GDDSG，用图着色理论将类按相似度分组——等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔒 LLM安全

**📷 CVPR2025** · **1** 篇论文解读

**[Order-Robust Class Incremental Learning: Graph-Driven Dynamic Similarity Grouping](order-robust_class_incremental_learning_graph-driven_dynamic_similarity_grouping.md)**

:   提出 GDDSG，用图着色理论将类按相似度分组——同组内类别尽量不相似（减少干扰），每组独立用 NCM 分类器+LoRA 适配器学习，在 CIFAR-100 10-step 上达到 94.00% 准确率和仅 0.78% 遗忘率（前 SOTA RanPAC 90.50%/3.49%）。
