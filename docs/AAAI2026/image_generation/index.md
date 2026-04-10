<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**🤖 AAAI2026** · 共 **43** 篇

**[AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs](abductivemllm_boosting_visual_abductive_reasoning_within_mll.md)**

:   模仿人类的"语言溯因+图像想象"双模式认知，提出AbductiveMLLM，通过Reasoner(因果感知假设生成+筛选)和Imaginer(扩散模型引导的图像想象)两个组件端到端联合训练，在VAR和YouCookII两个benchmark上显著超越传统方法和通用MLLM，设置新的SOTA。

**[AEDR: Training-Free AI-Generated Image Attribution via Autoencoder Double-Reconstruction](aedr_training-free_ai-generated_image_attribution_via_autoen.md)**

:   提出一种基于自编码器双重重建损失比值的免训练图像归因方法，通过图像均匀度校准消除纹理复杂度偏差，在8个主流扩散模型上平均准确率达95.1%，比最强基线高24.7%，且速度快约100倍。

**[Aggregating Diverse Cue Experts for AI-Generated Image Detection](aggregating_diverse_cue_experts_for_ai-generated_image_detec.md)**

:   提出Multi-Cue Aggregation Network (MCAN)，通过混合编码器适配器(MoEA)将原始图像、高频信息和新提出的色度不一致性(CI)三种互补线索统一融合，实现跨生成模型的鲁棒AI生成图像检测。

**[Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation](annealed_relaxation_of_speculative_decoding_for_faster_autor.md)**

:   提出Cool-SD，一种有理论支撑的退火松弛speculative decoding框架：通过推导TV距离上界得到最优重采样分布，并证明接受概率递减调度比均匀调度产生更小的分布偏移，在LlamaGen和Lumina-mGPT上实现了比LANTERN++更优的速度-质量权衡。

**[AnoStyler: Text-Driven Localized Anomaly Generation via Lightweight Style Transfer](anostyler_text-driven_localized_anomaly_generation_via_light.md)**

:   将零样本异常生成建模为文本引导的局部风格迁移问题，通过轻量级U-Net + CLIP损失将正常图像的掩码区域风格化为语义对齐的异常图像，在MVTec-AD和VisA上以263M参数（仅0.61M可训练）超越扩散模型基线，同时显著提升下游异常检测性能。

**[Backdoors in Conditional Diffusion: Threats to Responsible Synthetic Data Pipelines](backdoors_in_conditional_diffusion_threats_to_responsible_synthetic_data_pipelin.md)**

:   揭示了 ControlNet 条件分支的后门攻击漏洞：仅需 1–5% 的投毒数据即可在不修改扩散主干的前提下植入后门，触发时无视文本 prompt 生成攻击者指定内容，并提出 clean fine-tuning (CFT) 作为实用防御。

**[Beautiful Images, Toxic Words: Understanding and Addressing Offensive Text in Generated Images](beautiful_images_toxic_words_understanding_and_addressing_offensive_text_in_gene.md)**

:   揭示扩散模型在生成图像中嵌入 NSFW 文字的新威胁，提出基于文本生成层定向 LoRA 微调的 NSFW-Intervention 方法，并发布 ToxicBench 基准。

**[Breaking the Modality Barrier: Generative Modeling for Accurate Molecule Retrieval from Mass Spectra](breaking_the_modality_barrier_generative_modeling_for_accurate_molecule_retrieva.md)**

:   提出 GLMR 两阶段框架（对比学习预检索 + 生成式语言模型重排），通过生成与输入质谱对齐的分子结构将跨模态检索转化为单模态检索，在 MassSpecGym 上 Recall@1 提升超 40%。

**[CAD-VAE: Leveraging Correlation-Aware Latents for Comprehensive Fair Disentanglement](cad-vae_leveraging_correlation-aware_latents_for_comprehensive_fair_disentanglem.md)**

:   提出CAD-VAE，引入"相关隐变量" $z_R$ 显式建模目标属性和敏感属性之间的共享信息，通过最小化条件互信息 $I(z_Y;z_S|z_R)$ 实现公平解缠绕，无需领域知识即可产生公平表示和高质量反事实样本。

