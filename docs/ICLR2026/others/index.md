---
title: >-
  ICLR2026 其他方向 69篇论文解读
description: >-
  69篇ICLR2026 其他方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**🔬 ICLR2026** · 共 **69** 篇

**[A Federated Generalized Expectation-Maximization Algorithm For Mixture Models Wi](a_federated_generalized_expectation-maximization_algorithm_for_mixture_models_wi.md)**

:   提出 FedGEM 算法，通过客户端本地 EM 步后构建不确定性集、服务器利用不确定性集交集检测聚类重叠并推断全局聚类数，首次实现在全局聚类数未知情况下的联邦聚类，并提供了概率收敛保证。

**[A Representer Theorem For Hawkes Processes Via Penalized Least Squares Minimizat](a_representer_theorem_for_hawkes_processes_via_penalized_least_squares_minimizat.md)**

:   为线性多元 Hawkes 过程在 RKHS 框架下的触发核估计建立了新型表示定理，证明最优估计器可用等价核在数据点上的线性组合表示且对偶系数全部解析地等于 1，无需求解对偶优化问题，从而实现高效可扩展的非参数估计。

**[A Scalable Inter-Edge Correlation Modeling In Copulagnn For Link Sign Prediction](a_scalable_inter-edge_correlation_modeling_in_copulagnn_for_link_sign_prediction.md)**

:   将 CopulaGNN 从节点级扩展到边级，通过将相关矩阵构造为边嵌入的 Gramian 矩阵并利用 Woodbury 恒等式重构条件概率分布，实现了在签名图上对边间统计依赖的可扩展建模，用于链接符号预测任务。

**[A Single Architecture For Representing Invariance Under Any Space Group](a_single_architecture_for_representing_invariance_under_any_space_group.md)**

:   设计了一种可自适应任意空间群不变性的单一架构 (Crystal Fourier Transformer)，通过解析推导群操作对傅里叶系数的约束来构造对称适配的傅里叶基，用约束的对偶图表示实现了跨 230 个空间群的参数共享和零样本泛化。

**[Active Learning For Decision Trees With Provable Guarantees](active_learning_for_decision_trees_with_provable_guarantees.md)**

:   为决策树主动学习提供首个理论保证：(1) 首次分析决策树的不一致系数（disagreement coefficient）并给出 $O(\ln^{OPT}(n))$ 上界；(2) 提出首个达到乘法误差 $(1+\epsilon)$ 保证的二分类主动学习算法；结合两者实现数据集大小的多对数标签复杂度。

**[Addressing Divergent Representations Causal](addressing_divergent_representations_causal.md)**

:   系统性地揭示因果干预（activation patching、DAS、SAE 等）会将模型内部表征推离自然分布，理论区分"无害偏移"与"有害偏移"两类情况，并提出 Counterfactual Latent (CL) loss 来约束干预表征不偏离流形，在 7B LLM 上验证可减少偏移同时保持干预准确率。

**[Agnostics Learning To Code In Any Programming Language Via Reinforcement With A ](agnostics_learning_to_code_in_any_programming_language_via_reinforcement_with_a_.md)**

:   提出Agnostics，一种语言无关的后训练pipeline：将编程任务统一为I/O行为规范格式，用通用验证器+GRPO强化学习训练LLM在任何编程语言上编码，使Qwen 4B在Lua/Julia/R/OCaml/Fortran五种低资源语言上达到匹敌16B-70B模型的SOTA水平。

**[An Information-Theoretic Framework For Optimizing Experimental Design To Disting](an_information-theoretic_framework_for_optimizing_experimental_design_to_disting.md)**

:   提出"信息间隙"（information gap）框架，通过优化刺激分布来最大化似然编码（likelihood code）与后验编码（posterior code）假设之间的可区分性，推导出真实后验与任务边缘化代理后验之间的KL散度作为优化目标，并通过DNN解码器在模拟神经群体上验证了该框架的有效性，揭示传统单上下文实验无法区分两种编码假设。

**[Ano Faster Is Better In Noisy Landscape](ano_faster_is_better_in_noisy_landscape.md)**

