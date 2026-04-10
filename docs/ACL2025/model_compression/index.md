<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**💬 ACL2025** · 共 **55** 篇

**[AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](aligndistil_token_level_alignment.md)**

:   AlignDistil 证明了 RLHF 目标函数与 token 级蒸馏过程的理论等价性，并据此设计了一种简单的蒸馏方法：用 DPO 模型和反向 DPO 模型的 logit 分布线性组合构造教师分布，配合 token 自适应外推机制实现 token 级奖励优化，在 AlpacaEval 2.0、MT-Bench 和 Arena-Hard 上优于现有方法且收敛更快。

**[APB: Accelerating Distributed Long-Context Inference by Passing Compressed Context Blocks across GPUs](apb_distributed_long_context.md)**

:   APB 提出了一种分布式长上下文推理框架，通过在序列并行框架中引入本地 KV cache 压缩和跨 GPU 传递压缩上下文块的机制，在不损失任务性能的前提下实现了相比 FlashAttn/RingAttn/StarAttn 分别高达 9.2x/4.2x/1.6x 的 prefill 加速。

**[ODLRI: Assigning Distinct Roles to Quantized and Low-Rank Matrices Toward Optimal Weight Decomposition](assigning_distinct_roles_to_quantized_and_low-rank_matrices_toward_optimal_weigh.md)**

:   提出 ODLRI（Outlier-Driven Low-Rank Initialization）——在量化+低秩联合权重分解 $\mathbf{W} \approx \mathbf{Q} + \mathbf{LR}$ 中，将低秩分量专门分配给捕获激活敏感权重（异常值相关），量化分量处理剩余权重。通过这种"角色分配"初始化，稳定量化、降低激活感知误差，在 Llama2/3 和 Mistral 的低比特设置中一致提升困惑度和零样本精度。

**[BeamLoRA: Beam-Constraint Low-Rank Adaptation](beamlora_beam_constraint_lora.md)**

:   BeamLoRA 发现 LoRA 模块中不同 rank 的重要性存在显著差异且随训练动态演变，受 beam search 启发，提出在训练过程中动态评估 rank 重要性、剪枝不重要的 rank 并将参数空间扩展给重要 rank，在固定总 rank 下提升性能，在三个基座模型的 12 个数据集上持续优于 LoRA 及其变体。

**[Beyond Text Compression: Evaluating Tokenizers Across Scales](beyond_text_compression_tokenizers.md)**

:   本文系统评估了 6 种 tokenizer 在 350M 和 2.7B 参数模型上的影响，发现 tokenizer 选择对英文任务影响极小但对多语言任务（如机器翻译）有显著且跨尺度一致的影响，并提出了基于 Zipf 定律的新型内在评估指标，比文本压缩率能更好地预测多语言场景下的下游性能。

**["Give Me BF16 or Give Me Death"? Accuracy-Performance Trade-Offs in LLM Quantization](bf16_or_death_quantization_tradeoffs.md)**

:   这是迄今最全面的 LLM 量化实证研究，在 Llama-3.1 全系列（8B/70B/405B）上对 FP8/INT8/INT4 进行了超过 50 万次评估，发现 FP8 几乎无损、INT8 仅降 1-3%、INT4 出奇地有竞争力，并给出了不同部署场景的量化格式选择建议。

**[BlockPruner: Fine-grained Pruning for Large Language Models](blockpruner_fine-grained_pruning_for_large_language_models.md)**

:   提出 BlockPruner，将 Transformer 层分解为 MHA 和 MLP 两个最小残差块，基于困惑度评估块重要性并通过迭代搜索进行细粒度剪枝，实现比层级剪枝更优的压缩效果。

**[BrainECHO: Semantic Brain Signal Decoding through Vector-Quantized Spectrogram Reconstruction for Whisper-Enhanced Text Generation](brainecho_semantic_brain_signal_decoding_through_vector-quantized_spectrogram_re.md)**

:   提出 BrainECHO 三阶段框架（自编码—对齐—微调），通过向量量化离散表示将脑信号映射到 Mel 频谱图空间，再借助 Whisper 完成非侵入式脑信号到文本的高质量解码。

**[Capture the Key in Reasoning to Enhance CoT Distillation Generalization](capture_key_cot_distillation.md)**

