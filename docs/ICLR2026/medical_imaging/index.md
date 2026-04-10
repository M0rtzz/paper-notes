<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🔬 ICLR2026** · 共 **78** 篇

**[Adaptive Domain Shift in Diffusion Models for Cross-Modality Image Translation](adaptive_domain_shift_in_diffusion_models_for_cross-modality_image_translation.md)**

:   提出CDTSDE框架，在扩散模型的逆向SDE中嵌入可学习的空间自适应域混合场 $\Lambda_t$，使跨模态翻译路径沿低能量流形前进，在MRI模态转换、SAR→光学、工业缺陷语义映射任务上以更少去噪步数实现更高保真度。

**[Adaptive Test-Time Training for Predicting Need for Invasive Mechanical Ventilation in Multi-Center Cohorts](adaptive_test-time_training_for_predicting_need_for_invasive_mechanical_ventilat.md)**

:   提出AdaTTT框架，通过动态特征感知self-supervised学习（自适应掩码策略）和原型引导的部分最优传输对齐，在ICU多中心EHR数据上实现鲁棒的测试时适应，用于提前24小时预测有创机械通气需求。

**[AFD-INSTRUCTION: A Comprehensive Antibody Instruction Dataset with Functional Annotations for LLM-Based Understanding and Design](afd-instruction_a_comprehensive_antibody_instruction_dataset_with_functional_ann.md)**

:   构建了首个大规模抗体功能注释指令数据集AFD-Instruction（430K+条目），通过多智能体文献抽取pipeline对齐抗体序列与自然语言功能描述，用于指令微调通用LLM使其掌握抗体理解和功能导向设计能力，在5类分类任务上平均准确率提升20+点。

**[An Orthogonal Learner for Individualized Outcomes in Markov Decision Processes](an_orthogonal_learner_for_individualized_outcomes_in_markov_decision_processes.md)**

:   从因果推断视角重新审视Q函数估计问题，揭示传统Q回归和FQE是具有插入偏差的plug-in学习器，提出DRQQ-learner——一种双重鲁棒、Neyman正交、准oracle高效的Q函数估计器，通过推导有效影响函数构建去偏两阶段损失函数，在Taxi和Frozen Lake环境中验证了其优越性。

**[AntigenLM: Structure-Aware DNA Language Modeling for Influenza](antigenlm_structure-aware_dna_language_modeling_for_influenza.md)**

:   AntigenLM 是一个保留基因组功能单元完整性的 GPT-2 风格 DNA 语言模型，通过在流感病毒全基因组上预训练并微调，能够自回归预测未来流行毒株的抗原序列，在氨基酸错配率上显著优于进化模型 beth-1 和通用基因组模型。

**[ATPO: Adaptive Tree Policy Optimization for Multi-Turn Medical Dialogue](atpo_adaptive_tree_policy_optimization_for_multi-turn_medical_dialogue.md)**

:   提出 ATPO（自适应树策略优化）算法，将多轮医疗对话建模为层级马尔可夫决策过程（H-MDP），通过不确定性感知的自适应树扩展机制动态分配rollout预算，结合Bellman误差和动作值方差的复合不确定性度量来引导探索，在三个医学对话基准上以Qwen3-8B超越GPT-4o。

**[Augmenting Representations with Scientific Papers](augmenting_representations_with_scientific_papers.md)**

:   提出首个将 X 射线光谱与科学文献通过对比学习对齐的多模态基础模型框架，在共享潜在空间中实现 20% Recall@1% 的跨模态检索，物理参数估计提升 16–18%，同时发现候选脉动超亮 X 射线源等罕见天体。

**[Benchmarking ECG FMs: A Reality Check Across Clinical Tasks](benchmarking_ecg_fms_a_reality_check_across_clinical_tasks.md)**

:   对8个ECG基础模型在12个数据集、26个临床任务上进行"现实检验"式全面基准评测，发现紧凑的结构化状态空间模型（SSM）ECG-CPC在7个任务类别中的5个上超越了大规模Transformer，证明架构设计比模型规模更重要。

**[BiomedSQL: Text-to-SQL for Scientific Reasoning on Biomedical Knowledge Bases](biomedsql_text-to-sql_for_scientific_reasoning_on_biomedical_knowledge_bases.md)**

:   提出 BiomedSQL，首个专门评估 Text-to-SQL 系统在生物医学知识库上科学推理能力的基准，包含 68,000 个问题/SQL/答案三元组，揭示当前最强模型（GPT-o3-mini 62.6%）与领域专家（90%）之间仍有巨大差距。

**[Boosting Medical Visual Understanding From Multi-Granular Language Learning](boosting_medical_visual_understanding_from_multi-granular_language_learning.md)**

