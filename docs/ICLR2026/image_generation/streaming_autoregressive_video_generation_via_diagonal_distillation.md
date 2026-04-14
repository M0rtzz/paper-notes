---
title: >-
  [论文解读] Streaming Autoregressive Video Generation via Diagonal Distillation
description: >-
  [ICLR 2026][图像生成][对角蒸馏] 提出 DiagDistill 对角蒸馏框架，通过对角去噪策略（早期多步、后期少步）和光流分布匹配，实现实时流式自回归视频生成，5秒视频仅需2.61秒（31 FPS），比未蒸馏模型加速277.3倍。
tags:
  - ICLR 2026
  - 图像生成
  - 对角蒸馏
  - 自回归视频生成
  - 流分布匹配
  - 对角强制
  - 流式视频
---

# Streaming Autoregressive Video Generation via Diagonal Distillation

**会议**: ICLR 2026  
**arXiv**: [2603.09488](https://arxiv.org/abs/2603.09488)  
**代码**: [SphereLab.ai/diagdistill](https://SphereLab.ai/diagdistill)  
**领域**: 视频生成 / 扩散蒸馏 / 实时推理  
**关键词**: 对角蒸馏, 自回归视频生成, 流分布匹配, 对角强制, 流式视频

## 一句话总结

提出 DiagDistill 对角蒸馏框架，通过对角去噪策略（早期多步、后期少步）和光流分布匹配，实现实时流式自回归视频生成，5秒视频仅需2.61秒（31 FPS），比未蒸馏模型加速277.3倍。

## 研究背景与动机

视频扩散模型质量优异但无法实时流式生成：

**双向注意力的限制**：标准扩散模型需要同时处理所有帧（包括未来帧），不适合实时场景

**自回归扩散的计算瓶颈**：AR+扩散混合模型每个chunk需多步去噪，延迟较高

**现有蒸馏方法的不足**：大多从图像生成适配而来，忽视时间维度
   - 压缩到极少步时运动连贯性下降
   - 长序列误差累积导致过饱和
   - 未充分利用跨chunk的时间上下文

**关键洞察**：在自回归视频生成中，预测下一个chunk本质上需要隐式预测下一个噪声水平。这引入了曝光偏差（exposure bias）和结构先验的浪费两个问题。

## 方法详解

### 1. 对角去噪策略

核心创新：非均匀步分配——早期chunk分配更多去噪步，后期逐渐减少。

- 前3个chunk：递减步数 $(s_1, s_2, s_3) = (5, 4, 3)$
- 第4个chunk起：固定2步去噪
- $\mathbf{X}_k = \mathcal{D}_2(\mathcal{D}_1(\mathbf{Z}_k|\mathbf{C}_k)|\mathbf{C}_k)$

**直觉**：早期chunk建立高质量的外观基础，后期chunk继承这些结构先验，因此即使少步也能生成清晰帧。

### 2. 对角强制（Diagonal Forcing）

训练时显式模拟对角去噪路径，通过可控噪声注入实现：

$$\mathbf{\tilde{X}}_{k-1} = \sqrt{\alpha_{k-1}} \cdot \mathbf{X}_{k-1} + \sqrt{1-\alpha_{k-1}} \cdot \boldsymbol{\epsilon}$$

- 将前一chunk的噪声化表示作为当前chunk的KV缓存
- 保持对角去噪轨迹 $\mathbf{X}_k \to \mathbf{\tilde{X}}_{k-1} \to \mathbf{X}_{k-1}$
- 最优噪声时间步：100步（1000步总范围），过多噪声模糊先验、过少导致过饱和

### 3. 光流分布匹配

解决少步去噪导致的运动幅度衰减：

**分布匹配损失**：
$$\nabla_\phi \mathcal{L}_{\text{DMD}}^{\text{flow}} = \mathbb{E}_t(\nabla_\phi \text{KL}(p_{\text{gen,flow},t} \| p_{\text{data,flow},t}))$$

**光流回归损失**：
$$\mathcal{L}_{\text{reg}}^{\text{flow}} = \mathbb{E}_{t,\epsilon}[\|\mathcal{F}(G_\phi^{\text{teacher}}(\epsilon,t)) - \mathcal{F}(G_\phi^{\text{student}}(\epsilon,t))\|_2^2]$$

- 光流提取模块 $\mathcal{F}$ 是轻量级自包含模块，无需外部预训练模型
- 基于连续潜在帧的差值和卷积提取局部运动模式
- 教师版本通过EMA更新

### 総体目标

$$\mathcal{L}_{\text{Total}} = \lambda_{\text{spatial}}\mathcal{L}_{\text{DMD}} + \mathcal{L}_{\text{reg}} + \gamma(\lambda_{\text{flow}}\mathcal{L}_{\text{DMD}}^{\text{flow}} + \mathcal{L}_{\text{reg}}^{\text{flow}})$$

## 实验

### 实现细节
- 基于 Wan2.1-T2V-1.3B（Flow Matching）
- 3帧chunk大小，滚动KV缓存（最近4个chunk）
- 固定显存 17.5 GB
- 评估：VBench（时间质量、帧质量、文本对齐）

### 主要结果

| 方法 | 吞吐量(FPS)↑ | 首帧延迟(s)↓ | 加速比 | 总分↑ | 质量↑ | 语义↑ |
|------|-------------|------------|--------|-------|-------|-------|
| Wan2.1 | 0.78 | 103 | 1× | 84.26 | 85.30 | 80.09 |
| SkyReels-V2 | 0.49 | 112 | 0.91× | 82.67 | 84.70 | 74.53 |
| MAGI-1 | 0.19 | 282 | 0.36× | 79.18 | 82.04 | 67.74 |
| Causvid | 17.0 | 0.69 | 149.3× | 81.20 | 84.05 | 69.80 |
| Self-Forcing | 17.0 | 0.69 | 149.3× | 84.31 | 85.07 | 81.28 |
| **DiagDistill** | **31.0** | **0.37** | **277.3×** | **84.48** | **85.26** | **81.73** |

### 消融实验

| 组件 | 效果 |
|------|------|
| 去除光流匹配 | 运动幅度衰减 |
| 去除对角强制 | 长序列过饱和 |
| 去除对角去噪 | 性能可比但速度慢1.53× |
| 对角强制100步 | 最优（vs 0步过饱和、1000步模糊） |

### 长视频生成（45秒）
相比 Self-Forcing 和 Causvid，DiagDistill 在长序列中保持细节和一致性，无明显饱和失真。

## 亮点

1. **277.3×加速**：实现实时31 FPS视频生成
2. **质量与基线模型持平**：85.26 vs Wan2.1的85.30
3. **对角蒸馏范式的独创性**：跨时间和去噪步的正交操作
4. **长序列稳定性**：对角强制有效缓解曝光偏差
5. **光流分布匹配**：隐式运动建模保持动态一致性

## 局限性

1. 基于特定模型（Wan2.1-1.3B）训练，泛化到更大模型需验证
2. 2步去噪的后期chunk仍可能在极复杂运动场景下质量下降
3. 对角步数调度需要预定义，缺乏自适应机制
4. 首帧延迟（0.37s）对某些实时交互场景可能仍不够

## 相关工作

- **扩散蒸馏**：DMD、LADD、ADD、一致性蒸馏
- **自回归视频**：Causvid、Self-Forcing、MAGI
- **混合模型**：SkyReels-V2、diffusion+AR混合

## 评分

- **创新性**: ⭐⭐⭐⭐⭐ — 对角蒸馏+对角强制+光流匹配的完整框架
- **实用性**: ⭐⭐⭐⭐⭐ — 实现真正的实时视频生成
- **实验**: ⭐⭐⭐⭐ — VBench全面评估，消融充分
- **写作**: ⭐⭐⭐⭐ — 动机清晰，方法描述系统
