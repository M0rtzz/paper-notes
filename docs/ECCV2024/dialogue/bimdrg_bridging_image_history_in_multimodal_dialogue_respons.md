---
title: >-
  [论文解读] BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation
description: >-
  [ECCV 2024][对话系统] 在多模态对话响应生成（MDRG）中，通过视觉交叉注意力层+注意力掩码调制桥接图像历史到文本回复，通过Citation Module标注跨轮重复物体并结合定制化T2I模型生成一致的图像回复。
tags:
  - ECCV 2024
  - 对话系统
  - image grounding
  - image consistency
  - citation module
  - customized text-to-image
---

# BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation

**会议**: ECCV 2024  
**arXiv**: [2408.05926](https://arxiv.org/abs/2408.05926)  
**代码**: [GitHub](https://github.com/hee-suk-yoon/BI-MDRG)  
**领域**: 对话系统  
**关键词**: multimodal dialogue, image grounding, image consistency, citation module, customized text-to-image

## 一句话总结

在多模态对话响应生成（MDRG）中，通过视觉交叉注意力层+注意力掩码调制桥接图像历史到文本回复，通过Citation Module标注跨轮重复物体并结合定制化T2I模型生成一致的图像回复。

## 研究背景与动机

**领域现状**：多模态对话响应生成（MDRG）要求模型根据对话上下文生成文本+图像混合回复。由于缺乏大规模多模态对话数据，现有方法（如Divter）将文本作为图像的中间表示——先用文本描述图像，再用T2I模型生成图像。

**现有痛点**：

1. **文本回复缺乏图像接地**：将图像转为文本描述会丢失关键视觉信息，导致回复无法基于图像内容（如"你的狗是什么品种？"无法从"狗吃西瓜"的文本描述中推断）

2. **图像回复缺乏物体一致性**：跨轮次生成的图像中同一物体外观不一致，因为模型缺乏跨轮次的视觉记忆

3. 现有评测缺少图像一致性的标准数据集

**核心矛盾**：文本中间表示在解耦训练复杂度的同时，牺牲了视觉信息的直接利用。

## 方法详解

### 整体框架

对话上下文 → Visual Encoder提取图像特征 → Textual Dialogue Response Generator（带视觉交叉注意力）→ 输出文本回复 + citation标注的图像描述 → 定制化T2I模型生成一致图像回复。

### 关键设计

1. **视觉交叉注意力 + 注意力掩码调制（Bridging Image to Text）**

    - 在decoder-only LM的每个transformer层之间插入视觉交叉注意力层（Flamingo风格），直接关注Visual Encoder输出的图像特征
    - 关键创新——多模态因果注意力掩码调制：阻止文本回复看到之前轮次的文本图像描述，强迫模型通过交叉注意力从原始图像特征获取视觉信息
    - 设计动机：防止模型"偷懒"依赖文本描述而忽视真实图像内容

2. **Citation Module（Bridging Image to Image Description）**

    - 流程：POS标注（spaCy）→ 开放集检测（GroundingDINO）→ 分割（SAM）→ 特征提取（DINOv2）→ 余弦相似度聚类（阈值τ=0.6）
    - 为每个关键物体添加 [cite]ID[/cite] 标签标注其cluster归属
    - 例："a dog running" → "a dog[cite]0[/cite] running"
    - 推理时利用citation标签将同一物体的历史图像送入定制化T2I模型保持一致性
    - 完全基于现成组件，无需额外训练

### 损失函数 / 训练策略

- 两阶段训练：第一阶段训练语言模型层（batch=256, max_len=256），第二阶段联合训练Visual Encoder感知重采样器和视觉交叉注意力层（batch=128, max_len=512）
- 损失函数：标准自回归下一个token预测的负对数似然
- 底座模型：OpenFlamingo 4B + BLIP2-flan-t5-xl（图像描述生成）
- 定制T2I模型：有citation时使用BLIP-Diffusion，无citation时使用Stable Diffusion 2.1
- 训练硬件：16× NVIDIA A100 80GB

## 实验关键数据

### 主实验

**PhotoChat 数据集**

| 模型 | Intent F1 | IS | Desc B1 | Desc R-L | Text B1 | Text R-L |
|------|-----------|----|---------|----------|---------|----------|
| Divter | 56.2 | 15.8 | 15.1 | 15.8 | 6.52 | 5.69 |
| Divter_LLM (3B) | 54.1 | 16.1 | 41.3 | 41.6 | 11.4 | 10.8 |
| **BI-MDRG** | **55.7** | **16.7** | **42.1** | **42.5** | **12.4** | **11.2** |

**MMDialog 数据集**

| 模型 | Intent F1 | IS | Text B1 | Text B2 | Text R1 | Text R-L |
|------|-----------|----|---------|---------|---------|----------|
| Divter | 71.8 | 20.5 | 9.44 | 7.45 | - | 11.2 |
| MiniGPT5 (9B) | - | 20.2 | 29.1 | 19.5 | - | 12.1 |
| Divter_LLM (3B) | 67.3 | 21.0 | 21.3 | 16.2 | 20.4 | 19.4 |
| **BI-MDRG** | **70.5** | **22.4** | **27.6** | **23.5** | **25.7** | **24.8** |

### 消融实验

| 组件 | MMDialog Text B1 | MMDialog Text R-L |
|------|-----------------|-------------------|
| Divter_LLM (baseline) | 21.3 | 19.4 |
| + Visual Cross-Attn | 24.1 | 22.3 |
| + Attention Mask Mod. | 26.2 | 23.9 |
| + Citation Module | **27.6** | **24.8** |

### 关键发现

- BI-MDRG在MMDialog上文本回复质量（B1: 27.6）大幅超越Divter_LLM（21.3），4B规模下与9B的MiniGPT5可比
- 注意力掩码调制贡献显著——强迫模型从图像而非文本描述获取视觉信息
- IS从21.0提升至22.4，说明图像回复质量也有提升
- 创建了MDIC数据集（300个标注对话）填补物体一致性评测空白

## 亮点与洞察

- 注意力掩码调制是一种巧妙的训练技巧：通过遮蔽文本描述迫使模型学习直接从图像特征提取信息
- Citation Module完全基于现成组件（GroundingDINO + SAM + DINOv2），zero-shot即可工作
- 桥接图像历史到文本回复和图像回复是两个解耦但互补的设计
- MDIC数据集的创建为多模态对话图像一致性评估提供了首个标准

## 局限性 / 可改进方向

- Citation Module依赖POS标注找到"关键物体"，对多物体或复杂场景可能遗漏
- 定制化T2I的物体一致性仍有限，特别是对细粒度外观
- 仅覆盖英文多模态对话，未测试多语种场景
- 生成图像质量评估仅用IS指标，缺少FID或人工评估
- 整个pipeline较为复杂（多个模块串联），端到端方案可能更优

## 相关工作与启发

- **vs Divter**：Divter完全依赖文本中间表示，BI-MDRG通过视觉交叉注意力直接利用图像特征
- **vs MiniGPT5**：MiniGPT5用更大模型（9B VLM）但BI-MDRG在4B规模下通过图像历史桥接获得可比效果
- **vs Flamingo**：借鉴了Flamingo的视觉交叉注意力架构，创新在于注意力掩码调制
- **vs DreamBooth**：Citation Module将定制化T2I从用户指定扩展到对话上下文自动追踪

## 评分

- 新颖性: ⭐⭐⭐ 注意力掩码调制和Citation Module组合有创意，但各组件基于现有方法
- 实验充分度: ⭐⭐⭐ 两个标准数据集+自建MDIC数据集，但缺少人工评估
- 写作质量: ⭐⭐⭐⭐ 问题动机清晰，架构图详尽
- 价值: ⭐⭐⭐ 对多模态对话中图像历史利用的系统性探索有参考价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis](a_multimodal_benchmark_dataset_and_model_for_crop_disease_di.md)
- [\[ICLR 2026\] AQuA: Toward Strategic Response Generation for Ambiguous Visual Questions](../../ICLR2026/dialogue/aqua_toward_strategic_response_generation_for_ambiguous_visual_questions.md)
- [\[ACL 2025\] UniConv: Unifying Retrieval and Response Generation for Large Language Models in Conversations](../../ACL2025/dialogue/uniconv_retrieval_response_gen.md)
- [\[NeurIPS 2025\] Bridging Human and LLM Judgments: Understanding and Narrowing the Gap](../../NeurIPS2025/dialogue/bridging_human_and_llm_judgments_understanding_and_narrowing_the_gap.md)
- [\[ACL 2026\] Author-in-the-Loop Response Generation and Evaluation: Integrating Author Expertise and Intent in Responses to Peer Review](../../ACL2026/dialogue/author-in-the-loop_response_generation_and_evaluation_integrating_author_experti.md)

</div>

<!-- RELATED:END -->
