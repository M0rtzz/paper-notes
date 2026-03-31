<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤖 机器人/具身智能

**🔬 ICLR2026** · 共 **26** 篇

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

**[Grounding Generative Planners In Verifiable Logic A Hybrid Architecture For Trus](grounding_generative_planners_in_verifiable_logic_a_hybrid_architecture_for_trus.md)**

:   提出 VIRF（Verifiable Iterative Refinement Framework），通过神经-符号混合架构将确定性的逻辑导师（Logic Tutor）与 LLM 规划器结合，以可验证的形式化本体作为安全锚点，在 SafeAgentBench 上实现 0% 危险动作率（HAR）和 77.3% 任务完成率（GCR），证明严格安全保障无需牺牲智能体效用。

**[Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots](ignore_all_previous_instructions_jailbreaking_as_a_de-escalatory_peace_building_.md)**

:   提出将"越狱"（jailbreaking）LLM 驱动的社交媒体机器人视为一种用户主导的、非暴力的去冲突化（de-escalation）和和平建设实践，通过暴露自动化账号的虚假性来抵抗误导信息传播。

**[JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation](janusvln_decoupling_semantics_and_spatiality_with_dual_implicit_memory_for_visio.md)**

:   受人类左脑语义理解、右脑空间认知的启发，提出 JanusVLN——首个为 VLN 设计的双隐式神经记忆框架，将空间几何记忆和视觉语义记忆分别建模为固定大小的 KV Cache，仅凭 RGB 视频即可实现高效空间推理，在 VLN-CE 基准上取得 SOTA。

**[JULI: Jailbreak Large Language Models by Self-Introspection](juli_jailbreak_large_language_models_by_self-introspection.md)**

:   揭示对齐 LLM 的 top-k token log probability 中仍包含有害信息，提出 JULI——仅用不到目标模型 1% 参数的 BiasNet 插件操纵 logit bias，在仅访问 top-5 token 概率的 API 场景下成功越狱 Gemini-2.5-Pro（harmfulness 4.19/5），比 SOTA 快 140 倍。

**[Lets Think In Two Steps Mitigating Agreement Bias In Mllms With Self-Grounded Ve](lets_think_in_two_steps_mitigating_agreement_bias_in_mllms_with_self-grounded_ve.md)**

:   本文发现多模态大语言模型（MLLM）作为 agent 行为验证器时存在严重的"同意偏差"（agreement bias）——系统性地过度认可 agent 行为，并提出 Self-Grounded Verification（SGV）方法，通过两步生成（先提取行为先验、再条件化验证）缓解该偏差，在 web 导航、桌面操作和机器人操控任务中将失败检测率提升最高 25pp、准确率提升 14pp。

**[PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra](persona_dynamic_and_compositional_inference-time_personality_control_via_activat.md)**

:   提出 PERSONA 框架，通过在激活空间中提取近似正交的人格向量并进行向量代数运算（缩放、加法、减法），实现免训练的动态组合式人格控制，在 PersonalityBench 上达到 9.60 分，几乎匹配 SFT 上界 9.61。

**[RF-MatID: Dataset and Benchmark for Radio Frequency Material Identification](rf-matid_dataset_and_benchmark_for_radio_frequency_material_identification.md)**

:   构建了首个开源的大规模、宽频段（4-43.5 GHz）、几何扰动多样的 RF 材料识别数据集 RF-MatID，包含 16 种细粒度材料类别（5 大类）/142K 样本，并建立了覆盖 9 个深度学习模型、5 种频率协议、7 种数据划分的系统基准。

**[RoboPARA: Dual-Arm Robot Planning with Parallel Allocation and Recomposition Across Tasks](robopara_dual-arm_robot_planning_with_parallel_allocation_and_recomposition_acro.md)**

:   提出 RoboPARA，一个 LLM 驱动的双臂机器人并行任务规划框架，通过依赖图生成与图重遍历调度两阶段方法，最大化双臂协同并行性，执行时间减少 30%-50%。

**[Sparse Imagination for Efficient Visual World Model Planning](sparse_imagination_for_efficient_visual_world_model_planning.md)**

:   提出 Sparse Imagination，在基于 ViT patch token 的世界模型规划中随机丢弃 token 以大幅加速推理（50% 丢弃率减少约 50% 时间），同时通过随机分组注意力训练保持任务性能不变。

**[String Seed Of Thought Prompting Llms For Distribution-Faithful And Diverse Gene](string_seed_of_thought_prompting_llms_for_distribution-faithful_and_diverse_gene.md)**

:   本文提出 String Seed of Thought（SSoT），一种简洁的提示方法，通过指示 LLM 先生成随机字符串再从中提取随机性来选择答案，显著提升了概率指令跟随（PIF）的分布忠实度和开放式任务（DAG）的响应多样性，理论证明了 TV 距离随字符串长度指数衰减，实验表明推理型 LLM 的表现接近伪随机数生成器。

**[THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning](thor_tool-integrated_hierarchical_optimization_via_rl_for_mathematical_reasoning.md)**

:   提出 THOR，通过 TIRGen 数据构建管线 + 层次化强化学习（episode 级+step 级优化）+ 自修正推理机制，系统性解决 LLM 工具集成数学推理中的数据构建、细粒度优化和推理增强三大挑战。

**[Tracing and Reversing Edits in LLMs](tracing_and_reversing_edits_in_llms.md)**

:   针对知识编辑（Knowledge Editing）的双重使用风险，提出 EditScope 方法从编辑后的权重中推断被编辑的目标实体（准确率高达 99%），以及基于 SVD bottom-rank 近似的无训练编辑逆转方法（逆转率高达 94%），仅依赖编辑后的权重、不需要编辑 prompt 或原始权重信息。
