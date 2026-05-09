---
title: >-
  [论文解读] Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification
description: >-
  [ECCV 2024][医学图像][病理图像分析] 提出 PEMP——病理知识增强的多实例提示学习框架，将视觉和文本病理先验（典型 patch/slide 示例 + 语言描述）注入 CLIP 的提示中，在 patch 和 slide 两个层级进行对比学习，显著提升少样本全切片图像（WSI）分类性能。
tags:
  - ECCV 2024
  - 医学图像
  - 病理图像分析
  - 提示学习
  - 多实例学习
  - 少样本分类
  - CLIP
---

# Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification

**会议**: ECCV 2024  
**arXiv**: [2407.10814](https://arxiv.org/abs/2407.10814)  
**代码**: 暂无  
**领域**: 医学图像  
**关键词**: 病理图像分析, 提示学习, 多实例学习, 少样本分类, CLIP

## 一句话总结

提出 PEMP——病理知识增强的多实例提示学习框架，将视觉和文本病理先验（典型 patch/slide 示例 + 语言描述）注入 CLIP 的提示中，在 patch 和 slide 两个层级进行对比学习，显著提升少样本全切片图像（WSI）分类性能。

## 研究背景与动机

- **WSI 分类的数据稀缺困境**：
    - 病理切片获取受限于患者隐私、罕见疾病发生率
    - 现有 MIL 方法需要大量切片训练，在少样本场景下表现不佳
- **Few-shot Weakly Supervised WSI Classification (FSWC)**：
    - 仅有 2/4/8/16/32 张带标签切片用于训练
    - 每张切片包含数千个 patch，patch 级标签未知
- **现有提示学习方法的不足**：
    - MI-Zero/PLIP 仅关注 patch 级文本提示
    - CoOp 等通用方法不理解病理专业术语
    - TOP 引入了语言描述但缺乏视觉侧的任务特定知识
- **核心灵感**：模拟病理医生从教科书学习——同时接触典型病理图像和对应文字描述

## 方法详解

### 整体框架

PEMP = 视觉提示学习（patch+slide 级视觉示例 + 可学习提示）+ 文本提示学习（任务描述 + slide/patch 病理描述 + 可学习提示）+ 双层对比对齐

### 关键设计

**1. 视觉提示学习**
- 构建**视觉 patch 示例**：由病理专家从权威来源选取典型 patch（如"血管侵犯"、"高级别不典型增生"、"坏死"等）
- 构建**视觉 slide 示例**：如"浸润型模糊瘤界+低肿瘤间质比" vs "推挤型清晰瘤界+高肿瘤间质比"
- 固定示例特征与当前 patch 特征拼接 → Messenger Layer（自注意力）建模 patch 间关系 → Summary Layer（注意力池化）聚合为 slide 特征
- 额外引入可学习 slide 级提示 $F_i^P$

**2. 文本提示学习**
- **Slide task [Token]**："A Whole Slide Image of cervical cancer with a [poor/good] prognosis" + 可学习向量
- **Slide-level descriptive [Token]**：slide 级病理描述（如"模糊的肿瘤边界"）+ 可学习向量
- **Patch-level descriptive [Token]**：patch 级特征描述（如"血管淋巴管侵犯"）+ 可学习向量
- 语言描述由病理专家提供，避免晦涩术语

**3. 双层对比对齐**
- $\mathcal{L}_{total} = \mathcal{L}_t + \lambda_1 \mathcal{L}_s + \lambda_2 \mathcal{L}_p$
- $\mathcal{L}_t$：slide 视觉特征 ↔ slide 文本特征（主分类）
- $\mathcal{L}_s$：slide 视觉示例 ↔ slide 病理描述（slide 级对齐）
- $\mathcal{L}_p$：patch 视觉示例 ↔ patch 病理描述（patch 级对齐）

### 损失函数 / 训练策略

- 所有损失均为对比学习形式的负对数似然
- CLIP 编码器参数完全冻结
- 仅训练：可学习提示向量、Messenger Layer、Summary Layer、Projector
- 5 次独立实验取平均

## 实验关键数据

### 主实验（宫颈癌预后预测 C-index）

| 方法 | 32-shot | 16-shot | 8-shot | 4-shot | 2-shot |
|------|---------|---------|--------|--------|--------|
| LinearProbe | 0.620 | 0.562 | 0.543 | 0.501 | 0.458 |
| CoOp | 0.641 | 0.594 | 0.561 | 0.517 | 0.490 |
| TOP | 0.652 | 0.608 | 0.574 | 0.539 | 0.508 |
| **PEMP** | **0.667** | **0.637** | **0.614** | **0.587** | **0.562** |

### 圆细胞亚型诊断（AUC）

| 方法 | 32-shot | 16-shot | 8-shot | 4-shot | 2-shot |
|------|---------|---------|--------|--------|--------|
| TOP | 0.682 | 0.652 | 0.633 | 0.584 | 0.560 |
| **PEMP** | **0.751** | **0.718** | **0.685** | **0.643** | **0.625** |

平均超越 TOP 约 6.2% AUC（罕见肿瘤诊断）

### 关键发现

- PEMP 在所有三个临床任务的所有 shot 设置下均达最优，平均超越对比方法 4%
- **极少样本场景优势更大**（2-shot/4-shot 提升尤其显著）
- 消融：去掉视觉示例（w/o vision em.）→ 性能下降明显；去掉 Summary Layer → 退化最严重
- TCGA 公开数据集验证：使用相同的 prompt，无数据泄露，仍保持优势

## 亮点与洞察

1. **病理知识注入方式很巧妙**：用"典型病例图+简单语言描述"而非复杂术语，降低了 VLM 理解门槛
2. **双层（patch+slide）提示设计**完整覆盖了 WSI 从局部到全局的分析需求
3. Messenger Layer + Summary Layer 提供了轻量级的 patch-to-slide 聚合方案
4. 在罕见肿瘤诊断（数据极度稀缺）场景中展现出最大价值

## 局限性 / 可改进方向

- 视觉示例需要病理专家手动选取，自动化程度有限
- 仅在宫颈癌和圆细胞肿瘤上验证，需更多肿瘤类型验证通用性
- 依赖 CLIP 骨干，而 CLIP 在病理域的预训练可能不充分
- 未与 CONCH 等最新病理 VLM 进行对比

## 相关工作与启发

- TOP 开创了 WSI 提示学习方向，PEMP 在视觉侧补充了先验知识
- CoOp/KgCoOp 的可学习提示机制被有效整合
- 可启发：将视觉示例注入思路推广到放射科（CT/MRI）和眼底影像分析

## 评分

- 新颖性：⭐⭐⭐⭐（病理知识增强提示的完整设计）
- 技术深度：⭐⭐⭐⭐
- 实验充分度：⭐⭐⭐⭐（3 个临床任务 + 公开数据集验证）
- 写作质量：⭐⭐⭐⭐
- 综合推荐：⭐⭐⭐⭐

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Improving Medical Multi-modal Contrastive Learning with Expert Annotations](improving_medical_multimodal_contrastive_learning_with_exper.md)
- [\[ECCV 2024\] AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection](adaclip_adapting_clip_with_hybrid_learnable_prompts_for_zero.md)
- [\[ICLR 2026\] Exploiting Low-Dimensional Manifold of Features for Few-Shot Whole Slide Image Classification](../../ICLR2026/medical_imaging/exploiting_low-dimensional_manifold_of_features_for_few-shot_whole_slide_image_c.md)
- [\[CVPR 2026\] MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification](../../CVPR2026/medical_imaging/muse_harnessing_precise_and_diverse_semantics_for_few-shot_whole_slide_image_cla.md)
- [\[ECCV 2024\] TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data](tip_tabular-image_pre-training_for_multimodal_classification_with_incomplete_dat.md)

</div>

<!-- RELATED:END -->
