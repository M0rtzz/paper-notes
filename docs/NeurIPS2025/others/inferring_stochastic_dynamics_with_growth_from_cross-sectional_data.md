<!-- 由 src/gen_stubs.py 自动生成 -->
# Inferring Stochastic Dynamics with Growth from Cross-Sectional Data

**会议**: NEURIPS2025  
**arXiv**: [2505.13197](https://arxiv.org/abs/2505.13197)  
**代码**: 待确认  
**领域**: others  
**关键词**: stochastic dynamics, cross-sectional data, Fokker-Planck equation, single-cell RNA-seq, unbalanced optimal transport, score matching, branching diffusion  

## 一句话总结

提出 Unbalanced Probability Flow Inference (UPFI)，通过 Fokker-Planck 方程的 Lagrangian 形式化，从横截面 (cross-sectional) 快照数据中同时推断含细胞增殖/死亡的随机动力学系统中的 drift、noise 和 growth rate。

## Problem

单细胞测序 (scRNA-seq) 等技术本质上是破坏性的——测量会杀死细胞，因此只能获得不同时间点的群体快照 (population snapshots)，而非单个细胞的纵向轨迹。这些群体中，细胞不仅会改变分子状态（drift + noise），还会发生分裂 (division) 和死亡 (death)，使得总细胞数不守恒。

现有方法的主要局限：

- **忽略噪声**：许多方法假设确定性动力学或常数各向同性扩散系数
- **忽略 growth**：大多数方法不建模细胞增殖/死亡，或需要先验信息（如增长率估计、谱系追踪数据）
- **PFI 的局限**：原始 Probability Flow Inference 能处理 intrinsic noise 但不能处理 growth，导致在有增殖的系统中推断出错误的状态转移
- **DeepRUOT 的不稳定性**：多阶段训练流程容易不稳定

## Core Idea

核心洞察：带 growth 的 Fokker-Planck 方程可以在 **Lagrangian 参考系**中被重写为一个 $d+1$ 维的 ODE 系统，从而将求解 $d$ 维 PDE 的问题转化为求解 ODE 的问题。具体地，密度 $\rho_t(\mathbf{x})$ 满足带源项的 FPE：

$$\partial_t \rho_t = -\nabla \cdot [\rho_t \mathbf{v}_t - \nabla \cdot (\rho_t \mathbf{D}_t)] + g_t \rho_t$$

其中 $g_t(\mathbf{x}) = b_t(\mathbf{x}) - d_t(\mathbf{x})$ 为净增长率。通过引入 score function $\nabla \log \rho_t$，可以将扩散项吸收为 transport 项，得到 Lagrangian ODE 系统，同时用额外一维追踪质量变化。

## Method

### 两步训练框架

**Step 1: Score Matching（离线）**

- 使用 denoising score matching 从所有快照数据估计时间依赖的 score function $\mathbf{s}_\phi(t, \mathbf{x}) \approx \nabla \log \rho_t(\mathbf{x})$
- Score 独立于动力学模型参数，因此可以预先计算
- 这一步的计算复杂度为 $\mathcal{O}(Bd)$（$B$ 为 batch size，$d$ 为维度）

**Step 2: ODE 拟合**

- 将观测样本从时间 $t_i$ 推进到 $t_{i+1}$，同时演化位置 $\mathbf{x}$ 和质量 $m$：
  - 位置更新：$\dot{\mathbf{x}}_t = \mathbf{v}_t(\mathbf{x}_t) - \nabla \cdot \mathbf{D}_t(\mathbf{x}_t) - \mathbf{D}_t(\mathbf{x}_t) \mathbf{s}_t(\mathbf{x}_t)$
  - 质量更新：$\dot{m}_t = g_t(\mathbf{x}_t) m_t$
- 构造预测边际分布 $\hat{\rho}_{t_{i+1}} = \sum_k m_{k,t_{i+1}} \delta(\hat{\mathbf{x}}_{k,t_{i+1}} - \mathbf{x})$
- 使用 **unbalanced Sinkhorn divergence** $S_{\varepsilon,\gamma}$ 度量预测与真实分布的差距
- 直接在离散测度上操作，无需计算密度值

### 损失函数与正则化

采用 Wasserstein-Fisher-Rao 能量函数作为正则化，总损失为：

$$L = \sum_{i=1}^K S_{\varepsilon,\gamma}(\hat{\rho}_{t_i}, \rho_{t_i}) + \lambda \int (\|\mathbf{v}_t\|^2 + \alpha |g_t|^2) \, d\rho_t \, dt$$

正则化确保在 drift 和 growth 不可完全辨识时仍有唯一解。

### 理论分析：不可辨识性

论文在 Ornstein-Uhlenbeck (OU) 过程 + 二次 fitness 的线性二次情形下给出精确理论分析：

- **Proposition 2.1**：OU 过程 + 二次 fitness 下密度保持高斯分布，推导出均值、协方差和总质量的 ODE
- **Corollary 2.2**：即使约束 drift 为自治 (autonomous)，对称和反对称部分都可以与 growth 混淆——同一序列的分布可以由不同的 drift + growth 组合产生
- **Theorem 2.3**：在连续时间极限下，正则化的损失函数在线性二次参数空间中有唯一最小值

这些理论结果阐明了"何时可以分离 drift 和 growth"这一根本性问题。

## Training/Inference

- **训练**：两阶段顺序训练（score matching → ODE 拟合），简洁稳定
- **ODE 积分**：实践中 2-3 步 Euler 积分即可满足精度要求
- **Sinkhorn 计算**：每步迭代复杂度 $\mathcal{O}(B^2)$，样本复杂度 $\mathcal{O}(B^{-1/2})$，与维度无关
- **可扩展性**：能处理中等高维数据 (实验中达到 50 维)，适合经过 PCA 降维的 scRNA-seq 数据
- **灵活架构**：可插入可解释性架构如 Neural Graphical Model (NGM)，从中提取基因调控网络

## Experiments

### 1. 高维双稳态系统 (Bistable System)

- 维度 $d \in \{2, 5, 10, 25, 50\}$
- 与 PFI、fitness-ODE、TIGON++、DeepRUOT、OTFM、UOTFM 对比
- **Path energy distance**：UPFI 在所有维度上表现最优或接近最优（如 $d=10$ 时 0.05 vs. 次优 0.29）
- **Fate correlation**：UPFI 始终 $\geq 0.97$，PFI 仅约 0.57-0.65

### 2. 模拟基因调控网络 (CLE Systems)

- 7-gene 分岔系统 + 11-gene 造血干细胞 (HSC) 系统
- 支持 additive 和 multiplicative noise 两种模型
- UPFI 的 fate correlation 达到 0.97-0.98，PFI 仅 0.62-0.66
- 使用 NGM 架构推断基因调控网络：UPFI 的 AUPR 为 0.59-0.64，PFI 为 0.33-0.53

### 3. 真实数据：单核-中性粒细胞发育 (Monocyte-Neutrophil)

- 3 个时间点、10 维 PCA 表示
- 与 RNA velocity 的 cosine similarity：UPFI 与 TIGON++ 可比
- **关键亮点**：lineage tracing 验证下，UPFI 的 fate probability 相关性最高（Pearson 0.26 vs. TIGON++ 0.19，PFI 0.09）
- UPFI 正确预测早期祖细胞具有更高分裂率，符合已知生物学

## Results

| 指标 | UPFI | PFI | fitness-ODE | TIGON++ | DeepRUOT |
|------|------|-----|-------------|---------|----------|
| Path energy (d=10) | **0.05** | 1.03 | 0.29 | 0.61 | 1.32 |
| Fate corr. (d=10) | **0.99** | 0.65 | 0.93 | 0.84 | 0.77 |
| Force cosine (d=10) | **0.10** | 0.12 | 0.37 | 0.35 | 0.45 |
| GRN AUPR (bifurc.) | **0.64** | 0.33 | — | — | — |
| Lineage fate Pearson | **0.26** | 0.09 | -0.02 | 0.19 | — |

核心结论：UPFI 在轨迹重建、向量场恢复、fate 预测和基因调控网络推断上全面优于现有方法。

## Limitations

- **不可辨识性的根本限制**：drift 和 growth 在一般情况下无法完全分离（Corollary 2.2 理论证明），只能通过正则化获得唯一但不一定"正确"的解
- **维度扩展性有限**：实验最高仅到 50 维，依赖 PCA 预处理降维，无法直接处理全基因组高维数据
- **自治性假设**：建议使用 autonomous drift/growth 作为归纳偏置，但真实生物系统中细胞间相互作用和时变环境效应会违反此假设
- **Score 估计质量依赖**：整个方法的精度受限于 Step 1 score matching 的准确性，尤其在高维和低样本情况下
- **Additive vs. Multiplicative noise**：虽然支持 multiplicative noise，但大部分实验使用 additive noise 模型，真实系统中的噪声结构可能更加复杂
- **缺少不确定性量化**：未提供推断结果的置信区间或后验分布

## My Notes

**方法论亮点**：

- 将 FPE 的 Lagrangian 重写与 unbalanced OT 结合的思路非常优雅，避免了直接在高维空间计算密度值的困难
- 两步训练方案（score matching + ODE fitting）比 DeepRUOT 的多阶段训练简洁得多，且 score 的学习与动力学参数解耦，有利于稳定训练
- 线性二次情形下的完整理论分析（不可辨识性 + 正则化唯一性）为理解方法的能力边界提供了宝贵的理论基础

**潜在扩展方向**：

- 结合 lineage tracing 数据作为额外约束可能部分缓解不可辨识性问题
- 可以考虑将 score matching 替换为更现代的 flow matching 作为第一步
- Neural Graphical Model 的集成展示了方法的灵活性，可进一步引入其他可解释架构来编码生物先验知识
- 扩展到空间转录组学数据，处理空间依赖的 growth rate

**评价**：理论与实验结合紧密，问题有明确的生物学动机，方法设计简洁有效。在计算生物学/单细胞分析领域是一项有意义的贡献。

## 评分
- 新颖性: ⭐⭐⭐⭐ — Lagrangian 重写 + unbalanced Sinkhorn 的组合在该领域是新颖的
- 实验充分度: ⭐⭐⭐⭐ — 模拟 (多维度) + 真实数据 + 多 baseline 对比 + 理论验证
- 写作质量: ⭐⭐⭐⭐⭐ — 理论推导清晰，动机阐述充分，图表质量高
- 价值: ⭐⭐⭐⭐ — 对单细胞动力学推断领域有实际推动作用
