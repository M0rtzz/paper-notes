<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 机器人/具身智能

**📷 CVPR2026** · 共 **34** 篇

**[Action–Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation](actiongeometry_prediction_with_3d_geometric_prior.md)**

:   利用预训练3D几何基础模型π3作为感知骨干，融合3D几何、2D语义和本体感知特征，通过扩散模型联合预测未来动作chunk和未来3D Pointmap，仅使用RGB输入就在RoboTwin双臂基准上全面超越点云方法。

**[Ada3Drift: Adaptive Training-Time Drifting for One-Step 3D Visuomotor Robotic Manipulation](ada3drift_adaptive_training-time_drifting_for_one-step_3d_visuomotor_robotic_man.md)**

:   针对扩散策略多步去噪慢、Flow Matching 单步快但模式平均导致碰撞的问题，提出 Ada3Drift：在训练阶段构造 drifting field 将预测吸引到最近 expert demonstration 并排斥其他模式，配合多尺度场聚合和 sigmoid 调度损失过渡，实现 1 NFE 推理下保持多模态动作分布，在 Adroit/Meta-World/RoboTwin 和真实机器人上达到 SOTA。

**[Ada3Drift: Adaptive Training-Time Drifting for One-Step 3D Visuomotor Robotic Manipulation](ada3drift_adaptive_trainingtime_drifting_for_onest.md)**

:   利用计算预算不对称性，将扩散策略的迭代细化从推理时移至训练时——通过自适应漂移场将预测动作吸引向专家模式并排斥其他生成样本，从3D点云实现单步（1 NFE）高保真多模态动作生成，比扩散策略快10倍以上。

**[AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](atomicvla_unlocking_the_potential_of_atomic_skill.md)**

:   AtomicVLA 提出统一规划-执行框架，通过Think-Act自适应切换生成任务链和原子技能抽象，用技能引导MoE（SG-MoE）构建可扩展的原子技能专家库，在LIBERO-LONG上超π₀ 10%，真实世界持续学习超基线21%且遗忘仅1.3%。

**[AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](atomicvla_unlocking_the_potential_of_atomic_skill_learning_in_robots.md)**

:   提出AtomicVLA，统一任务规划(thinking)和动作执行(acting)，通过自适应[think]/[act]切换、技能引导MoE(SG-MoE)和可扩展持续学习机制，在LIBERO-LONG上超越π₀达10%，真实Franka长任务+18.3%，实现高效的原子技能分解与持续获取。

**[Chain of World: World Model Thinking in Latent Motion (CoWVLA)](chain_of_world_world_model_thinking_in_latent_motion.md)**

:   提出CoWVLA，统一世界模型VLA和隐动作VLA的优势：通过Latent Motion Extractor将视频分解为结构隐变量和运动隐变量，VLA在隐运动空间做世界模型预测而非重建冗余像素，配合Co-Fine-tuning交替生成关键帧和动作token，LIBERO-LONG达95.2%超越π₀(85.2%)，SimplerEnv-WidowX avg 0.560超π₀(0.425)。

**[Cross-Domain Demo-To-Code Via Neurosymbolic Counterfactual Reasoning](cross-domain_demo-to-code_via_neurosymbolic_counterfactual_reasoning.md)**

:   提出 NeSyCR 神经符号反事实推理框架，将视频示教抽象为符号世界模型，通过反事实状态推演检测跨域不兼容并自动修正程序步骤，在跨域 demo-to-code 任务上比最强基线 Statler 提升 31.14% 成功率。

**[DAWN: Pixel Motion Diffusion is What We Need for Robot Control](dawn_pixel_motion_diffusion_robot_control.md)**

:   提出 DAWN，一个两阶段全扩散的视觉语言动作框架——Motion Director（潜扩散模型）生成稠密像素运动场作为可解释的中间表示，Action Expert（扩散 Transformer 策略）将像素运动转换为可执行机器人动作；在 CALVIN 基准上取得 SOTA（平均长度 4.00），并在真实世界单臂/双臂操控中展现强泛化能力。

