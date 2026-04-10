<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**💬 ACL2025** · 共 **381** 篇

**[A Case Study of Cross-Lingual Zero-Shot Generalization for Classical Languages in LLMs](a_case_study_of_cross-lingual_zero-shot_generalization_for_classical_languages_i.md)**

:   系统评估 LLM（GPT-4o/Llama-3.1）在三种古典语言（梵语、拉丁语、古希腊语）上的零样本跨语言泛化能力——涵盖 NER、机器翻译、问答三个 NLU 任务，发现大模型在域外数据上可比肩甚至超越微调基线，模型规模是决定性因素，并贡献了一个 1501 对的梵语事实问答数据集。

**[A Large-Scale Real-World Evaluation of LLM-Based Virtual Teaching Assistant](a_large-scale_real-world_evaluation_of_llm-based_virtual_teaching_assistant.md)**

:   在 KAIST 477 名研究生的 AI 编程课上部署基于 GPT-4o-mini + RAG 的虚拟教学助手（VTA），通过三轮大规模问卷调查和 3,869 条交互日志分析系统性评估 VTA 的有效性与接受度，发现 VTA 在编程和概念问题上有效但信任度随时间下降。

**[A Modular Dataset to Demonstrate LLM Abstraction Capability](a_modular_dataset_to_demonstrate_llm_abstraction_capability.md)**

:   提出ArrangementPuzzle拼图数据集并训练LLM激活值分类器，发现分类器以>80%准确率识别推理正确性，揭示LLM在中间-后层Transformer层编码了区分逻辑等价与语义等价的抽象推理概念。

**[A Semantic-Aware Layer-Freezing Approach to Computation-Efficient Fine-Tuning of Language Models](a_semantic-aware_layer-freezing_approach_to_computation-efficient_fine-tuning_of.md)**

:   通过分析LLM推理过程中潜在表征的转移轨迹（transition traces）计算各层语义偏差，结合推导的缩放律公式估计各层对降低损失的贡献，从而确定"在哪些层微调"，实现与PEFT正交的高效微调方法。

**[A Survey of Automatic Prompt Optimization with Instruction-focused Heuristic-based Search Algorithm](a_survey_of_automatic_prompt_optimization_with_instruction-focused_heuristic-bas.md)**

:   系统综述 80+ 种基于启发式搜索算法的自动 Prompt 优化方法，提出五维分类体系（Where/What/What criteria/Which operators/Which algorithms）将碎片化研究统一到一个完整的分析框架下。

**[A Survey of Large Language Models in Psychotherapy: Current Landscape and Future Directions](a_survey_of_large_language_models_in_psychotherapy_current_landscape_and_future_.md)**

:   系统综述 LLM 在心理治疗中的应用——提出评估（Assessment）→ 诊断（Diagnosis）→ 治疗（Treatment）三阶段概念分类法，覆盖症状检测、诊断推理、治疗对话策略等，揭示当前研究失衡（聚焦常见障碍、语言偏差、方法碎片化、理论整合不足），并提出连续多阶段建模和实时自适应系统等未来方向。

**[A Survey of LLM-based Agents in Medicine: How Far Are We from Baymax?](a_survey_of_llm-based_agents_in_medicine_how_far_are_we_from_baymax.md)**

:   系统综述 LLM-based Agent 在医学中的应用——分析 Agent 架构（系统配置/临床规划/医学推理/外部能力增强）、应用场景（临床决策/文档/训练模拟/服务优化）和评估框架，覆盖 60 篇研究，识别幻觉管理、多模态整合、部署障碍和伦理问题等关键挑战。

**[A Survey on Efficient Large Language Model Training: From Data-centric Perspectives](a_survey_on_efficient_large_language.md)**

:   首个系统性的数据高效 LLM 后训练综述，提出"数据价值飞轮"分类法，将方法分为五大类（数据选择、质量增强、合成生成、蒸馏压缩、自演进生态），覆盖 100+ 篇代表性工作并展望未来方向。

**[A Survey on Proactive Defense Strategies Against Misinformation in Large Language Models](a_survey_on_proactive_defense_strategies_against_misinformation_in_large_languag.md)**

:   系统综述 LLM 主动防御错误信息的策略——提出"三支柱"框架：(1) 知识可信度（训练数据质量+知识编辑+RAG）, (2) 推理可靠性（自对齐+解码策略）, (3) 输入鲁棒性（对抗攻击防御+输入净化）。127 种技术的分类映射，48 项基准研究的元分析显示主动防御比传统检测方法提升 42-63%。

**[A Systematic Study of Compositional Syntactic Transformer Language Models](a_systematic_study_of_compositional_syntactic_transformer_language_models.md)**

:   对组合型句法 Transformer 语言模型（Compositional SLMs）进行系统研究——识别四个关键设计维度（句法树二叉化、线性化方向、组合函数、子成分掩码），提出统一框架涵盖 16 种变体（含 13 种全新变体），在语言建模、句法泛化、摘要、对话和推理效率上全面评估，给出多条设计建议。

**[A Training-free LLM-based Approach to General Chinese Character Error Correction](a_training-free_llm-based_approach_to_general_chinese_character_error_correction.md)**

:   提出通用中文字符纠错任务C2EC（覆盖替换、缺失、冗余三种错误类型），通过扩展训练无关的CSC方法并结合Levenshtein距离和prompt-based LLM，使14B参数模型在不微调的条件下达到近50倍大模型的纠错性能。

**[AAD-LLM: Neural Attention-Driven Auditory Scene Understanding](aad-llm_neural_attention-driven_auditory_scene_understanding.md)**

:   提出意图感知听觉场景理解（II-ASU）范式和 AAD-LLM 原型系统——通过颅内脑电（iEEG）解码听者正在关注哪个说话人，将注意力状态注入听觉 LLM（Qwen2-Audio），使模型在多说话人场景中生成与听者感知对齐的回答，在描述/转录/提取/问答四个任务上主观和客观评估均优于无注意力感知的基线。

**[AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research](abgen_evaluating_large_language_models_in.md)**

:   提出 AbGen——首个评估 LLM 设计消融实验能力的基准（1500 条专家标注数据来自 807 篇 NLP 论文），发现最强 LLM (DeepSeek-R1) 与人类专家差距 14.4%，且 LLM-as-Judge 评分与人类评估严重不一致。

**[Ad-hoc Concept Forming in the Game Codenames as a Means for Evaluating Large Language Models](ad-hoc_concept_forming_in_the_game_codenames_as_a_means_for_evaluating_large_lan.md)**

:   以桌游 Codenames 作为 LLM 评测工具——LLM 分别扮演线索给出者（Spymaster）和猜测者（Field Operative），通过控制词频/歧义性/具体性/风险等级/对手速度等变量系统评估 LLM 的临时概念形成、语义关联、合作推理和语用能力，发现 o3-mini 和 Claude-3.5 领先但所有模型在高风险和抽象词条件下均显著退化。

**[AD-LLM: Benchmarking Large Language Models for Anomaly Detection](ad-llm_benchmarking_large_language_models_for_anomaly_detection.md)**

:   首个系统评估 LLM 在 NLP 异常检测中角色的基准 AD-LLM——覆盖三个关键任务：(1) 零样本检测（LLM 预训练知识直接做 AD），(2) 数据增强（生成合成数据/类别描述提升 AD 模型），(3) 模型选择（LLM 推荐无监督 AD 模型）。多数据集实验发现 LLM 零样本 AD 表现出色，精心设计的增强有用，但模型选择的可解释性仍是挑战。

