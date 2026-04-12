---
title: >-
  ICML2025 对话系统方向 3篇论文解读
description: >-
  3篇ICML2025 对话系统方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🗣️ 对话系统

**🧪 ICML2025** · 共 **3** 篇

**[Agent Warpp Workflow Adherence Via Runtime Parallel Personalization](agent_warpp_workflow_adherence_via_runtime_parallel_personalization.md)**

:   提出 WARPP，一个无需训练的多智能体框架，在运行时根据用户属性动态剪枝条件分支工作流，并通过并行化的 Personalizer 智能体与模块化域特定智能体协同执行，在提升工具调用精度和参数保真度的同时减少 token 消耗。

**[Investigating Non-Transitivity In Llm-As-A-Judge](investigating_non-transitivity_in_llm-as-a-judge.md)**

:   揭示了 LLM-as-a-Judge 框架中评判偏好的**非传递性**问题（A>B, B>C 不能推出 A>C），证明固定基线模型的排名方式不可靠，提出基于循环赛 + Bradley-Terry 模型的排名方法及高效的 Swim 锦标赛策略。

**[Position Uncertainty Quantification Needs Reassessment For Large-Language Model ](position_uncertainty_quantification_needs_reassessment_for_large-language_model_.md)**

:   这篇 position paper 挑战了传统"偶然 vs 认知"不确定性二分法在 LLM Agent 场景中的适用性，指出两类不确定性的定义本身相互矛盾，并提出三个面向 Agent 交互的新研究方向：欠规范不确定性、交互式学习、以及丰富的输出不确定性表达。
