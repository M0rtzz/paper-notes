---
title: >-
  ACL2026 178篇论文解读
description: >-
  178篇ACL2026论文解读，涵盖医学图像(19篇)、模型压缩(16篇)、多模态VLM(16篇)、信息检索/RAG(12篇)等36个方向，每篇含核心思想、方法详解与实验分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 ACL2026 论文笔记

**178** 篇论文解读，覆盖 **36** 个领域。

<div class="conf-index" markdown>

---

## 🏥 医学图像 { #medical_imaging }

**["Excuse Me, May I Say Something…" CoLabScience: A Proactive AI Assistant for Biomedical Discovery](medical_imaging/34excuse_me_may_i_say_something34_colabscience_a_proactive_ai_assistant_for_biom.md)**

:   CoLabScience 通过 PULI（正无标注学习干预）框架，训练一个能在生物医学团队讨论中**主动判断何时介入、如何介入**的 LLM 助手，利用 GRPO 和强化学习协调器从流式对话中自动识别最佳干预时机并生成科学建议。

**[AROMA: Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling](medical_imaging/aroma_augmented_reasoning_over_a_multimodal_architecture_for_virtual_cell_geneti.md)**

:   提出 AROMA 框架，通过整合文本证据、知识图谱拓扑信息和蛋白质序列特征的多模态架构，结合两阶段训练策略（SFT + GRPO），实现了可解释且精确的基因扰动效应预测。

**[Benchmarking and Enabling Efficient Chinese Medical Retrieval via Asymmetric Encoders](medical_imaging/benchmarking_and_enabling_efficient_chinese_medical_retrieval_via_asymmetric_enc.md)**

:   提出 CMedTEB（中文医学文本嵌入基准）和 CARE（非对称检索框架），前者通过多 LLM 投票+专家验证构建高质量的中文医学检索/重排/STS 基准，后者用轻量 BERT 编码查询+大型 LLM 编码文档的非对称架构，通过两阶段渐进对齐策略实现 LLM 级检索精度+BERT 级在线延迟。

**[Beyond Prompt: Fine-grained Simulation of Cognitively Impaired Standardized Patients via Stochastic Steering](medical_imaging/beyond_prompt_fine-grained_simulation_of_cognitively_impaired_standardized_patie.md)**

:   提出 StsPatient，通过从对比指令/回复对中提取领域特定的转向向量（Steering Vector），配合随机 Token 调制（STM）机制控制注入概率来模拟不同认知障碍领域和严重程度的标准化病人，相比 prompt engineering 方法在临床真实性上平均提升 11.23%，在严重程度可控性上超越最佳基线 18.54%。

**[Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical Intake via Collaborative Agents](medical_imaging/beyond_the_individual_virtualizing_multi-disciplinary_reasoning_for_clinical_int.md)**

:   提出 Aegle 框架，通过图结构多智能体架构虚拟化多学科会诊（MDT），将解耦并行推理和动态拓扑引入门诊问诊流程，在24个科室53项指标上超越SOTA模型。

**[BioHiCL: Hierarchical Multi-Label Contrastive Learning for Biomedical Retrieval with MeSH Labels](medical_imaging/biohicl_hierarchical_multi-label_contrastive_learning_for_biomedical_retrieval_w.md)**

:   BioHiCL 利用 MeSH（医学主题词）的**层级多标签标注**为稠密检索器提供结构化监督，通过深度加权的标签相似度对齐嵌入空间与 MeSH 语义空间，使 0.1B 模型在生物医学检索、句子相似度和问答任务上超越大多数专用模型。

**[Calibrated? Not for Everyone: How Sexual Orientation and Religious Markers Distort LLM Accuracy and Confidence in Medical QA](medical_imaging/calibrated_not_for_everyone_how_sexual_orientation_and_religious_markers_distort.md)**

:   研究社会身份标记（性取向和宗教信仰）如何扭曲LLM在医疗问答中的准确率和置信度校准，发现"同性恋"标记在9个LLM上一致导致性能下降和校准危机，且交叉身份产生非加性的特异性伤害。

**[CURA: Clinical Uncertainty Risk Alignment for Language Model-Based Risk Prediction](medical_imaging/cura_clinical_uncertainty_risk_alignment_for_language_model-based_risk_predictio.md)**

:   CURA 提出一个双层不确定性校准框架：个体层面将预测不确定性与错误概率对齐，队列层面通过嵌入空间的邻域风险率正则化预测，在 MIMIC-IV 的五个临床风险预测任务上一致提升校准指标而不牺牲判别性能。

**[Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](medical_imaging/detecting_hallucinations_in_speechllms_at_inference_time_using_attention_maps.md)**

:   提出四种基于音频注意力的指标（AudioRatio、AudioConsistency、AudioEntropy、TextEntropy），训练轻量级逻辑回归分类器在推理时检测语音大模型（SpeechLLM）的幻觉，在域内数据上 PR-AUC 提升最高达 +0.23。

**[Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction](medical_imaging/efficient_and_effective_internal_memory_retrieval_for_llm-based_healthcare_predi.md)**

:   本文提出K2K框架，将LLM的FFN参数空间视为可检索的知识库，通过LoRA注入临床知识、激活引导的探针构建精确检索、交叉注意力重排序自适应整合，实现了无需外部检索延迟的医疗预测SOTA。

**[Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach](medical_imaging/eliciting_medical_reasoning_with_knowledge-enhanced_data_synthesis_a_semi-superv.md)**

:   本文提出MedSSR框架，通过注入罕见病知识的可控数据合成和"自监督RL→监督RL"的半监督训练范式，高效提升LLM的医学推理能力，在罕见病任务上实现最高+5.93%的提升，突破了现有方法+3%的改进上限。

**[From Answers to Arguments: Toward Trustworthy Clinical Diagnostic Reasoning with Toulmin-Guided Curriculum Goal-Conditioned Learning](medical_imaging/from_answers_to_arguments_toward_trustworthy_clinical_diagnostic_reasoning_with_.md)**

:   本文将Toulmin论证模型适配到临床诊断过程，提出CGCL三阶段课程训练框架（事实收集→假设检验→综合结论），配合T-Eval量化评估推理结构完整性，在无需RL的情况下实现与RL方法可比的诊断推理质量。

**[HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering](medical_imaging/hypehr_hyperbolic_modeling_of_electronic_health_records_for_efficient_question_a.md)**

:   本文提出 HypEHR，一个仅 22M 参数的洛伦兹双曲模型，将医学编码、就诊记录和问题嵌入双曲空间，通过层级感知正则化对齐 ICD 本体结构，在 MIMIC-IV 电子病历问答任务上接近 LLM 方法的效果。

**[Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness](medical_imaging/learning_dynamic_representations_and_policies_from_multimodal_clinical_time-seri.md)**

:   提出 OPL-MT-MNAR 框架，通过 MNAR 感知的多模态编码器 + 贝叶斯滤波隐状态 + 离线策略学习，从结构化数据和临床文本的"缺失模式本身携带的信息"中学习 ICU 患者动态表示，实现优于临床医生行为的脓毒症治疗策略（FQE 0.679 vs 0.528）。

**[MHSafeEval: Role-Aware Interaction-Level Evaluation of Mental Health Safety in Large Language Models](medical_imaging/mhsafeeval_role-aware_interaction-level_evaluation_of_mental_health_safety_in_la.md)**

:   本文提出 R-MHSafe 角色感知心理健康安全分类体系和 MHSafeEval 闭环 agent 评估框架，通过对抗性多轮咨询交互系统性发现 LLM 在心理咨询场景中的角色依赖型累积安全失败，揭示了现有静态基准无法捕捉的交互层面危害。

**[RADS: Reinforcement Learning-Based Sample Selection Improves Transfer Learning in Low-resource and Imbalanced Clinical Settings](medical_imaging/rads_reinforcement_learning-based_sample_selection_improves_transfer_learning_in.md)**

:   本文提出 RADS（Reinforcement Adaptive Domain Sampling），一种基于强化学习的样本选择策略，在极端低资源和类别不平衡的临床场景下，通过智能选择少量目标域样本进行标注和联合微调，显著提升跨域疾病检测的迁移效果。

**[Region-Grounded Report Generation for 3D Medical Imaging: A Fine-Grained Dataset and Graph-Enhanced Framework](medical_imaging/region-grounded_report_generation_for_3d_medical_imaging_a_fine-grained_dataset_.md)**

:   本文提出首个带有细粒度 ROI 标注的 3D PET/CT 数据集 VietPET-RoI（越南语），以及模拟放射科医生诊断流程的层次化报告生成框架 HiRRA，通过图神经网络建模 ROI 间的空间-形态学关系，BLEU-4 提升 19.7%，临床指标 RoIQ 提升 45.8%。

**[RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models](medical_imaging/reprompt_recurrent_prompt_tuning_for_integrating_structured_ehr_encoders_with_la.md)**

:   本文提出 RePrompT，一种时间感知的 LLM 框架，通过循环提示调优（将前一次就诊的隐状态作为下一次就诊的软提示）和结构化编码提示调优（注入群体级 EHR 编码器的嵌入）两种互补机制，在 MIMIC-III/IV 上的再入院和死亡率预测任务上一致超越 EHR 基线和 LLM 基线。

**[Thinking Like a Botanist: Challenging Multimodal Language Models with Intent-Driven Chain-of-Inquiry](medical_imaging/thinking_like_a_botanist_challenging_multimodal_language_models_with_intent-driv.md)**

:   本文提出PlantInquiryVQA基准和Chain-of-Inquiry（CoI）框架，包含24,950张植物图像和138,068个问答对，模拟植物学家的适应性诊断提问策略，评估18个MLLM在植物病理诊断中的多步视觉推理能力，发现结构化提问显著提升诊断准确性并减少幻觉，但即使最强模型的临床实用性得分仅0.188。

---

## 📦 模型压缩 { #model_compression }

**[A Computational Method for Measuring "Open Codes" in Qualitative Analysis](model_compression/a_computational_method_for_measuring_34open_codes34_in_qualitative_analysis.md)**

:   提出一种基于理论的计算方法，通过LLM增强的代码合并算法和四个无需ground truth的指标（Coverage, Overlap, Novelty, Divergence），系统评估人类和AI在归纳定性编码中的表现。

**[A Layer-wise Analysis of Supervised Fine-Tuning](model_compression/a_layer-wise_analysis_of_supervised_fine-tuning.md)**

:   通过信息论、几何和优化三个视角对 1B-32B 模型的 SFT 进行逐层分析，发现指令跟随能力集中在中间层（20%-80%），而非均匀分布，据此提出 Mid-Block Efficient Tuning 策略，选择性更新中间层，在 GSM8K 上比标准 LoRA 提升高达 10.2%。

