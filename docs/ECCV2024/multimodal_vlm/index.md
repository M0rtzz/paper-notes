<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**🎞️ ECCV2024** · 共 **56** 篇

**[A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis](a_multimodal_benchmark_dataset_and_model_for_crop_disease_di.md)**

:   构建了包含13.7万张作物病害图像和100万问答对的CDDM数据集，并提出同时对视觉编码器、adapter和语言模型施加LoRA微调的策略，使Qwen-VL-Chat和LLaVA在作物病害诊断准确率上从个位数跃升至90%以上。

**[AdaShield: Safeguarding Multimodal Large Language Models from Structure-based Attack via Adaptive Shield Prompting](adashield_safeguarding_multimodal_large_language_models_from_structure-based_att.md)**

:   AdaShield通过在MLLM输入前添加防御提示(defense prompt)来防御结构化越狱攻击（图像中嵌入有害文本），提出静态手动提示和自适应自动精化框架两种方案，无需微调模型即可显著提升安全性且不损害正常能力。

**[AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_visionlanguage_models_for_citywide_im.md)**

:   AddressCLIP 定义了"图像地址定位"(IAL) 新任务，提出端到端框架通过图像-文本对齐（图像↔地址/场景描述的对比学习）和图像-地理匹配（流形学习约束特征空间距离与地理距离一致）直接预测图像拍摄的可读文本地址，在自建的 Pittsburgh 和 San Francisco 数据集上优于现有 VLM 迁移方法。

**[ArtVLM: Attribute Recognition Through Vision-Based Prefix Language Modeling](artvlm_attribute_recognition_through_vision-based_prefix_language_modeling.md)**

:   本文提出将视觉属性识别问题重新建模为基于图像条件的前缀语言模型（PrefixLM）下的句子生成概率问题，通过"生成式检索"（Generative Retrieval）替代传统的"对比式检索"（Contrastive Retrieval），显式建模物体-属性间的条件依赖关系，在VAW和新提出的VGARank数据集上显著超越对比检索方法。

**[ArtVLM: Attribute Recognition Through Vision-Based Prefix Language Modeling](artvlm_attribute_recognition_through_visionbased_prefix_lang.md)**

:   ArtVLM将属性识别定义为语言建模问题，PrefixLM生成式检索灵活建模物体-属性条件依赖。

**[Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)**

:   本文提出Attention Prompting on Image（API），通过辅助模型（如CLIP或LLaVA）根据文本查询生成注意力热力图，将热力图叠加到原始图像上作为视觉提示输入LVLM，在不修改模型参数的情况下在MM-Vet、LLaVA-Bench等多个VL基准上稳定提升多种LVLM的性能（LLaVA-1.5提升3.8%/2.9%）。

**[Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_visionlanguage_models.md)**

:   API用辅助VLM根据文本查询生成注意力热力图叠加原图，引导LVLM关注相关区域。

**[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](beaf_observing_before-after_changes_to_evaluate_hallucination_in_vision-language.md)**

:   提出 BEAF 幻觉评估基准，通过图像编辑（移除物体）构造"前后对比"场景，设计 TU/IG/SB/ID 四个变化感知指标，揭示现有 VLM 即使传统 accuracy 高也可能存在严重幻觉。

**[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](beaf_observing_beforeafter_changes_to_evaluate_hallucination.md)**

:   BEAF提出"前-后对比"的幻觉评估范式：通过图像编辑移除物体后观察VLM回答的变化，引入TU/IG/SB/ID四个变化感知指标，揭示了传统文本轴评估无法发现的幻觉行为。

**[BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation](bi-mdrg_bridging_image_history_in_multimodal_dialogue_response_generation.md)**

:   提出 BI-MDRG 框架，通过桥接图像历史信息来增强多模态对话中文本回复的图像 grounding 能力和连续图像回复中物体的一致性。

**[BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation](bimdrg_bridging_image_history_in_multimodal_dialogue_respons.md)**

:   BI-MDRG通过视觉交叉注意力和Citation Module桥接图像历史增强多模态对话。

**[BLINK: Multimodal Large Language Models Can See but Not Perceive](blink_multimodal_large_language_models_can_see_but_not_perceive.md)**

