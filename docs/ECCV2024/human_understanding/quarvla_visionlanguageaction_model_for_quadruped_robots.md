---
title: >-
  [论文解读] QUAR-VLA: Vision-Language-Action Model for Quadruped Robots
description: >-
  [ECCV 2024][人体理解][quadruped robot] 提出 QUAR-VLA 范式，首次将视觉、语言指令和动作生成统一到四足机器人中，构建了大规模多任务数据集 QUARD（259K episodes），训练 QUART 模型（基于 8B VLM）实现感知、导航、全身操控等多种任务，并展示了从仿真到真实的迁移能力。
tags:
  - ECCV 2024
  - 人体理解
  - quadruped robot
  - 视觉语言
  - embodied AI
  - sim-to-real
  - multi-task learning
---

# QUAR-VLA: Vision-Language-Action Model for Quadruped Robots

**会议**: ECCV 2024  
**arXiv**: [2312.14457](https://arxiv.org/abs/2312.14457)  
**代码**: https://github.com/Dingpx/QUAR-VLA (有)  
**领域**: Agent  
**关键词**: quadruped robot, vision-language-action, embodied AI, sim-to-real, multi-task learning

## 一句话总结
提出 QUAR-VLA 范式，首次将视觉、语言指令和动作生成统一到四足机器人中，构建了大规模多任务数据集 QUARD（259K episodes），训练 QUART 模型（基于 8B VLM）实现感知、导航、全身操控等多种任务，并展示了从仿真到真实的迁移能力。

## 研究背景与动机
1. **领域现状**：四足机器人学习通常将语言交互和视觉感知分开处理。QUAR-VA（仅视觉→动作）只依赖粗粒度目标图像指令，难以执行组合任务；QUAR-LA（仅语言→动作）缺乏视觉感知，无法自主导航。
2. **现有痛点**：(a) 缺乏大规模四足机器人多任务数据集；(b) 四足机器人的动作空间复杂（需要同时控制速度、姿态、步态参数），比固定基座操控机器人更难建模；(c) 仿真到真实的域差距。
3. **核心矛盾**：要让四足机器人自主完成多样化任务，必须同时理解视觉环境和语言指令并生成复杂的动作序列——但目前没有同时整合三者的模型和数据。
4. **本文要解决什么？** (a) 定义 QUAR-VLA 新范式；(b) 构建大规模数据集 QUARD；(c) 训练统一的 VLA 模型 QUART。
5. **切入角度**：利用预训练大型视觉-语言模型的语义理解能力，通过微调将其扩展为动作生成器，同时设计合理的动作空间（高层指令级别而非关节级别）降低学习难度。
6. **核心idea一句话**：将四足机器人控制建模为 VLA 问题，用预训练 MLLM 微调生成 12 维离散化动作 token，配合底层运动控制器实现端到端的视觉-语言-动作闭环。

## 方法详解

### 整体框架
输入：第一人称 RGB 图像 + 自然语言指令 → Tokenizer 编码为 token 序列 → 预训练 VLM（8B decoder-only transformer）→ 输出 12 维离散化动作 token → Detokenize 为连续动作→ 发送给底层运动控制器 → 四足机器人执行。推理频率 2Hz。

### 关键设计

1. **QUARD 数据集**:
    - 做什么：首个整合视觉、语言指令和机器人指令数据的大规模四足机器人数据集
    - 核心思路：7 种任务跨 3 个难度级别：Easy（字母识别 10K）、Medium（导航 72K sim + 3K real）、Hard（穿隧道 48K + 避障 63K + 钻杆 1K + 卸物 52K）。仿真数据在 Isaac Gym 中用 A*/D* 算法规划路径 + PD 控制器生成轨迹。真实数据 3K episodes 在实验室遥控收集
    - 设计动机：任务从简单到复杂形成层次——感知→导航→高级操控，高级任务需要组合多种基础能力

2. **动作空间设计**:
    - 做什么：定义 12 维高层指令动作空间
    - 核心思路：$[v_x, v_y, \omega_z, \theta_1, \theta_2, \theta_3, f, h_z, \phi, s_y, h_z^f, t]$ 包含速度（3维）、步态模式（3维）、频率、身高、俯仰角、脚宽、脚高、终止信号。每个连续维度离散化为 256 个 bin
    - 设计动机：不直接控制关节电机（对 VLM 太底层），也不仅输出 2D 导航速度（太简单），而是选择中间层级的指令控制——平衡灵活性和可学习性

3. **QUART 模型架构**:
    - 做什么：将预训练 VLM 微调为动作生成器
    - 核心思路：基于 8B 预训练 VLM，将动作 bin 映射到已有 token（整数 token），通过 symbol tuning 实现"语言模型输出动作"。标准的 next-token prediction + causal masking 训练
    - 设计动机：直接复用预训练 VLM 的视觉-语言对齐能力和常识推理能力，通过最小化的架构改动（仅重映射输出 token 含义）实现 VLA 功能

4. **Sim-to-Real Co-training**:
    - 做什么：混合仿真和真实数据训练，实现知识蒸馏
    - 核心思路：用大量仿真数据（256K）+ 少量真实数据（3K）共同训练，让仿真数据提供多样性、真实数据提供域对齐信号
    - 设计动机：纯仿真数据存在视觉、传感器、动力学差异，少量真实数据起到"锚定"作用

### 训练策略
- 基于 8B VLM，学习率 2e-5，batch size 256，训练 100K 步
- 标准 behavior cloning 损失（categorical cross-entropy）

## 实验关键数据

### 主实验

| 模型 | Easy(Distinguish) | Medium(Go to) | Hard(Avoid) | Hard(Tunnel) | Hard(Crawl) | Hard(Unload) | Unseen Object | Unseen Verbal |
|------|-------------------|---------------|-------------|-------------|-------------|-------------|---------------|---------------|
| CLIP | 0.44 | 0.43 | 0.45 | 0.19 | 0 | 0 | 0.11 | 0.14 |
| R3M | 0.58 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| VC-1 | 0.46 | 0.43 | 0.45 | 0.31 | 0 | 0 | 0.29 | 0.19 |
| **QUART** | **0.66** | **0.60** | **0.53** | **0.41** | **0.32** | **0.12** | **0.35** | **0.33** |

### Sim-to-Real Scaling

| Sim:Real 数据比 | 0K:3K | 25.6K:3K | 256K:3K |
|----------------|-------|----------|---------|
| 成功率 | 3/20 | 7/20 | **13/20** |

### 关键发现
- R3M 只在简单识别任务上有效，缺乏与文本的对齐导致无法理解指令执行动作
- CLIP/VC-1 在简单导航上可以，但复杂机械运动（钻杆、卸物）完全失败——VLM 理解世界原理不等于能执行复杂物理动作
- QUART 是唯一在所有任务上都有正成功率的模型，特别是在 crawl 和 unload 这类零 baseline 任务上取得突破
- 仿真数据量的增加直接提升真实世界性能（3/20 → 13/20），证明 sim-to-real 蒸馏有效
- QUART 对未见过的语言指令（verbal generalization）表现出合理泛化，得益于预训练 LLM 的语言理解能力

## 亮点与洞察
- **动作空间的层级选择**：不走极端（关节级 vs 导航级），选择指令级控制是关键设计决策——让 VLM 学"做什么"而非"怎么转关节"，降低了学习难度同时保留了动作丰富性
- **Symbol tuning 复用 token**：将连续动作离散化后映射到 VLM 已有的整数 token，无需修改架构——这种 trick 可迁移到任何需要让 LLM "输出非语言信号"的场景
- **Sim-to-Real 的数据配比**：大量仿真 + 少量真实数据的共训练范式，对于机器人学习有重要参考价值

## 局限性 / 可改进方向
- 动作空间粒度较粗（256 bin），精确控制能力有限
- 仅 2Hz 推理频率，高动态任务可能不够快
- 整体成功率仍然不高（最难任务 unload 只有 0.12），离实用差距大
- 任务场景相对简单（室内实验室），未在野外复杂地形测试
- 数据集主要在仿真中用 A*/D* 生成，行为多样性可能不足

## 相关工作与启发
- **vs RT-2**: RT-2 在固定基座操控臂上做 VLA，QUART 首次扩展到四足移动平台，动作空间设计不同（运动指令 vs 关节角度）
- **vs Octopus**: Octopus 输出代码调用API，QUART 直接输出控制指令——后者更端到端但可解释性较差
- **vs Tang et al. (QUAR-LA)**: 纯语言条件策略缺乏视觉感知，QUART 补上了这块短板

## 评分
- 新颖性: ⭐⭐⭐⭐ 首个四足机器人 VLA 范式，有开创性意义
- 实验充分度: ⭐⭐⭐ 缺少更多 baseline 对比，真实世界实验规模偏小
- 写作质量: ⭐⭐⭐ 结构尚可，但部分描述略冗余
- 价值: ⭐⭐⭐⭐ 数据集和范式对四足机器人社区很有价值

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] EgoExo-Fitness: Towards Egocentric and Exocentric Full-Body Action Understanding](egoexo-fitness_towards_egocentric_and_exocentric_full-body_action_understanding.md)
- [\[ECCV 2024\] Bridging the Gap Between Human Motion and Action Semantics via Kinematic Phrases](bridging_the_gap_between_human_motion_and_action_semantics_via_kinematic_phrases.md)
- [\[ECCV 2024\] A Simple Baseline for Spoken Language to Sign Language Translation with 3D Avatars](a_simple_baseline_for_spoken_language_to_sign_language_trans.md)
- [\[ECCV 2024\] HUMOS: Human Motion Model Conditioned on Body Shape](humos_human_motion_model_conditioned_on_body_shape.md)
- [\[ECCV 2024\] Large Motion Model for Unified Multi-Modal Motion Generation](large_motion_model_for_unified_multimodal_motion_generation.md)

<!-- RELATED:END -->
