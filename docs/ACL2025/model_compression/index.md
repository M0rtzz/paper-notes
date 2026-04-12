---
title: >-
  ACL2025 模型压缩方向 62篇论文解读
description: >-
  62篇ACL2025 模型压缩方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**💬 ACL2025** · 共 **62** 篇

**[500Xcompressor Generalized Prompt Compression For Large Language Models](500xcompressor_generalized_prompt_compression_for_large_language_models.md)**

:   提出 500xCompressor，将最多约 500 个自然语言 token 压缩为最少 1 个特殊 token 的 KV 值，实现 6x 到 480x 的压缩比，仅增加约 0.25% 的参数，LLM 在压缩后保留 62.26%-72.89% 的原始能力，显著超越 ICAE 基线。

**[Accurate Kv Cache Quantization With Outlier Tokens Tracing](accurate_kv_cache_quantization_with_outlier_tokens_tracing.md)**

:   发现 KV Cache 的 outlier channel 中存在少量异常 token 偏离先前假设的均匀分布，提出 OTT（Outlier Tokens Tracing）方法，在量化过程中动态追踪并排除这些 token，在 2-bit 量化下实现 6.4x 内存压缩和 2.3x 吞吐提升，同时显著提高精度。

**[Aligndistil Token Level Alignment](aligndistil_token_level_alignment.md)**

:   AlignDistil 证明了 RLHF 目标函数与 token 级蒸馏过程的理论等价性，并据此设计了一种简单的蒸馏方法：用 DPO 模型和反向 DPO 模型的 logit 分布线性组合构造教师分布，配合 token 自适应外推机制实现 token 级奖励优化，在 AlpacaEval 2.0、MT-Bench 和 Arena-Hard 上优于现有方法且收敛更快。

**[Apb Distributed Long Context](apb_distributed_long_context.md)**

:   APB 提出了一种分布式长上下文推理框架，通过在序列并行框架中引入本地 KV cache 压缩和跨 GPU 传递压缩上下文块的机制，在不损失任务性能的前提下实现了相比 FlashAttn/RingAttn/StarAttn 分别高达 9.2x/4.2x/1.6x 的 prefill 加速。

**[Assigning Distinct Roles To Quantized And Low-Rank Matrices Toward Optimal Weigh](assigning_distinct_roles_to_quantized_and_low-rank_matrices_toward_optimal_weigh.md)**

:   提出 ODLRI（Outlier-Driven Low-Rank Initialization）——在量化+低秩联合权重分解 $\mathbf{W} \approx \mathbf{Q} + \mathbf{LR}$ 中，将低秩分量专门分配给捕获激活敏感权重（异常值相关），量化分量处理剩余权重。通过这种"角色分配"初始化，稳定量化、降低激活感知误差，在 Llama2/3 和 Mistral 的低比特设置中一致提升困惑度和零样本精度。

**[Basic Reading Distillation](basic_reading_distillation.md)**

:   本文提出基础阅读蒸馏（BRD），通过让教师LLM在通用语料上生成基础阅读行为数据（包括NER和问答），训练小型学生模型模仿这些行为，使564M参数的小模型在不接触下游任务数据的情况下就能在多种NLP任务上达到或超过20倍大的教师模型性能。

**[Beamlora Beam Constraint Lora](beamlora_beam_constraint_lora.md)**

:   BeamLoRA 发现 LoRA 模块中不同 rank 的重要性存在显著差异且随训练动态演变，受 beam search 启发，提出在训练过程中动态评估 rank 重要性、剪枝不重要的 rank 并将参数空间扩展给重要 rank，在固定总 rank 下提升性能，在三个基座模型的 12 个数据集上持续优于 LoRA 及其变体。

**[Beyond Text Compression Tokenizers](beyond_text_compression_tokenizers.md)**

:   本文系统评估了 6 种 tokenizer 在 350M 和 2.7B 参数模型上的影响，发现 tokenizer 选择对英文任务影响极小但对多语言任务（如机器翻译）有显著且跨尺度一致的影响，并提出了基于 Zipf 定律的新型内在评估指标，比文本压缩率能更好地预测多语言场景下的下游性能。

