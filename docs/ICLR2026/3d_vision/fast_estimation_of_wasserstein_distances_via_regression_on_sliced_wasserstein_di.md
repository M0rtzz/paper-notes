---
description: "【论文笔记】Fast Estimation of Wasserstein Distances via Regression on Sliced Wasserstein Distances 论文解读 | ICLR 2026 | arXiv 2509.20508 | Wasserstein距离 | 提出通过将 Wasserstein 距离回归到 Sliced Wasserstein (SW) 距离的线性模型（RG 框架），实现对 Wasserstein 距离的快速高效估计，在低数据场景下显著优于深度学习方法 Wasserstein Wormhole。"
tags:
  - ICLR 2026
---

# Fast Estimation of Wasserstein Distances via Regression on Sliced Wasserstein Distances

**会议**: ICLR 2026  
**arXiv**: [2509.20508](https://arxiv.org/abs/2509.20508)  
**代码**: [有](https://github.com/hainn2803/Regression-Wasserstein)  
**领域**: 3D视觉  
**关键词**: Wasserstein距离, Sliced Wasserstein, 最优传输, 线性回归, 点云分类

## 一句话总结

提出通过将 Wasserstein 距离回归到 Sliced Wasserstein (SW) 距离的线性模型（RG 框架），实现对 Wasserstein 距离的快速高效估计，在低数据场景下显著优于深度学习方法 Wasserstein Wormhole。

## 研究背景与动机

Wasserstein 距离是衡量分布间差异的重要工具，在生成模型、计算生物学、3D 点云处理等领域广泛应用。然而其计算复杂度为 O(n^3 log n)，严重限制大规模应用。

**现有加速方案的不足**：

1. **Sinkhorn 正则化**：通过熵正则化加速，但引入近似误差
2. **深度学习方法**（如 Wasserstein Wormhole）：用 Transformer 学习嵌入空间，但需大量训练数据，低数据场景性能差
3. **Sliced Wasserstein（SW）**：投影到 1D 计算（O(n log n)），但只是 Wasserstein 的下界，精度不足

**核心洞察**：SW 距离提供下界，lifted SW 距离提供上界。可以将真实 Wasserstein 距离用这些上下界进行线性回归来高效估计。

## 方法详解

### 整体框架

RG（Regression）框架的核心思想：将 Wasserstein 距离作为因变量，各种 SW 距离变体作为自变量，建立线性回归模型。训练仅需少量分布对的精确 Wasserstein 距离，训练后可用于任意分布对的快速估计。

### 关键设计

**（1）SW 距离变体作为预测因子**

下界类（1D 投影后的 Wasserstein）：

- **SW**（Sliced Wasserstein）：均匀采样投影方向的期望
- **Max-SW**：最大化投影距离的方向
- **EBSW**（Energy-Based SW）：用能量函数加权的投影方向

上界类（利用 lifted transportation plan）：

- **PW**（Projected Wasserstein）：均匀采样方向的 lifted cost 期望
- **Min-SWGG**：最小化 lifted cost 的方向
- **EST**（Expected Sliced Transport）：能量加权的 lifted cost

关键数学关系：SW <= EBSW <= Max-SW <= W(真实) <= Min-SWGG <= EST <= PW

**（2）无约束线性模型**

给定 K 种 SW 距离变体，回归模型为：

W_p(mu, nu) = sum_{k=1}^K omega_k * S_p^(k)(mu, nu) + epsilon

最小二乘估计有闭式解：omega_LSE = (S^T S)^{-1} S^T W

**（3）约束线性模型**

利用上下界先验，将每对上下界组合为加权平均，约束 0 <= omega_k <= 1，参数量减半。K=1 时有闭式解。

**（4）Few-Shot 估计策略**

从 N 对分布中采样 M << N 对，计算精确 Wasserstein 用于训练。训练后仅需计算 SW 距离即可快速预测。

**具体模型实例**：

- RG-o：Max-SW + Min-SWGG
- RG-s：SW + PW
- RG-e：EBSW + EST
- RG-se：SW + EBSW + PW + EST
- RG-seo：全部 6 种变体

### 损失函数 / 训练策略

- 最小二乘损失（MSE），闭式解无需迭代
- 约束模型通过二次规划求解
- 总复杂度远低于全量 Wasserstein 计算
- RG-Wormhole：将 Wormhole 中所有 Wasserstein 计算替换为 RG 代理，保留其嵌入、插值、重建能力

## 实验关键数据

### 主实验：ShapeNetV2 点云 k-NN 分类

| 方法 | R^2 | k=1 | k=3 | k=5 | k=10 |
|------|-----|------|------|------|------|
| WD（精确） | - | 83.6% | 83.5% | 84.2% | 82.9% |
| SW | - | 72.2% | - | - | - |
| RG-s | 0.868 | 82.1% | 81.7% | 80.8% | 79.4% |
| RG-seo | 0.937 | 82.8% | 83.3% | **83.5%** | 82.3% |

### 低数据场景对比 Wormhole（M0=100）

| 方法 | MNIST R^2 | ShapeNetV2 R^2 | MERFISH R^2 | scRNA-seq R^2 |
|------|-----------|----------------|-------------|---------------|
| Wormhole | 0.28 | 0.65 | -3.6 | 0.04 |
| RG-s（约束） | 0.84 | 0.88 | 0.91 | 1.00 |
| RG-e（约束） | 0.86 | 0.90 | 0.92 | 1.00 |
| RG-se（无约束） | **0.93** | **0.95** | **0.98** | **1.00** |

### 消融实验

- **约束 vs 无约束**：无约束模型数据充足时更强，约束模型极少数据时收敛更快
- **RG-Wormhole**：训练速度大幅提升（batch size 增大时 Wormhole 近指数增长，RG-Wormhole 几乎持平），嵌入质量和重建误差与原版几乎一致

### 关键发现

1. **低数据碾压**：仅需 10-100 对分布训练，RG 在所有数据集上大幅领先 Wormhole（R^2 0.28 vs 0.93）
2. **接近精确 Wasserstein**：RG-seo 在 ShapeNetV2 分类上达 83.5%，精确 WD 为 84.2%
3. **跨维度鲁棒**：从 2D（MNIST）到 2500D（scRNA-seq）均有效
4. **RG-Wormhole 加速显著**：保留全部功能的同时大幅缩短训练时间

## 亮点与洞察

- **极简但有效**：线性模型 + 闭式解，无需神经网络，概念清晰
- **理论驱动**：利用 SW 的上下界关系构建约束模型，比纯数据驱动更高效
- **兼容连续与离散分布**：不像深度方法仅限于经验分布
- **即插即用的 RG-Wormhole**：保留所有功能，仅替换距离计算

## 局限性 / 可改进方向

1. **线性假设**：SW 与 Wasserstein 的关系可能非线性，核方法可能更优
2. **元分布假设**：需要训练与测试分布来自同一元分布
3. **不生成嵌入空间**：纯 RG 框架无法进行插值，需与 Wormhole 结合
4. **投影方向数量 L 的选择**：对不同数据集可能需要调整

## 相关工作与启发

- **Wasserstein Wormhole**：Transformer 学习分布嵌入，RG 在低数据场景完胜
- **Sinkhorn 距离**：熵正则化加速 OT
- **启发**：上下界回归的思路可推广到其他计算昂贵的距离度量

## 评分

- 新颖性：4/5 - 巧妙利用 SW 上下界构建回归框架
- 技术深度：4/5 - 严谨的数学推导和理论保证
- 实验完整度：5/5 - 跨维度、跨任务全面验证
- 实用价值：5/5 - 即插即用加速方案，工程友好
