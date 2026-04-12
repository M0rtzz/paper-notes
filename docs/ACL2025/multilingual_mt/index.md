---
title: >-
  ACL2025 多语言/翻译方向 73篇论文解读
description: >-
  73篇ACL2025 多语言/翻译方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🌐 多语言/翻译

**💬 ACL2025** · 共 **73** 篇

**[A Case Study Of Cross-Lingual Zero-Shot Generalization For Classical Languages I](a_case_study_of_cross-lingual_zero-shot_generalization_for_classical_languages_i.md)**

:   系统评估 LLM（GPT-4o/Llama-3.1）在三种古典语言（梵语、拉丁语、古希腊语）上的零样本跨语言泛化能力——涵盖 NER、机器翻译、问答三个 NLU 任务，发现大模型在域外数据上可比肩甚至超越微调基线，模型规模是决定性因素，并贡献了一个 1501 对的梵语事实问答数据集。

**[Alleviating Distribution Shift In Synthetic Data For Machine Translation Quality](alleviating_distribution_shift_in_synthetic_data_for_machine_translation_quality.md)**

:   提出 DCSQE 框架，通过约束波束搜索生成更真实的合成翻译、利用独立的标注模型纠正标签偏差、以及 SPCE 算法将 token 级标签聚合为短语级标签，有效缓解合成 QE 数据的分布偏移问题，在有监督和无监督设置下均超越 CometKiwi 等 SOTA 基线。

**[An Expanded Massive Multilingual Dataset For High-Performance Language Technolog](an_expanded_massive_multilingual_dataset_for_high-performance_language_technolog.md)**

:   本文介绍 HPLT v2，一个从 4.5 PB 的 Internet Archive 和 Common Crawl 数据中提取的大规模多语言数据集，包含覆盖 193 种语言的 8 万亿 token 单语数据和覆盖 51 种语言的 3.8 亿句对平行数据，并通过改进的数据处理管线显著提升了数据质量。

**[Are Rules Meant To Be Broken Understanding Multilingual Moral Reasoning As A Com](are_rules_meant_to_be_broken_understanding_multilingual_moral_reasoning_as_a_com.md)**

:   提出UniMoral——一个跨6种语言的统一道德推理数据集，将道德推理建模为包含行为预测、道德类型分类、因素归因和后果生成的计算流水线，对3个LLM的基准测试揭示隐式道德语境能增强模型道德推理能力但仍需专门化方法。

**[Askqe Question Answering As Automatic Evaluation For Machine Translation](askqe_question_answering_as_automatic_evaluation_for_machine_translation.md)**

:   提出 AskQE——基于问答的机器翻译质量估计框架，通过对源文本生成问题、分别在源文本和回译输出上回答、对比答案差异来检测翻译错误，帮助不懂目标语言的用户判断翻译是否可接受，在 BioMQM 数据集上 Kendall's τ 相关和决策准确率均优于现有 QE 指标。

**[Assessing Agentic Large Language Models In Multilingual National Bias](assessing_agentic_large_language_models_in_multilingual_national_bias.md)**

:   首次研究 LLM 作为推理型 Agent 在多语言场景下的国籍偏见——在大学申请/旅行/搬迁三个决策场景中，让 GPT-3.5/GPT-4/Sonnet 对同一实体（大学/城市）用不同语言打分，发现普遍存在"本地语言偏向"（用中文问清华得 10 分，用英文问只得 7 分），GPT-4 在英语上偏见减少但非英语上偏见显著，CoT 不一定缓解反而可能放大偏差。

**[Beyond N-Grams Rethinking Evaluation Metrics And Strategies For Multilingual Abs](beyond_n-grams_rethinking_evaluation_metrics_and_strategies_for_multilingual_abs.md)**

:   系统评估了 n-gram 和神经指标在 8 种语言（4 种类型学家族）上与人工判断的相关性，发现 n-gram 指标在融合语言中可靠性差，而专门训练的神经指标 COMET 在所有语言上一致优于其他指标；还发现分词策略可以显著改善融合语言的评估效果。

**[Blessing Of Multilinguality A Systematic Analysis Of Multilingual In-Context Lea](blessing_of_multilinguality_a_systematic_analysis_of_multilingual_in-context_lea.md)**

