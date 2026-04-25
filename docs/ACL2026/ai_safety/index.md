---
title: >-
  ACL2026 AI安全方向 10篇论文解读
description: >-
  10篇ACL2026 AI安全论文解读，主题涵盖：提出自适应文本匿名化框架，通过进化式提示优化自动为、提出 ChainFed，一种打破内存墙的链式联邦微、本文提出 DAS（De-Anonymization等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI安全

**💬 ACL2026** · **10** 篇论文解读

**[Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization](adaptive_text_anonymization_learning_privacy-utility_trade-offs_via_prompt_optim.md)**

:   提出自适应文本匿名化框架，通过进化式提示优化自动为LLM发现任务特定的匿名化指令，在多个隐私-效用权衡场景中超越手工设计的策略，且可在开源模型上运行。

**[Beyond End-to-End: Dynamic Chain Optimization for Private LLM Adaptation on the Edge](beyond_end-to-end_dynamic_chain_optimization_for_private_llm_adaptation_on_the_e.md)**

:   提出 ChainFed，一种打破内存墙的链式联邦微调范式，通过逐层顺序训练-冻结适配器使资源受限边缘设备也能参与 LLM 微调，结合动态层协调、全局感知优化和功能导向自适应三项技术，平均准确率提升最高 46.46%。

**[De-Anonymization at Scale via Tournament-Style Attribution](de-anonymization_at_scale_via_tournament-style_attribution.md)**

:   本文提出 DAS（De-Anonymization at Scale），一种基于 LLM 的大规模作者去匿名化方法，采用锦标赛式淘汰策略+密集检索预过滤+多轮投票聚合，可在数万候选文本中进行作者匹配，揭示了 LLM 对匿名平台（如双盲评审）的隐私威胁。

**[ForgeryTalker: Generating Attribution Reports for Manipulated Facial Images](generating_attribution_reports_for_manipulated_facial_images_a_dataset_and_basel.md)**

:   本文提出伪造归因报告生成（Forgery Attribution Report Generation）这一新任务，构建了包含 152,217 个样本的 MMTT 数据集（首个同时提供像素级掩码和人工文本描述的大规模面部伪造数据集），并提出 ForgeryTalker 端到端基线，通过共享编码器和双解码器（掩码+语言模型）联合生成定位掩码和归因报告，达到 59.3 CIDEr 和 73.67 IoU。

**[Indic-CodecFake meets SATYAM: Towards Detecting Neural Audio Codec Synthesized Speech Deepfakes in Indic Languages](indic-codecfake_meets_satyam_towards_detecting_neural_audio_codec_synthesized_sp.md)**

:   本文构建了首个多印度语言的 CodecFake 检测基准 ICF，并提出 SATYAM——一个双曲音频大语言模型，通过在双曲空间中用 Bhattacharyya 距离对齐语义和副语言表示再与提示对齐，仅训练 3.75M 参数即达到 98.32% 的检测准确率。

**[Jailbreaking Large Language Models with Morality Attacks](jailbreaking_large_language_models_with_morality_attacks.md)**

:   本文构建10.3K道德攻击数据集（价值模糊+价值冲突），通过四种对抗策略操纵LLM道德判断，发现LLM和guardrail模型对道德攻击极度脆弱，且更大模型反而更容易被攻破。

**[Synthia: Scalable Grounded Persona Generation from Social Media Data](synthia_scalable_grounded_persona_generation_from_social_media_data.md)**

:   提出 Synthia 框架，基于真实社交媒体帖子（Bluesky）生成有根据的 LLM 人格叙事，在社会调查对齐度上比 SOTA 提升最高 11.6%，同时使用更小的模型，并保留社交网络拓扑结构支持网络感知分析。

**[Topic-Based Watermarks for Large Language Models](topic-based_watermarks_for_large_language_models.md)**

:   本文提出基于主题的轻量水印方案 TBW，将词表按语义主题聚类为"绿色列表"（而非随机分区），根据输入提示选择语义对齐的主题列表进行 logit 偏置，在保持与无水印文本相当的困惑度的同时，显著提升了对释义和词汇扰动攻击的鲁棒性。

**[When Bigger Isn't Better: A Comprehensive Fairness Evaluation of Political Bias in Multi-News Summarisation](when_bigger_isn39t_better_a_comprehensive_fairness_evaluation_of_political_bias_.md)**

:   本文构建了首个带政治倾向标签的多文档新闻摘要数据集 FairNews，并通过五维公平性评估框架对 13 个 LLM 进行评估，发现中等规模模型在公平性和效率上优于大模型，且实体情感相似性是最难通过提示去偏的维度。

**[XQ-MEval: A Dataset with Cross-lingual Parallel Quality for Benchmarking Translation Metrics](xq-meval_a_dataset_with_cross-lingual_parallel_quality_for_benchmarking_translat.md)**

:   构建首个具有跨语言平行质量的翻译评估基准 XQ-MEval，通过半自动注入 MQM 错误生成可控质量的伪翻译，首次实证揭示自动评估指标的跨语言评分偏差，并提出 LGN 归一化策略有效校准多语言指标评估。
