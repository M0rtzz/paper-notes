---
title: >-
  CVPR2026 异常检测论文汇总 · 2篇论文解读
description: >-
  2篇CVPR2026的异常检测方向论文解读，涵盖布局/合成、异常检测、对齐/RLHF、推理等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2026"
  - "异常检测"
  - "论文解读"
  - "论文笔记"
  - "布局/合成"
  - "对齐/RLHF"
  - "推理"
item_list:
  - u: "anomaly_as_non-conformity_via_training-free_graph_laplacian_energy_minimization/"
    t: "Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization"
  - u: "layoutad_exploring_semantic-geometric_misalignment_reasoning_for_scene_layout_an/"
    t: "LayoutAD: Exploring Semantic-Geometric Misalignment Reasoning for Scene Layout Anomaly Detection"
item_total: 2
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔍 异常检测

**📷 CVPR2026** · **2** 篇论文解读

**[Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization](anomaly_as_non-conformity_via_training-free_graph_laplacian_energy_minimization.md)**

:   ANoCo 把异常检测从"这个 patch 像不像正常的"重新定义成"把这个 patch 拉回正常流形要花多大代价"，用一个锚定的二部图 Laplacian 能量最小化把每个查询 patch 往正常流形上拉，**拉动的位移幅度本身**就是异常分——无需训练、无消息传递、闭式解，在 MVTec-AD / VisA 的 1/2/4-shot 上全面刷新 SOTA。

**[LayoutAD: Exploring Semantic-Geometric Misalignment Reasoning for Scene Layout Anomaly Detection](layoutad_exploring_semantic-geometric_misalignment_reasoning_for_scene_layout_an.md)**

:   LayoutAD 提出"场景布局异常检测"这一新任务，用无监督方式给图像里每个物体打出对象级异常分——它把场景拆成语义图与几何图，通过跨图注意力推理两者之间的"错配"，从而发现诸如"五条腿的狗""停在湖面上的车"这类像素级检测器看不见的布局级幻觉。
