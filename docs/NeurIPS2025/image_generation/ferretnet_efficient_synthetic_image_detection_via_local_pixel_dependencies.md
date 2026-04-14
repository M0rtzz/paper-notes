---
title: >-
  [论文解读] FerretNet: Efficient Synthetic Image Detection via Local Pixel Dependencies
description: >-
  [NeurIPS 2025][图像生成][synthetic image detection] 基于 Markov Random Field 理论提出局部像素依赖（LPD）特征表示，结合仅 1.1M 参数的轻量 FerretNet 网络，仅在 4 类 ProGAN 数据上训练即在 22 个生成模型上达到 97.1% 平均准确率。
tags:
  - NeurIPS 2025
  - 图像生成
  - synthetic image detection
  - local pixel dependencies
  - Markov Random Fields
  - lightweight network
  - generalization
---

# FerretNet: Efficient Synthetic Image Detection via Local Pixel Dependencies

**会议**: NeurIPS 2025  
**arXiv**: [2509.20890](https://arxiv.org/abs/2509.20890)  
**代码**: [FerretNet](https://github.com/xigua7105/FerretNet)  
**领域**: image_generation  
**关键词**: synthetic image detection, local pixel dependencies, Markov Random Fields, lightweight network, generalization

## 一句话总结

基于 Markov Random Field 理论提出局部像素依赖（LPD）特征表示，结合仅 1.1M 参数的轻量 FerretNet 网络，仅在 4 类 ProGAN 数据上训练即在 22 个生成模型上达到 97.1% 平均准确率。

## 研究动机

合成图像检测面临两大核心挑战：

- **泛化能力不足**：许多检测方法依赖模型特定特征（如频域伪影），难以跨模型泛化
- **计算效率低**：基于预训练大模型（如 CLIP）的方法虽有较好泛化性，但参数量大、推理慢

本文从生成过程的共性出发，识别出两类通用伪影来源：
1. **潜变量分布偏移**：采样分布 $Q(z)$ 与训练时先验 $P(z)$ 的不匹配
2. **解码过程的平滑效应**：卷积核大小、步幅、上采样方式引入的纹理异常

## 方法详解

### 局部像素依赖（LPD）特征提取

基于 Markov Random Field 假设，像素的概率分布仅依赖于局部邻域：

$$P(x_{i,j} \mid x_{k,l}, (k,l) \neq (i,j)) = P(x_{i,j} \mid x_{k,l}, (k,l) \in \mathcal{N}_{i,j})$$

其中 $\mathcal{N}_{i,j}$ 为以 $(i,j)$ 为中心的 $n \times n$ 邻域（不含中心）。

**中值重建**：引入零掩码策略，将中心像素置零后计算邻域中值：

$$y_{i,j} = \text{Median}(x_{k,l}, (k,l) \in \mathcal{N}_{i,j}')$$

其中 $\mathcal{N}_{i,j}' = \mathcal{N}_{i,j} \cup \{x_{i,j} = 0\}$。

**LPD 特征图**为原图与中值重建图的逐像素差异：

$$\text{LPD} = I - I'$$

真实图像因物理成像过程的局部一致性，LPD 差异小且均匀；合成图像在纹理连续性和边缘连贯性上存在微观破坏，LPD 差异更大且呈结构化分布。

### FerretNet 架构

轻量卷积网络，总计仅 **1.1M 参数**：

- **输入层**：2 个 3×3 卷积 + BN + ReLU
- **核心模块**：4 个级联 Ferret Block
  - **主路径**：3×3 膨胀分组卷积（dilation=2），扩大感受野
  - **辅路径**：3×3 标准分组卷积，捕获细粒度局部模式
  - 双路径输出通过 1×1 卷积融合，等效稀疏 5×5 感受野
  - 残差连接保证梯度稳定
- **输出层**：1×1 卷积 + 全局平均池化 + Dropout + 全连接分类

### 训练细节

- 仅在 ProGAN 4 类（car, cat, chair, horse）上训练，每类 18K 合成 + 18K 真实
- Adam 优化器，lr=2×10⁻⁴，batch=32，100 epochs
- 训练裁剪 224×224，测试中心裁剪 256×256
- BCEWithLogitsLoss 损失函数

## 实验结果

### ForenSynths 测试集（8 个 GAN + Deepfake 模型）

| 方法 | 参数量 | ProGAN | StyleGAN2 | BigGAN | CycleGAN | Deepfake | 均值 ACC/AP |
|------|--------|--------|-----------|--------|----------|----------|-------------|
| Ojha | ~300M | 99.7 | 83.9 | 90.5 | 87.9 | 80.2 | 89.1/98.3 |
| FatFormer | ~150M | 99.9 | 98.8 | 99.5 | 99.3 | 93.2 | 98.4/99.7 |
| **FerretNet** | **1.1M** | **99.9** | **98.5** | **92.6** | **98.8** | **89.2** | **95.9/99.3** |

### Diffusion-6-cls 测试集（6 个扩散模型）

| 方法 | DALL-E | Guided | LDM-200 | 均值 ACC/AP |
|------|--------|--------|---------|-------------|
| FatFormer | 98.8 | 76.1 | 98.6 | 95.0/98.8 |
| SAFE | 97.5 | 82.4 | 98.8 | 94.5/99.1 |
| **FerretNet** | 91.4 | **92.1** | **98.8** | **96.9/99.6** |

### Synthetic-Pop 测试集（6 个最新高分辨率模型）

| 方法 | SDXL-Turbo | RealVisXL-4.0 | SD-3.5-Medium | 均值 ACC/AP |
|------|-----------|---------------|---------------|-------------|
| FatFormer | 58.7 | 49.0 | 81.9 | 70.5/74.8 |
| SAFE | 98.1 | 97.9 | 98.1 | 97.9/99.7 |
| **FerretNet** | **98.9** | **98.8** | **97.2** | **98.3/99.8** |

### 效率对比

| 方法 | 参数量(M) | FLOPs(G) | FPS |
|------|----------|----------|-----|
| FatFormer | 174.83 | 61.10 | 79.9 |
| SAFE | 1.85 | 2.58 | 223.1 |
| **FerretNet** | **1.10** | **0.24** | **4024.8** |

FerretNet 的 FPS 是 FatFormer 的 50 倍、SAFE 的 18 倍。

### 跨 22 模型平均性能

在全部 22 个生成模型的开放世界测试中，FerretNet 以 97.1% 的平均准确率名列前茅，同时保持极低计算开销。

## 评价

⭐⭐⭐⭐

**优点**：
- LPD 特征基于 MRF 理论有清晰的物理直觉，抓住了生成模型的共性伪影
- 极致轻量设计：1.1M 参数、0.24G FLOPs、4000+ FPS，适合边缘部署
- 仅 4 类 ProGAN 训练即泛化到 22 个生成模型（含最新 SD 3.5），泛化能力极强
- 新提出 Synthetic-Pop 60K 基准，覆盖最新高保真生成模型

**局限**：
- 在部分 GAN 模型（如 BigGAN）上略逊于 FatFormer 等大模型方法
- LPD 特征依赖中值滤波窗口大小 $n$ 的选择，对不同分辨率可能需要调整
- 面对未来更先进的生成模型（如视频生成），LPD 方法的适用性需进一步验证
- 价值: 待评
