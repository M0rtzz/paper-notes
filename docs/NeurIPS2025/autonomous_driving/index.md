<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**🧠 NeurIPS2025** · 共 **30** 篇

**[3EED: Ground Everything Everywhere in 3D](3eed_ground_everything_everywhere_in_3d.md)**

:   提出 3EED——首个大规模多平台（车、无人机、四足机器人）、多模态（LiDAR+RGB）室外 3D 视觉定位基准，包含超 12.8 万目标和 2.2 万语言描述，规模是现有室外数据集的 10 倍；同时设计了跨平台对齐、多尺度采样和尺度自适应融合的基线方法，揭示了跨平台 3D grounding 的巨大性能差距。

**[AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead](aha_predicting_what_matters_next_online_highlight_detection.md)**

:   提出 AHA，一个自回归高光检测框架，在**不访问未来帧**的情况下根据自然语言任务描述实时预测每帧视频的相关性——利用多模态视觉语言模型+轻量解耦头+Dynamic SinkCache实现无限长度流媒体的恒定内存推理，在TVSum上超越离线全上下文方法+5.9% mAP、在Mr. Hisum上+8.3% mAP。

**[AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](autovla_a_vision-language-action_model_for_end-to-end_autonomous_driving_with_ad.md)**

:   提出AutoVLA——基于Qwen2.5-VL-3B的端到端自动驾驶VLA模型，将连续轨迹离散化为物理action tokens嵌入语言模型词表，支持fast/slow thinking双模式推理，通过GRPO强化微调同时提升10.6%性能和66.8%推理效率，在NAVSIM和Bench2Drive上达SOTA。

**[Availability-aware Sensor Fusion via Unified Canonical Space](availability-aware_sensor_fusion_via_unified_canonical_space.md)**

:   提出 ASF（Availability-aware Sensor Fusion），通过统一规范投影（UCP）将 Camera/LiDAR/4D Radar 特征映射到共享空间 + 跨传感器沿 patch 交叉注意力（CASAP，复杂度 $O(N_qN_s)$ 而非 $O(N_qN_sN_p)$）自动适配可用传感器 + 传感器组合损失（SCL）覆盖所有 7 种组合，在 K-Radar 上 AP_3D 73.6%（超 SOTA 20.1%），传感器故障时性能仅降 1.7%。

**[BayesG: Bayesian Ego-Graph Inference for Networked Multi-Agent Reinforcement Learning](bayesian_ego-graph_inference_for_networked_multi-agent_reinforcement_learning.md)**

:   BayesG 让网络化 MARL 中的每个 agent 通过贝叶斯变分推断学习其局部通信图的动态结构——用 Gumbel-Softmax 采样边掩码、ELBO 目标联合优化策略和图结构，在 167 agent 的纽约交通场景中奖励比最佳 baseline 高 50%+。

**[Causality Meets Locality: Provably Generalizable and Scalable Policy Learning for Networked Systems](causality_meets_locality_provably_generalizable_and_scalable_policy_learning_for.md)**

:   提出 GSAC 框架，将因果表示学习与元 Actor-Critic 结合，通过从网络 MARL 中学习稀疏因果掩码构建近似紧凑表示 (ACR) 实现可扩展性，通过域因子条件化策略实现跨域泛化，给出了因果恢复、收敛和自适应间隙的有限样本保证。

**[Chronograph A Real-World Graph-Based Multivariate Time Series Dataset](chronograph_a_real-world_graph-based_multivariate_time_series_dataset.md)**

:   提出 ChronoGraph——首个同时包含多元时间序列、显式服务依赖图和事件标签的真实世界微服务数据集（6个月 / ~700服务 / 5维指标 / 8005时间步），基准测试表明现有预测和异常检测方法在长期预测和拓扑感知方面均存在较大提升空间。

**[Continuous Simplicial Neural Networks](continuous_simplicial_neural_networks.md)**

:   提出 COSIMO，首个基于偏微分方程（PDE）的连续单纯形神经网络，通过在 Hodge Laplacian 上定义热扩散动力学实现连续信息流，比离散 SNN 具有更好的稳定性和过平滑控制能力。

**[CuMoLoS-MAE: A Masked Autoencoder for Remote Sensing Data Reconstruction](cumolos-mae_a_masked_autoencoder_for_remote_sensing_data_reconstruction.md)**

:   提出 CuMoLoS-MAE，一种结合课程掩码策略和 Monte Carlo 随机集成的 Masked Autoencoder，用于遥感大气廓线数据的高保真重建与逐像素不确定性量化。

**[CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation](cymbadiff_structured_spatial_diffusion_for_sketch-based_3d_semantic_urban_scene_.md)**

:   提出首个"草图→3D户外语义场景"生成任务与基准数据集 SketchSem3D，并设计 CymbaDiff（Cylinder Mamba Diffusion）去噪网络，通过柱坐标扫描+笛卡尔扫描的双路 Mamba 块实现结构化空间建模，在 FID 上比 3D Latent Diffusion 低 75%、比 3D DiT 低 71%。

