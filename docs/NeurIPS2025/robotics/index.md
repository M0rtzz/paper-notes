<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 机器人/具身智能

**🧠 NeurIPS2025** · 共 **30** 篇

**[A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning](a_snapshot_of_influence_a_local_data_attribution_framework_f.md)**

:   首次将数据归因（data attribution）引入在线强化学习，提出局部归因框架量化每条训练记录对策略更新的贡献，并基于此设计了迭代影响力过滤算法（IIF），在经典RL基准和LLM的RLHF上均显著提升了样本效率和最终性能。

**[Adaptive Frontier Exploration on Graphs with Applications to Network-Based Disease Testing](adaptive_frontier_exploration_on_graphs_with_applications_to_network-based_disea.md)**

:   提出 Adaptive Frontier Exploration on Graphs (AFEG) 问题框架，设计基于 Gittins index 的策略，在图是森林时可证明最优，在实际性传播疾病检测网络上仅测试一半人口即可检出几乎全部 HIV 感染者，大幅超越贪心和 DQN 等基线。

**[AutoToM: Scaling Model-based Mental Inference via Automated Agent Modeling](autotom_scaling_model-based_mental_inference_via_automated_agent_modeling.md)**

:   AutoToM 实现完全自动化的基于模型的心智理论推理——自动提出 agent 模型（贝叶斯网络结构）并进行贝叶斯逆规划，通过推理不确定性迭代调整模型（添加心智变量/扩展时间步），在5个 ToM benchmark 上超越 SOTA LLM 和推理模型，且产生类人的置信度估计。

**[Beyond Parallelism: Synergistic Computational Graph Effects in Multi-Head Attention](beyond_parallelism_synergistic_computational_graph_effects_in_multi-head_attenti.md)**

:   将多头注意力重新建模为共享汇节点的多个前馈 DAG 系统，理论证明多头可通过跨头路径实现协同效应——降低混合时间(mixing time)并放大 minimax 保真度(fidelity)，在序列操作任务上实验验证了该效应。

**[Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots](bridging_embodiment_gaps_deploying_vision-language-action_models_on_soft_robots.md)**

:   首次在柔性连续体机械臂上部署 VLA 模型（OpenVLA-OFT 和 π₀），发现开箱即用的策略因构型不匹配完全失败，但通过针对性微调可弥合刚性-柔性的 embodiment gap，使柔性机器人在操作任务上达到与刚性 UR5 相当的成功率——证明 VLA + 柔性机器人可实现安全的人机交互。

**[C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](c-nav_towards_self-evolving_continual_object_navigation_in_open_world.md)**

:   提出 C-Nav 框架，通过**双路径抗遗忘**（特征蒸馏 + 特征回放）和**自适应经验选择**（LOF 异常检测选关键帧），让导航智能体在不断学习新物体类别时避免灾难性遗忘，在 4 种架构上均超越全量数据回放基线。

**[Can Agents Fix Agent Issues](can_agents_fix_agent_issues.md)**

:   AgentIssue-Bench(50个bug任务)评估SE代理解决LLM代理bug的能力，仅0.67%-4.67%解决率。

**[CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification](cogvla_cognition-aligned_vision-language-action_model_via_instruction-driven_rou.md)**

:   提出 CogVLA——模仿人类多模态认知的三阶段 VLA 架构：(1) EFA-Routing 将视觉 token 压缩至 25%；(2) LFP-Routing 裁剪 50% 的 LLM 无关 token；(3) V-L-A 耦合注意力保持语义一致性——在 LIBERO 上达 97.4% 成功率，训练成本降 2.5×，推理延迟降 2.8×。

**[C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](coopera_continual_open-ended_human-robot_assistance.md)**

:   提出 C-Nav 持续目标导航框架，通过**双路径抗遗忘机制**（特征蒸馏 + 特征回放）和**基于 LOF 的自适应经验选择**，使导航智能体在增量学习新物体类别时有效避免灾难性遗忘，在 4 种主流架构和 2 个数据集上均超越全量数据回放基线。

**[DexFlyWheel: A Scalable Self-Improving Data Generation Framework for Dexterous Manipulation](dexflywheel_a_scalable_and_self-improving_data_generation_framework_for_dexterou.md)**

:   提出 DexFlyWheel，一个从单个人类示教出发、通过 IL + 残差 RL + 数据增强组成的自改进循环逐步扩展数据多样性的灵巧操作数据生成框架，在 4 个任务上生成 2000+ 示教，策略平均成功率 81.9%，真实世界迁移成功率 78.3%。

