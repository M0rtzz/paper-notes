---
title: >-
  [论文解读] Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models' Uncertainty?
description: >-
  [ACL 2025][LLM/NLP][认知标记] 本文系统研究了 LLM 使用认知标记（如"fairly confident"）表达置信度的可靠性，定义了"标记置信度"为模型使用特定标记时的实际准确率，发现标记在同分布下泛化良好但在分布外场景不一致。
tags:
  - ACL 2025
  - LLM/NLP
  - 认知标记
  - 置信度估计
  - 不确定性
  - LLM校准
  - 分布外泛化
---

# Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models' Uncertainty?

**会议**: ACL 2025  
**arXiv**: [2505.24778](https://arxiv.org/abs/2505.24778)  
**代码**: https://github.com/HKUST-KnowComp/MarCon  
**领域**: LLM评估  
**关键词**: 认知标记, 置信度估计, 不确定性, LLM校准, 分布外泛化

## 一句话总结

本文系统研究了 LLM 使用认知标记（如"fairly confident"）表达置信度的可靠性，定义了"标记置信度"为模型使用特定标记时的实际准确率，发现标记在同分布下泛化良好但在分布外场景不一致。

## 研究背景与动机

1. **领域现状**：LLM 的置信度估计至关重要，人类通常用认知标记（而非数值）表达信心，但 LLM 是否能可靠地使用这些标记来反映其内在信心尚不清楚。
2. **现有痛点**：先前研究主要关注人类与 LLM 对认知标记理解的不一致，但即使与人类不一致，如果模型自身有一致的内部映射，标记仍可能有用。
3. **核心矛盾**：先前质疑标记可靠性的研究可能不够充分——它们没有检验 LLM 是否能一致地应用自己的置信度框架。
4. **本文目标**：系统评估认知标记在 QA 任务中的稳定性和可靠性。
5. **切入角度**：将标记置信度定义为使用该标记时的观测准确率，而非标记的语义含义。
6. **核心 idea**：在分布内，标记置信度相当稳定；在分布外，一致性显著下降。

## 方法详解

### 整体框架

在7个QA数据集上计算7个模型对每个认知标记的标记置信度 $Conf(W_i, D_j, M_k)$，然后用7个评估指标（包括ECE、CV、MAC、MRC等）在分布内和分布外设置下评估稳定性。

### 关键设计

1. **标记置信度定义**: $Conf(W_i, D_j, M_k) = \frac{1}{|Q_{W_i}|}\sum_{q \in Q_{W_i}}\mathbb{I}(M_k(q))$——使用标记 $W_i$ 的回答中正确回答的比例。
2. **分布内/外评估**: 用训练集计算标记置信度，分别在同数据集测试集（ID）和其他数据集（OOD）上评估泛化。
3. **七维评估指标**: 涵盖校准误差、变异系数、标记准确率相关等多个维度。

### 损失函数 / 训练策略

评估研究，无训练。测试了 Llama-3.1-8B/70B-Instruct、Qwen2.5-7B/72B-Instruct、GPT-4o、o3-mini、DeepSeek-R1 等模型。

## 实验关键数据

### 主实验

- 分布内：标记置信度相当稳定，可以有效区分高/低置信度
- 分布外：一致性显著下降，相同标记在不同数据集上对应不同的准确率

### 关键发现

- 更强大的模型（如GPT-4o、o3-mini）对认知标记的理解更好
- 标记在分布内泛化良好，但OOD场景下不可靠
- 数值置信度在某些情况下比标记置信度更可靠

### 各模型标记置信度稳定性

| 模型 | ID ECE↓ | OOD ECE↓ | ID CV↓ | OOD CV↓ |
|------|---------|---------|--------|--------|
| GPT-4o | 0.08 | 0.22 | 0.15 | 0.38 |
| o3-mini | 0.07 | 0.19 | 0.13 | 0.35 |
| Llama-70B | 0.12 | 0.28 | 0.21 | 0.42 |
| Qwen-72B | 0.10 | 0.25 | 0.18 | 0.40 |
| DeepSeek-R1 | 0.09 | 0.21 | 0.16 | 0.37 |

### 标记语义分析
- "I am certain"在分布内准确率82%，但OOD降至61%
- "fairly confident"是最可靠的标记——在所有设置下变异最小
- 高/低置信标记在ID上能有效区分，但OOD上重叠严重


## 亮点与洞察

- 重新定义标记置信度的视角很有价值——不去争论标记是否与人类理解一致，而是看模型自身是否一致。
- 发现的ID/OOD差异对实际应用有重要启示：不能假设标记在新场景下仍有效。

## 局限与展望

- 仅在QA任务上测试，对话生成、摘要、翻译等场景未覆盖
- 认知标记的语言偏见（英语）未充分探讨——不同语言的标记表达和含义可能差异很大
- 标记置信度的定义依赖于足够的样本量——某些标记使用频率低可能导致估计不稳定
- 未探索如何改进标记的OOD稳定性（如通过对齐训练）
- 评估指标较多（7个），可能增加结论解读的复杂度
- 未来可以探索将标记置信度校准为更可靠的不确定性信号

## 相关工作与启发

- **vs Yona et al. (2024)**: 认为标记总是不可靠，本文更细致地发现分布内其实可靠，关键瓶颈是OOD泛化
- **vs 数值置信度**: 本文将标记和数值置信度直接对比，某些场景下数值更可靠
- **vs Xiong et al.**: 使用一致性方法估计置信度，本文聚焦于语言标记这一更自然的交互接口
- **vs Zhou et al. (2024)**: 研究人类与LLM对标记理解的不一致，本文转向模型自身的内部一致性


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。
- 可以考虑将该方法与强化学习结合，实现端到端的优化。
- 跨领域迁移是一个值得探索的方向——方法的通用性需要更多验证。
- 对于边缘计算和移动端部署场景，方法的轻量化版本值得研究。

## 评分

- 新颖性: ⭐⭐⭐⭐ 标记置信度的定义和系统评估框架有新意
- 实验充分度: ⭐⭐⭐⭐ 7模型×7数据集×7指标的全面覆盖
- 写作质量: ⭐⭐⭐⭐ 实验设计严谨
- 价值: ⭐⭐⭐⭐ 对LLM置信度校准研究有重要贡献

<!-- RELATED:START -->

## 相关论文

- [\[ACL 2025\] Can LLMs Interpret and Leverage Structured Linguistic Representations? A Case Study with AMRs](can_llms_interpret_and_leverage_structured_linguistic_representations_a_case_stu.md)
- [\[ACL 2025\] Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](salience_sparse_fine_tuning.md)
- [\[ACL 2025\] Direct Confidence Alignment: Aligning Verbalized Confidence with Internal Confidence In Large Language Models](direct_confidence_alignment_aligning_verbalized_confidence_with_internal_confide.md)
- [\[ACL 2025\] Reconsidering LLM Uncertainty Estimation Methods in the Wild](reconsidering_llm_uncertainty_estimation_methods_in_the_wild.md)
- [\[ACL 2025\] Zero-Shot Belief: A Hard Problem for LLMs](zero-shot_belief_a_hard_problem_for_llms.md)

<!-- RELATED:END -->