**[Adaptive-VP: A Framework for LLM-Based Virtual Patients that Adapts to Trainees' Dialogue](adaptive-vp_a_framework_for_llm-based_virtual_patients_that_adapts_to_trainees_d.md)**

:   提出 Adaptive-VP——基于 LLM 的虚拟病人对话生成框架，根据护理学员的沟通质量动态调整虚拟病人行为（沟通差→升级敌意，沟通好→缓和），包含案例开发管线+评估模块+动态适应模块+对话生成模块+安全监控模块五个组件，专家护士评估显示其交互自然度和真实感显著优于现有方法。

**[ToxEdit: Adaptive Detoxification Safeguarding General Capabilities of LLMs through Toxicity-Aware Knowledge Editing](adaptive_detoxification_safeguarding_general_capabilities_of_llms_through_toxici.md)**

:   提出 ToxEdit——毒性感知的知识编辑方法，在前向传播中动态检测毒性激活模式（SVM 二分类器检测有害隐藏状态），将计算路由到原始 FFN 或编辑后的 FFN，实现自适应去毒而不过度编辑。增强 SafeEdit 基准加入指令遵从评估，在多个 LLM 上去毒能力和通用能力保留均 SOTA。

**[Adversarial Tokenization](adversarial_tokenization.md)**

:   本文发现 LLM 管线中 BPE tokenizer 只使用唯一一种分词方式，但同一字符串存在指数级多种合法分词；通过对抗性地选择非标准分词方案，可以在不改变原始文本的情况下绕过安全对齐，攻击成功率与现有 SOTA 文本级攻击方法相当。

**[AfroBench: How Good Are Large Language Models on African Languages?](afrobench_how_good_are_large_language_models_on_african_languages.md)**

:   构建 AfroBench——首个大规模非洲语言 LLM 多任务评测基准，覆盖 64 种非洲语言、15 个任务、22 个数据集（9 NLU + 6 生成 + 6 知识QA + 1 数学推理），系统对比提示式 LLM 与微调 BERT/T5 基线，发现非洲语言与英语之间存在巨大性能差距，且性能与单语资源可用性密切相关。

**[AIMSCheck: Leveraging LLMs for AI-Assisted Review of Modern Slavery Statements Across Jurisdictions](aimscheck_modern_slavery.md)**

:   提出 AIMSCheck——使用 LLM 辅助审查企业现代奴隶制声明是否合规的端到端框架，构建英国和加拿大的新标注数据集（AIMS.uk/AIMS.ca），三层分解合规评估增强可解释性，在澳大利亚数据上训练的模型能有效跨司法管辖泛化到英国和加拿大。

**[Algorithmic Fidelity of Large Language Models in Generating Synthetic German Public Opinions: A Case Study](algorithmic_fidelity_german_opinion.md)**

:   使用德国纵向选举研究（GLES）的开放式调查数据，评估 LLM 在生成反映德国亚群体公共舆论方面的"算法保真度"，发现 Llama2 在建模群体意见方面优于其他 LLM，但对左翼政党支持者的表征好于右翼（如 AfD），且提示中包含更多人口统计变量可改善表现。

**[NOVA: Aligning LLMs to Follow Instructions and Hallucinate Less via Effective Data Filtering](aligning_large_language_models_to_follow_instructions_and_hallucinate_less_via_e.md)**

:   提出 NOVA 框架——通过过滤掉 LLM "不熟悉"的指令数据来同时减少幻觉和保持指令遵从能力——Internal Consistency Probing（ICP）通过多次自生成回复的隐藏状态一致性评估 LLM 对指令的熟悉度，Semantic Equivalence Identification（SEI）通过语义聚类+投票评估 LLM 对目标回复的熟悉度，再用质量奖励模型确保数据质量。大幅减少幻觉同时保持指令遵从。

**[Alignment Drift in CEFR-prompted LLMs for Interactive Spanish Tutoring](alignment_drift_in_cefr-prompted_llms_for_interactive_spanish_tutoring.md)**

:   通过 LLM 模拟师生对话实验，发现基于 CEFR 等级的 system prompting 虽然能初步约束 LLM 输出的西班牙语难度，但随着对话轮次增加，这种约束效果逐渐衰减——作者将此现象命名为"alignment drift"，表明仅靠提示工程不足以支撑长期的自适应语言教学。

**[Answer When Needed, Forget When Not: Language Models Pretend to Forget via In-Context Knowledge Unlearning](answer_when_needed_forget_when_not_language_models_pretend_to_forget_via_in-cont.md)**

:   提出"上下文知识遗忘"（In-Context Knowledge Unlearning）——通过引入遗忘 token（`<<UNL>>...<<UNL>>`）使 LLM 在推理时根据查询上下文选择性地"遗忘"特定知识，微调后 LLM 在 TOFU/AGE/RWKU 上达到 95% 遗忘准确率同时保留 80% 无关知识。更深入的内部分析发现 LLM 在中间层仍生成正确答案，仅在最后一层决定"假装遗忘"。

**[Revisiting Common Assumptions about Arabic Dialects in NLP](arabic_dialects_assumptions_revisited.md)**

:   系统验证了阿拉伯语 NLP 中四个被广泛接受的假设，通过 978 个方言句子+33 名标注者的多标签标注数据集证明：56% 的方言句子在多个区域方言中有效，方言词表的区分度被高估，句子长度与方言歧义性的相关性远弱于方言化程度（ALDi），不同方言说话者对同一句子的 ALDi 评级差异显著。

**[Are Your LLMs Capable of Stable Reasoning?](are_your_llms_capable_of_stable_reasoning.md)**

:   提出 G-Pass@k 评估指标和 LiveMathBench 动态基准，从"性能上限"和"稳定性"两个维度全面评估LLM的推理能力，揭示了当前LLM在推理一致性上存在巨大提升空间。

**[ArithmAttack: Evaluating Robustness of LLMs to Noisy Context in Math Problem Solving](arithmattack_evaluating_robustness_of_llms_to_noisy_context_in_math_problem_solv.md)**

:   提出 ArithmAttack，通过在数学题上下文中随机插入标点符号（不改变任何单词）来测试 LLM 的鲁棒性，发现八个主流 LLM（包括 Llama3、Mistral、DeepSeek）在面对这种简单噪声时性能都显著下降。

**[Astute RAG: Overcoming Imperfect Retrieval Augmentation and Knowledge Conflicts for Large Language Models](astute_rag_knowledge_conflicts.md)**

:   Astute RAG 提出了一种对不完美检索具有鲁棒性的 RAG 方法，通过自适应生成 LLM 内部知识作为补充、带有来源标注的知识整合、以及基于可靠性的答案生成三个步骤，在 Gemini 和 Claude 上显著优于现有鲁棒 RAG 方法，且是唯一在最坏情况下（检索全部无用）不劣于无 RAG 基线的方法。

**[Atomic Calibration of LLMs in Long-Form Generations](atomic_calibration_of_llms_in_long-form_generations.md)**

:   系统研究长文本生成中的原子级校准（Atomic Calibration）——将长回复分解为原子主张（atomic claims），为每个主张分配置信度分数，发现回复级校准良好的模型在原子级校准很差，将置信度获取方法分为判别式（内部状态）和生成式（外部评估）两类并发现它们互补，提出两种融合策略达到 SOTA 校准效果。

**[Automating Legal Interpretation with LLMs: Retrieval, Generation, and Evaluation](atrie_legal_interpretation.md)**

:   提出 ATRIE 框架模拟法学教义研究流程——自动从判例法中检索概念相关信息、解释法律概念、并通过下游任务（法律概念蕴涵LCE）自动评估解释质量，生成的解释在全面性和可读性上与专家相当。

**[AutoGUI: Scaling GUI Grounding with Automatic Functionality Annotations from LLMs](autogui_scaling_gui_grounding_with_automatic.md)**

:   提出 AutoGUI 自动标注管线——通过模拟交互比较 UI 状态变化 + LLM 推断元素功能 + LLM 验证过滤，构建 704K 高质量 UI 功能标注数据集，标注正确率 96.7% 可比人类，显著提升 VLM 的 UI grounding 能力且展现数据扩展效应。

**[LLM-AT: Automatic Transmission for LLM Tiers Optimizing Cost and Accuracy](automatic_transmission_for_llm_tiers_optimizing_cost_and_accuracy_in_large_langu.md)**

:   提出 LLM-AT（LLM Automatic Transmission）框架——无需训练即可动态选择 LLM 层级，Starter 通过准确率估计器选择初始层级，Generator 生成回答，Judge 评估有效性，无效则自动升级到更高层级，在不同难度任务上平衡准确率和成本，比始终用顶级模型更高效。

**[Awes, Laws, and Flaws From Today's LLM Research](awes_laws_and_flaws_from_todays_llm_research.md)**

:   对 2020-2024 年 2000+ 篇 LLM 相关论文进行科学方法论的系统批判——基于统计检验/可复现性/伦理声明等标准评估研究质量，发现多种趋势：伦理声明减少、LLM 作为评估器增多、无人工评估的推理能力声称增多、统计严谨性下降，但会议检查清单（如 ACL 强制 limitations 章节）确实有效缓解部分问题。

**[OPTS: Bandit-Based Prompt Design Strategy Selection Improves Prompt Optimizers](bandit-based_prompt_design_strategy_selection_improves_prompt_optimizers.md)**

:   首次提出 Prompt 设计策略的显式选择机制 OPTS——将 CoT/角色提示/少样本等多种策略视为多臂老虎机的"臂"，用 Thompson 采样动态选择要应用的策略，集成到 EvoPrompt 后在 BIG-Bench Hard 上将 GPT-4o mini 性能提升最高 50%，超越隐式策略选择（APET）和均匀采样。

**[BanStereoSet: A Dataset to Measure Stereotypical Social Biases in LLMs for Bangla](banstereoset_a_dataset_to_measure_stereotypical_social_biases_in_llms_for_bangla.md)**

:   构建 BanStereoSet，一个包含 1194 条填空式样本、覆盖 9 类偏见（种族/性别/宗教/职业/美貌/年龄/种姓/地区等）的孟加拉语刻板印象偏见数据集，用于评估多语言 LLM 在孟加拉语中的社会偏见，发现 GPT-4o 偏见最高，Mistral 最低。

**[Batayan: A Filipino NLP Benchmark for Evaluating Large Language Models](batayan_a_filipino_nlp_benchmark_for_evaluating_large_language_models.md)**

:   提出 Batayan——首个全面的菲律宾语 LLM 评测基准，覆盖理解/推理/生成三大能力的 8 个任务（含 3 个全新菲律宾语任务），由母语者翻译和标注确保语言真实性，评测 50+ 开源和商用 LLM 后发现菲律宾语表现显著落后于英语，显式菲律宾语支持和模型规模的提升均能带来明显增益。

**[Binary Classifier Optimization for Large Language Model Alignment](bco_binary_classifier_alignment.md)**

:   提出 BCO（Binary Classifier Optimization），从数学上证明二元交叉熵损失是 DPO 损失的上界，使 LLM 对齐仅需"点赞/踩"二元反馈而非成对偏好数据，并通过新颖的 reward shift 技术收紧上界，在配对偏好数据集上与 DPO 持平，在真实 Likert-5 标注数据上优于 DPO 和 KTO。

**[Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases](between_circuits_chomsky.md)**

:   提出在自然语言预训练前先在形式语言上进行"pre-pretraining"，发现具有层级依赖结构的形式语言（如 k-Shuffle Dyck）能为 Transformer 提供有效的归纳偏置，使 1B 参数模型以 33% 更少的 token 达到相同的语言建模损失。

**[Beyond In-Context Learning: Aligning Long-form Generation of LLMs via Task-Inherent Attribute Guidelines](beyond_in-context_learning_aligning_long-form_generation_of_large_language_model.md)**

:   证明 ICL 示例不足以教会 LLM 任务的语言和格式分布，提出 LongGuide 自动生成质量指标和输出约束两种 guidelines 来增强长文本生成。

**[Beyond Profile: From Surface-Level Facts to Deep Persona Simulation in LLMs](beyond_profile_from_surface-level_facts_to_deep_persona_simulation_in_llms.md)**

:   提出 CharacterBot，通过 4 个训练任务（视角重建预训练 + 选择题/生成式QA/风格迁移微调）和 CharLoRA 参数更新机制，从鲁迅 17 部杂文集中学习其语言风格和深层思想模式，在语言准确性和观点理解上显著超越各基线。

**[Beyond Prompt Engineering: Robust Behavior Control in LLMs via Steering Target Atoms](beyond_prompt_engineering_robust_behavior_control_in_llms_via_steering_target_at.md)**

:   提出 STA（Steering Target Atoms），利用稀疏自编码器 (SAE) 将 LLM 的表示解耦为原子知识组件，通过激活幅度和频率筛选目标原子并操控，实现比提示工程更鲁棒、更精细的行为控制，在安全解毒和推理控制任务上效果优于现有 steering 方法。

**[Bias Attribution in Filipino Language Models: Extending a Bias Interpretability Metric for Application on Agglutinative Languages](bias_attribution_in_filipino_language_models_extending_a_bias_interpretability_m.md)**

:   将信息论偏见归因分数指标扩展到黏着语（菲律宾语），通过对子词分数取均值来处理复杂词素结构，在 4 个多语言 PLM 上揭示菲律宾语模型的偏见由实体类主题词（人物/物品/关系）驱动，与英语中动作类主题词（犯罪/性行为）形成鲜明对比。

**[Bias in Language Models: Beyond Trick Tests and Towards RUTEd Evaluation](bias_in_language_models_beyond_trick_tests_ruted_evaluation.md)**

:   通过对比标准偏见基准（"trick tests"）与基于真实使用场景的 RUTEd 评估，发现标准偏见基准与真实场景中的偏见表现无显著相关性，主张偏见评估应面向具体应用场景。

**[BiasGuard: A Reasoning-Enhanced Bias Detection Tool for Large Language Models](biasguard_a_reasoning-enhanced_bias_detection_tool_for_large_language_models.md)**

:   提出 BiasGuard，通过显式推理公平性规范来检测 LLM 输出偏见：第一阶段用教师模型生成推理轨迹做 SFT 初始化，第二阶段用 DPO 强化推理质量，在 5 个数据集上超越分类器和 LLM-as-Judge 方法且降低过度公平误判。

**[Blessing of Multilinguality: A Systematic Analysis of Multilingual In-Context Learning](blessing_of_multilinguality_a_systematic_analysis_of_multilingual_in-context_lea.md)**

:   系统分析多语言 ICL 策略，发现在 prompt 中混合多种高资源语言（HRL）的 demonstrations 一致性优于纯英文 demonstrations，尤其在低资源语言（LRL）上提升显著（Llama3.1 上 LRL 平均准确率提升 8.9~12.6%），甚至仅在 prompt 中加入不相关的非英语句子也能带来可测量的增益，揭示了"多语言暴露本身即有效"的现象。

**[BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning](bmike-53_investigating_cross-lingual_knowledge_editing_with_in-context_learning.md)**

:   提出 BMIKE-53，覆盖 53 种语言的跨语言上下文知识编辑 (IKE) 基准，统一了 zsRE/CounterFact/WikiFactDiff 三个知识编辑数据集，系统评估发现模型规模和示例对齐对跨语言 IKE 效果至关重要，文字系统类型是影响跨语言性能差异的关键因素。

**[Boosting LLM's Molecular Structure Elucidation with Knowledge Enhanced Tree Search Reasoning](boosting_llms_molecular_structure_elucidation_with_knowledge_enhanced_tree_searc.md)**

:   提出 K-MSE，通过构建分子子结构知识库补充 LLM 化学知识 + 设计分子-光谱评分器作为奖励模型 + MCTS 树搜索推理框架，在分子结构解析任务上将 GPT-4o-mini 和 GPT-4o 的性能提升超过 20%。

**[Brevity is the soul of sustainability: Characterizing LLM response lengths](brevity_is_the_soul_of_sustainability_characterizing_llm_response_lengths.md)**

:   系统研究 12 个 LLM 在 5 个数据集上的响应长度行为，发现 LLM 普遍生成远超必要的冗长回复（核心答案仅占 42%），并提出多种提示策略将响应长度缩短 25-88%、推理能耗降低 25-60%，同时保持甚至提升 ROUGE-L F1 质量。

**[Can Large Language Models Understand Internet Buzzwords Through User-Generated Content](buzzword_understanding_ugc.md)**

:   研究 LLM 能否通过用户生成内容（UGC）理解中文网络流行语——构建首个中文网络流行语数据集 Cheer（含定义和相关UGC），提出 Ress 方法引导 LLM 模拟人类语言学习过程来生成流行语定义，揭示了 LLM 在流行语理解上的三大共性挑战。

**[Automated CAD Modeling Sequence Generation from Text Descriptions via Transformer-Based Large Language Models](cadllm_cad_modeling_from_text.md)**

:   提出一个语言引导的 CAD 设计自动化框架——通过半自动数据标注流水线、Transformer CAD 生成器（TCADGen）和 LLM 增强模型（CADLLM）三个创新，从文本参数和外观描述自动生成 CAD 建模序列，在精度和效率上超越传统方法。

**[Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?](can_external_validation_tools_improve_annotation_quality_for_llm-as-a-judge.md)**

:   提出 Evaluation Agent，一个工具增强的 LLM-as-a-Judge 框架，通过集成网络搜索（事实核查）、代码执行和数学验证工具，在长文本事实验证上将与人类一致性从 63% 提升到 81%，在编程评估上从 31% 提升到 71%，且对无关领域几乎无退化。

**[Can Input Attributions Explain Inductive Reasoning in In-Context Learning?](can_input_attributions_explain_inductive_reasoning_in_in-context_learning.md)**

:   设计受控的合成归纳推理任务评估 4 种输入归因方法解释 ICL 的能力，发现最简单的梯度范数常常最好，但所有方法在不同任务和模型规模上表现不一致且不稳定——ICL 的可解释性比预期更难。

**[Can Language Models Reason about Individualistic Human Values and Preferences?](can_language_models_reason_about_individualistic_human_values_and_preferences.md)**

:   提出"个体价值对齐"范式，构建 IndieValueCatalog 数据集（基于世界价值观调查 WVS 的 9.3 万真人数据），评估并训练语言模型根据个人价值表达陈述推理其在新情境下的价值判断，揭示前沿 LM 仅达 55%-65% 准确率且存在显著的跨群体不公平性。

**[Can Large Language Models Address Open-Target Stance Detection?](can_large_language_models_address_open-target_stance_detection.md)**

:   提出开放目标立场检测（OTSD）任务——目标在训练时未见且不作为输入提供，系统评估了 GPT、Gemini、LLaMA、Mistral 四个系列共 8 个 LLM 在目标生成和立场检测两阶段的表现，发现 LLM 整体优于现有 TSE 方法，但在目标未显式出现时表现明显下降。

**[Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](can_llms_help_uncover_insights_about_llms_a_large-scale_evolving_literature_anal.md)**

:   本文提出半自动化文献分析管线，利用LLM从arXiv论文中自动抽取实验结果构建可持续更新的LLMEvalDB数据集（18127条记录/1737篇论文），并通过该数据集复现并扩展了关于CoT和ICL提示策略在不同任务类型上有效性的关键发现。

**[Can LLMs Interpret and Leverage Structured Linguistic Representations? A Case Study with AMRs](can_llms_interpret_and_leverage_structured_linguistic_representations_a_case_stu.md)**

:   本文系统评估了 LLM 利用抽象语义表示（AMR）进行下游任务的能力，发现 AMR 增强的 prompt 在长上下文任务（如对话摘要）中显著提升 Llama 3.1 零样本性能（余弦相似度从 66% 提升至 76%），但在短上下文任务中通常会降低性能。

**[Can LLMs Understand Unvoiced Speech? Exploring EMG-to-Text Conversion with LLMs](can_llms_understand_unvoiced_speech_exploring_emg-to-text_conversion_with_llms.md)**

:   本文提出了一种基于可训练 EMG 适配器模块的方法，将无声肌电图（EMG）信号映射到大语言模型（LLM）的输入嵌入空间，在闭合词汇无声 EMG 转文本任务中实现了 0.49 的词错误率（WER），仅需 6 分钟训练数据即比专用模型提升约 20%。

**[CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](cchall_a_novel_benchmark_for_joint_cross-lingual_and_cross-modal_hallucinations_.md)**

:   提出首个**联合跨语言与跨模态**幻觉检测基准 CCHall，覆盖 9 种语言和 4 类多模态数据集，系统评估 6 款主流 MLLM 在联合场景下的幻觉表现，揭示当前模型在该联合场景中 F1 比单独跨模态低 10.9、比单独跨语言低 3.4，且提出多语提示和外部工具辅助两条缓解路径。

**[CER: Confidence Enhanced Reasoning in LLMs](cer_confidence_enhanced_reasoning.md)**

:   提出置信度增强推理框架 CER——在 CoT 推理的每个中间步骤中量化关键 token（数学任务的数值/开放域的专有名词）的置信度，用步间置信度乘积评估整条推理链的可靠性，用置信度加权聚合替代简单多数投票，在数学和开放域任务上比 self-consistency 分别提升最高 7.4% 和 5.8%。

**[ChainEdit: Propagating Ripple Effects in LLM Knowledge Editing through Logical Rule-Guided Chains](chainedit_propagating_ripple_effects_in_llm.md)**

:   提出 ChainEdit 框架，通过将知识图谱中挖掘的逻辑规则与 LLM 内在逻辑推理能力对齐，实现知识编辑时的链式更新，将逻辑泛化准确率从约 20% 提升至 58-65%。

**[Enhancing Character-Level Understanding in LLMs through Token Internal Structure Learning](character_level_understanding.md)**

:   提出 TIPA（Token Internal Position Awareness）方法，通过在 tokenizer 词汇表上进行逆序字符预测训练，增强 LLM 对 token 内部字符结构和位置的感知能力，显著提升中文拼写纠错等字符级任务的表现。

**[Chronosense Exploring Temporal Understanding In Large Language Models With Time ](chronosense_exploring_temporal_understanding_in_large_language_models_with_time_.md)**

:   提出 ChronoSense 基准，系统评估 LLM 在 Allen 13 种时间区间关系和时间算术任务上的表现，揭示模型在时间理解方面的显著不足及对记忆的依赖。

**[Circuit Compositions: Exploring Modular Structures in Transformer-Based Language Models](circuit_compositions_modular_structures.md)**

:   通过在 PCFG SET 数据集上识别 10 个组合性字符串编辑操作的电路（circuits），研究 Transformer 中功能相关电路之间的模块化关系，发现功能相似的电路具有显著的节点重叠和跨任务忠实度，且电路可以通过集合运算（并集）组合以表示超出单个电路能力的更复杂功能。

**[CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs](cknowedit_chinese_knowledge_editing_dataset_llms.md)**

:   提出首个面向中文语言特征的知识编辑数据集 CKnowEdit，涵盖语言学、事实性和逻辑性三大类共10个子类的1,854条样本，揭示了当前知识编辑方法在中文场景下的不足。

**[Classifying Unreliable Narrators with Large Language Models](classifying_unreliable_narrators.md)**

:   借用叙事学理论定义三种不可靠叙事者类型，构建专家标注数据集 TUNa，系统评估 LLM 在零样本、少样本、微调和课程学习设定下的分类能力，发现该任务极具挑战性且课程学习对小模型有显著提升。

**[CodeMEnv: Benchmarking Large Language Models on Code Migration](codemenv_benchmarking_large_language_models_on_code_migration.md)**

:   提出 CodeMEnv，首个系统评估 LLM 跨环境代码迁移能力的基准，包含 922 个样本、19 个 Python/Java 包、3 个层次化任务（定位不兼容函数→描述变更→迁移代码），9 个 LLM 的平均 Pass@1 仅 26.50%，GPT-4o 最高 43.84%，揭示 LLM 更熟悉新版本函数且存在版本推理逻辑不一致问题。

**[CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models](codereviewqa_the_code_review_comprehension_assessment_for_large_language_models.md)**

:   提出 CodeReviewQA 基准，将代码审查自动修正（ACR）任务分解为三个中间推理步骤——变更类型识别（CTR）、变更定位（CL）、解决方案识别（SI），各自设计为不同难度的多选题探测，在 900 个人工验证的高质量样例（9 种语言）上评测 72 个 LLM，揭示了模型在代码审查理解中的具体弱点。

**[CogniBench: A Legal-inspired Framework and Dataset for Assessing Cognitive Faithfulness of Large Language Models](cognibench_cognitive_faithfulness.md)**

:   借鉴法律领域间接证据认定标准，提出分层评估框架和 CogniBench 数据集，首次系统性地定义和评估 LLM 在认知性陈述（推理、评价、解释）中的忠实度问题，并训练 CogniDet 检测器实现事实与认知幻觉的同时检测。

**[CogSteer: Cognition-Inspired Selective Layer Intervention for Efficiently Steering Large Language Models](cogsteer_cognition-inspired_selective_layer_intervention_for_efficiently_steerin.md)**

:   利用认知科学中的眼动数据分析 LLM 各层行为，发现中间层与人类注视相关性最高且最适合语义干预，提出 CogSteer 框架——仅微调最优单层（约 3% 参数）即可达到或超过全层微调的效果，在 GLUE/毒性控制任务上有效。

**[Enough Coin Flips Can Make LLMs Act Bayesian](coin_flips_bayesian.md)**

:   通过受控的有偏硬币抛掷实验，证明 LLM 在获得足够的上下文示例后能以贝叶斯方式更新其先验，但初始先验通常存在系统性偏差（偏向正面），且注意力幅度对贝叶斯推理影响甚微。

**[Combining The Best Of Both Worlds A Method For Hybrid Nmt And Llm Translation](combining_the_best_of_both_worlds_a_method_for_hybrid_nmt_and_llm_translation.md)**

:   提出基于源句特征的NMT与LLM混合翻译调度策略（PPLT与JDM），在保持翻译质量最优的同时将LLM调用比例降至约25-30%，大幅减少计算开销。

**[ComparisonQA: Evaluating Factuality Robustness of LLMs Through Knowledge Frequency Control and Uncertainty](comparisonqa_evaluating_factuality_robustness_of_llms_through_knowledge_frequenc.md)**

:   构建 ComparisonQA 基准（283K 配对问题），通过让高频和低频实体共享同一抽象问题实现受控对比，结合正确性和不确定性的两轮评估方法发现 LLM（包括 GPT-4o）对低频知识的鲁棒性极差。

**[CompileAgent: Automated Real-World Repo-Level Compilation with Tool-Integrated LLM-based Agent System](compileagent_automated_real-world_repo-level_compilation_with_tool-integrated_ll.md)**

:   提出 CompileAgent，首个面向仓库级代码编译的 LLM Agent 框架，集成五种专用工具和流程化 Agent 策略，在 100 个 C/C++ 真实项目的 CompileAgentBench 上将编译成功率最高提升 71%，平均每个项目仅需 $0.22。

**[Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability](compositional_generalization_instruction.md)**

:   提出 Ordered CommonGen 基准，通过要求 LLM 按指定顺序生成包含所有概念的句子，同时评估组合泛化与指令遵循能力，在 36 个 LLM 上发现即使最强模型也仅能达到约 75% 的有序覆盖率。

**[Computation Mechanism Behind LLM Position Generalization](computation_mechanism_behind_llm_position_generalization.md)**

:   揭示 LLM 注意力 logit 学习了位置相关性和语义重要性的近似算术加法解耦（$W_{i,j} \approx f(\mathbf{q}, i-j) + g(\mathbf{q}, \mathbf{k})$，线性相关 0.959），发现了使这种解耦成立的中间表示模式，并用此解释了 LLM 的位置排列容忍性和长度泛化能力。

**[How Humans and LLMs Organize Conceptual Knowledge: Exploring Subordinate Categories in Italian](conceptual_knowledge_org.md)**

:   通过构建首个意大利语下位类别心理语言学数据集（187 个基本类别），系统对比了人类和 LLM 在下位概念层级上的类别组织结构，发现两者的对齐度较低但在不同语义领域存在显著差异。

**[Conformity in Large Language Models](conformity_in_large_language_models.md)**

:   将心理学中的 Asch 从众实验范式迁移到 LLM 上，系统研究了 LLM 的从众行为（conformity），发现所有模型都会受多数意见影响改变答案，且不确定性越高越容易从众，并提出 Devil's Advocate 和 Question Distillation 两种干预方法有效缓解从众效应。

**[ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities](consistencychecker_tree_evaluation.md)**

:   ConsistencyChecker 提出基于自一致性树（self-consistency tree）的无参考 LLM 评估框架，通过构建可逆变换的树状多步路径（如多语言往返翻译、代码等价重写），量化模型在迭代变换中的语义/功能保持能力，动态生成 benchmark 从根源消除数据泄露，且与 WMT 2024 权威排名的相关性 r > 0.7，证明无需配对数据即可可靠评估 LLM 泛化能力。

**[Context-Robust Knowledge Editing for Language Models](context-robust_knowledge_editing_for_language_models.md)**

:   发现现有知识编辑方法在前缀上下文存在时大幅失败（编辑成功率从 90.9% 降至 69.1%），提出 CHED 基准评估上下文鲁棒性，并设计 CoRE 方法通过多样化前缀上下文 + 跨前缀隐藏状态方差正则化来增强编辑的上下文鲁棒性，在保持模型通用能力的同时显著缩小有/无上下文的性能差距。

**[Contrastive Perplexity for Controlled Generation: An Application in Detoxifying Large Language Models](contrastive_perplexity_controlled_gen.md)**

:   提出基于原型对比困惑度（Contrastive Perplexity, CP）的框架，通过构造语义相似但毒性属性不同的正负样本对，在困惑度空间中进行对比学习来微调 LLM，实现显著的毒性降低（Mistral-7b 毒性从 33.1% 降至 4.3%）且几乎不影响下游任务性能。

**[Contrastive Prompting Enhances Sentence Embeddings in LLMs through Inference-Time Steering](contrastive_prompting_embeddings.md)**

:   提出对比提示（Contrastive Prompting, CP）方法，通过引入辅助提示（引导编码非核心信息）并在推理时与正常提示的激活值做对比减法，过滤掉停用词等无关语义，使 LLM 的句子嵌入更聚焦核心语义，在 STS 和分类任务上一致提升现有提示方法。

**[Convert Language Model into a Value-based Strategic Planner](convert_language_model_into_a_value-based_strategic_planner.md)**

:   提出 straQ* 框架，将 LLM 转化为基于 Q-learning 的策略规划器，用平均 logit 作为 Q 值实现策略级 MDP，在情感支持对话中基于长期回报选择最优策略，超越直接推理、CoT 和微调等基线。

**[COSMIC: Generalized Refusal Direction Identification in LLM Activations](cosmic_generalized_refusal_direction_identification_in_llm_activations.md)**

:   提出 COSMIC（Cosine Similarity Metrics for Inversion of Concepts），一种基于余弦相似度的自动化方向选择框架，无需依赖模型输出 token 或预定义的拒绝模板即可在 LLM 激活空间中识别拒绝方向，在对抗场景和弱对齐模型中仍能有效执行拒绝引导。

**[Cross-Lingual Optimization for Language Transfer in Large Language Models](cross-lingual_optimization_for_language_transfer_in_large_language_models.md)**

:   提出 Cross-Lingual Optimization (CLO)，通过修改 DPO 损失函数实现跨语言偏好优化——给目标语言输入时偏好目标语言回复、给英语输入时偏好英语回复——在 5 个模型 × 6 种语言上一致超越 SFT，低资源语言中仅 3,200 样本的 CLO 即超越 6,400 样本的 SFT。

**[Cross-Lingual Transfer of Debiasing and Detoxification in Multilingual LLMs: An Extensive Investigation](cross-lingual_transfer_of_debiasing_and_detoxification_in_multilingual_llms_an_e.md)**

:   在 7 个 LLM 和 20 种语言上系统研究了英语去偏见/去毒化微调的跨语言迁移效果，发现 SFT 有效去偏见、DPO 有效去毒化，但迁移到非英语语言时普遍伴随语言生成能力下降（语言一致性、流畅度、多样性均受损），迁移效果可由预训练数据中目标语言的数据量预测。

**[Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](cross_model_transferability_sv.md)**

:   提出 L-Cross Modulation 方法，通过简单线性变换将一个 LLM 的概念方向向量（steering vectors）迁移到另一个 LLM 中实现行为控制，发现三个关键结论：(1) 跨模型 SV 迁移有效；(2) 不同概念共享同一变换矩阵；(3) 小模型的 SV 可以控制大模型（弱到强迁移）。

**[Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models](crosslingual_pitfalls.md)**

:   提出基于束搜索和 LLM 仿真的自动化方法来高效发现多语言 LLM 的跨语言弱点，构建了覆盖 16 种语言的 6000+ 双语问答对数据集，揭示即使 GPT-4o 也存在超过 30% 的跨语言性能下降。

**[Cultural Learning-Based Culture Adaptation of Language Models](cultural_learning-based_culture_adaptation_of_language_models.md)**

:   提出 CLCA 框架，借鉴文化学习理论，通过模拟社会交互生成文化适配对话数据，结合意图理解进行多任务训练，在 World Values Survey 上显著提升多种 LLM 的文化价值观对齐。

**[Culture is Not Trivia: Sociocultural Theory for Cultural NLP](culture_is_not_trivia_sociocultural_theory_for_cultural_nlp.md)**

:   提出基于社会文化理论的文化 NLP 框架，批判现有将文化简化为"常识琐事"的做法，主张文化应被理解为动态的、情境化的社会建构过程，而非静态的知识标签。

**[Data Caricatures: On the Representation of African American Language in Pretraining Corpora](data_caricatures_on_the_representation_of_african_american_language_in_pretraini.md)**

:   结合定量实验、人工判断和定性分析，系统评估了 12 个开源预训练语料库中非裔美国人语言（AAL）的数量与质量：发现 AAL 仅占 0.007%–0.18% 的文档（远低于人口比例），C4 中 28.9% 的 AAL 文本被判为不适合 LLM 生成、24.5% 强化有害刻板印象，且 16 种自动过滤器中有 13 种系统性地偏向保留白人主流英语（WME）而非 AAL。

**[Data Whisperer: Efficient Data Selection for Task-Specific LLM Fine-Tuning via Few-Shot In-Context Learning](data_whisperer_data_selection.md)**

:   Data Whisperer 提出一种无需训练的注意力加权 few-shot ICL 数据选择方法，利用预训练模型自身的 ICL 能力和注意力分数为训练样本打分，仅用 10% 数据即可超越全量微调性能，同时比现有方法快 7-20 倍。

**[DeAL: Decoding-time Alignment for Large Language Models](deal_decoding_time_alignment.md)**

:   DeAL 将 LLM 对齐问题重新形式化为解码时的启发式搜索问题，在推理阶段利用可定制的奖励函数（包括程序化约束和参数化 reward model）引导 token 选择，实现了灵活的多目标对齐且可与 RLHF 互补叠加。

**[Defense Against Prompt Injection Attack by Leveraging Attack Techniques](defense_prompt_injection.md)**

:   本文提出一种"以攻为防"的 prompt injection 防御策略：将已有的攻击技术（ignore、escape、fake completion）反转用于防御，在被注入的数据内容后追加 shield prompt + 原始指令，使 LLM 忽略注入指令而执行原始指令，在多种攻击场景下将 ASR 降至接近零。

**[When People are Floods: Analyzing Dehumanizing Metaphors in Immigration Discourse with Large Language Models](dehumanizing_metaphors_immigration.md)**

:   提出结合 LLM 词级隐喻检测与 SBERT 篇章级语义关联的计算框架，在 40 万条美国移民推文上揭示保守派更多使用去人化隐喻、但生物类隐喻对自由派的用户互动效应更强的复杂图景。

**[Deontological Keyword Bias: The Impact of Modal Expressions on Normative Judgments of Language Models](deontological_keyword_bias.md)**

:   本文揭示LLM存在"义务论关键词偏见"(DKB)——当提示中包含"must"、"ought to"等模态义务表达时，模型会将超过90%的常识场景误判为义务，并提出基于少样本示例与推理提示的去偏策略。

**[Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](derta_decoupled_refusal.md)**

:   发现标准安全微调数据存在"拒绝位置偏差"——模型只学会在回答开头拒绝，中途发现不安全时无法中断。提出 DeRTa（Decoupled Refusal Training），通过"有害前缀+安全拒绝"的 MLE 训练和在每个位置模拟"从有害到安全"转换的 RTO 训练，让 LLM 能在回答的任何位置感知到不安全时拒绝，在六种攻击场景下超越 GPT-4 和 LLaMA3-Instruct。

**[Detecting Referring Expressions in Visually Grounded Dialogue with Autoregressive Models](detecting_referring_expressions_in_visually_grounded_dialogue_with_autoregressiv.md)**

:   提出使用自回归模型在视觉对话中检测指代表达（referring expressions），将 RE 检测建模为序列标注任务的自回归变体，在 PhotoBook 和 MeetUp 数据集上实现 SOTA。

**[DICE-Bench: Evaluating the Tool-Use Capabilities of Large Language Models in Multi-turn Settings](dice-bench_evaluating_the_tool-use_capabilities_of_large_language_models_in_mult.md)**

:   提出 DICE-Bench 基准评估 LLM 在多轮对话中的工具使用能力，涵盖工具发现、调用、错误恢复和组合使用四个维度，发现即使最强模型在复杂多轮场景下也仅达 ~60% 成功率。

**[DiffLM: Controllable Synthetic Data Generation via Diffusion Language Models](difflm_controllable_synthetic_data_generation_via_diffusion_language_models.md)**

:   提出 DiffLM，将扩散模型应用于文本合成数据生成，通过引导函数实现对生成文本属性的精细控制，在多个下游任务上生成的合成数据质量超越 GPT-4 和传统增强方法。

**[Direct Confidence Alignment: Aligning Verbalized Confidence with Internal Confidence](direct_confidence_alignment_aligning_verbalized_confidence_with_internal_confide.md)**

:   通过 DPO 将 LLM 的外化置信度（文字表达的概率）与内部置信度（token 概率）对齐，提升模型的透明度和可信度，Gemma-2-9B 上表现最佳。

**[DiSCo: Device-Server Collaborative LLM-Based Text Streaming Services](disco_device-server_collaborative_llm-based_text_streaming_services.md)**

:   提出 DiSCo 设备-服务器协作 LLM 文本流服务框架，端侧小模型快速生成初始 token 减少首 token 延迟（TTFT），服务端大模型并行处理后替换，实现低延迟高质量的文本流式服务。

**[Disentangling Language and Culture for Evaluating Multilingual Large Language Models](disentangle_language_culture.md)**

:   提出 Dual Evaluation Framework，将多语言 LLM 评估沿"语言媒介"和"文化语境"两个维度解耦，发现"文化-语言协同"(Cultural-Linguistic Synergy) 现象——模型在文化语境与提问语言对齐时表现更好，并通过 FFN 神经元激活分析从可解释性角度给出解释。

**[Disentangling Memory and Reasoning Ability in Large Language Models](disentangle_memory_reasoning.md)**

:   提出将 LLM 的推理过程显式分解为"记忆回忆"和"逻辑推理"两个步骤——引入 `<memory>` 和 `<reason>` 两个可学习特殊 token 标记每步是知识回忆还是逻辑推理，用双 LLM 框架生成训练数据后 LoRA 微调，在 StrategyQA/CommonsenseQA/TruthfulQA 上提升性能并增强可解释性，8B 模型在 TruthfulQA 上超越 GPT-4o。

**[DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts](dive_moe_reconstruction.md)**

:   提出 DIVE，一种将 Dense LLM 重构为 MoE 架构的方法，核心洞察是不同领域的校准数据集会让结构化剪枝产生不同的剪枝结果，利用这种多样性构建领域特异的专家，配合高效的两阶段重训练（router dense训练 + expert LoRA稀疏训练），在仅调不到 1% 参数的情况下实现优于现有剪枝和 MoE 重构方法的效果。

**[Diversity-oriented Data Augmentation with Large Language Models](diversity_data_augmentation.md)**

:   提出 DoAug 框架，通过 SFT+DPO 微调 LLM 释义器并结合核心集选择与多样性采样，在保持语义一致性的同时显著提升增强数据集的多样性，在 12 个数据集上平均性能提升 10.52%，超出次优基线 3.76 个百分点。

**[Diversity Explains Inference Scaling Laws: Through a Case Study of Minimum Bayes Risk Decoding](diversity_explains_inference_scaling_laws_through_a_case_study_of_minimum_bayes_.md)**

:   从 bias-diversity 分解的理论视角重新解释 MBR 解码：质量估计误差 MSE = Bias - Diversity，增加 diversity（伪参考的多样性）是提升 MBR 性能的关键；进一步通过信息论扩展到一般推理方法，揭示 diversity 是推理 scaling law（增加采样提升性能但边际递减）的理论根源，并在机器翻译、摘要、图像描述任务上实证验证。

**[Do Language Models Mirror Human Confidence?](do_language_models_mirror_human_confidence_exploring_psychological_insights_to_a.md)**

:   探索 LLM 的置信度是否呈现与人类类似的心理学模式（如过度自信效应、达克效应），在 MMLU 等基准上发现 LLM 确实存在类人的过度自信偏差，但在某些维度上也有独特模式。

**[Do Language Models Understand Honorific Systems in Javanese?](do_language_models_understand_honorific_systems_in_javanese.md)**

:   首次系统评估 LLM 对爪哇语敬语系统的理解能力，构建专门测试集发现即使是最强模型对复杂敬语层级的掌握也仅约 60% 准确率。

**[Do Language Models Understand the Cognitive Tasks Given to Them?](do_language_models_understand_the_cognitive_tasks_given_to_them_investigations_w.md)**

:   用 N-back 任务系统分析 LLM 认知任务理解能力，发现性能低下的主因是任务理解不足而非工作记忆限制，挑战了 LLM 工作记忆容量约 3 的结论。

**[Do Large Language Models Perform Latent Multi-Hop Reasoning without Exploiting Shortcuts?](do_large_language_models_perform_latent_multi-hop_reasoning_without_exploiting_s.md)**

:   构建无快捷方式的评估数据集 SOCRATES，系统评估 41 个 LLM 在潜在多跳推理中的真实能力，发现模型在国家类桥接实体上可达 80% 组合率，但年份类仅约 5%。

**[Do LLMs Give Psychometrically Plausible Responses in Educational Assessments?](do_llms_give_psychometrically_plausible_responses_in_educational_assessments.md)**

:   从心理测量学角度评估 18 个 LLM 在教育评估中的表现，发现大模型过度自信且无法预测干扰项选择模式。

**[Does Time Have Its Place? Temporal Heads Where Language Models Recall Time-specific Information](does_time_have_its_place_temporal_heads_where_language_models_recall_time-specif.md)**

:   通过 EAP-IG 电路分析在 Llama-2/Qwen/Phi-3 中发现了专门处理时间条件知识的"时间头"（Temporal Heads），消融这些头只降低时间知识准确率（降 3-9%）而不影响时间无关知识和通用 QA，并展示了通过注入时间头激活值实现选择性时间知识编辑的可能性。

**[DRAMA: Diverse Augmentation from LLMs to Smaller Dense Retrievers](drama_diverse_augmentation_from_large_language_models_to_smaller_dense_retriever.md)**

:   通过多策略 LLM 数据增强+知识蒸馏创建小型高效检索器 Drama 0.3B，在 BEIR 上达到与 1B 模型相当的性能。

**[Dynamic Knowledge Integration for Evidence-Driven Counter-Argument Generation](dynamic_knowledge_integration_for_evidence-driven_counter-argument_generation_wi.md)**

:   提出动态网络知识检索框架提升反驳论证生成质量，构建新评估数据集并用 LLM-as-Judge 进行评估。

**[ECLM: Entity Level Language Model for Spoken Language Understanding with Chain of Intent](eclm_entity_level_language_model_spoken_language_understanding.md)**

:   提出 ECLM 框架，将 LLM 应用于多意图口语理解：通过将 token 级槽填充转化为实体识别任务解决序列对齐问题，引入"意图链"（Chain of Intent）实现逐步多意图识别，在 MixATIS 和 MixSNIPS 上大幅超越 SOTA 基线。

**[Edit Once, Update Everywhere: Cross-Lingual Knowledge Synchronization](edit_once_update_everywhere_a_simple_framework_for_cross-lingual_knowledge_synch.md)**

:   提出 X-KDE 框架通过指令微调+偏好优化实现知识的跨语言同步编辑——在一种语言中编辑知识后自动在其他语言同步生效。

**[EdiText: Controllable Coarse-to-Fine Text Editing with Diffusion Language Models](editext_diffusion_text_editing.md)**

:   提出 EdiText，基于嵌入扩散模型（LD4LG）的可控文本编辑框架，通过将 SDEdit 技术从图像域迁移到文本域实现粗粒度编辑（控制加噪时间步），并创新性地利用自条件化（self-conditioning）机制实现细粒度编辑（将参考文本嵌入注入为去噪条件），两者结合实现从粗到细的多粒度文本属性编辑。

**[ELABORATION: A Comprehensive Benchmark on Human-LLM Competitive Programming](elaboration_competitive_programming.md)**

:   提出ELABORATION——首个全面评估人类-LLM协作竞赛编程的基准，包含覆盖编程全流程（理解→规划→编码→调试）的人类反馈分类体系和8320题精标注数据集，实验表明LLM在困难题上仅3.4% Pass@1，但人类反馈（特别是在编码阶段）可平均提升9.3%。

**[ELI-Why: Evaluating the Pedagogical Utility of Language Model Explanations](eli-why_evaluating_the_pedagogical_utility_of_language_model_explanations.md)**

:   构建了包含 13.4K "Why" 问题的 ELI-Why 基准，通过两项人类研究发现 GPT-4 生成的面向不同教育水平的解释仅 50% 能匹配目标年级（人工策划达 79%），且对学习者信息需求的满足度比人类答案低 20%。

**[Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation](emergent_abilities_continued_pt.md)**

:   揭示了持续预训练（CPT）进行语言适应时，混入英文数据对保留模型上下文学习（ICL）能力和下游涌现能力至关重要——尽管不影响验证困惑度；并提出课程学习和 EMA 权重平均作为替代方案。

**[Enhancing Lexicon-Based Text Embeddings with Large Language Models](enhancing_lexicon-based_text_embeddings_with_large_language_models.md)**

:   用 LLM 增强基于词典的稀疏文本嵌入，在保持可解释性的同时提升检索性能。

**[Enhancing Transformation from Natural Language to Signal Temporal Logic using LLMs](enhancing_transformation_from_natural_language_to_signal_temporal_logic_using_ll.md)**

:   用 LLM 改进自然语言到信号时序逻辑（STL）的转换，提出两阶段方法（语义解析+逻辑生成）。

**[Growing Through Experience: Scaling Episodic Grounding in Language Models](episodic_grounding_experience.md)**

:   提出一个 weak-to-strong episodic grounding 框架，利用 MCTS 收集结构化经验数据，通过行为比率蒸馏将小模型的 episodic grounding 能力迁移到大模型，结合 DPO 优化实现从成功和失败经验中学习，在物理规划任务上超越 GPT-4o 等 SOTA 模型 3.45%。

**[Efficient and Accurate Prompt Optimization: the Benefit of Memory in Exemplar-Guided Reflection](erm_prompt_optimization_memory.md)**

:   提出 ERM 方法，通过指导性元提示生成带详细解题过程的 exemplar 来增强 feedback 质量，并引入 Feedback Memory 和 Exemplar Factory 两种长期记忆机制来高效存储和复用历史反馈与示例，在多个任务上以约一半的优化步数超越了 SOTA prompt 优化方法。

**[EscapeBench: Towards Advancing Creative Intelligence of Language Model Agents](escapebench_creative_agent.md)**

:   提出EscapeBench密室逃脱游戏基准（36个场景、3种难度）评估LM agent的创造性智能，并设计EscapeAgent通过Foresight（工具使用假设生成）和Reflection（未解任务追踪）模块将提示依赖降低约50%，但仍远落后于人类。

**[Evaluating Implicit Bias in LLMs by Attacking from a Psychometric Perspective](evaluating_implicit_bias_in_large_language_models_by_attacking_from_a_psychometr.md)**

:   借鉴心理测量学中的隐式联想测验（IAT）方法评估 LLM 的隐式偏见，发现模型存在系统性偏见且与人类偏见模式部分相似。

**[Evaluating Language Models as Synthetic Data Generators](evaluating_lms_synthetic_data_gen.md)**

:   提出 AgoraBench 基准，系统评估 6 个 LLM 在 3 个领域×3 种数据生成方式下的数据生成能力，通过训练 99 个学生模型发现：LLM 的数据生成能力与问题求解能力不直接相关，GPT-4o 在实例生成上最强而 Claude-3.5-Sonnet 在质量增强上最强。

**[Evaluation of Attribution Bias in Generator-Aware Retrieval-Augmented Large Language Models](evaluation_of_attribution_bias_in_generator-aware_retrieval-augmented_large_lang.md)**

:   定义并研究 RAG 中 LLM 对作者身份信息的归因敏感性和偏差，通过反事实评估发现告知 LLM 文档作者身份可显著改变归因质量 3-18%，且 LLM 存在对人类作者身份的归因偏差。

**[LLMs Can Simulate Standardized Patients via Agent Coevolution](evopatient_standardized_patient.md)**

:   EvoPatient 提出了一个多智能体协同进化框架，通过患者 Agent 和医生 Agent 之间的自主模拟对话，让 LLM 无需人工监督即可学会模拟标准化病人（SP），在需求对齐度上超过现有推理方法 10%+。

**[EXECUTE: A Multilingual Benchmark for LLM Token Understanding](execute_a_multilingual_benchmark_for_llm_token_understanding.md)**

:   扩展字符理解基准 CUTE 到 8 种语言和多种文字系统，提出 EXECUTE 框架，发现 LLM 在不同语言的字符/词/子字符级别表现差异巨大，且意外发现 LLM 对越不熟悉的语言反而在 token 理解任务上表现越好。

**[Explain-then-Process: Using Grammar Prompting to Enhance Grammatical Acceptability](explain-then-process_using_grammar_prompting_to_enhance_grammatical_acceptabilit.md)**

:   提出先解释语法规则再判断可接受性的 Explain-then-Process 策略，在语法可接受性判断任务上超越直接 prompting 和 CoT。

**[ExpliCa: Evaluating Explicit Causal Reasoning in Large Language Models](explica_evaluating_explicit_causal_reasoning_in_large_language_models.md)**

:   提出 ExpliCa 数据集（4800 条问题，含因果和时间连接词），首次整合因果和时间关系评估并配以众包人类评分，发现即使顶级模型准确率也难超 0.80，且模型系统性地将时间关系误判为因果关系。

**[Explicit vs. Implicit: Investigating Social Bias in Large Language Models through Self-Reflection](explicit_vs_implicit_investigating_social_bias_in_large_language_models_through_.md)**

:   借鉴社会心理学中隐式联想测验（IAT）和自我报告评估（SRA），提出自反思评估框架系统研究 LLM 的显式和隐式偏见，发现 LLM 与人类一样存在显式-隐式偏见不一致——显式偏见轻微但隐式偏见强烈，且模型越大/对齐训练越多，这种不一致越严重。

**[Exploring Explanations Improves the Robustness of In-Context Learning](exploring_explanations_improves_the_robustness_of_in-context_learning.md)**

:   提出 X²-ICL 框架，通过在上下文学习的示例中为所有可能的标签（而非仅观测标签）生成解释推理路径，系统性地探索隐变量推理空间，从而显著提升 ICL 在分布外（OOD）数据上的鲁棒性——在 5 个 LLM 上的 8 个 OOD 数据集中，X²-ICL 在 6-8 个上超越 ICL 和 X-ICL。

**[Exploring Graph Representations of Logical Forms for Language Modeling](exploring_graph_representations_of_logical_forms_for_language_modeling.md)**

:   提出 GFoLDS，一种在 DMRS 逻辑形式图表示上预训练的图 Transformer 语言模型，并提出"语言知识催化假说"(LKCH)：逻辑形式语言模型几乎立刻学会基础语言现象，进而加速复杂模式学习，在相同数据量下大幅超越 BERT。

**[Exploring the Impact of Instruction-Tuning on LLMs' Susceptibility to Misinformation](exploring_the_impact_of_instruction-tuning_on_llms_susceptibility_to_misinformat.md)**

:   首次系统研究指令微调如何影响 LLM 对虚假信息的易感性，发现指令微调使模型从偏信 assistant-role 转变为偏信 user-role，当虚假信息以独立 user-turn 呈现时易感性最高，揭示了指令微调的"副作用"。

**[HiCUPID: Exploring the Potential of LLMs as Personalized Assistants](exploring_the_potential_of_llms_as.md)**

:   提出 HiCUPID，首个全面满足个性化 AI 助手五大需求（用户信息遵循、隐含信息理解、多信息推理、长上下文建模、主动性回复）的基准，含 1,250 用户 × 25 人格 × 10 日程 + Llama-3.2 自动评估模型。

**[Exposing Numeracy Gaps: A Benchmark to Evaluate Fundamental Numerical Abilities in Large Language Models](exposing_numeracy_gaps_a_benchmark_to_evaluate_fundamental_numerical_abilities_i.md)**

:   提出 NumericBench 综合基准，通过 6 类数据集评估 LLM 的 6 种基本数值能力（数字识别、算术运算、上下文检索、比较、汇总、逻辑推理），发现包括 GPT-4o、DeepSeek-V3 在内的 SOTA 模型在简单数值任务上仍表现极差，并深入分析了 5 种根因。

**[Factual Knowledge in Language Models: Robustness and Anomalies under Simple Temporal Context Variations](factual_knowledge_in_language_models_robustness_and_anomalies_under_simple_tempo.md)**

:   发布 TimeStress 数据集（521K 陈述，2003 条时间事实），评估 18 个 LLM 在时间上下文变化下的事实知识鲁棒性，发现最好的模型仅对 11% 的事实实现完美鲁棒，且存在人类不会犯的关键错误。

**[Fairsteer Inference Time Debiasing For Llms With Dynamic Activation Steering](fairsteer_inference_time_debiasing_for_llms_with_dynamic_activation_steering.md)**

:   提出 FairSteer，一种推理时去偏框架，通过轻量线性分类器检测激活中的偏见信号，再用对比 prompt 对计算的去偏转向向量（DSV）动态调整隐藏层激活，无需重训即可在多任务上有效缓解 LLM 的社会偏见。

**[FlashBack: Efficient Retrieval-Augmented Language Modeling for Fast Inference](flashbackefficient_retrieval-augmented_language_modeling_for_long_context_infere.md)**

:   针对检索增强语言模型(RALM)中因检索内容前置(prepending)导致 KV cache 反复重算的推理效率问题，提出 FlashBack，将检索内容后置(appending)以保留输入的 KV cache，并用 Marking Token + LoRA 微调适配新的上下文模式，在 Llama 2-7B 上实现最高 4 倍推理加速且 perplexity 持平。

**[FoodTaxo: Generating Food Taxonomies with Large Language Models](foodtaxo_generating_food_taxonomies_with_large_language_models.md)**

:   提出 FoodTaxo，基于 Llama-3 的迭代自底向上分类法生成与补全算法，利用 CoT 提示 + RAG 检索 + NLI 验证三阶段流程，从已知叶节点概念出发逐步构建层次化 taxonomy；在五个基准数据集上与 TacoPrompt 等 SOTA 方法竞争，同时通过 reference-free 指标和消融实验揭示了非叶节点放置这一根本性瓶颈。

**[A Survey on Foundation Language Models for Single-cell Biology](foundation_lm_single_cell_survey.md)**

:   首篇从语言建模视角系统综述单细胞生物学基础语言模型的工作，将现有模型划分为 PLM（从头预训练）和 LLM（利用已有大模型）两大类，全面分析了数据 tokenization 策略、预训练/微调范式以及下游任务。

**[FR-Spec: Accelerating Large-Vocabulary Language Models via Frequency-Ranked Speculative Sampling](fr_spec_speculative_sampling.md)**

:   发现大词表LLM（如LLaMA-3的128k词表）中投机采样的瓶颈从Transformer层转移到LM Head，提出FR-Spec通过频率排序将草稿模型的词表压缩75%（128k→32k），在EAGLE-2基础上额外获得1.12×加速，且保证最终输出分布数学等价。

**[From Data to Knowledge: Evaluating How Efficiently Language Models Learn Facts](from_data_to_knowledge_evaluating_how_efficiently_language_models_learn_facts.md)**

:   首次直接研究事实在预训练数据中出现频次与 LLM 能否回忆该事实之间的关系，提出两种样本效率指标，发现不同架构/规模的模型在高频事实上表现相似但在低频事实上差异显著——低频事实的学习能力是区分模型样本效率的关键。

**[From Misleading Queries to Accurate Answers: A Three-Stage Fine-Tuning Method for LLMs](from_misleading_queries_to_accurate_answers_a_three-stage_fine-tuning_method_for.md)**

:   提出三阶段微调方法（误导检测->查询纠正->准确回答）增强 LLM 处理含误导信息输入的能力，在误导检测和 QA 任务上显著提升准确率，同时减少幻觉生成。

**[From Selection to Generation: A Survey of LLM-based Active Learning](from_selection_to_generation_a_survey.md)**

:   首篇系统综述 LLM 时代的主动学习（Active Learning），提出以 Querying（选择/生成）和 Annotation（标注）为核心的分类体系，全面梳理 LLM 如何变革传统主动学习的选择-标注流程。

**[From Selection To Generation A Survey Of Llm-Based Active Learning](from_selection_to_generation_a_survey_of_llm-based_active_learning.md)**

:   首篇系统梳理 LLM 时代主动学习的综述，提出以 Querying（从传统选择到 LLM 生成）和 Annotation（从人工标注到 LLM 标注）为双轴的统一分类体系，覆盖查询策略、标注方案、停止准则、AL 范式和应用领域。

**[From Tools to Teammates: Evaluating LLMs in Multi-Session Coding Interactions](from_tools_to_teammates_evaluating_llms_in_multi-session_coding_interactions.md)**

:   提出 MemoryCode 合成多会话数据集评估 LLM 在长期交互中追踪和执行编码指令的能力，发现即使 GPT-4o 在提供完整对话历史时准确率也下降 67%，揭示了当前 LLM 在前瞻性记忆和信息整合上的根本局限。

**[GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding](galla_graph_aligned_large_language_models.md)**

:   提出 GALLa，通过 GNN 编码代码的 AST/DFG 结构图并用跨模态适配器对齐到 LLM 嵌入空间，在微调时作为辅助任务注入代码结构信息，推理时丢弃 GNN 和 adapter 实现零额外开销，在 5 个代码任务 × 7 个基线 LLM（350M-14B）上持续提升。

**[Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](gapo_multi_objective_alignment.md)**

:   提出GAPO，一种基于梯度自适应缩放的多目标策略优化方法，利用多梯度下降算法(MGDA)结合梯度归一化，平衡LLM在帮助性和无害性等冲突目标间的权衡，并通过P-GAPO支持用户偏好驱动的Pareto前沿生成。

**[GAPO: Learning Preferential Prompt through Generative Adversarial Policy Optimization](gapo_preferential_prompt.md)**

:   提出 GAPO（Generative Adversarial Policy Optimization）框架，将 GAN 的对抗训练机制与 PPO 结合，使用 encoder-only 奖励模型替代传统 decoder-only 架构，通过"Preferential Prompt"（修改 prompt 中的约束而非 response）的新范式来增强 LLM 对细粒度约束的理解和遵循能力，在 IFEval 和产品描述生成任务上大幅超越 DPO/KTO/SimPO 等基线。

**[Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models](generative_psycholexical_approach_for_constructing_value.md)**

:   提出生成式心理词汇方法（GPLA），自动化构建面向LLM的五因素价值体系（社会责任、冒险性、规则遵循、自我效能、理性），在结构效度、安全预测和价值对齐上优于经典Schwartz人类价值体系。

**[Genetic Instruct: Scaling up Synthetic Generation of Coding Instructions for Large Language Models](genetic_instruct_scaling_up_synthetic_generation_of_coding_instructions_for_larg.md)**

:   提出 Genetic-Instruct 算法，借鉴进化算法的交叉和变异操作，从 512 个种子指令扩展生成 750 万+高质量编码指令，使用 Instructor-LLM/Coder-LLM/Judge-LLM 三角色流水线，训练后的模型在代码生成基准上超越 Self-Instruct 和 Evol-Instruct。

**[GenKnowSub: Improving Modularity and Reusability of LLMs through General Knowledge Substitution](genknowsub_improving_modularity_and_reusability_of_llms_through_general_knowledg.md)**

:   提出 GenKnowSub 框架通过通用知识替换改善 LLM 的模块化和可重用性，实现知识组件的即插即用。

**[Towards Geo-Culturally Grounded LLM Generations](geocultural_grounded_llm.md)**

:   研究 RAG/搜索增强技术对 LLM 文化意识的影响——搜索增强显著提升了文化命题知识的选择题表现，但也增加了刻板印象风险，且在开放式文化流畅性的人工评估中改进不显著，揭示了"文化知识"和"文化流畅性"的本质区别。

**[Geometric Signatures of Compositionality Across a Language Model's Lifetime](geometric_compositionality_lifetime.md)**

:   通过将数据集的组合性程度与语言模型表示的非线性内在维度(I_d)和线性有效维度(d)联系起来，揭示了一个形式-意义二分：非线性 I_d 编码有意义的组合语义复杂度，而线性 d 编码表面词形复杂度；该对应关系在训练过程中随语言能力涌现而建立。

**[Efficient Universal Goal Hijacking with Semantics-guided Prompt Organization](goal_hijacking_attack.md)**

:   本文提出POUGH方法，通过高效的渐进式优化算法和两种语义引导的提示组织策略（采样策略+排序策略），实现了对LLM的高效通用目标劫持攻击，在四个开源LLM和十种恶意目标响应上平均攻击成功率达93.41%。

**[What Makes a Good Natural Language Prompt?](good_natural_language_prompt.md)**

:   通过元分析150+篇prompting相关论文和博客，提出一个以属性为中心、以人为中心的prompt质量评估框架，涵盖6个维度21个属性，并发现单属性增强往往比多属性组合更有效。

**[GORP: Continual Gradient Low-Rank Projection Fine-Tuning for LLMs](gorp_continual_gradient_projection.md)**

:   GORP 提出将全秩参数和 LoRA 低秩参数的梯度统一投影到低秩梯度子空间中联合更新，利用 Adam 一阶矩隐式构建跨任务共享梯度空间来缓解灾难性遗忘，在 T5 和 LLaMA2 上持续学习性能接近多任务联合训练上界。

**[Can Graph Descriptive Order Affect Solving Graph Problems with LLMs?](graph_descriptive_order_llm.md)**

:   首次系统研究了图描述顺序（BFS、DFS、PageRank、PPR）对LLM解决图推理问题的影响，发现有序描述显著优于随机描述，且不同任务偏好不同的排列策略。

**[Group then Scale: Dynamic Mixture-of-Experts Multilingual Language Model](group_then_scale_dynamic_mixture-of-experts_multilingual_language_model.md)**

:   提出 DMoE——基于参数偏差的动态语言分组 + 选择性 MoE 层扩展方法，通过仅 10 步微调量化语言间相似性，将相似语言分组共享同一 expert，只在参数偏差大的层（语言特定层）扩展为 MoE 层，在 18~128 种语言上 PPL 比持续预训练降低 11.4%，用 3.6 倍少的参数超越 X-ELM 9.6%。

**[GuessArena: Guess Who I Am? A Self-Adaptive Framework for Evaluating LLMs in Domain-Specific Knowledge and Reasoning](guessarena_guess_who_i_am_a.md)**

:   提出 GuessArena，一种基于"猜猜我是谁"博弈游戏的自适应 LLM 评估框架，通过领域知识建模和多轮交互推理，在五个垂直行业中有效区分模型的领域知识和推理能力。

**[Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](hallucination_detox_send.md)**

:   本文揭示了 LLM 训练过程中幻觉行为的振荡现象，提出 Sensitivity Dropout（SenD）训练协议——通过识别并确定性丢弃高变异敏感嵌入索引来降低训练中的幻觉方差，同时提出计算高效的 Efficient EigenScore（EES）近似方法，在 Pythia 和 Llama 模型上实现高达 17% 的测试时可靠性提升。

**[HALoGEN: Fantastic LLM Hallucinations and Where to Find Them](halogen_hallucinations.md)**

:   提出 HALoGEN——覆盖 9 个领域（含编程、科学引用、摘要等）的 10,923 条 prompt 的大规模幻觉评测框架，配套原子级自动验证器，在 14 个 LLM 的约 150,000 条生成上系统性评估幻觉，发现即使最佳模型也可能有高达 86% 的原子事实存在幻觉，并提出 Type A/B/C 三类错误分类法。

**[Health-LLM: Personalized Retrieval-Augmented Disease Prediction System](health-llm_personalized_retrieval-augmented_disease_prediction_system.md)**

:   提出 Health-LLM 个性化 RAG 疾病预测系统，结合可穿戴设备数据和医学知识库进行健康风险评估。

**[HELIOS: Harmonizing Early Fusion, Late Fusion, and LLM Reasoning for Multi-Granular Table-Text Retrieval](helios_harmonizing_early_fusion_late_fusion_and_llm_reasoning_for_multi-granular.md)**

:   提出 HELIOS 框架，结合早期融合（边级别二部子图检索）、晚期融合（查询相关节点扩展）和 LLM 推理（星图级逻辑推断），在 OTT-QA 上 recall 和 nDCG 分别提升达 42.6% 和 39.9%。

**[HellaSwag-Pro: A Large-Scale Bilingual Benchmark for Evaluating the Robustness of LLMs](hellaswag-pro_a_large-scale_bilingual_benchmark_for_evaluating_the_robustness_of.md)**

:   构建首个大规模双语（中英）LLM 常识推理鲁棒性评估基准 HellaSwag-Pro，包含 7 种问题变体共 11,200 道题，系统评估 41 个 LLM 发现所有模型在常识推理上远未达到鲁棒。

**[Help Me Write a Story: Evaluating LLMs' Ability to Generate Writing Feedback](help_write_story_feedback.md)**

:   探索 LLM 能否为创意写作者提供有意义的写作反馈——构建包含 1300 个故意引入写作问题的故事测试集，评估常用 LLM 的写作反馈生成能力，发现模型虽能提供具体且多数准确的反馈，但常错过最重要的写作问题且不会恰当地在批评和鼓励之间切换。

**[How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training](how_do_llms_acquire_new_knowledge_a_knowledge_circuits_perspective_on_continual_.md)**

:   从知识电路（knowledge circuits）角度研究 LLM 在持续预训练中如何获取新知识：新知识的获取依赖于与已有知识的关联性，电路经历"形成→优化"的阶段转变，且呈现从深层到浅层的演化模式。

**[How does Misinformation Affect Large Language Model Behaviors and Preferences?](how_does_misinformation_affect_large_language.md)**

:   构建了目前最大的误信息评估基准 MisBench（1034 万条误信息），从知识冲突类型和文本风格两个维度系统分析 LLM 对误信息的行为和偏好，并提出 RtD 方法结合外部知识源提升误信息检测能力。

**[How Numerical Precision Affects Arithmetical Reasoning Capabilities of LLMs](how_numerical_precision_affects_arithmetical_reasoning_capabilities_of_llms.md)**

:   从电路复杂度理论出发，严格证明低精度（如 int4/int8）Transformer 在迭代加法和整数乘法上需要超多项式规模才能求解，而标准精度（float32）Transformer 仅需常数深度+多项式宽度即可高效求解三类算术任务，并在 LLaMA-3.1-8B 上实验验证了精度对算术能力的关键影响。

**[HPSS: Heuristic Prompting Strategy Search for LLM Evaluators](hpss_heuristic_prompting_strategy_search_for_llm_evaluators.md)**

:   整合 8 个影响 LLM 评估提示效果的关键因子（评分尺度、ICL 示例、评估标准、参考答案、CoT、AutoCoT、度量指标、组件顺序），提出基于遗传算法的启发式提示策略搜索方法 HPSS，在 12,960 种组合空间中高效找到最优提示策略，仅用基线 5% 的生成成本即超越 G-Eval 和 CloserLook。

**[How to Enable Effective Cooperation Between Humans and NLP Models: A Survey of Principles, Formalizations, and Beyond](human_nlp_cooperation_survey.md)**

:   首次系统性地综述了人与NLP模型之间的合作范式，提出基于"谁为最终决策负责"的三类合作形式化分类体系（顺序合作、分诊合作、联合合作），并借鉴Grice合作原则定义了人机合作的基本原则，为后续研究提供了统一视角。

**[HumT DumT: Measuring and Controlling Human-like Language in LLMs](humt_dumt_measuring_and_controlling_human-like_language_in_llms.md)**

:   提出基于 GPT-2 对数概率比的文本人类化语气度量 HumT 及其社会感知泛化版 SocioT，在 40 万+偏好样本上发现用户普遍偏好更低人类化的 LLM 输出且人类化语气与社交亲近（r=0.87）、低地位（r=-0.80）、女性化（r=0.47）强相关，进而通过仅 500 对偏好数据的 DPO 微调（DumT）有效降低人类化程度而不损模型性能。

**[HyGenar: An LLM-Driven Hybrid Genetic Algorithm for Few-Shot Grammar Generation](hygenar_an_llm-driven_hybrid_genetic_algorithm_for_few-shot_grammar_generation.md)**

:   构建 540 个挑战的文法生成数据集，设计 6 种评测指标，提出基于 LLM 驱动的混合遗传算法 HyGenar，显著提升 LLM 从少量示例生成 BNF 文法的能力。

**[Hypothetical Documents or Knowledge Leakage? Rethinking LLM-based Query Expansion](hypothetical_documents_or_knowledge_leakage_rethinking_llm-based_query_expansion.md)**

:   质疑 LLM-based 查询扩展（HyDE/Query2doc）的性能提升是否来自"假设性文档生成"，发现性能增益仅在 LLM 生成的文档包含与 gold evidence 语义一致的句子时才一致出现，揭示了 benchmark 中可能存在的知识泄露问题。

**[Enhancing the Rule Learning Ability of Large Language Model Agent through Induction, Deduction, and Abduction](idea_enhancing_the_rule_learning_ability_of_large_language_model_agent_through_i.md)**

:   提出 RULEARN benchmark（300 个手工交互式文字环境谜题，涵盖三类场景）和 IDEA 框架（溯因假设生成→演绎计划验证→归纳反馈修正的迭代循环），在 GPT-4o 上达到 50.33% 成功率（+7% vs ReAct baseline），但仍远低于人类 63.33%，细粒度人类评估揭示了 LLM 在假设修正阶段的根本瓶颈。

**[If Eleanor Rigby Had Met ChatGPT: A Study on Loneliness in a Post-LLM World](if_eleanor_rigby_had_met_chatgpt_a_study_on_loneliness_in_a_post-llm_world.md)**

:   研究 LLM 聊天伴侣对孤独感的影响，发现 ChatGPT 交互可短期缓解孤独但长期效果有限，且可能减少人际互动动力。

**[The Impossibility of Fair LLMs](impossibility_fair_llms.md)**

:   系统分析了多种技术公平性框架（fairness through unawareness、group fairness、fair representations、multi-sided fairness等）在通用LLM上的适用性，论证了每种框架要么在逻辑上无法扩展到通用AI场景、要么在实践中不可行——主要源于非结构化训练数据的敏感属性不可剥离、用例/人群组合的组合爆炸、以及公平性不具备可组合性。

**[Improve Language Model and Brain Alignment via Associative Memory](improve_language_model_and_brain_alignment_via_associative_memory.md)**

:   通过模拟人类联想记忆（用相关概念扩展输入文本）提升语言模型与大脑 fMRI 活动的对齐度，发现联想记忆增强在内侧颞叶等记忆相关脑区效果最显著，并构建 Association 数据集通过 SFT 让 LLM 学会生成联想内容。

**[Can Indirect Prompt Injection Attacks Be Detected and Removed?](indirect_prompt_injection_detection.md)**

:   本文系统研究间接 prompt injection 攻击的检测与移除：构建评估基准，发现现有检测模型对间接攻击表现不佳但专门训练的模型可达 99% 准确率，提出分割移除和抽取移除两种方法，并将检测+移除组合为过滤管道，有效降低间接 prompt injection 的攻击成功率。

**[InfiniSST: Simultaneous Translation of Unbounded Speech with Large Language Models](infinisst_simultaneous_translation_of_unbounded_speech_with_large_language_model.md)**

:   提出 InfiniSST，将流式同声翻译建模为多轮对话任务，结合流式语音编码器和 KV cache 管理策略实现无限长语音输入的实时翻译，在 MuST-C 上减少 0.5-1s 计算感知延迟且不损失翻译质量。

**[Leveraging Self-Attention for Input-Dependent Soft Prompting in LLMs](input_dependent_soft_prompting.md)**

:   提出 ID-SPAM，通过在输入 token 嵌入上施加可学习自注意力层并经瓶颈 MLP 生成**输入依赖**的软提示，仅在单层 Transformer 输入端拼接即可超越多种 Soft Prompt 基线，且具备优秀的零样本跨任务/跨领域迁移能力。

**[Beyond Facts: Evaluating Intent Hallucination in Large Language Models](intent_hallucination_eval.md)**

:   本文提出"意图幻觉"（Intent Hallucination）概念——LLM 在处理复杂多条件查询时遗漏或误解部分意图约束导致的偏离用户意图的生成，构建 FaithQA 基准（20,068 题）和 Constraint Score 评估指标，实验表明意图幻觉在 SOTA 模型中普遍存在且随查询复杂度增加而加剧。

**[Internal and External Impacts of Natural Language Processing Papers](internal_and_external_impacts_of_natural_language_processing_papers.md)**

:   从内部（NLP 社区）和外部（其他领域）两个维度衡量 NLP 论文影响力，构建影响力预测模型。

**[Investigating Context-Faithfulness in Large Language Models: The Roles of Memory Strength and Evidence Style](investigating_context-faithfulness_in_large_language_models_the_roles_of_memory_.md)**

:   通过测量 LLM 对同一问题不同释义的回答一致性来量化"记忆强度"，发现 LLM 对外部证据的接受度与记忆强度高度负相关，且改写式证据比重复或详细证据更有效。

**[IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory](irt_router_multi_llm.md)**

:   IRT-Router 借鉴心理测量学的项目反应理论（IRT），将 LLM 视为"考生"、query 视为"考题"，学习多维能力向量和难度/区分度参数实现可解释的多 LLM 路由，在 OOD 场景下达 87%+ 准确率且成本仅为 GPT-4o 的 1/30。

**[Is It Just Semantics? A Case Study of Discourse Particle Understanding in LLMs](is_it_just_semantics_a_case_study_of_discourse_particle_understanding_in_llms.md)**

:   以德语语气词为案例研究 LLM 的语用理解能力，发现模型对语义细微差异（如 'doch''halt''ja'）的掌握远不如语法和词汇。

**[Is LLM an Overconfident Judge? Unveiling the Capabilities of LLMs in Detecting Offensive Language with Annotation Disagreement](is_llm_an_overconfident_judge_unveiling_the_capabilities_of_llms_in_detecting_of.md)**

:   系统评估了多个 LLM 在攻击性语言检测中面对标注分歧时的表现，发现 LLM 在标注者高度一致的样本上表现优异（GPT-4o F1 85.24%）但在低一致度样本上骤降至 57.06%，且模型对不确定样本表现出严重的过度自信；进一步通过 few-shot 和指令微调实验证明，在训练中引入分歧样本可同时提升检测准确率和人-AI 对齐度。

**[JoPA: Explaining Large Language Model's Generation via Joint Prompt Attribution](jopa_explaining_large_language_models_generation_via_joint_prompt_attribution.md)**

:   提出 JoPA（Joint Prompt Attribution）框架，将 LLM 生成任务的 prompt 归因建模为组合优化问题，用概率搜索算法高效寻找对输出有因果影响的输入 token 组合，解决了现有方法忽略 token 间协同效应的问题。

**[Just a Scratch: Enhancing LLM Capabilities for Self-Harm Detection through Intent Refinement](just_a_scratch_enhancing_llm_capabilities_for_self-harm_detection_through_intent.md)**

:   通过意图精炼增强 LLM 自伤检测能力，将帖子按意图分类（求助/记录/警示等）再进行风险评估，准确率显著提升。

**[Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](just_go_parallel_improving_the_multilingual_capabilities_of_large_language_model.md)**

:   系统研究在 decoder-only LLM 训练中加入平行数据对多语言能力的影响，发现将平行数据放在训练末期效果最好，且平行数据显著优于等量的单语数据；LLM 无法自动泛化到训练方向的反向翻译。

**[JuStRank: Benchmarking LLM Judges for System Ranking](justrank_llm_judge_system_ranking.md)**

:   首次大规模研究LLM判官在系统排名任务中的表现，提出JuStRank基准，揭示实例级判断能力与系统级排名能力之间的差距，并发现判官的"果断性"和"偏见"两个新兴特征。

**[Knockout: LLM Assessment Using Large Language Models for Evaluations through Iterative Elimination](knockout_llm_assessment_using_large_language_models_for_evaluations_through_iter.md)**

:   提出 Knockout 淘汰赛式 LLM 评估方法，通过迭代配对比较逐步淘汰弱模型，比全配对比较效率高 O(n log n) vs O(n^2)。

**[Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations](knowledge_boundary_crosslingual.md)**

:   通过探测 LLM 内部表示，揭示知识边界认知在多语言间呈线性结构，提出 training-free 对齐方法实现跨语言知识边界感知迁移，并发现"弱到强泛化"现象。

**[Knowledge Boundary of Large Language Models: A Survey](knowledge_boundary_survey.md)**

:   本文提出了 LLM 知识边界的形式化定义框架，将知识分为四种类型（PAK/PSK/MSU/MAU），并围绕"为什么研究知识边界""如何识别知识边界""如何缓解知识边界问题"三个核心问题系统综述了相关研究。

**[La Leaderboard: A Large Language Model Leaderboard for Spanish Varieties and Languages of Spain and Latin America](la_leaderboard_spanish.md)**

:   构建首个面向西班牙和拉丁美洲语言的开源LLM排行榜，整合66个数据集覆盖西班牙语、加泰罗尼亚语、巴斯克语、加利西亚语，评估50个模型并分析训练策略、算力与性能的关系。

**[LangSAMP: Language-Script Aware Multilingual Pretraining](langsamp_multilingual_pretraining.md)**

:   提出 LangSAMP 方法，在多语言预训练中将语言和文字系统 (script) embedding 添加到 Transformer 输出端（而非输入端），使模型主干学到更语言中立的表示，在 500+ 语言的零样本跨语言迁移中一致优于基线。

**[Language-Codec: Bridging Discrete Codec Representations and Speech Language Models](language_codec_bridging_discrete_codec_speech_language_models.md)**

:   提出 Language-Codec，通过掩码通道残差向量量化（MCRVQ）机制和改进的傅里叶变换解码器，弥合离散编解码器表示与下游语音语言模型之间的鸿沟，仅用4个码本通道即实现高质量音频重建。

**[Language Complexity Measurement as a Noisy Zero-Shot Proxy for Evaluating LLM Performance](language_complexity_measurement_as_a_noisy_zero-shot_proxy_for_evaluating_llm_pe.md)**

:   探索语言复杂度指标作为 LLM 性能的零样本代理评估，发现文本复杂度与 LLM 表现负相关但噪声大，仅可作为粗略参考。

**[Language Models Can Subtly Deceive Without Lying: A Case Study on Strategic Phrasing](language_models_can_subtly_deceive_without_lying_a_case_study_on_strategic_phras.md)**

:   构建了一个立法环境测试平台（LobbyLens），研究 LLM 是否能通过策略性措辞（strategic phrasing）——即不说谎但有意操纵表达方式——来隐藏修正案中对特定公司的利益导向，发现 LLM 经过 re-planning 可使欺骗率提升最多 40 个百分点。

**[Large Language Models for Predictive Analysis: How Far Are They?](large_language_models_for_predictive_analysis_how_far_are_they.md)**

:   提出 PredictiQ 基准（1130 查询×44 真实数据集×8 领域），从文本分析、代码生成和文本-代码对齐三个维度评估 12 个 LLM 的预测分析能力，发现现有 LLM 在此领域仍面临巨大挑战。

**[Large Language Models in Bioinformatics: A Survey](large_language_models_in_bioinformatics_a_survey.md)**

:   系统综述 LLM 在生物信息学中的应用，覆盖基因组序列建模、RNA 结构预测、蛋白质功能推断、单细胞转录组学四大方向，讨论数据稀缺、计算复杂度、跨组学整合等挑战。

**[Large Vocabulary Size Improves Large Language Models](large_vocabulary_size_improves_large_language_models.md)**

:   实证研究词表大小与 LLM 性能的关系，在英语和日语上证明更大的词表（从 5K 到 500K）一致带来更好的下游性能，并提出在继续训练场景中替换词表的方法。

**[LazyReview: A Dataset for Uncovering Lazy Thinking in NLP Peer Reviews](lazyreview_peer_review.md)**

:   构建首个标注"懒惰思维"细粒度类别的同行评审数据集 LazyReview——发现 LLM 在零样本下难以检测评审中的懒惰思维启发式，但在 LazyReview 上指令微调后性能提升 10-20 个点，且经懒惰思维反馈修改的评审显著更全面和可操作。

**[Less, but Better: Efficient Multilingual Expansion for LLMs via Layer-wise Mixture-of-Experts](less_but_better_efficient_multilingual_expansion.md)**

:   分析 LLM 不同层间的跨语言表征相似度，提出 LayerMoE 按层分配不同数量的新语言专家（高相似层少分配、低相似层多分配），用 60% 更少的专家参数超越 SOTA，并通过在高相似层添加路由分类器进一步缓解灾难性遗忘。

**[Leveraging Large Language Models to Measure Gender Representation Bias in Gendered Language Corpora](leveraging_large_language_models_to_measure_gender_representation_bias_in_gender.md)**

:   提出基于 LLM 的方法量化有语法性别语言（西班牙语、巴伦西亚语）语料中的性别表示偏差，发现 4:1 到 6:1 的男性主导失衡，并证明少量反向偏差数据（5000句）可有效缓解模型输出中的性别不平衡。

**[On the Limit of Language Models as Planning Formalizers](limit_llm_planning_formalizer.md)**

:   系统评估"LLM-as-Formalizer"方法论的极限——首次要求 LLM 生成完整 PDDL 表示（而非部分），从不同自然度的文本描述中形式化规划领域，发现最强模型（GPT-4o/o3-mini/DeepSeek-R1）可有效形式化超越直接规划，但描述越自然性能越低，弱模型卡在语法错误而强模型面临语义错误。

**[Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs](llama_see_llama_do_entrainment.md)**

:   本文发现并定义了"上下文夹带"(contextual entrainment)现象——LLM会对上下文中出现过的任意token赋予更高概率，并通过可微掩码方法定位了负责该现象的entrainment heads，关闭这些头后可显著抑制干扰效应。

**[LlamaDuo: LLMOps Pipeline for Seamless Migration from Service LLMs to Small-Scale Local LLMs](llamaduo_llmops_pipeline_for_seamless_migration_from_service_llms_to_small-scale.md)**

:   提出 LlamaDuo 自动化 LLMOps 流水线，通过服务 LLM 生成合成数据迭代微调小模型，使 2B-8B 本地模型在特定下游任务上逼近甚至匹敌 GPT-4o 等大模型性能，且长期部署成本显著降低。

**[LLM as Effective Streaming Processor: Bridging Streaming-Batch Mismatches with Group Position Encoding](llm_as_effective_streaming_processor_bridging_streaming-batch_mismatches_with_gr.md)**

:   系统性地识别并量化了 batch-trained LLM 适配流式场景的三种不匹配（输入注意力 / 输出注意力 / 位置 ID），发现仅输入注意力不匹配才是关键瓶颈（+2.20 BLEU），据此提出组位置编码（Group Position Encoding）——源/目标各自维护连续位置 ID 即可，无需昂贵的 KV cache 重编码，在机器翻译和 ASR 两种跨模态任务上均超越专用流式架构。

**[LLM Braces: Straightening Out LLM Predictions with Relevant Sub-Updates](llm_braces_straightening.md)**

:   LLMBraces 通过计算 FFN 层中各 value 向量与输入的相关性得分，动态调节子更新（sub-update）的贡献权重，用极少参数（比 LoRA 少 75%）同时提升模型预测精度和实现可控文本生成。

**[LLM as a Broken Telephone: Iterative Generation Distorts Information](llm_broken_telephone.md)**

:   类比"传话游戏"研究 LLM 在迭代生成中的信息失真现象，通过多语言翻译链实验发现：信息失真随迭代累积，受中间语言选择和链复杂度影响，可通过温度控制和受限提示缓解但无法消除。

**[LLM Meets Scene Graph: Can Large Language Models Understand and Generate Scene Graphs?](llm_meets_scene_graph_can_large_language_models_understand_and_generate_scene_gr.md)**

:   构建 TSG Bench（120 场景、2041 描述、4289 文本场景图），系统评估 11 个 LLM 在场景图理解（SGDS/SGQA）和生成（SA-SGG/MA-SGG）四类任务上的能力，发现最强模型在理解上接近人类但生成任务仍有 15-17% 的差距。

**[Evaluation of LLM Vulnerabilities to Being Misused for Personalized Disinformation Generation](llm_personalized_disinformation.md)**

:   系统评估了 6 个主流 LLM 生成个性化虚假信息的能力，发现大多数 LLM 能生成高质量个性化虚假新闻，且个性化请求反而降低了安全过滤器的触发率（相当于一种 jailbreak），同时轻微降低了机器生成文本的可检测性。

**[Re-ranking Using Large Language Models for Mitigating Exposure to Harmful Content on Social Media Platforms](llm_reranking_harmful_content.md)**

:   提出基于 LLM 的成对偏好重排序方法，在零样本和少样本设置下对社交媒体推荐序列中的有害内容进行降级排序，显著优于 Perspective API 和 OpenAI Moderation API 等工业级分类器，同时引入 PP-k 和 EWN 两个新评估指标。

**[Wait, that's not an option: LLMs Robustness with Incorrect Multiple-Choice Options](llm_robustness_incorrect_mcq.md)**

:   提出"反思判断力"（Reflective Judgment）概念来衡量 LLM 在所有选项都错误的选择题中拒绝选择的能力，发现对齐后的模型（GPT-4o 等）往往盲目服从指令选择错误选项，而基座模型反而表现更好，且该能力随模型规模增大而涌现。

**[LLM-Powered Test Case Generation for Detecting Bugs in Plausible Programs](llm_test_case_gen_bugs.md)**

:   提出TrickCatcher——一种LLM驱动的测试用例生成方法，通过PUT引导的程序变体生成、基于生成器的输入生成和多样性驱动的差异测试三阶段流程，专门检测"plausible programs"（能通过现有测试套件但仍含隐蔽bug的程序）中的tricky bugs，F1分数达到SOTA基线的1.66倍。

**[LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks](llm_vs_human_judges_study.md)**

:   构建包含20个NLP数据集（7万+实例）的 Judge-Bench 基准，系统评估11个LLM作为评判者与人类标注的一致性，发现模型在不同任务/属性/标注者专业水平上表现差异巨大，建议部署前必须针对特定任务做人类标注验证。

**[LLMs can Perform Multi-Dimensional Analytic Writing Assessments](llm_writing_assessment.md)**

:   利用 L2 研究生文献综述语料库，系统评估了 LLM 在多维分析写作评估（评分+评论）上的能力，并提出可解释的反馈质量评估框架 ProEval。

**[LLMs Know Their Vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](llms_know_their_vulnerabilities_uncover_safety_gaps_through_natural_distribution.md)**

:   提出 ActorBreaker 多轮攻击方法，基于 Latour 的行动者网络理论，利用与有害内容语义相关的良性 prompt（自然分布偏移）绕过安全机制，在 HarmBench 上达到 SOTA 攻击成功率，揭示了预训练数据与安全训练数据之间的语义覆盖差距。

**[Language Models, Graph Searching, and Supervision Adulteration: When More Supervision is Less and How to Make More More](lm_graph_search_supervision.md)**

:   本文证明了 path-star 图搜索任务在 decoder-only LM 上的失败并非 next-token prediction 范式的根本缺陷，而是由"监督污染"（supervision adulteration）导致的——过量的 teacher-forcing 监督信号诱导模型学到 Clever Hans Cheat 捷径，阻碍了子任务分解；通过 token masking、ranking-into-the-future、scratchpad、树形拓扑等六种正交方法均可使任务可学。

**[Locate-and-Focus: Enhancing Terminology Translation in Speech Language Models](locateandfocus_enhancing_terminology_translation_in_speech.md)**

:   提出Locate-and-Focus方法用于语音LLM的术语翻译：先用滑动窗口检索定位语音中包含术语的片段，再通过音频替换和Tag Cue引导模型聚焦翻译知识，在英中/英德方向上术语翻译成功率大幅提升。

**[LongDPO: Unlock Better Long-form Generation Abilities for LLMs via Critique-augmented Stepwise Information](longdpo_unlock_better_long-form_generation_abilities_for_llms_via_critique-augme.md)**

:   提出 LongDPO，通过 MCTS 收集步级偏好对、全局记忆池维护事实一致性、critique 增强低质量候选，再用步级 DPO 进行细粒度优化，在 LongBench-Write 上显著提升长文本生成质量，同时保持通用能力。

**[Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models](lost_in_multilinguality_dissecting_cross-lingual_factual_inconsistency_in_transf.md)**

:   用机制可解释性方法解剖多语言 LLM 的跨语言事实不一致问题，发现模型在大多数层中以语言无关的概念空间处理知识，但在最后几层的"语言转换"过程中失败导致不一致，提出线性快捷方法绕过最后层以提升一致性和准确率。

**[Making LLMs Better Many-to-Many Speech-to-Text Translators with Curriculum Learning](making_llms_better_many-to-many_speech-to-text_translators_with_curriculum_learn.md)**

:   提出 LLM-SRT，将语音到文本翻译（S2TT）任务转化为语音识别与翻译联合任务（SRT），并通过三阶段课程学习策略（ASR→SMT→SRT）有效利用 LLM 的机器翻译能力，在低资源场景（每种语言不到 10 小时数据）下实现 15×14 语言对的 SOTA 多对多语音翻译性能。

**[Mapping 1,000+ Language Models via the Log-Likelihood Vector](mapping_1000_models_loglikelihood.md)**

:   提出用对数似然向量（log-likelihood vector）将 1000+ 语言模型映射到一个统一空间，证明向量间欧氏距离近似 KL 散度，可实现模型聚类可视化、基准性能预测（r=0.96）和数据泄漏检测。

**[MAPS: Motivation-Aware Personalized Search via LLM-Driven Consultation Alignment](maps_personalized_search.md)**

:   首次建模电商搜索中的"搜索动机"——用户在搜索前的咨询行为蕴含的真实需求，提出MAPS框架融合LLM语义、MoAE池化和双重对齐机制，在真实商业数据上HR@10提升24.4%（从0.5685到0.7071）。

**[Marco-Bench-MIF: On Multilingual Instruction-Following Capability of Large Language Models](marco_bench_multilingual_if.md)**

:   将英文IFEval基准扩展到30种语言并进行文化本地化，揭示LLM在多语言指令遵循中高/低资源语言间25-35%的准确率差距，以及机器翻译数据低估模型性能7-22%。

**[MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset](mars_benchmarking_the_metaphysical_reasoning_abilities_of_language_models_with_a.md)**

:   本文提出了 **Metaphysical Reasoning（形而上推理）** 的形式化定义，将分布变化下的推理分解为三步判别过程，并构建了首个大规模评估基准 Mars（355K 标注数据），实验表明 20+ 语言模型在该任务上表现均不理想，揭示了 LLM 在理解事件组成要素变化及其因果效应方面的显著短板。

**[Masking in Multi-hop QA: How LMs Perform with Context Permutation](masking_in_multi-hop_qa_an_analysis_of_how_language_models_perform_with_context_.md)**

:   系统分析因果掩码对 LLM 多跳 QA 的影响，发现 encoder-decoder（Flan-T5 770M）零样本多跳性能优于 decoder-only（Qwen 7B），且 prefix mask 可提升 decoder-only 的多跳推理能力 5.1%。

**[MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion](mathfusion_instruction_fusion.md)**

:   MathFusion 提出了跨问题指令融合的数学数据增强框架，通过顺序融合、并行融合和条件融合三种策略将两个数学问题合成新问题，仅用 45K 额外合成指令就在 6 个 benchmark 上平均提升 18 分准确率。

**[Math Neurosurgery: Isolating Language Models' Math Reasoning Abilities Using Only Forward Passes](mathneuro_math_reasoning_isolation.md)**

:   MathNeuro 提出了一种仅用前向传播就能隔离 LLM 中数学推理特定参数的方法，通过计算权重×激活的重要性分数并过滤掉通用语言任务也需要的参数，实现了精准的数学能力"手术"——剪除这些参数删除数学能力，缩放它们则提升 4-35% 数学性能。

**[McBE: A Multi-task Chinese Bias Evaluation Benchmark for Large Language Models](mcbe_a_multi-task_chinese_bias_evaluation_benchmark_for_large_language_models.md)**

:   提出首个多任务中文偏见评估基准 McBE，包含 4,077 条偏见评估实例（BEI），覆盖 12 种偏见类别和 82 个子类别，通过 5 种评估任务（偏好计算/子类别分类/场景选择/偏见分析/偏见评分）多角度量化 LLM 中的中文偏见，并揭示"参数越大偏见越强"的传统结论可能源于单任务评估的局限性。

**[Mechanistic Interpretability of Emotion Inference in Large Language Models](mechanistic_interpretability_of_emotion_inference_in_large_language_models.md)**

:   通过 probing、activation patching 和 generation steering 三种机制可解释性技术，发现 LLM 的情感表征功能性地定位于中间层的 MHSA 单元，并基于认知评估理论（appraisal theory）证明这些表征具有心理学合理性，成功通过干预评估概念（如 self-agency、pleasantness）引导情感输出。

**[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](membench_towards_more_comprehensive_evaluation_on_the_memory_of_llm-based_agents.md)**

:   提出 MemBench，从多场景（参与/观察）、多层级（事实记忆/反思记忆）和多指标（准确率/召回率/容量/效率）三个维度全面评估 LLM Agent 的记忆能力，弥补了现有评估在记忆层级和交互场景上的不足。

**[MEraser: An Effective Fingerprint Erasure Approach for Large Language Models](meraser_fingerprint_erasure.md)**

:   提出 MEraser（Mismatched Eraser），通过两阶段微调策略（错配数据擦除 + 干净数据恢复）以不到 1000 条样本完全移除 LLM 中基于后门的指纹水印，同时保持模型性能，并首创可迁移的 LoRA 擦除适配器。

**[MergePrint: Merge-Resistant Fingerprints for Robust Black-box Ownership Verification of Large Language Models](mergeprint_fingerprint_ownership.md)**

:   提出 MergePrint，首个针对模型合并（model merging）场景的 LLM 黑盒指纹验证方法，通过伪合并模型模拟合并行为并两阶段优化（输入优化 + 参数优化），使嵌入的指纹在合并后仍可被检测，实现高效、无害、抗篡改的所有权验证。

**[Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models](metarater_a_multidimensional_data_selection_method.md)**

:   提出Meta-rater多维数据选择框架，定义PRRC四个质量维度（专业性/可读性/推理性/清洁度），通过proxy模型回归学习多个质量分数的最优加权组合，使1.3B模型训练收敛速度翻倍、下游任务提升3.23%。

**[Multi-Level Explanations for Generative Language Models](mexgen_multi_level_explanations.md)**

:   提出 MExGen（Multi-Level Explanations for Generative Language Models），将 LIME/SHAP 等扰动式归因方法扩展到 LLM 的上下文生成任务上——为摘要/问答等任务中 LLM 输出的每个部分量化上下文各段落的影响程度，比 LLM 自解释更忠实。

**[MHA2MLA: Towards Economical Inference by Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-based LLMs](mha2mla_deepseek_latent_attention.md)**

:   MHA2MLA 首次提出将已训练好的 MHA 模型高效迁移到 DeepSeek 的 MLA 架构的方法，通过贡献度感知的 partial-RoPE 移除和联合 SVD 低秩近似，仅用 0.6%-1% 的训练数据即可恢复性能，将 Llama2-7B 的 KV cache 压缩 92.19% 且 LongBench 性能仅下降 1%。

**[Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](mid_layer_crosslingual_alignment.md)**

:   通过分析 1000+ 语言对发现 LLM 中间层具有最强的跨语言对齐潜力，提出在任务训练中集成中间层对齐目标（对比损失），在槽填充（F1 61.7%）、机器翻译（BLEU 32.3）和结构化文本生成上显著提升跨语言迁移，对未见语言也有效。

**[MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages](milic-eval_benchmarking_multilingual_llms_for_chinas_minority_languages.md)**

:   构建首个中国少数民族语言 LLM 评估基准 MiLiC-Eval，包含 24K 实例覆盖 9 个任务、聚焦藏语/维吴尔语/哈萨克语/蒙古语 4 种语言，发现开源 LLM 在语法密集型任务和多文字语言上表现极差。

**[Mind the Belief Gap: Group Identity in the World of LLMs](mind_the_belief_gap_group_identity_in_the_world_of_llms.md)**

:   构建多智能体信念一致性模拟框架，发现 LLM 比人类表现出更强的信念一致性偏见（gpt-3.5: 0.93 vs 人类: 0.2-0.62），导致虚假信息传播加剧、跨群体学习受阻，并探索接触假说等缓解策略（最优可改善 37%）。

**[Mitigate Position Bias in LLMs via Scaling a Single Hidden States Channel](mitigate_position_bias_in_large_language_models_via_scaling_a_single_dimension.md)**

:   发现 LLM 隐状态中存在编码绝对位置信息的特定通道（positional hidden states），通过缩放这单一通道即可缓解"lost in the middle"位置偏差，在多文档 QA 基准上提升高达 15.2%，且不影响模型其他能力。

**[Model Performance-Guided Evaluation Data Selection for Effective Prompt Optimization](model_performance-guided_evaluation_data_selection_for_effective_prompt_optimiza.md)**

:   提出 IPOMP——一种两阶段评估数据选择方法，第一阶段通过语义聚类和边界分析选取多样化样本，第二阶段利用提示优化过程中的实时模型性能迭代替换冗余样本，在 BIG-bench 和 LIAR 上将提示优化效果提升 1.6%-3.1%，稳定性提升 50%+，额外开销不到 1%。

**[Comparing Moral Values in Western English-speaking Societies and LLMs with Word Associations](moral_values_western.md)**

:   提出通过词语联想（word association）而非直接提问来比较 LLM 与西方英语社会的道德价值观，发现 LLM 在正面道德维度上与人类更一致，但在情感多样性和具体性上存在系统性差异。

**[Delving into Multilingual Ethical Bias: The MSQAD with Statistical Hypothesis Tests for Large Language Models](msqad_multilingual_ethical_bias.md)**

:   提出多语言敏感问答数据集MSQAD（基于Human Rights Watch 17个人权话题），通过McNemar检验和PERMANOVA检验两种统计假设检验方法，系统验证了LLM在不同语言下对相同敏感问题的回答存在显著伦理偏差——中文和印地语拒绝率最高，西班牙语和德语最容易生成不当回答，且该偏差在7个不同LLM中普遍存在。

**[Multi-Prompting Decoder Helps Better Language Understanding](multi-prompting_decoder_helps_better_language_understanding.md)**

:   提出 Multi-Prompting Decoder（MPD）框架，通过多提示查询 PLM 获取多组隐状态和类别分数，结合最优传输匹配和校准解码策略，在 MaaS（模型即服务）场景下的 few-shot 分类任务上显著超越现有方法。

**[Multi-Attribute Steering of Language Models via Targeted Intervention](multi_attribute_steering.md)**

:   提出 MAT-Steer，通过属性感知的 token 级 gating 机制和正交性约束，实现推理时对 LLM 多属性（如真实性、毒性、偏见）的同时精准干预，在 QA 和生成任务上全面超越现有 ITI 和微调方法。

**[Multilingual Encoder Knows More Than You Realize: Shared Weights Pretraining for Extremely Low-Resource Languages](multilingual_encoder_knows_more_than_you_realize_shared_weights_pretraining_for_.md)**

:   提出 XLM-SWCM 框架，通过将多语言编码器权重复用到解码器中（CustomDecoderLayer 共享 + NormalDecoderLayer 随机初始化交替插入），以 457M 参数在极低资源语言（藏语）上超越 13B 参数的 MC2-LLaMA，藏语摘要 ROUGE-L 达 25.7 vs 16.1。

**[Do Large Language Models Have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs](multilingual_llm_english_accent.md)**

:   本文揭示多语言 LLM 在非英语语言生成中存在"英语口音"——词汇和句法上偏向英语模式，提出了基于 JSD（词汇分布）和 WL 图核+MMD（句法依赖树）的语料级自然度指标，并通过 DPO 对齐方法有效提升目标语言的自然度。

**[Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](multiple_choice_eval.md)**

:   系统性论证了 MCQA（多选题问答）作为 LLM 评测标准格式的三大缺陷——格式本身的局限性、数据集构建质量问题、以及 LLM 在 MCQA 上的特有错误——并从教育测试学中引入改进方案。

**[Natural Language Processing in Support of Evidence-based Medicine: A Scoping Review](natural_language_processing_in_support_of_evidence-based_medicine_a_scoping_revi.md)**

:   对 129 篇研究进行范围综述，系统梳理了 NLP 技术在循证医学（EBM）五步流程（Ask-Acquire-Appraise-Apply-Assess）中的应用，覆盖证据检索、PICO 提取、质量评估、证据合成、摘要生成、临床试验匹配等任务，指出了 LLM 时代的新机遇与挑战。

**[Navigating Rifts in Human-LLM Grounding: Study and Benchmark](navigating_rifts_in_human-llm_grounding_study_and_benchmark.md)**

:   系统研究人与 LLM 对话中的 grounding（建立共识）失败问题，发现 LLM 主动澄清的频率仅为人类的 1/3、主动追问的频率仅为 1/16，提出 Rifts 基准（约 1.8K 任务）评测 LLM 的 grounding 能力，并通过 grounding forecaster 实现初步干预。

**[Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset](nemotron_cc_pretraining_data.md)**

:   Nemotron-CC 通过分类器集成、合成数据改写和减少启发式过滤三种策略，从 Common Crawl 构建了 6.3T token 的长期预训练数据集，在 15T token 训练中超越 Llama 3.1 8B。

**[NewsInterview: a Dataset and a Playground to Evaluate LLMs' Grounding Gap via Informational Interviews](newsinterview_a_dataset_and_a_playground_to_evaluate_llms_grounding_gap_via_info.md)**

:   构建了 4 万条新闻采访对话数据集，发现 LLM 在采访场景中缺乏 acknowledgement（少 50%）和话题转换能力（少 30%），并设计了含说服机制的模拟博弈环境（NewsInterview），证明最优 LLM（gpt-4o）也仅能提取 50.4% 的信息项。

**[Nudging: Inference-time Alignment of LLMs via Guided Decoding](nudging_inference_time_alignment.md)**

:   提出 Nudging，一种免训练的推理时对齐算法，利用小型对齐模型在基础模型不确定时注入少量"nudging tokens"来引导输出，用 7-14 倍小的模型就能达到甚至超过大型对齐模型的性能。

**[OLMoTrace: Tracing Language Model Outputs Back to Trillions of Training Tokens](olmotrace_tracing_language_model_outputs_back_to_trillions_of_training_tokens.md)**

:   推出 OLMoTrace，首个能实时将语言模型输出追溯到万亿 token 训练数据的系统，基于扩展的 infini-gram 后缀数组索引，在 4.5 秒内完成逐字匹配追溯，支持事实核查、幻觉检测和创造力分析。

**[On Entity Identification in Language Models](on_entity_identification_in_language_models.md)**

:   提出基于聚类的评估框架（Purity/Inverse Purity）分析 LLM 内部表示中的实体区分能力，发现实体信息在早期层（~归一化位置 0.2）的 20 维子空间中达到线性可分（F1~0.9），且不同大模型收敛到结构同构的实体编码——为"LLM 从纯文本训练中涌现离散知识结构"提供了系统性证据。

**[On the Mutual Influence of Gender and Occupation in LLM Representations](on_the_mutual_influence_of_gender_and_occupation_in_llm_representations.md)**

:   通过在 LLM 嵌入空间中近似性别方向（gender direction），系统研究了名字的性别表征与职业上下文之间的双向影响：职业上下文会偏移名字的性别表征，而名字的性别表征反过来影响 LLM 在职业预测任务中的偏差行为，但二者的相关性仅为中等强度。

**[Open-Set Living Need Prediction with Large Language Models](open-set_living_need_prediction_with_large_language_models.md)**

:   提出开放集生活需求预测任务，利用 LLM 从用户描述中预测生活需求，不限于预定义类别，应用于养老服务、社区管理等场景。

**[Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport](opt-out_investigating_entity-level_unlearning_for_large_language_models_via_opti.md)**

:   提出 Opt-Out，一种基于最优传输理论的实体级 LLM 遗忘方法，利用 Sliced Wasserstein Distance 正则化参数偏移实现精细遗忘；同时构建首个实体级遗忘数据集 ELUDe（20 目标实体 + 144 邻居实体，15K+ forget / 90K+ retain QA 对），在 Llama-3.1-8B 和 Phi-3.5 上全面超越现有方法。

**[Pandora's Box or Aladdin's Lamp: A Comprehensive Analysis Revealing the Role of RAG Noise in Large Language Models](pandora_box_rag_noise.md)**

:   本文从语言学视角定义了 RAG 系统中的 7 种噪声类型，构建了 NoiserBench 综合评测框架，通过 8 个 LLM 的大规模实验发现噪声可分为有害噪声（反事实、支持性、拼写）和有益噪声（语义、数据类型、非法句子），其中有益噪声反而能提升模型准确率 1-3%。

**[Enhancing Open-Domain Task-Solving Capability of LLMs via Autonomous Tool Integration from GitHub](paper_2312_17294.md)**

:   提出 OpenAgent 系统，通过自主从 GitHub 发现和集成专业工具来解决开放域任务，并构建 OpenAct 基准评测 LLM 在需要领域特定工具的开放域问题上的能力。

**[PapersPlease: A Benchmark for Evaluating Motivational Values of Large Language Models Based on ERG Theory](papersplease_a_benchmark_for_evaluating_motivational_values_of_large_language_mo.md)**

:   基于 Alderfer ERG 需求理论构建 3700 个道德困境场景（移民检查官角色扮演），评估 6 个 LLM 的动机价值偏好，发现 Claude 拒绝所有场景、GPT-4o-mini 对生存需求 99% 满足但对关系需求仅 47%，且模型对穆斯林/边缘化群体存在显著的隐性社会偏见。

**[Parenting: Optimizing Knowledge Selection of Retrieval-Augmented Language Models with Parameter Decoupling and Tailored Tuning](parenting_optimizing_knowledge_selection_of_retrievalaugmented.md)**

:   受人脑功能分区启发，提出 Parenting 框架，通过解耦并定位 LLM 参数空间中与"上下文遵循"(adherence)和"噪声鲁棒"(robustness)相关的子空间，并为不同子空间设计定制化微调策略，实现两种能力的平衡提升。

**[PATCH: Psychometrics-Assisted Benchmarking of LLMs Against Human Populations](patch_psychometrics-assisted_benchmarking_of_large_language_models_against_human.md)**

:   提出 PATCH 框架，将心理测量学中的项目反应理论（IRT 3PL/2PL 模型）引入 LLM 基准测试，在 TIMSS 2011 八年级数学测试（88 道题、56 个国家/地区）上对比 GPT-4V、Gemini-Pro-Vision、Qwen-VL 与人类群体的能力值，发现 IRT 能力估计与简单准确率排名显著不同，GPT-4V 与韩国/新加坡/中国台北学生处于同一排名区间；同时发布 4 个高质量数据集（TIMSS 2011 & 2008 数学/科学/物理）。

**[Perspective Transition of Large Language Models for Solving Subjective Tasks](perspective_transition_of_large_language_models_for_solving_subjective_tasks.md)**

:   提出 RPT（Reasoning through Perspective Transition），通过在同一 prompt 中让 LLM 依次探索直接/角色扮演/第三人称三种视角、按置信度排序、选最优视角推理，在 12 个主观任务、4 个模型（GPT-4/GPT-3.5/Llama-3/Qwen-2）上均超越固定视角与集成基线，GPT-3.5 上平均提升 +4.56 点。

**[Pitfalls of Scale: Investigating the Inverse Task of Redefinition in Large Language Models](pitfalls_of_scale_investigating_the_inverse_task_of_redefinition_in_large_langua.md)**

:   通过重定义任务（给著名物理常数或度量单位赋予新值并要求 LLM 据此推理），揭示大模型比小模型更容易锚定于先验知识，展现规模增长带来推理灵活性下降的逆向缩放现象。

**[PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](plangenllms_planning_survey.md)**

:   PlanGenLLMs 是一篇系统性综述，基于经典 AI 规划评估框架提出完整性、可执行性、最优性、表示、泛化性和效率六大评估准则，全面梳理了 LLM 作为规划器的方法、评估和未来方向。

**[Plug-in and Fine-tuning: Bridging the Gap between Small Language Models and Large Language Models](plugin_finetuning_bridge.md)**

:   提出 PiFi 框架，将 LLM 的单个冻结层"插入"到 SLM 中再进行微调，以极低的额外计算成本将 LLM 的语言知识和泛化能力迁移到小模型，在 NLU 和 NLG 任务上均获得一致提升。

**[KoGEM: Polishing Every Facet of the GEM: Testing Linguistic Competence of LLMs and Humans in Korean](polishing_every_facet_of_the_gem.md)**

:   提出 KoGEM（韩语语法评估基准），包含 1,524 道基于理论语言学分类的多选题，覆盖音韵/形态/句法/语义/规范 5 大类 16 子类，零样本评估 27 个 LLM 并与人类对比，揭示 LLM 在需要经验知识的语言子类（如发音规则、音韵变化）上远逊人类，而显式补充经验知识（发音文本、语素分解）后可大幅提升。

**[Only a Little to the Left: A Theory-grounded Measure of Political Bias in LLMs](political_bias_theory_grounded.md)**

:   本文用政治科学中经过验证的 World Values Survey (WVS) 替代缺乏科学基础的 Political Compass Test (PCT)，设计 30 种提示变体在 11 个开源/商业 LLM 上收集 88,110 条开放式回复并训练立场分类器自动标注，发现指令微调模型普遍偏左但偏见度量对提示高度敏感，PCT 会夸大特定模型（如 GPT-3.5）的政治偏见。

**[Pragmatics in the Era of Large Language Models: A Survey on Datasets, Evaluation, Opportunities and Challenges](pragmatics_survey.md)**

:   全面梳理用于评估 NLP 系统语用能力的资源——按语用现象（隐含义、指称、言语行为、会话含义、预设等）分类数据集，分析任务设计、数据收集方法和评估方式，揭示了现代 LLM 在处理语境相关语言使用上的趋势、挑战和空白。

**[PRAISE: Enhancing Product Descriptions with LLM-Driven Structured Insights](praise_enhancing_product_descriptions_with_llm-driven_structured_insights.md)**

:   提出 PRAISE，一个 4 步 LLM pipeline（属性提取 → 跨产品对比 → 语义分组 → 结构化呈现），使用 Gemini 2.0 Flash 从 Amazon 产品描述中自动生成结构化洞察。在 90 个产品 × 9 个类别上验证，多步 pipeline 显著优于单次生成；效果与产品主观性高度相关（Arts&Crafts F1=0.82 vs Books F1=0.36），每产品仅需 $2R+1$ 次 API 调用。

**[Pre-Training Curriculum for Multi-Token Prediction in Language Models](pre-training_curriculum_for_multi-token_prediction_in_language_models.md)**

:   针对小语言模型（SLM）难以直接受益于多 token 预测（MTP）目标的问题，提出前向/反向课程学习策略——前向课程（NTP→MTP）使 SLM 在保持自推测解码加速的同时提升生成质量，反向课程（MTP→NTP）在 NTP 性能上更优但失去推理加速优势。

**[Pre³: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation](pre3_deterministic_pda_structured_gen.md)**

:   提出 Pre³，将 LR(1) 文法转化为确定性下推自动机（DPDA），通过预计算前缀条件边消除运行时非确定性探索，实现结构化 LLM 生成的显著加速——每 token 耗时降低最高 40%，吞吐提升最高 36%。

**[Probabilistic Aggregation and Targeted Embedding Optimization for Collective Moral Reasoning](probabilistic_aggregation_and_targeted_embedding_optimization_for_collective_mor.md)**

:   提出一种双阶段框架：先用截断正态分布EM算法将多个LLM的连续道德评分聚合为集体共识概率，再对偏离共识的模型进行道德理论token级嵌入优化，使其与集体意见对齐，实现多LLM间一致的道德推理。

**[Probing LLMs for Multilingual Discourse Generalization Through a Unified Label Set](probing_llms_for_multilingual_discourse_generalization_through_a_unified_label_s.md)**

:   本文提出首个跨框架、跨语言的统一篇章关系标签集（17类），并通过对23个LLM的注意力探针实验，证明多语言LLM能够在中间层编码跨语言可迁移的篇章级表征，且多语言训练和模型规模共同提升泛化能力。

**[Problem-Solving Logic Guided Curriculum ICL for LLMs Complex Reasoning](problem-solving_logic_guided_curriculum_in-context_learning_for_llms_complex_rea.md)**

:   提出问题解决逻辑引导的课程式 ICL，基于 QDMR 分析解题步骤结构来选择和排序 few-shot 示例（按步骤数从易到难），在多个复杂推理基准上超越现有 ICL 方法。

**[Psycholinguistic Word Features: A New Approach for the Evaluation of LLMs Alignment with Humans](psycholinguistic_word_features_a_new_approach_for_the_evaluation_of_llms_alignme.md)**

:   首次系统提出使用心理语言学词汇规范（Glasgow和Lancaster数据集共13种词汇特征）来评估LLM与人类的对齐程度，发现LLM在情感/概念特征上对齐较好，但在感知觉特征（味觉、嗅觉、触觉等）上对齐极差，揭示了LLM缺乏具身认知的根本局限。

**[Aligning Large Language Models with Implicit Preferences from User-Generated Content](pugc_align_implicit_pref_ugc.md)**

:   提出 PUGC 框架，利用非标注用户生成内容（UGC）中的隐式人类偏好来生成偏好数据——将 UGC 转化为查询+参考文本，以此评分模型生成的响应，用 DPO 实现可扩展的领域特定对齐，在 Alpaca Eval 2 上基于 Mistral-7B 达到 35.93% 长度控制胜率 SOTA。

**[RAEmoLLM: Retrieval Augmented LLMs for Cross-Domain Misinformation Detection Using In-Context Learning Based on Emotional Information](raemollm_retrieval_augmented_llms_for_cross-domain_misinformation_detection_usin.md)**

:   提出 RAEmoLLM，首个基于情感信息检索的 RAG 框架，利用情感 LLM 的隐式嵌入构建检索数据库，为跨域虚假信息检测提供情感相关的 few-shot 示例，在三个基准上最高分别提升 15.64%、31.18% 和 15.73%（对比其他 few-shot 方法），无需微调。

**[RARE: Retrieval-Augmented Reasoning Enhancement for Large Language Models](rare_retrieval_augmented_reasoning.md)**

:   提出 RARE，在 rStar 的 MCTS 推理框架中引入两个检索增强动作（A6: 基于原始问题生成搜索查询并检索，A7: 对子问题进行检索并重新回答），并用检索增强的事实性评分器（RAFS）替代原始判别器，使 LLaMA 3.1 在医学和常识推理任务上达到甚至超越 GPT-4o 的水平。

**[Re-TASK: Revisiting LLM Tasks from Capability, Skill, and Knowledge Perspectives](re-task_revisiting_llm_tasks_from_capability_skill_and_knowledge_perspectives.md)**

:   借鉴 Bloom 分类学和知识空间理论，提出 Re-TASK 框架将 LLM 任务从"能力项-技能-知识"三层视角进行重新审视，并设计 Re-TASK prompting 策略通过针对性的知识注入和技能适配来增强 CoT 在领域任务上的表现，在法律任务上最高提升 45%。

**[RealHiTBench: A Comprehensive Realistic Hierarchical Table Benchmark for Evaluating LLM-Based Table Analysis](realhitbench_a_comprehensive_realistic_hierarchical_table_benchmark_for_evaluati.md)**

:   提出 RealHiTBench——首个全面评估 LLM 对复杂层次化表格理解能力的基准，包含 708 张来自 13 个平台、24 个领域的真实复杂表格和 3,752 道题目，定义了 5 种复杂结构类型和 5 大任务类型，并提出基于树结构的 TreeThinker 推理管线显著提升模型对层次化表头的理解能力。

**[Reason from Future: Reverse Thought Chain Enhances LLM Reasoning](reason_from_future_reverse_thought_chain_enhances_llm_reasoning.md)**

:   提出 Reason from Future（RFF）推理范式，通过交替进行逆向推理（从目标向前分解）和正向推理（从当前状态向目标逼近）实现双向推理，在 Game of 24、GSM8K、MATH-500 等基准上显著超越 CoT、ToT、CR 等方法，同时大幅减少搜索空间。

**[Reasoning Circuits in Language Models: A Mechanistic Interpretation of Syllogistic Inference](reasoning_circuits_in_language_models_a_mechanistic_interpretation_of_syllogisti.md)**

:   用机械可解释性技术（激活补丁 + Logit Lens + 电路消融）发现语言模型中实现三段论推理的完整电路：三阶段机制——长归纳偏差→中间项抑制（h11.10）→传递项移动，该电路在符号输入上既充分又必要，可迁移到自然语言输入，且跨 GPT-2/Pythia/LLaMA/Qwen 四种架构存在兼容模式。

**[Recent Advances in Speech Language Models: A Survey](recent_advances_in_speech_language_models_a_survey.md)**

:   首篇 Speech Language Models (SpeechLMs) 综合综述，系统梳理从"ASR+LLM+TTS"级联架构到端到端语音语言模型的演进，提出按三大组件（speech tokenizer / language model / vocoder）和训练方案分类的分类体系，覆盖下游能力、评估指标、挑战与未来方向。

**[Recurrent Knowledge Identification and Fusion for Language Model Continual Learning](recurrent_kif_continual_learning.md)**

:   提出Recurrent-KIF持续学习框架，通过内外循环迭代机制动态估计参数重要性分布，利用基于重要性的二值掩码进行知识融合，有效缓解灾难性遗忘并促进知识迁移。

**[Red-Teaming Llm Multi-Agent Systems Via Communication Attacks](red-teaming_llm_multi-agent_systems_via_communication_attacks.md)**

:   提出 Agent-in-the-Middle (AiTM) 攻击，通过拦截和篡改 LLM 多智能体系统中的 agent 间通信消息（而非直接修改 agent 本身），利用一个带反思机制的对抗性 agent 生成上下文感知的恶意指令，在多种框架/通信结构/真实应用上均取得 40%~100% 的攻击成功率。

**[Redundancy, Isotropy and Intrinsic Dimensionality of Prompt-Based Text Embeddings](redundancy_isotropy_and_intrinsic_dimensionality_of_prompt-based_text_embeddings.md)**

:   系统研究了基于Prompt的文本嵌入模型（如gte-Qwen2、E5-mistral等）在后处理降维下的性能鲁棒性，发现分类/聚类任务仅保留原始维度的0.5%即可基本保持性能，并通过内在维度（ID）和各向同性（IsoScore）两个指标定量解释了不同任务Prompt产生的嵌入冗余度差异。

**[REFIND at SemEval-2025 Task 3: Retrieval-Augmented Factuality Hallucination Detection in Large Language Models](refind_at_semeval-2025_task_3_retrieval-augmented_factuality_hallucination_detec.md)**

:   提出 REFIND 框架，通过计算每个 token 在有无检索文档条件下的生成概率之比（Context Sensitivity Ratio, CSR），实现对 LLM 输出中幻觉片段的高效检测，在 SemEval-2025 Task 3 的 9 种语言上显著超越基线。

**[Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](refining_salience-aware_sparse_fine-tuning_strategies_for_language_models.md)**

:   首次系统评估了 8 种显著性度量在稀疏参数高效微调（SPEFT）中的效果，发现简单的梯度基方法配合静态掩码即可一致性地超越 LoRA，挑战了"PEFT 需要复杂设计"的常见认知。

**[Representation Bending for Large Language Model Safety](repbend_representation_bending_safety.md)**

:   提出 RepBend，将 activation steering 的核心思想（安全/不安全表示的向量差异）引入 LoRA 微调的损失函数设计，通过"弯曲"模型的表示空间使安全和不安全状态在潜在空间中远离彼此，在多种越狱攻击基准上实现高达 95% 的攻击成功率降低，且对模型通用能力影响极小。

**[Representations of Fact, Fiction and Forecast in Large Language Models: Epistemics and Attitudes](representations_of_fact_fiction_and_forecast_in_large_language_models_epistemics.md)**

:   通过受控故事任务评估 8 个开源 LLM 对认识情态（may/must、know/believe/doubt）的语义知识，发现 LLM 在生成恰当认知表达方面表现有限且不鲁棒——必然性（must）优于可能性（may），事实陈述优于信念陈述。

**[Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models](retrieval_models_arent_tool-savvy_benchmarking_tool_retrieval_for_large_language.md)**

:   提出 ToolRet——首个大规模工具检索基准（7.6k 任务 + 43k 工具语料库），系统评估了现有 IR 模型在工具检索场景下的表现，发现即使强力检索器也表现不佳，并贡献了超过 200k 训练实例显著提升检索质量。

**[Reversal of Thought: Enhancing Large Language Models with Preference-Guided Reverse Reasoning Warm-up](reversal_of_thought_enhancing_large_language.md)**

:   提出 Reversal of Thought (RoT)，一个即插即用的推理框架，通过偏好引导的逆向推理预热策略，让 LLM 从示例中反向生成"LLM 口味"的最优 prompt，再通过认知偏好管理器自动区分已知/未知任务，在多种推理任务上超越 CoT/ToT/GoT 等基线。

**[Revisiting 3D LLM Benchmarks: Are We Really Testing 3D Capabilities?](revisiting_3d_llm_benchmarks_are_we_really_testing_3d_capabilities.md)**

:   揭示了 3D LLM 评测中的"2D-Cheating"问题——将点云渲染为图像后，2D VLM 在部分基准上超越 3D SOTA，说明这些基准未能有效评估真正的 3D 理解能力，并据此提出了有效 3D 评测的设计原则。

**[REVS: Unlearning Sensitive Information in Language Models via Rank Editing in the Vocabulary Space](revs_unlearning_sensitive_information_in_language_models_via_rank_editing_in_the.md)**

:   提出 REVS，一种无梯度的模型编辑方法，通过在 FF2 层中定位与敏感 token 关联最强的神经元，将其投影到词汇空间后迭代降低目标 token 排名，在 SSN/Email/URL 三类敏感数据上 Unlearning Score 显著超越 6 种基线（89.58 vs 36.98），同时通用能力几乎零损（MMLU 61.05→60.87），且对 Logit-Lens 和 Delta 提取攻击高度鲁棒。

**[RuleArena: A Benchmark for Rule-Guided Reasoning with LLMs in Real-World Scenarios](rulearena_rule_guided_reasoning.md)**

:   提出 RuleArena——一个基于航空行李费、NBA交易规则、税务法规三个真实场景的benchmark，用于评估LLM遵循复杂自然语言规则进行推理的能力；实验发现即使最强模型（o1-preview）在最难任务上准确率也不足50%，暴露了LLM在规则召回、规则区分和数学计算三方面的系统性缺陷。

**[Safer Or Luckier Llms As Safety Evaluators Are Not Robust To Artifacts](safer_or_luckier_llms_as_safety_evaluators_are_not_robust_to_artifacts.md)**

:   系统评估了11个LLM裁判在安全领域的鲁棒性，发现道歉前缀等表面文本特征（artifact）可将评估偏好扭曲高达98%，提出基于jury的多模型聚合方案但仍未完全解决该问题。

**[SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models](saferoute_adaptive_model_selection_for_efficient_and_accurate_safety_guardrails_.md)**

:   提出 SafeRoute，一个二分类路由器，根据输入难度自适应地在小型和大型安全护栏模型之间选择，仅对约5%的"困难"样本使用大模型，在保持安全检测精度的同时大幅降低计算开销。

**[Safety is Not Only About Refusal: Reasoning-Enhanced Fine-tuning for Interpretable LLM Safety](safety_is_not_only_about_refusal_reasoning-enhanced_fine-tuning_for_interpretabl.md)**

:   提出 Rational 框架，通过推理增强微调让 LLM 在回答前进行显式的安全推理（分析意图、伦理和潜在危害），而非依赖僵硬的拒绝启发式，在保持有用性的同时显著提升对推理层面对抗攻击的鲁棒性。

**[Refining Salience-Aware Sparse Fine-Tuning Strategies for Language Models](salience_sparse_fine_tuning.md)**

:   首次系统评估 8 种 salience 指标用于稀疏微调（SPEFT）的效果，发现简单的梯度指标 + 静态掩码即可提供最佳性价比，在 GSM8k 上比 LoRA 高出 22.6%，质疑了"复杂方法才能做好 PEFT"的假设。

**[SANSKRITI: A Comprehensive Benchmark for Evaluating Language Models' Knowledge of Indian Culture](sanskriti_a_comprehensive_benchmark_for_evaluating_language_models_knowledge_of_.md)**

:   提出 SANSKRITI——一个包含 21,853 个问答对、覆盖印度全部 28 个邦和 8 个联邦属地、涵盖 16 类文化属性的大规模基准数据集，用于评估语言模型对印度文化多样性的理解程度。

**[Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](sarft_roleplay_safety.md)**

:   首次系统评估了角色扮演微调（role-play fine-tuning）对 LLM 安全性的影响，发现安全退化程度与角色特质（特别是反派角色）正相关，并提出 SaRFT 框架，通过隐式奖励函数自适应识别对不同角色有害的训练数据子集，配合 KL 散度正则化实现角色表现力与安全性的 Pareto 最优平衡。

**[SConU: Selective Conformal Uncertainty in Large Language Models](sconu_selective_conformal_uncertainty_in_large_language_models.md)**

:   提出选择性保形不确定性框架 SConU，通过构建保形 p-value 进行显著性检验，首次实现对违反可交换性假设的不确定性数据异常点的自动过滤，从而在单域和跨域 QA 场景中严格管理 LLM 的错误覆盖率。

**[Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion](second_language_arabic_acquisition_of_llms_via_progressive_vocabulary_expansion.md)**

:   受人类第二语言习得启发，提出渐进式词表扩展（Progressive Vocabulary Expansion）方法，通过分阶段指数增长地扩展阿拉伯语子词到 LLaMA2 词表中，在保留原模型英语知识的同时高效适配阿拉伯语，构建出 AraLLaMA 7B/13B 模型。

**[Stepwise Reasoning Disruption Attack of LLMs](seed_stepwise_reasoning_disruption_attack.md)**

:   提出 SEED（Stepwise rEasoning Error Disruption）攻击方法，通过在 LLM 的推理链前几步中巧妙注入细微错误（如微调计算数字），让模型在后续推理中自然传播错误得出错误答案，兼容零样本/少样本设置，GPT-4o 检测率低至 0.8%，揭示了 LLM 逐步推理过程的严重安全漏洞。

**[SeedBench: A Multi-task Benchmark for Evaluating Large Language Models in Seed Science](seedbench_a_multi-task_benchmark_for_evaluating_large_language_models_in_seed_sc.md)**

:   提出 SeedBench——首个面向种子科学（种子育种）的多任务 LLM 评测基准，包含 2,264 道专家验证题目，覆盖基因信息检索、基因功能调控和品种选育三大育种流程，对 26 个 LLM 进行系统评估，揭示了当前 LLM 与真实育种需求之间的显著差距。

**[Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](segment_level_diffusion.md)**

:   提出段落级扩散（Segment-Level Diffusion, SLD），将长文本输出切分为多个段落（如句子/对话轮次），对每个段落的潜在表示进行扩散建模，结合对比学习和对抗训练增强表示鲁棒性，在摘要、故事生成、对话生成等任务上实现了比现有扩散模型更好的长文本生成质量。

**[Self-Instructed Derived Prompt Generation Meets In-Context Learning: Unlocking New Potential of Black-Box LLMs](self-instructed_derived_prompt_generation_meets_in-context_learning_unlocking_ne.md)**

:   提出一种自指导强化学习框架来训练"派生提示生成模型"，并将派生提示-响应对作为上下文学习（ICL）示例来增强原始提示的查询，在不修改黑盒 LLM（如 GPT-4）参数的情况下显著提升响应质量。

**[Self-Training Elicits Concise Reasoning in Large Language Models](self-training_elicits_concise_reasoning_in_large_language_models.md)**

:   发现 LLM 输出分布中天然包含简洁推理路径，提出 FS-BoN（Few-shot 条件化 + Best-of-N 采样）自训练框架，从模型自身分布中筛选短且正确的推理样本进行微调，在 GSM8K 和 MATH 上跨 5 个模型族实现平均 30% token 缩减且不损准确率，效率为先前方法 Rational Metareasoning 的 2.4 倍。

**[Self-Tuning: Instructing LLMs to Effectively Acquire New Knowledge through Self-Teaching](self-tuning_instructing_llms_to_effectively_acquire_new_knowledge_through_self-t.md)**

:   受费曼学习法启发，提出 Self-Tuning 框架，通过记忆-理解-自省三层自教学策略，显著提升 LLM 从新文档中有效获取和回忆知识的能力。

**[SelfElicit: Your Language Model Secretly Knows Where is the Relevant Evidence](selfelicit_evidence_highlighting.md)**

:   SelfElicit 发现 LLM 深层注意力分数天然能识别上下文中的关键证据（即使回答错误时也是），据此提出推理时自动高亮关键证据句的上下文增强方法，无需训练即可显著提升基于证据的 QA 任务性能。

**[Semantic Aware Linear Transfer by Recycling Pre-trained Language Models for Cross-Lingual Transfer](semantic_aware_linear_transfer_by_recycling_pre-trained_language_models_for_cros.md)**

:   提出 SALT（Semantic Aware Linear Transfer），通过为每个非共享词表 token 基于语义相似的共享 token 对构建独立的最小二乘变换矩阵，将目标语言 PLM 的丰富嵌入表示迁移到英语中心 LLM 的嵌入空间，在下游任务、持续预训练收敛速度和跨语言理解上均优于现有方法。

**[Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis](shortcut_neuron_eval.md)**

:   提出通过对比分析和因果分析定位污染模型中的"捷径神经元"（shortcut neurons），并通过 activation patching 抑制这些神经元，实现更可信的 LLM 评估，与 MixEval 的 Spearman 相关系数超过 0.95。

**[Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents](simulating_diverse_students.md)**

:   提出一种基于知识图谱认知原型的免训练框架，使LLM Agent能够模拟不同认知水平学生的学习行为（包括错误），在GPT-4o上实现94%的行为预测准确率，相比基线提升100%。

**[SkillVerse: Assessing and Enhancing LLMs with Tree Evaluation](skillverse_tree_eval.md)**

:   提出 SkillVerse，一种无监督的树结构 LLM 诊断框架——用 LLM-as-Judge 批评模型回答后组织为层次化技能树（dendrogram），可在任意粒度上分析模型能力，并用于改善 ICL（提升 25%）和预测新模型弱点（55% 成功率，高于基线 22pp）。

**[SocialEval: Evaluating Social Intelligence of Large Language Models](socialeval_evaluating_social_intelligence_of_large_language_models.md)**

:   提出基于叙事脚本的双语社会智能基准 SocialEval，通过"世界树"结构整合结果导向的目标达成评估和过程导向的人际能力评估，全面评测 LLM 的社会智能。

**[SongComposer: A Large Language Model for Lyric and Melody Generation in Song Composition](songcomposer_llm_lyric_melody_generation.md)**

:   提出 SongComposer，首个能同时生成歌词和旋律的大语言模型，通过元组格式对齐歌词与旋律、标量音高初始化和渐进式结构感知训练，在多个歌曲生成任务上超越 GPT-4。

**[Splintering Nonconcatenative Languages for Better Tokenization](splintering_nonconcatenative_languages_for_better_tokenization.md)**

:   提出 Splinter，一种预分词步骤，通过迭代剪除模板字符将非拼接性语言（希伯来语、阿拉伯语、马来语）的词重排为线性形式，使标准 BPE/UnigramLM 能发现形态学上有意义的连续片段，在内在指标和希伯来语下游任务上均优于原始分词。

**[Sqlong Enhanced Nl2Sql For Longer Contexts With Llms](sqlong_enhanced_nl2sql_for_longer_contexts_with_llms.md)**

:   提出 SQLong，一种面向长上下文场景的 NL2SQL 数据增强框架，通过向训练数据中注入采样自其他数据库的合成 CREATE TABLE 语句来扩展上下文长度，使微调后的 LLM 在大规模 Schema 场景下显著提升 SQL 生成准确率。

**[Stem-Pom Evaluating Language Models Math-Symbol Reasoning In Document Parsing](stem-pom_evaluating_language_models_math-symbol_reasoning_in_document_parsing.md)**

:   提出 STEM-PoM 基准数据集（2K+ 数学符号实例），将 Part-of-Math Tagging 与文档解析结合，系统评估 LLM 对数学符号上下文多义性的分类能力，并证明符号分类能力的提升可迁移增强下游数学推理表现。

**[Stepwise Reasoning Disruption Attack of LLMs](stepwise_reasoning_disruption_attack_of_llms.md)**

:   提出SEED（Stepwise rEasoning Error Disruption）攻击方法，通过在LLM推理链的早期步骤中注入细微错误来误导模型产生错误的后续推理和最终答案，在四个数据集和四个模型上验证了高攻击成功率和极低的检测率。

**[Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs](stochastic_chameleons_irrelevant_context_hallucinations_reveal_class-based_misge.md)**

:   通过行为分析和机械可解释性实验揭示 LLM 无关上下文幻觉的内部机制：模型在底层构建抽象类别表示（如"语言"），然后两条竞争电路（query-based vs context-based）争夺特征选择权，相对激活强度决定正确泛化还是产生幻觉。

**[Stress-testing Machine Generated Text Detection: Shifting Language Models Writing Style to Fool Detectors](stress-testing_machine_generated_text_detection_shifting_language_models_writing.md)**

:   通过 DPO 微调将 LLM 的写作风格对齐到人类文本的语言特征分布，生成更难被检测的机器文本，揭示了现有 MGT 检测器对浅层语言线索的过度依赖。

**[StrucText-Eval: Evaluating Large Language Model's Reasoning Ability in Structure-Rich Text](structext_eval.md)**

:   提出StrucText-Eval——一个覆盖8种结构化语言（JSON/YAML/XML/Markdown/LaTeX/Org/CSV/Tree）和29个任务的自动生成评测基准，共5,800个样本，通过可控的嵌套深度和结构宽度调节难度。实验揭示开源LLM在标准集最高仅74.9%准确率，困难集降至45.8%，而人类在困难集达92.6%，暴露了LLM在复杂结构推理上的严重不足。

**[SynapticRAG: Enhancing Temporal Memory Retrieval in Large Language Models through Synaptic Mechanisms](synapticrag_enhancing_temporal_memory_retrieval_in_large_language_models_through.md)**

:   提出 SynapticRAG，借鉴神经科学中突触传播和漏积分发放（LIF）模型，将时序关联触发与语义相似度融合，在对话记忆检索任务上较 SOTA 提升最高 14.66%。

**[Synergizing Unsupervised Episode Detection with LLMs for Large-Scale News Events](synergizing_unsupervised_episode_detection_with_llms_for_large-scale_news_events.md)**

:   本文提出 EpiMine，一种无监督的 episode 检测框架，通过判别性词项共现驱动的文章分割与 LLM 协同，从新闻语料中检测关键事件下的 episode（子事件片段），在三个真实数据集上平均提升 59.2%。

**[Systematic Generalization in Language Models Scales with Information Entropy](systematic_generalization_in_language_models_scales_with_information_entropy.md)**

:   证明语言模型的系统泛化能力与训练数据中成分分布的信息熵正相关——高熵训练分布下即使没有内置组合先验的标准 seq2seq 模型也能实现强系统泛化。

**[T5Score: A Methodology for Automatically Assessing the Quality of LLM Generated Multi-Document Topic Sets](t5score_a_methodology_for_automatically_assessing_the_quality_of_llm_generated_m.md)**

:   提出 T5Score 方法论，将 LLM 生成的自由文本主题集(FT-topics)的质量分解为五个可量化维度（可解释性、主题覆盖、文档覆盖、非重叠性、内部排序），通过简单标注任务实现高标注者一致性，并验证 LLM 可作为自动评估器替代人工。

**[TaxoAdapt: Aligning LLM-Based Multidimensional Taxonomy Construction to Evolving Research Corpora](taxoadapt_aligning_llm-based_multidimensional_taxonomy_construction_to_evolving_.md)**

:   提出 TaxoAdapt 框架，通过层次分类驱动的深度/宽度扩展和分类感知聚类，将 LLM 生成的多维度分类体系动态对齐到特定科学语料库，在粒度保持和兄弟节点一致性上分别超越最优基线 26.51% 和 50.41%。

**[Team Anotheroption at SemEval-2025 Task 8: Bridging the Gap Between Open-Source and Proprietary LLMs in Table QA](team_anotheroption_at_semeval-2025_task_8_bridging_the_gap_between_open-source_a.md)**

:   提出一种混合 LLM 管道系统，通过 Text-to-SQL/Code 生成、RAG 检索、自纠错机制和 LLM Orchestrator 协调多个开源模型，在 SemEval-2025 Task 8（表格问答）中达到 80% 准确率（Top-13/38），开源模型组合（88%）超越 GPT-4o 单模型（74%）。

**[Tess 2 A Large-Scale Generalist Diffusion Language Model](tess_2_a_large-scale_generalist_diffusion_language_model.md)**

:   提出 TESS 2，首个从已有自回归模型适配而来的大规模通用指令遵循扩散语言模型，通过 UL2 masking + label shifting + 双向注意力的适配训练方案 + reward guidance 推理引导，在 QA 和指令遵循任务上匹配甚至超越同等 AR 模型。

**[Can LLMs Generate High-Quality Test Cases for Algorithm Problems? TestCase-Eval](testcase_eval_llm_test_gen.md)**

:   提出 TestCase-Eval 基准评估 LLM 生成算法题测试用例的能力，包含 500 道 Codeforces 算法题和 10 万条人工解答，聚焦两个任务——故障覆盖（测试集能覆盖多少潜在错误）和故障暴露（能否为特定错误代码生成暴露性测试），对 19 个 SOTA LLM 的评估揭示了当前模型在测试生成上的能力和局限。

**[The Hidden Space Of Safety Understanding Preference-Tuned Llms In Multilingual C](the_hidden_space_of_safety_understanding_preference-tuned_llms_in_multilingual_c.md)**

:   本文系统分析了偏好调优（RLHF/DPO 等）对 LLM 内部表示空间在多语言场景下的影响，发现对齐机制在英语上能有效分离有害/无害内容的隐空间表示，但在印地语、中文、德语等非英语语言上效果显著退化，揭示了当前对齐方法存在严重的单语偏差问题。

**[The Nature of NLP: Analyzing Contributions in NLP Papers](the_nature_of_nlp_analyzing_contributions_in_nlp_papers.md)**

:   提出 NLP 论文贡献的分类体系（知识/工件 × 8 子类），构建 ~2k 人工标注数据集 NLPContributions，训练 SciBERT 自动识别贡献声明，并对 ~29k 篇 ACL Anthology 论文做 50 年纵向趋势分析，揭示 NLP 研究从语言学导向转向方法/模型主导、近年又重拾人文与语言关注的演化轨迹。

**[A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive](theory_of_llm_sampling.md)**

:   本文从认知科学视角揭示了LLM的采样启发式机制与人类决策类似：采样不仅反映概念的统计规范（描述性成分），还系统性地偏向隐含的理想值（规范性成分），这种偏移在500个概念、15个模型上均显著，并可能导致医疗等应用中的有偏决策。

**[Theory of Mind in Large Language Models: Assessment and Enhancement](theory_of_mind_llm.md)**

:   系统综述了 LLM 的心智理论（ToM）能力的评估基准（10+ story-based benchmarks）和增强策略（prompt-only 和 fine-tuning 两类方法），指出当前 LLM 在 ToM 推理上仍有显著不足，并提出未来方向。

**[To Code Or Not To Code Adaptive Tool Integration For Math Language Models Via Ex](to_code_or_not_to_code_adaptive_tool_integration_for_math_language_models_via_ex.md)**

:   提出基于EM框架的AutoCode方法，让数学LLM自主决定何时使用代码工具辅助推理，通过E-step引导探索高潜力代码触发决策+M-step离线RL优化，7B模型在MATH500上提升11%+。

**[The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](token_granularity_impact.md)**

:   本文系统研究了子词 token 粒度（词表大小 256~128K）对语言模型 surprisal 预测人类阅读时间能力的影响，发现约 8K 词表大小的中等粒度 token 在自然阅读时间预测上最优，而更粗粒度（更接近词级）的 token 在花园路径句法效应上表现更敏感。

**[Token Prepending: A Training-Free Approach for Eliciting Better Sentence Embeddings from LLMs](token_prepending_training_free.md)**

:   提出 Token Prepending (TP) 技术，通过在每层将解码得到的句子嵌入前置到句子开头，使因果注意力机制下的早期 token 也能感知完整句子信息，无需训练即可显著提升 LLM 的句子嵌入质量。

**[Turning Trash into Treasure: Accelerating Inference of Large Language Models with Token Recycling](token_recycling.md)**

:   提出Token Recycling——一种无需额外训练的投机解码方法，将解码过程中产生的候选token存入邻接矩阵，通过BFS算法构建draft tree并用tree attention验证，仅需<2MB额外存储即在所有规模LLM上实现约2倍加速，超越现有无训练方法30%和有训练方法25%。

**[Tokenization is Sensitive to Language Variation](tokenization_is_sensitive_to_language_variation.md)**

:   系统研究了 BPE tokenizer 的三个关键设计选择（拟合语料、pre-tokenizer、词表大小）对语言变体鲁棒性任务和敏感性任务下游性能的差异化影响，并提出基于 logistic regression 的 task-aware tokenizer 评估指标，显著优于 Rényi efficiency 等 task-agnostic 指标。

**[Toolcoder A Systematic Code-Empowered Tool Learning Framework For Large Language](toolcoder_a_systematic_code-empowered_tool_learning_framework_for_large_language.md)**

:   ToolCoder 将工具学习重新建模为代码生成任务，借鉴软件工程的需求分析、模块化设计、代码复用和错误诊断原则，让 LLM 通过生成并执行结构化 Python 代码来调用外部工具，在 RestBench 和 API-Bank 基准上显著超越 ReAct、CodeAct 等现有方法。

**[ToolCoder: A Systematic Code-Empowered Tool Learning Framework for Large Language Models](toolcoder_code_empowered_tool_learning.md)**

:   提出 ToolCoder 框架，将工具学习重新定义为代码生成任务，借鉴软件工程原则（需求分析→模块化设计→实现执行→错误调试→代码复用）让 LLM 通过生成和执行 Python 代码来完成多步工具调用，在 RestBench 和 API-Bank 上全面超越 ReAct、CodeAct 等基线方法。

**[Towards Dynamic Theory Of Mind Evaluating Llm Adaptation To Temporal Evolution O](towards_dynamic_theory_of_mind_evaluating_llm_adaptation_to_temporal_evolution_o.md)**

:   提出 DynToM 基准，通过 1,100 个社会情境中 5,500 个时序关联场景和 78,100 道题目，评估 LLM 追踪人类心理状态时序演化的能力，揭示模型平均落后人类 44.7%。

**[Towards Explainable Temporal Reasoning in Large Language Models: A Structure-Aware Generative Framework](towards_explainable_temporal_reasoning_in_large_language_models_a_structure-awar.md)**

:   提出 GETER 框架，通过轻量级 Structure-Text Adapter 将时序知识图谱的结构信息注入 LLM，使模型在时序推理任务中既能给出准确预测又能生成可解释的推理说明。

**[Towards Harmonized Uncertainty Estimation for Large Language Models](towards_harmonized_uncertainty_estimation_for_large_language_models.md)**

:   提出 CUE 框架，通过训练一个与目标 LLM 性能对齐的轻量级分类器（Corrector）来校正现有不确定性估计方法的分数，在指示性、精确-召回平衡和校准三个维度上实现协调一致的改进，最高提升达 60%。

**[Training Dynamics Underlying Language Model Scaling Laws: Loss Deceleration and Zero-Sum Learning](training_dynamics_underlying_language_model_scaling_laws_loss_deceleration_and_z.md)**

:   发现语言模型训练中存在 loss deceleration（损失减速）现象——损失曲线在 log-log 空间呈分段线性，根因是 zero-sum learning（ZSL）：per-token 梯度系统性对立导致破坏性干涉，将一部分样本的改善抵消另一部分的恶化；scale up 通过降低减速触发损失 $L_d$ 和提升减速后斜率 $r_d$ 来缓解 ZSL，为突破 scaling law 瓶颈提供了可直接干预的机制。

**[Training Language Model to Critique for Better Refinement](training_language_model_to_critique_for_better_refinement.md)**

:   提出 Refinement-oriented Critique Optimization（RCO），以"批判效用"（Critique Utility, CU）——即批判导致的精炼改善比例——作为奖励信号训练 critic 模型，通过 DPO 变体的 MSE 目标函数优化，无需直接评估批判质量；在对话生成、摘要、问答、数学推理、代码生成 5 个任务上，RCO 训练的 7B/13B critic 模型在 CU 和 RQS 指标上显著超过 70B 基线模型和 DPCO 方法。

**[Trans-Zero Self-Play Incentivizes Large Language Models For Multilingual Transla](trans-zero_self-play_incentivizes_large_language_models_for_multilingual_transla.md)**

:   提出 Trans-Zero 自博弈框架，仅使用单语数据，通过遗传蒙特卡洛树搜索（G-MCTS）在多语言翻译过程中探索语义一致的候选翻译，结合偏好优化实现无平行数据的多语言翻译训练，性能可媲美大规模监督微调方法。

**[Transforming Podcast Preview Generation From Expert Models To Llm-Based Systems](transforming_podcast_preview_generation_from_expert_models_to_llm-based_systems.md)**

:   Spotify 提出用 LLM（Gemini 1.5 Pro）替代传统多模型特征工程流水线来生成播客预览片段，在离线人工评估和线上 A/B 测试中均显著优于传统系统，用户互动时长提升 4.6%，处理效率提升 5 倍。

**[Translate With Care: Addressing Gender Bias, Neutrality, and Reasoning in Large Language Model Translations](translate_with_care_addressing_gender_bias_neutrality_and_reasoning_in_large_lan.md)**

:   提出 Translate-with-Care (TWC) 数据集（3,950 条跨 6 种无性别语言的翻译挑战），系统揭示 GPT-4、Google Translate 等模型在无性别→有性别语言翻译中的性别偏见和推理错误，并通过微调 mBART-50 在偏见消除和翻译准确率上大幅超越闭源 LLM。

**[TRATES: Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring](trates_trait-specific_rubric-assisted_cross-prompt_essay_scoring.md)**

:   提出 TRATES 框架，重新定义 LLM 在自动作文评分中的角色——从直接评分者转变为**特质特征生成器与提取器**，通过 LLM 将评分标准(rubric)自动转化为评估问题(子特质)，结合通用写作质量特征和提示特定特征训练回归模型，在 ASAP 数据集 8 个特质上全部达到 SOTA，且首次在 ELLIPSE 数据集上建立跨提示特质评分基线。

**[Treecut A Synthetic Unanswerable Math Word Problem Dataset For Llm Hallucination](treecut_a_synthetic_unanswerable_math_word_problem_dataset_for_llm_hallucination.md)**

:   提出 TreeCut，一种基于树结构的合成数据集生成方法，通过在树路径上移除必要条件边来系统性生成无穷多的不可回答数学应用题，用以评估 LLM 在面对不可解问题时的幻觉行为。

**[Tremu Towards Neuro-Symbolic Temporal Reasoning For Llm-Agents With Memory In Mu](tremu_towards_neuro-symbolic_temporal_reasoning_for_llm-agents_with_memory_in_mu.md)**

:   提出TReMu框架，通过时间感知记忆化（时间线摘要）和神经符号时间推理（LLM生成Python代码执行时间计算），将GPT-4o在多会话对话时间推理基准上的准确率从29.83%提升到77.67%。

**[UAlign: Leveraging Uncertainty Estimations for Factuality Alignment on Large Language Models](ualign_leveraging_uncertainty_estimations_for_factuality_alignment_on_large_lang.md)**

:   提出 UAlign 框架，利用置信度分数和语义熵两种不确定性估计来显式建模 LLM 知识边界，并将其作为输入特征融入 PPO 对齐训练，使模型自信回答已知问题、坚定拒绝未知问题，在多个知识 QA 数据集上显著提升可靠性与泛化性。

**[UAQFact: Evaluating Factual Knowledge Utilization of LLMs on Unanswerable Questions](uaqfact_evaluating_factual_knowledge_utilization_of_llms_on_unanswerable_questio.md)**

:   提出双语不可回答问题数据集UAQFact（13,970题），每个问题附带知识图谱事实知识，定义三个评估任务分别衡量LLM区分不可回答问题（UAQ）与可回答问题（ABQ）、利用内部/外部事实知识处理UAQ的能力，实验揭示即使LLM已存储相关知识也难以有效利用。

**[Un-considering Contextual Information: Assessing LLMs' Understanding of Indexical Elements](un-considering_contextual_information_assessing_llms_understanding_of_indexical_.md)**

:   首次系统评估 LLM 对英语指示词（I/you/here/tomorrow）的理解能力，发现模型在 "I" 上表现接近人类但在 "you/here/tomorrow" 上严重依赖无关上下文信息而非语法规则，揭示了 LLM 在语用推理上的根本缺陷。

**[Uncertainty Unveiled: Can Exposure to More In-context Examples Mitigate Uncertainty for Large Language Models?](uncertainty_unveiled_can_exposure_to_more_in-context_examples_mitigate_uncertain.md)**

:   本文系统研究了长上下文 ICL 中增加示例数量对 LLM 预测不确定性的影响，通过不确定性分解揭示性能提升主要源于认知不确定性（EU）的降低，并从残差流投影角度解释了不确定性减少的内部机制。

**[Understanding and Meeting Practitioner Needs When Measuring Representational Harms Caused by LLM-Based Systems](understanding_and_meeting_practitioner_needs_when_measuring_representational_har.md)**

:   通过对 12 位负责评估 LLM 系统表征性伤害（representational harms）的从业者进行半结构化访谈，发现公开可用的测量工具普遍无法满足实践者需求——要么因效度/特异性不足而"不好用"（not useful），要么因组织/制度壁垒而"用不了"（not used），并基于测量理论和实用测量框架提出系统性改进建议。

**[Understanding the Repeat Curse in Large Language Models from a Feature Perspective](understanding_the_repeat_curse_in_large_language_models_from_a_feature_perspecti.md)**

:   从机制可解释性角度研究 LLM 重复生成问题（Repeat Curse），用 Sparse Autoencoder 提取单语义特征，定位中间层和最终层的"重复特征"，激活它们可诱导重复、关闭它们可缓解重复且不损害模型性能。

**[UniConv: Unifying Retrieval and Response Generation for Large Language Models in Conversations](uniconv_retrieval_response_gen.md)**

:   探索如何将对话场景中的稠密检索和响应生成统一到单个 LLM 中，通过三个联合训练目标（对话检索 + 响应生成 + 上下文识别指令）和数据差异缓解机制，在五个对话搜索数据集上实现检索和生成的相互促进，超越分离式基线。

**[Unintended Harms of Value-Aligned LLMs: Psychological and Empirical Insights](unintended_harms_of_value-aligned_llms_psychological_and_empirical_insights.md)**

:   本文首次系统揭示了基于Schwartz价值观对齐的LLM存在非预期安全风险——特定价值维度与特定安全风险类别显著相关，并从心理学视角解释了这些关联的根源，进而提出通过提示抑制相关价值来降低有害行为的缓解策略。

**[ScaleQuest: Unleashing LLM Reasoning Capability via Scalable Question Synthesis from Scratch](unleashing_llm_reasoning_capability_via_scalable.md)**

:   提出 ScaleQuest，通过 Question Fine-Tuning (QFT) + Question Preference Optimization (QPO) 两阶段训练将 7B 解题模型变为出题模型，从零合成 100 万高质量数学问题-解答对，在四个基准上全面超越所有开源数据集，且数据量扩展至 1M 时性能持续提升未见饱和。

**[Unlocking Recursive Thinking of LLMs: Alignment via Refinement](unlocking_recursive_thinking_of_llms_alignment_via_refinement.md)**

:   提出 AvR（Alignment via Refinement）两阶段框架，通过细化感知奖励（refinement-aware reward）和差分学习，让 LLM 学会"批评→改进"的递归思维能力，仅用 10k 数据即在 AlpacaEval 2 上将 LLaMA-3-8B-Instruct 的胜率提升超 26 个百分点。

**[Unsupervised Morphological Tree Tokenizer](unsupervised_morphological_tree_tokenizer.md)**

:   提出 TreeTok，一种基于无监督神经形态结构归纳的分词器，通过 MorphOverriding 机制和自监督目标学习字符级树结构，以自顶向下词表匹配方式进行分词，在形态分割和语言建模任务上均优于 BPE/WordPiece。

**[Unveiling And Addressing Pseudo Forgetting In Large Language Models](unveiling_and_addressing_pseudo_forgetting_in_large_language_models.md)**

:   揭示 LLM 持续学习中的"伪遗忘"现象：性能下降并非因为模型丧失了旧任务能力，而是指令无法正确激活已有能力。通过归因分析证明遗忘模型的指令依赖度降低，并提出基于 Rationale-Guidance Difficulty（RGD）的动态数据回放框架 RGD-R 来缓解伪遗忘。

**[Veracity Bias and Beyond: Uncovering LLMs' Hidden Beliefs in Problem-Solving Reasoning](veracity_bias_llm_hidden_beliefs.md)**

:   揭示了 LLM 在推理任务中存在"真实性偏见"（Veracity Bias）——尽管显式对齐反对刻板印象，LLM 仍系统性地将正确答案归因于特定种族群体（归因偏差），并对相同解答因"作者"种族不同给出不同评价（评估偏差），在数学、编程、常识推理和写作任务中普遍存在。

**[Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System](virsci_multi_agent_idea_gen.md)**

:   提出基于 LLM 的多智能体系统 Virtual Scientists（VirSci），模拟真实科研团队的协作过程——组织多个 agent 团队协作生成、评估和改进科研 idea，在生成新颖科学想法方面超越单智能体 SOTA。

**[VoxEval: Benchmarking the Knowledge Understanding Capabilities of End-to-End Spoken Language Models](voxeval_benchmarking_the_knowledge_understanding_capabilities_of_end-to-end_spok.md)**

:   提出 VoxEval，首个支持端到端纯语音输入-输出评估的 SpeechQA 基准，涵盖 56 个学科、26 种输入音频条件，系统揭示了当前端到端语音大模型在知识理解和数学推理方面的严重不足。

**[When Large Language Models Meet Speech: A Survey on Integration Approaches](when_large_language_models_meet_speech_a_survey_on_integration_approaches.md)**

:   系统综述语音与大语言模型的集成方法，将现有工作分为文本级、隐表示级、音频token级三大类，覆盖 ASR/S2TT/S2ST/TTS 等应用场景，并给出各方法的优劣对比与未来挑战。

**[Which Demographics Do LLMs Default to During Annotation?](which_demographics_do_llms_default_to_during_annotation.md)**

:   通过对比 LLM 在无人口统计信息(N)、有人口统计(SD)、安慰剂信息(P)三种 prompt 条件下的标注行为，揭示 LLM 在主观标注任务(冒犯性/礼貌性)中默认更接近白人、年轻、高学历群体的标注模式，且人口统计 prompting 确实产生了比安慰剂信息更系统性的影响。

**[Which Retain Set Matters For Llm Unlearning A Case Study On Entity Unlearning](which_retain_set_matters_for_llm_unlearning_a_case_study_on_entity_unlearning.md)**

:   系统研究实体遗忘中 retain set 的选择问题，提出 Syntactically Similar Neighbor Set，发现句法相似性（而非领域/实体相似性）才是遗忘过程中知识退化的主要驱动因素，用句法相似的 retain set 做正则化可同时最优保护所有类型的邻居知识。

**[Why Not Act on What You Know? Unleashing Safety Potential of LLMs via Self-Aware Guard Enhancement](why_not_act_on_what_you_know_unleashing_safety_potential_of_llms_via_self-aware_.md)**

:   发现 LLM 作为判别器时能准确识别越狱请求、但作为生成器时却仍产出有害内容的"判别-生成安全差距"，提出免训练的 SAGE（Self-Aware Guard Enhancement）策略，通过判别分析模块和判别响应模块将模型自身的安全鉴别能力桥接到生成行为，在 6 个模型上达到平均 99% 的防御成功率。

**[Zero-Shot Belief: A Hard Problem for LLMs](zero-shot_belief_a_hard_problem_for_llms.md)**

:   本文提出了统一式和混合式两种零样本框架用于源-目标信念预测任务，使用 DeBERTa 事件标注器 + LLM 的混合方法在 FactBank 上达到新 SOTA（Full F1 72.0%），同时揭示了嵌套信念预测（Nested F1 仅 25.3%）对 LLM 而言仍是极大挑战。
