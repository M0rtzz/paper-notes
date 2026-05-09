---
title: >-
  [论文解读] VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection
description: >-
  [CVPR 2025][LLM推理][视频问答] 本文提出VideoEspresso数据集及混合LVLM协作框架，通过语义感知的冗余去除构建高质量视频QA对，并引入多模态链式思维（CoT）标注，结合轻量帧选择器和两阶段推理模型实现高效精准的视频推理。
tags:
  - CVPR 2025
  - LLM推理
  - 视频问答
  - 链式思维
  - 核心帧选择
  - 多模态推理
  - 数据集
---

# VideoEspresso: A Large-Scale Chain-of-Thought Dataset for Fine-Grained Video Reasoning via Core Frame Selection

**会议**: CVPR 2025  
**arXiv**: [2411.14794](https://arxiv.org/abs/2411.14794)  
**代码**: [https://github.com/hshjerry/VideoEspresso](https://github.com/hshjerry/VideoEspresso)  
**领域**: LLM推理  
**关键词**: 视频问答, 链式思维, 核心帧选择, 多模态推理, 数据集

## 一句话总结
本文提出VideoEspresso数据集及混合LVLM协作框架，通过语义感知的冗余去除构建高质量视频QA对，并引入多模态链式思维（CoT）标注，结合轻量帧选择器和两阶段推理模型实现高效精准的视频推理。

## 研究背景与动机
1. **领域现状**：大型视觉语言模型（LVLM）在视频理解上取得进展，但在复杂视频推理任务上表现仍不理想，主要受限于高质量大规模数据集的匮乏。
2. **现有痛点**：现有VideoQA数据集要么依赖昂贵的人工标注且粒度不足，要么自动构建方法存在逐帧分析的冗余问题，限制了可扩展性和复杂推理训练的有效性。
3. **核心矛盾**：视频内容高度冗余，关键信息分布稀疏——逐帧分析计算昂贵且信息过载，而仅用元数据则丢失细节。
4. **本文目标**：构建一个保留空间细节和时间连贯性的细粒度推理VideoQA数据集，并设计高效利用该数据集的框架。
5. **切入角度**：先将视频帧映射到语言空间，基于语义相似度去除冗余帧，再用GPT-4o从精简描述中生成QA对和CoT标注。
6. **核心idea**：语义驱动的视频信息压缩 + 多模态CoT标注 + 轻量-重量模型协作推理框架。

## 方法详解

### 整体框架
原始视频 → InternVL2-8B帧级描述 → BGE-M3语义去冗余 → 连续分组(每组15帧描述) → GPT-4o生成QA对 → GPT-4o提取CoT证据+核心帧+关键物体 → GroundingDINO空间标注 + BGE-M3时间标注 → 多模态CoT数据集。推理框架：轻量LVLM(1B)+LLM(0.5B)帧选择器 → 两阶段微调推理LVLM。

### 关键设计

1. **语义感知冗余去除**:

    - 功能：从视频中提取最精简且保留关键信息的帧序列。
    - 核心思路：先用LVLM对采样帧生成文本描述，然后用BGE-M3计算相邻帧描述的语义相似度，对余弦相似度超过阈值 $\tau$ 的相邻帧执行LIFO过滤。不同于基于图像表示的关键帧提取，这里在语言空间进行语义过滤。
    - 设计动机：传统基于视觉特征的关键帧提取可能保留视觉相似但语义不同的帧，在语义空间去重更准确。

2. **多模态CoT标注流水线**:

    - 功能：为每个QA对标注多模态推理证据，包含时间和空间维度的关键信息。
    - 核心思路：(1) GPT-4o从帧描述组中选出与问题最相关的核心帧描述；(2) 提取关键物体；(3) 组织为证据文本。空间标注用GroundingDINO标注边界框 + CLIP验证一致性；时间标注用BGE-M3检索匹配原始帧获取时间戳。
    - 设计动机：仅有文本级CoT不够，需要时空维度的多模态证据来支持复杂视频推理。

3. **混合LVLM协作推理框架**:

    - 功能：通过轻量选择器+强力推理器实现高效准确的视频推理。
    - 核心思路：第一阶段用1B参数LVLM为帧生成描述，0.5B参数LLM选出与问题最相关的核心帧；第二阶段用大LVLM进行两阶段SFT——Stage-1学习从核心帧提取证据（提示词："Please provide evidence..."），Stage-2学习基于证据回答问题（提示词："Please answer with evidence..."）。
    - 设计动机：将证据生成和答案生成解耦，增强推理透明度和准确性；轻量选择器显著降低推理成本。

### 损失函数 / 训练策略
帧选择器使用标准SFT训练；推理LVLM使用两阶段SFT，第一阶段训练证据提取能力（提示词："Please provide evidence..."），第二阶段训练基于证据的问答能力（提示词："Please answer with evidence..."）。推理时先选帧再生成证据最后回答。最终数据集涵盖14个视频推理任务类别。

## 实验关键数据

### 主实验

| 模型 | 参数 | 平均得分 (14任务) | Causal | Theme | Behav. |
|------|------|------------------|--------|-------|--------|
| GPT-4o | - | 26.4 | 22.8 | 32.8 | 19.3 |
| Qwen-VL-Max | - | 26.0 | 21.4 | 26.2 | 26.3 |
| LLaVA-1.5 (7B) | 7B | 24.2 | 17.1 | 26.2 | 21.1 |
| **VideoEspresso (ours)** | 7B | **最优** | - | - | - |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| Full (选择器+两阶段) | 最优 | 完整框架 |
| w/o 帧选择器 (均匀采样) | 下降 | 核心帧选择重要 |
| 单阶段SFT | 下降 | 两阶段解耦推理更优 |
| w/o CoT标注 | 下降 | 多模态证据提升推理 |

### 关键发现
- 不同任务的关键帧间距分布差异巨大，证实均匀采样策略次优。
- VideoEspresso的QA长度和词汇多样性远超MVBench，质量更高。
- 帧选择器作为即插即用模块可应用于任何LVLM前端，降低视频token长度。
- 两阶段训练中证据生成阶段对提升最终答案质量至关重要——GT-CoT证据使性能从34.13%跃升至72.95%（+38.82%）。
- 选择器采用InternVL2-1B+QwenLM-0.5B仅增加1.5B参数和0.37 GPU小时训练，将平均帧数从8帧降至2.36帧，推理内存减少26-28GB。
- 选择器可零样本迁移到GPT-4o和InternVL2上分别带来+2.59%和+1.46%的准确率提升，同时帧输入减少约85%。
- 对LongVA实现了98%的帧输入减少，虽然性能略降但计算开销大幅降低。

## 亮点与洞察
- **语义空间去冗余的思路**：将视频帧先映射到语言空间再去重，比视觉特征层面去重更有效，因为语义相似的帧才真正冗余。
- **轻重模型协作**：用小模型做帧选择、大模型做推理的设计非常实用，显著降低了计算成本。
- **两阶段推理解耦**：先提取证据再回答的范式增加了推理的可解释性和准确性，可迁移到其他需要解释性推理的任务。
- **数据集规模与质量**：14个推理任务覆盖因果推理、主题分析、行为理解等维度。整体方法7B参数在平均准确率上达34.1%，比开源最优InternVL2高+5.4%，比闭源GPT-4o高+7.7%。输入帧数仅为LongVA-DPO的1.8%，FLOPs仅为LLaVA-Next-interleave的14.74%。

## 局限与展望
- 数据生成依赖GPT-4o，成本仍然较高。
- 14个任务的分类可能不够细粒度，某些推理类型未被覆盖。
- 帧选择器的性能受限于轻量LVLM的描述质量。
- 未来可探索端到端训练帧选择器和推理器。
- 空间标注（GroundingDINO边界框）与时间标注（BGE-M3帧检索）的精度受限于各自工具的能力上限。
- 当视频内容在语义空间中变化缓慢（如监控视频）时，语义去冗余可能过度删帧。
- InternVL2和LongVA-DPO在"主题分析"和"烹饪过程"任务上表现优异，可能源于预训练数据中类似数据的覆盖。
- 主观评估（逻辑一致性、事实性、准确性、简洁性）中，在简洁性上超越GPT-4o达5%。

## 相关工作与启发
- **vs MVBench**: MVBench的QA较短且聚焦基础查询，VideoEspresso包含更长更复杂的推理QA。
- **vs VideoCoT**: VideoCoT仅关注文本级推理，VideoEspresso引入了空间（边界框）和时间（帧索引）的多模态CoT。
- **vs LLaVA-Video**: LLaVA-Video直接处理所有帧导致token爆炸，本文通过核心帧选择实现高效推理。
- **vs TimeChat**: TimeChat虽有时间标注但缺乏空间定位，VideoEspresso的时空联合CoT更完整。
- **构建规模**：数据生成成本约$2,500（GPT-4o API），产生约14K多模态CoT-QA对，每条包含核心帧列表、关键物体、空间边界框和时间戳。

## 评分

### 实现细节
语义去冗余使用BGE-M3编码器，余弦相似度阈值$tau$控制帧过滤粒度。
GroundingDINO标注边界框后用CLIP验证视觉-文本一致性。
- 新颖性: ⭐⭐⭐⭐ 多模态CoT标注和混合协作框架设计新颖
- 实验充分度: ⭐⭐⭐⭐ 14个任务评估全面，但部分消融不够详细
- 写作质量: ⭐⭐⭐⭐ 流水线描述清晰，图表丰富
- 价值: ⭐⭐⭐⭐ 对视频推理研究有重要贡献，数据集有长期使用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2025\] Argus: Vision-Centric Reasoning with Grounded Chain-of-Thought](argus_vision-centric_reasoning_with_grounded_chain-of-thought.md)
- [\[CVPR 2025\] Interleaved-Modal Chain-of-Thought](interleaved-modal_chain-of-thought.md)
- [\[CVPR 2025\] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](cot-vla_visual_chain-of-thought_reasoning_for_vision-language-action_models.md)
- [\[CVPR 2025\] Style Evolving along Chain-of-Thought for Unknown-Domain Object Detection](style_evolving_along_chain-of-thought_for_unknown-domain_object_detection.md)
- [\[CVPR 2025\] Reason-before-Retrieve: One-Stage Reflective Chain-of-Thoughts for Training-Free Zero-Shot Composed Image Retrieval](osrcir_reflective_cot.md)

</div>

<!-- RELATED:END -->
