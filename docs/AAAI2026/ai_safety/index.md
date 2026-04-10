<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**🤖 AAAI2026** · 共 **44** 篇

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

**[Fair Model-Based Clustering](fair_model-based_clustering.md)**

:   提出基于有限混合模型的公平聚类算法 FMC，通过在模型参数（而非样本级赋值）上施加公平性约束，实现参数量与样本量无关的可扩展公平聚类，支持小批量学习和分类数据，在大规模数据集上显著优于现有方法。

**[FairGSE: Fairness-Aware Graph Neural Network without High False Positive Rates](fairgse_fairness-aware_graph_neural_network_without_high_false_positive_rates.md)**

:   首次揭示公平感知 GNN 中的"FPR 捷径"问题——现有方法通过大量误判负样本为正来达到公平指标，提出 FairGSE 框架通过最大化二维结构熵重新加权图边来同时改善公平性并降低假阳性率，FPR 降低 39%。

**[FedALT: Federated Fine-Tuning through Adaptive Local Training with Rest-of-World LoRA](fedalt_federated_fine-tuning_through_adaptive_local_training_with_rest-of-world_.md)**

:   提出 FedALT，通过为每个客户端维护独立的 Individual LoRA（本地训练更新）和冻结的 Rest-of-World (RoW) LoRA（其他客户端平均），配合自适应 MoE 混合器动态平衡本地知识与全局知识，彻底避免 FedAvg 聚合导致的跨客户端干扰，在异构任务联邦 LLM 微调上显著优于 SOTA。

**[From Pretrain to Pain: Adversarial Vulnerability of Video Foundation Models without Finetuning](from_pretrain_to_pain_adversarial_vulnerability_of_video_foundation_models_witho.md)**

:   提出 Transferable Video Attack (TVA)，仅利用开源视频基础模型（VFM）的嵌入空间即可生成对抗扰动，无需任何下游任务知识便能有效攻击24个视频任务上的下游模型和多模态LLM。

**[From Single to Societal: Analyzing Persona-Induced Bias in Multi-Agent Interactions](from_single_to_societal_analyzing_persona-induced_bias_in_multi-agent_interactio.md)**

:   本文首次系统研究了 LLM 多智能体交互中的人格诱导偏见，通过在协作问题解决和说服任务中的受控实验，揭示了三个关键发现：(1) 不同人格在可信度和坚持度上存在显著偏差（优势群体如男性和白人被视为更不可信）；(2) 智能体表现出显著的内群体偏好；(3) 这些偏见在多轮、多智能体场景中持续存在且有放大趋势。

**[Generalizing Fair Clustering to Multiple Groups: Algorithms and Applications](generalizing_fair_clustering_to_multiple_groups_algorithms_and_applications.md)**

:   将最近公平聚类（Closest Fair Clustering）问题从仅两个群体推广到任意多群体，证明三群体以上等比例情形已为NP-hard，提出近线性时间近似算法（等比例 $O(|\chi|^{1.6}\log^{2.81}|\chi|)$、任意比例 $O(|\chi|^{3.81})$），并将结果推广至公平相关聚类和公平共识聚类问题。

**[Ghost in the Transformer: Detecting Model Reuse with Invariant Spectral Signatures](ghost_in_the_transformer_detecting_model_reuse_with_invariant_spectral_signature.md)**

:   提出 GhostSpec，一种无需数据、不修改模型行为的白盒方法，通过对注意力权重矩阵的不变乘积做 SVD 提取光谱指纹，可在微调、剪枝、合并、扩展甚至对抗性变换下稳健地验证 LLM 血统。

**[GraphTextack: A Realistic Black-Box Node Injection Attack on LLM-Enhanced GNNs](graphtextack_a_realistic_black-box_node_injection_attack_on_llm-enhanced_gnns.md)**

:   提出 GraphTextack——首个针对 LLM 增强 GNN 的黑盒多模态节点注入投毒攻击，通过进化优化框架联合优化注入节点的图结构连接和语义特征，不依赖模型内部信息或代理模型，在5个数据集和2类LLM-GNN模型上显著优于12种基线方法。

