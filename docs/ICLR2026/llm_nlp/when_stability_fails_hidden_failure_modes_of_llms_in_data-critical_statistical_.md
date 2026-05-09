---
title: >-
  [论文解读] When Stability Fails: Hidden Failure Modes of LLMs in Data-Constrained Scientific Decision-Making
description: >-
  [ICLR2026][LLM/NLP][LLM评估] 揭示 LLM 在数据约束的科学决策任务中的隐藏失败模式：模型可以展现近乎完美的运行间稳定性，同时系统性偏离统计学基准真值，表现为过度选择、prompt 敏感和幻觉基因标识符。
tags:
  - ICLR2026
  - LLM/NLP
  - LLM评估
  - 科学决策
  - 稳定性
  - 正确性
  - 基因优先级排序
  - 差异表达分析
---

# When Stability Fails: Hidden Failure Modes of LLMs in Data-Constrained Scientific Decision-Making

**会议**: ICLR2026  
**arXiv**: [2603.15840](https://arxiv.org/abs/2603.15840)  
**代码**: [github.com/NaziaRiasat/llm-prompt-sensitivity](https://github.com/NaziaRiasat/llm-prompt-sensitivity)  
**领域**: LLM/NLP  
**关键词**: LLM评估, 科学决策, 稳定性, 正确性, 基因优先级排序, 差异表达分析

## 一句话总结
揭示 LLM 在数据约束的科学决策任务中的隐藏失败模式：模型可以展现近乎完美的运行间稳定性，同时系统性偏离统计学基准真值，表现为过度选择、prompt 敏感和幻觉基因标识符。

## 背景与动机
- LLM 越来越多被用于科学工作流中的决策支持工具（数据解释、假设生成、候选基因优先级排序等）
- 评估实践通常强调**稳定性**（运行间可重复性）作为可靠性指标
- 但在结构化科学决策任务中，稳定性**不等于正确性**——当统计学标准答案存在时，稳定的输出可能系统性偏离真值
- 核心问题：LLM 的运行间一致性能否作为科学任务中正确性的代理指标？

## 核心问题
当可靠的统计学参考标准可用时，LLM 的稳定性是否足以保证其输出的正确性？本文通过控制实验系统性地分离四个行为维度来回答这一问题。

## 方法详解

### 评估框架设计
基于差异表达 (DE) 分析的基因优先级排序任务：
- **输入**：固定的 DESeq2 差异表达结果表（RNA-seq 数据，GSE239514）
- **统计参考**：DESeq2 确定性分析结果作为基准真值
- **评估模型**：ChatGPT (GPT-5.2)、Google Gemini 3、Claude Opus 4.5
- **所有模型使用温度 = 0 的确定性解码**

### 四个评估维度
1. **稳定性 (Stability)**：运行间输出一致性，使用 Jaccard 相似度和重叠系数衡量
2. **正确性 (Correctness)**：与 DESeq2 统计参考的一致程度
3. **Prompt 敏感性 (Prompt Sensitivity)**：语义等价 prompt 间的输出差异
4. **输出有效性 (Output Validity)**：模型生成的基因标识符是否在输入表中存在

### Prompt 体系设计
多种 prompt 条件覆盖典型分析场景：
- **P1**：严格阈值（FDR ≤ 0.05）
- **P5**：宽松阈值（0.05 < FDR ≤ 0.10）
- **P6**：边界 Top-20 选择
- **P7a vs P7b**：语义等价但措辞不同（统计显著性 vs 效应量优先）
- **P9**：显式排名 Top-20

每个配置运行 10 次，相同输入。

### 评估指标

**Jaccard 相似度**：
$$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$

**重叠系数**（处理不等大小集合）：
$$O(A, B) = \frac{|A \cap B|}{\min(|A|, |B|)}$$

### 数据特征
- 0 个基因满足 FDR ≤ 0.05
- 35 个基因在 0.05 < FDR ≤ 0.10 范围
- 127 个基因在 0.05 < FDR ≤ 0.15 范围

## 实验关键数据

### 核心结果汇总

| Prompt | 任务类型 | 指标 | ChatGPT | Gemini | Claude | 解释 |
|--------|---------|------|---------|--------|--------|------|
| P1 (FDR≤0.05) | 阈值DE | Jaccard vs truth | 1.00 | 1.00 | 0.00 | Claude 无法恢复 DE 基因 |
| P5 (FDR≤0.10) | 宽松阈值 | Jaccard vs truth | 0.47 | 0.28 | 0.00 | 过度选择/崩溃 |
| P6 (边界) | 排序不确定 | Jaccard vs truth | 0.14 | 1.00 | 0.00 | Gemini 恢复真值 |
| P6 (稳定性) | 模型内 | Pairwise Jaccard | **1.00** | **1.00** | **1.00** | 完美内部稳定性 |
| P7a vs P7b | Prompt敏感 | Jaccard | 0.74 | 0.08 | 1.00 | 高措辞敏感性 |
| P9 (排名) | 有效性 | 无效基因ID/轮 | 0 | 0 | **20** | 幻觉标识符 |

### 关键观察汇总

| 失败模式 | ChatGPT | Gemini | Claude |
|---------|---------|--------|--------|
| 运行间稳定性 | ✓ 完美 | ✓ 完美 | ✓ 完美 |
| 与统计参考一致 | 部分（P5:0.47, P6:0.14） | 部分（P5:0.28, P6:1.00） | ✗ 系统性失败 |
| Prompt 措辞敏感 | 中等 (0.74) | 严重 (0.08) | 不敏感 (1.00) |
| 输出有效性 | ✓ | ✓ | ✗ (每轮20个无效ID) |

## 四种失败模式详解

### 1. 稳定性不等于正确性
- 所有模型展现近乎完美的运行间稳定性（Pairwise Jaccard = 1.00）
- 但与 DESeq2 参考的 Jaccard 从 0 到 1.00 不等
- Jaccard = 0 意味着预测集与参考集**无任何重叠**
- 结论：确定性行为反映内部一致性，而非可靠的统计推理

### 2. 宽松阈值下的过度选择
- 从 FDR ≤ 0.05 放宽到 0.05 < FDR ≤ 0.10 后：
    - ChatGPT Jaccard 从 1.00 降至 0.47
    - Gemini 从 1.00 降至 0.28
    - Claude 始终为 0.00
- 表现为广泛纳入或完全崩溃，而非有原则的灵敏度-特异度权衡

### 3. Prompt 措辞敏感性
- P7a（统计显著性优先）和 P7b（效应量优先）仅措辞微调：
    - Gemini 的 Jaccard 仅为 0.08（几乎完全不同的基因集）
    - ChatGPT 为 0.74（中等差异）
    - Claude 为 1.00（不敏感但可能是因为系统性失败）
- Prompt 措辞充当**隐性决策变量**而非中性指示

### 4. 幻觉基因标识符
- Claude 在 P9 设置下每轮产生 20 个不在输入表中的基因 ID
- 这些 ID 语法上合理、形似真实基因名称，但完全不在输入数据中
- ChatGPT 和 Gemini 输出仅包含有效标识符
- 这是系统性违反输入域约束，而非偶发格式噪声

## 亮点
1. **问题定义精准**：清晰分离稳定性/正确性/敏感性/有效性四个维度
2. **控制实验设计严谨**：固定输入数据、确定性解码、相同统计参考
3. **实际价值高**：对 LLM 在科学工作流中的应用提出重要警示
4. **发现具有普遍意义**：稳定性≠正确性的结论不限于基因分析领域
5. **Claude 的系统性幻觉发现**：暴露了约束生成中的严重可靠性问题

## 局限性 / 可改进方向
- 仅使用单一差异表达数据集和单一统计范式
- 评估对象仅三个商业模型，未涵盖开源模型
- 未探索 prompt 优化策略是否能缓解失败模式
- 基因优先级排序是特定生物信息学任务，结论的跨领域验证不足
- 未讨论 few-shot 示例或 RAG 是否能改善正确性
- 统计推理任务中 FDR ≤ 0.05 恰好 0 个显著基因，这一特殊情况可能放大了某些失败模式

## 与相关工作的对比
- 相比一般 LLM 幻觉研究（Li et al. 2024）：本文在受控统计任务中量化幻觉
- 相比 prompt 敏感性研究（Zhu et al. 2023）：本文在科学决策场景中验证
- 相比 LLM 临床推理评估（Singhal 2023）：本文使用确定性统计基准真值
- 创新之处在于将多个已知问题（幻觉、敏感性、稳定性假象）统一在受控框架中分析

## 启发与关联
- LLM 辅助科学管线需要显式基准真值验证和输入域有效性检查
- 不应以输出稳定性或内部一致性替代正确性验证
- Prompt 措辞对科学决策的影响比预期更大，需要标准化 prompt 协议
- 对 LLM-in-the-loop 的科学工作流设计有直接指导意义
- 可扩展到其他定量决策任务（药物筛选、临床试验分析等）

## 评分
- 新颖性: ⭐⭐⭐ (观察有价值但各失败模式已分别被报道，创新在于统一框架)
- 实验充分度: ⭐⭐⭐ (控制设计严谨但仅1个数据集、3个模型、1个任务)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，四个维度的分离叙述有力)
- 价值: ⭐⭐⭐⭐ (对科学社区使用LLM具有重要警示作用)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Statistical Advantage of Softmax Attention: Insights from Single-Location Regression](statistical_advantage_of_softmax_attention_insights_from_single-location_regress.md)
- [\[ICLR 2026\] Unsupervised Evaluation of Multi-Turn Objective-Driven Interactions](unsupervised_evaluation_of_multi-turn_objective-driven_interactions.md)
- [\[ICLR 2026\] The Lattice Representation Hypothesis of Large Language Models](the_lattice_representation_hypothesis_of_large_language_models.md)
- [\[ICLR 2026\] Is the Reversal Curse a Binding Problem? Uncovering Limitations of Transformers from a Basic Generalization Failure](is_the_reversal_curse_a_binding_problem_uncovering_limitations_of_transformers_f.md)
- [\[ICLR 2026\] Trapped by simplicity: When Transformers fail to learn from noisy features](trapped_by_simplicity_when_transformers_fail_to_learn_from_noisy_features.md)

</div>

<!-- RELATED:END -->
