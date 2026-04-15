---
title: >-
  ACL2025 对话系统方向 10篇论文解读
description: >-
  10篇ACL2025 对话系统方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🗣️ 对话系统

**💬 ACL2025** · 共 **10** 篇

**[Dialogue Systems For Emotional Support Via Value Reinforcement](dialogue_systems_for_emotional_support_via_value_reinforcement.md)**

:   提出 ES-VR，首个将人类价值观强化融入情感支持对话系统的方法，通过目标价值检测器和参考生成器（均在 Reddit 数据上训练），结合 SFT + DPO 两阶段训练，使支持者模型不仅能缓解求助者的负面情绪，还能探索和强化其积极价值观，实现更深层的内在转变。

**[Enabling Chatbots With Eyes And Ears An Immersive Multimodal Conversation System](enabling_chatbots_with_eyes_and_ears_an_immersive_multimodal_conversation_system.md)**

:   本文提出赋予聊天机器人"眼睛和耳朵"的沉浸式多模态对话系统，构建了融合视觉与听觉的多会话多方对话数据集 M3C，并设计了包含对话模块和多模态记忆检索模块的对话模型，实现了多说话者共享视听体验的动态长期对话。

**[Enstom Enhancing Dialogue Systems With Entropy-Scaled Steering Vectors For Topic](enstom_enhancing_dialogue_systems_with_entropy-scaled_steering_vectors_for_topic.md)**

:   提出 EnSToM，一种基于熵缩放转向向量的轻量级方法，通过利用 LLM 内部层级熵分布差异来动态调整转向强度，在不修改模型参数的情况下提升任务导向对话系统的主题维持能力。

**[Know You First And Be You Better Modeling Human-Like User Simulators Via Implici](know_you_first_and_be_you_better_modeling_human-like_user_simulators_via_implici.md)**

:   本文提出 USP（User Simulator with Implicit Profiles）框架，通过从人机对话中提取隐式用户画像，并结合条件监督微调和基于循环一致性的强化学习，在真实性、一致性和多样性三个维度上显著超越基线方法，语义相似度和风格相似度分别提升约 34% 和 43%。

**[Know Your Mistakes Towards Preventing Overreliance On Task-Oriented Conversation](know_your_mistakes_towards_preventing_overreliance_on_task-oriented_conversation.md)**

:   本文提出面向任务型对话系统的 Accountability Model，在 LLM 中加入额外的 accountability head 作为二分类器预测对话状态中各 slot 的概率，从而检测并自校正假阳性和假阴性错误，在 MultiWOZ 上将 JGA 从 64.34 提升到 70.51（↑9.6%），达到 SOTA。

**[Kokorochat A Japanese Psychological Counseling Dialogue](kokorochat_a_japanese_psychological_counseling_dialogue.md)**

:   提出 KokoroChat，一个通过训练有素的咨询师角色扮演收集的日语心理咨询对话数据集，包含 6,589 段长对话及详细的客户反馈评分，用于提升 LLM 的心理咨询回复生成和对话评估能力。

**[Persona Sentiment Dialogue](persona_sentiment_dialogue.md)**

:   大规模分析发现 LLM 生成的个性化对话质量对人物画像的情感极性高度敏感——负面画像导致过度强调人设引发矛盾，正面画像则选择性融入人设产生更高质量对话——基于此提出结合轮次生成、画像排序和情感感知提示的改进方法。

**[Personalens A Benchmark For Personalization Evaluation In Conversational Ai Assi](personalens_a_benchmark_for_personalization_evaluation_in_conversational_ai_assi.md)**

:   提出 PersonaLens，一个面向任务导向型 AI 助手个性化能力的综合评测基准，包含 1500 个丰富用户画像、20 个领域 111 个任务、用户模拟 Agent 和 Judge Agent，通过大规模自动化评估揭示当前 LLM 助手在个性化方面的显著不足。

**[Reflectdiffu Empathetic Response](reflectdiffu_empathetic_response.md)**

:   提出轻量级共情对话框架 ReflectDiffu，融合情感传染（捕捉情绪）、意图二次机制（Exploring-Sampling-Correcting将情绪映射为行动意图）和扩散模型生成，在相关性、可控性和信息量上全面超越现有基线和 Llama-3.1-8B。

**[Uniconv Retrieval Response Gen](uniconv_retrieval_response_gen.md)**

:   探索如何将对话场景中的稠密检索和响应生成统一到单个 LLM 中，通过三个联合训练目标（对话检索 + 响应生成 + 上下文识别指令）和数据差异缓解机制，在五个对话搜索数据集上实现检索和生成的相互促进，超越分离式基线。
