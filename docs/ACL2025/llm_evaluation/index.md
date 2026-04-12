---
title: >-
  ACL2025 LLM评测方向 73篇论文解读
description: >-
  73篇ACL2025 LLM评测方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📊 LLM评测

**💬 ACL2025** · 共 **73** 篇

**[A Conformal Risk Control Framework For Granular Word Assessment And Uncertainty ](a_conformal_risk_control_framework_for_granular_word_assessment_and_uncertainty_.md)**

:   提出基于保形风险控制（Conformal Risk Control）框架校准 CLIPScore 的方法——通过对 CLIP 视觉/文本编码器的注意力掩码采样生成 CLIPScore 分布，然后利用保形风险控制 (1) 检测图像描述中的干扰词（foil words），(2) 生成校准置信区间，在 FOIL-it/FOIL-nocaps/Rich-HF 基准上以简单方法达到与复杂专用方法相当的干扰词检测性能，同时提供形式化风险保证。

**[MisMatched: A Benchmark for Scientific Natural Language Inference](a_mismatched_benchmark_for_scientific_natural_language_inference.md)**

:   引入 MisMatched——首个覆盖非 CS 领域（心理学、工程、公共卫生）的科学 NLI 评估基准，2700 对人工标注句子对，最佳基线 Macro F1 仅 78.17%，且发现训练时加入隐式关系句子对可提升性能。

**[Abgen Evaluating Large Language Models In](abgen_evaluating_large_language_models_in.md)**

:   提出 AbGen——首个评估 LLM 设计消融实验能力的基准（1500 条专家标注数据来自 807 篇 NLP 论文），发现最强 LLM (DeepSeek-R1) 与人类专家差距 14.4%，且 LLM-as-Judge 评分与人类评估严重不一致。

**[Access Denied Inc: The First Benchmark Environment for Sensitivity Awareness](access_denied_inc_the_first_benchmark_environment_for_sensitivity_awareness.md)**

:   提出敏感性感知（Sensitivity Awareness, SA）概念——评估 LLM 是否能遵守基于角色的访问控制规则——并构建首个评估基准 Access Denied Inc：模拟企业数据库 + 多用户组权限 + 自动化问卷+半自动评分（99.9%自动），揭示模型在拒绝未授权请求和响应合法查询上的显著差异。

**[Ad-Hoc Concept Forming In The Game Codenames As A Means For Evaluating Large Lan](ad-hoc_concept_forming_in_the_game_codenames_as_a_means_for_evaluating_large_lan.md)**

:   以桌游 Codenames 作为 LLM 评测工具——LLM 分别扮演线索给出者（Spymaster）和猜测者（Field Operative），通过控制词频/歧义性/具体性/风险等级/对手速度等变量系统评估 LLM 的临时概念形成、语义关联、合作推理和语用能力，发现 o3-mini 和 Claude-3.5 领先但所有模型在高风险和抽象词条件下均显著退化。

**[Ad-Llm Benchmarking Large Language Models For Anomaly Detection](ad-llm_benchmarking_large_language_models_for_anomaly_detection.md)**

:   首个系统评估 LLM 在 NLP 异常检测中角色的基准 AD-LLM——覆盖三个关键任务：(1) 零样本检测（LLM 预训练知识直接做 AD），(2) 数据增强（生成合成数据/类别描述提升 AD 模型），(3) 模型选择（LLM 推荐无监督 AD 模型）。多数据集实验发现 LLM 零样本 AD 表现出色，精心设计的增强有用，但模型选择的可解释性仍是挑战。

**[Androidlab Autonomous Agent](androidlab_autonomous_agent.md)**

:   提出AndroidLab——首个统一训练和评估Android Agent的系统性框架，包含9个App上的138个可复现任务，同时支持纯文本（XML模式）和多模态（SoM模式）模型，并构建Android Instruct数据集（94.3k步骤），将开源LLM的成功率从4.59%提升至21.50%。

**[Antileakbench Preventing Data Contamination By Automatically Constructing Benchm](antileakbench_preventing_data_contamination_by_automatically_constructing_benchm.md)**

:   提出 AntiLeakBench——自动化反泄露基准框架，通过识别 LLM 知识截止后更新的真实世界新知识自动构建 QA 测试样本（而非简单收集新发布数据），确保测试知识严格不在训练集中，全自动流程无需人工标注，实验证实截止后性能普遍下降验证了数据污染的普遍存在。

