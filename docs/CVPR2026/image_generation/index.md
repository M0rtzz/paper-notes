<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**📷 CVPR2026** · 共 **83** 篇

**[Accelerating Diffusion Model Training under Minimal Budgets: A Condensation-Based Perspective](accelerating_diffusion_model_training_under_minimal_budgets_a_condensation-based.md)**

:   提出 D2C（Diffusion Dataset Condensation）——首个面向扩散模型的数据集压缩框架，通过"Select + Attach"两阶段流水线，在仅使用 ImageNet 0.8%–8% 数据的条件下实现 100–233× 的训练加速，同时保持高质量图像生成能力。

**[ADAPT: Attention Driven Adaptive Prompt Scheduling and InTerpolating Orthogonal Complements for Rare Concepts Generation](adapt_attention_driven_adaptive_prompt_scheduling_and_interpolating_orthogonal_c.md)**

:   提出 ADAPT 框架，通过注意力驱动的自适应 Prompt 调度（APS）、池化嵌入操控（PEM）和潜空间操控（LSM）三个零样本模块，确定性且语义对齐地控制从通用到罕见概念的生成过渡，在 RareBench 上显著超越 R2F 基线。

**[Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration](adaptive_spectral_feature_forecasting_for_diffusion_sampling_acceleration.md)**

:   提出 Spectrum，一种基于切比雪夫多项式的全局谱域特征预测方法，将扩散模型去噪器的中间特征视为时间函数并用岭回归拟合系数，实现误差不随步长增长的长程特征预测，在 FLUX.1 上达到 4.79× 加速、在 Wan2.1-14B 上达到 4.67× 加速而质量几乎无损。

**[Agentic Retoucher for Text-To-Image Generation](agentic_retoucher_for_text-to-image_generation.md)**

:   将 T2I 扩散模型输出的局部失真（手指畸变、面部异常、文字错误等）校正问题建模为感知-推理-行动的多智能体循环系统 Agentic Retoucher，通过 Perception Agent 的上下文感知失真显著性图定位缺陷、Reasoning Agent 的结构化推理诊断失真类型、Action Agent 的工具选择执行修复，并配合 GenBlemish-27K 数据集实现端到端的迭代式自动修正。

**[Agentic Retoucher for Text-To-Image Generation](agentic_retoucher_for_texttoimage_generation.md)**

:   Agentic Retoucher 将 T2I 生成后的缺陷修复重构为"感知→推理→行动"的人类式闭环决策过程，用三个协作 agent 分别做上下文感知的扭曲检测、人类对齐的诊断推理和自适应局部修复，在 GenBlemish-27K 上 plausibility 提升 2.89 分，83.2% 的结果被人类评为优于原图。

**[AlignVAR: Towards Globally Consistent Visual Autoregression for Image Super-Resolution](alignvar_towards_globally_consistent_visual_autoregression_for_image_super-resol.md)**

:   针对视觉自回归（VAR）模型在图像超分辨率中的两个一致性问题——注意力局部偏差导致的空间不连贯和残差监督导致的跨尺度误差累积，提出 AlignVAR 框架，通过空间一致性自回归（SCA）和层级一致性约束（HCC）协同解决，实现比扩散方法快 10× 以上的推理速度且重建质量更优。

**[All-in-One Slider for Attribute Manipulation in Diffusion Models](all-in-one_slider_for_attribute_manipulation_in_diffusion_models.md)**

:   提出 All-in-One Slider 框架，通过在文本编码器中间层嵌入上训练一个轻量级 Attribute Sparse Autoencoder，将属性分解为高维稀疏激活空间中的解耦方向，从而用单一模块实现对多种面部属性的连续、细粒度、可组合控制，并首次展示对未见属性（如种族、名人）的零样本连续操控能力。

**[All-in-One Slider for Attribute Manipulation in Diffusion Models](all_in_one_slider_attribute_manipulation.md)**

:   提出 All-in-One Slider 框架，通过在文本嵌入空间上训练一个属性稀疏自编码器（Attribute Sparse Autoencoder），将多种人脸属性解耦为稀疏的语义方向，实现单一轻量模块对 52+ 种属性的细粒度连续控制，并支持多属性组合和未见属性的零样本操控。

**[Ani3Dhuman Photorealistic 3D Human Animation With Self-Guided Stochastic Samplin](ani3dhuman_photorealistic_3d_human_animation_with_self-guided_stochastic_samplin.md)**

:   提出 Ani3DHuman 框架，将运动学驱动的网格动画与视频扩散先验相结合，通过自引导随机采样（Self-guided Stochastic Sampling）将低质量的刚体渲染恢复为高保真视频，从而实现逼真的非刚体服装动态建模。

