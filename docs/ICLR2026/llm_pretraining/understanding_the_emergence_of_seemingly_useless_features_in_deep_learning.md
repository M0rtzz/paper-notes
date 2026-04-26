---
title: >-
  [论文解读] Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors
description: >-
  [ICLR2026][特征涌现] 从梯度信号的角度解释了为什么用下一 token 预测(NTP)训练的 Transformer 会学习到对预测当前下一 token "无用"的特征，提出三种梯度路径分解（直接学习、预缓存、电路共享）并在玩具任务、OthelloGPT 和语言模型中验证。
tags:
  - ICLR2026
  - 特征涌现
  - 下一token预测
  - 预缓存
  - 电路共享
  - 世界模型
  - 机制可解释性
---

# Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors

**会议**: ICLR2026  
**arXiv**: [2603.14087](https://arxiv.org/abs/2603.14087)  
**代码**: [GitHub](https://github.com/Markfryazino/useless-features-iclr-code)  
**领域**: llm_nlp  
**关键词**: 特征涌现, 下一token预测, 预缓存, 电路共享, 世界模型, 机制可解释性

## 一句话总结

从梯度信号的角度解释了为什么用下一 token 预测(NTP)训练的 Transformer 会学习到对预测当前下一 token "无用"的特征，提出三种梯度路径分解（直接学习、预缓存、电路共享）并在玩具任务、OthelloGPT 和语言模型中验证。

## 背景与动机

- LLM 通常用 NTP 目标训练：学习 $p(x_{t+1}|x_1 \cdots x_t)$
- 直觉上，模型只需学习对预测下一 token 有用的特征
- 但大量研究发现 Transformer 学到了远超此需要的丰富表征：抽象特征、世界模型、多步前瞻等
- OthelloGPT 甚至学到了棋盘状态表征，尽管预测合法走法不需要知道所有棋子位置
- **核心问题**：NTP 目标的梯度信号从何而来，使得模型学习了这些"无用"特征？

## 核心问题

训练用于 NTP 的 Transformer 如何学习到对预测当前下一 token 无用的特征？梯度信号的哪些组分驱动了这些特征的涌现？

## 方法详解

### 三种梯度路径分解

对残差流 $r_{\theta,i}^k(x)$ 在位置 $i$、层 $k$ 处，损失梯度可分解为三条独立路径：

**1. 直接学习(Direct Learning)** — 绿色路径

来自位置 $i+1$ 的下一 token 预测损失，经过 $r_{\theta,i}^k(x)$：

$$\nabla_\theta L_{i(\text{direct})}^k = \nabla_\theta L_i - \nabla_\theta L_i^{\text{sg}(k,i)}$$

**2. 预缓存(Pre-caching)** — 蓝色路径

来自位置 $j > i+1$ 的预测损失，通过注意力机制"回看"位置 $i$ 的内容：

$$\nabla_\theta L_{i(\text{pre-cached})}^k = \nabla_\theta \sum_{j \neq i} \left[L_j - L_j^{\text{sg}(k,i)}\right]$$

**3. 电路共享(Circuit Sharing)** — 橙色路径

不经过 $r_{\theta,i}^k(x)$ 的路径。由于 Transformer 共享参数，其他位置的梯度信号也会影响计算位置 $i$ 的参数：

$$\nabla_\theta L_{i(\text{shared})}^k = \sum_j \nabla_\theta L_j^{\text{sg}(k,i)}$$

**Proposition 3.1**：三者构成总梯度的精确分解：
$$\nabla_\theta L = \nabla_\theta L_{i(\text{direct})}^k + \nabla_\theta L_{i(\text{pre-cached})}^k + \nabla_\theta L_{i(\text{shared})}^k$$

### 消融方法

- **消融预缓存**：使用 myopic training，阻断不同位置之间的梯度流
- **消融电路共享**：使用 $m$-untied training，位置 $m$ 前后用不同参数
- **极端情况**：myopic + untied = "分裂大脑"，三种路径都被隔离

### 影响力度量

**定义 Feature Mismatch**：
$$R(x|\theta_1, \theta_2, w_i^k) = \frac{1}{2}(\langle w_i^k, r_{\theta_1,i}^k(x)\rangle - \langle w_i^k, r_{\theta_2,i}^k(x)\rangle)^2$$

**定义 Influence**：
$$I_i^k(\theta, x | w_i^k, \theta^*, G) = \frac{d}{d\varepsilon} R(x|\theta + \varepsilon G, \theta^*, w_i^k)\bigg|_{\varepsilon=0}$$

将 $G$ 分别代入三个梯度组分，获得各组分的 integrated influence。

### 大模型适配：Proposition 5.1

对于无法重训练的大模型，通过激活干预近似影响力比值：

$$Q(w) = \frac{\sum_{j>i+1} d_j^{/i}}{d_{i+1}^{/i}} \approx \frac{I_{\text{pre-cached}}}{I_{\text{direct}}}$$

$Q(w)$ 高表示该特征主要由预缓存驱动。

## 实验关键数据

### 玩具任务：Majority 和 Conditioned Majority

| 训练方式 | Majority 特征探针 | Conditioned Majority 特征探针 |
|---------|-----------------|---------------------------|
| 正常训练 | 高 | 高 |
| Myopic (无预缓存) | 降低 | 无法学习 |
| Untied (无电路共享) | 降低 | 高 |
| Myopic + Untied | **最低** | **无法学习** |

- Conditioned Majority 需要预缓存才能学习（需要两层注意力交互）
- 消融两种机制后，NTP-无用特征基本不出现

### OthelloGPT

| 梯度组分 | NTP-有用特征 95%CI | NTP-无用特征 95%CI |
|---------|-------------------|-------------------|
| Direct | [2.85, 12.38] | [-4.69, 2.74] |
| Pre-cached | [-1.99, 0.66] | [0.55, 3.05] |
| Shared | [4.80, 12.48] | [2.93, 9.91] |
| Combined | [12.14, 19.05] | [4.42, 10.07] |

- Direct influence 仅对 NTP-有用特征显著为正，对 NTP-无用特征不显著
- Pre-cached 和 Shared influence 对 NTP-无用特征仍为正，解释了为何它们能被学到
- 解释了 Vafa et al. (2025) 发现的 OthelloGPT 世界模型脆弱性

### 语言模型 (TinyStories)

| 特征类型 | 是否需要预缓存 | 预缓存 influence |
|---------|-------------|----------------|
| POS 标签 | 否 | 低 |
| 依存标签 | 否 | 低 |
| 位置特征(故事中位置) | **是** | **高** |

- Myopic 模型 loss 为 3.29±0.02，正常模型为 2.53±0.10（差异巨大）
- 简单语法不需要预缓存，但连贯文本生成需要

### Gemma 2 2B：SAE 特征分析

- $Q(w)$ 极端高或低的特征主要与**编程/形式推理**相关
- $\sigma_{\text{formal}} = 1.63 \pm 0.03$ vs $\sigma_{\text{not formal}} = 1.23 \pm 0.02$
- 对高 $Q(w)$ 特征进行 steering 会生成更多代码和标点
- 预缓存特征与前瞻(look-ahead)呈**负相关**，支持"面包屑假说"

## 亮点

1. **从发展视角理解特征**：不同于传统的功能性可解释性，从梯度信号的发展角度解释特征为何出现
2. **三路径分解的优雅**：将总梯度精确分解为三个有明确物理含义的组分
3. **OthelloGPT 世界模型的新解释**：NTP-无用棋格的表征来自预缓存和电路共享，而非直接学习
4. **否定了预缓存=前瞻假说**：实证表明预缓存特征与前瞻能力呈负相关
5. **跨尺度验证**：从玩具任务到 Gemma 2 2B 的一致性发现

## 局限性 / 可改进方向

- Attribution 方法依赖重训练模型（对大模型不可行），Proposition 5.1 仅是近似
- 特征定义限于线性探针方向，非线性特征未被覆盖
- 仅在 Gemma 2 上进行大模型实验，更多 LLM 的验证待做
- Myopic training 同时阻断了正向信息传递和反向梯度流，难以完全解开因果关系
- 未探讨 RLHF 等后训练阶段对特征涌现的影响

## 与相关工作的对比

| 方向 | 本文贡献 |
|------|---------|
| Li et al. (2023) OthelloGPT | 解释了 NTP-无用特征为何仍可学到 |
| Vafa et al. (2025) 世界模型脆弱性 | 用 gradient 组分解释了 NTP-有用/无用特征的差距 |
| Wu et al. (2024) 预缓存假说 | 引入电路共享，否定预缓存=前瞻 |
| Bachmann & Nagarajan (2024) NTP 局限 | 补充了 NTP 正面能力来源的分析 |

## 启发与关联

- "发展可解释性"(developmental interpretability) 是理解 LLM 的新范式
- 预缓存机制与 CoT 推理有联系：模型可能在早期位置就为后续推理做准备
- 电路共享解释了为何共享参数的 Transformer 比位置独立模型更强大
- $Q(w)$ 指标可作为实用工具，帮助筛选 SAE 特征中的"规划型"特征

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 从梯度信号角度解释特征涌现，视角全新
- 实验充分度: ⭐⭐⭐⭐ — 从玩具到大模型的完整链条，但大模型实验有限
- 写作质量: ⭐⭐⭐⭐⭐ — 逻辑清晰，数学严谨，图表精美
- 价值: ⭐⭐⭐⭐⭐ — 为理解 LLM 内部表征提供了新的分析框架

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] Explaining Grokking and Information Bottleneck through Neural Collapse Emergence](explaining_grokking_and_information_bottleneck_through_neural_collapse_emergence.md)
- [\[ICLR 2026\] A Law of Data Reconstruction for Random Features (and Beyond)](a_law_of_data_reconstruction_for_random_features_and_beyond.md)
- [\[ICLR 2026\] Block-Sample MAC-Bayes Generalization Bounds](block-sample_mac-bayes_generalization_bounds.md)
- [\[ICLR 2026\] CHAMMI-75: Pre-training multi-channel models with heterogeneous microscopy images](chammi-75_pre-training_multi-channel_models_with_heterogeneous_microscopy_images.md)
- [\[ICLR 2026\] Deconstructing Positional Information: From Attention Logits to Training Biases](deconstructing_positional_information_from_attention_logits_to_training_biases.md)

<!-- RELATED:END -->
