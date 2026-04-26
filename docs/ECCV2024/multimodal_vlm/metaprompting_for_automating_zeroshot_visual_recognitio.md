---
title: >-
  [论文解读] Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs
description: >-
  [ECCV 2024][多模态][zero-shot recognition] 提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段元提示策略自动让 LLM 生成任务特定且类别特定的 VLM 提示，在 20 个数据集上将 CLIP 零样本识别提升最高 19.8%，完全消除人工提示设计。
tags:
  - ECCV 2024
  - 多模态
  - zero-shot recognition
  - 提示学习
  - VLM
  - CLIP
---

# Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs

**会议**: ECCV 2024  
**arXiv**: [2403.11755](https://arxiv.org/abs/2403.11755)  
**代码**: https://github.com/jmiemirza/Meta-Prompting (有)  
**领域**: LLM/NLP  
**关键词**: zero-shot recognition, meta-prompting, VLM, CLIP, prompt ensembling

## 一句话总结

提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段元提示策略自动让 LLM 生成任务特定且类别特定的 VLM 提示，在 20 个数据集上将 CLIP 零样本识别提升最高 19.8%，完全消除人工提示设计。

## 研究背景与动机

### 领域现状

**领域现状**：CLIP 的零样本分类性能高度依赖文本提示的质量

### 核心矛盾

**核心矛盾**：提示集成（多个类别特定提示的平均嵌入）带来显著提升，但手工设计大量提示不可行

### 现有痛点

**现有痛点**：现有 LLM 辅助方法（CUPL/DCLIP/Waffle）仍需手工设计 LLM 查询模板或数据集特定的概念

### 解决思路

**解决思路**：核心问题：手工设计 LLM 查询是否引入了主观偏见？能否完全自动化提示生成？

### 补充说明

**补充说明**：关键观察：将人工设计从 VLM 提示层面转移到 LLM 查询层面，并没有真正消除人工干预

## 方法详解

### 整体框架

MPVR 采用两阶段提示生成：
1. **第一阶段（元提示）**：LLM 根据任务描述自动生成多样的、类别无关的 LLM 查询模板
2. **第二阶段（类别化）**：将类别名称填入查询模板，再次查询 LLM 生成类别特定的 VLM 提示
3. 最终用这些 VLM 提示构建集成零样本分类器

### 关键设计

**元提示的三部分组成**：

1. **系统提示（System Prompt）**：
    - 通用指令，描述元提示任务和期望输出格式
    - 跨所有任务保持不变

2. **上下文示例（In-context Example）**：
    - 包含一个示例任务的描述和对应的 LLM 查询模板
    - 引导 LLM 理解期望的输出格式和风格
    - 跨所有任务保持不变

3. **下游任务规范（Task Specification）**：
    - 唯一与任务相关的部分
    - 从公开 API 或数据集网页抓取的简短自然语言描述
    - 提供粗粒度任务信息让 LLM 生成任务特定的查询

**两阶段生成的优势**：
- 第一阶段注入任务视觉风格信息但保持类别无关
- 第二阶段填入类别信息生成细粒度视觉描述
- 两阶段比单阶段直接生成效果更好（消融验证）

### 损失函数 / 训练策略

- **无需训练**：MPVR 是纯推理时方法
- 零样本分类使用标准余弦相似度 + 温度缩放
- 类别嵌入 = 所有 VLM 提示嵌入的均值
- 总共生成约 250 万条唯一类别描述（GPT + Mixtral）

## 实验关键数据

### 主实验

在 20 个数据集上的平均零样本准确率提升：

| 方法 | 相对 CLIP 的平均提升 |
|------|-------------------|
| DCLIP | +1.8% |
| CUPL | +2.5% |
| Waffle | +2.9% |
| **MPVR (GPT)** | **+5.0%** |
| **MPVR (Mixtral)** | **+4.5%** |

单数据集最大提升：EuroSAT 上 +19.8%（GPT）、+18.2%（Mixtral）

### 消融实验

| 元提示组件 | 平均准确率变化 |
|-----------|-------------|
| 完整 MPVR | baseline |
| w/o 系统提示 | -2.1% |
| w/o 上下文示例 | -1.8% |
| w/o 任务描述 | -3.5% |
| 单阶段（跳过第一阶段） | -1.2% |

### 关键发现

- **开源模型也有效**：首次证明 Mixtral 等开源 LLM 生成的描述也能提升 VLM 零样本性能
- MPVR-CLIP 甚至超越了 LLM 解码器类方法（如 LLaVA-1.5）在视觉识别上的表现
- 任务描述是最关键的组件，移除后性能下降最多
- 与 MetaCLIP 和 OpenCLIP 等更强 VLM 配合使用时，提升同样显著
- 在细粒度分类数据集（如花卉、汽车）上提升尤为明显

## 亮点与洞察

1. **极简人工干预**：仅需任务的短文本描述（可从网页自动获取），完全消除手工提示设计
2. **两阶段策略的洞察**：先生成任务风格→再填充类别信息，比一步到位更有效
3. **首次验证开源 LLM 的有效性**：Mixtral 的表现与 GPT 接近，降低了 API 依赖
4. 生成的 250 万描述语料本身就是对 LLM 视觉世界知识的有价值提取
5. 方法的通用性和可扩展性：对无视觉数据的新领域也可直接使用

## 局限与展望 / 可改进方向

- 两次 LLM 查询增加了计算成本（但仅需一次性生成）
- LLM 生成的描述可能包含不准确的视觉信息
- 对类别数量极多的数据集（如 DomainNet 的 345 类），生成成本较高
- 未探索 VLM 提示的加权集成（当前简单平均）

## 相关工作与启发

- **CLIP**: 零样本分类基线
- **CUPL**: 手工 LLM 查询生成 VLM 提示的先驱
- **DCLIP**: 类别描述符方法
- **Waffle**: 随机描述符和广泛概念的混合
- 启发：减少人工干预不应止于第一层提示工程，应递归地将提示生成自动化

## 评分

| 维度 | 分数 (1-10) |
|------|-----------|
| 新颖性 | 8 |
| 技术深度 | 6 |
| 实验充分性 | 9 |
| 实用价值 | 9 |
| 写作质量 | 8 |
| 总体评分 | 8.0 |

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)
- [\[ECCV 2024\] Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_visionlangu.md)
- [\[ICCV 2025\] Synergistic Prompting for Robust Visual Recognition with Missing Modalities](../../ICCV2025/multimodal_vlm/synergistic_prompting_for_robust_visual_recognition_with_missing_modalities.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_visionlanguage_models.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)

<!-- RELATED:END -->
