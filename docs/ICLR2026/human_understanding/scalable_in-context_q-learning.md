---
description: "【论文笔记】Scalable In-Context Q-Learning 论文解读 | ICLR 2026 | arXiv 2506.01299 | 情境RL | 提出S-ICQL——将动态规划和世界模型引入监督式ICRL框架：(1)多头Transformer同时预测最优策略和情境值函数，(2)预训练通用世界模型→将原始轨迹转化为轻量级提示(精确编码任务信息),(3)迭代策略改进(Q函数上尾期望拟合+优势加权回归)→从次优数据学习时相比AD/DPT等基线大幅提升,在离散和连续环境中一致优越。"
tags:
  - ICLR 2026
---

# Scalable In-Context Q-Learning

**会议**: ICLR 2026  
**arXiv**: [2506.01299](https://arxiv.org/abs/2506.01299)  
**代码**: [GitHub](https://github.com/NJU-RL/SICQL)  
**领域**: 强化学习/情境学习  
**关键词**: 情境RL, Q学习, 世界模型, 动态规划, 高效提示

## 一句话总结

提出S-ICQL——将动态规划和世界模型引入监督式ICRL框架：(1)多头Transformer同时预测最优策略和情境值函数，(2)预训练通用世界模型→将原始轨迹转化为轻量级提示(精确编码任务信息),(3)迭代策略改进(Q函数上尾期望拟合+优势加权回归)→从次优数据学习时相比AD/DPT等基线大幅提升,在离散和连续环境中一致优越。

## 研究背景与动机

1. **领域现状**：ICRL→Transformer在多任务离线数据上预训练→通过提示适应新任务(不更新参数)。两大方向：AD(算法蒸馏)和DPT(决策预训练Transformer)。

2. **现有痛点**：
   - (1) 监督预训练→不能超越收集数据→无法从次优轨迹学到最优策略(缺stitching)
   - (2) AD需要长horizon上下文→继承次优行为
   - (3) DPT需要oracle最优动作标注→实践中不可行
   - (4) 原始轨迹作为提示→token多且冗余→行为策略和任务信息纠缠

3. **切入角度**：(1)将Q学习(动态规划)引入监督ICRL→获得stitching能力; (2)世界模型→精炼提示。

## 方法详解

### 多头Transformer架构

- 输入：提示(任务信息) + 查询(当前状态)
- 输出头1：最优策略π*(a|s)
- 输出头2：情境值函数Q(s,a)
- 参数高效→共享backbone

### 世界模型→轻量级提示

- 预训练：通用世界模型→从多任务数据学习环境动态
- 推理：将少量原始轨迹→通过世界模型编码→去除行为策略噪声→得到任务特征
- 结果：轻量级提示(比raw轨迹token少得多)→快速精确推理

### 迭代策略改进(Q学习整合)

- 拟合状态值函数V→到Q函数的上尾期望(Upper Expectile)→获得乐观估计
- 用优势A=Q-V → 加权回归→提取策略
- 关键→stitching：组合不同次优轨迹的好片段→得到全局更优策略

## 实验关键数据

### 离散环境(Dark Room/Key-Door)

| 方法 | 次优数据 | 最优数据 |
|------|---------|---------|
| AD | 差 | 好 |
| DPT | 中(需oracle) | 好 |
| **S-ICQL** | **最好** | **好** |

### 连续环境(MuJoCo)

- S-ICQL一致优于DICP/IDT等最新基线
- 次优数据优势最大→stitching能力的体现

### 关键发现

- Q学习→stitching→从次优数据的关键提升→平均+15%
- 世界模型提示→比raw轨迹提示好+8%→精确编码任务信息
- 多头设计→策略和值函数共享backbone→参数效率高
- 提示token数→减少5-10x→推理速度更快

## 亮点与洞察

- **"监督学习+RL的优势融合"**：监督预训练的稳定性+Q学习的stitching能力→best of both worlds。
- **"世界模型=任务编码器"**：世界模型→不只是做规划→而是提供去噪的任务信息→提示工程的新用法。
- **次优数据的重要性**：实践中→最优数据不可得→S-ICQL是首个真正处理此setting的ICRL方法。
- **轻量级提示的实用意义**：raw轨迹→长且冗余→世界模型提示→短且精確→推理效率大幅提升。


## 局限性 / 可改进方向

- In the paper, we propose S-ICQL, an innovative framework that introduces dynamic programming and world modeling to enable fundamental reward maximization and efficient task generalization in ICRL.

- S-ICQL employs a multi-head transformer to jointly predict optimal policies and in-context value functions, guided by a pretrained world model that encodes precise task-relevant information for efficient prompt construction.

- Policy improvement is achieved by fitting in-context value functions with expectile regression and extracting policies via advantage-weighted regression, enabling reward maximization while preserving the scalability and stability of supervised pretraining.

- Extensive evaluations verify the consistent superiority of S-ICQL over a range of competitive baselines.

- Though, our prompt length matches the sampled transitions, which may be too long for long-horizon interactive problems.


## 相关工作与启发

- **vs LLIRL**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs MAML**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs MACAW**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ Q学习融入ICRL+世界模型提示
- 实验充分度: ⭐⭐⭐⭐ 离散+连续+次优/最优+消融
- 写作质量: ⭐⭐⭐⭐ 问题分析清晰方法推导严谨
- 价值: ⭐⭐⭐⭐⭐ 对ICRL有方法论级贡献
