---
title: >-
  [论文解读] Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models
description: >-
  [ECCV 2024][多模态][区域视觉编码] 提出Groma，通过在视觉tokenizer中引入区域提议和区域编码机制，将定位能力嵌入图像token化过程，实现统一的referring和grounding能力，在标准基准上超越同类MLLM。
tags:
  - ECCV 2024
  - 多模态
  - 区域视觉编码
  - 视觉定位
  - Grounding MLLM
  - 区域提议
  - GPT-4V数据生成
---

# Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models

**会议**: ECCV 2024  
**arXiv**: [2404.13013](https://arxiv.org/abs/2404.13013)  
**代码**: https://groma-mllm.github.io/ (有)  
**领域**: 多模态VLM  
**关键词**: 区域视觉编码, 视觉定位, Grounding MLLM, 区域提议, GPT-4V数据生成

## 一句话总结

提出Groma，通过在视觉tokenizer中引入区域提议和区域编码机制，将定位能力嵌入图像token化过程，实现统一的referring和grounding能力，在标准基准上超越同类MLLM。

## 研究背景与动机

1. **领域现状**：MLLM在图像级理解任务上表现优异，但在需要定位能力的场景（如机器人、自动驾驶、AR）中存在短板，无法将理解与视觉上下文中的具体位置关联。
2. **现有痛点**：现有方案分两类——让LLM直接输出坐标（计算量大且不适合密集预测），或引入外部定位模块如SAM（需要两次处理图像，引入额外延迟）。
3. **核心矛盾**：定位需要高分辨率和空间感知能力，但LLM擅长语义理解而非空间定位，两者的能力边界不一致。
4. **本文要解决什么**：在不依赖外部模块的情况下，让MLLM具备高效精确的定位能力。
5. **切入角度**：受开放词汇目标检测启发，将grounding任务分解为定位（在tokenizer中完成）和识别（在LLM中完成），解耦两种能力。
6. **核心idea一句话**：将定位能力嵌入视觉token化过程，通过region token统一实现referring和grounding。

## 方法详解

### 整体框架

Groma由四个核心模块组成：(1) DINOv2图像编码器（448×448分辨率），提取全局图像特征；(2) 区域提议器（Deformable DETR），发现感兴趣区域；(3) 区域编码器，将区域提议编码为region token；(4) Vicuna-7B语言模型，处理多模态输入输出。训练分三阶段：检测预训练→对齐预训练→指令微调。

### 关键设计

**1. 图像编码器选择——DINOv2**
- 做什么：使用DINOv2-L/14（而非CLIP）作为图像编码器，输入分辨率448×448
- 核心思路：每4个相邻patch token合并为1个（2D合并优于1D），减少到256个token
- 设计动机：DINOv2在高分辨率输入和细粒度定位特征方面优于CLIP，消融实验证实了这一选择

**2. 区域提议器**
- 做什么：基于Deformable DETR的类别无关检测头，生成300个区域提议
- 核心思路：从图像编码器最后4层提取特征金字塔，二分类器评估提议质量，NMS+置信度过滤后保留top-100
- 设计动机：类别无关设计使其关注定位质量而非语义分类；利用大规模检测数据预训练（COCO、Objects365、OpenImages、V3Det + SA1B 200万子集），覆盖从物体到部件到背景的多粒度区域

**3. 区域编码器**
- 做什么：将区域提议（边界框）和用户输入区域编码为region token
- 核心思路：多尺度ROIAlign从编码器最后3层提取层次化特征，融合为统一的region token
- 设计动机：region token与底层区域语义对齐，比坐标数值或位置token更直观，LLM更容易理解

**4. 统一的Referring/Grounding格式**
- 做什么：通过proxy token (`<r1>, <r2>,...`)注册region token，实现文本输出中的区域引用
- 核心思路：grounding输出时，模型在文本中引用proxy token来定位语义对应的区域；referring输入时，用户指定区域同样编码为region token后插入指令
- 设计动机：用统一的token化机制同时处理输入（referring）和输出（grounding），无需分别设计

**5. GPT-4V辅助数据生成(Groma Instruct)**
- 做什么：构建30K visually grounded对话数据
- 核心思路：在VG图像上用SoM技术标注数字标记→GPT-4V结合视觉和文本提示生成带grounding的对话
- 设计动机：现有自由形式对话数据缺乏细粒度区域信息，难以让模型在长文本中保持grounding能力

### 损失函数 / 训练策略

三阶段训练：
- **Stage 1 检测预训练**（12 epoch）：仅训练图像编码器+区域提议器，冻结编码器，专注框定位
- **Stage 2 对齐预训练**（2 epoch）：训练MLP投影层+区域编码器，冻结其他模块，使用ShareGPT-4V-PT、RefCOCO系列、VG、Flickr30k等
- **Stage 3 指令微调**（1 epoch）：解冻LLM，使用高质量数据（LLaVA Instruct、ShareGPT-4V、Groma Instruct）

## 实验关键数据

### 主实验

| 方法 | RefCOCO val | RefCOCO+ val | RefCOCOg val | 平均 |
|------|-----------|-------------|-------------|------|
| Shikra | 87.01 | 81.60 | 82.27 | 82.93 |
| Ferret | 87.49 | 80.78 | 83.93 | 83.91 |
| MiniGPT-v2 | 88.69 | 79.97 | 84.44 | 84.29 |
| **Groma** | **89.53** | **83.90** | **86.37** | **86.24** |

### 消融实验

| 组件 | RefCOCO val | LVIS AR |
|------|-----------|---------|
| CLIP编码器 | 87.1 | - |
| DINOv2编码器 | 89.5 | +显著提升 |
| 无Groma Instruct | - | 降低 |
| 有Groma Instruct | - | 最优 |

### 关键发现

1. Groma在所有referring/grounding基准上超越同类方法，平均提升2-3个点
2. 在LVIS物体grounding评估中，Groma以超过10% AR的优势领先，展示了精确多目标定位能力
3. 解耦定位和理解的架构设计使得可以在百万级bbox标注上预训练，而无需LLM参与
4. Groma在对话式VQA基准(LLaVA-Bench)上也保持了强大的图像级理解能力

## 亮点与洞察

- **架构解耦的洞察**：定位是感知能力而非语义理解，应由视觉模块处理，而非让LLM学习回归坐标。这个分工符合人类视觉处理的"先感知后理解"流程
- **region token的统一性**：用同一种token化机制同时处理输入和输出，设计优雅简洁
- **检测预训练的高效性**：由于定位与LLM解耦，可在大规模检测数据上高效预训练，这对端到端MLLM来说计算成本将非常高
- **Groma Instruct数据**：首个结合视觉和文本提示的grounded对话数据，利用GPT-4V的in-context learning能力

## 局限性 / 可改进方向

1. 区域提议器存在上限（NMS阈值和置信度截断），可能遗漏密集场景中的小目标
2. 当前仅支持bbox级定位，尚未扩展到像素级分割
3. 仅在7B规模验证，更大模型的效果未知
4. 区域提议器的目标上限为100个区域，对于复杂场景可能不够
5. 对高分辨率图像的支持仍受限于448×448

## 相关工作与启发

- **Kosmos-2/Shikra**：让LLM直接输出坐标，简单但效率低，Groma证明了解耦方案更优
- **LISA/GLaMM**：使用外部模块(SAM)做像素级grounding，但引入额外延迟
- **GPT4RoI/RegionGPT**：用pooling提取区域特征，Groma的region token更丰富
- **启发**：视觉tokenizer的设计空间远未被探索完——除了全局token，还可以引入局部/区域/空间token

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ (在tokenizer中嵌入定位是新颖的范式)
- **技术深度**: ⭐⭐⭐⭐ (三阶段训练设计合理，各模块配合紧密)
- **实验充分性**: ⭐⭐⭐⭐ (多基准验证+LVIS扩展评测)
- **写作质量**: ⭐⭐⭐⭐ (动机清晰，方法描述详尽)
- **影响力**: ⭐⭐⭐⭐ (为grounded MLLM提供了新设计范式)

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] LoA-Trans: Enhancing Visual Grounding by Location-Aware Transformers](loa-trans_enhancing_visual_grounding_by_location-aware_transformers.md)
- [\[ECCV 2024\] Self-Adapting Large Visual-Language Models to Edge Devices across Visual Modalities](self-adapting_large_visual-language_models_to_edge_devices_across_visual_modalit.md)
- [\[ECCV 2024\] IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models](ivtp_instruction-guided_visual_token_pruning_for_large_vision-language_models.md)
- [\[ECCV 2024\] CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios](cat_enhancing_multimodal_large_language_model_to_answer_questions_in_dynamic_aud.md)
- [\[ECCV 2024\] UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_lan.md)

<!-- RELATED:END -->
