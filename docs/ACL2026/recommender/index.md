---
title: >-
  ACL2026 推荐系统方向13篇论文解读
description: >-
  13篇ACL2026的推荐系统方向论文解读，涵盖个性化生成、推荐系统、对话系统、推理等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎁 推荐系统

**💬 ACL2026** · **13** 篇论文解读

📌 **同领域跨会议浏览：** [🔬 ICLR2026 (10)](../../ICLR2026/recommender/) · [🤖 AAAI2026 (26)](../../AAAI2026/recommender/) · [🧠 NeurIPS2025 (24)](../../NeurIPS2025/recommender/) · [🧪 ICML2025 (17)](../../ICML2025/recommender/) · [💬 ACL2025 (7)](../../ACL2025/recommender/) · [📷 CVPR2025 (1)](../../CVPR2025/recommender/)

🔥 **高频主题：** 个性化生成 ×4 · 推荐系统 ×4 · 对话系统 ×3 · 推理 ×2

**[Beyond Itinerary Planning: A Real-World Benchmark for Multi-Turn and Tool-Using Travel Tasks](beyond_itinerary_planning-a_real-world_benchmark_for_multi-turn_and_tool-using_t.md)**

:   提出 TravelBench，首个融合真实用户查询、隐式用户偏好、多轮交互、不可解任务识别和10种真实工具的旅行规划基准，通过沙箱环境实现可复现评估，揭示前沿模型在不同能力维度上表现不均衡。

**[Content Fuzzing for Escaping Information Cocoons on Social Media](content_fuzzing_for_escaping_information_cocoons_on_digital_social_media.md)**

:   提出 ContentFuzz，一个从内容创作者视角出发的置信度引导模糊测试框架，通过 LLM 改写帖子使其在保持人类解读含义不变的前提下改变机器推断的立场标签，从而突破社交媒体信息茧房。

**[Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](decisive_guiding_user_decisions_with_optimal_preference_elicitation_from_unstruc.md)**

:   提出 DECISIVE 交互式决策框架，通过从非结构化文档中提取客观选项评分矩阵，结合贝叶斯偏好推断自适应选择成对比较问题高效学习用户潜在偏好向量，在最小化用户交互负担的同时实现透明个性化推荐，决策准确率比强基线提升最高 20%。

**[From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](from_recall_to_forgetting_benchmarking_long-term_memory_for_personalized_agents.md)**

:   本文提出Memora基准和FAMA指标，将长期记忆评估从浅层事实检索扩展到跨越数周至数月的记忆整合与突变处理，揭示现有LLM和记忆agent在处理频繁知识更新时的系统性失败。

**[HARPO: Hierarchical Agentic Reasoning for User-Aligned Conversational Recommendation](harpo_hierarchical_agentic_reasoning_for_user-aligned_conversational_recommendat.md)**

:   提出 HARPO 框架，将对话推荐重新定义为以推荐质量为优化目标的结构化决策问题，通过层次化偏好学习、基于价值网络的树搜索推理、虚拟工具操作和多智能体精炼四大组件，在 ReDial、INSPIRED 和 MUSE 三个基准上显著超越现有方法。

**[HORIZON: A Benchmark for in-the-wild User Behaviour Modeling](horizon_a_benchmark_for_in-the-wild_user_behaviour_modeling.md)**

:   本文提出 HORIZON，首个全开源的大规模跨领域长期推荐基准，基于 Amazon Reviews 合并构建包含 54M 用户和 35M 商品的统一交互历史，设计了沿时间轴和用户维度解耦的四象限评估协议，揭示了 BERT4Rec 等模型在分布内表现强劲但在时序外推和未见用户场景下显著退化的现象，且 LLM 在用户行为建模上并未一致优于专用架构。

**[IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters](icebreaker_for_conversational_agents_breaking_the_first-message_barrier_with_per.md)**

:   本文提出 IceBreaker，通过两步"握手"——共鸣感知兴趣蒸馏捕获触发兴趣 + 交互导向启动语生成配合个性化偏好对齐——解决对话智能体的"首条消息壁垒"，在全球最大对话产品之一的 A/B 测试中提升用户活跃天数 +1.84‰ 和点击率 +94.25‰。

**[Learning to Retrieve User History and Generate User Profiles for Personalized Persuasiveness Prediction](learning_to_retrieve_user_history_and_generate_user_profiles_for_personalized_pe.md)**

:   本文提出 ReCAP 框架，通过可训练的查询生成器和用户画像生成器，从用户历史记录中检索与说服相关的信息并构建上下文感知的用户画像，显著提升个性化说服力预测的效果。

**[Personalized Benchmarking: Evaluating LLMs by Individual Preferences](personalized_benchmarking_evaluating_llms_by_individual_preferences.md)**

:   本文对 Chatbot Arena 的 115 名活跃用户进行个性化排名分析，发现 Bradley-Terry 个性化排名与全局排名的平均 Spearman 相关仅 ρ=0.04（57% 用户近零或负相关），证明聚合基准无法反映大多数用户的个体偏好，并通过话题+风格特征成功预测了用户特定的模型排名。

**[Scripts Through Time: A Survey of the Evolving Role of Transliteration in NLP](scripts_through_time_a_survey_of_the_evolving_role_of_transliteration_in_nlp.md)**

:   本文系统综述了音译（transliteration）在跨语言 NLP 中的演变角色，提出五大动机分类（命名实体/OOV处理、代码混合、跨文字相似性利用、英语中心迁移、统一预处理），比较了六种整合方式的优劣，并在现代 LLM 语境下讨论了音译是否仍然必要。

**[What Makes an Ideal Quote? Recommending "Unexpected yet Rational" Quotations via Novelty](what_makes_an_ideal_quote_recommending_34unexpected_yet_rational34_quotations_vi.md)**

:   NOVELQR 提出了一个新颖性驱动的引用推荐框架，通过生成式标签代理构建深层语义知识库实现语义理性检索，并用 token 级新颖性估计器缓解自回归续写偏差，在双语基准上显著提升推荐质量。

**[What Makes LLMs Effective Sequential Recommenders? A Study on Preference Intensity and Temporal Context](what_makes_llms_effective_sequential_recommenders_a_study_on_preference_intensit.md)**

:   本文揭示现有 LLM 推荐系统的二元偏好建模丢失了偏好强度和时间上下文两个关键信息，提出 RecPO 框架通过自适应奖励边际将这两个因素纳入偏好优化，在五个数据集上显著超越 S-DPO 等基线。

**[Where and What: Reasoning Dynamic and Implicit Preferences in Situated Conversational Recommendation](where_and_what_reasoning_dynamic_and_implicit_preferences_in_situated_conversati.md)**

:   SiPeR 通过场景转换估计（"Where"）和贝叶斯逆推理（"What"）两个机制，解决情景对话推荐中用户偏好随环境动态变化且常常隐式表达的挑战，在 SIMMC 2.1 和 SCREEN 上分别提升 10.9% 和 10.6%。