:   提出 EDIT（mistakE-Driven key reasonIng step distillaTion），通过构造正确/错误配对的 dual CoTs 数据，利用最小编辑距离算法定位关键推理步骤，并以 token 级细粒度损失函数引导小模型聚焦学习这些关键步骤，而非简单模仿教师的推理形式。

**[Correcting Hallucinations in News Summaries: Exploration of Self-Correcting LLM Methods with External Knowledge](correcting_hallucinations_in_news_summaries_exploration_of_self-correcting_llm_m.md)**

:   系统性地探究了两种自纠正方法（CoVE 和 RARR）在新闻摘要幻觉纠正中的表现，比较了三种搜索引擎、多种检索设置和提示策略，发现 Bing 搜索片段 + RARR（few-shot）组合效果最佳，且 G-Eval 与人类评估高度一致。

**[Cross-Lingual Generalization and Compression: From Language-Specific to Shared Neurons](cross_lingual_neurons_compression.md)**

:   本文通过追踪多语言语言模型预训练过程中的检查点，发现模型从语言特定表示逐渐压缩为跨语言共享表示：中间层的语言识别能力下降、语义概念的"专家神经元"跨语言对齐，操控从西班牙语数据提取的概念神经元后模型反而生成语义相关的英语文本。

**[DAC: A Dynamic Attention-aware Approach for Task-Agnostic Prompt Compression](dac_prompt_compression.md)**

:   DAC 提出动态注意力感知的 prompt 压缩方法，通过融合信息熵和注意力分数作为 token 重要性度量，并动态感知压缩过程中的熵偏移来进行细粒度压缩，在 LongBench 上比 SOTA 方法提升平均 1.33 分。

**[DeepSolution: Boosting Complex Engineering Solution Design via Tree-based Exploration and Bi-point Thinking](deepsolution_boosting_complex_engineering_solution_design_via_tree-based_explora.md)**

:   提出面向复杂工程方案设计的新基准 SolutionBench 和新系统 SolutionRAG，通过树搜索探索+双视角思维（设计-审查交替）在 RAG 框架下逐步生成满足多约束的可靠工程方案，在 8 个工程领域达到 SOTA。

**[Direct Behavior Optimization: Unlocking the Potential of Lightweight LLMs](direct_behavior_optimization_unlocking_the_potential_of_lightweight_llms.md)**

:   提出 DeBoP 范式，将轻量级 LLM（LwLLM）的行为优化转化为对离散执行序列的优化，通过无梯度蒙特卡洛树搜索（MCTS）自动寻找最优 demonstration，使 LLaMA3-8B 在多数任务上超越 GPT-3.5 并减少约 60% 计算时间。

**[DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination](drag_distilling_rag_slm.md)**

:   DRAG 提出了一种从大模型向小模型蒸馏 RAG 能力的框架：用大模型（如 GPT-4o）为给定问题生成证据和知识图谱三元组，经排序过滤后作为结构化上下文输入给小模型（2B-9B），无需微调即可将小模型在 ARC-C 上提升高达 27.7%，同时显著减少幻觉。

**[DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization](drpruning_robust_pruning.md)**

:   DRPruning 将分布稳健优化（DRO）引入 LLM 结构化剪枝，通过 scaling law 预测各领域最终 loss 作为参考、动态调整训练数据分布来平衡剪枝后各领域性能，在单语和多语设置下分别以 -5.59% PPL 和 +2.95% 下游任务的提升超越 Sheared LLaMA。

**[EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](eac_moe_expert_aware_compression.md)**

:   EAC-MoE 从 MoE 模型的专家选择特性出发，提出量化时校准路由器缓解 expert-shift 问题（QESC）+ 推理时基于专家选择频率动态剪枝不重要专家（PESF），在 Mixtral-8x7B 上实现 4.92× 内存压缩和 1.68× 推理加速且精度损失不到 1%。

**[EfficientQAT: Efficient Quantization-Aware Training for Large Language Models](efficientqat.md)**

:   EfficientQAT 提出两阶段 QAT 框架——先逐块训练所有参数（Block-AP）提供良好初始化，再端到端训练量化参数（E2E-QP）捕获跨块交互，在单张 A100 上 41 小时完成 Llama-2-70B 的 2-bit 量化，精度仅降 3 点。

**[Entropy-based Exploration Conduction for Multi-step Reasoning](entropy-based_exploration_conduction_for_multi-step_reasoning.md)**

