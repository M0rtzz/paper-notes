<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**💬 ACL2025** · 共 **304** 篇

**[Towards Robust ESG Analysis Against Greenwashing Risks: A3CG](a3cg_esg_greenwashing.md)**

:   提出 A3CG 数据集和方面-行动分析任务（从可持续性声明中提取方面及其行动类型：已实施/计划中/不确定），通过跨类别泛化设置评估 NLP 方法抵御漂绿风险的鲁棒性，发现监督学习（GRACE F1=47.51）优于 LLM（Claude 3.5 F1=42.03）但泛化效率更差。

**[A Conformal Risk Control Framework for Granular Word Assessment and Uncertainty Calibration of CLIPScore Quality Estimates](a_conformal_risk_control_framework_for_granular_word_assessment_and_uncertainty_.md)**

:   提出基于保形风险控制（Conformal Risk Control）框架校准 CLIPScore 的方法——通过对 CLIP 视觉/文本编码器的注意力掩码采样生成 CLIPScore 分布，然后利用保形风险控制 (1) 检测图像描述中的干扰词（foil words），(2) 生成校准置信区间，在 FOIL-it/FOIL-nocaps/Rich-HF 基准上以简单方法达到与复杂专用方法相当的干扰词检测性能，同时提供形式化风险保证。

**[A Dual-Perspective NLG Meta-Evaluation Framework with Automatic Benchmark and Better Interpretability](a_dual-perspective_nlg_meta-evaluation_framework_with_automatic_benchmark_and_be.md)**

:   揭示传统 NLG 元评估的局限（人工评分平均聚合不合理、相关系数选择模糊），提出双视角元评估框架：全局视角（序数分类，评估粗粒度评级能力）+ 局部视角（相邻成对比较，评估细粒度区分能力），并引入基于可控错误注入的自动基准构建方法，在 16 个 LLM 上验证不同模型在两个视角上的能力分布差异显著。

**[GKI-ICD: A General Knowledge Injection Framework for ICD Coding](a_general_knowledge_injection_framework_for_icd_coding.md)**

:   提出 GKI-ICD，首个无需额外专用网络模块即可同时注入三种 ICD 编码知识（描述、同义词、层级结构）的通用框架——通过合成知识引导文本（Guideline Synthesis）+ 多任务学习实现知识注入，在 MIMIC-III 和 MIMIC-III-50 上大多数指标达到 SOTA。

**[Barec: A Large and Balanced Corpus for Fine-grained Arabic Readability Assessment](a_large_and_balanced_corpus_for_fine-grained_arabic_readability_assessment.md)**

:   构建 Barec（Balanced Arabic Readability Evaluation Corpus）——首个大规模细粒度阿拉伯语可读性评估语料库，包含 69K+ 句子（100万+词），覆盖 19 个可读性等级（从幼儿园到研究生），由 6 名专业阿拉伯语教育者标注，并在多种分级粒度（19/7/5/3级）上基准测试自动可读性评估模型。

**[A Little Human Data Goes A Long Way](a_little_human_data_goes_a_long_way.md)**

:   首次系统研究合成数据在事实验证和问答中能否替代人工标注——替换 90% 仅轻微下降，但替换最后 10% 严重退化；仅 125 条人工数据可显著提升纯合成模型，等效增益需 10 倍以上合成数据。

**[MisMatched: A Benchmark for Scientific Natural Language Inference](a_mismatched_benchmark_for_scientific_natural_language_inference.md)**

:   引入 MisMatched——首个覆盖非 CS 领域（心理学、工程、公共卫生）的科学 NLI 评估基准，2700 对人工标注句子对，最佳基线 Macro F1 仅 78.17%，且发现训练时加入隐式关系句子对可提升性能。

**[A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs](a_practical_approach_for_building_production-grade_conversational_agents_with_wo.md)**

:   提出基于有向无环图（DAG）工作流的混合对话 Agent 框架——每个图节点有独立系统提示/工具/执行规则以处理特定场景约束。结合原型 Agent 数据收集、状态感知的响应掩码微调策略，在 Kakao 移动电商场景中任务准确率提升 52%、格式遵从度提升 50%，超越 GPT-4o。

**[A Reality Check on Context Utilisation for Retrieval-Augmented Generation](a_reality_check_on_context_utilisation_for_retrieval-augmented_generation.md)**

:   提出DRUID真实世界事实验证数据集和ACU评估指标，揭示合成数据集（CounterFact、ConflictQA）夸大了上下文特征的影响，导致对LLM上下文利用能力的过度乐观评估，呼吁使用真实检索数据研究RAG。

**[SSUF: A Semi-supervised Scalable Unified Framework for E-commerce Query Classification](a_semi-supervised_scalable_unified_framework_for_e-commerce_query_classification.md)**

:   提出电商查询分类的半监督可扩展统一框架 SSUF——三个可插拔模块：知识增强（LLM 世界知识+后验点击）解决短查询信息不足、标签增强（语义编码+半监督信号）打破对后验标签的依赖、结构增强（共现+语义+层级图 GCN）传播长尾标签梯度。已在 JD.COM 部署，离线和在线 A/B 实验均显著超越 SOTA。

**[A Spatio-Temporal Point Process for Fine-Grained Modeling of Reading Behavior](a_spatio-temporal_point_process_for_fine-grained_modeling_of_reading_behavior.md)**

:   提出基于标记时空点过程（Marked Spatio-Temporal Point Process）的阅读行为概率模型——用 Hawkes 过程建模跳视（何时何处注视），用对数正态分布+卷积建模注视时长（持续多久），避免传统聚合测量的信息丢失。实证发现：Hawkes 模型比基线更好拟合跳视数据，但上下文 surprisal 作为预测因子仅带来边际改善——surprisal 理论难以解释细粒度眼动。

**[IDR²: Accelerating Adaptive RAG via Instruction-Driven Representation Reduction of Retrieval Overlaps](accelerating_adaptive_retrieval_augmented_generation_via_instruction-driven_repr.md)**

:   首次识别自适应 RAG（A-RAG）中多轮检索结果重叠导致的冗余计算问题，提出 IDR²（Instruction-Driven Representation Reduction）框架：跨迭代 KV 缓存共享（CICS）加速预填充 2.79 倍、指令引导去重增强（IDGR）帮助 LLM 正确处理缓存vs新文档、信息引导并行生成（IGPG）加速解码 2.33 倍，总体 A-RAG 流程加速 2.0 倍且不损失生成质量。

**[Access Denied Inc: The First Benchmark Environment for Sensitivity Awareness](access_denied_inc_the_first_benchmark_environment_for_sensitivity_awareness.md)**

:   提出敏感性感知（Sensitivity Awareness, SA）概念——评估 LLM 是否能遵守基于角色的访问控制规则——并构建首个评估基准 Access Denied Inc：模拟企业数据库 + 多用户组权限 + 自动化问卷+半自动评分（99.9%自动），揭示模型在拒绝未授权请求和响应合法查询上的显著差异。

**[AceCoder: Acing Coder RL via Automated Test-Case Synthesis](acecoder_acing_coder_rl_via_automated.md)**

:   构建 AceCode-87K（87K 编码题 + 138 万自动合成测试用例），训练代码专用 Reward Model（7B 超越 340B Nemotron），Best-of-N 提升 Llama-3.1-8B 平均 8.9 分，R1 风格从 base 直接 RL 仅 80 步 HumanEval+ 提升 22.5%。

**[ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Clause Retrieval](acord_an_expert-annotated_retrieval_dataset_for_legal_contract_drafting.md)**

:   构建首个面向合同起草的专家标注条款检索基准 ACORD——114 个律师编写的查询、126,000+ 查询-条款对、1-5 星相关性评分，聚焦责任限制/赔偿/控制权变更/最惠国等复杂条款；bi-encoder 检索 + LLM 点式重排序表现有前景但距律师需求仍有显著差距。LLM 直接起草对比律师修改暴露了多种缺陷。

**[NTIL: Advancing Sequential Numerical Prediction in Autoregressive Models](advancing_sequential_numerical_prediction_in_autoregressive_models.md)**

:   提出 NTIL（Numerical Token Integrity Loss）解决自回归模型数值预测的两大缺陷——(1) token 级用 EMD 替代交叉熵保留数字间序数关系+指数位置加权，(2) 序列级通过可微数值构建+相对偏差度量评估整体数值误差。首次将 EMD 用于自回归模型优化，在目标检测/文本识别/数学推理上显著提升。

**[AIDE: Attribute-Guided Multi-Hop Data Expansion for Data Scarcity in Task-Specific Fine-tuning](aide_attribute-guided_multi-hop_data_expansion_for_data_scarcity_in_task-specifi.md)**

:   提出 AIDE——属性引导的多跳数据扩展框架，从仅 10 个种子数据点出发，通过提取主题/属性/关系三元组引导 LLM 多跳递归合成新数据，加入 Persona 增加多样性和残差连接防止偏离，在 Mistral-7B/Llama-3.1-8B/Llama-3.2-3B 上超越人工标注数据微调，比 Evol-Instruct 等 SOTA 提升 30%+。

**[AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark](air-bench_automated_heterogeneous_information_retrieval_benchmark.md)**

:   提出 AIR-Bench——首个自动化、异构、动态的信息检索评测基准，通过 LLM 自动从真实语料生成高质量测试数据（三阶段管线：语料准备→候选生成→质量控制），覆盖 2 类任务、9 个领域、13 种语言共 69 个数据集，与人工标注数据高度一致，且持续动态更新避免数据泄露。

**[Aligned but Blind: Alignment Increases Implicit Bias by Reducing Awareness of Race](aligned_but_blind_implicit_bias.md)**

:   揭示对齐训练的"种族盲视"副作用：对齐使 LLM 在歧义上下文中不再将 black/white 表征为种族概念，安全护栏因此无法激活，导致隐式偏见从 64.1% 飙升至 91.4%；反直觉地，在早期层注入种族感知激活（而非遗忘）可将隐式偏见从 97.3% 降至 42.4%。

**[AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment](ambik_dataset_of_ambiguous_tasks_in_kitchen_environment.md)**

:   提出 AmbiK，一个专门用于厨房环境中歧义指令检测的纯文本数据集，包含 1000 对歧义/非歧义指令，按三种歧义类型（用户偏好/常识/安全）分类标注，并评估了多种基于 conformal prediction 的歧义检测方法，发现现有方法在该基准上表现很差。

**[An Analysis of Datasets, Metrics and Models in Keyphrase Generation](an_analysis_of_datasets_metrics_and_models_in_keyphrase_generation.md)**

:   对关键短语生成（keyphrase generation）领域50+篇论文进行系统性分析，揭示了基准数据集高度相似、评估指标计算不一致导致性能被高估等关键问题，并发布了一个强力PLM-based模型以促进未来研究。

**[AnalyticKWS: Towards Exemplar-Free Analytic Class Incremental Learning for Small-footprint Keyword Spotting](analytickws_towards_exemplar-free_analytic_class_incremental_learning_for_small-.md)**

:   提出 AnalyticKWS，一种无需存储历史样本的关键词检测增量学习方法，通过冻结特征提取器 + 递归最小二乘解析解更新分类器，在 GSC 和 SC-100 数据集上超过了所有基于样本回放的方法，且训练时间和内存开销极低。

**[AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge](antileakbench_preventing_data_contamination_by_automatically_constructing_benchm.md)**

:   提出 AntiLeakBench——自动化反泄露基准框架，通过识别 LLM 知识截止后更新的真实世界新知识自动构建 QA 测试样本（而非简单收集新发布数据），确保测试知识严格不在训练集中，全自动流程无需人工标注，实验证实截止后性能普遍下降验证了数据污染的普遍存在。

**[Anything Goes? A Crosslinguistic Study of (Im)possible Language Learning in LMs](anything_goes_a_crosslinguistic_study_of_impossible_language_learning_in_lms.md)**

:   跨语言研究 LM 能否区分可能语言和不可能语言——在 12 种语言（4 个语系）上训练 GPT-2 Small 的可能/不可能/未见证变体，发现模型大体上能区分可能 vs 不可能语言（单语言内），但**跨语言**时区分能力减弱，且对类型学未见证语言（Greenberg Universal 20 的未见证词序）的区分仅在泛化测试中有效而在困惑度上无效——LM 有部分人类样的归纳偏置但弱于人类。

**[Are Bias Evaluation Methods Biased?](are_bias_evaluation_methods_biased.md)**

:   严格控制变量后比较三种主流偏见评估方法（结构化问答 BBQ、LLM-as-a-Judge、情感分析），发现不同方法对同一组 LLM 产生显著不同的偏见排名——偏见评估方法本身就是有偏的，企业不应依赖单一偏见基准来选择模型。

**[Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral](are_rules_meant_to_be_broken_understanding_multilingual_moral_reasoning_as_a_com.md)**

:   提出UniMoral——一个跨6种语言的统一道德推理数据集，将道德推理建模为包含行为预测、道德类型分类、因素归因和后果生成的计算流水线，对3个LLM的基准测试揭示隐式道德语境能增强模型道德推理能力但仍需专门化方法。

**[ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](arise_risk_adaptive_search.md)**

:   提出 ARise 框架，将贝叶斯风险评估与动态 RAG 集成到蒙特卡洛树搜索中，解决知识增强推理中的错误传播和验证瓶颈问题，在多跳QA任务上平均准确率超 SOTA KAR 方法 23.10%，超 RAG-equipped 推理模型（DeepSeek-R1）25.37%。

**[Attention Entropy is a Key Factor for Parallel Context Encoding](attention_entropy_parallel_encoding.md)**

:   发现并行上下文编码导致 query token 的注意力熵异常升高是性能下降的关键因素，并提出 Attention Sink 共享前缀和 Selective Attention 两种免微调方法有效缓解该问题。

**[AutoDS: Autonomous Data Selection with Zero-shot Generative Classifiers for Mathematical Texts](autonomous_data_selection_with_zero-shot_generative_classifiers_for_mathematical.md)**

:   提出 AutoDS——用基座 LLM 自身作为零样本"生成分类器"自动评估数学文本质量。通过两个 yes/no 问题的 logits 计算连续 LM-Score（而非二分类），筛选高质量数学文本做持续预训练，在 MATH/GSM8K/BBH 上大幅提升并实现约 2 倍 token 效率提升。发布 AutoMathText 数据集。

**[Behavioural vs. Representational Systematicity in End-to-End Models: An Opinionated Survey](behavioural_vs_representational_systematicity_in_end-to-end_models_an_opinionate.md)**

:   区分行为系统性（模型能否正确处理新组合）与表征系统性（模型内部表征是否结构化），指出当前基准和模型主要测试行为系统性却常声称解决了 Fodor-Pylyshyn 对表征系统性的挑战。基于 Hadley (1994) 的三级分类（弱/准/强系统性）分析语言和视觉关键基准的测试范围，最终呼吁用机械可解释性方法在行为评估之上补充表征分析。

**[Better Embeddings with Coupled Adam](better_embeddings_with_coupled_adam.md)**

:   从理论上证明 Adam 优化器的逐 token 二阶矩是导致 LLM 词嵌入各向异性（均值偏移）的根因，提出 Coupled Adam——对嵌入层的二阶矩取词汇平均——消除了各向异性问题，并在大规模实验中提升了嵌入质量和下游性能。

**[Beyond Frameworks: Unpacking Collaboration Strategies in Multi-Agent Systems](beyond_frameworks_multi_agent_collaboration.md)**

:   本文系统化地将多智能体协作分解为四个维度（治理模式、参与控制、交互模式、上下文管理），通过两个上下文依赖任务的大量实验证明：集中治理+指导者控制参与+有序交互+指导者摘要的组合最优，在保持甚至提升准确率的同时减少高达 93% 的 token 消耗。

**[Beyond True or False: Retrieval-Augmented Hierarchical Analysis of Nuanced Claims](beyond_true_or_false_retrieval-augmented_hierarchical_analysis_of_nuanced_claims.md)**

:   提出 ClaimSpect 框架，将复杂声明自动分解为层次化的方面（aspect）树，并通过区分性检索从语料库中发现各方面的支持/中立/反对观点及其共识程度。

**[Bone Soups: A Seek-and-Soup Model Merging Approach for Controllable Multi-Objective Generation](bone_soups_multi_objective_gen.md)**

:   提出 Bone Soup 模型合并方法，通过先构造"骨架奖励"（多目标奖励的组合）训练骨架模型、再用对称循环矩阵映射确定合并系数，解决了 Rewarded Soup 中单目标模型合并的次优性问题，在三个多目标生成任务上实现更好的 Pareto 前沿和可控性。

**[Bregman Conditional Random Fields: Sequence Labeling with Parallelizable Inference](bregman_conditional_random_fields_sequence_labeling_with_parallelizable_inferenc.md)**

