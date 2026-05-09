---
title: >-
  [论文解读] Towards Better Chain-of-Thought: A Reflection on Effectiveness and Faithfulness
description: >-
  [ICML 2025][LLM推理][链式思维] 本文从有效性和忠实性两个角度系统分析影响 CoT 性能的关键因素，发现问题难度、信息增益和信息流是有效性的核心因素，并揭示 LLM 在预测答案时可从问题中直接召回 CoT 缺失的正确信息导致不忠实推理，进而提出 QUIRE 方法同时提升 CoT 的忠实性和有效性。
tags:
  - ICML 2025
  - LLM推理
  - 链式思维
  - 推理有效性
  - 推理忠实性
  - 信息增益
  - 信息流
---

# Towards Better Chain-of-Thought: A Reflection on Effectiveness and Faithfulness

**会议**: ICML 2025  
**arXiv**: [2405.18915](https://arxiv.org/abs/2405.18915)  
**代码**: [GitHub](https://github.com/BugMakerzzz/better_cot)  
**领域**: LLM推理  
**关键词**: 链式思维, 推理有效性, 推理忠实性, 信息增益, 信息流

## 一句话总结
本文从有效性和忠实性两个角度系统分析影响 CoT 性能的关键因素，发现问题难度、信息增益和信息流是有效性的核心因素，并揭示 LLM 在预测答案时可从问题中直接召回 CoT 缺失的正确信息导致不忠实推理，进而提出 QUIRE 方法同时提升 CoT 的忠实性和有效性。

## 研究背景与动机

1. **领域现状**: CoT 技术让 LLM 在数学等复杂推理任务上表现出色，甚至通过 RL 扩展（如 o1、DeepSeek-R1）超越人类。但 CoT 在某些任务上效果不佳甚至有害。

2. **现有痛点**: 已有评估工作要么只关注有效性（CoT 在哪些任务上好用），要么只关注忠实性（CoT 是否真正影响答案），但都缺乏深入的因果分析。

3. **核心矛盾**: CoT 有效性和忠实性的关系不清楚——不忠实的 CoT（错误推理但正确答案）大量存在于逻辑推理任务中。

4. **本文目标**: 识别影响 CoT 有效性的关键因素，解释不忠实 CoT 的机制，并设计方法同时提升两者。

5. **切入角度**: 使用信息论工具（信息增益、梯度归因分析）量化 question-CoT-answer 三者间的信息交互。

6. **核心 idea**: 不忠实 CoT 的根因是 LLM 在预测答案时直接从问题中召回了 CoT 遗漏的正确信息——利用这一发现，主动召回信息增强 CoT 生成可同时提升忠实性和有效性。

## 方法详解

### 整体框架
QUIRE（Question Information Recall and Enhancement）方法包含两个核心组件：AAE Recall 和 IG Vote。输入为问题和 CoT，输出为增强后的 CoT 和最终答案。

### 关键设计

1. **AAE Recall（归因效应召回）**:
    - 功能: 从问题上下文中主动召回关键信息
    - 核心思路: 先用 Self-Consistency 生成原始答案 A，计算问题中每个语句到答案的平均归因效应 $AAE(S,A)$，选取 top-k 高分语句作为额外 hint 注入提示，引导模型生成信息更完整的 CoT
    - 设计动机: 实验发现不忠实情况下 LLM 在预测答案时与问题中正确语句有强因果关联，主动利用此机制补全 CoT

2. **IG Vote（信息增益投票）**:
    - 功能: 基于 CoT 质量对多个候选答案进行加权投票
    - 核心思路: 计算每个 CoT 的信息增益 $IG(Q,C) = H(C) - H(C|Q)$，IG 越高表示 CoT 从问题获取的信息越多、自身引入的幻觉越少。用 IG 作为 Self-Consistency 投票权重
    - 设计动机: 高 IG 的 CoT 包含更少幻觉语句，更可能产生正确答案

3. **信息流分析框架**:
    - 功能: 量化 CoT 推理过程中的信息交互
    - 核心思路: 使用积分梯度归因（IGA）计算输入 token 对输出 token 的重要性，定义信息流单调性（MIF）为 AAE 随 CoT 步骤变化的 Spearman 相关系数
    - 设计动机: MIF 越高表示 CoT 越有效地向答案传递信息

### 损失函数 / 训练策略
- 本文方法为推理时方法，无需训练
- 使用 4 个开源 LLM 评估：Mistral-7B、Gemma2-9B、Llama3.1-8B、Qwen2.5-14B
- 9 个数据集覆盖数学、逻辑、常识三类推理

## 实验关键数据

### 主实验

| 数据集 | 指标 | QUIRE | SC (baseline) | 提升 |
|--------|------|-------|---------------|------|
| ProofWriter | Acc | 63.0 | 60.6 | +2.4% |
| ProntoQA | Acc | 95.0 | 93.2 | +1.8% |
| ProofWriter | FBS (忠实性) | 58.0 | 57.8 | +0.2% |
| ProntoQA | FBS (忠实性) | 89.2 | 83.6 | +5.6% |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| -AAE Recall | Acc 下降 | 缺少信息召回导致 CoT 不完整 |
| -IG Vote | FBS 下降 | 缺少质量加权导致不忠实 CoT 被采纳 |
| 完整 QUIRE | 最优 | 两组件互补 |

### 关键发现
- CoT 在难题上更有效（难度级别 4-5 提升显著，级别 1-2 甚至有害）
- 数学推理的 CoT 信息增益最低（额外信息最多），常识推理最高（额外信息最少）
- 信息流单调性（MIF）与 CoT 有效性强正相关
- 逻辑推理任务中不忠实 CoT 比例最高（ProntoQA 达 17/50）
- AAE Recall和IG Vote两组件互补：移除任一都会导致性能下降
- 在Mistral-7B、Gemma2-9B、Llama3.1-8B、Qwen2.5-14B四个模型上均验证有效，展示了跨模型的通用性

## 亮点与洞察
- 首次从信息论角度系统解释了 CoT 有效性和忠实性的关联
- 揭示了 LLM 的"信息召回"机制：即使 CoT 推理错误，模型仍能从原始问题中提取正确信息
- QUIRE 方法巧妙地将"问题"变为"特征"：主动利用信息召回增强 CoT 生成
- 提出的 MIF 和 FBS 指标为 CoT 质量评估提供了新工具- 实验证明提升CoT忠实性可以直接带来有效性的提升，两者之间存在正相关关系

## 局限与展望
- 分析仅限于开源白盒 LLM，无法获取 GPT-4 等黑盒模型的梯度信息
- 忠实性提升导致有效性提升的结论缺乏理论证明
- AAE Recall 引入的噪声 hint 可能在某些场景下降低性能
- 未探索在 reasoning model（如 o1）上的表现
- 信息增益的计算依赖于模型内部状态，不同模型架构之间的可比性有限
- QUIRE的两次LLM调用增加了推理成本，在实时应用中可能不实用
- 归因分析（IGA）的计算开销较大，限制了方法在大规模场景下的应用

## 相关工作与启发
- **vs Self-Consistency**: QUIRE 在 SC 基础上增加了信息召回和质量加权
- **vs Self-Refine**: QUIRE 不依赖模型自我反思，而是利用信息论工具指导改进
- **vs CoT 忠实性评估**: 此前工作只检测不忠实，本文进一步解释原因并提出缓解方案
- 信息增益作为CoT质量的新度量具有广泛的应用潜力，可用于CoT重排序、筛选等场景
- 对于多轮CoT迭代的场景，信息召回机制可能被用于指导每一轮的CoT生成
- 未来可探索将QUIRE与思维链蒸馏结合，提升小模型的CoT质量
- 在多步推理任务中逐步应用信息召回可能带来累积收益

## 评分
- 新颖性: ⭐⭐⭐⭐ 信息论视角分析 CoT 是新颖的研究方向
- 实验充分度: ⭐⭐⭐⭐ 9 个数据集 4 个模型的广泛评估
- 写作质量: ⭐⭐⭐⭐⭐ 结构清晰，从分析到方法的逻辑链完整
- 价值: ⭐⭐⭐⭐ 对理解和改进 CoT 推理有重要启发

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation](pcot_persuasion_disinfo.md)
- [\[ICML 2025\] Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](rethinking_external_slow-thinking_from_snowball_errors_to_probability_of_correct.md)
- [\[ICML 2025\] Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](improving_rationality_in_the_reasoning_process_of_language_models_through_self-p.md)
- [\[ICML 2025\] AdaDecode: Accelerating LLM Decoding with Adaptive Layer Parallelism](adadecode_accelerating_llm_decoding_with_adaptive_layer_parallelism.md)
- [\[ICML 2025\] Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](soft_reasoning_navigating_solution_spaces_in_large_language_models_through_contr.md)

</div>

<!-- RELATED:END -->