**[CausalCLIP: Causally-Informed Feature Disentanglement and Filtering for Generalizable Detection of Generated Images](causalclip_causally-informed_feature_disentanglement_and_filtering_for_generaliz.md)**

:   提出 CausalCLIP，通过 Gumbel-Softmax 掩码 + HSIC 约束将 CLIP 特征解耦为因果/非因果子空间，结合对抗掩码和反事实干预保留稳定取证线索，跨生成器泛化准确率提升 6.83%。

**[Conditional Diffusion Model for Multi-Agent Dynamic Task Decomposition](conditional_diffusion_model_for_multi-agent_dynamic_task_dec.md)**

:   提出 CD3T，一个两层层次化 MARL 框架：用条件扩散模型学习动作语义表示（以观测和他人动作为条件，预测下一观测和奖励），通过 k-means 聚类得到子任务划分，高层选择子任务、低层在受限动作空间执行策略，在 SMAC 的 Super Hard 场景上显著超越所有基线。

**[Constrained Particle Seeking: Solving Diffusion Inverse Problems with Just Forward Passes](constrained_particle_seeking_solving_diffusion_inverse_problems_with_just_forwar.md)**

:   提出 Constrained Particle Seeking (CPS)，一种无梯度的扩散模型反问题求解方法，通过利用所有候选粒子信息构建前向过程的局部线性代理模型，并在转移核高密度区域的超球面约束下寻找最优粒子，性能可与梯度方法媲美。

**[Continuous Degradation Modeling via Latent Flow Matching for Real-World Super-Resolution](continuous_degradation_modeling_via_latent_flow_matching_for_real-world_super-re.md)**

:   提出 DegFlow，通过残差自编码器 + 潜空间 Flow Matching 从离散尺度的真实 HR-LR 对学习连续退化轨迹，仅需单张 HR 图像即可合成任意连续尺度的逼真 LR 图像，用于训练超分模型达到 SOTA。

**[Copyright Infringement Detection in Text-to-Image Diffusion Models via Differential Privacy](copyright_infringement_detection_in_text-to-image_diffusion_models_via_different.md)**

:   从差分隐私（Differential Privacy）角度形式化版权侵权的定义，提出 D-Plus-Minus（DPM）框架，通过对扩散模型分别进行"学习"和"遗忘"两个方向的微调，测量条件敏感度差异来事后检测文本到图像模型中的版权侵权行为。

**[CountSteer: Steering Attention for Object Counting in Diffusion Models](countsteer_steering_attention_for_object_counting_in_diffusion_models.md)**

:   提出 CountSteer，一种免训练的推理时方法，通过在扩散模型的 cross-attention 隐状态中注入自适应 steering vector，将物体计数准确率提升约 4%，且不损害图像质量。

**[Creating Blank Canvas Against AI-Enabled Image Forgery](creating_blank_canvas_against_ai-enabled_image_forgery.md)**

:   提出"空白画布"机制，通过对抗扰动使 SAM 对受保护图像"视而不见"，当图像被篡改后篡改区域会被 SAM 自动识别，实现无需篡改训练数据的主动式篡改定位。

**[DICE: Distilling Classifier-Free Guidance into Text Embeddings](dice_distilling_classifier-free_guidance_into_text_embedding.md)**

:   提出 DICE，训练一个仅 2M 参数的轻量 sharpener 将 CFG 的引导效果蒸馏进 text embedding，使无引导采样达到与 CFG 同等的生成质量、推理计算量减半，在 SD1.5 多个变体、SDXL 和 PixArt-α 上全面验证有效，是 AAAI 2026 口头报告论文。

**[Diff-V2M: A Hierarchical Conditional Diffusion Model with Explicit Rhythmic Modeling for Video-to-Music Generation](diff-v2m_a_hierarchical_conditional_diffusion_model_with_explicit_rhythmic_model.md)**

:   提出 Diff-V2M，一个基于层次条件扩散 Transformer 的视频到音乐生成框架，通过显式节奏建模（低分辨率 ODF）和层次交叉注意力机制整合情感/语义/节奏特征，在域内和域外数据集上均达到 SOTA。

