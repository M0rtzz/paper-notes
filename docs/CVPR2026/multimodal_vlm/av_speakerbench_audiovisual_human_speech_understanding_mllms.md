---
title: >-
  [论文解读] See, Hear, and Understand: Benchmarking Audiovisual Human Speech Understanding in Multimodal Large Language Models
description: >-
  [CVPR 2026][多模态][音视频推理] 提出 AV-SpeakerBench，一个包含 3212 道选择题的以说话人为中心的音视频推理基准，揭示了 Gemini 2.5 Pro 在音视频融合方面的优势以及开源模型在说话人推理上的显著不足。
tags:
  - CVPR 2026
  - 多模态
  - 多模态VLM
  - 说话人中心基准
  - 多模态融合
  - 语音理解
  - 时序定位
---

# See, Hear, and Understand: Benchmarking Audiovisual Human Speech Understanding in Multimodal Large Language Models

**会议**: CVPR 2026  
**arXiv**: [2512.02231](https://arxiv.org/abs/2512.02231)  
**代码**: [https://plnguyen2908.github.io/AV-SpeakerBench-project-page/](https://plnguyen2908.github.io/AV-SpeakerBench-project-page/)  
**领域**: 多模态VLM / 音视频理解  
**关键词**: 音视频推理, 说话人中心基准, 多模态融合, 语音理解, 时序定位

## 一句话总结

提出 AV-SpeakerBench，一个包含 3212 道选择题的以说话人为中心的音视频推理基准，揭示了 Gemini 2.5 Pro 在音视频融合方面的优势以及开源模型在说话人推理上的显著不足。

## 研究背景与动机

1. **领域现状**：多模态大模型已从图像-文本扩展到视频和音频理解，开始追求统一处理视觉、音频和语言的能力。
2. **现有痛点**：现有视频基准中很多问题仅靠视觉即可解答（如 Video-MME），音视频基准要么聚焦非语音声事件（AVQA），要么做粗粒度分类（VGGSounder），不评估精细的说话人推理。
3. **核心矛盾**：没有基准系统评估模型是否能联合确定"谁在说话、说了什么、何时说的"。
4. **本文目标**：构建以说话人为核心推理单元的音视频推理基准。
5. **切入角度**：融合驱动的问题设计，将音视频依赖嵌入问题和选项的语义中。
6. **核心 idea**：每个问题都需要跨模态融合才能回答——例如将口头短语与可见说话人关联、根据视觉事件定位语音。

## 方法详解

### 整体框架

IRB 批准的基准，2051 个视频片段，3212 道四选一选择题，覆盖 12 个任务类型。数据来自 YouTube（电影片段、游戏节目、街头采访等）。

### 关键设计

1. **以说话人为中心的任务设计**:

    - 功能：将评估从场景级理解转移到以人为中心的音视频定位
    - 核心思路：12 个任务分三大类：说话人中心（检测、识别、计数）、视觉中心（属性、活动、计数识别）、音频中心（识别、时长、音高、语速、强度、计数）。每个任务至少 200 道验证题。
    - 设计动机：涵盖多种说话人推理模式，从基础感知到时序推理。

2. **融合驱动的问题设计**:

    - 功能：确保每道题需要真正的音视频融合
    - 核心思路：音视频依赖嵌入问题语义中：(1) 口语短语与可见身份关联；(2) 视觉事件定位语音；(3) 多说话人场景中结合音视频线索。干扰项来自同一片段中的实体/事件。
    - 设计动机：避免模型仅靠单一模态即可回答。

3. **专家策划标注管道**:

    - 功能：确保标注质量和跨模态有效性
    - 核心思路：标注者为经验丰富的研究人员而非众包工人。多阶段精炼：(1) 独立研究人员初审；(2) 语言模型润色；(3) 至少两位额外研究人员终审。过滤歧义和可单模态解决的样本。
    - 设计动机：确保所有保留问题展现时序敏感性和说话人定位。

### 损失函数 / 训练策略

纯评测基准，无训练。人类基线由研究生完成。

## 实验关键数据

### 主实验

| 模型 | 说话人中心 | 视觉中心 | 音频中心 | 总体 |
|------|-----------|---------|---------|------|
| Gemini 2.5 Pro | 76.7 | 71.5 | 72.9 | 73.0 |
| Qwen3-Omni-30B | 54.5 | 51.8 | 53.7 | 54.1 |
| Gemini 2.0 Flash | 57.2 | 54.8 | 51.5 | 53.2 |
| 人类 | 94.4 | 93.5 | 92.3 | 93.7 |

### 消融实验

| 配置 | Gemini 2.5 Pro | Qwen3-Omni | 说明 |
|------|---------------|------------|------|
| 仅视觉 | ~55-60% | ~50-55% | 基础视觉能力 |
| 音频+视觉 | ~70-80% | ~50-55% | Gemini 提升 10-20pp |
| 音频增益 | +10-20pp | 0~负 | 核心融合能力差距 |

### 关键发现

- Gemini 2.5 Pro 音频输入稳定提升 10-20pp，Qwen3-Omni 增益微弱甚至为负
- 错误分析：音频感知错误和时序定位错误是主要失败模式
- 可见人数增加时所有模型准确率下降，多人场景是主要挑战
- 早期开源音视频模型（Video-LLaMA、PandaGPT）表现接近随机

## 亮点与洞察

- **融合能力诊断**：模态消融实验清晰展示了不同模型的融合能力差距
- **错误类型学**：系统化分类了视觉/音频感知错误、跨模态归因错误、时序定位错误等
- **设计合理性**：承认强模型可能通过视觉线索（嘴型运动）部分回答问题，这是合理能力而非缺陷

## 局限与展望

- 部分任务中强视觉模型可仅靠视觉回答，虽承认为合理能力但降低了音频必要性
- 视频均来自 YouTube，场景以影视为主
- 目前评估覆盖的开源音视频模型较少

## 相关工作与启发

- **vs Video-MME**: Video-MME 问题多可仅靠视觉解答，AV-SpeakerBench 强制音视频融合
- **vs WorldSense**: WorldSense 侧重场景与声学匹配，AV-SpeakerBench 聚焦说话人与语音绑定

## 评分

- 新颖性: ⭐⭐⭐⭐ 说话人中心的音视频推理评测填补空白
- 实验充分度: ⭐⭐⭐⭐⭐ 覆盖开源和闭源模型，模态消融+错误分析深入
- 写作质量: ⭐⭐⭐⭐ 结构清晰，案例分析生动
- 价值: ⭐⭐⭐⭐⭐ 为音视频融合模型发展提供了急需的诊断工具

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Purify-then-Align: Towards Robust Human Sensing under Modality Missing with Knowledge Distillation from Noisy Multimodal Teacher](purify-then-align_towards_robust_human_sensing_under_modality_missing_with_knowl.md)
- [\[CVPR 2026\] Towards Multimodal Domain Generalization with Few Labels](towards_multimodal_domain_generalization_with_few_labels.md)
- [\[CVPR 2026\] Mixture of States (MoS): Routing Token-Level Dynamics for Multimodal Generation](mos_mixture_of_states_multimodal_generation.md)
- [\[CVPR 2026\] Venus: Benchmarking and Empowering Multimodal Large Language Models for Aesthetic Guidance and Cropping](venus_benchmarking_and_empowering_multimodal_large_language_models_for_aesthetic.md)
- [\[CVPR 2026\] GraphVLM: Benchmarking Vision Language Models for Multimodal Graph Learning](graphvlm_benchmarking_vision_language_models_for_multimodal_graph_learning.md)

</div>

<!-- RELATED:END -->
