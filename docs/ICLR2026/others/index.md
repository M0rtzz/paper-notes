<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**🔬 ICLR2026** · 共 **122** 篇

**[A Federated Generalized Expectation-Maximization Algorithm for Mixture Models with an Unknown Number of Components](a_federated_generalized_expectation-maximization_algorithm_for_mixture_models_wi.md)**

:   提出 FedGEM 算法，通过客户端本地 EM 步后构建不确定性集、服务器利用不确定性集交集检测聚类重叠并推断全局聚类数，首次实现在全局聚类数未知情况下的联邦聚类，并提供了概率收敛保证。

**[A Law of Data Reconstruction for Random Features (and Beyond)](a_law_of_data_reconstruction_for_random_features_and_beyond.md)**

:   从信息论和代数角度证明随机特征模型中存在数据重构定律：当参数量 $p \gg dn$（$d$ 为数据维度，$n$ 为样本数）时，训练数据可被完整重构，并通过投影损失优化方法在 RF、两层网络和 ResNet 上验证了该阈值的普适性。

**[A Representer Theorem for Hawkes Processes via Penalized Least Squares Minimization](a_representer_theorem_for_hawkes_processes_via_penalized_least_squares_minimizat.md)**

:   为线性多元 Hawkes 过程在 RKHS 框架下的触发核估计建立了新型表示定理，证明最优估计器可用等价核在数据点上的线性组合表示且对偶系数全部解析地等于 1，无需求解对偶优化问题，从而实现高效可扩展的非参数估计。

**[A Scalable Inter-edge Correlation Modeling in CopulaGNN for Link Sign Prediction](a_scalable_inter-edge_correlation_modeling_in_copulagnn_for_link_sign_prediction.md)**

:   将 CopulaGNN 从节点级扩展到边级，通过将相关矩阵构造为边嵌入的 Gramian 矩阵并利用 Woodbury 恒等式重构条件概率分布，实现了在签名图上对边间统计依赖的可扩展建模，用于链接符号预测任务。

**[A Single Architecture for Representing Invariance Under Any Space Group](a_single_architecture_for_representing_invariance_under_any_space_group.md)**

:   设计了一种可自适应任意空间群不变性的单一架构 (Crystal Fourier Transformer)，通过解析推导群操作对傅里叶系数的约束来构造对称适配的傅里叶基，用约束的对偶图表示实现了跨 230 个空间群的参数共享和零样本泛化。

**[Accessible, Realistic, and Fair Evaluation of Positive-Unlabeled Learning Algorithms](accessible_realistic_and_fair_evaluation_of_positive-unlabeled_learning_algorith.md)**

:   提出首个 PU 学习统一基准，系统解决两个关键问题：(1) 用代理准确率和代理 AUC 实现无负样本的模型选择；(2) 发现并通过将正样本并入无标签集的简单校准方法解决单样本设置下的内部标签偏移问题，使双样本算法在单样本评估中得到公平比较。

**[Active Learning for Decision Trees with Provable Guarantees](active_learning_for_decision_trees_with_provable_guarantees.md)**

:   为决策树主动学习提供首个理论保证：(1) 首次分析决策树的不一致系数（disagreement coefficient）并给出 $O(\ln^{OPT}(n))$ 上界；(2) 提出首个达到乘法误差 $(1+\epsilon)$ 保证的二分类主动学习算法；结合两者实现数据集大小的多对数标签复杂度。

**[Addressing Divergent Representations from Causal Interventions on Neural Networks](addressing_divergent_representations_causal.md)**

:   系统性地揭示因果干预（activation patching、DAS、SAE 等）会将模型内部表征推离自然分布，理论区分"无害偏移"与"有害偏移"两类情况，并提出 Counterfactual Latent (CL) loss 来约束干预表征不偏离流形，在 7B LLM 上验证可减少偏移同时保持干预准确率。

**[Agnostics: Learning to Synthesize Code in Any Programming Language with a Universal RL Environment](agnostics_learning_to_code_in_any_programming_language_via_reinforcement_with_a_.md)**

:   提出Agnostics，一种语言无关的后训练pipeline：将编程任务统一为I/O行为规范格式，用通用验证器+GRPO强化学习训练LLM在任何编程语言上编码，使Qwen 4B在Lua/Julia/R/OCaml/Fortran五种低资源语言上达到匹敌16B-70B模型的SOTA水平。

**[An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes](an_information-theoretic_framework_for_optimizing_experimental_design_to_disting.md)**

:   提出"信息间隙"（information gap）框架，通过优化刺激分布来最大化似然编码（likelihood code）与后验编码（posterior code）假设之间的可区分性，推导出真实后验与任务边缘化代理后验之间的KL散度作为优化目标，并通过DNN解码器在模拟神经群体上验证了该框架的有效性，揭示传统单上下文实验无法区分两种编码假设。

**[AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning](anessuite_a_comprehensive_benchmark_and_dataset_suite_for_anesthesiology_reasoni.md)**

:   构建首个面向麻醉学推理的综合数据集套件AnesSuite——包括AnesBench（7972道双语选择题）、AnesCorpus（240万篇文档语料库）、AnesQA（2万条QA对）和AnesR1（1万条CoT推理数据），提出三级认知需求分类（System 1/1.x/2），训练的Morpheus模型（Qwen2.5 + SFT + GRPO）在7B参数下达到14B基线性能，揭示当前最强模型在复杂推理（System 2）上仍低于0.6。

**[ANO: Faster is Better in Noisy Landscapes](ano_faster_is_better_in_noisy_landscape.md)**

:   提出 Ano 优化器，将更新方向和幅度解耦——方向用动量的符号（sign）确保噪声鲁棒，幅度用瞬时梯度绝对值（而非动量幅度）确保响应速度，配合改进的 Yogi 式方差估计，在噪声和非平稳环境（如 RL）中显著优于 Adam/Lion/Adan，同时在标准任务上保持竞争力。

**[AnyUp: Universal Feature Upsampling](anyup_universal_feature_upsampling.md)**

:   提出AnyUp——首个推理时encoder无关的可学习特征上采样方法，通过feature-agnostic层处理任意维度/类型的视觉特征，配合窗口注意力架构和crop-based训练策略，训练一次即可对任意视觉编码器（DINO/CLIP/SigLIP/MAE等）的特征进行任意分辨率上采样，在多个下游任务上超越FeatUp/JAFAR/LoftUp等方法。

**[Articulation in Motion: Prior-Free Part Mobility Analysis for Articulated Objects](articulation_in_motion_prior-free_part_mobility_analysis_for_articulated_objects.md)**

:   提出AiM（Articulation in Motion）框架，从交互视频和初始状态扫描中无需部件数量先验地重建铰接物体——通过双高斯表征（静态GS + 可变形GS）实现动静解耦，结合顺序RANSAC进行无先验部件分割和关节估计，辅以SDMD模块处理新暴露的静态区域，在复杂6部件物体（Storage）上以79.34% mean IoU大幅超越需先验的ArtGS（52.23%）。

**[ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity](assess_a_semantic_and_structural_evaluation_framework_for_statement_similarity.md)**

