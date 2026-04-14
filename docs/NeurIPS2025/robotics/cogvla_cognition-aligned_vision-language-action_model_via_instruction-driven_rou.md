---
title: >-
  [论文解读] CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification
description: >-
  [NeurIPS 2025][机器人][VLA] 提出 CogVLA——模仿人类多模态认知的三阶段 VLA 架构：(1) EFA-Routing 将视觉 token 压缩至 25%；(2) LFP-Routing 裁剪 50% 的 LLM 无关 token；(3) V-L-A 耦合注意力保持语义一致性——在 LIBERO 上达 97.4% 成功率，训练成本降 2.5×，推理延迟降 2.8×。
tags:
  - NeurIPS 2025
  - 机器人
  - VLA
  - token routing
  - sparsification
  - instruction-driven
  - robotic manipulation
---

# CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification

**会议**: NeurIPS 2025  
**arXiv**: [2508.21046](https://arxiv.org/abs/2508.21046)  
**代码**: 无（论文中未提及）  
**领域**: 机器人 / 多模态VLM  
**关键词**: VLA, token routing, sparsification, instruction-driven, robotic manipulation

## 一句话总结
提出 CogVLA——模仿人类多模态认知的三阶段 VLA 架构：(1) EFA-Routing 将视觉 token 压缩至 25%；(2) LFP-Routing 裁剪 50% 的 LLM 无关 token；(3) V-L-A 耦合注意力保持语义一致性——在 LIBERO 上达 97.4% 成功率，训练成本降 2.5×，推理延迟降 2.8×。

## 研究背景与动机

**领域现状**：VLA 模型（OpenVLA、π₀）将视觉+语言+动作统一在单一模型中进行机器人控制。但大量视觉 token 和 dense LLM 计算导致训练和推理成本高昂。

**现有痛点**：(a) OpenVLA 等方法所有视觉 token 同等处理，但大多数与任务指令无关；(b) LLM 的所有 token 都参与计算，但许多与动作生成无关；(c) 视觉-语言-动作三模态的注意力模式应不同但被统一处理。

**切入角度**：模仿人类认知——先选择性注意（视觉过滤）→ 重点处理（LLM 稀疏化）→ 协调执行（耦合注意力），三阶段渐进式信息压缩。

## 方法详解

### 三阶段架构

1. **Stage 1 - EFA-Routing（Early Feature Aggregation）**:
    - 功能：基于指令引导聚合视觉 token，压缩至 25%
    - 机制：指令 embedding 作为 query，视觉 token 作为 key/value，聚合出最相关的 1/4

2. **Stage 2 - LFP-Routing（LLM Feature Pruning）**:
    - 功能：在 LLM 中用指令感知的稀疏模式裁剪 50% 不相关 token
    - 保留与动作生成最相关的 token 进入深层

3. **Stage 3 - V-L-A Coupled Attention**:
    - 视觉-语言部分：因果注意力（保持序列一致性）
    - 动作部分：双向注意力（保持时间连贯性）
    - 分层注意力确保不同模态用不同模式处理

## 实验关键数据

| 指标 | CogVLA | OpenVLA | 说明 |
|------|--------|---------|------|
| LIBERO 成功率 | **97.4%** | 90.2% | +7.2% |
| 真实机器人成功率 | **70.0%** | - | - |
| 训练成本 | **2.5×** 降低 | 基线 | - |
| 推理延迟 | **2.8×** 降低 | 基线 | - |

### 关键发现
- **75% 视觉 token 可以裁剪**：大多数视觉信息与任务无关
- **50% LLM token 可以稀疏化**：指令引导的裁剪比随机裁剪好得多
- **三个组件协同效应**：消融显示每个阶段都有贡献，组合效果 > 各自之和

## 亮点与洞察
- **认知启发的架构设计**：从人类注意力机制出发——选择性注意→重点处理→协调执行——不是暴力压缩而是有理论依据的稀疏化
- **指令驱动路由**：不是盲目压缩视觉/文本 token，而是根据任务指令选择保留什么——做到了"task-aware compression"
- **效率提升巨大**：2.5× 训练 + 2.8× 推理加速——使 VLA 的实际部署更加可行

## 局限性 / 可改进方向
- 仅在 LIBERO 和少量真实任务上验证
- 路由策略是预定义规则，非端到端学习
- **改进方向**：(1) 自适应压缩率（不同任务不同压缩）；(2) 扩展到更复杂的操作任务

## 评分
- 新颖性: ⭐⭐⭐⭐ 认知启发的三阶段压缩设计有创意
- 实验充分度: ⭐⭐⭐⭐ LIBERO+真实机器人+消融
- 写作质量: ⭐⭐⭐⭐ 架构描述清晰
- 价值: ⭐⭐⭐⭐ 对 VLA 的高效部署有直接实用价值
