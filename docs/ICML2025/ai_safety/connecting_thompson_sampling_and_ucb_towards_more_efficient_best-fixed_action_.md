---
title: >-
  [论文解读] Connecting Thompson Sampling and UCB: Towards More Efficient Trade-offs Between Privacy and Regret
description: >-
  [ICML2025][AI安全][Thompson Sampling] 本文提出 DP-TS-UCB 算法，通过限制每轮高斯采样次数并在采样预算耗尽后切换为 UCB 式探索，实现了隐私与遗憾的参数化权衡，将 GDP 保证从 $O(\sqrt{T})$ 大幅改善至 $\tilde{O}(T^{0.25(1-\alpha)})$，同时保持近最优的遗憾界。
tags:
  - ICML2025
  - AI安全
  - Thompson Sampling
  - UCB
  - 差分隐私
  - 随机赌臂问题
  - Gaussian DP
  - 隐私-遗憾权衡
---

# Connecting Thompson Sampling and UCB: Towards More Efficient Trade-offs Between Privacy and Regret

**会议**: ICML2025  
**arXiv**: [2505.02383](https://arxiv.org/abs/2505.02383)  
**代码**: 无  
**领域**: AI安全 / 差分隐私 / 在线学习  
**关键词**: Thompson Sampling, UCB, 差分隐私, 随机赌臂问题, Gaussian DP, 隐私-遗憾权衡

## 一句话总结

本文提出 DP-TS-UCB 算法，通过限制每轮高斯采样次数并在采样预算耗尽后切换为 UCB 式探索，实现了隐私与遗憾的参数化权衡，将 GDP 保证从 $O(\sqrt{T})$ 大幅改善至 $\tilde{O}(T^{0.25(1-\alpha)})$，同时保持近最优的遗憾界。

## 研究背景

### 领域现状

**领域现状**：差分隐私赌臂问题**：在线学习中既要平衡探索-利用，又要保护隐私（限制从拉臂序列推断个体信息）

### 核心矛盾

**核心矛盾**：Thompson Sampling 天然隐私**：TS-Gaussian 从后验分布采样模型时自然注入噪声，Ou et al. 2024 证明其满足 $O(\sqrt{T})$-GDP，但该界不紧

### 现有痛点

**现有痛点**：两个导致隐私损失的原因**：
  1. 每轮每臂都采样高斯模型 → 注入过多噪声
  2. 重复使用同一观测计算经验估计 → 隐私损失累积

### 解决思路

**解决思路**：核心观察**：一旦确信某臂次优，不需要继续高斯采样探索它

## 方法详解

### DP-TS-UCB 算法核心设计

**输入参数**：权衡参数 $\alpha \in [0,1]$，学习时域 $T$

**采样预算**：$\phi = c_0 T^{0.5(1-\alpha)} \ln^{0.5(3-\alpha)}(T)$

**两阶段机制**（对每个臂 $i$）：

1. **强制 TS-Gaussian 阶段**（$h_i \geq 1$）：
    - 从 $\mathcal{N}(\hat{\mu}_{i,n_i}, \ln^\alpha(T)/n_i)$ 采样新的模型 $\theta_i^{(h_i)}$
    - 预算递减 $h_i \leftarrow h_i - 1$
    - 记录最大值 $\text{MAX}_i \leftarrow \max(\text{MAX}_i, \theta_i^{(h_i)})$

2. **可选 UCB 阶段**（$h_i = 0$）：
    - 复用之前 $\phi$ 个模型中的最大值 $\text{MAX}_i$
    - 该最大值的行为等价于 UCB 中的上置信界

**臂特定 epoch 结构**：
- 第 $r$ 个 epoch 使用最近 $2^r$ 个观测更新经验均值
- 每个观测仅用一次 → 严格控制隐私损失
- epoch 结束时重置采样预算

### 关键引理

**引理 4.1（UCB 式充分探索）**：
$$\Pr\left\{\max_{h \in [\phi]} \theta_{i,s}^{(h)} \geq \mu_i\right\} \geq 1 - O(1/T)$$

$\phi$ 个高斯采样的最大值以高概率超过真实均值 → 等价于 UCB 的乐观性原则。

### 理论结果

**定理 4.2（遗憾界）**：
$$\sum_{i:\Delta_i>0} O\left(\frac{\ln(T^{0.5(3-\alpha)}\Delta_i^2)\ln^\alpha(T)}{\Delta_i}\right)$$

- $\alpha=0$：$\sum O(\ln(T^{1.5}\Delta_i^2)/\Delta_i)$，近最优
- $\alpha=1$：$\sum O(\ln(T\Delta_i^2)\ln(T)/\Delta_i)$，多一个 $\ln(T)$ 因子

**定理 4.4（GDP 保证）**：
$$\sqrt{2c_0 T^{0.5(1-\alpha)} \ln^{1.5(1-\alpha)}(T)}\text{-GDP}$$

- $\alpha=0$：$\tilde{O}(T^{0.25})$-GDP（比 TS-Gaussian 的 $O(\sqrt{T})$ 显著改善）
- $\alpha=1$：$O(1)$-GDP（常数隐私保证！增加 $T$ 不增加隐私损失）

**定理 4.6（转化为 (ε,δ)-DP）**：通过 GDP 对偶定理直接转化

### 隐私分析核心机制

1. 每个观测仅在一个 epoch 中被使用（epoch 结构）
2. 每个高斯分布最多采样 $\phi$ 个模型（采样预算）
3. UCB 阶段是 TS 阶段的后处理（post-processing 保持 DP）
4. 组合 TS + UCB 两阶段的 GDP：$\sqrt{\phi/\ln^\alpha(T)}$-GDP

## 实验

本文为理论贡献为主，实验验证在 Appendix 中。

### 与现有方法比较


### 主实验

| 方法 | 遗憾界 | GDP |
|------|--------|-----|
| TS-Gaussian | $O(K\ln(T\Delta^2)/\Delta)$ | $O(T^{0.5})$ |
| M-TS-G ($b,c=\ln^\alpha T$) | $O(K\ln^\alpha(T)\ln(T\Delta^2)/\Delta)$ | $O(T^{0.5}/\ln^\alpha T)$ |
| M-TS-G ($b,c=T^\gamma$) | $O(KT^\gamma\ln(T\Delta^2)/\Delta)$ | $O(T^{0.5-\gamma})$ |
| **DP-TS-UCB** ($\alpha=0$) | $O(K\ln(T^{1.5}\Delta^2)/\Delta)$ | $\tilde{O}(T^{0.25})$ |
| **DP-TS-UCB** ($\alpha=1$) | $O(K\ln(T\Delta^2)\ln T/\Delta)$ | $O(1)$ |

### 关键发现

- DP-TS-UCB 在相同遗憾级别下 GDP 界比 M-TS-Gaussian 显著更优
- M-TS-Gaussian 要达到 $O(T^{0.25})$-GDP 需设 $\gamma=0.25$，但遗憾界含 $T^{0.25}$ 因子（非 problem-dependent optimal）
- DP-TS-UCB 以 $\alpha$ 实现连续的隐私-遗憾 Pareto 前沿

## 亮点与洞察

- 🔥 揭示了 Thompson Sampling 与 UCB 的深层联系：高斯采样最大值 ≈ 上置信界
- 🔥 参数 $\alpha$ 实现隐私-遗憾的无缝权衡，从无隐私代价到常数隐私
- 🔥 $\alpha=1$ 时实现常数 GDP——增加时域 $T$ 不增加隐私损失，对长期部署极有价值
- 🔥 理论分析精巧：高斯分布反集中界 + epoch 结构 + GDP 组合定理
- 🔥 统一了两大经典框架（TS 和 UCB）的优势

## 局限

- 需要知道时域 $T$ 来计算采样预算 $\phi$（非 anytime 算法）
- problem-dependent 遗憾界中多了 $\ln\ln(T)$ 项，相比纯 TS 略有损失
- 未提供 minimax 遗憾下界的 GDP 版本对应
- epoch 结构丢弃了部分观测数据，可能在有限样本场景下影响实际表现

## 相关工作

- **DP 赌臂**：Sajed & Sheffet 2019, Hu et al. 2021, Azize & Basu 2022（(ε,0)-DP 最优算法）
- **Thompson Sampling 隐私**：Ou et al. 2024（TS-Gaussian 的 GDP 分析）
- **UCB**：Auer et al. 2002（UCB1）, Lattimore 2018
- **GDP**：Dong et al. 2022（高斯差分隐私框架）
- **下界**：Shariff & Sheffet 2018, Wang & Zhu 2024

## 评分

⭐⭐⭐⭐ (4/5)
- 理论优雅，将 TS 和 UCB 的联系转化为实用的隐私改善
- 参数化权衡设计灵活，$\alpha=1$ 的常数隐私结果具有重大实际意义
- 纯理论贡献，缺乏充分的实验对比

<!-- RELATED:START -->

## 相关论文

- [\[ICML 2025\] Empirical Privacy Variance](empirical_privacy_variance.md)
- [\[ICML 2025\] Clients Collaborate: Flexible Differentially Private Federated Learning with Guaranteed Improvement of Utility-Privacy Trade-off](clients_collaborate_flexible_differentially_private_federated_learning_with_guar.md)
- [\[ICML 2025\] Activation Space Interventions Can Be Transferred Between Large Language Models](activation_space_interventions_can_be_transferred_between_large_language_models.md)
- [\[ICML 2025\] On Differential Privacy for Adaptively Solving Search Problems via Sketching](on_differential_privacy_for_adaptively_solving_search_problems_via_sketching.md)
- [\[ICML 2025\] Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](cape_context-aware_prompt_perturbation_mechanism_with_differential_privacy.md)

<!-- RELATED:END -->
