---
description: "【论文笔记】AgentRM: Enhancing Agent Generalization with Reward Modeling 论文解读 | ACL 2025 | arXiv 2502.18407 | Agent | 提出 AgentRM，一种可泛化的奖励模型，通过显式/隐式奖励建模和 LLM-as-a-judge 三种方式构建，配合 Best-of-N 采样和步级波束搜索引导策略模型进行测试时搜索，在 9 个 Agent 任务上平均提升 8.8 分，且展现出弱到强的泛化能力。"
tags:
  - ACL 2025
---

# AgentRM: Enhancing Agent Generalization with Reward Modeling

**会议**: ACL 2025  
**arXiv**: [2502.18407](https://arxiv.org/abs/2502.18407)  
**代码**: 即将开源  
**领域**: LLM Alignment / Agent  
**关键词**: Agent, 奖励模型, 泛化性, 测试时搜索, MCTS

## 一句话总结

提出 AgentRM，一种可泛化的奖励模型，通过显式/隐式奖励建模和 LLM-as-a-judge 三种方式构建，配合 Best-of-N 采样和步级波束搜索引导策略模型进行测试时搜索，在 9 个 Agent 任务上平均提升 8.8 分，且展现出弱到强的泛化能力。

## 研究背景与动机

基于 LLM 的 Agent 在见过的任务（held-in tasks）上表现强劲，但对未见任务（held-out tasks）泛化能力差。现有工作主要通过扩大任务多样性来微调策略模型（policy model），但作者发现这种方式存在严重问题：

**核心发现**：微调策略模型会导致对已见任务的过拟合——在 held-in 任务上提升，但在 held-out 任务上显著退化。原因在于策略模型微调会增加已见动作 token 的生成概率，同时降低未见动作的概率。

**关键假设**：微调奖励模型（RM）来引导策略模型比直接微调策略模型更鲁棒。因为奖励函数的回归训练目标对动作 token 的具体分布天然不敏感。

初步实验验证了这一假设：在单个任务上微调策略模型后做 Best-of-5，只对该 held-in 任务有正收益（对角线为正）；而微调 RM 后做 Best-of-5，绝大多数任务都获得正收益，呈现出明显的泛化性。

## 方法详解

### 整体框架

AgentRM 的流程分为四步：
1. **行为克隆（SFT）**：在专家轨迹上微调得到具有基本任务能力的策略模型
2. **搜索树构建**：用 SFT 模型探索环境，构建搜索树
3. **训练奖励模型**：从搜索树中提取状态-奖励对训练 RM
4. **测试时搜索**：用 RM 引导策略模型在未见任务上搜索最优动作

### 关键设计

**1. 任务形式化**

Agent 任务建模为部分可观测马尔可夫决策过程（POMDP），包含指令空间、状态空间、动作空间、观测空间、状态转移函数和奖励函数。环境只在最后一步提供结果奖励（outcome reward），中间步骤的奖励需要通过 RM 估计。

**2. 三种奖励建模方法**

**显式奖励建模（Explicit RM）**：
- 将过程奖励定义为 Q 值（从某状态出发的期望累积奖励）
- 使用受 MCTS 启发的树搜索算法构建搜索树来估计 Q 值
- 搜索树的每次迭代包含四步：选择（UCB）→ 扩展（采样 k 个动作）→ 模拟（n 条完整轨迹取平均）→ 反向传播（更新访问次数和状态值）
- 过滤访问次数低于阈值 λ 的状态以保证质量
- 用 MSE 损失训练带 value head 的语言模型

**隐式奖励建模（Implicit RM）**：
- 将过程奖励定义为优势函数（advantage），即某动作相对于替代动作的相对收益
- 利用策略模型和参考模型的对数似然比隐式推导步级奖励：r_θ^t = β·log(π_θ(a_t|s_t) / π_ref(a_t|s_t))
- 对每个指令采样 16 条完整轨迹，用 MSE 损失训练

**LLM-as-a-judge**：
- 无需训练，直接提示 LLM 作为选择器评估轨迹质量
- 属于训练自由（training-free）方法

**3. 奖励引导搜索**

- **Best-of-N**：采样 N 条完整轨迹，用 RM 选最优
- **步级波束搜索**：初始采样 W1×W2 个动作 → 用 RM 评分 → 保留 top-W1 → 每个扩展 W2 → 迭代至终止

### 损失函数 / 训练策略

- 行为克隆：标准 SFT 损失，在专家轨迹的动作 token 上计算交叉熵
- 显式 RM 训练：MSE 损失，拟合 MCTS 估计的状态值
- 隐式 RM 训练：MSE 损失，拟合环境提供的标量奖励（进度率）
- 使用 LLaMA-3-8B-Instruct 作为策略模型，训练数据来自 Webshop、Alfworld、Sciworld 三个 held-in 任务

## 实验关键数据

### 主实验

**与通用 Agent 对比（9 个任务，6 个 held-out）**：
- Greedy Search 基线：52.7
- Explicit RM + Best-of-5：61.5（+8.8）
- Implicit RM + Best-of-5：54.7
- LLM-as-a-judge + Best-of-5：52.1（-0.6，8B 模型直接当 judge 效果差）
- Explicit RM + Beam Search (5,5)：63.3
- 超越最佳通用 Agent（AgentGym 59.3）4.0 分

**与专用 Agent 对比（3 个 held-in 任务）**：
- Webshop: Explicit RM + Best-of-5 达 71.0（QLASS 70.3），Beam Search 达 75.3
- Alfworld: Best-of-5 达 94.8（QLASS 82.8），Beam Search 达 96.3
- Sciworld: Best-of-5 达 76.1（Agent-R 70.2），Beam Search 达 82.6
- 全面超越 QLASS、Agent-R 等专用 Agent

### 消融实验

**鲁棒性测试**：对 Alfworld 的 5 种指令扰动：
- AgentGym 平均成功率从 61.9 降到 36.3（-25.6），标准差 20.0
- Agent-FLAN 从 67.2 降到 36.9（-30.3），标准差 22.0
- AgentRM 从 54.5 到 52.4（平均 53.0），标准差仅 2.7，鲁棒性显著更好

**状态表示消融**：
- 移除 thought 或 observation 单独影响小
- 同时移除 thought 和 observation 导致 3.2 分下降
- 建模主要依赖 action token

**弱到强泛化**：
- LLaMA-3-70B 上 RM 提升 12.6 分（62.4→74.9）
- AgentGen 上提升 5.9 分，在更强模型上收益更大

### 关键发现

1. **显式 RM 一致最优**：三种 RM 方法中，显式 RM 在所有任务类型上最有效
2. **RM 泛化性强于策略模型微调**：RM 微调不会过拟合到特定动作分布
3. **扰动鲁棒性**：AgentRM 学到的是决策能力而非记忆模式
4. **数据效率高**：仅 4k 状态即可训练出超越 LLM-as-a-judge 的 RM
5. **跨模型泛化**：8B 模型采样训练的 RM 可直接用于 70B 模型
6. **测试时计算可扩展**：显式 RM 随 N 增大持续提升，隐式 RM 和 LLM-as-a-judge 存在饱和或退化

## 亮点与洞察

- 通过 Figure 1 的可视化对比，直观展示了"微调策略模型 vs 微调 RM"在泛化性上的本质差异，motivation 非常有说服力
- MCTS 启发的搜索树构建方法有效解决了 Agent 任务中长链推理和大搜索空间的挑战
- 弱到强泛化现象（weak-to-strong generalization）具有重要的工程意义：便宜模型生成训练数据，昂贵模型享受收益
- 训练数据的 log-linear 增长趋势暗示性能尚未饱和

## 局限性 / 可改进方向

- 隐式 RM 和 LLM-as-a-judge 在大 N 时性能不稳定，需要进一步研究测试时计算的 scaling law
- 搜索树构建的计算成本较高（需要多次环境交互）
- 当前仅在 3 个 held-in 任务上训练 RM，任务多样性扩展的效果有待探索
- RM 对通用推理任务（GSM8k、MATH）影响可忽略，说明 Agent 和推理的 RM 可能需要不同设计
- 未探索更大规模 RM 模型的效果

## 相关工作与启发

- 与 Agent-FLAN、AgentGym 等"扩大训务多样性"的路线形成互补：前者改善策略模型，AgentRM 改善引导信号
- 显式 RM 使用 MCTS 构建训练数据，与 AlphaGo/AlphaZero 的思路一脉相承
- 弱到强泛化的发现与 OpenAI 的 weak-to-strong generalization 研究方向呼应
- 对 RLHF 和 test-time compute 两个热点主题都有贡献

## 评分

- **新颖性**: 8/10 — RM 引导 Agent 的视角新颖，实验设计全面
- **技术深度**: 8/10 — 三种 RM 方法的深入对比，MCTS 树搜索实现完整
- **实用性**: 8/10 — 弱到强泛化使方法具有良好的工程可行性
- **写作质量**: 8/10 — 结构清晰，分析深入，可视化有效
