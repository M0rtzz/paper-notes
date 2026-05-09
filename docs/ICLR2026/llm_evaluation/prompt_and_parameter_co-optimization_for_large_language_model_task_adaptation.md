---
title: >-
  [论文解读] Prompt and Parameter Co-Optimization for Large Language Model Task Adaptation
description: >-
  [ICLR 2026][LLM评测] 提出 MetaTuner 框架，通过共享元编码器同时生成查询特定的提示和 LoRA 参数，使提示优化与微调相互增强，并设计监督正则化损失解决离散-连续混合优化问题，在 MATH、GSM8K、HotpotQA、CosmosQA 上一致超越独立的提示优化和微调方法。
tags:
  - ICLR 2026
  - LLM评测
  - 微调
  - 联合优化
  - LoRA
  - 离散-连续优化
---

# Prompt and Parameter Co-Optimization for Large Language Model Task Adaptation

**会议**: ICLR 2026  
**arXiv**: [2509.24245](https://arxiv.org/abs/2509.24245)  
**代码**: [GitHub](https://github.com/BoXiaohe/MetaTuner)  
**领域**: LLM评测  
**关键词**: 提示优化, 微调, 联合优化, LoRA, 离散-连续优化

## 一句话总结

提出 MetaTuner 框架，通过共享元编码器同时生成查询特定的提示和 LoRA 参数，使提示优化与微调相互增强，并设计监督正则化损失解决离散-连续混合优化问题，在 MATH、GSM8K、HotpotQA、CosmosQA 上一致超越独立的提示优化和微调方法。

## 研究背景与动机

### 两种 LLM 增强范式

大语言模型有两种互补的增强策略：

- **提示优化 (Prompt Optimization)**：通过显式自然语言优化输入，激活模型已有知识；适合泛化场景但难以适应大规模数据的复杂模式
- **微调 (Fine-tuning)**：通过隐式参数更新适配任务；擅长学习复杂模式但高度依赖训练时的提示选择

### 核心问题

两种方法各有局限，且**先前工作都是独立研究它们**，协同潜力未被挖掘：

- 微调在次优提示下性能显著下降——甚至可能低于纯提示优化
- 提示优化中编码的知识可能与模型参数冲突
- 两者优化空间不同（提示是离散的，参数是连续的），联合优化存在技术挑战

### 统一形式化

将提示和参数统一到一个优化目标中：

$$\min_{\theta, p_i} \sum_{i=1}^{N} \mathcal{L}(\mathcal{M}_\theta(p_i, x_i), y_i)$$

其中 $\theta$ 是模型参数，$p_i$ 是输入特定的提示。将提示视为"特殊参数"，寻找最优的提示-参数组合。

## 方法详解

### 整体框架

MetaTuner 由三个核心组件组成：

1. **元编码器 (Meta Encoder)**：共享的底层编码器 $\phi_s$，编码输入查询
2. **提示解码器 (Prompt Decoder)**：参数 $\phi_p$，从编码表示生成查询特定的自然语言提示
3. **参数解码器 (Parameter Decoder)**：参数 $\phi_q$，从编码表示生成查询特定的 LoRA 参数

### 提示生成的连续化

为解决离散优化问题，先设定初始提示 $\tilde{p}$，用 LLM $\mathcal{G}$ 改写：

$$p_i = \mathcal{G}_\phi(\tilde{p}, x_i)$$

将目标改为对连续参数 $\phi$ 的优化：

$$\min_{\theta, \phi} \sum_{i=1}^{N} \mathcal{L}(\mathcal{M}_\theta(\mathcal{G}_\phi(\tilde{p}, x_i), x_i), y_i)$$

### 关键设计：共享-私有参数机制

提示生成器 $\mathcal{G}$ 和参数生成器 $\mathcal{F}$ 共享编码层 $\phi_s$：

$$\min_{\phi_s, \phi_p, \phi_q} \sum_{i=1}^{N} \mathcal{L}(\mathcal{M}_{\mathcal{F}_{(\phi_s, \phi_q)}(\tilde{p}, x_i)}(\mathcal{G}_{(\phi_s, \phi_p)}(\tilde{p}, x_i), x_i), y_i)$$

- 共享参数 $\phi_s$：使两种方法互相正则化
- 私有参数 $\phi_p, \phi_q$：各自保留独立探索空间

### 参数解码器具体实现

采用 LoRA 生成方式，从隐藏状态 $h_i$ 推导 LoRA 矩阵：

$$\theta_i^b = \text{MM}(\text{ReLU}(\text{MM}(W_d^b, h_i)), W_u^b)$$
$$\theta_i^a = \text{MM}(\text{ReLU}(\text{MM}(W_d^a, h_i)), W_u^a)$$

其中 $\text{MM}$ 为矩阵乘法，$W_d, W_u$ 构成参数解码器的可学习参数。

### 损失函数：监督正则化

为解决提示生成中的不可导问题，设计两项损失：

$$\min_{\phi_s, \phi_p, \phi_q} \underbrace{\sum_{(x_i, y_i) \in D_1} \mathcal{L}(\mathcal{M}_{\mathcal{F}(\tilde{p}, x_i)}(\mathcal{G}_{(\phi_s, \phi_p')}(\tilde{p}, x_i), x_i), y_i)}_{\text{主任务损失（冻结 } \phi_p' \text{）}} + \underbrace{\sum_{(x_i, p_i) \in D_2} \alpha \cdot \mathcal{L}(\mathcal{G}_{(\phi_s, \phi_p)}(\tilde{p}, x_i), p_i)}_{\text{监督正则化}}$$

- 第一项：固定 $\phi_p'$ 的任务损失，梯度流经参数解码器
- 第二项：用专家数据集 $D_2$（模型自身 rollout 生成的最优提示）监督训练提示解码器
- 每隔若干步将 $\phi_p$ 同步到 $\phi_p'$

### 框架规格

- 提示生成器 $\mathcal{G}$：Qwen2.5-7B，前 $k$ 层为元编码器，后续层为提示解码器
- 下游模型 $\mathcal{M}$：Qwen2.5-3B，用生成的 LoRA 参数微调
- 两种训练策略：MetaTuner-I（交替优化）和 MetaTuner-J（联合优化）

## 实验关键数据

### 主实验：4 个数据集上的全面比较

| 方法 | MATH | GSM8K | HotpotQA | CosmosQA |
|------|------|-------|----------|----------|
| **提示优化方法** | | | | |
| RLPrompt | 31.33 | 53.15 | 43.00 | 81.20 |
| BPO | 32.67 | 58.00 | 43.90 | 82.05 |
| OPRO | 22.00 | 75.06 | 25.55 | 69.10 |
| **微调方法** | | | | |
| SFT | 41.33 | 61.41 | 43.20 | 82.65 |
| DPO | 43.78 | 63.68 | 44.70 | 87.90 |
| PPO | 41.78 | 62.02 | 45.85 | 84.10 |
| **混合方法** | | | | |
| BetterTogether | 41.56 | 67.93 | 52.30 | 89.80 |
| **MetaTuner-I** | 48.22 | 78.54 | **55.75** | 92.15 |
| **MetaTuner-J** | **48.67** | **78.92** | 54.56 | **92.25** |

MetaTuner 在所有 4 个数据集上大幅领先：MATH +4.89（vs DPO），GSM8K +10.99（vs BetterTogether），HotpotQA +3.45。

### 消融实验

| 变体 | MATH | GSM8K | HotpotQA | CosmosQA |
|------|------|-------|----------|----------|
| MetaTuner (w/o F) 去微调 | 48.00 | 77.79 | 54.05 | 91.10 |
| MetaTuner (w/o P) 去提示 | 46.22 | 78.54 | 53.90 | 91.00 |
| MetaTuner (w/o S) 去共享 | 46.67 | 77.86 | 53.65 | 91.50 |
| **MetaTuner 完整** | **48.67** | **78.92** | **54.56** | **92.25** |

去掉任一组件均导致约 1% 的绝对精度下降，共享机制的贡献尤为显著。

### 其他关键实验

**共享深度分析**：7B 模型最佳共享比例为 K/4，3B 模型为 3K/4——大模型容量足够时应少共享以保持专化，小模型需更多共享保持一致性。

**Gumbel-Softmax 对比**：监督正则化显著优于 Gumbel-Softmax，后者的连续松弛引入梯度偏差。

**泛化实验**：在 MATH+HotpotQA+CosmosQA 上训练，在 GSM8K 上测试，MetaTuner 仍优于所有基线。

### 关键发现

1. **混合方法一致优于独立方法**：验证了提示和参数优化的互补性
2. **MetaTuner 相对 BetterTogether 提升 10-17%**：共享编码和监督正则化是关键
3. **联合优化 (J) 略优于交替优化 (I)**：但在复杂任务上交替可能更稳定
4. **Rollout 数量不宜过多**：过度探索导致策略频繁波动和过拟合

## 亮点与洞察

1. **统一视角新颖**：将提示视为"特殊参数"，用统一损失函数连接离散和连续优化
2. **共享-私有机制设计巧妙**：既保证知识共享又允许独立探索
3. **监督正则化解决不可导问题**：比 Gumbel-Softmax 等替代方案有效得多
4. **端到端可训练**：从输入到提示和参数的完整生成管道
5. **OOD 泛化有效**：跨数据集泛化证明方法学到了可迁移的提示-参数协同策略

## 局限性

1. 引入了较大的额外计算开销（元编码器 + 双解码器），实际部署成本未详细分析
2. 需要预先确定初始提示 $\tilde{p}$，初始提示的质量可能影响最终效果
3. 实验仅在 3B/7B 规模验证，更大模型（70B+）的适用性未知
4. 生成查询特定的 LoRA 参数在每次推理时都需额外计算，推理延迟需关注
5. 对 $D_2$ 数据集的生成依赖模型自身 rollout，初期策略差时可能产生低质量监督

## 相关工作与启发

- **OPRO (Yang et al. 2024)**：LLM 作为提示优化器，MetaTuner 通过参数协同大幅超越
- **BetterTogether (Soylu et al. 2024)**：最直接可比的混合方法，但缺乏知识共享机制
- **LoRA (Hu et al. 2022)**：MetaTuner 的参数生成基于 LoRA，但生成方式是查询条件化的
- **启发**：提示和参数不应孤立优化，未来的 LLM 训练框架应原生支持两者的协同

## 评分

- **新颖性**: ⭐⭐⭐⭐ — 首次将提示优化和微调统一到端到端可训练框架
- **理论深度**: ⭐⭐⭐☆ — 形式化清晰但理论贡献有限，主要是工程设计
- **实验充分度**: ⭐⭐⭐⭐⭐ — 4 个数据集、10+ 基线、丰富的消融和分析实验
- **实用价值**: ⭐⭐⭐⭐ — 性能提升显著，但部署复杂度较高
- **总评**: ⭐⭐⭐⭐☆ — 问题重要且方案优雅，实验全面，对 LLM 后训练有启发价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Prompt and Parameter Co-Optimization for Large Language Models](prompt_and_parameter_co-optimization_for_large_language_models.md)
- [\[ICLR 2026\] Breaking the Correlation Plateau: On the Optimization and Capacity Limits of Attention-Based Regressors](breaking_the_correlation_plateau_on_the_optimization_and_capacity_limits_of_atte.md)
- [\[ICLR 2026\] Revisiting the Past: Data Unlearning with Model State History](revisiting_the_past_data_unlearning_with_model_state_history.md)
- [\[ICLR 2026\] Predicting LLM Reasoning Performance with Small Proxy Model](predicting_llm_reasoning_performance_with_small_proxy_model.md)
- [\[ICLR 2026\] ASIDE: Architectural Separation of Instructions and Data in Language Models](aside_architectural_separation_of_instructions_and_data_in_language_models.md)

</div>

<!-- RELATED:END -->
