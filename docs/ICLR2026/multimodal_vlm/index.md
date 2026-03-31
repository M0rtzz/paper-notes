<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**🔬 ICLR2026** · 共 **44** 篇

**[A-TPT: Angular Diversity Calibration Properties for Test-Time Prompt Tuning of Vision-Language Models](a-tpt_angular_diversity_calibration_properties_for_test-time_prompt_tuning_of_vi.md)**

:   提出 A-TPT 框架，通过最大化归一化文本特征在单位超球面上的最小成对角距离来促进角度多样性，解决测试时提示调优 (TPT) 中 VLM 预测过度自信导致的校准不良问题，在自然分布偏移和医学数据集上均优于现有 TPT 校准方法。

**[Adaptive Debiasing Tsallis Entropy for Test-Time Adaptation](adaptive_debiasing_tsallis_entropy_for_test-time_adaptation.md)**

:   提出将 Tsallis 熵（SE 的广义形式）引入 VLM 的 Test-Time Adaptation，并进一步发展为自适应去偏 Tsallis 熵（ADTE），为每个类别定制去偏参数 $q^l$，在不引入分布特定超参数的情况下比 Shannon 熵选择更可靠的高置信视图，在 ImageNet 及其 5 个变体和 10 个跨域 benchmark 上均超越 SOTA。

**[AgilePruner: An Empirical Study of Attention and Diversity for Adaptive Visual Token Pruning in LVLMs](agilepruner_an_empirical_study_of_attention_and_diversity_for_adaptive_visual_to.md)**

:   通过 erank（有效秩）和注意力熵的系统性实证分析，揭示了视觉 token 剪枝中注意力方法和多样性方法的互补特性——注意力方法抑制幻觉但覆盖有限，多样性方法覆盖全面但易引入幻觉——并据此提出基于图像复杂度自适应切换剪枝策略的 AgilePruner，在 9 个 benchmark 上表现稳健。

**[AQuA: Toward Strategic Response Generation for Ambiguous Visual Questions](aqua_toward_strategic_response_generation_for_ambiguous_visual_questions.md)**

:   提出 AQuA，首个按模糊度细粒度分级（4 级）的视觉问答数据集（7.2K 样本），为每级定义最优回应策略（直接回答/推断/列举/请求澄清），发现 GPT-5 和 Gemini 在模糊 VQA 上都过度自信地直接回答，通过 SFT+GRPO 训练的 3B 模型反而能超越闭源大模型的策略适应能力。

**[BioCAP: Exploiting Synthetic Captions Beyond Labels in Biological Foundation Models](biocap_exploiting_synthetic_captions_beyond_labels_in_biological_foundation_mode.md)**

:   提出 BioCAP，通过用 MLLM 生成 wiki 知识引导的合成描述性 caption（而非仅用物种标签）来训练生物学多模态基础模型，在 10 个物种分类 benchmark 上比 BioCLIP 平均提升 8.8%，在文本-图像检索任务上提升 21.3%。

**[Bongard-RWR+: Real-World Representations of Fine-Grained Concepts in Bongard Problems](bongard-rwr_real-world_representations_of_fine-grained_concepts_in_bongard_probl.md)**

:   构建 Bongard-RWR+，一个包含 5400 个 Bongard 问题的 benchmark，使用 VLM 流水线（Pixtral-12B + Flux.1-dev）自动生成真实感图像来表示抽象概念，系统评估揭示 SOTA VLM 在辨别细粒度视觉概念（如轮廓、旋转、角度）时表现挣扎，准确率低至 19%。

**[Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting (WS-COC)](bootstrapping_mllm_for_weakly-supervised_class-agnostic_object_counting.md)**

:   提出 WS-COC，首个基于 MLLM 的弱监督类无关目标计数框架，通过分而治之的对话微调（逐步缩小计数范围）、比较排序优化（学习图像间相对计数关系）和全局-局部计数增强三个策略，仅用图像级计数标注即可匹敌甚至超越全监督方法。

**[Breaking the Limits of Open-Weight CLIP: An Optimization Framework for Self-supervised Fine-tuning of CLIP](breaking_the_limits_of_open-weight_clip_an_optimization_framework_for_self-super.md)**

:   本文提出 TuneCLIP，一个自监督微调（SSFT）框架，通过两阶段设计——先恢复优化器统计量（OSR）消除冷启动偏差，再用带margin的铰链全局对比损失（HGCL）缓解假负样本过度惩罚——在不使用任何标签的条件下持续提升已有开源 CLIP 模型的通用性能，在 ImageNet 及变体上提升最高 +2.5%，在 DataComp 基准上提升 +1.2%。

