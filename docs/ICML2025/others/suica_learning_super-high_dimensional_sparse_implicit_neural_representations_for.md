---
title: >-
  [论文解读] SUICA: Learning Super-high Dimensional Sparse Implicit Neural Representations for Spatial Transcriptomics
description: >-
   提出SUICA框架，通过图增强自编码器将超高维零膨胀基因表达映射到紧凑嵌入空间，再用INR进行连续空间建模，实现跨平台ST数据的空间插值、基因插补和去噪。
tags:

---

# SUICA: Learning Super-high Dimensional Sparse Implicit Neural Representations for Spatial Transcriptomics

## 元信息
- **会议**: ICML 2025
- **arXiv**: [2412.01124](https://arxiv.org/abs/2412.01124)
- **代码**: [GitHub](https://github.com/Szym29/SUICA)
- **领域**: 空间转录组学 / 隐式神经表示
- **关键词**: INR, 空间转录组, 图自编码器, 基因表达, 空间插值

## 一句话总结
提出SUICA框架，通过图增强自编码器将超高维零膨胀基因表达映射到紧凑嵌入空间，再用INR进行连续空间建模，实现跨平台ST数据的空间插值、基因插补和去噪。

## 研究背景与动机
- **空间转录组(ST)**：在保留空间信息的同时量化基因表达，但分辨率有限、成本高昂
- **核心挑战**：(1) 基因表达维度超高（>20000维）(2) 零膨胀分布（90%以上为0）(3) 不同平台采样模式差异大
- INR擅长连续建模，但难以扩展到超高维且零膨胀输出

## 方法详解

### 整体流程
1. **Graph Autoencoder (GAE) 预训练**：基于细胞图(k=5 NN)的GCN编码器 + MLP解码器
2. **INR嵌入映射**：空间坐标 $\mathbf{x} \to$ 嵌入 $\mathbf{z}$
3. **解码器微调**：INR固定，微调解码器 $\mathbf{z} \to \mathbf{y}$

### GAE设计
- GCN编码器利用邻域上下文信息，使嵌入结构感知
- 解码器为MLP（插值时无图结构）
- GAE嵌入比普通AE具有更高的Graph Total Variation和更好的特征解耦

### INR嵌入映射
- 空间稀疏ST用SIREN，密集分布用FFN
- 嵌入空间MSE损失：$\mathcal{L}_{\text{embd}} = \frac{1}{|\mathbf{M}_\mathbf{z}|}\sum(\hat{\mathbf{z}} - \mathbf{z}_{\text{gt}})^2$

### 零膨胀处理——回归即分类
采用Dice Loss强制稀疏性：
$$\mathcal{L}_{\text{dice}} = 1 - \frac{2\sum(\tanh(\hat{\mathbf{y}}) \circ \text{sgn}(\mathbf{y}_{\text{gt}})) + \epsilon}{\sum\tanh(\hat{\mathbf{y}}) + \sum\text{sgn}(\mathbf{y}_{\text{gt}}) + \epsilon}$$

总重建损失：非零MSE + 全局MAE + Dice Loss

## 实验

### 空间插值（20%测试集）
| 方法 | MAE↓ | MSE↓ | Cosine↑ | ARI↑ |
|------|------|------|---------|------|
| FFN | 6.51 | 1.20 | 0.706 | 0.143 |
| SIREN | 7.21 | 1.31 | 0.661 | 0.289 |
| STAGE | 6.52 | 1.11 | 0.732 | 0.139 |
| **SUICA** | **5.66** | **0.85** | **0.797** | **0.343** |

SUICA在所有指标上优于基线，ARI甚至超过真值(0.312)，说明插补增强了生物信号。

### 基因插补和去噪
SUICA在MOSTA数据集上也优于对比方法，证明了方法的通用性。

## 亮点
- 首次将INR扩展到超高维（>20000通道）零膨胀数据
- GAE嵌入空间巧妙解决维度与稀疏性双重挑战
- Dice Loss的回归即分类思想适配零膨胀分布
- 跨多个ST平台（Stereo-seq、Slide-seqV2、Visium、MERFISH）统一框架
- 生物学验证：标记基因表达预测与已知生物学知识一致

## 局限性
- 依赖k-NN图构建，对极稀疏采样可能不稳定
- GAE预训练+INR训练+解码器微调三阶段流程较复杂
- 未与基于组织学图像的分辨率增强方法（如Hist2ST）比较
- 嵌入维度选择对性能影响未充分消融

## 评分
⭐⭐⭐⭐ 技术方案巧妙地解决了INR在生物信息学中的关键挑战，跨平台通用性和生物学一致性令人印象深刻。
