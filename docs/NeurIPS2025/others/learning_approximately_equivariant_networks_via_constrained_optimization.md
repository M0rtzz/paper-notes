---
title: >-
  [论文解读] Learning (Approximately) Equivariant Networks via Constrained Optimization
description: >-
  [NEURIPS2025][equivariance] 提出 Adaptive Constrained Equivariance (ACE)，将等变性训练建模为约束优化问题，通过 homotopy 原理从非等变模型逐步过渡到等变模型，自动平衡下游性能与对称性约束，无需手动调参。
tags:
  - NEURIPS2025
  - equivariance
  - constrained optimization
  - homotopy
  - approximate symmetry
  - neural network training
---

# Learning (Approximately) Equivariant Networks via Constrained Optimization

**会议**: NEURIPS2025  
**arXiv**: [2505.13631](https://arxiv.org/abs/2505.13631)  
**代码**: 待确认  
**领域**: others  
**关键词**: equivariance, constrained optimization, homotopy, approximate symmetry, neural network training  

## 一句话总结

提出 Adaptive Constrained Equivariance (ACE)，将等变性训练建模为约束优化问题，通过 homotopy 原理从非等变模型逐步过渡到等变模型，自动平衡下游性能与对称性约束，无需手动调参。

## Problem

等变神经网络（Equivariant NNs）通过架构强制对称性来提升泛化和样本效率，但存在两个核心挑战：

1. **严格等变性导致优化困难**：等变约束使 loss landscape 变得复杂，即使数据完全满足对称性，训练也容易陷入局部最优，收敛慢且需精细调参。
2. **真实数据的对称性不完美**：噪声、测量偏差、结构变化、动态相变等会破坏对称性（symmetry-breaking effects），严格等变模型无法适应这些 partial symmetries，而完全不约束又浪费了部分对称性信息。

现有的放松等变性方法主要有两类：

- **REMUL**：在训练目标中加等变性违反的惩罚项，通过调节 $\alpha, \beta$ 权重来平衡精度与等变性。但无法保证最终模型的等变程度，超参数敏感。
- **Penn et al.**：对等变层加非等变扰动，按手动设计的 schedule 逐步衰减扰动至零。对 schedule 敏感，还额外引入 Lie 导数惩罚项增加复杂度。

两类方法都依赖人工调参，缺乏自动检测数据对称性违反程度的能力。

## Core Idea

核心思想来自 **homotopy（同伦）原理**与**约束优化中的对偶方法**的联系：

- 先解一个简单问题（非等变模型，参数空间不受限）→ 逐步过渡到目标问题（等变模型）
- 关键洞察：对偶方法本质上就是一种自适应的 homotopy/模拟退火——通过逐步加严的惩罚函数序列求解约束问题

ACE 的做法：

1. 引入逐层调制系数 $\gamma_i$，$\gamma_i = 0$ 时该层等变，$|\gamma_i| > 0$ 时允许偏离
2. 将 $\gamma_i = 0$（或 $|\gamma_i| \leq u_i$）作为**显式优化约束**
3. 用 primal-dual 梯度法自动调节对偶变量 $\lambda_i$，数据驱动地平衡性能与等变性

核心区别：不需要手动设计 penalty weight、衰减 schedule 或 equivariance loss，约束的松紧完全由优化算法根据数据自动决定。

## Method

### Homotopic 架构

将每一层设计为等变分支与非等变分支的线性组合：

$$f_{\theta,\gamma}^i = f_\theta^{\text{eq},i} + \gamma_i \cdot f_\theta^{\text{neq},i}, \quad i=1,\dots,L$$

其中 $f^{\text{eq},i}$ 是等变层（如 SEGNN、EGNN、VN 层），$f^{\text{neq},i}$ 是非等变层（如普通 MLP），$\gamma_i$ 是可学习的标量。$\gamma = 0$ 时整个网络等变。完整网络为 $f_{\theta,\gamma} = f_{\theta,\gamma}^L \circ \cdots \circ f_{\theta,\gamma}^1$。

注意：ACE 框架不依赖特定架构，适用于任何对 $\theta, \gamma$ 可微且 $f_{\theta,0}$ 等变的模型。

### Algorithm 1：严格等变数据（等式约束）

对数据完全满足对称性的场景，训练目标为：

$$\min_{\theta, \gamma} \; \mathbb{E}[\ell_0(f_{\theta,\gamma}(x), y)] \quad \text{s.t.} \quad \gamma_i = 0, \; \forall i$$

通过 Lagrangian 对偶转化为 min-max 问题，得到梯度下降-上升算法：

- **Step 3**（Primal $\theta$）：$\theta^{(t+1)} = \theta^{(t)} - \eta_p \nabla_\theta J_0^{(t)}$
- **Step 4**（Primal $\gamma_i$）：$\gamma_i^{(t+1)} = \gamma_i^{(t)} - \eta_p(\nabla_{\gamma_i} J_0^{(t)} + \lambda_i^{(t)})$
- **Step 5**（Dual $\lambda_i$）：$\lambda_i^{(t+1)} = \lambda_i^{(t)} + \eta_d \gamma_i^{(t)}$

初始化 $\gamma_i = 1$（完全非等变），$\lambda_i = 0$。随着训练进行，如果 $\gamma_i$ 持续为正，$\lambda_i$ 会持续增长，将 $\gamma_i$ 推向零——相当于自适应退火。

### Algorithm 2：部分等变数据（弹性不等式约束）

当数据只部分满足对称性时（如 MoCap 数据），$\gamma_i = 0$ 过于严格，会导致 $\gamma_i$ 振荡不收敛。引入 resilient constraints：

$$\min_{\theta, \gamma, u} \; \mathbb{E}[\ell_0(f_{\theta,\gamma}(x), y)] + \frac{\rho}{2}\|u\|^2 \quad \text{s.t.} \quad |\gamma_i| \leq u_i, \; \forall i$$

slack 变量 $u_i$ 是优化变量（非超参数），自动权衡性能与等变性。理论上 $u_i^\star = \lambda_i^\star / \rho$，即 slack 正比于对偶变量，对偶变量越大说明该层的等变约束越难满足，slack 自动放大。

对偶更新变为 $\lambda_i^{(t+1)} = [\lambda_i^{(t)} + \eta_d(|\gamma_i^{(t)}| - u_i^{(t)})]_+$，投影到非负象限（因为不等式约束）。

### 理论保证

- **Theorem 4.1（近似误差界）**：在 Lipschitz 和有界算子假设下，部署时将 $\gamma$ 置零的误差 $\|f_{\theta,\gamma}(x) - f_{\theta,0}(x)\| \leq [\sum_{k=0}^{L-1}(1+\bar\gamma)^k] \cdot \bar\gamma B M^{L-1} \|x\|$，$\bar\gamma = \max_i |\gamma_i|$ 越小误差越小。
- **Theorem 4.2（等变性误差界）**：$\|\rho_Y(g)f_{\theta,\gamma}(x) - f_{\theta,\gamma}(\rho_X(g)x)\| \leq 2\bar\gamma(M + C\bar\gamma)^{L-1} L B^2 \|x\|$，通过约束 $\gamma$ 可精确控制等变性偏离程度。

## Training/Inference

**训练**：
- 初始化 $\gamma_i = 1$，$\lambda_i = 0$
- 使用 primal-dual 梯度算法（Adam/SGD）交替更新 $\theta, \gamma, \lambda$（及 resilient 版本的 $u$）
- 超参数：primal 学习率 $\eta_p$、dual 学习率 $\eta_d$、$\rho = 1$（固定）
- 额外引入非等变 MLP 层带来一定训练开销，但推理可消除

**推理**：
- 等式约束版本：设 $\gamma = 0$，只使用等变分支 $f^{\text{eq}}$，**无额外推理开销**
- 不等式约束版本：保留 $f^{\text{eq}} + \gamma \cdot f^{\text{neq}}$（$\gamma$ 已很小），利用 partial equivariance

## Experiments

在四个领域、多种等变架构上进行全面实验：

### N-Body Simulations（SEGNN）
| 方法 | Test MSE ($\times 10^{-3}$) |
|------|---------------------------|
| EGNN | 7.1 |
| SEGNN (vanilla) | 5.6 ± 0.25 |
| SEGNN + 松弛 (Penn et al.) | 4.9 ± 0.18 |
| **SEGNN ACE $f^{\text{eq}}$** | **3.8 ± 0.17** |

- 仅用 5000 样本即可匹配 vanilla SEGNN 在 9000 样本上的性能，**数据需求减少约 44%**
- 收敛速度显著快于所有 baseline

### Molecular Property Regression（QM9）
- SchNet + ACE 在全部 12 个量子化学属性上均降低 MAE（如 $U_0$: 9.64 → 3.40）
- SEGNN + ACE 在大多数属性上进一步降低 MAE，说明 ACE 对严格等变架构也能提供额外增益

### 3D Shape Classification（ModelNet40, VN-DGCNN）
- ACE $f^{\text{eq}}$ class accuracy +2.78 pp，instance accuracy +1.77 pp
- 鲁棒性：加入 0-85% 随机点丢弃后，vanilla 模型不收敛，ACE 模型稳定收敛到高准确率

### Motion Capture（CMU MoCap, EGNO）
| 方法 | MSE (Run) | MSE (Walk) |
|------|-----------|------------|
| EGNO (vanilla) | 35.3 ± 3.2 | 8.5 ± 1.0 |
| EGNO ACE† $f^{\text{eq}}+f^{\text{neq}}$ | 32.6 ± 1.6 | 7.5 ± 0.3 |
| **EGNO ACE‡ (resilient)** | **23.8 ± 1.5** | **7.4 ± 0.2** |

弹性不等式约束在 Run 上 MSE 降低约 33%，说明 MoCap 数据的对称性是 partial 的，resilient constraints 能自适应放松。

### $\gamma$ 动力学分析
- **ModelNet40**: $\gamma$ 在训练前 1/3 内迅速衰减至零 → 数据对称性完整
- **MoCap**: $\gamma$ 持续振荡不收敛 → 自动检测到数据对称性违反
- **Slack $u$ 行为**: 早期层获得较大 slack（局部结构主导），后期层保持接近等变；随训练推进所有层约束逐步收紧

## Results

| 关键发现 | 细节 |
|---------|------|
| 收敛加速 | N-Body 上 ACE 显著快于 vanilla SEGNN，早期即达更低 MSE |
| 样本效率 | N-Body 上数据需求减少 ~44% |
| 鲁棒性 | ModelNet40 噪声下 vanilla 不收敛，ACE 稳定高精度 |
| Partial equivariance | MoCap 上弹性约束比严格约束 MSE 降低 ~33%（Run） |
| $\gamma$ 行为诊断 | $\gamma$ 衰减→数据等变；$\gamma$ 振荡→数据对称性不完美 |
| 理论-实验一致 | 弹性模型等变性偏差在训练中稳步降至接近零 |

## Limitations

1. **训练开销**：引入额外非等变 MLP 层，训练速度略降（但推理时等式约束版本无额外开销）
2. **实验范围**：仅在点云、分子、运动轨迹等 3D 数据上验证，未扩展到 2D 图像卷积或 2D 图神经网络（附录 $C_4$ 对称性 toy experiment 初步验证了可行性）
3. **超参数**：虽消除了 penalty weight 和 schedule 调参，但引入了 primal/dual 学习率 $\eta_p, \eta_d$ 和 $\rho$
4. **非等变分支设计**：$f^{\text{neq}}$ 统一用简单 MLP，未探索更优的非等变组件
5. **截断误差**：等式约束版本推理时直接将 $\gamma$ 置零，在 $\gamma$ 未完全收敛时存在截断误差（Theorem 4.1 给出了界）

## My Notes

**方法论亮点**：
- 将 inductive bias（等变性）作为"可协商的约束"而非硬编码，用约束优化框架自动调节——这个思路非常通用，可迁移到其他 structural priors（稀疏性、局部性、因果不变性等）
- Homotopy + constrained optimization 的结合很优雅：从简单问题过渡到困难问题，过渡完全由数据驱动
- 对偶变量 $\lambda_i$ 自然提供了"等变性对性能影响的定量度量"，可用于自动检测对称性违反、指导架构设计

**与相关工作的关键区别**：
- vs REMUL：REMUL 加惩罚项但不保证最终等变性程度；ACE 通过约束提供理论保证
- vs Penn et al.：手动 schedule 衰减 $\gamma$，对 schedule 敏感；ACE 全自动
- vs Residual Pathway Priors：RPP 简单加非等变分支但无约束控制，等变程度不可控

**评分**：
- 新颖性: ★★★★☆ — 约束优化视角处理等变训练新颖，理论与实践结合好
- 实验充分度: ★★★★☆ — 四领域覆盖广，含 ablation 和动力学分析，缺 2D 任务
- 写作质量: ★★★★★ — 动机清晰、理论严谨、图表丰富
- 价值: ★★★★☆ — 通用框架，适配多种等变架构，有实用潜力
