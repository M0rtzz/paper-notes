<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**🤖 AAAI2026** · 共 **29** 篇

**[A Data-Driven Model Predictive Control Framework for Multi-Aircraft TMA Routing Under Travel Time Uncertainty](a_data-driven_model_predictive_control_framework_for_multi-aircraft_tma_routing_.md)**

:   提出面向终端管制区（TMA）多机冲突解脱和着陆调度的闭环 MPC 框架——集成 XGBoost 到达时间预测、MILP 优化模型（路径选择+速度调整+等待约束）和交通仿真器，在樟宜机场 50 海里 STAR 网络上实现实时无冲突调度，高峰期计算时间比一次性优化降低 7 倍，Monte Carlo 仿真验证鲁棒性。

**[AI-based Traffic Modeling for Network Security and Privacy: Challenges Ahead](ai-based_traffic_modeling_for_network_security_and_privacy_challenges_ahead.md)**

:   一篇面向网络安全与隐私（NetS&P）任务的 AI 流量建模综述与展望，系统梳理了异常检测、攻击分类、IoT 设备识别、网站指纹攻击等任务的 AI 方案，并深入讨论了数据质量、实际部署、可解释性和基础模型四大前沿挑战。

**[Backdoor Attacks on Open Vocabulary Object Detectors via Multi-Modal Prompt Tuning](backdoor_attacks_on_open_vocabulary_object_detectors_via_multi-modal_prompt_tuni.md)**

:   首次研究开放词汇目标检测器（OVOD）的后门攻击，提出 TrAP（Trigger-Aware Prompt tuning），通过联合优化视觉和文本分支的 learnable prompt 与可学习触发器，在不修改模型权重的前提下注入高成功率后门。

**[Beta Distribution Learning for Reliable Roadway Crash Risk Assessment](beta_distribution_learning_for_reliable_roadway_crash_risk_a.md)**

:   提出基于 Beta 分布学习的地理空间深度学习框架，利用多尺度卫星图像预测道路致命事故风险的完整概率分布（而非点估计），在 Recall 上提升 17-23%，并通过分布形状自然表达不确定性。

**[Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation](bridging_day_and_night_target-class_hallucination_suppressio.md)**

:   首次系统性解决无配对日→夜图像翻译中的"目标类幻觉"问题，通过双头判别器（风格头+SAM2伪标签分割头）检测幻觉 + 类原型对比学习抑制幻觉，在BDD100K日夜域适应检测上将mAP从15.08提升到17.40（+15.5%），交通灯AP提升31.7%。

**[CaTFormer: Causal Temporal Transformer with Dynamic Contextual Fusion for Driving Intention Prediction](catformer_causal_temporal_transformer_with_dynamic_contextual_fusion_for_driving.md)**

:   提出 CaTFormer，通过因果时序 Transformer 显式建模驾驶员行为与环境上下文之间的因果交互，在 Brain4Cars 数据集上以 98.6% F1 达到 SOTA。

**[Cheating Stereo Matching in Full-Scale: Physical Adversarial Attack against Binocular Depth Estimation](cheating_stereo_matching_in_full-scale_physical_adversarial_attack_against_binoc.md)**

:   提出首个针对立体匹配模型的3D全表面纹理物理对抗攻击，通过立体对齐渲染模块和区域感知的融合攻击（merging attack），使对抗车辆在深度图中与背景无缝融合，导致自动驾驶感知系统严重失效。

**[CompTrack: 信息瓶颈引导的低秩动态Token压缩用于点云跟踪 (Oral)](comptrack_information_bottleneckguided_lowrank_dynamic_token_compres.md)**

:   针对LiDAR点云3D单目标跟踪中的"双重冗余"问题（空间冗余：大量背景噪声；信息冗余：前景中大量不具区分性的平面点），提出SFP前景预测器+IB-DTC信息瓶颈引导动态Token压缩两个模块，在KITTI/nuScenes/Waymo上达到SOTA，90 FPS实时运行（比P2P快1.4倍）。

**[Debiased Dual-Invariant Defense for Adversarially Robust Person Re-Identification](debiased_dual-invariant_defense_for_adversarially_robust_person_re-identificatio.md)**

:   系统识别出行人ReID对抗防御的两大独特挑战（模型偏差和复合泛化需求），提出去偏双不变防御框架：数据平衡阶段用扩散模型重采样缓解偏差，双对抗自元防御阶段通过最远负样本扩展软化的度量对抗训练和对抗增强的自元学习实现对未见ID和未见攻击的双重泛化。

**[AdaptiveAD: Decoupling Scene Perception and Ego Status for End-to-End Autonomous Driving](decoupling_scene_perception_and_ego_status_a_multi-context_fusion_approach_for_e.md)**

:   识别出端到端自动驾驶中ego status过度依赖的架构根源（BEV编码器中ego status的过早融合），提出AdaptiveAD双分支架构：场景驱动分支（去除ego status）和自我驱动分支独立生成决策，再通过场景感知融合模块自适应整合，配合路径注意力、BEV单向蒸馏和自回归在线建图辅助任务，在nuScenes上达到SOTA规划性能。

