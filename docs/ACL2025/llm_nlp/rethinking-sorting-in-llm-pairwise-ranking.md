---
title: >-
  [论文解读] Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching and Caching
description: >-
  [ACL 2025][LLM/NLP][成对排序] 本文重新审视了 LLM 成对排序提示（PRP）中排序算法的效率分析，以 LLM 推理调用次数（而非传统比较次数）为成本度量，提出批处理和缓存优化，证明在 LLM 场景下 Quicksort 可以比 Heapsort 减少 44% 的推理调用。
tags:
  - ACL 2025
  - LLM/NLP
  - 成对排序
  - LLM重排序
  - 排序算法
  - 批处理优化
  - 推理效率
---

# Are Optimal Algorithms Still Optimal? Rethinking Sorting in LLM-Based Pairwise Ranking with Batching and Caching

**会议**: ACL 2025  
**arXiv**: [2505.24643](https://arxiv.org/abs/2505.24643)  
**代码**: 无  
**领域**: LLM/NLP  
**关键词**: 成对排序, LLM重排序, 排序算法, 批处理优化, 推理效率

## 一句话总结

本文重新审视了 LLM 成对排序提示（PRP）中排序算法的效率分析，以 LLM 推理调用次数（而非传统比较次数）为成本度量，提出批处理和缓存优化，证明在 LLM 场景下 Quicksort 可以比 Heapsort 减少 44% 的推理调用。

## 研究背景与动机

1. **领域现状**：成对排序提示（PRP）是一种零样本 LLM 重排序方法，每次比较两个文档来确定排序。研究者使用 Heapsort 来最小化比较次数。
2. **现有痛点**：传统排序理论将每次比较视为等成本原子操作，但 LLM 推理调用是主要成本瓶颈。批处理和缓存等基本优化会根本性地改变算法效率排名。
3. **核心矛盾**：经典最优算法（如 Heapsort）在 LLM 推理成本模型下可能不再最优。
4. **本文目标**：建立以 LLM 推理调用为核心的排序算法分析框架。
5. **切入角度**：分析 Heapsort、Bubblesort、Quicksort 在批处理和缓存优化下的推理调用次数。
6. **核心 idea**：Quicksort 的分区阶段天然支持批处理——多个元素可同时与 pivot 比较，一次推理完成多个比较。

## 方法详解

### 整体框架

分析三种排序算法在批处理、缓存和top-k三种优化下的适用性，以推理调用次数为核心指标。

### 关键设计

1. **Quicksort + 批处理**: 分区阶段多个元素同时与pivot比较，batch size=2时即比Heapsort减少44%推理调用。
2. **Bubblesort + 缓存**: 相邻比较跨pass重复，缓存结果避免重复推理。
3. **Heapsort**: 二叉堆结构不支持批处理也不支持缓存——每次比较是顺序且唯一的。

### 损失函数 / 训练策略

理论分析+实证验证，无训练。在TREC DL 2019/2020和BEIR基准上验证。

## 实验关键数据

### 主实验

batch size=2时 Quicksort 比 Heapsort 减少 44% 推理调用，排序质量相同。

### 关键发现

- 传统最优算法（Heapsort）在LLM场景下不再最优
- 批处理和缓存不改变排序结果，只减少推理调用
- 首次将 Quicksort 引入 PRP 场景

### 算法推理调用次数对比

| 算法 | 比较次数 | 推理调用(batch=2) | 缓存节省 |
|------|---------|-----------------|--------|
| Heapsort | O(nlogn) | O(nlogn) | 不可缓存 |
| Bubblesort | O(n²) | O(n²) | 30-40% |
| **Quicksort** | O(nlogn) | **O(nlogn/2)** | 不需要 |

### TREC DL验证结果

| 数据集 | 算法 | 推理调用减少 | nDCG@10 |
|--------|------|-----------|--------|
| TREC DL 2019 | QS vs HS | -44% | 相同 |
| TREC DL 2020 | QS vs HS | -42% | 相同 |
| BEIR-NQ | QS vs HS | -43% | 相同 |


## 亮点与洞察

- 简洁有力的核心观察：将成本模型从"比较次数"转换到"推理调用次数"就颠覆了传统智慧。
- 实用价值高，对任何使用LLM做成对比较的系统都有指导意义。

## 局限与展望

- 分析假设每次推理调用成本相同（不区分batch大小的延迟差异），实际GPU吞吐量可能非线性
- 仅考虑了三种经典算法（Heapsort、Bubblesort、Quicksort），未覆盖Mergesort、Timsort等
- Quicksort的最坏情况复杂度O(n²)在极端情况下可能成为问题（虽然平均O(nlogn)）
- 分析主要基于理论，大规模实证验证（如百万级文档排序）有限
- 未讨论算法选择与文档数量的关系（小n和大n可能偏好不同算法）
- 批处理的最优batch size与硬件配置（GPU内存、模型大小）相关，需要具体调优

## 相关工作与启发

- **vs Qin et al. (PRP)**: 使用Heapsort因其O(nlogn)和top-k支持，本文证明考虑LLM推理成本后Quicksort更高效
- **vs Zhuang et al.**: 也研究PRP中的排序优化，但未重新审视成本模型本身
- **vs Listwise Ranking**: 将多个文档一次性输入LLM排序，受上下文长度限制且排序质量不稳定
- **vs 传统IR系统**: 使用学习到的排序函数，PRP的优势在于零样本但代价是推理成本高


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
- 长期评估和用户研究可以提供更全面的方法评价。

## 评分

- 新颖性: ⭐⭐⭐⭐ 成本模型的重新定义视角新颖
- 实验充分度: ⭐⭐⭐⭐ 理论+标准IR基准验证
- 写作质量: ⭐⭐⭐⭐ 简洁清晰
- 价值: ⭐⭐⭐⭐ 对LLM排序实践有直接指导意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](unintended_harms_of_value-aligned_llms_psychological_and_empirical_insights.md)
- [\[ACL 2025\] Can LLMs Interpret and Leverage Structured Linguistic Representations? A Case Study with AMRs](can_llms_interpret_and_leverage_structured_linguistic_representations_a_case_stu.md)
- [\[ACL 2025\] Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](salience_sparse_fine_tuning.md)
- [\[ACL 2025\] Zero-Shot Belief: A Hard Problem for LLMs](zero-shot_belief_a_hard_problem_for_llms.md)
- [\[ACL 2025\] SR-LLM: Rethinking the Structured Representation in Large Language Model](sr-llm_rethinking_the_structured_representation_in_large_language_model.md)

</div>

<!-- RELATED:END -->