:   提出BLINK——一个包含14个经典计算机视觉感知任务的多模态评测基准（3807道选择题），这些任务人类可以"眨眼间"解决（95.7%准确率），但最强的GPT-4V仅达51.26%（仅高于随机猜测13.17%），揭示了当前MLLM在核心视觉感知能力上的严重缺失。

**[BRAVE: Broadening the Visual Encoding of Vision-Language Models](brave_broadening_the_visual_encoding_of_vision-language_models.md)**

:   本文系统性地分析了不同视觉编码器（CLIP、DINOv2、EVA-CLIP等）对VLM性能的影响，发现没有单一编码器能在所有任务上最优，基于此提出BRAVE方法，通过轻量级的MEQ-Former将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在captioning和VQA任务上取得SOTA，并显著降低视觉幻觉。

**[BRAVE: Broadening the Visual Encoding of Vision-Language Models](brave_broadening_the_visual_encoding_of_visionlanguage_model.md)**

:   通过系统benchmarking发现没有单一视觉编码器在所有VLM任务上最优，提出BRAVE方法用Multi-Encoder Querying Transformer（MEQ-Former）将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在多个captioning和VQA基准上达到SOTA。

**[CLAP: Isolating Content from Style Through Contrastive Learning with Augmented Prompts](clap_isolating_content_from_style_through_contrastive_learni.md)**

:   从因果生成模型视角出发，提出CLAP（Contrastive Learning with Augmented Prompts），通过文本增强（而非图像增强）在预训练CLIP的特征空间中解耦内容与风格信息，以极低训练成本（<1小时）显著提升CLIP在零样本/少样本分类和对抗鲁棒性上的表现。

**[CLAP: Isolating Content from Style through Contrastive Learning with Augmented Prompts](clap_isolating_content_from_style_through_contrastive_learning_with_augmented_pr.md)**

:   从因果生成模型视角出发，提出 CLAP（Contrastive Learning with Augmented Prompts），通过文本 prompt 增强 + 对比学习训练一个轻量解耦网络，将 CLIP 预训练特征中的 content 与 style 分离，仅用文本训练即可同时提升图像和文本两侧的表征质量，在 zero-shot、few-shot 分类和对抗鲁棒性上均取得一致提升。

**[Dataset Growth (InfoGrowth)](dataset_growth.md)**

:   提出 InfoGrowth，一种高效的在线数据清洗与选择算法，通过近邻搜索估计每个样本的信息增益，实现数据集的持续增长，同时保证清洁度和多样性，在 CC3M 上仅用 1/6 数据即超过全量训练效果。

**[DeCUR: Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](decoupling_common_and_unique_representations_for_multimodal_.md)**

:   DeCUR将嵌入维度分为跨模态公共和模态独特维度进行多模态自监督学习。

**[Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](decoupling_common_and_unique_representations_for_multimodal_self-supervised_lear.md)**

:   提出 DeCUR，在多模态自监督学习中将嵌入维度显式拆分为跨模态共有 (common) 和模态独有 (unique) 两部分，通过互相关矩阵分别驱动对齐与去相关，同时引入模态内训练保证独有维度学到有意义信息，在 SAR-光学、RGB-DEM、RGB-Depth 三类多模态场景上均优于 Barlow Twins / CLIP 等基线。

**[SpLIP: 通过多模态提示学习提升所有零样本草图检索任务](elevating_all_zero-shot_sketch-based_image_retrieval_through_multimodal_prompt_l.md)**

:   提出 SpLIP，一种基于冻结 CLIP 的双向多模态提示学习框架，通过视觉-文本编码器间的双向知识交换、自适应 margin 的三元组损失和条件跨模态拼图任务，在 ZS-SBIR、GZS-SBIR 和 FG-ZS-SBIR 三种草图检索设定下均取得 SOTA。

**[SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)**

:   SpLIP提出双向prompt共享用于零样本sketch检索，配合自适应margin和跨模态拼图任务。

**[Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation](eyes_closed_safety_on_protecting_multimodal_llms_via_image-to-text_transformatio.md)**

:   提出ECSO（Eyes Closed, Safety On），一种无需训练的MLLM保护方法，通过检测自身响应的安全性，并将不安全查询中的图像自适应转换为文本描述，从而恢复预对齐LLM的内在安全机制，在MM-SafetyBench上实现最高71.3%的安全性提升，且不损害常规性能。