:   提出 Multi-Granular Language Learning (MGLL)，一个即插即用的对比学习框架，通过 soft CLIP loss、point-wise loss 和 smooth KL 散度联合优化，实现医学图像与多标签多粒度文本描述的对齐，在眼底和 X 光数据集上全面超越 SOTA 方法，并可作为视觉编码器嵌入多模态大语言模型提升诊断准确率最高达 34.1%。

**[Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer](brain-it_image_reconstruction_from_fmri_via_brain-interaction_transformer.md)**

:   提出 Brain-IT 框架，通过脑启发式的 Brain Interaction Transformer (BIT) 将功能相似的脑体素聚类为跨被试共享的 Brain Token，并从中预测局部化的语义和结构图像特征，实现从 fMRI 到图像的高保真重建，仅用 1 小时数据即达到先前方法 40 小时的性能。

**[Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model](brain-semantoks_learning_semantic_tokens_of_brain_dynamics_with_a_self-distilled.md)**

:   提出 Brain-Semantoks，一种基于语义分词器和自蒸馏目标的 fMRI 基础模型，将大脑功能网络聚合为鲁棒的语义 token，并通过跨时间视角的一致性学习抽象的脑动态表征，在线性探测设置下即可达到 SOTA 性能。

**[Bridging Explainability and Embeddings: BEE Aware of Spuriousness](bridging_explainability_and_embeddings_bee_aware_of_spuriousness.md)**

:   提出BEE框架，通过分析微调如何扰动预训练表征的权重空间几何结构，直接从分类器学到的权重中识别和命名虚假相关性（spurious correlations），无需反例样本即可发现隐藏的数据偏差，在ImageNet-1k上发现可导致准确率下降高达95%的虚假关联。

**[Can SAEs Reveal and Mitigate Racial Biases of LLMs in Healthcare?](can_saes_reveal_and_mitigate_racial_biases_of_llms_in_healthcare.md)**

:   研究稀疏自编码器（SAE）能否揭示和缓解 LLM 在医疗场景中的种族偏见：发现 SAE 能识别出与种族相关的有害联想（如黑人与暴力），但在复杂临床任务中缓解偏见的效果有限（FLDD < 3%），远不如简单的提示策略（FLDD 8-15%）。

**[CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework](care_towards_clinical_accountability_in_multi-modal_medical_reasoning_with_an_ev.md)**

:   提出 CARE Agent 框架，将医学 VQA 分解为实体提议、指称分割和证据引导推理三个专家模块，通过 GPT-5 作为动态协调器，在医学 VQA 基准上以 77.54% 准确率超越 32B 模型。

**[Causal Interpretation of Neural Network Computations with Contribution Decomposition](causal_interpretation_of_neural_network_computations_with_contribution_decomposi.md)**

:   提出 CODEC（Contribution Decomposition），用 Integrated Gradients 计算隐藏层神经元对输出的贡献（而非仅分析激活），再用 Sparse Autoencoder 将贡献分解为稀疏模式（modes），实现比激活分析更强的因果可解释性和网络控制能力，并成功应用于 ResNet-50 和视网膜生物神经网络模型。

**[Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space](characterizing_human_semantic_navigation_in_concept_production_as_trajectories_i.md)**

:   提出将人类概念产生过程建模为 Transformer 嵌入空间中的累积轨迹，定义 5 个运动学指标（距离、速度、加速度、熵、质心距离），在 4 个数据集（3 种语言、神经退行性疾病/脏话流畅性/属性列举）上成功区分临床组和概念类别，且不同嵌入模型产生高度一致的结果。

**[COMPASS: Robust Feature Conformal Prediction for Medical Segmentation Metrics](compass_robust_feature_conformal_prediction_for_medical_segmentation_metrics.md)**

:   提出 COMPASS 框架，在分割模型的中间特征空间而非输出空间做共形预测，通过沿 Jacobian 确定的低维敏感子空间扰动特征来构建预测区间，在多个医学分割数据集上以更紧凑的区间达到目标覆盖率。

**[ConfHit: Conformal Generative Design with Oracle Free Guarantees](confhit_conformal_generative_design_with_oracle_free_guarantees.md)**

:   提出 ConfHit，一个模型无关的保理推断框架，通过密度比加权的共形 p 值和嵌套检验策略，在无需实验验证（oracle-free）和分布偏移条件下，为生成模型（药物发现等）提供有限样本统计保证——生成的候选集以 $1-\alpha$ 概率包含至少一个 hit。

**[Controllable Sequence Editing for Biological and Clinical Trajectories](controllable_sequence_editing_for_biological_and_clinical_trajectories.md)**

:   提出 Clef，一个基于"时间概念"（temporal concepts）的可控序列编辑模型，能够在给定条件（如药物、手术）下对生物/临床多变量轨迹进行即时和延迟编辑，在细胞重编程和患者实验室检测数据上，即时编辑 MAE 提升 16.28%，延迟编辑提升 26.73%，零样本反事实生成提升达 62.84%。