**[Decovln Decoupling Observation Reasoning And Correction For Vision-And-Language ](decovln_decoupling_observation_reasoning_and_correction_for_vision-and-language_.md)**

:   提出 DecoVLN 框架，将 VLN 任务中的观察、推理和纠错三个过程解耦，通过自适应记忆优化机制和基于状态-动作对的纠错微调策略，在仅使用自中心 RGB 输入的条件下实现了 R2R-CE 和 RxR-CE 上的 SOTA 性能。

**[Expert Pyramid Tuning: Efficient Parameter Fine-Tuning for Expertise-Driven Task Allocation](expert_pyramid_tuning_efficient_parameter_fine-tuning_for_expertise-driven_task_.md)**

:   针对MoE-LoRA方法中所有expert结构相同（统一rank）导致无法适配不同复杂度任务的问题，提出EPT：通过共享meta-knowledge子空间 + 不同kernel size的反卷积expert构建参数金字塔，配合Adaptive LoRA Pruner和对比学习Task Embedding，在GLUE上以仅0.41M参数/任务达到87.0%平均分，超越所有MoE-LoRA变体。

**[Expert Pyramid Tuning: Efficient Parameter Fine-Tuning for Expertise-Driven Task Allocation](expert_pyramid_tuning_efficient_parameter_finetuni.md)**

:   提出 Expert Pyramid Tuning (EPT)，将 CV 中的多尺度特征金字塔思想引入 MoE-LoRA 框架，通过共享元知识子空间 + 不同尺度的反卷积专家 + 对比学习任务嵌入，以仅 0.41M 参数/任务在 GLUE 上达到 87.0% 均分（超越所有 MoE-LoRA 基线）。

**[Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](fast-thinkact_efficient_vision-language-action_reasoning_via_verbalizable_latent.md)**

:   提出 Fast-ThinkAct，通过将冗长的文本 CoT 推理（~250 token）压缩为 6 个可语言化的连续 latent token，结合 reward-guided preference distillation 和 visual trajectory alignment，实现 89.3% 推理延迟降低（9.3× faster than ThinkAct-7B）同时保持甚至超越 SOTA reasoning VLA 的性能。

**[FORCE: Transferable Visual Jailbreaking Attacks via Feature Over-Reliance CorrEction](force_transferable_visual_jailbreaking_attacks_via_feature_over-reliance_correct.md)**

:   通过分析视觉越狱攻击在层特征和频谱域的过度依赖问题，提出FORCE方法纠正非泛化性特征依赖，引导攻击探索更平坦的损失景观，从而显著提升跨模型迁移性。

**[FORCE: Transferable Visual Jailbreaking Attacks via Feature Over-Reliance CorrEction](force_transferable_visual_jailbreaking_attacks_via_feature_over_reliance_correct.md)**

:   分析发现视觉 jailbreak attack 迁移性差的根因是 attack 处于 high-sharpness loss region——源于浅层特征过度依赖 model-specific 表示和高频信息过度影响；提出 FORCE 方法通过 layer-aware regularization 扩展浅层 feasible region + spectral rescaling 抑制高频非语义成分，引导 attack 进入 flatter loss landscape，显著提升跨模型迁移性。

**[ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](forcevla2_unleashing_hybrid_force-position_control_with_force_awareness_for_cont.md)**

:   提出ForceVLA2，首个在VLA框架中统一力感知(force awareness)与混合力-位置控制(hybrid force-position control)的端到端模型：通过Force-based Prompts在VLM中构建跨阶段力感知任务概念，Cross-Scale MoE自适应融合任务语义与实时交互力实现闭环力-位置调节，在5个contact-rich任务上平均成功率66%，超π₀和π₀.5分别48.0%和35.0%。

**[GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer](geco-srt_geometry-aware_continual_adaptation_for_robotic_cross-task_sim-to-real_.md)**

:   提出一种基于几何感知的持续适应方法 GeCo-SRT，通过从局部几何特征中提取跨域/跨任务不变知识，在多次 sim-to-real 迁移中实现知识积累，从而高效适应新任务。

**[GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer](gecosrt_geometryaware_continual_adaptation_for_rob.md)**

