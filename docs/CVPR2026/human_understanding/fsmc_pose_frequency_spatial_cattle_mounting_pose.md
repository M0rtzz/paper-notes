---
title: >-
  [论文解读] FSMC-Pose: Frequency and Spatial Fusion with Multiscale Self-calibration for Cattle Mounting Pose Estimation
description: >-
  [CVPR 2026][人体理解][牛群姿态估计] FSMC-Pose 提出了一种面向牧场密集场景的轻量级牛群爬跨姿态估计框架，通过频率-空间融合骨干网络 CattleMountNet 和多尺度自校准预测头 SC2Head，在参数仅 2.698M、4.4G FLOPs 下实现了89% AP的高精度。
tags:
  - CVPR 2026
  - 人体理解
  - 牛群姿态估计
  - 频率空间融合
  - 多尺度自校准
  - 爬跨检测
  - 轻量级
---

# FSMC-Pose: Frequency and Spatial Fusion with Multiscale Self-calibration for Cattle Mounting Pose Estimation

**会议**: CVPR 2026  
**arXiv**: [2603.16596](https://arxiv.org/abs/2603.16596)  
**代码**: [https://github.com/FSMC-Pose](https://github.com/FSMC-Pose)  
**领域**: 人体/动物姿态估计  
**关键词**: 牛群姿态估计, 频率空间融合, 多尺度自校准, 爬跨检测, 轻量级

## 一句话总结

FSMC-Pose 提出了一种面向牧场密集场景的轻量级牛群爬跨姿态估计框架，通过频率-空间融合骨干网络 CattleMountNet 和多尺度自校准预测头 SC2Head，在参数仅 2.698M、4.4G FLOPs 下实现了89% AP的高精度。

## 研究背景与动机

1. **领域现状**：动物姿态估计主要沿用人体姿态方法（自底向上/自顶向下），但农业生产场景的复杂性使这些方法难以直接部署。
2. **现有痛点**：爬跨是母牛发情的关键视觉指标，但牧场场景存在杂乱背景干扰、牛群间严重遮挡、相似毛色混淆等挑战；缺乏公开的牛群爬跨数据集。
3. **核心矛盾**：发情期牛群会聚集，爬跨场景比一般牧场更密集，四肢交织导致身份混淆，而实时监控要求低计算量。
4. **本文目标**：在密集、杂乱的真实牧场环境中实现准确的爬跨姿态估计，同时保持轻量计算。
5. **切入角度**：从频域增强前景-背景分离、多尺度感受野聚合、空间-通道自校准三个角度分别解决背景干扰、尺度变化和遮挡问题。
6. **核心 idea**：频率域小波变换增强牛体与背景的可分性 + 多感受野聚合处理关键点尺度差异 + 自校准分支纠正遮挡导致的结构错位。

## 方法详解

### 整体框架

自顶向下框架：先检测单头牛的边界框，再对每头牛进行关键点定位。骨干网络 CattleMountNet 基于倒置残差结构（depthwise separable convolution），嵌入 SFEBlock 和 RABlock 两个模块。预测头 SC2Head 基于 RTMPose，增加空间-通道注意力和自校准分支。

### 关键设计

1. **空间频率增强块 (SFEBlock)**:
    - 功能：增强牛体与杂乱背景的分离度
    - 核心思路：先用小波变换卷积(WTConv)将特征分解为低频/高频子带并分别卷积，提供多尺度频域建模和扩大感受野；再用固定的 $5 \times 5$ 高斯核平滑响应、抑制背景噪声。融合后通过 $1 \times 1$ 卷积压缩，元素乘法精化空间响应，残差连接保留原始信息。
    - 设计动机：牧场中泥土、阴影使牛体纹理与背景相似，需要在频域层面增强区分度

2. **感受野聚合块 (RABlock)**:
    - 功能：捕获多尺度上下文信息，处理从小蹄到大躯干的关键点尺度差异
    - 核心思路：在倒置残差单元上增加三个并行的 $3 \times 3$ 深度可分离卷积，膨胀率分别为 1/3/5，捕获局部/中距离/远距离上下文。三路特征相加后 LayerNorm 归一化，残差连接稳定训练。
    - 设计动机：单一尺度特征无法同时精确定位小关节和大躯干区域

3. **空间-通道自校准头 (SC2Head)**:
    - 功能：在遮挡和身份混淆下保持结构一致性
    - 核心思路：包含三个分支——空间注意力(SAB)通过平均/最大池化+卷积生成空间权重、通道注意力(CAB)通过全局池化+双分支交互生成通道权重、自校准分支(SCB)通过上下采样+卷积建立长程依赖。三分支输出融合：$C_o = f_{1\times1}([SA, CA]) \odot SC + X$
    - 设计动机：骨干网络的改进主要在早期特征提取层，预测头仍需处理交叠牛体间的结构混淆

### 损失函数 / 训练策略

- 基于 RTMPose 的坐标回归策略进行关键点预测
- 构建了 MOUNT-Cattle 数据集（1176个爬跨实例）并与公开 NWAFU-Cattle 合并
- 16个关键点标注，遵循 COCO 格式，支持即插即用训练

## 实验关键数据

### 主实验

| 方法 | 骨干 | AP/% | AP75/% | AR/% | FLOPs/G | Params/M |
|------|------|------|--------|------|---------|----------|
| RTMPose | CSPNext | 88.6 | 90.6 | 89.0 | 1.926 | 13.550 |
| FSMC-Pose | CattleMountNet | **89.0** | **92.5** | **89.9** | 4.411 | **2.698** |
| SimCC | ResNet50 | 87.4 | 91.0 | 89.9 | 5.493 | 36.753 |
| DEKR | HRNet | 87.2 | 90.3 | 89.0 | 44.416 | 29.548 |

### 消融实验

| 配置 | AP/% | 说明 |
|------|------|------|
| Baseline (RTMPose) | 88.6 | 基线 |
| + SFEBlock | 提升 | 频率增强改善前景-背景分离 |
| + RABlock | 提升 | 多尺度感受野改善尺度变化 |
| + SC2Head | 进一步提升 | 自校准改善遮挡下结构一致性 |
| Full FSMC-Pose | 89.0 | AP提升1.4%，参数减少80% |

### 关键发现

- FSMC-Pose 在 AP 上比 RTMPose 提升 1.4%，但参数量减少 80%（2.698M vs 13.550M）
- SC2Head 的自校准分支对遮挡场景改善最大
- 频域增强(SFEBlock)对杂乱背景场景特别有效

## 亮点与洞察

- **将频域处理（小波变换+高斯平滑）引入动物姿态估计**，巧妙解决了低对比度下的前景-背景分离问题
- **MOUNT-Cattle 数据集填补了牛群爬跨姿态的数据空白**，遵循 COCO 格式可直接复用现有方法
- 参数减少80%但精度更高，适合边缘部署的实际需求

## 局限与展望

- 数据集规模较小（仅1176个爬跨实例），可能限制泛化能力
- 仅在牛群场景验证，未测试对其他大型动物的泛化性
- 未结合时序信息，爬跨行为本身是动态过程

## 相关工作与启发

- **vs RTMPose**: 在其基础上引入频域增强和自校准机制，精度提升同时参数大幅减少
- **vs DeepLabCut**: 底向上方法在拥挤场景下个体区分能力差，本文的自顶向下+自校准方案更适合密集场景

## 评分

- 新颖性: ⭐⭐⭐ 模块设计合理但缺乏突破性创新
- 实验充分度: ⭐⭐⭐⭐ 多基线对比和消融完整
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰，方法描述详细
- 价值: ⭐⭐⭐⭐ 填补了牛群爬跨姿态估计的研究空白，有实际应用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Efficient Onboard Spacecraft Pose Estimation with Event Cameras and Neuromorphic Hardware](efficient_onboard_spacecraft_pose_estimation_with_event_cameras_and_neuromorphic_hardware.md)
- [\[CVPR 2026\] E-3DPSM: A State Machine for Event-Based Egocentric 3D Human Pose Estimation](e-3dpsm_a_state_machine_for_event-based_egocentric_3d_human_pose_estimation.md)
- [\[CVPR 2026\] Beyond the Fold: Quantifying Split-Level Noise and the Case for Leave-One-Dataset-Out AU Evaluation](beyond_the_fold_quantifying_split-level_noise_and_the_case_for_leave-one-dataset.md)
- [\[CVPR 2026\] How to Take a Memorable Picture? Empowering Users with Actionable Feedback](how_to_take_a_memorable_picture_empowering_users_with_actionable_feedback.md)
- [\[CVPR 2026\] LCA: Large-scale Codec Avatars - The Unreasonable Effectiveness of Large-scale Avatar Pretraining](lca_large-scale_codec_avatars_the_unreasonable_effectiveness_of_large-scale_avata.md)

</div>

<!-- RELATED:END -->
