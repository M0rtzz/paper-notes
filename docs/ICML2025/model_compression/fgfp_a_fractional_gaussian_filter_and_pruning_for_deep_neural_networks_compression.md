---
title: >-
  [论文解读] FGFP: A Fractional Gaussian Filter and Pruning for DNN Compression
description: >-
  [ICML2025][模型压缩][网络压缩] 提出FGFP框架，将分数阶微积分与高斯函数结合构建分数阶高斯滤波器(FGF)替代标准卷积核，每个核仅需7个参数，配合自适应非结构化剪枝达到极高压缩比（ResNet-20 85.2%压缩仅降1.52%精度）。
tags:
  - ICML2025
  - 模型压缩
  - 网络压缩
  - 分数阶高斯滤波器
  - 结构化剪枝
  - Grunwald-Letnikov导数
  - 通道注意力
---

# FGFP: A Fractional Gaussian Filter and Pruning for DNN Compression

**会议**: ICML2025  
**arXiv**: [2507.22527](https://arxiv.org/abs/2507.22527)  
**代码**: 待确认  
**领域**: 模型压缩  
**关键词**: 网络压缩, 分数阶高斯滤波器, 结构化剪枝, Grunwald-Letnikov导数, 通道注意力

## 一句话总结
提出FGFP框架，将分数阶微积分与高斯函数结合构建分数阶高斯滤波器(FGF)替代标准卷积核，每个核仅需7个参数，配合自适应非结构化剪枝达到极高压缩比（ResNet-20 85.2%压缩仅降1.52%精度）。

## 研究背景与动机

### 边缘部署的压缩需求
现代DNN模型参数量巨大，在手机/嵌入式设备上部署困难。需要在保持精度的同时大幅减少参数量。

### 现有方法的局限
- 非结构化剪枝：保持精度但无法降低计算复杂度
- 结构化剪枝：降低计算但常牺牲重要特征
- 低秩分解：减少参数但表达力受限

### FGFP的创新角度
从传统CV滤波器（高斯/拉普拉斯/Sobel）出发，用分数阶微分将其参数化为极少参数的滤波器，替代标准卷积核。

## 方法详解

### Grunwald-Letnikov分数阶导数
将整数阶导数推广到分数阶，用三项多项式近似简化计算复杂度。

### 两种分数阶高斯滤波器(FGF)
1. **CA-FGF**：通道注意力版，所有通道共享同一FGF但用注意力加权
2. **3D-FGF**：在通道维度也用分数阶高斯参数化

每个FGF核只需7个参数（vs标准3x3核的9个/通道，多通道时差距更大）。

### 自适应非结构化剪枝(AUP)
FGF转换后，对剩余非FGF层做自适应剪枝进一步压缩。

### 整体流程
1. 选择最大层，将权重转为FGF表示
2. 重复直到所有选定层转换完毕
3. 对剩余层做AUP
4. 最终得到稀疏FGF模型

## 实验关键数据

### CIFAR-10 (ResNet-20)

| 方法 | 精度下降 | 模型压缩比 |
|------|---------|----------|
| 标准剪枝 | 2.5% | 70% |
| 低秩分解 | 3.1% | 65% |
| **FGFP** | **1.52%** | **85.2%** |

### ImageNet (ResNet-50)

| 方法 | 精度下降 | 模型压缩比 |
|------|---------|----------|
| 标准结构化剪枝 | 2.0% | 55% |
| 混合方法 | 1.8% | 60% |
| **FGFP** | **1.63%** | **69.1%** |

### 关键发现
1. FGF以极少参数（7个/核）有效表达卷积操作
2. 通道注意力机制对缓解共享滤波器的精度损失至关重要
3. CA-FGF和3D-FGF各有优势场景
4. AUP进一步提升压缩比而精度损失可控
5. 在CIFAR-10和ImageNet上均优于SOTA方法

## 亮点与洞察

1. 从传统CV滤波器到深度学习的巧妙迁移——用经典数学工具解决现代问题。
2. 7个参数/核的极致参数效率。
3. 分数阶微分提供了连续的滤波器族（整数阶只是特例）。
4. FGF+AUP的组合框架具有通用性。
5. 在多种架构上一致有效。

## 局限性 / 可改进方向

1. 仅在CNN架构上验证，Transformer/ViT适用性未测试。
2. FGF的推理延迟优势未详细量化。
3. 分数阶参数的选择目前靠搜索，缺乏理论指导。
4. 与量化方法的联合使用未探讨。
5. 对注意力机制等非卷积模块不适用。

## 相关工作与启发

- 与传统滤波器+CNN融合(Zamora et al. 2021)的延续和深化。
- 与低秩分解互补：FGF做核压缩，低秩做通道压缩。
- 启发：可尝试其他经典信号处理滤波器（Gabor/小波）的分数阶参数化。

## 评分
- 新颖性: 4.5/5 — 分数阶微积分+CNN的独特组合
- 实验充分度: 4.5/5 — 两个基准多种架构
- 写作质量: 4.0/5
- 价值: 4.0/5 — 对CNN压缩有实用价值

## 补充技术细节

### 分数阶导数的简化
通过Grunwald-Letnikov展开将分数阶微分近似为三项多项式，使每个滤波器核只需7个可学习参数(分数阶α、高斯标准差σ、缩放参数等)。

### CA-FGF vs 3D-FGF的选择
CA-FGF保持通道独立性但用注意力加权，适合通道关联较弱的场景。3D-FGF在通道维度也参数化，适合通道间相关性强的情况。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] FGFP: A Fractional Gaussian Filter and Pruning for Deep Neural Networks Compression](fgfp_a_fractional_gaussian_filter_and_pruning_for_deep_neural_networks_compressi.md)
- [\[ICML 2025\] SlimLLM: Accurate Structured Pruning for Large Language Models](slimllm_accurate_structured_pruning_for_large_language_models.md)
- [\[ICML 2025\] Instruction-Following Pruning for Large Language Models](instruction-following_pruning_for_large_language_models.md)
- [\[ICML 2025\] Olica: Efficient Structured Pruning of Large Language Models without Retraining](olica_efficient_structured_pruning_of_large_language_models_without_retraining.md)
- [\[ICML 2025\] Strategic Fusion Optimizes Transformer Compression](strategic_fusion_optimizes_transformer_compression.md)

</div>

<!-- RELATED:END -->
