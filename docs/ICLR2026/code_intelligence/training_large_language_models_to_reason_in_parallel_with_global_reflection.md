---
title: >-
  [论文解读] Training Large Language Models to Reason in Parallel with Global Forking Tokens
description: >-
  [ICLR2026][并行推理] 提出 Set Supervised Fine-Tuning (SSFT)，通过引入全局分叉 token 和基于二部匹配的集合损失，训练 LLM 从单个控制 token 触发多样且正确的推理模式，在 Pass@1 和 Cons@k 上均超越标准 SFT+GRPO。
tags:
  - ICLR2026
  - 并行推理
  - 全局分叉token
  - 集合监督微调
  - 二部匹配
  - 多样性推理
---

# Training Large Language Models to Reason in Parallel with Global Forking Tokens

**会议**: ICLR2026  
**arXiv**: [2510.05132](https://arxiv.org/abs/2510.05132)  
**代码**: [GitHub](https://github.com/Sheng-J/SSFT)  
**领域**: llm_alignment  
**关键词**: 并行推理, 全局分叉token, 集合监督微调, 二部匹配, 多样性推理

## 一句话总结

提出 Set Supervised Fine-Tuning (SSFT)，通过引入全局分叉 token 和基于二部匹配的集合损失，训练 LLM 从单个控制 token 触发多样且正确的推理模式，在 Pass@1 和 Cons@k 上均超越标准 SFT+GRPO。

## 背景与动机

- 测试时并行采样（如 self-consistency、Best-of-N）是提升 LLM 推理性能的有效手段，但依赖于生成多样且正确的推理路径
- 对于困难问题，触发不同推理模式的"分叉 token"通常深埋在采样树中，增加温度虽然能提高多样性但会降低准确性
- 理论研究表明：仅提高温度无法保证多样性，除非模型被显式训练以确保覆盖(coverage)
- 标准 SFT 在多推理轨迹上训练会导致模式坍塌——不同控制 token 生成几乎相同的推理

## 核心问题

如何训练 LLM 使其能通过简单的控制 token 在推理开始时就触发多样且正确的推理模式？

## 方法详解

### 全局分叉 Token

- 预留 $N$ 个特殊 token $\{$`<think i>`$\}_{i=1}^N$（实验中 $N=6$）
- 目标：给定问题 $\mathbf{x}$，不同的 `<think i>` 能启动 $M$ 条不同的推理轨迹（$M=4$）

### SSFT 损失函数

将并行推理建模为**集合预测问题**，通过二部匹配实现：

**Step 1: 计算代价矩阵**

对每个 (分叉token $g^{(i)}$, 推理轨迹 $\mathbf{r}^{(j)}$) 对，计算 NTP 损失：
$$\mathcal{L}_{\text{matching}}(g^{(i)}, \mathbf{r}^{(j)}) = -\text{sg}\left(\frac{1}{T_\mathbf{r}} \sum_{t=1}^{T_\mathbf{r}} \log \pi_\theta(r_t^{(j)}|\mathbf{x}, g^{(i)}, \mathbf{r}_{<t}^{(j)})\right)$$

其中 $\text{sg}(\cdot)$ 为 stop-gradient 操作，节省显存。

**Step 2: 匈牙利算法求最优匹配**

$$\hat{\boldsymbol{\sigma}} = \arg\min_{\boldsymbol{\sigma} \in \mathfrak{S}_P} \sum_{j=1}^M \mathcal{L}_{\text{matching}}(g^{(\boldsymbol{\sigma}(j))}, \mathbf{r}^{(j)})$$

**Step 3: 在最优匹配下训练**

$$\mathcal{L}_{\text{Hungarian}}(\theta) = -\mathbb{E}_{\mathbf{x}, \mathbf{R} \sim \mathcal{D}}\left[\sum_{j=1}^M \sum_t \log \pi_\theta(r_t^{(j)}|\mathbf{x}, g^{(\hat{\sigma}(j))}, \mathbf{r}_{<t}^{(j)})\right]$$

### 计算效率

- 仅用前 $L < T_\mathbf{r}$ 个 token 计算匹配代价（实验中 $L \approx 1000$）
- 时间复杂度降低 $k = T_\mathbf{r}/L$ 倍，反向传播仅在 $M$ 条匹配序列上进行

### GFPO：全局分叉策略优化

- SSFT 后施加少量 RL 步骤，仅优化全局分叉 token $g^{(i)}$ 的输出分布
- 实现极简：只需在现有 GRPO 代码中添加几行 slicing

### 推理策略

- **Cons@k**：用不同 `<think i>` 分别提示，多数投票
- **Pass@1**：通过图启发式选择覆盖最多推理轨迹的 $g^{(i^\star)}$，或用 GFPO 让模型自行采样最优 $g^{(i)}$

## 实验关键数据

### Pass@1 性能对比 (Qwen2.5-32B-Instruct 基座)

| 方法 | AIME24 | AIME25 | MATH-500 | GPQA-D | LCB(v5) |
|------|--------|--------|----------|--------|---------|
| Qwen2.5-32B-Instruct | 15.80 | 10.40 | 80.40 | 47.00 | 23.35 |
| s1.1-32B (单轨迹) | 54.79 | 44.27 | 92.16 | 62.12 | – |
| SFT-mixed-32B (多轨迹) | 58.23 | 51.96 | 88.49 | 59.96 | 32.34 |
| **SSFT-32B** | **64.06** | **58.13** | **90.02** | 60.39 | **38.92** |
| SSFT-32B-GFPO | 64.22 | **58.80** | 89.90 | **62.48** | **42.10** |

### Cons@6 与 Cons@32 (并行推理)

| 方法 | AIME24 Cons@6 | AIME25 Cons@6 | AIME25 Cons@32 |
|------|--------------|--------------|----------------|
| s1.1-32B | 70.30 | 53.33 | 63.33 |
| SFT-mixed-32B | 73.94 | 70.00 | 76.67 |
| **SSFT-32B** | **75.45** | **73.94** | **86.67** |
| SSFT-32B-GFPO | **76.67** | **78.48** | 83.33 |

- SSFT 在 AIME24 上 Pass@1 超越 SFT-mixed 8.33%，在 AIME25 上超越 6.57%
- Cons@32 在 AIME25 上达到 86.67%
- 代码生成 OOD 任务 LCB 上同样大幅领先

### 消融：最优匹配 vs 随机匹配

| 匹配方式 | AIME24 Pass@1 | AIME25 Cons@6 |
|---------|--------------|--------------|
| 随机匹配 | 61.77 | 67.58 |
| **最优匹配** | **64.06** | **73.94** |

## 亮点

1. **类 DETR 的集合损失首次引入语言建模**：将目标检测中的二部匹配思想迁移到推理多样性问题上，设计精巧
2. **全局分叉 token 的涌现行为**：不同 `<think i>` 自动学习到不同推理长度和策略，无需人工指定
3. **模式坍塌问题的优雅解决**：标准 SFT 会使所有控制 token 坍塌为同一模式，SSFT 保持了多样性
4. **训练数据高效**：仅用 1K 问题，每题4条推理轨迹，就在 32B 模型上取得大幅提升
5. **代码生成的 OOD 泛化**：在代码任务上同样有效

## 局限性 / 可改进方向

- 仅在 Qwen2.5 系列上充分验证，Llama 等其他模型的效果增益较小
- 匹配代价计算引入额外开销（虽然论文指出影响很小）
- 推理轨迹的多样性依赖于教师模型的质量
- 未探索 $N$ 和 $M$ 更大规模时的行为
- GFPO 的 RL 步骤较少，更深入的 RL 训练可能带来更多收益

## 与相关工作的对比

| 方法 | 核心思路 | 多样性保证 | 需要额外标注 | Pass@1 |
|------|---------|-----------|-------------|--------|
| Self-consistency | 温度采样+投票 | 无保证 | 否 | 低 |
| Multiverse | 并行 CoT 改写 | 隐式 | 教师模型 | 中 |
| 标准 SFT (多轨迹) | 重复训练 | 模式坍塌 | 否 | 中 |
| **SSFT** | **集合匹配损失** | **显式保证** | **教师轨迹** | **高** |

## 启发与关联

- 二部匹配 + 语言建模的范式有潜力推广到其他需要多样性输出的任务（如翻译、代码生成多方案）
- 全局分叉 token 可以看作一种可学习的提示/模式选择器
- 与 mixture-of-experts 的思路有精神联系，但作用于推理路径层面

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 将 DETR 的集合损失引入语言建模，全局分叉 token 概念新颖
- 实验充分度: ⭐⭐⭐⭐ — 多基准、消融充分，但模型多样性有限
- 写作质量: ⭐⭐⭐⭐ — 形式化清晰，图表直观
- 价值: ⭐⭐⭐⭐ — 为并行测试时计算提供了新的训练范式

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models](dro-instructzero_distributionally_robust_prompt_optimization_for_large_language_.md)
- [\[ICLR 2026\] Learning to Reason without External Rewards](learning_to_reason_without_external_rewards.md)
- [\[ICLR 2026\] DiaBlo: Diagonal Blocks Are Sufficient For Finetuning](diablo_diagonal_blocks_are_sufficient_for_finetuning.md)
- [\[AAAI 2026\] SPAN: Benchmarking and Improving Cross-Calendar Temporal Reasoning of Large Language Models](../../AAAI2026/code_intelligence/span_benchmarking_and_improving_cross-calendar_temporal_reasoning_of_large_langu.md)
- [\[ACL 2026\] KoCo-Bench: Can Large Language Models Leverage Domain Knowledge in Software Development?](../../ACL2026/code_intelligence/koco-bench_can_large_language_models_leverage_domain_knowledge_in_software_devel.md)

<!-- RELATED:END -->
