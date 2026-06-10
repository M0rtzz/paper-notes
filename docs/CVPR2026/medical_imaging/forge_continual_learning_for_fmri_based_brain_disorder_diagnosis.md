---
title: >-
  [论文解读] Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay
description: >-
  [CVPR 2026][医学图像][continual learning] 提出 FORGE，首个专为跨站点 fMRI 脑疾病诊断设计的持续学习框架，通过结构感知 VAE 生成逼真的功能连接矩阵进行隐私保护式生成回放，结合双层知识蒸馏和层次化上下文赌博机采样策略，有效缓解灾难性遗忘。
tags:
  - "CVPR 2026"
  - "医学图像"
  - "continual learning"
  - "fMRI"
  - "functional connectivity"
  - "generative replay"
  - "知识蒸馏"
---

# Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay

**会议**: CVPR 2026  
**arXiv**: [2604.14259](https://arxiv.org/abs/2604.14259)  
**代码**: [github.com/4me808/FORGE](https://github.com/4me808/FORGE)  
**领域**: 医学影像  
**关键词**: continual learning, fMRI, functional connectivity, generative replay, knowledge distillation

## 一句话总结

提出 FORGE，首个专为跨站点 fMRI 脑疾病诊断设计的持续学习框架，通过结构感知 VAE 生成逼真的功能连接矩阵进行隐私保护式生成回放，结合双层知识蒸馏和层次化上下文赌博机采样策略，有效缓解灾难性遗忘。

## 研究背景与动机

fMRI 功能连接 (FC) 矩阵是脑疾病诊断的强大表示，但临床数据通常从不同机构依次到达。现有诊断模型要么在单站点训练要么需要完整多站点数据访问，面临灾难性遗忘问题。传统持续学习方法主要针对图像数据设计，对图结构的医学数据（特别是 fMRI）研究不足。隐私法规进一步限制了跨机构的原始数据共享。

## 方法详解

### 整体框架

FORGE 要解决的是跨站点 fMRI 诊断的"边学边忘"：临床数据从不同机构依次到达，又因隐私法规不能把旧站点的原始数据留下来回放。它的思路是用生成回放替代真实数据回放，再套上双层知识蒸馏。每到一个新站点，学生分类器同时学两份数据——当前站点的真实 FC 矩阵，加上一个 VAE 现场生成的旧站点合成 FC 矩阵；同时通过 logit 级和图表示级蒸馏，让学生与上一站点的教师对齐。负责造样本的 FCM-VAE 也在每个站点更新，以生成符合该站点分布的合成样本。

### 关键设计

**1. FCM-VAE 结构感知编码器：让生成器真正"懂" FC 矩阵的拓扑**

传统持续学习的生成器多为自然图像设计，套到 FC 矩阵这种图结构数据上会丢掉脑网络的拓扑和谱属性，生成的样本不够真。FORGE 的编码器改用图 Transformer：每个 ROI 节点的特征由 FC 连接谱、谱嵌入和节点度拼接而成，注意力层同时融合局部邻接偏置（保住局部拓扑约束）和谱位置偏置（捕获全局几何信息）。这样编码器既看得到"谁和谁直接相连"，也看得到整张脑网络的全局形状，回放样本的保真度自然更高。

**2. 低秩解码器：用功能连接已知的低秩特性约束生成**

大规模功能连接本身有很强的低秩结构，解码器若无视这一点，生成的连接强度容易偏离真实分布。FORGE 的解码器直接利用这一先验，对 Fisher-z 变换并标准化后的连接强度建模为 Poisson 似然来重建。把低秩假设写进生成过程，既缩小了搜索空间，也让合成 FC 矩阵在生物学上更可信。

**3. 层次化上下文赌博机的自适应回放采样：把有限回放预算花在刀刃上**

回放缓冲区里的合成样本价值并不均等，均匀采样会把预算浪费在低信息量样本上。FORGE 用层次化上下文赌博机（hierarchical contextual bandit）策略，自适应地挑出最有信息量的合成样本去回放，从而在同样的回放次数下更高效地抵抗遗忘。配合它的是双层蒸馏——既对齐分类 logit，也对齐图读出（graph readout）表示，把教师的知识从两个粒度同时传给学生。

### 损失函数 / 训练策略

统一训练目标含四项：(1) 当前站点真实数据的分类损失；(2) 回放合成数据的分类损失；(3) logit 级蒸馏，用 L2 对齐学生与教师的 logits；(4) 图读出级蒸馏，用 L2 对齐图级表示。教师输出在样本加入缓冲区时计算一次后固定不变，避免反复前向。

## 实验关键数据

### 主实验

在 ABIDE（自闭症）、REST-meta-MDD（抑郁症）和 BSNIP（精神分裂症）大规模神经影像数据集上评估：

| 数据集 | 任务 | 方法 | 遗忘缓解 | 预测准确率 |
|--------|------|------|----------|-----------|
| ABIDE | ASD 诊断 | FORGE | **最优** | **最优** |
| REST-meta-MDD | MDD 诊断 | FORGE | **最优** | **最优** |
| BSNIP | SZ 诊断 | FORGE | **最优** | **最优** |

### 消融实验

- FCM-VAE 生成的 FC 矩阵质量显著优于现有图生成模型
- 图读出蒸馏相比仅 logit 蒸馏进一步提升性能
- 层次化采样策略优于均匀随机采样

### 关键发现

- 结构感知编码有效捕获了 FC 矩阵的拓扑特性
- 生成回放在隐私保护的前提下有效缓解灾难性遗忘
- 低秩解码器生成的 FC 矩阵具有更高的生物学保真度

## 亮点与洞察

- 首个将持续学习与 fMRI 功能连接分析结合的完整框架
- 隐私保护式生成回放解决了医疗数据共享的法规限制
- 结构感知设计充分利用了 FC 矩阵的领域特性

## 局限与展望

- 116 个 ROI 的固定脑图谱（AAL-116）限制了更精细的脑区分析
- 生成模型的保真度在极小样本站点上可能下降
- 未考虑站点间扫描仪差异的域适应

## 相关工作与启发

- 图级持续学习的设计可推广到其他图分类场景
- 谱位置编码在图 Transformer 中的应用值得关注
- 低秩解码器的思路适用于其他具有低秩结构的数据生成

## 评分

7/10 — 问题定义清晰、方法设计全面，是跨学科的有价值工作，但下游任务影响力受 fMRI 领域规模限制。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[NeurIPS 2025\] Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry](../../NeurIPS2025/medical_imaging/riemannian_flow_matching_for_brain_connectivity_matrices_via_pullback_geometry.md)
- [\[CVPR 2026\] Residual SODAP: Residual Self-Organizing Domain-Adaptive Prompting with Structural Knowledge Preservation for Continual Learning](residual_sodap_residual_self-organizing_domain-adaptive_prompting_with_structura.md)
- [\[CVPR 2026\] Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding](meta-learning_in-context_enables_training-free_cross_subject_brain_decoding.md)
- [\[ICML 2026\] Learning Multi-Scale Hypergraph for High-Order Brain Connectivity Analysis](../../ICML2026/medical_imaging/learning_multi-scale_hypergraph_for_high-order_brain_connectivity_analysis.md)
- [\[NeurIPS 2025\] EWC-Guided Diffusion Replay for Exemplar-Free Continual Learning in Medical Imaging](../../NeurIPS2025/medical_imaging/ewc-guided_diffusion_replay_for_exemplar-free_continual_learning_in_medical_imag.md)

</div>

<!-- RELATED:END -->