**[Controlling Repetition in Protein Language Models](controlling_repetition_in_protein_language_models.md)**

:   首次系统性研究蛋白质语言模型（PLM）中的病态重复问题，提出统一的重复度量指标 $R(x)$ 和效用指标 $U(x)$，并设计 UCCS（Utility-Controlled Contrastive Steering）方法，通过在隐层注入与重复解耦的引导向量，在不重训模型的前提下有效抑制重复同时保持折叠可信度。

**[CryoNet.Refine: A One-step Diffusion Model for Rapid Refinement of Structural Models with Cryo-EM Density Map Restraints](cryonetrefine_a_one-step_diffusion_model_for_rapid_refinement_of_structural_mode.md)**

:   提出CryoNet.Refine——首个基于AI的冷冻电镜(cryo-EM)原子模型精修框架：设计单步扩散模型(初始化自Boltz-2权重)→创新可微分密度生成器(物理模拟合成密度图)→首次将密度图相关性作为可微损失函数(余弦相似度)→联合Ramachandran/Rotamer/键角等几何约束损失→测试时优化策略逐案定制→在120个蛋白质/DNA-RNA复合物上全面超越Phenix.real_space_refine(CC_mask 0.59 vs 0.54, Ramachandran favored 98.92%)。

**[Decentralized Attention Fails Centralized Signals: Rethinking Transformers for Medical Time Series](decentralized_attention_fails_centralized_signals_rethinking_transformers_for_me.md)**

:   提出 TeCh 框架，核心是用 CoTAR（Core Token Aggregation-Redistribution）模块替代 Transformer 中的标准注意力来建模医学时间序列的通道依赖——通过引入全局"核心 token"充当代理，先聚合所有通道信息再重分配回每个通道，复杂度从 $O(n^2)$ 降至 $O(n)$，在 APAVA 数据集上精度 86.86%（超 Medformer 12.13%），内存仅 33%、推理时间仅 20%。

**[Deep Hierarchical Learning with Nested Subspace Networks for Large Language Models](deep_hierarchical_learning_with_nested_subspace_networks_for_large_language_mode.md)**

:   提出嵌套子空间网络（NSN），通过低秩分解使线性层形成严格嵌套的子空间层次，配合不确定性感知多秩训练，使单个模型在测试时可即时调节计算量与性能的权衡（50% FLOPs 减少仅损失 5% 精度），且可后验应用于预训练 LLM。

**[DISCO: Densely-overlapping Cell Instance Segmentation via Adjacency-aware Collaborative Coloring](disco_densely-overlapping_cell_instance_segmentation_via_adjacency-aware_collabo.md)**

:   提出基于图着色理论的密集重叠细胞实例分割框架 DISCO，通过"显式标记冲突+隐式消歧邻接约束"的分治策略，在高密度病理图像上 PQ 提升 7.08%。

**[Discrete Diffusion Trajectory Alignment via Stepwise Decomposition](discrete_diffusion_trajectory_alignment_via_stepwise_decomposition.md)**

:   提出 SDPO（Stepwise Decomposition Preference Optimization），将离散扩散模型的轨迹对齐问题分解为逐步后验对齐子问题，避免了在整条去噪链上反传梯度的困难，在 DNA 序列设计、蛋白质逆折叠和语言建模三个任务上均显著超越现有方法。

**[DistMLIP: A Distributed Inference Platform for Machine Learning Interatomic Potentials](distmlip_a_distributed_inference_platform_for_machine_learning_interatomic_poten.md)**

:   提出 DistMLIP 分布式推理平台，基于零冗余图级并行化策略（graph-level parallelization），解决现有机器学习原子间势（MLIP）缺乏多 GPU 支持的问题，在 8 GPU 上实现接近百万原子的模拟，比空间分区方法快达 8 倍且能模拟 3.4 倍更大的系统。

**[Distributional Consistency Loss: Beyond Pointwise Data Terms in Inverse Problems](distributional_consistency_loss_beyond_pointwise_data_terms_in_inverse_problems.md)**

:   提出分布一致性（DC）损失，用分布级别的校准替代传统逐点数据保真项（如MSE/NLL），避免对噪声的过拟合，在DIP去噪和PET图像重建中显著提升性能且无需早停。

**[DM4CT: Benchmarking Diffusion Models for Computed Tomography Reconstruction](dm4ct_benchmarking_diffusion_models_for_computed_tomography_reconstruction.md)**

:   提出DM4CT——首个系统性的CT重建扩散模型基准，涵盖十种扩散方法和七种基线方法，在医疗、工业和同步辐射三类数据集上进行全面评估，揭示了扩散模型在CT重建中的优势与局限。

