---
title: >-
  [论文解读] NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models
description: >-
  [ECCV 2024][多模态][Vision-and-Language Navigation] 提出 NavGPT-2，通过将冻结 LLM 与视觉内容对齐，结合拓扑图导航策略网络，在保持 LLM 可解释性推理能力的同时，消除了基于语言模型的导航智能体与 VLN 专用模型之间的性能差距。
tags:
  - ECCV 2024
  - 多模态
  - Vision-and-Language Navigation
  - 视觉语言
  - Navigational Reasoning
  - Topological Graph
  - InstructBLIP
---

# NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

**会议**: ECCV 2024  
**arXiv**: [2407.12366](https://arxiv.org/abs/2407.12366)  
**代码**: https://github.com/GengzeZhou/NavGPT-2 (有)  
**领域**: Agent  
**关键词**: Vision-and-Language Navigation, Large Vision-Language Model, Navigational Reasoning, Topological Graph, InstructBLIP

## 一句话总结

提出 NavGPT-2，通过将冻结 LLM 与视觉内容对齐，结合拓扑图导航策略网络，在保持 LLM 可解释性推理能力的同时，消除了基于语言模型的导航智能体与 VLN 专用模型之间的性能差距。

## 研究背景与动机

1. **领域现状**：将 LLM 引入 Vision-and-Language Navigation (VLN) 任务已成为研究热点，目标是利用 LLM 的常识推理和语言理解能力来构建导航智能体。
2. **现有痛点**：当前将 LLM 用于 VLN 的方法存在两个极端——zero-shot 方法（如 NavGPT）依赖复杂 prompt 工程且性能差距巨大（~40% SR gap）；fine-tuning 方法（如 LangNav）虽然利用了预训练权重但性能仍远落后 VLN 专用模型，且牺牲了 LLM 的通用语言能力。
3. **核心矛盾**：如何在保持 LLM 的可解释导航推理和交互能力的同时，弥合与 VLN 专用模型的性能差距？
4. **本文要解决什么**：构建一个既能有效导航又能生成可解释导航推理的 VLN 智能体。
5. **切入角度**：不直接微调 LLM，而是冻结 LLM 并通过 Q-former 进行视觉对齐，同时利用 LLM 中间层特征驱动下游拓扑图导航策略网络。
6. **核心 idea 一句话**：将 VLM 的隐层表征同时用于语言解码（生成推理）和动作解码（拓扑图策略），在冻结 LLM 的前提下实现导航与推理的双重能力。

## 方法详解

### 整体框架

NavGPT-2 由两大组件构成：(1) 大型视觉语言模型 (VLM)，基于 InstructBLIP 架构，通过 Q-former 将多视角图像编码为 image tokens 输入冻结的 LLM；(2) 基于拓扑图的导航策略网络，利用 VLM 隐层特征进行全局动作预测。两阶段训练：第一阶段用 GPT-4V 生成的导航推理数据训练 Q-former；第二阶段冻结 VLM 训练策略网络。

### 关键设计

1. **Visual Aligning with LLMs（视觉-LLM 对齐）**
    - **做什么**：将多视角环境图像编码为固定长度 visual tokens，输入冻结 LLM。
    - **核心思路**：采用 Q-former 设计，对每个候选视角图像，先用冻结 ViT-g/14 (EVA-CLIP) 提取视觉特征，再通过 32 个可学习 query 与指令文本进行交叉注意力，得到指令感知的图像查询，最后线性投影为 LLM 输入 tokens。
    - **设计动机**：Q-former 可以有效控制多视角图像输入的长度，避免 token 过长问题，同时保留指令相关的视觉信息。

2. **Navigation System Prompt（导航系统提示）**
    - **做什么**：设计结构化导航提示格式，注入方向信息。
    - **核心思路**：使用 "Candidate i, facing a_i, {direction}" 格式化输入，引入 <IMG>, </IMG>, <INST>, </INST> 等特殊 token 插入图像和指令。用 GPT-4V 从 R2R 训练集生成 10K 导航推理数据进行 instruction tuning。
    - **设计动机**：让 LLM 理解空间方位关系，同时通过导航推理数据赋予 LLM 可解释的推理能力。

3. **VLM Latents as Visual-Linguistic Representation（VLM 隐层表征）**
    - **做什么**：将 LLM 隐层的图像和指令表征作为下游策略网络的输入特征。
    - **核心思路**：从 LLM 最后一层 Transformer 提取图像 tokens 和指令 tokens 的隐层表征，用 MLP 将每个视角的 32 个 image tokens 合并为单个 token。
    - **设计动机**：LLM 隐层经过跨模态注意力后已包含丰富的视觉-语言对齐信息，比原始视觉特征更适合导航决策。

4. **Graph Based Navigation Policy（基于图的导航策略）**
    - **做什么**：在导航过程中动态构建拓扑图，在全图上进行全局动作预测。
    - **核心思路**：维护包含已访问节点和未探索邻居节点的图记忆。每个节点由其所有候选视角的 VLM 特征平均池化表示，加上方向嵌入和步数嵌入。通过多层 Transformer 自注意力建模节点间空间关系，再通过图感知自注意力 (GASA) 引入距离和视觉相似性的空间亲和矩阵。
    - **设计动机**：解决 LLM 对空间结构理解不足和长程经验建模能力有限的问题，拓扑图可实现有效回溯。

### 损失函数 / 训练策略

- **两阶段训练**：
    - Stage 1：冻结 LLM 和视觉编码器，仅训练 Q-former 和投影层，使用自回归损失在导航推理数据上训练 200K steps。
    - Stage 2：冻结整个 VLM，仅训练下游导航策略网络。
- **策略学习**：结合 Behaviour Cloning (BC) 和 DAgger 损失：$\mathcal{L} = \lambda \mathcal{L}_{BC} + \mathcal{L}_{DAG}$
- **数据生成**：用 GPT-4V 在 R2R 训练集上随机选择 10K 中间步骤，输入全景图像生成单步导航推理数据。

## 实验关键数据

### 主实验

在 R2R 数据集上与 SOTA 方法对比（Val Unseen）：

| 方法 | Freeze LLM | NE↓ | SR↑ | SPL↑ |
|------|-----------|-----|-----|------|
| NavGPT (GPT-4) zero-shot | ✓ | 6.46 | 34 | 29 |
| MapGPT (GPT-4) zero-shot | ✓ | 6.92 | 39 | 26 |
| DiscussNav (GPT-4) zero-shot | ✓ | 5.32 | 43 | 40 |
| NavCoT (LLaMA2-7B) | ✗ | 6.26 | 40 | 37 |
| DUET (Baseline) | - | 3.31 | 72 | 60 |
| **NavGPT-2 (FlanT5-XXL)** | **✓** | **~3.0** | **~72** | **~62** |

### 消融实验

不同 LLM backbone 对比（Val Unseen SR）：

| LLM | 参数量 | SR↑ |
|-----|--------|-----|
| FlanT5-XL | 3B | ~67 |
| FlanT5-XXL | 11B | ~72 |
| Vicuna-7B | 7B | ~68 |
| Vicuna-13B | 13B | ~70 |

关键发现：encoder-decoder 架构 (FlanT5) 整体优于 decoder-only (Vicuna)。

### 关键发现

- NavGPT-2 首次消除了基于 LM 的智能体与 VLN 专用模型之间的性能差距
- 即使冻结 LLM 参数，通过 Q-former 对齐也能获得高质量的视觉-语言表征
- 10K 导航推理数据即可赋予 LLM 生成可解释导航推理的能力
- 拓扑图策略比直接让 LLM 输出动作更有效

## 亮点与洞察

- **保持 LLM 通用能力**：冻结 LLM 不破坏其语言生成能力，使智能体能交互问答、解释决策、接受用户干预
- **数据效率**：仅需 10K 推理数据 + R2R 训练集即可达到 SOTA 性能
- **架构巧妙**：VLM 隐层同时服务于「语言解码」和「动作解码」两条路径，一举两得
- **实用价值**：生成人类可理解的导航推理过程，有助于构建可信赖的交互式 VLN 智能体

## 局限性 / 可改进方向

- 仅在离散导航图上验证，未扩展到连续环境
- GPT-4V 生成的推理数据质量有限且成本较高
- 拓扑图策略的可扩展性——大规模环境中图节点过多时效率可能下降
- 未探索端到端训练 VLM + 策略网络的可能性

## 相关工作与启发

- 与 NavGPT (zero-shot) 是同一团队的升级版，从 zero-shot 转向 visual alignment 范式
- DUET 的拓扑图策略被 NavGPT-2 复用，说明好的导航策略模块可以与不同的感知前端组合
- InstructBLIP 的 Q-former 架构被证明在导航领域也非常有效
- 启发：冻结大模型 + 轻量对齐模块 + 下游任务头的范式在具身智能中前景广阔

## 评分

- ⭐⭐⭐⭐ 新颖性：巧妙地将 VLM 隐层表征同时用于推理和动作，但整体框架是已有组件的组合
- ⭐⭐⭐⭐⭐ 实验充分度：多个 LLM backbone、详细消融、定性分析
- ⭐⭐⭐⭐ 写作质量：结构清晰，动机阐述充分
- ⭐⭐⭐⭐⭐ 价值：首次消除 LM 智能体与 VLN 专家的差距，具有里程碑意义

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](sq-llava_self-questioning_for_large_vision-language_assistant.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)
- [\[ECCV 2024\] Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models](vary_scaling_up_the_vision_vocabulary_for_large_vision-language_model.md)
- [\[ECCV 2024\] IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models](ivtp_instruction-guided_visual_token_pruning_for_large_vision-language_models.md)
- [\[ECCV 2024\] Robust Calibration of Large Vision-Language Adapters](robust_calibration_of_large_vision-language_adapters.md)

<!-- RELATED:END -->
