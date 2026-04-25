---
title: >-
  ACL2026 多语言/翻译方向 18篇论文解读
description: >-
  18篇ACL2026 多语言/翻译论文解读，主题涵盖：构建首个多语言MRE Mix数据集（MMM、Alexandria 构建了覆盖 13、构建非字面翻译元评估数据集 MENT（7,530等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🌐 多语言/翻译

**💬 ACL2026** · **18** 篇论文解读

**[A Multilingual Dataset and Empirical Validation for the Mutual Reinforcement Effect in Information Extraction](a_multilingual_dataset_and_empirical_validation_for_the_mutual_reinforcement_eff.md)**

:   构建首个多语言MRE Mix数据集（MMM，21个子集覆盖英中日），并通过大规模消融实验系统验证了词级与文本级信息抽取任务的互增强效应（MRE）跨语言普遍存在。

**[Alexandria: A Multi-Domain Dialectal Arabic Machine Translation Dataset for Culturally Inclusive and Linguistically Diverse LLMs](alexandria_a_multi-domain_dialectal_arabic_machine_translation_dataset_for_cultu.md)**

:   Alexandria 构建了覆盖 13 个阿拉伯国家、11 个社会影响领域、107K 轮次的多轮对话方言阿拉伯语-英语平行数据集，通过社区驱动的人工翻译与修订流程，为方言阿拉伯语机器翻译提供了前所未有的细粒度训练和评测资源，并在 24 个 LLM 上进行了系统性基准评估。

**[Beyond Literal Mapping: Benchmarking and Improving Non-Literal Translation Evaluation](beyond_literal_mapping_benchmarking_and_improving_non-literal_translation_evalua.md)**

:   构建非字面翻译元评估数据集 MENT（7,530 条人工标注），揭示传统指标和 LLM-as-Judge 在非字面翻译评估上的不可靠性，并提出 RATE 智能体评估框架，通过反思核心智能体动态调用子智能体，提升 3.2+ 点人类判断相关性。

**[BhashaSutra: A Task-Centric Unified Survey of Indian NLP Datasets, Corpora, and Resources](bhashasutra_a_task-centric_unified_survey_of_indian_nlp_datasets_corpora_and_res.md)**

:   首篇专门针对印度语言NLP资源的统一综述，覆盖200+数据集、50+基准、100+模型/工具，按17个任务类别组织（从核心语言处理到社会文化任务），系统分析了语言覆盖不均、标注碎片化、评估不一致等持续挑战。

**[Efficient Training for Cross-lingual Speech Language Models](efficient_training_for_cross-lingual_speech_language_models.md)**

:   本文提出CSLM，一种高效训练跨语言语音LLM的方法，通过新颖的对齐策略实现跨模态和跨语言对齐，并引入语音-文本交织链式模态生成来提升质量和降低延迟，无需大规模语音数据即可扩展到新语言。

**[Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models](exploring_continual_fine-tuning_for_enhancing_language_ability_in_large_language.md)**

:   本文提出两阶段持续微调（CFT）框架——先在英语指令数据上微调，再在多语言数据上微调——发现阶段间数据集的指令相似性是决定英语能力是否退化的关键因素，并通过生成式重放和启发式层冻结有效缓解了不相似数据集导致的表示漂移和英语遗忘。

**[Just Use XML: Revisiting Joint Translation and Label Projection](just_use_xml_revisiting_joint_translation_and_label_projection.md)**

:   提出 LabelPigeon，一种基于 XML 标签的联合翻译与标签投影方法，通过在高质量 XML 标记平行语料上微调 NLLB-200 翻译模型，在 11 种语言上超越所有基线并主动提升翻译质量，在下游跨语言 NER 任务中实现最高 +40.2 F1 的提升。

**[Language Models Entangle Language and Culture](language_models_entangle_language_and_culture.md)**

:   本文通过基于 WildChat 数据集构建的通用建议类问题评估多语言 LLM，发现不同语言查询会导致回答质量和文化上下文的系统性差异——低资源语言的回答质量显著低于英语，且语言选择会隐式地改变回答中使用的文化信息，在翻译版 CulturalBench 上验证了语言与文化在 LLM 中的纠缠关系。

**[Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs](location_not_found_exposing_implicit_local_and_global_biases_in_multilingual_llm.md)**

:   本文提出 LocQA 基准（12 种语言、49 个地区、2156 个地域相关问答），通过地域模糊问题（如"紧急电话号码是多少？"）揭示 LLM 的隐式偏差：跨语言上存在持续的美国中心默认行为（模型回答的 50% 包含美国答案 vs 数据中仅 26%），语言内部存在人口规模驱动的"人口概率引擎"效应，且指令微调加剧了全球偏差。

