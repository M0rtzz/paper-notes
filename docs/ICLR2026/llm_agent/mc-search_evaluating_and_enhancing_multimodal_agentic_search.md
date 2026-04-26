---
title: >-
  [论文解读] MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains
description: >-
  [ICLR 2026][LLM Agent][多模态RAG] 提出 MC-Search，首个面向代理式多模态 RAG 的基准，包含 3,333 个高质量样本、5 种推理拓扑结构和步级标注的推理链，同时引入过程级评估指标和 Search-Align 对齐框架显著提升开源 MLLM 的搜索规划能力。
tags:
  - ICLR 2026
  - LLM Agent
  - 多模态RAG
  - 代理式搜索
  - 长推理链
  - 过程级评估
  - 搜索对齐
---

# MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains

**会议**: ICLR 2026  
**arXiv**: [2603.00873](https://arxiv.org/abs/2603.00873)  
**代码**: [mc-search-project.github.io](https://mc-search-project.github.io)  
**领域**: LLM Agent  
**关键词**: 多模态RAG, 代理式搜索, 长推理链, 过程级评估, 搜索对齐  

## 一句话总结

提出 MC-Search，首个面向代理式多模态 RAG 的基准，包含 3,333 个高质量样本、5 种推理拓扑结构和步级标注的推理链，同时引入过程级评估指标和 Search-Align 对齐框架显著提升开源 MLLM 的搜索规划能力。

## 研究背景与动机

多模态大语言模型（MLLM）正从固定的"检索后生成"范式向更复杂的**代理式多模态 RAG（Agentic MM-RAG）**演进。然而，现有基准存在三大关键局限：

1. **浅层检索**：大多数基准（OK-VQA、InfoSeek、MMSearch 等）只涉及 1-2 跳检索，无法评估自适应多步搜索行为
2. **缺乏步级标注**：没有逐步标注的子问题、检索模态、支持事实和中间答案，无法进行过程级分析
3. **无推理拓扑**：未明确区分不同模态在推理过程中的角色（如图文串行 vs 并行）

| 基准 | 知识类型 | 典型跳数 | 长链(≥4跳) | 步级标注 | 推理拓扑 |
|------|:-:|:-:|:-:|:-:|:-:|
| OK-VQA | 文本 | 1 | ✗ | ✗ | ✗ |
| WebQA | 文本/图像 | ≤2 | ✗ | ✗ | ✗ |
| MMSearch | 文本/图像 | 1 | ✗ | ✗ | ✗ |
| **MC-Search** | **文本/图像** | **≥4** | **✓** | **✓** | **✓** |

## 方法详解

### 整体框架

MC-Search 包含三个核心贡献：

1. **基准构建**：5 种推理拓扑 + HAVE 过滤 + 3,333 个高质量样本
2. **评估协议**：统一代理式 MM-RAG 管线 + 过程级评估指标
3. **Search-Align**：基于验证推理链的过程级监督微调

### 关键设计

**五种搜索增强推理拓扑**：

每个推理图 $\mathcal{G}(Q, A) = \{(q_t, m_t, r_t, a_t)\}_{t=1}^T$ 包含子问题、检索模态、证据和中间答案：

1. **图像发起链（Image-Initiated Chain）**：从图像检索开始，后续基于文本检索（1,306 样本）
2. **文本发起链（Text-Initiated Chain）**：从文本检索开始，后续引入图像验证（169 样本）
3. **并行图文分叉（Parallel Image-Text Fork）**：图像和文本检索并发进行，无特定跳间依赖（680 样本）
4. **多图分叉（Multi-Images Fork）**：需检索多张图像进行视觉对比后转向文本证据（233 样本）
5. **纯文本链（Text-Only Chain）**：仅通过文本推理，作为基线（945 样本）

**HAVE 过滤机制（Hop-wise Attribution and Verification of Evidence）**：

解决 MLLM 生成长推理链时的幻觉步骤和冗余步骤问题。

上下文效用（Context Utility）——移除证据 $r_t$ 后答案准确度的下降：

$$\text{Util}(t) = \text{F1}(\mathcal{C}) - \text{F1}(\mathcal{C} \setminus r_t)$$

导航角色（Navigational Role）——步骤是否连接下游子问题：

$$\text{Nav}(t) = \begin{cases} 1, & \text{if } \text{Ent}(a_t) \cap \text{Ent}(q_{t+1:T}) \neq \emptyset \\ 0, & \text{otherwise} \end{cases}$$

当 $\text{Util}(t) < \text{threshold}$ 且 $\text{Nav}(t) = 0$ 时，该步骤被标记为冗余。三阶段过滤：Qwen2.5-VL-7B 初筛 → Gemini-2.5-Pro 跳缩减和验证 → Gemini-2.5-Flash 冗余检查，从 21k 初始样本过滤至 3,333 个高质量样本。

**过程级评估指标**：

除标准 F1 和 LLM-as-a-Judge 外，引入两个链对齐指标：

1. **Hit per Step (HPS)**——预测图中匹配黄金步骤证据的比例：

$$\text{HPS}(\hat{\mathcal{G}}, \mathcal{G}) = \frac{1}{|\mathcal{G}|} |\{(t,t') \mid r_t \in \mathcal{G}, \hat{r}_{t'} \in \hat{\mathcal{G}}, \hat{r}_{t'} = r_t\}|$$

2. **Rollout Deviation (RD)**——预测和黄金推理图的步长差：

$$\text{RD}(\hat{\mathcal{G}}, \mathcal{G}) = ||\hat{\mathcal{G}}| - |\mathcal{G}||$$

**统一代理式 MM-RAG 管线**：

迭代过程包含三个模块：

1. **子查询和动作生成**：MLLM 预测下一个子目标，选择三种检索动作之一（文本查询的文本搜索、文本查询的图像搜索、图像查询的图像搜索）
2. **证据获取**：多模态编码器进行密集检索，返回 top-1 结果
3. **迭代推理与合成**：子答案和证据反馈到模型指导下一步规划，直到证据充分后输出最终答案

### Search-Align：过程级对齐

与传统 SFT 仅监督最终答案不同，Search-Align 提供**过程级监督**：

1. **训练数据构建**：用 Gemini-2.5-Flash 为每条推理链添加解释性推理思维，将步级标注转换为连贯对话轨迹
2. **监督微调**：在对话式轨迹上微调 MLLM，学习规划、选择检索模态和跨步整合证据

## 实验关键数据

### 主实验：六个 MLLM 在 MC-Search 上的评估

| 推理拓扑 | 模型 | F1↑ | ΔF1↑ | HPS↑ | RD↓ |
|------|------|:-:|:-:|:-:|:-:|
| Image-Initiated | Gemini-2.5-Pro | **47.61** | **42.76** | 25.90 | **1.05** |
| | Qwen2.5-VL-7B | 26.30 | 8.65 | 16.51 | 4.04 |
| | +Search-Align | **45.70** | **28.05** | **33.59** | **0.70** |
| Multi-Images Fork | Gemini-2.5-Pro | **40.37** | **36.58** | 18.68 | **1.40** |
| | Qwen2.5-VL-7B | 26.13 | 7.53 | 12.58 | 3.80 |
| | +Search-Align | **38.01** | **19.41** | **38.01** | **1.16** |
| Text-Only Chain | Gemini-2.5-Pro | 34.47 | 34.46 | 21.59 | 1.07 |
| | Qwen2.5-VL-7B | 23.54 | 14.89 | 13.35 | 4.63 |
| | +Search-Align | **37.54** | **28.89** | **19.04** | **0.98** |

### Search-Align 提升效果

| 模型 | 平均 F1 提升 | 平均 HPS 提升 | 平均 RD 降低 |
|------|:-:|:-:|:-:|
| InternVL3.5-8B + Search-Align | +2.8 | +12.0 | -0.6 |
| **Qwen2.5-VL-7B + Search-Align** | **+13.7** | **+16.0** | **-3.1** |

Search-Align 后的 Qwen2.5-VL-7B 在文本类链上接近 Gemini-2.5-Pro 的性能，说明开源模型的弱点在于检索规划而非基础感知。

### 消融实验与关键发现

**链长度 vs 性能（RQ2）**：1-3 跳时性能差异温和，4-5 跳时所有模型急剧下降，Gemini-2.5-Pro 最鲁棒。

**过度/不足检索分析（RQ3）**：
- 严重不足检索（ΔStep < -2）：性能骤降
- 适度过度检索（ΔStep = 1-2）：反而提升准确率——额外 1-2 轮搜索可弥补不完美规划
- 过度检索过量（ΔStep ≥ 4）：噪声导致所有模型性能下降

**模态覆盖度分析（RQ4）**：
- Gemini-2.5-Pro 在有图像输入时图像覆盖率 87.35%，无图像输入时骤降至 29.50%
- InternVL3.5-8B 从 63.84% 降至 0.66%
- 暴露了严重的**模态差距**：模型默认倾向文本检索

**拓扑难度排序**：并行图文分叉 > 多图分叉 > 图像发起链 > 文本发起链 ≈ 纯文本链

## 亮点与洞察

- **推理拓扑设计新颖**：五种结构化拓扑首次系统化了多模态搜索推理的空间，为后续研究提供了分析框架
- **HAVE 过滤确保数据质量**：三阶段、多模型交叉验证的严格过滤，最终质量评分 4.87/5.0
- **过程级指标填补评估空白**：HPS 和 RD 超越最终答案准确率，精确归因检索和规划的质量
- **Search-Align 的实际价值**：仅用 SFT 就能让 Qwen2.5-VL-7B 在多项指标上逼近 Gemini-2.5-Pro
- **揭示关键缺陷**：模态差距和过度/不足检索问题为社区指明了改进方向

## 局限性 / 可改进方向

1. 每步仅检索 top-1 结果，限制了证据覆盖度，更灵活的检索策略可能更好
2. 知识库基于 Wikipedia 构建，可能缺乏实时性和专业领域覆盖
3. Search-Align 仅使用 SFT，结合强化学习（如过程奖励模型）可能进一步提升
4. 推理拓扑是预定义的五种，真实场景可能有更复杂的混合结构
5. HAVE 过滤依赖 LLM 评估，可能引入模型偏见

## 相关工作与启发

- **与 LiveNewsBench 的互补**：LiveNewsBench 评估文本搜索能力，MC-Search 评估多模态搜索能力，覆盖不同维度
- **与 MRAG/M2RAG 的升级**：从 1-2 跳扩展到 4+ 跳，从结果评估扩展到过程评估
- **对过程奖励模型（PRM）的启发**：步级标注的推理链可直接用于训练 PRM，推动搜索推理的强化学习
- **对多模态 Agent 设计的启发**：模态差距问题表明需要更好的多模态规划机制，而非简单依赖模型对查询模态的感知

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ — 首个代理式 MM-RAG 长链推理基准，五种拓扑+过程级指标开创性
- **技术深度**: ⭐⭐⭐⭐ — HAVE 过滤、Search-Align 框架设计合理
- **实验充分度**: ⭐⭐⭐⭐⭐ — 6 个模型、5 种拓扑、5 个研究问题、多维度分析
- **写作质量**: ⭐⭐⭐⭐⭐ — 逻辑紧凑，问题→基准→评估→改进完整闭环
- **实用性**: ⭐⭐⭐⭐⭐ — 基准+管线+训练数据三位一体，社区可直接使用
- **综合评分**: ⭐⭐⭐⭐⭐ (9/10)

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News](livenewsbench_evaluating_llm_web_search_capabilities_with_freshly_curated_news.md)
- [\[ICLR 2026\] ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning](tooltree_efficient_llm_agent_tool_planning_via_dual-feedback_monte_carlo_tree_se.md)
- [\[ICLR 2026\] ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](st-webagentbench_a_benchmark_for_evaluating_safety_and_trustworthiness_in_web_ag.md)
- [\[ICLR 2026\] Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents](harnessing_uncertainty_entropy-modulated_policy_gradients_for_long-horizon_llm_a.md)
- [\[ICLR 2026\] Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents](solving_the_granularity_mismatch_hierarchical_preference_learning_for_long-horiz.md)

<!-- RELATED:END -->
