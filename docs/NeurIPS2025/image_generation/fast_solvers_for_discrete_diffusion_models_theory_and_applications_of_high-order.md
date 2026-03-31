# Fast Solvers for Discrete Diffusion Models: Theory and Applications of High-Order Algorithms

**会议**: NeurIPS 2025  
**arXiv**: [2502.00234](https://arxiv.org/abs/2502.00234)  
**代码**: [DiscreteFastSolver](https://github.com/yuchen-zhu-zyc/DiscreteFastSolver)  
**领域**: image_generation  
**关键词**: discrete diffusion, high-order solver, τ-leaping, Trapezoidal method, text generation, image generation  

## 一句话总结

为离散扩散模型推理首次提出高阶数值求解器（θ-RK-2 和 θ-Trapezoidal），在 KL 散度意义下证明二阶收敛，在文本和图像生成任务上以同等计算预算获得更好的样本质量。

## 研究动机

离散扩散模型在文本、图像、分子等离散数据生成中取得了重要进展，但推理效率是核心瓶颈：

- **精确仿真方法**（如 uniformization、First-Hitting Sampler）：无偏但推理时间不可预测，跳跃次数分布高度偏斜，终端阶段大量冗余计算
- **近似方法**（如 τ-leaping）：简单可并行，但仅有一阶精度，需要极小步长才能控制误差
- 连续扩散模型已有 DPM-Solver、DDIM 等高阶加速方法，但离散领域尚为空白

## 方法详解

### 背景：离散扩散与 τ-leaping

离散扩散模型定义在有限状态空间 $\mathbb{X} = [S]^d$ 上的连续时间 Markov 链。前向过程满足：

$$\frac{d\mathbf{p}_t}{dt} = \mathbf{Q}_t \mathbf{p}_t$$

反向过程通过学习的 score 函数 $\hat{\mathbf{s}}_t$ 近似。τ-leaping（一阶 Euler 方法）的更新：

$$\hat{y}_{t+\Delta} = \hat{y}_t + \sum_{\nu \in \mathbb{D}} \nu \, \mathcal{P}(\hat{\mu}_t(\nu) \Delta)$$

其离散化误差为 $\mathcal{O}(\kappa T)$（一阶），$\kappa$ 为最大步长。

### θ-RK-2 方法

类比 ODE 的二阶 Runge-Kutta，分两阶段：

1. **预测步**：以 τ-leaping 走 $\theta\Delta$ 步得到中间状态 $\hat{y}_{\rho_n}^*$
2. **校正步**：用当前和中间点的强度加权和走完整步

$$\hat{y}_{s_{n+1}} = \hat{y}_{s_n} + \sum_{\nu} \nu \, \mathcal{P}\left(\mathbf{1}_{\hat{\mu}_{s_n}>0}\left[(1-\frac{1}{2\theta})\hat{\mu}_{s_n} + \frac{1}{2\theta}\hat{\mu}_{\rho_n}^*\right]_+(\nu)\Delta_n\right)$$

- 二阶收敛仅在 $\theta \in (0, 1/2]$ 时成立（条件性二阶）

### θ-Trapezoidal 方法（核心贡献）

改进 θ-RK-2 的第二步设计：

1. **预测步**：与 θ-RK-2 相同
2. **校正步**：从中间状态 $\hat{y}_{\rho_n}^*$ 出发，走 $(1-\theta)\Delta_n$ 步，使用外推系数：

$$\hat{y}_{s_{n+1}} = \hat{y}_{\rho_n}^* + \sum_{\nu} \nu \, \mathcal{P}\left((\alpha_1 \hat{\mu}_{\rho_n}^* - \alpha_2 \hat{\mu}_{s_n})_+(\nu)(1-\theta)\Delta_n\right)$$

其中 $\alpha_1 = \frac{1}{2\theta(1-\theta)}$，$\alpha_2 = \frac{(1-\theta)^2 + \theta^2}{2\theta(1-\theta)}$，满足 $\alpha_1 - \alpha_2 = 1$。

### 理论保证

**定理（θ-Trapezoidal 二阶收敛）**：在正则性假设下，

$$D_{\text{KL}}(p_\delta \| \hat{q}_{T-\delta}^{\text{trap}}) \lesssim \exp(-T) + (\epsilon_I + \epsilon_{II})T + \kappa^2 T$$

关键改进：离散化误差从 τ-leaping 的 $\mathcal{O}(\kappa T)$ 提升到 $\mathcal{O}(\kappa^2 T)$，且对 $\theta \in (0,1]$ **无条件成立**，鲁棒性优于 θ-RK-2。

## 实验结果

### 15-State 玩具模型

- θ-Trapezoidal 在 KL 散度上呈现清晰的二次收敛（与理论一致）
- 绝对值和收敛速率均优于 θ-RK-2

### 文本生成（RADD/GPT-2 级别，d=1024, S=50258）

| 方法 | NFE=128 | NFE=1024 |
|------|---------|----------|
| FHS | 122.7 | 109.4 |
| Euler | 86.3 | 44.7 |
| τ-leaping | 52.4 | 28.8 |
| θ-RK-2 | 64.3 | 36.3 |
| **θ-Trapezoidal** | **49.1** | **27.6** |

生成困惑度越低越好。θ-Trapezoidal 在所有 NFE 下均优于现有方法。

### 图像生成（MaskGIT/ImageNet 256×256）

- θ-Trapezoidal 在 NFE≥16 时 FID 持续优于 Euler 和 τ-leaping
- FHS 和 parallel decoding 在极低 NFE（≤8）时有优势但快速饱和

### LLaDA-Instruct 8B 数学推理（GSM8K）

| 方法 | NFE=64 | NFE=128 | NFE=256 |
|------|--------|---------|---------|
| Semi-AR (Rand.) | 33.8 | 34.3 | **40.3** |
| **θ-Trapezoidal** | **35.1** | **38.4** | 39.7 |

在低 NFE（计算受限）场景下优势尤为明显，验证了高阶求解器在大模型上的有效性。

### 超参数鲁棒性

$\theta \in [0.3, 0.5]$ 在文本和图像任务上均为稳健选择，性能曲面平坦。

## 评价

⭐⭐⭐⭐⭐

**优点**：
- 首次将高阶数值方法引入离散扩散模型推理，填补了重要空白
- 理论严谨：证明了 θ-Trapezoidal 的无条件二阶收敛，理论与实验高度一致
- 实验覆盖 200M~8B 不同规模模型，跨文本/图像/数学推理多任务验证
- 无需额外训练，即插即用加速推理

**局限**：
- 外推强度的非负性假设目前依赖经验验证（理论上仍是 open problem）
- 仅考虑了二阶方法，更高阶方案留待未来探索
- 文本生成实验仅在 GPT-2 级别模型上验证
- 价值: 待评
