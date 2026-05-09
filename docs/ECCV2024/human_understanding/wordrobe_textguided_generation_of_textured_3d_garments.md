---
title: >-
  [论文解读] WordRobe: Text-Guided Generation of Textured 3D Garments
description: >-
  [ECCV 2024][人体理解][text-to-3D] 提出 WordRobe 框架，通过学习 3D 服装潜在空间并与 CLIP 嵌入对齐，实现文本驱动的带纹理 3D 服装网格生成，并利用 ControlNet 的单步前向推理实现高效视角一致的纹理合成。
tags:
  - ECCV 2024
  - 人体理解
  - text-to-3D
  - 3D garment generation
  - texture synthesis
  - CLIP
  - ControlNet
---

# WordRobe: Text-Guided Generation of Textured 3D Garments

**会议**: ECCV 2024  
**arXiv**: [2403.17541](https://arxiv.org/abs/2403.17541)  
**代码**: 有（计划公开）  
**领域**: 人体理解  
**关键词**: text-to-3D, 3D garment generation, texture synthesis, CLIP, ControlNet

## 一句话总结

提出 WordRobe 框架，通过学习 3D 服装潜在空间并与 CLIP 嵌入对齐，实现文本驱动的带纹理 3D 服装网格生成，并利用 ControlNet 的单步前向推理实现高效视角一致的纹理合成。

## 研究背景与动机

- 3D 服装生成在虚拟试穿、游戏角色、AR/VR 等领域有广泛应用
- 现有方法的局限：
    - 参数化方法（基于 SMPL）仅限于紧身衣物
    - 非参数化方法生成的服装带姿态且纹理质量低
    - 通用 text-to-3D 方法的网格质量不够用于标准图形管线
    - DrapeNet 学习了形状潜在空间但不支持纹理和文本控制
- 核心挑战：如何在文本控制下生成高质量、无姿态（canonical pose）的 3D 服装网格和逼真纹理

## 方法详解

### 整体框架

WordRobe 包含三个核心组件：
1. **3D 服装潜在空间（Ω）**：将无姿态 3D 服装编码为潜在码
2. **映射网络（MLP_map）**：从 CLIP 嵌入预测服装潜在码
3. **纹理合成**：利用 ControlNet 生成视角一致的纹理

### 关键设计

**1. Coarse-to-Fine 服装潜在空间学习**

- 编码器：DGCNN 将 3D 服装表面点聚合为 32 维潜在码 ϕ
- 表示：使用无符号距离函数（UDF）表示开放服装表面
- 两阶段解码器：
    - 粗解码器 D_coarse：学习正则化的潜在空间和平滑 UDF
    - 细解码器 D_fine：预测粗解码器输出的残差变化，捕捉褶皱等细节
    - σ_fine = D_coarse(ϕ) + D_fine(ϕ)
- **解纠缠损失 L_latent**：约束潜在向量各维度的批次协方差矩阵趋近单位矩阵，使各维度独立编码不同形状特征

**2. CLIP 引导的 3D 服装生成**

- 弱监督训练方案：无需显式文本标注
    - 随机旋转服装网格，渲染深度图
    - 深度图输入 ControlNet 生成服装 RGB 图像
    - 用 CLIP 图像编码器提取嵌入 ψ_i
    - 同时用编码器 ξ 得到服装潜在码 ϕ_i
    - 训练 MLP_map 最小化 ψ → ϕ 的 L1 损失

**3. 单步纹理合成**

- 发现 ControlNet 的重要性质：多视角深度图合成在单张图像中时，生成的 RGB 图像保持视角间颜色和光照一致
- 方法：渲染服装正面和背面深度图并排合成 → 输入 ControlNet → 单步前向生成 1024×1024 视角合成 RGB 图像 → 投影到 UV 纹理贴图
- 使用正交投影减少切线区域信息损失

### 损失函数 / 训练策略

- 粗阶段：L_coarse = λ_dist · L_dist + λ_grad · L_grad + λ_latent · L_latent
    - L_dist: BCE 距离损失，L_grad: L2 梯度损失
- 细阶段：L_fine = λ_dist · L_dist + λ_grad · L_grad（冻结编码器）
- 映射网络：L1 损失对齐 CLIP 嵌入与服装潜在码

## 实验关键数据

### 主实验

| 方法 | CD ↓ | P2S ↓ |
|------|------|-------|
| DrapeNet | 1.796 | 0.573 |
| WordRobe（单阶段） | 1.631 | 0.494 |
| **WordRobe** | **1.078** | **0.329** |

CD 降低 40%，P2S 降低 42%，显著优于 DrapeNet。

### 消融实验

| 变体 | CD ↓ | P2S ↓ |
|------|------|-------|
| w/o L_grad | 1.886 | 0.612 |
| w/o L_latent | 1.094 | 0.331 |
| 完整模型 | **1.078** | **0.329** |

### 关键发现

- 纹理合成：WordRobe 仅需 ~22 秒 vs Text2Tex 的 ~5 分钟，快 13 倍
- CLIP Score 在三种 CLIP 编码器变体上均超越 Text2Tex
- 在 CLOTH3D 数据集上泛化性优异——仅在另一数据集训练，性能与在 CLOTH3D 上训练的 DrapeNet 相当
- 训练数据集比 DrapeNet 大 30 倍（~20K vs ~600 样本）

## 亮点与洞察

1. **ControlNet 新性质的发现**：多视角深度图合成输入 ControlNet 可保持视角一致性，这是首次在纹理合成中利用此性质
2. **弱监督训练方案**：巧妙避免了昂贵的手动文本标注
3. **解纠缠损失设计**：简洁的协方差正则化使潜在空间更有序
4. CLIP 引导支持文本/草图/图像多种输入模态的统一控制

## 局限性 / 可改进方向

- UDF 表示的分辨率限制了细节捕捉能力
- 32 维潜在码可能不足以表示更复杂的服装
- 纹理合成仅使用正面+背面两个视角，可能遗漏侧面细节
- 弱监督训练依赖 ControlNet 生成的图像质量

## 相关工作与启发

- **DrapeNet**: 潜在空间学习服装形状的基线
- **ControlNet**: 纹理合成和训练数据生成的关键工具
- **Mesh-UDF**: UDF 到网格的转换
- 启发：利用预训练生成模型的零样本能力替代昂贵的多视角优化是高效 3D 内容生成的可行方向

## 评分

| 维度 | 分数 (1-10) |
|------|-----------|
| 新颖性 | 8 |
| 技术深度 | 8 |
| 实验充分性 | 8 |
| 实用价值 | 8 |
| 写作质量 | 7 |
| 总体评分 | 7.8 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] TELA: Text to Layer-wise 3D Clothed Human Generation](tela_text_to_layer-wise_3d_clothed_human_generation.md)
- [\[ECCV 2024\] TF-FAS: Twofold-Element Fine-Grained Semantic Guidance for Generalizable Face Anti-Spoofing](tf-fas_twofold-element_fine-grained_semantic_guidance_for_generalizable_face_ant.md)
- [\[ECCV 2024\] Generalizable Facial Expression Recognition](generalizable_facial_expression_recognition.md)
- [\[ECCV 2024\] ReLoo: Reconstructing Humans Dressed in Loose Garments from Monocular Video in the Wild](reloo_reconstructing_humans_dressed_in_loose_garments_from_monocular_video_in_th.md)
- [\[ECCV 2024\] FreeMotion: A Unified Framework for Number-free Text-to-Motion Synthesis](freemotion_a_unified_framework_for_number-free_text-to-motion_synthesis.md)

</div>

<!-- RELATED:END -->
