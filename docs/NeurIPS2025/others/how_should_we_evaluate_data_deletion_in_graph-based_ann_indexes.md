---
title: >-
  [论文解读] How Should We Evaluate Data Deletion in Graph-Based ANN Indexes?
description: >-
  [NeurIPS 2025 (ML for Systems Workshop)][Approximate Nearest Neighbor Search] 针对图索引（graph-based ANNS）中数据删除缺乏系统评估方法的问题，形式化定义了三种删除策略（逻辑删除、物理删除、重建），提出一套面向实际部署的评估框架和指标体系，并在 HNSW 上实验分析后提出 Deletion Control 算法，可根据精度需求动态选择删除策略。
tags:
  - NeurIPS 2025 (ML for Systems Workshop)
  - Approximate Nearest Neighbor Search
  - data deletion
  - HNSW
  - graph-based index
  - evaluation methodology
---

# How Should We Evaluate Data Deletion in Graph-Based ANN Indexes?

**会议**: NeurIPS 2025 (ML for Systems Workshop)  
**arXiv**: [2512.06200](https://arxiv.org/abs/2512.06200)  
**代码**: 无  
**领域**: Information Retrieval / Systems  
**关键词**: Approximate Nearest Neighbor Search, data deletion, HNSW, graph-based index, evaluation methodology

## 一句话总结

针对图索引（graph-based ANNS）中数据删除缺乏系统评估方法的问题，形式化定义了三种删除策略（逻辑删除、物理删除、重建），提出一套面向实际部署的评估框架和指标体系，并在 HNSW 上实验分析后提出 Deletion Control 算法，可根据精度需求动态选择删除策略。

## 研究背景与动机

近似最近邻搜索（ANNS）是 RAG、推荐系统等应用的核心构建块。这些应用中数据频繁更新——新产品上架、下架商品删除——因此需要支持动态数据的 ANNS 算法。

现有工作的关键不足：

**缺乏综合评估方法论**：现有研究（FreshDiskANN、MN-RU、IPGM）各自使用不同的实验设置和指标，无法横向比较

**实验设置不切实际**：如 FreshDiskANN 和 MN-RU 在实验中重新插入已删除的数据，这在实际场景中不会发生

**评估指标不全面**：现有研究通常只关注搜索精度，忽略了删除速度、插入速度、内存占用等同等重要的指标

本文的目标是统一、规范化数据删除的评估方法，为实际部署场景提供可靠的决策依据。

## 方法详解

### 整体框架

论文将图索引中的数据删除方法分为三类，并对每类给出严格的形式化数学定义。

### 关键设计

1. **逻辑删除（Logical Deletion）**：不修改图结构，仅为被删除节点添加标志位 $\mathcal{F} \subseteq \{1, 2, \ldots, n\}$。搜索时先正常搜索再从结果中过滤被标记节点。

    - **优势**：删除速度极快（仅设置 flag），$O(1)$ 操作
    - **劣势**：内存持续增长（删除数据仍在内存中）；搜索精度随删除量增加而下降；搜索速度因额外过滤操作而变慢
    - **形式化**：$\mathcal{F} \leftarrow \mathcal{F} \cup \mathcal{D}$，搜索返回 $\mathcal{R} \leftarrow \text{SEARCH}(\mathbf{q}, \mathcal{P}, \mathcal{N}) \setminus \mathcal{F}$

2. **物理删除（Physical Deletion）**：从图中移除被删除节点及其所有连接边，同时更新邻居节点的邻接表。

    - **优势**：释放内存，保持合理精度
    - **劣势**：删除边可能破坏图连通性，影响搜索精度
    - **形式化**：对 $\mathbf{p}_i \in \mathcal{D}$，$\mathcal{P} \leftarrow \mathcal{P} \setminus \{\mathbf{p}_i\}$；对其余节点 $j \neq i$，$\mathcal{N}_j \leftarrow \mathcal{N}_j \setminus \mathcal{D}$

3. **重建（Rebuilding）**：删除数据后，用剩余数据完全重新构建索引。

    - **优势**：保证最优搜索精度
    - **劣势**：计算代价极高
    - **形式化**：$\mathcal{P} \leftarrow \{\mathbf{p}_i \in \mathcal{P} \mid i \notin \mathcal{D}\}$，$\mathcal{N} \leftarrow \text{CONSTRUCT}(\mathcal{P})$

### 评估指标体系

论文提出多维度评估指标：

- **搜索精度**：1-Recall@10 = $\frac{1}{n_q}\sum_{i=1}^{n_q} f(g_i \in \hat{\mathcal{R}}_i)$
- **搜索速度**：QPS-search（每秒查询数）
- **插入速度**：QPS-add
- **删除速度**：QPS-delete
- **内存占用**：随删除步数变化的内存使用
- **QPS-Recall 曲线**：搜索速度 vs 精度的权衡曲线

### Deletion Control 算法

基于实验发现提出的自适应策略。核心思想是根据精度需求 $\alpha$ 动态选择删除方法：

- 引入参数 $\theta$（物理删除收敛后的最低 1-Recall@10）和 $\pi$（逻辑删除保持精度高于 $\alpha$ 的最大步数）
- **当 $\alpha < \theta$**：只用物理删除（精度永远不会低于 $\theta$）
- **当 $\alpha \geq \theta$**：交替使用逻辑删除（$\pi$ 步）和重建（1 次），利用逻辑删除的速度优势同时用重建维持精度
- $\pi$ 的估计：将 1-Recall@10 随步数的变化近似为线性函数 $\Delta = (R_S - R_0)/S$，则 $\pi \approx (\alpha - R_0)/\Delta$

## 实验关键数据

### 实验设置

使用 5 个标准数据集：SIFT1M（128维）、GIST1M（960维）、SIFT1B（128维，取 2M 子集）、DEEP1M（96维）、Glove100Angular（100维）。在 HNSW 上实现三种删除方法，通过反复插入/删除同等批量数据评估性能。

### 主实验（三种删除方法对比）

| 指标 | 逻辑删除 | 物理删除 | 重建 |
|------|---------|---------|------|
| 删除速度（QPS-delete） | ~$10^9$ 1/s（最快） | ~$10^3$ 1/s | ~$10^3$ 1/s |
| 搜索精度（多步后）| 持续下降 | 趋于稳定常数 | 始终最高 |
| 内存占用 | 线性增长 | 不变 | 不变 |
| 搜索速度 | 最慢（额外过滤） | 最快（图稀疏化） | 中等 |
| 插入速度 | 正常 | 最快（图稀疏化减少距离计算） | 正常 |

### 关键发现（跨数据集一致）

| 发现 | 详细说明 |
|------|---------|
| 物理删除精度收敛 | 多次更新后 1-Recall@10 稳定在常数值 $\theta$，不再下降 |
| batch 大小影响收敛精度 | 更大 batch → 更高的收敛精度（插入过程更好恢复图结构） |
| 逻辑删除精度线性下降 | 1-Recall@10 随步数近似线性减少 |
| 向量维度仅影响重建速度 | GIST（960维）vs SIFT（128维），物理/逻辑删除速度不变，重建变慢 |
| 小 batch 下重建相对更慢 | batch 从 $10^5$ 降到 $10^3$，重建速度下降约 100 倍（固定开销主导） |

### Deletion Control 实验

在 SIFT1B（$b=10^5$）上设 $\alpha = 0.84$：
- 估计 $\theta = 0.816$，$\pi = 1$
- 因 $\alpha > \theta$，选择「逻辑删除 + 定期重建」策略
- 结果：在测试集上几乎满足精度要求，且总删除时间是所有满足精度要求方案中最小的

## 亮点与洞察

- **形式化定义三种删除策略**并提供统一的伪代码描述，清晰区分了各方法的本质差异
- **物理删除精度收敛现象**是一个重要但此前未被注意到的发现：图结构在多次更新后趋于稳定
- **评估框架的系统性**：同时覆盖精度、速度、内存多个维度，比之前单一指标评估更全面
- **Deletion Control 的实用性**：simple yet effective，根据精度需求自动选择最优策略

## 局限性 / 可改进方向

1. **仅在 HNSW 上验证**：未扩展到 DiskANN、IVFPQ 等其他图索引或非图索引方法
2. **单线程实验**：实际部署通常是多线程，并发删除/搜索的竞态条件未考虑
3. **未考虑高级删除方法**：如 FreshDiskANN 的边重连、IPGM 的邻居重计算等，三种策略都是最基础的 baseline
4. **Deletion Control 假设 1-Recall@10 线性下降**：对更复杂场景可能不成立
5. **数据集规模有限**：SIFT1B 只取了 2M 子集，真正十亿级场景的表现未知
6. **未讨论删除分布的影响**：随机删除 vs 聚类删除可能对图结构影响差异很大

## 相关工作与启发

- **FreshDiskANN**：基于 DiskANN 的动态 ANNS，删除时重连邻居边以维持精度
- **MN-RU**：通过备份图（backup graph）解决 HNSW 中删除后不可达节点的问题
- **IPGM**：重计算被删除节点一跳范围内所有邻居并重连边
- **Ada-IVF / SPFresh**：基于倒排文件结构处理动态数据
- 核心启示：**评估方法论与算法本身同等重要**——没有统一标准就无法公平比较和推进研究

## 评分
- 新颖性: ⭐⭐⭐ (评估框架和形式化定义有价值，但缺少全新算法贡献)
- 实验充分度: ⭐⭐⭐⭐ (5 个数据集、多指标、多 batch 大小、消融完整)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，数学定义严谨)
- 价值: ⭐⭐⭐ (为 ANNS 社区提供统一评估标准，Deletion Control 有实用价值)
