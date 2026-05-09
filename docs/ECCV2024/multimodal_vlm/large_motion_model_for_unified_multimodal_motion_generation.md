---
title: >-
  [论文解读] Large Motion Model for Unified Multi-Modal Motion Generation
description: >-
  [ECCV 2024][多模态VLM][人体动作生成] LMM是首个多模态通用人体动作生成模型，统一了文本/动作/音乐/语音等10种任务、16个数据集（320K序列/1亿帧），通过身体部位感知的ArtAttention机制和可变帧率+随机遮掩的预训练策略，在多个标准benchmark上与专家模型竞争甚至超越。
tags:
  - ECCV 2024
  - 多模态VLM
  - 人体动作生成
  - 多模态统一模型
  - Transformer
  - 预训练策略
  - 身体部位感知
---

# Large Motion Model for Unified Multi-Modal Motion Generation

**会议**: ECCV 2024  
**arXiv**: [2404.01284](https://arxiv.org/abs/2404.01284)  
**代码**: [https://mingyuan-zhang.github.io/projects/LMM.html](https://mingyuan-zhang.github.io/projects/LMM.html)  
**领域**: 多模态VLM  
**关键词**: 人体动作生成, 多模态统一模型, Diffusion Transformer, 预训练策略, 身体部位感知

## 一句话总结

LMM是首个多模态通用人体动作生成模型，统一了文本/动作/音乐/语音等10种任务、16个数据集（320K序列/1亿帧），通过身体部位感知的ArtAttention机制和可变帧率+随机遮掩的预训练策略，在多个标准benchmark上与专家模型竞争甚至超越。

## 研究背景与动机

1. **领域现状**：人体动作生成包含多个子任务——文本到动作、动作到类别、音乐到舞蹈、语音到手势、动作预测、动作补间等。现有方法为每个任务设计专门模型，如MDM做text-to-motion，Bailando做music-to-dance。

2. **现有痛点**：(1) 专家模型受限于单一任务数据量和数据域，泛化能力差；(2) 不同数据集使用不同的动作表示（SMPL旋转/关键点坐标）、不同帧率（12.5-30fps）、不同关键点数（有些只有上半身），知识迁移极其困难；(3) 少数尝试多任务的工作只统一了2-3个使用相同格式的数据集。

3. **核心矛盾**：跨数据集的动作格式高度异构（表示方式/关键点数/帧率不统一），使得用单一模型学习跨任务通用知识面临巨大的数据对齐挑战。

4. **本文要解决什么？** (1) 如何统一异构的动作数据格式？(2) 如何设计能处理不完整身体部位数据的模型架构？(3) 如何有效利用多模态数据进行预训练？

5. **切入角度**：借鉴LLM的"大模型"思路——通过统一数据格式（MotionVerse）、部位感知架构（ArtAttention）和两阶段训练（无监督预训练+有监督微调），构建动作生成领域的基础模型。

6. **核心idea一句话**：将人体分为10个部位用统一中间表示对齐所有数据集，设计部位感知的Diffusion Transformer在身体部位级别独立控制生成，通过可变帧率和随机遮掩预训练充分利用异构数据。

## 方法详解

### 整体框架

(1) **MotionVerse数据集**：16个数据集统一到TOMATO中间表示格式，人体分为10个部位，标注哪些部位可用；训练表示转换器在测试时转回各数据集原始格式。(2) **LMM模型**：基于Diffusion Transformer，用ArtAttention在身体部位级别做注意力，支持多条件输入和部位遮掩。(3) **训练策略**：先无监督预训练（随机帧率+随机遮掩），再有监督微调。

### 关键设计

1. **MotionVerse统一数据表示**:
    - 做什么：将不同格式的动作数据对齐到统一中间表示
    - 核心思路：采用TOMATO格式作为统一中间表示，将人体划分为10个部位（头、躯干、左上臂、右上臂、左前臂、右前臂、左腿、右腿、左手、右手），每个序列标注可用部位。测试时训练表示转换器将中间格式转回各数据集的原始格式
    - 设计动机：不同数据集关键点数不同（如TED-Gesture只有上半身），部位级划分使得即使某些部位缺失也能正常训练

2. **ArtAttention（关节感知注意力）**:
    - 做什么：在身体部位级别实现精细控制的注意力计算
    - 核心思路：三个关键特性——(a) 多条件融合：通过交叉注意力融合文本/音乐/语音等多种条件信号；(b) 时空独立注意力：空间维度和时间维度分别做注意力，降低计算量；(c) 遮掩注入：在注意力计算中注入部位可用性遮掩，使缺失部位不参与计算
    - 设计动机：传统全身注意力无法处理部分身体缺失的数据，部位级注意力使不同数据集的知识可以在可用的身体部位上独立传递

3. **可变帧率+随机遮掩预训练**:
    - 做什么：通过数据增强策略使模型适应异构数据
    - 核心思路：(a) 随机帧率增强：训练时随机改变序列帧率，使模型学习帧率无关的动作表示；(b) 随机遮掩：以多种方式随机遮掩时间帧和身体部位，让模型学习不完整序列的补全能力；(c) 两阶段训练：先在全部数据上无监督预训练（遮掩补全），再在各任务数据上有监督微调
    - 设计动机：不同数据集帧率从12.5到30fps不等，随机帧率使模型鲁棒。随机遮掩类似BERT的MLM理念，让模型学习动作的时空分布

### 损失函数 / 训练策略

标准扩散去噪损失。无监督预训练阶段用遮掩重建损失，有监督微调阶段用条件生成损失。涵盖10个任务：T2M、A2M、M2D、S2G、MIm、MP、MIn、CMP、CMI、MMG。

## 实验关键数据

### 主实验

| 任务/数据集 | 方法 | FID↓ | R@3↑ | 说明 |
|-------------|------|------|------|------|
| T2M (HumanML3D) | MDM | 0.544 | 0.611 | 专家模型 |
| T2M (HumanML3D) | MLD | 0.473 | 0.772 | 专家模型 |
| T2M (HumanML3D) | **LMM** | **0.457** | **0.780** | 通用模型 |
| A2M (UESTC) | INR | 1.82 | - | 专家模型 |
| A2M (UESTC) | **LMM** | **1.65** | - | 通用模型 |
| M2D (AIST++) | Bailando | 28.16 | - | 专家模型 |
| M2D (AIST++) | **LMM** | **26.50** | - | 通用模型 |

### 消融实验

| 配置 | T2M FID↓ | M2D FID↓ | 说明 |
|------|----------|----------|------|
| w/o 部位感知 | 0.52 | 29.1 | 全身注意力无法处理缺失部位 |
| w/o 随机帧率 | 0.49 | 28.5 | 帧率敏感 |
| w/o 预训练 | 0.51 | 28.8 | 缺乏跨数据集知识 |
| Full LMM | **0.457** | **26.50** | 完整模型 |

### 关键发现

- **通用模型可以与专家模型竞争甚至超越**：LMM在9个标准benchmark中的大多数上达到竞争力结果，验证了多模态数据训练的价值
- **跨任务知识迁移有效**：预训练阶段学到的动作先验知识确实能迁移到不同下游任务
- **LMM展现涌现能力**：能处理多模态输入同时控制（如文本+音乐），完成训练中未见过的组合任务
- **数据规模效应**：随着数据量增大模型性能持续提升，但收益逐渐递减

## 亮点与洞察

- **MotionVerse的构建**：320K序列/1亿帧的统一动作数据集本身就是重要贡献，统一了10种任务16个数据集的格式差异
- **ArtAttention的部位级独立性**：将人体看作关节机器人的铰接结构，每个部位独立注意力+遮掩注入，优雅解决了缺失部位问题
- **LLM范式向动作领域的迁移**：预训练+微调、遮掩补全等策略的成功迁移，证明了"大模型"范式在非语言/视觉领域同样有效

## 局限性 / 可改进方向

- 表示转换器引入额外误差，不同数据集间的转换并非无损
- 当前10个部位划分粒度可能不够精细，手指动作等细节难以独立控制
- 模型规模和训练成本较大，但相比LLM仍小几个数量级
- 未探索人与场景/物体的交互生成
- 可以进一步扩展到全身+面部表情的联合生成

## 相关工作与启发

- **vs MDM/MLD**: 它们是文本到动作的专家模型，LMM通过多任务训练在相同任务上达到或超过其能力
- **vs MCM/UDE**: 它们处理2-3种任务但要求相同动作格式，LMM通过MotionVerse统一了16个异构数据集
- **vs Motion-X**: Motion-X也做统一动作数据集但只提供SMPLX格式，LMM的部位级中间表示更灵活
- 动作生成的"foundation model"思路可启发其他序列生成领域（如机器人轨迹规划）

## 评分

- 新颖性: ⭐⭐⭐⭐ 首个多模态通用动作生成模型，架构和数据设计有创新
- 实验充分度: ⭐⭐⭐⭐⭐ 9个benchmark+全面消融+涌现能力分析
- 写作质量: ⭐⭐⭐⭐ 问题分析透彻，方法描述系统
- 价值: ⭐⭐⭐⭐⭐ 动作生成领域的里程碑式工作

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] MotionChain: Conversational Motion Controllers via Multimodal Prompts](motionchain_conversational_motion_controllers_via_multimodal_prompts.md)
- [\[ECCV 2024\] Uni3DL: Unified Model for 3D and Language Understanding](uni3dl_a_unified_model_for_3d_vision-language_understanding.md)
- [\[ECCV 2024\] Nymeria: A Massive Collection of Multimodal Egocentric Daily Motion in the Wild](nymeria_a_massive_collection_of_multimodal_egocentric_daily_motion_in_the_wild.md)
- [\[ECCV 2024\] LEGO: Learning EGOcentric Action Frame Generation via Visual Instruction Tuning](lego_learning_egocentric_action_frame_generation_via_visual_instruction_tuning.md)
- [\[ECCV 2024\] MMBench: Is Your Multi-modal Model an All-Around Player?](mmbench_is_your_multimodal_model_an_allaround_player.md)

</div>

<!-- RELATED:END -->