:   系统分析多语言 ICL 策略，发现在 prompt 中混合多种高资源语言（HRL）的 demonstrations 一致性优于纯英文 demonstrations，尤其在低资源语言（LRL）上提升显著（Llama3.1 上 LRL 平均准确率提升 8.9~12.6%），甚至仅在 prompt 中加入不相关的非英语句子也能带来可测量的增益，揭示了"多语言暴露本身即有效"的现象。

**[Cchall A Novel Benchmark For Joint Cross-Lingual And Cross-Modal Hallucinations ](cchall_a_novel_benchmark_for_joint_cross-lingual_and_cross-modal_hallucinations_.md)**

:   提出首个**联合跨语言与跨模态**幻觉检测基准 CCHall，覆盖 9 种语言和 4 类多模态数据集，系统评估 6 款主流 MLLM 在联合场景下的幻觉表现，揭示当前模型在该联合场景中 F1 比单独跨模态低 10.9、比单独跨语言低 3.4，且提出多语提示和外部工具辅助两条缓解路径。

**[Clix Cross-Lingual Explanations Of Idiomatic Expressions](clix_cross-lingual_explanations_of_idiomatic_expressions.md)**

:   提出跨语言习语解释任务 CLIX，构建了包含英语习语及其西班牙语/德语解释的数据集，系统评估了 seq2seq 模型和 LLM 在该任务上的表现，发现 GPT-3.5 Turbo 的 pipeline 策略（先英文解释再翻译）配合 few-shot 效果最佳，人工评估流畅度和准确度高达 4.7+/5。

**[Cosmmic Commentsensitive Multimodal Multilingual Indian Corpus](cosmmic_commentsensitive_multimodal_multilingual_indian_corpus.md)**

:   构建首个面向印度语言的评论感知多模态多语言数据集 COSMMIC（9 种语言、4,959 篇文章-图像对、24,484 条读者评论），提出评论过滤（IndicBERT）和图像分类（CLIP）增强方案，用 GPT-4 和 LLama3 建立摘要和标题生成的基准。

**[Cross-Lingual Auto Evaluation For Assessing Multilingual Llms](cross-lingual_auto_evaluation_for_assessing_multilingual_llms.md)**

:   提出 CIA (Cross Lingual Auto Evaluation) Suite，一个跨语言 LLM 评估框架，包含评估模型 Hercule 和人工标注测试集 Recon，通过利用英语参考答案对非英语语言的 LLM 响应进行评分，8B 模型在多语言评估上超越了 GPT-4o 等闭源大模型。

**[Cross-Lingual Optimization For Language Transfer In Large Language Models](cross-lingual_optimization_for_language_transfer_in_large_language_models.md)**

:   提出 Cross-Lingual Optimization (CLO)，通过修改 DPO 损失函数实现跨语言偏好优化——给目标语言输入时偏好目标语言回复、给英语输入时偏好英语回复——在 5 个模型 × 6 种语言上一致超越 SFT，低资源语言中仅 3,200 样本的 CLO 即超越 6,400 样本的 SFT。

**[Cross-Lingual Representation Alignment Through Contrastive Image-Caption Tuning](cross-lingual_representation_alignment_through_contrastive_image-caption_tuning.md)**

:   探索了一种无需平行语料的跨语言表示对齐方法——通过多语言图像-文本描述的对比学习（类 CLIP），让不同语言的文本表示在共享视觉空间中隐式对齐，并证明即使是编码器预训练中未见过的语言（如 Quechua）也能通过这种方式被纳入对齐体系。

**[Cross-Lingual Transfer Of Cultural Knowledge An Asymmetric Phenomenon](cross-lingual_transfer_of_cultural_knowledge_an_asymmetric_phenomenon.md)**

:   通过构建可解释的实验框架，研究 LLM 语言适应过程中文化知识的跨语言迁移现象，发现高资源语言（中文、韩语）与英语之间存在双向迁移，而低资源语言（藏语、蒙古语）则呈现不对称迁移——知识主要从低资源语言流向英语，反向流动有限，并提出频率假说加以解释。

**[Cross-Lingual Transfer Of Debiasing And Detoxification In Multilingual Llms An E](cross-lingual_transfer_of_debiasing_and_detoxification_in_multilingual_llms_an_e.md)**

