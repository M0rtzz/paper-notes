---
title: >-
  [论文解读] Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models
description: >-
  [ACL 2025][parallel data] 系统研究在 decoder-only LLM 训练中加入平行数据对多语言能力的影响，发现将平行数据放在训练末期效果最好，且平行数据显著优于等量的单语数据；LLM 无法自动泛化到训练方向的反向翻译。
tags:
  - ACL 2025
  - parallel data
  - multilingual
  - continual pre-training
  - translation
  - cross-lingual
---

# Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models

**会议**: ACL 2025  
**arXiv**: [2506.13044](https://arxiv.org/abs/2506.13044)  
**代码**: https://github.com/nusnlp/just-go-parallel  
**领域**: LLM/NLP  
**关键词**: parallel data, multilingual, continual pre-training, translation, cross-lingual

## 一句话总结
系统研究在 decoder-only LLM 训练中加入平行数据对多语言能力的影响，发现将平行数据放在训练末期效果最好，且平行数据显著优于等量的单语数据；LLM 无法自动泛化到训练方向的反向翻译。

## 研究背景与动机

**领域现状**：即使未显式使用平行数据训练，LLM 也展现出翻译能力——被归因于训练数据中的偶然双语信号。一些主流多语言 LLM（如 BLOOM）选择不使用平行数据。

**现有痛点**：平行数据对 encoder 模型有效已被证明（如 XLM），但 decoder-only LLM 是否也受益？最优使用策略（何时加入、加多少）未知。

**核心矛盾**：decoder LLM 通常忽略平行数据——这是否是个错误决策？

**本文要解决什么？** 通过控制实验系统回答平行数据的价值和最优使用方式。

**切入角度**：固定总训练量，对比 7 种不同数据策略（无平行/单语替代/平行前置/分散/末置等）。

**核心idea一句话**：平行数据放在训练末期对多语言能力的提升最大；放在开始会导致严重的灾难性遗忘。

## 方法详解

### 整体框架
保持相同的总训练量和数据顺序 -> 在不同位置插入等量平行数据（替换等量非平行数据）-> 对比翻译/多语言常识推理/其他 NLP 任务的性能。

### 关键设计

1. **7 种实验设置**

    - No Parallel：无平行数据（基线）
    - Multilingual：加等量目标语言单语数据（对照组）
    - Parallel Non-Adjacent：平行数据不相邻排列
    - Parallel First：平行数据在训练开始
    - Parallel Distributed：平行数据均匀分散
    - Parallel Last (all)：平行数据在训练末尾，双向翻译
    - Parallel Last (uni)：平行数据在训练末尾，单向翻译
    - 设计动机：控制变量，隔离位置和双语性的影响

2. **控制训练量**

    - 加入平行数据时移除等量末尾非平行数据
    - 确保总 token 数和训练顺序一致
    - 设计动机：消除数据量差异的干扰

## 实验关键数据

### 主实验 — 翻译性能（WMT22, BLEU）
| 设置 | En→X 平均 | X→En 平均 | 说明 |
|------|----------|----------|------|
| No Parallel | 12.3 | 15.1 | 基线 |
| Multilingual (单语替代) | 14.2 | 16.5 | 单语有帮助但有限 |
| Parallel First | 10.5 | 13.2 | **灾难性遗忘** |
| Parallel Distributed | 16.8 | 19.3 | 分散较好 |
| **Parallel Last (all)** | **19.5** | **22.1** | **最佳** |
| Parallel Last (uni) | 18.2 | 14.8 | 仅训练方向提升 |

### 消融 — 关键发现
| 发现 | 证据 |
|------|------|
| 平行 > 单语 | Parallel Last >> Multilingual（+5 BLEU） |
| 末置 > 首置 | Parallel Last >> Parallel First（+9 BLEU） |
| 首置灾难性遗忘 | Parallel First 甚至低于 No Parallel |
| 无反向泛化 | uni 训练 En→X，X→En 无提升 |
| 双语信号量影响 | 更多平行数据 → 更好翻译 |

### 关键发现
- **平行数据在末期加入显著优于其他策略**——可能因为前期训练先建立了语言理解基础
- **LLM 不能自发泛化到反向翻译**：只训练 En→Zh 不会让 Zh→En 也变好
- **平行数据 > 等量单语数据**：证明对齐信号有额外价值
- **训练位置比训练量更重要**（Distributed < Last，尽管数据量相同）
- **灾难性遗忘**：将平行数据放在开始会"浪费"——模型后续训练会覆盖学到的对齐

## 亮点与洞察
- **"末置最优"**是一个简单但重要的发现——为多语言 LLM 训练提供了直接可用的策略
- **反向翻译不泛化**挑战了"LLM 内部有语言无关表示"的假设
- **控制实验设计**极其严谨，7 种对比全面覆盖可能的策略

## 局限性 / 可改进方向
- 仅在中等规模模型上验证（基于 Pythia/TinyLlama）
- 语言覆盖有限
- 改进方向：更大模型、更多语言对、与CLO等方法结合

## 相关工作与启发
- **vs CLO (Lee et al.)**：CLO 用 DPO 做跨语言迁移，本文用平行数据继续预训练——两者可互补
- **vs XLM/mBART**：encoder/encoder-decoder 模型的平行数据策略已成熟，本文将其扩展到 decoder-only

## 评分
- 新颖性: ⭐⭐⭐⭐ 系统性对比研究+多个重要发现
- 实验充分度: ⭐⭐⭐⭐⭐ 7种设置×多语言×多任务，极其充分
- 写作质量: ⭐⭐⭐⭐⭐ 实验设计严谨，结论清晰
- 价值: ⭐⭐⭐⭐⭐ 对多语言LLM训练有直接指导价值
