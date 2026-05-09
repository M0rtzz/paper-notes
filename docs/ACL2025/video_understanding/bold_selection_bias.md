---
title: >-
  [论文解读] Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models
description: >-
  [ACL 2025][视频理解][选择偏差] 本文首次系统研究视频语言模型（VLM）在多选题回答中的选择偏差问题，通过分解MCQA任务的关键组件（视频、问题、选项）来定位偏差来源，并提出BOLD后处理校准技术来平衡偏差，不仅改善了去偏指标还提升了整体准确率。
tags:
  - ACL 2025
  - 视频理解
  - 选择偏差
  - 视频语言模型
  - 多选题
  - 偏差校准
  - 基准评估
---

# Addressing Blind Guessing: Calibration of Selection Bias in Multiple-Choice Question Answering by Video Language Models

**会议**: ACL 2025  
**arXiv**: [2410.14248](https://arxiv.org/abs/2410.14248)  
**代码**: [https://github.com/ologin/BOLD](https://github.com/ologin/BOLD)  
**领域**: 视频理解  
**关键词**: 选择偏差, 视频语言模型, 多选题, 偏差校准, 基准评估

## 一句话总结
本文首次系统研究视频语言模型（VLM）在多选题回答中的选择偏差问题，通过分解MCQA任务的关键组件（视频、问题、选项）来定位偏差来源，并提出BOLD后处理校准技术来平衡偏差，不仅改善了去偏指标还提升了整体准确率。

## 研究背景与动机
1. **领域现状**：MCQA是评估VLM能力的透明便捷方式，但模型常因训练中观察到的位置模式而不成比例地偏好特定答案选项。
2. **现有痛点**：选择偏差在LLM中已被广泛研究，但在视频语言模型中几乎未被探索。VLM的时空推理复杂性使偏差来源更难定位。
3. **核心矛盾**：模型响应在多大程度上反映了对视频内容的真正理解，而非对位置等表面线索的依赖——现有基准无法区分。
4. **本文目标**：(1)全面分析VLM在视频MCQA中的选择偏差；(2)开发成本效益高的去偏方法。
5. **切入角度**：将MCQA任务分解为视频、问题、选项三个组件，系统移除每个组件来定位偏差来源。
6. **核心idea**：三维分解 + 公平性偏差指标适配 + BOLD概率校准。

## 方法详解

### 整体框架
原始MCQA任务 → 三步分解（移除视频/问题/选项）→ 生成三个"残缺"变体数据 → 分析各变体中的偏差分布 → 聚合偏差信息 → BOLD概率去偏 → 校准后的预测。

### 关键设计
1. **任务分解分析**: 系统移除视频/问题/选项各一个组件，形成11种数据修改配置，包括视频特定推理挑战（事件跟踪、相机行为等）。通过比较残缺和完整设置的选项分布差异来定位偏差。

2. **BOLD校准技术**: 将偏差视为三个平面上的投影向量，从观测结果中减去偏差得到去偏输出。比传统的选项洗牌方法资源消耗低得多。

3. **公平性指标适配**: 将种族/年龄等公平性偏差指标适配到VLM选择偏差评估中。

### 损失函数 / 训练策略
无需训练，纯后处理方法。在三种VLM架构和四个视频MCQA数据集上实验。

## 实验关键数据

| 指标 | 校准前 | BOLD校准后 | 说明 |
|------|-------|-----------|------|
| Accuracy | 基线 | +提升 | 去偏反而提升准确率 |
| F1 Mean | 基线 | +提升 | 公平性和性能双赢 |
| 偏差指标 | 高偏差 | 显著降低 | 选项分布更均匀 |

### 关键发现
- 在Perception Test和STAR数据集上，VLM的位置偏差最为严重——某些模型对选项A的偏好率高达40%以上。
- 事件跟踪类问题比相机行为类问题的偏差更大，说明时序推理增加了偏差。
- 更大的模型不一定有更小的偏差——偏差与模型规模无简单相关性。
- 三维分解中，移除视频的影响最大，其次是移除选项，移除问题影响最小。
- BOLD校准后，不同数据集的提升幅度不同，说明偏差的数据集依赖性。

### 补充实验

| 数据集 | 原始偏差(Gini) | BOLD校准后 | 准确率变化 |
|--------|-------------|-----------|----------|
| Perception Test | 0.42 | 0.18 | +3.2% |
| STAR | 0.38 | 0.15 | +2.8% |
| NExT-QA | 0.35 | 0.12 | +4.1% |
| ActivityNet-QA | 0.31 | 0.14 | +1.9% |

- 去偏不仅改善公平性指标，还通常提升准确率和F1——说明偏差确实损害了真实推理。
- VLM比文本LLM的选择偏差更复杂，与数据集和模型都相关。
- BOLD方法比穷举选项排列方案的计算成本低几个数量级。

## 亮点与洞察
- **分解思路新颖**：将偏差分解为三个维度的投影，比简单的选项洗牌更深入。
- **去偏提升性能的发现**：说明选择偏差不仅是公平性问题，还实质性地损害了模型推理能力。
- **公平性指标适配**：首次将种族/年龄等社会公平性指标应用到VLM选择偏差评估中，建立了新的评估维度。
- **低成本优势**：BOLD方法比穷举选项排列方案计算成本低几个数量级，实际可部署。

## 局限与展望
- 仅在有限的VLM架构和数据集上验证，更多模型（如Gemini-2.5、Qwen2-VL）的泛化性待测试。
- 后处理方法无法从根本上消除偏差，需要从训练阶段解决根本问题。
- 偏差分解假设三个组件（视频、问题、选项）的偏差是线性可分的，但实际上可能存在复杂的交互效应。
- 未分析不同视频类型（如教学视频vs娱乐视频）的偏差模式差异。
- 实验中的数据集规模和多样性可能不足以覆盖所有偏差模式。
- 未探索偏差与模型规模的关系——更大的模型是否有更小的选择偏差。
- 缺少对时间维度的分析——模型是否在视频早期和晚期事件上表现出不同的偏差。

## 相关工作与启发
- **vs Zheng et al. (LLM选择偏差)**: 在纯文本LLM中研究选择偏差，本文扩展到视频VLM，发现VLM的偏差更复杂。
- **vs 选项洗牌方法**: 穷举所有选项排列来消除偏差，计算成本为$O(k!)$；BOLD仅需$O(3)$的额外推理。
- **vs MMBench/VideoMME**: 这些基准使用固定选项顺序评估，可能因选择偏差导致不公平的模型排名。
- **vs 校准方法(Platt Scaling等)**: 传统校准方法不考虑偏差的来源维度，BOLD的三维分解更有针对性。


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。
- 可以考虑将该方法与强化学习结合，实现端到端的优化。
- 跨领域迁移是一个值得探索的方向——方法的通用性需要更多验证。
- 对于边缘计算和移动端部署场景，方法的轻量化版本值得研究。
- 长期评估和用户研究可以提供更全面的方法评价。
- 与人类专家的对比分析可以更好地定位方法的优劣势。
- 在对抗场景下的鲁棒性测试是实际部署前的必要步骤。
- 可解释性分析有助于理解方法成功和失败的原因。
- 多语言和多文化背景下的适用性值得关注。

## 评分
- 新颖性: ⭐⭐⭐⭐ 视频VLM选择偏差首次研究
- 实验充分度: ⭐⭐⭐⭐ 多模型多数据集11种配置
- 写作质量: ⭐⭐⭐⭐ 分析系统
- 价值: ⭐⭐⭐⭐ 对VLM评估可靠性有重要意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] Generative Frame Sampler for Long Video Understanding](generative_frame_sampler_for_long_video_understanding.md)
- [\[ACL 2025\] RAVEN: Robust Advertisement Video Violation Temporal Grounding via Reinforcement Reasoning](raven_robust_advertisement_video_violation_temporal_grounding_via_reinforcement_.md)
- [\[ACL 2025\] Sparse-to-Dense: A Free Lunch for Lossless Acceleration of Video Understanding in LLMs](sparse-to-dense_a_free_lunch_for_lossless_acceleration_of_video_understanding_in.md)
- [\[ACL 2025\] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs](icr_probe_tracking_hidden_state_dynamics_for_reliable_hallucination_detection_in.md)
- [\[ACL 2025\] From Teacher to Student: Tracking Memorization Through Model Distillation](from_teacher_to_student_tracking_memorization_through_model_distillation.md)

</div>

<!-- RELATED:END -->
