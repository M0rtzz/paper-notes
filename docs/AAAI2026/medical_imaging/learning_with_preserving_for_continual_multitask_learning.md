---
title: >-
  [论文解读] Learning with Preserving for Continual Multitask Learning
description: >-
  [AAAI2026][医学图像][continual learning] 提出 Learning with Preserving (LwP) 框架，通过 Dynamically Weighted Distance Preservation (DWDP) 损失保持 latent space 的几何结构，在无需 replay buffer 的条件下解决 Continual Multitask Learning (CMTL) 中的灾难性遗忘，是唯一超越 single-task baseline 的方法。
tags:
  - AAAI2026
  - 医学图像
  - continual learning
  - multitask learning
  - representation preservation
  - catastrophic forgetting
  - distance preservation
---

<!-- 由 src/gen_stubs.py 自动生成 -->
# Learning with Preserving for Continual Multitask Learning

**会议**: AAAI2026  
**arXiv**: [2511.11676](https://arxiv.org/abs/2511.11676)  
**代码**: [AICPS-Lab/lwp](https://github.com/AICPS-Lab/lwp)  
**领域**: medical_imaging  
**关键词**: continual learning, multitask learning, representation preservation, catastrophic forgetting, distance preservation  

## 一句话总结
提出 Learning with Preserving (LwP) 框架，通过 Dynamically Weighted Distance Preservation (DWDP) 损失保持 latent space 的几何结构，在无需 replay buffer 的条件下解决 Continual Multitask Learning (CMTL) 中的灾难性遗忘，是唯一超越 single-task baseline 的方法。

## 背景与动机
- 实际场景（自动驾驶、医学影像）中，模型需要在共享输入流上持续学习新任务
- 标准 MTL 要求所有任务标签同时可用，不适用于增量场景
- 传统 CL 方法专注于隔离 task-specific 知识（参数冻结、replay buffer），但这与 CMTL 需要构建统一共享表征的目标矛盾
- CMTL 独特之处：任务共享同一输入域、需要顺序学习、既防遗忘又要建共享表征

## 核心问题
在共享输入分布上顺序学习多个异构任务时，如何在防止灾难性遗忘的同时构建鲁棒的共享表征，且不依赖 replay buffer？

## 方法详解

### 整体框架
共享特征提取器 $f_{\theta_s}(\mathbf{x})$ 生成表征 $\mathbf{z}$，每个任务有独立 head $g_{\theta_t}(\mathbf{z})$。学习新任务时，冻结上一步模型作为 teacher，当前模型用三项损失联合训练：
$$\mathcal{L}_{lwp} = \lambda_c \mathcal{L}_{cur} + \lambda_o \mathcal{L}_{old} + \lambda_d \mathcal{L}_{DWDP}$$

### 关键设计
1. **距离保持损失** $\mathcal{L}_{pres}$：保持当前模型表征 $Z'$ 和冻结模型表征 $Z$ 之间的 pairwise distance 不变
$$\mathcal{L}_{pres}(Z,Z') = \frac{1}{N^2}\sum_{i,j}(d(\mathbf{z}_i,\mathbf{z}_j) - d(\mathbf{z}'_i,\mathbf{z}'_j))^2$$

2. **RKHS 理论保证**：保持 pairwise distance 等价于保持 Gaussian kernel Gram matrix，确保新旧表征在 RKHS 中功能等价（存在 isometry $T$ 使得 $\phi(\mathbf{z}'_i) = T(\phi(\mathbf{z}_i))$）

3. **Dynamic Weighting (DWDP)**：引入动态 mask $m_{ij}$，仅对同类样本对保持距离，避免与分类目标冲突
$$\mathcal{L}_{DWDP} = \frac{1}{N^2}\sum_{i,j} m_{ij}(\Delta d_{ij})^2, \quad m_{ij} = \mathbb{1}[y_i^{[t]} = y_j^{[t]}]$$

4. **Distillation loss** $\mathcal{L}_{old}$：冻结 teacher 生成旧任务伪标签，当前模型匹配

## 实验关键数据

| 方法 | BDD100k (3 tasks) | CelebA (10 tasks) | PhysiQ (3 tasks) | FairFace (3 tasks) |
|------|------------------|------------------|-----------------|-------------------|
| STL | 75.12 | 72.23 | 87.17 | 64.44 |
| LwF | 76.65 | 64.63 | 69.95 | 61.03 |
| DER | 77.18 | 70.70 | 84.80 | 64.11 |
| **LwP** | **78.30** | **73.48** | **88.24** | **66.48** |

- LwP 是**唯一**在所有数据集上超越 STL baseline 的方法
- 在 CelebA (224×224 + ResNet50) 上，LwP 达到 85.06%，比第二名高 ~15 个百分点
- 在 distribution shift 场景下（weather/scene/time-of-day shift），LwP 保持最佳鲁棒性
- Backward Transfer 指标在所有 benchmark 上均优于 baseline

## 亮点
1. **无需 replay buffer**：适用于隐私敏感场景（医疗、自动驾驶），不存储历史数据
2. **理论支撑完整**：通过 RKHS isometry 证明保持 pairwise distance 即可保证表征功能等价
3. **唯一超 STL**：说明 LwP 不仅防遗忘，还实现了跨任务正迁移
4. **模态无关**：在图像（BDD100k/CelebA/FairFace）和时序（PhysiQ）上均有效

## 局限性 / 可改进方向
- DWDP 的 $O(N^2)$ pairwise 计算在大 batch size 下开销大
- 实验的 backbone 限于 ResNet，未验证在 ViT 等现代架构上的效果
- 任务数量较少（最多 10 tasks），超长任务序列（50+ tasks）的可扩展性未知
- Dynamic weighting 仅使用当前任务标签，无法利用旧任务的类别信息
- Combined shift 场景下 LwP 的优势减弱（74.00 vs DER 75.94）

## 与相关工作的对比
- vs **LwF** (知识蒸馏)：LwF 仅保持输出一致，LwP 保持表征空间结构，CMTL 下 LwP 在 CelebA 上高 ~9%
- vs **EWC/SI** (参数正则化)：参数空间正则化倾向于冻结参数，不适合需要共享表征的 CMTL
- vs **DER/DERPP** (经验回放)：需要 buffer 且在 CMTL 下不稳定，LwP 无 buffer 仍更优
- vs **RKD/Co2L** (关系蒸馏)：RKD 保持所有 pair 距离导致与分类目标冲突，LwP 通过 dynamic masking 解决
- vs **PODNet** (空间特征保持)：PODNet 不区分类别统一保持，LwP 按类别选择性保持更优

## 启发与关联
- 保持表征空间几何结构比保持输出/参数更本质，这一 insight 可迁移到其他 incremental learning 场景
- Dynamic masking（只保持同类 pair 距离）的策略在 contrastive learning 中也可能有用
- 无 replay buffer 的设计对数据隐私要求高的医疗/金融领域有实际意义
- CMTL 作为新 setting 的定义值得关注，介于 MTL 和 Task-IL 之间

## 评分
- 新颖性: ⭐⭐⭐⭐ — CMTL setting 的正式定义 + DWDP loss 设计新颖
- 实验充分度: ⭐⭐⭐⭐ — 4 数据集 + 11 baseline + distribution shift + 消融
- 写作质量: ⭐⭐⭐⭐ — 理论推导清晰，实验组织有条理
- 价值: ⭐⭐⭐⭐ — CMTL 框架和 DWDP 均有实际应用价值
