<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**🤖 AAAI2026** · 共 **25** 篇

**[A Theoretical Analysis of Detecting Large Model-Generated Time Series](a_theoretical_analysis_of_detecting_large_model-generated_time_series.md)**

:   首次研究时间序列大模型（TSLM）生成内容的检测问题——提出收缩假说（Contraction Hypothesis）：TSLM 生成的时间序列在递归预测下不确定性逐渐降低（分布越来越集中），而真实序列不会。基于此提出白盒检测器 UCE（Uncertainty Contraction Estimator），在 32 个数据集上超越 SOTA 基线。

**[Actor-Critic for Continuous Action Chunks: A Reinforcement Learning Framework for Long-Horizon Robotic Manipulation with Sparse Reward](actor-critic_for_continuous_action_chunks_a_reinforcement_le.md)**

:   AC3 提出了一个直接学习连续动作序列（action chunk）的 actor-critic 框架，通过"仅从成功轨迹更新 actor"的非对称更新规则和基于自监督锚点的内在奖励来稳定稀疏奖励下的长时域机器人操作学习，在 BiGym 和 RLBench 的 25 个任务上取得优于现有方法的成功率。

**[AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios](aerialmind_towards_referring_multi-object_tracking_in_uav_sc.md)**

:   构建了首个面向无人机场景的大规模 Referring Multi-Object Tracking（RMOT）基准数据集 AerialMind，并提出 HawkEyeTrack（HETrack）方法，通过视觉-语言共进化融合编码器和尺度自适应上下文精炼模块，在无人机航拍场景中实现语言引导的多目标跟踪。

**[An Overall Real-Time Mechanism for Classification and Quality Evaluation of Rice](an_overall_real-time_mechanism_for_classification_and_quality_evaluation_of_rice.md)**

:   提出一个实时大米品质评估整体机制，整合改进的 YOLO-v5（品种检测）、改进的 ConvNeXt-Tiny（完整度分级）和 K-means（垩白区域量化）三个模块，在自建的六品种两万张图像数据集上实现了 99.14% mAP 和 97.89% 检测准确率。

**[Beyond Boundaries: Leveraging Vision Foundation Models for Source-Free Object Detection](beyond_boundaries_leveraging_vision_foundation_models_for_so.md)**

:   提出利用VFM（DINOv2+Grounding DINO）增强无源域自适应目标检测（SFOD）的框架，通过全局特征对齐(PGFA)、实例级原型对比学习(PIFA)和双源伪标签融合(DEPF)三个模块，在6个跨域检测基准上取得SOTA，例如Cityscapes→Foggy Cityscapes达47.1% mAP（比DRU高3.5%），Sim10k→Cityscapes达67.4% AP（比DRU高8.7%）。

**[Beyond Fact Retrieval: Episodic Memory for RAG with Generative Semantic Workspaces](beyond_fact_retrieval_episodic_memory_for_rag_with_generative_semantic_workspace.md)**

:   提出 Generative Semantic Workspace (GSW)，一种神经科学启发的生成式记忆框架，为 LLM 构建结构化的情景记忆表示，在 EpBench 上 F1 达到 0.85，同时减少 51% 的查询时上下文 token。

**[Beyond Semantic Features: Pixel-Level Mapping for Generalized AI-Generated Image Detection](beyond_semantic_features_pixel-level_mapping_for_generalized_ai-generated_image_.md)**

:   提出像素级映射（pixel-level mapping）预处理方法，通过打破像素值的单调排列来抑制低频语义偏差、增强高频生成伪影，将 AI 生成图像检测的跨模型泛化准确率提升至 98.4%。

**[Connecting the Dots: Training-Free Visual Grounding via Agentic Reasoning](connecting_the_dots_training-free_visual_grounding_via_agent.md)**

:   提出 GroundingAgent，一个完全不需要任务特定微调的视觉定位框架，通过组合预训练的开放词汇检测器（YOLO World）、MLLM（Llama-3.2-11B-Vision）和 LLM（DeepSeek-V3）进行结构化迭代推理，在 RefCOCO/+/g 上实现 65.1% 的零样本平均准确率，大幅超越之前的 zero-shot 方法。