**[DynaNav: Dynamic Feature and Layer Selection for Efficient Visual Navigation](dynanav_dynamic_feature_and_layer_selection_for_efficient_visual_navigation.md)**

:   提出 DynaNav，通过可训练的硬特征选择器和基于贝叶斯优化的 early-exit 机制，根据场景复杂度动态调整特征与层的使用，在视觉导航中实现 2.26× FLOPs 降低、42.3% 推理时间减少，同时保持甚至提升导航性能。

**[EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](efficientnav_towards_on-device_object-goal_navigation_with_navigation_map_cachin.md)**

:   通过离散内存缓存（KV cache分组独立计算+选择性加载）、注意力驱动聚类（LLM浅层attention指导分组）和语义感知检索（CLIP+背包问题适配不同内存预算），首次在Jetson Orin上用LLaMA-3.2-11b实现零样本ObjNav，比GPT-4基线提升11.1% SR且实时延迟降低6.7×。

**[EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT](egothinker_unveiling_egocentric_reasoning_with_spatiotempora.md)**

:   针对第一人称视频推理中“主体不可见、意图隐含、交互细粒度”的挑战，EgoThinker 提出时空 CoT 监督与两阶段训练（SFT + RFT），并构建 EgoRe-5M 大规模 egocentric QA 数据，显著提升 MLLM 在自我中心视频推理与时空定位任务上的表现。

**[Enginuity: Building an Open Multi-Domain Dataset of Complex Engineering Diagrams](enginuity_building_an_open_multi-domain_dataset_of_complex_engineering_diagrams.md)**

:   提出 Enginuity——首个大规模开放多领域工程图数据集（50K+ 标注图），涵盖层级组件关系与连接语义，旨在突破当前 AI 无法理解工程图中视觉-结构知识的瓶颈。

**[Explaining and Mitigating Crosslingual Tokenizer Inequities](explaining_and_mitigating_crosslingual_tokenizer_inequities.md)**

:   系统训练约 7000 个单语分词器覆盖 97 种语言，首次证明即使控制训练数据量、词表大小和算法后，不同语言间仍存在显著的 token premium 差异；进一步识别出词表大小和预分词策略是关键因素，并提出"最优词表大小"和 SuperBPE 两种缓解方案。

**[FALCON: Fine-grained Activation Manipulation by Contrastive Orthogonal Unalignment for Large Language Model](falcon_fine-grained_activation_manipulation_by_contrastive_orthogonal_unalignmen.md)**

:   提出 FALCON——基于表示引导的 LLM 遗忘框架，利用互信息进行参数选择、对比机制实现精细知识分离、梯度正交投影解决遗忘-保留冲突，在有害知识/版权/实体遗忘任务上全面超越现有方法。

**[Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training](generalizable_domain_adaptation_for_sim-and-real_policy_co-training.md)**

:   提出基于不平衡最优运输（UOT）的模拟-真实策略联合训练框架，通过对观察-动作联合分布进行对齐（而非仅对齐观察边际分布），结合时间对齐采样策略处理数据不平衡，在机器人操纵任务上实现30%的OOD泛化提升。

**[Harnessing the Computation Redundancy in ViTs to Boost Adversarial Transferability](harnessing_the_computation_redundancy_in_vits_to_boost_adversarial_transferabili.md)**

:   深入挖掘 ViT 中数据级和模型级的计算冗余，提出注意力稀疏化、注意力头置换、干净 token 正则化、Ghost MoE 多样化和鲁棒化 token 五种技术，结合在线学习策略动态选择操作，在 ImageNet-1K 上以 86.9% 平均 fooling rate 大幅超越所有基线。

**[HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data](himacon_discovering_hierarchical_manipulation_concepts_from_unlabeled_multi-moda.md)**

:   提出自监督框架从无标注多模态机器人演示中学习层级操作概念，通过跨模态相关性网络和多时域子目标预测器组织表示，增强模仿学习策略在新物体、新障碍和新环境下的泛化能力。

**[Knolling Bot: Teaching Robots the Human Notion of Tidiness](knolling_bot_teaching_robots_the_human_notion_of_tidiness.md)**

:   提出基于 Transformer + GMM 的自监督学习框架，让机器人从 240 万组整理示范中学习"整洁"的抽象概念，以自回归方式预测物体目标位置，实现桌面物体的美观且紧凑的自动整理（knolling），并支持基于用户偏好（颜色/类别/大小）生成多样化整理方案。