**[AS-Bridge: A Bidirectional Generative Framework Bridging Next-Generation Astronomical Surveys](as-bridge_a_bidirectional_generative_framework_bridging_next-generation_astronom.md)**

:   提出 AS-Bridge，一个基于 Brownian Bridge 扩散过程的双向生成框架，在地基 LSST 与空基 Euclid 天文巡天之间建模概率条件分布，实现跨巡天图像翻译和罕见事件检测（引力透镜），并通过 $\epsilon$-prediction 训练目标改进了标准 Brownian Bridge 的似然估计。

**[AS-Bridge: A Bidirectional Generative Framework Bridging Next-Generation Astronomical Surveys](asbridge_a_bidirectional_generative_framework_brid.md)**

:   提出 AS-Bridge，基于双向 Brownian Bridge 扩散过程建模地面巡天（LSST）与空间巡天（Euclid）观测之间的随机映射，同时实现跨巡天图像转换和稀有天文事件检测。

**[Attribution as Retrieval: Model-Agnostic AI-Generated Image Attribution](attribution_as_retrieval_model-agnostic_ai-generated_image_attribution.md)**

:   将 AI 生成图像归因从分类范式转为实例检索范式，提出 LIDA 框架：利用 RGB 低位平面提取生成器特有指纹作为输入，通过在真实图像上无监督预训练 + 少样本适配实现开放集归因，在 GenImage 和 WildFake 上以 1-shot 设置即取得 40.4%/77.5% 的平均 Rank-1 准确率，大幅超越现有方法。

**[Attribution as Retrieval: Model-Agnostic AI-Generated Image Attribution](attribution_as_retrieval_modelagnostic_aigenerated.md)**

:   将 AI 生成图像归因从分类范式重新定义为实例检索问题，提出 LIDA 框架：利用低位平面提取生成器指纹，通过无监督预训练 + 少样本适配实现开放集归因，在 GenImage 和 WildFake 上全面超越现有方法。

**[AutoDebias: An Automated Framework for Detecting and Mitigating Backdoor Biases in Text-to-Image Models](autodebias_automated_framework_for_debiasing_text-to-image_models.md)**

:   提出 AutoDebias——首个同时检测和缓解 T2I 模型中恶意后门偏见的统一框架，利用 VLM 开放集检测发现触发词-偏见关联并构建查找表，再通过 CLIP 引导的分布对齐训练消除后门关联，在 17 种后门场景中将攻击成功率从 90% 降至接近 0 且保持图像质量。

**[BiGain: Unified Token Compression for Joint Generation and Classification](bigain_token_compression.md)**

:   提出BiGain——一个训练免的token压缩框架，通过频域分离（保留高频细节+低中频语义），在扩散模型加速时同时保持生成质量和分类能力。70% token合并下分类精度+7.15%且FID反而更好。

**[Bigain Unified Token Compression For Joint Generation And Classification](bigain_unified_token_compression_for_joint_generation_and_classification.md)**

:   BiGain 提出频率感知的 token 压缩框架，通过拉普拉斯门控 token 合并和插值-外推 KV 下采样两个无训练算子，首次在扩散模型加速中同时保持生成质量并显著提升判别分类性能。

**[Bimotion B-Spline Motion For Text-Guided Dynamic 3D Character Generation](bimotion_b-spline_motion_for_text-guided_dynamic_3d_character_generation.md)**

:   提出 BiMotion，用连续可微的 B 样条曲线将变长运动序列压缩为固定数量控制点，配合专用 VAE 和 flow-matching 扩散模型，实现快速、高表达力、语义完整的文本引导动态 3D 角色生成，在质量和效率上均超越现有方法。

**[Blackmirror Black-Box Backdoor Detection For Text-To-Image Models Via Instructio](blackmirror_black-box_backdoor_detection_for_text-to-image_models_via_instructio.md)**

:   提出 BlackMirror 框架，通过细粒度的指令-响应语义偏差检测（MirrorMatch）和跨 prompt 稳定性验证（MirrorVerify）两阶段流程，在黑盒条件下实现对 T2I 模型多种后门攻击的通用检测，F1 平均达 89.46%，大幅超越已有黑盒方法 UFID。

**[CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing](care-edit_condition-aware_routing_of_experts_for_contextual_image_editing.md)**

:   提出 CARE-Edit，一种条件感知的专家路由框架，通过异构专家（Text/Mask/Reference/Base）配合轻量级 latent-attention 路由器，在 DiT 骨干上实现动态计算分配，有效解决统一图像编辑器中多条件信号（文本、掩码、参考图）冲突导致的颜色溢出、身份漂移等问题。

**[CaReFlow: Cyclic Adaptive Rectified Flow for Multimodal Fusion](careflow_cyclic_adaptive_rectified_flow_for_multimodal_fusion.md)**