:   提出 TransTED Similarity，一种基于算子树 (Operator Tree) 和语义变换增强的树编辑距离指标，用于评估自动形式化 (autoformalization) 生成的形式化数学命题与参考命题之间的语义相似度，并构建了 EPLA 基准数据集。

**[AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite](astabench_benchmarking_ai_agents.md)**

:   由 AI2 团队构建的首个端到端科学研究 Agent 基准 AstaBench，包含 2400+ 问题覆盖科学发现全流程，配备生产级可复现搜索工具，评估了 57 个 Agent（22 类），发现尽管单任务有进展但 AI 距离完整科学研究助手仍很远，同时系统性修复先前基准的 5 大方法学缺陷。

**[Behavior Learning (BL): Learning Hierarchical Optimization Structures from Data](behavior_learning_bl_learning_hierarchical_optimization_structures_from_data.md)**

:   受行为科学中效用最大化范式启发，提出 Behavior Learning (BL) 框架，将数据建模为由可解释的模块化效用最大化问题（UMP）层次组合所诱导的 Gibbs 分布，在预测性能、内在可解释性和参数可辨识性三者之间实现了统一。

**[Block-Sample MAC-Bayes Generalization Bounds](block-sample_mac-bayes_generalization_bounds.md)**

:   提出块样本MAC-Bayes泛化界（mean approximately correct），将训练数据划分为J个块后用各块条件下的KL散度之和替代整体KL散度，在确定性学习算法（如均值估计）等原始PAC-Bayes界为空（vacuous）的场景下仍能给出有限、有意义的泛化误差界，并证明了该界的高概率版本在一般情况下不可行。

**[CaDrift: A Time-dependent Causal Generator of Drifting Data Streams](cadrift_a_time-dependent_causal_generator_of_drifting_data_streams.md)**

:   提出 CaDrift，一个基于结构因果模型（SCM）的时间依赖合成数据流生成框架，通过 EWMA 平滑和自回归噪声引入时序相关性，并通过修改因果映射函数实现可控的分布漂移、协变量漂移、严重漂移和局部漂移，填补了现有数据流生成器既不因果又不时序依赖的空白。

**[Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation and Beyond](can_you_hear_me_now_a_benchmark_for_long-range_graph_propagation_and_beyond.md)**

:   本文提出 ECHO 基准，包含 3 个合成任务和 2 个基于密度泛函理论（DFT）的真实化学任务，要求图神经网络在 17–40 跳范围内有效传播信息，系统评估了 11 种 GNN 架构的长程传播能力。

**[CHAMMI-75: Pre-training multi-channel models with heterogeneous microscopy images](chammi-75_pre-training_multi-channel_models_with_heterogeneous_microscopy_images.md)**

:   构建 CHAMMI-75——最大的异构多通道显微镜图像预训练数据集（280 万图像，75 个来源，25 种通道类型，16 种物种），证明成像模态多样性是提升多通道模型泛化能力的关键因素，训练的 MorphEm 模型在 7 个 benchmark 中 6 个达到 SOTA。

**[Characterizing and Optimizing the Spatial Kernel of Multi Resolution Hash Encodings](characterizing_and_optimizing_the_spatial_kernel_of_multi_resolution_hash_encodi.md)**

:   从物理系统角度分析 Instant-NGP 的多分辨率哈希编码（MHE），推导出其点扩展函数（PSF）的闭式近似，发现有效分辨率由平均分辨率 $N_{\text{avg}}$ 而非最细分辨率 $N_{\max}$ 决定，且存在网格引起的各向异性，并提出零开销的 Rotated MHE（R-MHE）通过逐层旋转输入坐标消除各向异性。

**[CHLU: The Causal Hamiltonian Learning Unit as a Symplectic Primitive for Deep Learning](chlu_the_causal_hamiltonian_learning_unit_as_a_symplectic_primitive_for_deep_lea.md)**

:   CHLU 是一种基于相对论哈密顿力学和辛积分的计算学习原语，通过强制相空间体积守恒和引入因果速度上限，解决了 LSTM 的梯度爆炸/消失和 Neural ODE 的信息耗散问题，实现无限时域稳定性和热力学生成能力。

**[Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevance Assessment](completing_missing_annotation_multi-agent_debate_for_accurate_and_scalable_relev.md)**

:   提出DREAM框架——用对立立场初始化的双Agent多轮辩论进行IR相关性标注，达到95.2%准确率且仅3.5%案例需人工介入。据此构建BRIDGE基准，发现29,824个缺失标注（原有标注的428%），修正了检索系统排名偏差和检索-生成性能不匹配。

**[Compositional Diffusion with Guided Search for Long-Horizon Planning](compositional_diffusion_long_horizon_planning.md)**

:   提出 CDGS（Compositional Diffusion with Guided Search），通过在扩散去噪过程中嵌入基于种群的搜索机制（迭代重采样 + 似然剪枝），解决组合式扩散模型在多模态局部分布合成时的模式平均问题，从短时域模型采样出全局一致的长时域规划。

**[Consistent Low-Rank Approximation](consistent_low-rank_approximation.md)**

:   提出并系统研究"一致低秩近似"问题——在流数据中逐行到达的矩阵上维护近最优 rank-$k$ 近似的同时最小化解的总变化量（recourse），证明加性误差下 $O(k/\varepsilon \cdot \log(nd))$ recourse 可行，乘性 $(1+\varepsilon)$ 误差下 $k^{3/2}/\varepsilon^2 \cdot \text{polylog}$ recourse 可行，并给出 $\Omega(k/\varepsilon \cdot \log(n/k))$ 的下界。

**[Decomposing Representation Space into Interpretable Subspaces with Unsupervised Learning](decomposing_representation_space_into_interpretable_subspaces_with_unsupervised_.md)**

:   提出 NDM（Neighbor Distance Minimization），通过最小化子空间内的近邻距离来无监督地发现神经网络表征空间中的可解释非基对齐子空间，在 GPT-2 上平均 Gini=0.71（信息高度集中），在 Qwen2.5-1.5B 上发现了参数化知识与上下文知识路由的分离子空间。

**[Deconstructing Positional Information: From Attention Logits to Training Biases](deconstructing_positional_information_from_attention_logits_to_training_biases.md)**

:   提出基于 Toeplitz 矩阵的统一分析框架，将位置编码分为加法（Absolute/T5/ALiBi）和乘法（RoPE）两类；通过合成任务发现 RoPE 在位置敏感任务上优势显著但存在"单头沉积模式"（single-head deposit pattern）——浅层几乎所有位置推理集中于单个注意力头；理论证明该模式是 RoPE 乘法结构的固有属性。

**[Digging Deeper: Learning Multi-Level Concept Hierarchies](digging_deeper_learning_multi-level_concept_hierarchies.md)**

:   本文提出Multi-Level Concept Splitting（MLCS）从仅有的顶层概念监督中自动发现多层次概念层级，结合Deep-HiCEMs架构表示这些层级结构，使模型在保持高精度的同时支持多个抽象层次的测试时概念干预。

**[Directional Sheaf Hypergraph Networks: Unifying Learning on Directed and Undirected Hypergraphs](directional_sheaf_hypergraph_networks_unifying_learning_on_directed_and_undirect.md)**

