---
title: >-
  [论文解读] Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention
description: >-
  [ICLR2026][LLM推理][LRM安全对齐] 提出 Intervened Preference Optimization (IPO)，通过在推理过程中的关键步骤替换合规线索为安全触发器，构造偏好对进行训练，显著提升大推理模型(LRM)思维链推理过程本身的安全性。
tags:
  - ICLR2026
  - LLM推理
  - LRM安全对齐
  - 推理过程安全
  - 过程监督
  - 偏好优化
  - 越狱防御
---

# Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

**会议**: ICLR2026  
**arXiv**: [2509.24393](https://arxiv.org/abs/2509.24393)  
**代码**: 未开源  
**领域**: LLM推理  
**关键词**: LRM安全对齐, 推理过程安全, 过程监督, 偏好优化, 越狱防御

## 一句话总结

提出 Intervened Preference Optimization (IPO)，通过在推理过程中的关键步骤替换合规线索为安全触发器，构造偏好对进行训练，显著提升大推理模型(LRM)思维链推理过程本身的安全性。

## 背景与动机

- 大推理模型(LRM)如 DeepSeek-R1 在复杂问题求解上表现优异，但其思维链(CoT)推理过程中经常包含有害内容
- 即使最终回答看起来安全，推理过程中的不安全内容仍然可被恶意用户利用
- 现有安全对齐方法(如 RealSafe、STAR)主要关注最终回复的安全性，忽视了推理过程本身的安全性
- 实验表明：安全推理几乎必然导致安全回复，但反之不成立——推理不安全而回复安全的情况很常见
- 直接用 GRPO 等 RL 方法对推理安全进行奖励效果有限，因为 rollout 多样性低，约50%的有害 prompt 难以采样到安全推理轨迹

## 核心问题

如何对齐 LRM 的推理过程本身使其安全？核心挑战是：(1) 推理过程安全比回复安全更难优化；(2) RL 方法受限于 rollout 多样性不足导致训练信号弱。

## 方法详解

### 三大关键发现

**发现1：安全触发器(Safety Triggers)**
- 定义 Continuation Safety Ratio (CSR)：对推理轨迹 $z_s$ 中第 $i$ 个 token，用32次采样估计后续安全概率
$$S_i(x, z_s) = \mathbb{E}_{z_c \sim \pi_\theta(\cdot|x, z_s^{\leq i})}[\mathbb{I}(z_s^{\leq i} \| z_c \text{ is safe})]$$
- 发现90%以上的安全轨迹存在 CSR 急剧上升到100%的转折点，且对应句子通常是模型显式识别风险、重构任务或调用安全准则
- 这些句子被称为"安全触发器"，是推理安全的关键步骤

**发现2：合规线索(Compliance Cues)**
- 不安全轨迹中，CSR 急剧下降的转折点与首个合规线索(表达倾向于执行恶意请求的句子)高度相关
- 合规线索出现的 token 位置与 CSR 转折点的 Pearson 相关系数达 **0.85**

**发现3：干预修正的有效性**
- 将不安全轨迹中的首个合规线索替换为安全触发器后，后续生成的有害比例大幅下降
- 干预可迭代应用，累积效果更强

### IPO 方法流程

1. **检测合规线索**：用 GPT-4o 自动检测推理轨迹中首个合规线索位置 $h$（与人工标注一致率>80%）
2. **替换与续写**：将合规线索替换为从安全触发器池 $\mathcal{T}$ 中采样的触发器 $\tau$，然后用模型续写：$\tilde{z}^{\geq h} \sim \pi_\theta(\cdot|x, z^{<h}, \tau)$
3. **构造偏好对**：修正后的安全轨迹 $\tilde{z}$ 与原始不安全轨迹 $z$ 形成偏好对 $(x, \tilde{z} \succ z, h)$
4. **偏好学习**：在分歧点之后的部分进行 DPO 训练

$$\mathcal{L} = -\mathbb{E}_{(x, \tilde{z} \succ z, h) \sim \mathcal{D}}\left[\log \sigma\left(\beta \log \frac{\pi_\theta(\tilde{z}^{\geq h}|x, z^{<h})}{\pi_{\theta_{\text{ref}}}(\tilde{z}^{\geq h}|x, z^{<h})} - \beta \log \frac{\pi_\theta(z^{\geq h}|x, z^{<h})}{\pi_{\theta_{\text{ref}}}(z^{\geq h}|x, z^{<h})}\right)\right]$$

### 与 Reward Shaping 的联系

- CSR 本质上就是安全标签的值函数 $V^\pi(s_t) = \Pr[S(x,z)=1|s_t]$
- IPO 相当于在安全关键步骤注入中间奖励信号，类似于 potential-based reward shaping
- 比 GRPO 的稀疏终端奖励更高效

## 实验关键数据

### 推理安全性 (Reasoning Harmful Ratio ↓)

| 方法 | JBB | StrongReject | WildJailbreak | 平均 |
|------|-----|-------------|---------------|------|
| DS-8B Base | 69.0% | 63.2% | 82.4% | 71.5% |
| SafeChain | 56.1% | 55.3% | 66.7% | 59.4% |
| RealSafe | 20.7% | 34.7% | 47.1% | 34.2% |
| STAR | 8.0% | 21.9% | 37.8% | 22.6% |
| GRPO | 0.3% | 19.0% | 36.3% | 18.5% |
| **IPO (Ours)** | **5.7%** | **16.7%** | **23.4%** | **15.3%** |

### 推理能力保持

| 方法 | AIME | MATH-500 | GPQA | HumanEval | 平均 |
|------|------|----------|------|-----------|------|
| DS-8B Base | 50.7% | 91.8% | 44.9% | 79.5% | 66.7% |
| STAR | 46.0% | 89.4% | 47.0% | 77.1% | 64.9% |
| GRPO | 50.0% | 92.8% | 50.5% | 79.9% | 68.3% |
| **IPO (Ours)** | **54.0%** | **91.6%** | **49.0%** | **79.5%** | **68.5%** |

- IPO 在 DS-8B 上将 WildJailbreak 推理有害率从 82.4% 降至 23.4%（减少71.6%）
- 同时推理能力平均提高 1.8%，在 AIME 上提升 3.3%
- 在 DS-7B 和 Qwen3-8B 上同样有效

## 亮点

1. **独特视角**：首次系统性地将安全对齐从"回复安全"提升到"推理过程安全"
2. **深入的实证分析**：通过 CSR 曲线分析发现安全触发器和合规线索的关键作用，Pearson 相关系数 0.85 提供了强有力的定量证据
3. **简洁有效的方法**：IPO 不需要复杂的 RL 训练，仅通过简单的"替换 + DPO"就实现了显著的安全提升
4. **理论联系**：将 IPO 与 reward shaping 建立联系，从理论角度解释了为何 IPO 比 GRPO 更高效
5. **安全与能力的双赢**：在提升安全性的同时保持甚至增强推理能力，打破了安全-效用的对立

## 局限性 / 可改进方向

- 安全触发器池依赖 GPT-4o 检测，未来可探索更自动化的方法
- XsTest 合规率有所下降（DS-8B: 98.4% → 80.0%），存在一定的过度拒绝问题
- 仅在8B级别模型上验证，更大模型的效果待探索
- 安全评估依赖 GPT-4o 自动评估器，可能有偏差
- 干预策略较简单（仅替换首个合规线索），更精细的多步干预策略可能进一步提升效果

## 与相关工作的对比

| 方法 | 对齐目标 | 训练方式 | 推理安全 | 回复安全 | 能力保持 |
|------|---------|---------|---------|---------|---------|
| RealSafe | 回复 | SFT(蒸馏) | 中等 | 很好 | 好 |
| STAR | 回复 | SFT(蒸馏) | 较好 | 好 | 好 |
| GRPO | 推理+回复 | RL | 较好 | 好 | 很好 |
| **IPO** | **推理过程** | **DPO(干预)** | **最好** | **很好** | **很好** |

## 启发与关联

- CSR 分析方法为理解推理模型的安全行为提供了新工具，可推广到其他过程监督场景
- "替换关键步骤 + 偏好学习"的框架有潜力应用于推理质量提升（如数学推理中的关键步骤纠正）
- 对 LRM-based agent 的安全性有重要指导意义

## 评分

- 新颖性: ⭐⭐⭐⭐ — 从推理过程安全角度出发，IPO 的干预思路非常新颖
- 实验充分度: ⭐⭐⭐⭐ — 三个模型、三个安全基准、四个推理基准，覆盖面广
- 写作质量: ⭐⭐⭐⭐⭐ — 分析深入、逻辑清晰、图表精美
- 价值: ⭐⭐⭐⭐ — 推理安全是 LRM 部署的核心问题，方法实用且有效

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](rfeval_benchmarking_reasoning_faithfulness_under_counterfactual_reasoning_interv.md)
- [\[ICLR 2026\] Training Large Reasoning Models Efficiently via Progressive Thought Encoding](training_large_reasoning_models_efficiently_via_progressive_solution_complexity.md)
- [\[ICLR 2026\] When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models](when_reasoning_meets_compression_understanding_the_effects_of_pruning_and_quant.md)
- [\[ICLR 2026\] Native Reasoning Models: Training Language Models to Reason on Unverifiable Data](native_reasoning_models_training_language_models_to_reason_on_unverifiable_data.md)
- [\[ICLR 2026\] Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models](reasoning_or_retrieval_a_study_of_answer_attribution_on_large_reasoning_models.md)

</div>

<!-- RELATED:END -->
