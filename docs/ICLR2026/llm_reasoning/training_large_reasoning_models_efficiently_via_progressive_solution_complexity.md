---
title: >-
  [论文解读] Training Large Reasoning Models Efficiently via Progressive Thought Encoding
description: >-
  [ICLR2026][LLM推理][大推理模型] 提出 Progressive Thought Encoding，通过在 KV 缓存被淘汰时将 token 信息编码为固定大小的 LoRA 权重更新，使大推理模型能在有限缓存下进行高效 RL 训练，同时保持长程推理能力。
tags:
  - ICLR2026
  - LLM推理
  - 大推理模型
  - RL训练效率
  - KV缓存压缩
  - 参数高效微调
  - 渐进思维编码
---

# Training Large Reasoning Models Efficiently via Progressive Thought Encoding

**会议**: ICLR2026  
**arXiv**: [2602.16839](https://arxiv.org/abs/2602.16839)  
**代码**: 未开源  
**领域**: LLM推理  
**关键词**: 大推理模型, RL训练效率, KV缓存压缩, 参数高效微调, 渐进思维编码

## 一句话总结

提出 Progressive Thought Encoding，通过在 KV 缓存被淘汰时将 token 信息编码为固定大小的 LoRA 权重更新，使大推理模型能在有限缓存下进行高效 RL 训练，同时保持长程推理能力。

## 背景与动机

- 大推理模型(LRM)通过 RL 训练需要长 rollout 才能获得结果奖励，自回归解码主导了时间和内存开销
- 滑动窗口缓存策略可以限制内存，但丢弃中间推理 token 会破坏长程上下文理解，导致推理质量下降
- 实验证实：对 Qwen 模型使用滑动窗口缓存进行 RL 训练，性能明显低于全缓存训练
- 核心矛盾：如何在固定缓存容量下让推理模型仍能"看到"所有之前的 token

## 核心问题

如何在严格的内存预算下高效训练 LRM，同时不牺牲推理准确度？

## 方法详解

### Cache-aware GRPO 目标

将标准 GRPO 改造为缓存感知版本。在每步 $t$，缓存策略 $D$ 选择裁剪后的上下文：

$$\pi_\theta^D(y|p) = \prod_{t=1}^T \pi_\theta(y_t | \mathcal{C}_t^D)$$

目标函数：
$$\mathcal{L}_{\text{GRPO}}^D(\theta_g; \theta_{\text{ref}}) = \mathbb{E}_{y \sim \pi_{\theta_g}^D(\cdot|p)}\left[r(y) - \beta \text{KL}(\pi_{\theta_g}^D(\cdot|p) \| \pi_{\theta_{\text{ref}}}(\cdot|p))\right]$$

### Progressive Thought Encoding

核心思想：不丢弃被淘汰的 token，而是从中学习并更新轻量参数。

**1. 上下文状态计算**

当缓存满时，被淘汰 token 的 key/value 为 $K_e, V_e$，利用可学习的全局查询 $q_g$ 计算上下文状态：

$$S_e = \left((W_Q^a q_g)(W_K^a K_e)^T\right)(W_V^a V_e)$$

其中 $W_Q^a, W_K^a, W_V^a$ 将全局查询和被淘汰的 key/value 映射到压缩潜空间。

**2. LoRA 权重更新**

将上下文状态转换为 LoRA 权重增量：
$$\Delta W = A \cdot S_e \cdot B$$

$A, B$ 为映射矩阵，将压缩的上下文信息注入模型权重。

**3. 渐进式更新**

- 模型以更新后的策略 $\pi_{\theta'}^D$ 继续解码，其中 $\theta' = \theta + \Delta W$
- 每次缓存满时计算新的 $S_e'$，累积更新：$S_e \leftarrow \text{Normalize}(S_e + S_e')$
- 初始化时使用可学习的全局 token $h_g$ 作为 $q_g$ 的载体

**4. 缓存淘汰策略**

- 问题 token 始终保留在缓存中（类似 sink token 机制）
- 仅对思维 token 应用滑动窗口淘汰
- 缓存饱和时淘汰 25% 的 token

### 训练与推理

- 训练时：rollout 过程中持续学习被淘汰 token，LoRA 适配器在线更新
- 推理时：学习到的适配器使模型在受限缓存下保持推理能力
- 不需要回传整个全缓存 rollout 的梯度

## 实验关键数据

### 主实验：不同方法对比 (最大生成长度 3072)

| 模型 | 方法 | 峰值GPU内存 | Math500 | Olympiad | AMC | AIME24 | AIME25 | 平均 |
|------|------|-----------|---------|----------|-----|--------|--------|------|
| Qwen2.5-3B | Baseline | – | 50.8 | 27.2 | 34.3 | 20.0 | 13.3 | 26.9 |
| | LoRA | 82.8% | 53.2 | 27.8 | 35.9 | 20.0 | 16.7 | 28.2 |
| | LoRA_c | 38.0% | 50.0 | 27.7 | 33.1 | 16.7 | 10.0 | 25.6 |
| | **Ours** | **45.3%** | **54.0** | **29.0** | **45.0** | 20.0 | 16.7 | **30.1** |
| Qwen2.5-7B | Baseline | – | 56.8 | 34.7 | 48.4 | 23.3 | 16.6 | 33.1 |
| | LoRA | 85.8% | 59.4 | 38.7 | 50.6 | 30.0 | 26.7 | 38.1 |
| | LoRA_c | 63.1% | 61.2 | 35.9 | 52.5 | 20.0 | 26.7 | 36.7 |
| | **Ours** | **67.2%** | 61.2 | **38.7** | 52.5 | **30.0** | **30.0** | **39.6** |
| DS-R1-8B | Baseline | – | 53.6 | 28.7 | 42.5 | 20.0 | 20.0 | 30.1 |
| | LoRA | 88.7% | 57.4 | 35.3 | 55.0 | 23.3 | 20.0 | 34.9 |
| | LoRA_c | 59.1% | 54.2 | 31.9 | 45.0 | 36.7 | 26.7 | 35.1 |
| | **Ours** | **59.8%** | **57.6** | **39.7** | **60.0** | **56.7** | **43.3** | **45.6** |

### 关键数字

- DS-R1-8B 上平均提升 +15.5%（30.1→45.6），AIME2024 提升 +36.7%，AIME2025 提升 +23.3%
- 峰值 GPU 内存从 88.7% 降至 59.8%（减少近30个百分点）
- 计算量(TFLOPs)从 7.4 降至 4.6（减少38%）
- 相比朴素缓存裁剪(LoRA_c)，平均提升 +10.5%

## 亮点

1. **将缓存淘汰转化为学习机会**：不是简单丢弃 token，而是从中提取信息编码为模型权重更新
2. **训练推理一致性**：训练和推理都在受限缓存下操作，避免了训练-推理不匹配问题
3. **显著的效率提升**：内存减少~50%、计算量减少~38%，且推理准确度不降反升
4. **在 DS-R1-8B 上效果惊人**：平均准确率提升 15.5 个百分点，远超全缓存 LoRA
5. **与 GRPO 无缝集成**：方法可以直接嵌入现有 RL 训练框架

## 局限性 / 可改进方向

- 仅在数学推理任务上验证，其他推理任务（代码、科学）的效果待探索
- 滑动窗口淘汰策略较简单，基于重要性的淘汰可能更有效但计算开销更大
- 全局查询 $q_g$ 的维度和全局 token 数量(32)的敏感性分析不够详细
- LoRA rank 固定为 32，rank 选择对性能的影响未深入分析
- 8 卡 A100 的训练设置对于更大模型的扩展性存疑

## 与相关工作的对比

| 方法 | 核心思路 | 内存效率 | 推理准确度 | 适用场景 |
|------|---------|---------|-----------|---------|
| 全缓存 LoRA | 标准 RL + LoRA | 低 | 基线 | 小模型/短序列 |
| 滑动窗口 LoRA | 裁剪缓存 | 高 | 低于基线 | 受限环境 |
| TTT (test-time training) | 推理时梯度更新 | 中 | 中 | 在线适应 |
| **本方法** | **淘汰 token 编码为权重** | **高** | **超越基线** | **长程推理 RL** |

## 启发与关联

- "从丢弃中学习"的思想与知识蒸馏有精神联系——被淘汰的 token 信息不是丢失而是被压缩保留
- 对 inference-time compute 的优化有重要实际意义：在边缘设备上部署长推理模型
- 可以与其他高效推理方法（投机解码、早停等）结合使用

## 评分

- 新颖性: ⭐⭐⭐⭐ — 将缓存淘汰转化为在线学习是巧妙的想法
- 实验充分度: ⭐⭐⭐⭐ — 三个模型六个基准，对比充分
- 写作质量: ⭐⭐⭐⭐ — 问题定义清晰，方法描述完整
- 价值: ⭐⭐⭐⭐ — 大幅降低 LRM RL 训练成本，实用价值高

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Native Reasoning Models: Training Language Models to Reason on Unverifiable Data](native_reasoning_models_training_language_models_to_reason_on_unverifiable_data.md)
- [\[ICLR 2026\] Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention](towards_safe_reasoning_in_large_reasoning_models_via_corrective_intervention.md)
- [\[ICLR 2026\] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](rfeval_benchmarking_reasoning_faithfulness_under_counterfactual_reasoning_interv.md)
- [\[ICLR 2026\] Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](dynamics-predictive_sampling_for_active_rl_finetuning_of_large_reasoning_models.md)
- [\[ICLR 2026\] When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models](when_reasoning_meets_compression_understanding_the_effects_of_llms_compression_o.md)

</div>

<!-- RELATED:END -->
