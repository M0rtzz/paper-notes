<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**🔬 ICLR2026** · 共 **120** 篇

**[A Cortically Inspired Architecture for Modular Perceptual AI](a_cortically_inspired_architecture_for_modular_perceptual_ai.md)**

:   从神经科学出发提出皮层启发的模块化感知 AI 架构蓝图，包含专用编码器、共享跨模态潜空间、路由控制器和递归预测反馈回路四个组件，并通过稀疏自编码器实验验证模块化分解可提升域内特征稳定性 (+15.4pp Jaccard 重叠)。

**[ASIDE: Architectural Separation of Instructions and Data in Language Models](aside_architectural_separation_of_instructions_and_data_in_language_models.md)**

:   提出 ASIDE，一种在 token embedding 层面通过正交旋转区分指令和数据的架构级改造，仅需修改前向传播并在标准指令微调数据上训练，即可显著提升指令-数据分离度和 prompt injection 鲁棒性，无需任何安全专项训练。

**[AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer](assetformer_modular_3d_assets_generation_with_autoregressive_transformer.md)**

:   提出 AssetFormer，基于 Llama 架构的自回归 Transformer，将模块化 3D 资产（由 primitive 序列组成）建模为离散 token 序列，通过 DFS/BFS 图遍历重排序和联合词汇表解码实现从文本描述生成可直接用于游戏引擎的模块化 3D 资产。

**[ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality](atlas_adaptive_transfer_scaling_laws_for_multilingual_pretraining_finetuning_and.md)**

:   提出 Adaptive Transfer Scaling Law (ATLAS)，通过将有效数据量分解为目标语言、迁移语言和其他语言三项并引入数据重复饱和函数，在774个多语言训练实验（10M–8B参数、400+语言）上显著优于现有scaling law（多语言 $R^2$ 从0.67提升至0.98），并系统量化了跨语言迁移矩阵、多语言诅咒的容量约束以及预训练vs微调的计算交叉点。

**[Attributing Response to Context: A Jensen-Shannon Divergence Driven Mechanistic Study of Context Attribution in Retrieval-Augmented Generation](attributing_response_to_context_a_jensen-shannon_divergence_driven_mechanistic_s.md)**

:   提出ARC-JSD方法，通过计算完整上下文与逐句消融上下文下的响应分布的Jensen-Shannon散度，在无需微调、梯度计算或代理模型的情况下实现高效精准的RAG上下文归因，并结合Logit Lens进行机制分析，定位负责上下文归因的注意力头和MLP层，通过门控操作降低约39%的幻觉率。

**[Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution](auditing_cascading_risks_in_multi-agent_systems_via_semanti-geometric_co-evolut.md)**

:   提出 SCCAL 框架，通过耦合语义流（semantic flow）和交互图的 Ollivier–Ricci 曲率（ORC）来建模多智能体系统中语义-几何的协同演化，利用两者的一致性残差作为级联风险的早期预警信号，在语义违规显现前数轮即可检测异常。

**[Benchmarking Overton Pluralism in LLMs](benchmarking_overton_pluralism_in_llms.md)**

:   提出 OvertonBench 框架，通过大规模人类研究（1208名美国代表性参与者、60个主观问题、8个LLM）将 Overton 多元主义形式化为集合覆盖度指标 OvertonScore，发现当前所有模型得分仅 0.35–0.41（理论上限为 1.0），并构建了与人类判断高度相关（ρ=0.88）的自动化评测工具。

**[BiasFreeBench: a Benchmark for Mitigating Bias in Large Language Model Responses](biasfreebench_a_benchmark_for_mitigating_bias_in_large_language_model_responses.md)**

:   本文构建了 BiasFreeBench 基准，首次在统一框架下系统比较 8 种主流去偏方法（4 种 prompting + 4 种 training），聚焦于 LLM 响应层面的偏差评估，并提出了 Bias-Free Score 指标，发现 prompting 方法（尤其是 CoT）整体优于 training 方法，而 DPO 在跨偏差类型泛化上表现突出。

**[Breaking the Correlation Plateau: On the Optimization and Capacity Limits of Attention-Based Regressors](breaking_the_correlation_plateau_on_the_optimization_and_capacity_limits_of_atte.md)**

:   本文首次从理论上分析了注意力回归模型在联合 MSE+PCC 训练时出现的"PCC平台期"现象——发现其根源在于 MSE 优化与 PCC 梯度之间的冲突以及 softmax 凸聚合的表达力上界——并提出 ECA（Extrapolative Correlation Attention）框架，通过缩放残差聚合、色散感知温度 softmax 和色散归一化 PCC 损失三个组件突破该限制。

**[Closing the Curvature Gap: Full Transformer Hessians and Their Implications for Scaling Laws](closing_the_curvature_gap_full_transformer_hessians_and_their_implications_for_s.md)**

:   首次推导完整 Transformer block（含 LayerNorm 和 FFN）的显式 Hessian 表达式及谱范数上界，建立了损失面随数据量增加以 $O(1/k)$ 速率收敛的理论框架，为 scaling laws 和曲率感知训练提供了数学基础。

**[Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training](common_corpus_ethical_data_for_llm_pretraining.md)**

:   构建 Common Corpus——约 2 万亿 token 的最大规模合法授权 LLM 预训练数据集，覆盖 6 大集合（政府/文化/科学/代码/Web/语义），多语言（含低资源语言），所有数据均为无版权或宽松许可来源，配有完整数据溯源和多阶段过滤管道，已被 Anthropic 等行业领导者采用。

**[Compositional-ARC: Assessing Systematic Generalization in Abstract Spatial Reasoning](compositional-arc_assessing_systematic_generalization_in_abstract_spatial_reason.md)**

:   提出 Compositional-ARC 数据集评估模型在抽象空间推理中的系统性泛化能力——从已知基础几何变换（如平移、旋转）泛化到未见过的变换组合。一个仅 5.7M 参数的 MLC 训练的 encoder-decoder 模型在系统性任务上达到 78.26%，与 ARC Prize 2024 冠军的 8B 模型+TTT 持平，远超 GPT-4o、o3-mini 等（<3%）。

**[Conformal Prediction Adaptive to Unknown Subpopulation Shifts](conformal_prediction_adaptive_to_unknown_subpopulation_shifts.md)**

:   针对子群体偏移（subpopulation shift）下标准 conformal prediction 失效的问题，提出三种自适应算法：利用学习的 domain classifier 加权校准数据（Algorithm 1/2）或利用嵌入相似度加权（Algorithm 3），在不完美甚至无 domain 标签的情况下仍能保证覆盖率，并应用于视觉分类和 LLM 幻觉检测。

**[CounselBench: A Large-Scale Expert Evaluation and Adversarial Benchmarking of LLMs in Mental Health QA](counselbench_llm_mental_health_qa.md)**