**[Can Vision-Language Models Answer Face to Face Questions in the Real-World?](can_vision-language_models_answer_face_to_face_questions_in_the_real-world.md)**

:   提出 QIVD（Qualcomm Interactive Video Dataset），一个面对面实时问答 benchmark（2900 个视频+音频+时间戳标注），揭示现有 VLM 在实时情境理解上远落后人类（最佳模型 60% vs 人类 87%），主要瓶颈在指代消歧、回答时机判断和情境常识，微调可显著缩小差距。

**[Can Vision–Language Models Assess Graphic Design Aesthetics? A Benchmark, Evaluation, and Dataset Perspective](can_vision_language_models_assess_graphic_design_aesthetics_a_benchmark_evaluati.md)**

:   提出 AesEval-Bench，首个系统性评估 VLM 图形设计美学评估能力的 benchmark（4维度×12指标×3任务），发现现有 VLM（含推理增强型）在设计美学上表现有限，并通过 human-guided VLM labeling + indicator-grounded reasoning 构建训练数据，微调 7B 模型在精确定位任务上超过 GPT-5。

**[Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts](capacity-aware_inference_mitigating_the_straggler_effect_in_mixture_of_experts.md)**

:   针对 MoE 推理时因 token 分配不均导致的 Straggler Effect（最重负载专家决定整体延迟），提出 Capacity-Aware Token Drop（丢弃过载专家的低分 token）和 Expanded Drop（将溢出 token 重路由到本地低负载专家），在 Mixtral-8×7B 上实现 1.85× 加速且性能提升 0.2%。

**[Chart Deep Research in LVLMs via Parallel Relative Policy Optimization](chart_deep_research_in_lvlms_via_parallel_relative_policy_optimization.md)**

:   提出 PRPO（Parallel Relative Policy Optimization），通过在奖励维度和数据类型两个层面做并行解耦优化，解决 GRPO 在多维奖励信号干扰和异构数据梯度冲突下的训练瓶颈；同时构建 MCDR-Bench，基于"错误唯一性原则"将主观生成评估转化为客观错误识别，实现图表深度研究能力的量化评估。

**[CityLens: Evaluating Large Vision-Language Models for Urban Socioeconomic Sensing](citylens_evaluating_large_vision-language_models_for_urban_socioeconomic_sensing.md)**

:   构建 CityLens——迄今最大规模的城市社会经济感知 benchmark（17 城市、6 大领域、11 个预测任务），评估 17 个 LVLM 在直接预测、归一化估计、特征回归三种范式下从卫星/街景图像推断社会经济指标的能力，发现通用 LVLM 在多数任务上仍不及领域特化的对比学习方法。

**[Closing the Modality Gap Aligns Group-Wise Semantics](closing_the_modality_gap_aligns_group-wise_semantics.md)**

:   证明 CLIP 中的 modality gap 对实例级任务（检索）无关紧要但严重损害群组级任务（聚类），并提出由 Align True Pairs loss + Centroid Uniformity loss 组成的新目标函数，在双模态和三模态设置中将 gap 几乎降为零，大幅提升聚类 V-Measure（+10-17 分），同时保持检索性能。

**[Contamination Detection for VLMs using Multi-Modal Semantic Perturbation](contamination_detection_for_vlms_using_multi-modal_semantic_perturbation.md)**

:   提出多模态语义扰动方法检测 VLM 数据污染：用 LLM 生成密集描述 + Flux ControlNet 在保持图像构图的同时改变答案相关语义元素，污染模型因记忆原始图像-文本对而在扰动版本上失败，首次系统验证现有 LLM 检测方法在 VLM 上不可靠。

**[Cross-Modal Redundancy and the Geometry of Vision-Language Embeddings](cross-modal_redundancy_and_the_geometry_of_vision-language_embeddings.md)**

:   提出 Iso-Energy 假设（真正跨模态共享的概念在不同模态中应具有相同的平均激活能量），并设计 Aligned SAE 作为分析工具，揭示 VLM 嵌入空间中双模态原子承载跨模态对齐信号、单模态原子完全解释模态间隙的几何结构。

**[Customizing Visual Emotion Evaluation for MLLMs: An Open-vocabulary, Multifaceted, and Scalable Approach](customizing_visual_emotion_evaluation_for_mllms_an_open-vocabulary_multifaceted_.md)**

