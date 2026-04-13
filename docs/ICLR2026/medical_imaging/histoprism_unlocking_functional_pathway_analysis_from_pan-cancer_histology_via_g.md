---
title: >-
  [论文解读] HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction
description: >-
  [ICLR 2026][医学图像][基因表达预测] 提出HistoPrism高效Transformer架构从H&E病理图像预测泛癌基因表达，并引入基因通路一致性(GPC)基准（50个Hallmark+87个GO通路）将评估从单基因方差升级到功能通路级别，在通路预测上大幅超越SOTA且参数效率更高。
tags:
  - ICLR 2026
  - 医学图像
  - 基因表达预测
  - 通路分析
  - 泛癌
  - Transformer
  - 空间转录组
---

# HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction

**会议**: ICLR 2026  
**arXiv**: [2601.21560](https://arxiv.org/abs/2601.21560)

**代码**: [GitHub](https://github.com/susuhu/HistoPrism)

**领域**: 计算病理学  
**关键词**: 基因表达预测, 通路分析, 泛癌, Transformer, 空间转录组

## 一句话总结

提出HistoPrism高效Transformer架构从H&E病理图像预测泛癌基因表达，并引入基因通路一致性(GPC)基准（50个Hallmark+87个GO通路）将评估从单基因方差升级到功能通路级别，在通路预测上大幅超越SOTA且参数效率更高。

## 研究背景与动机

**领域现状**：从H&E切片预测空间基因表达是低成本替代测序的方向。现有方法（BLEEP/TRIPLEX/STEM/STPath）要么限于单癌种、要么评估仅看高变异基因(HVG)的Pearson相关。

**现有痛点**：(1) HVG评估忽略了基因间的功能协调——单基因好不等于通路级别好；(2) 多数方法受限于单癌种训练→泛化差；(3) STPath虽然泛癌但依赖基因-基因相关性假设+参数量巨大。

**切入角度**：提出GPC基准——在50个Hallmark+87个GO通路上评估功能一致性→比HVG更接近临床意义。

## 方法详解

### HistoPrism架构

1. **泛癌条件化Cross-Attention**：将癌种one-hot编码投射为嵌入→作为K/V与图像patch特征(Query)做cross-attention→使模型学习癌种特异模式

2. **Transformer编码器**：捕捉patch间短/长距离空间依赖→建模组织级结构

3. **MLP回归头**：每个patch潜表示→基因表达向量

### GPC基准构建

1. 从MSigDB(Hallmark)和GO(BP/CC/MF)收集通路

2. 筛选50-100基因的通路→避免太小(噪声)或太大(无信息)

3. Jaccard相似度>0.1的通路去重→最终50+87=137个非冗余通路

4. 通路分数 = 通路内所有基因在所有WSI上的平均Pearson相关

## 实验关键数据

### HVG + GPC评估

| 方法 | HVG相关 | GPC(Hallmark) | GPC(GO) | 参数量 |
|------|---------|-------------|---------|--------|
| BLEEP | 中 | 低 | 低 | 中 |
| STPath | 好 | 中 | 中 | **巨大** |
| **HistoPrism** | **最优** | **最优** | **最优** | **小** |

### 关键发现

- HistoPrism在HVG和GPC上都达到SOTA→不是牺牲一个指标换另一个

- 通路级评估揭示了之前被掩盖的模型差距——HVG接近的模型在GPC上差距很大

- 泛癌条件化(cross-attention)对跨癌种泛化至关重要

- 模型参数量显著小于STPath→更适合实际部署

## 亮点与洞察

- **GPC基准的贡献可能比模型本身更大**：从单基因方差到功能通路的评估升级，让"什么是好的基因表达预测"有了生物学意义上的答案。

- **简洁高效的架构**：不用对比学习/扩散/masked预训练→直接回归+泛癌条件化→简单但有效。

- **泛癌条件化的必要性**：不同癌种的形态-表达关系不同→条件化使同一模型适配多癌种。

## 局限性 / 可改进方向

- GPC的137个通路可能未覆盖所有重要生物学过程

- 仅用MSE回归训练→生成式方法(STEM等)可能捕捉更多不确定性

- 跨ST平台泛化性未测试


## 相关工作与启发

- **vs BLEEP**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs GraphST**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs TRIPLEX**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs STPath**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐ GPC基准的提出是重要评估方法贡献


- 实验充分度: ⭐⭐⭐⭐ HVG+GPC双评估+多SOTA对比


- 写作质量: ⭐⭐⭐⭐ 动机清晰，GPC构建过程严谨


- 价值: ⭐⭐⭐⭐⭐ 对计算病理学的评估范式有推动作用

