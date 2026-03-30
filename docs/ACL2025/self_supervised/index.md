<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**💬 ACL2025** · 共 **4** 篇

**[Improving Low-Resource Morphological Inflection via Self-Supervised Objectives](improving_low-resource_morphological_inflection_via_self-supervised_objectives.md)**

:   系统探索 13 种自监督辅助目标（自编码、CMLM、T5-style 等）在极低资源形态变化任务中的效果，发现无标注数据极少时自编码最优，数据增多后字符级 MLM 更好，按形态素边界采样掩码是最有前景的方向。

**[Contrastive Learning on LLM Back Generation Treebank for Cross-domain Constituency Parsing](llm_back_gen_treebank.md)**

:   提出 LLM 反向生成方法自动构建跨领域成分句法树库——给定只有领域关键词叶节点的不完整句法树，用 LLM 填充缺失词汇生成完整的跨领域句法树库，结合 span 级对比学习预训练，在 MCTB 五个目标领域上达到跨领域成分句法分析 SOTA。

**[QAEncoder: Towards Aligned Representation Learning in Question Answering Systems](qaencoder_aligned_representation.md)**

:   提出 QAEncoder，一种免训练方法通过蒙特卡洛采样估计文档对应查询的期望嵌入作为文档表示的代理，配合文档指纹保持区分性，在 BEIR 上将 bge-large 从 58.5 提升到 61.8 NDCG@10，零额外存储和延迟开销。

**[WhiSPA: Semantically and Psychologically Aligned Whisper with Self-Supervised Contrastive and Student-Teacher Learning](whispa_semantically_and_psychologically_aligned_whisper_with_self-supervised_con.md)**

:   提出 WhiSPA，通过对比学习将 Whisper 音频编码器的潜在空间与 SBERT 语义表征和心理学维度（情感、人格）对齐，消除语音处理中对额外文本 LM 的依赖，在心理学评估任务上误差降低 73-84%。