**[Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference](model_compression/adaptive_layer_selection_for_layer-wise_token_pruning_in_llm_inference.md)**

:   提出ASL（Adaptive Selection Layer），通过监控token注意力分数排名的方差来自适应确定KV缓存剪枝的层位置，在困难任务上显著优于固定层选择方法，同时保持无需训练。

**[Are Emotion and Rhetoric Neurons in LLM? Neuron Recognition and Adaptive Masking for Emotion-Rhetoric Prediction Steering](model_compression/are_emotion_and_rhetoric_neurons_in_llm_neuron_recognition_and_adaptive_masking_.md)**

:   系统研究LLM中情感和修辞神经元的表征机制及其内在关联，提出结合多维筛选的神经元识别框架和自适应遮蔽验证方法，实现了情感/修辞预测的定向诱导和修辞神经元辅助情感识别。

**[Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference](model_compression/calibrated_speculative_decoding_frequency-guided_candidate_selection_for_efficie.md)**

:   CSD 提出一种训练免的推测解码增强框架，通过在线校正记忆（OCM）记录高频拒绝模式提供救援候选，再用语义一致性门控（SCG）基于概率比验证候选可靠性，将推测解码的吞吐量提升至最高 2.33×，同时在 HumanEval 和 MATH500 上甚至提升了准确率。

**[CBRS: Cognitive Blood Request System with Bilingual Dataset and Dual-Layer Filtering](model_compression/cbrs_cognitive_blood_request_system_with_bilingual_dataset_and_dual-layer_filter.md)**

:   CBRS 提出一个多平台框架，通过双层过滤架构（轻量分类器 + LLM）从社交媒体消息流中高效检测并解析血液捐献请求，构建了首个包含 11K 条孟加拉语-英语-转写孟加拉语的血液捐献请求数据集，LoRA 微调的 Llama-3.2-3B 在解析任务上达到 92% 零样本准确率。

**[CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents](model_compression/clag_adaptive_memory_organization_via_agent-driven_clustering_for_small_language.md)**

:   本文提出 CLAG，一种基于聚类的 Agent 记忆框架，通过 SLM 驱动的路由将记忆组织到语义一致的聚类中，在聚类内部进行局部进化更新，并通过两阶段检索过滤噪声，在多个 QA 数据集上显著优于全局记忆池基线。

**[CounterRefine: Answer-Conditioned Counterevidence Retrieval for Inference-Time Knowledge Repair in Factual Question Answering](model_compression/counterrefine_answer-conditioned_counterevidence_retrieval_for_inference-time_kn.md)**

:   本文提出 CounterRefine，一个轻量级推理时修复层：先用标准 RAG 产生初步答案，再通过答案条件化的反证检索收集支持/反对证据，最后通过受限的 KEEP/REVISE 决策和确定性验证修复错误答案，在 SimpleQA 上将 GPT-5 的正确率从 67.3% 提升至 73.1%。

**[Do Not Step Into the Same River Twice: Learning to Reason from Trial and Error](model_compression/do_not_step_into_the_same_river_twice_learning_to_reason_from_trial_and_error.md)**

:   提出 LTE (Learning to reason from Trial and Error)，通过将模型自身生成的错误答案作为提示引导额外 rollout，在不依赖外部专家的情况下有效缓解 RLVR 中的探索停滞问题。

**[Efficient Learned Data Compression via Dual-Stream Feature Decoupling](model_compression/efficient_learned_data_compression_via_dual-stream_feature_decoupling.md)**

:   本文提出FADE框架，通过双流多尺度解耦器将微观句法和宏观语义特征分离到并行浅层流中处理（取代深层串行堆叠），结合层次化门控精炼器和并发流并行流水线，在压缩率和吞吐量上同时达到SOTA。

**[JudgeMeNot: Personalizing Large Language Models to Emulate Judicial Reasoning in Hebrew](model_compression/judgemenot_personalizing_large_language_models_to_emulate_judicial_reasoning_in_.md)**

:   提出了一个 synthetic-organic 监督管线，将法官的原始判决文书转化为推理指令微调数据，通过 CLM→指令微调的 Chain-of-LoRA 策略实现对个体法官推理风格的高保真模拟，在希伯来语低资源场景下生成内容与真实法官不可区分。

**[Mem²Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](model_compression/mem2evolve_towards_self-evolving_agents_via_co-evolutionary_capability_expansion.md)**

:   本文提出 Mem²Evolve，一种通过双记忆机制（资产记忆 + 经验记忆）实现能力扩展与经验蒸馏协同进化的自进化 Agent 框架，在 6 类任务 8 个基准上平均 Pass@1 达 70.24%，分别超过纯经验进化和纯能力进化的最强基线 11.80% 和 6.46%。

**[Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data](model_compression/memory-augmented_llm-based_multi-agent_system_for_automated_feature_generation_o.md)**

:   提出 MALMAS，一个记忆增强的 LLM 多智能体系统用于表格数据自动特征生成，通过六个专职 Agent 分工探索不同特征空间维度 + 三级记忆机制（过程/反馈/概念）实现跨轮迭代优化，在 16 个分类和 7 个回归数据集上超越现有基线。

**[Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models](model_compression/meta-tool_efficient_few-shot_tool_adaptation_for_small_language_models.md)**

:   通过在四个基准上系统对比超网络 LoRA 适应 vs 精心设计的 few-shot 提示，发现 2.28 亿参数的超网络提供零增益——few-shot 示例贡献 +21.5%、文档编码贡献 +5.0%、超网络贡献 0%，3B 模型配合良好提示可达 GPT-5 平均性能的 79.7% 且延迟低 10 倍。

**[Supplement Generation Training for Enhancing Agentic Task Performance](model_compression/supplement_generation_training_for_enhancing_agentic_task_performance.md)**

:   SGT（Supplement Generation Training）训练一个小型 LLM（1.7B）生成逐实例的补充文本（推理线索、摘要、错误提醒等），附加到输入后让冻结的大型 Actor 模型更有效地解决任务，在 5 个基准上平均提升 21%，无需修改大模型参数。

**[Think Outside the Policy: In-Context Steered Policy Optimization](model_compression/think_outside_the_policy_in-context_steered_policy_optimization.md)**

:   提出 ICPO (In-Context Steered Policy Optimization)，利用大语言模型自身的上下文学习(ICL)能力作为隐式专家引导，在 RLVR 训练中扩展策略探索空间，无需依赖外部更强模型的推理轨迹。

---

## 🧩 多模态VLM { #multimodal_vlm }

**[Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](multimodal_vlm/addressing_overthinking_in_large_vision-language_models_via_gated_perception-rea.md)**

:   提出GPRO框架，通过元推理控制器在每个token生成步动态路由计算到三条路径（快速/感知重检/推理反思），解决LVLM的过度思考问题，同时提升精度和效率。

**[AICA-Bench: Holistically Examining the Capabilities of VLMs in Affective Image Content Analysis](multimodal_vlm/aica-bench_holistically_examining_the_capabilities_of_vlms_in_affective_image_co.md)**

:   提出 AICA-Bench，一个涵盖情感理解（EU）、情感推理（ER）和情感引导内容生成（EGCG）三个维度的综合基准，评估 23 个 VLM 后发现模型存在强度校准失败和描述浅薄两大缺陷，并提出 GAT Prompting 训练无关框架来缓解这些问题。

**[Automatic Slide Updating with User-Defined Dynamic Templates and Natural Language Instructions](multimodal_vlm/automatic_slide_updating_with_user-defined_dynamic_templates_and_natural_languag.md)**

:   定义了"基于自然语言指令在用户自定义模板上进行动态幻灯片更新"的新任务，构建了包含 20,036 个指令-执行三元组的 DynaSlide 基准，并提出了 SlideAgent 作为强参考基线。

**[Benchmarking Deflection and Hallucination in Large Vision-Language Models](multimodal_vlm/benchmarking_deflection_and_hallucination_in_large_vision-language_models.md)**

:   提出 VLM-DeflectionBench，一个包含 2775 个样本的多模态基准，通过四种评估场景（参数化/Oracle/现实/对抗）系统性地评估大型视觉语言模型在证据不足或误导时的拒答（deflection）vs 幻觉（hallucination）行为，实验覆盖 20 个 SOTA LVLM，发现几乎所有模型都无法在噪声证据下可靠拒答。

**[CogGen: A Cognitively Inspired Recursive Framework for Deep Research Report Generation](multimodal_vlm/coggen_a_cognitively_inspired_recursive_framework_for_deep_research_report_gener.md)**

:   CogGen 提出一个模拟人类认知写作过程的多智能体递归框架，通过宏观认知循环实现全局重构、微观认知循环实现并行章节精炼、抽象视觉表示（AVR）实现文本-图表的语义级协同规划，在 OWID 基准上达到人类专家水平并超越 Gemini Deep Research。

**[Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games](multimodal_vlm/collaborative_multi-agent_scripts_generation_for_enhancing_imperfect-information.md)**

:   提出一个协作式多智能体框架用于自动生成高质量剧本杀游戏脚本和训练数据，通过两阶段训练策略（CoT 微调 + GRPO 强化学习配合 ScoreAgent 奖励塑形）增强 VLM 在不完全信息下的多跳推理能力，在 WhodunitBench 上显著提升 VLM 的叙事推理、事实提取和欺骗抵御能力。

**[Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](multimodal_vlm/don39t_act_blindly_robust_gui_automation_via_action-effect_verification_and_self.md)**

:   本文提出VeriGUI框架，通过Thinking-Verification-Action-Expectation（TVAE）闭环推理机制和两阶段训练管线（Robust SFT + GRPO），让GUI Agent能够验证每步操作是否成功并在失败时自我纠正，在3B和7B规模上均显著优于基线。

**[Dynamic Emotion and Personality Profiling for Multimodal Deception Detection](multimodal_vlm/dynamic_emotion_and_personality_profiling_for_multimodal_deception_detection.md)**

:   本文指出现有欺骗检测数据集仅提供受试者级别的情感/人格标签（同一人所有样本共用标签），提出样本级动态标注方案和可靠性加权多模态融合框架 Rel-DDEP，在欺骗检测 F1 上提升 2.53%，情感检测提升 2.66%，人格检测提升 9.30%。

**[Efficient Inference for Large Vision-Language Models: Bottlenecks, Techniques, and Prospects](multimodal_vlm/efficient_inference_for_large_vision-language_models_bottlenecks_techniques_and_.md)**