**[DiffA: Large Language Diffusion Models Can Listen and Understand](diffa_large_language_diffusion_models_can_listen_and_understand.md)**

:   提出 DIFFA——首个基于扩散语言模型的大型音频-语言模型，通过冻结 LLaDA-8B 骨干网络 + 轻量双适配器架构 + 两阶段训练管线，仅用 960 小时 ASR 数据和 127 小时合成指令数据就在 MMSU、MMAU、VoiceBench 上达到与自回归 baseline 竞争的性能。

**[DiffBench Meets DiffAgent: End-to-End LLM-Driven Diffusion Acceleration Code Generation](diffbench_meets_diffagent_end-to-end_llm-driven_diffusion_ac.md)**

:   提出DiffBench（604个扩散模型加速任务的评估基准，分5个难度等级）和DiffAgent（集成规划-编码-调试三Agent + 遗传算法选择器的闭环框架），在Claude Sonnet 4上将扩散加速代码生成通过率从54.30%提升到81.59%，复杂优化任务达成率68.27%。

**[Difficulty Controlled Diffusion Model for Synthesizing Effective Training Data](difficulty_controlled_diffusion_model_for_synthesizing_effec.md)**

:   在Stable Diffusion中引入难度编码器（MLP，输入类别+难度分数），通过LoRA微调解耦"域对齐"和"难度控制"两个目标，使生成数据的学习难度可控——仅用10%额外合成数据即超过Real-Fake的最佳结果，节省63.4 GPU小时。

**[Diffusion Reconstruction-Based Data Likelihood Estimation for Core-Set Selection](diffusion_reconstruction-based_data_likelihood_estimation_for_core-set_selection.md)**

:   提出利用扩散模型的部分反向去噪重建偏差作为数据似然的理论近似信号，配合信息瓶颈理论选择最优重建时间步，实现分布感知的核心集选择，在 ImageNet 上仅用 50% 数据即可逼近全量训练性能。

**[DogFit: Domain-guided Fine-tuning for Efficient Transfer Learning of Diffusion Models](dogfit_domain-guided_fine-tuning_for_efficient_transfer_learning_of_diffusion_mo.md)**

:   提出 DogFit，将域引导（Domain Guidance）内化到扩散模型的微调损失中，使模型在训练时学会引导方向，推理时无需双重前向传播即可实现可控的保真度-多样性权衡，在 6 个目标域上以一半的采样 TFLOPS 超越 SOTA 引导方法。

**[DOS: Directional Object Separation in Text Embeddings for Multi-Object Image Generation](dos_directional_object_separation_in_text_embeddings_for_mul.md)**

:   识别出多物体生成失败的四种场景（相似形状/纹理、不同背景偏好、多物体），通过构建方向性分离向量修改CLIP的三类文本嵌入（语义token/EOT/pooled），在SDXL上将成功率提升16-25%并将融合率降低3-12%，推理速度接近baseline（约4×快于Attend-and-Excite）。

**[EchoGen: Cycle-Consistent Learning for Unified Layout-Image Generation and Understanding](echogen_cycle-consistent_learning_for_unified_layout-image_generation_and_unders.md)**

:   提出 EchoGen，统一布局到图像生成（L2I）和图像定位（I2L）两个任务的框架，通过渐进式训练——并行预训练→双任务联合优化→循环强化学习（CycleRL）——利用布局→图像→布局回环的一致性约束作为自监督奖励，在 MS-COCO 和 LayoutSAM 上达到 SOTA。

**[EfficientFlow: Efficient Equivariant Flow Policy Learning for Embodied AI](efficientflow_efficient_equivariant_flow_policy_learning_for_embodied_ai.md)**

:   提出 EfficientFlow，将等变性引入 Flow Matching 策略学习框架，理论证明各向同性先验+等变速度网络保证动作分布等变，并提出 Flow Acceleration Upper Bound (FABO) 正则化加速采样，在 MimicGen 12 个任务上实现比 EquiDiff 快 20-56 倍的推理速度且性能更优。

