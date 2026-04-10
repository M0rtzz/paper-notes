<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**🧠 NeurIPS2025** · 共 **71** 篇

**[A Set of Generalized Components to Achieve Effective Poison-only Clean-label Backdoor Attacks with Collaborative Sample Selection and Triggers](a_set_of_generalized_components_to_achieve_effective_poison-only_clean-label_bac.md)**

:   提出一组通用化组件（Component A/B/C），通过充分挖掘样本选择与触发器之间的双向协作关系，同时提升 Poison-only Clean-label 后门攻击的攻击成功率（ASR）和隐蔽性，并在多种攻击类型上展现了良好的泛化能力。

**[Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning](adaptive_lora_experts_allocation_and_selection_for_federated_fine-tuning.md)**

:   提出 FedLEASE——解决联邦 LoRA 微调中两个关键问题：(1) 用 LoRA B 矩阵相似度聚类自动确定最优专家数量和分配，(2) 用扩展路由空间（$2M-1$ 维）实现自适应 top-M 专家选择（每个客户端自动决定用几个专家），在 GLUE 上比最强基线平均提升 5.53%。

**[Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text](adversarial_paraphrasing_a_universal_attack_for_humanizing_ai-generated_text.md)**

:   提出 Adversarial Paraphrasing——一种无需训练的通用攻击框架，在逐 token 改写时利用 AI 文本检测器的反馈信号选择"最像人写"的 token，使改写后的 AI 文本在 8 种检测器上平均 T@1%F 下降 87.88%，且具有跨检测器的强迁移性。

**[AI Should Sense Better, Not Just Scale Bigger: Adaptive Sensing as a Paradigm Shift](ai_should_sense_better_not_just_scale_bigger_adaptive_sensin.md)**

:   提出"自适应感知"作为AI发展的范式级转变——受生物感觉系统启发，主张在传感器层面动态调整输入参数（如曝光、增益、多模态配置），而非仅靠扩大模型规模来应对分布偏移，实证表明5M参数的EfficientNet-B0通过自适应感知可超越632M参数的OpenCLIP-H。

**[ALMGuard: Safety Shortcuts and Where to Find Them as Guardrails for Audio-Language Models](almguard_safety_shortcuts_and_where_to_find_them_as_guardrails_for_audio-languag.md)**

:   首个针对音频语言模型（ALM）越狱攻击的防御框架——发现对齐过的 ALM 存在可被激活的潜在安全快捷路径（safety shortcuts），通过 Mel 梯度稀疏掩码（M-GSM）定位关键频率段，施加快捷路径激活扰动（SAP），将平均攻击成功率从 41.6% 降至 4.6%，同时几乎不影响正常任务性能。

