<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🤖 AAAI2026** · 共 **31** 篇

**[10 Open Challenges Steering the Future of Vision-Language-Action Models](10_open_challenges_steering_the_future_of_vision-language-ac.md)**

:   一篇针对Vision-Language-Action(VLA)模型的综述/展望论文，系统梳理了VLA领域的10大开放挑战（多模态感知、鲁棒推理、数据质量、评估、跨机器人泛化、效率、全身协调、安全、多智能体、人机协作）以及4大新兴趋势（层次化规划、空间理解、世界动力学建模、数据合成），为VLA研究指明方向。

**[AHAN: Asymmetric Hierarchical Attention Network for Identical Twin Face Verification](ahan_asymmetric_hierarchical_attention_network_for_identical.md)**

:   针对同卵双胞胎人脸验证这一极端细粒度识别挑战，提出 AHAN 多流架构，通过层次交叉注意力 (HCA) 对语义面部区域做多尺度分析、面部不对称注意力模块 (FAAM) 捕获左右脸差异签名、以及双胞胎感知配对交叉注意力 (TA-PWCA) 训练正则化，在 ND_TWIN 数据集上将双胞胎验证精度从 88.9% 提升至 92.3%（+3.4%）。

**[Anti-adversarial Learning: Desensitizing Prompts for Large Language Models](anti-adversarial_learning_desensitizing_prompts_for_large_la.md)**

:   提出 PromptObfus，通过"反对抗学习"思路将用户 prompt 中的敏感词替换为语义不同但不影响任务输出的词，从而在不降低远端 LLM 任务表现的前提下彻底消除显式隐私泄露，并将隐式隐私推理攻击成功率降低 62.70%。

**[Authority Backdoor: A Certifiable Backdoor Mechanism for Authoring DNNs](authority_backdoor_a_certifiable_backdoor_mechanism_for_authoring_dnns.md)**

:   提出 Authority Backdoor，将硬件指纹作为后门触发器嵌入 DNN，使模型仅在授权设备上正常工作，并通过随机平滑实现可认证鲁棒性，抵御自适应触发器逆向攻击。

**[Auto-PRE: An Automatic and Cost-Efficient Peer-Review Framework for Language Generation Evaluation](auto-pre_an_automatic_and_cost-efficient_peer-review_framework_for_language_gene.md)**

:   提出 Auto-PRE 框架，通过自动资格考试从一致性、相关性、自信度三个维度筛选合格的 LLM 评估者，在无需人工标注的前提下实现了 SOTA 评估性能并大幅降低成本。

**[Behavior Tokens Speak Louder: Disentangled Explainable Recommendation with Behavior Vocabulary](behavior_tokens_speak_louder_disentangled_explainable_recommendation_with_behavi.md)**

:   提出 BEAT 框架，通过向量量化自编码将用户/物品的行为表征离散化为可解释的 behavior tokens，结合多层级语义监督将协同过滤信号对齐到冻结 LLM 的语义空间，实现零样本可解释推荐。

**[Bias Association Discovery Framework for Open-Ended LLM Generations](bias_association_discovery_framework_for_open-ended_llm_generations.md)**

:   提出偏见关联发现框架 BADF，通过分析 LLM 开放式故事生成中的叙事内容，系统性地提取人口统计身份与描述性概念之间的已知和未知偏见关联，突破了以往依赖预定义偏见概念的局限。

**[Can LLMs Truly Embody Human Personality? Analyzing AI and Human Behavior Alignment in Dispute Resolution](can_llms_truly_embody_human_personality_analyzing_ai_and_human_behavior_alignmen.md)**

:   提出首个系统对比框架，在配对的冲突调解场景中直接比较人类与人格提示LLM的策略行为差异，发现LLM在人格-行为映射上与人类存在显著偏差，挑战了"人格提示即可代理人类行为"的假设。

**[CCFQA: A Benchmark for Cross-Lingual and Cross-Modal Speech and Text Factuality Evaluation](ccfqa_a_benchmark_for_cross-lingual_and_cross-modal_speech_and_text_factuality_e.md)**

:   提出 CCFQA，一个覆盖 8 种语言、包含 14,400 条平行语音-文本事实问答样本的跨语言跨模态基准，用于系统评估多模态大语言模型在不同语言和输入模态下的事实一致性，并提出基于英语桥接的 few-shot 迁移策略 LLM-SQA。

**[CLIP-FTI: Fine-Grained Face Template Inversion via CLIP-Driven Attribute Conditioning](clip-fti_fine-grained_face_template_inversion_via_clip-driven_attribute_conditio.md)**

:   首次利用 CLIP 提取面部细粒度语义属性嵌入来辅助人脸模板反演（FTI），通过跨模态特征交互网络将泄露模板与属性嵌入融合并投影到 StyleGAN 潜空间，生成身份一致且属性细节更丰富的人脸图像，在识别准确率、属性相似度和跨模型攻击迁移性上均超越 SOTA。