:   联合100名持证心理健康专家构建CounselBench双组件基准——CounselBench-EVAL（2,000条六维度专家评估）和CounselBench-Adv（120个对抗性问题+1,080条响应标注），系统性揭示LLM在心理健康开放式问答中表面得分高但存在过度泛化、擅自医疗建议等安全隐患，同时证明LLM-as-Judge在安全关键领域严重不可靠。

**[d²Cache: Accelerating Diffusion-Based LLMs via Dual Adaptive Caching](d2cache_accelerating_diffusion-based_llms_via_dual_adaptive_caching.md)**

:   提出 d²Cache，一种面向 Diffusion-based LLM（dLLM）的无训练近似 KV 缓存框架，通过确定性先验引导的 masked token 选择 + 注意力感知的非 mask token 选择两阶段策略，实现 4.1× 推理加速同时提升生成质量。

**[DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science](dare-bench_evaluating_modeling_and_instruction_fidelity_of_llms_in_data_science.md)**

:   DARE-bench 是一个面向数据科学任务的大规模可验证基准，包含 6300 个 Kaggle 衍生任务，支持 ML 建模和指令遵循两类评估，提供训练集支持 SFT 和 RL——SFT 将 Qwen3-32B 提升 1.83×，RL 将 Qwen3-4B 提升 8× 以上。

**[DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-size Canvas](dreamon_diffusion_language_models_for_code_infilling_beyond_fixed-size_canvas.md)**

:   DreamOn 通过引入 [expand] 和 [delete] 两个特殊状态解决了扩散语言模型（DLM）的固定长度生成限制，无需架构修改即可实现变长代码填充，在 HumanEval-Infilling 上比扩散基线平均提升 26.4%，达到与 SOTA 自回归模型持平的水平。

**[DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models](dro-instructzero_distributionally_robust_prompt_optimization_for_instruction_fol.md)**

:   将分布鲁棒优化（DRO）引入贝叶斯优化框架以实现零样本指令优化，使优化后的指令在分布偏移和对抗性评估条件下仍保持可靠性能。

**[DRO-InstructZero: Distributionally Robust Prompt Optimization for Large Language Models](dro-instructzero_distributionally_robust_prompt_optimization_for_large_language_.md)**

:   将分布鲁棒优化（DRO）引入 InstructZero 的贝叶斯优化框架，通过在 f-divergence 球定义的模糊集上最大化最坏情况期望效用，使自动搜索得到的 prompt 在分布偏移下仍能保持可靠性能。

**[EAMET: Robust Massive Model Editing via Embedding Alignment Optimization](eamet_robust_massive_model_editing_via_embedding_alignment_optimization.md)**

:   发现大规模模型编辑失败的根本原因是 key embedding 和 residual embedding 之间的结构不一致（embedding misalignment），提出 EAMET 通过 KL+MSE 双损失渐进式对齐优化，在 6 个 LLM 上平均提升编辑成功率 14%（CounterFact）。

**[ELLMob: Event-Driven Human Mobility Generation with Self-Aligned LLM Framework](ellmob_event-driven_human_mobility_generation_with_self-aligned_language_models.md)**

:   提出 ELLMob 框架，基于认知心理学的模糊痕迹理论（FTT），通过提取并迭代对齐"习惯 gist"和"事件 gist"来调和用户日常模式与社会事件约束之间的竞争，实现事件驱动的可解释轨迹生成。

**[ELLMob: Event-Driven Human Mobility Generation with Self-Aligned LLM Framework](ellmob_event-driven_human_mobility_generation_with_self-aligned_llm_framework.md)**

:   提出 ELLMob，一个基于模糊痕迹理论（FTT）的自对齐 LLM 框架，通过提取并迭代对齐"习惯模式要旨"与"事件约束要旨"来生成兼顾日常规律与事件响应的人类移动轨迹。

**[Emergent Misalignment is Easy, Narrow Misalignment is Hard](emergent_misalignment_is_easy_narrow_misalignment_is_hard.md)**

:   研究发现在窄域有害数据上微调会造成广域错位（emergent misalignment），因为"通用错位"比"仅在特定域错位"是更简单高效的参数空间解——通用解的参数范数更小且对噪声更稳定。

**[Enabling Fine-Grained Operating Points for Black-Box LLMs](enabling_fine-grained_operating_points_for_black-box_llms.md)**

:   发现黑盒 LLM 的语言化概率仅输出 16-23 个唯一值（低基数问题），导致 PR/ROC 曲线粗糙无法精细调优；通过注入参数化噪声和可选的 MLP 校正，将唯一值从 16 个提升到 20,000+，在仅需 1-2 次 API 调用的条件下达到 20 次采样的性能。

**[Enhancing Hallucination Detection through Noise Injection](enhancing_hallucination_detection_through_noise_injection.md)**

:   在 LLM 中间层的 MLP 激活中注入均匀噪声来近似贝叶斯后验，捕获认知不确定性（epistemic uncertainty），与采样温度捕获的偶然不确定性（aleatoric uncertainty）互补，将 GSM8K 上的幻觉检测 AUROC 从 71.56 提升到 76.14。

**[Enhancing Persona Following at Decoding Time via Dynamic Importance-Guided Token Estimation for Role-Playing Agents](enhancing_persona_following_at_decoding_time_via_dynamic_importance-guided_token.md)**

:   提出 Persona Dynamic Decoding (PDD) 框架，通过条件互信息动态估计人格属性的场景依赖重要性，并将重要性分数整合到多目标奖励引导解码中，实现无需微调的推理时人格跟随。

**[Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents](enhancing_persona_following_at_decoding_time_via_dynamic_importance_estimation_.md)**

:   提出 Persona Dynamic Decoding (PDD) 框架，通过条件互信息动态估计人格属性的场景相关重要性，并以加权多目标奖励引导解码，实现无需微调的推理时自适应人格跟随。

**[Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents](enhancing_persona_following_at_decoding_time_via_dynamic_importance_estimation_f.md)**

:   提出 PDD（Persona Dynamic Decoding）框架，通过条件互信息动态估计不同场景下人设属性的重要性，并以加权多目标奖励引导推理时解码，实现无需微调的自适应人设遵循。

**[Evaluating Text Creativity across Diverse Domains: A Dataset and Large Language Model Evaluator](evaluating_text_creativity_across_diverse_domains_a_dataset_and_large_language_m.md)**

:   提出基于上下文感知的成对比较框架来评估文本创造力，构建了包含 100K+ 人类级别和 1M+ 合成数据的 CreataSet 数据集，训练出 CrEval 评估器，在与人类判断的对齐度上超越 GPT-4o 达 18.7%。

