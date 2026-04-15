---
title: >-
  [论文解读] MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training
description: >-
  [人体理解] 诊断出大 batch 训练语言模型时 AdamW/LAMB 导致 attention logit 最大值急剧增长（引发注意力分布坍塌为 one-hot）的问题，提出 MERIT 优化器——用 max-norm（而非 $\ell_2$-norm）计算 trust ratio 以更有效约束 query/key 权重极值，用行列级 element-wise trust ratio 捕捉局部权重结构、消除其他行列极端值的干扰。在 GPT-2 Medium 上实现 6k batch 无性能损失（对比标准 batch 480），且计算开销仅增加 1%。
tags:
  - 人体理解
---

# MERIT: Maximum-normalized Element-wise Ratio for Language Model Large-batch Training

| 项目 | 内容 |
|------|------|
| 会议 | ICML 2025 |
| 作者 | Yang Luo, Zangwei Zheng, Ziheng Qin, Zirui Zhu, Yong Liu, Yang You (NUS) |
| arXiv | [2508.20577](https://arxiv.org/abs/2508.20577) |
| 代码 | [GitHub](https://github.com/NUS-HPC-AI-Lab/MERIT) |
| 领域 | LLM 训练, 优化器设计 |
| 关键词 | large-batch training, optimizer, MERIT, trust ratio, max attention logit |

## 一句话总结

诊断出大 batch 训练语言模型时 AdamW/LAMB 导致 attention logit 最大值急剧增长（引发注意力分布坍塌为 one-hot）的问题，提出 MERIT 优化器——用 max-norm（而非 $\ell_2$-norm）计算 trust ratio 以更有效约束 query/key 权重极值，用行列级 element-wise trust ratio 捕捉局部权重结构、消除其他行列极端值的干扰。在 GPT-2 Medium 上实现 6k batch 无性能损失（对比标准 batch 480），且计算开销仅增加 1%。

## 研究背景与动机

**领域现状**：大 batch 训练是加速大语言模型训练的关键手段——通过数据并行减少训练时间。LAMB (You et al., 2020) 是目前最主流的大 batch 优化器，通过层级 trust ratio（权重 $\ell_2$ 范数 / 更新 $\ell_2$ 范数）自适应调节每层学习率。

**现有痛点**：随着 batch 增大，语言模型性能下降。本文发现根本原因是 **max attention logit 急剧增长**——注意力分数的最大值在大 batch 训练中远超小 batch 训练。这导致 softmax 输出退化为 one-hot 向量（注意力熵坍塌），限制了注意力层捕获全局信息的能力。

**核心矛盾**：大 batch 需要更高学习率来保持收益，但高学习率导致 query/key 权重极值增大 → max attention logit 增长 → 注意力坍塌。LAMB 通过 $\ell_2$-norm trust ratio 试图缓解，但 $\ell_2$ 范数与 max norm 之间存在巨大差距（相对差异达 0.99-0.996），使得 LAMB 无法有效约束权重矩阵的最大值。此外 LAMB 的层级 trust ratio 忽略了行列内部的相似性结构——一行中的极端值会通过全局 $\ell_2$ 范数影响其他行的更新稳定性。

**切入角度**：(1) Attention logit 上界直接与 $W_Q, W_K$ 的 max norm 相关：$\text{Logit}_{i,j} \leq d \cdot M_Q \cdot M_K \cdot C_X^2$（Appendix D 证明）；(2) 多头注意力和 outlier dimension 现象使得权重矩阵行列内部具有高度相似性。

**核心 idea 一句话**：用 max-norm trust ratio 直接约束 attention logit 增长的根源（Q/K 权重极值），用 element-wise trust ratio 利用行列内部相似性提供更精细的更新缩放。

## 方法详解

### 整体框架

MERIT 在 Adam 基础上引入三个修改：(1) max-norm 替代 $\ell_2$-norm 计算 trust ratio；(2) element-wise trust ratio 细粒度调节；(3) element-wise clipping 限制最大更新幅度为 1。

### 关键设计

1. **Maximum Normalized Trust Ratio**:

    - 功能：更有效地约束 Q/K 权重极值，从而控制 max attention logit
    - 核心思路：将 LAMB 的 trust ratio $R = \|w_t\| / \|u_t + \lambda w_t\|$ 中的 $\ell_2$-norm 替换为 max-norm（最大绝对值）。由于 attention logit 上界与 $M_Q \cdot M_K$ 成正比（Appendix D），而 $\ell_2$ 范数和 max norm 之间相对差异高达 99%+（图 10），$\ell_2$-norm 缩放无法有效抑制极端权重值。Max-norm 则直接对最大值元素施加最强的更新约束。
    - 设计动机：LAMB 在第 1 层注意力的 max attention logit 上成功降低，但中间层（第 12 层）仍然存在急剧增长（图 2b）。分析发现这些层正是 max norm 与 $\ell_2$ norm 差距最大的层。

2. **Element-wise Trust Ratio**:

    - 功能：利用行列内部权重相似性提供更精细的更新缩放
    - 核心思路：先计算行级 ratio $r^{(i)} = \|w^{(i)}\|_m / \|u^{(i)}\|_m$ 和列级 ratio $c^{(j)} = \|w^{(j)}\|_m / \|u^{(j)}\|_m$，然后取 $s^{(i,j)} = \max(r^{(i)}, c^{(j)})$。取最大值确保每个元素至少受到行和列两个方向中更保守的约束。同时用权重级（层级）trust ratio 作为下界，防止更新过小。
    - 设计动机：多头注意力导致行内权重相似（不同头共享投影），outlier dimension 导致列内权重相似（图 3 可视化）。LAMB 的层级 ratio 把所有行列混在一起——某一行的极端值通过全局 $\ell_2$ 范数影响其他行的更新，导致训练不稳定。Element-wise ratio 隔离了这种跨行列干扰。

3. **Element-wise Clipping**:

    - 功能：防止 element-wise ratio 导致个别元素更新过大
    - 核心思路：将更新后的参数变化量在每个维度上裁剪到 [-1, 1]——类似 SignSGD 的更新策略，但保留了梯度幅度信息。分析显示裁剪主要发生在中间层（第 6 层裁剪率峰值 12%），浅层和深层几乎不裁剪。
    - 设计动机：element-wise ratio 提供了更精细但也更不稳定的缩放，个别元素可能获得异常大的更新。Clipping 作为安全阀确保稳定性。

### 损失函数 / 训练策略

标准语言模型训练（next-token prediction）。收敛分析在 Theorem 1 中证明：对于 $\beta_1=0, \lambda=0$ 的简化版本（MERIT-W），在光滑性和有界梯度假设下，收敛速率为 $O(1/\sqrt{T})$。

## 实验关键数据

### 主实验——Chinchilla Scaling Law 设置的 GPT-2 预训练

| 模型 | Batch Size | AdamW | LAMB | Lion | Sophia-G | **MERIT** |
|------|-----------|-------|------|------|----------|-----------|
| GPT-2 Small (125M) | 1K | 3.470 | 3.355 | — | — | **3.280** |
| GPT-2 Medium (355M) | 4K | 3.172 | 3.068 | — | — | **2.982** |
| GPT-2 Large (770M) | 8K | 3.039 | 2.971 | — | — | **2.897** |

### 消融实验

| 消融内容 | GPT-2 Small Val Loss |
|---------|---------------------|
| MERIT（完整） | **3.280** |
| 去掉 element-wise clipping | ~3.32（性能下降） |
| 去掉 weight-wise ratio 下界 | ~3.35（性能下降明显） |
| 去掉 element-wise ratio（回退到 maxLAMB） | 3.304 |
| maxLAMB 与 LAMB 对比 | 3.304 vs 3.355（仅 norm 选择的改进有限） |

### 关键发现

- **Scaling law 优势**：MERIT 允许使用比 LAMB 和 AdamW 更大的 batch——从图 1 的 scaling law 曲线看，MERIT 的"ideal scaling"区间更宽。对于 GPT-2 Medium，MERIT 在 6k batch 下与 AdamW 在 480 batch 下性能持平（表 1）
- **收敛点曲率**：MERIT 的收敛点 Hessian 特征值更集中（top eigenvalue 12.326 vs AdamW 的 37.231，trace 3444.92 vs 12994.91）——收敛到更平坦的极小值，有利于泛化
- **计算开销极小**：相比 LAMB 仅增加 1% 的 FLOPS（表 2），max-norm 和 element-wise ratio 的计算成本可忽略
- **QK-Norm 是解决方案吗？**：虽然 QK-Norm 能提高 AdamW 的可用学习率，但在大 batch 训练中反而导致性能下降——它限制了注意力层的信息流通能力
- **跨架构验证**：在 Llama 架构上（130M: 3.199 vs LAMB 3.265；350M: 2.957 vs LAMB 3.001）同样有效

## 亮点与洞察

- 将大 batch 训练的性能下降归因于 max attention logit 增长是一个清晰且可行动的诊断——直接指向了 Q/K 权重极值问题，而非模糊的"泛化差距"
- Element-wise trust ratio 的设计巧妙利用了 Transformer 权重矩阵的结构先验（行相似性来自多头、列相似性来自 outlier dimensions），使细粒度 ratio 计算既有理论依据又实际可行
- MERIT 在计算开销仅增加 1% 的前提下实现显著的大 batch 训练改进——对于追求训练速度的工业场景极具吸引力

## 局限性

- 仅评估了 GPT-2 和 Llama 架构到 770M 参数规模——更大模型（7B+）和更大数据集上的效果未验证
- 收敛分析基于简化版本（$\beta_1 = 0, \lambda = 0$），完整 MERIT 的理论保证有待补充
- 未评估在 CV、RL 等其他领域的迁移效果——优化器设计中 max attention logit 的洞察是否通用？
- Element-wise ratio 引入了行/列级别的计算，虽然开销小但增加了实现复杂度
- 与 LAMB 使用相同的 $\beta$ 值，未专门为 MERIT 调优

## 相关工作与启发

- **vs LAMB (You et al., 2020)**：LAMB 的 $\ell_2$-norm trust ratio 是层级的、基于全局统计——适合 CNN（BatchNorm 和均匀权重）但不适合 Transformer 的异质权重结构。MERIT 用更精细的 max-norm + element-wise ratio 弥补了这一不足
- **vs σReparam (Zhai et al., 2023)**：他们用谱归一化解决 attention entropy collapse——与 MERIT 解决的问题一致但手段不同。σReparam 修改模型架构（需要重新训练），MERIT 修改优化器（即插即用）
- **vs Dehghani et al. (2023) — QK-Norm**：他们用 LayerNorm 归一化 Q/K 来稳定注意力。本文发现 QK-Norm 在大 batch 下反而有害——因为它过度限制了信息流，而 MERIT 只约束极端值不约束整体分布

## 评分

| 维度 | 分数 | 理由 |
|------|------|------|
| 新颖性 | ⭐⭐⭐⭐ | Max attention logit 诊断 + max-norm/element-wise ratio 设计原创且实用 |
| 技术深度 | ⭐⭐⭐⭐ | 理论分析（logit 上界、收敛证明）和实验分析（Hessian、clipping ratio）扎实 |
| 实验充分度 | ⭐⭐⭐⭐ | 三种规模 GPT-2 + Llama、多 baseline、详尽消融，但缺少 >1B 模型 |
| 写作质量 | ⭐⭐⭐⭐ | 问题定义清晰、图表丰富、消融系统化 |
| 实用性 | ⭐⭐⭐⭐⭐ | 1% 额外开销、即插即用、已开源——实用性极高 |