:   提出 CaReFlow，首次将 rectified flow 用于多模态分布映射以缩小模态间隙：通过 one-to-many mapping 让源模态数据点观测目标模态全局分布，adaptive relaxed alignment 对不同关联度的模态对施加不同对齐强度，cyclic rectified flow 保证映射后信息不丢失，即使用简单拼接融合也能在多个多模态情感计算 benchmark 上达到 SOTA。

**[Causal Motion Diffusion Models for Autoregressive Motion Generation](causal_motion_diffusion_models_for_autoregressive_motion_generation.md)**

:   提出 CMDM 框架，在运动-语言对齐的因果隐空间中统一扩散去噪与自回归生成，通过帧级独立噪声和因果不确定性采样调度，实现高质量、低延迟的文本到动作生成和长序列流式合成。

**[CDG: Guiding Diffusion Models with Semantically Degraded Conditions](cdg_condition_degradation_guidance_diffusion.md)**

:   提出CDG替代CFG——用语义退化条件替代空null prompt作为负面引导，将引导信号从粗粒度"好vs空"变为精细"好vs差一点"，在SD3/FLUX/Qwen-Image上显著提升组合精度，零额外计算。

**[CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance](cfg-ctrl_control-based_classifier-free_diffusion_guidance.md)**

:   将 Classifier-Free Guidance (CFG) 重新解释为流匹配扩散模型中的反馈控制过程，提出统一框架 CFG-Ctrl，并基于滑模控制 (SMC) 设计非线性反馈引导机制 SMC-CFG，在大引导尺度下显著提升语义一致性和生成鲁棒性。

**[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](chain_of_event-centric_causal_thought_for_physically_plausible_video_generation.md)**

:   将物理现象建模为因果连接的事件序列，通过物理公式驱动的事件链推理分解复杂物理过程，再用渐进式语义-视觉双提示引导现成视频扩散模型生成物理合理的因果演进视频。

**[Chordedit One-Step Low-Energy Transport For Image Editing](chordedit_one-step_low-energy_transport_for_image_editing.md)**

:   基于动态最优传输理论，推导出低能量的 Chord 控制场，将不稳定的朴素编辑场平滑化，首次实现了对蒸馏单步 T2I 模型的无训练、无反演、高保真实时图像编辑。

**[CoD: A Diffusion Foundation Model for Image Compression](cod_a_diffusion_foundation_model_for_image_compression.md)**

:   提出首个面向压缩的扩散基础模型 CoD，从零训练学习端到端的压缩-生成联合优化，替换 Stable Diffusion 后在下游扩散编解码器中实现超低码率（0.0039 bpp）下的 SOTA 性能，训练成本仅为 SD 的 0.3%。

**[coDrawAgents: A Multi-Agent Dialogue Framework for Compositional Image Generation](codrawagents_a_multi-agent_dialogue_framework_for_compositional_image_generation.md)**

:   提出 coDrawAgents，一个交互式多智能体对话框架（Interpreter-Planner-Checker-Painter），通过分而治之的增量布局规划、视觉上下文驱动的空间推理和显式错误纠正机制，大幅提升复杂场景下组合式文本到图像生成的忠实度。

**[coDrawAgents: A Multi-Agent Dialogue Framework for Compositional Image Generation](codrawagents_a_multiagent_dialogue_framework_for_c.md)**

:   提出 coDrawAgents 交互式多智能体对话框架，通过解释器、规划器、检查器、画家四个专业智能体的闭环协作，以分治策略逐步规划布局并基于画布视觉上下文纠错，在 GenEval 上达到 0.94 的 SOTA 组合保真度。

**[CoLoGen: Progressive Learning of Concept-Localization Duality for Unified Image Generation](cologen_progressive_learning_of_concept-localization_duality_for_unified_image_g.md)**

:   提出 CoLoGen，一个基于"概念-定位对偶性"（Concept-Localization Duality）的统一图像生成框架，通过渐进式分阶段训练和 Progressive Representation Weaving（PRW）动态专家路由架构，在指令编辑、可控生成和个性化生成三大任务上同时达到或超越专用模型水平。

**[ConsistCompose: Unified Multimodal Layout Control for Image Composition](consistcompose_multimodal_layout_control.md)**

:   提出 ConsistCompose，通过将布局坐标直接嵌入语言prompt（LELG范式），在统一多模态框架中实现布局可控的多实例图像生成；构建340万样本的ConsistCompose3M数据集提供布局+身份监督；配合坐标感知CFG机制，在COCO-Position上实现布局IoU 7.2%提升和AP 13.7%提升，同时保持通用理解能力。

**[Consistcompose Unified Multimodal Layout Control For Image Composition](consistcompose_unified_multimodal_layout_control_for_image_composition.md)**

