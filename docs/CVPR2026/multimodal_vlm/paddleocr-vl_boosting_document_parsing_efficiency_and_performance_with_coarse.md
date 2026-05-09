---
title: >-
  [论文解读] PaddleOCR-VL: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing
description: >-
  [CVPR 2026][多模态][文档解析] PaddleOCR-VL 提出粗到细（coarse-to-fine）的文档解析框架，先用轻量 VRFM 模块检测有效区域和阅读顺序，再用紧凑的 0.9B VLM 进行精细识别，以最少的视觉 token 和参数实现了文档解析 SOTA。
tags:
  - CVPR 2026
  - 多模态
  - 文档解析
  - 粗到细
  - 视觉冗余
  - OCR
  - 多模态VLM
---

# PaddleOCR-VL: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing

**会议**: CVPR 2026  
**arXiv**: [2603.24326](https://arxiv.org/abs/2603.24326)  
**代码**: [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)  
**领域**: 多模态VLM / 文档理解  
**关键词**: 文档解析, 粗到细, 视觉冗余, OCR, 视觉语言模型

## 一句话总结

PaddleOCR-VL 提出粗到细（coarse-to-fine）的文档解析框架，先用轻量 VRFM 模块检测有效区域和阅读顺序，再用紧凑的 0.9B VLM 进行精细识别，以最少的视觉 token 和参数实现了文档解析 SOTA。

## 研究背景与动机

文档解析需要识别文本、公式、表格等元素并确定正确阅读顺序。当前方案分三类：流水线方法（易错误传播）、通用 VLM（幻觉严重、计算昂贵）和专用 VLM（端到端参数量大或坐标漂移）。

**核心痛点**：高分辨率输入对文档解析至关重要，但视觉编码的计算成本随分辨率二次增长。文档图像的视觉信息高度不均匀——PPT 中有效区域仅占约 39%，即使信息密集的报纸也只占约 60%。

**本文切入**：既然文档中大量区域是冗余背景，不如先快速定位有效区域，再只对这些区域做精细识别。这种解耦设计让每个模块各司其职，同时大幅减少送入 VLM 的视觉 token 数量。

## 方法详解

### 整体框架

两阶段流水线：粗阶段 VRFM 检测文档元素、分类和预测阅读顺序 → 裁切有效区域 → 细阶段 PaddleOCR-VL-0.9B 对每个区域做精细识别 → 按阅读顺序重组为结构化文档。

### 关键设计

1. **有效区域聚焦模块 (VRFM)**:

    - 功能：高效定位文档中的有效视觉元素并预测阅读顺序
    - 核心思路：基于 RT-DETR 检测器进行布局元素检测和分类，在此基础上扩展指针网络（Pointer Network）预测 $N \times N$ 的阅读顺序矩阵。训练分两阶段：先训 RT-DETR（100 epochs），再冻结核心只训指针网络（200 epochs，使用噪声鲁棒的 Generalized Cross Entropy Loss）
    - 设计动机：将区域检测和阅读顺序预测统一在轻量框架中，避免将大量冗余背景送入后续 VLM

2. **PaddleOCR-VL-0.9B 元素识别模型**:

    - 功能：对裁切出的有效区域做精细的多类型识别（文本/表格/公式/图表）
    - 核心思路：采用 NaViT 风格视觉编码器（Keye-VL 初始化）+ 2 层 MLP 投影器 + ERNIE-4.5-0.3B 语言模型（配 3D-RoPE）。关键特点是原生动态分辨率处理，避免固定分辨率或切片带来的失真和幻觉
    - 设计动机：0.9B 参数极其紧凑，但因为只处理裁切后的有效区域（而非整个页面），信息密度更高，反而获得更好的识别效果

3. **高质量数据流水线**:

    - 功能：构建 30M+ 训练样本的多来源数据集
    - 核心思路：四来源（开源+合成+网络爬取+内部数据）+ 自动标注（PP-StructureV3 初标 → VLM 精修 → 幻觉过滤）+ 难例挖掘（细粒度评测找弱项 → 合成针对性数据）
    - 设计动机：数据质量是性能的关键因素，难例挖掘形成"评测-合成-训练"的闭环

### 损失函数 / 训练策略

VLM 两阶段训练：Stage 1 用 29M 样本做预训练对齐（1 epoch，LR 5e-5→5e-6），Stage 2 用 2.7M 样本做指令微调（2 epochs，更高分辨率上限 2048，LR 5e-6→5e-7）。

## 实验关键数据

### 主实验

| 方法 | 参数量 | 视觉Token | Overall↑ | Text↓ | Formula↑ | Table↑ | ReadOrder↓ |
|------|--------|-----------|----------|-------|----------|--------|------------|
| Gemini-2.5 Pro | - | - | 88.03 | 0.075 | 85.82 | 85.71 | 0.097 |
| Qwen2.5-VL-72B | 72B | 5626 | 87.02 | 0.094 | 88.27 | 82.15 | 0.102 |
| PaddleOCR-VL | **0.9B** | **最少** | **91.32** | **0.046** | **90.98** | **85.77** | **0.050** |

在 OmniDocBench v1.5 上以最少的参数和视觉 token 超越所有方法。

### 消融实验

| 配置 | Overall | 说明 |
|------|---------|------|
| 端到端 VLM（无 VRFM） | 更低 | 处理全图效率低且效果差 |
| VRFM + PaddleOCR-VL-0.9B | 91.32 | 粗到细策略的完整效果 |
| 无难例挖掘 | 明显下降 | 数据质量闭环至关重要 |

### 关键发现

- 0.9B 模型在所有四个核心指标上超越 72B/241B 的通用 VLM，证明"只看有效区域"比"大模型看全图"更高效
- 支持 109 种语言，在手写体和历史文档等困难场景也保持鲁棒
- 推理延迟和吞吐量大幅优于竞争方案

## 亮点与洞察

- **小而精的设计哲学**：通过精准裁切避免 VLM 处理无用像素，0.9B 打败 72B，这说明"喂什么"比"模型多大"更重要
- **粗细解耦的工程价值**：VRFM 和 VLM 可独立优化、独立升级，维护成本低
- **数据闭环的启示**：评测-难例挖掘-合成数据的闭环流程，对所有领域特定 VLM 的训练都有参考价值

## 局限与展望

- VRFM 的检测精度对下游识别有连锁影响——漏检区域会直接丢失信息
- 阅读顺序预测依赖指针网络，对极度复杂的跨页布局可能不够鲁棒
- 两阶段设计引入额外延迟，虽然总体更快但不如真正的端到端简洁
- 未来可探索 VRFM 与 VLM 的联合训练或端到端优化

## 相关工作与启发

- **vs MinerU/Dolphin**: 端到端 VLM 方案参数量大、阅读顺序易混乱，PaddleOCR-VL 通过解耦避免了这些问题
- **vs DeepSeek-OCR**: DeepSeek-OCR 用统一的视觉 token 压缩，但粗粒度压缩损失布局精度；PaddleOCR-VL 的选择性聚焦更精准
- **vs PP-StructureV3**: 传统流水线方案，PaddleOCR-VL 在识别阶段引入 VLM 获得更强的语义理解能力

## 评分

- 新颖性: ⭐⭐⭐⭐ 粗到细思路不新，但文档场景的具体设计很精到
- 实验充分度: ⭐⭐⭐⭐⭐ 多基准全面对比，覆盖各类文档类型
- 写作质量: ⭐⭐⭐⭐ 结构清晰，数据详实
- 价值: ⭐⭐⭐⭐⭐ 开源且性能突出，实际工业应用价值很高

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Multimodal OCR: Parse Anything from Documents](multimodal_ocr_parse_anything_from_documents.md)
- [\[CVPR 2026\] Efficient Document Parsing via Parallel Token Prediction](efficient_document_parsing_via_parallel_token_prediction.md)
- [\[CVPR 2026\] Towards Real-World Document Parsing via Realistic Scene Synthesis and Document-Aware Training](towards_real-world_document_parsing_via_realistic_scene_synthesis_and_document-a.md)
- [\[CVPR 2026\] DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding](docseeker_long_document_understanding.md)
- [\[CVPR 2026\] ReasonMap: Towards Fine-Grained Visual Reasoning from Transit Maps](reasonmap_towards_finegrained_visual_reasoning_fro.md)

</div>

<!-- RELATED:END -->
