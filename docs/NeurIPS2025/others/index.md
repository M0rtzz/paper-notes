<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**🧠 NeurIPS2025** · 共 **91** 篇

**[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](4dgt_learning_a_4d_gaussian_transformer_using_realworld_mono.md)**

:   提出4DGT——一种基于4D高斯的Transformer模型，完全在真实世界单目带位姿视频上训练，以前馈方式在几秒内完成动态场景重建，显著优于同类前馈网络，并达到与优化类方法可比的精度。

**[A Cramér–von Mises Approach to Incentivizing Truthful Data Sharing](a_cramrvon_mises_approach_to_incentivizing_truthful_data_sha.md)**

:   提出一种基于 Cramér-von Mises 两样本检验统计量的激励机制，在贝叶斯和无先验两种设定下均能证明"如实提交数据"构成（近似）Nash 均衡，同时鼓励参与者提交更多真实数据，且不依赖对数据分布的强假设（如高斯、伯努利）。

**[A Differentiable Model Of Supply-Chain Shocks](a_differentiable_model_of_supply-chain_shocks.md)**

:   用 JAX 实现可微分的供应链 Agent-Based Model（~1000 家企业），通过 GPU 并行化 + 自动微分实现比传统 ABC 快 3 个数量级的贝叶斯参数校准，为全球供应链网络的冲击传播建模铺平道路。

**[A Generalized Label Shift Perspective for Cross-Domain Gaze Estimation](a_generalized_label_shift_perspective_for_crossdomain_gaze_e.md)**

:   本文将跨域视线估计(CDGE)问题建模为广义标签偏移(GLS)问题，指出现有域不变表示学习方法在标签偏移存在时理论上不充分，提出基于截断高斯分布的连续重要性重加权和概率感知条件算子差异(PCOD)来联合纠正标签偏移和条件偏移，在多个backbone上平均降低误差12%~27%。

**[A High-Dimensional Statistical Method for Optimizing Transfer Quantities in Multi-Source Transfer Learning](a_highdimensional_statistical_method_for_optimizing_transfer.md)**

:   提出基于K-L散度和高维统计分析的理论框架，用于确定多源迁移学习中每个源任务的最优样本迁移数量，避免"用所有源数据"带来的负迁移问题，在DomainNet和Office-Home上超过SOTA 1.0-1.5%的同时减少47.85%的样本使用量和35.19%的训练时间。

**[A Reliable Cryptographic Framework for Empirical Machine Unlearning Evaluation](a_reliable_cryptographic_framework_for_empirical_machine_unl.md)**

:   将机器遗忘的评估问题建模为密码学博弈（unlearning sample inference game），通过定义adversary的"advantage"来衡量遗忘质量，克服了传统MIA准确率作为评估指标的多种缺陷（不以retrain为零基准、对数据划分敏感、对MIA选择敏感），并提出SWAP test作为高效的实用近似方案。

**[A Standardized Benchmark for Multilabel Antimicrobial Peptide Classification](a_standardized_benchmark_for_multilabel_antimicrobial_peptide_classification.md)**

:   提出 **ESCAPE**——首个标准化的多标签抗菌肽分类基准，整合 27 个公开数据库共 80,000+ 肽段，并设计基于双分支 Transformer + 双向交叉注意力的 Baseline 模型，在 mAP 上相对第二名提升 2.56%。

**[A Sustainable AI Economy Needs Data Deals That Work for Generators](a_sustainable_ai_economy_needs_data_deals_that_work_for_gene.md)**

:   本文通过分析73个公开数据交易案例，揭示了ML价值链中的"经济数据处理不等式"——从原始数据到模型权重再到合成输出，每一步都提炼了技术信号但剥夺了数据生成者的经济权益，并提出EDVEX框架来构建更公平的数据交换市场。

**[A Theoretical Framework for Grokking: Interpolation followed by Riemannian Norm Minimisation](a_theoretical_framework_for_grokking_interpolation_followed_by_riemannian_norm_m.md)**

:   本文从纯优化角度严格证明了 grokking 现象的成因：带小 weight decay 的梯度流在 $\lambda\to 0$ 极限下呈现两阶段动力学——先快速收敛到训练损失的临界流形 $\mathcal{M}$，再在 $t\approx 1/\lambda$ 时沿流形做黎曼梯度流以最小化 $\ell_2$ 范数，从而延迟实现泛化。

**[A Unified Framework for Provably Efficient Algorithms to Estimate Shapley Values](a_unified_framework_for_provably_efficient_algorithms_to_estimate_shapley_values.md)**

:   提出统一框架将 KernelSHAP、LeverageSHAP 等 Shapley 值估计器纳入随机草图（sketching）视角，首次为 KernelSHAP 提供非渐近理论保证，并通过算法改进（Poisson 近似等）将方法扩展到 CIFAR-10 等高维数据集。

**[A Unified Framework for Variable Selection in Model-Based Clustering with Missing Not at Random](a_unified_framework_for_variable_selection_in_modelbased_clu.md)**

:   提出了一个统一框架（SelvarMNARz），在高斯混合模型聚类中同时完成变量选择和MNAR（Missing Not At Random）缺失数据建模，通过两阶段策略（LASSO排序 + BIC角色分配）实现高维场景下的高效推理，并给出了可辨识性和选择一致性的理论保证。

