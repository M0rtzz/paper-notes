---
title: >-
  [论文解读] Understanding and Mitigating Miscalibration in Prompt Tuning for Vision-Language Models
description: >-
  [ICML 2025][多模态][CLIP] 揭示 CLIP prompt tuning 在 base 和 novel 类之间存在校准权衡（CoOp 导致 novel 类过度自信，KgCoOp 导致 base 类自信不足），从文本特征散度视角解释原因，并提出 Dynamic Outlier Regularization (DOR) 通过正则化非训练类文本标签的特征偏差同时保持两端校准。
tags:
  - ICML 2025
  - 多模态
  - CLIP
  - Calibration
  - 提示学习
  - Feature Divergence
  - Outlier Regularization
---

# Understanding and Mitigating Miscalibration in Prompt Tuning for Vision-Language Models

**会议**: ICML 2025  
**arXiv**: [2410.02681](https://arxiv.org/abs/2410.02681)  
**代码**: [github.com/ml-stat-Sustech/Outlier-Calibration](https://github.com/ml-stat-Sustech/Outlier-Calibration)  
**领域**: 视觉语言模型, 置信度校准, Prompt Learning  
**关键词**: CLIP, Calibration, prompt tuning, Feature Divergence, Outlier Regularization

## 一句话总结

揭示 CLIP prompt tuning 在 base 和 novel 类之间存在校准权衡（CoOp 导致 novel 类过度自信，KgCoOp 导致 base 类自信不足），从文本特征散度视角解释原因，并提出 Dynamic Outlier Regularization (DOR) 通过正则化非训练类文本标签的特征偏差同时保持两端校准。

## 研究背景与动机

CLIP 零样本推理具有出色的置信度校准能力，但 fine-tuning 后会破坏这一优势。**safe deployment 要求模型的置信度与实际准确率一致。**

本文首次系统研究了 prompt tuning 对 CLIP 校准的影响，发现：
- **CoOp**（标准 CE 训练）：base 类校准良好，但 novel 类严重过度自信
- **KgCoOp**（正则化训练）：novel 类校准保持，但 base 类自信不足

这形成了一个**base-novel 校准权衡**，现有方法无法同时保证两端。

## 方法详解

### 问题理解：文本特征散度

**Feature Divergence (FD) Score** 定义为文本特征到 $M$ 近邻的平均距离，衡量文本标签在特征空间中的"散开程度"。

**CoOp 过度自信的原因**：
- CE 损失最大化真标签概率 → 拉大所有文本特征间距 → FD 增大
- logit 中置信值（最大值与次大值差距）增大 → softmax 置信度升高
- 在 base 类上与提升的准确率匹配 → 校准良好
- 在 novel 类上准确率未变但置信度升高 → **过度自信**

**KgCoOp 自信不足的原因**：
- 正则化约束了 FD 增长 → 置信度与零样本 CLIP 相当
- 但 fine-tuning 提升了 base 类准确率 → 准确率 > 置信度 → **自信不足**

### Dynamic Outlier Regularization (DOR)

核心思想：**正则化 novel 类文本特征的散度，但不约束 base 类特征**。

**步骤 1：构建文本 outlier 集合**

从 WordNet（>150K 词）中选择与 base 类语义相关但不重叠的名词：

$$s_i = \frac{1}{n}\sum_{j=1}^n \text{sim}(\psi(t_{o_i}), \psi(t_{c_j}))$$

取 Top-K 构成 outlier 集合 $\mathcal{O}_{\text{out}}$。

**步骤 2：DOR 正则化**

每个迭代随机采样一批 outlier，最小化 fine-tuned 与 zero-shot CLIP 的文本特征偏差：

$$\mathcal{L}_{\text{dor}} = 1 - \frac{1}{B}\sum_{b=1}^B \text{sim}(\psi(t'_{o_b}), \psi(t_{o_b}))$$

总损失：$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{ce}} + \lambda \cdot \mathcal{L}_{\text{dor}}$

### DOR 的关键优势

- **Easy-to-use**：文本 outlier 容易获取
- **Algorithm-agnostic**：可与 CoOp、CoCoOp、MaPLe、PromptSRC 等任意方法组合
- **Fine-tuning-nontoxic**：不约束 base 类特征，不与微调目标冲突

## 实验关键数据

### 11 数据集平均 ECE（×10⁻²，越低越好）

| 方法 | Base | Novel | HM |
|------|------|-------|-----|
| ZSCLIP | 3.58 | 4.61 | 4.10 |
| CoOp | 3.07 | 14.58 | 8.82 |
| **CoOp+DOR** | **2.67** | **6.49** | **4.58** |
| MaPLe | 2.75 | 5.46 | 4.11 |
| **MaPLe+DOR** | **2.83** | **4.44** | **3.63** |
| CoCoOp | 3.60 | 6.14 | 4.87 |
| **CoCoOp+DOR** | **4.22** | **4.02** | **4.12** |

### 关键数据

- CoOp+DOR 将 novel 类 ECE 从 14.58% 降至 6.49%（**降 8.09%**）
- DOR 也提升了准确率（base-novel HM 在 CoOp 上从 71.66 到 77.79 不等）
- 在 4 类 ImageNet 协变量偏移数据集上同样有效

### 与正则化方法组合

DOR 与 KgCoOp、TCP、PromptSRC、CoPrompt、PromptKD 组合，在所有方法上一致降低 HM ECE。

## 亮点与洞察

1. **文本散度视角的可解释性分析**：优雅地解释了 CE 和正则化方法校准行为的对称差异
2. **用 outlier 而非 base 类正则化**：巧妙避免了约束 base 类特征的副作用
3. **动态采样**：每 epoch 随机采样不同 outlier，增强鲁棒性
4. **可扩展到视觉微调**：用图像 outlier 替代文本 outlier 同样有效

## 局限性

- WordNet 名词可能不完全覆盖所有 novel 概念空间
- $\lambda$ 和 TopK 超参数需要调优
- 主要验证了分类任务，开放语义任务的泛化性待验证

## 相关工作

- CoOp/CoCoOp（prompt tuning）
- KgCoOp/PromptSRC（正则化 prompt tuning）
- 置信度校准（ECE、Temperature Scaling）
- 零样本 CLIP 校准（Minderer et al.）

## 评分

⭐⭐⭐⭐ — 分析视角新颖（文本散度解释校准权衡），DOR 方法简单优雅且广泛适配。11 数据集 + 4 种 ImageNet 变体的全面实验增强了说服力。
