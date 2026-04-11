---
description: "【论文笔记】CodePercept: Code-Grounded Visual STEM Perception for MLLMs 论文解读 | CVPR2026 | arXiv 2603.10757 | STEM视觉感知 | 通过系统性缩放分析发现 **感知(perception)而非推理(reasoning)** 是MLLM在STEM领域的真正瓶颈，提出以可执行Python代码为锚定媒介的CodePercept范式，构建百万级ICC-1M数据集和STEM2Code-Eval基准，显著提升MLLM的STEM视觉感知能力。"
tags:
  - CVPR2026
---

<!-- 由 src/gen_stubs.py 自动生成 -->
# CodePercept: Code-Grounded Visual STEM Perception for MLLMs

**会议**: CVPR2026  
**arXiv**: [2603.10757](https://arxiv.org/abs/2603.10757)  
**代码**: [TongkunGuan/Qwen-CodePercept](https://github.com/TongkunGuan/Qwen-CodePercept)  
**领域**: 多模态VLM  
**关键词**: STEM视觉感知, 可执行代码, 图像重建, 代码锚定字幕, 多模态大模型, 感知增强

## 一句话总结

通过系统性缩放分析发现 **感知(perception)而非推理(reasoning)** 是MLLM在STEM领域的真正瓶颈，提出以可执行Python代码为锚定媒介的CodePercept范式，构建百万级ICC-1M数据集和STEM2Code-Eval基准，显著提升MLLM的STEM视觉感知能力。

## 研究背景与动机

1. **STEM推理的瓶颈之问**：当前大量工作聚焦于用强化学习增强MLLM的推理能力（冷启动数据、RL奖励设计、单模态推理数据迁移），但始终未回答：模型STEM任务失败到底是感知不足还是推理不足？
2. **缩放实验揭示真相**：作者将STEM视觉推理解耦为感知（image→caption）和推理（caption→answer）两阶段，独立缩放一端并固定另一端，发现**扩展感知始终优于扩展推理**，证明感知才是STEM视觉推理的真正杠杆。
3. **知识蒸馏的幻觉问题**：直觉方案——用GPT/Gemini等强模型生成描述性字幕进行知识蒸馏——faced两大缺陷：教师模型在空间关系、数量细节上易幻觉；复杂STEM图像存在"描述失语"（descriptive aphasia），自然语言无法精确刻画辅助线、多面体等结构。
4. **评测范式的缺失**：现有STEM评测（MathVision、MathVista等）以问题解答准确度为代理指标，只能反映"与问题相关的理解"，无法度量全面的视觉感知能力。
5. **代码作为感知媒介的优势**：可执行代码天然具有精确语义、可验证性、结构化表达，与STEM视觉内容的结构化本质对齐——只有完整理解图像才能生成正确的重建代码。
6. **训练数据的空白**：缺乏大规模、高质量的STEM图像-代码配对数据来训练模型的代码锚定感知能力。

## 方法详解

### 整体框架

CodePercept包含三大模块：(1) 图像-代码对构建引擎 → (2) 两种代码锚定训练任务 → (3) SFT+RL两阶段后训练。基于Qwen3-VL系列模型。

### 关键设计

**1. 图像-代码对构建（三条互补pipeline）**

- **Image Reproduction (IR)**：对种子STEM图像，先用MLLM生成详细描述，再基于图像+描述生成matplotlib重建代码。受限于源图像多样性。
- **Image Diversity (ID)**：抽取种子图像的底层科学原理（Gₚᵣᵢₙ꜀ᵢₚₗₑ），基于同一原理生成K个不同视觉实例化代码。例如从多米诺逻辑谜题生成圆形排列、三角组合、瓢虫矩阵等变体，保持STEM严谨性的同时引入结构新颖性。
- **Solid Geometry (SG)**：针对LLM/MLLM在立体几何代码生成上的根本缺陷，构建参数化模板库（立方体展开折叠、正投影三视图、截面分析、多面体构造等），通过参数采样批量生成。

**2. 统一质量控制**：三阶段过滤——图像质量Qᵢ + 代码质量Q꜀ + 图像-代码一致性Qᵢ꜀，均由SOTA MLLM+专用prompt评估。

**3. Code-Grounded Caption Generation（代码锚定字幕生成）**

核心思路：用可执行代码作为ground truth来修正自然语言字幕的幻觉。

- **Step 1 Native Caption**：MLLM直接生成图像描述草稿t_draft（语言流畅但事实易错）
- **Step 2 Code Analysis**：利用代码本身+执行日志ξ(c)提取经验证的视觉事实t_code。执行追踪器记录几何精度（坐标、尺寸、空间关系）、数量属性（计数、RGB值）、渲染语义（z-order、变换矩阵）等
- **Step 3 Code-Grounded Refinement**：LLM做"外科手术式"编辑——修正事实错误、替换模糊量词为精确数值、补充遗漏内容，同时保持原始语言风格和描述流畅性

**4. STEM Image-to-Code Translation（STEM图像到代码翻译）**

- 先让MLLM直接从图像生成"讲解式"代码草稿（含分步注释、参数解释）
- 再用ground-truth代码作为参考进行修正，保留讲解结构但确保代码正确性
- 最终得到兼具教学性和正确性的explanatory code

### 训练策略

- **Stage 1 SFT (CodePercept-S1)**：在ICC-1M上联合训练image→caption和image→code两个任务，两种模态互补——字幕提供语义上下文，代码提供精确结构化细节
- **Stage 2 RL (CodePercept-R1)**：仅对代码生成施加GRPO强化学习，设计两类奖励：
  - Format Reward：正则验证代码格式（二值奖励）
  - Content Reward：执行奖励（代码能否执行）+ 代码级奖励（GPT-4o评估语义等价性）+ 图像级奖励（GPT-4o评估视觉相似性）

## 实验

### 主要结果

**感知能力评估（Captioner-Solver范式）**：CodePercept作为captioner生成描述，固定LLM solver解题。

| 模型 | MathVision | MathVista | MathVerse | DynaMath | WeMath | LogicVista | Avg |
|---|---|---|---|---|---|---|---|
| Qwen3-VL-4B-Instruct | 54.21 | 67.30 | 64.59 | 69.40 | 46.10 | 54.14 | 59.29 |
| **CodePercept-4B-S1** | **57.63** | **69.60** | **65.59** | **71.38** | **47.81** | **60.40** | **62.07 (+2.8)** |
| Qwen3-VL-8B-Instruct | 54.37 | 69.60 | 63.75 | 72.19 | 45.43 | 56.82 | 60.36 |
| **CodePercept-8B-S1** | **59.31** | **70.20** | **66.52** | **73.20** | **49.14** | **61.52** | **63.32 (+3.0)** |
| Qwen3-VL-32B-Instruct | 58.55 | 72.20 | 71.09 | 75.78 | 48.00 | 62.19 | 64.63 |
| **CodePercept-32B-S1** | **62.27** | **72.90** | **71.70** | **77.41** | **54.19** | **65.33** | **67.30 (+2.7)** |

**STEM2Code-Eval（图像重建感知评估）**：

| 模型 | Image Score | Code Score | Avg | Exec Rate |
|---|---|---|---|---|
| Qwen3-VL-8B-Instruct | 28.59 | 28.23 | 28.41 | 85.3% |
| CodePercept-8B-S1 | 44.53 | 46.78 | 45.66 | 87.6% |
| **CodePercept-8B-R1** | **50.25** | **47.04** | **48.65** | **93.4%** |
| CodePercept-32B-S1 | 61.14 | 56.99 | 59.07 | 93.0% |
| **CodePercept-32B-R1** | **68.97** | **62.53** | **65.75** | **95.9%** |

### 消融实验

| 配置 | Avg |
|---|---|
| Qwen3-VL-8B baseline | 60.36 |
| + IR-CodeCap | 60.91 |
| + ID-CodeCap | 62.15 |
| + SG-CodeCap | 62.75 |
| NativeCap（无代码锚定） | 60.78 |
| CodeCap（代码锚定字幕） | 62.75 (+2.0) |
| CodeCap + ImCode（双任务） | 63.32 (+0.6) |

### 关键发现

- CodePercept-8B-S1在captioner-solver设置下超越了Qwen2.5-VL-72B等大得多的模型（+6.2%），接近Claude-Opus 4.1-Thinking和GPT5-Thinking的水平
- RL阶段对代码生成质量提升显著：4B模型Avg从40.78→46.52，执行成功率从80.7%→91.3%
- 三条数据pipeline逐步叠加均有增益，ID-CodeCap贡献最大（程序化生成多样STEM图像+验证代码提供更强训练信号）
- 代码锚定字幕比直接字幕生成高2.0个点，验证了代码作为ground truth消除幻觉的有效性
- Image-to-code和image-to-caption两任务互补：字幕提供语义上下文助力代码生成，代码生成通过精确可执行的特性反哺字幕准确性

## 亮点

- **insight深刻**：通过严谨的缩放实验首次定量证明"感知>推理"是STEM瓶颈，而非仅凭直觉
- **范式创新**：将可执行代码同时用于(1)评测感知能力和(2)增强感知能力，形成闭环
- **执行追踪器设计精巧**：通过运行代码获取执行日志来辅助LLM分析复杂代码逻辑，解决了深层递归/嵌套循环难以静态分析的问题
- **立体几何模板化方案务实**：不回避LLM生成立体几何代码的根本缺陷，而是用参数化模板绕过
- **评测benchmark有价值**：STEM2Code-Eval首次提供确定性、可验证的STEM视觉感知评测

## 局限性

- RL阶段的Content Reward依赖GPT-4o打分，成本高且引入主观性，难以规模化
- 代码生成局限于matplotlib库，无法覆盖所有STEM可视化类型（如3D交互图、动态仿真）
- 立体几何依赖人工设计模板，覆盖范围受限于模板数量
- STEM2Code-Eval仅1000样本，统计置信度有限
- 未探索代码锚定范式对非STEM领域（如医学图像、遥感等）的泛化性

## 相关工作

- **STEM推理增强**：Intern-S1、KeyeVL1.5、MiMo-VL-7B-RL等聚焦推理，本文指出应先解决感知
- **感知评测**：[30]采用captioner-solver两阶段但只度量问题相关信息，本文提出代码重建作为更全面的评测
- **领域特定代码生成**：UI/Chart/SVG代码生成关注下游应用，本文的STEM图像-代码对既用于评测也用于训练
- **知识蒸馏**：传统直接蒸馏teacher模型描述，本文用代码作为中间媒介消除幻觉

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 感知瓶颈的缩放验证+代码锚定感知范式均为首创
- 实验充分度: ⭐⭐⭐⭐ — 6个benchmark + 3种模型规模 + 完整消融，但RL阶段消融不够细致
- 写作质量: ⭐⭐⭐⭐⭐ — 逻辑清晰，动机→方法→评测一脉相承
- 价值: ⭐⭐⭐⭐⭐ — 揭示STEM瓶颈在感知而非推理，对社区有重要指导意义
