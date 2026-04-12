---
title: >-
  [论文解读] Scaling Generalist Data-Analytic Agents
description: >-
  [ICLR 2026][人体理解][数据分析] 提出DataMind——可扩展的数据分析Agent训练pipeline：(1)细粒度18类任务分类法+递归由简到难任务组合→多样高质量合成query,(2)知识增强轨迹采样+自一致性过滤,(3)SFT+RL动态混合训练目标,(4)内存友好的稳定多轮代码rollout框架→DataMind-14B在多个基准上SOTA(71.16%,超越DeepSeek-V3.1和GPT-5)。
tags:
  - ICLR 2026
  - 人体理解
  - 数据分析
  - Agent训练
  - 多轮代码执行
  - 课程合成
  - SFT+RL
---

# Scaling Generalist Data-Analytic Agents

**会议**: ICLR 2026  
**arXiv**: [2509.25084](https://arxiv.org/abs/2509.25084)  
**代码**: [GitHub](https://github.com/zjunlp/DataMind)  
**领域**: 数据分析Agent/LLM  
**关键词**: 数据分析, Agent训练, 多轮代码执行, 课程合成, SFT+RL

## 一句话总结

提出DataMind——可扩展的数据分析Agent训练pipeline：(1)细粒度18类任务分类法+递归由简到难任务组合→多样高质量合成query,(2)知识增强轨迹采样+自一致性过滤,(3)SFT+RL动态混合训练目标,(4)内存友好的稳定多轮代码rollout框架→DataMind-14B在多个基准上SOTA(71.16%,超越DeepSeek-V3.1和GPT-5)。

## 研究背景与动机

1. **领域现状**：数据分析Agent→处理/建模/计算数据→发现洞察→支持决策。现有方法→主要用闭源模型+prompt工程+预定义workflow+多Agent脚手架。

2. **现有痛点**：
   - (1) 开源模型→仅能做简单表格理解→对多样格式/大规模数据文件+长程多步推理→崩溃
   - (2) 训练数据不足→公开数据分析基准→仅测试集→缺轨迹标注
   - (3) Agent长程训练不稳定→SFT和RL如何分配不清
   - (4) 多轮代码执行→内存管理复杂→并行rollout+有限内存→不稳定

3. **切入角度**：全面的数据合成+Agent训练+rollout工程。

## 方法详解

### 数据合成

- 从互联网/开放社区收集多种格式数据文件
- 18类细粒度任务分类→递归由简到难组合→增加多样性和难度
- 知识增强轨迹采样→改善有效性和可靠性
- 自一致性过滤+规则检查→保证质量
- 最终：DataMind-12K高质量训练集

### 训练策略

- SFT损失+RL损失→动态系数调度
- 早期→SFT权重高(exploitation)→后期→RL权重高(exploration)
- 平衡利用和探索→稳定训练

### rollout框架

- 异步Agent生成和代码执行
- 分块式代码维护→降低峰值内存
- 隔离沙盒+执行时间/内存限制→稳定

## 实验关键数据

### 多个数据分析基准

| 模型 | 平均分 | 类型 |
|------|--------|------|
| GPT-5 | ~68% | 闭源 |
| DeepSeek-V3.1 | ~70% | 开源(大) |
| **DataMind-14B** | **71.16%** | 开源(训练后) |
| **DataMind-7B** | **68.10%** | 开源最强 |

### 关键洞察(来自消融)

1. 自一致性过滤 > 最佳轨迹选择→因为鼓励多样思考模式
2. SFT损失→可以稳定RL→但过多也导致不稳定→平衡关键
3. RL→可以缩小不同基座模型的差距→但不能逆转顺序

### 关键发现

- 14B超越GPT-5→在数据分析上→说明domain-specific训练>通用大模型
- 12K样本→足够训练SOTA数据分析Agent→质量>数量
- 多轮rollout→最大技术挑战→稳定性是关键

## 亮点与洞察

- **14B超越GPT-5**→证明specialized training比scale更重要(在此任务上)。
- **完整的pipeline**→从数据合成→训练→rollout→部署→端到端。
- **实践洞察**→SFT和RL的关系/自一致性过滤的价值→对Agent训练社区有直接指导。
- **18类任务分类法**→首次对数据分析任务进行细粒度分类→为后续研究提供框架。


## 局限性 / 可改进方向

- This paper introduces DataMind, a scalable data synthesis and agent training recipe designed to build generalist data-analytic agents.

- Built on DataMind, we curate DataMind-12K, a high-quality training set that spans diverse task categories and data file formats for data-analytic tasks.

- Trained on DataMind-12K, we obtain DataMind-7B and 14B, two advanced data-analytic agents with superior performance on multiple benchmarks compared with various proprietary and open-source baselines.

- We also incorporate some empirical insights gained from our exploratory trials into the analysis experiments, aiming to provide actionable insights about agentic training for the community.

- Ethics Statement

This study was conducted in full compliance with established ethical standards and research best practices.


## 相关工作与启发

- 本文提出的方法为该研究方向提供了新的视角和解决思路。

- 核心模块设计可以迁移到相关任务中，具有较好的通用性。

- 可以作为该领域后续改进工作的有力基线。

## 评分

- 新颖性: ⭐⭐⭐⭐ 完整的数据分析Agent训练pipeline
- 实验充分度: ⭐⭐⭐⭐⭐ 多基准+vs GPT-5+消融+洞察
- 写作质量: ⭐⭐⭐⭐ 全面但清晰
- 价值: ⭐⭐⭐⭐⭐ 对开源数据分析Agent有范式级贡献