:   提出 LELG（语言嵌入式布局引导生成）范式，将 bounding box 坐标直接编码为文本 token 嵌入语言流，在统一多模态 Transformer 中实现布局可控的多实例图像生成，无需任何布局专用编码器或分支。

**[COT-FM: Cluster-wise Optimal Transport Flow Matching](cot-fm_cluster-wise_optimal_transport_flow_matching.md)**

:   提出 COT-FM，一个即插即用的 Flow Matching 增强框架：通过聚类目标样本、反转预训练模型获取簇级源分布、在簇内近似最优传输，显著拉直传输路径，在不改变模型架构的前提下同时加速采样和提升生成质量。

**[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](cubecomposer_spatio-temporal_autoregressive_4k_360_video_generation_from_perspec.md)**

:   提出 CubeComposer，将360°视频分解为 cubemap 六面表示并按时空自回归方式逐面生成，首次实现从透视视频原生生成4K（3840×1920）分辨率的360°全景视频，无需后处理超分辨率。

**[Cycle-Consistent Tuning for Layered Image Decomposition](cycle-consistent_tuning_for_layered_image_decomposition.md)**

:   提出基于扩散模型的循环一致性微调框架，通过联合训练分解模型和合成模型实现图像层分离（如logo-物体分解），并引入渐进式自改进数据扩增策略，在非线性层交互场景下实现鲁棒分解。

**[D2C: Accelerating Diffusion Model Training under Minimal Budgets via Condensation](d2c_diffusion_dataset_condensation.md)**

:   首次将数据集压缩(Dataset Condensation)应用于扩散模型训练，提出D2C两阶段框架——Select阶段用扩散难度分数+区间采样选出紧凑子集、Attach阶段为每个样本附加文本和视觉表示——仅用0.8% ImageNet(10K图像)在40K步即达FID 4.3,比REPA快100×、比vanilla SiT快233×。

**[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](denoising_as_path_planning_training-free_acceleration_of_diffusion_models_with_d.md)**

:   将扩散模型采样加速形式化为全局路径规划问题，构建路径感知代价张量（PACT）量化跳步误差的路径依赖性，通过动态规划选择最优关键步序列，在FLUX上以4.87×加速超越全步基线+0.028 ImageReward。

**[Diffusion Probe: Generated Image Result Prediction Using CNN Probes](diffusion_probe_generated_image_result_prediction_using_cnn_probes.md)**

:   发现扩散模型早期去噪步骤的交叉注意力分布与最终图像质量高度相关，提出 Diffusion Probe——用轻量CNN从早期注意力图预测生成结果质量，实现在完成10%去噪即可预筛选低质量生成路径，加速 Prompt 优化、Seed 选择和 GRPO 训练。

**[DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](diflowdubber_discrete_flow_matching_for_automated_video_dubbing_via_cross-modal_.md)**

:   提出DiFlowDubber，基于**离散流匹配(DFM)**的自动视频配音框架，通过两阶段训练（零样本TTS预训练→视频配音适配）将大规模TTS知识迁移到视频驱动配音，设计FaPro模块捕获面部表情-韵律映射、Synchronizer模块实现精准唇音同步。

**[Diversity over Uniformity: Rethinking Representation in Generated Image Detection](diversity_over_uniformity_rethinking_representation_in_generated_image_detection.md)**

:   提出反特征坍塌学习框架 AFCL，通过信息瓶颈过滤无关特征并抑制不同伪造线索之间的过度重叠，保持判别表征的多样性和互补性，在跨模型生成图像检测上取得显著提升。

**[DPCache: 去噪即路径规划——免训练扩散模型加速](dpcache_denoising_path_planning_diffusion_accel.md)**

:   将扩散采样加速形式化为全局路径规划问题，通过Path-Aware Cost Tensor量化路径依赖的跳步误差，用动态规划选出最优关键时间步序列，在FLUX上实现4.87×加速且ImageReward反超全步基线。

**[EffectErase: Joint Video Object Removal and Insertion for High-Quality Effect Erasing](effecterase_joint_video_object_removal_and_insertion_for_high-quality_effect_era.md)**

:   提出 EffectErase 框架，将视频物体插入作为移除的逆辅助任务进行联合学习，并构建包含 60K 视频对的大规模 VOR 数据集，实现对物体及其遮挡、阴影、反射、光照、变形等视觉副效应的高质量擦除。

**[Enhancing Image Aesthetics with Dual-Conditioned Diffusion Models Guided by Multimodal Perception](enhancing_image_aesthetics_with_dual-conditioned_diffusion_models_guided_by_mult.md)**

:   提出 DIAE 框架，通过多模态美学感知（MAP）将模糊的美学指令转化为 HSV/轮廓图视觉信号 + 文本联合引导，并构建"不完美配对"数据集 IIAEData 实现弱监督的图像美学增强。

