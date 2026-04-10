<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📐 优化/理论

**🤖 AAAI2026** · 共 **17** 篇

**[A Distributed Asynchronous Generalized Momentum Algorithm Without Delay Bounds](a_distributed_asynchronous_generalized_momentum_algorithm_wi.md)**

:   提出一种完全异步（totally asynchronous）的广义动量（Generalized Momentum）分布式优化算法，无需假设通信/计算延迟的上界即可保证线性收敛，在 Fashion-MNIST 分类任务上比梯度下降快 71%、比 Heavy Ball 快 41%、比 Nesterov 加速梯度法快 19%。

**[A Unified Convergence Analysis for Semi-Decentralized Learning: Sampled-to-Sampled vs. Sampled-to-All Communication](a_unified_convergence_analysis_for_semi-decentralized_learni.md)**

:   本文在统一的收敛分析框架下，首次系统比较了半去中心化联邦学习中两种服务器-设备通信原语（S2S仅返回被采样设备 vs. S2A广播给所有设备），揭示了S2S在高组间异质性下更优、S2A在低异质性下更优的不同regime，并给出了实用的系统配置指南。

**[BeeRNA: Tertiary Structure-Based RNA Inverse Folding Using Artificial Bee Colony](beerna_tertiary_structure-based_rna_inverse_folding_using_artificial_bee_colony.md)**

:   提出 BeeRNA，将人工蜂群（ABC）优化算法应用于 RNA 三级结构逆折叠问题，通过碱基对距离预筛选 + RMSD 两阶段适应度评估，在短/中长度 RNA（<100 nt）上超越深度学习方法 gRNAde 和 RiboDiffusion。

**[Beyond the Mean: Fisher-Orthogonal Projection for Natural Gradient Descent in Large Batch Training](beyond_the_mean_fisher-orthogonal_projection_for_natural_gradient_descent_in_lar.md)**

:   提出 Fisher-Orthogonal Projection (FOP)，通过在 Fisher 度量下对子批次梯度差做正交投影来补充方差信息，使二阶优化器 KFAC 在超大 batch 训练中保持有效，实现最高 ×7.5 的加速。

**[Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation](bridging_synthetic_and_real_routing_problems_via_llm-guided_instance_generation_.md)**

:   提出 EvoReal 框架，利用 LLM 驱动的进化搜索生成结构上接近真实世界的 VRP 合成实例，再通过两阶段渐进微调策略将预训练神经求解器适配到真实基准，在 TSPLib (1.05% gap) 和 CVRPLib (2.71% gap) 上大幅超越已有神经求解器。

**[Co-Layout: LLM-driven Co-optimization for Interior Layout](co-layout_llm-driven_co-optimization_for_interior_layout.md)**

:   提出 Co-Layout 框架，利用 LLM 从自然语言需求中提取结构化约束，再通过基于网格的整数规划（IP）联合优化房间布局与家具摆放，辅以粗到精求解策略提升效率，显著优于现有两阶段方案。

**[Convex Clustering Redefined: Robust Learning with the Median of Means Estimator](convex_clustering_redefined_robust_learning_with_higher_order_norms_and_beyond.md)**

:   本文将 Median of Means (MoM) 估计器融入凸聚类框架，提出 COMET 算法，通过随机分箱与中位数聚合实现对噪声和离群点的鲁棒性，同时无需预知簇数 $k$，理论上证明了弱一致性，实验在多个真实数据集上显著超越 k-means、MoM k-means、凸聚类等六种基线方法。

**[Convex Clustering Redefined: Robust Learning with the Median of Means Estimator](convex_clustering_redefined_robust_learning_with_the_median_of_means_estimator.md)**

:   提出 COMET（Convex Clustering with Median of Means Estimator），将中位数均值（MoM）估计器整合到凸聚类框架中，通过随机分箱、截断距离和 ADAM 优化实现对噪声和异常值的鲁棒聚类，无需预设聚类数量，在理论上证明了弱一致性，在合成和真实数据集上全面超越现有方法。

**[Data Heterogeneity and Forgotten Labels in Split Federated Learning](data_heterogeneity_and_forgotten_labels_in_split_federated_learning.md)**

