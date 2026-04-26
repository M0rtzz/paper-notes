---
title: >-
  [论文解读] SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering
description: >-
  [CVPR 2026][3D视觉][逆渲染] SGS-Intrinsic 提出两阶段室内逆渲染框架，第一阶段利用语义和几何先验构建稠密几何一致的高斯场，第二阶段结合混合光照模型和材质先验进行材质-光照分解，并通过去阴影模块防止阴影烘焙到反照率中。
tags:
  - CVPR 2026
  - 3D视觉
  - 逆渲染
  - 稀疏视图
  - 高斯溅射
  - 材质分解
  - 室内场景
---

# SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering

**会议**: CVPR 2026  
**arXiv**: [2603.27516](https://arxiv.org/abs/2603.27516)  
**代码**: https://github.com/GrumpySloths/SGS_Intrinsic.github.io  
**领域**: 3D视觉  
**关键词**: 逆渲染, 稀疏视图, 高斯溅射, 材质分解, 室内场景

## 一句话总结

SGS-Intrinsic 提出两阶段室内逆渲染框架，第一阶段利用语义和几何先验构建稠密几何一致的高斯场，第二阶段结合混合光照模型和材质先验进行材质-光照分解，并通过去阴影模块防止阴影烘焙到反照率中。

## 研究背景与动机

稀疏视图的室内逆渲染是极度病态的问题：监督信号稀疏、室内光照复杂（近场+高频）、材质与光照强耦合。现有方法要么只做几何重建不分解材质，要么假设远距离光源（对室内不适用），要么无法在稀疏视图下工作。

**三大挑战**：(1) 稀疏视图下高斯重建几何不可靠；(2) 室内近场高频光照建模困难；(3) 投射阴影容易被错误地烘焙进材质。

## 方法详解

### 整体框架

两阶段：Stage I 用 VGGT 初始化稠密点云，加入法线和语义先验监督构建高质量高斯几何场；Stage II 在此基础上用混合光照模型（环境图+球面高斯混合）+ 扩散材质先验 + 去阴影模块做逆渲染。

### 关键设计

1. **先验引导的稠密几何重建**:

    - 功能：在稀疏视图下构建可靠的高斯几何基础
    - 核心思路：用 VGGT 替代传统 SfM 获取稠密场景布局点云。然后用 StableNormal 提供法线监督 $\mathcal{L}_{normal} = 1 - \hat{n}^T n_m$，用 LSEG 提供语义监督。额外引入训练视图与虚拟视图间的语义一致性约束防止过拟合
    - 设计动机：传统 SfM 在稀疏视图下只能产生稀疏点云，不足以支撑高斯优化。预训练模型提供的稠密先验弥补了监督不足

2. **混合光照模型 + 材质先验**:

    - 功能：准确建模室内复杂光照并实现有效的材质-光照分解
    - 核心思路：环境图捕获远距离环境光，球面高斯混合（SGM）建模近场高频光照。利用扩散模型的材质先验提供跨视图和跨光照的材质一致性约束，收获光照-视图不变的材质重建
    - 设计动机：单一光照模型不够灵活，混合方案分别处理不同频率的光照成分。材质先验帮助打破材质-光照的固有歧义

3. **轻量去阴影模块**:

    - 功能：防止投射阴影被错误烘焙到反照率（albedo）中
    - 核心思路：引入轻量去阴影模型显式建模可见性，将阴影区域的暗色归因于遮挡而非材质。配合光照不变的材质一致性约束，确保同一材质在不同光照条件下产生相同的反照率
    - 设计动机：室内场景阴影复杂，如果不显式处理，优化器会把阴影解释为材质颜色

### 损失函数 / 训练策略

Stage I：RGB重建损失 + 法线损失 + 语义一致性损失。Stage II：PBR渲染损失 + 材质一致性损失 + 去阴影正则化。

## 实验关键数据

### 主实验

| 方法 | Interiorverse NVS PSNR | Albedo准确度 | 说明 |
|------|----------------------|-------------|------|
| GeoSplat | 较低 | 较低 | 几何不够 |
| IRGS | 中等 | 中等 | 光照模型受限 |
| **SGS-Intrinsic** | **最优** | **最优** | 全面超越 |

在基准数据集上的新视图合成和逆渲染指标全面领先。

### 消融实验

| 配置 | NVS质量 | 材质分解 | 说明 |
|------|---------|---------|------|
| 无先验引导 | 明显下降 | 差 | 几何不可靠影响后续 |
| 无混合光照 | — | 下降 | 近场光照建模不足 |
| 无去阴影 | — | 阴影烘焙 | 反照率被阴影污染 |
| 完整模型 | 最优 | 最优 | 所有组件必要 |

### 关键发现

- VGGT 提供的稠密初始化是稀疏视图成功的关键基础——好的几何是好的逆渲染的前提
- 去阴影模块对反照率估计质量的提升非常显著，室内场景中阴影烘焙是主要的材质估计误差来源
- 语义一致性约束有效防止了稀疏视图下的过拟合

## 亮点与洞察

- **两阶段解耦的合理性**：几何和材质分解有明确的依赖关系——先搞好几何再分解材质，比端到端联合优化更稳定
- **去阴影作为独立模块**：将阴影显式建模而非让优化器隐式处理，是一个简单但关键的设计
- **预训练模型作为先验来源**：StableNormal/LSEG/VGGT 等预训练模型的组合使用，展示了如何在稀疏视图下用丰富的先验补偿数据不足

## 局限与展望

- 依赖多个预训练模型（VGGT/StableNormal/LSEG/扩散模型），系统复杂度高
- 对非朗伯材质（如镜面、玻璃）的处理能力有限
- 两阶段训练的效率不如端到端方案
- 未来可探索减少先验模型依赖或统一为单一模型

## 相关工作与启发

- **vs GeoSplat/IRGS**: 同为3DGS逆渲染方法，SGS-Intrinsic 通过更强的先验和去阴影模块取得更好效果
- **vs NeRF-based 逆渲染**: 3DGS 的显式表示使得PBR属性的解耦更直接
- **vs 单图逆渲染**: 多视图方法天然具有3D一致性，但稀疏视图增加了挑战

## 评分

- 新颖性: ⭐⭐⭐⭐ 各模块设计扎实，去阴影思路有价值，但整体是已有技术的组合
- 实验充分度: ⭐⭐⭐⭐ 基准对比充分，消融清晰
- 写作质量: ⭐⭐⭐⭐ 方法描述系统清晰
- 价值: ⭐⭐⭐⭐ 对室内AR/VR应用有直接价值

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2025\] IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images](../../CVPR2025/3d_vision/iris_inverse_rendering_of_indoor_scenes_from_low_dynamic_range_images.md)
- [\[ICCV 2025\] GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering](../../ICCV2025/3d_vision/geosplatting_towards_geometry_guided_gaussian_splatting_for_physically-based_inv.md)
- [\[ICLR 2026\] RadioGS: Radiometrically Consistent Gaussian Surfels for Inverse Rendering](../../ICLR2026/3d_vision/radiogs_radiometric_gaussian_surfels.md)
- [\[CVPR 2025\] SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](../../CVPR2025/3d_vision/svg-ir_spatially-varying_gaussian_splatting_for_inverse_rendering.md)
- [\[CVPR 2026\] DropAnSH-GS: Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting](dropping_anchor_and_spherical_harmonics_for_sparse-view_gaussian_splatting.md)

<!-- RELATED:END -->