**[DBLoss: Decomposition-based Loss Function for Time Series Forecasting](dbloss_decomposition-based_loss_function_for_time_series_forecasting.md)**

:   提出 DBLoss——一种基于指数移动平均分解的通用损失函数，在预测窗口内将预测值与真实值分别分解为季节和趋势分量并分开计算损失，可即插即用替换 MSE 为任意深度学习预测模型带来一致性提升，在 8 个基准数据集 × 8 个 SOTA 模型上全面验证有效性。

**[DINO-Foresight: Looking into the Future with DINO](dino-foresight_looking_into_the_future_with_dino.md)**

:   提出 DINO-Foresight，在视觉基础模型（VFM）的语义特征空间中预测未来帧特征演化，通过自监督 Masked Feature Transformer 预测 DINOv2 多层特征的 PCA 压缩表示，搭配即插即用的 task-specific heads，单一模型同时完成语义分割、实例分割、深度估计和表面法线预测四项任务，大幅超越 VISTA 世界模型且推理快 100 倍。

**[DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving](drivedpo_policy_learning_via_safety_dpo_for_end-to-end_autonomous_driving.md)**

:   提出DriveDPO两阶段框架——先通过统一策略蒸馏将人类模仿相似度与规则安全分数融合为单一监督分布，再用Safety DPO构建"看似human-like但不安全 vs 既human-like又安全"的轨迹偏好对进行策略微调——在NAVSIM上达PDMS 90.0新SOTA。

**[Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation](extremely_simple_multimodal_outlier_synthesis_for_out-of-distribution_detection_.md)**

:   提出 Feature Mixing——一种极其简单的多模态异常值合成方法，从两种模态的特征中随机交换 $N$ 个维度即可生成 OOD 样本用于训练正则化，理论上保证合成异常值位于 ID 分布的低似然区域且偏移有界，在 8 个数据集 4 种模态上达到 SOTA 且比 NP-Mix 快 10×~370×。

**[Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling](flow_matching-based_autonomous_driving_planning_with_advanced_interactive_behavi.md)**

:   提出 Flow Planner——通过细粒度轨迹 token 化、交互增强时空融合架构和 flow matching + classifier-free guidance 三项协同创新，在 nuPlan Val14 上首次作为纯学习方法突破 90 分大关（90.43），在交互密集的 interPlan 基准上比 Diffusion Planner 高 8.92 分。

**[Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution](future-aware_end-to-end_driving_bidirectional_modeling_of_trajectory_planning_an.md)**

:   提出 SeerDrive，通过双向建模场景演化与轨迹规划（未来感知规划 + 迭代交互），在 NAVSIM 和 nuScenes 上取得 SOTA。

**[FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](futuresightdrive_thinking_visually_with_spatiotemporal_cot_f.md)**

:   FutureSightDrive 认为自动驾驶 VLA 的文本 CoT 会把关键视觉时空信息压缩丢失，提出“视觉时空 CoT”范式：先让模型以 world model 方式生成融合未来背景、车道线和 3D 目标框的统一未来帧，再将该 imagined scene 作为推理中介供 inverse-dynamics 规划器生成轨迹，从而显著提升轨迹精度、降低碰撞并改善场景理解。

**[GSAlign: Geometric and Semantic Alignment Network for Aerial-Ground Person Re-Identification](gsalign_geometric_and_semantic_alignment_network_for_aerial-ground_person_re-ide.md)**

:   提出 GSAlign 框架，通过可学习薄板样条变换 (LTPS) 和动态对齐模块 (DAM) 分别解决空地行人重识别中几何畸变与语义不对齐问题，在 CARGO 数据集空地协议上 mAP 提升 +18.8%、Rank-1 提升 +16.8%。

**[HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning](holollm_multisensory_foundation_model_for_language-grounded_human_sensing_and_re.md)**

:   提出 HoloLLM，首次将 LiDAR、红外、毫米波雷达、WiFi 等稀有传感模态接入多模态大语言模型（MLLM），通过 Universal Modality-Injection Projector（UMIP）在数据稀缺条件下实现传感模态与文本的高效对齐，在人体动作问答和描述任务上较现有 MLLM 提升约 30%。

**[How Different from the Past? Spatio-Temporal Time Series Forecasting with Self-Supervised Deviation Learning](how_different_from_the_past_spatio-temporal_time_series_forecasting_with_self-su.md)**

:   提出 ST-SSDL 框架，通过自监督偏差学习（SSDL）捕捉当前输入与历史模式之间的动态偏差，利用可学习原型离散化隐空间并以对比损失+偏差损失实现相对距离一致性，在六个时空基准上取得 SOTA。

**[L2RSI: Cross-View LiDAR-Based Place Recognition for Large-Scale Urban Scenes via Remote Sensing Imagery](l2rsi_cross-view_lidar-based_place_recognition_for_large-scale_urban_scenes_via_.md)**

