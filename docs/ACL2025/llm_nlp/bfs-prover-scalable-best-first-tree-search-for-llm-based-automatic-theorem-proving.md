---
title: >-
  [论文解读] BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving
description: >-
  [ACL 2025][LLM/NLP][自动定理证明] 本文提出 BFS-Prover，一个基于最优优先搜索（BFS）的自动定理证明系统，通过战略性数据过滤、DPO 优化和长度归一化三项创新，在 MiniF2F 测试集上以 72.95% 的准确率达到了 SOTA，证明了简单的 BFS 方法在适当扩展后可以超越复杂的 MCTS 方法。
tags:
  - ACL 2025
  - LLM/NLP
  - 自动定理证明
  - 最优优先搜索
  - 专家迭代
  - DPO
  - Lean4
---

# BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving

**会议**: ACL 2025  
**arXiv**: [2502.03438](https://arxiv.org/abs/2502.03438)  
**代码**: https://huggingface.co/ByteDance-Seed/BFS-Prover-V1-7B  
**领域**: LLM推理  
**关键词**: 自动定理证明, 最优优先搜索, 专家迭代, DPO, Lean4

## 一句话总结

本文提出 BFS-Prover，一个基于最优优先搜索（BFS）的自动定理证明系统，通过战略性数据过滤、DPO 优化和长度归一化三项创新，在 MiniF2F 测试集上以 72.95% 的准确率达到了 SOTA，证明了简单的 BFS 方法在适当扩展后可以超越复杂的 MCTS 方法。

## 研究背景与动机

1. **领域现状**：自动定理证明（ATP）是评估 LLM 推理能力的关键基准，主流方法依赖 MCTS 和价值函数来导航巨大的证明搜索空间。
2. **现有痛点**：MCTS 和价值函数在 ATP 中存在独特困难——证明搜索缺乏清晰的终止条件（不像棋类有明确输赢），中间进度难以评估，分支因子更大且动态变化。
3. **核心矛盾**：BFS（最优优先搜索）因为缺乏探索机制和偏向浅层路径而被认为不适合 ATP，但复杂方法如 MCTS 引入了过多的计算开销和系统复杂度。
4. **本文目标**：验证 BFS 是否能在大规模定理证明中达到有竞争力的表现，具体分为三个子问题：如何过滤训练数据、如何利用负样本、如何克服深度偏见。
5. **切入角度**：作者观察到 BFS 的两个主要缺陷（缺乏探索和深度偏见）可以通过训练策略和评分函数改进来缓解，而不需要复杂的搜索算法。
6. **核心 idea**：通过专家迭代框架 + 战略性数据过滤 + DPO 负样本学习 + 长度归一化，将简单的 BFS 扩展为高效的定理证明系统。

## 方法详解

### 整体框架

BFS-Prover 采用专家迭代（Expert Iteration）流水线：在每一轮中，先用 beam search 过滤简单问题，再用 BFS 温度采样搜索更难的问题，收集成功的证明路径作为 SFT 数据，同时收集编译器错误作为 DPO 负样本。多轮迭代后，策略 LLM 逐步提升，能解决越来越难的定理。

### 关键设计

1. **长度归一化 BFS**:

    - 功能：消除 BFS 对深层路径的固有偏见
    - 核心思路：BFS 的节点评分函数为 $\text{score}(s_L) = \frac{\sum_{t=0}^{L-1} \log p(a_t|s_t)}{L^\alpha}$，其中 $\alpha \in [0,1]$ 是可调的长度归一化参数。当 $\alpha > 0$ 时，较长路径的累积对数概率被路径长度归一化，从而鼓励探索更深的证明路径。
    - 设计动机：标准 BFS 依赖累积对数概率，深层节点天然获得更低的分数，导致系统偏向浅层证明。长度归一化直接解决了这个结构性偏见。

2. **带自过滤的专家迭代**:

    - 功能：确保训练数据聚焦于更难的定理
    - 核心思路：每轮迭代先用 beam search（宽度 32）识别当前策略模型可以轻松解决的定理并将其从语料库中移除，但不将这些简单证明加入训练数据。然后用温度采样 BFS 搜索剩余更难的问题，收集成功证明的 (state, tactic) 对加入累积训练集。
    - 设计动机：beam search 是确定性的，能解决的定理说明当前模型已掌握。过滤掉这些简单样本，训练数据逐轮聚焦于更具挑战性的推理模式，使策略 LLM 持续进步。

3. **基于编译器反馈的 DPO**:

    - 功能：利用搜索过程中自然产生的负样本来改善策略分布
    - 核心思路：在证明路径上的每个状态 $s$，将正确的 tactic $a_w$（位于证明路径上）与导致 Lean 编译器错误的 tactic $a_l$ 配对，形成偏好对 $(s, a_w, a_l)$，然后用 DPO 损失进行训练。
    - 设计动机：SFT 只学习正样本，而 DPO 通过显式引入负信号，使策略模型学会避免无效 tactic，从而提高 BFS 的样本效率和搜索时的扩展性。

### 损失函数 / 训练策略

- SFT 阶段：在所有累积的 (state, tactic) 对上训练 3 个 epoch，学习率从 $2 \times 10^{-5}$ 余弦衰减到 $1 \times 10^{-6}$
- DPO 阶段：在编译器错误偏好对上训练 1 个 epoch，学习率 $5 \times 10^{-6}$，KL 正则化参数 $\beta = 10$
- 根据每轮新数据量选择 SFT 或 DPO：数据量大时用 SFT，数据量小时用 DPO（因为 DPO 样本效率更高）

## 实验关键数据

### 主实验

| 方法 | 是否需要 Critic | 搜索方法 | MiniF2F-test |
|------|----------------|----------|-------------|
| DeepSeek-Prover-V1.5 | 否 | MCTS | 63.5% |
| InternLM2.5-StepProver | 是 | BFS | 65.9% |
| HunyuanProver | 是 | BFS | 68.4% |
| **BFS-Prover** | **否** | **BFS** | **70.83%** |
| **BFS-Prover (累积)** | **否** | **BFS** | **72.95%** |

### 消融实验

| 配置 | MiniF2F-test (pass@2048) | 说明 |
|------|------------------------|------|
| SFT only | 70.38% | 仅 SFT 训练 |
| SFT + DPO | 70.83% | 加 DPO 后稳定提升 |
| $\alpha=0.0$ | - | 最小归纳偏见，适合专家迭代 |
| $\alpha=0.5$ | - | 平衡探索与利用，适合推理 |
| 累积多个 $\alpha$ | 72.95% | 不同 $\alpha$ 互补发现更多证明 |

### 关键发现

- DPO 在所有 pass 数量下一致优于纯 SFT，证明了负样本学习的有效性
- BFS 性能随 pass 数量呈对数增长（logarithmic scaling），说明单纯增加计算资源有其极限
- 专家迭代过程中，证明长度分布从均值 10.2 步逐渐右移到 16.7 步，说明系统逐步解决更难的定理
- tactic 长度分布保持多样性，未出现模式坍缩，这对有效证明至关重要

## 亮点与洞察

- **简单方法 + 精心扩展策略 > 复杂方法**：这一发现挑战了"ATP 需要 MCTS"的主流观点。BFS-Prover 不需要价值函数和 MCTS，却超越了所有现有方法，说明算法简洁性在正确扩展策略下可以成为优势。
- **自过滤的专家迭代**是一个非常巧妙的设计：beam search 作为"难度探测器"自动将训练数据聚焦到难题上，这个想法可以迁移到其他需要 curriculum learning 的场景。
- **编译器反馈天然提供 DPO 偏好对**：这是 ATP 领域独有的优势——形式系统的编译器可以自动生成高质量负样本，无需人工标注。

## 局限与展望

- 目前仅使用 7B 参数模型，更大模型（32B/70B）可能捕捉更复杂的数学推理模式，但会带来推理延迟和内存挑战
- BFS 的对数扩展规律暗示单纯增加搜索预算的收益递减，需要更好的扩展方式
- 仅在 MiniF2F 上验证，未测试更广泛的数学领域
- 长证明可能超出 7B 模型的上下文窗口限制

## 相关工作与启发

- **vs DeepSeek-Prover-V1.5**: 使用 MCTS + 全证明生成，BFS-Prover 用更简单的 BFS + tactic 级生成超越了它
- **vs InternLM2.5-StepProver**: 需要额外的 critic 模型（等效双倍推理开销），BFS-Prover 无需 critic 即超越
- **vs HunyuanProver**: 同样需要 critic + BFS，BFS-Prover 说明关键不在 critic 而在训练策略

## 评分

- 新颖性: ⭐⭐⭐⭐ 挑战主流观点，证明简单方法可以超越复杂方法，但核心组件各自不完全新颖
- 实验充分度: ⭐⭐⭐⭐⭐ 在 MiniF2F 上 SOTA，有详细的消融和分布分析，附录含 IMO 证明展示
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图表丰富，理论与实验结合好
- 价值: ⭐⭐⭐⭐⭐ 开源模型和代码，结果具有很强的实用价值和启发意义

<!-- RELATED:START -->

## 相关论文

- [\[ACL 2025\] Big5-Chat: Shaping LLM Personalities Through Training on Human-Grounded Data](big5-chat_shaping_llm_personalities_through_training_on_human-grounded_data.md)
- [\[ACL 2025\] Dynamic Parallel Tree Search for Efficient LLM Reasoning](dynamic_parallel_tree_search_for_efficient_llm_reasoning.md)
- [\[ACL 2025\] Zero-Shot Belief: A Hard Problem for LLMs](zero-shot_belief_a_hard_problem_for_llms.md)
- [\[ACL 2025\] Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](unintended_harms_of_value-aligned_llms_psychological_and_empirical_insights.md)
- [\[ACL 2025\] Can LLMs Interpret and Leverage Structured Linguistic Representations? A Case Study with AMRs](can_llms_interpret_and_leverage_structured_linguistic_representations_a_case_stu.md)

<!-- RELATED:END -->
