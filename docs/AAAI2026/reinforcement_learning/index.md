<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**🤖 AAAI2026** · 共 **27** 篇

**[A Course Correction in Steerability Evaluation: Revealing Miscalibration and Side Effects in LLMs](a_course_correction_in_steerability_evaluation_revealing_mis.md)**

:   本文提出了一个基于多维目标空间的 LLM 可操控性（steerability）评估框架，将 steering error 分解为校准偏差（miscalibration）和副作用（side effects/orthogonality），在文本改写任务上发现即使是最强的 LLM 也会产生严重副作用，prompt engineering 无效、best-of-N 采样代价高、RL 微调有改善但仍未彻底解决。

**[A Learning Framework For Cooperative Collision Avoidance of UAV Swarms Leveraging Domain Knowledge](a_learning_framework_for_cooperative_collision_avoidance_of_.md)**

:   提出 reMARL 框架，将图像处理中的主动轮廓模型（active contour）作为领域知识引入多智能体强化学习的奖励设计，使无人机集群仅通过最大化个体奖励即可学会协作避撞，在大规模集群（≤10架）中性能显著优于 COMA/VDN/QMIX/MAPPO 等 SOTA MARL 方法，反应时间比元启发式方法快 98.75%，能耗降低 85.37%。

**[A Learning Framework For Cooperative Collision Avoidance of UAV Swarms Leveraging Domain Knowledge](a_learning_framework_for_cooperative_collision_avoidance_of_uav_swarms_leveragin.md)**

:   提出 reMARL 框架，利用图像处理领域知识（active contour model）设计多智能体强化学习奖励函数，实现无人机集群的协作避碰，相比传统元启发式方法反应时间缩短 98.75%、能耗降低 85.37%。

**[A Multi-Agent Conversational Bandit Approach to Online Evaluation and Selection of User-Aligned LLM Responses](a_multi-agent_conversational_bandit_approach_to_online_evaluation_and_selection_.md)**

:   提出 MACO 多智能体会话式 Bandit 框架，通过本地 agent 的在线淘汰和云服务器的自适应偏好查询机制，实现 LLM 响应的在线评估与用户偏好对齐，达到 $\tilde{O}(\sqrt{dMT})$ 的近优 regret 界。

**[Aligning Machiavellian Agents: Behavior Steering via Test-Time Policy Shaping](aligning_machiavellian_agents_behavior_steering_via_test-tim.md)**

:   提出一种测试时策略塑形方法，通过轻量级伦理属性分类器在推理阶段插值修改预训练 RL 智能体的动作概率分布，无需重训练即可实现对多种伦理属性的细粒度行为引导。

**[BAMAS: Structuring Budget-Aware Multi-Agent Systems](bamas_structuring_budget-aware_multi-agent_systems.md)**

:   提出 BAMAS 框架，通过整数线性规划（ILP）在预算约束下选择最优 LLM 组合，再用强化学习策略选择最佳协作拓扑（线性/星型/反馈/规划驱动），在 GSM8K/MBPP/MATH 上达到与 SOTA 多 Agent 系统相当的准确率，同时成本降低最高 86%。

**[Behaviour Policy Optimization: Provably Lower Variance Return Estimates for Off-Policy Reinforcement Learning](behaviour_policy_optimization_provably_lower_variance_return_estimates_for_off-p.md)**

:   提出 Behaviour Policy Optimization (BPO)，通过优化一个专用行为策略来采集离策略数据，使得回报估计的方差可证明低于在策略采集，从而提升 REINFORCE 和 PPO 的样本效率与稳定性。

**[Beyond Monotonicity: Revisiting Factorization Principles in Multi-Agent Q-Learning](beyond_monotonicity_revisiting_factorization_principles_in_multi-agent_q-learnin.md)**

:   通过动力系统分析证明：在近似贪心探索策略下，非单调值分解Q学习中所有违反IGM一致性的零损失解都是不稳定鞍点，只有IGM一致解才是稳定吸引子，因此无需单调性约束即可可靠收敛到最优解。

**[Beyond the Lower Bound: Bridging Regret Minimization and Best Arm Identification in Lexicographic Bandits](beyond_the_lower_bound_bridging_regret_minimization_and_best_arm_identification_.md)**

:   提出两种消除式算法 LexElim-Out 和 LexElim-In，首次在词典序多目标赌博机中同时解决遗憾最小化（RM）和最优臂识别（BAI）问题，其中 LexElim-In 通过跨目标信息共享突破了单目标问题的已知下界。

