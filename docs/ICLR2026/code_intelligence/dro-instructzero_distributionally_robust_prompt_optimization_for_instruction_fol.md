---
title: >-
  [论文解读] DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models
description: >-
  [ICLR 2026][代码智能] 将分布鲁棒优化（DRO）引入贝叶斯优化框架以实现零样本指令优化，使优化后的指令在分布偏移和对抗性评估条件下仍保持可靠性能。
tags:
  - ICLR 2026
  - 代码智能
  - 分布鲁棒优化
  - 贝叶斯优化
  - 零样本指令学习
  - 黑盒LLM
---

# DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models

**会议**: ICLR 2026  
**arXiv**: [2510.15260](https://arxiv.org/abs/2510.15260)  
**代码**: 未公开  
**领域**: 代码智能  
**关键词**: 提示优化, 分布鲁棒优化, 贝叶斯优化, 零样本指令学习, 黑盒LLM  

## 一句话总结

将分布鲁棒优化（DRO）引入贝叶斯优化框架以实现零样本指令优化，使优化后的指令在分布偏移和对抗性评估条件下仍保持可靠性能。

## 研究背景与动机

大语言模型对提示措辞高度敏感——即便是对强指令的轻微改写也会导致准确率下降，且在一个评估环境中有效的指令往往无法迁移到稍有变化的领域。现有的自动提示搜索方法（包括 InstructZero）存在如下核心问题：

1. **分布依赖**：优化期望性能时依赖固定验证分布，忽略分布偏移的可能性
2. **脆弱性**：优化后的指令容易过拟合训练分布，在对抗性条件或领域不匹配时性能急剧下降
3. **实际需求**：真实部署中输入分布不可避免地会发生变化，需要鲁棒的指令优化策略

InstructZero 的成功表明贝叶斯优化（BO）是指令优化的有效框架，但其 EI/UCB 采集函数仅优化期望评分，本质上是平均情况优化。

## 方法详解

### 整体框架

DRO-InstructZero 建立在 InstructZero 的管道之上：开源 LLM（Vicuna）生成候选指令 → 黑盒 LLM（ChatGPT）评估 → 贝叶斯优化迭代优化软提示。核心创新是将采集函数从期望情况替换为分布鲁棒目标。

### 关键设计

**从 InstructZero 的标准目标：**

$$\max_{v \in \mathcal{V}} \; \mathbb{E}_{(X,Y) \sim \mathcal{D}_t} \left[ h(f([v;X]), Y) \right]$$

**扩展到分布鲁棒目标：**

$$\max_{v \in V} \; \inf_{Q \in \mathcal{U}(D^t)} \; \mathbb{E}_{(X,Y) \sim Q} \left[ h(f([v;X]), Y) \right]$$

其中 $\mathcal{U}(D^t)$ 是以参考分布 $w_{\text{ref}}$ 为中心、以 $f$-散度（KL 散度）为度量的模糊集（ambiguity set），半径为 $\epsilon$。

**连续化转换：** 将离散指令空间的 DRO 目标转化为低维连续黑盒函数：

$$H(p) \triangleq \inf_{Q \in \mathcal{U}(D^t)} \; \mathbb{E}_{(X,Y) \sim Q} \left[ h(f([g([Ap; \text{exemplars}]); X]), Y) \right]$$

**鲁棒采集规则：** 对每个候选软提示 $p_m$，首先计算乐观上界：

$$\text{ucb}_m = \left[ \mu^t(p_m) + \beta(m) \sigma^t(p_m) \right]_t$$

然后在模糊集内求解最坏情况权重：

$$w_m^* = \arg\min_{w': \|w' - w_{\text{ref}}\|_{\mathcal{M}} \leq \epsilon(m)} \langle \text{ucb}_m, w' \rangle$$

最终选择最大化鲁棒采集值的提示：

$$p_{m+1} = \arg\max_p \langle \text{ucb}_m, w_m^* \rangle$$

**指令耦合核（DRO 扩展版）：**

$$\mathbf{K}_{ij}^t = l(p_i, p_j)^\top L^{-1} S L^{-1} l(p_j, p_i)$$

其中 $S$ 进一步被对抗性分布 $w^*$ 加权，统一考虑了语义相似性和分布鲁棒性。

### 训练策略

- 使用 CMA-ES 演化策略搜索最优软提示
- Mini-batch 版本每轮探索 25 个软提示
- 参考分布 $w_{\text{ref}}$ 通过指数移动平均逐步更新
- 探索系数 $\beta(t) = 2.0 \cdot \sqrt{2.0 \cdot \log(t+1)}$
- 模糊半径 $\epsilon = 0.1$（固定常数）
- 对抗性权重通过 cvxpy 凸优化求解器求解
- 每轮跨 2 个任务联合优化

## 实验关键数据

### 主实验

**32 个 BIG-Bench 任务的整体表现：**

| 指标 | InstructZero | DRO-InstructZero | 提升 |
|------|-------------|-----------------|------|
| 平均准确率 | 0.719 | 0.756 | +3.6 pts |
| 中位每任务增益 | — | — | +5.5 pts |
| 胜/平/负 | — | 18/8/6 | — |

**代表性任务详细结果：**

| 任务类型 | InstructZero | DRO-InstructZero | 提升 |
|---------|-------------|-----------------|------|
| 翻译 (EN-DE/ES/FR) | 0.867 | 0.980 | +11.3 pts |
| Auto-Debugging (偏移) | baseline | — | +25 pts |
| Formality Rewriting (偏移) | 61.3±0.7% | 85-90% | +25-30 pts |
| Cause-and-Effect (分布内) | ≥96% | ≥96% | 无损 |
| Unscrambling | 0.67 | 0.80 | +13 pts |
| Second Letter | 0.62 | 0.74 | +12 pts |
| Taxonomy | 0.82 | 0.92 | +10 pts |
| Sentiment | 0.93 | 0.99 | +6 pts |

**饱和任务保持 100%：** Sum、Periodic、Passivation、Num2Verbal、Letters List、First Letter、Diff

### 消融实验

| 方法 | 分布内(ID) | 偏移(Shift) | 说明 |
|------|-----------|------------|------|
| InstructZero-EI | 强 | 61.3±0.7% | 偏移下急剧退化 |
| InstructZero-UCB | 一般 | 一般 | 标准 BO 替代 |
| DRO w/o BO | 弱 | 中等 | 证明 BO 搜索必要 |
| DRO-InstructZero | 强 | 85-90% | 最优 |

关键消融发现：
- DRO 在分布偏移下比 EI/UCB 采集函数高 15-25 个绝对百分点
- "DRO w/o BO" 性能低于完整方法，证实潜空间贝叶斯搜索对效率和可扩展性至关重要
- DRO 与 BO 的结合是关键：DRO 提供鲁棒性目标，BO 提供高效搜索

### 关键发现

1. **鲁棒性增益来自原理性设计**：不是简单的正则化副产品，而是来自对平均情况采集函数的分布鲁棒替换
2. **少数任务回退**：Antonyms -11pts、Object Counting -10pts、CS-algorithm -8pts——发生在最坏情况加权强调的模式偏离评估器使用的确切词汇规则时
3. **查询效率不变**：与 InstructZero 使用相同的查询预算，无额外 API 开销

## 亮点与洞察

1. **理论优雅**：将 DRO 与 BO 的结合用于提示学习是非常自然的形式化，直觉上最坏情况优化确实是实际部署所需
2. **即插即用**：仅修改采集函数即可将任何 BO-based 提示优化方法升级为鲁棒版本
3. **分布偏移是提示优化的真实痛点**：论文准确识别了现有方法忽视的关键问题
4. **翻译任务的巨大增益**（+11.3 pts）表明鲁棒优化在跨语言场景特别有价值

## 局限性 / 可改进方向

1. **对抗性重加权增加计算复杂度**：每轮迭代尤其 cvxpy 凸优化带来额外开销
2. **固定散度度量和模糊半径**：当前使用固定 KL 散度和 $\epsilon = 0.1$，未必适用于所有分布不确定性
3. **实验受 API 成本限制**：仅使用 ChatGPT 作为黑盒 LLM，未扩展到 GPT-4 等更强模型
4. **少数词汇/分类任务的退化**需要进一步分析——混合采集函数的消融被推迟到附录
5. **未探索多模态或推理密集型场景**

## 相关工作与启发

- **InstructZero**（Chen et al., 2024）是直接基础，本文的贡献是在其上加入 DRO 层
- **DRBO**（Kirschner et al., 2020）提供了分布鲁棒贝叶斯优化的理论基础
- **APE / Auto-prompt 方向**：Zhou et al., 2022 等工作通过不同路线自动化提示设计
- 启发：DRO 思想可扩展到其他基于搜索的 LLM 优化场景——如思维链优化、RLHF 奖励建模等

## 评分

- **新颖性**: ⭐⭐⭐⭐ — DRO + BO 的组合在提示优化领域是首次，形式化优雅
- **技术深度**: ⭐⭐⭐⭐ — 理论基础扎实（信息论 + 凸优化 + GP），算法设计完善
- **实验充分度**: ⭐⭐⭐ — 32 个任务覆盖面广，但缺乏更强基线（如 GPT-4）和更多消融细节
- **实用性**: ⭐⭐⭐⭐ — 即插即用设计使其容易集成到现有管道
- **写作质量**: ⭐⭐⭐⭐ — 结构清楚，问题动机阐述到位

**总评**: ⭐⭐⭐⭐ (4/5) — 方向正确、形式化优雅的工作，将鲁棒优化理论与 LLM 提示工程有效桥接，但实验深度和模型覆盖仍有提升空间。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] ShieldedCode: Learning Robust Representations for Virtual Machine Protected Code](shieldedcode_learning_robust_representations_for_virtual_machine_protected_code.md)
- [\[ICLR 2026\] A Problem-Oriented Perspective and Anchor Verification for Code Optimization](a_problem-oriented_perspective_and_anchor_verification_for_code_optimization.md)
- [\[ICLR 2026\] Training Large Language Models To Reason In Parallel With Global Forking Tokens](training_large_language_models_to_reason_in_parallel_with_global_forking_tokens.md)
- [\[ICLR 2026\] The Limits of Long-Context Reasoning in Automated Bug Fixing](the_limits_of_long-context_reasoning_in_automated_bug_fixing.md)
- [\[ICLR 2026\] Learning to Reason without External Rewards](learning_to_reason_without_external_rewards.md)

</div>

<!-- RELATED:END -->
