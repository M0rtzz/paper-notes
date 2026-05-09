---
title: >-
  [论文解读] FreeInit: Bridging Initialization Gap in Video Diffusion Models
description: >-
  [ECCV 2024][视频扩散模型] 提出 FreeInit，一种无需额外训练的推理采样策略，通过迭代精炼初始噪声的时空低频分量来弥合视频扩散模型训练与推理之间的初始化差距，显著提升生成视频的时序一致性。
tags:
  - ECCV 2024
  - 视频扩散模型
  - 初始噪声
  - 时序一致性
  - 频域分析
  - 视频生成
---

# FreeInit: Bridging Initialization Gap in Video Diffusion Models

**会议**: ECCV 2024  
**arXiv**: [2312.07537](https://arxiv.org/abs/2312.07537)  
**代码**: [https://github.com/TianxingWu/FreeInit](https://github.com/TianxingWu/FreeInit)  
**领域**: 视频生成  
**关键词**: 视频扩散模型, 初始噪声, 时序一致性, 频域分析, 推理策略

## 一句话总结

提出 FreeInit，一种无需额外训练的推理采样策略，通过迭代精炼初始噪声的时空低频分量来弥合视频扩散模型训练与推理之间的初始化差距，显著提升生成视频的时序一致性。

## 研究背景与动机

### 领域现状

**领域现状**：当前视频扩散模型（如 AnimateDiff、ModelScope、VideoCrafter）生成的视频存在时序不一致和不自然动态的问题

### 现有痛点

**现有痛点**：作者深入研究了视频扩散模型的噪声初始化过程，发现了一个隐式的训练-推理差距（initialization gap）

### 解决思路

**解决思路**：核心发现**：
  1. 扩散过程无法完全腐蚀干净latent中的信息，尤其是时空低频分量——即使在 t=1000 步仍保留大量低频信息
  2. 初始噪声的低频分量对生成结果有决定性影响——即使替换80%的高频成分，生成结果仍大致不变

### 核心矛盾

**核心矛盾**：训练时初始噪声由真实视频加噪得到，低频带保留了帧间时序相关性；推理时用独立高斯噪声，完全无时序相关性

### 补充说明

**补充说明**：这种差距导致推理时模型面对无关联噪声难以生成时序一致的视频

## 方法详解

### 整体框架

FreeInit 在推理阶段通过迭代的"去噪-加噪-重初始化"流程，逐步将初始噪声的低频分量引导至接近训练分布：

1. **初始化**：采样高斯噪声 ε，执行标准 DDIM 采样得到去噪 latent z₀
2. **前向扩散**：用原始噪声 ε 将 z₀ 重新加噪到 z_T（使用同一噪声以保留中频带的时空相关性）
3. **噪声重初始化**：在频域中组合 z_T 的低频分量与新随机噪声 η 的高频分量
4. **迭代采样**：用重初始化的噪声 z'_T 作为下一轮 DDIM 采样的起点

### 关键设计

- **时空频率分析**：使用 3D FFT 对视频 latent 进行时空频率分解，发现 SNR 在低频段远高于高频段
- **频域滤波器**：使用高斯低通滤波器（GLPF），归一化截止频率 D₀=0.25，分离低频和高频分量
- **噪声重初始化公式**：
    - 低频部分：F^L_zT = FFT₃D(z_T) ⊙ H（保留 z_T 的低频）
    - 高频部分：F^H_η = FFT₃D(η) ⊙ (1-H)（取随机噪声的高频）
    - 合并：z'_T = IFFT₃D(F^L_zT + F^H_η)
- **复用原始噪声**：前向扩散过程中使用与 DDIM 采样相同的噪声 ε，避免在中频段引入不确定性

### 损失函数 / 训练策略

- **无需任何训练或微调**，纯推理时方法
- 使用 4 次 FreeInit 迭代，参数对所有模型保持一致
- 代价是推理时间增加（每次迭代需完整 DDIM 采样），但质量显著提升

## 实验关键数据

### 主实验

| 方法 | UCF-101 DINO↑ | MSR-VTT DINO↑ |
|------|--------------|---------------|
| AnimateDiff | 85.24 | 83.24 |
| AnimateDiff+FreeInit | **92.01** | **91.86** |
| ModelScope | 88.16 | 88.95 |
| ModelScope+FreeInit | **91.11** | **93.28** |
| VideoCrafter | 85.62 | 84.68 |
| VideoCrafter+FreeInit | **89.27** | **88.72** |

运动质量指标（FVD↓）：

| 方法 | FVD↓ | MS(|Δ_UCF|↓) | DD(|Δ_UCF|↓) |
|------|------|-------------|-------------|
| AnimateDiff | 1340.96 | 7.33 | 20.2 |
| AnimateDiff+FreeInit | **1032.47** | **0.04** | **1.53** |

### 消融实验

- **滤波器类型**：高斯低通滤波器优于 Butterworth 和理想滤波器
- **截止频率 D₀**：D₀=0.25 为最佳平衡点；过大保留过多低频导致过平滑，过小无法有效补偿
- **迭代次数**：DINO 指标随迭代单调递增，4次迭代已接近收敛
- **滤波器可调性**：不同基础模型可通过调整滤波器参数获得更优结果

### 关键发现

1. 低频分量对视频生成起决定性作用——仅保留20%低频信息就能保持生成结果的整体分布
2. FreeInit 在所有三个基础模型上均一致性提升，证明方法的通用性
3. 运动平滑度和动态程度更接近真实视频分布

## 亮点与洞察

- **频域视角的创新分析**：首次从频域角度系统研究视频扩散模型的初始噪声问题
- **优雅简洁**：不引入任何可学习参数，纯频域操作，即插即用
- **理论与实践统一**：SNR 分析为低频信息泄漏提供了理论支撑
- **通用性强**：适用于任意视频扩散模型，无需针对模型定制

## 局限与展望 / 可改进方向

- 推理时间线性增加（N 次迭代 = N 倍推理时间），4次迭代代价较大
- 频率滤波器参数（D₀、类型）需要针对不同模型手动调整以获得最优效果
- 主要解决时序一致性问题，对生成内容的语义丰富度提升有限
- 理论分析基于 Stable Diffusion 噪声调度，对其他调度方案的适用性未充分验证
- 未来可探索自适应选择截止频率或减少迭代次数的加速策略

## 相关工作与启发

- PYoCo 关注训练阶段的渐进视频噪声先验，FreeInit 则专注推理阶段且无需微调
- 与图像域的 Common Diffusion Noise Schedules 工作相呼应，扩展到视频域的时空频率分析
- 频域分析方法可类推到其他基于扩散的生成任务（如 3D 生成、音频生成）

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4 |
| 技术深度 | 4 |
| 实验充分性 | 4 |
| 写作质量 | 4.5 |
| 实用价值 | 4.5 |
| 总分 | 4.2 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Exploring Pre-trained Text-to-Video Diffusion Models for Referring Video Object Segmentation](exploring_pretrained_texttovideo_diffusion_models_for_referr.md)
- [\[ECCV 2024\] SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](sv3d_novel_multi-view_synthesis_and_3d_generation_from_a_single_image_using_late.md)
- [\[ECCV 2024\] Kalman-Inspired Feature Propagation for Video Face Super-Resolution](kalman-inspired_feature_propagation_for_video_face_super-resolution.md)
- [\[ECCV 2024\] VFusion3D: Learning Scalable 3D Generative Models from Video Diffusion Models](vfusion3d_learning_scalable_3d_generative_models_from_video_diffusion_models.md)
- [\[CVPR 2025\] VideoGuide: Improving Video Diffusion Models without Training Through a Teacher's Guide](../../CVPR2025/video_generation/videoguide_improving_video_diffusion_models_without_training_through_a_teachers_.md)

</div>

<!-- RELATED:END -->