:   提出 Ano 优化器，将更新方向和幅度解耦——方向用动量的符号（sign）确保噪声鲁棒，幅度用瞬时梯度绝对值（而非动量幅度）确保响应速度，配合改进的 Yogi 式方差估计，在噪声和非平稳环境（如 RL）中显著优于 Adam/Lion/Adan，同时在标准任务上保持竞争力。

**[Anyup Universal Feature Upsampling](anyup_universal_feature_upsampling.md)**

:   提出AnyUp——首个推理时encoder无关的可学习特征上采样方法，通过feature-agnostic层处理任意维度/类型的视觉特征，配合窗口注意力架构和crop-based训练策略，训练一次即可对任意视觉编码器（DINO/CLIP/SigLIP/MAE等）的特征进行任意分辨率上采样，在多个下游任务上超越FeatUp/JAFAR/LoftUp等方法。

**[Articulation In Motion Prior-Free Part Mobility Analysis For Articulated Objects](articulation_in_motion_prior-free_part_mobility_analysis_for_articulated_objects.md)**

:   提出AiM（Articulation in Motion）框架，从交互视频和初始状态扫描中无需部件数量先验地重建铰接物体——通过双高斯表征（静态GS + 可变形GS）实现动静解耦，结合顺序RANSAC进行无先验部件分割和关节估计，辅以SDMD模块处理新暴露的静态区域，在复杂6部件物体（Storage）上以79.34% mean IoU大幅超越需先验的ArtGS（52.23%）。

**[Cadrift A Time-Dependent Causal Generator Of Drifting Data Streams](cadrift_a_time-dependent_causal_generator_of_drifting_data_streams.md)**

:   提出 CaDrift，一个基于结构因果模型（SCM）的时间依赖合成数据流生成框架，通过 EWMA 平滑和自回归噪声引入时序相关性，并通过修改因果映射函数实现可控的分布漂移、协变量漂移、严重漂移和局部漂移，填补了现有数据流生成器既不因果又不时序依赖的空白。

**[Characterizing And Optimizing The Spatial Kernel Of Multi Resolution Hash Encodi](characterizing_and_optimizing_the_spatial_kernel_of_multi_resolution_hash_encodi.md)**

:   从物理系统角度分析 Instant-NGP 的多分辨率哈希编码（MHE），推导出其点扩展函数（PSF）的闭式近似，发现有效分辨率由平均分辨率 $N_{\text{avg}}$ 而非最细分辨率 $N_{\max}$ 决定，且存在网格引起的各向异性，并提出零开销的 Rotated MHE（R-MHE）通过逐层旋转输入坐标消除各向异性。

**[Chlu The Causal Hamiltonian Learning Unit As A Symplectic Primitive For Deep Lea](chlu_the_causal_hamiltonian_learning_unit_as_a_symplectic_primitive_for_deep_lea.md)**

:   CHLU 是一种基于相对论哈密顿力学和辛积分的计算学习原语，通过强制相空间体积守恒和引入因果速度上限，解决了 LSTM 的梯度爆炸/消失和 Neural ODE 的信息耗散问题，实现无限时域稳定性和热力学生成能力。

**[Completing Missing Annotation Multi-Agent Debate For Accurate And Scalable Relev](completing_missing_annotation_multi-agent_debate_for_accurate_and_scalable_relev.md)**

:   提出DREAM框架——用对立立场初始化的双Agent多轮辩论进行IR相关性标注，达到95.2%准确率且仅3.5%案例需人工介入。据此构建BRIDGE基准，发现29,824个缺失标注（原有标注的428%），修正了检索系统排名偏差和检索-生成性能不匹配。

**[Compositional Diffusion Long Horizon Planning](compositional_diffusion_long_horizon_planning.md)**

:   提出 CDGS（Compositional Diffusion with Guided Search），通过在扩散去噪过程中嵌入基于种群的搜索机制（迭代重采样 + 似然剪枝），解决组合式扩散模型在多模态局部分布合成时的模式平均问题，从短时域模型采样出全局一致的长时域规划。

**[Consistent Low-Rank Approximation](consistent_low-rank_approximation.md)**

