---
title: >-
  [论文解读] CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation
description: >-
  [CVPR 2025][LLM对齐][CAD生成] 本文提出CAD-Llama，通过分层标注流水线将参数化CAD序列转化为带语义描述的结构化代码（SPCC），并使用自适应预训练和指令微调使LLM具备从文本生成复杂参数化3D CAD模型的能力，在多个CAD任务上显著超越现有方法。
tags:
  - CVPR 2025
  - LLM对齐
  - CAD生成
  - 大语言模型
  - 参数化3D建模
  - 指令微调
  - 结构化代码
---

# CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation

**会议**: CVPR 2025  
**arXiv**: [2505.04481](https://arxiv.org/abs/2505.04481)  
**代码**: 无  
**领域**: 3D视觉  
**关键词**: CAD生成, 大语言模型, 参数化3D建模, 指令微调, 结构化代码

## 一句话总结
本文提出CAD-Llama，通过分层标注流水线将参数化CAD序列转化为带语义描述的结构化代码（SPCC），并使用自适应预训练和指令微调使LLM具备从文本生成复杂参数化3D CAD模型的能力，在多个CAD任务上显著超越现有方法。

## 研究背景与动机
1. **领域现状**：CAD生成模型日益受到关注，LLM在代码生成等任务上表现卓越，但在参数化CAD序列生成方面的探索仍不充分。
2. **现有痛点**：参数化CAD序列缺乏语义标注（设计意图和几何形状描述），LLM在预训练阶段未见过CAD参数序列，直接生成困难。现有尝试只能生成简单CAD模型，无法处理复杂文本指令。
3. **核心矛盾**：CAD序列是纯数值参数，与LLM擅长的自然语言存在巨大鸿沟；但LLM在代码生成上的成功说明，如果将CAD序列转化为类似代码的结构化格式并附带语义描述，LLM可能能够有效学习。
4. **本文目标**：构建一个完整框架，让开源LLM能够基于文本指令生成复杂的参数化3D CAD模型。
5. **切入角度**：受LLM代码生成能力的启发，将CAD序列转化为Python式代码格式，并通过VLM分层标注丰富的3D语义描述。
6. **核心idea**：分层标注流水线 + 结构化参数化CAD代码（SPCC）+ 自适应预训练 + 指令微调。

## 方法详解

### 整体框架
CAD数据集 → 分层标注流水线（VLM标注组件描述+全局描述）→ SPCC语料库构建（CAD代码+分层描述）→ 自适应预训练（相似CAD分组学习）→ 多任务指令微调（text-to-CAD、补全、描述、增删组件）→ CAD-Llama。

### 关键设计

1. **分层标注流水线（Hierarchical Annotation Pipeline）**:

    - 功能：为CAD模型生成结构化的多层次文本描述，弥合参数序列与自然语言的鸿沟。
    - 核心思路：两阶段标注——(1)组件级：对每个组件生成3D渲染图和2D草图图，送入GPT-4o生成详细描述（形状、挤出方向/长度等）；(2)全局级：生成带组件高亮透明度的轮廓图，GPT-4o生成抽象概述、详细描述（含组件间空间关系和装配过程）和每个组件的短名称。按复杂度分5级，每级提供50个高质量示例，使用两样本提示减少幻觉。
    - 设计动机：单一提示无法同时捕获细粒度几何属性和组件间关系。分层标注让每层专注于不同粒度的信息。

2. **结构化参数化CAD代码（SPCC）**:

    - 功能：将CAD参数序列转化为LLM可理解的类Python代码格式，并嵌入分层语义描述。
    - 核心思路：每个草图表示为循环列表（loop），每个循环调用Line/Arc/Circle方法；挤出操作引用对应草图。坐标使用8位量化参数，起点重置为(0,0)。SPCC = 全局描述（抽象+详细）+ 组件描述 + CAD代码。还包含仅抽象描述的版本，使模型能处理不同详细程度的文本输入。
    - 设计动机：LLM在代码生成上有大量预训练知识，代码格式比原始参数序列更接近LLM的能力范围。

3. **自适应预训练与指令微调**:

    - 功能：使LLM具备CAD建模能力，并适配多种下游任务。
    - 核心思路：(1)自适应预训练：使用CLIP对CAD模型图像编码，基于余弦相似度将相似CAD分组到同一上下文中学习，使模型捕捉相似模型间的细微差异；(2)指令微调：构建6种任务的指令数据集——text-to-CAD、补全、描述（caption）、添加组件、删除组件、及其SPCC增强版本。添加/删除任务通过GPT-4o判断可删除组件的逻辑合理性。
    - 设计动机：随机拼接预训练数据效率低，相似CAD分组让模型更高效学习参数差异。多任务指令微调使模型能适配从设计到迭代优化的完整CAD工作流。

### 损失函数 / 训练策略
基于LLaMA3-8B。自适应预训练使用标准语言模型损失（next token prediction）。指令微调使用标准SFT损失。添加/删除任务使用GPT-4o生成指令并验证逻辑合理性。坐标使用8位量化参数表示，起点重置为(0,0)，每个草图表示为循环列表调用Line/Arc/Circle方法。

## 实验关键数据

### 主实验

| 方法 | 有效率(%) | Coverage(%) | MMD↓ | JSD↓ |
|------|---------|------------|------|------|
| DeepCAD | 78.3 | 58.2 | - | - |
| Text2CAD | 82.1 | 61.5 | - | - |
| GPT-4 (zero-shot) | 45.2 | 32.1 | - | - |
| LLaMA3 (zero-shot) | 28.6 | 18.4 | - | - |
| **CAD-Llama-PT** | **89.7** | **72.3** | - | - |
| **CAD-Llama-INS** | **93.5** | **78.6** | - | - |

### 消融实验

| 配置 | 有效率(%) | 说明 |
|------|---------|------|
| Full CAD-Llama-INS | 93.5 | 完整模型 |
| w/o SPCC (纯代码) | 83.2 | 语义描述贡献+10.3% |
| w/o 分层标注 | 86.8 | 全局描述贡献+6.7% |
| w/o 自适应预训练 | 88.1 | 分组学习贡献+5.4% |
| w/o 指令微调 | 89.7 | 指令微调贡献+3.8% |

### 关键发现
- CAD-Llama能生成比现有方法更复杂的多组件CAD模型。
- SPCC中的语义描述对LLM理解3D结构至关重要——去掉描述后有效率下降超10%。
- 自适应预训练的相似分组策略显著提升了学习效率。
- 在SPCC增强的编辑任务上，Addition*的ACCcmd从79.41%提升至84.89%(+5.48%)，Deletion*的EM从81.93%提升至89.55%(+7.62%)。GPT-4在Deletion*任务上凭借自然语言推理能力达到90.41%（最高），但在需要生成CAD参数的Addition*上仍落后于CAD-Llama。
- CAD表示方式消融：SPCC(代码+分层描述)的ACCcmd=80.41%，SPCS(序列+分层描述)=73.13%，SDCC(代码+单描述)=42.62%，SDCS(序列+单描述)=39.17%。分层描述比单一描述贡献+30%，代码格式比原始序列贡献+7%。
- 首次展示LLM在复杂文本指令下生成专业参数化3D CAD模型的能力。

## 亮点与洞察
- **代码格式的巧妙选择**：将CAD序列转化为类Python代码，充分利用了LLM在代码生成上的预训练优势。
- **分层标注的系统性**：组件级+全局级的分层标注确保了局部细节和全局结构的完整描述。按复杂度分5级标注，每级50个高质量示例，使用两样本提示减少幻觉。
- **可迁移到其他领域**：分层标注+结构化代码表示的框架可迁移到建筑设计、电路设计等其他参数化设计领域。
- **CAD-Llama-INS平均分63.58%，超越GPT-4的47.88%达+15.7%，超越LLaMA3/Mistral约+30%，在Caption任务的BLEU@4上达13.88（GPT-4仅3.39），Completion任务ACCcmd达73.87%（GPT-4仅51.18%）。**

## 局限与展望
- 依赖GPT-4o进行标注，标注成本较高。
- 当前仅支持2D草图+挤出的CAD建模方式，不支持更复杂的3D操作。
- 生成的CAD模型复杂度仍有上限，难以处理工业级复杂模型。
- 未探索图像到CAD的跨模态生成。
- SPCC使用8位量化参数表示坐标，可能在高精度要求的工业CAD场景中精度不足。
- 自适应预训练中的CLIP相似度分组策略可能将形状相似但语义不同的模型错误归组。
- 添加/删除组件的指令数据质量依赖GPT-4o的逻辑判断，可能在复杂装配关系中出错。
- SPCC中的分层描述覆盖抽象概述、详细描述（含组件间空间关系和装配过程）和每个组件的短名称三个层次。数据按复杂度分5级，确保标注覆盖从简单到复杂的完整CAD模型。

## 相关工作与启发
- **vs Text2CAD/CAD Translator**: 使用编码器-解码器架构，泛化能力受限；CAD-Llama利用LLM预训练知识，泛化更好。
- **vs OpenECAD**: 使用VLM+CAD内核，但未深入利用LLM的文本生成先验。
- **vs DeepCAD**: 传统自回归方法，不支持文本条件生成。

## 评分

### 实现细节
基于LLaMA3-8B，使用GPT-4o进行分层标注。
自适应预训练使用CLIP编码CAD模型图像进行相似度分组。坐标8位量化。
- 新颖性: ⭐⭐⭐⭐⭐ 首次系统性地利用LLM生成先验进行复杂CAD生成
- 实验充分度: ⭐⭐⭐⭐ 多任务评估全面，但部分指标缺乏绝对数值
- 写作质量: ⭐⭐⭐⭐ 方法描述系统，符号清晰
- 价值: ⭐⭐⭐⭐⭐ 对CAD自动生成领域有重要推动作用

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2025\] Do We Really Need Curated Malicious Data for Safety Alignment in Multi-Modal LLMs?](do_we_really_need_curated_malicious_data_for_safety_alignment_in_multi-modal_lar.md)
- [\[CVPR 2025\] Debiasing Multimodal Large Language Models via Noise-Aware Preference Optimization](debiasing_multimodal_large_language_models_via_noise-aware_preference_optimizati.md)
- [\[CVPR 2025\] Boost Your Human Image Generation Model via Direct Preference Optimization](boost_your_human_image_generation_model_via_direct_preference_optimization.md)
- [\[CVPR 2025\] Task Preference Optimization: Improving Multimodal Large Language Models with Vision Task Alignment](task_preference_optimization_improving_multimodal_large_language_models_with_vis.md)
- [\[CVPR 2025\] SymDPO: Boosting In-Context Learning of Large Multimodal Models with Symbol Demonstration Direct Preference Optimization](symdpo_boosting_in-context_learning_of_large_multimodal_models_with_symbol_demon.md)

<!-- RELATED:END -->
