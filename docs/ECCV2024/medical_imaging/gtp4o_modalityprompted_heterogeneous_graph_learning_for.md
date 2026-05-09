---
title: >-
  [论文解读] GTP-4o: Modality-prompted Heterogeneous Graph Learning for Omni-modal Biomedical Representation
description: >-
  [ECCV 2024][医学图像][异构图] 提出 GTP-4o，一种基于异构图的全模态生物医学学习框架，通过图提示机制补全缺失模态、知识引导的层次聚合融合基因组学/病理图像/细胞图/文本四种异构临床模态。
tags:
  - ECCV 2024
  - 医学图像
  - 异构图
  - 多模态融合
  - 模态缺失
  - 图提示
  - 生存预测
---

# GTP-4o: Modality-prompted Heterogeneous Graph Learning for Omni-modal Biomedical Representation

**会议**: ECCV 2024  
**arXiv**: [2407.05540](https://arxiv.org/abs/2407.05540)  
**代码**: [https://gtp-4-o.github.io/](https://gtp-4-o.github.io/)  
**领域**: 医学图像 / 多模态学习  
**关键词**: 异构图, 多模态融合, 模态缺失, 图提示, 生存预测

## 一句话总结
提出 GTP-4o，一种基于异构图的全模态生物医学学习框架，通过图提示机制补全缺失模态、知识引导的层次聚合融合基因组学/病理图像/细胞图/文本四种异构临床模态。

## 研究背景与动机

**领域现状**：生物医学多模态融合（基因组+病理图像+文本报告）已在疾病诊断中取得进展，主流方法通过交叉注意力或最优传输对齐不同模态。

**现有痛点**：(1) 生物医学模态间的语义异质性极大——基因组和病理图像之间不像自然图像与文本那样有直观的对应关系；(2) 现有方法用统一的注意力处理所有跨模态关系，忽略了不同模态对之间关系的本质差异（如基因→图像是"表达"，图像→文本是"描述"）；(3) 临床实践中模态缺失是常态，但多数方法假设数据完整。

**核心矛盾**：需要一种表示方法既能捕获不同模态和跨模态关系上的异质属性，又能优雅地处理模态缺失情况。

**本文目标**：从基因组学、病理图像、细胞空间图和诊断文本四种异构临床模态中学习统一表示，同时处理训练/测试时的模态缺失。

**切入角度**：利用异构图天然支持不同类型节点和边的特性，将多模态融合重构为异构图上的消息传递问题。

**核心 idea**：将每个模态实例作为异构图节点（带模态类型属性），跨模态关系作为异构边（带关系语义属性），用图提示（graph prompting）为缺失模态生成幻觉节点，再通过知识引导的元路径聚合进行跨模态信息融合。

## 方法详解

### 整体框架
输入四种模态的特征通过异构图嵌入映射到统一图空间 → 模态缺失时通过图提示生成幻觉节点补全 → 全局元路径邻居发现+局部多关系聚合 → 任务特定头做分类/生存预测。

### 关键设计

1. **异构图嵌入 (Heterogeneous Graph Embedding)**:

    - 功能：显式捕获模态实例（节点）和跨模态关系（边）上的异构属性
    - 核心思路：构建图 $\mathcal{G} = \{\mathcal{V}, \mathcal{E}, \mathcal{A}, \mathcal{R}\}$，节点属性集 $\mathcal{A} = \{G, I, C, T\}$ 对应四种模态，边属性集 $\mathcal{R} = \{\text{"express"}, \text{"depict"}, \text{"atomize"}, \text{"intra-modal"}\}$ 编码跨模态语义关系。初始边权重用头尾节点的余弦相似度
    - 设计动机：相比把所有跨模态交互塞进同一个注意力矩阵，异构图显式区分了"基因组→图像"和"图像→文本"的关系类型，使模型能学习关系特定的聚合策略

2. **模态提示补全 (Modality-prompted Completion)**:

    - 功能：当某模态缺失时，生成幻觉图节点补全图表示
    - 核心思路：训练一个图提示模块 $g_\phi$，为缺失模态生成幻觉节点特征和拓扑连接。提示模块学习将不完整图嵌入映射到完整图嵌入的空间，使下游聚合能正常工作
    - 设计动机：临床中隐私/伦理/技术限制导致模态缺失普遍，与其在缺失时降级使用不完整特征，不如主动补全维持融合效果

3. **知识引导的层次聚合**:

    - 功能：在异构图上进行有意义的跨模态信息融合
    - 核心思路：分两层——(a) 全局元路径邻居：基于领域知识定义元路径（如 基因→图像→文本），发现图中的高阶异构邻居关系；(b) 局部多关系聚合：对每种边类型分别做消息传递，然后融合不同关系的聚合结果
    - 设计动机：元路径利用领域先验减少无效的节点交互，多关系聚合尊重不同关系的语义特异性

### 损失函数 / 训练策略
胶质瘤分级：交叉熵损失。生存预测：Cox 回归损失（负对数部分似然）。模态缺失在训练时随机模拟。

## 实验关键数据

### 主实验

| 任务 | GTP-4o | PathomicFusion | MCAT | 备注 |
|------|--------|----------------|------|------|
| 胶质瘤分级 (ACC%) | 最优 | 次优 | 较低 | 完整模态 |
| 生存预测 (C-index) | 最优 | 较低 | 次优 | 完整模态 |
| 模态缺失场景 | 性能稳定 | 显著下降 | 显著下降 | 缺少1-2个模态 |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 完整 GTP-4o | 最优 | 异构图+提示+层次聚合 |
| 无图提示补全 | 模态缺失时显著下降 | 补全模块关键 |
| 同构图替代异构图 | 下降 | 异构属性有助于区分关系 |
| 无元路径（仅局部聚合） | 下降 | 全局高阶关系重要 |
| 2 模态 vs 4 模态 | 4 模态显著更优 | 支持模态越多效果越好 |

### 关键发现
- 异构图嵌入相比同构图在融合效果上有明显优势，显式的关系类型建模确实有帮助
- 图提示补全在模态缺失场景下效果显著——相比简单的零向量填充，性能提升明显
- 四模态联合（基因组+图像+细胞图+文本）效果优于任何模态子集

## 亮点与洞察
- **异构图作为多模态融合范式**是一个优雅的框架——不同模态是不同类型的节点，不同关系是不同类型的边，这比"拼接+注意力"的范式更结构化
- **图提示补全缺失模态**的想法很新颖，可迁移到任何多模态场景（如自动驾驶的传感器缺失）
- 用 LLM (MiniGPT-4) 为病理图像生成文本描述作为第四模态，是一种创造性的数据增强

## 局限与展望
- 文本模态依赖 MiniGPT-4 生成的描述而非真实的诊断报告，质量和信息量有限
- 元路径需要领域专家手动设计，自动化元路径发现可作为未来方向
- 仅在胶质瘤数据上验证，泛化到其他癌症类型需要额外验证
- 异构图的构建和聚合增加了模型复杂度，推理效率需要关注

## 相关工作与启发
- **vs PathomicFusion**: 用 Kronecker 积融合基因组和图像，但不显式建模跨模态关系类型，且不处理模态缺失
- **vs MCAT (Chen et al.)**: 用交叉注意力融合基因组和图像，但只处理两种模态
- **vs PatchGCN**: 仅用同构图处理病理图像单模态，GTP-4o 将图扩展到多模态异构设置

## 评分
- 新颖性: ⭐⭐⭐⭐ 异构图+图提示的组合在生物医学多模态中是首创
- 实验充分度: ⭐⭐⭐⭐ 完整/缺失模态、消融、多任务全面对比
- 写作质量: ⭐⭐⭐⭐ 框架图清晰，模块化设计描述详细
- 价值: ⭐⭐⭐⭐ 为临床多模态学习提供了处理模态异构性和缺失的系统方案

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Improving Medical Multi-modal Contrastive Learning with Expert Annotations](improving_medical_multi-modal_contrastive_learning_with_expert_annotations.md)
- [\[ECCV 2024\] Energy-induced Explicit Quantification for Multi-modality MRI Fusion](energy-induced_explicit_quantification_for_multi-modality_mri_fusion.md)
- [\[ECCV 2024\] RadEdit: Stress-Testing Biomedical Vision Models via Diffusion Image Editing](radedit_stress-testing_biomedical_vision_models_via_diffusion_image_editing.md)
- [\[ECCV 2024\] Unsupervised Multi-modal Medical Image Registration via Invertible Translation](unsupervised_multi-modal_medical_image_registration_via_invertible_translation.md)
- [\[CVPR 2026\] MUST: Modality-Specific Representation-Aware Transformer for Diffusion-Enhanced Survival Prediction with Missing Modality](../../CVPR2026/medical_imaging/must_modality-specific_representation-aware_transformer_for_diffusion-enhanced_s.md)

</div>

<!-- RELATED:END -->
