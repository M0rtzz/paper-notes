---
title: >-
  ECCV2024 多模态VLM方向 44篇论文解读
description: >-
  44篇ECCV2024 多模态VLM方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态VLM

**🎞️ ECCV2024** · 共 **44** 篇

**[A Multimodal Benchmark Dataset And Model For Crop Disease Di](a_multimodal_benchmark_dataset_and_model_for_crop_disease_di.md)**

:   构建了包含13.7万张作物病害图像和100万问答对的CDDM数据集，并提出同时对视觉编码器、adapter和语言模型施加LoRA微调的策略，使Qwen-VL-Chat和LLaVA在作物病害诊断准确率上从个位数跃升至90%以上。

**[Adashield Safeguarding Multimodal Large Language Models From Structure-Based Att](adashield_safeguarding_multimodal_large_language_models_from_structure-based_att.md)**

:   AdaShield通过在MLLM输入前添加防御提示(defense prompt)来防御结构化越狱攻击（图像中嵌入有害文本），提出静态手动提示和自适应自动精化框架两种方案，无需微调模型即可显著提升安全性且不损害正常能力。

**[Addressclip Empowering Visionlanguage Models For Citywide Im](addressclip_empowering_visionlanguage_models_for_citywide_im.md)**

:   AddressCLIP 定义了"图像地址定位"(IAL) 新任务，提出端到端框架通过图像-文本对齐（图像↔地址/场景描述的对比学习）和图像-地理匹配（流形学习约束特征空间距离与地理距离一致）直接预测图像拍摄的可读文本地址，在自建的 Pittsburgh 和 San Francisco 数据集上优于现有 VLM 迁移方法。

**[Attention Prompting On Image For Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)**

:   本文提出Attention Prompting on Image（API），通过辅助模型（如CLIP或LLaVA）根据文本查询生成注意力热力图，将热力图叠加到原始图像上作为视觉提示输入LVLM，在不修改模型参数的情况下在MM-Vet、LLaVA-Bench等多个VL基准上稳定提升多种LVLM的性能（LLaVA-1.5提升3.8%/2.9%）。

**[Bad Students Make Great Teachers Active Learning Accelerates Large-Scale Visual ](bad_students_make_great_teachers_active_learning_accelerates_large-scale_visual_.md)**

:   提出 ClassAct/ActiveCLIP 方法，利用小型廉价代理模型为数据点计算"可学习性"评分来优先选择训练数据，使大规模视觉分类器和多模态模型分别减少46%和51%的训练更新量，且总计算量节省高达25%，是首个在大规模预训练中实现计算正收益的主动学习方法。

**[Beaf Observing Before-After Changes To Evaluate Hallucination In Vision-Language](beaf_observing_before-after_changes_to_evaluate_hallucination_in_vision-language.md)**

:   提出 BEAF 幻觉评估基准，通过图像编辑（移除物体）构造"前后对比"场景，设计 TU/IG/SB/ID 四个变化感知指标，揭示现有 VLM 即使传统 accuracy 高也可能存在严重幻觉。

**[Blink Multimodal Large Language Models Can See But Not Perceive](blink_multimodal_large_language_models_can_see_but_not_perceive.md)**

:   提出BLINK——一个包含14个经典计算机视觉感知任务的多模态评测基准（3807道选择题），这些任务人类可以"眨眼间"解决（95.7%准确率），但最强的GPT-4V仅达51.26%（仅高于随机猜测13.17%），揭示了当前MLLM在核心视觉感知能力上的严重缺失。

**[Brave Broadening The Visual Encoding Of Vision-Language Models](brave_broadening_the_visual_encoding_of_vision-language_models.md)**

:   本文系统性地分析了不同视觉编码器（CLIP、DINOv2、EVA-CLIP等）对VLM性能的影响，发现没有单一编码器能在所有任务上最优，基于此提出BRAVE方法，通过轻量级的MEQ-Former将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在captioning和VQA任务上取得SOTA，并显著降低视觉幻觉。

**[Cat Enhancing Multimodal Large Language Model To Answer Questions In Dynamic Aud](cat_enhancing_multimodal_large_language_model_to_answer_questions_in_dynamic_aud.md)**

