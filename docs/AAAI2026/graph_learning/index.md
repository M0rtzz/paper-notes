<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**🤖 AAAI2026** · 共 **15** 篇

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

**[Posterior Label Smoothing for Node Classification](posterior_label_smoothing_for_node_classification.md)**

:   提出PosteL（Posterior Label Smoothing），通过贝叶斯后验分布从邻域标签中推导soft label用于节点分类，自然适应同质图和异质图，在8种backbone×10个数据集的80个组合中76个取得精度提升。

**[Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG](relink_constructing_query-driven_evidence_graph_on-the-fly_for_graphrag.md)**

:   提出从"先构建再推理"到"边推理边构建"的GraphRAG范式转变，通过Relink框架动态构建查询特定的证据图——结合高精度KG骨架和高召回潜在关系池，用查询驱动的排序器统一评估、按需补全缺失路径并过滤干扰事实——在5个多跳QA基准上平均提升EM 5.4%和F1 5.2%。

**[RFKG-CoT: Relation-Driven Adaptive Hop-count Selection and Few-Shot Path Guidance for Knowledge-Aware QA](rfkg-cot_relation-driven_adaptive_hop-count_selection_and_few-shot_path_guidance.md)**

:   提出RFKG-CoT，通过关系驱动的自适应跳数选择（利用KG关系激活掩码动态调整推理步数）和Few-Shot路径引导（Question-Paths-Answer格式的in-context示例），在4个KGQA基准上显著提升LLM的知识图谱推理能力，GPT-4在WebQSP上达91.5%（+6.6pp），Llama2-7B提升幅度最大达+14.7pp。

**[S-DAG: A Subject-Based Directed Acyclic Graph for Multi-Agent Heterogeneous Reasoning](s-dag_a_subject-based_directed_acyclic_graph_for_multi-agent.md)**

:   提出 S-DAG，通过 GNN 从问题中识别相关学科及其依赖关系构建有向无环图，将学科节点匹配到最擅长的专家 LLM（14 个 7-13B 领域模型），按 DAG 拓扑顺序协作推理（支撑学科→主导学科），用小模型池超越 GPT-4o-mini（59.73 vs 58.52）且接近 72B 模型。