:   提出并系统研究"一致低秩近似"问题——在流数据中逐行到达的矩阵上维护近最优 rank-$k$ 近似的同时最小化解的总变化量（recourse），证明加性误差下 $O(k/\varepsilon \cdot \log(nd))$ recourse 可行，乘性 $(1+\varepsilon)$ 误差下 $k^{3/2}/\varepsilon^2 \cdot \text{polylog}$ recourse 可行，并给出 $\Omega(k/\varepsilon \cdot \log(n/k))$ 的下界。

**[Directional Sheaf Hypergraph Networks Unifying Learning On Directed And Undirect](directional_sheaf_hypergraph_networks_unifying_learning_on_directed_and_undirect.md)**

:   本文提出 Directional Sheaf Hypergraph Networks (DSHN)，通过将 Cellular Sheaf 理论与有向超图的方向信息结合，构造了一种复值 Hermitian Laplacian 算子，统一并推广了现有的图和超图 Laplacian，在 7 个真实数据集上相对准确率提升 2%–20%。

**[Distributed Algorithms For Euclidean Clustering](distributed_algorithms_for_euclidean_clustering.md)**

:   在分布式环境下为 Euclidean $(k,z)$-clustering 构造 $(1+\varepsilon)$-coreset，在 coordinator 模型和 blackboard 模型中均达到通信复杂度的最优下界（至多差 polylog 因子）。

**[Distributionally Robust Classification For Multi-Source Unsupervised Domain Adap](distributionally_robust_classification_for_multi-source_unsupervised_domain_adap.md)**

:   提出一种分布鲁棒学习框架，通过联合建模目标域协变量分布和条件标签分布的不确定性，在目标数据极度稀缺或源域存在虚假相关性的UDA场景中显著提升泛化性能。

**[Distributions As Actions A Unified Framework For Diverse Action Spaces](distributions_as_actions_a_unified_framework_for_diverse_action_spaces.md)**

:   DA-AC 提出将动作分布的参数（如 softmax 概率或 Gaussian 均值/方差）作为 Agent 的"动作"输出，将动作采样过程移入环境，从而用统一的确定性策略梯度框架处理离散/连续/混合动作空间，理论证明方差严格低于 LR 和 RP 估计器，并在 40+ 环境上取得 competitive 或 SOTA 性能。

**[Enhancing Generative Auto Bidding](enhancing_generative_auto_bidding.md)**

:   提出 AIGB-Pearl，为生成式自动竞价方法引入离线轨迹评估器和 KL-Lipschitz 约束的分数最大化方案，使生成模型能在理论保证下安全地突破静态离线数据的性能天花板，在淘宝真实广告系统上实现 GMV +3% 的显著提升。

**[Entropic Confinement And Mode Connectivity In Overparameterized Neural Networks](entropic_confinement_and_mode_connectivity_in_overparameterized_neural_networks.md)**

:   揭示了深度网络损失景观中的"熵垒"现象：连接不同极小值的低损失路径上曲率系统性升高，与SGD噪声交互产生熵力将优化动力学限制在平坦端点附近——这解释了为何能量上连通的极小值在动力学上是有效断开的。

**[Evaluating Gflownet From Partial Episodes For Stable And Flexible Policy-Based T](evaluating_gflownet_from_partial_episodes_for_stable_and_flexible_policy-based_t.md)**

:   建立GFlowNet中状态流函数与策略评价函数之间的理论联系，提出子轨迹评价平衡（Sub-EB）目标用于可靠学习评价函数，增强策略基GFlowNet训练的稳定性和灵活性。

**[Exchangeability of GNN Representations with Applications to Graph Retrieval](exchangeability_gnn_representations.md)**

:   发现训练好的 GNN 节点嵌入沿特征维度是**可交换随机变量**（即 $p(X) = p(X\pi)$ 对任意维度排列 $\pi$），利用此性质通过维度排序将基于传输距离的图相似度近似为欧氏距离，构建高效的局部敏感哈希（LSH）框架 GraphHash，在子图匹配和图编辑距离检索任务上超越基线，可扩展到 100 万图语料库。

**[Fast And Stable Riemannian Metrics On Spd Manifolds Via Cholesky Product Geometr](fast_and_stable_riemannian_metrics_on_spd_manifolds_via_cholesky_product_geometr.md)**

