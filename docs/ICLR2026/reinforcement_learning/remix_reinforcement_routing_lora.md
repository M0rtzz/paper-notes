---
title: >-
  [论文解读] ReMix: Reinforcement Routing for Mixtures of LoRAs in LLM Finetuning
description: >-
  [ICLR 2026][强化学习] ReMix 发现现有 Mixture-of-LoRAs 模型存在严重的路由权重坍缩问题（即使激活 k>1 个 LoRA，有效 LoRA 数也迅速降到 1），提出用非可学习的常数路由权重确保所有激活 LoRA 平等贡献，并用 RLOO 强化学习梯度估计器训练路由器，显著优于 SOTA PEFT 方法。
tags:
  - ICLR 2026
  - 强化学习
  - 路由权重坍缩
  - 强化学习路由
  - RLOO
  - 参数高效微调
---

# ReMix: Reinforcement Routing for Mixtures of LoRAs in LLM Finetuning

**会议**: ICLR 2026  
**arXiv**: [2603.10160](https://arxiv.org/abs/2603.10160)  
**代码**: 无  
**领域**: 强化学习  
**关键词**: Mixture-of-LoRAs, 路由权重坍缩, 强化学习路由, RLOO, 参数高效微调

## 一句话总结

ReMix 发现现有 Mixture-of-LoRAs 模型存在严重的路由权重坍缩问题（即使激活 k>1 个 LoRA，有效 LoRA 数也迅速降到 1），提出用非可学习的常数路由权重确保所有激活 LoRA 平等贡献，并用 RLOO 强化学习梯度估计器训练路由器，显著优于 SOTA PEFT 方法。

## 研究背景与动机

**领域现状**：LoRA 是最流行的参数高效微调方法，Mixture-of-LoRAs 通过在每层维护多个 LoRA 并用路由器选择子集来扩展模型容量。现有方法（如 MixLoRA、HydraLoRA）使用可学习的路由权重，通过 softmax 计算每个 LoRA 的权重。

**现有痛点**：作者发现现有 Mixture-of-LoRAs 路由器存在一个严重的根本性缺陷——**路由权重坍缩**。即使设定激活 k>1 个 LoRA，在训练过程中，softmax 路由权重会迅速集中到单一 LoRA 上（有效支撑大小 ESS 降到 1），其他 LoRA 的权重趋近于 0。这意味着额外 k-1 个 LoRA 的计算完全被浪费。

**核心矛盾**：可学习路由权重允许端到端训练但天然倾向于不平衡——Theorem 1 证明在 Gaussian 初始化下，有效 LoRA 数以高概率极小（如 8 个 LoRA 中，84% 概率只有 ≤2 个有效）。而且这种不平衡在训练过程中还会加剧。

**本文目标**：(1) 理论和实验揭示路由权重坍缩问题；(2) 设计不会坍缩的路由器；(3) 解决非可学习权重带来的不可微问题。

**切入角度**：根本重新思考路由器设计——放弃可学习权重，改用常数权重确保所有激活 LoRA 平等贡献。由此产生的梯度不可计算问题，重新建模为强化学习问题来解决。

**核心 idea**：用常数路由权重 $\omega$ 消除坍缩（$ESS = k$），用 RLOO 梯度估计器训练路由器做 LoRA 选择，推理时用 top-k 选择（理论证明当路由器训练充分时 top-k 是最优策略）。

## 方法详解

### 整体框架

每层有 $n$ 个 LoRA 和一个路由器。路由器 $\mathbf{q}^{(l)} = \text{softmax}(\mathbf{P}^{(l)}\mathbf{x}^{(l)})$ 产生概率分布。训练时，从该分布无替换采样 $k$ 个 LoRA，赋予常数权重 $\omega$，计算 $\mathbf{y}^{(l)} = \mathbf{W}^{(l)}\mathbf{x}^{(l)} + \omega \sum_{j=1}^{k} \mathbf{B}_{i_j}^{(l)}\mathbf{A}_{i_j}^{(l)}\mathbf{x}^{(l)}$。用 RLOO 估计路由器的梯度。推理时，确定性地选 top-k 概率最高的 LoRA。

### 关键设计

1. **非可学习常数路由权重**:

    - 功能：从根本上消除路由权重坍缩，确保所有激活 LoRA 平等贡献
    - 核心思路：将路由权重从可学习的 softmax 输出替换为固定常数 $\omega$，激活的 LoRA 权重为 $\omega$，未激活的为 0。$\omega$ 可选 LoRA 型 $2/(kr)$ 或 rsLoRA 型 $2/\sqrt{kr}$。这保证了 $ESS(\boldsymbol{\pi}^{(l)}) = k$，即有效 LoRA 数恒等于激活数，从根本上避免了坍缩
    - 设计动机：当权重固定为常数，问题从"如何分配权重"转变为"如何选择 LoRA 子集"。所有被选中的 LoRA 都必须全力贡献，不存在某个 LoRA 被边缘化的可能

2. **RLOO 强化学习梯度估计器**:

    - 功能：为不可微的离散 LoRA 选择提供无偏梯度估计
    - 核心思路：将路由器训练视为 RL 问题——SFT 损失 $\mathcal{L}(\mathfrak{I})$ 作为负奖励，路由分布 $\mathbf{q}^{(l)}$ 作为策略。独立采样 $M$ 个 selection $\mathfrak{J}_1, \ldots, \mathfrak{J}_M$，每个 selection 包含所有层的 LoRA 选择。RLOO 梯度估计器 $\hat{\mathbf{G}}_{\mathbf{P}^{(l)}} = \frac{1}{M-1}\sum_{m}(\mathcal{L}(\mathfrak{I}_m) - \bar{\mathcal{L}})\nabla_{\mathbf{P}^{(l)}}\log Q(\mathfrak{J}_m)$，其中 $\bar{\mathcal{L}}$ 是均值 baseline 用于方差控制。该估计器是无偏的
    - 设计动机：标准 REINFORCE 方差太大，RLOO 用 leave-one-out 方式计算 baseline（直接用其他采样的平均损失），无需额外的 value 网络就能有效降低方差

3. **Top-k 推理选择与理论保证**:

    - 功能：推理时确定性地选择最优 LoRA 子集
    - 核心思路：Theorem 2 证明：只要路由器训练得足够好（最优子集被采中的概率 > 50%），则 top-k 选择保证恢复最优子集。直觉是：如果最优子集 $\mathcal{I}^*$ 被采中概率最高，则 $\mathcal{I}^*$ 中每个 LoRA 的边际概率也最高，因此 top-k 就能选出 $\mathcal{I}^*$
    - 设计动机：随机采样虽然对训练必要（提供探索），但推理时引入不必要的随机性。Top-k 是理论最优的确定性策略

### 损失函数 / 训练策略

LoRA 参数用标准 SFT 梯度 $\nabla_{\mathbf{A},\mathbf{B}}\mathcal{L}(\mathfrak{I})$ 更新。路由器参数用 RLOO 梯度估计器更新。训练计算量可通过增大采样数 $M$ 来扩展——这是 ReMix 独特的优势，因为基线方法的训练计算量是固定的。使用 Llama 3 8B 作为基础模型，用 LLaMA-Factory 训练。

## 实验关键数据

### 主实验

| 方法 | GSM8K | HumanEval Pass@1 | ARC-c | 平均 | 参数量 |
|------|-------|------------------|-------|------|--------|
| LoRA | 59.21 | 26.83 | 83.05 | 56.36 | 0.112B |
| rsLoRA | 62.47 | 28.66 | 82.71 | 57.95 | 0.028B |
| MixLoRA | 61.87 | 28.05 | 82.37 | 57.43 | 0.101B |
| HydraLoRA | 62.47 | 20.12 | 82.71 | 55.10 | 0.084B |
| **ReMix** | **65.66** | **32.93** | **83.73** | **60.77** | **0.070B** |

ReMix 在三个基准上一致超越所有基线，平均提升 2.82 准确率。

### 消融实验

| 配置 | GSM8K 准确率 | 说明 |
|------|-------------|------|
| 完整 ReMix | 最高 | RLOO + top-k |
| 去除 RLOO | 显著下降 | 路由器训练不充分 |
| 去除 top-k（随机采样推理） | 下降 | 引入不必要随机性 |
| Rank-kr LoRA (k=4, r=8) | 59.21 | 单个高秩 LoRA |
| k 个 Rank-r LoRA (ReMix) | 64.22 | 证明激活了多样化子集 |
| 训练计算 M=2→32 | 56.03→58.83 | 持续改善 |

### 关键发现

- **路由权重坍缩**在 MixLoRA 中确实存在且迅速恶化——ESS 从初始 ~4 在 1000 步内降至 1，之后再也不回升
- ReMix (k=4, r=8) 显著优于 Rank-32 LoRA（64.22 vs 59.21），证明 ReMix 确实激活了不同的 LoRA 子集，而非始终选择同一子集
- ReMix 的训练计算量可扩展（$M$ 从 2 到 32 持续改善），这是基线方法所不具备的独特优势
- 10% 的额外训练时间换来 15.97% 的准确率相对提升，效率显著

## 亮点与洞察

- **路由权重坍缩的理论揭示**是本文最重要的贡献之一——Theorem 1 给出了 ESS 的概率上界，将这个普遍存在但被忽视的问题严格化。这个发现对所有使用 softmax 路由的 MoE 架构都有警示意义
- **用 RL 训练路由器**的思路非常优雅——常数权重使路由器"选择"LoRA 而非"加权"LoRA，这恰好是离散决策问题，天然适合 RL。RLOO 的引入同时解决了梯度估计和方差控制
- **可扩展训练计算**是一个独特优势——对于追求极致性能的场景，可以直接增大 $M$ 来提升效果，而不需要改变模型结构

## 局限与展望

- 额外的 $M$ 次前向传播增加了训练成本（虽然每步仅增加 ~10%）
- 理论分析基于 Gaussian 初始化，训练后期的坍缩机制可能更复杂
- 仅在 Llama 3 8B 上验证，更大模型和更多任务的泛化性有待确认
- 常数路由权重是否是唯一解？渐进的权重均衡（如引入 load balancing loss）可能也有效

## 相关工作与启发

- **vs MixLoRA (Li et al., 2024)**: MixLoRA 用标准可学习路由权重，本文证明其会坍缩；ReMix 用常数权重+RL 消除坍缩
- **vs MoE 中的 load balancing**: Switch Transformer 等用 auxiliary loss 平衡专家使用率，但那是跨样本的平衡；本文关注的是单个样本内不同 LoRA 的权重平衡
- **vs VB-LoRA (Li et al., 2024)**: VB-LoRA 用向量量化共享 LoRA 参数，参数效率更高但性能较差；ReMix 在参数效率和性能间取得更好平衡

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 路由权重坍缩的理论发现+RL路由的解决方案，两个贡献都很有洞见
- 实验充分度: ⭐⭐⭐⭐ 三个基准、详细消融、效率和扩展性分析
- 写作质量: ⭐⭐⭐⭐⭐ 问题动机极强，理论和实验紧密配合
- 价值: ⭐⭐⭐⭐⭐ 对 MoE/MoLoRA 范式有根本性改进，即插即用的实用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Routing, Cascades, and User Choice for LLMs](routing_cascades_and_user_choice_for_llms.md)
- [\[ICLR 2026\] Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control](towards_bridging_the_gap_between_large-scale_pretraining_and_efficient_finetunin.md)
- [\[ICLR 2026\] $\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving](textbfre2_unlocking_llm_reasoning_via_reinforcement_learning_with_re-solving.md)
- [\[ICLR 2026\] Trinity: An Evolved LLM Coordinator](trinity_an_evolved_llm_coordinator.md)
- [\[ICLR 2026\] References Improve LLM Alignment in Non-Verifiable Domains](references_improve_llm_alignment_in_non-verifiable_domains.md)

</div>

<!-- RELATED:END -->
