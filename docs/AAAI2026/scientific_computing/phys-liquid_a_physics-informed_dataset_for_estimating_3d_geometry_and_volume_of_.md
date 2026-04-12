---
title: >-
  [论文解读] Phys-Liquid: A Physics-Informed Dataset for Estimating 3D Geometry and Volume of Transparent Deformable Liquids
description: >-
  [AAAI 2026][科学计算][physics-informed dataset] 提出 Phys-Liquid 数据集（97,200 张仿真图像 + 3D mesh），基于 Navier-Stokes 方程模拟容器旋转引起的透明液体动态变形，并设计四阶段管线验证其在液体几何重建和体积估计中的有效性。
tags:
  - AAAI 2026
  - 科学计算
  - physics-informed dataset
  - transparent liquid
  - 3D重建
  - Navier-Stokes
  - liquid dynamics
---

# Phys-Liquid: A Physics-Informed Dataset for Estimating 3D Geometry and Volume of Transparent Deformable Liquids

**会议**: AAAI 2026  
**arXiv**: [2511.11077](https://arxiv.org/abs/2511.11077)  
**代码**: [项目页](https://dualtransparency.github.io/Phys-Liquid/)  
**领域**: scientific_computing  
**关键词**: physics-informed dataset, transparent liquid, 3D reconstruction, Navier-Stokes, liquid dynamics  

## 一句话总结

提出 Phys-Liquid 数据集（97,200 张仿真图像 + 3D mesh），基于 Navier-Stokes 方程模拟容器旋转引起的透明液体动态变形，并设计四阶段管线验证其在液体几何重建和体积估计中的有效性。

## 背景与动机

自主实验室机器人执行精密液体操作（分注、吸取、混合）时，容器运动不可避免地导致液体变形，现有数据集不足：
- Objaverse 等大规模 3D 数据集主要是刚体
- ClearGrasp/ClearPose 关注透明物体但忽略液体
- DTLD 有液体但仅静态状态，无变形动态
- 缺乏基于物理仿真的动态液体数据集

## 核心问题

如何创建具有物理真实性的动态液体仿真数据集，并验证其对真实世界液体感知任务的有效性？

## 方法详解

### 数据集生成

**物理仿真**：基于 Navier-Stokes 方程，由 Blender + Mantaflow 求解：
$$\frac{D\mathbf{u}}{Dt} = -\frac{1}{\rho}\nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{g}, \quad \nabla \cdot \mathbf{u} = 0$$

数据集参数：20 种实验室容器 × 5 种液体颜色 × 8 种光照 × 5 种场景 × 6 种旋转模式（0°-80°）× 81 时间帧 × 6 正交视角 = **97,200 张图像** + 8,100 个标注 3D mesh (OBJ 格式)

### 四阶段重建管线

$$S = F(I) = T(R(G(S(I))), s)$$

1. **液体分割**：YOLO-world 检测 → SAM2 精细分割
2. **多视角 mask 生成**：CRM 扩散模型（在 Phys-Liquid 上 fine-tune）从单视角生成 6 个正交视角 mask
3. **3D mesh 重建**：Triplane 表示 + 卷积 U-Net 编码 + MLP 解码
4. **真实尺度缩放**：多视角 ViT 回归缩放因子 $s = \sqrt[3]{\frac{S_{PI,x}}{V_x} \cdot \frac{S_{PI,y}}{V_y} \cdot \frac{S_{PI,z}}{V_z}}$

## 实验关键数据

| 方法 | RMSE | Chamfer Dist | Volume IoU | F-Score |
|------|------|-------------|------------|--------|
| Eppel et al. (XYZ map) | 0.0842 | 0.0412 | 0.1216 | 30.91% |
| InstantMesh | - | 0.0189 | 0.2794 | 46.18% |
| TripoSR | - | 0.0275 | 0.2275 | 38.06% |
| Ours (w/o ft) | 0.0254 | 0.0128 | 0.3246 | 58.19% |
| **Ours (w/ ft)** | **0.0192** | **0.0085** | **0.6236** | **78.57%** |

- Fine-tune 后多视角 mask IoU 从 74.38% 提升至 90.05%
- 迁移到真实世界 DTLD 数据集：F-Score 62.43%，RMSE 0.0266
- 时间一致性：100 个序列的 RMSE 方差仅 0.00038

## 亮点

- 首个包含透明液体动态变形的物理仿真数据集，覆盖时空 4D 维度
- 基于 Navier-Stokes 方程保证物理真实性，与真实实验对比验证一致
- 四阶段管线从单张RGB图像重建 3D 液体 mesh 并估计真实体积
- 对真实世界数据有良好泛化（DTLD 数据集零样本迁移）

## 局限性

- 数据集规模适中（97K 图像），覆盖的容器形状有限（20 种）
- 仅模拟旋转运动引起的液体变形，未涉及振荡、倾倒等操作
- 重建管线依赖多个串联模型，任何一步的误差都会累积
- Blender/Mantaflow 仿真与真实物理仍有差距（折射、气泡等未建模）

## 对比

| 数据集 | 物体数 | 图像数 | 液体变形 | 多视角 | 时间变化 |
|--------|--------|--------|---------|--------|--------|
| Narasimhan et al. | 2 | 4,601 | ✗ | ✗ | ✗ |
| DTLD | 4 | 27,458 | ✗ | ✓ | ✗ |
| **Phys-Liquid** | **20** | **97,200** | **✓** | **✓** | **✓** |

## 启发

- 物理仿真数据集 + 真实数据验证的"仿真-真实"闭环值得推广
- 多视角正交渲染 + triplane 重建的组合简洁有效
- 为实验室自动化机器人的精密液体操作提供基础

## 评分

⭐⭐⭐⭐ — 数据集贡献有价值，管线设计完整，但核心方法依赖现有模块组合
