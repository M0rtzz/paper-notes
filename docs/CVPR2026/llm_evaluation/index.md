---
title: >-
  CVPR2026 LLM评测方向 12篇论文解读
description: >-
  12篇CVPR2026 LLM评测方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📊 LLM评测

**📷 CVPR2026** · 共 **12** 篇

**[Adabet Gradient-Free Layer Selection For Efficient Training Of Deep Neural Netwo](adabet_gradient-free_layer_selection_for_efficient_training_of_deep_neural_netwo.md)**

:   提出 AdaBet，一种基于代数拓扑（第一 Betti 数 $b_1$）的无梯度层选择方法，仅通过前向传播计算每层激活空间的拓扑复杂度来决定哪些层需要微调，无需标签、梯度或反向传播，在 ResNet50/VGG16/MobileNetV2/ViT-B16 上以仅 10% 层微调达到优于全量训练的准确率，同时峰值内存降低约 40%。

**[Cross-Scale Pansharpening Via Scaleformer And The Panscale Benchmark](cross-scale_pansharpening_via_scaleformer_and_the_panscale_benchmark.md)**

:   提出首个跨尺度全色锐化数据集PanScale和评测基准PanScale-Bench，以及ScaleFormer框架——将分辨率变化重新解释为序列长度变化，通过Scale-Aware Patchify分桶采样+解耦空间-序列建模+RoPE实现跨尺度泛化。

**[Cryohype Reconstructing A Thousand Cryo-Em Structures With Transformer-Based Hyp](cryohype_reconstructing_a_thousand_cryo-em_structures_with_transformer-based_hyp.md)**

:   提出 CryoHype，一种基于 Transformer 超网络的冷冻电镜重建方法，通过动态调整隐式神经表示（INR）的权重来减少参数共享，首次实现了从无标签冷冻电镜图像中同时重建 1000 种不同蛋白质结构。

**[Enhancing Out-Of-Distribution Detection With Extended Logit Normalization](enhancing_out-of-distribution_detection_with_extended_logit_normalization.md)**

:   本文发现 LogitNorm 在训练中会导致两种特征坍塌（维度坍塌和原点坍塌），提出了一种无超参数的 Extended Logit Normalization（ELogitNorm），用特征到决策边界的距离替代到原点的距离作为缩放因子，在不损失分类精度的前提下显著提升各种 post-hoc OOD 检测方法的性能和置信度校准。

**[Flow3R Factored Flow Prediction For Scalable Visual Geometry Learning](flow3r_factored_flow_prediction_for_scalable_visual_geometry_learning.md)**

:   提出"分解式光流预测"（Factored Flow）模块，用源视图的几何 latent + 目标视图的位姿 latent 预测光流，使无标注视频可作为三维几何学习的监督信号，在静态/动态场景的 8 个基准上达到 SOTA。

**[Free-Grained Hierarchical Visual Recognition](free-grained_hierarchical_visual_recognition.md)**

:   提出"自由粒度"层级视觉识别（free-grained hierarchical recognition），允许训练标签出现在分类法的任意层级，并提出文本引导伪属性和分类法引导半监督学习两种方法来弥补缺失监督，推理时模型自适应选择预测深度。

**[Hier-Cos Making Deep Features Hierarchy-Aware Via Composition Of Orthogonal Subs](hier-cos_making_deep_features_hierarchy-aware_via_composition_of_orthogonal_subs.md)**

:   提出 Hier-COS 框架，通过为层次树中每个节点分配正交基向量，构造理论上保证层次一致性的层次感知向量空间(HAVS)，首次统一了"层次感知细粒度分类"和"层次多级分类"，同时提出新评估指标HOPS，在4个数据集上全面超越SOTA。

**[Hiercos Making Deep Features Hierarchyaware Via Co](hiercos_making_deep_features_hierarchyaware_via_co.md)**

:   提出Hier-COS框架，为层次标签树中的每个节点分配正交基向量，通过子空间组合（祖先基+自身基+后代基）构建层次感知向量空间（HAVS），理论保证特征空间的距离结构与层次树一致，同时提出HOPS评估指标解决现有层次化评估指标的排列不变性缺陷。

**[Out Of Sight Out Of Mind Evaluating State Evolution In Video World Models](out_of_sight_out_of_mind_evaluating_state_evolution_in_video_world_models.md)**

:   提出 StEvo-Bench 基准（225个任务×6类演化），通过遮挡或相机移开等观测控制手段系统评测9个视频世界模型能否将状态演化与观测解耦，发现所有模型在观测中断时成功率不足10%，并通过5个专项验证器精准定位失败模式。

**[Semi-Supervised Conformal Prediction With Unlabeled Nonconformity Score](semi-supervised_conformal_prediction_with_unlabeled_nonconformity_score.md)**

:   提出 SemiCP 框架，通过最近邻匹配（NNM）分数将无标签数据引入 conformal prediction 的校准流程，在标注数据极少时将平均覆盖率偏差降低最多 77%，同时缩小预测集。

**[Temporal Imbalance Of Positive And Negative Supervision In Class-Incremental Lea](temporal_imbalance_of_positive_and_negative_supervision_in_class-incremental_lea.md)**

:   提出时序不平衡（Temporal Imbalance）这一被忽视的类增量学习偏差来源，并设计 Temporal-Adjusted Loss（TAL）通过时间衰减记忆核动态降低旧类的负监督权重，以即插即用的方式显著缓解灾难性遗忘。

**[Weakly Supervised Video Anomaly Detection With Anomaly-Connected Components And ](weakly_supervised_video_anomaly_detection_with_anomaly-connected_components_and_.md)**

:   提出 LAS-VAD 框架，通过异常连通分量机制（ACC）将视频帧划分为语义一致的组来生成伪标签弥补帧级标注缺失，并通过意图感知机制（IAM）利用位置-速度-加速度特征区分外观相似但意图不同的正常/异常行为，在 XD-Violence 上达 89.96% AP (I3D)。