**[CLIPPan: Adapting CLIP as A Supervisor for Unsupervised Pansharpening](clippan_adapting_clip_as_a_supervisor_for_unsupervised_pansharpening.md)**

:   提出 CLIPPan，通过轻量微调 CLIP 使其理解多光谱/全色/高分辨率多光谱图像类型及全色锐化过程，然后利用 Wald 协议等文本提示作为语义监督信号，实现无需地面真值的全分辨率无监督全色锐化，可作为即插即用模块兼容任意全色锐化骨干网络。

**[CoordAR: One-Reference 6D Pose Estimation of Novel Objects via Autoregressive Coordinate Map Generation](coordar_one-reference_6d_pose_estimation_of_novel_objects_via_autoregressive_coo.md)**

:   提出 CoordAR，将单参考视图 6D 位姿估计中的 3D-3D 对应关系建模为离散 token 的自回归生成问题，通过坐标图 token 化、模态解耦编码和自回归 Transformer 解码器，在多个基准上显著超越现有单视图方法，并对对称、遮挡等挑战场景展现强鲁棒性。

**[DEIG: Detail-Enhanced Instance Generation with Fine-Grained Semantic Control](deig_detail-enhanced_instance_generation_with_fine-grained_semantic_control.md)**

:   提出 DEIG，一个面向细粒度多实例图像生成的框架，通过实例细节提取器（IDE）将 LLM 编码器的高维嵌入蒸馏为紧凑的实例感知表示，并用细节融合模块（DFM）的实例掩码注意力防止属性泄漏，在多属性（颜色+材质+纹理）复合描述的生成任务上大幅超越现有方法。

**[Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment](dexterous_manipulation_transfer_via_progressive_kinematic-dynamic_alignment.md)**

:   提出 PKDA 框架，通过渐进式运动学-动力学对齐，将人手操作视频自动转化为多指灵巧手的高质量操作轨迹，平均迁移成功率达 73%。

**[Distributionally Robust Online Markov Game with Linear Function Approximation](distributionally_robust_online_markov_game_with_linear_function_approximation.md)**

:   本文研究具有线性函数近似的在线分布鲁棒马尔可夫博弈，首次识别了该设定下的学习困难性，并提出 DR-CCE-LSI 算法，在特定特征映射条件下实现了关于特征维度 $d$ 的极小极大最优样本复杂度。

**[Efficient and Reliable Hitting-Set Computations for the Implicit Hitting Set Approach](efficient_and_reliable_hitting-set_computations_for_the_implicit_hitting_set_app.md)**

:   探索IHS框架中打击集计算的替代方案（PB推理+随机局部搜索），发现商业IP最高效但有数值不稳定性，PB推理可提供竞争性效率+正确性保证+计算证书。

**[Enhancing Noise Resilience in Face Clustering via Sparse Differential Transformer](enhancing_noise_resilience_in_face_clustering_via_sparse_differential_transforme.md)**

:   提出预测驱动的 Top-K Jaccard 相似度系数提升邻居纯度，配合稀疏差分 Transformer（SDT）消除噪声注意力，在 MS-Celeb-1M 等大规模人脸聚类数据集上达到 SOTA 性能。

**[Enhancing Robustness of Offline RL Under Data Corruption via SAM](enhancing_robustness_of_offline_reinforcement_learning_under_data_corruption_via.md)**

:   首次将 Sharpness-Aware Minimization (SAM) 作为即插即用优化器应用于离线 RL，假设数据损坏导致损失景观中出现尖锐极小值从而泛化差，SAM 通过寻找平坦极小值提升鲁棒性，在 D4RL 基准上 IQL+SAM 平均得分从 34.47 提升到 44.40。

**[Failures to Surface Harmful Contents in Video Large Language Models](failures_to_surface_harmful_contents_in_video_large_language_models.md)**

:   本文首次系统分析了 VideoLLM 的安全性，揭示了三种结构性设计缺陷（稀疏时间采样、空间 token 下采样、模态融合不平衡），使得视频中清晰可见的有害内容在模型生成的文本摘要中被遗漏（omission rate 超 90%），并设计了三种零查询黑盒攻击来验证漏洞严重性。

**[Finextrol Controllable Motion Generation Via Fine-Grained Text](finextrol_controllable_motion_generation_via_fine-grained_text.md)**

:   提出 FineXtrol 框架，使用带时间标注的细粒度文本描述作为控制信号，结合层次化对比学习增强 text encoder 的判别力，实现对特定身体部位在指定时间区间内的精确动作生成控制。

**[Improving Sparse IMU-based Motion Capture with Motion Label Smoothing](improving_sparse_imu-based_motion_capture_with_motion_label_smoothing.md)**

:   提出 Motion Label Smoothing，将经典 label smoothing 从分类任务适配到稀疏IMU运动捕捉中，通过融合骨骼结构感知的Perlin噪声作为平滑标签，在不修改模型架构的前提下以即插即用方式提升三种SOTA方法在四个数据集上的精度，GlobalPose在TotalCapture上SIP误差降低20.41%。

