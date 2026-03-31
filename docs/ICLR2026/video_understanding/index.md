<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🔬 ICLR2026** · 共 **22** 篇

**[A.I.R.: Adaptive, Iterative, and Reasoning-based Frame Selection For Video Question Answering](air_enabling_adaptive_iterative_and_reasoning-based_frame_selection_for_video_qu.md)**

:   提出 A.I.R.，一种无需训练的自适应-迭代-推理驱动帧选择框架，通过两阶段策略（GMM 自适应初始采样 + 迭代式 VLM 精细分析）解决 VideoQA 中轻量模型（CLIP）相似度不准确和 VLM 分析成本爆炸的双重困境，在最坏情况下也仅需分析 72 帧（vs 基线 128 帧），同时显著提升多个长视频 benchmark 性能。

**[BindWeave: Subject-Consistent Video Generation via Cross-Modal Integration](bindweave_subject-consistent_video_generation_via_cross-modal_integration.md)**

:   BindWeave 用多模态大语言模型（MLLM）替代传统的浅层融合机制来解析多主体复杂文本指令，生成主体感知的隐状态作为 DiT 的条件信号，结合 CLIP 语义特征和 VAE 细粒度外观特征，实现高保真、主体一致的视频生成。

**[Decoding Open-Ended Information Seeking Goals from Eye Movements in Reading](decoding_open-ended_information_seeking_goals_from_eye_movements_in_reading.md)**

:   提出从阅读时眼动轨迹解码开放式信息检索目标的新任务，基于 OneStop 眼动数据集（360人、486问题、162段落），开发判别式和生成式多模态模型；RoBERTEye-Fixations 在三选一目标选择上达 49.3%（随机 33%），不同 critical span 达 70.9%；DalEye-Llama/GPT 在目标重建中也显著优于无眼动基线。

**[Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought](emergence_of_superposition_unveiling_the_training_dynamics_of_chain_of_continuou.md)**

:   从理论上分析了两层 Transformer 在有向图可达性问题上使用连续 Chain-of-Thought（Coconut）训练时的训练动力学，揭示了"叠加态"（superposition）机制如何自然涌现：index-matching logit 先增长后有界，从而在探索与利用之间取得平衡。

**[FlashVID: Efficient Video Large Language Models via Training-free Tree-Based Spatiotemporal Token Merging](flashvid_efficient_video_large_language_models_via_training-free_tree-based_spat.md)**

:   提出 FlashVID，一个免训练的视频大语言模型推理加速框架，通过树状时空 token 合并（TSTM）联合建模空间和时间冗余，仅保留 10% 的视觉 token 就能保持 LLaVA-OneVision 99.1% 的性能，并能将 Qwen2.5-VL 的输入帧数提升 10 倍。

**[FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding](floc_facility_location-based_efficient_visual_token_compression_for_long_video_u.md)**

:   提出 FLoC，基于设施选址函数（facility location function）的视觉 token 压缩框架，通过子模优化在给定预算下快速选择兼具代表性和多样性的 token 子集，实现无训练、模型无关、查询无关的长视频理解 token 压缩。

**[From Vicious to Virtuous Cycles: Synergistic Representation Learning for Unsupervised Video Object-Centric Learning](from_vicious_to_virtuous_cycles_synergistic_representation_learning_for_unsuperv.md)**

:   发现 slot-based 目标中心学习中编码器（产生尖锐但有噪声的注意力图）与解码器（产生空间一致但模糊的重建掩码）之间的恶性循环，提出同步对比学习目标和 slot 正则化预热策略将其转化为良性循环，在 MOVi 和 YouTube-VIS 上大幅提升物体发现性能。

**[GOT-Edit: Geometry-Aware Generic Object Tracking via Online Model Editing](got-edit_geometry-aware_generic_object_tracking_via_online_model_editing.md)**

:   通过零空间约束的在线模型编辑，将 VGGT 提供的 3D 几何信息融入 2D 通用目标跟踪器中，在保持语义判别力的同时增强几何感知能力，在遮挡和背景杂乱场景中显著提升跟踪性能。

**[JavisDiT: Joint Audio-Video Diffusion Transformer with Hierarchical Spatio-Temporal Prior Synchronization](javisdit_joint_audio-video_diffusion_transformer_with_hierarchical_spatio-tempor.md)**

:   提出 JavisDiT，基于 DiT 架构的音视频联合生成模型，通过层级化时空同步先验估计器（HiST-Sypo）实现细粒度的音视频时空对齐；同时构建了新基准 JavisBench（10K 复杂场景样本）和新评估指标 JavisScore。

**[Language-guided Open-world Video Anomaly Detection under Weak Supervision](language-guided_open-world_video_anomaly_detection_under_weak_supervision.md)**

:   提出语言引导的开放世界视频异常检测范式 LaGoVAD，通过将异常定义建模为随机变量并以自然语言形式输入，从理论上规避概念漂移问题；同时构建了目前最大规模的视频异常数据集 PreVAD（35K 视频），在七个数据集上零样本 SOTA。

