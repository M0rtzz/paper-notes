---
title: >-
  [论文解读] Memory-Efficient Transfer Learning with Fading Side Networks via Masked Dual Path Distillation
description: >-
  [CVPR 2026][模型压缩][记忆高效迁移学习] MDPD提出通过冻结骨干网络与轻量侧网络之间的双向知识蒸馏实现高效微调，训练完成后丢弃侧网络，从而同时实现训练时的参数/内存高效和推理时的速度高效。
tags:
  - CVPR 2026
  - 模型压缩
  - 记忆高效迁移学习
  - 知识蒸馏
  - 侧网络
  - 推理加速
  - 双路径蒸馏
---

# Memory-Efficient Transfer Learning with Fading Side Networks via Masked Dual Path Distillation

**会议**: CVPR 2026  
**arXiv**: [2604.09088](https://arxiv.org/abs/2604.09088)  
**代码**: https://github.com/Zhang-VKk/MDPD  
**领域**: 模型压缩/高效迁移学习  
**关键词**: 记忆高效迁移学习, 知识蒸馏, 侧网络, 推理加速, 双路径蒸馏

## 一句话总结

MDPD提出通过冻结骨干网络与轻量侧网络之间的双向知识蒸馏实现高效微调，训练完成后丢弃侧网络，从而同时实现训练时的参数/内存高效和推理时的速度高效。

## 研究背景与动机

**领域现状**：记忆高效迁移学习（METL）通过构建轻量平行侧网络来避免大骨干的梯度反传，显著降低训练内存。但侧网络在推理时引入额外的内存和时间开销。

**现有痛点**：现有METL方法在训练阶段实现了参数和内存高效，但推理阶段的额外开销与高效迁移学习的终极目标相矛盾。

**核心矛盾**：侧网络在训练中不可或缺（避免大骨干的梯度存储），但在推理中是累赘（增加前向传播开销）。

**本文目标**：设计一种方法，在训练时利用侧网络实现内存高效，在推理时丢弃侧网络而不损失精度。

**切入角度**：通过双向知识蒸馏将侧网络学到的下游任务知识迁移回骨干网络。

**核心idea**：训练时骨干和侧网络互为师生进行蒸馏，推理时只用优化后的骨干，侧网络被"消融"。

## 方法详解

### 整体框架

MDPD包含两个并行路径：冻结的骨干网络和可学习的侧网络。训练时通过特征级蒸馏（骨干→侧网络）和logits级蒸馏（侧网络→骨干）实现双向知识迁移。推理时仅使用骨干网络加任务头。

### 关键设计

1. **双路径知识蒸馏（DPKD）**:

    - 功能：在骨干和侧网络之间建立双向知识流
    - 核心思路：特征蒸馏中骨干为教师、侧网络为学生（利用预训练知识增强侧网络）；logits蒸馏中侧网络为教师、骨干为学生（将下游任务知识迁移回骨干）。使用低秩矩阵 $M_{down} \in \mathbb{R}^{D_S \times d}$ 和 $M_{up} \in \mathbb{R}^{d \times D_B}$ 进行维度对齐
    - 设计动机：双向蒸馏使两个网络互相提升——骨干的预训练知识帮助侧网络更好学习，侧网络的任务知识帮助骨干适应下游

2. **分层特征蒸馏（HFD）**:

    - 功能：针对编码器不同层设计差异化蒸馏策略
    - 核心思路：浅层师生注意力模式相似（都是对角自注意力），采用直接模仿；深层注意力模式分歧大（关注不同稀疏关键token），采用掩码生成策略——学生不直接模仿教师特征，而是生成教师的特征
    - 设计动机：深浅层的注意力差异使得"一刀切"的蒸馏策略效果不佳，分层策略更有效地传递知识

3. **消融侧网络的推理策略**:

    - 功能：推理时完全去除侧网络
    - 核心思路：训练时骨干仅更新LayerNorm的缩放/偏移系数和最终输出层参数（大部分参数冻结），但通过蒸馏获得了任务适应能力。推理时直接使用骨干+任务头
    - 设计动机：避免侧网络的推理开销，实现训练和推理的双重高效

### 损失函数 / 训练策略

交替优化骨干和侧网络，使其特征分布差异最小化。总损失包含特征蒸馏损失和logits蒸馏损失两部分。

## 实验关键数据

### 主实验

| 任务 | 指标 | MDPD | SOTA METL | 提升 |
|------|------|------|-----------|------|
| 视觉任务 | 推理加速 | ≥25.2% | 0% | +25.2% |
| 语言任务 | 推理加速 | ≥22.5% | 0% | +22.5% |
| 多模态任务 | 精度 | 超越SOTA | - | 提升 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 无特征蒸馏 | 精度下降 | 缺少预训练知识传递 |
| 无logits蒸馏 | 精度下降 | 缺少任务知识迁移 |
| 不分层蒸馏 | 精度下降 | 深浅层策略不当 |
| 完整MDPD | 最优 | 双向蒸馏+分层策略 |

### 关键发现

- 推理加速至少25.2%同时保持甚至提升精度——这说明侧网络的角色可以完全通过蒸馏迁移
- 分层蒸馏策略对多层编码器至关重要，浅层直接模仿、深层掩码生成的组合最优
- 方法在视觉、语言和视觉-语言三种模态下均有效，验证了通用性

## 亮点与洞察

- **训练时用、推理时丢**：侧网络作为"一次性教练"的设计理念巧妙解决了METL的推理开销问题
- **分层蒸馏的发现**：深浅层注意力模式差异的观察及其对应的蒸馏策略设计值得借鉴
- **低秩维度对齐**：用瓶颈结构避免维度对齐引入大量参数，保持参数效率

## 局限与展望

- 训练时间可能增加（需要双路径前向和蒸馏损失计算）
- 仅更新骨干的LayerNorm参数可能限制了更极端域偏移下的适应能力
- 未讨论侧网络规模与蒸馏效果的关系

## 相关工作与启发

- **vs LoRA**: LoRA直接修改骨干权重但仍需要反传，MDPD通过侧网络间接更新骨干，内存更省
- **vs Side-Tuning**: 传统侧网络方法推理时保留侧网络，MDPD通过蒸馏实现了推理时的完全去除

## 评分

- 新颖性: ⭐⭐⭐⭐ 双向蒸馏+消融侧网络的组合设计新颖
- 实验充分度: ⭐⭐⭐⭐ 跨视觉/语言/多模态三种任务验证
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰
- 价值: ⭐⭐⭐⭐ 解决了METL领域的核心矛盾

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] DAGE: Dual-Stream Architecture for Efficient and Fine-Grained Geometry Estimation](dage_dual-stream_architecture_for_efficient_and_fine-grained_geometry_estimation.md)
- [\[CVPR 2026\] WPT: World-to-Policy Transfer via Online World Model Distillation](wpt_world-to-policy_transfer_via_online_world_model_distillation.md)
- [\[CVPR 2026\] MEMO: Human-like Crisp Edge Detection Using Masked Edge Prediction](memo_human-like_crisp_edge_detection_using_masked_edge_prediction.md)
- [\[ICLR 2026\] LightMem: Lightweight and Efficient Memory-Augmented Generation](../../ICLR2026/model_compression/lightmem_lightweight_and_efficient_memory-augmented_generation.md)
- [\[ACL 2026\] Efficient Learned Data Compression via Dual-Stream Feature Decoupling](../../ACL2026/model_compression/efficient_learned_data_compression_via_dual-stream_feature_decoupling.md)

<!-- RELATED:END -->
