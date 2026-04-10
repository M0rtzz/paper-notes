<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频理解

**📷 CVPR2026** · 共 **60** 篇

**[A4VL: A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning](a4vl_multiagent_long_video_reasoning.md)**

:   提出 A4VL，一个 training-free 的多 Agent 感知-行动联盟框架：多个异构 VLM Agent 在多轮循环中执行感知探索（事件分区 + CLIP 线索对齐定位关键帧）和行动探索（独立推理 → 交叉评分 → 共识/剪枝），在 5 个 VideoQA 基准上全面超越 18 个 VLM 和 11 个长视频专用方法，且推理延迟显著更低（MLVU 上 74s vs GPT-4o 127s）。

**[A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning](a_multi-agent_perception-action_alliance_for_efficient_long_video_reasoning.md)**

:   提出 A4VL，一个无训练的多智能体感知-行动联盟框架，通过事件驱动视频分块、线索引导的关键帧选择和多轮智能体协商剪枝机制，在五个视频问答基准上以显著更低的推理延迟全面超越 28 个基线方法。

**[ActivityForensics: A Comprehensive Benchmark for Localizing Manipulated Activity in Videos](activityforensics_a_comprehensive_benchmark_for_localizing_manipulated_activity_.md)**

:   首次提出活动级视频伪造定位任务和ActivityForensics大规模基准数据集（6K+伪造片段），通过grounding辅助的自动化数据构造管线制造高度逼真的活动篡改，并提出Temporal Artifact Diffuser (TADiff)基线方法，通过扩散式特征正则化放大伪造线索。

**[Attend Before Attention Efficient And Scalable Video Understanding Via Autoregre](attend_before_attention_efficient_and_scalable_video_understanding_via_autoregre.md)**

:   提出 AutoGaze——一个仅 3M 参数的轻量自回归模块，在 ViT 之前以多尺度方式选择最少量 patch 并去除时空冗余，实现 4×-100× token 压缩和最高 19× ViT 加速，使 MLLM 可扩展到 1K 帧 4K 分辨率视频。

**[AutoCut: End-to-end Advertisement Video Editing Based on Multimodal Discretization and Controllable Generation](autocut_end-to-end_advertisement_video_editing_based_on_multimodal_discretizatio.md)**

:   AutoCut 提出了一个端到端的广告视频编辑框架，通过残差向量量化（RQVAE）将视频、音频和文本统一到共享的离散 token 空间中，在 Qwen3-8B 上进行多模态对齐和监督微调，实现了视频选择、排序、脚本生成和背景音乐选择四项任务的统一处理，在多项指标上超越 GPT-4o 基线。

**[AutoGaze: Attend Before Attention — Efficient and Scalable Video Understanding via Autoregressive Gazing](autogaze_attend_before_attention_efficient_video.md)**

:   提出AutoGaze——在ViT/MLLM处理视频之前，用一个轻量模块自回归地选择最少的多尺度patch，减少4x-100x视觉token，加速最高19x，支持1K帧4K视频并在VideoMME达67.0%。

**[Beyond Single-Sample Reliable Multi-Sample Distillation For Video Understanding](beyond_single-sample_reliable_multi-sample_distillation_for_video_understanding.md)**

:   揭示视频 LVLM 黑盒蒸馏中单样本 teacher 响应存在严重不可靠性（跨问题方差 σ=0.22、采样内方差 σ=0.07~0.15、格式违规 1%~10%），提出 R-MSD 框架通过多样本 teacher pool + 任务自适应匹配 + 两阶段 SFT→RL 对抗蒸馏解决该问题，4B student 在 VideoMME/Video-MMMU/WorldSense 上全面超越同规模 Qwen3-VL-4B。

**[Beyond Single-Sample: Reliable Multi-Sample Distillation for Video Understanding](beyond_singlesample_reliable_multisample_distillat.md)**

:   提出 R-MSD 框架，通过每输入采样 K 个教师响应构建教师池，结合任务自适应质量匹配（封闭题质量加权、开放题均匀配对）和在线判别器对抗蒸馏，解决视频 LVLM 黑盒蒸馏中单样本监督不可靠的问题。

