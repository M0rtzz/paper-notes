---
title: >-
  [论文解读] Smoothing the Score Function for Generalization in Diffusion Models: An Optimization-based Explanation Framework
description: >-
  [CVPR 2026][图像生成][扩散模型] 从理论上证明扩散模型的记忆化源于经验得分函数的"尖锐性"（softmax 权重集中），提出噪声无条件化和温度平滑两种方法，通过平滑得分函数权重来提升泛化、减少记忆化，同时保持生成质量。
tags:
  - CVPR 2026
  - 图像生成
  - 扩散模型
  - 记忆化
  - 泛化
  - 得分函数平滑
  - 温度平滑
---

# Smoothing the Score Function for Generalization in Diffusion Models: An Optimization-based Explanation Framework

**会议**: CVPR 2026  
**arXiv**: [2601.19285](https://arxiv.org/abs/2601.19285)  
**代码**: [GitHub](https://github.com)  
**领域**: 扩散模型 / 生成模型理论  
**关键词**: 扩散模型, 记忆化, 泛化, 得分函数平滑, 温度平滑

## 一句话总结

从理论上证明扩散模型的记忆化源于经验得分函数的"尖锐性"（softmax 权重集中），提出噪声无条件化和温度平滑两种方法，通过平滑得分函数权重来提升泛化、减少记忆化，同时保持生成质量。

## 研究背景与动机

1. **领域现状**：扩散模型在生成质量上达到 SOTA，但研究发现部分生成样本与训练数据完全相同（记忆化问题），引发隐私和版权担忧。
2. **现有痛点**：理论上若神经网络完美学习经验得分函数，只会复制训练样本。但实践中模型能生成新样本——这个理论-实践不一致缺乏解释。
3. **核心矛盾**：为什么神经网络能（部分）解决记忆化问题？如何进一步改善泛化？
4. **本文目标**：建立理论框架解释记忆化原因和泛化机制，并提出改进方法。
5. **切入角度**：分析经验得分函数权重 $w_{ij}(x)$ 的数学结构——它是 softmax 函数形式。
6. **核心 idea**：在高维空间中，经验得分函数权重在低噪声水平下极度集中（尖锐），导致单个训练点主导采样过程。神经网络通过隐式平滑这些权重来实现泛化。

## 方法详解

### 整体框架

理论分析：证明记忆化与得分函数权重的尖锐性直接相关。两种平滑方法：(1) 噪声无条件化——移除噪声条件使每个训练点自适应选择最优噪声层；(2) 温度平滑——在 softmax 权重中引入温度参数控制平滑度。

### 关键设计

1. **记忆化的数学解释（σ 和 μ 主导性）**:

    - 功能：严格证明为什么记忆化发生
    - 核心思路：得分函数权重 $w_{ij}(x) = \text{Softmax}(f(x, \mu_j, \sigma_i))$ 其中 $f = -(d-2)\ln\sigma_i - \|x-\mu_j\|^2 / (2\sigma_i^2)$。σ 主导性：给定位置 $x$ 和中心 $\mu_j$，存在最优噪声 $\sigma_j^*$ 使该项权重以指数级主导其他噪声级。μ 主导性：给定 $x$，最近训练点的权重以 $\exp(\delta\|\mu_j-\mu_l\|^2/\sigma_j^{*2})$ 级别主导其他点。当 $\sigma^* \to 0$，单个训练点完全主导 → 记忆化。
    - 设计动机：高维几何中高斯分布集中在薄壳上，使得得分函数权重变为尖锐的 softmax。

2. **噪声无条件化（Noise Unconditioning）**:

    - 功能：通过移除噪声条件使采样点受更多训练样本影响
    - 核心思路：将 $s_\theta(x, t) \to s_\theta(x)$，所有噪声水平统一到一个高斯混合分布 $p_{\text{MN}}$。每个训练点可自适应找到最优噪声壳层，使更多训练点能显著贡献于得分函数。采样可重新表述为对 $\log p_{\text{MN}}$ 的梯度上升。
    - 设计动机：标准扩散中噪声级固定，采样点可能不在大多数训练点的最优壳层上，导致这些点的权重被压制。无条件化允许每个点"自选"最优壳层。

3. **温度平滑（Temperature Smoothing）**:

    - 功能：显式控制得分函数权重的平滑度
    - 核心思路：引入温度向量 $T$，修改权重为 $w_j^*(x;T) = \exp(f(x,\mu_j,\sigma_j^*)/T_j^*) / \sum_l \exp(f(x,\mu_l,\sigma_l^*)/T_l^*)$。在 $\sigma_i \leq \sigma_{\text{collapse}}$ 时用 top-K 近邻训练点近似得分函数，并设 $T_i = \max(\sigma_{\text{collapse}}/\sigma_i, 1)$。
    - 设计动机：温度升高使权重分布更均匀，延迟采样过程的"坍缩"到单点，允许在局部流形上持续探索。

### 损失函数 / 训练策略

无条件化损失 $\mathcal{L}_u$：与标准 NCSN 相同但移除噪声输入。温度损失 $\mathcal{L}_T$：在 $\sigma > \sigma_{\text{collapse}}$ 时用 $\mathcal{L}_u$，否则用温度修改的得分匹配。特征空间 KNN 优于像素空间 KNN。

## 实验关键数据

### 主实验

| 方法 | CIFAR-10 FID(train) | FID(test) | CelebA FID(train) | FID(test) |
|------|--------------------|-----------|--------------------|-----------|
| Conditioning | 6.49 | 6.56 | 7.25 | 7.81 |
| Unconditioning | 7.33 | 7.34 | 7.07 | 7.34 |
| Temp (feature KNN, K=100) | 7.96 | 7.98 | 8.40 | 8.19 |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 像素空间 KNN, T=7/σ, K=100 | FID=50.81 | 流形曲率过大导致崩溃 |
| 特征空间 KNN, T=7/σ, K=100 | FID=7.96 | 低曲率空间支持强平滑 |
| α=1/3 时权重比 | ≈403:1 | 即使微小距离优势也产生巨大权重差 |

### 关键发现

- 神经网络学到的得分函数比经验得分函数平滑得多——扩展比率 $\gamma_{ex}$ 小两个数量级
- 特征空间 KNN 一致优于像素空间，支持"神经网络通过平滑局部流形实现泛化"的假说
- 猫-狞猫数据集上出现明显泛化：生成了具有狞猫面部但短耳和灰色毛色的"新物种"

## 亮点与洞察

- **优雅的理论框架**：用高维几何和 softmax 分析将记忆化问题转化为可操作的数学框架
- **无条件化的优化视角**：将采样重新表述为梯度上升，统一了扩散理论和优化理论
- **直觉性强的几何类比**：登山者类比使复杂理论变得直观——传统扩散是"分段指南"，无条件化是"全景地图"

## 局限与展望

- 温度平滑需要 KNN 查找最近训练点，大规模数据集上成本较高
- FID 略有下降（以泛化换质量），需要在具体应用中权衡
- 当前仅在 VE-SDE 上验证，未扩展到 DDPM 或 Flow Matching
- 理论分析主要基于高斯混合模型假设，实际数据分布更复杂
- 温度参数 $T$ 与早停时机的联合调优需要实践经验

## 相关工作与启发

- **vs Yoon et al.**: 他们从模型容量角度解释记忆化，本文从得分函数数学性质解释
- **vs Bonnaire et al.**: 他们研究神经网络如何学习得分函数，本文进一步解释为什么学到的差异有助于泛化

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 理论框架极具洞察力，两种方法都基于深刻的数学分析，登山者类比尤其精彩
- 实验充分度: ⭐⭐⭐⭐ 定量定性验证充分，扩展比率实验巧妙设计，猫-狞猫数据集直观展示泛化
- 写作质量: ⭐⭐⭐⭐⭐ 理论阐述清晰，直觉类比优秀，证明严格但不失可读性
- 价值: ⭐⭐⭐⭐⭐ 为扩散模型泛化理论奠定了重要基础，对理解和改进生成模型有深远影响

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework](taming_score-based_denoisers_in_admm_a_convergent_plug-and-play_framework.md)
- [\[CVPR 2026\] Fractals made Practical: Denoising Diffusion as Partitioned Iterated Function Systems](fractals_made_practical_denoising_diffusion_as_partitioned_iterated_function_sys.md)
- [\[CVPR 2026\] Reviving ConvNeXt for Efficient Convolutional Diffusion Models](reviving_convnext_for_efficient_convolutional_diffusion_models.md)
- [\[CVPR 2026\] PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](pixelrush_ultra-fast_training-free_high-resolution_image_generation_via_one-step.md)
- [\[CVPR 2026\] coDrawAgents: A Multi-Agent Dialogue Framework for Compositional Image Generation](codrawagents_a_multi-agent_dialogue_framework_for_compositional_image_generation.md)

<!-- RELATED:END -->