**[Atomic Calibration Of Llms In Long-Form Generations](atomic_calibration_of_llms_in_long-form_generations.md)**

:   系统研究长文本生成中的原子级校准（Atomic Calibration）——将长回复分解为原子主张（atomic claims），为每个主张分配置信度分数，发现回复级校准良好的模型在原子级校准很差，将置信度获取方法分为判别式（内部状态）和生成式（外部评估）两类并发现它们互补，提出两种融合策略达到 SOTA 校准效果。

**[Batayan A Filipino Nlp Benchmark For Evaluating Large Language Models](batayan_a_filipino_nlp_benchmark_for_evaluating_large_language_models.md)**

:   提出 Batayan——首个全面的菲律宾语 LLM 评测基准，覆盖理解/推理/生成三大能力的 8 个任务（含 3 个全新菲律宾语任务），由母语者翻译和标注确保语言真实性，评测 50+ 开源和商用 LLM 后发现菲律宾语表现显著落后于英语，显式菲律宾语支持和模型规模的提升均能带来明显增益。

**[Belarusian Glue](belarusian_glue.md)**

:   为白俄罗斯语（Belarusian，东斯拉夫语族）构建了首个NLU benchmark——BelarusianGLUE，包含5个任务约15K条实例，系统评估了BERT系列和LLM的表现，发现简单任务（情感分析）接近人类水平但难任务（Winograd）仍有显著差距，且最优模型类型因任务而异。

**[Besstie A Benchmark For Sentiment And Sarcasm Classification For Varieties Of En](besstie_a_benchmark_for_sentiment_and_sarcasm_classification_for_varieties_of_en.md)**

:   构建 BESSTIE，首个针对英语变体（澳大利亚/印度/英国英语）的情感分析和讽刺检测标注基准，通过 9 个微调 LLM 评估发现模型在印度英语（外圈变体）上表现显著差于内圈变体，跨变体泛化能力也有限。

**[Beyond One-Size-Fits-All Tailored Benchmarks For Efficient Evaluation](beyond_one-size-fits-all_tailored_benchmarks_for_efficient_evaluation.md)**

:   提出 TailoredBench 方法，为每个待评估的目标模型**自适应构建定制化核心集**（Native-coreset），而非使用所有模型共享的静态子集，通过自适应源模型选择、可扩展 K-Medoids 聚类和校准估计策略，在仅需 20-40 个样本的推理预算下将准确率估计的 MAE 平均降低 **31.4%**。

**[Browsing Lost Unformed Recollections A Benchmark For Tip-Of-The-Tongue Search An](browsing_lost_unformed_recollections_a_benchmark_for_tip-of-the-tongue_search_an.md)**

:   > 提出 BLUR（Browsing Lost Unformed Recollections），一个包含 573 道真实"话到嘴边"(tip-of-the-tongue) 已知物品搜索与推理问题的基准数据集，人类准确率 98%，而最佳 AI 系统仅约 56%，揭示了当前 AI 在工具使用和多跳推理上的巨大差距。

**[Calibraeval Calibrating Prediction Distribution To Mitigate Selection Bias In Ll](calibraeval_calibrating_prediction_distribution_to_mitigate_selection_bias_in_ll.md)**

:   提出 CalibraEval，一种无标签的推理时去偏方法，通过将去偏问题形式化为优化任务，利用非参数保序算法（NOA）学习校准函数，将 LLM 评判器的观测概率分布映射到无偏分布，有效缓解 LLM-as-Judge 中的选择偏差。

**[Calibration Confidence Text Gen](calibration_confidence_text_gen.md)**

:   针对文本生成中多个有效输出导致传统置信度指标失效的问题，提出两种任务无关的置信度度量——"比率"（头部vs中部概率比）和"尾部稀薄度"（分布尾部薄厚），仅依赖模型输出概率即可改善 BART/Flan-T5 在摘要、翻译、问答任务上的置信度校准。

**[Can External Validation Tools Improve Annotation Quality For Llm-As-A-Judge](can_external_validation_tools_improve_annotation_quality_for_llm-as-a-judge.md)**

:   提出 Evaluation Agent，一个工具增强的 LLM-as-a-Judge 框架，通过集成网络搜索（事实核查）、代码执行和数学验证工具，在长文本事实验证上将与人类一致性从 63% 提升到 81%，在编程评估上从 31% 提升到 71%，且对无关领域几乎无退化。

**[Cfbench A Comprehensive Constraints-Following Benchmark For Llms](cfbench_a_comprehensive_constraints-following_benchmark_for_llms.md)**

