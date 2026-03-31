<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🔬 ICLR2026** · 共 **18** 篇

**[AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations](amemgym_interactive_memory_benchmarking_for_assistants_in_long-horizon_conversat.md)**

:   提出AMemGym——首个支持on-policy交互式评估的长程对话记忆基准环境，通过结构化数据采样（用户画像→状态演化→个性化问答）驱动LLM模拟用户进行角色扮演，揭示了off-policy评估的排名偏差问题，并系统诊断了RAG/长上下文/Agent记忆系统的write/read/utilization三阶段失败模式。

**[AMPED: Adaptive Multi-objective Projection for balancing Exploration and skill Diversification](amped_adaptive_multi-objective_projection_for_balancing_exploration_and_skill_di.md)**

:   提出AMPED框架，在技能预训练阶段用梯度手术（PCGrad）平衡探索（熵+RND）和技能多样性（AnInfoNCE）之间的梯度冲突，在微调阶段用SAC-based技能选择器自适应选择最优技能，在Maze和URLB基准上超越DIAYN/CeSD/CIC等SBRL基线。

**[An Efficient, Provably Optimal Algorithm for the 0-1 Loss Linear Classification Problem](an_efficient_provably_optimal_algorithm_for_the_0-1_loss_linear_classification_p.md)**

:   提出增量单元枚举算法（ICE），首个具有严格证明的独立算法，可以在 $O(N^{D+1})$ 时间内精确求解0-1损失线性分类问题的全局最优解，并扩展到多项式超曲面分类。

**[Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence](antibody_strengthening_defense_against_harmful_fine-tuning_for_large_language_mo.md)**

:   提出Antibody防御框架：在对齐阶段通过平坦度正则化使模型处于有害损失的平坦区域（梯度小→难被攻击），在微调阶段用基于模型安全知识的样本加权方案（对比目标完成 vs 拒绝的似然比）抑制有害样本的学习，平均Harmful Score从15.29%降至7.04%。

**[Bayesian Influence Functions for Hessian-Free Data Attribution](bayesian_influence_functions_for_hessian-free_data_attribution.md)**

:   提出 Local Bayesian Influence Function (BIF)，用 SGLD 采样估计的协方差替代经典影响函数中不可行的 Hessian 逆运算，实现了对数十亿参数模型的无架构限制数据归因，在重训练实验中达到 SOTA。

**[Biologically Plausible Online Hebbian Meta-Learning: Two-Timescale Local Rules for Spiking Neural Brain Interfaces](biologically_plausible_online_hebbian_meta-learning_two-timescale_local_rules_fo.md)**

:   提出一种无需BPTT的在线SNN解码器，通过三因子Hebbian局部学习规则结合双时间尺度eligibility trace和自适应学习率控制，在O(1)内存下实现可比离线训练方法的BCI神经解码精度（Pearson R≥0.63/0.81），并在闭环仿真中展现了对神经信号非平稳性的持续适应能力。

**[COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics](cold-steer_steering_large_language_models_via_in-context_one-step_learning_dynam.md)**

:   提出 COLD-Steer，通过近似梯度下降在上下文示例上产生的表征变化来实现无训练的 LLM 激活转向，在仅用 50 分之一样本量的情况下达到 95% 的转向效果。

**[CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation](collectivekv_decoupling_and_sharing_collaborative_information_in_sequential_reco.md)**

:   观察到序列推荐中不同用户的 KV cache 具有显著跨用户相似性（协同信号），提出 CollectiveKV 将 KV 分解为低维用户特有部分和从全局 KV 池检索的高维共享部分，实现 0.8% 的压缩率且性能不降。

**[Condition Matters in Full-head 3D GANs](condition_matters_in_full-head_3d_gans.md)**

:   发现全头 3D GAN 中视角条件导致严重方向偏差（条件视角生成质量远优于其他视角），提出用视角不变的语义特征（正脸 CLIP 特征）替代视角作为条件，配合 Flux.1 Kontext 合成的 1120 万张 360° 平衡数据集，首次实现全视角一致的高保真多样全头生成。

