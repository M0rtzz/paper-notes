---
description: "【论文笔记】Fast Data Attribution for Text-to-Image Models 论文解读 | NeurIPS 2025 | arXiv 2511.10721 | data attribution | 将慢而准确的 unlearning-based 数据归因方法蒸馏为一个可快速检索的特征嵌入空间，在 Stable Diffusion 级别模型上实现比现有方法快 2,500× ~ 400,000× 的数据归因。"
tags:
  - NeurIPS 2025
  - 知识蒸馏
---

# Fast Data Attribution for Text-to-Image Models

**会议**: NeurIPS 2025  
**arXiv**: [2511.10721](https://arxiv.org/abs/2511.10721)  
**代码**: [FastGDA](https://peterwang512.github.io/FastGDA)  
**领域**: image_generation  
**关键词**: data attribution, text-to-image, learning-to-rank, knowledge distillation, efficient retrieval  

## 一句话总结

将慢而准确的 unlearning-based 数据归因方法蒸馏为一个可快速检索的特征嵌入空间，在 Stable Diffusion 级别模型上实现比现有方法快 2,500× ~ 400,000× 的数据归因。

## 研究动机

数据归因（Data Attribution）旨在找出对文本到图像模型生成结果影响最大的训练图像。现有方法面临严重的效率瓶颈：

- **影响函数方法**（如 TRAK、D-TRAK）需要存储大量梯度数据（数十到数百 GB），且运行时间以分钟计
- **Unlearning 方法**（如 AbU）准确但单次查询需 2+ 小时
- 文本到图像平台生成一张图仅需几美分，但归因计算成本可能高出数量级
- 实际部署要求毫秒级响应，现有方法完全无法满足

## 方法详解

### 核心思想：蒸馏归因到特征空间

将 Attribution by Unlearning (AbU) 的精确归因结果作为教师信号，训练特征嵌入网络作为学生，使得简单的余弦相似度检索就能近似昂贵的归因排序。

### Attribution by Unlearning (AbU/AbU+)

对预训练模型 $\theta_0$ 执行 certified unlearning：

$$\theta_{-\hat{\mathbf{z}}} = \theta_0 + \frac{\alpha}{N} F^{-1} \nabla \mathcal{L}(\hat{\mathbf{z}}, \theta)$$

其中 $F$ 为 Fisher 信息矩阵，$\alpha$ 为步长。对每个训练样本 $\mathbf{z}$ 计算归因分数：

$$\tau(\hat{\mathbf{z}}, \mathbf{z}) = \mathcal{L}(\mathbf{z}, \theta_{-\hat{\mathbf{z}}}) - \mathcal{L}(\mathbf{z}, \theta_0)$$

**AbU+ 改进**：将 Fisher 矩阵的对角近似替换为 EK-FAC（Eigenvalue-corrected Kronecker Factorization）近似，性能更优。

### 两阶段数据收集

直接对所有训练样本计算归因分数计算量过大，因此采用两阶段策略：

1. 使用现成特征（DINO）检索每个查询的 $K$ 近邻子集 $\mathcal{D}_{\hat{\mathbf{z}}}$
2. 只对近邻子集计算 AbU+ 归因分数 $\mathcal{S}_{\hat{\mathbf{z}}}$

### Learning-to-Rank 目标

学习特征嵌入 $f_\psi = g_\psi \circ \phi$（预训练网络 $\phi$ + MLP $g_\psi$），通过余弦相似度预测归因排名：

$$r_\psi(\hat{\mathbf{z}}, \mathbf{z}_i) = \cos(f_\psi(\hat{\mathbf{z}}), f_\psi(\mathbf{z}_i))$$

使用 BCE 损失训练：

$$\mathcal{L}(\psi, \alpha, \beta) = \mathbb{E}_{\hat{\mathbf{z}} \sim \hat{\mathcal{Z}}, \mathbf{z}_i \sim \mathcal{D}_{\hat{\mathbf{z}}}} \ell_{\text{BCE}}\left(\pi_{\hat{\mathbf{z}}}^i, \sigma_{\alpha,\beta}(r_\psi(\hat{\mathbf{z}}, \mathbf{z}_i))\right)$$

其中 $\pi_{\hat{\mathbf{z}}}^i \in [\frac{1}{K}, \frac{2}{K}, \ldots, 1]$ 为归一化排名标签，$\sigma_{\alpha,\beta}(x) = \frac{1}{1+e^{-(\alpha x + \beta)}}$ 为带学习仿射缩放的 logit 函数。

### 采样策略

- **负样本注入**：以 0.1 概率从非近邻集合采样并赋予最差排名，防止模型忽略无关图像
- **子采样近邻**：每次迭代只用 $M \approx 0.1K$ 候选项训练，大幅降低数据收集成本

## 实验结果

### MSCOCO 反事实评估（Leave-K-Out）

| 方法 | 延迟 | 存储 | ΔL (k=500) | ΔL (k=4000) | MSE↑ (k=500) |
|------|------|------|------------|------------|-------------|
| AbU+ | 2.28 hr | 1.9 GB | **5.83** | **10.70** | 5.64 |
| D-TRAK | 46.7 s | 30 GB | 5.44 | 9.59 | **5.86** |
| DINO | 11.6 ms | 354 MB | 4.76 | 8.06 | 4.51 |
| **Ours** | **18.7 ms** | **354 MB** | **5.28** | **9.35** | 4.78 |

- 本方法在快速方法（<生成时间 21.5s）中**归因性能最优**
- 比影响函数方法快 2,500×，比 unlearning 方法快 400,000×
- 存储仅需 354 MB，远小于训练集 19 GB

### 特征空间分析

- Tuning 前：文本嵌入（CLIP-Text）优于图像嵌入
- Tuning 后：图像嵌入（DINO）反超文本嵌入
- 最佳组合：**DINO + CLIP-Text**，融合视觉和文本信号

### Stable Diffusion 规模实验

- 在 LAION-400M 训练集上成功验证可扩展性
- Tuning 后特征在所有 mAP 阈值上显著提升
- 文本特征对 SD 模型归因尤为关键（与 MSCOCO 结论不同）

## 评价

⭐⭐⭐⭐

**优点**：
- 首次将数据归因扩展到 Stable Diffusion + LAION-400M 规模，具有实际部署价值
- 蒸馏 + 检索的思路优雅，保留精确方法的归因能力同时获得毫秒级速度
- 系统性研究了特征选择、损失函数、数据规模等关键设计选择
- AbU+ 改进（EK-FAC 替代对角近似）本身也是有价值的贡献

**局限**：
- 蒸馏只保留排名信息，丢失影响力的绝对度和集中/分散程度
- 教师方法的失败模式会被继承
- 需要大量 GPU 时间收集归因训练数据（50M 排名对）
- 价值: 待评
