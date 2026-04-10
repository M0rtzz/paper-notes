<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**💬 ACL2025** · 共 **104** 篇

**[AdamMeme: Adaptively Probe the Reasoning Capacity of Multimodal Large Language Models on Harmfulness](adammeme_adaptively_probe_the_reasoning_capacity_of_multimodal_large_language_mo.md)**

:   提出AdamMeme——一个基于多智能体协作的自适应评估框架，通过迭代生成更具挑战性的meme样本来探测多模态大语言模型(mLLM)在有害内容理解上的推理能力和特定弱点。

**[Adaptive Linguistic Prompting (ALP) Enhances Phishing Webpage Detection in Multimodal Large Language Models](adaptive_linguistic_prompting_alp_enhances_phishing_webpage_detection_in_multimo.md)**

:   提出 Adaptive Linguistic Prompting (ALP)，一种 8-shot 结构化提示方法，引导多模态 LLM 从 HTML 文本、截图和 URL 三个维度联合推理，检测钓鱼网页，在 GPT-4o 上组合分析达到 F1=0.93，超过传统零样本基线。

**[Can LLMs Deceive CLIP? Benchmarking Adversarial Compositionality of Pre-trained Multimodal Representation via Text Updates](adversarial_compositionality_clip.md)**

:   提出MAC基准和diversity-promoting自训练方法，通过让LLM生成欺骗性文本来系统暴露CLIP等预训练多模态表征的组合性漏洞，在图像/视频/音频三个模态上均显著超越已有方法。

**[Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents](agent_rewardbench.md)**

:   Agent-RewardBench 提出了首个面向多模态 Agent 的奖励建模评测基准，覆盖感知/规划/安全 3 个维度、7 个真实场景、1136 个高质量样本，实验发现即使 GPT-4o 也仅达 61.4% 准确率，揭示了 Agent 奖励建模的巨大挑战。

**[AkaCE: A Multimodal Multi-party Dataset for Emotion Recognition in Movie Dialogues](akan_cinematic_emotions_ace_a_multimodal_multi-party_dataset_for_emotion_recogni.md)**

:   构建 AkaCE——首个非洲语言多模态对话情感识别数据集，覆盖阿坎语（加纳主要语言，约 2000 万使用者），含 385 段对话 6162 条发言（音频+视觉+文本三模态）、308 名说话人（性别平衡 155男/153女），并提供首个非洲语言词级韵律突出标注。

**[Aligning VLM Assistants with Personalized Situated Cognition](aligning_vlm_assistants_with_personalized_situated.md)**

:   基于社会学"角色集合"(Role-Set) 概念刻画用户多样性，提出 PCogAlign 框架，通过认知感知的动作导向奖励模型来为 VLM 助手生成个性化回复，使不同角色的用户在相同视觉场景下获得最适合自身需求的建议。

**[AlignMMBench: Evaluating Chinese Multimodal Alignment in Large Vision-Language Models](alignmmbench_evaluating_chinese_multimodal_alignment_in_large_vision-language_mo.md)**

:   提出 AlignMMBench，首个面向中文视觉上下文的多模态对齐评测基准，涵盖 3 大类 13 项任务、1054 张图像和 4978 个 QA 对（含单轮/多轮对话），并训练了基于 ChatGLM3-6B 的评估器 CritiqueVLM，其评估一致性超过 GPT-4。

**[Aria-UI: Visual Grounding for GUI Instructions](aria-ui_visual_grounding_for_gui_instructions.md)**

:   提出 Aria-UI，一个专为 GUI 视觉定位设计的纯视觉多模态模型，通过可扩展的指令合成数据管线和文本-图像交错的动作历史机制，在离线和在线 Agent 基准上均达到 SOTA，包括 AndroidWorld 第1名（44.8%）和 OSWorld 第3名（15.2%）。

**[Attacking Vision-Language Computer Agents via Pop-ups](attacking_vl_agents_popups.md)**

:   系统性设计了一套对抗性弹窗攻击方法来攻击基于视觉语言模型的计算机操控 agent，在 OSWorld 和 VisualWebArena 上平均攻击成功率达 86%，任务成功率下降 47%，基础防御手段几乎无效。

**[AVG-LLaVA: An Efficient Large Multimodal Model with Adaptive Visual Granularity](avg-llava_an_efficient_large_multimodal_model_with_adaptive_visual_granularity.md)**

:   提出 AVG-LLaVA——在 LLaVA-NeXT 基础上引入视觉粒度缩放器（多级池化获取不同粒度视觉 token）+ 视觉粒度路由器（基于图像和指令自适应选择最合适粒度），并提出 RGLF 训练范式将路由器预测与 LMM 偏好对齐。在 11 个基准上实现更好性能同时大幅减少视觉 token（如 AI2D 上减少 85.3%，推理加速 2.53×）。

**[Enhancing Multimodal Continual Instruction Tuning with BranchLoRA](branchlora_continual_instruction.md)**

:   发现MoELoRA在多模态持续指令微调(MCIT)中存在参数低效——矩阵A跨任务趋同而B保持区分，提出BranchLoRA：共享一个A矩阵（树干）+ 多个专有B矩阵（树枝） + 灵活调参-冻结机制 + 任务特定路由器，在CoIN benchmark上显著超越MoELoRA，有效缓解灾难性遗忘。

**[Burn After Reading: Do Multimodal Large Language Models Truly Capture Order of Events in Image Sequences?](burn_after_reading_do_multimodal_large_language_models_truly_capture_order_of_ev.md)**

:   提出 TempVS 基准测试，系统评估 38 个 MLLM 在图像序列中对多事件时序关系的 grounding 和推理能力，揭示 SOTA 模型与人类之间存在巨大性能差距。

**[Can Vision Language Models Understand Mimed Actions?](can_vision_language_models_understand_mimed_actions.md)**

:   构建 Mime 基准（86 个动作、860 个样本），利用动作捕捉 + 3D 渲染系统化评估 VLM 对哑剧动作的理解能力，发现 VLM 严重依赖场景上下文而无法像人类一样从纯肢体动作推断语义。