:   提出 CFBench——一个包含 1000 条精标样本、覆盖 200+ 真实场景和 50+ NLP 任务的中文大规模约束遵循基准，系统性地定义了 10 大类 25+ 子类的约束分类体系，并设计结合约束满足率（CSR）、指令满足率（ISR）和需求优先级满足率（PSR）的多维评估框架，揭示当前顶级 LLM 在约束遵循方面仍存在显著提升空间。

**[Chatbench From Static Benchmarks To Human-Ai Evaluation](chatbench_from_static_benchmarks_to_human-ai_evaluation.md)**

:   通过用户实验将 MMLU 静态基准转换为用户-AI 对话，构建 ChatBench 数据集（396 道题、7336 段对话），发现 AI-alone 准确率无法预测 user-AI 准确率，并训练用户模拟器使相关性提升 22-26 个百分点，为可扩展的交互式评估奠基。

**[Codemenv Benchmarking Large Language Models On Code Migration](codemenv_benchmarking_large_language_models_on_code_migration.md)**

:   提出 CodeMEnv，首个系统评估 LLM 跨环境代码迁移能力的基准，包含 922 个样本、19 个 Python/Java 包、3 个层次化任务（定位不兼容函数→描述变更→迁移代码），9 个 LLM 的平均 Pass@1 仅 26.50%，GPT-4o 最高 43.84%，揭示 LLM 更熟悉新版本函数且存在版本推理逻辑不一致问题。

**[Com2 Causal Commonsense](com2_causal_commonsense.md)**

:   提出Com2基准，利用因果事件图和因果理论（干预/反事实）构建复杂常识推理任务，发现LLM在推理深度和广度上存在不足，后训练和慢思考可部分缓解。

**[Culemo Cultural Lenses On Emotion - Benchmarking Llms For Cross-Cultural Emotion](culemo_cultural_lenses_on_emotion_-_benchmarking_llms_for_cross-cultural_emotion.md)**

:   提出 CuLEmo，首个评估文化感知情感预测的多语言基准数据集，涵盖 6 种语言/文化（阿姆哈拉语、阿拉伯语、英语、德语、印地语、西班牙语），通过 400 个文化相关场景评估 LLM 的跨文化情感理解能力，发现情感表达在不同文化间存在显著差异且 LLM 表现参差不齐。

**[Culturalbench A Robust Diverse And Challenging Cultural Benchmark By Human-Ai Cu](culturalbench_a_robust_diverse_and_challenging_cultural_benchmark_by_human-ai_cu.md)**

:   通过 Human-AI CulturalTeaming（人机协作红队测试）流水线构建 CulturalBench，包含 1,696 个人类撰写并经五人独立验证的文化知识问题，覆盖 45 个全球地区和 17 个主题。CulturalBench-Hard（True/False格式）对最强模型（OpenAI o1）也仅 61.5%，远低于人类的 92.4%，揭示了模型在多答案问题上的模式寻求倾向和跨区域文化知识的不均衡表现。

**[Ecomscriptbench](ecomscriptbench.md)**

:   提出电商脚本规划（EcomScript）任务及其首个大规模benchmark EcomScriptBench（605K脚本、2.4M产品），通过购买意图（purchase intention）桥接用户行动步骤与产品检索的语义鸿沟，实验发现当前LLM在涉及产品的子任务上表现显著不足，注入意图知识可提升性能。

**[Educationq Evaluating Llms Teaching Capabilities Through Multi-Agent Dialogue Fr](educationq_evaluating_llms_teaching_capabilities_through_multi-agent_dialogue_fr.md)**

:   提出 EducationQ 多智能体对话框架，通过模拟真实课堂中教师-学生的形成性评估交互来评估 LLM 的教学能力，发现教学效果与模型规模或通用推理能力不呈线性关系，Llama 3.1 70B 在教学中表现最优。

**[Elaboration Competitive Programming](elaboration_competitive_programming.md)**

:   提出ELABORATION——首个全面评估人类-LLM协作竞赛编程的基准，包含覆盖编程全流程（理解→规划→编码→调试）的人类反馈分类体系和8320题精标注数据集，实验表明LLM在困难题上仅3.4% Pass@1，但人类反馈（特别是在编码阶段）可平均提升9.3%。

**[Evowiki Evaluating Llms On Evolving Knowledge](evowiki_evaluating_llms_on_evolving_knowledge.md)**

