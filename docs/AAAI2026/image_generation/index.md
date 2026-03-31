<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**🤖 AAAI2026** · 共 **28** 篇

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

**[DOS: Directional Object Separation in Text Embeddings for Multi-Object Image Generation](dos_directional_object_separation_in_text_embeddings_for_mul.md)**

:   识别出多物体生成失败的四种场景（相似形状/纹理、不同背景偏好、多物体），通过构建方向性分离向量修改CLIP的三类文本嵌入（语义token/EOT/pooled），在SDXL上将成功率提升16-25%并将融合率降低3-12%，推理速度接近baseline（约4×快于Attend-and-Excite）。

**[HACK: Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling](head-aware_kv_cache_compression_for_efficient_visual_autoreg.md)**

:   发现VAR模型中attention head天然分为Contextual Heads（语义一致性，垂直注意力模式）和Structural Heads（空间连贯性，多对角线模式），提出HACK框架通过非对称预算分配和模式特定压缩策略，在70%压缩率下实现无损生成质量，Infinity-8B上1.75×显存减少和1.57×加速。

**[Infinite-Story: A Training-Free Consistent Text-to-Image Generation](infinite-story_a_training-free_consistent_text-to-image_gene.md)**

:   基于 scale-wise 自回归模型（Infinity），通过三个 training-free 技术——Identity Prompt Replacement（消除文本编码器的上下文偏差）、Adaptive Style Injection（参考图像特征注入）和 Synchronized Guidance Adaptation（同步 CFG 两个分支），实现了身份与风格一致的多图像生成，速度比扩散模型快 6 倍（1.72 秒/张）。

**[Laytrol: Preserving Pretrained Knowledge in Layout Control for Multimodal Diffusion Transformers](laytrol_preserving_pretrained_knowledge_in_layout_control_fo.md)**

:   通过从 MM-DiT 复制参数初始化布局控制网络、设计专用初始化方案（布局编码器初始化为纯文本编码器 + 输出零初始化）、并用 FLUX 自己生成的图像构建 LaySyn 数据集来缓解分布偏移，实现了在 FLUX 上高质量的布局到图像生成。

**[ORVIT: Near-Optimal Online Distributionally Robust Reinforcement Learning](orvit_near-optimal_online_distributionally_robust_reinforcement_learning.md)**

:   本文研究在线分布鲁棒强化学习，提出了基于 $f$-散度不确定性集的 RVI-$f$ 算法，在 $\chi^2$ 和 KL 散度下均实现了近似极小极大最优的遗憾界，且不依赖任何结构性假设。

**[T2I-RiskyPrompt: A Benchmark for Safety Evaluation, Attack, and Defense on Text-to-Image Model](t2i-riskyprompt_a_benchmark_for_safety_evaluation_attack_and_defense_on_text-to-.md)**

:   构建T2I-RiskyPrompt——一个包含6,432条有效风险prompt的综合基准，涵盖6大类14细分风险类别，每条prompt带有层次化标注和详细风险原因，并提出reason-driven的MLLM风险检测方法（3B模型达91.8%准确率），系统评估了8个T2I模型、9种防御方法、5种安全过滤器和5种攻击策略。
