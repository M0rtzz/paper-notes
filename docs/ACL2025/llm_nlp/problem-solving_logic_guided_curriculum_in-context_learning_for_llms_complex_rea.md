---
title: >-
  [论文解读] Problem-Solving Logic Guided Curriculum ICL for LLMs Complex Reasoning
description: >-
  [ACL 2025][LLM/NLP][in-context learning] 提出问题解决逻辑引导的课程式 ICL，基于 QDMR 分析解题步骤结构来选择和排序 few-shot 示例（按步骤数从易到难），在多个复杂推理基准上超越现有 ICL 方法。
tags:
  - ACL 2025
  - LLM/NLP
  - in-context learning
  - curriculum learning
  - QDMR
  - demonstration selection
  - reasoning
---

# Problem-Solving Logic Guided Curriculum ICL for LLMs Complex Reasoning

**会议**: ACL 2025  
**arXiv**: [2502.15401](https://arxiv.org/abs/2502.15401)  
**代码**: https://github.com/maxuetao/CurriculumICL  
**领域**: LLM/NLP  
**关键词**: in-context learning, curriculum learning, QDMR, demonstration selection, reasoning

## 一句话总结
提出问题解决逻辑引导的课程式 ICL，基于 QDMR 分析解题步骤结构来选择和排序 few-shot 示例（按步骤数从易到难），在多个复杂推理基准上超越现有 ICL 方法。

## 研究背景与动机

**领域现状**：ICL 通过 few-shot 示例增强 LLM 推理能力，关键在于示例选择和排序。
**现有痛点**：现有方法依赖文本相似度或困惑度等表面特征，无法反映解题逻辑联系。
**核心矛盾**：如何度量解题过程相似度而非文本相似度？
**本文要解决什么？** 用 QDMR 分析的解题逻辑来选择和排序示例。
**切入角度**：QDMR 将复杂问题分解为操作符序列（13种），即解题逻辑。
**核心idea一句话**：选解题逻辑相似的示例 + 按步骤数从易到难排序 = 课程式 ICL。

## 方法详解

### 整体框架
训练解题逻辑分析模型（基于 BREAK 数据集微调）-> 分析查询和候选的 QDMR 操作符序列 -> 按逻辑相似度选择 -> 按步骤数从易到难排序 -> 构建 ICL prompt。

### 关键设计

1. **解题逻辑提取**

    - 微调 LM 自动分析 QDMR 操作符序列（SELECT/FILTER/AGGREGATE 等 13 种）
    - 设计动机：操作符序列比文本特征更能反映解题过程

2. **基于逻辑的示例选择**

    - 计算查询与候选的操作符序列相似度
    - 设计动机：解题逻辑相似的示例更有助于学习解题模式

3. **课程排序**

    - 难度 = 操作符序列长度，从易到难排列
    - 设计动机：遵循课程学习原则

## 实验关键数据

### 主实验 -- 5 个基准平均
| 方法 | 平均提升 |
|------|--------|
| Random ICL | 基线 |
| 相似度选择 | +2.8% |
| **Curriculum ICL** | **+5.5%** |

### 消融
| 配置 | 提升 | 说明 |
|------|------|------|
| 逻辑选择+随机排序 | +4.0% | 选择有效但排序也重要 |
| 逻辑选择+难到易 | +3.5% | 易到难优于难到易 |
| **逻辑选择+易到难** | **+5.5%** | 完整课程式最优 |

### 关键发现
- 解题逻辑比文本相似度更有效（+2.7%）
- 课程排序有显著贡献（+1.5%）
- 易到难优于难到易，符合课程学习理论

## 亮点与洞察
- QDMR 用于 ICL 示例选择是优雅的跨领域迁移
- 课程学习在 ICL 中的应用为 prompt 工程提供理论指导

## 局限性 / 可改进方向
- QDMR 分析模型需额外训练
- 改进方向：更丰富的问题分解表示

## 相关工作与启发
- **vs 相似度选择**：表面相似度不如解题逻辑
- **vs LIMO**：LIMO 证明少量示例足够，本文优化示例质量

## 评分
- 新颖性: ⭐⭐⭐⭐ QDMR+课程学习+ICL 新颖结合
- 实验充分度: ⭐⭐⭐⭐ 5 数据集+消融
- 写作质量: ⭐⭐⭐⭐ 动机清晰
- 价值: ⭐⭐⭐⭐ 对 ICL 策略有实用指导