:   在 7 个 LLM 和 20 种语言上系统研究了英语去偏见/去毒化微调的跨语言迁移效果，发现 SFT 有效去偏见、DPO 有效去毒化，但迁移到非英语语言时普遍伴随语言生成能力下降（语言一致性、流畅度、多样性均受损），迁移效果可由预训练数据中目标语言的数据量预测。

**[Cross Lingual Neurons Compression](cross_lingual_neurons_compression.md)**

:   本文通过追踪多语言语言模型预训练过程中的检查点，发现模型从语言特定表示逐渐压缩为跨语言共享表示：中间层的语言识别能力下降、语义概念的"专家神经元"跨语言对齐，操控从西班牙语数据提取的概念神经元后模型反而生成语义相关的英语文本。

**[Crosslingual Pitfalls](crosslingual_pitfalls.md)**

:   提出基于束搜索和 LLM 仿真的自动化方法来高效发现多语言 LLM 的跨语言弱点，构建了覆盖 16 种语言的 6000+ 双语问答对数据集，揭示即使 GPT-4o 也存在超过 30% 的跨语言性能下降。

**[Cruxeval-X A Benchmark For Multilingual Code Reasoning Understanding And Executi](cruxeval-x_a_benchmark_for_multilingual_code_reasoning_understanding_and_executi.md)**

:   提出 CruxEval-X，一个覆盖 19 种编程语言的多语言代码推理基准，通过全自动的测试引导翻译流水线从 Python 版 CruxEval 扩展而来，包含 12,660 个题目和 19K 测试用例，对 24 个 LLM 的评估揭示了编程语言间的相关性以及单语言训练模型的跨语言泛化能力。

**[Dictionaries To The Rescue Cross-Lingual Vocabulary Transfer For Low-Resource La](dictionaries_to_the_rescue_cross-lingual_vocabulary_transfer_for_low-resource_la.md)**

:   本文提出一种基于双语词典的跨语言词汇迁移方法，利用BPE分词器"删除子词后回退到更短子词"的特性，通过迭代删除-重分词-对齐的过程最大化目标语言子词的映射覆盖率，在低资源语言上显著优于依赖单语语料或平行语料的现有方法。

**[Disentangle Language Culture](disentangle_language_culture.md)**

:   提出 Dual Evaluation Framework，将多语言 LLM 评估沿"语言媒介"和"文化语境"两个维度解耦，发现"文化-语言协同"(Cultural-Linguistic Synergy) 现象——模型在文化语境与提问语言对齐时表现更好，并通过 FFN 神经元激活分析从可解释性角度给出解释。

**[Edit Once, Update Everywhere: Cross-Lingual Knowledge Synchronization](edit_once_update_everywhere_a_simple_framework_for_cross-lingual_knowledge_synch.md)**

:   提出 X-KDE 框架通过指令微调+偏好优化实现知识的跨语言同步编辑——在一种语言中编辑知识后自动在其他语言同步生效。

**[Execute A Multilingual Benchmark For Llm Token Understanding](execute_a_multilingual_benchmark_for_llm_token_understanding.md)**

:   扩展字符理解基准 CUTE 到 8 种语言和多种文字系统，提出 EXECUTE 框架，发现 LLM 在不同语言的字符/词/子字符级别表现差异巨大，且意外发现 LLM 对越不熟悉的语言反而在 token 理解任务上表现越好。

**[Exploring In-Context Example Generation For Machine Translation](exploring_in-context_example_generation_for_machine_translation.md)**

:   提出DAT(Demonstration Augmentation for Translation)——在**无需任何外部资源**的情况下，让LLM自动生成与用户查询相关且多样的源-目标句对作为in-context示例，在5个低资源语言翻译任务上超越zero-shot和固定示例的few-shot基线。

**[Exploring In-Image Machine Translation With Real-World Background](exploring_in-image_machine_translation_with_real-world_background.md)**

:   提出 DebackX 模型，通过将图像分离为背景和文字图像分别处理，首次解决了真实复杂背景下的图像内机器翻译 (IIMT) 任务，在翻译质量和视觉效果上均优于现有方法。

**[Flare Crosslingual Lora](flare_crosslingual_lora.md)**

