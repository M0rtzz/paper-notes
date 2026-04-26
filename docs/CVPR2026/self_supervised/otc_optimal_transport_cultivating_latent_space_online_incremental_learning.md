---
title: >-
  [论文解读] An Optimal Transport-driven Approach for Cultivating Latent Space in Online Incremental Learning
description: >-
  [CVPR 2026][自监督学习][在线类增量学习] 提出基于最优传输理论的在线混合模型框架（MMOT），为每个类别维护多个自适应质心来表征流式数据的多模态分布，结合动态保持策略缓解灾难性遗忘，在 OCIL 场景显著超越现有方法。
tags:
  - CVPR 2026
  - 自监督学习
  - 在线类增量学习
  - 最优传输
  - 高斯混合模型
  - 灾难性遗忘
  - 潜空间建模
---

# An Optimal Transport-driven Approach for Cultivating Latent Space in Online Incremental Learning

**会议**: CVPR 2026  
**arXiv**: [2211.16780](https://arxiv.org/abs/2211.16780)  
**代码**: 无  
**领域**: 持续学习 / 在线增量学习  
**关键词**: 在线类增量学习, 最优传输, 高斯混合模型, 灾难性遗忘, 潜空间建模

## 一句话总结

提出基于最优传输理论的在线混合模型框架（MMOT），为每个类别维护多个自适应质心来表征流式数据的多模态分布，结合动态保持策略缓解灾难性遗忘，在 OCIL 场景显著超越现有方法。

## 研究背景与动机

1. **领域现状**：在线类增量学习（OCIL）是持续学习中最具挑战性的场景——数据分布动态变化，模型每批数据只能更新一次，推理时无任务 ID。现有方法通常使用单一分类头或单个质心表征每个类别。
2. **现有痛点**：单个自适应质心无法捕捉类别数据流的多模态特性（一个类可能包含多个聚类）；GMM 方法虽用多质心但训练后固定不更新。
3. **核心矛盾**：模型骨干网络不断适应新数据导致特征漂移，而固定质心无法跟随漂移——训练和测试的潜在表征之间存在明显偏移。
4. **本文目标**：在线学习过程中动态更新多质心，同时保持类间可分性和类内紧凑性。
5. **切入角度**：借助 OT 理论的连续性和几何敏感性替代传统 EM 算法。OT 可微分、数值稳定、尊重数据几何结构。
6. **核心 idea**：用 Wasserstein 距离熵正则化对偶形式最小化经验分布与 GMM 距离，质心通过梯度下降在线增量更新，Gumbel-Softmax 实现混合比例可微分采样。

## 方法详解

### 整体框架

输入新类数据批次 $X$ 和缓冲区旧类数据 $\bar{X}$，经特征提取器 $f_\theta$ 得到潜在表征。流程三步：(1) CE 损失初步分离类别；(2) MMOT 框架为每个类学习多个自适应质心；(3) 动态保持策略强化类别区分。推理时利用 Mahalanobis 距离分类。

### 关键设计

1. **MMOT（多模态最优传输框架）**:

    - 功能：为每个类别在线学习多个自适应质心和协方差矩阵
    - 核心思路：对每个类 $c$，用 GMM $\mathbb{Q}_c = \sum_{k=1}^K \pi_{k,c} \mathcal{N}(\mu_{k,c}, \text{diag}(\sigma_{k,c}^2))$ 近似其经验分布。通过最小化 Wasserstein 距离的熵正则化对偶形式学习 GMM 参数。重参数化技巧使采样可微分，Gumbel-Softmax 使混合比例采样也可微分。目标函数是期望形式，天然适合在线学习。
    - 设计动机：EM 算法需多次迭代且计算昂贵不适合在线场景；KL 散度在分布支撑不重叠时不稳定。OT 提供连续可微、数值稳定的替代方案。

2. **动态保持策略（Dynamic Preservation）**:

    - 功能：利用 MMOT 学到的多质心增强表征学习的类别区分能力
    - 核心思路：对比学习式目标函数，分子鼓励样本特征靠近自身类的所有 $K$ 个质心，分母推离其他类的质心和特征。使用温度参数 $\tau$ 缩放相似度值。
    - 设计动机：类边界上的质心特别有效地增强类间分离；多质心使信息表征更精确。

3. **记忆缓冲区选择与推理策略**:

    - 功能：利用质心选代表性样本存入缓冲区，推理时用 Mahalanobis 距离分类
    - 核心思路：对每个质心选最近样本加入缓冲区；推理时取测试样本到各类各高斯的 Mahalanobis 距离最小值。
    - 设计动机：基于质心选择确保缓冲区样本多样化覆盖类别分布。

### 损失函数 / 训练策略

每个批次：CE 损失初步训练 → MMOT 更新质心（交替更新 Kantorovich 网络和 GMM 参数） → 动态保持策略 → 更新缓冲区。

## 实验关键数据

### 主实验

| 数据集 | 指标 | OTC | BiC+AC (之前SOTA) | 提升 |
|--------|------|-----|-------------------|------|
| CIFAR-10 (M=0.2k) | Avg Acc | 64.8 | 63.5 | +1.3 |
| CIFAR-100 (M=2k) | Avg Acc | 48.5 | 47.3 | +1.2 |
| CIFAR-100 (M=5k) | Avg Acc | 56.5 | 54.2 | +2.3 |
| Tiny-ImageNet (M=5k) | Avg Acc | 31.6 | 22.6 | +9.0 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 基于质心选择缓冲区 (K=4) | 75.9% | MMOT 质心选样本 |
| 随机选择缓冲区 (K=4) | 73.4% | 质心选择一致优于随机 |
| 质心数=1 | 71.6% | 单质心性能最低 |
| 质心数=4 | 75.9% | 最优质心数 (M=1k) |

### 关键发现

- 缓冲区最小时 OTC 优势最显著，Tiny-ImageNet 领先高达 9 个百分点
- CoPE 遗忘指标低是因为初始准确率就很低，实际表征学习质量差
- 增加质心数在合理范围内持续提升，过多则缓冲区无法支撑

## 亮点与洞察

- **OT 替代 EM 的巧妙设计**：首次将 OT 用于 OCIL 中 GMM 学习，期望形式天然适合在线场景
- **统一框架**：质心同时用于训练（动态保持）、推理（Mahalanobis 距离）和缓冲区选择，三环节紧密耦合
- **可迁移性**：多质心+OT 的思路可迁移到其他需要在线表征学习的任务

## 局限与展望

- 仅在较小数据集验证，缺乏大规模（ImageNet-1k）实验
- 质心数 $K$ 是固定超参数，不同类别可能需要不同数量
- Kantorovich 网络增加额外计算开销，具体成本分析不够详细

## 相关工作与启发

- **vs OnPro**: OnPro 用单一自适应质心，OTC 扩展为多质心并用 OT 在线更新
- **vs MOSE**: MOSE 用固定 GMM 质心，OTC 质心通过梯度下降持续更新
- **vs BiC+AC**: BiC+AC 通过偏差校正缓解遗忘，不关注潜空间多模态结构

## 评分

- 新颖性: ⭐⭐⭐⭐ 首次将 OT 用于 OCIL 的 GMM 学习，理论推导扎实
- 实验充分度: ⭐⭐⭐ 数据集规模偏小，消融充分但缺少大规模验证
- 写作质量: ⭐⭐⭐⭐ 动机清晰，公式推导完整，图表直观
- 价值: ⭐⭐⭐⭐ 为在线增量学习提供了新的理论工具

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction](talo_pushing_3d_vision_foundation_models_towards_globally_consistent_online_reco.md)
- [\[CVPR 2026\] LaS-Comp: Zero-shot 3D Completion with Latent-Spatial Consistency](las-comp_zero-shot_3d_completion_with_latent-spatial_consistency.md)
- [\[CVPR 2026\] TrackMAE: Video Representation Learning via Track, Mask, and Predict](trackmae_video_representation_learning_via_track_mask_and_predict.md)
- [\[CVPR 2026\] A Stitch in Time: Learning Procedural Workflow via Self-Supervised Plackett-Luce Ranking](a_stitch_in_time_learning_procedural_workflow_via_self_supervised_plackett_luce_r.md)
- [\[CVPR 2026\] Group-DINOmics: Incorporating People Dynamics into DINO for Self-supervised Group Activity Feature Learning](group_dinomics_incorporating_people_dynamics_into_dino_for_self_supervised_group_activity_feature_learning.md)

<!-- RELATED:END -->