:   提出 EvoWiki，一个可自动更新的动态评估基准，将知识分为稳定（stable）、演化（evolved）和未知（uncharted）三个层级，用于评估 LLM 在知识持续演化场景下的利用能力，并揭示 RAG 与持续学习（CL）结合具有协同效应。

**[Exposing Numeracy Gaps A Benchmark To Evaluate Fundamental Numerical Abilities I](exposing_numeracy_gaps_a_benchmark_to_evaluate_fundamental_numerical_abilities_i.md)**

:   提出 NumericBench 综合基准，通过 6 类数据集评估 LLM 的 6 种基本数值能力（数字识别、算术运算、上下文检索、比较、汇总、逻辑推理），发现包括 GPT-4o、DeepSeek-V3 在内的 SOTA 模型在简单数值任务上仍表现极差，并深入分析了 5 种根因。

**[Financereasoning Benchmarking Financial Numerical Reasoning More](financereasoning_benchmarking_financial_numerical_reasoning_more.md)**

:   提出 FinanceReasoning benchmark，通过重标注公开数据集、构建 3,133 个 Python 金融函数库和新增 908 道专家标注难题，在可信度、全面性和挑战性三个维度提升金融数值推理评估能力。

**[From Tools To Teammates Evaluating Llms In Multi-Session Coding Interactions](from_tools_to_teammates_evaluating_llms_in_multi-session_coding_interactions.md)**

:   提出 MemoryCode 合成多会话数据集评估 LLM 在长期交互中追踪和执行编码指令的能力，发现即使 GPT-4o 在提供完整对话历史时准确率也下降 67%，揭示了当前 LLM 在前瞻性记忆和信息整合上的根本局限。

**[Grace A Granular Benchmark For Evaluating Model Calibration Against Human Calibr](grace_a_granular_benchmark_for_evaluating_model_calibration_against_human_calibr.md)**

:   提出GRACE基准，通过渐进式增量问答和真人vs模型竞赛收集1749个数据点，以人类校准表现为参照评估LLM校准能力，并引入CalScore指标发现：虽然人类准确率可能低于模型，但人类在校准方面普遍优于SOTA模型——模型在不确定时过度自信、在正确时又信心不足。

**[Guessarena Guess Who I Am A](guessarena_guess_who_i_am_a.md)**

:   提出 GuessArena，一种基于"猜猜我是谁"博弈游戏的自适应 LLM 评估框架，通过领域知识建模和多轮交互推理，在五个垂直行业中有效区分模型的领域知识和推理能力。

**[Hallulens Llm Hallucination Benchmark](hallulens_llm_hallucination_benchmark.md)**

:   提出了 HalluLens 幻觉基准，明确区分幻觉与事实性，建立了外在幻觉（与训练数据不一致）和内在幻觉（与输入上下文不一致）的清晰分类体系，引入三个动态可重生成的外在幻觉评估任务，并全面分析了现有基准的局限性。

**[Hellaswag-Pro A Large-Scale Bilingual Benchmark For Evaluating The Robustness Of](hellaswag-pro_a_large-scale_bilingual_benchmark_for_evaluating_the_robustness_of.md)**

:   构建首个大规模双语（中英）LLM 常识推理鲁棒性评估基准 HellaSwag-Pro，包含 7 种问题变体共 11,200 道题，系统评估 41 个 LLM 发现所有模型在常识推理上远未达到鲁棒。

**[Help Write Story Feedback](help_write_story_feedback.md)**

:   探索 LLM 能否为创意写作者提供有意义的写作反馈——构建包含 1300 个故意引入写作问题的故事测试集，评估常用 LLM 的写作反馈生成能力，发现模型虽能提供具体且多数准确的反馈，但常错过最重要的写作问题且不会恰当地在批评和鼓励之间切换。

**[Hpss Heuristic Prompting Strategy Search For Llm Evaluators](hpss_heuristic_prompting_strategy_search_for_llm_evaluators.md)**

:   整合 8 个影响 LLM 评估提示效果的关键因子（评分尺度、ICL 示例、评估标准、参考答案、CoT、AutoCoT、度量指标、组件顺序），提出基于遗传算法的启发式提示策略搜索方法 HPSS，在 12,960 种组合空间中高效找到最优提示策略，仅用基线 5% 的生成成本即超越 G-Eval 和 CloserLook。

**[Justrank Llm Judge System Ranking](justrank_llm_judge_system_ranking.md)**