**[Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation](eyes_closed_safety_on_protecting_multimodal_llms_via_imageto.md)**

:   发现MLLM虽易受图像输入的越狱攻击但具备内省能力（能检测自身不安全回复）、且去除图像后安全机制恢复，据此提出ECSO——通过自检不安全回复后将图像转为query-aware文本描述来恢复预对齐LLM的固有安全机制，无需额外训练即可大幅提升安全性。

**[FlexAttention: 面向高效高分辨率视觉语言模型的灵活注意力机制](flexattention_for_efficient_high-resolution_vision-language_models.md)**

:   提出 FlexAttention，通过基于注意力图的高分辨率token动态选择和层次化自注意力融合机制，在保持甚至超越现有高分辨率VLM性能的同时，将计算成本降低近40%。

**[FlexAttention for Efficient High-Resolution Vision-Language Models](flexattention_for_efficient_highresolution_visionlanguage_mo.md)**

:   FlexAttention动态选择约10%高分辨率token进行层次自注意力，计算成本降40%且性能超越。

**[FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](freemotion_mocap-free_human_motion_synthesis_with_multimodal_large_language_mode.md)**

:   首次在**完全不使用动捕数据**的情况下，利用 MLLM（GPT-4V）作为关键帧设计师和动画师，结合基于物理的运动跟踪，实现开放集人体运动合成。

**[FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](freemotion_mocapfree_human_motion_synthesis_with_multimodal_.md)**

:   FreeMotion首次在不使用任何动捕数据的情况下，利用GPT-4V作为关键帧设计师和动画师，将自然语言指令分解为关键帧序列，再通过插值和基于物理的运动跟踪填充帧间运动，实现了开放集人体动作合成。

**[GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator](genixer_empowering_multimodal_large_language_model_as_a_powe.md)**

:   Genixer提出一套完整的视觉指令微调数据生成pipeline，通过训练现有MLLM（LLaVA1.5和Shikra）使其具备数据生成能力，无需GPT-4即可生成高质量的VQA和REC指令数据，并通过Fuyu驱动和CLIP驱动的自动过滤框架保证数据质量。

**[Genixer: Empowering Multimodal Large Language Model as a Powerful Data Generator](genixer_empowering_multimodal_large_language_model_as_a_powerful_data_generator.md)**

:   提出 Genixer 数据生成流水线，训练 MLLM 自身作为数据生成器，无需依赖 GPT-4V 即可自动生成高质量视觉指令微调数据，生成的 915K VQA 数据和 350K REC 数据分别提升 LLaVA1.5 和 Shikra 在多个基准上的表现。

**[Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](groma_localized_visual_tokenization_for_grounding_multimodal.md)**

:   提出Groma，通过在视觉tokenizer中引入区域提议和区域编码机制，将定位能力嵌入图像token化过程，实现统一的referring和grounding能力，在标准基准上超越同类MLLM。

**[Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](groma_localized_visual_tokenization_for_grounding_multimodal_large_language_mode.md)**

:   Groma提出了将定位能力嵌入视觉tokenization过程的新范式——通过region proposer发现感兴趣区域并编码为region token，使MLLM无需依赖LLM输出坐标或外部模块即可实现高精度的referring和grounding，同时利用GPT-4V+visual prompting构建了首个视觉-文本双prompt的grounded chat数据集Groma Instruct。

**[AutoVER: Grounding Language Models for Visual Entity Recognition](grounding_language_models_for_visual_entity_recognition.md)**

:   提出 AutoVER，在多模态大语言模型中统一集成对比检索和前缀树约束解码，将 600 万级 Wikipedia 实体空间先缩小到数百候选再做受限生成，在 Oven-Wiki 上将 entity seen 准确率从 PaLI-17B 的 30.6% 翻倍到 61.5%，同时在 unseen/query split 上也大幅领先。

**[MarvelOVD: 融合目标检测器与视觉语言模型实现鲁棒开放词汇目标检测](marvelovd_marrying_object_recognition_and_vision-language_models_for_robust_open.md)**

:   提出 MarvelOVD 框架，通过将检测器的上下文感知能力和背景识别能力融入 VLM 的伪标签生成与训练流程，在线净化噪声伪标签并自适应重加权训练框，在 COCO 和 LVIS 上大幅超越已有方法。

