---
title: >-
  ICML2025 图学习方向 31篇论文解读
description: >-
  31篇ICML2025 图学习方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**🧪 ICML2025** · 共 **31** 篇

**[A Cognac Shot To Forget Bad Memories Corrective Unlearning For Graph Neural Netw](a_cognac_shot_to_forget_bad_memories_corrective_unlearning_for_graph_neural_netw.md)**

:   提出 Cognac——首个有效的 GNN 纠正性遗忘方法，通过交替执行图邻域对比遗忘（CoGN）和解耦梯度上升/下降（AC⚡DC），在仅识别 5% 被操纵实体时即可恢复接近 oracle（完全干净数据训练）的性能，比从头重训高效 8×。

**[A General Graph Spectral Wavelet Convolution Via Chebyshev Order Decomposition](a_general_graph_spectral_wavelet_convolution_via_chebyshev_order_decomposition.md)**

:   提出 WaveGC——通过分离 Chebyshev 多项式的奇偶项构建严格满足可容许性条件的可学习图小波，结合矩阵值滤波核的多分辨率图谱卷积网络，在短程和长程图任务上均实现一致改进（VOC 上提升 15.7%）。

**[A Recipe For Causal Graph Regression Confounding Effects Revisited](a_recipe_for_causal_graph_regression_confounding_effects_revisited.md)**

:   首次系统性地将因果图学习从分类扩展到回归任务，通过增强型图信息瓶颈（Enhanced GIB）承认混淆子图的预测能力，并用对比学习替代依赖离散标签的因果干预方法，在图级 OOD 回归基准上显著超越现有方法。

**[Balancing Efficiency And Expressiveness Subgraph Gnns With Walk-Based Centrality](balancing_efficiency_and_expressiveness_subgraph_gnns_with_walk-based_centrality.md)**

:   提出 HyMN——通过游走中心性（Subgraph Centrality）对子图 GNN 的子图包进行高效采样，仅需 1-2 个子图即可媲美全包 Subgraph GNN 的性能，同时将中心性作为结构编码进一步增强判别能力，使子图方法首次可扩展到数百倍更大的图。

**[Banyan Improved Representation Learning With Explicit Structure](banyan_improved_representation_learning_with_explicit_structure.md)**

:   Banyan 通过**纠缠层次树结构**和**对角化消息传递**两大创新，仅用 14 个非嵌入参数就在语义文本相似度任务上超越了大规模 Transformer 模型，为低资源语言的语义表示学习提供了高效可行的替代方案。

**[Beyond Message Passing Neural Graph Pattern Machine](beyond_message_passing_neural_graph_pattern_machine.md)**

:   提出 Neural Graph Pattern Machine (GPM)，用随机游走采样图模式，通过语义路径与匿名路径的双编码器捕捉节点特征和拓扑结构，再用 Transformer 识别任务相关的关键模式，彻底绕过消息传递范式，在节点/边/图级任务上全面超越 SOTA。

**[Cody Counterfactual Explainers For Dynamic Graphs](cody_counterfactual_explainers_for_dynamic_graphs.md)**

:   提出 CoDy——首个用于时序图神经网络（TGNN）的反事实解释方法，通过蒙特卡洛树搜索（MCTS）结合时空启发式策略高效探索可能的解释子图空间，在多个数据集上 AUFSC+ 提升 16%。

**[Diss-L-Ect Dissecting Graph Data With Local Euler Characteristic Transforms](diss-l-ect_dissecting_graph_data_with_local_euler_characteristic_transforms.md)**

:   提出 Local Euler Characteristic Transform (ℓ-ECT)，将经典 ECT 拓扑不变量扩展到图的局部邻域，为每个节点生成无损的拓扑-几何指纹，在节点分类任务（尤其是高异质性图）上超越标准 GNN，同时提供理论可逆性保证与可解释性。

**[Does Graph Prompt Work A Data Operation Perspective With Theoretical Analysis](does_graph_prompt_work_a_data_operation_perspective_with_theoretical_analysis.md)**

:   首次从"数据操作"角度为 Graph Prompt 提供完整理论框架：证明 Prompt 能通过模拟图数据变换将原始图映射到"桥接图"使冻结模型适配下游任务，并推导了单图/多图场景下的误差上界与分布。

**[From Rag To Memory Non-Parametric Continual Learning For Large Language Models](from_rag_to_memory_non-parametric_continual_learning_for_large_language_models.md)**

:   提出 HippoRAG 2，通过将段落节点融入知识图谱、用 query-to-triple 深度上下文化链接、以及 LLM 驱动的识别记忆过滤，全面超越标准 RAG 在事实记忆、语义理解和关联推理三大维度的表现，向 LLM 的非参数化持续学习迈进一步。

