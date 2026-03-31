<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM 效率

**🔬 ICLR2026** · 共 **31** 篇

**[Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation](bayesian_attention_mechanism_a_probabilistic_framework_for_positional_encoding_a.md)**

:   将位置编码重新表述为贝叶斯注意力机制中的先验分布，统一了 NoPE（均匀先验）和 ALiBi（拉普拉斯先验），并提出广义高斯先验（GGD-BAM），仅增加 384 个参数即可在 500 倍训练长度上实现完美的 passkey 检索。

**[Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding](beyond_rag_vs_long-context_learning_distraction-aware_retrieval_for_efficient_kn.md)**

:   提出 LDAR（Learning Distraction-Aware Retrieval），一个轻量级自适应检索器，通过学习基于查询-段落相似度分布选择段落的连续区间（band），在平衡信息覆盖与干扰段落影响的同时，以约一半的 token 用量超越长上下文方法的性能。

**[Did You Check the Right Pocket? Cost-Sensitive Store Routing for Memory-Augmented Agents](did_you_check_the_right_pocket_cost-sensitive_store_routing_for_memory-augmented.md)**

:   将记忆增强 Agent 的多存储检索形式化为代价敏感的存储路由问题（store routing），证明选择性检索相比全量检索可在减少 62% context token 的同时提升 QA 准确率（86% vs 81%），并提出基于语义信号的启发式路由基线。

**[EvoEngineer: Mastering Automated CUDA Kernel Code Evolution with Large Language Models](evoengineer_mastering_automated_cuda_kernel_code_evolution_with_large_language_m.md)**

:   提出 EvoEngineer，首个系统化的 LLM-based 代码演化框架，将代码演化分解为 traverse technique（含两层设计：solution guiding + prompt engineering）和 population management 两个正交组件，在 91 个真实 CUDA kernel 上实现最高 2.72× 中位加速比和 69.8% 代码有效率，在性能和正确性两个维度上超越现有方法。

**[Expert Divergence Learning for MoE-based Language Models](expert_divergence_learning_for_moe-based_language_models.md)**

:   解决 MoE 训练中的专家同质化问题，通过最大化不同数据域之间路由分布的 Jensen-Shannon 散度，鼓励不同域激活不同专家子集，在 15B-A1.5B 模型上提升专家特化程度和语言建模性能。

**[Fast Catch-Up, Late Switching: Optimal Batch Size Scheduling via Functional Scaling Laws](fast_catch-up_late_switching_optimal_batch_size_scheduling_via_functional_scalin.md)**

:   通过 Functional Scaling Law 框架理论推导出 batch size scheduling 的最优策略——对困难任务，最优策略是训练大部分时间用小 batch，仅在最后阶段切换到大 batch（late switching）；并揭示了 fast catch-up 效应——切换后 loss 迅速追上全程大 batch 的轨迹，在 1.1B 参数 1T token 的 LLM 预训练中验证了该原则。

**[IMSE: Intrinsic Mixture of Spectral Experts Fine-tuning for Test-Time Adaptation](imse_intrinsic_mixture_of_spectral_experts_fine-tuning_for_test-time_adaptation.md)**

:   提出 IMSE——将预训练 ViT 线性层通过 SVD 分解为"谱专家"，仅微调奇异值实现极端参数高效的测试时适应，并通过多样性最大化损失和域感知谱码检索机制，在 TTA/CTTA/渐进 CTTA 三种场景下达到 SOTA。

**[LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding](lycheedecode_accelerating_long-context_llm_inference_via_hybrid-head_sparse_deco.md)**

:   提出 LycheeDecode，通过将注意力头细粒度分为少量 retrieval heads（负责全注意力选关键 token）和大量 sparse heads（复用选出的 token 做稀疏计算），并用 HardKuma 分布端到端学习头类型，在 128K 上下文下实现 2.7× 加速且性能不降。

**[LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding](lycheedecode_accelerating_long-context_llm_inference_via_hybrid_speculative_deco.md)**

:   提出 LycheeDecode，一种细粒度的混合头稀疏解码方法，通过将注意力头分为少量"检索头"和大量"稀疏头"，并用 HardKuma 分布进行可微头类型识别，在 128K 上下文下实现 2.7× 加速且性能持平甚至超越全注意力基线。

**[Multilingual Routing in Mixture-of-Experts](multilingual_routing_in_mixture-of-experts.md)**

:   系统分析MoE LLM中多语言路由模式，发现中间层存在跨语言共享专家、语言性能与英语路由对齐度强相关，并提出推理时路由干预方法，通过激活英语任务专家在中间层一致性地提升多语言性能1-2%。

**[MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning](mvar_visual_autoregressive_modeling_with_scale_and_spatial_markovian_conditionin.md)**