**[Color When It Counts: Grayscale-Guided Online Triggering for Always-On Streaming Video Sensing](color_when_it_counts_grayscale-guided_online_triggering_for_always-on_streaming_.md)**

:   提出"灰度常开、彩色按需"新范式，通过 ColorTrigger 在灰度流上用轻量二次规划在线检测色彩冗余，仅使用 8.1% 的 RGB 帧即保持全彩基线 91.6% 的性能，实现资源受限设备的 always-on 视频感知。

**[CVA: Context-aware Video-text Alignment for Video Temporal Grounding](cva_context-aware_video-text_alignment_for_video_temporal_grounding.md)**

:   提出 CVA（Context-aware Video-text Alignment）框架，通过 Query-aware Context Diversification（QCD）、Context-invariant Boundary Discrimination（CBD）损失和 Context-enhanced Transformer Encoder（CTE）三个协同组件，解决视频时序定位中的假阴性和背景关联问题，在 QVHighlights 上 R1@0.7 提升约 5 个点。

**[Decompose and Transfer: CoT-Prompting Enhanced Alignment for Open-Vocabulary Temporal Action Detection](decompose_and_transfer_cot-prompting_enhanced_alignment_for_open-vocabulary_temp.md)**

:   提出 Phase-wise Decomposition and Alignment (PDA) 框架，利用 LLM 的 CoT 推理能力将动作标签分解为"开始-中间-结束"三个阶段描述，通过文本引导的前景过滤和自适应阶段对齐实现细粒度动作模式迁移，在 THUMOS14 OV-TAD 上 Avg mAP 达 46.9（超越 SOTA Ti-FAD 的 41.2）。

**[DIvide, then Ground: Adapting Frame Selection to Query Types for Long-Form Video Understanding](divide_then_ground_adapting_frame_selection_to_query_types_for_long-form_video_u.md)**

:   提出 DIG，一个免训练的帧选择框架，通过将查询分为全局查询和定位查询两类，对全局查询使用均匀采样、对定位查询使用一套专门的内容自适应帧选择+LMM奖励评分+视频精炼流水线，在三个长视频理解基准上持续超越现有方法。

**[Do You See What I Am Pointing At? Gesture-Based Egocentric Video Question Answering](do_you_see_what_i_am_pointing_at_gesture-based_egocentric_video_question_answeri.md)**

:   提出 EgoPointVQA 数据集和 HINT（Hand Intent Tokens）方法，通过将 3D 手部关键点编码为手意图 token 并与视觉 token 交错输入 MLLM，解决第一人称视频中基于手势指向的指示性问答任务，HINT-14B 达 68.1% 准确率超越 InternVL3-14B 5.4pp。

**[Dual-Agent Reinforcement Learning For Adaptive And Cost-Aware Visual-Inertial Od](dual-agent_reinforcement_learning_for_adaptive_and_cost-aware_visual-inertial_od.md)**

:   提出双智能体强化学习框架，通过 Select Agent（基于IMU信号决定是否启动视觉前端）和 Fusion Agent（自适应融合视觉-惯性状态）两个轻量RL策略，在不完全移除VIBA的前提下大幅降低其调用频率和计算开销，实现精度-效率-显存的更优折中。

**[Echoes Of Ownership Adversarial-Guided Dual Injection For Copyright Protection I](echoes_of_ownership_adversarial-guided_dual_injection_for_copyright_protection_i.md)**

:   提出 AGDI 框架，通过对抗优化生成 trigger image 进行 MLLM 黑盒版权追踪：双注入机制同时在 response 级（CE loss 驱动辅助模型输出 target answer）和 semantic 级（最小化 trigger image 与 target text 的 CLIP 余弦距离）注入版权信息，并引入模型对抗训练模拟 fine-tune 抵抗，在 Qwen2-VL/LLaVA-1.5 上全面超越 PLA 和 RNA 基线。

**[EgoPointVQA: Gesture-Based Egocentric Video Question Answering](egopointvqa_gesture_based_egocentric_video_qa.md)**