:   本文提出 Directional Sheaf Hypergraph Networks (DSHN)，通过将 Cellular Sheaf 理论与有向超图的方向信息结合，构造了一种复值 Hermitian Laplacian 算子，统一并推广了现有的图和超图 Laplacian，在 7 个真实数据集上相对准确率提升 2%–20%。

**[Disentangling Shared and Private Neural Dynamics with SPIRE: A Latent Modeling Framework for Deep Brain Stimulation](disentangling_shared_and_private_neural_dynamics_with_spire_a_latent_modeling_fr.md)**

:   提出 SPIRE（Shared–Private Inter-Regional Encoder），一种深度多编码器自编码器，将多脑区神经记录分解为跨区域共享和区域专属的潜在子空间，仅在基线数据上训练即可揭示深脑刺激（DBS）引发的网络级动态重组。

**[Distributed Algorithms for Euclidean Clustering](distributed_algorithms_for_euclidean_clustering.md)**

:   在分布式环境下为 Euclidean $(k,z)$-clustering 构造 $(1+\varepsilon)$-coreset，在 coordinator 模型和 blackboard 模型中均达到通信复杂度的最优下界（至多差 polylog 因子）。

**[Distributionally Robust Classification for Multi-Source Unsupervised Domain Adaptation](distributionally_robust_classification_for_multi-source_unsupervised_domain_adap.md)**

:   提出一种分布鲁棒学习框架，通过联合建模目标域协变量分布和条件标签分布的不确定性，在目标数据极度稀缺或源域存在虚假相关性的UDA场景中显著提升泛化性能。

**[DA-AC: Distributions as Actions — A Unified RL Framework for Diverse Action Spaces](distributions_as_actions_a_unified_framework_for_diverse_action_spaces.md)**

:   DA-AC 提出将动作分布的参数（如 softmax 概率或 Gaussian 均值/方差）作为 Agent 的"动作"输出，将动作采样过程移入环境，从而用统一的确定性策略梯度框架处理离散/连续/混合动作空间，理论证明方差严格低于 LR 和 RP 估计器，并在 40+ 环境上取得 competitive 或 SOTA 性能。

**[Do We Really Need Permutations? Impact of Model Width on Linear Mode Connectivity](do_we_really_need_permutations_impact_of_model_width_on_linear_mode_connectivity.md)**

:   实证表明无需参数置换，仅靠增加模型宽度即可实现独立训练模型间的线性模式连通性（LMC），并提出"逐层指数加权连通性"（LEWC）解释这一现象的机理。

**[Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search](enhancing_generative_auto_bidding.md)**

:   提出 AIGB-Pearl，为生成式自动竞价方法引入离线轨迹评估器和 KL-Lipschitz 约束的分数最大化方案，使生成模型能在理论保证下安全地突破静态离线数据的性能天花板，在淘宝真实广告系统上实现 GMV +3% 的显著提升。

**[Entropic Confinement and Mode Connectivity in Overparameterized Neural Networks](entropic_confinement_and_mode_connectivity_in_overparameterized_neural_networks.md)**

:   揭示了深度网络损失景观中的"熵垒"现象：连接不同极小值的低损失路径上曲率系统性升高，与SGD噪声交互产生熵力将优化动力学限制在平坦端点附近——这解释了为何能量上连通的极小值在动力学上是有效断开的。

**[Evaluating GFlowNet from Partial Episodes for Stable and Flexible Policy-Based Training](evaluating_gflownet_from_partial_episodes_for_stable_and_flexible_policy-based_t.md)**

:   建立GFlowNet中状态流函数与策略评价函数之间的理论联系，提出子轨迹评价平衡（Sub-EB）目标用于可靠学习评价函数，增强策略基GFlowNet训练的稳定性和灵活性。

**[Exchangeability of GNN Representations with Applications to Graph Retrieval](exchangeability_gnn_representations.md)**

:   发现训练好的 GNN 节点嵌入沿特征维度是**可交换随机变量**（即 $p(X) = p(X\pi)$ 对任意维度排列 $\pi$），利用此性质通过维度排序将基于传输距离的图相似度近似为欧氏距离，构建高效的局部敏感哈希（LSH）框架 GraphHash，在子图匹配和图编辑距离检索任务上超越基线，可扩展到 100 万图语料库。

**[Explaining Grokking and Information Bottleneck through Neural Collapse Emergence](explaining_grokking_and_information_bottleneck_through_neural_collapse_emergence.md)**

:   通过 Neural Collapse 的视角统一解释 Grokking（延迟泛化）和 Information Bottleneck（压缩阶段）两大训练后期现象，证明群体类内方差的收缩是两者的共同关键因素，并揭示训练损失收敛与 Neural Collapse 发生存在由 weight decay 控制的不同时间尺度。

**[Fast and Stable Riemannian Metrics on SPD Manifolds via Cholesky Product Geometry](fast_and_stable_riemannian_metrics_on_spd_manifolds_via_cholesky_product_geometr.md)**

:   揭示Cholesky流形上的简单乘积结构，基于此提出两种快速且数值稳定的SPD度量（PCM和BWCM），所有黎曼算子均有闭式表达式，在SPD深度学习中实现效果、效率和稳定性的三重提升。

**[FastLSQ: Solving PDEs in One Shot via Fourier Features with Exact Analytical Derivatives](fastlsq_solving_pdes_in_one_shot_via_fourier_features_with_exact_analytical_deri.md)**

:   利用正弦基函数的循环导数闭式结构，实现了无需自动微分、无需迭代训练的 PDE 一次性求解框架，在线性 PDE 上 0.07s 达到 $10^{-7}$ 精度，非线性 PDE 上 <9s 达到 $10^{-8}$–$10^{-9}$ 精度，比 PINNs 快数千倍且精确数个数量级。

**[Federated ADMM from Bayesian Duality](federated_admm_from_bayesian_duality.md)**

:   从变分贝叶斯(VB)视角推导出ADMM的贝叶斯对偶结构，证明经典ADMM是VB在各向同性高斯族上的特例，并导出Newton-like（二次目标一轮收敛）和Adam-like（深度异构场景+7%准确率）两个新扩展。

**[FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability-Plasticity Tradeoff](fire_frobenius_isometry_reinitialization.md)**

:   将持续学习中的稳定性-可塑性平衡形式化为约束优化问题——最小化权重偏差（稳定性）同时约束权重正交性（可塑性），得到正交 Procrustes 问题的闭式解 $\tilde{W}^* = W(W^\top W)^{-1/2}$（极分解），通过 Newton-Schulz 迭代高效实现（<1% 额外时间），在视觉持续学习、LLM 持续预训练和 RL 上全面超越 S&P 等基线。

**[From Movement to Cognitive Maps: RNNs Reveal How Locomotor Development Shapes Hippocampal Spatial Coding](from_movement_to_cognitive_maps.md)**

:   结合幼鼠运动发育的计算分析和浅层 RNN 模型，证明运动统计特征的发育变化（爬行→行走→奔跑→成年）驱动了空间调谐神经元的序贯涌现，复现了大鼠海马空间编码的发育时间线，且具体的发育运动统计（而非简单的感觉输入加速）是位置中心空间表征涌现的关键。

