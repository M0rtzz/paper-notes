<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**📷 CVPR2026** · 共 **44** 篇

**[All in One: Unifying Deepfake Detection, Tampering Localization, and Source Tracing with a Robust Landmark-Identity Watermark](all_in_one_unifying_deepfake_detection_tampering_localization_and_source_tracing.md)**

:   提出 LIDMark，首个将 deepfake 检测、篡改区域定位和源追踪统一到单一主动取证框架中的方法——通过嵌入 152 维 Landmark-Identity 水印（136D 面部关键点 + 16D 源 ID），利用内在/外在一致性实现三合一取证，PSNR/SSIM 和检测精度均超越现有方法。

**[AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video](avatar_reinforcement_learning_to_see_hear_and_reason_over_video.md)**

:   提出AVATAR框架，通过离线策略训练架构（分层回放缓冲区）和时间优势塑造(TAS)策略解决GRPO在多模态视频推理中的数据低效、优势消失和均匀信用分配三大问题，在音视频理解基准上显著超越标准GRPO（OmniBench +3.7，样本效率提升5倍）。

**[Bilevel Layer-Positioning LoRA for Real Image Dehazing](bilevel_layer-positioning_lora_for_real_image_dehazing.md)**

:   提出 BiLaLoRA，通过双层优化自动定位 LoRA 应插入的最优网络层，配合 H2C Loss（基于 CLIP 语义方向的无监督去雾损失），实现合成数据预训练的去雾模型向真实场景的高效适配——训练时间降低 77.7%，性能持平全量微调，跨模型跨域均有效。

**[Bilevel Layer-Positioning LoRA for Real Image Dehazing](bilevel_lora_real_image_dehazing.md)**

:   提出H2C文本引导无监督损失（利用CLIP将去雾重构为语义对齐问题）和BiLaLoRA双层优化策略（自动搜索最佳LoRA注入层），实现高效且即插即用的合成到真实域去雾适配。

**[BiPreManip: Learning Affordance-Based Bimanual Preparatory Manipulation through Anticipatory Collaboration](bipremanip_learning_affordance-based_bimanual_preparatory_manipulation_through_a.md)**

:   提出 BiPreManip 框架，基于视觉可供性表示实现双臂预备操作：先预想主手的目标交互区域，再引导辅助手进行预备动作（如翻转瓶子使瓶盖朝向主手），在仿真和真实环境中大幅优于基线。

**[Breaking the Tuning Barrier: Zero-Hyperparameters Yield Multi-Corner Analysis Via Learned Priors](breaking_the_tuning_barrier_zero-hyperparameters_yield_multi-corner_analysis_via.md)**

:   提出基于 Learned Priors（TabPFN 基础模型）的零超参良率多角分析框架，通过 in-context Bayesian 推断替代传统 GP/normalizing flow 的超参调优，结合自动特征选择、Cross-Corner 知识迁移和不确定性驱动主动学习，MRE 低至 0.11% 且完全免调参，验证成本降低 10× 以上。

**[Breaking the Tuning Barrier: Zero-Hyperparameters Yield Multi-Corner Analysis Via Learned Priors](breaking_the_tuning_barrier_zerohyperparameters_yi.md)**

:   用TabPFN（在百万回归任务上预训练的基础模型）替代传统手工先验，实现零超参数的SRAM多角良率分析，通过注意力机制自动进行跨角知识迁移，配合自动特征选择（1152D到48D）和不确定性引导的主动学习，达到SOTA精度（MRE低至0.11%）同时降低10倍以上验证成本。

**[Cigpose Causal Intervention Graph Neural Network For Whole-Body Pose Estimation](cigpose_causal_intervention_graph_neural_network_for_whole-body_pose_estimation.md)**

:   提出因果干预图姿态估计框架 CIGPose，通过结构因果模型识别视觉上下文混杂因素，利用预测不确定性定位受混杂影响的关键点并用学习得到的上下文无关规范嵌入替换，再经层次图神经网络建模骨骼解剖约束，在 COCO-WholeBody 上达到 67.0% AP 的新 SOTA。

**[Cog Confidence-Aware Optimal Geometric Correspondence For Unsupervised Single-Re](cog_confidence-aware_optimal_geometric_correspondence_for_unsupervised_single-re.md)**

