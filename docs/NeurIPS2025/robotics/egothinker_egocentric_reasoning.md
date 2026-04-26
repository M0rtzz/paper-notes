---
title: >-
  [论文解读] EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT
description: >-
  [NeurIPS 2025][机器人][第一人称视频] 本文提出 EgoThinker，通过构建 EgoRe-5M 大规模第一人称视频推理数据集（含因果 CoT 标注和手物定位标注）和两阶段训练（SFT + GRPO 强化微调），赋予 MLLM 鲁棒的第一人称推理、手物定位和时间定位能力，在多个 egocentric 基准上实现 SOTA。
tags:
  - NeurIPS 2025
  - 机器人
  - 第一人称视频
  - 链式思维推理
  - 手物交互
  - 强化微调
  - 时空定位
---

# EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT

**会议**: NeurIPS 2025  
**arXiv**: [2510.23569](https://arxiv.org/abs/2510.23569)  
**代码**: [GitHub](https://github.com/InternRobotics/EgoThinker)  
**领域**: 视频理解  
**关键词**: 第一人称视频, 链式思维推理, 手物交互, 强化微调, 时空定位

## 一句话总结
本文提出 EgoThinker，通过构建 EgoRe-5M 大规模第一人称视频推理数据集（含因果 CoT 标注和手物定位标注）和两阶段训练（SFT + GRPO 强化微调），赋予 MLLM 鲁棒的第一人称推理、手物定位和时间定位能力，在多个 egocentric 基准上实现 SOTA。

## 研究背景与动机
1. **领域现状**: MLLM 在第三人称视觉推理上表现出色，但缺乏第一人称（egocentric）视角的具身认知理解。
2. **现有痛点**: 现有 egocentric 数据集（Ego4D）缺乏显式推理链、时间跨度标注和细粒度手物定位数据。
3. **核心矛盾**: 第一人称推理需要推断不可见的摄像者意图和行为，而非仅识别可见事件。
4. **本文目标**: 使 MLLM 具备第一人称推理、精确手物定位和长程时间理解的综合能力。
5. **切入角度**: 构建大规模因果 CoT 标注数据 + 两阶段训练（SFT 建立基础 + RFT 强化定位）。
6. **核心 idea**: 用 HowTo100M 等网络视频大规模挖掘 egocentric 数据，构建因果推理 QA，再用 GRPO 强化时空定位。

## 方法详解

### 整体框架
EgoRe-5M 数据集 → SFT 阶段（因果 CoT 推理能力）→ RFT 阶段（GRPO 强化手物定位和时间定位）。

### 关键设计
1. **EgoRe-5M 数据集**: 从 13M egocentric 视频片段构建 500 万 QA 对，包含多分钟片段的因果 CoT 标注、密集手物定位标注。通过多阶段过滤流水线从 HowTo100M（30M 初始片段）中挖掘 egocentric 视频，使用 HTM-AA 和 Howto-Interlink7M 的时间对齐标注。
2. **两阶段训练范式**:
    - SFT 阶段: 在 EgoRe-5M 上建立 egocentric 理解和推理基础，学习因果 CoT 标注
    - RFT 阶段: 使用 GRPO 在时空定位数据上强化精确定位能力，使用 IoU 和 bbox 匹配作为奖励
3. **时空 CoT 标注**: 标注包含完整因果关系链（为什么执行此动作→如何执行→接下来做什么），使模型模拟人类 egocentric 因果推理和规划过程。
4. **手物交互数据**: 专门构建密集的手-物体交互定位数据，标注手的位置、抓取的物体和交互类型。

### 损失函数 / 训练策略
- SFT: 标准交叉熵损失
- RFT: GRPO with IoU/bbox 匹配奖励
- 基座: InternVL 系列视觉-语言模型
- 数据多样性: 覆盖从几秒到数分钟的不同时间跨度

## 实验关键数据

| 基准 | EgoThinker | 之前 SOTA | 提升 |
|------|-----------|----------|------|
| EgoSchema | 显著提升 | - | SOTA |
| Ego4D NLQ | SOTA | - | +显著 |
| 多个 egocentric QA | SOTA | - | - |

### 关键发现
- 因果 CoT 标注对复杂 egocentric 推理至关重要
- GRPO 强化训练显著提升时空定位精度
- 从网络视频挖掘 egocentric 数据是可扩展的策略

### EgoRe-5M数据集构成

| 数据来源 | 初始片段 | 过滤后 | QA对 |
|---------|---------|--------|------|
| HowTo100M | 30M | ~6M | ~3M |
| HTM-AA | 2M | ~1.5M | ~1M |
| Howto-Interlink7M | 7M | ~3M | ~1M |
| 合计 | 39M | ~10.5M | ~5M |

### 训练阶段消融

| 配置 | EgoSchema | Ego4D NLQ | 手物定位 |
|------|----------|-----------|--------|
| 仅SFT | 良好 | 中等 | 较差 |
| SFT+RFT | **SOTA** | **SOTA** | **最优** |
| 仅RFT(无SFT) | 差 | 差 | 中等 |


## 亮点与洞察
- 首个同时具备推理和精确手物理解的 egocentric MLLM
- EgoRe-5M 的数据构建流水线可复用于其他 egocentric 任务
- 两阶段训练范式（SFT → RFT）在 egocentric 领域验证有效

## 局限与展望
- 数据挖掘流水线可能引入非 egocentric 视频噪声，过滤质量影响下游任务。
- 仅验证在现有 egocentric 基准上，真实穿戴设备场景（AR 眼镜等）待验证。
- 未探索与机器人操作任务的结合，而这是 egocentric 理解的重要应用场景。
- CoT 标注依赖 LLM 生成，质量可能参差不齐，尤其是复杂因果链的准确性。
- 手物交互定位精度在遮挡严重场景下可能下降。
- 未探索实时推理的延迟和效率，穿戴设备对延迟要求严格。
- GRPO 强化训练的奖励设计（IoU/bbox 匹配）可能不足以覆盖所有定位场景。
- HowTo100M 主要是教学视频，日常生活场景的覆盖可能不足。

## 相关工作与启发
- **vs EgoVLP**: EgoVLP 做视觉-语言预训练但缺乏因果推理链
- **vs VideoChat-R1**: VideoChat-R1 做通用视频 RL 微调，EgoThinker 专注 egocentric 场景
- **vs Ego-Plan-Bench**: 评估规划能力但模型本身未优化
- **vs InternVL**: 通用 VLM 缺乏第一人称视角的具身理解


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

## 评分
- 新颖性: ⭐⭐⭐⭐ 大规模 egocentric 因果推理数据集构建是重要贡献
- 实验充分度: ⭐⭐⭐⭐ 多基准 SOTA 验证
- 写作质量: ⭐⭐⭐⭐ 框架清晰，数据构建详尽
- 价值: ⭐⭐⭐⭐⭐ 对穿戴助手和具身 AI 有直接价值

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] NeSyPr: Neurosymbolic Proceduralization For Efficient Embodied Reasoning](nesypr_neurosymbolic_proceduralization_for_efficient_embodied_reasoning.md)
- [\[NeurIPS 2025\] MMTU: A Massive Multi-Task Table Understanding and Reasoning Benchmark](mmtu_a_massive_multi-task_table_understanding_and_reasoning_benchmark.md)
- [\[NeurIPS 2025\] ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning](thinkact_vision-language-action_reasoning_via_reinforced_visual_latent_planning.md)
- [\[NeurIPS 2025\] MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning](mesatask_towards_task-driven_tabletop_scene_generation_via_3d_spatial_reasoning.md)
- [\[NeurIPS 2025\] LLM World Models Are Mental: Output Layer Evidence of Brittle World Model Use in LLM Mechanical Reasoning](llm_world_models_are_mental_output_layer_evidence_of_brittle_world_model_use_in_.md)

<!-- RELATED:END -->
