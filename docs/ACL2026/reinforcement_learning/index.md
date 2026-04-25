---
title: >-
  ACL2026 强化学习方向 4篇论文解读
description: >-
  4篇ACL2026 强化学习论文解读，主题涵盖：首篇系统综述数据稀缺条件下LLM强化学习的工作、提出 Adaptive Instruction、提出 AJ-Bench，首个系统评估等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**💬 ACL2026** · **4** 篇论文解读

**[A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions](a_survey_of_reinforcement_learning_for_large_language_models_under_data_scarcity.md)**

:   首篇系统综述数据稀缺条件下LLM强化学习的工作，提出数据中心、训练中心、框架中心三层分类体系，覆盖数据剪枝/合成/压缩、轨迹生成/奖励工程/策略优化、以及自演化/协同演化/多智能体演化等方向。

**[Adaptive Instruction Composition for Automated LLM Red-Teaming](adaptive_instruction_composition_for_automated_llm_red-teaming.md)**

:   提出 Adaptive Instruction Composition (AIC) 框架，利用 Neural Thompson Sampling 在众包有害查询和越狱策略的组合空间中自适应地选择攻击指令，同时优化攻击成功率和多样性，在 Harmbench 上大幅超越已有方法。

**[AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation](aj-bench_benchmarking_agent-as-a-judge_for_environment-aware_evaluation.md)**

:   提出 AJ-Bench，首个系统评估 Agent-as-a-Judge 能力的基准，覆盖搜索、数据系统和 GUI 三个领域共 155 个任务和 516 条标注轨迹，实验表明 Agent-as-a-Judge 比 LLM-as-a-Judge 平均 F1 提升约 13 个百分点。

**[Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study](scaling_behaviors_of_llm_reinforcement_learning_post-training_an_empirical_study.md)**

:   首次系统研究 LLM 强化学习后训练的缩放行为，在 Qwen2.5 系列(0.5B-72B)上发现性能与训练资源之间遵循幂律关系，且学习效率随模型规模增大呈饱和趋势。
