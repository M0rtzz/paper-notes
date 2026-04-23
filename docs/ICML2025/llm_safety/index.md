---
title: >-
  ICML2025 LLM安全方向 6篇论文解读
description: >-
  6篇ICML2025 LLM安全论文解读，主题涵盖：提出 BECAME——基于贝叶斯持续学习原则重新建、提出 CUTER（CUT-out-and-Expe、本文首次探索了早退出网络（early-exit等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔒 LLM安全

**🧪 ICML2025** · **6** 篇论文解读

**[BECAME: BayEsian Continual Learning with Adaptive Model MErging](became_bayesian_continual_learning_with_adaptive_model_merging.md)**

:   提出 BECAME——基于贝叶斯持续学习原则重新建模模型融合机制，利用 Laplace 近似推导出最优融合系数的闭式解，结合梯度投影（稳定性）和无约束训练（可塑性）的两阶段框架，在多个持续学习基准上显著超越 SOTA。

**[Cut out and Replay: A Simple yet Versatile Strategy for Multi-Label Online Continual Learning](cut_out_and_replay_a_simple_yet_versatile_strategy_for_multi-label_online_contin.md)**

:   提出 CUTER（CUT-out-and-Experience-Replay），通过裁剪图像中标签特定区域并存入记忆缓冲区进行回放，将多标签在线持续学习转化为多个单标签子图像分类任务，同时解决灾难性遗忘、缺失标签和类别不平衡三大挑战。

**[Improving Continual Learning Performance and Efficiency with Auxiliary Classifiers](improving_continual_learning_performance_and_efficiency_with_auxiliary_classifie.md)**

:   本文首次探索了早退出网络（early-exit networks）在持续学习中的应用，发现早期分类器天然遭受更少的灾难性遗忘，并提出 Task-wise Logits Correction (TLC) 方法来均衡任务偏差，在阶段增量学习中以不到 70% 的计算量匹配标准方法的准确率。

**[NegMerge: Sign-Consensual Weight Merging for Machine Unlearning](negmerge_sign-consensual_weight_merging_for_machine_unlearning.md)**

:   提出 NegMerge，通过合并多个不同超参数微调模型的任务向量、仅保留符号一致的权重元素来构造更有效的遗忘向量，在零样本与标准分类场景中均取得 SOTA 遗忘效果。

**[System-Aware Unlearning Algorithms: Use Lesser, Forget Faster](system-aware_unlearning_algorithms_use_lesser_forget_faster.md)**

:   提出系统感知遗忘 (system-aware unlearning) 新定义，将攻击者的能力限制为只能访问系统实际存储的内容而非全部剩余数据，并基于核心集 (core set) + 选择采样 (selective sampling) 设计了线性分类的精确遗忘算法，实现亚线性内存和极低删除时间。

**[Unlocking the Power of Rehearsal in Continual Learning: A Theoretical Perspective](unlocking_the_power_of_rehearsal_in_continual_learning_a_theoretical_perspective.md)**

:   从理论角度严格证明持续学习中排练策略的有效性机制——排练通过控制梯度方向偏差将多任务顺序学习近似为联合训练，遗忘界随缓冲区大小 $m$ 呈 $O(\sqrt{T/m})$ 次线性增长，为实际系统的缓冲区配置提供了 $O(d/\epsilon^2)$ 的精确指导。