**[SAML: 可微语义元学习框架用于长尾运动预测](differentiable_semantic_meta-learning_framework_for_long-tail_motion_forecasting.md)**

:   提出SAML框架，首次给出运动预测中"长尾性"(tailness)的可微语义定义——通过内在属性(运动学动态性、几何复杂度、时间不规则性)和交互属性(局部/全局风险)量化稀有度，经贝叶斯尾部感知器融合为连续Tail Index驱动MAML元学习适配，在nuScenes/NGSIM/HighD上取得SOTA，尤其在worst-case top 1-5%子集上大幅领先。

**[Difficulty-Aware Label-Guided Denoising for Monocular 3D Object Detection](difficulty-aware_label-guided_denoising_for_monocular_3d_object_detection.md)**

:   提出 MonoDLGD，通过根据实例级检测难度自适应扰动并重建 ground-truth 标签，为单目 3D 检测提供显式几何监督，在 KITTI 上取得 SOTA。

**[DiffRefiner: Coarse to Fine Trajectory Planning via Diffusion Refinement with Semantic Interaction for End to End Autonomous Driving](diffrefiner_coarse_to_fine_trajectory_planning_via_diffusion_refinement_with_sem.md)**

:   提出 DiffRefiner，通过"粗到精"两阶段框架——先用判别式 Proposal Decoder 生成粗轨迹，再用扩散模型迭代精炼——结合细粒度语义交互模块，在 NAVSIM v2 和 Bench2Drive 两个基准上均达到 SOTA。

**[Drive As You Like Strategy-Level Motion Planning Based On A Multi-Head Diffusion](drive_as_you_like_strategy-level_motion_planning_based_on_a_multi-head_diffusion.md)**

:   提出 M-Diffusion Planner，基于多头扩散模型和 GRPO 后训练，实现策略级（strategy-level）运动规划，允许用户通过自然语言切换激进/保守/舒适等驾驶风格，同时保持 SOTA 规划性能。

**[DriveFlow: Rectified Flow Adaptation for Robust 3D Object Detection in Autonomous Driving](driveflow_rectified_flow_adaptation_for_robust_3d_object_detection_in_autonomous.md)**

:   提出 DriveFlow，一种基于预训练 T2I Flow 模型的 rectified flow 适配方法，通过频率分解对前景高频保持和背景双频优化，实现无需训练的驾驶场景图像编辑数据增强，大幅提升视觉 3D 检测器在 OOD 场景下的鲁棒性。

**[DriveSuprim: Towards Precise Trajectory Selection for End-to-End Planning](drivesuprim_towards_precise_trajectory_selection_for_end-to-end_planning.md)**

:   提出 DriveSuprim，通过粗到精的轨迹筛选范式、旋转数据增强和自蒸馏软标签框架，解决选择式端到端规划中难以区分相似轨迹、方向偏差和硬标签不稳定的问题，在 NAVSIM v1/v2 和 Bench2Drive 上达到 SOTA。

**[Dual-branch Spatial-Temporal Self-supervised Representation for Enhanced Road Network Learning](dual-branch_spatial-temporal_self-supervised_representation_for_enhanced_road_ne.md)**

:   提出 DST（Dual-branch Spatial-Temporal）路网表示学习框架，通过空间分支（mix-hop 转移矩阵 + 图-超图对比学习）和时间分支（Transformer 编码器 + 下一 token 预测 + 工作日/周末分类）两条支路联合建模路网的空间异质性和时间动态性，在三个城市的三项下游任务上取得 SOTA。

**[ExpertAD: Enhancing Autonomous Driving Systems with Mixture of Experts](expertad_enhancing_autonomous_driving_systems_with_mixture_of_experts.md)**

:   提出 ExpertAD，将混合专家（MoE）架构引入端到端自动驾驶系统的感知和预测模块——Perception Adapter 动态重加权 BEV 特征以放大任务关键语义，Mixture of Sparse Experts 通过路由器动态激活相关驾驶任务专家并用稀疏注意力降低计算量，在保持或提升规划效果的同时降低约 25% 推理延迟。

**[FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning](fastdrivevla_efficient_end-to-end_driving_via_plug-and-play_.md)**

:   提出 FastDriveVLA，通过 MAE 风格的前景像素重建训练轻量级 plug-and-play 的 ReconPruner 模块（仅 0.07B），利用对抗前景-背景重建策略优先保留驾驶决策所需的前景 token，在 nuScenes 开环规划基准上各剪枝率均达 SOTA，一次训练可迁移至同一视觉编码器的不同 VLA 模型。

**[FQ-PETR: Fully Quantized Position Embedding Transformation for Multi-View 3D Object Detection](fq-petr_fully_quantized_position_embedding_transformation_fo.md)**