:   揭示Cholesky流形上的简单乘积结构，基于此提出两种快速且数值稳定的SPD度量（PCM和BWCM），所有黎曼算子均有闭式表达式，在SPD深度学习中实现效果、效率和稳定性的三重提升。

**[Fastlsq Solving Pdes In One Shot Via Fourier Features With Exact Analytical Deri](fastlsq_solving_pdes_in_one_shot_via_fourier_features_with_exact_analytical_deri.md)**

:   利用正弦基函数的循环导数闭式结构，实现了无需自动微分、无需迭代训练的 PDE 一次性求解框架，在线性 PDE 上 0.07s 达到 $10^{-7}$ 精度，非线性 PDE 上 <9s 达到 $10^{-8}$–$10^{-9}$ 精度，比 PINNs 快数千倍且精确数个数量级。

**[Federated Admm From Bayesian Duality](federated_admm_from_bayesian_duality.md)**

:   从变分贝叶斯(VB)视角推导出ADMM的贝叶斯对偶结构，证明经典ADMM是VB在各向同性高斯族上的特例，并导出Newton-like（二次目标一轮收敛）和Adam-like（深度异构场景+7%准确率）两个新扩展。

**[Fire Frobenius Isometry Reinitialization](fire_frobenius_isometry_reinitialization.md)**

:   将持续学习中的稳定性-可塑性平衡形式化为约束优化问题——最小化权重偏差（稳定性）同时约束权重正交性（可塑性），得到正交 Procrustes 问题的闭式解 $\tilde{W}^* = W(W^\top W)^{-1/2}$（极分解），通过 Newton-Schulz 迭代高效实现（<1% 额外时间），在视觉持续学习、LLM 持续预训练和 RL 上全面超越 S&P 等基线。

**[From Movement to Cognitive Maps: RNNs Reveal How Locomotor Development Shapes Hippocampal Spatial Coding](from_movement_to_cognitive_maps.md)**

:   结合幼鼠运动发育的计算分析和浅层 RNN 模型，证明运动统计特征的发育变化（爬行→行走→奔跑→成年）驱动了空间调谐神经元的序贯涌现，复现了大鼠海马空间编码的发育时间线，且具体的发育运动统计（而非简单的感觉输入加速）是位置中心空间表征涌现的关键。

**[Harpoon Generalised Manifold Guidance For Conditional Tabular Diffusion](harpoon_generalised_manifold_guidance_for_conditional_tabular_diffusion.md)**

:   将流形理论从图像扩展到表格数据扩散模型，证明任意可微推理时损失的梯度都位于数据流形切线空间中（不限于平方误差损失），据此提出Harpoon方法在推理时沿流形引导无条件样本满足多样化表格约束。

**[Heegnet Hyperbolic Embeddings For Eeg](heegnet_hyperbolic_embeddings_for_eeg.md)**

:   首次系统验证EEG数据具有双曲性（层次结构），提出HEEGNet混合双曲网络架构，结合欧几里得编码器提取时空频谱特征和双曲编码器捕捉层次关系，配合创新的粗到细域适应策略(DSMDBN)，在视觉诱发电位、情感识别和颅内EEG多个跨域任务上达到SOTA。

**[Hilbert-Guided Sparse Local Attention](hilbert-guided_sparse_local_attention.md)**

:   利用Hilbert空间填充曲线将2D图像token重排为保持空间邻近性的1D序列，大幅提升局部注意力的块稀疏率（空块比例从87.5%到96.9%），结合FlexAttention实现窗口注意力4倍和滑动注意力18倍加速，精度损失极小。

**[Implicit Bias Of Per-Sample Adam On Separable Data Departure From The Full-Batch](implicit_bias_of_per-sample_adam_on_separable_data_departure_from_the_full-batch.md)**

:   首次证明mini-batch Adam的隐式偏差与full-batch不同：构造数据集使单样本Adam收敛到 $\ell_2$ 最大间隔分类器（而full-batch Adam收敛到 $\ell_\infty$），并通过AdamProxy刻画一般数据集上的数据自适应Mahalanobis范数间隔最大化行为。

