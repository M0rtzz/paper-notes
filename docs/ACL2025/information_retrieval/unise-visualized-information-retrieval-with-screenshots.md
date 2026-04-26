---
title: >-
  [论文解读] Any Information Is Just Worth One Single Screenshot: Unifying Search With Visualized Information Retrieval
description: >-
  [ACL 2025][可视化信息检索] 本文定义了可视化信息检索（Vis-IR）新范式，将多模态信息统一表示为截图（Screenshot）进行检索，贡献了大规模数据集 VIRA（1300万截图）、通用检索模型 UniSE 和综合基准 MVRB。
tags:
  - ACL 2025
  - 可视化信息检索
  - 截图嵌入
  - 多模态检索
  - 跨模态搜索
  - 检索基准
---

# Any Information Is Just Worth One Single Screenshot: Unifying Search With Visualized Information Retrieval

**会议**: ACL 2025  
**arXiv**: [2502.11431](https://arxiv.org/abs/2502.11431)  
**代码**: 无（将开源）  
**领域**: 信息检索  
**关键词**: 可视化信息检索, 截图嵌入, 多模态检索, 跨模态搜索, 检索基准

## 一句话总结

本文定义了可视化信息检索（Vis-IR）新范式，将多模态信息统一表示为截图（Screenshot）进行检索，贡献了大规模数据集 VIRA（1300万截图）、通用检索模型 UniSE 和综合基准 MVRB。

## 研究背景与动机

1. **领域现状**：信息检索从纯文本扩展到多模态，但不同模态（文本、图像、表格、图表）仍需不同的处理管道。
2. **现有痛点**：缺乏统一的检索模型来支持各种 Vis-IR 应用；没有专门的基准评估截图检索性能；没有针对性的训练数据集。
3. **核心矛盾**：现实中用户越来越多地使用截图形式的信息（如圈选搜索），但检索系统未能统一处理这种视觉化的信息表示。
4. **本文目标**：形式化 Vis-IR 问题，并提供数据集、模型和基准三大核心资源。
5. **切入角度**：将截图视为多模态数据的统一视觉格式，支持"截图查询"和"查询截图"两个方向。
6. **核心 idea**：任何信息都可以用一张截图表示——这提供了统一的检索入口。

## 方法详解

### 整体框架

三大贡献：(1) VIRA数据集包含1300万截图和2000万+训练样本；(2) UniSE模型基于CLIP或MLLM架构提供截图嵌入；(3) MVRB基准覆盖多种任务形式和应用场景。

### 关键设计

1. **VIRA数据集构建**: 从新闻、产品、论文、GitHub等7类来源收集截图，通过OCR或元数据提取细粒度caption，生成q2s（查询→截图）和sq2s（截图+查询→截图）两种QA数据。
2. **UniSE模型**: 提供CLIP架构（高效）和MLLM架构（表达力强）两种选择。CLIP版本用线性组合实现组合查询；MLLM版本用Qwen2-VL-2B作为backbone。
3. **两阶段训练**: 先用截图-caption对做预训练（双向对比学习），再用QA数据做微调。

### 损失函数 / 训练策略

双向对比学习损失 + 带硬负例的检索训练。

## 实验关键数据

### 主实验

在MVRB基准上UniSE显著超越现有多模态检索器，尤其在域外（OOD）场景下优势明显。

### 关键发现

- 现有多模态检索器在截图检索任务上存在显著不足
- UniSE的两种架构在不同场景下各有优势：CLIP版更快，MLLM版在组合查询上更强
- 截图作为统一的检索格式具有很强的实用价值

## 亮点与洞察

- "任何信息都值一张截图"这个理念简洁有力，统一了多模态检索的入口。
- 数据集覆盖面广（7类来源、1300万截图），为社区提供了重要资源。

### 损失函数 / 训练策略

- 预训练阶段：双向对比学习损失，使截图和 caption 在嵌入空间中对齐
- 微调阶段：在 q2s 和 sq2s 数据上训练，使用基于文本和视觉相似度的硬负例增强
- UniSE-CLIP 使用 OpenAI CLIP-Large 作为基础，UniSE-MLLM 使用 Qwen2-VL-2B

## 实验关键数据

### 主实验

| 任务类型 | 现有最佳检索器 | UniSE-CLIP | UniSE-MLLM |
|---------|-------------|-----------|-----------|
| 截图→文本 | 一般 | 显著提升 | 最优 |
| 文本→截图 | 一般 | 显著提升 | 最优 |
| 截图+查询→截图 | 差 | 良好 | 最优 |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 无预训练直接微调 | 下降 | 预训练阶段很重要 |
| 无硬负例 | 下降 | 硬负例提升辨别力 |
| 单一来源数据 | 下降 | 多来源提升泛化 |

### 关键发现

- 现有多模态检索器在截图检索任务上存在显著不足
- UniSE 的两种架构在不同场景下各有优势：CLIP 版更快（适合大规模检索），MLLM 版在组合查询上更强（适合复杂场景）
- 截图作为统一的检索格式具有很强的实用价值——它天然地将文本、图像、表格等多模态信息融合为单一视觉实体
- 数据来源的多样性（新闻、产品、论文等7类）对模型泛化至关重要

## 局限与展望

- 截图分辨率和信息密度的权衡——高分辨率截图包含更多信息但推理更慢
- MLLM 架构的推理速度限制了大规模部署，CLIP 架构更实用但表达力有限
- 组合查询（截图+文本→截图）的场景还有很大提升空间
- 未来可探索多分辨率截图表示和更高效的 MLLM 架构

## 相关工作与启发

- **vs ColPali**: 专注于 Wiki 网页截图检索，UniSE 覆盖更广的 Vis-IR 场景（新闻、产品、论文、代码项目等7类）
- **vs CLIP/BLIP**: 通用 VLM 未针对截图检索优化，在 MVRB 上表现不佳
- **vs MegaPairs**: UniSE 借鉴了其挖掘相似截图对的方法用于 sq2s 数据构建

## 评分

- 新颖性: ⭐⭐⭐⭐ Vis-IR形式化定义和三大资源的全面贡献
- 实验充分度: ⭐⭐⭐⭐ 综合基准覆盖多种场景
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰
- 价值: ⭐⭐⭐⭐⭐ 数据集+模型+基准的完整生态对检索社区价值巨大

<!-- RELATED:START -->

## 相关论文

- [\[ACL 2025\] AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](air-bench_automated_heterogeneous_information_retrieval_benchmark.md)
- [\[ACL 2025\] CoIR: A Comprehensive Benchmark for Code Information Retrieval Models](coir_a_comprehensive_benchmark_for_code_information_retrieval_models.md)
- [\[ACL 2025\] Atomic LLM: A Fine-Grained Information Retrieval Evaluation Benchmark for Language Models](atomic_llm_a_fine-grained_information_retrieval_evaluation_benchmark_for_languag.md)
- [\[ACL 2025\] HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on Retrieval-Augmented Generation](hoh_a_dynamic_benchmark_for_evaluating_the_impact_of_outdated_information_on_ret.md)
- [\[ACL 2025\] Logical Consistency is Vital: Neural-Symbolic Information Retrieval for Negative-Constraint Queries](logical_consistency_is_vital_neural-symbolic_information_retrieval_for_negative-.md)

<!-- RELATED:END -->