:   提出 COG 框架，将跨视图对应关系建模为置信度感知的最优传输(OT)问题，通过预测逐点置信度作为传输边际约束来抑制非重叠区域和离群点，实现无监督条件下媲美有监督方法的单参考图像新物体6DoF位姿估计。

**[CraterBench-R: Instance-Level Crater Retrieval for Planetary Scale](craterbench-r_instance-level_crater_retrieval_for_planetary_scale.md)**

:   首次将陨石坑分析形式化为实例级图像检索问题——提出CraterBench-R基准(~25K火星陨石坑ID, 50K gallery, 5K查询)，诊断发现单向量池化有精度上限+有监督度量学习反而退化，提出无训练的实例token聚合(选K个种子+余弦最近邻残差分配)将196个ViT patch token压缩为K个代表token做late interaction匹配，K=64时匹配全token精度且存储大幅降低，实用两阶段管线(单向量粗筛+实例token精排)恢复89-94%完整精度。

**[AdvMark: Decoupling Defense Strategies for Robust Image Watermarking](decoupling_defense_strategies_for_robust_image_watermarking.md)**

:   提出 AdvMark 两阶段解耦防御框架：Stage 1 Encoder Adversarial Training（EAT）将水印图像移入 non-attackable 区域抵御对抗攻击，Stage 2 直接图像优化抵御失真+再生攻击并保留对抗鲁棒性，在 9 种水印方法 ×10 种攻击上分别提升失真/再生/对抗准确率 29%/33%/46%，且图像质量最优。

**[E-3DPSM: A State Machine for Event-Based Egocentric 3D Human Pose Estimation](e-3dpsm_a_state_machine_for_event-based_egocentric_3d_human_pose_estimation.md)**

:   提出 E-3DPSM，一种基于事件相机的自我中心 3D 人体姿态状态机，将姿态估计建模为连续时间状态演化过程，通过双向 SSM 时序建模和可学习的卡尔曼式融合模块融合直接预测与增量预测，实现 80Hz 实时推理，MPJPE 降低 19%、时序稳定性提升 2.7 倍。

**[Egoposeformer V2 Accurate Egocentric Human Motion Estimation For Arvr](egoposeformer_v2_accurate_egocentric_human_motion_estimation_for_arvr.md)**

:   提出 EgoPoseFormer v2 (EPFv2)，通过端到端 Transformer 架构（单一全局查询 + 因果时序注意力 + 条件多视图交叉注意力）和基于不确定性蒸馏的自动标注系统，在 EgoBody3M 基准上以 0.8ms GPU 延迟实现了自我中心 3D 人体运动估计的 SOTA 精度（MPJPE 4.02cm，比前作提升 15-22%）。

**[Face Time Traveller Travel Through Ages Without Losing Identity](face_time_traveller_travel_through_ages_without_losing_identity.md)**

:   提出 FaceTT 框架，通过面部属性感知提示词精炼、角度反演和自适应注意力控制三大模块，实现高保真、身份一致的人脸年龄变换，在多个基准上超越现有方法。

**[FDeID-Toolbox: Face De-Identification Toolbox](fdeidtoolbox_face_deidentification_toolbox.md)**

:   发布 FDeID-Toolbox，一个模块化人脸去识别研究工具箱，统一了数据加载、方法实现（经典到 SOTA 生成模型）、推理流水线和三维评估协议（隐私/效用/质量），解决该领域实验碎片化和结果不可比的问题。

**[FedBPrompt: Federated Domain Generalization Person Re-Identification via Body Distribution Aware Visual Prompts](fedbprompt_federated_domain_generalization_person.md)**

:   提出 FedBPrompt，将可学习视觉提示分为身体部件对齐提示（受限局部注意力处理视角错位）和全身整体提示（抑制背景干扰），并设计仅传输提示参数（~0.46M vs. 全模型~86M）的联邦微调策略，在 FedDG-ReID 上取得一致性提升。

**[FedBPrompt: Federated Domain Generalization Person Re-Identification via Body Distribution Aware Visual Prompts](fedbprompt_federated_domain_generalization_person_re-identification_via_body_dis.md)**