:   提出情感陈述判断（ESJ）任务和 INSETS 自动标注流水线，构建 MVEI benchmark，系统评估 MLLMs 的视觉情感感知能力，揭示当前模型在情感极性辨别和感知主观性理解上的显著不足。

**[Detecting Misbehaviors of Large Vision-Language Models by Evidential Uncertainty Quantification](detecting_misbehaviors_of_large_vision-language_models_by_evidential_uncertainty.md)**

:   提出 EUQ（Evidential Uncertainty Quantification），基于 Dempster-Shafer 证据理论将 LVLM 的认识不确定性分解为冲突（CF，内部矛盾）和无知（IG，信息缺失），单次前向传播即可检测幻觉、越狱、对抗攻击和 OOD 失败四类错误行为，AUROC 相对提升最高 10.5%。

**[Directional Embedding Smoothing for Robust Vision Language Models](directional_embedding_smoothing_for_robust_vision_language_models.md)**

:   将 RESTA（Randomized Embedding Smoothing and Token Aggregation）防御方法从 LLM 扩展到 VLM，发现方向性嵌入噪声（directional noise）在安全-实用性权衡上显著优于各向同性噪声（isotropic noise），可作为推理时的轻量防御层抵御多模态越狱攻击。

**[DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage](diva-grpo_enhancing_multimodal_reasoning_through_difficulty-adaptive_variant_adv.md)**

:   提出 DIVA-GRPO，通过动态评估问题难度、自适应生成不同难度的语义一致变体、并结合难度加权的局部-全局 advantage 估计，解决 GRPO 训练中的 reward sparsity 和 advantage vanishing 问题，在 7B 规模模型上实现 SOTA 多模态推理性能。

**[Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models](dynamic_multimodal_activation_steering_for_hallucination_mitigation_in_large_vis.md)**

:   提出动态多模态激活引导（DMAS），通过构建基于语义的真实性引导向量数据库和视觉感知引导向量，在推理时动态选择最相关的引导向量对关键注意力头进行干预，无需训练即可显著缓解LVLM幻觉，在MME上提升94.66分，在CHAIR上降低20.2%幻觉率。

**[Efficient Discriminative Joint Encoders for Large Scale Vision-Language Re-ranking](efficient_discriminative_joint_encoders_for_large_scale_vision-language_rerankin.md)**

:   提出EDJE（高效判别式联合编码器），通过将视觉特征提取离线化并用轻量级注意力适配器压缩视觉Token，实现50k图文对/秒的高吞吐推理，同时在Flickr（零样本）和COCO（微调）检索上匹配现有联合编码器的性能，每张图仅需49kB存储。

**[Enhanced Continual Learning of Vision-Language Models with Model Fusion](enhanced_continual_learning_of_vision-language_models_with_model_fusion.md)**

:   提出Continual Decoupling-Unifying（ConDU）框架，首次将模型融合引入VLM持续学习，通过维护统一模型并结合任务触发器进行解耦-统一迭代操作，在MTIL基准上平均性能超SOTA 2%，同时增强了零样本能力。

**[Error Notebook-Guided, Training-Free Part Retrieval in 3D CAD Assemblies via Vision-Language Models](error_notebook-guided_training-free_part_retrieval_in_3d_cad_assemblies_via_visi.md)**

:   提出一种无训练的两阶段VLM框架，通过Error Notebook记录纠正后的推理轨迹并结合RAG进行推理时适应，在3D CAD装配体的规格驱动零件检索任务上，GPT-4o准确率从41.7%提升至65.1%（+23.4%），并通过语法约束验证器进一步提升4.5%。

**[Exploring Interpretability for Visual Prompt Tuning with Cross-layer Concepts](exploring_interpretability_for_visual_prompt_tuning_with_cross-layer_concepts.md)**

:   提出IVPT（Interpretable Visual Prompt Tuning），通过跨层类别无关概念原型将抽象visual prompt关联到人类可理解的语义区域，在保持参数高效微调优势的同时，首次实现了visual prompt的可解释性，在CUB-200等细粒度分类基准上同时提升解释一致性（+8.4%）和准确率。

**[FRIEDA: Benchmarking Multi-Step Cartographic Reasoning in Vision-Language Models](frieda_benchmarking_multi-step_cartographic_reasoning_in_vision-language_models.md)**

:   提出 FRIEDA 基准，系统评估大型视觉语言模型在多步骤、跨地图的制图推理能力，发现最强模型 Gemini-2.5-Pro 准确率仅 38.20%，远低于人类 84.87%。