:   首次实现PETR系列3D检测器的全INT8量化部署，通过量化友好的LiDAR-ray位置编码(QFPE)解决多模态特征幅度不匹配问题、双查找表(DULUT)高效逼近非线性算子、数值稳定后量化(QANS)避免softmax注意力失真，在PETR/StreamPETR/PETRv2/MV2D上W8A8精度损失<1%且延迟降低75%（3.9×加速）。

**[Generalising Traffic Forecasting To Regions Without Traffic Observations](generalising_traffic_forecasting_to_regions_without_traffic_observations.md)**

:   本文提出 GenCast 模型，通过物理信息神经网络（引入 LWR 交通方程作为软约束）、动态外部天气信号融合和空间分组模块三大创新，实现了从有传感器区域到无传感器连续区域的交通预测泛化，在五个真实数据集上一致性地超越了现有最优方法。

**[LiDARCrafter: Dynamic 4D World Modeling from LiDAR Sequences](lidarcrafter_dynamic_4d_world_modeling_from_lidar_sequences.md)**

:   提出LiDARCrafter，首个专用于LiDAR的4D生成世界模型，通过Text2Layout（LLM解析文本→场景图→三分支扩散生成4D布局）→Layout2Scene（Range-image扩散生成高保真单帧）→Scene2Seq（自回归warp+扩散生成时序一致的序列）三阶段流程，在nuScenes上取得SOTA。

**[MambaSeg: Harnessing Mamba for Accurate and Efficient Image-Event Semantic Segmentation](mambaseg_harnessing_mamba_for_accurate_and_efficient_image-e.md)**

:   提出 MambaSeg，用双分支并行 Mamba 编码器分别处理 RGB 图像和事件流，通过空间-时间双维度交互模块 (DDIM) 实现细粒度跨模态融合，在 DDD17 和 DSEC 数据集上以 25.44M 参数取得 77.56%/75.10% mIoU 的 SOTA，效率远优于 Transformer 方案。

**[SPARC: 用单一策略驾驶100辆未见车辆的OOD泛化](out-of-distribution_generalization_with_a_sparc_racing_100_u.md)**

:   提出 SPARC（Single-Phase Adaptation for Robust Control），将 RMA 的两阶段上下文编码与历史适应统一为单阶段训练，在 Gran Turismo 7 高保真赛车模拟器中用单一策略驾驶100+未见车辆实现SOTA OOD泛化性能。

**[PriorDrive: 用统一向量先验增强在线HD地图构建](priordrive_enhancing_online_hd_mapping_with_unified_vector_p.md)**

:   提出 PriorDrive 框架，通过 Unified Vector Encoder (UVE) 和 Hybrid Prior Representation (HPQuery) 将多种向量化先验地图（SD地图、旧HD地图、历史预测地图）统一编码并集成到各种在线建图模型中，在 nuScenes 上 mAP 提升 14.3，兼容 query-based 和 non-query-based 两类建图架构。

**[ReflexDiffusion: 反思增强的高侧向加速度自动驾驶轨迹规划](reflexdiffusion_reflection-enhanced_trajectory_planning_for_.md)**

:   提出 ReflexDiffusion，在扩散模型推理阶段引入物理感知的反思机制，通过梯度注入强化曲率-速度-加速度耦合约束（a_y = κv²），在 nuPlan 高侧向加速度长尾场景中驾驶分数提升 14.1%，架构无关可直接部署到现有扩散规划器。

**[Task Prototype-Based Knowledge Retrieval for Multi-Task Learning from Partially Annotated Data](task_prototype-based_knowledge_retrieval_for_multi-task_lear.md)**

:   提出基于任务原型的知识检索框架，通过可学习 Task Prototype 嵌入任务特性并量化任务关联、Knowledge Retrieval Transformer 基于 task-affinity score 自适应精炼特征表示，在部分标注多任务学习（MTPSL）中避免依赖未标注任务的预测，PASCAL-Context 和 NYUD-v2 上全面超越 SOTA。

**[VILTA: A VLM-in-the-Loop Adversary for Enhancing Driving Policy Robustness](vilta_a_vlm-in-the-loop_adversary_for_enhancing_driving_poli.md)**

:   VILTA 将 VLM（Gemini-2.5-Flash）直接嵌入自动驾驶 RL 训练循环中，通过"Vision-Language-Editing"（VLE）范式让 VLM 编辑周围车辆的未来轨迹来生成具有挑战性的危险场景，训练出的驾驶策略在 CARLA 挑战场景中路线完成率提升 13.3%、碰撞率降低 28.5%。

**[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy Prediction (Oral)](visiononly_gaussian_splatting_for_collaborative_semantic_occupancy_p.md)**

:   首次将 3D 高斯 Splatting 作为多智能体协同感知的通信媒介和中间表征，利用高斯基元的刚体变换可解析性和稀疏性，通过高斯打包（ROI 裁剪+刚体变换）和跨智能体邻域融合模块，实现了高效且可解释的视觉协同语义占用预测。
