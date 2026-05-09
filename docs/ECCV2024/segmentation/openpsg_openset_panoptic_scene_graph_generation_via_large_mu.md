---
title: >-
  [论文解读] OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models
description: >-
  [ECCV 2024][图像分割][全景场景图生成] 本文首次提出开放集全景场景图生成任务（OpenPSG），利用大型多模态模型（BLIP-2）以自回归方式预测物体间的开放集关系，通过关系查询Transformer高效提取物体对特征并过滤无关对，在闭集和开放集设置下均取得SOTA。
tags:
  - ECCV 2024
  - 图像分割
  - 全景场景图生成
  - 开放集关系预测
  - 大型多模态模型
  - 自回归生成
  - Transformer
---

# OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models

**会议**: ECCV 2024  
**arXiv**: [2407.11213](https://arxiv.org/abs/2407.11213)  
**代码**: [https://github.com/franciszzj/OpenPSG](https://github.com/franciszzj/OpenPSG)  
**领域**: 图像分割  
**关键词**: 全景场景图生成, 开放集关系预测, 大型多模态模型, 自回归生成, 关系查询Transformer

## 一句话总结

本文首次提出开放集全景场景图生成任务（OpenPSG），利用大型多模态模型（BLIP-2）以自回归方式预测物体间的开放集关系，通过关系查询Transformer高效提取物体对特征并过滤无关对，在闭集和开放集设置下均取得SOTA。

## 研究背景与动机

1. **领域现状**：全景场景图生成（PSG）旨在对图像中的物体进行分割并识别物体间的关系，构建结构化的场景图表示。现有方法如PSGTR、HiLo等均在闭集设置下进行，只能预测预定义类别。

2. **现有痛点**：随着开放集物体检测和分割的快速发展（如CLIP、SAM等大模型推动），开放集的物体识别已取得巨大进步，但关系的开放集预测几乎未被探索。现有方法无法识别训练集之外的新颖关系类别。

3. **核心矛盾**：开放集关系预测比开放集物体检测更具挑战——不仅需要理解不同物体，还需要基于物体间的交互来识别关系，计算量随物体数呈指数增长（N×(N-1)个配对）。

4. **本文要解决什么？** (1) 如何实现开放集的关系类别预测；(2) 如何高效处理大量物体对以降低计算开销；(3) 如何结合开放集物体分割实现真正的开放集PSG。

5. **切入角度**：LLM/LMM在文本理解上不仅擅长名词（物体）也注重谓词（关系），生成内容具有语义连贯性。作者利用这一特性，让LMM以自回归方式预测物体间的开放集关系。

6. **核心idea一句话**：用Relation Query Transformer过滤无关物体对并提取交互特征，再利用LMM的自回归解码能力实现开放集关系预测。

## 方法详解

### 整体框架

OpenPSG由三个核心组件构成：(1) 开放集全景分割器（OpenSeeD）提取物体类别、掩码和全局视觉特征；(2) 关系查询Transformer（RelQ-Former）提取物体对特征并判断关系是否存在；(3) 多模态关系解码器（RelDecoder）基于BLIP-2以自回归方式预测开放集关系。输入一张图像，输出包含开放集物体和关系的全景场景图。

### 关键设计

1. **Patchify与Pairwise模块**:
    - 做什么：将物体分割器输出的视觉特征序列化，并构建所有物体的Subject-Object配对
    - 核心思路：用单层卷积将视觉特征图转换为patch序列 $F_{Iseq} \in \mathbb{R}^{L \times D}$，同时将物体掩码下采样并序列化。对N个物体生成 $N \times (N-1)$ 个配对，并通过逻辑OR操作合并Subject和Object的掩码
    - 设计动机：为后续RelQ-Former提供统一格式的输入，使其能高效地在视觉特征上进行注意力操作

2. **关系查询Transformer（RelQ-Former）**:
    - 做什么：从全局视觉特征中提取物体对的交互特征，并判断物体对之间是否可能存在关系
    - 核心思路：设计两组可学习query——Pair Feature Extraction Query和Relation Existence Estimation Query。前者通过自注意力+掩码交叉注意力+FFN的流程，从视觉特征中提取关注交互区域的物体对特征；后者通过类似流程输出一个二元判断（是否存在关系），用sigmoid归一化到[0,1]
    - 设计动机：(1) 直接mask pooling会平等对待所有区域，但关系预测应更关注交互发生的区域，因此用注意力机制替代；(2) N×(N-1)个物体对中大多数没有关系，引入存在性判断以过滤无关对，推理时实现约20倍加速

3. **多模态关系解码器（RelDecoder）**:
    - 做什么：接收通过过滤的物体对特征，以自回归方式预测开放集关系
    - 核心思路：直接继承BLIP-2的解码器。设计了两种指令模式——Generation指令（"What are the relations between A and B?"直接生成关系词）和Judgement指令（"Please judge between A and B whether there is a relation R"判断特定关系是否存在）。Judgement模式通过缓存prefix特征，对每个候选关系只需处理关系名的token，保持与Generation相同的预测速度
    - 设计动机：Generation倾向于偏好常见关系，Judgement利用LMM的判断能力降低了开放集预测的复杂度

### 损失函数 / 训练策略

总损失为 $\mathcal{L} = \lambda \mathcal{L}_{exist} + \mathcal{L}_{LM}$，其中 $\mathcal{L}_{exist}$ 是关系存在性的二元交叉熵损失，$\mathcal{L}_{LM}$ 是语言模型标准交叉熵损失，$\lambda=10$。训练时冻结物体分割器和多模态解码器，只训练RelQ-Former。使用AdamW优化器，学习率1e-4，12个epoch，4块A100。

## 实验关键数据

### 主实验

| 数据集/设置 | 方法 | PredCls R/mR@50 | SGDet R/mR@50 |
|-------------|------|-----------------|---------------|
| PSG闭集 | HiLo | –/– | 40.7/30.3 |
| PSG闭集 | **OpenPSG** | **70.6/53.8** | **42.9/33.9** |
| PSG开放集 | OvSGTr | –/9.5 | –/– |
| PSG开放集 | **OpenPSG** | **–/30.2** | **–/22.2** |

### 消融实验

| 配置 | PredCls mR@50 | 说明 |
|------|-------------|------|
| Full (OpenPSG-J) | 53.8 | 完整模型，Judgement模式 |
| OpenPSG-G | 51.2 | Generation模式，略低 |
| w/o 存在性估计 | ~48.0 | 去掉过滤模块推理慢且精度降 |
| w/o pair instruction | ~50.5 | 指令辅助query理解任务 |

### 关键发现

- **Judgement指令优于Generation指令**：OpenPSG-J在大多数指标上优于OpenPSG-G，前者利用LMM的判断能力减少了对常见关系的偏好
- **关系存在性估计带来20倍推理加速**：阈值θ=0.35时在精度和效率之间取得最佳平衡
- **在开放集设置下大幅超越以往方法**：在novel关系上的mR@50远超OvSGTr和Pair-Net-O等方法，验证了LMM自回归预测对新颖关系的泛化能力

## 亮点与洞察

- **首次定义开放集PSG任务**：区分了base和novel的物体类别与关系类别，为社区建立新benchmark。这个任务定义本身就是重要贡献
- **Judgement指令设计巧妙**：将开放集关系预测转化为二分类，利用LMM的语义判断能力，同时通过prefix缓存保持效率
- **RelQ-Former的双query设计**：一组query负责特征提取、一组负责存在性判断，分工明确，可迁移到其他需要处理指数级配对的场景

## 局限性 / 可改进方向

- 依赖预训练的开放集分割器（OpenSeeD），分割质量直接影响上游关系预测
- 阈值θ需要手动调节，且不同场景可能需要不同阈值
- Judgement模式在面对完全未见过的关系类型时，仍需要外部提供候选关系列表
- 当前只在PSG和VG数据集上验证，缺乏更大规模、更多样化场景的测试

## 相关工作与启发

- **vs OvSGTr/Pair-Net-O**: 它们用CLIP做对比学习来匹配视觉-文本关系特征，本文直接用LMM自回归生成，避免了固定embedding空间的限制
- **vs HiLo**: HiLo通过分别处理高频/低频关系来缓解长尾偏差，但仍限于闭集。OpenPSG的Judgement方式天然绕开了频率偏差问题
- 场景图的开放集扩展思路可迁移到视频场景图、3D场景图等方向

## 评分

- 新颖性: ⭐⭐⭐⭐ 首个开放集PSG任务定义+LMM自回归关系预测
- 实验充分度: ⭐⭐⭐⭐ PSG和VG双数据集，闭集开放集均验证
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰，任务定义明确
- 价值: ⭐⭐⭐⭐ 为PSG方向开辟了开放集新赛道

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] SPADE: Spatial-Aware Denoising Network for Open-vocabulary Panoptic Scene Graph Generation](../../ICCV2025/segmentation/spade_spatial-aware_denoising_network_for_open-vocabulary_panoptic_scene_graph_g.md)
- [\[ECCV 2024\] EAFormer: Scene Text Segmentation with Edge-Aware Transformers](eaformer_scene_text_segmentation_with_edge-aware_transformers.md)
- [\[ECCV 2024\] VISA: Reasoning Video Object Segmentation via Large Language Models](visa_reasoning_video_object_segmentation_via_large_language_models.md)
- [\[ECCV 2024\] Diffusion Models for Open-Vocabulary Segmentation](diffusion_models_for_open-vocabulary_segmentation.md)
- [\[ECCV 2024\] Attention Decomposition for Cross-Domain Semantic Segmentation](attention_decomposition_for_cross-domain_semantic_segmentation.md)

</div>

<!-- RELATED:END -->
