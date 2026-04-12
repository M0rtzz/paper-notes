---
title: >-
  ICML2025 自动驾驶方向 11篇论文解读
description: >-
  11篇ICML2025 自动驾驶方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🚗 自动驾驶

**🧪 ICML2025** · 共 **11** 篇

**[Dont Be So Negative Score-Based Generative Modeling With Oracle-Assisted Guidanc](dont_be_so_negative_score-based_generative_modeling_with_oracle-assisted_guidanc.md)**

:   提出 Gen-neG，利用 oracle 标记的负样本迭代训练分类器引导扩散模型，将生成分布从无效区域引导至正支撑域，应用于自动驾驶碰撞避免和安全人体运动生成。

**[Drivegpt Scaling Autoregressive Behavior Models For Driving](drivegpt_scaling_autoregressive_behavior_models_for_driving.md)**

:   提出 DriveGPT，一个 1.4B 参数的自回归驾驶行为模型，在 1.2 亿训练片段上训练，探索了驾驶行为建模中数据/模型/计算的缩放特性，在规划和预测任务上展示了缩放收益。

**[Geometry-To-Image Synthesis-Driven Generative Point Cloud Registration](geometry-to-image_synthesis-driven_generative_point_cloud_registration.md)**

:   提出生成式点云配准新范式，通过 DepthMatch-ControlNet 和 LiDARMatch-ControlNet 从点云生成跨视图一致的 RGB 图像对，融合颜色信息增强几何描述子，即插即用地提升现有配准方法。

**[Goirl Graph-Oriented Inverse Reinforcement Learning For Multimodal Trajectory Pr](goirl_graph-oriented_inverse_reinforcement_learning_for_multimodal_trajectory_pr.md)**

:   提出 GoIRL，首次将最大熵 IRL 框架与向量化场景表示结合的轨迹预测方法，通过 feature adaptor 将车道图特征聚合到网格空间实现 IRL 兼容，结合层级参数化轨迹生成器和 MCMC 概率融合，在 Argoverse 和 nuScenes 上达 SOTA。

**[Hierarchical And Collaborative Llm-Based Control For Multi-Uav Motion And Commun](hierarchical_and_collaborative_llm-based_control_for_multi-uav_motion_and_commun.md)**

:   提出一种基于 LLM 的层次化协作控制框架，通过 HAPS 端部署的元控制器 LLM 和 UAV 端部署的边缘控制器 LLM 的双层协同，实现多 UAV 在 3D 空中高速公路场景下的运动规划与通信接入联合优化。

**[Hybrid Quantum-Classical Multi-Agent Pathfinding](hybrid_quantum-classical_multi-agent_pathfinding.md)**

:   提出首个混合量子-经典多智能体路径规划（MAPF）最优算法 QP/QCP，基于分支-割-定价框架，通过将受限 ILP 子问题转化为 QUBO 问题在量子硬件上求解，在基准数据上优于先前 QUBO 方法和 SOTA MAPF 求解器。

**[Infocons Identifying Interpretable Critical Concepts In Point Clouds Via Informa](infocons_identifying_interpretable_critical_concepts_in_point_clouds_via_informa.md)**

:   提出InfoCons框架，用信息论原理将点云分解为3D概念，通过可学习先验检验每个概念对模型预测的因果效应，生成既忠实（保留因果影响点）又概念连贯（语义有意义）的解释。

**[R3Dm Enabling Role Discovery And Diversity Through Dynamics Models In Multi-Agen](r3dm_enabling_role_discovery_and_diversity_through_dynamics_models_in_multi-agen.md)**

:   提出 R3DM 框架，通过最大化智能体角色、历史轨迹与未来预期行为之间的互信息，利用动力学模型驱动的内在奖励实现角色多样性与协调性的平衡，在 SMAC/SMACv2 环境中将胜率提升最高 20%。

**[Safemap Robust Hd Map Construction From Incomplete Observations](safemap_robust_hd_map_construction_from_incomplete_observations.md)**

:   SafeMap 提出了一个即插即用的鲁棒高精地图构建框架，通过高斯采样视角重建（G-PVR）和蒸馏式 BEV 校正（D-BEVC）两个模块，在相机视角缺失的不完整观测条件下仍能准确构建矢量化高精地图。

**[Sphinx Structural Prediction Using Hypergraph Inference Network](sphinx_structural_prediction_using_hypergraph_inference_network.md)**

:   提出SPHINX模型以无监督方式从点级信号中推断潜在超图结构：将超边发现建模为聚类问题，用k-subset可微采样生成离散超图，可插入任何超图网络，在轨迹预测和节点分类上超越现有方法。

**[When Every Millisecond Counts Real-Time Anomaly Detection Via The Multimodal Asy](when_every_millisecond_counts_real-time_anomaly_detection_via_the_multimodal_asy.md)**

:   提出多模态异步混合网络，结合事件相机的高时间分辨率（异步 GNN 处理）和 RGB 相机的丰富空间特征（CNN 处理），在交通异常检测中实现 579 FPS 的推理速度和 1.17s 的平均响应时间，首次将事件流引入自动驾驶异常检测领域。
