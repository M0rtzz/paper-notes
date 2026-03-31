<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**🧠 NeurIPS2025** · 共 **93** 篇

**[A Frustratingly Simple Yet Highly Effective Attack Baseline: Over 90% Success Rate Against the Strong Black-box Models of GPT-4.5/4o/o1](a_frustratingly_simple_yet_highly_effective_attack_baseline.md)**

:   提出 M-Attack，通过对对抗图像做随机裁剪后与目标图像在嵌入空间做局部对齐（而非传统的全局对齐），配合多模型集成，使得生成的对抗扰动具有丰富的局部语义细节，在 GPT-4.5/4o/o1 等商业黑盒 LVLM 上实现超过 90% 的目标攻击成功率，大幅超越所有已有方法。

**[A Multimodal Benchmark for Framing of Oil & Gas Advertising and Potential Greenwashing Detection](a_multimodal_benchmark_for_framing_of_oil_gas_advertising_an.md)**

:   构建了首个面向石油天然气行业视频广告的多模态框架分析基准数据集（706个视频，覆盖Facebook和YouTube两个平台，13种框架类型），用于评估VLM在检测企业"洗绿"宣传中的能力，发现GPT-4.1在环境信息检测上可达79% F1但在绿色创新识别上仅46% F1。

**[AC-LoRA: (Almost) Training-Free Access Control-Aware Multi-Modal LLMs](aclora_almost_trainingfree_access_controlaware_multimodal_ll.md)**

:   设计AC-LoRA系统，通过为不同权限数据集维护独立的LoRA适配器，并基于查询相似度和用户权限进行检索+无训练合并，实现企业级LLM聊天机器人的强信息隔离保证。

**[ACT as Human: Multimodal Large Language Model Data Annotation with Critical Thinking](act_as_human_multimodal_large_language_model_data_annotation.md)**

:   提出ACT（Annotation with Critical Thinking）流水线，先用MLLM批量标注数据，再用另一个MLLM作为"批评者"识别可能的错误标注，仅让人类审核被标记的样本，在减少70-90%人工标注成本的同时将性能差距控制在<2%。

**[AdaLRS: Loss-Guided Adaptive Learning Rate Search for Efficient Foundation Model Pretraining](adalrs_lossguided_adaptive_learning_rate_search_for_efficien.md)**

:   提出AdaLRS，一种即插即用的在线学习率搜索算法，通过监控损失下降速度（loss velocity）来自适应调整学习率，将学习率超参搜索的成本从多次独立训练降低到单次训练，实现~50%的训练成本节省。

**[Adapting Vision-Language Models for Evaluating World Models](adapting_visionlanguage_models_for_evaluating_world_models.md)**

:   提出UNIVERSE框架，通过仅微调PaliGemma 2的投影头（0.07%参数）和优化数据混合策略，实现对游戏世界模型rollout的高效视觉语言评估，在动作/角色识别任务上以极低成本接近完整微调的性能。

**[ADMN: A Layer-Wise Adaptive Multimodal Network for Dynamic Input Noise and Compute Resources](admn_a_layerwise_adaptive_multimodal_network_for_dynamic_inp.md)**

:   提出 ADMN（Adaptive Depth Multimodal Network），通过两阶段训练——(1) Multimodal LayerDrop 微调使 backbone 适应任意层配置，(2) QoI感知控制器动态分配层预算给各模态——在严格计算约束下根据每个模态的信息质量(QoI)自适应分配层数，匹配全量模型精度同时减少 75% FLOPs 和 60% 延迟。

**[Advancing Compositional Awareness in CLIP with Efficient Fine-Tuning](advancing_compositional_awareness_in_clip_with_efficient_fin.md)**

:   提出 CLIC（Compositionally-aware Learning in CLIP），通过拼接图像对 + 跨图词汇交换生成 hard negatives + 多正样本训练的策略，在仅微调文本编码器的情况下同时提升 CLIP 的组合推理能力和检索性能，在 SugarCrepe++ 上取得 CLIP 类模型 SOTA。

**[AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models](affordbot_3d_fine-grained_embodied_reasoning_via_multimodal_large_language_model.md)**

:   提出细粒度 3D 具身推理任务（预测可操作元素的空间位置+运动类型+运动轴），通过将 3D 点云渲染为环视图并投影 affordance 候选，结合定制的 CoT 推理范式指导 MLLM 实现 SOTA，AP25 达 23.3%。

**[Aligning by Misaligning: Boundary-aware Curriculum Learning for Multimodal Alignment](aligning_by_misaligning_boundaryaware_curriculum_learning_fo.md)**

:   提出 BACL（Boundary-Aware Curriculum with Local Attention），通过可学习的边界感知负样本采样器（由易到难课程学习）+ 对比局部注意力损失（定位 token 级 mismatch），在 LAION-400M 上为 CLIP 带来 +32% R@1 提升，并在四个大规模基准上取得 SOTA。

**[AntiGrounding: Lifting Robotic Actions into VLM Representation Space for Decision Making](antigrounding_lifting_robotic_actions_into_vlm_representatio.md)**

:   提出 AntiGrounding，逆转传统指令 grounding 过程——不是将语言映射到动作空间，而是将候选机器人动作"提升"到 VLM 表示空间（通过多视角轨迹渲染 + 结构化 VQA），实现零样本闭环机器人轨迹合成。

**[Approximate Domain Unlearning for Vision-Language Models](approximate_domain_unlearning_for_visionlanguage_models.md)**

