---
title: >-
  [论文解读] Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale
description: >-
  [NeurIPS 2025][behavioral phases] 在 Transformer、Mamba、RWKV 三种架构，OpenWebText 和 The Pile 两种数据集，14M-12B 参数规模上系统分析 1400+ 检查点，发现所有自回归语言模型在预训练中展现高度一致的行为阶段——词级预测最多 98% 方差可由 unigram 频率、n-gram 概率和语义相似度三类简单启发式解释。
tags:
  - NeurIPS 2025
  - behavioral phases
  - n-gram
  - semantic similarity
  - pretraining dynamics
  - cross-architecture
---

# Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale

**会议**: NeurIPS 2025  
**arXiv**: [2510.24963](https://arxiv.org/abs/2510.24963)  
**代码**: [https://github.com/jmichaelov/lm-behavioral-phases](https://github.com/jmichaelov/lm-behavioral-phases)  
**领域**: 语言模型预训练分析  
**关键词**: behavioral phases, n-gram, semantic similarity, pretraining dynamics, cross-architecture

## 一句话总结

在 Transformer、Mamba、RWKV 三种架构，OpenWebText 和 The Pile 两种数据集，14M-12B 参数规模上系统分析 1400+ 检查点，发现所有自回归语言模型在预训练中展现高度一致的行为阶段——词级预测最多 98% 方差可由 unigram 频率、n-gram 概率和语义相似度三类简单启发式解释。

## 研究背景与动机

语言模型训练通常被视为"黑箱能力增长"过程，但模型实际经历了怎样的学习轨迹？已有工作发现：

-    模型预测与 n-gram 概率的相关性在训练中发生变化，先贴合低阶 n-gram 再贴合高阶 n-gram
-    模型预测与上下文语义相似度存在相关性
-    训练中出现突然的行为转变（如 induction heads 的涌现）

但这些发现多限于单一架构（Transformer）和特定规模。核心问题：**语言模型的学习阶段是架构/数据/规模的偶然产物，还是自回归建模任务本身的必然？**

## 方法详解

### 整体框架

论文围绕两个实验展开：实验 1 计算简单启发式与模型预测的 Pearson 相关系数随训练步数的变化；实验 2 用线性回归量化各启发式对模型行为的独立贡献和解释力。

### 关键设计

1.    **大规模 checkpoint 行为分析**：

    -    功能：覆盖 1418 个模型实例（含所有 seed、架构、步数），在 NaWoCo 数据集（>150K 词）上计算每个 checkpoint 的词级 log-probability
    -    核心思路：训练 Parc 模型（6 seed × 3 架构 × 73 checkpoints），与 Pythia 系列（14M-12B）和 Open-GPT2 对齐分析
    -    设计动机：跨架构（Transformer/Mamba/RWKV）训练在完全相同的数据上，严格控制变量

2.    **三类行为解释变量**：

    -    功能：用 unigram 概率（词频）、n-gram 概率（1-5阶）和上下文语义相似度（fastText 余弦相似度）解释模型 log-probability
    -    核心思路：通过 z-标准化后的多元线性回归分离各变量的独立贡献
    -    设计动机：这些启发式是自回归任务的自然统计量——高频词本就更可能出现，n-gram 概率反映局部上下文统计，语义相似度反映主题连贯性

3.    **Behavioral Phases 发现**：

    -    功能：识别三个一致的行为阶段
    -    **Phase 1**：unigram coefficient 急剧上升至峰值，语义相似度 coefficient 同步上升，5-gram coefficient 微弱或为负——模型首先学会词频偏好
    -    **Phase 2**：unigram coefficient 下降，5-gram coefficient 急剧上升——模型从依赖词频转向依赖上下文
    -    **Phase 3**：各 coefficient 趋于稳定——行为成熟

### 损失函数 / 训练策略

Parc 模型使用标准自回归 next-token prediction 训练，batch size 512，序列长度 1024，4000 步。三种架构使用相同 tokenizer 和相同数据顺序，仅架构不同。

## 实验关键数据

### 主实验（表格）

| 模型 | 参数量 | R² (峰值) | R² (最终) | unigram peak step | Phase 2 onset |
|------|--------|----------|----------|-------------------|--------------|
| Pythia-14M | 14M | 0.98 | ~0.78 | ~step 128 | ~step 256 |
| Pythia-160M | 160M | 0.97 | ~0.65 | ~step 32 | ~step 128 |
| Pythia-1.4B | 1.4B | 0.95 | ~0.55 | ~step 16 | ~step 64 |
| Pythia-12B | 12B | 0.93 | ~0.50 | ~step 8 | ~step 32 |
| Parc-Pythia | 160M | 0.97 | ~0.70 | ~step 40 | ~step 160 |
| Parc-Mamba | 130M | 0.96 | ~0.68 | ~step 40 | ~step 160 |
| Parc-RWKV | 169M | 0.96 | ~0.69 | ~step 40 | ~step 160 |

跨架构的行为阶段时间高度一致：Parc-Pythia/Mamba/RWKV 在每步 ≥80 时的 Pearson 相关 r≥0.93（不仅跨 seed，也跨架构）。

### 消融实验

-    匹配 vs 不匹配 n-gram 语料：使用模型训练数据计算的 n-gram 比使用其他语料略好，但模式不变
-    Wikipedia-based vs Common Crawl-based fastText：Common Crawl 版与 unigram 相关更高（r=0.67-0.69），Wikipedia 版与高阶 n-gram 时间点更同步
-    SGPT 加权 vs 均匀加权上下文向量：影响极小

### 关键发现

-    **模型越大，越快脱离低阶 n-gram 偏好**：12B 模型在 Phase 3 时 unigram coefficient 最低，5-gram 最高
-    **小模型永远更依赖词频**：14M 模型即使训练完成，unigram coefficient 仍较高——可能受限于容量
-    **三个启发式始终解释 >50% 方差**：除了训练最初几步外，R² 不低于 0.5
-    **相位时间由架构和数据共同决定**：但 Phase 存在性本身是普适的

## 亮点与洞察

-    **基础发现**：自回归语言建模任务本身——而非架构细节——是行为阶段的决定因素
-    **跨架构一致性惊人**：Transformer、Mamba、RWKV 在相同数据上的行为轨迹几乎重合
-    **简单启发式的解释力**：三个变量解释最高 98% 方差——语言模型的词级行为远比想象的简单
-    **实用含义**：行为阶段可作为预训练诊断信号，Phase 2→3 的转变可能标志着模型开始习得超越 n-gram 的能力

## 局限性 / 可改进方向

-    分析限于 n∈{1,2,3,4,5} 和静态词向量——模型可能对更高阶 n-gram 和上下文向量敏感
-    主要基于英文语料——跨语言泛化未验证
-    "阶段一致"不等于"能力一致"——不同架构在下游任务上的表现差异未解释
-    回归仍有 ~50% 方差未解释（对大模型）——大模型学到了什么超越简单启发式的东西？
-    因果机制未知——模型是否"必须"经历这些阶段，还是特定优化器的偶然轨迹？

## 相关工作与启发

-    **Chang et al. (2024)**：发现 GPT-2 的 n-gram 相位变化；本文将其推广到跨架构+跨规模+跨数据
-    **Belrose et al. (2024)**：用 KL 散度分析 Pythia 与 n-gram 的距离变化；本文用回归方法分离各因素独立贡献
-    **Nguyen (2024)**：用 n-gram 规则匹配模型 top 预测（准确率 68-79%）；本文提供了连续值的方差解释框架
-    启发：行为阶段可用于课程学习和蒸馏阶段划分——在特定阶段匹配不同的知识蒸馏策略

## 评分

-    新颖性: ⭐⭐⭐⭐ 跨架构行为阶段的首次系统验证
-    实验充分度: ⭐⭐⭐⭐⭐ 1400+ checkpoints 的大规模分析
-    写作质量: ⭐⭐⭐⭐ 分析层次清晰
-    价值: ⭐⭐⭐⭐ 对预训练动态理解有基础性贡献
