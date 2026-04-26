---
title: >-
  [论文解读] AutoTool: Automatic Scaling of Tool-Use Capabilities in RL via Decoupled Entropy Constraints
description: >-
  [ICLR 2026][工具使用] 本文提出 AutoTool，通过解耦自适应熵约束策略解决 LLM 工具使用中直接 RL 训练的推理坍缩问题和缩放后模型的过度思考问题，实现自动根据问题难度切换长短推理模式，在准确率提升 9.8% 的同时减少 ~81% 的推理 token 开销。
tags:
  - ICLR 2026
  - 工具使用
  - 强化学习
  - 测试时扩展
  - 熵约束
  - 自动推理缩放
---

# AutoTool: Automatic Scaling of Tool-Use Capabilities in RL via Decoupled Entropy Constraints

**会议**: ICLR 2026  
**arXiv**: [2603.13348](https://arxiv.org/abs/2603.13348)  
**代码**: 无  
**领域**: LLM Agent  
**关键词**: 工具使用, 强化学习, 测试时扩展, 熵约束, 自动推理缩放

## 一句话总结
本文提出 AutoTool，通过解耦自适应熵约束策略解决 LLM 工具使用中直接 RL 训练的推理坍缩问题和缩放后模型的过度思考问题，实现自动根据问题难度切换长短推理模式，在准确率提升 9.8% 的同时减少 ~81% 的推理 token 开销。

## 研究背景与动机

1. **领域现状**: LLM 与外部工具的集成是 AI agent 的关键能力。RLVR（带可验证奖励的强化学习）在数学和代码任务上成功实现了测试时扩展，但在工具使用中尚未验证。

2. **现有痛点**: (1) 直接 RL 训练在工具使用中出现"推理坍缩"——模型无法充分延长思考长度解决复杂问题；(2) 蒸馏模型对所有问题都生成冗长推理，简单问题浪费大量 token。

3. **核心矛盾**: 数学任务中 RL 训练会自然增长推理长度，但工具使用任务中推理长度反而缩短。根因是低熵导致模型过早收敛到短推理策略。

4. **本文目标**: 设计能自动根据问题难度选择推理模式的训练方法，复杂问题长思考、简单问题直接回答。

5. **切入角度**: 发现低信息熵与推理坍缩强正相关，但简单的熵约束对系数极其敏感。

6. **核心 idea**: 解耦长短推理的策略损失，对长推理施加自适应熵约束保持探索能力，对短推理保持固定约束防止过度探索。

## 方法详解

### 整体框架
三阶段流程：(1) 数据准备——构建 PubTool 混合数据集；(2) 预热 SFT——混合长短推理数据让模型感知难度；(3) 解耦自适应熵约束 RL——GRPO + 解耦熵正则化。

### 关键设计

1. **预热 SFT 与混合推理数据**:
    - 功能: 让模型初步感知问题难度
    - 核心思路: 对训练数据用无思考模型（Qwen2.5-7B-Instruct）和思考模型（Qwen3-32B）分别推理 8 次。无思考模型正确则用短推理作为标签，否则用思考模型的长推理。设计 auto-thinking 模板支持模式切换
    - 设计动机: 直接 RL 训练会坍缩，需要 SFT 预热建立初始的长短推理能力

2. **解耦自适应熵约束**:
    - 功能: 差异化控制长短推理的探索能力
    - 核心思路: 策略损失 $\mathcal{L}_p$ 中的熵系数 $\beta_i$ 根据推理模式解耦：短推理用固定 $\beta_s$，长推理用自适应 $\beta_l$。$\beta_l$ 通过辅助损失 $\mathcal{L}_\beta^l = \frac{1}{N}\sum (1-m_i)\cdot\beta_l\cdot(H_i - H_l)$ 动态调整，当 $H_i < H_l$ 时增大以鼓励探索
    - 设计动机: 直接RL中低熵→推理坍缩；但全局高熵又导致简单问题过度探索

3. **非对称奖励设计**:
    - 功能: 鼓励简单问题用短推理、复杂问题用长推理
    - 核心思路: 正确+不思考: +1.0, 正确+思考: +0.5, 错误+思考: -0.5, 错误+不思考: -1.0
    - 设计动机: 对短推理正确给予更高奖励（效率）；对短推理错误给予更重惩罚（鼓励思考）

### 损失函数 / 训练策略
- 基座模型：Qwen2.5-7B-Instruct
- RL 算法：GRPO
- 数据：PubTool（8.2k SFT + 7k RL），来自 ToolACE + xLAM + Hermes
- 数据质量优化：去除极简单/极难样本，基于多轮训练奖励方差筛选

## 实验关键数据

### 主实验

| 模型 | BFCL Overall | Non-Live | Live | Multi-Turn |
|------|-------------|----------|------|-----------|
| Qwen2.5-7B (Base) | 53.69 | 86.46 | 67.44 | 7.62 |
| PubTool-SFT | 58.17 | 88.98 | 77.28 | 9.68 |
| PubTool-Distilled | 60.30 | 87.73 | 78.64 | 15.65 |
| **AutoTool-7B** | **70.12** | **89.76** | **80.22** | **38.18** |
| GPT-4o | 70.42 | 87.67 | 79.88 | 43.00 |

### 消融实验

| 配置 | Overall | 变化 |
|------|---------|------|
| 完整方法 | 70.12 | - |
| w/o data refine | 63.69 | -6.43 |
| w/o decouple | 64.23 | -5.89 |
| w/o adapt coeff | 67.78 | -2.34 |

### 关键发现
- Multi-Turn 场景 thinking rate 达 45%，Non-Live 场景为 0%——模型学会了自动判断难度
- 复杂问题推理轨迹延长 5 倍，简单问题保持简洁
- 数据质量优化是最关键组件（移除后 -6.43%）
- AutoTool-7B 在 BFCL 上逼近 GPT-4o（70.12 vs 70.42）

## 亮点与洞察
- 首次揭示并解决工具使用 RL 训练中的"推理坍缩"现象
- 通过信息熵视角理解坍缩机制，发现与数据难度分布无关而与熵强正相关
- 非对称奖励设计巧妙地编码了效率偏好
- 7B 模型超越多数 SFT/RLVR 同规模模型，逼近前沿模型

## 局限与展望
- 仅验证在工具使用场景，未扩展到其他 agent 任务
- 预热 SFT 阶段依赖外部推理模型（Qwen3-32B）生成长推理数据
- 自适应熵约束的目标熵值仍需预设
- 数据来源为公开数据集混合，未验证在特定领域工具上的效果

## 相关工作与启发
- **vs DeepSeek-R1**: R1 在数学/代码上扩展推理成功，但在工具使用中面临坍缩
- **vs Thinkless**: Thinkless 也做推理模式切换，但用 SFT 蒸馏而非 RL
- **vs AdaCtrl**: AdaCtrl 做自适应推理控制，AutoTool 通过解耦熵约束实现更好的自动化

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 推理坍缩现象的发现和解耦熵约束方案是重要贡献
- 实验充分度: ⭐⭐⭐⭐ 3 个基准、多个基线、详细消融
- 写作质量: ⭐⭐⭐⭐ 预分析→发现→方法的逻辑链清晰
- 价值: ⭐⭐⭐⭐⭐ 对 LLM agent 训练实践有直接指导意义

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning](cuda-l1_improving_cuda_optimization_via_contrastive_reinforcement_learning.md)
- [\[ICLR 2026\] Don't Just Fine-tune the Agent, Tune the Environment](dont_just_fine-tune_the_agent_tune_the_environment.md)
- [\[ICLR 2026\] ReMoT: Reinforcement Learning with Motion Contrast Triplets](remot_reinforcement_learning_with_motion_contrast_triplets.md)
- [\[ICLR 2026\] Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning](echo_towards_advanced_audio_comprehension_via_audio-interleaved_reasoning.md)
- [\[ICLR 2026\] RLP: Reinforcement as a Pretraining Objective](rlp_reinforcement_as_a_pretraining_objective.md)

<!-- RELATED:END -->
