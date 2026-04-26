---
title: >-
  [论文解读] Affostruction: 3D Affordance Grounding with Generative Reconstruction
description: >-
  [CVPR 2026][3D视觉][3D功能可供性] 提出Affostruction，通过稀疏体素融合的生成式重建完成物体几何（包括未观测区域），并用Flow Matching建模功能可供性的多模态分布，在完整3D形状上实现功能区域定位，重建IoU提升54.8%、affordance aIoU提升40.4%。
tags:
  - CVPR 2026
  - 3D视觉
  - 3D功能可供性
  - 生成式重建
  - 稀疏体素融合
  - Flow Matching
  - 主动视角选择
---

# Affostruction: 3D Affordance Grounding with Generative Reconstruction

**会议**: CVPR 2026  
**arXiv**: [2601.09211](https://arxiv.org/abs/2601.09211)  
**代码**: [项目页面](https://chrockey.github.io/Affostruction/)  
**领域**: 三维视觉 / 机器人感知  
**关键词**: 3D功能可供性, 生成式重建, 稀疏体素融合, Flow Matching, 主动视角选择

## 一句话总结

提出Affostruction，通过稀疏体素融合的生成式重建完成物体几何（包括未观测区域），并用Flow Matching建模功能可供性的多模态分布，在完整3D形状上实现功能区域定位，重建IoU提升54.8%、affordance aIoU提升40.4%。

## 研究背景与动机

机器人操作需要理解物体的功能可供性——"哪里可以抓握"。但现实中机器人只能从有限视角的RGBD相机观测物体，存在大量遮挡。现有方法只能在可见表面预测affordance，而机器人需要在未观测区域（如杯子背面的手柄）也能推理功能属性。这要求同时完成几何补全和affordance预测。

核心洞察：TRELLIS等3D生成模型有强大的几何先验但不支持深度输入和功能预测；affordance方法只在完整点云或可见表面上工作。Affostruction用稀疏体素融合扩展TRELLIS支持多视角RGBD输入，并新增Flow-based affordance模块。

## 方法详解

### 整体框架

多视角RGBD → DINOv2提取特征+深度投影到3D → 稀疏体素融合 → Flow Transformer生成式重建完整结构 → 稀疏Flow Transformer生成affordance热力图(CLIP文本条件) → Affordance引导的主动视角选择 → 输出完整3D网格+affordance标注。

### 关键设计

1. **稀疏体素融合条件化**:
    - 功能：将多视角RGBD特征聚合为常数复杂度的3D条件信号
    - 核心思路：每个视角的DINOv2特征通过深度和相机参数投影到3D世界坐标，重叠体素平均、非重叠取并集，加3D正弦位置编码
    - 设计动机：保持O(1)的token数量（不随视角数增长），使Flow Transformer能泛化处理1-8个视角

2. **Flow-based Affordance定位**:
    - 功能：在重建几何上生成affordance热力图
    - 核心思路：训练一个稀疏Flow Transformer从CLIP文本嵌入条件下去噪affordance logits，使用BCE+Dice的mask损失替代MSE
    - 设计动机：affordance本质上是多模态的——同一查询可能对应多个有效交互区域（如"抓握"的多个位置），生成模型能捕获这种分布

3. **Affordance驱动的主动视角选择**:
    - 功能：在有限视角预算下优先覆盖功能区域
    - 核心思路：将affordance热力图渲染到候选视角的2D图像，选择热力图值之和最大的视角作为下一观测点
    - 设计动机：一次额外视角即可实现2倍于顺序采样的改善

### 损失函数 / 训练策略

- 重建阶段：Rectified Flow的条件流匹配（CFM）损失
- Affordance阶段：BCE+Dice的mask损失替代MSE（binary affordance更适合mask损失）
- 随机多视角训练（每次迭代随机1-8个视角），使模型适应可变输入

## 实验关键数据

### 3D重建（Toky4K）

| 方法 | IoU↑ | CD↓ | 是否用深度 |
|------|------|-----|----------|
| TRELLIS | 19.49 | 0.3694 | ✗ |
| MCC | 21.11 | 0.3299 | ✓ |
| Affostruction | 32.67 | 0.2427 | ✓ |

### 部分观测Affordance定位

| 方法 | aIoU↑ | aCD↓ |
|------|-------|------|
| MCC + Espresso-3D | 4.74 | 0.1354 |
| Affostruction | 9.26 | 0.1044 |

### 主动视角选择

| 策略 | 1次额外视角aIoU | 4次额外视角aIoU |
|------|-----------------|-----------------|
| 顺序 | 4.7 | 9.1 |
| 随机 | 6.2 | 11.0 |
| Affordance驱动 | 9.2 | 12.4 |

### 关键发现

- 随机多视角训练至关重要：单视角训练的模型给多视角输入时几乎无提升
- BCE+Dice mask损失优于MSE用于affordance预测
- 生成式方法在aIoU上大幅超越判别式方法（19.1 vs 13.6），即使不微调编码器

## 亮点与洞察

- 首次将3D生成式重建与affordance预测统一到一个框架
- 稀疏体素融合实现了O(1)复杂度的多视角聚合
- Flow Matching建模affordance的多模态分布是优雅的设计
- 主动视角选择形成"感知→重建→定位→选择"的闭环

## 局限与展望

- 严重遮挡下初始重建可能有误差，传播到affordance预测
- 初始affordance估计错误会误导主动视角选择
- 当前仅支持单物体场景，多物体需结合SAM3D
- 未在真实机器人上验证操作可行性

## 相关工作与启发

- **vs OpenAD/PointRefer/Espresso-3D**: 仅预测可见表面affordance；Affostruction在完整重建几何上预测
- **vs TRELLIS**: 单RGB输入无深度无affordance；Affostruction扩展支持多视角RGBD+affordance
- **vs MCC**: 判别式重建仅恢复观测表面；Affostruction生成式外推未见区域

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 生成式重建+affordance定位+主动视角的统一框架首创
- 实验充分度: ⭐⭐⭐⭐ 重建/affordance/主动视角均有定量评估，消融完整
- 写作质量: ⭐⭐⭐⭐⭐ 问题定义清晰，方法模块化，失败案例分析诚实
- 价值: ⭐⭐⭐⭐⭐ 对机器人操作的affordance理解具有直接应用价值

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Scene Grounding In the Wild](scene_grounding_in_the_wild.md)
- [\[CVPR 2026\] AffordMatcher: Affordance Learning in 3D Scenes from Visual Signifiers](affordmatcher_affordance_learning_in_3d_scenes_from_visual_signifiers.md)
- [\[CVPR 2025\] Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions](../../CVPR2025/3d_vision/grounding_3d_object_affordance_with_language_instructions_visual_observations_an.md)
- [\[CVPR 2026\] AffordGrasp: Cross-Modal Diffusion for Affordance-Aware Grasp Synthesis](affordgrasp_cross-modal_diffusion_for_affordance-aware_grasp_synthesis.md)
- [\[CVPR 2025\] GREAT: Geometry-Intention Collaborative Inference for Open-Vocabulary 3D Object Affordance Grounding](../../CVPR2025/3d_vision/great_geometry-intention_collaborative_inference_for_open-vocabulary_3d_object_a.md)

<!-- RELATED:END -->
