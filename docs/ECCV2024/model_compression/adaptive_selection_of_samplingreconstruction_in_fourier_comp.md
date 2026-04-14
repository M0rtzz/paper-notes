---
title: >-
  [论文解读] Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing
description: >-
  [ECCV 2024][模型压缩][傅里叶压缩感知] 提出自适应选择采样-重建框架 $\mathcal{H}_{1.5}$，为每个输入数据自适应选择最佳的采样mask与专用重建网络对，利用超分辨率空间生成模型量化高频不确定性实现选择，理论证明优于非自适应联合优化 $\mathcal{H}_1$ 和自适应采样 $\mathcal{H}_2$。
tags:
  - ECCV 2024
  - 模型压缩
  - 傅里叶压缩感知
  - 自适应采样
  - Pareto最优
  - 贝叶斯不确定性
  - 超分辨率
---

# Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing

**会议**: ECCV 2024  
**arXiv**: [2409.11738](https://arxiv.org/abs/2409.11738)  
**代码**: [smhongok.github.io/ada-sel.html](https://smhongok.github.io/ada-sel.html)  
**领域**: 压缩感知 / MRI重建  
**关键词**: 傅里叶压缩感知, 自适应采样, Pareto最优, 贝叶斯不确定性, 超分辨率

## 一句话总结
提出自适应选择采样-重建框架 $\mathcal{H}_{1.5}$，为每个输入数据自适应选择最佳的采样mask与专用重建网络对，利用超分辨率空间生成模型量化高频不确定性实现选择，理论证明优于非自适应联合优化 $\mathcal{H}_1$ 和自适应采样 $\mathcal{H}_2$。

## 研究背景与动机
**领域现状**：傅里叶压缩感知（Fourier CS）通过欠采样k空间数据大幅加速MRI等成像，深度学习重建已远超传统 $l_1$ 优化。核心挑战是：给定采样预算，如何最优地分配采样位置？

**现有痛点**：(1) 联合优化采样-重建 $\mathcal{H}_1$：mask不自适应于每个数据点，且需要在离散空间做反向传播（straight-through estimator）；(2) 自适应采样 $\mathcal{H}_2$：mask生成器 $\pi_\phi$ 的离散空间优化困难，且单一重建网络 $\theta$ 面对多种mask是Pareto次优——类似于一个盲降噪网络不如专用降噪网络。

**核心矛盾**：既要自适应于每个输入，又要为每种采样mask配备专用最优重建网络——但自适应采样 $\mathcal{H}_2$ 中这两个目标冲突。

**切入角度**：不去生成mask（避免离散空间优化），而是从预定义的J个mask-网络对中选择一个——兼得自适应性和Pareto最优性。

## 方法详解

### 整体框架
$\mathcal{H}_{1.5}$ 框架定义为：$h = \sum_{j=1}^J e_\psi(\cdot)_j \cdot h(\cdot; M_j, \theta_j)$，其中 $e_\psi: M_0\mathcal{K} \to \{e_j\}_{j=1}^J$ 是选择器（输出one-hot向量），每个submodel $(M_j, \theta_j)$ 是固定mask+专用重建网络对。训练时：(1) 对所有训练数据用SR模型量化高频不确定性；(2) k-means++聚类不确定性模式为J类；(3) 基于每类中心构建采样mask $M_j$；(4) 独立训练每个专用网络 $\theta_j$。

### 关键设计
1. **理论保证：自适应选择优于两端（Theorems 3.1 & 3.2）**:
    - 功能：证明 $\mathcal{H}_{1.5}$ 的true risk下确界不高于 $\mathcal{H}_1$ 和 $\mathcal{H}_2$
    - 核心思路：Theorem 3.1（$\inf_{h \in \mathcal{H}_{1.5}} \mathcal{L}[h] \leq \inf_{h \in \mathcal{H}_1} \mathcal{L}[h]$）因 $\mathcal{H}_1 \subseteq \mathcal{H}_{1.5}$；Theorem 3.2证明在 $|\pi_\phi(M_0\mathcal{K})| \leq J$ 条件下 $\mathcal{H}_{1.5}$ 也优于 $\mathcal{H}_2$——因为专用 $\theta_j$ 是Pareto最优的
    - 设计动机：$\mathcal{H}_1$ 的mask不自适应，$\mathcal{H}_2$ 的 $\theta$ 是Pareto次优。$\mathcal{H}_{1.5}$ 两个问题都解决

2. **高频贝叶斯不确定性量化（mask selector $e_\psi$）**:
    - 功能：用超分辨率空间生成模型量化每个输入的高频不确定性分布
    - 核心思路：先采样低频k空间 $M_0 k$，用SR flow模型 $f_\psi$ 生成 $S$ 个高分辨率样本，计算样本方差 $v(M_0 k) = (\hat{\text{Var}}_{q_\psi}[k'_s])_{s=1}^S$ 作为高频不确定性估计，归一化后 $u = v/\|v\|_2$ 用k-means++聚类。推理时计算 $u$ 到各聚类中心的距离选择最近类对应的 $(M_j, \theta_j)$
    - 设计动机：SR模型的样本方差天然估计了k空间MSE；不同图像的高频不确定性模式不同（如横纹背景vs长发——不确定性分布方向不同），需要不同的采样策略

3. **采样mask构建与专用网络训练**:
    - 功能：从聚类中心构建mask并训练专用重建网络
    - 核心思路：直接排序样本方差可最优化PSNR（Proposition 1），但对SSIM需要引入随机性。因此用rejection sampling按中心 $c_j$ 概率采样生成mask $M_j$，再独立训练 $\theta_j$ 最小化 $\hat{\mathcal{L}}[h(\cdot; M_j, \theta_j)]$
    - 设计动机：每个 $\theta_j$ 只为一个 $M_j$ 训练，保证Pareto最优——避免了 $\mathcal{H}_2$ 中单网络多mask的性能瓶颈

### 损失函数 / 训练策略
每个重建网络 $\theta_j$ 独立用 $1-\text{SSIM}$ 损失训练（U-Net或E2E-VarNet架构），默认 $J=3$ 个mask-网络对，SR flow模型用conditional normalizing flow在低频重建图像上训练。

## 实验关键数据

### 主实验（SSIM↑）
| 方法 | CelebA 8× | CelebA 16× | CS-MRI 2D 4× | CS-MRI 1D 4× | CS-MRI 1D 8× |
|------|-----------|-----------|--------------|-------------|-------------|
| Random ($\mathcal{H}_1$) | 0.8378 | 0.8684 | 0.9663 | 0.9533 | 0.9255 |
| VD ($\mathcal{H}_1$) | 0.9073 | 0.8734 | 0.9698 | 0.9603 | 0.9367 |
| LOUPE ($\mathcal{H}_1$) | 0.8742 | 0.8673 | 0.9671 | 0.9541 | 0.9218 |
| Policy ($\mathcal{H}_2$) | 0.8501 | 0.8394 | 0.9698 | 0.9569 | 0.9240 |
| **Ours ($\mathcal{H}_{1.5}$)** | **0.9405** | **0.8952** | **0.9704** | **0.9624** | **0.9407** |

### 消融实验（CS-MRI 8×，J的影响）
| J | 平均SSIM | 最低5% SSIM | 最低10% SSIM |
|---|---------|------------|-------------|
| 1 | baseline | baseline | baseline |
| 2 | +显著提升 | +提升 | +提升 |
| 3 | +趋于平稳 | +继续提升 | +继续提升 |
| 4 | ≈J=3 | +最佳 | +最佳 |

### 关键发现
- CelebA 8×上SSIM提升0.033（0.9073→0.9405），在图像重建中是巨大提升
- CS-MRI 1D 8×上SSIM提升0.004（0.9367→0.9407），在MRI重建中也是显著差异
- $J$增大时平均SSIM趋于平稳，但outlier性能持续改善——更多segment提供更强鲁棒性
- SR生成模型的不确定性量化有效：Sorted-Self PSNR>Sorted-Another>VD

## 亮点与洞察
- 框架定位精准："segmented regression"类比清晰——既利用了自适应性又保证了Pareto最优
- 避免了离散空间反向传播这一长期痛点——选择器只需要计算距离，无需梯度
- SR空间生成模型作为不确定性量化工具的巧妙复用，无需额外训练新模型
- Remark 2（J的trade-off）提供了实用的选择指导

## 局限性 / 可改进方向
- SR模型本身的训练和推理有额外开销（S次采样换取不确定性估计）
- J=3-4个submodel意味着3-4倍的存储和训练开销
- 仅在face图像和脑部MRI上验证，其他成像模态（如膝关节MRI、CT）效果未知
- k-means++聚类假设不确定性模式可以被球形cluster良好分离

## 相关工作与启发
- **vs LOUPE (MedIA 2020)**: 学习非自适应mask，CelebA 8× SSIM 0.8742远低于本文0.9405
- **vs Policy-based (MedIA 2022)**: 自适应但Pareto次优，CelebA 8× SSIM 0.8501最低
- **vs Pineda et al. (2020)**: 用cGAN量化不确定性做贪心自适应采样，但仍面临单网络多mask问题
- 启示：在采样-重建联合优化中，"选择"比"生成"更高效——避免了离散优化的根本困难

## 评分
- 新颖性: ⭐⭐⭐⭐ 框架设计巧妙，理论保证实在，SR不确定性量化复用创新
- 实验充分度: ⭐⭐⭐⭐ 人脸+多线圈MRI、1D+2D采样、消融充分
- 写作质量: ⭐⭐⭐⭐⭐ 问题层次（$\mathcal{H}_1$→$\mathcal{H}_2$→$\mathcal{H}_{1.5}$）定义清晰，理论和实验紧密配合
- 价值: ⭐⭐⭐⭐ 对CS-MRI采样优化有理论和实践贡献