**[Improving Black-Box Generative Attacks Via Generator Semantic Consistency](improving_black-box_generative_attacks_via_generator_semantic_consistency.md)**

:   通过分析生成器中间层特征的语义退化现象，提出基于 Mean Teacher 的语义结构感知框架，在生成器早期层进行自特征蒸馏以保持语义一致性，从而增强对抗样本在跨模型、跨域、跨任务场景中的可迁移性。

**[In-Context Algebra](in-context_algebra.md)**

:   本文设计了一个 **in-context 代数任务**——令 token 成为纯变量、每条序列重新随机分配含义——发现 Transformer 在此设定下不再学习经典的傅里叶/几何表示，而是涌现出三种 **符号推理机制**（交换复制、单位元识别、闭包消去），并揭示了训练过程中这些能力按阶段性相变依次出现的规律。

**[Jackpot Optimal Budgeted Rejection Sampling For Extreme Actor-Policy Mismatch Re](jackpot_optimal_budgeted_rejection_sampling_for_extreme_actor-policy_mismatch_re.md)**

:   提出 Jackpot 框架，通过 Optimal Budget Rejection Sampling（OBRS）以可控接受预算在 token 级别拒绝/重加权 rollout 样本，理论证明任意预算下都能严格缩小 actor-policy 间 KL 散度，配合 rollout 模型联合训练与蒸馏，使小模型（如 Qwen3-1.7B）rollout 训练大模型（如 Qwen3-8B）达到接近 on-policy 的性能。

**[Key And Value Weights Are Probably All You Need On The Necessity Of The Query Ke](key_and_value_weights_are_probably_all_you_need_on_the_necessity_of_the_query_ke.md)**

:   理论证明Transformer自注意力中Query/Key/Value权重三元组存在冗余——Query权重可被替换为单位矩阵（减少25%注意力参数），GPT风格模型从头训练验证在适当超参数调整下性能不降，且训练在3倍更低权重衰减下仍然稳定。

**[Latent Equivariant Operators For Robust Object Recognition Promises And Challeng](latent_equivariant_operators_for_robust_object_recognition_promises_and_challeng.md)**

:   在潜空间中学习/预定义等变移位算子来处理旋转和平移等群变换，推理时通过KNN搜索推断变换参数并恢复到标准pose后分类，在MNIST上展示了训练范围外变换的成功外推能力，相比传统网络和等变网络更灵活，但向复杂数据集扩展仍面临挑战。

**[Latent Fourier Transform](latent_fourier_transform.md)**

:   将扩散自编码器与潜在空间 DFT 结合，在潜在时间序列表征上应用傅里叶变换按时间尺度分离音乐模式，训练时使用随机相关对数频率掩码让解码器学习从部分频谱信息重建，推理时用户指定频率掩码控制保留/混合的时间尺度，在条件生成和音乐融合任务上超越 ILVR/guidance/codec filtering/RAVE 等基线，29 名音乐家的听力测试确认其音质和融合能力优越。

**[Latent Particle World Models Self-Supervised Object-Centric Stochastic Dynamics ](latent_particle_world_models_self-supervised_object-centric_stochastic_dynamics_.md)**

:   LPWM 是首个能扩展到真实世界多物体数据集的自监督物体中心世界模型，核心创新是为每个粒子学习独立的潜在动作分布（per-particle latent actions），通过因果时空 Transformer 并行编码所有帧，支持动作/语言/图像目标/多视角等多种条件生成，在视频预测上达到 SOTA 并展示了模仿学习能力（OGBench task3 成功率 89%）。

**[Learning Adaptive Distribution Alignment With Neural Characteristic Function For](learning_adaptive_distribution_alignment_with_neural_characteristic_function_for.md)**

:   提出ADAlign框架，利用神经特征函数在谱域自适应对齐源/目标图分布——无需手动选择对齐标准，自动识别每个迁移场景中最显著的分布差异。在10个数据集16个迁移任务上达SOTA，同时降低内存和训练时间。

**[Learning On A Razors Edge Identifiability And Singularity Of Polynomial Neural N](learning_on_a_razors_edge_identifiability_and_singularity_of_polynomial_neural_n.md)**

