---
title: >-
  [论文解读] NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather
description: >-
  [CVPR 2026][3D视觉][3D高斯溅射] NimbusGS 提出统一的3D场景重建框架，通过将天气退化分解为连续散射场（雾/霾）和逐视图粒子残差层（雨/雪），配合几何引导梯度缩放机制，在单一框架内实现跨天气和混合天气条件下的SOTA重建。
tags:
  - CVPR 2026
  - 3D视觉
  - 3D高斯溅射
  - 恶劣天气
  - 场景重建
  - 物理建模
  - 天气分解
---

# NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather

**会议**: CVPR 2026  
**arXiv**: [2603.27228](https://arxiv.org/abs/2603.27228)  
**代码**: [https://github.com/lyy-ovo/NimbusGS](https://github.com/lyy-ovo/NimbusGS)  
**领域**: 3D视觉  
**关键词**: 3D高斯溅射, 恶劣天气, 场景重建, 物理建模, 天气分解

## 一句话总结

NimbusGS 提出统一的3D场景重建框架，通过将天气退化分解为连续散射场（雾/霾）和逐视图粒子残差层（雨/雪），配合几何引导梯度缩放机制，在单一框架内实现跨天气和混合天气条件下的SOTA重建。

## 研究背景与动机

3D场景重建假设输入干净高质量，但实际环境中雾、雨、雪等天气严重影响成像。天气退化有两种机制：(1) 连续介质（雾/霾）——深度相关的光衰减，视图间一致；(2) 离散粒子（雨/雪）——动态高频遮挡，视图间独立。

**现有方法的局限**：预处理恢复+重建的两阶段方案破坏多视图一致性；将天气建模嵌入重建的方案通常只针对单一天气类型。在混合天气（如同时有雾和雨）场景下，现有方法普遍失效。

**本文核心**：基于天气的物理本质，设计统一框架同时建模连续散射和离散粒子两种退化机制。

## 方法详解

### 整体框架

基于3DGS，增加两个退化建模分支：连续散射场建模全局透射率和大气光（视图一致），粒子残差层建模逐视图的动态干扰（视图独立）。几何引导梯度缩放机制稳定优化过程。

### 关键设计

1. **连续散射场建模 (Continuous Scattering Field)**:

    - 功能：建模雾/霾等连续介质造成的视图一致的光衰减效应
    - 核心思路：使用体积消光场估计场景级别的透射率和大气光。透射率随深度衰减，大气光对所有视图共享。渲染公式在标准3DGS的基础上加入大气散射模型
    - 设计动机：雾霾是全局性的物理效应，必须以视图一致的方式建模才能保持多视图几何一致性

2. **粒子残差层建模 (Particulate Residual Layer)**:

    - 功能：建模雨/雪等离散粒子造成的视图独立的局部遮挡
    - 核心思路：为每个视图维护独立的残差图，捕获该视图特有的动态干扰。残差在渲染后叠加，不影响底层的3D几何。训练时自动学习将瞬态干扰归到残差层，将持久结构归到高斯场
    - 设计动机：雨滴/雪花在不同视图位置不同，无法用视图一致的方式建模，需要逐视图的独立处理

3. **几何引导梯度缩放 (Geometry-Guided Gradient Scaling)**:

    - 功能：在严重遮挡下稳定几何学习
    - 核心思路：根据可见度线索自适应调整不同区域的梯度幅度。可见度高的区域给正常梯度，可见度低的区域（被雾霾严重遮挡）缩小梯度防止噪声主导优化。这解决了远处或重度退化区域的梯度不平衡问题
    - 设计动机：天气导致不均匀的可见度，远处重度退化区域的重建信号很弱但梯度可能因噪声而很大，需要抑制

### 损失函数 / 训练策略

渐进式优化策略：逐步解耦连续散射和粒子效应。L1重建损失 + D-SSIM + 用于散射场和残差层的正则化损失。不需要配对数据或大规模预训练。

## 实验关键数据

### 主实验

| 天气条件 | NimbusGS | 之前SOTA | 提升 |
|---------|----------|---------|------|
| 雾/霾 | SOTA | DehazeGS | 显著提升 |
| 雨 | SOTA | DeRainGS | 显著提升 |
| 雪 | SOTA | WeatherGS | 显著提升 |
| 混合天气 | **新基准** | 无可比方法 | — |

在单一天气和混合天气条件下全面超越各专用方法。

### 消融实验

| 配置 | PSNR | 说明 |
|------|------|------|
| 仅3DGS基线 | 低 | 天气严重影响重建 |
| + 连续散射场 | 提升 | 全局退化去除 |
| + 粒子残差层 | 进一步提升 | 局部干扰去除 |
| + 梯度缩放 | 最优 | 远处几何改善 |

### 关键发现

- 物理驱动的分解比数据驱动的端到端方法更鲁棒，尤其在混合天气下优势明显
- 梯度缩放对远处/重度退化区域的重建质量有关键贡献
- 统一框架的泛化能力：无需针对新天气类型做任何调整

## 亮点与洞察

- **物理驱动的优雅分解**：将天气按物理机制分为连续/离散两类，每类用对应的建模方式处理，既物理合理又工程简洁
- **梯度缩放的通用性**：这种基于可见度的自适应优化策略可以迁移到其他退化场景（如低光照、水下等）
- **统一框架的价值**：一个模型处理所有天气，避免了维护多个专用模型的工程负担

## 局限与展望

- 粒子残差层的容量有限，对极端降水（如暴雨）可能不足
- 连续散射场假设均匀大气，对非均匀雾（如局部浓雾）不够灵活
- 未验证在极端天气组合（如雪+雾+雨）下的表现
- 未来可扩展到动态场景（如移动车辆+天气）

## 相关工作与启发

- **vs WeatherGS**: WeatherGS 分离粒子和透镜伪影但需要2D先验，NimbusGS 在3D空间中统一建模
- **vs DehazeNeRF/ScatterNeRF**: 这些方法只处理雾霾，NimbusGS 同时处理雾+雨+雪
- **vs RainyScape/DeRainGS**: 专用雨天方法，缺乏对其他天气的泛化能力

## 评分

- 新颖性: ⭐⭐⭐⭐ 物理分解思路清晰，梯度缩放设计实用
- 实验充分度: ⭐⭐⭐⭐ 多天气条件覆盖全面
- 写作质量: ⭐⭐⭐⭐ 物理动机阐述清楚
- 价值: ⭐⭐⭐⭐ 对自动驾驶等户外3D重建有直接应用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] RobuSTereo: Robust Zero-Shot Stereo Matching under Adverse Weather](../../ICCV2025/3d_vision/robustereo_robust_zero-shot_stereo_matching_under_adverse_weather.md)
- [\[CVPR 2026\] Sky2Ground: A Benchmark for Site Modeling under Varying Altitude](sky2ground_a_benchmark_for_site_modeling_under_varying_altitude.md)
- [\[CVPR 2026\] FreeArtGS: Articulated Gaussian Splatting Under Free-Moving Scenario](freeartgs_articulated_gaussian_splatting_under_free-moving_scenario.md)
- [\[CVPR 2026\] PoseMaster: A Unified 3D Native Framework for Stylized Pose Generation](posemaster_a_unified_3d_native_framework_for_stylized_pose_generation.md)
- [\[CVPR 2026\] RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations](rng_a_unified_transformer_for_complete_3d_modeling_from_partial_observations.md)

</div>

<!-- RELATED:END -->
