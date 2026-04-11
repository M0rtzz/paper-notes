# Hybrid-Balance GFlowNet for Solving Vehicle Routing Problems

**会议**: NeurIPS 2025  
**arXiv**: [2510.04792](https://arxiv.org/abs/2510.04792)  
**代码**: [GitHub](https://github.com/ZHANG-NI/HBG)  
**领域**: others  
**关键词**: GFlowNet, Vehicle Routing Problem, Combinatorial Optimization, Trajectory Balance, Detailed Balance

## 一句话总结

提出 Hybrid-Balance GFlowNet (HBG) 框架，在 VRP 求解中首次引入并形式化 Detailed Balance，将其与 Trajectory Balance 统一整合实现局部-全局联合优化，并设计 depot-guided inference 策略，在 CVRP 和 TSP 上一致提升现有 GFlowNet 求解器的性能。

---

## Problem

Vehicle Routing Problems (VRP) 是物流与运输中的核心组合优化问题。现有基于 GFlowNet 的 VRP 求解方法（AGFN、GFACS）只使用 **Trajectory Balance (TB)** 进行全局优化训练，存在两个关键缺陷：

1. **局部信号被全局淹没**：TB 以整条轨迹的总代价作为 reward 并按比例分配给所有 transition。若一条长轨迹的整体代价很高（如前段出现差决策），即使后段存在高质量的局部决策（如 W→X→Y），这些好决策也会收到弱甚至误导性的训练信号。
2. **无法保留局部好模式**：TB 缺乏 step 级别评估单个 transition 优劣的能力，无法在全局次优轨迹中识别和保护有价值的局部路径模式。

另一方面，**Detailed Balance (DB)** 可以提供 step-wise 精细反馈，但单独使用 DB 不能捕捉 VRP 全局约束（总距离最小化、车辆容量限制等），也不够。

因此需要一种同时兼顾全局轨迹结构和局部转移质量的统一方法。

---

## Core Idea

**Hybrid-Balance 原则**：将 TB（全局优化）和 DB（局部优化）以理论一致的方式统一整合。核心洞察在于 TB 和 DB 具有**内在互补性**：

- TB 负责 holistic trajectory optimization，确保整体路径质量
- DB 负责 fine-grained local refinement，提供 step 级别的精确反馈

二者结合能让模型同时学习全局路径规划能力和局部节点选择能力。

---

## Method

### 1. 建模基础

- **问题定义**：CVRP 在完全图 $\mathcal{G} = (\mathcal{V}, \mathcal{U})$ 上，$\mathcal{V} = \{v_0, v_1, \ldots, v_n\}$，$v_0$ 是 depot，其余为 customer。每条边有欧氏距离代价，每个 customer 有需求量，车辆有容量上限。目标是找到一组从 depot 出发并返回的路线，使每个 customer 恰好被访问一次，总路程最小。
- **State** $s_t^i$：轨迹 $\tau_i$ 中决策步 $t$ 时已访问节点序列 $\{x_0^i, x_1^i, \ldots, x_t^i\}$
- **Action** $a_t^i$：从未访问节点中选择下一个节点（需满足容量约束）
- **Reward**：双层设计——轨迹级 $R(\tau_i) = \sum_{k=0}^{m-1} d(x_k^i, x_{k+1}^i)$ 和状态级 $R(s_t^i) = d(x_{t-1}^i, x_t^i)$
- **GNN 编码**：将完全图稀疏化为 k-NN 图，通过多层 GNN 获得节点和边嵌入，边嵌入经 MLP 生成边概率分布 $\eta(\mathcal{G}^*, \theta)$，节点嵌入用于计算 state flow

### 2. TB 全局优化（原有部分）

AGFN 和 GFACS 都采用 TB loss 进行训练：

$$\ell_{\text{TB}}^{\text{AG}}(\mathcal{T}; \theta) = \frac{1}{h}\sum_{k=1}^{h}\left(\log \frac{Z(\theta) \cdot P_F(\tau_k; \theta)}{\widetilde{R}(\tau_k) \cdot P_B(\tau_k)}\right)^2$$

其中 $Z$ 是 source flow，$P_F$ 是前向概率（所有 step 前向概率之积），$P_B$ 是后向概率，$\widetilde{R}$ 是（可能经过 discriminator 增强的）reward。

### 3. DB 局部优化（本文核心贡献）

本文首次在 VRP 场景下引入并形式化 DB。对相邻状态 $(s_t^i, s_{t+1}^i)$，DB loss 采用 forward-looking 技术：

$$\ell_{\text{DB}}(s_t^i, s_{t+1}^i; \theta) = \left(\log \frac{P_f(s_{t+1}^i | s_t^i; \theta) \cdot F(s_t^i; \theta) \cdot \exp(\tilde{\mathcal{E}}(s_{t+1}^i))}{P_b(s_t^i | s_{t+1}^i) \cdot F(s_{t+1}^i; \theta) \cdot \exp(\tilde{\mathcal{E}}(s_t^i))}\right)^2$$

关键组件设计：

- **后向概率** $P_b$：基于子轨迹 backward destruction 的排列计数分析。假设完整轨迹由 $a$ 条多节点子轨迹和 $j$ 条单节点子轨迹组成，排列计数的闭合形式为 $B(\mathcal{A}_a, \mathcal{J}_j) = (a+j)! \cdot 2^a$。由此 depot 节点处 $P_b = \frac{1}{2a+j}$（多节点子轨迹有 2 种拆解方向），其余节点 $P_b = 1$（唯一前驱）。
- **State flow** $F(s_t^i; \theta)$：对当前状态中所有已访问节点的 GNN 嵌入取平均，再经双层 MLP + ReLU 计算 $F(s_t^i; \theta) = \frac{1}{t}\sum_{x_k \in s_t^i}(W_2 \cdot \text{ReLU}(W_1 \cdot q_k + b_1) + b_2)$。
- **Energy** $\tilde{\mathcal{E}}(s_t^i)$：使用 relative advantage 形式 $\tilde{\mathcal{E}}(s_t^i) = R(s_t^i) - \frac{1}{h}\sum_{k=1}^h R(s_t^k)$，捕捉当前状态相对于同一 batch 内其它轨迹同步状态的相对优势。随训练推进 reward variance 减小，energy 值自然增长。

### 4. Hybrid-Balance 统一目标

最终训练目标直接将 TB 和 DB loss 相加：

$$\ell_{\text{HB}}(\mathcal{T}; \theta) = \sum_{i=1}^h \left(\ell_{\text{TB}}(\tau_i; \theta) + \ell_{\text{DB}}(\tau_i; \theta)\right)$$

其中 $\ell_{\text{DB}}(\tau_i; \theta) = \sum_{t=0}^{m-1} \ell_{\text{DB}}(s_t^i, s_{t+1}^i; \theta)$，整条轨迹的 DB loss 为所有相邻状态对的 DB loss 之和。

### 5. Depot-Guided Inference

基于后向策略分析的关键发现：depot 是唯一在轨迹构建中保有多候选选择灵活性的节点。据此设计推理策略：

$$x_{t+1} = \begin{cases} x \sim P_f(s_{t+1} | s_t; \theta) & \text{当前节点是 depot（sampling 保持探索）} \\ \arg\max P_f(s_{t+1} | s_t; \theta) & \text{当前节点是 customer（greedy 选最优）} \end{cases}$$

该策略仅适用于有 depot 的问题（如 CVRP）；对于无 depot 的 TSP，保留原有推理方式（AGFN 用 hybrid decoding，GFACS 用 ant colony search）。

---

## Training/Inference

- **训练设置**：在 100 节点 CVRP/TSP 实例上训练，使用 sampling-based decoding，每个实例生成 $\mathcal{N}=20$ 条路线
- **推理方式**：AGFN 用 depot-guided inference，GFACS 用 ant colony search + depot-guided node selection
- **硬件**：NVIDIA A100 GPU + Intel Xeon 6342 CPU
- **框架适配**：HBG 是即插即用模块，分别集成到 AGFN（construction-based）和 GFACS（improvement-based + ACO）
- **推理开销极低**：仅增加 0.01–0.04 秒（来自临时加载 flow 参数），不影响整体效率

---

## Experiments

### CVRP 主实验

在 CVRP200/500/1000 上评估（每个规模 128 个合成实例），以 LKH 为参考基准：

| 方法 | CVRP200 Gap(%) | CVRP500 Gap(%) | CVRP1000 Gap(%) |
|------|---------------|----------------|-----------------|
| AGFN | 11.48 | 12.21 | 11.15 |
| **HBG-AGFN** | **9.95** | **10.44** | **9.34** |
| GFACS | 23.11 | 23.83 | 23.82 |
| **HBG-GFACS** | **16.48** | **13.53** | **10.61** |
| GFACS (LS) | 2.10 | 3.03 | 3.00 |
| **HBG-GFACS (LS)** | **1.96** | **2.81** | **2.75** |

HBG 在所有规模上一致提升 AGFN 和 GFACS，gap 降幅最高达 55.46%（GFACS CVRP1000）。

### TSP 泛化实验

TSP200/500/1000 上评估（无 depot-guided inference）：

| 方法 | TSP200 Gap(%) | TSP500 Gap(%) | TSP1000 Gap(%) |
|------|--------------|---------------|----------------|
| AGFN | 11.58 | 17.06 | 19.71 |
| **HBG-AGFN** | **10.45** | **14.05** | **18.47** |
| GFACS (LS) | 1.51 | 4.91 | 7.80 |
| **HBG-GFACS (LS)** | **1.50** | **4.60** | **7.67** |

即使没有 depot-guided inference，HB 模块本身仍能带来一致提升，最大降幅 17.64%。

### Ablation Study

**TB vs DB vs HB 对比**：

| 方法 | GFACS CVRP200 Gap | GFACS CVRP500 Gap | GFACS CVRP1000 Gap |
|------|-------------------|-------------------|--------------------|
| DB only | 54.36% | 48.77% | 50.89% |
| TB only | 23.11% | 23.83% | 23.82% |
| **HB** | **21.29%** | **21.08%** | **19.87%** |

- 单独 DB 效果非常差（全局约束缺失），验证了单独使用 DB 的不足
- HB 统一后稳定优于 TB，最多降低 gap 16.58%

**Depot-Guided Inference 变体**（DG=depot greedy, DS=depot sampling, CG=customer greedy, CS=customer sampling）：

| 变体 | AGFN CVRP1000 Gap | GFACS CVRP1000 Gap |
|------|-------------------|---------------------|
| DG + CS | 21.25% | 23.23% |
| DG + CG | 10.61% | 12.28% |
| DS + CS | 20.09% | 19.02% |
| **DS + CG** | **9.34%** | **10.61%** |

DS+CG（depot sampling + customer greedy）是最优组合，验证了 depot 需要保持探索多样性、customer 适合贪心选择的设计直觉。

---

## Results

- HBG 在所有规模的 CVRP 和 TSP 上**一致性提升**两个不同类型的 GFlowNet 求解器
- 在 GFACS 上提升最显著：CVRP1000 gap 从 23.82% 降至 10.61%（降幅超 55%）
- 随问题规模增大提升越明显，显示出良好的可扩展性
- 推理几乎无额外开销（0.01–0.04s）
- 超越 POMO、ACO、NeuOpt、GANCO 等多种基线方法

---

## Limitations

1. **依赖底层求解器**：HBG 是增强框架，性能上界受限于所集成的 GFlowNet 基础模型质量
2. **Depot-guided inference 限于有 depot 的问题**：对 TSP 等无 depot 问题无法使用该推理策略，只能依赖 HB 模块本身
3. **TB+DB 简单等权相加**：未探索自适应加权或更精细的融合策略（如 curriculum learning）
4. **仅在合成数据集上大规模验证**：虽提到 CVRPLib 真实基准，但主实验均为合成实例
5. **VRP 变体覆盖有限**：仅验证 CVRP 和 TSP，未扩展到 VRPTW、PDVRP 等更多变体

---

## My Notes

**值得关注的点：**

- TB 和 DB 在 GFlowNet 中的互补性分析清晰有力——TB 适合全局但局部信号弱，DB 适合局部但缺全局视角。该 insight 可推广到其它长 horizon 组合优化问题。
- 后向概率推导是技术上最有趣的部分：子轨迹 backward destruction counting 给出 $P_b = \frac{1}{2a+j}$ 的闭合形式，多节点子轨迹有 2 种拆解方向 × 排列数的乘积。
- Depot-guided inference 的动机来自后向策略分析，depot 作为"枢纽"天然具备更多选择权——sampling 保持探索、customer 用 greedy 避免噪声，简单但有效。
- Energy 用 relative advantage（减去同 batch 均值）是巧妙设计：随训练进行 reward variance 减小 → energy 自然增长，无需手动 schedule。
- 作为即插即用框架同时适配 construction-based 和 improvement-based 两类求解器，增强了实用价值。

**潜在改进方向：**

- 探索 TB 和 DB 之间的自适应权重调度（如从 TB-dominant 逐步过渡到 balanced）
- 将 HBG 扩展到更多 VRP 变体（VRPTW、PDVRP）和更大规模实例
- 结合 Sub-Trajectory Balance (SubTB) 等中间粒度的 balance 策略

## 评分

- 新颖性: ⭐⭐⭐⭐ — 首次在 VRP 场景引入并形式化 DB，TB+DB 统一框架有理论贡献
- 实验充分度: ⭐⭐⭐⭐ — 多规模、多基线、充分的 ablation，但缺少更多 VRP 变体
- 写作质量: ⭐⭐⭐⭐ — 动机清晰、理论推导完整、图示直观
- 价值: ⭐⭐⭐⭐ — 即插即用框架、一致性提升，对 GFlowNet+CO 社区有参考价值
