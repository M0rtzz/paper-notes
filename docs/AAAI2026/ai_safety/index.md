<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**🤖 AAAI2026** · 共 **21** 篇

**[Alternative Fairness and Accuracy Optimization in Criminal Justice](alternative_fairness_and_accuracy_optimization_in_criminal_j.md)**

:   本文系统综述了算法公平性的三大维度（群体公平、个体公平、过程公平），提出了一种基于容差约束的改进群体公平性优化公式，并构建了面向公共决策系统的"公平三支柱"部署框架。

**[An Improved Privacy and Utility Analysis of Differentially Private SGD with Bounded Domain and Smooth Losses](an_improved_privacy_and_utility_analysis_of_differentially_p.md)**

:   在仅假设损失函数L-光滑（不需要凸性）的条件下，为DPSGD推导出了更紧的闭式RDP隐私界，并首次在有界域场景下给出了完整的收敛性/效用分析，揭示了较小的参数域直径可以同时改善隐私和效用。

**[An Information Theoretic Evaluation Metric for Strong Unlearning](an_information_theoretic_evaluation_metric_for_strong_unlear.md)**

:   提出 Information Difference Index (IDI)，一种基于信息论的白盒评估指标，通过度量中间层特征与遗忘标签之间的互信息来衡量机器遗忘的彻底程度，揭示了现有黑盒指标（MIA、JSD等）无法捕捉的中间层残留信息问题，并提出 COLA 方法在特征层面消除残余信息。

**[An Information Theoretic Evaluation Metric for Strong Unlearning](an_information_theoretic_evaluation_metric_for_strong_unlearning.md)**

:   揭示现有黑盒遗忘评估指标（MIA/JSD等）的根本缺陷——仅修改最后一层即可满足所有黑盒指标但中间层完整保留遗忘数据信息，提出IDI白盒指标通过InfoNCE估计各层与遗忘标签的互信息差异来量化遗忘效果，并提出COLA方法在CIFAR-10/100和ImageNet-1K上实现接近Retrain的IDI得分。

**[An LLM-Based Simulation Framework for Embodied Conversational Agents in Psychological Counseling](an_llm-based_simulation_framework_for_embodied_conversationa.md)**

:   提出 ECAs 框架，基于认知行为治疗(CBT)等心理学理论，利用 LLM 将真实咨询案例扩展为具身认知记忆空间，模拟心理咨询中来访者的完整认知过程，生成高保真度的咨询对话数据，在专家评估和自动评估中均显著优于基线。

**[Angular Gradient Sign Method: Uncovering Vulnerabilities in Hyperbolic Networks](angular_gradient_sign_method_uncovering_vulnerabilities_in_h.md)**

:   提出Angular Gradient Sign Method (AGSM)，将双曲空间中的梯度分解为径向（层次深度）和角度（语义）分量，仅沿角度方向施加扰动来生成对抗样本，在图像分类和跨模态检索任务上比标准FGSM/PGD多降低5-13%的准确率。

**[Argumentative Debates for Transparent Bias Detection (ABIDE)](argumentative_debates_for_transparent_bias_detection_technic.md)**

:   提出ABIDE框架，将偏见检测过程结构化为基于量化二极论辩框架（QBAF）的辩论：通过邻域级局部统计公平性（neighbourhood-based local statistical parity）生成偏见论据，利用批判性问题（critical questions）作为攻击机制挑战不可靠论据，在合成/真实/LLM模型上均优于IRB基线。

**[AUVIC: Adversarial Unlearning of Visual Concepts for Multi-modal Large Language Models](auvic_adversarial_unlearning_of_visual_concepts_for_multi-mo.md)**

:   提出AUVIC框架，通过对抗性扰动生成器 + 动态锚点保留机制，在MLLM中精确遗忘目标视觉概念（如特定人脸），同时避免对语义相似概念的附带遗忘，并构建了首个面向群体场景视觉概念遗忘的评测基准VCUBench。

**[Beyond Superficial Forgetting: Thorough Unlearning through Knowledge Density Estimation and Block Re-insertion](beyond_superficial_forgetting_thorough_unlearning_through_knowledge_density_esti.md)**

:   提出 KUnBR 框架，通过梯度引导的知识密度估计定位有害知识富集层，并采用块重插入策略绕过 cover layer 的梯度遮蔽效应，实现对 LLM 有害知识的深度遗忘而非表面抑制。

**[Breaking the Adversarial Robustness-Performance Trade-off in Text Classification via Manifold Purification](breaking_the_adversarial_robustness-performance_trade-off_in_text_classification.md)**

:   提出 Manifold-Correcting Causal Flow (MC²F) 框架，通过分层黎曼连续正则化流 (SR-CNF) 学习干净数据嵌入的流形密度进行对抗样本检测，再用测地线净化求解器 (Geodesic Purification Solver) 将被检测为对抗的嵌入沿最短路径投影回干净流形，在 SST-2/AGNews/YELP 三个数据集上对抗鲁棒性全面超越 SOTA，同时完全不损失（甚至略微提升）干净数据精度。