**[Active Measurement: Efficient Estimation at Scale](active_measurement_efficient_estimation_at_scale.md)**

:   提出Active Measurement框架，结合AI检测器的自适应重要性采样和迭代人工标注，实现大规模科学测量（如鸟类计数、疟疾检测）的无偏估计，将原始检测器3.78的误差率降至0.06，同时提供理论保证的置信区间。

**[AcuRank: 不确定性感知的自适应计算重排序](acurank_uncertainty-aware_adaptive_computation_for_listwise_reranking.md)**

:   通过基于TrueSkill模型的不确定性估计，动态调整重排序子集大小和验证范围，在实现更优精度效率权衡的同时避免过度计算。

**[AdaptGrad: Adaptive Sampling to Reduce Noise](adaptgrad_adaptive_sampling_to_reduce_noise.md)**

:   通过卷积公式视角首次理论分析了SmoothGrad的噪声来源（越界采样），提出AdaptGrad方法通过概率界约束采样范围来抑制噪声，在不增加计算开销的前提下提升梯度显著性图的质量。

**[Adaptive Data Analysis for Growing Data](adaptive_data_analysis_for_growing_data.md)**

:   首次为动态/增长数据场景下的自适应数据分析提供泛化界，允许分析者根据当前数据规模和历史查询结果自适应地调度统计查询，在数据不断积累时获得更紧的准确性保证。

**[Additive Models Explained: A Computational Complexity Approach](additive_models_explained_a_computational_complexity_approach.md)**

:   对广义可加模型（GAM）的多种解释类型（充分理由、对比解释、Shapley值等）进行系统的计算复杂度分析，揭示了GAM的可解释性代价高度依赖于输入域类型、组件模型类型和任务类型（回归vs分类），某些看似"可解释"的设定实际上是NP-Hard甚至#P-Hard。

**[Addressing Mark Imbalance In Integrationfree Neural Marked T](addressing_mark_imbalance_in_integrationfree_neural_marked_t.md)**

:   论文针对现实事件流中常见的 mark 类别长尾失衡问题，提出基于先验归一化概率的阈值学习策略，并设计 integration-free 的神经 MTPP 架构，先预测 mark 再预测 time，在避免昂贵数值积分的同时显著提升稀有事件的 mark 与到达时间预测性能。

**[Adjoint Schrödinger Bridge Sampler](adjoint_schrödinger_bridge_sampler.md)**

:   提出 Adjoint Schrödinger Bridge Sampler (ASBS)，通过将 Schrödinger Bridge 问题重新解释为随机最优控制问题，消除了先前扩散采样器的 memoryless 条件限制，支持任意源分布（如高斯、谐波先验），使用可扩展的 matching 目标无需重要性权重估计，在多粒子能量函数和分子构象生成上全面超越先前方法。

**[ADPretrain: Advancing Industrial Anomaly Detection via Anomaly Representation Pretraining](adpretrain_advancing_industrial_anomaly_detection_via_anomaly_representation_pre.md)**

:   首次提出面向工业异常检测的专用表示预训练框架 ADPretrain，通过角度和范数导向的对比损失在大规模异常检测数据集 RealIAD 上学习残差特征表示，替换五种主流嵌入式 AD 方法的原始特征后在五个数据集、五个骨干网络上取得一致性提升。

**[Aggregation Hides OOD Generalization Failures from Spurious Correlations](aggregation_hides_out-of-distribution_generalization_failures_from_spurious_corr.md)**

:   揭示 OOD 泛化 benchmark 中"聚合掩蔽"现象——aggregate 评估显示 accuracy-on-the-line（ID 与 OOD 准确率正相关），但 OODSelect 方法可从同一 OOD 数据中找到大规模语义连贯子集（最高达 75%），这些子集上 ID 越高 OOD 反而越低（Pearson R 低至 -0.92），证明虚假相关的危害被聚合评估系统性隐藏。

**[Alias-Free ViT: Fractional Shift Invariance via Linear Attention](alias-free_vit_fractional_shift_invariance_via_linear_attention.md)**

:   提出Alias-Free ViT，通过两个关键组件实现Vision Transformer对整数和亚像素平移的鲁棒性：(1) 抗混叠下采样和非线性层设计，(2) 基于交叉协方差的线性注意力（shift-equivariant），在图像分类中保持竞争力的同时显著提升对抗性平移鲁棒性。

**[Alternating Gradient Flows: A Theory of Feature Learning in Two-layer Neural Networks](alternating_gradient_flows_a_theory_of_feature_learning_in_two-layer_neural_netw.md)**

:   提出交替梯度流（AGF）理论框架解释神经网络的逐步"鞍到鞍"特征学习动力学——将训练建模为休眠神经元的效用最大化和活跃神经元的代价最小化的交替过程，统一了对角线性网络、注意力模型和模块加法的特征选择分析，预测与实际梯度流高度一致。

**[An Analysis of Concept Bottleneck Models: Measuring, Understanding, and Mitigating Noisy Annotations](an_analysis_of_concept_bottleneck_models_measuring_understanding_and_mitigating_.md)**