**[DriftLite: Lightweight Drift Control for Inference-Time Scaling of Diffusion Models](driftlite_lightweight_drift_control_for_inference-time_scaling_of_diffusion_mode.md)**

:   DriftLite 提出在 Fokker-Planck 方程中利用漂移-势函数的自由度，通过轻量级线性系统求解最优控制漂移来主动稳定粒子权重，以最小代价解决 Sequential Monte Carlo 中的权重退化问题，在高斯混合、分子系统和蛋白质-配体共折叠任务上大幅超越 Guidance-SMC 基线。

**[Dual Distillation for Few-Shot Anomaly Detection](dual_distillation_for_few-shot_anomaly_detection.md)**

:   提出双蒸馏框架 D24FAD，结合 query 图像上的教师-学生蒸馏（TSD）和 support 图像上的学生自蒸馏（SSD），辅以学习权重机制（L2W）自适应评估 support 重要性，在 APTOS 眼底数据集上仅用 2-shot 达到 100% AUROC。

**[EMR-AGENT: Automating Cohort and Feature Extraction from EMR Databases](emr-agent_automating_cohort_and_feature_extraction_from_emr_databases.md)**

:   提出EMR-AGENT，首个基于LLM Agent的电子病历（EMR）自动化预处理框架，通过动态SQL交互替代手工规则编写，实现跨数据库的队列选择、特征提取和代码映射，在MIMIC-III/eICU/SICdb上表现优异并具强泛化能力。

**[EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](evoflows_evolutionary_edit-based_flow-matching_for_protein_engineering.md)**

:   EvoFlows 提出一种基于编辑操作的 Flow Matching 方法，通过学习进化相关蛋白质序列间的突变轨迹，能在模板序列上执行可控数量的突变（插入、删除、替换），同时预测"突变什么"和"在哪里突变"。

**[Exo-Plore: Exploring Exoskeleton Control Space through Human-Aligned Simulation](exo-plore_exploring_exoskeleton_control_space_through_human-aligned_simulation.md)**

:   提出 Exo-plore 框架，通过神经力学仿真与深度强化学习相结合，无需真人实验即可优化髋关节外骨骼控制参数，并能推广到病理步态场景。

**[ExpGuard: LLM Content Moderation in Specialized Domains](expguard_llm_content_moderation_in_specialized_domains.md)**

:   提出面向金融、医疗、法律等专业领域的安全护栏模型 ExpGuard 及配套数据集 ExpGuardMix（58,928 样本），在领域特定测试集上 prompt 分类 F1 超 WildGuard 8.9%、response 分类超 15.3%，同时在通用安全基准上保持 SOTA 水平。

**[Exploiting Low-Dimensional Manifold of Features for Few-Shot Whole Slide Image Classification](exploiting_low-dimensional_manifold_of_features_for_few-shot_whole_slide_image_c.md)**

:   发现病理基础模型特征具有低维流形几何结构（有效秩仅29.7/512维），而线性层会破坏这种结构导致少样本过拟合，提出即插即用的MR Block（冻结随机矩阵做几何锚+低秩残差路径做任务适配）在少样本WSI分类上达到SOTA。

**[Extending Sequence Length is Not All You Need: Effective Integration of Multimodal Signals for Gene Expression Prediction](extending_sequence_length_is_not_all_you_need_effective_integration_of_multimoda.md)**

:   挑战基因表达预测中"越长越好"的长序列建模范式，发现当前 SSM 模型本质上只利用近端信息；进而识别出背景染色质信号（DNase-seq/Hi-C）作为混杂变量引入虚假关联，提出 Prism 框架通过后门调整去混杂，仅用 2k 短序列即超越 200k 长序列的 SOTA。

**[Fine-Tuning Diffusion Models via Intermediate Distribution Shaping](fine-tuning_diffusion_models_via_intermediate_distribution_shaping.md)**

:   统一拒绝采样微调方法为GRAFT框架并证明其隐式执行KL正则化奖励最大化，进而提出P-GRAFT在中间去噪步骤做分布整形（偏差-方差权衡更优），以及Inverse Noise Correction无需奖励即可改进流模型质量，在T2I上VQAScore提升8.81%。

**[From Conversation to Query Execution: Benchmarking User and Tool Interactions for EHR Database Agents](from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for.md)**

:   提出EHR-ChatQA基准，首次评估数据库Agent在电子病历场景中的端到端交互工作流（澄清模糊查询→解决术语不匹配→生成SQL→返回答案），发现最强模型(o4-mini)的Pass@5超90%但Pass∧5(全部成功)大幅下降(差距达60%)，暴露了安全关键领域的鲁棒性缺陷。

**[Fusing Pixels and Genes: Spatially-Aware Learning in Computational Pathology](fusing_pixels_and_genes_spatially-aware_learning_in_computational_pathology.md)**