:   本文提出一个系统性的LVLM推理效率分类体系，围绕编码-预填充-解码三阶段推理流水线分析瓶颈，揭示了"视觉token主导"导致的系统性效率屏障，并梳理了从信息密度塑形、长上下文注意力管理到内存带宽突破的完整优化技术图谱。

**[Enhancing Multimodal Large Language Models for Ancient Chinese Character Evolution Analysis via Glyph-Driven Fine-Tuning](multimodal_vlm/enhancing_multimodal_large_language_models_for_ancient_chinese_character_evoluti.md)**

:   本文构建了一个包含11个任务、13万+实例的古汉字演变分析基准，评估了19个MLLM后发现现有模型在字形级识别和演变推理上能力有限，并提出字形驱动对比微调框架GEVO，在2B模型上实现全任务提升。

**[FineSteer: A Unified Framework for Fine-Grained Inference-Time Steering in Large Language Models](multimodal_vlm/finesteer_a_unified_framework_for_fine-grained_inference-time_steering_in_large_.md)**

:   FineSteer 将推理时转向分解为两个互补阶段：子空间引导的条件转向（SCS）决定"何时转向"——用 IR 查询子空间的能量比做门控；混合转向专家（MoSE）决定"如何转向"——通过注意力门控网络动态聚合原型专家+残差精炼生成查询特异性转向向量，在安全和真实性 benchmark 上超越 SOTA。

**[From Heads to Neurons: Causal Attribution and Steering in Multi-Task Vision-Language Models](multimodal_vlm/from_heads_to_neurons_causal_attribution_and_steering_in_multi-task_vision-langu.md)**

:   提出 HONES 框架，通过先定位任务关键注意力头再以其为条件引导 FFN 神经元归因，实现了多任务 VLM 中跨异构任务的统一、无梯度的神经元级因果分析和轻量级任务性能提升。

**[Mitigating Hallucinations in Large Vision-Language Models without Performance Degradation](multimodal_vlm/mitigating_hallucinations_in_large_vision-language_models_without_performance_de.md)**

:   本文提出 MPD 框架，通过语义感知正交子空间投影分离幻觉成分，并仅选择性更新与幻觉最相关的少量参数，在减少 23.4% 幻觉的同时保持 97.4% 的通用生成能力，不引入额外推理开销。

**[OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Models](multimodal_vlm/omibench_benchmarking_olympiad-level_multi-image_reasoning_in_large_vision-langu.md)**

:   本文提出 OMIBench——首个面向奥赛级多图推理的大规模基准，涵盖生物、化学、数学、物理四学科超 1000 道竞赛题，发现即使最强 LVLM（Gemini-3-Pro）也仅达约 50% 准确率，比单图基准下降超 25%。

**[Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval](multimodal_vlm/omni-embed-audio_leveraging_multimodal_llms_for_robust_audio-text_retrieval.md)**

:   本文提出 OEA（Omni-Embed-Audio），利用多模态 LLM 作为统一编码器构建检索导向的音频-文本嵌入空间，并引入 User-Intent Queries（UIQ）基准和硬负例区分指标（HNSR/TFR），发现 LLM 主干在 T2T 检索（+22%）和硬负例区分（+4.3%p HNSR@10）上显著优于 CLAP 系列方法。

**[SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models](multimodal_vlm/safetyalfred_evaluating_safety-conscious_planning_of_multimodal_large_language_m.md)**

:   本文提出 SafetyALFRED 基准，在 ALFRED 具身任务中引入六类厨房安全隐患，揭示了多模态大语言模型在静态 QA 中能识别危险（最高 92%）但在具身规划中却难以主动缓解危险（<60%）的严重对齐差距，倡导从 QA 评估范式转向具身安全评估。

---

## 🔍 信息检索/RAG { #information_retrieval }

**[A Survey on MLLM-based Visually Rich Document Understanding: Methods, Challenges, and Emerging Trends](information_retrieval/a_survey_on_mllm-based_visually_rich_document_understanding_methods_challenges_a.md)**

:   系统综述基于多模态大语言模型（MLLM）的视觉丰富文档理解（VRDU），从特征表示/融合和训练范式两个维度梳理OCR-based和OCR-free方法，并讨论数据稀缺、多页文档、多语言支持、RAG和智能体等新兴方向。

**[All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG](information_retrieval/all_languages_matter_understanding_and_mitigating_language_bias_in_multilingual_.md)**

:   系统揭示多语言 RAG 系统在重排序阶段存在严重的语言偏差（偏好英语和查询语言），提出 LAURA 框架通过下游生成质量驱动的监督信号对齐重排序器，有效缓解偏差并提升生成性能。

**[CarO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation](information_retrieval/caro_chain-of-analogy_reasoning_optimization_for_robust_content_moderation.md)**

:   提出 CarO（Chain-of-Analogy Reasoning Optimization），一个两阶段训练框架，通过 RAG 引导生成类比推理链 + SFT + 定制 DPO 优化，使 LLM 在推理时自主生成类比参考案例进行内容审核，在模糊审核基准上 F1 平均提升 24.9%，显著超越推理模型（DeepSeek R1）和专用审核模型（LLaMA Guard）。

**[ChAIRO: Contextual Hierarchical Analogical Induction and Reasoning Optimization for LLMs](information_retrieval/chairo_contextual_hierarchical_analogical_induction_and_reasoning_optimization_f.md)**

:   提出 ChAIRO，一个上下文层次化类比归纳与推理优化框架，通过三阶段 pipeline（类比案例生成→规则归纳→规则注入微调）让 LLM 在内容审核中自主生成类比案例并归纳显式审核规则，比单实例规则生成提升 F1 4.5%，比静态 RAG 提升 2.3%。

**[ChunQiuTR: Time-Keyed Temporal Retrieval in Classical Chinese Annals](information_retrieval/chunqiutr_time-keyed_temporal_retrieval_in_classical_chinese_annals.md)**

:   提出 ChunQiuTR，首个基于非格里历的时间键检索基准，从《春秋》及其注疏传统中构建，并设计了 CTD（历法时间双编码器），通过傅里叶绝对历法上下文和相对偏移偏置实现时间感知检索，显著优于纯语义基线。

**[CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](information_retrieval/curate_continual_unlearning_in_real_time_with_ensured_preservation_of_llm_knowle.md)**

:   CURaTE 提出一种基于句子嵌入匹配的行为遗忘框架：预部署时训练一个通用的遗忘嵌入器（不使用任何遗忘集），部署后实时将新遗忘请求嵌入存入数据库，推理时通过余弦相似度决定是回答还是拒绝，完全不修改 LLM 权重从而实现近乎完美的知识保留。

**[Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game](information_retrieval/detecting_rag_extraction_attack_via_dual-path_runtime_integrity_game.md)**

:   提出 CanaryRAG，一个受软件安全中栈金丝雀启发的 RAG 运行时防御机制，通过在检索块中注入非语义金丝雀 token 并设计双路径完整性博弈（目标路径不应泄露金丝雀 + Oracle 路径应能引出金丝雀），实时检测知识库提取攻击，在不影响任务性能和推理延迟的前提下实现最强防护。

**[DQA: Diagnostic Question Answering for IT Support](information_retrieval/dqa_diagnostic_question_answering_for_it_support.md)**

:   本文提出DQA框架，通过维护持久化的诊断状态和在根因层面聚合检索证据（而非逐文档处理），实现企业IT支持场景下的系统化故障排查，成功率从基线41.3%提升至78.7%，平均轮次从8.4降至3.9。

**[FAITH: Factuality Alignment through Integrating Trustworthiness and Honestness](information_retrieval/faith_factuality_alignment_through_integrating_trustworthiness_and_honestness.md)**

:   本文提出FAITH框架，通过将LLM的不确定性信号（一致性+语义熵）映射到自然语言描述的知识状态象限（可信度×诚实度），设计考虑不确定性的细粒度奖励函数进行PPO训练，再用RAG模块纠正潜在错误，系统性提升LLM的事实准确性。

**[Feedback Adaptation for Retrieval-Augmented Generation](information_retrieval/feedback_adaptation_for_retrieval-augmented_generation.md)**

:   本文提出"反馈适应"作为RAG系统的新问题设定——研究纠正性反馈多快、多有效地传播到未来查询，定义了纠正延迟和反馈后性能两个评估轴，并提出PatchRAG作为免训练的推理时反馈整合方案，实现即时纠正和强泛化。

**[FLARE: Task-Agnostic Embedding Model Evaluation via Normalizing Flows](information_retrieval/flare_task-agnostic_embedding_model_evaluation_through_a_normalization_process.md)**

:   提出FLARE框架，利用正则化流（Normalizing Flows）进行无标签的文本嵌入模型评估，通过直接从对数似然估计信息充分性来避免基于距离的密度估计在高维空间中的崩溃，在11个数据集上与有监督基准的Spearman $\rho$ 达0.90。

**[From Relevance to Authority: Authority-aware Generative Retrieval in Web Search Engines](information_retrieval/from_relevance_to_authority_authority-aware_generative_retrieval_in_web_search_e.md)**

:   本文提出AuthGR，首个将文档权威性系统性整合到生成式检索中的框架，通过VLM多模态权威评分、三阶段渐进式训练（CPT→SFT→GRPO）和混合集成部署管线，在Naver商业搜索引擎的大规模A/B测试中验证了显著的用户参与度提升。

---

## 🦾 LLM Agent { #llm_agent }

**[AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts](llm_agent/agencybench_benchmarking_the_frontiers_of_autonomous_agents_in_1m-token_real-wor.md)**

:   提出AgencyBench——一个包含138个真实世界任务的综合基准，评估6种核心智能体能力，每个场景平均需90次工具调用和100万token，通过用户模拟agent和Docker沙箱实现全自动化评估。

**[CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents](llm_agent/ci-work_benchmarking_contextual_integrity_in_enterprise_llm_agents.md)**

:   基于上下文完整性（Contextual Integrity）理论构建企业场景基准 CI-Work，揭示前沿 LLM 智能体在企业工作流中普遍存在隐私泄漏问题，且模型规模扩大反而加剧泄漏。

**[CodeStruct: Code Agents over Structured Action Spaces](llm_agent/codestruct_code_agents_over_structured_action_spaces.md)**

:   本文提出CodeStruct框架，将代码仓库重新定义为基于AST的结构化动作空间，让LLM代码Agent通过命名的程序实体（而非文本片段）进行读取和编辑操作，在SWE-Bench Verified上提升1.2-5.0%准确率并减少12-38% token消耗。

