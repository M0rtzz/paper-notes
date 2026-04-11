---
description: "【论文笔记】Versatile Transition Generation with Image-to-Video Diffusion 论文解读 | ICCV 2025 | arXiv 2508.01698 | 过渡视频生成 | 本文提出 VTG，一个统一的过渡视频生成框架，通过插值初始化（噪声/LoRA/文本 SLERP）、双向运动微调和 DINOv2 表征对齐正则化，在单一框架中处理物体变形、运动预测、概念混合和场景过渡四类任务。"
tags:
  - ICCV 2025
---

# Versatile Transition Generation with Image-to-Video Diffusion

**会议**: ICCV 2025  
**arXiv**: [2508.01698](https://arxiv.org/abs/2508.01698)  
**代码**: https://mwxely.github.io/projects/yang2025vtg/  
**领域**: 视频生成 / 扩散模型  
**关键词**: 过渡视频生成, 图像变形, 概念混合, 双向运动, 表征对齐

## 一句话总结

本文提出 VTG，一个统一的过渡视频生成框架，通过插值初始化（噪声/LoRA/文本 SLERP）、双向运动微调和 DINOv2 表征对齐正则化，在单一框架中处理物体变形、运动预测、概念混合和场景过渡四类任务。

## 研究背景与动机

1. **过渡视频的难度**：给定首尾两帧和文本描述生成高质量过渡视频需满足四个标准——语义保真、视觉保真、时序平滑、文本对齐。现有方法大多只能处理单一过渡类型。

2. **现有方法的不足**：
   - **形变方法**（DiffMorpher）：仅生成离散图像而非时序连贯的视频帧
   - **视频插帧**：对大内容变化的输入产生不合理的过渡（突变）
   - **缺乏统一框架**：不同过渡类型（形变、混合、运动、场景）各自为政

3. **统一四类过渡任务**：
   - **物体变形**：拓扑相似的物体/同一物体不同姿态
   - **概念混合**：概念不同的物体（飞机→邮轮）
   - **运动预测**：同一场景中运动物体的两个时刻
   - **场景过渡**：语义相关但域不同的场景

## 方法详解

### 整体架构

基于预训练 Image-to-Video 扩散模型（DynamiCrafter），包含三个核心设计：

### 关键设计一：插值初始化

**球面线性插值(SLERP)噪声注入**：

$$\mathbf{z}_{tn} = \frac{\sin((1-\lambda_{noise})\phi)}{\sin\phi}\mathbf{z}_{t1} + \frac{\sin(\lambda_{noise}\phi)}{\sin\phi}\mathbf{z}_{tN}$$

将两个输入帧 DDIM 反演得到的潜在噪声通过 SLERP 插值，保持高斯分布的欧几里得范数，避免线性插值的 off-distribution 问题。仅在早期去噪步注入。

**LoRA 插值**：分别为两个输入帧训练 LoRA $\Delta\theta_1, \Delta\theta_N$，线性插值融合语义：

$$\Delta\theta = (1-\lambda_{LoRA})\Delta\theta_1 + \lambda_{LoRA}\Delta\theta_N$$

**帧感知文本 SLERP**：对两帧对应 caption 的文本嵌入也进行 SLERP，实现逐帧语义渐变。

### 关键设计二：双向运动微调 (BMP)

解决 I2V 模型仅学习单向运动导致的"帧序反转质量不对称"问题：

$$\mathcal{L}_{BMP} = \|\text{flip}(\epsilon_t) - \epsilon_{\theta_{w,o}}(\mathbf{z}_{t'}, \mathbf{c}, t, A'_{i,j})\|_2^2$$

- 将时序自注意力映射旋转 180°，反转视频帧序
- 仅更新时序注意力中的 Value 和 Output 矩阵（轻量微调）
- 推理时前向/后向预测噪声线性融合：$\epsilon_t = (1-\lambda_{BMP})\epsilon_{t,i} + \lambda_{BMP}\epsilon'_{t,N-i}$

### 关键设计三：表征对齐正则化 (RAR)

解决扩散潜在表示缺乏高频语义导致的模糊问题：

$$\mathcal{L}_{RAR} = -\sum_{n=1}^{N}\mathbb{E}_{t,\mathbf{x}_*,\epsilon_t}\left[\frac{1}{P}\sum_{p=1}^{P}\text{sim}(\mathbf{y}_*^{[p]}, y_\phi(\mathbf{h}_t)^{[p]})\right]$$

- 将每帧潜在表示 patchify 后通过 MLP 投影
- 与 DINOv2 编码器提取的 patch 级表征对齐
- 推理时丢弃 DINOv2 和 MLP，零额外推理开销

## 实验

### MorphBench 定量结果

| 方法 | FID↓ (变形) | PPL↓ (变形) | FID↓ (动画) | PPL↓ (动画) |
|------|------------|------------|------------|------------|
| DiffMorpher | 70.49 | 18.19 | 43.15 | 5.14 |
| TVG | 86.92 | 35.18 | 42.99 | 12.46 |
| SEINE | 82.03 | 47.72 | 48.25 | 16.26 |
| DynamiCrafter | 87.32 | 42.09 | 43.31 | 11.16 |
| **VTG** | **67.39** | **22.80** | **39.16** | **5.14** |

### TC-Bench 运动一致性

| 方法 | Attr TCR↑ | Object TCR↑ | Bg TCR↑ |
|------|-----------|-------------|---------|
| DiffMorpher | 41.82 | 19.57 | 50.00 |
| TVG | 41.82 | 30.44 | 38.89 |
| **VTG** | **42.78** | **33.46** | **50.00** |

### 关键发现

- VTG 在 MorphBench 变形任务上 FID 最低（67.39 vs DiffMorpher 70.49），PPL 接近最佳
- 在 TC-Bench 上属性、物体、背景一致性均排名第一
- 定性对比中，VTG 是唯一能在概念混合中生成合理中间语义的方法（如"狮子颜色大小的卡车"）
- 训练仅需 150 个高质量视频、4×A100、约 20K 迭代，成本可控

## 亮点与洞察

1. **统一四类过渡任务**：首次在单一框架中处理变形、混合、运动和场景过渡
2. **TransitBench**：新基准数据集含 200 对概念混合/场景过渡图像对
3. **LoRA 训练极快**：每对输入帧仅需 ~85s（1×A100），200 步

## 局限性

- 每对新输入帧需重新训练 LoRA（约 85s），非完全即插即用
- BMP 需要额外训练视频数据；RAR 训练时需 DINOv2 前向传播
- 概念变化极大时插值假设可能不成立

## 相关工作

- **图像变形**: DiffMorpher, SDS-Interpolation
- **视频插帧**: FILM, RIFE, AMT
- **过渡生成**: SEINE, TVG

## 评分

- 新颖性：⭐⭐⭐⭐ — 四类任务统一框架有价值
- 技术深度：⭐⭐⭐⭐ — 三个核心组件逻辑紧密
- 实验充分度：⭐⭐⭐⭐ — 多基准覆盖四类任务
- 实用价值：⭐⭐⭐⭐ — 视频/电影后期制作
