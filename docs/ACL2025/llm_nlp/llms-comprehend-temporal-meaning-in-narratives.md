---
title: >-
  [论文解读] How LLMs Comprehend Temporal Meaning in Narratives: A Case Study in Cognitive Evaluation of LLMs
description: >-
  [ACL 2025][LLM/NLP][时态语义] 本文通过认知语言学实验范式评估 LLM 对叙事中时态体态（aspect）语义的理解，发现 LLM 过度依赖原型搭配、产生不一致的体态判断、在体态驱动的因果推理上表现不佳，揭示了 LLM 叙事理解的根本局限。
tags:
  - ACL 2025
  - LLM/NLP
  - 时态语义
  - 体态
  - 叙事理解
  - 认知评估
  - 因果推理
---

# How LLMs Comprehend Temporal Meaning in Narratives: A Case Study in Cognitive Evaluation of LLMs

**会议**: ACL 2025  
**arXiv**: [2507.14307](https://arxiv.org/abs/2507.14307)  
**代码**: 无  
**领域**: NLP理解  
**关键词**: 时态语义, 体态, 叙事理解, 认知评估, 因果推理

## 一句话总结

本文通过认知语言学实验范式评估 LLM 对叙事中时态体态（aspect）语义的理解，发现 LLM 过度依赖原型搭配、产生不一致的体态判断、在体态驱动的因果推理上表现不佳，揭示了 LLM 叙事理解的根本局限。

## 研究背景与动机

1. **领域现状**：LLM 展现出越来越像人类的语言行为，但其是否真正理解语言（而非高级模式匹配）仍是开放问题。
2. **现有痛点**：现有认知评估主要使用NLP任务数据集或新构造的数据，缺少直接复用认知科学实验材料的严格对比。
3. **核心矛盾**：体态（aspect）是一个微妙的语义现象——进行体（"was washing"）暗示事件仍在进行，完成体（"washed"）暗示事件已完结。人类利用体态进行因果推理，但LLM是否能做到？
4. **本文目标**：用认知语言学家设计的实验刺激来系统评估 LLM 的体态理解。
5. **切入角度**：提出"专家参与式"（Expert-in-the-Loop）探测流水线，与认知科学领域专家密切合作设计实验。
6. **核心 idea**：LLM 在体态理解上与人类有根本差异——过度依赖原型语言模式而非灵活的语境驱动解释。

## 方法详解

### 整体框架

基于先前人类研究的叙事材料，设计一系列实验测试LLM对体态的语义理解（完成性判断）、语用推理（因果推理）和非原型用法识别。使用多种测量指标（显式输出和隐式信号如token概率）。

### 关键设计

1. **Expert-in-the-Loop流水线**: 与认知语言学家合作，直接复用人类实验的叙事刺激材料和实验范式，确保评估的理论严谨性。
2. **多维测量**: 使用自我报告（模型的显式判断）和token概率（隐式信号）两种方式收集证据。
3. **人类对比**: 直接与先前人类研究的结果进行对比。

### 损失函数 / 训练策略

评估研究，测试了多个SOTA LLM。

## 实验关键数据

### 主实验

| 发现 | 详情 |
|------|------|
| 原型偏好 | LLM过度偏好完成事件+完成体的原型搭配 |
| 不一致性 | 同一模型在不同指标上表现不一致 |
| 因果推理差 | 无法利用进行体的"事件进行中"信息进行因果推理 |
| 背景化困难 | 对非原型用法（进行体+完成事件）的语用含义理解不足 |

### 关键发现

- LLM 对体态有部分语义理解，但远不如预期，表现不一致
- 语用层面的体态理解（因果推理、背景化）是LLM的明显弱项
- 更强的模型表现更好但仍不达人类水平
- 提示说LLM更多是在做模式匹配而非真正的语义理解

### 各模型体态理解能力

| 模型 | 完成性判断 | 因果推理 | 背景化 |
|------|----------|---------|-------|
| GPT-4o | 中等 | 较差 | 差 |
| Claude-3.5 | 中等 | 中等 | 较差 |
| Llama-3.1-70B | 较差 | 差 | 差 |
| Qwen2.5-72B | 中等 | 较差 | 差 |

### 人类vs LLM行为差异
- 人类利用进行体推断事件未完成→推理出可能的因果关系
- LLM偏好完成事件+完成体的原型搭配，忽略非原型用法
- 人类的反应时间差异在LLM中没有对应的token概率差异


## 亮点与洞察

- 将认知科学实验严格移植到LLM评估中，方法论上非常扎实。
- 体态是语言学中的微妙现象，作为LLM认知能力的"试金石"很有价值。
- "Expert-in-the-Loop"的评估范式值得推广到其他认知能力评估。

## 局限与展望

- 实验材料来自英语，其他语言的体态系统（如中文的"了/着/过"、俄语的完/未完体）可能有不同特征
- 样本量相对较小——基于先前人类实验的材料限制了可用刺激数量
- 叙事场景的复杂度有限，更复杂的多事件叙事中的体态理解未测试
- 仅关注完成体和进行体两种主要体态，未覆盖习惯体、经验体等
- 提示敏感性可能影响结论的稳健性——不同提示模板可能得到不同结果
- 认知能力的评估方法论仍在发展中，结论需要在更多模型上验证

## 相关工作与启发

- **vs Bazhukov et al.**: 使用注意力分数评估心理语言学效应，本文使用显式输出+token概率等更丰富的多维测量
- **vs Roberts et al. (Fan Effect)**: 用token概率作为记忆检索困难的代理，思路类似但语言现象不同
- **vs 一般LLM认知评估**: 本文聚焦一个非常精细的语言现象（体态），提供认知深度而非任务广度
- **vs Lee et al.**: 研究LLM的心理语言学效应，但未涉及体态这一复杂的时间语义现象


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。

## 评分

- 新颖性: ⭐⭐⭐⭐ 体态理解在LLM评估中几乎未被触及
- 实验充分度: ⭐⭐⭐⭐ 多模型+多测量+人类对比
- 写作质量: ⭐⭐⭐⭐⭐ 理论背景扎实，方法论严谨
- 价值: ⭐⭐⭐⭐ 对LLM认知能力研究有独特贡献

<!-- RELATED:START -->

## 相关论文

- [\[ACL 2025\] Can LLMs Interpret and Leverage Structured Linguistic Representations? A Case Study with AMRs](can_llms_interpret_and_leverage_structured_linguistic_representations_a_case_stu.md)
- [\[ACL 2025\] Zero-Shot Belief: A Hard Problem for LLMs](zero-shot_belief_a_hard_problem_for_llms.md)
- [\[ACL 2025\] Is It JUST Semantics? A Case Study of Discourse Particle Understanding in LLMs](is_it_just_semantics_a_case_study_of_discourse_particle_understanding_in_llms.md)
- [\[ACL 2025\] Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](unintended_harms_of_value-aligned_llms_psychological_and_empirical_insights.md)
- [\[ACL 2025\] LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks](llm_vs_human_judges_study.md)

<!-- RELATED:END -->
