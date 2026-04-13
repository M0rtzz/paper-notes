---
title: >-
  [论文解读] Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study
description: >-
  [ICLR 2026][人体理解][安全子空间] 通过4个系统实验(权重投影/正交补/更新相似度/激活空间)在5个LLM上证明安全对齐信息与通用学习在线性空间中不可分离——放大安全行为的子空间同时放大有用行为,有害更新与安全更新的相似性并非最高→基于线性子空间的安全防御策略面临根本性限制。
tags:
  - ICLR 2026
  - 人体理解
  - 安全子空间
  - 微调攻击
  - 线性可分性
  - 权重空间
  - 激活空间
---

# Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study

**会议**: ICLR 2026  
**arXiv**: [2505.14185](https://arxiv.org/abs/2505.14185)  
**代码**: [GitHub](https://github.com/CERT-Lab/safety-subspaces)  
**领域**: LLM安全/对齐  
**关键词**: 安全子空间, 微调攻击, 线性可分性, 权重空间, 激活空间

## 一句话总结

通过4个系统实验(权重投影/正交补/更新相似度/激活空间)在5个LLM上证明安全对齐信息与通用学习在线性空间中不可分离——放大安全行为的子空间同时放大有用行为,有害更新与安全更新的相似性并非最高→基于线性子空间的安全防御策略面临根本性限制。

## 研究背景与动机

**领域现状**：LLM安全对齐→脆弱→微调(即使良性数据)可破坏安全性。学界假设安全信息编码在权重空间的可辨识线性方向→可隔离/保护。

**现有痛点**：
   - (1) 安全子空间假说→被用于设计防御(投影/过滤)→但是否成立未验证
   - (2) 如果安全和有用的学习信号纠缠→投影式防御→删安全同时删有用→性能代价
   - (3) 多数防御仅在特定模型/数据上验证→缺少系统性cross-model研究
   - (4) 权重空间vs激活空间→两个角度都需要检验

**切入角度**：不提出新防御→而是系统验证"安全子空间可否线性隔离"这一基础假设。

## 方法详解

### 4个实验

**实验1: 有害/有用更新投影到"安全子空间"**
- 安全子空间Δ_A/Δ_S→投影有害更新和有用更新→比较表达能力
- 结果：有害更新在安全子空间中并不比有用更新更有表达力→子空间不安全特异

**实验2: 正交补去除**
- 将更新投影到安全子空间的正交补→期望去除有害分量
- 结果：有害分量未被选择性去除→有用分量同等受损→不可分离

**实验3: 更新间两两相似度**
- 比较(有害,安全)/(有用,安全)/(有害,有用)的子空间相似度
- 预期：(有害,安全)应最相似→因为都涉及安全
- 结果：(有害,安全)相似度并非最高→有时最低→反直觉

**实验4: 激活空间分析**
- 有害提示vs安全提示→在激活空间中是否占据不同区域？
- 结果：大幅重叠→无法线性分离

### 模型覆盖

- 5个LLM: Llama-3.1-8B, Llama-3.2-3B, Qwen-2.5-7B等

## 实验关键数据

### 所有4个实验一致结论:不可分离

| 实验 | 预期(如果可分) | 实际观察 |
|------|------------|---------|
| 投影表达力 | 有害>有用 | ≈相等 |
| 正交补去除 | 有害被去除 | 两者同等受损 |
| 更新相似度 | (害,安)最高 | 有时最低 |
| 激活重叠 | 不重叠 | 大幅重叠 |

### 5个模型一致

- 不是某个模型的特殊性→是普遍现象

### 关键发现

- 安全对齐与通用学习**深度纠缠**→不在独立线性子空间
- 子空间防御→必然在删安全的同时删有用→两难
- 这解释了为什么微调(即使良性)也能轻易破坏安全→因为不可分

## 亮点与洞察

- **"负面结果的价值"**：证明了一个流行假设是错的→比提出又一个防御更有影响→指导未来方向。
- **"安全和有用共享子空间"**：不是bug→是LLM的根本性质→安全行为就是通用能力的一部分。
- **对防御方向的启示**：线性投影/过滤→注定有根本限制→需要非线性/更复杂的方案。
- **激活空间的确认**：不只是权重空间→激活空间也不可分→排除了所有线性内省方案。


## 局限性 / 可改进方向

- This work set out to investigate how safety alignment is encoded in LLMs and whether it can be isolated in weight or activation space.

- Our findings challenge the common assumption that alignment or safety-specific updates correspond to unique “safety subspaces”.

- Subspaces with strong behavioral impact are not unique to safety; rather, they amplify both utility and harmfulness, indicating that safety is deeply entangled with general learning.

- Similarly, harmful and useful prompts activate overlapping regions of activation space, providing no evidence for a distinct safety subspace.

- Together, these results establish that safety alignment is not linearly separable in LLMs.


## 相关工作与启发

- 本文提出的方法为该研究方向提供了新的视角和解决思路。

- 核心模块设计可以迁移到相关任务中，具有较好的通用性。

- 可以作为该领域后续改进工作的有力基线。

## 评分

- 新颖性: ⭐⭐⭐⭐ 系统性否定安全子空间假说
- 实验充分度: ⭐⭐⭐⭐⭐ 4个实验×5个LLM→极其系统
- 写作质量: ⭐⭐⭐⭐⭐ 逻辑严密结论有力
- 价值: ⭐⭐⭐⭐⭐ 对LLM安全研究方向有根本性影响