:   提出 CAT 模型，通过设计问题相关线索聚合器（Clue Aggregator）捕获细粒度音视频特征，结合混合多模态训练策略和 AI 辅助的模糊感知直接偏好优化（ADPO）策略，显著提升 MLLM 在动态音视频场景中的问答准确性，在多个 AVQA 基准上达到 SOTA。

**[Clap Isolating Content From Style Through Contrastive Learning With Augmented Pr](clap_isolating_content_from_style_through_contrastive_learning_with_augmented_pr.md)**

:   从因果生成模型视角出发，提出 CLAP（Contrastive Learning with Augmented Prompts），通过文本 prompt 增强 + 对比学习训练一个轻量解耦网络，将 CLIP 预训练特征中的 content 与 style 分离，仅用文本训练即可同时提升图像和文本两侧的表征质量，在 zero-shot、few-shot 分类和对抗鲁棒性上均取得一致提升。

**[Dataset Growth](dataset_growth.md)**

:   提出 InfoGrowth，一种高效的在线数据清洗与选择算法，通过近邻搜索估计每个样本的信息增益，实现数据集的持续增长，同时保证清洁度和多样性，在 CC3M 上仅用 1/6 数据即超过全量训练效果。

**[Decoupling Common And Unique Representations For Multimodal Self-Supervised Lear](decoupling_common_and_unique_representations_for_multimodal_self-supervised_lear.md)**

:   提出 DeCUR，在多模态自监督学习中将嵌入维度显式拆分为跨模态共有 (common) 和模态独有 (unique) 两部分，通过互相关矩阵分别驱动对齐与去相关，同时引入模态内训练保证独有维度学到有意义信息，在 SAR-光学、RGB-DEM、RGB-Depth 三类多模态场景上均优于 Barlow Twins / CLIP 等基线。

**[Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt L](elevating_all_zero-shot_sketch-based_image_retrieval_through_multimodal_prompt_l.md)**

:   提出 SpLIP，一种基于冻结 CLIP 的双向多模态提示学习框架，通过视觉-文本编码器间的双向知识交换、自适应 margin 的三元组损失和条件跨模态拼图任务，在 ZS-SBIR、GZS-SBIR 和 FG-ZS-SBIR 三种草图检索设定下均取得 SOTA。

**[Eyes Closed Safety On Protecting Multimodal Llms Via Image-To-Text Transformatio](eyes_closed_safety_on_protecting_multimodal_llms_via_image-to-text_transformatio.md)**

:   提出ECSO（Eyes Closed, Safety On），一种无需训练的MLLM保护方法，通过检测自身响应的安全性，并将不安全查询中的图像自适应转换为文本描述，从而恢复预对齐LLM的内在安全机制，在MM-SafetyBench上实现最高71.3%的安全性提升，且不损害常规性能。

**[Flexattention For Efficient High-Resolution Vision-Language Models](flexattention_for_efficient_high-resolution_vision-language_models.md)**

:   提出 FlexAttention，通过基于注意力图的高分辨率token动态选择和层次化自注意力融合机制，在保持甚至超越现有高分辨率VLM性能的同时，将计算成本降低近40%。

**[Freemotion Mocap-Free Human Motion Synthesis With Multimodal Large Language Mode](freemotion_mocap-free_human_motion_synthesis_with_multimodal_large_language_mode.md)**

:   首次在**完全不使用动捕数据**的情况下，利用 MLLM（GPT-4V）作为关键帧设计师和动画师，结合基于物理的运动跟踪，实现开放集人体运动合成。

**[Genixer Empowering Multimodal Large Language Model As A Powerful Data Generator](genixer_empowering_multimodal_large_language_model_as_a_powerful_data_generator.md)**

:   提出 Genixer 数据生成流水线，训练 MLLM 自身作为数据生成器，无需依赖 GPT-4V 即可自动生成高质量视觉指令微调数据，生成的 915K VQA 数据和 350K REC 数据分别提升 LLaVA1.5 和 Shikra 在多个基准上的表现。