:   FLARE 在 LoRA 适配器的低秩瓶颈中通过轻量线性/非线性变换融合源语言（英语）和目标语言的逐层表示，无需额外参数即可实现参数高效的跨语言迁移，在 Llama 3.1 上 QA 精确匹配提升 4.9%。

**[Grammamt Improving Machine Translation With Grammar-Informed In-Context Learning](grammamt_improving_machine_translation_with_grammar-informed_in-context_learning.md)**

:   提出 GrammaMT，利用语素间注释文本 (Interlinear Glossed Text, IGT) 的语法信息来增强 LLM 的 few-shot 机器翻译，在濒危语言上平均提升 12+ BLEU，在中高资源语言上也有一致改进。

**[Group Then Scale Dynamic Mixture-Of-Experts Multilingual Language Model](group_then_scale_dynamic_mixture-of-experts_multilingual_language_model.md)**

:   提出 DMoE——基于参数偏差的动态语言分组 + 选择性 MoE 层扩展方法，通过仅 10 步微调量化语言间相似性，将相似语言分组共享同一 expert，只在参数偏差大的层（语言特定层）扩展为 MoE 层，在 18~128 种语言上 PPL 比持续预训练降低 11.4%，用 3.6 倍少的参数超越 X-ELM 9.6%。

**[Hierarchical News Clustering](hierarchical_news_clustering.md)**

:   本文提出利用多语言 Matryoshka 嵌入的分层特性进行新闻文章聚类：低维捕捉主题级相似度、中维捕捉叙事级相似度、高维捕捉事件级相似度，结合改良的 RAC 层级聚类算法，在 SemEval 2022 Task 8 上达到 SOTA（Pearson ρ = 0.816）。

**[Just Go Parallel Improving The Multilingual Capabilities Of Large Language Model](just_go_parallel_improving_the_multilingual_capabilities_of_large_language_model.md)**

:   系统研究在 decoder-only LLM 训练中加入平行数据对多语言能力的影响，发现将平行数据放在训练末期效果最好，且平行数据显著优于等量的单语数据；LLM 无法自动泛化到训练方向的反向翻译。

**[Knowcoder-X Boosting Multilingual Information Extraction Via Code](knowcoder-x_boosting_multilingual_information_extraction_via_code.md)**

:   提出 KnowCoder-X，通过统一的 Python 类表示多语言 IE schema，并引入 IE 跨语言对齐指令微调阶段（含高质量 ParallelNER 数据集），在 64 个 IE 基准上大幅提升跨语言信息抽取性能。

**[Laca Crosslingual Absa](laca_crosslingual_absa.md)**

:   提出 LACA 框架，利用 LLM 为目标语言生成高质量伪标注数据（而非依赖机器翻译），在六种语言上显著提升跨语言 ABSA 性能，在 mBERT 和 XLM-R 上分别平均超过前 SOTA 1.50% 和 2.62%。

**[Langmark A Multilingual Dataset For Automatic Post-Editing](langmark_a_multilingual_dataset_for_automatic_post-editing.md)**

:   发布 LangMark——一个包含 206,983 个三元组、覆盖英语到七种语言的大规模多语言自动后编辑（APE）数据集，并证明 LLM 配合 few-shot prompting 能有效改善专有 NMT 引擎的输出质量。

**[Langsamp Multilingual Pretraining](langsamp_multilingual_pretraining.md)**

:   提出 LangSAMP 方法，在多语言预训练中将语言和文字系统 (script) embedding 添加到 Transformer 输出端（而非输入端），使模型主干学到更语言中立的表示，在 500+ 语言的零样本跨语言迁移中一致优于基线。

**[Lemonade A Large Multilingual Expert-Annotated Abstractive Event Dataset For The](lemonade_a_large_multilingual_expert-annotated_abstractive_event_dataset_for_the.md)**

:   发布 Lemonade——基于 ACLED 冲突数据的大规模多语言专家标注事件数据集（39,786 事件，20 种语言，171 个国家，10,707 实体），提出 Abstractive Event Extraction (AEE) 新任务范式，事件参数不限于文本 span 而是归一化为数值/类别/实体，配套 Zest 零样本实体链接系统在 AEL 子任务上 F1=45.7% 大幅超越 baseline 的 23.7%。