**[EvoEngineer: Mastering Automated CUDA Kernel Code Evolution with Large Language Models](evoengineer_mastering_automated_cuda_kernel_code_evolution_with_large_language_m.md)**

:   提出 EvoEngineer，首个系统化的 LLM-based 代码演化框架，将代码演化分解为 traverse technique（含两层设计：solution guiding + prompt engineering）和 population management 两个正交组件，在 91 个真实 CUDA kernel 上实现最高 2.72× 中位加速比和 69.8% 代码有效率，在性能和正确性两个维度上超越现有方法。

**[Evolution of Concepts in Language Model Pre-Training](evolution_of_concepts_in_language_model_pre-training.md)**

:   首次将 crosscoders（跨快照稀疏字典学习）应用于追踪语言模型预训练过程中特征的涌现和演化，发现预训练存在"统计学习→特征学习"两阶段相变，并通过归因分析将微观特征演化与宏观下游任务指标因果关联。

**[FictionalQA: A Dataset for Studying Memorization and Knowledge Acquisition](fictionalqa_a_dataset_for_studying_memorization_and_knowledge_acquisition.md)**

:   提出 FictionalQA 数据集及生成管线，通过合成关于虚构事件的 webtext 风格文档和 QA 对，在受控环境下研究 LLM 训练中事实记忆与逐字记忆的双重过程，发现更多样的表面形式有助于知识获取而简洁的结构化列表反而最不利于泛化。

**[Fine-Grained Activation Steering: Steering Less, Achieving More](fine-grained_activation_steering_steering_less_achieving_more.md)**

:   AUSteer 发现块级激活转向（steering）本质上是异质的——不同维度控制不同 token 分布，混合转向既放大有益信号也放大有害信号。提出原子单元（AU）级细粒度转向：用激活动量定位判别性维度，自适应调节转向强度，仅转向 ≤100 个维度即大幅超越转向数千维度的 SOTA 方法。

**[Fine-tuning Done Right in Model Editing](fine-tuning_done_right_in_model_editing.md)**

:   揭示模型编辑中 fine-tuning 被低估的根因是错误的训练 pipeline（深度优先逐样本优化），修正为标准的广度优先 mini-batch 训练后，配合局部化参数调优形成 LocFT-BF，首次支持 10 万次连续编辑和 72B 模型规模。

**[First is Not Really Better Than Last: Evaluating Layer Choice and Aggregation Strategies in Language Model Data Influence Estimation](first_is_not_really_better_than_last_evaluating_layer_choice_and_aggregation_str.md)**

:   通过理论和实验证明先前工作所推崇的"第一层（embedding）最适合做 influence estimation"的结论是不可靠的，发现中间 attention 层才是更好的估计层，并提出 Rank 和 Vote 两种新的跨层聚合策略以及 Noise Detection Rate (NDR) proxy 指标，显著改善了 LLM 中有害训练样本的检测效果。

**[FlexiCodec: A Dynamic Neural Audio Codec for Low Frame Rates](flexicodec_a_dynamic_neural_audio_codec_for_low_frame_rates.md)**

:   提出 FlexiCodec，通过 ASR 特征引导的动态帧率合并策略，在 3–12.5Hz 超低帧率下实现高质量语音编解码，同时保持优异的语义信息保留能力。

**[From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning](from_assumptions_to_actions_turning_llm_reasoning_into_uncertainty-aware_plannin.md)**

:   提出 PCE（Planner-Composer-Evaluator）框架，将 LLM 推理链中隐含的环境假设显式提取并组织为决策树，通过似然度-增益-成本评分实现不确定性感知的行动选择，大幅减少多智能体协作中的通信开销。

**[Function Induction and Task Generalization: An Interpretability Study with Off-by-One Addition](function_induction_and_task_generalization_an_interpretability_study_with_off-by.md)**

:   通过 off-by-one addition（如 1+1=3, 2+2=5）这一反事实任务，利用 path patching 发现大语言模型内部存在 **function induction** 机制——一种超越 token 级别 pattern matching、在函数级别进行归纳推理的注意力头电路，并证明该机制可跨任务复用。

**[Functional Embeddings Enable Aggregation of Multi-Area SEEG Data for Robust BCI](functional_embeddings_enable_aggregation_of_multi-area_seeg_data_for_robust_bci.md)**

:   提出 FunctionalMap 框架，通过对比学习从颅内局部场电位（LFP）中学习被试无关的功能嵌入作为"功能坐标系"，替代不可靠的 MNI 解剖坐标，结合 Transformer 实现跨被试、跨电极的神经数据聚合和信号重建，在 20 名被试的多脑区 SEEG 数据集上验证有效。

**[Functional Embeddings Enable Aggregation of Multi-Area SEEG Data for Robust BCI](functional_embeddings_enable_aggregation_of_multi-area_seeg_recordings_over_subj.md)**

:   提出 FunctionalMap 框架，通过对比学习从颅内局部场电位（LFP）中学习被试无关的功能嵌入作为"功能坐标系"，替代不可靠的 MNI 解剖坐标，结合 Transformer 实现跨被试、跨电极的神经数据聚合和信号重建，在 20 名被试的多脑区 SEEG 数据集上验证有效。

**[GAVEL: Towards Rule-Based Safety through Activation Monitoring](gavel_towards_rule-based_safety_through_activation_monitoring.md)**

:   提出 GAVEL 框架，将 LLM 安全从"粗粒度误用数据集训练分类器"范式转向"可组合认知元素 (CE) + 布尔规则"范式：定义可解释的激活级原语（如"发出威胁"、"处理支付"），组合为精确的策略规则，实现高精度、可定制、可审计的实时安全监控。

**[Generative Value Conflicts Reveal LLM Priorities](generative_value_conflicts_reveal_llm_priorities.md)**

:   提出 ConflictScope，一个自动生成价值冲突场景的 pipeline，通过开放式评估（非选择题）揭示 LLM 在冲突情境下的价值优先级排序，发现模型在开放式设置中从保护性价值（如无害性）转向个人价值（如用户自主性），且系统提示可将目标排序对齐提升 14%。

**[Hidden Breakthroughs in Language Model Training](hidden_breakthroughs_in_language_model_training.md)**

:   提出 POLCA 方法，将训练损失沿低秩训练子空间的任意基方向进行分解，揭示了在整体损失曲线平滑区域中隐藏的概念性突破（hidden breakthroughs），实现了对模型技能习得过程的无监督可解释性分析。

**[Hierarchical Concept-based Interpretable Models](hierarchical_concept-based_interpretable_models.md)**

:   HiCEMs引入层级概念嵌入模型，通过Concept Splitting方法在预训练CEM的嵌入空间中自动发现细粒度子概念（无需额外标注），构建层级概念结构，使模型能在不同粒度层次进行测试时概念干预以提升任务性能。

