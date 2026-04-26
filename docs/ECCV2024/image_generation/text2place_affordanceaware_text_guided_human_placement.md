---
title: >-
  [论文解读] Text2Place: Affordance-Aware Text Guided Human Placement
description: >-
  [ECCV 2024][图像生成][human placement] 提出 Text2Place，通过 SDS 损失优化 Gaussian blob 参数化的语义掩码学习场景中的人体 affordance，再结合主体条件修复实现逼真的文本引导人物放置，无需大规模训练。
tags:
  - ECCV 2024
  - 图像生成
  - human placement
  - affordance
  - score distillation sampling
  - text-to-image
  - 图像修复
---

# Text2Place: Affordance-Aware Text Guided Human Placement

**会议**: ECCV 2024  
**arXiv**: [2407.15446](https://arxiv.org/abs/2407.15446)  
**代码**: 有（项目页面）  
**领域**: LLM/NLP  
**关键词**: human placement, affordance, score distillation sampling, text-to-image, inpainting

## 一句话总结

提出 Text2Place，通过 SDS 损失优化 Gaussian blob 参数化的语义掩码学习场景中的人体 affordance，再结合主体条件修复实现逼真的文本引导人物放置，无需大规模训练。

## 研究背景与动机

### 领域现状

**领域现状**：给定背景场景，人类能轻松推理出人物可放置的位置和姿态——这就是 affordance

### 现有痛点

**现有痛点**：现有方法的局限：

### 核心矛盾

**核心矛盾**：Kulal et al. 需要在给定 bounding box 中放置人物，无法推理全局 affordance

### 解决思路

**解决思路**：Ramrakhya et al. 需要大规模成对数据集训练

### 补充说明

**补充说明**：SmartMask 需要大规模训练扩散模型预测掩码

### 补充说明

**补充说明**：核心挑战：
  1. 缺乏标注 affordance 的数据集（现有数据集只描述已存在的物体）
  2. 如何在不进行大规模训练的情况下学习场景中的人物 affordance
  3. 放置后需要保持背景完整性和主体身份

## 方法详解

### 整体框架

两阶段方法：
1. **语义掩码优化**：利用 T2I 模型的 SDS 损失优化 blob 参数化的语义掩码
2. **主体条件修复**：使用 Textual Inversion 学习主体 token，结合 T2I 修复管线实现身份保持的人物放置

### 关键设计

**1. Gaussian Blob 掩码参数化**

- 直接在像素空间优化语义掩码会导致崩溃（覆盖整张图像）
- 创新参数化：K 个相连的高斯椭球 blob
- 每个 blob 的参数：中心位置 x、缩放 s、长宽比 a、旋转角 θ
- blob 间通过固定距离 r 和相对角度 α 连接
- x_i = x_{i-1} + [r·cos(α_i), r·sin(α_i)]
- 可渲染为可微分的 Mahalanobis 距离掩码图

**2. SDS 驱动的语义掩码优化**

- 设立可学习的前景人物图像 I_p（初始化为背景副本）
- 每步迭代：I_c = I_p ⊙ M + I_b ⊙ (1-M)
- 对 I_c 加噪后通过 T2I 模型计算 SDS 损失（动作提示如 "a person sitting on sofa"）
- 梯度回传更新掩码参数和 I_p
- 训练中仅优化：第一个 blob 中心 x_1、所有旋转角 θ_i、相对角度 α_i
- 固定 s、a、r 得到更好的收敛

**3. 主体条件修复**

- 使用 Textual Inversion 从 3-5 张主体图像学习 token 嵌入 V*
- 修复提示："A V* person sitting on a sofa"
- 关键发现：T2I 修复管线需要粗糙语义掩码（而非精确掩码）
    - 精确掩码过于严格，T2I 修复管线难以成功
    - Blob 参数化天然产生粗糙掩码，恰好适配修复需求

### 损失函数 / 训练策略

- SDS 损失：guidance scale = 200
- 优化 1000 次迭代
- c = 0.02 控制每个 blob 的锐度
- 默认 blob 数量 K=5，scale s=0.6
- Textual Inversion：3-5 张主体图像

## 实验关键数据

### 主实验

| 方法 | LPIPS ↓ | CLIP-sim ↑ | % Person ↑ |
|------|---------|-----------|------------|
| GracoNet | 0.1090 | 0.2601 | 53.48 |
| TopNet | 0.1162 | 0.2617 | 67.3 |
| LLaVA | 0.1296 | 0.2501 | 20.91 |
| GPT-4V | 0.1059 | 0.2615 | 64.18 |
| Ours (center only) | **0.0845** | 0.2613 | 55.52 |
| **Ours** | 0.0934 | **0.2726** | **88.55** |

### 消融实验

**Blob scale 消融**：

| Scale | LPIPS ↓ | CLIP-sim ↑ | % Person ↑ |
|-------|---------|-----------|------------|
| 0.3 | 0.0537 | 0.2594 | 41.1 |
| 0.5 | 0.0858 | 0.2712 | 81.5 |
| **0.6** | **0.0904** | **0.2736** | **90.6** |
| 0.7 | 0.1074 | 0.2729 | 96.0 |

**Blob 数量消融**：K=5 是最优选择

### 关键发现

- 88.55% 的图像成功生成了人物（% Person），远超所有基线
- GPT-4V 等 VLM 虽有多模态推理能力，但预测的 bounding box 位置和大小通常不准确
- 掩码形状比位置更重要：Ours (center) 位置正确但形状不对，导致姿态不自然
- 粗糙掩码反而比精确掩码更适合 T2I 修复——给模型留出调整空间
- 方法泛化到人物以外的物体（椅子、花盆等）同样有效

## 亮点与洞察

1. **无需大规模训练**：仅通过 SDS 测试时优化即可学习 affordance，是高效的零样本方法
2. **Blob 参数化精妙**：约束了掩码形状空间，防止崩溃；粗糙性恰好适配修复需求
3. **丰富的下游应用**：人物幻想、场景幻想、多人放置、文本编辑、儿童放置
4. T2I 修复管线需要粗糙掩码的发现非常实用
5. 问题定义（Semantic Human Placement）本身是创新性贡献

## 局限与展望 / 可改进方向

- SDS 优化需要 1000 次迭代，每张图像约需几分钟
- 依赖 Textual Inversion 的身份保持质量，3-5 张图可能不足
- Blob 参数化限制了复杂姿态（如躺下、弯腰）的掩码表示
- 固定 s、a、r 的策略限制了不同体型的自适应
- 评估数据集仅 30 张背景图 + 15 个名人主体，规模较小

## 相关工作与启发

- **DreamFusion/SDS**: SDS 损失从 3D 生成迁移到 2D 掩码优化
- **Textual Inversion**: 主体个性化的基础
- **Kulal et al.**: 局部人物 affordance 学习
- **Gaussian Splatting**: Blob 参数化的灵感来源
- 启发：T2I 模型中隐式编码的物体-场景组合知识可以通过 SDS 提取，而不仅限于 3D 生成

## 评分

| 维度 | 分数 (1-10) |
|------|-----------|
| 新颖性 | 9 |
| 技术深度 | 7 |
| 实验充分性 | 7 |
| 实用价值 | 8 |
| 写作质量 | 8 |
| 总体评分 | 7.8 |

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] LivePhoto: Real Image Animation with Text-guided Motion Control](livephoto_real_image_animation_with_text-guided_motion_control.md)
- [\[ECCV 2024\] Local Action-Guided Motion Diffusion Model for Text-to-Motion Generation](local_action-guided_motion_diffusion_model_for_text-to-motion_generation.md)
- [\[ECCV 2024\] Realistic Human Motion Generation with Cross-Diffusion Models](realistic_human_motion_generation_with_cross-diffusion_models.md)
- [\[ECCV 2024\] MagicEraser: Erasing Any Objects via Semantics-Aware Control](magiceraser_erasing_any_objects_via_semantics-aware_control.md)
- [\[ECCV 2024\] Learning Semantic Latent Directions for Accurate and Controllable Human Motion Prediction](learning_semantic_latent_directions_for_accurate_and_controllable_human_motion_p.md)

<!-- RELATED:END -->