:   提出 EgoPointVQA 数据集（4000 合成 + 400 真实第一人称视频）和 HINT 方法，通过 3D 手部关键点编码为手势意图 token 并与视觉 token 交织输入 MLLM，使模型能理解用户指向手势并回答指示性问题，HINT-14B 达到 68.1% 准确率，超越 InternVL3-14B 6.6 个百分点。

**[EgoXtreme: A Dataset for Robust Object Pose Estimation in Egocentric Views under Extreme Conditions](egoxtreme_a_dataset_for_robust_object_pose_estimation_in_egocentric_views_under_.md)**

:   提出 EgoXtreme，首个面向极端条件下第一人称视角的大规模 6D 物体位姿估计基准数据集，涵盖严重运动模糊、动态光照和烟雾遮挡三种真实挑战，揭示了当前 SOTA 位姿估计器在这些条件下的严重失效。

**[Enhancing Accuracy of Uncertainty Estimation in Appearance-based Gaze Tracking](enhancing_accuracy_of_uncertainty_estimation_in_ap.md)**

:   提出基于等保序回归的后校准(post-hoc calibration)方法，仅用50个标定样本即可修正视线追踪模型在域偏移下的不确定性估计失准，并引入CPE(Coverage Probability Error)指标替代EUC正确评估不确定性质量——校准后CPE从8%-45%降至~5%，95%置信区间覆盖率从16%-67%提升至86%-89%。

**[Enhancing Accuracy of Uncertainty Estimation in Appearance-based Gaze Tracking with Probabilistic Evaluation and Calibration](enhancing_accuracy_of_uncertainty_estimation_in_appearance-based_gaze_tracking_w.md)**

:   提出一种数据高效的后验校准方法，通过等保序回归将不确定性感知视线追踪模型的预测分布与真实观测分布对齐，并引入 Coverage Probability Error (CPE) 指标替代不可靠的误差-不确定性相关性(EUC)来评估不确定性质量。

**[FC-Track: Overlap-Aware Post-Association Correction for Online Multi-Object Tracking](fc-track_overlap-aware_post-association_correction_for_online_multi-object_track.md)**

:   提出 FC-Track，一种轻量级的后关联校正框架，通过基于 IoA（Intersection over Area）的重叠感知外观特征过滤和局部不匹配重分配策略，在在线 MOT 中显式纠正由目标重叠引起的身份切换错误，将长期身份切换比例降至 29.55%。

**[FC-Track: Overlap-Aware Post-Association Correction for Online Multi-Object Tracking](fctrack_overlapaware_postassociation_correction_fo.md)**

:   提出轻量后关联校正框架 FC-Track，通过 IoA 触发的外观更新抑制和局部检测-轨迹错配重分配，将长期身份切换比例从 36.86% 降至 29.55%，同时保持 MOT17/MOT20 上的 SOTA 水平。

**[First Frame Is the Place to Go for Video Content Customization](first_frame_is_the_place_to_go_for_video_content_customization.md)**

:   FFGo 揭示了视频生成模型的一个被忽视的固有能力——将首帧作为概念记忆缓冲区存储多个参考主体，仅通过 20-50 个训练样本的轻量 LoRA 适配即可激活这一能力，实现无需架构修改的多参考视频内容定制，在用户研究中以 81.2% 的首选率大幅超越现有方法。

**[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](flashmotion_few-step_controllable_video_generation_with_trajectory_guidance.md)**

:   提出 FlashMotion，一个三阶段训练框架，将多步轨迹可控视频生成模型蒸馏为少步版本，通过混合扩散+对抗目标微调 adapter，在少步推理下同时保持视频质量和轨迹准确性。

**[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](flashmotion_fewstep_controllable_video_generation.md)**

:   提出 FlashMotion 三阶段训练框架——先训轨迹 adapter、再蒸馏少步生成器、最后用扩散+对抗混合目标微调 adapter——在少步推理下实现高质量轨迹可控视频生成，并发布 FlashBench 评估基准。

**[FluxMem: Adaptive Hierarchical Memory for Streaming Video Understanding](fluxmem_adaptive_hierarchical_memory_for_streaming_video_understanding.md)**

