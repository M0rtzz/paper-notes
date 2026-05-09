---
title: >-
  [论文解读] Robust Calibration of Large Vision-Language Adapters
description: >-
  [ECCV 2024][多模态][CLIP calibration] 发现CLIP适配方法（Prompt Learning、Adapters、Test-Time Adaptation）在OOD上的校准退化根因是logit范围（range）增大而非logit范数（norm），提出三种方案——ZS-Norm、Penalty和SaLS（Sample-adaptive Logit Scaling），其中SaLS无需训练即可在推理时将ECE降低50%以上。
tags:
  - ECCV 2024
  - 多模态
  - CLIP calibration
  - logit range
  - OOD
  - 提示学习
  - 多模态VLM
---

# Robust Calibration of Large Vision-Language Adapters

**会议**: ECCV 2024  
**arXiv**: [2407.13588](https://arxiv.org/abs/2407.13588)  
**代码**: [GitHub](https://github.com/Bala93/CLIPCalib)  
**领域**: 多模态VLM  
**关键词**: CLIP calibration, logit range, OOD, prompt learning, adapter

## 一句话总结

发现CLIP适配方法（Prompt Learning、Adapters、Test-Time Adaptation）在OOD上的校准退化根因是logit范围（range）增大而非logit范数（norm），提出三种方案——ZS-Norm、Penalty和SaLS（Sample-adaptive Logit Scaling），其中SaLS无需训练即可在推理时将ECE降低50%以上。

## 研究背景与动机

**领域现状**：CLIP的零样本分类性能已很强，社区通过Prompt Learning（CoOp/CoCoOp）、Adapters（CLIP-Adapter/TIP-Adapter）和Test-Time Adaptation（TPT）三类方法进一步提升分类准确率。但这些方法在提升ACC的同时严重恶化了模型的校准性能。

**现有痛点**：(1) 适配后的模型过于自信——即使预测错误也给出高置信度，这在医疗等安全关键场景是致命的；(2) 已有校准方法（如Temperature Scaling）需要验证集且假设同分布，在OOD下失效；(3) 社区普遍认为logit范数增大是miscalibration的根因，但本文发现这一认知对CLIP适配场景不成立。

**核心矛盾**：如何在保持CLIP适配带来的ACC提升的同时，修复OOD场景下严重退化的校准性能？

**切入角度**：重新分析miscalibration的根因——从logit向量的范数和范围两个维度入手，发现范围（max - min）才是真正的驱动因素。

## 方法详解

### 整体框架

作者首先通过两个命题（Proposition 1 & 2）从理论上证明：(1) logit向量整体加常数会增加范数但不改变softmax概率（即范数增大不一定导致过自信）；(2) logit向量乘以标量$a>1$会同时增大范围和softmax置信度。由此推出：**logit范围增大**而非范数增大才是miscalibration的根因。基于此提出约束优化问题：限制适配后logit的范围不超过零样本预测的logit范围。

### 关键设计

1. **ZS-Norm（训练时集成）**

    - 在CEW损失计算前，将适配后的logit线性归一化到零样本logit的[min, max]范围：$\mathbf{l}'_i = \frac{l^{ZS\text{-}max}_i - l^{ZS\text{-}min}_i}{l^{max}_i - l^{min}_i}(\mathbf{l}_i - l^{min}_i) + l^{ZS\text{-}min}_i$
    - 保留logit方向（决定预测类别）但将幅度缩放回零样本范围
    - 集成到训练过程中，对所有PL/Adapter方法通用

2. **SaLS（推理时应用）**

    - 对每个测试样本$i$，先计算其零样本logit的min/max，再用相同的归一化公式缩放适配后的logit
    - **无需训练、无需验证集**——直接在推理时应用
    - 本质上是sample-adaptive的温度缩放：每个样本有自己的"温度"，由其零样本logit范围决定
    - 设计动机：与全局Temperature Scaling不同，SaLS适应每个样本的特性，不受分布偏移影响

3. **Penalty（训练时正则化）**

    - 将约束转化为ReLU惩罚项加入训练损失：$\lambda \sum_k [\text{ReLU}(l_{ik}-l^{ZS\text{-}max}_i) + \text{ReLU}(l^{ZS\text{-}min}_i-l_{ik})]$
    - 只有当logit超出零样本范围时才产生梯度，不影响范围内的正常训练
    - $\lambda=10$固定不调

### 损失函数 / 训练策略

ZS-Norm和Penalty在各适配方法的原始训练流程中集成（CoOp 50 epochs, CoCoOp 10 epochs, Adapters 300 epochs，SGD lr=0.1）。SaLS无需训练。所有方法基于CLIP的ResNet-50和ViT-B/16。

## 实验关键数据

### 主实验（ResNet-50, ImageNet OOD平均）

**Adapters:**

| 方法 | ACC | ECE |
|------|-----|-----|
| Zero-Shot | 40.62 | 7.18 |
| CLIP-Adapter | 34.07 | 15.45 |
| + SaLS | 34.07 | **8.95** (-6.50) |
| TIP-Adapter(f) | 41.45 | 19.04 |
| + SaLS | 41.45 | **8.13** (-10.91) |
| TaskRes | 41.18 | 11.25 |
| + SaLS | 41.18 | **9.03** (-2.22) |

**Prompt Learning:**

| 方法 | ACC | ECE |
|------|-----|-----|
| CoOp | 40.86 | 10.97 |
| + SaLS | 40.86 | **7.82** (-3.15) |
| CoCoOp | 43.36 | 7.69 |
| + Penalty | 43.86 (+0.50) | **6.15** (-1.54) |

### 消融实验

| 分析 | 结论 |
|------|------|
| Logit范数 vs Logit范围 | 适配后logit范数降低但ECE升高→范数非根因；logit范围增大与ECE升高高度相关→范围是根因 |
| SaLS vs Temperature Scaling | SaLS在OOD上一致更好——TS依赖同分布验证集，在OOD下失效 |
| ZS-Norm vs SaLS | ZS-Norm有时降ACC（因训练时限制了logit范围影响梯度）；SaLS无此问题 |

### 关键发现

- SaLS在不改变ACC的情况下将ECE平均降低40-60%——因为它只改变logit幅度不改变排序
- "logit范围而非范数是miscalibration根因"的发现具有理论意义——推翻了LogitNorm（ICML 2022）的结论（至少在CLIP适配场景下）
- 三种方法中SaLS最实用——零训练、零验证集、即插即用
- Penalty方案在某些情况下甚至提升ACC（CoOp +1.01%），因为logit范围约束起到了正则化作用

## 亮点与洞察

- 发现了CLIP适配方法miscalibration的真正根因（logit范围≠logit范数），纠正了社区的认知偏差
- SaLS是一个极其优雅的解法——用零样本预测作为每个样本的"校准锚点"，无需任何额外数据或训练
- 对三大类CLIP适配方法（PL、Adapter、TTA）的系统性校准评估填补了空白

## 局限性 / 可改进方向

- SaLS依赖零样本logit作为参考——如果零样本本身就严重miscalibrated则效果减弱
- Penalty的$\lambda=10$是全局固定的，不同数据集/方法可能需要不同值
- 仅在分类任务上验证，未扩展到VQA、Caption等生成任务
- 理论分析假设logit非负，实际中可能为负值

## 相关工作与启发

- **vs LogitNorm（ICML 2022）**：LogitNorm认为logit范数增大导致miscalibration并提出范数约束；本文证明在CLIP适配场景下范围才是根因——两个场景的机制不同
- **vs Temperature Scaling**：TS是全局固定温度且需验证集；SaLS是sample-adaptive且无需验证集——在OOD下显著更好
- **启发**：零样本预测可以作为适配方法的"校准基准"——这个思路可能推广到LLM微调的校准问题

## 评分

- 新颖性: ⭐⭐⭐⭐ 发现logit范围vs范数的根因区分，SaLS设计优雅
- 实验充分度: ⭐⭐⭐⭐⭐ 三大类方法×多个数据集×多个backbone的系统评估
- 写作质量: ⭐⭐⭐⭐⭐ 理论分析严谨，实验设计完善
- 价值: ⭐⭐⭐⭐ SaLS实用性强，校准分析填补了CLIP适配文献空白

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_visionlangu.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_visionlanguage_models.md)
- [\[ECCV 2024\] SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](sq-llava_self-questioning_for_large_vision-language_assistant.md)
- [\[ECCV 2024\] NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](navgpt2_unleashing_navigational_reasoning_capability.md)

</div>

<!-- RELATED:END -->
