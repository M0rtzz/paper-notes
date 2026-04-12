---
title: >-
  ICLR2026 信息检索/RAG方向 30篇论文解读
description: >-
  30篇ICLR2026 信息检索/RAG方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔍 信息检索/RAG

**🔬 ICLR2026** · 共 **30** 篇

**[Attributing Response To Context A Jensen-Shannon Divergence Driven Mechanistic S](attributing_response_to_context_a_jensen-shannon_divergence_driven_mechanistic_s.md)**

:   提出ARC-JSD方法，通过计算完整上下文与逐句消融上下文下的响应分布的Jensen-Shannon散度，在无需微调、梯度计算或代理模型的情况下实现高效精准的RAG上下文归因，并结合Logit Lens进行机制分析，定位负责上下文归因的注意力头和MLP层，通过门控操作降低约39%的幻觉率。

**[Bayesian Attention Mechanism A Probabilistic Framework For Positional Encoding A](bayesian_attention_mechanism_a_probabilistic_framework_for_positional_encoding_a.md)**

:   将位置编码重新表述为贝叶斯注意力机制中的先验分布，统一了 NoPE（均匀先验）和 ALiBi（拉普拉斯先验），并提出广义高斯先验（GGD-BAM），仅增加 384 个参数即可在 500 倍训练长度上实现完美的 passkey 检索。

**[Beyond Rag Vs Long-Context Learning Distraction-Aware Retrieval For Efficient Kn](beyond_rag_vs_long-context_learning_distraction-aware_retrieval_for_efficient_kn.md)**

:   提出 LDAR（Learning Distraction-Aware Retrieval），一个轻量级自适应检索器，通过学习基于查询-段落相似度分布选择段落的连续区间（band），在平衡信息覆盖与干扰段落影响的同时，以约一半的 token 用量超越长上下文方法的性能。

**[Btzsc A Benchmark For Zero-Shot Text Classification Across Cross-Encoders Embedd](btzsc_a_benchmark_for_zero-shot_text_classification_across_cross-encoders_embedd.md)**

:   提出 BTZSC 基准（22 个数据集），首次在统一零样本协议下系统比较 NLI 交叉编码器、嵌入模型、Reranker 和指令微调 LLM 四大模型家族（共 38 个模型），发现 Qwen3-Reranker-8B 以 macro F1=0.72 取得新 SOTA，嵌入模型在精度-延迟权衡上最优。

**[Digging Deeper Learning Multi-Level Concept Hierarchies](digging_deeper_learning_multi-level_concept_hierarchies.md)**

:   本文提出Multi-Level Concept Splitting（MLCS）从仅有的顶层概念监督中自动发现多层次概念层级，结合Deep-HiCEMs架构表示这些层级结构，使模型在保持高精度的同时支持多个抽象层次的测试时概念干预。

**[Efficient Discriminative Joint Encoders For Large Scale Vision-Language Rerankin](efficient_discriminative_joint_encoders_for_large_scale_vision-language_rerankin.md)**

:   提出EDJE（高效判别式联合编码器），通过将视觉特征提取离线化并用轻量级注意力适配器压缩视觉Token，实现50k图文对/秒的高吞吐推理，同时在Flickr（零样本）和COCO（微调）检索上匹配现有联合编码器的性能，每张图仅需49kB存储。

**[Embedding-Based Context-Aware Reranker](embedding-based_context-aware_reranker.md)**

:   提出 EBCAR，一个基于嵌入空间的轻量级重排序框架，通过文档 ID 嵌入和段落位置编码引入结构信息，结合共享全注意力 + 专用掩码注意力的混合机制实现跨段落推理，在 ConTEB 基准上以 126M 参数达到最优平均 nDCG@10，推理速度比 LLM 重排器快 150 倍以上。

**[Fine-Tuning With Rag For Improving Llm Learning Of New Skills](fine-tuning_with_rag_for_improving_llm_learning_of_new_skills.md)**

:   提出将 RAG 从推理时的永久依赖转化为训练时的教师信号：从 agent 失败中提取 hint、用 hint 增强的教师生成更优轨迹、然后移除 hint 蒸馏到学生模型，使学生内化检索增益而无需运行时 RAG，在 ALFWorld 达到 91% 成功率（基线 79%），WebShop 分数达 72（基线 61）。

**[Flow Of Spans Generalizing Language Models To Dynamic Span-Vocabulary Via Gflown](flow_of_spans_generalizing_language_models_to_dynamic_span-vocabulary_via_gflown.md)**

:   提出 FoSS，首次将 GFlowNets 引入 span 级别语言模型，通过构建 DAG 结构的状态空间代替传统 token-by-token 的树形结构，实现更灵活多样的文本生成，MAUVE 分数最高提升 12.5%。

**[Futuremind Equipping Small Language Models With Strategic Thinking-Pattern Prior](futuremind_equipping_small_language_models_with_strategic_thinking-pattern_prior.md)**