**[Bf16 Or Death Quantization Tradeoffs](bf16_or_death_quantization_tradeoffs.md)**

:   这是迄今最全面的 LLM 量化实证研究，在 Llama-3.1 全系列（8B/70B/405B）上对 FP8/INT8/INT4 进行了超过 50 万次评估，发现 FP8 几乎无损、INT8 仅降 1-3%、INT4 出奇地有竞争力，并给出了不同部署场景的量化格式选择建议。

**[Blockpruner Fine-Grained Pruning For Large Language Models](blockpruner_fine-grained_pruning_for_large_language_models.md)**

:   提出 BlockPruner，将 Transformer 层分解为 MHA 和 MLP 两个最小残差块，基于困惑度评估块重要性并通过迭代搜索进行细粒度剪枝，实现比层级剪枝更优的压缩效果。

**[Brainecho Semantic Brain Signal Decoding Through Vector-Quantized Spectrogram Re](brainecho_semantic_brain_signal_decoding_through_vector-quantized_spectrogram_re.md)**

:   提出 BrainECHO 三阶段框架（自编码—对齐—微调），通过向量量化离散表示将脑信号映射到 Mel 频谱图空间，再借助 Whisper 完成非侵入式脑信号到文本的高质量解码。

**[Capture Key Cot Distillation](capture_key_cot_distillation.md)**

:   提出 EDIT（mistakE-Driven key reasonIng step distillaTion），通过构造正确/错误配对的 dual CoTs 数据，利用最小编辑距离算法定位关键推理步骤，并以 token 级细粒度损失函数引导小模型聚焦学习这些关键步骤，而非简单模仿教师的推理形式。

**[Correcting Hallucinations In News Summaries Exploration Of Self-Correcting Llm M](correcting_hallucinations_in_news_summaries_exploration_of_self-correcting_llm_m.md)**

:   系统性地探究了两种自纠正方法（CoVE 和 RARR）在新闻摘要幻觉纠正中的表现，比较了三种搜索引擎、多种检索设置和提示策略，发现 Bing 搜索片段 + RARR（few-shot）组合效果最佳，且 G-Eval 与人类评估高度一致。

**[Dac Prompt Compression](dac_prompt_compression.md)**

:   DAC 提出动态注意力感知的 prompt 压缩方法，通过融合信息熵和注意力分数作为 token 重要性度量，并动态感知压缩过程中的熵偏移来进行细粒度压缩，在 LongBench 上比 SOTA 方法提升平均 1.33 分。

**[Data Laundering Artificially Boosting Benchmark Results Through Knowledge Distil](data_laundering_artificially_boosting_benchmark_results_through_knowledge_distil.md)**

:   本文揭示了知识蒸馏可被滥用来人为提高基准测试分数的漏洞——通过"数据洗白"（Data Laundering）方法，将教师模型在测试集上学到的知识通过看似合法的中间训练步骤隐蔽地传递给学生模型，使一个2层BERT即可在GPQA上达到73.94%（接近OpenAI o1的77.30%），而该模型并未真正学会推理。

**[Deepsolution Boosting Complex Engineering Solution Design Via Tree-Based Explora](deepsolution_boosting_complex_engineering_solution_design_via_tree-based_explora.md)**

:   提出面向复杂工程方案设计的新基准 SolutionBench 和新系统 SolutionRAG，通过树搜索探索+双视角思维（设计-审查交替）在 RAG 框架下逐步生成满足多约束的可靠工程方案，在 8 个工程领域达到 SOTA。

**[Denselora Dense Low-Rank Adaptation Of Large Language Models](denselora_dense_low-rank_adaptation_of_large_language_models.md)**

:   本文提出DenseLoRA，通过引入跨层共享的Encoder-Decoder进行隐藏表示的压缩与重建，用一个稠密的小型低秩矩阵替代LoRA中两个冗余的低秩矩阵来进行适配，仅用0.01%可训练参数在LLaMA3-8B上达到83.8%准确率，超越了LoRA用0.70%参数达到的80.8%。

