---
title: >-
  [论文解读] CHORDS: Diffusion Sampling Accelerator with Multi-Core Hierarchical ODE Solvers
description: >-
  [ICCV 2025][图像生成][扩散模型] 提出 Chords，一种基于多核层级 ODE 求解器的无训练、模型无关扩散采样加速框架，通过慢到快的求解器层级和核间纠偏机制，在 4~8 个 GPU 核上实现最高 2.9× 加速而不损失生成质量。
tags:
  - ICCV 2025
  - 图像生成
  - 扩散模型
  - 多核并行采样
  - ODE求解器
  - 无训练加速
  - 视频生成
---

# CHORDS: Diffusion Sampling Accelerator with Multi-Core Hierarchical ODE Solvers

**会议**: ICCV 2025  
**arXiv**: [2507.15260](https://arxiv.org/abs/2507.15260)  
**代码**: [https://hanjq17.github.io/CHORDS](https://hanjq17.github.io/CHORDS)  
**领域**: 图像/视频生成加速  
**关键词**: 扩散模型, 多核并行采样, ODE求解器, 无训练加速, 视频生成

## 一句话总结

提出 Chords，一种基于多核层级 ODE 求解器的无训练、模型无关扩散采样加速框架，通过慢到快的求解器层级和核间纠偏机制，在 4~8 个 GPU 核上实现最高 2.9× 加速而不损失生成质量。

## 研究背景与动机

扩散模型已成为高保真图像和视频生成的主流方法，但其迭代采样过程计算开销极大，严重限制了在实时编辑、流式应用等延迟敏感场景的部署。现有加速方法主要分为两类：(1) 基于蒸馏的方法需要额外训练且可能损失质量；(2) 基于高效 ODE 求解器的方法在单核下进一步提速空间有限。

**核心矛盾**：如何在不重新训练、不限定模型架构的前提下，利用多 GPU 并行资源实现显著加速？现有多核方法要么依赖特定架构、要么需要额外训练、要么资源分配不灵活。

**切入角度**：受传统多重网格 ODE 加速算法启发，将多核扩散采样视为一条 ODE 求解流水线，快速但不精确的求解器可通过慢速精确求解器的信息进行层级纠偏，从而在理论上保证加速的同时不降低精度。

## 方法详解

### 整体框架

Chords 将 K 个计算核组织为从慢到快的层级求解器序列。最慢的核从时间 t=0（纯噪声）开始完整求解 ODE，而较快的核从更晚的时间点启动，先用粗糙的单步跳跃初始化，再通过流水线式的核间纠偏获得与慢速核相当的精度。

### 关键设计

1. **多核纠偏（Multi-core Rectification）**：核心操作。当慢速核 k-1 到达快速核 k 的某个时间点时，用两者在同一时间步的差异来纠正快速核的轨迹。纠偏项定义为：

    $\mathbf{r}_\theta(\mathbf{x}_t, \tilde{\mathbf{x}}_t, t, \delta_t) = \delta_t \cdot (\mathbf{f}_\theta(\mathbf{x}_t, t) - \mathbf{f}_\theta(\tilde{\mathbf{x}}_t, t)) + \mathbf{x}_t - \tilde{\mathbf{x}}_t$

   **理论保证**（Proposition 2.1）：在 f 充分光滑的条件下，纠偏后的误差相比纠偏前是高阶小量，即 $\|\text{误差后}\| = o(\|\text{误差前}\|)$。这意味着信息可以从最精确的核逐层传递到最快的核，有效抑制误差积累。

2. **初始化序列选择**：通过定义一个代理奖励函数 $\mathcal{R}(\mathbf{I})$（满足最优性、单调性、效率-精度权衡三个公理），将 K 核的最优初始化时间分配问题分解为一系列三核优化子问题。Theorem 2.5 给出了封闭解：当加速比 $s \leq 3$ 时，中间核初始化在 $t^{(2)} = t^{(3)}/2$；当 $s > 3$ 时，$t^{(2)} = 2t^{(3)} - 1$。一般 K 核的情况通过从快到慢的递推确定。

3. **离散化实现**：将连续框架转化为实际算法（Algorithm 1）。每个核按照调度器（Scheduler）确定当前和下一步的离散时间步，同时执行前向求解。通信条件由核间时间步差的整除性决定，保证流水线无空泡。

### 训练策略

Chords 完全无训练——不修改预训练扩散模型的任何参数，仅通过调度多核的前向推理过程实现加速。它与 DDIM、Euler 等任意 ODE 求解器兼容。

## 实验关键数据

### 主实验

在三个视频扩散模型和两个图像扩散模型上对比 ParaDIGMS 和 SRDS：

| 模型 | 核数 | 方法 | 加速比 | 质量 (VBench/CLIP) | Latent RMSE |
|------|------|------|--------|-------------------|-------------|
| HunyuanVideo | 4 | Sequential | 1.0× | 84.4% | - |
| HunyuanVideo | 4 | SRDS | 1.4× | 84.2% | 0.068 |
| HunyuanVideo | 4 | **Chords** | **2.1×** | 84.1% | 0.066 |
| HunyuanVideo | 8 | SRDS | 2.6× | 84.2% | 0.068 |
| HunyuanVideo | 8 | **Chords** | **2.9×** | 84.1% | 0.068 |
| Flux | 8 | SRDS | 2.3× | 31.0 | 0.183 |
| Flux | 8 | **Chords** | **2.6×** | 31.0 | 0.179 |

### 消融实验

| 核数 | 初始化 | HunyuanVideo 加速 | VBench | Flux 加速 | CLIP |
|------|---------|-------------------|--------|-----------|------|
| 8 | Ours | 2.9× | 84.1% | 2.4× | 31.0 |
| 8 | Uniform | 2.6× | 84.0% | 2.2× | 30.9 |
| 4 | Ours | 2.1× | 84.1% | 2.0× | 31.1 |
| 4 | Uniform | 1.8× | 84.2% | 1.8× | 31.0 |

理论驱动的非均匀初始化序列在所有设置下一致优于均匀分布，验证了 Theorem 2.5 的实用价值。

### 关键发现

- 4 核时 Chords 比 SRDS 快约 50%（1.4× vs 2.1×），8 核时优势更大
- 随着总扩散步数 N 增大（50→100），加速比从 2.9× 提升到 3.6×，同时质量还略有提升
- 方法天然支持"扩散流式"范式——快速核先输出粗略结果，慢速核随后提供更高质量的输出

## 亮点与洞察

- **理论与实践高度统一**：从连续 ODE 分析出发推导最优初始化，再离散化为实用算法，整个设计链路严谨
- **完全无训练、模型无关**：仅需多卡推理即可对任意扩散模型加速，部署门槛极低
- **流式输出**：层级结构天然支持渐进式质量提升，适合交互式应用

## 局限性 / 可改进方向

- 需要多个 GPU 核同时可用，单卡场景不适用
- 理论最优初始化基于简化的线性 ODE 代理函数，与实际非线性神经网络 ODE 存在 gap
- 未探索与模型蒸馏、注意力并行等正交加速方法的组合效果
- 对不同模型的通信开销和负载均衡未深入分析

## 相关工作与启发

- **ParaDIGMS**（Picard 迭代并行）和 **SRDS**（自纠偏多网格）可视为本文框架的特例
- 与模型并行（如 xDiT 的注意力分布）正交，可组合使用
- 流式输出机制可能对交互式视频编辑等应用有特殊价值

## 评分

- 新颖性：⭐⭐⭐⭐⭐ — 从多重网格 ODE 理论出发的全新视角
- 理论深度：⭐⭐⭐⭐⭐ — 完整的理论分析和最优性证明
- 实验充分度：⭐⭐⭐⭐⭐ — 5 个模型、多种核数配置、充分消融
- 实用性：⭐⭐⭐⭐ — 需要多卡但部署简单

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation](a0_affordance_aware_hierarchical_model_robotic_manipulation.md)
- [\[ICCV 2025\] End-to-End Multi-Modal Diffusion Mamba](end-to-end_multi-modal_diffusion_mamba.md)
- [\[ICCV 2025\] FlowDPS: Flow-Driven Posterior Sampling for Inverse Problems](flowdps_flow-driven_posterior_sampling_for_inverse_problems.md)
- [\[ICCV 2025\] Holistic Unlearning Benchmark: A Multi-Faceted Evaluation for Text-to-Image Diffusion Model Unlearning](holistic_unlearning_benchmark_a_multi-faceted_evaluation_for_text-to-image_diffu.md)
- [\[ICCV 2025\] StyleMotif: Multi-Modal Motion Stylization using Style-Content Cross Fusion](stylemotif_multi-modal_motion_stylization_using_style-content_cross_fusion.md)

</div>

<!-- RELATED:END -->
