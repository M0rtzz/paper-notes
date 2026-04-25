---
title: >-
  ACL2026 医学图像方向 19篇论文解读
description: >-
  19篇ACL2026 医学图像论文解读，主题涵盖：CoLabScience 通过、提出 AROMA 框架，通过整合文本证据、提出 CMedTEB（中文医学文本嵌入基准）和等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**💬 ACL2026** · **19** 篇论文解读

**["Excuse Me, May I Say Something…" CoLabScience: A Proactive AI Assistant for Biomedical Discovery](34excuse_me_may_i_say_something34_colabscience_a_proactive_ai_assistant_for_biom.md)**

:   CoLabScience 通过 PULI（正无标注学习干预）框架，训练一个能在生物医学团队讨论中**主动判断何时介入、如何介入**的 LLM 助手，利用 GRPO 和强化学习协调器从流式对话中自动识别最佳干预时机并生成科学建议。

**[AROMA: Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling](aroma_augmented_reasoning_over_a_multimodal_architecture_for_virtual_cell_geneti.md)**

:   提出 AROMA 框架，通过整合文本证据、知识图谱拓扑信息和蛋白质序列特征的多模态架构，结合两阶段训练策略（SFT + GRPO），实现了可解释且精确的基因扰动效应预测。

**[Benchmarking and Enabling Efficient Chinese Medical Retrieval via Asymmetric Encoders](benchmarking_and_enabling_efficient_chinese_medical_retrieval_via_asymmetric_enc.md)**

:   提出 CMedTEB（中文医学文本嵌入基准）和 CARE（非对称检索框架），前者通过多 LLM 投票+专家验证构建高质量的中文医学检索/重排/STS 基准，后者用轻量 BERT 编码查询+大型 LLM 编码文档的非对称架构，通过两阶段渐进对齐策略实现 LLM 级检索精度+BERT 级在线延迟。

**[Beyond Prompt: Fine-grained Simulation of Cognitively Impaired Standardized Patients via Stochastic Steering](beyond_prompt_fine-grained_simulation_of_cognitively_impaired_standardized_patie.md)**

:   提出 StsPatient，通过从对比指令/回复对中提取领域特定的转向向量（Steering Vector），配合随机 Token 调制（STM）机制控制注入概率来模拟不同认知障碍领域和严重程度的标准化病人，相比 prompt engineering 方法在临床真实性上平均提升 11.23%，在严重程度可控性上超越最佳基线 18.54%。

**[Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical Intake via Collaborative Agents](beyond_the_individual_virtualizing_multi-disciplinary_reasoning_for_clinical_int.md)**

:   提出 Aegle 框架，通过图结构多智能体架构虚拟化多学科会诊（MDT），将解耦并行推理和动态拓扑引入门诊问诊流程，在24个科室53项指标上超越SOTA模型。

**[BioHiCL: Hierarchical Multi-Label Contrastive Learning for Biomedical Retrieval with MeSH Labels](biohicl_hierarchical_multi-label_contrastive_learning_for_biomedical_retrieval_w.md)**

:   BioHiCL 利用 MeSH（医学主题词）的**层级多标签标注**为稠密检索器提供结构化监督，通过深度加权的标签相似度对齐嵌入空间与 MeSH 语义空间，使 0.1B 模型在生物医学检索、句子相似度和问答任务上超越大多数专用模型。

**[Calibrated? Not for Everyone: How Sexual Orientation and Religious Markers Distort LLM Accuracy and Confidence in Medical QA](calibrated_not_for_everyone_how_sexual_orientation_and_religious_markers_distort.md)**

:   研究社会身份标记（性取向和宗教信仰）如何扭曲LLM在医疗问答中的准确率和置信度校准，发现"同性恋"标记在9个LLM上一致导致性能下降和校准危机，且交叉身份产生非加性的特异性伤害。

**[CURA: Clinical Uncertainty Risk Alignment for Language Model-Based Risk Prediction](cura_clinical_uncertainty_risk_alignment_for_language_model-based_risk_predictio.md)**

:   CURA 提出一个双层不确定性校准框架：个体层面将预测不确定性与错误概率对齐，队列层面通过嵌入空间的邻域风险率正则化预测，在 MIMIC-IV 的五个临床风险预测任务上一致提升校准指标而不牺牲判别性能。

**[Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](detecting_hallucinations_in_speechllms_at_inference_time_using_attention_maps.md)**

:   提出四种基于音频注意力的指标（AudioRatio、AudioConsistency、AudioEntropy、TextEntropy），训练轻量级逻辑回归分类器在推理时检测语音大模型（SpeechLLM）的幻觉，在域内数据上 PR-AUC 提升最高达 +0.23。

**[Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction](efficient_and_effective_internal_memory_retrieval_for_llm-based_healthcare_predi.md)**