**[Less But Better Efficient Multilingual Expansion](less_but_better_efficient_multilingual_expansion.md)**

:   分析 LLM 不同层间的跨语言表征相似度，提出 LayerMoE 按层分配不同数量的新语言专家（高相似层少分配、低相似层多分配），用 60% 更少的专家参数超越 SOTA，并通过在高相似层添加路由分类器进一步缓解灾难性遗忘。

**[Lost In Multilinguality Dissecting Cross-Lingual Factual Inconsistency In Transf](lost_in_multilinguality_dissecting_cross-lingual_factual_inconsistency_in_transf.md)**

:   用机制可解释性方法解剖多语言 LLM 的跨语言事实不一致问题，发现模型在大多数层中以语言无关的概念空间处理知识，但在最后几层的"语言转换"过程中失败导致不一致，提出线性快捷方法绕过最后层以提升一致性和准确率。

**[Low Resource Translation](low_resource_translation.md)**

:   将语法书辅助的极低资源翻译（XLR MT）分解为语法规则检索和规则应用两步，并提出用代码格式表示语法规则以提升 LLM 在两步中的表现，在壮语翻译上实现了 13.1% BLEU 的提升。

**[M-Mad Multidimensional Multi-Agent Debate For Advanced Machine Translation Evalu](m-mad_multidimensional_multi-agent_debate_for_advanced_machine_translation_evalu.md)**

:   提出 M-MAD 框架，将 MQM 评估标准解耦为独立维度（准确性、流畅性、风格、术语），在每个维度内进行多智能体正反方辩论，最后由裁判智能体综合各维度结果，在 segment 级别显著超越已有 LLM-as-a-judge 方法，甚至用 GPT-4o mini 就能媲美 SOTA 有参考自动指标。

**[M2Rc-Eval Massively Multilingual Repository-Level Code Completion Evaluation](m2rc-eval_massively_multilingual_repository-level_code_completion_evaluation.md)**

:   提出覆盖18种编程语言的大规模多语言仓库级代码补全基准 M2rc-Eval，配合基于 AST 的桶级和语义级细粒度标注，并构建 M2rc-Instruct 指令语料以提升模型性能。

**[M3Finmeeting A Multilingual Multi-Sector And Multi-Task Financial Meeting Unders](m3finmeeting_a_multilingual_multi-sector_and_multi-task_financial_meeting_unders.md)**

:   构建了 M3FinMeeting——首个面向金融会议的多语言（中英日）、多行业、多任务评测基准，包含 600 场真实金融会议的摘要、QA 对抽取和问答三项任务，揭示了当前最先进 LLM 在金融会议理解上仍有显著提升空间。

**[M Rewardbench](m_rewardbench.md)**

:   构建首个多语言奖励模型评估基准M-RewardBench（23种语言、2.87K偏好实例，覆盖对话/安全/推理/翻译四类能力），系统评估多种RM后发现英语与非英语RM性能存在显著差距，且翻译质量和语言资源量对RM表现有重要影响。

**[Machine Translation Models Are Zero-Shot Detectors Of Translation Direction](machine_translation_models_are_zero-shot_detectors_of_translation_direction.md)**

:   提出一种基于 NMT 模型翻译概率的无监督翻译方向检测方法：若 $p(\text{translation}|\text{original}) > p(\text{original}|\text{translation})$，则可零样本判断平行文本的原始翻译方向，NMT 翻译的文档级检测准确率达 96%。

**[Marco Bench Multilingual If](marco_bench_multilingual_if.md)**

:   将英文IFEval基准扩展到30种语言并进行文化本地化，揭示LLM在多语言指令遵循中高/低资源语言间25-35%的准确率差距，以及机器翻译数据低估模型性能7-22%。

**[Memorization Inheritance Seqkd](memorization_inheritance_seqkd.md)**

:   本文首次系统研究了序列级知识蒸馏（SeqKD）中教师模型的记忆行为如何传递给学生模型，发现学生模型虽未直接接触原始训练数据，但其提取式记忆率比基线模型高 57%，幻觉率也增加，并提出 Adaptive-SeqKD 通过在高质量子集上微调教师来缓解这些问题。

**[Mid Layer Crosslingual Alignment](mid_layer_crosslingual_alignment.md)**