**[LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](labutopia_high-fidelity_simulation_and_hierarchical_benchmark_for_scientific_emb.md)**

:   提出 LabUtopia——面向科学实验室的高保真仿真与层级基准套件，包含支持化学反应建模的 LabSim 仿真器、可程序化生成实验室场景的 LabScene、以及从原子操作到长程移动操纵的五级 LabBench 基准，揭示现有模仿学习方法在长程实验流程和物体泛化方面的显著瓶颈。

**[LatentGuard: Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation](latentguard_controllable_latent_steering_for_robust_refusal_of_attacks_and_relia.md)**

:   提出 LatentGuard 三阶段框架，通过行为级对齐微调 + 结构化 VAE 监督潜空间 + 潜空间维度操控，实现对 LLM 拒绝行为的可解释、可控制调节，在抵御对抗攻击的同时保持对正常查询的响应能力。

**[Manipulating Feature Visualizations With Gradient Slingshots](manipulating_feature_visualizations_with_gradient_slingshots.md)**

:   提出梯度弹弓攻击，通过利用分布外梯度轨迹操纵神经网络特征可视化结果，无需修改模型参数，揭示特征可视化作为解释性工具的脆弱性。

**[MindForge: Empowering Embodied Agents with Theory of Mind for Lifelong Cultural Learning](mindforge_empowering_embodied_agents_with_theory_of_mind_for_lifelong_cultural_l.md)**

:   MindForge 为 LLM 驱动的具身智能体引入显式的心智理论（ToM）表征、自然语言通信和多组件记忆系统，使开源 LLM 智能体通过与专家协作对话（无需梯度更新）大幅提升任务完成率，在 Minecraft 中比 Voyager 多获得 3× 科技树里程碑和 2.3× 独特物品。

**[MineAnyBuild: Benchmarking Spatial Planning for Open-world AI Agents](mineanybuild_benchmarking_spatial_planning_for_openworld_ai.md)**

:   基于 Minecraft 构建空间规划基准 MineAnyBuild，要求 AI Agent 根据多模态指令生成可执行的建筑蓝图矩阵，包含 4000 个任务和 500+ 建筑/装饰资产，从空间理解、空间推理、创造力和空间常识四个维度系统评估 MLLM 的空间规划能力，揭示即便 GPT-4o 整体得分仅 41.02/100，开源模型更差。

**[MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](mip_against_agent_malicious_image_patches_hijacking_multimod.md)**

:   揭示针对多模态OS Agent的新型攻击向量——Malicious Image Patches (MIPs)：在屏幕截图中嵌入人类不可察觉的对抗性扰动图像块，当OS Agent截屏时自动触发恶意行为（如数据泄露、内存溢出），且可跨用户指令、屏幕布局和屏幕解析器泛化，甚至具备"计算机蠕虫"般的自传播潜力。

**[mmWalk: Towards Multi-modal Multi-view Walking Assistance](mmwalk_towards_multi-modal_multi-view_walking_assistance.md)**

:   mmWalk 构建了首个面向视障人群步行辅助的多模态多视角数据集（CARLA 仿真器生成 62K 帧/559K 全景图 + 69K VQA 对），基准测试发现 SOTA VLM 在风险评估和导航地标识别等安全关键任务上表现不足（最优仅 55.21%），微调后在真实数据集上泛化提升 16.7%。

**[SegMASt3R: Geometry Grounded Segment Matching](segmast3r_geometry_grounded_segment_matching.md)**

:   SegMASt3R 在预训练 MASt3R 3D 基础模型上添加轻量分割特征头和可微 Sinkhorn 匹配层，利用 3D 几何先验实现极端视角变化（达 180°）下的鲁棒语义段匹配，AUPRC 在 135-180° 基线上达 83.6%（vs SAM2 的 17%）。

**[Talk2Event Grounded Understanding Of Dynamic Scenes From Event Cameras](talk2event_grounded_understanding_of_dynamic_scenes_from_event_cameras.md)**

:   Talk2Event 提出首个大规模事件相机视觉定位基准（30,690 条标注表达式 + 四种定位属性），并设计 EventRefer 框架通过混合事件-属性专家（MoEE）动态融合外观/状态/观察者关系/物体间关系特征，在纯事件、纯帧和融合三种设置下均超越现有方法。

**[Toward Engineering Agi Benchmarking The Engineering Design Capabilities Of Llms](toward_engineering_agi_benchmarking_the_engineering_design_capabilities_of_llms.md)**