:   提出Stamp框架，构建SpaVis-6M（最大10X Visium空间转录组数据集，575万条数据）训练空间感知基因编码器，再通过层次多尺度对比对齐将病理图像与空间基因表达谱联合预训练，在6个数据集4个下游任务上达到SOTA。

**[Glance and Focus Reinforcement for Pan-cancer Screening](glance_and_focus_reinforcement_for_pan-cancer_screening.md)**

:   提出GF-Screen框架模拟放射科医生"扫视-聚焦"策略，Glance模型通过RL学习选择含病灶的子体积，Focus模型精确分割——通过组相对学习(GRL)直接将GRPO从NLP迁移到视觉任务，在FLARE25泛癌挑战中以+25.6%DSC领先冠军方案，同时推理效率提升5.7倍。

**[HistoPrism: Unlocking Functional Pathway Analysis from Pan-Cancer Histology via Gene Expression Prediction](histoprism_unlocking_functional_pathway_analysis_from_pan-cancer_histology_via_g.md)**

:   提出HistoPrism高效Transformer架构从H&E病理图像预测泛癌基因表达，并引入基因通路一致性(GPC)基准（50个Hallmark+87个GO通路）将评估从单基因方差升级到功能通路级别，在通路预测上大幅超越SOTA且参数效率更高。

**[How Do Medical MLLMs Fail? A Study on Visual Grounding in Medical Images](how_do_medical_mllms_fail_a_study_on_visual_grounding_in_medical_images.md)**

:   首次系统验证医学MLLM的核心失败模式是视觉扎根不足——模型注意力未对准临床相关区域(与自然图像不同)，构建VGMED数据集(28K三元组)定量诊断，提出VGRefine推理时方法在6个Med-VQA基准(110K+样本/8种成像模态)上达到SOTA。

**[How to Make the Most of Your Masked Language Model for Protein Engineering](how_to_make_the_most_of_your_masked_language_model_for_protein_engineering.md)**

:   提出基于随机束搜索(SBS)的MLM采样方法用于蛋白质/抗体工程——利用MLM可高效评估整个1-编辑邻域的特点做全序列评估(而非逐突变采样)，支持灵活的多目标引导，系统性的in silico + in vitro评估揭示采样方法的选择至少与模型选择同等重要。

**[Human Behavior Atlas: Benchmarking Unified Psychological and Social Behavior Understanding](human_behavior_atlas_benchmarking_unified_psychological_and_social_behavior_unde.md)**

:   构建 Human Behavior Atlas——首个覆盖情感、认知、病理和社会过程四大维度的大规模多模态行为理解统一基准（101K+ 样本），并训练三种 OmniSapiens-7B 模型变体验证其在多任务训练和迁移学习中的有效性。

**[Improving 2D Diffusion Models for 3D Medical Imaging with Inter-Slice Consistent Stochasticity](improving_2d_diffusion_models_for_3d_medical_imaging_with_inter-slice_consistent.md)**

:   提出 Inter-Slice Consistent Stochasticity (ISCS)，通过球面线性插值(Slerp)在扩散采样的 re-noising 步骤中生成层间相关噪声，从根源消除 2D 扩散先验做 3D 医学重建时的层间不连续伪影——零额外计算/超参数/训练开销，即插即用到任何 2D 扩散逆问题求解器，在稀疏视角 CT、限角 CT 和 MRI 超分辨率上均持续提升。

**[Incentives in Federated Learning with Heterogeneous Agents](incentives_in_federated_learning_with_heterogeneous_agents.md)**

:   建立了数据异构联邦学习的博弈论框架——agent的效用取决于"谁"提供数据而非仅总量,证明纯Nash均衡可能不存在且最优均衡成本可无限倍于合作最优,证明最小成本贡献向量计算是NP-hard但可用LP获得对数近似,并设计出唯一的策略防伪机制(付你所贡献)。

**[Inference-Time Dynamic Modality Selection for Incomplete Multimodal Classification](inference-time_dynamic_modality_selection_for_incomplete_multimodal_classificati.md)**

:   提出DyMo——推理时动态模态选择框架解决不完整多模态分类的"丢弃-补全困境"：丢弃缺失模态损失任务相关信息，补全可能引入噪声/语义错位，DyMo通过信息增益驱动的选择算法动态决定哪些恢复模态值得融合(正reward→有用/负reward→有害)，在5个数据集上显著超越SOTA。

**[Intrinsic Lorentz Neural Network](intrinsic_lorentz_neural_network.md)**

:   提出完全内禀（fully intrinsic）的双曲神经网络 ILNN，所有运算均在 Lorentz 模型内完成，消除了现有方法中混合欧几里得操作的几何不一致性，在图像分类、基因组学和图分类上取得 SOTA。