**[Grasp Any Region: Towards Precise, Contextual Pixel Understanding for Multimodal LLMs](grasp_any_region_towards_precise_contextual_pixel_understanding_for_multimodal_l.md)**

:   提出 GAR（Grasp Any Region），通过 RoI-aligned feature replay 在保持全局上下文的同时提取高保真局部特征，实现精准的单区域描述、多区域交互建模和复合推理，1B 模型即超越 InternVL3-78B。

**[Grounding-IQA: Grounding Multimodal Language Models for Image Quality Assessment](grounding-iqa_grounding_multimodal_language_model_for_image_quality_assessment.md)**

:   将空间定位（referring + grounding）与图像质量评估结合，构建 GIQA-160K 数据集训练多模态 LLM 生成带有边界框的质量描述和空间 VQA，在细粒度质量感知上显著优于通用 MLLM。

**[GTR-Bench: Evaluating Geo-Temporal Reasoning in Vision-Language Models](gtr-bench_evaluating_geo-temporal_reasoning_in_vision-language_mod.md)**

:   提出 GTR-Bench，一个面向大规模摄像头网络中移动目标地理时空推理的新基准，评估发现最强模型 Gemini-2.5-Pro（34.9%）远落后于人类水平（78.61%），揭示了当前 VLM 在时空上下文利用失衡、时序预测能力弱、地图-视频对齐能力不足三大缺陷。

**[IVC-Prune: Revealing the Implicit Visual Coordinates in LVLMs for Vision Token Pruning](ivc-prune_revealing_the_implicit_visual_coordinates_in_lvlms_for_vision_token_pr.md)**

:   揭示了LVLM中RoPE位置编码隐式建立的视觉坐标系统（IVC tokens），提出一种训练免的、提示感知的视觉token剪枝策略，在保留IVC tokens和语义前景token的同时，削减约50%视觉token并维持≥99%原始性能。

**[KeepLoRA: Continual Learning with Residual Gradient Adaptation](keeplora_continual_learning_with_residual_gradient_adaptation.md)**

:   通过分析预训练模型权重的SVD分解，发现通用知识编码在主子空间、领域特定知识编码在残差子空间，提出KeepLoRA方法将新任务的LoRA更新约束在残差子空间中，同时用梯度信息初始化以保持可塑性，在持续学习中达到前向稳定、后向稳定和可塑性的最优平衡。

**[Leveraging Data to Say No: Memory Augmented Plug-and-Play Selective Prediction](leveraging_data_to_say_no_memory_augmented_plug-and-play_selective_prediction.md)**

:   提出 MA-PaPSP 框架，通过外部检索数据集构建代理嵌入（k-NN 加权平均降低表示方差）+ 对比归一化评分（改善校准），无训练地为任意 VLM 提供可靠的"拒绝回答"能力，在图像描述、图文匹配、分类的选择性预测上全面优于 PaPSP 和 LLM-as-judge 基线。

**[LiveWeb-IE: A Benchmark For Online Web Information Extraction](liveweb-ie_a_benchmark_for_online_web_information_extraction.md)**

:   提出首个面向在线网页的信息抽取（WIE）基准LiveWeb-IE，覆盖文本/图片/超链接等多类数据抽取，并设计Visual Grounding Scraper（VGS）框架，通过模拟人类认知过程——视觉扫描定位区域→精确定位元素→生成XPath——在动态网页上实现鲁棒的信息抽取。

**[Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation](look_carefully_adaptive_visual_reinforcements_in_multimodal_large_language_model.md)**

:   提出 AIR（Adaptive vIsual Reinforcement）框架，通过原型距离的 token 精简 + 最优传输引导的 patch 选择性增强，在推理时无训练地减少 MLLM 幻觉（LLaVA-1.5-7B CHAIR_S: 22→18.4，POPE 准确率 +5.3%），同时保持多模态通用能力。

**[MATA: A Trainable Hierarchical Automaton System for Multi-Agent Visual Reasoning](mata_a_trainable_hierarchical_automaton_system_for_multi-agent_visual_reasoning.md)**

:   提出MATA（Multi-Agent hierarchical Trainable Automaton），将多Agent视觉推理建模为层次有限状态自动机，顶层状态转移由可训练的hyper agent（基于LLM的状态控制器）学习，每个Agent内部使用规则化的子自动机，通过共享内存实现协作与竞争，在多个视觉推理基准上达到SOTA。