:   GeCo-SRT提出持续跨任务Sim-to-Real迁移范式，利用局部几何特征的域不变性和任务不变性，通过几何感知MoE模块提取可复用的几何知识并用专家引导的优先经验回放防遗忘，在4个操作任务上比基线平均提升52%成功率且仅需1/6数据。

**[HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation](haltnav_reactive_visual_halting_over_lightweight_t.md)**

:   提出层级导航框架 HaltNav，结合轻量文本拓扑图 (osmAG) 全局规划 + VLN 模型局部执行，并引入反应式视觉停止 (RVH) 机制在遇到未知障碍时实时中断、更新拓扑、重规划绕行，在仿真和真实机器人上均显著优于基线。

**[HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation](haltnav_reactive_visual_halting_over_lightweight_topological_priors_for_robust_v.md)**

:   提出 HaltNav，一个层级化导航框架，结合轻量级文本拓扑先验（osmAG）做全局规划，用 VLN 模型做局部执行，并通过 Reactive Visual Halting 机制检测意外障碍、动态更新拓扑并重规划，在仿真和真机上均显著提升长程导航鲁棒性。

**[Influence Malleability in Linearized Attention: Dual Implications of Non-Convergent NTK Dynamics](influence_malleability_in_linearized_attention_dua.md)**

:   通过NTK框架证明线性化注意力不会收敛到无限宽度核极限（需要宽度m=Ω(κ⁶)），并提出"影响可塑性"指标量化其双面效应：注意力比ReLU网络高6-9倍的数据依赖灵活性，既能降低近似误差也增加对抗脆弱性。

**[Influence Malleability In Linearized Attention Dual Implications Of Non-Converge](influence_malleability_in_linearized_attention_dual_implications_of_non-converge.md)**

:   本文揭示线性化注意力机制在 NTK 框架下不收敛至无穷宽极限，并提出"影响力可塑性"(influence malleability) 度量，证明注意力的强大能力与对抗脆弱性共享同一来源——偏离核regime的数据依赖核结构。

**[Language-Grounded Decoupled Action Representation for Robotic Manipulation (LaDA)](lada_robotic_manipulation.md)**

:   提出LaDA框架，将连续7-DoF动作解耦为平移/旋转/夹爪三个语言锚定的语义原语，通过软标签对比学习和自适应权重策略在共享嵌入空间中对齐跨任务动作表示，在LIBERO上达93.6%成功率（0.6B参数），MimicGen上67%平均成功率，超越所有基线。

**[Language-Grounded Decoupled Action Representation for Robotic Manipulation](language-grounded_decoupled_action_representation_for_robotic_manipulation.md)**

:   提出 LaDA 框架，将连续 7-DoF 机器人动作解耦为语言描述的可解释运动基元（平移、旋转、夹爪），通过语义引导的软标签对比学习统一视觉-语言-动作表示空间，实现跨任务泛化。

**[Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation](learning_to_see_and_act_task-aware_virtual_view_exploration_for_robotic_manipula.md)**

:   提出 TVVE 框架，通过强化学习驱动的多视角探索策略（MVEP）选择最优虚拟相机视角并在线重渲染观测，同时设计任务感知 MoE 视觉编码器（TaskMoE）解决多任务特征干扰问题，在 RLBench 18 个任务上平均成功率达 86.6%。

**[MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent](mergevla_crossskill_model_merging_toward_a_general.md)**

:   MergeVLA 通过诊断 VLA 模型不可合并的两大根因（LoRA 参数冲突 + action expert 自注意力导致的架构不兼容），设计了稀疏激活的 task mask 和去除自注意力的 action expert 架构，实现了多个单任务 VLA 专家的免训练合并，在 LIBERO 上达到 90.2% 成功率。

**[MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents](mindpower_enabling_theory-of-mind_reasoning_in_vlm-based_embodied_agents.md)**

:   MindPower 提出以机器人为中心（Robot-Centric）的心智理论推理框架，将感知→信念→欲望→意图→决策→行动组织为三级六层推理层级（MindPower Reasoning Hierarchy），并用 Mind-Reward（基于 GRPO 强化学习）优化推理一致性，在决策和动作生成上分别超过 GPT-4o 12.77% 和 12.49%。