:   首次大规模研究LLM判官在系统排名任务中的表现，提出JuStRank基准，揭示实例级判断能力与系统级排名能力之间的差距，并发现判官的"果断性"和"偏见"两个新兴特征。

**[Kitab-Bench A Comprehensive Multi-Domain Benchmark For Arabic Ocr And Document U](kitab-bench_a_comprehensive_multi-domain_benchmark_for_arabic_ocr_and_document_u.md)**

:   KITAB-Bench 是一个涵盖 9 大领域 36 个子领域共 8,809 个样本的综合性阿拉伯语 OCR 基准，评估结果显示现代视觉语言模型（如 GPT-4o、Gemini）在字符错误率上平均超过传统 OCR 方法 60%，但在 PDF-to-Markdown 转换中最优模型仅达到 65% 准确率，凸显了阿拉伯语文档理解的巨大挑战。

**[La Leaderboard Spanish](la_leaderboard_spanish.md)**

:   构建首个面向西班牙和拉丁美洲语言的开源LLM排行榜，整合66个数据集覆盖西班牙语、加泰罗尼亚语、巴斯克语、加利西亚语，评估50个模型并分析训练策略、算力与性能的关系。

**[Language Complexity Measurement as a Noisy Zero-Shot Proxy for Evaluating LLM Performance](language_complexity_measurement_as_a_noisy_zero-shot_proxy_for_evaluating_llm_pe.md)**

:   探索语言复杂度指标作为 LLM 性能的零样本代理评估，发现文本复杂度与 LLM 表现负相关但噪声大，仅可作为粗略参考。

**[Language Model Probabilities Are Not Calibrated In Numeric Contexts](language_model_probabilities_are_not_calibrated_in_numeric_contexts.md)**

:   系统研究了语言模型在数值上下文中的概率校准问题，发现即使在简单场景（如从袋中取弹珠）下，包括 GPT-4o 在内的所有测试模型均严重校准不良，存在基于词序、词频和词标识的系统性偏差（如某些模型总选第一个选项，其他模型总选第二个），指令微调加剧了模式崩塌。

**[Mars Benchmarking The Metaphysical Reasoning Abilities Of Language Models With A](mars_benchmarking_the_metaphysical_reasoning_abilities_of_language_models_with_a.md)**

:   本文提出了 **Metaphysical Reasoning（形而上推理）** 的形式化定义，将分布变化下的推理分解为三步判别过程，并构建了首个大规模评估基准 Mars（355K 标注数据），实验表明 20+ 语言模型在该任务上表现均不理想，揭示了 LLM 在理解事件组成要素变化及其因果效应方面的显著短板。

**[Mcbe A Multi-Task Chinese Bias Evaluation Benchmark For Large Language Models](mcbe_a_multi-task_chinese_bias_evaluation_benchmark_for_large_language_models.md)**

:   提出首个多任务中文偏见评估基准 McBE，包含 4,077 条偏见评估实例（BEI），覆盖 12 种偏见类别和 82 个子类别，通过 5 种评估任务（偏好计算/子类别分类/场景选择/偏见分析/偏见评分）多角度量化 LLM 中的中文偏见，并揭示"参数越大偏见越强"的传统结论可能源于单任务评估的局限性。

**[Mdbench A Synthetic Multi-Document Reasoning Benchmark Generated With Knowledge ](mdbench_a_synthetic_multi-document_reasoning_benchmark_generated_with_knowledge_.md)**

:   提出 MDBench，一个通过「结构化知识→LLM 辅助增强→自然文本生成」管线合成的多文档推理 QA 基准，可控地注入跨文档依赖，对前沿 LLM 构成显著挑战（最佳模型 EM 仅~60%）。

**[Mis-Prompt Benchmarking Large Language Models For Proactive Error Handling](mis-prompt_benchmarking_large_language_models_for_proactive_error_handling.md)**

:   提出 Mis-prompt 基准，包含 4 项评估任务、14 类错误分类体系和 14,969 条数据集，系统研究 LLM 在无显式错误处理指令时的**主动**纠错能力，发现当前 LLM 主动纠错能力严重不足，SFT 可显著提升。

**[Mmlu-Cf A Contamination-Free Multi-Task Language Understanding Benchmark](mmlu-cf_a_contamination-free_multi-task_language_understanding_benchmark.md)**

