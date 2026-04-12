---
title: >-
  [论文解读] Locality-Attending Vision Transformer
description: >-
  [ICLR 2026][图像分割][ViT] 提出 LocAt，一个轻量级 ViT 插件，通过可学习高斯核调制自注意力偏向局部邻域(GAug)和无参数的 Patch 表征精炼(PRR)，在不改变训练范式的前提下为 ViT 带来 6%+ 的分割性能提升且不牺牲分类精度。
tags:
  - ICLR 2026
  - 图像分割
  - ViT
  - locality
  - 注意力机制
  - patch representation
  - dense prediction
---

# Locality-Attending Vision Transformer

**会议**: ICLR 2026  
**arXiv**: [2603.04892](https://arxiv.org/abs/2603.04892)  
**代码**: [GitHub](https://github.com/sinahmr/LocAtViT/)  
**领域**: segmentation / vision transformer  
**关键词**: ViT, locality, Gaussian attention, semantic segmentation, patch representation, dense prediction  

## 一句话总结
提出 LocAt，一个轻量级 ViT 插件，通过可学习高斯核调制自注意力偏向局部邻域(GAug)和无参数的 Patch 表征精炼(PRR)，在不改变训练范式的前提下为 ViT 带来 6%+ 的分割性能提升且不牺牲分类精度。

## 背景与动机
1. ViT 的全局自注意力在分类中表现出色，但会模糊密集预测所需的细粒度空间细节
2. 分类训练 ViT 中，patch token 逐渐丢失局部结构并向 [CLS] token 对齐
3. 现有改进(层级 ViT、窗口注意力)需要大幅修改架构，不适合基础模型
4. 分类目标未考虑密集预测需求，patch 位置的输出不受直接监督
5. GAP 聚合也存在问题：均匀梯度流让所有 patch 接收相同重要性
6. CLIP 等基础模型采用 vanilla ViT，增强 ViT 本身比设计新架构更有实用价值

## 方法详解
**Gaussian-Augmented Attention (GAug)**:
- 在注意力 logit 上加一个补充矩阵 $\mathbf{S}$：$\mathbf{Z} = \text{softmax}(\frac{\mathbf{q}\mathbf{k}^\top}{\sqrt{d}} + \mathbf{S})\mathbf{v}$
- $\mathbf{S}$ 由可学习高斯核生成：以每个 patch 为中心，方差从 query 预测
- $\boldsymbol{\Sigma} = f(\mathbf{q}_{sp} \mathbf{W}^\sigma)$，缩放系数 $\boldsymbol{\alpha} = \text{softplus}(\mathbf{q}_{sp}\mathbf{W}^\alpha)$
- 数据依赖的软局部性约束：$\alpha$ 小时接近标准全局注意力，$\alpha$ 大时强局部偏置
- [CLS] token 不受局部偏置影响

**Patch Representation Refinement (PRR)**:
- 在分类头前加一个无参数多头自注意力
- 将梯度路由到所有 patch token 位置
- 解决 ViT 分类训练中 patch 输出无直接监督的问题

**耦合关系**: PRR 将梯度传到最后一层的 GAug 参数使其能有效学习

## 实验关键数据
| 方法 (Tiny) | ADE20K mIoU | P-Context mIoU | COCO-Stuff mIoU | ImageNet Top-1 |
|---|---|---|---|---|
| ViT | 17.30 | 33.71 | 20.29 | 72.39 |
| **LocAtViT** | **23.47 (+6.17)** | **38.57 (+4.86)** | **26.15 (+5.86)** | **73.94 (+1.55)** |
| RegViT | 15.98 | 33.45 | 19.58 | 72.90 |
| **LocAt+RegViT** | **24.39 (+8.41)** | **39.90 (+6.45)** | **27.38 (+7.80)** | **74.08** |

- Base 规模在 ADE20K 上也提升 4%+
- 适用于 ViT/Swin/RegViT/RoPEViT/Jumbo 等多个基线
- FLOPs 增加可忽略（Tiny: 1.26→1.27G）
- 分割评估使用冻结主干 + 单层 MLP 解码器

### 消融实验

| 配置 (ViT-Tiny) | ADE20K mIoU | ImageNet Top-1 | 说明 |
|------|-------------|---------------|------|
| ViT 原始 | 17.30 | 72.39 | 基线 |
| +GAug only | 19.82 | 73.21 | 仅高斯注意力 |
| +PRR only | 20.15 | 72.95 | 仅梯度修复 |
| **+GAug+PRR (LocAt)** | **23.47** | **73.94** | **两者耦合最佳** |

### 关键发现
- GAug 和 PRR 通过梯度路径耦合：若无 PRR 将梯度路由到 patch 输出，最后一层的 GAug 参数无法从损失获得梯度
- 小数据集（CIFAR-100/mini-ImageNet）上分类提升更显著（4-7%），表明局部性先验在数据不充分时尤为关键
- LocAt 在已有局部性机制的 Swin 上仍有 ~1% 提升，在 vanilla ViT 和 RegViT 上提升最大（6-8%）
- FLOPs 增加可忽略（Tiny: 1.26→1.27 GFLOPs），LocAt 仅新增 2,340 参数（Base 规模仅增 0.003%）

## 亮点与洞察
- **极简设计**：仅新增 $\mathbf{W}^\sigma$（d×2）和 $\mathbf{W}^\alpha$（d×1）两个小矩阵，PRR 完全无参数——是我见过参数效率最高的 ViT 改进
- **segmentation-in-mind pretraining**：不改变分类训练范式，却显著提升分割性能，这个理念对基础模型设计有启发
- **梯度流分析**：揭示了 ViT 分类训练中 patch token 在最后层缺乏监督的根本问题——PRR 通过非均匀梯度流优雅解决
- **分类不降反升**：在多数模型上分类精度还有小幅提升（Tiny +1.55%），说明局部性先验的引入不是以牺牲全局理解为代价
- **通用即插即用**：可插入 ViT/Swin/RegViT/RoPEViT/Jumbo 等多种基线，且与 RoPE 等位置编码正交互补

## 局限性 / 可改进方向
- 分割评估仅用冻结主干 + 单层 MLP 解码器，未在完整分割框架（如 UperNet/Mask2Former）下充分验证实际部署效果
- 高斯核假设二维独立方差，可能不适合高度非对称的目标（如细长物体）
- 未在 CLIP/DINOv2 等大规模基础模型上实测，这恰恰是 LocAt 最有价值的应用场景
- PRR 的无参数自注意力在更大分辨率（如 1024×1024）下的计算开销和效果未讨论
- 高斯核的尺度 σ 在不同分辨率间的传递策略（按比例缩放）缺乏理论依据

## 相关工作与启发
- **vs Swin/PVT**：层级 ViT 通过架构变化引入多尺度，但改动大不兼容 vanilla ViT 生态；LocAt 是最小改动
- **vs DeiT/RegViT**：Register token 吸收噪声信息改善特征图但未解决梯度流到 patch 位置的核心问题
- **vs RoPE/RPE**：位置编码增强空间感知与 LocAt 的注意力局部性正交互补——实验证明组合使用进一步提升
- **vs NAT/DAT**：邻域/稀疏注意力限制或掩蔽交互，而 GAug 是软约束不阻断全局信息流

## 评分
- 新颖性: ⭐⭐⭐⭐ 高斯注意力调制 + PRR 梯度流修复的组合简洁新颖
- 实验充分度: ⭐⭐⭐⭐ 5 种模型 × 3 种分割基准 + 分类 + 小数据集 + 消融
- 写作质量: ⭐⭐⭐⭐⭐ 动机推导清晰，理论与实验分析深入
- 价值: ⭐⭐⭐⭐ 对基础模型的 ViT backbone 有直接改进价值