**[MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents](mindpower_enabling_theoryofmind_reasoning_in_vlmba.md)**

:   MindPower 提出了以机器人为中心的心智理论（ToM）推理框架，将感知→信念→欲望→意图→决策→行动组织为六层推理层级，并用 Mind-Reward（基于 GRPO）优化推理一致性，在决策和动作生成上分别超过 GPT-4o 12.77% 和 12.49%。

**[PanoAffordanceNet: Towards Holistic Affordance Grounding in 360° Indoor Environments](panoaffordancenet_towards_holistic_affordance_grou.md)**

:   提出PanoAffordanceNet，首次定义360°室内环境中的全局affordance grounding任务，通过失真感知光谱调制器(DASM)和全球面密化头(OSDH)解决ERP几何失真和稀疏激活问题，配合多级训练目标抑制语义漂移，在自建360-AGD数据集上大幅超越现有方法（KLD从2.853→1.270）。

**[RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset](radar_closedloop_robotic_data_generation_via_seman.md)**

:   提出RADAR——一个完全自主的闭环机器人操作数据生成引擎，通过VLM语义规划+GNN策略执行+VQA成功评估+FSM驱动的LIFO因果逆序环境重置四个模块，仅需2-5个人工演示即可持续生成高保真操作数据，在仿真中复杂长horizon任务达到90%成功率。

**[RC-NF: Robot-Conditioned Normalizing Flow for Real-Time Anomaly Detection in Robotic Manipulation](rcnf_robot_conditioned_normalizing_flow_anomaly.md)**

:   提出RC-NF，一种基于条件归一化流的实时异常检测模型，通过解耦处理机器人状态和物体轨迹特征，仅需正样本无监督训练即可在100ms内检测VLA模型执行中的OOD异常，在LIBERO-Anomaly-10上以约8% AUC和10% AP的优势超越SOTA（包括GPT-5、Gemini 2.5 Pro等VLM基线）。

**[RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model](rehearsevla_simulated_posttraining_world_model.md)**

:   针对 VLA 模型在数据稀缺场景下的性能退化和真实环境不可重置的限制，提出 RehearseVLA——用物理一致的世界模型模拟器替代真实物理交互进行 RL 后训练，配合 VLM 引导的即时反射器提供奖励信号和终止预测，仅用每个任务 5 个专家演示即可显著提升 VLA 在复杂操控任务上的表现。

**[Sapave Towards Active Perception And Manipulation In Vision-Language-Action Mode](sapave_towards_active_perception_and_manipulation_in_vision-language-action_mode.md)**

:   提出 SaPaVe 端到端框架，通过解耦相机运动与操控动作的两阶段自底向上学习策略，实现语义驱动的主动感知与视角不变的操控执行，在真实世界任务中超越 GR00T N1 和 π₀ 分别 31.25% 和 40%。

**[Test-Time Ego-Exo-Centric Adaptation For Action Anticipation Via Multi-Label Pro](test-time_ego-exo-centric_adaptation_for_action_anticipation_via_multi-label_pro.md)**

:   首次提出 Test-time Ego-Exo Adaptation for Action Anticipation（TE2A3）任务，设计 DCPGN 网络通过多标签原型增长和双线索（视觉+文本）一致性，在测试时将源视角训练模型在线适配到目标视角进行动作预测，大幅超越现有 TTA 方法。

**[The Coherence Trap: MLLM-Crafted Narratives Exploit Manipulated Visual Contexts](the_coherence_trap_when_mllmcrafted_narratives_exp.md)**

:   揭示现有多模态虚假信息检测的两个根本缺陷（低估MLLM生成的语义一致虚假叙事+依赖简单不对齐的伪影），构建441k样本的MDSM数据集（图像篡改+MLLM生成语义对齐文本），并提出AMD框架（Artifact Pre-perception + Manipulation-Oriented Reasoning），在跨域检测中达88.18 ACC / 60.25 mAP / 61.02 mIoU。
