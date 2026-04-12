---
title: >-
  [论文解读] More Than Irrational: Modeling Belief-Biased Agents
description: >-
  [AAAI 2026][机器人][computational rationality] 提出一类计算理性 (CR) 用户模型，将人类"非理性"行为解释为在有限记忆等认知约束下基于偏差信念做出的理性决策，并设计嵌套粒子滤波方法在线推断用户的认知边界参数和信念状态，进一步构建自适应 AI 助手。
tags:
  - AAAI 2026
  - 机器人
  - computational rationality
  - user modeling
  - biased belief
  - memory decay
  - POMDP
  - particle filtering
  - adaptive assistance
---

# More Than Irrational: Modeling Belief-Biased Agents

**会议**: AAAI 2026  
**arXiv**: [2511.12359](https://arxiv.org/abs/2511.12359)  
**代码**: [GitHub](https://github.com/Yifan-Zhu/More-Than-Irrational-Modeling-Belief-Biased-Agents)  
**领域**: Human-AI Collaboration / Computational Rationality  
**关键词**: computational rationality, user modeling, biased belief, memory decay, POMDP, particle filtering, adaptive assistance  

## 一句话总结

提出一类计算理性 (CR) 用户模型，将人类"非理性"行为解释为在有限记忆等认知约束下基于偏差信念做出的理性决策，并设计嵌套粒子滤波方法在线推断用户的认知边界参数和信念状态，进一步构建自适应 AI 助手。

## 背景与动机

- 人机协作中，AI 需从行为观测推断用户目标、信念和未来行动，但人类行为常显得"非理性"
- Computational Rationality 理论认为人类是在认知资源约束下的理性决策者，看似次优的行为源于认知约束导致的偏差信念
- 日常例子：找手机时可能检查不相关的位置，因为记忆衰退导致关于手机位置的信念有偏差
- 现有 CR 工作集中在视觉、打字、驾驶等领域，很少系统地建模有限记忆这一普遍认知约束
- 亟需一个通用框架来建模记忆受限用户并在线推断其认知参数

## 核心问题

1. 如何形式化建模因记忆受限导致偏差信念的计算理性用户？
2. 如何从被动观察的行为流中在线推断用户的潜在认知约束参数和信念状态？
3. 推断结果如何用于构建自适应 AI 辅助系统？

## 方法详解

### 整体框架

在标准 POMDP 基础上引入参数化的内部记忆过程 f_θ，建模用户的记忆衰退如何导致历史观测被污染，进而产生偏差信念 b̃，用户在偏差信念下最优行动（softmax 策略），形成看似次优的行为。

### 关键设计

**CR User Model**:
- 定义内部记忆状态 h̃_t = (õ_{t}^{:t}, ã_{t}^{:t-1})，记忆中的观测可随时间演变（õ_t^j ≠ õ_{t-1}^j）
- 记忆动力学函数 f_θ 将旧记忆和新观测映射为新记忆状态（含可能的污染）
- 偏差信念 b̃_t 通过在污染记忆上做 Bayes 推断计算，需边际化整个记忆序列（失去 Markov 性质）
- 用户策略 π*(a|b̃; θ) 是在偏差信念上的 softmax 最优策略

**Online Inference via Nested Particle Filtering (NPF)**:
- 外层 N_θ 个粒子估计 p(θ|h_t)，内层每个 θ^i 维护 N_{h̃} 个粒子估计 p(h̃_{t-1}|h_t, θ^i)
- 权重更新核心：用策略 likelihood π*(a_{t-1}|b̃; θ^i) 评估每个粒子解释观测行为的能力
- 计算复杂度从精确推断的 O(|S|^t · t!) 降至 O(N_θ · N_{h̃} · t · |S|)

**Assistive-POMDP**:
- AI 助手观测环境状态和用户行为，不知用户内部状态和 θ
- 三种干预：DoNothing、MemoryHint（提醒被遗忘的观测）、ActionHint（直接建议行动）
- 用 NPF 维护对用户 (h̃, θ) 的信念，用 PPO 学习基于信念的辅助策略

## 实验关键数据

**实验环境**: T-maze 导航任务（需记住目标物体后导航到对应终点）

**CR 模型验证**:
- θ=0.0（完美记忆）: 最短路径直达目标
- θ=0.4: 学会多次观察以巩固记忆
- θ=0.7: 出现"遗忘-重新检查"行为模式
- θ=1.0（无记忆）: 直接随机猜测，不浪费时间探索

**在线推断**:
- PM Error 在 45 步内下降 90%，78 步内下降 95%
- 最终 PM Error: 0.0087 ± 0.0035（非常准确）
- 对温度参数 τ ∈ {1.0, 3.0, 5.0} 均鲁棒，τ=10.0 时收敛较慢

**自适应辅助**:
- θ≤0.3: AI 几乎不干预
- θ ∈ [0.4, 0.8]: 以 MemoryHint 为主，在关键时刻提醒
- θ≥0.9: 转向 ActionHint，因为记忆提示也会被遗忘

## 亮点

- 将"非理性"行为优雅地解释为记忆约束下的理性行为，理论框架严谨完整
- CR 模型生成的行为模式直觉上非常合理（多次观察、遗忘重查、放弃探索），验证了模型的表达力
- NPF 推断方法在 <100 步内准确恢复 θ，实用性强
- Assistive-POMDP 闭环展示了从建模→推断→辅助的完整 pipeline
- 开源代码

## 局限性 / 可改进方向

- 仅在 T-maze 简单环境验证，需在更复杂真实任务中测试
- 假设 AI 完全知道环境动力学（T 和 O），现实中可能需要同时学习
- 记忆衰退模型（每步独立以 θ 概率遗忘）过于简化，真实记忆衰退更复杂（如与时间呈指数关系、受情绪/注意力影响）
- θ 假设为静态参数，真实用户的认知能力可能随时间/疲劳变化
- 未与真实人类实验数据对比验证

## 与相关工作的对比

- vs. Kwon et al. (inverse RL): 后者假设完美记忆但不完美内部模型；本文建模记忆缺陷
- vs. Jacob et al. (bounded inference): 后者关注推理预算约束；本文关注记忆资源约束
- vs. 应用特定 CR 工作 (CRTypist, 视觉追踪等): 本文提供更通用的记忆建模框架
- vs. Boltzmann rationality: 后者用温度参数解释次优行为，无法刻画信念偏差的结构性原因

## 启发与关联

- 将认知约束形式化为 POMDP 中的记忆污染函数 f_θ，是一个优雅且可扩展的框架
- 未来可将 f_θ 替换为更复杂的认知模型（如注意力约束、信息处理带宽限制）
- 自适应辅助的思路适用于教育 AI、医疗提醒系统、驾驶辅助等场景
- NPF 的嵌套粒子滤波技术可应用于其他需要同时推断静态参数和动态状态的问题

## 评分
- 新颖性: ⭐⭐⭐⭐⭐
- 实验充分度: ⭐⭐⭐
- 写作质量: ⭐⭐⭐⭐⭐
- 价值: ⭐⭐⭐⭐