:   本文利用代数几何工具，对多项式激活的 MLP 和 CNN 进行了系统性分析：证明了 MLP 的有限可辨识性和 CNN 的唯一可辨识性，揭示了稀疏子网络对应神经流形的奇异点，并从"临界暴露性"角度给出了 MLP 稀疏偏差的几何解释——而 CNN 不具备这种偏差。

**[Learning Structure-Semantic Evolution Trajectories For Graph Domain Adaptation](learning_structure-semantic_evolution_trajectories_for_graph_domain_adaptation.md)**

:   提出DiffGDA——首个将扩散模型引入图域适应(GDA)的方法，用随机微分方程(SDE)建模源图到目标图的连续时间结构-语义联合演化过程，配合基于密度比的域感知引导网络驾驶扩散轨迹朝向目标域，理论证明收敛到最优适应路径，在8个真实数据集14个迁移任务上全面超越SOTA。

**[Lipnext Scaling Up Lipschitz-Based Certified Robustness To Billion-Parameter Mod](lipnext_scaling_up_lipschitz-based_certified_robustness_to_billion-parameter_mod.md)**

:   提出LipNeXt——首个无约束、无卷积的1-Lipschitz架构，通过正交流形优化学习正交矩阵 + 由Theorem 1理论驱动的Spatial Shift Module实现空间混合，成功扩展到十亿参数规模，在CIFAR-10/100、Tiny-ImageNet和ImageNet上全面刷新认证鲁棒精度(CRA) SOTA，ImageNet上 $\varepsilon=1$ 时CRA提升达+8%。

**[Lipschitz Bandits With Stochastic Delayed Feedback](lipschitz_bandits_with_stochastic_delayed_feedback.md)**

:   首次研究连续臂空间的Lipschitz bandit问题在随机延迟反馈下的学习——对有界延迟提出延迟感知zooming算法保持最优遗憾率仅多加性τ_max项，对无界延迟提出分阶段学习策略DLPP并证明近最优遗憾下界，两者均通过"lazy update"机制处理延迟观测对置信半径的非平凡影响。

**[Missing Mass For Differentially Private Domain Discovery](missing_mass_for_differentially_private_domain_discovery.md)**

:   为差分隐私域发现问题提供首批绝对效用保证——用缺失质量(recovered mass fraction)替代基数(unique items)度量,证明简单的加权高斯机制(WGM)在Zipf数据上有近最优ℓ1缺失质量保证且有分布无关的ℓ∞保证,并将WGM作为域发现前驱用于私有top-k和k-hitting set问题获得新效用保证,实验在6个真实数据集上验证。

**[Neural Force Field: Few-shot Learning of Generalized Physical Reasoning](neural_force_field_few-shot_learning_of_generalized_physical_reasoning.md)**

:   提出Neural Force Field(NFF)——将复杂物体交互表示为连续力场→通过ODE积分预测轨迹,与离散隐空间不同,NFF在低维力场中捕捉基本物理概念(重力/支撑/碰撞),仅需少量训练样本即可泛化到未见场景,支持高效的前向-后向规划和交互式精化,在I-PHYRE/N-body/PHYRE上超越所有基线。

**[Noisy-Pair Robust Representation Alignment For Positive-Unlabeled Learning](noisy-pair_robust_representation_alignment_for_positive-unlabeled_learning.md)**

:   提出NcPU框架解决PU学习中判别性表示学习的瓶颈：(1) NoiSNCL噪声对鲁棒的非对比损失使clean pair梯度主导训练；(2) PhantomGate伪标签消歧提供保守负标签。两者在EM框架下迭代互利，在CIFAR-100上将差距（vs 监督学习）从14.26%缩至接近0。

**[On The Impact Of The Utility In Semivalue-Based Data Valuation](on_the_impact_of_the_utility_in_semivalue-based_data_valuation.md)**

:   提出数据集空间签名概念和鲁棒性度量R_p，将数据点嵌入低维空间使效用变为线性泛函，揭示半值数据估值对效用选择的几何敏感性，Banzhaf在多数据集上一致最鲁棒。

