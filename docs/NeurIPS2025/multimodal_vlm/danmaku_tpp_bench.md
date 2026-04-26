---
title: >-
  [论文解读] DanmakuTPPBench: A Multi-modal Benchmark for Temporal Point Process Modeling and Understanding
description: >-
  [NeurIPS 2025][多模态][时间点过程] 本文提出 DanmakuTPPBench，首个融合时间、文本和视觉的多模态时间点过程（TPP）基准，包含从 B 站弹幕系统收集的 DanmakuTPP-Events（7,250 个视频序列，1080 万弹幕事件）和基于多 Agent 流水线构建的 DanmakuTPP-QA（10 种评估任务），揭示了当前 LLM/MLLM 在 TPP 理解上的显著差距。
tags:
  - NeurIPS 2025
  - 多模态
  - 时间点过程
  - 弹幕
  - 多模态基准
  - 大语言模型
  - 时序推理
---

# DanmakuTPPBench: A Multi-modal Benchmark for Temporal Point Process Modeling and Understanding

**会议**: NeurIPS 2025  
**arXiv**: [2505.18411](https://arxiv.org/abs/2505.18411)  
**代码**: [GitHub](https://github.com/FRENKIE-CHIANG/DanmakuTPPBench)  
**领域**: 多模态视觉语言模型  
**关键词**: 时间点过程, 弹幕, 多模态基准, 大语言模型, 时序推理

## 一句话总结
本文提出 DanmakuTPPBench，首个融合时间、文本和视觉的多模态时间点过程（TPP）基准，包含从 B 站弹幕系统收集的 DanmakuTPP-Events（7,250 个视频序列，1080 万弹幕事件）和基于多 Agent 流水线构建的 DanmakuTPP-QA（10 种评估任务），揭示了当前 LLM/MLLM 在 TPP 理解上的显著差距。

## 研究背景与动机

1. **领域现状**: TPP 在社交媒体、医疗、金融等领域广泛应用，但现有 TPP 数据集几乎全为单模态（仅时间+类别），限制了多模态 TPP 模型的发展。

2. **现有痛点**: 现有数据集缺乏文本和视觉上下文。LLM/MLLM 的 TPP 理解能力几乎未被探索。缺少专门的 TPP 问答基准。

3. **核心矛盾**: 真实世界的事件流天然包含多模态信息，但无法用单模态数据训练和评估。

4. **本文目标**: 构建首个原生多模态 TPP 数据集和问答基准。

5. **切入角度**: B 站弹幕系统天然形成"时间戳精确对齐 + 文本内容 + 视频帧"的多模态 TPP。

6. **核心 idea**: 弹幕作为天然的多模态 TPP 数据源 + 多 Agent 流水线自动构建 QA 基准。

## 方法详解

### 整体框架
两个互补组件：(1) DanmakuTPP-Events 提供传统 TPP 建模数据；(2) DanmakuTPP-QA 提供评估 LLM/MLLM TPP 理解能力的 QA 任务。数据从 B 站 2024 年 Top100 创作者的 7,250 个视频中收集，覆盖 14 个视频类别。

### 关键设计

1. **DanmakuTPP-Events 数据集**:
    - 功能: 首个多模态 TPP 建模数据集
    - 核心思路: 从 B 站 2024 年 Top100 创作者收集 7,250 个视频，每个弹幕事件包含时间戳 $t_i$、事件类型 $e_i$（9 种）、文本标记 $m_i^{text}$ 和视频帧 $m_i^{image}$
    - 设计动机: 弹幕天然融合了时间、文本和视觉三种模态；覆盖 14 个视频类别

2. **多 Agent 构建流水线**:
    - 功能: 自动化构建高质量 QA 数据
    - 核心思路: 5 个 Agent 协同——任务设计 Agent（DeepSeek-R1 设计 10 种任务）、标注 Agent（Qwen2.5 + Qwen2.5-VL + RAM 标注）、质量控制 Agent（Qwen3 多数投票）、可视化 Agent（Qwen2.5-Coder 生成图表）、任务求解 Agent（多 LLM 多数投票生成答案）
    - 设计动机: 弹幕数据量大且复杂，手工标注不可行；多 Agent 流水线确保质量

3. **10 种评估任务**:
    - 功能: 全面评估 TPP 理解能力
    - 核心思路: 8 个封闭式任务（弹幕爆发计数、时间预测、情感预测、事件类型推理等）+ 2 个开放式任务（全局情感动态分析、弹幕爆发因果分析）
    - 设计动机: 覆盖从简单预测到复杂多模态推理的不同难度层级

### 损失函数 / 训练策略
- 传统 TPP 模型评估: RMSE（时间预测）+ log-likelihood（建模性能）
- QA 评估: 封闭式用 Accuracy/RMSE，开放式用 Qwen3-235B 评分（0-1）
- 微调实验: Qwen2.5-VL-3B + LoRA，单 4090，3 epochs
- 每个 MLLM 仅采样 3 帧视频用于评估，MLLM 输入包含弹幕事件序列文本和采样视频帧

## 实验关键数据

### 主实验

| 模型 | T-1 (ACC) | T-2 (RMSE↓) | T-7 (ACC) | T-8 (ACC) |
|------|-----------|------------|-----------|-----------|
| Qwen2.5-7B | 0.33 | 27.64 | 10.67 | 32.67 |
| Qwen2.5-72B | 0.67 | 1.28 | 16.00 | 43.83 |
| DeepSeek-V3 | 25.00 | 1.30 | 13.67 | 34.50 |
| Qwen2.5-VL-72B | 0.33 | 1.14 | 15.98 | 47.17 |
| Fine-tuned 3B | **27.00** | 1.35 | - | - |

### 关键发现
- 传统 TPP 模型中 NHP 表现最佳（log-likelihood 0.799）
- 模型规模增大对 TPP 理解有帮助（RMSE 从 27.64 降至 1.28）
- 视觉信息（MLLM）并未一致提升性能，说明多模态融合仍有挑战
- 弹幕爆发计数（T-1）对所有模型都非常困难（最高仅 27%）
- 微调 3B 模型在部分任务上可接近 72B 模型的表现
- 模型族对比：Qwen3 在情感相关任务上表现最优（T-4 RMSE 最低 0.20），DeepSeek-V3 和 Llama-3.3 在情感极性预测（T-5/T-6）上领先
- MLLM 并未一致优于 LLM——Llama-3.3-70B 在 T-2 上 RMSE 最低（1.11），说明文本模型可通过语言线索推断时间模式
- 微调 3B 模型在情感预测任务（T-4/5/6）上误差比最优预训练模型低 4-6 倍（RMSE 0.05/0.16/0.08），但 T-3 上出现过拟合（RMSE 220.43）
- 开放式任务中 Qwen3-235B 在因果分析（T-10）上最强（0.52），Qwen2.5-VL-72B 在全局情感分析（T-9）上最强（0.48）

## 亮点与洞察
- 弹幕作为 TPP 数据源的创意选择——天然多模态、大规模、有丰富社交信号
- 多 Agent 流水线是可扩展的数据集构建范式
- 9 种弹幕事件类型的分类体系有社会学研究价值
- 揭示了 LLM/MLLM 在时序事件理解上的巨大差距
- 微调实验：Qwen2.5-VL-3B + LoRA，单 4090 GPU，3 epochs 即可在情感任务上超越 72B 预训练模型，展示了任务特定适配的重要性

## 局限与展望
- 数据仅来自 B 站中文平台，跨平台/跨语言泛化待验证
- 每个 MLLM 仅采样 3 帧视频，更多帧可能改善性能
- 弹幕数据可能包含不当内容，需要内容审核
- 传统 TPP 模型未利用多模态信息，需要新的多模态 TPP 架构
- 多 Agent 流水线中 5 个 Agent 分工明确：DeepSeek-R1 设计任务、Qwen2.5/Qwen2.5-VL/RAM 标注、Qwen3 多数投票控制质量、Qwen2.5-Coder 生成可视化图表、多 LLM 多数投票生成答案
- 8 个封闭式任务覆盖弹幕爆发计数、时间预测、精确时间预测、情感/极性预测、事件类型推理等；2 个开放式任务要求全局动态分析和因果归因

## 相关工作与启发
- **vs Retweet/StackOverflow 数据集**: 仅有时间+类型，缺乏文本和视觉
- **vs Amazon Review**: 有文本但无视觉，DanmakuTPP 三模态齐全
- **vs TSQA (时间序列QA)**: TSQA 面向通用时间序列，DanmakuTPP 专注事件序列
- **vs Language-TPP**: Language-TPP 尝试将 LLM 用于 TPP 但仅使用单模态文本数据，DanmakuTPP 首次引入原生多模态 TPP 评估

## 评分

### 实现细节
数据从B站2024年Top100创作者的7,250个视频收集，14个类别。
5个Agent协同：DeepSeek-R1设计任务、Qwen2.5标注、Qwen3质量控制。
微调：Qwen2.5-VL-3B + LoRA，单4090 GPU，3 epochs。
- 新颖性: ⭐⭐⭐⭐⭐ 首个多模态 TPP 基准，弹幕数据源创新
- 实验充分度: ⭐⭐⭐⭐ 传统模型+LLM/MLLM 全面评估
- 写作质量: ⭐⭐⭐⭐ 流水线设计详尽，统计分析丰富
- 价值: ⭐⭐⭐⭐ 开辟了多模态 TPP 研究的新方向

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] MoniTor: Exploiting Large Language Models with Instruction for Online Video Anomaly Detection](monitor_exploiting_large_language_models_with_instruction_for_online_video_anoma.md)
- [\[NeurIPS 2025\] Efficient Multi-modal Large Language Models via Progressive Consistency Distillation](efficient_multi-modal_large_language_models_via_progressive_consistency_distilla.md)
- [\[NeurIPS 2025\] VaMP: Variational Multi-Modal Prompt Learning for Vision-Language Models](vamp_variational_multi-modal_prompt_learning_for_vision-language_models.md)
- [\[NeurIPS 2025\] Can Multi-Modal LLMs Provide Live Step-by-Step Task Guidance?](can_multi-modal_llms_provide_live_step-by-step_task_guidance.md)
- [\[NeurIPS 2025\] VT-FSL: Bridging Vision and Text with LLMs for Few-Shot Learning](vt-fsl_bridging_vision_and_text_with_llms_for_few-shot_learning.md)

<!-- RELATED:END -->
