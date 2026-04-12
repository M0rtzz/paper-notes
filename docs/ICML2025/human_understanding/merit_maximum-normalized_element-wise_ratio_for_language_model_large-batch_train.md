---
title: >-
  [论文解读] MERIT: Maximum-normalized Element-wise Ratio for LM Large-batch Training
description: >-
  [ICML2025][人体理解][大批量训练] 识别了LLM大批量训练中"max attention logit急剧上升"的关键问题，提出MERIT优化器——用max-norm替代l2-norm计算trust ratio，并引入element-wise trust ratio约束局部权重结构，GPT-2 Medium在6K batch size下无性能退化。
tags:
  - ICML2025
  - 人体理解
  - 大批量训练
  - 优化器
  - 注意力logit
  - trust ratio
  - GPT-2
---

# MERIT: Maximum-normalized Element-wise Ratio for LM Large-batch Training

**会议**: ICML2025  
**arXiv**: [2508.20577](https://arxiv.org/abs/2508.20577)  
**代码**: [GitHub - MERIT](https://github.com/NUS-HPC-AI-Lab/MERIT)  
**领域**: human_understanding  
**关键词**: 大批量训练, 优化器, 注意力logit, trust ratio, GPT-2

## 一句话总结
识别了LLM大批量训练中"max attention logit急剧上升"的关键问题，提出MERIT优化器——用max-norm替代l2-norm计算trust ratio，并引入element-wise trust ratio约束局部权重结构，GPT-2 Medium在6K batch size下无性能退化。

## 研究背景与动机

### 大批量训练的困境
大批量可加速训练但导致泛化性能退化。AdamW在大batch下表现出max attention logit急剧上升，导致注意力分布过于尖锐。

### LAMB的局限
LAMB通过l2-norm trust ratio部分缓解了第一层的问题，但中间层仍存在。原因：l2-norm不能有效抑制query/key权重的最大值。且weight-wise trust ratio忽略了行/列间的结构关系。

### MERIT的核心改进
1. 用max-norm替代l2-norm计算trust ratio——更直接约束最大注意力logit
2. 引入element-wise trust ratio——关注局部权重结构而非全局平均

## 方法详解

### Max-norm Trust Ratio
传统LAMB: ratio = ||w||_2 / ||update||_2
MERIT: ratio = ||w||_max / ||update||_max
Max-norm直接约束权重的最大绝对值，阻止attention logit爆炸。

### Element-wise Trust Ratio
不是对整个权重矩阵算一个ratio，而是对每个元素或行/列分别计算ratio。这保留了权重内部的结构信息，避免了全局平均的信息损失。

### 结合策略
先用element-wise ratio缩放更新，再用max-norm ratio做全局约束。两层控制确保既有局部精细调整又有全局安全保障。

## 实验关键数据

### GPT-2训练（不同batch size）

| Batch Size | AdamW | LAMB | **MERIT** |
|-----------|-------|------|---------|
| 480 (标准) | 基线 | 基线 | **基线** |
| 2K | 退化 | 轻微退化 | **无退化** |
| 4K | 明显退化 | 退化 | **无退化** |
| 6K | 严重退化 | 明显退化 | **无退化** |

### GPT-2 Medium训练

| 优化器 | 6K batch训练质量 | 相比标准batch |
|--------|---------------|-----------|
| AdamW | 不可用 | 严重退化 |
| LAMB | 勉强可接受 | 退化 |
| **MERIT** | **可用** | **无退化** |

### Max Attention Logit分析

| 优化器 | 训练后max logit | 稳定性 |
|--------|---------------|--------|
| AdamW | 急剧增长 | 不稳定 |
| LAMB | 部分控制 | 中间层仍高 |
| **MERIT** | **全层控制** | **稳定** |

### 关键发现
1. Max attention logit是大batch退化的直接原因
2. Max-norm比l2-norm更有效抑制注意力爆炸
3. Element-wise比weight-wise提供更鲁棒的更新缩放
4. MERIT在GPT-2 Medium上首次实现6K batch无退化

## 亮点与洞察

1. 诊断精准："max attention logit"作为大batch退化的根因。
2. 解决方案极简：只改变norm类型和ratio粒度。
3. GPT-2 Medium 6K batch无退化是实际加速的重要突破。
4. 对LLM训练基础设施有直接工程价值。
5. 理论分析与实验高度一致。

## 局限性 / 可改进方向

1. 仅在GPT-2（小模型）上验证，更大模型待测试。
2. Element-wise ratio增加了内存开销。
3. 与更新的优化器（如SOAP/Adam-mini）的对比缺失。
4. 超大batch (>10K)的效果未探索。

## 相关工作与启发

- 与LAMB的关系：直接改进其trust ratio设计。
- 启发：可将max-norm思想推广到其他需要控制极值的优化场景。

## 评分
- 新颖性: 4.5/5 — 问题诊断+max-norm+element-wise
- 实验充分度: 4.0/5 — GPT-2多规模验证
- 写作质量: 4.5/5
- 价值: 4.5/5 — 直接加速LLM训练

## 补充

### Max-norm的数学直觉
l2-norm被大量小值元素稀释，无法约束个别极端值。max-norm直接监控最大绝对值，一旦某个权重超阈就拉回。

### 与最新优化器的关系
MERIT与SOAP/Adam-mini等新优化器正交，可以组合使用。
