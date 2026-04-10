<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**🧪 ICML2025** · 共 **140** 篇

**[A Square Peg in a Square Hole: Meta-Expert for Long-Tailed Semi-Supervised Learning](a_square_peg_in_a_square_hole_meta-expert_for_long-tailed_semi-supervised_learni.md)**

:   提出 Meta-Expert 算法，通过动态专家分配（DEA）模块根据样本的类别归属（头/中/尾）自动选择最擅长的专家生成伪标签，并利用多深度特征融合（MFF）模块缓解模型对头类的偏向，实现"方枘方凿"——让每个专家处理它最擅长的样本区间。

**[Ab Initio Nonparametric Variable Selection for Scalable Symbolic Regression with Large p](ab_initio_nonparametric_variable_selection_for_scalable_symbolic_regression_with.md)**

:   提出 PAN+SR 框架，通过基于 BART 的非参数变量预筛选，将高维符号回归问题降维至低维子空间，使 19 种现有 SR 方法在高维场景下均获显著性能提升。

**[Adversarial Combinatorial Semi-bandits with Graph Feedback](adversarial_combinatorial_semi-bandits_with_graph_feedback.md)**

:   本文将图反馈（graph feedback）引入对抗组合半臂赌博机（combinatorial semi-bandits）框架，提出 OSMD-G 算法，建立了最优遗憾（regret）界 $\widetilde{\Theta}(S\sqrt{T} + \sqrt{\alpha S T})$，其中 $S$ 是组合决策大小，$\alpha$ 是反馈图的独立数，关键技术在于利用随机化轮换舍入（randomized swap rounding）实现负相关采样。

**[Algebra Unveils Deep Learning -- An Invitation to Neuroalgebraic Geometry](algebra_unveils_deep_learning_--_an_invitation_to_neuroalgebraic_geometry.md)**

:   本文提出 **neuroalgebraic geometry（神经代数几何）** 这一新研究方向，系统地利用代数几何的工具（维度、度、奇异点、纤维、临界点理论等）来分析深度学习模型参数化的函数空间（neuromanifold），建立起代数几何不变量与机器学习核心问题（样本复杂度、表达能力、训练动力学、隐式偏差）之间的对应字典。

**[AutoAL: Automated Active Learning with Differentiable Query Strategy Search](autoal_automated_active_learning_with_differentiable_query_strategy_search.md)**

:   提出首个可微的主动学习策略搜索框架 AutoAL，通过 SearchNet 和 FitNet 两个网络在双层优化框架下协同训练，自动从多个候选 AL 策略中为给定任务选出最优策略，在自然图像和医学图像数据集上一致超越所有候选策略及其他 SOTA 方法。

**[Avoiding Catastrophe in Online Learning by Asking for Help](avoiding_catastrophe_in_online_learning_by_asking_for_help.md)**

:   提出一种避免灾难性错误的在线学习模型：将每轮回报定义为"该轮避免灾难的概率"，最大化回报之积（总体避灾概率），允许有限次数向导师求助，证明在可学习策略类下后悔和求助率都趋零。

**[Avoiding Leakage Poisoning: Concept Interventions Under Distribution Shifts](avoiding_leakage_poisoning_concept_interventions_under_distribution_shifts.md)**

:   揭示概念模型（CBM）中的"泄漏中毒"现象——绕过概念瓶颈的信息泄漏在分布偏移下反而损害预测准确率，使概念干预失效，提出 MixCEM 通过置信度门控动态决定何时使用/丢弃泄漏信息，在分布内外均保持高准确率和有效干预。

**[BECAME: BayEsian Continual Learning with Adaptive Model MErging](became_bayesian_continual_learning_with_adaptive_model_merging.md)**

:   提出 BECAME——基于贝叶斯持续学习原则重新建模模型融合机制，利用 Laplace 近似推导出最优融合系数的闭式解，结合梯度投影（稳定性）和无约束训练（可塑性）的两阶段框架，在多个持续学习基准上显著超越 SOTA。

**[Beyond Entropy: Region Confidence Proxy for Wild Test-Time Adaptation](beyond_entropy_region_confidence_proxy_for_wild_test-time_adaptation.md)**

:   揭示熵最小化在野外测试时适应（WTTA）中的根本局限——局部区域内语义相似样本的预测不一致导致冲突优化动态，提出 ReCAP 框架用概率区域建模和有限到无穷渐近近似将不可处理的区域置信度转化为高效可优化的代理目标，在 ImageNet-C 上一致超越 SOTA。

**[Bipartite Ranking From Multiple Labels: On Loss Versus Label Aggregation](bipartite_ranking_from_multiple_labels_on_loss_versus_label_aggregation.md)**

:   本文从理论上分析了多标签二部排序（bipartite ranking）中两种聚合策略——损失聚合（loss aggregation）与标签聚合（label aggregation）——的Bayes最优解，揭示了损失聚合会产生"标签独裁"（label dictatorship）现象（某一标签因边际偏斜度而主导排序），而标签聚合能更均衡地对待所有标签。

**[Concept-Based Unsupervised Domain Adaptation](concept-based_unsupervised_domain_adaptation.md)**

:   提出 CUDA 框架——将概念瓶颈模型（CBM）与无监督域适应（UDA）结合，通过松弛一致性对齐概念表示（允许域间小差异）和目标域的无标注概念推断，首次在域偏移下同时提供可解释性和跨域泛化，并提供理论保证。

**[Conformal Prediction as Bayesian Quadrature](conformal_prediction_as_bayesian_quadrature.md)**

:   从贝叶斯视角重新审视共形预测——证明分裂共形预测和共形风险控制都是贝叶斯求积（Bayesian Quadrature）框架的特例，提出实用的贝叶斯替代方案，提供可解释的保证和对未来损失范围的更丰富表示。

**[Constrained Hamiltonian Systems on Observation-Induced Fiber Bundles: Theory of Symmetry and Integrability](constrained_hamiltonian_systems_on_observation-induced_fiber_bundles_theory_of_s.md)**

:   提出"观测诱导纤维丛"几何框架，将部分可观测系统中的观测不确定性从外部扰动内化为纤维坐标的内禀变化，在此结构上统一处理状态约束与观测约束，建立了完整的辛几何、可积性、对称性与守恒律理论。

**[Continuous-Time Analysis of Heavy Ball Momentum in Min-Max Games](continuous-time_analysis_of_heavy_ball_momentum_in_min-max_games.md)**

:   通过连续时间ODE建模，系统揭示了Heavy Ball动量在min-max博弈中与极小化问题截然不同的行为：**更小的动量**（包括负动量）能扩大收敛步长范围并引导轨迹走向更浅梯度区域，而**交替更新**比同步更新收敛更快且放大了这一正则化效应。

**[Cooperation of Experts: Fusing Heterogeneous Information with Large Margin](cooperation_of_experts_fusing_heterogeneous_information_with_large_margin.md)**

:   提出 Cooperation of Experts (CoE) 框架，将异构信息编码为多重网络，通过两级专家设计与大间隔置信张量优化实现专家**协作**（而非竞争），在节点分类任务上全面超越现有 MoE 和多重网络方法。

**[Counting in Small Transformers: The Delicate Interplay between Attention and Feed-Forward Layers](counting_in_small_transformers_the_delicate_interplay_between_attention_and_feed.md)**

:   通过直方图计数任务，揭示了小型Transformer中注意力层与前馈层之间的精细分工：注意力擅长关系比较（relation-based counting），前馈层负责字典记忆（inventory-based counting），两种策略的出现由嵌入维度 $d$、隐层大小 $p$ 和词表大小 $T$ 的相对关系决定。