**[DIAE: Enhancing Image Aesthetics with Dual-Conditioned Diffusion Models Guided by Multimodal Perception](enhancing_image_aesthetics_with_dualconditioned_di.md)**

:   提出DIAE——一个基于SD1.5的图像美学增强框架，通过多模态美学感知(MAP)将模糊的美学指令转化为HSV+轮廓图的视觉控制信号，配合"不完美配对"数据集IIAEData和双分支监督训练策略，在美学提升(LAION score +17.4%)和内容一致性(CLIP-I 0.784)上同时优于InstructPix2Pix等SOTA编辑方法。

**[Enhancing Spatial Understanding in Image Generation via Reward Modeling](enhancing_spatial_understanding_in_image_generation_via_reward_modeling.md)**

:   构建 80K 对抗性偏好数据集 SpatialReward-Dataset，训练专门评估空间关系准确性的奖励模型 SpatialScore（准确率超越 GPT-5），并用 top-k 过滤策略结合 GRPO 在线 RL 显著提升 FLUX.1-dev 的空间生成能力。

**[Evatok Adaptive Length Video Tokenization For Efficient Visual Autoregressive Ge](evatok_adaptive_length_video_tokenization_for_efficient_visual_autoregressive_ge.md)**

:   提出 EVATok 四阶段框架，通过代理奖励（proxy reward）定义最优 token 分配，训练轻量路由器预测每段视频的最优 token 预算，实现内容自适应的可变长度视频 tokenization，在 UCF-101 上达到 SOTA 生成质量的同时节省至少 24.4% 的 token 用量。

**[ExpPortrait: Expressive Portrait Generation via Personalized Representation](expportrait_expressive_portrait_generation_via_personalized_representation.md)**

:   提出高保真度的个性化头部表征（静态身份偏移 + 动态表情偏移），解决 SMPL-X 等参数化模型表达力不足的问题，结合身份自适应表情迁移模块和 DiT 生成器，在人像视频自驱动和跨身份重演任务上取得 SOTA 表现。

**[Face2Scene: Using Facial Degradation as an Oracle for Diffusion-Based Scene Restoration](face2scene_using_facial_degradation_as_an_oracle_for_diffusion-based_scene_resto.md)**

:   提出 Face2Scene 两阶段框架：先用参考人脸复原模型(Ref-FR)获得 HQ-LQ 人脸对，从中提取退化编码作为"oracle"，再以此条件化单步扩散模型完成包含身体与背景的全场景图像复原。

**[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](fastlightgen_fast_and_light_video_generation_with_fewer_steps_and_parameters.md)**

:   FastLightGen 提出三阶段蒸馏算法，首次实现采样步数与模型大小的联合蒸馏，通过识别冗余层、动态概率剪枝和 well-guided teacher guidance 分布匹配，将 HunyuanVideo/WanX 压缩为 4 步 30% 参数剪枝的轻量生成器，实现约 35 倍加速且性能超越教师模型。

**[Few-shot Acoustic Synthesis with Multimodal Flow Matching](few-shot_acoustic_synthesis_with_multimodal_flow_matching.md)**

:   提出 FLAC，首个基于 flow matching 的少样本房间脉冲响应（RIR）生成框架，仅凭单次录音即可在未见场景中合成空间一致的声学响应，并引入 AGREE 联合嵌入用于几何-声学一致性评估。

**[Flash-Unified: Training-Free and Task-Aware Acceleration for Native Unified Models](flash-unified_a_training-free_and_task-aware_acceleration_framework_for_native_u.md)**

:   FlashU 首次对原生统一多模态模型进行系统性冗余分析，发现参数特化和计算异质性现象，据此提出免训练任务感知加速框架，通过 FFN 剪枝、动态层跳过、自适应引导缩放和扩散头缓存，在 Show-o2 上实现 1.78x-2.01x 加速同时保持 SOTA 性能。

**[Garments2Look: A Multi-Reference Dataset for High-Fidelity Outfit-Level Virtual Try-On with Clothing and Accessories](garments2look_a_multi-reference_dataset_for_high-fidelity_outfit-level_virtual_t.md)**

:   提出 Garments2Look，首个大规模多模态整套搭配级虚拟试穿数据集（80K 对，40 类，300+ 子类），每组包含 3-12 件参考服饰图、模特穿搭图和详细文本标注，揭示现有方法在多层搭配和配饰一致性上的重大不足。

**[gQIR: Generative Quanta Image Reconstruction](gqir_generative_quanta_image_reconstruc_tion.md)**

:   将大规模 text-to-image latent diffusion model 适配到单光子雪崩二极管（SPAD）的极端光子受限成像场景，通过三阶段框架（Quanta-aligned VAE → 对抗微调 LoRA U-Net → FusionViT 时空融合）实现从稀疏二值光子检测到高质量 RGB 图像的重建，在 10K-100K fps 极端条件下显著超越所有现有方法。