:   提出 Approximate Domain Unlearning (ADU) 新任务，通过 Domain Disentangling Loss (DDL) 和 Instance-wise Prompt Generator (InstaPG) 两个模块，让预训练 VLM 选择性遗忘指定域（如插画、素描）的识别能力，同时保持其他域（如真实照片）的分类精度，在四个多域数据集上大幅超越所有基线。

**[Balanced Token Pruning: Accelerating Vision Language Models Beyond Local Optimization](balanced_token_pruning_accelerating_vision_language_models_b.md)**

:   提出 Balanced Token Pruning (BTP)，通过在浅层优先多样性剪枝、深层优先注意力剪枝的分阶段策略，联合优化局部输出一致性和全局表示质量，在仅保留 22% 视觉 token 的情况下保持原模型 98% 的性能。

**[Benchmarking Retrieval-Augmented Multimodal Generation for Document Question Answering](benchmarking_retrievalaugmented_multimodal_generation_for_do.md)**

:   提出 MMDocRAG 基准（4055 个专家标注的 QA 对），系统评估了 60 个 VLM/LLM 和 14 个检索器在多模态文档检索增强生成中的引用选择和交错图文回答能力，揭示当前最强模型 GPT-4.1 的 Quote Selection F1 仅 70.2%，微调可显著提升性能。

**[Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging](better_tokens_for_better_3d_advancing_vision-language_modeling_in_3d_medical_ima.md)**

:   提出 BTB3D，一种基于因果卷积编解码器 + 3D Haar 小波压缩 + 三阶段渐进训练的 3D CT tokenizer，在放射报告生成和文本条件 CT 合成两大下游任务上大幅刷新 SOTA，证明"更好的 token 比更大的语言模型更重要"。

**[Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability](beyond_greedy_exits_improved_early_exit_decisions_for_risk_control_and_reliabili.md)**

:   UAT（Unsupervised Adaptive Thresholding）为早退 DNN 设计了可靠性函数来评估中间层输出质量，并用多臂赌博机（MAB）算法在推理时动态学习最优退出阈值，实现 1.7-2.1× 加速且性能损失 <2%，同时对分布偏移鲁棒。

**[Bias in the Picture: Benchmarking VLMs with Social-Cue News Images and LLM-as-Judge](bias_in_the_picture_benchmarking_vlms_with_social-cue_news_images_and_llm-as-jud.md)**

:   构建 1,343 个新闻图片-问答对的偏见评估基准，标注年龄/性别/种族/职业等人口统计属性，用 GPT-4o 作为评判员（LLM-as-judge）评估 15 个 VLM 在开放式问答中的偏见表现，发现高忠实度不等于低偏见，且性别和职业偏见尤为严重。

**[BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning](bioclip_2_emergent_properties_from_scaling_hierarchical_contrastive_learning.md)**

:   BioCLIP 2 在 TreeOfLife-200M（2.14 亿图像/95.2 万物种）上用层级对比学习训练 ViT-L，零样本物种识别比 BioCLIP 提升 18%，并发现规模化带来的涌现性质——嵌入自动编码生态关系（如达尔文雀喙大小排列）且种内变异与种间差异正交。

**[BLINK-Twice: You See But Do You Observe? A Reasoning Benchmark on Visual Perception](blink-twice_you_see_but_do_you_observe_a_reasoning_benchmark_on_visual_perceptio.md)**

:   提出视觉中心推理 benchmark BLINK-Twice（345 张视觉挑战图 + 103 个对抗样本 + 896 个 VQA + 1725 个推理步骤标注），通过 7 类视觉错觉场景评估 MLLM "看到但未观察到"的推理能力，发现最强模型 Gemini-2.5 Pro 的 G-Acc 仅 26.9%，多轮图像观察和主动视觉交互是提升方向。

**[Breaking the Compression Ceiling: Data-Free Pipeline for Ultra-Efficient Delta Compression](breaking_the_compression_ceiling_data-free_pipeline_for_ultra-efficient_delta_co.md)**

:   提出 UltraDelta——首个无数据 delta 权重压缩流水线，通过方差引导的混合稀疏分配、分布感知压缩和迹范数引导缩放三个组件，在 LLM/NLP/视觉/多模态模型上实现最高 224× 的超高压缩比且性能不降甚至超越微调模型。

**[BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models](bridgevla_input-output_alignment_for_efficient_3d_manipulation_learning_with_vis.md)**

:   提出 BridgeVLA，通过将 3D 点云投影为多视角 2D 图像并以 2D 热力图作为中间表示来对齐输入输出空间，实现了高效且有效的 3D 机器人操作学习。

**[Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning](can_llms_reason_over_non-text_modalities_in_a_training-free_manner_a_case_study_.md)**

:   提出 In-Context Representation Learning（ICRL），首个训练无关框架，将非文本模态基础模型（FM）的表征注入纯文本 LLM 进行少样本推理，通过 PCA 文本注入和最优传输嵌入对齐两种策略实现跨模态知识利用。

**[Can Multi-Modal LLMs Provide Live Step-by-Step Task Guidance?](can_multi-modal_llms_provide_live_step-by-step_task_guidance.md)**

:   提出 Qualcomm Interactive Cooking 基准和 LiveMamba 模型，首次系统评估多模态 LLM 在实时流式视频中提供分步任务指导（包括指令下发、完成检测和错误反馈）的能力。

**[CAPability: A Comprehensive Visual Caption Benchmark for Evaluation](capability_a_comprehensive_visual_caption_benchmark_for_eval.md)**

:   构建 CAPability——11K 标注的图片/视频描述评估基准，从 6 个视角 12 个维度评估 VLM 的描述能力，引入 KT（know-but-cannot-tell）指标衡量 VLM 在 QA 中已知但描述中遗漏的信息差距。

