---
title: >-
  [论文解读] THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning
description: >-
  [ICLR 2026][机器人][tool-integrated reasoning] 提出 THOR（Tool-Integrated Hierarchical Optimization via RL），通过三个互补组件系统性解决 LLM 工具集成数学推理中的核心挑战：TIRGen 数据构建管线生成策略对齐的 TIR 训练数据、层次化强化学习（episode 级解题+step 级代码修正）缓解稀疏奖励、自修正推理机制利用工具反馈在线纠错。在 MATH500、AIME 等多个数学基准上达到同规模 SOTA，同时在代码生成基准上也有提升。
tags:
  - ICLR 2026
  - 机器人
  - tool-integrated reasoning
  - hierarchical RL
  - GRPO
  - code generation
  - self-correction
  - mathematical reasoning
---

# THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

**会议**: ICLR 2026  
**arXiv**: [2509.13761](https://arxiv.org/abs/2509.13761)  
**代码**: [GitHub](https://github.com/JingMog/THOR)  
**领域**: LLM Reasoning / Mathematical Reasoning  
**关键词**: tool-integrated reasoning, hierarchical RL, GRPO, code generation, self-correction, mathematical reasoning  

## 一句话总结
提出 THOR（Tool-Integrated Hierarchical Optimization via RL），通过三个互补组件系统性解决 LLM 工具集成数学推理中的核心挑战：TIRGen 数据构建管线生成策略对齐的 TIR 训练数据、层次化强化学习（episode 级解题+step 级代码修正）缓解稀疏奖励、自修正推理机制利用工具反馈在线纠错。在 MATH500、AIME 等多个数学基准上达到同规模 SOTA，同时在代码生成基准上也有提升。

## 背景与动机
1. LLM 作为概率 next-token 预测器在高精度任务（数值计算、方程求解、符号操作、形式证明）上天然不足——概率采样导致的误差在多步计算中会累积
2. 工具集成推理（TIR）是克服此瓶颈的有力范式，但面临三大挑战：
   - **数据构建**: 用外部大模型（如 GPT-4o）prompt 合成数据存在风格不匹配，对推理模型（如 DeepSeek-R1）效果差；START 等规则注入方法位置选择不精准导致冗余
   - **细粒度优化**: 现有 RL 方法（Agent-R、ToRL、ReTool）仅做 episode 级优化，忽略中间代码步骤的细粒度更新——在长推理链中导致严重的稀疏奖励问题
   - **推理增强**: 单 pass 推理忽略了工具即时反馈的修正作用——代码执行失败时应该回溯修正而非继续
3. SFT 方法（Toolformer、AIMO-2）需大量高质量示范数据且泛化差
4. **关键洞察**：中间工具调用的执行成功是最终答案正确性的强预测因子——这为 step 级优化提供了天然的奖励信号

## 方法（框架/设计）
- **TIRGen 数据构建管线**:
  - Generator 生成自然语言推理步骤（限长 $L_{step}$）
  - Refiner 评估哪些步骤可转为代码，提取纯推理部分后转换为 Python 代码
  - 代码通过外部执行器运行，结果替换原始计算——保证精确性
  - 优势：(a) 数据与 Generator 策略对齐（Refiner 仅看单步不看全题），(b) 降低对大模型依赖（Refiner 只需基本指令跟随+代码能力）
  - 多阶段过滤：格式一致性 → 代码质量（需有 sympy/numpy 调用或控制流）→ 难度平衡（按代码调用次数分层采样）→ 排除纯 CoT 可解的简单题

- **层次化 RL 训练**:
  - **Cold Start**: 用 $\mathcal{D}_{SFT}$ 做 SFT 建立工具调用基础模式
  - **Episode 级优化**: GRPO + 最终答案正确性奖励（$\mathcal{R}=1$ 正确/$0$ 错误），过滤执行失败轨迹以避免不当惩罚
  - **Step 级优化**: 对执行失败的代码步进行回溯——保留推理前缀 $r_{pre}^t$，截取后缀 $r_{suf}^t$（长度 $L_{suf}$），重新生成后缀+代码动作；以代码执行成功率为步级奖励
  - 总损失: $\mathcal{L} = \mathcal{L}^{epis} + \mathcal{L}^{step}$，两级均采用 GRPO + VAPO 式 NLL 损失（正向样本额外强化）

- **自修正推理机制**: 推理时代码执行失败则回溯到推理前缀重新生成后缀和动作，最多修正 $N_{corr}$ 次，增量计算成本极小（仅重新生成 ~20% token）

## 实验关键数据

### 主实验（SOTA 比较）

| Benchmark | THOR 表现 | vs 此前 SOTA | 说明 |
|-----------|----------|-------------|------|
| MATH500 | **SOTA** | 超越同规模所有模型 | 核心数学推理基准 |
| AIME 2024 | **SOTA** | 竞赛级数学题 | 需精确数值计算 |
| AIME 2025 | **SOTA** | 最新竞赛题 | 验证泛化性 |
| AMC | **SOTA** | 美国数学竞赛 | 多难度级别 |
| Minerva Math | **SOTA** | 理工科数学 | 需符号运算 |
| Olympiad Bench | **SOTA** | 奥林匹克数学 | 最高难度 |
| HumanEval | 提升 | 代码生成也受益 | 验证代码能力正迁移 |
| MBPP | 提升 | 代码生成也受益 | |
| LiveCodeBench | 提升 | 实时代码评测 | |

## 亮点与洞察
- **三位一体框架**系统性解决 TIR 的数据/优化/推理三大挑战——每个组件可独立使用也可组合
- **TIRGen 的 Generator-Refiner 分工设计**最为巧妙：Generator 负责高层数学推理，Refiner 负责底层代码转换——分工使得数据质量不再受限于单一模型的能力
- **Step 级 RL 的回溯+重生成设计**精确瞄准代码错误步——不惩罚整条轨迹，而是对失败步骤重点优化，是对稀疏奖励问题的精巧解决方案
- **自修正机制几乎零额外成本**——仅重新生成 ~20% token（推理后缀+代码动作），不需要完整 rollout
- **数学推理+代码生成双赢**——在代码 benchmark 上的一致提升说明 step 级优化提升了通用代码能力，非仅限数学

## 消融实验与深入分析

| 组件 | 移除后影响 | 说明 |
|------|-----------|------|
| Step 级 RL | 显著下降 | 仅 episode RL 无法有效优化中间代码步骤 |
| 自修正推理 | 中等下降 | 执行失败时无法回溯探索替代路径 |
| TIRGen（用 prompt 替代） | 明显下降 | 直接 prompt 生成的 TIR 数据与策略模型不对齐 |
| VAPO 式 NLL 损失 | 轻微下降 | 正向样本的额外强化有辅助作用 |

### 关键洞察验证
- **"中间工具调用成功 ↔ 最终答案正确"统计验证**：代码执行全部成功的轨迹最终答案正确率约 85%，而有执行失败的轨迹仅约 40%
- **回溯重生成的效率**：自修正仅重新生成推理后缀和代码动作（~20% token），相比完整重采样节省 ~80% 推理成本
- **跨模型泛化**：TIRGen 在推理模型（DeepSeek-R1）和非推理模型上都能生成高质量 TIR 数据
- **代码能力正迁移**：数学 benchmark 上的 step 级代码优化同时提升了 HumanEval、MBPP 等纯代码任务的性能

## 局限性 / 可改进方向
- Step 级优化依赖代码执行是否成功作为信号，对逻辑正确但因环境问题执行报错的情况可能产生误判——过滤机制部分缓解但不完美
- 回溯机制的 $L_{suf}$（后缀长度）和 $N_{corr}$（最大修正次数）需调参，论文未讨论超参数敏感性
- TIRGen 的 Refiner 仍需具备一定代码能力的模型，在极弱模型（如 <1B 参数）上的适用性未验证
- 仅关注数学推理，未验证在其他工具使用场景（如搜索、API 调用）的推广性
- 层次化 RL 的两级优化增加了训练复杂度和超参数空间

## 相关工作与启发
- **vs ToRA (Gou et al.)**：ToRA 用 GPT-4 直接 prompt 合成 TIR 数据，风格不匹配；THOR 的 TIRGen 通过 Generator-Refiner 协作保持策略对齐。ToRA 还需要大量 GPT-4 API 调用，成本高。
- **vs START (Li et al.)**：START 用规则注入代码 prompt 到长 CoT 中，位置选择不精准导致冗余；TIRGen 由 Refiner 智能判断。START 也不适用于非推理模型。
- **vs ToRL/ReTool (RL-based TIR)**：它们仅做 episode 级 RL，THOR 增加了 step 级优化——在长推理链（>10 步工具调用）中差距尤为明显
- **vs VAPO/DAPO (数学 RL)**：纯 CoT RL 方法不集成工具；THOR 将工具调用纳入 RL 优化。纯 CoT 在精确数值计算上有天然瓶颈。
- **vs Toolformer/AIMO-2 (SFT)**：SFT 方法需要大量高质量标注数据且泛化差；THOR 的 RL 方法更具可扩展性
- **启发**：TIRGen 的 Generator-Refiner 解耦设计可迁移到其他工具学习场景——如搜索增强生成（RAG）中，一个模型负责推理、另一个负责查询构造

## 评分
- 新颖性: ⭐⭐⭐⭐ 层次化 RL 和 TIRGen 管线均有创新
- 实验充分度: ⭐⭐⭐⭐ 多 benchmark SOTA，跨模型架构验证
- 写作质量: ⭐⭐⭐⭐ 形式化严谨，算法描述详尽
- 价值: ⭐⭐⭐⭐⭐ TIR 领域的系统性贡献，三个挑战的解决方案可独立使用
