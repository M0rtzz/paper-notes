---
title: >-
  ICML2025 预训练/数据方向 29篇论文解读
description: >-
  29篇ICML2025 预训练/数据方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📚 预训练/数据

**🧪 ICML2025** · 共 **29** 篇

**[A Square Peg In A Square Hole Meta-Expert For Long-Tailed Semi-Supervised Learni](a_square_peg_in_a_square_hole_meta-expert_for_long-tailed_semi-supervised_learni.md)**

:   提出 Meta-Expert 算法，通过动态专家分配（DEA）模块根据样本的类别归属（头/中/尾）自动选择最擅长的专家生成伪标签，并利用多深度特征融合（MFF）模块缓解模型对头类的偏向，实现"方枘方凿"——让每个专家处理它最擅长的样本区间。

**[Algebra Unveils Deep Learning -- An Invitation To Neuroalgebraic Geometry](algebra_unveils_deep_learning_--_an_invitation_to_neuroalgebraic_geometry.md)**

:   本文提出 **neuroalgebraic geometry（神经代数几何）** 这一新研究方向，系统地利用代数几何的工具（维度、度、奇异点、纤维、临界点理论等）来分析深度学习模型参数化的函数空间（neuromanifold），建立起代数几何不变量与机器学习核心问题（样本复杂度、表达能力、训练动力学、隐式偏差）之间的对应字典。

**[Bayesian Neural Scaling Law Extrapolation With Prior-Data Fitted Networks](bayesian_neural_scaling_law_extrapolation_with_prior-data_fitted_networks.md)**

:   首个面向神经缩放定律(Neural Scaling Law)的贝叶斯外推方法，通过设计专门的先验分布（覆盖Down/Down-Down/Down-Up-Down三种功能族），利用PFN (Prior-data Fitted Networks) meta-learn外推能力，在点估计精度和不确定性质量上均优于现有方法。

**[Benign Overfitting In Token Selection Of Attention Mechanism](benign_overfitting_in_token_selection_of_attention_mechanism.md)**

:   本文首次从理论上证明了注意力机制中 token 选择的良性过拟合现象，表明一层注意力网络通过梯度下降可以完美拟合含噪标签的训练数据，同时在信号学习与噪声记忆之间保持平衡时仍能泛化。

**[Chameleon A Flexible Data-Mixing Framework For Language Model Pretraining And Fi](chameleon_a_flexible_data-mixing_framework_for_language_model_pretraining_and_fi.md)**

:   提出Chameleon框架，用kernel ridge leverage scores在学习的嵌入空间中量化域重要性，实现高效的数据混合权重计算，可在预训练/微调/域变化三种场景下工作，且无需重新训练代理模型。

**[Counting In Small Transformers The Delicate Interplay Between Attention And Feed](counting_in_small_transformers_the_delicate_interplay_between_attention_and_feed.md)**

:   通过直方图计数任务，揭示了小型Transformer中注意力层与前馈层之间的精细分工：注意力擅长关系比较（relation-based counting），前馈层负责字典记忆（inventory-based counting），两种策略的出现由嵌入维度 $d$、隐层大小 $p$ 和词表大小 $T$ 的相对关系决定。

**[Density Ratio Estimation-Based Bayesian Optimization With Semi-Supervised Learni](density_ratio_estimation-based_bayesian_optimization_with_semi-supervised_learni.md)**

:   提出 DRE-BO-SSL，将半监督学习（标签传播/标签扩散）引入密度比估计型贝叶斯优化，通过无标签数据点缓解监督分类器的过度利用(over-exploitation)问题，在探索与利用之间取得更好平衡。

**[Dipllm Fine-Tuning Llm For Strategic Decision-Making In Diplomacy](dipllm_fine-tuning_llm_for_strategic_decision-making_in_diplomacy.md)**

:   提出 DipLLM，通过自回归分解框架将外交博弈的指数级组合动作空间分解为单元级决策序列，并微调 LLM 学习均衡策略，仅用 Cicero 1.5% 的训练数据即超越其性能。

**[Does Data Scaling Lead To Visual Compositional Generalization](does_data_scaling_lead_to_visual_compositional_generalization.md)**

:   本文通过受控实验系统研究了数据规模与数据多样性对视觉模型组合泛化能力的影响，发现组合泛化的关键驱动力是数据多样性而非数据量，并证明当表示呈线性分解结构时仅需每个概念值2个组合样本即可完美泛化。