**[Direct Behavior Optimization Unlocking The Potential Of Lightweight Llms](direct_behavior_optimization_unlocking_the_potential_of_lightweight_llms.md)**

:   提出 DeBoP 范式，将轻量级 LLM（LwLLM）的行为优化转化为对离散执行序列的优化，通过无梯度蒙特卡洛树搜索（MCTS）自动寻找最优 demonstration，使 LLaMA3-8B 在多数任务上超越 GPT-3.5 并减少约 60% 计算时间。

**[Drpruning Robust Pruning](drpruning_robust_pruning.md)**

:   DRPruning 将分布稳健优化（DRO）引入 LLM 结构化剪枝，通过 scaling law 预测各领域最终 loss 作为参考、动态调整训练数据分布来平衡剪枝后各领域性能，在单语和多语设置下分别以 -5.59% PPL 和 +2.95% 下游任务的提升超越 Sheared LLaMA。

**[Eac Moe Expert Aware Compression](eac_moe_expert_aware_compression.md)**

:   EAC-MoE 从 MoE 模型的专家选择特性出发，提出量化时校准路由器缓解 expert-shift 问题（QESC）+ 推理时基于专家选择频率动态剪枝不重要专家（PESF），在 Mixtral-8x7B 上实现 4.92× 内存压缩和 1.68× 推理加速且精度损失不到 1%。

**[Efficientqat](efficientqat.md)**

:   EfficientQAT 提出两阶段 QAT 框架——先逐块训练所有参数（Block-AP）提供良好初始化，再端到端训练量化参数（E2E-QP）捕获跨块交互，在单张 A100 上 41 小时完成 Llama-2-70B 的 2-bit 量化，精度仅降 3 点。

**[Entropy-Based Exploration Conduction For Multi-Step Reasoning](entropy-based_exploration_conduction_for_multi-step_reasoning.md)**

:   提出 Entro-duction 方法，通过监控 LLM 推理过程中输出的熵和方差熵变化来动态调整探索深度，使用 $\epsilon$-greedy 策略选择加深、扩展或停止三种探索行为，在避免冗余推理的同时提升推理准确率。

**[Explaining Puzzle Solutions In Natural Language An Exploratory Study On 6X6 Sudo](explaining_puzzle_solutions_in_natural_language_an_exploratory_study_on_6x6_sudo.md)**

:   评估 5 个 LLM 在解决和解释 6×6 数独谜题上的能力，发现开源模型几乎无法正确求解（<1%），o1-preview 可解 65% 但其解释在正当性、清晰度和教育价值三个维度上均严重不足，揭示了 LLM 在多步推理解释方面的根本局限。

**[Fedex Lora Federated Exact Aggregation](fedex_lora_federated_exact_aggregation.md)**

:   FedEx-LoRA 发现联邦学习中独立平均 LoRA 的 A 和 B 矩阵会导致不精确的全局更新（"乘积的均值≠均值的乘积"），通过在冻结权重矩阵中加入残差误差项实现精确聚合，在多个推理和 NLU 任务上一致优于 FedIT 和 FFA-LoRA。

**[Flipping Kd Small To Large](flipping_kd_small_to_large.md)**

:   本文提出"反向知识蒸馏"范式——让 LLM 从微调过的小模型学习文本匹配的领域专家知识，通过将 decoder-only LLM 重新解释为 encoder-decoder 架构（用 LoRA 的压缩矩阵做 encoder）并设计 Margin-aware Contrastive Loss 来对齐表示相似度。

**[Gist Token Context Compression](gist_token_context_compression.md)**

:   系统研究Gist Token上下文压缩方法，提出统一框架分类现有架构（记忆位置×粒度），发现Fine-grained KV Cache在RAG/QA上近无损但在合成召回上有明显缺陷，识别出三种失败模式（边界丢失/意外丢失/中途丢失），并提出细粒度自编码和分段token重要性估计两种改进策略。

**[Graph Counselor Multiagent Graphrag](graph_counselor_multiagent_graphrag.md)**

:   Graph Counselor 提出了一个多智能体协作的 GraphRAG 推理框架，通过 Planning/Thought/Execution 三个 Agent 自适应提取图结构信息，并引入多视角自反思机制纠正推理偏差，在多个图推理任务上超越现有方法。

