<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 机器人/具身智能

**🔬 ICLR2026** · 共 **46** 篇

**[All-day Multi-scenes Lifelong Vision-and-Language Navigation with Tucker Adaptation](all-day_multi-scenes_lifelong_vision-and-language_navigation_with_tucker_adaptat.md)**

:   提出Tucker Adaptation (TuKA)，将多场景多环境的多层级导航知识表示为高阶张量，用Tucker分解解耦为共享子空间（核心张量+编解码器）和场景/环境专家向量，配合解耦知识增量学习策略实现全天候多场景终身VLN，在24个导航场景上的SR和遗忘率均优于LoRA变体。

**[Attribution-Guided Decoding](attribution-guided_decoding.md)**

:   提出 Attribution-Guided Decoding (AGD)，在解码时利用归因方法（LRP）对候选 token 计算其对"感兴趣区域"(ROI) 的依赖分数，选择归因最高的 token，从而在不修改模型内部激活的前提下提升指令遵循和事实准确性。

**[Building Spatial World Models from Sparse Transitional Episodic Memories](building_spatial_world_models_from_sparse_transitional_episodic_memories.md)**

:   提出 Episodic Spatial World Model (ESWM)，从稀疏、不连续的情景记忆（one-step transitions）中构建空间世界模型，其潜空间自发涌现出与环境拓扑对齐的认知地图，并支持零样本探索和导航。

**[Capability-Based Scaling Trends for LLM-Based Red-Teaming](capability-based_scaling_trends_for_llm-based_red-teaming.md)**

:   在 600+ 对攻击者-目标 LLM 组合上系统评估了 4 种越狱方法，发现攻击成功率（ASR）与攻击者-目标的能力差距遵循 sigmoid 缩放定律（R^2=0.83），能力差距可用 MMLU-Pro 的 logit 变换量化。

**[CLIP Behaves like a Bag-of-Words Model Cross-modally but not Uni-modally](clip_behaves_like_a_bag-of-words_model_cross-modally_but_not_uni-modally.md)**

:   通过线性探测实验证明 CLIP 的 BoW（词袋）行为并非源于编码器缺乏绑定信息，而是跨模态对齐的失败；提出 LABCLIP，仅训练一个轻量线性变换即可显著恢复属性-对象绑定能力。

**[Constructive Distortion: Improving MLLMs with Attention-Guided Image Warping](constructive_distortion_improving_mllms_with_attention-guided_image_warping.md)**

:   提出 AttWarp，一种即插即用的测试时图像变形方法，利用 MLLM 自身的跨模态注意力图进行矩形网格重采样，

**[D2E: Scaling Vision-Action Pretraining on Desktop Data for Transfer to Embodied AI](d2e_scaling_vision-action_pretraining_on_desktop_data_for_transfer_to_embodied_a.md)**

:   提出 D2E 框架，证明桌面游戏交互数据可作为具身 AI 的有效预训练基底：通过 OWA 工具包收集 335h 人类演示 + Generalist-IDM 伪标注 1000+h YouTube 游戏视频 + VAPT 迁移训练，1B 参数模型在 LIBERO 操作达 96.6%、CANVAS 导航达 83.3%，匹敌或超越 7x 更大的模型。

**[Domain Expansion: A Latent Space Construction Framework for Multi-Task Learning](domain_expansion_a_latent_space_construction_framework_for_multi-task_learning.md)**

:   提出 Domain Expansion 框架，通过正交池化(Orthogonal Pooling)将潜在空间重构为互相正交的子空间，从结构上防止多目标训练中的梯度冲突与表征崩塌，实现可解释、可组合的概念代数。

**[Doubly-Robust LLM-as-a-Judge: Externally Valid Estimation with Imperfect Personas](doubly-robust_llm-as-a-judge_externally_valid_estimation_with_imperfect_personas.md)**

:   提出一种 doubly-robust 估计框架，将不完美的 LLM persona 评分与存在采样偏差的人工评分相结合，在协变量偏移和选择偏差同时存在时仍能产生统计有效的 GenAI 系统质量估计。

**[Enhancing Instruction Following of LLMs via Activation Steering with Dynamic Rejection](enhancing_instruction_following_of_llms_via_activation_steering_with_dynamic_rej.md)**

:   提出 Directer（Dynamic Rejection Steering），通过在每个解码步动态调节 KV 缓存引导强度并引入合理性约束，显著提升 LLM 指令遵循能力，同时避免过度引导导致的文本质量下降。