:   提出 MMLU-CF，一个包含 20,000 道题的无数据污染多任务语言理解基准，通过从更广泛的来源收集数据并应用三条去污染规则（改写题目、打乱选项、随机替换选项）来避免无意和恶意的数据泄露，最强模型 GPT-4o 在该基准上仅获得 73.4%（MMLU 上为 88.0%）。

**[Movie101V2 Improved Movie Narration Benchmark](movie101v2_improved_movie_narration_benchmark.md)**

:   提出 Movie101v2，一个包含 203 部电影、46K 双语（中英文）视频-叙事对的大规模电影叙事基准，将自动电影叙事任务分解为三个渐进式目标（视觉事实描述 L1 → 情节叙述 L2 → 可部署 AD L3），并基于 LLM 提出新的评估框架，全面基线测试了包括 GPT-4V 在内的多种视觉语言模型。

**[Navigating Rifts In Human-Llm Grounding Study And Benchmark](navigating_rifts_in_human-llm_grounding_study_and_benchmark.md)**

:   系统研究人与 LLM 对话中的 grounding（建立共识）失败问题，发现 LLM 主动澄清的频率仅为人类的 1/3、主动追问的频率仅为 1/16，提出 Rifts 基准（约 1.8K 任务）评测 LLM 的 grounding 能力，并通过 grounding forecaster 实现初步干预。

**[Onebench To Test Them All Sample-Level Benchmarking Over Open-Ended Capabilities](onebench_to_test_them_all_sample-level_benchmarking_over_open-ended_capabilities.md)**

:   ONEBench提出了一种新的基准评测范式：将多个评测数据集的样本合并为统一数据池，通过Plackett-Luce排名聚合算法在样本级别进行模型比较，支持异构指标聚合、不完整数据处理和个性化能力探测。

**[Pap2Pat Benchmarking Outline-Guided Long-Text Patent Generation With Patent-Pape](pap2pat_benchmarking_outline-guided_long-text_patent_generation_with_patent-pape.md)**

:   构建了包含 1.8k 专利-论文配对的 Pap2Pat 基准，提出基于大纲的分块专利描述生成方法 COPGen，并设计了基于 NLI 的事实性/覆盖率/风格评估指标，系统评测了当前 LLM 在超长专利文档生成上的能力与不足。

**[Papersplease A Benchmark For Evaluating Motivational Values Of Large Language Mo](papersplease_a_benchmark_for_evaluating_motivational_values_of_large_language_mo.md)**

:   基于 Alderfer ERG 需求理论构建 3700 个道德困境场景（移民检查官角色扮演），评估 6 个 LLM 的动机价值偏好，发现 Claude 拒绝所有场景、GPT-4o-mini 对生存需求 99% 满足但对关系需求仅 47%，且模型对穆斯林/边缘化群体存在显著的隐性社会偏见。

**[Patch Psychometrics-Assisted Benchmarking Of Large Language Models Against Human](patch_psychometrics-assisted_benchmarking_of_large_language_models_against_human.md)**

:   提出 PATCH 框架，将心理测量学中的项目反应理论（IRT 3PL/2PL 模型）引入 LLM 基准测试，在 TIMSS 2011 八年级数学测试（88 道题、56 个国家/地区）上对比 GPT-4V、Gemini-Pro-Vision、Qwen-VL 与人类群体的能力值，发现 IRT 能力估计与简单准确率排名显著不同，GPT-4V 与韩国/新加坡/中国台北学生处于同一排名区间；同时发布 4 个高质量数据集（TIMSS 2011 & 2008 数学/科学/物理）。

**[Physreason A Comprehensive Benchmark Towards Physics-Based Reasoning](physreason_a_comprehensive_benchmark_towards_physics-based_reasoning.md)**

:   提出 PhysReason 基准，包含 1200 道物理题（平均 8.1 步解题），设计了答案级和步骤级两层自动评估框架 PSAS，揭示顶尖模型（Deepseek-R1、o3-mini）在物理推理上准确率不足 60%，并识别出四大推理瓶颈。

**[Readoc A Unified Benchmark For Realistic Document Structured Extraction](readoc_a_unified_benchmark_for_realistic_document_structured_extraction.md)**

:   READoc 提出了首个将文档结构化提取（DSE）定义为端到端 PDF 到 Markdown 转换的统一基准，包含 3,576 篇来自 arXiv/GitHub/Zenodo 的真实文档和三模块评估套件（标准化+分割+评分），首次揭示了当前 DSE 系统与真实场景需求之间的差距。

