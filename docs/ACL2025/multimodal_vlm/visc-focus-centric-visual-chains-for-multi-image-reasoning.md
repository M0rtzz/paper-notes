---
title: >-
  [论文解读] Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains
description: >-
  [ACL 2025][多模态][多图推理] 本文提出 Focus-Centric Visual Chain 推理范式，将多图复杂任务分解为聚焦子集图像的逐步推理序列，并提出 FCDS 数据合成框架构建 VISC-150K 数据集，在 7 个多图基准上平均提升 3.16% 和 2.24%。
tags:
  - ACL 2025
  - 多模态
  - 多模态VLM
  - 视觉推理链
  - 焦点分解
  - 数据合成
  - 多图基准
---

# Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains

**会议**: ACL 2025  
**arXiv**: [2504.20199](https://arxiv.org/abs/2504.20199)  
**代码**: [https://github.com/VISC](https://github.com/VISC)  
**领域**: 多模态VLM  
**关键词**: 多图推理, 视觉推理链, 焦点分解, 数据合成, 多图基准

## 一句话总结

本文提出 Focus-Centric Visual Chain 推理范式，将多图复杂任务分解为聚焦子集图像的逐步推理序列，并提出 FCDS 数据合成框架构建 VISC-150K 数据集，在 7 个多图基准上平均提升 3.16% 和 2.24%。

## 研究背景与动机

1. **领域现状**：VLM 在单图任务上表现优异，但面对多图输入时性能显著下降，因为跨图关联和视觉不连续性带来了巨大挑战。
2. **现有痛点**：现有多图推理数据稀缺，直接用多模态模型生成推理链不可靠（即使 GPT-4o 在多图任务上也不稳定），闭源模型生成数据成本过高。
3. **核心矛盾**：多图推理需要模型理解跨图关系，但当前训练范式在扩展图像上下文窗口时收益递减。
4. **本文目标**：设计一种多图推理范式和配套的数据合成方法，以数据驱动方式提升 VLM 的多图推理能力。
5. **切入角度**：将复杂多图问题分解为一系列子问题，每个子问题聚焦于输入图像的一个子集。
6. **核心 idea**：渐进式聚焦——每步推理只关注最相关的图像子集，逐步聚合视觉证据。

## 方法详解

### 整体框架

推理范式：模型在每步生成子问题 $q_i$ 并选择焦点图像子集 $G_i$，回答后决定是否继续推理。数据合成框架 FCDS：自底向上地从特征提取 → 配对连接 → 关系标注 → 问题生成，完全使用开源模型。

### 关键设计

1. **Focus-Centric Visual Chain**:
    - 每步推理产生 $(q_i, G_i, a_i, z_i)$：子问题、焦点图像、中间答案、终止信号
    - 渐进式信息聚合，最终综合所有中间答案得到最终回答

2. **FCDS 数据合成**:
    - 特征提取：为每张图生成结构化 profile（整体视图、背景、物体属性、交互）
    - 配对连接：基于物体共现和事件关联识别图像对
    - 关系标注：分为时间、空间、语义三类关系
    - 问题生成：基于图像网络和关系标注构建推理路径和问题

3. **自底向上设计**: 从单图特征到图对关系再到链式推理，确保每步都有可靠的基础。

### 损失函数 / 训练策略

标准的指令微调损失。

## 实验关键数据

### 主实验

| 基准 | LLaVA-OV | +VISC-150K | 提升 |
|------|----------|------------|------|
| 7个多图基准平均 | baseline | +3.16% | 在4/7基准上SOTA |

### 关键发现

- 一致性提升：在不同模型架构上都有效（LLaVA-OV +3.16%, Qwen2-VL +2.24%）
- 不损害通用VL能力
- GPT-4o在部分多图任务上仍会失败，但用VISC训练的2B模型可以解决

### VISC-150K数据集构成

| 关系类型 | 样本数 | 平均推理步数 |
|---------|--------|----------|
| 时间关系 | 52K | 2.3 |
| 空间关系 | 48K | 2.1 |
| 语义关系 | 50K | 2.5 |
| 合计 | 150K | 2.3 |

### 各基准提升详情

| 基准 | LLaVA-OV | +VISC | Δ |
|------|----------|------|---|
| NLVR2 | 83.2 | 87.1 | +3.9 |
| QBench | 72.5 | 76.8 | +4.3 |
| MuirBench | 68.1 | 70.3 | +2.2 |


## 亮点与洞察

- "聚焦分解"的思路简洁有效——它不是让模型同时处理所有图像，而是教模型选择性地关注最相关的子集。
- FCDS框架完全基于开源模型，可重复性和可扩展性好。

## 局限与展望

- 合成数据的推理链质量依赖于特征提取和关系标注的准确性，错误可能逐步传播
- 推理步数的控制机制（终止信号 $z_i$）可能需要更精细的设计——何时停止推理很关键
- 关系标注限于时间/空间/语义三类，可能不覆盖所有跨图关系（如因果、对比等）
- 图像数量增加时焦点选择的复杂度也会增加，可扩展性待验证
- 未来可以探索与强化学习结合来优化推理路径选择
- 对视频输入的适用性未探索，可能需要帧选择策略

## 相关工作与启发

- **vs CoT for VLMs**: 一般CoT不针对多图场景的焦点选择，VISC每步动态选择相关图像子集，更有针对性
- **vs 直接蒸馏GPT-4o**: 成本高且不可靠（GPT-4o在多图上也会出错），FCDS完全基于开源模型更高效可控
- **vs Mantis/LLaVA-OneVision**: 这些模型架构支持多图但训练范式未针对多图推理优化，VISC-150K填补了数据空白
- **vs Tree-of-Thought**: ToT是通用推理框架，VISC针对多图场景的视觉焦点选择做了特化设计


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。

## 评分

- 新颖性: ⭐⭐⭐⭐ 焦点视觉链范式和自底向上合成方法都有新意
- 实验充分度: ⭐⭐⭐⭐ 7个基准+两种架构+不损害通用能力的验证
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰，图示直观
- 价值: ⭐⭐⭐⭐ 数据集开源，对多图VLM有实际价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] MathCoder-VL: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning](mathcoder-vl_bridging_vision_and_code_for_enhanced_multimodal_mathematical_reaso.md)
- [\[ACL 2025\] Symmetrical Visual Contrastive Optimization: Aligning Vision-Language Models with Minimal Contrastive Images](symmetrical_visual_contrastive_optimization_aligning_visionlanguage.md)
- [\[ACL 2025\] Benchmarking and Improving Large Vision-Language Models for Fundamental Visual Graph Understanding and Reasoning](benchmarking_and_improving_large_vision-language_models_for_fundamental_visual_g.md)
- [\[ACL 2025\] Vision-Language Models Struggle to Align Entities across Modalities](vision-language_models_struggle_to_align_entities_across_modalities.md)
- [\[ACL 2025\] Performance Gap in Entity Knowledge Extraction Across Modalities in Vision Language Models](performance_gap_in_entity_knowledge_extraction_across_modalities_in_vision_langu.md)

</div>

<!-- RELATED:END -->