**[Cover Learning for Large-Scale Topology Representation](cover_learning_for_large-scale_topology_representation.md)**

:   提出将"覆盖学习"作为独立优化问题：学习几何数据集的拓扑忠实覆盖，由此构建的单纯复形在大小上优于标准拓扑推断方法，在大尺度拓扑表示上优于Mapper类算法。

**[Cross-regularization: Adaptive Model Complexity through Validation Gradients](cross-regularization_adaptive_model_complexity_through_validation_gradients.md)**

:   提出 Cross-regularization（交叉正则化），通过验证集梯度直接优化正则化参数（权重范数、噪声尺度、增强强度），在单次训练中收敛到交叉验证最优解，消除手动调参需求。

**[Cut out and Replay: A Simple yet Versatile Strategy for Multi-Label Online Continual Learning](cut_out_and_replay_a_simple_yet_versatile_strategy_for_multi-label_online_contin.md)**

:   提出 CUTER（CUT-out-and-Experience-Replay），通过裁剪图像中标签特定区域并存入记忆缓冲区进行回放，将多标签在线持续学习转化为多个单标签子图像分类任务，同时解决灾难性遗忘、缺失标签和类别不平衡三大挑战。

**[Decision Making under the Exponential Family DRO](decision_making_under_the_exponential_family_distributionally_robust_optimisatio.md)**

:   研究基于指数族分布的分布鲁棒优化（DRO）框架，利用指数族分布的自然参数空间构建不确定集，分析最优决策的性质和计算方法，在多种决策场景（如投资组合优化、风险管理）中展示优势。

**[Democratic AI is Possible. The Democracy Levels Framework Shows How It Might Work](democratic_ai_is_possible_the_democracy_levels_framework_shows_how_it_might_work.md)**

:   提出"Democracy Levels"（民主等级）框架，将 AI 决策权从单方面权威向民主系统的转移划分为 L0–L5 六个等级，并配套维度评估体系和实操工具，为 AI 治理的民主化提供了系统性路线图。

**[Density Ratio Estimation-Based Bayesian Optimization With Semi-Supervised Learni](density_ratio_estimation-based_bayesian_optimization_with_semi-supervised_learni.md)**

:   提出 DRE-BO-SSL，将半监督学习（标签传播/标签扩散）引入密度比估计型贝叶斯优化，通过无标签数据点缓解监督分类器的过度利用(over-exploitation)问题，在探索与利用之间取得更好平衡。

**[DiLQR: Differentiable Iterative LQR via Implicit Differentiation](dilqr_differentiable_iterative_linear_quadratic_regulator_via_implicit_different.md)**

:   提出DiLQR——通过隐式微分在iLQR控制器的不动点处计算梯度，使反向传播成本恒定(不随迭代次数增加)，实现128倍加速和10^6倍学习性能提升。

**[Discrepancy Minimization in Input-Sparsity Time](discrepancy_minimization_in_input-sparsity_time.md)**

:   提出首个实值矩阵差异最小化的输入稀疏时间算法，组合版 $\widetilde{O}(\mathrm{nnz}(A)+n^3)$、快速矩阵乘法版 $\widetilde{O}(\mathrm{nnz}(A)+n^{2.53})$，逼近 herdisc 的对数因子保证不变，几乎弥合了实值矩阵与二值矩阵之间的计算鸿沟。

**[Discrete Neural Algorithmic Reasoning](discrete_neural_algorithmic_reasoning.md)**

:   提出离散神经算法推理器(DNAR)，通过特征离散化、硬注意力和连续/离散数据流分离三大组件，迫使神经网络沿有限预定义状态执行算法轨迹，在 BFS/DFS/Dijkstra/Prim/MIS 等任务上实现**100%完美测试得分**，并可形式化证明所学算法的正确性。

**[Diverse Prototypical Ensembles Improve Robustness To Subpopulation Shift](diverse_prototypical_ensembles_improve_robustness_to_subpopulation_shift.md)**

:   提出 Diversified Prototypical Ensemble (DPE)，用多个多样化的原型分类器替换标准线性分类头，通过显式（inter-prototype similarity loss）和隐式（bootstrap 采样）两种多样化策略，在不需要子群标注的情况下自适应发现子群决策边界，显著提升 worst-group accuracy。

**[Diversity by Design: Leveraging Distribution Matching for Offline Model-Based Optimization](diversity_by_design_leveraging_distribution_matching_for_offline_model-based_opt.md)**

:   DynAMO 在离线模型优化 (MBO) 中将设计多样性建模为分布匹配问题，通过对抗训练使生成设计的分布捕捉离线数据集中的固有多样性，在多个科学领域显著提升候选方案的多样性而不牺牲质量。

**[DSP: Dynamic Sequence Parallelism for Multi-Dimensional Transformers](dsp_dynamic_sequence_parallelism_for_multi-dimensional_transformers.md)**

:   针对多维 Transformer（如视频生成中的时空注意力模型）中现有序列并行方法只能沿单一维度分片导致大量冗余通信的问题，提出 Dynamic Sequence Parallelism (DSP)，通过在计算阶段之间动态切换并行维度（而非在模块内部通信），利用高效 all-to-all 操作实现 resharding，端到端吞吐提升 32.2%~10×，通信量减少至少 50%。

**[Efficient Network Automatic Relevance Determination](efficient_network_automatic_relevance_determination.md)**

:   将自动相关性确定（ARD）从单输出扩展到多输出回归场景，提出 NARD 框架联合估计稀疏回归系数和输出精度矩阵，并设计 Sequential/Surrogate/Hybrid 三种加速算法将复杂度从 $\mathcal{O}(d^3)$ 降至 $\mathcal{O}(p^2)$。

**[Efficient Optimization with Orthogonality Constraint: a Randomized Riemannian Submanifold Method](efficient_optimization_with_orthogonality_constraint_a_randomized_riemannian_sub.md)**

:   提出随机黎曼子流形下降方法 (RSDM)，通过将每步更新限制在随机低维子流形上，将正交约束优化中 retraction 操作的复杂度从 $O(np^2)$ 降至 $O(r^3)$，同时保持与全空间黎曼梯度下降相匹配的总计算复杂度。

**[Enhancing Certified Robustness via Block Reflector Orthogonal Layers and Logit Annealing Loss](enhancing_certified_robustness_via_block_reflector_orthogonal_layers_and_logit_a.md)**

:   本文提出了一种高效的低秩正交层参数化方法（BRO Layer）和一种退火机制的损失函数（Logit Annealing Loss），用于构建具有更强认证鲁棒性的 Lipschitz 神经网络 BRONet，在 CIFAR-10/100、Tiny-ImageNet 和 ImageNet 上达到 SOTA。

**[Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](evaluating_neuron_explanations_a_unified_framework_with_sanity_checks.md)**

:   提出 NeuronEval 统一框架，将 19 种现有神经元解释评估方法形式化为同一数学范式，并设计 Missing Labels / Extra Labels 两项合理性检验，揭示大多数常用指标（如 Recall、AUC、top-and-random 采样下的 Correlation）不可靠，仅 Correlation(Pearson)、Cosine、AUPRC、F1 和 IoU 通过测试。

**[Explaining, Fast and Slow: Abstraction and Refinement of Provable Explanations](explaining_fast_and_slow_abstraction_and_refinement_of_provable_explanations.md)**

