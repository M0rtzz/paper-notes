---
title: >-
  [论文解读] Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner
description: >-
  [ICML 2025][多模态][Theory-of-Mind] 提出可扩展的贝叶斯 ToM 规划器，通过将多步多模态心智推理分解为逐步贝叶斯更新来规避推理边界，并用弱到强控制机制将小模型（4B–8B）后训练获得的 ToM 似然估计能力迁移到大模型（70B–405B）的推理中，在 MMToM-QA 基准上达 81.3% 准确率，超越此前最优 BIPALM 4.6 个百分点。
tags:
  - ICML 2025
  - 多模态
  - Theory-of-Mind
  - Bayesian inverse planning
  - weak-to-strong control
  - LLM scaling
---

# Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner

**会议**: ICML 2025  
**arXiv**: [2506.01301](https://arxiv.org/abs/2506.01301)  
**代码**: 无  
**领域**: 多模态VLM  
**关键词**: Theory-of-Mind, Bayesian inverse planning, weak-to-strong control, multimodal reasoning, LLM scaling

## 一句话总结

提出可扩展的贝叶斯 ToM 规划器，通过将多步多模态心智推理分解为逐步贝叶斯更新来规避推理边界，并用弱到强控制机制将小模型（4B–8B）后训练获得的 ToM 似然估计能力迁移到大模型（70B–405B）的推理中，在 MMToM-QA 基准上达 81.3% 准确率，超越此前最优 BIPALM 4.6 个百分点。

## 研究背景与动机

**领域现状**：心智理论（Theory-of-Mind, ToM）是 AI 社会认知的基础能力，要求模型从观察到的行为推断他人的信念、意图和目标。现有 ToM 计算方法分两类：(1) 基于结构化工作流和 ToM 先验的规划方法（如贝叶斯逆规划 BIP）；(2) 将 ToM 先验整合到语言模型中通过微调实现。评测通常使用 MMToM-QA 基准，包含 VirtualHome 模拟器生成的 134 个视频和 600 个关于信念/目标推断的问题。

**现有痛点**：关键实验发现（Figure 1）揭示了严重的扩展性瓶颈——随着规划步数增加，小模型（Llama3.1-8B/70B）和推理时缩放方法（o1-mini、CoT）的准确率都急剧退化，只有 405B 级别的大模型才能维持性能。根源有二：(1) **推理边界**：CoT 等方法的有效推理步数存在上限，超过后收益递减甚至有害；(2) **知识依赖**：ToM 推理需要广泛的社会和世界知识来理解环境动态，这与模型规模强相关。

**核心矛盾**：小模型知识不足但可以廉价后训练，大模型知识丰富但后训练成本极高。单纯微调小模型或单纯用大模型推理都不够——需要将小模型的专业化能力与大模型的世界知识结合起来。

**本文要解决什么？** (1) 如何在规划步数增加时维持 ToM 推理准确率？(2) 如何利用大模型的世界知识而不需要对其进行昂贵的后训练？

**切入角度**：作者将解决方案分解为两部分：用贝叶斯逆规划（BIP）将复杂的多步推理分解为可管理的单步贝叶斯更新，避免长链推理的累积误差；用弱到强控制（weak-to-strong control）让小模型学习 ToM 专业化的似然估计，然后在推理时通过概率比值将学到的 ToM 行为迁移到大模型。

**核心idea一句话**：用逐步贝叶斯更新分解多步 ToM 推理的复杂度，同时通过弱到强控制将小模型后训练获得的 ToM 专业能力零成本迁移到 405B 级大模型的推理中。

## 方法详解

### 整体框架

系统基于 POMDP 形式化将 ToM 推理建模为贝叶斯逆规划。多模态输入（视频+文本描述）被转化为统一的符号表示（状态序列 $s^{1:t}$ 和动作序列 $a^{1:t-1}$）。给定观察到的行为，系统通过贝叶斯后验推断代理的目标 $g$ 和信念 $b^t$：$P(g, b^t | s^{1:t}, a^{1:t-1}) \propto \prod_{\tau=1}^t \pi(a^\tau | g, b^\tau) P(b^\tau | b^{\tau-1}, s^\tau) P(b^0) P(g)$。策略函数 $\pi(a^\tau | g, b^\tau)$ 由大 LM 估计，通过弱到强控制增强。

### 关键设计

1. **逐步贝叶斯逆规划（Stepwise BIP）**:

    - 功能：将多步 ToM 推理分解为模块化的单步贝叶斯更新，避免长链推理的复杂度爆炸
    - 核心思路：在每个时间步 $\tau$，独立完成三个计算：(1) 状态转移估计 $\mathcal{T}(s^\tau | s, a)$；(2) 信念分布更新 $P(b^\tau | b^{\tau-1}, s^\tau)$——如果观察到物体在容器中则更新信念包含该容器，否则从信念中移除未观察到的位置；(3) 动作似然计算 $\pi(a^\tau | g, b^\tau)$。假设比较通过累积对数似然比实现：$\log \frac{P(g_1, b_1^t)}{P(g_2, b_2^t)} = \sum_{\tau=1}^{t-1} \log \frac{\pi(a^\tau | g_1, \hat{b}^\tau)}{\pi(a^\tau | g_2, \hat{b}^\tau)} + \text{当前步比较}$
    - 设计动机：端到端的长链推理（如 CoT）在步数增加时存在推理边界，累积误差导致性能退化。BIP 的模块化分解使每步独立可控

2. **弱到强控制（Weak-to-Strong Control）**:

    - 功能：将小模型后训练获得的 ToM 专业能力零成本迁移到大模型的推理中
    - 核心思路：分两阶段后训练小模型（Llama3.1-8B）：(1) 指令微调阶段：在 VirtualHome 生成的 1000 个视频经验池上，用 LoRA（rank=16, alpha=32）最大化动作似然 $\mathcal{L}_{\text{IT}} = -\sum_i \log \pi^{\mathcal{E}_0}(a_i | s_i, b_i, g_i)$；(2) 偏好优化阶段：用 DPO 变体区分有效动作 $a^+$（简洁成功）和无效动作 $a^-$（冗长失败）。推理时，大模型（405B）的策略通过概率比值调整：$\bar{\pi}(a^t) = \frac{1}{\bar{Z}} \pi^{\mathcal{L}}(a^t) \frac{\pi^{\mathcal{E}}(a^t)}{\pi^{\mathcal{N}}(a^t)}$，其中 $\pi^{\mathcal{E}}$ 是后训练小模型，$\pi^{\mathcal{N}}$ 是原始小模型，$\pi^{\mathcal{L}}$ 是大模型。后训练效果通过比值 $\pi^{\mathcal{E}} / \pi^{\mathcal{N}}$ 表示，乘到大模型输出上实现行为迁移
    - 设计动机：405B 模型后训练成本极高且可能破坏通用能力。弱到强控制仅需后训练 8B 小模型，运行时通过概率比值将 ToM 行为"注入"大模型，等价于在 logit 空间做方向校正

3. **理论保证（KL 散度分析）**:

    - 功能：形式化证明弱到强控制的有效性
    - 核心思路：Theorem 1 证明重定向后的大模型策略 $\bar{\pi}$ 与理想 ToM 策略之间的 KL 散度有界，且界随大模型规模增大和后训练质量提升而变紧。核心是行为控制依赖于学到的 $\Delta s$（logit 偏移）来近似大模型的缩放梯度，大模型用其内在能力适配 ToM 场景
    - 设计动机：提供了不只是经验有效、理论上也有保证的方法基础

### 损失函数

小模型后训练包含两阶段损失：指令微调损失 $\mathcal{L}_{\text{IT}} = -\sum_i \log \pi^{\mathcal{E}_0}(a_i | s_i, b_i, g_i)$ 和偏好优化损失 $\mathcal{L}_{\text{PO}} = -\mathbb{E}[\log \sigma(\beta \cdot \Delta \log \pi^{\mathcal{E}})] + \lambda \cdot \text{KL}(\pi^{\mathcal{E}_0} \| \pi^{\mathcal{E}})$，其中 $\beta$ 控制偏好学习的锐度，$\lambda$ 正则化偏离初始策略的幅度。

## 实验关键数据

### 主实验表格：MMToM-QA 多模态输入下的模型对比

| 方法 | 信念推断 avg | 目标推断 avg | 总体准确率 |
|------|-----------|-----------|----------|
| Video-Llama2-13B | 42.0 | 38.3 | 40.2 |
| GPT-4V | 55.3 | 34.7 | 44.0 |
| BIPALM w/ GPT-J-6B | 81.7 | 69.0 | 75.3 |
| BIPALM w/ Llama2-7B | 80.3 | 73.3 | 76.7 |
| **本文 w/ Llama3.1-405B** | **87.1** | **76.9** | **81.3** |
| 人类 | 97.5 | 88.5 | 93.0 |

本文方法在信念推断（87.1% vs 81.7%）和目标推断（76.9% vs 73.3%）上均超越 BIPALM，总体提升 4.6 个百分点。

### 消融实验表格：大模型规模的影响（弱到强控制中的强组件）

| 大模型 (强) | 小模型 (弱) | 总体准确率 |
|-----------|-----------|----------|
| Llama3.1-8B | 8B post-trained | 76.3 |
| Llama3.1-70B | 8B post-trained | 78.4 |
| Llama3.1-405B | 8B post-trained | **81.3** |
| Llama3.1-405B (无弱控制) | - | 72.9 |

405B 模型无弱控制时仅 72.9%，加入 8B 后训练的弱到强控制后跃升至 81.3%（+8.4 pt），证明弱到强控制的有效性。模型规模越大收益越明显。

### 关键发现

- 贝叶斯分解使每步推理可靠，避免了 CoT/o1 式长链推理在步数增加时的急剧退化
- 弱到强控制成功将 8B 模型的 ToM 专业化迁移到 405B，无需对大模型后训练
- DeepSeek-R1-671B（61.5%）和 o3-mini（55.6%）的纯推理缩放方法均远低于本文的 81.3%，证明结构化框架不可替代
- 在文本-only 设置下本文方法（82.7%）也超越 BIPALM（81.7%），证明 BIP + 弱到强控制的通用性

## 亮点与洞察

- Figure 1 的扩展性分析极具说服力：清晰展示了推理边界现象和模型规模的重要性
- BIP 的模块化分解思路优雅——将"理解他人心理状态"分解为"在每步更新信念"
- 弱到强控制是训练与推理效率的巧妙平衡：后训练 8B 很便宜，推理时注入 405B 就能获得两者之长
- 理论保证（KL 散度有界）使方法不只是经验有效

## 局限性

- 依赖 405B 模型推理，部署成本极高（需同时运行 8B + 405B）
- 仅在 VirtualHome 模拟器环境验证，真实社交场景中的泛化性未知
- POMDP 形式化在某些 ToM 场景中可能过于简化（如涉及情感、欺骗等）
- 贝叶斯更新的模块化粒度需要领域专家设计，自动化程度有限

## 相关工作与启发

- **vs BIPALM (Jin et al., 2024)**：同基于 BIP 框架，但 BIPALM 仅用 6B/7B 小模型，本文通过弱到强控制将规模扩展到 405B
- **vs CoT/o1 推理缩放**：这些方法在简单任务上有效，但在多步 ToM 推理中存在推理边界，本文的结构化 BIP 分解从根本上规避了这一问题
- **启发**：弱到强控制可推广到其他需要专业化知识+广泛世界知识的任务（如医学诊断推理、法律推理等）

## 评分

⭐⭐⭐⭐ BIP + 弱到强控制的组合有创新性，扩展性分析深入，理论与实验结合紧密。但依赖 405B 模型限制了实际应用，且仅在模拟环境验证。

<!-- RELATED:START -->

## 相关论文

- [\[ICML 2025\] M3-JEPA: Multimodal Alignment via Multi-gate MoE based on JEPA](m3-jepa_multimodal_alignment_via_multi-gate_moe_based_on_the_joint-embedding_pre.md)
- [\[ICML 2025\] From Black Boxes to Transparent Minds: Evaluating and Enhancing the Theory of Mind in Multimodal Large Language Models](from_black_boxes_to_transparent_minds_evaluating_and_enhancing_the_theory_of_min.md)
- [\[ICML 2025\] Reasoning Limitations of Multimodal Large Language Models. A Case Study of Bongard Problems](reasoning_limitations_of_multimodal_large_language_models_a_case_study_of_bongar.md)
- [\[ICML 2025\] Universal Retrieval for Multimodal Trajectory Modeling](universal_retrieval_for_multimodal_trajectory_modeling.md)
- [\[ICML 2025\] Core Knowledge Deficits in Multi-Modal Language Models](core_knowledge_deficits_in_multi-modal_language_models.md)

<!-- RELATED:END -->
