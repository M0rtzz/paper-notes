---
title: >-
  [论文解读] Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space
description: >-
  [AAAI 2026][自监督学习][Knowledge Tracing] 提出 L-HAKT 框架，利用 LLM 双 Agent（Teacher + Student）生成合成数据，在双曲空间中进行对比对齐，将知识点的树状层级结构显式建模到知识追踪中。
tags:
  - AAAI 2026
  - 自监督学习
  - Knowledge Tracing
  - LLM Agent
  - Hyperbolic Space
  - 对比学习
  - 教育智能
---

# Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space

**会议**: AAAI 2026  
**arXiv**: [2602.22879](https://arxiv.org/abs/2602.22879)  
**代码**: 待确认  
**领域**: self_supervised  
**关键词**: Knowledge Tracing, LLM Agent, Hyperbolic Space, Contrastive Learning, 教育智能  

## 一句话总结

提出 L-HAKT 框架，利用 LLM 双 Agent（Teacher + Student）生成合成数据，在双曲空间中进行对比对齐，将知识点的树状层级结构显式建模到知识追踪中。

## 背景与动机

知识追踪 (KT) 通过分析学生历史交互预测未来答题表现。现有方法存在三大不足：(1) 传统方法在欧几里得空间建模，无法表达知识体系的树状层级结构；(2) 题目间通过知识概念的隐式拓扑关系未被有效捕获；(3) 学生个体掌握程度会扭曲题目难度感知——低水平学生将中等题判为高难度，高水平者反之。

## 核心问题

如何利用 LLM 挖掘题目语义中的知识层级结构，并在保持层级感知的同时对齐 LLM 生成的通用认知与真实学生的个性化动态认知？

## 方法详解

### 整体框架

L-HAKT 由三部分组成：LLM 双 Agent 数据增强 → 双曲图神经网络编码 → 双曲对比对齐 + 知识追踪。

### 关键设计

**Teacher Agent**：解析题目图像为文本 $q_i^{text} = M_t(q_i^{image})$，执行三项任务：(1) 提取知识点并分 4 级层级 $L_j \in \{1,2,3,4\}$；(2) 基于层级关系构建知识图谱；(3) 量化题目难度。

**Student Agent**：模拟学生答题认知过程，包含两个模块：
- 认知投入模块：$\Gamma_j = \sigma(W_q \cdot [X_{q_i}; X_{c_{ij}}; t] + b_q)$
- 层级遗忘模块：$F_j = \exp(-\lambda \cdot L_{avg} \cdot t_j)$，基础/中等/困难知识遗忘曲线斜率不同
- 知识状态更新：$h_j^s = \text{LSTM}([X_{q_j}; \sum w_c X_c] \oplus (\Gamma_j \odot F_j \odot h_{j-1}^s))$

**双曲图注意力网络**：分别在真实图和合成图上定义曲率 $\kappa_{real}$、$\kappa_{syn}$，通过指数/对数映射在双曲流形上聚合：
$$h_i^{(L+1)} = \exp_0^\kappa\Big(\sigma\big(\sum_{j \in \mathcal{N}_i} \alpha_{ij}^{(L)} W^{(L)} \log_0^\kappa(h_j^{(L)})\big)\Big)$$

**双曲对比对齐**：正样本为两空间共享的题目-知识点对，负样本为其余实体，损失：
$$\mathcal{L}_{con} = -\sum_{(u,v) \in \mathcal{P}} \log \frac{pos(h_u, h_v)}{pos(h_u, h_v) + neg(h_u)}$$

总损失：$\mathcal{L}_{total} = \mathcal{L}_{KT} + \alpha \mathcal{L}_{con}$

## 实验关键数据

| 模型 | ASSIST09 AUC | ASSIST12 AUC | EdNet AUC | Eedi AUC |
|------|-------------|-------------|-----------|----------|
| DKT | 75.97 | 72.90 | 70.10 | 76.01 |
| AKT | 78.23 | 78.21 | 76.78 | 78.84 |
| MIKT | 79.38 | 78.65 | 77.10 | 79.59 |
| **L-HAKT** | **80.22** | **80.27** | **78.23** | **80.29** |

- 在 4 个数据集上 AUC 和 ACC 均取得最优
- 消融实验：去掉双曲空间（w/o hyp）AUC 下降 1-2%，去掉对比学习（w/o con）下降更多

## 亮点

- 首个将 LLM 双 Agent 协作框架引入知识追踪，补充传统数据缺失的"学生思维路径"
- 利用双曲空间的指数膨胀特性自然编码知识点的树状层级
- 通过曲率优化实现层级感知的对齐，不同深度知识点在不同曲率区域

## 局限性

- LLM Agent 生成质量依赖 prompt 设计，不同 LLM 效果可能差异大
- 双曲空间操作（指数/对数映射）增加训练复杂度
- 4 级知识层级划分较为粗糙，实际知识体系更复杂
- 缺少对 LLM Agent 生成数据质量的定量评估

## 对比

与 AKT、MIKT 等 SOTA 方法相比，L-HAKT 在四个数据集上 AUC 平均提升 ~1%。关键优势在于双曲空间建模和 LLM 数据增强的结合，而非单纯的序列建模改进。

## 启发

- LLM 作为 "Teacher" 构建知识图谱 + "Student" 模拟行为的双 Agent 范式可推广到其他教育 AI 任务
- 双曲空间在具有天然层级结构的任务中有显著优势
- 合成数据与真实数据的对比对齐思路值得借鉴

## 评分

⭐⭐⭐⭐ — 方法新颖，LLM+双曲空间的组合有创意，实验全面但改进幅度有限
