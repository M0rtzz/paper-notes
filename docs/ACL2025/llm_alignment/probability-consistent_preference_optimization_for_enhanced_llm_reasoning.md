---
title: >-
  [论文解读] Probability-Consistent Preference Optimization for Enhanced LLM Reasoning
description: >-
  [ACL 2025][LLM对齐][偏好优化] 提出 PCPO（Probability-Consistent Preference Optimization），在偏好对选择时同时考虑答案正确性和 token 级概率一致性（用 Levenshtein 距离过滤+概率一致性评分），并在 DPO 损失中按一致性加权，在 GSM8K/MATH-500/Olympiadbench 上一致超越标准 DPO 和 ScPO。
tags:
  - ACL 2025
  - LLM对齐
  - 偏好优化
  - Token概率一致性
  - DPO
  - 数学推理
  - Levenshtein距离
---

# Probability-Consistent Preference Optimization for Enhanced LLM Reasoning

**会议**: ACL 2025  
**arXiv**: [2505.23540](https://arxiv.org/abs/2505.23540)  
**代码**: https://github.com/YunqiaoYang/PCPO (有)  
**领域**: LLM对齐 / 推理  
**关键词**: 偏好优化, Token概率一致性, DPO, 数学推理, Levenshtein距离

## 一句话总结
提出 PCPO（Probability-Consistent Preference Optimization），在偏好对选择时同时考虑答案正确性和 token 级概率一致性（用 Levenshtein 距离过滤+概率一致性评分），并在 DPO 损失中按一致性加权，在 GSM8K/MATH-500/Olympiadbench 上一致超越标准 DPO 和 ScPO。

## 研究背景与动机

**领域现状**：偏好优化（DPO/RLHF）已广泛用于 LLM 对齐。在数学推理中，常用方法是从模型采样多个回答，正确的做 chosen、错误的做 rejected。
**现有痛点**：仅看最终答案选偏好对忽略了推理过程的质量——两个都错的回答，推理链质量可能天差地别；两个表面相似的回答（Levenshtein 距离小），其 token 概率分布可能揭示模型对推理步骤的内在不确定性。
**核心矛盾**：答案正确 ≠ 推理可靠。模型可能通过"碰运气"得到正确答案但推理链不一致。
**本文要解决什么**：如何选择更高质量的偏好对，并在训练中利用概率信息？
**切入角度**：用 token 级概率一致性度量推理链的"内在逻辑连贯性"。
**核心 idea**：Levenshtein 距离过滤→token 概率一致性评分→加权 DPO 损失。

## 方法详解

### 关键设计

1. **Levenshtein 距离过滤**：过滤掉表面差异太小的偏好对（难以区分的对）

2. **Token 概率一致性评分**：

    - 对每个 token 计算 $c_t = p(t) \cdot \mathbb{1}[t = \arg\max]$
    - 聚合为 pair-weighted score $s_w$
    - 概率一致性高 = 模型对每步推理都很"确信"且一致

3. **加权 DPO 损失**：按概率一致性评分给偏好对加权，一致性更高的对获得更大梯度

## 实验关键数据

### 主实验（Llama-3-8B）

| 方法 | GSM8K | MATH-500 | Olympiadbench | AMC23 |
|------|-------|----------|---------------|-------|
| IRPO | 81.1 | 30.6 | 6.7 | 0 |
| ScPO | 81.6 | 32.2 | 7.9 | 5.0 |
| **PCPO** | **82.8** | **33.2** | **9.5** | **10.0** |

### 关键发现
- **极难任务提升最大**：AMC23 从 0/5.0→10.0，说明概率一致性在候选质量都不高时更能区分
- **概率一致性比 PRM 更有效**区分表面相似的回答
- **可泛化到 RPO、IPO、ORPO、TDPO** 等多种偏好优化变体
- 计算开销增加约 15% GPU hours（概率计算）

## 亮点与洞察
- **Token 概率一致性捕捉"推理信心"**：这是比答案正确性更深层的信号
- **Levenshtein 距离做粗筛**：简单有效地过滤低质量偏好对

## 局限性 / 可改进方向
- 需要标准答案做偏好选择
- 额外 15% 计算开销
- 仅在数学推理上验证

## 评分
- 新颖性: ⭐⭐⭐⭐ Token概率一致性作为偏好质量信号很新
- 实验充分度: ⭐⭐⭐⭐ 多模型多benchmark+泛化到多种PO变体
- 写作质量: ⭐⭐⭐⭐ 方法阐述清晰
- 价值: ⭐⭐⭐⭐ 对偏好优化实践有直接指导