**[Guiding Diffusion Models with Semantically Degraded Conditions](guiding_diffusion_models_with_semantically_degraded_conditions.md)**

:   提出 Condition-Degradation Guidance (CDG)，用语义退化的条件 $\boldsymbol{c}_{\text{deg}}$ 替代 CFG 中的空提示 $\emptyset$，将引导从粗粒度"好 vs. 空"转变为细粒度"好 vs. 差一点"的对比，通过分层退化策略（先退化内容 token 再退化上下文聚合 token）构建自适应负样本，在 SD3/FLUX/Qwen-Image 等模型上即插即用地提升组合生成精度，几乎零额外开销。

**[Heterogeneous Decentralized Diffusion Models](heterogeneous_decentralized_diffusion_models.md)**

:   提出异构去中心化扩散框架，允许不同专家使用不同扩散目标（DDPM ε-prediction 与 Flow Matching velocity-prediction）完全独立训练，在推理时通过确定性 schedule-aware 转换统一到速度空间进行融合，相比同构基线同时提升 FID 和生成多样性，并将计算量压缩 16 倍。

**[HiFi-Inpaint: Towards High-Fidelity Reference-Based Inpainting for Generating Detail-Preserving Human-Product Images](hifi-inpaint_towards_high-fidelity_reference-based_inpainting_for_generating_det.md)**

:   提出 HiFi-Inpaint 框架，通过共享增强注意力（SEA）利用高频信息增强产品细节特征，结合细节感知损失（DAL）实现像素级高频监督，在人-产品图像生成中达到 SOTA 的细节保真度。

**[High-Fidelity Diffusion Face Swapping with ID-Constrained Facial Conditioning](high-fidelity_diffusion_face_swapping_with_id-constrained_facial_conditioning.md)**

:   提出身份约束的属性调优框架用于扩散模型人脸替换：先约束身份解空间，再注入属性条件，最后端到端精炼身份损失和对抗损失，结合解耦条件注入设计，在 FFHQ 上实现 SOTA 的 FID（3.61）和身份检索准确率（97.9% Top-1）。

**[Image Generation as a Visual Planner for Robotic Manipulation](image_generation_as_a_visual_planner_for_robotic_manipulation.md)**

:   将预训练图像生成模型（DiT）通过 LoRA 微调适配为机器人操作的视觉规划器，以 3×3 网格图像形式生成时序连贯的操作序列，支持文本条件和轨迹条件两种控制模式。

**[Improving Text-to-Image Generation with Intrinsic Self-Confidence Rewards](improving_text-to-image_generation_with_intrinsic_self-confidence_rewards.md)**

:   提出 SOLACE，一种利用文本-图像生成模型自身去噪自信度作为内在奖励的后训练框架，无需外部奖励模型即可在组合生成、文字渲染和文图对齐上获得一致提升，且可与外部奖励互补缓解 reward hacking。

**[Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout](infinity-rope_action-controllable_infinite_video_generation_emerges_from_autoreg.md)**

:   提出 ∞-RoPE，一个训练免调的推理时框架，通过 Block-Relativistic RoPE、KV Flush 和 RoPE Cut 三个组件，将仅在5秒视频上训练的自回归视频扩散模型扩展为支持无限时长生成、精细动作控制和电影级场景切换的系统。

**[InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation](innoads-composer_efficient_condition_composition_for_e-commerce_poster_generatio.md)**

:   提出 InnoAds-Composer，一个基于 MM-DiT 的单阶段电商海报生成框架，通过统一 token 化将商品主体、字形文本和背景风格三类条件映射到同一空间，结合文本特征增强模块（TFEM）和重要性感知条件注入策略，在保持高质量生成的同时显著降低推理开销。

**[InterEdit: Navigating Text-Guided Multi-Human 3D Motion Editing](interedit_navigating_text-guided_multi-human_3d_motion_editing.md)**

:   提出 InterEdit，首个文本引导的多人3D运动编辑框架，通过语义感知 Plan Token 对齐和交互感知频域 Token 对齐两个机制，在条件扩散模型中实现对双人交互动作的精准编辑，同时保持源运动的一致性和交互协调性。

**[InterEdit: Navigating Text-Guided Multi-Human 3D Motion Editing](interedit_navigating_textguided_multihuman_3d_moti.md)**

:   首次定义多人3D运动编辑(TMME)任务，构建5161个源-目标-指令三元组的InterEdit3D数据集，提出基于同步无分类器引导的条件扩散模型InterEdit，通过语义感知规划Token对齐和交互感知频域Token对齐两个核心模块，在指令跟随(g2t R@1 30.82%)和源保持(g2s R@1 17.08%)上全面超越基线。