**[How Catastrophic is Your LLM? Certifying Risk in Conversation](how_catastrophic_is_your_llm_certifying_risk_in_conversation.md)**

:   提出 C3LLM（Certification of Catastrophic risks in multi-turn Conversation for LLMs），首个为多轮 LLM 对话中灾难性风险提供统计认证的框架：用语义相似度图上的 Markov 过程建模对话分布，定义 3 种对话采样策略 + 增强层，使用 Clopper-Pearson 95% 置信区间认证模型产生有害输出的概率界——发现最差模型风险下界高达 72%。

**[How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Understanding](how_do_transformers_learn_to_associate_tokens_gradient_leading_terms_bring_mecha.md)**

:   通过对训练梯度的前导项近似分析，推导出Transformer在训练早期阶段各权重矩阵的闭式表达——均可分解为三种基函数（bigram、token-interchangeability、context mapping）的简单组合——从而揭示Transformer如何从自然语言数据中学习"bird"↔"flew"这类语义关联，且理论预测与真实LLM的学到权重高度吻合。

**[How Far Are LLMs from Professional Poker Players? Revisiting Game-Theoretic Reasoning with Agentic Tool Use](how_far_are_llms_from_professional_poker_players_revisiting_game-theoretic_reaso.md)**

:   系统分析了 LLM 在扑克中的三大推理缺陷（启发式推理、事实误解、知行差距），提出 ToolPoker 框架——首个面向不完全信息博弈的工具集成 LLM 推理系统，通过外部 CFR solver 提供博弈论最优的行动指导，使 7B 模型在 Limit Hold'em 中逼近 Nash 均衡。

**[How Reliable is Language Model Micro-Benchmarking?](how_reliable_is_language_model_micro-benchmarking.md)**

:   提出 Minimum Detectable Ability Difference (MDAD) 元评估指标，系统揭示了 micro-benchmark 在极小规模下无法可靠区分性能差距小的模型对，且当样本量达到 ~250 时随机采样与精心设计的 micro-benchmark 方法表现相当。

**[HUME: Measuring the Human-Model Performance Gap in Text Embedding Tasks](hume_measuring_the_human-model_performance_gap_in_text_embedding_tasks.md)**

:   提出 HUME 框架，首次系统测量人类在文本嵌入任务（重排序、分类、聚类、语义相似度）上的表现，为 MTEB 建立人类性能基线，发现人类总体排名第 4（77.6 vs 模型最佳 80.1），并揭示了多个数据集的质量问题。

**[Identifying and Evaluating Inactive Heads in Pretrained LLMs](identifying_and_evaluating_inactive_heads_in_pretrained_llms.md)**

:   系统评估 12 种评分函数来识别 LLM 中不活跃的注意力头，发现平均头输出范数（Avg Head Output Norm）比传统注意力权重指标更能模型无关地识别不活跃头；14 个模型上验证平均超过 12% 的头可被置零而保持 MMLU 精度在 1% 以内。

**[Imagine How To Change: Explicit Procedure Modeling for Change Captioning](imagine_how_to_change_explicit_procedure_modeling_for_change_captioning.md)**

:   提出 ProCap 框架，将变化描述从静态图像对比较重新定义为动态过程建模：第一阶段通过帧插值和掩码重建训练过程编码器学习时空变化动力学，第二阶段用可学习过程查询隐式推断变化过程，在三个数据集上超越 SOTA。

**[Implicit Statistical Inference in Transformers: Approximating Likelihood-Ratio Tests In-Context](implicit_statistical_inference_in_transformers_approximating_likelihood-ratio_te.md)**

:   从统计决策论视角出发，证明Transformer在上下文学习中能近似Bayes最优的**似然比检验**充分统计量，并通过机制分析揭示模型对线性/非线性任务采用不同深度的自适应电路。

**[In-Context Algebra](in-context_algebra.md)**

:   本文设计了一个 **in-context 代数任务**——令 token 成为纯变量、每条序列重新随机分配含义——发现 Transformer 在此设定下不再学习经典的傅里叶/几何表示，而是涌现出三种 **符号推理机制**（交换复制、单位元识别、闭包消去），并揭示了训练过程中这些能力按阶段性相变依次出现的规律。

**[In-Context Learning of Temporal Point Processes with Foundation Inference Models](in-context_learning_of_temporal_point_processes_with_foundation_inference_models.md)**

:   提出 FIM-PP——首个面向时间点过程的基础推断模型，通过在大规模合成 MTPP 数据上预训练 Transformer，实现对条件强度函数的上下文学习推断，零样本即可匹配专用模型性能，微调后在多个真实数据集上达到 SOTA。

**[KVComm: Enabling Efficient LLM Communication through Selective KV Sharing](kvcomm_enabling_efficient_llm_communication_through_selective_kv_sharing.md)**

:   提出 KVComm 框架通过选择性共享 KV pairs 实现 LLM 间高效通信，发现 hidden states 存在"信息集中偏差"使其不适合跨模型传递，设计基于注意力重要性 + 高斯先验的层选择策略，仅传输 30% 层即可超越大多数 baseline。

**[LH-Deception: Simulating and Understanding LLM Deceptive Behaviors in Long-Horizon Interactions](lh-deception_simulating_and_understanding_llm_deceptive_behaviors_in_long-horizo.md)**

:   提出首个长时域 LLM 欺骗行为仿真框架 LH-Deception，通过执行者-监督者多智能体系统 + 概率事件机制 + 独立欺骗审计，在 11 个前沿模型上系统量化了欺骗行为的频率、严重性、类型及其对信任的侵蚀。

**[Lifelong Learning with Behavior Consolidation for Vehicle Routing](lifelong_learning_with_behavior_consolidation_for_vehicle_routing.md)**

:   提出 LLR-BC——面向神经 VRP 求解器的终身学习框架，通过置信度感知经验加权（CaEW）和决策寻求行为巩固（DsBC），在分布和规模变化的任务序列上有效缓减灾难性遗忘、保持可塑性并提升零样本泛化。

**[LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery](llema_evolutionary_search_with_llms_for_multi-objective_material_design.md)**

:   提出 LLEMA 框架，将 LLM 的科学知识与化学规则引导的进化搜索和记忆驱动的迭代优化相结合，在 14 个多目标材料发现任务上实现了更高的命中率、稳定性和 Pareto 前沿质量。

**[LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery](llema_evolutionary_search_with_llms_for_multi-objective_materials_discovery.md)**

:   提出 LLEMA 框架，将 LLM 的科学先验知识与化学规则引导的进化搜索和记忆驱动的迭代优化相结合，在 14 个多目标材料发现任务上显著超越生成式和纯 LLM 基线。

**[Meta-RL Induces Exploration in Language Agents](meta-rl_induces_exploration_in_language_agents.md)**

