---
title: >-
  [论文解读] SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs
description: >-
  [ECCV 2024][3D视觉][视觉定位] 提出SceneGraphLoc，首次将queryimage在多模态3D场景图数据库中进行粗定位，通过学习场景图节点和图像patch的统一嵌入空间，在存储效率提升1000倍的同时接近图像检索方法的定位精度。
tags:
  - ECCV 2024
  - 3D视觉
  - 视觉定位
  - 3D场景图
  - 跨模态匹配
  - 多模态嵌入
  - 对比学习
---

# SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

**会议**: ECCV 2024  
**arXiv**: [2404.00469](https://arxiv.org/abs/2404.00469)  
**代码**: https://scenegraphloc.github.io (有)  
**领域**: 多模态VLM  
**关键词**: 视觉定位, 3D场景图, 跨模态匹配, 多模态嵌入, 对比学习

## 一句话总结

提出SceneGraphLoc，首次将queryimage在多模态3D场景图数据库中进行粗定位，通过学习场景图节点和图像patch的统一嵌入空间，在存储效率提升1000倍的同时接近图像检索方法的定位精度。

## 研究背景与动机

1. **领域现状**：粗定位（place recognition）通常作为图像检索问题，将query图像与大规模图像数据库比对。SOTA方法如NetVLAD等通过学习嵌入实现高效检索，但依赖庞大的图像数据库。
2. **现有痛点**：(a) 图像数据库存储量大、查询慢；(b) 跨模态方法通常限于两种模态之间（如图像-点云或图像-鸟瞰图），应用范围受限。
3. **核心矛盾**：高精度定位需要丰富的视觉信息，但存储和计算成本与信息量正相关。3D场景图提供了结构化、多模态、紧凑的场景表示，但尚未被用于定位。
4. **本文要解决什么**：将query图像定位到3D场景图组成的数据库中，利用场景图的紧凑性实现高效且相对准确的粗定位。
5. **切入角度**：将定位问题转化为图像patch与场景图节点的跨模态匹配问题，学习统一嵌入空间。
6. **核心idea一句话**：将3D场景图中的多模态节点信息（点云、图像、属性、关系）和query图像的patch蒸馏到统一嵌入空间，通过匹配实现定位。

## 方法详解

### 整体框架

系统包含两条并行流水线：(1) 场景图编码：为每个节点融合点云、图像、结构、属性和关系五种模态的嵌入；(2) 查询图像编码：将图像分为patch，为每个patch生成嵌入。训练目标是使可见物体对应的patch-node对嵌入接近。推理时，通过最近邻匹配和相似度打分找到最匹配的场景图。

### 关键设计

**1. 场景图节点多模态嵌入**
- 做什么：为每个场景图节点v生成融合五种模态的统一嵌入e_v
- 核心思路：
    - 点云模态：PointNet提取几何特征
    - 图像模态：为每个3D物体选择可见性最高的K_view=10张图像，多层级裁剪(multi-level bounding box)后由DINOv2提取特征，再通过Transformer编码器（含位姿位置编码）融合多视角信息
    - 结构模态：GAT编码物体间的相对位置关系
    - 属性/关系模态：bag-of-words + FFN
- 设计动机：加权拼接后通过MLP得到固定维度嵌入，权重可学习，使维度与模态数量无关

**2. 查询图像patch嵌入**
- 做什么：将query图像分割为规则patch，为每个patch生成嵌入
- 核心思路：DINOv2提取patch级特征，经4层ResNet CNN + 3层MLP映射到与节点嵌入相同的D维空间
- 设计动机：避免使用2D全景分割（易出现过/欠分割），patch化更鲁棒

**3. 对比学习训练**
- 做什么：用静态损失（同时刻场景图）和时序损失（不同时刻场景图）联合优化
- 核心思路：双向N-pair损失，正样本为可见物体对应的patch-node对，负样本来自其他场景图的节点和同场景的非对应patch
- 设计动机：时序损失使用3RScan数据集中同一场景不同时间点的扫描，增强对动态变化（物体移动、光照变化）的鲁棒性

**4. 图像到场景图的相似度打分**
- 做什么：对每个候选场景图，通过patch-node最近邻匹配计算相似度分数
- 核心思路：找到每个patch在场景图中的最匹配节点，聚合匹配距离得到整体打分
- 设计动机：选择打分最高的场景图作为定位结果

### 损失函数 / 训练策略

- 损失函数：ℒ = α×ℒ_static + (1-α)×ℒ_temp，均为双向N-pair对比损失
- 训练数据：3RScan数据集，包含多时间点扫描
- 映射阶段需要所有模态；定位阶段仅需预计算的固定嵌入e_v

## 实验关键数据

### 主实验

| 方法 | 模态 | Recall@1 (ScanNet) | 存储占用 |
|------|------|-------------------|---------|
| 纯图像检索SOTA | 图像 | ~最高 | 极大 |
| 跨模态方法 | 点云 | 大幅落后 | 中等 |
| SceneGraphLoc(无图像) | 点云+属性+关系 | 大幅超越其他跨模态 | 极小 |
| SceneGraphLoc(含图像) | 全模态 | 接近图像检索SOTA | 小1000倍 |

### 消融实验

| 模态组合 | 效果 |
|---------|------|
| 仅点云 | 基线 |
| +结构关系 | 提升显著 |
| +图像 | 再提升一大截 |
| +属性 | 小幅提升 |
| 全模态 | 最优 |

### 关键发现

1. **即使不用图像**，仅靠几何+属性+关系，SceneGraphLoc就大幅超越其他跨模态方法
2. 加入图像后定位精度接近SOTA图像检索方法，但**存储减少三个数量级，速度快数个数量级**
3. 多层级图像裁剪(multi-level bounding box)对图像模态嵌入质量至关重要
4. 时序对比损失有效提升了对场景动态变化的鲁棒性

## 亮点与洞察

- **问题定义创新**：首次提出在3D场景图中进行图像定位，开辟了新的研究方向
- **极致的存储效率**：场景图蒸馏为固定嵌入后，数据库从GB级图像压缩到KB级嵌入
- **多模态融合的灵活性**：模块化设计使得可以根据场景条件（如夜间无图像）灵活选择模态
- **时序鲁棒性**：利用3RScan多次扫描数据训练，使定位对场景变化具有鲁棒性

## 局限性 / 可改进方向

1. 当前仅实现粗定位（场景/房间级），精确6DoF位姿估计需要后续的fine localization pipline
2. 场景图构建本身需要3D扫描数据，构建成本不低
3. 实验限于室内场景，室外大规模场景的扩展性待验证
4. DINOv2特征的提取仍有一定计算开销
5. 对于外观高度相似的房间（如酒店标准间），仅靠物体级特征可能难以区分

## 相关工作与启发

- **NetVLAD**：SOTA图像检索方法，SceneGraphLoc在存储效率上有巨大优势
- **3D Scene Graphs (Armeni等)**：场景图概念的先驱，本文将其应用于定位
- **SGAligner**：场景图对齐工作，专注于地图对齐而非图像定位
- **启发**：结构化场景表示（场景图）比非结构化表示（图像/点云）在效率和可解释性上有显著优势

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ (全新问题定义)
- **技术深度**: ⭐⭐⭐⭐ (多模态融合设计完整)
- **实验充分性**: ⭐⭐⭐⭐ (消融充分，但数据集有限)
- **写作质量**: ⭐⭐⭐⭐ (问题定义和方法描述清晰)
- **影响力**: ⭐⭐⭐⭐ (连接了场景图和定位两个领域)

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] The NeRFect Match: Exploring NeRF Features for Visual Localization](the_nerfect_match_exploring_nerf_features_for_visual_localization.md)
- [\[ECCV 2024\] WaSt-3D: Wasserstein-2 Distance for Scene-to-Scene Stylization on 3D Gaussians](wast-3d_wasserstein-2_distance_for_scene-to-scene_stylization_on_3d_gaussians.md)
- [\[ECCV 2024\] Zero-Shot Multi-Object Scene Completion](zero-shot_multi-object_scene_completion.md)
- [\[ECCV 2024\] SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](sceneverse_scaling_3d_vision-language_learning_for_grounded_scene_understanding.md)
- [\[ECCV 2024\] Vista3D: Unravel the 3D Darkside of a Single Image](vista3d_unravel_the_3d_darkside_of_a_single_image.md)

<!-- RELATED:END -->
