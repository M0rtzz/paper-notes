---
title: >-
  [论文解读] Convert Language Model into a Value-based Strategic Planner
description: >-
  [ACL 2025][LLM/NLP][emotional support conversation] 提出 straQ* 框架，将 LLM 转化为基于 Q-learning 的策略规划器，用平均 logit 作为 Q 值实现策略级 MDP，在情感支持对话中基于长期回报选择最优策略，超越直接推理、CoT 和微调等基线。
tags:
  - ACL 2025
  - LLM/NLP
  - emotional support conversation
  - Q-learning
  - strategic planning
  - reinforcement-learning
  - dialogue
---

# Convert Language Model into a Value-based Strategic Planner

**会议**: ACL 2025  
**arXiv**: [2505.06987](https://arxiv.org/abs/2505.06987)  
**代码**: https://github.com/suran662/StraQ  
**领域**: LLM/NLP  
**关键词**: emotional support conversation, Q-learning, strategic planning, reinforcement-learning, dialogue

## 一句话总结
提出 straQ* 框架，将 LLM 转化为基于 Q-learning 的策略规划器，用平均 logit 作为 Q 值实现策略级 MDP，在情感支持对话中基于长期回报选择最优策略，超越直接推理、CoT 和微调等基线。

## 研究背景与动机

**领域现状**：情感支持对话（ESC）旨在缓解用户情绪困扰，LLM 在此方向取得进展。ESC 通常分三阶段：探索->安慰->行动。

**现有痛点**：现有 LLM 方法聚焦即时回复质量，缺乏长期策略规划，导致策略偏差和阶段转换不流畅。

**核心矛盾**：如何让 LLM 在对话中考虑长期回报而非短视地选择当前最优策略？

**本文要解决什么？** 将 ESC 形式化为策略级 MDP，用价值 RL 方法学习最优策略选择。

**切入角度**：用 LLM 的平均 token logit 作为 Q 值，通过 Bellman 方程训练 Q 网络。

**核心idea一句话**：将 LLM 的 next-token prediction 转化为 next-strategy prediction，用 DQN 学习策略价值函数。

## 方法详解

### 整体框架
定义策略级 MDP（状态=对话历史+情绪，动作=支持策略，奖励=对话质量）-> 用 LLM 作为 Q 网络 -> Bellman 方程训练 -> 推理时选最大 Q 值策略 -> 另一个 LLM 根据策略生成回复。

### 关键设计

1. **策略级 MDP**

    - 状态：对话历史 + 当前情绪 + 背景描述
    - 动作：ESC 支持策略集合（如"提供建议""情感验证"等）
    - Q(s,a) = LLM 对策略 token 的平均 log probability
    - 设计动机：策略级比 token 级 MDP 更适合对话规划

2. **Q 值计算与训练**

    - 用 Bellman 方程的 TD loss 替代交叉熵损失训练
    - 设计动机：平均 logit 自然表示 LLM 对策略的"信心"

3. **两种奖励机制**

    - Imitation reward：基于专家策略序列
    - Distillation reward：用强 LLM 评估策略合理性
    - 设计动机：imitation 更适合自动指标，distillation 更适合人类评价和泛化

## 实验关键数据

### 主实验 -- ESConv 数据集
| 方法 | 策略准确率 | 回复质量 | 人类评分 |
|------|-----------|---------|---------|
| Direct Inference | 基线 | 基线 | 基线 |
| CoT | +2% | +0.5 | +0.3 |
| SFT | +5% | +1.2 | +0.5 |
| **straQ*** | **+8%** | **+1.8** | **+1.0** |

### 消融实验
| 配置 | 策略准确率 | 说明 |
|------|-----------|------|
| straQ* (imitation) | 最高自动指标 | 模仿专家策略 |
| straQ* (distillation) | 最高人类评分 | 更好泛化 |
| w/o Q-learning | 下降显著 | 证明 RL 的必要性 |

### 关键发现
- **straQ* 在策略规划和回复质量上全面超越基线**
- **Bellman TD 损失可以在 LLM 上收敛**：验证了用 logit 做 Q 值的可行性
- **两种奖励互补**：imitation 擅长模式匹配，distillation 擅长泛化

## 亮点与洞察
- **将 Q-learning 优雅地嵌入 LLM 架构**——不引入额外网络，直接用 LLM 的 logit 作为 Q 值
- **策略级 MDP**比 token 级 RL 更适合对话系统——动作空间小且有明确语义

## 局限性 / 可改进方向
- 仅在 ESC 领域验证，其他对话场景未测试
- Q 值用平均 logit 近似，理论保证不足
- 改进方向：多轮 Q 值迭代、模型感知的策略空间设计

## 相关工作与启发
- **vs RLHF（PPO/DPO）**：RLHF 优化 token 级策略，straQ* 优化对话策略级
- **vs FSM 方法**：FSM 是硬编码的策略转换，straQ* 是数据驱动的学习

## 评分
- 新颖性: ⭐⭐⭐⭐ LLM+Q-learning 的结合方式新颖
- 实验充分度: ⭐⭐⭐ ESC 数据集较小，仅 2 个数据集
- 写作质量: ⭐⭐⭐⭐ MDP 形式化清晰
- 价值: ⭐⭐⭐⭐ 对对话系统策略规划有启发