**[DGNet: Discrete Green Networks for Data-Efficient Learning of Spatiotemporal PDEs](dgnet_discrete_green_networks_for_data-efficient_learning_of_spatiotemporal_pdes.md)**

:   基于Green函数理论，将叠加原理嵌入物理-神经混合架构，构建离散Green网络DGNet，在仅用数十条训练轨迹的条件下实现SOTA精度，并展现对未见源项的鲁棒零样本泛化。

**[DiffVax: Optimization-Free Image Immunization Against Diffusion-Based Editing](diffvax_optimization-free_image_immunization_against_diffusion-based_editing.md)**

:   DiffVax 训练一个前馈免疫器（UNet++），对任意图像仅需一次前向传播（~70ms）即可生成不可感知的对抗扰动，使基于扩散模型的恶意编辑失败，相比先前逐图优化方法实现 250,000× 加速，并首次将免疫扩展到视频内容。

**[Distilling and Adapting: A Topology-Aware Framework for Zero-Shot Interaction Prediction in Multiplex Biological Networks](distilling_and_adapting_a_topology-aware_framework_for_zero-shot_interaction_pre.md)**

:   提出CAZI-MBN框架，通过融合领域特定LLM序列嵌入、拓扑感知图分词器、上下文感知跨层注意力和教师-学生蒸馏，实现多重生物网络中未见实体的零样本交互预测，在5个基准数据集上AUROC较最优baseline提升3.1-20.4%。

**[EgoHandICL: Egocentric 3D Hand Reconstruction with In-Context Learning](egohandicl_egocentric_3d_hand_reconstruction_with_in-context_learning.md)**

:   首次将上下文学习（ICL）范式引入3D手部重建，通过VLM引导的模板检索、多模态ICL分词器和MAE驱动的重建流程，在ARCTIC和EgoExo4D基准上显著超越SOTA方法。

**[Function Spaces Without Kernels: Learning Compact Hilbert Space Representations](function_spaces_without_kernels_learning_compact_hilbert_space_representations.md)**

:   证明函数编码器（Function Encoders）通过学习神经网络基函数定义了一个有效的核，建立了神经特征学习与RKHS理论的桥梁，并提出PCA引导的紧凑基选择算法和有限样本泛化界。

**[GaitSnippet: Gait Recognition Beyond Unordered Sets and Ordered Sequences](gaitsnippet_gait_recognition_beyond_unordered_sets_and_ordered_sequences.md)**

:   提出 Snippet 范式：将步态轮廓序列组织为若干"片段"（snippet），每个 snippet 由一个连续区间内随机抽取的帧构成，兼顾短程时序上下文与长程时序依赖，在 Gait3D 上以 2D 卷积骨干达到 77.5% Rank-1，超越所有 3D 卷积方法。

**[Generalizable End-to-End Tool-Use RL with Synthetic CodeGym](generalizable_end-to-end_tool-use_rl_with_synthetic_codegym.md)**

:   提出 CodeGym 框架，将编程题自动转化为多轮工具调用的交互式环境，用于 LLM agent 的强化学习训练，在分布外基准上取得显著泛化提升（如 Qwen2.5-32B 在 τ-Bench 上 +8.7 点）。

**[NeuroGaze-Distill: Brain-informed Distillation and Depression-Inspired Geometric Priors for Robust Facial Emotion Recognition](neurogaze-distill_brain-informed_distillation_and_depression-inspired_geometric_.md)**

:   提出 NeuroGaze-Distill 跨模态蒸馏框架：从 EEG 脑电训练的教师模型中提取静态 Valence-Arousal 原型，通过 Proto-KD 和抑郁症启发的几何先验（D-Geo）注入纯视觉学生模型，无需 EEG-人脸配对数据，提升表情识别的跨数据集鲁棒性。

**[Soft Equivariance Regularization for Invariant Self-Supervised Learning](soft_equivariance_regularization_for_invariant_self-supervised_learning.md)**

:   提出 SER（Soft Equivariance Regularization），通过在 ViT 中间层施加软等变正则化、在最终层保持不变性目标的层解耦设计，在不引入额外模块的情况下，为不变性 SSL 方法（MoCo-v3, DINO, Barlow Twins）带来一致的分类精度和鲁棒性提升。