:   提出 FluxMem，一个无需训练的流式视频理解框架，通过层级化记忆设计（短期/中期/长期）和两个自适应 token 压缩模块（TAS 去时间冗余 + SDC 去空间冗余），在丢弃 60-70% 视觉 token 的同时在 StreamingBench 和 OVO-Bench 上取得新 SOTA。

**[Frame2Freq Spectral Adapters For Fine-Grained Video Understanding](frame2freq_spectral_adapters_for_fine-grained_video_understanding.md)**

:   提出 Frame2Freq——首个在频域进行时序建模的 PEFT 适配器族，通过 FFT 将冻结 VFM 的帧嵌入变换到频谱空间并学习频带级滤波，在五个细粒度动作识别基准上以 <10% 的可训练参数超越全量微调模型。

**[GoalForce: Teaching Video Models to Accomplish Physics-Conditioned Goals](goal_force_teaching_video_models_to_accomplish_physics-conditioned_goals.md)**

:   提出 Goal Force 框架，通过多通道物理控制信号（目标力、直接力、质量）在简单合成数据上训练视频生成模型，使其学会从目标效果逆向规划因果链，实现零样本泛化到工具使用、人-物交互等复杂现实场景。

**[Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning](learning_to_assist_physics-grounded_human-human_control_via_multi-agent_reinforc.md)**

:   提出 AssistMimic，将人-人辅助交互动作的物理模仿建模为多智能体强化学习（MARL）问题，通过运动先验初始化、动态参考重定向和接触促进奖励，首次实现了力交换型辅助动作的物理仿真跟踪。

**[Let Your Image Move With Your Motion -- Implicit Multi-Object Multi-Motion Trans](let_your_image_move_with_your_motion_--_implicit_multi-object_multi-motion_trans.md)**

:   FlexiMMT 是首个支持隐式多目标多运动迁移的 I2V 框架，通过运动解耦掩码注意力机制 (MDMA) 和差异化掩码提取机制 (DMEM)，将多个参考视频的不同运动独立分配给目标图像中的不同物体，实现灵活组合式运动迁移。

**[Longvideo-R1 Smart Navigation For Low-Cost Long Video Understanding](longvideo-r1_smart_navigation_for_low-cost_long_video_understanding.md)**

:   提出 LongVideo-R1，一个配备推理能力的多模态 Agent，通过层次化视频树结构和智能导航策略，以平均仅 10.5 轮工具调用实现高效长视频问答，在精度-效率权衡上显著优于穷举式方法。

**[Occlusion-Aware SORT: Observing Occlusion for Robust Multi-Object Tracking](occlusion-aware_sort_observing_occlusion_for_robust_multi-object_tracking.md)**

:   提出遮挡感知跟踪框架 OA-SORT，通过显式建模目标遮挡状态来缓解位置代价混淆和 Kalman Filter 估计不稳定问题，在 DanceTrack/SportsMOT/MOT17 上均取得 SOTA 级提升，且组件可即插即用地集成到多种跟踪器中。

**[OpenMarcie: Dataset for Multimodal Action Recognition in Industrial Environments](openmarcie_dataset_for_multimodal_action_recognition_in_industrial_environments.md)**

:   提出目前最大规模的工业场景多模态动作识别数据集 OpenMarcie，融合可穿戴传感器与视觉数据共 8 种模态、200+ 通道、37+ 小时录制，并在 HAR 分类、开放词表描述、跨模态对齐三个基准上验证了惯性+视觉融合的优越性。

**[Question-Guided Visual Compression With Memory Feedback For Long-Term Video Unde](question-guided_visual_compression_with_memory_feedback_for_long-term_video_unde.md)**

:   提出 QViC-MF 框架，通过问题引导的多帧视觉压缩（QMSA）和上下文记忆反馈机制，在长视频理解任务上以极少的视觉 token（每帧仅 16 个）实现了 MLVU/LVBench/VNBench 等多个基准上的 SOTA。

**[Ragtrack Language-Aware Rgbt Tracking With Retrieval-Augmented Generation](ragtrack_language-aware_rgbt_tracking_with_retrieval-augmented_generation.md)**

:   首次将文本描述引入 RGBT 跟踪，提出基于检索增强生成（RAG）的框架 RAGTrack，通过多模态 Transformer 编码器、自适应 Token 融合和上下文感知推理模块，在四个 RGBT 基准上取得 SOTA。