:   通过分析 1000+ 语言对发现 LLM 中间层具有最强的跨语言对齐潜力，提出在任务训练中集成中间层对齐目标（对比损失），在槽填充（F1 61.7%）、机器翻译（BLEU 32.3）和结构化文本生成上显著提升跨语言迁移，对未见语言也有效。

**[Milic-Eval Benchmarking Multilingual Llms For Chinas Minority Languages](milic-eval_benchmarking_multilingual_llms_for_chinas_minority_languages.md)**

:   构建首个中国少数民族语言 LLM 评估基准 MiLiC-Eval，包含 24K 实例覆盖 9 个任务、聚焦藏语/维吴尔语/哈萨克语/蒙古语 4 种语言，发现开源 LLM 在语法密集型任务和多文字语言上表现极差。

**[Modular Sentence Encoders](modular_sentence_encoders.md)**

:   本文提出模块化多语言句子编码器训练方案：先训练语言特定模块（embedding + 语言适配器 + 句子编码适配器）缓解多语言诅咒，再训练跨语言对齐适配器同时使用平行和释义数据解决不同跨语言任务间的性能权衡，在 4 个任务和 23 种语言上全面优于单体模型训练。

**[Moscar A Large-Scale Multilingual And Multimodal Document-Level Corpus](moscar_a_large-scale_multilingual_and_multimodal_document-level_corpus.md)**

:   提出 mOSCAR——首个大规模多语言多模态文档级语料库（163种语言、303M文档、200B tokens、1.15B图片），从 Common Crawl 中提取交错的图文文档，并证明在此数据上训练的多语言 mLLM 能获得显著的 few-shot 学习提升。

**[Msqad Multilingual Ethical Bias](msqad_multilingual_ethical_bias.md)**

:   提出多语言敏感问答数据集MSQAD（基于Human Rights Watch 17个人权话题），通过McNemar检验和PERMANOVA检验两种统计假设检验方法，系统验证了LLM在不同语言下对相同敏感问题的回答存在显著伦理偏差——中文和印地语拒绝率最高，西班牙语和德语最容易生成不当回答，且该偏差在7个不同LLM中普遍存在。

**[Mt Eval Human Parity](mt_eval_human_parity.md)**

:   首次将人类基线引入 WMT Metrics Shared Task 的排名，发现最先进的自动指标经常与人类评估者排名持平甚至更高，但论证了现在声称"人类对等"为时尚早，并讨论了衡量 MT 评估进步的根本困难。

**[Mtvqa Benchmarking Multilingual Text-Centric Visual Question Answering](mtvqa_benchmarking_multilingual_text-centric_visual_question_answering.md)**

:   构建了 MTVQA——首个覆盖 9 种语言的多语言文本中心视觉问答基准，通过人类专家标注解决翻译方法的"视觉-文本不对齐"问题，评估显示最佳 MLLM（InternVL-2.5，32.2%）与人类表现（79.7%）差距巨大，揭示了多语言文本理解的严峻挑战。

**[Multi-Perspective Alignment For Increasing Naturalness In Neural Machine Transla](multi-perspective_alignment_for_increasing_naturalness_in_neural_machine_transla.md)**

:   提出多视角对齐框架 (Multi-perspective Alignment)，同时奖励翻译自然度和内容保留，通过翻译体分类器和 COMET 的联合奖励信号对 NMT 模型进行强化学习微调，使译文词汇更丰富且不损失翻译准确度。

**[Multilingual Encoder Knows More Than You Realize Shared Weights Pretraining For ](multilingual_encoder_knows_more_than_you_realize_shared_weights_pretraining_for_.md)**

:   提出 XLM-SWCM 框架，通过将多语言编码器权重复用到解码器中（CustomDecoderLayer 共享 + NormalDecoderLayer 随机初始化交替插入），以 457M 参数在极低资源语言（藏语）上超越 13B 参数的 MC2-LLaMA，藏语摘要 ROUGE-L 达 25.7 vs 16.1。

**[Multilingual Llm English Accent](multilingual_llm_english_accent.md)**

:   本文揭示多语言 LLM 在非英语语言生成中存在"英语口音"——词汇和句法上偏向英语模式，提出了基于 JSD（词汇分布）和 WL 图核+MMD（句法依赖树）的语料级自然度指标，并通过 DPO 对齐方法有效提升目标语言的自然度。