:   本文提出了一种基于抽象-细化的方法来高效计算神经网络预测的可证明充分解释（provably sufficient explanations），通过将大网络抽象为小网络来加速验证过程，解释质量有形式化保证。

**[Exploiting Similarity for Computation and Communication-Efficient Decentralized Mean Estimation](exploiting_similarity_for_computation_and_communication-efficient_decentralized_.md)**

:   利用分布式节点间数据的相似性，设计计算和通信高效的去中心化均值估计算法，实现比忽略相似性的方法更好的估计精度-通信trade-off。

**[Faster and Stronger: When ANN-SNN Conversion Meets Parallel Spiking Calculation](faster_and_stronger_when_ann-snn_conversion_meets_parallel_spiking_calculation.md)**

:   首次将并行脉冲计算与 ANN-SNN 转换结合，建立数学等价映射关系，在超低时间步（4步）下实现 ImageNet Top-1 72.90%，推理速度加速 19~38 倍。

**[Feature Learning Beyond The Lazy-Rich Dichotomy Insights From Representational G](feature_learning_beyond_the_lazy-rich_dichotomy_insights_from_representational_g.md)**

:   提出用**流形容量 (manifold capacity)** 及其关联的几何度量 (GLUE) 来刻画特征学习的丰富程度，超越传统的 lazy vs rich 二分法，揭示了不同学习阶段、学习策略以及在神经科学和 OOD 泛化问题中的新洞察。

**[FEDTAIL: Federated Long-Tailed Domain Generalization with Sharpness-Guided Gradient Matching](fedtail_federated_long-tailed_domain_generalization_with_sharpness-guided_gradie.md)**

:   FedTAIL 提出了一个联邦域泛化框架，通过梯度一致性正则化、逐类锐度感知最小化和曲率感知动态加权三个模块，同时解决域偏移和长尾类别不平衡的双重挑战，在多个基准上达到 SOTA。

**[Feedforward Few-shot Species Range Estimation](feedforward_few-shot_species_range_estimation.md)**

:   提出前馈式少样本物种分布估计方法：输入少量观测位置+可选元数据，一次前传输出物种编码用于预测未见物种的空间分布，比迭代优化方法快orders of magnitude且SOTA。

**[Fishers for Free? Approximating the Fisher Information Matrix by Recycling the Squared Gradient Accumulator](fishers_for_free_approximating_the_fisher_information_matrix_by_recycling_the_sq.md)**

:   本文系统分析了 Adam 优化器的平方梯度累积器（Squisher）与 Fisher 信息矩阵对角线之间的理论联系，证明 Squisher 可以作为 Fisher 对角线的免费近似，在模型合并、持续学习、稀疏化等五大应用中表现与 Fisher 相当。

**[Fixed-Confidence Multiple Change Point Identification under Bandit Feedback](fixed-confidence_multiple_change_point_identification_under_bandit_feedback.md)**

:   提出了固定置信度下分段常数 bandit 中多变点识别问题，给出实例相关的采样复杂度下界，并设计了简单高效且渐近最优的 MCPI（Multiple Change Point Identification）算法。

**[Fixing The Loose Brake Exponential-Tailed Stopping Time In Best Arm Identificati](fixing_the_loose_brake_exponential-tailed_stopping_time_in_best_arm_identificati.md)**

:   揭示了经典固定置信度最佳臂识别算法（Successive Elimination、KL-LUCB）存在永不停止的正概率事件，并提出 FC-DSH 和元算法 BrakeBooster 两种方案，首次实现了停止时间的指数尾衰减保证，且不损失实例依赖复杂度（仅差对数因子）。

**[Fully Dynamic Euclidean Bi-Chromatic Matching in Sublinear Update Time](fully_dynamic_euclidean_bi-chromatic_matching_in_sublinear_update_time.md)**

:   本文首次提出了欧氏双色匹配问题的全动态亚线性更新算法，对于任意固定 $\varepsilon > 0$，实现 $O(1/\varepsilon)$ 近似比和 $O(n^{\varepsilon})$ 更新时间，可用于高效监控分布漂移（Wasserstein距离）。

**[Fully Heteroscedastic Count Regression with Deep Double Poisson Networks](fully_heteroscedastic_count_regression_with_deep_double_poisson_networks.md)**

:   提出 Deep Double Poisson Network (DDPN)，通过输出 Double Poisson 分布的参数实现离散计数回归中的完全异方差性，支持任意高或低的预测方差，在精度、校准和 OOD 检测上全面超越现有基线。

**[Function Encoders: A Principled Approach to Transfer Learning in Hilbert Spaces](function_encoders_a_principled_approach_to_transfer_learning_in_hilbert_spaces.md)**

:   提出基于 Hilbert 空间几何视角的迁移学习分类体系（凸包插值 / 线性张成外推 / 全空间外推），并设计 Function Encoder 方法利用可学习神经网络基函数实现三种迁移，在多项基准上超越 MAML、Transformer 等方法。

**[General Agents Contain World Models](general_agents_contain_world_models.md)**

:   本文从理论上证明：任何能在多步目标导向任务上泛化的智能体，必然隐式学到了一个其环境的预测模型（世界模型），且该模型可以从智能体的策略中提取出来——智能体越强、目标越复杂，其隐含的世界模型越准确。

**[Generation from Noisy Examples](generation_from_noisy_examples.md)**

:   将 Kleinberg & Mullainathan (2024) 的"极限语言生成"理论框架扩展至噪声样本流场景，提出 Noisy Closure 维度，完整刻画了均匀噪声依赖可生成性的充要条件，并证明所有可数假设类在有限噪声下仍可非均匀生成。

**[GLGENN: 基于Clifford几何代数的轻参数等变神经网络架构](glgenn_a_novel_parameter-light_equivariant_neural_networks_architecture_based_on.md)**

:   提出广义Lipschitz群等变神经网络(GLGENN)，利用几何代数中grade involution和reversion定义的四个基本子空间实现权重共享，在保持伪正交群等变性的同时大幅减少可训练参数（约为CGENN的1/2至1/3），在多个基准任务上匹配或超越CGENN。

**[GPU-friendly and Linearly Convergent First-order Methods for Certifying Optimal $k$-sparse GLMs](gpu-friendly_and_linearly_convergent_first-order_methods_for_certifying_optimal_.md)**

:   提出GPU友好的线性收敛一阶方法，通过复合重构+对偶间隙重启策略，将透视松弛求解加速1-2个数量级，实现大规模稀疏GLM的最优性认证。

**[Gradient Aligned Regression via Pairwise Losses](gradient_aligned_regression_via_pairwise_losses.md)**

:   提出 GAR（Gradient Aligned Regression），通过在标签空间引入两个成对差异损失（误差方差 + 负Pearson相关系数）来对齐预测函数与真实函数的梯度，并利用 DRO 鲁棒聚合三个子损失，实现与传统回归损失相同的线性复杂度，同时在多个基准上超越 MAE/MSE 及对比学习方法。

**[Heavy-Tailed Linear Bandits: Huber Regression with One-Pass Update](heavy-tailed_linear_bandits_huber_regression_with_one-pass_update.md)**

:   提出基于 Online Mirror Descent 的单遍 Huber 回归算法 Hvt-UCB，用于重尾噪声线性 bandit，将每轮计算复杂度从 $\mathcal{O}(t\log T)$ 降至 $\mathcal{O}(1)$，同时保持最优且依赖实例的 regret 界。

**[Hierarchical Refinement: Optimal Transport to Infinity and Beyond](hierarchical_refinement_optimal_transport_to_infinity_and_beyond.md)**

