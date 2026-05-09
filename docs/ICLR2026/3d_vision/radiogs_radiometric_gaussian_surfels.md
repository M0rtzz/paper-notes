---
title: >-
  [论文解读] RadioGS: Radiometrically Consistent Gaussian Surfels for Inverse Rendering
description: >-
  [ICLR 2026][3D视觉][逆渲染] RadioGS 提出辐射一致性损失——通过最小化每个 Gaussian surfel 的学习辐射与其物理渲染辐射之间的残差，为未观测方向提供基于物理的监督信号，构建自纠正反馈循环，实现了准确的间接照明和材质分解，并支持分钟级重新打光。
tags:
  - ICLR 2026
  - 3D视觉
  - 逆渲染
  - Gaussian Splatting
  - 间接照明
  - 辐射一致性
  - 光线追踪
---

# RadioGS: Radiometrically Consistent Gaussian Surfels for Inverse Rendering

**会议**: ICLR 2026  
**arXiv**: [2603.01491](https://arxiv.org/abs/2603.01491)  
**代码**: [https://qbhan.github.io/radiogs-page/](https://qbhan.github.io/radiogs-page/)  
**领域**: 3D视觉  
**关键词**: 逆渲染, Gaussian Splatting, 间接照明, 辐射一致性, 光线追踪

## 一句话总结

RadioGS 提出辐射一致性损失——通过最小化每个 Gaussian surfel 的学习辐射与其物理渲染辐射之间的残差，为未观测方向提供基于物理的监督信号，构建自纠正反馈循环，实现了准确的间接照明和材质分解，并支持分钟级重新打光。

## 研究背景与动机

**领域现状**：基于 Gaussian Splatting 的逆渲染发展迅速，能高效地从多视角图像中恢复几何、材质和光照。然而，准确分解全局光照效应（尤其是间接照明和表面间反射）仍是核心挑战。

**现有痛点**：现有方法处理间接照明的方式主要有两种：(1) 将间接辐射作为可学习残差（如 R3DG、GS-IR），无约束优化会导致光照和材质的模糊分解；(2) 从预训练 NVS 的 Gaussian 原语查询间接辐射（如 IRGS、SVG-IR），但预训练只针对训练视角有监督，从未观测方向查询的辐射可能完全错误。

**核心矛盾**：NVS 训练只约束了相机可见方向的 Gaussian 辐射，而间接照明需要查询任意方向（包括表面间反射方向）的辐射。缺乏对未观测方向的监督导致间接辐射不准确，进而导致光照被错误地烘焙到表面材质中。

**本文目标**：提供一种基于物理的约束，使 Gaussian surfel 在未观测方向上也能获得正确的辐射值，从而准确建模间接照明和表面间反射。

**切入角度**：借鉴自训练辐射缓存（self-training radiance cache）的思想——通过迭代最小化渲染方程残差，让 Gaussian 原语的辐射值逐步收敛到物理正确的解。

**核心 idea**：辐射一致性 = 让每个 Gaussian surfel 的学习辐射 $L_\mathbf{G}$ 与其基于渲染方程的物理渲染辐射 $L_\mathbf{G}^{PBR}$ 一致，形成自纠正循环——相机视角的重建监督传播到间接照明项，物理渲染又反过来约束未观测方向的辐射。

## 方法详解

### 整体框架

两阶段流程：初始化阶段——用 split-sum 近似的简化辐射一致性损失 + NVS 重建损失预训练 Gaussian surfels，建立稳定的几何基础。逆渲染阶段——用完整的蒙特卡洛辐射一致性损失 + 材质平滑损失 + 光照先验损失联合优化几何、材质和光照。重新打光——固定几何和材质，新光照下只微调 surfel 辐射（约 2 分钟），然后直接用 surfel 辐射渲染（<10ms/帧）。

### 关键设计

1. **辐射一致性损失 (Radiometric Consistency Loss)**:

    - 功能：为 Gaussian surfel 的未观测方向辐射提供基于物理的监督信号
    - 核心思路：对每个 surfel 位置 $x$ 和出射方向 $\omega_o$，计算物理渲染辐射 $L_\mathbf{G}^{PBR}(x,\omega_o) = \int f_r \cdot (V \cdot L_{dir} + L_{ind}) \cdot (\omega_i \cdot n_x) d\omega_i$，其中可见性 $V$ 和间接辐射 $L_{ind}$ 通过 2D Gaussian 光线追踪获得。残差 $\mathcal{R}_\mathbf{G} = L_\mathbf{G} - L_\mathbf{G}^{PBR}$，损失为 $\mathcal{L}_{rad} = \mathbb{E}_{j,\omega_o}[\|\mathcal{R}_\mathbf{G}\|_1]$。最小化残差形成双向反馈：物理渲染引导未观测方向的辐射，而相机约束的辐射通过间接照明项传播给其他 surfel
    - 设计动机：自纠正循环的关键在于：相机视角的重建损失保证了部分方向的辐射准确，这些准确辐射通过光线追踪成为其他 surfel 的间接照明，进而约束那些 surfel 的辐射值

2. **2D Gaussian 光线追踪与蒙特卡洛采样**:

    - 功能：高效获取 surfel 间的可见性和间接辐射，并使其可微分
    - 核心思路：使用 2D Gaussian ray tracer 发射光线，$\text{Trace}(x, \omega_i; \mathbf{G}) = (L_{trace}, T_{trace})$，累积辐射 $L_{trace}$ 直接作为间接辐射 $L_{ind}$，$1-T_{trace}$ 作为可见性 $V$。蒙特卡洛估计：每步随机采样 $N_g = 4096$ 个 surfel，每个 surfel 在其法线定义的半球上均匀采样 $N_s = 64$ 条入射光线（共 $2^{18}$ 条光线），同时采样随机出射方向（未观测）和相机方向（已约束）
    - 设计动机：2D Gaussian 光线追踪与 Gaussian surfel 共享 ray-splat 交叉计算，无缝集成且可微分；采样相机方向确保已约束的辐射信号能传播到光线追踪的 surfel

3. **基于微调的高效重新打光**:

    - 功能：在新光照条件下快速适应 surfel 辐射
    - 核心思路：给定新光照，只需最小化辐射一致性损失 $\mathcal{L}_{rad}$ 对 surfel 辐射参数进行几轮微调（约 2 分钟）。微调完成后，可从任意视角直接用 surfel 辐射渲染（<10ms/帧），无需运行时光线追踪或存储每个 surfel 的多方向入射辐射
    - 设计动机：传统方法在重新打光时需要运行时查询间接辐射（昂贵），而辐射一致性微调让 surfel 直接"记住"新光照下的正确辐射

### 损失函数 / 训练策略

初始化阶段：$\mathcal{L}_{init} = \mathcal{L}_{recon} + \mathcal{L}_{recon}^{PBR} + \lambda_{rad}\mathcal{L}_{rad} + \lambda_{dist}\mathcal{L}_{dist} + \lambda_n\mathcal{L}_n + \lambda_{ns}\mathcal{L}_{ns} + \lambda_m\mathcal{L}_m$（split-sum 近似版辐射一致性）。逆渲染阶段：$\mathcal{L}_{inv} = \mathcal{L}_{init} + \lambda_{as}\mathcal{L}_{as} + \lambda_{rs}\mathcal{L}_{rs} + \lambda_{light}\mathcal{L}_{light}$（完整蒙特卡洛辐射一致性 + 材质平滑 + 光照先验）。辐射一致性权重 $\lambda_{rad} = 0.2$（逆渲染），$1.0$（重新打光微调）。总训练时间约 60 分钟（RTX 4090）。

## 实验关键数据

### 主实验

| 方法 | NVS PSNR↑ | Normal MAE↓ | Albedo PSNR↑ | Relight PSNR↑ | 训练时间 |
|------|-----------|-------------|-------------|--------------|---------|
| TensoIR (NeRF) | 35.09 | 4.10 | 29.27 | 28.58 | 4h |
| GS-IR | 35.33 | 4.95 | 29.94 | 24.37 | - |
| IRGS | - | - | - | - | - |
| SVG-IR | - | - | - | - | - |
| **RadioGS** | **最优** | **最优** | **最优** | **最优** | **1h** |

RadioGS 在 TensoIR 数据集上几乎所有指标上超越现有 GS 方法和 NeRF 方法，同时保持计算效率。

### 消融实验

| 配置 | Relight PSNR | 说明 |
|------|-------------|------|
| 完整 RadioGS | 最优 | 全蒙特卡洛辐射一致性 |
| 去除辐射一致性损失 | 显著下降 | 间接照明不准确 |
| 仅 split-sum（无 MC） | 下降 | 近似不足以捕捉复杂反射 |
| 去除初始化阶段辐射一致性 | 下降 | 几何基础不稳定 |
| 微调重新打光 vs RT重新打光 | 略低但渲染极快 | <10ms vs ~100ms |

### 关键发现

- 辐射一致性损失是 RadioGS 优势的核心来源——去除后重新打光质量大幅下降，证明了物理约束对间接照明建模的必要性
- 红色灯泡在黄色乐高表面的反射效果（TensoIR 数据集）展示了 RadioGS 对表面间反射的精准建模能力——其他方法往往将这种间接照明烘焙到 albedo 中
- 微调重新打光策略只需 2 分钟训练就能达到接近光线追踪重新打光的质量，但渲染速度快一个数量级

## 亮点与洞察

- **自纠正反馈循环**的设计理念极具洞察力——NVS 监督和物理约束不是对立的，而是互补的：NVS 约束已观测方向，物理渲染约束未观测方向，两者通过间接照明项连接形成闭环
- **初始化阶段的简化辐射一致性**是一个重要的工程洞见——直接在不稳定几何上用蒙特卡洛采样会导致训练震荡，split-sum 近似提供了平滑的过渡
- **微调重新打光**将运行时光线追踪的成本转化为离线微调成本，非常适合需要渲染多帧的应用场景

## 局限与展望

- 假设材质为电介质（Dielectric），对金属等强镜面材质的效果未验证
- 每步 $2^{18}$ 条光线追踪仍有计算开销，训练时间约 1 小时
- 蒙特卡洛采样在低 surfel 密度区域可能估计不准
- 微调重新打光在光照变化极大时（如从室内到室外）可能需要更多迭代

## 相关工作与启发

- **vs IRGS (Gu et al., 2024)**: IRGS 也用 Gaussian 光线追踪优化间接辐射，但训练信号仍只来自已观测视角图像；RadioGS 通过物理约束为未观测方向提供额外监督
- **vs SVG-IR (Sun et al., 2025)**: SVG-IR 从 NVS 预训练的 Gaussian 点追踪查询间接辐射，但预训练的 Gaussian 在未观测方向无约束；RadioGS 的辐射一致性解决了这一根本问题
- **vs Neural Radiance Cache (Müller et al., 2021)**: 辐射缓存用于前向渲染的全局光照；RadioGS 将这一思想拓展到逆渲染中的 Gaussian 原语

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 辐射一致性损失的自纠正反馈循环思想新颖且有物理动机
- 实验充分度: ⭐⭐⭐⭐ 合成和真实数据集评测，消融充分
- 写作质量: ⭐⭐⭐⭐⭐ 问题动机、方法推导、实验分析都非常清晰
- 价值: ⭐⭐⭐⭐⭐ 对 GS 逆渲染中间接照明的准确建模有重要推动

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](../../CVPR2026/3d_vision/sgs-intrinsic_semantic-invariant_gaussian_splatting_for_sparse-view_indoor_invers.md)
- [\[CVPR 2025\] SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](../../CVPR2025/3d_vision/svg-ir_spatially-varying_gaussian_splatting_for_inverse_rendering.md)
- [\[ICCV 2025\] GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering](../../ICCV2025/3d_vision/geosplatting_towards_geometry_guided_gaussian_splatting_for_physically-based_inv.md)
- [\[ICLR 2026\] 3DGEER: 3D Gaussian Rendering Made Exact and Efficient for Generic Cameras](3dgeer_3d_gaussian_rendering_made_exact_and_efficient_for_generic_cameras.md)
- [\[CVPR 2025\] PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields](../../CVPR2025/3d_vision/pbr-nerf_inverse_rendering_with_physics-based_neural_fields.md)

</div>

<!-- RELATED:END -->