:   提出 Bregman CRF (Bcrf)，一种基于均值正则化（mean regularization）的新型序列标注判别模型，使用迭代 Bregman 投影实现可并行化的推理算法，替代传统 CRF 中固有顺序的 Viterbi/Forward 算法，在 POS/NER/分词任务上性能与标准 CRF 持平但更快，且在有禁止标签转移约束的场景下优于 Mean Field 方法。

**[Byte Latent Transformer: Patches Scale Better Than Tokens](byte_latent_transformer.md)**

:   Meta FAIR提出BLT——首个在大规模（8B参数/4T字节）上匹配基于tokenizer的LLM性能的字节级架构，通过基于下一字节熵的动态分组（patching）将字节聚合为可变长度patch，在保持性能的同时实现最高50%推理FLOP节省，并开辟了"同时增大模型和patch尺寸"的全新scaling维度。

**[CADReview: Automatically Reviewing CAD Programs with Error Detection and Correction](cadreview_automatically_reviewing_cad_programs_with_error_detection_and_correcti.md)**

:   提出 CAD 程序审查任务及 ReCAD 框架，基于参考图像自动检测 CAD 程序中的错误并生成修正反馈，构建了包含 20K+ 样本（8 类错误）的 CADReview 数据集。

**[Can Community Notes Replace Professional Fact-Checkers?](can_community_notes_replace_professional_fact-checkers.md)**

:   通过大规模分析 Twitter/X 的 Community Notes 数据（66.4 万条），发现社区笔记对专业事实核查的依赖远超此前报告（至少 5-7%），证明高质量社区审核离不开专业事实核查，尤其在涉及阴谋论和更广泛虚假叙事的高风险内容上。

**[Can Uniform Meaning Representation Help GPT-4 Translate from Indigenous Languages?](can_uniform_meaning_representation_help_gpt-4_translate_from_indigenous_language.md)**

:   探索将统一意义表示（UMR）语义图纳入 GPT-4 提示中，翻译三种原住民语言（纳瓦霍语、阿拉帕霍语、库卡马语），发现在大多数情况下 UMR 的加入带来统计显著的性能提升。

**[Capacity Matters: A Proof-of-Concept for Transformer Memorization on Real-World Data](capacity_matters_a_proof-of-concept_for_transformer_memorization_on_real-world_d.md)**

:   本文以SNOMED医学知识图谱为数据源，系统研究了decoder-only Transformer在结构化数据上的记忆容量，发现嵌入维度是决定学习速度和容量的主要因素，而增加层数收效甚微，Softmax激活函数表现最稳定。

**[Causal Estimation of Tokenisation Bias](causal_tokenisation_bias.md)**

:   本文首次将 tokeniser 选择对语言模型输出的影响定义为"分词偏差"(tokenisation bias)，并利用因果推断中的断点回归设计(RDD)来量化这一效应——发现当一个 subword 被纳入词表时，其对应字符串的概率最高可提升 17 倍（小模型），揭示分词是语言建模中一个被低估的关键设计选择。

**[Cautious Next Token Prediction](cautious_next_token_prediction.md)**

:   提出 Cautious Next Token Prediction (CNTP)，一种无需训练的自适应解码策略：在模型预测熵较高（不确定）时采样多条候选路径至标点处，选择困惑度最低的路径作为最终续写，从而在不牺牲多样性的前提下显著提升准确性。

**[ChartLens: Fine-Grained Visual Attribution in Charts](chartlens_fine-grained_visual_attribution_in_charts.md)**

:   提出图表的事后细粒度视觉归因（Post-Hoc Fine-grained Visual Attribution）任务，设计 ChartLens 算法利用分割技术标记图表元素并通过 Set-of-Marks 提示多模态 LLM 进行精确归因，同时构建 ChartVA-Eval 基准，在三类图表上取得 26-66% 的 F1 提升。

**[ChatBench: From Static Benchmarks to Human-AI Evaluation](chatbench_from_static_benchmarks_to_human-ai_evaluation.md)**

:   通过用户实验将 MMLU 静态基准转换为用户-AI 对话，构建 ChatBench 数据集（396 道题、7336 段对话），发现 AI-alone 准确率无法预测 user-AI 准确率，并训练用户模拟器使相关性提升 22-26 个百分点，为可扩展的交互式评估奠基。

**[ChuLo: Chunk-Level Key Information Representation for Long Document Understanding](chulo_chunk-level_key_information_representation_for_long_document_understanding.md)**

:   ChuLo 的核心不是单纯把长文档切小，而是先在全文范围内找出最关键的语义短语，再把这些关键信息重新注入每个 chunk 的表示里，从而在只用紧凑块表示的前提下，同时保住全局语义和细粒度 token 信息。

**[CiteEval: Principle-Driven Citation Evaluation for Source Attribution](citeeval_principle-driven_citation_evaluation_for_source_attribution.md)**

:   本文提出 CiteEval，一个基于原则驱动的引用评估框架，通过考虑完整检索上下文、超越检索的多种上下文以及细粒度评价标准，构建了 CiteBench 基准和 CiteEval-Auto 自动指标，在引用质量评估上显著优于基于 NLI 的现有方法。

**[CLaC at SemEval-2025 Task 6: A Multi-Architecture Approach for Corporate Environmental Promise Verification](clac_at_semeval-2025_task_6_a_multi-architecture_approach_for_corporate_environm.md)**

:   本文针对SemEval-2025 Task 6（PromiseEval）的企业ESG报告承诺验证任务，探索了三种递进的模型架构：ESG-BERT基线、语言特征增强版、以及融合注意力池化和多目标学习的联合子任务模型，最终以0.5268的私榜分数略超基线（0.5227），验证了语言特征工程和多任务学习在ESG承诺验证中的有效性。

**[CLIX: Cross-Lingual Explanations of Idiomatic Expressions](clix_cross-lingual_explanations_of_idiomatic_expressions.md)**

:   提出跨语言习语解释任务 CLIX，构建了包含英语习语及其西班牙语/德语解释的数据集，系统评估了 seq2seq 模型和 LLM 在该任务上的表现，发现 GPT-3.5 Turbo 的 pipeline 策略（先英文解释再翻译）配合 few-shot 效果最佳，人工评估流畅度和准确度高达 4.7+/5。

**[CoachMe: Decoding Sport Elements with a Reference-Based Coaching Instruction Generation Model](coachme_sport_instruction.md)**

:   提出 CoachMe，通过对比学习者动作与参考动作的差异（时间+物理两个维度），自动生成运动特异性的教练指导文本，在花样滑冰和拳击上分别超过 GPT-4o 31.6% 和 58.3%（G-Eval）。

**[CoAM: Corpus of All-Type Multiword Expressions](coam_corpus_of_all-type_multiword_expressions.md)**

:   构建了一个高质量的全类型多词表达(MWE)识别数据集 CoAM（1.3K句），通过多步质量保障流程解决了现有数据集标注不一致的问题，并发现微调大语言模型在 MWE 识别任务上显著优于此前的 SOTA 方法 MWEasWSD。

**[CoIR: A Comprehensive Benchmark for Code Information Retrieval Models](coir_a_comprehensive_benchmark_for_code_information_retrieval_models.md)**

:   提出 CoIR，首个全面的代码信息检索基准，包含 10 个数据集、覆盖 4 大类 8 个子任务和 14 种编程语言，揭示了即使是 SOTA 检索模型在代码检索中也表现不佳，并指出许多模型已在现有排行榜上过拟合。

**[CoLA: Collaborative Low-Rank Adaptation](cola_collaborative_low-rank_adaptation.md)**

:   提出 CoLA，一种灵活的 LoRA 架构，打破矩阵 A 和 B 之间的固定数量约束（#A=M, #B=N），并设计三种协作策略（全协作/随机协作/启发式协作），结合扩展的 PiSSA 初始化，在低样本场景下显著优于现有 PEFT 方法。

**[Collapse of Dense Retrievers: Short, Early, and Literal Biases Outranking Factual Evidence](collapse_dense_retrievers.md)**

:   本文首次系统研究稠密检索器中多种启发式偏见（简短偏见、前置偏见、字面偏见、重复偏见）的个体和组合效应，发现当多种偏见叠加时，检索器选择包含答案的文档的概率低于10%，且这些偏见可被利用来操纵RAG系统，导致34%的性能下降。

**[Com2: A Causal-Guided Benchmark for Complex Commonsense Reasoning](com2_causal_commonsense.md)**

:   提出Com2基准，利用因果事件图和因果理论（干预/反事实）构建复杂常识推理任务，发现LLM在推理深度和广度上存在不足，后训练和慢思考可部分缓解。

**[ComfyUI-Copilot: An Intelligent Assistant for Automated Workflow Development](comfyui-copilot_an_intelligent_assistant_for_automated_workflow_development.md)**

:   提出 ComfyUI-Copilot，一个基于 LLM 的层次化多 agent 框架，作为 ComfyUI 插件提供智能节点/模型推荐和一键式工作流构建，覆盖 7K 节点、62K 模型和 9K 工作流的知识库，在线服务 22 国的 19K 用户并处理了 85K+ 查询。

**[Commonsense Reasoning in Arab Culture](commonsense_arab_culture.md)**

:   构建首个阿拉伯文化特定常识推理数据集 ArabCulture（3482 道由母语者原创的题目，覆盖 13 国×54 主题），评估多种 LLM 发现即使 32B 参数模型也在文化常识推理上表现不佳，且不同地区表现差异显著，地理/文化上下文线索的加入仅部分有效。

**[Completing A Systematic Review in Hours instead of Months with Interactive AI Agents](completing_a_systematic_review_in_hours.md)**

:   提出 InsightAgent，一个以人为中心的交互式多 Agent 系统，通过语义聚类分区、多 agent 并行阅读和实时用户交互，将医学系统综述的撰写时间从数月缩短到约 1.5 小时，达到人类撰写质量的 79.7%。

**[ConceptCarve: Dynamic Realization of Evidence](conceptcarve_dynamic_realization_of_evidence.md)**

:   提出 ConceptCarve 框架，通过 LLM 与传统检索器的交互式协作，动态构建概念树来表征证据在特定社区中的实现形式，解决了证据检索中的推理鸿沟和领域敏感性两大挑战。

**[ConECT Dataset: Overcoming Data Scarcity in Context-Aware E-Commerce MT](conect_dataset_overcoming_data_scarcity_in_context-aware_e-commerce_mt.md)**

:   构建了 ConECT——一个包含 11,400 句对的捷克-波兰电商产品翻译数据集，配有图片和类目路径元数据，系统评估了 VLM、NMT+类目路径和 NMT+图像描述三种上下文感知翻译方法，证明视觉和类目上下文能提升翻译质量，但合成图像描述反而有害。

**[Consultant Decoding: Yet Another Synergistic Mechanism](consultant_decoding_yet_another_synergistic_mechanism.md)**

:   提出 Consultant Decoding (CD)，一种基于目标模型负对数似然（NLL）验证 draft token 的新型协同解码机制，相比传统 Speculative Decoding 的似然比验证方法，能大幅提升接受率、降低大模型调用频率，同时保持甚至超越目标模型的生成质量。

**[CORAL: Learning Consistent Representations across Multi-step Training with Lighter Speculative Drafter](coral_speculative_drafting.md)**

:   CORAL 通过跨步表示对齐（CSRA）改进多步训练中 draft 模型的特征一致性，并用权重分组机制压缩大词表 LM head 的推理延迟，在 LLaMA3/Qwen2.5 上实现 2.50-4.07× 加速，超越 EAGLE-2 和 HASS。

**[CoRet: Improved Retriever for Code Editing](coret_improved_retriever_for_code_editing.md)**

:   提出 CoRet，一个面向代码编辑任务的稠密检索模型，通过整合代码语义、仓库文件层级结构和调用图依赖关系，并使用针对仓库级检索设计的对数似然损失函数，在 SWE-bench 和 Long Code Arena 上比现有模型的 Recall 至少提升 15 个百分点。

**[CortexDebate: Debating Sparsely and Equally for Multi-Agent Debate](cortexdebate_debating_sparsely_and_equally_for_multi-agent_debate.md)**

:   提出 CortexDebate，一种受人脑皮层工作机制启发的多智能体辩论方法，通过构建稀疏动态辩论图和基于 McKinsey 信任公式的评估模块（MDM），同时解决了现有 MAD 方法中"输入上下文过长"和"过度自信导致不平等辩论"两大核心问题。

**[Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity](cramming_tokens_embedding_capacity.md)**

:   通过逐样本优化方法将文本压缩到可训练的 [mem] 向量中，发现 Llama-3.1-8B 可以将 1568 个 token 无损压缩到单个输入向量中，揭示了现有方法（约 x10 压缩比）与实际可达极限（x1500+）之间存在两个数量级的差距。

**[Cross-Lingual Representation Alignment Through Contrastive Image-Caption Tuning](cross-lingual_representation_alignment_through_contrastive_image-caption_tuning.md)**

:   探索了一种无需平行语料的跨语言表示对齐方法——通过多语言图像-文本描述的对比学习（类 CLIP），让不同语言的文本表示在共享视觉空间中隐式对齐，并证明即使是编码器预训练中未见过的语言（如 Quechua）也能通过这种方式被纳入对齐体系。

**[Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon](cross-lingual_transfer_of_cultural_knowledge_an_asymmetric_phenomenon.md)**

:   通过构建可解释的实验框架，研究 LLM 语言适应过程中文化知识的跨语言迁移现象，发现高资源语言（中文、韩语）与英语之间存在双向迁移，而低资源语言（藏语、蒙古语）则呈现不对称迁移——知识主要从低资源语言流向英语，反向流动有限，并提出频率假说加以解释。

**[CruxEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution](cruxeval-x_a_benchmark_for_multilingual_code_reasoning_understanding_and_executi.md)**

:   提出 CruxEval-X，一个覆盖 19 种编程语言的多语言代码推理基准，通过全自动的测试引导翻译流水线从 Python 版 CruxEval 扩展而来，包含 12,660 个题目和 19K 测试用例，对 24 个 LLM 的评估揭示了编程语言间的相关性以及单语言训练模型的跨语言泛化能力。

**[CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming](culturalbench_a_robust_diverse_and_challenging_cultural_benchmark_by_human-ai_cu.md)**

:   通过 Human-AI CulturalTeaming（人机协作红队测试）流水线构建 CulturalBench，包含 1,696 个人类撰写并经五人独立验证的文化知识问题，覆盖 45 个全球地区和 17 个主题。CulturalBench-Hard（True/False格式）对最强模型（OpenAI o1）也仅 61.5%，远低于人类的 92.4%，揭示了模型在多答案问题上的模式寻求倾向和跨区域文化知识的不均衡表现。

**[Data-Constrained Synthesis of Training Data for De-Identification](data-constrained_synthesis_of_training_data_for_de-identification.md)**

:   本文系统研究了在数据受限条件下，如何利用领域适应的LLM生成合成临床文本，并通过机器标注训练NER模型进行个人身份信息（PII）检测，发现机器标注器的质量而非生成模型的规模是决定合成数据效用的关键因素。

**[Decoding Knowledge Attribution in Mixture-of-Experts: A Framework of Basic-Refinement Collaboration and Efficiency Analysis](decoding_knowledge_attribution_in_mixture-of-experts_a_framework_of_basic-refine.md)**

:   提出跨层级知识归因算法，系统解析 MoE 模型中共享专家与路由专家的"基础-精炼"协作框架，揭示 MoE 相比稠密模型实现 31% 更高的逐层效率，并通过语义驱动路由机制（注意力头-专家相关性 r=0.68）和专家阻断实验验证了架构深度对鲁棒性的决定性影响。

**[Decoding Reading Goals From Eye Movements](decoding_reading_goals_from_eye_movements.md)**

:   本文首次提出从眼动轨迹中解码读者阅读目标（信息检索 vs. 普通阅读）的任务，通过 12 种模型的系统比较发现基于 Transformer 的扫视路径+语言建模方案（RoBERTa-Eye-F）最优，可在阅读早期即实现高精度实时预测。

**[DeepRTL2: A Versatile Model for RTL-Related Tasks](deeprtl2_a_versatile_model_for_rtl-related_tasks.md)**

:   DeepRTL2是首个统一处理RTL（寄存器传输级）相关生成任务与嵌入任务的LLM，通过精心构建的数据集和GRIT训练策略，在代码生成、代码理解、自然语言代码搜索、功能等价检查和性能预测五大任务上达到SOTA。

**[DEMO: Reframing Dialogue Interaction with Fine-grained Element Modeling](demo_reframing_dialogue_interaction_with_fine-grained_element_modeling.md)**

:   本文提出对话元素建模（Dialogue Element Modeling）这一新任务，系统定义了对话生命周期中从"前奏"到"尾声"的全面元素体系，构建了包含元素感知和对话智能体交互两大能力的DEMO benchmark，并通过模仿学习训练DEMO agent在域内外任务上均表现优异。

**[Detection of Human and Machine-Authored Fake News in Urdu](detection_of_human_and_machine-authored_fake_news_in_urdu.md)**