**[Realhitbench A Comprehensive Realistic Hierarchical Table Benchmark For Evaluati](realhitbench_a_comprehensive_realistic_hierarchical_table_benchmark_for_evaluati.md)**

:   提出 RealHiTBench——首个全面评估 LLM 对复杂层次化表格理解能力的基准，包含 708 张来自 13 个平台、24 个领域的真实复杂表格和 3,752 道题目，定义了 5 种复杂结构类型和 5 大任务类型，并提出基于树结构的 TreeThinker 推理管线显著提升模型对层次化表头的理解能力。

**[Retrieval Models Arent Tool-Savvy Benchmarking Tool Retrieval For Large Language](retrieval_models_arent_tool-savvy_benchmarking_tool_retrieval_for_large_language.md)**

:   提出 ToolRet——首个大规模工具检索基准（7.6k 任务 + 43k 工具语料库），系统评估了现有 IR 模型在工具检索场景下的表现，发现即使强力检索器也表现不佳，并贡献了超过 200k 训练实例显著提升检索质量。

**[Revisiting 3D Llm Benchmarks Are We Really Testing 3D Capabilities](revisiting_3d_llm_benchmarks_are_we_really_testing_3d_capabilities.md)**

:   揭示了 3D LLM 评测中的"2D-Cheating"问题——将点云渲染为图像后，2D VLM 在部分基准上超越 3D SOTA，说明这些基准未能有效评估真正的 3D 理解能力，并据此提出了有效 3D 评测的设计原则。

**[Right Answer Wrong Score Uncovering The Inconsistencies Of Llm Evaluation In Mul](right_answer_wrong_score_uncovering_the_inconsistencies_of_llm_evaluation_in_mul.md)**

:   系统揭示了LLM在多选问答(MCQA)评估中的不一致性——不同评估策略(RegEx/Logprobs/xFinder)和提示设置(约束/自由生成)组合会导致模型性能报告产生显著差异，且即使是SOTA的LLM-based答案提取器也无法可靠识别推理矛盾，呼吁建立标准化评估协议。

**[Rulearena Rule Guided Reasoning](rulearena_rule_guided_reasoning.md)**

:   提出 RuleArena——一个基于航空行李费、NBA交易规则、税务法规三个真实场景的benchmark，用于评估LLM遵循复杂自然语言规则进行推理的能力；实验发现即使最强模型（o1-preview）在最难任务上准确率也不足50%，暴露了LLM在规则召回、规则区分和数学计算三方面的系统性缺陷。

**[Sanskriti A Comprehensive Benchmark For Evaluating Language Models Knowledge Of ](sanskriti_a_comprehensive_benchmark_for_evaluating_language_models_knowledge_of_.md)**

:   提出 SANSKRITI——一个包含 21,853 个问答对、覆盖印度全部 28 个邦和 8 个联邦属地、涵盖 16 类文化属性的大规模基准数据集，用于评估语言模型对印度文化多样性的理解程度。

**[Seedbench A Multi-Task Benchmark For Evaluating Large Language Models In Seed Sc](seedbench_a_multi-task_benchmark_for_evaluating_large_language_models_in_seed_sc.md)**

:   提出 SeedBench——首个面向种子科学（种子育种）的多任务 LLM 评测基准，包含 2,264 道专家验证题目，覆盖基因信息检索、基因功能调控和品种选育三大育种流程，对 26 个 LLM 进行系统评估，揭示了当前 LLM 与真实育种需求之间的显著差距。

**[Somethings Fishy In The Data Lake A Critical Re-Evaluation Of Table Union Search](somethings_fishy_in_the_data_lake_a_critical_re-evaluation_of_table_union_search.md)**

:   系统性分析了主流表联合搜索 (Table Union Search, TUS) 基准测试的三大结构性缺陷——过度重叠、语义简单、真值噪声，揭示简单的词袋 (BoW) 和预训练嵌入基线就能在这些基准上达到或超越复杂 SOTA 方法的效果，调研结论指出当前基准无法有效评估语义理解能力。

**[Structext Eval](structext_eval.md)**

:   提出StrucText-Eval——一个覆盖8种结构化语言（JSON/YAML/XML/Markdown/LaTeX/Org/CSV/Tree）和29个任务的自动生成评测基准，共5,800个样本，通过可控的嵌套深度和结构宽度调节难度。实验揭示开源LLM在标准集最高仅74.9%准确率，困难集降至45.8%，而人类在困难集达92.6%，暴露了LLM在复杂结构推理上的严重不足。