**[Multilingual Speech Data Quality](multilingual_speech_data_quality.md)**

:   对三大公开多语言语音数据集（Common Voice、FLEURS、VoxPopuli）进行系统质量审计，发现低资源语言存在严重的微观和宏观质量问题，并提出基于社会语言学意识的数据集创建指南。

**[Nametag 3 A Tool And A Service For Multilingualmultitagset Ner](nametag_3_a_tool_and_a_service_for_multilingualmultitagset_ner.md)**

:   本文介绍 NameTag 3，一个开源的多语言、多数据集、多标签集命名实体识别工具和云服务，基于微调的预训练语言模型，单个 355M 参数模型在 15 种语言的 21 个测试集上达到 SOTA，同时比 DeepSeek-R1 等 LLM 快 10,000 倍以上。

**[Probing Llms For Multilingual Discourse Generalization Through A Unified Label S](probing_llms_for_multilingual_discourse_generalization_through_a_unified_label_s.md)**

:   本文提出首个跨框架、跨语言的统一篇章关系标签集（17类），并通过对23个LLM的注意力探针实验，证明多语言LLM能够在中间层编码跨语言可迁移的篇章级表征，且多语言训练和模型规模共同提升泛化能力。

**[Q2E Query-To-Event Decomposition For Zero-Shot Multilingual Text-To-Video Retrie](q2e_query-to-event_decomposition_for_zero-shot_multilingual_text-to-video_retrie.md)**

:   Q2E 提出了一种零样本的查询到事件分解方法，利用 LLM 和 VLM 的参数化世界知识将简单查询分解为前因/当前/后果事件，并结合视频的视觉描述和语音转录，通过逆熵融合排序实现 SOTA 的多语言文本到视频检索性能。

**[Registering Source Tokens To Target Language Spaces In Multilingual Neural Machi](registering_source_tokens_to_target_language_spaces_in_multilingual_neural_machi.md)**

:   提出 Registering 方法：在源语言和目标语言 token 之间插入一组目标语言标记（registers），通过修改注意力掩码使目标生成仅依赖 registers 的激活，彻底解决多语言翻译中的 off-target 问题，使小模型 MITRE-913M 超越 NLLB-3.3B。

**[Semantic Aware Linear Transfer By Recycling Pre-Trained Language Models For Cros](semantic_aware_linear_transfer_by_recycling_pre-trained_language_models_for_cros.md)**

:   提出 SALT（Semantic Aware Linear Transfer），通过为每个非共享词表 token 基于语义相似的共享 token 对构建独立的最小二乘变换矩阵，将目标语言 PLM 的丰富嵌入表示迁移到英语中心 LLM 的嵌入空间，在下游任务、持续预训练收敛速度和跨语言理解上均优于现有方法。

**[Seqpo-Simt Sequential Policy Optimization For Simultaneous Machine Translation](seqpo-simt_sequential_policy_optimization_for_simultaneous_machine_translation.md)**

:   将同步机器翻译（SiMT）建模为多步序列决策问题，提出 SeqPO-SiMT 策略优化框架，融合翻译质量和延迟的奖励信号，在 7B LLM 上实现 SiMT 性能媲美离线翻译的强模型。

**[Shifcon Nondominant Language](shifcon_nondominant_language.md)**

:   提出 ShifCon 框架，通过将非优势语言的表示 shift 到优势语言子空间以获取更丰富的模型知识，再 shift 回原语言子空间进行生成，结合多语言对比学习，显著提升低资源语言的表现。

**[Statement-Tuning Enables Efficient Cross-Lingual Generalization In Encoder-Only ](statement-tuning_enables_efficient_cross-lingual_generalization_in_encoder-only_.md)**

:   将 Statement-Tuning 方法扩展到多语言场景，证明仅 276M 参数的 mDeBERTa 编码器模型通过多语言 Statement-Tuning 微调后，能在未见任务和未见语言上实现跨语言零样本泛化，在多个 NLU 任务上匹敌甚至超越 70B+ 参数的生成式 LLM。

