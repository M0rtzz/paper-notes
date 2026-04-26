---
title: >-
  [论文解读] RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations
description: >-
  [CVPR 2026][3D视觉][3D重建] 提出 RnG，一个统一的前馈 Transformer，通过重建引导的因果注意力机制将 KV-Cache 作为隐式 3D 表征，从少量无姿态图像中同时完成 3D 重建和新视角 RGBD 生成，推理速度比扩散方法快 100 倍以上。
tags:
  - CVPR 2026
  - 3D视觉
  - 3D重建
  - 新视角合成
  - KV-Cache
  - 因果注意力
  - Transformer
---

# RnG: A Unified Transformer for Complete 3D Modeling from Partial Observations

**会议**: CVPR 2026  
**arXiv**: [2603.01194](https://arxiv.org/abs/2603.01194)  
**代码**: [https://npucvr.github.io/RnG](https://npucvr.github.io/RnG)  
**领域**: 3D视觉 / 重建与生成  
**关键词**: 3D重建, 新视角合成, KV-Cache, 因果注意力, 前馈Transformer

## 一句话总结

提出 RnG，一个统一的前馈 Transformer，通过重建引导的因果注意力机制将 KV-Cache 作为隐式 3D 表征，从少量无姿态图像中同时完成 3D 重建和新视角 RGBD 生成，推理速度比扩散方法快 100 倍以上。

## 研究背景与动机

1. **领域现状**：可泛化 3D 重建（DUSt3R、VGGT）能从稀疏图像恢复可见区域几何，但不建模未见区域。新视角合成（LVSM）可生成未见视角图像但缺乏一致的 3D 结构。
2. **现有痛点**：重建方法输出不完整（仅可见区域），NVS 方法缺乏 3D 一致性或依赖已知相机姿态。Matrix3D 虽统一两任务但扩散设计导致推理极慢（27秒/视角）。
3. **核心矛盾**：如何在单个模型中统一重建和生成，同时保持实时推理能力？
4. **本文目标**：利用 3D 重建基础模型的潜在 3D 理解能力，通过神经渲染激活并显式化这种理解。
5. **切入角度**：将重建先验迁移到生成（而非常见的生成先验辅助重建），是反向知识迁移。
6. **核心 idea**：因果注意力掩码使源视图 Token 不受目标视图影响，KV-Cache 自然成为可复用的隐式 3D 表征。

## 方法详解

### 整体框架

源视图图像经 DINO 提取 Token，目标视图编码为 Plücker 射线图。所有 Token 经 24 层交替的全局/帧注意力处理。源视图 Token 用于姿态估计，目标视图 Token 经 DPT 头生成 RGB 和点图。

### 关键设计

1. **重建引导的因果注意力**:

    - 功能：在注意力层面解耦重建和生成任务
    - 核心思路：引入二值掩码 $M$，禁止源视图 Query 关注目标视图 Key。源视图 Token 仅关注源视图（重建），目标视图 Token 关注所有视图（生成）。两个任务共享网络参数但通过注意力掩码分离。
    - 设计动机：重建应引导生成但生成不应干扰重建。此设计确保给定不同目标视图时源视图重建结果一致。

2. **KV-Cache 作为隐式 3D 表征**:

    - 功能：支持高效的两阶段推理
    - 核心思路：因果注意力使源视图 Token 的处理独立于目标视图。因此可先缓存源视图的 K/V Token（重建阶段，~0.2s），后续对任意目标视角仅需前向目标 Token 并读取缓存（生成阶段，<0.1s）。
    - 设计动机：KV-Cache 机制使同一场景的多视角生成极其高效，类似语言模型的自回归推理。

3. **重建先验驱动的生成**:

    - 功能：利用 3D 重建知识提升新视角生成质量
    - 核心思路：继承 VGGT 预训练权重和架构。RGB 头和点图头分别解码目标视角外观和几何。通过多视角点图积累可获得完整 3D 结构——如同"虚拟 3D 扫描仪"。
    - 设计动机：实验证明重建先验迁移到生成是可行且有效的，比从扩散先验迁移更高效。

### 损失函数 / 训练策略

$\mathcal{L} = \mathcal{L}_{RGB} + \lambda_{pmap}\mathcal{L}_{pmap} + \lambda_c\mathcal{L}_{cam}$。RGB 损失 = MSE + 感知损失；点图损失 = 不确定性加权 L1；姿态损失 = Huber loss。8 × A800 训练 40K 步。

## 实验关键数据

### 主实验

| 方法 | 姿态 RA@5↑ | 源深度 Rel↓ | 新视角深度 Rel↓ | NVS PSNR↑ | 3D CD↓ |
|------|-----------|-----------|-------------|----------|--------|
| RnG (无姿态) | 85.1 | 0.584 | 0.717 | 26.28 | 0.0067 |
| VGGT (无姿态) | 74.2 | 5.96 | - | - | 0.0260 |
| Matrix3D (无姿态) | 43.8 | 9.43 | 9.96 | 18.74 | 0.0670 |
| LVSM (需姿态) | - | - | - | 27.52 | - |

### 消融实验

| 配置 | NVS PSNR | 说明 |
|------|----------|------|
| 从头训练 (15K) | 20.78 | 无重建先验 |
| 预训练初始化 (15K) | 24.86 | 重建先验有效 |
| 全注意力 (无因果掩码) | 24.86 | 性能相当但无法用 KV-Cache |
| 有 KV-Cache | 85ms推理 | 无 KV-Cache 213ms |

### 关键发现

- 无姿态 RnG 在 NVS 上接近最佳需姿态方法 LVSM，同时提供姿态和 3D 几何
- 重建先验的重要性：预训练初始化 vs 从头训练相差 4+ dB
- 因果注意力不损失精度但实现 2.5× 推理加速（213ms → 85ms）
- RnG 推理比 Matrix3D 快 300+ 倍（85ms vs 27s）

## 亮点与洞察

- **反向知识迁移**：首次系统性展示重建先验→生成的有效性，挑战了"生成先验辅助重建"的传统范式
- **KV-Cache 的新解释**：将语言模型的 KV-Cache 重新诠释为隐式 3D 表征，概念上优雅
- **"虚拟 3D 扫描仪"**：通过积累多视角查询的点图即可获得完整 3D，无需显式 3D 重建算法

## 局限与展望

- 缺乏精细纹理细节（与扩散方法相比），可考虑引入图像生成预训练
- 世界原点定义依赖输入视角交叉，限制了手持设备的实际应用
- 从多视角积累 3D 可能引入噪声和冲突

## 相关工作与启发

- **vs VGGT**: VGGT 仅重建可见区域，RnG 在其基础上添加生成能力得到完整 3D
- **vs Matrix3D**: 同为统一模型但 RnG 是确定性前馈（实时），Matrix3D 是扩散方法（27s）
- **vs LVSM**: LVSM 需已知姿态且无 3D 几何，RnG 同时提供姿态、几何和外观

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ KV-Cache 作为 3D 表征的概念极具启发性
- 实验充分度: ⭐⭐⭐⭐ 多任务多指标全面评估 + 消融充分
- 写作质量: ⭐⭐⭐⭐⭐ 动机清晰，架构图直观
- 价值: ⭐⭐⭐⭐⭐ 为统一 3D 重建与生成提供了高效范式

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Learning 3D Reconstruction with Priors in Test Time](tco_learning_3d_reconstruction_with_priors_in_test_time.md)
- [\[CVPR 2026\] Scaling View Synthesis Transformers (SVSM)](scaling_view_synthesis_transformers.md)
- [\[CVPR 2026\] GGPT: Geometry-Grounded Point Transformer](ggpt_geometry_grounded_point_transformer.md)
- [\[CVPR 2026\] PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](pr-iqa_partial-reference_image_quality_assessment_for_diffusion-based_novel_view.md)
- [\[CVPR 2026\] LitePT: Lighter Yet Stronger Point Transformer](litept_lighter_yet_stronger_point_transformer.md)

<!-- RELATED:END -->