**[Knowledgeable Language Models as Black-Box Optimizers for Personalized Medicine](knowledgeable_language_models_as_black-box_optimizers_for_personalized_medicine.md)**

:   提出 LEON（LLM-based Entropy-guided Optimization with kNowledgeable priors），一种数学原理严格的方法，将个性化医疗治疗方案设计建模为条件黑箱优化问题，通过熵约束和对抗性源批评模型引导 LLM 在不微调的情况下作为零样本优化器提出个性化治疗计划。

**[Learning Domain-Aware Task Prompt Representations for Multi-Domain All-in-One Image Restoration](learning_domain-aware_task_prompt_representations_for_multi-domain_all-in-one_im.md)**

:   提出DATPRL-IR——首个多域全能图像复原方法：通过双提示池设计(任务提示池编码跨任务知识+域提示池从MLLM蒸馏域先验)和提示组合机制(PCM)为每个输入图像动态组合实例级域感知任务提示表示，一个模型统一处理自然场景/医学影像/遥感三域的多种退化任务，显著超越单域SOTA。

**[Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation](learning_patient-specific_disease_dynamics_with_latent_flow_matching_for_longitu.md)**

:   提出Δ-LFM——用流匹配建模患者特异性疾病进展：(1)ArcRank损失强制患者潜在轨迹沿特定轴单调递增(与疾病严重度对齐)构建语义有意义的潜在空间，(2)将流匹配的标准[0,1]时间范围扩展为[0,T]实际时间间隔使预测任意未来时间点成为可能，在3个纵向MRI基准上实现高保真度+精确疾病进展对齐。

**[mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules](mclm_a_modular_chemical_language_model_that_generates_functional_and_makeable_mo.md)**

:   提出mCLM——模块化化学语言模型将分子在功能构建块(而非原子)级别tokenize：用自动化合成兼容的构建块(酰胺偶联/Suzuki/Buchwald反应)作为化学词汇+GNN编码块+自然语言描述功能→形成code-switch双语训练，前置合成可行性同时改善分子功能预测，在430个FDA药物上显著改善关键药物属性，3B参数超越GPT-5的合成可及性。

**[MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](medagentgym_agentic_training_biomedical.md)**

:   构建了首个统一的生物医学数据科学 Agent 训练环境 MedAgentGym，包含 72,413 个任务实例（12 个真实场景、129 个类别），配备可执行沙盒和可验证 ground truth，基准评估 29 个 LLM，并通过离线/在线 RL 训练出 Med-Copilot（分别 +43%/+45% 提升），达到与 GPT-4o 竞争的性能同时保持成本效益和隐私保护。

**[MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](mmedagent-rl_optimizing_multi-agent_collaboration_for_multimodal_medical_reasoni.md)**

:   提出MMedAgent-RL——RL驱动的多智能体医学推理框架：模拟临床流程(分诊→专科→主治)，用GRPO分别优化分诊医生(准确分科)和主治医生(整合专家意见做最终决策)，创新性地引入课程学习驱动的熵感知RL(C-MARL)渐进教主治医生处理不同质量的专家意见(全对→部分对→全错)，在5个医学VQA基准上平均超越基线23.6%。

**[Moving Beyond Medical Exams: A Clinician-Annotated Fairness Dataset of Real-World Tasks and Ambiguity in Mental Healthcare](moving_beyond_medical_exams_a_clinician-annotated_fairness_dataset_of_real-world.md)**

:   提出MENTAT——由精神科临床医生创建和标注的数据集,覆盖5个心理健康实践领域(诊断/治疗/分诊/监测/文档),通过人口统计变量替换(年龄/种族/性别)系统评估LM决策中的偏见→不同于考试题→捕捉真实临床模糊性(多个有效答案+不确定性标注)→评估22个LM发现显著的决策质量差异和人口统计敏感性。

**[Neuro-Symbolic Decoding of Neural Activity](neuro-symbolic_decoding_of_neural_activity.md)**

:   提出NEURONA——fMRI解码的神经符号框架：将查询解析为符号表达式+将fMRI信号划分为脑区级候选实体→学习每个概念(person/holding等)的接地模块→按符号结构组合接地分数回答fMRI-QA→证明建模谓词-论元依赖(holding依赖person和bat的脑区)显著优于端到端神经解码,且泛化到未见查询。

**[Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research](omni-ieeg_a_large-scale_comprehensive_ieeg_dataset_and_benchmark_for_epilepsy_re.md)**

:   构建Omni-iEEG——迄今最大规模的术前iEEG数据集(302患者×178小时×8个癫痫中心)+3.6万+专家标注病理事件,定义临床意义任务+统一评估指标→展示端到端建模可匹敌/超越临床生物标志物,发现跨域迁移(音频预训练→iEEG)有效→为可重复、可泛化的癫痫研究建立基础。

