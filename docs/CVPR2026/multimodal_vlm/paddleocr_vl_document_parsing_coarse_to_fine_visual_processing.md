---
title: >-
  [论文解读] PaddleOCR-VL: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing
description: >-
  [CVPR 2026][多模态][文档解析] 提出 PaddleOCR-VL 粗到精文档解析框架：粗阶段用轻量 VRFM 模块识别有效视觉区域，精阶段用紧凑 0.9B VLM 仅处理有效区域，以最少视觉 token 和参数在 OmniDocBench v1.5 上实现 SOTA，大幅降低延迟和资源消耗。
tags:
  - CVPR 2026
  - 多模态
  - 文档解析
  - 粗到精视觉处理
  - 多模态VLM
  - OCR
  - 视觉token压缩
---

# PaddleOCR-VL: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing

**会议**: CVPR 2026  
**arXiv**: [2603.24326](https://arxiv.org/abs/2603.24326)  
**代码**: [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)  
**领域**: 多模态VLM / 文档理解  
**关键词**: 文档解析, 粗到精视觉处理, 视觉语言模型, OCR, 视觉token压缩

## 一句话总结

提出 PaddleOCR-VL 粗到精文档解析框架：粗阶段用轻量 VRFM 模块识别有效视觉区域，精阶段用紧凑 0.9B VLM 仅处理有效区域，以最少视觉 token 和参数在 OmniDocBench v1.5 上实现 SOTA，大幅降低延迟和资源消耗。

## 研究背景与动机

1. **领域现状**：文档解析是构建 LLM 训练语料和 RAG 系统的关键技术。高分辨率输入对文档解析至关重要但导致视觉 token 数量二次增长。
2. **现有痛点**：流水线方法（检测+识别+结构重建）容易错误传播；通用 VLM 在手写或高度结构化文档上产生幻觉；专用 VLM 参数量大或受坐标漂移影响。
3. **核心矛盾**：高分辨率对细节识别必要 → 视觉 token 数量暴增 → 计算成本高。但文档中有效信息分布极不均匀——PPT 仅 ~39% 区域有效，报纸约 ~60%。
4. **本文目标**：在保持高分辨率精度的同时消除视觉冗余，提高效率。
5. **切入角度**：有效视觉区域的稀疏性——大量背景和装饰元素不包含有用信息。
6. **核心 idea**：粗阶段快速识别有效区域（定位+上下文关系预测），精阶段仅处理这些区域。

## 方法详解

### 整体框架

两阶段：(1) 粗阶段——VRFM（有效区域聚焦模块）快速定位文档元素（文本、公式、表格等）；(2) 精阶段——PaddleOCR-VL-0.9B 对提取的有效区域进行详细识别。两阶段解耦允许独立优化。

### 关键设计

1. **VRFM（有效区域聚焦模块）**:

    - 功能：快速定位文档中的语义有效区域
    - 核心思路：轻量级检测器，同时预测区域位置和区域间的上下文关系（阅读顺序）。相比通用目标检测器，VRFM 针对文档元素优化，速度更快、精度更高。
    - 设计动机：标准 VLM 直接处理整页图像浪费了大量计算在背景区域上。先定位再识别可以大幅减少精阶段的输入量。

2. **PaddleOCR-VL-0.9B**:

    - 功能：对有效视觉区域进行详细的文本/公式/表格识别
    - 核心思路：仅 0.9B 参数的紧凑 VLM，由 VRFM 输出引导，只处理裁剪后的有效区域而非整页大图。通过高质量数据流水线（3000 万+样本）弥补模型规模的不足。
    - 设计动机：小模型 + 精确输入 > 大模型 + 粗粒度输入。0.9B 的规模使得边缘部署成为可能。

3. **大规模高质量数据流水线**:

    - 功能：为小模型提供足够的训练信号
    - 核心思路：从公开数据源和合成数据中收集超过 3000 万个广泛分布的样本，成为模型性能的关键因素之一。
    - 设计动机：小模型的数据效率更低，需要更多高质量数据补偿。

### 损失函数 / 训练策略

VRFM: 标准检测损失 + 阅读顺序预测损失。VLM: 标准语言建模损失。

## 实验关键数据

### 主实验

| 指标 | PaddleOCR-VL | GOT-OCR | Qwen2.5-VL-7B | InternVL3 |
|------|-------------|---------|---------------|-----------|
| 文本分数 | **SOTA** | 次优 | 第三 | 第四 |
| 公式分数 | **SOTA** | 次优 | 第三 | 第四 |
| 表格分数 | **SOTA** | 次优 | 第三 | 第四 |
| 阅读顺序 | **SOTA** | 次优 | 第三 | 第四 |
| 视觉token数 | **最少** | 较多 | 多 | 最多 |
| 参数量 | **0.9B** | 更大 | 7B | 更大 |

### 消融实验

| 配置 | 综合分 | 说明 |
|------|-------|------|
| 完整 PaddleOCR-VL | **SOTA** | VRFM + 0.9B VLM |
| w/o VRFM (直接全图) | 下降 + 慢 | token 数暴增 |
| w/o 数据流水线 | 显著下降 | 数据是小模型的关键 |

### 关键发现

- VRFM 使有效 token 数减少 40-60%，同时性能提升
- 0.9B 模型在专注有效区域时可超越 7B 通用模型
- 数据流水线是 0.9B 模型达到 SOTA 的关键因素之一

## 亮点与洞察

- "小模型 + 精确输入 > 大模型 + 粗粒度输入"的设计哲学对资源受限部署有重要启示
- VRFM 的粗阶段成本远低于 VLM，但可以节省精阶段的大量计算——ROI 约为 10-100 倍
- 解耦设计允许 VRFM 和 VLM 独立优化和升级

## 局限与展望

- VRFM 的检测错误会传播到精阶段（错过的区域无法被识别）
- 对极度复杂布局（如嵌套表格+公式+图像）的鲁棒性有待加强
- 阅读顺序预测在多栏布局下可能出错

## 相关工作与启发

- **vs GOT-OCR**: GOT-OCR 端到端处理整页，计算量大；PaddleOCR-VL 通过粗到精减少冗余
- **vs Qwen2.5-VL**: 通用 VLM 参数量大（7B+），在文档场景过度设计；PaddleOCR-VL 用 0.9B 达到更好效果
- **vs 传统流水线**: 传统流水线缺乏全局语义理解；PaddleOCR-VL 的 VLM 精阶段提供了语义理解能力

## 评分

- 新颖性: ⭐⭐⭐⭐ 粗到精的文档解析框架和 VRFM 设计有实用创新
- 实验充分度: ⭐⭐⭐⭐⭐ OmniDocBench 全面评估，四个维度 SOTA
- 写作质量: ⭐⭐⭐⭐ 效率分析直观，对比清晰
- 价值: ⭐⭐⭐⭐⭐ 开源框架对文档 AI 社区有重要价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Multimodal OCR: Parse Anything from Documents](multimodal_ocr_parse_anything_from_documents.md)
- [\[CVPR 2026\] Efficient Document Parsing via Parallel Token Prediction](efficient_document_parsing_via_parallel_token_prediction.md)
- [\[CVPR 2026\] Towards Real-World Document Parsing via Realistic Scene Synthesis and Document-Aware Training](towards_real-world_document_parsing_via_realistic_scene_synthesis_and_document-a.md)
- [\[CVPR 2026\] V2Drop: Variation-aware Vision Token Dropping for Faster Large Vision-Language Models](v2drop_variation_aware_token_dropping.md)
- [\[CVPR 2026\] DUET-VLM: Dual Stage Unified Efficient Token Reduction for VLM Training and Inference](duet_vlm_dual_stage_token_reduction.md)

</div>

<!-- RELATED:END -->