:   首次系统研究噪声概念标注对 CBM 的影响——发现即使中等噪声也同时损害预测性能、可解释性和干预效果，识别出"脆弱概念"子集是性能下降的主因，提出训练阶段用 SAM 稳定脆弱概念学习 + 推断阶段用预测熵排序仅校正最不确定概念的两阶段缓解框架。

**[An Empirical Investigation of Neural ODEs and Symbolic Regression for Dynamical Systems](an_empirical_investigation_of_neural_odes_and_symbolic_regression_for_dynamical_.md)**

:   系统实证研究 Neural ODE 和符号回归（SR）在动力系统建模中的组合使用：NODE 可以在动态相似条件下外推到新边界条件，SR 可以从有噪声数据中恢复控制方程，且用 NODE 训练数据（仅 10% 原始数据）生成的数据也能让 SR 恢复大部分方程。

**[EPHAD: An Evidence-Based Post-Hoc Adjustment Framework for Anomaly Detection Under Data Contamination](an_evidence-based_post-hoc_adjustment_framework_for_anomaly_detection_under_data.md)**

:   EPHAD 提出一种测试时后处理框架来修正在被污染数据上训练的异常检测模型——在不接触训练流程/数据的前提下，用多模态基础模型（CLIP）或经典方法（LOF）等"证据"在测试时调整模型输出，在 8 个视觉+26 个表格 AD 数据集上有效提升性能。

**[Are Pixel-Wise Metrics Reliable For Sparse-View Computed Tomography Reconstructi](are_pixel-wise_metrics_reliable_for_sparse-view_computed_tomography_reconstructi.md)**

:   揭示 PSNR/SSIM 等像素级指标无法反映稀疏视图 CT 重建中解剖结构完整性（相关性仅 0.16-0.30），提出基于自动分割的解剖感知指标（NSD/clDice）和 CARE 框架——在扩散模型训练中加入分割引导损失，大器官结构完整性提升 32%、血管提升 36%。

**[Asymmetric Duos: Sidekicks Improve Uncertainty](asymmetric_duos_sidekicks_improve_uncertainty.md)**

:   Asymmetric Duos（AD）将一个大模型与一个小"sidekick"配对——通过温度加权的 logit 平均融合两者预测，在仅增加 10-20% FLOPs 的条件下达到接近 5× 深度集成的不确定性估计质量，RN50 AD（5% FLOPs 额外开销）在 AUROC/AURC/SAC@98 上接近 m=5 深度集成（400% 额外 FLOPs）。

**[AutoSciDACT: Automated Scientific Discovery through Contrastive Embedding and Hypothesis Testing](autoscidact_automated_scientific_discovery_through_contrastive_embedding_and_hyp.md)**

:   提出 AutoSciDACT 管线：先用有监督对比学习将高维科学数据压缩到 4 维嵌入空间，再用 NPLM（New Physics Learning Machine）似然比检验对嵌入空间中的分布偏差进行统计量化，在天文、粒子物理、病理、图像和合成数据集上以 ≤1% 的信号注入比例实现 ≥3σ 发现。

**[AVerImaTeC: A Dataset for Automatic Verification of Image-Text Claims with Evidence from the Web](averimatec_a_dataset_for_automatic_verification_of_image-text_claims_with_eviden.md)**

:   AVerImaTeC 构建了首个带完整证据标注的图文事实核查数据集——1297 条真实图文声明 + 5 阶段标注流水线（提取→QA 推理→充分性检查→迭代精炼→二次检查）+ 时间约束证据（防止时间泄露），基线系统在有 ground truth 证据时准确率 82%，但自动检索证据后降至 15-25%，揭示了图文核查的巨大挑战。

**[Beyond Benign Overfitting in Nadaraya-Watson Interpolators](beyond_benign_overfitting_in_nadaraya-watson_interpolators.md)**

:   通过调节 Nadaraya-Watson 插值器中的单一带宽参数 $\beta$，精确刻画了从灾难性过拟合（$\beta < d$）→ 良性过拟合（$\beta = d$）→ 温和过拟合（$\beta > d$）的完整相变谱，证明高估数据内禀维度比低估更安全。

**[Brain-Like Processing Pathways Form in Models With Heterogeneous Experts](brain-like_processing_pathways_form_in_models_with_heterogeneous_experts.md)**

:   在异构 Mixture-of-Experts 模型中，异构专家并不会自动形成处理通路；本文提出三个受大脑启发的归纳偏置（路由代价、任务表现缩放、专家 Dropout），使模型形成类似大脑"皮层-皮层下"动态通路的 Mixture-of-Pathways 架构。

**[CLIMB: Class-Imbalanced Learning Benchmark on Tabular Data](climb_class-imbalanced_learning_benchmark_on_tabular_data.md)**

:   提出 Climb——迄今最全面的表格数据类别不平衡学习基准，涵盖 73 个真实数据集和 29 种 CIL 算法，通过大规模实验揭示了朴素重平衡往往无效、集成方法至关重要、数据质量比不平衡本身更影响性能等实用洞察。

**[Computable Universal Online Learning](computable_universal_online_learning.md)**

:   在 universal online learning 框架中引入可计算性约束，证明了"数学上可学习"不等于"可用计算机程序实现的可学习"，并给出了 agnostic 和 proper 变体下可计算学习的精确刻画。