**[Evaluating Morphological Alignment Of Tokenizers In 70 Languages](evaluating_morphological_alignment_of_tokenizers_in_70_languages.md)**

:   扩展 MorphScore 评估框架至 70 种语言，系统研究分词器的形态边界对齐程度与下游任务性能之间的相关性，发现形态对齐仅能解释极少量的性能方差，且呈负相关，挑战了"形态对齐分词有利于模型性能"的主流假设。

**[How To Synthesize Text Data Without Model Collapse](how_to_synthesize_text_data_without_model_collapse.md)**

:   提出 Token-level Editing (ToEdit)，通过对人类数据进行 token 级别的局部重采样（而非完全生成合成数据），在理论上证明测试误差存在有限上界，从而避免 model collapse，并在预训练、持续预训练和微调三个阶段验证了有效性。

**[In-Context Adaptation To Concept Drift For Learned Database Operations](in-context_adaptation_to_concept_drift_for_learned_database_operations.md)**

:   提出 FLAIR 框架，利用数据库执行结果作为上下文实现 in-context adaptation，无需运行时参数更新即可应对 concept drift，在基数估计等任务上实现 5.2× 加速和 22.5% 误差降低。

**[Inductive Gradient Adjustment For Spectral Bias In Implicit Neural Representatio](inductive_gradient_adjustment_for_spectral_bias_in_implicit_neural_representatio.md)**

:   本文从 NTK 线性动力学模型出发，提出 Inductive Gradient Adjustment (IGA) 方法，通过归纳泛化 eNTK 梯度变换矩阵，**有目的性**地缓解 MLP 的频谱偏差，使 INR 在百万级数据点上也能高效学习高频细节。

**[Language Model Developers Should Report Train-Test Overlap](language_model_developers_should_report_train-test_overlap.md)**

:   本文系统性地调研了30个语言模型开发者在训练-测试重叠（train-test overlap）方面的报告实践，发现仅9个模型提供了足够的重叠信息，并呼吁所有开发者在发布评估结果时必须同时报告训练-测试重叠统计数据或公开训练数据。

**[Language Models Over Canonical Byte-Pair Encodings](language_models_over_canonical_byte-pair_encodings.md)**

:   揭示基于 BPE 的语言模型会给指数多个"非规范"编码分配非零概率导致浪费，提出条件化（推理时约束）和构造化（新模型参数化）两种方法强制规范性，改善 held-out 似然。

**[Large Language Models Are Demonstration Pre-Selectors For Themselves](large_language_models_are_demonstration_pre-selectors_for_themselves.md)**

:   提出 FEEDER（FEw yet Essential Demonstration prE-selectoR），一个基于"充分性"和"必要性"度量的示例预选框架，利用 LLM 自身能力从训练数据中识别代表性子集，在 ICL 和微调两个场景下均可减少 20%+ 数据量同时保持甚至提升性能。

**[Llm Data Selection And Utilization Via Dynamic Bi-Level Optimization](llm_data_selection_and_utilization_via_dynamic_bi-level_optimization.md)**

:   提出动态数据加权模型(DWM)，通过双层优化在LLM训练过程中实时调整每批数据的权重，捕捉模型动态变化的数据偏好，比静态数据选择方法一致提升性能且可迁移到不同模型规模。

**[Metadata Conditioning Accelerates Language Model Pre-Training](metadata_conditioning_accelerates_language_model_pre-training.md)**

:   提出 MeCo（Metadata Conditioning then Cooldown），在预训练时将文档的 URL 等元数据前置拼接到文本中，帮助模型区分异质数据源，最后 10% 训练用标准数据做 cooldown，使 1.6B 模型用 **33% 更少的数据**即可达到同等下游性能，同时解锁了通过条件推理引导生成的能力。

**[On The Clean Generalization And Robust Overfitting In Adversarial Training From ](on_the_clean_generalization_and_robust_overfitting_in_adversarial_training_from_.md)**

:   本文从**表示复杂度**和**训练动态**两个视角，理论解释了对抗训练中"干净泛化与鲁棒过拟合共存"(CGRO)现象：CGRO分类器仅需额外 $\tilde{O}(ND)$ 参数即可通过鲁棒记忆实现，而真正的鲁棒泛化在最坏情况下需要指数级模型容量；在结构化数据上，对抗训练的三阶段相变过程会使网络部分学习真特征、完全记忆噪声，从而可证地收敛到CGRO状态。