:   本文提出了乌尔都语四分类假新闻检测任务（人类假/人类真/机器假/机器真），构建了首个乌尔都语机器生成新闻数据集，并提出层次化检测方法将四分类分解为机器文本检测和假新闻检测两个子任务，在域内和跨域设置中均优于基线。

**[Dictionaries to the Rescue: Cross-Lingual Vocabulary Transfer for Low-Resource Languages Using Bilingual Dictionaries](dictionaries_to_the_rescue_cross-lingual_vocabulary_transfer_for_low-resource_la.md)**

:   本文提出一种基于双语词典的跨语言词汇迁移方法，利用BPE分词器"删除子词后回退到更短子词"的特性，通过迭代删除-重分词-对齐的过程最大化目标语言子词的映射覆盖率，在低资源语言上显著优于依赖单语语料或平行语料的现有方法。

**[Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](distractor_gen_multiple_choice.md)**

:   提出选择题干扰项生成的三步流水线：(1) 训练配对排序器预测学生误选哪个干扰项；(2) 用排序器构造偏好数据集；(3) 用 DPO 训练生成器产生更具迷惑性的干扰项。在 CS 领域（Python/DB/ML）实验中，生成的干扰项更难以区分，且题目鉴别指数(DI)更高。

**[Divide-Then-Align: Honest Alignment based on the Knowledge Boundary of RAG](divide_then_align_rag_knowledge_boundary.md)**

:   DTA 提出将 RAG 查询按参数知识边界和检索知识边界划分为四个象限，对"两者都不知道"的查询构造偏好数据用 DPO 训练模型回答"我不知道"，解决了 RAFT 模型即使在检索完全噪声时也强行生成答案的问题，在准确率和适当弃权之间实现了有效平衡。

**[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](docagent_a_multi-agent_system_for_automated_code_documentation_generation.md)**

:   提出 DocAgent，一个基于拓扑依赖排序的多智能体代码文档生成系统，通过 Reader-Searcher-Writer-Verifier 协作流程增量构建上下文，在完整性、实用性和真实性三个维度上显著优于 FIM 和 Chat 基线。

**[DocMEdit: Towards Document-Level Model Editing](docmedit_towards_document-level_model_editing.md)**

:   首次提出文档级模型编辑任务，构建包含 37,990 条数据、105,652 个编辑事实的 DocMEdit 基准，揭示现有编辑方法在长上下文、多事实并行编辑场景下的严重不足。

**[DoMIX: An Efficient Framework for Exploiting Domain Knowledge in Fine-Tuning](domix_an_efficient_framework_for_exploiting.md)**

:   提出 DoMIX，将各领域知识用独立 LoRA 模块存储后通过对角初始化的 bridge 矩阵在微调时灵活组合利用，在持续领域适应预训练场景下减少 58% 预训练时间和 87% GPU 内存，同时性能超越 SOTA。