:   提出FedBPrompt框架，通过身体分布感知视觉提示机制(BAPM)将prompt分为Body Part Alignment Prompts和Holistic Full Body Prompts两组，配合Prompt-based Fine-Tuning Strategy(PFTS)冻结ViT backbone仅训练轻量prompt（通信量降至~1%），在FedDG-ReID任务上平均mAP提升3.3%、Rank-1提升4.9%。

**[FedDAP: Domain-Aware Prototype Learning for Federated Learning under Domain Shift](feddap_domain-aware_prototype_learning_for_federated_learning_under_domain_shift.md)**

:   提出域感知原型联邦学习框架 FedDAP，通过构建域特定全局原型和双重原型对齐策略（域内对齐 + 跨域对比），解决联邦学习中客户端数据域偏移导致的全局模型性能退化问题。

**[FlexAvatar: Learning Complete 3D Head Avatars with Partial Supervision](flexavatar_learning_complete_3d_head_avatars_with_partial_supervision.md)**

:   提出 FlexAvatar，通过引入可学习的"偏置吸收器"（bias sinks）token 统一单目和多视角数据训练，解决了驱动信号与目标视角的纠缠问题，从单张图像生成完整、高质量、可动画的 3D 头部化身。

**[Fozo Forward-Only Zeroth-Order Prompt Optimization For Test-Time Adaptation](fozo_forward-only_zeroth-order_prompt_optimization_for_test-time_adaptation.md)**

:   提出 FOZO，一种仅需前向传播的零阶 prompt 优化范式，通过 SPSA 梯度估计 + 动态扰动策略 + 深浅层特征统计对齐，在不修改模型权重的情况下实现高效 TTA，在 ImageNet-C 上以 59.52% 准确率超越所有前向方法（含 FOA 58.13%），并支持 INT8 量化模型。

**[GeoWorld: Geometric World Models](geoworld_geometric_world_models.md)**

:   在V-JEPA 2中引入双曲流形表示（Hyperbolic JEPA）和几何强化学习（GRL），利用测地线距离编码层次关系，通过能量函数优化实现更稳定的长时域规划，3步规划提升约3% SR，超越GPT-5 zero-shot。

**[Graph2Eval: Automatic Multimodal Task Generation for Agents via Knowledge Graphs](graph2eval_automatic_multimodal_task_generation_for_agents_via_knowledge_graphs.md)**

:   提出 Graph2Eval，一个知识图谱驱动的 agent 评估任务自动生成框架——通过从文档/网页构建结构化知识图谱、子图采样、LLM 条件生成和多阶段过滤，自动产出语义一致（+20%）且可解（+17%）的多模态 agent 任务，构建了包含 1319 个任务的 Graph2Eval-Bench。

**[Graph2Eval: Automatic Multimodal Task Generation for Agents via Knowledge Graphs](graph2eval_multimodal_task_generation_agents.md)**

:   提出 Graph2Eval，一个基于知识图谱的自动化多模态 Agent 任务生成框架——从异构外部数据源构建知识图谱作为结构化任务空间，通过子图采样和元路径引导的任务构造生成语义一致且可解的 Agent 评测任务，相比 LLM 直接生成的任务提升语义一致性 20% 和可解性 17%，并发布了 1,319 个任务的 Graph2Eval-Bench 数据集。

**[IDperturb: Enhancing Variation in Synthetic Face Generation via Angular Perturbations](idperturb_enhancing_variation_in_synthetic_face_generation_via_angular_perturbat.md)**

:   提出 IDperturb，一种在单位超球面上对身份嵌入进行角度扰动的几何采样策略，无需修改生成模型即可显著增强合成人脸数据集的类内多样性，提升下游人脸识别性能。

**[Lamogen Language To Motion Generation Through Llm-Guided Symbolic Inference](lamogen_language_to_motion_generation_through_llm-guided_symbolic_inference.md)**

:   提出 LabanLite 符号动作表示和 LaMoGen 框架，首次让 LLM 通过可解释的 Laban 符号推理自主组合动作序列，在时序精度和可控性上超越传统文本-动作联合嵌入方法。

**[Laser Layer-Wise Scale Alignment For Training-Free Streaming 4D Reconstruction](laser_layer-wise_scale_alignment_for_training-free_streaming_4d_reconstruction.md)**