**[MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)**

:   分析了VLM（CLIP）在局部区域预测中产生噪声伪标签的两大根因——缺乏上下文信息和无"背景"概念，提出MarvelOVD结合检测器的上下文和背景感知能力进行在线伪标签挖掘，配合自适应提案重加权和分层标签分配，在COCO和LVIS上显著超越SOTA。

**[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)**

:   提出MathVerse——一个包含2612道视觉数学题目（转化为6个版本共15K测试样本）的多模态数学推理评测基准，通过系统性地调控文本与图像中的信息分配来检验MLLM是否真正"看懂"了数学图表，并提出CoT评估策略进行细粒度推理过程评分，揭示了大多数MLLM严重依赖文本而非视觉图表进行数学推理。

**[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?](mathverse_does_your_multimodal_llm_truly_see_the_diagrams_in.md)**

:   提出MathVerse——一个专门评估MLLM视觉数学推理能力的基准，通过将每道题转化为6个版本（从文本主导到纯视觉），揭示大多数MLLM严重依赖文本提示而非真正理解数学图表，并提出CoT评估策略进行细粒度推理过程评分。

**[Meta-Prompting for Automating Zero-Shot Visual Recognition with LLMs](meta-prompting_for_automating_zero-shot_visual_recognition_with_llms.md)**

:   提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段 meta-prompting 策略自动化生成多样化的类别特定 VLM prompt，无需人工设计 LLM 查询即可显著提升 CLIP 等模型的 zero-shot 识别性能。

**[Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs](metaprompting_for_automating_zeroshot_visual_recognitio.md)**

:   提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段元提示策略自动让 LLM 生成任务特定且类别特定的 VLM 提示，在 20 个数据集上将 CLIP 零样本识别提升最高 19.8%，完全消除人工提示设计。

**[MMBench: Is Your Multi-modal Model an All-Around Player?](mmbench_is_your_multi-modal_model_an_all-around_player.md)**

:   提出 MMBench——一个包含 3217 道多选题、覆盖 20 个细粒度能力维度的双语（英/中）视觉语言模型评测基准，并设计了 CircularEval 循环评测策略和基于 LLM 的选项提取机制，显著提升了评测的鲁棒性和公平性。

**[MMBench: Is Your Multi-modal Model an All-Around Player?](mmbench_is_your_multimodal_model_an_allaround_player.md)**

:   提出MMBench——一个系统设计的双语多模态评测基准，包含3000+多选题覆盖20个能力维度，并引入CircularEval策略和LLM辅助选项匹配，实现对VLM的鲁棒、细粒度评估。

**[MyVLM: Personalizing VLMs for User-Specific Queries](myvlm_personalizing_vlms_for_userspecific_queries.md)**

:   MyVLM首次探索VLM个性化问题，通过外挂概念识别头检测用户特定概念（如"你的狗"），并在VLM中间特征空间学习概念嵌入引导语言模型在回答中自然融入该概念，仅需3-5张图像即可实现个性化caption和VQA。

**[NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](navgpt2_unleashing_navigational_reasoning_capability.md)**

:   提出 NavGPT-2，通过将冻结 LLM 与视觉内容对齐，结合拓扑图导航策略网络，在保持 LLM 可解释性推理能力的同时，消除了基于语言模型的导航智能体与 VLN 专用模型之间的性能差距。

**[Omniview-Tuning: Boosting Viewpoint Invariance of Vision-Language Pre-training Models](omniviewtuning_boosting_viewpoint_invariance_of_visionlangua.md)**

:   OVT构建400万+MVCap数据集+Cross-Viewpoint Alignment提升VLP视角不变性。

**[Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_visionlangu.md)**

:   发现适度噪声可以抑制VLM prompt tuning中的过拟合和灾难性遗忘，首次将量化误差视为正则化，设计了基于K-Means聚类的量化感知训练算法，在11个数据集上以极小存储开销（0.26KB）超越了众多SOTA方法。

**[Robust Calibration of Large Vision-Language Adapters](robust_calibration_of_large_visionlanguage_adapters.md)**

:   CLIP适配方法OOD校准退化的根因是logit范围增大，提出SaLS等方案。

