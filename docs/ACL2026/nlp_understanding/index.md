---
title: >-
  ACL2026 NLP理解方向 4篇论文解读
description: >-
  4篇ACL2026 NLP理解论文解读，主题涵盖：DiZiNER 模拟人类试标注流程：多个异构、提出 HCRE 模型，通过构建层次化关系树将跨文档、本文提供了时序问答（TQA）的全面综述等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📖 NLP理解

**💬 ACL2026** · **4** 篇论文解读

**[DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot NER](diziner_disagreement-guided_instruction_refinement_via_pilot_annotation_simulati.md)**

:   DiZiNER 模拟人类试标注流程：多个异构 LLM 独立标注同一文本，分析模型间分歧来迭代精炼任务指令，在 18 个 NER 基准中的 14 个上达到零样本 SOTA，平均 F1 提升 +8.0，且超越其监督模型 GPT-5 mini。

**[HCRE: LLM-based Hierarchical Classification for Cross-Document Relation Extraction](hcre_llm-based_hierarchical_classification_for_cross-document_relation_extractio.md)**

:   提出 HCRE 模型，通过构建层次化关系树将跨文档关系抽取从大规模关系集的直接分类转化为逐层层次化分类，并设计预测-验证推理策略缓解层间错误传播，在 CodRED 数据集上显著超越 SLM 和 LLM 基线。

**[It's High Time: A Survey of Temporal Question Answering](it39s_high_time_a_survey_of_temporal_question_answering.md)**

:   本文提供了时序问答（TQA）的全面综述，提出了基于语料时间性、问题时间性和模型时间能力三个维度的统一分析框架，系统梳理了从规则管道到 Transformer/LLM 时代的 TQA 方法演进、基准数据集和评估策略，并识别了未来挑战。

**[Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models](lost_in_the_prompt_order_revealing_the_limitations_of_causal_attention_in_langua.md)**

:   本文深入研究了大语言模型在多选题问答中对提示组件顺序的敏感性，通过系统性实验排除了训练偏差和记忆衰退假说，揭示了因果注意力掩码是导致 QOC（问题-选项-上下文）顺序性能大幅下降的根本机制。