:   提出 Entro-duction 方法，通过监控 LLM 推理过程中输出的熵和方差熵变化来动态调整探索深度，使用 $\epsilon$-greedy 策略选择加深、扩展或停止三种探索行为，在避免冗余推理的同时提升推理准确率。

**[EXIT: Context-Aware Extractive Compression for Enhancing Retrieval-Augmented Generation](exit_context-aware_extractive_compression_for_enhancing_retrieval-augmented_gene.md)**

:   提出 EXIT——一种抽取式上下文压缩框架，通过上下文感知的句子级二分类并行选取与查询相关的句子，在 QA 准确率和推理延迟上同时优于现有的抽生式和抽取式压缩方法。

**[Explaining Puzzle Solutions in Natural Language: An Exploratory Study on 6×6 Sudoku](explaining_puzzle_solutions_in_natural_language_an_exploratory_study_on_6x6_sudo.md)**

:   评估 5 个 LLM 在解决和解释 6×6 数独谜题上的能力，发现开源模型几乎无法正确求解（<1%），o1-preview 可解 65% 但其解释在正当性、清晰度和教育价值三个维度上均严重不足，揭示了 LLM 在多步推理解释方面的根本局限。

**[FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning of Large Language Models](fedex_lora_federated_exact_aggregation.md)**

:   FedEx-LoRA 发现联邦学习中独立平均 LoRA 的 A 和 B 矩阵会导致不精确的全局更新（"乘积的均值≠均值的乘积"），通过在冻结权重矩阵中加入残差误差项实现精确聚合，在多个推理和 NLU 任务上一致优于 FedIT 和 FFA-LoRA。

**[Language Fusion for Parameter-Efficient Cross-lingual Transfer (FLARE)](flare_crosslingual_lora.md)**

:   FLARE 在 LoRA 适配器的低秩瓶颈中通过轻量线性/非线性变换融合源语言（英语）和目标语言的逐层表示，无需额外参数即可实现参数高效的跨语言迁移，在 Llama 3.1 上 QA 精确匹配提升 4.9%。

