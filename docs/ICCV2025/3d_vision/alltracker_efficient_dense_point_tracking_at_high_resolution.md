---
title: >-
  [论文解读] AllTracker: Efficient Dense Point Tracking at High Resolution
description: >-
  [ICCV 2025][3D视觉][dense point tracking] 提出AllTracker，将点跟踪问题转化为多帧长距离光流估计问题，通过低分辨率迭代推理（2D卷积+时间注意力）加高分辨率上采样，以16M参数实现高分辨率(768-1024像素)全像素稠密点跟踪的SOTA精度。
tags:
  - ICCV 2025
  - 3D视觉
  - dense point tracking
  - 光流
  - long-range correspondence
  - high-resolution tracking
  - recurrent architecture
---

# AllTracker: Efficient Dense Point Tracking at High Resolution

**会议**: ICCV 2025  
**arXiv**: 无  
**代码**: [项目页](https://alltracker.github.io)  
**领域**: 3D视觉 / 点跟踪  
**关键词**: dense point tracking, optical flow, long-range correspondence, high-resolution tracking, recurrent architecture

## 一句话总结

提出AllTracker，将点跟踪问题转化为多帧长距离光流估计问题，通过低分辨率迭代推理（2D卷积+时间注意力）加高分辨率上采样，以16M参数实现高分辨率(768-1024像素)全像素稠密点跟踪的SOTA精度。

## 研究背景与动机

视频中的长距离点跟踪是计算机视觉的基础问题。光流方法仅处理相邻帧间的瞬时运动，串联时会累积漂移；而现有点跟踪器（如CoTracker3）通过多帧时间先验解决漂移和遮挡穿越，但以空间感知为代价——只能处理稀疏点集，难以高分辨率稠密输出。近期"稠密"跟踪尝试（DTF、DELTA）不如最新稀疏跟踪器准确，且在高分辨率输入上内存溢出。核心洞察：**可学习的多帧时间先验可以与高分辨率空间感知共建**——通过将点跟踪重新定义为多帧长距离光流问题。

## 方法详解

### 整体框架

AllTracker估计一个"查询帧"到视频中每一帧的高分辨率光流场。采用滑动窗口策略处理长视频。架构核心是循环模块：在低分辨率网格上迭代改进对应估计，通过2D卷积传播空间信息，通过像素对齐注意力层传播时间信息。最终通过上采样层恢复到全分辨率。

### 关键设计

1. **长距离光流作为点跟踪**: 直接计算查询帧到每一帧的流场（而非仅相邻帧），采样流场得到任意点的长程轨迹。滑动窗口（16帧）内同时解多个流问题，窗口内和窗口间共享信息，实现跨越遮挡和大时间间隔的准确对应。这使稀疏跟踪器变得多余。

2. **低分辨率处理+高分辨率上采样**: 借鉴SEA-RAFT，在1/8分辨率网格上执行主要计算——先直接估计低分辨率流，用ResNet-34计算特征，构建多尺度代价体积金字塔，通过2D卷积迭代细化。最终用pixel-shuffle层快速上采样到全分辨率。参数仅16M，在40G GPU上可处理768-1024像素输入。

3. **联合训练光流+点跟踪数据集**: 设计统一的损失函数支持光流数据集（FlyingThings3D、Spring等）和点跟踪数据集（Kubric、PointOdyssey等）的联合训练。光流数据提供稠密且精确的2帧监督，点跟踪数据提供稀疏但长时的监督。联合训练对最终性能至关重要。

### 损失函数 / 训练策略

在多个合成数据集上联合训练，均匀采样。长训练计划对性能很关键。不使用任何伪标签自监督，仅用更多合成数据即可获得优异表现。

## 实验关键数据

### 主实验

| 方法 | 参数量 | 分辨率 | TAP-Vid评估 | 稠密/稀疏 |
|------|--------|--------|------------|----------|
| CoTracker3 | - | 标准 | SOTA(稀疏) | 稀疏 |
| DELTA | - | 低 | 次优 | 稠密 |
| DTF | - | 低 | 不竞争 | 稠密 |
| **AllTracker** | **16M** | **768-1024** | **SOTA** | **稠密** |

AllTracker在高分辨率稠密跟踪上达到SOTA，同时在稀疏评估上也超越最新的稀疏跟踪器。

### 消融实验

- 光流数据联合训练 vs 仅Kubric：联合训练显著提升
- 时间注意力层：去除后跨遮挡跟踪能力下降
- 低分辨率处理比例：1/8为最佳平衡点
- 训练计划长度：更长的训练带来更好的收敛

### 关键发现

- 光流和点跟踪可以在统一框架中协同解决
- 2D卷积在低分辨率网格上足以实现空间消息传播，无需复杂的Transformer
- 联合使用光流和跟踪数据集比单独使用效果更好
- 高分辨率上采样技术是被低估的关键组件

## 亮点与洞察

- 极简优雅的设计——将点跟踪回归到光流问题，统一了两个研究方向
- 16M参数实现SOTA，参数效率极高
- 稠密+高分辨率+SOTA精度的首次实现
- 联合训练多数据集的策略简单有效

## 局限与展望

- 仅在合成数据上训练，对真实世界的泛化依赖特征匹配的鲁棒性
- 滑动窗口策略在极长视频上可能存在窗口边界不一致
- 遮挡处理依赖时间注意力层的学习能力，无显式遮挡推理
- 计算开销仍随帧数线性增长

## 相关工作与启发

- SEA-RAFT提供了低分辨率处理+上采样的架构灵感
- CoTracker3的虚拟点设计虽精确但限制为稀疏跟踪
- RAFT的迭代细化策略被广泛采用
- 统一光流和跟踪的思路可扩展到3D场景流

## 评分

- 新颖性: ⭐⭐⭐⭐ — 将点跟踪回归光流问题，视角独特
- 技术深度: ⭐⭐⭐⭐ — 架构设计精妙，组件选择有理有据
- 实验充分性: ⭐⭐⭐⭐⭐ — 详尽消融、多基准、多分辨率评估
- 写作质量: ⭐⭐⭐⭐ — 动机清晰，相关工作分析到位
- 实用价值: ⭐⭐⭐⭐⭐ — 16M参数、高分辨率稠密跟踪、代码开源

<!-- RELATED:START -->

## 相关论文

- [\[ICCV 2025\] Multi-View 3D Point Tracking](multi-view_3d_point_tracking.md)
- [\[ICCV 2025\] ArgMatch: Adaptive Refinement Gathering for Efficient Dense Matching](argmatch_adaptive_refinement_gathering_for_efficient_dense_matching.md)
- [\[ICCV 2025\] TAPNext: Tracking Any Point (TAP) as Next Token Prediction](tapnext_tracking_any_point_tap_as_next_token_prediction.md)
- [\[ICCV 2025\] Efficient Spiking Point Mamba for Point Cloud Analysis](efficient_spiking_point_mamba_for_point_cloud_analysis.md)
- [\[ICCV 2025\] TurboReg: TurboClique for Robust and Efficient Point Cloud Registration](turboreg_turboclique_for_robust_and_efficient_point_cloud_registration.md)

<!-- RELATED:END -->
