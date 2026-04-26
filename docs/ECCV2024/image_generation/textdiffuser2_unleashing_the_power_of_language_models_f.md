---
title: >-
  [论文解读] TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering
description: >-
  [ECCV 2024][图像生成][文本渲染] TextDiffuser-2 利用两个语言模型（一个用于布局规划、一个用于布局编码）实现灵活自动的文本渲染，克服了现有方法在灵活性、布局能力和样式多样性方面的局限。
tags:
  - ECCV 2024
  - 图像生成
  - 文本渲染
  - 扩散模型
  - 大语言模型
  - 布局规划
  - 混合粒度分词
---

# TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering

**会议**: ECCV 2024  
**arXiv**: [2311.16465](https://arxiv.org/abs/2311.16465)  
**代码**: https://aka.ms/textdiffuser-2 (有)  
**领域**: LLM/NLP  
**关键词**: 文本渲染, 扩散模型, 大语言模型, 布局规划, 混合粒度分词

## 一句话总结

TextDiffuser-2 利用两个语言模型（一个用于布局规划、一个用于布局编码）实现灵活自动的文本渲染，克服了现有方法在灵活性、布局能力和样式多样性方面的局限。

## 研究背景与动机

### 核心矛盾

**核心矛盾**：**领域现状**：扩散模型在图像生成上表现出色，但在视觉文本渲染方面仍有挑战（常生成错误符号或伪影）

### 解决思路

**本文目标**：**现有痛点**：现有文本渲染方法的三大不足：
  1. **灵活性和自动化有限**：GlyphDraw 需要用户设计字形图像，TextDiffuser 需手动指定关键词
  2. **布局预测能力受限**：GlyphDraw 仅支持单行文本，TextDiffuser 的 Layout Transformer 生成布局不美观
  3. **样式多样性受限**：TextDiffuser 使用字符级分割掩码，隐式约束了每个字符位置，限制了手写/艺术字体

## 方法详解

### 整体框架

两阶段训练：
1. **阶段一**：微调 LLM M₁（Vicuna-7B）将用户 prompt 转换为文本布局
2. **阶段二**：用布局编码器 M₂（CLIP text encoder）+ U-Net 联合训练扩散模型

### 关键设计

**语言模型布局规划（M₁）**：
- 输入格式：`[description] Prompt: [prompt] Keywords: [keywords]`
- 输出格式：每行 `textline x₀, y₀, x₁, y₁`（归一化到 128×128）
- 支持两种模式：自动推断关键词 / 用户指定关键词
- 使用 5K caption-OCR 数据对微调，交叉熵损失
- 支持通过对话修改布局（重新生成/添加/移动关键词）

**混合粒度分词（M₂）**：
- 提示文本保持原 BPE 分词
- 关键词分解为字符级 token（如 "WILD" → "[W][I][L][D]"）
- 引入坐标 token（如 "[x5]" 表示 x=5，"[y70]" 表示 y=70）
- 关键词间用 ⟨eos⟩ 分隔，总长度 L=128

**行级布局指导**：
- 与 TextDiffuser 的字符级分割掩码不同，采用行级边界框
- 行级指导提供更大灵活性，不约束字体样式

### 损失函数 / 训练策略

- 阶段一：交叉熵损失微调 Vicuna-7B，LR=2e-5，6 epochs，BS=256，8×A100
- 阶段二：L2 去噪损失训练 CLIP encoder + U-Net，LR=1e-4，6 epochs，BS=576，SD 1.5 基础
- 模型总参数：922M（含 256 坐标 token + 95 字符 token）
- 推理：布局生成 1.1s/张，图像生成 6s/张（50步采样）

## 实验关键数据

### 主实验

在 MARIO-Eval 基准上的定量结果：

| 方法 | FID↓ | CLIPScore↑ | OCR Acc↑ | OCR F↑ |
|------|------|-----------|---------|--------|
| SD-XL | 62.54 | 31.31 | 0.31 | 3.66 |
| PixArt-α | 87.09 | 27.88 | 0.02 | 0.03 |
| GlyphControl | 50.82 | 34.56 | 32.56 | 64.07 |
| TextDiffuser | 38.76 | 34.36 | 56.09 | 78.24 |
| **TextDiffuser-2** | **33.66** | **34.50** | **57.58** | 75.06 |

用户研究（人类/GPT-4V）：TextDiffuser-2 在布局美观、文本质量、图文匹配、修复能力上均领先。

### 消融实验

**微调数据量**：

| 数据量 | Acc↑ | F↑ | IoU↓ |
|--------|------|-----|------|
| 0k(2-shot) | 49.65 | 76.25 | 19.69 |
| 5k | **64.85** | **85.67** | 3.25 |
| 100k | 62.87 | 85.62 | 4.31 |

**坐标表示**：LT+RB（左上右下）+ 字符级分词最优；中心点表示准确率下降 22%。

**分词粒度**：字符级显著优于子词级（准确率差 42%）。

### 关键发现

1. 仅需 5K 数据即可有效微调 LLM 进行布局规划，更多数据并未带来提升
2. 字符级分词是文本渲染的关键——子词级分词使模型对拼写不敏感
3. 行级指导 vs 字符级指导是准确性与多样性的权衡——行级牺牲少量准确率换取更丰富字体样式
4. GPT-4V 作为评估者与人类评估高度一致

## 亮点与洞察

- **LLM 作为布局规划器**：将布局生成重构为语言生成任务，实现了自动化+可交互的文本布局
- **混合粒度分词创新**：prompt 用 BPE、关键词用字符级、位置用坐标 token，三者有机结合
- **行级灵活性**：比字符级控制更灵活，允许手写体、斜体等多样字体
- **仅 5K 数据的高效微调**：展示了 LLM 在少量数据下即可完成布局规划的能力

## 局限与展望 / 可改进方向

- OCR F-measure 略低于 TextDiffuser（75.06 vs 78.24），行级指导在精确渲染上有代价
- 布局规划 LLM 偶尔生成不合格式的输出
- 单点坐标表示（中心/左上）渲染角度多样但准确率大幅下降，实用性不足
- 仅支持英文文本，中文等其他语言的适用性未验证
- 未来可结合实例分割精确定位文本区域，或引入字体风格控制

## 相关工作与启发

- TextDiffuser 开创了字符级控制的文本渲染范式，TextDiffuser-2 在此基础上从字符级升级到行级
- LayoutGPT 用 GPT-4 布局的思路被本文用更小的开源 LLM 实现
- 混合粒度分词策略对多模态大模型中的文本感知有参考价值

## 评分

| 维度 | 分数 (1-5) |
|------|-----------|
| 新颖性 | 4 |
| 技术深度 | 4 |
| 实验充分性 | 4.5 |
| 写作质量 | 4 |
| 实用价值 | 4.5 |
| 总分 | 4.2 |

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] The Fabrication of Reality and Fantasy: Scene Generation with LLM-Assisted Prompt Interpretation](the_fabrication_of_reality_and_fantasy_scene_generation_with_llm-assisted_prompt.md)
- [\[ECCV 2024\] WebRPG: Automatic Web Rendering Parameters Generation for Visual Presentation](webrpg_automatic_web_rendering_parameters_generation_for_visual_presentation.md)
- [\[ECCV 2024\] M2D2M: Multi-Motion Generation from Text with Discrete Diffusion Models](m2d2m_multi-motion_generation_from_text_with_discrete_diffusion_models.md)
- [\[ECCV 2024\] NL2Contact: Natural Language Guided 3D Hand-Object Contact Modeling with Diffusion Model](nl2contact_natural_language_guided_3d_hand-object_contact_modeling_with_diffusio.md)
- [\[ECCV 2024\] Enhancing Diffusion Models with Text-Encoder Reinforcement Learning](enhancing_diffusion_models_with_text-encoder_reinforcement_learning.md)

<!-- RELATED:END -->
