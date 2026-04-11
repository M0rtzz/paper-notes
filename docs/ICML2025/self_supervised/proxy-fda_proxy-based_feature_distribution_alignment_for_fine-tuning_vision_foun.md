---
description: "【论文笔记】Proxy-FDA: Proxy-based Feature Distribution Alignment for Fine-tuning Vision Foundation Models without Forgetting 论文解读 | ICML2025 | arXiv 2505.24088 | 鲁棒微调 | 提出 Proxy-FDA，通过基于最近邻图的特征分布对齐（FDA）和动态生成的代理特征（Proxy），在微调视觉基础模型时显式保留特征邻域结构中的丰富知识，大幅减少概念遗忘。"
tags:
  - ICML2025
---

# Proxy-FDA: Proxy-based Feature Distribution Alignment for Fine-tuning Vision Foundation Models without Forgetting

**会议**: ICML2025  
**arXiv**: [2505.24088](https://arxiv.org/abs/2505.24088)  
**代码**: 待确认  
**领域**: self_supervised  
**关键词**: 鲁棒微调, 概念遗忘, 特征分布对齐, 代理学习, 视觉基础模型

## 一句话总结

提出 Proxy-FDA，通过基于最近邻图的特征分布对齐（FDA）和动态生成的代理特征（Proxy），在微调视觉基础模型时显式保留特征邻域结构中的丰富知识，大幅减少概念遗忘。

## 研究背景与动机

- **概念遗忘问题**：CLIP/DINOv2 等基础模型微调后会丧失对其他任务概念的识别能力
- **现有方法局限**：L2SP（权重空间正则）和 LDIFS（特征逐点匹配）仅做点对点约束，未考虑特征邻域结构
- **核心洞察**：特征局部邻域编码了超越类别标签的丰富知识（如颜色、纹理等视觉属性），逐点匹配不足以保留这些结构性信息
- **本文主张**：需要结构级正则化来保留特征分布的局部拓扑关系
- **关键观察**：OTDD（最优传输数据集距离）与遗忘的相关性远强于 L2 距离

## 方法详解

### 总体损失

$$\mathcal{L}=\frac{1}{B}\sum_{i=1}^B(\mathcal{L}_{task}^i+\lambda\mathcal{L}_{FDA}^i)$$

### Feature Distribution Alignment (FDA)

1. **构建最近邻图**：用预训练模型特征 $\hat{X}$ 的 kNN 关系定义正集 $X_i^+$ 和负集 $X_i^-$
2. **图迁移**：将预训练特征邻域索引和相似度迁移到微调特征空间
3. **Sigmoid 对比损失**：$\mathcal{L}_{FDA}^i=\frac{1}{|X|-1}\sum_{j\neq i}\log(1+e^{w_{ij}(-\cos(x_i,x_j)/\tau+b)})$

### Proxy-FDA（代理增强）

- **动机**：下游数据有限时 FDA 覆盖不足
- **代理生成器**：轻量网络（23.6K 参数），生成代理 $P_i^+$ 和 $P_i^-$
- **代理损失**：约束代理落在真实特征流形上 + 方差损失鼓励多样性
- **最终损失**：代理拼接到真实特征集扩大 FDA 覆盖
- **可视化分析**：代理能合成当前 batch 中未出现的概念（如未见类的颜色/纹理属性）
- **在线学习**：代理生成器与主模型联合训练，确保代理始终适配当前特征分布

### Batch 构建

- 类均衡采样（$m=16$ 类，$n=4$），hard class mining，$K>n$
- Hard class mining：预计算预训练特征的类间相似度矩阵，优先选择相似类构造 batch
- $K>n$ 保证邻域跨越多类，FDA 传递跨类知识而非仅类内知识

## 实验关键数据

### End-to-end 微调（CLIP ViT-B/32，10数据集）

| 方法 | 平均 $\mathcal{A}_{LP}$ | 平均 $\Delta_{LP}\uparrow$ |
|---|---|---|
| Naive FT | 91.90 | -4.37 |
| LDIFS | 91.66 | +0.86 |
| FDA | 91.86 | +1.39 |
| **Proxy-FDA** | 91.82 | **+1.54** |

- 所有 10 个微调任务实现正向迁移
- OTDD 与遗忘的相关性 > L2 距离 → 结构对齐更有效
- 跨架构有效：CLIP/FLAVA/DINOv2/MAE 四种预训练方法均有效
- Few-shot/continual/captioning/VQA 任务均有效
- 微调时间增加仅 17-21%，推理无任何额外开销
- 计算开销分析：FDA 增加 7-9%，Proxy-FDA 增加 17-21%

## 亮点与洞察

1. **结构级 vs 点级正则**：邻域结构保留远优于逐点匹配
2. **代理用于分布增强**而非样本替代，合成未见概念
3. **OTDD 指标**与遗忘强相关
4. 计算效率高（23.6K 参数代理）

## 局限性 / 可改进方向

- kNN 图质量依赖 batch 构建策略，对极端类不平衡场景可能退化
- 代理仅从当前 batch 生成，未利用外部数据
- 大规模模型效果需验证
- 邻域大小 K 和类数 m 的超参数需要针对不同数据集调整

## 相关工作与启发

- Mukhoti et al. (2024) LDIFS：点级特征正则
- Park et al. (2019) RKD：关系知识蒸馏
- Proxy 学习源自度量学习但用法不同
- Alvarez-Melis & Fusi (2020) OTDD：最优传输数据集距离
- Zhai et al. (2023) SigLIP：Sigmoid 损失函数来源

## 评分

⭐⭐⭐⭐ — 结构级特征对齐思路新颖有效，对鲁棒微调有实操价值，OTDD相关性分析有洞察力

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
