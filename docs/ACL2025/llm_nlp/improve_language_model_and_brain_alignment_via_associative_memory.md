---
title: >-
  [论文解读] Improve Language Model and Brain Alignment via Associative Memory
description: >-
  [ACL 2025][LLM/NLP][brain alignment] 通过模拟人类联想记忆（用相关概念扩展输入文本）提升语言模型与大脑 fMRI 活动的对齐度，发现联想记忆增强在内侧颞叶等记忆相关脑区效果最显著，并构建 Association 数据集通过 SFT 让 LLM 学会生成联想内容。
tags:
  - ACL 2025
  - LLM/NLP
  - brain alignment
  - associative memory
  - fMRI
  - language model
  - cognitive science
---

# Improve Language Model and Brain Alignment via Associative Memory

**会议**: ACL 2025  
**arXiv**: [2505.13844](https://arxiv.org/abs/2505.13844)  
**代码**: https://github.com/lemonsis/Association  
**领域**: LLM/NLP  
**关键词**: brain alignment, associative memory, fMRI, language model, cognitive science

## 一句话总结
通过模拟人类联想记忆（用相关概念扩展输入文本）提升语言模型与大脑 fMRI 活动的对齐度，发现联想记忆增强在内侧颞叶等记忆相关脑区效果最显著，并构建 Association 数据集通过 SFT 让 LLM 学会生成联想内容。

## 研究背景与动机

**领域现状**：语言模型的激活可以线性映射到处理同一文本时的大脑活动（brain score），这一对齐效应在多项研究中被验证。
**现有痛点**：虽然已知可以通过预测未来词来提升对齐度，但联想记忆——人类语言理解中整合关联信息的基本认知过程——在 LLM-大脑对齐中几乎未被探索。
**核心矛盾**：模型处理文本时只看到字面信息，而人类还会自发联想到相关概念——这种信息不对称是否是对齐度不高的原因之一？
**本文要解决什么？** (1) 模拟联想记忆是否改善对齐？(2) 教 LLM 生成联想内容是否改善对齐？
**切入角度**：用数据增强模拟联想（扩展上下文+关联知识），用 SFT 教 LLM 联想。
**核心idea一句话**：给 LLM 输入补充"联想到的"概念后，其在记忆相关脑区（内侧颞叶）的 brain score 显著提升。

## 方法详解

### 整体框架
两个研究问题：(1) 数据增强模拟联想 -> 用增强后的文本计算 LM 激活 -> 映射到 fMRI -> 对比 brain score；(2) 构建 Association SFT 数据集 -> 微调 LLaMA -> 用微调后 LLM 重新计算 brain score。

### 关键设计

1. **联想记忆数据增强**

    - 对每个词，扩展上下文窗口 + 加入 GPT-4 生成的关联概念
    - 设计动机：模拟人类听语音时脑中自发联想的过程

2. **Brain Score 计算**

    - 用线性回归将 LM 的层级激活映射到各脑区的 fMRI 信号
    - 使用 Pearson 相关系数评估映射质量
    - 设计动机：标准的 LM-大脑对齐评估方法

3. **Association SFT 数据集**

    - 1000 条样本：故事+联想指令为输入，联想内容为输出
    - 设计动机：教 LLM "主动联想"

## 实验关键数据

### 主实验 -- 联想增强后的 Brain Score 变化
| 脑区 | 原始 (GPT-2) | 联想增强后 | 提升 |
|------|-------------|-----------|------|
| 内侧颞叶 (MTL) | 基线 | **显著提升** | 主要改善区域 |
| 前额叶 | 基线 | 轻微提升 | |
| 语言区 (Wernicke) | 基线 | 基本不变 | |

### SFT 后 Brain Score
| 模型 | SFT 前 | SFT 后 (Association) |
|------|--------|---------------------|
| LLaMA-2 | 基线 | **MTL区显著提升** |

### 关键发现
- **联想记忆模拟选择性地提升记忆相关脑区的对齐度**
- **MTL 是最大受益区域**——符合认知科学中 MTL 负责联想记忆的知识
- **SFT 也能提升对齐度**：教 LLM 联想 => LLM 行为更像大脑
- **更大的模型获益更多**

## 亮点与洞察
- **认知科学与 AI 的交叉**——将联想记忆理论应用于 LLM，为"模型理解语言像人类吗"提供了新视角
- **SFT 改变 brain alignment**的发现暗示：训练数据的认知相关性可能比规模更重要

## 局限性 / 可改进方向
- Association 数据集仅 1000 条，规模小
- 联想内容由 GPT-4 生成，可能不完全反映真实人类联想
- 改进方向：更真实的联想数据、多模态联想

## 相关工作与启发
- **vs Caucheteux et al. (2023)**：他们用未来词预测提升对齐，本文用联想记忆提升对齐——互补
- **vs Moussa et al. (2024)**：他们微调语音模型，本文微调语言模型

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 联想记忆+LLM-大脑对齐的跨学科创新
- 实验充分度: ⭐⭐⭐ 两种验证方式但数据集小
- 写作质量: ⭐⭐⭐⭐ 认知基础扎实
- 价值: ⭐⭐⭐⭐ 对认知计算和 LLM 研究都有启发