**[Let's Split Up: Zero-Shot Classifier Edits for Fine-Grained Video Understanding](lets_split_up_zero-shot_classifier_edits_for_fine-grained_video_understanding.md)**

:   提出了"类别拆分"(Category Splitting)新任务，通过挖掘视频分类器权重中的潜在组合结构，在零样本条件下将粗粒度动作类别拆分为细粒度子类别，无需重训或额外数据。

**[Log Probability Tracking of LLM APIs](log_probability_tracking_of_llm_apis.md)**

:   提出 Logprob Tracking (LT) 方法，仅用单token输入和单token输出的log概率即可检测LLM API的微小变更（如单步微调），灵敏度比现有方法高2-3个数量级，成本低1000倍。

**[LUMINA: Detecting Hallucinations in RAG System with Context-Knowledge Signals](lumina_detecting_hallucinations_in_rag_system_with_context-knowledge_signals.md)**

:   提出 Lumina 框架，通过"上下文-知识信号"检测RAG系统中的幻觉：用MMD度量**外部上下文利用**程度，用跨层token预测演化度量**内部知识利用**程度，无需超参调优即可泛化。

**[Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective](lumos-1_on_autoregressive_video_generation_with_discrete_diffusion_from_a_unifie.md)**

:   提出 Lumos-1，一个基于 LLM 架构的统一视频生成模型：通过 MM-RoPE（分布式多模态 RoPE）解决视觉时空编码问题，通过 AR-DF（自回归离散扩散强迫）解决帧间损失不均衡问题，仅用 48 GPU 训练即可在 GenEval、VBench-I2V 和 VBench-T2V 上达到竞争力水平。

**[Mamba-3: Improved Sequence Modeling using State Space Principles](mamba-3_improved_sequence_modeling_using_state_space_principles.md)**

:   从SSM视角提出三项核心改进：指数-梯形离散化、复值状态空间、多输入多输出(MIMO)公式化，在不增加解码延迟的前提下显著提升模型质量和状态追踪能力，推进性能-效率Pareto前沿。

**[Online Time Series Prediction Using Feature Adjustment](online_time_series_prediction_using_feature_adjustment.md)**

:   提出 ADAPT-Z（Automatic Delta Adjustment via Persistent Tracking in Z-space），将在线时序预测的适应目标从模型参数更新转移到特征空间修正，通过轻量 adapter 融合当前特征与历史梯度来应对多步预测中的延迟反馈问题，在13个数据集上一致超越现有在线学习方法。

**[Quantsparse Comprehensively Compressing Video Diffusion Transformer With Model Q](quantsparse_comprehensively_compressing_video_diffusion_transformer_with_model_q.md)**

:   本文提出 QuantSparse 框架，首次将模型量化（quantization）与注意力稀疏化（attention sparsification）协同整合用于视频扩散 Transformer 压缩，通过多尺度显著注意力蒸馏（MSAD）和二阶稀疏注意力重参数化（SSAR）解决两者朴素结合导致的"放大注意力偏移"问题，在 HunyuanVideo-13B 上以 W4A8 + 15% 注意力密度实现 3.68× 存储压缩和 1.88× 推理加速，同时几乎无损保持生成质量。

**[CAPO: Curvature-Aware Policy Optimization for Sample-Efficient RL in LLM Reasoning](stabilizing_policy_gradients_for_sample-efficient_reinforcement_learning_in_llm_.md)**

:   CAPO 通过建模优化景观的二阶几何（仅在 LM head 最后一层计算曲率），实现 token 级别的数据筛选——拒绝会导致策略崩溃的更新，使 LLM 推理 RL 训练在激进超参数下仍保持稳定，样本效率提升 30 倍。

**[Stop Tracking Me! Proactive Defense Against Attribute Inference Attack in LLMs](stop_tracking_me_proactive_defense_against_attribute_inference_attack_in_llms.md)**

:   TRACE-RPS 提出统一防御框架应对 LLM 属性推断攻击：TRACE 通过注意力+推理链精准定位隐私泄露文本元素做细粒度匿名化，RPS 通过轻量后缀优化诱导模型拒绝推断，将属性推断准确率从约 50% 降至 5% 以下。

**[TTOM: Test-Time Optimization and Memorization for Compositional Video Generation](ttom_test-time_optimization_and_memorization_for_compositional_video_generation.md)**

:   提出 TTOM 框架，在推理时通过优化新增参数将视频生成模型的注意力与 LLM 生成的时空布局对齐，并用参数记忆机制保存历史优化上下文支持复用，在 T2V-CompBench 上相对提升 34%（CogVideoX）和 14%（Wan2.1）。

**[Videonsa Native Sparse Attention Scales Video Understanding](videonsa_native_sparse_attention_scales_video_understanding.md)**

:   本文提出 VideoNSA，将 Native Sparse Attention（NSA）引入视频语言模型，通过压缩、选择和滑动窗口三分支动态门控的混合稀疏注意力机制，在仅使用 3.6% 注意力预算的条件下实现 128K token 的视频理解，在长视频理解、时序推理和空间理解任务上全面超越 token 压缩和无训练稀疏注意力基线。

**[WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](weboperator_action-aware_tree_search_for_autonomous_agents_in_web_environment.md)**

:   提出 WebOperator，一个动作感知的树搜索框架，通过投机性回溯、破坏性动作检测、动作验证与合并等机制，使 Web 自主代理能在部分可观测、不可逆的真实网页环境中安全高效地探索，在 WebArena 上以 gpt-4o 达到 54.6% SOTA 成功率。