**[Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning](continuous_vision-language-action_co-learning_with_semantic-.md)**

:   提出CCoL框架，通过NeuralODE驱动的多模态连续协同学习（MCC）和双向交叉注意力的语义-物理对齐（CSA），在Behavioral Cloning中同时解决动作序列的物理不连续性和语义-物理失配问题，在三个仿真平台上平均相对提升8.0%，双臂插入任务最高达19.2%。

**[CTPD: Cross Tokenizer Preference Distillation](ctpd_cross_tokenizer_preference_distillation.md)**

:   提出 Cross-Tokenizer Preference Distillation (CTPD)，首个支持不同分词器间偏好蒸馏的统一框架，通过 Aligned Span Projection、跨分词器重要性加权和 Teacher-Anchored Reference 三项创新，在多个 benchmark 上显著超越现有方法。

**[Deep Incomplete Multi-View Clustering via Hierarchical Imputation and Alignment](deep_incomplete_multi-view_clustering_via_hierarchical_imputation_and_alignment.md)**

:   提出 DIMVC-HIA，一个集成层次化填充与双重对齐的深度不完整多视图聚类框架，先填充缺失聚类分配再填充缺失特征，在高缺失率（70%）下仍保持稳健性能。

**[Sketch-HARP: 分层自回归草图生成实现灵活笔画级绘制操控](generating_sketches_in_a_hierarchical_auto-regressive_proces.md)**

:   提出 Sketch-HARP 分层自回归草图生成框架，通过三阶段层次化过程（预测笔画嵌入→确定画布位置→生成绘制动作序列），首次实现草图绘制过程中的灵活笔画级操控，在替换/擦除/扩展等任务上显著优于 SketchEdit。

**[Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback, Diversity-Aware Sampling, and Conflict Regularization](ground_what_you_see_hallucination-resistant_mllms_via_caption_feedback_diversity.md)**

:   针对多模态大模型（MLLM）在强化学习训练中产生幻觉的三大根因——视觉误解、探索多样性不足、样本冲突——分别提出 Caption Reward、奖励方差引导的样本选择、以及基于 NTK 相似度的 InfoNCE 正则化，在多个基准上显著降低幻觉率。

**[H-GAR: A Hierarchical Interaction Framework via Goal-Driven Observation-Action Refinement for Robotic Manipulation](h-gar_a_hierarchical_interaction_framework_via_goal-driven_observation-action_re.md)**

:   提出层次化目标驱动框架 H-GAR，通过先预测目标观测再合成中间观测、并利用历史动作记忆库细化粗粒度动作，实现了观测与动作的显式双向交互，在仿真和真实机器人操控任务上取得 SOTA。

**[How Many Experts Are Enough? Towards Optimal Semantic Specialization for Mixture-of-Experts](how_many_experts_are_enough_towards_optimal_semantic_specialization_for_mixture-.md)**

:   提出MASS框架，通过基于梯度的语义漂移检测自适应扩展MoE专家池，并结合Top-p置信度路由策略，在无需超参搜索的情况下自动发现最优专家数量，同时增强专家间的语义分化。

**[Perceive Act And Correct Confidence Is Not Enough For Hyperspectral Classificati](perceive_act_and_correct_confidence_is_not_enough_for_hyperspectral_classificati.md)**

:   提出 CABIN 框架，通过认知感知-行动-纠正的闭环学习机制，利用认识论不确定性（epistemic uncertainty）替代单纯的置信度来指导半监督高光谱图像分类中的样本选择与伪标签管理，在仅用 75% 标注的情况下显著超过全标注基线。

**[Resource Efficient Sleep Staging via Multi-Level Masking and Prompt Learning](resource_efficient_sleep_staging_via_multi-level_masking_and_prompt_learning.md)**

