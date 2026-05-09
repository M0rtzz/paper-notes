---
title: >-
  [论文解读] Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems
description: >-
  [ACL 2025][LLM Agent][奖励模型] 本文提出 Agentic Reward Modeling，将传统基于人类偏好的奖励模型与可验证正确性信号（事实性和指令遵循）相结合，通过路由器-验证代理-判断器的 Agent 架构，实现了在多个奖励模型基准和下游任务上的显著提升。
tags:
  - ACL 2025
  - LLM Agent
  - 奖励模型
  - 可验证正确性
  - Agent系统
  - 事实性验证
  - 指令遵循
---

# Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems

**会议**: ACL 2025  
**arXiv**: [2502.19328](https://arxiv.org/abs/2502.19328)  
**代码**: [https://github.com/THU-KEG/Agentic-Reward-Modeling](https://github.com/THU-KEG/Agentic-Reward-Modeling)  
**领域**: LLM Agent  
**关键词**: 奖励模型, 可验证正确性, Agent系统, 事实性验证, 指令遵循

## 一句话总结

本文提出 Agentic Reward Modeling，将传统基于人类偏好的奖励模型与可验证正确性信号（事实性和指令遵循）相结合，通过路由器-验证代理-判断器的 Agent 架构，实现了在多个奖励模型基准和下游任务上的显著提升。

## 研究背景与动机

1. **领域现状**：奖励模型（RM）是 LLM 后训练（RLHF、DPO）和推理时扩展（best-of-n search）的关键组件，主流 RM 基于人类偏好训练。
2. **现有痛点**：现有 RM 主要关注人类偏好，容易受主观偏见影响（如偏好更长、更详细的回答），忽略了可验证的正确性信号，比如事实性错误和指令约束违反。
3. **核心矛盾**：人类偏好是主观的且难以避免偏见，而正确性（事实准确性、指令遵循）是客观可验证的。现有 RM 将这两者混为一谈，导致可靠性不足。
4. **本文目标**：设计一个结合人类偏好与可验证正确性信号的奖励系统，在不同维度提供更可靠的奖励。
5. **切入角度**：受 DeepSeek-R1 等工作中规则奖励成功应用的启发，认为可验证正确性信号可以有效补充传统 RM。
6. **核心 idea**：用 Agent 架构（路由器 + 专项验证代理 + 判断器）将偏好分数与正确性信号融合，得到更可靠的综合奖励。

## 方法详解

### 整体框架

RewardAgent 由三个模块组成：(1) Router 分析指令并决定调用哪些验证代理；(2) Verification Agents 从事实性和指令遵循两个角度评估回答的正确性；(3) Judger 将验证信号与基础 RM 的偏好分数加权融合为最终奖励。

### 关键设计

1. **事实性验证代理**:

    - 功能：高效评估两个回答之间的事实正确性差异
    - 核心思路：采用成对比较策略而非逐条验证。流程包括：差异提议（识别两个回答中声明事实的关键差异）→ 查询生成（基于差异构造搜索查询）→ 证据生成（用搜索引擎或 LLM 参数知识获取支持证据）→ 验证（用证据判断哪个回答更准确，输出 0/1 分数）。
    - 设计动机：相比 FactScore 等逐条验证方法，成对比较只验证差异部分，大幅降低搜索引擎查询次数和时间成本。

2. **指令遵循验证代理**:

    - 功能：自动检查回答是否满足指令中的硬约束（如长度、格式、关键词等）
    - 核心思路：约束解析（从指令中提取硬约束）→ 代码生成与优化（生成 Python 脚本来检查约束，脚本输入回答输出 0/1）→ 验证（在 Python 解释器中执行代码）。如果代码执行出错，会将错误信息反馈给模型进行 self-refinement。最终分数是所有硬约束得分的平均值。
    - 设计动机：硬约束（如"回答不超过 100 字"）可以被代码精确验证，但传统 RM 很难捕捉这类表面形式的约束。代码执行提供了确定性的验证方式。

3. **路由器与判断器**:

    - 功能：动态选择需要调用的验证代理，并整合多维度分数
    - 核心思路：路由器用 LLM 分析指令需求，为每条指令选择合适的验证代理子集 $A_x$。判断器用加权求和整合分数：$r(x,y) = \lambda \cdot r_{RM}(x,y) + \sum_{i \in A_x} w_i \cdot a_i(x,y)$，目前所有权重设为 1.0。
    - 设计动机：不同指令需要不同维度的评估，动态选择避免了不必要的计算和累积错误。

### 损失函数 / 训练策略

RewardAgent 本身不需要训练——它是一个推理时的 Agent 系统。底层 RM 使用已训练好的 ArmoRM，验证代理使用 GPT-4o mini 或 Llama3-8B Instruct 作为 backbone。

## 实验关键数据

### 主实验

| 模型 | RM-Bench Normal | RM-Bench Hard | JudgeBench | IFBench | Overall |
|------|----------------|---------------|------------|---------|---------|
| ArmoRM | 76.7 | 34.6 | 66.2 | 59.5 | 56.5 |
| GPT-4o | 71.4 | 27.9 | 66.2 | 54.4 | 56.3 |
| DeepSeek-R1 | 83.7 | 50.1 | 74.4 | 64.0 | 69.1 |
| **RewardAgent_mini** | **86.0** | **60.2** | 69.2 | **78.0** | **72.5** |
| **RewardAgent_Llama** | 79.3 | 53.5 | 63.9 | 67.8 | 63.2 |

### 消融实验

| 配置 | RM-Bench | JudgeBench | IFBench | 说明 |
|------|----------|------------|---------|------|
| Full RewardAgent_mini | 73.1 | 68.2 | 75.5 | 完整模型 |
| − 事实性验证 | 54.0 | 52.9 | 73.6 | 事实性验证贡献最大 |
| − 指令遵循验证 | 74.7 | 66.2 | 60.4 | 对 IFBench 影响显著 |
| − 两者都去掉 | 55.4 | 58.8 | 58.8 | 退化为基础 RM |

### 关键发现

- 事实性验证代理对 RM-Bench 和 JudgeBench 的提升最为显著，说明现有 RM 在事实性判断上严重不足
- 指令遵循验证代理在 IFBench 上提升 15+ 点，尤其在 hard 子集上效果突出
- 即使使用开源 Llama3-8B 作为 backbone，RewardAgent 也超越了 GPT-4o 等更大的模型
- 使用搜索引擎作为外部知识源反而略微降低了某些基准上的表现（检索噪声问题）

## 亮点与洞察

- **Agent 架构解耦了偏好与正确性**：这是一个优雅的设计思路——不试图让单个模型同时学会偏好和正确性，而是用专项代理处理各自擅长的维度。这种模块化设计使系统易于扩展新的验证维度。
- **代码验证指令约束**是一个非常实用的 trick：硬约束的代码化验证提供了确定性保证，可以迁移到任何需要格式/约束检查的场景。
- 成对事实性验证（只验证差异）是减少成本的关键设计，在 reward scoring 的高频场景中非常实用。

## 局限与展望

- 权重 $\lambda$ 和 $w_i$ 目前固定为 1.0，自适应权重调整可能进一步提升效果
- 事实性验证依赖 LLM 生成查询和判断，本身可能引入错误
- 搜索引擎检索的噪声问题尚未解决
- 验证代理的推理成本较高，大规模应用需要效率优化

## 相关工作与启发

- **vs ArmoRM**: 纯偏好 RM，RewardAgent 在此基础上加入正确性信号，Overall 从 56.5 提升到 72.5
- **vs DeepSeek-R1 as judge**: R1 的推理能力使其成为强 baseline，但 RewardAgent 在 IFBench 上显著超越
- **vs FactScore**: 传统事实性评估需要逐条验证所有原子事实，RewardAgent 的成对差异验证更高效

## 评分

- 新颖性: ⭐⭐⭐⭐ Agent 架构整合偏好与可验证信号的思路新颖，但各组件技术不算全新
- 实验充分度: ⭐⭐⭐⭐⭐ 基准测试+best-of-n+DPO训练三层验证，消融分析全面
- 写作质量: ⭐⭐⭐⭐ 结构清晰，公式化框架优雅
- 价值: ⭐⭐⭐⭐⭐ 方向正确，代码开源，对奖励模型领域有重要启发

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] REPRO-Bench: Can Agentic AI Systems Assess the Reproducibility of Social Science Research?](repro-bench_can_agentic_ai_systems_assess_the_reproducibility_of_research_claims.md)
- [\[ACL 2025\] Browsing Like Human: A Multimodal Web Agent with Experiential Fast-and-Slow Thinking](browsing_like_human_a_multimodal_web_agent_with_experiential_fast-and-slow_think.md)
- [\[ACL 2025\] iAgent: LLM Agent as a Shield between User and Recommender Systems](iagent_llm_agent_as_a_shield_between_user_and_recommender_systems.md)
- [\[ACL 2025\] Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-AI Collaboration](dpt_agent_dual_process.md)
- [\[ACL 2025\] Agentic Knowledgeable Self-Awareness](agentic_knowledgeable_self-awareness.md)

</div>

<!-- RELATED:END -->
