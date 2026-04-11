---
description: "【论文笔记】Parameter-Efficient Fine-Tuning of State Space Models 论文解读 | ICML 2025 | arXiv 2410.09016 | 参数高效微调 | 本文系统性地评估了现有 PEFT 方法在 SSM（如 Mamba）模型上的效果，发现 LoRA 虽在线性投影层表现最优但无法有效调优 SSM 模块，进而提出 Sparse Dimension Tuning（SDT）——一种专为 SSM 模块设计的 PEFT 方法，结合 LoRA 用于线性层，在多个基准上达到 SOTA 性能。"
tags:
  - ICML 2025
---

# Parameter-Efficient Fine-Tuning of State Space Models

**会议**: ICML 2025  
**arXiv**: [2410.09016](https://arxiv.org/abs/2410.09016)  
**代码**: [furiosa-ai/ssm-peft](https://github.com/furiosa-ai/ssm-peft)  
**领域**: 模型压缩  
**关键词**: 参数高效微调, State Space Models, Mamba, LoRA, Sparse Dimension Tuning

## 一句话总结

本文系统性地评估了现有 PEFT 方法在 SSM（如 Mamba）模型上的效果，发现 LoRA 虽在线性投影层表现最优但无法有效调优 SSM 模块，进而提出 Sparse Dimension Tuning（SDT）——一种专为 SSM 模块设计的 PEFT 方法，结合 LoRA 用于线性层，在多个基准上达到 SOTA 性能。

## 研究背景与动机

### 现状
State Space Models（SSMs），特别是 Mamba 系列，已成为 Transformer 的有力替代品，具有线性时间复杂度和出色的长序列处理能力。随着预训练 SSM 模型规模增大，参数高效微调（PEFT）变得至关重要。

### 痛点
1. PEFT 方法在 Transformer 上已被充分研究（LoRA、Prefix-tuning 等），但在 SSM 模型上的适用性尚未系统探索
2. SSM 模块的参数结构与 Transformer 的注意力层有本质区别（对角状态矩阵 A、输入依赖的 B/C/Δ），现有 PEFT 方法无法直接有效应用
3. LoRA 对 SSM 内部参数（如 A、B、C 矩阵）无效，而其他适用于 SSM 的方法（如 Additional-scan）表现更差

### 核心矛盾
SSM 模块需要专门的微调方法，但如何设计既高效又理论上有保证的 SSM 专用 PEFT 方法？

### 切入角度
通过理论分析 SSM 参数的角色，发现不同 channel 和 state dimension 的重要性不同，从而提出选择性地更新部分 dimension 的稀疏调优策略。

## 方法详解

### 整体框架

SSM-based 模型（如 Mamba）的每个 block 包含：
1. **SSM 模块**（S6）：包含状态矩阵 A、输入转换 B、输出映射 C、步长 Δ
2. **线性投影层**：输入投影 $W_{\text{in}}$、输出投影 $W_{\text{out}}$
3. **1D 卷积层**（Conv1d）

PEFT 策略：**LoRA 用于线性投影层 + SDT 用于 SSM 模块**

### 关键设计

#### 1. 全面基准测试

评估了三类共六种 PEFT 方法在 Mamba 和 Jamba 上的表现：

| 类别 | 方法 | 主要目标 |
|------|------|----------|
| 输入注入 | Prompt Tuning | 嵌入层 |
| 输入注入 | Prefix-Tuning | SSM 模块 |
| 架构增强 | Additional-scan | SSM 模块 |
| 权重调优 | BitFit | 偏置项 |
| 权重调优 | LoRA/DoRA | 投影矩阵 |

**核心发现**：
- LoRA 在所有 PEFT 方法中一致表现最优
- LoRA 仅用于线性投影层时效果最佳，扩展到 SSM 模块反而无提升
- 输入注入方法（Prompt/Prefix-tuning）在 SSM 上普遍无效
- Additional-scan 表现最差，GLUE 仅 62.4%

#### 2. Sparse Dimension Tuning（SDT）

通过理论分析 SSM 参数角色，提出稀疏维度调优：

**SDT-P（Sparse Dimension Tuning and Pruning）**：
- 冻结部分 channel 和 state dimension
- 剪枝不重要的维度
- 仅训练剩余维度的参数

**SDT（简化版）**：
- 省略显式剪枝（被剪枝的维度等价于训练参数设为零）
- 选择性更新部分 channel
- 在选中的 channel 内微调特定 state dimension

**设计动机**：
- SSM 的不同 channel 对下游任务的贡献不同
- State dimension 内部同样存在重要性差异
- 类比于 LoRA 的低秩更新，SDT 通过稀疏选择实现参数效率

#### 3. 理论保证

论文证明了 SDT-P 结合 LoRA 在 SSM 模型上的有效性保证。在线性 SSM 设置下，理论表明：
- 选择性更新关键维度足以近似全参数微调的效果
- 参数选择基于梯度幅度，确保更新最有信息量的参数

### 损失函数 / 训练策略

- 标准任务损失（交叉熵等），无特殊损失设计
- LoRA 秩和 SDT 稀疏度作为可调超参数
- 全部方法训练参数量控制在 Mamba 的 1% 以下、Jamba 的 0.15% 以下

## 实验关键数据

### 主实验：Mamba 上的 PEFT 比较

| 方法 | 目标模块 | GLUE | DART BLEU | SAMSum RL | Spider Acc | CIFAR-10 | CelebA |
|------|----------|------|-----------|-----------|------------|----------|--------|
| Prompt Tuning | 其他 | 63.8 | 39.8 | 41.6 | 43.6 | 30.4 | 82.5 |
| Prefix-Tuning | SSM | 68.6 | 42.5 | 42.1 | 39.7 | 41.0 | 86.5 |
| Additional-scan | SSM | 62.4 | 15.8 | 30.9 | 26.9 | 32.2 | 86.0 |
| LoRA | SSM | 76.9 | 48.0 | 41.8 | 55.0 | 52.3 | 87.0 |
| LoRA | LinProj | **81.2** | 49.5 | 42.3 | 57.5 | 61.0 | 87.0 |
| DoRA | LinProj | 81.1 | 51.6 | 42.8 | 60.7 | 57.6 | 86.7 |
| Full FT | 全部 | 80.5 | 51.8 | 42.9 | 66.2 | 60.0 | 89.4 |

### 消融实验：SDT 配置对比

| 配置 | GLUE | 参数量 |
|------|------|--------|
| LoRA only (LinProj) | 81.2 | <1% |
| LoRA (LinProj) + SDT (SSM) | **82.5+** | <1% |
| LoRA (Both) | 80.3 | >1% |
| Full Fine-Tuning | 80.5 | 100% |

SDT+LoRA 组合超越全参数微调，同时参数量不到 1%。

### 关键发现

1. **LoRA 对线性层最有效**：在所有 PEFT 方法中一致最优，但扩展到 SSM 模块无增益
2. **SSM 模块需要专门方法**：现有通用 PEFT 方法（BitFit、Additional-scan）均不适合 SSM
3. **SDT + LoRA 协同增效**：两者互补，分别处理 SSM 和线性层
4. **在 Jamba（混合架构）上同样有效**：证明方法的通用性

## 亮点与洞察

1. **系统性基准**：首次全面评估六种 PEFT 方法在 SSM 模型上的表现，填补了该领域空白
2. **问题驱动的设计**：先通过实验发现问题（LoRA 对 SSM 无效），再通过理论分析驱动解决方案设计
3. **SDT 的本质洞察**：SSM 的维度重要性不均匀，稀疏选择比全局低秩更新更适合 SSM 的参数结构
4. **混合架构兼容**：在 Jamba（Transformer+Mamba）上同样验证，具有更广泛的适用性
5. **实用意义**：提供了 SSM 模型微调的最佳实践指南

## 局限性 / 可改进方向

1. **主体集中于 Mamba-I**：Mamba-II 的实验放在了附录中，对更新架构的覆盖不够深入
2. **SDT 维度选择策略**：当前基于梯度幅度选择，可以探索更智能的选择策略（如基于 Fisher 信息）
3. **缺少大规模模型实验**：主要在 Mamba-130M/370M 和 Jamba 上实验，缺少超大规模 SSM 的验证
4. **视觉任务的处理方式**：将图像像素值扁平化为数字序列，非标准做法，可能影响结果可靠性
5. **未探索 SSM+Attention 混合层的联合调优策略**

## 相关工作与启发

- **LoRA (Hu et al. 2021)**：低秩更新的经典方法 → 对线性层仍是最优选择
- **Mamba (Gu & Dao 2024)**：S6 选择性状态空间模型 → SDT 的设计对象
- **Yoshimura et al. 2025**：Additional-scan 方法 → 通过扩展状态维度，效果不佳
- **Kang et al. 2025**：State-offset Tuning → 仅关注 S6 块
- **Song et al. 2024**：稀疏调优的一般框架 → 启发了 SDT 的稀疏选择思路
- **启发**：不同架构的参数结构决定了最优 PEFT 策略，盲目迁移可能失效

## 评分

- 新颖性: ⭐⭐⭐⭐ SDT 是首个针对 SSM 的 PEFT 方法，但核心思想（稀疏选择）并非全新
- 实验充分度: ⭐⭐⭐⭐⭐ 6 数据集、3 类任务、多种 PEFT 方法全面对比
- 写作质量: ⭐⭐⭐⭐ 结构清晰、图表丰富，roadmap 设计好
- 价值: ⭐⭐⭐⭐⭐ 填补 SSM-PEFT 空白，为该方向提供了基准和最佳实践
