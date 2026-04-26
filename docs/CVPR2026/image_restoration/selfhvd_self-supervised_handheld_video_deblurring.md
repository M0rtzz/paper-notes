---
title: >-
  [论文解读] SelfHVD: Self-Supervised Handheld Video Deblurring
description: >-
  [CVPR 2026][图像恢复][视频去模糊] SelfHVD 利用手持视频中自然存在的清晰帧作为监督信号，通过自增强视频去模糊（SEVD）构建高质量训练对和自约束空间一致性维护（SCSCM）防止位移偏移，实现了无需配对数据的手持视频去模糊。
tags:
  - CVPR 2026
  - 图像恢复
  - 视频去模糊
  - 自监督学习
  - 手持设备
  - 光学防抖
  - 自增强训练
---

# SelfHVD: Self-Supervised Handheld Video Deblurring

**会议**: CVPR 2026  
**arXiv**: [2508.08605](https://arxiv.org/abs/2508.08605)  
**代码**: https://cshonglei.github.io/SelfHVD  
**领域**: 图像恢复  
**关键词**: 视频去模糊, 自监督学习, 手持设备, 光学防抖, 自增强训练

## 一句话总结
SelfHVD 利用手持视频中自然存在的清晰帧作为监督信号，通过自增强视频去模糊（SEVD）构建高质量训练对和自约束空间一致性维护（SCSCM）防止位移偏移，实现了无需配对数据的手持视频去模糊。

## 研究背景与动机
1. **领域现状**：学习式视频去模糊方法在网络设计上取得了很大进展，但其预训练模型通常只对与训练样本类似的模糊数据有效。
2. **现有痛点**：手持视频的模糊不仅受相机抖动影响，还受OIS校正影响，其模糊分布与现有训练数据集（如GoPro、BSD）显著不同，导致现有模型表现不佳。
3. **核心矛盾**：采集配对手持视频去模糊数据集成本高昂且过程复杂，但直接使用合成模糊数据又存在域差距。
4. **本文目标**：利用手持视频中自然存在的清晰帧，以自监督方式学习去模糊模型，避免对配对数据的需求。
5. **切入角度**：当拍摄设备运动轨迹简单（如直线）且速度缓慢时，OIS可以正常工作，产生清晰帧。这些清晰帧可为相邻模糊帧提供去模糊线索和监督。
6. **核心idea**：清晰帧→对齐监督→SEVD自增强超越清晰帧上限→SCSCM防止空间漂移。

## 方法详解

### 整体框架
给定手持模糊视频，首先通过拉普拉斯方差+Otsu阈值选择清晰帧，将其对齐后作为去模糊模型的监督信号。然后通过SEVD构建更高质量的训练对来提升模型，通过SCSCM防止输入输出之间的空间位移。

### 关键设计

1. **清晰帧选择与对齐**:
    - 功能：从手持视频中自动识别清晰帧并与模糊帧对齐
    - 核心思路：用图像拉普拉斯的方差 $v_l(\mathbf{I})$ 衡量清晰度，通过Otsu方法自动确定阈值。将视频分段（每段20帧），确保清晰帧均匀分布。使用SEA-RAFT光流模型对齐清晰帧与模糊帧，同时设计不确定性掩码 $\mathbf{M}_{uncer}$ 和遮挡掩码 $\mathbf{M}_{occ}$ 排除错误对齐和遮挡区域。
    - 设计动机：清晰帧是手持视频的自然产物，选择准确率在GoProShake上达96.77%，HVD上达91.88%。

2. **自增强视频去模糊（SEVD）**:
    - 功能：利用模型自身的去模糊能力构建更高质量的训练数据
    - 核心思路：（1）随机清晰线索移除（RSCR）：随机将输入视频中的清晰帧替换为相邻模糊帧，得到更少线索的视频 $\tilde{\mathbf{B}}$；（2）监督信息选择（SIS）：在对齐的清晰帧 $\mathbf{S}_{j \to i}$ 和原始视频的去模糊结果 $\mathcal{D}(\mathbf{B})_k$ 中选择更好的作为 $\tilde{\mathbf{B}}$ 的监督。当对齐清晰帧未过度失真且更清晰时用清晰帧，否则用去模糊结果（stop gradient）。
    - 设计动机：直接以清晰帧为监督的上限就是清晰帧本身；SEVD使模型能超越输入中最清晰帧的质量，且能处理物体运动模糊。

3. **自约束空间一致性维护（SCSCM）**:
    - 功能：防止训练过程中输入输出之间的空间位移
    - 核心思路：基于信息瓶颈理论的观察——训练早期模型能保持空间一致性，后期才出现位移。用历史模型（第 $e$ 次迭代的参数 $\Theta_{\mathcal{D}_e}$）的输出作为辅助监督 $\mathcal{L}_{scscm} = \|\tilde{\mathbf{R}}_i - sg(\mathbf{R}_k^e)\|_1$，约束当前输出与历史结果的空间一致性。
    - 设计动机：光流对齐不可能完美，微小的对齐误差会随训练积累导致空间位移。利用早期模型天然保持空间一致性的特性作为正则化。

### 损失函数 / 训练策略
总损失 = 重建损失 $\mathcal{L}_{rec}$（使用掩码的L1） + SEVD损失 $\mathcal{L}_{sevd}$（条件选择的L1） + SCSCM损失 $\mathcal{L}_{scscm}$（历史模型约束的L1）。

## 实验关键数据

### 主实验

| 数据集 | 指标 | SelfHVD | Ren et al. | DaDeblur | 提升 |
|--------|------|---------|-----------|---------|------|
| GoProShake | PSNR | 最优 | 次优 | - | 显著提升 |
| HVD (真实) | 视觉质量 | 最优 | - | 次优 | 明显更清晰 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| Full SelfHVD | 最优 | 完整模型 |
| 仅清晰帧监督 | 基础水平 | 上限受限于清晰帧质量 |
| +SEVD | 显著提升 | 自增强突破上限 |
| +SCSCM | 进一步提升 | 防止空间漂移 |
| 不确定性+遮挡掩码 | 优于无掩码 | 排除错误对齐区域 |

### 关键发现
- SEVD能让模型超越输入视频中最清晰帧的质量，是最关键的贡献。
- SCSCM在训练后期尤为重要，没有它模型会逐渐出现空间漂移。
- 该方法对物体运动模糊也有一定的修复能力，因为SEVD利用了跨帧的清晰信息。

## 亮点与洞察
- **自监督的闭环设计**非常巧妙：清晰帧→模型→更好的监督→更好的模型。
- **信息瓶颈理论的实用化**：利用训练早期空间一致性好的观察设计SCSCM，理论指导实践。
- 方法对去模糊网络架构是通用的，可适配多种backbone。

## 局限与展望
- 依赖视频中存在足够的清晰帧，对全程严重模糊的视频不适用。
- 光流模型的准确性仍是瓶颈，复杂运动场景的对齐可能不准确。
- 未来可探索与基于扩散模型的去模糊方法结合。

## 相关工作与启发
- **vs Ren et al.**: 使用随机生成的模糊核来模糊清晰帧构建训练对，但合成模糊与真实模糊仍有差距。本文直接利用真实清晰帧+自增强策略更接近真实分布。
- **vs DaDeblur**: 使用扩散模型来模糊清晰图像，但生成的模糊仍非真实模糊。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ SEVD自增强训练和SCSCM空间一致性维护都是创新贡献
- 实验充分度: ⭐⭐⭐⭐ 合成+真实数据集验证，消融完整
- 写作质量: ⭐⭐⭐⭐ 方法动机清晰，逻辑链条完整
- 价值: ⭐⭐⭐⭐ 解决了手持视频去模糊的实际痛点

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Domain-Adaptive Video Deblurring via Test-Time Blurring](../../ECCV2024/image_restoration/domain-adaptive_video_deblurring_via_test-time_blurring.md)
- [\[CVPR 2026\] TM-BSN: Triangular-Masked Blind-Spot Network for Real-World Self-Supervised Image Denoising](tm-bsn_triangular-masked_blind-spot_network_for_real-world_self-supervised_image.md)
- [\[ECCV 2024\] Asymmetric Mask Scheme for Self-supervised Real Image Denoising](../../ECCV2024/image_restoration/asymmetric_mask_scheme_for_self-supervised_real_image_denoising.md)
- [\[ICML 2025\] TimeDART: A Diffusion Autoregressive Transformer for Self-Supervised Time Series Representation](../../ICML2025/image_restoration/timedart_a_diffusion_autoregressive_transformer_for_self-supervised_time_series_.md)
- [\[NeurIPS 2025\] MoE-Gyro: Self-Supervised Over-Range Reconstruction and Denoising for MEMS Gyroscopes](../../NeurIPS2025/image_restoration/moe-gyro_self-supervised_over-range_reconstruction_and_denoising_for_mems_gyrosc.md)

<!-- RELATED:END -->
