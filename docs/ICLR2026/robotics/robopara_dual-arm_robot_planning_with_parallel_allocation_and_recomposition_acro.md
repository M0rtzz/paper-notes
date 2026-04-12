---
title: >-
  [论文解读] RoboPARA: Dual-Arm Robot Planning with Parallel Allocation and Recomposition Across Tasks
description: >-
  [ICLR 2026][机器人][dual-arm manipulation] 提出 RoboPARA，一个 LLM 驱动的双臂机器人并行任务规划框架，通过依赖图生成与图重遍历调度两阶段方法，最大化双臂协同并行性，执行时间减少 30%-50%。
tags:
  - ICLR 2026
  - 机器人
  - dual-arm manipulation
  - LLM task planning
  - DAG
  - parallel scheduling
  - System-1+2
---

# RoboPARA: Dual-Arm Robot Planning with Parallel Allocation and Recomposition Across Tasks

**会议**: ICLR 2026  
**arXiv**: [2506.06683](https://arxiv.org/abs/2506.06683)  
**代码**: [GitHub](https://github.com/AiDuanshiying/RoboPARA)  
**领域**: Robotics / Task Planning  
**关键词**: dual-arm manipulation, LLM task planning, DAG, parallel scheduling, System-1+2  

## 一句话总结
提出 RoboPARA，一个 LLM 驱动的双臂机器人并行任务规划框架，通过依赖图生成与图重遍历调度两阶段方法，最大化双臂协同并行性，执行时间减少 30%-50%。

## 背景与动机
1. 双臂机器人在复杂多任务场景中具有关键优势，但现有方法多关注任务成功率而忽略并行性
2. 现有 LLM 规划方法（如 RoCo、FLTRNN）主要产生单臂顺序执行计划
3. 类比人类日常行为：烧水时同时刷牙，关键在于推理哪些任务可并行、哪些需同步
4. 双臂协同调度问题（何时同步、何时解耦）在现有研究中缺乏探索
5. 缺少专门评估双臂并行规划的标准化基准数据集
6. System-1+System-2 架构中，System-2 层面的长时程并行双臂规划是关键空白

## 方法（框架/设计）
- **两阶段架构**:
  - **Stage 1 — 依赖图生成**: 利用 RAG 从记忆系统（短期观察 + 长期执行历史）中检索任务知识，构造结构化 prompt 让 LLM 生成 DAG；通过 3 类错误检测（跨对象依赖/跳过步骤/无关依赖）进行迭代修正
  - **Stage 2 — 图重遍历并行调度**: 维护调度队列，根据依赖满足度、臂空闲状态和对象持有一致性进行任务分配；单臂任务分配给空闲臂，双臂任务需两臂同步
- **形式化约束**: ①任务依赖（拓扑序）②臂互斥（同一臂不重叠）③臂锁定一致性（pick-use-place 同臂执行）④死锁预防（回滚较后执行的 pick 链）
- **目标**: 最小化 makespan $C_{\max} = \max_{v}(\sigma(v) + t_v)$

## 实验关键数据
| 指标 | RoboPARA vs 基线 |
|------|-----------------|
| 并行/协同步数 | 平均 4.5× 于其他方法 |
| 执行时间减少 | 30%-50% |
| Hard 任务成功率 | 比基线平均高 34% |
| 任务失败率(TFR) | Kitchen 场景为 0 (最优) |
| TEI (效率指标) | Kitchen 1.407, Office 1.553 (远超基线) |

- 基线: LLM³、ChatGPT-Prompts、VOYAGER、Embodied TaPA、LLM-Planner、FLTRNN、RoCo
- LLM 基础: GPT-4o 和 DeepSeek V3; 物理验证: Franka Research 3 + UR5e
- X-DAPT 数据集: 10 场景 × 3 难度 × 1000+ 任务包, 首个专注双臂并行评估的 benchmark

## 亮点
- 首次系统性定义和解决双臂协同调度问题，填补了 LLM 规划中并行性优化的空白
- DAG + 图重遍历的两阶段设计优雅且可解释，死锁预防机制实用
- X-DAPT 数据集覆盖 10 个贴近日常生活的场景，具有较高 benchmark 价值
- 硬件验证（人形机器人 + 工业臂）增强了可信度

## 局限性
- 任务基元（pick/use/place）需预定义，未处理更灵活的操作空间
- DAG 构建依赖 LLM 的正确理解，实际复杂场景可能仍有未覆盖的错误模式
- 未讨论执行失败后的在线重规划能力
- 场景以桌面操作为主，缺乏移动操作或人机交互场景

### 损失函数 / 训练策略
- Stage 1（DAG 生成）采用迭代 LLM 调用 + 结构验证 + 错误反馈的自修正流程,无需梯度训练
- Stage 2（调度优化）通过确定性算法求解,基于优先级队列和死锁检测+回滚实现
- System-1 动作执行端使用 ACT、DP、π₀ 等算法训练，与 System-2 规划解耦

## 实验关键数据

### 主实验

| 场景 | 指标 | RoboPARA | RoCo | VOYAGER | LLM-Planner |
|------|------|----------|------|---------|-------------|
| Kitchen | TEI↑ | **1.407** | 0.893 | 0.842 | 0.867 |
| Kitchen | TFR↓ | **0.000** | 0.167 | 0.222 | 0.194 |
| Office | PPR↑ | **4.5×** 基线 | 1.0× | 0.8× | 1.1× |
| Factory | Hard 成功率 | **+34%** | 基线 | 基线-10% | 基线-5% |

### 消融实验

| 配置 | Hard 成功率 | 并行步数 | 说明 |
|------|-----------|---------|------|
| Full RoboPARA | 最高 | 4.5× | 完整模型 |
| w/o DAG 修正 | -15% | 3.2× | 去掉结构验证后依赖关系频繁出错 |
| w/o 死锁检测 | -25% | 4.0× | 死锁导致执行中断 |
| 单臂顺序执行 | -40% | 1.0× | 完全退化为顺序规划 |
| GPT-4o vs DeepSeek V3 | 相当 | 相当 | LLM 选择影响不大 |

### 关键发现
- 并行调度带来的执行时间减少 30%-50%，且在 Hard 难度任务上优势最显著
- DAG 结构验证中最常见的错误是跨对象依赖（操作依赖了不相关对象的 place 节点）
- 死锁预防的回滚机制在 Factory 场景中触发最频繁，因为该场景的双臂任务比例最高
- 硬件验证（Franka Research 3 + UR5e）的成功率与仿真一致，证明方法的实际可部署性

## 亮点与洞察
- **问题定义本身就是贡献**：首次系统性地定义了双臂协同调度问题（Dual-Arm Cooperative Scheduling Problem），填补了 LLM 规划中并行性优化的空白。现有工作只关注"任务能否完成"，本文关注"任务能否高效完成"。
- **DAG + 图重遍历的两阶段设计**是本文最优雅的地方：Stage 1 解决"做什么"，Stage 2 解决"怎么分配"，解耦使得每阶段可以独立优化和扩展。
- **X-DAPT 数据集**覆盖 10 个贴近日常生活的场景（厨房到灾难救援），是领域首个专注双臂并行评估的 benchmark，对后续研究的推动价值很大。
- **归纳偏置的胜利**：约束满足和图论方法在这类有明确结构的规划问题上比端到端学习更可靠。

## 局限性 / 可改进方向
- 任务基元（pick/use/place/open/close）需预定义，无法处理更灵活或连续的操作空间
- DAG 构建完全依赖 LLM 的正确理解，实际复杂场景（如工具共享、资源竞争）可能有未覆盖的错误模式
- 未讨论执行失败后的在线重规划能力——现实中执行端失败后 System-2 需要动态调整
- 场景以桌面定点操作为主，缺乏移动操作、人机交互或动态环境的验证
- 调度算法是确定性的，未考虑不确定性（如动作时间的随机性）

## 相关工作与启发
- **vs RoCo (Mandi et al. 2023)**：RoCo 用多智能体对话实现协调，但本质上仍是顺序规划；RoboPARA 通过 DAG 显式建模并行性，效率和可靠性全面领先
- **vs MAPF-GPT**：MAPF-GPT 用 Transformer 处理多智能体路径规划，RoboPARA 用 DAG+图重遍历处理多臂任务规划，结构化先验都是关键
- **vs FLTRNN (Zhang et al. 2024)**：FLTRNN 用 RNN 框架增强长时程规划，但不处理并行分配；RoboPARA 的 Stage 2 正好解决了 FLTRNN 缺失的并行维度
- 本文的 DAG 调度+死锁预防框架可以迁移到多机器人协同（不局限于双臂）

## 评分
- 新颖性: ⭐⭐⭐⭐ 双臂并行调度问题定义+DAG 调度方案均为新颖贡献
- 实验充分度: ⭐⭐⭐⭐ 多场景多难度多基线+硬件验证，X-DAPT 数据集有价值
- 写作质量: ⭐⭐⭐⭐ 形式化清晰，数学定义严谨，图表丰富
- 价值: ⭐⭐⭐⭐ 问题定义和数据集对后续研究有持续推动作用
