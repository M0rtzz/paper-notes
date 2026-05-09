---
title: >-
  [论文解读] Bad Students Make Great Teachers: Active Learning Accelerates Large-Scale Visual Understanding
description: >-
  [ECCV 2024][多模态][主动学习] 本文提出 ClassAct / ActiveCLIP 方法，利用小型代理模型为训练数据计算"可学习性"分数，优先选择对大模型训练最有价值的数据，在 JFT 分类和 CLIP 多模态预训练中分别减少 46% 和 51% 的训练更新量，同时实现端到端计算正收益。
tags:
  - ECCV 2024
  - 多模态
  - 主动学习
  - 数据选择
  - 多模态VLM
  - CLIP
  - 计算效率
---

# Bad Students Make Great Teachers: Active Learning Accelerates Large-Scale Visual Understanding

**会议**: ECCV 2024  
**arXiv**: [2312.05328](https://arxiv.org/abs/2312.05328)  
**代码**: 无  
**领域**: 多模态VLM  
**关键词**: 主动学习, 数据选择, 大规模预训练, CLIP, 计算效率

## 一句话总结
本文提出 ClassAct / ActiveCLIP 方法，利用小型代理模型为训练数据计算"可学习性"分数，优先选择对大模型训练最有价值的数据，在 JFT 分类和 CLIP 多模态预训练中分别减少 46% 和 51% 的训练更新量，同时实现端到端计算正收益。

## 研究背景与动机

1. **领域现状**: 大规模视觉和语言模型的训练遵循 power-law scaling，即模型性能的增量改进需要数量级的计算量增加。当前训练普遍采用均匀采样策略。

2. **现有痛点**: 已有主动学习方法虽然能提升数据效率，但未能同时满足三个条件：(a) 跨模型和任务通用，(b) 可扩展到大规模数据集，(c) 在考虑数据选择开销后仍能节省总计算量（compute-positive）。

3. **核心矛盾**: 基于损失的优先采样（优先难样本或易样本）各有局限——优先难样本会纳入噪声数据，优先易样本则忽视了学习者当前状态。同时，精确的数据评分需要大模型推理，成本过高。

4. **本文目标**: 设计一种同时满足通用性、可扩展性和计算正收益的主动数据选择算法。

5. **切入角度**: 利用"可学习性"（learnability）概念——优先选择参考模型容易解决但当前学习者难以解决的样本，即 $s^{learn}(\mathbf{x}_i|\theta^t, \theta^*) = \ell(\mathbf{x}_i|\theta^t) - \ell(\mathbf{x}_i|\theta^*)$。

6. **核心 idea**: 用远小于学习者模型的代理模型（甚至小 1000 倍）来近似计算可学习性分数，仍能获得接近大模型评分的训练加速效果，从而实现计算正收益。

## 方法详解

### 整体框架
输入为大规模数据集（如 JFT-300M 或 ALIGN），通过在线批量选择（Online Batch Selection）框架运行。每步先均匀采样一个 super-batch，用小型 actor 模型计算可学习性分数，按分数优先采样出 sub-batch 用于更新大的 learner 模型。

### 关键设计

1. **可学习性评分（Learnability Scoring）**:
    - 功能: 为每个数据点计算优先级分数
    - 核心思路: 分数 $s^{learn} = \ell(\mathbf{x}_i|\theta^{online}) - \ell(\mathbf{x}_i|\theta^{ref})$，其中 online 模型和 learner 同步训练，ref 模型预训练后固定。高分表示数据"可学习但尚未学会"，通过 Softmax 转化为采样概率
    - 设计动机: 结合"难样本"和"干净样本"两个正交目标，自动过滤噪声数据和已学会的数据

2. **小模型代理评分（Proxy Model Scoring）**:
    - 功能: 将评分模型缩小到 learner 的 1/50 甚至 1/1000
    - 核心思路: 引入第三个 online 模型，与 reference 模型同架构同规模（如 ViT-Ti），替代 learner 进行评分。评分成本 $F_{act} = 2F_{ref}$，可随 ref 模型缩小
    - 设计动机: RHO loss 需要 learner 推理（成本与 learner 成正比），无法实现 compute-positive。实验发现可学习性评分对模型规模鲁棒，ViT-Ti 评分仍能为 ViT-L 提供 26% 加速

3. **ActiveCLIP / ActiveSigLIP 扩展**:
    - 功能: 将框架应用于多模态对比学习
    - 核心思路: actor 损失使用图文嵌入点积 $\ell_{act} = -\mathbf{z}_i^{im} \cdot \mathbf{z}_i^{txt}$，learner 使用标准对比损失。在干净小数据集（LTIP）上训练 reference 模型，用于指导大噪声数据集（ALIGN）的训练
    - 设计动机: 多模态数据集噪声更严重，用干净数据训练的 reference 能更有效地过滤噪声

### 损失函数 / 训练策略
- Learner: 分类任务用交叉熵 + label smoothing 0.1；多模态任务用对比损失或 sigmoid 损失
- 优化器: AdamW，cosine 学习率衰减，最大学习率 0.001
- 数据过滤: 保留 50%（ρ = B/b = 2），super-batch 中按可学习性分数 softmax 采样
- Online Reference 变体: reference 模型可在线训练（batch 10 倍，学习率 2 倍），无需预训练

## 实验关键数据

### 主实验

| 数据集 | 指标 | 本文 | 均匀采样 | 提升 |
|--------|------|------|----------|------|
| JFT-300M (ViT-L) | 学习者加速 | ClassAct (ViT-Ti) | Uniform | 26% fewer updates |
| JFT-300M (ViT-L) | 总 FLOP 节省 | ClassAct (ViT-Ti) | Uniform | ~25% total compute |
| ALIGN (ViT-B) | IN 0-shot | ActiveCLIP 71.3% | CLIP 68.3% | +3.0% |
| ALIGN+LTIP 3B | COCO im2txt | ActiveCLIP 57.7 | CLIP 52.4 | +5.3 |
| Webli 3B | COCO im2txt | ActiveSigLIP 63.5 | SigLIP 60.7 | +2.8 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| hard learner (高 loss 优先) | 微弱提升 | 噪声数据也有高 loss |
| easy reference (低 loss 优先) | 33% 加速但不可扩展 | 缩小 actor 后加速急剧下降 |
| learnability + ViT-B actor | 31% learner 加速 | compute-negative |
| learnability + ViT-Ti actor | 26% learner 加速 | **compute-positive** |
| learnability + ViT-Mu (1000x 小) | 16% learner 加速 | 仍有非平凡加速 |
| Online-ClassAct | 17% 加速 | 无需预训练 ref 模型 |

### 关键发现
- 可学习性评分对 actor 模型规模具有强鲁棒性，而 easy-reference 评分对此非常敏感
- 跨数据集迁移有效：LTIP 训练的 reference 模型用于 ALIGN 数据选择效果最佳
- 数据选择策略与 SigLIP 等新训练目标互补
- scaling law 在主动学习下仍然成立，但曲线整体左移

## 亮点与洞察
- 首次在大规模预训练中实现 compute-positive 的主动学习，解决了该领域长期难题
- 将 RL 中的 prioritized replay 概念引入数据选择，建立 actor-learner 异步框架
- 理论分析表明可学习性分数在 Taylor 展开下近似为梯度对齐度
- reference 模型可跨任务迁移，暗示数据选择策略可作为"基础课程"复用

## 局限与展望
- 仅过滤 50% 数据，更激进的过滤可能带来更大收益但也增加开销
- 目前仅验证图像分类和对比学习，未扩展到语言、视频和生成模型
- actor 模型需要与 learner 同架构族（都是 ViT），跨架构迁移未验证
- 异步框架的工程实现复杂，需要分布式基础设施支持

## 相关工作与启发
- **vs RHO Loss**: RHO 需要 learner 推理计算分数，ClassAct 用小 online 模型替代，实现 compute-positive
- **vs DataComp**: DataComp 做静态数据过滤，ClassAct 做动态在线选择，两者互补
- **vs DoReMi**: DoReMi 优化数据混合比例，ClassAct 优化样本级选择，更细粒度

## 评分
- 新颖性: ⭐⭐⭐⭐ 首次在大规模预训练中实现 compute-positive 主动学习
- 实验充分度: ⭐⭐⭐⭐⭐ 从 ImageNet 到 JFT 到 ALIGN/Webli，规模跨越大
- 写作质量: ⭐⭐⭐⭐ 逻辑清晰，Pareto 前沿分析直观
- 价值: ⭐⭐⭐⭐⭐ 对大规模训练实践有直接指导意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Omniview-Tuning: Boosting Viewpoint Invariance of Vision-Language Pre-training Models](omniview-tuning_boosting_viewpoint_invariance_of_vision-language_pre-training_mo.md)
- [\[ECCV 2024\] The Hard Positive Truth About Vision-Language Compositionality](the_hard_positive_truth_about_visionlanguage_compositionalit.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)
- [\[ECCV 2024\] AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_vision-language_models_for_city-wide_image_address_locali.md)
- [\[ECCV 2024\] Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_visionlangu.md)

</div>

<!-- RELATED:END -->
