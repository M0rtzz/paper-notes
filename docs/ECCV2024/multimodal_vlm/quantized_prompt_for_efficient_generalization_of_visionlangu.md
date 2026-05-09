---
title: >-
  [论文解读] Quantized Prompt for Efficient Generalization of Vision-Language Models
description: >-
  [ECCV 2024][多模态][量化] 发现适度噪声可以抑制VLM prompt tuning中的过拟合和灾难性遗忘，首次将量化误差视为正则化，设计了基于K-Means聚类的量化感知训练算法，在11个数据集上以极小存储开销（0.26KB）超越了众多SOTA方法。
tags:
  - ECCV 2024
  - 多模态
  - 多模态VLM
  - 提示学习
  - CLIP
  - 泛化
  - 参数高效
---

# Quantized Prompt for Efficient Generalization of Vision-Language Models

**会议**: ECCV 2024  
**arXiv**: [2407.10704](https://arxiv.org/abs/2407.10704)  
**代码**: [https://github.com/](https://github.com/)  
**领域**: 多模态VLM  
**关键词**: 量化, Prompt Tuning, CLIP, 泛化, 参数高效

## 一句话总结
发现适度噪声可以抑制VLM prompt tuning中的过拟合和灾难性遗忘，首次将量化误差视为正则化，设计了基于K-Means聚类的量化感知训练算法，在11个数据集上以极小存储开销（0.26KB）超越了众多SOTA方法。

## 研究背景与动机
1. **领域现状**：CLIP等大规模视觉语言预训练模型在下游任务迁移时，prompt tuning（如CoOp、MaPLe）是主流PEFT方法，通过添加少量可学习prompt参数来适配下游数据。
2. **现有痛点**：(1) 下游适配中最核心的问题是过拟合和灾难性遗忘——模型过度关注当前小规模数据而丢失领域通用知识；(2) 现有解决方案（如ProGrad等正则化方法）日趋复杂，带来不断增长的存储和推理成本；(3) 传统正则化方法在VLM场景下效果有限。
3. **核心观察**：适当的随机噪声可以有效抑制过拟合和灾难性遗忘。直接向prompt添加高斯噪声时，只有中等强度的噪声能改善泛化（太大破坏适配能力，太小无法正则化）。
4. **核心idea**：将量化误差视为一种可控噪声形式，利用量化来正则化VLM的prompt。量化不仅能提供适度"噪声"增强泛化，还天然带来模型压缩优势（16倍存储节省）。
5. **切入角度**：深入分析prompt权重分布特征（shape稳定、方差增长、无outlier），据此总结量化模块设计原则，构建高效的量化感知训练方法。

## 方法详解

### 整体框架
在CLIP prompt tuning基础上引入量化操作。训练时对prompt权重进行归一化→K-Means聚类量化→反归一化，通过STE传播梯度。存储时将fp16参数转为b-bit索引+码本，大幅压缩模型大小。该方法可集成到CoOp、MaPLe等已有方法中。

### 关键设计

1. **噪声-泛化关系的重新思考**：
    - 做什么：系统研究向prompt添加不同强度高斯噪声对模型特化能力（base类准确率）和泛化能力（new类准确率）的影响
    - 核心发现：噪声强度0（无噪声）导致泛化持续下降；噪声过大（0.1）严重损害特化能力；只有中等噪声（如0.01）在特化-泛化间取得最佳平衡
    - 设计动机：量化误差是比高斯噪声更可控的"噪声"形式，且自带压缩优势

2. **Prompt权重分布特征分析**：
    - 做什么：分析CoOp训练过程中prompt权重的分布变化
    - 核心发现：(1) 分布形状在整个训练中基本不变；(2) 分布方差在训练初期快速增长；(3) 几乎没有outlier；(4) 相邻阶段的权重变化温和
    - 设计原则：可以使用激进量化（如1-bit）；QAT优于PTQ；应先归一化消除平移和缩放变换；K-Means等聚类算法适合（因无outlier）

3. **归一化+K-Means量化**：
    - 做什么：对prompt权重先做z-score归一化，然后在归一化空间做K-Means聚类量化，最后反归一化
    - 核心思路：W_hat = (W - μ) / σ → Q(W_hat) → W_q = σ·Q(W_hat) + μ
    - 设计动机：训练过程中分布shape不变只有方差变化，归一化可以消除这种影响，提升量化精度

4. **约束自适应聚类（Constrained Adaptive Clustering）**：
    - 做什么：控制K-Means码本的更新频率和时机
    - 核心思路：设置最小更新间隔t；通过KL散度检测当前权重和缓存权重的分布差异，只有差异超过阈值T_KL时才重新聚类
    - 设计动机：(1) 频繁聚类降低效率；(2) 始终最小化量化误差可能有害（需要适度误差）；(3) 权重变化温和，频繁更新是无用功

### 损失函数 / 训练策略
- 使用标准的CLIP对比学习loss（交叉熵）
- 通过STE（Straight-Through Estimator）传播量化操作的梯度
- 量化位宽b通常取1、2或4-bit
- 存储：原始方法需要16N bits，量化后只需bN + 2^b × 16 bits

## 实验关键数据

### 主实验

| 方法 | 模型大小 | Base准确率 | New准确率 | 调和平均H |
|------|---------|-----------|-----------|----------|
| CLIP | 0KB | 69.34 | 74.22 | 71.70 |
| CoOp | 4.1KB | 82.69 | 63.22 | 71.66 |
| CoCoOp | 70.8KB | 80.47 | 71.69 | 75.83 |
| ProGrad | 16.4KB | 82.79 | 68.55 | 75.00 |
| **QCoOp** | **0.26KB** | **80.68** | **74.44** | **77.43** |
| MaPLe | 7096KB | 82.28 | 75.14 | 78.55 |
| **QMaPLe** | **1774KB** | **83.02** | **75.57** | **79.12** |

### 消融实验

| 设计选择 | 影响 |
|---------|------|
| 无量化（baseline） | H = 71.66 |
| 高斯噪声（0.01） | 中等噪声最优 |
| 有量化无归一化 | 性能下降 |
| 有量化有归一化 | H = 77.43 |
| 固定聚类 vs 自适应聚类 | 自适应显著更优 |

### 关键发现
1. QCoOp仅0.26KB体积就超越了63倍大的ProGrad（16.4KB），证明量化正则化的高效性
2. QMaPLe集成到MaPLe后在提升0.57%准确率的同时，模型仅为原来的1/4大小
3. 在域泛化、跨数据集迁移、少样本学习设置中均取得竞争性结果
4. 适度量化误差对泛化有利——既不是越小越好也不是越大越好

## 亮点与洞察
1. **量化即正则化**：首次将量化技术的"副作用"（量化误差）正面利用为对VLM的正则化手段，思路新颖
2. **设计原则驱动**：不是盲目套用量化方法，而是通过对prompt权重分布的深入分析，总结了4条设计原则，使方法选择有理有据
3. **双赢效果**：在提升模型泛化性能的同时自然获得模型压缩优势，QCoOp 0.26KB的存储需求使极端资源受限设备上的适配成为可能
4. **强通用性**：量化策略可无缝集成到CoOp、MaPLe等多种已有方法中，带来一致提升

## 局限性 / 可改进方向
1. 当前仅在prompt参数上进行量化，未探索对其他PEFT参数（如Adapter、LoRA权重）的量化正则化效果
2. 量化位宽和聚类更新阈值等超参数仍需手动设定，缺乏自适应选择机制
3. 主要在分类任务上验证，未在检测、分割等密集预测任务上测试
4. K-Means聚类的初始化和收敛性可能影响不同运行的一致性

## 相关工作与启发
- **CoOp/CoCoOp**：prompt tuning的基础方法，本文在其基础上引入量化
- **MaPLe**：多模态prompt方法，本文将量化成功集成
- **ProGrad**：基于梯度投影的正则化方法，本文以更小模型超越之
- **启发**：对其他PEFT方法是否也可以将"压缩技术的误差"作为正则化？如LoRA的低秩是否也是一种有益的"信息损失"？

## 评分
- 新颖性：⭐⭐⭐⭐ （量化误差→正则化的视角新颖）
- 技术深度：⭐⭐⭐⭐ （原理分析充分、设计原则完整）
- 实验充分性：⭐⭐⭐⭐⭐ （11个数据集、4种评估设置）
- 实用价值：⭐⭐⭐⭐⭐ （极低存储、即插即用）
- 写作质量：⭐⭐⭐⭐ （结构清晰，逻辑流畅）

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] A Parameter-Efficient and Fine-Grained Prompt Learning for Vision-Language Models](../../ACL2025/multimodal_vlm/a_parameter-efficient_and_fine-grained_prompt_learning_for_vision-language_model.md)
- [\[ECCV 2024\] SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)
- [\[ECCV 2024\] AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_visionlanguage_models_for_citywide_im.md)
- [\[ECCV 2024\] Omniview-Tuning: Boosting Viewpoint Invariance of Vision-Language Pre-training Models](omniviewtuning_boosting_viewpoint_invariance_of_visionlangua.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)

</div>

<!-- RELATED:END -->
