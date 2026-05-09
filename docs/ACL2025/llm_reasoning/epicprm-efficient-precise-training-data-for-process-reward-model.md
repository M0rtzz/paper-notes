---
title: >-
  [论文解读] EpicPRM: An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning
description: >-
  [ACL 2025][LLM推理][过程奖励模型] 本文提出 EpicPRM 框架，通过基于困惑度的贡献量化和自适应二分搜索算法，高效精确地构建高质量过程监督训练数据集 Epic50k，其训练的 PRM 以不到 PRM800k 10% 的数据量达到了相当甚至更好的监督性能。
tags:
  - ACL 2025
  - LLM推理
  - 过程奖励模型
  - 数学推理
  - 蒙特卡洛估计
  - 自适应二分搜索
  - 数据质量
---

# EpicPRM: An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning

**会议**: ACL 2025  
**arXiv**: [2503.02382](https://arxiv.org/abs/2503.02382)  
**代码**: [https://github.com/xiaolizh1/EpicPRM](https://github.com/xiaolizh1/EpicPRM)  
**领域**: LLM推理  
**关键词**: 过程奖励模型, 数学推理, 蒙特卡洛估计, 自适应二分搜索, 数据质量

## 一句话总结

本文提出 EpicPRM 框架，通过基于困惑度的贡献量化和自适应二分搜索算法，高效精确地构建高质量过程监督训练数据集 Epic50k，其训练的 PRM 以不到 PRM800k 10% 的数据量达到了相当甚至更好的监督性能。

## 研究背景与动机

1. **领域现状**：过程监督奖励模型（PRM）通过逐步监督推理过程，已被证明比结果监督更有效地提升 LLM 的数学推理能力。
2. **现有痛点**：构建过程监督数据的两种方法各有缺陷——人工标注（如 PRM800k）质量高但成本巨大，自动标注（如 Math-Shepherd）成本低但标注质量差。
3. **核心矛盾**：自动标注中的蒙特卡洛（MC）估计使用 $M/N$ 计数法估计正确概率存在固有的采样偶然性，且完成者（completer）的纠错能力会导致即使有错误步骤也能得到正确答案（如图1所示），进一步降低标注精度。
4. **本文目标**：在有限计算预算下，构建数量小但质量高的过程监督数据集。
5. **切入角度**：(1) 用困惑度替代计数来量化 MC 估计；(2) 量化每个步骤对最终答案的贡献；(3) 用自适应二分搜索替代顺序搜索来定位第一个错误步骤。
6. **核心 idea**：数据质量比数量更重要——50k 高精度标注的数据可以超过 800k 粗糙标注的效果。

## 方法详解

### 整体框架

EpicPRM 包含三个关键创新：(1) 用困惑度加权的 MC 估计（$MC_{PPL}$）替代简单计数，提高估计精度；(2) 量化每一步的贡献来判断步骤正确性；(3) 自适应二分搜索算法，根据题目难度动态调整搜索起点和采样数量，大幅降低标注成本。

### 关键设计

1. **困惑度加权 MC 估计（$MC_{PPL}$）**:

    - 功能：更精确地估计从给定状态获得正确答案的概率
    - 核心思路：对每个 rollout 计算其困惑度 $PPL(j; s_t, \theta_k)$，用对数困惑度作为权重替代简单的正确/错误计数。使用 $K$ 个不同能力的 completer 各采样 $N$ 个 rollouts，最终估计为 $MC_{PPL}(s_t, \theta_{1:K}) = \frac{1}{K}\sum_{k=1}^{K}\frac{\sum_{m=1}^{M}\log PPL(j;s_t,\theta_k)}{\sum_{n=1}^{N}\log PPL(j;s_t,\theta_k)}$。
    - 设计动机：计数法在采样量不足时有严重的偶然性（如2次抛硬币都是正面不代表100%概率）。困惑度直接计算模型生成每个 rollout 的概率，消除了采样偶然性的影响。

2. **步骤贡献量化**:

    - 功能：判断每一步对最终正确答案的贡献，识别无贡献或负贡献的步骤
    - 核心思路：计算每个步骤的贡献为 $\Delta MC_{PPL}(s_t) = MC_{PPL}(s_t) - MC_{PPL}(s_{t-1})$。如果 $\Delta < 0$，说明该步骤降低了获得正确答案的概率，很可能是错误步骤。
    - 设计动机：传统方法仅看当前状态的 MC 值，忽略了错误步骤后 completer 可能自行纠错的问题。通过看步骤间的增量变化，可以更精确地定位错误。

3. **自适应二分搜索**:

    - 功能：高效定位链式推理中的第一个错误步骤
    - 核心思路：(1) 根据题目难度动态调整搜索起始位置——简单题的第一个错误通常在后面，难题在前面（如图2所示）；(2) 根据难度动态调整每个位置的 rollout 采样数——简单题需要更少的采样就能准确判断。相比传统二分搜索减少了约20%的 MC 估计次数，相比顺序搜索减少了 64.39% 的标注成本。
    - 设计动机：OmegaPRM 的标准二分搜索不考虑题目难度，对所有题目使用相同策略，浪费了计算资源。

### 损失函数 / 训练策略

- 使用多个不同能力的 LLM（如 Qwen2.5-Math-7B-Instruct、DeepSeek-Math-7B-Instruct 等）作为 completers 生成多样化的推理链
- PRM 训练使用标准的 token-level 分类损失

## 实验关键数据

### 主实验

| 数据集 | 数据量 | Best-of-N (GSM8K) | Best-of-N (MATH) |
|--------|--------|-------------------|------------------|
| PRM800k | 800k | 78.2 | 42.0 |
| Math-Shepherd | 440k | 80.2 | 42.6 |
| **Epic50k** | **50k** | **82.1** | **44.8** |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| MC count vs MC_PPL | MC_PPL更优 | 困惑度加权消除采样偶然性 |
| 顺序搜索 vs 标准二分 vs 自适应二分 | 自适应最优 | 成本降低64.39%，精度更高 |
| 单一completer vs 多completer | 多completer更优 | 不同模型互补，覆盖更多推理路径 |
| 步骤贡献 vs 不使用 | 贡献量化更优 | 更精确识别错误步骤 |

### 关键发现

- 数据质量远比数量重要：50k 高质量数据 > 800k 中等质量数据
- 题目难度与第一个错误步骤位置有很强的相关性（简单题错误多在后面，难题错误多在前面）
- completer 的纠错能力是传统 MC 估计失准的主要原因

## 亮点与洞察

- **困惑度替代计数**是一个非常简洁有效的改进——它利用了模型本身的概率信息，无需增加采样量就能提高估计精度。这个思路可以迁移到任何使用 MC 估计的场景。
- **自适应二分搜索**利用题目难度先验信息优化搜索策略，体现了"根据问题特性调整算法"的工程智慧。
- 数据质量 > 数据量的发现，对 PRM 训练有重要指导意义。

## 局限与展望

- 目前仅在数学推理上验证，未推广到代码生成等其他需要过程监督的场景
- 困惑度加权假设 completer 的概率校准良好，实际上可能存在校准偏差
- 多 completer 策略增加了推理成本，需要权衡收益

## 相关工作与启发

- **vs PRM800k**: 人工标注虽然精确但极其昂贵，Epic50k 以自动化方式达到甚至超越其效果
- **vs Math-Shepherd**: 使用简单 MC 计数，数据量大但质量不够，Epic50k 以 1/9 的数据量实现更好效果
- **vs OmegaPRM**: 使用标准二分搜索，EpicPRM 的自适应策略更高效

## 评分

- 新颖性: ⭐⭐⭐⭐ 困惑度加权和自适应二分搜索各自不全新但组合有效
- 实验充分度: ⭐⭐⭐⭐ 消融分析全面，与多个数据集对比
- 写作质量: ⭐⭐⭐⭐ 方法动机清晰，数学推导完整
- 价值: ⭐⭐⭐⭐ 开源数据集和框架，对 PRM 训练有实用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] An Efficient and Precise Training Data Construction Framework for Process-Supervised Reward Model in Mathematical Reasoning](an_efficient_and_precise_training_data_construction_framework_for_process-superv.md)
- [\[ACL 2025\] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification](safe_math_reasoning.md)
- [\[ACL 2025\] ProcessBench: Identifying Process Errors in Mathematical Reasoning](processbench_identifying_process_errors_in_mathematical_reasoning.md)
- [\[ACL 2025\] Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](enhancing_mathematical_reasoning_in_llms_by_stepwise_correction.md)
- [\[ACL 2025\] Chain-of-Reasoning: Towards Unified Mathematical Reasoning in Large Language Models](chain-of-reasoning_towards_unified_mathematical_reasoning_in_large_language_mode.md)

</div>

<!-- RELATED:END -->