**[Evaluating VLMs' Spatial Reasoning Over Robot Motion: A Step Towards Robot Planning with Motion Preferences](evaluating_vlms_spatial_reasoning_over_robot_motion_a_step_towards_robot_plannin.md)**

:   系统评估了 VLM 对机器人运动路径的空间推理能力，提出 4 种图像查询方法用于让 VLM 根据用户自然语言描述选择最佳运动路径，发现 Qwen2.5-VL 零样本准确率达 71.4%，且微调后小模型可获显著提升。

**[ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning](exopredicator_learning_abstract_models_of_dynamic_worlds_for_robot_planning.md)**

:   提出 ExoPredicator 框架，联合学习符号化状态抽象和因果过程（含内生动作与外生机制），通过变分贝叶斯推断 + LLM 提议从少量轨迹中学习带随机延迟的因果世界模型，在 5 个桌面机器人环境中实现快速泛化规划。

**[Experience-based Knowledge Correction for Robust Planning in Minecraft](experience-based_knowledge_correction_for_robust_planning_in_minecraft.md)**

:   证明 LLM 无法通过 prompting 自我纠正其错误的规划先验知识（物品依赖关系），提出 XENON——通过算法化的知识管理（自适应依赖图 ADG + 失败感知动作记忆 FAM）从二值反馈中学习，使 7B LLM 在 Minecraft 长期规划中超越使用 GPT-4V + oracle 知识的 SOTA。

**[From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](from_spatial_to_actions_grounding_vision-language-action_model_in_spatial_founda.md)**

:   提出 FALCON（From Spatial to Action），通过将空间基础模型的丰富 3D 空间 token 注入到 Action Head 而非 VLM 主干中，实现了 VLA 模型的强 3D 空间感知，同时保持仅 RGB 到 RGB-D 的灵活模态切换，在仿真和真实世界任务中均达到 SOTA。

**[Grounding Generative Planners in Verifiable Logic: A Hybrid Architecture for Trustworthy Embodied AI](grounding_generative_planners_in_verifiable_logic_a_hybrid_architecture_for_trus.md)**

:   提出 VIRF（Verifiable Iterative Refinement Framework），通过神经-符号混合架构将确定性的逻辑导师（Logic Tutor）与 LLM 规划器结合，以可验证的形式化本体作为安全锚点，在 SafeAgentBench 上实现 0% 危险动作率（HAR）和 77.3% 任务完成率（GCR），证明严格安全保障无需牺牲智能体效用。

**[Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots](ignore_all_previous_instructions_jailbreaking_as_a_de-escalatory_peace_building_.md)**

:   提出将对 LLM 驱动的社交媒体宣传机器人进行"越狱"（jailbreaking）重新定义为一种用户主导的、非暴力的去冲突化（de-escalation）和平建设实践，通过 prompt injection 暴露自动化账号的虚假身份来抵抗国家支持的误导信息传播。

**[JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation](janusvln_decoupling_semantics_and_spatiality_with_dual_implicit_memory_for_visio.md)**

:   受人类左脑语义理解、右脑空间认知的启发，提出 JanusVLN——首个为 VLN 设计的双隐式神经记忆框架，将空间几何记忆和视觉语义记忆分别建模为固定大小的 KV Cache，仅凭 RGB 视频即可实现高效空间推理，在 VLN-CE 基准上取得 SOTA。

**[JULI: Jailbreak Large Language Models by Self-Introspection](juli_jailbreak_large_language_models_by_self-introspection.md)**

:   揭示对齐 LLM 的 top-k token log probability 中仍包含有害信息的知识泄露问题，提出 JULI——仅用不到目标模型 1% 参数量的 BiasNet 插件操纵 logit bias，在仅访问 top-5 token 概率的 API 场景下成功越狱 Gemini-2.5-Pro（Harmful Info Score 4.19/5），比 LINT 快 140 倍同时 harmfulness 提升约 2 倍。

**[Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification](lets_think_in_two_steps_mitigating_agreement_bias_in_mllms_with_self-grounded_ve.md)**

:   本文发现多模态大语言模型（MLLM）作为 agent 行为验证器时存在严重的"同意偏差"（agreement bias）——系统性地过度认可 agent 行为，并提出 Self-Grounded Verification（SGV）方法，通过两步生成（先提取行为先验、再条件化验证）缓解该偏差，在 web 导航、桌面操作和机器人操控任务中将失败检测率提升最高 25pp、准确率提升 14pp。

**[MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation](memoryvla_perceptual-cognitive_memory_in_vision-language-action_models_for_robot.md)**

:   受认知科学双重记忆系统启发，提出MemoryVLA框架，在VLA模型中引入感知-认知记忆库（PCMB），通过记忆检索、门控融合和整合机制捕捉长时序依赖，在SimplerEnv/LIBERO/真实世界150+任务上全面超越CogACT和π₀。

**[ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](odesteer_a_unified_ode-based_steering_framework_for_llm_alignment.md)**

:   提出基于常微分方程(ODE)的统一激活操纵理论框架，揭示传统激活加法是ODE的一阶Euler近似，将操纵方向识别与控制论障碍函数统一，据此设计ODESteer进行多步自适应操纵，在TruthfulQA/UltraFeedback/RealToxicityPrompts上分别提升5.7%/2.5%/2.4%。

**[On Entropy Control in LLM-RL Algorithms](on_entropy_control_in_llm-rl_algorithms.md)**

:   从理论解释为什么传统熵正则化在LLM-RL中几乎无效（因极大动作空间+稀疏最优导致熵偏差压倒优化增益），提出AEnt方法用截断熵（在缩小的token空间上计算）+自适应系数来有效平衡偏差与收益，在数学推理上持续超越baseline。

**[On the Generalization Capacities of MLLMs for Spatial Intelligence](on_the_generalization_capacities_of_mllms_for_spatial_intelligence.md)**

:   揭示RGB-only空间MLLM忽略相机内参导致的根本性几何歧义——近小物体和远大物体成像相同→模型过拟合训练相机分布而非学习真正的3D原理,提出Camera-Aware MLLM框架通过密集相机嵌入+相机感知数据增强+几何先验蒸馏三项技术实现跨相机泛化,证明相机感知是空间智能的先决条件。

**[One Demo Is All It Takes: Planning Domain Derivation with LLMs from A Single Demonstration](one_demo_is_all_it_takes_planning_domain_derivation_with_llms_from_a_single_demo.md)**

:   提出 PDDLLM 框架，仅需**一个演示轨迹**即可自动推导完整的 PDDL 规划域（谓词+动作），通过 LLM 推理与物理仿真的交叉验证生成可解释的符号表示，并借助逻辑约束适配器 (LoCA) 自动对接运动规划器，在 9 个环境 1200+ 任务中成功率领先 6 个 LLM 基线至少 20%，且成功部署于 3 个物理机器人平台。

**[PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra](persona_dynamic_and_compositional_inference-time_personality_control_via_activat.md)**

:   提出 PERSONA 框架，通过在激活空间中提取近似正交的人格向量并进行向量代数运算（缩放、加法、减法），实现免训练的动态组合式人格控制，在 PersonalityBench 上达到 9.60 分，几乎匹配 SFT 上界 9.61。

**[Real-Time Robot Execution with Masked Action Chunking](real-time_robot_execution_with_masked_action_chunking.md)**

:   提出REMAC，通过掩码动作分块训练策略和前缀保持采样管线，系统性解决异步推理下的段内不一致（intra-chunk inconsistency）和段间不连续（inter-chunk discontinuity）两大问题，在不引入额外推理延迟的前提下实现更可靠的实时机器人控制。

**[REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?](rei-bench_can_embodied_agents_understand_vague_human_instructions_in_task_planni.md)**

:   首次系统研究人类模糊指令中的指称表达(Referring Expressions)对LLM机器人任务规划的影响——构建REI-Bench基准建模9级共指模糊度(3级RE难度×3级上下文)，发现隐式RE可使现有规划器成功率下降高达36.9%，提出Task-Oriented Context Cognition (TOCC)方法将任务理解与规划决策解耦，平均提升成功率6.5%。

**[RF-MatID: Dataset and Benchmark for Radio Frequency Material Identification](rf-matid_dataset_and_benchmark_for_radio_frequency_material_identification.md)**

:   构建了首个开源的大规模、宽频段（4-43.5 GHz）、几何扰动多样的 RF 材料识别数据集 RF-MatID，包含 16 种细粒度材料类别（5 大类）/142K 样本，并建立了覆盖 9 个深度学习模型、5 种频率协议、7 种数据划分的系统基准。

**[RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](robocasa365_a_large-scale_simulation_framework_for_training_and_benchmarking_gen.md)**

:   RoboCasa365 构建了一个包含 365 个日常厨房任务、2500 个多样化厨房场景和超过 2000 小时机器人交互数据的大规模仿真基准，系统评估了多任务学习、基础模型训练和终身学习三大范式下通用机器人策略的性能表现，发现预训练数据的任务多样性是提升下游泛化能力的关键因素。

**[RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation](robointer_a_holistic_intermediate_representation_suite_towards_robotic_manipulat.md)**

:   提出RoboInter操作套件——统一的中间表示数据/基准/模型资源：RoboInter-Tool(半自动标注GUI)+RoboInter-Data(23万episode×571场景×10+类中间表示的密集逐帧标注)+RoboInter-VQA(29类具身VQA基准)+RoboInter-VLA(支持模块化和端到端的plan-then-execute框架)，为通过中间表示提升VLA泛化提供完整基础设施。

**[RoboPARA: Dual-Arm Robot Planning with Parallel Allocation and Recomposition Across Tasks](robopara_dual-arm_robot_planning_with_parallel_allocation_and_recomposition_acro.md)**

:   提出 RoboPARA，一个 LLM 驱动的双臂机器人并行任务规划框架，通过依赖图生成与图重遍历调度两阶段方法，最大化双臂协同并行性，执行时间减少 30%-50%。

**[Sparse Imagination for Efficient Visual World Model Planning](sparse_imagination_for_efficient_visual_world_model_planning.md)**

:   提出 Sparse Imagination，在基于 ViT patch token 的世界模型规划中通过随机丢弃 token 和随机分组注意力训练实现大幅推理加速（50% 丢弃率可减少约 50% 规划时间），同时保持甚至在某些任务上超越全量 token 的规划性能。关键发现是简单随机丢弃优于复杂的 token 选择方法，原因是静态重要性排序在动态规划场景中存在"盲点问题"。

**[String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation](string_seed_of_thought_prompting_llms_for_distribution-faithful_and_diverse_gene.md)**

:   本文提出 String Seed of Thought（SSoT），一种简洁的提示方法，通过指示 LLM 先生成随机字符串再从中提取随机性来选择答案，显著提升了概率指令跟随（PIF）的分布忠实度和开放式任务（DAG）的响应多样性，理论证明了 TV 距离随字符串长度指数衰减，实验表明推理型 LLM 的表现接近伪随机数生成器。

**[SynthWorlds: Controlled Parallel Worlds for Disentangling Reasoning and Knowledge in Language Models](synthworlds_controlled_parallel_worlds_for_disentangling_reasoning_and_knowledge.md)**

:   提出SynthWorlds——通过构建结构相同但实体不同的平行语料(真实映射vs合成映射)来解耦LLM推理能力和参数知识：真实映射语料中模型可利用记忆的事实知识,合成映射语料中参数知识无用→两者的性能差即"知识优势差距(KA)"→在多跳QA和页面导航任务上发现即使有RAG/CoT知识增强KA仍持续存在。

**[Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts](sysformer_safeguarding_frozen_large_language_models_with_adaptive_system_prompts.md)**

:   提出Sysformer——轻量级Transformer模块附着在冻结LLM输入端,根据用户提示自适应修改系统提示嵌入：保持LLM参数不变→Sysformer学习在嵌入空间中将固定系统提示转化为更鲁棒的版本,在5个LLM×2个基准上有害提示拒绝率提升80%+安全提示合规率提升90%,对越狱攻击鲁棒性提升100%。

**[Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments](test-time_mixture_of_world_models_for_embodied_agents_in_dynamic_environments.md)**

:   提出TMoW(Test-time Mixture of World Models)——将MoE范式扩展到具身agent的世界模型：不像传统MoE训练后路由固定,TMoW在测试时更新路由函数以适应未见域,通过(1)多粒度原型路由(物体→场景级相似度),(2)测试时原型精化(加权插值已有原型),(3)蒸馏混合增广(少样本构建新世界模型),在VirtualHome/ALFWorld/RLBench上零样本+27%/少样本+26%。

**[Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?](theory_of_space_can_foundation_models_construct_spatial_beliefs_through_active_e.md)**

:   提出Theory of Space框架——评估基础模型通过主动探索构建空间信念的能力：在文本和视觉环境中进行好奇心驱动探索→通过空间信念探测(让模型输出认知地图)直接测量内部空间模型质量→发现关键瓶颈：(1)主动-被动差距(GPT-5.2: 57→46)，(2)低效探索(冗余步骤多)，(3)信念惰性(无法覆写过时先验→尤其视觉模型严重)。

**[THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning](thor_tool-integrated_hierarchical_optimization_via_rl_for_mathematical_reasoning.md)**

:   提出 THOR（Tool-Integrated Hierarchical Optimization via RL），通过三个互补组件系统性解决 LLM 工具集成数学推理中的核心挑战：TIRGen 数据构建管线生成策略对齐的 TIR 训练数据、层次化强化学习（episode 级解题+step 级代码修正）缓解稀疏奖励、自修正推理机制利用工具反馈在线纠错。在 MATH500、AIME 等多个数学基准上达到同规模 SOTA，同时在代码生成基准上也有提升。

**[Token Taxes: Mitigating AGI's Economic Risks](token_taxes_mitigating_agis_economic_risks.md)**

:   提出Token Tax（基于模型推理token使用量的税收）作为缓解后AGI时代经济风险的一线治理工具，具有可通过现有计算治理基础设施执行和在使用地而非托管地征收两大优势。

**[Tracing and Reversing Edits in LLMs](tracing_and_reversing_edits_in_llms.md)**

:   针对知识编辑（Knowledge Editing）的双重使用风险，提出 EditScope 方法从编辑后的权重中推断被编辑的目标实体（准确率高达 99%），以及基于 SVD bottom-rank 近似的无训练编辑逆转方法（逆转率高达 94%），仅依赖编辑后的权重、不需要编辑 prompt 或原始权重信息。

**[TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models](twinvla_data-efficient_bimanual_manipulation_with_twin_single-arm_vision-languag.md)**

:   提出TwinVLA——将两个预训练单臂VLA通过联合注意力组合为双臂VLA的模块化框架：不需要双臂预训练数据→仅用公开单臂数据预训练SingleVLA→复制为twin→联合注意力+MoE协调→少量双臂数据微调即可→数据效率(800h单臂+50 episode双臂)和计算效率(25 GPU-day)远优于RDT-1B和π0。

**[UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos](urbanverse_scaling_urban_simulation_by_watching_city-tour_videos.md)**

:   UrbanVerse是一个数据驱动的real-to-sim系统，将众包城市旅拍视频转化为物理感知的交互式仿真场景，包含10万+标注3D资产和自动场景构建流水线，在IsaacSim中生成160个高质量场景，训练的PPO导航策略在真实世界零样本转移中成功率达89.7%，完成337m长距离任务仅需2次人工干预。

**[Visual Planning: Let's Think Only with Images](visual_planning_lets_think_only_with_images.md)**

:   提出Visual Planning——首个纯视觉推理范式：规划过程完全由图像序列表达（无文本中介），用Large Vision Model自回归生成逐步状态图像；引入VPRL两阶段RL框架（随机轨迹初始化探索+GRPO进度奖励优化），在FrozenLake/Maze/MiniBehavior三个导航任务上平均EM超越文本推理方法27%，证明"vision-first"任务中图像推理远优于文本推理。

**[What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering](whats_the_plan_metrics_for_implicit_planning_in_llms_and_their_application_to_rh.md)**

:   提出简单的定量方法评估LLM的隐式规划行为——在韵律诗(计划押韵词)和问答(计划答案)两个案例上,通过激活引导干预证明:目标token(押韵/答案)的表示在序列早期位置已形成(前向规划),且影响中间token的生成(后向规划)→在23个1B-32B模型上验证→隐式规划从1B模型即开始出现→是普遍机制。

**[When Agents Persuade: Propaganda Generation and Mitigation in LLMs](when_agents_persuade_propaganda_generation_and_mitigation_in_llms.md)**

:   系统研究LLM能否生成宣传内容→训练宣传检测器(F1=0.98)+修辞技术检测器(6种技术,平均F1=0.82)→发现LLM被prompting时会广泛使用宣传修辞(name-calling/loaded language/appeal to fear等)→SFT/DPO/ORPO三种微调方法可显著减少宣传生成→ORPO最有效。

**[When would Vision-Proprioception Policies Fail in Robotic Manipulation?](when_would_vision-proprioception_policies_fail_in_robotic_manipulation.md)**

:   揭示视觉-本体感觉操作策略在运动转换阶段（motion-transition phases）会失效的原因——本体感觉信号在优化中占主导导致视觉学习被抑制，并提出Gradient Adjustment with Phase-guidance (GAP)算法，通过自适应调低本体感觉梯度来恢复视觉模态的学习，在仿真和真实环境中均显著提升策略的泛化性。
