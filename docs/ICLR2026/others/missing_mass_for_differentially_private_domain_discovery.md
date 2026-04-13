---
title: >-
  [论文解读] Missing Mass for Differentially Private Domain Discovery
description: >-
  [ICLR 2026][差分隐私] 为差分隐私域发现问题提供首批绝对效用保证——用缺失质量(recovered mass fraction)替代基数(unique items)度量,证明简单的加权高斯机制(WGM)在Zipf数据上有近最优ℓ1缺失质量保证且有分布无关的ℓ∞保证,并将WGM作为域发现前驱用于私有top-k和k-hitting set问题获得新效用保证,实验在6个真实数据集上验证。
tags:
  - ICLR 2026
  - 差分隐私
  - 集合并集
  - 缺失质量
  - Zipf数据
  - top-k
---

# Missing Mass for Differentially Private Domain Discovery

**会议**: ICLR 2026  
**arXiv**: [2603.14016](https://arxiv.org/abs/2603.14016)  
**代码**: 无  
**领域**: 差分隐私/集合发现  
**关键词**: 差分隐私, 集合并集, 缺失质量, Zipf数据, top-k

## 一句话总结
为差分隐私域发现问题提供首批绝对效用保证——用缺失质量(recovered mass fraction)替代基数(unique items)度量,证明简单的加权高斯机制(WGM)在Zipf数据上有近最优ℓ1缺失质量保证且有分布无关的ℓ∞保证,并将WGM作为域发现前驱用于私有top-k和k-hitting set问题获得新效用保证,实验在6个真实数据集上验证。

## 研究背景与动机

**领域现状**：隐私集合并集(DP set union)是工业DP框架的核心组件→每个用户有一组items→目标是在隐私保护下输出尽可能多的items。现有算法多但几乎无可证明的效用保证。

**现有痛点**：
   - (1) 现有效用保证都是相对的(相对于其他算法)→无绝对保证
   - (2) 基于基数的度量(发现了多少unique items)→不反映item重要性
   - (3) 扩展到top-k和k-hitting set时→域未知增加了难度

**切入角度**：从基数→缺失质量(未发现items的频率占比)→更有意义的度量→在此度量下证明WGM的保证。

## 方法详解

### 缺失质量度量

$$\text{MM}(W,S) = \sum_{x \in \bigcup_i W_i \setminus S} \frac{N(x)}{N}$$

- 0=完美(发现所有频繁items)→ 1=最差
- 比基数更有意义→高频items更重要

### 贡献1: Zipf数据的ℓ1缺失质量(Theorem 3.3)

- 假设频率满足Zipf律(N(r)∝r^{-α})→很现实
- WGM的缺失质量近最优
- 与数据规模和Zipf指数的精确关系

### 贡献2: 分布无关的ℓ∞缺失质量(Theorem 3.6)

- 不假设特定分布→对任意数据
- 界:最大单item缺失频率有限
- 更强但更松(因为无分布假设)

### 贡献3: Top-k和k-Hitting Set

**Top-k**(输出k个最频繁items):
- WGM发现域→已知域top-k算法→新效用保证(Theorem 4.3)

**k-Hitting Set**(输出k个items覆盖最多用户):
- 同样WGM+已知域算法→新保证(Theorem 4.5)
- 两者都利用Theorem 3.6提供的ℓ∞保证

## 实验关键数据

### 6个真实数据集
| 方法 | 集合并集MM | top-k质量 | k-hitting覆盖 |
|------|-----------|---------|------------|
| 之前SOTA | 基线 | 基线 | 基线 |
| **WGM-based** | **竞争力** | **更好** | **更好** |

### 关键发现
- WGM虽然简单→在缺失质量度量下非常有效
- 理论保证与实验结果吻合
- Top-k和k-hitting set→WGM前驱+后续算法→比端到端方法更好
- Zipf指数α影响保证的紧度→α越大(越集中)→保证越紧

## 亮点与洞察
- **"首批绝对效用保证"**：之前都是相对保证→本文对DP集合并集提供了真正的性能保证。
- **缺失质量度量的转变**：从"发现了多少unique"→"覆盖了多少mass"→更实际更有意义。
- **WGM的理论验证**：WGM是最简单的方法之一→本文证明它在正确度量下是近最优的→简单即powerful。
- **域发现作为前驱**：将集合并集定位为top-k/hitting set的第一步→模块化设计。

## 评分
- 新颖性: ⭐⭐⭐⭐ 缺失质量视角+首批绝对保证
- 实验充分度: ⭐⭐⭐⭐ 6个真实数据集+3个问题
- 写作质量: ⭐⭐⭐⭐⭐ 理论清晰严谨
- 价值: ⭐⭐⭐⭐ 对DP域发现理论有重要贡献