**[IROTE: Human-like Traits Elicitation of Large Language Model via In-Context Self-Reflective Optimization](irote_human-like_traits_elicitation_of_large_language_model_via_in-context_self-.md)**

:   提出 IROTE，一种基于信息瓶颈理论的上下文自我反思优化方法，通过迭代生成并优化紧凑且富有唤起力的文本"自我反思"（self-reflection），无需微调即可稳定地激发 LLM 在多种下游任务中表现出目标人类特质（价值观、道德、人格），一致性超越现有基线。

**[mmPred: Radar-based Human Motion Prediction in the Dark](mmpred_radar-based_human_motion_prediction_in_the_dark.md)**

:   首次将毫米波雷达引入人体运动预测(HMP)任务，提出mmPred——基于扩散模型的框架，通过双域历史运动表示（时域姿态细化TPR + 频域主导运动FDM）和全局骨骼关系Transformer(GST)，有效抑制雷达特有的噪声和时序不一致性，在mmBody和mm-Fi数据集上分别超越SOTA方法8.6%和22%。

**[Opera A Reinforcement Learning--Enhanced Orchestrated Planner-Executor Architect](opera_a_reinforcement_learning--enhanced_orchestrated_planner-executor_architect.md)**

:   提出 OPERA 框架，通过 Goal Planning Module 和 Reason-Execute Module 的分层架构，结合专为多 agent 设计的 MAPGRPO 训练算法，大幅提升 reasoning-oriented multi-hop retrieval 性能。

**[Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation](plug-and-play_clarifier_a_zero-shot_multimodal_framework_for_egocentric_intent_d.md)**

:   提出 Plug-and-Play Clarifier，一个零样本、模块化的多模态框架，将第一人称视角中的意图歧义问题分解为文本澄清、视觉质量评估和跨模态手势定位三个子任务，使 4-8B 小模型在意图消歧任务上提升约 30%，接近甚至超越大模型水平。

**[RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways](renew_risk-_and_energy-aware_navigation_in_dynamic_waterways.md)**

:   提出 RENEW 全局路径规划器，为水面自主航行器 (ASV) 在动态水流 (洋流) 环境中引入统一的风险感知和能量感知策略，通过自适应不可导航区域识别、最佳努力应急策略和基于约束 Delaunay 三角化的分层架构实现安全高效导航，应急碰撞测试中实现零碰撞。

**[Renormalization Group Guided Tensor Network Structure Search](renormalization_group_guided_tensor_network_structure_search.md)**

:   提出 RGTN 框架，将统计物理中的重正化群（Renormalization Group）理论引入张量网络结构搜索，通过多尺度粗粒化-扩展-压缩流程和可学习边门控实现连续拓扑演化，在光场压缩、高阶张量分解和视频补全任务上达到 SOTA 压缩率，同时比已有方法快 4–600 倍。

**[SOSControl: Enhancing Human Motion Generation through Saliency-Aware Symbolic Orientation and Timing Control](soscontrol_enhancing_human_motion_generation_through_saliency-aware_symbolic_ori.md)**

:   提出Salient Orientation Symbolic (SOS) script——基于Labanotation启发的可编程符号化运动表示框架，通过时序约束的凝聚聚类提取关键帧显著性，结合SMS数据增强和梯度优化的SOSControl框架实现对身体部位朝向和运动时序的精确控制，在HumanML3D上SOS-Acc达0.988且FID仅3.892。

**[Streaming Generation of Co-Speech Gestures via Accelerated Rolling Diffusion](streaming_generation_of_co-speech_gestures_via_accelerated_rolling_diffusion.md)**

:   提出基于 Rolling Diffusion 的流式共语手势生成框架，通过结构化渐进噪声调度将任意扩散模型转化为流式手势生成器，并引入 Rolling Diffusion Ladder Acceleration (RDLA) 实现最高 4× 加速（200 FPS），在 ZEGGS 和 BEAT 基准上全面超越基线。

**[W2S-AlignTree: Weak-to-Strong Inference-Time Alignment for Large Language Models via Monte Carlo Tree Search](w2s-aligntree_weak-to-strong_inference-time_alignment_for_large_language_models_.md)**

:   提出 W2S-AlignTree，首个将蒙特卡洛树搜索（MCTS）与弱到强泛化（W2SG）范式结合的推理时对齐框架，利用弱模型的步级代理值函数实时引导强模型生成，在情感控制、摘要、指令遵循任务上均显著超越基线，其中 Llama3-8B 摘要任务提升 15.9%。

**[Xlinear A Lightweight And Accurate Mlp-Based Model For Long-Term Time Series For](xlinear_a_lightweight_and_accurate_mlp-based_model_for_long-term_time_series_for.md)**

:   提出 XLinear，一个基于 MLP + sigmoid gating 的轻量时间序列预测模型，通过 global token 机制高效融合 endogenous 与 exogenous 变量信息，在 12 个数据集上实现精度与效率的最优平衡。
