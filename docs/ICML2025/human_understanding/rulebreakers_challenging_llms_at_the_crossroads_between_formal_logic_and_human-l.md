---
title: >-
  [论文解读] RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning
description: >-
  [ICML 2025][人体理解] 本文构建了 RULEBREAKERS 数据集（25,600 个实例），专门用于评估 LLM 能否像人类一样在推理中利用常识和事实知识拒绝那些虽然在形式逻辑上有效、但在事实上与前提矛盾的结论，揭示了 LLM 在过度刚性应用逻辑规则方面的显著盲点。
tags:
  - ICML 2025
  - 人体理解
---

# RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning

**会议**: ICML 2025  
**arXiv**: [2410.16502](https://arxiv.org/abs/2410.16502)  
**领域**: 人体理解  

## 一句话总结

本文构建了 RULEBREAKERS 数据集（25,600 个实例），专门用于评估 LLM 能否像人类一样在推理中利用常识和事实知识拒绝那些虽然在形式逻辑上有效、但在事实上与前提矛盾的结论，揭示了 LLM 在过度刚性应用逻辑规则方面的显著盲点。

## 研究背景与动机

形式逻辑通过将自然语言转换为符号形式并应用规则来推导结论。然而，有一类重要的推理场景被忽视了——"规则破坏者"（rulebreaker）：

**经典例子**（改编自 Johnson-Laird, 1983）：
- 前提1："Anne 在斯德哥尔摩或瑞典的某个地方"（$A \vee B$）
- 前提2："Anne 不在瑞典"（$\neg B$）
- 应用析取三段论规则：得出"Anne 在斯德哥尔摩"（$A$）

但大多数知道斯德哥尔摩在瑞典的人**不会**得出这个结论，因为它与第二个前提事实矛盾。

认知科学研究已证实人类在面对此类情境时通常会拒绝形式逻辑得出的结论。然而，在 NLP 领域，rulebreaker 几乎未被系统研究过。更重要的是，越来越多的研究依赖形式逻辑来增强 LLM 的推理能力（如逻辑数据增强、逻辑约束推理等），但这可能**加剧** LLM 与人类推理之间的偏离。

## 方法详解

### 数据集构建

RULEBREAKERS 包含 12,800 个 rulebreaker 和 12,800 个对应的 non-rulebreaker，共 25,600 个实例。

**四种模板**（2 种逻辑规则 × 2 种实体类型）：

| | 地理实体（国家, 城市） | 类别实体（类型, 实例） |
|---|---|---|
| **否定后件（MT）** | If Anne in Sweden, then not Stockholm → Stockholm → Not Sweden | If plays brass, then not trumpet → trumpet → Not brass |
| **析取三段论（DS）** | Stockholm or Sweden → not Sweden → Stockholm | trumpet or brass → not brass → trumpet |

**实体对来源**：
- 地理对：WikiData 查询获取 183 个（国家, 首都）对
- 类别对：ConceptNet 提取 91 个（类型, 实例）对（鸟类、鱼类、乐器等）

**Non-rulebreaker 创建**：随机替换国家或类型名，使结论与前提不再矛盾。

### 评估指标

**配对准确率**：rulebreaker 和 non-rulebreaker 配对都回答正确的比例：

$$\tau = \frac{1}{|D^{paired}|}\sum_{(x^R, x^N) \in D^{paired}} [\![T(x^R) \wedge T(x^N)]\!]$$

随机猜测基线为 0.25。如果模型完全不区分两者（全部回答"是"），得分为 0。

**模型置信度**：比较模型在 non-rulebreaker（正确应回答"是"）和 rulebreaker（错误回答"是"）上的正答置信度差异。

### 实验设置

评估 7 个 LLM：Phi-3-mini/medium、LLaMA-3-8B/70B、Mistral-7B、Gemma-2-27b、GPT-4o。每个实例用 10 种表述变体（5 种措辞 × 2 种答案选项格式）进行测试。

## 实验

### 主实验 - 配对准确率

| 模型 | 总体 τ | rulebreaker 准确率 | non-rulebreaker 准确率 |
|---|---|---|---|
| LLaMA-3-8B-Instruct | ~0.609 | 中等 | 高 |
| LLaMA-3-70B-Instruct | ~0.497 | 中等 | 高 |
| Mistral-7B | ~0.476 | 中等 | 高 |
| Phi-3-medium | ~0.292 | 低 | 高 |
| Phi-3-mini | ~0.208 | 低 | 非常高 |
| Gemma-2-27b | ~0.071 | 非常低 | **完美** |
| GPT-4o | ~0.14 | 非常低 | **完美** |

**关键发现**：在 non-rulebreaker 上表现越好的模型（如 Gemma、GPT-4o），在 rulebreaker 上表现往往越差。这表明这些模型在**过度泛化**逻辑规则。

### 模型置信度分析

所有模型（排除 GPT-4o）在 non-rulebreaker 上的正答置信度 $\Pi_{D^N}^+$ 都显著高于在 rulebreaker 上的 $\Pi_{D^R}^+$（$p < 0.0001$），说明模型具有**潜在的区分能力**，即使最终输出未能体现。

### 失败原因分析

**假设1：与模型对实体的熟悉度相关**
- 大多数模型（LLaMA-3-8B 和 GPT-4o 除外）在正确配对组中的实体熟悉度高于错误配对组
- 但高熟悉度不保证高性能（如 Gemma-2-27b 最熟悉但准确率最低）

**假设2：与对第二前提的注意力分配相关**
- 使用 input × gradient 和注意力权重计算第二前提（事实性前提）的重要性比率
- LLaMA-3-8B 和 LLaMA-3-70B（准确率最高）也有最高的注意力比率
- 但 Gemma-2-27b 注意力比率第三高却准确率最低

## 亮点

- **首个大规模 rulebreaker 数据集**：25,600 个最小差异的 rulebreaker/non-rulebreaker 对，支持严格受控的评估
- **揭示 LLM 的深层盲点**：模型可能同时擅长事实检索和逻辑规则应用，却无法识别两者冲突的情况
- **对逻辑增强方法的重要警示**：提醒社区依赖形式逻辑改进 LLM 推理的潜在风险
- **潜在能力的发现**：置信度分析表明区分能力可能存在但未被利用
- **与认知科学的深度结合**：研究设计直接受心理模型理论启发

## 局限性

- 仅测试了两种逻辑规则（MT 和 DS），覆盖面有限
- 实体类型集合相对较小，可能不能充分代表真实世界知识
- 评估限于选择式回答，未充分测试开放式生成场景
- 训练数据中可能已包含类似推理模式，影响结果的可解释性
- 未提出改进 LLM 在 rulebreaker 上表现的具体方法

## 评分

⭐⭐⭐⭐ (4/5)

论文选题新颖，数据集构建严谨，实验分析深入。将认知科学与 NLP 研究结合的视角令人耳目一新。对当前依赖形式逻辑增强 LLM 推理的趋势提出了及时且重要的警示。