:   提出 L2RSI，首个利用高分辨率遥感影像实现超大规模（100km²）城市场景 LiDAR 位置识别的框架，通过语义对比学习对齐 LiDAR BEV 与遥感语义空间，并引入时空粒子估计（STPE）聚合连续查询的时空信息，在 100km² 范围内 Top-1 精度达 83.27%。

**[LabelAny3D: Label Any Object 3D in the Wild](labelany3d_label_any_object_3d_in_the_wild.md)**

:   提出 LabelAny3D，一个基于分析合成（analysis-by-synthesis）的自动 3D 标注流水线，从单目图像重建完整 3D 场景以获取高质量 3D 包围框标注；基于此构建了 COCO3D 基准，覆盖 80 类日常物体，在开放词汇单目 3D 检测上显著提升性能。

**[Layer-Wise Modality Decomposition For Interpretable Multimodal Sensor Fusion](layer-wise_modality_decomposition_for_interpretable_multimodal_sensor_fusion.md)**

:   提出 LMD（Layer-Wise Modality Decomposition），一种事后、模型无关的可解释性方法，通过逐层线性化神经网络操作将多模态融合模型的预测精确分解为各传感器模态的贡献，首次实现了自动驾驶感知模型中对单个输入模态的预测归因，并在 camera-radar、camera-LiDAR、camera-radar-LiDAR 多种融合设置下验证了有效性。

**[Neurosymbolic Diffusion Models](neurosymbolic_diffusion_models.md)**

:   本文提出神经符号扩散模型（NeSyDM），通过将离散掩码扩散模型与符号程序结合，突破了传统神经符号预测器中概念条件独立假设的限制，在保持可扩展性的同时建模概念间依赖关系和不确定性，在视觉推理和自动驾驶任务上取得了 SOTA 准确率和校准性能。

**[Regret Lower Bounds for Decentralized Multi-Agent Stochastic Shortest Path Problems](regret_lower_bounds_for_decentralized_multi-agent_stochastic_shortest_path_probl.md)**

:   本文首次为去中心化多智能体随机最短路径问题（Dec-MASSP）在线性函数逼近设定下建立了 $\Omega(\sqrt{K})$ 的 regret 下界，通过构造难以学习的实例族并利用对称性论证识别最优策略结构，证明了该下界与已有上界在 episode 数 $K$ 上达到匹配。

**[SDTagNet: Leveraging Text-Annotated Navigation Maps for Online HD Map Construction](sdtagnet_leveraging_text-annotated_navigation_maps_for_online_hd_map_constructio.md)**

:   提出 SDTagNet，首次通过 BERT 编码 OpenStreetMap 文本标注（路名/车道数/单行道等）并用点级图 Transformer 编码所有 SD 地图元素（点/线/关系），在远距离 HD 地图构建上相比无先验方法提升 +5.9 mAP（+45%），超越已有 SD 地图先验方法 +3.2 mAP（+20%）。

**[Simworld-Robotics Synthesizing Photorealistic And Dynamic Urban Environments For](simworld-robotics_synthesizing_photorealistic_and_dynamic_urban_environments_for.md)**

:   提出 SimWorld-Robotics (SWR)，一个基于 Unreal Engine 5 的大规模城市仿真平台，支持程序化生成无限逼真城市环境，并以此构建了多模态导航（SimWorld-MMNav）和多机器人搜索（SimWorld-MRS）两个新 benchmark，揭示了当前 VLM 在户外城市任务中的严重能力缺陷。

**[Towards Foundational LiDAR World Models with Efficient Latent Flow Matching](towards_foundational_lidar_world_models_with_efficient_latent_flow_matching.md)**

:   本文提出首个**可迁移的 LiDAR 世界模型**，通过 Swin Transformer VAE 实现 192× 高压缩比（SOTA 重建精度）、条件流匹配（CFM）替代扩散模型实现 SOTA 语义占据预测（仅需前人 4.38% FLOPs），并在三种域迁移任务中以 5% 标注数据超越 OccWorld 全量训练。

**[Transun A Preemptive Paradigm To Eradicate Retransformation Bias Intrinsically F](transun_a_preemptive_paradigm_to_eradicate_retransformation_bias_intrinsically_f.md)**

:   针对推荐系统中变换 MSE 回归模型的逆变换偏差（retransformation bias）问题，提出先发制人（preemptive）的 TranSUN 方法，通过联合学习辅助分支显式建模偏差，在训练阶段即从模型内部消除偏差，具有理论无偏保证和良好收敛性，并已部署在淘宝首页猜你喜欢的商品和短视频推荐场景。

**[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](unifying_appearance_codes_and_bilateral_grids_for_driving_scene_gaussian_splatti.md)**

:   提出多尺度双边网格金字塔统一全局外观编码和像素级双边网格——3 级层级（粗→中→细）分别捕捉全局/区域/像素级光度变化，通过亮度引导的切片-融合管线和自适应正则化解决驾驶场景 3DGS 的光度不一致问题，Waymo 上 Chamfer Distance 比 OmniRe 改善 28.2%。