**[Gaussian Certified Unlearning in High Dimensions: A Hypothesis Testing Approach](gaussian_certified_unlearning.md)**

:   提出 $(\phi,\varepsilon)$-Gaussian certifiability——基于假设检验 trade-off 函数的高维机器遗忘隐私框架，严格证明在高维比例体系 ($p \sim n$) 下单步 Newton 更新 + 校准高斯噪声即可同时满足隐私 (GPAR) 和精度 (GED→0) 要求，推翻了 Zou et al. (2025) "至少需两步 Newton" 的结论，并从理论上揭示旧 $\varepsilon$-certifiability 与噪声添加机制不兼容的根本原因。

**[GRADIEND: Feature Learning within Neural Networks Exemplified through Biases](gradiend_feature_learning_within_neural_networks_exemplified_through_biases.md)**

:   提出GRADIEND——一个基于梯度的编码器-解码器架构，通过单个瓶颈神经元从模型梯度中学习可解释的单语义特征（以性别为例），不仅可以识别哪些权重编码了特定特征，还能通过解码器直接修改模型权重来消除偏见，与INLP结合在所有基线模型上达到SOTA去偏效果。

**[Harpoon: Generalised Manifold Guidance for Conditional Tabular Diffusion](harpoon_generalised_manifold_guidance_for_conditional_tabular_diffusion.md)**

:   将流形理论从图像扩展到表格数据扩散模型，证明任意可微推理时损失的梯度都位于数据流形切线空间中（不限于平方误差损失），据此提出Harpoon方法在推理时沿流形引导无条件样本满足多样化表格约束。

**[HEEGNet: Hyperbolic Embeddings for EEG](heegnet_hyperbolic_embeddings_for_eeg.md)**

:   首次系统验证EEG数据具有双曲性（层次结构），提出HEEGNet混合双曲网络架构，结合欧几里得编码器提取时空频谱特征和双曲编码器捕捉层次关系，配合创新的粗到细域适应策略(DSMDBN)，在视觉诱发电位、情感识别和颅内EEG多个跨域任务上达到SOTA。

**[Hilbert-Guided Sparse Local Attention](hilbert-guided_sparse_local_attention.md)**

:   利用Hilbert空间填充曲线将2D图像token重排为保持空间邻近性的1D序列，大幅提升局部注意力的块稀疏率（空块比例从87.5%到96.9%），结合FlexAttention实现窗口注意力4倍和滑动注意力18倍加速，精度损失极小。

**[Human or Machine? A Preliminary Turing Test for Speech-to-Speech Interaction](human_or_machine_a_preliminary_turing_test_for_speech-to-speech_interaction.md)**

:   对9个SOTA语音对话系统开展首次语音图灵测试（2968次人类判断），发现所有系统均未通过（成功率7%-31%），瓶颈不在语义理解而在副语言特征、情感表达和对话人格，并构建了18维细粒度评估框架和可解释AI评审模型。

**[Implicit Bias and Loss of Plasticity in Matrix Completion: Depth Promotes Low-Rank](implicit_bias_and_loss_of_plasticity_in_matrix_completion_depth_promotes_low-ran.md)**

:   通过分析深度矩阵分解（深度线性网络）在矩阵补全任务中的梯度流动力学，证明了耦合动力学是深度网络低秩隐式偏差的关键机制，且深度≥3的网络除对角初始化外必然展现耦合，从而解释了深度模型为何能避免可塑性损失。

**[Implicit Bias of Per-sample Adam on Separable Data: Departure from the Full-batch Regime](implicit_bias_of_per-sample_adam_on_separable_data_departure_from_the_full-batch.md)**

:   首次证明mini-batch Adam的隐式偏差与full-batch不同：构造数据集使单样本Adam收敛到 $\ell_2$ 最大间隔分类器（而full-batch Adam收敛到 $\ell_\infty$），并通过AdamProxy刻画一般数据集上的数据自适应Mahalanobis范数间隔最大化行为。

**[Improving Black-Box Generative Attacks via Generator Semantic Consistency](improving_black-box_generative_attacks_via_generator_semantic_consistency.md)**

:   通过分析生成器中间层特征的语义退化现象，提出基于 Mean Teacher 的语义结构感知框架，在生成器早期层进行自特征蒸馏以保持语义一致性，从而增强对抗样本在跨模型、跨域、跨任务场景中的可迁移性。

**[Improving Code Localization with Repository Memory](improving_code_localization_with_repository_memory.md)**

:   通过利用代码仓库的 commit 历史构建情景记忆（过去 commit）和语义记忆（活跃代码功能摘要），增强语言代理的代码定位能力，在 SWE-bench 上取得显著提升。

**[Improving Set Function Approximation with Quasi-Arithmetic Neural Networks](improving_set_function_approximation_with_quasi-arithmetic_neural_networks.md)**

:   提出QUANN（准算术神经网络），用可逆神经网络实现可学习的Kolmogorov均值作为池化操作，首次实现机器学习版本的广义中心趋势度量，QUANN是均值可分解集合函数的通用近似器，且学到的嵌入跨任务迁移性更强。

**[In-Context Algebra](in-context_algebra.md)**

:   本文设计了一个 **in-context 代数任务**——令 token 成为纯变量、每条序列重新随机分配含义——发现 Transformer 在此设定下不再学习经典的傅里叶/几何表示，而是涌现出三种 **符号推理机制**（交换复制、单位元识别、闭包消去），并揭示了训练过程中这些能力按阶段性相变依次出现的规律。

**[Initialization Schemes for Kolmogorov-Arnold Networks: An Empirical Study](initialization_schemes_for_kolmogorov-arnold_networks_an_empirical_study.md)**

:   首次系统研究样条KAN的初始化策略，提出LeCun/Glorot启发的方差保持方案和经验幂律初始化族，通过大规模网格搜索+NTK动态分析发现幂律初始化整体最优，Glorot在参数多的模型上显著优于基线。

**[Intrinsic Training Dynamics of Deep Neural Networks](intrinsic_training_dynamics_of_deep_neural_networks.md)**

:   本文研究深度神经网络梯度流训练中，参数空间的轨迹何时可以被"提升"到低维本征空间并表示为内禀的黎曼梯度流，提出了基于守恒律的内禀可恢复性（intrinsic recoverability）准则，并将结果推广到任意深度的 ReLU 网络和线性网络。

**[Jackpot: Optimal Budgeted Rejection Sampling for Extreme Actor-Policy Mismatch RL](jackpot_optimal_budgeted_rejection_sampling_for_extreme_actor-policy_mismatch_re.md)**

:   提出 Jackpot 框架，通过 Optimal Budget Rejection Sampling（OBRS）以可控接受预算在 token 级别拒绝/重加权 rollout 样本，理论证明任意预算下都能严格缩小 actor-policy 间 KL 散度，配合 rollout 模型联合训练与蒸馏，使小模型（如 Qwen3-1.7B）rollout 训练大模型（如 Qwen3-8B）达到接近 on-policy 的性能。

**[Key and Value Weights Are Probably All You Need: On the Necessity of the Query, Key, and Value Weight Triplet in Self-Attention](key_and_value_weights_are_probably_all_you_need_on_the_necessity_of_the_query_ke.md)**

