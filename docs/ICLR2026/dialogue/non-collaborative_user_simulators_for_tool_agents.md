---
title: >-
  [论文解读] Non-Collaborative User Simulators for Tool Agents
description: >-
  [ICLR 2026][用户模拟器] 提出四类非协作用户行为模拟框架（不可用服务/跑题/不耐烦/不完整表述），在MultiWOZ和τ-bench上揭示SOTA工具Agent在面对非协作用户时性能显著下降（平均-29% tangential模式），暴露了幻觉增加和对话崩溃的系统性弱点。
tags:
  - ICLR 2026
  - 用户模拟器
  - 工具使用Agent
  - 非协作行为
  - 鲁棒性测试
  - 对话系统
---

# Non-Collaborative User Simulators for Tool Agents

**会议**: ICLR 2026  
**arXiv**: [2509.23124](https://arxiv.org/abs/2509.23124)  
**代码**: https://github.com/holi-lab/NCUser  
**领域**: 其他 / LLM Agent评测  
**关键词**: 用户模拟器, 工具使用Agent, 非协作行为, 鲁棒性测试, 对话系统

## 一句话总结
提出四类非协作用户行为模拟框架（不可用服务/跑题/不耐烦/不完整表述），在MultiWOZ和τ-bench上揭示SOTA工具Agent在面对非协作用户时性能显著下降（平均-29% tangential模式），暴露了幻觉增加和对话崩溃的系统性弱点。

## 研究背景与动机
工具Agent通过多轮对话理解用户请求、执行API调用、返回结果。现有用户模拟器只模拟协作行为——用户总是清晰、耐心、配合地表达需求。但真实世界中用户经常表现出非协作行为：请求超出能力范围的服务、闲聊跑题、因延迟表达不满、发送不完整信息。这些行为在marketing和客服研究中已有大量记录，却从未被系统性地引入Agent评测。

现有训练和评测的空白导致Agent在部署时面对真实用户行为束手无策。特别是小模型(GPT-4.1-nano)在非协作场景下性能扑街：tangential模式下成功率仅为协作模式的41.5%。

## 方法详解

### 整体框架
(1) 基于marketing研究定义4类非协作行为 → (2) 设计保持goal-alignment的模拟架构 → (3) 在MultiWOZ/τ-bench上系统评测。

### 关键设计

1. **四类非协作行为**：
   - Unavailable Service：请求超出API能力的服务（如"预订靠窗座位"但API无此参数）
   - Tangential：插入无关闲聊，被忽略时还会抱怨
   - Impatience：因延迟或失败表现出越来越强的愤怒（belligerent abuse/threat/urge三级升级）
   - Incomplete Utterances：极简表述("Book train, 2")或意外截断("I want to res")

2. **Goal-Aligned Simulation**：在非协作行为下仍须传达所有必要intent和信息。通过 dialogue state tracker 监控已传达信息 + ending verifier 防止过早终止。

3. **实现方式**：各类行为通过对协作用户模拟器的不同干预实现。Unavailable通过GPT生成额外goal sentences；Tangential用Persona Hub采样人设后合并闲聊；Impatience概率递增激活；Incomplete通过风格迁移或随机截断。

### 损失函数 / 训练策略
无训练。使用GPT-4.1-mini作为用户模拟器。Agent侧使用ReAct框架，30步推理限制。

## 实验关键数据

### 主实验 (MultiWOZ / τ-bench)
| 模型 | Collab SR | Unavail. SR | Tang. SR | Impat. SR | Incomp. SR |
|------|----------|------------|---------|----------|-----------|
| GPT-4.1-mini | 92.7/45.5 | 89.3/41.7 | 89.3/39.5 | 90.7/45.1 | 88.2/45.4 |
| GPT-4.1-nano | 23.6/12.0 | 16.9/10.0 | **9.8/6.8** | 26.7/8.8 | 14.7/8.0 |
| Qwen3-235b | 77.8/41.4 | 62.4/36.8 | 57.3/32.3 | 69.4/37.6 | 69.9/39.3 |

### 消融实验
| 模式 | 平均相对SR降幅 | 主要失败机制 |
|------|-------------|------------|
| Tangential | **-29.1%** | Agent被闲聊分散注意力，遗漏核心任务 |
| Unavailable | -11.3% | Agent反复调用helper API陷入循环 |
| Impatience | -12.4% | Agent在愤怒言论中耗尽推理步骤 |
| Incomplete | -16.5% | Agent对截断信息产生幻觉 |

### 关键发现
- **Tangential是最致命的非协作行为**——Agent被闲聊拉跑后难以回到正轨。
- GPT-4.1-nano在tangential下性能暴跌至9.8%，因为它回应闲聊的能力最差→触发最多用户抱怨→消耗推理预算。
- Qwen3-235b在unavailable模式下出现API结果幻觉（而非重复调用helper API）——不同模型的失败模式不同。
- 小模型在协作数据上fine-tuning后，非协作场景的改善显著落后于协作场景——仅训练协作数据不够。

## 亮点与洞察
- 首个系统性的非协作用户模拟框架，填补了Agent鲁棒性评测的重要空白。
- 揭示了"协作偏见"：现有Agent仅在理想用户下工作良好，部署后表现可能远低于预期。
- 框架具有扩展性——已成功推广到ColBench（无工具使用）和MINT（用户-Agent协作）。

## 局限性 / 可改进方向
- 非协作行为的定义源自西方marketing研究，跨文化适用性待验证。
- 使用GPT-4.1-mini生成的非协作行为本身可能不够自然。
- 如何训练Agent应对非协作行为的方法论尚未深入探索。

## 相关工作与启发
- 与τ-bench (Yao et al., 2024) 互补，扩展了评测维度。
- 为Agent部署前的压力测试提供了标准化工具。

## 评分
- 新颖性: ⭐⭐⭐⭐ 首个系统性非协作用户模拟
- 实验充分度: ⭐⭐⭐⭐⭐ 多模型+多基准+详细错误分析
- 写作质量: ⭐⭐⭐⭐ 结构清晰
- 价值: ⭐⭐⭐⭐ Agent鲁棒性评测的重要贡献