:   提出 MASS (Mask-Aware Sleep Staging) 框架，通过多层级 masking 策略和层次化 prompt learning 机制，仅用 **10% 的原始 EEG 信号**即可实现可靠的睡眠分期，为资源受限的可穿戴睡眠监测系统提供方案。

**[REXO: Indoor Multi-View Radar Object Detection via 3D Bounding Box Diffusion](rexo_indoor_multi-view_radar_object_detection_via_3d_bounding_box_diffusion.md)**

:   将 DiffusionDet 的 2D BBox 扩散范式提升到 3D 雷达空间，提出 REXO 框架：通过含噪 3D BBox 的投影引导显式跨视图雷达特征关联，并引入地面约束减少扩散参数，在 HIBER 和 MMVR 两个室内雷达数据集上分别超越 SOTA +4.22 AP 和 +11.02 AP。

**[Robust Long-term Test-Time Adaptation for 3D Human Pose Estimation through Motion Discretization](robust_long-term_test-time_adaptation_for_3d_human_pose_estimation_through_motio.md)**

:   针对 3D 人体姿态估计在线测试时自适应中的误差累积问题，提出基于运动离散化（无监督聚类获得锚运动集）+ 自回放机制 + 软重置策略的解决方案，使模型能在长时间持续适应中稳健利用个人形态和习惯性运动特征，在 Ego-Exo4D 和 3DPW 上超越所有现有在线 TTA 方法。

**[SAGA: Learning Signal-Aligned Distributions for Improved Text-to-Image Generation](saga_learning_signal-aligned_distributions_for_improved_text-to-image_generation.md)**

:   提出SAGA方法，通过学习与提示词对齐的高斯分布来改进文本到图像生成模型的语义对齐，无需重新训练且支持文本和空间双条件生成，在SD 1.4和SD 3上大幅提升对齐性能（TIAM-3从8.4%提升到50.7%）。

**[Sm3Det A Unified Model For Multi-Modal Remote Sensing Object Detection](sm3det_a_unified_model_for_multi-modal_remote_sensing_object_detection.md)**

:   SM3Det提出了遥感领域的M2Det新任务（多模态数据集+多任务目标检测），通过网格级稀疏MoE骨干网络和动态子模块优化（DSO）机制，用单一模型同时处理SAR/光学/红外三种模态的水平/旋转框检测，显著超越各模态独立训练的三个专用模型组合。

**[Test-time Diverse Reasoning by Riemannian Activation Steering](test-time_diverse_reasoning_by_riemannian_activation_steering.md)**

:   提出 SPREAD 框架——一种无监督的测试时激活引导策略，通过在球面流形乘积上求解黎曼优化问题来最大化多条推理路径的隐藏激活张成的总体积，从而提升 Best-of-N 采样中的推理多样性和准确率，在数学推理基准上超越温度采样基线。

**[Towards Effective, Stealthy, and Persistent Backdoor Attacks Targeting Graph Foundation Models](towards_effective_stealthy_and_persistent_backdoor_attacks_targeting_graph_found.md)**

:   提出 GFM-BA，首个系统性地针对 Graph Foundation Models (GFMs) 预训练阶段的后门攻击方法，通过 label-free trigger 关联、node-adaptive trigger 生成和 persistent backdoor anchoring 三个模块，同时解决有效性、隐蔽性和持久性三大挑战。

**[Towards Scalable Web Accessibility Audit with MLLMs as Copilots](towards_scalable_web_accessibility_audit_with_mllms_as_copilots.md)**

:   提出 AAA 框架，通过 GRASP（基于图的多模态页面采样）和 MaC（MLLM 作为 Copilot）两大创新，将 WCAG-EM 标准操作化，实现可扩展的端到端网页无障碍审计。

**[TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models](ttf-vla_temporal_token_fusion_via_pixel-attention_integratio.md)**

:   TTF-VLA 提出了一种免训练的时序 Token 融合方法，通过灰度像素差异+注意力语义检测的双维度机制选择性地复用历史帧的视觉 Token，提升 VLA 模型在机器人操作任务中的推理质量，在 LIBERO 上平均提升 4.0 个百分点。
