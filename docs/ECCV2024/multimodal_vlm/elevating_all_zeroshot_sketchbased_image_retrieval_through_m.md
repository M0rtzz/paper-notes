---
title: >-
  [论文解读] SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning
description: >-
  [ECCV 2024][多模态][ZS-SBIR] 提出SpLIP，在冻结CLIP backbone上实现双向prompt共享（视觉→文本、文本→视觉），结合自适应margin三元组损失和条件跨模态拼图任务，首次将多模态prompt learning引入ZS-SBIR，在Sketchy-Ext、TU-Berlin-Ext、QuickDraw-Ext上全面超越现有方法。
tags:
  - ECCV 2024
  - 多模态
  - ZS-SBIR
  - CLIP
  - 提示学习
  - adaptive margin
  - 跨模态
---

# SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning

**会议**: ECCV 2024  
**arXiv**: [2407.04207](https://arxiv.org/abs/2407.04207)  
**代码**: [项目页面](https://mainaksingha01.github.io/SpLIP/)  
**领域**: 零样本Sketch检索 / 多模态Prompt Learning  
**关键词**: ZS-SBIR, CLIP, multimodal prompt, adaptive margin, cross-modal jigsaw

## 一句话总结

提出SpLIP，在冻结CLIP backbone上实现双向prompt共享（视觉→文本、文本→视觉），结合自适应margin三元组损失和条件跨模态拼图任务，首次将多模态prompt learning引入ZS-SBIR，在Sketchy-Ext、TU-Berlin-Ext、QuickDraw-Ext上全面超越现有方法。

## 研究背景与动机

**领域现状**：Sketch-Based Image Retrieval (SBIR)根据手绘草图从图库中检索对应照片，在零样本场景下（测试类别未见过）尤具挑战性。CLIP的强大零样本能力使其成为ZS-SBIR的理想backbone，但已有方法仅利用单模态prompt或简单集成CLIP，未充分挖掘其视觉-文本协同潜力。

**现有痛点**：(1) 已有CLIP-based SBIR方法多为单向prompt（仅视觉或仅文本），无法充分利用双流协同信息；(2) 多模态prompt方法（如MaPLe）的token共享是单向的，文本流对视觉特征不敏感；(3) 细粒度ZS-SBIR需要精确的sketch-photo形状对齐，已有patch shuffling策略不区分正负样本的排列关系。

**核心矛盾**：如何在冻结CLIP的前提下，让视觉和文本prompt之间实现深层双向知识交换，并同时解决类别级和实例级的sketch-photo对齐？

## 方法详解

### 整体框架

SpLIP在冻结的CLIP视觉编码器$\mathcal{F}_v$和文本编码器$\mathcal{F}_t$上构建三个可学习模块：(1) 视觉→文本映射$\mathcal{B}_t$：将图像patch嵌入转换为文本prompt token注入每层$\mathcal{F}_t$；(2) 文本→视觉映射$\mathcal{B}_v$ + $\mathcal{B}_{vt}$：将文本token信息注入每层$\mathcal{F}_v$；(3) 条件跨模态拼图解码器$\mathcal{F}_{js}$用于细粒度对齐。检索时通过$\mathcal{F}_v$输出的嵌入做最近邻排序。

### 关键设计

1. **双向深层prompt共享**

    - **视觉→文本**：通过$\mathcal{B}_t$（3层线性层）将图像patch嵌入$\mathbf{E}_0$转换为$m=4$个文本prompt token $\mathbf{T}$，在$\mathcal{F}_t$的每一层替换部分word embedding——使文本流能"看到"输入图像
    - **文本→视觉**：双通路注入——(a) 通过$\mathcal{B}_v$将"sketch/photo of a"的文本token投射到视觉空间产生$\mathbf{V}^{tg}$；(b) 通过$\mathcal{B}_{vt}$将$\mathcal{F}_t$第$l$层所有类别的文本embedding汇总，生成层特定的视觉token $\mathbf{V}^{ms}$
    - 关键区别：$\mathbf{V}^{ms}$汇聚了所有训练类别$\mathcal{C}^s$的语义信息，是类别无关的——这帮助在推理时泛化到未见类

2. **条件跨模态拼图任务 + 自适应margin三元组损失**

    - 条件拼图：给定打乱的sketch $s'_a$，分别配对正照片$p_a^+$和负照片$p_a^-$送入拼图解码器$\mathcal{F}_{js}$，要求正照片能更好地帮助预测patch排列
    - 自适应margin：三元组损失的margin不再固定，而是由CLIP文本编码器对正/负类名embedding的余弦相似度$\mu(c^+,c^-)$动态决定——语义相近的类别需要更大margin

### 损失函数 / 训练策略

总损失 $\mathcal{L}_{total} = \mathcal{L}_{triplet} + \alpha \cdot \mathcal{L}_{class} + \beta \cdot \mathcal{L}_{cjs}$：

- $\mathcal{L}_{triplet}$：自适应margin的跨模态三元组损失
- $\mathcal{L}_{class}$：基于CLIP相似度的sketch/photo-text分类损失
- $\mathcal{L}_{cjs}$：条件跨模态拼图损失 = CE分类损失 + hinge margin损失

仅训练LayerNorm参数和$(\mathcal{B}_v, \mathcal{B}_t, \mathcal{B}_{vt}, \mathcal{F}_{js})$，CLIP backbone保持冻结。Adam优化，lr=0.001，60 epochs，batch size 192。

## 实验关键数据

### 主实验

| 方法 | Sketchy-1 mAP@all | Sketchy-2 mAP@200 | TU-Berlin mAP@all | QuickDraw mAP@all |
|------|-------------------|-------------------|-------------------|-------------------|
| TCN (TPAMI'21) | 61.6 | 51.6 | 49.5 | 14.0 |
| PSKD (MM'22) | 68.8 | - | 51.8 | - |
| CLIP4SBIR (CVPR'23) | 69.6 | 57.2 | 56.0 | 18.1 |
| **SpLIP (本文)** | **75.2** | **62.8** | **59.4** | **23.6** |

### 消融实验

| 组件 | Sketchy-1 mAP@all | 变化 |
|------|-------------------|------|
| Full SpLIP | 75.2 | - |
| 去掉双向prompt | 71.3 | -3.9 |
| 去掉$\mathbf{V}^{ms}$ | 72.8 | -2.4 |
| 去掉自适应margin | 73.5 | -1.7 |
| 去掉条件拼图 | 73.9 | -1.3 |

### 关键发现

- 双向prompt共享是最重要的设计——去掉后mAP下降3.9%
- $\mathbf{V}^{ms}$汇聚所有类别信息对零样本泛化至关重要（贡献2.4%）
- SpLIP在GZS-SBIR和FG-ZS-SBIR设置下同样全面领先
- 推理时不需要测试类标签——$\mathbf{V}^{ms}$使用训练类生成即可泛化

## 亮点与洞察

- 首次将多模态prompt learning引入ZS-SBIR，建立了该方向的新范式
- 双向prompt共享让CLIP的视觉和文本流实现了深度信息交叉——比单向共享显著更强
- 自适应margin将语义距离编码到度量学习中是一个优雅的设计

## 局限性 / 可改进方向

- 仅在ViT-B/32上实验，未验证更大CLIP模型（ViT-L/14）的效果
- 条件拼图任务增加了训练复杂度但提升有限（+1.3%），性价比可商榷
- 推理时仍使用训练类的$\mathbf{V}^{ms}$，类别数量极多时可能影响效率
- 未探索sketch生成或sketch-to-photo生成等下游应用

## 相关工作与启发

- **vs CLIP4SBIR**：CLIP4SBIR主要做视觉prompt + patch shuffling，SpLIP通过双向prompt和条件拼图全面超越
- **vs MaPLe**：MaPLe的prompt共享是视觉→文本单向的，SpLIP增加了文本→视觉方向并汇聚多类别信息
- **启发**：多模态prompt learning的潜力在跨域检索任务中被低估——双向共享可能也适用于text-image retrieval等场景

## 评分

- 新颖性: ⭐⭐⭐⭐ 首次将多模态prompt引入ZS-SBIR，双向共享设计有创意
- 实验充分度: ⭐⭐⭐⭐ 三个数据集×三种SBIR设置+详细消融
- 写作质量: ⭐⭐⭐⭐ 方法描述严谨，符号系统完整
- 价值: ⭐⭐⭐⭐ 为ZS-SBIR建立了强基线，多模态prompt共享思路可迁移

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs](metaprompting_for_automating_zeroshot_visual_recognitio.md)
- [\[ECCV 2024\] SpLIP: 通过多模态提示学习提升所有零样本草图检索任务](elevating_all_zero-shot_sketch-based_image_retrieval_through_multimodal_prompt_l.md)
- [\[CVPR 2025\] Visual and Semantic Prompt Collaboration for Generalized Zero-Shot Learning](../../CVPR2025/multimodal_vlm/visual_and_semantic_prompt_collaboration_for_generalized_zero-shot_learning.md)
- [\[CVPR 2026\] Noise-Aware Few-Shot Learning through Bi-directional Multi-View Prompt Alignment](../../CVPR2026/multimodal_vlm/noiseaware_fewshot_learning_through_bidirectional.md)
- [\[ECCV 2024\] Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_visionlangu.md)

<!-- RELATED:END -->
