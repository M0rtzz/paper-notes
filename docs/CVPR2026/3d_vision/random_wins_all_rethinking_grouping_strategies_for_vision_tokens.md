---
description: "【论文笔记】Random Wins All: Rethinking Grouping Strategies for Vision Tokens 论文解读 | CVPR 2026 | arXiv 2603.00486 | Transformer Vision Transformer | 发现一个极简策略——随机分组 Vision Token——在图像分类、目标检测、点云分割等多类任务中几乎全面超越精心设计的分组方法，并分析了四个关键成功因素。"
tags:
  - CVPR 2026
  - Transformer
---

# Random Wins All: Rethinking Grouping Strategies for Vision Tokens

**会议**: CVPR 2026  
**arXiv**: [2603.00486](https://arxiv.org/abs/2603.00486)  
**作者**: Qihang Fan, Yuang Ai, Huaibo Huang, Ran He (中科院自动化所)  
**代码**: [GitHub](https://github.com/qhfan/random)  
**领域**: 3D视觉  
**关键词**: Vision Transformer, Token分组, 随机分组, 注意力机制, 效率优化

## 一句话总结

发现一个极简策略——随机分组 Vision Token——在图像分类、目标检测、点云分割等多类任务中几乎全面超越精心设计的分组方法，并分析了四个关键成功因素。

## 背景与动机

Transformer 的自注意力机制具有二次复杂度，Vision Token 分组是降低复杂度的主流方案。现有方法从简单的窗口分区（Swin）到复杂的语义聚类（Quadtree, BiFormer），设计越来越复杂但效率不断下降。核心疑问：这些精心设计的分组方法真的有必要吗？

## 核心问题

是否存在一种极简且统一的 token 分组策略，能够替代各种复杂分组方法并维持甚至提升性能？

## 方法详解

### 随机分组策略

方法极为简洁，仅四步：

**Step 1: 生成随机张量**。对输入 token $X \in \mathbb{R}^{h \times w \times d}$，生成一个固定的随机张量 $P \in \mathbb{R}^{h \times w}$，与 $X$ 一一对应。$P$ 生成后即被存储固定。

**Step 2: 排序**。按 $P$ 降序排列，$X$ 随之重排得到 $X_p$。由于 $P$ 固定，每张图的 token 排列顺序相同。

**Step 3: 等分分组**。将已随机打乱的 $X_p$ 均等分割，即得到随机分组结果。

**Step 4: 多头扩展**。将 $P$ 的形状从 $h \times w$ 扩展为 $n \times h \times w$（$n$ 为注意力头数），每个头使用不同的随机分组。

### 高分辨率适配

当应用于检测/分割等高分辨率任务时，使用最近邻插值将固定的 $P$ 调整到对应分辨率。

### 三类 baseline 适配

- **Plain backbone**（如 DeiT）：随机分组后组内做 self-attention
- **Partition-based**（如 Swin）：直接替换窗口分组为随机分组
- **Pooling-based**（如 PVTv2）：替换 token pooling 前的分组策略

### 四个关键成功因素

通过深入分析，论文总结了随机分组成功的四要素：

1. **位置信息 (Positional Information)**：有位置编码时随机分组才有效
2. **头特征多样性 (Head Feature Diversity)**：多头中不同的随机分组产生互补的注意力模式
3. **全局感受野 (Global Receptive Field)**：随机分组天然打破局部性，tokens 来自全局
4. **固定分组模式 (Fixed Grouping Pattern)**：所有图片使用相同的随机排列，保证训练稳定

## 实验关键数据

| 模型 | Params (M) | FLOPs (G) | 吞吐量 (img/s) | Top-1 Acc (%) |
|------|-----------|-----------|---------------|---------------|
| Swin-T | 28 | 4.5 | 1738 | 81.3 |
| **Random-Swin-T** | **28** | **4.5** | **1866** | **82.7 (+1.4)** |
| Swin-S | 50 | 8.7 | 1186 | 83.0 |
| **Random-Swin-S** | **50** | **8.7** | **1248** | **83.9 (+0.9)** |
| Quadtree-b2 | 24 | 4.5 | 467 | 82.7 |
| **Random-Quadtree-b2** | **21** | **4.3** | **1926** | **83.4 (+0.7)** |
| BiFormer-B | 57 | 9.8 | 544 | 84.3 |
| **Random-BiFormer-B** | **57** | **9.6** | **667** | **85.1 (+0.8)** |

| Backbone | Mask R-CNN $AP^b$ | $AP^m$ | RetinaNet $AP^b$ |
|----------|------------------|--------|-----------------|
| Swin-T | 43.7 | 39.8 | 41.7 |
| **Random-Swin-T** | **46.0 (+2.3)** | **41.9 (+2.1)** | **44.3 (+2.6)** |

*在目标检测和实例分割上优势更加明显*

## 亮点

- **反直觉的发现**：随机方法几乎全面胜过所有精心设计的分组策略
- **极致简洁**：实现仅需排序和等分，无复杂聚类或路由操作
- **速度提升显著**：vs Quadtree 速度提升 3× 以上，同时精度也更高
- **跨模态验证**：在图像分类、目标检测、语义分割、点云分割和 VLM 上均验证有效
- **四关键因素的深入分析**：不仅展示结果，还解释了为什么随机性有效

## 局限性 / 可改进方向

- 随机分组在某些超低计算量 baseline 上的增益可能较小（如 CSwin-T 仅 +0.4）
- 固定随机排列是否最优？可探索周期性更换或学习化的"伪随机"
- 对 3D 点云的验证范围有限，仅基于 Point Transformer v3
- 未深入分析在极长序列（如视频）或极大分辨率下的表现

## 与相关工作的对比

- vs **Swin Transformer**：Swin 使用空间局部窗口 + 移位窗口，Random 直接打破空间局部性，精度 +1.3 且推理更快
- vs **BiFormer**：BiFormer 用双级路由做 content-aware 分组，Random 无需路由开销也更好
- vs **Quadtree**：Quadtree 用树结构层级分组，复杂度高速度慢 3×，精度反而更低
- vs **EViT**：EViT 通过丢弃/融合不重要 token 降低计算量，Random 全部保留但分组计算

## 启发与关联

- 这项工作挑战了"复杂设计 = 更好性能"的惯性思维，与 Lottery Ticket Hypothesis 等简洁主义有呼应
- 随机性在深度学习中的正面效应值得进一步研究（Dropout, Random Erasing, Stochastic Depth）
- 四因素分析为设计新的高效注意力机制提供了实用指导：只要满足这四条件，不必在分组策略上花太多心思

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 反直觉的发现，挑战了领域常识
- 实验充分度: ⭐⭐⭐⭐⭐ — 10+ baseline，多任务多模态验证
- 写作质量: ⭐⭐⭐⭐ — 叙述清晰，分析深入
- 价值: ⭐⭐⭐⭐⭐ — 对 Vision Transformer 设计有重要启示
