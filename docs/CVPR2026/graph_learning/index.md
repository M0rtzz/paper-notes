---
title: >-
  CVPR2026 图学习方向 3篇论文解读
description: >-
  3篇CVPR2026 图学习方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**📷 CVPR2026** · 共 **3** 篇

**[Hyperbolic Busemann Neural Networks](hyperbolic_busemann_neural_networks.md)**

:   利用 Busemann 函数将多类逻辑回归（MLR）和全连接层（FC）内蕴地提升到双曲空间，提出 BMLR 和 BFC 两个统一组件，在 Poincaré 球和 Lorentz 模型上同时适用，且在图像分类、基因组序列、节点分类、链接预测四类任务上均优于已有双曲层。

**[Mario Multimodal Graph Reasoning With Large Language Models](mario_multimodal_graph_reasoning_with_large_language_models.md)**

:   提出 Mario，针对多模态图（MMG）上的 LLM 推理，通过图条件视觉语言模型（GVLM）实现拓扑感知的跨模态对齐，再用模态自适应提示路由器（MAPR）为每个节点选择最优模态配置，在节点分类和链接预测上达到 SOTA。

**[ViterbiPlanNet: Injecting Procedural Knowledge via Differentiable Viterbi for Planning in Instructional Videos](viterbiplannet_injecting_procedural_knowledge_via_differentiable_viterbi_for_pla.md)**

:   通过可微 Viterbi 层将过程知识图端到端集成到视频过程规划中，神经网络只学发射概率，参数量比扩散/LLM规划器少一个数量级