:   提出FutureMind无训练框架，将LLM的结构化推理和检索策略蒸馏为可复用的思维模式先验，通过四阶段pipeline（问题分析→逻辑推理→策略规划→检索指导）和三种检索范式，使SLM在多跳QA上达到SOTA。

**[G-Reasoner Foundation Models For Unified Reasoning Over Graph-Structured Knowled](g-reasoner_foundation_models_for_unified_reasoning_over_graph-structured_knowled.md)**

:   提出 G-reasoner，通过 QuadGraph 四层统一图接口将异构知识源标准化，训练 34M 参数的 GNN 图基础模型联合推理图拓扑和文本语义，配合 LLM 在 6 个基准上全面超越 SOTA GraphRAG 方法。

**[Hierarchical Concept-Based Interpretable Models](hierarchical_concept-based_interpretable_models.md)**

:   HiCEMs引入层级概念嵌入模型，通过Concept Splitting方法在预训练CEM的嵌入空间中自动发现细粒度子概念（无需额外标注），构建层级概念结构，使模型能在不同粒度层次进行测试时概念干预以提升任务性能。

**[Hume Measuring The Human-Model Performance Gap In Text Embedding Tasks](hume_measuring_the_human-model_performance_gap_in_text_embedding_tasks.md)**

:   提出 HUME 框架，首次系统测量人类在文本嵌入任务（重排序、分类、聚类、语义相似度）上的表现，为 MTEB 建立人类性能基线，发现人类总体排名第 4（77.6 vs 模型最佳 80.1），并揭示了多个数据集的质量问题。

**[Hybrid Deep Searcher Scalable Parallel And Sequential Search Reasoning](hybrid_deep_searcher_scalable_parallel_and_sequential_search_reasoning.md)**

:   提出 HybridDeepSearcher，通过构建 HDS-QA 数据集训练大语言推理模型（LRM）区分可并行化和顺序依赖的搜索查询，在 FanOutQA 上 F1 提升 +15.9、BrowseComp 子集上提升 +11.5，同时显著降低推理延迟并展示出一致的测试时搜索扩展能力。

**[Judges Verdict A Comprehensive Analysis Of Llm Judge Capability Through Human Ag](judges_verdict_a_comprehensive_analysis_of_llm_judge_capability_through_human_ag.md)**

:   提出 Judge's Verdict Benchmark——两步评估框架，通过相关性过滤 + Cohen's Kappa 人类相似性测试，从 54 个 LLM 中识别 27 个 Tier 1 评委（23 人类相似型 + 4 超一致型），揭示相关性不足以评估 LLM 评委质量。

**[Leveraging Data To Say No Memory Augmented Plug-And-Play Selective Prediction](leveraging_data_to_say_no_memory_augmented_plug-and-play_selective_prediction.md)**

:   提出 MA-PaPSP 框架，通过外部检索数据集构建代理嵌入（k-NN 加权平均降低表示方差）+ 对比归一化评分（改善校准），无训练地为任意 VLM 提供可靠的"拒绝回答"能力，在图像描述、图文匹配、分类的选择性预测上全面优于 PaPSP 和 LLM-as-judge 基线。

**[Lightretriever A Llm-Based Text Retrieval Architecture With Extremely Faster Que](lightretriever_a_llm-based_text_retrieval_architecture_with_extremely_faster_que.md)**

:   提出 LightRetriever，一种极端不对称的LLM检索架构：文档端保留完整LLM编码器，查询端完全去除深度建模——稠密检索仅需嵌入查表+平均，稀疏检索仅需token计数——实现查询编码1000倍加速、端到端10倍吞吐提升，同时保持95%的检索性能。

**[Mapping Semantic Syntactic Relationships With Geometric Rotation](mapping_semantic_syntactic_relationships_with_geometric_rotation.md)**

:   提出RISE(Rotor-Invariant Shift Estimation)——将话语级语义-句法变换(否定/条件/礼貌)建模为嵌入空间超球面上的一致旋转操作，首次证明这些变换可跨7种语言(5个语系)+跨3种嵌入模型泛化，将线性表示假说从词级扩展到跨语言话语级。

**[Multimodal Dataset Distillation Made Simple By Prototype-Guided Data Synthesis](multimodal_dataset_distillation_made_simple_by_prototype-guided_data_synthesis.md)**

:   提出PDS (Prototype-Guided Data Synthesis)，首个免训练的多模态数据集蒸馏方法——用CLIP提取对齐的图文嵌入→聚类→线性分配匹配跨模态原型→unCLIP解码器从图像原型合成图像，在极小蒸馏集上以零训练代价达到SOTA的跨架构泛化。

**[On The Wings Of Imagination Conflicting Script-Based Multi-Role Framework For Hu](on_the_wings_of_imagination_conflicting_script-based_multi-role_framework_for_hu.md)**

