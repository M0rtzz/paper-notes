---
title: >-
  ACL2025 图像恢复方向 2篇论文解读
description: >-
  2篇ACL2025 图像恢复方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**💬 ACL2025** · 共 **2** 篇

**[Diffusedef Adversarial Defense](diffusedef_adversarial_defense.md)**

:   DiffuseDef 提出了一种将扩散层作为去噪器插入编码器和分类器之间的对抗防御方法，通过扩散训练学会预测隐状态噪声，推理时对对抗隐状态加噪+迭代去噪+集成，在黑盒和白盒攻击下达 SOTA 鲁棒性。

**[Prep-Ocr A Complete Pipeline For Document Image Restoration And Enhanced Ocr Acc](prep-ocr_a_complete_pipeline_for_document_image_restoration_and_enhanced_ocr_acc.md)**

:   提出 PreP-OCR 两阶段流水线：先用合成退化数据训练的 ResShift 模型修复历史文档图像（多方向 patch 提取+中值融合），再用 ByT5 做 OCR 后语义纠错，在 13,831 页真实历史文档上降低 CER 63.9-70.3%。
