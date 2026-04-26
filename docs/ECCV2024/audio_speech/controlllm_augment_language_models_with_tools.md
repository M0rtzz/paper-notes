---
title: >-
  [论文解读] ControlLLM: Augment Language Models with Tools by Searching on Graphs
description: >-
  [ECCV 2024][语音][Tool-Augmented LLM] 提出 ControlLLM 框架，通过任务分解、Thoughts-on-Graph (ToG) 图搜索范式和执行引擎三大组件，让 LLM 在预构建的工具图上搜索最优解决方案路径，准确高效地调用多模态工具完成复杂任务，在困难任务上达到 93% 的解决方案成功率。
tags:
  - ECCV 2024
  - 语音
  - Tool-Augmented LLM
  - Thoughts-on-Graph
  - Task Planning
  - 多模态
  - Tool Graph
---

# ControlLLM: Augment Language Models with Tools by Searching on Graphs

**会议**: ECCV 2024  
**arXiv**: [2310.17796](https://arxiv.org/abs/2310.17796)  
**代码**: https://github.com/OpenGVLab/ControlLLM (有)  
**领域**: Agent  
**关键词**: Tool-Augmented LLM, Thoughts-on-Graph, Task Planning, Multi-modal Interaction, Tool Graph

## 一句话总结

提出 ControlLLM 框架，通过任务分解、Thoughts-on-Graph (ToG) 图搜索范式和执行引擎三大组件，让 LLM 在预构建的工具图上搜索最优解决方案路径，准确高效地调用多模态工具完成复杂任务，在困难任务上达到 93% 的解决方案成功率。

## 研究背景与动机

1. **领域现状**：工具增强型 LLM（如 HuggingGPT、Visual ChatGPT）通过让 LLM 调用外部工具实现多模态能力延伸，已成为研究热点。
2. **现有痛点**：现有方法在工具调用上面临三大挑战——用户 prompt 歧义、工具选择和参数化不准确、工具调度效率低。基于 CoT/ToT 的方法在处理复杂拓扑结构的工具调用链时容易产生幻觉。
3. **核心矛盾**：复杂任务的解决方案往往需要复杂拓扑结构的工具调用，但链式或树式思维范式无法生成这种复杂网络。
4. **本文要解决什么**：设计一个新范式，让 LLM 准确高效地选择、参数化和调度多模态工具。
5. **切入角度**：预构建工具依赖图，将任务规划转化为图上搜索问题，而非依赖 LLM 直接生成方案。
6. **核心 idea 一句话**：在预建的工具依赖图上进行深度优先搜索找到最优工具调用路径，避免 LLM 直接推理导致的幻觉问题。

## 方法详解

### 整体框架

ControlLLM 由三个顺序阶段组成：(1) **Task Decomposition** — 将用户请求分解为多个并行子任务；(2) **Task Planning (ToG)** — 在工具图上搜索每个子任务的最优解决方案；(3) **Solution Execution** — 解析方案并调度工具执行。

### 关键设计

1. **Task Decomposer（任务分解器）**
    - **做什么**：分析用户 prompt 并分解为属性明确的子任务（描述、领域、参数、输出）。
    - **核心思路**：利用 LLM（ChatGPT 或微调 LLaMA）处理用户请求，输出 JSON 格式的子任务列表。仅做分解不做工具选择，缩小后续规划范围。
    - **设计动机**：将复杂请求拆分为可管理单元加速规划；确定任务领域缩小工具搜索范围；推断输入输出资源类型确定搜索起终点。

2. **Tool Graph Construction（工具图构建）**
    - **做什么**：预构建描述工具间依赖关系的拓扑图。
    - **核心思路**：图中有两类节点——Resource 节点（类型如 image/video/audio）和 Tool 节点（描述 desc、参数 args、返回值 ret）。两类边——Tool-Resource 边（工具产出资源）和 Resource-Tool 边（资源作为工具输入）。
    - **设计动机**：工具之间天然存在输入输出的拓扑结构，将其显式建模为图，使搜索有据可依。

3. **Thoughts-on-Graph (ToG) Search（图搜索）**
    - **做什么**：在工具图上用深度优先搜索算法寻找从输入到输出的所有可行工具链路径。
    - **核心思路**：DFS 算法从输入资源节点出发，遍历所有可行路径到达输出节点。提供四种搜索策略：Greedy（最高分工具）、Beam（k-best）、Adaptive（阈值动态调整）、Exhaustive（穷举）。引入工具评估模块用 LLM 打分过滤不相关工具。最后由 Solution Expert 选最优方案、Resource Expert 补全参数。
    - **设计动机**：搜索范式避免 LLM 幻觉；多种策略平衡效率和效果；图结构天然支持复杂拓扑方案。

4. **Execution Engine（执行引擎）**
    - **做什么**：解析搜索到的方案为 Action 序列，调度工具执行并生成回复。
    - **核心思路**：根据方案拓扑自动并行化独立子任务，维护状态记忆存储中间结果，支持本地/远程/混合端点。最后用 LLM 汇总执行结果生成用户友好回复。
    - **设计动机**：并行执行降低延迟；状态记忆支持运行时参数自动修正。

### 损失函数 / 训练策略

- **ControlLLM-ChatGPT 变体**：直接使用现成 LLM，设计精心的 prompt 进行零样本使用，无需训练
- **ControlLLM-LLaMA 变体**：用 self-instruct 方法微调 LLaMA，在任务分解、工具评估等模块获得更高性能
- **ControlLLM-Mix 变体**（默认）：混合使用两种 LLM，取长补短

## 实验关键数据

### 主实验

与 SOTA 方法对比（自建 Benchmark，~100 条指令，20+ 工具）：

| 方法 | IR↓ | NR↑ | HR↓ | CR↑ | SE (All)↑ | SE (Hard)↑ |
|------|-----|-----|-----|-----|-----------|------------|
| HuggingGPT | 0.45 | 0.64 | 0.16 | 0.69 | 0.59 | 0.33 |
| Visual ChatGPT | 0.26 | 0.58 | 0.09 | 0.76 | 0.57 | 0.10 |
| InternGPT | 0.12 | 0.51 | 0.49 | 0.43 | 0.44 | 0.00 |
| GPT4Tools | 0.19 | 0.44 | 0.28 | 0.72 | 0.43 | 0.00 |
| **ControlLLM-Mix** | **0.03** | **0.93** | **0.02** | **0.98** | **0.93** | **0.81** |

### 消融实验

不同搜索策略对比：

| 策略 | SE (All)↑ | SE (Hard)↑ | 时间复杂度 |
|------|-----------|------------|-----------|
| Greedy | 0.49 | 0.19 | 4.07 |
| Beam (k=3) | 0.88 | 0.76 | 121.29 |
| Adaptive | 0.93 | 0.81 | 236.49 |
| Exhaustive | 0.97 | 0.91 | 3444.23 |

### 关键发现

- ControlLLM 在困难任务上达到 81% 成功率，而最佳 baseline 仅 33%（HuggingGPT）或 0%（InternGPT/GPT4Tools）
- 工具图搜索范式彻底解决了 LLM 直接规划的幻觉问题（HR 从 0.09-0.49 降至 0.02）
- Adaptive 策略在效率-效果间取得最佳平衡
- 微调 LLaMA 在任务分解上显著优于 ChatGPT 零样本

## 亮点与洞察

- **范式创新**：从 CoT/ToT 到 ToG 的升级，将工具调用从 LLM "生成" 转变为图 "搜索"
- **可扩展性**：新增工具只需重建图，无需重训 LLM 或更新 prompt
- **突破 token 限制**：搜索在图上进行而非 LLM 上下文窗口中，不受 token 长度限制
- **工程完整度**：从分解到搜索到执行到回复的完整pipeline，支持图文声视多模态

## 局限性 / 可改进方向

- 工具图需要人工预定义工具的 desc/args/ret，新工具接入仍需人工配置
- Benchmark 自建且规模较小（约 100 条），评估采用三人投票制主观性较强
- Exhaustive 搜索虽效果最佳但时间代价过高（3444 vs Greedy 的 4），实际部署需权衡
- 未讨论工具出错或不可用时的容错机制

## 相关工作与启发

- 比 HuggingGPT 更进一步——后者直接让 LLM 规划，ControlLLM 将规划转为图搜索
- Graph-of-Thought 的思路启发了 ToG，但 GoT 仍依赖 LLM 生成，ToG 完全基于图结构
- ToolLLM 的 DFS 决策树类似 ToT 局限性，而 ToG 直接在工具图上 DFS 更高效准确
- 启发：构建领域工具图 + 搜索规划 是让 LLM 可靠使用工具的优秀范式

## 评分

- ⭐⭐⭐⭐⭐ 新颖性：Thoughts-on-Graph 范式新颖有效，图搜索替代 LLM 直接推理是关键创新
- ⭐⭐⭐⭐ 实验充分度：多策略、多 LLM、多 baseline 对比全面，但 benchmark 规模偏小
- ⭐⭐⭐⭐ 写作质量：框架清晰，图表直观
- ⭐⭐⭐⭐⭐ 价值：在工具增强 LLM 领域提出了关键的范式改进，困难任务成功率从 33% 到 81%

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Siamese Vision Transformers are Scalable Audio-Visual Learners](siamese_vision_transformers_are_scalable_audio-visual_learners.md)
- [\[ECCV 2024\] Listen to Look into the Future: Audio-Visual Egocentric Gaze Anticipation](listen_to_look_into_the_future_audio-visual_egocentric_gaze_anticipation.md)
- [\[ECCV 2024\] Beat-It: Beat-Synchronized Multi-Condition 3D Dance Generation](beat-it_beat-synchronized_multi-condition_3d_dance_generation.md)
- [\[ECCV 2024\] Action2Sound: Ambient-Aware Generation of Action Sounds from Egocentric Videos](action2sound_ambientaware_generation_of_action_sounds_from_e.md)
- [\[ECCV 2024\] Label-Anticipated Event Disentanglement for Audio-Visual Video Parsing](label-anticipated_event_disentanglement_for_audio-visual_video_parsing.md)

<!-- RELATED:END -->