:   系统研究了 Split Federated Learning 中数据异构导致的灾难性遗忘现象（尤其是 server 端处理顺序造成的 intra-round 遗忘），并提出基于 multi-head 的 Hydra 方法，将 part-2 的最后层分组训练再聚合，显著降低标签间性能差距（PG 最高降低 75.4%）。

**[ECPv2: Fast, Efficient, and Scalable Global Optimization of Lipschitz Functions](ecpv2_fast_efficient_and_scalable_global_optimization_of_lipschitz_functions.md)**

:   提出ECPv2算法，通过三项创新（自适应下界、Worst-$m$ memory、固定随机投影），将Lipschitz函数全局优化的运行时从$\Omega(n^2 d)$降至$\Omega(n(m+d)\log n)$，同时保持与minimax下界匹配的$O(n^{-1/d})$ regret收敛速率。

**[Explore How to Inject Beneficial Noise in MLLMs](explore_how_to_inject_beneficial_noise_in_mllms.md)**

:   提出 Multimodal Noise Generator (MuNG)，通过变分推断框架从图文对中动态生成"有益噪声"注入冻结的MLLM视觉特征中，以抑制无关语义、增强跨模态表征对齐，仅需约1%额外参数即可超越全参数微调和LoRA等PEFT方法。

**[FedP²EFT: Federated Learning to Personalize PEFT for Multilingual LLMs](fedp2eft_federated_learning_to_personalize_peft_for_multilingual_llms.md)**

:   提出FedP²EFT，通过联邦学习协作训练一个Personalization Strategy Generator (PSG)，为每个客户端自动生成个性化的LoRA rank结构，在多语言LLM微调中大幅超越手工设计的PEFT配置和现有FL个性化方法。

**[On the Learning Dynamics of Two-Layer Linear Networks with Label Noise SGD](on_the_learning_dynamics_of_two-layer_linear_networks_with_label_noise_sgd.md)**

:   在二层过参数化线性网络上理论分析 Label Noise SGD 的学习动力学，揭示了两阶段行为——Phase I 中权重范数逐渐缩小使模型从 lazy regime 逃逸到 rich regime，Phase II 中权重与真实插值器对齐并收敛——并将该理论扩展到 SAM 优化器。

**[Parametrized Multi-Agent Routing via Deep Attention Models](parametrized_multi-agent_routing_via_deep_attention_models.md)**

:   提出Deep FLPO框架，将最大熵原理（MEP）的代数结构与permutation-invariant的encoder-decoder神经网络（SPN）融合，解决设施选址与路径联合优化的NP-hard混合整数问题，实现策略推理100倍加速、与Gurobi精确解匹配且快1500倍。

**[Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization](pareto-grid-guided_large_language_models_for_fast_and_high-quality_heuristics_de.md)**

:   提出 MPaGE 框架，将 LLM 与 Pareto Front Grid 机制和语义聚类结合，自动为多目标组合优化问题生成兼顾解质量与运行效率的启发式算法，在 Bi-TSP、Tri-TSP、Bi-CVRP、Bi-KP 上 HV 和 IGD 均显著优于 EoH、MEoH 等基线。

**[Personalized Federated Learning With Bidirectional Communication Compression Via](personalized_federated_learning_with_bidirectional_communication_compression_via.md)**

:   提出 pFed1BS 框架，通过单比特随机草图实现联邦学习中上下行双向极致通信压缩（降低 99%+），同时引入基于符号的正则化器实现客户端模型个性化，在非 IID 数据场景下同时解决通信瓶颈和数据异质性两大难题。

**[SMoFi: Step-wise Momentum Fusion for Split Federated Learning on Heterogeneous Data](smofi_step-wise_momentum_fusion_for_split_federated_learning_on_heterogeneous_da.md)**

:   提出 SMoFi 框架，通过在 Split FL 的 server 端每步同步各 surrogate 模型的 momentum buffer，有效缓解 non-IID 数据导致的梯度分歧，在精度（最高+7.1%）和收敛速度（最高10.25×）上均显著优于现有方法。
