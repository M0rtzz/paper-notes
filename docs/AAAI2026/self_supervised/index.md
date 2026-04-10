<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**🤖 AAAI2026** · 共 **12** 篇

**[BCE3S: Binary Cross-Entropy Based Tripartite Synergistic Learning for Long-tailed Recognition](bce3s_binary_cross-entropy_based_tripartite_synergistic_learning_for_long-tailed.md)**

:   提出 BCE3S，一种基于二元交叉熵（BCE）的三方协同学习框架，将 BCE 式联合学习、BCE 式对比学习和 BCE 式分类器均匀性学习集成在一起，通过 Sigmoid 解耦不同类别的度量来抑制长尾不平衡效应，在 CIFAR10/100-LT、ImageNet-LT 和 iNaturalist2018 上均取得 SOTA。

**[Explainable Melanoma Diagnosis with Contrastive Learning and LLM-based Report Generation](explainable_melanoma_diagnosis_with_contrastive_learning_and_llm-based_report_ge.md)**

:   提出 CEFM 框架，通过跨模态对比学习将 ViT 视觉特征与基于 ABCD 规则的临床特征（不对称性、边界、颜色）对齐，再由 CLIP + DeepSeek 生成结构化诊断报告，在 ISIC 数据集上达到 92.79% 准确率和 0.961 AUC，专家评分可解释性达 4.6/5。

**[Explanation-Preserving Augmentation for Semi-Supervised Graph Representation Learning](explanation-preserving_augmentation_for_semi-supervised_graph_representation_lea.md)**

:   提出EPA-GRL（Explanation-Preserving Augmentation），利用少量标签训练的GNN explainer识别图的语义子图（explanation subgraph），增强时只扰动非语义部分（marginal subgraph），实现语义保持的图增强，在6个benchmark上显著优于语义无关的随机增强方法。

**[Improving Region Representation Learning from Urban Imagery with Noisy Long-Caption Supervision](improving_region_representation_learning_from_urban_imagery_with_noisy_long-capt.md)**

:   提出 UrbanLN 框架，通过长文本感知的位置编码插值策略和数据-模型双层噪声抑制机制，改善基于 LLM 生成描述的城市区域表征学习。

**[Let The Void Be Void Robust Open-Set Semi-Supervised Learning Via Selective Non-](let_the_void_be_void_robust_open-set_semi-supervised_learning_via_selective_non-.md)**

:   提出 SkipAlign 框架，在对比学习的传统 pull/push 操作之外引入第三种 "skip" 操作，对低置信度样本选择性跳过对齐（只做温和排斥），使 ID 类形成紧凑"星系"、OOD 样本自然散布于"星际虚空"，在未见过的 OOD 检测中平均 AUC 提升 +3.1，最高 +7.1。

**[MovSemCL: Movement-Semantics Contrastive Learning for Trajectory Similarity (Extension)](movsemcl_movement-semantics_contrastive_learning_for_trajectory_similarity_exten.md)**

:   提出 MovSemCL 框架，将 GPS 轨迹转化为运动语义特征（位移向量 + 航向角 + Node2Vec 空间图嵌入），通过 patch 级双层注意力实现层次编码（复杂度从 $O(L^2)$ 降为近线性），并设计曲率引导增广（CGA）保留转弯/路口等行为关键片段，在轨迹检索任务上 mean rank 接近理想值 1，推理延迟降低 43.4%。

**[NeuroBridge: Bio-Inspired Self-Supervised EEG-to-Image Decoding via Cognitive Priors and Bidirectional Semantic Alignment](neurobridge_bio-inspired_self-supervised_eeg-to-image_decoding_via_cognitive_pri.md)**

:   提出NeuroBridge框架，通过认知先验增强（CPA，非对称增广模拟感知变异性）和共享语义投影器（SSP，双向对齐到统一语义空间），在THINGS-EEG数据集200类零样本EEG-图像检索任务上达到63.2% Top-1（+12.3%）和89.9% Top-5（+10.2%），大幅超越现有SOTA。

**[Robust Tabular Foundation Models](robust_tabular_foundation_models.md)**

:   提出 RTFM——一种模型无关的对抗训练框架，通过在合成数据生成器的参数空间上做 min-max 优化（最大化 TFM 与传统树模型之间的"最优性差距"），仅用不到 10 万额外合成数据集就显著提升了 TabPFN V2 在多个表格基准上的表现。

**[Self-Supervised Inductive Logic Programming](self-supervised_inductive_logic_programming.md)**

:   提出 Self-Supervised ILP 新范式和 Poker 系统，通过在学习过程中自动生成正负例来替代人工标注负例和定制背景理论，实现从少量正例学习递归逻辑程序。

**[Spikingformer: A Key Foundation Model for Spiking Neural Networks](spikingformer_a_key_foundation_model_for_spiking_neural_networks.md)**

:   提出 Spikingformer，通过将 MS Residual 与 Self-Attention 以 spike-driven 方式结合，解决 Spikformer 中 SEW Residual 导致的非脉冲计算问题，同时保持全局建模能力。

**[Towards Better Code Understanding in Decoder-Only Models with Contrastive Learning](towards_better_code_understanding_in_decoder-only_large_language_models_via_hie.md)**

:   提出CL4D对比学习框架，通过继续预训练将decoder-only代码生成模型适配到代码理解任务（代码搜索、克隆检测），在不重新训练encoder模型的前提下实现了与同等规模encoder-only模型相当甚至更优的性能。

**[Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space](towards_llm-empowered_knowledge_tracing_via_llm-student_hierarchical_behavior_al.md)**

:   提出 L-HAKT 框架，利用 LLM 双 Agent（Teacher + Student）生成合成数据，在双曲空间中进行对比对齐，将知识点的树状层级结构显式建模到知识追踪中。
