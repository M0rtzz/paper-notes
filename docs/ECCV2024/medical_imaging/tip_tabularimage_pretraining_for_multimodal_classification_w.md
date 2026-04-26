---
title: >-
  [论文解读] TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data
description: >-
  [ECCV 2024][医学图像][表格-图像预训练] 提出TIP框架，通过掩码表格重建、图像-表格匹配和对比学习三个自监督任务，在表格数据不完整的条件下学习鲁棒的多模态表示，在自然图像和医学图像分类任务上超越现有方法。
tags:
  - ECCV 2024
  - 医学图像
  - 表格-图像预训练
  - 多模态分类
  - 数据缺失
  - 自监督学习
  - 异构数据
---

# TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data

**会议**: ECCV 2024  
**arXiv**: [2407.07582](https://arxiv.org/abs/2407.07582)  
**代码**: https://github.com/siyi-wind/TIP (有)  
**领域**: 多模态VLM  
**关键词**: 表格-图像预训练, 多模态分类, 数据缺失, 自监督学习, 异构数据

## 一句话总结
提出TIP框架，通过掩码表格重建、图像-表格匹配和对比学习三个自监督任务，在表格数据不完整的条件下学习鲁棒的多模态表示，在自然图像和医学图像分类任务上超越现有方法。

## 研究背景与动机
1. **领域现状**：现实数据库中图像和结构化表格是核心两大模态，表格-图像联合学习可以挖掘新的洞察（如医学影像+电子病历），但当前多模态方法主要关注图像-文本或图像-图像对。
2. **现有痛点**：(1) 表格数据天然异构（数值+类别，维度不一），与图像存在巨大的模态鸿沟；(2) 现实场景中表格数据频繁缺失（传感器故障、患者隐私等），现有方法假设数据完整无法应对；(3) 早期工作仅用简单的模态融合策略（late fusion、concat），不能有效捕捉跨模态交互。
3. **核心矛盾**：表格数据的异构性和不完整性使得标准对齐方法（如CLIP式对比学习）难以直接应用，需要同时解决"如何编码异构不完整表格"和"如何与图像对齐"两个问题。
4. **本文要解决什么？** (1) 设计适配异构不完整表格的编码器；(2) 设计对缺失数据鲁棒的预训练目标；(3) 学习可迁移的表格-图像联合表示。
5. **切入角度**：从自监督预训练出发，结合掩码重建（学缺失恢复能力）和跨模态对齐（学模态关联）。
6. **核心idea一句话**：通过掩码表格重建任务赋予模型数据缺失鲁棒性，配合图像-表格匹配和对比学习实现跨模态对齐。

## 方法详解

### 整体框架
TIP由图像编码器 $\phi^i$、表格编码器 $\phi^t$、跨模态交互模块 $\psi$、投影头 $g^i, g^t$ 和任务头 $h^{itm}, h^{mtr}$ 组成。预训练阶段通过三个自监督任务联合优化：图像-表格对比学习（ITC）、图像-表格匹配（ITM）、掩码表格重建（MTR）。

### 关键设计

1. **异构表格编码器**：
    - 做什么：将包含数值和类别特征、可能有缺失的表格数据编码为统一表示
    - 核心思路：每个表格特征（列）独立tokenize后拼接，数值特征通过线性映射，类别特征通过embedding层，缺失位置用可学习的mask token替代
    - 设计动机：传统方法无法处理不同类型特征共存和缺失问题，token化设计允许灵活处理

2. **掩码表格重建（MTR）任务**：
    - 做什么：随机掩码一定比例 $\rho$ 的表格特征，让模型在图像辅助下重建缺失值
    - 核心思路：将掩码表格 $\tilde{X}^t$ 与图像特征通过交互模块 $\psi$ 融合后，由重建头 $h^{mtr}$ 预测被掩码位置的原始值
    - 设计动机：(1) 赋予模型在测试时处理自然缺失的能力；(2) 利用图像信息填补表格缺失，强制学习跨模态互补

3. **图像-表格匹配（ITM）+ Hard Negative Mining**：
    - 做什么：判断图像-表格对是否匹配，并使用hard negative增加任务难度
    - 核心思路：对每个正样本对，从batch内选择对比学习相似度最高的非匹配样本作为hard negative，由匹配头 $h^{itm}$ 做二分类
    - 设计动机：简单的随机负样本太容易区分，hard negative mining确保模型学到更细粒度的匹配模式

4. **图像-表格对比学习（ITC）**：
    - 做什么：在共享嵌入空间中拉近匹配对、推远不匹配对
    - 核心思路：用投影头 $g^i, g^t$ 将图像/表格特征映射到同一空间做InfoNCE对比
    - 设计动机：建立模态间的粗粒度对齐，为ITM和MTR提供基础

### 损失函数 / 训练策略
总损失 $\mathcal{L} = \frac{1}{3}(\mathcal{L}_{itc} + \mathcal{L}_{itm} + \mathcal{L}_{mtr})$，三个任务等权联合训练。预训练后冻结编码器，在下游分类任务上微调。

## 实验关键数据

### 主实验
在DVM Car（自然图像+车辆属性表格）和医学影像数据集上验证：

| 数据集 | 方法 | 完整数据准确率 | 50%缺失准确率 | 说明 |
|--------|------|---------------|--------------|------|
| DVM Car | 图像 Supervised | ~82% | ~82% | 无表格 |
| DVM Car | Late Fusion | ~85% | ~78% | 缺失时大幅下降 |
| DVM Car | TIP (Ours) | **~88%** | **~85%** | 缺失下仍保持高性能 |

### 消融实验

| 配置 | 准确率 | 说明 |
|------|--------|------|
| ITC only | 基线 | 仅对比学习 |
| ITC + ITM | +1.2% | 加入匹配任务提升跨模态理解 |
| ITC + ITM + MTR | +2.5% | 掩码重建显著提升鲁棒性 |
| w/o Hard Negative | -0.8% | hard negative mining比随机负样本更有效 |

### 关键发现
- 在数据完整场景下TIP就已超越有监督和其他SSL方法，说明预训练目标设计的有效性
- 在50%特征缺失场景下TIP性能相对保持最好，验证MTR任务赋予的缺失鲁棒性
- 图像模态在表格高度缺失时提供了关键补充信息
- 预训练表示在不同缺失率下具有良好的泛化性

## 亮点与洞察
- **填补了表格-图像多模态预训练的空白**：大量工作关注图像-文本预训练，TIP将类似思路迁移到表格-图像场景，设计了针对性的编码器和预训练任务。
- **MTR任务设计巧妙**：通过掩码训练自然获得缺失鲁棒性，同时利用图像辅助重建强化跨模态交互——一个任务同时解决两个问题。
- **实用性强**：医学场景中表格缺失极为常见（检查未做、数据丢失），这一方法可直接应用于临床决策辅助。

## 局限性 / 可改进方向
- 表格编码器相对简单，可探索更强的表格基础模型（如TabNet、FT-Transformer）
- 仅验证了分类任务，未测试回归、检索等下游场景
- 缺失模式假设为随机缺失（MCAR），实际可能是非随机缺失（MNAR）
- 未探索图像缺失的场景（仅处理了表格缺失）

## 相关工作与启发
- **vs CLIP/BLIP**：这些方法针对图像-文本对，无法处理异构表格数据的token化和缺失问题。TIP的编码器设计可视为表格领域的"tokenizer"。
- **vs ShaSpec/ActionMAE**：这些处理缺失模态的方法生成伪特征但不考虑跨模态重建，TIP的MTR直接利用另一模态辅助。
- **vs 传统多模态融合**：Late/Early fusion不能处理缺失，TIP通过预训练获得了鲁棒的联合表示。

## 补充说明
- 支持不同缺失率（0%~80%）的鲁棒评估
- 三个预训练任务等权联合训练($\frac{1}{3}$)，简单但有效
- 表格编码器对数值和类别特征采用不同的tokenization策略
- 可以扩展到更多模态（如时序数据+图像+表格）

## 评分
- 新颖性: ⭐⭐⭐⭐ 首个针对表格-图像不完整数据的预训练框架，问题定义新颖
- 实验充分度: ⭐⭐⭐ 数据集不算多，消融较简单，但自然+医学场景验证较好
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰，动机合理
- 价值: ⭐⭐⭐⭐ 对医学、金融等表格密集领域有实际应用价值

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification](pathology-knowledge_enhanced_multi-instance_prompt_learning_for_few-shot_whole_s.md)
- [\[ECCV 2024\] I-MedSAM: Implicit Medical Image Segmentation with Segment Anything](i-medsam_implicit_medical_image_segmentation_with_segment_anything.md)
- [\[ECCV 2024\] Adaptive Correspondence Scoring for Unsupervised Medical Image Registration](adaptive_correspondence_scoring_for_unsupervised_medical_ima.md)
- [\[ECCV 2024\] Is User Feedback Always Informative? Retrieval Latent Defending for Semi-Supervised Domain Adaptation without Source Data](is_user_feedback_always_informative_retrieval_latent_defending_for_semi-supervis.md)
- [\[ECCV 2024\] Alternate Diverse Teaching for Semi-supervised Medical Image Segmentation](alternate_diverse_teaching_for_semi-supervised_medical_image_segmentation.md)

<!-- RELATED:END -->
