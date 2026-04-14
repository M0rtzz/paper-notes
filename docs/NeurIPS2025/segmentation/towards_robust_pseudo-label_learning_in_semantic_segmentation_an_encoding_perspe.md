---
title: >-
  [论文解读] Towards Robust Pseudo-Label Learning in Semantic Segmentation: An Encoding Perspective
description: >-
  [NeurIPS 2025][图像分割][伪标签] ECOCSeg从编码形式角度重新审视伪标签噪声问题，用纠错输出码(ECOC)替代argmax one-hot编码，将N类分类分解为K个二分类子任务，利用类间共享属性和bit级去噪机制显著提升伪标签学习的鲁棒性。
tags:
  - NeurIPS 2025
  - 图像分割
  - 伪标签
  - 纠错输出码
  - 语义分割
  - 无监督域自适应
  - 半监督学习
---

# Towards Robust Pseudo-Label Learning in Semantic Segmentation: An Encoding Perspective

**会议**: NeurIPS 2025  
**arXiv**: [2512.06870](https://arxiv.org/abs/2512.06870)  
**代码**: [GitHub](https://github.com/Woof6/ECOCSeg)  
**领域**: 语义分割 / 伪标签学习  
**关键词**: 伪标签, 纠错输出码, 语义分割, 无监督域自适应, 半监督学习

## 一句话总结

ECOCSeg从编码形式角度重新审视伪标签噪声问题，用纠错输出码(ECOC)替代argmax one-hot编码，将N类分类分解为K个二分类子任务，利用类间共享属性和bit级去噪机制显著提升伪标签学习的鲁棒性。

## 研究背景与动机

伪标签学习在语义分割的UDA和SSL中广泛使用，但不可避免地产生错误伪标签。现有方法沿两条路线缓解：(1) 过滤机制——只保留高置信度伪标签，但忽略困难样本导致次优；(2) 加权函数——依赖置信度设计权重，但超参数敏感。

作者观察到一个被忽略的关键点：**编码形式本身放大了伪标签噪声**。当模型将sheep误分为horse或cow时，argmax产生的one-hot标签完全丢失了"这些类共享有角、有蹄等视觉属性"的信息。这启发从编码角度设计新的伪标签形式，使得即使部分属性预测错误，共享属性仍能提供有效监督。

## 方法详解

### 整体框架

ECOCSeg将伪标签学习分解为三个基本组件并分别创新：
1. **编码形式**：ECOC二进制编码替代one-hot
2. **伪标签选择**：bit级去噪的混合伪标签
3. **优化准则**：pixel-code距离 + pixel-code对比损失

模型用K个sigmoid二分类器替代原始N类softmax分类器，通过码本近邻查询确定最终类别。

### 关键设计

1. **ECOC密集分类器**:
    - 功能：将N类分割问题分解为K个二分类子任务，每个类用K-bit码字表示
    - 核心思路：用sigmoid预测每个bit概率，通过软汉明距离 $d_{SH}(\mathbf{c}_n, \mathbf{p}^i)$ 在码本中近邻查询确定类别
    - 设计动机：相似类共享更多bit，即使部分bit预测错误也可正确分类；码本设计保证足够的最小汉明距离实现纠错
    - 码本构建：max-min距离编码（最大化类间最小距离）和text-based编码（利用类名语义）

2. **可靠Bit挖掘 (Reliable Bit Mining)**:
    - 功能：融合bit-wise和code-wise两种伪标签形式，产生高质量混合伪标签
    - 核心思路：对每个像素自适应查找C个最近邻候选码字，提取所有候选共享的bit作为可靠bit，与bit-wise预测融合
    - 设计动机：code-wise标签分类正确时可纠正个别bit错误，但分类错误时引入大噪声；bit-wise更软但可能不一致。混合取长补短
    - 融合公式：$\mathbf{c}^i_{hyb} = \mathcal{M}^i \odot \mathbf{c}^i_{code} + (1-\mathcal{M}^i) \odot \mathbf{c}^i_{bit}$

### 损失函数 / 训练策略

- **BCE损失**：独立优化每个bit的二分类
- **Pixel-code距离损失**：$\mathcal{L}_{pcd} = 1 - \cos(\hat{\mathbf{p}}^i, \hat{\mathbf{c}}^i)$，增强类内紧凑性
- **Pixel-code对比损失**：仅在码字差异部分(distinctive bits)计算对比学习，增强类间分离
- 总损失：$\mathcal{L}_{total} = \mathcal{L}_{bce} + \lambda_1 \mathcal{L}_{pcd} + \lambda_2 \mathcal{L}_{pcc}$
- 理论保证：在最小码距足够大时，ECOC比one-hot有更紧的分类错误上界（Theorem 4.2）

## 实验关键数据

### 主实验（表格）

| 方法 | 架构 | GTA→CS mIoU | SYN→CS mIoU |
|------|------|-------------|-------------|
| CDAC (baseline) | Transformer | 76.0 | - |
| +ECOCSeg | Transformer | **77.3** (+1.3) | - |
| MIC (baseline) | Transformer | 75.9 | 67.3 |
| +ECOCSeg | Transformer | **77.0** (+1.1) | **68.7** (+1.4) |
| UniMatch (SSL) | CNN | 76.6 (1/16) | - |
| +ECOCSeg | CNN | **77.5** (+0.9) | - |

### 消融实验

- 码本设计：max-min距离编码和text-based编码性能相当，前者略优
- 伪标签形式：hybrid > code-wise > bit-wise > one-hot
- 优化准则：BCE + PCD + PCC三者联合效果最佳
- 码长K=64时在多数设置下取得最佳平衡

### 关键发现

- ECOC编码在伪标签噪声下的校准性(ECE)显著优于one-hot
- 在GTAv→CS上将SOTA从76.0提升至77.3 mIoU
- 作为即插即用模块，在多个UDA和SSL基准上均带来一致提升
- 理论证明ECOC在最小码距满足条件时，错误率上界严格低于one-hot

## 亮点与洞察

- **视角新颖**：首次从编码形式角度分析伪标签噪声，提供与现有方法正交的新方向
- **即插即用**：可无缝集成到self-training和consistency regularization等主流框架
- **理论扎实**：基于NTK分析了ECOC在全监督和伪标签设置下的性能保证
- 核心启发：混淆类共享视觉属性，即使分错也能保留部分正确的属性信息

## 局限性 / 可改进方向

- 性能提升幅度有限(~1-2 mIoU)，但方向正交可与其他方法叠加
- 码本构建是静态的，未能随训练动态调整码字分配
- 码长K的选择需要与类别数匹配，过短纠错不足，过长计算开销增加
- 未探索与负学习等其他伪标签去噪方法的组合效果

## 相关工作与启发

- 与标签平滑的区别：ECOC提供结构化的软编码而非简单概率平滑
- 与multi-label分类的联系：ECOC将多类转化为多二分类，但有纠错码的数学保证
- 可启发其他需要伪标签的任务（如目标检测、实例分割）采用类似编码策略

## 评分

⭐⭐⭐⭐ — 视角独到，理论扎实，即插即用设计优秀，但绝对性能提升相对有限
