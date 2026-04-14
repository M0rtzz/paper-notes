---
title: >-
  [论文解读] RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation
description: >-
  [ICLR 2026][机器人][中间表示] 提出RoboInter操作套件——统一的中间表示数据/基准/模型资源：RoboInter-Tool(半自动标注GUI)+RoboInter-Data(23万episode×571场景×10+类中间表示的密集逐帧标注)+RoboInter-VQA(29类具身VQA基准)+RoboInter-VLA(支持模块化和端到端的plan-then-execute框架)，为通过中间表示提升VLA泛化提供完整基础设施。
tags:
  - ICLR 2026
  - 机器人
  - 中间表示
  - VLA
  - 操作数据集
  - 具身VQA
  - plan-then-execute
---

# RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation

**会议**: ICLR 2026  
**arXiv**: [2602.09973](https://arxiv.org/abs/2602.09973)  
**代码**: [GitHub](https://github.com/RoboInter)  
**领域**: 机器人学习/数据集  
**关键词**: 中间表示, VLA, 操作数据集, 具身VQA, plan-then-execute

## 一句话总结
提出RoboInter操作套件——统一的中间表示数据/基准/模型资源：RoboInter-Tool(半自动标注GUI)+RoboInter-Data(23万episode×571场景×10+类中间表示的密集逐帧标注)+RoboInter-VQA(29类具身VQA基准)+RoboInter-VLA(支持模块化和端到端的plan-then-execute框架)，为通过中间表示提升VLA泛化提供完整基础设施。

## 研究背景与动机

**领域现状**：VLA(Vision-Language-Action)通过大规模预训练+端到端训练→但现有机器人数据集成本高、embodiment特异、覆盖不足。Plan-then-execute范式(先高层规划再低层执行)需要中间表示监督→但现有数据集缺乏。

**现有痛点**：
   - (1) 中间表示标注几乎不存在→限制plan-then-execute方法的发展
   - (2) 现有数据集要么小规模要么标注类型单一
   - (3) 缺乏评估VLM在具身场景中推理能力的基准
   - (4) 模块化 vs 端到端VLA缺乏统一框架比较

**切入角度**：提供完整的中间表示生态：标注工具→数据→基准→模型框架。

## 方法详解

### 四大组件

1. **RoboInter-Tool**：
    - 轻量GUI→半自动标注多种中间表示
    - 支持：子任务/技能/可供性/接触点/抓取框/物体框/轨迹trace等10+类

2. **RoboInter-Data**：
    - 23万+episode × 571场景
    - 主要来源：DROID + RH20T
    - 密集逐帧标注(不是稀疏的)→每帧都有中间表示
    - 10+类标注(比先前任何数据集都多)
    - 支持端到端动作对齐(E2E-ACT)

3. **RoboInter-VQA**：
    - 9类空间+20类时间的具身VQA
    - 空间：物体定位/空间关系/可供性/接触分析
    - 时间：子任务分解/动作序列/因果推断
    - 系统性评估VLM的具身推理

4. **RoboInter-VLA**：
    - 统一的plan-then-execute框架
    - 模块化变体：VLM规划→策略执行
    - 端到端变体：联合训练→中间表示作为中间监督
    - 支持CoT(chain-of-thought)式的多步中间表示

## 实验关键数据

### VQA基准测试
| VLM | 空间准确率 | 时间准确率 | 说明 |
|-----|---------|---------|------|
| GPT-4V | ~60% | ~50% | 通用VLM |
| Qwen-VL | ~55% | ~45% | 开源VLM |
| **RoboInter微调** | **~75%** | **~65%** | 显著提升 |

### VLA实验
| 方法 | 成功率 | 说明 |
|------|--------|------|
| 端到端(无中间) | 基线 | 直接预测动作 |
| +子任务监督 | +5% | 单一中间表示 |
| **+全中间表示** | **+12%** | 多种中间表示协同 |

### 关键发现
- 密集逐帧标注比稀疏标注更有效→信息更丰富
- 多种中间表示的组合比单一类型好→不同表示提供互补信息
- 端到端+中间监督 > 纯模块化→减少误差传递
- 现有VLM在具身时间推理上显著弱于空间推理

## 亮点与洞察
- **"基础设施级贡献"**：不只是数据集→工具+数据+基准+框架=完整生态→降低后续研究的门槛。
- **中间表示的"越多越好"**：之前通常用一种(如子任务或trace)→RoboInter证明多种协同效果更好。
- **密集vs稀疏标注的区别**：逐帧标注工程量大→但RoboInter-Tool半自动化降低了成本→使大规模密集标注可行。
- **Plan-then-Execute的统一视角**：将模块化和端到端纳入同一框架→公平比较→发现端到端+中间监督组合最优。

## 评分
- 新颖性: ⭐⭐⭐⭐ 规模和覆盖度的飞跃+完整生态
- 实验充分度: ⭐⭐⭐⭐⭐ VQA基准+VLA实验+消融+多数据源
- 写作质量: ⭐⭐⭐⭐ 系统性强
- 价值: ⭐⭐⭐⭐⭐ 对机器人学习社区有基础设施级贡献
