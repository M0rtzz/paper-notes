---
title: >-
  [论文解读] LiDAR-Event Stereo Fusion with Hallucinations
description: >-
  [ECCV 2024][自动驾驶][事件相机] 首次探索 LiDAR 与事件立体相机的融合，提出虚拟堆叠幻觉（VSH）和回溯时间幻觉（BTH）两种策略，通过在事件流/堆叠中注入虚拟事件来增强匹配可辨别性，大幅提升事件立体匹配精度。
tags:
  - ECCV 2024
  - 自动驾驶
  - 事件相机
  - LiDAR融合
  - 立体匹配
  - 幻觉事件注入
  - 深度估计
---

# LiDAR-Event Stereo Fusion with Hallucinations

**会议**: ECCV 2024  
**arXiv**: [2408.04633](https://arxiv.org/abs/2408.04633)  
**代码**: [https://eventvppstereo.github.io/](https://eventvppstereo.github.io/)  
**领域**: 自动驾驶  
**关键词**: 事件相机, LiDAR融合, 立体匹配, 幻觉事件注入, 深度估计

## 一句话总结

首次探索 LiDAR 与事件立体相机的融合，提出虚拟堆叠幻觉（VSH）和回溯时间幻觉（BTH）两种策略，通过在事件流/堆叠中注入虚拟事件来增强匹配可辨别性，大幅提升事件立体匹配精度。

## 研究背景与动机

- 事件相机具有微秒级时间分辨率和高动态范围，适合高速运动和极端光照场景
- 但事件相机仅在亮度变化时触发，面临无运动或大面积无纹理区域时的困难——对应点匹配极具挑战
- LiDAR 能在事件相机失效的区域提供稀疏深度测量（互补性强）
- **关键挑战**：LiDAR 固定频率（如 10Hz）与事件相机异步采集不同步
- 现有 RGB 立体-LiDAR 融合方法（Guided Stereo、LidarStereoNet、CCVNorm）未适配事件相机
- 本文是**首次**将 LiDAR 与事件立体框架结合的尝试

## 方法详解

### 整体框架

根据对立体网络的访问程度分三类：
- **白盒**：可访问网络实现和事件堆叠构建
- **灰盒**：可访问事件堆叠但不可修改网络内部 → 适用 VSH
- **黑盒**：堆叠表示也不可访问 → 适用 BTH

两种幻觉策略：
1. **VSH（Virtual Stack Hallucination）**：在堆叠表示中直接注入虚拟模式
2. **BTH（Back-in-Time Hallucination）**：在原始事件流中注入虚拟事件

### 关键设计

**VSH — 虚拟堆叠幻觉**：
- 给定左右事件堆叠 S_L, S_R 和稀疏深度 Z
- 将深度转换为视差：d(x,y) = bf/z(x,y)
- 在堆叠的对应位置 (x,y) 和 (x',y) 注入相同的虚拟模式
- A(x,y,x',c) ~ U(S⁻, S⁺)：从堆叠值域均匀随机采样
- 支持单像素或 patch（3×3 最优）
- alpha 混合系数 0.5 效果最佳

**BTH — 回溯时间幻觉**：
- 在原始事件流中注入虚拟事件 ê^L = (x̂, ŷ, p̂, t̂) 和 ê^R = (x̂', ŷ, p̂, t̂)
- 满足三个约束：时间排序、几何一致性（x̂' = x̂ - d）、相似性（同极性同时间戳）

*单时间戳注入*：在固定时间戳 t_z 注入随机极性事件
*重复注入（关键改进）*：沿时间轴分 B=12 个 bin，在每个 bin 的 MDES 风格时间点注入
  - 每个深度测量仅用一次（随机分配到某个 bin）
  - 大幅提升对 LiDAR 数据不同步的鲁棒性

**利用过期 LiDAR 数据**：
- 即使 LiDAR 扫描时间 t_z < t_d（不同步），仍可将虚拟事件放在事件历史中的对应位置
- 保持了事件相机的微秒级分辨率，无需等待 LiDAR 同步

### 损失函数 / 训练策略

- 基于 SE-CFF 框架，使用 AANet 立体骨干
- Adam 优化器，LR=5×10⁻⁴，余弦退火，weight decay=10⁻⁴
- 25 epochs，batch size 4，最大视差 192
- 评估 8 种事件堆叠表示：Histogram, Voxel Grid, MDES, Concentrated, TORE, Time Surface, ERGO-12, Tencode

## 实验关键数据

### 主实验

DSEC 数据集（预训练模型，直接应用融合）：

| 表示 | Baseline 1PE | Guided 1PE | VSH 1PE | BTH 1PE |
|------|-------------|-----------|---------|---------|
| Histogram | 16.21 | 16.07 | 13.71 | **13.32** |
| MDES | 15.32 | 15.13 | - | - |

VSH 和 BTH 在所有 8 种表示上均显著优于 Guided Stereo 等现有融合方法。

### 消融实验

| 超参数 | 最优设置 |
|--------|---------|
| Patch 大小 | 3×3（VSH/BTH 均一致） |
| 均匀模式 vs 随机模式 | 均匀更优 |
| Alpha 混合 | 0.5 |
| 单次 vs 重复注入 | 重复注入显著更优 |
| 注入事件数 | 2 即饱和 |
| 均匀极性 vs 随机极性 | 均匀极性更优 |

### 关键发现

1. 事件流本身的半稀疏特性使虚拟模式注入比 RGB 域更有效——不需要与已有像素值"竞争"
2. BTH 的重复注入在处理不同步 LiDAR 数据时显著更鲁棒
3. VSH 更简单快速（2-15ms CPU），BTH 更通用（黑盒兼容）但稍慢（10ms CPU）
4. 方法对 M3ED 数据集（域外）的泛化性良好

## 亮点与洞察

- **"幻觉"概念的巧妙应用**：不是在结果中添加信息，而是在输入中注入虚拟事件来增强可辨别性
- **互补性分析精辟**：事件相机在纹理边界处强（LiDAR弱），LiDAR在无纹理区域强（事件相机弱）
- **保持微秒分辨率**：通过利用过期 LiDAR 数据，避免了被 LiDAR 10Hz 帧率限制
- **全面的表示覆盖**：在 8 种不同事件堆叠表示上验证，证明了方法的通用性

## 局限性 / 可改进方向

- VSH 需要灰盒访问（知道堆叠表示），BTH 的遮挡处理策略不成熟
- Fixed-point Inversion 的 LiDAR-事件对齐（ICP + LiDAR IMU odometry）复杂度较高
- 仅在两个数据集上验证（DSEC 室外 + M3ED 室内外）
- 虚拟模式的注入可能引入匹配歧义（相邻像素相似模式）
- 未来方向：学习最优注入模式（而非随机）、3D 场景变化时的深度更新策略

## 相关工作与启发

- VPP（Virtual Pattern Projection）在 RGB 立体中的成功启发了本文的事件域适配
- Guided Stereo Matching 和 LidarStereoNet 作为 baseline 对比展示了直接迁移的局限
- 事件相机-LiDAR 融合是新兴方向，本文开辟了立体匹配这一特定应用

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4.5 |
| 技术深度 | 4 |
| 实验充分性 | 4.5 |
| 写作质量 | 4.5 |
| 实用价值 | 4 |
| 总分 | 4.3 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection](detecting_as_labeling_rethinking_lidar-camera_fusion_in_3d_object_detection.md)
- [\[ECCV 2024\] DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion](dvlo_deep_visuallidar_odometry_with_localtoglobal_featu.md)
- [\[ECCV 2024\] MapDistill: Boosting Efficient Camera-based HD Map Construction via Camera-LiDAR Fusion Model Distillation](mapdistill_boosting_efficient_camera-based_hd_map_construction_via_camera-lidar_.md)
- [\[ECCV 2024\] OPEN: Object-wise Position Embedding for Multi-view 3D Object Detection](open_object-wise_position_embedding_for_multi-view_3d_object_detection.md)
- [\[ECCV 2024\] Monocular Occupancy Prediction for Scalable Indoor Scenes](monocular_occupancy_prediction_for_scalable_indoor_scenes.md)

</div>

<!-- RELATED:END -->
