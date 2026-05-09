---
title: >-
  [论文解读] Towards Open-Ended Visual Quality Comparison
description: >-
  [ECCV 2024][多模态][视觉质量评估] 提出 Co-Instruct，首个开源的开放式视觉质量比较大模型，通过构建 Co-Instruct-562K 数据集和 MICBench 基准，使 LMM 在视觉质量比较任务上超越 GPT-4V。
tags:
  - ECCV 2024
  - 多模态
  - 多模态VLM
  - 大规模多模态模型
  - 多图比较
  - 指令微调
  - 基准测试
---

# Towards Open-Ended Visual Quality Comparison

**会议**: ECCV 2024  
**arXiv**: [2402.16641](https://arxiv.org/abs/2402.16641)  
**代码**: [https://huggingface.co/q-future/co-instruct](https://huggingface.co/q-future/co-instruct)  
**领域**: 多模态VLM  
**关键词**: 视觉质量评估, 大规模多模态模型, 多图比较, 指令微调, 基准测试

## 一句话总结

提出 Co-Instruct，首个开源的开放式视觉质量比较大模型，通过构建 Co-Instruct-562K 数据集和 MICBench 基准，使 LMM 在视觉质量比较任务上超越 GPT-4V。

## 研究背景与动机

- 比较设置（成对选择、列表排名）是图像质量评估（IQA）中广泛采用的主观研究方法，因为它天然标准化了不同观察者的评估标准
- 现有开源 LMM 仅用单图指令微调数据训练，缺乏多图比较设置的能力
- 现有比较方法局限于整体质量比较，未扩展到开放式场景（开放问题 + 详细推理）
- 收集人工标注的比较数据集成本极高
- **核心动机**：将 LMM 的能力扩展到开放式视觉质量比较，允许响应开放范围的比较问题并提供详细推理

## 方法详解

### 整体框架

系统由三部分组成：
1. **Co-Instruct-562K** 数据集构建（两种弱监督来源）
2. **Co-Instruct** 模型（基于 mPLUG-Owl2 + 视觉 token 压缩 + 图文交错格式）
3. **MICBench** 基准测试

### 关键设计

**数据构建策略**：

1. **Merge2Compare（10万组）**：
    - 从 Q-Pathway 的 19K 图像中随机匹配为 2-4 图组
    - 用文本嵌入模型去除高相似度描述对（Top-similarity Pair Removal）
    - 用单模态 LLM 将各图的人工质量描述"合并"为比较文本
    - 准确率 96%

2. **Teach2Compare（26万QA + 3万通用）**：
    - 收集 9K 多样化未标注图像（野外 + 人工失真 + AI 生成）
    - 用 GPT-4V 生成整体质量比较和质量相关 QA 对
    - 准确率 94%

**模型设计**：
- **视觉 token 压缩**：采用 abstractor 结构将每图 1025 token 减至 65 token，适配多图输入
- **图文交错格式**：`The first image: <img₀> The second image: <img₁> ... <query>`，使模型能区分不同图像

**MICBench 基准**：
- 2000 个多选题，比较 3-4 张图的质量/属性
- 题型：Which 问题 60%、Yes-or-No 22%、其他 18%
- 分为 dev set (1004) 和 test set (996)

### 损失函数 / 训练策略

- 基础模型：mPLUG-Owl2 (LLaMA-2 + CLIP-ViT-L14)
- 输入分辨率：448×448
- 学习率 2e-5，batch size 192，训练 2 epochs，全参数更新
- 训练时间：25 小时 / 8×A100

## 实验关键数据

### 主实验

| 指标 | SD-XL | PixArt-α | GlyphControl | TextDiffuser | Co-Instruct |
|------|-------|----------|--------------|--------------|-------------|
| Q-Bench^PAIR 整体 | - | - | - | - | **最优** |
| MICBench | - | - | - | - | **超越GPT-4V** |

Co-Instruct 在 Q-Bench^PAIR-A1 上比无比较数据变体高 51%，是唯一超越人类能力的 LMM。

### 消融实验

| 组件 | 效果 |
|------|------|
| Merge2Compare only | 准确率提升但缺少细粒度 |
| Teach2Compare only | 更多样但略低准确率 |
| 组合训练 | 最优，互补增强 |
| 图文交错 vs 图片堆叠 | 交错格式显著优于堆叠 |
| Abstractor vs 线性投影 | Abstractor 解决多图 context 溢出 |

### 关键发现

1. Co-Instruct 比最佳开源 LMM 平均高 30% 准确率
2. 虽然用 GPT-4V 作为老师之一，但学生超越了老师
3. 两种数据子集互补：Merge2Compare 准确但缺细粒度，Teach2Compare 多样但略不准确
4. Which 类问题是质量比较中最重要也最具挑战性的类型

## 亮点与洞察

- **弱监督数据构建的巧妙设计**：完全避免了昂贵的人工多图比较标注，两种方法互补
- **学生超越老师**：Co-Instruct 在多个基准上超越了其老师 GPT-4V
- **开辟新任务**：首次将视觉质量比较推进到开放式多图场景
- **实用价值高**：图像质量比较在推荐系统和图像改进指导中有直接应用

## 局限性 / 可改进方向

- Merge2Compare 的 Top-similarity Removal 会丢弃部分数据（四图组仅保留 55%）
- 仅支持 2-4 图比较，未扩展到更多图的列表排名场景
- 视觉 abstracto 的 token 压缩可能丢失细节信息
- GPT-4V 伪标签存在约 6% 错误率，可能引入噪声
- 未来可探索：更多图比较、视频质量比较、主动学习减少伪标签噪声

## 相关工作与启发

- Q-Bench 系列（Q-Bench, Q-Instruct, Q-Align）奠定了 LMM 质量评估的基础，本文是比较设置的自然延伸
- 弱监督数据构建策略（LLM 合并 + GPT-4V 教学）可推广到其他需要比较标注的任务
- 图文交错输入格式对多图 LMM 有通用参考价值

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4 |
| 技术深度 | 3.5 |
| 实验充分性 | 4.5 |
| 写作质量 | 4 |
| 实用价值 | 4 |
| 总分 | 4 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](sqllava_selfquestioning_for_large_visionlanguage_assistant.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)
- [\[ECCV 2024\] LEGO: Learning EGOcentric Action Frame Generation via Visual Instruction Tuning](lego_learning_egocentric_action_frame_generation_via_visual_instruction_tuning.md)
- [\[ECCV 2024\] BRAVE: Broadening the Visual Encoding of Vision-Language Models](brave_broadening_the_visual_encoding_of_visionlanguage_model.md)
- [\[ECCV 2024\] IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models](ivtp_instruction-guided_visual_token_pruning_for_large_vision-language_models.md)

</div>

<!-- RELATED:END -->