**[Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling](overthinking_reduction_with_decoupled_rewards_and_curriculum_data_scheduling.md)**

:   提出DeCS——通过解耦token级奖励+课程batch调度解决LLM过度思考：理论发现现有长度奖励的两个缺陷(1.错误惩罚有效探索token 2.虚假奖励冗余token)→训练轻量评判模型识别必要推理前缀(NRP)边界→NRP后的token一致惩罚→课程调度控制简单题比例→7个基准推理token减50%+且性能不降甚至提升。

**[Protein as a Second Language for LLMs](protein_as_a_second_language_for_llms.md)**

:   提出"蛋白质即第二语言"框架——将氨基酸序列视为LLM可通过上下文学习获取的符号语言：自适应构建序列-问题-答案三元组作为上下文示例→零样本(无训练)即可理解蛋白质功能→构建7.9万蛋白质双语QA语料→在多个开源LLM和GPT-4o上ROUGE-L平均+7%(最高+17.2%)→甚至超越微调的蛋白质专用模型。

**[Protein Counterfactuals via Diffusion-Guided Latent Optimization](protein_counterfactuals_via_diffusion-guided_latent_optimization.md)**

:   提出MCCOP——在蛋白质连续序列-结构潜在空间中用扩散模型作为流形先验进行反事实优化：给定预测为"不良"的蛋白质→找到最小且生物合理的序列编辑使预测翻转→平衡三目标(有效性/近似性/合理性)→在GFP荧光恢复/热稳定性增强/E3连接酶活性恢复三个任务上→比离散/连续基线更少突变+更高合理性→恢复的突变与已知生物物理机制一致。

**[Protein Structure Tokenization via Geometric Byte Pair Encoding](protein_structure_tokenization_via_geometric_byte_pair_encoding.md)**

:   提出GeoBPE——首个几何感知蛋白质结构BPE tokenizer，将连续骨架构象离散化为几何motif句子，通过k-medoids+自适应量化+可微IK(SE(3)端帧损失)校正漂移，>10x压缩比、>10x数据效率，12个下游任务24个测试集上超越所有PST基线。

**[Q-FSRU: Quantum-Augmented Frequency-Spectral Fusion for Medical Visual Question Answering](q-fsru_quantum-augmented_frequency-spectral_for_medical_visual_question_answerin.md)**

:   提出 Q-FSRU 框架，通过 FFT 将医学图像和文本特征变换到频率域进行融合，并引入量子启发的检索增强机制（Quantum RAG）从外部知识库中获取医学事实，在 VQA-RAD 数据集上取得 90.0% 准确率。

**[Resp-Agent: An Agent-Based System for Multimodal Respiratory Sound Generation and Disease Diagnosis](resp-agent_an_agent-based_system_for_multimodal_respiratory_sound_generation_and.md)**

:   提出 Resp-Agent 闭环多智能体框架，通过主动对抗课程规划器（Thinker-A2CA）协调可控呼吸音生成器与多模态诊断器，在 229k 规模基准上实现生成↔诊断协同设计，大幅提升长尾类别诊断性能。

**[Reverse Distillation: Consistently Scaling Protein Language Model Representations](reverse_distillation_consistently_scaling_protein_language_model_representations.md)**

:   解决PLM反常缩放(更大不一定更好)，提出反向蒸馏：用小模型表示作基、SVD提取大模型正交残差→前k维=小模型嵌入(Matryoshka嵌套)→更大rd模型一致优于更小，ESM-2 15B rd后首次成为家族最强。

**[Scalable Spatio-Temporal SE(3) Diffusion for Long-Horizon Protein Dynamics](scalable_spatio-temporal_se3_diffusion_for_long-horizon_protein_dynamics.md)**

:   提出 STAR-MD，一个 SE(3) 等变的因果扩散 Transformer，通过联合时空注意力和上下文噪声扰动实现微秒级蛋白质动力学轨迹生成，在 ATLAS 基准上所有指标达到 SOTA，且能稳定外推到训练中未见的微秒时间尺度。

**[Scaling with Collapse: Efficient and Predictable Training of LLM Families](scaling_with_collapse_efficient_and_predictable_training_of_llm_families.md)**

:   证明 LLM 家族的训练损失曲线在优化超参数与数据预算匹配时会“崩塞”到同一条通用曲线上，并利用这一现象实现两个实用应用：(1) 偏离崩塞作为训练病理的早期诊断信号，(2) 崩塞曲线的可预测性实现大规模超参调优的早停。

**[scDFM: Distributional Flow Matching for Robust Single-Cell Perturbation Prediction](scdfm_distributional_flow_matching_model_for_robust_single-cell_perturbation_pre.md)**

:   提出 scDFM，基于条件流匹配（CFM）的生成式框架，通过 MMD 正则化保证分布级保真度，并设计 PAD-Transformer 骨干处理噪声稀疏的单细胞数据，在组合扰动预测上比最强基线 CellFlow 的 MSE 降低 19.6%。

