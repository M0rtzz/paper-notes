<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**🤖 AAAI2026** · 共 **5** 篇

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
