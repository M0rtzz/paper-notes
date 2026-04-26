---
title: >-
  [论文解读] DeCUR: Decoupling Common and Unique Representations for Multimodal Self-supervised Learning
description: >-
  [ECCV 2024][多模态][多模态] 将Barlow Twins扩展到多模态场景，通过将嵌入维度显式分为跨模态公共（对齐到identity矩阵）和模态独特（推到零矩阵）两部分，配合模态内自监督训练避免退化，在SAR-光学、RGB-DEM、RGB-深度三类场景中一致超越SimCLR-cross和Barlow Twins基线。
tags:
  - ECCV 2024
  - 多模态
  - representation decoupling
  - Barlow Twins
  - remote sensing
  - RGB-depth
---

# DeCUR: Decoupling Common and Unique Representations for Multimodal Self-supervised Learning

**会议**: ECCV 2024  
**arXiv**: [2309.05300](https://arxiv.org/abs/2309.05300)  
**代码**: [GitHub](https://github.com/zhu-xlab/DeCUR)  
**领域**: 多模态自监督学习 / 表示解耦  
**关键词**: multimodal SSL, representation decoupling, Barlow Twins, remote sensing, RGB-depth

## 一句话总结

将Barlow Twins扩展到多模态场景，通过将嵌入维度显式分为跨模态公共（对齐到identity矩阵）和模态独特（推到零矩阵）两部分，配合模态内自监督训练避免退化，在SAR-光学、RGB-DEM、RGB-深度三类场景中一致超越SimCLR-cross和Barlow Twins基线。

## 研究背景与动机

**领域现状**：多模态自监督学习主要通过跨模态对比学习（如CLIP、SimCLR-cross）将不同模态对齐到公共嵌入空间。这些方法只学习跨模态共享信息，忽略了模态独特信息（如SAR的纹理结构、光学的颜色信息），导致表示能力受限。

**现有痛点**：(1) 纯跨模态对齐会压制模态特有信息，迫使模型将正交的表示塞入共享空间；(2) 已有解耦方法（FactorCL等）需要模态特定的增强策略或复杂的信息瓶颈，实现复杂；(3) 缺少模态内训练导致独特维度可能退化为无意义值。

**核心矛盾**：如何在一个简单框架中同时学习跨模态共享表示和模态独特表示，且防止独特维度退化？

## 方法详解

### 整体框架

DeCUR是Barlow Twins的多模态扩展。两个模态各有独立的编码器和3层MLP投射器，产出嵌入后分为公共维度（$K_c$个）和独特维度（$K_u$个）。跨模态：公共维度的互相关矩阵→驱向identity（对齐），独特维度的互相关矩阵→驱向zero（解耦）。模态内：每个模态用两个增广视图计算全维度互相关矩阵→驱向identity（自监督）。可选在ConvNet最后两层加入Deformable Attention增强模态敏感区域聚焦。

### 关键设计

1. **跨模态表示解耦**

    - 将总嵌入维度$K$分为$K_c$（公共）和$K_u$（独特），比例通过网格搜索确定（SAR-光学87.5%公共，RGB-DEM/深度75%公共）
    - 公共维度损失$\mathcal{L}_{com}$：驱动互相关矩阵$\mathcal{C}_c$对角线为1（不变性）、非对角线为0（去冗余）
    - 独特维度损失$\mathcal{L}_{uni}$：驱动$\mathcal{C}_u$所有元素为0——确保两个模态的独特维度互不相关
    - 设计动机：直接在嵌入维度上操作，无需信息瓶颈或特殊增强，实现极其简单

2. **模态内表示增强**

    - 对每个模态用Barlow Twins方式训练（两个增广视图的全维度互相关矩阵→identity）
    - 关键作用：防止独特维度退化——如果只推独特维度跨模态为零而无模态内约束，这些维度可能坍缩到随机不相关值
    - 同时为跨模态学习提供更强的模态内知识基础

### 损失函数 / 训练策略

总损失 $\mathcal{L} = \mathcal{L}_{com} + \mathcal{L}_{uni} + \mathcal{L}_{M1} + \mathcal{L}_{M2}$

各项中的权衡系数$\lambda$统一设为0.0051。投射器输出维度8192。ResNet-50 backbone + 可选Deformable Attention。分布式4×A100，SSL4EO-S12 100 epochs，GeoNRW 100 epochs，SUN-RGBD 200 epochs，batch size 128-256。

## 实验关键数据

### 主实验

**SAR-光学场景分类（BigEarthNet-MM mAP，linear/fine-tune）：**

| 方法 | 多模态 1% | 多模态 100% | SAR-only 1% | SAR-only 100% |
|------|----------|-----------|------------|-------------|
| SimCLR-cross | 77.4/78.7 | 82.8/89.6 | 68.1/70.4 | 71.7/83.7 |
| Barlow Twins | 78.7/80.3 | 83.2/89.5 | 72.3/73.7 | 77.8/83.6 |
| **DeCUR** | **79.8/81.5** | **86.2/89.8** | **74.4/76.0** | **79.5/84.0** |

**RGB-DEM语义分割（GeoNRW mIoU）：**

| 方法 | 多模态 Frozen 1% | 多模态 Fine-tune 100% |
|------|----------------|---------------------|
| SimCLR-cross | 23.0 | 47.3 |
| Barlow Twins | 31.2 | 48.4 |
| **DeCUR** | **34.7** | **48.9** |

### 消融实验

| 消融项 | BigEarthNet mAP (100%) |
|--------|----------------------|
| Full DeCUR | 86.2 |
| 无$\mathcal{L}_{uni}$（无解耦） | 83.6 |
| 无模态内损失 | 84.1 |
| 无Deformable Attention | 85.5 |
| 公共比例 75% / 87.5% / 100% | 85.8 / 86.2 / 83.2 |

### 关键发现

- 解耦损失$\mathcal{L}_{uni}$贡献最大（+2.6%），证实了显式解耦的必要性
- 100%公共维度（即标准Barlow Twins）表现最差——独特维度携带了不可忽视的模态特有信息
- SAR-only场景中DeCUR比单模态Barlow Twins高2-3%——多模态预训练帮助模型更好理解单个模态
- 与ResNet-50规模的EO基础模型相比，DeCUR达到同等水平（BigEarthNet-S2 87.2% vs SeCo 82.6%）

## 亮点与洞察

- 极其简单优雅的方法——只需在Barlow Twins的互相关矩阵上做维度切分，无需额外架构或复杂训练策略
- 模态内训练是防止独特维度退化的关键，解决了一个容易被忽视的工程问题
- t-SNE可视化清晰展示了公共和独特维度的分离效果

## 局限性 / 可改进方向

- 公共/独特维度比例需要手动搜索，缺乏自适应确定机制
- 仅在ResNet-50和MiT上验证，未测试更大backbone（ViT-L等）
- 三个场景的数据规模较小（最大251K），在更大规模数据上的效果未知
- 只考虑了双模态情况，扩展到三模态及以上的方案未讨论

## 相关工作与启发

- **vs Barlow Twins**：DeCUR是其自然的多模态扩展，核心改进是将嵌入分为公共和独特维度
- **vs FactorCL**：FactorCL需要模态特定增强和信息论约束，DeCUR更简洁——直接在维度上操作
- **vs CLIP/CROMA**：这些对比学习方法只学共享表示；DeCUR额外保留模态独特信息
- **启发**：在遥感等多传感器场景，模态独特信息（如SAR的穿透能力）可能比共享信息更有价值——有必要显式保留

## 评分

- 新颖性: ⭐⭐⭐⭐ 维度切分解耦思路简洁有效，Barlow Twins的自然且有意义的扩展
- 实验充分度: ⭐⭐⭐⭐ 三种多模态场景+多模态/单模态评估+详细消融
- 写作质量: ⭐⭐⭐⭐ 方法清晰，损失设计逻辑自洽
- 价值: ⭐⭐⭐⭐ 对多模态自监督学习有启发，方法简单易复现

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](decoupling_common_and_unique_representations_for_multimodal_self-supervised_lear.md)
- [\[ECCV 2024\] SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](sqllava_selfquestioning_for_large_visionlanguage_assistant.md)
- [\[ECCV 2024\] UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_lan.md)
- [\[ECCV 2024\] Self-Adapting Large Visual-Language Models to Edge Devices across Visual Modalities](self-adapting_large_visual-language_models_to_edge_devices_across_visual_modalit.md)
- [\[ECCV 2024\] SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)

<!-- RELATED:END -->