**[Lost in Translation: Do LVLM Judges Generalize Across Languages?](lost_in_translation_do_lvlm_judges_generalize_across_languages.md)**

:   本文提出 MM-JudgeBench，首个大规模多语言多模态评判模型基准（25 种语言、60K+ 偏好实例），评估 22 个 LVLM 发现当前 LVLM 评判器存在显著的跨语言性能差异——模型大小和架构不能预测多语言鲁棒性，即使最先进的评判器也表现不一致，突显了多语言多模态评估基准的必要性。

**[Mitigating Extrinsic Gender Bias for Bangla Classification Tasks](mitigating_extrinsic_gender_bias_for_bangla_classification_tasks.md)**

:   针对孟加拉语预训练模型在下游分类任务中的外在性别偏见，提出 RandSymKL 方法，通过随机化交叉熵损失和对称 KL 散度联合优化，在保持分类准确率的同时有效缩小性别间预测差异。

**[MORPHOGEN: A Multilingual Benchmark for Evaluating Gender-Aware Morphological Generation](morphogen_a_multilingual_benchmark_for_evaluating_gender-aware_morphological_gen.md)**

:   本文提出 MORPHOGEN，一个涵盖法语/阿拉伯语/印地语的大规模性别感知形态学生成基准（共 20,328 句对），定义了 GENFORM 任务（将第一人称句子改写为相反性别），并提出 SGA/GIoU/CGA 三个评估指标，对 15 个多语言 LLM 的基准测试揭示了模型在复杂形态推理、性别偏差和多实体干扰方面的系统性不足。

**[No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs](no_one_fits_all_from_fixed_prompting_to_learned_routing_in_multilingual_llms.md)**

:   本文证明没有一种提示策略在所有语言和任务上普遍最优，提出将策略选择建模为学习决策问题，用轻量级分类器为每个实例预测最优策略，在四个基准上显著优于固定策略。

**[Prosody as Supervision: Bridging the Non-Verbal–Verbal for Multilingual Speech Emotion Recognition](prosody_as_supervision_bridging_the_non-verbal--verbal_for_multilingual_speech_e.md)**

:   本文提出 NOVA-ARC，首次将多语言语音情感识别（SER）建模为从标注的非语言发声（NVV）到未标注的语言语音（UVS）的无监督迁移问题，通过双曲空间中的韵律向量量化编码本、双曲情感透镜和最优传输原型对齐实现跨模态情感迁移，在 6 个数据集上验证了非语言→语言迁移的可行性和优越性。

**[SERM: Self-Evolving Relevance Model with Agent-Driven Learning from Massive Query Streams](serm_self-evolving_relevance_model_with_agent-driven_learning_from_massive_query.md)**

:   提出 SERM 框架，通过多智能体样本挖掘器和多智能体相关性标注器，从大规模真实查询流中持续自进化搜索相关性模型，经三轮迭代在工业搜索平台上实现 NDCG@1 提升 +2.99，并在在线 A/B 测试中显著提升用户留存率。

**[Syntax as a Rosetta Stone: Universal Dependencies for In-Context Coptic Translation](syntax_as_a_rosetta_stone_universal_dependencies_for_in-context_coptic_translati.md)**

:   本文首次探索将 Universal Dependencies 句法信息作为上下文学习的增强源用于低资源科普特语到英语的机器翻译，发现虽然句法信息单独不如词典有效，但将词典与句法信息结合（LEX+SYN）在所有模型上取得最佳效果，Gemma-27B 的 BERTScore F1 达到 0.8746（+0.0361）。

**[Unlocking the Edge: Multi-LoRA On-Device Deployment and Acceleration](unlocking_the_edge_deployment_and_ondevice_acceleration_of_multi-lora_enabled_on.md)**

:   本文提出面向三星 Galaxy S24/S25 的端侧 LLM 部署框架，通过 LoRA 权重作为运行时输入实现动态任务切换、多流并发 token 生成减少风格变体延迟达 6 倍、无草稿模型的 Dynamic Self-Speculative Decoding 加速解码达 2.3 倍，在 9 语言 8 任务上实现 4-6 倍整体优化。

**[What Factors Affect LLMs and RLLMs in Financial Question Answering?](what_factors_affect_llms_and_rllms_in_financial_question_answering.md)**

:   本文系统研究了提示方法、Agent 框架和多语言对齐方法对 LLM 和 RLLM（推理型大模型）在金融问答任务上的影响，发现现有方法本质上是通过模拟 Long CoT 来提升 LLM 性能，但对已具备 Long CoT 能力的 RLLM 效果有限。
