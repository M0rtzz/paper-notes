---
title: >-
  [论文解读] Octopus: Embodied Vision-Language Programmer from Environmental Feedback
description: >-
  [ECCV 2024][embodied agent] Octopus 是一个具身视觉-语言编程模型，通过将 VLM 与可执行代码生成相结合，利用 GPT-4 收集训练数据并引入 RLEF（环境反馈强化学习）进行微调，在三个不同模拟器（OmniGibson、Minecraft、GTA-V）中实现了端到端的视觉感知→计划→代码生成→执行闭环。
tags:
  - ECCV 2024
  - embodied agent
  - 视觉语言
  - code generation
  - 强化学习
  - environmental feedback
---

# Octopus: Embodied Vision-Language Programmer from Environmental Feedback

**会议**: ECCV 2024  
**arXiv**: [2310.08588](https://arxiv.org/abs/2310.08588)  
**代码**: https://github.com/dongyh20/Octopus (有)  
**领域**: Agent  
**关键词**: embodied agent, vision-language programming, code generation, reinforcement learning, environmental feedback

## 一句话总结
Octopus 是一个具身视觉-语言编程模型，通过将 VLM 与可执行代码生成相结合，利用 GPT-4 收集训练数据并引入 RLEF（环境反馈强化学习）进行微调，在三个不同模拟器（OmniGibson、Minecraft、GTA-V）中实现了端到端的视觉感知→计划→代码生成→执行闭环。

## 研究背景与动机
1. **领域现状**：大型视觉-语言模型（VLMs）在多模态感知和推理上取得了显著进展。当应用于具身智能体时，现有方法要么输出底层操控动作序列（如 RT-2），要么只提供抽象级别的计划（如 SayCan、SayPlan）。
2. **现有痛点**：高层计划和底层操控之间存在鸿沟——纯语言模型（如 Voyager）虽能调用API但缺乏视觉感知；视觉模型（如 EmbodiedGPT）虽有视觉但缺少可执行代码生成能力；TAPA 等方法依赖独立视觉模块将图像转文本再给 LLM，信息损失严重。
3. **核心矛盾**：现有的具身 AI 模拟器环境缺乏精心设计的视觉依赖型函数调用——很多函数（如 Minecraft 的 exploreUntil()）完全绕过了视觉信息，使模型变成"盲"模型。
4. **本文要解决什么？** (a) 如何让 VLM 同时输出计划和可执行代码？(b) 如何构建视觉依赖的基准环境？(c) 如何利用环境反馈改进模型？
5. **切入角度**：将可执行代码作为连接高层计划和底层操控的中间表示，用 System-I/System-II 思维框架——底层动作（System-I）用预定义代码实现，计划推理（System-II）交给大模型。
6. **核心idea一句话**：用 VLM 生成可执行代码作为计划-操控桥梁，并通过环境反馈的强化学习（RLEF）持续优化决策。

## 方法详解

### 整体框架
输入：智能体的第一人称视角图像（8张FPV + 2张BEV）+ 文本任务描述 → 经过 Octopus 模型 → 输出：自然语言计划 + 可执行 Python 代码 → 在模拟器中执行 → 获取环境反馈用于 RLEF 训练。

整个流程分三步：(1) 用 GPT-4 在 OctoVerse 中收集训练数据；(2) SFT 监督微调 Octopus 模型；(3) RLEF 环境反馈强化学习进一步优化。

### 关键设计

1. **OctoVerse 环境套件**:
    - 做什么：提供三个不同风格的模拟器环境用于训练和评估
    - 核心思路：包括 OctoGibson（基于 OmniGibson 的室内场景，476个任务，16个函数调用）、OctoMC（基于 Minecraft 的开放世界，40个任务，6个函数）、OctoGTA（基于 GTA-V 的城市场景，25个任务，19个函数）
    - 设计动机：关键创新是**视觉依赖的函数设计**——限制 moveBot(object) 只能接收大物体（桌子）作参数，让机器人必须用视觉识别小物体的位置；Minecraft 中用 teleport(yaw, distance) 替代自动寻路的 exploreUntil()；GTA 中用 goForward(distance) + turnPlayer(degree) 替代直接 walkTo(location)

2. **GPT-4 驱动的数据收集**:
    - 做什么：自动化收集视觉-代码训练对
    - 核心思路：给 GPT-4 提供系统提示 + 环境信息（观察到的物体、关系、库存等），让它生成计划和代码。同时收集执行反馈——成功的步骤标记为正样本，失败的为负样本。使用 GPT-4 32K 处理超长上下文
    - 设计动机：手工标注成本过高，利用 GPT-4 的代码能力实现自动化数据收集。错误管理策略保证即使任务失败的数据也有训练价值

3. **Octopus 模型架构**:
    - 做什么：统一的视觉-语言编程模型
    - 核心思路：基于 Otter 架构，使用 CLIP ViT-L/14 作为视觉编码器 + MPT-7B 作为语言解码器，通过 Perceiver Resampler 将图像转为视觉 token，然后通过 Cross-Gated Attention 实现视觉-语言交互。标准的 next-token prediction 训练：$p(\mathbf{T}_r|\mathbf{T}_i,\mathbf{X}_v)=\prod_{l=1}^{L}p(t_l|\mathbf{X}_v,\mathbf{T}_i,\mathbf{T}_{r,<l})$
    - 设计动机：Flamingo 风格的架构天然支持多图像输入，适合处理360度FPV + BEV的多视角输入

4. **RLEF（环境反馈强化学习）**:
    - 做什么：利用环境执行反馈优化模型的决策策略
    - 核心思路：将任务进度表示为树结构——每个节点是一个子任务，带有成功/失败的二值标签。用 CodeLLaMA-7B + value head 作为奖励模型 $r_\phi$，评估文本状态转换的质量。用 PPO 训练策略模型：$\mathcal{L}(\pi_\theta^{RL})=-\mathbb{E}[r_\phi(\mathbf{T}_i^*,\mathbf{T}_r)-\beta\cdot D_{KL}(\pi_\theta^{RL}\|\pi^{INIT})]$
    - 设计动机：与 RLHF 类比但用环境反馈代替人类偏好——环境反馈是确定性的（任务是否完成），比人类打分更准确、更可扩展

### 训练策略
- 第一阶段 SFT：在收集的视觉-代码对上做监督微调
- 第二阶段 RLEF：用环境反馈建立奖励模型，然后用 PPO 微调策略模型
- KL 散度惩罚防止策略偏离太远

## 实验关键数据

### 主实验（OctoGibson）

| 模型 | 整体任务完成率 | 可见环境 | 未见环境 | Follow任务 | Reason任务 |
|------|---------------|---------|---------|-----------|-----------|
| GPT-4 (blind) | 0.43/0.68 | 0.42/0.69 | 0.46/0.67 | 0.49/0.78 | 0.27/0.40 |
| GPT-4V | 0.45/0.63 | 0.40/0.62 | 0.60/0.67 | 0.42/0.67 | 0.53/0.53 |
| EmbodiedGPT | 0.10/0.40 | 0.04/0.36 | 0.27/0.53 | 0.13/0.38 | 0.00/0.40 |
| Octopus (SFT) | 0.15/0.37 | 0.11/0.33 | 0.27/0.47 | 0.16/0.38 | 0.13/0.33 |
| **Octopus (SFT+RLEF)** | **0.18/0.42** | 0.13/0.38 | **0.33/0.53** | 0.18/0.40 | **0.20/0.53** |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 仅训练 connector | 4/60 任务成功 | 参数太少不够 |
| connector + language decoder | 5/60 任务成功 | 略有提升 |
| 7B 模型 | 9/60 (SFT), 11/60 (RLEF) | 完整大小 |
| 3B 模型 | 性能明显下降 | 模型大小很重要 |
| 随机打乱视觉输入 | 显著性能下降 | 确认模型确实利用视觉信号 |

### 关键发现
- RLEF 在**推理任务和未见环境**上提升最为显著（Reason: 0.13→0.20, 未见环境: 0.27→0.33），说明环境反馈帮助模型学到了更鲁棒的决策策略
- CodeLLaMA 虽然代码执行率高（92% vs LLaMA 24%），但计划能力并不突出——说明具身任务瓶颈在计划而非代码
- 盲LLM在处理长文本环境信息时效果差——凸显了直接视觉感知的优势
- 即使在训练数据极少的 OctoGTA（仅160个训练任务）上也能完成部分任务

## 亮点与洞察
- **代码作为计划-操控的桥梁**：这是一个非常优雅的设计——代码既是人可读的计划，又是机器可执行的指令。比直接输出低层动作更可控、更可解释，比纯语言计划更可执行
- **视觉依赖的环境设计**：通过精心限制API参数，强制模型使用视觉信息，这个思路可以迁移到任何具身AI benchmark的设计中
- **RLEF vs RLHF**：用环境反馈代替人类偏好是clever的——具身AI天然有"任务是否完成"的客观信号，比主观偏好更准确、标注成本更低
- **树结构的任务表示**：将multi-step任务表示为树，自然支持step-level和task-level的反馈信号收集

## 局限性 / 可改进方向
- 整体性能仍然较低（最好也只有 0.18 的任务完成率），与 GPT-4 的 0.43 差距明显
- 仅在模拟器中验证，未测试真实物理环境的迁移能力
- 视觉编码器（CLIP ViT-L/14）可能不够强大，未尝试更大的视觉模型
- 奖励模型是纯文本的（CodeLLaMA），没有利用视觉信息来判断奖励，可能限制了RLEF的效果
- 训练数据收集依赖 GPT-4，成本较高且受限于 GPT-4 自身的能力上限

## 相关工作与启发
- **vs EmbodiedGPT**: 都是视觉-语言具身模型，但 EmbodiedGPT 输出策略映射而非代码，Octopus 的代码生成方式更可控更可解释
- **vs Voyager**: Voyager 用 GPT 生成代码但无视觉感知，Octopus 统一了视觉+代码生成
- **vs RT-2/PaLM-E**: 这些模型直接输出低层动作，Octopus 通过代码层的抽象保持了更好的可解释性

## 评分
- 新颖性: ⭐⭐⭐⭐ 代码作为计划-操控桥梁 + RLEF 是有趣的创新，但核心模型架构较常规
- 实验充分度: ⭐⭐⭐⭐ 三个环境 + 消融实验充分，但整体性能偏低
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图表丰富，但符号使用略繁琐
- 价值: ⭐⭐⭐⭐ OctoVerse 环境套件对社区有很好的基准价值，RLEF思路有启发性

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] AdaGlimpse: Active Visual Exploration with Arbitrary Glimpse Position and Scale](adaglimpse_active_visual_exploration_with_arbitrary_glimpse_position_and_scale.md)
- [\[AAAI 2026\] Vision-Language Reasoning for Geolocalization: A Reinforcement Learning Approach](../../AAAI2026/reinforcement_learning/vision-language_reasoning_for_geolocalization_a_reinforcement_learning_approach.md)
- [\[ACL 2026\] Feedback-Driven Tool-Use Improvements in Large Language Models via Automated Build Environments](../../ACL2026/reinforcement_learning/feedback-driven_tool-use_improvements_in_large_language_models_via_automated_bui.md)
- [\[ICLR 2026\] CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning](../../ICLR2026/reinforcement_learning/cuda-l1_improving_cuda_optimization_via_contrastive_reinforcement_learning.md)
- [\[AAAI 2026\] STELAR-Vision: Self-Topology-Aware Efficient Learning for Aligned Reasoning in Vision](../../AAAI2026/reinforcement_learning/stelar-vision_self-topology-aware_efficient_learning_for_aligned_reasoning_in_vi.md)

<!-- RELATED:END -->
