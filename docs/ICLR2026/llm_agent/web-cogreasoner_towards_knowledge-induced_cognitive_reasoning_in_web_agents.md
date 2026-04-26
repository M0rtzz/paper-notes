---
title: >-
  [论文解读] Web-CogReasoner: Towards Knowledge-Induced Cognitive Reasoning in Web Agents
description: >-
  [ICLR2026][LLM Agent][Web Agent] Web-CogReasoner 借鉴 Bloom 教育分类法，将 Web Agent 的能力分解为事实知识、概念知识和程序性知识三层体系，构建结构化的知识驱动 CoT 推理框架，在 Web 导航任务上显著超越现有方法。
tags:
  - ICLR2026
  - LLM Agent
  - Web Agent
  - 认知推理
  - Bloom分类法
  - 知识驱动CoT
  - 课程学习
---

# Web-CogReasoner: Towards Knowledge-Induced Cognitive Reasoning in Web Agents

**会议**: ICLR2026  
**arXiv**: [2508.01858](https://arxiv.org/abs/2508.01858)  
**代码**: [github.com/Gnonymous/Web-CogReasoner](https://github.com/Gnonymous/Web-CogReasoner)  
**领域**: llm_agent  
**关键词**: Web Agent, 认知推理, Bloom分类法, 知识驱动CoT, 课程学习

## 一句话总结
Web-CogReasoner 借鉴 Bloom 教育分类法，将 Web Agent 的能力分解为事实知识、概念知识和程序性知识三层体系，构建结构化的知识驱动 CoT 推理框架，在 Web 导航任务上显著超越现有方法。

## 背景与动机
- 多模态大模型推动了 Web Agent 发展，但通用领域预训练知识在专业任务中仍存在性能瓶颈
- 现有知识增强方法缺乏系统性或理论基础
- 本文从教育学核心理论 Bloom 分类法出发，将学习分为两个阶段：
    - **Phase 1（知识内容学习）**：积累事实知识和概念知识 → 解决"学什么"
    - **Phase 2（认知过程）**：发展程序性知识 → 解决"怎么做"
- 这映射了人类学习轨迹：先通过教育积累知识，再基于知识和经验学会应用、创新和创造
- 核心问题：如何系统性地为 Web Agent 注入分层知识，使其具备认知推理能力？

## 方法详解

### 1. Web-CogKnowledge Framework（知识框架）
基于 Bloom 分类法的三层知识体系：

**事实知识（Factual Knowledge）**：
- 从网页内容中提取的具体信息
- 如识别网页元素属性、预测单次交互的直接结果

**概念知识（Conceptual Knowledge）**：
- 网页内容和结构的语义关系与抽象模式
- 如推断界面组件功能、理解网页整体目的和结构

**程序性知识（Procedural Knowledge）**：
- 通过交互完成特定任务的可操作知识
- 如执行目标导向的动作序列、推断用户意图、处理意外中断

### 2. Web-CogDataset（训练数据集）
- 从 14 个主流真实网站爬取多模态元数据
- 设计 12 种细粒度、渐进挑战的任务：
    - 事实层：元素属性识别、下一页预测、来源元素预测
    - 概念层：元素理解、网页理解
    - 程序层：用户意图预测、弹窗关闭、单步探索等
- 数据从感知→理解→行动逐步深入

### 3. Web-CogBench（评估基准）
- 876 个测试实例，跨 8 种任务
- 三个认知维度评估：
    - **记忆（Memorizing）**：评估回忆具体信息的能力（对应事实知识）
    - **理解（Understanding）**：评估语义解释能力（对应概念知识）
    - **探索（Exploring）**：评估规划和执行目标导向动作的能力（对应程序性知识）
- 使用 ROUGE-L、Accuracy、LVM Judge 等多种评估指标

### 4. Web-CogReasoner 推理框架
建模为 POMDP：$P = (S, A, O, K, T, R)$

**知识驱动 CoT 推理过程**：
$$\textbf{Task Prompt} \rightarrow \textbf{Knowledge-driven CoT} \rightarrow \textbf{Plan} \rightarrow \textbf{Action}$$

推理分三层：
1. **事实推理**："页面上有什么？" → 识别页面元素和状态
2. **概念推理**："这意味什么？" → 推断角色和交互关系
3. **程序推理**："如何完成任务？" → 规划目标导向的步骤

基础模型为 Qwen2.5-VL-7B，在 Web-CogDataset 上进行监督微调。

## 实验关键数据

### Web-CogBench 综合评估

| 模型 | Elem Attr | Next Page | Source Elem | Elem Und | WebPage Und | User Intent | Popup | Step Exp | Overall |
|------|-----------|-----------|-------------|----------|-------------|-------------|-------|----------|---------|
| Claude Sonnet 4 | 79.7 | 93.5 | 62.5 | 62.8 | 54.3 | 64.7 | 100 | 96.8 | 76.8 |
| Gemini 2.5 Pro | 79.8 | 94.6 | 84.4 | 62.6 | 73.5 | 51.9 | 96.6 | 98.4 | 80.4 |
| UI-TARs-7B-SFT | 63.5 | 88.0 | 31.3 | 48.0 | 48.0 | 32.4 | 25.9 | 33.9 | 46.4 |
| **Web-CogReasoner** | **91.4** | 93.5 | **87.5** | **69.2** | **79.0** | 61.4 | 98.3 | 95.2 | **84.4** |

### VisualWebBench

| 模型 | Perception Avg | Reasoning Avg | Overall Avg |
|------|----------------|---------------|-------------|
| Claude Sonnet 4 | 80.7 | 91.2 | 85.9 |
| UI-TARs-7B-SFT | 82.4 | 89.7 | 86.0 |
| **Web-CogReasoner** | 79.0 | **93.6** | **86.3** |

### 课程学习消融实验

| 配置 | Memorizing | Understanding | Exploring | Overall |
|------|------------|---------------|-----------|---------|
| Qwen2.5-VL-7B (Base) | 67.6 | 61.0 | 77.9 | 69.8 |
| + Factual (S1) | 85.5 (+17.9) | 64.2 | 60.1 | 72.1 |
| + Conceptual (S2) | 88.1 | 75.5 (+11.3) | 65.8 | 78.3 |
| + Procedural (S3) | 90.8 | 74.1 | 85.0 (+19.2) | **84.4** |

### 在线 Web 任务 - WebVoyager 成功率

| Agent | Overall |
|-------|---------|
| Claude Sonnet 4 | 47.7% |
| Gemini 2.5 Pro | 54.9% |
| OpenWebVoyager_Max | 26.2% |
| **Web-CogReasoner** | **30.2%** |

开源模型中最佳，平均步数也最少（4.73 步/成功任务）。

## 亮点
1. **理论基础扎实**：从教育学 Bloom 分类法出发，将 Agent 能力分解为可训练的知识层次，有良好的理论指导
2. **结构化知识驱动 CoT**：不是简单的 prompt engineering，而是将知识体系嵌入推理过程
3. **课程学习效果显著**：消融实验清晰展示每层知识的贡献，整体提升 14.6%
4. **全面的评估体系**：Web-CogBench 从记忆/理解/探索三个认知维度系统评估
5. **超越闭源模型**：7B 模型在 Web-CogBench 上超越 Claude Sonnet 4 和 Gemini 2.5 Pro
6. **高效执行**：在线任务中平均步数最少，说明知识驱动推理减少了冗余探索

## 局限性 / 可改进方向
- 在线任务（Mind2Web cross-web）上表现不如 Claude/Gemini，泛化到完全未见网站仍有挑战
- 14 个训练网站的覆盖面可能不够广，难以涵盖所有网页类型
- POMDP 建模中未引入显式记忆机制，长序列决策可能受限
- 未探索与 RL 结合的训练方式（当前仅用 SFT）
- 知识层次的划分可能过于刚性，实际任务中三种知识往往交织

## 与相关工作的对比
- 相比 UI-TARs（视觉感知强但认知推理弱）：Web-CogReasoner 在认知任务上大幅领先（84.4% vs 46.4%），说明纯视觉感知不够
- 相比 OpenWebVoyager（需要在目标网站重新训练）：Web-CogReasoner 仅靠结构化知识即可泛化
- 相比通用 LVM（Claude/Gemini）：开源 7B 模型在知识密集型任务上具有竞争力
- 相比 AutoWebGLM 等早期课程学习方法：Web-CogReasoner 的知识体系更系统化

## 启发与关联
- Bloom 分类法可推广到其他 Agent 领域（如 GUI Agent、机器人操作）
- 知识驱动 CoT 的思路可用于其他需要结构化推理的任务
- 事实→概念→程序的渐进训练策略对多阶段训练有参考价值
- Web-CogBench 的认知维度评估方法可启发更好的 Agent 评测设计

## 评分
- 新颖性: ⭐⭐⭐⭐ (Bloom分类法与Web Agent的结合新颖，但知识注入的思路本身不全新)
- 实验充分度: ⭐⭐⭐⭐⭐ (4个benchmark、详细消融、组件分析、在线任务评估)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，但篇幅较长，部分内容可精简)
- 价值: ⭐⭐⭐⭐ (提供了系统化的Web Agent知识训练方法论，Web-CogBench有实用价值)

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] Web-CogReasoner: Towards Knowledge-Induced Cognitive Reasoning for Web Agents](web-cogreasoner_towards_knowledge-induced_cognitive_reasoning_for_web_agents.md)
- [\[ICLR 2026\] WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents](webarbiter_a_principle-guided_reasoning_process_reward_model_for_web_agents.md)
- [\[ICLR 2026\] ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](st-webagentbench_a_benchmark_for_evaluating_safety_and_trustworthiness_in_web_ag.md)
- [\[ACL 2026\] SynthAgent: Adapting Web Agents with Synthetic Supervision](../../ACL2026/llm_agent/synthagent_adapting_web_agents_with_synthetic_supervision.md)
- [\[ACL 2026\] ExpSeek: Self-Triggered Experience Seeking for Web Agents](../../ACL2026/llm_agent/expseek_self-triggered_experience_seeking_for_web_agents.md)

<!-- RELATED:END -->