**[Intrinsic Concept Extraction Based on Compositional Interpretability](intrinsic_concept_extraction_based_on_compositional_interpretability.md)**

:   HyperExpress 提出组合可解释本征概念提取（CI-ICE）新任务，利用双曲空间的层次建模能力和等球面投影模块，从单张图像中提取可组合的物体级和属性级概念，实现可逆的复杂视觉概念分解。

**[InvAD: Inversion-based Reconstruction-Free Anomaly Detection with Diffusion Models](invad_inversion-based_reconstruction-free_anomaly_detection_with_diffusion_model.md)**

:   提出 InvAD，将扩散模型异常检测从"RGB 空间去噪重建"范式转变为"潜空间加噪反演"范式，通过 DDIM 反演直接推断最终潜变量并在先验分布下度量偏差来检测异常，仅需 3 步反演即达 SOTA 性能且推理速度提升约 2 倍。

**[InvAD: Inversion-based Reconstruction-Free Anomaly Detection with Diffusion Models](invad_inversionbased_reconstructionfree_anomaly_de.md)**

:   提出"检测即加噪"范式取代传统"检测即去噪"——通过DDIM反转将图像映射到潜在噪声空间，仅用3步推理判断偏离先验分布的程度作为异常分数，无需重建，实现SOTA精度的同时推理速度达88 FPS（比OmiAD快2倍+）。

**[Learning Latent Proxies for Controllable Single-Image Relighting](learning_latent_proxies_for_controllable_single-image_relighting.md)**

:   提出 LightCtrl，一个基于扩散模型的单图重光照框架，通过小样本潜在代理编码器（few-shot latent proxy）提供轻量材质-几何先验、光照感知掩码引导空间选择性去噪、DPO 后训练增强物理一致性，实现对光照方向/强度/色温的精确连续控制，在合成和真实场景上均优于现有方法。

**[Learning Latent Transmission and Glare Maps for Lens Veiling Glare Removal](learning_latent_transmission_and_glare_maps_for_lens_veiling_glare_removal.md)**

:   提出 VeilGen + DeVeiler 框架，通过物理引导的 Stable Diffusion 生成模型学习潜在透射率和眩光图以合成逼真的复合退化训练数据，并用可逆约束训练修复网络，实现简化光学系统中像差与雾化眩光的联合去除。

**[LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation](linvideo_linear_attention_video_generation.md)**

:   首个data-free后训练框架LinVideo，通过选择性转移自动选择最适合替换为线性注意力的层+任意时刻分布匹配(ADM)目标函数高效恢复性能，实现Wan 1.3B/14B的1.43-1.71×加速且质量无损，叠加4步蒸馏后达15.9-20.9×加速。

**[Mitigating Memorization in Text-to-Image Diffusion via Region-Aware Prompt Augmentation and Multimodal Copy Detection](mitigating_memorization_in_text-to-image_diffusion_via_region-aware_prompt_augme.md)**

:   提出 RAPTA（训练时区域感知提示增强）缓解扩散模型记忆化，以及 ADMCD（注意力驱动多模态拷贝检测）检测生成图像是否复制训练数据，两个模块互补形成端到端的记忆化缓解与检测框架。

**[Mitigating Memorization in Text-to-Image Diffusion via Region-Aware Prompt Augmentation and Multimodal Copy Detection](mitigating_memorization_in_texttoimage_diffusion_v.md)**

:   提出训练时区域感知提示增强(RAPTA)和注意力驱动多模态复制检测(ADMCD)两个互补模块，前者通过检测器proposal生成语义接地的提示变体来缓解扩散模型的训练数据记忆化，后者融合patch/CLIP/纹理三流特征实现零训练复制检测，在LAION-10k上将复制率从7.4降至2.6。

**[Mixture Of States Routing Token-Level Dynamics For Multimodal Generation](mixture_of_states_routing_token-level_dynamics_for_multimodal_generation.md)**

:   提出 Mixture of States (MoS)——一种基于可学习 token 级稀疏路由的多模态融合范式，使视觉 token 能在每个去噪步骤自适应地从文本编码器任意层选取隐藏状态，仅用 3-5B 参数即可匹敌或超越 20B 级模型。

**[One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers](one_model_many_budgets_elastic_latent_interfaces_f.md)**

:   提出ELIT（Elastic Latent Interface Transformer），通过在DiT中插入可变长度的潜在token接口和轻量级Read/Write交叉注意力层，将计算量与输入分辨率解耦，使单一模型支持多种推理预算，在ImageNet-1K 512px上FID和FDD分别提升35.3%和39.6%。

**[One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers](one_model_many_budgets_elastic_latent_interfaces_for_diffusion_transformers.md)**