**[Groma Localized Visual Tokenization For Grounding Multimodal Large Language Mode](groma_localized_visual_tokenization_for_grounding_multimodal_large_language_mode.md)**

:   Groma提出了将定位能力嵌入视觉tokenization过程的新范式——通过region proposer发现感兴趣区域并编码为region token，使MLLM无需依赖LLM输出坐标或外部模块即可实现高精度的referring和grounding，同时利用GPT-4V+visual prompting构建了首个视觉-文本双prompt的grounded chat数据集Groma Instruct。

**[Grounding Language Models For Visual Entity Recognition](grounding_language_models_for_visual_entity_recognition.md)**

:   提出 AutoVER，在多模态大语言模型中统一集成对比检索和前缀树约束解码，将 600 万级 Wikipedia 实体空间先缩小到数百候选再做受限生成，在 Oven-Wiki 上将 entity seen 准确率从 PaLI-17B 的 30.6% 翻倍到 61.5%，同时在 unseen/query split 上也大幅领先。

**[M Ampmaposs A Benchmark To Evaluate Tool-Use For Multi-Step Multi-Modal Tasks](m_ampmaposs_a_benchmark_to_evaluate_tool-use_for_multi-step_multi-modal_tasks.md)**

:   提出 m&m's 基准，包含 4K+ 多步骤多模态任务和 33 个可执行工具，系统评估 10 个 LLM 在不同规划策略（多步 vs 逐步）、计划格式（JSON vs 代码）和反馈类型（解析/验证/执行）下的工具使用能力，发现多步JSON规划配合反馈是当前最优设计。

**[Marvelovd Marrying Object Recognition And Vision-Language Models For Robust Open](marvelovd_marrying_object_recognition_and_vision-language_models_for_robust_open.md)**

:   提出 MarvelOVD 框架，通过将检测器的上下文感知能力和背景识别能力融入 VLM 的伪标签生成与训练流程，在线净化噪声伪标签并自适应重加权训练框，在 COCO 和 LVIS 上大幅超越已有方法。

**[Mathverse Does Your Multi-Modal Llm Truly See The Diagrams In Visual Math Proble](mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)**

:   提出MathVerse——一个包含2612道视觉数学题目（转化为6个版本共15K测试样本）的多模态数学推理评测基准，通过系统性地调控文本与图像中的信息分配来检验MLLM是否真正"看懂"了数学图表，并提出CoT评估策略进行细粒度推理过程评分，揭示了大多数MLLM严重依赖文本而非视觉图表进行数学推理。

**[Meta-Prompting For Automating Zero-Shot Visual Recognition With Llms](meta-prompting_for_automating_zero-shot_visual_recognition_with_llms.md)**

:   提出 MPVR（Meta-Prompting for Visual Recognition），通过两阶段 meta-prompting 策略自动化生成多样化的类别特定 VLM prompt，无需人工设计 LLM 查询即可显著提升 CLIP 等模型的 zero-shot 识别性能。

**[Mm1 Methods Analysis And Insights From Multimodal Llm Pre-Training](mm1_methods_analysis_and_insights_from_multimodal_llm_pre-training.md)**

:   Apple 系统性地消融了 MLLM 构建的三大轴（架构、数据、训练），得出关键设计准则：图像分辨率 > 模型大小 > 训练数据；VL 连接器类型影响甚微；caption/interleaved/text-only 三类数据的精细混合至关重要，最终构建了 3B-30B dense 和最高 64B MoE 的 MM1 模型族，在 few-shot 预训练评测上达到 SOTA。

**[Mmbench Is Your Multi-Modal Model An All-Around Player](mmbench_is_your_multi-modal_model_an_all-around_player.md)**

:   提出 MMBench——一个包含 3217 道多选题、覆盖 20 个细粒度能力维度的双语（英/中）视觉语言模型评测基准，并设计了 CircularEval 循环评测策略和基于 LLM 的选项提取机制，显著提升了评测的鲁棒性和公平性。

**[Myvlm Personalizing Vlms For User-Specific Queries](myvlm_personalizing_vlms_for_user-specific_queries.md)**

