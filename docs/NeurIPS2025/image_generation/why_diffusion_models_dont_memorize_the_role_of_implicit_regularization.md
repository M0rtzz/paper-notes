---
title: >-
  [论文解读] Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
description: >-
  [NeurIPS 2025][图像生成][扩散模型] 本文从数值实验和理论分析两个层面揭示扩散模型训练中存在**隐式动态正则化**机制：生成高质量样本的时间尺度 τ_gen 与出现记忆化的时间尺度 τ_mem 之间的间隔随训练集大小 n 线性增长，为"早停"提供了理论支撑。
tags:
  - NeurIPS 2025
  - 图像生成
  - 扩散模型
  - memorization
  - generalization
  - implicit-regularization
  - score-matching
---

# Why Diffusion Models Don't Memorize: The Role of Implicit Regularization

**会议**: NeurIPS 2025  
**arXiv**: [2505.17638](https://arxiv.org/abs/2505.17638)  
**代码**: 无  
**领域**: 图像生成  
**关键词**: diffusion-model, memorization, generalization, implicit-regularization, score-matching  
# Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training

## 一句话总结

本文从数值实验和理论分析两个层面揭示扩散模型训练中存在**隐式动态正则化**机制：生成高质量样本的时间尺度 τ_gen 与出现记忆化的时间尺度 τ_mem 之间的间隔随训练集大小 n 线性增长，为"早停"提供了理论支撑。

## 背景与动机

1. **扩散模型的实际成功**：扩散模型（DMs）在图像、音频、视频等生成任务中取得 SOTA 表现，但其为何能在高度过参数化设置下避免记忆训练数据，机制尚不清楚。
2. **经验分数的记忆化本质**：理论上，若模型完美学到经验分数（empirical score），则生成过程会精确复现训练样本；只有当 n 随维度 d 指数增长时才能避免，但实践中远未达到此条件。
3. **已有正则化解释不充分**：架构偏置、有限参数容量、有限学习率等因素被证明可抑制记忆化，但即便同时存在这些因素，记忆化-泛化转变仍一致出现，表明核心机制在别处。
4. **Spectral bias 的启示**：深度网络倾向于先学低频函数，而经验分数在低噪声水平下包含接近总体分数的低频部分和依赖数据集的高频部分，这种频率依赖性尚未被系统利用。
5. **需要可分析的理论模型**：此前对记忆化的理论研究主要关注无限训练时间下的渐近行为，未系统刻画训练动态中两个时间尺度的出现与分离。
6. **实际应用需求**：理解何时"早停"可安全避免记忆化，对数据稀缺场景下的模型训练具有直接指导意义。

## 方法详解

### 核心发现：两个时间尺度的分离

作者在训练过程中识别出两个关键时间尺度：

- **τ_gen（泛化时间）**：模型开始生成高质量样本的时间，约 100K SGD 步，**与训练集大小 n 无关**。
- **τ_mem（记忆化时间）**：模型开始记忆训练数据的时间，**随 n 线性增长**（τ_mem ∝ n）。

两者之间存在一个"泛化窗口" [τ_gen, τ_mem]，在此区间内早停可获得高质量且不记忆的生成结果。该窗口随 n 线性扩大。

### 数值实验设计

- **数据集**：CelebA 灰度 32×32 图像，训练集大小 n 从 128 到 32768。
- **模型**：U-Net 架构（DDPM），三层分辨率，基础宽度 W∈{8,16,32,48,64}，参数量 p∈{0.26M, 1M, 4M, 9M, 16M}。
- **优化器**：SGD with momentum，固定批大小 min(n, 512)。
- **评估指标**：FID 衡量生成质量；基于最近邻比率的记忆化分数 f_mem (阈值 k=1/3)；固定扩散时间 t=0.01 下的训练/测试损失。

### 模型容量的影响

- 更大的 W（更多参数）使 τ_gen 和 τ_mem 均提前，但两者的缩放关系保持：τ_gen ∝ W⁻¹，τ_mem ∝ nW⁻¹。
- 在 (n, p) 平面上构建了相图：当 n > n_gm(p) 时，泛化窗口打开；当 n > n*(p) 时，即使无限训练也不会记忆化（架构正则化区域）。

### 理论分析：随机特征网络（RFNN）

将分数函数参数化为两层随机特征网络 s_A(x) = (A/√p) σ(Wx/√d)，其中 W 固定、A 可学习。

在高维极限 d, p, n → ∞（保持 ψ_p = p/d, ψ_n = n/d 固定）下：

- **训练动态为线性**：梯度流方程可精确求解，时间尺度由矩阵 U 的本征值决定。
- **Theorem 3.1**：利用 replica method 推导了 U 的谱密度 ρ(λ) 的 Stieltjes 变换方程。
- **Theorem 3.2**：在过参数化区域 ψ_p > ψ_n ≫ 1，谱分为两个分离的体（bulk）：
    - **ρ₂**（高本征值 bulk）：对应 τ_gen，与具体训练集无关，取决于数据的总体协方差 Σ；
    - **ρ₁**（低本征值 bulk）：对应 τ_mem，尺度为 ψ_p/ψ_n，随 n 增大而使 τ_mem ∝ n。
    - 另有一个 δ 峰 δ(λ − s_t²)（权重 1 − (1+ψ_n)/ψ_p），对应的本征向量不影响生成质量。

### 三个区域的相图

在 (n, p) 平面中划分三个区域：
1. **记忆化区域**：n 小，模型在 τ_gen 即开始记忆。
2. **动态正则化区域**：n 适中，早停于 [τ_gen, τ_mem] 可泛化。
3. **架构正则化区域**：n > n*(p)，模型不够表达力以记忆，无限训练也不过拟合。

## 实验结果

### 表1：不同训练集大小下的关键指标（U-Net on CelebA, W=32）

| 训练集大小 n | 最佳 FID (↓) | τ_gen (K steps) | τ_mem/n (rescaled) | f_mem(τ_max) |
|---|---|---|---|---|
| 128 | ~60 | ~100K | ~300 | 高 |
| 512 | ~35 | ~100K | ~300 | 中 |
| 1024 | ~25 | ~100K | ~300 | 低 |
| 4096 | ~18 | ~100K | ~300 | 极低 |
| 32768 | ~15 | ~100K | ~300 | ~0 |

**关键观察**：所有 n 的归一化记忆化曲线在 τ/n ≈ 300 处坍缩，证实 τ_mem ∝ n。

### 表2：不同模型宽度下的时间尺度缩放（n=1024）

| 基础宽度 W | 参数量 p (M) | Wτ_gen (rescaled) | τ_mem 缩放 |
|---|---|---|---|
| 8 | 0.26 | ~3×10⁶ | ∝ nW⁻¹ |
| 16 | 1 | ~3×10⁶ | ∝ nW⁻¹ |
| 32 | 4 | ~3×10⁶ | ∝ nW⁻¹ |
| 48 | 9 | ~3×10⁶ | ∝ nW⁻¹ |
| 64 | 16 | ~3×10⁶ | ∝ nW⁻¹ |

**关键观察**：Wτ_gen ≈ 3×10⁶ 的坍缩表明 τ_gen ∝ W⁻¹，与 n 无关。

## 亮点

- **提出了训练动态中隐式正则化的清晰理论图景**：两个时间尺度的分离为早停策略提供了严格支撑，揭示了扩散模型泛化的核心机制。
- **理论与实验双重验证**：在真实 U-Net + CelebA 上和可精确求解的随机特征模型上均验证了相同现象，增强了结论的可信度。
- **谱分析的物理直觉**：利用 replica method 和随机矩阵理论，将生成与记忆化分别对应到谱的两个分离的体，提供了优雅且可操作的理论工具。
- **相图的实用价值**：(n, p) 相图可指导实践者根据数据量和模型规模选择安全的训练时长。

## 局限性

- **仅使用 SGD 优化器**：实际扩散模型多用 Adam，虽然附录中展示了 Adam 下两个时间尺度仍存在，但具体缩放关系可能不同。
- **无条件生成设置**：主要实验为无条件 DDPM，条件生成（如 classifier-free guidance）下 τ_gen 和 τ_mem 的具体依赖关系仍为开放问题。
- **参数量范围有限**：数值实验覆盖 1M–16M 参数，未探索更大模型（如 >100M），难以完整绘制 (n, p) 相图。
- **理论模型的简化**：RFNN 的第一层固定、数据分布为高斯等假设，与实际 U-Net 和真实图像数据存在差距；理论分析限于固定扩散时间 t 的情形。

## 相关工作对比

| 对比维度 | 本文 | Biroli et al. (2024) / George et al. (2025) |
|---|---|---|
| **研究重点** | 训练动态中的隐式正则化与两个时间尺度 | 分析扩散模型的记忆化-泛化转变的渐近行为 |
| **核心贡献** | τ_gen 不依赖 n、τ_mem ∝ n 的发现及谱理论解释 | 在 RFNN 框架下计算 τ→∞ 的训练/测试损失 |
| **方法差异** | 关注有限训练时间下的动态行为，强调早停的作用 | 主要关注无限训练时间的渐近状态 |
| **适用范围** | 同时覆盖实际 U-Net 和理论 RFNN | 主要理论分析 |

| 对比维度 | 本文 | Li et al. (2024) / Zhang et al. (2023) |
|---|---|---|
| **研究重点** | 训练动态导致的记忆化避免 | 架构偏置和网络容量对记忆化的约束 |
| **机制类型** | 隐式动态正则化（时间尺度分离） | 架构正则化（有限表达力） |
| **适用区域** | (n, p) 相图中的中间区域 | (n, p) 相图中 n > n*(p) 的大数据区域 |
| **互补关系** | 二者互补：架构正则化定义了 n*(p)，动态正则化在 n < n*(p) 时仍可通过早停避免记忆化 | 不考虑训练动态中的时间依赖行为 |

## 评分

| 维度 | 评分 | 说明 |
|---|---|---|
| 新颖性 | ⭐⭐⭐⭐ | 首次系统刻画扩散模型训练中泛化与记忆化两个时间尺度的分离机制 |
| 理论深度 | ⭐⭐⭐⭐⭐ | replica method + 随机矩阵理论提供了严格的谱分析，Theorem 3.1/3.2 给出了精确的解析结果 |
| 实验充分性 | ⭐⭐⭐⭐ | CelebA 上多种 n 和 p 的系统实验，但仅限低分辨率灰度图和较小模型 |
| 实用价值 | ⭐⭐⭐⭐ | 相图和缩放律可直接指导早停策略，对数据稀缺场景尤其有用 |

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training](why_diffusion_models_dont_memorize_the_role_of_implicit_dynamical_regularization.md)
- [\[NeurIPS 2025\] Encoder-Decoder Diffusion Language Models for Efficient Training and Inference](encoder-decoder_diffusion_language_models_for_efficient_training_and_inference.md)
- [\[NeurIPS 2025\] Understanding Representation Dynamics of Diffusion Models via Low-Dimensional Models](understanding_representation_dynamics_of_diffusion_models_via_low-dimensional_mo.md)
- [\[NeurIPS 2025\] When Are Concepts Erased From Diffusion Models?](when_are_concepts_erased_from_diffusion_models.md)
- [\[NeurIPS 2025\] Token Perturbation Guidance for Diffusion Models](token_perturbation_guidance_for_diffusion_models.md)

<!-- RELATED:END -->
