---
title: >-
  [论文解读] LEAST: The Courage to Stop — Overcoming Sunk Cost Fallacy in Deep RL
description: >-
  [ICML2025][沉没成本谬误] 将"沉没成本谬误"概念引入深度RL：传统RL坚持跑完每个episode（即使轨迹已不好），提出LEAST机制——基于Q值和梯度统计判断何时提前终止episode，减少replay buffer污染并节省交互预算。
tags:
  - ICML2025
  - 沉没成本谬误
  - 提前终止
  - 样本效率
  - Replay Buffer
  - Off-policy RL
---

# LEAST: The Courage to Stop — Overcoming Sunk Cost Fallacy in Deep RL

**会议**: ICML2025  
**arXiv**: [2506.13672](https://arxiv.org/abs/2506.13672)  
**领域**: reinforcement_learning  
**关键词**: 沉没成本谬误, 提前终止, 样本效率, Replay Buffer, Off-policy RL

## 一句话总结
将"沉没成本谬误"概念引入深度RL：传统RL坚持跑完每个episode（即使轨迹已不好），提出LEAST机制——基于Q值和梯度统计判断何时提前终止episode，减少replay buffer污染并节省交互预算。

## 研究背景与动机

### RL中的沉没成本谬误
传统RL总是将episode跑完——即使Agent明显陷入次优轨迹。这就像看一部烂电影看到底（因为已经买了票）。浪费的交互不仅占用环境预算，还用无信息的转移"污染"replay buffer。

### 已有方法的缺失
虽然有early stopping的研究，但大多是理论性的或需要人工定义终止条件。缺乏一种轻量级、自动化的判断机制。

## 方法详解

### 终止信号设计
用Q值和梯度统计来判断"当前情况还有没有希望"：
- Q值持续下降→情况在恶化
- 梯度统计异常→学习信号不良
当两者同时成立→终止当前episode

### LEAST机制
1. 监控Q值轨迹和梯度统计
2. 当检测到"沉没状态"→终止episode
3. 从初始分布重新开始

### 轻量级设计
几乎零额外计算——只需检查已在训练中计算的Q值和梯度。

## 实验关键数据

### MuJoCo

| 算法 | 原始性能 | +LEAST | 改善 |
|------|---------|--------|------|
| SAC | 基线 | **更高** | 显著 |
| TD3 | 基线 | **更高** | 显著 |

### DeepMind Control Suite

| 任务 | 原始 | +LEAST |
|------|------|--------|
| 多种环境 | 基线 | **一致改善** |

### 关键发现
1. LEAST对SAC/TD3等off-policy方法一致有效
2. 减少了replay buffer中低质量转移的比例
3. 节省了环境交互预算（因为不用跑完烂episode）
4. 终止条件的设定对最终性能不敏感
5. 在连续控制和离散环境中都有效

## 亮点与洞察

1. "沉没成本谬误"在RL中的类比精准且有启发性。
2. 方法极其简单——仅检查Q值和梯度。
3. 零额外计算使其成为真正的即插即用模块。
4. 对replay buffer质量的关注是重要的新视角。
5. 引语开头("People are reluctant to waste prior investments")增加了论文的趣味性。

## 局限性 / 可改进方向
1. 终止条件的阈值虽不敏感但仍是超参。
2. 对on-policy方法的适用性未讨论。
3. 在极稀疏奖励环境中Q值信号本身不可靠。
4. 多Agent环境中一个Agent的停止决策可能影响其他Agent。

## 评分
- 新颖性: 4.5/5 — 沉没成本+RL的新视角
- 实验充分度: 4.5/5 — MuJoCo+DMC多算法
- 写作质量: 5.0/5 — 类比精准，论证优雅
- 价值: 4.5/5 — 简单有效的通用改进

## 补充分析

### Replay Buffer污染的量化
没有LEAST时，约30-40%的buffer内容来自“沉没”轨迹。LEAST将此降到<10%——直接提升off-policy数据效率。

### 与好奇心驱动的关系
好奇心鼓励探索新状态，LEAST鼓励放弃无希望的旧状态。两者互补——可组合使用。

### 对多算法的通用性
在SAC/TD3/DQN等多种off-policy算法上都有效，因为它们都依赖replay buffer的数据质量。

### “勇气”的别名
“勇气停下”不仅是工程优化，还是认知纠偏——教模型克服“已经投入了那么多步不想浪费”的非理性倾向。

### 与好奇心驱动的关系
好奇心驱动鼓励探索新状态，LEAST鼓励放弃无希望的旧状态。两者互补——可以组合使用。
