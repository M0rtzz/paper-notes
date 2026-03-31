<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🧠 NeurIPS2025** · 共 **62** 篇

**[3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](3drad_a_comprehensive_3d_radiology_medvqa_dataset_with_multi.md)**

:   提出 3D-RAD——首个大规模3D医学VQA基准，包含170K条CT影像问答数据，覆盖六类临床任务（含创新性的多时相诊断任务），并配套136K训练集，揭示了现有VLM在3D时序推理上的严重不足。

**[A Novel Approach to Classification of ECG Arrhythmia Types with Latent ODEs](a_novel_approach_to_classification_of_ecg_arrhythmia_types_with_latent_odes.md)**

:   将 Latent ODE 编码器与梯度提升决策树结合，构建端到端 ECG 心律失常分类流水线，在 360Hz→45Hz 降采样下 AUC-ROC 仅从 0.984 降至 0.976，展示了对低采样率的鲁棒性。

**[A Unified Solution to Video Fusion: From Multi-Frame Learning to Benchmarking](a_unified_solution_to_video_fusion_from_multi-frame_learning_to_benchmarking.md)**

:   提出首个统一视频融合框架 UniVF（基于多帧学习 + 光流特征 warping + 时序一致性损失），并构建首个覆盖四大融合任务（多曝光、多焦点、红外-可见光、医学）的视频融合基准 VF-Bench，在全部子任务上取得 SOTA。

**[A Variational Manifold Embedding Framework for Nonlinear Dimensionality Reduction](a_variational_manifold_embedding_framework_for_nonlinear_dimensionality_reductio.md)**

:   提出一种变分流形嵌入框架，将降维问题形式化为最优嵌入映射的优化问题（最小化先验分布与数据分布pullback之间的KL散度），在理论上统一了PCA与非线性降维方法，并利用变分法（Euler-Lagrange方程）和Noether定理为最优嵌入提供了可解释性约束。

**[AANet: Virtual Screening under Structural Uncertainty via Alignment and Aggregation](aanet_virtual_screening_under_structural_uncertainty_via_alignment_and_aggregati.md)**

:   针对现实药物发现中蛋白质 holo 结构不可用的问题，提出 AANet——通过三模态对比学习（配体-holo pocket-检测cavity）对齐表征并用交叉注意力聚合多个候选结合位点，在 apo/predicted 蛋白质结构上的盲筛性能远超 SOTA（DUD-E 上 EF1% 从 11.75 提升至 37.19）。

**[Active Target Discovery under Uninformative Prior: The Power of Permanent and Transient Memory](active_target_discovery_under_uninformative_prior_the_power_of_permanent_and_tra.md)**

:   提出 EM-PTDM 框架，受神经科学双记忆系统启发，利用预训练扩散模型作为"永久记忆"并结合基于 Doob's h-transform 的轻量"瞬时记忆"模块，在**无领域先验数据**的条件下实现高效的主动目标发现，理论保证先验单调改进。

**[Amortized Active Generation of Pareto Sets](amortized_active_generation_of_pareto_sets.md)**

:   提出 A-GPS 框架，通过学习 Pareto 集的条件生成模型实现在线离散黑箱多目标优化——用非支配类概率估计器（CPE）作为 PHVI 的隐式估计替代显式超体积计算，并通过偏好方向向量实现摊还式后验偏好条件化（无需重新训练），在合成基准和蛋白质设计任务上展示了优越的样本效率。

**[AQuaMaM: An Autoregressive Quaternion Manifold Model for Rapidly Estimating Complex Protein Structures](aquamam_an_autoregressive_quaternion_manifold_model_for_rapidly_estimating_compl.md)**

:   AQuaMaM 提出基于四元数流形的自回归蛋白质结构预测模型——将蛋白质骨架的旋转表示为四元数（在 $S^3$ 流形上），用自回归方式沿序列逐步预测每个残基的局部坐标系旋转，实现比 AlphaFold 快数个量级的结构估计。

