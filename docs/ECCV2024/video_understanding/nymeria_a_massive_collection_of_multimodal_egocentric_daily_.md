---
title: >-
  [论文解读] Nymeria: A Massive Collection of Multimodal Egocentric Daily Motion in the Wild
description: >-
  [ECCV 2024][视频理解][egocentric motion] 构建了全球最大的野外人体运动数据集Nymeria：300小时日常活动、264人、50个场景、多设备多模态自我中心数据（Project Aria眼镜+手环+动捕服），配备亚毫秒级同步和310.5K句层次化运动语言描述。
tags:
  - ECCV 2024
  - 视频理解
  - egocentric motion
  - 多模态
  - motion-language
  - synchronization
  - SMPL
---

# Nymeria: A Massive Collection of Multimodal Egocentric Daily Motion in the Wild

**会议**: ECCV 2024  
**arXiv**: [2406.09905](https://arxiv.org/abs/2406.09905)  
**代码**: [Project Page](https://www.projectaria.com/datasets/nymeria)  
**领域**: 人体运动数据集 / 自我中心视觉  
**关键词**: egocentric motion, multimodal dataset, motion-language, synchronization, SMPL

## 一句话总结

构建了全球最大的野外人体运动数据集Nymeria：300小时日常活动、264人、50个场景、多设备多模态自我中心数据（Project Aria眼镜+手环+动捕服），配备亚毫秒级同步和310.5K句层次化运动语言描述。

## 研究背景与动机

**领域现状**：人体运动数据集是推动运动理解、合成和追踪算法的关键资源，但现有数据集在规模、模态丰富度和野外场景覆盖方面存在明显不足。

**现有痛点**：

1. **规模与多样性**：标记器/相机方案受视线遮挡限制，仅能在受控空间内采集短时运动；IMU方案有全局定位漂移

2. **多设备对齐**：不同采集设备之间的时间和空间同步精度不足，现有方法依赖视觉/音频线索，精度有限且干扰自然行为

3. **语言标注**：现有运动-语言数据集（如HumanML3D仅45K句）规模小、描述简短、缺乏场景上下文

**核心矛盾**：获取大规模、高质量、多模态、野外运动数据的三大挑战——野外动捕精度、多设备同步、丰富语言标注——难以同时解决。

## 方法详解

### 整体框架

每位参与者穿戴XSens MVN Link动捕服（17个IMU）+ Project Aria眼镜（RGB/灰度/ET/IMU等多传感器）+ 两个miniAria手环 + 同步设备 → 亚毫秒级硬件同步 → MPS空间定位 → XSens骨架重定向到SMPL参数化模型 + 全局漂移修正 → 层次化语言标注。

### 关键设计

1. **亚毫秒级硬件同步方案**

    - 设计专用同步设备，向所有设备提供统一时间信号
    - 可选接收来自无线服务器的时间参考（~100m范围），支持多人同时采集
    - XSens与Aria的对齐精度在1个运动帧内（4.2ms）
    - 设计动机：避免基于视觉/音频的后处理同步对自然行为的干扰

2. **全身参数化运动表示与漂移修正**

    - 开发新算法将XSens骨架运动重定向为SMPL全身参数化模型
    - 利用Project Aria MPS的SLAM输出进行全局漂移优化修正
    - 提供260M个body pose帧，平均每段录制15分钟
    - 设计动机：IMU动捕的累积漂移是野外数据集的核心精度瓶颈

3. **层次化运动-语言标注体系**

    - 三层标注：细粒度运动叙述 → 简化原子动作 → 高层活动摘要
    - 310.5K句、8.64M词、6545词汇量——规模远超HumanML3D（45K句/5371词汇）
    - 标注包含场景上下文（in-context），而非抽象的动作标签

### 数据采集策略

- 20种场景（室内：烹饪、工作、娱乐；室外：徒步、骑行、运动等）
- 每人4-8段录制，每段15-20分钟
- 额外第三视角"观察者"穿戴Aria记录参与者
- 隐私保护：EgoBlur去识别化处理面部和车牌

## 实验关键数据

### 数据集规模对比

| 数据集 | 时长(h) | 姿态帧(M) | 均长(min) | 参与者 | 语言句(K) | 词汇量 |
|--------|---------|-----------|-----------|--------|-----------|--------|
| AMASS | 42 | 0.9 | 0.22 | 346 | - | - |
| HumanML3D | 28.6 | 2.9 | 0.12 | - | 45.0 | 5371 |
| EgoExo4D | 88.8 | 9.6 | 2.6 | 740 | 432 | 4405 |
| MotionX | 144 | 15.6 | 0.11 | - | 81.1 | - |
| **Nymeria** | **300** | **260** | **15** | **264** | **310.5** | **6545** |

### Benchmark 实验

**自我中心身体追踪**

| 方法 | 输入条件 | 全局 MPJPE(cm)↓ |
|------|---------|-----------------|
| AvatarPoser | 头部6DOF | 18.7 |
| AGRoL | 头部6DOF | 15.3 |
| AGRoL | + 手环IMU | 12.1 |
| AGRoL | + 手环6DOF | 10.8 |

### 关键发现

- 300小时是此前最大野外数据集（EgoExo4D 88.8h）的3.4倍，姿态帧数是27倍
- 运动-语言数据规模是HumanML3D的6.9倍，首次提供场景内上下文描述
- 手环IMU/6DOF的加入能进一步降低追踪误差（MPJPE从15.3降至10.8）
- 15分钟的平均录制时长远超现有数据集（通常<1分钟），捕捉了自然长时活动

## 亮点与洞察

- 工程贡献突出：亚毫秒级硬件同步 + XSens到SMPL重定向 + 全局漂移修正的完整pipeline是数据集技术壁垒
- miniAria手环是首创，为未来AR/VR设备的运动追踪研究提供了新的数据通道
- 层次化运动-语言标注（叙述→原子动作→活动摘要）比现有单层标注更有利于多粒度运动理解
- 首次为自我中心运动数据提供了第三人称同步视角

## 局限性 / 可改进方向

- XSens动捕服精度低于光学标记系统，手部和面部精度有限
- 264人在体型/年龄/运动能力方面的多样性可能不足
- 语言标注质量依赖标注者经验，一致性可能存在偏差
- 仅提供SMPL模型，未覆盖SMPL-X（手部+面部建模）
- 场景3D重建精度受限于SLAM输出质量

## 相关工作与启发

- **vs AMASS**：AMASS汇编了多个标记基数据集但缺乏场景上下文，Nymeria提供完整的多模态环境信息
- **vs EgoExo4D**：EgoExo4D规模大但缺乏参数化运动表示，Nymeria提供SMPL全身模型
- **vs MotionX**：MotionX时长更长但平均片段仅6.6秒，Nymeria 15分钟长录制更适合建模长时活动
- **vs HumanML3D**：运动-语言数据量6.9倍提升，且首次提供in-context描述

## 评分

- 新颖性: ⭐⭐⭐⭐ 首个大规模多设备同步的野外自我中心运动数据集
- 实验充分度: ⭐⭐⭐ 提供了追踪/合成/动作识别benchmark，但baseline实验偏简略
- 写作质量: ⭐⭐⭐⭐ 数据集构建流程描述详尽，统计数据丰富
- 价值: ⭐⭐⭐⭐⭐ 数据集规模和模态丰富度具有标志性意义

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Data Collection-Free Masked Video Modeling](data_collection-free_masked_video_modeling.md)
- [\[ECCV 2024\] SemTrack: A Large-Scale Dataset for Semantic Tracking in the Wild](semtrack_a_large-scale_dataset_for_semantic_tracking_in_the_wild.md)
- [\[ECCV 2024\] AMEGO: Active Memory from Long EGOcentric Videos](amego_active_memory_from_long_egocentric_videos.md)
- [\[ECCV 2024\] Motion-prior Contrast Maximization for Dense Continuous-Time Motion Estimation](motion-prior_contrast_maximization_for_dense_continuous-time_motion_estimation.md)
- [\[ECCV 2024\] IAM-VFI: Interpolate Any Motion for Video Frame Interpolation with Motion Complexity Map](iam-vfi_interpolate_any_motion_for_video_frame_interpolation_with_motion_complex.md)

<!-- RELATED:END -->