:   提出 LaMer 框架，将元强化学习（Meta-RL）引入 LLM agent 训练，通过跨 episode 的奖励优化和基于反思的上下文策略适应，使语言智能体学会主动探索环境，在 Sokoban/MineSweeper/Webshop 上分别获得 11%/14%/19% 的绝对性能提升。

**[Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses](multi-llm_adaptive_conformal_inference_for_reliable_llm_responses.md)**

:   提出 MACI（Multi-LLM Adaptive Conformal Inference），通过**累积乘积型 conformity score** + **多 LLM 集成**的 factuality 评分 + **组条件校准**，在严格保证用户指定错误率的同时，显著提升 LLM 回复中事实性声明的保留率。

**[Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](narrow_finetuning_leaves_clearly_readable_traces_in_activation_differences.md)**

:   发现窄域微调（narrow finetuning）在 LLM 激活中留下清晰可读的痕迹：即使在无关文本的前几个 token 上，微调前后模型的激活差异也编码了微调目标的语义信息。通过 Activation Difference Lens（ADL）方法，可解释性 agent 识别微调目标的成功率达 91%，比黑盒基线高 2 倍以上。

**[Near-Optimal Online Deployment and Routing for Streaming LLMs](near-optimal_online_deployment_and_routing_for_streaming_llms.md)**

:   首次形式化 LLM 流式在线部署+路由联合问题：新模型持续出现、旧模型可能过时，在并发部署上限 $M_{\max}$ 和成本预算约束下，提出 StageRoute 分层算法，证明 $\tilde{\mathcal{O}}(T^{2/3})$ 遗憾界并给出匹配下界，达到近最优。

**[Neural Synchrony Between Socially Interacting Language Models](neural_synchrony_between_socially_interacting_language_models.md)**

:   首次研究社会交互中 LLM 间的神经同步现象：通过训练仿射变换预测交互伙伴的未来表征，定义 $SyncR^2$ 指标量化同步强度，发现该同步依赖于社会参与和时间邻近性，且与 LLM 的社会行为表现高度相关（Pearson $r$ = 0.88-0.99），呼应了人类脑间同步（IBS）的神经科学发现。

**[Noise Stability of Transformer Models](noise_stability_of_transformer_models.md)**

:   提出噪声稳定性（noise stability）替代平均敏感度（average sensitivity）作为衡量 Transformer 简单性偏差的更优指标，并基于此设计正则化方法，在合成任务和语言建模上分别加速训练约 35% 和 75%。

**[Optimas: Optimizing Compound AI Systems with Globally Aligned Local Rewards](optimas_optimizing_compound_ai_systems_with_globally_aligned_local_rewards.md)**

:   提出 Optimas 框架，为复合 AI 系统中每个组件维护一个与全局奖励对齐的局部奖励函数（LRF），使异构组件（prompt、模型参数、超参数、模型选择）可独立优化，在五个真实系统上平均提升 11.92%。

**[Pre-training LLM without Learning Rate Decay Enhances Supervised Fine-Tuning](pre-training_llm_without_learning_rate_decay_enhances_supervised_fine-tuning.md)**

:   提出 Warmup-Stable-Only (WSO) 学习率调度策略——在预训练中完全去掉学习率衰减阶段，虽然预训练指标较差，但在 SFT 后一致性地超越所有衰减策略，通过损失景观分析揭示 WSO 保持更平坦的极小值区域是其优势根源。

**[Predicting LLM Reasoning Performance with Small Proxy Model](predicting_llm_reasoning_performance_with_small_proxy_model.md)**

:   提出 rBridge，通过使用 frontier 模型的推理 trace 作为 gold label 并按 token 级任务对齐加权 NLL，使 ≤1B 的小模型能有效预测 13B-32B 大模型的推理性能，在数据集排名任务中实现 100× 以上的计算节省。

**[Predicting LLM Reasoning Performance with Small Proxy Models](predicting_llm_reasoning_performance_with_small_proxy_models.md)**

:   提出 rBridge 方法，通过结合前沿模型推理轨迹 (reasoning trace) 的 NLL 评估与 token 级任务对齐权重，使 ≤1B 的小模型能有效预测 13B-32B 大模型的推理性能，数据排序计算成本降低 100 倍以上。

**[Predicting Training Re-evaluation Curves Enables Effective Data Curriculums](predicting_training_re-evaluation_curves_enables_effective_data_curriculums_for_.md)**

:   提出训练再评估曲线（TREC）诊断工具，通过分析训练完成后模型在各时间步训练数据上的损失来指导高质量数据的最优放置位置，并证明 TREC 形状可通过 AdamW 的隐式 EMA 系数预测，无需实际训练即可设计数据课程。

**[Preference Leakage: A Contamination Problem in LLM-as-a-judge](preference_leakage_a_contamination_problem_in_llm-as-a-judge.md)**

:   首次定义并系统研究 LLM-as-a-Judge 中的 **偏好泄漏 (Preference Leakage)** 问题——当合成数据生成器 $M_G$ 与评估器 $M_J$ 存在关联（同模型/继承/同家族）时，评委会对"相关学生模型"产生系统性偏好，同模型场景下 PLS 高达 28.7%（Arena-Hard），且该偏差比自中心偏差更隐蔽、更难检测。

**[Prompt and Parameter Co-Optimization for Large Language Model Task Adaptation](prompt_and_parameter_co-optimization_for_large_language_model_task_adaptation.md)**

:   提出 MetaTuner 框架，通过共享元编码器同时生成查询特定的提示和 LoRA 参数，使提示优化与微调相互增强，并设计监督正则化损失解决离散-连续混合优化问题，在 MATH、GSM8K、HotpotQA、CosmosQA 上一致超越独立的提示优化和微调方法。

**[Prompt and Parameter Co-Optimization for Large Language Models](prompt_and_parameter_co-optimization_for_large_language_models.md)**

:   提出 MetaTuner 框架，通过共享 meta encoder 同时生成 prompt 和 LoRA 参数，将离散 prompt 优化与连续参数微调统一为端到端可优化的联合框架，在数学推理和问答任务上大幅超越单独优化的方法。

**[RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty](rankllm_weighted_ranking_of_llms_by_quantifying_question_difficulty.md)**

:   提出 RankLLM，一个基于有向二部图双向分数传播的非参数化框架，联合估计题目难度和模型能力，实现难度感知的 LLM 排名，与人类判断达到 90% 一致性。

**[Reasoning on Time-Series for Financial Technical Analysis](reasoning_on_time-series_for_financial_technical_analysis.md)**

:   提出 Verbal Technical Analysis (VTA) 框架，结合 LLM 的语言推理能力与时间序列模型的模式捕捉能力，通过 Time-GRPO 强化学习优化推理链，并以推理属性条件化时序预测，实现了兼具准确性和可解释性的金融时间序列预测。