:   提出 Hierarchical Refinement (HiRef) 算法，通过递归求解低秩 OT 子问题动态构建多尺度数据划分，最终恢复双射 Monge 映射，实现 $O(n\log n)$ 时间和 $O(n)$ 空间复杂度，将全秩 OT 扩展到百万级数据。

**[How Do Transformers Learn Variable Binding in Symbolic Programs?](how_do_transformers_learn_variable_binding_in_symbolic_programs.md)**

:   通过训练Transformer在合成程序上做变量解引用(dereference)，揭示了三阶段发展轨迹：(1)随机预测→(2)浅层启发式→(3)系统性解引用机制，因果干预证明模型学会将残差流用作可寻址内存空间。

**[Improved And Oracle-Efficient Online Ell 1-Multicalibration](improved_and_oracle-efficient_online_ell_1-multicalibration.md)**

:   提出将在线 $\ell_1$-multicalibration 归约为新定义的在线线性乘积优化 (OLPO) 问题，分别达到 $\widetilde{O}(T^{-1/3})$（改进速率）和 $\widetilde{O}(T^{-1/4})$（oracle 高效速率）的多校准误差上界。

**[Improved Generalization Bounds for Transductive Learning by Transductive Local Complexity and Its Applications](improved_generalization_bounds_for_transductive_learning_by_transductive_local_c.md)**

:   提出转导局部复杂度（TLC）框架，将经典的局部 Rademacher 复杂度扩展到转导学习设定，获得了与归纳学习几乎一致的超额风险界（仅差对数因子），并解决了十年未决的开放问题。

**[Improved Learning via k-DTW: A Novel Dissimilarity Measure for Curves](improved_learning_via_k-dtw_a_novel_dissimilarity_measure_for_curves.md)**

:   提出 $k$-DTW——一种对多边形曲线的新型不相似度量，仅关注遍历中**最大的 $k$ 个距离之和**，兼具 DTW 的鲁棒性与 Fréchet 距离的度量性质，并首次证明了曲线聚类的**无维度依赖**学习界。

**[Improving Continual Learning Performance and Efficiency with Auxiliary Classifiers](improving_continual_learning_performance_and_efficiency_with_auxiliary_classifie.md)**

:   本文首次探索了早退出网络（early-exit networks）在持续学习中的应用，发现早期分类器天然遭受更少的灾难性遗忘，并提出 Task-wise Logits Correction (TLC) 方法来均衡任务偏差，在阶段增量学习中以不到 70% 的计算量匹配标准方法的准确率。

**[Improving Generalization with Flat Hilbert Bayesian Inference](improving_generalization_with_flat_hilbert_bayesian_inference.md)**

:   提出 Flat Hilbert Bayesian Inference (FHBI)，将 SAM 的平坦性概念从有限维欧氏空间推广到无限维再生核希尔伯特空间 (RKHS)，并与粒子采样贝叶斯推断结合，在 VTAB-1K 基准上以 73.7% 平均 Top-1 准确率全面超越九个基线方法。

**[Improving the Effective Receptive Field of Message-Passing Neural Networks](improving_the_effective_receptive_field_of_message-passing_neural_networks.md)**

:   本文形式化了 MPNN 中有效感受野（ERF）的概念，证明节点贡献随距离指数衰减（二项式分布），并提出 IM-MPNN 架构通过多尺度图粗化和跨尺度信息交织来扩展 ERF，在 LRGB 等长程依赖基准上显著提升。

**[In-Context Adaptation to Concept Drift for Learned Database Operations](in-context_adaptation_to_concept_drift_for_learned_database_operations.md)**

:   提出 FLAIR 框架，利用数据库执行结果作为上下文实现 in-context adaptation，无需运行时参数更新即可应对 concept drift，在基数估计等任务上实现 5.2× 加速和 22.5% 误差降低。

**[Inductive Gradient Adjustment for Spectral Bias in Implicit Neural Representations](inductive_gradient_adjustment_for_spectral_bias_in_implicit_neural_representatio.md)**

:   本文从 NTK 线性动力学模型出发，提出 Inductive Gradient Adjustment (IGA) 方法，通过归纳泛化 eNTK 梯度变换矩阵，**有目的性**地缓解 MLP 的频谱偏差，使 INR 在百万级数据点上也能高效学习高频细节。

**[K²IE: Kernel Method-based Kernel Intensity Estimators for Inhomogeneous Poisson Processes](k2ie_kernel_method-based_kernel_intensity_estimators_for_inhomogeneous_poisson_p.md)**

:   提出 K²IE——基于 RKHS 最小二乘正则化的核强度估计器，证明其 representer theorem 的对偶系数恒为 1，从而将经典核强度估计 (KIE) 与现代核方法在理论上统一，同时兼顾 KIE 的高效性与核方法的边缘校正优势。

**[LapSum -- One Method to Differentiate Them All: Ranking, Sorting and Top-k Selection](lapsum_--_one_method_to_differentiate_them_all_ranking_sorting_and_top-k_selecti.md)**

:   提出 LapSum，基于 Laplace 分布累积密度函数之和的闭式可逆公式，统一解决可微 ranking、sorting、top-k 选择和置换矩阵四大排序问题，时间复杂度仅 $O(n\log n)$、空间 $O(n)$，在大规模场景下显著优于现有方法。

**[Latent Imputation before Prediction: A New Computational Paradigm for De Novo Peptide Sequencing](latent_imputation_before_prediction_a_new_computational_paradigm_for_de_novo_pep.md)**

:   LIPNovo 提出在肽段预测前，通过隐空间补全（latent imputation）来弥补质谱中碎片缺失信息的新范式，利用可学习peak queries和二部匹配补全理论peak隐表示，在三个基准上大幅超越 CasaNovo 等 SOTA（氨基酸精度提升 5.6%-20%）。

**[Latent Variable Estimation in Bayesian Black-Litterman Models](latent_variable_estimation_in_bayesian_black-litterman_models.md)**

:   将经典 Black-Litterman 组合优化模型中的主观投资者观点 $(q, \Omega)$ 视为隐变量，通过贝叶斯网络从市场特征数据中自动推断，消除对人工主观输入的依赖，在 30 年道琼斯和 20 年 ETF 数据上 Sharpe 比率提升约 50%、换手率降低约 55%。

**[Learning-Augmented Algorithms for MTS with Bandit Access to Multiple Predictors](learning-augmented_algorithms_for_mts_with_bandit_access_to_multiple_predictors.md)**

:   在度量任务系统(MTS)中，当算法仅能以 bandit 方式（每步只查询一个启发式且需连续查询 $m$ 步才能观测状态）访问 $\ell$ 个启发式时，本文给出了 regret 为 $O(\text{OPT}^{2/3})$ 的算法，并证明该界是紧的。

**[Learning-Augmented Hierarchical Clustering](learning-augmented_hierarchical_clustering.md)**

:   本文研究借助分裂预言机（splitting oracle）的辅助信息来突破层次聚类的近似硬度障碍，获得 Dasgupta 目标的 $O(1)$ 常数近似和 Moseley-Wang 目标的 $(1-o(1))$ 近似，并推广到流式和并行计算场景。

**[Learning Distances from Data with Normalizing Flows and Score Matching](learning_distances_from_data_with_normalizing_flows_and_score_matching.md)**

:   本文提出利用 normalizing flows 和 score matching 学习密度函数与得分函数，从而高效计算基于密度的 Fermat 距离，解决了传统图方法在高维空间中收敛慢、路径粗糙的问题。

