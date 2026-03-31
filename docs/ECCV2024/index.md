<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎞️ ECCV2024 论文笔记

共 **317** 篇笔记，覆盖 **30** 个领域。

## 领域概览

| 领域 | 篇数 |
|:-----|-----:|
| 🧩 [多模态 VLM](#multimodal_vlm) | 56 |
| 🧊 [3D 视觉](#3d_vision) | 43 |
| 🎨 [图像生成](#image_generation) | 39 |
| 🧑 [人体理解](#human_understanding) | 19 |
| ✂️ [语义分割](#segmentation) | 19 |
| 🚗 [自动驾驶](#autonomous_driving) | 17 |
| 💬 [LLM / NLP](#llm_nlp) | 16 |
| 🎯 [目标检测](#object_detection) | 15 |
| 🎬 [视频理解](#video_understanding) | 14 |
| 🏥 [医学图像](#medical_imaging) | 10 |
| 🛡️ [AI 安全](#ai_safety) | 9 |
| 🎵 [音频/语音](#audio_speech) | 7 |
| 🤖 [机器人/具身智能](#robotics) | 7 |
| 📦 [模型压缩](#model_compression) | 6 |
| 🕸️ [图学习](#graph_learning) | 4 |
| 🎮 [强化学习](#reinforcement_learning) | 4 |
| 💡 [LLM 推理](#llm_reasoning) | 3 |
| 🔄 [自监督/表示学习](#self_supervised) | 3 |
| 🖼️ [图像恢复](#image_restoration) | 2 |
| 🦾 [LLM Agent](#llm_agent) | 2 |
| 🛰️ [遥感](#remote_sensing) | 2 |
| 📈 [时间序列](#time_series) | 2 |
| 🔗 [因果推理](#causal_inference) | 1 |
| 🌍 [地球科学](#earth_science) | 1 |
| ⚖️ [对齐 / RLHF](#llm_alignment) | 1 |
| 📐 [优化/理论](#optimization) | 1 |
| ⚛️ [物理学](#physics) | 1 |
| 🎁 [推荐系统](#recommender) | 1 |
| 📡 [信号/通信](#signal_comm) | 1 |
| 📂 [其他](#others) | 11 |

---

## 🧩 多模态 VLM { #multimodal_vlm }

**[A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis](multimodal_vlm/a_multimodal_benchmark_dataset_and_model_for_crop_disease_di.md)**

:   构建了包含13.7万张作物病害图像和100万问答对的CDDM数据集，并提出同时对视觉编码器、adapter和语言模型施加LoRA微调的策略，使Qwen-VL-Chat和LLaVA在作物病害诊断准确率上从个位数跃升至90%以上。

**[AdaShield: Safeguarding Multimodal Large Language Models from Structure-based Attack via Adaptive Shield Prompting](multimodal_vlm/adashield_safeguarding_multimodal_large_language_models_from_structure-based_att.md)**

:   AdaShield通过在MLLM输入前添加防御提示(defense prompt)来防御结构化越狱攻击（图像中嵌入有害文本），提出静态手动提示和自适应自动精化框架两种方案，无需微调模型即可显著提升安全性且不损害正常能力。

**[AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](multimodal_vlm/addressclip_empowering_visionlanguage_models_for_citywide_im.md)**

:   AddressCLIP 定义了"图像地址定位"(IAL) 新任务，提出端到端框架通过图像-文本对齐（图像↔地址/场景描述的对比学习）和图像-地理匹配（流形学习约束特征空间距离与地理距离一致）直接预测图像拍摄的可读文本地址，在自建的 Pittsburgh 和 San Francisco 数据集上优于现有 VLM 迁移方法。

**[ArtVLM: Attribute Recognition Through Vision-Based Prefix Language Modeling](multimodal_vlm/artvlm_attribute_recognition_through_vision-based_prefix_language_modeling.md)**

:   本文提出将视觉属性识别问题重新建模为基于图像条件的前缀语言模型（PrefixLM）下的句子生成概率问题，通过"生成式检索"（Generative Retrieval）替代传统的"对比式检索"（Contrastive Retrieval），显式建模物体-属性间的条件依赖关系，在VAW和新提出的VGARank数据集上显著超越对比检索方法。

**[ArtVLM: Attribute Recognition Through Vision-Based Prefix Language Modeling](multimodal_vlm/artvlm_attribute_recognition_through_visionbased_prefix_lang.md)**

:   ArtVLM将属性识别定义为语言建模问题，PrefixLM生成式检索灵活建模物体-属性条件依赖。

**[Attention Prompting on Image for Large Vision-Language Models](multimodal_vlm/attention_prompting_on_image_for_large_vision-language_models.md)**

:   本文提出Attention Prompting on Image（API），通过辅助模型（如CLIP或LLaVA）根据文本查询生成注意力热力图，将热力图叠加到原始图像上作为视觉提示输入LVLM，在不修改模型参数的情况下在MM-Vet、LLaVA-Bench等多个VL基准上稳定提升多种LVLM的性能（LLaVA-1.5提升3.8%/2.9%）。

**[Attention Prompting on Image for Large Vision-Language Models](multimodal_vlm/attention_prompting_on_image_for_large_visionlanguage_models.md)**

:   API用辅助VLM根据文本查询生成注意力热力图叠加原图，引导LVLM关注相关区域。

**[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](multimodal_vlm/beaf_observing_before-after_changes_to_evaluate_hallucination_in_vision-language.md)**

:   提出 BEAF 幻觉评估基准，通过图像编辑（移除物体）构造"前后对比"场景，设计 TU/IG/SB/ID 四个变化感知指标，揭示现有 VLM 即使传统 accuracy 高也可能存在严重幻觉。

**[BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-Language Models](multimodal_vlm/beaf_observing_beforeafter_changes_to_evaluate_hallucination.md)**

:   BEAF提出"前-后对比"的幻觉评估范式：通过图像编辑移除物体后观察VLM回答的变化，引入TU/IG/SB/ID四个变化感知指标，揭示了传统文本轴评估无法发现的幻觉行为。

**[BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation](multimodal_vlm/bi-mdrg_bridging_image_history_in_multimodal_dialogue_response_generation.md)**

:   提出 BI-MDRG 框架，通过桥接图像历史信息来增强多模态对话中文本回复的图像 grounding 能力和连续图像回复中物体的一致性。

**[BI-MDRG: Bridging Image History in Multimodal Dialogue Response Generation](multimodal_vlm/bimdrg_bridging_image_history_in_multimodal_dialogue_respons.md)**

:   BI-MDRG通过视觉交叉注意力和Citation Module桥接图像历史增强多模态对话。

**[BLINK: Multimodal Large Language Models Can See but Not Perceive](multimodal_vlm/blink_multimodal_large_language_models_can_see_but_not_perceive.md)**

:   提出BLINK——一个包含14个经典计算机视觉感知任务的多模态评测基准（3807道选择题），这些任务人类可以"眨眼间"解决（95.7%准确率），但最强的GPT-4V仅达51.26%（仅高于随机猜测13.17%），揭示了当前MLLM在核心视觉感知能力上的严重缺失。

**[BRAVE: Broadening the Visual Encoding of Vision-Language Models](multimodal_vlm/brave_broadening_the_visual_encoding_of_vision-language_models.md)**

:   本文系统性地分析了不同视觉编码器（CLIP、DINOv2、EVA-CLIP等）对VLM性能的影响，发现没有单一编码器能在所有任务上最优，基于此提出BRAVE方法，通过轻量级的MEQ-Former将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在captioning和VQA任务上取得SOTA，并显著降低视觉幻觉。

**[BRAVE: Broadening the Visual Encoding of Vision-Language Models](multimodal_vlm/brave_broadening_the_visual_encoding_of_visionlanguage_model.md)**

:   通过系统benchmarking发现没有单一视觉编码器在所有VLM任务上最优，提出BRAVE方法用Multi-Encoder Querying Transformer（MEQ-Former）将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在多个captioning和VQA基准上达到SOTA。

**[CLAP: Isolating Content from Style Through Contrastive Learning with Augmented Prompts](multimodal_vlm/clap_isolating_content_from_style_through_contrastive_learni.md)**

:   从因果生成模型视角出发，提出CLAP（Contrastive Learning with Augmented Prompts），通过文本增强（而非图像增强）在预训练CLIP的特征空间中解耦内容与风格信息，以极低训练成本（<1小时）显著提升CLIP在零样本/少样本分类和对抗鲁棒性上的表现。

**[CLAP: Isolating Content from Style through Contrastive Learning with Augmented Prompts](multimodal_vlm/clap_isolating_content_from_style_through_contrastive_learning_with_augmented_pr.md)**

:   从因果生成模型视角出发，提出 CLAP（Contrastive Learning with Augmented Prompts），通过文本 prompt 增强 + 对比学习训练一个轻量解耦网络，将 CLIP 预训练特征中的 content 与 style 分离，仅用文本训练即可同时提升图像和文本两侧的表征质量，在 zero-shot、few-shot 分类和对抗鲁棒性上均取得一致提升。

**[Dataset Growth (InfoGrowth)](multimodal_vlm/dataset_growth.md)**

:   提出 InfoGrowth，一种高效的在线数据清洗与选择算法，通过近邻搜索估计每个样本的信息增益，实现数据集的持续增长，同时保证清洁度和多样性，在 CC3M 上仅用 1/6 数据即超过全量训练效果。

**[DeCUR: Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](multimodal_vlm/decoupling_common_and_unique_representations_for_multimodal_.md)**

:   DeCUR将嵌入维度分为跨模态公共和模态独特维度进行多模态自监督学习。

**[Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](multimodal_vlm/decoupling_common_and_unique_representations_for_multimodal_self-supervised_lear.md)**

:   提出 DeCUR，在多模态自监督学习中将嵌入维度显式拆分为跨模态共有 (common) 和模态独有 (unique) 两部分，通过互相关矩阵分别驱动对齐与去相关，同时引入模态内训练保证独有维度学到有意义信息，在 SAR-光学、RGB-DEM、RGB-Depth 三类多模态场景上均优于 Barlow Twins / CLIP 等基线。

**[SpLIP: 通过多模态提示学习提升所有零样本草图检索任务](multimodal_vlm/elevating_all_zero-shot_sketch-based_image_retrieval_through_multimodal_prompt_l.md)**

:   提出 SpLIP，一种基于冻结 CLIP 的双向多模态提示学习框架，通过视觉-文本编码器间的双向知识交换、自适应 margin 的三元组损失和条件跨模态拼图任务，在 ZS-SBIR、GZS-SBIR 和 FG-ZS-SBIR 三种草图检索设定下均取得 SOTA。

**[SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](multimodal_vlm/elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)**

:   SpLIP提出双向prompt共享用于零样本sketch检索，配合自适应margin和跨模态拼图任务。

**[Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation](multimodal_vlm/eyes_closed_safety_on_protecting_multimodal_llms_via_image-to-text_transformatio.md)**

:   提出ECSO（Eyes Closed, Safety On），一种无需训练的MLLM保护方法，通过检测自身响应的安全性，并将不安全查询中的图像自适应转换为文本描述，从而恢复预对齐LLM的内在安全机制，在MM-SafetyBench上实现最高71.3%的安全性提升，且不损害常规性能。

**[Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation](multimodal_vlm/eyes_closed_safety_on_protecting_multimodal_llms_via_imageto.md)**

:   发现MLLM虽易受图像输入的越狱攻击但具备内省能力（能检测自身不安全回复）、且去除图像后安全机制恢复，据此提出ECSO——通过自检不安全回复后将图像转为query-aware文本描述来恢复预对齐LLM的固有安全机制，无需额外训练即可大幅提升安全性。

**[FlexAttention: 面向高效高分辨率视觉语言模型的灵活注意力机制](multimodal_vlm/flexattention_for_efficient_high-resolution_vision-language_models.md)**

:   提出 FlexAttention，通过基于注意力图的高分辨率token动态选择和层次化自注意力融合机制，在保持甚至超越现有高分辨率VLM性能的同时，将计算成本降低近40%。

**[FlexAttention for Efficient High-Resolution Vision-Language Models](multimodal_vlm/flexattention_for_efficient_highresolution_visionlanguage_mo.md)**

:   FlexAttention动态选择约10%高分辨率token进行层次自注意力，计算成本降40%且性能超越。

**[FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](multimodal_vlm/freemotion_mocap-free_human_motion_synthesis_with_multimodal_large_language_mode.md)**

:   首次在**完全不使用动捕数据**的情况下，利用 MLLM（GPT-4V）作为关键帧设计师和动画师，结合基于物理的运动跟踪，实现开放集人体运动合成。

**[FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](multimodal_vlm/freemotion_mocapfree_human_motion_synthesis_with_multimodal_.md)**

:   FreeMotion首次在不使用任何动捕数据的情况下，利用GPT-4V作为关键帧设计师和动画师，将自然语言指令分解为关键帧序列，再通过插值和基于物理的运动跟踪填充帧间运动，实现了开放集人体动作合成。

**[GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator](multimodal_vlm/genixer_empowering_multimodal_large_language_model_as_a_powe.md)**

:   Genixer提出一套完整的视觉指令微调数据生成pipeline，通过训练现有MLLM（LLaVA1.5和Shikra）使其具备数据生成能力，无需GPT-4即可生成高质量的VQA和REC指令数据，并通过Fuyu驱动和CLIP驱动的自动过滤框架保证数据质量。

**[Genixer: Empowering Multimodal Large Language Model as a Powerful Data Generator](multimodal_vlm/genixer_empowering_multimodal_large_language_model_as_a_powerful_data_generator.md)**

:   提出 Genixer 数据生成流水线，训练 MLLM 自身作为数据生成器，无需依赖 GPT-4V 即可自动生成高质量视觉指令微调数据，生成的 915K VQA 数据和 350K REC 数据分别提升 LLaVA1.5 和 Shikra 在多个基准上的表现。

**[Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](multimodal_vlm/groma_localized_visual_tokenization_for_grounding_multimodal.md)**

:   提出Groma，通过在视觉tokenizer中引入区域提议和区域编码机制，将定位能力嵌入图像token化过程，实现统一的referring和grounding能力，在标准基准上超越同类MLLM。

**[Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](multimodal_vlm/groma_localized_visual_tokenization_for_grounding_multimodal_large_language_mode.md)**

:   Groma提出了将定位能力嵌入视觉tokenization过程的新范式——通过region proposer发现感兴趣区域并编码为region token，使MLLM无需依赖LLM输出坐标或外部模块即可实现高精度的referring和grounding，同时利用GPT-4V+visual prompting构建了首个视觉-文本双prompt的grounded chat数据集Groma Instruct。

**[AutoVER: Grounding Language Models for Visual Entity Recognition](multimodal_vlm/grounding_language_models_for_visual_entity_recognition.md)**

:   提出 AutoVER，在多模态大语言模型中统一集成对比检索和前缀树约束解码，将 600 万级 Wikipedia 实体空间先缩小到数百候选再做受限生成，在 Oven-Wiki 上将 entity seen 准确率从 PaLI-17B 的 30.6% 翻倍到 61.5%，同时在 unseen/query split 上也大幅领先。

**[MarvelOVD: 融合目标检测器与视觉语言模型实现鲁棒开放词汇目标检测](multimodal_vlm/marvelovd_marrying_object_recognition_and_vision-language_models_for_robust_open.md)**

:   提出 MarvelOVD 框架，通过将检测器的上下文感知能力和背景识别能力融入 VLM 的伪标签生成与训练流程，在线净化噪声伪标签并自适应重加权训练框，在 COCO 和 LVIS 上大幅超越已有方法。

**[MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](multimodal_vlm/marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)**

:   分析了VLM（CLIP）在局部区域预测中产生噪声伪标签的两大根因——缺乏上下文信息和无"背景"概念，提出MarvelOVD结合检测器的上下文和背景感知能力进行在线伪标签挖掘，配合自适应提案重加权和分层标签分配，在COCO和LVIS上显著超越SOTA。

**[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](multimodal_vlm/mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)**

:   提出MathVerse——一个包含2612道视觉数学题目（转化为6个版本共15K测试样本）的多模态数学推理评测基准，通过系统性地调控文本与图像中的信息分配来检验MLLM是否真正"看懂"了数学图表，并提出CoT评估策略进行细粒度推理过程评分，揭示了大多数MLLM严重依赖文本而非视觉图表进行数学推理。

**[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?](multimodal_vlm/mathverse_does_your_multimodal_llm_truly_see_the_diagrams_in.md)**

:   提出MathVerse——一个专门评估MLLM视觉数学推理能力的基准，通过将每道题转化为6个版本（从文本主导到纯视觉），揭示大多数MLLM严重依赖文本提示而非真正理解数学图表，并提出CoT评估策略进行细粒度推理过程评分。

**[Meta-Prompting for Automating Zero-Shot Visual Recognition with LLMs](multimodal_vlm/meta-prompting_for_automating_zero-shot_visual_recognition_with_llms.md)**

:   提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段 meta-prompting 策略自动化生成多样化的类别特定 VLM prompt，无需人工设计 LLM 查询即可显著提升 CLIP 等模型的 zero-shot 识别性能。

**[Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs](multimodal_vlm/metaprompting_for_automating_zeroshot_visual_recognitio.md)**

:   提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段元提示策略自动让 LLM 生成任务特定且类别特定的 VLM 提示，在 20 个数据集上将 CLIP 零样本识别提升最高 19.8%，完全消除人工提示设计。

**[MMBench: Is Your Multi-modal Model an All-Around Player?](multimodal_vlm/mmbench_is_your_multi-modal_model_an_all-around_player.md)**

:   提出 MMBench——一个包含 3217 道多选题、覆盖 20 个细粒度能力维度的双语（英/中）视觉语言模型评测基准，并设计了 CircularEval 循环评测策略和基于 LLM 的选项提取机制，显著提升了评测的鲁棒性和公平性。

**[MMBench: Is Your Multi-modal Model an All-Around Player?](multimodal_vlm/mmbench_is_your_multimodal_model_an_allaround_player.md)**

:   提出MMBench——一个系统设计的双语多模态评测基准，包含3000+多选题覆盖20个能力维度，并引入CircularEval策略和LLM辅助选项匹配，实现对VLM的鲁棒、细粒度评估。

**[MyVLM: Personalizing VLMs for User-Specific Queries](multimodal_vlm/myvlm_personalizing_vlms_for_userspecific_queries.md)**

:   MyVLM首次探索VLM个性化问题，通过外挂概念识别头检测用户特定概念（如"你的狗"），并在VLM中间特征空间学习概念嵌入引导语言模型在回答中自然融入该概念，仅需3-5张图像即可实现个性化caption和VQA。

**[NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](multimodal_vlm/navgpt2_unleashing_navigational_reasoning_capability.md)**

:   提出 NavGPT-2，通过将冻结 LLM 与视觉内容对齐，结合拓扑图导航策略网络，在保持 LLM 可解释性推理能力的同时，消除了基于语言模型的导航智能体与 VLN 专用模型之间的性能差距。

**[Omniview-Tuning: Boosting Viewpoint Invariance of Vision-Language Pre-training Models](multimodal_vlm/omniviewtuning_boosting_viewpoint_invariance_of_visionlangua.md)**

:   OVT构建400万+MVCap数据集+Cross-Viewpoint Alignment提升VLP视角不变性。

**[Quantized Prompt for Efficient Generalization of Vision-Language Models](multimodal_vlm/quantized_prompt_for_efficient_generalization_of_visionlangu.md)**

:   发现适度噪声可以抑制VLM prompt tuning中的过拟合和灾难性遗忘，首次将量化误差视为正则化，设计了基于K-Means聚类的量化感知训练算法，在11个数据集上以极小存储开销（0.26KB）超越了众多SOTA方法。

**[Robust Calibration of Large Vision-Language Adapters](multimodal_vlm/robust_calibration_of_large_visionlanguage_adapters.md)**

:   CLIP适配方法OOD校准退化的根因是logit范围增大，提出SaLS等方案。

**[ShareGPT4V: Improving Large Multi-Modal Models with Better Captions](multimodal_vlm/sharegpt4v_improving_large_multi-modal_models_with_better_captions.md)**

:   ShareGPT4V 构建了一个120万条高质量描述性caption数据集（由GPT4-Vision生成100K种子 + Share-Captioner扩展至1.2M），通过在预训练和SFT两阶段使用该数据集训练LLaVA架构的模型ShareGPT4V-7B，在11个多模态benchmark中9个取得最优，证明了高质量caption是LMM模态对齐的关键瓶颈。

**[ShareGPT4V: Improving Large Multi-modal Models with Better Captions](multimodal_vlm/sharegpt4v_improving_large_multimodal_models_with_better_cap.md)**

:   指出现有LMM训练中低质量caption是模态对齐的瓶颈，构建了1.2M高质量详细描述的ShareGPT4V数据集（100K来自GPT4-Vision + 1.2M来自训练得到的Share-Captioner），在预训练和SFT两阶段使用该数据，以简单架构的7B模型在11个基准中9个取得最优。

**[SQ-LLaVA: Self-Questioning for Large Vision-Language Assistant](multimodal_vlm/sqllava_selfquestioning_for_large_visionlanguage_assistant.md)**

:   提出SQ-LLaVA，首次将指令数据中问题作为额外学习目标，训练MLLM不仅回答问题还学会"自问"，通过视觉自提问（visual self-questioning）任务挖掘指令数据中被忽视的问题上下文信息，配合原型提取器和LoRA微调，在10个VQA基准中9个超越基线。

**[The Hard Positive Truth About Vision-Language Compositionality](multimodal_vlm/the_hard_positive_truth_about_visionlanguage_compositionalit.md)**

:   本文揭示了现有CLIP组合性基准的评估盲区——缺少hard positives测试，发现hard negative微调会导致模型"过敏"（对语义保持的改写也错误地降低匹配分数），并通过同时加入hard positives和hard negatives训练来缓解这一问题。

**[Towards Open-Ended Visual Quality Comparison](multimodal_vlm/towards_openended_visual_quality_comparison.md)**

:   提出 Co-Instruct，首个开源的开放式视觉质量比较大模型，通过构建 Co-Instruct-562K 数据集和 MICBench 基准，使 LMM 在视觉质量比较任务上超越 GPT-4V。

**[Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models](multimodal_vlm/towards_realworld_adverse_weather_image_restoration_enhancin.md)**

:   提出WResVLM半监督框架，利用VLM评估图像清晰度和提供语义信息，通过伪标签选择+天气prompt学习增强清晰度、VLM描述引导的语义正则化增强语义，首次有效地将合成数据训练的复原模型泛化到真实恶劣天气场景。

**[UMBRAE: Unified Multimodal Brain Decoding](multimodal_vlm/umbrae_unified_multimodal_brain_decoding.md)**

:   提出UMBRAE，通过通用脑编码器将fMRI信号与图像特征对齐后送入冻结的MLLM，实现多模态脑解码（描述、定位、检索、视觉重建），并创新性地引入跨被试训练策略，使单一模型服务多个被试且优于单被试模型。

**[UniCode: Learning a Unified Codebook for Multimodal Large Language Models](multimodal_vlm/unicode_learning_a_unified_codebook_for_multimodal_large_lan.md)**

:   提出UniCode，通过语言驱动的迭代训练范式学习一个统一码本，使LLM的词表可同时量化视觉和文本信号，无需额外对齐模块即可实现多模态理解与生成，并引入上下文图像解压缩任务提升生成质量。

**[UniCode: Learning a Unified Codebook for Multimodal Large Language Models](multimodal_vlm/unicode_learning_a_unified_codebook_for_multimodal_large_language_models.md)**

:   UniCode提出学习一个统一的codebook来同时tokenize视觉和文本信号，通过language-driven iterative training范式将视觉tokenizer的码本与LLM的词表渐进对齐，并引入in-context image decompression预训练任务提升图像生成质量，使MLLM无需额外对齐模块即可实现多模态理解与生成。

**[Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models](multimodal_vlm/vary_scaling_up_the_vision_vocabulary_for_large_visionlanguag.md)**

:   提出 Vary 方法，通过生成并融合新的视觉词汇表（vision vocabulary）来扩展 LVLM 的视觉感知能力，使模型在保持原有通用能力的同时，获得文档级 OCR、图表理解等细粒度视觉感知新能力。

**[X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs](multimodal_vlm/xformer_unifying_contrastive_and_reconstruction_learning_for.md)**

:   提出X-Former，一个轻量级Transformer模块，通过双交叉注意力机制融合CLIP（全局语义）和MAE（局部细节）两种视觉编码器的互补特征，结合ITC/ITM/ITG和重建四个损失联合优化，提升MLLM的细粒度视觉理解能力。

---

## 🧊 3D 视觉 { #3d_vision }

**[3D Congealing: 3D-Aware Image Alignment in the Wild](3d_vision/3d_congealing_3d-aware_image_alignment_in_the_wild.md)**

:   3D Congealing将一组语义相似的无标注互联网图像对齐到共享的3D canonical空间，通过结合预训练扩散模型的SDS指导获得3D形状 + DINO语义特征匹配估计位姿和坐标映射，无需模板、位姿标注或相机参数。

**[3D Reconstruction of Objects in Hands without Real World 3D Supervision](3d_vision/3d_reconstruction_of_objects_in_hands_without_real_world_3d.md)**

:   提出HORSE框架，通过从野外视频中提取多视角2D mask监督（以手部姿态作为物体姿态代理）和从合成3D形状集合中学习2D切片对抗形状先验，训练occupancy网络从单张RGB图像重建手持物体3D形状，在不使用任何真实世界3D标注的情况下，在MOW数据集上超越使用3D监督的方法11.6%。

**[3D Single-Object Tracking in Point Clouds with High Temporal Variation](3d_vision/3d_single-object_tracking_in_point_clouds_with_high_temporal_variation.md)**

:   HVTrack首次探索高时间变化场景下的3D单目标跟踪，通过相对位姿感知记忆模块(RPM)、基础-扩展特征交叉注意力(BEA)和上下文点引导自注意力(CPA)三个模块，分别解决点云形状剧变、相似物体干扰和背景噪声问题，在KITTI-HV 5帧间隔下比SOTA提升11.3%/15.7% Success/Precision。

**[3DEgo: 3D Editing on the Go!](3d_vision/3dego_3d_editing_on_the_go.md)**

:   3DEgo将传统三阶段3D编辑流程（COLMAP位姿估计→未编辑场景初始化→迭代编辑更新）压缩为单阶段框架：先用自回归噪声混合模块对视频帧进行多视角一致的2D编辑，再用COLMAP-free的3DGS从编辑后帧直接重建3D场景，速度提升约10倍且支持任意来源视频。

**[3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting](3d_vision/3igs_factorised_tensorial_illumination_for_3d_gaussian_splatting.md)**

:   3iGS 用基于张量分解的连续入射光照场替代 3DGS 中每个高斯体独立优化的球谐系数，结合可学习 BRDF 特征和轻量神经渲染器来建模出射辐射，在保持实时渲染速度的同时显著提升了镜面反射等视角依赖效果的渲染质量。

**[3×2: 3D Object Part Segmentation by 2D Semantic Correspondences](3d_vision/3x2_3d_object_part_segmentation_by_2d_semantic_correspondenc.md)**

:   提出了一种无需训练的3D物体部件分割方法3-By-2，利用扩散模型(DIFT)的2D语义对应关系从已标注2D数据集或少量3D标注对象中迁移部件标签到3D，在zero-shot和few-shot设置下均达到SOTA。

**[6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model](3d_vision/6dgs_6d_pose_estimation_from_a_single_image_and_a_3d_gaussia.md)**

:   提出6DGS，通过反转3DGS渲染流程——从椭球体表面均匀发射光线（Ellicell），利用注意力机制将光线与目标图像像素绑定，再用加权最小二乘闭式求解相机位姿，无需迭代和初始位姿，在真实场景上旋转精度提升12%、平移精度提升22%，达到15fps近实时性能。

**[A Compact Dynamic 3D Gaussian Representation for Real-Time Dynamic View Synthesis](3d_vision/a_compact_dynamic_3d_gaussian_representation_for_realtime_dy.md)**

:   将3DGS中的位置和旋转参数建模为时间的函数（位置用Fourier逼近、旋转用线性逼近），使动态场景的存储复杂度从O(TN)降低到O(LN)，在D-NeRF/DyNeRF/HyperNeRF三个数据集上实现了与NeRF方法匹敌的渲染质量，同时保持118+ FPS的实时渲染速度。

**[Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration](3d_vision/analytic-splatting_anti-aliased_3d_gaussian_splatting_via_analytic_integration.md)**

:   通过使用条件 logistic 函数解析近似高斯信号在像素窗口上的积分，替代 3DGS 的像素中心点采样，实现无混叠的 3D 高斯泼溅，在多尺度渲染上超越 Mip-Splatting。

**[AnimatableDreamer: Text-Guided Non-rigid 3D Model Generation and Reconstruction with Canonical Score Distillation](3d_vision/animatabledreamer_text-guided_non-rigid_3d_model_generation_and_reconstruction_w.md)**

:   提出 AnimatableDreamer，通过 Canonical Score Distillation (CSD) 技术，从单目视频提取骨骼和运动后生成文本引导的可动画化 3D 非刚体模型，在生成质量和时序一致性上全面超越现有方法。

**[BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting](3d_vision/bad-gaussians_bundle_adjusted_deblur_gaussian_splatting.md)**

:   首次将运动模糊物理成像模型引入 3D Gaussian Splatting 框架，联合优化场景 Gaussian 参数与曝光时间内的相机运动轨迹，从模糊图像中恢复清晰 3D 场景并实现实时渲染。

**[BeNeRF: Neural Radiance Fields from a Single Blurry Image and Event Stream](3d_vision/benerf_neural_radiance_fields_from_a_single_blurry_image_and_event_stream.md)**

:   提出 BeNeRF，仅从**单张模糊图像**及其对应的事件流（event stream）联合恢复神经辐射场与相机运动轨迹，无需多视角输入或已知位姿，即可实现高质量去模糊与新视角合成。

**[Bi-directional Contextual Attention for 3D Dense Captioning](3d_vision/bi-directional_contextual_attention_for_3d_dense_captioning.md)**

:   提出 BiCA，通过双向上下文注意力机制将 instance query 和 context query 解耦并行解码，解决了 3D 密集描述中定位与描述生成之间的目标冲突，在 ScanRefer 和 Nr3D 两个基准上取得 SOTA。

**[Binomial Self-compensation for Motion Error in Dynamic 3D Scanning](3d_vision/binomial_self-compensation_for_motion_error_in_dynamic_3d_scanning.md)**

:   提出二项式自补偿(BSC)算法,通过对运动受影响的相位序列按二项式系数加权求和,无需任何中间变量即可指数级消除四步相位移轮廓术中的运动误差,实现与相机帧率相同的高精度动态3D扫描。

**[CaesarNeRF: Calibrated Semantic Representation for Few-Shot Generalizable Neural Rendering](3d_vision/caesarnerf_calibrated_semantic_representation_for_few-shot_generalizable_neural_.md)**

:   提出 CaesarNeRF，在可泛化 NeRF（GNT）基础上引入场景级语义表征，通过相机位姿校准（特征旋转对齐到目标视角）和序列细化（跨 Transformer 层逐步更新全局特征），在 1-view 设置下 PSNR 比 GNT 提升 1.74dB（LLFF），且可即插即用地增强 IBRNet、MatchNeRF 等其他基线。

**[Camera Height Doesn't Change: Unsupervised Training for Metric Monocular Road-Scene Depth Estimation](3d_vision/camera_height_doesnapost_change_unsupervised_training_for_metric_monocular_road-.md)**

:   提出FUMET训练框架,利用道路上检测到的车辆尺寸先验聚合为相机高度估计,并利用相机高度在同一视频序列中不变的事实作为度量尺度监督,使任意单目深度网络无需辅助传感器即可学习绝对尺度。

**[CanonicalFusion: Generating Drivable 3D Human Avatars from Multiple Images](3d_vision/canonicalfusion_generating_drivable_3d_human_avatars_from_multiple_images.md)**

:   提出CanonicalFusion框架,通过联合预测深度图和压缩LBS权重映射图实现直接规范化,并利用前向蒙皮可微渲染融合多张图像信息,从多张输入图像生成可驱动的3D人体Avatar。

**[CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-Aware 3D Gaussian Field](3d_vision/cg-slam_efficient_dense_rgb-d_slam_in_a_consistent_uncertainty-aware_3d_gaussian.md)**

:   提出CG-SLAM,基于一致性和几何稳定性优化的不确定性感知3D高斯场,实现高效稠密RGB-D SLAM,在定位精度和建图质量上均达到SOTA,跟踪速度最高15Hz。

**[CityGaussian: Real-Time High-Quality Large-Scale Scene Rendering with Gaussians](3d_vision/citygaussian_real-time_high-quality_large-scale_scene_rendering_with_gaussians.md)**

:   提出 CityGaussian (CityGS)，通过分治训练策略和 block-wise Level-of-Detail 机制，首次实现了城市级大规模场景（>1.5 km²）的高质量 3D Gaussian Splatting 训练与跨尺度实时渲染。

**[Compress3D: a Compressed Latent Space for 3D Generation from a Single Image](3d_vision/compress3d_a_compressed_latent_space_for_3d_generation_from_a_single_image.md)**

:   提出一种高度压缩的 triplane 潜空间自编码器，配合两阶段扩散模型（先生成 shape embedding 再生成 triplane latent），仅需 7 秒即可从单张图像生成高质量 3D 资产，且训练数据和时间远少于同类方法。

**[CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization](3d_vision/cor-gs_sparse-view_3d_gaussian_splatting_via_co-regularization.md)**

:   发现同时训练两个 3DGS 辐射场时它们在高斯位置和渲染结果上的差异（disagreement）与重建质量负相关，据此提出 CoR-GS 通过协同剪枝和伪视角协同正则化来抑制不准确重建，在稀疏视角下实现 SOTA 新视角合成。

**[CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model](3d_vision/crm_single_image_to_3d_textured_mesh_with_convolutional_reconstruction_model.md)**

:   提出卷积重建模型 CRM，利用 triplane 与六个正交视图之间的空间对齐先验，用 U-Net 替代 Transformer 直接从六视图映射到 triplane，结合 FlexiCubes 端到端训练，10 秒内从单张图像生成高保真纹理网格，训练成本仅为 LRM 的 1/8。

**[CrossScore: Towards Multi-View Image Evaluation and Scoring](3d_vision/crossscore_towards_multi-view_image_evaluation_and_scoring.md)**

:   提出 Cross-Reference（CR）图像质量评估新范式，通过对比查询图像与多个不同视角参考图像，利用 cross-attention 神经网络预测与 SSIM 高度相关的像素级质量分数，无需 ground truth 参考图像即可评估新视角合成质量。

**[CrossScore: Towards Multi-View Image Evaluation and Scoring](3d_vision/crossscore_towards_multiview_image_evaluation_and_scori.md)**

:   提出 CrossScore——一种新型的交叉参考图像质量评估方法，利用多视角参考图像替代真实参考图，通过 cross-attention 机制预测 SSIM 分数图，在无需 ground truth 的条件下实现接近全参考指标的评估精度。

**[D-SCo: Dual-Stream Conditional Diffusion for Monocular Hand-Held Object Reconstruction](3d_vision/d-sco_dual-stream_conditional_diffusion_for_monocular_hand-held_object_reconstru.md)**

:   提出双流条件扩散模型 D-SCo 从单张 RGB 图像重建手持物体点云，通过统一手-物语义嵌入和手关节几何嵌入两个分支分别提供语义和几何先验，配合手约束质心固定策略稳定扩散过程，在 ObMan 上 F-5 达 0.61（超 DDF-HO 10.9%），真实数据集 HO3D/MOW 上也大幅领先。

**[Deceptive-NeRF/3DGS: Diffusion-Generated Pseudo-observations for High-Quality Sparse-View Reconstruction](3d_vision/deceptive-nerf3dgs_diffusion-generated_pseudo-observations_for_high-quality_spar.md)**

:   利用微调的 Stable Diffusion + ControlNet 将粗糙 NeRF/3DGS 渲染结果转化为高质量伪观测图像，将稀疏输入视图增密 5-10 倍后重新训练，在 Hypersim/LLFF/ScanNet 等数据集上超越 FreeNeRF 等方法 1-2dB PSNR，训练速度比扩散正则化方法快约 10 倍。

**[DG-PIC: Domain Generalized Point-In-Context Learning for Point Cloud Understanding](3d_vision/dgpic_domain_generalized_pointincontext_learning_for_po.md)**

:   提出 DG-PIC，首个在统一模型中同时处理多域多任务点云理解的方法，通过双层源域原型估计和双层测试时特征平移机制，在无需模型更新的情况下提升对未见域的泛化能力。

**[DreamDrone: Text-to-Image Diffusion Models Are Zero-Shot Perpetual View Generators](3d_vision/dreamdrone_texttoimage_diffusion_models_are_zeroshot_perpetu.md)**

:   DreamDrone提出零样本、免训练的无限场景飞越生成pipeline，核心创新是在扩散模型的latent空间进行视角变换（而非像素空间），并通过特征对应引导和高通滤波策略保证帧间的几何一致性和高频细节一致性。

**[DreamView: Injecting View-Specific Text Guidance Into Text-to-3D Generation](3d_vision/dreamview_injecting_viewspecific_text_guidance_into_textto3d.md)**

:   DreamView通过自适应引导注入模块协调全局和视角特定文本实现3D定制化生成。

**[DSPDet3D: 3D Small Object Detection with Dynamic Spatial Pruning](3d_vision/dspdet3d_3d_small_object_detection_with_dynamic_spatial_pruning.md)**

:   提出动态空间剪枝（DSP）策略，在多级 3D 检测器的解码器中逐级移除已检测到大物体区域的体素特征，使检测器能以高空间分辨率处理场景、大幅提升小目标检测精度（ScanNet 小目标 mAP@0.25 从 27.5% 提升到 44.8%），同时通过剪枝将显存降低为同分辨率方法的 1/5。

**[FALIP: Visual Prompt as Foveal Attention Boosts CLIP Zero-Shot Performance](3d_vision/falip_visual_prompt_as_foveal_attention_boosts_clip_zer.md)**

:   提出 FALIP（Foveal-Attention CLIP），通过在 CLIP 的多头自注意力模块中插入类似人眼中央凹的注意力掩码，在不修改原始图像内容的前提下引导模型关注特定区域，显著提升指代表达理解、图像分类和 3D 点云识别等零样本任务的性能。

**[Gaussian Grouping: Segment and Edit Anything in 3D Scenes](3d_vision/gaussian_grouping_segment_and_edit_anything_in_3d_scenes.md)**

:   为 3D Gaussian Splatting 中的每个高斯学习 16 维 Identity Encoding 实现实例级分组，使用 SAM + DEVA 视频跟踪生成多视图一致的 2D 伪标签做监督，在 LERF-Mask 开放词汇分割上 mIoU 达 69-77%（超 LERF 2 倍+），全景分割超 Panoptic Lifting 4.9% mIoU 且 14× 更快，同时支持 3D 物体移除/修复/着色/风格迁移等多种编辑。

**[JointDreamer: Ensuring Geometry Consistency and Text Congruence in Text-to-3D Generation](3d_vision/jointdreamer_ensuring_geometry_consistency_and_text_congruen.md)**

:   JointDreamer提出JSD通过能量函数建模多视角联合分布确保3D一致性。

**[milliFlow: Scene Flow Estimation on mmWave Radar Point Cloud for Human Motion Sensing](3d_vision/milliflow_scene_flow_estimation_on_mmwave_radar_point_cloud_for_human_motion_sen.md)**

:   提出首个毫米波雷达点云场景流估计方法 milliFlow，通过多尺度特征提取、全局聚合、GRU 时序传播和约束回归，在自建数据集上将 EPE3D 从次优 0.107m 降至 0.046m（cm 级精度），并展示场景流特征对人体活动识别（+7.9%）、人体部位解析（+3.6%）、人体追踪等下游任务的增强效果。

**[MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo](3d_vision/mvsgaussian_fast_generalizable_gaussian_splatting_reconstruction_from_multi-view.md)**

:   将MVS的代价体深度估计与3D高斯溅射结合，通过混合渲染(splatting+volume rendering)提升泛化性，并提出基于多视图几何一致性的点云聚合策略，使per-scene优化仅需45秒就超越3D-GS的10分钟效果。

**[NOVUM: Neural Object Volumes for Robust Object Classification](3d_vision/novum_neural_object_volumes_for_robust_object_classification.md)**

:   提出 NOVUM 架构，为每个物体类别维护一个由 3D 高斯组成的神经体积表征，通过将图像特征与各类别的高斯特征匹配实现分类，在遮挡/损坏/真实 OOD 场景下相比 ResNet/ViT/Swin 等标准架构分类准确率提升 6-33%，同时支持 3D 位姿估计和可解释性可视化。

**[PointLLM: Empowering Large Language Models to Understand Point Clouds](3d_vision/pointllm_empowering_large_language_models_to_understand_point_clouds.md)**

:   将点云编码器（Point-BERT）通过 MLP 投影层对接 LLaMA 大语言模型，构建 PointLLM；利用 730K 指令数据（660K 简述 + 70K 复杂指令）两阶段训练后，在 3D 物体分类上达到 53.4% 生成式准确率（超越 LLaVA-13B 的 44.2%），在物体描述任务上人类评估胜率 55%（超越人工标注）。

**[Progressive Classifier and Feature Extractor Adaptation for Unsupervised Domain Adaptation on Point Clouds](3d_vision/progressive_classifier_and_feature_extractor_adaptation_for_unsupervised_domain_.md)**

:   提出 PCFEA 方法用于点云无监督域自适应，通过渐进构建从源域到目标域的中间域，在宏观层面用目标风格特征增强训练分类器（PTFA），微观层面引导特征提取器向中间域对齐（IDFA），在 PointDA-10 上均值准确率达 76.5%（超 SOTA +2.9%），GraspNetPC-10 上达 87.6%（超 SOTA +13.7%）。

**[ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities](3d_vision/scanreason_empowering_3d_visual_grounding_with_reasoning_capabilities.md)**

:   提出 3D reasoning grounding 新任务和 ScanReason 基准（10K+ QA-location pairs，5种推理类型），设计 ReGround3D 框架将 MLLM 推理与 3D grounding 模块通过 Chain-of-Grounding 机制协同，在隐式指令下实现准确的 3D 目标定位。

**[SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs](3d_vision/scenegraphloc_crossmodal_coarse_visual_localization_on_3d_sc.md)**

:   提出SceneGraphLoc，首次将queryimage在多模态3D场景图数据库中进行粗定位，通过学习场景图节点和图像patch的统一嵌入空间，在存储效率提升1000倍的同时接近图像检索方法的定位精度。

**[SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](3d_vision/sceneverse_scaling_3d_visionlanguage_learning_for_grounded_s.md)**

:   提出SceneVerse——首个百万级3D视觉语言数据集（68K场景+250万语言描述），通过结合人工标注和基于场景图的自动生成pipeline构建多粒度描述，并设计GPS预训练框架实现多层次场景-文本对齐，在3D grounding和QA基准上达到SOTA。

**[View Selection for 3D Captioning via Diffusion Ranking](3d_vision/view_selection_for_3d_captioning_via_diffusion_ranking.md)**

:   DiffuRank用预训练text-to-3D扩散模型评估视角对齐度选择最佳视角减少幻觉。

**[When Do We Not Need Larger Vision Models?](3d_vision/when_do_we_not_need_larger_vision_models.md)**

:   提出 Scaling on Scales (S2) 策略：冻结小模型（如 ViT-B）在多个图像尺度上运行并拼接特征，无需增加参数即可在分类、分割、深度估计、MLLM 等任务上匹敌甚至超越大模型（ViT-H/G），并从理论和实验上论证了大模型学到的表征大部分可由多尺度小模型线性近似。

---

## 🎨 图像生成 { #image_generation }

**[2S-ODIS: Two-Stage Omni-Directional Image Synthesis by Geometric Distortion Correction](image_generation/2s-odis_two-stage_omni-directional_image_synthesis_by_geometric_distortion_corre.md)**

:   2S-ODIS通过两阶段结构利用预训练VQGAN（无需微调）合成全景图像：第一阶段生成低分辨率粗略ERP图，第二阶段通过生成26个NFoV局部图像并融合来校正几何畸变，训练时间从14天缩短到4天且图像质量更优。

**[A Diffusion Model for Simulation Ready Coronary Anatomy with Morpho-skeletal Control](image_generation/a_diffusion_model_for_simulation_ready_coronary_anatomy_with.md)**

:   用潜在扩散模型（LDM）可控生成3D多组织冠状动脉分割图，通过拓扑交互损失保证解剖合理性，通过形态-骨架双通道条件化实现对截面形态和分支结构的解耦控制，并提出自适应空条件引导（ANG）以非可微回归器高效增强条件保真度，最终支持面向有限元仿真的反事实解剖结构编辑。

**[AccDiffusion: An Accurate Method for Higher-Resolution Image Generation](image_generation/accdiffusion_an_accurate_method_for_higher-resolution_image_generation.md)**

:   提出AccDiffusion，通过将全局文本prompt解耦为patch级别的内容感知prompt（利用cross-attention map判断每个词汇是否属于某patch），并引入带窗口交互的膨胀采样来改善全局一致性，在无需额外训练的情况下有效解决patch-wise高分辨率图像生成中的目标重复问题，在SDXL上实现了从2K到4K分辨率的无重复高质量图像外推。

**[AdaDiffSR: Adaptive Region-Aware Dynamic Acceleration Diffusion Model for Real-World Image Super-Resolution](image_generation/adadiffsr_adaptive_region-aware_dynamic_acceleration_diffusion_model_for_real-wo.md)**

:   观察到扩散模型超分中不同图像区域所需去噪步数差异巨大（背景区域早已收敛而前景纹理仍需迭代），提出基于多指标潜在熵（MMLE）感知信息增益来动态跳步的策略，将子区域分为稳定/增长/饱和三类给予不同步长，并通过渐进特征注入（PFJ）平衡保真度与真实感，在DRealSR等数据集上取得与StableSR可比的质量但推理时间和FLOPs分别减少1.5×和2.7×。

**[AdaGen: Learning Adaptive Policy for Image Synthesis](image_generation/adagen_learning_adaptive_policy_for_image_synthesis.md)**

:   将多步生成模型（MaskGIT/AR/Diffusion/Rectified Flow）的步级参数调度（温度、mask ratio、CFG scale、timestep等）统一建模为MDP，用轻量RL策略网络实现样本自适应调度，并提出对抗奖励设计防止策略过拟合，在四种生成范式上一致提升性能（VAR FID 1.92→1.59，DiT-XL推理成本降3倍同时性能更优）。

**[AdaNAT: Exploring Adaptive Policy for Token-Based Image Generation](image_generation/adanat_exploring_adaptive_policy_for_token-based_image_generation.md)**

:   提出AdaNAT，将非自回归Transformer（NAT）的生成策略配置建模为MDP，通过轻量策略网络+PPO强化学习+对抗奖励模型自动为每个样本定制生成策略（重掩码比例、采样温度、CFG权重等），在ImageNet-256上仅用8步达到FID 2.86，相比手工策略实现约40%的相对提升。

**[AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation](image_generation/anycontrol_create_your_artwork_with_versatile_control_on_tex.md)**

:   AnyControl提出Multi-Control Encoder，通过交替执行多控制融合块和多控制对齐块，从任意组合的多种空间控制信号中提取统一的多模态embedding，实现高质量、语义对齐的多条件可控图像生成。

**[AnyControl: Create Your Artwork with Versatile Control on Text-to-Image Generation](image_generation/anycontrol_create_your_artwork_with_versatile_control_on_text-to-image_generatio.md)**

:   提出 AnyControl，通过 Multi-Control Encoder（fusion + alignment 交替块结构）支持任意组合的多种空间控制信号（深度、边缘、分割、姿态），在 COCO 多控制基准上 FID 44.28 全面超越现有方法。

**[Bridging the Gap: Studio-Like Avatar Creation from a Monocular Phone Capture](image_generation/bridging_the_gap_studio-like_avatar_creation_from_a_monocular_phone_capture.md)**

:   提出从单目手机视频生成类似影棚级质量的面部纹理贴图的方法，结合 StyleGAN2 的 W+ 空间参数化与扩散模型超分辨率，实现从手机扫描到高质量 3D 头像的跨越。

**[ByteEdit: Boost, Comply and Accelerate Generative Image Editing](image_generation/byteedit_boost_comply_and_accelerate_generative_image_editing.md)**

:   提出 ByteEdit，一个将人类反馈学习引入生成式图像编辑（inpainting/outpainting）的框架，通过美学、对齐、一致性三个奖励模型提升编辑质量，并利用对抗训练和渐进策略加速推理。

**[Challenging Forgets: Unveiling the Worst-Case Forget Sets in Machine Unlearning](image_generation/challenging_forgets_unveiling_the_worst-case_forget_sets_in_machine_unlearning.md)**

:   提出从对抗视角识别"最坏情况遗忘集"的方法，通过双层优化框架找到最难被遗忘的数据子集，利用 SignSGD 将二阶 BLO 简化为一阶问题，从而更可靠地评估机器遗忘方法的真实效能。

**[COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation](image_generation/coin_control-inpainting_diffusion_prior_for_human_and_camera_motion_estimation.md)**

:   提出COIN方法，通过控制-补绘（Control-Inpainting）的改进版Score Distillation Sampling，结合人-场景关系损失，从单目动态相机视频中同时估计高质量的全局人体运动和相机运动。

**[ColorPeel: Color Prompt Learning with Diffusion Models via Color and Shape Disentanglement](image_generation/colorpeel_color_prompt_learning_with_diffusion_models_v.md)**

:   提出 ColorPeel，通过在目标颜色的基础几何体上联合学习颜色和形状 token 来实现颜色与形状解耦，使 T2I 扩散模型能精确生成用户指定 RGB 颜色的物体。

**[Controlling the World by Sleight of Hand](image_generation/controlling_the_world_by_sleight_of_hand.md)**

:   提出 CosHand，通过手部二值掩码作为动作条件，在预训练 Stable Diffusion 上微调，预测手-物交互后的未来图像，并可零样本泛化到机器人末端执行器。

**[Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers](image_generation/difftracker_texttoimage_diffusion_models_are_unsupervised_tr.md)**

:   Diff-Tracker利用预训练T2I扩散模型知识进行无监督跟踪，学习prompt在cross-attention上激活目标区域。

**[EMDM: Efficient Motion Diffusion Model for Fast and High-Quality Motion Generation](image_generation/emdm_efficient_motion_diffusion_model_for_fast_and_high.md)**

:   提出 EMDM，通过条件去噪扩散 GAN 捕获大步长采样时的复杂多模态去噪分布，结合几何损失约束，实现 T≤10 步的实时人体运动生成，推理速度提升 60-240 倍，同时保持高质量。

**[FineMatch: Aspect-Based Fine-Grained Image and Text Mismatch Detection and Correction](image_generation/finematch_aspectbased_finegrained_image_and_text_mismat.md)**

:   提出 FineMatch benchmark，要求模型识别图文对中不匹配的方面短语（Entity/Relation/Attribute/Number）、确定类别并提出修正，构建了 49,906 个人工标注样本，并提出 ITM-IoU 评估指标和 AutoAlign 文生图幻觉检测校正系统。

**[FreeDiff: Progressive Frequency Truncation for Image Editing with Diffusion Models](image_generation/freediff_progressive_frequency_truncation_for_image_edi.md)**

:   提出 FreeDiff，通过渐进式频率截断从频域精化扩散模型的编辑引导信号，无需微调或修改网络结构，实现覆盖多种编辑类型的通用图像编辑方法。

**[FreeInit: Bridging Initialization Gap in Video Diffusion Models](image_generation/freeinit_bridging_initialization_gap_in_video_diffusion.md)**

:   提出 FreeInit，一种无需额外训练的推理采样策略，通过迭代精炼初始噪声的时空低频分量来弥合视频扩散模型训练与推理之间的初始化差距，显著提升生成视频的时序一致性。

**[Getting it Right: Improving Spatial Consistency in Text-to-Image Models](image_generation/getting_it_right_improving_spatial_consistency_in_texttoimag.md)**

:   发现现有VL数据集严重缺乏空间关系描述（如left/right/above/behind出现率极低），构建了首个空间聚焦的大规模数据集SPRIGHT（600万张图像重描述），仅用0.25%数据微调即可提升22%空间一致性得分，用<500张多物体图像微调达到T2I-CompBench空间SOTA 0.2133。

**[HybridBooth: Hybrid Prompt Inversion for Efficient Subject-Driven Generation](image_generation/hybridbooth_hybrid_prompt_inversion_for_efficient_subje.md)**

:   提出 HybridBooth，融合优化方法和直接回归方法的优势——先用预训练编码器（Word Embedding Probe）生成初始 word embedding，再通过残差精细化（仅 3-5 步）快速适配特定主体，实现高效高保真的 subject-driven 生成。

**[Infinite-ID: Identity-Preserved Personalization via ID-Semantics Decoupling Paradigm](image_generation/infiniteid_identitypreserved_personalization_via_idsema.md)**

:   提出 Infinite-ID，通过 ID-语义解耦范式将身份信息和文本语义信息分离训练，再通过混合注意力机制和 AdaIN-mean 操作在推理时融合，实现高保真身份保持与精确语义控制的平衡。

**[∞-Brush: Controllable Large Image Synthesis with Diffusion Models in Infinite Dimensions](image_generation/inftybrush_controllable_large_image_synthesis_with_diffusion.md)**

:   提出首个在无限维函数空间中的条件扩散模型 ∞-Brush，通过交叉注意力神经算子实现可控条件生成，仅用 0.4% 像素训练即可在任意分辨率（最高 4096×4096）上生成保持全局结构的大图像。

**[Latent Guard: A Safety Framework for Text-to-Image Generation](image_generation/latent_guard_a_safety_framework_for_texttoimage_generation.md)**

:   Latent Guard在T2I文本编码器上学习潜在空间检测黑名单概念。

**[LCM-Lookahead for Encoder-Based Text-to-Image Personalization](image_generation/lcmlookahead_for_encoderbased_texttoimage_personalization.md)**

:   本文提出利用LCM（Latent Consistency Model）作为"快捷通道"，在扩散模型encoder训练中实现图像空间损失（如身份识别loss）的反向传播，配合自注意力特征共享和一致性数据生成，显著提升encoder-based人脸个性化的身份保持和prompt对齐能力。

**[Learning Trimodal Relation for Audio-Visual Question Answering with Missing Modality](image_generation/learning_trimodal_relation_for_audiovisual_question_answerin.md)**

:   提出面向音视觉问答（AVQA）的缺失模态处理框架，通过Relation-aware Missing Modal生成器利用三模态关系召回缺失信息，再通过Audio-Visual Relation-aware扩散模型增强特征表示，即使缺少一个模态也能准确回答问题。

**[LEGO: Learning EGOcentric Action Frame Generation via Visual Instruction Tuning](image_generation/lego_learning_egocentric_action_frame_generation_via_vi.md)**

:   提出 LEGO 模型，通过视觉指令微调增强 VLLM 的动作描述能力，并将 VLLM 的图像/文本嵌入作为额外条件注入扩散模型，实现从第一人称视角生成动作执行帧。

**[MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed-Precision Quantization](image_generation/mixdq_memoryefficient_fewstep_texttoimage_diffusion_models_w.md)**

:   针对少步扩散模型（如SDXL-turbo 1-step）比多步模型更难量化的问题，提出MixDQ混合精度量化方法，包含BOS-aware文本嵌入量化、指标解耦敏感度分析和整数规划比特分配，在W4A8下仅增加0.5 FID，实现3倍模型压缩和1.5倍加速。

**[MotionChain: Conversational Motion Controllers via Multimodal Prompts](image_generation/motionchain_conversational_motion_controllers_via_multimodal.md)**

:   MotionChain构建视觉-运动语言模型，通过VQ-VAE将动作token化支持多轮对话运动生成。

**[Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization](image_generation/pixelaware_stable_diffusion_for_realistic_image_superre.md)**

:   提出像素感知稳定扩散（PASD）网络，通过像素感知交叉注意力（PACA）在潜空间中实现像素级结构保持，配合退化移除模块和可调噪声调度，统一解决真实图像超分辨率和个性化风格迁移两大任务。

**[Ponymation: Learning Articulated 3D Animal Motions from Unlabeled Online Videos](image_generation/ponymation_learning_articulated_3d_animal_motions_from_.md)**

:   提出从原始、无标签的互联网视频中学习动物 3D 关节运动生成模型的方法，核心是一个视频光几何自编码框架，将训练视频分解为静止姿态形状、关节姿态序列和纹理，实现无需姿态标注的 3D 运动 VAE 学习。

**[Powerful and Flexible: Personalized Text-to-Image Generation via Reinforcement Learning](image_generation/powerful_and_flexible_personalized_texttoimage_generation_vi.md)**

:   将个性化T2I建模为DPG框架，引入Q函数和向前看机制捕获长期视觉一致性。

**[Removing Distributional Discrepancies in Captions Improves Image-Text Alignment](image_generation/removing_distributional_discrepancies_in_captions_improves_i.md)**

:   发现训练图文对齐模型时正负caption之间存在被忽视的数据集级别分布偏差（如GPT生成负样本时倾向用elephant替换giraffe），提出用纯文本分类器过滤高置信样本来消除偏差，结合替换型+交换型两类负样本微调LLaVA-1.5，在Winoground、SeeTRUE等多个基准上大幅超越现有方法。

**[ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation](image_generation/scaledreamer_scalable_textto3d_synthesis_with_asynchronous_s.md)**

:   提出异步分数蒸馏(ASD)，通过将扩散时间步前移（而非微调扩散模型）来减小噪声预测误差，实现稳定的3D生成器训练并可扩展到100K文本提示，保持扩散模型的文本理解能力不受损。

**[Soft Prompt Generation for Domain Generalization](image_generation/soft_prompt_generation_for_domain_generalization.md)**

:   提出 SPG（Soft Prompt Generation），首次将生成模型引入 VLM 的 prompt learning，通过 CGAN 从图像动态生成实例特定的软提示，将域知识存储在生成模型中而非提示向量中，实现更好的领域泛化性能。

**[Text2Place: Affordance-Aware Text Guided Human Placement](image_generation/text2place_affordanceaware_text_guided_human_placement.md)**

:   提出 Text2Place，通过 SDS 损失优化 Gaussian blob 参数化的语义掩码学习场景中的人体 affordance，再结合主体条件修复实现逼真的文本引导人物放置，无需大规模训练。

**[TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering](image_generation/textdiffuser2_unleashing_the_power_of_language_models_f.md)**

:   TextDiffuser-2 利用两个语言模型（一个用于布局规划、一个用于布局编码）实现灵活自动的文本渲染，克服了现有方法在灵活性、布局能力和样式多样性方面的局限。

**[Towards Reliable Advertising Image Generation Using Human Feedback](image_generation/towards_reliable_advertising_image_generation_using_human_fe.md)**

:   针对电商广告图像生成中大量不可用图像（空间不匹配、尺寸不匹配、不显著、形状幻觉）的问题，构建了百万级RF1M数据集训练多模态检测网络RFNet，并提出基于RFNet反馈微调扩散模型的RFFT方法（含Consistent Condition正则化），将可用率从约50%提升至接近100%且不损失美观性。

**[XPSR: Cross-modal Priors for Diffusion-based Image Super-Resolution](image_generation/xpsr_crossmodal_priors_for_diffusionbased_image_superresolut.md)**

:   XPSR提出将多模态大语言模型（LLaVA）生成的高层与低层语义描述作为跨模态先验，通过Semantic-Fusion Attention融合到扩散模型中，并设计Degradation-Free Constraint提取语义保留特征，实现高保真高真实感的图像超分辨率。

---

## 🧑 人体理解 { #human_understanding }

**[3D Hand Pose Estimation in Everyday Egocentric Images](human_understanding/3d_hand_pose_estimation_in_everyday_egocentric_images.md)**

:   通过系统研究裁剪输入、相机内参感知位置编码(KPE)、辅助监督(手部分割+抓握标签)和多数据集联合训练这四个实践，提出WildHands系统，在仅用ResNet50和少量数据的条件下，实现了对野外第一人称图像中3D手部姿态的鲁棒估计，零样本泛化超过FrankMocap全部指标且与10倍大的HaMeR竞争。

**[3DGazeNet: Generalizing 3D Gaze Estimation with Weak-Supervision from Synthetic Views](human_understanding/3dgazenet_generalizing_3d_gaze_estimation_with_weak-supervision_from_synthetic_v.md)**

:   提出将视线估计重新表述为密集3D眼球网格回归，并通过从大规模野外人脸图像中自动提取伪标签+HeadGAN合成多视图进行弱监督训练，在跨域场景下比SOTA提升最多30%。

**[A Probability-guided Sampler for Neural Implicit Surface Rendering](human_understanding/a_probabilityguided_sampler_for_neural_implicit_surface_rend.md)**

:   提出一种概率引导的光线采样器（Probability-guided Sampler），在3D图像投影空间中建模概率密度函数来指导光线采样朝向感兴趣区域，同时设计了包含近表面和空白空间两个分量的新型表面重建损失，可作为插件集成到现有神经隐式表面渲染器中，显著提升重建精度和渲染质量。

**[A Simple Baseline for Spoken Language to Sign Language Translation with 3D Avatars](human_understanding/a_simple_baseline_for_spoken_language_to_sign_language_trans.md)**

:   提出首个基于3D Avatar输出的Spoken2Sign翻译基线系统，通过三步流程（字典构建→SMPLSign-X 3D手语估计→检索-连接-渲染翻译）将口语文本翻译为3D手语动画，在Phoenix-2014T上back-translation BLEU-4达25.46，同时其3D手语副产品（关键点增强和多视角理解）显著提升了手语理解任务性能。

**[AdaDistill: Adaptive Knowledge Distillation for Deep Face Recognition](human_understanding/adadistill_adaptive_knowledge_distillation_for_deep_face_rec.md)**

:   提出AdaDistill，将知识蒸馏概念嵌入margin penalty softmax loss中，通过基于EMA的自适应类中心（早期用sample-sample简单知识、后期用sample-center复杂知识）和困难样本感知机制，无需额外超参数即可提升轻量级人脸识别模型的判别能力，在IJB-B/C和ICCV21-MFR等挑战性基准上超越SOTA蒸馏方法。

**[ADen: Adaptive Density Representations for Sparse-view Camera Pose Estimation](human_understanding/aden_adaptive_density_representations_for_sparseview_camera.md)**

:   ADen提出生成器-判别器框架统一位姿回归和概率位姿估计：生成器输出多个6DoF位姿假设来建模多模态分布（处理对称歧义），判别器选出最佳假设，在稀疏视角位姿估计上同时实现了更高精度和更低运行时间。

**[Alignist: CAD-Informed Orientation Distribution Estimation by Fusing Shape and Correspondences](human_understanding/alignist_cad-informed_orientation_distribution_estimation_by_fusing_shape_and_co.md)**

:   提出 Alignist，首个利用 CAD 模型信息（SDF + SurfEmb 对应特征）训练隐式分布网络来推断 SO(3) 上姿态分布的方法，通过 product of experts 融合几何和特征对齐，在低数据场景下显著优于对比学习方法。

**[Audio-Driven Talking Face Generation with Stabilized Synchronization Loss](human_understanding/audio-driven_talking_face_generation_with_stabilized_synchronization_loss.md)**

:   提出 AVSyncNet、stabilized synchronization loss 和 silent-lip generator 三项改进，系统性地解决音频驱动说话人脸生成中 SyncNet 不稳定和嘴唇泄漏两大核心问题，在唇形同步和视觉质量上均达到 SOTA。

**[Bi-TTA: Bidirectional Test-Time Adapter for Remote Physiological Measurement](human_understanding/bi-tta_bidirectional_test-time_adapter_for_remote_physiological_measurement.md)**

:   提出 Bi-TTA 框架，首次将 Test-Time Adaptation 引入远程光电容积脉搏波 (rPPG) 任务，通过时空一致性自监督先验和前瞻-回溯双向适应策略，在推理时仅用无标注单实例数据即可完成模型域适应。

**[Combining Generative And Geometry Priors For Wide-Angle Portrait Correction](human_understanding/combining_generative_and_geometry_priors_for_wide-angle_portrait_correction.md)**

:   提出结合 StyleGAN 生成式先验（用于人脸矫正）和几何对称先验（用于背景直线矫正）的双模块框架，大幅提升广角人像畸变校正的视觉质量和定量指标。

**[CoMo: Controllable Motion Generation Through Language Guided Pose Code Editing](human_understanding/como_controllable_motion_generation_through_language_guided_pose_code_editing.md)**

:   提出 CoMo，通过将动作序列分解为语义明确的 pose code（如"左膝微弯"），实现基于文本的可控动作生成与基于 LLM 的零样本动作编辑。

**[Decomposed Vector-Quantized Variational Autoencoder for Human Grasp Generation](human_understanding/decomposed_vector-quantized_variational_autoencoder_for_human_grasp_generation.md)**

:   提出 Decomposed VQ-VAE (DVQ-VAE)，通过将手部分解为六个部分分别编码到独立码本，并设计双阶段解码策略（先姿态后位置），在四个基准数据集上质量指标相对提升约14.1%。

**[Domain Reduction Strategy for Non-Line-of-Sight Imaging](human_understanding/domain_reduction_strategy_for_non-line-of-sight_imaging.md)**

:   提出一种面向非视线成像（NLOS）的优化方法，通过将瞬态信号建模为逐点光传播函数的叠加，并设计由粗到细的域缩减策略剪除空白区域，在通用NLOS场景下实现约20倍加速且同时重建反射率和表面法线。

**[EgoExo-Fitness: Towards Egocentric and Exocentric Full-Body Action Understanding](human_understanding/egoexo-fitness_towards_egocentric_and_exocentric_full-body_action_understanding.md)**

:   提出 EgoExo-Fitness 数据集，包含同步的第一人称和第三人称健身视频，提供两级时间边界标注和创新性的可解释动作评判标注（技术关键点验证、自然语言评论、质量评分），并构建五个基准任务。

**[EvSign: Sign Language Recognition and Translation with Streaming Events](human_understanding/evsign_sign_language_recognition_and_translation_with_streaming_events.md)**

:   首次构建面向连续手语识别（CSLR）和手语翻译（SLT）任务的事件相机基准数据集 EvSign，并提出基于稀疏Transformer的高效框架，在仅0.34% FLOPs和44.2%参数量下达到与SOTA RGB方法可比或更优的性能。

**[Large Motion Model for Unified Multi-Modal Motion Generation](human_understanding/large_motion_model_for_unified_multimodal_motion_generation.md)**

:   LMM是首个多模态通用人体动作生成模型，统一了文本/动作/音乐/语音等10种任务、16个数据集（320K序列/1亿帧），通过身体部位感知的ArtAttention机制和可变帧率+随机遮掩的预训练策略，在多个标准benchmark上与专家模型竞争甚至超越。

**[QUAR-VLA: Vision-Language-Action Model for Quadruped Robots](human_understanding/quarvla_visionlanguageaction_model_for_quadruped_robots.md)**

:   提出 QUAR-VLA 范式，首次将视觉、语言指令和动作生成统一到四足机器人中，构建了大规模多任务数据集 QUARD（259K episodes），训练 QUART 模型（基于 8B VLM）实现感知、导航、全身操控等多种任务，并展示了从仿真到真实的迁移能力。

**[Self-supervised Feature Adaptation for 3D Industrial Anomaly Detection](human_understanding/selfsupervised_feature_adaptation_for_3d_industrial_ano.md)**

:   提出 LSFA（Local-to-global Self-supervised Feature Adaptation），通过模态内特征紧致化（IFC）和跨模态局部到全局一致性对齐（CLC）微调适配器，学习面向异常检测的任务导向表示，在 MVTec-3D AD 上达到 97.1% I-AUROC（+3.4%）。

**[WordRobe: Text-Guided Generation of Textured 3D Garments](human_understanding/wordrobe_textguided_generation_of_textured_3d_garments.md)**

:   提出 WordRobe 框架，通过学习 3D 服装潜在空间并与 CLIP 嵌入对齐，实现文本驱动的带纹理 3D 服装网格生成，并利用 ControlNet 的单步前向推理实现高效视角一致的纹理合成。

---

## ✂️ 语义分割 { #segmentation }

**[A Semantic Space is Worth 256 Language Descriptions: Make Stronger Segmentation Models with Descriptive Properties](segmentation/a_semantic_space_is_worth_256_language_descriptions_make_str.md)**

:   ProLab 用 LLM 生成类别的常识性描述，通过句子嵌入和 K-Means 聚类将其压缩为 256 个可解释的描述性属性，构建属性级多热标签空间替代传统 one-hot 类别标签来监督分割模型，在五个经典基准上一致超越类别级监督且涌现出域外泛化能力。

**[A Simple Latent Diffusion Approach for Panoptic Segmentation and Mask Inpainting](segmentation/a_simple_latent_diffusion_approach_for_panoptic_segmentation_and_mask_inpainting.md)**

:   基于Stable Diffusion构建了一个极简的潜在扩散分割框架LDMSeg，通过浅层自编码器将分割mask压缩到潜空间、再训练图像条件扩散模型来生成全景分割结果，避免了传统方法中的目标检测模块、匈牙利匹配和复杂后处理，并天然支持mask inpainting和多任务扩展。

**[ActionVOS: Actions as Prompts for Video Object Segmentation](segmentation/actionvos_actions_as_prompts_for_video_object_segmentation.md)**

:   提出ActionVOS——一种以人类动作叙述作为额外语言提示的Referring Video Object Segmentation新设定，通过无参数的动作感知标注模块生成伪标签，并设计动作引导的focal loss来抑制假阳性，在VISOR上将非活跃物体的误分割降低35.6% mIoU，同时在VOST/VSCOS上对状态变化物体的分割提升3.0% mIoU。

**[Active Coarse-to-Fine Segmentation of Moveable Parts from Real Images](segmentation/active_coarsetofine_segmentation_of_moveable_parts_from_real.md)**

:   提出首个面向真实室内场景RGB图像中可运动部件实例分割的主动学习框架，通过姿态感知masked attention网络实现由粗到细的分割，仅需人工标注11.45%的图像即可获得全量验证的高质量分割结果，相比最优非AL方法节省60%人工时间。

**[AdaLog: Post-Training Quantization for Vision Transformers with Adaptive Logarithm Quantizer](segmentation/adalog_post-training_quantization_for_vision_transformers_with_adaptive_logarith.md)**

:   提出自适应对数底量化器AdaLog，通过可搜索的对数底替代固定log₂/log√2量化器来处理ViT中post-Softmax和post-GELU激活的幂律分布，并设计快速渐进组合搜索(FPCS)策略高效确定量化超参，在极低比特(3/4-bit)下显著优于现有ViT PTQ方法。

**[BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion](segmentation/brushnet_a_plug-and-play_image_inpainting_model_with_decomposed_dual-branch_diff.md)**

:   提出 BrushNet，一种即插即用的双分支扩散模型图像修复架构，通过将遮罩图像特征提取与图像生成解耦到独立分支，实现逐层像素级特征注入，在图像质量、遮罩区域保持和文本对齐三方面全面超越已有方法。

**[CoLA: Conditional Dropout and Language-Driven Robust Dual-Modal Salient Object Detection](segmentation/cola_conditional_dropout_and_language-driven_robust_dual-modal_salient_object_de.md)**

:   提出 CoLA 框架，通过语言驱动的质量评估（LQA）和条件性 Dropout（CD）两个核心模块，首次在双模态显著性目标检测中同时解决噪声输入和模态缺失两大鲁棒性问题。

**[ColorMAE: Exploring Data-Independent Masking Strategies in Masked AutoEncoders](segmentation/colormae_exploring_data-independent_masking_strategies_in_masked_autoencoders.md)**

:   提出 ColorMAE，通过对随机噪声施加不同频域滤波器生成具有空间与语义先验的数据无关遮罩模式，在不增加任何参数和计算开销的前提下，显著提升 MAE 的下游任务表现，尤其在语义分割任务上相比随机遮罩提升 2.72 mIoU。

**[ControlNet++: Improving Conditional Controls with Efficient Consistency Feedback](segmentation/controlnet_improving_conditional_controls_with_efficien.md)**

:   提出 ControlNet++，通过预训练判别模型提取生成图像的条件并优化像素级循环一致性损失来显式提升可控生成的精度，同时提出高效单步去噪奖励策略避免多步采样的巨大开销。

**[ControlNet++: Improving Conditional Controls with Efficient Consistency Feedback](segmentation/controlnet_improving_conditional_controls_with_efficient_consistency_feedback.md)**

:   提出 ControlNet++，通过像素级循环一致性损失显式优化条件可控生成质量：用预训练判别模型从生成图像中提取条件并与输入条件对齐，并设计高效单步去噪 reward 策略避免多步采样的巨大显存开销，在分割掩码、边缘、深度等多种条件控制下显著提升可控性（如分割 mIoU +11.1%）。

**[CoReS: Orchestrating the Dance of Reasoning and Segmentation](segmentation/cores_orchestrating_the_dance_of_reasoning_and_segmentation.md)**

:   提出 CoReS（Chains of Reasoning and Segmenting），一种双链结构的多模态思维链框架，通过推理链和分割链的层次化协作，结合 in-context 引导策略，实现对复杂推理文本中目标物体的渐进式精确分割，在 ReasonSeg 数据集上超越 LISA 6.5%。

**[CPM: Class-Conditional Prompting Machine for Audio-Visual Segmentation](segmentation/cpm_class-conditional_prompting_machine_for_audio-visual_segmentation.md)**

:   提出 CPM（Class-conditional Prompting Machine），通过结合类无关查询与基于 GMM 采样的类条件查询来增强 Mask2Former 在音视频分割中的二部图匹配稳定性和跨模态注意力效力，同时设计音频条件提示（ACP）、视觉条件提示（VCP）和提示对比学习（PCL）三个辅助任务，在 AVSBench 和 VPO 基准上达到 SOTA。

**[Cs2K: Class-Specific and Class-Shared Knowledge Guidance for Incremental Semantic Segmentation](segmentation/cs2k_class-specific_and_class-shared_knowledge_guidance_for_incremental_semantic.md)**

:   提出 Cs2K 框架，从类别特有知识（原型引导伪标签 + 原型引导类别适应）和类别共享知识（权重引导选择性整合）两个方面协同缓解增量语义分割中的灾难性遗忘与新类欠拟合问题。

**[DenseNets Reloaded: Paradigm Shift Beyond ResNets and ViTs](segmentation/densenets_reloaded_paradigm_shift_beyond_resnets_and_vits.md)**

:   重新审视 DenseNet 的密集拼接连接（concatenation shortcut），通过系统性现代化改造（加宽减深、现代化 block、扩大中间维度、更多 transition 层等），提出 RDNet（Revitalized DenseNet），在 ImageNet-1K 上超越 Swin Transformer、ConvNeXt、DeiT-III，证明了拼接连接作为一种被低估的范式具有强大潜力。

**[Exploring Pre-trained Text-to-Video Diffusion Models for Referring Video Object Segmentation](segmentation/exploring_pretrained_texttovideo_diffusion_models_for_referr.md)**

:   VD-IT首次探索预训练T2V扩散模型（ModelScopeT2V）在视频理解任务中的应用，通过Text-Guided Image Projection和Video-specific Noise Prediction设计，从固定T2V模型中提取语义对齐、时序一致的视频特征，在Referring VOS任务上超越传统判别式backbone。

**[OpenPSG: Open-set Panoptic Scene Graph Generation via Large Multimodal Models](segmentation/openpsg_openset_panoptic_scene_graph_generation_via_large_mu.md)**

:   本文首次提出开放集全景场景图生成任务（OpenPSG），利用大型多模态模型（BLIP-2）以自回归方式预测物体间的开放集关系，通过关系查询Transformer高效提取物体对特征并过滤无关对，在闭集和开放集设置下均取得SOTA。

**[Rotary Position Embedding for Vision Transformer](segmentation/rotary_position_embedding_for_vision_transformer.md)**

:   本文系统研究了将 RoPE（Rotary Position Embedding）从1D语言模型扩展到2D视觉任务的方法，提出 RoPE-Mixed（混合可学习频率）替代传统的 Axial 频率分配，在 ViT 和 Swin Transformer 上实现了显著的分辨率外推性能提升，在 ImageNet 分类、COCO 检测和 ADE20k 分割上均带来一致增益。

**[SCLIP: Rethinking Self-Attention for Dense Vision-Language Inference](segmentation/sclip_rethinking_selfattention_for_dense_visionlanguage_infe.md)**

:   发现CLIP在密集预测中失败的根因是自注意力机制导致的空间位置错配（spatial-invariant features），提出Correlative Self-Attention(CSA)机制——仅用一个投影矩阵计算token间相关性作为注意力分数，无需任何训练/额外参数即可将CLIP的零样本语义分割mIoU从14.1%提升至38.2%（8个基准平均），大幅超越现有SOTA的33.9%。

**[VISA: Reasoning Video Object Segmentation via Large Language Models](segmentation/visa_reasoning_video_object_segmentation_via_large_language_models.md)**

:   提出 ReasonVOS 新任务和 VISA 模型，利用多模态 LLM 的世界知识推理能力实现基于隐式文本查询的视频目标分割与跟踪。

---

## 🚗 自动驾驶 { #autonomous_driving }

**[4D Contrastive Superflows are Dense 3D Representation Learners](autonomous_driving/4d_contrastive_superflows_are_dense_3d_representation_learners.md)**

:   提出SuperFlow框架，通过视图一致性对齐、稠密-稀疏一致性正则化、和基于流的时空对比学习三个模块，利用连续LiDAR-相机对建立4D预训练目标，在11个异构LiDAR数据集上全面超越了之前的Image-to-LiDAR预训练方法。

**[Accelerating Online Mapping and Behavior Prediction via Direct BEV Feature Attention](autonomous_driving/accelerating_online_mapping_and_behavior_prediction_via_dire.md)**

:   提出直接将在线地图估计模型内部的BEV特征暴露给下游轨迹预测模型（而非仅传递解码后的矢量化地图），通过三种BEV特征注入策略实现推理加速最高73%、预测精度提升最高29%。

**[Adaptive Human Trajectory Prediction via Latent Corridors](autonomous_driving/adaptive_human_trajectory_prediction_via_latent_corridors.md)**

:   将prompt tuning思想引入行人轨迹预测，通过在预训练轨迹预测器的输入端添加可学习的低秩图像prompt（称为latent corridors），以不到0.1%的额外参数实现对部署场景特定行为模式的高效自适应，在合成和真实数据上分别取得最高23.9%和26.8%的ADE提升。

**[Approaching Outside: Scaling Unsupervised 3D Object Detection from 2D Scene](autonomous_driving/approaching_outside_scaling_unsupervised_3d_object_detection_from_2d_scene.md)**

:   提出 LiSe 方法，将 2D 图像信息引入无监督 3D 目标检测，通过自步学习（self-paced learning）中的自适应采样和弱模型聚合策略，大幅提升远距离和小目标的检测能力。

**[CarFormer: Self-Driving with Learned Object-Centric Representations](autonomous_driving/carformer_self-driving_with_learned_object-centric_representations.md)**

:   提出 CarFormer，首次将自监督 slot attention 学到的 object-centric 表征用于自动驾驶，在 CARLA Longest6 基准上超越了使用精确物体属性的 PlanT，同时具备世界模型预测未来状态的能力。

**[DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion and Bi-directional Structure Alignment](autonomous_driving/dvlo_deep_visual-lidar_odometry_with_local-to-global_feature_fusion_and_bi-direc.md)**

:   提出基于聚类的 Local-to-Global 融合网络 DVLO，通过双向结构对齐（图像→伪点云 + 点云→伪图像）解决视觉与 LiDAR 的数据结构不一致问题，在 KITTI 里程计和 FlyingThings3D 场景流任务上均取得 SOTA。

**[DVLO: Deep Visual-LiDAR Odometry with Local-to-Global Feature Fusion and Bi-Directional Structure Alignment](autonomous_driving/dvlo_deep_visuallidar_odometry_with_localtoglobal_featu.md)**

:   提出 DVLO——基于从局部到全局融合 + 双向结构对齐的视觉-LiDAR 里程计网络，通过将图像视为伪点云进行局部聚类融合、将点云投影为伪图像进行全局自适应融合，解决了两种模态间固有的数据结构不一致问题。

**[Enhancing Vectorized Map Perception with Historical Rasterized Maps](autonomous_driving/enhancing_vectorized_map_perception_with_historical_rasterized_maps.md)**

:   提出 HRMapNet，通过维护一张低成本的全局历史栅格化地图（historical rasterized map），为在线矢量化地图感知提供互补先验信息，在 BEV 特征聚合和 query 初始化两个层面增强现有方法，在 nuScenes 和 Argoverse 2 上取得显著提升。

**[Equivariant Spatio-Temporal Self-Supervision for LiDAR Object Detection](autonomous_driving/equivariant_spatio-temporal_self-supervision_for_lidar_object_detection.md)**

:   E-SSL3D 提出一种时空联合等变自监督预训练框架，通过空间等变（对旋转用分类目标、对平移/缩放/翻转用对比目标）和时间等变（用 3D 场景流约束相邻帧特征变换一致性）联合训练 3D 特征编码器，在低数据场景下仅用 20% 标注数据就能达到接近 100% 数据从头训练的检测性能。

**[FSD-BEV: Foreground Self-Distillation for Multi-View 3D Object Detection](autonomous_driving/fsd-bev_foreground_self-distillation_for_multi-view_3d_object_detection.md)**

:   提出前景自蒸馏（FSD）框架，在同一模型内构建教师-学生分支共享图像特征，避免跨模态蒸馏中的分布差异问题，配合点云增强和多尺度前景增强模块，在 nuScenes 上取得 SOTA 性能。

**[Fully Sparse 3D Occupancy Prediction](autonomous_driving/fully_sparse_3d_occupancy_prediction.md)**

:   提出 SparseOcc，首个完全稀疏的 3D 占用预测网络，通过稀疏体素解码器和掩码引导的 Mask Transformer 实现高效占用预测，并设计了 RayIoU 评价指标解决传统 mIoU 的深度方向不一致惩罚问题。

**[GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction](autonomous_driving/gaussianformer_scene_as_gaussians_for_vision-based_3d_semantic_occupancy_predict.md)**

:   提出以物体为中心的 3D 语义高斯表示替代传统密集体素，用一组稀疏的 3D 语义高斯描述场景并通过高斯到体素的 splatting 生成占用预测，在性能可比的情况下将内存消耗降低 75%-82%。

**[LiDAR-Event Stereo Fusion with Hallucinations](autonomous_driving/lidarevent_stereo_fusion_with_hallucinations.md)**

:   首次探索 LiDAR 与事件立体相机的融合，提出虚拟堆叠幻觉（VSH）和回溯时间幻觉（BTH）两种策略，通过在事件流/堆叠中注入虚拟事件来增强匹配可辨别性，大幅提升事件立体匹配精度。

**[Navigation Instruction Generation with BEV Perception and Large Language Models](autonomous_driving/navigation_instruction_generation_with_bev.md)**

:   提出 BEVInstructor，将鸟瞰图 (BEV) 特征融入多模态大语言模型 (MLLM) 用于导航指令生成，通过 Perspective-BEV 视觉编码、参数高效 prompt tuning 和实例引导的迭代精化，在室内外多个数据集上全面超越 SOTA。

**[OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving](autonomous_driving/occgen_generative_multimodal_3d_occupancy_prediction_for_aut.md)**

:   提出OccGen，首次将扩散模型的"噪声到占据"生成范式引入3D语义占据预测任务，通过条件编码器+渐进式精炼解码器实现由粗到精的占据图生成，在nuScenes-Occupancy上多模态/纯LiDAR/纯相机设置下分别提升mIoU 9.5%/6.3%/13.3%。

**[Reason2Drive: Towards Interpretable and Chain-Based Reasoning for Autonomous Driving](autonomous_driving/reason2drive_towards_interpretable_and_chainbased_reasoning.md)**

:   构建 Reason2Drive 基准数据集（600K+ 视频-文本对，覆盖感知-预测-推理链式任务），提出 ADRScore 评估链式推理正确性的新指标，并设计 Prior Tokenizer + Instructed Vision Decoder 框架增强 VLM 的目标级感知和推理能力，在自动驾驶推理任务上显著超越所有基线。

**[VisionTrap: Vision-Augmented Trajectory Prediction Guided by Textual Descriptions](autonomous_driving/visiontrap_visionaugmented_trajectory_prediction_guided.md)**

:   提出 VisionTrap，利用环视相机视觉输入和 VLM/LLM 生成的文本描述作为训练监督，增强自动驾驶场景下的多智能体轨迹预测，同时保持 53ms 实时推理速度。

---

## 💬 LLM / NLP { #llm_nlp }

**[AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection](llm_nlp/adaclip_adapting_clip_with_hybrid_learnable_prompts_for_zero.md)**

:   在CLIP中同时引入静态（全局共享）和动态（逐图生成）两种可学习提示，用辅助异常检测数据训练后，在14个工业+医学异常检测数据集上实现零样本SOTA，核心在于"任务级+实例级"双层自适应的混合提示设计。

**[ColorMNet: A Memory-based Deep Spatial-Temporal Feature Propagation Network for Video Colorization](llm_nlp/colormnet_a_memory-based_deep_spatial-temporal_feature_propagation_network_for_v.md)**

:   提出 ColorMNet，一种基于记忆机制的时空特征传播网络，通过预训练大视觉模型引导的特征提取（PVGFE）、基于记忆的特征传播（MFP）和局部注意力（LA）三个模块，在显著降低 GPU 显存消耗（仅需 1.9G）的同时实现了优于 SOTA 的视频上色效果。

**[Dataset Growth](llm_nlp/dataset_growth.md)**

:   提出 InfoGrowth，一种高效的在线数据清洗与选择算法，通过噪声检测+信息增益计算+采样策略，使数据集在持续增长过程中保持清洁性与多样性，实现 2-4 倍数据效率提升。

**[Deep Cost Ray Fusion for Sparse Depth Video Completion](llm_nlp/deep_cost_ray_fusion_for_sparse_depth_video_completion.md)**

:   本文提出 RayFusion 框架，通过在 cost volume 上沿射线方向施加 self-attention 和 cross-attention 实现时序融合，以仅 1.15M 参数在 KITTI、VOID、ScanNetV2 三个数据集上全面超越或持平 SOTA 稀疏深度补全方法。

**[FunQA: Towards Surprising Video Comprehension](llm_nlp/funqa_towards_surprising_video_comprehension.md)**

:   构建了大规模反直觉视频问答基准 FunQA（4.3K 视频、312K QA 对），覆盖幽默/创意/魔术三类令人惊讶的视频，并提出 FunMentor 智能体通过多轮对话增强 VLM 的反常识推理能力。

**[Grounding Language Models for Visual Entity Recognition](llm_nlp/grounding_language_models_for_visual_entity_recognition.md)**

:   提出 AutoVER——首个将多模态大语言模型（MLLM）应用于大规模视觉实体识别的方法，通过将检索能力集成到 MLLM 内部，结合对比训练和前缀树约束解码，在 Oven-Wiki 基准上大幅超越 PaLI-17B 等先前方法。

**[On the Utility of 3D Hand Poses for Action Recognition](llm_nlp/on_the_utility_of_3d_hand_poses_for_action_recognition.md)**

:   提出 HandFormer，一种高效多模态 Transformer，通过密集采样的 3D 手部姿态与稀疏采样的 RGB 帧相结合，以远低于现有方法的计算量实现了手-物交互动作识别 SOTA。

**[OneRestore: A Universal Restoration Framework for Composite Degradation](llm_nlp/onerestore_a_universal_restoration_framework_for_composite_degradation.md)**

:   提出 OneRestore，一种基于 Transformer 的通用图像复原框架，通过场景描述符引导的交叉注意力机制和复合退化复原损失，能在单一模型中自适应地处理低光照、雾、雨、雪及其任意组合的复合退化场景，并支持文本/视觉双模式的可控复原。

**[Prompting Language-Informed Distribution for Compositional Zero-Shot Learning](llm_nlp/prompting_language-informed_distribution_for_compositional_zero-shot_learning.md)**

:   本文提出 PLID 方法，利用 LLM 生成的句子级类别描述构建语言知识驱动的高斯分布，配合视觉-语言原语分解和随机 logit 融合，在组合零样本学习（CZSL）任务上取得 SOTA。

**[PromptIQA: Boosting the Performance and Generalization for No-Reference Image Quality Assessment via Prompts](llm_nlp/promptiqa_boosting_the_performance_and_generalization_for_no-reference_image_qua.md)**

:   提出 PromptIQA，通过少量"图像-分数对"（ISP）作为 prompt 的方式，使 NR-IQA 模型训练完成后无需微调即可自适应适配新的质量评估需求，在 12 个数据集、5 类 IQA 任务上均达到 SOTA 性能和泛化能力。

**[Reprojection Errors as Prompts for Efficient Scene Coordinate Regression](llm_nlp/reprojection_errors_as_prompts_for_efficient_scene_coordinate_regression.md)**

:   本文提出 EGFS（Error-Guided Feature Selection）机制，利用低重投影误差区域作为 SAM 的 point prompts 扩展为语义掩码，迭代地筛选可靠训练样本，在 Cambridge Landmarks 和 Indoor6 数据集上以更小模型和更少训练时间超越现有无 3D 信息依赖的 SCR 方法。

**[Rotary Position Embedding for Vision Transformer](llm_nlp/rotary_position_embedding_for_vision_transformer.md)**

:   系统研究将大语言模型中的旋转位置编码（RoPE）扩展到 2D 视觉 Transformer，提出 RoPE-Mixed（混合可学习频率）变体，在多分辨率分类、目标检测和语义分割上均带来显著且接近零额外计算的性能提升。

**[SIGMA: Sinkhorn-Guided Masked Video Modeling](llm_nlp/sigma_sinkhorn-guided_masked_video_modeling.md)**

:   本文提出 SIGMA，通过引入投影网络将 masked video modeling 的重建目标从像素级升级为可学习的深层特征聚类分配，利用 Sinkhorn 算法的最优传输实施高熵正则化避免坍缩，在 10 个数据集 3 个 benchmark 上全面超越 VideoMAE 等 SOTA 方法。

**[VisFocus: Prompt-Guided Vision Encoders for OCR-Free Dense Document Understanding](llm_nlp/visfocus_promptguided_vision_encoders_for_ocrfree_dense.md)**

:   提出 VisFocus，通过在视觉编码器的 patch merging 层引入 prompt 感知的 ViLMA 层，并设计 LMPM 预训练任务，使 OCR-Free 文档理解模型能聚焦于与用户查询相关的文本区域，在多个文档 VQA 基准上达到同规模 SOTA。

**[When Do We Not Need Larger Vision Models?](llm_nlp/when_do_we_not_need_larger_vision_models.md)**

:   提出 Scaling on Scales (S2)，通过让预训练的冻结小模型在多个图像尺度上运行（而非增大模型参数），即可超越更大模型在分类、分割、深度估计、MLLM 和机器人操控等任务上的表现。

**[Zero-Shot Object Counting with Good Exemplars (VA-Count)](llm_nlp/zeroshot_object_counting_with_good_exemplars.md)**

:   提出 VA-Count，一种基于视觉关联的零样本物体计数框架，通过 Grounding DINO 驱动的样例增强模块和对比学习噪声抑制模块，为任意类别建立高质量样例与图像间的鲁棒视觉关联。

---

## 🎯 目标检测 { #object_detection }

**[A New Dataset and Framework for Real-World Blurred Images Super-Resolution](object_detection/a_new_dataset_and_framework_for_real-world_blurred_images_super-resolution.md)**

:   针对现有盲超分方法在处理含模糊（散焦/运动模糊）图像时过度纹理化、破坏模糊区域感知质量的问题，构建了包含近3000张模糊图像的ReBlurSR数据集，并提出PBaSR框架，通过双分支解耦训练（CDM）和基于权重插值的跨分支融合（CFM），在不增加任何推理开销的前提下，同时提升模糊图像和普通图像的超分效果，LPIPS提升0.02~0.10。

**[Adaptive Bounding Box Uncertainties via Two-Step Conformal Prediction](object_detection/adaptive_bounding_box_uncertainties_via_twostep_conformal_pr.md)**

:   提出两步共形预测框架为多类目标检测的边界框生成带理论覆盖率保证的自适应不确定性区间——第一步用共形分类集处理类别误判风险，第二步用集成/分位数回归等方法构建自适应于目标尺寸的边界框预测区间，在COCO/Cityscapes/BDD100k上达到约90%目标覆盖率且区间实际可用。

**[AFreeCA: Annotation-Free Counting for All](object_detection/afreeca_annotation-free_counting_for_all.md)**

:   利用 Stable Diffusion 生成合成排序/计数数据，通过先学排序再学计数的两阶段策略 + 密度引导的图像分块，实现了首个适用于任意类别物体的无标注计数方法，在人群计数上超越已有无监督方法。

**[AFreeCA: Annotation-Free Counting for All](object_detection/afreeca_annotationfree_counting_for_all.md)**

:   利用潜在扩散模型（LDM）生成合成计数和排序数据，提出首个可适用于任意物体类别的无监督计数方法，无需任何人工标注即可实现准确计数。

**[BAM-DETR: Boundary-Aligned Moment Detection Transformer for Temporal Sentence Grounding in Videos](object_detection/bam-detr_boundary-aligned_moment_detection_transformer_for_temporal_sentence_gro.md)**

:   提出边界对齐的时刻检测 Transformer（BAM-DETR），用 anchor-boundary 三元组 $(p, d_s, d_e)$ 替代传统的 center-length 二元组 $(c, l)$ 来建模时刻，配合双路径解码器和基于质量的排序机制，有效解决了中心模糊导致的定位不精确问题。

**[Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](object_detection/be_yourself_bounded_attention_for_multi-subject_text-to-image_generation.md)**

:   提出 Bounded Attention，一种无需训练的注意力约束方法，通过在去噪过程中限制 cross-attention 和 self-attention 的信息流动来解决多主体文本到图像生成中的语义泄漏问题。

**[Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](object_detection/be_yourself_bounded_attention_for_multisubject_texttoimage_g.md)**

:   Be Yourself深入分析了扩散模型中Cross-Attention和Self-Attention导致的多主体语义泄漏问题，提出Bounded Attention机制，通过在去噪过程中限制不同主体间的信息流动来生成语义独立的多主体图像，免训练即可生成5+个语义相似主体。

**[Bridge Past and Future: Overcoming Information Asymmetry in Incremental Object Detection](object_detection/bridge_past_and_future_overcoming_information_asymmetry_in_incremental_object_de.md)**

:   提出 Bridge Past and Future (BPF) 方法，通过伪标签桥接过去阶段、注意力机制排除未来潜在物体，并结合双教师蒸馏（Distillation with Future），解决增量目标检测中跨阶段信息不对称导致的优化目标不一致问题。

**[Can OOD Object Detectors Learn from Foundation Models?](object_detection/can_ood_object_detectors_learn_from_foundation_models.md)**

:   SyncOOD 提出一种自动化数据策展方法，利用 LLM 想象语义新颖的 OOD 概念，通过 Stable Diffusion Inpainting 在 ID 图像上进行区域级编辑合成场景级 OOD 样本，再经 SAM 精炼框和特征相似度过滤后训练轻量 MLP 分类器，在多个 OOD 检测基准上以极少量合成数据大幅超越 SOTA。

**[DAMSDet: Dynamic Adaptive Multispectral Detection Transformer](object_detection/damsdet_dynamic_adaptive_multispectral_detection_transformer_with_competitive_qu.md)**

:   DAMSDet 提出一种基于 DETR 架构的动态自适应红外-可见光目标检测方法，通过模态竞争 Query 选择（为每个目标动态选择主导模态特征作为初始 query）和多光谱可变形交叉注意力（在多语义层级上自适应采样和聚合双模态特征），同时解决互补信息融合和模态未对齐两大挑战，在 4 个公开数据集上显著超越 SOTA。

**[Efficient Inference of Vision Instruction-Following Models with Elastic Cache](object_detection/efficient_inference_of_vision_instruction-following_models_with_elastic_cache.md)**

:   Elastic Cache 提出一种针对多模态指令遵循模型的 KV Cache 管理方法，在指令编码阶段采用基于重要性的 cache 合并策略（而非丢弃），在输出生成阶段采用固定点淘汰策略，以"一个序列、两种策略"实现任意加速比的高效推理，在 KV Cache 预算仅 0.2 时实现 78% 的实际速度提升且保持生成质量。

**[GRA: Detecting Oriented Objects Through Group-Wise Rotating and Attention](object_detection/gra_detecting_oriented_objects_through_group-wise_rotating_and_attention.md)**

:   提出轻量级的 Group-wise Rotating and Attention (GRA) 模块，通过将卷积核分组旋转并施加分组空间注意力，在参数量减少近 50% 的同时超越了此前 SOTA 方法 ARC，在 DOTA-v2.0 上取得新的最优性能。

**[LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer](object_detection/layoutdetr_detection_transformer_is_a_good_multimodal_layout.md)**

:   将版式设计问题重新构建为基于背景图像的目标检测问题，提出LayoutDETR框架，利用DETR的transformer编解码器结构结合GAN/VAE生成先验，以多模态前景元素（图像+文本）为输入，生成考虑背景语义的排版布局，在公开基准和自建广告横幅数据集上均达到SOTA。

**[Towards Natural Language-Guided Drones: GeoText-1652 Benchmark with Spatial Relation Matching](object_detection/towards_natural_languageguided_drones_geotext1652_bench.md)**

:   构建 GeoText-1652 多视角自然语言引导地理定位基准数据集（276K text-bbox 对），提出利用区域级空间关系匹配（grounding loss + spatial loss）进行精细化文本-图像跨模态检索的方法，实现自然语言控制无人机导航。

**[Tracking Meets LoRA: Faster Training, Larger Model, Stronger Performance](object_detection/tracking_meets_lora_faster_training_larger_model_strong.md)**

:   首次将 LoRA 引入视觉目标跟踪领域，通过解耦位置编码和设计 MLP-only 头网络，使大规模 ViT 模型（最大 ViT-g）在实验室级资源下实现高效训练和 SOTA 跟踪性能。

---

## 🎬 视频理解 { #video_understanding }

**[ActionSwitch: Class-agnostic Detection of Simultaneous Actions in Streaming Videos](video_understanding/actionswitch_class-agnostic_detection_of_simultaneous_actions_in_streaming_video.md)**

:   提出 ActionSwitch——首个无需类别信息即可检测流式视频中重叠动作实例的在线时序动作定位（On-TAL）框架，核心将多动作检测建模为有限状态机的状态分类问题，并辅以 conservativeness loss 减少碎片化误检，在 THUMOS14、FineAction、Epic-Kitchens 100 等数据集上在 OAD 扩展方法中达到 SOTA。

**[Adapt2Reward: Adapting Video-Language Models to Generalizable Robotic Rewards via Failure Prompts](video_understanding/adapt2reward_adapting_videolanguage_models_to_generalizable.md)**

:   提出 Adapt2Reward，通过可学习的失败提示（failure prompts）将预训练视频语言模型适配为可泛化的语言条件奖励函数，仅需少量单一环境的机器人数据即可泛化到新环境和新任务，在 MetaWorld 上比前方法高出约 28%。

**[AMEGO: Active Memory from Long EGOcentric Videos](video_understanding/amego_active_memory_from_long_egocentric_videos.md)**

:   提出 AMEGO，一种从长第一人称视频中在线构建结构化"活跃记忆"的方法，通过 HOI tracklet + 位置分段 + 语义无关的视觉查询，在新提出的 AMB benchmark 上超越 Video QA baselines 12.7%。

**[Benchmarks and Challenges in Pose Estimation for Egocentric Hand Interactions with Objects](video_understanding/benchmarks_and_challenges_in_pose_estimation_for_egocentric_hand_interactions_wi.md)**

:   基于 HANDS23 挑战赛（AssemblyHands + ARCTIC 数据集），系统性地对第一人称视角下手-物体交互的 3D 姿态估计方法进行了基准测试和深入分析，揭示了畸变校正、高容量 Transformer 和多视角融合的有效性，以及快速运动、遮挡和窄视角下物体重建等仍未解决的挑战。

**[BlazeBVD: Make Scale-Time Equalization Great Again for Blind Video Deflickering](video_understanding/blazebvd_make_scale-time_equalization_great_again_for_blind_video_deflickering.md)**

:   提出 BlazeBVD，利用经典 Scale-Time Equalization (STE) 在光照直方图空间提取 deflickering 先验（滤波光照图、曝光图、闪烁帧索引），将复杂的视频时空学习简化为 2D 空间网络逐帧处理 + 轻量 3D 时序一致性网络，在盲视频去闪烁任务上实现 SOTA 质量且推理速度比基线快 10 倍以上。

**[Classification Matters: Improving Video Action Detection with Class-Specific Attention](video_understanding/classification_matters_improving_video_action_detection_with_class-specific_atte.md)**

:   提出类别专属查询（class queries）机制，通过为每个动作类别分配独立的可学习查询，让模型动态关注与各类别相关的上下文区域，显著提升视频动作检测中的分类性能。

**[CrossGLG: LLM Guides One-Shot Skeleton-Based 3D Action Recognition in a Cross-Level Manner](video_understanding/crossglg_llm_guides_one-shot_skeleton-based_3d_action_recognition_in_a_cross-lev.md)**

:   提出CrossGLG框架，利用LLM生成的文本描述以"全局→局部→全局"的方式引导骨架特征学习，在单样本3D动作识别中以仅2.8%的SOTA模型参数量大幅超越对手。

**[Data Collection-Free Masked Video Modeling](video_understanding/data_collection-free_masked_video_modeling.md)**

:   提出基于伪运动生成器（PMG）从静态图像递归生成伪运动视频，结合掩码视频建模（VideoMAE）进行自监督预训练，完全摆脱真实视频数据的采集成本和隐私/版权顾虑，甚至可用合成图像实现有效的视频Transformer预训练。

**[DINO-Tracker: Taming DINO for Self-Supervised Point Tracking in a Single Video](video_understanding/dino-tracker_taming_dino_for_self-supervised_point_tracking_in_a_single_video.md)**

:   提出DINO-Tracker，将预训练DINOv2的语义特征与测试时单视频优化相结合，通过Delta-DINO残差微调和多源自监督损失实现长程稠密点追踪，在自监督方法中达到SOTA且可媲美有监督追踪器，尤其在长期遮挡场景中大幅领先。

**[Elysium: Exploring Object-Level Perception in Videos via MLLM](video_understanding/elysium_exploring_objectlevel_perception_in_videos_via_mllm.md)**

:   提出Elysium，首个端到端可训练的多模态大语言模型系统化处理视频目标级任务（如目标跟踪），构建了百万级ElysiumTrack-1M视频数据集支持SOT/RSOT/Video-REG三类任务，并设计T-Selector token压缩网络在保持性能的同时大幅减少视觉token消耗。

**[Nymeria: A Massive Collection of Multimodal Egocentric Daily Motion in the Wild](video_understanding/nymeria_a_massive_collection_of_multimodal_egocentric_daily_.md)**

:   Nymeria是全球最大野外人体运动数据集，300h/264人多设备多模态自我中心数据和310.5K句语言描述。

**[On the Utility of 3D Hand Poses for Action Recognition](video_understanding/on_the_utility_of_3d_hand_poses_for_action_recognition.md)**

:   提出 HandFormer，一种轻量级多模态 Transformer，将密集采样的 3D 手部姿态（捕捉细粒度动作）与稀疏采样的 RGB 帧（提供场景语义）结合，通过 micro-action 时序分解和 trajectory 编码高效建模手-物交互，在 Assembly101 和 H2O 上达到 SOTA，且纯 pose 模型以 5× 更少 FLOPs 超越已有骨架方法。

**[PiTe: Pixel-Temporal Alignment for Large Video-Language Model](video_understanding/pite_pixeltemporal_alignment_for_large_videolanguage_mo.md)**

:   提出 PiTe，一种通过物体轨迹引导的像素-时序对齐方法，利用自动构建的 PiTe-143K 数据集在空间和时间维度上实现视频与语言的精细对齐，显著提升视频理解能力。

**[R²-Tuning: Efficient Image-to-Video Transfer Learning for Video Temporal Grounding](video_understanding/r2tuning_efficient_imagetovideo_transfer_learning_for_video.md)**

:   R²-Tuning提出了一个仅需1.5%参数的轻量R²Block，通过从CLIP后层向前层的逆向递归方式聚合多层空间特征并精化时序关联，在6个VTG基准上以2.7M参数超越了使用额外时序骨干的4倍大方法。

---

## 🏥 医学图像 { #medical_imaging }

**[Adaptive Correspondence Scoring for Unsupervised Medical Image Registration](medical_imaging/adaptive_correspondence_scoring_for_unsupervised_medical_ima.md)**

:   针对医学图像无监督配准中噪声、遮挡等干扰因素导致的虚假重建误差问题，提出了一个自适应对应关系评分框架（AdaCS），通过学习像素级的对应置信度图来重新加权误差残差，以即插即用方式一致提升三种主流配准架构在三个数据集上的性能。

**[Alternate Diverse Teaching for Semi-supervised Medical Image Segmentation](medical_imaging/alternate_diverse_teaching_for_semi-supervised_medical_image_segmentation.md)**

:   提出 AD-MT（Alternate Diverse Mean Teacher），通过随机周期性交替更新两个教师模型 + 基于熵的冲突调和策略，在半监督医学分割中解决 confirmation bias 问题，在 ACDC/LA/Pancreas 上全面超越 SOTA。

**[Architecture-Agnostic Untrained Network Priors for Image Reconstruction with Frequency Regularization](medical_imaging/architecture-agnostic_untrained_network_priors_for_image_reconstruction_with_fre.md)**

:   提出三种与架构无关的频率正则化技术（带宽受限输入、带宽可控上采样、Lipschitz 正则化卷积层），统一解决 untrained network prior 的架构敏感性、过拟合和运行效率问题，在 MRI 重建任务中显著缩小不同架构间的性能差距。

**[CardiacNet: Learning to Reconstruct Abnormalities for Cardiac Disease Assessment from Echocardiogram Videos](medical_imaging/cardiacnet_learning_to_reconstruct_abnormalities_for_cardiac_disease_assessment_.md)**

:   提出基于重建的心脏疾病评估框架 CardiacNet，通过 Consistency Deformation Codebook (CDC) 和 Consistency Deformation Discriminator (CDD) 学习正常与异常心脏超声视频之间的结构和运动差异，在射血分数预测、肺动脉高压和房间隔缺损分类三个任务上达到 SOTA。

**[Chameleon: A Data-Efficient Generalist for Dense Visual Prediction in the Wild](medical_imaging/chameleon_a_data-efficient_generalist_for_dense_visual_prediction_in_the_wild.md)**

:   提出 Chameleon，一个基于 meta-learning 和 token matching 的数据高效视觉通才模型，仅需几十张标注图像即可适应全新的密集预测任务（包括医学图像、视频、3D 等），在六个下游基准上显著超越现有通才方法。

**[GTP-4o: Modality-Prompted Heterogeneous Graph Learning for Omni-modal Biomedical Representation](medical_imaging/gtp4o_modalityprompted_heterogeneous_graph_learning_for.md)**

:   提出 GTP-4o，一种基于模态提示的异构图学习框架，通过异构图嵌入、图提示补全缺失模态、知识引导的层级聚合，实现基因组学-病理图像-细胞图-文本等多种临床模态的统一表示学习。

**[Improving Medical Multi-modal Contrastive Learning with Expert Annotations](medical_imaging/improving_medical_multimodal_contrastive_learning_with_exper.md)**

:   提出eCLIP，通过引入放射科医生的眼动热力图（eye-gaze heatmap）作为专家标注，利用热力图处理器和mixup增强策略扩充高质量正样本对，有效缓解医学CLIP中的"模态间隙"问题，在零样本推理、线性探测、跨模态检索和RAG报告生成等任务上取得一致性提升。

**[Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification](medical_imaging/pathologyknowledge_enhanced_multiinstance_prompt_learni.md)**

:   提出 PEMP——病理知识增强的多实例提示学习框架，将视觉和文本病理先验（典型 patch/slide 示例 + 语言描述）注入 CLIP 的提示中，在 patch 和 slide 两个层级进行对比学习，显著提升少样本全切片图像（WSI）分类性能。

**[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](medical_imaging/textttnephi_neural_deformation_fields_for_approximately_diff.md)**

:   NePhi用隐式神经网络（SIREN）替代传统的体素化形变场来表示配准变换，通过编码器预测latent code + 可选的测试时优化实现快速且近似微分同胚的医学图像配准，在多分辨率设置下与SOTA精度相当但内存降低5倍。

**[TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data](medical_imaging/tip_tabularimage_pretraining_for_multimodal_classification_w.md)**

:   提出TIP框架，通过掩码表格重建、图像-表格匹配和对比学习三个自监督任务，在表格数据不完整的条件下学习鲁棒的多模态表示，在自然图像和医学图像分类任务上超越现有方法。

---

## 🛡️ AI 安全 { #ai_safety }

**[Any Target Can Be Offense: Adversarial Example Generation via Generalized Latent Infection](ai_safety/any_target_can_be_offense_adversarial_example_generation_via_generalized_latent_.md)**

:   提出 GAKer，首个可泛化到未知目标类别的定向对抗攻击生成器，通过在 UNet 中间层注入目标特征（latent infection）+ 余弦距离损失替代交叉熵实现类别无关训练，在未知类上的攻击成功率比 HGN 高 14.13%。

**[CLIP-Guided Generative Networks for Transferable Targeted Adversarial Attacks](ai_safety/clip-guided_generative_networks_for_transferable_targeted_adversarial_attacks.md)**

:   提出 CGNC，利用 CLIP 文本编码器为条件生成网络注入目标类别语义信息，结合交叉注意力模块和 masked fine-tuning，大幅提升多目标/单目标定向对抗攻击的黑盒迁移成功率。

**[Event Trojan: Asynchronous Event-Based Backdoor Attacks](ai_safety/event_trojan_asynchronous_event-based_backdoor_attacks.md)**

:   提出 Event Trojan 框架，首次研究直接在异步事件数据流中注入后门触发器（immutable trigger 和 mutable trigger），揭示了事件相机视觉任务面临的后门攻击安全风险。

**[Event Trojan: Asynchronous Event-based Backdoor Attacks](ai_safety/genq_quantization_in_low_data_regimes_with_generative_synthetic_data.md)**

:   提出 Event Trojan 框架，首次针对异步事件数据流设计后门攻击方法，包含不可变触发器和可变触发器两种模式，直接在事件流层面注入恶意事件实现隐蔽高效的后门攻击。

**[Preventing Catastrophic Overfitting In Fast Adversarial Training A Bi-Level Opti](ai_safety/preventing_catastrophic_overfitting_in_fast_adversarial_training_a_bi-level_opti.md)**

:   从双层优化视角分析快速对抗训练中灾难性过拟合的成因，提出 FGSM-PCO 方法，通过自适应融合历史与当前对抗样本并配合定制正则化损失，有效防止并纠正内层优化崩溃。

**[Resilience of Entropy Model in Distributed Neural Networks](ai_safety/resilience_of_entropy_model_in_distributed_neural_networks.md)**

:   首次系统研究分布式 DNN 中熵编码模型在有意干扰（对抗攻击）和无意干扰（天气变化、运动模糊等）下的鲁棒性，发现熵模型学习的压缩特征与分类特征截然不同，并提出基于目标感知全变差去噪的防御方法，可将攻击后的传输开销降低至低于干净数据水平，准确率仅下降约 2%。

**[SkyMask: Attack-Agnostic Robust Federated Learning with Fine-Grained Learnable Masks](ai_safety/skymask_attack-agnostic_robust_federated_learning_with_fine-grained_learnable_ma.md)**

:   提出 SkyMask，利用参数级可学习二值掩码在服务器端检测恶意客户端模型更新，实现攻击无关的鲁棒联邦学习，在恶意客户端占比高达 80% 时仍能有效防御。

**[Towards Multi-modal Transformers in Federated Learning](ai_safety/towards_multi-modal_transformers_in_federated_learning.md)**

:   提出 FedCola 框架，通过互补本地训练和协作聚合两个策略，在联邦学习中实现多模态 Transformer 的跨模态知识迁移，无需公共数据即可弥合单模态与多模态客户端之间的差距。

**[Towards Multi-modal Transformers in Federated Learning](ai_safety/towards_multimodal_transformers_in_federated_learning.md)**

:   首次探索Transformer架构在转移式多模态联邦学习中的应用，提出FedCola框架，通过互补式本地训练（利用跨模态Transformer blocks）和协作式服务器聚合（选择性聚合self-attention层），在保护数据隐私的前提下有效训练多模态Transformer。

---

## 🎵 音频/语音 { #audio_speech }

**[Beat-It: Beat-Synchronized Multi-Condition 3D Dance Generation](audio_speech/beat-it_beat-synchronized_multi-condition_3d_dance_generation.md)**

:   提出 Beat-It 框架，通过将节拍条件从音乐中解耦并设计层次化多条件融合机制，实现了节拍同步且关键帧可控的 3D 舞蹈生成，在 AIST++ 上大幅领先现有方法。

**[CoLeaF: A Contrastive-Collaborative Learning Framework for Weakly Supervised Audio-Visual Video Parsing](audio_speech/coleaf_a_contrastive-collaborative_learning_framework_for_weakly_supervised_audi.md)**

:   提出 CoLeaF 双分支学习框架，通过事件感知对比学习显式优化跨模态上下文的整合，在弱监督音视频解析任务上平均提升 1.9% F-score。

**[ControlLLM: Augment Language Models with Tools by Searching on Graphs](audio_speech/controlllm_augment_language_models_with_tools.md)**

:   提出 ControlLLM 框架，通过任务分解、Thoughts-on-Graph (ToG) 图搜索范式和执行引擎三大组件，让 LLM 在预构建的工具图上搜索最优解决方案路径，准确高效地调用多模态工具完成复杂任务，在困难任务上达到 93% 的解决方案成功率。

**[ControlLLM: Augment Language Models with Tools by Searching on Graphs](audio_speech/controlllm_augment_language_models_with_tools_by_searching_on_graphs.md)**

:   提出 ControlLLM 框架，通过在预构建的工具图（Tool Graph）上进行图搜索（Thoughts-on-Graph）来规划多模态工具调用，显著提升了复杂任务中工具选择和参数赋值的准确性。

**[EDTalk: Efficient Disentanglement for Emotional Talking Head Synthesis](audio_speech/edtalk_efficient_disentanglement_for_emotional_talking_head_synthesis.md)**

:   提出基于正交可学习基向量的高效解耦框架 EDTalk，将人脸动态分解为嘴型、头部姿态和情感表情三个独立潜空间，同时支持视频驱动和音频驱动的情感说话人头像生成。

**[Label-Anticipated Event Disentanglement for Audio-Visual Video Parsing](audio_speech/label-anticipated_event_disentanglement_for_audio-visual_video_parsing.md)**

:   提出 LEAP（Label semantic-based Projection）解码范式，利用事件类别的标签文本嵌入作为语义锚点，通过跨模态注意力机制将音频/视觉隐特征中潜在重叠的事件语义解耦到独立的标签嵌入中，配合基于 EIoU 的音视觉语义相似度损失，在 AVVP 任务上取得 SOTA。

**[Latent-INR: A Flexible Framework for Implicit Representations of Videos with Discriminative Semantics](audio_speech/latent-inr_a_flexible_framework_for_implicit_representations_of_videos_with_disc.md)**

:   提出 Latent-INR 框架，通过为视频每帧学习一个隐式 latent code 并结合 hypernetwork 进行低秩权重调制，将视频 INR 的空间与时间建模解耦，在保持压缩性能的同时赋予表征语义判别能力，支持检索、视频插帧和任意分辨率推理等多种下游任务。

---

## 🤖 机器人/具身智能 { #robotics }

**[AFF-ttention! Affordances and Attention models for Short-Term Object Interaction Anticipation](robotics/aff-ttention_affordances_and_attention_models_for_short-term_object_interaction_.md)**

:   提出 STAformer 架构和两个基于 affordance 的模块（环境 affordance 数据库 + 交互热点），将第一人称视频中的短期物体交互预测（STA）在 Ego4D 和 EPIC-Kitchens 上提升了 30-45% 的相对性能。

**[DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-Level Control](robotics/disco_embodied_navigation_and_interaction.md)**

:   提出 DISCO，通过可微分场景语义表征（包含物体和 affordance）实现动态场景建模，结合全局-局部双层粗到细控制策略实现高效移动操作，在 ALFRED benchmark 的 unseen scenes 上以 +8.6% 成功率超越使用分步指令的 SOTA，且无需分步指令。

**[DISCO: Embodied Navigation and Interaction via Differentiable Scene Semantics and Dual-Level Control](robotics/disco_embodied_navigation_and_interaction_via_differentiable_scene_semantics_and.md)**

:   提出 DISCO 框架，通过可微分场景语义表示和双层粗-细动作控制，在 ALFRED 基准上实现具身导航与交互的显著性能提升（未见场景成功率超越 SOTA +8.6%，且无需逐步指令）。

**[Hierarchically Structured Neural Bones for Reconstructing Animatable Objects from Casual Videos](robotics/hierarchically_structured_neural_bones_for_reconstructing_animatable_objects_fro.md)**

:   提出层次化神经骨骼（Hierarchical Neural Bones）框架，通过树状结构的骨骼系统以粗到细的方式分解物体运动，从随手拍摄的视频中重建可操控的高质量 3D 模型。

**[Prioritized Semantic Learning for Zero-Shot Instance Navigation](robotics/prioritized_semantic_learning_for_zeroshot_instance_navigation.md)**

:   提出 Prioritized Semantic Learning (PSL) 方法，通过语义感知智能体架构、优先语义训练策略和语义扩展推理方案，显著提升导航智能体的语义感知能力，在零样本 ObjectNav 上超越 SOTA  66%（SR），并提出了更具挑战性的 InstanceNav 任务。

**[See and Think: Embodied Agent in Virtual Environment](robotics/see_and_think_embodied_agent_in_virtual_environment.md)**

:   提出 STEVE，一个基于视觉感知、语言指令和代码动作三大组件的 Minecraft 开放世界具身智能体，通过 STEVE-21K 数据集微调 LLaMA-2 并结合视觉编码器和技能数据库，在科技树解锁和方块搜索任务上大幅超越现有方法。

**[SemGrasp: Semantic Grasp Generation via Language Aligned Discretization](robotics/semgrasp_semantic_grasp_generation_via_language_aligned.md)**

:   提出 SemGrasp，通过层次化 VQ-VAE 将抓取姿态离散化为三个语义对齐的 token（方向/方式/精修），并微调多模态大语言模型实现基于语言指令的语义抓取生成。

---

## 📦 模型压缩 { #model_compression }

**[A Simple Low-bit Quantization Framework for Video Snapshot Compressive Imaging](model_compression/a_simple_lowbit_quantization_framework_for_video_snapshot_co.md)**

:   首个面向视频快照压缩成像（Video SCI）重建任务的低比特量化框架Q-SCI，通过高质量特征提取模块、精确视频重建模块和Transformer分支的query/key分布偏移操作，在4-bit量化下实现7.8倍理论加速且性能仅下降2.3%。

**[Adaptive Compressed Sensing with Diffusion-Based Posterior Sampling](model_compression/adaptive_compressed_sensing_with_diffusionbased_posterior_sa.md)**

:   提出AdaSense，利用预训练扩散模型的零样本后验采样来量化重建不确定性，从而自适应地选择最优测量矩阵，无需额外训练即可在人脸图像、MRI和CT等多领域实现优于非自适应方法的压缩感知重建。

**[Adaptive Selection of Sampling-Reconstruction in Fourier Compressed Sensing](model_compression/adaptive_selection_of_samplingreconstruction_in_fourier_comp.md)**

:   提出ℋ1.5框架：为每个输入数据自适应选择最佳采样mask-重建网络对（J=3对），利用超分辨率空间生成模型量化高频贝叶斯不确定性来决定采样策略，理论证明优于联合优化ℋ1（非自适应）和自适应采样ℋ2（Pareto次优）。

**[Anytime Continual Learning for Open Vocabulary Classification](model_compression/anytime_continual_learning_for_open_vocabulary_classification.md)**

:   提出 AnytimeCL 框架，通过部分微调 CLIP 最后一个 transformer block 并动态加权融合微调模型与原始模型的预测，实现任意时刻接收样本、任意标签集推理的开放词汇持续学习。

**[Bidirectional Stereo Image Compression with Cross-Dimensional Entropy Model](model_compression/bidirectional_stereo_image_compression_with_cross-dimensional_entropy_model.md)**

:   提出双向对称的立体图像压缩框架 BiSIC，采用 3D 卷积联合编解码器和跨维度熵模型，在 PSNR 和 MS-SSIM 上均超越传统标准和已有学习方法，同时消除了单向方法中左右视图压缩质量不平衡的问题。

**[Category Adaptation Meets Projected Distillation in Generalized Continual Category Discovery](model_compression/category_adaptation_meets_projected_distillation_in_generalized_continual_catego.md)**

:   提出 CAMP 方法，通过可学习投影器蒸馏与类别中心适应网络的协同组合，在广义持续类别发现（GCCD）场景中显著提升了新类别学习与旧知识保持之间的平衡。

---

## 🕸️ 图学习 { #graph_learning }

**[Confidence Self-Calibration for Multi-Label Class-Incremental Learning](graph_learning/confidence_self-calibration_for_multi-label_class-incremental_learning.md)**

:   针对多标签类增量学习(MLCIL)中部分标签导致的过度自信预测和假阳性错误问题，提出 Confidence Self-Calibration (CSC) 框架，通过类增量图卷积网络(CI-GCN)校准标签关系 + 最大熵正则化校准置信度，在 MS-COCO 和 VOC 上大幅超越 SOTA。

**[Fine-Grained Scene Graph Generation via Sample-Level Bias Prediction](graph_learning/fine-grained_scene_graph_generation_via_sample-level_bias_prediction.md)**

:   提出样本级偏置预测方法 SBP，通过 Bias-Oriented GAN 利用物体对 union region 的上下文信息预测样本特异性纠偏向量，将粗粒度关系修正为细粒度关系，在 VG/GQA/VG-1800 上相比数据集级纠偏方法平均提升 5.6%/3.9%/3.2% 的 Average@K。

**[GKGNet: Group K-Nearest Neighbor Based Graph Convolutional Network for Multi-Label Image Recognition](graph_learning/gkgnet_group_k-nearest_neighbor_based_graph_convolutional_network_for_multi-labe.md)**

:   提出首个全图卷积多标签识别模型 GKGNet，通过 Group KNN 机制动态构建标签与图像区域间的图结构，在 MS-COCO 和 VOC2007 上以更低计算量取得 SOTA。

**[SENC: Handling Self-collision in Neural Cloth Simulation](graph_learning/senc_handling_self-collision_in_neural_cloth_simulation.md)**

:   提出 SENC，通过基于 Global Intersection Analysis (GIA) 的自碰撞损失和自碰撞感知图神经网络，首次在自监督神经布料模拟中有效解决布料自碰撞问题。

---

## 🎮 强化学习 { #reinforcement_learning }

**[AdaGlimpse: Active Visual Exploration with Arbitrary Glimpse Position and Scale](reinforcement_learning/adaglimpse_active_visual_exploration_with_arbitrary_glimpse_position_and_scale.md)**

:   提出AdaGlimpse，利用Soft Actor-Critic强化学习从连续动作空间中选择任意位置和尺度的glimpse，结合弹性位置编码的ViT编码器实现多任务（重建/分类/分割）的主动视觉探索，以仅6%像素超越了使用18%像素的SOTA方法。

**[Octopus: Embodied Vision-Language Programmer from Environmental Feedback](reinforcement_learning/octopus_embodied_vision-language_programmer_from_environmental_feedback.md)**

:   提出 Octopus，一个具身视觉-语言编程模型，通过生成可执行代码来连接高层规划与底层操控，并引入 Reinforcement Learning with Environmental Feedback (RLEF) 训练方案来提升决策质量。

**[Octopus: Embodied Vision-Language Programmer from Environmental Feedback](reinforcement_learning/octopus_embodied_visionlanguage_programmer_from_environmental_feedback.md)**

:   Octopus 是一个具身视觉-语言编程模型，通过将 VLM 与可执行代码生成相结合，利用 GPT-4 收集训练数据并引入 RLEF（环境反馈强化学习）进行微调，在三个不同模拟器（OmniGibson、Minecraft、GTA-V）中实现了端到端的视觉感知→计划→代码生成→执行闭环。

**[Visual Grounding for Object-Level Generalization in Reinforcement Learning](reinforcement_learning/visual_grounding_for_object-level_generalization_in_reinforcement_learning.md)**

:   利用视觉语言模型 (MineCLIP) 的 visual grounding 能力生成目标物体的 confidence map，通过奖励设计和任务表征两条路径将 VLM 知识迁移到强化学习中，实现对未见物体和指令的零样本泛化。

---

## 💡 LLM 推理 { #llm_reasoning }

**[Controllable Navigation Instruction Generation with Chain of Thought Prompting](llm_reasoning/controllable_navigation_instruction_generation.md)**

:   提出 C-Instructor，利用 Chain-of-Thought with Landmarks (CoTL) 机制引导 LLM 先识别关键地标再生成指令，结合空间拓扑建模任务 (STMT) 和风格混合训练 (SMT)，实现风格可控和内容可控的导航指令生成，在四个室内外 benchmark 上全面超越 SOTA。

**[Controllable Navigation Instruction Generation with Chain of Thought Prompting](llm_reasoning/controllable_navigation_instruction_generation_with_chain_of_thought_prompting.md)**

:   提出 C-Instructor，利用 LLM 的思维链提示实现风格和内容可控的导航指令生成，通过 CoTL（带地标的思维链）、STMT（空间拓扑建模）和 SMT（混合风格训练）三大机制，在四个室内外导航数据集上全面超越已有方法。

**[RoadPainter: Points Are Ideal Navigators for Topology Transformer](llm_reasoning/roadpainter_points_are_ideal_navigators_for_topology_transformer.md)**

:   提出 RoadPainter，通过先回归车道中心线点再利用实例 mask 精炼的两阶段策略，结合混合注意力机制和真实-虚拟车道分离策略，在 OpenLane-V2 数据集上实现 SOTA 的拓扑推理性能。

---

## 🔄 自监督/表示学习 { #self_supervised }

**[Adaptive Multi-head Contrastive Learning](self_supervised/adaptive_multihead_contrastive_learning.md)**

:   AMCL提出使用多个投影头（各自产生不同特征）+ 对每个样本对和每个头自适应学习温度参数，从最大似然估计推导出损失函数，作为通用插件在SimCLR/MoCo/Barlow Twins/CAN/LGP上一致提升1-5%性能。

**[COHO: Context-Sensitive City-Scale Hierarchical Urban Layout Generation](self_supervised/coho_context-sensitive_city-scale_hierarchical_urban_layout_generation.md)**

:   提出基于图掩码自编码器 (GMAE) 的城市级 2.5D 布局生成方法，通过规范图表示捕获建筑-街区-社区的多层语义上下文，结合优先级调度的迭代采样，在 330 个美国城市上实现了兼具真实感、语义一致性和正确性的大规模城市布局生成。

**[Distribution-Aware Robust Learning from Long-Tailed Data with Noisy Labels](self_supervised/distribution-aware_robust_learning_from_long-tailed_data_with_noisy_labels.md)**

:   提出 DaSC 框架，通过分布感知的类中心估计（DaCC）和置信度感知的对比学习（SBCL + MIDL），同时解决长尾分布和噪声标签的联合问题，在 CIFAR 和真实噪声数据集上达到 SOTA。

---

## 🖼️ 图像恢复 { #image_restoration }

**[Accelerating Image Super-Resolution Networks with Pixel-Level Classification](image_restoration/accelerating_image_super-resolution_networks_with_pixel-level_classification.md)**

:   提出PCSR——首个像素级计算资源分配的超分方法，用轻量MLP分类器逐像素判断恢复难度并分配到不同容量的上采样器，在PSNR几乎不掉的情况下将FLOPs压低至原始模型的18%~57%，大幅优于现有patch级方法ClassSR和ARM。

**[Asymmetric Mask Scheme for Self-supervised Real Image Denoising](image_restoration/asymmetric_mask_scheme_for_self-supervised_real_image_denoising.md)**

:   提出非对称掩码方案 AMSNet，训练时用单掩码、推理时用多掩码互补，突破了 blind spot network 对网络感受野的结构限制，在真实图像自监督去噪任务上取得 SOTA。

---

## 🦾 LLM Agent { #llm_agent }

**[Agent3D-Zero: An Agent for Zero-shot 3D Understanding](llm_agent/agent3d-zero_an_agent_for_zero-shot_3d_understanding.md)**

:   Agent3D-Zero 提出一个基于 VLM 的零样本 3D 场景理解 Agent 框架，通过鸟瞰图上的 Set-of-Line 视觉提示引导 VLM 主动选择观察视角，并综合多视角图像进行 3D 推理，在 ScanQA 等任务上超越了需要微调的 3D-LLM 方法。

**[HYDRA: A Hyper Agent for Dynamic Compositional Visual Reasoning](llm_agent/hydra_a_hyper_agent_for_dynamic_compositional_visual_reasoning.md)**

:   （注：基于摘要的简要笔记）提出 HYDRA，一种多阶段动态组合式视觉推理框架，通过规划器（Planner）、强化学习认知控制器（RL Agent）和推理器（Reasoner）三模块协作，实现可靠且渐进式的视觉推理，在 RefCOCO/RefCOCO+、OK-VQA、GQA 等多个数据集上取得 SOTA。

---

## 🛰️ 遥感 { #remote_sensing }

**[Adapting Fine-Grained Cross-View Localization to Areas without Fine Ground Truth](remote_sensing/adapting_fine-grained_cross-view_localization_to_areas_without_fine_ground_truth.md)**

:   针对细粒度跨视角定位模型在新区域部署时精度下降的问题，提出基于知识自蒸馏的弱监督学习方法——通过模式化伪GT生成、粗粒度监督和离群值过滤三个策略，仅使用目标区域的地面-航拍图像对（无需精确GT），即可在VIGOR和KITTI上将定位误差降低12%~20%。

**[ConGeo: Robust Cross-View Geo-Localization Across Ground View Variations](remote_sensing/congeo_robust_cross-view_geo-localization_across_ground_view_variations.md)**

:   提出 ConGeo，一种模型无关的单视图+跨视图对比学习框架，通过强制同一地点不同地面视角变体之间的特征一致性，使单一模型即可在任意朝向和任意视场角(FoV)下实现鲁棒的跨视图地理定位。

---

## 📈 时间序列 { #time_series }

**[OmniSat: Self-Supervised Modality Fusion for Earth Observation](time_series/omnisat_self-supervised_modality_fusion_for_earth_observation.md)**

:   提出OmniSat统一框架，通过模态特异编码器+跨模态对比自监督预训练，将多光谱时序（S2）、SAR时序（S1）、高分辨率单时相（SPOT/Aerial）等异构遥感数据融合为统一表示，在语义分割和作物分类上超越所有单模态和多模态基线。

**[Semantically Guided Representation Learning For Action Anticipation](time_series/semantically_guided_representation_learning_for_action_anticipation.md)**

:   提出 S-GEAR 框架，通过学习视觉动作原型并利用语言模型的语义关联来引导原型之间的几何关系，使模型理解动作间的语义互联性，从而提升动作预测性能，在 Epic-Kitchens 55/100、EGTEA Gaze+、50 Salads 四个基准上取得 SOTA 或极具竞争力的结果。

---

## 🔗 因果推理 { #causal_inference }

**[Distill Gold from Massive Ores: Bi-level Data Pruning towards Efficient Dataset Distillation](causal_inference/distill_gold_from_massive_ores_bi-level_data_pruning_towards_efficient_dataset_d.md)**

:   提出双层数据剪枝策略 BiLP，通过经验损失静态剪枝和基于因果效应 (ITE) 的动态剪枝，高效选择对数据集蒸馏最有价值的真实样本，以即插即用方式一致性提升现有蒸馏方法性能并降低计算开销。

---

## 🌍 地球科学 { #earth_science }

**[Semi-supervised Video Desnowing Network via Temporal Decoupling Experts and Distribution-Driven Contrastive Regularization](earth_science/semi-supervised_video_desnowing_network_via_temporal_decoupling_experts_and_dist.md)**

:   提出首个半监督视频去雪框架 SemiVDN，通过物理先验引导的时序解耦专家模块和分布驱动的对比正则化，利用无标签真实雪景视频缩小合成-真实域差距，在合成与真实数据集上均超越现有方法。

---

## ⚖️ 对齐 / RLHF { #llm_alignment }

**[Improving Intervention Efficacy via Concept Realignment in Concept Bottleneck Models](llm_alignment/improving_intervention_efficacy_via_concept_realignment_in_concept_bottleneck_mo.md)**

:   本文发现 Concept Bottleneck Models (CBMs) 中人工干预效率低下的原因在于干预时各概念独立处理、忽视了概念间关联，提出了一个轻量级的 Concept Intervention Realignment Module (CIRM)，在干预后自动重新对齐相关概念的预测值，将达到目标性能所需的干预次数最多减少 70%。

---

## 📐 优化/理论 { #optimization }

**[Handling the Non-smooth Challenge in Tensor SVD: A Multi-objective Tensor Recovery Framework](optimization/handling_the_non-smooth_challenge_in_tensor_svd_a_multi-objective_tensor_recover.md)**

:   提出基于可学习张量核范数的多目标张量恢复框架 (MOTC)，通过引入可学习酉矩阵替代固定变换来解决 t-SVD 方法在非光滑张量数据上的性能退化问题，并通过多目标优化有效利用张量各维度的低秩性。

---

## ⚛️ 物理学 { #physics }

**[Robust Fitting on a Gate Quantum Computer](physics/robust_fitting_on_a_gate_quantum_computer.md)**

:   首次在真实门量子计算机（IonQ Aria）上实现鲁棒拟合：提出用于一维 $\ell_\infty$ 可行性检验的量子电路，填补了 Bernstein-Vazirani（BV）电路计算 Boolean influence 的关键空缺，并展示如何将一维 influence 累积到高维非线性模型（如基础矩阵估计）。

---

## 🎁 推荐系统 { #recommender }

**[AID-AppEAL: Automatic Image Dataset and Algorithm for Content Appeal Enhancement and Assessment Labeling](recommender/aid-appeal_automatic_image_dataset_and_algorithm_for_content_appeal_enhancement_.md)**

:   首次提出图像内容吸引力评估（ICAA）任务，区别于传统美学评估（IAA），设计了一套自动化数据集生成 + 吸引力估计 + 吸引力增强的完整 pipeline，用 Stable Diffusion + Textual Inversion 实现零人工标注的大规模数据集构建。

---

## 📡 信号/通信 { #signal_comm }

**[PYRA: Parallel Yielding Re-Activation for Training-Inference Efficient Task Adaptation](signal_comm/pyra_parallel_yielding_re-activation_for_training-inference_efficient_task_adapt.md)**

:   提出PYRA方法同时实现训练高效和推理高效的任务适配，通过并行生成通道和token维度的自适应调制权重，在token合并前对特征进行re-activation校准，在ViT-L/16上1.7×加速仅掉0.1%精度、3×加速下消除"逆向压缩"现象。

---

## 📂 其他 { #others }

**[A Closer Look at GAN Priors: Exploiting Intermediate Features for Enhanced Model Inversion Attacks](others/a_closer_look_at_gan_priors_exploiting_intermediate_features.md)**

:   提出 IF-GMI，将预训练 StyleGAN2 的生成器拆解为多个 block，在中间特征层逐层优化（配合 $\ell_1$ 球约束防止图像崩塌），把模型反演攻击的搜索空间从潜码扩展到中间特征，在 OOD 场景下攻击准确率提升高达 38.8%。

**[A Framework for Efficient Model Evaluation through Stratification, Sampling, and Estimation](others/a_framework_for_efficient_model_evaluation_through_stratific.md)**

:   提出一个统计框架，通过分层（stratification）、采样设计（sampling）和估计器（estimation）三个组件的协同设计，在仅标注少量测试样本的情况下精确估计CV模型准确率，最高可实现10倍的效率增益（即用1/10的标注量达到同等精度）。

**[A High-Quality Robust Diffusion Framework for Corrupted Dataset](others/a_highquality_robust_diffusion_framework_for_corrupted_datas.md)**

:   提出 RDUOT 框架，首次将非平衡最优传输(UOT)融入扩散模型(DDGAN)中，通过学习 $q(x_0|x_t)$ 而非 $q(x_{t-1}|x_t)$ 来有效过滤训练数据中的离群值，在污染数据集上实现鲁棒生成的同时，在干净数据集上也超越了 DDGAN 基线。

**[ABC Easy as 123: A Blind Counter for Exemplar-Free Multi-Class Class-Agnostic Counting](others/abc_easy_as_123_a_blind_counter_for_exemplar-free_multi-class_class-agnostic_cou.md)**

:   提出首个无需样例图像即可同时计数图像中多类未知物体的方法ABC123，通过ViT回归多通道密度图+匈牙利匹配训练+SAM示例发现机制，在自建合成数据集MCAC上大幅超越需要样例的方法，且能泛化到FSC-147真实数据集。

**[Action2Sound: Ambient-Aware Generation of Action Sounds from Egocentric Videos](others/action2sound_ambientaware_generation_of_action_sounds_from_e.md)**

:   提出 AV-LDM，通过在训练时引入同一视频不同时间段的音频作为环境音条件，隐式解耦前景动作声和背景环境音，结合检索增强生成(RAG)在推理时选择合适的环境音条件，在 Ego4D 和 EPIC-KITCHENS 上大幅超越已有方法。

**[Active Generation for Image Classification](others/active_generation_for_image_classification.md)**

:   ActGen将主动学习思想引入扩散模型数据增强，通过识别分类器的错分样本并以注意力掩码引导+梯度对抗引导生成"难样本"，仅用10%的合成数据量即超越了此前需要近等量合成数据的方法，在ImageNet上ResNet-50获得+2.26%的精度提升。

**[Adaptive High-Frequency Transformer for Diverse Wildlife Re-Identification](others/adaptive_highfrequency_transformer_for_diverse_wildlife_reid.md)**

:   提出自适应高频Transformer（AdaFreq），通过频域混合增强、目标感知的高频token动态选择、特征均衡损失三大策略，将高频信息（毛皮纹理、轮廓边缘等）统一用于多种野生动物的重识别，在8个跨物种数据集上超越现有ReID方法。

**[Bidirectional Uncertainty-Based Active Learning For Open-Set Annotation](others/bidirectional_uncertainty-based_active_learning_for_open-set_annotation.md)**

:   提出 BUAL 框架，通过 Random Label Negative Learning 将未知类样本推向高置信区域、已知类样本推向低置信区域，结合双向不确定性采样策略，在开放集场景下有效选出高信息量的已知类样本。

**[Cross-Domain Learning for Video Anomaly Detection with Limited Supervision](others/cross-domain_learning_for_video_anomaly_detection_with_limited_supervision.md)**

:   提出弱监督跨域学习（CDL）框架，通过不确定性驱动的伪标签机制将无标注外部视频整合到训练中，显著提升视频异常检测的跨域泛化能力。

**[DC-Solver: Improving Predictor-Corrector Diffusion Sampler via Dynamic Compensation](others/dc-solver_improving_predictor-corrector_diffusion_sampler_via_dynamic_compensati.md)**

:   提出 DC-Solver，通过动态补偿（Dynamic Compensation）缓解 predictor-corrector 扩散采样器中的 misalignment 问题，仅需 10 个数据点即可优化补偿比率，并通过级联多项式回归（CPR）实现对未见 NFE/CFG 配置的即时泛化。

**[Teaching Tailored to Talent: Adverse Weather Restoration via Prompt Pool and Depth-Anything Constraint](others/teaching_tailored_to_talent_adverse_weather_restoration.md)**

:   提出 T3-DiffWeather，采用 prompt pool 自主组合子 prompt 构建天气退化信息，结合 Depth-Anything 约束的通用 prompt 提供场景信息，以对比 prompt 损失约束两类 prompt，在恶劣天气图像恢复任务上仅用 WeatherDiffusion 十分之一的采样步数达到 SOTA。
