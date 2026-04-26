---
title: >-
  [论文解读] OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving
description: >-
  [ECCV 2024][自动驾驶][3D占据预测] 提出OccGen，首次将扩散模型的"噪声到占据"生成范式引入3D语义占据预测任务，通过条件编码器+渐进式精炼解码器实现由粗到精的占据图生成，在nuScenes-Occupancy上多模态/纯LiDAR/纯相机设置下分别提升mIoU 9.5%/6.3%/13.3%。
tags:
  - ECCV 2024
  - 自动驾驶
  - 3D占据预测
  - 扩散模型
  - 多模态融合
  - 生成式感知
---

# OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving

**会议**: ECCV 2024  
**arXiv**: [2404.15014](https://arxiv.org/abs/2404.15014)  
**代码**: https://occgen-ad.github.io/ (有)  
**领域**: 多模态VLM  
**关键词**: 3D占据预测, 扩散模型, 自动驾驶, 多模态融合, 生成式感知

## 一句话总结
提出OccGen，首次将扩散模型的"噪声到占据"生成范式引入3D语义占据预测任务，通过条件编码器+渐进式精炼解码器实现由粗到精的占据图生成，在nuScenes-Occupancy上多模态/纯LiDAR/纯相机设置下分别提升mIoU 9.5%/6.3%/13.3%。

## 研究背景与动机
1. **领域现状**：3D语义占据预测为自动驾驶提供比BEV更精细的3D场景表示，为每个体素分配语义标签。现有方法分为LiDAR、视觉、多模态三类，均采用判别式单次前馈预测。
2. **现有痛点**：(1) 判别式方法仅学习输入到输出的单步映射，忽视了占据图底层分布的建模；(2) 单次推理不足以完成细粒度场景补全，就像人需要持续观察才能完全感知场景一样；(3) 判别式方法无法提供预测不确定性估计。
3. **核心观察**：扩散模型的去噪过程天然可以建模密集3D占据图的由粗到精精炼，从高斯噪声逐步生成详细预测。
4. **核心idea**：将3D占据预测reformulate为条件生成问题——"噪声→占据"，利用多次精炼步骤渐进生成占据图。

## 方法详解

### 整体框架
OccGen由两部分组成：(1) **条件编码器**（仅运行一次）：处理多模态输入（LiDAR点云+多视角图像），提取多尺度融合特征作为条件；(2) **渐进式精炼解码器**（运行多次）：接收3D噪声图，利用条件特征通过3D可变形注意力逐步去噪，生成最终占据预测。

### 关键设计

1. **条件编码器 - 多模态特征融合**：
    - LiDAR流：VoxelNet + 3D稀疏卷积提取LiDAR体素特征
    - 相机流：预训练2D backbone + FPN提取多视角图像特征→2D-to-3D视角转换
    - **Hard 2D-to-3D视角转换**：用Gumbel-Softmax生成one-hot深度编码（替代传统softmax深度概率），保证更精确的深度估计
    - **几何掩码（Geometry Mask）**：利用LiDAR体素特征生成空间掩码，施加到相机体素特征上，弥合相机特征与真实空间分布的差距
    - 自适应融合：σ(W)⊙F_p + (1-σ(W))⊙F_c

2. **渐进式精炼解码器**：
    - 输入：3D高斯噪声图（或上一步的预测噪声图）+ 采样步索引t + 多尺度融合特征
    - **3D可变形交叉注意力**：将噪声图下采样为多尺度query，在条件特征上采样关键点计算注意力
    - **3D可变形自注意力**：增强query间的自补全能力
    - **时间扩散模块**：对步索引t做embedding后进行scale-shift操作
    - 上采样+投影回原始3D分辨率→占据头输出最终语义标签

3. **训练过程 - Occupancy Corruption**：
    - 按DDPM方式向ground truth占据图添加高斯噪声，使用cosine noise schedule
    - 训练解码器学习从噪声中恢复干净占据图

### 损失函数 / 训练策略
- **总损失**：L_total = L_ce + L_ls + L_scal^geo + L_scal^sem + L_d
    - L_ce：交叉熵损失
    - L_ls：Lovász-Softmax损失
    - L_scal^geo/L_scal^sem：几何/语义亲和力损失
    - L_d：深度估计损失
- 推理时采用DDIM采样策略，使用非对称时间间隔(td=1)

## 实验关键数据

### 主实验（nuScenes-Occupancy验证集）

| 方法 | 输入 | IoU | mIoU |
|------|------|-----|------|
| MonoScene | Camera | 18.4 | 6.9 |
| TPVFormer | Camera | - | ~11 |
| VoxFormer | Camera | - | ~12 |
| OpenOccupancy-C | Camera | - | - |
| OccGen-C | Camera | - | +13.3% relative |
| OpenOccupancy-L | LiDAR | - | - |
| OccGen-L | LiDAR | - | +6.3% relative |
| OpenOccupancy-M | Multi-modal | - | - |
| **OccGen-M** | **Multi-modal** | **-** | **+9.5% relative** |

### 消融实验

| 组件 | 效果 |
|------|------|
| Hard vs Soft 2D-to-3D View Transform | Hard更精确 |
| 有/无几何掩码 | 几何掩码提升相机特征质量 |
| Cosine vs Linear noise schedule | Cosine更优 |
| 推理步数1→3→5 | 性能逐步提升（更多步=更精细） |
| 不确定性估计 | 多次独立推理可得到预测方差 |

### 关键发现
1. 生成式范式在三种输入设置下均大幅超越判别式方法，证明了渐进精炼的有效性
2. 编码器只运行一次、解码器多次运行的设计保证了推理效率——延迟与单次前馈方法相当
3. 生成模型天然支持不确定性估计——这是判别式方法无法做到的
4. 更多推理步数可以换取更高预测质量——"更多计算=更好结果"的可控trade-off
5. cosine noise schedule在3D占据预测中表现最好
6. Gumbel-Softmax的Hard视角转换比传统softmax深度更准确

## 亮点与洞察
1. **跨领域迁移创新**：将扩散模型从生成任务迁移到自动驾驶感知任务，"噪声到占据"新范式
2. **高效架构设计**：编码器一次+解码器多次的分离使得多步推理不会线性增加延迟
3. **生成式感知独有特性**：(1) 渐进推理支持计算-质量trade-off；(2) 天然支持不确定性估计——判别式方法不具备
4. **多模态完整方案**：从相机到LiDAR到多模态全面覆盖，融合策略设计完善

## 局限性 / 可改进方向
1. 多步推理虽然延迟可控，但仍比单步方法慢，在实时性要求极高的场景可能受限
2. 扩散模型的训练成本通常较高，收敛速度可能不如判别式方法
3. 仅在nuScenes上充分验证，其他数据集（如Waymo）的表现待确认
4. 生成模型可能引入"幻觉"——生成不存在于实际场景中的占据体素
5. 未探索时序信息融合（跨帧一致性）

## 相关工作与启发
- **DiffusionDet**：扩散模型用于目标检测的先驱，本文扩展到3D占据
- **DDP**：noise-to-map用于深度估计，本文扩展到3D语义占据
- **OpenOccupancy**：首个3D多模态占据基准，本文在其上大幅刷新性能
- **启发**：其他密集预测任务（BEV分割、点云语义分割）是否也能受益于生成式范式？

## 评分
- 新颖性：⭐⭐⭐⭐⭐ （生成式3D占据预测的首创工作）
- 技术深度：⭐⭐⭐⭐⭐ （多模态编码+扩散解码+3D注意力）
- 实验充分性：⭐⭐⭐⭐ （多设置验证，但仅一个数据集）
- 实用价值：⭐⭐⭐⭐ （自动驾驶核心模块）
- 写作质量：⭐⭐⭐⭐ （结构清晰，图示表达好）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] GraphBEV: Towards Robust BEV Feature Alignment for Multi-Modal 3D Object Detection](graphbev_towards_robust_bev_feature_alignment_for_multi-modal_3d_object_detectio.md)
- [\[ECCV 2024\] UniM2AE: Multi-modal Masked Autoencoders with Unified 3D Representation for 3D Perception in Autonomous Driving](unim2ae_multi-modal_masked_autoencoders_with_unified_3d_representation_for_3d_pe.md)
- [\[ECCV 2024\] OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](occworld_learning_a_3d_occupancy_world_model_for_autonomous_driving.md)
- [\[ECCV 2024\] Fully Sparse 3D Occupancy Prediction](fully_sparse_3d_occupancy_prediction.md)
- [\[ECCV 2024\] Optimizing Diffusion Models for Joint Trajectory Prediction and Controllable Generation](optimizing_diffusion_models_for_joint_trajectory_prediction_and_controllable_gen.md)

<!-- RELATED:END -->