**[CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution](llm_agent/coevolve_training_llm_agents_via_agent-data_mutual_evolution.md)**

:   CoEvolve 提出**智能体-数据共进化框架**，通过从训练轨迹中提取遗忘/边界/稀有三类弱点信号，引导 LLM 做针对性环境再探索和任务合成，使训练数据分布随智能体能力动态适应，在 AppWorld 和 BFCL 上分别带来 19-23% 的绝对提升。

**[Conjunctive Prompt Attacks in Multi-Agent LLM Systems](llm_agent/conjunctive_prompt_attacks_in_multi-agent_llm_systems.md)**

:   本文研究多智能体 LLM 系统中的联合提示攻击（conjunctive prompt attacks）：用户查询中嵌入的触发键和被入侵远程代理中的隐藏模板各自看起来无害，但当路由将它们带到同一代理时会激活有害行为，现有防御（PromptGuard、Llama-Guard 等）均无法可靠阻止。

**[EA-Agent: A Structured Multi-Step Reasoning Agent for Entity Alignment](llm_agent/ea-agent_a_structured_multi-step_reasoning_agent_for_entity_alignment.md)**

:   提出 EA-Agent，将实体对齐（EA）分解为结构化多步推理过程，通过工具池（三元组选择器+对齐工具+反思器）的规划和执行实现可解释的对齐决策，配合奖励引导的离线策略优化持续改进规划能力，在 DBP15K 上 Hits@1 提升高达 3.17%，同时减少冗余三元组带来的效率问题。

**[FairQE: Multi-Agent Framework for Mitigating Gender Bias in Translation Quality Estimation](llm_agent/fairqe_multi-agent_framework_for_mitigating_gender_bias_in_translation_quality_e.md)**

:   提出 FairQE 多智能体框架，通过性别线索检测、性别翻转变体生成和动态偏见感知分数聚合机制，在不牺牲翻译质量评估准确性的前提下有效缓解 QE 模型中的系统性性别偏见。

**[FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems](llm_agent/fedgui_benchmarking_federated_gui_agents_across_heterogeneous_platforms_devices_.md)**

:   FedGUI 是首个面向跨平台 GUI 代理的联邦学习综合基准，包含六个数据集覆盖移动端/网页端/桌面端，系统研究跨平台、跨设备、跨操作系统和跨数据源四种异构性对联邦 GUI 代理训练的影响。

**[FregeLogic at SemEval 2026 Task 11: A Hybrid Neuro-Symbolic Architecture for Content-Robust Syllogistic Validity Prediction](llm_agent/fregelogic_at_semeval_2026_task_11_a_hybrid_neuro-symbolic_architecture_for_cont.md)**

:   提出 FregeLogic 混合神经符号系统，结合五成员 LLM 集成和 Z3 SMT 求解器作为决胜裁判，在三段论有效性判断中将内容效应降低16%的同时提升准确率0.9%。

**[From Query to Counsel: Structured Reasoning with a Multi-Agent Framework and Dataset for Legal Consultation](llm_agent/from_query_to_counsel_structured_reasoning_with_a_multi-agent_framework_and_data.md)**

:   本文构建了JurisCQAD——一个包含43000+真实中文法律咨询的大规模数据集，并提出JurisMA多智能体框架，通过法律元素图进行结构化任务分解和动态多Agent协作（管理Agent+格式检查+法条检索），在LawBench上显著优于通用和法律专用LLM。

**[JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents](llm_agent/jtpro_a_joint_tool-prompt_reflective_optimization_framework_for_language_agents.md)**

:   JTPRO 提出了一种无需模型微调的联合优化框架，通过反思驱动的迭代编辑同时优化全局指令和逐工具的 schema/参数描述，在大规模工具库场景下显著提升工具选择和参数填充的端到端成功率，相比 GEPA 等基线在 OSR 上提升 5%–20%。

**[When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors](llm_agent/when_agents_look_the_same_quantifying_distillation-induced_similarity_in_tool-us.md)**

:   本文提出了 RPS 和 AGS 两个互补指标来量化 LLM Agent 在工具使用行为上的蒸馏导致的同质化现象，通过区分必要行为和非必要行为，在 18 个模型上揭示了跨家族行为继承模式，发现 Kimi-K2 与 Claude Sonnet 4.5 的行为相似度甚至超过 Anthropic 自家模型。

---

## 🧑 人体理解 { #human_understanding }

**[Agentic Conversational Search with Contextualized Reasoning via Reinforcement Learning](human_understanding/agentic_conversational_search_with_contextualized_reasoning_via_reinforcement_le.md)**

:   提出ConvAgent，通过将RL训练奖励分解为结果奖励、信息增益奖励和混合主动行为奖励三个互补组件，训练对话式搜索智能体在多轮交互中交替进行搜索和推理。

**[Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning](human_understanding/bridging_sft_and_rl_dynamic_policy_optimization_for_robust_reasoning.md)**

:   提出 DYPO（Dynamic Policy Optimization），通过动态难度分级将样本路由到不同优化路径——Hard样本用多教师蒸馏降低SFT偏差、Mid样本用Group Alignment Loss降低RL方差，在数学推理benchmark上平均提升4.8%，OOD任务提升13.3%。

**[CAP: Controllable Alignment Prompting for Unlearning in LLMs](human_understanding/cap_controllable_alignment_prompting_for_unlearning_in_llms.md)**

:   提出 CAP 框架，通过训练轻量 SLM 生成可控的提示前缀来引导冻结的 LLM 选择性遗忘目标知识，无需修改模型参数，实现了可逆、可迁移的 LLM 知识遗忘。

**[Cross-Modal Taxonomic Generalization in (Vision-) Language Models](human_understanding/cross-modal_taxonomic_generalization_in_vision-_language_models.md)**

:   本文系统研究 VLM 中语言模型是否能将纯文本习得的分类学知识（上位词关系）跨模态泛化到视觉输入，发现即使训练时完全不提供上位词标签，预训练 LM 仍能在图像中识别上位词类别，但这种泛化需要类别成员在视觉上的一致性。

**[Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views](human_understanding/discovering_a_shared_logical_subspace_steering_llm_logical_reasoning_via_alignme.md)**

:   发现 LLM 内部存在一个共享的逻辑子空间，可同时对齐自然语言和符号逻辑两种推理表示，通过在推理时沿该子空间引导激活可无训练提升逻辑推理准确率最高达 11 个百分点。

**[Dynamics of Cognitive Heterogeneity: Investigating Behavioral Biases in Multi-Stage Supply Chains with LLM-Based Simulation](human_understanding/dynamics_of_cognitive_heterogeneity_investigating_behavioral_biases_in_multi-sta.md)**

:   使用LLM智能体（DeepSeek/GPT系列）在经典啤酒分销博弈中模拟多阶段供应链，系统研究认知异质性（推理能力差异）对系统行为的影响，发现LLM智能体能复现人类的牛鞭效应和短视行为，且信息共享能有效缓解这些不良效应。

**[Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization](human_understanding/enhancing_llm-based_search_agents_via_contribution_weighted_group_relative_polic.md)**

:   CW-GRPO 将过程监督重新定义为"优势重分配"：用 LLM 判断器评估每轮搜索的检索有用性和推理正确性，计算贡献分数来缩放基于结果的优势，实现轮级别信用分配而不引入不稳定的价值函数，在 Qwen3-8B 上超越标准 GRPO 5.0%。

**[Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation](human_understanding/planning_beyond_text_graph-based_reasoning_for_complex_narrative_generation.md)**

:   本文提出 PLOTTER 框架，首次将叙事规划从文本表示转移到图结构表示（事件图+角色图），通过多 agent 的 Evaluate-Plan-Revise 迭代循环在图拓扑上诊断和修复叙事缺陷，在叙事性、角色塑造、戏剧张力等维度上显著优于现有方法。

**[Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](human_understanding/revisiting_non-verbatim_memorization_in_large_language_models_the_role_of_entity.md)**

:   本文通过构建 RedirectQA 数据集（利用 Wikipedia 重定向信息将同一实体关联到多种表面形式），系统研究了 LLM 的非逐字记忆如何受实体命名变体的影响，发现事实记忆既非纯粹依赖特定表面形式也非完全表面无关，且实体级频率在表面频率之外仍有独立贡献。

**[The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models](human_understanding/the_gaoyao_benchmark_a_comprehensive_framework_for_evaluating_multilingual_and_m.md)**

:   本文提出GaoYao基准，包含182.3K样本、26种语言和51个国家/地区，通过三层文化评估框架（通用多语言/跨文化/单文化）和九个认知子层，结合人工本地化的主观测试集和专家验证的跨文化合成数据集SuperBLEnD，深度诊断20+旗舰与紧凑型LLM的多语言能力，揭示了显著的地理数字鸿沟和任务能力分层。

---

## 🎯 目标检测 { #object_detection }

**[Anchored Cyclic Generation: A Novel Paradigm for Long-Sequence Symbolic Music Generation](object_detection/anchored_cyclic_generation_a_novel_paradigm_for_long-sequence_symbolic_music_gen.md)**

:   本文提出锚定循环生成（ACG）范式，通过在自回归过程中用已确认的音乐内容作为锚点来校准生成方向，有效缓解长序列符号音乐生成中的误差累积问题，并构建了层次化框架Hi-ACG实现从全局到局部的音乐生成。

**[AnchorMem: Anchored Facts with Associative Contexts for Building Memory in Large Language Models](object_detection/anchormem_anchored_facts_with_associative_contexts_for_building_memory_in_large_.md)**

:   提出AnchorMem记忆框架，受普鲁斯特现象启发，将检索单元（原子事实）与生成上下文（原始交互）解耦，通过关联事件图连接碎片化记忆，在LoCoMo基准上大幅超越A-Mem、Mem0等现有记忆系统。

**[Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models](object_detection/breaking_block_boundaries_anchor-based_history-stable_decoding_for_diffusion_lar.md)**

:   提出 AHD（Anchor-based History-stable Decoding），一种无需训练的即插即用动态解码策略，通过动态锚点回溯历史轨迹判定扩散LLM中跨块稳定token，实现早期解锁，在BBH上减少80%解码步数的同时提升3.67%性能。

**[Debating the Unspoken: Role-Anchored Multi-Agent Reasoning for Half-Truth Detection](object_detection/debating_the_unspoken_role-anchored_multi-agent_reasoning_for_half-truth_detecti.md)**

:   提出RADAR框架，通过角色锚定（政客 vs 科学家）的多智能体辩论来检测基于遗漏上下文的半真半假信息，配合双阈值自适应早停机制，在噪声检索条件下一致超越单智能体和传统多智能体基线。