**[Atomic Diffusion Models for Small Molecule Structure Elucidation from NMR Spectra](atomic_diffusion_models_for_small_molecule_structure_elucidation_from_nmr_spectr.md)**

:   提出 ChefNMR，首个基于 3D 原子扩散模型的端到端框架，仅从 1D NMR 光谱和化学式直接预测未知小分子（尤其是复杂天然产物）的分子结构，在合成和实验数据集上均达到 SOTA。

**[GraphFLA: Augmenting Biological Fitness Prediction Benchmarks with Landscape Features](augmenting_biological_fitness_prediction_benchmarks_with_landscapes_features_fro.md)**

:   GraphFLA 是一个高效的适应度景观分析框架——计算 20 个生物学意义的景观特征（粗糙度/上位性/可导航性/中性），在 5300+ 真实景观（ProteinGym/RNAGym/CIS-BP）上揭示模型性能高度依赖景观拓扑，如 VenusREM 在高可导航性景观上优于 ProSST 但在高上位性景观上弱于后者，处理百万突变体仅需 20 秒（vs MAGELLAN 5 小时）。

**[Autoencoding Random Forests](autoencoding_random_forests.md)**

:   RFAE 首次为随机森林构建了原则性的编码-解码框架——利用 RF 核的正定性和普适性进行扩散映射谱分解得到低维编码，通过 k-NN 回归在叶节点空间中解码回原始特征，在 20 个表格数据集上重建质量排名 1.80（大幅优于 TVAE 3.38、AE 3.27），并成功应用于 MNIST 重建和 scRNA-seq 批次效应去除。

**[BarcodeMamba+: Advancing State-Space Models for Fungal Biodiversity Research](barcodemamba_advancing_state-space_models_for_fungal_biodiversity_research.md)**

:   BarcodeMamba+ 是用于真菌 DNA 条形码分类的基础模型——基于状态空间模型架构，采用预训练+微调范式利用部分标注数据，结合层次标签平滑、加权损失和多头输出增强真菌分类（93%样本种级未标注），在所有分类层级上超越现有方法。

**[CrossNovo: Bidirectional Representations Augmented Autoregressive Biological Sequence Generation](bidirectional_representations_augmented_autoregressive_biological_sequence_gener.md)**

:   CrossNovo 融合自回归（AR）和非自回归（NAR）解码器，通过共享谱编码器 + 重要性退火 + 梯度阻断知识蒸馏，让 NAR 的双向全局理解增强 AR 的序列生成能力，在 9-Species 基准上氨基酸精度达 0.811（+2.6%）、肽段召回 0.654（+5.3%）。

**[Brain-Tuning Improves Generalizability And Efficiency Of Brain Alignment In Spee](brain-tuning_improves_generalizability_and_efficiency_of_brain_alignment_in_spee.md)**

:   提出 Multi-brain-tuning 方法，通过联合多个被试的 fMRI 数据微调预训练语音模型，将脑对齐所需数据量降低 5 倍，同时脑对齐度提升最高 50%，并可泛化到全新被试和数据集。

**[Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens](brain_harmony_a_multimodal_foundation_model_unifying_morphology_and_function_int.md)**

:   首个统一脑结构形态（T1 sMRI）与功能动态（fMRI）的多模态脑基础模型，通过几何谐波预对齐和时序自适应 Patch Embedding（TAPE）将高维神经影像压缩为紧凑的 1D token 表示，在神经发育/退行性疾病诊断和认知预测任务上全面超越先前方法。

**[Bridging Graph and State-Space Modeling for Intensive Care Unit Length of Stay Prediction](bridging_graph_and_state-space_modeling_for_intensive_care_unit_length_of_stay_p.md)**

:   提出 S2G-Net，将 Mamba 状态空间模型的时序编码与多视图图神经网络（GraphGPS）进行双路融合，用于 ICU 住院时长（LOS）预测，在 MIMIC-IV 数据集上全面超越序列模型、图模型和混合基线。

