<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**🤖 AAAI2026** · 共 **28** 篇

**[Adaptive Initial Residual Connections for GNNs with Theoretical Guarantees](adaptive_initial_residual_connections_for_gnns_with_theoretical_guarantees.md)**

:   研究图神经网络中自适应初始残差连接（Adaptive IRC）——每个节点有个性化的残差强度——证明该方案防止过平滑（Dirichlet 能量有下界）、保持嵌入矩阵秩，在异质图上显著优于标准消息传递，并提出基于 PageRank 的非学习变体大幅降低复杂度。

**[Adaptive Riemannian Graph Neural Networks](adaptive_riemannian_graph_neural_networks.md)**

:   提出 ARGNN 框架，为图上每个节点学习一个连续的、各向异性的对角黎曼度量张量，从而自适应地捕获图中不同区域（层级结构 vs 密集社区）的局部几何特性，统一并超越了固定曲率和离散混合曲率的几何 GNN 方法。

**[Are Graph Transformers Necessary? Efficient Long-Range Message Passing with Fractal Nodes in MPNNs](are_graph_transformers_necessary_efficient_long-range_messag.md)**

:   提出分形节点（Fractal Nodes）增强 MPNN 的长距离消息传递：通过 METIS 图划分生成子图级聚合节点，结合低通+高通滤波器（LPF+HPF）与可学习频率参数 $\omega$，使用 MLP-Mixer 实跨子图通信，在保持 $O(L(|V|+|E|))$ 线性复杂度的同时达到甚至超越图 Transformer 的性能，获 AAAI Oral。

**[Assemble Your Crew: Automatic Multi-agent Communication Topology Design via Autoregressive Graph Generation](assemble_your_crew_automatic_multi-agent_communication_topol.md)**

:   提出 ARG-Designer，将多 Agent 系统的拓扑设计重新定义为条件自回归图生成任务，从零开始逐步生成 Agent 节点和通信边（而非从模板图剪枝），在6个基准上达到 SOTA（平均 92.78%），同时 Token 消耗比 G-Designer 降低约 50%，且支持无需重训练的角色扩展。

**[Assessing LLMs for Serendipity Discovery in Knowledge Graphs: A Case for Drug Repurposing](assessing_llms_for_serendipity_discovery_in_knowledge_graphs_a_case_for_drug_rep.md)**

:   提出 SerenQA 框架，首次形式化定义知识图谱问答中的"意外发现"(serendipity)任务，包含基于信息论的 RNS 度量、专家标注的药物重定位基准数据集和三阶段评估流水线，揭示当前 LLM 在检索任务上表现尚可但在意外发现探索上仍有巨大改进空间。

**[Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification Under Varying Homophily](beyond_fixed_depth_adaptive_graph_neural_networks_for_node_classification_under_.md)**

:   提出 AD-GNN，通过理论分析节点级别的同配/异配特性，为每个节点自适应分配不同的聚合深度，在统一框架中同时处理同配和异配图上的节点分类任务。

**[BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](bugsweeper_function-level_detection_of_smart_contract_vulnerabilities_using_grap.md)**

:   提出 BugSweeper，通过构建函数级抽象语法图 (FLAG) 并设计两阶段 GNN 架构，实现无需专家规则的端到端智能合约漏洞检测，在重入攻击检测上 F1 达 98.57%。

**[Commonality in Few: Few-Shot Multimodal Anomaly Detection via Hypergraph-Enhanced Memory](commonality_in_few_few-shot_multimodal_anomaly_detection_via_hypergraph-enhanced.md)**

:   提出 CIF，利用超图（hypergraph）提取少量训练样本的类内结构共性，指导 memory bank 的构建与搜索，在少样本多模态工业异常检测中取得 SOTA。

**[Connectivity-Guided Sparsification of 2-FWL GNNs Preserving Full Expressivity](connectivity-guided_sparsification_of_2-fwl_gnns_preserving_full_expressivity_wi.md)**

:   Co-Sparsify 提出一种基于连通性感知的稀疏化框架，通过将 3-节点交互限制在双连通分量内、2-节点交互限制在连通分量内，消除可证明冗余的计算，在保持完整 2-FWL 表达力的同时显著提升效率，在合成子结构计数任务和 ZINC、QM9 等基准上取得 SOTA。

**[EchoLess: Label-Based Pre-Computation for Memory-Efficient Heterogeneous Graph Learning](echoless_label-based_pre-computation_for_memory-efficient_heterogeneous_graph_le.md)**