**[Learning Safe Strategies for Value Maximizing Buyers in Uniform Price Auctions](learning_safe_strategies_for_value_maximizing_buyers_in_uniform_price_auctions.md)**

:   针对重复统一价格多物品拍卖中带有RoI约束的价值最大化买家，提出"安全竞标策略"概念，证明其仅需满足温和的不超出竞价条件，并设计多项式时间在线学习算法实现 $\widetilde{O}(M\sqrt{mT})$ 的遗憾界。

**[Learning Survival Distributions with the Asymmetric Laplace Distribution](learning_survival_distributions_with_the_asymmetric_laplace_distribution.md)**

:   提出基于非对称拉普拉斯分布 (ALD) 的参数化生存分析方法，通过神经网络学习 ALD 的三个参数（位置、尺度、不对称性），实现连续、闭式的生存分布估计，在判别性和校准性上全面优于现有参数化与非参数化方法。

**[Leveraging Predictive Equivalence in Decision Trees](leveraging_predictive_equivalence_in_decision_trees.md)**

:   提出将决策树转换为最小析取范式(DNF)表示，消除"预测等价性"问题，统一表示具有相同决策边界的不同决策树，进而改善变量重要性度量、缺失数据鲁棒性和特征获取成本优化。

**[Lightspeed Geometric Dataset Distance via Sliced Optimal Transport](lightspeed_geometric_dataset_distance_via_sliced_optimal_transport.md)**

:   提出 s-OTDD（sliced optimal transport dataset distance），通过 Moment Transform Projection（MTP）将标签分布映射为标量，实现近线性复杂度的数据集距离计算，速度远超 OTDD 且性能相当。

**[Maximum Coverage in Turnstile Streams with Applications to Fingerprinting Measures](maximum_coverage_in_turnstile_streams_with_applications_to_fingerprinting_measur.md)**

:   首次在 turnstile 流模型（支持任意插入/删除）下给出最大覆盖问题的单遍流算法，空间 $\tilde{O}(d/\varepsilon^3)$、更新时间 $\tilde{O}(1)$，并将其推广到隐私指纹识别（fingerprinting）场景，实验比先前方法快 210×。

**[Meek Models Shall Inherit the Earth](meek_models_shall_inherit_the_earth.md)**

:   基于Chinchilla scaling laws论证AI模型性能差距将因计算收益递减而收窄，资源有限的"meek模型"将逐渐接近SOTA性能水平。

**[LANTERN: Modeling User Behavior from Adaptive Surveys with Supplemental Context](modeling_user_behavior_from_adaptive_surveys_with_supplemental_context.md)**

:   提出LANTERN——模块化的用户行为建模架构，通过选择性门控+残差连接+后期融合交叉注意力将调查数据作为主信号、外部上下文作为补充，在多标签调查响应预测中超越纯调查基线。

**[Modified K-means Algorithm with Local Optimality Guarantees](modified_k-means_algorithm_with_local_optimality_guarantees.md)**

:   首次指出经典K-means算法并不总是收敛到局部最优解这一长期误解，并提出LO-K-means修改方案，在不增加单步计算复杂度的前提下保证收敛到连续或离散意义下的局部最优解。

**[Multiple-Policy Evaluation via Density Estimation](multiple-policy_evaluation_via_density_estimation.md)**

:   提出CAESAR算法解决K个策略同时评估问题：通过两阶段方法（粗估计访问分布→计算最优采样分布→密度比估计）实现实例依赖的样本复杂度，比单策略评估K次的朴素方法高效得多。

**[Near-Optimal Consistency-Robustness Trade-Offs for Learning-Augmented Online Knapsack Problems](near-optimal_consistency-robustness_trade-offs_for_learning-augmented_online_kna.md)**

:   提出一族基于简洁预测（临界值的点预测或区间预测）的在线背包算法，在consistency与robustness之间实现近Pareto最优的权衡，并给出分数解到整数解的通用转换方法。

**[Near Optimal Best Arm Identification for Clustered Bandits](near_optimal_best_arm_identification_for_clustered_bandits.md)**

:   在多智能体聚类多臂赌博机设置下，提出 Cl-BAI 和 BAI-Cl 两种算法，利用聚类结构大幅降低最优臂识别的样本复杂度，并证明 BAI-Cl++ 在 $M$ 为常数时达到 minimax 最优。

**[Near-Optimal Decision Trees in a SPLIT Second](near_optimal_decision_trees_in_a_split_second.md)**

:   提出 SPLIT 算法族，通过在决策树根部附近做全局最优搜索、叶节点附近用贪心策略的混合方案，实现比全局最优方法快 100 倍以上且精度几乎无损的决策树构建。

**[NegMerge: Sign-Consensual Weight Merging for Machine Unlearning](negmerge_sign-consensual_weight_merging_for_machine_unlearning.md)**

:   提出 NegMerge，通过合并多个不同超参数微调模型的任务向量、仅保留符号一致的权重元素来构造更有效的遗忘向量，在零样本与标准分类场景中均取得 SOTA 遗忘效果。

**[NeuronTune: Towards Self-Guided Spurious Bias Mitigation](neurontune_towards_self-guided_spurious_bias_mitigation.md)**

:   NeuronTune 提出一种**无需组标签**的自引导去偏方法：通过对比模型隐空间中正确/错误预测样本的神经元激活差异，识别受虚假偏差影响的维度并将其置零，再重训最后一层分类器，从而显著提升 worst-group accuracy。

**[Nonparametric Modern Hopfield Models](nonparametric_modern_hopfield_models.md)**

:   本文提出现代 Hopfield 模型的非参数框架，将记忆存储与检索过程建模为非参数回归问题，由此推导出首个具有亚二次复杂度的高效稀疏结构现代 Hopfield 模型，并提供了完备的理论分析（检索误差界、噪声鲁棒性、指数记忆容量）。

**[On Fine-Grained Distinct Element Estimation](on_fine-grained_distinct_element_estimation.md)**

:   提出以**成对碰撞数** $C$（pairwise collisions）作为分布式去重计数问题的细粒度复杂度参数，设计了通信量随 $C$ 减小而显著降低的协议，打破了此前 $\Omega(\alpha/\varepsilon^2)$ 的最坏情况下界，并给出了所有参数区间的匹配下界。

**[On Temperature Scaling and Conformal Prediction of Deep Classifiers](on_temperature_scaling_and_conformal_prediction_of_deep_classifiers.md)**

:   首次系统研究 Temperature Scaling (TS) 校准对 Conformal Prediction (CP) 方法的影响，揭示 TS 在改善 APS/RAPS 类条件覆盖率的同时会增大预测集尺寸的反直觉现象，建立了完整的非单调理论解释并提出实用指南。

**[On the Clean Generalization and Robust Overfitting in Adversarial Training from Two Theoretical Views: Representation Complexity and Training Dynamics](on_the_clean_generalization_and_robust_overfitting_in_adversarial_training_from_.md)**

:   本文从**表示复杂度**和**训练动态**两个视角，理论解释了对抗训练中"干净泛化与鲁棒过拟合共存"(CGRO)现象：CGRO分类器仅需额外 $\tilde{O}(ND)$ 参数即可通过鲁棒记忆实现，而真正的鲁棒泛化在最坏情况下需要指数级模型容量；在结构化数据上，对抗训练的三阶段相变过程会使网络部分学习真特征、完全记忆噪声，从而可证地收敛到CGRO状态。