**[E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition](object_detection/e2e-gmner_end-to-end_generative_grounded_multimodal_named_entity_recognition.md)**

:   提出E2E-GMNER，首个将实体识别、语义分类、视觉定位和隐式知识推理统一在单一多模态大语言模型中的端到端GMNER框架，通过CoT推理自适应判断视觉/知识线索的可用性，并引入高斯风险感知框扰动（GRBP）提升生成式框预测的鲁棒性。

**[Evaluating Memory Capability in Continuous Lifelog Scenario](object_detection/evaluating_memory_capability_in_continuous_lifelog_scenario.md)**

:   本文提出LifeDialBench，一个评估连续生活日志场景下记忆能力的基准（含7天真实数据的EgoMem和1年模拟的LifeMem），引入在线评估协议确保时间因果性，反直觉地发现简单RAG基线一致优于复杂记忆系统。

**[Evolutionary Negative Module Pruning for Better LoRA Merging](object_detection/evolutionary_negative_module_pruning_for_better_lora_merging.md)**

:   提出 ENMP 方法，通过进化搜索策略发现并剪除 LoRA 合并中降低性能的"负面模块"，作为即插即用的增强手段，在 NLP 和视觉领域全面提升现有合并算法的效果。

**[GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization](object_detection/gigacheck_detecting_llm-generated_content_via_object-centric_span_localization.md)**

:   提出 GigaCheck，一个双策略框架：文档级使用微调 LLM 进行分类，片段级创新地将 AI 生成文本片段视为"目标"，用 DETR-like 架构实现端到端的字符级定位。

**[HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents](object_detection/higmem_a_hierarchical_and_llm-guided_memory_system_for_long-term_conversational_.md)**

:   本文提出 HiGMem，一个两层事件-对话轮记忆系统，通过让 LLM 先浏览事件摘要再预测哪些细粒度对话轮值得读取，在 LoCoMo10 基准上以少一个数量级的检索量达到了五类问题中四类的最优 F1。

**[StructMem: Structured Memory for Long-Horizon Behavior in LLMs](object_detection/structmem_structured_memory_for_long-horizon_behavior_in_llms.md)**

:   StructMem 提出了一种结构增强的层次化记忆框架，通过事件级双视角提取和跨事件语义整合，在 LoCoMo 长对话基准上实现 SOTA 性能（76.82%），同时大幅降低 token 消耗（1.94M vs. 图记忆的 35.8M）和 API 调用次数。

---

## 🔬 可解释性 { #interpretability }

**[A Structured Clustering Approach for Inducing Media Narratives](interpretability/a_structured_clustering_approach_for_inducing_media_narratives.md)**

:   提出一个从大规模新闻语料中自动归纳媒体叙事模式的框架，通过联合建模事件因果链和角色（英雄/威胁/受害者）信息，使用角色约束的聚类算法将叙事链组织成语义连贯的叙事模式，在移民和枪支控制两个领域生成了可解释且与框架理论一致的叙事模式。

**[ChemVLR: Prioritizing Reasoning in Perception for Chemical Vision-Language Understanding](interpretability/chemvlr_prioritizing_reasoning_in_perception_for_chemical_vision-language_unders.md)**

:   提出 ChemVLR，首个化学领域推理型 VLM，通过跨模态逆向工程策略构建 760K 推理数据集，结合持续预训练-SFT-RL 三阶段训练流程，在分子识别和反应预测任务上显著超越专有模型和领域专家 VLM。

**[Context-Value-Action Architecture for Value-Driven Large Language Model Agents](interpretability/context-value-action_architecture_for_value-driven_large_language_model_agents.md)**

:   提出 CVA（Context-Value-Action）架构，基于 S-O-R 心理学模型和 Schwartz 价值理论，通过训练在真实人类数据上的 Value Verifier 解耦行为生成与认知推理，有效缓解 LLM 智能体的行为极化问题，在超过 110 万真实交互轨迹的 CVABench 上显著优于基线。

**[Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations](interpretability/do_llms_know_tool_irrelevance_demystifying_structural_alignment_bias_in_tool_inv.md)**

:   发现并形式化了 LLM 工具调用中的"结构对齐偏差"——当查询属性可以有效映射到工具参数时（即使工具功能与用户目标无关），LLM 仍倾向调用该工具。构建 SABEval 数据集解耦结构对齐和语义相关性，用对比注意力归因揭示内部存在语义检查和结构匹配两条竞争路径，提出再平衡策略实现 80% 的相对错误减少。

**[Evian: Towards Explainable Visual Instruction-tuning Data Auditing](interpretability/evian_towards_explainable_visual_instruction-tuning_data_auditing.md)**

:   提出"分解-再评估"（Decomposition-then-Evaluation）范式和 EVIAN 框架，将视觉指令微调数据的回答分解为视觉描述、主观推理和事实声明三个组件，沿图文一致性、逻辑连贯性和事实准确性三个正交维度评估，发现用其筛选的少量高质量数据训练的模型优于大规模数据集训练的模型。

**[Experiments or Outcomes? Probing Scientific Feasibility in Large Language Models](interpretability/experiments_or_outcomes_probing_scientific_feasibility_in_large_language_models.md)**

:   构建控制知识框架系统研究LLM在科学可行性评估中如何利用实验描述和结果证据，发现提供结果证据比实验描述更可靠，部分实验信息常导致性能低于仅用参数知识的基线，揭示了LLM推理的脆弱性。

**[From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization](interpretability/from_signal_degradation_to_computation_collapse_uncovering_the_two_failure_modes.md)**

:   本文通过系统的机械可解释性分析，揭示LLM量化存在两种质性不同的失败模式：4-bit的信号退化（Signal Degradation，计算模式完整但精度受损，可局部修复）和2-bit的计算崩溃（Computation Collapse，关键组件功能性破坏，需结构重建）。

**[SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks](interpretability/spence_a_syntactic_probe_for_detecting_contamination_in_nl2sql_benchmarks.md)**

:   SPENCE 通过对 NL2SQL 基准查询进行系统性句法改写并测量执行准确率随句法距离的衰减程度，检测和量化 LLM 在 NL2SQL 基准上的数据污染行为，发现越老的基准（如 Spider）污染信号越强，而较新的 BIRD 基准几乎不受影响。

**[Tracing Relational Knowledge Recall in Large Language Models](interpretability/tracing_relational_knowledge_recall_in_large_language_models.md)**

:   本文系统研究LLM在文本生成过程中回忆关系知识的内部机制，发现注意力头对残差流的逐头贡献（$\Delta_{att,h}$）是线性关系分类的最强特征（准确率达91%），并提出HeadScore和TokenScore两种探针归因方法来分解预测到注意力头和源token级别，揭示了探针精度与关系特异性、实体连通度及探针信号集中度之间的明确相关性。

---

## 💡 LLM推理 { #llm_reasoning }

**[AIM-CoT: Active Information-driven Multimodal Chain-of-Thought for Vision-Language Reasoning](llm_reasoning/aim-cot_active_information-driven_multimodal_chain-of-thought_for_vision-languag.md)**

:   提出 AIM-CoT 框架，通过信息觅食理论驱动的主动视觉证据选择(AVP)和基于注意力偏移的动态触发机制(DAT)，解决交错模态思维链(I-MCoT)中"看什么"和"何时看"两个核心问题。

**[Dissecting Failure Dynamics in Large Language Model Reasoning](llm_reasoning/dissecting_failure_dynamics_in_large_language_model_reasoning.md)**

:   通过分析 LLM 推理轨迹，发现错误集中在早期的少数关键转折点，错误发生后模型进入"认知螺旋"——局部连贯但全局错误地不断延伸；基于此提出 GUARD 框架，在熵信号检测到的高风险转折点处进行短距分支修复。

**[DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency](llm_reasoning/dpc_training-free_text-to-sql_candidate_selection_via_dual-paradigm_consistency.md)**

:   DPC 将 Text-to-SQL 的候选选择从"在隐藏数据上猜测"转化为"在可见数据上确定性验证"：构造最小区分数据库（MDD）使冲突 SQL 产生不同结果，再用 Python/Pandas 解作为参考锚点通过跨范式一致性选择正确候选，在 BIRD 和 Spider 上超越 Self-Consistency 最高 2.2%。

**[Efficient Process Reward Modeling via Contrastive Mutual Information](llm_reasoning/efficient_process_reward_modeling_via_contrastive_mutual_information.md)**

:   提出 CPMI（Contrastive Pointwise Mutual Information），一种高效的自动步级奖励标注方法，通过对比推理步骤对正确答案和错误答案的条件概率变化量来估计步级贡献，比 Monte Carlo 估计减少 84% 构建时间和 98% token 生成量，同时在过程级评估和数学推理基准上取得更高准确率。

**[Explicit Trait Inference for Multi-Agent Coordination](llm_reasoning/explicit_trait_inference_for_multi-agent_coordination.md)**

:   提出显式特质推理（ETI）方法，基于心理学中温暖和能力两个维度让LLM智能体推理并追踪合作伙伴的行为特征，在经济博弈中减少45-77%收益损失，在MultiAgentBench上提升3-29%任务表现。

**[Generating Effective CoT Traces for Mitigating Causal Hallucination](llm_reasoning/generating_effective_cot_traces_for_mitigating_causal_hallucination.md)**

:   本文首先提出了因果幻觉率（CHR）指标来量化小型 LLM 在事件因果识别中过度预测因果关系的倾向，然后通过系统实验确定了有效 CoT 数据的两个关键标准（充分长度的语义解释+与目标模型对齐的分布），设计了一套低成本的 CoT 数据生成管线，将 Qwen2.5-1.5B 的 CHR 从 83.54% 降至 6.26%，同时提升平均准确率至 66.00%。

**[Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards](llm_reasoning/process_reward_models_meet_planning_generating_precise_and_scalable_datasets_for.md)**

:   本文提出利用规划领域定义语言（PDDL）自动生成大规模、高精度的步骤级奖励数据集，用于训练过程奖励模型（PRM），在数学和非数学推理基准上均取得显著提升。

**[ReCoQA: A Benchmark for Tool-Augmented and Multi-Step Reasoning in Real Estate Question and Answering](llm_reasoning/recoqa_a_benchmark_for_tool-augmented_and_multi-step_reasoning_in_real_estate_qu.md)**

:   本文构建了 ReCoQA——一个包含 29,270 个房地产问答对的大规模基准，要求模型融合数据库查询和地图 API 调用进行混合多源推理，并提出层次化多 Agent 框架 HIRE-Agent 作为强基线，系统性地揭示了现有 LLM 在垂直领域复杂推理中的瓶颈。

