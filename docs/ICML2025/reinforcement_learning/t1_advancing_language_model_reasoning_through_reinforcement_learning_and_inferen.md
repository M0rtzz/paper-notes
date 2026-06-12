---
title: >-
  [论文解读] T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling
description: >-
  [ICML 2025][强化学习][推理能力] T1 通过合成 CoT 数据初始化 + RL 训练中的过采样和熵奖励策略来鼓励探索，使开源 LLM 展现出推理时缩放（inference scaling）行为，在 MATH500、AIME2024 等挑战性数学推理基准上超越了 QwQ-32B-Preview。
tags:
  - "ICML 2025"
  - "强化学习"
  - "推理能力"
  - "推理时缩放"
  - "Chain-of-Thought"
  - "数学推理"
---

# T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling

**会议**: ICML 2025  
**arXiv**: [2501.11651](https://arxiv.org/abs/2501.11651)  
**代码**: [https://github.com/THUDM/T1](https://github.com/THUDM/T1)  
**领域**: LLM推理 / 强化学习  
**关键词**: 强化学习, 推理能力, 推理时缩放, Chain-of-Thought, 数学推理

## 一句话总结

T1 通过合成 CoT 数据初始化 + RL 训练中的过采样和熵奖励策略来鼓励探索，使开源 LLM 展现出推理时缩放（inference scaling）行为，在 MATH500、AIME2024 等挑战性数学推理基准上超越了 QwQ-32B-Preview。

## 研究背景与动机

1. **领域现状**：大语言模型在复杂推理任务上展现了出色能力，但现有方法主要依赖模仿学习（如蒸馏 CoT 数据），在测试时缩放（test-time scaling）方面表现不佳。

2. **现有痛点**：强化学习虽然有望通过自主探索和反馈学习来提升推理能力，但近期的 RL 尝试在复杂推理任务上仅取得了有限的改进。核心问题在于——RL 训练过程中模型容易陷入局部最优、采样多样性不足、策略优化不稳定。

3. **核心矛盾**：RL 理论上能让模型通过试错学到更优的推理策略，但实践中 RL 训练的不稳定性和探索不足限制了其在 LLM 推理上的收益。如何让 RL 训练"规模化"（scale up）成为关键瓶颈。

4. **本文目标**：如何通过 RL 有效提升 LLM 的推理能力，同时实现推理时缩放——即增加推理计算预算就能获得更好的性能。

5. **切入角度**：从三个维度鼓励 RL 探索——(1) 用融合试错和自验证的 CoT 数据做冷启动，(2) 过采样增加 RL 训练的采样多样性，(3) 熵奖励 + 动态锚点正则化稳定训练。

6. **核心 idea**：通过精心设计的 SFT 初始化和 RL 训练技巧，让开源 LLM 获得类似 o1 的推理能力和推理时缩放行为。

## 方法详解

### 整体框架

T1 的训练分为两个阶段：

1. **SFT 初始化阶段**：用合成的 CoT 数据对基础 LLM 进行监督微调，使其具备基本的"长思考"能力
2. **RL 训练阶段**：用强化学习进一步优化模型的推理策略，鼓励更多探索

输入：数学推理问题 → T1 生成包含试错、回溯、自验证的长 CoT → 输出最终答案

### 关键设计

1. **合成 CoT 数据（SFT 初始化）**:
    - **功能**：构造融合了 trial-and-error（试错）和 self-verification（自我验证）的 CoT 训练数据
    - **核心思路**：不同于传统的简洁 CoT，T1 的训练数据模拟人类思考过程——包含尝试、犯错、回溯、验证等环节。这种数据让模型学会在推理过程中主动检查和纠正自己
    - **设计动机**：传统 CoT 数据通常是"一次性正确"的解题过程，模型只学会模仿正确路径而不具备自主纠错能力。加入试错和验证环节让模型在 RL 阶段有更好的起点

2. **过采样策略（Oversampling）**:
    - **功能**：在 RL 训练中，对每个问题生成更多的候选响应（增加采样数量）
    - **核心思路**：增加 sampling diversity，从 $K$ 个候选中选取奖励信号进行策略更新。更多的采样意味着更大的探索空间
    - **设计动机**：RL 训练中采样多样性不足是导致模型陷入局部最优的主要原因。过采样直接增加了策略优化的搜索空间

3. **熵奖励（Entropy Bonus）**:
    - **功能**：在 RL 的奖励函数中加入策略分布熵作为辅助损失
    - **核心思路**：总奖励 = 任务奖励 + $\beta \cdot H(\pi_\theta)$，其中 $H(\pi_\theta)$ 是策略的熵，$\beta$ 控制探索强度
    - **设计动机**：防止 RL 训练过程中策略过早收敛到某一类解法，保持模型生成多样化推理路径的能力

4. **动态锚点正则化（Dynamic Anchor）**:
    - **功能**：引入动态更新的参考策略作为 KL 散度正则化的锚点
    - **核心思路**：使用 $D_{KL}(\pi_\theta \| \pi_{anchor})$ 进行正则化，但 $\pi_{anchor}$ 不是固定的初始策略，而是随训练动态更新
    - **设计动机**：传统 PPO/RLHF 用固定的 SFT 策略作为 KL 锚点，这限制了 RL 优化能走多远。动态锚点在稳定训练的同时允许更大的策略更新幅度

### 训练策略

- 基础模型：Qwen2.5 系列（7B/14B/32B）和 GLM-4-9B
- SFT 阶段：使用合成 CoT 数据（已在 HuggingFace 发布）
- RL 阶段：基于数学问题的正确性奖励进行策略优化
- 推理时缩放策略：增加推理 token 预算即可提升性能，无需额外验证器

## 实验关键数据

### 主实验

| 模型 | MATH500 | AIME2024 | Omni-math-500 | GPQA |
|------|---------|----------|---------------|------|
| GPT-4o | 76.6 | 9.3 | 26.8 | 53.6 |
| Claude-3.5-sonnet | 78.3 | 16.0 | - | 65.0 |
| Llama-3.3-70B-Instruct | 73.9 | 24.2 | 27.9 | 50.5 |
| Qwen2.5-Math-7B-Instruct | 82.7 | 16.7 | 29.7 | 36.9 |
| o1-preview | 85.5 | 44.6 | - | 72.3 |
| QwQ-32B-Preview | 90.6 | 50.0 | 46.6 | 58.2 |
| **T1-SFT (Qwen2.5-32B)** | 83.4 | 24.9 | 34.6 | 49.5 |
| **T1 (Qwen2.5-32B)** | **92.4** | **50.6** | **49.6** | 56.1 |

### 消融实验（不同基础模型）

| 配置 | MATH500 | AIME2024 | 说明 |
|------|---------|----------|------|
| T1-SFT (GLM-4-9B) | 60.2 | 4.1 | SFT-only, 小模型 |
| T1 (GLM-4-9B) | 65.8 | 9.2 | +RL 后显著提升 |
| T1-SFT (Qwen2.5-14B) | 77.2 | 10.3 | SFT-only, 中模型 |
| T1 (Qwen2.5-14B) | 87.4 | 30.5 | +RL 后 AIME 提升 3 倍 |
| T1-SFT (Qwen2.5-32B) | 83.4 | 24.9 | SFT-only, 大模型 |
| T1 (Qwen2.5-32B) | 92.4 | 50.6 | +RL 后全面超越 QwQ |

### 关键发现

1. **RL 训练的巨大增益**：从 SFT → RL，14B 模型在 AIME2024 上从 10.3 提升到 30.5（约 3 倍），32B 模型从 24.9 到 50.6（约 2 倍），说明 RL 训练带来的探索性推理能力提升远超 SFT
2. **推理时缩放行为**：增加推理 token 预算可以持续提高 T1 的性能，且**不需要额外的验证器**（如 majority voting 或 reward model reranking），这是一种类似 o1 的"原生"推理缩放
3. **开源模型的竞争力**：T1 (32B) 在 MATH500 和 AIME2024 上超越了 QwQ-32B-Preview 和 o1-preview，展示了开源 RL 训练方法的潜力

## 亮点与洞察

- **从 SFT 到 RL 的关键跳跃**：SFT 提供了"思考方式"的蓝图，但 RL 通过自主探索学到了更高质量的推理策略。这种两阶段范式可能成为训练推理模型的标准流程
- **推理时缩放的民主化**：之前只有闭源模型（如 o1）展示了推理时缩放，T1 证明开源模型通过 RL 训练也能获得这一能力
- **探索鼓励机制的系统化设计**：过采样 + 熵奖励 + 动态锚点，三位一体地解决 RL 训练中探索不足的问题

## 局限与展望

1. 当前仅在数学推理任务上验证，对代码生成、逻辑推理等其他推理任务的泛化能力未知
2. RL 训练的计算成本较高（需要大量采样），如何降低训练开销是实际部署的关键
3. 动态锚点的更新策略对最终性能的影响需要更详细的消融研究
4. 推理时缩放在 GPQA 等非数学任务上效果未充分验证

## 相关工作与启发

- **OpenAI o1/o3**：闭源推理模型的先驱，T1 可视为其开源替代方案
- **DeepSeek-R1**：通过 RL 训练提升推理能力的另一个尝试
- **QwQ-32B-Preview**：Qwen 团队的推理模型，T1 在此基础上进一步提升
- **启发**：RL 训练中的探索机制设计可能比模型规模更重要——14B 模型加上好的 RL 训练可以接近 72B 模型的 SFT 效果

## 评分
- 新颖性: ⭐⭐⭐⭐ 系统化地解决 RL 训练中的探索问题，但各组件（熵奖励、过采样）非全新
- 实验充分度: ⭐⭐⭐⭐ 多模型规模、多基准的全面评估，但缺少非数学推理任务
- 写作质量: ⭐⭐⭐⭐ 清晰地阐述了方法和实验，结构合理
- 价值: ⭐⭐⭐⭐⭐ 开源模型的推理时缩放具有重要实用价值，推动了推理模型的开源进展

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] BRITE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](brite_bootstrapping_reinforced_thinking_process_to_enhance_language_model_reason.md)
- [\[ICML 2025\] Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](optimizing_language_models_for_inference_time_objectives_using_reinforcement_lea.md)
- [\[ICCV 2025\] R1-Onevision: Advancing Generalized Multimodal Reasoning through Cross-Modal Formalization](../../ICCV2025/reinforcement_learning/r1-onevision_advancing_generalized_multimodal_reasoning_through_cross-modal_form.md)
- [\[ICML 2025\] Network Sparsity Unlocks the Scaling Potential of Deep Reinforcement Learning](network_sparsity_unlocks_the_scaling_potential_of_deep_reinforcement_learning.md)
- [\[ICML 2026\] Coupled Variational Reinforcement Learning for Language Model General Reasoning](../../ICML2026/reinforcement_learning/coupled_variational_reinforcement_learning_for_language_model_general_reasoning.md)

</div>

<!-- RELATED:END -->