:   Echoless-LP 通过分区聚焦的无回声传播（PFEP）消除标签预计算中多跳消息传递导致的训练标签泄露（回声效应），结合非对称分区方案（APS）和 PostAdjust 机制解决分区造成的信息损失和分布偏移，在保持内存高效的同时兼容任意消息传递方法，在多个异构图数据集上取得 SOTA 性能。

**[Enhancing Logical Expressiveness in GNNs via Path-Neighbor Aggregation](enhancing_logical_expressiveness_in_graph_neural_networks_via_path-neighbor_aggr.md)**

:   PN-GNN 提出在条件消息传递的基础上聚合推理路径上的邻居节点嵌入，以即插即用的方式增强 GNN 的逻辑规则表达力（严格超越 C-GNN），同时避免标注技巧（labeling trick）对泛化能力的损害，在合成数据集和真实知识图谱推理任务上均取得提升。

**[Feature-Centric Unsupervised Node Representation Learning Without Homophily Assumption](feature-centric_unsupervised_node_representation_learning_without_homophily_assu.md)**

:   提出 FUEL 方法，通过以节点特征为中心的聚类方案自适应学习图卷积的使用程度，无需同配性假设即可在同配和非同配图上均获得高质量的无监督节点表示。

**[Format as a Prior: Quantifying and Analyzing Bias in LLMs for Heterogeneous Data](format_as_a_prior_quantifying_and_analyzing_bias_in_llms_for_heterogeneous_data.md)**

:   首次系统研究 LLM 在处理异构格式数据（文本/表格/信息框/知识图谱）时的格式偏差问题，通过三阶段实验揭示偏差的存在性、数据层面驱动因素和注意力机制层面的内部成因，并验证了注意力重平衡干预的有效性。

**[GCL-OT: Graph Contrastive Learning with Optimal Transport for Heterophilic Text-Attributed Graphs](gcl-ot_graph_contrastive_learning_with_optimal_transport_for_heterophilic_text-a.md)**

:   提出 GCL-OT 框架，首次将最优传输（OT）引入异质性文本属性图的图对比学习中，通过 RealSoftMax 相似度估计、滤波提示机制和 OT 引导的潜在同质性挖掘三个模块，分别应对部分异质性、完全异质性和潜在同质性三种多粒度异质性挑战。

**[GSAP-ERE: Fine-Grained Scholarly Entity and Relation Extraction Focused on Machine Learning](gsap-ere_fine-grained_scholarly_entity_and_relation_extraction_focused_on_machin.md)**

:   提出GSAP-ERE——一个面向机器学习领域的细粒度学术实体与关系抽取数据集，包含10种实体类型和18种关系类型，在100篇全文论文上标注了63K实体和35K关系，实验表明微调模型（NER: 80.6%, RE: 54.0%）大幅超越LLM提示方法（NER: 44.4%, RE: 10.1%）。

**[GT-SNT: A Linear-Time Transformer for Large-Scale Graphs via Spiking Node Tokenization](gt-snt_a_linear-time_transformer_for_large-scale_graphs_via_spiking_node_tokeniz.md)**

:   提出 GT-SNT，将脉冲神经网络（SNN）用作图节点分词器（tokenizer），通过多步特征传播生成紧凑的脉冲计数嵌入作为节点 token，再利用码本引导自注意力（CGSA）在线性时间内捕获全局上下文，在 9 个节点分类基准上取得可比性能的同时实现最高 130× 的推理加速。

**[Hybrid-Dmkg A Hybrid Reasoning Framework Over Dynamic Multimodal Knowledge Graph](hybrid-dmkg_a_hybrid_reasoning_framework_over_dynamic_multimodal_knowledge_graph.md)**

:   提出MMQAKE基准和Hybrid-DMKG框架，在动态多模态知识图谱上构建"关系链接预测 + RAG增强LVLM推理"双通道混合推理机制，配合背景反思决策模块，在2-5跳多模态知识编辑问答中显著超越现有方法（LLaVA上H-Acc达29.90%，超IKE 13.52个百分点）。

**[Hyperbolic Continuous Structural Entropy for Hierarchical Clustering](hyperbolic_continuous_structural_entropy_for_hierarchical_clustering.md)**

:   提出 HypCSE，将离散结构熵（SE）松弛为双曲空间中的连续结构熵（CSE），结合图结构学习和对比学习，实现端到端可微的层次聚类，在 7 个数据集上全面超越离散和连续层次聚类方法。

**[Logical Characterizations of GNNs with Mean Aggregation](logical_characterizations_of_gnns_with_mean_aggregation.md)**

