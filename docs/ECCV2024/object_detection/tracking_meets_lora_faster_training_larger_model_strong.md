---
title: >-
  [论文解读] Tracking Meets LoRA: Faster Training, Larger Model, Stronger Performance
description: >-
  [ECCV 2024][目标检测][visual tracking] 首次将 LoRA 引入视觉目标跟踪领域，通过解耦位置编码和设计 MLP-only 头网络，使大规模 ViT 模型（最大 ViT-g）在实验室级资源下实现高效训练和 SOTA 跟踪性能。
tags:
  - ECCV 2024
  - 目标检测
  - visual tracking
  - LoRA
  - parameter-efficient fine-tuning
  - ViT
  - one-stream tracker
---

# Tracking Meets LoRA: Faster Training, Larger Model, Stronger Performance

**会议**: ECCV 2024  
**arXiv**: [2403.05231](https://arxiv.org/abs/2403.05231)  
**代码**: https://github.com/LitingLin/LoRAT (有)  
**领域**: LLM/NLP  
**关键词**: visual tracking, LoRA, parameter-efficient fine-tuning, ViT, one-stream tracker

## 一句话总结

首次将 LoRA 引入视觉目标跟踪领域，通过解耦位置编码和设计 MLP-only 头网络，使大规模 ViT 模型（最大 ViT-g）在实验室级资源下实现高效训练和 SOTA 跟踪性能。

## 研究背景与动机

- 基于 Transformer 的跟踪器性能不断提升，但训练资源需求急剧增长——SeqTrack-L384 需要大量高端 GPU 和长时间训练
- 大语言模型中的参数高效微调（PEFT）方法已相当成熟，但在视觉跟踪中未被探索
- 直接将 LoRA 应用于跟踪器会遇到两个关键问题：
  1. 跟踪器为 template 和 search image 使用不同的位置编码，破坏了预训练模型结构
  2. 卷积头网络的归纳偏置阻碍了 LoRA 微调的收敛
- 目标：在可承受的计算资源下训练更大规模的跟踪器，使先进模型更易接触

## 方法详解

### 整体框架

LoRAT 基于 one-stream 跟踪框架（OSTrack），将 LoRA 应用于预训练 ViT 的所有线性层，仅微调少量参数。训练时冻结大部分预训练权重，只更新 LoRA 模块、token type embedding 和头网络。

### 关键设计

**1. 解耦输入嵌入（Decoupled Input Embedding）**

- 借鉴 BERT 的 token type embedding 思想，将位置编码解耦为：
    - **共享空间位置编码**：继承自预训练 ViT，描述多分辨率图像的绝对坐标
    - **独立 token type embedding**：从零学习，标识每个 token 来源（template 前景/背景、search region）
- 多分辨率绝对位置嵌入适配策略：
    - 插值方法（interpolation）：将搜索区域位置编码插值到模板分辨率
    - 切片方法（slicing）：从搜索区域编码中截取子矩阵作为模板编码
    - 实验证明切片方法更优，被采用为默认策略
- 前景对象指示嵌入：进一步在 template 中区分目标前景和背景 token

**2. MLP-only 头网络**

- 替换原有卷积头网络，消除卷积的归纳偏置对 LoRA 微调的阻碍
- 分为分类分支和边界框回归分支，各由 3 层 MLP 组成
- 采用无锚框（anchor-free）设计，基于中心点预测，加速训练收敛

### 损失函数 / 训练策略

- LoRA rank 设为 64，应用于 ViT backbone 的所有线性层（含 attention 的 4 个投影矩阵和 MLP 的 2 个投影矩阵）
- 训练 170 个 epoch，每 epoch 131,072 图像对，batch size 128
- LoRA 层使用截断正态分布初始化（std=0.02）
- 推理时添加 Hanning 窗抑制分类响应图中的大位移

## 实验关键数据

### 主实验

| 模型 | LaSOT SUC | LaSOText SUC | TrackingNet SUC | GOT-10k AO | TNL2K SUC |
|------|-----------|-------------|-----------------|------------|-----------|
| LoRAT-B-224 | 0.717 | 0.530 | 0.842 | 0.749 | 0.588 |
| LoRAT-L-224 | 0.742 | 0.555 | 0.852 | 0.762 | 0.596 |
| LoRAT-g-378 | **0.762** | **0.578** | **0.862** | - | **0.604** |

- LoRAT-g-378 在 LaSOT 上创下 0.762 SUC 新纪录
- LoRAT-B-224 在 209 FPS 下仍达 0.717 SUC，比 OSTrack-256 高 3.4%

### 消融实验

| 组件 | LaSOT SUC |
|------|-----------|
| Baseline (OSTrack + LoRA) | 0.682 |
| + Token type embedding | 0.701 |
| + Slicing positional embedding | 0.708 |
| + MLP-only head | 0.717 |
| + Foreground indication | 0.717 |

- 切片位置编码适配优于插值方法（0.708 vs 0.698）
- MLP-only 头对 LoRA 微调至关重要

### 关键发现

- LoRAT-L-224 训练时间从 35.0 GPU 小时降至 10.8 GPU 小时（降低 69%）
- 训练内存从 >40GB 降至 25.8GB（batch size 16）
- 推理速度从 52 FPS 提升至 119 FPS（L-224 变体）
- LoRAT-B-224 可在单张 RTX 4090 上 11 小时内完成训练

## 亮点与洞察

1. **首创性**：首次系统研究 PEFT 在视觉跟踪中的应用，为大模型在跟踪领域的普及铺平道路
2. **简洁有效的设计**：token type embedding 和 MLP-only head 两个设计虽然简单，但精准解决了 LoRA 在跟踪领域的适配问题
3. **实用价值突出**：使 ViT-g 级别模型在消费级 GPU 上可训练，大幅降低研究门槛
4. **性能-效率双赢**：更少训练参数的同时实现了更高性能，挑战了"全参数微调必不可少"的传统观念
5. 切片 vs 插值位置编码的发现：将位置编码视为离散 patch 索引优于连续空间位置的解释

## 局限性 / 可改进方向

- 仅探索了 LoRA 一种 PEFT 方法，AdaLoRA、QLoRA 等变体值得研究
- 未探索多模板或在线更新的跟踪场景
- 头网络设计相对简单，可以融入更多跟踪先验
- 固定 rank=64 对所有变体，不同规模模型的最优 rank 可能不同

## 相关工作与启发

- **OSTrack**: 提供 one-stream 跟踪基线框架
- **BERT**: token type embedding 的思想来源
- **LoRA**: 参数高效微调的核心技术
- 启发：将 NLP 领域的 PEFT 技术转移到视觉任务时，需要针对领域特点进行适配设计，不能简单移植

## 评分

| 维度 | 分数 (1-10) |
|------|-----------|
| 新颖性 | 8 |
| 技术深度 | 7 |
| 实验充分性 | 9 |
| 实用价值 | 9 |
| 写作质量 | 8 |
| 总体评分 | 8.2 |

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Spherical Linear Interpolation and Text-Anchoring for Zero-shot Composed Image Retrieval](spherical_linear_interpolation_and_text-anchoring_for_zero-shot_composed_image_r.md)
- [\[ECCV 2024\] TAPTR: Tracking Any Point with Transformers as Detection](taptr_tracking_any_point_with_transformers_as_detection.md)
- [\[ECCV 2024\] WALKER: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs](walker_self-supervised_multiple_object_tracking_by_walking_on_temporal_appearanc.md)
- [\[ECCV 2024\] LaMI-DETR: Open-Vocabulary Detection with Language Model Instruction](lami-detr_open-vocabulary_detection_with_language_model_instruction.md)
- [\[ECCV 2024\] MutDet: Mutually Optimizing Pre-training for Remote Sensing Object Detection](mutdet_mutually_optimizing_pre-training_for_remote_sensing_object_detection.md)

<!-- RELATED:END -->
