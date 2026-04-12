---
title: >-
  [论文解读] Thompson Sampling for Multi-Objective Linear Contextual Bandit
description: >-
  [NeurIPS 2025][Thompson采样] 提出 MOL-TS，首个具有 Pareto regret 保证的多目标线性上下文 Bandit Thompson 采样算法，通过乐观采样策略和新定义的有效 Pareto 最优概念，实现 $\widetilde{O}(d^{3/2}\sqrt{T})$ 的 regret 上界。
tags:
  - NeurIPS 2025
  - Thompson采样
  - 多目标优化
  - 上下文Bandit
  - Pareto最优
  - 有效Pareto前沿
---

# Thompson Sampling for Multi-Objective Linear Contextual Bandit

**会议**: NeurIPS 2025  
**arXiv**: [2512.00930](https://arxiv.org/abs/2512.00930)  
**代码**: 无  
**领域**: 强化学习  
**关键词**: Thompson采样, 多目标优化, 上下文Bandit, Pareto最优, 有效Pareto前沿

## 一句话总结
提出 MOL-TS，首个具有 Pareto regret 保证的多目标线性上下文 Bandit Thompson 采样算法，通过乐观采样策略和新定义的有效 Pareto 最优概念，实现 $\widetilde{O}(d^{3/2}\sqrt{T})$ 的 regret 上界。

## 研究背景与动机

1. **领域现状**：多目标多臂 Bandit（MOMAB）中，Pareto 最优比标量化方法更通用。但所有现有 Pareto regret 分析都基于 UCB 算法
2. **现有痛点**：TS 在单目标中实证表现常优于 UCB，但多目标 TS 的理论分析存在根本困难——需跨多个目标协调随机采样的乐观性
3. **核心矛盾**：单目标 TS 的单次采样有常数概率乐观，但多目标需要所有目标同时乐观，概率随目标数 $L$ 指数下降
4. **核心 idea**：通过每个目标多次采样（$M = O(\log L)$ 次）并取最大值，避免乐观概率的指数衰减

## 方法详解

### 关键设计

1. **有效 Pareto 最优臂**：标准 Pareto 最优只要求不被单个臂支配，但可能被臂的凸组合支配。有效 Pareto 最优要求对**任意凸组合**都不被支配，确保重复选择时累积奖励真正最优

2. **乐观采样策略**：每个目标采样 $M$ 个参数，用最大值评估奖励。当 $M \geq 1 - \frac{\log L}{\log(1-\tilde{p})}$ 时，各目标同时乐观的概率保持恒常

3. **Regret 分析**：将有效 Pareto regret 上界化为 $\boldsymbol{w}_t^\top(\boldsymbol{\mu}_{t,\bar{a}_*} - \boldsymbol{\mu}_{t,a_t})$，但 $\boldsymbol{w}_t$ 本身是随机的（从有效 Pareto 前沿决定），增加了分析难度

## 实验关键数据

### 主实验 — 4目标, 50臂, 5维

| 算法 | Pareto Regret | EPR | 各目标累积奖励 |
|------|--------------|-----|-------------|
| MOL-TS (M=O(logL)) | **最低** | **最低** | **全部最高** |
| MOL-UCB | 中等 | 中等 | 中等 |
| MOL-ε-Greedy | 最高 | 最高 | 偏低 |
| MOL-TS (M=1) | 略高于M=O(logL) | 略高 | 略低 |

### 关键发现
- 有效 Pareto 前沿确实比普通 Pareto 前沿带来更高的累积奖励
- $M = O(\log L)$ 的设定既有理论保证又在实验中必要

## 亮点与洞察
- **有效 Pareto 最优**的定义解决了一个被忽视的问题：重复选择 Pareto 最优臂不一定带来最优累积奖励
- 与 Theorem 1 的对偶性：有效 Pareto 最优 ↔ 线性标量化最优，建立了优雅的理论连接

## 局限性 / 可改进方向
- 每轮计算有效 Pareto 前沿需要求解凸包，目标数或臂数大时计算开销增加
- Regret 中 $\log L$ 和 $\log M$ 依赖虽小但不可完全消除

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 首个多目标 TS + 有效Pareto概念
- 实验充分度: ⭐⭐⭐ 实验设定较简单
- 写作质量: ⭐⭐⭐⭐ 理论分析深入严谨
- 价值: ⭐⭐⭐⭐ 填补了多目标 Bandit 理论空白
