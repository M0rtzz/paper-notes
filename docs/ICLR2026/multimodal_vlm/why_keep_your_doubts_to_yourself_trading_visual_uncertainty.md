---
title: >-
  [论文解读] Why Keep Your Doubts to Yourself? Trading Visual Uncertainties in Multi-Agent Bandit Systems
description: >-
  [ICLR 2026][多模态][multi-agent systems] 提出 Agora 框架，将多智能体 VLM 协调问题重新建模为去中心化的不确定性交易市场，通过将认知不确定性拆分为可交易资产（感知/语义/推理三维），并用基于盈利性驱动的交易协议和 Thompson Sampling 代理人实现成本感知的最优分配，在五个多模态基准上以超 3 倍成本节省获得至多 +8.5% 准确率提升。
tags:
  - ICLR 2026
  - 多模态
  - 多模态VLM
  - VLM coordination
  - uncertainty quantification
  - market mechanism
  - Thompson Sampling
---

# Why Keep Your Doubts to Yourself? Trading Visual Uncertainties in Multi-Agent Bandit Systems

**会议**: ICLR 2026  
**arXiv**: [2601.18735](https://arxiv.org/abs/2601.18735)  
**代码**: 无  
**领域**: 多模态VLM  
**关键词**: multi-agent systems, VLM coordination, uncertainty quantification, market mechanism, Thompson Sampling  

## 一句话总结

提出 Agora 框架，将多智能体 VLM 协调问题重新建模为去中心化的不确定性交易市场，通过将认知不确定性拆分为可交易资产（感知/语义/推理三维），并用基于盈利性驱动的交易协议和 Thompson Sampling 代理人实现成本感知的最优分配，在五个多模态基准上以超 3 倍成本节省获得至多 +8.5% 准确率提升。

## 背景与动机

1. **VLM 多智能体系统成本失控**：随着 VLM 规模扩大，协调异构智能体的运营成本急剧攀升，经济可行性成为部署瓶颈，亟需从"暴力堆算力"转向精细化资源管理。
2. **现有聚合策略（MoA）错误假设独立性**：Mixture-of-Agents 依赖共识投票，但共享架构偏置导致误差高度相关，共识反而放大系统性幻觉，无法保证收敛到正确答案。
3. **现有路由策略（KABB）忽略成本与不确定性结构**：知识路由器基于历史表现和语义相似度的代理分数进行选择，评分函数中既无成本项也无不确定性向量，属于"成本无感"和"结构无感"的双重盲区。
4. **理论可证的次优性**：论文形式化定义了"Agnostic Coordination"，并证明任何同时满足成本无感和结构无感的协调机制在最优智能体非最便宜时必然次优（Theorem 1）。
5. **信息不对称与有限理性的经济学挑战**：多智能体系统本质上是去中心化的经济问题，每个智能体有私有信息和异构能力，需要机制设计来揭示私有信息并引导全局最优。
6. **缺乏不确定性交易的范式**：已有工作将不确定性视为单一标量或整体负担，从未将其分解为结构化、可定价、可交易的资产来实现精细化管理，这是 Agora 的核心创新点。

## 方法详解

### 整体框架：Agora 去中心化不确定性交易市场

- **做什么**：将多智能体 VLM 协调重构为微观经济学市场，不确定性是可交易资产，智能体是交易参与方，代理人（Broker）是市场撮合者。
- **为什么**：直接将协调问题映射为经济优化（式 1），最小化总成本 $\mathcal{C}$ 同时约束残余不确定性 $\|\mathbf{u}_{\text{final}}\| \leq \epsilon$，避免启发式代理带来的理论盲区。
- **怎么做**：三阶段流程——(1) 将查询不确定性"铸币"为三维可交易资产；(2) 代理人用市场感知的 Thompson Sampling 选择初始处理智能体；(3) 迭代执行盈利性交易直至市场均衡。

### 关键设计 1：三维不确定性资产化

- **做什么**：将总不确定性 $\mathbf{u}$ 分解为认知不确定性（可交易）和偶然不确定性（不可交易），认知部分进一步拆为感知 $u_{\text{perc}}$、语义 $u_{\text{sem}}$、推理 $u_{\text{inf}}$ 三维向量。
- **为什么**：向量化使不同类型不确定性可独立定价和交易，解决"结构无感"问题。每个维度对应不同认知能力，某些智能体擅长感知但不擅长推理，精细化分配可降低成本。
- **怎么做**：每个智能体 $a_i$ 维护不确定性组合 $\mathbf{U}(a_i, t)$，由自身基础不确定性和从其他智能体获得的交易不确定性线性叠加（式 3），历史交易记录加权聚合。

### 关键设计 2：盈利性驱动交易协议

- **做什么**：定义交易赢利条件，只有当转移不确定性包能降低系统总成本时才执行交易。
- **为什么**：直接消除"成本无感"问题——交易准入规则显式包含成本向量 $\mathbf{c}$ 和专长矩阵 $\Xi$，违反了 Theorem 1 的次优条件。
- **怎么做**：计算成本变化量 $\Delta\mathcal{C}(T_{ij}) = T_{ij} \cdot [c_j(1 - \xi_j) - c_i]$（式 4），仅当 $\Delta\mathcal{C} < 0$ 且接收方有剩余容量时执行交易（式 5），每次交易是全局代价函数的贪心下降步。

### 关键设计 3：市场感知代理人（Broker）

- **做什么**：基于 Thompson Sampling 扩展的智能代理人，为每个任务选择经济效用最高的初始处理智能体。
- **为什么**：交易协议是局部贪心优化，一个好的初始分配可显著缩短收敛路径、降低总成本。
- **怎么做**：代理人计算多因素效用函数 $\tilde{\theta}_S^{(t)}$（式 6），综合考虑期望收益减成本、任务距离衰减、战略效用、智能体协同效应和时间衰减，通过 Thompson Sampling 平衡探索与利用。

## 实验结果

### 实验 1：五基准综合性能（Table 1）

| 模型 | MMMU | MMBench | MathVision | InfoVQA | CC-OCR |
|------|------|---------|------------|---------|--------|
| qwen2.5vl-72b | 70.2% | 88.4% | 39.3% | 87.3% | 79.8% |
| gemini-2.0-flash | 70.7% | 83.0% | 41.3% | 83.2% | 73.1% |
| gemini-2.5-pro | 81.7% | 88.3% | 63.5% | 81.0% | 73.0% |
| InternVL3-78B | 72.2% | 87.7% | 43.1% | 84.1% | 80.3% |
| **Agora** | **79.2%**(+8.5) | **89.5%**(+1.1) | **44.3%**(+2.0) | **88.9%**(+1.6) | **81.2%**(+1.4) |

**发现**：Agora 使用 5 个中小型 VLM 组成的智能体池，在 MMBench、InfoVQA、CC-OCR 上超越所有单一模型包括 gemini-2.5-pro，MMMU 上 +8.5% 是最大增益；仅在 MathVision 上不敌专用推理模型 gemini-2.5-pro（63.5% vs 44.3%），但仍强于池中所有单模型。

### 实验 2：路由与多智能体策略比较（Figure 4）

| 方法 | MMBench Acc. | 相对成本 | 最终认知不确定性 |
|------|-------------|---------|----------------|
| **Agora** | **89.50%** | 1.00 | **0.16** |
| KABB-VLM | 87.12% | 1.24× | 0.21 |
| MOA | 86.65% | 3.11× | 0.25 |
| FrugalGPT | 81.50% | 0.73× | 0.27 |
| RouteLLM | 80.85% | 0.91× | 0.30 |

**发现**：Agora 在准确率最高的同时成本最低（归一化为 1.0），KABB 和 MOA 在相近准确率下成本分别高出 24%/211%；低成本路由方法 FrugalGPT/RouteLLM 虽然便宜但准确率下降 8-9 个点且残余不确定性更高，验证了 Agora 在帕累托前沿的优势。

### 实验 3：MAB 策略消融（Table 2）

| 选择策略 | MMMU Acc. | 最终不确定性↓ | UAPS↑ |
|----------|----------|--------------|-------|
| **Agora (MAB)** | **79.0%** | **0.15** | **70.5%** |
| KABB + Trading | 76.0% | 0.25 | 65.5% |
| PPO + Trading | 74.0% | 0.28 | 62.0% |
| DQN + Trading | 73.0% | 0.30 | 60.0% |
| No Trading | 75.5% | 0.22 | 65.0% |

**发现**：MAB 代理人比最佳启发式 KABB 高 3.0%、比 RL 方法（PPO/DQN/A2C/MCTS）高 5-6%，证明经济效用函数设计是优于纯强化学习和启发式的；即使去掉交易只用代理人选初始模型也有 75.5%，交易机制额外贡献 3.5%。

## 亮点

- **理论驱动的范式创新**：从经济学角度形式化多智能体协调，证明现有方法的理论次优性，再设计非无感机制来突破
- **不确定性资产化**：首次将认知不确定性分解为三维可交易资产，使模糊的"信心"概念变为可量化、可定价、可交易的经济对象
- **成本效率的帕累托最优**：在五个异构基准上同时提升准确率和降低成本，特别是 MMMU +8.5% 且成本降低 3 倍以上
- **算法简洁**：核心交易规则（式 5）仅用两个条件判断，实现高效且可解释的协调

## 局限性

- 交易协议基于贪心下降，收敛到局部最优而非全局最优；当智能体池异构性不足时，交易空间有限
- 三维不确定性分解（感知/语义/推理）的量化方法依赖提示工程和启发式，缺乏自动化的不确定性估计
- 实验中所有模型都通过 OpenRouter API 调用，成本模型依赖 API 定价，自部署场景下成本结构可能完全不同
- 仅评估了选择题/简答题形式的视觉理解任务，未验证在开放式生成或视频理解等场景的适用性

## 相关工作对比

| 维度 | Agora（本文） | MoA (Mixture-of-Agents) | KABB-VLM |
|------|-------------|------------------------|----------|
| 协调机制 | 去中心化市场交易 | 中心化聚合投票 | 启发式路由评分 |
| 成本建模 | 显式成本项，盈利性交易 | 无成本感知 | 无成本感知 |
| 不确定性处理 | 三维向量可交易 | 标量共识 | 标量语义相似 |
| MMBench Acc. | 89.50% | 86.65% | 87.12% |
| 相对成本 | 1.00× | 3.11× | 1.24× |

## 评分

- ⭐⭐⭐⭐ 创新性：将经济学市场机制引入多智能体 VLM 协调，理论与方法均有原创贡献
- ⭐⭐⭐⭐ 实验充分度：五个基准、多种对比方法（路由/MAS/RL/消融），成本-性能帕累托分析全面
- ⭐⭐⭐ 清晰度：经济学概念和符号较多，论文整体偏长，阅读门槛较高
- ⭐⭐⭐⭐ 实用价值：提供了可落地的多智能体 VLM 成本优化方案，对 API 场景尤其实用

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Multimodal Prompt Optimization: Why Not Leverage Multiple Modalities for MLLMs](multimodal_prompt_optimization_why_not_leverage_multiple_modalities_for_mllms.md)
- [\[ICLR 2026\] TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding](tabledart_dynamic_adaptive_multi-modal_routing_for_table_understanding.md)
- [\[ICLR 2026\] Enhancing Multi-Image Understanding through Delimiter Token Scaling](enhancing_multi-image_understanding_through_delimiter_token_scaling.md)
- [\[ICLR 2026\] MMR-Life: Piecing Together Real-life Scenes for Multimodal Multi-image Reasoning](mmr-life_piecing_together_real-life_scenes_for_multimodal_multi-image_reasoning.md)
- [\[ICLR 2026\] Steering and Rectifying Latent Representation Manifolds in Frozen Multi-Modal LLMs for Video Anomaly Detection](steering_and_rectifying_latent_representation_manifolds_in_frozen_multi-modal_ll.md)

</div>

<!-- RELATED:END -->