**[Iam Efficient Inference Through Attention Mapping Between Different-Scale Llms](iam_efficient_inference_through_attention_mapping_between_different-scale_llms.md)**

:   发现不同规模 LLM 的注意力矩阵具有高度相似性，提出 IAM 框架——在 prefill 阶段建立小模型与大模型注意力头之间的余弦相似度映射，decode 阶段用小模型的注意力矩阵替代大模型映射层的注意力计算，实现 KV cache 减少 22% 和推理加速 11%，且与现有 KV cache 压缩方法正交。

**[L4Q Parameter Efficient Quantization Aware Finetuning](l4q_parameter_efficient_quantization_aware_finetuning.md)**

:   提出 L4Q，将量化感知训练 (QAT) 与 LoRA 深度整合：先合并权重与LoRA参数再统一量化，通过定制反向传播路径消除权重梯度存储开销，实现联合优化量化与微调参数，在4-bit和3-bit量化下显著超越现有方法。

**[Lacuna Inc At Semeval-2025 Task 4 Lora-Enhanced Influence-Based Unlearning For L](lacuna_inc_at_semeval-2025_task_4_lora-enhanced_influence-based_unlearning_for_l.md)**

:   提出 LIBU（LoRA 增强的影响函数遗忘算法），分两阶段实现 LLM 机器遗忘：Phase 1 用对角 Fisher 信息矩阵加权的影响函数更新参数精准遗忘，Phase 2 用 Sophia 二阶优化器稳定化训练，在 SemEval-2025 Task 4 的 OLMo-7B 上达到 0.283 遗忘率同时维持 0.469 MMLU 准确率。

**[Language Models Resist Alignment](language_models_resist_alignment.md)**

:   本文从压缩理论视角揭示了LLM存在"弹性"(elasticity)现象——模型倾向于保持预训练分布而抵触对齐分布，且对齐后的模型在受到扰动时会以与数据量差距成反比的速率回弹到预训练状态，这解释了为什么对齐如此脆弱且容易被少量微调逆转。

**[Language Specific Features](language_specific_features.md)**

:   利用 Sparse Autoencoders (SAEs) 分析多语言 LLM 的内部表示，发现存在强烈的语言特定 SAE features，这些 features 不仅与语言特有 token 相关还与语言上下文相关，消融它们只影响对应语言能力，且多个语言 features 之间存在协同效应；进一步利用这些 features 增强 steering vectors 实现对生成语言的精确控制。

**[Law Of Capacity Gap Distilling Language Models](law_of_capacity_gap_distilling_language_models.md)**

:   揭示了语言模型蒸馏中的"容量差距定律"——最优教师模型的参数量与学生模型成线性关系（约 2.5 倍），将 LLM 蒸馏中的"不可能三角"转化为可解问题，并据此成功蒸馏出 3B 的 MiniMA 模型。

**[Limited-Resource Adapters Are Regularizers Not Linguists](limited-resource_adapters_are_regularizers_not_linguists.md)**

:   本文将 adapter souping（权重平均）与交叉注意力微调结合用于低资源克里奥尔语机器翻译，发现虽然方法带来了显著提升（最高 +8 BLEU），但语言关联性与 adapter 性能无有意义的协变关系——随机初始化的未训练 adapter 表现同样优秀，表明 adapter 在此设定下的作用本质是**参数正则化而非语言信息迁移**。

**[Longred Mitigating Short-Text Degradation Of Long-Context Large Language Models ](longred_mitigating_short-text_degradation_of_long-context_large_language_models_.md)**

:   本文系统分析了长上下文LLM在短文本任务上性能退化的两个原因（分布漂移和灾难性遗忘），并提出LongReD方法，通过短文本蒸馏和短到长蒸馏两个训练目标来最小化扩展模型与原始模型之间的分布差异，在保持长文本建模能力的同时将短文本性能保留至原始模型的99.4%。

**[Magnet Multi-Turn Tool-Use Data Synthesis And Distillation Via Graph Translation](magnet_multi-turn_tool-use_data_synthesis_and_distillation_via_graph_translation.md)**

