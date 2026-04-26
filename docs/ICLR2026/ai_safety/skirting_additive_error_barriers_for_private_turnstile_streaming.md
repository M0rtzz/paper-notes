---
title: >-
  [论文解读] Skirting Additive Error Barriers for Private Turnstile Streams
description: >-
  [AI安全] 本文证明了在差分隐私的 turnstile 流模型中，通过允许乘性误差（multiplicative error）可以绕过已知的多项式加性误差下界，将 distinct elements 和 F₂ 矩估计的加性误差从多项式级别降至 polylog(T)。
tags:
  - AI安全
---

# Skirting Additive Error Barriers for Private Turnstile Streams

## 基本信息

- **标题**: Skirting Additive Error Barriers for Private Turnstile Streams
- **作者**: Anders Aamand (BARC, University of Copenhagen), Justin Y. Chen (MIT), Sandeep Silwal (University of Wisconsin-Madison)
- **会议**: ICLR 2026
- **arXiv**: [2602.10360](https://arxiv.org/abs/2602.10360)
- **领域**: 差分隐私, 流算法, 连续发布

## 一句话总结

本文证明了在差分隐私的 turnstile 流模型中，通过允许乘性误差（multiplicative error）可以绕过已知的多项式加性误差下界，将 distinct elements 和 F₂ 矩估计的加性误差从多项式级别降至 polylog(T)。

## 研究背景与动机

### 问题设置
差分隐私连续发布（DP continual release）是隐私数据流处理的核心设置：数据逐个到达，算法需要在每个时间步私密地发布统计量。本文关注 **turnstile 流**模型（元素可以插入也可以删除），研究两个经典流统计量：

1. **Distinct Elements (不同元素计数)**：流中频率非零的元素个数
2. **F₂ 矩估计**：流中元素频率的平方和

### 已知下界与差距
- Distinct elements: 已知纯加性误差的下界为 Ω(T^{1/4})，最优上界为 Õ(T^{1/3})，两者之间存在多项式级别的差距
- F₂ 矩: 由灵敏度分析可知纯加性误差的下界为 Ω(T)，这意味着纯加性误差方案在实际中几乎不可用

### 核心洞察
作者观察到，已知的加性误差下界实例中，真实统计量本身就远大于加性误差。这暗示着：如果允许输出同时具有**乘性误差和加性误差**，就有可能绕过这些下界。这一思路在 insertion-only 流中已有先例（Epasto et al., NeurIPS '23），但 turnstile 流中尚属空白。

## 方法详解

### 误差定义
本文定义了 (α, β) 混合误差框架：对于统计量 Y_t，估计值 Ŷ_t 满足：

$$Y_t / p - r \leq \hat{Y}_t \leq q \cdot Y_t + s$$

其中 p·q = α（乘性因子），r + s = β（加性因子）。直觉上，当真实值 Y_t 远超噪声地板 β 时，算法给出接近 α 倍的近似。

### 算法一：MinHash 方法（Theorem 3.1, 严格 turnstile）

**核心思想**：利用最小哈希值估计集合大小的经典思想。

1. **桶化**：将哈希值按最低有效非零位（lsb）分桶，第 k 个桶包含 lsb(h(a)) = k 的元素，期望元素数按几何级数增长
2. **私密连续计数**：对每个桶维护一个 DP 连续计数器（基于高斯二叉树机制），加性误差 τ = O(log^{1.5}(T)/√ρ)
3. **估计**：找到满足计数器值 > τ 的最大桶索引 ℓ，输出 D̂ = 2^ℓ
4. **中位数放大**：运行 O(log T) 个独立副本取中位数，提升成功概率

**误差分析关键**：
- 桶太小不会被遗漏：当 D_t > 6τ 时，Chebyshev 不等式保证存在足够大的非空桶
- 桶太大时没有元素：空桶计数器值 ≤ τ，不会被误选
- 乘性误差来源：无法区分一个桶的高计数是来自τ个低频元素还是一个高频元素

**结果**：(O(log²(T)/√ρ), O(log²(T)/√ρ)) 误差，O(log n · log²(T)) 空间。

### 算法二：域缩减方法（Theorem 4.1, 一般 turnstile）

**核心思想**：通过哈希函数将高维域映射到低维，利用碰撞检测估计 distinct elements。

1. **域缩减**：对多种尺度 m = 2^i，将 [n] 映射到 [m]，同时用随机符号函数 g 处理频率
2. **反集中性（Lemma 4.1）**：当 m ≤ ‖x‖₀/ℓ 时，Erdős-Littlewood-Offord 界保证缩减后坐标值足够大（≥ √ℓ/1000）
3. **稀疏性（Lemma 4.2）**：当 m ≥ ℓ·‖x‖₀ 时，缩减后坐标几乎都为零
4. **阈值检测**：利用连续计数器检测哪些尺度下坐标值超过噪声阈值，从而估算 ‖x‖₀

**结果**：(O(log¹⁰(T)/ρ²), O(log¹⁰(T)/ρ²)) 误差，适用于一般 turnstile 流。

### 算法三：F₂ 矩估计（Theorem 5.1）

**核心思想**：Johnson-Lindenstrauss 降维 + 连续计数。

1. **JL 降维**：用 m × n 的 Rademacher 随机矩阵 A 将频率向量 x ∈ ℝⁿ 映射到 y = Ax ∈ ℝᵐ，保持 ‖y‖₂² ≈ ‖x‖₂²
2. **连续计数**：对降维后的每个坐标 y_t^i 维护连续计数器，每步更新量为 ±1/√m
3. **F₂ 估计**：输出 Σ(ŷ_t^i)² 作为 F₂ 的估计
4. **误差控制**：通过精细的误差分解（大坐标 vs 小坐标），将最终误差分为 JL 带来的乘性部分和计数器噪声带来的加性部分

**结果**：(1+η) 乘性 + O(log⁴(T)/(η³ρ)) 加性误差，O(log²(T)/η²) 空间。

## 实验

本文为理论工作，不含实验评估。以下两个表格总结了理论结果与已有工作的对比。

### 表1: Distinct Elements 问题的误差对比

| 来源 | 误差 (α, β) | 空间 | 隐私模型 | 备注 |
|------|-------------|------|----------|------|
| Jain et al. '23 | (1, Õ(T^{1/3})) | O(T) | Item-level | — |
| Cummings et al. '25 | (1+η, Õ(T^{1/3})) | Õ_η(T^{1/3}) | Event-level | — |
| Jain et al. '23 | (1, Ω̃(T^{1/4})) | — | Event-level | 下界 |
| Epasto et al. '23 | (1+η, O_η(log²(T))) | polylog(T) | Event-level | 仅 insertion-only |
| **Theorem 3.1 (本文)** | **(O(log²(T)), O(log²(T)))** | **O(log³(T))** | **Event-level** | **严格 turnstile** |
| **Theorem 4.1 (本文)** | **(O(log¹⁰(T)), O(log¹⁰(T)))** | **poly(T)** | **Event-level** | **一般 turnstile** |

### 表2: F₂ 矩估计问题的误差对比

| 来源 | 误差 (α, β) | 空间 | 隐私模型 | 备注 |
|------|-------------|------|----------|------|
| Epasto et al. '23 | (1+η, Õ_η(log⁷(T))) | O_η(log²(T)) | Event-level | 仅 insertion-only |
| Lemma 5.1 (本文) | (1, Ω(T)) | — | Event-level | 下界 |
| **Theorem 5.1 (本文)** | **(1+η, Õ_η(log⁴(T)))** | **O_η(log²(T))** | **Event-level** | **一般 turnstile** |

## 亮点

1. **概念突破**：首次系统性地证明了在 turnstile 流中，允许乘性误差可以完全绕过多项式加性误差下界，将加性误差降至 polylog(T)
2. **空间效率极高**：MinHash 算法仅需 polylog(n, T) 空间，与先前 polynomial 空间的算法形成鲜明对比
3. **统一范式**：所有算法的核心原语都是 DP 连续计数，通过不同的流式变换将目标问题归约到计数问题
4. **理论框架完整**：提出了 (α, β) 混合误差的规范定义，为后续研究提供了统一语言
5. **归约结果（Theorem 4.2）**：证明了纯加性误差 o(n) 的算法可以被提升为 (1+η) 乘性误差 + polylog 加性误差的算法，为未来改进指明方向

## 局限性

1. **仅限 event-level 隐私**：所有上界结果仅在 event-level DP 下成立；并发工作 [Aryanfard et al.] 表明相同结果在 item-level DP 下不可能实现（α·β 必须为 T^{1/3}）
2. **乘性误差为 polylog(T)**：对于 distinct elements，乘性误差为多对数级别而非常数，是否能实现常数乘性误差仍是开放问题
3. **两种算法各有局限**：MinHash 方法仅适用于严格 turnstile（频率非负），域缩减方法虽适用于一般 turnstile 但空间为多项式级别
4. **纯理论工作无实验**：缺乏实际数据上的实验验证，算法常数因子和实际性能未知
5. **对抗性模型受限**：假设非自适应对手（流独立于算法随机性），自适应对手下需要多项式空间

## 相关工作

- **DP 连续计数**: Dwork et al. 2010, Chan et al. 2011 提出二叉树机制；后续工作优化了常数因子和组合界
- **Insertion-only 流**: Epasto et al. 2023 在 insertion-only 模型中首先实现了 polylog 加性误差 + 乘性误差
- **Turnstile distinct elements**: Jain et al. 2023 建立了 Ω(T^{1/4}) 加性下界和 O(T^{1/3}) 上界；Henzinger et al. 2024 给出了依赖于 flippancy 的最优界
- **空间高效方案**: Cummings et al. 2025 实现了 Õ(T^{1/3}) 空间的方案但仍有多项式加性误差
- **混合误差范式**: Aamand et al. 2025, Ghazi et al. 2025 在其他 DP 问题中也利用乘性误差突破加性下界
- **并发工作**: Aryanfard et al. 2025（item-level 下界），Andersson et al. 2026（常数因子优化），Epasto et al. 2026（空间下界）

## 评分

- **新颖性**: 9/10 — 首次在 turnstile 流中实现 polylog 加性误差，概念贡献重大
- **技术深度**: 8/10 — MinHash + 连续计数、域缩减 + 反集中性、JL + 连续计数，三套技术路线各有巧妙之处
- **实用性**: 5/10 — 纯理论工作，polylog(T) 乘性误差在实际中偏大，缺乏实验
- **清晰度**: 8/10 — 结构清晰，动机阐述充分，开放问题讨论有价值
- **综合评分**: 8/10 — 在差分隐私流算法这一重要方向取得了显著的概念和技术突破

<!-- RELATED:START -->

## 相关论文

- [\[AAAI 2026\] Privacy Auditing of Multi-Domain Graph Pre-Trained Model under Membership Inference Attack](../../AAAI2026/ai_safety/privacy_auditing_of_multi-domain_graph_pre-trained_model_under_membership_infere.md)
- [\[AAAI 2026\] Robust Watermarking on Gradient Boosting Decision Trees](../../AAAI2026/ai_safety/robust_watermarking_on_gradient_boosting_decision_trees.md)
- [\[AAAI 2026\] Rethinking Target Label Conditioning in Adversarial Attacks: A 2D Tensor-Guided Generative Approach](../../AAAI2026/ai_safety/rethinking_target_label_conditioning_in_adversarial_attacks_a_2d_tensor-guided_g.md)
- [\[AAAI 2026\] ProbLog4Fairness: A Neurosymbolic Approach to Modeling and Mitigating Bias](../../AAAI2026/ai_safety/problog4fairness_a_neurosymbolic_approach_to_modeling_and_mitigating_bias.md)
- [\[AAAI 2026\] Learning to Collaborate: An Orchestrated-Decentralized Framework for Peer-to-Peer Collaborative Learning](../../AAAI2026/ai_safety/learning_to_collaborate_an_orchestrated-decentralized_framework_for_peer-to-peer.md)

<!-- RELATED:END -->