**[FGM-HD: Boosting Generation Diversity of Fractal Generative Models through Hausdorff Dimension Induction](fgm-hd_boosting_generation_diversity_of_fractal_generative_models_through_hausdo.md)**

:   本文首次将 Hausdorff 维数（HD）引入分形生成模型（FGM），提出可学习的 HD 估计模块、单调动量驱动调度策略（MMDS）和 HD 引导的拒绝采样，在 ImageNet 上实现 39% 的生成多样性提升（Recall），同时保持图像质量。

**[Flowing Backwards: Improving Normalizing Flows via Reverse Representation Alignment](flowing_backwards_improving_normalizing_flows_via_reverse_representation_alignme.md)**

:   提出 R-REPA（Reverse Representation Alignment），创造性地利用 Normalizing Flows 的可逆性，在生成（反向）路径上将中间特征与视觉基础模型对齐，同时提出免训练分类算法，在 ImageNet 64×64 和 256×256 上实现 NF 新 SOTA，训练加速 3.3 倍。

**[HACK: Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling](head-aware_kv_cache_compression_for_efficient_visual_autoreg.md)**

:   发现VAR模型中attention head天然分为Contextual Heads（语义一致性，垂直注意力模式）和Structural Heads（空间连贯性，多对角线模式），提出HACK框架通过非对称预算分配和模式特定压缩策略，在70%压缩率下实现无损生成质量，Infinity-8B上1.75×显存减少和1.57×加速。

**[Hierarchicalprune Position-Aware Compression For Large-Scale Diffusion Models](hierarchicalprune_position-aware_compression_for_large-scale_diffusion_models.md)**

:   基于 MMDiT 的双层级结构洞察（inter-block + intra-block hierarchy），提出 position-aware 的剪枝+蒸馏+量化框架，将 SD3.5 Large (8B) 从 15.8GB 压缩至 3.2GB（80% 内存降低），质量仅下降 ~5%。

**[Infinite-Story: A Training-Free Consistent Text-to-Image Generation](infinite-story_a_training-free_consistent_text-to-image_gene.md)**

:   基于 scale-wise 自回归模型（Infinity），通过三个 training-free 技术——Identity Prompt Replacement（消除文本编码器的上下文偏差）、Adaptive Style Injection（参考图像特征注入）和 Synchronized Guidance Adaptation（同步 CFG 两个分支），实现了身份与风格一致的多图像生成，速度比扩散模型快 6 倍（1.72 秒/张）。

**[Laytrol: Preserving Pretrained Knowledge in Layout Control for Multimodal Diffusion Transformers](laytrol_preserving_pretrained_knowledge_in_layout_control_fo.md)**

:   通过从 MM-DiT 复制参数初始化布局控制网络、设计专用初始化方案（布局编码器初始化为纯文本编码器 + 输出零初始化）、并用 FLUX 自己生成的图像构建 LaySyn 数据集来缓解分布偏移，实现了在 FLUX 上高质量的布局到图像生成。

**[Mass Concept Erasure in Diffusion Models with Concept Hierarchy](mass_concept_erasure_in_diffusion_models_with_concept_hierarchy.md)**

:   提出基于supertype-subtype概念层级的分组擦除策略和Supertype-Preserving LoRA (SuPLoRA)，通过冻结down-projection矩阵（正交于supertype子空间）仅训练up-projection矩阵，在大规模多领域概念擦除中实现擦除效果与生成质量的最优平衡。

**[Multi-Metric Preference Alignment For Generative Speech Restoration](multi-metric_preference_alignment_for_generative_speech_restoration.md)**

:   提出多指标偏好对齐策略（Multi-Metric Preference Alignment），通过构建要求多个互补指标一致同意的偏好数据集 GenSR-Pref（80K 对），利用 DPO 对三种生成式语音修复范式（AR、MGM、FM）进行后训练对齐，显著提升修复质量并有效缓解 reward hacking。

**[ORVIT: Near-Optimal Online Distributionally Robust Reinforcement Learning](orvit_near-optimal_online_distributionally_robust_reinforcement_learning.md)**

