---
title: >-
  [论文解读] Linear Attention for Efficient Bidirectional Sequence Modeling
description: >-
  [NeurIPS 2025][模型压缩][注意力机制] 提出 Lion 框架，首次系统地将线性 Transformer 扩展到双向序列建模，统一了全线性注意力、双向 RNN 和分块并行三种等价表示，在图像分类和 MLM 任务上训练速度比 SSM 快达 10 倍且性能可比 softmax Transformer。
tags:
  - NeurIPS 2025
  - 模型压缩
  - 注意力机制
  - bidirectional modeling
  - state space model
  - Transformer
  - RNN
---

# Linear Attention for Efficient Bidirectional Sequence Modeling

**会议**: NeurIPS 2025  
**arXiv**: [2502.16249](https://arxiv.org/abs/2502.16249)  
**代码**: [GitHub](https://github.com/LIONS-EPFL/Lion) (LION Code)  
**领域**: 模型压缩  
**关键词**: linear attention, bidirectional modeling, state space model, efficient transformer, RNN

## 一句话总结

提出 Lion 框架，首次系统地将线性 Transformer 扩展到双向序列建模，统一了全线性注意力、双向 RNN 和分块并行三种等价表示，在图像分类和 MLM 任务上训练速度比 SSM 快达 10 倍且性能可比 softmax Transformer。

## 研究背景与动机

1. **领域现状**：线性 Transformer（如 RetNet、Mamba-2、GLA）在因果序列建模中已成为 softmax Transformer 的高效替代，支持矩阵乘法并行训练和 RNN 推理。但在双向任务（如 BERT、ViT）中，线性 Transformer 几乎没有被系统研究。

2. **现有痛点**：
   - 现有双向 SSM（如 Vim、Hydra）主要基于 Mamba，简单地将因果扫描在前向和后向各执行一次
   - 这种"双扫描"方法未利用双向建模的天然先验：训练和推理时整个序列都可用
   - 结果是训练速度严重落后于 softmax Transformer（Vim 比 DeiT 慢 14.95 倍）

3. **核心矛盾**：SSM 在因果任务中的效率优势（RNN 推理）在双向任务中因为需要 chunking 而大打折扣，但如果直接用全注意力矩阵则又退回了 $\mathcal{O}(L^2)$ 复杂度。

4. **本文要解决什么**：为线性 Transformer 提供系统的双向扩展框架，使其在训练速度、推理效率和模型性能上同时达到最优。

5. **切入角度**：基于因果线性 Transformer 的 mask 结构，从因果 mask $\mathbf{M}^C$（下三角）推广到双向 mask $\mathbf{M}$（满矩阵），其中 $\mathbf{M}_{ij}$ 等于位置 $i$ 和 $j$ 之间所有衰减因子的乘积。

6. **核心idea一句话**：定义双向 mask = 下三角因果 mask + 上三角反向 mask - 单位阵（避免对角线重复计数），从而将任意因果线性 Transformer 转化为双向版本。

## 方法详解

### 整体框架

Lion 提供三种理论等价的表示：
1. **Full Linear Attention**：$\mathbf{Y} = \text{Scale}(\mathbf{Q}\mathbf{K}^\top \odot \mathbf{M})\mathbf{V}$（最快训练）
2. **Bidirectional RNN**：前向 + 后向 RNN（最省内存推理）
3. **Chunkwise Parallel**：分块处理（平衡速度和内存）

### 关键设计

**1. 双向 Mask 构造**

$$\mathbf{M} = \mathbf{M}^F + \mathbf{M}^B - \mathbf{I}$$

- $\mathbf{M}^F$：下三角（含对角），每个元素 $\mathbf{M}_{ij}^F = \prod_{k=j+1}^i \lambda_k$
- $\mathbf{M}^B$：上三角（含对角），每个元素 $\mathbf{M}_{ij}^B = \prod_{k=i+1}^j \lambda_k$
- 减去 $\mathbf{I}$ 防止对角线重复计数

三种 mask 类型：
- **选择性 mask**（$\lambda_i$ 输入依赖）：$\mathbf{M}^F = \text{Tril}(\mathbf{L}^F / \mathbf{L}^{F\top})$
- **固定可学习 mask**：$\mathbf{M}_{ij} = \lambda^{|i-j|}$（KMS 矩阵）
- **全一 mask**（无衰减）：$\mathbf{M}_{ij} = 1$

**2. 双向 RNN 的正确推导（Theorem 3.1）**

简单求和两个方向的 RNN 会导致不均衡注意力（对角线被双重计算）。正确做法：

$$\mathbf{y}_i = \frac{\mathbf{y}_i^F + \mathbf{y}_i^B}{c_i^F + c_i^B}$$

其中：
$$\mathbf{y}_i^{F/B} = \mathbf{q}_i^\top (\mathbf{S}_i^{F/B} - \frac{1}{2}\mathbf{k}_i \mathbf{v}_i^\top)$$
$$\mathbf{S}_i^{F/B} = \Lambda_i \mathbf{S}_{i-1}^{F/B} + \mathbf{k}_i \mathbf{v}_i^\top$$

关键是减去 $\frac{1}{2}\mathbf{k}_i \mathbf{v}_i^\top$ 来修正对角线的重复计算。

**3. 分块并行形式（Theorem 3.2）**

将序列分为 $N = L/C$ 个大小为 $C$ 的块：
- 块内（intra）：正常注意力计算
- 块间（inter）：通过隐状态 $\mathbf{S}_{[ij]}$ 和 $\mathbf{C}_{[ij]}$ 传递信息
- 双向情况下仅需块间计算（整序列可用）

### 三个实例化模型

| 模型 | 衰减类型 | 基于 |
|------|---------|------|
| **Lion-lit** | $\lambda_i = 1$（无衰减） | Vanilla Linear Transformer |
| **Lion-d** | $\lambda = \sigma(a)$（固定可学习） | RetNet |
| **Lion-s** | $\lambda_i = \sigma(\mathbf{W}\mathbf{x}_i + b)$（选择性） | Gated RFA / Mamba-2 |

### 损失函数/训练策略

- 训练时使用 Full Linear Attention 形式（最快），$\mathcal{O}(L^2 d)$ 复杂度但 $\mathcal{O}(1)$ 序列步
- 推理时切换到 RNN 形式（最省内存）或 Chunkwise 形式（平衡）
- 特征映射 $\phi(\mathbf{x}) = \frac{\text{SiLU}(\mathbf{x}) + 0.5}{\|\text{SiLU}(\mathbf{x}) + 0.5\|}$
- 直接替换 DeiT/BERT 中的注意力层，其余配置不变

## 实验关键数据

### ImageNet 图像分类（Small scale, 22M params）

| 模型 | Top-1 Acc (%) | 训练时间 (相对 DeiT) |
|------|--------------|---------------------|
| ViT | 72.2 | ×1 |
| DeiT | 79.8 | ×1 |
| Hydra | 78.6 | ×2.50 |
| Vim | 80.3 | **×14.95** |
| Lion-lit | 72.4 | **×0.74** |
| Lion-d | 73.5 | ×1.49 |
| **Lion-d♮** | **79.9** | ×1.66 |
| Lion-s | 74.0 | ×2.03 |
| Lion-s♮ | 79.6 | ×2.72 |

Lion-d♮ 准确率超过 DeiT（79.9 vs 79.8），训练速度比 Vim **快 9 倍**。

### C4 MLM + GLUE（Large scale, 334M params）

| 模型 | MLM Acc | GLUE | 训练时间 |
|------|---------|------|---------|
| BERT | 69.88 | **82.95** | ×1 |
| Hydra | **71.18** | 81.77 | ×3.13 |
| Lion-lit | 67.11 | 80.76 | **×0.95** |
| Lion-d | 68.64 | 81.34 | ×1.10 |
| Lion-s | 69.16 | 81.58 | ×1.32 |

Lion 变体训练比 Hydra **快 2-3 倍**，性能接近 BERT。

### LRA 长距离基准

| 模型 | PathX | Avg |
|------|-------|-----|
| Lion-lit | 50.41 | — |
| Lion-d (w/ HIPPO) | 97.28 | 85.63 |
| Lion-s (w/ HIPPO) | **97.99** | **86.07** |

HIPPO 初始化对解决长距离任务至关重要。

### 关键发现

- Lion-lit 训练速度最快（×0.74 DeiT），但无衰减导致长距离建模弱
- Lion-d♮ 是准确率-速度最佳平衡点，超越 DeiT 同时比 Vim 快 9 倍
- RNN 推理形式内存随分辨率线性增长，而 softmax attention 为二次增长
- 分块大小 8-16 是速度-内存的最佳平衡
- 多扫描策略（♮）在视觉任务中贡献显著（+6% 准确率），但增加了训练时间

## 亮点与洞察

- **首个统一的双向线性 Transformer 框架**：覆盖 10+ 现有模型（RetNet, Mamba-2, GLA, HGRN-2, xLSTM, DeltaNet 等）
- **三种等价表示的优雅统一**：训练用注意力，推理用 RNN，妙用各自优势
- **双向 RNN 的重复计数修正**：看似简单的 $-\frac{1}{2}\mathbf{k}_i\mathbf{v}_i^\top$ 修正是关键创新
- **纯 PyTorch 实现即可超越 CUDA 优化的 SSM**：说明全注意力形式的硬件友好性

## 局限性/可改进方向

- 全注意力形式仍为 $\mathcal{O}(L^2)$ 训练复杂度，超长序列下不如 chunked SSM
- Lion-lit 和 Lion-d 的非选择性 mask 限制了表达力
- 视觉任务依赖多扫描策略，增加了工程复杂度
- MLM 性能与 BERT 仍有小差距（Large 规模上 -0.72 MLM Acc）
- 缺少在更多下游任务上的评估（如问答、摘要、生物序列）

## 相关工作与启发

- Vim 开创了双向 SSM 视觉应用，但训练效率极低；Lion 从训练效率角度切入
- Hydra 的双 SSD 是目前最强双向 SSM，Lion 在训练速度上大幅领先
- 与 Flash Attention 互补：Flash Attention 优化 softmax 注意力的 I/O，Lion 用线性注意力从根本上改变复杂度
- 启发：双向任务中"全序列可用"这一先验被严重低估——它使得全注意力矩阵可以直接计算，无需 chunking

## 评分

⭐⭐⭐⭐⭐ (5/5)

框架性贡献：首次统一了双向线性 Transformer 的三种表示，理论优雅（等价性证明），实践价值高（10 倍训练加速），覆盖面广（10+ 模型的双向扩展）。
