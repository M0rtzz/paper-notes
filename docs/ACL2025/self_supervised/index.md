---
title: >-
  ACL2025 自监督/表示学习方向 6篇论文解读
description: >-
  6篇ACL2025 自监督/表示学习方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**💬 ACL2025** · 共 **6** 篇

**[Improving Low-Resource Morphological Inflection Via Self-Supervised Objectives](improving_low-resource_morphological_inflection_via_self-supervised_objectives.md)**

:   系统探索 13 种自监督辅助目标（自编码、CMLM、T5-style 等）在极低资源形态变化任务中的效果，发现无标注数据极少时自编码最优，数据增多后字符级 MLM 更好，按形态素边界采样掩码是最有前景的方向。

**[Llm Back Gen Treebank](llm_back_gen_treebank.md)**

:   提出 LLM 反向生成方法自动构建跨领域成分句法树库——给定只有领域关键词叶节点的不完整句法树，用 LLM 填充缺失词汇生成完整的跨领域句法树库，结合 span 级对比学习预训练，在 MCTB 五个目标领域上达到跨领域成分句法分析 SOTA。

**[Magnet Augmenting Generative Decoders With Representation Learning And Infilling](magnet_augmenting_generative_decoders_with_representation_learning_and_infilling.md)**

:   提出 Magnet 方法，通过混合注意力机制（双向+因果）和三个自监督目标（掩码预测+对比学习+缺失片段生成），将纯解码器 LLM 同时增强为文本编码器和填充模型，在 token 级和句子级表示学习任务上超越 LLM2Vec 等专用方法，同时避免了双向化带来的严重文本重复问题。

**[Qaencoder Aligned Representation](qaencoder_aligned_representation.md)**

:   提出 QAEncoder，一种免训练方法通过蒙特卡洛采样估计文档对应查询的期望嵌入作为文档表示的代理，配合文档指纹保持区分性，在 BEIR 上将 bge-large 从 58.5 提升到 61.8 NDCG@10，零额外存储和延迟开销。

**[Shubert Self-Supervised Sign Language Representation Learning Via Multi-Stream C](shubert_self-supervised_sign_language_representation_learning_via_multi-stream_c.md)**

:   提出 SHuBERT（Sign Hidden-Unit BERT），将语音自监督学习模型 HuBERT 的 masked cluster prediction 范式迁移到手语视频——对手部、面部、身体姿态四个流分别聚类并同时预测 masked 帧的聚类标签，在约 984 小时 ASL 视频上预训练后，在翻译/孤立识别/指拼检测多任务上达到公开数据 SOTA。

**[Whispa Semantically And Psychologically Aligned Whisper With Self-Supervised Con](whispa_semantically_and_psychologically_aligned_whisper_with_self-supervised_con.md)**

:   提出 WhiSPA，通过对比学习将 Whisper 音频编码器的潜在空间与 SBERT 语义表征和心理学维度（情感、人格）对齐，消除语音处理中对额外文本 LM 的依赖，在心理学评估任务上误差降低 73-84%。
