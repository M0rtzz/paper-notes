<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎁 推荐系统

**💬 ACL2025** · 共 **5** 篇

**[CoVE: Compressed Vocabulary Expansion Makes Better LLM-based Recommender Systems](cove_compressed_vocabulary_expansion_makes_better_llm-based_recommender_systems.md)**

:   提出 CoVE 框架，通过扩展 LLM 词表为每个物品分配唯一 token ID 和嵌入，将序列推荐任务转化为 next-token prediction，相比现有方法推荐准确率提升最高 62%，推理速度提升约 100 倍，并通过哈希嵌入压缩解决大规模场景的内存问题。

**[GRAM: Generative Recommendation via Semantic-aware Multi-granular Late Fusion](gram_generative_recommendation.md)**

:   提出 GRAM 生成式推荐模型，通过语义到词汇的翻译（将隐式物品关系编码到 LLM 词汇空间）和多粒度迟融合（分别编码不同粒度提示后在解码时融合），在四个基准上比八个 SOTA 方法在 Recall@5 上提升 11.5-16.0%。

**[KERL: Knowledge-Enhanced Personalized Recipe Recommendation using Large Language Models](kerl_knowledge-enhanced_personalized_recipe_recommendation_using_large_language_.md)**

:   提出 KERL 统一食品推荐系统，结合 FoodKG 知识图谱和 Phi-3-mini 多 LoRA 微调，实现个性化食谱推荐（F1=0.973）、食谱生成和微量营养素估算三个功能，大幅超越基线 LLM 和传统嵌入方法。

**[LOTUS: A Leaderboard for Detailed Image Captioning from Quality to Societal Bias and User Preferences](lotus_a_leaderboard_for_detailed_image_captioning_from_quality_to_societal_bias_.md)**

:   提出 LOTUS 排行榜，从描述质量（对齐性、描述性、语言复杂度）、副作用（幻觉、有害性）和社会偏见（性别、肤色）三个维度统一评估大型视觉语言模型的详细图像描述能力，并支持基于用户偏好的定制化评估。

**[MIRA: Empowering One-Touch AI Services on Smartphones with MLLM-based Instruction Recommendation](mira_empowering_one-touch_ai_services_on_smartphones_with_mllm-based_instruction.md)**

:   提出 MIRA 框架，通过结构化推理、模板增强推理和前缀树约束解码，让用户在智能手机上长按文本或图片即可获得上下文相关的 AI 服务指令推荐，在 7B 模型上超越 GPT-4V（F1: 0.9121 vs 0.879），token 使用量仅为 1/7。