**[On The Lipschitz Continuity Of Set Aggregation Functions And Neural Networks For](on_the_lipschitz_continuity_of_set_aggregation_functions_and_neural_networks_for.md)**

:   系统研究了三种常用集合聚合函数（sum/mean/max）和注意力机制在三种多集距离函数下的Lipschitz连续性，推导出集合神经网络的Lipschitz常数上界，并将其与扰动稳定性和分布偏移泛化联系起来。

**[Optimizer Choice Matters For The Emergence Of Neural Collapse](optimizer_choice_matters_for_the_emergence_of_neural_collapse.md)**

:   通过 3,900+ 次训练实验和理论分析，揭示了优化器选择（特别是权重衰减的耦合方式）对 Neural Collapse 现象涌现起关键决定性作用——AdamW（解耦权重衰减）无法产生 Neural Collapse，而 SGD 和 Adam（耦合权重衰减）可以。

**[Out Of The Shadows Exploring A Latent Space For Neural Network Verification](out_of_the_shadows_exploring_a_latent_space_for_neural_network_verification.md)**

:   提出一种基于潜空间（latent space）的规范驱动输入细化方法，通过在高维潜空间中转移输出约束到输入空间，显著减少分支定界过程中的子问题数量，实现高效GPU加速的神经网络验证工具。

**[Oversmoothing Oversquashing Heterophily Long-Range And More Demystifying Common ](oversmoothing_oversquashing_heterophily_long-range_and_more_demystifying_common_.md)**

:   系统梳理并反驳了图机器学习中关于过平滑（OSM）、过挤压（OSQ）、异质性和长程依赖的9个常见但不总成立的"信念"，通过简洁反例推动社区更精确地理解和表述这些概念。

**[Owleye Zero-Shot Learner For Cross-Domain Graph Data Anomaly Detection](owleye_zero-shot_learner_for_cross-domain_graph_data_anomaly_detection.md)**

:   提出OwlEye框架，通过跨域特征对齐、多域多模式字典学习和截断注意力重建三个模块，实现了在完全未见图上的零样本异常检测，且支持无需重训练的持续学习。

**[Predicting Kernel Regression Learning Curves From Only Raw Data Statistics](predicting_kernel_regression_learning_curves_from_only_raw_data_statistics.md)**

:   提出 Hermite 特征结构假设（HEA），仅用数据协方差矩阵和目标函数的 Hermite 分解两个统计量，就能解析预测旋转不变核在真实图像数据集（CIFAR-5m、SVHN、ImageNet）上的学习曲线（测试误差 vs 样本量），并证明该假设在高斯数据下成立，且 MLP 在特征学习 regime 下也按 HEA 预测的顺序学习 Hermite 多项式。

**[Probabilistic Kernel Function For Fast Angle Testing](probabilistic_kernel_function_for_fast_angle_testing.md)**

:   本文研究高维欧氏空间中的角度测试问题，提出两个基于参考角度的确定性概率核函数 $K_S^1$ 和 $K_S^2$，分别用于角度比较和角度阈值判断，无需高斯分布的渐近假设即可获得理论保证，并将其应用于近似最近邻搜索（ANNS），在 HNSW 图上实现 2.5×–3× 的 QPS 加速。

**[Revisiting Sharpness-Aware Minimization A More Faithful And Effective Implementa](revisiting_sharpness-aware_minimization_a_more_faithful_and_effective_implementa.md)**

:   对 SAM 的底层机制提出新的直觉解释——扰动点梯度近似局部最大值方向，并揭示其不精确性及多步退化问题，进而提出 XSAM 通过显式估计最大值方向实现更忠实更有效的锐度感知最小化。

**[Scalable Random Wavelet Features Efficient Non-Stationary Kernel Approximation W](scalable_random_wavelet_features_efficient_non-stationary_kernel_approximation_w.md)**

:   提出 Random Wavelet Features (RWF)，通过从小波族中随机采样构建可扩展的非平稳核近似，保留随机特征的线性时间复杂度，同时具有正定性、无偏性和一致收敛保证。

**[Seed Towards More Accurate Semantic Evaluation For Visual Brain Decoding](seed_towards_more_accurate_semantic_evaluation_for_visual_brain_decoding.md)**

