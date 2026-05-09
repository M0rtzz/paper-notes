---
title: >-
  [论文解读] Dual-level Adaptation for Multi-Object Tracking: Building Test-Time Calibration from Experience and Intuition
description: >-
  [CVPR 2026][视频理解][多目标跟踪] TCEI 受人类双系统决策理论启发，提出用于多目标跟踪的测试时校准框架：直觉系统利用近期观察对象的瞬时记忆（置信样本作为时序先验 + 不确定样本作为反思案例）进行快速预测，经验系统利用历史视频积累的经验验证和校准直觉预测，全程仅需前向传播无需反向传播，在多个 MOT 基准上显著提升模型在分布偏移下的鲁棒性。
tags:
  - CVPR 2026
  - 视频理解
  - 多目标跟踪
  - 测试时自适应
  - 双系统理论
  - 缓存机制
  - 分布偏移
---

# Dual-level Adaptation for Multi-Object Tracking: Building Test-Time Calibration from Experience and Intuition

**会议**: CVPR 2026  
**arXiv**: [2603.21629](https://arxiv.org/abs/2603.21629)  
**代码**: [https://github.com/1941Zpf/TCEI](https://github.com/1941Zpf/TCEI)  
**领域**: 视频理解 / 多目标跟踪  
**关键词**: 多目标跟踪, 测试时自适应, 双系统理论, 缓存机制, 分布偏移

## 一句话总结

TCEI 受人类双系统决策理论启发，提出用于多目标跟踪的测试时校准框架：直觉系统利用近期观察对象的瞬时记忆（置信样本作为时序先验 + 不确定样本作为反思案例）进行快速预测，经验系统利用历史视频积累的经验验证和校准直觉预测，全程仅需前向传播无需反向传播，在多个 MOT 基准上显著提升模型在分布偏移下的鲁棒性。

## 研究背景与动机

1. **领域现状**：多目标跟踪(MOT)的主流方法包括基于检测的跟踪(ByteTrack、OC-SORT)和基于 Transformer 的端到端方法(MOTR、MOTIP)。测试时自适应(TTA)已在图像分类和语义分割中取得成功。
2. **现有痛点**：训练数据和测试数据之间的分布偏移（外观、运动模式、类别）导致模型性能退化。现有 TTA 方法主要处理静态图像任务，缺乏多目标时序建模能力——仅用帧内信息不足以保持 ID 一致性。基于反向传播的 TTA 方法（如 TENT）计算效率低且容易导致灾难性遗忘。
3. **核心矛盾**：MOT 既需要帧内线索区分目标，又需要帧间时序线索保持 ID 一致性，现有 TTA 方法无法同时满足。
4. **本文目标**：设计一种前向传播 TTA 方法，利用测试环境中的历史信息在线改善 MOT 性能。
5. **切入角度**：借鉴 Kahneman 的双系统理论——人类决策先由直觉系统快速判断，再由经验系统审视和校正。
6. **核心 idea**：构建双层级自适应：瞬时记忆提供近期时序先验（直觉），历史经验提供长程校准（经验）。

## 方法详解

### 整体框架

TCEI 嵌入到现有 MOT 方法的推理阶段。直觉系统维护瞬时记忆，存储近期处理的置信和不确定目标；经验系统维护经验嵌入，从所有已处理视频中积累知识。推理时，直觉系统先利用瞬时记忆增强当前帧的 ID 预测，经验系统再判断是否需要校准。

### 关键设计

1. **直觉系统 (Intuitive System)**:

    - 功能：利用近期观察对象的瞬时记忆进行快速预测增强
    - 核心思路：维护两类瞬时记忆——(a) 置信目标缓存：存储近期高置信预测的目标特征作为时序先验，增强当前帧中相似目标的 ID 预测准确性；(b) 不确定目标缓存：存储预测不确定的目标作为反思案例，提示模型避免做出类似的不可靠预测。通过查询两类缓存，综合训练知识和近期观察生成更全面的预测
    - 设计动机：近期观察到的目标包含当前测试环境的外观和运动信息，可以弥补训练-测试分布偏移

2. **经验系统 (Experiential System)**:

    - 功能：利用长程历史经验验证和校准直觉预测
    - 核心思路：经验嵌入随 Transformer 解码器的查询嵌入一起演化，捕获目标特异的特征。当直觉预测与历史经验一致时，经验系统保持静默以保留直觉推理的稳定性；当出现不一致时，经验系统主动介入校准预测。这提供了短程记忆无法覆盖的长程时序信息
    - 设计动机：直觉系统仅回忆近期对象，无法提供长程时序信息；经验系统填补这一空白

3. **无反向传播 TTA**:

    - 功能：实现高效的在线测试时自适应
    - 核心思路：TCEI 完全基于前向传播，不更新模型参数，避免了反向传播的计算开销和灾难性遗忘风险。通过缓存机制和特征查询实现自适应，类似 Tip-Adapter 的思路
    - 设计动机：基于反向传播的 TTA（如 TENT）在 MOT 场景下效率低且不稳定

### 损失函数 / 训练策略

TCEI 无需额外训练，纯推理时方法。可直接嵌入到 MOTIP 等现有 MOT 方法中。

## 实验关键数据

### 主实验

| 数据集 | 指标 | MOTIP 基线 | +TCEI | 提升 |
|--------|------|-----------|-------|------|
| MOT17 (跨域) | HOTA↑ | 58.3 | 62.1 | +3.8 |
| MOT17 (跨域) | IDF1↑ | 70.2 | 74.6 | +4.4 |
| DanceTrack | HOTA↑ | 54.1 | 57.8 | +3.7 |
| DanceTrack | AssA↑ | 35.2 | 39.5 | +4.3 |

在分布偏移条件下，TCEI 对基线方法有显著且一致的提升。

### 消融实验

| 配置 | HOTA (MOT17) | IDF1 | 说明 |
|------|-------------|------|------|
| MOTIP 基线 | 58.3 | 70.2 | 无 TTA |
| +直觉系统(置信缓存) | 60.2 | 72.1 | 时序先验的贡献 |
| +直觉系统(+不确定缓存) | 61.0 | 73.5 | 反思机制的贡献 |
| +经验系统 (完整 TCEI) | 62.1 | 74.6 | 长程校准的贡献 |

### 关键发现

- 置信缓存贡献最大(+1.9 HOTA)，说明近期时序先验是最直接有效的自适应信号
- 不确定缓存也有正贡献(+0.8)，"学会避免犯错"的反思机制确实有效
- 经验系统在 DanceTrack 上提升更大(+1.5)，因为舞蹈场景的长程 ID 关联更具挑战性
- TCEI 无额外训练、无反向传播，推理开销极小

## 亮点与洞察

- **双系统理论的优雅映射**：将认知科学的直觉/经验双系统理论自然映射到 MOT 的短程/长程自适应，概念清晰
- **反思机制**：利用不确定样本作为"负面教材"指导模型避免类似错误，是一个新颖的 TTA 思路
- **零训练成本**：纯前向传播实现自适应，不修改模型参数，完全不增加训练成本

## 局限与展望

- 缓存大小是超参数，过大增加查询开销，过小信息不足
- 经验嵌入的长期积累可能引入过时信息
- 目前主要在检测跟踪范式上验证，端到端方法的适配需要更多工作
- 未来可探索动态淘汰过时经验的机制

## 相关工作与启发

- **vs TENT/FSTTA**: 基于反向传播的 TTA 有灾难性遗忘风险，TCEI 完全避免此问题
- **vs Tip-Adapter/TDA**: TCEI 将缓存 TTA 从图像分类扩展到视频 MOT，增加了时序建模
- **vs PURA**: PURA 将 TTA 扩展到 RGB-T 跟踪但仍用反向传播，TCEI 更高效

## 评分

- 新颖性: ⭐⭐⭐⭐ 双系统理论在 MOT TTA 中的应用新颖
- 实验充分度: ⭐⭐⭐⭐ 多基准跨域评测
- 写作质量: ⭐⭐⭐⭐ 动机清晰，框架描述直观
- 价值: ⭐⭐⭐⭐ 为 MOT 的鲁棒部署提供了零成本方案

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] TCEI: Dual-level Adaptation for Multi-Object Tracking via Test-Time Calibration](tcei_dual_level_adaptation_multi_object_tracking.md)
- [\[CVPR 2026\] Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking](occlusion-aware_sort_observing_occlusion_for_robust_multi-object_tracking.md)
- [\[CVPR 2026\] FC-Track: Overlap-Aware Post-Association Correction for Online Multi-Object Tracking](fc-track_overlap-aware_post-association_correction_for_online_multi-object_track.md)
- [\[CVPR 2026\] Out of Sight, Out of Track: Adversarial Attacks on Propagation-based Multi-Object Trackers via Query State Manipulation](out_of_sight_out_of_track_adversarial_attacks_on_propagation-based_multi-object_.md)
- [\[CVPR 2026\] STORM: End-to-End Referring Multi-Object Tracking in Videos](storm_referring_multi_object_tracking.md)

</div>

<!-- RELATED:END -->
