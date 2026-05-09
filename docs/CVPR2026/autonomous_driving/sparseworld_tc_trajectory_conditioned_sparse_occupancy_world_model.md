---
title: >-
  [论文解读] SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model
description: >-
  [CVPR 2026][自动驾驶][4D占用预测] 提出一种基于纯注意力的稀疏占用世界模型SparseWorld-TC，绕过VAE离散化和BEV中间表示，直接从原始图像特征端到端预测轨迹条件的多帧未来占用，在nuScenes上大幅超越现有方法。
tags:
  - CVPR 2026
  - 自动驾驶
  - 4D占用预测
  - 世界模型
  - 稀疏表示
  - 轨迹条件
  - 纯注意力架构
---

# SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model

**会议**: CVPR 2026  
**arXiv**: [2511.22039](https://arxiv.org/abs/2511.22039)  
**代码**: [GitHub](https://github.com/MrPicklesGG/SparseWorld)  
**领域**: 自动驾驶 / 世界模型  
**关键词**: 4D占用预测, 世界模型, 稀疏表示, 轨迹条件, 纯注意力架构

## 一句话总结

提出一种基于纯注意力的稀疏占用世界模型SparseWorld-TC，绕过VAE离散化和BEV中间表示，直接从原始图像特征端到端预测轨迹条件的多帧未来占用，在nuScenes上大幅超越现有方法。

## 研究背景与动机

占用世界模型通过预测未来3D场景占用来理解环境动态，在自动驾驶中至关重要。现有方法主要存在两类局限：

1. **VAE离散化瓶颈**：OccWorld、OccLLaMA等方法使用VQ-VAE将连续3D场景数据编码为有限词表的离散token，这种离散化限制了表征能力并丢失了细粒度信息。
2. **BEV中间表示限制**：大多数方法依赖密集BEV特征图进行时空建模，引入了显式几何约束，限制了不同尺度特征的灵活交互。

受GPT和VGGT等纯注意力架构在语言和3D视觉领域的成功启发，作者提出：能否用完全基于注意力的前馈架构，通过稀疏占用表示直接从原始图像特征捕获时空依赖关系？

## 方法详解

### 整体框架

历史多帧图像 → 图像骨干网络提取特征 → 可变形注意力采样传感器嵌入 → 帧级注意力+时间注意力交替融合占用/传感器/轨迹嵌入 → MLP解码每个锚点的偏移和语义标签 → 输出多帧未来占用预测。

### 关键设计

1. **稀疏占用表示**:
    - 功能：用一组锚点（anchor）表示场景占用，每个锚点包含一组随机初始化的3D点和关联特征向量
    - 核心思路：每个锚点特征向量通过MLP解码每个点的3D偏移量和语义标签，将随机点"去噪"到一致的占用场
    - 设计动机：避免BEV的固定分辨率限制和VAE的离散化信息损失，保持完全稀疏和灵活

2. **轨迹时空嵌入**:
    - 功能：将轨迹航点编码为特征向量作为条件信号
    - 核心思路：结合位置嵌入（MLP投影16维齐次矩阵）和时间嵌入（正弦位置编码），通过仿射变换融合时空信息
    - 设计动机：受MLN启发，使模型能适应任意未来轨迹条件，支持不同时间间隔的航点

3. **纯注意力融合架构**:
    - 功能：统一融合占用、传感器和轨迹三种嵌入
    - 核心思路：堆叠帧级注意力（占用与传感器交叉注意力+轨迹自注意力）和时间注意力（跨帧自注意力）模块，多次迭代逐步精化
    - 设计动机：所有模态投射到统一嵌入空间后，标准注意力机制即可有效捕获长程时空依赖

### 损失函数 / 训练策略

- Chamfer Distance损失监督预测点与GT占用体素中心点的对齐
- Focal分类损失监督语义预测
- **随机集合策略**：训练时随机选择预测帧数L∈{2,...,T}，使模型适应不同预测长度需求，提升泛化能力

## 实验关键数据

### 主实验（Occ3D-nuScenes, Camera输入）

| 方法 | 1s mIoU | 2s mIoU | 3s mIoU | 平均mIoU | 平均IoU |
|------|---------|---------|---------|----------|---------|
| COME | 26.56 | 21.73 | 18.49 | 22.26 | 44.07 |
| Ours-Small | 27.95 | 25.51 | 23.35 | 25.60 | 49.02 |
| Ours-Large | 28.64 | 26.28 | 24.36 | 26.42 | 49.21 |
| Ours-Large* (DINOv3) | 32.76 | 29.62 | 27.28 | 29.89 | 53.52 |

### 长期预测（8秒）

| 方法 | 输入 | 平均mIoU | 平均IoU |
|------|------|----------|---------|
| COME | Occ GT | 19.07 | 29.96 |
| Ours-Large | Camera | 22.33 | 45.35 |

### 消融实验

| 配置 | 平均mIoU | 平均IoU | 说明 |
|------|----------|---------|------|
| 无轨迹 | 15.44 | 32.19 | 轨迹条件至关重要 |
| 预测轨迹 | 21.57 | 44.76 | 预测轨迹仍有效 |
| GT轨迹 | 25.60 | 49.02 | 更精确轨迹持续提升 |
| 固定帧训练 | 20.36 | 43.25 | 随机集合策略更优 |

### 关键发现

- 仅用Camera输入即超越使用GT占用输入的DOME方法（mIoU 29.89 vs 27.10）
- 长期预测性能衰减远小于现有方法，8秒预测IoU仍达39.97
- Small版本速度是Large版本的2.6倍，且性能差距不大，可实现效率-精度平衡

## 亮点与洞察

- 首个完全绕过VAE和BEV的纯注意力占用世界模型，设计理念简洁有力
- 稀疏表示的灵活性使模型可扩展至不同锚点数量和长期预测
- 长期预测优势显著：3秒后性能几乎不衰减，而现有方法急剧下降
- 可直接利用DINOv3等大规模基础模型提升性能

## 局限与展望

- 稀疏表示在极细粒度场景细节恢复方面可能不如密集方法
- 计算成本随锚点数量增加而增长，Large版本FPS仅3.58
- 长期预测的"多可能性"问题使单一GT评估存在局限
- 未探索与下游规划模块的联合训练

## 相关工作与启发

- **vs OccWorld/OccLLaMA**: 使用VAE离散化+自回归生成，受限于codebook容量；本方法端到端无需离散化
- **vs DOME/COME**: 使用扩散模型+BEV+连续VAE；本方法前馈单次推理，更高效
- **vs VGGT**: 借鉴其纯注意力架构理念，但专为4D占用预测设计

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首个纯注意力稀疏占用世界模型，设计范式全新
- 实验充分度: ⭐⭐⭐⭐ 短期/长期预测、消融、可视化均覆盖，对比方法充分
- 写作质量: ⭐⭐⭐⭐ 框架清晰，公式简洁，动机阐述充分
- 价值: ⭐⭐⭐⭐⭐ 为占用世界模型提供了全新的稀疏注意力范式，实际应用潜力大

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Generalizing Visual Geometry Priors to Sparse Gaussian Occupancy Prediction](generalizing_visual_geometry_priors_to_sparse_gaussian_occupancy_prediction.md)
- [\[ICCV 2025\] LangTraj: Diffusion Model and Dataset for Language-Conditioned Trajectory Simulation](../../ICCV2025/autonomous_driving/langtraj_diffusion_model_and_dataset_for_language-conditioned_trajectory_simulat.md)
- [\[CVPR 2026\] Learning Vision-Language-Action World Models for Autonomous Driving](vla_world_learning_vision_language_action_world_models_for_autonomous_driving.md)
- [\[ECCV 2024\] OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](../../ECCV2024/autonomous_driving/occworld_learning_a_3d_occupancy_world_model_for_autonomous_driving.md)
- [\[CVPR 2025\] GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction](../../CVPR2025/autonomous_driving/gaussianworld_gaussian_world_model_for_streaming_3d_occupancy_prediction.md)

</div>

<!-- RELATED:END -->
