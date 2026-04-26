---
title: >-
  [论文解读] SGI: Structured 2D Gaussians for Efficient and Compact Large Image Representation
description: >-
  [CVPR 2026][3D视觉][2D高斯溅射] 提出 SGI，通过种子点（seed）组织非结构化 2D 高斯基元并用轻量 MLP 解码属性，配合上下文模型驱动的熵编码和多尺度拟合策略，实现高分辨率图像表征中最多 7.5× 压缩和 6.5× 加速，同时保持或提升保真度。
tags:
  - CVPR 2026
  - 3D视觉
  - 2D高斯溅射
  - 图像表征
  - 结构化高斯
  - 熵编码
  - 多尺度拟合
---

# SGI: Structured 2D Gaussians for Efficient and Compact Large Image Representation

**会议**: CVPR 2026  
**arXiv**: [2603.07789](https://arxiv.org/abs/2603.07789)  
**代码**: [https://github.com/zx-pan/SGI](https://github.com/zx-pan/SGI)  
**领域**: 模型压缩 / 图像表征  
**关键词**: 2D高斯溅射, 图像表征, 结构化高斯, 熵编码, 多尺度拟合

## 一句话总结

提出 SGI，通过种子点（seed）组织非结构化 2D 高斯基元并用轻量 MLP 解码属性，配合上下文模型驱动的熵编码和多尺度拟合策略，实现高分辨率图像表征中最多 7.5× 压缩和 6.5× 加速，同时保持或提升保真度。

## 研究背景与动机

1. **领域现状**：2D 高斯溅射已成为新的图像表征技术，支持在低端设备上高效渲染。但扩展到高分辨率需要百万级非结构化高斯基元，导致收敛慢和参数冗余。
2. **现有痛点**：GaussianImage 等方法独立优化每个高斯，未利用空间局部性（相邻像素通常共享相似颜色和纹理），导致相邻基元间大量参数冗余。
3. **核心矛盾**：3D 场景中 anchor-based 方法（如 Scaffold-GS）能有效压缩，但直接迁移到 2D 因已去除的参数（如不透明度）而压缩效果有限（仅约 3%）。
4. **本文目标**：为高分辨率图像设计紧凑且高效的 2D 高斯表征。
5. **切入角度**：引入种子点组织高斯基元，并在种子级别进行熵编码以进一步压缩。
6. **核心 idea**：种子点 + 共享 MLP → 结构化高斯 → 熵编码去除剩余冗余 → 多尺度拟合加速优化。

## 方法详解

### 整体框架

(1) 种子点均匀覆盖图像，每个种子关联 $K$ 个高斯基元，两个共享 MLP 解码颜色和协方差；(2) 上下文模型+二值化哈希网格估计种子属性分布进行熵编码；(3) 多尺度拟合从粗到精渐进优化。

### 关键设计

1. **种子基2D神经高斯**:

    - 功能：将非结构化高斯组织为紧凑的种子级表征
    - 核心思路：每个种子位于 $x_a$ 处，关联属性 $\mathcal{A} = \{f_a, s_o, s_a, \delta\}$（特征向量、偏移缩放、尺度缩放、$K$ 个偏移量）。高斯位置由 $\mu^{(k)} = x_a + \delta^{(k)} \cdot s_o$ 计算。两个共享 MLP $\text{MLP}_c$ 和 $\text{MLP}_\Sigma$ 从 $f_a$ 解码颜色和协方差。每个高斯仅需 8 个参数。
    - 设计动机：通过共享 MLP 和种子级特征向量利用空间局部性，大幅减少参数量。

2. **上下文模型驱动的熵编码**:

    - 功能：进一步压缩种子属性的剩余空间冗余
    - 核心思路：可学习二值化哈希网格 $\mathcal{H}$ 编码种子的空间一致性。上下文 MLP 从哈希特征预测每个种子属性分量的均值 $\mu_j^{(i)}$ 和标准差 $\sigma_j^{(i)}$，用于算术编码。训练时用均匀噪声注入模拟量化，量化步长通过可学习精炼因子调整。
    - 设计动机：种子基表征引入的结构规律性使得属性分布可建模，实现有效压缩。仅种子化不足（约 3% 压缩），必须结合熵编码。

3. **多尺度拟合策略**:

    - 功能：加速优化并提升稳定性
    - 核心思路：构建高斯金字塔 $\{I_0=I, I_1, ..., I_{M-1}\}$，从最粗层开始优化，将优化结果作为下一层的初始化（位置和尺度按 2× 缩放）。固定总迭代次数，层间递进。
    - 设计动机：直接在全分辨率上优化收敛慢且不稳定，尤其加上量化感知训练和概率建模的开销。粗到精的热启动显著加速。

### 损失函数 / 训练策略

$L = L_{\text{img}} + \frac{\lambda}{N \cdot d_{\mathcal{A}}} (L_{\text{entropy}} + L_{\text{hash}})$。$\lambda=0.001$，$M=3$ 层金字塔，15000 步优化。

## 实验关键数据

### 主实验

| 方法 | FGF2 PSNR↑ | 大小(MB)↓ | 优化时间(min)↓ |
|------|-----------|----------|-------------|
| SGI (低码率, 3.5M) | 31.24 | 16.33 | 48.43 |
| GaussianImage | 27.30 | 23.37 | 322.17 |
| LIG | 32.10 | 106.81 | 87.56 |
| SGI (高码率, 10M) | 36.27 | 41.74 | 97.75 |
| 3DGS | 34.93 | 787.73 | 642.85 |

### 消融实验

| 配置 | FGF2 PSNR | 大小 | 说明 |
|------|-----------|------|------|
| λ=0 (无熵编码) | 32.36 | 104.08 | 种子化几乎不压缩 |
| λ=0.001 | 31.24 | 16.33 | 6.4× 压缩 |
| K=5 | 31.29 | 18.48 | 少高斯每种子 |
| K=10 (默认) | 31.24 | 16.33 | 质量-紧凑平衡 |
| M=1 (无多尺度) | 30.58 | - | 71.59 min |
| M=3 (默认) | 31.24 | - | 48.43 min |

### 关键发现

- 仅用种子化压缩约 3%，熵编码是核心——将 104MB 压缩到 16MB
- 多尺度拟合不仅加速 32%（71→48 min）还提升 PSNR 0.66 dB
- 特征空间 KNN 在低码率下优于 JPEG（PSNR +3.3 dB @ 0.245 bpp）
- K=10 是最佳平衡点，过多高斯增大 MLP 和特征维度

## 亮点与洞察

- **种子+MLP 的参数共享**：将非结构化高斯转化为结构化表征，使熵编码成为可能
- **熵编码是关键**：不同于 3D 场景中 anchor 化即可大幅压缩，2D 场景必须显式熵建模
- **多尺度拟合的双重收益**：既加速又提升质量，因为粗层提供良好初始化

## 局限与展望

- 种子数 $N$ 和每种子高斯数 $K$ 均为固定超参数，未实现内容自适应
- 当前用均匀噪声模拟量化，更高级的 QAT 技术可能进一步提升
- 仅在单图像表征上验证，视频扩展值得探索

## 相关工作与启发

- **vs GaussianImage**: GaussianImage 独立优化每个高斯无结构化，SGI 引入种子和熵编码大幅减小模型
- **vs LIG**: LIG 用层级高斯做残差拟合，SGI 用全量多尺度拟合+熵编码实现更好压缩

## 评分

- 新颖性: ⭐⭐⭐⭐ 种子级熵编码是2D高斯表征压缩的首次尝试
- 实验充分度: ⭐⭐⭐⭐⭐ 三个数据集域+全面消融+与压缩基线对比
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图表丰富
- 价值: ⭐⭐⭐⭐ 为高分辨率图像的紧凑表征提供了有效方案

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] MAGICIAN: Efficient Long-Term Planning with Imagined Gaussians for Active Mapping](magician_efficient_long-term_planning_with_imagined_gaussians_for_active_mapping.md)
- [\[CVPR 2026\] LumiMotion: Improving Gaussian Relighting with Scene Dynamics](lumimotion_gaussian_relighting_dynamics.md)
- [\[CVPR 2026\] CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](crowdgaussian_reconstructing_high-fidelity_3d_gaussians_for_human_crowd_from_a_s.md)
- [\[CVPR 2026\] CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](cghair_compact_gaussian_hair_reconstruction_with_card_clustering.md)
- [\[CVPR 2026\] SwiftTailor: Efficient 3D Garment Generation with Geometry Image Representation](swifttailor_efficient_3d_garment_generation_with_geometry_image_representation.md)

<!-- RELATED:END -->