**[On the Importance of Gaussianizing Representations](on_the_importance_of_gaussianizing_representations.md)**

:   基于信息论动机（正态分布同时是最优信号与最差噪声分布），提出 Normality Normalization 层：在常规归一化之后用 Power Transform 高斯化激活值，并注入缩放高斯噪声进行正则化，在 ViT/ResNet 上普遍提升泛化与鲁棒性，且不引入额外可学习参数。

**[On the Role of Label Noise in the Feature Learning Process](on_the_role_of_label_noise_in_the_feature_learning_process.md)**

:   从理论和实证角度分析标签噪声在神经网络特征学习中的作用，发现适量的标签噪声可以促进更鲁棒的特征学习（类似正则化效果），但过多噪声会破坏特征质量。

**[OOD-Chameleon: Is Algorithm Selection for OOD Generalization Learnable?](ood-chameleon_is_algorithm_selection_for_ood_generalization_learnable.md)**

:   探索"为OOD泛化学习算法选择"的可能性：将选择形式化为基于数据集特征的多标签分类，在"数据集的数据集"上训练选择器，可根据数据集特征预测最佳训练算法，无需先训练模型。

**[Optimal Auction Design in the Joint Advertising](optimal_auction_design_in_the_joint_advertising.md)**

:   本文针对联合广告场景（零售商与供应商共同竞标广告位）提出最优拍卖机制：单槽位下给出Myerson式闭式最优解，多槽位下设计BundleNet神经网络以bundle为单位构建IC约束，在保证近似激励兼容的同时最大化平台收入。

**[Optimal Sensor Scheduling and Selection for Continuous-Discrete Kalman Filtering with Auxiliary Dynamics](optimal_sensor_scheduling_and_selection_for_continuous-discrete_kalman_filtering.md)**

:   提出一种面向连续-离散卡尔曼滤波 (CD-KF) 的最优传感器调度框架：将多传感器观测建模为独立 Poisson 过程，推导后验协方差矩阵的可微上界，利用梯度优化方法联合优化观测频率与辅助动力学输入，并通过 Wasserstein-2 最优量化确定性地选取观测时刻。

**[PAC Learning with Improvements](pac_learning_with_improvements.md)**

:   提出"带改进的PAC学习"框架：当agent能真正提升自身特征时，学习器可以通过保守分类实现零误差，且可学性与标准PAC模型和策略性分类模型存在本质分离。

**[Permutation Equivariant Neural Networks for Symmetric Tensors](permutation_equivariant_neural_networks_for_symmetric_tensors.md)**

:   本文首次研究了以对称张量为输入的置换等变神经网络，给出了对称幂空间之间所有线性置换等变函数的两种完整刻画，实验证明该方法在数据效率和泛化能力上显著优于标准 MLP。

**[Position: AI Evaluation Should Learn from How We Test Humans](position_ai_evaluation_should_learn_from_how_we_test_humans.md)**

:   提出将人类心理测量学中的自适应测试范式引入AI评估，通过估计测试题目特征（难度/区分度/猜测因子）实现更高效、可靠的模型能力评估。

**[Position: Solve Layerwise Linear Models First to Understand Neural Dynamical Phenomena](position_solve_layerwise_linear_models_first_to_understand_neural_dynamical_phen.md)**

:   提出**动态反馈原则 (Dynamical Feedback Principle)**，论证逐层线性模型（layerwise linear models）足以统一解释 neural collapse、emergence、lazy/rich regime 和 grokking 四大深度学习动力学现象，呼吁优先研究逐层结构而非非线性激活。

**[Position: The Future of Bayesian Prediction Is Prior-Fitted](position_the_future_of_bayesian_prediction_is_prior-fitted.md)**

:   本文是一篇 position paper，主张 **Prior-Data Fitted Networks (PFNs)**——在随机生成的合成数据集上训练神经网络以近似贝叶斯后验预测分布——代表了贝叶斯推断的未来方向，因为它在实现简洁性、先验定义灵活性、推理速度上全面超越传统 MCMC/VI/GP 方法，并已在表格学习 (TabPFN) 中证明了超越 XGBoost 的实力。

**[Positional Attention: Expressivity and Learnability of Algorithmic Computation](positional_attention_expressivity_and_learnability_of_algorithmic_computation.md)**

:   提出 **Positional Transformer**——注意力权重仅由位置编码决定、与输入数据无关的 Transformer 变体，证明其保持了与 MPC 并行计算模型等价的表达力（仅增加 $O(\log n)$ 深度代价），并在算法任务上展现出显著更优的分布外泛化能力。

**[Practical Principles for AI Cost and Compute Accounting](practical_principles_for_ai_cost_and_compute_accounting.md)**

:   提出AI成本与计算量核算的七项原则，旨在减少监管漏洞（特别是蒸馏漏洞）、避免抑制风险缓解措施、并实现跨企业一致性。

**[Prediction-Powered Adaptive Shrinkage Estimation](prediction-powered_adaptive_shrinkage_estimation.md)**

:   将Prediction-Powered Inference (PPI)与经验贝叶斯收缩结合，提出PAS方法，在多个并行均值估计问题中通过问题内方差缩减和问题间自适应收缩实现MSE最优。

**[Prediction via Shapley Value Regression (ViaSHAP)](prediction_via_shapley_value_regression.md)**

:   提出 ViaSHAP，将 Shapley 值的计算融入模型训练过程，使得推理时通过对 Shapley 值求和直接得到预测，无需后验解释器，在表格数据上达到 XGBoost 级别的预测精度，同时 Shapley 值近似质量显著优于 FastSHAP。

**[Principled Algorithms for Optimizing Generalized Metrics in Binary Classification](principled_algorithms_for_optimizing_generalized_metrics_in_binary_classificatio.md)**

:   本文提出了优化广义分类指标（如 $F_\beta$、Jaccard、加权准确率等）的有原则算法 METRO，基于 $H$-一致性界和代理损失理论，将指标优化重新表述为广义代价敏感学习问题，具有有限样本泛化保证。

**[Probably Approximately Global Robustness Certification](probably_approximately_global_robustness_certification.md)**

:   提出基于 ε-net 采样的概率近似全局鲁棒性（PAG）认证框架，所需样本量与输入维度、类别数和模型架构无关，可高效认证大规模神经网络的全局鲁棒性。

**[Provably Cost-Sensitive Adversarial Defense via Randomized Smoothing](provably_cost-sensitive_adversarial_defense_via_randomized_smoothing.md)**

:   基于 randomized smoothing 框架提出"代价敏感认证半径"（cost-sensitive certified radius），首次实现可扩展到大模型与高维数据的代价敏感对抗鲁棒性认证与训练，在保持整体准确率的同时显著提升对高代价误分类的鲁棒性。

**[Provably Efficient Algorithm for Best Scoring Rule Identification in Online Principal-Agent Information Acquisition](provably_efficient_algorithm_for_best_scoring_rule_identification_in_online_prin.md)**

:   本文在委托-代理（principal-agent）在线信息获取框架下研究最佳评分规则识别（Best Scoring Rule Identification, BSRI）问题，提出 OIAFC（固定置信度）和 OIAFB（固定预算）两种算法，首次建立了实例依赖的样本复杂度上界 $\widetilde{O}(MH_\Delta)$，并将实例无关的样本复杂度从已有工作的 $\widetilde{O}(C_O^3 K^6 \epsilon^{-3})$ 大幅改进至 $\widetilde{O}(MK\epsilon^{-2})$。

