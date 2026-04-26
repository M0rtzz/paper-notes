---
title: >-
  [论文解读] Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale
description: >-
  [NeurIPS 2025][语言模型行为阶段] 本文通过分析 1,400+ 个模型检查点在 110,000+ token 上的行为，发现自回归语言模型在训练过程中展现高度一致的行为阶段——预测概率依次过拟合到递增 n 的 n-gram 概率，且三个简单启发式（词频、n-gram 概率、语义相似度）可解释高达 98% 的模型行为方差，此规律跨架构（Transformer/Mamba/RWKV）、数据集和规模保持一致。
tags:
  - NeurIPS 2025
  - 语言模型行为阶段
  - n-gram概率
  - 语义相似度
  - 训练动态
  - 架构无关性
---

# Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale

**会议**: NeurIPS 2025  
**arXiv**: [2510.24963](https://arxiv.org/abs/2510.24963)  
**代码**: [GitHub](https://github.com/jmichaelov/lm-behavioral-phases)  
**领域**: LLM 预训练 / 可解释性  
**关键词**: 语言模型行为阶段, n-gram概率, 语义相似度, 训练动态, 架构无关性

## 一句话总结
本文通过分析 1,400+ 个模型检查点在 110,000+ token 上的行为，发现自回归语言模型在训练过程中展现高度一致的行为阶段——预测概率依次过拟合到递增 n 的 n-gram 概率，且三个简单启发式（词频、n-gram 概率、语义相似度）可解释高达 98% 的模型行为方差，此规律跨架构（Transformer/Mamba/RWKV）、数据集和规模保持一致。

## 研究背景与动机
1. **领域现状**: 语言模型通过 next-token prediction 训练，展现出语法生成、知识推理等涌现能力，但学习过程的规律尚不清楚。
2. **现有痛点**: 已有分析主要关注特定行为或子网络的突变，缺乏对模型整体行为的系统刻画。
3. **核心矛盾**: 是否存在不依赖模型细节（架构、规模、数据）的通用学习规律？
4. **本文目标**: 用简单启发式量化刻画语言模型在训练全程的行为变化。
5. **切入角度**: 聚焦三个启发式——词频（unigram）、n-gram 概率、上下文语义相似度。
6. **核心 idea**: 所有模型都经历相同的行为阶段：先过拟合低阶 n-gram，再逐步过拟合高阶 n-gram，同时与语义相似度的相关性在早期快速建立。

## 方法详解

### 整体框架
训练并收集 1,418 个模型检查点（Pythia/Mamba/RWKV 三种架构 × 多种规模 × 多个种子），在去污染评估集 NaWoCo 上计算模型 log-probability 与各启发式的相关性。进行 Pearson/Spearman 相关分析和回归分析。

### 关键设计
1. **Parc 模型**: 首批公开的 checkpointed Mamba-1 和 RWKV-4 模型，三种架构在相同 OpenWebText 数据上并行训练（相同序列、相同步数），每种 6 个种子、73 个检查点。使用相同 tokenizer 确保公平比较。
2. **NaWoCo 数据集**: 从 FineWeb 提取的 150,000+ 词在句子上下文中的评估集，确保单 token（所有模型通用）、非训练数据（通过 infini-gram 计数验证）、低毒性（< 0.1 概率），分为训练/验证/测试集。
3. **回归分析**: 用 unigram、2-5 gram log-probability 和 fastText 语义相似度（Wikipedia 和 Common Crawl 版本，均匀加权和 SGPT 加权）作为特征，回归预测模型 log-probability，计算 R² 解释方差比例。
4. **n-gram 计算**: 使用 infini-gram 工具在训练数据上计算词级 n-gram 概率，采用 Stupid Backoff 平滑。

### 损失函数 / 训练策略
- 纯分析工作，无训练损失设计
- 使用 Pearson 相关、Spearman 相关和 R² 回归分析
- 涵盖 14M 到 12B 参数规模（Pythia 系列包含完整规模范围）

## 实验关键数据

| 发现 | 细节 |
|------|------|
| 行为方差解释率 | 三个启发式解释高达 **98%** 模型 log-prob 方差 |
| 跨架构一致性 | Pythia/Mamba/RWKV 在相同步数的 Pearson r ≥ 0.93 |
| 行为阶段 | 依次过拟合 unigram → bigram → trigram → ... → 5-gram |
| 规模效应 | 更大模型与低阶 n-gram 的去相关更强 |

### 关键发现
- 所有模型（不论架构/规模/数据）展现相同的 n-gram 过拟合序列
- 语义相似度的峰值与 unigram（CommonCrawl 版）或 trigram（Wikipedia 版）同步
- 随机种子间的差异极小（置信区间几乎不可见）
- 更大模型能力更强，可从低阶 n-gram 中解脱出来学习更复杂的关系

### Parc模型系列详情

| 架构 | 参数量 | 训练数据 | 检查点数 | 种子数 |
|------|--------|---------|---------|-------|
| Pythia | 14M-12B | The Pile | 143 | 1 |
| Mamba-1 | ~160M | OpenWebText | 73 | 6 |
| RWKV-4 | ~160M | OpenWebText | 73 | 6 |

### 行为阶段时间线
- 阶段1 (0-5K步): unigram过拟合，模型学习词频分布
- 阶段2 (5K-20K步): bigram过拟合，开始学习局部依赖
- 阶段3 (20K-100K步): trigram+过拟合，学习更长范围依赖
- 阶段4 (100K+步): 高阶n-gram去相关，开始学习语义关系


## 亮点与洞察
- 揭示了深度学习中罕见的跨架构通用规律
- 三个极简启发式解释 98% 方差——暗示语言模型本质上在学习这三种模式
- Parc 模型和 NaWoCo 数据集是重要公开资源
- 对理解 scaling law 和涌现行为提供了新视角

## 局限与展望
- 仅分析词级行为，未扩展到句子/段落级的语义行为分析。
- 简单启发式可能无法解释更复杂的推理行为（如多步推理、规划）。
- 未分析指令微调或RLHF后的行为阶段变化，对齐训练可能改变阶段顺序。
- 因果机制（为什么会出现这些阶段）尚未解释，仅是观察性发现。
- 98%方差解释率可能高估了启发式的重要性，因为语言本身具有很强的统计规律性。
- 未探索不同训练数据组成（如代码数据比例）对行为阶段的影响。
- Mamba和RWKV模型规模较小，更大规模的非Transformer架构上的行为可能不同。
- NaWoCo评估集的构建可能引入选择偏差——仅选择单token词可能不代表更复杂的词类。

## 相关工作与启发
- **vs Chang et al. 2024**: 仅在 GPT-2 上发现 n-gram 过拟合，本文扩展到多架构/多规模
- **vs Voita et al. 2024**: 分析 n-gram 专用神经元，本文从行为层面分析
- **vs Schaeffer et al. 2023**: 认为涌现是度量伪影，本文从不同角度分析训练动态


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。
- 可以考虑将该方法与强化学习结合，实现端到端的优化。
- 跨领域迁移是一个值得探索的方向——方法的通用性需要更多验证。
- 对于边缘计算和移动端部署场景，方法的轻量化版本值得研究。
- 长期评估和用户研究可以提供更全面的方法评价。
- 与人类专家的对比分析可以更好地定位方法的优劣势。
- 在对抗场景下的鲁棒性测试是实际部署前的必要步骤。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 跨架构通用行为阶段的发现是重要科学贡献
- 实验充分度: ⭐⭐⭐⭐⭐ 1,400+ 检查点、3 种架构、多规模的超大规模实验
- 写作质量: ⭐⭐⭐⭐ 分析严谨，可视化清晰
- 价值: ⭐⭐⭐⭐⭐ 对理解语言模型学习机制有根本性意义

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] Disaggregation Reveals Hidden Training Dynamics: The Case of Agreement Attraction](disaggregation_reveals_hidden_training_dynamics_the_case_of_agreement_attraction.md)
- [\[NeurIPS 2025\] Nemotron-CLIMB: CLustering-based Iterative Data Mixture Bootstrapping for Language Model Pre-training](nemotron-climb_clustering-based_iterative_data_mixture_bootstrapping_for_languag.md)
- [\[NeurIPS 2025\] Memory Mosaics at Scale](memory_mosaics_at_scale.md)
- [\[NeurIPS 2025\] Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training](through_the_river_understanding_the_benefit_of_schedule-free_methods_for_languag.md)
- [\[NeurIPS 2025\] Final-Model-Only Data Attribution with a Unifying View of Gradient-Based Methods](final-model-only_data_attribution_with_a_unifying_view_of_gradient-based_methods.md)

<!-- RELATED:END -->
