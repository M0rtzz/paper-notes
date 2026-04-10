<!-- 由 src/gen_stubs.py 自动生成 -->
# How Should We Evaluate Data Deletion in Graph-Based ANN Indexes?

**会议**: NEURIPS2025 (Workshop on ML for Systems)  
**arXiv**: [2512.06200](https://arxiv.org/abs/2512.06200)  
**代码**: 待确认  
**领域**: others  
**关键词**: Approximate Nearest Neighbor Search, HNSW, Data Deletion, Graph-based Index, Dynamic Data  

## 一句话总结

提出了一套面向实际部署场景的图基 ANN 索引数据删除评估框架，形式化定义了三种删除策略（logical/physical/rebuilding），并在 HNSW 上实验验证后提出了 Deletion Control——一种根据精度要求动态切换删除策略的算法。

## Problem

Approximate Nearest Neighbor Search (ANNS) 在 RAG、推荐系统等应用中至关重要。这些应用场景下数据频繁增删（如商品上架/下架），因此需要支持动态数据的 ANNS 算法。然而，目前缺乏一套**全面且贴近实际部署**的数据删除评估方法论：

- 现有评估实验设置不够现实，如 FreshDiskANN 和 MN-RU 的实验中会重新插入已删除数据
- 评估指标不够全面，通常只关注搜索精度，忽略了删除速度、插入速度、内存占用等关键指标
- 缺乏对不同删除方法的统一数学形式化与系统性对比

## Core Idea

论文的核心贡献有三点：

1. **形式化定义三种删除策略**：将图基 ANNS 中的删除方法统一归纳为 logical deletion、physical deletion 和 rebuilding，并给出数学定义
2. **建立部署导向的评估框架**：设计了一套现实的实验协议，综合评估删除延迟、搜索/插入吞吐量、内存占用、删除后精度等多个维度
3. **提出 Deletion Control 算法**：根据目标搜索精度 α 动态选择最合适的删除策略

## Method

### 三种删除策略的形式化

给定图 $(\mathcal{P}, \mathcal{N})$，其中 $\mathcal{P} = \{\mathbf{p}_i\}_{i=1}^n \subset \mathbb{R}^d$ 为节点集，$\mathcal{N} = \{\mathcal{N}_i\}_{i=1}^n$ 为邻居集合。删除查询集合为 $\mathcal{D}$。

**Logical Deletion（逻辑删除）**：

- 维护一个标志集合 $\mathcal{F} \subset \{1,...,n\}$，删除时仅更新 $\mathcal{F} \leftarrow \mathcal{F} \cup \mathcal{D}$
- 搜索时从结果中排除被标记节点：$\mathcal{R} \leftarrow \text{SEARCH}(\mathbf{q}, \mathcal{P}, \mathcal{N}) \setminus \mathcal{F}$
- 优点：删除速度极快（~$10^9$ QPS）；缺点：内存线性增长，精度随更新次数递减

**Physical Deletion（物理删除）**：

- 真正移除节点并删除所有连接边：从 $\mathcal{P}$ 中删除节点，从邻居集中删除对应索引
- 具体地，$\mathcal{P} \leftarrow \mathcal{P} \setminus \{\mathbf{p}_i | i \in \mathcal{D}\}$，对剩余节点 $\mathcal{N}_i \leftarrow \mathcal{N}_i \setminus \mathcal{D}$
- 优点：内存最优，精度收敛到稳定值；缺点：删除速度远慢于逻辑删除

**Rebuilding（重建）**：

- 删除指定数据后，用剩余数据重新构建整个图结构：$\mathcal{P} \leftarrow \{\mathbf{p}_i \in \mathcal{P} | i \notin \mathcal{D}\}$，$\mathcal{N} \leftarrow \text{CONSTRUCT}(\mathcal{P})$
- 优点：精度最优，保持图结构最优；缺点：计算开销最大

### Deletion Control 算法

针对需要在持续删除下维持目标搜索精度 $\alpha$ 的场景：

**关键参数估计**：

- $\theta$：仅使用 physical deletion 时 1-Recall@10 的稳定下界
- $\pi$：使用 logical deletion 后，搜索精度保持在 $\alpha$ 以上的最大更新步数，通过线性拟合估计 $\pi \approx (\alpha - R_0) / \Delta$，其中 $\Delta = (R_S - R_0) / S$

**策略选择**：

- 当 $\alpha < \theta$：仅使用 physical deletion（精度不会低于 $\theta > \alpha$）
- 当 $\alpha \geq \theta$：交替使用 logical deletion（$\pi$ 步）+ rebuilding（1 步），在精度即将跌破阈值时通过重建恢复

## Training/Inference

本文不涉及神经网络训练。实验评估流程如下：

- **索引构建**：用前 $n$ 个基向量构建初始 HNSW 索引
- **更新协议**：每步先删除 batch size $b$ 个向量，再插入 $b$ 个新向量（插入的数据始终是新数据，不重复）
- **Ground-truth 重算**：每步更新后对当前索引进行完整搜索重新计算 ground-truth
- **单线程执行**：所有实验在 Intel i7-13700H@2.4GHz, 32GB RAM 上单线程运行

Deletion Control 的参数通过 10% 查询作为 training set 估计，然后在完整查询集上验证。

## Experiments

### 数据集

| 数据集 | 维度 $d$ | 数据量 $n_o$ | 索引大小 $n$ | Batch size $b$ |
|--------|---------|-------------|-------------|----------------|
| SIFT1M | 128 | $10^6$ | $5 \times 10^5$ | $10^5$ |
| GIST1M | 960 | $10^6$ | $5 \times 10^5$ | $10^5$ |
| SIFT1B | 128 | $2 \times 10^6$ | $5 \times 10^5$ | $10^3$ 或 $10^5$ |
| DEEP1M | 96 | $10^6$ | $5 \times 10^5$ | $10^5$ |
| Glove100Angular | 100 | $10^6$ | $5 \times 10^5$ | $10^5$ |

### 评估指标

- **1-Recall@10**：搜索精度
- **QPS-search**：搜索吞吐量
- **QPS-add**：插入吞吐量
- **QPS-delete**：删除吞吐量
- **Memory Usage**：内存占用
- **QPS-Recall curve**：综合搜索性能曲线

## Results

### 搜索精度排序

Rebuilding > Physical Deletion > Logical Deletion（所有数据集一致）

### 删除速度

- Logical deletion 速度最快，约 $10^9$ QPS（~$10^{-4}$ 秒完成 $10^5$ 个删除）
- Physical deletion 和 rebuilding 最高约 $10^3$ QPS

### 精度变化趋势

- Logical deletion：精度随更新步数**线性下降**
- Physical deletion：精度经过多步更新后**收敛到稳定值**（较大 batch size 收敛到更高精度）
- Rebuilding：精度始终保持最优

### 内存管理

- Logical deletion：内存线性增长（已删除数据仍保留在内存中）
- Physical deletion 和 Rebuilding：内存保持不变

### 高维影响

向量维度仅影响 rebuilding 的删除速度（GIST1M 960维 比 SIFT1M 128维 慢），因为重建需要大量距离计算。

### Deletion Control 验证

在 SIFT1B ($b = 10^5$, $\alpha = 0.84$) 上：估计 $\theta = 0.816$, $\pi = 1$。由于 $\alpha > \theta$，选择 logical deletion + rebuilding 交替策略。结果验证该方法基本满足精度要求，且在满足精度的所有策略中**总删除耗时最小**。

## Limitations

- **仅针对 HNSW**：三种删除策略的实验仅在 HNSW 上进行，未验证对其他图基 ANNS 方法（如 DiskANN、NSG）的适用性
- **Workshop paper 篇幅有限**：Deletion Control 的理论分析较为简化，线性拟合 $R_s$ 的假设在极端场景下可能不成立
- **单线程评估**：实际部署中多线程并发执行是常见需求，缺乏并行场景下的评估
- **未考虑混合读写负载**：实验中搜索和更新是分开进行的，未评估并发读写的影响
- **Batch size 固定**：假设每步的删除/插入量相同，实际场景中 workload 可能是不均匀的
- **缺少与现有删除算法的对比**：未直接对比 FreshDiskANN、MN-RU、IPGM 等方法的性能

## My Notes

- **问题意义**：这篇论文抓住了一个容易被忽视但实际上非常重要的问题——ANNS 索引的数据删除评估。随着 RAG 系统的大规模部署，动态数据管理会成为工程中必须面对的问题
- **三种策略的 trade-off 很清晰**：logical 快但牺牲精度和内存；physical 平衡但改变图结构；rebuilding 最优但代价大。这个分类和形式化本身就很有价值
- **Deletion Control 思路简单但实用**：利用训练集估计两个关键参数然后做策略切换，工程上易于实现
- **Physical deletion 的精度收敛现象值得注意**：说明图结构在反复更新后会达到某种"平衡态"，这个发现可以进一步从图论角度分析
- **可扩展方向**：(1) 将评估框架推广至其他 ANN 索引类型（IVF、PQ-based）；(2) 研究边重连策略（如 IPGM）在本框架下的表现；(3) 在线 Deletion Control 的参数自适应调整

## 评分
- 新颖性: ⭐⭐⭐（系统性评估框架是新的，但技术贡献有限）
- 实验充分度: ⭐⭐⭐⭐（5个数据集、6个指标、多 batch size 对比）
- 写作质量: ⭐⭐⭐⭐（形式化清晰，实验分析充分）
- 价值: ⭐⭐⭐⭐（为 ANNS 动态数据管理提供了实用的评估标准和策略选择指导）