**[Conformal Online Learning Of Deep Koopman Linear Embeddings](conformal_online_learning_of_deep_koopman_linear_embeddings.md)**

:   提出 COLoKe 框架，将 conformal prediction 重新解读为模型一致性诊断工具，仅在 Koopman 模型的预测误差超过动态校准阈值时才触发参数更新，从而实现对非线性动力系统的高效在线 Koopman 线性嵌入学习。

**[Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization](conformal_prediction_in_the_loop_a_feedback-based_uncertainty_model_for_trajecto.md)**

:   提出 Feedback-Based Conformal Prediction (Fb-CP) 框架，将已执行轨迹的信息反馈给 CP 以动态调整预测区域大小，在缩减时域轨迹优化中同时保证覆盖率和显著提升轨迹性能。

**[Contextual Dynamic Pricing with Heterogeneous Buyers](contextual_dynamic_pricing_with_heterogeneous_buyers.md)**

:   首次系统研究买家类型异质（$K_\star$ 种未知类型）的上下文动态定价问题，提出基于乐观后验采样 (OPS) 的算法实现 $\tilde{O}(K_\star\sqrt{dT})$ 遗憾界（对 $d$ 和 $T$ 最优），并在非上下文情形通过方差感知自适应离散化算法 ZoomV 实现 $\tilde{O}(\sqrt{K_\star T})$ 最优遗憾。

**[Continuous Thought Machines](continuous_thought_machines.md)**

:   提出 Continuous Thought Machine (CTM)，通过私有参数化的 Neuron-Level Models (NLMs) 产生神经元级时间动力学，并以神经同步矩阵作为核心潜在表征，在迷宫求解、ImageNet 分类、奇偶校验等任务上展现复杂推理、自适应计算和可解释注意力行为。

**[Coreset for Robust Geometric Median: Eliminating Size Dependency on Outliers](coreset_for_robust_geometric_median_eliminating_size_dependency_on_outliers.md)**

:   首次消除鲁棒几何中位数 coreset 大小对异常值数 $m$ 的依赖：在 $n \geq 4m$ 条件下，$d=1$ 时实现最优 coreset 大小 $\tilde{\Theta}(\varepsilon^{-1/2} + \frac{m}{n}\varepsilon^{-1})$，高维时实现 $\tilde{O}(\varepsilon^{-2}\min\{\varepsilon^{-2}, d\})$，核心技术是新颖的**非逐分量误差分析**。

**[Coresets for Clustering Under Stochastic Noise](coresets_for_clustering_under_stochastic_noise.md)**

:   首次系统研究噪声数据下 $(k,z)$-聚类 coreset 构造问题，提出新的代理误差度量 $\mathsf{Err}_\alpha$ 替代传统 $\mathsf{Err}$，在温和数据假设下实现 coreset 大小缩减 $\text{poly}(k)$ 倍、质量保证收紧 $\text{poly}(k)$ 倍，并设计噪声感知的 cluster-wise 采样算法。

**[Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning](cost-sensitive_freeze-thaw_bayesian_optimization_for_efficient_hyperparameter_tu.md)**

:   CFBO 将用户定义的效用函数（成本 vs 性能的权衡）引入冻结-解冻贝叶斯优化框架，结合自适应停止准则和基于 LC mixup 的迁移学习，在多保真度 HPO 基准上实现了成本-性能最优权衡。

**[Deep Continuous-Time State-Space Models for Marked Event Sequences](deep_continuous-time_state-space_models_for_marked_event_sequences.md)**

:   S2P2 将线性 Hawkes 过程与深度状态空间模型结合，通过堆叠多层隐式线性 Hawkes (LLH) 层 + 非线性激活构建高表达力的连续时间 MTPP 模型，利用并行扫描实现线性复杂度和亚线性时间，在 8 个真实数据集上平均提升 33% 预测似然。

**[Deep Legendre Transform](deep_legendre_transform.md)**

:   DLT 利用凸共轭的隐式 Fenchel 表示 $f^*(\nabla f(x)) = \langle x, \nabla f(x) \rangle - f(x)$ 将凸共轭计算转化为标准回归问题，避免求解 max/min-max 优化，且能提供后验误差估计，结合 KAN 还可获得精确解析解。

**[Depth-Bounds for Neural Networks via the Braid Arrangement](depth-bounds_for_neural_networks_via_the_braid_arrangement.md)**

:   本文证明了在 $\mathcal{B}_d^0$-conforming 约束下，ReLU 网络精确表示 $\max\{0, x_1, \ldots, x_d\}$ 需要 $\Omega(\log \log d)$ 层——这是首个不限制权重的非常数深度下界；同时证明 rank-(3,2) maxout 网络可以计算 7 个数的最大值，说明标准上界不紧。

**[Depth-Supervised Fusion Network for Seamless-Free Image Stitching](depth-supervised_fusion_network_for_seamless-free_image_stitching.md)**

:   DSFN 提出深度一致性约束的无缝图像拼接方法：通过深度感知的两阶段变换估计解决大视差对齐，软缝合区域扩散实现自然融合，结合重参数化策略提升效率，在 UDIS-D 和 IVSD 数据集上全面超越 SOTA。

