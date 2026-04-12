---
title: >-
  CVPR2026 社会计算方向 3篇论文解读
description: >-
  3篇CVPR2026 社会计算方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 👥 社会计算

**📷 CVPR2026** · 共 **3** 篇

**[As Language Models Scale Low-Order Linear Depth Dynamics Emerge](as_language_models_scale_low-order_linear_depth_dynamics_emerge.md)**

:   这篇论文把 Transformer 的层深看成离散时间系统，证明在给定上下文附近可以用一个 32 维的低阶线性状态空间代理去近似 GPT-2 的层间传播与干预响应，而且模型越大，这个低阶代理越准确，还能据此算出比启发式注入更省能量的多层干预策略。

**[As Language Models Scale Loworder Linear Depth Dyn](as_language_models_scale_loworder_linear_depth_dyn.md)**

:   将 Transformer 的逐层前向传播视为离散时间动力系统，发现 32 维低阶线性代理（LLV）可精确复现完整模型的层级灵敏度曲线，且该线性可辨识性随模型规模单调增强。

**[Revisiting Unknowns Towards Effective And Efficient Open-Set Active Learning](revisiting_unknowns_towards_effective_and_efficient_open-set_active_learning.md)**

:   提出 E2OAL，一个无需额外检测器的开放集主动学习框架，通过标签引导聚类发现未知类潜在结构、Dirichlet 校准辅助头联合建模已知/未知类别，并设计两阶段自适应查询策略，在多个基准上同时实现高准确率、高查询纯度和高训练效率。