**[Graph-Constrained Reasoning Faithful Reasoning On Knowledge Graphs With Large La](graph-constrained_reasoning_faithful_reasoning_on_knowledge_graphs_with_large_la.md)**

:   提出 Graph-constrained Reasoning (GCR)，通过将知识图谱编码为 KG-Trie 并嵌入 LLM 解码过程，实现零幻觉的忠实推理，在 KGQA 基准上达到 SOTA 且具备零样本跨图谱迁移能力。

**[Graph Attention Is Not Always Beneficial A Theoretical Analysis Of Graph Attenti](graph_attention_is_not_always_beneficial_a_theoretical_analysis_of_graph_attenti.md)**

:   通过 CSBM 理论分析揭示图注意力并非总有益：结构噪声>特征噪声时有效，反之简单卷积更优；多层 GAT 的完美分类 SNR 要求从 $\omega(\sqrt{\log n})$ 放松到 $\omega(\sqrt{\log n}/\sqrt[3]{n})$。

**[Grokformer Graph Fourier Kolmogorov-Arnold Transformers](grokformer_graph_fourier_kolmogorov-arnold_transformers.md)**

:   提出 GrokFormer，通过傅里叶级数参数化的 Kolmogorov-Arnold 可学习激活函数，在图 Laplacian 的多阶谱上自适应学习滤波器基，同时具备 **谱阶自适应** 和 **谱自适应** 能力，是目前唯一在两个维度上都可学习的图 Transformer 滤波器。

**[Hgot Self-Supervised Heterogeneous Graph Neural Network With Optimal Transport](hgot_self-supervised_heterogeneous_graph_neural_network_with_optimal_transport.md)**

:   提出 HGOT，首次将最优传输理论引入异质图自监督学习，用 branch view（元路径视图）与 central view（聚合视图）之间的 Fused Gromov-Wasserstein 传输计划替代传统对比学习中的数据增强与正负样本选取，在节点分类上平均提升超过 6%。

**[Hyperbolic-Pde Gnn Spectral Graph Neural Networks In The Perspective Of A System](hyperbolic-pde_gnn_spectral_graph_neural_networks_in_the_perspective_of_a_system.md)**

:   将消息传递建模为双曲偏微分方程组，证明节点特征的解空间由拉普拉斯矩阵的特征向量张成，从而将拓扑结构信息内嵌到节点表示中，并通过多项式近似建立与谱 GNN 的桥梁以增强其性能。

**[Is Complex Query Answering Really Complex](is_complex_query_answering_really_complex.md)**

:   本文揭示了知识图谱复杂查询回答（CQA）现有基准中高达 98% 的"复杂"查询实际上可被简化为简单的单链接预测问题，由此导致研究进展被严重高估；作者提出了平衡采样的新基准（FB15k237+H、NELL995+H、ICEWS18+H），并引入混合求解器 CQD-Hybrid 验证了这一发现，在新基准上所有 SOTA 方法的 MRR 大幅下降（最多超过 30 个点）。

**[Learnable Spatial-Temporal Positional Encoding for Link Prediction](learnable_spatial-temporal_positional_encoding_for_link_prediction.md)**

:   提出 L-STEP，一种可学习的时空位置编码方法，从时空谱角度证明可保持图属性，仅用 MLP 即可达到 Transformer 性能，在 13 个数据集和 TGB 基准上取得领先表现，且计算复杂度更优。

**[Llm Enhancers For Gnns An Analysis From The Perspective Of Causal Mechanism Iden](llm_enhancers_for_gnns_an_analysis_from_the_perspective_of_causal_mechanism_iden.md)**

:   从因果机制识别的角度分析"LLM增强器+GNN"范式的内部机制，发现LLM增强器主要提供节点级/原始数据级信息，并据此提出注意力传输（AT）模块优化两者间的信息传递。

**[Machines And Mathematical Mutations Using Gnns To Characterize Quiver Mutation C](machines_and_mathematical_mutations_using_gnns_to_characterize_quiver_mutation_c.md)**

:   利用图神经网络 (GNN) 和可解释性技术研究箭图变异等价类问题，**独立重新发现**了 $\tilde{D}$ 型箭图变异类的组合刻画定理，展示了 ML 作为数学研究工具的价值。

**[Mitigating Over-Squashing In Graph Neural Networks By Spectrum-Preserving Sparsi](mitigating_over-squashing_in_graph_neural_networks_by_spectrum-preserving_sparsi.md)**

:   提出 GOKU（稠密化-稀疏化重连范式），通过将输入图视为未知稠密潜在图的谱稀疏器并求解逆稀疏化问题，在增强图连通性的同时显式保留拉普拉斯谱，有效缓解 GNN 的 over-squashing 问题。

**[Mixed-Curvature Decision Trees And Random Forests](mixed-curvature_decision_trees_and_random_forests.md)**