**[Directional Non-Commutative Monoidal Structures for Compositional Embeddings in Machine Learning](directional_non-commutative_monoidal_structures_for_compositional_embeddings_in_.md)**

:   提出一种基于方向性非交换幺半群算子的代数框架，为多维组合嵌入提供统一数学基础，将 SSM 递归、Transformer 自注意力和 RoPE 位置编码统一为特例。

**[Distributional Autoencoders Know the Score](distributional_autoencoders_know_the_score.md)**

:   本文为 Distributional Principal Autoencoder (DPA) 提供了精确的理论保证：证明了最优编码器的等值面几何与数据分布的 score 函数之间的闭合形式关系，并证明了超出流形维度的潜在分量与数据条件独立，从而统一了分布学习与内在维度发现两个长期目标。

**[Distributionally Robust Feature Selection](distributionally_robust_feature_selection.md)**

:   本文提出一种模型无关的分布鲁棒特征选择方法，通过向协变量注入可控高斯噪声实现离散选择的连续松弛，并优化 Bayes 最优预测器的条件方差，使选出的特征子集能在多个子群体上同时训练出高质量下游模型。

**[Double Descent Meets Out-of-Distribution Detection: Theoretical Insights and Empirical Analysis](double_descent_meets_out-of-distribution_detection_theoretical_insights_and_empi.md)**

:   本文首次揭示 post-hoc OOD 检测中存在 double descent 现象——OOD 检测性能随模型宽度在插值阈值附近出现谷值后再次上升，通过随机矩阵理论提供理论解释，并提出基于 Neural Collapse 的 NC1 判据来识别最佳模型复杂度区间。

**[DPA: A One-Stop Metric to Measure Bias Amplification in Classification Datasets](dpa_a_one-stop_metric_to_measure_bias_amplification_in_classification_datasets.md)**

:   本文提出 Directional Predictability Amplification (DPA)，一种基于可预测性的偏差放大度量指标，是唯一同时满足方向性、适用于平衡/非平衡数据集、能正确识别正负偏差放大的一站式指标，通过测量模型偏差与数据集偏差的相对变化来量化偏差放大程度。

**[Dynamic Algorithm for Explainable k-medians Clustering under lp Norm](dynamic_algorithm_for_explainable_k-medians_clustering_under_lp_norm.md)**

:   本文提出首个适用于一般 $\ell_p$ 范数的可解释 k-medians 聚类算法，实现 $\tilde{O}(p(\log k)^{1+1/p-1/p^2})$ 近似比（改进了 p=2 的已知最优界），并给出首个动态版本：在中心集合的插入/删除下，以 $O(d \log^3 k)$ 摊还更新时间和 $O(\log k)$ 重分配次数维护可解释聚类。

**[Efficient Parametric SVD of Koopman Operator for Stochastic Dynamical Systems](efficient_parametric_svd_of_koopman_operator_for_stochastic_dynamical_systems.md)**

:   提出基于 low-rank approximation (LoRA) 的目标函数来学习随机动力系统 Koopman 算子的 top-k 奇异函数，完全避免了 VAMPnet/DPNet 中数值不稳定的矩阵分解操作，且梯度天然无偏。

**[Emergency Response Measures for Catastrophic AI Risk](emergency_response_measures_for_catastrophic_ai_risk.md)**

:   本文分析了如何将前沿安全政策（Frontier Safety Policies, FSPs）模型整合到中国四阶段应急响应框架中，以应对来自先进AI系统的灾难性风险（如大规模杀伤性武器扩散、失控事件等）。

**[Empowering Decision Trees via Shape Function Branching](empowering_decision_trees_via_shape_function_branching.md)**

:   提出 Shape Generalized Tree (SGT)，在决策树每个内部节点使用可学习的轴对齐形状函数替代传统线性阈值分裂，以更紧凑的树结构捕捉非线性特征效应，同时保持可解释性。

**[Enhancing Sample Selection Against Label Noise by Cutting Mislabeled Easy Examples](enhancing_sample_selection_against_label_noise_by_cutting_mislabeled_easy_exampl.md)**

:   发现并定义了误标注易学样本（Mislabeled Easy Examples, MEEs）——被模型早期训练即正确预测为错误标签的样本对泛化伤害最大，并提出 Early Cutting 方法利用模型后期状态重新校准早期置信子集来过滤MEEs。

**[Equivariance by Contrast: Identifiable Equivariant Embeddings from Unlabeled Finite Group Actions](equivariance_by_contrast_identifiable_equivariant_embeddings_from_unlabeled_fini.md)**

:   提出 Equivariance by Contrast (EbC)，一种仅用编码器的方法，从观测对 $(\mathbf{y}, g \cdot \mathbf{y})$ 中联合学习等变嵌入空间和隐式群表示，使有限群作用在潜空间中对应可逆线性映射，并提供可辨识性理论保证。

**[Evaluating In Silico Creativity: An Expert Review of AI Chess Compositions](evaluating_in_silico_creativity_an_expert_review_of_ai_chess_compositions.md)**

:   使用生成式神经网络（自回归Transformer、离散扩散、MaskGit）+强化学习生成国际象棋谜题，通过奖励函数筛选具有唯一解和反直觉性的谜题，并邀请三位世界级国际象棋专家评审AI生成谜题的创造力和美学品质。