:   提出MyVLM，通过外部概念识别头（concept head）和可学习的概念嵌入向量（concept embedding），在不修改VLM原始权重的情况下实现个性化视觉语言交互——仅需3-5张图片即可让VLM识别并描述用户特定概念（如"你的狗"、"你的朋友"），在BLIP-2和LLaVA上均取得了显著的个性化效果。

**[Navgpt-2 Unleashing Navigational Reasoning Capability For Large Vision-Language ](navgpt-2_unleashing_navigational_reasoning_capability_for_large_vision-language_.md)**

:   NavGPT-2通过将冻结LLM的隐层表征作为视觉-语言特征输入拓扑图导航策略网络，在保留LLM可解释性导航推理能力的同时，消除了基于LM的智能体与VLN专用模型之间的性能差距，并展现出优异的数据效率。

**[Omniview-Tuning Boosting Viewpoint Invariance Of Vision-Language Pre-Training Mo](omniview-tuning_boosting_viewpoint_invariance_of_vision-language_pre-training_mo.md)**

:   OVT通过构建460万多视角图文数据集MVCap和设计minimax优化的跨视角对齐框架，以参数高效微调方式显著提升VLP模型（如CLIP）对3D视角变化的鲁棒性（平均+9-10%），同时几乎不损失原始性能。

**[Quantized Prompt For Efficient Generalization Of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_vision-language_models.md)**

:   将量化误差视为一种正则化噪声，对VLM的可学习prompt进行极低比特量化（最低1-bit），在大幅减少存储开销（最高16倍压缩）的同时显著提升模型在未见类别上的泛化能力，QCoOp仅需0.26KB即超越大量SOTA方法。

**[Revision Rendering Tools Enable Spatial Fidelity In Vision-Language Models](revision_rendering_tools_enable_spatial_fidelity_in_vision-language_models.md)**

:   提出 REVISION 框架，利用 Blender 3D 渲染生成空间关系精确的合成图像，以免训练方式引导 T2I 模型生成空间一致的图像，并构建 RevQA 基准评估 MLLM 的空间推理能力。

**[Robust Calibration Of Large Vision-Language Adapters](robust_calibration_of_large_vision-language_adapters.md)**

:   本文发现CLIP适配方法（Adapter/Prompt Learning/TTA）在OOD场景下严重损害了零样本基线的校准能力，揭示logit范围增大（而非logit范数增大）是误校准的根本原因，并提出三种简单且模型无关的logit范围约束方案（ZS-Norm、Penalty、SaLS），有效缓解误校准同时保持判别性能。

**[Select And Distill Selective Dual-Teacher Knowledge Transfer For Continual Learn](select_and_distill_selective_dual-teacher_knowledge_transfer_for_continual_learn.md)**

:   提出选择性双教师知识迁移框架（SND），通过衡量预训练VLM和最近微调VLM之间的特征差异，在无标签参考数据集上自适应选择合适的教师进行知识蒸馏，同时缓解灾难性遗忘并保持零样本分类能力。

**[Self-Adapting Large Visual-Language Models To Edge Devices Across Visual Modalit](self-adapting_large_visual-language_models_to_edge_devices_across_visual_modalit.md)**

:   提出EdgeVL框架，通过两阶段适配（双模态知识蒸馏+量化感知对比学习），将大规模VLM（如CLIP）适配到边缘设备上，实现无需人工标注的跨模态（RGB和非RGB）开放词汇分类，达到最高15.4%的准确率提升和93倍的模型压缩。

**[Sharegpt4V Improving Large Multi-Modal Models With Better Captions](sharegpt4v_improving_large_multi-modal_models_with_better_captions.md)**

:   ShareGPT4V 构建了一个120万条高质量描述性caption数据集（由GPT4-Vision生成100K种子 + Share-Captioner扩展至1.2M），通过在预训练和SFT两阶段使用该数据集训练LLaVA架构的模型ShareGPT4V-7B，在11个多模态benchmark中9个取得最优，证明了高质量caption是LMM模态对齐的关键瓶颈。

**[Sq-Llava Self-Questioning For Large Vision-Language Assistant](sq-llava_self-questioning_for_large_vision-language_assistant.md)**

