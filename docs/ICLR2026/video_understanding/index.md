<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**🔬 ICLR2026** · 共 **36** 篇

**[AdAEM: An Adaptively and Automated Extensible Measurement of LLMs' Value Difference](adaem_an_adaptively_and_automated_extensible_measurement_of_llms_value_differenc.md)**

:   提出 AdAEM，一个自适应、自扩展的 LLM 价值观评估框架，通过信息论优化自动生成能最大化揭示不同 LLM 价值差异的测试问题，解决现有静态基准无法区分模型价值取向的"信息量不足"问题。

**[A.I.R.: Adaptive, Iterative, and Reasoning-based Frame Selection For Video Question Answering](air_enabling_adaptive_iterative_and_reasoning-based_frame_selection_for_video_qu.md)**

:   提出 A.I.R.，一种无需训练的自适应-迭代-推理驱动帧选择框架，通过两阶段策略（GMM 自适应初始采样 + 迭代式 VLM 精细分析）解决 VideoQA 中轻量模型（CLIP）相似度不准确和 VLM 分析成本爆炸的双重困境，在最坏情况下也仅需分析 72 帧（vs 基线 128 帧），同时显著提升多个长视频 benchmark 性能。

**[AnveshanaAI: A Multimodal Platform for Adaptive AI/ML Education through Automated Question Generation and Interactive Assessment](anveshanaai_a_multimodal_platform_for_adaptive_aiml_education_through_automated_.md)**

:   提出 AnveshanaAI，一个基于 Bloom 认知分类学的自适应 AI/ML 教育平台，通过自动化题目生成（基于微调的 GPT-2）、语义相似度检测去重、XAI 可解释性技术和游戏化机制（积分/徽章/排行榜），实现了覆盖数据科学到多模态 AI 七大领域的个性化学习评估系统，实验表明微调后困惑度显著下降且学习者参与度明显提升。

**[Arbitrary Generative Video Interpolation](arbitrary_generative_video_interpolation.md)**

:   ArbInterp 提出了一种支持任意时间戳、任意长度的生成式视频帧插值框架，通过时间戳感知旋转位置编码（TaRoPE）实现精准时间控制，并通过外观-运动解耦的条件注入策略实现长序列的无缝拼接。

**[BindWeave: Subject-Consistent Video Generation via Cross-Modal Integration](bindweave_subject-consistent_video_generation_via_cross-modal_integration.md)**

:   BindWeave 用多模态大语言模型（MLLM）替代传统的浅层融合机制来解析多主体复杂文本指令，生成主体感知的隐状态作为 DiT 的条件信号，结合 CLIP 语义特征和 VAE 细粒度外观特征，实现高保真、主体一致的视频生成。

**[Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss](coupling_experts_and_routers_in_mixture-of-experts_via_an_auxiliary_loss.md)**

:   提出 Expert-Router Coupling (ERC) Loss，一种轻量级辅助损失函数，通过将路由器参数视为聚类中心的代理 token 并约束专家对其激活范数，实现路由器决策与专家能力的紧密耦合，仅需 $n^2$ 次激活计算即可显著提升 MoE-LLM 性能。

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

**[Map the Flow: Revealing Hidden Pathways of Information in VideoLLMs](map_the_flow_revealing_hidden_pathways_of_information_in_videollms.md)**

:   首次系统揭示VideoLLM内部时序推理的信息流动规律：(1)早中层跨帧交互建立时空表示→(2)中层视频-语言整合→(3)中后层答案生成，并证明仅保留42%的注意力边即可维持VideoQA性能。

**[MoSA: Motion-Coherent Human Video Generation via Structure-Appearance Decoupling](mosa_motion-coherent_human_video_generation_via_structure-appearance_decoupling.md)**

:   提出MoSA框架，将人物视频生成解耦为结构生成（3D骨骼Transformer生成运动序列）和外观生成（DiT在骨骼引导下合成视频），配合人体感知动态控制(HADC)模块、密集跟踪损失和接触约束，在复杂全身运动上显著超越现有方法。

**[MotionStream: Real-Time Video Generation with Interactive Motion Controls](motionstream_real-time_video_generation_with_interactive_motion_controls.md)**

:   提出MotionStream实现首个运动控制的实时流式视频生成——将双向运动控制teacher通过Self Forcing+DMD蒸馏为因果student，引入注意力沉降+滑动窗口KV缓存实现无限长度恒速生成，单GPU达29FPS+亚秒延迟，运动跟踪质量达SOTA。

**[NerVE: Nonlinear Eigenspectrum Dynamics in LLM Feed-Forward Networks](nerve_nonlinear_eigenspectrum_dynamics_in_llm_feed-forward_networks.md)**

:   提出 NerVE，一个轻量级的特征谱分析框架，通过四个互补指标（频谱熵、参与比、特征值早期富集、JS 散度）系统揭示了 LLM 中 FFN 非线性如何重新注入方差、重塑特征谱，以及架构和优化器选择如何印刻独特的频谱签名。

**[Online Time Series Prediction Using Feature Adjustment](online_time_series_prediction_using_feature_adjustment.md)**

:   提出 ADAPT-Z（Automatic Delta Adjustment via Persistent Tracking in Z-space），将在线时序预测的适应目标从模型参数更新转移到特征空间修正，通过轻量 adapter 融合当前特征与历史梯度来应对多步预测中的延迟反馈问题，在13个数据集上一致超越现有在线学习方法。

**[Paper Copilot: Tracking the Evolution of Peer Review in AI Conferences](paper_copilot_tracking_the_evolution_of_peer_review_in_ai_conferences.md)**

:   构建Paper Copilot——AI会议同行评审的持久数字档案和分析系统：跨数十个AI/ML会议统一收集评审数据(OpenReview API+网页抓取+社区贡献)，提供评分动态追踪(含rebuttal前后变化的时间戳快照)、机构/国家级人才流动分析，以及ICLR多年评审演化的大规模实证分析，发现2025年评审呈现更尖锐的分数驱动分层趋势。

**[PreciseCache: Precise Feature Caching for Efficient and High-fidelity Video Generation](precisecache_precise_feature_caching_for_efficient_and_high-fidelity_video_gener.md)**

:   提出PreciseCache——精确检测并跳过视频生成中真正冗余计算的即插即用加速框架：LFCache用低频差异(LFD)度量步级冗余(高噪声步结构重要/低噪声步细节可缓存)→BlockCache度量块级冗余(非关键block直接复用)→在Wan2.1-14B上实现2.6x加速且无明显质量损失。

**[QuantSparse: Comprehensively Compressing Video Diffusion Transformer with Model Quantization and Attention Sparsification](quantsparse_comprehensively_compressing_video_diffusion_transformer_with_model_q.md)**

:   本文提出 QuantSparse 框架，首次将模型量化（quantization）与注意力稀疏化（attention sparsification）协同整合用于视频扩散 Transformer 压缩，通过多尺度显著注意力蒸馏（MSAD）和二阶稀疏注意力重参数化（SSAR）解决两者朴素结合导致的"放大注意力偏移"问题，在 HunyuanVideo-13B 上以 W4A8 + 15% 注意力密度实现 3.68× 存储压缩和 1.88× 推理加速，同时几乎无损保持生成质量。

**[Stabilizing Policy Gradients for Sample-Efficient Reinforcement Learning in LLM Reasoning](stabilizing_policy_gradients_for_sample-efficient_reinforcement_learning_in_llm_.md)**

:   提出 CAPO（Curvature-Aware Policy Optimization），通过在 LM head 最后一层建模二阶优化几何来预测并过滤会导致策略崩溃的 token 更新，在激进超参数（5× 学习率、1/12 batch size）下仍保持训练稳定，实现 MATH 上相较标准 GRPO 的 30× 样本效率提升。

**[Stop Tracking Me! Proactive Defense Against Attribute Inference Attack in LLMs](stop_tracking_me_proactive_defense_against_attribute_inference_attack_in_llms.md)**

:   TRACE-RPS 提出统一防御框架应对 LLM 属性推断攻击：TRACE 通过注意力+推理链精准定位隐私泄露文本元素做细粒度匿名化，RPS 通过轻量后缀优化诱导模型拒绝推断，将属性推断准确率从约 50% 降至 5% 以下。

**[The Expressive Limits of Diagonal SSMs for State-Tracking](the_expressive_limits_of_diagonal_ssms_for_state-tracking.md)**

:   研究输入依赖复数对角(DCD) SSM的表达能力极限——证明单层DCD SSM不能在有限精度下追踪任何非阿贝尔群的状态,更一般地k层DCD SSM能追踪一个群当且仅当该群有长度为k的子正规链且因子为阿贝尔群→精确刻画了k层DCD SSM在可解群中的表达范围,实验揭示多层模型在非阿贝尔群上表达能力和可学习性之间的gap。

**[FuncBenchGen: 面向可靠基准测试的无污染可控评估框架](towards_reliable_benchmarking_a_contamination_free_controllable_evaluation_frame.md)**

:   提出 FuncBenchGen 框架，通过将多步函数调用建模为 DAG 图遍历问题，实现无数据污染、可精细控制任务难度的 LLM 工具使用能力评估，并揭示了推理模型在长调用链和连接型干扰函数下的关键失败模式。

**[TTOM: Test-Time Optimization and Memorization for Compositional Video Generation](ttom_test-time_optimization_and_memorization_for_compositional_video_generation.md)**

:   提出 TTOM 框架，在推理时通过优化新增参数将视频生成模型的注意力与 LLM 生成的时空布局对齐，并用参数记忆机制保存历史优化上下文支持复用，在 T2V-CompBench 上相对提升 34%（CogVideoX）和 14%（Wan2.1）。

**[Video-KTR: 通过关键 Token 归因增强视频推理](video-ktr_reinforcing_video_reasoning_via_key_token_attribution.md)**

:   提出 Video-KTR，一种模态感知的策略塑造框架，通过反事实分析识别视觉感知型、时序敏感型和高熵 Token 三类关键 Token，仅对这些 Token 执行选择性强化学习更新，在多个视频推理基准上达到 SOTA（Video-Holmes 42.7%，超越 GPT-4o）。

**[VideoNSA: Native Sparse Attention Scales Video Understanding](videonsa_native_sparse_attention_scales_video_understanding.md)**

:   本文提出 VideoNSA，将 Native Sparse Attention（NSA）引入视频语言模型，通过压缩、选择和滑动窗口三分支动态门控的混合稀疏注意力机制，在仅使用 3.6% 注意力预算的条件下实现 128K token 的视频理解，在长视频理解、时序推理和空间理解任务上全面超越 token 压缩和无训练稀疏注意力基线。

**[联邦学习中水印的鲁棒性与放射性可能相互矛盾](watermark_robustness_and_radioactivity_may_be_at_odds_in_federated_learning.md)**

:   首次研究联邦学习中 LLM 水印的数据溯源问题，发现水印在 FL 中具有放射性（可检测），但恶意服务器可通过强鲁棒聚合算法过滤水印更新，揭示了放射性、鲁棒性和模型效用之间的根本性三元矛盾。

**[WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](weboperator_action-aware_tree_search_for_autonomous_agents_in_web_environment.md)**

:   提出 WebOperator，一个动作感知的树搜索框架，通过投机性回溯、破坏性动作检测、动作验证与合并等机制，使 Web 自主代理能在部分可观测、不可逆的真实网页环境中安全高效地探索，在 WebArena 上以 gpt-4o 达到 54.6% SOTA 成功率。