**[ReIn: Conversational Error Recovery with Reasoning Inception](rein_conversational_error_recovery_with_reasoning_inception.md)**

:   提出 Reasoning Inception（ReIn），一种无需修改模型参数或系统提示的测试时干预方法，通过外部 inception 模块检测对话错误并将恢复计划注入任务 agent 的推理链中，在多种错误场景下显著提升对话任务完成率，且可泛化至未见错误类型。

**[Rethinking Code Similarity for Automated Algorithm Design with LLMs](rethinking_code_similarity_for_automated_algorithm_design_with_llms.md)**

:   提出 BehaveSim，一种基于"问题求解轨迹"（PSTrajs）和动态时间规整（DTW）的算法相似度度量方法，从执行行为层面而非语法或输出层面衡量算法差异，集成到 FunSearch/EoH 等 LLM-AAD 框架后显著提升性能。

**[Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation](retrieval-augmented_generation_for_predicting_cellular_responses_to_gene_perturb.md)**

:   提出 **PT-RAG**（Perturbation-aware Two-stage Retrieval-Augmented Generation），首次将可微检索增强生成范式应用于单细胞基因扰动响应预测：通过 GenePT 语义检索候选扰动 + Gumbel-Softmax 条件离散采样实现细胞类型感知的端到端检索优化，在 Replogle-Nadig 数据集上超越 STATE 基线（Pearson 0.633 vs 0.624），同时发现朴素 RAG 会严重损害性能（Pearson 仅 0.396），证明**可微且细胞类型感知的检索**在该领域不可或缺。

**[Revisiting the Past: Data Unlearning with Model State History](revisiting_the_past_data_unlearning_with_model_state_history.md)**

:   提出 MSA（Model State Arithmetic）算法，利用训练中间检查点构造"遗忘向量"，通过参数空间算术运算移除特定数据对模型的影响，在 TOFU 和 RESTOR 基准上一致优于 NPO、RMU、GradDiff 等现有遗忘方法，且即使不用保留集也能保持模型效用。

**[Rote Learning Considered Useful: Generalizing over Memorized Data in LLMs](rote_learning_considered_useful_generalizing_over_memorized_data_in_llms.md)**

:   提出"记忆-再泛化"（memorize-then-generalize）框架，通过先用无语义合成 token 死记硬背事实关联、再用少量语义提示微调的两阶段策略，揭示 LLM 能从死记硬背数据中泛化，且记忆越深泛化越好，同时指出该机制可被恶意利用的安全隐患。

**[Rote Learning Considered Useful: Generalizing over Memorized Training Examples](rote_learning_considered_useful_generalizing_over_memorized_training_examples.md)**

:   本文提出"先记忆再泛化"两阶段框架，证明 LLM 可以在死记硬背合成关键 token 后，通过极少量语义微调实现泛化，挑战了"记忆阻碍泛化"的传统观点。

**[Self-Destructive Language Model](self-destructive_language_model.md)**

:   提出 Seam，通过耦合良性和有害数据的优化轨迹（使梯度方向相反），将 LLM 转变为"自毁模型"——在有害微调时自动触发灾难性性能崩溃，创造攻击者的两难困境：低强度攻击无效，高强度攻击导致模型报废。

**[Semantic Regexes: Auto-Interpreting LLM Features with a Structured Language](semantic_regexes_auto-interpreting_llm_features_with_a_structured_language.md)**

:   提出 semantic regexes——一种用于自动描述 LLM 特征的结构化语言，通过 symbol/lexeme/field 三种原语及 context/composition/quantification 修饰符，在保持与自然语言同等准确度的同时，实现了更简洁、更一致的特征描述，并可量化特征复杂度随层的变化趋势。

**[Semantic Regexes: Auto-Interpreting LLM Features with a Structured Language](semantic_regexes_auto-interpreting_llm_features_with_a_structured_language_of_re.md)**

:   本文提出 **Semantic Regexes（语义正则表达式）**，一种用于自动描述 LLM 特征的结构化语言，通过原语（symbol/lexeme/field）+ 修饰符（context/composition/quantification）组合，实现与自然语言同等准确但更简洁、一致且可分析的特征描述。

**[SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs](simpletom_exposing_the_gap_between_explicit_tom_inference_and_implicit_tom_appli.md)**

:   SimpleToM 揭示了 LLM 在 Theory of Mind 上的关键缺陷：前沿模型能准确推断他人心理状态（显式 ToM），但在将此知识应用于行为预测和行为判断时性能急剧下降（应用 ToM），暴露了"知道什么"与"如何使用所知"之间的重大鸿沟。

**[Spectral Attention Steering for Prompt Highlighting](spectral_attention_steering_for_prompt_highlighting.md)**

:   提出 SEKA/AdaSEKA，通过对 key embedding 进行谱分解学习"相关性子空间"，在注意力计算前直接编辑 key 向量来实现 prompt highlighting，无需存储完整注意力矩阵，与 FlashAttention 完全兼容，且开销极低（+0.03s/sample）。

**[Statistical Advantage of Softmax Attention: Insights from Single-Location Regression](statistical_advantage_of_softmax_attention_insights_from_single-location_regress.md)**

:   通过提出"单位置回归"(Single-Location Regression, SLR) 理论框架，结合统计物理中的 order parameter 方法，在高维极限下严格证明了 softmax attention 在种群层面达到 Bayes 风险而线性 attention 本质上无法做到，并在有限样本情形下证实 softmax 始终优于线性 attention，为 softmax 在检索任务中的优势提供了首个原理性解释。

**[Stochastic Self-Organization in Multi-Agent Systems](stochastic_self-organization_in_multi-agent_systems.md)**

:   提出 SelfOrg 框架，基于 Agent 响应的语义相似度和 Shapley 值贡献估计，动态构建有向无环通讯图（DAG），实现多 Agent 系统的自组织协作。在弱模型场景下优势尤为显著。

**[Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding](stopping_computation_for_converged_tokens_in_masked_diffusion-lm_decoding.md)**

:   提出 SureLock，当 Masked Diffusion LM 中已 unmask 的 token 后验分布稳定后永久锁定该位置（跳过 Q 投影和 FFN，缓存 KV），将每步注意力计算从 $O(N^2d)$ 降为 $O(MNd)$，在 LLaDA-8B 上减少 30-50% FLOPs 且不损生成质量。

**[Subliminal Signals in Preference Labels](subliminal_signals_in_preference_labels.md)**

:   证明偏好标签可以作为隐蔽通信通道：即使学生模型生成的是语义无关的数字序列，有偏见的裁判模型仅通过二值偏好标签就能向学生模型传递潜意识行为特征，且这种传递在迭代对齐中会增强。

