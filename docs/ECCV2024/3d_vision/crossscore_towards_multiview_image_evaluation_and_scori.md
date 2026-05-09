---
title: >-
  [论文解读] CrossScore: Towards Multi-View Image Evaluation and Scoring
description: >-
  [ECCV 2024][3D视觉][图像质量评估] 提出 CrossScore——一种新型的交叉参考图像质量评估方法，利用多视角参考图像替代真实参考图，通过 cross-attention 机制预测 SSIM 分数图，在无需 ground truth 的条件下实现接近全参考指标的评估精度。
tags:
  - ECCV 2024
  - 3D视觉
  - 图像质量评估
  - 交叉参考
  - 新视角合成
  - SSIM预测
  - 跨视角
---

# CrossScore: Towards Multi-View Image Evaluation and Scoring

**会议**: ECCV 2024  
**arXiv**: [2404.14409](https://arxiv.org/abs/2404.14409)  
**代码**: [https://crossscore.active.vision](https://crossscore.active.vision)  
**领域**: 3D视觉  
**关键词**: 图像质量评估, 交叉参考, 新视角合成, SSIM预测, 跨视角

## 一句话总结

提出 CrossScore——一种新型的交叉参考图像质量评估方法，利用多视角参考图像替代真实参考图，通过 cross-attention 机制预测 SSIM 分数图，在无需 ground truth 的条件下实现接近全参考指标的评估精度。

## 研究背景与动机

### 领域现状

**领域现状**：IQA 现有方案的不足**：

### 现有痛点

**现有痛点**：全参考指标（FR-IQA）如 SSIM/PSNR 需要 ground truth，在 NVS 中限制了训练数据使用

### 核心矛盾

**核心矛盾**：无参考指标（NR-IQA）如 NIQE/BRISQUE 缺乏场景特定上下文分析能力

### 解决思路

**解决思路**：通用参考指标（GR-IQA）如 FID 只评估分布层面，不适合逐像素评估

### 补充说明

**补充说明**：多模态参考指标（MMR-IQA）如 CLIPScore 缺乏细粒度评估能力

### 补充说明

**补充说明**：NVS 评估痛点**：

### 补充说明

**补充说明**：子采样策略（留出测试图像）面临训练数据与评估统计相关性的平衡问题

### 补充说明

**补充说明**：真正新颖视角无法获得 ground truth，FR 指标无法使用

### 补充说明

**补充说明**：核心思路**：用同一场景的多视角图像替代 ground truth，实现"透视版 SSIM"

## 方法详解

### 整体框架

1. **Image Encoder**：使用预训练 DINOv2-small 提取查询图和参考图的特征
2. **Cross-Reference Module**：Transformer Decoder，查询图特征作为 query，参考图特征集作为 key/value
3. **Score Regression Head**：MLP 将 latent score map 解码为逐像素分数图

目标：学习函数 $g(\tilde{I}_q, \mathcal{I}_r) \mapsto \mathbf{S}_{cross} \approx \mathbf{S}_{ssim}$

### 关键设计

**自监督数据收集**
- 利用现有 NVS 系统（Gaussian Splatting、Nerfacto、TensoRF）在优化过程的不同 checkpoint 渲染图像
- 渲染图像与原始图像比较得到 SSIM map 作为训练标签
- 覆盖多种失真类型和程度，形成丰富训练集

**网络架构**
- DINOv2 patch-wise 编码，忽略 CLS token
- Cross-reference module：2 层 Transformer decoder，hidden dim 384
- Score regression head：2 层 MLP，最终每 patch 输出 14×14 分数图

**训练策略**
- L1 loss：$\mathcal{L} = |\mathbf{S}_{ssim} - \mathbf{S}_{cross}|$
- SSIM map 截断至 [0,1] 确保训练稳定
- 参考图数量 $N_{ref} = 5$

### 损失函数 / 训练策略

- 仅在 MFR 数据集上训练，使用 L1 损失
- Adam-W 优化器，学习率 5e-4
- 2× A5000 GPU，160K 迭代，60 小时
- 训练数据生成约两周（4× A5000），~1.5TB 存储

## 实验关键数据

### 主实验（与 SSIM 的 Pearson 相关系数）

| 数据集 | PSNR(FR) | BRISQUE(NR) | NIQE(NR) | PIQE(NR) | CrossScore(CR) |
|--------|----------|-------------|----------|----------|----------------|
| RE10K | 0.92 | 0.46 | 0.32 | 0.27 | **0.99** |
| Mip360 | 0.91 | 0.19 | 0.61 | 0.69 | **0.95** |
| MFR | 0.92 | 0.23 | -0.30 | -0.11 | **0.83** |

### 消融实验（Novel Trajectory IQA）

- 14 个场景的 SSIM vs CrossScore 排名相关系数（Spearman）= 0.84
- CrossScore 在无 ground truth 条件下成功区分不同质量的 NVS 渲染

### 关键发现

- CrossScore 与 SSIM 高度相关（RE10K 上 0.99），远超所有 NR 指标
- 仅在 MFR 上训练，成功泛化到 Mip360（室内外360°扫描）和 RE10K
- Few-shot NeRF 评估中，CrossScore 正确判断 IBRNet > PixelNeRF，与 FR 指标一致
- NR 指标在多个数据集上甚至出现负相关（如 NIQE 在 MFR 上 -0.30）

## 亮点与洞察

1. **开创 CR-IQA（交叉参考）新范式**，填补 FR 和 NR 之间的空白
2. **实用性极强**：NVS 评估可用全部图像训练，不再需要留出测试集
3. 自监督数据收集策略巧妙——利用 NVS 优化过程中自然产生的多级别失真
4. 支持任意分辨率输入（推理时）

## 局限与展望 / 可改进方向

- 仅预测 SSIM 这一种 FR 指标，可扩展到 LPIPS 等感知指标
- Cross-attention 计算量随参考图数量增长，大规模场景可能需要优化
- MFR 训练数据主要为室外建筑物，对其他场景类型（如人脸、文本）的泛化需验证
- 当前仅支持静态场景，动态场景评估待探索

## 相关工作与启发

- DINOv2 的 patch 级特征为跨视角匹配提供了强力基础
- NeRF/3DGS 的优化过程作为"失真生成器"是极具创意的自监督数据源
- 可启发：将 CR-IQA 推广到视频质量评估、3D 重建质量评估等领域

## 评分

- 新颖性：⭐⭐⭐⭐⭐（全新评估范式）
- 技术深度：⭐⭐⭐⭐
- 实验充分度：⭐⭐⭐⭐（多数据集验证 + 应用场景展示）
- 写作质量：⭐⭐⭐⭐⭐
- 综合推荐：⭐⭐⭐⭐

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](mvsplat_efficient_3d_gaussian_splatting_from_sparse_multi-view_images.md)
- [\[ECCV 2024\] MVDiffusion++: A Dense High-Resolution Multi-View Diffusion Model for Single or Sparse-View 3D Object Reconstruction](mvdiffusion_a_dense_high-resolution_multi-view_diffusion_model_for_single_or_spa.md)
- [\[ECCV 2024\] Vista3D: Unravel the 3D Darkside of a Single Image](vista3d_unravel_the_3d_darkside_of_a_single_image.md)
- [\[ECCV 2024\] Zero-Shot Multi-Object Scene Completion](zero-shot_multi-object_scene_completion.md)
- [\[ECCV 2024\] ZeST: Zero-Shot Material Transfer from a Single Image](zest_zero-shot_material_transfer_from_a_single_image.md)

</div>

<!-- RELATED:END -->
