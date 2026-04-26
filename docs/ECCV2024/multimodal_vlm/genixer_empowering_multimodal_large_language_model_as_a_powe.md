---
title: >-
  [论文解读] GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator
description: >-
  [ECCV 2024][多模态][数据生成] Genixer提出一套完整的视觉指令微调数据生成pipeline，通过训练现有MLLM（LLaVA1.5和Shikra）使其具备数据生成能力，无需GPT-4即可生成高质量的VQA和REC指令数据，并通过Fuyu驱动和CLIP驱动的自动过滤框架保证数据质量。
tags:
  - ECCV 2024
  - 多模态
  - 数据生成
  - 视觉指令微调
  - MLLM
  - VQA
  - REC
---

# GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator

**会议**: ECCV 2024  
**arXiv**: [2312.06731](https://arxiv.org/abs/2312.06731)  
**代码**: https://github.com/zhaohengyuan1/Genixer (有)  
**领域**: 多模态VLM  
**关键词**: 数据生成, 视觉指令微调, MLLM, VQA, REC

## 一句话总结

Genixer提出一套完整的视觉指令微调数据生成pipeline，通过训练现有MLLM（LLaVA1.5和Shikra）使其具备数据生成能力，无需GPT-4即可生成高质量的VQA和REC指令数据，并通过Fuyu驱动和CLIP驱动的自动过滤框架保证数据质量。

## 研究背景与动机

1. **领域现状**：MLLM展现了卓越的多模态问题解决能力，但训练数据主要依赖两种途径：将现有VL数据集转为指令格式（受限于图像多样性）或使用GPT-4生成（成本高、复杂任务效果差）。

2. **现有痛点**：(1) GPT-4生成数据成本高，难以大规模使用；(2) GPT-4V在REC等复杂任务上无法生成正确的边界框；(3) 现有VL数据集多来自COCO，图像多样性受限。

3. **核心矛盾**：高质量指令数据是MLLM训练的关键，但获取成本高，且生成质量难以保证。

4. **本文要解决什么？** 探索现有MLLM独立生成视觉指令数据的能力，无需GPT-4辅助。

5. **切入角度**：设计两级指令模板控制数据生成的任务类型，配合自动数据过滤保证质量。

6. **核心idea一句话**：训练MLLM自身成为数据生成器，用两级指令控制生成模式，再用Fuyu/CLIP驱动的过滤框架保证质量。

## 方法详解

### 整体框架

Genixer pipeline包含四步：(1) 收集9种代表性VL任务数据；(2) 设计两级指令模板（通用指令+特定指令）控制生成；(3) 训练两个数据生成器GenixerL（基于LLaVA1.5，通用任务）和GenixerS（基于Shikra，定位任务）；(4) 自动生成并过滤数据。

### 关键设计

1. **两级指令模板**：Generic Instruction让模型自由生成任意类型数据（模式1），Specific Instruction指定特定任务类型如"This is a Common VQA task"（模式2）。通过控制常数τ调节训练样本中两种指令的比例。

2. **Fuyu驱动数据过滤**：对通用任务生成的数据，用Fuyu-8B模型验证生成的QA是否与图像一致。计算回答"Yes"的概率，设阈值λ=0.7过滤，从1.4M原始数据中筛选出915K高质量实例。

3. **CLIP驱动数据过滤**：对REC任务数据，先用正则表达式提取文本表达和坐标，再逐步过滤：排除格式错误→排除过小框→用OpenCLIP计算文本-区域相似度，阈值0.6，从1.4M中筛选350K。

### 损失函数 / 训练策略

- 自回归训练目标，最大化条件概率：$\max \sum_{i}^{L} \log p(X_o | X_G, X_S, X_I)$
- GenixerL：AdamW优化器，lr=1e-5，batch=128，1 epoch，约14小时
- GenixerS：两阶段训练，第一阶段REC/REG（lr=3e-5），第二阶段加入PointQA/RD（lr=1e-5）

## 实验关键数据

### 主实验

| 模型 | VQAv2 | GQA | VizWiz | ScienceQA | POPE | MME |
|------|-------|-----|--------|-----------|------|-----|
| LLaVA-1.5 | 78.5 | 62.0 | 50.0 | 66.8 | 85.9 | 1465.0 |
| +Genixer-915K | 79.1 | 63.1 | **53.8** | **69.7** | **87.3** | **1502.7** |

Shikra+Genixer-350K在8个REC数据集中7个提升，平均+0.6%。

### 消融实验

| 数据规模 | VQAv2 | ScienceQA | POPE |
|----------|-------|-----------|------|
| 300K | 79.0 | 68.5 | 87.1 |
| 610K | 79.0 | 69.2 | 87.2 |
| 915K | 79.1 | 69.7 | 87.3 |

### 关键发现

- 更大的数据规模持续提升性能，验证生成数据质量
- 更高的过滤阈值（λ=0.7优于λ=0）虽减少数据量但提升效果，说明质量比数量重要
- GenixerS在REC数据生成上超越GPT-4V

## 亮点与洞察

- 首次系统验证了MLLM自身可作为高质量数据生成器
- 两级指令设计实现了任务类型的灵活控制
- GenixerS在REC等需要精确定位的任务上超越GPT-4V
- 合成数据能有效缓解模型幻觉问题

## 局限性 / 可改进方向

- 受限于计算资源未测试更大LLM规模（13B/34B）
- 数据规模可进一步扩展至LAION-2B级别
- 对RD等开放式复杂任务的数据质量评估仍有挑战

## 相关工作与启发

- 与ShareGPT4V等依赖GPT-4V生成数据的方法不同，Genixer完全自给自足
- 启发：MLLM的数据生成能力被低估，未来可构建更大规模的自动生成训练数据

## 评分

- ⭐ 创新性：⭐⭐⭐⭐（自给自足的数据生成思路新颖）
- ⭐ 实用性：⭐⭐⭐⭐⭐（节省成本，灵活性强）
- ⭐ 实验充分度：⭐⭐⭐⭐（12+8个benchmark全面评估）
- ⭐ 写作清晰度：⭐⭐⭐⭐（pipeline清晰，统计分析详实）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_lan.md)
- [\[ECCV 2024\] FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](freemotion_mocapfree_human_motion_synthesis_with_multimodal_.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)
- [\[ECCV 2024\] Merlin: Empowering Multimodal LLMs with Foresight Minds](merlin_empowering_multimodal_llms_with_foresight_minds.md)
- [\[ECCV 2024\] BRAVE: Broadening the Visual Encoding of Vision-Language Models](brave_broadening_the_visual_encoding_of_vision-language_models.md)

<!-- RELATED:END -->