**[Hashed Watermark as a Filter: A Unified Defense Against Forging and Overwriting Attacks in Neural Network Watermarking](hashed_watermark_as_a_filter_defeating_forging_and_overwriting_attacks_in_weight.md)**

:   提出 NeuralMark——一种基于哈希水印过滤器的权重水印方法，利用哈希函数从秘钥生成不可逆二值水印作为私有过滤器选择嵌入参数，借助雪崩效应阻断伪造攻击的梯度反推，通过多轮过滤减少参数重叠抵御覆写攻击，在13种CNN/Transformer架构、5个图像分类和1个文本生成任务上验证了有效性和鲁棒性。

**[Lamp Learning Universal Adversarial Perturbations For Multi-Image Tasks Via Pre-](lamp_learning_universal_adversarial_perturbations_for_multi-image_tasks_via_pre-.md)**

:   提出 LAMP，一种针对多图 MLLM 的 black-box Universal Adversarial Perturbation 学习方法，通过 attention 约束和"传染式"损失实现仅扰动少量图像即可跨模型/任务迁移攻击。

**[Learning to Collaborate: An Orchestrated-Decentralized Framework for Peer-to-Peer Collaborative Learning](learning_to_collaborate_an_orchestrated-decentralized_framework_for_peer-to-peer.md)**

:   提出 KNEXA-FL 框架，通过一个不接触模型的中央配对器（CPM）将 P2P 协作建模为上下文 Bandit 问题，使用 LinUCB 学习最优配对策略，在异构 LLM 联邦学习中实现比随机 P2P 高约 50% 的 Pass@1 提升，且避免了中心化蒸馏的灾难性崩溃。

**[Matrix-Free Two-To-Infinity And One-To-Two Norms Estimation](matrix-free_two-to-infinity_and_one-to-two_norms_estimation.md)**

:   提出 TwINEst 和 TwINEst++ 两种 matrix-free 随机算法用于估计 $\|A\|_{2\to\infty}$ 和 $\|A\|_{1\to 2}$ 范数，并将其应用于深度网络 Jacobian 正则化（提升分类泛化和对抗鲁棒性）和推荐系统对抗防御。

**[Perturb Your Data: Paraphrase-Guided Training Data Watermarking](perturb_your_data_paraphrase-guided_training_data_watermarking.md)**

:   提出SPECTRA——一种基于paraphrase采样的训练数据水印方法，通过LLM生成改写文本并利用Min-K%++评分选择与原文分数接近的paraphrase作为水印，在数据仅占训练语料0.001%的情况下，member与non-member的p-value差距稳定超过9个数量级。

**[Privacy Auditing of Multi-Domain Graph Pre-Trained Model under Membership Inference Attack](privacy_auditing_of_multi-domain_graph_pre-trained_model_under_membership_infere.md)**

:   提出 MGP-MIA 框架，首次针对多域图预训练模型开展成员推理攻击（MIA），通过机器遗忘放大成员信号、增量学习构建影子模型、基于相似度的推理机制，有效揭示多域图预训练的隐私泄漏风险。

**[ProbLog4Fairness: A Neurosymbolic Approach to Modeling and Mitigating Bias](problog4fairness_a_neurosymbolic_approach_to_modeling_and_mitigating_bias.md)**

:   提出 ProbLog4Fairness 框架，利用概率逻辑编程语言 ProbLog 将数据中的偏差机制形式化为可解释的逻辑程序，并通过 DeepProbLog 的远程监督将偏差假设集成到神经网络训练中，实现灵活、原则性的偏差缓解。

**[RegionMarker: A Region-Triggered Semantic Watermarking Framework for Embedding-as-a-Service](regionmarker_a_region-triggered_semantic_watermarking_framework_for_embedding-as.md)**