**[Team Ack At Semeval-2025 Task 2 Beyond Word-For-Word Machine Translation For Eng](team_ack_at_semeval-2025_task_2_beyond_word-for-word_machine_translation_for_eng.md)**

:   本文在 SemEval-2025 Task 2 中系统评估了 13 个模型（LLM + 传统 MT）在英韩实体密集文本翻译上的表现，通过自动指标和双语人工评估揭示了 LLM 虽优于传统 MT 但在需要文化适应的实体翻译上仍普遍失败，并构建了翻译错误分类体系。

**[The Hidden Space Of Safety Understanding Preference-Tuned Llms In Multilingual C](the_hidden_space_of_safety_understanding_preference-tuned_llms_in_multilingual_c.md)**

:   本文系统分析了偏好调优（RLHF/DPO 等）对 LLM 内部表示空间在多语言场景下的影响，发现对齐机制在英语上能有效分离有害/无害内容的隐空间表示，但在印地语、中文、德语等非英语语言上效果显著退化，揭示了当前对齐方法存在严重的单语偏差问题。

**[Thor-Moe Hierarchical Task-Guided And Context-Responsive Routing For Neural Mach](thor-moe_hierarchical_task-guided_and_context-responsive_routing_for_neural_mach.md)**

:   提出THOR-MoE框架，通过层级任务引导路由（自动预测领域/语言并生成混合任务表示来选任务级专家子集）和上下文响应路由（将全局上下文注入token表示以辅助专家选择），在多领域和多语言翻译中以更少激活参数获得显著性能提升。

**[Towards Global Ai Inclusivity A Large-Scale Multilingual Terminology Dataset Gis](towards_global_ai_inclusivity_a_large-scale_multilingual_terminology_dataset_gis.md)**

:   构建了首个大规模多语言 AI 术语数据集 GIST，包含从顶级 AI 会议论文中提取的 5K 术语及其阿拉伯语、中文、法语、日语和俄语翻译，并探索了三种无需重训练的术语集成方法来提升机器翻译质量。

**[Trans-Zero Self-Play Incentivizes Large Language Models For Multilingual Transla](trans-zero_self-play_incentivizes_large_language_models_for_multilingual_transla.md)**

:   提出 Trans-Zero 自博弈框架，仅使用单语数据，通过遗传蒙特卡洛树搜索（G-MCTS）在多语言翻译过程中探索语义一致的候选翻译，结合偏好优化实现无平行数据的多语言翻译训练，性能可媲美大规模监督微调方法。

**[Translation Robustness](translation_robustness.md)**

:   通过合成噪声和社交媒体文本的系统性实验，证明现代大规模预训练翻译模型（LLM）在未经任何专门鲁棒性训练的情况下，对多种输入噪声的鲁棒性已远超传统 NMT 模型，鲁棒性随模型规模增长自然提升。

**[Unveiling The Power Of Source Source-Based Minimum Bayes Risk Decoding For Neura](unveiling_the_power_of_source_source-based_minimum_bayes_risk_decoding_for_neura.md)**

:   提出 source-based MBR (sMBR) 解码方法，利用释义/回译生成的准源端句子作为"支持假设"，结合无参考 QE 指标作为效用函数，首次在 MBR 解码中完全依赖源端信息，在经典和 LLM 两种 NMT 设置下均优于 QE reranking 和标准 MBR 解码。

**[Watching The Watchers Exposing Gender Disparities In Machine Translation Quality](watching_the_watchers_exposing_gender_disparities_in_machine_translation_quality.md)**

:   系统性地揭示了机器翻译质量估计(QE)指标中的性别偏见：当源语言性别模糊时，阳性形式翻译得分系统性地高于阴性形式，性别中性翻译被惩罚；即使有上下文消歧线索，阴性指称的错误率仍显著高于阳性，且该偏见会传播到数据过滤和解码等下游任务中。

**[Zipa A Family Of Efficient Models For Multilingual Phone Recognition](zipa_a_family_of_efficient_models_for_multilingual_phone_recognition.md)**

:   提出 Zipa 系列高效语音模型，基于 Zipformer 骨干和 IpaPack++（17,132 小时多语言标注数据），在多语言音素识别上达到 SOTA，64M 参数模型即超越现有 300M 模型，并通过噪声学生训练在 4000+ 种语言上进一步提升。