:   提出 Magnet 框架，基于函数依赖图的随机游走和节点操作（Insert/Merge/Split）构建高质量多轮 Function Calling 训练轨迹，结合基于提示的上下文蒸馏生成正负对比轨迹进行 SFT + mDPO 训练，使 14B 模型 Magnet-14B-mDPO 在 BFCL-v3 上达到 68.01（排名第 4），在多轮场景上大幅超越教师模型 Gemini-1.5-pro-002。

**[Moqae Mixed Precision Kv Cache](moqae_mixed_precision_kv_cache.md)**

:   MoQAE 创造性地将不同量化比特宽度配置视为 MoE 中的"专家"，通过轻量路由器学习每个 chunk 的最优量化策略，结合路由冻结和路由共享机制，在几乎不损失精度的情况下大幅减少长上下文推理的 KV cache 内存。

**[Mplug Docowl2 Doc Compress](mplug_docowl2_doc_compress.md)**

:   提出High-resolution DocCompressor模块，利用低分辨率全局视觉特征作为query通过交叉注意力将高分辨率文档图像压缩为仅324个token（不到同类方法的20%），在多页文档理解benchmark上达到SOTA且首token延迟降低50%+。

**[One QuantLLM for ALL: Fine-tuning Quantized LLMs Once for Efficient Deployments](one_quantllm_for_all_fine-tuning_quantized_llms_once_for_efficient_deployments.md)**

**[Osrm Lora Merging Orthogonal](osrm_lora_merging_orthogonal.md)**

:   OSRM 发现 LoRA 模型合并失败的根因是参数与数据分布的交互干扰（而非仅仅是参数冲突），提出在微调前通过数据协方差矩阵的特征分解来初始化 LoRA 矩阵 A，使其子空间与其他任务的数据分布正交，从而在合并时最小化跨任务干扰，在 8 个数据集、5 个模型上显著提升合并性能。

**[Outlier-Safe Pre-Training For Robust 4-Bit Quantization Of Large Language Models](outlier-safe_pre-training_for_robust_4-bit_quantization_of_large_language_models.md)**

:   OSP（Outlier-Safe Pre-Training）框架通过三项创新——Muon 优化器（消除特权基方向）、Single-Scale RMSNorm（防止通道放大）和可学习嵌入投影层（重分布嵌入层激活），在预训练阶段主动防止异常值形成，训练的 1.4B 模型在 1T tokens 上实现近零超额峰度（0.04 vs 标准模型的 1818.56），在激进4-bit量化下平均分 35.7（Adam 为 26.5），仅 2% 训练开销。

**[Parameter-Efficient Fine-Tuning Via Circular Convolution](parameter-efficient_fine-tuning_via_circular_convolution.md)**

:   提出Circular Convolution Adaptation (C3A)，用循环卷积算子替代LoRA的低秩矩阵分解来构造增量权重$\Delta W$——循环矩阵的秩与可训练参数数量解耦，实现"少参数+高秩"适配；同时利用FFT加速前向/反向传播，在计算和显存效率上均可与LoRA媲美。在GLUE、常识推理、数学推理、代码生成等任务上持续优于LoRA及其变体。

**[Pre-Training Distillation For Large Language Models A Design Space Exploration](pre-training_distillation_for_large_language_models_a_design_space_exploration.md)**

:   系统性地探索大语言模型预训练蒸馏（Pre-training Distillation）的设计空间，从 logits 处理、损失函数选择、scaling law 和 offline/online logits 四个维度进行广泛实验，找到更优配置并得出有价值的结论。

**[Prompt Distill Teacher Student](prompt_distill_teacher_student.md)**

:   提出候选标注+蒸馏范式（CanDist）——当 LLM 对样本不确定时输出所有可能标签（而非强制给唯一标签），然后用小语言模型（SLM）从候选标注中蒸馏出唯一标签，理论证明候选标注蒸馏比直接使用单标签有更好的理论保证，在六个文本分类任务上验证有效。

**[Ptq161 Low Bit Quantization](ptq161_low_bit_quantization.md)**