**[Shoot First, Ask Questions Later? Building Rational Agents that Explore and Act Like People](shoot_first_ask_questions_later_building_rational_agents_that_explore_and_act_li.md)**

:   提出 Collaborative Battleship 任务评估语言模型的信息搜索能力，设计三种贝叶斯推断策略（Bayes-Q/M/D）增强 LM 的提问、行动和决策能力，使弱模型（Llama-4-Scout）以 GPT-5 约 1% 的成本达到超人表现（82% 胜率）。

**[SONIC: Spectral Oriented Neural Invariant Convolutions](sonic_spectral_oriented_neural_invariant_convolutions.md)**

:   SONIC 提出了一种基于连续频谱参数化的卷积算子，利用少量共享的方向选择性分量在频域中建模全局感受野，在合成基准、大规模图像分类和3D医学数据集上以数量级更少的参数匹配或超越CNN、ViT和现有频谱架构。

**[SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis](survhte-bench_a_benchmark_for_heterogeneous_treatment_effect_estimation_in_survi.md)**

:   提出 SurvHTE-Bench，首个面向右删失生存数据的异质处理效应（HTE）估计综合基准，涵盖 40 个合成数据集、10 个半合成数据集和 2 个真实数据集，系统评估了 53 种估计方法在不同因果假设违反和删失水平下的表现，发现没有单一方法占主导地位，生存 meta-learner（特别是 S-Learner-Survival 和 Matching-Survival）在高删失和假设违反场景下表现最为稳健。

**[SynCoGen: Synthesizable 3D Molecule Generation via Joint Reaction and Coordinate Modeling](syncogen_synthesizable_3d_molecule_generation_via_joint_reaction_and_coordinate_.md)**

:   SynCoGen 提出了一种结合掩码图扩散和流匹配的多模态生成框架，能够同时采样分子构建块反应图和3D原子坐标，在保证合成可行性的同时实现高质量的3D分子生成。

**[Thompson Sampling via Fine-Tuning of LLMs](thompson_sampling_via_fine-tuning_of_llms.md)**

:   提出 ToSFiT，通过微调大语言模型直接参数化最大概率（Probability of Maximality），将 Thompson Sampling 扩展到大规模非结构化离散空间，避免了获取函数最大化的难题。

**[Towards Interpretable Visual Decoding with Attention to Brain Representations](towards_interpretable_visual_decoding_with_attention_to_brain_representations.md)**

:   提出 NeuroAdapter，一个端到端的脑活动视觉解码框架，通过交叉注意力直接将 fMRI 信号接入潜在扩散模型，跳过中间特征空间，并通过 IBBI 可解释性框架分析各脑区对图像生成的贡献。

**[Tracing Pharmacological Knowledge in Large Language Models](tracing_pharmacological_knowledge_in_large_language_models.md)**

:   首次系统性地对生物医学 LLM 中药物分组语义的编码机制进行因果分析，发现药物组知识存储在早期层、分布在多个 token 上（非最后一个 token），线性可分的语义信息在嵌入层即已存在。

**[Ultra-Fast Language Generation via Discrete Diffusion Divergence Instruct](ultra-fast_language_generation_via_discrete_diffusion_divergence_instruct.md)**

:   提出 DiDi-Instruct，一种基于积分 KL 散度 (IKL) 最小化的蒸馏框架，将预训练的扩散大语言模型 (dLLM) 蒸馏为少步学生模型，通过对抗性密度比估计 + 分组奖励归一化 + 分数分解 + 奖励引导祖先采样器 (RGAS) 四大关键设计，在 OpenWebText 上仅用 16 步即超越 1024 步教师模型的 PPL，实现最高 64× 推理加速，同时训练成本仅需 1 GPU 小时。

**[Unified Biomolecular Trajectory Generation via Pretrained Variational Bridge](unified_biomolecular_trajectory_generation_via_pretrained_variational_bridge.md)**

:   PVB（Pretrained Variational Bridge）通过编码器-解码器架构结合增强桥匹配，统一了单结构预训练和配对轨迹微调的训练目标，实现了跨领域生物分子轨迹生成，并通过RL微调加速蛋白质-配体holo态探索。

**[VLM-SubtleBench: How Far Are VLMs from Human-Level Subtle Comparative Reasoning?](vlm-subtlebench_how_far_are_vlms_from_human-level_subtle_comparative_reasoning.md)**

:   提出 VLM-SubtleBench，一个评估视觉语言模型在细微差异比较推理能力的基准，覆盖 10 种差异类型和 6 个图像领域（自然、游戏、工业、航空、医学、合成），揭示了 VLM 与人类在空间/时间/视角推理上超过 30% 的性能差距。
