# Graph Distance as Surprise: Free Energy Minimization in Knowledge Graph Reasoning

**会议**: NeurIPS 2025 (NORA Workshop)  
**arXiv**: [2512.01878](https://arxiv.org/abs/2512.01878)  
**代码**: 无  
**领域**: Knowledge Graphs / Active Inference  
**关键词**: Knowledge Graphs, Graph Neural Networks, Active Inference, Free Energy Principle, Semantic Grounding  

## 一句话总结

将神经科学中的 Free Energy Principle (FEP) 引入知识图谱推理，提出用图的最短路径距离（graph distance）作为 surprise 的度量，为 KG-based agent 的 entity grounding 提供理论框架。

## Problem

知识图谱（Knowledge Graph, KG）在现代 AI agent 中被广泛使用，用于增强推理、记忆和规划能力。然而，当 agent 需要基于 KG 进行推理时，一个核心问题是：**给定 KG 作为 agent 的生成模型（generative model），在特定上下文中哪些 entity grounding 是合理的？** 目前缺乏一个有原则的理论框架来衡量 KG 中实体的"可信度"或"合理性"。

Murphy et al. 此前的工作证明了句法操作（syntactic operations）通过浅层树结构来最小化 surprise 和 free energy，但该框架局限于树结构，无法处理 KG 中常见的有向图、环路（cycles）和多路径等复杂拓扑。

## Core Idea

核心思想非常直觉：**在 KG 中，距离上下文越近的实体越不令人惊讶（less surprising），距离越远的实体越令人惊讶。** 这将 FEP 的 surprise minimization 概念与图的最短路径距离直接联系起来。

具体而言：
- KG 充当 agent 的 **generative model**
- 图距离（graph distance）作为 **surprise** 的代理指标
- entity grounding 的合理性与图距离**成反比**
- 该框架是 Murphy et al. 树结构 surprise 度量的**推广**：对于树结构，图距离退化为树深度，恢复原有结论

## Method

### 形式化定义

给定知识图谱 $\mathcal{G} = (\mathcal{E}, \mathcal{R}, \mathcal{T})$，其中 $\mathcal{E}$ 为实体集合，$\mathcal{R}$ 为关系集合，$\mathcal{T} \subseteq \mathcal{E} \times \mathcal{R} \times \mathcal{E}$ 为三元组集合。

**Geometric Surprise** 定义为：

$$S_{\text{geo}}(e \mid C) = \begin{cases} \min_{c \in C} d_{\mathcal{G}}(c, e) & \text{if path exists} \\ \alpha & \text{otherwise} \end{cases}$$

其中 $d_{\mathcal{G}}(c, e)$ 是从上下文 $c \in C$ 到实体 $e$ 的最短有向路径长度（通过 BFS 计算），$\alpha$ 是惩罚断开连接的超参数（应大于图的直径）。

### Free Energy 组合公式

结合 algorithmic complexity：

$$F(e \mid C) = S_{\text{geo}}(e \mid C) + \lambda K(\pi_{C \to e})$$

其中 $K(\pi_{C \to e})$ 是关系路径的 Kolmogorov complexity（通过 Lempel-Ziv 压缩近似），$\lambda$ 为权重参数。

### 与 FEP 的连接

在 FEP 框架下，agent 最小化 variational free energy $F = -\log P(o,s) - H[Q(s)]$。本文的映射关系为：
- $-\log P(e \mid C) \propto d_{\mathcal{G}}(C, e)$：距离越短→概率越高→surprise 越低
- $S_{\text{geo}}$ 实现 surprise 项
- $K(\pi)$ 近似 $H[Q(s)]$ 项

### 环路处理

与树结构不同，KG 可能包含环路。BFS 通过 visited set 自然处理环路，保证终止性和正确性。FEP 本身也容纳循环因果关系（circular causality）。

### 理论依据

三个原则支撑最短路径距离的合理性：
1. **Proper generalization**：对树结构退化为树深度
2. **Least-action principle**：最短路径最小化累积代价，与 active inference 的 expected free energy 最小化一致
3. **Computational grounding**：GNN 中 $k$ 次 message passing 聚合 $k$-hop 邻域，最小化迭代次数即最小化距离和 surprise

## Training/Inference

本文为**理论框架论文**，不涉及模型训练。推理流程如下：

1. **构建 KG**：定义实体、关系和三元组
2. **确定上下文** $C$：根据查询确定上下文实体集合
3. **BFS 计算距离**：从上下文实体出发，BFS 计算到所有候选实体的最短路径，时间复杂度 $O(|\mathcal{E}| + |\mathcal{T}|)$
4. **计算 Kolmogorov complexity**：提取关系路径序列，通过 LZ77 压缩计算压缩比
5. **组合 Free Energy**：$F = S_{\text{geo}} + \lambda K(\pi)$
6. **排序**：按 free energy 从低到高排序候选实体，低 free energy 意味着高合理性

## Experiments

### Worked Example

论文使用加拿大政治知识图谱作为示例：
- **实体**：Canada, Trudeau, Harper, PrimeMinister, Biden
- **查询**："Who is the Prime Minister?" 上下文 $C = \{\text{Canada}\}$
- **设置**：$\alpha = 5$，$\lambda = 1$

### Results

| Entity | $S_{\text{geo}}$ | $K(\pi)$ | $F$ |
|--------|:-:|:-:|:-:|
| Trudeau | 1 | Low | ~1.3 |
| Harper | 1 | Low | ~1.3 |
| Biden | 5 | High | ~5.5 |

- Trudeau 和 Harper（都是加拿大 PM）具有低 free energy（1 hop 直接连接 + 规则关系模式）
- Biden（美国总统）具有高 free energy（无路径连接 + 不规则模式）
- PrimeMinister 节点距离为 2，$F \approx 2.3$，但作为抽象角色节点不是直接答案

### 关键验证

示例验证了三个关键性质：
1. **环路自然处理**：Trudeau ↔ Harper 的 successor/predecessor 关系构成环路，BFS 正确处理
2. **多个有效答案共存**：Trudeau 和 Harper 具有相同的 surprise
3. **断开实体正确惩罚**：Biden 因无路径连接而获得最高 surprise

## Limitations

1. **仅为 work-in-progress**：论文自述为初步探索性工作，缺乏大规模实验验证
2. **无 benchmark 实验**：没有在 FB15k-237、YAGO 等标准 KG 数据集上进行定量评估
3. **仅有 toy example**：加拿大 PM 示例过于简单，无法验证框架在复杂 KG 上的可扩展性
4. **Kolmogorov complexity 近似粗糙**：LZ 压缩对短序列的近似质量存疑
5. **未考虑关系类型权重**：所有关系等权处理，实际 KG 中不同关系的重要性差异很大
6. **未与 embedding-based 方法比较**：如 TransE、RotatE 等已有成熟的 KG 推理方法
7. **scalability 不明**：BFS 在超大规模 KG（百万节点）上的效率未讨论
8. **$\alpha$ 和 $\lambda$ 超参数选择**：缺乏系统的调参策略

## My Notes

**论文定位**：这是一篇发表在 NeurIPS 2025 NORA Workshop 的 position/theoretical paper，提出了一个将 FEP 与 KG 推理连接的概念框架。核心贡献在于**理论视角的新颖性**，而非实验验证。

**优点**：
- 跨学科视角有趣：将神经科学的 FEP 与 KG 推理联系起来
- 数学形式化清晰，从 surprise 定义到 free energy 组合公式逻辑自洽
- 对 GNN message passing 深度的理论解释有启发价值
- 将 Murphy et al. 的树结构结论推广到一般有向图

**不足**：
- 作为 workshop paper，深度和完整度有限
- "图距离越近越合理" 本身是一个相当直觉的观点，FEP 的包装增加了理论装饰但实质贡献有限
- 缺乏与现有 KG reasoning 方法（如 embedding-based、path-based）的实验对比

**潜在应用方向**：
- LLM-KG 系统中的 entity grounding 排序
- GNN 架构设计中 message passing 深度的理论指导
- KG embedding 训练中保留距离结构的正则化

**分类说明**：此论文被归类到 image_generation 可能是分类错误，其实际领域应为 Knowledge Graphs / Neuro-symbolic AI。

## 评分
- 新颖性: ⭐⭐⭐ (FEP + KG 的跨学科连接有新意，但核心 insight 较直觉)
- 实验充分度: ⭐ (仅 toy example，无定量实验)
- 写作质量: ⭐⭐⭐⭐ (数学推导清晰，结构完整)
- 价值: ⭐⭐ (理论探索性质，实际影响有限)