:   首次将LLM权重真正量化到1.61-bit（此前号称sub-2bit的方法实际都超过2bit），通过一维结构化掩码（仅增加0.0002-bit/权重）保留显著通道、块级缩放因子优化和量化预处理三大创新，在LLaMA系列上以更低比特超越BiLLM和PB-LLM。

**[Quaff Quantized Peft](quaff_quantized_peft.md)**

:   本文提出 Outlier Spatial Stability Hypothesis (OSSH)——微调期间激活异常通道的空间位置保持稳定——并基于此设计了 Quaff 框架，通过目标动量缩放仅处理少量不变的异常通道，实现 1.73× 延迟降低和 30% 内存节省，同时在 GPQA 上精度还提升了 0.6%。

**[Quantification Of Large Language Model Distillation](quantification_of_large_language_model_distillation.md)**

:   本文提出了两种互补的LLM蒸馏量化方法——身份一致性评估（ICE）和响应相似性评估（RSE），通过越狱攻击挖掘模型身份信息泄露和多粒度响应相似性来衡量模型的蒸馏程度，发现大多数知名LLM（除Claude、Doubao和Gemini外）都表现出较高的蒸馏程度。

**[Revisiting Lora Through The Lens Of Parameter Redundancy Spectral Encoding Helps](revisiting_lora_through_the_lens_of_parameter_redundancy_spectral_encoding_helps.md)**

:   本文系统研究了 LoRA 微调中的参数冗余问题，发现降低密度冗余不会损害表达能力（稀疏性质），并提出 SeLoRA——利用频谱变换（Fourier/Wavelet）从稀疏频谱子空间重参数化 LoRA 矩阵，以更少参数实现更优性能，且可即插即用地集成到多种 LoRA 变体中。

**[Rise Reasoning Enhancement Via Iterative Self-Exploration In Multi-Hop Question ](rise_reasoning_enhancement_via_iterative_self-exploration_in_multi-hop_question_.md)**

:   提出 RISE——结合 RAG 与自迭代训练的多跳问答框架，通过问题分解、检索阅读、自我批判三个动作的自我探索循环，迭代生成训练数据并多目标优化模型，在 2Wiki/HotpotQA/MuSiQue 上超越 GPT-3.5 和所有 8B 级基线。

**[Sci-Lora Mixture Of Scientific Loras For Cross-Domain Lay Paraphrasing](sci-lora_mixture_of_scientific_loras_for_cross-domain_lay_paraphrasing.md)**

:   提出 Sci-LoRA——一种混合多领域 LoRA 的框架，通过对比学习训练文本编码器+动态权重生成器+LoRA 融合模块，在无需领域标签的情况下实现跨12个学科领域的科学文本通俗化改写，在5个数据集10个指标上超越 SOTA。

**[See Strategic Exploration Exploitation Prompt Optimization](see_strategic_exploration_exploitation_prompt_optimization.md)**

:   本文提出 SEE 框架，首次将指令（instruction）和示例（examples）作为整体进行联合优化，采用元启发式优化原则设计四阶段探索-利用策略，在35个基准任务上实现平均13.94%的准确率提升并降低58.67%的计算成本。

**[Selection Bias Node Pruning](selection_bias_node_pruning.md)**

:   提出Bias Node Pruning (BNP)和Auxiliary Option Injection (AOI)两种互补方法，从模型内部和输入端同时缓解LLM在多选题中的选择偏差，仅剪除0.002%权重即可将Llama-3准确率从52.3%提升至65.3%（+24.9%组合提升）。

**[Semantic Exploration Adaptive Gating](semantic_exploration_adaptive_gating.md)**

:   针对 LLM 树搜索推理中"简单题也做复杂搜索"和"语义重复路径反复扩展"两大浪费问题，提出 SEAG 框架：先用 entropy 门控决定是否启动树搜索，再用语义聚类合并等价推理步骤，最终在准确率平均提升 4.3% 的同时仅需 RAP 31% 的推理开销。

**[State Offset Tuning Ssm Peft](state_offset_tuning_ssm_peft.md)**