**[Randomized Dimensionality Reduction for Euclidean Maximization and Diversity Measures](randomized_dimensionality_reduction_for_euclidean_maximization_and_diversity_mea.md)**

:   证明了对一大类欧氏最大化问题（最大匹配、最大TSP、最大生成树、子图多样性等），使用数据无关的高斯 JL 变换将维度降至 $O(\lambda)$（$\lambda$ 为数据集倍增维度）即可近似保持所有候选解的值，并证明该依赖是紧的。

**[Regression for the Mean: Auto-Evaluation and Inference with Few Labels through Post-hoc Regression](regression_for_the_mean_auto-evaluation_and_inference_with_few_labels_through_po.md)**

:   将 PPI++ 中调参 $\lambda$ 的过程重新解释为事后回归（post-hoc regression），提出 Ridge-PPI 和 Sigmoid-PPI 两种改进方法，在少标签（$n < 50$）场景下显著降低均值估计方差，优于经典估计和 PPI++。

**[Residual Matrix Transformers: Scaling the Size of the Residual Stream](residual_matrix_transformers_scaling_the_size_of_the_residual_stream.md)**

:   用外积记忆矩阵替换 Transformer 的残差流向量，使残差流大小可独立于模型参数量和 FLOPS 扩展，在相同 loss 下节省 58% FLOPS、25% 参数和 41% 训练 token。

**[Rethinking Aleatoric and Epistemic Uncertainty](rethinking_aleatoric_and_epistemic_uncertainty.md)**

:   本文指出机器学习中 aleatoric/epistemic 不确定性二分法存在根本性概念混淆，提出基于决策理论的替代框架，将预测不确定性、可约/不可约分解、预测性能和数据分散度统一在一个连贯的理论体系中，并揭示了 BALD 作为 epistemic uncertainty 估计器的局限性。

**[Rethinking Explainable Machine Learning as Applied Statistics](rethinking_explainable_machine_learning_as_applied_statistics.md)**

:   本文是一篇立场论文，提出可解释机器学习应被视为"高维函数的应用统计学"——解释算法本质上是函数的统计量（functionals），应当像传统统计量（如 p 值、置信区间）一样关注其**解释**（interpretation）问题，而非仅研究数学性质；当前文献最大的缺陷正是忽视了"解释算法的输出到底回答了哪个直觉问题"这一核心议题。

**[Revisiting Instance-Optimal Cluster Recovery in the Labeled Stochastic Block Model](revisiting_instance-optimal_cluster_recovery_in_the_labeled_stochastic_block_mod.md)**

:   提出IAC算法，在标签随机块模型(LSBM)中以$O(n\text{polylog}(n))$复杂度首次实现匹配实例最优下界的聚类恢复，同时给出期望和高概率保证。

**[Revisiting the Predictability of Performative, Social Events](revisiting_the_predictability_of_performative_social_events.md)**

:   本文用现代学习理论工具（performative prediction + outcome indistinguishability）重新回答了20世纪社会科学中的经典问题：在预测会主动影响结果的情况下，社会事件是否仍可被准确预测？答案是肯定的——但这种"准确"的预测可能毫无用处。

**[Runtime Analysis of Evolutionary NAS for Multiclass Classification](runtime_analysis_of_evolutionary_nas_for_multiclass_classification.md)**

:   首次对进化神经架构搜索(ENAS)在多类分类问题上进行运行时理论分析，证明 one-bit 和 bit-wise 变异的 (1+1)-ENAS 算法均以 $O(rM\ln rM)$ 期望运行时找到最优架构，说明简单的 one-bit 变异即可与复杂的 bit-wise 变异媲美。

**[Sampling from Binary Quadratic Distributions via Stochastic Localization](sampling_from_binary_quadratic_distributions_via_stochastic_localization.md)**

:   首次将随机局部化 (Stochastic Localization, SL) 框架应用于一般二元二次分布 (BQD) 采样，证明经过足够SL迭代后后验分布几乎处处满足 Poincaré 不等式，从而保证离散 MCMC 采样器多项式时间混合，并在 QUBO 组合优化问题上验证了一致的采样效率提升。

**[Sassha: Sharpness-aware Adaptive Second-order Optimization with Stable Hessian Approximation](sassha_sharpness-aware_adaptive_second-order_optimization_with_stable_hessian_ap.md)**

:   提出 Sassha 优化器，将 sharpness-aware minimization（SAM）引入二阶优化框架，通过稳定 Hessian 近似和 lazy 更新策略，使二阶方法首次在泛化性能上全面超越 SGD、AdamW 和 SAM 等一阶方法。

**[Scalable Equilibrium Sampling with Sequential Boltzmann Generators](scalable_equilibrium_sampling_with_sequential_boltzmann_generators.md)**

:   SBG通过Transformer架构规范化流(TarFlow)和退火Langevin动力学的序列蒙特卡洛，首次在笛卡尔坐标系中实现六肽(66原子)系统的高效平衡采样。

**[Score Matching with Missing Data](score_matching_with_missing_data.md)**

:   本文将 score matching 及其主要扩展适配到缺失数据场景，提出两种变体——重要性加权（IW）方法和变分方法，在图模型估计等任务上展示了不同场景下各自的优势。

**[Set-Valued Predictions for Robust Domain Generalization](set_valued_predictions_for_robust_domain_generalization.md)**

:   提出集值预测器（set-valued predictor）解决域泛化（DG）中的鲁棒性问题：输出标签子集而非单一标签，使预测在尽可能多的未见域上满足预定义的覆盖率要求，同时最小化预测集大小。

**[Softmax is not Enough (for Sharp Size Generalisation)](softmax_is_not_enough_for_sharp_size_generalisation.md)**

:   本文从理论上证明了 softmax 注意力在输入规模增大时**必然发生系数分散（dispersion）**，无法保持对少量关键元素的尖锐聚焦，并提出自适应温度（adaptive temperature）作为缓解手段。

**[Sparse-Pivot: Dynamic Correlation Clustering for Node Insertions](sparse-pivot_dynamic_correlation_clustering_for_node_insertions.md)**

:   提出 Sparse-Pivot 算法，在节点动态插入的 Correlation Clustering 问题中以摊销 $O_\varepsilon(\log^{O(1)} n)$ 的数据库操作实现 $(20+\varepsilon)$-近似，大幅改善了 Cohen-Addad et al. (ICML 2024) 的近似因子，并在实验中全面优于基线。

**[Sparse Training from Random Initialization: Aligning Lottery Ticket Masks using Weight Symmetry](sparse_training_from_random_initialization_aligning_lottery_ticket_masks_using_w.md)**

:   从权重对称性角度解释彩票假说(LTH)掩码不能迁移到新初始化的原因，并提出通过置换匹配对齐LTH掩码与新初始化的优化盆地来实现稀疏训练。

**[SUICA: Learning Super-high Dimensional Sparse Implicit Neural Representations for Spatial Transcriptomics](suica_learning_super-high_dimensional_sparse_implicit_neural_representations_for.md)**

:   提出SUICA框架，通过图增强自编码器将超高维零膨胀基因表达映射到紧凑嵌入空间，再用INR进行连续空间建模，实现跨平台ST数据的空间插值、基因插补和去噪。

**[Suitability Filter: A Statistical Framework for Classifier Evaluation in Real-World Settings](suitability_filter_a_statistical_framework_for_classifier_evaluation_in_real-wor.md)**