**[EvoBrain: Dynamic Multi-Channel EEG Graph Modeling for Time-Evolving Brain Networks](evobrain_dynamic_multi-channel_eeg_graph_modeling_for_time-evolving_brain_networ.md)**

:   提出 EvoBrain——首次从理论上证明 **显式动态图建模** 优于隐式静态图、**time-then-graph** 架构表达力严格优于其他两种动态 GNN 范式(graph-then-time / time-and-graph)，并据此设计双流 Mamba + Laplacian PE 增强的 GCN 模型，在 TUSZ 和 CHB-MIT 数据集的癫痫检测与早期预测任务上取得 AUROC 提升 23%、F1 提升 30% 的显著效果，同时训练速度比 SOTA 快 17 倍。

**[Evolutionary Prediction Games](evolutionary_prediction_games.md)**

:   提出"演化预测博弈"框架，用演化博弈论分析预测算法与用户群体之间的反馈循环，揭示理想学习器导致竞争排斥（强者生存），而实际学习器（有限数据/代理损失/过参数化）反而能促成群体间的稳定共存与互利共生。

**[Exact Learning of Arithmetic with Differentiable Agents](exact_learning_of_arithmetic_with_differentiable_agents.md)**

:   提出可微有限状态转换器（DFST），一种图灵完备且端到端可微的模型族，在 2D 符号网格上通过观察专家算术计算的中间步骤（Policy-Trajectory Observations）训练，仅用 20 个样本（最长 3 位数加法）即可完美泛化到 3850 位二进制加法、2450 位十进制加法，未发现任何错误。

**[Exploiting Task Relationships in Continual Learning via Transferability-Aware Task Embeddings](exploiting_task_relationships_in_continual_learning_via_transferability-aware_ta.md)**

:   提出基于 H-score 可迁移性度量的任务嵌入（H-embedding），并将其嵌入超网络框架，通过在嵌入空间中显式建模任务间关系来指导持续学习中的参数生成，在 rehearsal-free 设定下取得 SOTA 最终准确率。

**[Faithful Group Shapley Value](faithful_group_shapley_value.md)**

:   提出 Faithful Group Shapley Value (FGSV)，唯一满足含"忠实性"在内五条公理的组级数据估值方法，有效防御"空壳公司攻击"（通过拆分子组不当膨胀估值），并设计了 $O(n \cdot \text{Poly}(\log n))$ 复杂度的高效近似算法。

**[Final-Model-Only Data Attribution with a Unifying View of Gradient-Based Methods](final-model-only_data_attribution_with_a_unifying_view_of_gradient-based_methods.md)**

:   明确提出"仅有最终模型"(FiMO)的训练数据归因设定，将问题从"贡献度"重构为"敏感性"度量，提出 further training 作为金标准，并统一推导出多种梯度方法（Grad-Dot、影响函数、TRAK、DataInf 等）均为 further training 的不同阶近似。

**[Finding Structure In Continual Learning](finding_structure_in_continual_learning.md)**

:   提出基于Douglas-Rachford Splitting (DRS)的持续学习优化框架，将稳定性与可塑性解耦为两个独立的近端子问题，并结合Rényi散度替代KL散度实现更鲁棒的先验对齐，从而在无需回放缓冲区或额外模块的条件下有效缓解灾难性遗忘。

**[FlashMD: Long-Stride, Universal Prediction of Molecular Dynamics](flashmd_long-stride_universal_prediction_of_molecular_dynamics.md)**

:   提出 FlashMD，基于 GNN 直接预测分子动力学轨迹的位置与动量跨步演化，实现比传统 MD 积分器大 1–2 个数量级的时间步长跨越，并在架构中融入哈密顿动力学约束，推广到任意热力学系综和通用化学体系。

**[Flatness is Necessary, Neural Collapse is Not: Rethinking Generalization via Grokking](flatness_is_necessary_neural_collapse_is_not_rethinking_generalization_via_grokk.md)**

:   利用 grokking（延迟泛化）作为因果探针，证明 **relative flatness 是泛化的（潜在）必要条件**，而 neural collapse 虽常伴随泛化出现，但并非必要——它只是通往 flatness 的一条路径。

**[FlowMoE: 分布式MoE训练的可扩展流水线调度框架](flowmoe_a_scalable_pipeline_scheduling_framework_for_distributed_mixture-of-expe.md)**

:   通过统一的流水线调度和优先级驱动的all-reduce张量分块，实现MHA、门控、专家计算和A2A/all-reduce通信的完全重叠，训练时间减少13-57%。

**[Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards](fostering_the_ecosystem_of_ai_for_social_impact_requires_expanding_and_strengthe.md)**

:   本文主张 AI for Social Impact (AISI) 领域的学术生态需要双轨改革：拓宽"影响力"的定义以认可非部署/非方法创新的贡献，同时对已部署系统采用因果推断级别的严格评估标准。

**[FSNet: Feasibility-Seeking Neural Network for Constrained Optimization with Guarantees](fsnet_feasibility-seeking_neural_network_for_constrained_optimization_with_guara.md)**

