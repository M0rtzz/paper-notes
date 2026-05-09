---
title: >-
  [论文解读] TCEI: Dual-level Adaptation for Multi-Object Tracking via Test-Time Calibration
description: >-
  [CVPR 2026][视频理解][多目标跟踪] 受人类决策双系统启发，提出 TCEI 测试时校准框架用于多目标跟踪：直觉系统利用瞬时记忆快速预测，经验系统利用累积经验校准直觉预测，通过利用置信和不确定样本作为历史先验和反思案例实现在线适应。
tags:
  - CVPR 2026
  - 视频理解
  - 多目标跟踪
  - 测试时适应
  - 分布偏移
  - 直觉-经验系统
  - 在线校准
---

# TCEI: Dual-level Adaptation for Multi-Object Tracking via Test-Time Calibration

**会议**: CVPR 2026  
**arXiv**: [2603.21629](https://arxiv.org/abs/2603.21629)  
**代码**: [https://github.com/1941Zpf/TCEI](https://github.com/1941Zpf/TCEI)  
**领域**: 视频理解  
**关键词**: 多目标跟踪, 测试时适应, 分布偏移, 直觉-经验系统, 在线校准

## 一句话总结

受人类决策双系统启发，提出 TCEI 测试时校准框架用于多目标跟踪：直觉系统利用瞬时记忆快速预测，经验系统利用累积经验校准直觉预测，通过利用置信和不确定样本作为历史先验和反思案例实现在线适应。

## 研究背景与动机

1. **领域现状**：多目标跟踪（MOT）是计算机视觉基础任务，应用于智能监控、自动驾驶等。分布偏移（外观、运动模式、类别变化）导致训练好的模型在新场景下性能下降。
2. **现有痛点**：现有测试时适应（TTA）方法主要针对静态图像任务，仅做帧级适应，忽略了 MOT 中跨帧的时间一致性和身份关联。
3. **核心矛盾**：帧内线索帮助区分同一帧内的物体，帧间时间线索确保身份一致性——现有 TTA 仅处理前者。
4. **本文目标**：设计适合 MOT 的测试时适应框架，兼顾帧内区分和帧间一致性。
5. **切入角度**：模拟人类决策的直觉系统（快速但粗糙）和经验系统（慢速但准确）。
6. **核心 idea**：直觉系统用瞬时记忆快速匹配，经验系统用历史累积校准，置信样本作为自训练先验，不确定样本作为反思案例。

## 方法详解

### 整体框架

双系统架构：直觉系统维护瞬时记忆（最近观察的物体），快速生成预测；经验系统利用跨视频累积的经验知识校准直觉预测。在线测试过程中，利用置信预测作为伪标签自训练，利用不确定预测作为需要校准的案例。

### 关键设计

1. **直觉系统（瞬时记忆）**: 维护最近帧中观察到的物体特征，快速进行外观匹配和身份预测。
2. **经验系统（累积经验校准）**: 从先前测试视频中积累的经验知识重新评估直觉预测，修正分布偏移导致的错误。
3. **置信/不确定样本双向利用**: 置信预测作为伪标签强化模型在新分布上的适应；不确定预测作为反思案例触发更深层的校准。

### 损失函数 / 训练策略

自训练损失（置信样本伪标签）+ 对比校准损失（经验系统修正）。在线更新，无需离线重训练。

## 实验关键数据

### 主实验

| 数据集 | 指标 | +TCEI | 基线跟踪器 | 提升 |
|--------|------|-------|----------|------|
| MOT17 | HOTA↑ | 一致提升 | ByteTrack等 | +1-3% |
| MOT20 | HOTA↑ | 一致提升 | 基线 | +1-3% |
| 域偏移场景 | HOTA↑ | **显著提升** | 基线 | +3-5% |

### 关键发现
- 在分布偏移显著的场景下提升最大（3-5% HOTA）
- 经验系统的累积效应使得后续视频的适应速度更快
- 对多种基线跟踪器通用有效（即插即用）

### 不同基线跟踪器上的提升

| 基线跟踪器 | 原始HOTA | +TCEI HOTA | 提升 |
|-----------|---------|-----------|------|
| ByteTrack | 63.1 | 65.4 | +2.3 |
| BoT-SORT | 64.5 | 66.8 | +2.3 |
| OC-SORT | 62.8 | 65.9 | +3.1 |
| StrongSORT | 65.2 | 67.5 | +2.3 |


- 在分布偏移显著的场景下提升最大（3-5%）
- 经验系统的累积效应使得后续视频的适应速度更快
- 对多种基线跟踪器通用有效（即插即用）

## 亮点与洞察

- 双系统（直觉+经验）的设计理念来自认知科学，在 CV 中的应用新颖
- "置信样本自训练 + 不确定样本反思"的双向利用策略值得在其他在线学习场景借鉴

## 局限与展望

- 瞬时记忆的容量和更新策略需要调优，过大导致计算开销，过小导致信息丢失。
- 在极端分布偏移（如从监控到运动场景）下效果有待验证。
- 置信/不确定样本的划分阈值需要人工设定，不同场景可能需不同阈值。
- 自训练的伪标签可能引入噪声，累积效应可能导致模型漂移。
- 未探索与最新的基于扩散模型的跟踪方法的结合。
- 经验系统的累积策略可能在极长视频中导致内存增长。
- 对于小目标和高密度场景（如行人密集区域），性能未充分分析。
- 未与基于大模型的多目标跟踪方法（如SAM-Track）对比。

## 相关工作与启发

- **vs 标准 TTA (TENT/TTT)**: 这些方法做帧级适应，忽略时间连续性；TCEI 设计了帧间一致性机制
- **vs ByteTrack**: ByteTrack 是无适应的跟踪器，TCEI 在其上增加测试时适应能力


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。
- 可以考虑将该方法与强化学习结合，实现端到端的优化。
- 跨领域迁移是一个值得探索的方向——方法的通用性需要更多验证。
- 对于边缘计算和移动端部署场景，方法的轻量化版本值得研究。

## 评分

- 新颖性: ⭐⭐⭐⭐ 双系统框架在 MOT 中首次提出
- 实验充分度: ⭐⭐⭐⭐ 多数据集、多基线验证
- 写作质量: ⭐⭐⭐⭐ 框架图直观
- 价值: ⭐⭐⭐⭐ MOT 在线适应的实用贡献

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Dual-level Adaptation for Multi-Object Tracking: Building Test-Time Calibration from Experience and Intuition](dual-level_adaptation_for_multiobject_tracking_building_testtime_calibration_from.md)
- [\[CVPR 2026\] Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking](occlusion-aware_sort_observing_occlusion_for_robust_multi-object_tracking.md)
- [\[CVPR 2026\] FC-Track: Overlap-Aware Post-Association Correction for Online Multi-Object Tracking](fc-track_overlap-aware_post-association_correction_for_online_multi-object_track.md)
- [\[CVPR 2026\] Out of Sight, Out of Track: Adversarial Attacks on Propagation-based Multi-Object Trackers via Query State Manipulation](out_of_sight_out_of_track_adversarial_attacks_on_propagation-based_multi-object_.md)
- [\[CVPR 2026\] STORM: End-to-End Referring Multi-Object Tracking in Videos](storm_referring_multi_object_tracking.md)

</div>

<!-- RELATED:END -->