:   提出 HOMER 框架，基于 GTVH 幽默理论构建三角色 LLM 协作机制（冲突脚本提取器 + 层次想象器 + 标题生成器），通过显式建模脚本对立、多视角联想链与笑话数据库检索构建想象树来扩展创意空间，在 New Yorker 漫画基准上以 GPT-4o 为底座平均提升 ~7%，人类评估也显著优于所有基线。

**[Query-Level Uncertainty In Large Language Models](query-level_uncertainty_in_large_language_models.md)**

:   提出Query-Level Uncertainty概念，通过Internal Confidence方法在生成前（单次前向传播）估计LLM能否回答给定查询，无需训练即可实现高效的自适应推理（RAG触发/模型级联/弃权）。

**[Raee A Robust Retrieval-Augmented Early Exit Framework For Efficient Inference](raee_a_robust_retrieval-augmented_early_exit_framework_for_efficient_inference.md)**

:   提出 RAEE，一种无需训练分类器的检索增强早退框架，通过检索语义相似样本的退出信息来动态确定最优退出层，不仅加速推理还能纠正模型错误预测，实现加速与性能提升的双赢。

**[Ravenea A Benchmark For Multimodal Retrieval-Augmented Visual Culture Understand](ravenea_a_benchmark_for_multimodal_retrieval-augmented_visual_culture_understand.md)**

:   构建首个评估多模态检索增强文化理解的基准 Ravenea，包含 1868 个实例和 11396 篇人工排序的 Wikipedia 文档，覆盖 8 个国家 11 个类别，评估 7 个多模态检索器和 17 个 VLM，发现文化感知的 RAG 可在 cVQA 上平均提升 6%、cIC 上提升 11%。

**[Reftool Reference-Guided Tool Creation For Knowledge-Intensive Reasoning](reftool_reference-guided_tool_creation_for_knowledge-intensive_reasoning.md)**

:   提出 RefTool 框架基于外部参考资料（教材、知识片段）自动创建可执行 Python 工具，解决了现有工具创建方法依赖 LLM 内在知识在专业领域失败的问题，在因果推理、物理和化学任务上平均超过已有方法 12.3%。

**[Retrieval-Augmented Generation For Predicting Cellular Responses To Gene Perturb](retrieval-augmented_generation_for_predicting_cellular_responses_to_gene_perturb.md)**

:   提出 **PT-RAG**（Perturbation-aware Two-stage Retrieval-Augmented Generation），首次将可微检索增强生成范式应用于单细胞基因扰动响应预测：通过 GenePT 语义检索候选扰动 + Gumbel-Softmax 条件离散采样实现细胞类型感知的端到端检索优化，在 Replogle-Nadig 数据集上超越 STATE 基线（Pearson 0.633 vs 0.624），同时发现朴素 RAG 会严重损害性能（Pearson 仅 0.396），证明**可微且细胞类型感知的检索**在该领域不可或缺。

**[Revela Dense Retriever Learning Via Language Modeling](revela_dense_retriever_learning_via_language_modeling.md)**

:   提出 Revela，通过 in-batch attention 机制将检索器学习融入语言建模——NTP 不仅依赖本序列上下文，还依赖批内其他序列（由检索器相似度加权），无需标注 query-document 对即可训练强大的密集检索器。

**[Summaries As Centroids For Interpretable And Scalable Text Clustering](summaries_as_centroids_for_interpretable_and_scalable_text_clustering.md)**

:   提出 k-NLPmeans 和 k-LLMmeans，通过在 k-means 迭代中周期性地用文本摘要替换数值质心（summary-as-centroid），在保持 k-means 标准目标的同时实现可解释的聚类原型，且 LLM 调用量与数据集大小无关。

**[Token-Guard Towards Token-Level Hallucination Control Via Self-Checking Decoding](token-guard_towards_token-level_hallucination_control_via_self-checking_decoding.md)**

:   提出 Token-Guard，一种基于自检验解码的 token 级幻觉控制方法，通过隐空间中的 token 级/段级评分和迭代修正机制，在解码过程中检测并抑制幻觉生成，F1 平均提升 16.3%。

**[Tokmem One-Token Procedural Memory For Large Language Models](tokmem_one-token_procedural_memory_for_large_language_models.md)**

:   提出 TokMem，将可复用的任务程序编译为单个可训练记忆 token，既作为程序索引又作为生成控制信号，无需长 prompt 即可高效调用 1000+ 任务程序，且支持无遗忘的持续扩展。

**[Your Language Model Secretly Contains Personality Subnetworks](your_language_model_secretly_contains_personality_subnetworks.md)**

:   本文提出通过激活引导的剪枝（activation-guided pruning）从预训练 LLM 中提取人格专用子网络，无需任何训练即可实现高效的人格切换，并引入对比剪枝策略增强对立人格间的参数分离。
