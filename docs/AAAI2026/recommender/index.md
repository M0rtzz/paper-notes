---
title: >-
  AAAI2026 推荐系统方向 21篇论文解读
description: >-
  21篇AAAI2026 推荐系统方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎁 推荐系统

**🤖 AAAI2026** · 共 **21** 篇

**[Align3Gr Unified Multi-Level Alignment For Llm-Based Generat](align3gr_unified_multi-level_alignment_for_llm-based_generat.md)**

:   提出统一三层对齐框架 Align³GR，在 token 级（双端 SCID）、行为建模级（多任务 SFT）和偏好级（渐进式 DPO）系统性弥合 LLM 与推荐系统之间的语义-行为鸿沟。

**[Autopp Towards Automated Product Poster Generation And Optimization](autopp_towards_automated_product_poster_generation_and_optimization.md)**

:   提出 AutoPP，首个将商品海报自动生成与基于 CTR 反馈的自动优化统一到一个框架中的流水线，通过 unified design module 联合设计背景/文字/排版，element rendering module 高效可控地生成海报，并利用 Isolated DPO (IDPO) 实现元素级别的点击率优化。

**[Bid Farewell To Seesaw Towards Accurate Long-Tail Session-Based Recommendation V](bid_farewell_to_seesaw_towards_accurate_long-tail_session-based_recommendation_v.md)**

:   提出HID框架，通过属性感知的谱聚类构建混合意图来区分会话相关与无关的尾部物品，并设计针对长尾和准确性的双约束损失（ICLoss），实现长尾推荐与准确性的"双赢"，打破传统方法中两者此消彼长的"跷跷板"困境。

**[Crops Improving Dense Retrieval With Cross-Perspective Positive Samples In Short](crops_improving_dense_retrieval_with_cross-perspective_positive_samples_in_short.md)**

:   提出 CroPS 数据引擎，通过 query 改写行为、推荐系统交互、LLM 世界知识三个视角扩充正样本集合，配合分层标签分配（HLA）和 H-InfoNCE 损失函数，打破工业级稠密检索系统中的信息茧房效应，已在快手搜索全量部署。

**[Evaluating Llms For Police Decision-Making A Framework Based On Police Action Sc](evaluating_llms_for_police_decision-making_a_framework_based_on_police_action_sc.md)**

:   提出 PAS（Police Action Scenarios）评估框架，一个面向警务场景的 LLM 评估体系，涵盖场景定义、参考答案构建、LLM 响应生成、核心指标提取和性能解读五个阶段，基于 8000+ 韩国警察官方文件构建评估数据集，发现商用 LLM（GPT-4、Gemini、Claude）在警务任务上显著低于参考答案，尤其在事实性和逻辑正确性方面。

**[Exploiting Inter-Session Information With Frequency-Enhanced Dual-Path Networks ](exploiting_inter-session_information_with_frequency-enhanced_dual-path_networks_.md)**

:   提出FreqRec双路径架构，通过batch维和时间维两条频域路径分别捕获跨session群体节律和用户个体细粒度兴趣，并引入频域一致性损失显式对齐预测与真实频谱，在三个Amazon数据集上NDCG@10最高提升7.38%。

**[From Parameter To Representation A Closed-Form Approach For Controllable Model M](from_parameter_to_representation_a_closed-form_approach_for_controllable_model_m.md)**

:   提出 ReACT，将可控模型合并从参数空间优化转移到表征空间校正，通过闭式解实现任意用户偏好下的 Pareto 最优模型即时生成，比现有方法快 36-208 倍且性能更优。

**[Generalization Bounds For Semi-Supervised Matrix Completion With Distributional ](generalization_bounds_for_semi-supervised_matrix_completion_with_distributional_.md)**

:   提出半监督矩阵补全的理论框架：假设采样分布 $P$ 与真实矩阵 $G$ 共享低秩子空间，利用大量无标签隐式反馈估计子空间、少量有标签显式反馈恢复矩阵，证明泛化误差可分解为两个独立项 $\widetilde{O}(\sqrt{(m+n)r/M} + \sqrt{dr/N})$。

**[Inference-Aware Prompt Optimization For Aligning Black-Box Large Language Models](inference-aware_prompt_optimization_for_aligning_black-box_large_language_models.md)**

:   揭示 prompt 选择与推理策略（Best-of-N、Majority Voting）之间存在非平凡交互关系，提出 IAPO 框架将 prompt 设计与推理规模联合优化为上下文最优臂识别问题，并设计 PSST 固定预算训练算法，在 6 个任务上相比推理无关方法提升最高 50%。

**[Interpretable Reward Model Via Sparse Autoencoder](interpretable_reward_model_via_sparse_autoencoder.md)**

:   提出 SARM（Sparse Autoencoder-enhanced Reward Model），将预训练的稀疏自编码器集成到奖励模型中，将隐层激活映射到可解释的稀疏单义特征空间，实现特征级的奖励归因和动态偏好操控，同时在 RewardBench 2 上取得了所有模型中的最高分。

**[Length-Adaptive Interest Network For Balancing Long And Short Sequence Modeling ](length-adaptive_interest_network_for_balancing_long_and_short_sequence_modeling_.md)**

