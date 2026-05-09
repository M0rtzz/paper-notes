---
title: >-
  [论文解读] AFreeCA: Annotation-Free Counting for All
description: >-
  [ECCV 2024][目标检测][无监督计数] 利用潜在扩散模型（LDM）生成合成计数和排序数据，提出首个可适用于任意物体类别的无监督计数方法，无需任何人工标注即可实现准确计数。
tags:
  - ECCV 2024
  - 目标检测
  - 无监督计数
  - 合成数据
  - 潜在扩散模型
  - 排序学习
  - 密度分类
---

# AFreeCA: Annotation-Free Counting for All

**会议**: ECCV 2024  
**arXiv**: [2403.04943](https://arxiv.org/abs/2403.04943)  
**代码**: [https://github.com/adrian-dalessandro/AFreeCA](https://github.com/adrian-dalessandro/AFreeCA)  
**领域**: 目标检测  
**关键词**: 无监督计数, 合成数据, 潜在扩散模型, 排序学习, 密度分类

## 一句话总结

利用潜在扩散模型（LDM）生成合成计数和排序数据，提出首个可适用于任意物体类别的无监督计数方法，无需任何人工标注即可实现准确计数。

## 研究背景与动机

### 领域现状

**领域现状**：物体计数在人群分析、野生动物监测、交通分析等场景中有广泛应用

### 现有痛点

**现有痛点**：现有全监督方法需要大量标注（如人群计数数据集标注 5109 张图需 3000 小时）

### 核心矛盾

**核心矛盾**：现有无监督方法仅限于人群计数，无法推广到任意物体类别

### 解决思路

**解决思路**：LDM（如 Stable Diffusion）可生成现实图像，但**文本编码器对数量理解有限**——提示 "20 people" 生成的图像中实际数量与提示数量的相对误差随数量增大而增大

### 补充说明

**补充说明**：关键洞察**：虽然 LDM 无法精确生成指定数量的图像，但可以可靠地**增加或减少**图像中物体数量，提供可靠的排序信号

## 方法详解

### 整体框架

三阶段流水线：
1. **学习排序**：用 LDM 生成排序三元组，训练排序网络学习与计数相关的特征
2. **学习计数**：用 LDM 生成带噪数量标签的合成图像，微调线性层锚定计数值
3. **密度引导分割**：训练密度分类器，推理时将密集区域分割为更小的可靠计数区域

### 关键设计

**排序数据生成**：
- 对参考图像用 SD 的 img2img 减少物体（正提示 "an empty place"，负提示 "people"）
- 用 outpainting 增加物体（在图像边缘扩展）
- 每张参考图生成 4 个增加版本 + 4 个减少版本 → 16 个排序三元组
- 验证显示 99% 的情况下增减关系正确

**排序网络预训练**：
- 使用 RankSim 风格的排序损失，同时约束特征空间和输出空间的排序一致性
- 损失函数 L_sort = ℓ^y_sort + λ·ℓ^z_sort（λ=5.0）
- 使用 blackbox combinatorial solver 优化排序函数

**计数网络微调**：
- 仅微调排序网络顶部的线性层（冻结特征提取器以保持排序特征完整性）
- 使用 CleanNet 风格的噪声过滤：计算类别原型，移除偏离原型的样本
- MSE 损失训练

**密度分类器引导分割（DCGP）**：
- 训练三类密度分类器（无目标/稀疏/密集），同样仅微调线性层
- 推理时：稀疏区域直接用 count map 求和；密集区域提取高分辨率 patch 重新计数
- 3×3 网格分割图像

### 损失函数 / 训练策略

- 排序阶段：排序损失 L_sort（结合输出排序和特征空间排序）
- 计数阶段：MSE 损失 L_count（线性层 + 冻结骨干）
- 密度分类阶段：交叉熵损失 L_dense

## 实验关键数据

### 主实验

人群计数数据集对比：

| 方法 | 类型 | SHB MAE | SHA MAE | QNRF MAE |
|------|------|---------|---------|----------|
| CrowdCLIP | 无监督 | 69.3 | 146.1 | 283.3 |
| AFreeCA (Ours) | **无监督** | **35.0** | **152.7** | **283.1** |
| CLIP-Count | 零样本 | 45.7 | 192.6 | - |

车辆计数（CARPK）对比：超越少样本方法 FamNet。

### 消融实验

| 组件 | 效果 |
|------|------|
| 排序预训练 | 学习到聚焦于目标物体的特征（可视化验证） |
| 噪声过滤 | 移除偏离类别原型的合成样本，提升计数准确性 |
| DCGP 密度引导 | 显著提升密集场景计数精度 |
| 增加+减少 vs 仅减少 | 双向增减生成更大范围的计数三元组 |

### 关键发现

1. 排序网络特征图的通道均值可视化显示，网络确实学会了关注目标物体，跨不同密度均有效
2. LDM 生成的排序数据比计数数据更可靠（排序关系 99% 正确 vs 计数标签噪声随数量增大）
3. DCGP 通过将密集区域分割为小 patch 并从原图提取高分辨率特征，有效扩展了计数范围

## 亮点与洞察

- **"排序比计数容易"的关键洞察**：巧妙地将 LDM 的弱点（无法精确控制数量）转化为优势（可靠地增减物体提供排序信号）
- **首个任意类别无监督计数**：突破了无监督方法仅限人群计数的局限
- **设计哲学**：先学排序特征（可靠信号），再用噪声计数数据锚定（脆弱信号 + 冻结骨干保护）
- **仅微调线性层**：避免合成数据的分布偏差破坏预训练特征

## 局限与展望 / 可改进方向

- 高密度场景下合成数据标签噪声较大，计数精度受限
- DCGP 使用固定 3×3 网格，可能不适合所有场景布局
- 三类密度分类（无/稀疏/密集）较粗糙，更细粒度分类可能提升效果
- 排序三元组的生成依赖 SD 的 img2img 质量，某些困难类别（如小物体）可能不可靠
- 未来方向：自适应分割策略、更强的噪声过滤机制、结合 SAM 等分割模型

## 相关工作与启发

- CSS-CCNN 和 CrowdCLIP 是此前的无监督计数方法，但限于人群
- RankSim 的排序思想被有效迁移到计数任务
- "先排序再计数"的两阶段策略对其他难以直接监督但排序关系可靠的任务有启发

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4.5 |
| 技术深度 | 4 |
| 实验充分性 | 4 |
| 写作质量 | 4 |
| 实用价值 | 4 |
| 总分 | 4.1 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Can OOD Object Detectors Learn from Foundation Models?](can_ood_object_detectors_learn_from_foundation_models.md)
- [\[ECCV 2024\] Adaptive Bounding Box Uncertainties via Two-Step Conformal Prediction](adaptive_bounding_box_uncertainties_via_twostep_conformal_pr.md)
- [\[ECCV 2024\] Plain-Det: A Plain Multi-Dataset Object Detector](plain-det_a_plain_multi-dataset_object_detector.md)
- [\[ECCV 2024\] LaMI-DETR: Open-Vocabulary Detection with Language Model Instruction](lami-detr_open-vocabulary_detection_with_language_model_instruction.md)
- [\[ECCV 2024\] Zero-Shot Detection of AI-Generated Images](zero-shot_detection_of_ai-generated_images.md)

</div>

<!-- RELATED:END -->