:   提出 LASER，一个无需重训练的框架，通过层级深度尺度对齐（Layer-wise Scale Alignment）将离线前馈重建模型（如 VGGT、π³）转换为流式系统，在 RTX A6000 上以 14 FPS、6GB 峰值显存实现千米级视频的实时流式 4D 重建。

**[MatchED: Crisp Edge Detection Using End-to-End, Matching-based Supervision](matched_crisp_edge_detection_using_end-to-end_matching-based_supervision.md)**

:   MatchED 提出一种轻量（约21K参数）plug-and-play 模块，通过在训练时对预测边缘和 GT 边缘进行基于空间距离+置信度的 one-to-one 二部匹配来生成 crisp（单像素宽）边缘图，可附加到任何边缘检测器端到端训练，首次在不依赖 NMS+thinning 后处理的情况下匹配或超越标准后处理方法。

**[Miburi: Towards Expressive Interactive Gesture Synthesis](miburi_towards_expressive_interactive_gesture_synthesis.md)**

:   提出 Miburi，首个在线因果框架，通过直接利用语音-文本大模型 Moshi 的内部 token 流和二维因果 Transformer，实现实时同步的全身手势与面部表情生成。

**[Mobile-VTON: High-Fidelity On-Device Virtual Try-On](mobile-vton_high-fidelity_on-device_virtual_try-on.md)**

:   提出 Mobile-VTON，首个可完全在移动设备上离线运行的扩散模型虚拟试穿系统，通过 TeacherNet-GarmentNet-TryonNet（TGT）架构和特征引导对抗蒸馏策略，以 415M 参数和 2.84GB 显存实现媲美服务器端基线的高质量试穿效果。

**[Mobile-VTON: High-Fidelity On-Device Virtual Try-On](mobile_vton_ondevice_virtual_tryon.md)**

:   首个全离线移动端扩散式虚拟试穿框架，基于TeacherNet-GarmentNet-TryonNet (TGT)架构，通过特征引导对抗蒸馏(FGA)将SD3.5 Large的能力迁移到415M参数的轻量学生网络，在VITON-HD和DressCode上以1024×768分辨率匹配甚至超越服务器端基线，端到端推理时间约80秒（小米17 Pro Max）。

**[OpenFS: Multi-Hand-Capable Fingerspelling Recognition with Implicit Signing-Hand Detection and Frame-Wise Letter-Conditioned Synthesis](openfs_multi-hand-capable_fingerspelling_recognition_with_implicit_signing-hand_.md)**

:   提出 OpenFS 框架，通过双层位置编码 + 签名手聚焦损失 + 单调对齐损失实现隐式签名手检测的多手指拼识别，并设计帧级字母条件扩散生成器合成 OOV 数据，在 ChicagoFSWild/ChicagoFSWildPlus/FSNeo 三个基准上取得 SOTA，推理速度比 PoseNet 快 100 倍以上。

**[ParTY: Part-Guidance for Expressive Text-to-Motion Synthesis](party_part-guidance_for_expressive_text-to-motion_synthesis.md)**

:   提出 ParTY 框架，通过部位引导网络（Part-Guided Network）和部位感知文本对齐（Part-aware Text Grounding），在保持全身动作连贯性的同时大幅提升身体各部位的文本-动作语义对齐精度，解决了现有整体式方法与部位拆分方法之间"部位表达力 vs 全身连贯性"的根本矛盾。

**[RecoverMark: Robust Watermarking for Localization and Recovery of Manipulated Faces](recovermark_robust_watermarking_for_localization_and_recovery_of_manipulated_fac.md)**

:   提出 RecoverMark，一个将人脸内容本身作为水印嵌入背景的鲁棒水印框架，同时实现篡改区域定位、原始内容恢复和版权验证，在水印移除攻击下仍保持有效。

**[Rethinking Concept Bottleneck Models: From Pitfalls to Solutions](rethinking_concept_bottleneck_models_from_pitfalls_to_solutions.md)**

:   提出 CBM-Suite 框架，系统性解决概念瓶颈模型的四大缺陷——缺乏概念相关性预评估指标、线性问题导致概念瓶颈被绕过、与黑盒模型的精度差距、以及不同视觉骨干/VLM 影响的研究空白——通过熵度量、非线性层和蒸馏损失显著提升 CBM 的精度与可解释性。

