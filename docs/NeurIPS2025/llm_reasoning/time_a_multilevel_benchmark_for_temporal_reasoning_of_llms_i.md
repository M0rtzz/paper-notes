---
title: >-
  [论文解读] TimE: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios
description: >-
  [NeurIPS 2025][LLM推理][时间推理] 提出TimE多层级时间推理Benchmark（38,522 QA + 943人工标注TimE-Lite），覆盖知识密集（Wiki）、快速演变（News）和长对话（Dialogue）三种真实场景，设计三级渐进11子任务体系评估24个LLM，揭示即使最强推理模型在复杂时间关系推理上仍有显著短板。
tags:
  - NeurIPS 2025
  - LLM推理
  - 时间推理
  - benchmark
  - 多层级评测
  - LLM
  - 真实场景
---

# TimE: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios

**会议**: NeurIPS 2025  
**arXiv**: [2505.12891](https://arxiv.org/abs/2505.12891)  
**代码**: [GitHub + HuggingFace](https://huggingface.co/datasets)  
**领域**: LLM推理  
**关键词**: 时间推理, benchmark, 多层级评测, LLM, 真实场景

## 一句话总结

提出TimE多层级时间推理Benchmark（38,522 QA + 943人工标注TimE-Lite），覆盖知识密集（Wiki）、快速演变（News）和长对话（Dialogue）三种真实场景，设计三级渐进11子任务体系评估24个LLM，揭示即使最强推理模型在复杂时间关系推理上仍有显著短板。

## 研究背景与动机

**领域现状**：LLM在数学推理和代码生成上已接近人类水平，但时间推理能力仍显著不足。

**现有痛点**：现有benchmark如TimeBench和TRAM聚焦简化场景（短文本简单QA），无法反映真实世界三大挑战：密集时间信息、快速事件动态、社交中的复杂时间依赖。

**核心矛盾**：时间推理是层级化能力框架，但现有工作忽视这种结构——TReMu只关注神经符号推理，TCELongBench忽略基础时间概念。

**本文要解决什么？** 构建能全面、公平、细粒度评估LLM在多种真实场景下时间推理能力的统一benchmark。

**切入角度**：三级渐进任务体系 + 三种真实数据源。

**核心idea一句话**：统一多层级任务框架+多样化真实场景实现LLM时间推理能力的细粒度诊断。

## 方法详解

### 整体框架

三个子数据集——TimE-Wiki（13,848 QA，Wikidata时间知识图谱）、TimE-News（19,958 QA，在线新闻+RAG）、TimE-Dial（4,716 QA，多轮长对话），每个覆盖三级任务。数据流程：收集时间事实→构建时间线→规则+LLM合成QA→STARC误导选项→人工标注验证。

### 关键设计

1. **三级渐进任务体系**:
    - 功能：从基础到复杂逐级评估时间推理
    - 核心思路：Level-1（5子任务）——基础理解检索（Extract/Localization/Computation/DurationCompare/OrderCompare）；Level-2（3子任务）——时间表达式推理（Explicit/Order/Relative）；Level-3（3子任务）——复杂关系推理（Co-temporality/Timeline/Counterfactual）
    - 设计动机：模拟人类认知过程——先捕获概念、再推理隐含时间、最后理解事件关系

2. **三维真实场景数据源**:
    - 功能：覆盖三种不同维度的时间推理挑战
    - 核心思路：Wiki（知识密度）、News（事件动态）、Dialogue（跨会话依赖，平均>15K tokens）
    - 设计动机：不同场景的挑战维度互补

3. **质量控制体系**:
    - 功能：确保生成QA质量和评估可靠性
    - 核心思路：基于时间线的逻辑正确性保证 + STARC误导选项 + 人工标注（Word-level Similarity 0.6626）+ 合成-人工一致率89.13%
    - 设计动机：避免LLM生成偏差，确保benchmark可靠

## 实验关键数据

### 主实验
| 模型 | Wiki L1均值 | Wiki L2均值 | Wiki L3均值 | News Timeline | Dial Extract(max) |
|------|-------------|-------------|-------------|---------------|-------------------|
| o3-mini | ~90% | ~61% | ~47% | 33.33% | - |
| GPT-4o | ~86% | ~58% | ~39% | 20.00% | - |
| DeepSeek-R1 | ~81% | ~64% | ~45% | 33.33% | - |
| Qwen2.5-72B | ~71% | ~50% | ~35% | - | - |
| Llama3.1-8B | ~48% | ~28% | ~20% | 3.09% | ~40% |

### 消融实验
| 配置 | 关键指标 | 说明 |
|------|---------|------|
| TimE vs TimE-Lite | 一致率89.13% | 合成数据质量高 |
| BM25 vs Vector vs Hybrid | Hybrid最佳 | 混合检索策略最优 |
| 推理 vs 非推理模型 | L1提升大，L3有限 | test-time scaling对基础计算帮助大，复杂推理有限 |

### 关键发现
- **知识密集场景**：o3-mini在Order/Relative Reasoning仅~52%/49%——复杂时间表达式严重阻碍模型
- **动态事件场景**：所有模型在Timeline任务（排序3事件）不超30%——事件细节相似导致定位错误
- **长对话场景**：Extract/Localization最高仅~40%——超长上下文+记忆型时间表达极大增加难度
- 推理模型的test-time scaling对时间计算有显著提升，对复杂推理帮助有限

## 亮点与洞察
- 三级任务设计精巧，能精确定位模型能力断裂点
- 三个数据源互补性强，各挑战不同维度
- 发现推理模型在时间计算上强但在复杂关系推理上仍有限
- TimE-Lite人工验证确保benchmark可靠性

## 局限性 / 可改进方向
- 数据生成依赖特定LLM可能引入偏差
- News RAG可能引入检索噪声
- 仅英文评估，多语言时间表达差异未考虑

## 相关工作与启发
- **vs TimeBench**: 聚合多数据集，任务过简且偏差大；TimE提供统一评估上下文
- **vs TReMu**: 仅关注特定方面；TimE全面覆盖基础到复杂

## 评分
- 新颖性: ⭐⭐⭐ benchmark有价值但本质是数据集构建
- 实验充分度: ⭐⭐⭐⭐ 24个模型广泛评估，分析深入
- 写作质量: ⭐⭐⭐⭐ 任务定义清晰，分析有深度
- 价值: ⭐⭐⭐⭐ 填补LLM时间推理评测空白
