---
title: >-
  [论文解读] OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use
description: >-
  [ACL 2025 (Long Paper, Oral)][LLM Agent][OS Agent] 首个系统性综述基于（多模态）大语言模型的操作系统智能体（OS Agents），按"环境-基础能力-构建方法-评估基准-商业产品-挑战"的框架全面梳理了 50+ 学术工作和 4 大商业产品的技术演进，并前瞻性地分析了安全、个性化和自进化等未来方向。
tags:
  - ACL 2025 (Long Paper, Oral)
  - LLM Agent
  - OS Agent
  - GUI Agent
  - MLLM
  - 自主操作
  - 计算机使用
---

# OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use

**会议**: ACL 2025 (Long Paper, Oral)  
**arXiv**: [2508.04482](https://arxiv.org/abs/2508.04482)  
**网站**: https://os-agent-survey.github.io/
**领域**: LLM Agent / 多模态VLM  
**关键词**: OS Agent, GUI Agent, MLLM, 自主操作, 计算机使用

## 一句话总结

首个系统性综述基于（多模态）大语言模型的操作系统智能体（OS Agents），按"环境-基础能力-构建方法-评估基准-商业产品-挑战"的框架全面梳理了 50+ 学术工作和 4 大商业产品的技术演进，并前瞻性地分析了安全、个性化和自进化等未来方向。

## 研究背景与动机

**领域现状**：OS Agent 是指能像人类一样使用电脑、手机和浏览器的 AI 智能体——通过 GUI 或 CLI 操作完成用户指定的任务。随着 GPT-4V、Claude、Gemini 等 MLLM 的涌现，OS Agent 从学术概念变为了商业现实：OpenAI Operator、Anthropic Computer Use、Apple Intelligence、Google Project Mariner 等产品相继发布。

**现有痛点**：学术研究高度分散——不同工作分别聚焦于手机、电脑或浏览器平台，使用不同的术语和评估方法，缺乏统一的综述和分类框架来理解全貌。

**核心矛盾**：该领域发展极快但缺乏系统性梳理，研究者和开发者难以把握技术现状和核心挑战。

**本文要解决什么？** 提供一个全面、结构化的综述，覆盖 OS Agent 的定义、核心能力、构建方法、评估基准和落地产品。

**切入角度**：按"环境→能力→方法→评估→产品→挑战"的自顶向下框架组织，同时从平台（手机/电脑/浏览器）和方法（基础模型/Agent框架）两个维度交叉分析。

**核心idea一句话**：以统一框架全景式梳理 OS Agent 领域，从基础概念到商业落地。

## 综述内容概述

### 整体框架

本综述按六部分组织：(1) OS Agent 基础定义（环境、观察空间、动作空间）；(2) 三大核心能力（理解、规划、定位）；(3) 构建方法（基础模型 + Agent 框架）；(4) 评估基准与协议；(5) 商业产品；(6) 挑战与未来方向。

### 关键内容

1. **OS Agent 基本组成**:

    - 环境（Environment）：三大操作平台——计算机桌面、手机、浏览器
    - 观察空间（Observation Space）：屏幕截图（视觉输入）、HTML 代码（结构化文本）、可访问性树（A11y Tree，语义化 GUI 描述）
    - 动作空间（Action Space）：点击、输入、滑动、长按、导航等基础操作。部分系统支持更高级的函数调用

2. **三大核心能力**:

    - 理解（Understanding）：识别复杂 GUI 界面中的小图标、密集文本和多层嵌套元素。高分辨率屏幕和动态内容使理解仍然困难
    - 规划（Planning）：将复杂的用户任务（如"订一张去北京的机票"）分解为子任务序列，并根据环境反馈动态调整计划。常用策略包括目标分解、反思（Reflexion）和任务图规划
    - 定位（Grounding）：将文本指令精确映射到屏幕上的具体 UI 元素和可执行动作（坐标点击、元素 ID、API 调用）。这是连接"理解了什么"与"执行什么"的关键桥梁

3. **构建方法——基础模型**:

    - 直接使用现有 LLM/MLLM：以 GPT-4V、Claude 等通用大模型为 backbone，通过 prompt 工程实现 Agent 功能
    - MLLM + 额外视觉模块：CogAgent 采用高低分辨率双编码器解决小元素检测问题，Ferret-UI 针对移动端界面设计
    - 定制架构：SeeClick、OS-Atlas 等专门针对 GUI 场景设计，在 GUI grounding 上表现突出
    - 训练策略三阶段：预训练（大规模 GUI 截图+操作数据）→ SFT（GUI 任务指令数据微调）→ RL（在线交互反馈强化学习）

4. **构建方法——Agent 框架**:

    - 观察处理：Set-of-Mark 提示（在截图上标注可交互元素编号）、HTML/A11y Tree 解析、OCR 辅助
    - 记忆机制：短期工作记忆（动作历史、当前状态）和长期经验记忆（知识库、过往成功案例）
    - 规划策略：目标分解（将复杂任务拆分为子任务链）、反思（Reflexion，从失败中学习并重新规划）、任务图规划
    - 动作定位：坐标预测（直接输出屏幕坐标）、元素 ID 匹配（通过 A11y Tree 的元素标识符）、函数调用

5. **评估基准**:

    - 手机平台：AndroidWorld（真实安卓环境端到端评估）、AITW（大规模安卓操作轨迹数据集）
    - 电脑平台：OSWorld（跨平台真实 OS 环境）、WindowsAgentArena（Windows 桌面自动化评估）
    - 浏览器平台：Mind2Web（大规模真实网页任务）、WebArena（可交互网页环境）、WebVoyager（端到端网页导航评估）
    - 跨平台：AssistantBench（复杂跨应用任务评估）

6. **商业产品**:

    - OpenAI Operator：任务自动化服务，通过浏览器完成用户指定任务
    - Anthropic Computer Use：Claude 直接操作用户电脑，支持截图理解和鼠标键盘操控
    - Apple Intelligence：集成 Siri + 设备操作，深度绑定 iOS/macOS 生态
    - Google Project Mariner：Chrome 扩展形式的 Agent，在浏览器标签页中自动执行任务

## 实验关键数据

### 主要 Benchmark 汇总

| 平台 | 代表性 Benchmark | 数据规模 | 特点 |
|------|----------------|---------|------|
| 手机 | AndroidWorld | 116 任务 | 真实安卓环境，端到端评估 |
| 手机 | AITW | 715K 轨迹 | 大规模人类操作轨迹 |
| 电脑 | OSWorld | 369 任务 | 跨 Linux/Windows/macOS |
| 浏览器 | WebArena | 812 任务 | 可交互真实网站环境 |
| 浏览器 | Mind2Web | 2350 任务 | 137 真实网站，多域覆盖 |
| 跨平台 | AssistantBench | 214 任务 | 复杂多步跨应用任务 |

### 模型性能横向对比

| 模型/方法 | 类别 | OSWorld 成功率 | 关键特点 |
|----------|------|-------------|---------|
| GPT-4V (SoM) | 通用MLLM | ~12% | 截图理解 + Set-of-Mark |
| Claude Computer Use | 商业Agent | ~15% | 端到端电脑操控 |
| CogAgent | 专用模型 | — | 高低分辨率双编码器 |
| SeeClick | GUI专用 | — | 专注 GUI grounding |

### 关键发现

- 即使最强模型在 OSWorld 上的成功率也仅约 12-15%，表明复杂桌面操作任务仍极具挑战性
- 长步骤任务（10-50 步操作）中错误累积导致成功率急剧下降，是当前最大瓶颈
- 在一个 App 上训练的 Agent 难以迁移到其他 App，泛化性是核心开放问题
- 浏览器场景因 HTML 提供了丰富的结构化信息，通常比纯视觉的桌面/手机场景更容易

## 亮点与洞察

- 全景式覆盖从基础概念到商业产品，三维度（平台/方法/能力）组织框架清晰且信息密度高
- 时间线完整（2023 年早期工作到 2025 年最新进展），涵盖 50+ 学术工作和 4 大商业产品
- 对安全与隐私的分析有前瞻性：OS Agent 直接操作用户设备，面临 prompt injection、对抗攻击、数据泄露等风险，这是商业化的核心技术障碍
- 指出了一个重要的技术洞察：GUI 理解本质上是一种特殊的文档理解，与 mPLUG-DocOwl2 等技术可以互通

## 局限性 / 可改进方向

- 作为综述缺乏统一的实验对比，不同 benchmark 的结果难以横向比较
- 对 Agent 的计算成本和延迟问题讨论不够深入——每步 MLLM 推理在实际部署中是关键瓶颈
- 多 Agent 协作和复杂工作流（如跨应用数据流转）的讨论篇幅有限
- 未深入探讨如何评估 OS Agent 的"实际可用性"（用户体验维度的评估几乎缺失）
- 对非英语环境/非西方 App 的覆盖有限

## 相关工作与启发

- **vs GUI 理解工作（mPLUG-DocOwl2）**: GUI 理解是文档理解的特殊形式，VLM 的文档理解能力进步可直接迁移
- **vs VLM Grounding 工作**: Agent 的"定位"能力可以受益于视觉定位（visual grounding）和证据提示（visual evidence prompting）技术的提升
- **vs 推理/搜索方法（MCTS）**: Agent 的长步骤推理问题可以借鉴树搜索/蒙特卡洛树搜索方法来缓解错误累积
- **vs 安全研究**: Prompt injection 防御是 OS Agent 商业化的核心前提——需要在 Agent 和用户设备之间建立可靠的安全边界

## 评分

- 新颖性: ⭐⭐⭐ 综述文章的新颖性体现在分类框架和前瞻性分析上，框架设计清晰
- 实验充分度: ⭐⭐⭐ 作为综述覆盖广泛但缺乏原创实验
- 写作质量: ⭐⭐⭐⭐⭐ 结构清晰、信息密度高、图表丰富
- 价值: ⭐⭐⭐⭐ 对 OS Agent 领域的研究者和开发者都有很好的参考价值