:   系统刻画了以均值（mean）为聚合函数的 GNN 的表达能力：非一致设定下等价于比率模态逻辑（RML）；一致设定下（相对 MSO）等价于模态逻辑（ML）；当额外要求组合函数连续、分类函数为阈值时，表达能力显著下降至交替无关模态逻辑（AFML）。

**[MUG: Meta-path-aware Universal Heterogeneous Graph Pre-Training](mug_meta-path-aware_universal_heterogeneous_graph_pre-training.md)**

:   首次提出无需 LLM 的通用异质图预训练方法 MUG，通过上下文结构编码统一异质节点/关系类型、维度感知编码器对齐不同图的表示空间，并利用元路径视图共享编码器 + 全局散射正则化实现跨域可迁移的编码与聚合，在跨域和小样本节点分类中显著超越已有方法。

**[On Stealing Graph Neural Network Models](on_stealing_graph_neural_network_models.md)**

:   证明了在严格查询限制下（如仅100次查询），攻击者可通过"本地获取encoder（随机初始化/SSL训练）+ K-means策略性查询选择"两阶段方法高效窃取GNN模型，在Physics数据集上仅用100次查询即达91%准确率，而现有SOTA需约5000次查询加额外embedding访问才能达到类似水平。

**[Posterior Label Smoothing for Node Classification](posterior_label_smoothing_for_node_classification.md)**

:   提出PosteL（Posterior Label Smoothing），通过贝叶斯后验分布从邻域标签中推导soft label用于节点分类，自然适应同质图和异质图，在8种backbone×10个数据集的80个组合中76个取得精度提升。

**[Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG](relink_constructing_query-driven_evidence_graph_on-the-fly_for_graphrag.md)**

:   提出从"先构建再推理"到"边推理边构建"的GraphRAG范式转变，通过Relink框架动态构建查询特定的证据图——结合高精度KG骨架和高召回潜在关系池，用查询驱动的排序器统一评估、按需补全缺失路径并过滤干扰事实——在5个多跳QA基准上平均提升EM 5.4%和F1 5.2%。

**[RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA](rfkg-cot_relation-driven_adaptive_hop-count_selection_and_few-shot_path_guidance.md)**

:   提出RFKG-CoT，通过关系驱动的自适应跳数选择（利用KG关系激活掩码动态调整推理步数）和Few-Shot路径引导（Question-Paths-Answer格式的in-context示例），在4个KGQA基准上显著提升LLM的知识图谱推理能力，GPT-4在WebQSP上达91.5%（+6.6pp），Llama2-7B提升幅度最大达+14.7pp。

**[S-DAG: A Subject-Based Directed Acyclic Graph for Multi-Agent Heterogeneous Reasoning](s-dag_a_subject-based_directed_acyclic_graph_for_multi-agent.md)**

:   提出 S-DAG，通过 GNN 从问题中识别相关学科及其依赖关系构建有向无环图，将学科节点匹配到最擅长的专家 LLM（14 个 7-13B 领域模型），按 DAG 拓扑顺序协作推理（支撑学科→主导学科），用小模型池超越 GPT-4o-mini（59.73 vs 58.52）且接近 72B 模型。

**[Self-Adaptive Graph Mixture of Models](self-adaptive_graph_mixture_of_models.md)**

:   提出 SAGMM 框架，通过拓扑感知注意力门控机制（TAAG）自动选择和组合来自异构 GNN 专家池（GCN/GAT/GraphSAGE 等）的输出，并引入自适应专家剪枝策略，在 16 个基准数据集上的节点分类、图分类、回归和链接预测任务中全面超越单一 GNN 和现有 MoE 方法。

**[Sheaf Graph Neural Networks via PAC-Bayes Spectral Optimization](sheaf_graph_neural_networks_via_pac-bayes_spectral_optimization.md)**

:   提出 SGPC（Sheaf GNNs with PAC-Bayes Calibration），结合 Wasserstein 最优传输学习 sheaf 限制映射、方差缩减扩散与自适应频率混合层、以及 PAC-Bayes 谱正则化，在同质和异质图节点分类上全面超越现有 GNN 和 sheaf 方法，同时提供理论泛化保证。

**[Unihr Hierarchical Representation Learning For Unified Knowledge Graph Link Pred](unihr_hierarchical_representation_learning_for_unified_knowledge_graph_link_pred.md)**

:   提出UniHR框架，通过Hierarchical Data Representation (HiDR)将超关系/时序/嵌套等多类KG统一转换为三元组形式，并设计Hierarchical Structure Learning (HiSL)模块在事实内部和事实间进行两阶段消息传递，在9个数据集5种KG类型上取得最优或竞争性的link prediction结果。