:   提出 ELIT（Elastic Latent Interface Transformer），在 DiT 中插入可变长度的潜变量接口（latent interface）和轻量 Read/Write 跨注意力层，使单一模型能在推理时动态调节计算预算，同时将计算非均匀地分配到图像中更难的区域，在 ImageNet 512px 上 FID 最高降低 53%。

**[Pixel Motion Diffusion Is What We Need for Robot Control](pixel_motion_diffusion_is_what_we_need_for_robot_control.md)**

:   DAWN 提出两阶段全扩散框架，通过 Motion Director 生成稠密像素运动场作为可解释中间表征，再由 Action Expert 转化为机器人动作序列，在 CALVIN 基准上实现 SOTA（平均长度 4.00）且数据效率极高。

**[PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](pixelrush_ultrafast_trainingfree_highresolution_im.md)**

:   PixelRush 首次实现了免训练的单步高分辨率图像生成，通过部分 DDIM 反转（只扰动到中间时间步而非全噪声）+ 少步扩散模型 + 高斯滤波 patch 融合 + 噪声注入，在单卡 A100 上 20 秒生成 4K 图像，比 SOTA 快 10-35× 且 FID 更优（50.13 vs 52.87）。

**[PROMO: Promptable Outfitting for Efficient High-Fidelity Virtual Try-On](promo_promptable_virtual_tryon_efficient.md)**

:   PROMO基于FLUX Flow Matching DiT骨干，通过潜空间多模态条件拼接、时序自参考KV缓存、3D-RoPE分组条件、以及fine-tuned VLM风格提示系统，在去除传统参考网络的前提下实现了高保真且高效的多件服装虚拟试穿，推理速度比无加速版快2.4倍，在VITON-HD和DressCode上超越现有VTON和通用图像编辑方法。

**[RAZOR: Ratio-Aware Layer Editing for Targeted Unlearning in Vision Transformers and Diffusion Models](razor_ratio_aware_unlearning_vit_diffusion.md)**

:   提出 RAZOR, 一种基于比率感知梯度评分的多层协调编辑方法, 用于 ViT 和扩散模型的目标遗忘: 通过 forget/retain 梯度的比率和余弦对齐度联合评分, 识别对遗忘贡献最大且对保留损害最小的层/头, 实现一次性高效遗忘, 在 CLIP 身份遗忘上达到 SOTA.

**[Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning](refining_few-step_text-to-multiview_diffusion_via_reinforcement_learning.md)**

:   提出 MVC-ZigAL 框架，通过多视图感知 MDP 建模、zigzag 自反思优势学习和 Lagrangian 对偶约束优化，有效提升少步文本到多视图扩散模型的单视图保真度和跨视图一致性。

**[Seacache Spectral-Evolution-Aware Cache For Accelerating Diffusion Models](seacache_spectral-evolution-aware_cache_for_accelerating_diffusion_models.md)**

:   提出 SeaCache，一种基于频谱演化感知（SEA）滤波器的无训练动态缓存策略，通过在频域中分离信号与噪声分量来测量时间步间的冗余度，显著提升扩散模型推理的延迟-质量权衡。

**[SegQuant: A Semantics-Aware and Generalizable Quantization Framework for Diffusion Models](segquant_diffusion_model_quantization.md)**

:   提出 SegQuant，一个面向部署的扩散模型后训练量化框架，通过基于计算图静态分析的语义感知分段量化（SegLinear）和硬件原生的双尺度极性保持量化（DualScale），在 SD3.5、FLUX、SDXL 上实现跨架构通用的高保真 W8A8/W4A8 量化，同时保持与 TensorRT 等工业推理引擎的兼容性。

**[SOLACE: Improving Text-to-Image Generation with Intrinsic Self-Confidence Rewards](solace_self_confidence_rewards_t2i.md)**

:   用T2I模型自身的去噪自信心（对注入噪声的恢复精度）作为内在奖励替代外部奖励模型做后训练，在组合生成、文字渲染、文图对齐上获一致提升，且与外部奖励互补可缓解reward hacking。

**[Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework](taming_score-based_denoisers_in_admm_a_convergent_plug-and-play_framework.md)**

:   提出 AC-DC 三阶段去噪器（自动校正 + 方向校正 + Score 去噪），解决 ADMM 迭代与 score 训练流形不匹配的问题，并首次为 ADMM-PnP + score denoiser 建立了收敛性保证，在多种逆问题上取得 SOTA。

**[Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework](taming_scorebased_denoisers_in_admm_a_convergent_p.md)**

:   提出ADMM-PnP with AC-DC去噪器，通过三阶段修正-去噪流程(自动修正+方向修正+基于分数的去噪)将扩散先验集成到ADMM原始-对偶框架中，解决了ADMM迭代与扩散训练流形的几何不匹配问题，同时在两种条件下建立了收敛保证，在7种逆问题上一致优于DAPS/DPS/DiffPIR等基线。
