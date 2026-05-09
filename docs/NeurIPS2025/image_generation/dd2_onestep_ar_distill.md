---
title: >-
  [论文解读] Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation
description: >-
  [NeurIPS 2025][图像生成][自回归模型] 本文提出 DD2，将自回归图像模型重新解释为条件分数模型，通过条件分数蒸馏（CSD）损失训练单步生成器匹配原始 AR 模型的输出分布，在 ImageNet-256 上实现 FID 仅增加约 2-3.5 的单步生成，获得 8-238 倍加速，相比 DD1 将单步性能差距缩小 67%。
tags:
  - NeurIPS 2025
  - 图像生成
  - 自回归模型
  - 单步生成
  - 分数蒸馏
  - 图像生成加速
  - 流匹配
---

# Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation

**会议**: NeurIPS 2025  
**arXiv**: [2510.21003](https://arxiv.org/abs/2510.21003)  
**代码**: [GitHub](https://github.com/imagination-research/Distilled-Decoding-2)  
**领域**: 图像生成  
**关键词**: 自回归模型, 单步生成, 分数蒸馏, 图像生成加速, 流匹配

## 一句话总结
本文提出 DD2，将自回归图像模型重新解释为条件分数模型，通过条件分数蒸馏（CSD）损失训练单步生成器匹配原始 AR 模型的输出分布，在 ImageNet-256 上实现 FID 仅增加约 2-3.5 的单步生成，获得 8-238 倍加速，相比 DD1 将单步性能差距缩小 67%。

## 研究背景与动机
1. **领域现状**: 图像 AR 模型（如 VAR、LlamaGen）达到 SOTA 质量，但逐 token 生成导致推理慢。
2. **现有痛点**: DD1 通过流匹配构造噪声到数据的确定性映射实现单步生成，但该映射难以学习，单步性能下降明显。
3. **核心矛盾**: DD1 依赖预定义映射限制灵活性；需要一种不依赖固定映射的分布匹配方法。
4. **本文目标**: 训练单步生成器使其输出分布匹配 AR 教师模型，无需预定义映射。
5. **切入角度**: 将 AR 模型视为每个 token 位置的条件分数模型。
6. **核心 idea**: 联合训练单步生成器和条件引导网络，用 CSD 损失对齐每个 token 位置的条件分数。

## 方法详解

### 整体框架
教师 AR 模型提供真实条件分数，引导网络学习生成器分布的条件分数，CSD 损失驱动两者对齐。生成器 $G_\theta$ 接受噪声 $\varepsilon$ 直接输出完整 token 序列。

### 关键设计
1. **教师 AR 模型作为条件分数模型**: 将 AR 模型输出的概率向量 $p = (p_1, ..., p_V)$ 重新解释为 RectFlow 噪声调度下的条件分数函数 $s(x_t, t, p)$，闭式表达为加权高斯混合的梯度。每个 token 位置的生成视为以前序 token 为条件的连续流匹配过程。
2. **条件分数蒸馏（CSD）损失**: 在每个 token 位置 $i$，对齐引导网络（学习生成器分布的分数）与教师模型（提供真实分数）的条件分数，条件为前 $i-1$ 个 token。理论证明 CSD 损失最优时生成器分布精确匹配 AR 模型分布。
3. **引导网络**: 独立网络学习生成器分布的条件分数 $s(q_i^t, t | q_{<i})$，用标准 AR-diffusion 损失训练。与生成器交替优化。
4. **DD1 初始化**: 用 DD1 预训练结果初始化生成器，显著加速 DD2 收敛（12.3 倍训练加速）。

### 损失函数 / 训练策略
- 生成器和引导网络交替训练
- 基于 RectFlow 噪声调度的分数函数闭式解
- 支持 VAR（10步→1步）和 LlamaGen（256步→1步）两种架构

## 实验关键数据

| 模型 | 步数 | FID | 加速 |
|------|------|-----|------|
| VAR-d30 原始 | 10 | 3.40 | 1× |
| VAR-d30 DD2 | **1** | 5.43 | **8.0×** |
| LlamaGen-XXL 原始 | 256 | 4.11 | 1× |
| LlamaGen-XXL DD2 | **1** | 7.58 | **238×** |
| DD1 (VAR-d30) | 1 | 9.30 | 8× |

### 关键发现
- DD2 将 DD1 的单步性能差距缩小 67%
- 训练速度比 DD1 快 12.3 倍
- CSD 损失理论上保证分布精确匹配

### 训练效率对比

| 配置 | 训练时间 | FID | 说明 |
|------|---------|-----|------|
| DD1 | 1.0x | 9.30 | 基线 |
| DD2 (冷启动) | 12.3x更慢 | ~6.0 | 无DD1初始化 |
| DD2 (DD1初始化) | **0.08x** | **5.43** | 推荐配置 |

### 不同AR模型上的效果

| 教师模型 | 原始步数 | 原始FID | DD2 FID | 加速比 |
|---------|---------|---------|---------|-------|
| VAR-d16 | 10 | 4.19 | 6.48 | 8.0× |
| VAR-d30 | 10 | 3.40 | 5.43 | 8.0× |
| LlamaGen-XL | 256 | 5.62 | 8.92 | 238× |
| LlamaGen-XXL | 256 | 4.11 | 7.58 | 238× |


## 亮点与洞察
- 巧妙借鉴扩散模型分数蒸馏思想应用于 AR 模型，但面临完全不同的建模挑战
- 不依赖预定义映射，灵活性更强
- 为 AR 模型的实时生成开辟新可能

## 局限与展望
- 仅在 ImageNet-256 验证，高分辨率（512/1024）和文本条件生成待探索。
- 引导网络增加了训练复杂度（需与生成器交替训练），总训练成本仍较高。
- 单步 FID 仍有一定差距（VAR: 3.40→5.43），多步蒸馏可能进一步改善。
- 依赖离散 codebook 嵌入空间，连续表征的 AR 模型需另行设计。
- 生成器架构选择（如何设计单步生成所有 token 的网络）仍需探索。
- 未与非 AR 生成方法（如扩散模型蒸馏）进行跨范式对比。
- DD1 初始化对 DD2 收敛速度至关重要，说明 DD2 对初始化敏感，冷启动效果可能较差。
- CSD 损失的计算需要对所有 codebook 元素求和，大 codebook 可能带来计算瓶颈。
- 未探索少步（2-4步）蒸馏的效果，可能在质量和速度之间取得更好的平衡。

## 相关工作与启发
- **vs DD1**: DD1 依赖预定义映射（流匹配 ODE），DD2 用分数蒸馏实现更灵活的分布匹配
- **vs 扩散蒸馏 (DMD/SiD)**: 目标和挑战完全不同——AR 是离散序列的条件生成，扩散是连续去噪
- **vs MaskGIT**: MaskGIT 通过并行解码减少步数但仍需多步，DD2 实现真正单步
- **vs 投机解码**: 投机解码需要草稿模型且仍是多步，DD2 将全部步数压缩为一步


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
- 新颖性: ⭐⭐⭐⭐⭐ AR 模型的条件分数蒸馏是重要理论贡献
- 实验充分度: ⭐⭐⭐⭐ 两个强基线模型的全面评估
- 写作质量: ⭐⭐⭐⭐ 理论推导清晰
- 价值: ⭐⭐⭐⭐⭐ 对 AR 图像生成加速有重大意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[NeurIPS 2025\] Physics-Constrained Flow Matching: Sampling Generative Models with Hard Constraints](physics-constrained_flow_matching_sampling_generative_models_with_hard_constrain.md)
- [\[NeurIPS 2025\] Ψ-Sampler: Initial Particle Sampling for SMC-Based Inference-Time Reward Alignment in Score Models](psi-sampler_initial_particle_sampling_for_smc-based_inference-time_reward_alignm.md)
- [\[NeurIPS 2025\] Understand Before You Generate: Self-Guided Training for Autoregressive Image Generation](understand_before_you_generate_self-guided_training_for_autoregressive_image_gen.md)
- [\[NeurIPS 2025\] Riemannian Consistency Model](riemannian_consistency_model.md)
- [\[NeurIPS 2025\] Real-Time Execution of Action Chunking Flow Policies](real-time_execution_of_action_chunking_flow_policies.md)

</div>

<!-- RELATED:END -->
