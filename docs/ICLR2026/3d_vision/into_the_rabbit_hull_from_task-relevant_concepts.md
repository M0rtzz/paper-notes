---
title: >-
  [论文解读] Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry
description: >-
  [ICLR 2026][3D视觉][可解释性] 本文通过稀疏自编码器（SAE）从 DINOv2 中提取 32,000 个视觉概念字典，系统研究了不同下游任务（分类/分割/深度估计）如何选择性地使用这些概念，揭示了表示空间的几何结构超越了线性稀疏编码假说（LRH），并提出了基于 Minkowski 和的新表示假说（MRH），认为 token 是多个凸混合的叠加。
tags:
  - ICLR 2026
  - 3D视觉
  - 可解释性
  - 视觉表示
  - 稀疏自编码器
  - DINOv2
  - 概念发现
---

# Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry

**会议**: ICLR 2026  
**arXiv**: [2510.08638](https://arxiv.org/abs/2510.08638)  
**代码**: 无  
**领域**: 3D视觉  
**关键词**: 可解释性, 视觉表示, 稀疏自编码器, DINOv2, 概念发现  

## 一句话总结

本文通过稀疏自编码器（SAE）从 DINOv2 中提取 32,000 个视觉概念字典，系统研究了不同下游任务（分类/分割/深度估计）如何选择性地使用这些概念，揭示了表示空间的几何结构超越了线性稀疏编码假说（LRH），并提出了基于 Minkowski 和的新表示假说（MRH），认为 token 是多个凸混合的叠加。

## 背景与动机

1. **DINOv2 表示的黑箱问题**：DINOv2 作为自监督视觉基础模型在分类、分割、深度估计、机器人感知等多个下游任务中表现优异，但其内部"到底编码了什么"仍然不清楚。理解其表示结构对于改进和控制模型至关重要。

2. **线性表示假说的局限**：现有的可解释性工作大多基于线性表示假说（LRH），假设特征是近正交方向的稀疏叠加。然而 LRH 能否完整描述视觉 Transformer 的表示结构尚未得到充分验证。

3. **概念级解释的需求**：传统归因方法（如 Grad-CAM）只能回答"模型看了哪里"，无法回答"模型计算了什么特征"。基于概念的解释方法需要一种系统化的特征提取框架。

4. **SAE 稳定性问题**：朴素的稀疏自编码器在不同训练运行中产生不一致的特征，严重损害可解释性。需要稳定的字典学习方法来获得可复现的概念。

5. **任务特异性分析缺失**：现有工作很少系统研究不同下游任务如何从同一表示空间中选择性地招募不同的概念子集，以及这些概念在几何上的组织方式。

6. **表示几何的深层结构**：初步观察表明表示空间存在各向异性、反极对、低秩任务子空间等现象，这些都无法用简单的稀疏编码模型解释，需要更精细的几何假说。

## 方法详解

### 稳定稀疏自编码器

作者使用 DINOv2-B（带 4 个 register token）作为特征提取器，在 140 万张 ImageNet-1K 图像上训练稳定 SAE。具体设置：

- **字典规模**：$c = 32{,}000$ 个原子，远大于嵌入维度 $d = 768$（超完备性）
- **稀疏度**：每个 token 仅激活 $k = 8$ 个概念
- **稳定性约束**：每个字典原子被约束在真实激活的凸包内（$\bm{D}_i \in \text{conv}(\bm{A})$），通过 128,000 个 k-means 聚类中心近似凸包
- **参数化**：$\bm{D} = \bm{S}\bm{C}$，其中 $\bm{S}$ 是行随机矩阵，$\bm{C}$ 是聚类中心
- **编码器**：单层编码器 + BatchTopK 投影产生稀疏编码 $\bm{Z}$
- **重建质量**：$R^2 > 88\%$

### 任务特异性概念分析

通过分析下游任务的线性探测头 $\bm{W}$ 与概念字典的交互，定义概念重要性：

$$\text{Importance} = \mathbb{E}(\bm{Z}) \cdot \bm{W}' = \mathbb{E}(\bm{Z}) \cdot \bm{D}\bm{W}^{\mathsf{T}}$$

这一评分在线性情况下是最优的忠实度度量（基于 C-Deletion、C-Insertion 等标准）。

### 三大发现

**Part I: 下游任务招募不同的概念**

- **分类 → "Elsewhere"概念**：最重要的概念不仅包含目标对象，还包含一种全新的"Elsewhere"概念——在目标对象所在位置之外的区域激活。这些概念实现了一种模糊空间逻辑："对象存在于别处，但当前 token 不是该对象"。
- **分割 → 边界概念**：前 50 个最重要概念全部沿物体轮廓激活，形成一个紧密的低维子空间。
- **深度估计 → 三类单目深度线索**：透视几何线索（消失线）、阴影线索（光照梯度）、频率过渡线索（纹理细节变化）。

**Part II: 概念几何与统计**

- 字典原子并非近正交（偏离 Grassmannian 框架），存在显著的局部相干性
- 存在反极对（$\cos\theta \approx -1$），编码语义对立概念（如"左/右"、"黑/白"）
- 奇异值谱快速衰减，表明表示空间各向异性
- 3 个异常密集概念编码位置信息（左/右/下），在整个数据集上频繁激活

**Part III: Minkowski 表示假说**

提出 MRH：激活空间是多个凸多面体的 Minkowski 和：

$$\mathcal{X} = \bigoplus_{i=1}^{m} \mathcal{P}_i, \quad \bm{x} = \sum_{i \in S} \bm{z}_i \mathcal{A}_{\mathcal{T}_i}$$

其中每个 tile $\mathcal{T}_i$ 对应一组原型（如动物类别、颜色、纹理），$\bm{z}_i$ 是凸系数（在单纯形上）。这一结构被多头注意力机制自然实现：每个注意力头产生 value 向量的凸组合，多头输出相加形成 Minkowski 和。

## 实验结果

### 任务概念招募的差异性分析

| 分析维度 | 分类 | 分割 | 深度估计 |
|---------|------|------|---------|
| 概念覆盖范围 | 广泛分散 | 紧凑局部 | 紧凑局部 |
| Top-100 概念内聚性 | 中等 | 高（边界子空间） | 高（三类线索） |
| 特征谱衰减速度 | 中等 | 快速 | 快速 |
| 概念类型 | Elsewhere + 物体概念 | 边界检测器 | 透视/阴影/频率 |

### SAE 字典几何分析

| 指标 | SAE 字典 | 随机基线 | Grassmannian |
|------|---------|---------|-------------|
| 内积分布尾部 | 重尾（高相干性） | 窄分布 | 最窄（理想正交） |
| 奇异值衰减 | 最快（低有效秩） | 中等 | 最慢 |
| Hoyer 稀疏度 | ~0.25（分布式编码） | ~0.20 | N/A |
| 反极对比例 | 显著存在 | 几乎不存在 | 不存在 |

### Register Token 的全局概念

作者发现数百个概念专门在 register token 上激活，编码全局场景属性（运动模糊、光照风格、焦散反射、镜头效果），而 cls token 仅有 1 个专属概念。这揭示了 DINOv2 在结构上将局部（patch token）和全局（register token）信息进行了分离。

## 亮点

- **首个大规模视觉概念字典**：32,000 个可解释概念 + 最大的交互式可视化 demo，为视觉模型可解释性提供了基础设施
- **"Elsewhere"概念的发现**：揭示了 DINO 通过"条件否定"进行分类的非直觉机制，挑战了传统热力图解释的假设
- **MRH 假说**：将认知科学（Gärdenfors 概念空间）与多头注意力机制的数学结构巧妙连接，提供了超越 LRH 的新理论框架
- **稳定 SAE 方法**：通过凸包约束保证字典原子在分布内，解决了 SAE 跨运行不一致的问题

## 局限性

- MRH 目前主要是定性假说，缺乏严格的定量验证标准来判断表示是否"真正"服从 Minkowski 和结构
- 分析仅限于 DINOv2-B 一个模型，尚不清楚结论是否推广到其他视觉 Transformer（如 CLIP、MAE、SigLIP）
- "Elsewhere"概念的因果机制尚未完全阐明——是模型显式学习的策略还是训练的副产品
- 凸包约束的 SAE 虽然稳定，但可能限制了某些概念的表达能力（无法表示凸包外的方向）
- 缺乏与其他概念发现方法（如 NMF、PCA、ICA）的系统对比

## 相关工作对比

| 维度 | 本文 | Bricken et al. 2023 (Anthropic SAE) | Cunningham et al. 2023 |
|------|------|--------------------------------------|----------------------|
| 领域 | 视觉（DINOv2） | 语言（Claude） | 语言模型 |
| 字典规模 | 32,000 | 4,096–131,072 | 数千 |
| 稳定性 | 凸包约束保证 | 无稳定性保证 | 无稳定性保证 |
| 几何分析 | 深入（Grassmannian、MRH） | 初步 | 初步 |
| 下游任务分析 | 三类任务对比 | 无 | 无 |

| 维度 | 本文 | Park et al. 2024 (LRH) | Gärdenfors 2004 |
|------|------|------------------------|-----------------|
| 假说 | MRH（Minkowski 和） | LRH（线性稀疏叠加） | 概念空间（凸区域） |
| 适用对象 | 视觉 Transformer | 语言模型 | 认知科学理论 |
| 操作化 | SAE + 凸几何 | SAE / 探针 | 无计算实现 |
| 核心结构 | 凸多面体的和 | 近正交方向 | 凸区域 + 原型 |

## 评分

- ⭐⭐⭐⭐⭐ 创新性：提出 MRH 假说，将认知科学理论与注意力机制的数学结构对齐，极具原创性
- ⭐⭐⭐⭐⭐ 实验充分度：大规模字典 + 三类下游任务 + 多维几何分析 + 交互式 demo，分析极为详尽
- ⭐⭐⭐⭐ 写作质量：结构清晰、图表极其精美，但论文整体偏长且 Part III 的理论严谨性有提升空间
- ⭐⭐⭐⭐ 实用价值：概念字典和 demo 可直接用于解释和调试视觉模型，MRH 对表示工程有指导意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] EgoNight: Towards Egocentric Vision Understanding at Night with a Challenging Benchmark](egonight_towards_egocentric_vision_understanding_at_night_with_a_challenging_ben.md)
- [\[ICLR 2026\] Quantized Visual Geometry Grounded Transformer](quantized_visual_geometry_grounded_transformer.md)
- [\[ICLR 2026\] Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](ctrlshift_high-quality_geometry-aware_object_manipulation_in_visual_generation.md)
- [\[ICLR 2026\] Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints](generalizable_coarse-to-fine_robot_manipulation_via_language-aligned_3d_keypoint.md)
- [\[ICLR 2026\] GIQ: Benchmarking 3D Geometric Reasoning of Vision Foundation Models with Simulated and Real Polyhedra](giq_benchmarking_3d_geometric_reasoning_of_vision_foundation_models_with_simulat.md)

</div>

<!-- RELATED:END -->
