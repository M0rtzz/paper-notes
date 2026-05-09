---
title: >-
  [论文解读] DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-Level Control
description: >-
  [ECCV 2024][机器人][Embodied Instruction Following] 提出 DISCO，通过可微分场景语义表征（包含物体和 affordance）实现动态场景建模，结合全局-局部双层粗到细控制策略实现高效移动操作，在 ALFRED benchmark 的 unseen scenes 上以 +8.6% 成功率超越使用分步指令的 SOTA，且无需分步指令。
tags:
  - ECCV 2024
  - 机器人
  - Embodied Instruction Following
  - Differentiable Scene Representation
  - Dual-level Control
  - Mobile Manipulation
  - ALFRED
---

# DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-Level Control

**会议**: ECCV 2024  
**arXiv**: [2407.14758](https://arxiv.org/abs/2407.14758)  
**代码**: [https://github.com/AllenXuuu/DISCO](https://github.com/AllenXuuu/DISCO)  
**领域**: 机器人  
**关键词**: Embodied Instruction Following, Differentiable Scene Representation, Dual-level Control, Mobile Manipulation, ALFRED

## 一句话总结

提出 DISCO，通过可微分场景语义表征（包含物体和 affordance）实现动态场景建模，结合全局-局部双层粗到细控制策略实现高效移动操作，在 ALFRED benchmark 的 unseen scenes 上以 +8.6% 成功率超越使用分步指令的 SOTA，且无需分步指令。

## 研究背景与动机

1. **领域现状**：室内具身智能体执行家务任务（如拿、放、开关）是具身 AI 的长期目标，ALFRED benchmark 是该领域的核心测试平台，要求智能体根据语言指令完成长序列导航-交互任务。
2. **现有痛点**：Neural policy 方法需要大量训练轨迹且缺乏长程记忆；Map-based planning 方法缺乏灵活性且难以自适应运行时变化。离散化场景表示（cell-based）不够鲁棒，需要手工规则修复感知错误。
3. **核心矛盾**：要高效完成移动操作任务，需要同时具备对全局场景的理解（知道物体在哪）和对局部状态的精细控制（如何操作物体），但现有方法难以兼顾。
4. **本文要解决什么**：构建能在动态场景中高效导航和交互的具身智能体，无需分步指令也能完成复杂长序列任务。
5. **切入角度**：可微分场景表征（动态、可查询、富语义）+ 粗到细双层控制（地图驱动粗导航 + 神经网络精细操作）。
6. **核心 idea 一句话**：用梯度下降动态优化场景语义表征实现鲁棒的全局规划，再用短序列神经策略进行局部精细操作。

## 方法详解

### 整体框架

DISCO 从自我中心 RGB 帧出发：(1) 感知系统预测深度、实例分割和 affordance；(2) 语义点云投影到场景表征并用梯度下降优化；(3) 粗控制基于语义地图导航接近目标；(4) 细控制用神经策略精调姿态并执行交互。

### 关键设计

1. **Perception System（感知系统）**
    - **做什么**：从自我中心 RGB 帧预测深度、实例分割（85 类）和 affordance（1 导航类 + 7 交互类）。
    - **核心思路**：Mask R-CNN 做实例分割（COCO 预训练 + 微调），两个 U-Net 分别估计深度（50 bins × 10cm）和 affordance。数据从 AI2THOR 模拟器收集。
    - **设计动机**：affordance 编码了"哪些区域可导航"、"哪些物体可拾取/打开"，直接指导规划。

2. **Differentiable Scene Representations（可微分场景表征）**
    - **做什么**：用连续特征建模 20m×20m 场景，支持语义查询和动态更新。
    - **核心思路**：场景离散化为 80×80 个 25cm 网格，每个网格一个 256 维 embedding $s_i$。初始化 $N^o + N^a$ 个语义查询 $q_j$。通过 $p_{i,j} = \sigma(s_i^T q_j)$ 查询任意位置的任意语义概率。每步将感知结果投影为语义点云，用交叉熵损失对可见网格梯度下降更新 $s_i$ 和 $q_j$（10 次迭代，lr=0.01）。
    - **设计动机**：连续特征比离散 cell 更鲁棒；梯度优化比匹配更新更灵活；动态更新处理交互后的场景变化。

3. **Coarse Control（粗控制）**
    - **做什么**：基于全局语义地图导航接近目标物体。
    - **核心思路**：查询 object 和 affordance 分布，选择物体-affordance 乘积概率最大的网格作为目标。扩展目标位置 1m 范围内的网格为 destination，用 BFS 在导航可达地图上规划路径。
    - **设计动机**：地图级规划高效处理长距离导航，避免神经策略在长序列上的训练困难。

4. **Fine Control（细控制）**
    - **做什么**：用神经策略精调智能体姿态并执行物体交互。
    - **核心思路**：状态为 $(o, x, z, h)$（目标物体、位置、相机仰角）。输入为 RGB + 估计深度 + 目标物体 mask 的拼接，用 ResNet50 编码特征，后接物体类别特定的分类器预测动作。仅在距交互 4 步内的短序列上训练，316,935 帧数据。
    - **设计动机**：先旋转到目标可见方向减少控制歧义；短序列策略比长序列更容易训练且数据高效。

### 损失函数 / 训练策略

- **场景表征**：交叉熵损失 $L(y_i^j, f(s_i, q_j)) = -(1-y_i^j)(1-f(s_i, q_j)) - y_i^j f(s_i, q_j)$
- **感知模块**：Mask R-CNN 默认损失 + 深度 CE 损失 + Affordance binary CE 损失
- **细控制策略**：行为克隆 (CE loss)，AdamW lr=5e-5，40 epochs，batch 100
- **自指令规划**：用微调 BERT 解析语言指令为 ALFRED 内部参数，模板转换为 verb-noun 子任务序列

## 实验关键数据

### 主实验

ALFRED Test 数据集结果：

| 方法 | 分步指令 | Test Seen SR↑ | Test Unseen SR↑ |
|------|---------|--------------|----------------|
| FILM | ✔ | 27.7 | 26.5 |
| LGS-RPA | ✔ | 40.1 | 35.4 |
| Prompter | ✔ | 53.2 | 45.7 |
| CAPEAM | ✔ | 51.8 | 46.1 |
| **DISCO** | **✔** | **59.5** | **56.5** |
| Prompter | ✗ | 49.4 | 42.6 |
| CAPEAM | ✗ | 47.4 | 43.7 |
| **DISCO** | **✗** | **58.0** | **54.7** |

**关键数字**：DISCO 无分步指令的 SR (54.7%) 超过了所有有分步指令的 SOTA (46.1%)！

### 消融实验

消融分析（Valid splits）：

| 设置 | Valid Seen SR | Valid Unseen SR |
|------|-------------|----------------|
| DISCO (默认，无分步指令) | 57.3 | 55.0 |
| + 分步指令 | 65.1 | 59.1 |
| + gt. lang. | 70.5 | - |

### 关键发现

- DISCO 在 unseen scenes 上成功率 56.5%，比 SOTA 高 10.4%
- 无分步指令比有分步指令的 SOTA 还高 8.6%，证明不依赖精细指令也能出色完成任务
- PLWSR 几乎是 Prompter 的 1.75 倍，说明 DISCO 执行步骤更少更高效
- 可微分场景表征比传统 cell-based 更鲁棒，无需手工规则修复

## 亮点与洞察

- **突破性能**：无分步指令超过有分步指令的 SOTA，证明好的场景理解比精细指令更重要
- **可微分场景表征设计精巧**：zero 初始化 + 梯度更新 + 语义查询的组合简洁有效
- **双层控制范式**：粗控制解决导航，细控制解决操作，各取所长
- **Affordance 的价值**：导航可达性 + 可交互性信息直接融入场景表征

## 局限性 / 可改进方向

- 感知模块依赖 AI2THOR 模拟器的 ground truth 训练，sim-to-real 转移困难
- 80×80 的场景表征分辨率有限，大规模环境需要更高效的表示
- 细控制仅在 4 步范围内训练，极端情况可能需要更长序列
- 语言理解依赖 BERT 模板匹配而非端到端方式

## 相关工作与启发

- 相比 FILM（经典 map-based 方法），DISCO 用可微分表征替代离散地图是关键升级
- Prompter 使用 LLM prompt 辅助规划，而 DISCO 完全不依赖 LLM 也能超越
- 可微分场景表征的思想可以推广到其他需要动态场景建模的机器人任务
- 启发：粗到细的控制层级 + 动态场景表征 + affordance = 高效移动操作

## 评分

- ⭐⭐⭐⭐ 新颖性：可微分场景表征和双层控制的组合新颖，但各组件独立来看非全新
- ⭐⭐⭐⭐⭐ 实验充分度：在 ALFRED 全面对标 13+ baseline，两种指令设置，消融详尽
- ⭐⭐⭐⭐ 写作质量：框架图清晰，方法阐述系统
- ⭐⭐⭐⭐⭐ 价值：ALFRED 上 10%+ 的 SR 提升是极其显著的进步，无指令超过有指令 SOTA 具有重要意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Octopus: Embodied Vision-Language Programmer from Environmental Feedback](octopus_embodied_visionlanguage_programmer_from_environmental_feedback.md)
- [\[ECCV 2024\] AFF-ttention! Affordances and Attention models for Short-Term Object Interaction Anticipation](aff-ttention_affordances_and_attention_models_for_short-term_object_interaction_.md)
- [\[ECCV 2024\] See and Think: Embodied Agent in Virtual Environment](see_and_think_embodied_agent_in_virtual_environment.md)
- [\[ECCV 2024\] ReALFRED: An Embodied Instruction Following Benchmark in Photo-Realistic Environments](realfred_an_embodied_instruction_following_benchmark_in_photo-realistic_environm.md)
- [\[ECCV 2024\] Prioritized Semantic Learning for Zero-Shot Instance Navigation](prioritized_semantic_learning_for_zeroshot_instance_navigation.md)

</div>

<!-- RELATED:END -->