:   将经典决策树和随机森林算法从欧几里得空间推广到混合曲率乘积流形（hyperbolic × spherical × Euclidean），通过角度重参数化（angular reformulation）构造尊重流形几何的分裂准则，在 57 个分类/回归/链路预测任务上表现优异（29 个第一，41 个前二）。

**[Modeling All-Atom Glycan Structures Via Hierarchical Message Passing And Multi-S](modeling_all-atom_glycan_structures_via_hierarchical_message_passing_and_multi-s.md)**

:   提出 GlycanAA，首个全原子级糖链建模方法：将糖链表示为包含原子节点和单糖节点的异构图，通过层次消息传递捕获从局部原子交互到全局单糖交互的多尺度信息，并通过多尺度掩码预测预训练（PreGlycanAA）进一步增强，在 GlycanML 基准 11 个任务上获得第一。

**[Neural Graph Matching Improves Retrieval Augmented Generation In Molecular Machi](neural_graph_matching_improves_retrieval_augmented_generation_in_molecular_machi.md)**

:   提出 MARASON，将**神经图匹配（Neural Graph Matching）**引入分子机器学习的检索增强生成（RAG）框架，通过可微分的碎片级对齐机制，把检索到的参考分子谱图信息有效融入目标分子的质谱预测中，在 NIST 数据集上将 top-1 检索准确率从 19% 提升到 28%。

**[On Measuring Long-Range Interactions In Graph Neural Networks](on_measuring_long-range_interactions_in_graph_neural_networks.md)**

:   形式化定义了图任务中的"长距离交互"概念，提出基于距离×影响力的range measure来量化算子的作用范围，发现常用LRGB基准和架构在实际中并非真正"长距离"的。

**[Open Your Eyes Vision Enhances Message Passing Neural Networks In Link Predictio](open_your_eyes_vision_enhances_message_passing_neural_networks_in_link_predictio.md)**

:   首次将视觉感知引入消息传递图神经网络(MPNN)，通过将子图可视化为图像并用视觉编码器提取视觉结构特征(VSF)，提出 GVN/E-GVN 框架，在 7 个链接预测基准上均达到 SOTA。

**[Positional Encoding Meets Persistent Homology On Graphs](positional_encoding_meets_persistent_homology_on_graphs.md)**

:   理论证明位置编码（PE）和持续同调（PH）互不可比——各存在对方失败但自身成功的图构造，提出 PiPE 方法统一两者，可证明比单独使用更具表达力，在分子/分类/OOD任务上表现优异。

**[Tined Gnns-To-Mlps By Teacher Injection And Dirichlet Energy Distillation](tined_gnns-to-mlps_by_teacher_injection_and_dirichlet_energy_distillation.md)**

:   提出 TINED，将 GNN 中特征变换（FT）的参数直接注入 MLP（Teacher Injection），并用 Dirichlet 能量蒸馏传递 GNN 层中 FT 与图传播（GP）的对立平滑特性，在 7 个数据集上超越 GNN 教师，推理速度提升 94 倍。

**[Toward Data-Centric Directed Graph Learning An Entropy-Driven Approach](toward_data-centric_directed_graph_learning_an_entropy-driven_approach.md)**

:   提出 EDEN（熵驱动有向图知识蒸馏），从数据中心视角利用层级知识树和互信息量化揭示有向图中拓扑与节点属性的潜在关联，作为即插即用模块增强任意 DiGNN 性能。

**[Towards Graph Foundation Models Learning Generalities Across Graphs Via Task-Tre](towards_graph_foundation_models_learning_generalities_across_graphs_via_task-tre.md)**

:   提出 Task-Tree 作为统一学习实例对齐节点/边/图级任务，理论分析其稳定性/可迁移性/泛化性，构建图基础模型 GIT 在 32 个图上通过微调/上下文学习/零样本展现跨域跨任务泛化能力。

**[Unifews You Need Fewer Operations For Efficient Graph Neural Networks](unifews_you_need_fewer_operations_for_efficient_graph_neural_networks.md)**

:   Unifews 提出统一的逐元素稀疏化框架，将 GNN 的图传播和特征变换视为矩阵运算，基于幅值阈值同时剪枝图边和模型权重，通过谱图平滑理论给出有界近似误差保证，在十亿边级别图上实现高达 100x 加速且不损失精度。

**[Wilting Trees Interpreting The Distance Between Mpnn Embeddings](wilting_trees_interpreting_the_distance_between_mpnn_embeddings.md)**

:   本文发现MPNN学到的嵌入距离与任务相关的functional distance对齐（而非结构距离），并提出基于加权Weisfeiler-Leman标记树（WILT）的最优传输距离来蒸馏和解释MPNN距离，边权揭示了少量关键子图主导了嵌入空间的度量结构。