:   提出 MVAR（Markovian Visual AutoRegressive），通过引入尺度 Markov 假设（仅依赖相邻尺度而非所有前序尺度）和空间 Markov 注意力（限制邻域大小 k），将 VAR 模型的注意力计算复杂度从 $\mathcal{O}(N^2)$ 降至 $\mathcal{O}(Nk)$，在 ImageNet 256×256 上实现同等或更优性能的同时，推理显存降低 3.0-4.2×，且仅需 8 张 RTX 4090 即可训练。

**[One-Prompt Strikes Back: Sparse Mixture of Experts for Prompt-based Continual Learning](one-prompt_strikes_back_sparse_mixture_of_experts_for_prompt-based_continual_lea.md)**

:   提出 SMoPE 框架，将单个共享 prompt 组织为稀疏 MoE 结构中的多个 prompt expert，通过 prompt-attention score aggregation 实现动态稀疏激活，在保持高参数效率的同时显著缓解知识干扰，在多个持续学习 benchmark 上达到 SOTA。

**[Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity](prior-based_noisy_text_data_filtering_fast_and_strong_alternative_for_perplexity.md)**

:   提出基于 token 词频先验（term frequency）的文本数据过滤方法，通过计算文档中 token 先验的均值和标准差来检测异常文档，实现了比 PPL 过滤快 1000× 以上且下游性能更优的数据清洗效果。

**[Prior-based Noisy Text Data Filtering: Fast and Strong Alternative for Perplexity](prior-based_noisy_text_data_filtering_fast_and_strong_alternative_to_perplexity.md)**

:   提出基于 token 先验（词频统计）的文本数据过滤方法，利用文档内 token 先验的均值和标准差作为 PPL 的近似替代，在 20 个下游基准上取得最高平均性能，同时比 PPL 过滤快 1000 倍以上。

**[Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training](q_rag_long_context_multi_step_retrieval.md)**

:   将多步检索建模为 MDP，用基于值的 RL（soft Q-learning）微调 **embedder 而非 LLM**，Q 函数设计为状态嵌入和动作嵌入的内积（理论证明为万能近似器），结合 RoPE 相对位置编码实现时序推理，在单卡 A100 上训练 12 小时，4K 训练泛化到 1M+ token 上下文，RULER 基准达到近乎完美的 NIAH 性能。

**[RACE Attention: A Strictly Linear-Time Attention for Long-Sequence Training](race_attention_a_strictly_linear-time_attention_for_long-sequence_training.md)**

:   提出 RACE Attention——用幂次角核替代 softmax 并通过可微 LSH 草图近似注意力输出，实现严格线性时间复杂度，支持单 GPU 处理 1200 万 token、单 CPU 处理 7500 万 token，在多种任务上匹配或超越 softmax 精度。

**[Randomization Boosts KV Caching, Learning Balances Query Load: A Joint Perspective](randomization_boosts_kv_caching_learning_balances_query_load_a_joint_perspective.md)**

:   提出首个KV缓存感知负载均衡统一数学模型，设计随机化叶节点淘汰算法RLT(O(log n)竞争比)和基于学习的贪心路由LBGR，在多LLM服务场景下将延迟降低最高11.96×、TTFT降低14.06×。

**[Rethinking Benign Relearning Syntax As The Hidden Driver Of The Safety Tax](rethinking_benign_relearning_syntax_as_the_hidden_driver_of_the_safety_tax.md)**

:   本文揭示了 LLM 机器遗忘中"良性重学习"（benign relearning）的真正驱动因素不是主题相关性而是**句法相似性**，并提出**句法多样化（syntactic diversification）**策略来提升遗忘的鲁棒性。

**[Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures](rethinking_benign_relearning_syntax_as_the_hidden_driver_of_unlearning_failures.md)**

:   揭示 LLM 机器遗忘中"良性重学习"现象的真正驱动因素是句法相似性而非主题相关性，并提出句法多样化策略（paraphrase forget set），有效抑制重学习、加速遗忘并缓解遗忘效果与模型效用之间的 trade-off。

**[Rethinking Uncertainty Estimation in LLMs: A Principled Single-Sequence Measure](rethinking_uncertainty_estimation_in_llms_a_principled_single-sequence_measure.md)**

:   从 proper scoring rules 框架出发，证明最高概率输出序列的负对数似然（MSP）是理论上合理的不确定性度量，并提出 G-NLL——仅用一次贪心解码就能逼近该度量，在多个场景下匹配或超越需要多次采样的 SOTA 方法。

**[Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling](semantic_parallelism_redefining_efficient_moe_inference_via_model-data_co-schedu.md)**