**[Structflowbench A Structured Flow Benchmark For Multi-Turn Instruction Following](structflowbench_a_structured_flow_benchmark_for_multi-turn_instruction_following.md)**

:   提出 StructFlowBench，一个融入结构流建模的多轮指令遵循基准测试，定义了六种基本的轮间关系（跟进、精炼、回忆、总结、扩展、不相关），建立了双层约束评估体系（轮内约束 + 轮间结构约束），系统评估了 13 个主流 LLM 在多轮对话结构理解上的能力。

**[Towards Dynamic Theory Of Mind Evaluating Llm Adaptation To Temporal Evolution O](towards_dynamic_theory_of_mind_evaluating_llm_adaptation_to_temporal_evolution_o.md)**

:   提出 DynToM 基准，通过 1,100 个社会情境中 5,500 个时序关联场景和 78,100 道题目，评估 LLM 追踪人类心理状态时序演化的能力，揭示模型平均落后人类 44.7%。

**[Towards Objective Fine-Tuning How Llms Prior Knowledge Causes Potential Poor Cal](towards_objective_fine-tuning_how_llms_prior_knowledge_causes_potential_poor_cal.md)**

:   揭示LLM的先验知识在微调过程中会导致校准退化（已知数据引发过度自信，未知数据反而有利于校准），提出CogCalib认知感知校准框架，在训练中根据知识偏差动态应用不同学习策略，在保持任务性能的同时平均降低57%的ECE。

**[Triptailor A Real-World Benchmark For Personalized Travel Planning](triptailor_a_real-world_benchmark_for_personalized_travel_planning.md)**

:   提出 TripTailor，一个基于真实数据的大规模旅行规划 benchmark，包含 40 个城市的 50 万+ POI 和近 4000 条真实行程，并引入可行性、合理性和个性化三维评估框架，发现最先进 LLM 生成的行程不到 10% 能达到人类水平。

**[Tumlu A Unified And Native Language Understanding Benchmark For Turkic Languages](tumlu_a_unified_and_native_language_understanding_benchmark_for_turkic_languages.md)**

:   提出 TUMLU 和 TUMLU-mini，首个面向突厥语系（9 种语言）的原生语言理解基准，包含 38139 道中高中学科的多选题，覆盖拉丁、西里尔和阿拉伯三种文字系统，为低资源语言的 LLM 评估提供了高质量的原生基准。

**[Vital Pluralistic Alignment Healthcare](vital_pluralistic_alignment_healthcare.md)**

:   本文构建了首个面向医疗健康领域的多元化对齐（pluralistic alignment）基准数据集 VITAL，包含 13.1K 价值观情境和 5.4K 多选题，并通过对 8 个 LLM 的广泛评估表明，现有多元化对齐技术（尤其是 ModPlural）在医疗场景下表现不佳，简单的 prompting 反而效果更好。

**[Voxeval Benchmarking The Knowledge Understanding Capabilities Of End-To-End Spok](voxeval_benchmarking_the_knowledge_understanding_capabilities_of_end-to-end_spok.md)**

:   提出 VoxEval，首个支持端到端纯语音输入-输出评估的 SpeechQA 基准，涵盖 56 个学科、26 种输入音频条件，系统揭示了当前端到端语音大模型在知识理解和数学推理方面的严重不足。

**[Wicked A Simple Method To Make Multiple Choice Benchmarks More Challenging](wicked_a_simple_method_to_make_multiple_choice_benchmarks_more_challenging.md)**

:   提出 WiCkeD 方法，通过随机将多选题的一个选项替换为"以上都不对"来增加现有基准难度，使18个 LLM 的平均性能下降12.1个百分点，且链式思维推理也无法弥补这一下降。

**[Wximpactbench A Disruptive Weather Impact Understanding Benchmark For Evaluating](wximpactbench_a_disruptive_weather_impact_understanding_benchmark_for_evaluating.md)**

:   提出 WXImpactBench，首个评估 LLM 理解极端天气社会影响的基准，包含经过 4 阶段管线处理的高质量历史报纸数据集和两个评估任务（多标签分类和排序问答）。

**[Yescieval Llm Judge Science](yescieval_llm_judge_science.md)**

:   提出YESciEval框架，结合九维细粒度评估准则和SFT+RL对齐策略来缓解LLM评估者的乐观偏差(optimism bias)，在科学问答场景下构建鲁棒的开源LLM-as-a-Judge系统，无需人类标注和闭源模型。