:   理论证明Transformer自注意力中Query/Key/Value权重三元组存在冗余——Query权重可被替换为单位矩阵（减少25%注意力参数），GPT风格模型从头训练验证在适当超参数调整下性能不降，且训练在3倍更低权重衰减下仍然稳定。

**[Latent Equivariant Operators for Robust Object Recognition: Promises and Challenges](latent_equivariant_operators_for_robust_object_recognition_promises_and_challeng.md)**

:   在潜空间中学习/预定义等变移位算子来处理旋转和平移等群变换，推理时通过KNN搜索推断变换参数并恢复到标准pose后分类，在MNIST上展示了训练范围外变换的成功外推能力，相比传统网络和等变网络更灵活，但向复杂数据集扩展仍面临挑战。

**[Latent Fourier Transform](latent_fourier_transform.md)**

:   将扩散自编码器与潜在空间 DFT 结合，在潜在时间序列表征上应用傅里叶变换按时间尺度分离音乐模式，训练时使用随机相关对数频率掩码让解码器学习从部分频谱信息重建，推理时用户指定频率掩码控制保留/混合的时间尺度，在条件生成和音乐融合任务上超越 ILVR/guidance/codec filtering/RAVE 等基线，29 名音乐家的听力测试确认其音质和融合能力优越。

**[LPWM: Latent Particle World Models for Object-Centric Stochastic Dynamics](latent_particle_world_models_self-supervised_object-centric_stochastic_dynamics_.md)**

:   LPWM 是首个能扩展到真实世界多物体数据集的自监督物体中心世界模型，核心创新是为每个粒子学习独立的潜在动作分布（per-particle latent actions），通过因果时空 Transformer 并行编码所有帧，支持动作/语言/图像目标/多视角等多种条件生成，在视频预测上达到 SOTA 并展示了模仿学习能力（OGBench task3 成功率 89%）。

**[LCA: Local Classifier Alignment for Continual Learning](lca_local_classifier_alignment_for_continual_learning.md)**

:   提出 Local Classifier Alignment (LCA) 损失函数，通过在类原型高斯分布的局部区域内同时最小化分类损失和损失灵敏度，解决持续学习中 backbone 增量合并后分类器不匹配的问题，配合增量 PEFT 合并策略 (IM)，在 7 个基准数据集上达到整体 85.6% 的平均精度，大幅超越 SOTA。

**[Learning Adaptive Distribution Alignment with Neural Characteristic Function for Graph Domain Adaptation](learning_adaptive_distribution_alignment_with_neural_characteristic_function_for.md)**

:   提出ADAlign框架，利用神经特征函数在谱域自适应对齐源/目标图分布——无需手动选择对齐标准，自动识别每个迁移场景中最显著的分布差异。在10个数据集16个迁移任务上达SOTA，同时降低内存和训练时间。