:   本文研究在线分布鲁棒强化学习，提出了基于 $f$-散度不确定性集的 RVI-$f$ 算法，在 $\chi^2$ 和 KL 散度下均实现了近似极小极大最优的遗憾界，且不依赖任何结构性假设。

**[SimDiff: Simpler Yet Better Diffusion Model for Time Series Point Forecasting](simdiff_simpler_yet_better_diffusion_model_for_time_series_point_forecasting.md)**

:   提出SimDiff——首个纯端到端扩散模型实现时间序列点预测SOTA，通过统一的Transformer网络同时充当去噪器和预测器，结合Normalization Independence处理分布偏移和Median-of-Means集成策略将概率采样转化为精确点预测，在9个数据集上6个第一、3个第二。

**[Stabilizing Self-Consuming Diffusion Models with Latent Space Filtering](stabilizing_self-consuming_diffusion_models_with_latent_space_filtering.md)**

:   提出Latent Space Filtering (LSF)方法，通过分析自消费扩散模型隐空间中潜在表示的低维结构退化现象，利用probing classifier的置信度分数过滤低质量合成数据，在固定训练预算下有效缓解模型坍塌，无需额外真实数据或增大训练集。

**[Structure-based RNA Design by Step-wise Optimization of Latent Diffusion Model](structure-based_rna_design_by_step-wise_optimization_of_latent_diffusion_model.md)**

:   提出SOLD框架，将潜在扩散模型（LDM）与强化学习（RL）结合，通过步进式单步采样优化策略，直接优化RNA逆折叠中不可微的结构指标（二级结构相似度SS、最小自由能MFE、LDDT），在多个指标上全面超越现有方法。

**[Studying Classifier(-Free) Guidance From A Classifier-Centric Perspective](studying_classifier-free_guidance_from_a_classifier-centric_perspective.md)**

:   通过系统实证研究揭示了classifier guidance和classifier-free guidance的本质机制——两者都通过将去噪轨迹推离分类器的决策边界来实现条件生成，并提出基于流匹配的后处理方法在高维数据上验证了这一"分类器中心"视角。

**[T2I-RiskyPrompt: A Benchmark for Safety Evaluation, Attack, and Defense on Text-to-Image Model](t2i-riskyprompt_a_benchmark_for_safety_evaluation_attack_and_defense_on_text-to-.md)**

:   构建T2I-RiskyPrompt——一个包含6,432条有效风险prompt的综合基准，涵盖6大类14细分风险类别，每条prompt带有层次化标注和详细风险原因，并提出reason-driven的MLLM风险检测方法（3B模型达91.8%准确率），系统评估了8个T2I模型、9种防御方法、5种安全过滤器和5种攻击策略。

**[Talk, Snap, Complain: Validation-Aware Multimodal Expert Framework for Fine-Grained Customer Grievances](talk_snap_complain_validation-aware_multimodal_expert_framework_for_fine-grained.md)**

:   提出VALOR框架，结合Chain-of-Thought推理的多专家路由架构与语义对齐验证机制，在多轮多模态客服对话中实现细粒度投诉方面(Aspect)和严重度(Severity)的联合分类，较最强baseline Gemma-3绝对提升12.94%/6.51%。

**[Voicecloak A Multi-Dimensional Defense Framework Against Unauthorized Diffusion-](voicecloak_a_multi-dimensional_defense_framework_against_unauthorized_diffusion-.md)**

:   针对 diffusion-based voice cloning (VC) 的主动防御框架，通过多维度对抗扰动同时实现说话人身份混淆和感知质量退化，显著优于现有防御方法。

**[X2Edit Revisiting Arbitrary-Instruction Image Editing Through Self-Constructed D](x2edit_revisiting_arbitrary-instruction_image_editing_through_self-constructed_d.md)**

:   构建 370 万高质量编辑数据集（14 类任务），并提出基于 Task-Aware MoE-LoRA + Contrastive Learning 的轻量级（0.9B 参数）plug-and-play 编辑模块，性能媲美 12B 全参数训练模型。
