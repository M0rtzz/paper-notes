---
description: "【论文笔记】Chameleon: A Flexible Data-mixing Framework for LM Pretraining and Finetuning 论文解读 | ICML2025 | arXiv 2505.24844 | 数据混合 | 提出Chameleon框架，用kernel ridge leverage scores在学习的嵌入空间中量化域重要性，实现高效的数据混合权重计算，可在预训练/微调/域变化三种场景下工作，且无需重新训练代理模型。"
tags:
  - ICML2025
---

# Chameleon: A Flexible Data-mixing Framework for LM Pretraining and Finetuning

**会议**: ICML2025  
**arXiv**: [2505.24844](https://arxiv.org/abs/2505.24844)  
**代码**: [GitHub - Chameleon](https://github.com/LIONS-EPFL/Chameleon)  
**领域**: llm_nlp  
**关键词**: 数据混合, 域重加权, leverage scores, 预训练, 微调

## 一句话总结
提出Chameleon框架，用kernel ridge leverage scores在学习的嵌入空间中量化域重要性，实现高效的数据混合权重计算，可在预训练/微调/域变化三种场景下工作，且无需重新训练代理模型。

## 研究背景与动机

### 数据混合的重要性
预训练LLM的数据混合比例显著影响泛化性能。

### 现有方法的成本问题
- DoReMi/DoGE用代理模型推导权重，计算昂贵
- 域变化时需要重新训练代理模型
- 不适配微调场景

### Chameleon的目标
1. 降低混合权重计算成本
2. 适应域变化而无需重训代理
3. 统一处理预训练和微调

## 方法详解

### 核心：Leverage Scores
1. 构建域嵌入的亲和矩阵
2. 从核岭回归导出leverage scores
3. Leverage scores量化每个域对整体嵌入空间的独特贡献
4. 高leverage score的域获得更高混合权重

### 三种场景
- **预训练**：在域嵌入上直接计算权重
- **域变化**：计算新域的嵌入，无需重训代理
- **微调**：同样框架适用于微调场景的域重加权

## 实验关键数据

### 预训练域重加权

| 方法 | 计算成本 | 平均困惑度改善 |
|------|---------|-------------|
| 均匀混合 | 无 | 基线 |
| DoReMi | 高(需代理模型) | 显著 |
| **Chameleon** | **低(无代理)** | **相当或更好** |

### 域变化适应性

| 场景 | DoReMi | Chameleon |
|------|--------|----------|
| 新域引入后 | 需重训代理 | **直接计算新嵌入** |
| Few-shot推理 | 退化 | **保持** |

### 微调域重加权

| 策略 | 测试困惑度 |
|------|----------|
| 均匀微调 | 基线 |
| **Chameleon微调** | **所有域一致改善** |

### 关键发现
1. Leverage scores有效量化域的独特贡献
2. 无需代理模型大幅降低计算成本
3. 对新域的适应完全免训练
4. 预训练和微调场景统一处理

## 亮点与洞察

1. Leverage scores的使用在数据混合中很新颖——将统计学工具引入LLM训练。
2. "无需代理模型"是对DoReMi的根本性简化。
3. 域变化无需重训是最大的实用优势。
4. 预训练+微调+域变化三种场景的统一框架。

## 局限性 / 可改进方向

1. 嵌入空间的选择影响leverage scores质量。
2. 在超大规模(1000+域)下的可扩展性未验证。
3. 与更新的数据选择方法(如DSIR)的对比不够。
4. 核函数的选择是额外超参。

## 相关工作与启发

- 与DoReMi/DoGE的关系：同目标但无需代理模型。
- 与Data Pruning的区别：本文做域级重加权而非样本级筛选。
- 启发：Leverage scores可用于其他需要数据重加权的ML任务。

## 评分
- 新颖性: 4.5/5 — leverage scores在数据混合中的首次应用
- 实验充分度: 4.0/5 — 三种场景验证
- 写作质量: 4.5/5
- 价值: 4.5/5 — 大幅降低数据混合的工程成本

## 补充分析

### Leverage Scores的统计学含义
高leverage score的域在嵌入空间中占据独特位置，对回归模型贡献大。低leverage的域在其他域的凸包内，信息冗余。

### 与DoReMi的计算成本对比
DoReMi需要训练代理模型（过程本身就是一次完整LM训练），Chameleon只需计算域嵌入的亲和矩阵+求解线性方程，几分钟即可完成。
