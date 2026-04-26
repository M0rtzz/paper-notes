---
title: >-
  [论文解读] M2-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining
description: >-
  [ICLR 2026][LLM Agent][GUI Agent] 提出 M2-Miner，首个基于 MCTS 的自动化移动 GUI 代理数据挖掘框架，通过 InferAgent/OrchestraAgent/JudgeAgent 三代理协作、意图回收策略和渐进式模型闭环训练，以 18 倍低于人工标注的成本生成 SOTA 质量的数据。
tags:
  - ICLR 2026
  - LLM Agent
  - GUI Agent
  - 数据挖掘
  - 蒙特卡洛树搜索
  - 多智能体协作
  - 意图回收
---

# M2-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining

**会议**: ICLR 2026  
**arXiv**: [2602.05429](https://arxiv.org/abs/2602.05429)  
**代码**: 即将公开  
**领域**: LLM Agent  
**关键词**: GUI Agent, 数据挖掘, 蒙特卡洛树搜索, 多智能体协作, 意图回收  

## 一句话总结

提出 M2-Miner，首个基于 MCTS 的自动化移动 GUI 代理数据挖掘框架，通过 InferAgent/OrchestraAgent/JudgeAgent 三代理协作、意图回收策略和渐进式模型闭环训练，以 18 倍低于人工标注的成本生成 SOTA 质量的数据。

## 研究背景与动机

GUI 代理（操控图形界面完成用户意图的智能体）的训练严重依赖高质量的意图-轨迹（intent-trajectory）数据。现有数据集面临三大挑战：

1. **高构建成本**：手动标注每条数据需数小时（如 Android Control 88k 图片花费 ~$31,662）
2. **数据质量差**：手动标注和自动挖掘数据常含冗余步骤、模糊意图描述和偏差操作路径
3. **数据丰富度低**：现有数据集仅记录单一成功路径（flat 结构），意图单调，缺乏描述信息

现有自动挖掘方法的不足：

- **AgentQ**：基于 MCTS 但仅支持 HTML 解析的 Web 环境，不支持移动端视觉场景
- **OS-Genesis**：基于规则的逐步交互+逆任务合成，缺乏结构化探索
- 直接应用原始 MCTS 到 GUI 数据挖掘效率极低：随机扩展和基于 rollout 的奖励计算代价过高

## 方法详解

### 整体框架

M2-Miner 基于 MCTS 四阶段循环（选择→扩展→模拟→反向传播），引入三代理协作增强扩展和模拟阶段。

**意图-轨迹树**形式化为 $\mathcal{T} = (\mathcal{V}, \mathcal{A}, \mathcal{P}, \mathcal{I})$：

- $\mathcal{V}$：节点集合，每个节点对应 GUI 状态
- $\mathcal{A}$：可执行动作集（点击、滑动、输入）
- $\mathcal{P}$：边集合（状态转移关系）
- $\mathcal{I}$：用户意图集合

每个节点 $v$ 定义为五元组 $(\mathit{img}_v, \mathit{meta}_v, Q_v, N_v, \mathit{stat}_v)$。

### 关键设计

**三代理协作框架**：

1. **InferAgent**：在扩展阶段推断最可能达成目标意图的动作。使用多个不同 MLLM 生成 $K$ 个候选动作，确保多样性。加入历史动作到提示中防止重复生成。

2. **OrchestraAgent**：合并等价动作并按置信度排序。通过多选题方式进行 $K-1$ 次查询得到排序后的动作队列，排序后的动作被赋予递减的初始 UCT 值。

3. **JudgeAgent**：替代成本高昂的 rollout 模拟。分析新扩展节点的 GUI 截图，判断任务完成状态并计算奖励：

$$r_{\text{intermediate}} = \frac{\exp(logits_{\text{valid}})}{\exp(logits_{\text{valid}}) + \exp(logits_{\text{invalid}})}$$

使用 softmax 归一化 MLLM 输出的 logits 为 [0,1] 范围的奖励值。节点 Q 值更新：

$$Q_i = \frac{Q_{i-1} \times N_{i-1} + R_i}{N_{i-1} + 1}, \quad N_i = N_{i-1} + 1$$

**意图回收策略（Intent Recycling）**：

核心观察：MCTS 树中除了原始意图的成功路径外，其他路径也可能对应有价值的新意图。例如在地图应用中，原始意图是查询路线，但误点"叫车"按钮产生了额外的叫车意图轨迹。

流程：

1. 对每棵完成的树，考虑从根到每个节点的路径
2. 使用 MLLM 构建意图回收过滤器评估轨迹质量
3. 对通过过滤的轨迹，使用 MLLM 生成匹配的新意图
4. 由 JudgeAgent 验证轨迹最后节点状态是否为成功

### 训练策略

**渐进式模型闭环训练（Model-in-the-Loop）**：

- **预热阶段**：用公开数据集训练 InferAgent 和 JudgeAgent 获得基础能力
- **Stage 1（基础意图）**：收集热门应用主页截图→生成常用服务意图→条件改写扩展→挖掘轨迹→训练
- **Stage 2（复杂意图）**：对 Stage 1 意图添加条件和功能组合（如"订酒店"→"订酒店+订机票"）→挖掘→训练
- **Stage 3（回收意图）**：对所有历史树应用意图回收策略→丰富轨迹→训练

基础模型：InferAgent 和 JudgeAgent 用 Qwen2.5-VL-7B，OrchestraAgent 用 Qwen2.5-VL-72B。

## 实验关键数据

### 主实验：GUI 代理性能

| 模型 | AC-Low TP/SR | AC-High TP/SR | AITZ TP/SR | CAGUI TP/SR |
|------|:-:|:-:|:-:|:-:|
| GPT-4o | 74.3/19.4 | 66.3/20.8 | 70.0/35.3 | 3.67/3.67 |
| Qwen2.5-VL-7B | 94.1/85.0 | 75.1/62.9 | 78.4/54.6 | 74.2/55.2 |
| UI-TARS-7B* | 98.0/90.8 | 83.7/72.5 | 80.4/65.8 | 88.6/70.0 |
| OS-Genesis-7B | 90.7/74.2 | 66.2/44.5 | 20.0/8.5 | 38.1/14.5 |
| GUI-Owl-7B | 93.8/90.0 | 81.5/72.8 | 78.9/65.1 | 80.0/59.2 |
| **M2-Miner-7B** | **97.5/93.5** | 81.8/**72.9** | **81.3/69.4** | **88.8/70.2** |

M2-Miner-7B 在几乎所有基准上达到 SOTA，在 SR 指标上一致超越使用大规模私有数据的 UI-TARS-7B。

### 数据效率对比

| 数据集 | 图片数 | 自动化 | 适合RL | 成本(USD) | 每图成本 |
|------|:-:|:-:|:-:|:-:|:-:|
| Android Control | 88k | ✗ | ✗ | $31,662 | $0.36 |
| AMEX | 38k | ✗ | ✗ | $13,680 | $0.36 |
| GUI-Odyssey | 119k | ✗ | ✗ | $42,816 | $0.36 |
| **M2-Miner-Agent** | 20k | **✓** | **✓** | **$466** | **$0.02** |

每图成本仅 $0.02，是手动标注的 **1/18**。

### 消融实验

**多代理框架效率**：

与仅使用 InferAgent 的原始 MCTS 相比，M2-Miner 的效率提升随任务复杂度指数增长，在任务长度为 9 时达到 **64× 加速**。

**模型闭环训练**：

| 阶段 | TP | SR |
|------|:-:|:-:|
| Warm-up | 85.0 | 64.2 |
| +Stage 1 (基础意图) | 86.5 | 67.3 |
| +Stage 2 (复杂意图) | 87.6 | 69.1 |
| +Stage 3 (回收意图) | 88.2 | 69.9 |

**数据结构消融**：

| 设置 | TP | SR |
|------|:-:|:-:|
| 仅动作 | 85.2 | 66.8 |
| 动作+描述 | 88.2 | 69.9 |
| 动作+描述+偏好 | **88.8** | **70.2** |

### 关键发现

1. **自动挖掘数据质量超越人工标注**：M2 数据的 DQA 高于 Android Control 和 AITZ
2. **意图回收显著丰富多样性**：t-SNE 可视化显示回收意图覆盖更广的语义空间
3. **描述和偏好数据有额外价值**：MCTS 树中保留的语义描述和偏好信号对训练有益
4. **在未见场景中泛化**：CAGUI 无训练数据，M2-Miner 将 Qwen2.5-VL-7B 的 SR 从 55.2% 提升至 70.2%

## 亮点与洞察

- **MCTS 首次用于移动 GUI 数据挖掘**：通过树结构完整记录探索过程，远比 flat 结构信息丰富
- **过程奖励替代结果奖励**：JudgeAgent 的中间节点奖励设计避免了昂贵的 rollout，是效率提升的关键
- **意图回收的巧妙性**：将 MCTS 探索中的"失败路径"变废为宝，这一洞察非常优雅
- **成本效益极高**：$466 挖掘的数据训练出的模型超越了 $42,816 人工标注数据训练的模型
- **偏好数据的自然获取**：MCTS 树天然包含正例（成功路径）和负例（失败分支），可直接构建偏好对

## 局限性 / 可改进方向

1. 当前仅在移动端验证，Web 环境和桌面端的扩展需要额外适配
2. OrchestraAgent 依赖 72B 模型，挖掘成本虽低于人工但 API 费用仍可观
3. 意图回收的质量依赖 MLLM 的意图生成能力，可能引入不准确的意图描述
4. 渐进训练策略需要多轮挖掘-训练迭代，整体流程时间较长
5. 评估主要基于静态基准，缺乏在真实用户场景中的评估

## 相关工作与启发

- **与 AgentQ 的改进**：AgentQ 也用 MCTS 但仅支持 Web HTML 环境且原始 MCTS 效率低，M2-Miner 扩展到移动视觉场景并用多代理大幅提升效率
- **与 OS-Genesis 的区别**：OS-Genesis 用非结构化的规则探索+逆任务合成，M2-Miner 用 MCTS 树结构+前向意图驱动，数据质量更高
- **对数据飞轮的启发**：渐进训练策略展示了 "数据→模型→更好的数据→更好的模型" 的正反馈循环，是自动化数据生成的通用范式

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ — 首个 MCTS+多代理的 GUI 数据挖掘框架，意图回收策略原创性强
- **技术深度**: ⭐⭐⭐⭐ — 三代理设计合理，过程奖励替代 rollout 有理论支撑
- **实验充分度**: ⭐⭐⭐⭐⭐ — 5 个基准、成本分析、多维消融、质量评估
- **写作质量**: ⭐⭐⭐⭐ — 结构完整，图示清晰
- **实用性**: ⭐⭐⭐⭐⭐ — 极低成本实现 SOTA，对 GUI 代理社区有直接推动作用
- **综合评分**: ⭐⭐⭐⭐⭐ (9/10)

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] M²-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining](m2-miner_multi-agent_enhanced_mcts_for_mobile_gui_agent_data_mining.md)
- [\[ICLR 2026\] FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](fingertip_20k_a_benchmark_for_proactive_and_personalized_mobile_llm_agents.md)
- [\[ICLR 2026\] Efficient Agent Training for Computer Use](efficient_agent_training_for_computer_use.md)
- [\[ICLR 2026\] CoMind: Towards Community-Driven Agents for Machine Learning Engineering](comind_towards_community-driven_agents_for_machine_learning_engineering.md)
- [\[ICLR 2026\] HAMLET: A Hierarchical and Adaptive Multi-Agent Framework for Live Embodied Theatre](hamlet_a_hierarchical_and_adaptive_multi-agent_framework_for_live_embodied_theat.md)

<!-- RELATED:END -->