**[On The Role Of Label Noise In The Feature Learning Process](on_the_role_of_label_noise_in_the_feature_learning_process.md)**

:   从理论和实证角度分析标签噪声在神经网络特征学习中的作用，发现适量的标签噪声可以促进更鲁棒的特征学习（类似正则化效果），但过多噪声会破坏特征质量。

**[Position The Future Of Bayesian Prediction Is Prior-Fitted](position_the_future_of_bayesian_prediction_is_prior-fitted.md)**

:   本文是一篇 position paper，主张 **Prior-Data Fitted Networks (PFNs)**——在随机生成的合成数据集上训练神经网络以近似贝叶斯后验预测分布——代表了贝叶斯推断的未来方向，因为它在实现简洁性、先验定义灵活性、推理速度上全面超越传统 MCMC/VI/GP 方法，并已在表格学习 (TabPFN) 中证明了超越 XGBoost 的实力。

**[Revisiting Continuity Of Image Tokens For Cross-Domain Few-Shot Learning](revisiting_continuity_of_image_tokens_for_cross-domain_few-shot_learning.md)**

:   发现破坏 ViT 图像 token 的连续性（使相邻 patch 像素不再平滑过渡）在源域性能显著下降但在目标域仅略降，揭示连续性帮助学习的大空间模式更难跨域迁移，据此提出简单有效的 ReCIT 方法来缩小域差距。

**[The Dark Side Of The Forces Assessing Non-Conservative Force Models For Atomisti](the_dark_side_of_the_forces_assessing_non-conservative_force_models_for_atomisti.md)**

:   系统评估非保守力模型在原子模拟中的实际影响，揭示其导致几何优化不收敛和分子动力学不稳定，并提出保守+非保守混合模型作为最佳实践。

**[The Double-Ellipsoid Geometry Of Clip](the_double-ellipsoid_geometry_of_clip.md)**

:   揭示CLIP嵌入的双椭球体几何结构——图像和文本分别位于偏离原点的可线性分离椭球壳上，并从对比学习的false negative处理角度解释这一结构的优势。

**[The Sharpness Disparity Principle In Transformers For Accelerating Language Mode](the_sharpness_disparity_principle_in_transformers_for_accelerating_language_mode.md)**

:   揭示了 Transformer 中不同类型模块（Emb、QK、FFN、VO、Norm）存在显著且持久的**锐度差异**（sharpness disparity），并据此提出 Blockwise LR 策略，为低锐度模块分配更大学习率，在不损失稳定性的前提下实现 LLM 预训练近 **2× 加速**。

**[Tokenized Bandit For Llm Decoding And Alignment](tokenized_bandit_for_llm_decoding_and_alignment.md)**

:   将 LLM 解码与对齐问题形式化为 **tokenized bandit**（token化老虎机）问题，提出 DDMC（Diminishing Distance with More Commons）假设，证明在该假设下贪心解码近似最优，并设计了具有次线性遗憾的在线学习算法 EOFUL 和 GreedyETC。

**[Towards Robust Influence Functions with Flat Validation Minima](towards_robust_influence_functions_with_flat_validation_minima.md)**

:   揭示影响函数(IF)在含噪数据上失效的根因在于验证损失的尖锐性而非参数估计精度，提出基于平坦验证极小值的新IF估计形式。

**[When Can In-Context Learning Generalize Out Of Task Distribution](when_can_in-context_learning_generalize_out_of_task_distribution.md)**

:   通过在线性回归ICL任务上系统改变训练任务分布的覆盖范围（超球面帽的半角 $\phi$），发现transformer存在从"专用解"到"通用解"的sharp phase transition：当任务多样性超过临界阈值（$\phi \gtrsim 120°$）时，模型能泛化到整个任务空间，甚至超越贝叶斯最优估计器的OOD性能。

**[Whitened CLIP as a Likelihood Surrogate of Images and Captions](whitened_clip_as_a_likelihood_surrogate_of_images_and_captions.md)**

:   （注：此文缓存不在已读范围内，基于arXiv元信息和领域知识推断写就基本结构。）