:   本文提出 Suitability Filter 框架，利用模型输出的"适用性信号"（suitability signals）在无标签的用户数据上检测分类器性能退化，通过统计假设检验判断准确率是否相比测试集显著下降。

**[Symmetry-Aware GFlowNets](symmetry-aware_gflownets.md)**

:   揭示GFlowNets中图对称性导致的系统性采样偏差，提出通过自同构群大小缩放奖励的简单修正方法SA-GFN，实现无偏采样。

**[Symmetry-Robust 3D Orientation Estimation](symmetry-robust_3d_orientation_estimation.md)**

:   提出一种对旋转对称性鲁棒的两阶段3D朝向估计流水线：第一阶段通过商回归（quotient regression）将朝向恢复到八面体对称群的等价类内，第二阶段通过分类器预测24个八面体翻转之一以完成精确复原，在ShapeNet上取得SOTA。

**[SynDaCaTE: A Synthetic Dataset for Evaluating Part-Whole Hierarchical Inference](syndacate_a_synthetic_dataset_for_evaluating_part-whole_hierarchical_inference.md)**

:   提出SynDaCaTE合成数据集用于评估部分-整体层次推断能力，揭示CapsNet瓶颈在于图像到部件推断，且SetTransformer是部件到整体推断的强基线。

**[System-Aware Unlearning Algorithms: Use Lesser, Forget Faster](system-aware_unlearning_algorithms_use_lesser_forget_faster.md)**

:   提出系统感知遗忘 (system-aware unlearning) 新定义，将攻击者的能力限制为只能访问系统实际存储的内容而非全部剩余数据，并基于核心集 (core set) + 选择采样 (selective sampling) 设计了线性分类的精确遗忘算法，实现亚线性内存和极低删除时间。

**[TANGO: Clustering with Typicality-Aware Nonlocal Mode-Seeking and Graph-Cut Optimization](tango_clustering_with_typicality-aware_nonlocal_mode-seeking_and_graph-cut_optim.md)**

:   提出"典型性(typicality)"概念，从全局视角量化数据点作为模式(聚类中心)的置信度，结合改进的路径相似度与图割优化，实现无需人工阈值设定的自动模式检测与聚类。

**[The Dark Side of the Forces: Assessing Non-Conservative Force Models for Atomistic Machine Learning](the_dark_side_of_the_forces_assessing_non-conservative_force_models_for_atomisti.md)**

:   系统评估非保守力模型在原子模拟中的实际影响，揭示其导致几何优化不收敛和分子动力学不稳定，并提出保守+非保守混合模型作为最佳实践。

**[The Double-Ellipsoid Geometry of CLIP](the_double-ellipsoid_geometry_of_clip.md)**

:   揭示CLIP嵌入的双椭球体几何结构——图像和文本分别位于偏离原点的可线性分离椭球壳上，并从对比学习的false negative处理角度解释这一结构的优势。

**[The Price of Freedom: Exploring Expressivity and Runtime Tradeoffs in Equivariant Networks](the_price_of_freedom_exploring_expressivity_and_runtime_tradeoffs_in_equivariant.md)**

:   本文系统分析了 $E(3)$-等变神经网络中多种张量积操作的表达力与运行时间权衡，发现理论复杂度与实际性能差距悬殊，并提出基于球面网格的简化 Gaunt 张量积实现，在 MACE 原子间势能训练中加速 30%。

**[Theoretical Performance Guarantees for Partial Domain Adaptation via Partial Optimal Transport](theoretical_performance_guarantees_for_partial_domain_adaptation_via_partial_opt.md)**

:   本文基于部分最优传输理论推导了部分领域自适应（PDA）的泛化界，证明了部分 Wasserstein 距离作为领域对齐项和提出的理论驱动权重方案的合理性，并据此开发了实用算法 WARMPOT。

**[Time-Aware World Model for Adaptive Prediction and Control](time-aware_world_model_for_adaptive_prediction_and_control.md)**

:   提出时间感知世界模型TAWM，通过将时间步长$\Delta t$作为模型输入并在多种$\Delta t$上混合训练，在不增加样本量的前提下跨时间尺度学习任务动力学。

**[To Each Metric Its Decoding: Post-Hoc Optimal Decision Rules of Probabilistic Hierarchical Classifiers](to_each_metric_its_decoding_post-hoc_optimal_decision_rules_of_probabilistic_hie.md)**

:   本文提出了针对概率层次分类器的后处理最优解码框架，为不同评价指标（如层次 $F_\beta$）推导了最优决策规则，在候选集限于节点集时给出通用算法，对子集预测推导了专门的层次 $hF_\beta$ 最优策略。

**[Towards Attributions of Input Variables in a Coalition](towards_attributions_of_input_variables_in_a_coalition.md)**

:   从AND-OR交互的角度揭示联盟归因与个体变量归因之间的冲突本质，定义了正式的联盟归因指标并提出三种评估联盟忠实度的度量。

**[Towards Robust Influence Functions with Flat Validation Minima](towards_robust_influence_functions_with_flat_validation_minima.md)**

:   揭示影响函数(IF)在含噪数据上失效的根因在于验证损失的尖锐性而非参数估计精度，提出基于平坦验证极小值的新IF估计形式。

**[Understanding Mode Connectivity via Parameter Space Symmetry](understanding_mode_connectivity_via_parameter_space_symmetry.md)**

:   通过参数空间的连续对称性（如 $GL_h(\mathbb{R})$）分析神经网络损失函数最小值集合的拓扑连通性，推导出线性网络最小值的连通分量数为 $2^{l-1}$，并证明 skip connection 可减少该数目，同时给出对称性诱导的显式低损失连接曲线及线性模式连通性近似成立的充分条件。

**[UnHiPPO: Uncertainty-Aware Initialization for State Space Models](unhippo_uncertainty-aware_initialization_for_state_space_models.md)**

:   本文扩展了 HiPPO 理论以处理带噪声的测量数据，将 SSM 的初始化问题重新表述为线性随机控制问题，推导出不确定性感知的动力学初始化方案，在不增加运行时间的前提下显著提升 SSM 的噪声鲁棒性。

**[Unlocking the Power of Rehearsal in Continual Learning: A Theoretical Perspective](unlocking_the_power_of_rehearsal_in_continual_learning_a_theoretical_perspective.md)**

:   从理论角度分析持续学习中排练（rehearsal/experience replay）策略的有效性，建立排练缓冲区大小、任务数量与遗忘程度之间的精确关系，证明适当的排练策略可以有效缓解灾难性遗忘。

**[WGFormer: An SE(3)-Transformer Driven by Wasserstein Gradient Flows for Molecular Generation](wgformer_an_se3-transformer_driven_by_wasserstein_gradient_flows_for_molecular_g.md)**

:   本文提出 WGFormer，一种由 Wasserstein 梯度流驱动的 SE(3)-Transformer，在自编码器框架内通过最小化原子潜在混合模型上的能量函数来优化分子构象，在基态构象预测任务上一致超越 SOTA。

**[What Makes an Ensemble (Un)interpretable?](what_makes_an_ensemble_un_interpretable.md)**

:   系统研究集成学习方法的可解释性问题——什么因素使集成模型难以解释，以及如何在保持预测性能的同时提高集成的可解释性，提出了量化集成可解释性的理论框架和实用的可解释集成构建方法。

**[Whitened CLIP as a Likelihood Surrogate of Images and Captions](whitened_clip_as_a_likelihood_surrogate_of_images_and_captions.md)**

:   （注：此文缓存不在已读范围内，基于arXiv元信息和领域知识推断写就基本结构。）
