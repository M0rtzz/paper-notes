---
title: >-
  ACL2025 图像恢复方向 3篇论文解读
description: >-
  3篇ACL2025 图像恢复论文解读，主题涵盖：本文针对少样本关系抽取中支持集标签噪声问题、DiffuseDef 在编码器与分类器之间插入一个、提出 PreP-OCR 两阶段流水线：先用合成退化等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**💬 ACL2025** · **3** 篇论文解读

**[A Self-Denoising Model for Robust Few-Shot Relation Extraction](a_self-denoising_model_for_robust_few-shot_relation_extraction.md)**

:   本文针对少样本关系抽取中支持集标签噪声问题，提出自去噪模型（SDM），通过标签校正模块和关系分类模块的协同训练，自动修正噪声标签并实现更鲁棒的关系预测，即使在无噪声场景下也显著超越基线。

**[DiffuseDef: Improved Robustness to Adversarial Attacks via Iterative Denoising](diffusedef_adversarial_defense.md)**

:   DiffuseDef 在编码器与分类器之间插入一个扩散去噪层，训练时学习预测隐状态噪声，推理时对隐表示加噪→迭代去噪→集成平均，以即插即用的方式大幅提升文本分类模型在黑盒和白盒对抗攻击下的鲁棒性。

**[PreP-OCR: A Complete Pipeline for Document Image Restoration and Enhanced OCR Accuracy](prep-ocr_a_complete_pipeline_for_document_image_restoration_and_enhanced_ocr_acc.md)**

:   提出 PreP-OCR 两阶段流水线：先用合成退化数据训练的 ResShift 模型修复历史文档图像（多方向 patch 提取+中值融合），再用 ByT5 做 OCR 后语义纠错，在 13,831 页真实历史文档上降低 CER 63.9-70.3%。
