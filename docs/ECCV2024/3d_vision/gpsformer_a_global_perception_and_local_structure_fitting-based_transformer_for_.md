---
title: >-
  [论文解读] GPSFormer: A Global Perception and Local Structure Fitting-Based Transformer for Point Cloud Understanding
description: >-
  [ECCV 2024][3D视觉][点云理解] 提出GPSFormer，通过全局感知模块(GPM)学习短程和长程依赖关系，并利用Taylor级数启发的局部结构拟合卷积(LSFConv)精确建模局部几何信息，在ScanObjectNN上以2.36M参数达到95.4%准确率，超越所有监督学习和预训练方法。
tags:
  - "ECCV 2024"
  - "3D视觉"
  - "点云理解"
  - "全局感知"
  - "可变形图卷积"
  - "局部结构拟合"
  - "Taylor级数"
---

# GPSFormer: A Global Perception and Local Structure Fitting-Based Transformer for Point Cloud Understanding

**会议**: ECCV 2024  
**arXiv**: [2407.13519](https://arxiv.org/abs/2407.13519)  
**代码**: [https://github.com/changshuowang/GPSFormer](https://github.com/changshuowang/GPSFormer)  
**领域**: 3D视觉  
**关键词**: 点云理解, 全局感知, 可变形图卷积, 局部结构拟合, Taylor级数

## 一句话总结

提出GPSFormer，通过全局感知模块(GPM)学习短程和长程依赖关系，并利用Taylor级数启发的局部结构拟合卷积(LSFConv)精确建模局部几何信息，在ScanObjectNN上以2.36M参数达到95.4%准确率，超越所有监督学习和预训练方法。

## 研究背景与动机

1. **领域现状**: 点云理解已广泛应用于自动驾驶、机器人和公共安全等领域，但由于点云的无序性和不规则性，有效提取形状信息仍是挑战。现有方法包括基于多视图/体素的间接方法、基于局部特征聚合的直接方法、以及基于预训练的方法。
2. **现有痛点**: (1) PointNet等方法忽略了局部结构信息；(2) PointNet++等局部聚合方法忽略了点之间的长程依赖关系；(3) 现有Transformer方法很少同时考虑短程依赖、长程依赖和局部结构建模；(4) 预训练方法虽然提升了性能，但需要大量外部数据且训练时间长。
3. **核心矛盾**: 如何在不依赖外部数据的情况下，同时捕获全局上下文信息和精细的局部几何结构。
4. **本文目标**: 设计一个纯监督学习的Transformer，同时学习全局感知和局部结构拟合，以精确捕获点云的形状信息。
5. **切入角度**: 将全局感知分解为短程依赖(ADGConv)和长程依赖(MHA)，将局部结构建模转化为Taylor级数的多项式拟合问题。
6. **核心 idea**: 用自适应可变形图卷积+多头注意力捕获多尺度全局依赖，用Taylor级数拟合局部几何结构的低阶基础和高阶细节信息。

## 方法详解

### 整体框架

GPSFormer由两个核心组件堆叠构成：**全局感知模块(GPM)** 和 **局部结构拟合卷积(LSFConv)**。分类任务使用3级GPS块级联(特征维度64→128→256)，分割任务使用5级GPS块编码器+U-Net解码器。每个GPS块中，先用GPM进行全局感知，再通过FPS采样+LSFConv进行局部结构拟合。

### 关键设计

1. **自适应可变形图卷积(ADGConv)**: 学习特征空间中相似特征的短程依赖。核心思路是为每个采样点学习一个特征偏移 $\Delta(f_i) = \phi(f_i)$，将特征变换为 $\hat{f}_i = f_i + \Delta(f_i)$，然后以变换后的特征为中心构建动态图进行特征聚合。这种"漫游"机制使点特征能够在整个特征空间中灵活导航，构建合适的局部邻域，避免了K值选取对感受野的影响。设计动机是传统KNN构建的动态图受K值影响大：K小则局限于局部，K大则引入语义无关点。

2. **残差交叉注意力(RCA)**: 融合变换前后的特征信息。公式为 $f_i^r = f_i^a + \text{Attn}(\hat{f}_i, f_i^a, f_i^a)$，其中 $\hat{f}_i$ 作为Query，ADGConv输出 $f_i^a$ 作为Key和Value。通过残差连接增强上下文结构理解。

3. **多头注意力(MHA)**: 捕获特征空间中所有位置间的长程依赖关系。RCA的输出 $f_i^r$ 经过标准自注意力机制 $f_i^g = \text{Softmax}(\frac{Q_i K^T}{\sqrt{h}})V$ 进一步增强全局表征能力。

4. **局部结构拟合卷积(LSFConv)**: 受Taylor级数 $f(x) = f(a) + \sum_{n=1}^{\infty} a_n(x-a)^n$ 启发，将局部结构表示分解为低阶分量和高阶分量：

   $$f(\{f_j\}_{j=1}^{K}) \approx f_i^L + f_i^H = \mathcal{A}(\{\phi(f_j)\}_{j=1}^{K}) + \mathcal{A}(\{\mathcal{T}(f_i, f_j)\}_{j=1}^{K})$$

   其中 $f_i^L$ 为**低阶卷积(LOConv)**，拟合局部结构的平坦部分和整体趋势；$f_i^H$ 为**高阶卷积(HOConv)**，拟合边缘和细节部分。HOConv使用新颖的仿射基函数：

   $$\mathcal{T}(f_i, f_j) = \left(\frac{w_j \cdot (f_j - f_i)}{|w_j \cdot (f_j - f_i)|}\right)^s \cdot |w_j \cdot (f_j - f_i)|^p$$

   当 $s=1, p=1$ 时退化为ABF，$s=0, p=2$ 时退化为RBF，通过可学习参数 $p$ 获得更强的表达能力。

5. **显式几何结构引入**: 权重 $w_j = \xi(h(p_i, p_j))$，其中 $h(p_i, p_j) = [p_i, p_j, p_j - p_i, \|p_i, p_j\|]$，利用采样点与邻近点的坐标交互信息学习权重，增强局部形状感知。

### 损失函数 / 训练策略

- 分类任务使用交叉熵损失，支持voting机制（多次随机采样取多数投票）
- LSFConv在每个阶段采用多尺度策略：球查询构建多尺度半径 $\{0.1, 0.2, 0.4\}$，对应邻域点数 $\{8, 16, 32\}$
- 多尺度参数在各阶段保持一致，避免参数调优

## 实验关键数据

### 主实验

| 数据集 | 指标 | GPSFormer | 之前SOTA | 提升 |
|--------|------|-----------|----------|------|
| ScanObjectNN (PB_T50_RS) | OA | **95.4%** | DeLA 90.4% (监督) / PointGPT 93.6% (预训练) | +5.0% / +1.8% |
| ScanObjectNN (PB_T50_RS) | mAcc | **93.8%** | DeLA 89.3% (监督) | +4.5% |
| ModelNet40 | OA | 94.2% | PointGPT 94.9% (预训练) | 接近饱和 |
| ShapeNetPart | class mIoU | **85.4%** | SPoTr 85.4% | 持平最佳 |
| ShapeNetPart | inst mIoU | 86.8% | SPoTr 87.2% | -0.4% |

### 消融实验

| 配置 | OA (%) | 说明 |
|------|--------|------|
| 仅ADGConv | 93.2 | 有效提取局部特征 |
| 仅RCA | 88.7 | 贡献全局关系 |
| 仅MHA | 89.6 | 捕获依赖关系 |
| ADGConv + RCA | 94.4 | 互补性显著 |
| ADGConv + MHA | 95.0 | 验证有效性 |
| ADGConv + RCA + MHA (完整) | **95.4** | 三者协同最优 |

| HOConv参数设置 | OA (%) | 说明 |
|---------------|--------|------|
| ABF (s=1, p=1固定) | 92.8 | 退化为仿射基函数 |
| RBF (s=0, p=2固定) | 93.2 | 退化为径向基函数 |
| s=0, p可学习 | 94.6 | 自适应参数有效 |
| s=1, p可学习 | **95.4** | 最优配置 |

### 关键发现

- GPSFormer-elite（0.68M参数）仍可达93.3% OA，表明模型设计高效
- ADGConv的邻域大小K=20为最优，过大或过小都会降低性能
- 模型仅2.36M参数、0.7G FLOPS，远低于MVTN(11.2M)和PointMLP(12.6M)
- 在Few-shot设置下（5-way 10-shot）GPSFormer在ScanObjectNN上达89.3%，远超PointNeXt的72.4%

## 亮点与洞察

- **纯监督学习超越预训练方法**：不依赖任何外部数据，仅靠精妙的结构设计就超越了PointGPT等预训练方法，说明模型结构本身的表达能力至关重要
- **Taylor级数的巧妙应用**：将局部结构拟合问题转化为多项式拟合，低阶拟合平坦部分、高阶拟合边缘细节，思路优雅且有效
- **极致的参数效率**：2.36M参数实现95.4%准确率，参数效率极高
- **可变形图卷积的创新**：通过学习特征偏移实现特征空间漫游，比传统KNN更灵活

## 局限与展望

- ModelNet40上性能接近饱和（94.2%），但该数据集已不足以区分方法优劣
- 分割任务性能略低于SPoTr，可能需要针对分割任务优化网络结构
- 多尺度策略参数固定（半径0.1/0.2/0.4），可探索自适应多尺度机制
- 未探索预训练+GPSFormer的结合，可能进一步提升上限

## 相关工作与启发

- 与DGCNN的动态图卷积相比，ADGConv通过特征偏移实现更灵活的邻域构建
- Taylor级数拟合思路可推广到其他需要局部结构建模的任务
- GPM的短程+长程依赖建模框架可启发其他3D理解任务的模型设计

## 评分

- 新颖性: ⭐⭐⭐⭐ Taylor级数拟合局部结构和自适应可变形图卷积都是有新意的设计
- 实验充分度: ⭐⭐⭐⭐⭐ 三个任务+详细消融+few-shot+模型复杂度分析+可视化，非常全面
- 写作质量: ⭐⭐⭐⭐ 条理清晰，公式推导完整，图表丰富
- 价值: ⭐⭐⭐⭐ 纯监督方法超越预训练方法具有重要意义，参数效率出色

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] DG-PIC: Domain Generalized Point-In-Context Learning for Point Cloud Understanding](dg-pic_domain_generalized_point-in-context_learning_for_point_cloud_understandin.md)
- [\[CVPR 2026\] Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding](../../CVPR2026/3d_vision/mamba_learns_in_context_structure-aware_domain_generalization_for_multi-task_poi.md)
- [\[ECCV 2024\] TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos](tram_global_trajectory_and_motion_of_3d_humans_from_in-the-wild_videos.md)
- [\[CVPR 2025\] PMA: Towards Parameter-Efficient Point Cloud Understanding via Point Mamba Adapter](../../CVPR2025/3d_vision/pma_towards_parameter-efficient_point_cloud_understanding_via_point_mamba_adapte.md)
- [\[ECCV 2024\] SegPoint: Segment Any Point Cloud via Large Language Model](segpoint_segment_any_point_cloud_via_large_language_model.md)

</div>

<!-- RELATED:END -->
