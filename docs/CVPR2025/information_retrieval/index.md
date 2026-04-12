---
title: >-
  CVPR2025 信息检索/RAG方向 2篇论文解读
description: >-
  2篇CVPR2025 信息检索/RAG方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔍 信息检索/RAG

**📷 CVPR2025** · 共 **2** 篇

**[Advancing Myopia To Holism Fully Contrastive Language-Image Pre-Training](advancing_myopia_to_holism_fully_contrastive_language-image_pre-training.md)**

:   将CLIP从传统的一对一(image, text)对比学习升级为多对多(multi-image-embeddings, multi-texts)对比学习范式，通过VLM生成多视角多层次的描述文本、多分支视觉编码器输出多种视觉embedding，实现更全面的视觉语言对齐，在检索/分类/密集任务上大幅超越baseline。

**[Chathuman Chatting About 3D Humans With Tools](chathuman_chatting_about_3d_humans_with_tools.md)**

:   提出 ChatHuman，一个基于 LLM 的语言驱动系统，通过自动选择和集成专门的 3D 人体分析工具（3D 姿态估计、形状恢复、接触检测、人物交互分析、情感识别等），利用学术论文作为工具使用说明和 RAG（检索增强生成）创建 in-context 示例以管理新工具，在工具选择准确率和整体 3D 人体任务性能上超越现有 LLM 模型。
