---
title: >-
  [论文解读] Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols
description: >-
  [CVPR 2026][机器人][失败诊断] 提出 ViFailback 框架，利用显式视觉符号（箭头、准星等）高效标注真实世界机器人操作失败数据，构建 58,128 条 VQA 对的大规模数据集，并微调得到 ViFailback-8B 模型，在真实机器人实验中结合 VLA 模型实现失败恢复，平均成功率提升 22.2%。
tags:
  - CVPR 2026
  - 机器人
  - 失败诊断
  - 视觉语言模型
  - 机器人操作
  - 视觉符号
  - VLA
---

# Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols

**会议**: CVPR 2026  
**arXiv**: [2512.02787](https://arxiv.org/abs/2512.02787)  
**代码**: [项目主页](https://github.com/)  
**领域**: Robotics / 机器人操作  
**关键词**: 失败诊断, 视觉语言模型, 机器人操作, 视觉符号, VLA

## 一句话总结

提出 ViFailback 框架，利用显式视觉符号（箭头、准星等）高效标注真实世界机器人操作失败数据，构建 58,128 条 VQA 对的大规模数据集，并微调得到 ViFailback-8B 模型，在真实机器人实验中结合 VLA 模型实现失败恢复，平均成功率提升 22.2%。

## 研究背景与动机

Vision-Language-Action (VLA) 模型近年在机器人操作领域取得了显著进展，但在部署到真实世界时不可避免地会遇到分布外（OOD）场景，导致动作失败。现有方法面临几个核心问题：

1. **失败数据稀缺**：现有失败数据集大多在仿真环境中通过注入扰动程序化生成，受 sim-to-real gap 限制，难以迁移到真实场景
2. **标注效率低**：真实世界失败数据的标注需要大量人工文本描述，尤其是任务规划失败、失败原因等抽象类别
3. **反馈形式局限**：现有方法的修正反馈主要是文本形式，但当前 VLA 模型的指令跟随能力有限，纯文本指导难以有效指导机器人恢复

本文核心洞察：在遥操作数据采集或策略执行过程中，必然会产生大量失败数据，关键在于如何简单高效地标注这些数据并利用它们。

## 方法详解

### 整体框架

ViFailback 框架包含三个核心部分：
1. **数据标注框架**：基于视觉符号的高效半自动标注流水线
2. **ViFailback 数据集与基准**：58,128 条 VQA 对 + ViFailback-Bench 评测基准
3. **ViFailback-8B 模型**：微调 Qwen3-VL-8B，在 VLA 执行时作为外部监督者进行失败诊断与修正

### 关键设计

1. **视觉符号系统（7 种符号，3 大类）**：
    - **运动符号**：彩色直箭头（红=前后、绿=左右、蓝=上下 表示 3D 空间运动）、半圆箭头（表示末端执行器旋转方向）
    - **空间关系符号**：双准星（用虚线连接，表示两个目标需要对齐）、准星（标注目标物体或区域）
    - **状态符号**：ON/OFF 标签（末端执行器开/关状态）、禁止图标（末端执行器应停止）、倒带图标（回退到先前状态）
    - 设计动机：标注者只需用鼠标在视频帧上绘制这些符号，VLM 就能自动生成所需的文本标注，大幅降低标注成本

2. **细粒度任务定义**：将失败分析分解为两大组件：
    - **失败诊断**（5 项）：失败检测、关键帧定位、子任务定位、失败类型识别（任务规划/夹爪位姿/夹爪状态/人为干预 4 大类）、失败原因推理
    - **修正动作指导**（3 项）：低级文本指导（具体运动方向）、高级文本指导（任务计划重整）、视觉指导（在关键帧上叠加视觉符号）

3. **三阶段标注流水线**：
    - 阶段 1：基础语义信息填写（通过 UI 滑块和按钮完成失败诊断标注）
    - 阶段 2：基于选定关键帧，标注者选择修正动作类别并绘制视觉符号
    - 阶段 3：用 Qwen3-VL-235B 结合所有标注信息和视觉符号自动生成高级描述，再人工验证和修正

4. **ViFailback-Bench 基准**：包含 500 条轨迹、22 个任务
    - **Lite 版**：闭合式 VQA，评估核心诊断能力和基于给定关键帧的低级修正
    - **Hard 版**：开放式 VQA，要求模型先检测和定位失败，再以 Chain-of-Thought 格式输出指导

### 损失函数 / 训练策略

- 使用 LoRA 微调 Qwen3-VL-8B（LoRA rank=32，α=64）
- 仅训练 1 个 epoch，学习率 1e-5
- 使用 DeepSpeed ZeRO-2 阶段训练
- 同时解冻 LLM 骨干和适配器参数
- 4 × NVIDIA Hopper GPU

## 实验关键数据

### 主实验（ViFailback-Bench 评测）

| 模型 | Lite (%) | Hard (%) | 平均 (%) |
|------|---------|---------|---------|
| Gemini-2.5-Pro | 54.64 | 32.45 | 44.54 |
| GPT-4o | 48.21 | 40.00 | 44.47 |
| Qwen2.5-VL-72B | 50.61 | 36.56 | 44.21 |
| Qwen3-VL-32B | 47.79 | 35.23 | 42.07 |
| RoboBrain2.0-32B | 49.92 | 29.22 | 40.50 |
| **ViFailback-8B (本文)** | **最优** | **最优** | **最优** |

ViFailback-8B 在 Lite 和 Hard 两个设置上均显著超越所有开源和闭源模型。

### 真实世界机器人实验

| 配置 | 平均成功率提升 |
|------|-------------|
| 基线 VLA (无 ViFailback-8B) | 基准 |
| VLA + ViFailback-8B 监督 | **+22.2%** |

### 数据集规模

| 指标 | 数值 |
|------|------|
| 真实轨迹数 | 5,202 |
| VQA 对数 | 58,128 |
| 覆盖任务数 | 100 |
| 失败类型 | 4 大类 |
| 成功轨迹 / 失败轨迹 | 657 / 4,545 |

### 关键发现

1. 即使是 Gemini-2.5-Pro 这样的顶级闭源模型，在机器人失败诊断和修正任务上表现也有限（仅 44.54%），说明该领域需要专门的数据和训练
2. 具身 VLM（如 RoboBrain2.0、Cosmos-Reason1）在该基准上并不优于通用 VLM，说明具身知识不等同于失败理解能力
3. 视觉符号不仅能辅助标注，还能作为 VLA 模型的运行时修正信号，比纯文本指令更有效

## 亮点与洞察

1. **视觉符号设计精巧**：用颜色编码 3D 方向、用简单几何符号表达复杂语义，既降低了标注门槛，又能被 VLM 学习生成
2. **真实世界数据优先**：没有走仿真生成的路线，而是直接从遥操作和策略滚出中收集真实失败数据，更具实际价值
3. **闭环验证**：不仅训练了诊断模型，还在真实机器人上验证了 VLA + 外部监督者的失败恢复范式
4. **标注成本低**：利用视觉符号 + VLM 辅助，实现了半自动化标注，使大规模真实失败数据的构建成为可能

## 局限性 / 可改进方向

1. 视觉符号系统目前仅覆盖 4 大类失败，更复杂的失败模式（如多步推理失败）可能需要扩展符号集
2. ViFailback-8B 的监督频率固定（每 6 个动作块查询一次），自适应触发机制可能更高效
3. 数据集主要基于 ALOHA 双臂平台，泛化到其他机器人形态需要更多验证
4. 标注流水线虽然高效，但仍需人工参与，完全自动化标注是未来方向

## 相关工作与启发

- **YAY (Yell at Your Robot)**：通过人在回路反馈改进修正指令，但扩展性差
- **AHA / RACER / RoboFAC**：在仿真中合成失败数据微调 VLM，受限于 sim-to-real gap
- **TraceVLA / MOKA / RoVI**：利用视觉提示引导机器人策略，但侧重初始引导而非实时修正
- 本文的启发：视觉符号可以作为 VLM 和 VLA 之间的桥梁语言，既人类可读，又模型可解析

## 评分

- 新颖性: ⭐⭐⭐⭐ — 视觉符号用于失败标注和修正是新颖的思路
- 实验充分度: ⭐⭐⭐⭐⭐ — 从数据集构建到模型评测到真实机器人验证，链条完整
- 写作质量: ⭐⭐⭐⭐ — 结构清晰，但符号系统部分可以更简洁
- 价值: ⭐⭐⭐⭐⭐ — 为机器人从失败中学习提供了完整的框架和数据基础

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Language-Grounded Decoupled Action Representation for Robotic Manipulation](language-grounded_decoupled_action_representation_for_robotic_manipulation.md)
- [\[CVPR 2026\] Language-Grounded Decoupled Action Representation for Robotic Manipulation (LaDA)](lada_robotic_manipulation.md)
- [\[CVPR 2026\] CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding](cyclemanip_enabling_cyclic_task_manipulation_via_effective_historical_percepti.md)
- [\[CVPR 2026\] GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer](geco-srt_geometry-aware_continual_adaptation_for_robotic_cross-task_sim-to-real_.md)
- [\[CVPR 2026\] ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](forcevla2_unleashing_hybrid_force-position_control_with_force_awareness_for_cont.md)

<!-- RELATED:END -->