**[MMSafeAware: Can't See the Forest for the Trees: Benchmarking Multimodal Safety Awareness for Multimodal LLMs](cant_see_the_forest_for_the.md)**

:   提出 MMSafeAware，首个同时评估"不安全内容识别"和"过度敏感"的多模态安全意识基准，包含 1,500 个跨 29 种安全场景的图文对，评估 9 个 MLLM 发现所有模型都存在安全与有用性的严重权衡——GPT-4V 将 36.1% 的不安全输入误判为安全，同时将 59.9% 的安全输入误判为不安全；三种改进方法均无法根本解决问题。

**[Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model](centurio_multilingual_vlm.md)**

:   系统研究多语言LVLM训练策略，发现可以同时支持100种语言、只需25-50%非英文数据即可大幅提升多语言性能且不损英语性能，最终训练的Centurio在14个任务56种语言上达到SOTA。

**[ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](chartcoder_chart_to_code.md)**

:   提出首个专用chart-to-code MLLM（ChartCoder），以Code LLM为语言骨干+160K大规模图表-代码数据集+Snippet-of-Thought逐步推理方法，7B模型在三个基准上超越所有开源MLLM，接近GPT-4o水平。

**[Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation](code_guided_text_rich_image.md)**

:   提出CoSyn框架，利用纯文本LLM的代码生成能力自动创建40万张文本丰富图像（图表、文档、图表等）+270万条指令微调数据，训练的7B VLM在7个基准上达到SOTA，超越GPT-4V和Gemini 1.5 Flash。

**[COLING-UniA at SciVQA 2025: Few-Shot Example Retrieval and Confidence-Informed Ensembling for Multimodal Large Language Models](coling-unia_at_scivqa_2025_few-shot_example_retrieval_and_confidence-informed_en.md)**

:   本文提出了一种基于多模态大模型（MLLM）集成的科学图表视觉问答系统，通过 few-shot 示例检索策略和置信度感知的模型选择机制，在 SciVQA 2025 共享任务中获得第三名（平均 F1 = 85.12）。

**[Insight Over Sight: Exploring the Vision-Knowledge Conflicts in Multimodal LLMs](conflictvis_vision_knowledge_conflict.md)**

:   首次系统探索 MLLM 中常识级别的视觉-知识冲突问题，提出自动化框架构建 ConflictVis 基准（374 图 + 1122 QA），发现 MLLM 在约 20% 的冲突场景中过度依赖参数化知识（尤其是 Yes-No 和动作类问题），并提出 Focus-on-Vision 提示策略进行缓解。

**[CoRe-MMRAG: Cross-Source Knowledge Reconciliation for Multimodal RAG](core_mmrag_knowledge_reconciliation.md)**

:   CoRe-MMRAG 提出了一个端到端多模态 RAG 框架，通过四阶段流水线（参数知识生成→视觉-文本联合重排序→外部知识生成→内外知识整合）解决参数知识-检索知识不一致(PRKI)和视觉-文本知识不一致(VTKI)两个问题，在 InfoSeek 和 Encyclopedic-VQA 上分别提升 5.6% 和 9.3%。

**[COSMMIC: Comment-Sensitive Multimodal Multilingual Indian Corpus for Summarization and Headline Generation](cosmmic_commentsensitive_multimodal_multilingual_indian_corpus.md)**

:   构建首个面向印度语言的评论感知多模态多语言数据集 COSMMIC（9 种语言、4,959 篇文章-图像对、24,484 条读者评论），提出评论过滤（IndicBERT）和图像分类（CLIP）增强方案，用 GPT-4 和 LLama3 建立摘要和标题生成的基准。

**[CoSyn: Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation](cosyn_code_guided_synthetic_data.md)**

:   提出 CoSyn 框架，利用纯文本 LLM 的代码生成能力自动合成多样化的文本丰富型图像及对应指令微调数据，构建 400K 图像 + 2.7M 指令数据集，在 7 个 benchmark 上达到开源 SOTA 并超越 GPT-4V。

**[Cracking the Code of Hallucination in LVLMs with Vision-aware Head Divergence](cracking_hallucination_vhd.md)**

:   提出Vision-aware Head Divergence (VHD)指标量化注意力头对视觉信息的敏感度，发现幻觉与模型过度依赖语言先验紧密相关，并提出Vision-aware Head Reinforcement (VHR)无训练方法，通过放大视觉敏感注意力头来缓解幻觉，在CHAIR上最高降低CHAIRS 16.36个点。

**[DALR: Dual-level Alignment Learning for Multimodal Sentence Representation Learning](dalr_dual-level_alignment_learning_for_multimodal_sentence_representation_learni.md)**

:   提出 DALR 框架，通过跨模态一致性学习 + 模态内排序蒸馏的双层对齐策略，解决多模态句子表示中的跨模态不对齐偏差（CMB）和模态内语义分歧（ISD）问题，在 STS 和 TR 任务上取得 SOTA。

**[Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation](do_vision-language_models_have_internal_world_models_towards_an_atomic_evaluatio.md)**

:   提出基于认知科学的双阶段框架（感知+预测），构建 WM-ABench 大规模基准（23 维度、6 模拟器、10 万+实例），通过 660 组实验系统揭示 15 个 SOTA VLM 在基本世界建模能力上的严重不足。

**[Donate or Create? Comparing Data Collection Strategies for Emotion-labeled Multimodal Social Media Posts](donate_or_create_comparing_data_collection.md)**

:   系统比较了两种情感标注数据的收集策略——"捐赠"真实社交媒体帖子 vs "创造"帖子——发现创造的帖子更长、更依赖文本、偏向原型化情感事件，但用创造数据训练的模型可以很好泛化到真实数据，只是需要真实数据来做靠谱的效果评估。

**[Don't Miss the Forest for the Trees: Attentional Vision Calibration for Large Vision Language Models](dont_miss_the_forest_for_the_trees_attentional_vision_calibration_for_large_visi.md)**

:   发现 LVLM 中存在"blind token"现象——少量语义无关的图像 token 吸引了不成比例的注意力权重，并提出 AvisC 方法通过测试时对比解码重新校准 blind token 影响，有效减轻视觉幻觉。

**[EffiVLM-Bench: A Comprehensive Benchmark for Evaluating Training-Free Acceleration in Large Vision-Language Models](effivlm_bench_acceleration.md)**

:   提出 EffiVLM-Bench，首个系统评估大型视觉语言模型（LVLM）训练免加速方法的统一框架，覆盖 17 个 benchmark、3 个前沿模型，引入泛化性和忠诚度等新指标，揭示了 token 压缩与参数压缩在不同场景下的性能-效率权衡。

**[EffiVLM-Bench: 大型视觉语言模型免训练加速的综合评测基准](effivlm_bench_vlm_acceleration.md)**

:   提出 EffiVLM-Bench，一个统一评估框架，系统性地评估大型视觉语言模型(LVLM)的免训练加速方法，涵盖 token 压缩和参数压缩两大类，从性能、泛化性、忠实度和效率四个维度进行全面对比分析。

**[Enabling Chatbots with Eyes and Ears: An Immersive Multimodal Conversation System](enabling_chatbots_with_eyes_and_ears_an_immersive_multimodal_conversation_system.md)**

:   本文提出赋予聊天机器人"眼睛和耳朵"的沉浸式多模态对话系统，构建了融合视觉与听觉的多会话多方对话数据集 M3C，并设计了包含对话模块和多模态记忆检索模块的对话模型，实现了多说话者共享视听体验的动态长期对话。

**[Enhance Multimodal Consistency and Coherence for Text-Image Plan Generation](enhance_multimodal_consistency_and_coherence_for_text-image_plan_generation.md)**

:   本文提出一种自回归文本-图像计划生成框架（MPlanner），通过四阶段迭代——文本草拟、图像编辑、视觉信息提取、文本精炼——有效提升多模态计划中视觉步骤的连贯性和文本-图像的一致性。

**[Evaluating Visual and Cultural Interpretation: The K-Viscuit Benchmark with Human-VLM Collaboration](evaluating_visual_and_cultural_interpretation_the_k-viscuit_benchmark_with_human.md)**

:   本文提出了一种半自动化的文化 VLM 基准构建框架，通过人-VLM 协作生成多选 VQA 样本，并以此构建了聚焦韩国文化的 K-Viscuit 数据集（657 题），揭示了开源与闭源 VLM 在文化理解上的显著差距。

**[EXPERT: An Explainable Image Captioning Evaluation Metric with Structured Explanations](expert_an_explainable_image_captioning_evaluation_metric_with_structured_explana.md)**

:   本文提出 EXPERT，一种基于 VLM 微调的无参考图像描述评估指标，通过构建大规模结构化解释数据集并设计两阶段评估模板，在多个基准数据集上达到 SOTA 的同时，提供基于流畅度、相关性、描述性三个维度的高质量结构化解释。

**[Exploring How Generative MLLMs Perceive More Than CLIP with the Same Vision Encoder](exploring_how_generative_mllms_perceive_more.md)**

:   系统探究为何生成式多模态LLM（如LLaVA）使用与CLIP相同的视觉编码器却能在视觉推理任务上大幅超越CLIP，发现patch token、位置编码和prompt加权是关键因素。

**[Exploring Multimodal Challenges in Toxic Chinese Detection: Taxonomy, Benchmark, and Findings](exploring_multimodal_challenges_in_toxic_chinese_detection_taxonomy_benchmark_an.md)**

:   这篇工作把中文毒性文本中的“形、音、义混合扰动”系统化为 3 类 8 种策略，构建了大规模扰动基准 CNTP，并证明当前中美主流 LLM 在这类中文多模态毒性检测上都明显不稳，而小样本 ICL / SFT 虽能抬高检出率，却容易把正常内容一起误杀。

**[FIHA: Autonomous Fine-grained Hallucination Evaluation in Vision-Language Models with Davidson Scene Graphs](fiha_autonomous_hallucination_evaluation_in_vision-language_models_with_davidson.md)**

:   本文提出 FIHA，一个无需 LLM 和人工标注的自动化细粒度幻觉评估框架，通过从图像和描述中提取实体、属性和关系生成 Q&A 对，并引入 Davidson 场景图（DSG）建模问题间的依赖关系，构建了 FIHA-v1 基准，全面评估了主流大视觉语言模型的幻觉水平。

**[Filter-And-Refine: A MLLM Based Cascade System for Industrial-Scale Video Content Moderation](filter-and-refine_a_mllm_based_cascade_system_for_industrial-scale_video_content.md)**

:   TikTok提出一种基于MLLM的两阶段级联内容审核系统（Router-Ranker），通过轻量级嵌入检索路由器过滤97.5%的合规流量，仅将高风险视频送入微调后的LLaVA进行精细分类，F1提升66.5%的同时部署成本降至直接全量部署的1.5%。

**[FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](finmme_benchmark_dataset_for_financial_multi-modal_reasoning_evaluation.md)**

:   构建了一个包含 11,000+ 高质量金融多模态样本的评估基准 FinMME，涵盖 18 个金融领域和 10 种图表类型，提出了融合幻觉惩罚和领域归一化的 FinScore 评估体系，实验表明即使 GPT-4o 也仅得 47 分，揭示了 MLLM 在金融领域的显著不足。

**[FlagEvalMM: A Flexible Framework for Comprehensive Multimodal Model Evaluation](flagevalmm_a_flexible_framework_for_comprehensive_multimodal_model_evaluation.md)**

:   提出 FlagEvalMM，一个开源的多模态模型评估框架，通过将模型推理与评估过程解耦的架构设计，统一支持视觉语言理解（VQA）、文生图/文生视频生成和图文检索等多种多模态任务的评估。

**[Harnessing PDF Data for Improving Japanese Large Multimodal Models](harnessing_pdf_data_for_improving_japanese_large_multimodal_models.md)**

:   提出一套全自动 PDF 数据提取管道，从日语 PDF 中提取图文对并生成指令数据，通过持续微调 LLaVA1.5 框架显著提升日语多模态模型性能，在 Heron-Bench 上实现 2.1%~13.8% 的提升。

**[HiDe-LLaVA: Hierarchical Decoupling for Continual Instruction Tuning of Multimodal Large Language Model](hidellava_hierarchical_decoupling_for_continual_instruction.md)**

:   通过 CKA 分析发现 MLLM 顶层学任务特异信息而其余层学通用知识，提出 HiDe-LLaVA：顶层 LoRA 做 MoE 式任务特异扩展（双模态锚点匹配）+ 其余层 LoRA 做均匀融合，在新构建的无信息泄露基准 UCIT 上比最佳基线提升 5.8%。

**[Hierarchical Safety Realignment: Lightweight Restoration of Safety in Pruned Large Vision-Language Models](hierarchical_safety_realignment_lightweight_restoration_of_safety_in_pruned_larg.md)**

:   提出层次化安全重对齐方法HSR，通过先识别安全关键注意力头、再在这些头中定位并恢复被剪枝的安全关键神经元，以极低参数开销（万分之几）显著恢复被剪枝LVLM丢失的安全性能。

**[HotelMatch-LLM: Joint Multi-Task Training of Small and Large Language Models for Efficient Multimodal Hotel Retrieval](hotelmatch_llm_retrieval.md)**

:   提出 HotelMatch-LLM，用 SLM 编码 query + LLM 编码酒店文档的非对称架构，配合三目标多任务优化（检索对齐 + MLM地理预测 + 视觉设施识别）和 patch 级 mean pooling 多图处理，在旅行领域多模态检索任务上显著超过 MARVEL/VISTA 等 SOTA。

**[Inference Compute-Optimal Video Vision Language Models](inference_compute_optimal_video_vlm.md)**

:   首次系统研究视频VLM推理时的计算预算最优分配问题：在固定推理FLOPs下，如何在语言模型大小(x_N)、帧数(x_T)和每帧视觉token数(x_V)三个维度间做最优权衡，通过大规模训练扫描（~100k A100小时）和参数化建模得出实用的分配策略。

**[InternLM-XComposer2.5-Reward: A Simple Yet Effective Multi-Modal Reward Model](internlm-xcomposer25-reward_a_simple_yet_effective_multi-modal_reward_model.md)**

:   基于InternLM-XComposer2.5构建判别式多模态奖励模型IXC-2.5-Reward，通过精心构建跨文本/图像/视频的多领域偏好数据集训练，在多模态奖励基准VL-RewardBench上以70.0% Macro Acc超越GPT-4o（62.4%），并展示了RL训练、Best-of-N测试时缩放和数据清洗三大应用。

**[JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games](jarvis-vla_post-training_large-scale_vision_language_models_to_play_visual_games.md)**

:   提出ActVLP训练范式，在动作模仿学习之前增加视觉语言后训练阶段（世界知识、视觉对齐、空间定位），构建首个能在Minecraft中执行1000+原子任务的VLA模型JARVIS-VLA，相比最佳基线提升40%。

**[Judging the Judges: Can Large Vision-Language Models Fairly Evaluate Chart Comprehension and Reasoning?](judging_the_judges_can_large_vision-language_models_fairly_evaluate_chart_compre.md)**

:   系统评估了 13 个开源小型 LVLM（≤9B 参数）作为图表理解和推理任务的评判者，发现部分开源模型（如 LLaVA-Critic-7B）可达到接近 GPT-4 水平的评判能力（约 80% 一致率），但位置偏差和长度偏差等问题仍然普遍存在。

**[Synergizing LLMs with Global Label Propagation for Multimodal Fake News Detection](llm_label_propagation.md)**

:   提出 GLPN-LLM 框架，通过 mask-based 全局标签传播机制有效整合 LLM 生成的伪标签，解决了 LLM 伪标签直接组合效果不佳的问题，在 Twitter/PHEME/Weibo 三个数据集上全面超越 SOTA。

**[LogicQA: Logical Anomaly Detection with Vision Language Model Generated Questions](logicqa_logical_anomaly_detection_with_vision_language_model_generated_questions.md)**

:   提出 LogicQA 框架，利用预训练 VLM 自动生成异常相关问题并通过问答投票机制检测逻辑异常，在无需训练、无需标注的少样本设置下达到 SOTA 性能，同时提供自然语言的异常原因解释。

**[LongDocURL: a Comprehensive Multimodal Long Document Benchmark Integrating Understanding, Reasoning, and Locating](longdocurl_multimodal_long_doc.md)**

:   提出LongDocURL基准（396篇文档、2,325 QA对、33,000+页，含理解/推理/定位三类20个子任务），通过半自动构建流程生成高质量长文档评测数据，26种配置的实验结果显示最强GPT-4o仅64.5分，开源最高30.6分，远低于人类84.8分。

**[MAGIC-VQA: Multimodal and Grounded Inference with Commonsense Knowledge for Visual Question Answering](magic-vqa_multimodal_and_grounded_inference_with_commonsense_knowledge_for_visua.md)**

:   提出MAGIC-VQA框架，通过三阶段流程（显式知识检索→按类型后处理→GNN隐式增强）将外部常识知识系统地注入LVLM，在ScienceQA、TextVQA、MMMU等基准上实现即插即用的常识推理增强，仅需0.33M可训练参数。

**[MAmmoTH-VL: Eliciting Multimodal Reasoning with Instruction Tuning at Scale](mammoth_vl_multimodal_reasoning.md)**

:   MAmmoTH-VL 提出了一种仅用开源模型构建 12M 多模态 CoT 推理指令数据的可扩展方法，通过数据收集→改写→自过滤三步管线，训练的 8B 模型在 MathVerse (+8.1%)、MMMU-Pro (+7%)、MuirBench (+13.3%) 上达到 SOTA。

**[Modality-Aware Neuron Pruning for Unlearning in Multimodal Large Language Models](manu_modality_aware_unlearning.md)**

:   提出MANU框架解决MLLM中的多模态遗忘不平衡问题：通过四种重要性函数（绝对/频率/方差/RMS）识别跨模态知识纠缠的神经元，选择性剪枝实现多模态输入和纯文本输入下的均衡知识遗忘，同时保持模型通用能力。

**[MathCoder-VL: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning](mathcoder-vl_bridging_vision_and_code_for_enhanced_multimodal_mathematical_reaso.md)**

:   提出利用代码作为跨模态对齐的监督信号，构建860万图像-代码对数据集ImgCode-8.6M和300万多模态数学指令微调数据集MM-MathInstruct-3M，训练的MathCoder-VL在开源模型中达到多模态数学推理SOTA，在几何问题上超越GPT-4o和Claude 3.5 Sonnet。

**[Evaluating Multimodal Large Language Models on Video Captioning via Monte Carlo Tree Search](mcts_video_captioning_eval.md)**

:   提出AutoCaption框架，利用蒙特卡洛树搜索(MCTS)自动迭代生成细粒度视频描述关键点（平均122个/视频），构建MCTS-VCB基准评估20+个MLLM的视频描述能力，并证明生成的数据可用于微调显著提升模型性能。

**[MDiT-Bench: Evaluating the Dual-Implicit Toxicity in Large Multimodal Models](mdit-bench_evaluating_the_dual-implicit_toxicity_in_large_multimodal_models.md)**

:   提出"双模态隐式毒性"(dual-implicit toxicity)概念——仅当结合图文两个模态时才能被识别的偏见与歧视，构建了包含317K问题、12类23子类的MDIT-Bench基准，并通过长上下文越狱揭示了主流多模态大模型中大量可被激活的隐藏毒性。

**[MEIT: Multimodal Electrocardiogram Instruction Tuning on Large Language Models for Report Generation](meit_multimodal_electrocardiogram_instruction_tuning_on_large_language_models_fo.md)**

:   提出 MEIT 框架，通过多模态指令微调将 ECG 信号与 LLM 对齐，利用轻量级拼接融合策略（无需额外参数）在 LLM 的自注意力层中注入 ECG 嵌入，实现自动 ECG 报告生成，并建立涵盖质量评估、零样本迁移、噪声鲁棒性和专家对齐四项任务的综合基准。

**[MIRe: Enhancing Multimodal Queries Representation via Fusion-Free Modality Interaction](mire_enhancing_multimodal_queries_representation_via_fusion-free_modality_intera.md)**

:   提出MIRe框架，通过"无融合模态交互"（fusion-free modality interaction）在视觉-文本对齐阶段避免直接融合文本特征，利用查询引导注意力池化模块让文本嵌入引导视觉信息提取但不将文本信号反馈回视觉表示，有效缓解多模态检索中的文本主导问题，在四个基准上取得零样本SOTA。

**[Mixture of Decoding: An Attention-Inspired Adaptive Decoding Strategy to Mitigate Hallucination in Multimodal LLMs](mixture_of_decoding_an_attention-inspired_adaptive_decoding_strategy_to_mitigate.md)**

:   提出了 Mixture of Decoding (MoD)，通过 JS 散度衡量模型对图像 token 注意力的正确性，在注意力正确时采用互补解码放大关键信息，注意力错误时采用对比解码抑制误导信息，从而自适应地缓解多模态大模型的幻觉问题。

**[MMBoundary: Advancing MLLM Knowledge Boundary Awareness through Reasoning Step Confidence Calibration](mmboundary_advancing_mllm_knowledge_boundary_awareness_through_reasoning_step_co.md)**

:   提出 MMBoundary 框架，通过对 MLLM 推理链中每一步进行置信度校准（而非仅对整体回答），结合文本+跨模态自奖励信号与强化学习，显著降低多模态置信度校准误差（平均 7.5%）并提升任务性能（最高 8.3%）。

**[MMBoundary: Advancing MLLM Knowledge Boundary Awareness through Reasoning Step Confidence Calibration](mmboundary_reasoning_step_confidence.md)**

:   提出 MMBoundary 框架，通过在推理链的每一步插入自然语言置信度表述（而非只在最终回答后给置信度），结合文本+跨模态的自奖励信号估计置信度，并用 SFT+RL 两阶段训练实现步级置信度校准，平均降低 7.5% 校准误差并提升 8.3% 任务准确率。

**[MMINA: Benchmarking Multihop Multimodal Internet Agents](mmina_benchmarking_multihop_multimodal_internet_agents.md)**

:   提出MMInA基准，包含1,050个人工编写的多跳多模态网页任务（覆盖14个真实动态网站，平均2.85跳），并设计逐跳评估协议和记忆增强方法，揭示当前最强Agent（GPT-4V仅21.8%任务成功率）在多跳网页导航上与人类（96.3%）的巨大差距。

**[MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](mmmu_pro_robust_benchmark.md)**

:   提出 MMMU-Pro 基准，通过过滤纯文本可解题目、扩增选项至 10 个、引入 vision-only 输入设置三步法，构建更鲁棒的多学科多模态理解评测，所有模型性能显著下降 16.8%-26.9%。

**[MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](mmmupro_a_more_robust_multidiscipline_multimodal.md)**

:   MMMU-Pro 通过三步流程（过滤纯文本可解题、扩展选项至 10 个、引入纯视觉输入设置）构建更鲁棒的多学科多模态理解基准，模型性能比原 MMMU 下降 16.8%~26.9%，揭示当前模型依赖捷径而非真正多模态理解。

**[MMSciBench: Benchmarking Language Models on Chinese Multimodal Scientific Problems](mmscibench_benchmarking_language_models_on_chinese_multimodal_scientific_problem.md)**

:   提出 MMSciBench，一个包含 4,482 道中文高中数学和物理题目的多模态科学推理基准，涵盖选择题和问答题、纯文本和图文配对两种模态，并带有人工标注难度等级和三级知识分类体系；评估显示最强模型 Gemini 1.5 Pro 002 仅达 63.77% 准确率，且在图文题上性能大幅下降（36.28 个百分点差距）。

**[mOSCAR: A Large-scale Multilingual and Multimodal Document-level Corpus](moscar_a_large-scale_multilingual_and_multimodal_document-level_corpus.md)**

:   提出 mOSCAR——首个大规模多语言多模态文档级语料库（163种语言、303M文档、200B tokens、1.15B图片），从 Common Crawl 中提取交错的图文文档，并证明在此数据上训练的多语言 mLLM 能获得显著的 few-shot 学习提升。

**[MTVQA: Benchmarking Multilingual Text-Centric Visual Question Answering](mtvqa_benchmarking_multilingual_text-centric_visual_question_answering.md)**

:   构建了 MTVQA——首个覆盖 9 种语言的多语言文本中心视觉问答基准，通过人类专家标注解决翻译方法的"视觉-文本不对齐"问题，评估显示最佳 MLLM（InternVL-2.5，32.2%）与人类表现（79.7%）差距巨大，揭示了多语言文本理解的严峻挑战。

**[MultiMM: Cultural Bias Matters — Cross-Cultural Benchmark for Multimodal Metaphors](multimm_cultural_metaphor.md)**

:   提出MultiMM——首个跨文化多模态隐喻数据集，包含8461个中英文广告图文对及细粒度标注，并设计SEMD模型融合情感特征增强隐喻检测。

**[NegVQA: Can Vision Language Models Understand Negation?](negvqa_can_vision_language_models_understand_negation.md)**

:   提出 NegVQA 基准（7,379 道二选一 VQA 题），系统评估 20 个 VLM 对否定句的理解能力，发现所有模型在否定问题上性能大幅下降（平均 29.7%），并揭示"U 型"缩放趋势。

**[OMGM: Orchestrate Multiple Granularities and Modalities for Efficient Multimodal Retrieval](omgm_orchestrate_multiple_granularities_and_modalities_for_efficient_multimodal_.md)**

:   提出OMGM——一个面向知识密集型视觉问答(KB-VQA)的多模态RAG系统，通过粗到细三步检索策略协调查询与知识库在不同粒度和模态间的匹配，在InfoSeek和E-VQA上取得SOTA检索性能和极具竞争力的问答结果。

**[A Survey on Patent Analysis: From NLP to Multimodal AI](patent_analysis_survey.md)**

:   全面综述基于 NLP 和多模态 AI 的专利分析方法，按专利生命周期中的四大任务（分类、检索、质量分析、生成）提出新的分类体系，覆盖从传统神经网络到 PLM/LLM 的技术演进。

**[Performance Gap in Entity Knowledge Extraction Across Modalities in Vision Language Models](performance_gap_in_entity_knowledge_extraction_across_modalities_in_vision_langu.md)**

:   系统性地揭示了视觉语言模型（VLM）在视觉 vs 文本表征下实体知识提取的显著性能差距（最高达 18%），通过机制可解释性工具发现图像 token 的关键信息流发生在模型中间层很深处，导致后续事实推理的层数不足。

**[PunchBench: Benchmarking MLLMs in Multimodal Punchline Comprehension](punchbench_mllm_punchline.md)**

:   提出PunchBench（6,000图文对、54,000 QA对），通过同义/反义标题替换消除文本捷径、多种问题格式与两层任务（感知+推理）全面评测MLLM的多模态梗图理解能力，并设计SC-CoQ由简到繁的提问策略显著提升表现，但GPT-4o仍远低于人类98%+水平。

**[R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding](r-vlm_region-aware_vision_language_model_for_precise_gui_grounding.md)**

:   提出R-VLM，将传统目标检测中的区域提议（region proposal）和IoU感知损失引入VLM的GUI元素定位，通过两阶段放大推理和IoU加权交叉熵损失，在ScreenSpot和AgentStudio上平均提升13%的grounding准确率。

**[RATE-Nav: Region-Aware Termination Enhancement for Zero-shot Object Navigation with Vision-Language Models](rate-nav_region-aware_termination_enhancement_for_zero-shot_object_navigation_wi.md)**

:   提出 RATE-Nav，一种基于边际效用理论的零样本目标导航方法，通过几何预测区域分割和基于区域的探索率估计，结合 VLM 的宏观环境感知能力智能判断是否终止当前区域的探索，在 HM3D 上达到 67.8% 成功率和 31.3% SPL，在 MP3D 上比先前零样本方法提升约 10%。

**[RedundancyLens: Revealing and Exploiting Visual Token Processing Redundancy for Efficient Decoder-Only MLLMs](redundancylens_revealing_and_exploiting_visual_token_processing_redundancy_for_e.md)**

:   提出 RedundancyLens 框架，系统揭示了 decoder-only MLLM 中视觉 token 在自注意力和 FFN 操作上存在大量结构化、聚簇式冗余，并利用这一发现实现免训练推理加速，与现有 token 压缩方法正交且可组合。

**[ReefKnot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models](reefknot_a_comprehensive_benchmark_for_relation_hallucination_evaluation_analysi.md)**

:   提出首个系统性评估多模态大模型**关系级幻觉**的综合基准 Reefknot（含 2 万+ 样本、三种任务），并基于置信度熵检测提出 Detect-then-Calibrate 缓解策略，平均降低幻觉率 9.75%。

**[Response Wide Shut: Surprising Observations in Basic Vision Language Model Capabilities](response_wide_shut_surprising_observations_in_basic_vision_language_model_capabi.md)**

:   通过在VLM的三个中间特征空间（视觉编码器、VL投影层、语言解码器）上训练线性探针，系统揭示了一个反直觉的现象：对于大多数视觉任务，视觉编码器和VL投影层其实保留了充分的视觉信息，真正的瓶颈在于语言解码器的响应空间——信息在从投影层传递到最终文本输出的过程中大量丢失。

**[Retrieval Visual Contrastive Decoding to Mitigate Object Hallucinations in Large Vision-Language Models](retrieval_visual_contrastive_decoding_to_mitigate_object_hallucinations_in_large.md)**

:   提出 RVCD（Retrieval Visual Contrastive Decoding），通过检索 AI 生成的单概念显式图像构建正/负 logit 集合，在解码阶段抑制 LVLM 的物体幻觉（Object Hallucination），无需额外训练即可显著优于现有解码方法。

**[Scalable Vision Language Model Training via High Quality Data Curation](scalable_vision_language_model_training_via_high_quality_data_curation.md)**

:   提出 SAIL-VL 系列开源视觉语言模型（2B/8B），核心贡献在于：构建了3亿规模最高质量的 SAIL-Caption 数据集，首次揭示了VLM预训练中的数据量对数缩放定律（655B token实验），并通过课程式三阶段SFT将缩放曲线从对数提升至近线性，在18个基准上达到SOTA。

**[SemEval-2025 Task 1: AdMIRe -- Advancing Multimodal Idiomaticity Representation](semeval-2025_task_1_admire_--_advancing_multimodal_idiomaticity_representation.md)**

:   设计了 SemEval-2025 AdMIRe 共享任务——通过图像排序和图像序列补全两个子任务，在多模态（文本+图像）和多语言（英语+巴西葡萄牙语）场景下评估模型对习语表达的理解能力，最佳系统通过混合专家和多查询平滑策略达到了接近人类水平的表现。

**[SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning](singakids_a_multilingual_multimodal_dialogic_tutor_for_language_learning.md)**

:   提出 SingaKids 系统，一个面向小学生的多语言多模态对话式语言学习辅导系统，通过图像描述任务整合稠密图像字幕、多语言对话、语音理解和儿童友好语音生成，支持英语、中文、马来语和泰米尔语四种语言的互动学习。

**[Sharper and Faster mean Better: Towards More Efficient Vision-Language Model for Hour-scale Long Video Understanding](sophia_efficient_long_video.md)**

:   提出Sophia模型处理小时级长视频：通过Shot-adaptive Frame Pruning（基于镜头分割的两阶段帧剪枝）精准选择查询相关帧，结合O(N)复杂度的Hierarchical Attention替代全注意力，在8/8个长视频benchmark中6个SOTA，且注意力FLOPs仅为InternVL2的1/17。

**[Can Multimodal Large Language Models Understand Spatial Relations?](spatialmqa_mllm_spatial_relations.md)**

:   提出SpatialMQA基准，通过5,392个基于COCO2017的人工标注多选题样本（无bbox、含视角替换、排除纯知识可答题），评测MLLM的空间关系推理能力，发现最强模型SpaceLLaVA仅达48.14%远低于人类98.40%。

**[Speaking Beyond Language: A Large-Scale Multimodal Dataset for Learning Nonverbal Cues from Video-Grounded Dialogues](speaking_beyond_language.md)**

:   提出 VENUS——首个大规模多模态对话数据集（89,459 段对话、14,910 小时），包含时间对齐的文本、3D 面部表情和肢体语言标注；基于该数据集开发 MARS 多模态语言模型，通过 VQ-VAE 将非语言线索离散化后与文本统一建模，实现对话中文本与非语言动作的联合理解和生成。

**[SPHERE: Unveiling Spatial Blind Spots in Vision-Language Models Through Hierarchical Evaluation](sphere_unveiling_spatial_blind_spots_in.md)**

:   提出 SPHERE 三层级空间推理评估框架（单技能→多技能→推理），基于 MS COCO 人工标注 2285 个 QA 对，发现 GPT-4o（67.9%）与人类（93.0%）差距 25%，尤其在距离判断、视角切换和物理推理上表现严重不足。

**[Symmetrical Visual Contrastive Optimization: Aligning Vision-Language Models with Minimal Contrastive Images](symmetrical_visual_contrastive_optimization_aligning_visionlanguage.md)**

:   提出 S-VCO（对称视觉对比优化），一种新的 VLM 微调目标，通过对称地对齐/拒绝匹配/矛盾的图像-文本对来增强视觉依赖，配合最小视觉对比数据集 MVC，在幻觉检测上减少 22%，视觉依赖任务上显著提升。

**[Table Understanding and (Multimodal) LLMs: A Cross-Domain Case Study on Scientific Tables](table_understanding_and_multimodal_llms_a_cross-domain_case_study_on_scientific_.md)**

:   提出 TableEval 基准（3017 张表格，5 种格式），系统比较了文本 LLM 和多模态 LLM 在科学 vs. 非科学表格理解任务上的表现，发现模型对表格模态（图像/文本）保持鲁棒但在科学表格上性能显著下降。

**[Teaching Vision-Language Models to Ask: Resolving Ambiguity in Visual Questions](teaching_vlm_ask_ambiguity.md)**

:   提出ClearVQA benchmark评估VLM处理歧义视觉问题的能力（覆盖指代歧义/意图欠明确/拼写歧义三类），并通过自动化pipeline生成歧义-澄清问题对用于SFT+DPO训练，使VLM学会"反问用户"而非猜测作答，VQA准确率相对提升13.3%。

**[TheoremExplainAgent: Towards Video-based Multimodal Explanations for LLM Theorem Understanding](theorem_explain_agent.md)**

:   提出 TheoremExplainAgent，一个基于多 Agent 协作的系统，能自动生成 5 分钟以上的定理讲解视频（Manim 动画+语音旁白），并构建了 TheoremExplainBench（240 个 STEM 定理，5 维评估指标）用于系统评估。

**[Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?](token_pruning_in_multimodal_large_language_models_are_we_solving_the_right_probl.md)**

:   通过大规模基准实验揭示了当前MLLM视觉token剪枝方法的多个根本性问题：精心设计的剪枝策略（FastV、SparseVLM）在多数基准上甚至不如随机选择和池化等朴素方法，原因在于注意力评分的位置偏差、对语言信息的误用、重要性与冗余性的失衡以及评估指标的不可靠。

**[Transferring Textual Preferences to Vision-Language Understanding through Model Merging](transferring_textual_preferences_to_vision-language_understanding_through_model_.md)**

:   提出一种免训练方法，通过模型参数合并（model merging）将纯文本奖励模型（RM）的偏好能力迁移到大视觉语言模型（LVLM）中，构建视觉语言奖励模型（VLRM），在多个多模态评估基准上超越LVLM直接评分和纯文本RM。

**[TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](trimllm_layer_dropping.md)**

:   基于"层级特化"现象（不同层对不同领域重要性不同），提出TrimLLM在领域微调过程中渐进式丢弃最不重要的层，将LLaMA-7B压缩到50%大小时性能几乎无损，在消费级GPU上实现2.1-5.7×推理加速——无需任何特殊硬件或kernel支持。

**[Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning](tvc_mitigating_visual_forgetting.md)**

:   发现MLLM长链推理中存在严重的"视觉遗忘"现象——推理进行到一半时移除图片仅导致2%精度下降，说明模型过度依赖文本输出而非视觉输入。提出Take-along Visual Conditioning (TVC)，在推理过程中周期性重新注入压缩后的图像特征，在5个数学推理基准上平均超越之前SOTA 3.4个点。

**[Unsolvable Problem Detection: Evaluating Trustworthiness of Large Multimodal Models](unsolvable_problem_detection.md)**

:   本文提出不可解问题检测（UPD）任务评估大型多模态模型（LMM）的鲁棒理解能力，包含三种不可解场景（答案缺失AAD、答案集不兼容IASD、图像问题不兼容IVQD），构建 MM-UPD Bench 基准，实验揭示现有 LMM 在标准 MCQA 上表现良好但在 UPD 上显著挣扎，且现有基准性能与 UPD 能力之间缺乏相关性。

**[Unveiling the Lack of LVLM Robustness to Fundamental Visual Variations: Why and Path Forward](unveiling_the_lack_of_lvlm_robustness_to_fundamental_visual_variations_why_and_p.md)**

:   提出 V2R-Bench 基准框架系统评估 21 个 LVLM 对位置/尺度/方向/上下文四种基本视觉变化的鲁棒性，揭示了即使先进模型在简单视觉任务上也存在显著脆弱性，并通过组件级分析证明这些漏洞根源在于多模态对齐不足和流水线架构的误差累积，而非数据不足。

**[Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition](value_spectrum_vlm_pref.md)**

:   提出 Value-Spectrum 基准，通过 50K+ 社交媒体短视频截图和 Schwartz 价值理论框架，系统评估 VLM 的内在价值偏好及角色扮演时的偏好适配能力。

**[VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos](vf_eval_aigc_video_feedback.md)**

:   提出VF-Eval基准，通过一致性验证、错误感知、错误类型检测、推理评估四大任务系统评估13个MLLM为AIGC视频提供反馈的能力，发现即使GPT-4.1也难以在所有任务上表现一致，揭示了AIGC视频理解的挑战性。

**[ViGiL3D: A Linguistically Diverse Dataset for 3D Visual Grounding](vigil3d_a_linguistically_diverse_dataset_for_3d_visual_grounding.md)**

:   提出 ViGiL3D——一个语言多样性诊断数据集和自动化分析框架，用于评估 3D 视觉定位（3DVG）方法在否定、粗粒度指代、共指消解等多种语言现象上的表现，揭示现有方法在分布外提示上性能显著下降（最高达 20+ 点）。

**[Vision-Language Models Struggle to Align Entities across Modalities](vision-language_models_struggle_to_align_entities_across_modalities.md)**

:   提出 MATE 基准测试，包含 5,500 个评估实例，通过问答任务评估视觉语言模型（VLM）的跨模态实体链接能力，发现 VLM 在将同一实体的视觉和文本表示进行对齐方面远不如人类，尤其随场景中物体数量增加性能急剧下降。

**[Visual Evidence Prompting Mitigates Hallucinations in Large Vision-Language Models](visual_evidence_prompting.md)**

:   提出Visual Evidence Prompting (VEP)，利用小型视觉专家模型（目标检测器、场景图生成器）的输出作为文本化"视觉证据"输入LVLM，无需训练即可在11个LVLM上显著降低幻觉——LLaVA-1.5在POPE上提升7.2%、Claude 3上提升12.1%。

**[VLMInferSlow: Evaluating the Efficiency Robustness of Large Vision-Language Models as a Service](vlminferslow_evaluating_the_efficiency_robustness_of.md)**

:   首次在黑盒设置下研究 VLM 的效率鲁棒性，提出 VLMInferSlow 方法，通过零阶优化搜索对抗性图像扰动，迫使 VLM 生成更长序列，将计算成本最高增加 128.47%，揭示了 VLM 在 MLaaS 部署场景下的效率安全隐患。

**[VReST: Enhancing Reasoning in Large Vision-Language Models through Tree Search and Self-Reward Mechanism](vrest_tree_search_vlm_reasoning.md)**

:   提出VReST，首次将蒙特卡洛树搜索（MCTS）应用于多模态CoT推理：每个节点是一个推理步骤，通过多模态自奖励机制（sub-question有用性+答案正确性+视觉-语言线索相关性）评估推理质量，无需训练即在MathVista上达到64.50%（超越CoT的54.60%和ToT的60.20%），并展示出多模态测试时缩放定律。

**[WikiMixQA: A Multimodal Benchmark for Question Answering over Tables and Charts](wikimixqa_a_multimodal_benchmark_for_question_answering_over_tables_and_charts.md)**

:   提出 WikiMixQA 基准，包含 1,000 道需要跨表格和图表进行多模态推理的多选题，评估 12 个 VLLM 后发现闭源模型在提供精确上下文时准确率约 70%，但需从长文档检索时性能骤降，开源模型最高仅 27%，揭示了当前视觉语言模型在长上下文多模态文档理解上的严重不足。
