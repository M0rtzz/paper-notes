---
title: >-
  [论文解读] ATRI: Mitigating Multilingual Audio Text Retrieval Inconsistencies by Reducing Data Distribution Errors
description: >-
  [ACL 2025][语音][多语言音频文本检索] 本文分析了多语言音频文本检索（ML-ATR）中跨语言检索不一致的根本原因是训练数据分布误差，并提出 KCL（1-to-K对比学习）和 CACL（音频-英语共锚对比学习）两种策略来减少该误差，在 8 种语言上达到了 SOTA 性能。
tags:
  - ACL 2025
  - 语音
  - 多语言音频文本检索
  - 跨语言一致性
  - 对比学习
  - 数据分布误差
  - 模态对齐
---

# ATRI: Mitigating Multilingual Audio Text Retrieval Inconsistencies by Reducing Data Distribution Errors

**会议**: ACL 2025  
**arXiv**: [2502.14627](https://arxiv.org/abs/2502.14627)  
**代码**: https://github.com/ATRI-ACL/ATRI-ACL  
**领域**: 语音音频  
**关键词**: 多语言音频文本检索, 跨语言一致性, 对比学习, 数据分布误差, 模态对齐

## 一句话总结

本文分析了多语言音频文本检索（ML-ATR）中跨语言检索不一致的根本原因是训练数据分布误差，并提出 KCL（1-to-K对比学习）和 CACL（音频-英语共锚对比学习）两种策略来减少该误差，在 8 种语言上达到了 SOTA 性能。

## 研究背景与动机

1. **领域现状**：音频文本检索（ATR）基于 CLAP 模型取得了显著进展，但主要面向英语，多语言检索研究有限。
2. **现有痛点**：现有 ML-ATR 方案在每个 epoch 随机选择一种语言的文本与音频配对训练，导致跨语言检索结果不一致——同一音频用不同语言查询可能得到完全不同的结果。
3. **核心矛盾**：随机语言采样导致实际训练数据分布与理想的全语言分布之间存在差距，这个分布误差在训练过程中累积放大，最终导致模态对齐不精确。
4. **本文目标**：理论分析不一致的根因，并提出计算效率与性能兼顾的解决方案。
5. **切入角度**：从模态对齐方向误差和权重误差上界两个角度进行理论分析，证明数据分布误差是不一致问题的根本原因。
6. **核心 idea**：通过消除（KCL）或减少（CACL）每个训练 epoch 的数据分布误差来同时改善检索召回率和跨语言一致性。

## 方法详解

### 整体框架

ATRI 包含两种训练策略供不同场景选择：KCL 将每条音频同时与所有 K 种语言的文本做对比学习（理论上消除分布误差，但内存开销大）；CACL 将每条音频与英语文本 + 一种随机语言文本 + 英语-随机语言之间做三方对比学习（近似减少分布误差，开销小）。

### 关键设计

1. **理论分析：权重误差上界**:

    - 功能：量化数据分布误差对模型权重的影响
    - 核心思路：推导了训练过程中权重误差的递推上界：$\|w_{eT} - w'_{eT}\| \leq a^T\|w_{(e-1)T} - w'_{(e-1)T}\| + \eta\sum_{(a,t)}\|p(a,t) - p'_e(a,t)\|\sum_{j}(a^j g_{max})$，其中 $p$ 是理想全语言分布，$p'_e$ 是随机采样分布。展开递推可知，所有 epoch 的数据分布误差累积决定了最终的权重偏差。
    - 设计动机：直觉上知道随机采样不好，但需要理论框架来量化影响并指导解决方案设计。

2. **1-to-K 对比学习（KCL）**:

    - 功能：在每个 epoch 中同时使用所有语言的文本进行训练
    - 核心思路：对每条音频 $a_i$，同时计算它与所有 $K$ 种语言文本的对比损失：$\mathcal{L}_{kcl} = \frac{1}{2NK}(\mathcal{L}^{a2t}_{kcl} + \mathcal{L}^{t2a}_{kcl})$，其中 a2t 和 t2a 分别是音频到文本和文本到音频的对比损失。
    - 设计动机：KCL 让训练数据分布与理想分布完全一致（$p'_e = p$），从理论上消除了分布误差。但代价是 GPU 内存随语言数线性增长。

3. **音频-英语共锚对比学习（CACL）**:

    - 功能：以接近原有方案的开销实现接近 KCL 的效果
    - 核心思路：每条数据使用三元组 $(a_i, t_{i1}, t_{iq_i})$（音频、英语文本、随机语言文本），计算三个对比损失：$\mathcal{L}_{cacl} = \frac{1}{6N}(\mathcal{L}^{ae} + \mathcal{L}^{at} + \mathcal{L}^{et})$，分别是音频-英语、音频-随机语言、英语-随机语言之间的对比学习。
    - 设计动机：英语作为锚点连接所有其他语言，$\mathcal{L}^{et}$ 拉近不同语言的嵌入，使音频对齐的目标方向更接近所有语言的算术平均。每个 epoch 的文本量不随语言数增长。

### 损失函数 / 训练策略

- 所有模型使用 Adam 优化器，学习率 $5 \times 10^{-6}$，温度 $\tau = 0.07$
- 预训练权重来自 ML-CLAP，微调 10 个 epoch
- CED-Base 作为音频编码器，SONAR 作为多语言文本编码器

## 实验关键数据

### 主实验（AudioCaps 英语 T2A R@1）

| 方法 | R@1 | R@5 | mAP10 |
|------|-----|-----|-------|
| ML-CLAP | 47.31 | 80.65 | 61.44 |
| CACL | 49.05 | 82.14 | 63.07 |
| **KCL** | **49.68** | **82.44** | **63.34** |

### 一致性实验

| 指标 | ML-CLAP | CACL | KCL |
|------|---------|------|-----|
| MRV (AudioCaps) | 10.38 | 8.71 | **7.52** |
| Avg Gap | 0.189 | 0.161 | **0.141** |
| Avg Dis | 0.330 | 0.312 | **0.288** |

### 关键发现

- KCL 在所有指标上最优但 GPU 内存开销是 ML-CLAP 的 2.8 倍
- CACL 仅增加约 10% 开销就实现了接近 KCL 的效果
- 日语和中文由于句法差异大，表现低于西方语言
- 噪声更多的 Clotho 数据集上 MRV 显著高于 AudioCaps

## 亮点与洞察

- **理论驱动的方法设计**：先推导权重误差上界，再根据上界中的关键项设计解决方案，这种"理论先行"的研究范式值得学习。
- CACL 的**英语锚点**策略巧妙利用了英语作为高资源语言的优势，以最小代价实现跨语言对齐。
- 这个框架可以推广到多语言图像/视频检索等其他多模态对齐场景。

## 局限与展望

- 权重误差上界基于 SGD 优化器启发式推导，对 Adam 等复杂优化器的理论保证较弱
- 翻译质量影响实验结果，日语/中文的翻译可能引入更多噪声
- 未探索更多语言（仅 8 种），更大规模的多语言场景效果待验证

## 相关工作与启发

- **vs ML-CLAP**: 随机语言采样的 baseline，ATRI 通过减少分布误差在召回和一致性上全面超越
- **vs CLAP**: 仅针对英语的单语言模型，ATRI 扩展到多语言场景

## 评分

- 新颖性: ⭐⭐⭐⭐ 理论分析角度新颖，KCL/CACL设计有理论支撑
- 实验充分度: ⭐⭐⭐⭐ 多数据集多语言测试，一致性指标全面
- 写作质量: ⭐⭐⭐⭐ 理论推导清晰，方法动机明确
- 价值: ⭐⭐⭐⭐ 对多语言多模态对齐有实际指导意义

<!-- RELATED:START -->

## 相关论文

- [\[ACL 2025\] SpeechWeave: Diverse Multilingual Synthetic Text & Audio Data Generation Pipeline for Training Text to Speech Models](speechweave_diverse_multilingual_synthetic_text_audio_data_generation_pipeline_f.md)
- [\[ACL 2025\] CLaMP 3: Universal Music Information Retrieval Across Unaligned Modalities and Unseen Languages](clamp_3_universal_music_information_retrieval_across_unaligned_modalities_and_un.md)
- [\[ACL 2025\] Analyzing and Mitigating Inconsistency in Discrete Audio Tokens for Neural Codec Language Models](audio_token_consistency.md)
- [\[ACL 2025\] WavRAG: Audio-Integrated Retrieval Augmented Generation for Spoken Dialogue Models](wavrag_audio-integrated_retrieval_augmented_generation_for_spoken_dialogue_model.md)
- [\[ACL 2025\] In-the-wild Audio Spatialization with Flexible Text-guided Localization](tas_audio_spatialization.md)

<!-- RELATED:END -->