:   提出 FSNet 框架，将**可微的可行性求解步骤**集成到神经网络中，通过最小化约束违反的无约束优化来保证约束满足，同时支持端到端训练，在凸/非凸、光滑/非光滑问题上均显著快于传统求解器且保持可行性。

**[Gaussian Process Upper Confidence Bound Achieves Nearly-Optimal Regret in Noise-Free Gaussian Process Bandits](gaussian_process_upper_confidence_bound_achieves_nearly-optimal_regret_in_noise-.md)**

:   本文证明 GP-UCB 在 noise-free GP bandit 问题中可达到 nearly-optimal regret，首次在 SE 核下实现 $O(1)$ 常数累积遗憾、在 Matérn 核（$d < \nu$）下实现 $O(1)$ 累积遗憾，弥合了 GP-UCB 理论与实践之间的长期差距。

**[Generalized Linear Mode Connectivity for Transformers](generalized_linear_mode_connectivity_for_transformers.md)**

:   提出统一对称性框架（置换、半置换、正交、可逆变换四级层次），首次在 Vision Transformer 和 GPT-2 上实现零/近零 barrier 的线性模式连通性（LMC），并扩展至多模型融合与异构宽度对齐。

**[Geometric Priors for Generalizable World Models via Vector Symbolic Architecture](geometric_priors_for_generalizable_world_models_via_vector_symbolic_architecture.md)**

:   提出将 Vector Symbolic Architecture (VSA) 中的 Fourier Holographic Reduced Representation (FHRR) 作为几何先验引入世界模型，通过 element-wise 复数乘法建模状态转移，在离散 GridWorld 上实现 87.5% 的 zero-shot 泛化准确率和 4 倍于 MLP 的噪声鲁棒性。

**[Gradient-Weight Alignment as a Train-Time Proxy for Generalization in Classification Tasks](gradient-weight_alignment_as_a_train-time_proxy_for_generalization_in_classifica.md)**

:   提出 Gradient-Weight Alignment (GWA)，通过量化每个训练样本梯度与模型权重的方向一致性（cosine similarity），在训练过程中无需验证集即可准确预测泛化性能、确定最佳早停时机，并定位有影响力的训练样本。

**[Graph Alignment via Birkhoff Relaxation](graph_alignment_via_birkhoff_relaxation.md)**

:   本文首次为图对齐问题的 Birkhoff 松弛（将排列矩阵约束松弛为双随机矩阵约束）提供了理论保证，在高斯 Wigner 模型下证明了最优解的相变行为：当噪声 $\sigma = o(n^{-1})$ 时松弛解接近真实排列，当 $\sigma = \Omega(n^{-0.5})$ 时松弛解远离真实排列。

**[Harnessing Feature Resonance under Arbitrary Target Alignment for Out-of-Distribution Node Detection](harnessing_feature_resonance_under_arbitrary_target_alignment_for_out-of-distrib.md)**

:   发现 Feature Resonance 现象——优化已知 ID 节点表征时未知 ID 节点的表征变化显著大于 OOD 节点，且该现象与标签无关，据此提出无需多类标签的图 OOD 节点检测框架 RSL，在 13 个数据集上达到 SOTA。

**[Improving Forecasts of Suicide Attempts for Patients with Little Data](improving_forecasts_of_suicide_attempts_for_patients_with_little_data.md)**

:   提出 Latent Similarity Gaussian Process (LSGP)，将患者嵌入连续隐空间以捕获异质性，使数据稀少的患者能从相似患者"借用"预测趋势，从而改进基于 EMA 数据的自杀未遂预测。

**[笔记2：PRM必要吗？RL隐式诱导PRM能力](is_prm_necessary_problem-solving_rl_implicitly_induces_prm_capability_in_llms.md)**

:   令人惊讶地，纯RL训练无需显式PRM监督即可诱发出强大的过程理解能力，且现有PRMs在SOTA模型上甚至不如简单多数投票有效。

**[Learning Dynamics of RNNs in Closed-Loop Environments](learning_dynamics_of_rnns_in_closed-loop_environments.md)**

:   从数学理论上揭示了 RNN 在闭环（agent-环境交互）与开环（监督学习）训练下呈现根本不同的学习动力学，闭环学习遵循三阶段过程，由短期策略改进与长期稳定性之间的竞争驱动。

**[Learning Generalizable Shape Completion with SIM(3) Equivariance](learning_generalizable_shape_completion_with_sim3_equivariance.md)**

:   提出首个 SIM(3) 等变形状补全网络 SIMECO，通过特征规范化→相似不变几何推理→变换恢复的三阶段模块设计，在去偏评估协议下超越所有增广和等变基线，KITTI 上 MMD 降低 17%、OmniObject3D 上 CD-$\ell_1$ 降低 14%，且在更严格协议下仍优于竞争者在其偏向性设置下的表现。

**[Learning non-equilibrium diffusions with Schrödinger bridges: from exactly solvable to simulation-free](learning_non-equilibrium_diffusions_with_schrödinger_bridges_from_exactly_solvab.md)**

:   将Schrödinger桥问题从布朗运动参考过程推广到多变量Ornstein-Uhlenbeck（mvOU）参考过程，推导高斯情形精确解，并提出无模拟的mvOU-OTFM算法处理一般分布。