**[Semantic-Aware Logical Reasoning via a Semiotic Framework](llm_reasoning/semantic-aware_logical_reasoning_via_a_semiotic_framework.md)**

:   提出 LogicAgent，一个基于格雷马斯符号方阵(Semiotic Square)的逻辑推理框架，通过多视角语义分析和反思验证，在语义复杂和逻辑复杂双重挑战下实现 SOTA 逻辑推理性能。

---

## 💻 代码智能 { #code_intelligence }

**[Across Programming Language Silos: A Study on Cross-Lingual Retrieval-Augmented Code Generation](code_intelligence/across_programming_language_silos_a_study_on_cross-lingual_retrieval-augmented_c.md)**

:   首次系统研究跨编程语言的检索增强代码生成（RACG），构建覆盖13种编程语言的14K实例数据集，揭示跨语言知识迁移的不对等性及其与语言亲缘性和预训练多样性的关系。

**[DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation](code_intelligence/deepguard_secure_code_generation_via_multi-layer_semantic_aggregation.md)**

:   提出 DeepGuard，通过注意力机制聚合 Transformer 上层多层表示克服"最终层瓶颈"问题，结合多目标训练和轻量推理时安全引导策略，在 5 个代码 LLM 上将安全-正确生成率平均提升 11.9%。

**[From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation](code_intelligence/from_if-statements_to_ml_pipelines_revisiting_bias_in_code-generation.md)**

:   揭示LLM代码生成的偏差评估严重低估了实际风险：在ML流水线生成中，敏感属性出现在87.7%的特征选择中（vs 条件语句中的59.2%），且模型能正确排除无关特征但仍选择保留种族、性别等敏感属性，显示出系统性的隐性歧视。

**[River-LLM: Large Language Model Seamless Exit Based on KV Share](code_intelligence/river-llm_large_language_model_seamless_exit_based_on_kv_share.md)**

:   本文提出 River-LLM，一个无需训练的框架，通过构建轻量级 KV 共享退出通道（Exit River）解决了 decoder-only 架构中 Early Exit 的 KV Cache 缺失问题，利用状态转换相似度引导退出决策，实现 1.71×-2.16× 的实际推理加速且保持近无损生成质量。

**[SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution](code_intelligence/solidcoder_bridging_the_mental-reality_gap_in_llm_code_generation_through_concre.md)**

:   SolidCoder 通过 S.O.L.I.D. 架构（Shift-left Planning、Oracle-based Assertions、Live Execution、Intermediate Simulation、Defensive Accumulation）将代码验证从 LLM 的"想象执行"转变为"真实执行"，在 GPT-4o 上达到 HumanEval 95.7%、CodeContests 77.0%、APPS 26.7% 的 pass@1 性能。

**[The Path Not Taken: Duality in Reasoning about Program Execution](code_intelligence/the_path_not_taken_duality_in_reasoning_about_program_execution.md)**

:   本文提出程序执行推理的对偶性概念，通过DexBench基准（445个配对实例）联合评估LLM的正向执行推理（预测给定输入下的代码覆盖）和反向反事实推理（推断使执行流转向目标分支的输入变异），发现单一方向上的强表现不能转化为联合评估下的成功，揭示了模型对程序因果理解的不足。

---

## 📊 LLM评测 { #llm_evaluation }

**[Beyond Reproduction: A Paired-Task Framework for Assessing LLM Comprehension and Creativity in Literary Translation](llm_evaluation/beyond_reproduction_a_paired-task_framework_for_assessing_llm_comprehension_and_.md)**

:   提出配对任务框架联合评估 LLM 的文学文本理解能力和翻译创造力，基于 11 本英文经典小说对 23 个模型进行大规模测评，发现强理解力并不能转化为人类水平的翻译创造力。

**[CAST: Achieving Stable LLM-based Text Analysis for Data Analytics](llm_evaluation/cast_achieving_stable_llm-based_text_analysis_for_data_analytics.md)**

:   提出CAST框架，通过算法提示（Algorithmic Prompting）和先思考后输出（Thinking-before-Speaking）两种机制约束LLM的潜在推理路径，显著提升文本摘要和标注任务的运行间稳定性，同时不损失输出质量。

**[Exploring the Capability Boundaries of LLMs in Mastering of Chinese Chouxiang Language](llm_evaluation/exploring_the_capability_boundaries_of_llms_in_mastering_of_chinese_chouxiang_la.md)**

:   本文将中文互联网亚文化语言"抽象话"引入 NLP 社区，构建首个评估基准 Mouse（含翻译、表征分类、意图识别、毒性检测、含义选择、完形填空六个任务），发现 SOTA LLM 在上下文语义理解上表现尚可但在其他任务上存在明显局限。

**[Self-Awareness before Action: Mitigating Logical Inertia via Proactive Cognitive Awareness](llm_evaluation/self-awareness_before_action_mitigating_logical_inertia_via_proactive_cognitive_.md)**

:   本文提出 SABA 推理框架，通过"先感知再行动"的范式，在做出最终决策前显式构建和审计知识状态——利用信息融合 (IF) 将叙事整合为可验证的基线状态，再通过查询驱动的结构化推理 (QSR) 递归识别和解决缺失前提——在侦探推理和通用推理基准上均取得最佳表现。

**[Subject-level Inference for Realistic Text Anonymization Evaluation](llm_evaluation/subject-level_inference_for_realistic_text_anonymization_evaluation.md)**

:   SPIA 提出首个主体级 PII 推断评估基准（675 篇文档、1712 个主体、7040 个 PII），揭示即使 90%+ 的 PII 片段被遮蔽，主体级推断保护率可低至 33%，且聚焦单一目标主体的匿名化会导致非目标主体暴露更多。

**[Text-to-Distribution Prediction with Quantile Tokens and Neighbor Context](llm_evaluation/text-to-distribution_prediction_with_quantile_tokens_and_neighbor_context.md)**

:   本文提出Quantile Token Regression方法，通过在输入序列中插入专用分位数token并结合检索到的邻居实例及其经验分布，使LLM能够预测完整的条件分布而非单一点估计，在Airbnb和StackSample数据集上相比基线降低约4个MAPE点并将预测区间收窄2倍以上。

---

## 💬 LLM/NLP { #llm_nlp }