**[Real-World Point Tracking With Verifier-Guided Pseudo-Labeling](real-world_point_tracking_with_verifier-guided_pseudo-labeling.md)**

:   提出 Verifier——一个元模型，通过学习逐帧评估多个预训练跟踪器预测的可靠性，从中选取最优候选构建高质量伪标签轨迹，实现无需人工标注的真实世界点跟踪微调，在四个真实基准上达到 SOTA。

**[Real-World Point Tracking with Verifier-Guided Pseudo-Labeling](realworld_point_tracking_with_verifierguided_pseud.md)**

:   提出一个可学习的Verifier元模型，通过逐帧评估多个预训练tracker预测的可靠性来生成高质量伪标签，实现合成数据到真实世界的高效域适应，在四个真实世界点跟踪基准上达到SOTA。

**[FlexHook: Rethinking Two-Stage Referring-by-Tracking in RMOT](rethinking_two-stage_referring-by-tracking_in_referring_multi-object_tracking_ma.md)**

:   提出 FlexHook，一种新颖的两阶段 Referring-by-Tracking 框架，通过基于采样的 Conditioning Hook（C-Hook）重新定义特征构建，并用 Pairwise Correspondence Decoder（PCD）替换 CLIP 余弦相似度匹配，首次使两阶段方法全面超越当前 SOTA 的一阶段方法。

**[FlexHook: Rethinking Two-Stage Referring-by-Tracking in RMOT](rethinking_twostage_referringbytracking_in_referri.md)**

:   FlexHook重新激活了两阶段RBT(Referring-by-Tracking)范式：用C-Hook从backbone直接采样目标特征(替代双编码)并注入语言条件线索，用PCD(成对对应解码器)替代CLIP余弦相似度做主动对应建模，首次让两阶段方法全面超越一阶段RMOT的SOTA——Refer-KITTI-V2上HOTA从10.32(iKUN)提升到42.53，训练仅1.91小时(2×4090)。

**[SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning](sail_similarity-aware_guidance_and_inter-caption_augmentation-based_learning_for.md)**

:   提出 SAIL，通过跨模态相似度引导的语义感知掩码生成和 LLM 合成字幕的辅助监督，在仅有字幕标注（无时间边界）的弱监督设置下，在 ActivityNet 和 YouCook2 上实现密集视频描述和事件定位的双 SOTA。

**[Sava-X Ego-To-Exo Imitation Error Detection Via Scene-Adaptive View Alignment An](sava-x_ego-to-exo_imitation_error_detection_via_scene-adaptive_view_alignment_an.md)**

:   提出 SAVA-X 框架，通过自适应采样、场景感知视角嵌入和双向交叉注意力融合三个互补模块，解决第三人称示范→第一人称模仿场景下的跨视角时序错误检测问题，在 EgoMe 基准上全面超越现有基线。

**[SAVA-X: Ego-to-Exo Imitation Error Detection via Scene-Adaptive View Alignment and Bidirectional Cross View Fusion](savax_egotoexo_imitation_error_detection_via_scene.md)**

:   提出Align-Fuse-Detect框架SAVA-X，通过Gumbel Top-K自适应采样去冗余、场景自适应视角嵌入缩小域差距、双向交叉注意力融合互补语义，在EgoMe数据集上Mean AUPRC达22.36，超越最强baseline +13.56%。

**[SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking](spiketrack_a_spike-driven_framework_for_efficient_visual_tracking.md)**

:   提出 SpikeTrack，首个完全符合脉冲驱动范式的 RGB 视觉跟踪框架，通过非对称时间步扩展、单向信息流和脑启发记忆检索模块（MRM），在 SNN 跟踪器中达到 SOTA 并与 ANN 跟踪器持平，同时能耗仅为 TransT 的 1/26。

**[Stay in your Lane: Role Specific Queries with Overlap Suppression Loss for Dense Video Captioning](stay_in_lane_role_query_dense_video_captioning.md)**