**[Bi-Level Contextual Bandits for Individualized Resource Allocation under Delayed Feedback](bi-level_contextual_bandits_for_individualized_resource_allocation_under_delayed.md)**

:   提出 MetaCUB——一种双层上下文赌博机框架，在延迟反馈、动态人群、冷却约束和公平性要求下实现个体化资源分配，元层优化子群预算分配保证公平，基层利用 UCB 策略选择最有潜力的个体。

**[ChartEditor: A Reinforcement Learning Framework for Robust Chart Editing](charteditor_a_reinforcement_learning_framework_for_robust_chart_editing.md)**

:   提出 ChartEditVista 基准（7,964 样本、31 种图表类型）和 ChartEditor 模型，通过 GRPO 强化学习框架结合新颖的 rendering reward，仅用 3B 参数即在图表编辑任务上超越 GPT-4o 和多个 72B 级模型。

**[CHDP: Cooperative Hybrid Diffusion Policies for RL in Parametric Environments](chdp_cooperative_hybrid_diffusion_policies_for_reinforcement_learning_in_paramet.md)**

:   将混合动作空间问题建模为两个agent的全合作博弈，分别用离散和连续扩散策略生成动作，通过顺序更新和Q引导码本解决策略冲突与高维可扩展性问题，成功率最高提升19.3%。

**[Deep (Predictive) Discounted Counterfactual Regret Minimization](deep_predictive_discounted_counterfactual_regret_minimization.md)**

:   提出VR-DeepDCFR+和VR-DeepPDCFR+两种无模型神经CFR算法，通过自举累积优势估计、折扣裁剪机制和基线方差缩减，首次将高级表格CFR变体（DCFR+/PDCFR+）有效整合到神经网络近似框架中，在典型不完全信息博弈中实现更快收敛。

**[DeepProofLog: Efficient Proving in Deep Stochastic Logic Programs](deepprooflog_efficient_proving_in_deep_stochastic_logic_programs.md)**

:   提出DeepProofLog（DPrL），一种基于随机逻辑程序的神经符号系统，通过在每个证明步骤引入神经网络参数化，并建立SLD解析过程与MDP的形式化映射，使得动态规划和强化学习技术可用于高效推理与学习，显著提升了神经符号系统的可扩展性。

**[DiffOP: Reinforcement Learning of Optimization-Based Control Policies via Implicit Policy Gradients](diffop_reinforcement_learning_of_optimization-based_control_policies_via_implici.md)**

:   提出 DiffOP 框架，将优化型控制策略（如 MPC）视为可微分模块，通过隐式微分推导解析策略梯度，实现端到端强化学习训练，并给出首个非渐近收敛保证。

**[Discounted Cuts: A Stackelberg Approach to Network Disruption](discounted_cuts_a_stackelberg_approach_to_network_disruption.md)**

:   引入“折扣切割”概念——在经典最小切割问题上加入攻击者可免除 k 条最贵/最便宜边的折扣机制，建模为 Stackelberg 攻防博弈，提供了 8 种折扣切割变体的完整复杂度分类，并证明所有变体在有界亏格图上均可多项式时间求解。

**[Distilling Deep RL into Interpretable Fuzzy Rules](distilling_deep_reinforcement_learning_into_interpretable_fuzzy_rules_an_explain.md)**

:   提出层次化 TSK 模糊分类系统，将深度 RL 的神经策略蒸馏为人类可读的 IF-THEN 规则，通过 K-Means 分区状态空间 + Ridge 回归学习局部动作推断，在 LunarLander 上达到 81.5% 保真度（比决策树高 21%），并引入 FRAD/FSC/ASG 三个可量化可解释性指标。

**[Do It for HER: First-Order Temporal Logic Reward Specification in RL](do_it_for_her_first-order_temporal_logic_reward_specification_in_reinforcement_l.md)**

:   提出基于 LTLfMT（线性时序逻辑模理论）的 RL 奖励规范框架，用一阶逻辑谓词替代布尔原子使得奖励可直接定义在连续/异构状态上（无需手工标签函数），并组合 CRM+HER 解决逻辑规范的稀疏奖励问题。

**[Does Self-Evaluation Enable Wireheading in Language Models?](does_self-evaluation_enable_wireheading_in_language_models.md)**