:   提出视觉自提问（Visual Self-Questioning）训练范式，让 LLM 不仅学习回答问题，还学习根据图像主动提问，通过充分利用指令数据中问题本身的丰富语义信息来增强视觉-语言对齐。

**[The Hard Positive Truth About Vision-Language Compositionality](the_hard_positive_truth_about_vision-language_compositionality.md)**

:   本文揭示了现有CLIP硬负例微调方法在提升组合性理解时引入了"过敏感"问题——模型将语义不变的硬正例（hard positives）也错误地判为不匹配；通过同时引入硬正例和硬负例进行微调，显著缓解了该问题并实现了更鲁棒的组合性提升。

**[Towards Open-Ended Visual Quality Comparison](towards_open-ended_visual_quality_comparison.md)**

:   本文提出 Co-Instruct，首个面向开放式视觉质量比较的大型多模态模型，通过从两种"弱监督源"（LLM合并的单图描述 + GPT-4V伪标签）构建562K指令微调数据集，实现比 GPT-4V（其教师模型）更高的多图质量比较准确率，并提出首个多图比较基准 MICBench。

**[Towards Real-World Adverse Weather Image Restoration Enhancing Clearness And Sem](towards_real-world_adverse_weather_image_restoration_enhancing_clearness_and_sem.md)**

:   本文提出WResVLM半监督学习框架，利用视觉-语言模型（VLM）为真实恶劣天气图像提供清晰度评估和语义描述监督信号，通过VLM图像评估+天气提示学习增强清晰度、描述辅助的语义正则化增强语义，在真实去雨/去雾/去雪任务上全面超越现有方法。

**[Umbrae Unified Multimodal Brain Decoding](umbrae_unified_multimodal_brain_decoding.md)**

:   提出UMBRAE，通过通用脑编码器将fMRI信号与图像特征对齐后送入冻结的MLLM，实现多模态脑解码（描述、定位、检索、视觉重建），并创新性地引入跨被试训练策略，使单一模型服务多个被试且优于单被试模型。

**[Unicode Learning A Unified Codebook For Multimodal Large Language Models](unicode_learning_a_unified_codebook_for_multimodal_large_language_models.md)**

:   UniCode提出学习一个统一的codebook来同时tokenize视觉和文本信号，通过language-driven iterative training范式将视觉tokenizer的码本与LLM的词表渐进对齐，并引入in-context image decompression预训练任务提升图像生成质量，使MLLM无需额外对齐模块即可实现多模态理解与生成。

**[Vary Scaling Up The Vision Vocabulary For Large Vision-Language Model](vary_scaling_up_the_vision_vocabulary_for_large_vision-language_model.md)**

:   提出 Vary 方法，通过生成并融合新的视觉词汇表来扩展 LVLM 的视觉感知能力，使模型在保持通用能力的同时获得文档 OCR、图表理解等细粒度视觉感知能力。

**[Vary Scaling Up The Vision Vocabulary For Large Visionlanguag](vary_scaling_up_the_vision_vocabulary_for_large_visionlanguag.md)**

:   提出 Vary 方法，通过生成并融合新的视觉词汇表（vision vocabulary）来扩展 LVLM 的视觉感知能力，使模型在保持原有通用能力的同时，获得文档级 OCR、图表理解等细粒度视觉感知新能力。

**[X-Former Unifying Contrastive And Reconstruction Learning For Mllms](x-former_unifying_contrastive_and_reconstruction_learning_for_mllms.md)**

:   提出X-Former，一个轻量级Transformer模块，通过双交叉注意力机制融合CLIP-ViT（对比学习）和MAE-ViT（掩码图像建模）的互补视觉特征，在仅使用1/10数据量的情况下显著超越BLIP-2在细粒度视觉理解任务上的表现。

**[Zero-Shot Object Counting With Good Exemplars](zero-shot_object_counting_with_good_exemplars.md)**

:   提出VA-Count框架，通过样本增强模块（EEM）利用Grounding DINO发现高质量正负样本，结合噪声抑制模块（NSM）用对比学习区分正负密度图，实现零样本目标计数在FSC-147和CARPK上的SOTA表现。
