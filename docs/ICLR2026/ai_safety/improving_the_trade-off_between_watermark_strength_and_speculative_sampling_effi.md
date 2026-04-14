---
title: >-
  [论文解读] Improving the Trade-off Between Watermark Strength and Speculative Sampling Efficiency for Language Models
description: >-
  [ICLR 2026][AI安全][水印] 将 LLM 水印强度从二值定义升级为连续量化（期望KL散度），完整刻画水印强度与speculative sampling效率的Pareto曲线，并提出伪随机接受机制使两者同时达到理论最大值。
tags:
  - ICLR 2026
  - AI安全
  - 水印
  - speculative sampling
  - KL散度
  - Pareto优化
  - 伪随机接受
---

# Improving the Trade-off Between Watermark Strength and Speculative Sampling Efficiency for Language Models

**会议**: ICLR 2026  
**arXiv**: [2602.01428](https://arxiv.org/abs/2602.01428)  
**代码**: https://github.com/hwq0726/watermark-tradeoff  
**领域**: AI安全 / LLM水印  
**关键词**: 水印, speculative sampling, KL散度, Pareto优化, 伪随机接受

## 一句话总结
将 LLM 水印强度从二值定义升级为连续量化（期望KL散度），完整刻画水印强度与speculative sampling效率的Pareto曲线，并提出伪随机接受机制使两者同时达到理论最大值。

## 研究背景与动机
LLM 水印通过微扰 token 采样分布嵌入可检测信号，是追踪生成内容来源的有力工具。水印方案通过伪随机数 ζ 将原始分布 P 修改为 P_ζ = S(P, ζ)，检测时测试 token 与 ζ 的统计依赖性。理想方案应同时满足：(1) 无偏性 E[P_ζ] = P；(2) 强水印信号（token 与 ζ 高度依赖）。

Speculative sampling 利用轻量 draft model 生成候选 token、大模型并行验证来加速推理。效率的关键是 acceptance rate——draft 分布 Q 与 target 分布 P 越接近，接受率越高。然而水印修改了分布，使 Q_ζ 与 P_ζ 的匹配变差。

Hu & Huang (2024) 证明两者存在根本性不可兼得：不可能同时保持最强水印和最高接受率。但其分析基于水印强度的二值定义（完全保持/不保持），忽略了连续中间状态。这留下了改进空间：也许通过精细的中间调控，可以在某些操作点同时做到近最优？

本文更进一步：不仅量化了连续trade-off，还证明通过改变随机性来源，可以完全消除这个看似根本的矛盾。

## 方法详解

### 整体框架
三步走：(1) 定义连续水印强度 WS = E_ζ[KL(P_ζ || P)]；(2) 将 trade-off 形式化为 Pareto 前沿；(3) 伪随机接受打破 trade-off。

### 关键设计

1. **水印强度量化 (Def 3.1)**：WS(P_ζ) = E_ζ[KL(P_ζ || P)] = I(w; ζ)（互信息）。Theorem 3.1 建立与检测 p-value 衰减率的精确联系：检测所需样本量 n ≥ (1/D̄)·log(1/α)。WS 越大，检测越容易。

2. **最大水印强度 (Thm 3.2)**：WS = Ent(P) - E_ζ[Ent(P_ζ)] ≤ Ent(P)。等号成立当且仅当 P_ζ 几乎处处退化为 Dirac 分布——即 token 是 ζ 的确定性函数。Gumbel-max 和 SynthID(m→∞) 均达到此上界。

3. **Trade-off Pareto 前沿 (Def 3.2)**：L(r) = max WS s.t. SSE ≥ r。对线性水印类 Q_ζ = (1-θ)Q + θS(Q,ζ)，问题化为求解凸优化。当 target decoder 退化时，约束简化为 γ ≥ γ_0 的单调条件。

4. **伪随机接受 (Algorithm 1)**：核心创新——acceptance 判断 u_{n+s} 从 U(0,1) 改为 G(ζ^R)。整个生成变为 (ζ^D, ζ^T, ζ^R) 的确定性函数。最终分布 P_ζ 退化（WS = Ent(P)），同时 SSE = 1 - TV(Q,P)（最高）。Two birds one stone.

### 损失函数 / 训练策略
无需额外训练。关键改动在推理阶段：将 acceptance 的真随机替换为确定性伪随机映射。伪随机数生成器 G 需要满足密码学安全要求。

## 实验关键数据

### 主实验
| 配置 | WS | SSE | 说明 |
|------|-----|-----|------|
| 标准 Speculative Sampling | 0 | 1-TV(Q,P) | 无水印 |
| Gumbel-max（无加速） | Ent(P) | N/A | 水印最强 |
| Hu & Huang 方案 | < Ent(P) | < 最优SSE | trade-off 次优 |
| Google's class | > Hu's class | 相同 r 下 | 曲线更优 |
| **Pseudorandom Acceptance** | **Ent(P)** | **1-TV(Q,P)** | **两者最优** |

### 消融实验
| 配置 | 关键指标 | 说明 |
|------|---------|------|
| SynthID m=30 | WS < Gumbel-max | 有限轮次WS不及 |
| SynthID m→∞ | WS = Gumbel-max = Ent(P) | 理论极限相同 |
| Linear class (θ∈[0,1], γ∈[0,1]) | 完整连续 Pareto 曲线 | 可精确计算 |
| 不同 (Q,P) 对 | 曲线形状变化 | Q与P越近→SSE上界越高 |

### 关键发现
- 伪随机接受不影响输出质量：最终 token 分布仍然无偏（E[P_ζ] = P 保持不变）。
- 机制可即插即用：适用于任意无偏水印方案（Gumbel-max、SynthID 等）。
- SynthID 在有限 m 下不如 Gumbel-max，因为 tournament sampling 未完全退化。
- 连续量化揭示了二值定义遗漏的丰富中间结构。

## 亮点与洞察
- "不可能定理"变成了连续 Pareto 刻画，并发现最优点其实是可达的——只要改变随机性来源。
- 洞察极度简洁优雅：让采样链所有随机性都来自可恢复伪随机数。
- 三个视角统一：信息论(互信息)、假设检验(p-value衰减)、优化(Pareto前沿)。

## 局限性 / 可改进方向
- 理论主要关注单 token，多 token 序列的联合分析更复杂。
- 伪随机数安全性（抗逆向工程）需独立评估。
- 实际部署中 draft model 质量对 SSE 的影响是分离的外部因素。
- 非无偏水印方案是否有类似结论未探讨。

## 相关工作与启发
- 与 Aaronson (2023) Gumbel-max、Google SynthID 构成统一理论框架。
- 为水印方案的实际部署（高效推理+可检测性）提供了理论最优策略。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 连续量化+打破trade-off，双重理论贡献
- 实验充分度: ⭐⭐⭐⭐ 理论驱动，实验验证清晰
- 写作质量: ⭐⭐⭐⭐⭐ 数学严谨，行文流畅
- 价值: ⭐⭐⭐⭐⭐ 为LLM水印部署提供最优方案