**[Sublinear Time Quantum Algorithm for Attention Approximation](sublinear_time_quantum_algorithm_for_attention_approximation.md)**

:   提出首个对序列长度 $n$ 具有**亚线性**时间复杂度的量子数据结构，用于近似 Transformer 注意力矩阵的行查询，预处理时间 $\widetilde{O}(\epsilon^{-1} n^{0.5} \cdot \text{poly}(d, s_\lambda, \alpha))$，每次行查询 $\widetilde{O}(s_\lambda^2 + s_\lambda d)$，相对经典算法实现了关于 $n$ 的二次加速。

**[Talk, Evaluate, Diagnose: User-aware Agent Evaluation with Automated Error Analysis](talk_evaluate_diagnose_user-aware_agent_evaluation_with_automated_error_analysis.md)**

:   提出 TED 框架（Talk-Evaluate-Diagnose），通过可复用的专家/非专家 persona 模板、基于 grading notes 的 LLM-as-judge 评估和自动化错误分析，实现跨领域的用户感知型 Agent 评估。

**[TASTE: Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](taste_text-aligned_speech_tokenization_and_embedding_for_spoken_language_modelin.md)**

:   提出 TASTE（Text-Aligned Speech Tokenization and Embedding），通过跨注意力机制将语音 token 与文本转录对齐，实现极低比特率（~150 bps）下的高质量语音重建，并使文本-语音联合建模变得直接高效，1.3B 参数的 TASLM 超越 7B 预训练 SLM。

**[The Lattice Representation Hypothesis of Large Language Models](the_lattice_representation_hypothesis_of_large_language_models.md)**

:   提出 LLM 的**格表示假说 (Lattice Representation Hypothesis)**：通过将线性表示假说与形式概念分析 (FCA) 统一，证明 LLM 嵌入空间中的属性方向通过半空间交集隐式编码了一个**概念格 (concept lattice)**，从而实现了连续几何与符号抽象之间的桥接。

**[The Path of Least Resistance: Guiding LLM Reasoning Trajectories for Efficient Consistency](the_path_of_least_resistance_guiding_llm_reasoning_trajectories_for_efficient_co.md)**

:   提出 PoLR（Path of Least Resistance），首个利用推理前缀一致性的推理时方法，通过聚类短前缀并仅扩展主导聚类来实现 Self-Consistency 的高效替代，可减少高达 60% token 使用和 50% 延迟。

**[Token-Efficient Item Representation via Images for LLM Recommender Systems](token-efficient_item_representation_via_images_for_llm_recommender_systems.md)**

:   提出 I-LLMRec，利用商品图像替代冗长文本描述来表示推荐系统中的物品语义，通过 RISA 对齐模块和 RERI 检索模块，在仅用单个token表示物品的同时保留丰富语义，推理速度提升约2.93倍且推荐性能超越文本描述方法。

**[Trapped by simplicity: When Transformers fail to learn from noisy features](trapped_by_simplicity_when_transformers_fail_to_learn_from_noisy_features.md)**

:   研究表明 Transformer 在从含特征噪声的数据中学习布尔函数时会失败——其简单性偏好（倾向学习低敏感度函数）导致模型被困在比目标函数更简单的最优噪声预测器上，无法恢复真实的无噪声目标函数。

**[Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](truthfulness_despite_weak_supervision_evaluating_and_training_llms_using_peer_pr.md)**

:   提出将博弈论中的 Peer Prediction 机制应用于 LLM 评估和训练，通过衡量参与者答案的互预测性来区分诚实与欺骗回答，无需真值标签即可实现诚实性激励，展现出惊人的"逆向缩放"特性——专家越弱反而越能抵抗强模型的欺骗。

**[UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking](uis-digger_towards_comprehensive_research_agent_systems_for_real-world_unindexed.md)**

:   识别并形式化"未索引信息检索"(UIS) 问题——搜索引擎无法直接检索的动态网页/嵌入文件/交互式内容，提出首个 UIS 基准 UIS-QA（110 题）和多 Agent 框架 UIS-Digger，以 ~30B 参数模型经 SFT+RFT 训练后达到 27.27% 准确率，超越集成 O3/GPT-4.1 的系统。

**[Understanding Sensitivity of Differential Attention through the Lens of Adversarial Robustness](understanding_sensitivity_of_differential_attention_through_the_lens_of_adversar.md)**

:   首次从对抗鲁棒性角度分析 Differential Attention（DA）机制，揭示其减法结构在抑制噪声的同时会通过负梯度对齐放大对抗扰动敏感度，发现"脆弱性原理"——DA 在干净样本上提升判别力但在对抗攻击下更脆弱，且存在深度依赖的鲁棒性交叉效应。

**[Understanding Sensitivity of Differential Attention through the Lens of Adversarial Robustness](understanding_sensitivity_of_differential_attention_through_the_lens_of_softmax_.md)**

:   首次从对抗鲁棒性角度分析 Differential Attention (DA) 的结构性脆弱：DA 的减法结构在抑制噪声的同时，由于负梯度对齐会放大对抗扰动敏感性，揭示了选择性与鲁棒性之间的根本权衡。

**[Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors](understanding_the_emergence_of_seemingly_useless_features_in_deep_learning.md)**

:   从梯度信号的角度解释了为什么用下一 token 预测(NTP)训练的 Transformer 会学习到对预测当前下一 token "无用"的特征，提出三种梯度路径分解（直接学习、预缓存、电路共享）并在玩具任务、OthelloGPT 和语言模型中验证。

**[Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors](understanding_the_emergence_of_seemingly_useless_features_in_next-token_predicto.md)**

:   通过将训练梯度信号分解为 direct、pre-cached 和 circuit sharing 三种成分，解释了为什么 NTP 训练的 Transformer 会学到对预测当前下一token"无用"的特征，并在 OthelloGPT、小型语言模型和预训练 LLM（Gemma 2）上验证了这一框架的解释力。

**[Universal Properties of Activation Sparsity in Modern Large Language Models](universal_properties_of_activation_sparsity_in_modern_large_language_models.md)**

:   对现代 LLM（GLU 架构 + SiLU/GELU）的激活稀疏性进行系统性研究，提出通用的 top-p 稀疏化框架和临界稀疏度（critical sparsity）指标，发现激活稀疏度随模型规模单调递增、输入稀疏化是最实用的免训练加速方案，并首次证明扩散型 LLM 也具有显著的激活稀疏性。

**[Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework](unpacking_human_preference_for_llms_demographically_aware_evaluation_of_long-fo.md)**