:   提出 SEED（Semantic Evaluation for Visual Brain Decoding），一个结合 Object F1、Cap-Sim 和 EffNet 三个互补指标的组合评估度量，在与人类评估的对齐度上显著超越现有所有指标。

**[Speculative Actions Faster Ai Agents](speculative_actions_faster_ai_agents.md)**

:   借鉴 CPU 推测执行和 LLM 推测解码的思想，提出 Speculative Actions 框架：在慢速 Actor（大模型）计算时用快速 Speculator（小模型）预测未来动作并预执行，匹配时跳过等待实现无损加速，在 Chess/电商/问答等场景实现 15-30% 延迟降低，置信度动态分支策略用 40% 更少 token 达到近似 3 条推测的加速效果。

**[T-Sne Exaggerates Clusters Provably](t-sne_exaggerates_clusters_provably.md)**

:   从理论上严格证明 t-SNE 存在两个根本性失败模式：（1）无法从输出推断输入聚类的强度，（2）无法忠实地展示极端离群点——即使输入毫无聚类结构或存在极端离群点，t-SNE 也可能产生完美聚类的可视化。

**[The Counting Power Of Transformers](the_counting_power_of_transformers.md)**

:   证明 Transformer 不仅能捕获（半）线性计数性质，还能表达所有**半代数计数性质**（即多元多项式不等式的布尔组合），从而推广了先前关于 Transformer 计数能力的所有结果，并由此推导出新的不可判定性结论。

**[The Hot Mess Of Ai How Does Misalignment Scale With Model Intelligence And Task ](the_hot_mess_of_ai_how_does_misalignment_scale_with_model_intelligence_and_task_.md)**

:   将AI模型错误分解为偏差（systematic misalignment）和方差（incoherent behavior），发现：推理越长→越不连贯；更大模型在困难任务上更不连贯。这暗示未来超级AI更可能表现为"工业事故"式的不可预测失败，而非一致追求错误目标。

**[The Invisibility Hypothesis Promises Of Agi And The Future Of The Global South](the_invisibility_hypothesis_promises_of_agi_and_the_future_of_the_global_south.md)**

:   本文提出"不可见性假说"（Invisibility Hypothesis），论证随着AI系统日益成为经济和政治分配的协调层，全球南方的大量人口——特别是非正式工人和小规模生产者——将因缺乏数字可验证性而被系统性排斥（managed exclusion），从被剥削转为被忽略，风险不仅是失业而是整体相关性的丧失。

**[The Price Of Robustness Stable Classifiers Need Overparameterization](the_price_of_robustness_stable_classifiers_need_overparameterization.md)**

:   建立了不连续分类器的稳定性-泛化界，证明了分类任务中的"鲁棒性代价定律"：任何参数量 $p \approx n$ 的插值分类器必然不稳定，实现高稳定性需要 $p \approx nd$ 量级的过参数化。

**[Towards Sustainable Investment Policies Informed By Opponent Shaping](towards_sustainable_investment_policies_informed_by_opponent_shaping.md)**

:   形式化证明 InvestESG 模拟环境在何种条件下构成社会困境，并应用 Advantage Alignment 对抗塑形算法引导经济智能体走向可持续投资均衡。

**[Training Deep Normalization-Free Spiking Neural Networks With Lateral Inhibition](training_deep_normalization-free_spiking_neural_networks_with_lateral_inhibition.md)**

:   提出基于皮层兴奋-抑制（E-I）回路的无归一化学习框架 DeepEISNN，通过 E-I Init 和 E-I Prop 两项技术实现深度 SNN 的稳定端到端训练，兼顾性能与生物合理性。

**[When To Retrain After Drift A Data-Only Test Of Post-Drift Data Size Sufficiency](when_to_retrain_after_drift_a_data-only_test_of_post-drift_data_size_sufficiency.md)**

:   CALIPER提出了一种检测器和模型无关的、仅依赖数据的检验方法，通过跟踪加权局部回归的代理误差随局部性参数$\theta$的单调性变化，来估计突发概念漂移后重训练所需的最小数据量，无需实际重训练下游模型。