**[SAVE: Speech-Aware Video Representation Learning for Video-Text Retrieval](save_speech-aware_video_representation_learning_for_video-text_retrieval.md)**

:   提出 SAVE 方法，通过添加专用语音分支（Whisper ASR + CLIP 文本编码器）和 soft-ALBEF 视觉-音频早期对齐策略，实现语音感知的视频表示学习，在五个视频-文本检索基准上全面超越 SOTA。

**[See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles](see_think_act_teaching_multimodal_agents_to_effectively_interact_with_gui_by_ide.md)**

:   提出 State-aware Reasoning (StaR)，通过教会多模态 Agent "感知当前状态→分析目标状态→决定是否操作"的三步推理链，将 GUI 开关控制准确率提升超 30%，同时不损害通用 Agent 任务性能。

**[Sketch2Colab: Sketch-Conditioned Multi-Human Animation via Controllable Flow Distillation](sketch2colab_sketch-conditioned_multi-human_animation_via_controllable_flow_dist.md)**

:   提出 Sketch2Colab，通过将草图驱动的扩散先验蒸馏为整流流学生网络，结合能量引导和连续时间马尔可夫链（CTMC）离散事件规划，从故事板草图生成协调的多人-物体交互 3D 动作，在 CORE4D 和 InterHuman 上实现 SOTA 约束遵从度和感知质量。

**[Stable Spike Dual Consistency Optimization Via Bitwise And Operations For Spikin](stable_spike_dual_consistency_optimization_via_bitwise_and_operations_for_spikin.md)**

:   提出 Stable Spike 双一致性优化框架，利用硬件友好的 AND 位运算从多时间步脉冲图中解耦稳定脉冲骨架，并注入振幅感知脉冲噪声增强泛化，在超低延迟(T=2)下将神经形态物体识别精度提升最高 8.33%。

**[Team RAS in 10th ABAW Competition: Multimodal Valence and Arousal Estimation Approach](team_ras_in_10th_abaw_competition_multimodal_valence_and_arousal_estimation_appr.md)**

:   提出一种结合人脸视觉特征、VLM行为描述嵌入和音频特征的多模态方法用于连续效价-唤醒（VA）估计，通过两种融合策略（DCMMOE 和 RAAV）在 Aff-Wild2 数据集上取得了竞争力的结果。

**[TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size](teamhoi_learning_a_unified_policy_for_cooperative_human-object_interactions_with.md)**

:   提出 TeamHOI 框架，通过基于 Transformer 的去中心化策略网络和掩码对抗运动先验（Masked AMP），使单一策略能够泛化到任意数量智能体的协作搬运任务，2-8 个仿人智能体协作搬桌子成功率达 97%+。

**[Towards Source-Aware Object Swapping with Initial Noise Perturbation](towards_source-aware_object_swapping_with_initial_noise_perturbation.md)**

:   提出 SourceSwap，通过频率分离的初始噪声扰动从单张图像生成高质量伪配对数据，并采用源感知双 U-Net 架构学习跨物体对齐，实现零样本、无逐物体微调的高保真物体替换。

**[Training High-Level Schedulers With Execution-Feedback Reinforcement Learning Fo](training_high-level_schedulers_with_execution-feedback_reinforcement_learning_fo.md)**

:   提出 CES（Coordinator-Executor-State Tracker）多智能体框架和分阶段执行反馈强化学习算法，将高层任务规划与低层执行解耦，通过专门训练的 Coordinator 和 State Tracker 显著提升 GUI Agent 在长时序任务上的规划和状态管理能力。

**[TriLite: Efficient WSOL with Universal Visual Features and Tri-Region Disentanglement](trilite_efficient_weakly_supervised_object_localization_with_universal_visual_fe.md)**

:   仅使用冻结 DINOv2 ViT + 不到 800K 可训练参数的 TriHead 模块，通过将 patch 特征解耦为前景/背景/模糊三区域并引入对抗性背景损失，在 WSOL 上以极少参数刷新 SOTA。

**[When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](when_robots_obey_the_patch_universal_transferable_patch_attacks_on_vision-langua.md)**

:   提出 UPA-RFAS 框架，学习一个单一物理对抗补丁，通过特征空间偏移、注意力劫持和语义错位三管齐下，实现对 VLA 机器人策略的通用、可迁移黑盒攻击。