:   ROS-DVC通过为DETR-based密集视频描述设计角色专用查询初始化（分离定位和描述查询）+跨任务对比对齐损失+重叠抑制损失，在YouCook2上无需预训练即达到CIDEr 39.18的SOTA，超越使用GPT-2的DDVC。

**[Stay in your Lane: Role Specific Queries with Overlap Suppression Loss for Dense Video Captioning](stay_in_your_lane_role_specific_queries_with_overlap_suppression_loss_for_dense_.md)**

:   提出 ROS-DVC，通过将 DETR-based DVC 框架中的共享 query 分离为独立的 localization query 和 caption query，并设计 Overlap Suppression Loss 惩罚 query 间的时序重叠、Cross-Task Contrastive Alignment 保证跨任务语义一致性，在 YouCook2 和 ActivityNet Captions 上实现了 SOTA 的 captioning 和 localization 性能。

**[StreamingTOM: Streaming Token Compression for Efficient Video Understanding](streamingtom_streaming_token_compression_for_efficient_video_understanding.md)**

:   提出 StreamingTOM，一个无需训练的两阶段流式视频理解框架：Causal Temporal Reduction (CTR) 在 LLM 前通过因果时序选择将每帧 token 从 196 压缩到 50，Online Quantized Memory (OQM) 在 LLM 后通过 4-bit 量化和按需检索限制 kv-cache 增长，实现 15.7× 压缩比、1.2× 更低峰值显存和 2× 更快 TTFT。

**[StreamingTOM: Streaming Token Compression for Efficient Video Understanding](streamingtom_streaming_token_compression_video.md)**

:   针对流式视频 VLM 面临的因果性（无法访问未来帧）和累积性（token 无界增长）两个约束，提出 StreamingTOM——一个免训练、即插即用的两阶段框架，通过因果时序缩减（减少 pre-LLM prefill）和在线量化记忆（4-bit KV-cache 存储+按需检索反量化），实现 15.7× KV-cache 压缩比、较 SOTA LiveVLM 降低 1.2× 峰值内存和 2× 更快 TTFT，在离线基准平均 63.8% 和流式基准 RVS 55.8% 达到免训练方法 SOTA。

**[StreamReady: Learning What to Answer and When in Long Streaming Videos](streamready_learning_what_to_answer_and_when_in_long_streaming_videos.md)**

:   提出就绪性感知的流式视频理解范式，通过可学习的 `<RDY>` token 和 Answer Readiness Score (ARS) 指标，让模型不仅回答正确，还能在证据出现的恰当时刻作答，在 9 个流式/离线视频基准上取得 SOTA。

**[TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models](tear_temporal-aware_automated_red-teaming_for_text-to-video_models.md)**

:   提出 TEAR，首个针对 T2V 模型时序维度漏洞的自动化红队测试框架，通过两阶段优化的时序感知测试生成器和迭代精炼模型，生成文本上无害但能利用时序动态触发有害视频的提示，在开源和商业 T2V 模型上达到 80%+ 的攻击成功率。

**[F²HDR: Two-Stage HDR Video Reconstruction via Flow Adapter and Physical Motion Modeling](textf2texthdr_two-stage_hdr_video_reconstruction_via_flow_adapter_and_physical_m.md)**

:   提出 F²HDR，一个两阶段 HDR 视频重建框架，通过 Flow Adapter 将通用预训练光流适配到交替曝光场景以实现鲁棒对齐，并利用物理运动建模从光流中提取连续运动掩码来引导第二阶段的伪影消除，在真实 HDR 视频基准上达到 SOTA。

**[The Devil is in the Details: Enhancing Video Virtual Try-On via Keyframe-Driven Details Injection](the_devil_is_in_the_details_enhancing_video_virtual_try-on_via_keyframe-driven_d.md)**

:   提出 KeyTailor 框架，通过关键帧驱动的细节注入策略（服装动态增强 + 协同背景优化）在不修改 DiT 架构的前提下，大幅提升视频虚拟试穿的服装保真度与背景一致性，同时发布 15K 高清数据集 ViT-HD。

**[Trajtok Learning Trajectory Tokens Enables Better Video Understanding](trajtok_learning_trajectory_tokens_enables_better_video_understanding.md)**

