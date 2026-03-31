# Flattening Hierarchies with Policy Bootstrapping

**会议**: NeurIPS 2025  
**arXiv**: [2505.14975](https://arxiv.org/abs/2505.14975)  
**代码**: [SAW](https://johnlyzhou.github.io/saw/)  
**领域**: image_generation  
**关键词**: offline GCRL, hierarchical RL, policy bootstrapping, subgoal, long-horizon control  

## 一句话总结

提出 Subgoal Advantage-Weighted Policy Bootstrapping（SAW），通过优势加权的重要性采样对子目标条件策略进行 bootstrapping，将层级 RL 的长距离推理能力蒸馏到一个扁平策略中，无需生成式子目标模型。

## 研究动机

离线目标条件强化学习（Offline GCRL）被视为预训练通用策略的有前途范式，但面临长距离推理的核心挑战：

- **稀疏奖励 + 折扣**：远距离目标的原始动作优势信号极弱（action gap 现象）
- **层级 RL（HRL）**方法效果好但引入巨大复杂性：
  - 需要学习子目标生成模型——在高维状态空间中这是困难的生成建模问题
  - 模块化架构固定于特定时间抽象层级，阻碍统一表示
  - 子目标表示学习的目标函数选择仍是开放问题

**核心问题**：能否将层级方法的优势提炼到一个简单的扁平策略中？

## 方法详解

### 对层级 RL 优势的深层分析

以 HIQL（当前 SOTA）为研究对象，发现层级方法的成功源于两个因素：

1. **值函数信噪比改善**：低层策略评估动作对近距离子目标的优势，信号更清晰
2. **更容易采样高优势样本**：数据集动作对轨迹中短距离未来状态天然具有高优势，而对远距离目标则很少有高优势动作

层级方法的推理可视为**测试时策略 bootstrapping**：用高层策略预测子目标，用低层策略的子目标条件分布近似全目标条件策略。

### RL 作为概率推断框架

引入子目标最优性变量 $U$，似然函数为：

$$p(U=1 \mid \tau, \{w\}, g) \propto \exp\left(\beta \sum_{t=0}^{\infty} \gamma^t A(s_t, w_t, g)\right)$$

其中子目标优势 $A(s_t, w, g) = V(w, g) - V(s_t, g)$（到 $w$ 的进展度量）。

考虑因式化层级策略形式，并引入扁平后验 $q^f(\tau \mid g)$ 和子目标后验 $q^h(\{w\} \mid g)$，构造 ELBO：

$$\mathcal{J}(q, \pi) = \mathbb{E}_{\mu(s), p(g)}\left[\mathbb{E}_{q^h(w|s,g)}[A(s,w,g)] - \mathbb{E}_{q^h}[D_{\text{KL}}(q^f \| \pi^\ell)] - \mathbb{E}_{q^f}[D_{\text{KL}}(q^h \| \pi^h)]\right]$$

### 消除子目标生成模型

关键洞察：用 Bayes 规则重写最优子目标后验：

$$p(w \mid s, g, U=1) \propto p^{\mathcal{D}}(w \mid s) \exp(A(s, w, g))$$

这意味着不需要学习子目标生成模型 $\pi^h$，直接从数据集轨迹中采样子目标，用优势函数加权即可。

### SAW 目标函数

$$\mathcal{J}(\theta) = \mathbb{E}_{p^{\mathcal{D}}(s,a,w), p(g)}\left[e^{\alpha A(s,a,g)} \log \pi_\theta(a \mid s, g) - e^{\beta A(s,w,g)} D_{\text{KL}}(\pi_\theta(a \mid s, g) \| \pi^{\text{sub}}(a \mid s, w))\right]$$

包含两个互补项：
- **一步 AWR 项**：直接从值函数获取学习信号，适合需要 stitching 的环境
- **策略 bootstrapping 项**：从子策略 $\pi^{\text{sub}}$ bootstrap，由子目标优势加权

动态平衡：目标越远，动作优势差异越小，自动减弱噪声较大的值函数信号，增大 bootstrapping 权重。

### 训练流程

1. 训练值函数 $V_\phi$（GCIVL，期望值回归避免 OOD 动作高估）
2. 训练目标子策略 $\pi^{\text{sub}}$（AWR，仅在近距离目标上）
3. 训练扁平策略 $\pi_\theta$（SAW 目标，综合一步和 bootstrapping 信号）

## 实验结果

### OGBench 20 个数据集、7 个环境、100 个评估任务

| 环境 | GCIVL | CRL | HIQL | RIS_off | **SAW** |
|------|-------|-----|------|---------|---------|
| antmaze-medium | 72 | 95 | 96 | 96 | **97** |
| antmaze-large | 16 | 83 | 91 | 89 | **90** |
| antmaze-giant | 0 | 16 | 65 | 65 | **73** |
| humanoidmaze-medium | 24 | 60 | **89** | 73 | **88** |
| humanoidmaze-large | 2 | 24 | **49** | 21 | 46 |
| humanoidmaze-giant | 0 | 3 | 12 | 3 | **35** |
| cube-single | 53 | 19 | 44 | 81 | 72 |
| scene-play | 42 | 19 | 38 | **64** | **63** |

### 关键发现

- **humanoidmaze-giant**：SAW 是唯一达到非平凡成功率的方法（35% vs HIQL 12%），69 维状态空间+21 DoF 下长距离导航
- 层级方法的子目标表示在高维大状态空间中**退化**（Figure 3）：HIQL 的子目标表示在 giant maze 上严重限制性能，而 SAW 直接在观测空间操作避免了此问题
- 视觉任务（64×64 像素观测）中 SAW 同样保持 SOTA 或接近 SOTA 性能

### 统一理论视角

SAW 的推导自然恢复了三种现有方法作为特殊情况：
- HIQL：因式化后验 + 分层训练
- RIS：学习子目标生成器 + 扁平策略回归
- one-step AWR：$\beta = 0$ 时退化为标准策略提取

## 评价

⭐⭐⭐⭐

**优点**：
- 理论推导清晰优雅，统一框架自然恢复 HIQL、RIS 等方法
- 消除子目标生成模型是实质性简化，避免了高维生成建模的困难
- 在最具挑战的 humanoidmaze-giant 上实现突破性进展（35% vs 12%）
- 实验覆盖 20 个数据集/100 个任务，包含状态和视觉两种观测空间

**局限**：
- 子目标仅从数据集轨迹采样，在高度需要 stitching 的 explore 数据集上性能下降
- 值函数训练在超长距离视觉任务（visual-antmaze-giant）上仍会发散
- 仍然依赖 IQL-style 值学习，继承了期望值回归的固有偏差
- 价值: 待评