**[Look-Ahead Reasoning on Learning Platforms](look-ahead_reasoning_on_learning_platforms.md)**

:   在学习平台的用户-算法交互中形式化 level-$k$ 前瞻推理，证明个体自私的高阶推理只加速收敛但不改变均衡（无长期收益），而集体协调的收益由学习者-用户效用函数的对齐程度决定，提供了刻画协调收益上界的理论框架。

**[MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision](maszero_designing_multiagent_systems_with_zero_supervision.md)**

:   MAS-ZERO 是首个推理时自动 MAS 设计框架，通过 meta-agent 迭代设计、批评和改进 MAS 配置（包括任务分解和 sub-MAS 分配），无需验证集和训练，在推理（+16.69%）、编程（+16.66%）和搜索代理（+5.45%）任务上均超越手动和自动 MAS baseline，同时保持 Pareto 最优的准确率-成本权衡。

**[MoESD: 揭示稀疏MoE推理中投机解码的潜力](moesd_unveil_speculative_decodings_potential_for_accelerating_sparse_moe.md)**

:   揭示投机解码在中等批大小下对MoE比对稠密模型更有效，通过目标效率指标捕捉系统级瓶颈，建立可靠的性能建模，达到2.29×加速。

**[Neural Collapse under Gradient Flow on Shallow ReLU Networks for Orthogonally Separable Data](neural_collapse_under_gradient_flow_on_shallow_relu_networks_for_orthogonally_se.md)**

:   首次证明在正交可分数据上，两层ReLU网络的梯度流（GF）在小初始化下可证收敛到Neural Collapse（NC）解，揭示了GF隐式偏置（早期神经元对齐+渐近最大间隔偏置）在促进NC出现中的关键作用。

**[On the Surprising Effectiveness of Large Learning Rates under Standard Width Scaling](on_the_surprising_effectiveness_of_large_learning_rates_under_standard_width_sca.md)**

:   揭示在标准参数化(SP)下，cross-entropy 损失函数使得"不稳定"区间实际分为灾难性不稳定和受控发散两个子区间：在受控发散区间（学习率 $\eta_n = \Theta(n^{-1/2})$）logits 发散但梯度和激活保持稳定，从而首次为 SP 提供了一个实用的、具有特征学习能力的无穷宽极限。

**[OrbitZoo: Real Orbital Systems Challenges for RL](orbitzoo_real_orbital_systems_challenges_for_reinforcement_learning.md)**

:   构建OrbitZoo，基于工业标准库Orekit的多智能体RL环境，支持碰撞规避和协同机动，经Starlink真实数据验证MAPE仅0.16%。

**[OrthoLoC: UAV 6-DoF Localization Using Orthographic Geodata](ortholoc_uav_6-dof_localization_and_calibration_using_orthographic_geodata.md)**

:   提出OrthoLoC——首个大规模UAV-正射影像配对数据集（16,425张，47地点，19城市），用于6-DoF定位和标定评估，AdHoP技术匹配精度提升95%、平移误差降低63%。

**[笔记7：价值引导搜索 - 高效链式思考推理](polymath_evaluating_mathematical_reasoning_in_multilingual_contexts.md)**

:   提出Value-Guided Search(VGS)——通过token级价值模型指导块级束搜索，无需预定义"步骤"，相对多数投票在竞赛数学上准确度提升+14.5%，同时推理计算效率提升30%，超越现有PRM方案。

**[笔记5：ReSearch - 学习通过搜索推理](research_learning_to_reason_with_search_for_llms_via_reinforcement_learning.md)**

:   ReSearch框架将搜索操作嵌入推理链中作为第一类原语，通过GRPO强化学习自动学习何时何如搜索，无需任何推理步骤的监督标注，在多跳QA任务上相对基线平均提升15.81%。

**[Sample-Adaptivity Tradeoff in On-Demand Sampling](sample-adaptivity_tradeoff_in_on-demand_sampling.md)**

:   系统研究了按需采样（on-demand sampling）中样本复杂度与自适应轮次之间的权衡关系，在可实现设定下证明 $r$ 轮算法的最优样本复杂度为 $dk^{\Theta(1/r)}/\varepsilon$，在不可知设定下提出仅需 $\widetilde{O}(\sqrt{k})$ 轮即可达近最优样本复杂度的LazyHedge算法，并引入OODS抽象框架建立了近紧的轮次复杂度下界。

**[Transfer Learning for Benign Overfitting in High-Dimensional Linear Regression](transfer_learning_for_benign_overfitting_in_high-dimensional_linear_regression.md)**

:   提出两步式Transfer MNI方法，在高维过参数化线性回归中通过"保留目标信号+零空间迁移源知识"机制增强良性过拟合的泛化能力，刻画了模型偏移和协变量偏移下的非渐近excess risk，并发现了"免费午餐"协变量偏移区间。

**[笔记4：WebThinker - 赋予推理模型深度研究能力](webthinker_empowering_large_reasoning_models_with_deep_research_capability.md)**

:   WebThinker赋予大型推理模型(LRM)自主的网络搜索与导航能力，通过Think-Search-Draft策略实现推理、信息采集与报告生成的无缝交织，经RL优化后在复杂推理与科学报告生成任务上超越o1与Gemini。
