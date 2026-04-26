---
title: >-
  [论文解读] Group-DINOmics: Incorporating People Dynamics into DINO for Self-supervised Group Activity Feature Learning
description: >-
  [CVPR 2026][自监督学习][group activity] 提出利用 DINOv3 结合两个自监督预训练任务（人物光流估计和群体相关物体定位）来学习群体活动特征（GAF），在无群体活动标注的情况下大幅超越现有方法。
tags:
  - CVPR 2026
  - 自监督学习
  - group activity
  - DINO
  - 光流
  - activity retrieval
---

# Group-DINOmics: Incorporating People Dynamics into DINO for Self-supervised Group Activity Feature Learning

**会议**: CVPR 2026  
**arXiv**: [2604.04467](https://arxiv.org/abs/2604.04467)  
**代码**: [https://github.com/tezuka0001/Group-DINOmics](https://github.com/tezuka0001/Group-DINOmics)  
**领域**: 视频理解 / 群体活动分析  
**关键词**: group activity, self-supervised learning, DINO, optical flow, activity retrieval

## 一句话总结

提出利用 DINOv3 结合两个自监督预训练任务（人物光流估计和群体相关物体定位）来学习群体活动特征（GAF），在无群体活动标注的情况下大幅超越现有方法。

## 研究背景与动机

群体活动分析在体育分析、机器人和监控中有重要应用。自监督 GAF 学习避免了大量人工标注和预定义活动类别的需求。但现有方法（如 HRN、GAFL）仅通过局部图像重建作为预训练任务，只能嵌入局部外观线索（如服装纹理），缺乏两个关键能力：(1) 每个人的运动动态特征（局部动态）；(2) 人群空间配置等全局特征。

即使 DINOv3 能平衡局部和全局特征，直接应用仍不足，因为其在静态图像上训练的通用特征包含大量与群体活动无关的局部特征（如地板纹理），且缺乏时序运动特征。

## 方法详解

### 整体框架

DINOv3 提取图像特征 → Transformer 编码器 + MLP → 时序池化得到 GAF。训练时通过两个预训练任务从 GAF 估计人物光流和群体物体位置。

### 关键设计

1. **人物光流估计**：从 GAF 估计每个人的 xy 光流值，鼓励 GAF 包含局部动态特征。设计辅助分支直接从单帧特征估计光流，解决 DINOv3 只在静态图像上训练的局限，缩短反向传播路径，使 DINOv3 学习运动特征。

2. **群体相关物体定位与修复**：训练时对群体相关物体（如球）进行图像修复（inpainting），从 GAF 估计物体位置。修复迫使模型不依赖物体的局部外观线索，而是从全局上下文（人群空间配置）推断物体位置，嵌入全局特征。

3. **两阶段训练**：第一阶段用光流损失训练 50 epochs，第二阶段用物体定位损失训练 30 epochs，分阶段优化避免冲突。

### 损失函数 / 训练策略

光流损失 L_F = L_{F,G} + L_{F,I}（从 GAF 和单帧特征分别估计），物体定位损失 L_O = L_{O,G} + L_{O,I}。伪标签来自 RAFT（光流）和 YOLOX（检测），仅训练时使用。

## 实验关键数据

### 主实验

| 数据集 | 方法 | Hit@1 | Hit@3 |
|--------|------|-------|-------|
| VBD | GAFL (之前SOTA) | 61.1 | 82.4 |
| VBD | **Ours** | **82.7** | **93.0** |
| NBA | GAFL | 24.7 | 50.4 |
| NBA | **Ours** | **43.9** | **72.0** |

### 消融实验

| 配置 | VBD Hit@1 | NBA Hit@1 |
|------|----------|----------|
| 无任何预训练任务 | 43.0 | 22.6 |
| 仅光流损失 | 75.4 | 34.1 |
| 仅物体定位损失 | 74.0 | 40.3 |
| 两阶段训练（完整） | **82.7** | **43.9** |

### 关键发现

- Hit@1 相比 GAFL 提升 21.6 (VBD) 和 19.2 (NBA)，是巨大的性能跃升
- 光流估计和物体定位任务各自独立贡献，两阶段组合效果最优
- 辅助分支（从单帧估计）对 DINOv3 学习动态特征至关重要

## 亮点与洞察

- 两个预训练任务设计精巧且各有明确动机
- Inpainting 迫使全局推理的思路巧妙
- 性能提升幅度巨大，证明动态+全局特征对群体活动理解至关重要

## 局限与展望

- 目前仅在团队球类运动场景验证
- 群体相关物体需要预定义（如球），通用性受限

## 评分

- 新颖性：⭐⭐⭐⭐ — 预训练任务设计新颖
- 技术深度：⭐⭐⭐⭐ — 双分支+两阶段设计合理
- 实验充分度：⭐⭐⭐⭐ — 充分消融验证
- 实用价值：⭐⭐⭐ — 场景相对受限

<!-- RELATED:START -->

## 相关论文

- [\[AAAI 2026\] FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards from Domain Clients](../../AAAI2026/self_supervised/fedgrpo_privately_optimizing_foundation_models_with_group-relative_rewards_from_.md)
- [\[CVPR 2026\] A Stitch in Time: Learning Procedural Workflow via Self-Supervised Plackett-Luce Ranking](a_stitch_in_time_learning_procedural_workflow_via_self_supervised_plackett_luce_r.md)
- [\[CVPR 2026\] Zero-Ablation Overstates Register Content Dependence in DINO Vision Transformers](zero_ablation_overstates_register_content_dependence_in_dino_vision_transformers.md)
- [\[CVPR 2026\] Re-Depth Anything: Test-Time Depth Refinement via Self-Supervised Re-lighting](redepth_anything_test-time_depth_refinement_via_self-supervised_re-lighting.md)
- [\[ICLR 2026\] Why Prototypes Collapse: Diagnosing and Preventing Partial Collapse in Prototypical Self-Supervised Learning](../../ICLR2026/self_supervised/why_prototypes_collapse_diagnosing_and_preventing_partial_collapse_in_prototypic.md)

<!-- RELATED:END -->