**[Learning on a Razor's Edge: Identifiability and Singularity of Polynomial Neural Networks](learning_on_a_razors_edge_identifiability_and_singularity_of_polynomial_neural_n.md)**

:   本文利用代数几何工具，对多项式激活的 MLP 和 CNN 进行了系统性分析：证明了 MLP 的有限可辨识性和 CNN 的唯一可辨识性，揭示了稀疏子网络对应神经流形的奇异点，并从"临界暴露性"角度给出了 MLP 稀疏偏差的几何解释——而 CNN 不具备这种偏差。

**[Learning Structure-Semantic Evolution Trajectories for Graph Domain Adaptation](learning_structure-semantic_evolution_trajectories_for_graph_domain_adaptation.md)**

:   提出DiffGDA——首个将扩散模型引入图域适应(GDA)的方法，用随机微分方程(SDE)建模源图到目标图的连续时间结构-语义联合演化过程，配合基于密度比的域感知引导网络驾驶扩散轨迹朝向目标域，理论证明收敛到最优适应路径，在8个真实数据集14个迁移任务上全面超越SOTA。

**[LipNeXt: Scaling up Lipschitz-based Certified Robustness to Billion-parameter Models](lipnext_scaling_up_lipschitz-based_certified_robustness_to_billion-parameter_mod.md)**

:   提出LipNeXt——首个无约束、无卷积的1-Lipschitz架构，通过正交流形优化学习正交矩阵 + 由Theorem 1理论驱动的Spatial Shift Module实现空间混合，成功扩展到十亿参数规模，在CIFAR-10/100、Tiny-ImageNet和ImageNet上全面刷新认证鲁棒精度(CRA) SOTA，ImageNet上 $\varepsilon=1$ 时CRA提升达+8%。

**[Lipschitz Bandits with Stochastic Delayed Feedback](lipschitz_bandits_with_stochastic_delayed_feedback.md)**

:   首次研究连续臂空间的Lipschitz bandit问题在随机延迟反馈下的学习——对有界延迟提出延迟感知zooming算法保持最优遗憾率仅多加性τ_max项，对无界延迟提出分阶段学习策略DLPP并证明近最优遗憾下界，两者均通过"lazy update"机制处理延迟观测对置信半径的非平凡影响。

**[LORE: Jointly Learning the Intrinsic Dimensionality and Relative Similarity Structure from Ordinal Data](lore_jointly_learning_the_intrinsic_dimensionality_and_relative_similarity_struc.md)**

:   提出LORE——首个同时从序数三元组比较中联合学习嵌入表示和内在维度的框架：用非凸Schatten-p拟范数(p<1)正则化替代传统的预设维度策略，通过迭代重加权(IRNN)算法求解并证明收敛到稳定点；在合成数据、LLM模拟感知实验和3个众包数据集上，LORE在维度恢复上远超所有基线方法，同时保持高三元组准确率和语义可解释性。

**[Mapping Semantic & Syntactic Relationships with Geometric Rotation](mapping_semantic_syntactic_relationships_with_geometric_rotation.md)**

:   提出RISE(Rotor-Invariant Shift Estimation)——将话语级语义-句法变换(否定/条件/礼貌)建模为嵌入空间超球面上的一致旋转操作，首次证明这些变换可跨7种语言(5个语系)+跨3种嵌入模型泛化，将线性表示假说从词级扩展到跨语言话语级。

**[Measuring Uncertainty Calibration](measuring_uncertainty_calibration.md)**

:   对二分类器L1校准误差的有限样本估计做出两个贡献：(1)证明校准函数有界变差时→基于全变差去噪的分桶方法可给出分布无关非渐近上界，(2)对任意分类器提出微小扰动(使校准函数有界二阶导)→基于核平滑器给出更紧的校准误差有限样本上界，且不显著影响分类性能→附带实用校准测量建议。

**[Missing Mass for Differentially Private Domain Discovery](missing_mass_for_differentially_private_domain_discovery.md)**

:   为差分隐私域发现问题提供首批绝对效用保证——用缺失质量(recovered mass fraction)替代基数(unique items)度量,证明简单的加权高斯机制(WGM)在Zipf数据上有近最优ℓ1缺失质量保证且有分布无关的ℓ∞保证,并将WGM作为域发现前驱用于私有top-k和k-hitting set问题获得新效用保证,实验在6个真实数据集上验证。

**[Mitigating Spurious Correlation via Distributionally Robust Learning with Hierarchical Ambiguity Sets](mitigating_spurious_correlation_via_distributionally_robust_learning_with_hierar.md)**

:   提出层次化DRO框架，同时捕获组间（group proportion shifts）和组内（intra-group distributional shifts）不确定性。使用W_∞距离在语义空间定义组内模糊集，在标准基准上达SOTA，且在新设计的少数群体分布偏移设置下——其他方法均失败时——仍保持强鲁棒性。

**[Modal Logical Neural Networks for Financial AI](modal_logical_neural_networks_for_financial_ai.md)**

:   提出模态逻辑神经网络（MLNN），将 Kripke 语义（必然/可能模态算子）集成到神经网络中，在金融合同安全审查、洗售合规和市场串谋检测中实现可审计的逻辑推理与深度学习性能的结合。

**[MoMa: A Modular Deep Learning Framework for Material Property Prediction](moma_a_modular_deep_learning_framework_for_material_property_prediction.md)**

:   提出MoMa——材料属性预测的模块化框架：先为多样化材料任务训练专用模块(full模块或adapter)集中到MoMa Hub,再通过自适应模块组合(AMC, 基于kNN表示传播+凸优化)为新任务选择最优模块加权组合后微调,在17个数据集上平均超越最强基线14%,少样本场景增益更大。

**[MOSIV: Multi-Object System Identification from Videos](mosiv_multi-object_system_identification_from_videos.md)**

:   提出MOSIV——首个从多视角视频进行多物体系统辨识的完整框架：(1) 物体感知的4D动态高斯重建每个物体的几何与运动 → (2) 高斯到连续体提升构建MPM仿真粒子 → (3) 可微MPM模拟器前向滚动+几何对齐目标(3D Chamfer + 2D轮廓)反传优化每个物体的连续材料参数($E, \nu, \mu$) → 在包含弹性/塑性/流体/沙粒四种材料的接触丰富合成基准上，PSNR 达30.51 vs OmniPhysGS 25.93，Chamfer距离降低9.4倍，建立多物体长期物理仿真新基准。

**[MT-DAO: Multi-Timescale Distributed Adaptive Optimizers with Local Updates](mt-dao_multi-timescale_distributed_adaptive_optimizers_with_local_updates.md)**

:   提出 MT-DAO，一种多时间尺度分布式自适应优化器，通过引入慢动量（高 $\beta$）来解决低频通信训练中标准动量衰减过快导致的时间尺度失配问题，首次提供了收敛保证，在语言模型预训练中消除了与全同步 DDP 的性能差距，同时减少 6-27% 的端到端训练时间。

**[Neural Force Field: Few-shot Learning of Generalized Physical Reasoning](neural_force_field_few-shot_learning_of_generalized_physical_reasoning.md)**

:   提出Neural Force Field(NFF)——将复杂物体交互表示为连续力场→通过ODE积分预测轨迹,与离散隐空间不同,NFF在低维力场中捕捉基本物理概念(重力/支撑/碰撞),仅需少量训练样本即可泛化到未见场景,支持高效的前向-后向规划和交互式精化,在I-PHYRE/N-body/PHYRE上超越所有基线。

**[NIMO: a Nonlinear Interpretable MOdel](nimo_a_nonlinear_interpretable_model.md)**

:   NIMO 提出一种混合模型 $y = \sum_j x_j \beta_j (1 + g_{\mathbf{u}_j}(\mathbf{x}_{-j}))$，在保留线性回归系数全局可解释性（通过均值边际效应 MEM）的同时，利用神经网络提供逐实例的非线性修正，并通过参数消去法高效联合优化线性系数和网络参数。

**[Noise-Aware Generalization: Robustness to In-Domain Noise and Out-of-Domain Generalization](noise-aware_generalization_robustness_to_in-domain_noise_and_out-of-domain_gener.md)**

:   首次系统研究噪声感知泛化(NAG)——标签噪声和域偏移共存时的学习→分析DG方法因噪声失效/LNL方法将域偏移误认为噪声→提出DL4ND利用跨域比较(而非单域内)检测噪声(因域内可能有共享的伪特征误导→跨域更可靠)→在7个数据集上超越DG/LNL方法及其组合达12.5%。

**[Noisy-Pair Robust Representation Alignment for Positive-Unlabeled Learning](noisy-pair_robust_representation_alignment_for_positive-unlabeled_learning.md)**

:   提出NcPU框架解决PU学习中判别性表示学习的瓶颈：(1) NoiSNCL噪声对鲁棒的非对比损失使clean pair梯度主导训练；(2) PhantomGate伪标签消歧提供保守负标签。两者在EM框架下迭代互利，在CIFAR-100上将差距（vs 监督学习）从14.26%缩至接近0。

**[Non-Clashing Teaching in Graphs: Algorithms, Complexity, and Bounds](non-clashing_teaching_in_graphs_algorithms_complexity_and_bounds.md)**

:   研究图中闭邻域概念类的非冲突教学问题，提供精确匹配的算法上下界（N-NCTD⁺ 的 $2^{\mathcal{O}(|E|)}$ 紧界）、对 treedepth/vertex cover 参数化的 FPT 算法（含首个负面标签 FPT 结果），以及平面图和单位正方形图的组合上界，全面推进了非冲突教学的计算与组合理解。

**[Non-Collaborative User Simulators for Tool Agents](non-collaborative_user_simulators_for_tool_agents.md)**

:   提出四类非协作用户行为模拟框架（不可用服务/跑题/不耐烦/不完整表述），在MultiWOZ和τ-bench上揭示SOTA工具Agent在面对非协作用户时性能显著下降（平均-29% tangential模式），暴露了幻觉增加和对话崩溃的系统性弱点。

**[On the Impact of the Utility in Semivalue-based Data Valuation](on_the_impact_of_the_utility_in_semivalue-based_data_valuation.md)**

:   提出数据集空间签名概念和鲁棒性度量R_p，将数据点嵌入低维空间使效用变为线性泛函，揭示半值数据估值对效用选择的几何敏感性，Banzhaf在多数据集上一致最鲁棒。

**[On the Lipschitz Continuity of Set Aggregation Functions and Neural Networks for Sets](on_the_lipschitz_continuity_of_set_aggregation_functions_and_neural_networks_for.md)**

:   系统研究了三种常用集合聚合函数（sum/mean/max）和注意力机制在三种多集距离函数下的Lipschitz连续性，推导出集合神经网络的Lipschitz常数上界，并将其与扰动稳定性和分布偏移泛化联系起来。

**[Optimal Transport-Induced Samples against Out-of-Distribution Overconfidence](optimal_transport-induced_samples_against_out-of-distribution_overconfidence.md)**

:   利用半离散OT几何奇异性(传输方向突变处)定位语义歧义区域，构造OTIS(OT诱导OOD样本)并用置信度抑制训练→系统缓解DNN对OOD的过度自信，多架构多设定下全面超越SOTA且不损ID性能。

**[Optimizer Choice Matters for the Emergence of Neural Collapse](optimizer_choice_matters_for_the_emergence_of_neural_collapse.md)**

:   通过 3,900+ 次训练实验和理论分析，揭示了优化器选择（特别是权重衰减的耦合方式）对 Neural Collapse 现象涌现起关键决定性作用——AdamW（解耦权重衰减）无法产生 Neural Collapse，而 SGD 和 Adam（耦合权重衰减）可以。

**[Out of the Shadows: Exploring a Latent Space for Neural Network Verification](out_of_the_shadows_exploring_a_latent_space_for_neural_network_verification.md)**

:   提出一种基于潜空间（latent space）的规范驱动输入细化方法，通过在高维潜空间中转移输出约束到输入空间，显著减少分支定界过程中的子问题数量，实现高效GPU加速的神经网络验证工具。

**[Oversmoothing, Oversquashing, Heterophily, Long-Range, and more: Demystifying Common Beliefs in Graph Machine Learning](oversmoothing_oversquashing_heterophily_long-range_and_more_demystifying_common_.md)**

:   系统梳理并反驳了图机器学习中关于过平滑（OSM）、过挤压（OSQ）、异质性和长程依赖的9个常见但不总成立的"信念"，通过简洁反例推动社区更精确地理解和表述这些概念。

**[OwlEye: Zero-Shot Learner for Cross-Domain Graph Data Anomaly Detection](owleye_zero-shot_learner_for_cross-domain_graph_data_anomaly_detection.md)**

:   提出OwlEye框架，通过跨域特征对齐、多域多模式字典学习和截断注意力重建三个模块，实现了在完全未见图上的零样本异常检测，且支持无需重训练的持续学习。

**[Perturbation-Induced Linearization: Constructing Unlearnable Data with Solely Linear Classifiers](perturbation-induced_linearization_constructing_unlearnable_data_with_solely_lin.md)**

:   提出PIL方法，仅使用无偏置线性分类器作为代理模型生成不可学习扰动，通过诱导深度模型线性化来阻止其学习语义特征，比现有方法快100倍以上（CIFAR-10上不到1分钟GPU时间）。

**[PlanetAlign: A Comprehensive Python Library for Benchmarking Network Alignment](planetalign_a_comprehensive_python_library_for_benchmarking_network_alignment.md)**

:   提出PlanetAlign，一个集成18个数据集、14种方法和标准化评估流程的PyTorch网络对齐基准库，首次覆盖一致性方法、嵌入方法和最优传输方法三大类，支持有效性、可扩展性和鲁棒性的全面评估。

**[PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression](polyshap_extending_kernelshap_with_interaction-informed_polynomial_regression.md)**

:   本文提出 PolySHAP，通过将 KernelSHAP 的线性近似扩展为高阶多项式回归来捕获特征间的非线性交互，从而提升 Shapley 值的估计精度；并从理论上证明了配对采样（paired sampling）等价于二阶 PolySHAP，首次解释了配对采样启发式方法优越性能的根本原因。

**[Predicting Kernel Regression Learning Curves from Only Raw Data Statistics](predicting_kernel_regression_learning_curves_from_only_raw_data_statistics.md)**

:   提出 Hermite 特征结构假设（HEA），仅用数据协方差矩阵和目标函数的 Hermite 分解两个统计量，就能解析预测旋转不变核在真实图像数据集（CIFAR-5m、SVHN、ImageNet）上的学习曲线（测试误差 vs 样本量），并证明该假设在高斯数据下成立，且 MLP 在特征学习 regime 下也按 HEA 预测的顺序学习 Hermite 多项式。

**[Probabilistic Kernel Function for Fast Angle Testing](probabilistic_kernel_function_for_fast_angle_testing.md)**

:   本文研究高维欧氏空间中的角度测试问题，提出两个基于参考角度的确定性概率核函数 $K_S^1$ 和 $K_S^2$，分别用于角度比较和角度阈值判断，无需高斯分布的渐近假设即可获得理论保证，并将其应用于近似最近邻搜索（ANNS），在 HNSW 图上实现 2.5×–3× 的 QPS 加速。

**[Provably Explaining Neural Additive Models](provably_explaining_neural_additive_models.md)**

:   针对 Neural Additive Models (NAMs) 设计了专用的高效解释算法，仅需对数级别的验证查询即可生成可证明的基数最小解释（cardinally-minimal explanations），在速度和解释质量上均超越了现有的通用子集最小解释算法。

**[RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs](radar_reasoning-ability_and_difficulty-aware_routing_for_reasoning_llms.md)**

:   本文提出 Radar 框架，将推理语言模型（RLM）的自适应推理问题建模为多目标优化，利用项目反应理论（IRT）联合估计可解释的查询难度和模型配置能力参数，实现轻量级、可扩展的查询级路由，在 8 个推理基准上优于 SOTA 路由方法，且仅增加约 7ms 延迟。

**[RECON: Robust symmetry discovery via Explicit Canonical Orientation Normalization](recon_robust_symmetry_discovery_via_explicit_canonical_orientation_normalization.md)**

:   提出 RECON，一种类-姿态无关的正则化方向归一化方法，通过简单的右平移（right translation）修正任意训练过程中产生的正则化表示，实现无监督的实例级对称性发现、OOD 姿态检测以及即插即用的测试时正则化层。

**[Redirection for Erasing Memory (REM): Towards a Universal Unlearning Method for Corrupted Data](redirection_for_erasing_memory_rem_towards_a_universal_unlearning_method_for_cor.md)**

:   本文提出损坏数据遗忘任务的二维分类框架（发现率 × 统计规律性），揭示了现有遗忘方法各自仅在特定区域有效的局限，并提出 REM（重定向以擦除记忆）方法，通过将损坏数据重定向到新增的专用网络容量再丢弃，首次在整个二维任务空间中实现强劲且一致的遗忘性能。

**[Reducing Class-Wise Performance Disparity via Margin Regularization](reducing_class-wise_performance_disparity_via_margin_regularization.md)**

:   提出 MR2（Margin Regularization for performance disparity Reduction），通过在 logit 和表征空间动态调整类别相关的 margin，基于理论推导的泛化界减少类间性能差异，同时提升整体准确率。

**[Revisiting Sharpness-Aware Minimization: A More Faithful and Effective Implementation](revisiting_sharpness-aware_minimization_a_more_faithful_and_effective_implementa.md)**

:   对 SAM 的底层机制提出新的直觉解释——扰动点梯度近似局部最大值方向，并揭示其不精确性及多步退化问题，进而提出 XSAM 通过显式估计最大值方向实现更忠实更有效的锐度感知最小化。

**[Scalable Random Wavelet Features: Efficient Non-Stationary Kernel Approximation with Convergence Guarantees](scalable_random_wavelet_features_efficient_non-stationary_kernel_approximation_w.md)**

:   提出 Random Wavelet Features (RWF)，通过从小波族中随机采样构建可扩展的非平稳核近似，保留随机特征的线性时间复杂度，同时具有正定性、无偏性和一致收敛保证。

**[SEED: Towards More Accurate Semantic Evaluation for Visual Brain Decoding](seed_towards_more_accurate_semantic_evaluation_for_visual_brain_decoding.md)**

:   提出 SEED（Semantic Evaluation for Visual Brain Decoding），一个结合 Object F1、Cap-Sim 和 EffNet 三个互补指标的组合评估度量，在与人类评估的对齐度上显著超越现有所有指标。

**[Soft Quality-Diversity Optimization](soft_quality-diversity_optimization.md)**

:   提出 Soft QD Score 作为无需行为空间离散化的质量多样性优化新目标，并据此推导出可微分算法 SQUAD，在高维行为空间中具有更好的可扩展性，且在标准基准上与 SOTA 竞争力相当。

**[Speculative Actions: A Lossless Framework for Faster AI Agents](speculative_actions_faster_ai_agents.md)**

:   借鉴 CPU 推测执行和 LLM 推测解码的思想，提出 Speculative Actions 框架：在慢速 Actor（大模型）计算时用快速 Speculator（小模型）预测未来动作并预执行，匹配时跳过等待实现无损加速，在 Chess/电商/问答等场景实现 15-30% 延迟降低，置信度动态分支策略用 40% 更少 token 达到近似 3 条推测的加速效果。

**[t-SNE Exaggerates Clusters, Provably](t-sne_exaggerates_clusters_provably.md)**

:   从理论上严格证明 t-SNE 存在两个根本性失败模式：（1）无法从输出推断输入聚类的强度，（2）无法忠实地展示极端离群点——即使输入毫无聚类结构或存在极端离群点，t-SNE 也可能产生完美聚类的可视化。

**[TabStruct: Measuring Structural Fidelity of Tabular Data](tabstruct_measuring_structural_fidelity_of_tabular_data.md)**

:   提出 TabStruct 评估框架和 global utility 指标，在不需要真实因果图的情况下衡量表格数据生成器对因果结构的保真度，在 29 个数据集上系统比较 13 种生成器，发现扩散模型在全局结构保持上显著优于其他方法。

**[The Counting Power of Transformers](the_counting_power_of_transformers.md)**

:   证明 Transformer 不仅能捕获（半）线性计数性质，还能表达所有**半代数计数性质**（即多元多项式不等式的布尔组合），从而推广了先前关于 Transformer 计数能力的所有结果，并由此推导出新的不可判定性结论。

**[The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?](the_hot_mess_of_ai_how_does_misalignment_scale_with_model_intelligence_and_task_.md)**

:   将AI模型错误分解为偏差（systematic misalignment）和方差（incoherent behavior），发现：推理越长→越不连贯；更大模型在困难任务上更不连贯。这暗示未来超级AI更可能表现为"工业事故"式的不可预测失败，而非一致追求错误目标。

**[The Invisibility Hypothesis: Promises of AGI and the Future of the Global South](the_invisibility_hypothesis_promises_of_agi_and_the_future_of_the_global_south.md)**

:   本文提出"不可见性假说"（Invisibility Hypothesis），论证随着AI系统日益成为经济和政治分配的协调层，全球南方的大量人口——特别是非正式工人和小规模生产者——将因缺乏数字可验证性而被系统性排斥（managed exclusion），从被剥削转为被忽略，风险不仅是失业而是整体相关性的丧失。

**[The Price of Robustness: Stable Classifiers Need Overparameterization](the_price_of_robustness_stable_classifiers_need_overparameterization.md)**

:   建立了不连续分类器的稳定性-泛化界，证明了分类任务中的"鲁棒性代价定律"：任何参数量 $p \approx n$ 的插值分类器必然不稳定，实现高稳定性需要 $p \approx nd$ 量级的过参数化。

**[There Was Never a Bottleneck in Concept Bottleneck Models](there_was_never_a_bottleneck_in_concept_bottleneck_models.md)**

:   指出概念瓶颈模型（CBM）实际上并不存在真正的"瓶颈"——表征变量 $z_j$ 能预测概念 $c_j$ 不意味着它只编码 $c_j$ 的信息。提出 MCBM（Minimal Concept Bottleneck Model），通过信息瓶颈正则化约束每个 $z_j$ 仅保留对应概念的信息，实现真正的解耦表征和可靠的概念干预。

**[Towards Anomaly-Aware Pre-Training and Fine-Tuning for Graph Anomaly Detection](towards_anomaly-aware_pre-training_and_fine-tuning_for_graph_anomaly_detection.md)**

:   提出 APF 框架，通过 Rayleigh 商引导的异常感知预训练和粒度自适应微调，解决图异常检测中标签稀缺和同质性差异的双重挑战。

**[Towards Sustainable Investment Policies Informed by Opponent Shaping](towards_sustainable_investment_policies_informed_by_opponent_shaping.md)**

:   形式化证明 InvestESG 模拟环境在何种条件下构成社会困境，并应用 Advantage Alignment 对抗塑形算法引导经济智能体走向可持续投资均衡。

**[Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition](training_deep_normalization-free_spiking_neural_networks_with_lateral_inhibition.md)**

:   提出基于皮层兴奋-抑制（E-I）回路的无归一化学习框架 DeepEISNN，通过 E-I Init 和 E-I Prop 两项技术实现深度 SNN 的稳定端到端训练，兼顾性能与生物合理性。

**[Understanding and Improving Shampoo and SOAP via Kullback-Leibler Minimization](understanding_and_improving_shampoo_and_soap_via_kullback-leibler_minimization.md)**

:   从 KL 散度最小化角度重新解释 Shampoo 和 SOAP 的结构化二阶矩估计，揭示其固有局限，并提出 KL-Shampoo 和 KL-SOAP 两种实用方案，在无需 Adam grafting 的情况下匹配或超越原始方法。

**[Unlearning Evaluation through Subset Statistical Independence](unlearning_evaluation_through_subset_statistical_independence.md)**

:   提出 Split-half Dependence Evaluation (SDE)，利用 HSIC 统计独立性检验在子集级别评估机器遗忘效果，无需重训模型或辅助分类器。

**[When and Where to Reset Matters for Long-Term Test-Time Adaptation](when_and_where_to_reset_matters_for_long-term_test-time_adaptation.md)**

:   ASR提出自适应选择性重置方案，通过预测集中度 $\mathcal{C}_t$ 动态判断何时重置（避免固定周期的次优性），通过从output层向input层渐进的层选择策略判断重置哪些层（保留有价值的适应知识），配合importance-aware正则化恢复被重置的关键知识和on-the-fly适应调整，在CCC-Hard上比SOTA提升44.12%。

**[When Machine Learning Gets Personal: Evaluating Prediction and Explanation](when_machine_learning_gets_personal_evaluating_prediction_and_explanation.md)**

:   本文提出统一框架量化模型个性化对预测准确性和解释质量的影响，证明二者可以分离（预测不变但解释变好/变差），推导了基于数据集统计量的假设检验误差概率有限样本下界，揭示了许多实际场景中个性化效果在统计上根本不可检验。

**[When to Retrain after Drift: A Data-Only Test of Post-Drift Data Size Sufficiency](when_to_retrain_after_drift_a_data-only_test_of_post-drift_data_size_sufficiency.md)**

:   CALIPER提出了一种检测器和模型无关的、仅依赖数据的检验方法，通过跟踪加权局部回归的代理误差随局部性参数$\theta$的单调性变化，来估计突发概念漂移后重训练所需的最小数据量，无需实际重训练下游模型。