:   提出LAIN框架，通过将序列长度作为显式条件信号注入CTR模型，缓解长序列用户与短序列用户之间的性能不均衡问题，包含谱长度编码器、长度条件提示和长度调制注意力三个轻量级即插即用模块。

**[Moral Change Or Noise On Problems Of Aligning Ai With Temporally Unstable Human ](moral_change_or_noise_on_problems_of_aligning_ai_with_temporally_unstable_human_.md)**

:   通过在肾脏移植分配领域对400+参与者进行3-5轮纵向研究，揭示了人类道德偏好在时间上的显著不稳定性（6-20%的响应变化率），并证明这种不稳定性会严重降低AI对齐模型的预测性能，从而质疑了当前基于静态偏好假设的对齐方法的有效性。

**[Multitab A Scalable Foundation For Multitask Learning On Tabular Data](multitab_a_scalable_foundation_for_multitask_learning_on_tabular_data.md)**

:   提出MultiTab-Net——首个面向表格数据的多任务Transformer架构，通过多任务掩码注意力机制缓解任务竞争，在推荐、人口普查、物理等多个领域的数据集上显著超越现有MLP-based多任务模型和单任务Transformer模型。

**[Preference Is More Than Comparisons Rethinking Dueling Bandits With Augmented Hu](preference_is_more_than_comparisons_rethinking_dueling_bandits_with_augmented_hu.md)**

:   提出一种基于增强人类反馈的无模型Dueling Bandit框架IPEA-HF，通过增强置信界（Augmented Confidence Bounds）集成上下文相似性和依赖关系来校准不确定性，在推荐、多目标优化和LLM响应优化等多个基准上表现优异。

**[Probabilistic Hash Embeddings For Online Learning Of Categorical Features](probabilistic_hash_embeddings_for_online_learning_of_categorical_features.md)**

:   提出 Probabilistic Hash Embeddings (PHE)，将 hash embedding 视为随机变量并通过 Bayesian online learning 进行后验推断，解决流式数据中类别特征词汇不断增长时确定性 hash embedding 遭受的灾难性遗忘问题。

**[Semi-Supervised Synthetic Data Generation With Fine-Grained Relevance Control Fo](semi-supervised_synthetic_data_generation_with_fine-grained_relevance_control_fo.md)**

:   提出SSRA（半监督相关性感知合成数据管道），通过两阶段流程生成具有可控细粒度相关性标签（4级）的领域自适应短视频数据，增强embedding模型的语义相关性建模能力，在抖音双列场景线上A/B测试中CTR提升1.45%。

**[Slidetailor Personalized Presentation Slide Generation For Scientific Papers](slidetailor_personalized_presentation_slide_generation_for_scientific_papers.md)**

:   提出 SlideTailor，一个受人类行为启发的 agentic 框架，通过从用户提供的论文-幻灯片示例对和 .pptx 模板中蒸馏隐式偏好，渐进式生成个性化、可编辑的学术论文幻灯片，并引入 chain-of-speech 机制提升内容与口头叙述的对齐。

**[Tokenize Once Recommend Anywhere Unified Item Tokenization For Multi-Domain Llm-](tokenize_once_recommend_anywhere_unified_item_tokenization_for_multi-domain_llm-.md)**

:   提出 UniTok，一个统一的商品 tokenization 框架，通过定制的 Mixture-of-Experts（TokenMoE）架构结合共享码本，实现跨多个领域的高效商品离散化表示，避免为每个领域单独训练 tokenizer，同时通过互信息校准机制保持跨域语义平衡。

**[Travellama A Multimodal Travel Assistant With Large-Scale Dataset And Structured](travellama_a_multimodal_travel_assistant_with_large-scale_dataset_and_structured.md)**

:   提出 TraveLLaMA，一个面向旅行辅助的多模态语言模型系统，通过构建 265K QA 对的 TravelQA 数据集和 Travel-CoT 结构化推理框架，在旅行相关问答上实现了 10.8% 的准确率提升，并在 500 人用户研究中获得了 82.5 的 SUS 可用性评分。

**[Wavelet Enhanced Adaptive Frequency Filter For Sequential Re](wavelet_enhanced_adaptive_frequency_filter_for_sequential_re.md)**

:   提出WEARec模型结合动态频域滤波(DFF)和小波特征增强(WFE)两个模块，分别捕获个性化全局频域信息和增强非平稳短期波动，在四个公开数据集上超越频域推荐SOTA基线，长序列场景提升可达11.4%。

**[When Top-Ranked Recommendations Fail Modeling Multi-Granular Negative Feedback F](when_top-ranked_recommendations_fail_modeling_multi-granular_negative_feedback_f.md)**

:   提出 ENF（Explainable Negative Feedback）框架，通过三个协作式 MLLM Agent（Profile Agent、Video Agent、Reason Agent）和渐进式 S-GRPO 强化学习训练策略，首次实现了对视频推荐系统中隐式负反馈的可解释预测和原因分析，在腾讯新闻业务平台上实现了平均观看时长提升 6.2% 和快速跳过率下降 9.4%。