:   提出 TrajTok——一种端到端可微的轨迹 tokenizer，将视频像素隐式聚类为目标轨迹 token，取代外部分割+跟踪流水线；在从头训练 (TrajViT2)、特征适配 (TrajAdapter) 和视觉语言模型连接器 (TrajVLM) 三种场景下均取得显著提升，尤其在长视频 QA 上大幅超越 patch pooling。

**[TrajTok: 学习轨迹Token实现更好的视频理解](trajtok_trajectory_token_video_understanding.md)**

:   提出TrajTok——首个端到端可微的轨迹视频tokenizer，通过隐式时空聚类将视频编码为物体轨迹token，无需外部分割/跟踪管线，在分类、检索和长视频QA上全面超越patch-based方法。

**[U-Mind: A Unified Framework for Real-Time Multimodal Interaction with Audiovisual Generation](u-mind_a_unified_framework_for_real-time_multimodal_interaction_with_audiovisual.md)**

:   提出 U-Mind，首个统一实时全栈多模态交互系统，支持高层推理对话和指令跟随，在单一交互循环中联合生成文本、语音、动作，并渲染为逼真视频，通过排练驱动学习和文本优先解码策略兼顾推理保持与跨模态对齐。

**[UETrack: A Unified and Efficient Framework for Single Object Tracking](uetrack_a_unified_and_efficient_framework_for_single_object_tracking.md)**

**[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](unitalking_a_unified_audio-video_framework_for_talking_portrait_generation.md)**

:   提出 UniTalking，一个基于 MM-DiT 的端到端说话人肖像生成框架，通过双流对称架构中的联合注意力机制显式建模音视频 token 的细粒度时序对应关系，实现 SOTA 的唇音同步精度，同时支持个性化语音克隆。

**[Utptrack Towards Simple And Unified Token Pruning For Visual Tracking](utptrack_towards_simple_and_unified_token_pruning_for_visual_tracking.md)**

:   提出 UTPTrack，首个在 one-stream Transformer 跟踪器中**同时对搜索区域 (SR)、动态模板 (DT) 和静态模板 (ST) 三个组件进行联合 token 剪枝**的统一框架，在 RGB 和多模态/语言引导跟踪中实现 65–67% 的视觉 token 裁减，且保持 99.7%–100.5% 的基线性能。

**[Videochat-M1 Collaborative Policy Planning For Video Understanding Via Multi-Age](videochat-m1_collaborative_policy_planning_for_video_understanding_via_multi-age.md)**

:   提出VideoChat-M1，用多智能体协作策略规划（CPP）+ 多智能体强化学习（MARL）替代传统固定工具调用策略，让多个策略Agent动态生成、执行和沟通工具调用计划，在8个视频理解基准上取得SOTA，LongVideoBench超Gemini 2.5 Pro 3.6%、超GPT-4o 15.6%。

**[VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning](videochatm1_collaborative_policy_planning_for_vide.md)**

:   VideoChat-M1 提出了多智能体协作策略规划（CPP）范式 + 多智能体强化学习（MARL）训练框架，让 4 个异构 VLM agent 动态生成和更新工具调用策略来理解视频，在 LongVideoBench 上超过 Gemini 2.5 Pro 3.6%，超过 GPT-4o 15.6%。

**[VirtueBench: Evaluating Trustworthiness under Uncertainty in Long Video Understanding](virtuebench_evaluating_trustworthiness_under_uncertainty_in_long_video_understan.md)**

:   提出 VirtueBench，首个评估 VLM 在不确定性下可信度的长视频理解基准，通过为每个视频构建多级帧采样并标注可回答/不可回答的 ground truth，揭示了现有模型普遍倾向于猜测而非诚实拒绝的问题。

**[Wavelet-Based Frame Selection By Detecting Semantic Boundary For Long Video Unde](wavelet-based_frame_selection_by_detecting_semantic_boundary_for_long_video_unde.md)**

:   提出 WFS-SB，一种免训练的帧选择框架，利用小波变换从查询-帧相似度信号中检测语义边界，将视频分割为语义连贯的片段后自适应分配帧预算并做多样性采样，在 VideoMME/MLVU/LongVideoBench 上大幅超越 SOTA。
