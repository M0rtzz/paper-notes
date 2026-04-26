---
title: >-
  [论文解读] AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation
description: >-
  [ECCV 2024][图像生成][可控图像生成] AnyControl提出Multi-Control Encoder，通过交替执行多控制融合块和多控制对齐块，从任意组合的多种空间控制信号中提取统一的多模态embedding，实现高质量、语义对齐的多条件可控图像生成。
tags:
  - ECCV 2024
  - 图像生成
  - 可控图像生成
  - 多条件融合
  - Text-to-Image
  - ControlNet
  - 注意力机制
---

# AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation

**会议**: ECCV 2024  
**arXiv**: [2406.18958](https://arxiv.org/abs/2406.18958)  
**代码**: https://any-control.github.io (有)  
**领域**: 多模态VLM  
**关键词**: 可控图像生成, 多条件融合, Text-to-Image, ControlNet, 注意力机制

## 一句话总结

AnyControl提出Multi-Control Encoder，通过交替执行多控制融合块和多控制对齐块，从任意组合的多种空间控制信号中提取统一的多模态embedding，实现高质量、语义对齐的多条件可控图像生成。

## 研究背景与动机

1. **领域现状**：T2I扩散模型（Stable Diffusion）已能生成高质量图像，ControlNet等方法通过引入额外的空间条件（深度图、边缘图、分割图、姿态等）实现精细控制。多条件控制是实际应用中的刚需。

2. **现有痛点**：(1) 输入灵活性不足：现有方法如Uni-ControlNet用固定长度输入通道，无法处理自由组合的条件；(2) 空间兼容性差：多条件通常通过手工加权求和组合，遮挡区域处理不当导致融合伪影；(3) 文本兼容性弱：空间条件常主导生成过程，文本语义被忽略。

3. **核心矛盾**：多个空间条件来自不同模态、数量可变，且彼此间存在复杂的空间关系（如遮挡），同时还需与文本语义保持一致。简单的加权求和或固定通道设计无法全面解决这些问题。

4. **本文要解决什么？** 同时解决输入灵活性（任意数量和类型的条件组合）、空间兼容性（条件间复杂关系处理）和文本兼容性（保持语义对齐）三大挑战。

5. **切入角度**：受Q-Former的启发，用可学习的query token作为桥梁，交替在空间条件和文本条件之间传递信息，实现多模态信息的统一理解。

6. **核心idea一句话**：用交替的交叉注意力（融合空间条件）和自注意力（对齐文本语义）块，通过query token提取统一的多控制表示。

## 方法详解

### 整体框架

AnyControl锁定预训练SD模型，设计Multi-Control Encoder提取多控制embedding注入生成过程。先从CLIP视觉编码器提取各空间条件的visual token，从CLIP文本编码器提取textual token，加上一组可学习的query token，通过交替的Multi-Control Fusion Block和Multi-Control Alignment Block处理，最终query token携带统一的多模态信息指导生成。

### 关键设计

1. **Multi-Control Fusion Block**:
    - 做什么：从多个空间条件中聚合兼容信息到query token
    - 核心思路：使用交叉注意力，query token作为Q，所有条件的visual token拼接后作为K和V。$\mathcal{Q}_j = CrossAttention(\mathcal{Q}_j, [\mathcal{V}_{1,j}+P, \mathcal{V}_{2,j}+P, ..., \mathcal{V}_{n,j}+P])$，其中P是共享的可学习位置编码
    - 设计动机：通过注意力机制自动学习条件间的组合权重，替代手工加权求和；共享位置编码帮助对齐不同条件的空间位置

2. **Multi-Control Alignment Block**:
    - 做什么：保证空间条件信息与文本语义的兼容性
    - 核心思路：将query token和textual token拼接后进行自注意力。$[\mathcal{Q}_{j+1}, \mathcal{T}_{j+1}] = SelfAttention([\mathcal{Q}_j, \mathcal{T}_j])$。额外在用户文本末尾添加textual task prompt解决模态差异
    - 设计动机：文本prompt作为全局控制信号可以指示空间条件间的关系优先级（如遮挡时谁在前）。自注意力使query token和textual token双向交换信息

3. **交替多层级融合**:
    - 做什么：多轮交替融合和对齐，每轮使用CLIP视觉编码器不同层级的visual token
    - 核心思路：浅层visual token提供底层纹理控制（如边缘图），深层提供高层语义控制（如分割图），多层级token匹配不同条件的控制粒度
    - 设计动机：不同控制信号的控制层级不同，多层级特征确保每种条件都能在合适的抽象层次被利用

### 损失函数 / 训练策略

标准扩散去噪损失。训练数据：MultiGen数据集（2.8M图像），加上0.44M自合成的未对齐数据（将图像分为前景/背景分别提取条件）。随机选择2个条件训练，以0.05概率drop所有条件启用classifier-free guidance。

## 实验关键数据

### 主实验（COCO-UM未对齐多控制benchmark）

| 方法 | FID↓ | CLIP↑ | Depth RMSE↓ | Seg mPA↑ | Pose mAP↑ |
|------|------|-------|-------------|----------|-----------|
| Multi-ControlNet | 55.95 | 24.80 | 17.81 | 42.78 | 15.69 |
| Uni-ControlNet | 55.28 | 24.48 | 20.57 | 41.10 | 18.40 |
| Cocktail | 47.39 | 25.33 | - | 31.74 | 12.16 |
| **AnyControl** | **44.28** | **26.41** | 18.00 | **43.34** | **18.81** |

### 消融实验

| 配置 | FID↓ | CLIP↑ | 说明 |
|------|------|-------|------|
| w/o Alignment Block | 48.5 | 25.1 | 空间与文本不兼容 |
| w/o 未对齐数据 | 47.2 | 25.8 | 遮挡处理能力下降 |
| w/o 多层级visual token | 46.8 | 25.9 | 精细控制能力减弱 |
| Full AnyControl | **44.28** | **26.41** | 完整模型 |

### 关键发现

- **注意力机制比MoE设计更适合多条件融合**：AnyControl在所有指标上优于基于MoE加权求和的Multi-ControlNet
- **未对齐训练数据至关重要**：只用对齐数据训练的模型无法处理实际应用中条件不对齐（来自不同图像）的情况
- **AnyControl展现出对空间关系的推理能力**：不仅能处理条件间遮挡，还能推断生成物体与环境的合理交互关系（如高度不同时自动生成合理的放置平面）

## 亮点与洞察

- **Q-Former思想的创新迁移**：将视觉-语言预训练中的桥梁设计迁移到多控制图像生成中，用query token统一异质控制信号
- **COCO-UM benchmark**：构建了首个未对齐多条件评估基准，填补了现有评估只考虑完美对齐条件的空白
- **兼容风格和颜色控制**：作为即插即用模块可与decoupled cross-attention结合，扩展到风格/颜色控制

## 局限性 / 可改进方向

- 目前只支持4种空间条件类型，可扩展到更多模态（如法线图、光流等）
- Multi-Control Encoder的计算开销随条件数线性增长
- 未对齐数据的合成策略较简单（前景/背景分离），更复杂的多物体场景值得探索
- 尚未与最新的SDXL架构适配

## 相关工作与启发

- **vs Multi-ControlNet**: 后者用独立编码器+加权求和（MoE），无法学习条件间关系，容易产生混合伪影
- **vs Uni-ControlNet**: 固定通道设计限制了输入灵活性，且仍用简单融合策略
- **vs Cocktail**: 将同类条件合为一张图的"组合设计"会产生贴纸伪影
- AnyControl的多模态融合思路可迁移到视频生成、3D生成等需要多条件控制的场景

## 评分

- 新颖性: ⭐⭐⭐⭐ Q-Former风格的多控制融合架构设计新颖
- 实验充分度: ⭐⭐⭐⭐ 提出新benchmark，定性定量分析充分
- 写作质量: ⭐⭐⭐⭐ 问题分析透彻，架构图清晰
- 价值: ⭐⭐⭐⭐ 多控制图像生成的实用方案

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] LivePhoto: Real Image Animation with Text-guided Motion Control](livephoto_real_image_animation_with_text-guided_motion_control.md)
- [\[ECCV 2024\] Latent Guard: a Safety Framework for Text-to-Image Generation](latent_guard_a_safety_framework_for_text-to-image_generation.md)
- [\[ECCV 2024\] Powerful and Flexible: Personalized Text-to-Image Generation via Reinforcement Learning](powerful_and_flexible_personalized_text-to-image_generation_via_reinforcement_le.md)
- [\[ECCV 2024\] MagicEraser: Erasing Any Objects via Semantics-Aware Control](magiceraser_erasing_any_objects_via_semantics-aware_control.md)
- [\[ECCV 2024\] LCM-Lookahead for Encoder-based Text-to-Image Personalization](lcm-lookahead_for_encoder-based_text-to-image_personalization.md)

<!-- RELATED:END -->