**[ShareGPT4V: Improving Large Multi-Modal Models with Better Captions](sharegpt4v_improving_large_multi-modal_models_with_better_captions.md)**

:   ShareGPT4V 构建了一个120万条高质量描述性caption数据集（由GPT4-Vision生成100K种子 + Share-Captioner扩展至1.2M），通过在预训练和SFT两阶段使用该数据集训练LLaVA架构的模型ShareGPT4V-7B，在11个多模态benchmark中9个取得最优，证明了高质量caption是LMM模态对齐的关键瓶颈。

**[ShareGPT4V: Improving Large Multi-modal Models with Better Captions](sharegpt4v_improving_large_multimodal_models_with_better_cap.md)**

:   指出现有LMM训练中低质量caption是模态对齐的瓶颈，构建了1.2M高质量详细描述的ShareGPT4V数据集（100K来自GPT4-Vision + 1.2M来自训练得到的Share-Captioner），在预训练和SFT两阶段使用该数据，以简单架构的7B模型在11个基准中9个取得最优。

**[SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](sqllava_selfquestioning_for_large_visionlanguage_assistant.md)**

:   提出SQ-LLaVA，首次将指令数据中问题作为额外学习目标，训练MLLM不仅回答问题还学会"自问"，通过视觉自提问（visual self-questioning）任务挖掘指令数据中被忽视的问题上下文信息，配合原型提取器和LoRA微调，在10个VQA基准中9个超越基线。

**[The Hard Positive Truth About Vision-Language Compositionality](the_hard_positive_truth_about_visionlanguage_compositionalit.md)**

:   本文揭示了现有CLIP组合性基准的评估盲区——缺少hard positives测试，发现hard negative微调会导致模型"过敏"（对语义保持的改写也错误地降低匹配分数），并通过同时加入hard positives和hard negatives训练来缓解这一问题。

**[Towards Open-Ended Visual Quality Comparison](towards_openended_visual_quality_comparison.md)**

:   提出 Co-Instruct，首个开源的开放式视觉质量比较大模型，通过构建 Co-Instruct-562K 数据集和 MICBench 基准，使 LMM 在视觉质量比较任务上超越 GPT-4V。

**[Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models](towards_realworld_adverse_weather_image_restoration_enhancin.md)**

:   提出WResVLM半监督框架，利用VLM评估图像清晰度和提供语义信息，通过伪标签选择+天气prompt学习增强清晰度、VLM描述引导的语义正则化增强语义，首次有效地将合成数据训练的复原模型泛化到真实恶劣天气场景。

**[UMBRAE: Unified Multimodal Brain Decoding](umbrae_unified_multimodal_brain_decoding.md)**

:   提出UMBRAE，通过通用脑编码器将fMRI信号与图像特征对齐后送入冻结的MLLM，实现多模态脑解码（描述、定位、检索、视觉重建），并创新性地引入跨被试训练策略，使单一模型服务多个被试且优于单被试模型。

**[UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_lan.md)**

:   提出UniCode，通过语言驱动的迭代训练范式学习一个统一码本，使LLM的词表可同时量化视觉和文本信号，无需额外对齐模块即可实现多模态理解与生成，并引入上下文图像解压缩任务提升生成质量。

**[UniCode: Learning a Unified Codebook for Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_language_models.md)**

:   UniCode提出学习一个统一的codebook来同时tokenize视觉和文本信号，通过language-driven iterative training范式将视觉tokenizer的码本与LLM的词表渐进对齐，并引入in-context image decompression预训练任务提升图像生成质量，使MLLM无需额外对齐模块即可实现多模态理解与生成。

**[Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models](vary_scaling_up_the_vision_vocabulary_for_large_visionlanguag.md)**

:   提出 Vary 方法，通过生成并融合新的视觉词汇表（vision vocabulary）来扩展 LVLM 的视觉感知能力，使模型在保持原有通用能力的同时，获得文档级 OCR、图表理解等细粒度视觉感知新能力。

**[X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs](xformer_unifying_contrastive_and_reconstruction_learning_for.md)**

:   提出X-Former，一个轻量级Transformer模块，通过双交叉注意力机制融合CLIP（全局语义）和MAE（局部细节）两种视觉编码器的互补特征，结合ITC/ITM/ITG和重建四个损失联合优化，提升MLLM的细粒度视觉理解能力。