**[Causal-LLaVA: Causal Disentanglement for Mitigating Hallucination in Multimodal Large Language Models](causalllava_causal_disentanglement_for_mitigating_hallucinat.md)**

:   揭示 MLLM 中物体幻觉的表示层根因——数据集共现偏差导致的语义纠缠，提出双路因果解纠缠框架（Causal-Driven Projector + Causal Intervention Module），通过后门调整在 projector 和最终 Transformer 层分离共现物体表示，使 MME-Perception 提升 22.6%。

**[ChartMuseum: Testing Visual Reasoning Capabilities of Large Vision-Language Models](chartmuseum_testing_visual_reasoning_capabilities_of_large_v.md)**

:   构建ChartMuseum——一个包含1,162个专家标注问题的图表QA benchmark，专门评估LVLM的复杂视觉和文本推理能力。与现有图表benchmark（前沿模型接近饱和）不同，ChartMuseum揭示了巨大的模型-人类性能差距：人类93%准确率 vs Gemini-2.5-Pro仅63.0% vs 最佳开源Qwen2.5-VL-72B仅38.5%，且所有模型在视觉推理重的问题上掉点35-55%。

**[CHOICE: Benchmarking the Remote Sensing Capabilities of Large Vision-Language Models](choice_benchmarking_the_remote_sensing_capabilities_of_large_vision-language_mod.md)**

:   提出 CHOICE，一个面向遥感领域的大规模多层级 VLM 基准，包含 10,507 道全新采集题目，覆盖感知与推理 2 大维度、6 个子维度、23 个叶任务，首次实现对 VLM 遥感能力的系统化与客观化评估。

**[CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization](coido_efficient_data_selection_for_visual_instruction_tuning_via_coupled_importa.md)**

:   提出 CoIDO，一个双目标优化数据选择框架，通过联合优化数据重要性和多样性，仅用 20% 随机数据训练轻量评分器，即可从 LLaVA-665K 中选出 20% 子集达到全量微调 98.2% 的性能，同时计算开销为所有方法最低。

**[Context Informs Pragmatic Interpretation in Vision-Language Models](context_informs_pragmatic_interpretation_in_vision-language_models.md)**

:   通过迭代参考游戏（iterated reference games）系统评估 VLM 的语用推理能力，发现模型在无上下文时表现远逊于人类，但在获得相关对话历史后能快速学习达到约 80% 准确率，揭示了 VLM 对上下文信息的强烈依赖性。

**[Continual Multimodal Contrastive Learning](continual_multimodal_contrastive_learning.md)**

:   首次形式化定义持续多模态对比学习(CMCL)问题——按顺序在不同模态对数据上训练而不忘记之前的对齐，提出Dual-sided Null Space (DNS)方法将新梯度投影到不影响旧知识的子空间，在7个数据集11个训练步骤上一致优于现有持续学习基线。

**[CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder](covmatch_crosscovariance_guided_multimodal_dataset_distillat.md)**

:   提出 CovMatch，通过将多模态对比学习的双层优化简化为跨协方差矩阵对齐的闭式解，首次实现图文双编码器的联合优化进行多模态数据集蒸馏，仅用 500 个合成图文对在 Flickr30K 上获得 38.4 平均检索精度（+6.8% 超越 SOTA LoRS），在极端数据高效场景下大幅超越冻结文本编码器的方法。

**[CyIN: Cyclic Informative Latent Space for Bridging Complete and Incomplete Multimodal Learning](cyin_cyclic_informative_latent_space_for_bridging_complete_and_incomplete_multim.md)**

:   提出 CyIN 框架，通过 token 级和 label 级信息瓶颈（IB）构建信息化潜空间，结合循环跨模态翻译重建缺失信息，在单一统一模型中同时优化完整和不完整多模态学习。

**[DanmakuTPPBench: A Multi-modal Benchmark for Temporal Point Process Modeling and Understanding](danmakutppbench_a_multimodal_benchmark_for_temporal_point_pr.md)**

:   论文提出首个面向多模态 Temporal Point Process 的系统 benchmark：一方面构建来自 Bilibili 弹幕视频的时间戳-文本-视频联合事件数据集 DanmakuTPP-Events，另一方面通过多智能体 LLM/MLLM pipeline 构建复杂时序推理问答集 DanmakuTPP-QA，系统揭示当前 TPP 模型与 MLLM 在多模态事件动态理解上的明显短板。