:   针对 SSM（如 Mamba）提出 State-offset Tuning，一种新的"状态基"PEFT 方法家族，通过在每个时间步直接注入可训练的状态偏移量 $h'$ 替代 Prefix-Tuning 的虚拟 token，解决了 prompt-based 方法在 SSM 上表达能力受限的问题，在更少参数量下持续优于 LoRA 和 Prefix-Tuning。

**[Stun Moe Pruning](stun_moe_pruning.md)**

:   STUN 提出了结构化→非结构化的两阶段 MoE 剪枝方法，第一阶段用 O(1) 前向传播实现可扩展的专家级剪枝，第二阶段在剩余专家内做非结构化剪枝，在 480B 参数的 Snowflake Arctic 上以 40% 稀疏度几乎无性能损失。

**[Table Lora Structure Understanding](table_lora_structure_understanding.md)**

:   TableLoRA 提出面向表格任务的专用 LoRA 模块，通过特殊 token 编码器改善表格序列化，并用 2D LoRA 编码单元格的行列位置信息，在参数高效微调设置下相比 vanilla LoRA 在 HiTab 上提升 5.9%，弥合了 LoRA 与全量微调之间 40.56% 的性能差距。

**[Tada Training-Free Recipe For Decoding With Adaptive Kv Cache Compression And Me](tada_training-free_recipe_for_decoding_with_adaptive_kv_cache_compression_and_me.md)**

:   提出 TaDA——无需训练的 KV cache 压缩方法，通过对 K/V 激活做 head 维度均值中心化后量化偏差（而非原始激活），自动消除离群值问题，配合逐层自适应量化精度搜索，将 KV cache 压缩至原始 16 位的 27% 同时保持接近基线的精度。

**[Trans Peft Transferable](trans_peft_transferable.md)**

:   Trans-PEFT 发现基座模型更新（如 Qwen2→Qwen2.5）主要改变 FFN 层的任务知识存储而较少影响 Attention 层的任务模式，据此提出层内知识掩码和跨层知识丢弃两种策略，使在旧版本上训练的 PEFT 模块可直接迁移到新版本而不需重新微调，性能提升可达 30%。

**[Uniicl Icl Framework](uniicl_icl_framework.md)**

:   提出 UniICL 框架，用**一个冻结的 LLM** 同时完成 demonstration 压缩（compress→virtual tokens）、demonstration 选择（基于压缩后的 virtual token 相似度排序）和最终响应生成三个任务，仅需 17M 可训练参数（projection layer + learnable embedding），配合 Demonstration Bank 缓存机制避免重复压缩，实现 12× 压缩率下从 4-shot 扩展到 64-shot ICL（24GB 显存内），在多个 out-of-domain 数据集上超越 AutoCompressor、ICAE、LLMLingua 等基线。

**[Uniquanf Unified Quantization](uniquanf_unified_quantization.md)**

:   UniQuanF 统一了均匀量化（UQ,表现力弱但优化性强）和二进制编码量化（BCQ,表现力强但优化性差）的优势，通过统一初始化、局部周期映射和统一定理，实现无额外部署开销的高精度 LLM 量化，在 GSM8K 上提升最高 4.60%。

**[Wanda Pruning Large Language Models Via Regional Gradients](wanda_pruning_large_language_models_via_regional_gradients.md)**

:   提出 Wanda++——基于 decoder block 级别区域梯度的轻量级 LLM 剪枝框架，通过区域梯度评分（RGS）改进剪枝准则 + 区域优化（RO）最小化稠密/稀疏块输出差异，在 2:4 稀疏下 WikiText 困惑度较 Wanda 最高降低 32%，单 H100 GPU 10 分钟内完成 7B 模型剪枝。

**[Who Taught You That Tracing Teachers In Model Distillation](who_taught_you_that_tracing_teachers_in_model_distillation.md)**

:   提出"教师模型归因"新问题：给定蒸馏后的学生模型，能否识别其教师模型？发现 n-gram 相似度和困惑度都不可靠，但词性（PoS）模板特征能有效捕捉教师模型在蒸馏中留下的语法"指纹"，在 5 个候选教师中达到 45-74% 的归因准确率（随机基线 20%）。
