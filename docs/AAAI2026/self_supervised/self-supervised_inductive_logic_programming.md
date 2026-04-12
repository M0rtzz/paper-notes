---
title: >-
  [论文解读] Self-Supervised Inductive Logic Programming
description: >-
  [AAAI 2026][自监督学习][Inductive Logic Programming] 提出 Self-Supervised ILP 新范式和 Poker 系统，通过在学习过程中自动生成正负例来替代人工标注负例和定制背景理论，实现从少量正例学习递归逻辑程序。
tags:
  - AAAI 2026
  - 自监督学习
  - Inductive Logic Programming
  - Meta-Interpretive Learning
  - predicate invention
  - grammar learning
---

# Self-Supervised Inductive Logic Programming

**会议**: AAAI 2026  
**arXiv**: [2507.16405](https://arxiv.org/abs/2507.16405)  
**代码**: [GitHub](https://github.com/stassa/aaai_26_experiments/)  
**领域**: self_supervised  
**关键词**: Inductive Logic Programming, Meta-Interpretive Learning, self-supervised learning, predicate invention, grammar learning  

## 一句话总结

提出 Self-Supervised ILP 新范式和 Poker 系统，通过在学习过程中自动生成正负例来替代人工标注负例和定制背景理论，实现从少量正例学习递归逻辑程序。

## 背景与动机

传统 ILP（归纳逻辑编程）要求用户手动提供：(1) 针对具体任务定制的背景理论 $B$；(2) 精心挑选的负例 $E^-$。这两项依赖专家知识，严重限制了 ILP 的实际应用。Meta-Interpretive Learning (MIL) 虽能从少量正例学习含递归和谓词发明的逻辑程序，但同样依赖上述人工标注。

## 核心问题

如何在**不提供负例**且仅使用**最大化通用的背景理论**的条件下，避免假设过度泛化？当背景理论足够通用以覆盖所有目标程序类时，缺少负例将导致无法区分目标语言与超集语言（如无法区分 $1^n0^n$ 与 $1^n0^m$）。

## 方法详解

### 整体框架

Poker 算法包含三个阶段：
1. **Generalise**：从正例 $E^+$ 和 SONF 背景理论构建初始假设集合 $T$
2. **Generate**：用 $T$ 作为生成器自动产生新未标注例（加入 $E^?$），并初始假设所有未标注例为负例
3. **Label**：通过矛盾检测迭代标注——对每个假定负例 $e^?$，从 $T$ 中移除接受它的假设；若剩余假设不再覆盖 $E^+$ 中某些正例，则 $e^?$ 重新标为正例

### 关键设计

**Second-Order Definite Normal Form (SONF)**：一种带约束的二阶元规则集，足以表达目标谓词的所有可能逻辑程序定义。以 Chomsky-Greibach Normal Form (C-GNF) 为例：

- Identity: $P(x,y) \leftarrow Q(x,y)$，约束 $target(P) \wedge (background(Q) \vee empty(Q))$
- Chain: $P(x,y) \leftarrow Q(x,z), R(z,y)$，约束 $P \neq Q \wedge (target(P) \vee invented(P))$

**矛盾检测机制**：若 $e_1, e_2$ 被假设集 $T$ 中同一子集接受，则假设 $e_1$ 正、$e_2$ 负的标注是矛盾的。通过移除接受 $e_2$ 的假设并检查是否仍覆盖正例来检测矛盾。

**理论保证**（Theorem 1）：Poker 返回正确假设的概率随未标注例数量**单调递增**。

## 实验关键数据

| 实验 | 系统 | k=0 | k=10 | k=50 | 趋势 |
|------|------|-----|------|------|------|
| CFL ($1^n0^n$) TPR | Poker | 1.0 | 1.0 | 1.0 | 稳定 |
| CFL ($1^n0^n$) TNR | Poker | ~0 | ↑ | ~1.0 | 随 k 递增 |
| CFL 所有 | Louise | 高 TPR | - | - | TNR 始终低（过泛化）|
| L-System 生成准确率 | Poker | 低 | ↑ | 高 | 随 k 递增 |
| L-System 假设大小 | Poker | 大 | ↓ | 小 | 随 k 递减 |

- Poker 在 6 种 CFL 和 4 种 L-System（Dragon/Hilbert/Koch/Sierpinski）上验证
- Louise 在无负例时始终过度泛化，TPR 高但 TNR 极低

## 亮点

- 首次形式化定义 Self-Supervised ILP 设定，填补 ILP 与自监督学习的空白
- SONF 概念优雅——用一组通用元规则替代针对每个任务定制的背景理论
- 自动生成正负例的矛盾检测机制简洁高效，有理论单调性保证
- 学到的逻辑程序既可用作判别器也可用作生成器

## 局限性

- SONF 的构造目前需要人工推导，尚无自动化方法
- 仅在语法学习（CFL 和 L-System）上验证，尚未扩展到其他 ILP 任务
- 自动生成例的数量 k 需要足够大才能保证正确性，效率可能受限
- 与 Popper 等现代 ILP 系统的公平对比受限（Popper 不支持无负例学习）

## 对比

| 系统 | 需要负例 | 通用背景理论 | 谓词发明 | 递归 | 自动生成例 |
|------|---------|-------------|---------|------|----------|
| Poker | ✗ | ✓ (SONF) | ✓ | ✓ | ✓ |
| Louise | ✗ | ✓ | ✓ | ✓ | ✗ |
| Popper | ✓ | ✗ | ✓ | ✓ | ✗ |
| DeepLog | ✗ | 部分 | ✓ | ✓ | ✗ |

## 启发

- "通过矛盾检测实现自监督"的思路可迁移到其他符号学习系统
- SONF 的思想——构造覆盖一类问题的最大通用背景——可用于自动化程序合成
- 自动生成训练样本在低资源逻辑推理任务中有广泛潜力

## 评分

⭐⭐⭐⭐ — 理论贡献突出，形式化优雅，但实验领域局限于语法学习
