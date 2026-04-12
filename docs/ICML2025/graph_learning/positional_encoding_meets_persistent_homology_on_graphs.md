---
title: >-
  [论文解读] Positional Encoding meets Persistent Homology on Graphs
description: >-
  [ICML2025][图学习][位置编码] 理论证明位置编码（PE）和持续同调（PH）互不可比——各存在对方失败但自身成功的图构造，提出 PiPE 方法统一两者，可证明比单独使用更具表达力，在分子/分类/OOD任务上表现优异。
tags:
  - ICML2025
  - 图学习
  - 位置编码
  - 持续同调
  - 图表达力
  - 图神经网络
  - 拓扑数据分析
---

# Positional Encoding meets Persistent Homology on Graphs

**会议**: ICML2025  
**arXiv**: [2506.05814](https://arxiv.org/abs/2506.05814)  
**代码**: [PiPE](https://github.com/Aalto-QuML/PIPE)  
**领域**: graph_learning  
**关键词**: 位置编码, 持续同调, 图表达力, GNN, 拓扑数据分析

## 一句话总结

理论证明位置编码（PE）和持续同调（PH）互不可比——各存在对方失败但自身成功的图构造，提出 PiPE 方法统一两者，可证明比单独使用更具表达力，在分子/分类/OOD任务上表现优异。

## 研究背景与动机

- **MP-GNN 局限**：至多 1-WL 表达力，无法捕获连通性/环等结构
- **PE 方法**：谱方法（Laplacian 特征向量）/ 随机游走距离等，增强位置感知
- **PH 方法**：多分辨率拓扑特征（连通分量/独立环的持续性）
- **关键问题**：PE 和 PH 谁更强？能否统一？

## 方法详解

### 理论核心结果

1. **PE 失败但 PH 成功**的图构造：存在 PE 无法区分但 PH 可区分的图对
2. **PH 失败但 PE 成功**的图构造：存在 PH 无法区分但 PE 可区分的图对
3. **结论**：PE 和 PH 互不可比（incomparable）

### PiPE（Persistence-informed Positional Encoding）

- 将 PH 特征（持续图/Betti 数等）注入可学习 PE 框架
- 通过消息传递网络统一 PE 和 PH
- **可证明比单独 PE 或 PH 更具表达力**
- 实现：将持续特征作为节点附加特征，通过额外 GNN 层传播

### 与 k-WL 层次的关系

- PiPE 的表达力分析置于 k-WL 层次框架中
- PiPE 可区分 1-WL 和 3-WL 之间的某些图对

### 灵活性与实用性

- PiPE 可基于任何现有 PE 方法（LSPE/SignNet/SPE 等）
- 仅增加少量参数（PH 特征提取 + 一层 GNN）
- 预计算 PH 特征后推理无额外开销

## 实验关键数据

### 分子属性预测（ZINC/OGB-Mol）

- PiPE 在多数指标上优于纯 PE 或纯 PH 方法

### 图分类

- 合成树任务：PiPE 完美区分 PE/PH 各自失败的案例
- 真实数据集：一致提升

### OOD 泛化

- PiPE 在分布偏移场景下更鲁棒
- 拓扑特征提供了对图大小/密度变化更稳定的表示

### 消融

- 仅 PE / 仅 PH / PE+PH（PiPE）：PiPE 一致最优
- 不同 PE 基础方法（LSPE/SignNet/SPE）上的一致提升
- PH 过滤函数选择（sublevel/superlevel/Rips）对结果有轻微影响

## 亮点与洞察

1. **首次严格的 PE vs PH 不可比性证明**
2. PiPE 的统一框架理论优雅实用
3. 可即插即用增强任何 PE 方法
4. 将拓扑数据分析与图学习连接

## 局限性 / 可改进方向

- PH 计算（尤其高维持续同调）开销较大，可能限制大规模图应用
- 仅考虑 0/1 维拓扑特征（连通分量和独立环），高维持续同调（如空腔）未探索
- 对大规模图的可扩展性需验证
- PiPE 的消息传递层数选择对性能有影响
- 不同过滤函数（sublevel vs superlevel）的选择可能影响结果

## 相关工作与启发

- Horn et al. (2022)：PH 增强 GNN 表达力的开创性工作
- Dwivedi et al. (2022) LSPE：可学习位置编码
- Lim et al. (2023) SignNet/BasisNet：处理特征向量符号歧义
- Huang et al. (2024) SPE：稳定位置编码
- Immonen et al. (2023)：PH 在分子属性预测的应用
- 启发：不同增强范式的互补性值得在更多任务中进一步探索

## 评分

⭐⭐⭐⭐⭐ — 理论优雅（不可比性证明+统一框架），实验全面覆盖多个任务，对图表示学习的表达力研究有深远影响

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
