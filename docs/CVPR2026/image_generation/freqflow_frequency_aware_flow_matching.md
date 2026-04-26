---
title: >-
  [论文解读] Frequency-Aware Flow Matching for High-Quality Image Generation
description: >-
  [CVPR 2026][图像生成][流匹配] FreqFlow 通过在流匹配框架中显式引入频域感知条件，采用双分支架构分别处理低频全局结构和高频细节信息，在 ImageNet-256 上以 1.38 FID 达到 SOTA。
tags:
  - CVPR 2026
  - 图像生成
  - 流匹配
  - 频域感知
  - 双分支架构
  - 自适应加权
---

# Frequency-Aware Flow Matching for High-Quality Image Generation

**会议**: CVPR 2026  
**arXiv**: [2604.15521](https://arxiv.org/abs/2604.15521)  
**代码**: [https://github.com/OliverRensu/FreqFlow](https://github.com/OliverRensu/FreqFlow)  
**领域**: 图像生成  
**关键词**: 流匹配, 频域感知, 图像生成, 双分支架构, 自适应加权

## 一句话总结

FreqFlow 通过在流匹配框架中显式引入频域感知条件，采用双分支架构分别处理低频全局结构和高频细节信息，在 ImageNet-256 上以 1.38 FID 达到 SOTA。

## 研究背景与动机

**领域现状**：流匹配（Flow Matching）已成为图像生成的主流框架之一，通过学习从高斯噪声到数据分布的连续变换路径实现高质量图像合成。SiT 和 DiT 等模型在大规模生成任务上取得了不错的效果。

**现有痛点**：现有的流匹配方法在空间域中均匀注入噪声，但噪声在潜空间中对不同频率分量的影响是不均匀的。模型在逆过程中倾向于先重建低频分量（全局结构），而高频分量（纹理和边缘等细节）在后期才逐渐出现。然而模型本身并没有显式机制来区分和处理不同频率分量，导致生成结果在细节上模糊不清。

**核心矛盾**：流匹配模型在空间域工作，但损坏和恢复过程本质上是以频率不均匀的方式影响图像的——这种频域特征既没有被显式建模，也没有被有效利用。频率误差分析显示 SiT 在高频误差（0.69）上远大于低频误差（0.08）。

**本文目标**：在流匹配框架中显式引入频域信息，让模型在不同生成阶段正确地关注对应的频率成分。

**切入角度**：作者观察到流匹配的逆过程天然地遵循"先低频后高频"的重建顺序，这与人类感知的从粗到细的认知过程一致。如果能显式地在模型中嵌入频域条件，就能强化这种自然的频率生成顺序。

**核心 idea**：用一个专门的频率分支分别处理低频和高频分量，通过时间依赖的自适应加权将频域信息注入空间分支，实现频域感知的流匹配。

## 方法详解

### 整体框架

FreqFlow 采用双分支架构：（1）频率分支，通过离散傅里叶变换将输入分解为低频和高频分量，分别处理全局结构和局部细节；（2）空间分支，在潜空间中合成图像，同时接受频率分支的输出作为条件引导。给定噪声图像 $X_t$，频率分支生成低频和高频的速度场预测，空间分支在频率引导下预测完整速度场。

### 关键设计

1. **频率分支（Frequency Branch）**:

    - 功能：将输入的噪声图像分解到频域，分别处理低频和高频分量
    - 核心思路：通过 DFT 将 $X_t$ 变换到频域，使用低通和高通滤波器分离频率成分。频率分支由独立的 Transformer blocks 组成，对低频和高频分量分别建模，并输出对应的频率速度场。训练时用低频和高频的速度场作为监督信号
    - 设计动机：不同频率成分在生成过程的不同阶段重要性不同，专门的频率处理能让模型更精准地控制各频段的重建质量

2. **时间依赖自适应加权（Time-Dependent Adaptive Weighting）**:

    - 功能：动态平衡频率分支和空间分支在不同生成阶段的贡献
    - 核心思路：引入可学习的时间依赖权重 $w(t)$，在早期阶段让低频条件主导（建立全局结构），在后期让高频条件增强（细化纹理细节）。权重随时间步自适应调整，确保频域信息在正确的阶段被正确地强调
    - 设计动机：流匹配的重建过程天然遵循先低频后高频的顺序，自适应加权使这一过程更加精确和高效

3. **双域监督（Dual-Domain Supervision）**:

    - 功能：在频域和空间域同时训练模型
    - 核心思路：空间分支使用标准流匹配损失（速度场预测误差），频率分支额外使用低频和高频速度场的预测损失。两个分支的损失联合优化，确保模型同时学到空间域的连贯性和频域的准确性
    - 设计动机：单一空间域损失无法有效约束频率分量的准确重建，双域监督让模型在两个互补的表示空间中都能得到有效训练

### 损失函数 / 训练策略

总损失为空间域流匹配损失和频域（低频+高频）速度场预测损失的加权组合。训练遵循标准流匹配范式，在 $t \in [0,1]$ 上均匀采样时间步。

## 实验关键数据

### 主实验

| 模型 | FID ↓ | 参数量 |
|------|-------|--------|
| DiT-XL | 2.17 | 675M |
| SiT-XL | 1.96 | 675M |
| DiMR-G | 1.53 | 1.1B |
| MAR-H | 1.45 | 943M |
| **FreqFlow-L** | **1.44** | 625M |
| **FreqFlow-H** | **1.38** | ~1B |

### 消融实验

| 配置 | FID |
|------|-----|
| 仅空间分支（baseline） | 1.96 |
| + 频率分支（无自适应加权） | 1.62 |
| + 时间依赖自适应加权 | 1.44 |

### 关键发现

- FreqFlow-L 用更少的参数量（625M vs 675M）超越了 DiT-XL 和 SiT-XL，FID 改善 0.73 和 0.52
- 频率误差分析证实 FreqFlow 在低频（0.06 vs 0.08）和高频（0.48 vs 0.69）上都显著优于 SiT
- FreqFlow 能更早建立全局结构（在 step 200 达到最低对数振幅，SiT 需要 step 280）

## 亮点与洞察

- **频域视角重新审视流匹配**：将流匹配从纯空间操作扩展到频域感知，这一思路非常自然但之前未被充分探索。频率分解为理解和改进生成模型提供了新的分析工具
- **效率优势**：FreqFlow-L 在更少参数下超越更大模型，说明频域信息是一种高效的归纳偏置，比单纯增加模型规模更有效
- **迁移潜力**：这种频域感知的设计思路可以迁移到视频生成、3D 生成等其他需要多尺度细节控制的生成任务

## 局限与展望

- 双分支架构带来额外的计算开销，频率分支的轻量化是一个值得探索的方向
- 目前仅在类条件生成（ImageNet-256）上验证，缺乏文本到图像等更复杂任务的评估
- 频率分解依赖 DFT，对于某些非周期性纹理可能不是最优的分解方式

## 相关工作与启发

- **vs SiT**: SiT 在纯空间域做流匹配，FreqFlow 增加了频域分支和自适应加权，在高频细节上明显更好
- **vs FreeU**: FreeU 通过重加权 U-Net 的 skip connection 来平衡频率，FreqFlow 则是从头设计了频域处理分支，更加系统化
- **vs DiMR**: DiMR 使用多分辨率策略，FreqFlow 使用频域分解，两者都试图解决多尺度问题但角度不同

## 评分

- 新颖性: ⭐⭐⭐⭐ 频域感知引入流匹配的思路新颖但方法较直接
- 实验充分度: ⭐⭐⭐⭐ ImageNet-256 上全面对比，频率分析深入
- 写作质量: ⭐⭐⭐⭐ 频域动机阐述清晰，图示直观
- 价值: ⭐⭐⭐⭐ 为流匹配模型提供了新的改进方向

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] RenderFlow: Single-Step Neural Rendering via Flow Matching](renderflow_single-step_neural_rendering_via_flow_matching.md)
- [\[CVPR 2026\] MPDiT: Multi-Patch Global-to-Local Transformer Architecture for Efficient Flow Matching](mpdit_multi-patch_global-to-local_transformer_architecture_for_efficient_flow_ma.md)
- [\[CVPR 2026\] DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation](deco_frequency-decoupled_pixel_diffusion_for_end-to-end_image_generation.md)
- [\[CVPR 2026\] VeCoR — Velocity Contrastive Regularization for Flow Matching](vecor_--_velocity_contrastive_regularization_for_flow_matching.md)
- [\[CVPR 2026\] EgoFlow: Gradient-Guided Flow Matching for Egocentric 6DoF Object Motion Generation](egoflow_gradient-guided_flow_matching_for_egocentric_6dof_object_motion_generati.md)

<!-- RELATED:END -->