**[Care-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson's Disease Gait Assessment](care-pd_a_multi-site_anonymized_clinical_dataset_for_parkinsons_disease_gait_ass.md)**

:   发布 Care-PD——目前最大的面向帕金森病步态分析的多站点匿名 3D 网格数据集（9 个队列、8 个临床中心、362 名受试者、8477 段步行），并在 UPDRS 步态评分和运动预训练任务上提供系统性 benchmark，证明在 Care-PD 上微调可将 MPJPE 从 60.8mm 降至 7.5mm，F1 提升 17 个百分点。

**[CGBench: Benchmarking Language Model Scientific Reasoning for Clinical Genetics Research](cgbench_benchmarking_language_model_scientific_reasoning_for_clinical_genetics_r.md)**

:   提出 CGBench，一个基于 ClinGen 专家标注的临床遗传学 benchmark，从变异和基因策展角度评估 LLM 的科学文献推理能力，涵盖证据评分、证据验证和实验证据提取三个任务，发现推理模型在细粒度任务上表现最佳但在高层判断上不如非推理模型。

**[CodeCrash: Exposing LLM Fragility to Misleading Natural Language in Code Reasoning](codecrash_exposing_llm_fragility_to_misleading_natural_language_in_code_reasonin.md)**

:   提出 CodeCrash 压力测试框架，通过功能等价的结构扰动和误导性自然语言注入（注释/print/暗示），系统评估 17 个 LLM 的代码推理鲁棒性，揭示模型平均性能下降 23.2%，CoT 仅能挽回至 13.8%，并首次发现大推理模型（LRM）中的 "Reasoning Collapse" 现象。

**[Compressing Biology: Evaluating the Stable Diffusion VAE for Phenotypic Drug Discovery](compressing_biology_evaluating_the_stable_diffusion_vae_for_phenotypic_drug_disc.md)**

:   首次系统评估 Stable Diffusion VAE（SD-VAE）在 Cell Painting 显微镜图像上的重建质量，发现 SD-VAE 在像素级和生物信号层面均能良好保留表型信息（FR 几乎无下降），且通用特征提取器 InceptionV3 在检索任务上与领域专用模型 OpenPhenom 持平甚至更优。

**[ConfRover: Simultaneous Modeling of Protein Conformation and Dynamics via Autoregression](confrover_simultaneous_modeling_of_protein_conformation_and_dynamics_via_autoreg.md)**

:   ConfRover 提出自回归框架将蛋白质 MD 轨迹分解为逐帧条件生成 $p(\mathbf{x}^{1:L}) = \prod_l p(\mathbf{x}^l | \mathbf{x}^{<l})$，通过编码器 + 因果 Transformer + SE(3) 扩散解码器的模块化架构，首次在单一模型中统一轨迹模拟、时间无关构象采样和构象插值三大任务，在 ATLAS 数据集上全面超越 MDGen。

**[Convolutional Monge Mapping between EEG Datasets to Support Independent Component Labeling](convolutional_monge_mapping_between_eeg_datasets_to_support_independent_componen.md)**

:   本文扩展 CMMN（Convolutional Monge Mapping Normalization）方法，提出通道平均 PSD + $\ell_1$ 归一化质心和 subject-to-subject 匹配两种策略，生成单一时域滤波器实现不同通道数的 EEG 数据集间域适应，在独立成分（IC）脑/非脑分类中 F1 从 0.77 提升至 0.84，超越 ICLabel（0.88→0.91）。

**[CureAgent: A Training-Free Executor-Analyst Framework for Clinical Reasoning](cureagent_a_training-free_executor-analyst_framework_for_clinical_reasoning.md)**

:   CureAgent 提出 Executor-Analyst 协作框架，将精确工具调用（TxAgent/Llama-8B 做 Executor）与高层临床推理（Gemini 2.5 做 Analyst）解耦，配合分层集成（Stratified Ensemble）的 Late Fusion 拓扑保留证据多样性，在 CURE-Bench 上达到 83.8% 准确率（无需端到端微调），揭示了上下文-性能悖论和动作空间维度灾难两个关键 scaling 发现。

**[CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays](cxreasonbench_a_benchmark_for_evaluating_structured_diagnostic_reasoning_in_ches.md)**

:   提出 CheXStruct + CXReasonBench，一个基于胸部X光的结构化诊断推理评估框架，通过多路径、多阶段评估揭示现有 LVLM 在中间推理步骤上的严重不足。

**[DCA: Graph-Guided Deep Embedding Clustering for Brain Atlases](dca_graph-guided_deep_embedding_clustering_for_brain_atlases.md)**

:   DCA（Deep Cluster Atlas）提出图引导深度嵌入聚类框架，结合预训练 Swin-UNETR 的体素级时空嵌入和 KNN 图空间正则化，通过 KL 散度对齐软分配与图谱聚类辅助标签，生成功能一致且空间连续的个性化脑图谱，在 HCP 数据集上同态性提升 98.8%、轮廓系数提升 29%，并在自闭症诊断、认知解码等下游任务中超越现有图谱。

**[De novo generation of functional terpene synthases using TpsGPT](de_novo_generation_of_functional_terpene_synthases_using_tpsgpt.md)**

:   TpsGPT 通过在 79K 萜烯合酶（TPS）序列上微调蒸馏版 ProtGPT2 Tiny（38.9M 参数），生成 28K 候选序列，经多阶段过滤（困惑度/pLDDT/EnzymeExplorer/CLEAN/InterPro/Foldseek）筛选出 7 条进化距离远（<60% 序列相似度）但结构保守的从头 TPS 序列，湿实验验证其中 2 条具有 TPS 酶活性——以不到 $200 GPU 成本实现功能酶从头设计。

**[Demo: Generative AI helps Radiotherapy Planning with User Preference](demo_generative_ai_helps_radiotherapy_planning_with_user_preference.md)**

:   提出 Flexible Dose Proposer (FDP)，通过两阶段训练框架（VQ-VAE 预训练 + 多条件编码）实现基于滑块的用户偏好交互式 3D 剂量分布预测，并集成到 Eclipse 临床治疗计划系统中，在头颈部癌症放疗场景中超越 Varian RapidPlan。

**[Demo: Guide-RAG: Evidence-Driven Corpus Curation for Retrieval-Augmented Generation in Long COVID](demo_guide-rag_evidence-driven_corpus_curation_for_retrieval-augmented_generatio.md)**

:   系统评估了六种 RAG 语料库配置用于长新冠（Long COVID）临床问答，发现将临床指南与高质量系统综述结合的 GS-4 配置在 faithfulness、relevance 和 comprehensiveness 三维度上一致优于单指南和大规模文献库方案，并提出 Guide-RAG 框架和 LongCOVID-CQ 评估数据集。

**[DermaCon-IN: A Multi-concept Annotated Dermatological Image Dataset of Indian Skin Disorders](dermacon-in_a_multi-concept_annotated_dermatological_image_dataset_of_indian_ski.md)**

:   构建了 DermaCon-IN——首个以印度肤色为主的密集标注皮肤病图像数据集（5,450 张 / 3,002 患者 / 245 种诊断），提供三级层次诊断标签、47 个病灶描述符和 49 个解剖位置标注，并用 CNN/ViT/概念瓶颈模型进行基准评测。

**[DesignX: Human-Competitive Algorithm Designer for Black-Box Optimization](designx_human-competitive_algorithm_designer_for_black-box_optimization.md)**

:   提出 DesignX，首个统一学习算法工作流生成和超参数动态控制两个子任务的自动算法设计框架，通过双 Transformer 智能体在 10k 合成问题上大规模预训练，在合成测试集和蛋白质对接/AutoML/UAV 路径规划等真实场景中超越人类手工设计的优化器。

**[DIsoN: Decentralized Isolation Networks for Out-of-Distribution Detection in Medical Imaging](dison_decentralized_isolation_networks_for_out-of-distribution_detection_in_medi.md)**

:   提出 Decentralized Isolation Networks (DIsoN)，通过训练二分类器将测试样本从训练数据中"隔离"来检测 OOD，并通过去中心化参数交换实现在不共享数据的情况下利用训练数据信息，在 4 个医学影像数据集 12 个 OOD 检测任务上取得 SOTA。

**[Ditch the Denoiser: Emergence of Noise Robustness in Self-Supervised Learning from Data Curriculum](ditch_the_denoiser_emergence_of_noise_robustness_in_self-supervised_learning_fro.md)**

:   提出一种全自监督的噪声鲁棒表示学习框架，通过"去噪→噪声"的数据课程学习策略 + 去噪教师正则化，使 DINOv2 等 SSL 模型在推理时无需去噪器即可直接处理噪声输入，在 ImageNet-1k 极端高斯噪声下线性探测精度提升 4.8%。

**[Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](doctor_approved_generating_medically_accurate_skin_disease_images_through_ai-exp.md)**

:   提出 MAGIC 框架，通过将皮肤科专家定义的临床检查清单转化为 MLLM（如 GPT-4o）可执行的评估反馈，利用 DPO 或奖励模型微调扩散模型，生成临床准确的皮肤病图像用于数据增强，在 20 类皮肤病分类任务上提升 +9.02%，少样本场景提升 +13.89%。

**[Domain-Adaptive Transformer for Data-Efficient Glioma Segmentation in Sub-Saharan MRI](domain-adaptive_transformer_for_data-efficient_glioma_segmentation_in_sub-sahara.md)**

:   提出 SegFormer3D+，一种面向撒哈拉以南非洲异质 MRI 数据的域自适应 Transformer 架构，通过直方图匹配、影像组学分层采样、频率感知双路径编码器和双注意力机制，在仅 60 例标注数据微调下实现胶质瘤分割 mean Dice 0.81，超越 nnU-Net +2.5%。

**[Dual Mixture-of-Experts Framework for Discrete-Time Survival Analysis](dual_mixture-of-experts_framework_for_discrete-time_survival_analysis.md)**

:   提出双混合专家（Dual MoE）框架用于离散时间生存分析，结合特征编码器 MoE（建模患者亚组异质性）与风险网络 MoE（捕获时间动态），在 METABRIC 和 GBSG 乳腺癌数据集上提升 time-dependent C-index 最高 0.04。

**[DyG-Mamba: Continuous State Space Modeling on Dynamic Graphs](dyg-mamba_continuous_state_space_modeling_on_dynamic_graphs.md)**

:   DyG-Mamba 将连续状态空间模型（SSM）引入动态图学习，设计时间跨度感知的连续 SSM——用 Ebbinghaus 遗忘曲线启发的指数衰减函数建模不规则时间间隔，配合谱范数约束的输入依赖参数实现 Lipschitz 鲁棒性，在 12 个动态图基准上平均排名 2.42（vs DyGFormer 2.92），且保持 $O(bdL)$ 线性复杂度。

**[EDBench: Large-Scale Electron Density Data for Molecular Modeling](edbench_large-scale_electron_density_data_for_molecular_modeling.md)**

:   构建了目前最大规模的电子密度（ED）数据集 EDBench（330 万分子，基于 B3LYP/6-31G** DFT 计算），并设计了涵盖预测、检索、生成三类任务的 ED 基准评估体系，首次系统评估了深度学习模型对电子密度的理解和利用能力。

**[Efficient Adaptive Experimentation with Noncompliance](efficient_adaptive_experimentation_with_noncompliance.md)**

:   提出 AMRIV——首个面向带非依从性（noncompliance）的自适应实验的半参数高效、多重鲁棒的ATE估计器，结合方差最优的工具变量分配策略和序贯推断保证。

**[EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis](endobench_a_comprehensive_evaluation_of_multi-modal_large_language_models_for_en.md)**

:   提出 EndoBench，首个覆盖 4 种内窥镜场景、12 项临床任务、5 级视觉提示粒度的综合 MLLM 评估基准，包含 6,832 个经临床验证的 VQA 对，对 23 个 MLLM 的评估显示商用模型整体领先但仍落后人类专家。

**[Energy Matching: Unifying Flow Matching and Energy-Based Models for Generative Modeling](energy_matching_unifying_flow_matching_and_energy-based_models_for_generative_mo.md)**

:   提出 Energy Matching，通过学习一个时间无关的标量势能场统一流匹配与能量模型：远离数据流形时沿最优传输路径高效传输，靠近流形时过渡为 Boltzmann 平衡分布以建模似然，在 CIFAR-10 上 FID 3.34 大幅超越现有 EBM（>50%提升）。

**[Ewc-Guided Diffusion Replay For Exemplar-Free Continual Learning In Medical Imag](ewc-guided_diffusion_replay_for_exemplar-free_continual_learning_in_medical_imag.md)**

:   提出将类条件 DDPM 扩散重放与弹性权重巩固（EWC）相结合的无样本持续学习框架，在 MedMNIST v2（8 个 2D/3D 任务）和 CheXpert 上实现了 AUROC 0.851，相比 DER++ 遗忘率降低超 30%，接近联合训练上界（0.869），同时完全无需存储患者原始数据。

**[Exploring and Leveraging Class Vectors for Classifier Editing](exploring_and_leveraging_class_vectors_for_classifier_editing.md)**

:   提出 Class Vector（类向量），通过计算预训练与微调模型在潜空间中类别质心的差异来捕获类别级适应，利用线性和独立性两个性质，通过简单向量算术实现分类器编辑（遗忘、环境适应、对抗防御），无需重训练即可完成潜空间注入，或用 <1.5K 参数在 1.5 秒内完成权重空间映射。

**[FairGRPO: Fair Reinforcement Learning for Equitable Clinical Reasoning](fairgrpo_fair_reinforcement_learning_for_equitable_clinical_reasoning.md)**

:   提出 FairGRPO，一种层级式公平强化学习算法，通过自适应重要性加权（基于群体表示量和任务难度）解决临床 AI 中的人群表现差异问题，在 7 个临床数据集（280K样本，5种模态）上将预测平价降低 27.2%、F1 提升 12.49%，并发布首个公平性优化的临床 VLLM——FairMedGemma-4B。

**[Faithful Summarization of Consumer Health Queries: A Cross-Lingual Framework with LLMs](faithful_summarization_of_consumer_health_queries_a_cross-lingual_framework_with.md)**

:   提出结合 TextRank 抽取式句子选择和医学命名实体识别 (NER) 来引导 LLM 生成忠实医学摘要的框架，在英文 MeQSum 和孟加拉语 BanglaCHQ-Summ 数据集上通过微调 LLaMA-2-7B 实现质量和忠实性的一致提升，SummaC 达 0.57，人工评估 82% 摘要保留关键医学信息。

**[Fapex Fractional Amplitude-Phase Expressor For Robust Cross-Subject Seizure Pred](fapex_fractional_amplitude-phase_expressor_for_robust_cross-subject_seizure_pred.md)**

:   提出 FAPEX 框架，通过可学习的分数阶神经帧算子 (FrNFO) 实现自适应时频分解，结合幅度-相位交叉编码和空间相关性聚合，在 12 个跨物种、跨模态的癫痫预测基准上全面超越 33 个基线方法。

**[Far from the Shallow: Brain-Predictive Reasoning Embedding through Residual Disentanglement](far_from_the_shallow_brain-predictive_reasoning_embedding_through_residual_disen.md)**

:   提出残差解纠缠方法，将 LLM 隐藏状态分离为词汇、句法、语义、推理四个近正交嵌入，用于预测颅内 ECoG 脑信号，发现推理信号在时间上（~350-400ms）和空间上（超越经典语言区扩展至视觉皮层）均具有独立的神经特征，揭示了 LLM 与人脑间的推理计算对齐。

**[Few-Shot Learning from Gigapixel Images via Hierarchical Vision-Language Alignment and Modeling](few-shot_learning_from_gigapixel_images_via_hierarchical_vision-language_alignme.md)**

:   提出 HiVE-MIL，一个层级视觉-语言 MIL 框架，通过构建统一异构图建模跨尺度层级关系（5× 和 20×）和同尺度多模态对齐，配合文本引导的动态过滤机制和层级对比损失，在 TCGA 肺/乳腺/肾癌三个数据集的 16-shot 设置下全面超越已有方法，Macro F1 最高提升 4.1%。

**[FGBench: A Dataset and Benchmark for Molecular Property Reasoning at Functional Group-Level](fgbench_a_dataset_and_benchmark_for_molecular_property_reasoning_at_functional_g.md)**

:   FGBench 构建了首个官能团级分子属性推理基准（625K QA 对，覆盖 245 个官能团），通过相似分子配对 + AccFG 标注 + 重建验证确保数据质量，揭示即使 o3-mini 在交互任务上也仅 69.3%，化学专用模型（ChemLLM）甚至仅 23.3%。

**[FireGNN: Neuro-Symbolic Graph Neural Networks with Trainable Fuzzy Rules for Interpretable Medical Image Classification](firegnn_neuro-symbolic_graph_neural_networks_with_trainable_fuzzy_rules_for_inte.md)**

:   提出 FireGNN，首次将可训练模糊规则嵌入 GNN 前向传播中，利用节点度、聚类系数和标签一致性三个拓扑描述子实现内生可解释的医学图像分类，在 5 个 MedMNIST 数据集和 MorphoMNIST 上取得优于标准 GCN/GAT/GIN 及辅助任务方法的性能。

**[Flow Density Control: Generative Optimization Beyond Entropy-Regularized Fine-Tuning](flow_density_control_generative_optimization_beyond_entropy-regularized_fine-tun.md)**

:   提出 Flow Density Control（FDC），将预训练流/扩散模型的微调从 KL 正则期望奖励最大化推广到**任意分布效用函数 + 任意散度正则**的通用框架，通过将非线性目标分解为一系列线性微调子任务实现，并提供收敛保证。

**[FOXES: A Framework For Operational X-ray Emission Synthesis](foxes_a_framework_for_operational_x-ray_emission_synthesis.md)**

:   提出 FOXES，一个基于 Vision Transformer 的框架，将太阳多通道 EUV 观测图像翻译为软 X 射线（SXR）通量，整体 Pearson 相关达到 0.982，为远端太阳耀斑检测和更完整的耀斑目录构建奠定基础。

**[Fractional Diffusion Bridge Models](fractional_diffusion_bridge_models.md)**

:   提出分数扩散桥模型（FDBM），将分数布朗运动（fBM）引入生成扩散桥框架，通过 Hurst 指数 $H$ 控制轨迹的粗糙度和长程依赖性，在蛋白质构象预测和图像翻译任务上超越布朗运动基线。

**[From Black Box to Biomarker: Sparse Autoencoders for Interpreting Speech Models of Parkinson's Disease](from_black_box_to_biomarker_sparse_autoencoders_for_interpreting_speech_models_o.md)**

:   将大语言模型可解释性研究中的稀疏自编码器（SAE）技术适配到语音帕金森病检测系统中，提出 Mask-based SAE 解决小数据集限制，发现模型预测主要基于低能量区域的频谱通量和频谱平坦度，并进一步揭示这些特征与 MRI 壳核体积显著相关，建立了从模型内部表征到临床生物标志物的桥梁。

**[Generative Distribution Embeddings: Lifting Autoencoders to the Space of Distributions for Multiscale Representation Learning](generative_distribution_embeddings_lifting_autoencoders_to_the_space_of_distribu.md)**

:   提出生成分布嵌入（GDE），将自编码器提升到分布空间——编码器作用于样本集合，解码器替换为条件生成模型，学习分布级别的表示，并在6个计算生物学任务上验证有效性。

**[Generative Modeling Of Full-Atom Protein Conformations Using Latent Diffusion On](generative_modeling_of_full-atom_protein_conformations_using_latent_diffusion_on.md)**

:   提出 **LD-FPG** 框架，使用 Chebyshev 图神经网络将蛋白质全原子 MD 轨迹编码到低维潜在空间，再用 DDPM 在该空间中生成新的构象集合体（ensemble），首次实现了包含侧链所有重原子的蛋白质构象生成。

**[H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis](h-ddx_a_hierarchical_evaluation_framework_for_differential_diagnosis.md)**

:   H-DDx 提出基于 ICD-10 分类层级的鉴别诊断评估框架——将预测和真实诊断扩展到祖先节点后计算层级 F1（HDF1），奖励"临床相关的近似正确"而非仅精确匹配，评估 22 个 LLM 后发现领域特化模型（MediPhi）在 HDF1 上从第 20 名升至第 2 名（Top-5 指标完全遮蔽其优势）。

**[LoMix: Learnable Weighted Multi-Scale Logits Mixing for Medical Image Segmentation](lomix_learnable_weighted_multi-scale_logits_mixing_for_medical_image_segmentatio.md)**

:   LoMix 提出通过组合突变模块（CMM）生成多尺度 logits 的"突变体"——4 种融合算子（加法/乘法/拼接/注意力加权）× 所有子集组合——配合 NAS 风格的 Softplus 可学习权重自动平衡各 logits 的贡献，在 Synapse 8 器官分割上 DICE 从 80.9% 提升到 85.1%（+4.2%），5% 训练数据下提升 +9.23%。

**[Posterior Sampling by Combining Diffusion Models with Annealed Langevin Dynamics](posterior_sampling_by_combining_diffusion_models_with_annealed_langevin_dynamics.md)**

:   提出将扩散模型与退火 Langevin 动力学结合的算法，仅需 $L^4$ 精度的 score 估计即可在（局部）对数凹分布下实现多项式时间的后验采样，首次为带暖启动的逆问题求解提供理论保障。

**[QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](qoq-med_building_multimodal_clinical_foundation_models_with_domain-aware_grpo_tr.md)**

:   QoQ-Med 构建了覆盖 9 个临床模态（1D ECG + 6 类 2D 影像 + 2 类 3D 扫描）的多模态临床基础模型，提出域感知相对策略优化（DRPO）——通过层级温度缩放（域间 × 域内 K-means 聚类）解决模态/难度不平衡问题，在 261 万指令调优对上训练后平均 F1 达 0.295（vs GRPO 0.193，+52.8%），8 个模态中 6 个最优。

**[SpecMER: Fast Protein Generation with K-mer Guided Speculative Decoding](specmer_fast_protein_generation_with_k-mer_guided_speculative_decoding.md)**

:   SpecMER 将投机解码引入蛋白质序列生成，用 K-mer 引导的批量选择策略从 draft 模型的多个候选中选取最符合进化保守性的序列供 target 模型验证，在保持分布一致性的同时实现 24-32% 加速，且生成序列的 NLL 和 pLDDT 结构置信度显著优于无引导的 baseline。

**[STAMP: Spatial-Temporal Adapter with Multi-Head Pooling](stamp_spatial-temporal_adapter_with_multi-head_pooling.md)**

:   STAMP 为时间序列基础模型（TSFM）设计了仅 750K 参数的轻量空间-时间适配器，通过三组位置编码（token/空间/时间）+ 交叉 GMLP 混合 + 多头注意力池化，使冻结的 TSFM（如 MOMENT 385M）在 8 个 EEG 数据集上与 29M 参数的 EEG 专用模型（CBraMod）竞争或超越，在 BCIC-IV-2a 上 Kappa 比 CBraMod 高 193%。

**[The Biased Oracle: Assessing LLMs' Understandability and Empathy in Medical Diagnoses](the_biased_oracle_assessing_llms_understandability_and_empathy_in_medical_diagno.md)**

:   系统评估 GPT-4o 和 Claude-3.7 在医疗诊断沟通中的可读性和共情能力，发现两者均产生超标的阅读难度（9-13 年级 vs 推荐的 6-8 年级），情感共情随诊断类型和患者教育水平显著变化，且 LLM-as-Judge 存在严重自我偏见（GPT 对自身共情评分膨胀 ~0.3 分）。
