---
title: >-
  [论文解读] SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant
description: >-
  [ECCV 2024][多模态][视觉自提问] 提出SQ-LLaVA，首次将指令数据中问题作为额外学习目标，训练MLLM不仅回答问题还学会"自问"，通过视觉自提问（visual self-questioning）任务挖掘指令数据中被忽视的问题上下文信息，配合原型提取器和LoRA微调，在10个VQA基准中9个超越基线。
tags:
  - ECCV 2024
  - 多模态
  - 视觉自提问
  - 指令微调
  - 视觉语言对齐
  - 原型提取器
  - 多模态VLM
---

# SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant

**会议**: ECCV 2024  
**arXiv**: [2403.11299](https://arxiv.org/abs/2403.11299)  
**代码**: [https://github.com/heliossun/SQ-LLaVA](https://github.com/heliossun/SQ-LLaVA)  
**领域**: 多模态VLM  
**关键词**: 视觉自提问, 指令微调, 视觉语言对齐, 原型提取器, LoRA

## 一句话总结

提出SQ-LLaVA，首次将指令数据中问题作为额外学习目标，训练MLLM不仅回答问题还学会"自问"，通过视觉自提问（visual self-questioning）任务挖掘指令数据中被忽视的问题上下文信息，配合原型提取器和LoRA微调，在10个VQA基准中9个超越基线。

## 研究背景与动机

1. **领域现状**：LLaVA系列方法通过视觉指令微调实现了强大的多模态理解能力，模型由预训练视觉编码器（CLIP-ViT）、投影器和LLM组成。
2. **现有痛点**：(a) 视觉编码器和LLM之间的模态鸿沟是整个网络的瓶颈；(b) 现有改进方案（更强的视觉编码器、更多数据、全量微调）要么成本高、要么数据获取困难；(c) 视觉指令数据中的问题包含丰富的图像相关信息，但训练时仅被当作输入条件，其语义内容未被利用。
3. **核心矛盾**：图像蕴含丰富信息（颜色、上下文、物体关系），但现有指令数据仅捕获一小部分，且问题中与图像高度相关的语义信息被浪费。
4. **本文要解决什么**：在不收集额外数据的前提下，通过更充分地利用现有指令数据中的信息来提升视觉语言对齐。
5. **切入角度**：从信息论角度观察到——问题的CLIPScore平均值(μq=0.184)高于答案(μa=0.183)，说明问题比答案包含更多图像相关信息。
6. **核心idea一句话**：训练模型学习"提问"而非仅"回答"，通过自监督方式挖掘指令数据中问题的丰富视觉语义。

## 方法详解

### 整体框架

SQ-LLaVA在LLaVA架构上增加两个核心设计：(1) 视觉自提问指令——引入[vusr] token让模型学习根据图像生成问题；(2) 原型提取器——通过EM聚类增强视觉表征。ViT-LoRA和LLM-LoRA实现参数高效的联合优化。

### 关键设计

**1. 视觉自提问指令设计**
- 做什么：定义新的special token [vusr]作为"提问"指令，让LLM预测图像相关问题而非答案
- 核心思路：在多轮对话数据中，以δ=0.5的概率将[usr]替换为[vusr]，将原来的问题Xq作为learning target，保持答案Xa也是target——模型同时学习提问和回答
- 设计动机：提问需要比回答更深的理解和背景知识（"能问出好问题说明真的懂了"），自提问迫使模型建立更深的图像-语言关联

**2. 原型提取器(Prototype Extractor)**
- 做什么：从视觉token中提取语义聚类信息来增强视觉表征
- 核心思路：
    - 随机初始化K=256个聚类中心C
    - 2轮EM迭代：E步计算软分配矩阵M=softmax(q(C)·k(Zv)^T)，M步更新中心C=M·v(Zv)
    - 将聚类信息反馈到每个视觉token：Zv(i) += z(1/K × Σ Sc(Cj, Zv(i)) × Cj)
- 设计动机：聚类中心捕获图像patch的共同语义（如"草地"、"狗"），将这种高级语义分布到每个token，增加上下文感知能力

**3. LoRA双路径微调**
- 做什么：在ViT和LLM中同时插入LoRA模块
- 核心思路：ViT-LoRA (rank=32, α=64) + LLM-LoRA (rank=128, α=256)，学习率不同（LoRA 2e-4, 其他2e-5）
- 设计动机：ViT-LoRA使视觉编码器适应新的对齐目标，LLM-LoRA使语言模型适应提问任务，双路径比仅调LLM更有效

**4. 训练流程**
- 做什么：两阶段训练
- Stage 1 预训练：冻结ViT和LLM，训练原型提取器和投影器W，学习基本的视觉-语言对齐
- Stage 2 微调：冻结ViT和LLM的原始权重，训练LoRA + 原型提取器 + 投影器，包含自提问和回答双任务

### 损失函数 / 训练策略

- 自提问损失：-log p(Hq^(j+1) | Hv, Hc^(1:j)) — 给定图像和上下文，预测下一个问题token
- 回答损失：-log p(Ha^(j+1) | Hv, Hc^(1:j), Hq^(j+1)) — 给定图像、上下文和问题，预测答案
- 预训练/微调数据都来自LLaVA和ShareGPT4V
- 全局batch size：预训练256，微调128
- 优化器：AdamW，lr=2e-3(预训练)，lr=2e-4/2e-5(微调)

## 实验关键数据

### 主实验

| 模型(7B) | VQAv2 | GQA | VizWiz | SQA-I | TextVQA | POPE | MM-Vet | LLaVA-W | MMB | MMB-CN |
|----------|-------|-----|--------|-------|---------|------|--------|---------|-----|--------|
| LLaVA-v1.5 | 78.5 | 62.0 | 50.0 | 66.8 | 58.2 | 85.9 | 30.5 | 63.4 | 64.3 | 58.3 |
| ShareGPT4V | 80.6 | 63.3 | 57.2 | 68.4 | 60.4 | 86.8 | 37.6 | 72.6 | 68.8 | 62.2 |
| **SQ-LLaVA** | **79.2** | **62.8** | **54.0** | **68.9** | **58.6** | **87.7** | **32.5** | **66.3** | **66.2** | **58.1** |
| **SQ-LLaVA*** | **80.3** | **63.7** | **55.3** | - | - | - | - | - | - | - |

*SQ-LLaVA在LLaVA数据上9/10超越LLaVA-v1.5，SQ-LLaVA*在ShareGPT4V数据上6/10超越ShareGPT4V*

### 消融实验

| 组件 | 效果 |
|------|------|
| 仅回答训练(baseline) | LLaVA-v1.5基线 |
| +自提问 | 多数基准提升 |
| +原型提取器 | 进一步提升 |
| +ViT-LoRA | 再提升 |
| 全部(SQ-LLaVA) | 最优 |

### 关键发现

1. **自提问确实有效**：在不收集新数据的情况下仅通过训练目标的改变就能带来稳定提升，验证了问题中的语义信息未被充分利用
2. SQ-LLaVA生成的问题**比GPT-4V更多样化**——因为它从大量不同格式的问题中学到了多样的提问模式
3. 在零样本图像描述任务中，SQ-LLaVA也有提升，说明自提问改善了整体视觉理解而非仅VQA能力
4. 原型提取器的聚类粒度K=256效果最佳，过大或过小都不理想
5. 自提问比例δ=0.5效果最好——太多自提问会喧宾夺主影响回答能力

## 亮点与洞察

- **观察的敏锐性**：从CLIPScore分布发现问题比答案更贴近图像——这个看似微小的统计差异揭示了被忽视的学习信号
- **"学会提问"的教育学直觉**：认知科学中，能问出好问题是深度理解的标志，将这一直觉引入MLLM训练是独特视角
- **零成本数据增广**：不需要收集新数据，仅改变训练目标就能改善性能——这是最高效的改进路线
- **原型提取器的轻量高效**：仅2轮EM迭代+一个线性层，引入极少参数但有效增强视觉表征

## 局限性 / 可改进方向

1. 自提问的质量受原始指令数据中问题质量的限制——如果原始问题就很简单，自提问学到的也有限
2. 当前仅用0.5概率随机替换问题为学习目标，更智能的选择策略（如选择高CLIPScore的问题）可能更好
3. 在更大模型规模（65B+）上的效果未验证
4. 自提问能力的实际应用场景（如主动学习、对话引导）尚未探索
5. 原型提取器的聚类过程在每个前向传播中进行，增加了一定计算开销

## 相关工作与启发

- **LLaVA/LLaVA-v1.5**：基础架构，SQ-LLaVA证明了在好架构上训练策略改进的价值
- **ShareGPT4V**：高质量指令数据的方向，SQ-LLaVA证明了更好地利用现有数据同样有效
- **Self-Instruct**：用LLM生成指令数据，SQ-LLaVA则让模型从已有数据中学习提问
- **启发**：多模态学习中"未被利用的信号"可能到处都是——问题、错误答案、图像中的非目标区域……

## 评分

- **新颖性**: ⭐⭐⭐⭐ (自提问作为训练目标是新颖且有价值的创新)
- **技术深度**: ⭐⭐⭐⭐ (原型提取器+双LoRA的设计合理高效)
- **实验充分性**: ⭐⭐⭐⭐⭐ (10个VQA基准+4个描述基准+全面消融)
- **写作质量**: ⭐⭐⭐⭐ (图1的CLIPScore分析很有说服力)
- **影响力**: ⭐⭐⭐⭐ (为MLLM训练提供了新的信号来源)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Towards Open-ended Visual Quality Comparison](towards_open-ended_visual_quality_comparison.md)
- [\[ECCV 2024\] Robust Calibration of Large Vision-Language Adapters](robust_calibration_of_large_visionlanguage_adapters.md)
- [\[ECCV 2024\] NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](navgpt-2_unleashing_navigational_reasoning_capability_for_large_vision-language_.md)
- [\[ECCV 2024\] IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models](ivtp_instruction-guided_visual_token_pruning_for_large_vision-language_models.md)
- [\[ECCV 2024\] UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_language_models.md)

</div>

<!-- RELATED:END -->
