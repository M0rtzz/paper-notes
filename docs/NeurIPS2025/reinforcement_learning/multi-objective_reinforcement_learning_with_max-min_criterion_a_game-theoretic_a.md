---
title: >-
  [论文解读] Multi-Objective Reinforcement Learning with Max-Min Criterion: A Game-Theoretic Approach
description: >-
  [NeurIPS 2025][多目标强化学习] 将max-min多目标强化学习重新表述为两人零和正则化连续博弈，提出ERAM/ARAM算法，利用镜像下降实现简洁的闭式权重更新，保证全局最后迭代收敛，在交通信号控制等任务中显著优于已有方法。
tags:
  - NeurIPS 2025
  - 多目标强化学习
  - Max-Min公平
  - 零和博弈
  - 镜像下降
  - 最后迭代收敛
---

# Multi-Objective Reinforcement Learning with Max-Min Criterion: A Game-Theoretic Approach

**会议**: NeurIPS 2025  
**arXiv**: [2510.20235](https://arxiv.org/abs/2510.20235)  
**代码**: [GitHub](https://github.com/whbyeon/ERAM-ARAM)  
**领域**: 强化学习  
**关键词**: 多目标强化学习, Max-Min公平, 零和博弈, 镜像下降, 最后迭代收敛

## 一句话总结

将max-min多目标强化学习重新表述为两人零和正则化连续博弈，提出ERAM/ARAM算法，利用镜像下降实现简洁的闭式权重更新，保证全局最后迭代收敛，在交通信号控制等任务中显著优于已有方法。

## 研究背景与动机

**领域现状**: 多目标强化学习（MORL）处理向量值奖励的MDP，效用函数方法是主流，其中加权和最常见。Max-min MORL追求最差目标维度的最大化，天然适合公平性资源分配场景。

**现有痛点**: (i) GGF-DQN/GGF-PPO优化的是代理目标 $\mathbb{E}_\pi[\min_k \sum_t \gamma^t r_k]$（Jensen不等式下界），而非真实目标 $\min_k \mathbb{E}_\pi[\sum_t \gamma^t r_k]$；(ii) Park et al.的双循环方法虽直接求解真实目标但内存和计算开销极大（20份Q网络），仅保证平均迭代收敛；(iii) GGF-PPO每批只优化当前最差维度，相当于 $w$ 在one-hot向量间切换，只有平均迭代收敛。

**核心矛盾**: $\min$ 算子的非线性导致max-min MORL无法直接用标准RL方法求解，同时又需要高效的数值求解方法。

**本文要解决什么**: 设计一个计算和内存高效、具有最后迭代收敛保证的max-min MORL算法。

**切入角度**: 利用max-min与min-max在熵正则化下的特殊等价性，将问题转化为两人零和博弈的纳什均衡求解。

**核心idea一句话**: Learner用NPG/PPO更新策略，Adversary用熵正则化镜像下降的闭式softmax公式更新权重 $w$——两者协同实现max-min公平。

## 方法详解

### 整体框架

**等价关系链**:
$$\max_\pi \min_{k} V_{k,\tau}^\pi = \max_\pi \min_{w \in \Delta^K} \langle w, \mathbf{V}_\tau^\pi \rangle = \min_{w \in \Delta^K} \max_\pi \langle w, \mathbf{V}_\tau^\pi \rangle$$

第一个等式是连续化（将离散 $\min_k$ 扩展到单纯形上的 $\min_w$），第三个等式是max-min = min-max的特殊性（Theorem 3.1）。由此定义两人零和博弈：

- **Learner**: 策略参数 $\theta$，最大化 $\langle w, \mathbf{V}_\tau^{\pi_\theta} \rangle$
- **Adversary**: 权重向量 $w \in \Delta^K$，最小化 $\langle w, \mathbf{V}_\tau^{\pi_\theta} \rangle$

### 关键设计

**模块1: 正则化博弈 $\mathcal{RG}$**
- 做什么：在原始博弈的效用函数上添加各自的正则化
- Learner效用：$u_{Learner}^{\mathcal{RG}} = \langle w, \mathbf{V}^{\pi_\theta} \rangle + \tau \tilde{H}(\pi_\theta) - \tau_w H(w)$
- $\tau \tilde{H}(\pi_\theta)$：避免max-min MORL的不确定性问题（某些MOMDP仅有随机最优策略）
- $-\tau_w H(w)$：防止 $w$ 退化为one-hot向量，促使同时考虑多个目标维度

**模块2: ERAM算法——Learner更新（NPG/PPO）**
- 做什么：通过自然策略梯度更新策略
- Tabular闭式：$\pi_{\theta_{t+1}}(a|s) = \frac{1}{Z_\pi} (\pi_{\theta_t}(a|s))^\alpha \exp\left(\frac{1-\alpha}{\tau} Q_{w_t,\tau}^{\pi_{\theta_t}}(s,a)\right)$，其中 $\alpha = 1 - \frac{\eta\tau}{1-\gamma}$
- Deep RL：直接替换为PPO

**模块3: ERAM算法——Adversary更新（闭式MD）**
- 做什么：用修正版镜像下降更新权重 $w$
- 核心公式：$w_{t+1} = \text{softmax}\left(-\frac{1-\beta}{\tau_w} \mathbf{V}^{\pi_{\theta_t}} + \beta \log w_t\right)$
- 其中 $\beta = \frac{1}{\lambda \tau_w + 1} \in (0,1)$，恒在合法范围内
- 设计动机：选择负熵正则（而非 $\ell_2$-范数）使得MD更新有解析解，无需投影梯度下降

**模块4: ARAM——自适应正则化改进**
- 做什么：将Adversary的正则从 $H(w)$（关于均匀分布的KL）改为 $-D_{KL}(w \| c)$
- 参考向量 $c$ 动态计算：$c_i = \text{softmax}(\mathbb{E}_{s,a}[r_i(s,a) r_{i'}(s,a)])$，$i'$ 是上一批次最差目标
- 设计动机：不像ERAM平等考虑所有维度，ARAM将更多权重放在表现差的维度上（但仍非仅关注最差维度），加速收敛

### 损失函数/训练策略

- Learner: PPO目标函数（Deep RL情况）
- Adversary: 闭式softmax更新（免投影）
- 步长关系：$\eta = O(\epsilon)$ > $\lambda = O(\epsilon^2)$（策略更新快于权重更新）

## 实验关键数据

### 主实验（Table 1, 交通信号控制）

| 环境 | ARAM | ERAM | Park et al. | GGF-PPO | GGF-DQN | Avg-DQN |
|------|:----:|:----:|:-----------:|:-------:|:-------:|:-------:|
| Base-4 | **-1160** | -1387 | -1681 | -1731 | -1838 | -2774 |
| Asym-4 | **-2696** | -2732 | -3510 | -3501 | -3053 | -4245 |
| Asym-16 | **-15043** | -17334 | -23663 | -21663 | -17792 | -27499 |

### 消融实验（附录中多环境结果）

| 实验 | 结论 |
|------|------|
| 物种保护环境 | ARAM/ERAM显著优于baselines |
| MO-Reacher环境 | 同上 |
| Four-Room环境 | 同上 |
| $\beta$ 消融 | $\beta$ 不接近0（ERAM）或1（ARAM）时性能稳定 |

### 效率对比（Table 2, 训练时间）

| 环境 | ERAM | ARAM | Park et al. | GGF-PPO |
|------|:----:|:----:|:-----------:|:-------:|
| Base-4 | **111min** | 120min | 346min | 122min |
| Asym-4 | **87min** | 87min | 241min | 85min |
| Asym-16 | **356min** | 365min | 1125min | 394min |

内存：ERAM/ARAM使用约13,704参数/次权重更新 vs Park et al.的274,084参数（减少95%）。

### 关键发现

1. ARAM在所有交通信号控制环境中一致最优，ERAM次之
2. 相比Park et al.，训练时间减少约65-68%，内存减少约95%
3. ERAM展示了最后迭代收敛（图3），Park et al.展示振荡行为
4. 自适应正则化（ARAM vs ERAM）带来显著提升，代价几乎可忽略

## 亮点与洞察

1. **max-min = min-max等价性的利用**: RL中值函数对策略非凸，不能直接用minimax定理，但在正则化设置中等价性成立（通过特殊构造证明）
2. **闭式权重更新**: 负熵正则 + KL散度Bregman = softmax闭式解，避免了投影梯度下降的迭代开销
3. **GGF-PPO作为特例**: 当 $\tau_w = 0$ 且去除 $D_\psi(w,w_t)$ 时，本方法退化为GGF-PPO（$w$ 成为one-hot向量）
4. **最后迭代收敛**: 比平均迭代收敛实用性更强——直接使用最终策略而非历史平均

## 局限性/可改进方向

1. ARAM的理论分析留作未来工作（目前仅有ERAM的tabular理论保证）
2. 正则化系数 $\tau$ 和 $\tau_w$ 引入了逼近误差，最优解与无正则版本有差距（线性于 $\tau, \tau_w$）
3. tabular设置的理论分析不能直接推广到深度RL（但实验中PPO替代有效）
4. 对 $K$ 很大时（Asym-16: $K=16$），性能差距缩小，扩展到更大 $K$ 的效率有待验证
5. 样本复杂度 $\tilde{O}(K / ((1-\gamma)^3 \epsilon^6 \epsilon_{acc}^2))$ 对 $\epsilon$ 的依赖较强

## 相关工作与启发

- **与Park et al. (2024)对比**: 后者是双循环 + 零阶梯度估计 + 投影梯度下降，仅平均迭代收敛；本文是单循环 + 闭式更新 + 最后迭代收敛，效率提升约95%
- **与GGF-PPO (Siddique et al., 2021)对比**: 后者每批仅优化最差维度（one-hot $w$）；本文通过熵正则同时考虑多维度
- **与APMD (Abe et al., 2024)对比**: 后者假设平滑单调博弈，不适用于RL（值梯度非单调）
- **启发**: 博弈论视角将MORL与均衡计算联系起来，正则化技巧（负熵→闭式解）对其他约束RL问题也值得借鉴

## 评分

⭐⭐⭐⭐⭐ (5/5)

理论与实践结合紧密——博弈论重新表述优雅，闭式权重更新实用，最后迭代收敛保证是重要进步。实验在真实交通信号控制中大幅优于baselines，95%内存减少和65%时间减少有强实用价值。ARAM的自适应正则是锦上添花。代码公开。