**[Don't Just Chase "Highlighted Tokens" in MLLMs: Revisiting Visual Holistic Context Retention](dont_just_chase_highlighted_tokens_in_mllms_revisiting_visual_holistic_context_r.md)**

:   提出 HoloV，一个即插即用的视觉 token 剪枝框架，通过在不同空间裁剪区域自适应分配剪枝预算，保留全局视觉上下文而非仅保留注意力高亮 token，在 LLaVA-1.5 上剪枝 88.9% token 仍保留 95.8% 原始性能。

**[DOTA: Distributional Test-Time Adaptation of Vision-Language Models](dota_distributional_testtime_adaptation_of_visionlanguage_mo.md)**

:   提出 DOTA（DistributiOnal Test-time Adaptation），不再简单缓存测试样本，而是**持续估计测试数据流的底层分布**，通过贝叶斯定理计算后验概率实现自适应，解决了缓存容量有限导致的灾难性遗忘问题，在多个分布偏移基准上达到 SOTA。

**[DynamicVL: Benchmarking MLLMs for Dynamic City Understanding](dynamicvl_benchmarking_multimodal_large_language_models_for_dynamic_city_underst.md)**

:   提出 DVL-Suite 框架，包含 DVL-Bench 基准和 DVL-Instruct 指令微调数据集，覆盖 42 座美国城市、14,871 张高分辨率多时相遥感影像，系统评估 18 个 MLLM 在长期城市动态理解上的能力，并开发了 DVLChat 基线模型。

**[Efficient Vision-Language Reasoning via Adaptive Token Pruning](efficient_vision-language_reasoning_via_adaptive_token_pruning.md)**

:   提出 Adaptive Token Pruning (ATP)，一种免训练的即插即用模块，通过融合 ViT CLS 注意力（模态内显著性）和 CLIP 文本-图像相似度（模态间相关性）来筛选最有信息量的视觉 token，在 VQA/GQA/COCO Captioning 上以约 40% FLOPs 降低和 1.5 倍加速换取不到 1% 的精度损失。

**[ElasticMM: Efficient MLLM Serving with Elastic Multimodal Parallelism](elasticmm_efficient_multimodal_llms_serving_with_elastic_multimodal_parallelism.md)**

:   提出弹性多模态并行（EMP）范式和 ElasticMM 系统，通过模态感知负载均衡和弹性分区调度将多模态推理的不同阶段解耦到独立实例，相比 vLLM TTFT 降低最高 4.2 倍、吞吐量提升 3.2-4.5 倍。

**[READ: Enhancing Compositional Reasoning in CLIP via Reconstruction and Alignment of Text Descriptions](enhancing_compositional_reasoning_in_clip_via_reconstruction.md)**

:   提出 READ 微调方法，通过两个辅助目标——(1) token-level 重建（冻结解码器从文本嵌入重建替代描述）和 (2) sentence-level 对齐（强制改述的嵌入一致）——增强 CLIP 文本编码器的组合推理能力，在 5 个组合推理基准上达到 SOTA（超 NegCLIP 4.5%，超 FSC-CLIP 4.1%）。

**[Enhancing Outcome Reward-Based RL Training of MLLMs with Self-Consistency Sampling](enhancing_the_outcome_reward-based_rl_training_of_mllms_with_self-consistency_sa.md)**

:   针对多模态多选题中"结果奖励 RL 训练导致不忠实推理轨迹"的问题，提出 Self-Consistency Sampling (SCS)，通过截断-重采样和视觉扰动获得一致性奖励来惩罚虚假推理，搭载 RLOO 后在六个基准上平均提升 7.7 个百分点。

**[Enhancing Vision-Language Model Reliability with Uncertainty-Guided Dropout Decoding](enhancing_visionlanguage_model_reliability_with_uncertaintyg.md)**

:   提出Dropout Decoding——量化视觉token的认知不确定性(epistemic uncertainty)，选择性遮掩高不确定性token，通过集成多个遮掩后的解码结果做多数投票，无需训练即在InstructBLIP上CHAIR_I降低16%、CHAIR_S降低12%。

**[Evaluating Multimodal Large Language Models on Core Music Perception Tasks](evaluating_multimodal_large_language_models_on_core_music_perception_tasks.md)**

:   本文通过三项核心音乐感知任务（切分节奏评分、移调检测、和弦辨识）系统性评估了多模态LLM在音频与MIDI两种输入下的表现，揭示了模型在符号推理上接近理想但在音频感知上存在显著缺陷的关键差距。

**[ExGra-Med: Extended Context Graph Alignment for Medical Vision-Language Models](exgra-med_extended_context_graph_alignment_for_medical_vision-language_models.md)**

:   ExGra-Med 提出了一种多图对齐（multi-graph alignment）框架，通过联合对齐图像、指令响应和扩展上下文描述在潜空间中的图结构关系，仅用10%预训练数据即可匹配 LLaVA-Med 的100%数据性能，并在多个医学VQA任务上超越现有SOTA。

**[Explaining Similarity in Vision-Language Encoders with Weighted Banzhaf Interactions](explaining_similarity_in_vision-language_encoders_with_weighted_banzhaf_interact.md)**

:   FIxLIP 提出基于加权 Banzhaf 交互指数的博弈论框架，统一分解视觉-语言编码器（如 CLIP、SigLIP-2）的相似度预测为一阶token归因和二阶跨模态/模态内交互，在效率和忠实度上均超越现有一阶归因方法。

**[FineGRAIN: Evaluating Failure Modes of Text-to-Image Models with Vision Language Model Judges](finegrain_evaluating_failure_modes_of_text-to-image_models_with_vision_language_.md)**

:   FineGRAIN 提出了一个结构化的联合评测框架，通过定义27种细粒度失败模式和利用 VLM+LLM agentic pipeline 来同时评估文本到图像模型的 prompt 遵循能力和视觉语言模型的图像理解能力，揭示了两类模型在特定任务上的系统性缺陷。

**[First SFT, Second RL, Third UPT: Continual Improving Multi-Modal LLM Reasoning via Unsupervised Post-Training](first_sft_second_rl_third_upt_continual_improving_multi-modal_llm_reasoning_via_.md)**

:   提出 MM-UPT 框架，在 SFT 和 RL 之后引入第三阶段"无监督后训练"，通过多数投票作为伪奖励信号结合 GRPO 实现 MLLM 的自我改进，在 MathVista 上将 Qwen2.5-VL-7B 从 66.3% 提升至 72.9%。

**[FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models](flexac_towards_flexible_control_of_associative_reasoning_in_multimodal_large_lan.md)**

:   FlexAC 发现 MLLM 的联想推理行为主要编码在中间层，通过从幻觉响应中提取引导向量并在推理时注入中间层表示，实现忠实性与创造力的灵活调控——幻觉率降低 29%(CHAIR)，创造力提升 5.8×(Creation-MMBench)，且无需训练。

**[FlowCut: Rethinking Redundancy via Information Flow for Efficient Vision-Language Models](flowcut_rethinking_redundancy_via_information_flow_for_effic.md)**

:   从信息流（Information Flow）视角重新理解VLM中视觉token的冗余性：发现CLS token是信息中继站、冗余渐进式涌现、单层单标准评分不够可靠，提出FlowCut——基于信息流感知的多标准累积重要性剪枝框架，在LLaVA-1.5-7B上以88.9%的token减少率超越SOTA 1.6%，在LLaVA-NeXT-7B上超越4.3%。

**[FOCUS: Internal MLLM Representations for Efficient Fine-Grained Visual Question Answering](focus_internal_mllm_representations_for_efficient_fine-grained_visual_question_a.md)**

:   提出 FOCUS，一种无需训练的视觉裁剪方法，利用 MLLM 内部 KV-cache 中 value 特征的余弦相似度构建目标相关性图，高效定位问题相关的图像区域，在细粒度 VQA 上实现与 SOTA 可比的精度，同时计算效率提升 3-6.5 倍。

**[ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](forcevla_enhancing_vla_models_with_a_force-aware_moe_for_contact-rich_manipulati.md)**

:   提出 ForceVLA，在 VLA 框架中将 6 轴力/力矩传感引入为一等模态，通过 FVLMoE（力感知混合专家）模块在动作解码阶段动态融合视觉-语言嵌入与实时力反馈，在 5 项接触密集操作任务上平均成功率提升 23.2%，个别任务达 80%。

**[FractalBench: Diagnosing Visual-Mathematical Reasoning Through Recursive Program Synthesis](fractalbench_diagnosing_visual-mathematical_reasoning_through_recursive_program_.md)**

:   提出 FractalBench，一个通过分形图像程序合成诊断 MLLM 视觉-数学推理能力的 benchmark：12 种经典分形、610 张测试图、4 个 MLLM，揭示 76% 的代码能执行但仅 4% 视觉正确，暴露了模型在递归抽象能力上的根本缺陷。

**[From Flat to Hierarchical: Extracting Sparse Representations with Matching Pursuit](from_flat_to_hierarchical_extracting_sparse_representations_with_matching_pursui.md)**

:   提出 MP-SAE，将经典 Matching Pursuit 算法展开为 SAE 的序列化编码器，通过残差引导的贪心特征选择实现条件正交性，能捕捉标准 SAE 无法发现的层次结构、非线性可及和跨模态特征，并天然支持推理时自适应稀疏度调节。

**[GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images](gem_empowering_mllm_for_grounded_ecg_understanding_with_time_series_and_images.md)**

:   提出 GEM，首个统一 ECG 时间序列、12 导联 ECG 图像和文本的多模态大语言模型，通过双编码器框架、跨模态对齐和知识引导的指令数据生成，实现了基于可量化生理特征的接地心电图诊断，诊断准确率提升 7.4%，可解释性提升 22.7%，接地能力提升 25.3%。

**[Generalized Contrastive Learning for Universal Multimodal Retrieval](generalized_contrastive_learning_for_universal_multimodal_re.md)**

:   提出 Generalized Contrastive Learning (GCL)——在 mini-batch 内对所有 6 种模态对组合（image↔text, image↔image+text, text↔image+text）执行对比学习，无需构建新的三元组数据集，仅用现有图文对即可在 M-BEIR 上将 VISTA 的平均检索精度从 21.18 提升到 34.06（+60.8%），在 MMEB 的 text→image+text 任务上从 10.1% 提升到 31.1%。

**[Generate, but Verify: Reducing Hallucination in Vision-Language Models with Retrospective Resampling](generate_but_verify_reducing_hallucination_in_visionlanguage.md)**

:   提出REVERSE框架——首次在单一VLM内统一了生成、验证和纠正三个阶段：通过引入<SPAN>、</CN>（置信）、</UN>（不置信）三个特殊token训练幻觉感知模型，推理时当</UN>概率超过阈值就回溯到上一个</CN>重新生成，在CHAIR-MSCOCO上降低12%、HaloQuest上降低34%的幻觉率。

**[GeoRanker: Distance-Aware Ranking for Worldwide Image Geolocalization](georanker_distance-aware_ranking_for_worldwide_image_geolocalization.md)**

:   提出 GeoRanker，一种距离感知排序框架，利用大视觉语言模型建模查询-候选之间的空间关系，通过多阶距离损失实现全球图像地理定位的 SOTA。

**[GLSim: Detecting Object Hallucinations in LVLMs via Global-Local Similarity](glsim_detecting_object_hallucinations_in_lvlms_via_globalloc.md)**

:   提出 GLSim，一种无训练的物体幻觉检测框架，结合图像-文本间的全局和局部嵌入相似度信号来判断 LVLM 生成的物体是否为幻觉，显著超越仅使用全局或局部信号的方法。

**[GoalLadder: Incremental Goal Discovery with Vision-Language Models](goalladder_incremental_goal_discovery_with_vision-language_models.md)**

:   提出 GoalLadder，利用 VLM 渐进式发现并排序候选目标状态，结合 ELO 评分系统抵抗噪声反馈，在学习的嵌入空间中定义距离奖励，仅凭单条语言指令就能训练 RL 智能体达到约 95% 的成功率。

**[Guiding Cross-Modal Representations with MLLM Priors via Preference Alignment](guiding_cross-modal_representations_with_mllm_priors_via_preference_alignment.md)**

:   提出 MAPLE 框架，利用现成 MLLM 的内在模态对齐能力自动构建偏好数据，通过 Relative Preference Alignment（RPA）损失引导跨模态表示学习，在细粒度检索任务上取得显著提升。

**[HAWAII: Hierarchical Visual Knowledge Transfer for Efficient VLM](hawaii_hierarchical_visual_knowledge_transfer_for_efficient_vision-language_mode.md)**

:   提出 Hawaii 框架，通过混合 LoRA 适配器（MoLA）和分层知识蒸馏（HKD），将多个视觉专家的知识蒸馏到单个视觉编码器中，在不增加推理成本的前提下显著提升 VLM 的视觉理解能力。

**[HermesFlow: Seamlessly Closing the Gap in Multimodal Understanding and Generation](hermesflow_seamlessly_closing_the_gap_in_multimodal_understanding_and_generation.md)**

:   首次揭示统一多模态大模型中理解能力普遍强于生成能力的现象，提出 HermesFlow 框架，通过同源偏好数据构建配对理解-生成偏好对，利用 Pair-DPO 和自博弈迭代优化，在不引入外部高质量数据的情况下同步提升理解与生成能力并缩小两者差距。

**[Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems](hierarchical_self-attention_generalizing_neural_attention_mechanics_to_multi-sca.md)**

:   从熵最小化第一性原理推导出层次化自注意力（HSA）机制，为嵌套信号（多模态、多尺度数据）提供理论最优的注意力计算方法，并证明 HSA 是在保持层次约束下最接近标准 Softmax 注意力的 KL 散度最优解。

**[HoPE: Hybrid of Position Embedding for Long Context Vision-Language Models](hope_hybrid_of_position_embedding_for_long_context_visionlan.md)**

:   提出 HoPE（Hybrid of Position Embedding），通过混合频率分配策略和动态时间缩放机制改进 VLM 中的位置编码，解决 RoPE 在长视频等长上下文多模态场景中无法可靠捕捉时空语义相似性的问题，在四个长视频基准上一致超越现有方法。

**[iFinder: Structured Zero-Shot VLM Grounding for Dash-Cam Video Reasoning](ifinder_structured_zero-shot_vision-based_llm_grounding_for_dash-cam_video_reaso.md)**

:   提出 iFinder，一个模块化免训练框架，将行车记录仪视频解耦为感知（结构化场景表示）与推理（LLM），通过层级数据结构和三块式提示策略使 LLM 获得可解释的时空推理能力，在四个驾驶视频基准上零样本超越端到端 V-VLM，事故推理准确率提升高达 39%。

**[Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats](intervene-all-paths_unified_mitigation_of_lvlm_hallucinations_across_alignment_f.md)**

:   提出 AllPath，一个基于 Transformer 因果架构的多路径幻觉干预框架，首次发现 LVLM 的幻觉不来自单一因果路径而是 image-to-input-text、image-to-output-text、text-to-text 三条路径的交互，并且模型会根据问答对齐格式自适应选择不同路径；通过为每条路径设计轻量级关键 head 识别方法并自适应干预，在 POPE、MCQ-POPE、CHAIR、MME 四个不同格式 benchmark 上一致降低幻觉。

**[JailBound: Jailbreaking Internal Safety Boundaries of Vision-Language Models](jailbound_jailbreaking_internal_safety_boundaries_of_vision-language_models.md)**

:   受 Eliciting Latent Knowledge (ELK) 框架启发，首次揭示 VLM 在 fusion layer 潜空间中存在可近似的安全决策边界，提出 JailBound 两阶段攻击框架（Safety Boundary Probing + Safety Boundary Crossing），通过联合优化图像和文本对抗扰动跨越该边界，在白盒和黑盒场景分别达到 94.32% 和 67.28% 平均攻击成功率，显著超越 SOTA。

**[Learning Shared Representations from Unpaired Data](learning_shared_representations_from_unpaired_data.md)**

:   提出 SUE (Spectral Universal Embedding)，首次证明几乎完全依赖非配对数据即可学习跨模态共享表示：通过独立的频谱嵌入从各模态随机游走中提取模态不变的"通用"结构，再用极少量配对样本（~100对）做 CCA 线性对齐 + MMD 非线性微调，在检索上超越使用同等配对数的对比学习 250%+。

**[Learning to Instruct for Visual Instruction Tuning](learning_to_instruct_for_visual_instruction_tuning.md)**

:   提出 L2T（Learning to Instruct），仅通过将训练损失扩展到指令序列（不再只在回答上计算 loss）来改善视觉指令调优——无额外数据和几乎零计算开销，在 16 个多模态基准上获得高达 9% 的相对提升，captioning 提升 18%，同时缓解幻觉。

**[Learning to Steer: Input-dependent Steering for Multimodal LLMs](learning_to_steer_input-dependent_steering_for_multimodal_llms.md)**

:   针对现有模型引导(steering)方法使用固定方向向量无法适配不同输入的局限，提出 L2S (Learn-to-Steer)：先通过输入特定的对比提示生成理想的引导向量（P2S），再训练一个轻量 2 层 MLP 从输入上下文预测该向量，以极低开销实现了输入依赖的行为引导，在安全执行和幻觉缓解两个应用上显著优于静态 steering 基线。

**[MemEIC: A Step Toward Continual and Compositional Knowledge Editing](memeic_a_step_toward_continual_and_compositional_knowledge_editing.md)**

:   提出 MemEIC 框架，通过外部双模态检索记忆 + 内部模态分离 LoRA 适配器 + 仿脑 Knowledge Connector 三层架构，实现大视觉语言模型的持续、组合式知识编辑，在新提出的 CCKEB 基准上大幅超越现有方法。

**[MERIT: Multilingual Semantic Retrieval with Interleaved Multi-Condition Query](merit_multilingual_semantic_retrieval_with_interleaved_multi-condition_query.md)**

:   提出首个多语言交错多条件语义检索数据集 MERIT（320K queries, 135K products, 5种语言, 7大品类），揭示现有检索模型仅关注全局语义而忽略条件细节的瓶颈，并设计 Coral 微调框架通过嵌入重建+对比学习将检索性能提升 45.9%。

**[Metacognitive Sensitivity for Test-Time Dynamic Model Selection](metacognitive_sensitivity_for_test-time_dynamic_model_selection.md)**

:   借鉴人类认知科学中的元认知灵敏度（meta-d'）概念，提出一种测试时动态模型选择框架：用 meta-d' 量化模型"知道自己知不知道"的能力，结合即时置信度构成上下文向量，通过 contextual bandit 在线选择最优模型，在多数据集上超越单模型性能。

**[MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning](midas_misalignment-based_data_augmentation_strategy_for_imbalanced_multimodal_le.md)**

:   首次提出将跨模态不对齐样本作为有监督训练信号（而非噪声/干扰）来缓解多模态学习中的模态不平衡问题，设计 MIDAS 数据增强框架：通过置信度标注不对齐样本 + 弱模态加权 + 难样本加权三重机制，在四个多模态分类基准上显著超越现有方法。

**[Mint: A Simple Test-Time Adaptation of Vision-Language Models against Common Corruptions](mint_a_simple_testtime_adaptation_of_visionlanguage_models_a.md)**

:   发现 CLIP 在图像损坏下的性能退化根源在于**嵌入方差坍缩**——类内与类间方差同步缩小导致嵌入空间判别性丧失；提出 Mint，通过最大化伪标签类间方差（PL-inter）在线修复嵌入几何，仅凭均值累加器和梯度累加器两个极简组件即可在 BS=1 的在线场景下稳定提升 CLIP 在多种损坏基准上的分类精度，同时比最强 baseline 快 45 倍。

**[Mirage A Benchmark For Multimodal Information-Seeking And Reasoning In Agricultu](mirage_a_benchmark_for_multimodal_information-seeking_and_reasoning_in_agricultu.md)**

:   MIRAGE 是首个基于真实农业专家咨询对话（35,000+条）构建的多模态基准，评估视觉语言模型在领域级实体识别、因果推理和"澄清还是回答"决策方面的能力，揭示了即使 GPT-4.1 识别准确率也仅 43.9% 的严峻挑战。

**[MM-OPERA: Benchmarking Open-ended Association Reasoning for Large Vision-Language Models](mm-opera_benchmarking_open-ended_association_reasoning_for_large_vision-language.md)**

:   提出 MM-OPERA，一个包含 11,497 实例的开放式联想推理基准，通过远程物品关联（RIA）和上下文关联（ICA）两大任务评估 LVLM 的关联推理能力，配套设计了 LLM-as-a-Judge 评分策略和过程奖励评估方法，揭示当前最强 LVLM 仍显著落后于人类。

**[MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios](mme-videoocr_evaluating_ocr-based_capabilities_of_multimodal_llms_in_video_scena.md)**

:   提出 MME-VideoOCR，一个包含 25 个任务、44 个场景、1464 个视频和 2000 个人工标注 QA 对的视频 OCR 综合评估基准，涵盖文本识别、理解和推理三个层次。评估 18 个 SOTA MLLM 揭示最强模型（Gemini-2.5 Pro）仅达 73.7%，跨帧理解任务低至 25% 以下。

**[MMLongBench: Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly](mmlongbench_benchmarking_longcontext_visionlanguage_models_e.md)**

:   构建首个全面的长上下文视觉语言模型（LCVLM）评估基准 MMLongBench——13,331 个样本覆盖 5 类下游任务、混合图像类型、5 级标准化输入长度（8K-128K tokens），评估 46 个模型后发现单任务性能是整体能力的弱代理，且强推理能力与长上下文性能正相关。

**[Multimodal Bandits: Regret Lower Bounds and Optimal Algorithms](multimodal_bandits_regret_lower_bounds_and_optimal_algorithms.md)**

:   针对奖励函数至多有 $m$ 个极值的多模态多臂赌博机问题，提出首个计算可行的算法求解 Graves-Lai 优化问题，实现渐近最优的遗憾界，并证明局部搜索策略是次优的。

**[On the Value of Cross-Modal Misalignment in Multimodal Representation Learning](on_the_value_of_cross-modal_misalignment_in_multimodal_representation_learning.md)**

:   提出潜变量模型将跨模态失配形式化为选择偏差和扰动偏差两种机制，理论证明MMCL学到的表征恰好捕获与两种偏差无关的不变语义子集，统一了"失配有害/有益"两种对立观点。

**[Partial Information Decomposition Via Normalizing Flows In Latent Gaussian Distr](partial_information_decomposition_via_normalizing_flows_in_latent_gaussian_distr.md)**

**[Praxis-VLM: Vision-Grounded Decision Making via Text-Driven Reinforcement Learning](praxisvlm_visiongrounded_decision_making_via_textdriven_rein.md)**

:   发现VLM的决策推理能力可以与视觉感知解耦——用文本描述替代图像时决策性能不降反升，据此提出Praxis-VLM：在纯文本场景上用GRPO训练决策推理能力，然后零样本迁移到视觉输入推理，在VIVA/PCA-Bench/EgoNormia三个决策benchmark上超越SFT基线且泛化性更强。

**[PrefixKV: Adaptive Prefix KV Cache is What Vision Instruction-Following Models Need for Efficient Generation](prefixkv_adaptive_prefix_kv_cache_is_what_vision_instruction.md)**

:   提出 PrefixKV，将 LVLM 各层 KV 缓存大小的确定转化为搜索最优全局前缀配置的问题，通过二分搜索找到信息保留阈值实现自适应逐层 KV 保留，在 20% 压缩率下仍保持接近原模型性能，提供 1.8× 推理加速。

**[Rethinking Multimodal Learning from the Perspective of Mitigating Classification Ability Disproportion](rethinking_multimodal_learning_from_the_perspective_of_mitig.md)**

:   提出"**分类能力不均衡**"视角理解多模态学习中的模态不平衡，设计 Sustained Boosting 算法（共享编码器 + 多可配置分类器，同时优化分类和残差误差）配合自适应分类器分配（ACA），理论证明跨模态 gap loss 以 $\mathcal{O}(1/T)$ 收敛，在 CREMAD 等 6 个数据集上大幅超越 SOTA。

**[Roborefer Towards Spatial Referring With Reasoning In Vision-Language Models For](roborefer_towards_spatial_referring_with_reasoning_in_vision-language_models_for.md)**

:   提出 **RoboRefer**，一个 3D 感知的推理型 VLM，通过 **SFT + RFT** 两阶段训练策略（含度量敏感的过程奖励函数），在空间指代任务中实现精确的单步空间理解和多步空间推理，在 RefSpatial-Bench 上超越 Gemini-2.5-Pro 达 17.4%。

**[Sherlock: Self-Correcting Reasoning in Vision-Language Models](sherlock_selfcorrecting_reasoning_in_visionlanguage_models.md)**

:   首个系统研究VLM推理自纠正能力的框架：发现现有推理VLM几乎不能自纠正（<10%出现aha moment），提出Sherlock三阶段训练框架（SFT冷启动→离线轨迹级偏好学习→在线自我迭代）仅用20K标注数据超越使用100K-260K数据的LLaVA-CoT/Mulberry/LlamaV-o1。

**[Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models](sparse_autoencoders_learn_monosemantic_features_in_visionlan.md)**

:   将Sparse Autoencoder (SAE)从LLM可解释性扩展到VLM领域，提出MonoSemanticity Score (MS)量化视觉神经元的单义性，发现SAE能将VLM中多义的神经元分解为单义特征，且可直接通过操控单个SAE神经元来steering LLaVA的输出（插入或抑制概念），无需修改LLM。

**[SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning](srpo_enhancing_multimodal_llm_reasoning_via_reflection-aware_reinforcement_learn.md)**

:   提出 SRPO（Self-Reflection enhanced reasoning with Group Relative Policy Optimization），一个两阶段反思感知 RL 框架：第一阶段用大模型生成反思数据做 SFT cold-start，第二阶段设计反思感知奖励函数在 GRPO 中强化简洁有效的自我反思能力，在 MathVista/MathVision/MMMU-Pro 等多模态推理基准上以 7B/32B 模型显著超越同规模 SOTA。

**[The Illusion of Progress? A Critical Look at Test-Time Adaptation for Vision-Language Models](the_illusion_of_progress_a_critical_look_at_testtime_adaptat.md)**

:   提出TTA-VLM benchmark，在统一实验条件下评估8种episodic和7种online测试时适应(TTA)方法在15个数据集上的表现，发现三个令人意外的结论：(1) 现有TTA方法相比早期TPT基线提升有限；(2) TTA与训练时微调方法协作效果差；(3) 准确率提升以牺牲校准、OOD检测和鲁棒性为代价。

**[The Narrow Gate: Localized Image-Text Communication in Native Multimodal Models](the_narrow_gate_localized_imagetext_communication_in_native.md)**

:   发现原生多模态VLM（如Chameleon、Emu3）中图像到文本的跨模态信息传递竟然集中在单一的end-of-image [EOI] token上（"narrow gate"机制），而非原生VLM（如LLaVA）则通过多个图像token分布式传递信息；删除[EOI]的attention可导致native模型性能崩溃，而修改[EOI]表示可精确控制模型的语义输出。

**[TRoVe: Discovering Error-Inducing Static Feature Biases in Temporal Vision-Language Models](trove_discovering_errorinducing_static_feature_biases_in_tem.md)**

:   TRoVe 提出一个自动化诊断框架，用于发现 temporal VLM 在时序理解任务中错误依赖的静态特征偏置；它通过从验证集提取候选静态特征，并同时评估这些特征对错误率的影响与模型对其依赖程度，在 101 个带偏置真值标注的 temporal VLM 上较最强基线提升 28.6%，还能进一步辅助 test-time 改善模型表现。

**[Unveiling Chain of Step Reasoning for Vision-Language Models with Fine-grained Rewards](unveiling_chain_of_step_reasoning_for_visionlanguage_models.md)**

:   提出Chain-of-Step (CoS)推理框架：将VLM的推理链分解为结构化步骤（Name+Thought+Reflection），训练Process Reward Model (PRM)提供步骤级精细奖励，通过迭代DPO和step-level beam search显著提升VLM推理能力——在InternVL-2.5-MPO-8B上平均提升4.0%达到73.4%，并揭示"对VLM而言推理质量比长度更重要"。

**[VL-SAE: Interpreting and Enhancing Vision-Language Alignment with a Unified Concept Set](vlsae_interpreting_and_enhancing_visionlanguage_alignment_wi.md)**

:   提出VL-SAE，一种带有距离编码器和模态特定解码器的稀疏自编码器，将视觉和语言表示的语义映射到统一概念集，从而解释和增强VLM的视觉-语言对齐机制，在零样本分类平均提升0.6-0.9%，在POPE幻觉消除上超越专用方法VCD。
