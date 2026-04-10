<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🤖 AAAI2026** · 共 **29** 篇

**[A Disease-Aware Dual-Stage Framework for Chest X-ray Report Generation](a_disease-aware_dual-stage_framework_for_chest_x-ray_report_.md)**

:   提出一种两阶段疾病感知框架，通过学习14个与病理类别对应的疾病感知语义token（DASTs）实现显式的疾病表征，再利用疾病-视觉注意力融合（DVAF）和双模态相似性检索（DMSR）机制辅助LLM生成临床准确的胸部X光报告，在CheXpert Plus、IU X-Ray和MIMIC-CXR三个数据集上取得SOTA。

**[A Principle-Driven Adaptive Policy for Group Cognitive Stimulation Dialogue for Elderly with Cognitive Impairment](a_principle-driven_adaptive_policy_for_group_cognitive_stimu.md)**

:   针对老年认知障碍患者的群体认知刺激治疗（CST）场景，提出GCSD系统：通过多说话人上下文控制、动态参与者状态建模（soft prompt）、认知刺激注意力损失和多维奖励策略优化四个模块，基于Qwen-2.5-3B微调，在500+小时真实粤语CST对话和1万+模拟对话上训练，BLEU-4达27.93超越GPT-4o等大模型，A/B测试胜率50% vs GPT-4o的39%。

**[Advancing Safe Mechanical Ventilation Using Offline RL With Hybrid Actions and Clinically Aligned Rewards](advancing_safe_mechanical_ventilation_using_offline_rl_with_.md)**

:   针对ICU机械通气（MV）设置优化问题，提出混合动作空间的离线RL方法（HybridIQL/HybridEDAC），避免传统离散化导致的分布偏移，同时引入基于无通气天数（VFD）和生理参数安全范围的临床对齐奖励函数，通过多目标优化选择最优奖励，将可优化的通气参数从2-3个扩展到6个，HybridIQL在性能和策略覆盖率间取得最佳平衡。

**[Ambiguity-aware Truncated Flow Matching for Ambiguous Medical Image Segmentation](ambiguity-aware_truncated_flow_matching_for_ambiguous_medica.md)**

:   提出 ATFM 框架，通过数据层级推理范式将预测精度和多样性解耦到分布级和样本级分别优化，结合高斯截断表示（GTR）和分割流匹配（SFM）两个模块，在模糊医学图像分割任务中同时提升预测的精度、保真度和多样性。

**[Apo2Mol: 3D Molecule Generation via Dynamic Pocket-Aware Diffusion Models](apo2mol_3d_molecule_generation_via_dynamic_pocket-aware_diff.md)**

:   提出Apo2Mol，一个基于扩散的全原子框架，从蛋白质apo（未结合）构象出发，同时生成3D配体分子和对应的holo（结合态）口袋构象，使用24K实验解析的apo-holo结构对训练，在结合亲和力（Vina min -7.86）和药物类似性上达到SOTA。

**[Bayesian Meta-Analyses Could Be More: A Case Study in Trial of Labor After a Cesarean-section Outcomes and Complications](bayesian_meta-analyses_could_be_more_a_case_study_in_trial_of_labor_after_a_cesa.md)**

:   提出一种层次贝叶斯 meta-analysis 方法，通过对未记录的决策变量（Bishop 分数）建模为截断隐变量，纠正传统固定效应 meta-analysis 中因忽略混杂因子而导致的偏差结论，在 TOLAC（剖宫产后试产）场景中证明机械扩张与 Pitocin 无显著差异。

**[BiCA: Effective Biomedical Dense Retrieval with Citation-Aware Hard Negatives](bica_effective_biomedical_dense_retrieval_with_citation-aware_hard_negatives.md)**

:   提出利用 PubMed 引文链构建多跳语义图并进行随机游走的 hard negative 挖掘方法，仅用 20k 训练样本和极少微调步数，即让 33M/110M 小模型在 BEIR 和 LoTTE 上超越数十亿参数的检索基线。

**[Bidirectional Channel-selective Semantic Interaction for Semi-Supervised Medical Segmentation](bidirectional_channel-selective_semantic_interaction_for_semi-supervised_medical.md)**

:   提出 BCSI 框架，通过通道选择路由器动态筛选关键特征通道，在标注和未标注数据流之间进行双向通道级交互，结合语义-空间扰动的弱到强一致性学习，显著提升半监督医学图像分割性能。

**[Bridging Vision and Language for Robust Context-Aware Surgical Point Tracking: The VL-SurgPT Dataset and Benchmark](bridging_vision_and_language_for_robust_context-aware_surgical_point_tracking_th.md)**

:   提出首个大规模多模态手术点追踪数据集 VL-SurgPT，结合视觉坐标与文本状态描述，并设计文本引导追踪方法 TG-SurgPT，通过语义信息显著提升复杂手术场景下的追踪精度和鲁棒性。

**[CD-DPE: Dual-Prompt Expert Network Based on Convolutional Dictionary Feature Decoupling for Multi-Contrast MRI Super-Resolution](cd-dpe_dual-prompt_expert_network_based_on_convolutional_dictionary_feature_deco.md)**

