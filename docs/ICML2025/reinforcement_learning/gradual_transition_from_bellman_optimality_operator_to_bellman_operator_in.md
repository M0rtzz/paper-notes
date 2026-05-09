---
title: >-
  [论文解读] Gradual Transition from Bellman Optimality Operator to Bellman Operator in Online RL
description: >-
  [ICML 2025][Actor-Critic] 揭示 Actor-Critic 中 Bellman 最优算子（加速学习但引入过估计偏差）和 Bellman 算子（减少偏差但收敛慢）的根本权衡，提出 Annealed Q-Learning (AQ-L)：用 expectile loss 实现从最优算子到标准算子的平滑退火，AQ-SAC 在 DM Control 10 任务上平均分达 746.1（vs SAC 657.9），实现极简即插即用的性能提升。
tags:
  - ICML 2025
  - Actor-Critic
  - 强化学习
  - overestimation bias
  - annealing
  - expectile loss
---

# Gradual Transition from Bellman Optimality Operator to Bellman Operator in Online RL

**会议**: ICML 2025  
**arXiv**: [2506.05968](https://arxiv.org/abs/2506.05968)  
**代码**: [GitHub](https://github.com/motokiomura/annealed-q-learning)  
**领域**: 强化学习  
**关键词**: Actor-Critic, Bellman operator, overestimation bias, annealing, expectile loss

## 一句话总结

揭示 Actor-Critic 中 Bellman 最优算子（加速学习但引入过估计偏差）和 Bellman 算子（减少偏差但收敛慢）的根本权衡，提出 Annealed Q-Learning (AQ-L)：用 expectile loss 实现从最优算子到标准算子的平滑退火，AQ-SAC 在 DM Control 10 任务上平均分达 746.1（vs SAC 657.9），实现极简即插即用的性能提升。

## 研究背景与动机

**领域现状**：在线强化学习中，离散动作空间的算法（如 DQN）直接使用 Bellman 最优算子 $\mathcal{T}^*$，通过 $\max_{a'} Q(s', a')$ 计算目标值，使 Q 值直接趋向最优。但在连续动作空间中，无法遍历无限多的动作取 max，因此 TD3、SAC 等主流 Actor-Critic 方法使用 Bellman 算子 $\mathcal{T}^\pi$，仅估计当前策略的 Q 值。

**现有痛点**：基于 Bellman 算子的方法中，Q 值改善完全依赖于策略先改善——形成"策略必须先变好 → Q 值才能跟着变好"的延迟链。这导致样本效率低下，尤其在机器人控制等采样昂贵的任务中成为关键瓶颈。

**核心矛盾**：Bellman 最优算子可以直接让 Q 值趋向最优（无需等策略改善），但与函数逼近器结合时，$\max$ 操作对带噪声的 Q 值引入过估计偏差（由 Jensen 不等式：$\mathbb{E}[\max Q] \geq \max \mathbb{E}[Q]$）。因此存在"加速学习 vs 估计偏差"的根本矛盾。

**切入角度**：作者通过简单表格 MDP 上的初步实验清晰地验证了这一矛盾——Q-learning 式更新收敛更快但最终过估计，SARSA 式更新无偏但更慢。自然的想法是：训练初期用最优算子加速学习（过估计反而促进探索），后期切换到标准算子消除偏差保证收敛。

**核心 idea 一句话**：用 expectile loss 的参数 $\tau$ 从接近 1 线性退火到 0.5，实现从 Bellman 最优算子到 Bellman 算子的平滑过渡。

## 方法详解

### 整体框架

输入为连续动作空间的 MDP 任务和基础 Actor-Critic 算法（TD3 或 SAC）。AQ-L 的核心修改仅在 Critic 的损失函数上：将标准 L2 损失替换为 expectile loss，并对参数 $\tau$ 执行线性退火调度。输出为改进后的策略。整个方法不改变网络架构、不增加网络数量、不修改 Actor 的更新方式。

### 关键设计

1. **Expectile Loss 实现算子插值**:

    - 功能：在连续动作空间中隐式计算 Bellman 最优算子的 $\max$ 操作，同时允许在最优算子和标准算子之间平滑插值
    - 核心思路：Expectile loss 定义为 $L_2^\tau(u) = |\tau - \mathbb{1}(u < 0)| \cdot u^2$。当 $\tau = 1$ 时等价于只关注高价值样本（近似取 max，即 Bellman 最优算子）；$\tau = 0.5$ 时等价于标准 L2 损失（取均值，即 Bellman 算子）。Critic 损失为 $L(\theta) = \mathbb{E}_{(s,a,s') \sim \mathcal{D}, a' \sim \pi}[L_2^\tau(r + \gamma Q_{\bar\theta}(s', a') - Q_\theta(s, a))]$
    - 设计动机：直接在连续空间计算 $\max_{a'} Q(s', a')$ 不可行（需要额外的优化循环或多采样 max-backup），而 expectile loss 通过对样本的非对称加权隐式实现了类似效果，且计算开销几乎为零

2. **线性退火调度**:

    - 功能：控制训练过程中算子从最优到标准的过渡速度
    - 核心思路：$\tau(t) = \tau_\text{init} - (\tau_\text{init} - 0.5) \cdot t/T$，其中 $\tau_\text{init}$ 为初始值（如 0.9），$T$ 为最大时间步。$\tau$ 从接近 1 线性降到 0.5
    - 设计动机：早期 $\tau$ 大时，过估计产生的乐观偏差促进探索——高估的动作更可能被选择并纠正，扩大了探索范围。后期当策略接近收敛时，$\tau$ 降到 0.5 切换为无偏估计，优先消除偏差而非继续改进

3. **与 TD3/SAC 的无缝集成**:

    - 功能：将 AQ-L 作为即插即用模块嵌入现有算法
    - 核心思路：对于 TD3，直接在 Critic 的 MSE loss 中替换为 expectile loss 即可得到 AQ-TD3。对于 SAC，同样替换 Critic loss 得到 AQ-SAC。当 $\tau$ 固定为 0.5 时，AQ-TD3/AQ-SAC 严格等价于原始 TD3/SAC——因此退火结束后算法行为不变
    - 设计动机：不引入额外的 V-function（IQL 需要），不增加 Q 网络数量（REDQ 需要），不需要额外采样（max-backup 需要），实现最小化的代码改动

### 损失函数

AQ-L 的 Critic 损失统一为：$L(\theta) = \mathbb{E}[L_2^{\tau(t)}(r + \gamma Q_{\bar\theta}(s', a') - Q_\theta(s, a))]$，其中 $a' \sim \pi(\cdot|s')$。相比原始 TD3/SAC 唯一改动是将 $(\cdot)^2$ 替换为 $L_2^{\tau(t)}(\cdot)$，并随训练步数退火 $\tau$。

## 实验关键数据

### DM Control 10 任务平均分 (3M 步)

| 方法 | Mean | IQM |
|------|------|-----|
| TD3 | 492.7 (459.5-527.1) | 516.0 (461.8-571.9) |
| SAC | 657.9 (623.6-688.9) | 765.0 (712.8-800.9) |
| XQL | 564.4 (522.2-604.7) | 628.8 (560.6-688.3) |
| **AQ-TD3** | **740.3 (731.0-749.0)** | **820.0 (811.5-826.8)** |
| **AQ-SAC** | **746.1 (736.3-755.0)** | **832.4 (820.5-841.6)** |

### 退火 vs 固定 τ (AQ-SAC, DM Control)

| 设置 | Mean | IQM |
|------|------|-----|
| Annealed (0.7→0.5) | 720.2 (694.8-741.0) | 821.7 (803.4-836.0) |
| Annealed (0.8→0.5) | 742.1 (729.1-754.7) | 824.0 (805.4-840.2) |
| **Annealed (0.9→0.5)** | **746.1 (732.0-758.5)** | **832.4 (815.3-844.8)** |
| Annealed (0.95→0.5) | 736.1 (725.7-745.9) | 815.6 (798.8-827.1) |
| Fixed τ=0.6 | 713.6 (690.5-734.5) | 822.7 (800.1-834.9) |
| Fixed τ=0.7 | 730.7 (715.3-745.7) | 825.0 (806.1-840.0) |
| Fixed τ=0.8 | 683.4 (660.8-702.9) | 775.9 (756.5-790.4) |
| Fixed τ=0.9 | 588.2 (559.0-613.6) | 632.7 (594.9-665.9) |
| Fixed τ=0.95 | 364.9 (338.8-390.6) | 303.5 (265.4-341.5) |

### 关键发现

1. AQ-TD3 平均分 740.3 大幅超越 TD3 的 492.7（+50.3%），AQ-SAC 746.1 超越 SAC 657.9（+13.4%）
2. 退火版 ($\tau_\text{init}$=0.9) 以 746.1 超越最佳固定 $\tau$=0.7 的 730.7，且对初始值的敏感性远低于固定 $\tau$
3. 固定 $\tau$=0.9 和 0.95 由于持续过估计导致分数骤降至 588.2 和 364.9，证明退火的必要性
4. 在 hopper-hop、humanoid-run 等高难度任务上提升尤为显著——这些任务上 TD3/SAC 的得分极低
5. AQ-SAC 在 Meta-World 操作任务上也优于 SAC，表明方法跨任务类型的通用性

## 亮点与洞察

1. **洞察精准且验证充分**：表格 MDP 初步实验清晰展示了最优算子加速 vs 过估计的矛盾，为退火设计提供了清晰的动机
2. **实现极简**：仅替换一行 loss 函数 + 添加退火调度，不改变任何网络架构或训练流程
3. **"早期过估计 = 有益探索"的反直觉发现**：过估计让未探索的动作看起来价值更高，促成纠错式探索。这一副作用在早期是有益的
4. **退火带来超参鲁棒性**：初始 $\tau$ 从 0.7 到 0.95 变化时，退火版分数变化 <3%，而固定 $\tau$ 在同范围内分数波动 >50%

## 局限性

- 退火持续时间和初始 $\tau$ 仍为超参数，虽然比固定 $\tau$ 鲁棒但仍需调节
- 理论分析局限于表格 MDP 的初步实验，缺乏函数逼近下的收敛保证
- 未与 REDQ、DroQ 等其他过估计缓解方法做系统对比
- 仅验证了运动和操作任务，未涉及视觉观测或超高维场景

## 相关工作与启发

- IQL (Kostrikov et al., 2022) 在离线 RL 中使用固定 expectile loss，AQ-L 的退火思想可视为"在线版 IQL + 自适应 τ"
- XQL (Garg et al., 2023) 用 Gumbel 回归估计软最优值，但指数型 loss 不如 expectile loss 稳定，AQ-SAC 746.1 远超 XQL 564.4
- 退火思想的普适性：任何需要在"激进探索"和"保守收敛"之间过渡的 RL 组件都可借鉴

## 评分

⭐⭐⭐⭐⭐ 洞察深刻、实现极简、效果显著的工作。从表格 MDP 的清晰洞察到连续空间的优雅解法，再到跨任务、跨基线的一致性提升，体现了"用最少的改动获得最大的收益"的研究美感。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] Gradual Transition from Bellman Optimality Operator to Bellman Operator in Online Reinforcement Learning](gradual_transition_from_bellman_optimality_operator_to_bellman_operator_in_onlin.md)
- [\[ICML 2025\] Actor-Critics Can Achieve Optimal Sample Efficiency](actor-critics_can_achieve_optimal_sample_efficiency.md)
- [\[ICML 2025\] Action-Dependent Optimality-Preserving Reward Shaping (ADOPS)](action-dependent_optimality-preserving_reward_shaping.md)
- [\[ICML 2025\] A Theoretical Study of (Hyper) Self-Attention through the Lens of Interactions: Representation, Training, Generalization](a_theoretical_study_of_hyper_self-attention_through_the_lens_of_interactions_rep.md)
- [\[ICML 2025\] BRITE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](brite_bootstrapping_reinforced_thinking_process_to_enhance_language_model_reason.md)

</div>

<!-- RELATED:END -->
