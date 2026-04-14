---
title: >-
  [论文解读] Adaptive Cooperative Transmission Design for Ultra-Reliable Low-Latency Communications via Deep Reinforcement Learning
description: >-
  [NeurIPS 2025][LLM Agent][URLLC] 提出DRL-CoLA双智能体DQN算法，为两跳解码转发中继系统中的每次（重）传输自适应选择5G NR的numerology、mini-slot和MCS参数，仅用本地CSI在严格时延约束下实现近最优可靠性。
tags:
  - NeurIPS 2025
  - LLM Agent
  - URLLC
  - 两跳中继
  - 深度强化学习
  - 5G NR
  - 有限块长度
---

# Adaptive Cooperative Transmission Design for Ultra-Reliable Low-Latency Communications via Deep Reinforcement Learning

**会议**: NeurIPS 2025  
**arXiv**: [2511.02216](https://arxiv.org/abs/2511.02216)  
**代码**: 无  
**领域**: 无线通信 / 强化学习  
**关键词**: URLLC, 两跳中继, 深度强化学习, 5G NR, 有限块长度

## 一句话总结

提出DRL-CoLA双智能体DQN算法，为两跳解码转发中继系统中的每次（重）传输自适应选择5G NR的numerology、mini-slot和MCS参数，仅用本地CSI在严格时延约束下实现近最优可靠性。

## 研究背景与动机

下一代无线通信需支持URLLC服务（误包率低至 $10^{-5} \sim 10^{-7}$，端到端时延毫秒级）。中继通信可增强可靠性但面临独特挑战：

- 现有两跳传输研究多集中于无重传的一次性传输，任一跳解码失败即传输失败
- 一次性方案假设两跳都有完美CSI，获取全局CSI的开销无法满足URLLC时延预算
- ARQ重传可提高可靠性但增加延迟
- 5G NR提供了自适应调制编码（AMC）、可伸缩numerology和mini-slot调度等灵活特性，但之前只被单独优化
- 没有工作联合考虑ARQ重传对两跳系统在时延约束下可靠性的影响

## 方法详解

### 整体框架

考虑源节点S通过半双工中继R向目的节点D传输延迟敏感数据包。每跳支持可伸缩numerology $\mu \in \{0,1,2,3,4\}$、可变mini-slot大小 $N_\text{sym} \in \{2,4,7,14\}$，以及15级MCS。在有限块长度下使用Polyanskiy近似计算解码错误概率。S和R仅基于本地CSI和剩余时延预算独立决策。

### 关键设计

1. **双智能体分布式MDP建模**:
    - 功能：将两跳自适应传输建模为MDP，S和R作为独立智能体
    - 核心思路：状态 $s_n^{(i)} = (\gamma_i, \bar{\gamma}_{i+1}, H, \tau_n)$ 包含本地SNR、下一跳平均SNR、包大小和剩余时延。动作 $a = (\mu, N_\text{sym}, I_\text{MCS})$ 共 $5 \times 4 \times 15 = 300$ 种组合
    - 设计动机：全局CSI交换开销过大，分布式决策符合URLLC实际约束

2. **时延感知奖励设计**:
    - 功能：基于延迟中断率（DOR）设计差异化奖励
    - 核心思路：成功传输的奖励为 $1 - \mathcal{P}_\text{DOR}(\bar{\gamma}_{i+1}, \tau_{n+1})$，惩罚为S消耗过多时延导致R预算不足。失败状态给 $-1$，未决状态给 $-0.1$ 鼓励减少不必要重传
    - 设计动机：S无法观测R的传输结果，DOR提供了估计下一跳成功概率的代理指标

3. **DQN逐跳训练**:
    - 功能：S和R各维护独立的DQN网络，从各自的经验回放缓冲中学习
    - 核心思路：连续状态空间 + 离散动作空间天然适合DQN。每 $E'$ 回合同步目标网络参数。训练完成后各智能体独立执行贪心策略
    - 设计动机：DQN适合处理连续状态和离散动作组合，且不需要智能体间通信

### 损失函数 / 训练策略

DQN损失：$\mathcal{L}_i(\boldsymbol{\theta}_i) = \mathbb{E}_{e_n \sim \mathcal{M}_i}[(y_n^{(i)} - Q_i(s_n^{(i)}, a_n^{(i)}; \boldsymbol{\theta}_i))^2]$

其中目标值 $y_n^{(i)} = \mathcal{R}_{n+1}^{(i)} + \gamma \max_{a'} Q_i(s_{n+1}^{(i)}, a'; \boldsymbol{\theta}_i^-)$。使用 $\epsilon$-贪心策略平衡探索与利用。

有限块长度下的解码错误概率：$\varepsilon_i(\gamma_i, m_i) = Q\left(\ln 2 \sqrt{\frac{m_i}{V_i}} \left(\log_2(1+\gamma_i) - \frac{H}{m_i}\right)\right)$

## 实验关键数据

### 主实验（表格）

DRL-CoLA相比其他方案的可靠性对比（不同时延预算 $T_\text{th}$ 下的成功投递概率）：

| 方案 | 特点 | 相对性能 |
|------|------|---------|
| 穷举搜索（最优） | 尝试所有参数组合 | 基准上界 |
| **DRL-CoLA** | 双智能体DQN | **接近最优** |
| 固定numerology | 仅优化MCS | 显著低于DRL-CoLA |
| 固定MCS | 仅优化numerology | 显著低于DRL-CoLA |
| 随机选择 | 基线 | 最差 |

### 消融实验

- 联合优化numerology + mini-slot + MCS的收益远大于单独优化任一参数
- DOR驱动的奖励设计显著优于简单二值奖励（成功/失败）
- 重传次数随训练自然收敛到合理值（隐式优化）

### 关键发现

- DRL-CoLA在各时延预算下均达到接近穷举搜索的最优可靠性
- 分布式决策（仅本地CSI）的性能损失极小，验证了DOR作为下一跳成功概率代理的有效性
- 联合优化三个5G NR参数比单独优化任一参数带来量级上的可靠性提升
- 在极紧时延预算下重传次数的最优策略非trivial——并非总是重传更好

## 亮点与洞察

- **系统模型完整**：首次联合考虑5G NR的三个可配置参数 + ARQ重传 + 两跳中继 + 有限块长度
- **分布式学习**：无需全局CSI交换，通过DOR桥接两个智能体的协调问题
- **重传次数隐式优化**：通过奖励设计中的小负惩罚自然实现，无需额外约束
- 实际适用性强：动作空间有限（300种），DQN网络规模小

## 局限性 / 可改进方向

- 假设Rayleigh平坦衰落，未考虑频率选择性衰落
- 假设ARQ请求总是成功，实际中ACK/NACK也可能丢失
- 仅考虑单中继两跳，多跳/多中继场景需扩展
- DQN状态维度仅4维，更复杂的场景可能需要更强的RL算法（如PPO、SAC）
- 未考虑多用户干扰和资源共享
- 缺少与最新URLLC RL方案（如Saatchi et al.的多载波版本）的对比

## 相关工作与启发

- **Saatchi et al.**：在点对点单/多载波系统中联合优化numerology+mini-slot+MCS，本文首次扩展到两跳中继
- **有限块长度理论 (Polyanskiy et al.)**：为短包URLLC提供准确的解码错误概率近似
- **多智能体DQN**：利用分散执行架构实现两个智能体的独立学习
- 对5G/6G URLLC服务的自适应无线资源管理具有实际参考价值

## 评分

⭐⭐⭐ — 系统模型完整、实际问题有意义，但RL方法本身较标准（DQN），实验深度有限