:   提出基于语义区域触发的水印框架 RegionMarker，在低维空间中定义触发区域并注入语义水印，是首个能同时抵御 CSE 攻击、改写攻击和维度扰动攻击的 EaaS 版权保护方法。

**[Rethinking Target Label Conditioning in Adversarial Attacks: A 2D Tensor-Guided Generative Approach](rethinking_target_label_conditioning_in_adversarial_attacks_a_2d_tensor-guided_g.md)**

:   提出 TGAF 框架，利用扩散模型将目标标签编码为 2D 语义张量来引导对抗噪声生成，并设计随机遮挡策略保留完整语义信息，显著提升目标对抗攻击的可迁移性。

**[Revisiting Unfairness In Recourse By Minimizing Worst-Case Social Burden](revisiting_unfairness_in_recourse_by_minimizing_worst-case_social_burden.md)**

:   指出现有 recourse 公平性指标忽略了分类器决策偏差和 ground-truth 信息，提出基于 social burden 的整体公平性框架和 MISOB 算法，通过 minimax 重加权减少所有群体的 worst-case 社会负担。

**[Robust Watermarking on Gradient Boosting Decision Trees](robust_watermarking_on_gradient_boosting_decision_trees.md)**

:   提出首个针对 GBDT 模型的鲁棒水印框架，通过 in-place 微调嵌入水印，设计了四种嵌入策略（Wrong Prediction Flip、Outlier Flip、Cluster Center Flip、Confidence Flip），实现高嵌入成功率、低精度损失和强抗微调鲁棒性。

**[SecMoE: Communication-Efficient Secure MoE Inference via Select-Then-Compute](secmoe_communication-efficient_secure_moe_inference_via_select-then-compute.md)**

:   提出 SecMoE 框架，通过 Select-Then-Compute 范式在两方安全计算中高效实现稀疏 MoE 推理，避免冗余专家计算，通信量降低最高 29.8 倍，端到端加速最高 16.1 倍。

**[Sim-to-Real: An Unsupervised Noise Layer for Screen-Camera Watermarking Robustness](sim-to-real_an_unsupervised_noise_layer_for_screen-camera_watermarking_robustnes.md)**

:   提出 Simulation-to-Real (S2R) 框架，首创"数学建模 → 无监督域迁移"两阶段噪声近似策略：先用数学模型将清晰图像变换到已知噪声域 $\mathcal{C}$，再用无监督 Image-to-Image 网络 $G$ 将 $\mathcal{C}$ 映射到真实屏幕-相机噪声域 $\mathcal{U}$，无需配对数据即可精确逼近真实 SC 噪声，在多设备、多角度、多距离条件下均取得最优水印鲁棒性（BER 降低 30-60%）和图像质量（PSNR 42.27 dB / SSIM 0.962）。

**[The Confidence Trap: Gender Bias and Predictive Certainty in LLMs](the_confidence_trap_gender_bias_and_predictive_certainty_in_llms.md)**

:   提出Gender-ECE指标，系统评估六种开源LLM在性别代词预测任务中的置信度校准与人类偏见对齐程度，发现Gemma-2模型校准最差且存在极端的男女代词校准差异，而训练数据过滤较少的GPT-J-6B反而校准最好。

**[Truth, Justice, and Secrecy: Cake Cutting Under Privacy Constraints](truth_justice_and_secrecy_cake_cutting_under_privacy_constraints.md)**

:   首个隐私保护蛋糕切割协议，在保持无嫉妒性和策略防谋性的同时，通过秘密共享和安全多方计算（MPC）技术确保参与者的估值函数不被泄露。

**[Uncovering Bias Paths With Llm-Guided Causal Discovery An Active Learning And Dy](uncovering_bias_paths_with_llm-guided_causal_discovery_an_active_learning_and_dy.md)**

:   提出一种融合LLM语义先验与统计信号的混合因果发现框架，通过主动学习（Active Learning）和动态评分机制优先查询信息量最大的变量对，在噪声和混淆条件下有效恢复公平性关键因果路径（如 sex→education→income），显著优于传统CD方法和朴素LLM方法。
