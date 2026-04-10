<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎁 推荐系统

**🤖 AAAI2026** · 共 **13** 篇

**[Align³GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation](align3gr_unified_multi-level_alignment_for_llm-based_generat.md)**

:   提出统一三层对齐框架 Align³GR，在 token 级（双端 SCID）、行为建模级（多任务 SFT）和偏好级（渐进式 DPO）系统性弥合 LLM 与推荐系统之间的语义-行为鸿沟。

**[AutoPP: Towards Automated Product Poster Generation and Optimization](autopp_towards_automated_product_poster_generation_and_optimization.md)**

:   提出 AutoPP，首个将商品海报自动生成与基于 CTR 反馈的自动优化统一到一个框架中的流水线，通过 unified design module 联合设计背景/文字/排版，element rendering module 高效可控地生成海报，并利用 Isolated DPO (IDPO) 实现元素级别的点击率优化。

**[Bid Farewell to Seesaw: Towards Accurate Long-tail Session-based Recommendation via Dual Constraints of Hybrid Intents](bid_farewell_to_seesaw_towards_accurate_long-tail_session-based_recommendation_v.md)**

:   提出HID框架，通过属性感知的谱聚类构建混合意图来区分会话相关与无关的尾部物品，并设计针对长尾和准确性的双约束损失（ICLoss），实现长尾推荐与准确性的"双赢"，打破传统方法中两者此消彼长的"跷跷板"困境。

**[CroPS: Improving Dense Retrieval with Cross-Perspective Positive Samples in Short-Video Search](crops_improving_dense_retrieval_with_cross-perspective_positive_samples_in_short.md)**

:   提出 CroPS 数据引擎，通过 query 改写行为、推荐系统交互、LLM 世界知识三个视角扩充正样本集合，配合分层标签分配（HLA）和 H-InfoNCE 损失函数，打破工业级稠密检索系统中的信息茧房效应，已在快手搜索全量部署。

**[Evaluating LLMs for Police Decision-Making: A Framework Based on Police Action Scenarios](evaluating_llms_for_police_decision-making_a_framework_based_on_police_action_sc.md)**

:   提出 PAS（Police Action Scenarios）评估框架，一个面向警务场景的 LLM 评估体系，涵盖场景定义、参考答案构建、LLM 响应生成、核心指标提取和性能解读五个阶段，基于 8000+ 韩国警察官方文件构建评估数据集，发现商用 LLM（GPT-4、Gemini、Claude）在警务任务上显著低于参考答案，尤其在事实性和逻辑正确性方面。

**[FreqRec: Exploiting Inter-Session Information with Frequency-enhanced Dual-Path Networks for Sequential Recommendation](exploiting_inter-session_information_with_frequency-enhanced_dual-path_networks_.md)**

:   提出FreqRec双路径架构，通过batch维和时间维两条频域路径分别捕获跨session群体节律和用户个体细粒度兴趣，并引入频域一致性损失显式对齐预测与真实频谱，在三个Amazon数据集上NDCG@10最高提升7.38%。

**[From Parameter to Representation: A Closed-Form Approach for Controllable Model Merging](from_parameter_to_representation_a_closed-form_approach_for_controllable_model_m.md)**

:   提出 ReACT，将可控模型合并从参数空间优化转移到表征空间校正，通过闭式解实现任意用户偏好下的 Pareto 最优模型即时生成，比现有方法快 36-208 倍且性能更优。

**[Generalization Bounds for Semi-supervised Matrix Completion with Distributional Side Information](generalization_bounds_for_semi-supervised_matrix_completion_with_distributional_.md)**

:   提出半监督矩阵补全的理论框架：假设采样分布 $P$ 与真实矩阵 $G$ 共享低秩子空间，利用大量无标签隐式反馈估计子空间、少量有标签显式反馈恢复矩阵，证明泛化误差可分解为两个独立项 $\widetilde{O}(\sqrt{(m+n)r/M} + \sqrt{dr/N})$。

**[Inference-Aware Prompt Optimization for Aligning Black-Box Large Language Models](inference-aware_prompt_optimization_for_aligning_black-box_large_language_models.md)**

:   揭示 prompt 选择与推理策略（Best-of-N、Majority Voting）之间存在非平凡交互关系，提出 IAPO 框架将 prompt 设计与推理规模联合优化为上下文最优臂识别问题，并设计 PSST 固定预算训练算法，在 6 个任务上相比推理无关方法提升最高 50%。

**[Probabilistic Hash Embeddings for Online Learning of Categorical Features](probabilistic_hash_embeddings_for_online_learning_of_categorical_features.md)**

:   提出 Probabilistic Hash Embeddings (PHE)，将 hash embedding 视为随机变量并通过 Bayesian online learning 进行后验推断，解决流式数据中类别特征词汇不断增长时确定性 hash embedding 遭受的灾难性遗忘问题。

**[SlideTailor: Personalized Presentation Slide Generation for Scientific Papers](slidetailor_personalized_presentation_slide_generation_for_scientific_papers.md)**

:   提出 SlideTailor，一个受人类行为启发的 agentic 框架，通过从用户提供的论文-幻灯片示例对和 .pptx 模板中蒸馏隐式偏好，渐进式生成个性化、可编辑的学术论文幻灯片，并引入 chain-of-speech 机制提升内容与口头叙述的对齐。

**[Tokenize Once, Recommend Anywhere: Unified Item Tokenization for Multi-domain LLM-based Recommendation](tokenize_once_recommend_anywhere_unified_item_tokenization_for_multi-domain_llm-.md)**

:   提出 UniTok，一个统一的商品 tokenization 框架，通过定制的 Mixture-of-Experts（TokenMoE）架构结合共享码本，实现跨多个领域的高效商品离散化表示，避免为每个领域单独训练 tokenizer，同时通过互信息校准机制保持跨域语义平衡。

**[Wavelet Enhanced Adaptive Frequency Filter for Sequential Recommendation](wavelet_enhanced_adaptive_frequency_filter_for_sequential_re.md)**

:   提出WEARec模型结合动态频域滤波(DFF)和小波特征增强(WFE)两个模块，分别捕获个性化全局频域信息和增强非平稳短期波动，在四个公开数据集上超越频域推荐SOTA基线，长序列场景提升可达11.4%。