:   提出 HUMAINE 框架，通过 23,404 名人口统计分层参与者对 28 个 SOTA 模型进行多维度（5 维）、多轮对话的人类偏好评估，用层次贝叶斯 BTD 模型揭示年龄是偏好异质性的最大驱动因素（平均排名偏移 ±2.8），证明单一聚合排行榜不足以反映不同人群的真实偏好。

**[Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework](unpacking_human_preference_for_llms_demographically_aware_evaluation_with_the_hu.md)**

:   提出 HUMAINE 框架，通过 23,404 名人口统计学分层参与者对 28 个模型的多维度评估，揭示了人类偏好中年龄是最大分歧轴、单一排行榜掩盖关键差异的发现。

**[Unsupervised Evaluation of Multi-Turn Objective-Driven Interactions](unsupervised_evaluation_of_multi-turn_objective-driven_interactions.md)**

:   提出三种**无监督**指标——LLM 引导聚类（目标识别）、基于微调完成模型的交互完整性检测、响应树（LLM 不确定性量化）——用于评估多轮目标驱动对话，无需标注数据或 LLM-as-a-judge，仅用 8B 模型即可匹配/超越 70B judge 的性能。

**[vCache: Verified Semantic Prompt Caching](vcache_verified_semantic_prompt_caching.md)**

:   提出 vCache——首个具有**用户定义错误率保证**的语义缓存系统，通过在线学习为每个缓存嵌入独立估计最优相似度阈值，无需预训练即可在满足正确性约束下实现最高 12.5× 缓存命中率提升和 26× 错误率降低。

**[VCWorld: A Biological World Model for Virtual Cell Simulation](vcworld_a_biological_world_model_for_virtual_cell_simulation.md)**

:   提出 VCWorld，一个细胞级白盒模拟器，通过整合结构化生物知识与大语言模型的迭代推理能力来构建生物世界模型，以数据高效的方式生成可解释的扰动预测和机制假说。

**[VeriTrail: Closed-Domain Hallucination Detection with Traceability](veritrail_closed-domain_hallucination_detection_with_traceability.md)**

:   提出 VeriTrail，首个面向多步生成（MGS）过程的闭域幻觉检测方法，通过将生成过程建模为 DAG 并沿图逐层验证 claim，实现了幻觉检测+溯源（provenance）+错误定位（error localization）的完整可追溯性，在两个新数据集上显著优于所有基线。

**[VeriTrail: Closed-Domain Hallucination Detection with Traceability](veritrail_closed-domain_hallucination_detection_with_traceable_evidence_synthes.md)**

:   提出 VeriTrail——首个为多步生成过程（MGS）提供可追溯性的闭域幻觉检测方法，建模生成过程为 DAG 并沿路径逐层验证，同时构建了首批包含所有中间输出和人工标注的 MGS 数据集。

**[WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality](webdevjudge_mllm_web_development.md)**

:   构建 WebDevJudge 元评估基准，系统评估 LLM/MLLM 及智能体工作流在 Web 开发质量评估任务上作为裁判的能力，发现当前最强模型与人类专家之间仍存在约15%的一致率差距，并揭示了功能等价识别失败和可行性验证薄弱两大根本瓶颈。

**[Weight Decay may matter more than μP for Learning Rate Transfer in Practice](weight_decay_may_matter_more_than_mup_for_learning_rate_transfer_in_practice.md)**

:   大规模实证研究表明 μP 的核心对齐假设在实际 LLM 训练中仅在开始时短暂成立，之后是 independent weight decay（而非 μP）正确稳定了不同宽度模型间的特征学习动态，使得学习率迁移成为可能。μP 的实际作用被重新解释为一种隐式学习率 warmup。

**[Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity](whatever_remains_must_be_true_filtering_drives_reasoning_in_llms_shaping_diversi.md)**

:   提出 DMVR 框架和 α-DPG 算法，通过显式定义"过滤掉错误答案"的目标分布并用 α-散度族来逼近，统一了 RLVR（Reverse KL）和拒绝采样微调（Forward KL），在 Lean 定理证明上实现了精度-覆盖率 Pareto 前沿的最优表现。

**[When Priors Backfire: On the Vulnerability of Unlearnable Examples to Pretraining](when_priors_backfire_on_the_vulnerability_of_unlearnable_examples_to_data_augmen.md)**

:   揭示了 Unlearnable Examples (UE) 在面对预训练模型时的根本脆弱性——预训练先验使模型绕过 UE 注入的虚假快捷方式，并提出 BAIT 双层优化框架通过将扰动绑定到错误标签来对抗预训练先验。

**[When Priors Backfire: On the Vulnerability of Unlearnable Examples to Pretraining](when_priors_backfire_on_the_vulnerability_of_unlearnable_examples_to_pretraining.md)**

:   揭示了不可学习样本 (UEs) 在预训练模型上的根本性脆弱性——预训练先验使模型能绕过扰动捷径学到真实语义，并提出 BAIT 框架通过将扰动绑定到错误标签来对抗预训练先验。

**[When Stability Fails: Hidden Failure Modes of LLMs in Data-Constrained Scientific Decision-Making](when_stability_fails_hidden_failure_modes_of_llms_in_data-constrained_scientific.md)**

:   通过控制性行为评估框架，揭示 LLM 在数据约束的科学决策任务中的四种隐藏失败模式：高稳定性≠正确性、prompt 措辞敏感性、放宽阈值下的过度选择、以及幻觉产生无效标识符。

**[When Stability Fails: Hidden Failure Modes of LLMs in Data-Constrained Scientific Decision-Making](when_stability_fails_hidden_failure_modes_of_llms_in_data-critical_statistical_.md)**

:   揭示 LLM 在数据约束的科学决策任务中的隐藏失败模式：模型可以展现近乎完美的运行间稳定性，同时系统性偏离统计学基准真值，表现为过度选择、prompt 敏感和幻觉基因标识符。

**[When to Ensemble: Identifying Token-Level Points for Stable and Fast LLM Ensembling](when_to_ensemble_identifying_token-level_points_for_stable_and_fast_llm_ensembli.md)**

:   提出 SAFE（Stable And Fast LLM Ensembling），通过 Generate-Verify-Ensemble 循环在 token 级别选择性地集成多个异构分词器 LLM，解决长序列生成中分词不匹配导致的 OOV-like 污染问题，仅在不到 1% 的 token 上集成即可提升效果，MATH500 上将 UniTE 从 59.6% 提升到 77.4%。

**[Which LLM Multi-Agent Protocol to Choose?](which_llm_multi-agent_protocol_to_choose.md)**

:   本文提出ProtocolBench基准和ProtocolRouter路由器，首次系统性比较了多Agent系统中的通信协议（A2A、ACP、ANP、Agora等）在任务成功率、延迟、消息开销和鲁棒性四个维度上的差异，并通过可学习的协议路由器实现场景自适应的协议选择，最高降低18.1%的故障恢复时间。