**[Breaking the Dyadic Barrier: Rethinking Fairness in Link Prediction Beyond Demographic Parity](breaking_the_dyadic_barrier_rethinking_fairness_in_link_prediction_beyond_demogr.md)**

:   本文揭示了链接预测中二元公平性（dyadic fairness）和 Demographic Parity（ΔDP）的三大根本缺陷——GNN 表达力不足、子群偏差被掩盖、对排序不敏感——并提出基于 NDKL 的排序感知公平度量和后处理算法 MORAL，在六个数据集上实现了 SOTA 的公平性-效用权衡。

**[Can Editing LLMs Inject Harm?](can_editing_llms_inject_harm.md)**

:   本文将知识编辑技术重新定义为一种新型 LLM 安全威胁（Editing Attack），系统性地研究了通过 ROME、FT、ICE 三种编辑方法向 LLM 注入虚假信息和偏见的可行性，发现其效果显著且极具隐蔽性。

**[CoRe-Fed: Bridging Collaborative and Representation Fairness via Federated Embedding Distillation](core-fed_bridging_collaborative_and_representation_fairness_via_federated_embedd.md)**

:   提出 CoRe-Fed 框架，通过嵌入级对比对齐与贡献感知聚合两个协同模块，同时解决联邦学习中的表示公平性和协作公平性问题，在异构数据分布下显著提升全局模型的公平性与泛化能力。

**[DeepTracer: Tracing Stolen Model via Deep Coupled Watermarks](deeptracer_tracing_stolen_model_via_deep_coupled_watermarks.md)**

:   提出DeepTracer鲁棒水印框架，通过自适应源类选择（K-Means聚类覆盖特征空间）+ 同类耦合损失（拉近水印样本与目标类在输出空间的距离）+ 两阶段关键样本过滤，使水印任务与主任务深度耦合，在6种模型窃取攻击（含hard-label和data-free）下水印成功率平均达77-100%，远超现有方法。

**[Democratizing LLM Efficiency: From Hyperscale Optimizations to Universal Deployability](democratizing_llm_efficiency_from_hyperscale_optimizations_to_universal_deployab.md)**

:   本文是一篇立场论文（position paper），指出当前 LLM 效率研究被超大规模假设所主导，提出面向中小规模部署者的五大开放研究挑战，并倡导以开销感知效率（OAE）重新定义效率指标。

**[Detect All-Type Deepfake Audio: Wavelet Prompt Tuning for Enhanced Auditory Perception](detect_all-type_deepfake_audio_wavelet_prompt_tuning_for_enhanced_auditory_perce.md)**

:   首次建立全类型（语音/声音/歌声/音乐）音频深伪检测基准，提出小波提示调优（WPT）方法通过离散小波变换增强 SSL 特征的全频域感知能力，在不增加训练参数的前提下超越全量微调，co-training 后平均 EER 仅 3.58%。

**[Diversifying Counterattacks: Orthogonal Exploration for Robust CLIP Inference](diversifying_counterattacks_orthogonal_exploration_for_robust_clip_inference.md)**

:   提出方向正交反攻击（DOC）方法，通过在反攻击优化中引入正交梯度分量和动量更新扩展搜索空间，结合基于余弦相似度的方向敏感度评分自适应调控反攻击强度，在 16 个数据集上显著提升 CLIP 的测试时对抗鲁棒性。

**[Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias](easy_to_learn_yet_hard_to_forget_towards_robust_unlearning_under_bias.md)**

:   提出 CUPID 框架，通过损失景观的锐度分析将遗忘集划分为因果/偏差子集，并识别和分离模型中的因果/偏差通路，实现对有偏模型的精准类别遗忘，有效解决"捷径遗忘"问题。

**[EFX and PO Allocation Exists for Two Types of Goods](efx_and_po_allocation_exists_for_two_types_of_goods.md)**

:   证明了当物品只有两种类型且所有估值为正时，满足 EFX（任意物品无嫉妒）和 Pareto 最优的分配总是存在的，并给出了准线性时间算法。

**[Enhancing Dpsgd Via Per-Sample Momentum And Low-Pass Filtering](enhancing_dpsgd_via_per-sample_momentum_and_low-pass_filtering.md)**

:   提出 DP-PMLF，通过逐样本动量（per-sample momentum）降低裁剪偏差，同时利用低通滤波器（low-pass filter）抑制高频 DP 噪声，首次同时从两个方向缓解 DPSGD 的精度退化问题。

**[Truth, Justice, and Secrecy: Cake Cutting Under Privacy Constraints](truth_justice_and_secrecy_cake_cutting_under_privacy_constraints.md)**

:   首个隐私保护蛋糕切割协议，在保持无嫉妒性和策略防谋性的同时，通过秘密共享和安全多方计算（MPC）技术确保参与者的估值函数不被泄露。