**[Don't Reinvent the Wheel: Efficient Instruction-Following Text Embedding based on Guided Space Transformation](dont_reinvent_the_wheel_efficient_instruction-following_text_embedding_based_on_.md)**

:   提出 GSTransform 框架，通过轻量级空间变换将预计算的通用嵌入实时适配到用户指令指定的语义空间，避免每次新指令都重新编码全部语料，在 9 个数据集上平均得分 66.01（SOTA 基线 55.31），同时实现 6~300 倍实时加速。

**[Principled Content Selection to Generate Diverse and Personalized Multi-Document Summaries](dpp_diverse_multidoc_summary.md)**

:   用行列式点过程（DPP）替代 LLM 的隐式内容选择来生成多样化多文档摘要——将任务分解为"提取原子关键点→DPP 选择多样子集→LLM 重写为摘要"三步，解决了 LLM 的"lost in the middle"问题，在 DiverseSumm 基准上一致提升了源覆盖率。

**[DREsS: Dataset for Rubric-based Essay Scoring on EFL Writing](dress_dataset_rubric_based_essay_scoring_efl_writing.md)**

:   发布 DREsS——一个面向 EFL（英语作为外语）写作教育的大规模标准化评分量规数据集（48.9K 样本），并提出基于文本损坏的 CASE 数据增强策略，将基线性能提升 45.44%。

**[DRS: Deep Question Reformulation With Structured Output](drs_deep_question_reformulation_with_structured_output.md)**

:   提出 DRS（Deep Question Reformulation with Structured Output），一种零样本方法，通过实体驱动的 DFS 搜索 + 结构化输出约束，将 GPT-3.5 的问题重构准确率从 23.03% 提升至 70.42%，使 LLM 能有效帮助用户将不可回答的问题转化为可回答的形式。

**[Divide-Then-Aggregate: An Efficient Tool Learning Method via Parallel Tool Invocation](dta_llama_parallel_tool_invocation.md)**

:   提出 DTA-Llama，将传统树搜索的串行工具调用路径转换为有向无环图（DAG）结构实现并行调用，设计 Process/Thread 推理框架使 LLM 在每轮中可分解任务并并行执行多个工具，在 StableToolBench 上使 Llama2-7B 达到 GPT-3.5 Parallel Function Calling 的水平。

**[An Effective Incorporating Heterogeneous Knowledge Curriculum Learning for Sequence Labeling](dual_stage_curriculum_learning_sequence_labeling.md)**

:   提出面向序列标注任务的双阶段课程学习（DCL）框架，通过数据级和模型级两阶段的由易到难训练策略以及基于贝叶斯不确定性的动态难度度量，在提升性能的同时加速训练超过 25%。

**[EcomScriptBench: A Multi-task Benchmark for E-commerce Script Planning via Step-wise Intention-Driven Product Association](ecomscriptbench.md)**

:   提出电商脚本规划（EcomScript）任务及其首个大规模benchmark EcomScriptBench（605K脚本、2.4M产品），通过购买意图（purchase intention）桥接用户行动步骤与产品检索的语义鸿沟，实验发现当前LLM在涉及产品的子任务上表现显著不足，注入意图知识可提升性能。

**[Efficient Knowledge Editing via Minimal Precomputation](efficient_knowledge_editing.md)**

:   证明了 MEMIT/ROME/EMMET 等知识编辑方法的预计算步骤（缓存 4400 万隐向量）可以减少到理论最小值的 2-10 倍（不到原来的 0.3%），将预计算时间从数十小时降到几分钟，且编辑性能基本无损。

**[Empaths at SemEval-2025 Task 11: Retrieval-Augmented Approach to Perceived Emotions Prediction](empaths_at_semeval-2025_task_11_retrieval-augmented_approach_to_perceived_emotio.md)**

:   提出 EmoRAG 系统，用检索增强生成（RAG）管道结合多 LLM 集成聚合，在 SemEval-2025 Task 11 多标签情感检测任务上无需额外训练即在 28 种语言中取得有竞争力的结果，平均 F1-micro 0.638。

**[Enhancing Conversational Agents with Theory of Mind: Aligning Beliefs, Desires, and Intentions for Human-Like Interaction](enhancing_conversational_agents_with_theory_of_mind_aligning_beliefs_desires_and.md)**

:   本文探索了从开源 LLM（LLaMA）内部表征中提取心智理论（ToM）相关信息的可行性，并利用 BDI（信念-愿望-意图）框架操纵这些表征来生成更符合人类社交认知的对话回复，ToM 对齐后的模型在 3B 和 8B 上分别达到 67% 和 63% 的胜率。

**[Enhancing Transformers for Generalizable First-Order Logical Entailment](enhancing_fol_entailment.md)**

:   系统性研究 Transformer 在一阶逻辑蕴涵任务中的泛化推理能力，揭示了查询语法、token 嵌入和 Transformer 架构（特别是位置编码）的影响，并提出 TEGA（Transformer Encoder with Guided Attention）在相对位置编码设定下显著提升逻辑推理性能。

**[Enhancing Marker Scoring Accuracy through Ordinal Confidence Modelling in Educational Assessments](enhancing_marker_scoring_accuracy_through_ordinal_confidence_modelling_in_educat.md)**

:   本文提出了一种基于核加权序数分类交叉熵（KWOCCE）的置信度建模方法，通过利用 CEFR 等级的序数结构和分数分箱策略，实现最高 47% 评分在 100% CEFR 一致性下释放，99% 在 ≥95% 一致性下释放，显著优于无置信度过滤时的约 92%。

**[Enhancing the Comprehensibility of Text Explanations via Unsupervised Concept Discovery](enhancing_the_comprehensibility_of_text_explanations_via_unsupervised_concept_di.md)**

:   提出 ECO-Concept 框架，通过 slot attention 机制自动提取文本概念，并利用 LLM 作为人类代理评估概念的可理解性，用可理解性反馈损失指导模型微调，在无概念标注的情况下实现了兼具高分类精度和人类可理解性的概念解释。

**[Entity Framing and Role Portrayal in the News](entity_framing_and_role_portrayal_in_the_news.md)**

:   本文构建了一个包含 5 种语言、1378 篇新闻文章、5800+ 实体标注的多语言层次化实体框架语料库，提出含 22 种精细角色的叙事角色分类体系（主角 / 反派 / 无辜者三大框架下），并在微调多语言 Transformer 和 LLM 层次零样本学习上建立了基准。

**[Entropy-UID: A Method for Optimizing Information Density](entropy-uid_a_method_for_optimizing_information_density.md)**

:   提出 Entropy-UID 方法，在自回归语言模型的解码过程中联合最小化熵和 surprisal 的加权组合，以实现信息密度的均匀分布。在 WikiText-2、OpenWebText 和 WMT 数据集上，该方法实现了最低的熵标准差（≈2.8）和稳定的 surprisal（≈5.7），优于单目标优化策略。

**[EpiCoDe: Boosting Model Performance Beyond Training with Extrapolation and Contrastive Decoding](epicode_boosting_model_performance_beyond_training_with_extrapolation_and_contra.md)**

:   提出 EpiCoDe，一种结合模型外推（Model Extrapolation）和对比解码（Contrastive Decoding）的无训练方法，在数据稀缺场景中通过参数空间外推和推理时logit差异对比来提升微调模型性能，并从logit误差角度给出了理论分析框架。

**[ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](etf_an_entity_tracing_framework_for_hallucination_detection_in_code_summaries.md)**

:   提出 Entity Tracing Framework (ETF)，一种通过静态程序分析提取代码实体、再用 LLM 验证这些实体在生成摘要中是否被正确描述的幻觉检测框架，配合首创的 CodeSumEval 数据集（~10K样本），在代码摘要幻觉检测上达到 73% F1。

**[Evaluating Design Decisions for Dual Encoder-based Entity Disambiguation](evaluating_design_decisions_for_dual_encoder-based_entity_disambiguation.md)**

:   系统评估了 Dual Encoder 在实体消歧（ED）任务中的关键设计选择（损失函数、相似度度量、标签语义化格式、负采样策略），并基于最优设计构建了 VerbalizED 系统，在 ZELDA 基准上达到了新的 SOTA，同时探索了一种迭代预测策略来利用已消歧的邻居实体改进困难样本。

**[Evaluating the Evaluation of Diversity in Commonsense Generation](evaluating_the_evaluation_of_diversity_in_commonsense_generation.md)**

:   对常识生成（GCR）任务中的12种多样性评估指标进行系统元评估，发现基于形式（n-gram）的指标在低质量生成上严重高估多样性，而基于内容（句子嵌入）的指标与人类判断一致性更高，推荐未来 GCR 研究使用 VS-Embed 或 Chamfer Distance 等内容级指标。

**[Explaining Matters: Leveraging Definitions and Semantic Expansion for Sexism Detection](explaining_matters_leveraging_definitions_and_semantic_expansion_for_sexism_dete.md)**

:   针对在线性别歧视检测中的数据稀疏和细粒度分类歧义问题，提出两种基于prompt的数据增强技术——定义驱动数据增强（DDA）利用类别定义生成语义对齐的合成样本，上下文语义扩展（CSE）通过分析模型错误的语义特征丰富训练数据——并结合 Mistral-7B 回退集成策略，在 EDOS 数据集上实现全任务 SOTA。

**[Model Extrapolation Expedites Alignment](expo_model_extrapolation.md)**

:   基于"对齐训练仅产生微小参数变化"的观察，提出ExPO方法——通过放大SFT→DPO的参数变化方向（$\theta_2 = \theta_1 + \alpha\Delta\theta$），在零额外训练开销下提升对齐性能，使仅训练20%步骤的DPO模型超越完整训练的版本。

**[FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation](faithfulrag_fact_level_conflict.md)**

:   发现现有忠实 RAG 方法通过强制抑制参数知识来实现上下文忠实，但这增加了误解上下文的风险（不忠实错误减少 6.65% 的同时错误匹配增加 6.42%）。提出 FaithfulRAG，通过事实级冲突识别（自事实挖掘）和冲突推理（自思考模块）解决知识冲突，在 FaithEval/SQuAD/MuSiQue/RealtimeQA 上超越最强基线 8-9 个百分点。

**[FastDraft: How to Train Your Draft](fastdraft_how_to_train_your_draft.md)**

:   提出 FastDraft，一套高效的 draft 模型预训练与对齐流程，可在24小时内用单节点8卡训练出约50M参数的 draft 模型，配合 Speculative Decoding 实现最高3倍内存带宽加速和2倍实际推理加速。

**[FCMR: Robust Evaluation of Financial Cross-Modal Multi-Hop Reasoning](fcmr_robust_evaluation_of_financial_cross-modal_multi-hop_reasoning.md)**

:   构建了金融领域跨模态多跳推理基准 FCMR，包含文本、表格和图表三种模态，分 Easy/Medium/Hard 三个难度等级，最强模型 Claude 3.5 Sonnet 在 Hard 级别仅达 30.4% 准确率，揭示了 MLLM 在信息检索阶段的关键瓶颈。

**[FEAT: A Preference Feedback Dataset through a Cost-Effective Auto-Generation and Labeling Framework for English AI Tutoring](feat_a_preference_feedback_dataset_through_a_cost-effective_auto-generation_and_.md)**

:   提出 FEAT 框架，通过 LLM 自动生成和标注教师反馈偏好数据集用于英语辅导系统，发现仅混入 5-10% 人工标注数据就能超越 100% 人工数据的排序性能。

**[Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients](federated_lora_heterogeneous.md)**

:   提出 LoRA-A²（Low Rank Adaptation with Alternating freeze and Adaptive rank selection），通过交替冻结 A/B 矩阵解决联邦 LoRA 聚合不一致问题，并结合自适应秩选择机制在大幅压缩上传参数量（最高减少 99.8%）的同时保持鲁棒性，尤其在低秩+高数据异构场景下显著优于现有方法。

**[FinanceReasoning: Benchmarking Financial Numerical Reasoning More Credible, Comprehensive and Challenging](financereasoning_benchmarking_financial_numerical_reasoning_more.md)**

:   提出 FinanceReasoning benchmark，通过重标注公开数据集、构建 3,133 个 Python 金融函数库和新增 908 道专家标注难题，在可信度、全面性和挑战性三个维度提升金融数值推理评估能力。

**[FlexRAG: A Flexible and Comprehensive Framework for Retrieval-Augmented Generation](flexrag_a_flexible_and_comprehensive_framework_for_retrieval-augmented_generatio.md)**

:   提出 FlexRAG，一个面向研究和原型开发的开源 RAG 框架，支持文本、多模态和 Web 检索三种模式，通过内存映射和异步处理实现比同类框架（FlashRAG）低一个数量级的资源开销。

**[Behind Closed Words: Creating and Investigating the forePLay Annotated Dataset for Polish Erotic Discourse](foreplay_polish_erotic_detection.md)**

:   构建了首个波兰语色情内容检测数据集 forePLay（24,768 句，5 类标签），提出涵盖模糊性、暴力和社会不可接受行为的多维标注体系，评估发现专用波兰语模型显著优于多语言模型，且 Transformer 编码器模型在不平衡类别处理上表现最强。

**[Frictional Agent Alignment Framework: Slow Down and Don't Break Things](frictional_agent_alignment.md)**

:   提出摩擦对齐框架 FAAF（Frictional Agent Alignment Framework），通过双策略（frictive state policy + intervention policy）目标函数，训练 LLM 在协作对话中识别信念冲突并生成促进反思与审议的"摩擦"干预，超越 DPO/IPO/PPO 等对齐方法。

**[GA-S3: Comprehensive Social Network Simulation with Group Agents](ga-s3_comprehensive_social_network_simulation_with_group_agents.md)**

:   提出基于"群体智能体"（Group Agent）的社交网络模拟系统 GA-S3，将具有相似行为的个体聚合为群体代理，通过层次化生成、马尔可夫网络推理和行为模块实现大规模社交网络的高效精确模拟。

**[GainRAG: Preference Alignment in Retrieval-Augmented Generation through Gain Signal Synthesis](gainrag_preference_alignment.md)**

:   发现 RAG 中检索器的"相关性"与 LLM 的"偏好"存在偏差——含正确答案的段落仍可能导致错误生成，而间接相关段落反而有用。提出 GainRAG，用基于对比解码困惑度的"增益"信号量化 LLM 偏好，训练轻量选择器在检索结果中选择真正有"增益"的段落，在 6 个 QA 数据集上显著超越 Standard RAG 和 Rerank 基线。

**[GaRAGe: A Benchmark with Grounding Annotations for RAG Evaluation](garage_a_benchmark_with_grounding_annotations_for_rag_evaluation.md)**

:   GaRAGe 是一个包含 2366 个问题和超过 35K 条人工标注 grounding 段落的 RAG 基准，通过细粒度的 grounding 相关性标注，系统评估 LLM 在 RAG 场景下识别相关信息、拒绝回答和归因引用的能力。

**[GeAR: Generation Augmented Retrieval](gear_generation_augmented_retrieval.md)**

:   GeAR 在传统 bi-encoder 检索框架上引入融合编码器和文本解码器，通过生成任务增强检索模型对文档内部细粒度语义的理解能力，同时不增加全局检索的计算开销。

**[Generating Synthetic Relational Tabular Data via Structural Causal Models](generating_synthetic_relational_tabular_data_via_structural_causal_models.md)**

:   本文扩展了 TabPFN 的基于结构因果模型（SCM）的合成数据生成方法，提出了一个能够生成多表关联（relational）合成表格数据的框架，通过耦合节点和隐因果关系实现跨表依赖建模。

**[Controllable and Reliable Knowledge-Intensive Task-Oriented Conversational Agents with Declarative Genie Worksheets](genie_worksheets_tod_agent.md)**

:   Genie 提出了一个可编程的知识密集型任务导向对话框架，通过声明式 Worksheet 规范定义 Agent 策略，将 LLM 限制在语义解析和回复生成两个角色，由算法化运行时系统强制执行策略，实现从 21.8% 到 82.8% 的真实任务完成率提升。

**[GeNRe: A French Gender-Neutral Rewriting System Using Collective Nouns](genre_a_french_gender-neutral_rewriting_system_using_collective_nouns.md)**

:   GeNRe 是首个法语性别中性重写系统，利用集体名词（collective nouns）替代阳性泛指（masculine generics），提出规则系统、微调模型和指令模型三种方案，其中规则系统和 Claude 3 Opus + 词典方案效果最好。

**[Graph-guided Cross-composition Feature Disentanglement for Compositional Zero-shot Learning](graph-guided_cross-composition_feature_disentanglement_for_compositional_zero-sh.md)**

:   DCDA 提出图引导的跨组合特征解耦方案，通过双适配器（L-Adapter 用于文本端 GNN 特征聚合、V-Adapter 用于视觉端跨注意力解耦）注入冻结 CLIP，在组合零样本学习任务上显著超越现有方法。

**[Guidelines for Fine-grained Sentence-level Arabic Readability Annotation](guidelines_for_fine-grained_sentence-level_arabic_readability_annotation.md)**

:   本文提出了 BAREC 语料库及其标注指南，这是一个拥有 69K+ 句子、覆盖 19 个可读性等级的大规模阿拉伯语句子级可读性评估资源，并在此基础上建立了自动可读性评估的基准模型。

**[Gumbel Reranking: Differentiable End-to-End Reranker Optimization](gumbel_reranking.md)**

:   将 RAG 系统中的重排序过程重新建模为文档级 Top-k 注意力掩码问题，利用 Gumbel 技巧和松弛 Top-k 采样实现端到端可微优化，直接最小化最终语言建模损失，在 HotpotQA 上 Recall@5 提升 10.4%。

**[Hanging in the Balance: Pivotal Moments in Crisis Counseling Conversations](hanging_in_the_balance_pivotal_moments_in_crisis_counseling_conversations.md)**

:   本文提出了一种无监督方法来检测对话中的"关键时刻"（pivotal moments）——即下一步回应可能极大影响对话结局的节点，并在危机心理咨询场景中验证了该方法的有效性。

**[Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems](hard_negative_mining_for_domain-specific_retrieval_in_enterprise_systems.md)**

:   本文提出了一种面向企业级领域特定检索的可扩展硬负样本挖掘框架，通过融合多种嵌入模型、PCA 降维和双语义条件筛选来动态选择高质量硬负样本，在内部云服务数据集和公开基准上均取得了显著提升。

**[HASH-RAG: Bridging Deep Hashing with Retriever for Efficient, Fine Retrieval and Augmented Generation](hash-rag_bridging_deep_hashing_with_retriever_for_efficient_fine_retrieval_and_a.md)**

:   Hash-RAG 将深度哈希技术系统集成到 RAG 框架中，实现了仅需传统方法 10% 检索时间的高效检索，并通过 Prompt-Guided Chunk-to-Context（PGCC）模块在保持效率的同时提升了生成质量。

**[HATA: Trainable and Hardware-Efficient Hash-Aware Top-k Attention for Scalable Large Model Inference](hata_trainable_and_hardware-efficient_hash-aware_top-k_attention_for_scalable_la.md)**

:   HATA 提出了一种将 learning-to-hash 技术集成到 top-k 注意力机制的方法，通过将查询和键映射为二进制哈希码来获取相对 qk 分数排序（而非绝对分数估计），在保持模型精度的同时实现了相对全注意力最高 7.2 倍的加速。

**[HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter](hateday_global_hate_speech.md)**

:   HateDay 构建了首个全球代表性仇恨言论数据集——24 万条随机采样的 Twitter 推文覆盖 8 种语言和 4 个英语国家，揭示了学术数据集大幅高估了检测模型在真实场景中的表现，尤其对非欧洲语言检测能力极差。

**[HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling](helpsteer3_human-annotated_feedback_and_edit_data_to_empower_inference-time_scal.md)**

:   NVIDIA 发布 HelpSteer3 数据集（7000+标注员、80+国家），训练专用的 Feedback 和 Edit 模型，在推理时通过"初始响应→反馈→编辑"循环实现开放域通用任务的推理时扩展，基于 Llama 3 系列 70B 模型在 Arena Hard 上达到 92.7 分，超越 OpenAI o1-preview (90.4) 和 DeepSeek R1 (92.3)。

**[Hierarchical Bracketing Encodings for Dependency Parsing as Tagging](hierarchical_bracketing_dep_parsing.md)**

:   提出层次化括号编码家族用于依存句法分析的序列标注范式，证明现有4-bit编码是该家族的非最优特例，推导出仅需12个标签的最优编码，并将其推广到处理任意非投射性。

**[Hierarchical Memory Organization for Wikipedia Generation](hierarchical_memory_wikipedia_gen.md)**

:   提出 Memory Organization-based Generation（MOG）框架，从网页文档中提取细粒度记忆单元（factoid），通过递归聚类-摘要算法组织为层次化 Wikipedia 大纲结构，使每个章节都有直接的记忆支撑，在 FreshWiki 和 WikiStart 数据集上信息量、引用率和可验证性全面超越 RAG 和 STORM 基线。

**[Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings](hierarchical_news_clustering.md)**

:   本文提出利用多语言 Matryoshka 嵌入的分层特性进行新闻文章聚类：低维捕捉主题级相似度、中维捕捉叙事级相似度、高维捕捉事件级相似度，结合改良的 RAC 层级聚类算法，在 SemEval 2022 Task 8 上达到 SOTA（Pearson ρ = 0.816）。

**[Counterspeech the Ultimate Shield! Multi-Conditioned Counterspeech Generation through Attributed Prefix Learning](hippro_counterspeech_gen.md)**

:   提出 HiPPrO 两阶段框架用于多条件反仇恨言论生成——第一阶段通过层次化前缀学习在多个属性（策略+情感）空间中优化反言论生成，第二阶段用无参考无奖励的偏好优化提升建设性，策略一致性提升 ~38%，ROUGE 指标提升 2-3%。

**[HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on Retrieval-Augmented Generation](hoh_a_dynamic_benchmark_for_evaluating_the_impact_of_outdated_information_on_ret.md)**

:   本文提出 HoH，首个专门评估过时信息对 RAG 系统影响的大规模动态基准，包含 96,124 个 QA 对和 219,463 篇文档，揭示了过时信息对 RAG 性能和安全性的严重危害。

**[HybGRAG: Hybrid Retrieval-Augmented Generation on Textual and Relational Knowledge Bases](hybgrag_hybrid_rag_skb.md)**

:   提出 HybGRAG 方法，通过检索器库（Retriever Bank）同时利用文本和关系信息，配合 Critic 模块的自反思迭代纠正问题路由错误，在半结构化知识库上的混合问答任务中 Hit@1 平均提升 51%。

**[Enhancing Hyperbole and Metaphor Detection with Their Bidirectional Dynamic Interaction and Emotion Knowledge](hyperbole_metaphor_detection.md)**

:   提出 EmoBi 框架，通过情感分析→情感引导的域映射→双向动态交互三阶段 prompting 流程，利用 LLM 挖掘夸张和隐喻背后的情感线索及二者的互促关系，在四个数据集上大幅超越 SoTA（TroFi 上夸张检测 F1 提升 28.1%，HYPO-L 上隐喻检测 F1 提升 23.1%）。

**[If Attention Serves as a Cognitive Model of Human Memory Retrieval, What is the Plausible Memory Representation?](if_attention_serves_as_a_cognitive.md)**

:   通过将 Transformer Grammar（TG）的注意力机制与人类阅读时间数据关联，首次证明在句法结构上操作的注意力比在 token 序列上操作的普通 Transformer 注意力能更好地预测人类阅读行为，揭示人类句子处理涉及"句法结构+词序列"的双重记忆表征。

**[If Attention Serves as a Cognitive Model of Human Memory Retrieval, What is the Plausible Memory Representation?](if_attention_serves_as_a_cognitive_model_of_human_memory_retrieval_what_is_the_p.md)**

:   本文探究 Transformer Grammar（TG）的注意力机制能否作为人类记忆检索的认知模型，通过 Normalized Attention Entropy（NAE）将模型与人类阅读时间关联，发现基于句法结构的注意力比基于 token 的注意力更能解释人类句子处理行为，且两者提供独立互补的贡献。

**[Predicting Implicit Arguments in Procedural Video Instructions](implicit_arguments_video_instructions.md)**

:   提出 Implicit-VidSRL 数据集与 iSRL-Qwen2-VL 模型，针对过程性视频指令中省略的隐含论元（食材成分）进行预测，通过 SRL 框架将多步指令分解为 {verb, what, where/with} 三元组，在银标数据上微调后在隐含论元 F1 上超越 GPT-4o 达 17%。

**[ImpliHateVid: Implicit Hate Speech Detection in Videos](implihatevid_video_hate.md)**

:   首次提出视频中隐性仇恨言论检测任务，构建2009个视频的ImpliHateVid数据集，并设计两阶段对比学习框架融合文本、图像、音频三模态特征。

**[Improve Rule Retrieval and Reasoning with Self-Induction and Relevance ReEstimate](improve_rule_retrieval_and_reasoning_with_self-induction_and_relevance_reestimat.md)**

:   针对规则检索中查询（具体实例化事实）与规则（抽象变量形式）之间的语义鸿沟，提出 SIAR（自归纳增强检索）和 R3（规则相关性重评估）两种方法，通过将查询映射到规则语义空间并重新评估规则相关性，显著提升规则检索和下游推理性能。

**[Improving Continual Pre-training Through Seamless Data Packing](improving_continual_pre-training_through_seamless_data_packing.md)**

:   提出 Seamless Packing (SP) 数据打包策略，通过两阶段方法——滑动窗口处理长文本 + FFD 算法打包短文本——在持续预训练中保持上下文连续性、最小化截断和填充，在 99% 的实验设置中超越基线方法。

**[Ewe: Improving Factuality with Explicit Working Memory](improving_factuality_with_explicit_working_memory.md)**

:   提出 Ewe（Explicit Working mEmory），在 LLM 解码过程中引入由多个 KV cache 单元组成的显式工作记忆，实时接收检索知识反馈和事实核查反馈，检测到错误时删除错误句子并用更新后的记忆重新生成，在 4 个事实性长文本生成基准上将 VeriScore F1 提升 2–6 分且不损失回答有用性。

**[Improving Language and Modality Transfer in Translation by Character-level Modeling](improving_language_and_modality_transfer_in.md)**

:   提出基于字符级编码器 charSONAR 的跨语言跨模态翻译方法，通过 teacher-student 训练获得字符级文本编码器，再用轻量适配器连接 1000+ 语言的 CTC ASR 模型（MMS），在 75 语言文本翻译和 33 语言语音翻译上实现 SOTA，零资源低资源场景表现尤其突出。

**[Inducing Lexicons of In-Group Language with Socio-Temporal Context](inducing_lexicons_of_in-group_language_with_socio-temporal_context.md)**

:   提出 LISTN（Lexicon Induction with Socio-Temporal Nuance）框架，利用动态词嵌入和用户嵌入联合建模社区语言的社会结构和时间演化，在反女性在线社区（manosphere）的群体内词汇归纳任务上达到 0.77 的平均精度，显著超越现有方法。

**[Inferring Functionality of Attention Heads from their Parameters](inferring_functionality_of_attention_heads_from_their_parameters.md)**

:   提出MAPS框架，通过将注意力头参数投影到词汇空间构建token映射矩阵$M$，无需任何推理或训练即可推断注意力头实现的功能，在6个LLM上验证了20种关系操作的映射准确性，并开发自动化pipeline发现了大量此前未被识别的注意力头功能。

**[InSerter: Speech Instruction Following with Unsupervised Interleaved Pre-training](inserter_speech_instruction.md)**

:   提出 InSerter（交错语音-文本预训练）方法，通过 TTS 将大规模文本语料合成为交错的语音-文本序列进行预训练，大幅提升 SpeechLLM 的语音指令遵循能力，并构建首个全面的语音指令遵循基准 SpeechInstructBench。

**[InspireDebate: Multi-Dimensional Evaluation-Guided Reasoning for Debating](inspiredebate_multidim_evaluation_debating.md)**

:   提出双组件框架：InspireScore（融合4个主观维度+2个客观维度的辩论评估系统）和 InspireDebate（通过CoT-SFT + 多维DPO + Web-RAG 三阶段优化的辩论框架），评估系统与专家判断相关性提高 44%，辩论性能超越基线 57%。

**[Instruction-Tuning Data Synthesis from Scratch via Web Reconstruction](instruction-tuning_data_synthesis_from_scratch_via_web_reconstruction.md)**

:   提出 Web Reconstruction (WebR)，一种从原始网页文档全自动合成高质量指令微调数据的框架，通过"Web作为指令"和"Web作为回复"双视角范式，无需人工标注即可生成优于现有SOTA的IT数据。

**[Intuitive Fine-Tuning: Towards Simplifying Alignment into a Single Process](intuitive_fine_tuning.md)**

:   通过MDP框架将SFT和偏好优化统一建模为"偏好估计+转移优化"两个子过程，揭示SFT本质上是偏好优化的特殊退化形式（使用偏差先验），提出IFT方法通过时间残差连接在仅使用SFT格式数据的条件下实现接近或超越SFT+PO顺序训练的对齐效果。

**[Investigating Language Preference of Multilingual RAG Systems](investigating_language_preference_of_multilingual_rag_systems.md)**

:   系统研究多语言RAG系统在检索和生成两个阶段的语言偏好问题，提出 MLRS 指标量化检索器语言偏好，并设计 DKM-RAG 框架通过融合翻译段落与模型内部知识来缓解偏好问题。

**[Investigating the Robustness of Retrieval-Augmented Generation at the Query Level](investigating_the_robustness_of_retrieval-augmented_generation_at_the_query_leve.md)**

:   系统研究 RAG 管道对查询级扰动（冗余插入、正式语气、歧义引入、拼写错误）的敏感性，提出解耦各模块鲁棒性的分析框架，发现检索器是性能瓶颈且不同扰动类型的主导因素不同。

**[IRIS: Interactive Research Ideation System for Accelerating Scientific Discovery](iris_interactive_research_ideation_system_for_accelerating_scientific_discovery.md)**

:   提出 IRIS，一个开源的交互式研究构思系统，通过蒙特卡洛树搜索（MCTS）扩展测试时计算、细粒度反馈机制和基于查询的文献综合，实现人机协作的科学假设生成。

**[Is Linguistically-Motivated Data Augmentation Worth It?](is_linguistically-motivated_data_augmentation_worth_it.md)**

:   系统比较语言学驱动和非语言学（随机扰动）数据增强策略在两种低资源语言上的效果，发现语言学方法仅在生成的样本接近训练数据分布时才有优势，否则可能有害。

**[It's Not a Walk in the Park! Challenges of Idiom Translation in Speech-to-text Systems](its_not_a_walk_in_the_park_challenges_of_idiom_translation_in_speech-to-text_sys.md)**

:   本文首次系统比较了语音到文本翻译（SLT）、文本机器翻译（MT）和大语言模型（LLM）在习语翻译任务上的表现，发现 SLT 系统在处理习语时性能大幅下降，即便在编码器高层仍倾向于字面翻译，而 MT 和 LLM 对习语的处理能力明显更优。

**[KITAB-Bench: A Comprehensive Multi-Domain Benchmark for Arabic OCR and Document Understanding](kitab-bench_a_comprehensive_multi-domain_benchmark_for_arabic_ocr_and_document_u.md)**

:   KITAB-Bench 是一个涵盖 9 大领域 36 个子领域共 8,809 个样本的综合性阿拉伯语 OCR 基准，评估结果显示现代视觉语言模型（如 GPT-4o、Gemini）在字符错误率上平均超过传统 OCR 方法 60%，但在 PDF-to-Markdown 转换中最优模型仅达到 65% 准确率，凸显了阿拉伯语文档理解的巨大挑战。

**[Know You First and Be You Better: Modeling Human-Like User Simulators via Implicit Profiles](know_you_first_and_be_you_better_modeling_human-like_user_simulators_via_implici.md)**

:   本文提出 USP（User Simulator with Implicit Profiles）框架，通过从人机对话中提取隐式用户画像，并结合条件监督微调和基于循环一致性的强化学习，在真实性、一致性和多样性三个维度上显著超越基线方法，语义相似度和风格相似度分别提升约 34% 和 43%。

**[Know Your Mistakes: Towards Preventing Overreliance on Task-Oriented Conversational AI Through Accountability Modeling](know_your_mistakes_towards_preventing_overreliance_on_task-oriented_conversation.md)**

:   本文提出面向任务型对话系统的 Accountability Model，在 LLM 中加入额外的 accountability head 作为二分类器预测对话状态中各 slot 的概率，从而检测并自校正假阳性和假阴性错误，在 MultiWOZ 上将 JGA 从 64.34 提升到 70.51（↑9.6%），达到 SOTA。

**[KnowShiftQA: How Robust are RAG Systems when Textbook Knowledge Shifts in K-12 Education?](knowshiftqa_rag_knowledge_shifts.md)**

:   构建了 KnowShiftQA 数据集（3,005 道题，覆盖 5 个学科），通过假设性知识更新模拟教科书与 LLM 参数知识的差异，系统评估 RAG 系统面对知识偏移时的鲁棒性，发现现有 RAG 系统在知识偏移下性能下降 22-27%。

**[KodCode: A Diverse, Challenging, and Verifiable Synthetic Dataset for Coding](kodcode_a_diverse_challenging_and_verifiable_synthetic_dataset_for_coding.md)**

:   KodCode 提出一套三阶段合成数据管线（编程题目合成→解决方案+单元测试自验证→后训练数据合成），构建了 447K 经过验证的编程 question-solution-test 三元组，微调后的模型在 HumanEval、MBPP、BigCodeBench、LiveCodeBench 等基准上超越 Qwen2.5-Coder-32B-Instruct 和 DeepSeek-R1-Distill-Llama-70B。

**[KokoroChat: A Japanese Psychological Counseling Dialogue Dataset Collected via Role-Playing by Trained Counselors](kokorochat_a_japanese_psychological_counseling_dialogue.md)**

:   提出 KokoroChat，一个通过训练有素的咨询师角色扮演收集的日语心理咨询对话数据集，包含 6,589 段长对话及详细的客户反馈评分，用于提升 LLM 的心理咨询回复生成和对话评估能力。

**[LADDER: Language-Driven Slice Discovery and Error Rectification in Vision Classifiers](ladder_language-driven_slice_discovery_and_error_rectification_in_vision_classif.md)**

:   提出 LADDER 框架，利用 LLM 的推理能力和潜在领域知识，通过分析文本（图像描述/医学报告/元数据）自动发现视觉分类器中的系统性偏差切片（error slices），并通过伪标签生成和属性重平衡实现无需标注的多偏差缓解。

**[LangMark: A Multilingual Dataset for Automatic Post-Editing](langmark_a_multilingual_dataset_for_automatic_post-editing.md)**

:   发布 LangMark——一个包含 206,983 个三元组、覆盖英语到七种语言的大规模多语言自动后编辑（APE）数据集，并证明 LLM 配合 few-shot prompting 能有效改善专有 NMT 引擎的输出质量。

**[LAQuer: Localized Attribution Queries in Content-grounded Generation](laquer_localized_attribution.md)**

:   提出 Localized Attribution Queries (LAQuer) 任务——将生成文本中用户选定的片段精确定位到源文档的对应片段，实现比句子级归因更精细、比子句级归因更用户导向的溯源，在多文档摘要和长文本问答上显著减少了归因文本长度。

**[LDIR: Low-Dimensional Dense and Interpretable Text Embeddings with Relative Representations](ldir_low-dimensional_dense_and_interpretable_text_embeddings_with_relative_repre.md)**

:   提出 LDIR 方法，通过最远点采样选取锚文本（anchor texts），计算待编码文本与各锚文本的语义相关度，构建低维（≤500 维）、稠密且可解释的文本嵌入，性能接近黑盒模型并显著优于已有可解释嵌入方法。

**[Learning to Align Multi-Faceted Evaluation: A Unified and Robust Framework](learning_to_align_multi-faceted_evaluation_a_unified_and_robust_framework.md)**

:   提出 ARJudge 评估框架，通过微调 Analyzer 自适应生成评估标准并执行文本+代码双驱动分析，配合无需微调的 Refiner 综合判断，在多个评估基准上超越现有微调评估器，尤其在指令遵循评估上通过代码驱动分析提升高达 11.1%。

**[Length-Induced Embedding Collapse in PLM-based Models](length-induced_embedding_collapse_in_plm-based_models.md)**

:   发现并严格证明了 PLM 文本嵌入模型中的"长度坍缩"现象——长文本嵌入趋于聚集，源于 self-attention 作为低通滤波器随文本长度增加而滤波率增强，高频信息被过度抑制；提出 TempScale 方法通过降低 attention 温度来缓解长短文本嵌入分布差异，在 MTEB 上提升 0.94%、LongEmbed 上提升 1.10%。

**[Limited Generalizability in Argument Mining: State-Of-The-Art Models Learn Datasets, Not Arguments](limited_generalizability_in_argument_mining_state-of-the-art_models_learn_datase.md)**

:   对 4 种 Transformer 模型在 17 个英语句子级论辩挖掘数据集上进行首次大规模跨数据集泛化评估，发现 SOTA 模型主要学到了数据集特有的词汇模式而非论辩的结构性信号，泛化能力远低于基准表现，但任务相关预训练和联合数据训练可部分缓解这一问题。

**[Literature Meets Data: A Synergistic Approach to Hypothesis Generation](literature_meets_data_hypothesis.md)**

:   提出首个将文献驱动和数据驱动假设生成进行协同整合的方法，通过 Refinement 和 Union 两种策略让 LLM 从论文摘要和观测数据中联合生成更具泛化性的假设，在五个社会科学分类任务的 OOD 数据集上比纯数据驱动方法平均提升 3.37%，并首次通过人类实验证明 LLM 生成的假设能显著改善人类决策准确率（+7.44% / +14.19%）。

**[Logical Consistency is Vital: Neural-Symbolic Information Retrieval for Negative-Constraint Queries](logical_consistency_is_vital_neural-symbolic_information_retrieval_for_negative-.md)**

:   提出 NS-IR，通过将自然语言查询和文档转换为一阶逻辑（FOL），利用逻辑对齐和连接词约束两项技术优化稠密检索嵌入，显著提升了负约束查询等复杂逻辑检索场景的性能。

**[LoGU: Long-form Generation with Uncertainty Expressions](logu_longform_gen_uncertainty.md)**

:   定义"长文本不确定性生成"（LoGU）任务，识别不确定性抑制和不确定性错位两个子挑战，提出基于分解的数据构造框架和 SFT+DPO 两阶段训练流水线，使 LLM 在长文本生成中对不确定事实显式表达不确定性，在三个数据集上将 Llama3-8B 的事实准确率从 51.9% 提升到 71.6%，错误声明数从 20.4 降到 5.81。

**[Low-Rank Interconnected Adaptation across Layers](low-rank_interconnected_adaptation_across_layers.md)**

:   提出 Lily（Low-rank Interconnected Adaptation across Layers），通过将 LoRA 的 A/B 适配器跨层解耦并互联共享，配合数据依赖的路由机制，在相同或更少参数下实现高秩权重更新，在多模态、多架构、多规模场景中均优于 LoRA。

**[Read it in Two Steps: Translating Extremely Low-Resource Languages with Code-Augmented Grammar Books](low_resource_translation.md)**

:   将语法书辅助的极低资源翻译（XLR MT）分解为语法规则检索和规则应用两步，并提出用代码格式表示语法规则以提升 LLM 在两步中的表现，在壮语翻译上实现了 13.1% BLEU 的提升。

**[M3FinMeeting: A Multilingual, Multi-Sector, and Multi-Task Financial Meeting Understanding Evaluation Dataset](m3finmeeting_a_multilingual_multi-sector_and_multi-task_financial_meeting_unders.md)**

:   构建了 M3FinMeeting——首个面向金融会议的多语言（中英日）、多行业、多任务评测基准，包含 600 场真实金融会议的摘要、QA 对抽取和问答三项任务，揭示了当前最先进 LLM 在金融会议理解上仍有显著提升空间。

**[Mamba Knockout for Unraveling Factual Information Flow](mamba_knockout_for_unraveling_factual_information_flow.md)**

:   将 Transformer 上的 Attention Knockout 可解释性方法迁移至 Mamba-1 和 Mamba-2，揭示了 SSM 模型中事实信息的流动模式——发现 Mamba 与 Transformer 共享"主语 token 在中后层向最后 token 传递关键信息"的普遍模式，但在首 token 偏置和关系 token 依赖等方面存在架构特异性差异。

**[MapQaTor: An Extensible Framework for Efficient Annotation of Map-Based QA Datasets](mapqator_an_extensible_framework_for_efficient_annotation_of_map-based_qa_datase.md)**

:   提出 MapQaTor——一个可扩展的开源 Web 框架，通过集成多种地图 API（Google Maps、OpenStreetMap 等），将地理空间 QA 数据集的标注速度提升至少 30 倍，同时通过 API 响应缓存确保数据可复现性。

**[Maximal Matching Matters: Preventing Representation Collapse for Robust Cross-Modal Retrieval](maximal_matching_matters_preventing_representation_collapse_for_robust_cross-mod.md)**

:   提出 MaxMatch 方法，通过基于匈牙利算法的最大配对相似度和两个新损失函数，解决集合嵌入方法中的稀疏监督和集合坍塌问题，在 MS-COCO 和 Flickr30k 上取得 SOTA 性能。

**[MDBench: A Synthetic Multi-Document Reasoning Benchmark Generated with Knowledge Guidance](mdbench_a_synthetic_multi-document_reasoning_benchmark_generated_with_knowledge_.md)**

:   提出 MDBench，一个通过「结构化知识→LLM 辅助增强→自然文本生成」管线合成的多文档推理 QA 基准，可控地注入跨文档依赖，对前沿 LLM 构成显著挑战（最佳模型 EM 仅~60%）。

**[MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](memerag_a_multilingual_end-to-end_meta-evaluation_benchmark_for_retrieval_augmen.md)**

:   构建首个原生多语言 RAG 元评估基准 MEMERAG，覆盖 5 种语言，通过流程图引导的标注达到高标注者一致性，用于评估和比较多语言 RAG 自动评估器。

**[Memorization: A Close Look at Books](memorization_a_close_look_at_books.md)**

:   系统研究 Llama 3 系列模型对完整书籍的记忆化程度，发现书籍提取率与其流行度（训练数据重复度代理）高度正相关，并通过 LoRA 微调揭示指令微调的抗反刍缓解措施仅涉及极少量集中在底层 transformer block 的权重变化。

**[Meta-Learning Neural Mechanisms rather than Bayesian Priors](meta-learning_neural_mechanisms_rather_than_bayesian_priors.md)**

:   挑战了"元学习在神经网络中蒸馏贝叶斯简单性先验"的主流观点，通过形式语言实验证明元学习实际上是在模型中植入有用的**神经机制**（如计数器），而非学习简单性偏好。

**[Micro-Act: Mitigate Knowledge Conflict in QA via Actionable Self-Reasoning](micro_act_knowledge_conflict_reasoning.md)**

:   提出 Micro-Act 框架，通过层次化动作空间（导航/功能/桥接动作）和自适应粒度分解，让 LLM 自动感知上下文复杂度并逐层拆解知识对比，在 5 个知识冲突基准上全面超越 SOTA，同时在无冲突场景下也保持鲁棒。

**[MindRef: Mimicking Human Memory for Hierarchical Reference Retrieval with Fine-Grained Location Awareness](mindref_mimicking_human_memory_hierarchical_reference_retrieval.md)**

:   提出 MindRef 框架，模拟人类先回忆文档标题再定位具体段落的两阶段记忆模式，通过 Trie 和 FM-Index 约束解码让 LLM 独立召回参考段落，无需额外检索模型或预分段。

**[Mitigating Confounding in Speech-Based Dementia Detection through Weight Masking](mitigating_confounding_in_speech-based_dementia_detection_through_weight_masking.md)**

:   本文针对基于语音转录文本的痴呆检测任务中的**性别混淆偏差**问题，提出两种权重掩码方法（Extended Confounding Filter 和 Dual Filter），通过识别并消除 Transformer 网络中与性别关联的权重来实现去混淆，在保持痴呆检测性能的同时显著降低性别间的公平性差距。

**[Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints](mitigating_negative_interference_in_multilingual_sequential_knowledge_editing_th.md)**

:   本文提出 LangEdit 框架，通过将每种语言的参数更新投影到先前编辑语言的零空间上，实现多语言序列知识编辑中不同语言更新之间的数学隔离，有效缓解负干扰并保持多语言泛化能力。

**[InterpoLL: Mitigating Shortcut Learning with InterpoLated Learning](mitigating_shortcut_learning_with_interpolated_learning.md)**

:   提出 InterpoLL，通过将多数样本的表征与同类少数样本的表征做插值 $z_i = (1-\lambda)f_{enc}(x_i) + \lambda f_{enc}(x_j)$ 来弱化捷径特征影响，在 MNLI/FEVER/QQP 等 NLU 任务上少数样本泛化显著超越 ERM 和 SOTA 捷径缓解方法，且不损失多数样本准确率。

**[MLDebugging: Towards Benchmarking Code Debugging Across Multi-Library Scenarios](mldebugging_towards_benchmarking_code_debugging_across_multi-library_scenarios.md)**

:   本文提出 MLDebugging——首个面向**多库 Python 代码调试**的综合基准，涵盖 126 个 Python 库和 7 种 bug 类型（共 1175 个样本），系统评估主流开源和闭源 LLM 在多库调试场景下的能力，发现当前 LLM 在此任务上仍有很大提升空间。

**[MockConf: A Student Interpretation Dataset: Analysis, Word- and Span-level Alignment and Baselines](mockconf_a_student_interpretation_dataset_analysis_word-_and_span-level_alignmen.md)**

:   本文构建了 MockConf——一个以捷克语为中心的**学生同声传译数据集**（7 小时，5 种欧洲语言），提供人工标注的 span 级和 word 级对齐，同时发布了专用标注工具 InterAlign，并建立了自动对齐的基线和评估指标体系。

**[Modular Sentence Encoders: Separating Language Specialization from Cross-Lingual Alignment](modular_sentence_encoders.md)**

:   本文提出模块化多语言句子编码器训练方案：先训练语言特定模块（embedding + 语言适配器 + 句子编码适配器）缓解多语言诅咒，再训练跨语言对齐适配器同时使用平行和释义数据解决不同跨语言任务间的性能权衡，在 4 个任务和 23 种语言上全面优于单体模型训练。

**[Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](monitoring_decoding_mitigating_hallucination_via_evaluating_the_factuality_of_pa.md)**

:   提出 Monitoring Decoding (MD) 框架，在生成过程中动态监控部分响应的事实性，通过监控函数识别易产生幻觉的 token 并利用树搜索策略选择性地修正这些关键 token，从而在保持效率的同时显著提升事实准确性。

**[MoRE: A Mixture of Low-Rank Experts for Adaptive Multi-Task Learning](more_a_mixture_of_low-rank_experts_for_adaptive_multi-task_learning.md)**

:   提出 MoRE (Mixture of Low-Rank Experts)，将 LoRA 中的不同秩视为不同专家，通过自适应秩选择器为每个任务动态选择最合适的秩，配合对比学习优化的任务嵌入和平衡数据采样策略，使用单个 LoRA 模块实现高效的多任务微调。

**[MOSAIC: Multiple Observers Spotting AI Content](mosaic_multiple_observers_spotting_ai_content.md)**

:   基于信息论中的通用压缩原理，提出 MOSAIC——多 LLM 集成的 AI 生成文本检测方法，通过 Blahut-Arimoto 算法为多个 detector LLM 计算最优组合权重，构建混合分布作为观察者，比较文本的实际 surprisal 与混合模型的期望交叉熵差异来判断是否为 AI 生成，在多个域/语言/生成器上鲁棒优于单模型和双模型（如 Binoculars）方法。

**[MT-RAIG: Novel Benchmark and Evaluation Framework for Retrieval-Augmented Insight Generation over Multiple Tables](mt-raig_novel_benchmark_and_evaluation_framework_for_retrieval-augmented_insight.md)**

:   提出MT-RAIG Bench——首个面向多表格检索增强洞察生成的大规模基准，以及MT-RAIG Eval——基于分解的细粒度自动评估框架，实验表明即使前沿LLM在多表格推理上仍表现不佳（忠实度仅约40%，完整度约60%）。

**[Multi-Agent Collaboration via Cross-Team Orchestration](multi-agent_collaboration_via_cross-team_orchestration.md)**

:   提出 Cross-Team Orchestration (Croto)，一个可扩展的多团队协作框架，通过将多个独立 agent 团队组织起来进行跨团队交互，利用层次化分组 (Hierarchy Partitioning) 和贪心聚合 (Greedy Aggregation) 机制将各团队的多样化解决方案融合为更优结果。

**[Multi-Hop Question Generation via Dual-Perspective Keyword Guidance](multi-hop_question_generation_via_dual-perspective_keyword_guidance.md)**

:   定义了双视角关键词——问题关键词（捕捉提问者意图）和文档关键词（反映 QA 对相关内容），并提出 DPKG 框架，通过扩展 Transformer 编码器和两个答案感知解码器，将关键词无缝集成到多跳问题生成过程中。

**[Multilingual Retrieval Augmented Generation for Culturally-Sensitive Tasks: A Benchmark for Cross-lingual Robustness](multilingual_retrieval_augmented_generation_for_culturally-sensitive_tasks_a_ben.md)**

:   构建了 BordIRLines 基准数据集，包含 49 种语言的领土争端查询及配对的 Wikipedia 检索文档，系统评估了多语言 RAG 环境下的跨语言鲁棒性，发现**检索多语言文档能比仅检索同语言文档更好地提高响应一致性并减少地缘政治偏差**。

**[Data Quality Issues in Multilingual Speech Datasets: The Need for Sociolinguistic Awareness and Proactive Language Planning](multilingual_speech_data_quality.md)**

:   对三大公开多语言语音数据集（Common Voice、FLEURS、VoxPopuli）进行系统质量审计，发现低资源语言存在严重的微观和宏观质量问题，并提出基于社会语言学意识的数据集创建指南。

**["My life is miserable, have to sign 500 autographs everyday": Exposing Humblebragging, the Brags in Disguise](my_life_is_miserable_have_to_sign_500_autographs_everyday_exposing_humblebraggin.md)**

:   首次将 humblebragging（谦虚式自夸）检测引入计算语言学领域，提出了一个4元组形式化定义，构建了 HB-24 合成数据集，并在 ML/DL/LLM 上进行了全面基准评估，GPT-4o 在 zero-shot+定义 设定下达到 0.88 F1，超越人类标注者。

**[Narrative Media Framing in Political Discourse](narrative_media_framing_in_political_discourse.md)**

:   将叙事学理论与媒体框架分析相结合，提出了包含角色（英雄/反派/受害者）、冲突/解决、文化故事三个结构化组件的叙事框架分析体系，在气候变化和 COVID-19 两个领域验证了该框架的有效性和可迁移性。

**[Unifying Continuous and Discrete Text Diffusion with Non-simultaneous Diffusion Processes](neodiff_unified_text_diffusion.md)**

:   提出 NeoDiff，通过引入"外在时间"（句子级扩散进度）和"内在时间"（token 级扩散进度）的双时间框架，利用 Poisson 过程为每个 token 独立分配细粒度噪声水平，并用上下文感知的时间预测器自适应调节去噪进度，统一了离散和连续文本扩散模型的理论框架，在机器翻译、复述、文本简化等多个任务上超越现有扩散基线。

**[Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](neuron_empirical_gradient_discovering_and_quantifying_neurons_global_linear_cont.md)**

:   揭示了预训练语言模型 FF 层神经元激活值与模型输出之间存在全局线性关系，提出了神经元经验梯度（NEG）来量化这种线性关系，并设计了高效估算方法 NeurGrad，最终通过技能神经元探测实验证明 NEG 能有效表征多种语言技能。

**[Normalized AOPC: Fixing Misleading Faithfulness Metrics for Feature Attribution Explainability](normalized_aopc_faithfulness_metrics.md)**

:   本文揭示了广泛使用的 AOPC（扰动曲线下面积）忠实度指标在跨模型比较时会产生误导性结论（因为不同模型的 AOPC 上下界差异巨大），提出 Normalized AOPC (NAOPC) 通过 min-max 归一化消除模型间的不可比性，实验表明归一化可以根本性地改变模型忠实度排名。

**[On-Policy Self-Alignment with Fine-grained Knowledge Feedback for Hallucination Mitigation](on-policy_self-alignment_with_fine-grained_knowledge_feedback_for_hallucination_.md)**

:   提出 RLFH（Reinforcement Learning for Hallucination），一种在策略（on-policy）自对齐方法，让 LLM 自己作为评判者，将回复分解为原子事实并进行真实性和信息量评估，生成 token 级别的密集奖励信号，通过在线 PPO 优化来有效缓解幻觉问题。

**[One for All: Update Parameterized Knowledge Across Multiple Models with Once Edit](one_for_all_update_parameterized_knowledge_across_multiple_models_with_once_edit.md)**

:   提出 OnceEdit，通过编辑一个轻量级插件模型并利用异构模型集成技术将编辑后的知识迁移到多个 LLM，实现"一次编辑，多模型更新"，在 ZsRE 和 Counterfact 数据集上显著超越现有方法。

**[Optimized Text Embedding Models and Benchmarks for Amharic Passage Retrieval](optimized_text_embedding_models_and_benchmarks_for_amharic_passage_retrieval.md)**

:   针对低资源、形态丰富的阿姆哈拉语（Amharic），提出基于预训练 Amharic BERT/RoBERTa 的稠密检索模型和 ColBERT 晚期交互模型，在参数量远小于多语言基线的情况下大幅提升段落检索效果，并建立了该语言首个系统性检索基准。

**[Enhancing Automated Interpretability with Output-Centric Feature Descriptions](output_centric_interpretability.md)**

:   提出两种以输出为中心的特征描述方法（VocabProj 和 TokenChange），弥补现有基于输入激活的自动可解释性流程只能捕获"什么激活了特征"而忽略"特征如何影响输出"的缺陷，并证明输入+输出方法的集成能生成最忠实的特征描述。

**[Pap2Pat: Benchmarking Outline-Guided Long-Text Patent Generation with Patent-Paper Pairs](pap2pat_benchmarking_outline-guided_long-text_patent_generation_with_patent-pape.md)**

:   构建了包含 1.8k 专利-论文配对的 Pap2Pat 基准，提出基于大纲的分块专利描述生成方法 COPGen，并设计了基于 NLI 的事实性/覆盖率/风格评估指标，系统评测了当前 LLM 在超长专利文档生成上的能力与不足。

**[Towards Better Evaluation for Generated Patent Claims](patclaimeval_patent_evaluation.md)**

:   提出首个专利权利要求评估基准 Patent-CE（1228 个专家标注的比较评估数据点）和专用评估方法 PatClaimEval（基于 Longformer + 对比学习变体），在特征完整性、概念清晰度、术语一致性、逻辑连接和整体质量五个维度上与人类专家评估的相关性全面超越 13 种现有指标（包括 G-Eval-4），整体质量维度的 Spearman 提升 58%。

**[PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data](personabench_evaluating_ai_models_on_understanding_personal_information_through_.md)**

:   提出一套合成数据生成管线，创建包含多样化用户画像和模拟私有文档（对话记录、AI 交互、购买历史）的 PersonaBench 基准，用于评估 AI 模型从嘈杂用户数据中提取个人信息的能力，实验表明当前 RAG 方案远不能胜任这一任务。

**[PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants](personalens_a_benchmark_for_personalization_evaluation_in_conversational_ai_assi.md)**

:   提出 PersonaLens，一个面向任务导向型 AI 助手个性化能力的综合评测基准，包含 1500 个丰富用户画像、20 个领域 111 个任务、用户模拟 Agent 和 Judge Agent，通过大规模自动化评估揭示当前 LLM 助手在个性化方面的显著不足。

**[Personalized Generation In Large Model Era A Survey](personalized_generation_in_large_model_era_a_survey.md)**

:   首篇跨模态个性化生成（PGen）综合综述，提出统一的用户中心视角将 NLP/CV/IR 社区的研究纳入一个框架，系统化梳理了文本/图像/视频/音频/3D/跨模态六大模态下的个性化技术、数据集和评估指标，涵盖 200+ 篇文献，并指出可扩展性、偏好演化、隐私公平等关键挑战。

**[All That Glitters is Not Novel: Plagiarism in AI Generated Research](plagiarism_ai_generated_research.md)**

:   在对自主科研 Agent（如 AI Scientist）生成的研究文档进行专家审查后发现，24% 的文档是"智能剽窃"——方法论与已有工作一一对应但不引用原始来源，且现有剽窃检测工具无法识别这种"改头换面"的抄袭。

**[Preventing Rogue Agents Improves Multi-Agent Collaboration](preventing_rogue_agents_improves_multi-agent_collaboration.md)**

:   提出一种通过实时监控 Agent 不确定性来检测"失控 Agent"（rogue agent）并进行干预的框架，在自建的 WhoDunitEnv 多智能体协作环境以及代码生成和资源可持续性任务上分别取得高达 17.4%、2.5% 和 20% 的性能提升。

**[Principled Understanding of Generalization for Generative Transformer Models in Arithmetic Reasoning Tasks](principled_generalization_arithmetic.md)**

:   建立首个统一理论框架来理解 Transformer 在算术任务（加法/乘法/模运算）上的泛化行为——从任务性质（平移不变性）和位置编码类型（APE/RPE）的交互出发，解释了之前困扰领域的多个泛化谜题（如加法能泛化但乘法不能，模100能泛化但模101不能），实验验证了理论预测。

**[PRISM: A Framework for Producing Interpretable Political Bias Embeddings](prism_political_bias_embeddings.md)**

:   提出PRISM框架——首个专为政治偏见嵌入设计的方法，通过争议性话题偏见指标挖掘和Cross-Encoder政治偏见评分两阶段，生成可解释的偏见感知嵌入，在政治偏见分类上超越通用文本嵌入模型。

**[Substance over Style: Evaluating Proactive Conversational Coaching Agents](proactive_conversational_coaching.md)**

:   通过健康教练领域的专家访谈和用户研究（31 名参与者、155 段对话），系统评估了五种不同对话风格（Directive、Interrogative、Facilitative）的 LLM 教练 Agent，发现用户高度重视核心功能性（substance）而对缺乏功能性时的风格修饰（style）持负面态度，同时揭示了用户第一人称评价与专家/LLM 第三方评价之间的显著不一致。

**[Probing Subphonemes in Morphology Models](probing_subphonemes_in_morphology_models.md)**

:   本文提出了一种语言无关的探测方法，研究在形态学变形任务上训练的 Transformer 模型如何隐式习得音韵特征，发现局部特征（如末辅音清化）在音素嵌入中编码良好，而长距离依赖（如元音和谐）在编码器层的上下文化表示中更显著。

**[ProxAnn: Use-Oriented Evaluations of Topic Models and Document Clustering](proxann_topic_model_eval.md)**

:   ProxAnn 设计了一个面向实际使用场景的主题模型/文档聚类评估协议——标注者先从模型输出推断类别再将类别应用到新文档——并证明 LLM 代理标注者可以统计不可分辨地替代人类标注者，同时发现经典 LDA 在此评估下表现不弱于现代方法。

**[Uncovering Visual-Semantic Psycholinguistic Properties from the Distributional Structure of Text Embedding Space](psycholinguistic_visual_semantic.md)**

:   提出 Neighborhood Stability Measure (NSM)，仅通过文本嵌入空间中邻域的"尖锐度"来无监督估计词汇的可意象性(imageability)和具体性(concreteness)，无需视觉模态或生成模型即可超越现有方法。

**[PVP: An Image Dataset for Personalized Visual Persuasion with Persuasion Strategies, Viewer Characteristics, and Persuasiveness Ratings](pvp_an_image_dataset_for_personalized.md)**

:   构建了首个大规模个性化视觉说服数据集 PVP（28,454 张图像、596 条消息、9 种说服策略、2,521 位标注者的心理特征），并提出说服图像生成和评估两个任务，发现融入观看者的心理特征能显著提升说服图像的生成和评估效果。

**[Q2E: Query-to-Event Decomposition for Zero-Shot Multilingual Text-to-Video Retrieval](q2e_query-to-event_decomposition_for_zero-shot_multilingual_text-to-video_retrie.md)**

:   Q2E 提出了一种零样本的查询到事件分解方法，利用 LLM 和 VLM 的参数化世界知识将简单查询分解为前因/当前/后果事件，并结合视频的视觉描述和语音转录，通过逆熵融合排序实现 SOTA 的多语言文本到视频检索性能。

**[QG-SMS: Enhancing Test Item Analysis via Student Modeling and Simulation](qg-sms_enhancing_test_item_analysis_via_student_modeling_and_simulation.md)**

:   QG-SMS 提出用单个 LLM 模拟不同理解水平的学生群体，通过学生画像生成、表现预测和分析三步流程，弥补了现有 LLM 评估器在考后分析维度（题目难度、区分度、干扰项效率）上的严重不足，在多个数据集上实现了最高一致性准确率。

**[Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](quantifying_lexical_semantic_shift_via_unbalanced_optimal_transport.md)**

:   将 Unbalanced OT 应用于上下文化词嵌入来量化词义变迁，提出 Sense Usage Shift (SUS) 指标在每个用法实例级别量化语义变化（义项使用频率增减），统一解决实例级变化检测、词级变化幅度量化、词义扩展/缩小判定。

**[Rank, Chunk, and Expand: Lineage-Oriented Reasoning for Taxonomy Expansion](rank_chunk_and_expand_lineage-oriented_reasoning_for_taxonomy_expansion.md)**

:   LORex 提出了一个即插即用的分类体系扩展框架，结合判别式排序器 TEMPORA（基于欧拉路径的分类路径语言化）和迭代式 LLM 推理（语义过滤→父节点检索→路径验证），无需微调 LLM，在 4 个基准上实现了 12% 的准确率提升和 5% 的 Wu&P 提升。

**[READoc: A Unified Benchmark for Realistic Document Structured Extraction](readoc_a_unified_benchmark_for_realistic_document_structured_extraction.md)**

:   READoc 提出了首个将文档结构化提取（DSE）定义为端到端 PDF 到 Markdown 转换的统一基准，包含 3,576 篇来自 arXiv/GitHub/Zenodo 的真实文档和三模块评估套件（标准化+分割+评分），首次揭示了当前 DSE 系统与真实场景需求之间的差距。

**[ReflectDiffu: Reflect between Emotion-intent Contagion and Mimicry for Empathetic Response Generation via a RL-Diffusion Framework](reflectdiffu_empathetic_response.md)**

:   提出轻量级共情对话框架 ReflectDiffu，融合情感传染（捕捉情绪）、意图二次机制（Exploring-Sampling-Correcting将情绪映射为行动意图）和扩散模型生成，在相关性、可控性和信息量上全面超越现有基线和 Llama-3.1-8B。

**[Re-identification of De-identified Documents with Autoregressive Infilling](reidentification_deidentified.md)**

:   提出一种基于 RAG 的再识别攻击方法，通过稀疏检索+稠密检索+自回归填充的三阶段流程，对去标识化文档进行逆向攻击，在三个数据集上高达 80% 的被遮蔽文本片段可被成功恢复，揭示了当前去标识化方法的脆弱性。

**[Identifying Reliable Evaluation Metrics for Scientific Text Revision](reliable_eval_metrics_scientific.md)**

:   系统分析了传统相似度指标（ROUGE、BERTScore 等）在科学文本修订评估中的局限性，发现它们强相关于编辑距离且惩罚深度修改，并证明结合 LLM-as-Judge 和任务特定指标的混合方法最能对齐人类评判。

**[REP: Keys to Robust Edits — From Theoretical Insights to Practical Advances](rep_robust_knowledge_editing.md)**

:   揭示locate-and-edit知识编辑方法中语义键的根本缺陷——内部表示无法同时满足鲁棒性和特异性，提出REP模块通过对比学习解耦编辑键，在鲁棒性测试上提升最高66.4%。

**[Research Borderlands: Analysing Writing Across Research Cultures](research_borderlands_analysing_writing_across_research_cultures.md)**

:   通过访谈跨学科研究者构建学术写作文化规范框架（结构/风格/修辞/引用四类），并用计算指标量化11个CS社区的写作差异，揭示LLM在跨社区写作改编时存在严重的"同质化"倾向。

**[Retrieve to Explain: Evidence-driven Predictions for Explainable Drug Target Identification](retrieve_to_explain_drug_target_identification.md)**

:   提出 R2E (Retrieve to Explain)，一种基于检索的架构，通过从文献语料库中检索证据来评分和排序所有候选答案，并利用 Shapley 值将预测忠实地归因到支撑证据，在药物靶点识别任务上超越了遗传学基线和 GPT-4 基线。

**[Revealing the Deceptiveness of Knowledge Editing: A Mechanistic Analysis of Superficial Editing](revealing_the_deceptiveness_of_knowledge_editing_a_mechanistic_analysis_of_super.md)**

:   本文定义了"表面编辑"（superficial editing）现象——经过知识编辑的模型在常规提示下表现良好，但在特制攻击探针下会回退到原始知识——并通过机制分析揭示了早期层残差流和后期层特定注意力头是导致该现象的两个关键因素。

**[Revisiting Weak-to-Strong Generalization: Reverse KL vs. Forward KL](revisiting_weak-to-strong_generalization_in_theory_and_practice_reverse_kl_vs_fo.md)**

:   在 Weak-to-Strong Generalization (W2SG) 框架中，提出用 reverse KL 替代 forward KL 作为损失函数——理论证明 reverse KL 的 mode-seeking 特性可保证强模型超过弱监督者至少"分歧量"的幅度，实验在 GPT-2/Pythia/Qwen2.5 系列上验证 reverse KL/CE 在 12/12 设置中超越 forward KL 且噪声鲁棒性更好。

**[RMoA: Optimizing Mixture-of-Agents through Diversity Maximization and Residual Compensation](rmoa_optimizing_mixture-of-agents_through_diversity_maximization_and_residual_co.md)**

:   受 ResNet 残差学习启发，提出 RMoA 框架，通过嵌入式多样性贪心选择、残差提取/聚合智能体和自适应终止机制来优化多智能体协作架构，在降低计算开销的同时实现 SOTA 性能。

**[RoToR: Towards More Reliable Responses for Order-Invariant Inputs](rotor_towards_more_reliable_responses_for_order-invariant_inputs.md)**

:   提出 RoToR，一种基于全局排序和循环位置编码分配的零样本顺序不变语言模型，通过最小化位置 ID 修改来实现稳定的顺序不变性，并设计选择路由（Selective Routing）机制自适应处理混合输入类型。

**[Rubrik's Cube: Testing a New Rubric for Evaluating Explanations on the CUBE Dataset](rubriks_cube_testing_a_new_rubric_for_evaluating_explanations_on_the_cube_datase.md)**

:   提出 Rubrik——受教育评估启发的解释质量评价量规，基于三层嵌套类型体系（Commentary⊆Justification⊆Argument）+ 8 维质量维度，配套 CUBE 数据集（26K 条由人类和 6 个 LLM 生成的解释），发现 LLM 解释低质主因是缺乏简洁性而非连贯性。

**[S2WTM: Spherical Sliced-Wasserstein Autoencoder for Topic Modeling](s2wtm_spherical_sliced-wasserstein_autoencoder_for_topic_modeling.md)**

:   提出 S2WTM，一种基于球面切片 Wasserstein 自编码器的主题模型，在超球面潜空间上对齐聚合后验与先验分布，有效避免 VAE 的后验坍塌问题，同时在主题连贯性和多样性上超越现有 SOTA。

**[SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning](scar_style_consistency_data_selection.md)**

:   SCAR 识别出回复的"语言形式"和"指令惊奇度"是影响 LLM 指令微调效果的两个关键风格因素，并提出基于风格一致性的排序方法自动选择高质量训练数据，仅用 0.7% 的原始数据就能让微调后的 LLM 匹配甚至超越全数据集训练的性能。

**[ScEdit: Script-based Assessment of Knowledge Editing](scedit_script-based_assessment_of_knowledge_editing.md)**

:   提出 ScEdit，一个基于脚本（Script）的知识编辑评估基准，将传统的"What"类事实回忆评估扩展为"How"类程序性推理评估，同时引入 token 级和文本级双层评估体系，揭示了现有知识编辑方法在实际应用场景中的显著不足。

**[Self-Correction is More than Refinement: A Learning Framework for Visual and Language Reasoning Tasks](self-correction_is_more_than_refinement_a_learning_framework_for_visual_and_lang.md)**

:   提出 Self-Correction Learning (SCL)，通过将 VLM 自身产生的自纠正数据（成功和失败的纠正样本）分类为偏好/非偏好对，利用 DPO 进行偏好微调，从根本上提升模型直接生成正确答案的能力，而非仅仅依赖推理时的迭代修正。

**[Self-Foveate: Enhancing Diversity and Difficulty of Synthesized Instructions from Unsupervised Text via Multi-Level Foveation](self-foveate_enhancing_diversity_and_difficulty_of_synthesized_instructions_from.md)**

:   提出 Self-Foveate 方法，受人类视觉注视机制启发，通过"微观-散射-宏观"三级注视策略，从无监督文本中系统性提取多粒度信息，合成具有更高多样性和难度的指令数据，用于 LLM 的指令微调。

**[SEOE: A Scalable and Reliable Semantic Evaluation Framework for Open Domain Event Detection](seoe_semantic_eval.md)**

:   针对开放域事件检测（ODED）评估的两大痛点——有限 benchmark 缺乏真实世界代表性、token 级匹配指标无法捕捉语义相似性——提出 SEOE 框架，构建包含 564 种事件类型覆盖 7 大领域的可扩展 benchmark，并引入基于 LLM 的语义 F1 评估指标。

**[Shifting from Ranking to Set Selection for Retrieval Augmented Generation](setr_set_selection_rag.md)**

:   提出从"逐个排序"到"集合选择"的 RAG 检索范式转换——SetR 通过 CoT 推理显式识别查询的信息需求，然后选择一组能共同满足这些需求的段落（而非逐个评分最相关的），在多跳 RAG 基准上超越 GPT-4o 级别的重排器。

**[SHARE: An SLM-based Hierarchical Action CorREction Assistant for Text-to-SQL](share_an_slm-based_hierarchical_action_correction_assistant_for_text-to-sql.md)**

:   提出 SHARE 框架，通过三个专门化小语言模型 (SLM, <8B) 的顺序管道协作，将声明式 SQL 转换为步骤化动作轨迹以暴露推理路径，再从 Schema 和逻辑两个维度分阶段纠正错误，实现高效低成本的 Text-to-SQL 自纠错。

**[SHARE: An SLM-based Hierarchical Action CorREction Assistant for Text-to-SQL](share_text_to_sql_correction.md)**

:   提出 SHARE 框架，通过三个专用小语言模型（SLM）组成的顺序管道，将 SQL 查询转换为逐步动作轨迹并分别修正 schema 错误和逻辑错误，从而以低成本高效辅助 LLM 进行 Text-to-SQL 自纠正。

**[ShifCon: Enhancing Non-Dominant Language Capabilities with a Shift-based Multilingual Contrastive Framework](shifcon_nondominant_language.md)**

:   提出 ShifCon 框架，通过将非优势语言的表示 shift 到优势语言子空间以获取更丰富的模型知识，再 shift 回原语言子空间进行生成，结合多语言对比学习，显著提升低资源语言的表现。

**[Silencing Empowerment, Allowing Bigotry: Auditing the Moderation of Hate Speech on Twitch](silencing_empowerment_allowing_bigotry_auditing_the_moderation_of_hate_speech_on.md)**

:   对 Twitch 平台的自动化内容审核工具 AutoMod 进行大规模审计，发送超过 10.7 万条消息，发现 AutoMod 在最严格设置下仅能标记 22% 的仇恨内容，高度依赖侮辱性词汇作为检测信号，同时错误屏蔽高达 89.5% 的教育性/赋权性内容。

**[Sleepless Nights, Sugary Days: Creating Synthetic Users with Health Conditions for Realistic Coaching Agent Interactions](sleepless_nights_sugary_days_creating_synthetic_users_with_health_conditions_for.md)**

:   提出一个端到端框架，基于真实人口学、健康/生活方式和行为/心理特征数据生成有健康状况的合成用户（涵盖睡眠和糖尿病管理），用于评估健康教练Agent的交互质量，并通过人类专家评估验证其显著优于通用合成用户。

**[Something's Fishy In The Data Lake: A Critical Re-evaluation of Table Union Search Benchmarks](somethings_fishy_in_the_data_lake_a_critical_re-evaluation_of_table_union_search.md)**

:   系统性分析了主流表联合搜索 (Table Union Search, TUS) 基准测试的三大结构性缺陷——过度重叠、语义简单、真值噪声，揭示简单的词袋 (BoW) 和预训练嵌入基线就能在这些基准上达到或超越复杂 SOTA 方法的效果，调研结论指出当前基准无法有效评估语义理解能力。

**[SPOT: Bridging Natural Language and Geospatial Search for Investigative Journalists](spot_bridging_natural_language_and_geospatial_search_for_investigative_journalis.md)**

:   提出 SPOT——一个面向调查记者的开源自然语言地理空间搜索工具，通过微调 LLaMA 3 将非结构化场景描述转换为 YAML 查询，结合 OSM 标签语义捆绑系统和 Elasticsearch 索引，实现对 OpenStreetMap 的准确自然语言访问。

**[Spotting Out-of-Character Behavior: Atomic-Level Evaluation of Persona Fidelity in Open-Ended Generation](spotting_out-of-character_behavior_atomic-level_evaluation_of_persona_fidelity_i.md)**

:   提出原子级（句子级）评估框架，通过三个指标（ACC_atom、IC_atom、RC_atom）细粒度检测大语言模型在开放式文本生成中的角色偏离（Out-of-Character）行为，弥补了传统整体评分方法无法捕捉长文本中微妙人格不一致的问题。

**[STATE ToxiCN: A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Detection](state_toxicn_a_benchmark_for_span-level_target-aware_toxicity_extraction_in_chin.md)**

:   构建了首个中文 span 级仇恨言论检测数据集 STATE ToxiCN（8029 条帖子、9533 个四元组标注），提出 Target-Argument-Hateful-Group 四元组标注体系，并首次建立了中文仇恨俚语标注词典（830 条），系统评估了多种 LLM 在 span 级中文仇恨言论检测上的能力。

**[Statement-Tuning Enables Efficient Cross-lingual Generalization in Encoder-only Models](statement-tuning_enables_efficient_cross-lingual_generalization_in_encoder-only_.md)**

:   将 Statement-Tuning 方法扩展到多语言场景，证明仅 276M 参数的 mDeBERTa 编码器模型通过多语言 Statement-Tuning 微调后，能在未见任务和未见语言上实现跨语言零样本泛化，在多个 NLU 任务上匹敌甚至超越 70B+ 参数的生成式 LLM。

**[Statistical Deficiency for Task Inclusion Estimation](statistical_deficiency_task_inclusion.md)**

:   基于统计缺陷性（statistical deficiency）理论，提出一种理论驱动的任务包含关系（task inclusion）定义与度量框架，以信息充分性（information sufficiency, IS）作为可计算代理指标，通过比较微调模型的中间层表征来估计任务间的包含程度，并在合成数据和真实NLP任务上成功重建了经典NLP pipeline的层次关系。

**[STRICTA: Structured Reasoning in Critical Text Assessment for Peer Review and Beyond](stricta_structured_reasoning_in_critical_text_assessment_for_peer_review_and_bey.md)**

:   提出 STRICTA 框架，基于结构因果模型（SCM）将文本评审建模为显式的逐步推理图（workflow），在生物医学论文评审中收集 40+ 位专家的 4000+ 推理步骤数据集，发现先验知识差异是专家分歧主因、写作风格对最终评审有因果影响，LLM 存在错误传播但人类监督可有效缓解。

**[StructFlowBench: A Structured Flow Benchmark for Multi-turn Instruction Following](structflowbench_a_structured_flow_benchmark_for_multi-turn_instruction_following.md)**

:   提出 StructFlowBench，一个融入结构流建模的多轮指令遵循基准测试，定义了六种基本的轮间关系（跟进、精炼、回忆、总结、扩展、不相关），建立了双层约束评估体系（轮内约束 + 轮间结构约束），系统评估了 13 个主流 LLM 在多轮对话结构理解上的能力。

**[Subword Models Struggle with Word Learning, but Surprisal Hides It](subword_models_struggle_with_word_learning_but_surprisal_hides_it.md)**

:   本文通过心理语言学的词汇判断任务（lexical decision task）揭示了使用子词（BPE）分词的语言模型在单词学习方面存在严重缺陷，而基于字符级分词的模型能轻松完成该任务；当使用 surprisal（在语境中的出乎意料程度）来评估时，这一差距被掩盖了。

**[SudoLM: Learning Access Control of Parametric Knowledge with Authorization Alignment](sudolm_authorization_alignment.md)**

:   SudoLM 提出了一种 LLM 参数化知识访问控制框架，通过"SUDO key"机制让授权用户解锁受限知识（如医学领域知识），未授权用户则只能访问公开知识，用 DPO 的 authorization alignment 在一个模型内实现了传统需要多版本模型才能完成的分级访问控制。

**[Synthia: Novel Concept Design with Affordance Composition](synthia_novel_concept_design_with_affordance_composition.md)**

:   Synthia 提出了一种基于 affordance（功能可供性）组合的新颖概念设计框架，通过层次化概念本体、affordance 采样策略和课程学习微调 T2I 模型，生成既视觉新颖又功能连贯的创新设计。

**[TabXEval: Why this is a Bad Table? An eXhaustive Rubric for Table Evaluation](tabxeval_why_this_is_a_bad_table_an_exhaustive_rubric_for_table_evaluation.md)**

:   TabXEval 提出了一种基于结构化评分规则（rubric）的两阶段表格评估框架——先通过 TabAlign 对齐参考表和生成表的结构，再通过 TabCompare 进行语义和语法层面的细粒度比较，同时构建了多领域基准 TabXBench。

**[TACLR: A Scalable and Efficient Retrieval-Based Method for Industrial Product Attribute Value Identification](taclr_a_scalable_and_efficient_retrieval-based_method_for_industrial_product_att.md)**

:   TACLR 提出了首个基于检索范式的产品属性值识别（PAVI）方法，通过分类感知对比学习和自适应推理机制，在处理隐含值、OOD 值和归一化输出方面全面超越分类和生成方法，并已成功部署在闲鱼（Xianyu）平台。

**[Tag-Evol: Achieving Efficient Instruction Evolving via Tag Injection](tag-evol_achieving_efficient_instruction_evolving_via_tag_injection.md)**

:   Tag-Evol 提出了一种基于知识标签注入的指令进化框架，通过构建多步细粒度标签池和预算控制注入机制，无需迭代即可生成不同难度的高质量进化指令数据，在多任务多骨干上显著优于 Evol-Instruct。

**[Task-Informed Anti-Curriculum by Masking Improves Downstream Performance on Text](task-informed_anti-curriculum_by_masking_improves_downstream_performance_on_text.md)**

:   TIACBM 提出了一种任务感知的反课程掩码微调策略：利用下游任务知识（如情感极性、词性标签）决定哪些 token 被掩码，并采用周期衰减的掩码率，在情感分析、文本分类和作者归属三个任务上均取得统计显著的性能提升。

**[taz2024full: Analysing German Newspapers for Gender Bias and Discrimination across Decades](taz2024full_analysing_german_newspapers_for_gender_bias_and_discrimination_acros.md)**

:   本文发布了 taz2024full——迄今最大的公开德语报纸语料库（180 万篇文章，1980-2024 年），并通过可扩展的分析管道展示了四十多年来德语新闻报道中性别表征的演变趋势。

**[TestNUC: Enhancing Test-Time Computing Approaches and Scaling through Neighboring Unlabeled Data Consistency](testnuc_enhancing_test-time_computing_approaches_and_scaling_through_neighboring.md)**

:   TestNUC 提出了一种线性扩展的测试时推理增强方法，通过检索测试样本的近邻无标注数据，让 LLM 同时预测测试样本及其邻居，再通过加权多数投票聚合，稳定提升分类准确率。

**[The Anatomy of Evidence: An Investigation Into Explainable ICD Coding](the_anatomy_of_evidence_an_investigation_into_explainable_icd_coding.md)**

:   本文对 MDACE 数据集和当前可解释 ICD 编码系统进行了深入的应用导向分析，揭示了人工标注证据与代码描述的重叠规律、证据在文档中的分布特征，并提出了新的匹配度量来评估模型解释的实用性。

**[The Harmonic Structure of Information Contours](the_harmonic_structure_of_information_contours.md)**

:   提出 Harmonic Surprisal (HS) 假说——文本中 surprisal 曲线呈周期性波动且周期与语篇结构（EDU/句子/段落）对齐，用带时间缩放的谐波回归检验，在 6 种语言上发现一致的周期模式，精化了经典的 Uniform Information Density 假说。

**[The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research](the_noisy_path_from_source_to_citation_measuring_how_scholars_engage_with_past_r.md)**

:   本文构建了一个大规模计算管道来量化引用保真度（citation fidelity），基于 1300 万引用句对分析发现：引用保真度与时间/学科接近度、开放获取和团队规模等因素显著相关，并通过准实验证实了中介引用导致信息失真的"电话效应"。

**[Learning to Reason Over Time: Timeline Self-Reflection for Temporal Reasoning](tiser_timeline_self_reflection_temporal.md)**

:   提出 TISER 框架，通过"推理→时间线构建→自反思→答案生成"四阶段管道实现LLM时间推理的test-time scaling，配合合成推理轨迹数据微调，让 7B 开源模型在多个时间推理基准上超越 GPT-4，在TGQA等任务上达到 SOTA。

**[TokAlign: Efficient Vocabulary Adaptation via Token Alignment](tokalign_vocab_adaptation.md)**

:   提出 TokAlign，基于 Token 共现信息学习两个词表之间的一对一映射矩阵，高效替换 LLM 的词表，实现跨语言知识迁移和跨模型 token 级蒸馏。

**[Towards a Principled Evaluation of Knowledge Editors](towards_a_principled_evaluation_of_knowledge_editors.md)**

:   本文系统性地揭示了知识编辑评估中评估方法、评估指标和编辑批量大小的选择会显著影响编辑器排名，并通过与LM Evaluation Harness集成来评估编辑对模型整体能力的副作用。

**[Towards Adaptive Memory-Based Optimization for Enhanced Retrieval-Augmented Generation](towards_adaptive_memory-based_optimization_for_enhanced_retrieval-augmented_gene.md)**

:   提出 Amber 框架，通过 Agent 协作式记忆更新器、自适应信息收集器和多粒度内容过滤器三个组件协同工作，在迭代式 RAG 范式中提升开放域问答的检索效率和答案质量。

**[Towards Comprehensive Argument Analysis in Education: Dataset, Tasks, and Method](towards_comprehensive_argument_analysis_in_education_dataset_tasks_and_method.md)**

:   本文针对中文高中议论文，提出包含纵向（论证关系）和横向（话语关系）两个维度共 14 种细粒度论证关系类型的标注方案，并在论证成分检测、关系预测和自动评分三个任务上建立了全面的 benchmark。

**[Towards Global AI Inclusivity: A Large-Scale Multilingual Terminology Dataset (GIST)](towards_global_ai_inclusivity_a_large-scale_multilingual_terminology_dataset_gis.md)**

:   构建了首个大规模多语言 AI 术语数据集 GIST，包含从顶级 AI 会议论文中提取的 5K 术语及其阿拉伯语、中文、法语、日语和俄语翻译，并探索了三种无需重训练的术语集成方法来提升机器翻译质量。

**[Towards Storage-Efficient Visual Document Retrieval: An Empirical Study on Reducing Patch-Level Embeddings](towards_storage-efficient_visual_document_retrieval_an_empirical_study_on_reduci.md)**

:   系统性研究了视觉文档检索（VDR）中 patch 级别嵌入的压缩策略，发现 pruning 在 VDR 中本质不适用（简单随机剪枝反而最优），而 token merging 结合微调可在仅保留 2.8% 存储量时维持 94.6% 的检索性能（Light-ColPali/ColQwen2）。

**[Towards Style Alignment in Cross-Cultural Translation](towards_style_alignment_in_cross-cultural_translation.md)**

:   本文提出跨文化翻译中的"风格对齐"概念，发现当前 LLM 翻译会破坏文本的风格信息（尤其偏向中性化），并提出 RASTA 方法通过学习嵌入空间中的风格概念来检索风格对齐的少样本示例，在不损害翻译质量的前提下显著提升风格保持。

**[Did Translation Models Get More Robust Without Anyone Even Noticing?](translation_robustness.md)**

:   通过合成噪声和社交媒体文本的系统性实验，证明现代大规模预训练翻译模型（LLM）在未经任何专门鲁棒性训练的情况下，对多种输入噪声的鲁棒性已远超传统 NMT 模型，鲁棒性随模型规模增长自然提升。

**[Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis](tree-of-debate_multi-persona_debate_trees_elicit_critical_thinking_for_scientifi.md)**

:   提出Tree-of-Debate (ToD)框架，将科学论文转化为LLM persona进行树结构化辩论，通过自我审议、迭代检索和主持人引导的层级子话题扩展，生成细粒度、上下文化的论文对比摘要，在领域专家评估中显著优于基线方法。

**[TripTailor: A Real-World Benchmark for Personalized Travel Planning](triptailor_a_real-world_benchmark_for_personalized_travel_planning.md)**

:   提出 TripTailor，一个基于真实数据的大规模旅行规划 benchmark，包含 40 个城市的 50 万+ POI 和近 4000 条真实行程，并引入可行性、合理性和个性化三维评估框架，发现最先进 LLM 生成的行程不到 10% 能达到人类水平。

**[TROVE: A Challenge for Fine-Grained Text Provenance via Source Sentence Tracing and Relationship Classification](trove_a_challenge_for_finegrained_text.md)**

:   提出TROVE文本溯源挑战，将目标文本中每个句子追溯到源文档中的具体源句，并分类其细粒度关系（引用、压缩、推理等），覆盖多文档和长文档场景。

**[TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages](tumlu_a_unified_and_native_language_understanding_benchmark_for_turkic_languages.md)**

:   提出 TUMLU 和 TUMLU-mini，首个面向突厥语系（9 种语言）的原生语言理解基准，包含 38139 道中高中学科的多选题，覆盖拉丁、西里尔和阿拉伯三种文字系统，为低资源语言的 LLM 评估提供了高质量的原生基准。

**[Tuna: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos](tuna_temporal_understanding.md)**

:   本文提出 Tuna，一个面向密集动态视频的细粒度时序理解基准，包含 1000 个精心标注的视频和两个互补任务（Tuna-cap 字幕生成和 Tuna-mcq 视频问答），覆盖相机状态、场景、动作、属性四大动态要素，评估 21 个模型后发现即使 GPT-4o 也仅达 58.5% F1，揭示了当前模型在时序理解上的重大不足。

**[Typed-RAG: Type-Aware Decomposition of Non-Factoid Questions for Retrieval-Augmented Generation](typed-rag_type-aware_decomposition_of_non-factoid_questions_for_retrieval-augmen.md)**

:   提出 Typed-RAG 框架，通过对非事实性问题（NFQ）进行类型感知的分解，将复杂的多方面问题拆解为单方面子查询，针对不同问题类型（辩论、经验、比较等）设计差异化的检索与生成策略，显著提升了 RAG 在 NFQA 中的表现。

**[Understanding Common Ground Misalignment in Goal-Oriented Dialog: A Case-Study with Ubuntu Chat Logs](understanding_common_ground_misalignment_in_goal-oriented_dialog_a_case-study_wi.md)**

:   本文通过在 Ubuntu IRC 技术支持对话中标注"对话摩擦"（conversational friction），实证揭示了共识基础（common ground）的失配与任务成功率之间的显著关联，并发现 LLM 能识别显式的对话摩擦但难以处理需要语用或领域推理的隐式摩擦。

**[Unifying Language Agent Algorithms with Graph-based Orchestration Engine for Reproducible Agent Research](unifying_language_agent_algorithms_with_graph-based_orchestration_engine_for_rep.md)**

:   提出 AGORA 框架，通过图编排引擎统一实现 10 种主流 Agent 推理算法，并建立标准化评测体系，系统比较不同算法在多种 LLM 上的表现，发现简单的 CoT 方法在成本效益上往往优于复杂算法。

**[Unlocking Speech Instruction Data Potential with Query Rewriting](unlocking_speech_instruction_data_potential_with_query_rewriting.md)**

:   提出基于多 LLM 知识融合的查询重写框架，通过零样本重写将文本指令转换为更适合 TTS 模型合成的分布，结合多 Agent 标注与验证机制，将语音指令数据可用率从 72% 提升至 93%。

**[Unveiling Dual Quality in Product Reviews: An NLP-Based Approach](unveiling_dual_quality_in_product_reviews_an_nlp-based_approach.md)**

:   首次将"产品双重质量"（同一品牌产品在不同市场存在质量差异）问题定义为 NLP 任务，构建了 1957 条波兰语评论的标注数据集，并系统评估了 SetFit、Transformer 编码器和 LLM 等多种方法在该任务上的表现。

**[USDC: A Dataset of User Stance and Dogmatism in Long Conversations](usdc_a_dataset_of_underlineuser_underlinestance_and_underlinedogmatism_in_long_u.md)**

:   构建 USDC——首个用户级长对话立场和教条主义数据集，764 个多用户 Reddit 对话（22 子版块），用 {Mistral Large, GPT-4} × {zero/one/few-shot} 共 6 设置多数投票标注立场(5级)+教条程度(4级)，并用 7 个 SLM 微调/指令微调建立基线。

**[Using Shapley Interactions to Understand How Models Use Structure](using_shapley_interactions_to_understand_how_models_use_structure.md)**

:   利用 Shapley Taylor 交互指数（STII）分析语言模型和语音模型如何在内部表征中编码输入的结构关系，发现自回归模型在句法邻近度、非组合语义和语音协同发音方面均展现出有意义的非线性交互模式。

**[Using Source-Side Confidence Estimation for Reliable Translation into Unfamiliar Languages](using_source-side_confidence_estimation_for_reliable_translation_into_unfamiliar.md)**

:   提出一种基于梯度归因的源端置信度估计方法，通过测量输出序列对源端嵌入的敏感度来识别可能误译的源端词汇，无需词对齐，在误译检测任务上显著优于传统对齐方法。

**[VAQUUM: Are Vague Quantifiers Grounded in Visual Data?](vaquum_are_vague_quantifiers_grounded_in_visual_data.md)**

:   构建 VAQUUM 数据集（20300 条人类评分），系统评估视觉语言模型在视觉场景中对模糊量词（few, many 等）理解和使用的能力，发现 VLM 的生成概率与人类判断存在一定对齐但在不同评估范式间表现不一致。

**[Velocitune: A Velocity-based Dynamic Domain Reweighting Method for Continual Pre-training](velocitune_a_velocity-based_dynamic_domain_reweighting_method_for_continual_pre-.md)**

:   提出 Velocitune 框架，通过学习速度（learning velocity）动态调整持续预训练中各数据域的采样权重——优先加大学习较慢的域的权重，并利用 scaling law 低成本估计目标损失，在数学/代码推理和系统命令生成任务上显著优于静态混合基线。

**[Verbosity-Aware Rationale Reduction: Effective Reduction of Redundant Rationale](verbosity-aware_rationale_reduction_effective_reduction_of_redundant_rationale_v.md)**

:   提出 VARR 框架，以句子为单位并利用基于似然度的"冗余度（verbosity）"标准识别和移除推理路径中的冗余句子，在多种推理任务上平均提升 7.71% 准确率同时减少 19.87% 的 token 生成。

**[Visual Cues Enhance Predictive Turn-Taking for Two-Party Human Interaction](visual_cues_enhance_predictive_turn-taking_for_two-party_human_interaction.md)**

:   提出 MM-VAP 多模态话轮转换预测模型，结合语音与面部表情、头部姿态、注视方向等视觉线索，在视频会议对话中以 84% 平衡准确率显著优于纯语音 SOTA 模型的 79%，并首次按转换沉默时长分析性能。

**[VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](vital_pluralistic_alignment_healthcare.md)**

:   本文构建了首个面向医疗健康领域的多元化对齐（pluralistic alignment）基准数据集 VITAL，包含 13.1K 价值观情境和 5.4K 多选题，并通过对 8 个 LLM 的广泛评估表明，现有多元化对齐技术（尤其是 ModPlural）在医疗场景下表现不佳，简单的 prompting 反而效果更好。

**[Voting or Consensus? Decision-Making in Multi-Agent Debate](voting_or_consensus_decision-making_in_multi-agent_debate.md)**

:   系统评估了 7 种决策协议（4 种投票 + 3 种共识）对多 Agent LLM 辩论的影响，发现投票在推理任务上优于共识 13.2%，共识在知识任务上优于投票 2.8%，并提出 AAD 和 CI 两种提升答案多样性的新方法。

**[Well Begun is Half Done: Low-resource Preference Alignment by Weak-to-Strong Decoding](well_begun_is_half_done_low-resource_preference_alignment_by_weak-to-strong_deco.md)**

:   提出 Weak-to-Strong Decoding (WSD) 框架，利用一个小型对齐模型为大型基座模型起草对齐的开头，再由大模型续写，以低资源方式实现偏好对齐且不产生 alignment tax。

**[When Should Dense Retrievers Be Updated in Evolving Corpora? Detecting Out-of-Distribution Corpora Using GradNormIR](when_should_dense_retrievers_be_updated_in_evolving_corpora_detecting_out-of-dis.md)**

:   提出 GradNormIR，一种利用梯度范数在无 query 条件下检测 OOD 语料库的无监督方法，帮助判断稠密检索器何时需要更新以应对不断演化的文档集合。

**[When to Speak, When to Abstain: Contrastive Decoding with Abstention](when_to_speak_when_to_abstain.md)**

:   提出 CDA（Contrastive Decoding with Abstention），一种免训练解码方法，通过熵校准的不确定性估计让 LLM 在参数/上下文知识可用时生成正确回答、在两者都不可靠时主动弃权，覆盖全部四种知识可用性场景。

**[Why Are Positional Encodings Nonessential for Deep Autoregressive Transformers? Revisiting a Petroglyph](why_are_positional_encodings_nonessential_for_deep_autoregressive_transformers_r.md)**

:   这是一篇综述/回顾性论文，系统解释了多层自回归 Transformer 无需显式位置编码即可区分不同序列的原理，并追溯该结论的历史起源（Irie et al., 2019），纠正了社区中将此发现误归因于后来工作的现象。

**[Words of Warmth: Trust and Sociability Norms for over 26k English Words](words_of_warmth_trust_and_sociability_norms_for_over_26k_english_words.md)**

:   构建了首个大规模人工标注的英文词汇-温暖（Warmth）关联词库 Words of Warmth，覆盖 26k+ 词汇的信任（Trust）和社会性（Sociability）维度评分，并利用该资源研究了儿童词汇习得和社交媒体刻板印象。

**[WXImpactBench: A Disruptive Weather Impact Understanding Benchmark for Evaluating Large Language Models](wximpactbench_a_disruptive_weather_impact_understanding_benchmark_for_evaluating.md)**

:   提出 WXImpactBench，首个评估 LLM 理解极端天气社会影响的基准，包含经过 4 阶段管线处理的高质量历史报纸数据集和两个评估任务（多标签分类和排序问答）。

**[X-Turing: Towards an Enhanced and Efficient Turing Test for Long-Term Dialogue Agents](xturing_enhanced_turing_test.md)**

:   提出 X-Turing 框架，通过引入 burst 对话模式和伪对话生成技术来增强和高效化图灵测试，能够评估 LLM 在长期对话中的人类模仿能力，发现 LLM 随着对话轮次增加表现显著下降。

**[You need to MIMIC to get FAME: Solving Meeting Transcript Scarcity with Multi-Agent Conversations](you_need_to_mimic_to_get_fame_solving_meeting_transcript_scarcity_with_a_multi-a.md)**

:   提出 MIMIC 框架，通过多智能体辩论模拟生成合成会议转录，构建了包含 800 场会议的 FAME 数据集（500 英语 + 300 德语），并设计了基于心理学的行为真实性评估框架。

**[Zero-Shot Conversational Stance Detection: Dataset and Approaches](zero-shot_conversational_stance_detection_dataset_and_approaches.md)**

:   构建了首个零样本多轮多方对话立场检测数据集 ZS-CSD（280 个目标、17k+ 样本），并提出 SITPCL 模型，通过说话者交互建模和目标感知原型对比学习实现了 SOTA 性能（F1-macro 43.81%）。

**[ZIPA: A Family of Efficient Models for Multilingual Phone Recognition](zipa_a_family_of_efficient_models_for_multilingual_phone_recognition.md)**

:   提出 Zipa 系列高效语音模型，基于 Zipformer 骨干和 IpaPack++（17,132 小时多语言标注数据），在多语言音素识别上达到 SOTA，64M 参数模型即超越现有 300M 模型，并通过噪声学生训练在 4000+ 种语言上进一步提升。

**[ZJUKLAB at SemEval-2025 Task 4: Unlearning via Model Merging](zjuklab_at_semeval-2025_task_4_unlearning_via_model_merging.md)**

:   在 SemEval-2025 Task 4（LLM 敏感内容遗忘）中获得第二名，核心思路是训练两个互补模型（一个过度遗忘、一个遗忘不足），通过 TIES-Merging 合并得到平衡遗忘的模型，本地实验达到近乎完美的 MIA 分数 0.501。
