---
title: >-
  [论文解读] Symmetry-Aware GFlowNets
description: >-
   揭示GFlowNets中图对称性导致的系统性采样偏差，提出通过自同构群大小缩放奖励的简单修正方法SA-GFN，实现无偏采样。
tags:

---

# Symmetry-Aware GFlowNets

## 元信息
- **会议**: ICML 2025
- **arXiv**: [2506.02685](https://arxiv.org/abs/2506.02685)
- **代码**: [GitHub](https://github.com/hohyun312/sagfn)
- **领域**: 生成模型 / 图生成
- **关键词**: GFlowNets, 图对称性, 自同构群, 等价动作, 分子生成

## 一句话总结
揭示GFlowNets中图对称性导致的系统性采样偏差，提出通过自同构群大小缩放奖励的简单修正方法SA-GFN，实现无偏采样。

## 研究背景与动机
- GFlowNets通过序列动作构建组合对象（如分子图），使采样概率正比于奖励
- **等价动作问题**：不同动作可能产生同构图（如在对称节点上添加新节点），其概率需累加
- 不处理等价动作会引入系统偏差：节点生成偏向低对称图，片段生成偏向高对称组件
- ZINC250k中超50%分子有多于1个对称性——偏差对分子设计影响严重

## 方法详解

### 核心理论

**等价动作分析**
- 轨道等价：同一轨道上的动作产生同构图（Theorem 4.3）
- 自同构群比例引理：$\frac{|\text{Orb}(G,u,v)|}{|\text{Orb}(G',u,v)|} = \frac{|\text{Aut}(G)|}{|\text{Aut}(G')|}$

**自同构修正定理（Theorem 4.6）**
$$\frac{p_{\bar{\mathcal{A}}}(a|s)}{q_{\bar{\mathcal{A}}}(a|s')} = \frac{|\text{Aut}(G)|}{|\text{Aut}(G')|} \cdot \frac{p_\mathcal{E}(G'|G)}{q_\mathcal{E}(G|G')}$$

### 修正方法——奖励缩放

**TB目标修正（Corollary 5.1）**
$$\mathcal{L}_{\text{TB}}(\tau) = \left(\log \frac{Z\prod p_\mathcal{E}(G_{t+1}|G_t)}{|\text{Aut}(G_n)|R(G_n)\prod q_\mathcal{E}(G_t|G_{t+1})}\right)^2$$

只需将奖励乘以终态自同构群大小：$\tilde{R}(G) = |\text{Aut}(G)| \cdot R(G)$

**片段修正（Theorem 5.3）**
$$\tilde{R}(G) = \frac{|\text{Aut}(G)| R(G)}{\prod_{i=1}^k |\text{Aut}(C_i)|}$$

### 无偏似然估计
$$\bar{p}_\mathcal{A}(x) \approx \frac{1}{M|\text{Aut}(G_n)|}\sum_{i=1}^M \frac{p_\mathcal{E}(\tau_i)}{q_\mathcal{E}(\tau_i|G_n)}$$

## 实验

### 合成图（72296个终态）
| 方法 | TB L1误差 |
|------|----------|
| Vanilla | 高，收敛差 |
| PE (近似) | 中等改善 |
| Reward Scaling | 接近精确修正 |
| Transition Correction | 精确（但计算昂贵）|

### 分子生成
| 生成方式 | 方法 | Diversity↑ | Top-K Reward↑ |
|---------|------|-----------|---------------|
| Atom | Vanilla | 0.929 | 1.09 |
| Atom | Reward Scaling | **0.959** | **1.091** |
| Fragment | Vanilla | 0.877 | 0.941 |
| Fragment | Reward Scaling | **0.879** | **0.952** |

Vanilla在片段生成中过度偏好环己烷（5220次 vs 修正后1042次）。

## 亮点
- 理论清晰：将等价动作问题归结为自同构群大小的简单奖励缩放
- 实现简单：仅需在轨迹末端计算一次自同构群，而非每步检测
- 同时适用于TB和DB目标、原子和片段生成
- 计算开销极小（bliss算法高效）

## 局限性
- 理论保证依赖于预定义图动作集的具体结构
- GNN表达能力有限可能使不同轨道节点获得相同表示
- 主要在分子生成上验证，其他类型图生成的效果待验证
- 奖励结构影响修正效果（如奖励与对称性负相关时改善有限）

## 评分
⭐⭐⭐⭐ 识别问题精准、解决方案优雅简洁，将复杂的等价动作问题化简为奖励缩放，理论贡献突出。