**[A Study of LLMs' Preferences for Libraries and Programming Languages](llm_nlp/a_study_of_llms39_preferences_for_libraries_and_programming_languages.md)**

:   首次系统研究8个LLM在代码生成中对库和编程语言的偏好行为，发现LLM严重偏好NumPy等流行库（45%的使用不必要）和Python语言（58%的高性能任务仍选Python），且自然语言推荐与实际代码选择不一致。

**[Adam's Law: Textual Frequency Law on Large Language Models](llm_nlp/adam39s_law_textual_frequency_law_on_large_language_models.md)**

:   本文提出"文本频率定律"（TFL），发现当语义相同时，使用更高频率的文本表达来提示或微调LLM能获得更好效果，并设计了频率蒸馏和课程训练策略来进一步利用该规律。

**[An Existence Proof for Neural Language Models That Can Explain Garden-Path Effects via Surprisal](llm_nlp/an_existence_proof_for_neural_language_models_that_can_explain_garden-path_effec.md)**

:   通过在花园路径句上微调神经语言模型，证明了存在一个神经 LM 能够通过惊奇度（surprisal）同时解释花园路径效应和自然阅读时间，为惊奇度理论提供了存在性证明。

**[CoSToM: Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models](llm_nlp/costomcausal-oriented_steering_for_intrinsic_theory-of-mind_alignment_in_large_l.md)**

:   提出 CoSToM 框架，先用因果追踪定位 LLM 中编码心智理论（ToM）特征的关键层（发现主要在早期层），再通过激活转向在这些层上进行轻量级对齐，使 LLM 在谈判和说服对话中显著提升社会推理质量——从"知道但不会用"变为"知道且会用"。

**[EvoSpark: Endogenous Interactive Agent Societies for Unified Long-Horizon Narrative Evolution](llm_nlp/evospark_endogenous_interactive_agent_societies_for_unified_long-horizon_narrati.md)**

:   EvoSpark 提出一个支持长程叙事演化的多智能体框架，通过分层递归记忆（RSB 做社会认知代谢）、生成式场面调度（GMS 做角色-地点-情节对齐）和涌现角色锚定协议（ECGP 将 LLM 幻觉转化为持久角色）三重设计解决社会记忆堆叠和叙事-空间失谐问题。

**[FastDiSS: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation](llm_nlp/fastdiss_few-step_match_many-step_diffusion_language_model_on_sequence-to-sequen.md)**

:   本文分析了连续扩散语言模型在少步采样时自条件化信号的不匹配和训练饱和两个瓶颈，提出FastDiSS框架通过自条件化扰动（SCP）和模型感知噪声缩放（MANS）来改善鲁棒性，在6个基准上实现4×-400×加速同时保持质量。

---

## 🎵 音频/语音 { #audio_speech }

**[Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations](audio_speech/affectron_emotional_speech_synthesis_with_affective_and_contextually_aligned_non.md)**

:   本文提出 Affectron 框架，通过情感驱动的 Top-K NV 匹配和情感感知的 Top-K 路由两个训练时增强策略，在小规模开源解耦语料上实现了多样且情感对齐的非语言发声（如笑声、叹息）合成，显著超越了基于纯语言预训练的 VoiceCraft 基线。

**[Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](audio_speech/beyond_transcription_unified_audio_schema_for_perception-aware_audiollms.md)**

:   揭示当前 AudioLLM 的感知弱点源于 ASR 中心的训练范式（系统性抑制副语言和非语言信息），提出 Unified Audio Schema（UAS）将音频信息结构化为转录、副语言和非语言事件三个维度的 JSON 格式，在 MMSU 基准上感知精度提升 10.9% 同时保持推理能力。

**[Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models](audio_speech/do_we_need_distinct_representations_for_every_speech_token_unveiling_and_exploit.md)**

:   本文通过逐层oracle干预实验揭示了大语音语言模型（LSLM）中语音token表示的结构化冗余层次——浅层编码必要声学细节而深层极度冗余——并提出Affinity Pooling这一免训练的基于相似度的token合并机制，在减少27.48% FLOPs的同时保持竞争力的准确率。

**[Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages](audio_speech/hard_to_be_heard_phoneme-level_asr_analysis_of_phonologically_complex_low-resour.md)**

:   本文对两种音系极端复杂的低资源濒危东高加索语言（Archi和Rutul）进行音素级ASR分析，发现音素识别准确率与训练频率呈S型学习曲线关系，许多归因于音系复杂性的错误实际上更多源于数据稀缺。

---

## 🔗 因果推理 { #causal_inference }

**[Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size](causal_inference/better_and_worse_with_scale_how_contextual_entrainment_diverges_with_model_size.md)**

:   本文首次为"上下文夹带效应"（contextual entrainment）建立缩放定律，发现更大的模型在语义上下文中更能抵抗虚假信息（负指数），但在非语义上下文中更容易复制无关 token（正指数），揭示了语义过滤和机械复制两种功能的对立缩放行为。

**[CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification](causal_inference/causaldetox_causal_head_selection_and_intervention_for_language_model_detoxifica.md)**

:   CausalDetox 使用"必要性和充分性概率"（PNS）作为因果准则来精确定位产生有毒内容的注意力头，并通过局部推理时干预和 PNS 引导的微调两种互补策略进行去毒化，在多个模型上实现最高 5.34% 的毒性降低，同时保持语言流畅性。

**[ClimateCause: Complex and Implicit Causal Structures in Climate Reports](causal_inference/climatecause_complex_and_implicit_causal_structures_in_climate_reports.md)**

:   ClimateCause 构建了首个针对气候报告中复杂和隐式因果结构的专家标注数据集（874 条因果关系），支持嵌套因果、多事件拆解、相关性方向和时空语境标注，并提出基于因果图语义复杂度的可读性度量，LLM 基准测试显示因果链推理仍是重要挑战。

**[Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate](causal_inference/dialectic-med_mitigating_diagnostic_hallucinations_via_counterfactual_adversaria.md)**

:   提出 Dialectic-Med，一个受波普尔证伪主义启发的多智能体医学诊断框架，通过提议者（诊断假设）、反对者（视觉证伪模块主动检索矛盾视觉证据）和调解者（加权共识图决策）的对抗辩证推理，在 MIMIC-CXR-VQA、VQA-RAD 和 PathVQA 上取得 SOTA，解释忠实度提升 12.5%，显著缓解诊断幻觉。

---

## 🎮 强化学习 { #reinforcement_learning }

**[A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions](reinforcement_learning/a_survey_of_reinforcement_learning_for_large_language_models_under_data_scarcity.md)**

:   首篇系统综述数据稀缺条件下LLM强化学习的工作，提出数据中心、训练中心、框架中心三层分类体系，覆盖数据剪枝/合成/压缩、轨迹生成/奖励工程/策略优化、以及自演化/协同演化/多智能体演化等方向。

**[Adaptive Instruction Composition for Automated LLM Red-Teaming](reinforcement_learning/adaptive_instruction_composition_for_automated_llm_red-teaming.md)**

:   提出 Adaptive Instruction Composition (AIC) 框架，利用 Neural Thompson Sampling 在众包有害查询和越狱策略的组合空间中自适应地选择攻击指令，同时优化攻击成功率和多样性，在 Harmbench 上大幅超越已有方法。

**[AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation](reinforcement_learning/aj-bench_benchmarking_agent-as-a-judge_for_environment-aware_evaluation.md)**

:   提出 AJ-Bench，首个系统评估 Agent-as-a-Judge 能力的基准，覆盖搜索、数据系统和 GUI 三个领域共 155 个任务和 516 条标注轨迹，实验表明 Agent-as-a-Judge 比 LLM-as-a-Judge 平均 F1 提升约 13 个百分点。

**[Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study](reinforcement_learning/scaling_behaviors_of_llm_reinforcement_learning_post-training_an_empirical_study.md)**

:   首次系统研究 LLM 强化学习后训练的缩放行为，在 Qwen2.5 系列(0.5B-72B)上发现性能与训练资源之间遵循幂律关系，且学习效率随模型规模增大呈饱和趋势。

---

## 🛡️ AI安全 { #ai_safety }

**[Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization](ai_safety/adaptive_text_anonymization_learning_privacy-utility_trade-offs_via_prompt_optim.md)**

:   提出自适应文本匿名化框架，通过进化式提示优化自动为LLM发现任务特定的匿名化指令，在多个隐私-效用权衡场景中超越手工设计的策略，且可在开源模型上运行。

**[Beyond End-to-End: Dynamic Chain Optimization for Private LLM Adaptation on the Edge](ai_safety/beyond_end-to-end_dynamic_chain_optimization_for_private_llm_adaptation_on_the_e.md)**

:   提出 ChainFed，一种打破内存墙的链式联邦微调范式，通过逐层顺序训练-冻结适配器使资源受限边缘设备也能参与 LLM 微调，结合动态层协调、全局感知优化和功能导向自适应三项技术，平均准确率提升最高 46.46%。

**[Indic-CodecFake meets SATYAM: Towards Detecting Neural Audio Codec Synthesized Speech Deepfakes in Indic Languages](ai_safety/indic-codecfake_meets_satyam_towards_detecting_neural_audio_codec_synthesized_sp.md)**

:   本文构建了首个多印度语言的 CodecFake 检测基准 ICF，并提出 SATYAM——一个双曲音频大语言模型，通过在双曲空间中用 Bhattacharyya 距离对齐语义和副语言表示再与提示对齐，仅训练 3.75M 参数即达到 98.32% 的检测准确率。

---

## 🎨 图像生成 { #image_generation }

**[AFMRL: Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce](image_generation/afmrl_attribute-enhanced_fine-grained_multi-modal_representation_learning_in_e-c.md)**

:   提出 AFMRL 框架，将电商产品的细粒度理解定义为属性生成任务，通过 MLLM 生成关键属性来增强对比学习（AGCL），并用检索性能作为奖励信号反向优化属性生成器（RAR），在大规模电商数据集上实现 SOTA 检索性能。

**[BookAgent: Orchestrating Safety-Aware Visual Narratives via Multi-Agent Cognitive Calibration](image_generation/bookagent_orchestrating_safety-aware_visual_narratives_via_multi-agent_cognitive.md)**

:   BookAgent 是一个安全感知的多智能体框架，通过**价值对齐故事板（VAS）+ 迭代跨模态精炼（ICR）+ 时序认知校准（TCC）**三阶段闭环架构，从用户草稿端到端生成高质量、角色一致、内容安全的绘本故事。

**[Follow the Flow: On Information Flow Across Textual Tokens in Text-to-Image Models](image_generation/follow_the_flow_on_information_flow_across_textual_tokens_in_text-to-image_model.md)**

:   本文通过因果干预框架系统研究了文本到图像模型中文本编码器输出的 token 级信息分布，发现词汇项的语义通常集中在 1-2 个代表性 token 上，且跨项信息流在 11% 的情况下会导致语义泄漏和图像错误解读，并提出了简单有效的 token 级干预方法来改善对齐。

---

## ⚡ LLM效率 { #llm_efficiency }

**[Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL](llm_efficiency/abstain-r1_calibrated_abstention_and_post-refusal_clarification_via_verifiable_r.md)**

:   Abstain-R1 提出一种**澄清感知的 RLVR 奖励**，在不可回答查询上联合优化"明确拒答"和"拒答后给出有用澄清（指出缺失信息）"，使 3B 模型在拒答和澄清质量上接近甚至超越 DeepSeek-R1 等大模型。

**[BOSCH: Black-Box Binary Optimization for Short-Context Attention-Head Selection in LLMs](llm_efficiency/bosch_black-box_binary_optimization_for_short-context_attention-head_selection_i.md)**

:   提出 BOSCH，一种免训练的注意力头级别 SWA 混合方法，将 SWA 头选择建模为大邻域搜索问题并分解为三阶段优化（层重要性探测→自适应比例分配→分组头选择），在 4 个模型 4 种比例设置下系统性超越层级启发式和 6 种静态头级别方法。

**[Forget What Matters, Keep the Rest: Selective Unlearning of Informative Tokens](llm_efficiency/forget_what_matters_keep_the_rest_selective_unlearning_of_informative_tokens.md)**

:   提出 Entropy-guided Token Weighting (ETW)，利用预测分布的熵值作为 token 信息量的代理指标，选择性地对信息性 token 施加更强的遗忘惩罚，在有效遗忘目标知识的同时更好地保持模型通用能力。

---

## 🌐 多语言/翻译 { #multilingual_mt }

**[A Multilingual Dataset and Empirical Validation for the Mutual Reinforcement Effect in Information Extraction](multilingual_mt/a_multilingual_dataset_and_empirical_validation_for_the_mutual_reinforcement_eff.md)**

:   构建首个多语言MRE Mix数据集（MMM，21个子集覆盖英中日），并通过大规模消融实验系统验证了词级与文本级信息抽取任务的互增强效应（MRE）跨语言普遍存在。

**[BhashaSutra: A Task-Centric Unified Survey of Indian NLP Datasets, Corpora, and Resources](multilingual_mt/bhashasutra_a_task-centric_unified_survey_of_indian_nlp_datasets_corpora_and_res.md)**

:   首篇专门针对印度语言NLP资源的统一综述，覆盖200+数据集、50+基准、100+模型/工具，按17个任务类别组织（从核心语言处理到社会文化任务），系统分析了语言覆盖不均、标注碎片化、评估不一致等持续挑战。

**[Efficient Training for Cross-lingual Speech Language Models](multilingual_mt/efficient_training_for_cross-lingual_speech_language_models.md)**

:   本文提出CSLM，一种高效训练跨语言语音LLM的方法，通过新颖的对齐策略实现跨模态和跨语言对齐，并引入语音-文本交织链式模态生成来提升质量和降低延迟，无需大规模语音数据即可扩展到新语言。

---

## 🎁 推荐系统 { #recommender }

**[Content Fuzzing for Escaping Information Cocoons on Social Media](recommender/content_fuzzing_for_escaping_information_cocoons_on_digital_social_media.md)**

:   提出 ContentFuzz，一个从内容创作者视角出发的置信度引导模糊测试框架，通过 LLM 改写帖子使其在保持人类解读含义不变的前提下改变机器推断的立场标签，从而突破社交媒体信息茧房。

**[From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](recommender/from_recall_to_forgetting_benchmarking_long-term_memory_for_personalized_agents.md)**

:   本文提出Memora基准和FAMA指标，将长期记忆评估从浅层事实检索扩展到跨越数周至数月的记忆整合与突变处理，揭示现有LLM和记忆agent在处理频繁知识更新时的系统性失败。

**[IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters](recommender/icebreaker_for_conversational_agents_breaking_the_first-message_barrier_with_per.md)**

:   本文提出 IceBreaker，通过两步"握手"——共鸣感知兴趣蒸馏捕获触发兴趣 + 交互导向启动语生成配合个性化偏好对齐——解决对话智能体的"首条消息壁垒"，在全球最大对话产品之一的 A/B 测试中提升用户活跃天数 +1.84‰ 和点击率 +94.25‰。

---

## 🔎 AIGC检测 { #aigc_detection }

**[Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection](aigc_detection/beyond_the_final_actor_modeling_the_dual_roles_of_creator_and_editor_for_fine-gr.md)**

:   提出 RACE（Rhetorical Analysis for Creator-Editor Modeling），利用修辞结构理论(RST)构建逻辑图来建模文本"创作者"的思维架构，同时提取篇章单元级特征捕获"编辑者"的语言风格，实现四类细粒度 LLM 生成文本检测（人写/LLM写/LLM润色人文/人改写LLM文）。

**[BIASEDTALES-ML: A Multilingual Dataset for Analyzing Narrative Attribute Distributions in LLM-Generated Stories](aigc_detection/biasedtales-ml_a_multilingual_dataset_for_analyzing_narrative_attribute_distribu.md)**

:   BiasedTales-ML 构建了约 35 万篇覆盖 8 种语言的 LLM 生成儿童故事语料库，通过全排列提示设计和分布分析框架，揭示了**叙事中社会属性分布在不同语言间存在显著差异**，英语中心的评估无法反映多语言场景下的偏见模式。

---

## 🕸️ 图学习 { #graph_learning }

**[AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning](graph_learning/agentgl_towards_agentic_graph_learning_with_llms_via_reinforcement_learning.md)**

:   提出 AgentGL，首个基于强化学习的智能体图学习（AGL）框架，让 LLM 智能体通过图原生搜索工具自主导航文本属性图（TAG），在节点分类和链接预测任务上分别实现最高 17.5% 和 28.4% 的绝对准确率提升。

**[AutoPKG: An Automated Framework for Dynamic E-commerce Product-Attribute Knowledge Graph Construction](graph_learning/autopkg_an_automated_framework_for_dynamic_e-commerce_product-attribute_knowledg.md)**

:   提出 AutoPKG，一个多智能体 LLM 框架，从多模态电商商品内容自动构建 Product-Attribute 知识图谱（PKG），通过类型归纳 Agent、属性键发现 Agent、属性值提取 Agent 和集中式 KGD 决策 Agent 实现动态本体的持续演化和规范化，在 Lazada 数据集上取得 0.953 WKE（类型）和 0.724 WKE（属性键），线上 A/B 测试推荐 GMV 提升 7.89%。

---

## ✂️ 语义分割 { #segmentation }

**[AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation](segmentation/anchorseg_language_grounded_query_banks_for_reasoning_segmentation.md)**

:   提出AnchorSeg，将推理分割重构为基于语言引导查询库的结构化条件生成过程，通过锚点查询显式解耦空间定位与语义推理，配合Token-Mask循环一致性训练目标，在ReasonSeg上达到SOTA（67.7% gIoU, 68.1% cIoU）。

**[Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](segmentation/hierarchical_policy_optimization_for_simultaneous_translation_of_unbounded_speec.md)**

:   本文提出 Hierarchical Policy Optimization (HPO)，通过层级奖励设计对基于 LLM 的同声传译模型进行后训练，在翻译质量未达阈值时抑制延迟优化，从而在 1.5 秒延迟下实现 +7 COMET 的翻译质量提升。

---

## 🗣️ 对话系统 { #dialogue }

**[Cognitive Policy-Driven LLM for Diagnosis and Intervention of Cognitive Distortions in Emotional Support Conversation](dialogue/cognitive_policy-driven_llm_for_diagnosis_and_intervention_of_cognitive_distorti.md)**

:   提出CoPoLLM框架，通过构建首个带认知扭曲标注的情感支持对话数据集CogBiasESC，结合认知策略强化学习（CPRL）引擎和双流条件优化（DSCO），使LLM能诊断8类认知扭曲并生成策略感知的干预回复，在15个SOTA基线上全面领先。

---

## 🖼️ 图像恢复 { #image_restoration }

**[Diffusion-CAM: Faithful Visual Explanations for dMLLMs](image_restoration/diffusion-cam_faithful_visual_explanations_for_dmllms.md)**

:   提出 Diffusion-CAM，首个专为扩散式多模态大语言模型（dMLLM）设计的可解释性方法，通过在去噪轨迹中提取结构有效的中间表征并配合四个后处理模块（自适应核去噪、分布感知置信门控、上下文背景衰减、单实例因果去偏），在 COCO Caption 和 GranDf 上显著超越自回归 CAM 基线。

---

## ✏️ 知识编辑 { #knowledge_editing }

**[FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](knowledge_editing/fable_fine-grained_fact_anchoring_for_unstructured_model_editing.md)**

:   本文发现现有非结构化模型编辑方法虽能整体性回忆编辑文本但无法进行细粒度事实访问，提出FABLE框架通过两阶段层次化策略将细粒度事实锚定到浅层、整体性叙事整合到深层，并构建UnFine诊断基准进行系统评估。

---

## ⚖️ 对齐/RLHF { #llm_alignment }

**[STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming](llm_alignment/star-teaming_a_strategy-response_multiplex_network_approach_to_automated_llm_red.md)**

:   本文提出 STAR-Teaming，一种基于策略-响应多路复用网络（Multiplex Network）的自动化红队测试框架，通过将攻击策略选择建模为逆 Ising 问题的概率优化，在 HarmBench 上达到平均 74.5% 的攻击成功率，比最强基线高 13.5%，同时显著降低计算开销。

---

## 📚 预训练 { #llm_pretraining }

**[Commonsense Knowledge with Negation: A Resource to Enhance Negation Understanding](llm_pretraining/commonsense_knowledge_with_negation_a_resource_to_enhance_negation_understanding.md)**

:   提出自动为现有常识知识库增添否定的方法，构建超过 200 万三元组的否定常识语料库（¬Atomic 和 ¬Anion），并证明在其上预训练可以提升 LLM 的否定理解能力。

---

## ✍️ 文本生成 { #nlp_generation }

**[AlphaContext: An Evolutionary Tree-based Psychometric Context Generator for Creativity Assessment](nlp_generation/alphacontext_an_evolutionary_tree-based_psychometric_context_generator_for_creat.md)**

:   提出 AlphaContext，一个基于进化树的心理测量情境生成器，通过 HyperTree 大纲规划、MCTS 逐句生成、MAP-Elites 多样性优化和评估引导迭代精炼四个模块，自动生成用于创造力评估的高质量长文本情境，在 7 个评估维度上平均超越竞争方法 8%。

---

## 📖 NLP理解 { #nlp_understanding }

**[DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot NER](nlp_understanding/diziner_disagreement-guided_instruction_refinement_via_pilot_annotation_simulati.md)**

:   DiZiNER 模拟人类试标注流程：多个异构 LLM 独立标注同一文本，分析模型间分歧来迭代精炼任务指令，在 18 个 NER 基准中的 14 个上达到零样本 SOTA，平均 F1 提升 +8.0，且超越其监督模型 GPT-5 mini。

---

## 🤖 具身智能 { #robotics }

**[DeCoVec: Building Decoding Space based Task Vector for Large Language Models via In-Context Learning](robotics/decovec_building_decoding_space_based_task_vector_for_large_language_models_via_.md)**

:   提出 DeCoVec（Decoding Space based Task Vector），一个无训练、非侵入式的框架，通过对比 few-shot 和 zero-shot prompt 的输出 logit 分布差异构建解码空间中的任务向量，注入解码过程引导生成，在 TruthfulQA、Math-500 和 AQUA-RAT 上比标准 few-shot 基线平均提升高达 5.50 准确率。

---

## 👥 社会计算 { #social_computing }

**[Explain the Flag: Contextualizing Hate Speech Beyond Censorship](social_computing/explain_the_flag_contextualizing_hate_speech_beyond_censorship.md)**

:   本文提出一种混合方法，结合 LLM 和三种语言（英/法/希腊语）的人工策展词汇表来检测和解释仇恨言论——术语管道通过词汇匹配+LLM 语义消歧检测固有贬损用语，无术语管道用 LLM 检测群体针对性内容，两者融合生成有据可查的解释。

---

## 📈 时间序列 { #time_series }

**[A Unified Framework for Modeling Heterogeneous Financial Data via Dual-Granularity Prompting](time_series/a_unified_framework_for_modeling_heterogeneous_financial_data_via_dual-granulari.md)**

:   提出FinLangNet框架，通过双模块架构（DeepFM处理静态特征 + 双粒度提示机制的Transformer处理时序行为）实现多尺度信用风险预测，在滴滴金融平台部署后实现KS提升6.3pp和坏账率下降9.9%。

---

## 🎬 视频生成 { #video_generation }

**[Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](video_generation/accelerating_training_of_autoregressive_video_generation_models_via_local_optimi.md)**

:   提出 Local Optimization + Representation Continuity (ReCo) 训练策略，通过在局部窗口内优化并约束隐状态的平滑过渡，实现自回归视频生成模型训练速度提升 2 倍且不牺牲生成质量。

---

## 📹 视频理解 { #video_understanding }

**[Distorted or Fabricated? A Survey on Hallucination in Video LLMs](video_understanding/distorted_or_fabricated_a_survey_on_hallucination_in_video_llms.md)**

:   本文首次对视频大语言模型（Vid-LLM）中的幻觉现象进行系统分类，提出"动态失真"（时空关系和引用一致性错误）和"内容捏造"（统计先验驱动和音视频冲突）的机制驱动分类体系，综述评估基准、缓解策略和根因分析。

---

## 📂 其他 { #others }

**[Are Large Language Models Economically Viable for Industry Deployment?](others/are_large_language_models_economically_viable_for_industry_deployment.md)**

:   提出Edge-Eval框架，通过5个部署指标（经济盈亏平衡、智能功耗比、系统密度、冷启动税、量化保真度）在传统T4 GPU上全生命周期评估LLM，揭示<2B小模型在经济和生态维度全面优于7B模型，并发现QLoRA虽降低内存但能耗增加最高7倍的反常现象。

**[Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning](others/beyond_accuracy_unveiling_inefficiency_patterns_in_tool-integrated_reasoning.md)**

:   提出 PTE（Prefill Token Equivalents），一个基于硬件感知的工具集成推理效率度量指标，统一了内部推理和外部工具使用的成本，并通过大规模实验揭示了四种 TIR 低效模式：确认性工具使用、工具混合、缺乏工具先验和工具格式崩溃。

</div>