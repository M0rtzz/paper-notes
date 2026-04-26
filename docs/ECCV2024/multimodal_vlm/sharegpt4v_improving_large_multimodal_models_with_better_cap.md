---
title: >-
  [论文解读] ShareGPT4V: Improving Large Multi-modal Models with Better Captions
description: >-
  [ECCV 2024][多模态][高质量图文数据] 指出现有LMM训练中低质量caption是模态对齐的瓶颈，构建了1.2M高质量详细描述的ShareGPT4V数据集（100K来自GPT4-Vision + 1.2M来自训练得到的Share-Captioner），在预训练和SFT两阶段使用该数据，以简单架构的7B模型在11个基准中9个取得最优。
tags:
  - ECCV 2024
  - 多模态
  - 高质量图文数据
  - GPT4-Vision
  - 模态对齐
  - 大规模caption
  - LMM预训练
---

# ShareGPT4V: Improving Large Multi-modal Models with Better Captions

**会议**: ECCV 2024  
**arXiv**: [2311.12793](https://arxiv.org/abs/2311.12793)  
**代码**: https://ShareGPT4V.github.io (有)  
**领域**: 多模态VLM  
**关键词**: 高质量图文数据, GPT4-Vision, 模态对齐, 大规模caption, LMM预训练

## 一句话总结
指出现有LMM训练中低质量caption是模态对齐的瓶颈，构建了1.2M高质量详细描述的ShareGPT4V数据集（100K来自GPT4-Vision + 1.2M来自训练得到的Share-Captioner），在预训练和SFT两阶段使用该数据，以简单架构的7B模型在11个基准中9个取得最优。

## 研究背景与动机
1. **领域现状**：当前LMM遵循预训练（大规模图文对做模态对齐）+ SFT（指令微调增强多模态能力）的两阶段范式。LLaVA-1.5、Qwen-VL-Chat等模型通过架构和数据多样性的改进不断提升。
2. **现有痛点**：(1) 主流图文数据集（如COCO-Caption）的caption过于简短（平均52字符），只描述主体物体，信息损失严重；(2) LLaVA-Instruct让GPT4"想象"图片内容，但GPT4并未真正"看到"图片，导致描述中有hallucination；(3) 现有预训练数据的BLIP caption质量低（平均54字符），视觉编码器的丰富信息被低质量文本浪费。
3. **核心矛盾**：视觉模态天然信息丰富、语义细粒度，但配对的文本监督信号过于简陋。这种信息不对等导致模态对齐是"次优"的。
4. **本文要解决什么？** (1) 证明高质量caption对LMM性能的关键作用；(2) 大规模收集高质量详细描述；(3) 在预训练和SFT阶段充分利用高质量数据。
5. **切入角度**：用最先进的GPT4-Vision直接看图生成描述（而非让语言模型"想象"），再训练Share-Captioner复制这种能力并扩展规模。
6. **核心idea一句话**：用GPT4-Vision生成100K高质量种子caption，训练Share-Captioner扩展到1.2M，在简单架构下通过数据质量（而非模型复杂度）驱动LMM性能提升。

## 方法详解

### 整体框架
分两阶段构建数据集：(1) GPT4-Vision Captioning：从多源图像中选100K张，设计数据特定prompt让GPT4-Vision生成详细描述（平均942字符）；(2) Share-Captioner训练：用100K caption微调一个captioner模型，再用它为1.2M图像生成高质量caption。最终在ShareGPT4V-7B模型的预训练和SFT阶段使用这些数据。

### 关键设计

1. **数据特定的Prompt设计**：
    - 做什么：为不同来源的图像设计针对性prompt，确保GPT4-Vision生成最相关的描述
    - 核心思路：基础prompt（描述物体属性、外观、空间关系）+ 数据特定prompt（如地标图要求提及名称和地理位置、名人图要求识别身份）+ 可选美学prompt
    - 设计动机：不同来源图像的信息侧重不同，通用prompt无法挖掘领域知识（如仅描述"高铁塔"而非识别为"埃菲尔铁塔"）

2. **Share-Captioner训练**：
    - 做什么：训练一个可以复制GPT4-Vision描述质量的通用captioner
    - 核心思路：在100K高质量caption上微调（无需数据特定prompt的通用指令），使其学会为任意图像生成丰富描述
    - 设计动机：GPT4-Vision API成本高昂，训练本地captioner可以低成本扩展数据规模。人类评估显示Share-Captioner与GPT4-Vision质量相当（35.3% vs 38.2%偏好，26.5%相当）

3. **预训练阶段的全模型微调**：
    - 做什么：在预训练阶段同时微调视觉编码器（后半部分）、投影器和语言模型
    - 核心思路：学习率统一2e-5，前面工作通常冻结视觉编码器，但高质量caption值得解锁编码器以获得更好的对齐
    - 设计动机：低质量caption下解锁编码器可能降低视觉知识，但高质量caption下可以引导编码器生成更贴合文本细节的嵌入

### 损失函数 / 训练策略
预训练：自回归captioning loss，batch size 256，~4700步。SFT：用LLaVA-1.5的665K SFT数据，将其中23K详细描述替换为ShareGPT4V caption，冻结视觉编码器，微调投影器和LLM。

## 实验关键数据

### 主实验

| 方法 | 参数 | MME-P | MME-C | MMBench | SEED-I | MM-Vet | VQAv2 |
|------|------|-------|-------|---------|--------|--------|-------|
| LLaVA-1.5-13B | 13B | 1531.3 | 295.4 | 67.7 | 68.2 | 35.4 | 80.0 |
| Qwen-VL-Chat | 7B | 1487.5 | 360.7 | 60.6 | 58.2 | - | 78.2 |
| **ShareGPT4V-7B** | 7B | **1567.4** | **376.4** | **68.8** | **69.7** | **37.6** | **80.6** |

### 消融实验

| 预训练用ShareGPT4V-PT | SFT用ShareGPT4V | MME-P | MMBench | SEED-I |
|----------------------|----------------|-------|---------|--------|
| ✗ | ✗ | 1510.7 | 64.3 | 66.2 |
| ✗ | ✓ | 1542.1 | 66.8 | 66.7 |
| ✓ | ✗ | 1557.2 | 67.4 | 68.5 |
| ✓ | ✓ | **1567.4** | **68.8** | **69.7** |

### 关键发现
- 仅替换3.5%的SFT数据为高质量caption即可带来一致性能提升（LLaVA-1.5-13B在MME上+22.0，MMBench+1.3）
- 高质量caption在预训练阶段的提升（+46.5 MME-P）大于SFT阶段（+31.4 MME-P），说明模态对齐是更根本的瓶颈
- 对比BLIP-558K和ShareGPT4V-558K（相同图像不同caption），高质量caption在MME上提升18.2、MMBench+1.9
- 解锁视觉编码器后半部分（block 12开始）达到最优平衡——全锁或全解锁都不如
- 100K高质量数据即可带来显著提升，1000K后趋于饱和

## 亮点与洞察
- **"数据质量 > 模型复杂度"的有力证据**：7B简单架构通过数据质量提升打败了很多更大更复杂的模型，对当前LMM社区过度关注架构设计和模型规模是一个重要提醒。
- **GPT4-Vision作为数据引擎的方法论**：用最强模型生成种子数据→训练本地模型→扩展数据规模——这个pipeline可以复用到任何需要高质量标注的场景。
- **预训练caption质量的重要性首次被系统验证**：之前的工作主要关注SFT阶段的数据质量，本文证明预训练阶段的数据质量同样甚至更加关键。

## 局限性 / 可改进方向
- Share-Captioner的质量仍不及GPT4-Vision（35.3% vs 38.2%偏好比），更强的蒸馏方法可能缩小差距
- 仅验证7B规模，更大模型是否同样受益待确认
- 预训练数据scaling在1M后饱和，可能需要更多样化的图像源而非单纯扩量
- 美学评估等维度的描述可能过于主观，对下游任务的贡献存疑

## 相关工作与启发
- **vs LLaVA-Instruct**：LLaVA让GPT4"想象"图片生成描述，但GPT4未看到图片导致hallucination。ShareGPT4V直接用GPT4-Vision看图描述，更准确。
- **vs BLIP/LaCLIP**：这些方法通过过滤或重写来改进caption，但受限于原始caption的低质量天花板。ShareGPT4V从源头重新生成。
- **vs Qwen-VL-Chat**：Qwen-VL使用1.4B训练样本，ShareGPT4V-7B仅用1.2M高质量数据就在MME总分上超过95.6分，验证了质量胜过数量。

## 补充说明
- 100K种子caption来源多样：50K COCO + 30K LCS + 20K SAM + 500 TextCaps + 500 WikiArt + 1K web
- 平均caption长度：ShareGPT4V 942字符 vs COCO-Caption 52字符 vs BLIP 54字符
- Share-Captioner训练在44 A100 GPU-days内完成1.2M caption生成
- 预训练时选择性微调ViT后半部分（block 12起）达到最优，全锁或全解锁均不如
- 100K高质量数据即可产生显著提升，数据量在1000K后趋于饱和
- 词汇组成分析显示Share-Captioner与GPT4-Vision在名词/动词/形容词比例上高度一致
- 人类评估中10位志愿者对100个样本评判，Share-Captioner与GPT4-Vision几乎平分秋色
- 涵盖世界知识、物体属性、空间关系、美学评估四大维度的描述

## 评分
- 新颖性: ⭐⭐⭐⭐ 数据质量驱动LMM的理念虽不复杂但极有洞察力，Share-Captioner pipeline实用
- 实验充分度: ⭐⭐⭐⭐⭐ 11个基准、多模型验证、详细消融（数据量、ViT block数、caption质量对比）
- 写作质量: ⭐⭐⭐⭐ 数据构建流程清晰，对比论证有说服力
- 价值: ⭐⭐⭐⭐⭐ ShareGPT4V数据集和Share-Captioner是社区重要资源

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] m&m's: A Benchmark to Evaluate Tool-Use for Multi-step Multi-modal Tasks](m_ampmaposs_a_benchmark_to_evaluate_tool-use_for_multi-step_multi-modal_tasks.md)
- [\[ECCV 2024\] MMBench: Is Your Multi-modal Model an All-Around Player?](mmbench_is_your_multimodal_model_an_allaround_player.md)
- [\[ECCV 2024\] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?](mathverse_does_your_multimodal_llm_truly_see_the_diagrams_in.md)
- [\[ECCV 2024\] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)

<!-- RELATED:END -->