:   提出语义并行(Semantic Parallelism)范式，通过预测token-expert路由路径并协同调度模型放置与数据分发，大幅削减MoE推理中专家并行的all-to-all通信开销，在Attention-DP场景下吞吐提升最高2.78×，Attention-TP场景下延迟降低最高24.9%。

**[Steering Language Models with Weight Arithmetic](steering_language_models_with_weight_arithmetic.md)**

:   提出对比式权重引导（Contrastive Weight Steering），通过对正/负行为微调模型的权重差来提取行为方向向量，直接修改模型权重实现行为控制，在谄媚性、恶意性和拒绝性实验中比激活引导（Activation Steering）具有更好的泛化能力和一致性。

**[Stretching Beyond the Obvious: A Gradient-Free Framework to Unveil the Hidden Landscape of Visual Invariance](stretching_beyond_the_obvious_a_gradient-free_framework_to_unveil_the_hidden_lan.md)**

:   提出 Stretch-and-Squeeze（SnS）算法，一个无梯度、模型无关的双目标优化框架，通过在不同处理层级"拉伸"表征同时"压缩"目标单元激活来系统性地探测视觉系统的不变性流形，揭示了标准与鲁棒 CNN 之间不变性可解释性的分层差异。

**[SwingArena: Adversarial Programming Arena for Long-context GitHub Issue Solving](swingarena_competitive_programming_arena_for_long-context_github_issue_solving.md)**

:   提出SwingArena对抗性评测框架，让LLM交替扮演提交者(生成补丁)和审查者(编写测试)，通过真实CI流水线验证，覆盖C++/Python/Rust/Go四种语言的400个GitHub issue，揭示不同模型在补丁生成vs验证方面的行为差异。

**[Token-level Data Selection for Safe LLM Fine-tuning](token-level_data_selection_for_safe_llm_fine-tuning.md)**

:   提出 TOSS（Token-level data Selection for Safe LLM fine-tuning），首个 token 级别的数据选择框架,通过安全退化模型和效用导向模型之间的损失差评估每个 token 的安全风险，实现比样本级方法更优的安全-效用权衡。

**[TokenSeek: Memory Efficient Fine Tuning via Instance-Aware Token Ditching](tokenseek_memory_efficient_fine_tuning_via_instance-aware_token_ditching.md)**

:   提出 TokenSeek，一个通用的 Transformer 微调内存优化插件，通过结合上下文注意力信息和梯度信息进行实例级 token 重要性评估，仅保留 10% 高价值 token 参与梯度更新，实现最高 65.7% 内存节省且性能持平甚至超越全 token 微调。

**[TokenSeek: Memory Efficient Fine Tuning via Instance-Aware Token Selection](tokenseek_memory_efficient_fine_tuning_via_instance-aware_token_selection.md)**

:   提出 TokenSeek，一个通用的实例感知 token 搜索与丢弃方法，通过结合上下文（注意力）和梯度信息评估每个 token 的重要性，仅在选中的 token 上更新参数，实现激活内存的大幅减少（最高 65.7%）而保持甚至超越全 token 微调性能。

**[Understanding and Improving Length Generalization in Hierarchical Sparse Attention Models](understanding_and_improving_length_generalization_in_hierarchical_sparse_attenti.md)**

:   系统解剖基于 chunk 的稀疏注意力架构，识别出三个关键设计原则（非线性 Chunk Encoder + CLS token、Bypassing Residual Path、训练时强制选择稀疏性），将 4K 上下文训练的模型成功外推到 3200 万 token。

**[Universe Routing: Why Self-Evolving Agents Need Epistemic Control](universe_routing_why_self-evolving_agents_need_epistemic_control.md)**

:   形式化"宇宙路由"问题——将问题分类到互斥的信念空间（频率主义/贝叶斯/经典物理/量子等）后再调用专用求解器，证明硬路由优于软路由（7× 快且等精度），且模块化架构天然适合持续学习。

**[When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework](when_does_divide_and_conquer_work_for_long_context_llm_a_noise_decomposition_fra.md)**

:   提出理论框架将长上下文任务失败分解为三类噪声（任务噪声/模型噪声/聚合器噪声），证明当模型噪声超线性增长时弱模型+分块处理可超越强模型单次处理，并给出快速估计最优 chunk size 的方法（3-5 个样本即可）。

**[xLSTM Scaling Laws: Competitive Performance with Linear Time-Complexity](xlstm_scaling_laws_competitive_performance_with_linear_time-complexity.md)**

:   系统对比 xLSTM 与 Transformer 的 scaling law，证明 xLSTM 在训练损失-算力 Pareto 前沿、过训练 regime 和推理速度上全面优于同规模 Transformer，且优势随上下文长度增大而增长。