:   本文理论证明并实验验证了当语言模型的自我评估与奖励信号耦合时，模型会系统性地膨胀自评分（wireheading），而解耦自评分与奖励可以缓解这一问题；在Llama-3.1-8B和Mistral-7B上三个任务的实验表明，摘要等模糊任务中自评分膨胀高达0.92。

**[HCPO: Hierarchical Conductor-Based Policy Optimization in Multi-Agent Reinforcement Learning](hcpo_hierarchical_conductor-based_policy_optimization_in_multi-agent_reinforceme.md)**

:   提出 HCPO 算法，通过引入 conductor（指挥者）机制增强多智能体联合策略的表达能力和探索效率，构建类似 Gaussian mixture model 的联合策略框架，并证明两级策略更新的单调改进保证。

**[MARS: Multi-Agent Adaptive Reasoning with Socratic Guidance for Automated Prompt Optimization](mars_multi-agent_adaptive_reasoning_with_socratic_guidance_f.md)**

:   提出 MARS 五智能体框架做自动提示优化（APO）：Planner 生成任务特定的优化轨迹，Teacher-Critic-Student 三体进行苏格拉底对话式迭代精炼 prompt（模拟文本空间中的伪梯度下降），Target 执行并反馈，整体建模为 POMDP，在 17 个数据集上平均超越前 SOTA（PE2）6.04%（通用任务）和 6.42%（领域任务），且仅需 1-shot 训练数据。

**[MMhops-R1: Multimodal Multi-hop Reasoning](mmhops-r1_multimodal_multi-hop_reasoning.md)**

:   提出了 MMhops 基准（31K 样本、3-4 跳推理深度）和 MMhops-R1 框架，通过强化学习训练 MLLM 自主规划推理路径、动态调用图像/文本检索器，实现多模态多跳推理，7B 模型超越 72B 基线和现有 mRAG 方法。

**[One-Step Generative Policies with Q-Learning: A Reformulation of MeanFlow](one-step_generative_policies_with_q-learning_a_reformulation_of_meanflow.md)**

:   将MeanFlow重新形式化为残差映射 $g(a_t,b,t) = a_t - u(a_t,b,t)$，实现一步噪声→动作的生成式策略，无需蒸馏或多步ODE积分，可直接与Q-learning联合训练，在OGBench和D4RL的73个任务上取得强性能。

**[Provably Efficient Multi-Objective Bandit Algorithms under Preference-Centric Customization](provably_efficient_multi-objective_bandit_algorithms_under_preference-centric_cu.md)**

:   首次从理论角度研究显式用户偏好下的多目标多臂赌博机（MO-MAB）定制化优化问题，提出 PAMO-MAB 框架并针对"未知偏好"和"隐藏偏好"两种场景分别设计 PRUCB-UP 和 PRUCB-HP 算法，通过偏好估计 + 偏好感知优化的双组件框架实现近最优遗憾界，证明了 preference-free 算法在 Pareto 前沿冲突时必然产生 $\Omega(T)$ 线性遗憾。

**[Risk-Sensitive Exponential Actor Critic](risk-sensitive_exponential_actor_critic.md)**

:   针对 entropic risk measure 下 policy gradient 的高方差和数值不稳定问题，推导了完整的 on/off-policy 风险敏感策略梯度定理，并提出 rsEAC 算法，通过 log-domain critic 参数化和梯度归一化裁剪机制实现稳定的风险敏感连续控制。

**[Test-driven Reinforcement Learning in Continuous Control](test-driven_reinforcement_learning_in_continuous_control.md)**

:   提出 Test-driven Reinforcement Learning (TdRL) 框架，用多个测试函数（pass-fail 测试定义最优目标 + indicative 测试引导学习）替代单一奖励函数表示任务目标，通过字典序启发式轨迹比较学习回报函数，在 DeepMind Control Suite 上匹配或超越手工奖励方法，天然支持多目标优化。

**[Thinker: Training LLMs in Hierarchical Thinking for Deep Search via Multi-Turn Interaction](thinker_training_llms_in_hierarchical_thinking_for_deep_search_via_multi-turn_in.md)**

:   提出 Thinker 框架，通过分层思维（breadth decomposition + depth solving）和双重表征（自然语言 + 逻辑函数）实现结构化的深度搜索推理，配合知识边界判定减少不必要检索，以 SFT 方式训练，在多个 QA 基准上显著超越 RL-based deep search 方法。
