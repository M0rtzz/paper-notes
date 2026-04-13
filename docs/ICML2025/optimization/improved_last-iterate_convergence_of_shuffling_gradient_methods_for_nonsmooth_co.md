---
title: >-
  [论文解读] Improved Last-Iterate Convergence of Shuffling Gradient Methods for Nonsmooth Convex Optimization
description: >-
  [ICML 2025][优化][shuffling gradient] 首次证明RR和SS在非光滑（强）凸有限和优化中，last-iterate收敛率严格优于Proximal GD，达到近似最优的O(1/(n^{1/4}sqrt(K)))，匹配下界。
tags:
  - ICML 2025
  - 优化
  - shuffling gradient
  - Random Reshuffle
  - last-iterate
  - nonsmooth convex
  - suffix average
---

# Improved Last-Iterate Convergence of Shuffling Gradient Methods for Nonsmooth Convex Optimization

**会议**: ICML 2025  
**arXiv**: [2505.23056](https://arxiv.org/abs/2505.23056)  
**代码**: 无  
**领域**: 优化  
**关键词**: shuffling gradient, Random Reshuffle, last-iterate, nonsmooth convex, suffix average

## 一句话总结
首次证明RR和SS在非光滑（强）凸有限和优化中，last-iterate收敛率严格优于Proximal GD，达到近似最优的O(1/(n^{1/4}sqrt(K)))，匹配下界。

## 研究背景与动机
**领域现状**: Shuffling方法（RR/SS/IG）是实践最常用的有限和优化算法。在光滑凸情况下已证明last-iterate收敛优于GD/SGD。
**现有痛点**: Liu & Zhou (2024b)建立了首个last-iterate结果，但非光滑情况下仅与Proximal GD相当（O(1/sqrt(K))），无法体现随机性优势。
**核心矛盾**: 非光滑性使标准分析技术（基于梯度Lipschitz性）失效。
**本文要解决什么**: 证明shuffling方法在非光滑情况下也严格快于Proximal GD。
**切入角度**: 利用RR/SS的排列结构结合新递推分析技巧。
**核心idea**: RR达到O(GD/(n^{1/4}sqrt(K)))的last-iterate速率，SS达到O(GD/(n^{1/4}K^{1/4}))，均优于O(GD/sqrt(K))。

## 方法详解

### 整体框架
优化 F(x) = f(x) + psi(x)，f = (1/n)sum f_i，f_i凸Lipschitz，psi可能mu-强凸。

### 关键设计
1. **RR的last-iterate (Thm 4.2)**: F(x_{Kn+1}) - F(x*) = O~(GD/(n^{1/4}sqrt(K)))。K=Omega(log n)时去掉多余对数。
2. **RR的suffix average (Cor 4.3)**: 同样达到O~(GD/(n^{1/4}sqrt(K)))——首个匹配Koren et al.下界的suffix average结果。
3. **SS的last-iterate (Thm 4.5/4.6)**: O~(GD/(n^{1/4}K^{1/4}) max GD/sqrt(n))。
4. **强凸情况 (Thm 4.4/4.7)**: RR达到O~(mu D^2/(n^2K^2) + G^2/(mu sqrt(n)K))，严格优于Proximal GD。

## 实验关键数据

### 速率对比

| 设定 | 方法 | 速率 |
|------|------|------|
| 凸 mu=0 | Proximal GD | O(GD/sqrt(K)) |
| 凸 mu=0 | **RR (本文)** | O~(GD/(n^{1/4}sqrt(K))) |
| 凸 mu=0 | **SS (本文)** | O~(GD/(n^{1/4}K^{1/4})) |
| 凸 mu=0 | 下界 (Koren) | Omega(1/(n^{1/4}sqrt(K))) |
| 强凸 | Proximal GD | O~(G^2/(mu K)) |
| 强凸 | **RR (本文)** | O~(G^2/(mu sqrt(n)K)) |

### 关键发现
- RR的last-iterate同时蕴含suffix average最优性——首次匹配下界
- n因子(n^{1/4}加速)精确反映每epoch遍历n个组件的优势
- SS弱于RR（K^{1/4} vs sqrt(K)），但仍严格优于GD
- 对数因子K=Omega(log n)时可消除

## 亮点与洞察
- **非光滑下shuffling严格优势**——终结了相关争论。随机排列优势来自每epoch内组件的均匀覆盖。
- **last-iterate蕴含suffix average最优性**——优雅的理论结果，说明last iterate分析足够精细。
- 分析技术可推广到其他非光滑有限和优化场景。

## 局限性 / 可改进方向
- 强凸情况RR速率是否最优仍为开放问题
- 未涉及IG（确定性排列）的非光滑分析
- 假设f_i凸且G-Lipschitz限制了对非凸deep learning的适用性
- 步长选择依赖参数先验知识
- 对数因子在某些regime下可能non-trivial

## 相关工作与启发
- **vs Liu & Zhou (2024b)**: 光滑时最优但非光滑仅达GD水平；本文填补非光滑gap
- **vs Koren et al. (2022)**: 下界和avg upper bound；本文last-iterate近似匹配
- **vs Mishchenko et al. (2020)**: 光滑强凸经典分析；本文推广到非光滑

## 评分
- 新颖性: ⭐⭐⭐⭐ 非光滑情况shuffling优于GD的首次证明
- 实验充分度: ⭐⭐ 纯理论
- 写作质量: ⭐⭐⭐⭐⭐ Table 1清晰全面
- 价值: ⭐⭐⭐⭐ 解决shuffling theory重要open问题
- 总体: ⭐⭐⭐⭐ 扎实的优化理论推进


## 补充分析

### 关键技术创新
本文的分析克服了两个核心技术困难：
- **非光滑性导致的梯度不连续**: 标准分析依赖梯度Lipschitz性来控制相邻迭代的目标函数变化。非光滑情况下需用次梯度技术。
- **排列依赖性**: RR中epoch内各步的梯度不独立。本文开发了新的递推不等式来处理这种相关性。
- **从epoch级到步级的分析**: 与现有work不同，本文在步级（而非仅epoch级）分析函数值变化，获得更精细的界。

### last-iterate vs average iterate的实践意义
- 实践中通常使用最后一个迭代点（last iterate），而非历史平均
- Average iterate需要额外存储或在线平均计算
- 本文证明last iterate已足够好，无需额外计算average
- Suffix average（最后一个epoch的平均）作为last iterate的近似也达到最优——提供了一个中间选择

### 与动量方法的关系
- 本文分析的是无动量的Proximal GD变体
- 加入Nesterov动量后，shuffling方法在光滑情况下已有加速版本
- 非光滑+动量+shuffling的组合分析是自然的后续方向

### 开放问题
- RR在非光滑强凸情况下的最优速率是什么？本文的 O~(G^2/(mu sqrt(n)K)) 是否可以进一步改进到 O(G^2/(mu n K))？
- IG（确定性排列）在非光滑情况下的行为如何？是否同样优于GD？
- 非光滑非凸有限和优化的shuffling分析是否可能？
- 自适应步长能否去除对参数(n,K,G,D)的先验知识依赖？
- 与方差减小方法(SVRG/SAGA)在非光滑情况下的比较如何？

- 分析非光滑情况下的mini-batch shuffling变体
