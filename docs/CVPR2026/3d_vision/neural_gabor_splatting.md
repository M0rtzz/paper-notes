---
title: >-
  [论文解读] Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction
description: >-
  [CVPR 2026][3D视觉][高斯溅射] Neural Gabor Splatting 为每个高斯原语嵌入一个轻量级 MLP（SIREN 架构），使单个原语能表示复杂的空间变化颜色模式，配合频率感知致密化策略，在相同数据预算下显著提升高频表面重建质量。
tags:
  - CVPR 2026
  - 3D视觉
  - 高斯溅射
  - 高频表面重建
  - 神经纹理
  - MLP原语
  - 频率感知致密化
---

# Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction

**会议**: CVPR 2026  
**arXiv**: [2604.15941](https://arxiv.org/abs/2604.15941)  
**代码**: [https://github.com/haato-w/neural-gabor-splatting](https://github.com/haato-w/neural-gabor-splatting)  
**领域**: 3D视觉  
**关键词**: 高斯溅射, 高频表面重建, 神经纹理, MLP原语, 频率感知致密化

## 一句话总结

Neural Gabor Splatting 为每个高斯原语嵌入一个轻量级 MLP（SIREN 架构），使单个原语能表示复杂的空间变化颜色模式，配合频率感知致密化策略，在相同数据预算下显著提升高频表面重建质量。

## 研究背景与动机

**领域现状**：3D 高斯溅射（3DGS）因其显式点云表示的优势（快速训练、实时渲染、方便编辑）成为新视角合成的主流方法。但典型场景需要数十万到上百万个高斯原语，内存开销巨大。

**现有痛点**：每个高斯原语只能表示一种颜色（给定视角方向），当场景包含高频细节（如棋盘格纹理、毛发等频繁颜色跳变区域）时，需要大量原语来覆盖每个颜色变化，导致原语数量急剧增长。

**核心矛盾**：原语的表达能力受限是存储开销的根本原因。现有改进方案各有局限：3D Gabor Splatting 受限于 Gabor 噪声函数的性质，纹理化高斯受限于预设纹理分辨率。

**本文目标**：提升单个原语的表达能力，使其能用更少的原语实现更好的高频表面重建。

**切入角度**：受神经纹理/延迟渲染的启发，用一个小型 MLP 来参数化每个原语内部的颜色变化，使单个原语能表示任意复杂的局部图案。

**核心 idea**：为每个 2D 高斯原语嵌入一个独立的轻量级 SIREN MLP，输入局部坐标和视角方向，输出 RGB 颜色。SIREN 的正弦激活天然编码高频信号，无需额外的位置编码。

## 方法详解

### 整体框架

基于 2D 高斯溅射（2DGS），每个原语通过仿射变换将 3D 空间点映射到局部 2D 坐标 $(u, v)$。不再使用球谐系数表示颜色，而是将 $(u, v)$ 和视角方向 $\vec{d}$ 送入逐原语 MLP 得到 RGB。最终像素颜色通过 alpha 混合计算：$\mathbf{c} = \sum_k \hat{\boldsymbol{c}}_k(\Theta_k, u, v, \vec{d}) \alpha_k \hat{G}_k T_k$。

### 关键设计

1. **Neural Gabor 原语（Per-Primitive MLP）**:

    - 功能：让单个原语表示空间变化的、视角依赖的颜色
    - 核心思路：每个原语拥有独立的单隐层 SIREN MLP（6 个隐藏神经元）。输入为 5 维向量 $\mathbf{y} = (u, v, \vec{d})$，颜色预测为 $\hat{\boldsymbol{c}}_k = \text{Sigmoid}[\bar{\mathbf{W}}_k \sin\{\omega_0(\mathbf{W}_k \mathbf{y} + \boldsymbol{b}_k)\} + \bar{\boldsymbol{b}}_k]$，频率参数 $\omega_0 = 30$。SIREN 的正弦激活隐式执行位置编码，使网络能表示高频信号
    - 设计动机：与离散纹素相比，MLP 提供了连续、分辨率无关的表示。与固定基函数（球谐、Gabor）相比，MLP 可以学习任意复杂的颜色模式。每个原语独立参数使得精细建模成为可能

2. **频率感知致密化策略（Frequency-aware Densification）**:

    - 功能：控制原语数量增长，优先分配原语到高频缺失区域
    - 核心思路：不使用基于梯度的传统致密化，而是在频域计算渲染误差。对渲染图和 GT 分别做 FFT，提取特定频段（0.01-0.10, 0.10-0.20, 0.20-0.40）的分量做 IFFT 再局部平均，得到频域误差图。将逐像素误差反投影到原语空间，误差高的原语被选中进行克隆/分裂
    - 设计动机：基于梯度的致密化在 neural Gabor 原语上会导致过度致密化（因为 MLP 学到的颜色变化导致梯度大）。频域误差能针对性地在高频信息不足的区域增加原语

3. **渐进不透明度重置**:

    - 功能：稳定致密化过程中的原语管理
    - 核心思路：替换原始 3DGS 的硬不透明度重置为渐进式重置，对克隆/分裂的原语复制父级 MLP 权重并进行不透明度校正
    - 设计动机：硬重置可能导致 MLP 参数突然失效，渐进重置保持了训练的稳定性

### 损失函数 / 训练策略

标准的 $\lambda L_1 + (1-\lambda) L_{SSIM}$ 损失。MLP 权重按 SIREN 初始化方案初始化。每 100 次迭代随机采样 20 个训练视角作为 GPU 批次累积误差。致密化阈值 0.01。总训练 20k 迭代。

## 实验关键数据

### 主实验

| 方法 | High-Frequency PSNR/SSIM/LPIPS | Mip-NeRF360 PSNR/SSIM/LPIPS |
|------|-------------------------------|------------------------------|
| 3DGS* | 23.97/0.8335/0.2769 | 27.23/0.8005/0.2931 |
| 2DGS* | 23.91/0.8279/0.2855 | 26.47/0.7804/0.3197 |
| NEST | 22.22/0.8588/0.2220 | - |
| NTS | 23.48/0.8139/0.3026 | 29.49/0.9028/0.2544 |
| **Ours** | **26.49/0.8808/0.2115** | 26.98/0.810/0.2521 |

### 消融实验

| 致密化策略 | High-Frequency PSNR/SSIM/LPIPS |
|-----------|-------------------------------|
| 频率感知（本文） | 25.72/0.8619/0.2352 |
| 误差驱动 | 25.95/0.8619/0.2376 |
| 梯度驱动 | 25.56/0.8534/0.2464 |

### 关键发现

- 在 High-Frequency 数据集上 PSNR 提升 2.5+ dB（vs 2DGS），证明了 neural Gabor 原语在高频场景的巨大优势
- 相同数据预算下，neural Gabor 原语的视觉质量显著锐利，毛发、棋盘格等细节远优于标准方法
- 频率感知致密化与误差驱动致密化精度相当但提供了频段级的可控性
- 低预算场景（1%-5% 数据）下优势更明显，NEST 和 NTS 在严格预算下快速退化
- 训练时间约为 2DGS 的 2 倍，但与 NEST/NTS 的 neural splatting 方法相当

## 亮点与洞察

- **最小化 MLP 设计极致精简**：单隐层 6 神经元的 SIREN，参数量极小但通过正弦激活获得了强大的高频表达能力。这证明了"微型网络+正确的激活函数"的强大组合
- **频率感知致密化的可控性**：可以精确选择在哪个频段上分配更多原语，为存储受限场景提供了精细的质量-容量平衡工具
- **连续 vs 离散表示优势**：与纹理图方案相比，MLP 天然分辨率无关，不会出现纹理锯齿

## 局限与展望

- 每个原语独立 MLP 的 atomicAdd 操作增加了训练时间（约 2x）
- 不直接适用于体积现象（如雾、烟），扩展到动态场景也不平凡
- 对于低频场景 MLP 的表达能力可能未被充分利用，存在参数浪费
- 未来方向：参数共享或 codebook 压缩可进一步减少存储

## 相关工作与启发

- **vs 3D Gabor Splatting**: 3D Gabor 受限于 Gabor 噪声函数的固定形式，neural Gabor 用 MLP 表达更灵活
- **vs NTS/NEST**: 这些方法使用哈希网格或三平面编码，在低预算下表达能力有限；neural Gabor 在低预算下更鲁棒
- **vs 纹理化高斯**: 纹理方案受限于预设分辨率且有方向依赖性，MLP 连续且分辨率无关

## 评分

- 新颖性: ⭐⭐⭐⭐ 逐原语 MLP 的思路直观有效，频率感知致密化设计精巧
- 实验充分度: ⭐⭐⭐⭐ 多数据集对比全面，预算分析和消融详细
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰，数学公式完整
- 价值: ⭐⭐⭐⭐ 在存储受限的高频场景重建中提供了实用的解决方案

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] 3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction](3d_gaussian_splatting_with_self-constrained_priors_for_high_fidelity_surface_rec.md)
- [\[CVPR 2026\] HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity Animatable Face Avatars](hypergaussians_high-dimensional_gaussian_splatting_for_high-fidelity_animatable_.md)
- [\[CVPR 2026\] Neu-PiG: Neural Preconditioned Grids for Fast Dynamic Surface Reconstruction on Long Sequences](neu-pig_neural_preconditioned_grids_for_fast_dynamic_surface_reconstruction_on_l.md)
- [\[CVPR 2026\] Neural Field-Based 3D Surface Reconstruction of Microstructures from Multi-Detector Signals in Scanning Electron Microscopy](neural_field-based_3d_surface_reconstruction_of_microstructures_from_multi-detec.md)
- [\[AAAI 2026\] SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](../../AAAI2026/3d_vision/sparsesurf_sparse-view_3d_gaussian_splatting_for_surface_reconstruction.md)

<!-- RELATED:END -->
