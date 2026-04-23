---
title: >-
  NeurIPS2025 NLP理解方向 2篇论文解读
description: >-
  2篇NeurIPS2025 NLP理解论文解读，主题涵盖：提出PNLC方法，通过训练轻量级目标条件价值函数作、本文发现朴素的弱到强泛化在分布偏移下会失败（强模型等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📖 NLP理解

**🧠 NeurIPS2025** · **2** 篇论文解读

**[Planning without Search: Refining Frontier LLMs with Offline Goal-Conditioned RL](planning_without_search_refining_frontier_llms_with_offline_goal-conditioned_rl.md)**

:   提出PNLC方法，通过训练轻量级目标条件价值函数作为"自然语言评论家"，在推理步骤层面引导LLM智能体进行多轮规划和自我精化，无需直接微调或推理时搜索，在Web导航、社交推理、劝服等复杂交互任务上显著超越现有方法且推理速度快8-10倍。

**[Weak-to-Strong Generalization under Distribution Shifts](weak-to-strong_generalization_under_distribution_shifts.md)**

:   本文发现朴素的弱到强泛化在分布偏移下会失败（强模型甚至不如弱监督者），并提出 RAVEN 框架，通过动态学习多个弱模型的最优组合权重来实现鲁棒的弱到强泛化，在 OOD 任务上超越 baseline 超过 30%。
