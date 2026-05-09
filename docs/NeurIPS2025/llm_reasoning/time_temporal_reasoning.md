---
title: >-
  [论文解读] TimE: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios
description: >-
  [NeurIPS 2025][LLM推理][时间推理] 本文提出 TimE，一个包含 38,522 个 QA 对的多层级时间推理基准，覆盖知识密集（Wiki）、动态事件（News）和多轮对话（Dial）三类真实场景，设计 11 个细粒度子任务系统评估 LLM 的时间推理能力，并发布人工标注子集 TimE-Lite。
tags:
  - NeurIPS 2025
  - LLM推理
  - 时间推理
  - 基准评估
  - 大语言模型
  - 多层级任务
  - 真实世界场景
---

# TimE: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios

**会议**: NeurIPS 2025  
**arXiv**: [2505.12891](https://arxiv.org/abs/2505.12891)  
**代码**: [GitHub](https://github.com/ShaohangWei/TimE)  
**领域**: LLM推理  
**关键词**: 时间推理, 基准评估, 大语言模型, 多层级任务, 真实世界场景

## 一句话总结
本文提出 TimE，一个包含 38,522 个 QA 对的多层级时间推理基准，覆盖知识密集（Wiki）、动态事件（News）和多轮对话（Dial）三类真实场景，设计 11 个细粒度子任务系统评估 LLM 的时间推理能力，并发布人工标注子集 TimE-Lite。

## 研究背景与动机

1. **领域现状**: LLM 在数学和代码推理上取得显著进展，但时间推理能力仍面临挑战。

2. **现有痛点**: 现有时间推理基准（TimeBench、TRAM）主要关注简化场景，忽视真实世界的三大挑战：密集时间信息、快速变化的事件动态、社交交互中的复杂时间依赖。

3. **核心矛盾**: 时间推理本质上是层级化的（基础理解→表达推理→复杂关系推理），但现有基准缺乏这种分层评估。

4. **本文目标**: 构建覆盖多种真实场景、多层级任务的综合时间推理基准。

5. **切入角度**: 从三种数据源（Wikidata、新闻、超长对话）构建，模拟人类利用时间概念理解世界的过程。

6. **核心 idea**: 三级递进框架——Level 1 基础时间理解与检索、Level 2 时间表达推理、Level 3 复杂时间关系推理。

## 方法详解

### 整体框架
三个子数据集对应三种真实挑战：TimE-Wiki（知识密集，13,848 QA）、TimE-News（动态事件，19,958 QA）、TimE-Dial（多轮对话，4,716 QA）。数据构建使用规则模板 + DeepSeek-V3/R1 合成 QA 对，STARC 框架生成干扰选项。TimE-News 使用 BM25/Vector/Hybrid 三种 RAG 检索器处理超长新闻文档。

### 关键设计

1. **三级任务体系**:
    - Level 1: Extract、Localization、Computation、DurationCompare、OrderCompare（5 个子任务）
    - Level 2: Explicit Reasoning、Order Reasoning、Relative Reasoning（3 个子任务）
    - Level 3: Co-temporality、Timeline、Counterfactual Reasoning（3 个子任务）
    - 设计动机: 模拟人类从捕获时间概念→推理隐式表达→理解复杂关系的认知过程

2. **数据构建流程**:
    - 功能: 确保数据质量和多样性
    - 核心思路: 收集时间事实→构建时间线→合成 QA 对。使用规则模板 + DeepSeek-V3/R1 合成，STARC 框架生成干扰选项
    - 设计动机: 不同数据源需要不同构建策略，News 使用 RAG 处理超长文档

3. **TimE-Lite**:
    - 功能: 提供高质量人工验证子集
    - 核心思路: 从 TimE 中系统采样 1,071 对，3 名专家标注，一致率 89.13%
    - 设计动机: 保证评估可靠性，便于高效评测

### 损失函数 / 训练策略
- 评估指标: 自由问答用 F1/EM，选择题用 Macro F1
- 解码策略: 贪心搜索
- 评估模型: 24 个模型，包括推理模型和非推理模型

## 实验关键数据

### 主实验

| 模型 | TimE-Wiki Level3 | TimE-News Timeline | TimE-Dial Extract |
|------|-----------------|-------------------|------------------|
| o3-mini | ~52% Avg | <30% | ~40% |
| Qwen2.5-72B | ~50% Avg | ~27% | ~40% |
| DeepSeek-R1 | ~55% Avg | 33% | - |

### 关键发现
- 知识密集场景：模型在隐式时间表达和跨事件关系上表现差（o3-mini 仅 52% Order Reasoning）
- 动态事件：Timeline 任务（排序 3 个事件）所有模型不超过 30%
- 多轮对话：时间检索和定位准确率仅约 40%，远低于其他数据集
- 推理模型在计算类任务优势明显，但在时间关系理解上提升有限
- 测试时扩展（TTS）对时间推理帮助不大
- TTS 影响不一致：R1-Distill-Qwen-14B 在 TimE-Dial 的 OrderCompare/DurationCompare/Counterfactual 上分别提升 24.44%/11.33%/12.0%，但在 TimE-Wiki 的 Extract/Localization 上反而下降 3.36%/8.16%——系统化上下文遍历策略可能导致过度思考循环
- 检索器选择显著影响时间推理：GPT-4o 使用 Hybrid 检索器在 Timeline 任务上比 BM25/Vector 低 10%以上，说明准确的时间事实检索直接影响复杂事件推理效果
- 基础时间检索能力（Extract/Localization）与几乎所有高级时间推理任务的相关系数超过 0.5，聚类分析证实检索是推理的基础

## 亮点与洞察
- 首个系统覆盖三种真实世界时间推理挑战的基准
- 揭示了即使最强推理模型在时间推理上仍有显著不足
- 对话中的记忆式时间表达（如"上周六"）对模型构成独特挑战
- 支持 leaderboard，便于社区持续评测
- TimE-Lite 提供 1,071 个人工验证 QA 对（3名专家标注，一致率 89.13%），确保评估可靠性
- 24 个模型的广泛评估覆盖推理模型（o3-mini、DeepSeek-R1）和非推理模型，使用贪心搜索解码

## 局限与展望
- QA 合成依赖 LLM，可能存在质量偏差
- News 数据依赖 RAG，检索质量影响评估
- 未覆盖多模态时间推理场景
- 部分任务的难度设计可能需要根据模型能力动态调整
- TimE-Dial 中小规模模型（8B）在 Extract 和 Localization 任务上仅约 30-40%，远低于 TimE-Wiki 的 60-70%，说明多轮对话中的记忆式时间表达（如"上次我们聊天时"、"两天后"）是独特挑战
- 聚类分析将 11 个子任务自然分为三组：基础检索（Extract/Localization）、推理（Reasoning/Compare）和复杂关系（Timeline/Counterfactual），各组难度递进

## 相关工作与启发
- **vs TimeBench**: TimeBench 聚合 10 个已有数据集，任务较简单；TimE 统一构建，挑战性更高
- **vs TRAM**: TRAM 仅评估事件序列理解，TimE 覆盖 11 个子任务更全面
- **vs TCELongBench**: 仅关注新闻场景的部分时间方面，TimE 覆盖三种场景
- **vs TReMu**: TReMu 仅做对话中的时间定位，TimE-Dial 覆盖更多任务类型
- **vs RealTimeQA/FreshLLM**: 关注知识更新而非时间推理本身，TimE 专注推理能力评估
- **数据规模**：总计 38,522 个 QA 对，是目前规模最大的时间推理专用基准。Wikidata 覆盖密集时间事实，新闻覆盖动态事件流，超长对话覆盖社交交互中的时间依赖

## 评分

### 实现细节
38,522个QA对，覆盖3种场景（Wiki/News/Dial）×3级任务×11子任务。
TimE-Lite含1,071个人工验证QA对，3名专家标注一致率89.13%。
评估24个模型，使用贪心搜索解码，F1/EM（自由问答）和Macro F1（选择题）。
- 新颖性: ⭐⭐⭐⭐ 多层级多场景的时间推理基准设计新颖
- 实验充分度: ⭐⭐⭐⭐⭐ 24 个模型的广泛评估
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图表丰富
- 价值: ⭐⭐⭐⭐⭐ 填补了时间推理评估的重要空白

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[NeurIPS 2025\] RealMath: A Continuous Benchmark for Evaluating Language Models on Research-Level Mathematics](realmath_a_continuous_benchmark_for_evaluating_language_models_on_research-level.md)
- [\[NeurIPS 2025\] 笔记6：Self-Evaluating LLMs - 多步任务的步级置信度估计](value-guided_search_for_efficient_chain-of-thought_reasoning.md)
- [\[NeurIPS 2025\] Segment Policy Optimization: Effective Segment-Level Credit Assignment in RL for Large Language Models](segment_policy_optimization_effective_segment-level_credit_assignment_in_rl_for_.md)
- [\[NeurIPS 2025\] ReasonFlux-PRM: Trajectory-Aware PRMs for Long Chain-of-Thought Reasoning in LLMs](reasonfluxprm_trajectoryaware_prms_for_long_chainofthought_r.md)
- [\[NeurIPS 2025\] SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction](sql-of-thought_multi-agentic_text-to-sql_with_guided_error_correction.md)

</div>

<!-- RELATED:END -->