:   提出 CD-DPE 网络，通过迭代卷积字典特征解耦模块（CD-FDM）将多对比度 MRI 特征分离为跨对比度共有和模态特有成分，再利用双提示特征融合专家模块（DP-FFEM）进行自适应融合重建，在多个公开数据集上超越现有 SOTA 方法。

**[CliCARE: Grounding Large Language Models in Clinical Guidelines for Decision Support over Longitudinal Cancer Electronic Health Records](clicare_grounding_large_language_models_in_clinical_guidelines_for_decision_supp.md)**

:   提出 CliCARE 框架，将非结构化的纵向癌症电子病历（EHR）转化为时序知识图谱（TKG），并与临床指南知识图谱对齐融合，为 LLM 提供循证依据的临床决策支持，同时设计了与专家评估高度相关的 LLM-as-a-Judge 评估协议。

**[Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models](coarse-to-fine_open-set_graph_node_classification_with_large_language_models.md)**

:   提出 Coarse-to-Fine Classification (CFC) 框架，利用 LLM 的零样本推理能力为图节点开放集分类提供语义化 OOD 样本和潜在 OOD 标签空间，实现不仅检测 OOD 还能将其分类到具体未知类别的能力。

**[CoCoLIT: ControlNet-Conditioned Latent Image Translation for MRI to Amyloid PET Synthesis](cocolit_controlnet-conditioned_latent_image_translation_for_mri_to_amyloid_pet_s.md)**

:   提出 CoCoLIT 框架，基于 ControlNet 条件化的潜在扩散模型，从结构 MRI 合成淀粉样蛋白 PET 图像，通过加权图像空间损失（WISL）和潜在平均稳定化（LAS）显著超越现有方法。

**[Constrained Best Arm Identification with Tests for Feasibility](constrained_best_arm_identification_with_tests_for_feasibility.md)**

:   提出带可行性约束的最优臂识别新框架，允许决策者分别测试臂的性能或可行性约束，设计了渐近最优算法，可自适应地选择通过性能或可行性中更容易的方式淘汰次优臂。

**[Cross-Sample Augmented Test-Time Adaptation for Personalized Intraoperative Hypotension Prediction](cross-sample_augmented_test-time_adaptation_for_personalized_intraoperative_hypo.md)**

:   提出 CSA-TTA 框架，通过跨样本库构建、粗到细检索和多任务优化，在测试时从其他患者数据中检索低血压事件信号来增强个性化术中低血压预测。

**[Decoding with Structured Awareness: Integrating Directional, Frequency-Spatial, and Structural Attention for Medical Image Segmentation](decoding_with_structured_awareness_integrating_directional_frequency-spatial_and.md)**

:   提出面向医学图像分割的新型解码器框架，包含三个模块：方向感知的自适应交叉融合注意力（ACFA）、空间-频率-小波三分支融合注意力（TFFA）和结构感知多尺度掩码模块（SMMM），在多个基准数据集上超越现有方法。

**[DeepGB-TB: A Risk-Balanced Cross-Attention Gradient-Boosted Convolutional Network for Rapid, Interpretable Tuberculosis Screening](deepgb-tb_a_risk-balanced_cross-attention_gradient-boosted_convolutional_network.md)**

:   提出 DeepGB-TB，一个结合轻量级1D-CNN（处理咳嗽音频）和梯度提升决策树（处理人口统计特征）的多模态TB筛查系统，通过双向交叉注意力（CM-BCA）模拟临床推理过程融合异构数据，配合风险平衡损失（TRBL）最小化漏诊，在7国数据集上达到 AUROC 0.903，可在手机上离线实时运行。

**[DeNAS-ViT: Data Efficient NAS-Optimized Vision Transformer for Ultrasound Image Segmentation](denas-vit_data_efficient_nas-optimized_vision_transformer_for_ultrasound_image_s.md)**

:   提出 DeNAS-ViT，首次将 NAS 应用于 ViT 的 Token 级搜索实现超声图像分割的多尺度特征提取优化，并设计基于 NAS 约束的半监督学习框架（网络独立性损失+层次对比损失+阶段式优化），在有限标注数据下达到 SOTA。

**[DiA-gnostic VLVAE: Disentangled Alignment-Constrained Vision Language Variational AutoEncoder for Robust Radiology Reporting with Missing Modalities](dia-gnostic_vlvae_disentangled_alignment-constrained_vision_language_variational.md)**

:   提出 DiA-gnostic VLVAE，通过视觉-语言混合专家VAE学习三因子潜空间（视觉特有/语言特有/共享），配合正交性+对比对齐的双约束实现解纠缠，使模型在临床上下文缺失时仍能生成可靠的放射学报告，在 IU X-Ray 和 MIMIC-CXR 上达到竞争性 BLEU@4。

**[Divide, Conquer and Unite: Hierarchical Style-Recalibrated Prototype Alignment for Federated Medical Segmentation](divide_conquer_and_unite_hierarchical_style-recalibrated_prototype_alignment_for.md)**

