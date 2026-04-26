---
title: >-
  [论文解读] CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios
description: >-
  [ECCV 2024][多模态][音视频问答] 本文提出 CAT 模型，通过设计线索聚合器（Clue Aggregator）提取问题相关的音视频细节特征、构建音视频联合指令数据集 AVinstruct、以及 AI 辅助的歧义感知 DPO 策略，显著提升多模态大语言模型在动态音视频场景中的问答能力。
tags:
  - ECCV 2024
  - 多模态
  - 音视频问答
  - 多模态大语言模型
  - 线索聚合
  - 直接偏好优化
  - 歧义消除
---

# CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios

**会议**: ECCV 2024  
**arXiv**: [2403.04640](https://arxiv.org/abs/2403.04640)  
**代码**: [GitHub](https://github.com/rikeilong/Bay-CAT)  
**领域**: 多模态视觉语言模型  
**关键词**: 音视频问答, 多模态大语言模型, 线索聚合, 直接偏好优化, 歧义消除

## 一句话总结
本文提出 CAT 模型，通过设计线索聚合器（Clue Aggregator）提取问题相关的音视频细节特征、构建音视频联合指令数据集 AVinstruct、以及 AI 辅助的歧义感知 DPO 策略，显著提升多模态大语言模型在动态音视频场景中的问答能力。

## 研究背景与动机

1. **领域现状**: 现有 MLLM（如 Video-LLaMA、ChatBridge）通过多分支独立处理音频和视频模态，然后拼接模态嵌入输入 LLM，能够响应音视频内容但存在明显缺陷。

2. **现有痛点**: (1) 音视频信息与问题关联不足——现有方法在底层未让文本信息与音视频交互，导致网络无法聚焦于问题相关细节；(2) 多模态-文本对齐困难——模型生成的响应往往含糊不清，在描述特定音视频对象时使用模糊词汇或生成大量无用文本。

3. **核心矛盾**: MLLM 在大规模多模态语料训练中难以对齐跨域数据，导致在描述动态音视频场景中的特定对象时产生歧义。

4. **本文目标**: 提升 MLLM 在 AVQA（音视频问答）任务中的表现，使模型能准确识别问题相关的视觉对象和声音，生成简洁无歧义的回答。

5. **切入角度**: 在模态桥接阶段引入问题感知机制，在训练后阶段通过偏好优化消除歧义。

6. **核心 idea**: 设计线索聚合器让问题文本在底层与音视频特征交互，并通过 DPO 让模型学会偏好无歧义的精准描述。

## 方法详解

### 整体框架
输入为视频 V 和音频 A，通过冻结的 ImageBind 编码器提取特征。模型包含三个分支：(1) 视觉投影分支生成 $x^{vid}$；(2) 音频投影分支生成 $x^{aud}$；(3) 线索聚合器提取问题相关特征生成 $x^{cue}$。三者与文本 token 合并后输入冻结的 LLaMA2-7B + LoRA。

### 关键设计

1. **线索聚合器（Clue Aggregator）**:
    - 功能: 动态提取与问题相关的音视频隐藏特征
    - 核心思路: 分两步——Step1 用感知器（Perceiver）进行问题感知定位，由正序 block $\mathcal{B}_1$ 做问题-音视频交叉注意力定位，反序 block $\mathcal{B}_2$ 巩固原始表征；Step2 用 Q-Former 架构的可学习查询向量（K=48）聚合问题感知特征
    - 设计动机: 简单线性投影无法捕获细粒度信息，且无法让文本在底层与音视频交互；视觉和音频感知器共享参数以学习潜在关联

2. **AVinstruct 音视频联合指令数据集**:
    - 功能: 提供音视频联合推理的训练数据
    - 核心思路: 从 YouTube 和 VGGSound 收集含音频的原始视频，结合 Music-AVQA 和 AVQA 的 QA 对，用 BLIP2 和 Whisper 生成描述，再用 GPT 合成问题引导的音视频描述
    - 设计动机: 现有指令数据集缺少音视频联合推理数据，导致模型无法在真实场景中同时利用视觉和听觉信息

3. **AI 辅助歧义感知 DPO（ADPO）**:
    - 功能: 重训练模型偏好无歧义响应
    - 核心思路: 先收集训练后 CAT 的歧义输出作为负样本 $y_{neg}$，用 GPT 改写为精准的正样本 $y_{pos}$；然后用 DPO loss $\mathcal{L}_{DPO}$ + SFT loss $\mathcal{L}_{SFT}$（$\lambda=0.1$）联合优化，最终损失 $\mathcal{L} = \mathcal{L}_{DPO} + \lambda \mathcal{L}_{SFT}$
    - 设计动机: 仅用提示工程无法在多样化动态场景中消除歧义，DPO 比 RLHF 更简单高效；额外的 SFT loss 在正负样本差异小时稳定训练

### 损失函数 / 训练策略
- **Stage-I 特征对齐**: 先用 Webvid 2.5M 训练视觉投影器（冻结 LLM 和音频），再用 WavCap 训练音频投影器
- **Stage-II 联合指令微调**: 在 100k 视频指令 + AVinstruct 上微调线索聚合器和 LoRA
- **Stage-III ADPO**: 仅更新 LoRA 参数（r=64, alpha=16），batch=1，lr=4e-6，β=0.1

## 实验关键数据

### 主实验

| 数据集 | 指标 | 本文 CAT | 之前SOTA | 提升 |
|--------|------|---------|----------|------|
| Music-AVQA | Overall Avg | 83.2 | VAST 80.7 | +2.5 |
| AVQA | Accuracy | 82.5 | - | SOTA |
| MSRVTT-QA | Acc / Score | 62.1 / 3.5 | VISTA 60.5 / 3.3 | +1.6 |
| ActivityNet-QA | Acc / Score | 50.2 / 3.5 | VideoChat2 49.1 / 3.3 | +1.1 |
| 视频文本生成 | 5 项 GPT 评分 | 61.6/62.0/69.8/56.2/57.8 | LLaMA-VID 61.4/61.0/72.0/51.6/52.6 | 整体更优 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 无 Clue Aggregator | 下降 ~3% | 缺少问题相关细节 |
| 无 AVinstruct | 下降显著 | 缺少音视频联合训练 |
| 无 ADPO | 生成歧义描述 | 无法消除模糊表达 |
| DPO only (无 SFT loss) | 效果不稳定 | 正负样本差异小时难以优化 |
| 不同 K 值 (查询数量) | K=48 最优 | 平衡信息量和计算成本 |

### 关键发现
- 视觉和音频感知器共享参数优于分离参数，说明音视频存在可学习的跨模态关联
- ADPO 策略使模型生成的回答更简洁精准，有效减少无用信息
- 在仅 7B 参数量下超越了多个 13B 模型
- 问题标记 \<Q\>\</Q\> 的简单设计有效帮助模型定位问题文本

## 亮点与洞察
- 将 DPO 从纯文本领域迁移到多模态场景，用 GPT 自动化正负样本构建
- 线索聚合器的双向 perceiver 设计既做问题定位又保留全局表征
- 三阶段训练策略（对齐→指令→DPO）渐进式提升模型能力
- 仅用 1 块 A100 即可完成全部训练，实践友好

## 局限与展望
- ImageBind 编码器被冻结，对音频的时间建模能力有限（音频特征仅 1×d_h）
- ADPO 依赖 GPT 进行歧义检测和改写，引入外部模型依赖
- 评估以封闭式和简单开放式 QA 为主，缺乏更复杂的多轮对话评估
- 未探索更大的 LLM backbone（如 13B/70B）的效果

## 相关工作与启发
- **vs Video-LLaMA**: Video-LLaMA 简单拼接模态，CAT 通过线索聚合器实现问题引导的特征提取
- **vs ChatBridge**: ChatBridge 用交叉注意力对齐，但缺乏歧义消除机制
- **vs VISTA-LLaMA**: VISTA 保持视觉-语言 token 距离一致，CAT 从不同角度（问题聚焦+DPO）解决

## 评分
- 新颖性: ⭐⭐⭐⭐ 线索聚合器和 ADPO 结合是新颖的音视频 QA 方案
- 实验充分度: ⭐⭐⭐⭐ 多任务多数据集评估，消融较完整
- 写作质量: ⭐⭐⭐⭐ 图示清晰，方法描述详细
- 价值: ⭐⭐⭐⭐ 对音视频多模态理解有实际价值

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Merlin: Empowering Multimodal LLMs with Foresight Minds](merlin_empowering_multimodal_llms_with_foresight_minds.md)
- [\[ECCV 2024\] REVISION: Rendering Tools Enable Spatial Fidelity in Vision-Language Models](revision_rendering_tools_enable_spatial_fidelity_in_vision-language_models.md)
- [\[ECCV 2024\] X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs](x-former_unifying_contrastive_and_reconstruction_learning_for_mllms.md)
- [\[ECCV 2024\] GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator](genixer_empowering_multimodal_large_language_model_as_a_powe.md)
- [\[ECCV 2024\] MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training](mm1_methods_analysis_and_insights_from_multimodal_llm_pre-training.md)

<!-- RELATED:END -->
