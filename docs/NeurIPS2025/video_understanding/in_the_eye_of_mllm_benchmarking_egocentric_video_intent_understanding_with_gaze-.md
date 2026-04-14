---
title: >-
  [论文解读] In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting
description: >-
  [NEURIPS2025][视频理解][egocentric video] 提出 EgoGazeVQA——首个利用注视（gaze）信号评估 MLLM 对第一人称视频中用户意图理解能力的基准，并设计三种 gaze-guided prompting 策略显著提升模型表现。
tags:
  - NEURIPS2025
  - 视频理解
  - egocentric video
  - gaze
  - video QA
  - MLLM
  - benchmark
  - intent understanding
---

# In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting

**会议**: NEURIPS2025  
**arXiv**: [2509.07447](https://arxiv.org/abs/2509.07447)  
**代码**: [项目主页](https://taiyi98.github.io/projects/EgoGazeVQA)  
**领域**: video_understanding  
**关键词**: egocentric video, gaze, video QA, MLLM, benchmark, intent understanding

## 一句话总结
提出 EgoGazeVQA——首个利用注视（gaze）信号评估 MLLM 对第一人称视频中用户意图理解能力的基准，并设计三种 gaze-guided prompting 策略显著提升模型表现。

## 背景与动机
第一人称（egocentric）视频天然地将用户视觉感知、注意力、动作和场景上下文对齐在同一坐标系中，是实现主动式、个性化 AI 助手的理想载体。然而，现有的视频 QA 基准几乎全部基于第三人称视角（exocentric），且忽略了注视信号这一最直接反映用户注意力与意图的线索。已有 egocentric VQA 基准如 QaEgo4D、EgoSchema 等分别聚焦于情景记忆或长视频推理，但均不包含 gaze 数据。这导致 MLLM 在面对"用户正在看什么""为什么看这个"等意图相关问题时表现不佳。

## 核心问题
1. 现有 MLLM 能否仅凭全局视觉信息准确理解第一人称视频中的用户空间/时间意图？
2. 引入 gaze 信号作为 prompt 是否能提升 MLLM 的意图理解能力？
3. 不同 gaze 编码方式（文本/视觉/显著图）对模型效果的影响差异如何？

## 方法详解

### EgoGazeVQA 基准构建
数据来自三个带眼动追踪的第一人称视频数据集：Ego4D（31h，168 clips）、EgoExo4D（263 clips）、EGTEA Gaze+（300+ clips），覆盖厨房、客厅、医疗、车库等多种日常场景。

构建流程分三阶段：
1. **视频预处理**：提取帧级描述（caption）与归一化 gaze 坐标 (x, y)，每 9 帧组成一个关键帧段
2. **QA 自动生成**：将 9 帧及其 gaze 坐标输入 Qwen2.5-VL，生成空间/时间/因果三类 QA 对，每题 5 个选项（含反因果、空间邻近陷阱、社交干扰、高显著性干扰项）
3. **人工审核**：标注员从相关性、可回答性、流畅性、准确性、简洁性、难度六个维度评审，剔除不合格样本

最终数据集包含 913 个视频、1757 个 QA 对，按场景（Kitchen/Living Room/Medical/Garage/Others）和活动（Cooking/Gaming/Health/Mechanics/Creative/Others）两种维度分类。

### Gaze-Guided Prompting 策略
论文提出三种将 gaze 信号注入 MLLM 的方式：

1. **GazeT（文本提示）**：将每帧 gaze 坐标归一化为 [0,1] 范围的二维数值，以文本形式拼接到 prompt 中。利用 MLLM 的语言理解能力处理坐标信息
2. **GazeV（视觉提示）**：在每帧 gaze 位置画一个半径 25 像素的红色圆圈，并在 prompt 中说明"红圈代表高关注区域"。直接在视觉层面引导模型注意力
3. **GazeS（时序显著图）**：随视频推进逐帧累积 gaze 热力图，用户反复注视的区域强度更高，最终生成一张编码空间和时间意图的综合显著图

### LoRA 微调实验
使用 LLaMA-Factory 对 Qwen2.5-VL-7B 进行 LoRA 微调：在 EGTEA 分割（约 500 对 gaze QA）上训练、在 Ego4D+EgoExo 上测试，以及反向设置，验证跨数据集迁移能力。

## 实验关键数据

| 模型 | 无 gaze | GazeT | GazeV | GazeS | 人类 |
|------|---------|-------|-------|-------|------|
| Qwen2.5-VL-72B | 60.5 | 65.0 | 63.9 | **66.3** | 83.8 |
| InternVL2.5-8B | 58.3 | 60.1 | 60.6 | 59.9 | — |
| GPT-4o mini | 57.0 | 58.8 | 58.5 | 58.7 | — |
| MiniCPM-o 2.6 | 35.9 | 50.0 | 50.2 | **53.7** | — |

关键发现：
- **GazeS（显著图）整体效果最佳**，尤其空间意图理解提升最大；GazeT 在时间意图理解上更优
- Qwen2.5-VL-72B 使用 GazeS 后平均提升 +5.8pp，空间维度从 57.1→64.3
- 模型规模越大，利用 gaze 的收益越显著；小模型（7B）提升有限
- CLIP/EgoVLP 等简单基线仅略高于随机（~22%），远不及 MLLM
- LoRA 微调后 Qwen2.5-VL-7B 零样本 54.0→**69.5**（在 EGTEA 上训练、Ego4D+EgoExo 上测试），空间推理从 40.4→67.7，提升 +27.3pp
- MLLM 估计的 gaze 精度与 QA 性能正相关：EgoExo 上 MSE=0.038 时提升 +2.8pp，EGTEA 上 MSE=0.119 时反而下降 -0.6pp

## 亮点
- **填补空白**：首个将 gaze 信号与 egocentric VQA 结合的 benchmark，问题设计涵盖空间/时间/因果三维度
- **干扰项设计巧妙**：包含反因果选项、空间邻近陷阱、社交影响干扰、高显著性干扰，需真正理解 gaze 才能正确作答
- **三种 prompting 策略互补**：GazeS 适合空间、GazeT 适合时间，为实际部署提供灵活选择
- **少量数据微调高效**：仅 500 对 gaze QA 的 LoRA 微调即可带来 +15pp 跨域提升

## 局限性 / 可改进方向
- 数据规模偏小（1757 QA 对），场景和活动类型覆盖有限
- 剧烈身体运动/相机晃动导致 gaze 信号失效，模型无法有效利用
- gaze saccade（扫视）可能误导模型关注不相关物体
- 小模型对 gaze prompt 的理解能力不足，收益有限
- 仅评估了多选题格式，未涉及开放式问答
- gaze 估计精度对实际应用影响大，低精度 gaze 反而可能降低性能

## 与相关工作的对比
与 EgoSchema（5063 视频/自动生成/无 gaze/长视频推理）、QaEgo4D（166 视频/人工/无 gaze/情景记忆）、AMEGO（100 视频/自动/无 gaze）等现有 egocentric VQA 基准相比，EgoGazeVQA 是**唯一整合 gaze 信号**的数据集。与 GazeGPT 相比，本工作提供了标准化的 benchmark 和系统性评估，而非仅展示 UI 设计。

## 启发与关联
- Gaze 作为意图先验可迁移到 AR/VR 中的主动式 AI 助手设计
- 显著图编码时空信息的思路可推广到其他注意力信号（如手部轨迹、头部朝向）
- LoRA 微调的高效性表明：少量领域特定 gaze-QA 数据即可大幅提升 MLLM 的 gaze 理解能力，值得在实际产品中探索
- 与 cobodied AI 方向有潜在结合点：gaze 可作为人机协作中意图沟通的隐式通道

## 评分
- 新颖性: 8/10 — 首次将 gaze 引入 egocentric VQA benchmark，切入点独特
- 实验充分度: 7/10 — 涵盖 7 个 MLLM + 3 种 prompting + LoRA + gaze 估计分析，但数据规模偏小
- 写作质量: 7/10 — 结构清晰，但部分实验分析稍显重复
- 价值: 7/10 — 为 egocentric AI 助手提供了重要的评估工具和设计思路
