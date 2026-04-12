---
title: >-
  [论文解读] Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training
description: >-
  [NeurIPS 2025][Schedule-Free优化] 从 River-Valley 损失景观的几何视角深入分析 Schedule-Free (SF) 优化器，揭示 SF-AdamW 在不需要学习率衰减或权重平均的情况下自动沿"河流"方向优化，并提出改进变体解决动量敏感性和大批量训练的局限性。
tags:
  - NeurIPS 2025
  - Schedule-Free优化
  - 学习率调度
  - River-Valley损失景观
  - Edge of Stability
  - 语言模型预训练
---

# Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training

**会议**: NeurIPS 2025  
**arXiv**: [2507.09846](https://arxiv.org/abs/2507.09846)  
**代码**: 未公开  
**领域**: llm_nlp  
**关键词**: Schedule-Free优化, 学习率调度, River-Valley损失景观, Edge of Stability, 语言模型预训练  

## 一句话总结

从 River-Valley 损失景观的几何视角深入分析 Schedule-Free (SF) 优化器，揭示 SF-AdamW 在不需要学习率衰减或权重平均的情况下自动沿"河流"方向优化，并提出改进变体解决动量敏感性和大批量训练的局限性。

## 研究背景与动机

随着模型和数据集规模快速增长，传统预训练策略（如 cosine 学习率调度）越来越不适用。主要替代方案存在各自问题：

1. **Warmup-Stable-Decay (WSD)**：灵活但依赖显式衰减阶段来评估进展
2. **权重平均（SWA/EWA）**：可替代衰减但引入额外内存开销（LLaMA-8B 需额外 16GB）

Schedule-Free (SF) 方法在多个任务表现出色（赢得 2024 AlgoPerf Challenge），但其成功原因和局限性缺乏理论理解。**核心问题**：是否存在既不需要学习率衰减、也不需要额外内存开销的优化方法？

## 方法详解

### 整体框架

研究分三个层次展开：
1. **经验观察**：SF-AdamW 自动沿 River 方向优化
2. **理论分析**：通过 Edge of Stability 和 Central Flow 解释机制
3. **改进方法**：提出解耦动量和平均的 Refined SF 变体

### 关键设计

**Schedule-Free 维护三个序列**：x_t（加权平均/输出迭代）、y_t（梯度评估点）、z_t（基础优化步）。x_t 是过去 y_t 的加权平均——SF 隐式地在不需要额外内存的情况下执行权重平均。

**River-Valley 损失景观视角**：损失景观分为 River 分量（低曲率进展方向）和 Hill 分量（偏离惩罚方向）。WSD 的稳定阶段沿 River 快速前进但在 Hill 方向震荡，衰减阶段拉回谷底。SF-AdamW 则自动紧贴 River。

**Edge of Stability 分析**：SF-GD 的稳定性阈值比标准 GD 放大了 1/(1-beta) 倍，允许使用更大学习率。y_t 的预条件化锐度在稳定性阈值附近均衡，展现典型 EoS 行为。

**Central Flow 分析**：y_t 的震荡方差随 beta_1 增大而减小，解释了较大 beta_1 使 y_t 更紧贴 River。

### 损失函数 / 训练策略

**改进的 SF 方法**：引入解耦参数 C，使 c_t = (1-beta)*C/t，让平均权重仅依赖 C，而 beta 独立控制 y_t 的动量。原始 SF 中 beta 同时控制动量和平均窗口——两者最优值可能不同。C 打破了这种耦合。

## 实验关键数据

### 主实验

使用 124M 参数 LLaMA 风格 Transformer，在 SlimPajama 6B token 子集上训练：

**SF-AdamW 的 River 跟踪能力**：

| 方法 | 衰减后额外收益 | EWA 额外收益 |
|------|----------------|-------------|
| AdamW (constant LR) | 显著下降（sharp drop） | 有收益 |
| SF-AdamW (constant LR) | **无额外收益** | **无额外收益** |

SF-AdamW 在恒定学习率下已达到接近最优的解。

**线性插值实验验证**（2B 和 2.5B token 检查点间）：
- AdamW (constant LR)：凸形——跨山谷震荡
- AdamW (decay LR)：单调 sharp 下降——从山壁走到谷底
- SF-AdamW (constant LR)：平坦缓慢下降——已在谷底

### 消融实验

**动量敏感性分析**：

| 方法配置 | 衰减后变化 | 跟踪 River? |
|---------|-----------|-----------|
| SF-AdamW, beta_1=0.95（最优） | 无变化 | 是 |
| SF-AdamW, beta_1=0.50 | sharp 下降 | 否 |
| SF-AdamW, beta_1=0.10 | sharp 下降 | 否 |

**Refined SF-AdamW 改进**：

| 场景 | vanilla SF | Refined SF (C=200) |
|------|-----------|-------------------|
| 动量非最优 (beta_1=0.1) | x_t 远差于 y_t | x_t 匹配或优于 y_t |
| 最优 (beta_1=0.95) | 良好 | 进一步降低验证损失 |
| 大批量 (2M tokens) | 落后于 cosine AdamW | 匹配 cosine AdamW |

### 关键发现

1. **y_t 比 x_t 更鲁棒**：即使动量非最优，y_t 仍然跟踪 River，但 x_t 可能偏离
2. **y_t 的 EWA 在所有设置下表现最好**——但需要额外内存
3. **C 参数广泛鲁棒**：在最优和非最优 beta_1 下，Refined SF 一致优于 vanilla

## 亮点与洞察

1. **几何直觉优雅**：River-Valley 视角将复杂优化动态简化为直观的"沿河流前进 vs 爬山壁"
2. **理论-实践完美闭环**：EoS + Central Flow 理论精确预测了实验观察，并指导改进
3. **根本性洞察**：SF 隐式实现权重平均但不需要额外内存——优于 WSD 和 SWA 的关键
4. **实用改进**：C 参数解耦设计简单有效，解决了 SF 两大痛点

## 局限性 / 可改进方向

1. **仅在小规模模型上验证**：124M 参数，未扩展到更大模型
2. **理论分析依赖简化假设**：Central Flow 近似的严格验证尚未完成
3. **未与最新优化器对比**：如 SOAP、Muon 等
4. **大批量设置仅初步探索**：C=200 仅是单次 sweep 结果
5. **multi-phase 训练未涉及**：如 DeepSeek-V3 的复杂多阶段流程

## 相关工作与启发

- **WSD** 及其几何解释（Wen et al., 2025）提供了核心对比框架
- **Edge of Stability**（Cohen et al., 2021）和 **Central Flow**（Cohen et al., 2025）提供理论工具
- **原始 Schedule-Free 方法**（Defazio et al., 2024）是本文分析和改进的基础
- 对实际 LLM 预训练的直接启发：SF-AdamW + C 去耦可能是 cosine/WSD 的更好替代

## 评分

- **创新性**: ⭐⭐⭐⭐ — River-Valley 视角下对 SF 的深入分析和 C 去耦改进
- **技术深度**: ⭐⭐⭐⭐⭐ — EoS 理论、Central Flow 推导、Toy Model + 实际训练验证极其扎实
- **实验质量**: ⭐⭐⭐ — 实验在小规模模型上充分但缺乏大规模验证
- **实用性**: ⭐⭐⭐⭐ — 对 LLM 预训练优化器选择有直接指导意义
- **总体评分**: ⭐⭐⭐⭐ (8/10)
