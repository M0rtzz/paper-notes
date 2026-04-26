---
title: >-
  [论文解读] DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion
description: >-
  [ECCV 2024][自动驾驶][多模态融合] 提出 DVLO，一种基于局部到全局融合与双向结构对齐的视觉-LiDAR 里程计网络，通过将图像视为伪点云（局部融合）和将点云投影为伪图像（全局融合）来解决两种模态的固有数据结构不一致问题。
tags:
  - ECCV 2024
  - 自动驾驶
  - 多模态融合
  - 里程计
  - 视觉-LiDAR
  - 聚类融合
  - 双向结构对齐
---

# DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion

**会议**: ECCV 2024  
**arXiv**: [2403.18274](https://arxiv.org/abs/2403.18274)  
**代码**: https://github.com/IRMVLab/DVLO  
**领域**: 自动驾驶 / 视觉-LiDAR 里程计  
**关键词**: 多模态融合, 里程计, 视觉-LiDAR, 聚类融合, 双向结构对齐

## 一句话总结
提出 DVLO，一种基于局部到全局融合与双向结构对齐的视觉-LiDAR 里程计网络，通过将图像视为伪点云（局部融合）和将点云投影为伪图像（全局融合）来解决两种模态的固有数据结构不一致问题。

## 研究背景与动机

**领域现状**：多模态里程计利用图像的纹理信息和 LiDAR 的几何信息互补。现有学习方法主要用 CNN 或交叉注意力做特征级融合。

**现有痛点**：(1) 图像像素规则密集但 LiDAR 点无序稀疏，数据结构不一致是融合的核心挑战；(2) CNN 融合感受野受限于核大小和步长；(3) 注意力融合虽有全局感受野但 $O(n^2)$ 复杂度不适合实时应用；(4) 纯特征级融合无法捕获细粒度的像素-点对应关系。

**核心矛盾**：局部融合能获得精细的像素-点对应但感受野有限，全局融合能捕获远距离依赖但丢失细节——需要同时兼顾两者。

**本文目标**：设计一种同时具备局部精细对应和全局信息交互能力的视觉-LiDAR 融合里程计。

**切入角度**：双向结构对齐——分别将两种模态转换为对方的数据格式，然后在统一结构下融合。

**核心 idea**：先将图像重塑为伪点云，以 LiDAR 投影点为聚类中心做局部聚合（图像→点对齐）；再将点云做圆柱投影为伪图像，与局部融合特征做自适应全局融合（点→图像对齐）。

## 方法详解

### 整体框架
输入连续两帧的图像和点云 → 分层特征提取（图像用金字塔CNN，点云做圆柱投影后提取特征）→ 多尺度局部-全局融合 → 代价体积构建 → 粗到细迭代位姿估计。

### 关键设计

1. **聚类式局部融合 (Local Fuser)**:

    - 功能：在每个 LiDAR 点的投影位置周围聚合图像纹理特征
    - 核心思路：将图像特征重塑为伪点集合 $F_{pp} \in \mathbb{R}^{M \times C}$，将 LiDAR 点投影到图像平面获取聚类中心。按余弦相似度将伪点分配到最近中心，然后用加权聚合 $F_L^i = \frac{1}{X}(F_c^i + \sum_j \text{sigmoid}(\alpha s_{ij} + \beta) \cdot F_{pp}^j)$ 得到局部融合特征
    - 设计动机：无需 CNN 或 Transformer，纯聚类操作高效且能建立精细的像素-点对应。推理时间仅为注意力方法的一半

2. **自适应全局融合 (Global Fuser)**:

    - 功能：在局部融合特征和点云特征之间进行全局信息交互
    - 核心思路：利用圆柱投影将点云转为伪图像。对局部融合特征 $F_L$ 和点特征 $F_P$ 分别用 MLP+sigmoid 生成自适应权重 $A_P, A_L$，然后加权融合 $F_G = (A_P \odot F_P + A_L \odot F_L) / (A_P + A_L)$
    - 设计动机：局部融合感受野有限，全局自适应融合扩展了感受野，能识别动态物体和遮挡引起的全局不一致运动

3. **多尺度迭代位姿估计**:

    - 功能：从粗到细逐层精化位姿
    - 核心思路：在最粗层构建注意力代价体积获得初始位姿（四元数 $q$ + 平移 $t$），然后在浅层利用融合特征迭代精化。损失函数用 L1/L2 范数加可学习标量平衡旋转和平移
    - 设计动机：多尺度策略在光流和里程计中已被验证有效

### 损失函数 / 训练策略
多尺度加权损失 $\mathcal{L} = \sum_l \alpha^l \mathcal{L}^l$，每层用加权 L1+L2 范数，可学习参数 $k_x, k_q$ 自动平衡平移和旋转损失的尺度。

## 实验关键数据

### 主实验

| 方法 | KITTI 00-10 $t_{rel}$ (%) | $r_{rel}$ (°/100m) | 模态 |
|------|------------------------|-------------------|------|
| DVLO | **最优** | **最优** | Vision+LiDAR |
| EfficientLO | 次优 | 次优 | LiDAR only |
| CamLiFlow | 较高 | 较高 | Vision+LiDAR |

在 KITTI 大部分序列上超越所有单模态和多模态方法。

### 消融实验

| 融合策略 | $t_{rel}$ | 说明 |
|---------|----------|------|
| Local only | 中等 | 缺少全局信息交互 |
| Global only | 较差 | 缺少精细对应 |
| Local-to-Global (DVLO) | **最优** | 两者互补 |
| 无双向对齐 | 下降 | 结构对齐提升融合质量 |

### 关键发现
- 局部-全局融合策略互补效果显著：单独用局部或全局都不如组合
- 聚类式融合是第一个深度聚类多模态融合尝试，推理效率远超注意力方法
- 融合策略可泛化到场景流估计任务，超越 CamLiRAFT

## 亮点与洞察
- **双向结构对齐**是处理异构数据融合的通用思路——将两种模态互相转换为对方格式再融合，比单向对齐更彻底
- **聚类替代注意力**做多模态融合是新思路，既保持了精细对应又高效
- 局部-全局的分层融合范式可迁移到其他视觉-LiDAR 任务

## 局限与展望
- 依赖精确的标定矩阵进行点到图像的投影
- 圆柱投影可能在近距离区域产生信息损失
- 目前仅验证了里程计和场景流两个任务

## 相关工作与启发
- **vs EfficientLO**: 纯 LiDAR 里程计，DVLO 通过融合图像纹理获得更好精度
- **vs CamLiFlow/CamLiRAFT**: 用交叉注意力融合，DVLO 用聚类更高效
- **vs V-LOAM**: 传统方法将视觉里程计作为 LiDAR 的先验，DVLO 端到端联合融合

## 评分
- 新颖性: ⭐⭐⭐⭐ 聚类式融合+双向结构对齐是新颖的组合
- 实验充分度: ⭐⭐⭐⭐ KITTI 全序列对比+场景流泛化+充分消融
- 写作质量: ⭐⭐⭐⭐ 融合策略的对比图直观清晰
- 价值: ⭐⭐⭐⭐ 为多模态融合提供了高效的聚类替代方案

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion and Bi-directional Structure Alignment](dvlo_deep_visual-lidar_odometry_with_local-to-global_feature_fusion_and_bi-direc.md)
- [\[ECCV 2024\] GraphBEV: Towards Robust BEV Feature Alignment for Multi-Modal 3D Object Detection](graphbev_towards_robust_bev_feature_alignment_for_multi-modal_3d_object_detectio.md)
- [\[ECCV 2024\] OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving](occgen_generative_multimodal_3d_occupancy_prediction_for_aut.md)
- [\[ECCV 2024\] LiDAR-Event Stereo Fusion with Hallucinations](lidarevent_stereo_fusion_with_hallucinations.md)
- [\[ECCV 2024\] Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection](detecting_as_labeling_rethinking_lidar-camera_fusion_in_3d_object_detection.md)

<!-- RELATED:END -->