**[Multimodal Classification via Total Correlation Maximization](multimodal_classification_via_total_correlation_maximization.md)**

:   从信息论角度分析多模态分类中的模态竞争问题，提出 TCMax 损失函数通过最大化多模态特征与标签之间的总相关性（Total Correlation），同时兼顾联合学习、单模态学习和跨模态对齐三重目标，在多个音视频/图文分类基准上超越 SOTA。

**[RAVENEA: A Benchmark for Multimodal Retrieval-Augmented Visual Culture Understanding](ravenea_a_benchmark_for_multimodal_retrieval-augmented_visual_culture_understand.md)**

:   构建首个评估多模态检索增强文化理解的基准 Ravenea，包含 1868 个实例和 11396 篇人工排序的 Wikipedia 文档，覆盖 8 个国家 11 个类别，评估 7 个多模态检索器和 17 个 VLM，发现文化感知的 RAG 可在 cVQA 上平均提升 6%、cIC 上提升 11%。

**[Revisit Visual Prompt Tuning: The Expressiveness of Prompt Experts](revisit_visual_prompt_tuning_the_expressiveness_of_prompt_experts.md)**

:   从混合专家（MoE）视角揭示 VPT 的局限性——prompt experts 是输入无关的常量函数表达力受限，提出 VAPT 通过 token-wise 投影器和共享特征投影器使 prompt experts 自适应输入，用更少参数实现更优性能，并给出了最优样本效率的理论保证。

**[Shuffle-R1: Efficient RL Framework for Multimodal Large Language Models via Data-centric Dynamic Shuffle](shuffle-r1_efficient_rl_framework_for_multimodal_large_language_models_via_data-.md)**

:   提出 Shuffle-R1 框架，通过 Pairwise Trajectory Sampling（选取高对比度轨迹对）和 Advantage-based Batch Shuffle（按优势值重分配训练批次），解决 RL 训练中的 Advantage Collapsing 和 Rollout Silencing 两大效率瓶颈，在 Geo3K 上比 baseline 提升 22%，MathVerse 上超越 GPT-4o。

**[SpatiaLab: Can Vision-Language Models Perform Spatial Reasoning in the Wild?](spatialab_can_vision-language_models_perform_spatial_reasoning_in_the_wild.md)**

:   提出SpatiaLab，一个包含1400个视觉QA对的真实场景空间推理基准，涵盖6大类30子类空间任务，支持多选和开放式双格式评估，揭示当前最强VLM（InternVL3.5-72B MCQ 54.93%）与人类（87.57%）之间存在巨大空间推理鸿沟，且开放式设置下差距更大。

**[ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding](thinkomni_lifting_textual_reasoning_to_omni-modal_scenarios_via_guidance_decodin.md)**

:   提出 ThinkOmni 无训练框架，利用纯文本大推理模型(LRM)在解码时引导全模态 LLM(OLLM)，通过 Stepwise Contrastive Scaling 自适应平衡感知与推理信号，MathVista 达 70.2%、MMAU 达 75.5%，匹配或超越 RFT 方法。

**[Visual Prompt-Agnostic Evolution](visual_prompt-agnostic_evolution.md)**

:   提出 Prompt-Agnostic Evolution (PAE)，通过频域感知的任务初始化 (MPA) 和 Koopman-Lyapunov 动力系统 (KLD) 跨层关联 prompt，加速 VPT 收敛（平均 1.41× 加速）并在 25 个数据集上提升 1–3% 精度，且对各类 VPT 变体即插即用、无推理开销。

**[Visual Symbolic Mechanisms: Emergent Symbol Processing in Vision Language Models](visual_symbolic_mechanisms_vlm.md)**

:   发现 VLM 内部涌现了一套三阶段符号处理机制（ID retrieval → ID selection → feature retrieval），利用内容无关的空间位置索引（position IDs）来解决视觉绑定问题，并证明绑定错误可直接追溯到这些机制的失败。

**[Why Keep Your Doubts To Yourself Trading Visual Uncertainty](why_keep_your_doubts_to_yourself_trading_visual_uncertainty.md)**

:   提出 Agora 框架，将多智能体 VLM 协调问题重新建模为去中心化的不确定性交易市场，通过将认知不确定性拆分为可交易资产（感知/语义/推理三维），并用基于盈利性驱动的交易协议和 Thompson Sampling 代理人实现成本感知的最优分配，在五个多模态基准上以超 3 倍成本节省获得至多 +8.5% 准确率提升。
