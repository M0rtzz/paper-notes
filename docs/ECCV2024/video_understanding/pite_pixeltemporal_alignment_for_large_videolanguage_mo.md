---
title: >-
  [论文解读] PiTe: Pixel-Temporal Alignment for Large Video-Language Model
description: >-
  [ECCV 2024][视频理解][视频语言大模型] 提出 PiTe，一种通过物体轨迹引导的像素-时序对齐方法，利用自动构建的 PiTe-143K 数据集在空间和时间维度上实现视频与语言的精细对齐，显著提升视频理解能力。
tags:
  - ECCV 2024
  - 视频理解
  - 视频语言大模型
  - 像素级对齐
  - 轨迹引导
  - 时空对齐
  - 指令微调
---

# PiTe: Pixel-Temporal Alignment for Large Video-Language Model

**会议**: ECCV 2024  
**arXiv**: [2409.07239](https://arxiv.org/abs/2409.07239)  
**代码**: 无  
**领域**: LLM/NLP  
**关键词**: 视频语言大模型, 像素级对齐, 轨迹引导, 时空对齐, 指令微调

## 一句话总结

提出 PiTe，一种通过物体轨迹引导的像素-时序对齐方法，利用自动构建的 PiTe-143K 数据集在空间和时间维度上实现视频与语言的精细对齐，显著提升视频理解能力。

## 研究背景与动机

- 现有大视频语言模型（LVidLM）主要通过一般化的指令微调对齐视觉和语言特征
- 传统 QA 训练范式主要帮助 LLM 从空间角度理解视觉数据，难以有效捕捉时序动态和空间一致性关系
- 仅靠指令微调不足以实现全面的视频理解，需要跨空间和时间维度的多模态对齐
- 更细粒度的跨模态对齐指导能显著增强 LVidLM 理解视频的能力
- **关键问题**：缺乏现成的带物体运动轨迹的视频-语言数据集

## 方法详解

### 整体框架

三阶段训练流程：
1. **阶段一**：用 Localized Narratives 数据集训练视觉适配器（图像级，空间对齐）
2. **阶段二**：用 PiTe-143K 数据集进行像素-时序对齐（视频级，时空对齐）
3. **阶段三**：高质量对话指令微调（增强指令跟随能力）

### 关键设计

**PiTe-143K 数据集自动标注流水线**：

*阶段一 — 名词短语提取 + 指称表达分割*：
- 用 SuPar 句法解析器从视频字幕中提取名词短语（仅取最低层）
- 用 GLaMM（首个能生成分割掩码的 LVLM）在视频首帧定位对应物体
- GLaMM 同时充当无效指称表达过滤器

*阶段二 — 点追踪*：
- 用 DOT 追踪器对每个视频片段中第一帧的物体进行全帧追踪
- 根据阶段一的分割掩码过滤轨迹
- K-means++ 聚类将轨迹浓缩为 3 个关键点

数据集规模：143.64K 视频，343.93K 事件片段，1.02M 运动轨迹

**模型架构**：
- 视觉编码器：CLIP ViT-L/14
- 视觉适配器：线性投影层（每帧仅取 CLS token）
- LLM：Vicuna v1.5
- 定位投影器 φ(·)：MLP，输出 2D 坐标（阶段一）
- 轨迹投影器 ρ(·)：MLP，输出 P×N 维轨迹矩阵（阶段二，用 φ 初始化）

**轨迹引导对齐**：
- 为文本中提及的每个物体名词预测其在 N 帧 × P 个关键点的 2D 坐标序列
- 轨迹连接了视频（物体在哪里/是否存在）和语言（文本提及哪些物体）

### 损失函数 / 训练策略

- 阶段一：L₁ = CE(生成) + λ·|p̂-p|（定位回归），使用 LoRA 微调 LLM
- 阶段二：L₂ = CE(生成) + λ/(P·N)·Σ|p̂ᵢⱼₖ-pᵢⱼₖ|（轨迹回归），合并前一阶段 LoRA + 新 LoRA
- 阶段三：标准指令微调（CE 损失）

## 实验关键数据

### 主实验

零样本视频问答：

| 方法 | MSVD-QA | MSRVTT-QA | ActivityNet-QA |
|------|---------|-----------|----------------|
| Video-ChatGPT | 64.9 | 49.3 | 35.2 |
| Video-LLaMA | 51.6 | 29.6 | 12.4 |
| **PiTe** | **最优** | **最优** | **最优** |

时序定位和稠密字幕任务也大幅超越SOTA。

### 消融实验

| 配置 | 效果 |
|------|------|
| 无轨迹对齐 | 基线性能 |
| 仅阶段二（无阶段一） | 空间对齐缺失导致轨迹学习不充分 |
| 关键点数 P=1,3,5 | P=3 最优平衡 |
| 定位投影器初始化 ρ | 用 φ 初始化显著优于随机初始化 |

### 关键发现

1. 轨迹引导对齐使模型能基于证据生成输出，而非纯粹依赖语言先验
2. 从图像级空间对齐到视频级时空对齐的渐进训练策略至关重要
3. 3 个关键点足以捕捉物体的典型几何形状
4. 仅使用 CLS token（1 token/帧）的简约设计迫使 LLM 学习更多视觉理解能力

## 亮点与洞察

- **像素级时空对齐的创新范式**：不同于传统的全局特征对齐，通过物体轨迹实现跨模态的精细连接
- **自动标注流水线**：完全自动化地构建了 100 万级轨迹数据集，无需人工标注
- **逐阶段能力积累**：图像空间对齐 → 视频时空对齐 → 指令跟随，渐进式增强
- **数据集贡献**：PiTe-143K 填补了视频-语言数据集缺乏物体运动轨迹标注的空白

## 局限性 / 可改进方向

- 过小的物体可能无法被 GLaMM 准确分割，相关轨迹信息会被丢弃
- K-means++ 聚类到 3 个关键点可能丢失复杂运动模式
- 每帧仅用 CLS token 表示，可能损失空间细节
- 轨迹追踪基于首帧检测，新出现的物体无法追踪
- 写作质量有待提升（部分句子语法不通顺）
- 未来方向：结合 SAM 实现更精确分割、扩展到 3D 空间理解、支持多轮交互式视频理解

## 相关工作与启发

- PixelLLM 在图像域使用词级坐标对齐，PiTe 是其在视频域的时空扩展
- Localized Narratives 数据集提供人类注意力轨迹，PiTe 将这一思想扩展到自动标注的物体轨迹
- 轨迹作为视频-语言桥梁的思路可类推到机器人操作中的动作-语言对齐

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4 |
| 技术深度 | 3.5 |
| 实验充分性 | 4 |
| 写作质量 | 3 |
| 实用价值 | 3.5 |
| 总分 | 3.6 |

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] VideoMamba: Spatio-Temporal Selective State Space Model](videomamba_spatio-temporal_selective_state_space_model.md)
- [\[ECCV 2024\] VideoMamba: State Space Model for Efficient Video Understanding](videomamba_state_space_model_for_efficient_video_understanding.md)
- [\[ECCV 2024\] Towards Model-Agnostic Dataset Condensation by Heterogeneous Models](towards_model-agnostic_dataset_condensation_by_heterogeneous_models.md)
- [\[ECCV 2024\] SAFNet: Selective Alignment Fusion Network for Efficient HDR Imaging](safnet_selective_alignment_fusion_network_for_efficient_hdr_imaging.md)
- [\[ECCV 2024\] Leveraging Temporal Contextualization for Video Action Recognition](leveraging_temporal_contextualization_for_video_action_recognition.md)

<!-- RELATED:END -->
