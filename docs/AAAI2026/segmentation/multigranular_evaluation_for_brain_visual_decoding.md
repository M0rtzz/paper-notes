---
description: "【论文笔记】Multigranular Evaluation for Brain Visual Decoding 论文解读 | AAAI 2026 | arXiv 2507.07993 | brain decoding | 提出 BASIC 多粒度评估框架，从结构（分割 mask 匹配）、推理（对象/属性/关系语义图）和上下文（场景叙事一致性）三个维度统一评估脑视觉解码质量，解决现有指标饱和、缺乏神经科学基础、无法区分模型差异的问题。"
tags:
  - AAAI 2026
  - 图像分割
---

# Multigranular Evaluation for Brain Visual Decoding

**会议**: AAAI 2026  
**arXiv**: [2507.07993](https://arxiv.org/abs/2507.07993)  
**代码**: [GitHub](https://github.com/weihaox/BASIC)  
**领域**: 脑视觉解码评估  
**关键词**: brain decoding, evaluation metric, segmentation, semantic matching, MLLM  

## 一句话总结
提出 BASIC 多粒度评估框架，从结构（分割 mask 匹配）、推理（对象/属性/关系语义图）和上下文（场景叙事一致性）三个维度统一评估脑视觉解码质量，解决现有指标饱和、缺乏神经科学基础、无法区分模型差异的问题。

## 背景与动机
脑视觉解码（Brain Visual Decoding）近年取得显著进展，能从 fMRI/EEG 等神经信号重建视觉刺激。然而现有评估体系存在三个核心缺陷：(1) 指标饱和——PixCorr、SSIM、CLIP 等主流指标在 SOTA 模型间得分趋同，无法区分模型差异；(2) 缺乏神经科学基础——未反映人类视觉感知的层次化特性；(3) 诊断能力不足——将多维对齐压缩为单一分数，无法定位重建失败的具体位置和原因。

人类视觉感知是多层次、结构化的过程，从低级像素模式到高级语义理解。脑解码的评估也应该反映这种层次结构，需要同时考察结构保真度、语义准确性和上下文合理性。

现有指标还难以判断解码出的细节是否真正来自脑信号，还是生成模型基于场景/物体标签的先验知识"幻觉"出的内容（hallucinated constructs）。

## 核心问题
如何设计一个统一的、多粒度的脑视觉解码评估框架，使其具备区分力、可解释性和神经科学合理性？

## 方法详解

### 整体框架
BASIC (Brain-Aligned Structural, Inferential, and Contextual similarity) 分为两个互补子指标：
- **BASIC-L**（低级结构相似度）：基于分割 mask 的多粒度结构匹配
- **BASIC-H**（高级语义相似度）：结合推理和上下文维度的语义对应

### 关键设计

**评估维度体系**：定义 5 个维度——Scene（布局/几何/事件/风格）、Object（类别/通用性/特异性）、Attribute（外观/位置/数量/文字）、Relation（空间/部分-整体/交互/运动）、Camera（光照/角度/运动）。

**BASIC-L：结构相似度**  
在四个分割粒度上计算 IoU 和 AP：
- **Foreground (F)**：前景显著性分割
- **Binary/Semantic (B/S)**：语义类别分割
- **Instance (I)**：实例级分割
- **Part (P)**：部件级分割

对重建图和参考图分别进行多粒度分割，通过粒度感知的 mask 对应匹配计算结构保真度。

**BASIC-H：语义相似度**  
三步流水线：
1. 使用 MLLM 为重建图和参考图生成语义丰富的详细描述
2. 将描述解析为语义图（对象、属性、关系）
3. 结合符号化概念匹配和 embedding 相似度计算语义对应

对 Object、Attribute、Relation 分别计算 Precision、Recall、F1，综合得到 BASIC-H 分数。

## 实验关键数据

在 NSD (fMRI-Image) 数据集上 BASIC-H 评估结果（F1）：

| 方法 | Object F1 | Attribute F1 | Relation F1 | BASIC-H |
|------|-----------|-------------|-------------|---------|
| SDRecon | 53.79 | 14.96 | 39.06 | 35.31 |
| MindEye | 61.26 | 25.06 | 48.84 | 44.30 |
| DREAM | 63.56 | 25.92 | 52.91 | 46.37 |
| NeuroVLA | 64.57 | 28.65 | 52.95 | **47.88** |
| STTM | 62.88 | 26.64 | 50.36 | 45.88 |

BASIC-L 评估（NSD）：NeuroPictor 以 25.88 领先，MindEye2 为 22.16，体现了结构匹配的区分能力。

跨模态覆盖：框架统一评估了 fMRI-Image、EEG-Image、fMRI-Video、EEG-Video、fMRI-3D、EEG-3D 共 6 种组合。

## 亮点
- 首个面向脑视觉解码的多粒度统一评估框架，涵盖结构-推理-上下文三个层面
- 利用 MLLM 提取结构化语义表示（对象、属性、关系图），实现可扩展的自动化评估
- 跨模态泛用性：同一框架适用于 fMRI/EEG × Image/Video/3D 的多种组合
- 具有更强的区分力：在现有指标饱和的情况下仍能区分不同方法的表现
- 评估维度体系设计有神经科学和认知心理学的理论支撑

## 局限性 / 可改进方向
- MLLM 生成描述存在幻觉风险，可能引入评估噪声
- 分割模型本身的精度会影响 BASIC-L 的可靠性
- 缺乏与人类感知判断的直接相关性验证（human correlation study）
- 语义图构建依赖文本解析，复杂场景中的关系提取可能不完整

## 与相关工作的对比
与传统指标（PixCorr/SSIM/CLIP/AlexNet-2/5 等）相比，BASIC 提供了多粒度、可解释的评估，不再将所有维度压缩为单一分数。与 nn-way 分类准确率等特定指标相比，BASIC 具有跨数据集/跨模态的统一性。框架同时覆盖低级结构和高级语义，填补了此前评估只关注某一层面的空白。

## 启发与关联
- 利用 MLLM 做自动化评估的思路可推广到其他图像生成/编辑任务的评估
- 语义图匹配的方法可借鉴用于 scene graph generation 的评估
- 多粒度分割匹配的设计对 image segmentation 质量评估有参考价值

## 评分
- 新颖性: ⭐⭐⭐⭐
- 实验充分度: ⭐⭐⭐⭐⭐
- 写作质量: ⭐⭐⭐⭐
- 价值: ⭐⭐⭐⭐