**[Benchmarking is Broken — Don't Let AI be its Own Judge](benchmarking_is_broken_--_dont_let_ai_be_its_own_judge.md)**

:   系统性批评当前 AI 基准评估的根本缺陷——数据污染（MMLU 45%+ 重叠）、选择性报告、缺乏监考——并提出 PeerBench 方案：借鉴高考/GRE 的监考范式，用滚动更新的保密题库 + 同行评审质量控制 + 声誉加权评分 + 加密承诺机制构建下一代 AI 评估基础设施。

**[Beyond Last-Click: An Optimal Mechanism for Ad Attribution](beyond_last-click_an_optimal_mechanism_for_ad_attribution.md)**

:   从博弈论角度分析广告归因中 Last-Click 机制的策略操纵漏洞——平台可以通过篡改时间戳获取不公正的归因信用，提出 Peer-Validated Mechanism（PVM）——每个平台的信用仅取决于其他平台的报告（类比同行评审），理论证明 PVM 是占优策略激励兼容（DSIC）且在同质设置下最优，准确率从 34% 提升到 75%（2 平台）。

**[Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks Against LLMs](bits_leaked_per_query_information-theoretic_bounds_on_adversarial_attacks_agains.md)**

:   将 LLM 对抗攻击建模为信息通道问题——定义每次查询的"泄漏比特数" $I(Z;T)$ 为攻击目标属性 $T$ 与可观测信号 $Z$ 的互信息，证明攻击达到误差 $\varepsilon$ 所需最少查询数为 $\log(1/\varepsilon)/I(Z;T)$，在 7 个 LLM 上验证：暴露 answer tokens 需 ~1000 次查询，加 logits 降到 ~100 次，加思维链降到 ~几十次，为透明性-安全性权衡提供首个原则性标尺。

**[Boosting Adversarial Transferability with Spatial Adversarial Alignment](boosting_adversarial_transferability_with_spatial_adversarial_alignment.md)**

:   提出 Spatial Adversarial Alignment (SAA)，通过空间感知对齐和对抗感知对齐两个模块微调代理模型，使其特征与见证模型对齐，从而显著提升对抗样本的跨架构迁移性（CNN→ViT 迁移率提升 25-39%）。

**[Bridging Symmetry and Robustness: On the Role of Equivariance in Enhancing Adversarial Robustness](bridging_symmetry_and_robustness_on_the_role_of_equivariance_in_enhancing_advers.md)**

:   通过在 CNN 中嵌入旋转等变（P4群）和尺度等变卷积层，提出 Parallel 和 Cascaded 两种对称性感知架构，无需对抗训练即可显著提升对抗鲁棒性，并从 CLEVER 框架出发理论证明等变架构能压缩假设空间、正则化梯度、收紧认证鲁棒性界。

**[Causally Reliable Concept Bottleneck Models](causally_reliable_concept_bottleneck_models.md)**

:   提出 C2BM（Causally reliable Concept Bottleneck Models），将概念瓶颈（concept bottleneck）按照因果图结构化组织，通过结合观测数据与背景知识自动学习因果关系，在保持分类精度的同时显著提升因果可靠性、干预响应和公平性。

**[Collective Narrative Grounding: Community-Coordinated Data Contributions to Improve Local AI Systems](collective_narrative_grounding_community-coordinated_data_contributions_to_impro.md)**

:   提出 Collective Narrative Grounding 协议，通过参与式工坊收集社区叙事并结构化为"叙事单元"，用 RAG 管道将本地知识注入 LLM 问答系统，在 LocalBench 上发现 76.7% 的错误可由本地叙事直接修复，GPT-5 在参与式 QA 集上仅 21% 正确率凸显了本地知识鸿沟。

**[Contextual Integrity in LLMs via Reasoning and Reinforcement Learning](contextual_integrity_in_llms_via_reasoning_and_reinforcement_learning.md)**

:   提出 CI-RL 框架，通过 Chain-of-Thought 推理提示 + GRPO 强化学习，用仅约 700 个合成样本训练 LLM 理解"上下文完整性"（contextual integrity），在 PrivacyLens 基准上将隐私泄露率降低最高 40%，且小模型训练后可超越更大基线模型。

**[CoreGuard: Safeguarding Foundational Capabilities of LLMs Against Model Stealing in Edge Deployment](coreguard_safeguarding_foundational_capabilities_of_llms_against_model_stealing_.md)**

:   提出 CoreGuard，通过行置换（row permutation）锁定 Transformer 线性层权重 + 列置换传播协议（propagation protocol）将 TEE 授权次数降至 1 次，以极低计算和通信开销保护边缘部署 LLM 的基础能力不被模型窃取攻击利用。

**[Cost Efficient Fairness Audit Under Partial Feedback](cost_efficient_fairness_audit_under_partial_feedback.md)**

:   在部分反馈（partial feedback）设定下，提出了一套包含新颖成本模型的公平性审计框架，分别在黑盒与混合模型两种场景给出近最优审计算法，审计成本比自然基线降低约 50%。

**[CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming](cpret_a_dataset_benchmark_and_model_for_retrieval_in_competitive_programming.md)**

:   针对竞赛编程中重复/相似题目泛滥导致比赛不公平及 LLM 评测分数虚高的问题，构建了包含四种检索任务的大规模基准 CPRet，并提出 Group-InfoNCE 损失训练的专用检索模型 CPRetriever，在所有任务上超越 20+ 现有嵌入模型，同时揭示了题目相似性对 LiveCodeBench 评测的系统性偏差。

**[CryptoMoE: Privacy-Preserving and Scalable Mixture of Experts Inference via Balanced Expert Routing](cryptomoe_privacy-preserving_and_scalable_mixture_of_experts_inference_via_balan.md)**

:   首个支持 MoE 架构 LLM 隐私推理的框架 CryptoMoE，通过平衡专家路由隐藏路由信息、置信度感知调度协议和批量密文矩阵乘法协议，相比 dense baseline 实现 2.8~3.5× 延迟降低和 2.9~4.3× 通信量降低，准确率损失仅 0.8%。

**[CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D](ctrl-alt-deceit_sabotage_evaluations_for_automated_ai_rd.md)**

:   扩展 MLE-Bench 构建了 20 个代码破坏(code-sabotage)任务和 sandbagging 评测，发现前沿 AI agent 能在完成正常 ML 工程任务的同时成功植入后门等破坏，且在部分情况下逃避 LM monitor 的检测。

**[DeepPersona: A Generative Engine for Scaling Deep Synthetic Personas](deeppersona_a_generative_engine_for_scaling_deep_synthetic_personas.md)**

:   提出 DeepPersona——一个两阶段分类引导的合成人格生成引擎：先从真实用户-ChatGPT 对话中挖掘构建 8000+ 节点的人类属性分类树，再通过渐进式属性采样生成平均 200+ 结构化属性的叙事完整人格，在个性化 QA 准确率上提升 11.6%，社会调查模拟偏差缩小 31.7%。

**[DESIGN: Encrypted GNN Inference via Server-Side Input Graph Pruning](design_encrypted_gnn_inference_via_server-side_input_graph_pruning.md)**

:   提出 DESIGN 框架，在全同态加密(FHE)下通过服务器端输入图剪枝和自适应多项式激活度分配两阶段优化，相比 SEAL 基线加速 FHE GNN 推理约 2× 并维持有竞争力的准确率。

**[DictPFL: Efficient and Private Federated Learning on Encrypted Gradients](dictpfl_efficient_and_private_federated_learning_on_encrypted_gradients.md)**

:   提出 DictPFL 框架，通过将模型权重分解为静态字典+可训练查找表，并结合加密感知剪枝，在联邦学习中实现全梯度同态加密保护的同时，将通信开销降低 402–748 倍、训练速度提升 28–65 倍，运行时间仅为明文 FL 的 2 倍以内。

**[Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming](differential_privacy_for_euclidean_jordan_algebra_with_applications_to_private_s.md)**

:   提出了基于 Euclidean Jordan Algebra (EJA) 的通用 Gaussian 隐私机制，并在此基础上设计了首个差分隐私的 Symmetric Cone Programming (SCP) 求解算法，解决了 Hsu et al. (ICALP 2014) 提出的关于差分隐私半定规划的重要开放问题。

**[Differentially Private Bilevel Optimization: Efficient Algorithms with Near-Optimal Rates](differentially_private_bilevel_optimization_efficient_algorithms_with_near-optim.md)**

:   本文系统研究差分隐私 (DP) 下的双层优化问题，在凸情形下通过指数机制和正则化指数机制给出近紧的上下界（匹配单层 DP-ERM 最优率），在非凸情形下提出二阶 DP 方法实现不依赖内层维度的 SOTA 收敛率。

**[Differentially Private Federated Low Rank Adaptation Beyond Fixed-Matrix](differentially_private_federated_low_rank_adaptation_beyond_fixed-matrix.md)**

:   提出FedASK框架，通过**双阶段sketching流水线**（randomized SVD启发），首次在差分隐私下实现联邦LoRA中**两个低秩矩阵A和B的同步有效更新**，在Llama-2 7B/13B上MMLU提升最高11.5%，GSM8K提升46%。

**[Differentially Private High-dimensional Variable Selection via Integer Programming](differentially_private_high-dimensional_variable_selection_via_integer_programmi.md)**

:   本文提出两种纯差分隐私的稀疏变量选择方法 (top-R 和 mistakes)，利用现代混合整数规划 (MIP) 技术高效探索非凸目标景观，在高维设置（p 达 10000）下实现 SOTA 支撑集恢复率，同时提供理论恢复保证。

**[Distributional Adversarial Attacks and Training in Deep Hedging](distributional_adversarial_attacks_and_training_in_deep_hedging.md)**

:   本文首次将分布对抗攻击引入深度对冲框架，提出基于 Wasserstein 球的可计算对抗训练方法（WPGD 和 WBPGD），显著提升了对冲策略在分布偏移和真实市场数据下的鲁棒性与样本外表现。

**[Distributive Fairness in Large Language Models: Evaluating Alignment with Human Values](distributive_fairness_in_large_language_models_evaluating_alignment_with_human_v.md)**

:   本文系统评估多个 SOTA LLM（GPT-4o、Claude-3.5S、Llama3-70b、Gemini-1.5P）在非策略性资源分配任务中的分配公平性偏好，发现 LLM 与人类存在显著偏差：LLM 偏好效率和无嫉妒性 (EF) 而忽视人类更看重的公平性/平等性 (EQ)，但在选择题模式下 GPT-4o 和 Claude 能正确识别公平方案。

**[DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm](dna-detectllm_unveiling_ai-generated_text_via_a_dna-inspired_mutation-repair_par.md)**

:   本文提出 DNA-DetectLLM，一种受 DNA 突变修复机制启发的零样本 AI 文本检测方法，通过构造理想 AI 序列并量化将输入文本修复到该序列的累积难度作为检测信号，在多个基准数据集上取得 AUROC 相对提升 5.55%、F1 提升 2.08% 的 SOTA 效果。

**[Dual-Flow: Transferable Multi-Target, Instance-Agnostic Attacks via In-the-wild Cascading Flow Optimization](dual-flow_transferable_multi-target_instance-agnostic_attacks_via_in-the-wild_ca.md)**

:   本文提出 Dual-Flow 框架，利用预训练扩散模型的正向 ODE 流和微调 LoRA 速度函数的逆向流进行多目标实例无关对抗攻击，通过级联分布偏移训练策略显著提升迁移攻击成功率（从 Inc-v3 到 Res-152 成功率提升 34.58%），在防御模型上也表现出强鲁棒性。

**[Efficient Fairness-Performance Pareto Front Computation](efficient_fairness-performance_pareto_front_computation.md)**

:   提出 MIFPO 方法，无需训练复杂的公平表示模型即可高效计算公平性-性能 Pareto 前沿，通过理论分析将问题化简为紧凑的离散凹优化问题。

**[Efficient Verified Machine Unlearning for Distillation](efficient_verified_machine_unlearning_for_distillation.md)**

:   提出 PURGE 框架，通过教师-学生 constituent mapping 和增量式多教师蒸馏策略，将 SISA 的验证式遗忘扩展到知识蒸馏场景，在教师端遗忘时仅需部分重训学生模型，实现至少 $N\times$ 的加速。

**[Enabling Differentially Private Federated Learning for Speech Recognition: Benchmarks, Adaptive Optimizers and Gradient Clipping](enabling_differentially_private_federated_learning_for_speech_recognition_benchm.md)**

:   首次为端到端ASR建立FL+DP的实用基准，通过**逐层裁剪（per-layer clipping）**结合**LAMB优化器**的层级梯度归一化，在强隐私保证下实现仅1.3%~4.6%的WER绝对退化。

**[Enhancing CLIP Robustness via Cross-Modality Alignment](enhancing_clip_robustness_via_crossmodality_alignment.md)**

:   提出COLA——一个training-free的框架，通过将对抗扰动后的图像特征投影到文本特征张成的子空间来消除非语义噪声，再用最优传输(OT)在分布层面细粒度对齐图文特征，在14个零样本分类基准上平均提升6.7%的对抗鲁棒准确率，同时维持干净样本性能。

**[Enhancing Graph Classification Robustness with Singular Pooling](enhancing_graph_classification_robustness_with_singular_pooling.md)**

:   首次系统分析 flat pooling（Sum/Avg/Max）对图分类对抗鲁棒性的影响，推导各自的对抗风险上界，并提出 RS-Pool——利用节点嵌入矩阵的主奇异向量构建图级表示，在不牺牲 clean accuracy 的前提下显著提升对抗鲁棒性。

**[Environment Inference for Learning Generalizable Dynamical System](environment_inference_for_learning_generalizable_dynamical_system.md)**

:   提出 DynaInfer 框架，通过分析固定神经网络的预测误差来推断未标注轨迹的环境标签，实现无环境标签条件下的动态系统泛化学习，在 ODE/PDE 系统上性能匹配甚至超越 Oracle（已知标签）。

**[Evaluating the Promise and Pitfalls of LLMs in Hiring Decisions](evaluating_the_promise_and_pitfalls_of_llms_in_hiring_decisions.md)**

:   在约 10,000 个真实招聘候选人-职位配对上系统评测了 GPT-4o/4.1、Claude 3.5、Gemini 2.5、Llama 3.1/4、DeepSeek R1 等主流 LLM 的招聘匹配表现，发现专用领域模型 Match Score 在准确性（AUC 0.85 vs 0.77）和公平性（种族 IR 0.957 vs ≤0.809）上全面优于通用 LLM。

**[Exploring the Limits of Strong Membership Inference Attacks on Large Language Models](exploring_the_limits_of_strong_membership_inference_attacks_on_large_language_mo.md)**

:   首次将强成员推断攻击（LiRA）扩展到10M~1B参数的GPT-2规模LLM，训练超过4000个参考模型，揭示四个关键发现：强MIA可以在LLM上成功但效果有限（AUC<0.7），且大量个体样本决策在训练随机性下**与抛硬币无法区分**。

**[Factor Decorrelation Enhanced Data Removal from Deep Predictive Models](factor_decorrelation_enhanced_data_removal_from_deep_predictive_models.md)**

:   提出 DecoRemoval 框架，通过判别性保持的因子去相关（基于随机傅里叶特征的空间映射+自适应权重）和平滑损失扰动两大模块，在不重训的前提下实现数据移除，尤其在分布外（OOD）场景下显著优于现有方法。

**[Fair Minimum Labeling: Efficient Temporal Network Activations for Reachability and Equity](fair_minimum_labeling_efficient_temporal_network_activations_for_reachability_an.md)**

:   本文提出公平最小标注（FML）问题，旨在设计最小代价的时序边激活方案，使网络中各节点组均有足够的时序路径可达性以满足公平覆盖要求；证明该问题是 NP-hard 且难以近似，并基于概率树嵌入给出匹配下界的近似算法。

**[Fair Representation Learning With Controllable High Confidence Guarantees Via Ad](fair_representation_learning_with_controllable_high_confidence_guarantees_via_ad.md)**

:   提出 FRG（Fair Representation learning with high-confidence Guarantees），首个允许用户指定公平性阈值 $\varepsilon$ 和置信水平 $1-\delta$ 的公平表征学习框架：通过 VAE 候选选择 + 对抗推断最大化协方差 + Student's t-检验构造高置信上界，保证对**任意**下游模型和任务，$\Delta_{DP} \leq \varepsilon$ 以至少 $1-\delta$ 概率成立。

**[FairContrast: Enhancing Fairness through Contrastive Learning and Customized Augmentation](faircontrast_enhancing_fairness_through_contrastive_learning_and_customized_augm.md)**

:   FairContrast 提出一种面向表格数据的公平对比学习框架，通过策略性的正对样本选择（将优势组有利结果样本与对应弱势组样本配对），结合有监督或自监督对比损失与交叉熵损失的端到端训练，在不引入额外公平约束损失的前提下显著降低了预测偏差，且精度损失极小。

**[Fairness-Regularized Online Optimization with Switching Costs](fairness-regularized_online_optimization_with_switching_costs.md)**

:   提出 FairOBD 算法，首次在平滑在线凸优化中同时处理**长期公平性正则项**和**切换代价**，通过引入辅助变量分解长期公平代价并用镜像下降更新对偶变量，证明了渐近竞争比保证。

**[Fairness under Competition](fairness_under_competition.md)**

:   本文首次研究竞争环境下多个公平分类器的联合公平性问题，理论证明即使每个分类器都满足 Equal Opportunity (EO)，生态系统可能仍然不公平，且对偏差分类器进行公平性调整反而可能降低生态系统公平性。

**[FedFACT: A Provable Framework for Controllable Group-Fairness Calibration in Federated Learning](fedfact_a_provable_framework_for_controllable_group-fairness_calibration_in_fede.md)**

:   提出FedFACT框架，通过刻画联邦学习下的**贝叶斯最优公平分类器**结构，将公平联邦学习分别在训练中（in-processing）化归为**个性化代价敏感学习**、在训练后（post-processing）化归为**双层优化**，首次实现多类别场景下全局公平性与局部公平性的可控协调，并提供收敛及泛化保证。

**[FedRW: Efficient Privacy-Preserving Data Reweighting for Enhancing Federated Learning of Language Models](fedrw_efficient_privacy-preserving_data_reweighting_for_enhancing_federated_lear.md)**

:   FedRW 提出首个无需可信第三方的联邦学习隐私保护软去重框架，通过安全多方计算获取全局样本频率并进行频率感知的样本加权，在预处理上实现最高 28.78× 加速，在模型性能上实现约 11.42% 的 perplexity 改善。

**[FedSVD: Adaptive Orthogonalization for Private Federated Learning with LoRA](fedsvd_adaptive_orthogonalization_for_private_federated_learning_with_lora.md)**

:   FedSVD 提出通过 SVD 对 LoRA 矩阵进行全局重参数化，在每轮通信后用聚合的 BA 乘积的右奇异向量更新 A 矩阵，避免 DP-SGD 下的二次噪声放大同时保持 A 的自适应能力，在多个 NLU 基准上一致超越固定 A 的基线。

**[Flux Efficient Descriptor-Driven Clustered Federated Learning Under Arbitrary Di](flux_efficient_descriptor-driven_clustered_federated_learning_under_arbitrary_di.md)**

:   提出Flux——基于描述符驱动聚类的联邦学习框架，通过提取隐私保护的客户端数据描述符（分布统计量的矩近似）和无监督密度聚类，自动处理四种分布偏移（特征/标签/P(Y|X)/P(X|Y)），在CheXpert医疗数据集上测试时精度比最佳基线高14.6pp。

**[ForensicHub: A Unified Benchmark & Codebase for All-Domain Fake Image Detection and Localization](forensichub_a_unified_benchmark_codebase_for_all-domain_fake_image_detection_and.md)**

:   ForensicHub 提出首个统一所有域（Deepfake/IMDL/AIGC/文档篡改）的假图检测与定位基准平台，包含 4 个任务、23 个数据集、42 个模型、6 个骨干网络和 11 个 GPU 加速评估指标，通过模块化架构和适配器设计打破领域孤岛，并进行了 16 种跨域评估得出 8 条关键洞察。

**[Geo-Sign: Hyperbolic Contrastive Regularisation for Geometrically Aware Sign Language Translation](geo-sign_hyperbolic_contrastive_regularisation_for_geometrically_aware_sign_lang.md)**

:   Geo-Sign 提出将骨架特征投影到 Poincaré 球模型的双曲空间中，通过双曲对比损失正则化 mT5 语言模型，使其感知手语运动的层次结构，仅用骨架数据就在 CSL-Daily 上超越了基于 RGB 的 SOTA 方法（BLEU-4 +1.81, ROUGE-L +3.03）。

**[HealthSLM-Bench: Benchmarking Small Language Models for Mobile and Wearable Healthcare Monitoring](healthslm-bench_benchmarking_small_language_models_for_mobile_and_wearable_healt.md)**

:   首个系统评估小语言模型 (SLMs, 1-4B参数) 在移动与可穿戴健康监测任务上表现的基准，覆盖zero-shot/few-shot/指令微调三种范式，并在iPhone上验证了端侧部署的可行性。

**[Impact of Dataset Properties on Membership Inference Vulnerability of Deep Transfer Learning](impact_of_dataset_properties_on_membership_inference.md)**

:   本文理论推导并实验验证了深度迁移学习中成员推理攻击（MIA）脆弱性与每类样本数之间的幂律关系 $\log(\text{tpr}-\text{fpr}) = -\beta_S \log(S) - \beta_0$，发现增加数据量可降低平均和最坏情况脆弱性，但保护最脆弱样本需要极大量数据。

**[Impact of Dataset Properties on Membership Inference Vulnerability of Deep Transfer Learning](impact_of_dataset_properties_on_membership_inference_vulnerability_of_deep_trans.md)**

:   从理论和实验两方面揭示深度迁移学习中成员推断攻击 (MIA) 脆弱性与每类样本数之间存在幂律关系：随着每类样本数 $S$ 增加，MIA 优势按 $S^{-1/2}$ 下降，但保护最脆弱样本所需的数据量极大，凸显了差分隐私形式化保障的不可替代性。

**[Incentivizing Time-Aware Fairness in Data Sharing](incentivizing_time-aware_fairness_in_data_sharing.md)**

:   提出了一个时间感知的数据共享框架，设计了新的激励机制（F6-F8）和两种奖励方案（时间感知奖励累计和时间感知数据估值），保证早加入协作的参与方能获得更高价值的奖励，同时兼顾公平性和个体理性。

**[Influence Functions for Edge Edits in Non-Convex Graph Neural Networks](influence_functions_for_edge_edits_in_non-convex_graph_neural_networks.md)**

:   提出适用于非凸 GNN 的边编辑影响函数，通过 proximal Bregman 响应函数放松凸性假设，并同时考虑参数偏移和消息传播两方面的影响，支持边的删除和插入。

**[InvisibleInk: High-Utility and Low-Cost Text Generation with Differential Privacy](invisibleink_high-utility_and_low-cost_text_generation_with_differential_privacy.md)**

:   提出 InvisibleInk 框架，通过差分裁剪（DClip）隔离敏感信息和 Top-$k^+$ 截断采样两项创新，将差分隐私长文本生成的计算成本降低 8 倍以上，首次实现不到非隐私生成 4-8 倍开销的高质量隐私文本生成。

**[It's Complicated: The Relationship of Algorithmic Fairness and Non-Discrimination Provisions for High-Risk Systems in the EU AI Act](its_complicated_the_relationship_of_algorithmic_fairness_and_non-discrimination_.md)**

:   系统分析了欧盟 AI 法案（EU AI Act）中高风险系统的非歧视条款与机器学习算法公平性概念之间的关系，指出两者存在显著脱节并提出未来标准化方向。

**[Keep It Real: Challenges in Attacking Compression-Based Adversarial Purification](keep_it_real_challenges_in_attacking_compression-based_adversarial_purification.md)**

:   本文系统评估了基于图像压缩的对抗净化防御，发现重建图像的"真实感"（realism）是提升防御鲁棒性的关键因素——高真实感压缩模型在面对强自适应攻击时仍能保持显著鲁棒性，而这并非源于梯度掩蔽。

**[LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory](llm_strategic_reasoning_agentic_study_through_behavioral_gam.md)**

:   论文不再把大模型战略推理简单等同于“是否接近纳什均衡”，而是基于 behavioral game theory 构建评测框架，区分真实推理能力与上下文因素，系统测评 22 个 LLM 的互动决策行为，发现模型规模并不决定战略水平，CoT 提升也并非普遍有效，同时暴露出显著的人口属性偏置。

**[Locally Optimal Private Sampling: Beyond the Global Minimax](locally_optimal_private_sampling_beyond_the_global_minimax.md)**

:   在本地差分隐私（LDP）下的采样问题中，提出**局部minimax**框架，利用公共数据分布 $P_0$ 定义的邻域约束，推导出闭式最优采样器，在理论和实验上均**一致优于全局minimax采样器**。

**[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](machine_unlearning_doesnt_do_what_you_think_lessons_for_generative_ai_policy_and.md)**

:   系统性论证"机器遗忘"（machine unlearning）并非万能方案，识别出遗忘动机与可行实现之间的五大根本错配（mismatches），为 ML 研究者和政策制定者提供严谨的分析框架。

**[Matchings Under Biased and Correlated Evaluations](matchings_under_biased_and_correlated_evaluations.md)**

:   在两机构稳定匹配模型中引入评估相关性参数 $\gamma$（机构间评分的对齐程度），分析偏差 $\beta$ 和相关性 $\gamma$ 如何联合影响弱势群体的代表性比率，证明即使轻微的相关性损失也可导致代表性急剧下降，并提出公平性干预策略的 Pareto 前沿。

**[Mitigating Privacy-Utility Trade-off in Decentralized Federated Learning via f-Differential Privacy](mitigating_privacy-utility_trade-off_in_decentralized_federated_learning_via_f-d.md)**

:   提出基于 f-DP 框架的两种去中心化联邦学习隐私记账方法——PN-f-DP 和 Sec-f-LDP，通过更精细的假设检验隐私度量，一致性地获得比 Rényi DP 更紧的隐私界，从而在相同隐私保证下减少噪声注入、提升模型效用。

**[Nearly-Linear Time Private Hypothesis Selection with the Optimal Approximation Factor](nearly-linear_time_private_hypothesis_selection_with_the_optimal_approximation_f.md)**

:   首次提出在中心差分隐私模型下同时实现近线性时间复杂度和最优近似因子 $\alpha=3$ 的假设选择算法，解决了Bun等人（NeurIPS 2019）提出的开放问题。

**[OmniFC: Rethinking Federated Clustering via Lossless and Secure Distance Reconstruction](omnifc_rethinking_federated_clustering_via_lossless_and_secure_distance_reconstr.md)**

:   提出 OmniFC，一个模型无关的联邦聚类框架：通过 Lagrange 编码计算在有限域上精确重建全局成对距离矩阵，任意集中式聚类方法（K-Means/谱聚类/DBSCAN/层次聚类等）可直接在其上运行，仅需一轮通信，天然抵抗 Non-IID，在 7 个数据集上全面超越 k-FED/MUFC/FedSC 等专用方法。

**[On the Hardness of Conditional Independence Testing In Practice](on_the_hardness_of_conditional_independence_testing_in_practice.md)**

:   系统分析了基于核的条件独立性（CI）检验在实践中失败的根本原因：条件均值嵌入的估计误差是导致Type-I错误膨胀的核心因素，同时揭示了选择条件核$k_C$对检验功效至关重要但会加剧假阳性的内在张力。

**[On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks](on_the_robustness_of_verbal_confidence_of_llms_in_adversarial_attacks.md)**

:   首次系统研究 LLM 语言化置信度（verbal confidence）在对抗攻击下的鲁棒性，提出基于扰动和越狱的攻击框架，揭示攻击可导致置信度下降最高 30%、答案翻转率高达 100%，且现有防御策略基本无效。

**[On the Sample Complexity of Differentially Private Policy Optimization](on_the_sample_complexity_of_differentially_private_policy_optimization.md)**

:   首次系统性研究差分隐私（DP）约束下策略优化的样本复杂度，提出统一的元算法框架，分析DP-PG、DP-NPG和DP-REBEL三种隐私策略优化算法，证明隐私代价通常仅作为样本复杂度的低阶项出现。

**[Provable Watermarking for Data Poisoning Attacks](provable_watermarking_for_data_poisoning_attacks.md)**

:   本文提出两种可证明的水印方案（后投毒水印和投毒并行水印），为数据投毒攻击提供透明性声明机制，理论证明在特定水印长度条件下可同时保证水印可检测性和投毒有效性。

**[Reconstruction and Secrecy under Approximate Distance Queries](reconstruction_and_secrecy_under_approximate_distance_queries.md)**

:   在近似距离查询模型下，通过学习理论视角研究重建博弈（reconstruction game），证明了最优重建误差等于Chebyshev半径的几何特征刻画，并对欧氏凸空间的伪有限性给出了完整分类。

**[The Unseen Threat Residual Knowledge In Machine Unlearning Under Perturbed Sampl](the_unseen_threat_residual_knowledge_in_machine_unlearning_under_perturbed_sampl.md)**

:   发现机器遗忘的关键安全漏洞：即使遗忘后的模型在统计意义上与重训练模型不可区分，对遗忘样本施加微小对抗扰动后，遗忘模型仍能正确识别而重训练模型则失败——揭示了"残余知识"这一新型隐私风险。提出 RURK 微调策略，通过惩罚对扰动遗忘样本的正确预测来消除残余知识，在 CIFAR-10 和 ImageNet-100 上有效抑制 11 种遗忘方法的残余知识。

**[Understanding and Improving Adversarial Robustness of Neural Probabilistic Circuits](understanding_and_improving_adversarial_robustness_of_neural_probabilistic_circu.md)**

:   理论分析神经概率电路（NPC）的对抗鲁棒性仅取决于属性识别模型而与概率电路无关，并提出 RNPC 通过类级推理集成方式实现可证明的鲁棒性提升，在保持良性准确率的同时显著增强对抗鲁棒性。
