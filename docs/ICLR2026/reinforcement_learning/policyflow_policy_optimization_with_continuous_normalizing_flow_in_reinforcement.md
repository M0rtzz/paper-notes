---
title: >-
  [论文解读] PolicyFlow: Policy Optimization with Continuous Normalizing Flow in Reinforcement Learning
description: >-
  [ICLR 2026][连续归一化流] 提出PolicyFlow——将连续归一化流(CNF)策略与PPO式目标结合的在线RL算法：通过沿插值路径评估速度场变化近似重要性比率(避免全流路径昂贵的反向传播)，提出受布朗运动启发的隐式熵正则器(促进单调熵增长防止模式坍缩)，在MultiGoal/PointMaze/IsaacLab/MuJoCo上超越高斯PPO和流式基线(FPO/DPPO)，特别擅长多模态动作分布。
tags:
  - ICLR 2026
  - 连续归一化流
  - PPO
  - 多模态策略
  - 重要性比率近似
  - 布朗运动熵正则
---

# PolicyFlow: Policy Optimization with Continuous Normalizing Flow in Reinforcement Learning

**会议**: ICLR 2026  
**arXiv**: [2602.01156](https://arxiv.org/abs/2602.01156)  
**代码**: [项目页面](https://policyflow2026.github.io/)  
**领域**: 强化学习/策略优化  
**关键词**: 连续归一化流, PPO, 多模态策略, 重要性比率近似, 布朗运动熵正则

## 一句话总结
提出PolicyFlow——将连续归一化流(CNF)策略与PPO式目标结合的在线RL算法：通过沿插值路径评估速度场变化近似重要性比率(避免全流路径昂贵的反向传播)，提出受布朗运动启发的隐式熵正则器(促进单调熵增长防止模式坍缩)，在MultiGoal/PointMaze/IsaacLab/MuJoCo上超越高斯PPO和流式基线(FPO/DPPO)，特别擅长多模态动作分布。

## 研究背景与动机

**领域现状**：PPO是最流行的在线RL算法→需通过重要性比率更新策略→高斯策略方便但只能表示单峰分布。CNF/扩散模型→表达力极强但似然计算昂贵→与PPO不兼容。

**现有痛点**：
   - (1) 扩散策略(DPPO)→通过全扩散链反向传播→梯度爆炸/消失
   - (2) FPO→ELBO近似重要性比率→不对称偏差(增大vs减小方向不均)
   - (3) CNF策略的熵→闭式需沿流路径积分散度→计算昂贵
   - (4) 从头训练时需要更好的探索→现有方法主要做微调

**切入角度**：沿简单插值路径(非全流路径)近似重要性比率+隐式布朗运动熵→两个轻量解决方案。

## 方法详解

### CNF策略

动作生成：$\mathbf{a} = \varphi_1(\mathbf{z};\mathbf{s}) + \mathbf{n}$，z~N(0,I)，n~N(0,σ²)

其中$\varphi_1$是从噪声到动作的CNF流终点。

### 重要性比率近似

关键观察：不需精确似然→只需似然比率。

- 标准方法：沿全流路径ODE求解→$O(T_{ODE})$步+反向传播→昂贵
- PolicyFlow：沿线性插值路径$\psi_t = (1-t)\mathbf{z} + t\mathbf{a}$评估速度场差异
- 近似：$\log\frac{\pi_{new}}{\pi_{old}} \approx$ 两个策略沿插值路径的速度场差的积分
- 计算量：O(1)→比全路径快得多

### 布朗运动熵正则器

- 灵感：布朗运动→粒子扩散→熵单调增加
- 设计速度场使其模仿布朗运动的扩散性质→隐式促进熵增
- 不需要显式计算策略熵→避免散度积分
- 防止模式坍缩→鼓励多样探索

### PPO式裁剪目标
- 使用近似的重要性比率→标准PPO裁剪目标
- 加上布朗运动正则项
- 端到端训练→与标准PPO一样简单

## 实验关键数据

### MultiGoal(多模态动作分布)
| 方法 | 模式覆盖 | 回报 |
|------|---------|------|
| 高斯PPO | 单模态 | 低 |
| FPO | 部分多模态 | 中 |
| DPPO | 多模态(微调好) | 中 |
| **PolicyFlow** | **全多模态** | **最高** |

### IsaacLab/MuJoCo(连续控制)
- PolicyFlow ≥ 高斯PPO ≥ FPO/DPPO
- 特别在需要多样策略的任务上优势明显

### 关键发现
- 重要性比率近似的误差→实践中很小→不影响训练稳定性
- 布朗运动正则→与显式熵正则效果相当但计算成本低10x
- 从头训练(非微调)→PolicyFlow>DPPO→DPPO需要good初始策略
- FPO的不对称偏差→在某些任务上导致不稳定→PolicyFlow避免了

## 亮点与洞察
- **"不需要精确似然→只需似然比率"**：这个观察极其关键→绕过了CNF最大的计算瓶颈。
- **布朗运动→探索的物理隐喻**：粒子在液体中随机扩散→策略在动作空间中探索→物理与RL的优美对应。
- **多模态的实际价值**：MultiGoal结果→高斯策略只到一个目标→PolicyFlow到所有目标→在多solution任务中至关重要。
- **与扩散策略的对比**：DPPO=扩散+PPO但需要反传全链→PolicyFlow=CNF+PPO但只需插值路径→更轻量。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 重要性比率近似+布朗运动熵正则都是新颖设计
- 实验充分度: ⭐⭐⭐⭐ MultiGoal+IsaacLab+MuJoCo+消融
- 写作质量: ⭐⭐⭐⭐⭐ 物理直觉和数学推导结合excellent
- 价值: ⭐⭐⭐⭐⭐ 对表达性策略的在线RL有重要推动
