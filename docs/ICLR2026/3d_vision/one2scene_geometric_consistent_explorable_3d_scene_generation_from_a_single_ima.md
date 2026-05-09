---
title: >-
  [论文解读] One2Scene: Geometric Consistent Explorable 3D Scene Generation from a Single Image
description: >-
  [ICLR 2026][3D视觉][3D Scene Generation] 提出 One2Scene 三阶段框架，将单图生成可探索 3D 场景分解为全景生成→前馈 3D 高斯溅射构建几何支架→支架引导的新视角合成，通过将全景深度估计重新表述为多视图立体匹配问题，实现几何一致且可自由探索的 3D 场景生成。
tags:
  - ICLR 2026
  - 3D视觉
  - 3D Scene Generation
  - Gaussian Splatting
  - Novel View Synthesis
  - Panorama
  - Feed-forward Reconstruction
---

# One2Scene: Geometric Consistent Explorable 3D Scene Generation from a Single Image

**会议**: ICLR 2026  
**arXiv**: [2602.19766](https://arxiv.org/abs/2602.19766)  
**代码**: [https://one2scene5406.github.io/](https://one2scene5406.github.io/)  
**领域**: 3D视觉/场景生成  
**关键词**: 3D Scene Generation, Gaussian Splatting, Novel View Synthesis, Panorama, Feed-forward Reconstruction  

## 一句话总结

提出 One2Scene 三阶段框架，将单图生成可探索 3D 场景分解为全景生成→前馈 3D 高斯溅射构建几何支架→支架引导的新视角合成，通过将全景深度估计重新表述为多视图立体匹配问题，实现几何一致且可自由探索的 3D 场景生成。

## 背景与动机

### 现有痛点

**现有痛点**：**领域现状**：1. **单图 3D 场景生成是高度欠定问题**：从一张图像生成可自由探索的 3D 场景，缺乏 3D 几何信息，现有方法在大视角变化时产生严重几何畸变和伪影。
2. **重建方法需要密集输入**：NeRF 和 3DGS 通常需要数百张输入图像；稀疏视角重建方法难以外推到未观测区域。
3. **视频扩散方法几何不一致**：基于视频生成的 3D 场景方法（ReconX、ViewCrafter 等）在长序列和闭环场景中几何误差累积，导致崩溃。
4. **全景方法探索范围有限**：DreamScene360、DreamCube 等将全景转 3D 场景，但仅支持有限的视角探索，远视角渲染质量急剧下降。
5. **迭代导航方法误差累积**：WonderJourney 等逐步导航+修补方法会导致全局语义漂移和拉伸畸变。
6. **尺度模糊问题**：单图输入使 SEVA 等方法存在尺度模糊，物体大小失真，甚至相机穿墙等物理不合理现象。

## 方法详解

### 整体架构：三阶段分解

将欠定的单图生成场景问题分解为三个可处理的子任务：

**阶段一：全景锚点视角生成**

- 使用 Hunyuan-Pano-DiT 将单张输入图像扩展为 360° 全景
- 全景提供全局覆盖，缓解信息不足问题
- 相比直接生成任意新视角，单图→全景是更良定的任务

**阶段二：前馈 3D 高斯几何支架**

核心创新——将全景深度估计重新表述为多视图立体匹配：

1. **锚点视角投影**：将 360° 全景投影为 6 个透视 cubemap 视角（FoV 扩展到 95°，相邻视角有 2.5° 重叠），利用大规模多视图数据集的几何先验
2. **双向融合模块**：在预训练 VGGT 的 DPT head 中集成跨视角一致性机制：
    - Cube-to-Equirectangular（C2E）：将 6 个视角特征图投影到统一等距柱状潜空间
    - 卷积层融合后 Equirectangular-to-Cube（E2C）变换回各视角
    - 残差连接保留视角特有细节：$\mathbf{F}'_i = \mathbf{F}_i + \text{E2C}(\mathbf{F}_e)$
3. **高斯参数预测**：对每个像素预测高斯中心（深度反投影+偏移）、不透明度、协方差、颜色

训练使用 MSE + LPIPS 渲染损失和 SILog 深度损失，在 Structured3D、Deep360、Matterport3D、Stanford2D3D 四个数据集上训练。**在 H20 GPU 上仅需 0.5 秒完成重建**。

**阶段三：支架引导新视角合成**

- 从 3D 支架渲染目标视角处的粗糙图像 $\mathbf{I}^{\text{render}}$（含伪影和遮挡黑洞，但保留大量结构信息）
- **Dual-LoRA 训练策略**：基于 SEVA 架构，使用两个独立 LoRA 分别处理高质量锚点视角和粗糙渲染视角，通过 3D 注意力融合特征，远优于简单拼接
- **记忆条件机制**：推理时从记忆库中选择与当前目标最近相机姿态的已生成帧作为额外条件，确保时空一致性

训练数据在 DL3DV 和 RealEstate10K 上用 MVSplat 做稀疏重建生成，故意模拟稀疏输入的伪影。

## 实验结果

### 可探索 3D 场景生成（Table 1）

在改编的 WorldScore 基准上评估（40 个场景，涵盖室内/室外、真实/风格化）：


### 主实验

| 方法 | NIQE↓ | Q-Align↑ | CLIP-I↑ | TransErr↓ | RotErr↓ | CamMC↓ |
|------|-------|----------|---------|-----------|---------|--------|
| DreamScene360 | 8.40 | 1.91 | 74.24 | - | - | - |
| WonderJourney | 4.97 | 3.02 | 77.92 | - | - | - |
| SEVA | 4.53 | 3.20 | 87.82 | 0.460 | 0.165 | 0.558 |
| VMem | 6.86 | 2.95 | 75.80 | 0.573 | 0.569 | 0.998 |
| **One2Scene** | **4.43** | **4.13** | **89.95** | **0.326** | **0.107** | **0.389** |

One2Scene 在视觉质量（NIQE/Q-Align）、语义一致性（CLIP-I）和几何一致性（CamMC 比 SEVA 降 30%，比 VMem 降 61%）上全面领先。

### 全景深度估计（Table 3，Matterport3D / Stanford2D3D）


### 消融实验

| 方法 | MP3D AbsRel↓ | MP3D δ₁↑ | S2D3D AbsRel↓ | S2D3D δ₁↑ |
|------|-------------|----------|--------------|----------|
| HRDFuse | 0.0967 | 91.62 | 0.0935 | 91.40 |
| Depth Anywhere | 0.0850 | 91.70 | 0.1180 | 91.00 |
| Ours (Zero-shot) | 0.1070 | 88.97 | **0.0675** | **95.20** |
| Ours (Finetune) | **0.0391** | **98.09** | 0.0444 | 96.95 |

零样本即在 Stanford2D3D 上超越所有对比方法；微调后 AbsRel 提升超 50%。

### 重建效率

6 个稀疏视角输入，H20 GPU 上重建用时 0.5 秒，比 AnySplat（2.8 秒）快 5.6 倍。替换支架网络为 AnySplat 后场景生成质量显著下降（Q-Align 从 4.13 降至 3.61）。

## 亮点与洞察

- **问题分解巧妙**：将单图→可探索场景拆解为三个可处理子任务，每个阶段各有明确职责
- **全景深度→多视图立体匹配的创新转化**：借助大规模多视图数据学到的几何先验，绕开全景深度数据集稀缺的瓶颈
- **高效前馈重建**：0.5 秒构建完整 3D 支架，兼具效率与精度
- **Dual-LoRA 有效融合异质条件**：分别处理高质量锚点和粗糙渲染视角，比简单拼接效果显著更好
- **全场景类型泛化**：室内/室外/真实/风格化均表现出色

## 局限与展望

- 生成视角可能存在细微不一致性，大视角下仍有局部伪影
- 全景生成质量依赖 Hunyuan-Pano-DiT，若全景本身有明显瑕疵会传播到后续阶段
- 3D 支架渲染在大遮挡区域产生黑洞，虽可由合成网络修补但信息有限
- 推理管线三阶段串联，端到端优化可能进一步提升性能
- 训练数据覆盖的场景类型仍有限，作者计划构建更大规模数据集

## 相关工作

- **稀疏视角重建**：MVSplat、VGGT、NoPosplat 等前馈高斯溅射模型，但在极稀疏视角下外推能力有限
- **视频扩散3D生成**：ReconX、ViewCrafter、VMem 利用 DUSt3R/CUT3R 等几何先验，但长序列误差累积
- **全景方法**：DreamScene360、Pano2Room 从全景构建 3D，探索范围有限或室内先验强
- **姿态条件视角合成**：SEVA、CAT3D 利用相机姿态引导生成，但缺乏持久几何表示
- **迭代导航**：WonderJourney、Höllein et al. 逐步探索+修补，全局语义漂移严重

## 评分

- ⭐⭐⭐⭐ 新颖性：三阶段分解+全景→多视图立体匹配的重新表述+Dual-LoRA 均有新意
- ⭐⭐⭐⭐⭐ 实验充分度：三个维度评估+多基准对比+消融+深度估计+效率分析，非常全面
- ⭐⭐⭐⭐ 实用性：0.5秒重建、支持室内外各类场景，有应用前景
- ⭐⭐⭐⭐ 写作清晰度：结构清晰、图示丰富、问题分解逻辑性强

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation](scenetransporter_optimal_transport-guided_compositional_latent_diffusion_for_sin.md)
- [\[ICLR 2026\] RadioGS: Radiometrically Consistent Gaussian Surfels for Inverse Rendering](radiogs_radiometric_gaussian_surfels.md)
- [\[ICLR 2026\] Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction for 3D-Aware Distillation](splat_and_distill_augmenting_teachers_with_feed-forward_3d_reconstruction_for_3d.md)
- [\[ICLR 2026\] EgoNight: Towards Egocentric Vision Understanding at Night with a Challenging Benchmark](egonight_towards_egocentric_vision_understanding_at_night_with_a_challenging_ben.md)
- [\[ICLR 2026\] LiTo: Surface Light Field Tokenization](lito_surface_light_field_tokenization.md)

</div>

<!-- RELATED:END -->