:   本文提出K2K框架，将LLM的FFN参数空间视为可检索的知识库，通过LoRA注入临床知识、激活引导的探针构建精确检索、交叉注意力重排序自适应整合，实现了无需外部检索延迟的医疗预测SOTA。

**[Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach](eliciting_medical_reasoning_with_knowledge-enhanced_data_synthesis_a_semi-superv.md)**

:   本文提出MedSSR框架，通过注入罕见病知识的可控数据合成和"自监督RL→监督RL"的半监督训练范式，高效提升LLM的医学推理能力，在罕见病任务上实现最高+5.93%的提升，突破了现有方法+3%的改进上限。

**[From Answers to Arguments: Toward Trustworthy Clinical Diagnostic Reasoning with Toulmin-Guided Curriculum Goal-Conditioned Learning](from_answers_to_arguments_toward_trustworthy_clinical_diagnostic_reasoning_with_.md)**

:   本文将Toulmin论证模型适配到临床诊断过程，提出CGCL三阶段课程训练框架（事实收集→假设检验→综合结论），配合T-Eval量化评估推理结构完整性，在无需RL的情况下实现与RL方法可比的诊断推理质量。

**[HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering](hypehr_hyperbolic_modeling_of_electronic_health_records_for_efficient_question_a.md)**

:   本文提出 HypEHR，一个仅 22M 参数的洛伦兹双曲模型，将医学编码、就诊记录和问题嵌入双曲空间，通过层级感知正则化对齐 ICD 本体结构，在 MIMIC-IV 电子病历问答任务上接近 LLM 方法的效果。

**[Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness](learning_dynamic_representations_and_policies_from_multimodal_clinical_time-seri.md)**

:   提出 OPL-MT-MNAR 框架，通过 MNAR 感知的多模态编码器 + 贝叶斯滤波隐状态 + 离线策略学习，从结构化数据和临床文本的"缺失模式本身携带的信息"中学习 ICU 患者动态表示，实现优于临床医生行为的脓毒症治疗策略（FQE 0.679 vs 0.528）。

**[MHSafeEval: Role-Aware Interaction-Level Evaluation of Mental Health Safety in Large Language Models](mhsafeeval_role-aware_interaction-level_evaluation_of_mental_health_safety_in_la.md)**

:   本文提出 R-MHSafe 角色感知心理健康安全分类体系和 MHSafeEval 闭环 agent 评估框架，通过对抗性多轮咨询交互系统性发现 LLM 在心理咨询场景中的角色依赖型累积安全失败，揭示了现有静态基准无法捕捉的交互层面危害。

**[RADS: Reinforcement Learning-Based Sample Selection Improves Transfer Learning in Low-resource and Imbalanced Clinical Settings](rads_reinforcement_learning-based_sample_selection_improves_transfer_learning_in.md)**

:   本文提出 RADS（Reinforcement Adaptive Domain Sampling），一种基于强化学习的样本选择策略，在极端低资源和类别不平衡的临床场景下，通过智能选择少量目标域样本进行标注和联合微调，显著提升跨域疾病检测的迁移效果。

**[Region-Grounded Report Generation for 3D Medical Imaging: A Fine-Grained Dataset and Graph-Enhanced Framework](region-grounded_report_generation_for_3d_medical_imaging_a_fine-grained_dataset_.md)**

:   本文提出首个带有细粒度 ROI 标注的 3D PET/CT 数据集 VietPET-RoI（越南语），以及模拟放射科医生诊断流程的层次化报告生成框架 HiRRA，通过图神经网络建模 ROI 间的空间-形态学关系，BLEU-4 提升 19.7%，临床指标 RoIQ 提升 45.8%。

**[RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models](reprompt_recurrent_prompt_tuning_for_integrating_structured_ehr_encoders_with_la.md)**

:   本文提出 RePrompT，一种时间感知的 LLM 框架，通过循环提示调优（将前一次就诊的隐状态作为下一次就诊的软提示）和结构化编码提示调优（注入群体级 EHR 编码器的嵌入）两种互补机制，在 MIMIC-III/IV 上的再入院和死亡率预测任务上一致超越 EHR 基线和 LLM 基线。

**[Thinking Like a Botanist: Challenging Multimodal Language Models with Intent-Driven Chain-of-Inquiry](thinking_like_a_botanist_challenging_multimodal_language_models_with_intent-driv.md)**

:   本文提出PlantInquiryVQA基准和Chain-of-Inquiry（CoI）框架，包含24,950张植物图像和138,068个问答对，模拟植物学家的适应性诊断提问策略，评估18个MLLM在植物病理诊断中的多步视觉推理能力，发现结构化提问显著提升诊断准确性并减少幻觉，但即使最强模型的临床实用性得分仅0.188。