**[Flipping Knowledge Distillation: Leveraging Small Models' Expertise to Enhance LLMs in Text Matching](flipping_kd_small_to_large.md)**

:   本文提出"反向知识蒸馏"范式——让 LLM 从微调过的小模型学习文本匹配的领域专家知识，通过将 decoder-only LLM 重新解释为 encoder-decoder 架构（用 LoRA 的压缩矩阵做 encoder）并设计 Margin-aware Contrastive Loss 来对齐表示相似度。

**[A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](gist_token_context_compression.md)**

:   系统研究Gist Token上下文压缩方法，提出统一框架分类现有架构（记忆位置×粒度），发现Fine-grained KV Cache在RAG/QA上近无损但在合成召回上有明显缺陷，识别出三种失败模式（边界丢失/意外丢失/中途丢失），并提出细粒度自编码和分段token重要性估计两种改进策略。

**[Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning](graph_counselor_multiagent_graphrag.md)**

:   Graph Counselor 提出了一个多智能体协作的 GraphRAG 推理框架，通过 Planning/Thought/Execution 三个 Agent 自适应提取图结构信息，并引入多视角自反思机制纠正推理偏差，在多个图推理任务上超越现有方法。

**[IAM: Efficient Inference through Attention Mapping between Different-scale LLMs](iam_efficient_inference_through_attention_mapping_between_different-scale_llms.md)**

:   发现不同规模 LLM 的注意力矩阵具有高度相似性，提出 IAM 框架——在 prefill 阶段建立小模型与大模型注意力头之间的余弦相似度映射，decode 阶段用小模型的注意力矩阵替代大模型映射层的注意力计算，实现 KV cache 减少 22% 和推理加速 11%，且与现有 KV cache 压缩方法正交。

**[L4Q: Parameter Efficient Quantization-Aware Fine-Tuning on Large Language Models](l4q_parameter_efficient_quantization_aware_finetuning.md)**

:   提出 L4Q，将量化感知训练 (QAT) 与 LoRA 深度整合：先合并权重与LoRA参数再统一量化，通过定制反向传播路径消除权重梯度存储开销，实现联合优化量化与微调参数，在4-bit和3-bit量化下显著超越现有方法。

**[Lacuna Inc. at SemEval-2025 Task 4: LoRA-Enhanced Influence-Based Unlearning for LLMs](lacuna_inc_at_semeval-2025_task_4_lora-enhanced_influence-based_unlearning_for_l.md)**

:   提出 LIBU（LoRA 增强的影响函数遗忘算法），分两阶段实现 LLM 机器遗忘：Phase 1 用对角 Fisher 信息矩阵加权的影响函数更新参数精准遗忘，Phase 2 用 Sophia 二阶优化器稳定化训练，在 SemEval-2025 Task 4 的 OLMo-7B 上达到 0.283 遗忘率同时维持 0.469 MMLU 准确率。

**[Language Models Resist Alignment: Evidence From Data Compression](language_models_resist_alignment.md)**

:   本文从压缩理论视角揭示了LLM存在"弹性"(elasticity)现象——模型倾向于保持预训练分布而抵触对齐分布，且对齐后的模型在受到扰动时会以与数据量差距成反比的速率回弹到预训练状态，这解释了为什么对齐如此脆弱且容易被少量微调逆转。

**[Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders](language_specific_features.md)**

:   利用 Sparse Autoencoders (SAEs) 分析多语言 LLM 的内部表示，发现存在强烈的语言特定 SAE features，这些 features 不仅与语言特有 token 相关还与语言上下文相关，消融它们只影响对应语言能力，且多个语言 features 之间存在协同效应；进一步利用这些 features 增强 steering vectors 实现对生成语言的精确控制。

**[Towards the Law of Capacity Gap in Distilling Language Models](law_of_capacity_gap_distilling_language_models.md)**

:   揭示了语言模型蒸馏中的"容量差距定律"——最优教师模型的参数量与学生模型成线性关系（约 2.5 倍），将 LLM 蒸馏中的"不可能三角"转化为可解问题，并据此成功蒸馏出 3B 的 MiniMA 模型。

**[Memorization Inheritance in Sequence-Level Knowledge Distillation for Neural Machine Translation](memorization_inheritance_seqkd.md)**

:   本文首次系统研究了序列级知识蒸馏（SeqKD）中教师模型的记忆行为如何传递给学生模型，发现学生模型虽未直接接触原始训练数据，但其提取式记忆率比基线模型高 57%，幻觉率也增加，并提出 Adaptive-SeqKD 通过在高质量子集上微调教师来缓解这些问题。

**[MoQAE: Mixed-Precision Quantization for Long-Context LLM Inference via Mixture of Quantization-Aware Experts](moqae_mixed_precision_kv_cache.md)**

:   MoQAE 创造性地将不同量化比特宽度配置视为 MoE 中的"专家"，通过轻量路由器学习每个 chunk 的最优量化策略，结合路由冻结和路由共享机制，在几乎不损失精度的情况下大幅减少长上下文推理的 KV cache 内存。

**[mPLUG-DocOwl2: High-resolution Compressing for OCR-free Multi-page Document Understanding](mplug_docowl2_doc_compress.md)**

:   提出High-resolution DocCompressor模块，利用低分辨率全局视觉特征作为query通过交叉注意力将高分辨率文档图像压缩为仅324个token（不到同类方法的20%），在多页文档理解benchmark上达到SOTA且首token延迟降低50%+。

**[Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging](osrm_lora_merging_orthogonal.md)**

:   OSRM 发现 LoRA 模型合并失败的根因是参数与数据分布的交互干扰（而非仅仅是参数冲突），提出在微调前通过数据协方差矩阵的特征分解来初始化 LoRA 矩阵 A，使其子空间与其他任务的数据分布正交，从而在合并时最小化跨任务干扰，在 8 个数据集、5 个模型上显著提升合并性能。

**[C3A: 基于循环卷积的参数高效微调](parameter-efficient_fine-tuning_via_circular_convolution.md)**

:   提出Circular Convolution Adaptation (C3A)，用循环卷积算子替代LoRA的低秩矩阵分解来构造增量权重$\Delta W$——循环矩阵的秩与可训练参数数量解耦，实现"少参数+高秩"适配；同时利用FFT加速前向/反向传播，在计算和显存效率上均可与LoRA媲美。在GLUE、常识推理、数学推理、代码生成等任务上持续优于LoRA及其变体。

**[Prompt Candidates, then Distill: A Teacher-Student Framework for LLM-driven Data Annotation](prompt_distill_teacher_student.md)**

:   提出候选标注+蒸馏范式（CanDist）——当 LLM 对样本不确定时输出所有可能标签（而非强制给唯一标签），然后用小语言模型（SLM）从候选标注中蒸馏出唯一标签，理论证明候选标注蒸馏比直接使用单标签有更好的理论保证，在六个文本分类任务上验证有效。

**[PTQ1.61: Push the Real Limit of Extremely Low-Bit Post-Training Quantization Methods for Large Language Models](ptq161_low_bit_quantization.md)**

:   首次将LLM权重真正量化到1.61-bit（此前号称sub-2bit的方法实际都超过2bit），通过一维结构化掩码（仅增加0.0002-bit/权重）保留显著通道、块级缩放因子优化和量化预处理三大创新，在LLaMA系列上以更低比特超越BiLLM和PB-LLM。

**[Quaff: Quantized Parameter-Efficient Fine-Tuning under Outlier Spatial Stability Hypothesis](quaff_quantized_peft.md)**

:   本文提出 Outlier Spatial Stability Hypothesis (OSSH)——微调期间激活异常通道的空间位置保持稳定——并基于此设计了 Quaff 框架，通过目标动量缩放仅处理少量不变的异常通道，实现 1.73× 延迟降低和 30% 内存节省，同时在 GPQA 上精度还提升了 0.6%。

**[Revisiting LoRA through the Lens of Parameter Redundancy: Spectral Encoding Helps](revisiting_lora_through_the_lens_of_parameter_redundancy_spectral_encoding_helps.md)**

:   本文系统研究了 LoRA 微调中的参数冗余问题，发现降低密度冗余不会损害表达能力（稀疏性质），并提出 SeLoRA——利用频谱变换（Fourier/Wavelet）从稀疏频谱子空间重参数化 LoRA 矩阵，以更少参数实现更优性能，且可即插即用地集成到多种 LoRA 变体中。

**[RISE: Reasoning Enhancement via Iterative Self-Exploration in Multi-hop Question Answering](rise_reasoning_enhancement_via_iterative_self-exploration_in_multi-hop_question_.md)**

:   提出 RISE——结合 RAG 与自迭代训练的多跳问答框架，通过问题分解、检索阅读、自我批判三个动作的自我探索循环，迭代生成训练数据并多目标优化模型，在 2Wiki/HotpotQA/MuSiQue 上超越 GPT-3.5 和所有 8B 级基线。

**[Sci-LoRA: Mixture of Scientific LoRAs for Cross-Domain Lay Paraphrasing](sci-lora_mixture_of_scientific_loras_for_cross-domain_lay_paraphrasing.md)**

:   提出 Sci-LoRA——一种混合多领域 LoRA 的框架，通过对比学习训练文本编码器+动态权重生成器+LoRA 融合模块，在无需领域标签的情况下实现跨12个学科领域的科学文本通俗化改写，在5个数据集10个指标上超越 SOTA。

**[SEE: Strategic Exploration and Exploitation for Cohesive In-Context Prompt Optimization](see_strategic_exploration_exploitation_prompt_optimization.md)**

:   本文提出 SEE 框架，首次将指令（instruction）和示例（examples）作为整体进行联合优化，采用元启发式优化原则设计四阶段探索-利用策略，在35个基准任务上实现平均13.94%的准确率提升并降低58.67%的计算成本。

**[Mitigating Selection Bias with Node Pruning and Auxiliary Options](selection_bias_node_pruning.md)**

:   提出Bias Node Pruning (BNP)和Auxiliary Option Injection (AOI)两种互补方法，从模型内部和输入端同时缓解LLM在多选题中的选择偏差，仅剪除0.002%权重即可将Llama-3准确率从52.3%提升至65.3%（+24.9%组合提升）。

**[Semantic Exploration with Adaptive Gating for Efficient Problem Solving with Language Models](semantic_exploration_adaptive_gating.md)**

:   针对 LLM 树搜索推理中"简单题也做复杂搜索"和"语义重复路径反复扩展"两大浪费问题，提出 SEAG 框架：先用 entropy 门控决定是否启动树搜索，再用语义聚类合并等价推理步骤，最终在准确率平均提升 4.3% 的同时仅需 RAP 31% 的推理开销。

**[State-offset Tuning: State-based Parameter-Efficient Fine-Tuning for State Space Models](state_offset_tuning_ssm_peft.md)**

:   针对 SSM（如 Mamba）提出 State-offset Tuning，一种新的"状态基"PEFT 方法家族，通过在每个时间步直接注入可训练的状态偏移量 $h'$ 替代 Prefix-Tuning 的虚拟 token，解决了 prompt-based 方法在 SSM 上表达能力受限的问题，在更少参数量下持续优于 LoRA 和 Prefix-Tuning。

**[STUN: Structured-Then-Unstructured Pruning for Scalable MoE Pruning](stun_moe_pruning.md)**

:   STUN 提出了结构化→非结构化的两阶段 MoE 剪枝方法，第一阶段用 O(1) 前向传播实现可扩展的专家级剪枝，第二阶段在剩余专家内做非结构化剪枝，在 480B 参数的 Snowflake Arctic 上以 40% 稀疏度几乎无性能损失。

**[TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](table_lora_structure_understanding.md)**

:   TableLoRA 提出面向表格任务的专用 LoRA 模块，通过特殊 token 编码器改善表格序列化，并用 2D LoRA 编码单元格的行列位置信息，在参数高效微调设置下相比 vanilla LoRA 在 HiTab 上提升 5.9%，弥合了 LoRA 与全量微调之间 40.56% 的性能差距。

**[TaDA: Training-free recipe for Decoding with Adaptive KV Cache Compression and Mean-centering](tada_training-free_recipe_for_decoding_with_adaptive_kv_cache_compression_and_me.md)**

:   提出 TaDA——无需训练的 KV cache 压缩方法，通过对 K/V 激活做 head 维度均值中心化后量化偏差（而非原始激活），自动消除离群值问题，配合逐层自适应量化精度搜索，将 KV cache 压缩至原始 16 位的 27% 同时保持接近基线的精度。

**[Trans-PEFT: Transferable Parameter-Efficient Fine-Tuning on Evolving Base Models](trans_peft_transferable.md)**

:   Trans-PEFT 发现基座模型更新（如 Qwen2→Qwen2.5）主要改变 FFN 层的任务知识存储而较少影响 Attention 层的任务模式，据此提出层内知识掩码和跨层知识丢弃两种策略，使在旧版本上训练的 PEFT 模块可直接迁移到新版本而不需重新微调，性能提升可达 30%。

**[UniICL: An Efficient ICL Framework Unifying Compression, Selection, and Generation](uniicl_icl_framework.md)**

:   提出 UniICL 框架，用**一个冻结的 LLM** 同时完成 demonstration 压缩（compress→virtual tokens）、demonstration 选择（基于压缩后的 virtual token 相似度排序）和最终响应生成三个任务，仅需 17M 可训练参数（projection layer + learnable embedding），配合 Demonstration Bank 缓存机制避免重复压缩，实现 12× 压缩率下从 4-shot 扩展到 64-shot ICL（24GB 显存内），在多个 out-of-domain 数据集上超越 AutoCompressor、ICAE、LLMLingua 等基线。

**[UniQuanF: Unifying Uniform and Binary-coding Quantization for Accurate Compression of Large Language Models](uniquanf_unified_quantization.md)**

:   UniQuanF 统一了均匀量化（UQ,表现力弱但优化性强）和二进制编码量化（BCQ,表现力强但优化性差）的优势，通过统一初始化、局部周期映射和统一定理，实现无额外部署开销的高精度 LLM 量化，在 GSM8K 上提升最高 4.60%。

**[Wanda++: Pruning Large Language Models via Regional Gradients](wanda_pruning_large_language_models_via_regional_gradients.md)**

:   提出 Wanda++——基于 decoder block 级别区域梯度的轻量级 LLM 剪枝框架，通过区域梯度评分（RGS）改进剪枝准则 + 区域优化（RO）最小化稠密/稀疏块输出差异，在 2:4 稀疏下 WikiText 困惑度较 Wanda 最高降低 32%，单 H100 GPU 10 分钟内完成 7B 模型剪枝。

**[Who Taught You That? Tracing Teachers in Model Distillation](who_taught_you_that_tracing_teachers_in_model_distillation.md)**

:   提出"教师模型归因"新问题：给定蒸馏后的学生模型，能否识别其教师模型？发现 n-gram 相似度和困惑度都不可靠，但词性（PoS）模板特征能有效捕捉教师模型在蒸馏中留下的语法"指纹"，在 5 个候选教师中达到 45-74% 的归因准确率（随机基线 20%）。