:   针对联邦医学图像分割中的"层间风格偏差累积"和"上下文表征不完整"两大挑战，提出FedBCS框架：通过频域自适应风格重校准（FSR）构建领域不变原型，并设计上下文感知的双层原型对齐（CDPA）融合编解码器多层级语义，在组织核分割和前列腺MRI分割任务上达到SOTA。

**[EgoEMS: A High-Fidelity Multimodal Egocentric Dataset for Cognitive Assistance in Emergency Medical Services](egoems_a_high-fidelity_multimodal_egocentric_dataset_for_cognitive_assistance_in.md)**

:   发布首个高保真多人多模态自我中心EMS数据集，包含233个试验20小时视频、9项干预67个关键步骤标注，提供三个基准任务（步骤分类/在线分割/CPR质量估计）推动EMS认知协助系统开发。

**[Experience with Single Domain Generalization in Real World Medical Imaging Deployments](experience_with_single_domain_generalization_in_real_world_medical_imaging_deplo.md)**

:   提出DL+EKE框架，将领域不变的专家知识与深度学习集成，解决医学影像中稀有类（rare class）的单域泛化（SDG）问题，在糖尿病视网膜病变分级、rs-fMRI癫痫灶定位和应激心电图CAD检测三个真实部署场景中显著优于SOTA SDG方法。

**[Expert-Guided Prompting And Retrieval-Augmented Generation For Emergency Medical](expert-guided_prompting_and_retrieval-augmented_generation_for_emergency_medical.md)**

:   构建了首个 EMS 领域多选问答数据集 EMSQA（24.3K 题），并提出 Expert-CoT + ExpertRAG 框架，通过注入 subject area 和 certification level 等专业属性引导 LLM 推理和检索，最高带来 4.59% 的准确率提升。

**[Intervention Efficiency and Perturbation Validation Framework: Capacity-Aware and Robust Clinical Model Selection under the Rashomon Effect](intervention_efficiency_and_perturbation_validation_framework_capacity-aware_and.md)**

:   针对临床小样本、类别不平衡场景下多个模型性能相近（Rashomon Effect）导致的模型选择困难，提出 **Intervention Efficiency (IE)** 容量感知评估指标和 **Perturbation Validation Framework (PVF)** 鲁棒性验证框架，联合实现资源约束下的可靠模型选择。

**[Learning Cell-Aware Hierarchical Multi-Modal Representations for Robust Molecular Modeling](learning_cell-aware_hierarchical_multi-modal_representations.md)**

:   提出CHMR框架，将分子结构(1D/2D/3D)与细胞形态/基因表达等生物模态联合建模，通过结构感知的模态增强解决>90%的外部生物模态缺失问题，用树状向量量化(Tree-VQ)捕获分子-细胞-基因的层次化依赖关系，在9个benchmark的728个任务上超越SOTA，分类平均AUC提升3.6%，回归MAE降低17.2%。

**[Learning With Preserving For Continual Multitask Learning](learning_with_preserving_for_continual_multitask_learning.md)**

:   提出 Learning with Preserving (LwP) 框架，通过 Dynamically Weighted Distance Preservation (DWDP) 损失保持 latent space 的几何结构，在无需 replay buffer 的条件下解决 Continual Multitask Learning (CMTL) 中的灾难性遗忘，是唯一超越 single-task baseline 的方法。

**[Mergedna Context-Aware Genome Modeling With Dynamic Tokenization Through Token M](mergedna_context-aware_genome_modeling_with_dynamic_tokenization_through_token_m.md)**

:   提出 MergeDNA，通过可微分的 Token Merging 机制实现上下文感知的动态 DNA tokenization，结合层次化 autoencoder Transformer 和自适应 masked token modeling 预训练，在多个基因组 benchmark 上取得 SOTA。

**[PINGS-X: Physics-Informed Normalized Gaussian Splatting with Axes Alignment for Efficient Super-Resolution of 4D Flow MRI](pings-x_physics-informed_normalized_gaussian_splatting_with_axes_alignment_for_e.md)**

:   提出PINGS-X框架，将3D高斯溅射（3DGS）的显式表示思想引入物理信息超分辨率领域，通过归一化高斯溅射（NGS）、轴对齐高斯和高斯合并三项创新，在合成CFD和真实4D Flow MRI数据集上实现了比PINN快一个数量级的训练速度，同时保持更高的超分辨率精度。

**[ProtSAE: Disentangling and Interpreting Protein Language Models via Semantically-Guided Sparse Autoencoders](protsae_disentangling_and_interpreting_protein_language_models_via_semantically-.md)**

:   提出 ProtSAE，在稀疏自编码器训练中引入语义标注和领域本体知识作为引导信号，解决传统 SAE 的语义纠缠问题，使蛋白质语言模型的隐层特征与生物学概念（分子功能、生物过程、离子结合位点等）精准对齐，同时保持高重建保真度并支持概念级别的生成控制。
