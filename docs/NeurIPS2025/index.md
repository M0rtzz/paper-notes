<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧠 NeurIPS2025 论文笔记

共 **1664** 篇笔记，覆盖 **35** 个领域。

## 领域概览

| 领域 | 篇数 |
|:-----|-----:|
| 🎨 [图像生成](#image_generation) | 136 |
| 💬 [LLM / NLP](#llm_nlp) | 132 |
| 🧩 [多模态 VLM](#multimodal_vlm) | 107 |
| 📦 [模型压缩](#model_compression) | 104 |
| 🎮 [强化学习](#reinforcement_learning) | 94 |
| 💡 [LLM 推理](#llm_reasoning) | 74 |
| 🏥 [医学图像](#medical_imaging) | 73 |
| 🛡️ [AI 安全](#ai_safety) | 71 |
| 📐 [优化/理论](#optimization) | 65 |
| 🧊 [3D 视觉](#3d_vision) | 59 |
| ⚡ [LLM 效率](#llm_efficiency) | 54 |
| 🦾 [LLM Agent](#llm_agent) | 53 |
| ⚖️ [对齐 / RLHF](#llm_alignment) | 52 |
| 🧑 [人体理解](#human_understanding) | 49 |
| 🎬 [视频理解](#video_understanding) | 43 |
| 🕸️ [图学习](#graph_learning) | 35 |
| 📈 [时间序列](#time_series) | 35 |
| 🚗 [自动驾驶](#autonomous_driving) | 33 |
| 🤖 [机器人/具身智能](#robotics) | 32 |
| 🎵 [音频/语音](#audio_speech) | 31 |
| 🎯 [目标检测](#object_detection) | 29 |
| ✂️ [语义分割](#segmentation) | 26 |
| 🔄 [自监督/表示学习](#self_supervised) | 24 |
| 🔗 [因果推理](#causal_inference) | 23 |
| 🖼️ [图像恢复](#image_restoration) | 22 |
| 🧮 [科学计算](#scientific_computing) | 22 |
| ⚛️ [物理学](#physics) | 21 |
| 🎁 [推荐系统](#recommender) | 18 |
| 📡 [信号/通信](#signal_comm) | 13 |
| ✍️ [文本生成](#nlp_generation) | 11 |
| 📖 [NLP 理解](#nlp_understanding) | 11 |
| 🛰️ [遥感](#remote_sensing) | 9 |
| 🔎 [AIGC 检测](#aigc_detection) | 7 |
| 🌍 [地球科学](#earth_science) | 5 |
| 📂 [其他](#others) | 91 |

---

## 🎨 图像生成 { #image_generation }

**[70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float (DFloat11)](image_generation/70_size_100_accuracy_lossless_llm_compression_for_efficient.md)**

:   DFloat11 利用 BFloat16 权重中指数位（exponent）的低熵特性，通过 Huffman 编码将 LLM/扩散模型无损压缩至原始大小的约 70%（等效 ~11 bit），并设计了层次化查找表和两阶段 GPU kernel 实现高效在线解压，使 Llama 3.1 405B 可在单节点 8×80GB GPU 上无损推理。

**[A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](image_generation/a_closer_look_at_model_collapse_from_a_generalization-to-memorization_perspectiv.md)**

:   发现扩散模型在自消耗循环（用生成数据训练下一代模型）中存在从"泛化"到"记忆"的转变过程，揭示训练集熵与模型泛化能力的强线性相关性（Pearson r=0.91），并提出基于熵的数据选择策略（Greedy Selection / Threshold Decay Filter）有效减缓该转变，在 CIFAR-10 accumulate 范式下第 8 轮 FID 从 75.7 降至 44.7。

**[A Connection Between Score Matching and Local Intrinsic Dimension](image_generation/a_connection_between_score_matching_and_local_intrinsic_dimension.md)**

:   证明去噪得分匹配损失（denoising score matching loss）的下界恰好是数据流形的局部固有维度（LID），从而将 DSM loss 本身作为一个高效的 LID 估计器——无需梯度计算或多次前向传播，在 Stable Diffusion 3.5 上内存占用仅为 FLIPD 的 60%，且量化后估计更稳定。

**[A Data-Driven Prism: Multi-View Source Separation with Diffusion Model Priors](image_generation/a_data-driven_prism_multi-view_source_separation_with_diffusion_model_priors.md)**

:   提出 DDPRISM 方法，利用多视图观测中不同线性变换的结构性差异，在 EM 框架下为每个未知源学习独立的扩散模型先验，无需预先获得任何单独的源样本即可完成源分离和后验采样，在合成问题和真实星系观测上超越现有方法。

**[A Diffusion Model for Regular Time Series Generation from Irregular Data with Completion and Masking](image_generation/a_diffusion_model_for_regular_time_series_generation_from_irregular_data_with_co.md)**

:   提出两步框架从不规则采样时序数据生成规则时序：先用 TST 自编码器补全缺失值构造"自然邻域"，再在视觉扩散模型中用 masking 策略仅在观测像素上计算损失，避免对补全值的过度依赖，在判别分数上平均改善 70%，训练速度提升 6.5 倍。

**[A Gradient Flow Approach to Solving Inverse Problems with Latent Diffusion Models](image_generation/a_gradient_flow_approach_to_solving_inverse_problems_with_latent_diffusion_model.md)**

:   提出 DWGF（Diffusion-regularized Wasserstein Gradient Flow），将隐空间扩散模型的后验采样问题严格形式化为 KL 散度在 Wasserstein-2 空间上的正则化梯度流，推导出隐空间中的 ODE 系统用于求解图像逆问题，在 FFHQ-512 上的修复和超分辨率任务中 PSNR 大幅超越基线。

**[Accelerating Parallel Diffusion Model Serving with Residual Compression](image_generation/accelerating_parallel_diffusion_model_serving_with_residual_compression.md)**

:   提出 CompactFusion 框架，通过残差压缩（仅传输相邻去噪步骤间的激活差异而非完整激活）来消除并行扩散推理中的通信冗余，在 4×L20 上实现 3.0× 加速且生成质量远优于 DistriFusion，在模拟以太网带宽下实现 6.7× 加速，甚至在 100× 压缩下仍优于 DistriFusion。

**[AccuQuant: Simulating Multiple Denoising Steps for Quantizing Diffusion Models](image_generation/accuquant_simulating_multiple_denoising_steps_for_quantizing.md)**

:   提出AccuQuant，一种用于扩散模型的训练后量化（PTQ）方法，通过在校准过程中显式模拟多个去噪步骤来最小化量化误差的累积效应，并通过新型目标函数将内存复杂度从O(n)降至O(1)。

**[Adapting Speech Language Model to Singing Voice Synthesis](image_generation/adapting_speech_language_model_to_singing_voice_synthesis.md)**

:   将 1.7B 参数的 TTS 预训练 Speech Language Model 适配到歌声合成（SVS）任务，通过乐谱 tokenization + multi-stream LM 预测 + conditional flow matching 精修 + vocoder，仅用 135 小时合成歌声数据达到与专用 SVS 系统可比的性能。

**[ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering](image_generation/alebench_a_benchmark_for_longhorizon_objectivedriven_algorit.md)**

:   提出 ALE-Bench，首个面向分数制算法工程竞赛（AtCoder Heuristic Contest）的 AI 基准，评估 LLM 和 Agent 在 NP-hard 优化问题上的长时间迭代改进能力，发现当前最强模型（o3-high）仅达人类平均水平，且在问题一致性和长时间改进方面与人类专家差距显著。

**[Aligning Compound AI Systems via System-level DPO](image_generation/aligning_compound_ai_systems_via_system-level_dpo.md)**

:   将复合 AI 系统建模为 DAG，提出 SysDPO 框架将 DPO 扩展到多组件联合对齐，通过 DAG 分解将系统级偏好转化为可端到端优化的损失函数，理论证明了 β-完美对齐保证，在 LLM+扩散模型和 LLM+LLM 系统上显著提升协作质量。

**[Aligning Text to Image in Diffusion Models is Easier Than You Think](image_generation/aligning_text_to_image_in_diffusion_models_is_easier_than_you_think.md)**

:   提出 SoftREPA——一种轻量级对比微调策略，通过引入可学习 soft text token（不到 1M 参数）在冻结的预训练 T2I 扩散模型上进行对比学习，显式提高文本和图像表征的互信息，在 SD1.5/SDXL/SD3 上显著提升文本-图像对齐质量，且适用于图像生成和图像编辑任务。

**[Amortized Sampling with Transferable Normalizing Flows](image_generation/amortized_sampling_with_transferable_normalizing_flows.md)**

:   提出 Prose——一个 285M 参数的全原子可迁移归一化流，基于 TarFlow 架构训练在 21,700 个短肽 MD 轨迹上（总计 4.3ms 模拟时长），实现对任意短肽系统的零样本无相关性提议采样，在能量评估预算相同时超越 MD 基线，生成速度比之前的可迁移玻尔兹曼生成器 (TBG) 快 4000 倍。

**[AugGen: Synthetic Augmentation using Diffusion Models Can Improve Recognition](image_generation/auggen_synthetic_augmentation_using_diffusion_models_can_imp.md)**

:   提出AugGen——一种自包含（self-contained）的合成数据增强方法：利用扩散模型的条件向量插值（$c^* = \alpha c_i + \beta c_j$）实现类间混合生成，无需外部数据或模型即可为人脸识别提供1-12%的性能提升，等效于1.7倍真实数据量，IR50+AugGen甚至超越IR101 real-only。

**[Autoregressive Adversarial Post-Training for Real-Time Interactive Video Generation](image_generation/autoregressive_adversarial_posttraining_for_realtime_interac.md)**

:   提出 AAPT（Autoregressive Adversarial Post-Training），将预训练的潜在视频扩散模型转化为实时交互式视频生成器——每帧仅需单次神经网络前向传播（1NFE），自回归逐帧生成，8B 模型在单张 H100 上以 24fps 流式生成 736×416 视频，最长可达一分钟（1440帧）。

**[BADiff: Bandwidth Adaptive Diffusion Model](image_generation/badiff_bandwidth_adaptive_diffusion_model.md)**

:   提出 BADiff——首个带宽自适应扩散模型，通过将目标熵约束作为条件嵌入扩散反向过程，配合可微熵正则化损失和自适应停止策略，使模型根据实时带宽动态调整生成质量并自适应提前终止采样，在保持感知质量的同时减少计算开销，从根本上避免了传统"高质量生成→后压缩"流程中的压缩伪影和计算浪费。

**[Balanced Conic Rectified Flow](image_generation/balanced_conic_rectified_flow.md)**

:   针对 k-rectified flow 中 reflow 步骤导致的分布漂移问题，提出 conic reflow：利用真实图像的反演噪声及其 Slerp 扰动构成锥形监督轨迹，大幅减少所需 fake pair 数量的同时获得更优的生成质量和更直的 ODE 路径。

**[Beyond Masked and Unmasked: Discrete Diffusion Models via Partial Masking](image_generation/beyond_masked_and_unmasked_discrete_diffusion_models_via_par.md)**

:   提出 Prime（Partial masking scheme），突破 Masked Diffusion Model 的二元状态（mask/unmask）限制，引入中间态（部分观测的 token 信息），减少冗余计算并实现更细粒度的去噪过程，在文本生成上 PPL 15.36 超越自回归模型（17.54）和标准 MDM（21.52），在图像生成上取得 CIFAR-10 FID 3.26。

**[BitMark: Watermarking Bitwise Autoregressive Image Generative Models](image_generation/bitmark_watermarking_bitwise_autoregressive_image_generative_models.md)**

:   提出 BitMark——首个针对比特级自回归图像生成模型（Infinity、Instella）的水印方案，在生成过程中通过对 logit 加偏置将 bit 序列引向"绿色列表"，实现可靠检测（z-test）、高图像保真度（FID 几乎不变）、对多种攻击的鲁棒性和放射性（训练在水印图上的下游模型也带有水印），为防止模型坍缩提供了关键工具。

**[Blameless Users in a Clean Room: Defining Copyright Protection for Generative Models](image_generation/blameless_users_in_a_clean_room_defining_copyright_protection_for_generative_mod.md)**

:   重建生成模型可证明版权保护的理论基础——证明现有的 Near Access-Freeness (NAF) 定义不能防止逐字复制（"被污染"），提出"无辜用户"(blameless) 框架和净室版权保护 ($(\kappa,\beta)$-clean) 定义，其中用户在反事实"净室设置"中不会复制则在真实世界中也不太可能复制，并证明差分隐私训练在"黄金数据集"假设下蕴含净室版权保护。

**[Blind Strong Gravitational Lensing Inversion: Joint Inference of Source and Lens Mass with Score-Based Models](image_generation/blind_strong_gravitational_lensing_inversion_joint_inference_of_source_and_lens_.md)**

:   首次将 score-based 生成模型先验应用于强引力透镜的盲反演——联合推断背景源天体形态和透镜质量分布参数，通过将 GibbsDDRM 扩展到连续时间域实现采样，重建残差与观测噪声一致，透镜参数边际后验无系统偏差。

**[BlurDM: A Blur Diffusion Model for Image Deblurring](image_generation/blurdm_a_blur_diffusion_model_for_image_deblurring.md)**

:   提出 BlurDM，将运动模糊的物理形成过程（连续曝光导致渐进模糊累积）集成到扩散模型——双扩散前向（同时加噪声+模糊）+ 双去噪去模糊反向，作为隐空间先验生成器一致性增强 4 种去模糊方法在 4 个数据集上的效果，GoPro 平均 +0.31 dB，RealBlur-J 平均 +0.78 dB，仅增加 ~4 GFLOPs 和 ~9ms。

**[BlurGuard: A Simple Approach for Robustifying Image Protection Against AI-Powered Edit](image_generation/blurguard_a_simple_approach_for_robustifying_image_protection_against_ai-powered.md)**

:   提出 BlurGuard——在生成对抗扰动之前先对图像做轻度模糊预处理，使扰动更鲁棒地抵御 JPEG 压缩、高斯噪声等后处理操作，从而更有效地保护图像不被 Stable Diffusion 等 AI 编辑工具篡改，在保护成功率上比不模糊基线提升 20%+。

**[BoltzNCE: Learning Likelihoods for Boltzmann Generation with Stochastic Interpolants](image_generation/boltznce_learning_likelihoods_for_boltzmann_generation_with_stochastic_interpola.md)**

:   BoltzNCE 用 Score Matching + InfoNCE 混合训练 Energy-Based Model 来近似 Boltzmann Generator 的似然，避免了昂贵的 Jacobian trace 计算，在丙氨酸二肽构象生成上实现 100× 推理加速且自由能误差仅 0.02 $k_BT$。

**[Boosting Generative Image Modeling via Joint Image-Feature Synthesis](image_generation/boosting_generative_image_modeling_via_joint_imagefeature_sy.md)**

:   提出 Latent-Semantic Diffusion，让扩散模型联合生成 VAE 低级图像 latent 和 DINO 高级语义特征，通过最小修改标准 DiT 实现生成质量和训练效率的显著提升，并解锁 Representation Guidance 推理策略。

**[Breaking AR's Sampling Bottleneck: Provable Acceleration via Diffusion Language Models](image_generation/breaking_ars_sampling_bottleneck_provable_acceleration_via_d.md)**

:   从信息论角度为扩散语言模型建立收敛保证，证明采样误差（KL散度）随迭代次数T成反比衰减且与token间互信息线性相关，关键证明了T<L（迭代次数可少于序列长度L）时仍可生成高质量样本，从理论上打破了自回归模型需要L步的基本采样瓶颈，并建立了匹配的上下界证明分析的紧致性。

**[CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop](image_generation/cadmorph_geometry-driven_parametric_cad_editing_via_a_plan-generate-verify_loop.md)**

:   提出 CADMorph，一个迭代式 plan–generate–verify 框架，利用预训练的 Parameter-to-Shape (P2S) 扩散模型和 Masked-Parameter-Prediction (MPP) 大语言模型协同工作，在无需三元组训练数据的情况下实现几何驱动的参数化 CAD 编辑。

**[CAMILA: Context-Aware Masking for Image Editing with Language Alignment](image_generation/camila_contextaware_masking_for_image_editing_with_language.md)**

:   提出 CAMILA，一种上下文感知的图像编辑方法，能够判断用户指令是否在当前图像上下文中可行，仅执行可行的编辑指令而忽略不可执行的指令，在单指令和多指令编辑场景中均优于现有方法。

**[CaMiT: A Time-Aware Car Model Dataset for Classification and Generation](image_generation/camit_a_time-aware_car_model_dataset_for_classification_and_generation.md)**

:   提出 CaMiT 数据集（787K 标注 + 5.1M 无标注汽车图像，2005–2023），系统研究细粒度视觉类别的时间漂移问题，并在静态预训练、时间增量预训练、时间增量分类器学习和时间感知图像生成四个场景下提供 benchmark。

**[Can Knowledge-Graph-based Retrieval Augmented Generation Really Retrieve What You Need?](image_generation/can_knowledge-graph-based_retrieval_augmented_generation_really_retrieve_what_yo.md)**

:   提出 GraphFlow 框架，将知识图谱上的检索建模为 GFlowNet 的流匹配问题，通过详细平衡目标和局部探索策略联合训练检索策略与流估计器，在 STaRK 基准上检索准确率和多样性均超越 GPT-4o 约 10%。

**[CDFlow: Building Invertible Layers with Circulant and Diagonal Matrices](image_generation/cdflow_building_invertible_layers_with_circulant_and_diagonal_matrices.md)**

:   提出 CDFlow，利用循环矩阵和对角矩阵的交替乘积构造可逆线性层，将参数复杂度从 $\mathcal{O}(n^2)$ 降至 $\mathcal{O}(mn)$，矩阵逆复杂度从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(mn\log n)$，对数行列式从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(mn)$，在密度估计和周期性数据建模上超越同类方法。

**[Composite Flow Matching for Reinforcement Learning with Shifted-Dynamics Data](image_generation/composite_flow_matching_for_reinforcement_learning_with_shifted-dynamics_data.md)**

:   提出 CompFlow，通过复合流匹配架构（在离线流输出分布上构建在线流）估计离线-在线环境间的动态差异（Wasserstein 距离），并结合高动态差异区域的主动探索策略，在 27 个动态偏移 RL 任务中平均回报超越最强基线 14.2%。

**[Composition and Alignment of Diffusion Models using Constrained Learning](image_generation/composition_and_alignment_of_diffusion_models_using_constrai.md)**

:   提出统一的约束学习框架来处理扩散模型的对齐（alignment）和组合（composition），将多奖励对齐形式化为 KL 散度最小化+奖励约束，将模型组合形式化为 minimax KL 散度问题，通过拉格朗日对偶的原-对偶训练算法求解，相比传统加权方法更可解释且避免了手动调权。

**[Conditional Panoramic Image Generation via Masked Autoregressive Modeling](image_generation/conditional_panoramic_image_generation_via_masked_autoregres.md)**

:   提出PAR（Panoramic AutoRegressive model），首次用掩码自回归建模统一文本到全景图和全景图外延两大任务，通过循环平移一致性损失和双空间循环填充解决ERP全景图的边界不连续问题，在Matterport3D上取得37.37 FID，同时展示出良好的可扩展性和零样本泛化能力。

**[Constrained Discrete Diffusion](image_generation/constrained_discrete_diffusion.md)**

:   提出 CDD（Constrained Discrete Diffusion），将可微约束优化投影算子嵌入离散扩散模型的去噪过程中，无需重训练即可在采样时强制满足序列级约束，在毒性文本生成、分子设计和指令遵循三类任务上实现零约束违反。

**[Contextual Thompson Sampling via Generation of Missing Data](image_generation/contextual_thompson_sampling_via_generation_of_missing_data.md)**

:   提出 Generative Thompson Sampling (TS-Gen)，将上下文老虎机中的不确定性建模为缺失数据而非未知参数，通过生成模型对缺失结果做自回归填充来实现 Thompson 采样，建立了与离线预测损失直接挂钩的遗憾界。

**[Continuous Diffusion Model for Language Modeling](image_generation/continuous_diffusion_model_for_language_modeling.md)**

:   提出一种面向离散语言建模的连续扩散框架，将离散扩散过程与统计流形上的连续流联系起来，并通过径向对称的 simulation-free 训练机制与降维技巧，显著提升扩散语言模型性能，接近自回归模型。

**[Continuous Uniqueness and Novelty Metrics for Generative Modeling of Inorganic Crystals](image_generation/continuous_uniqueness_and_novelty_metrics_for_generative_modeling_of_inorganic_c.md)**

:   针对无机晶体生成模型评估中广泛使用的离散距离函数 (StructureMatcher) 的四大缺陷，提出基于 Magpie 指纹（成分）和 AMD 向量（结构）的连续距离函数，实现更可靠的 uniqueness 和 novelty 度量。

**[CORAL: Disentangling Latent Representations in Long-Tailed Diffusion](image_generation/coral_disentangling_latent_representations_in_longtailed_dif.md)**

:   论文系统分析长尾数据下扩散模型尾部类别生成质量下降的根因，指出 U-Net 瓶颈潜表示发生“头类-尾类子空间重叠”导致特征借用，并提出 CORAL 对比式潜空间对齐正则，显著提升尾类样本的多样性与视觉质量。

**[Co-Reinforcement Learning for Unified Multimodal Understanding and Generation](image_generation/coreinforcement_learning_for_unified_multimodal_understandin.md)**

:   提出CoRL框架——通过"统一RL→精细RL"两阶段GRPO训练策略，在不依赖额外监督数据的情况下，让统一多模态模型(ULM)的理解和生成能力协同进化，在Janus-Pro-1.5B上取得生成+7%、理解+23%的平均提升。

**[Counterfactual Identifiability via Dynamic Optimal Transport](image_generation/counterfactual_identifiability_via_dynamic_optimal_transport.md)**

:   利用动态最优传输 (dynamic OT) 理论，首次解决了高维多变量 Markovian SCM 中反事实的可辨识性问题——证明 OT flow 机制产生唯一的单调保序反事实传输映射，并扩展至非 Markovian 设置（IV/BC/FC 准则）。

**[Coupling Generative Modeling and an Autoencoder with the Causal Bridge](image_generation/coupling_generative_modeling_and_an_autoencoder_with_the_causal_bridge.md)**

:   在存在未观测混淆因子的因果推断中，提出将生成模型与自编码器耦合来提升因果桥函数 (causal bridge) 的估计质量——通过共享编码器在处理/控制/结果变量间传递统计强度，并将框架扩展到生存分析。

**[Cross-fluctuation Phase Transitions Reveal Sampling Dynamics in Diffusion Models](image_generation/cross-fluctuation_phase_transitions_reveal_sampling_dynamics_in_diffusion_models.md)**

:   借鉴统计物理中的涨落理论（fluctuation theory），提出了一种通过 **交叉涨落（cross-fluctuation）** 检测扩散模型采样过程中离散相变的框架，从而在无需重新训练的情况下加速采样、改进条件生成、提升零样本分类和风格迁移。

**[Decomate: Leveraging Generative Models for Co-Creative SVG Animation](image_generation/decomate_leveraging_generative_models_for_co-creative_svg_animation.md)**

:   提出 Decomate 交互系统，利用多模态大语言模型 (MLLM) 将非结构化 SVG 图形自动分解为语义组件，设计师通过自然语言为各组件指定动画行为，系统生成可生产的 HTML/CSS/JS 动画代码，支持迭代协作创作。

**[DEFT: Decompositional Efficient Fine-Tuning for Text-to-Image Models](image_generation/deft_decompositional_efficient_finetuning_for_texttoimage_mo.md)**

:   提出DEFT——将权重更新分解为两个可训练矩阵的组合：(1)低秩子空间的正交投影和(2)子空间内的低秩调整，相比LoRA在T2I个性化中CLIP-T从0.341提升到0.361（DreamBench+），在统一模型上实现风格迁移和条件生成的SOTA。

**[Denoising Weak Lensing Mass Maps with Diffusion Model and Generative Adversarial Network](image_generation/denoising_weak_lensing_mass_maps_with_diffusion_model_and_generative_adversarial.md)**

:   将扩散模型（DM）应用于弱引力透镜质量图去噪任务，与 GAN（pix2pix）在相同实验设置下进行系统性对比，证明 DM 在训练稳定性、多样本平均鲁棒性和多种统计量重建精度上全面优于 GAN。

**[Detecting Generated Images by Fitting Natural Image Distributions](image_generation/detecting_generated_images_by_fitting_natural_image_distributions.md)**

:   提出一致性验证框架 ConV，利用自然图像流形与生成图像之间的几何差异，通过两个梯度正交的函数实现无需训练的生成图像检测，并引入 Normalizing Flow 增强版 F-ConV 进一步放大流形偏差。

**[Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model](image_generation/detection_and_simulation_of_urban_heat_islands_using_a_fine-tuned_geospatial_fou.md)**

:   提出一套利用微调地理空间基础模型（Granite-GFM）的完整工作流，涵盖城市热岛效应的实证量化、未来气候情景下的温度外推预测，以及通过卫星图像 inpainting 模拟城市绿化降温效果。

**[DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models](image_generation/dexter_diffusion-guided_explanations_with_textual_reasoning_for_vision_models.md)**

:   提出 DEXTER，一个无需数据的框架，通过优化文本提示驱动扩散模型生成最大化目标分类器激活的图像，再用 LLM 对合成样本进行推理，生成全局性、可读的文本解释，实现模型行为的偏差发现和全局解释。

**[DiCo: Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling](image_generation/dico_revitalizing_convnets_for_scalable_and_efficient_diffus.md)**

:   重新发掘卷积网络在扩散模型中的潜力——发现预训练DiT的全局自注意力主要捕获局部模式（冗余），提出用标准ConvNet模块+紧凑通道注意力构建纯卷积扩散模型DiCo，在ImageNet-256上以2.05 FID超越DiT-XL/2且速度快2.7倍。

**[Diff-ICMH: Harmonizing Machine and Human Vision in Image Compression with Generative Prior](image_generation/diff-icmh_harmonizing_machine_and_human_vision_in_image_compression_with_generat.md)**

:   提出 Diff-ICMH，一种基于扩散模型的生成式图像压缩框架，通过语义一致性损失（SC loss）保持语义完整性，通过标签引导模块（TGM）激活生成先验，以单一编解码器和码流同时服务 10+ 种智能任务和人类视觉感知，无需任何任务特定适配。

**[DiffEye: Diffusion-Based Continuous Eye-Tracking Data Generation Conditioned on Natural Images](image_generation/diffeye_diffusion-based_continuous_eye-tracking_data_generation_conditioned_on_n.md)**

:   提出 DiffEye，首个基于扩散模型直接利用原始眼动轨迹数据、以自然图像为条件生成连续且多样化眼动轨迹的框架，同时引入对应位置嵌入 (CPE) 对齐注视空间与图像语义空间。

**[Diffusion-Based Electromagnetic Inverse Design of Scattering Structured Media](image_generation/diffusion-based_electromagnetic_inverse_design_of_scattering_structured_media.md)**

:   提出基于条件扩散模型的电磁逆设计框架，从目标微分散射截面 (DSCS) 直接生成介电球超表面几何结构，绕过昂贵的迭代优化，并自然处理逆问题的非唯一性，性能优于 CMA-ES 进化优化且速度快数个数量级。

**[Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation](image_generation/diffusion-driven_progressive_target_manipulation_for_source-free_domain_adaptati.md)**

:   提出 DPTM 框架，利用潜在扩散模型对不可信目标样本进行语义变换，生成伪目标域并通过渐进式重建机制迭代缩小与真实目标域的差距，在大域偏移场景下比现有 SFDA SOTA 提升高达 18.6%。

**[Diffusion Adaptive Text Embedding for Text-to-Image Diffusion Models](image_generation/diffusion_adaptive_text_embedding_for_texttoimage_diffusion.md)**

:   发现T2I扩散模型中固定的text embedding在不同时间步是次优的，提出DATE——在推理时动态更新text embedding以最大化mean predicted image与文本的对齐评分（如CLIP Score/ImageReward），无需训练，可即插即用到任何扩散模型和采样器中，在多概念生成和图像编辑中一致提升text-image对齐。

**[Diffusion Classifiers Understand Compositionality, but Conditions Apply](image_generation/diffusion_classifiers_understand_compositionality_but_condit.md)**

:   全面研究零样本扩散分类器在组合理解任务上的判别能力：覆盖3个扩散模型(SD 1.5/2.0/3-m)×10个数据集×30+任务，引入Self-Bench诊断基准（用扩散模型自己生成的图像消除域差异），发现扩散分类器确实理解组合性但受域差距和时间步加权影响——"条件适用"。

**[Diffusion Generative Modeling on Lie Group Representations](image_generation/diffusion_generative_modeling_on_lie_group_representations.md)**

:   提出在李群**表示空间**（而非李群本身）上构建扩散过程的新理论框架，通过广义分数匹配将非阿贝尔李群的弯曲动力学映射到欧几里得空间中，实现无模拟训练的李群扩散模型，并证明标准分数匹配是其平移群的特例。

**[Diffusion Models Meet Contextual Bandits](image_generation/diffusion_models_meet_contextual_bandits.md)**

:   将预训练扩散模型作为上下文赌博机 (contextual bandits) 问题中动作参数的表达性先验，提出 diffusion Thompson Sampling (dTS) 算法，通过高效的层次化后验近似实现快速更新与采样，在大动作空间下显著优于传统方法。

**[Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation](image_generation/distilled_decoding_2_onestep_sampling_of_image_autoregressiv.md)**

:   提出 Distilled Decoding 2 (DD2)，通过条件分数蒸馏损失将图像自回归模型压缩为单步生成器，在 ImageNet-256 上 FID 仅从 3.40 增至 5.43，比 DD1 的 one-step 差距缩小 67%，训练加速 12.3×。

**[DOVE: Efficient One-Step Diffusion Model for Real-World Video Super-Resolution](image_generation/dove_efficient_one-step_diffusion_model_for_real-world_video_super-resolution.md)**

:   提出 DOVE，基于 CogVideoX 预训练视频生成模型，通过两阶段潜空间-像素空间训练策略和高质量 HQ-VSR 数据集实现单步推理的视频超分辨率，比多步扩散方法快 28 倍且性能相当或更优。

**[Dynamic Diffusion Schrödinger Bridge in Astrophysical Observational Inversions](image_generation/dynamic_diffusion_schrödinger_bridge_in_astrophysical_observational_inversions.md)**

:   提出 Astro-DSB，一种基于 Diffusion Schrödinger Bridge 的天文物理反问题建模方法，直接学习观测量到真实物理分布的概率映射，训练成本仅为条件 DDPM 的 25%，且在分布外（OOD）测试中展现出显著的泛化优势，并成功应用于 Taurus B213 真实观测数据。

**[EditInfinity: Image Editing with Binary-Quantized Generative Models](image_generation/editinfinity_image_editing_with_binary-quantized_generative_models.md)**

:   提出 EditInfinity，首次将经典"图像反演-图像编辑"范式应用于二值量化自回归生成模型 Infinity，利用量化表示可获取精确中间监督的优势实现高精度图像反演，配合分段线性平滑核实现高保真编辑效果，在 PIE-Bench 上全面超越扩散模型基线。

**[EEGReXferNet: A Lightweight Gen-AI Framework for EEG Subspace Reconstruction via Cross-Subject Transfer Learning and Channel-Aware Embedding](image_generation/eegrexfernet_a_lightweight_gen-ai_framework_for_eeg_subspace_reconstruction_via_.md)**

:   提出 EEGReXferNet，一种轻量级生成式 AI 框架，通过邻域通道感知输入选择、频带特定子窗口卷积编解码、动态滑窗隐空间和参考统计量缩放，在跨被试迁移学习设置下实现 EEG 子空间重建，参数减少约 45%、推理延迟 <1ms，同时保持 PSD 相关性 $\geq 0.95$ 和谱图 RV 系数 $\geq 0.85$。

**[Efficient Rectified Flow for Image Fusion](image_generation/efficient_rectified_flow_for_image_fusion.md)**

:   提出 RFfusion，首次将 Rectified Flow 引入图像融合任务，实现无需额外训练的单步采样，同时设计面向融合的两阶段 VAE 训练策略，在速度和质量上全面超越现有扩散融合方法。

**[Elucidated Rolling Diffusion Models for Probabilistic Forecasting of Complex Dynamics](image_generation/elucidated_rolling_diffusion_models_for_probabilistic_forecasting_of_complex_dyn.md)**

:   提出 ERDM，首次将滚动扩散（Rolling Diffusion）框架与 EDM 的原则性设计（噪声调度、预条件化、Heun 采样器）成功统一，通过渐进噪声调度显式建模不确定性增长，在 Navier-Stokes 和 ERA5 天气预报任务上显著优于自回归 EDM 基线。

**[Emergence and Evolution of Interpretable Concepts in Diffusion Models](image_generation/emergence_and_evolution_of_interpretable_concepts_in_diffusi.md)**

:   首次将 Sparse Autoencoders (SAEs) 系统性地应用于多步扩散模型 (Stable Diffusion v1.4)，揭示了图像构图在第一步反向扩散就已涌现、风格概念在中期阶段形成的时间演化规律，并据此设计了时间自适应的因果干预技术。

**[Encoder-Decoder Diffusion Language Models for Efficient Training and Inference](image_generation/encoder-decoder_diffusion_language_models_for_efficient_training_and_inference.md)**

:   提出 E2D2，一种面向离散扩散语言模型的编码器-解码器架构，通过轻量解码器迭代去噪、大型编码器定期更新表征，同时实现更快推理（~3× vs MDLM）和更高效的 block diffusion 训练（FLOPs 减半）。

**[Energy Loss Functions for Physical Systems](image_generation/energy_loss_functions_for_physical_systems.md)**

:   提出基于物理能量的损失函数框架，通过反向 KL 散度与玻尔兹曼分布推导出以成对距离为基础的能量差损失，天然满足 SE(d) 不变性，在分子生成和自旋基态预测中显著优于 MSE 和交叉熵损失。

**[Enhancing Diffusion Model Guidance through Calibration and Regularization](image_generation/enhancing_diffusion_model_guidance_through_calibration_and_regularization.md)**

:   针对分类器引导扩散模型中分类器过度自信导致梯度消失的问题，提出两类互补方案：(1) Smooth ECE 校准损失微调分类器，FID 改善 ~3%；(2) 基于 f-散度的正则化采样引导（RKL/FKL/JS），无需重训练即在 ImageNet 128×128 上达到 FID 2.13。

**[Entropy Rectifying Guidance for Diffusion and Flow Models](image_generation/entropy_rectifying_guidance_for_diffusion_and_flow_models.md)**

:   提出 Entropy Rectifying Guidance (ERG)，通过操控注意力层的 Hopfield 能量景观（温度缩放、步长调整）来获取弱预测信号，替代传统 CFG 中的无条件预测，在文本到图像、类条件和无条件生成中同时提升质量、多样性和一致性。

**[Epistemic Uncertainty for Generated Image Detection](image_generation/epistemic_uncertainty_for_generated_image_detection.md)**

:   提出 WePe（Weight Perturbation），通过对预训练视觉大模型（DINOv2）施加权重扰动来估计认识不确定性（epistemic uncertainty），利用自然图像与 AI 生成图像在不确定性空间的差异实现检测，无需训练即可使用。

**[Equivariant Flow Matching for Symmetry-Breaking Bifurcation Problems](image_generation/equivariant_flow_matching_for_symmetry-breaking_bifurcation_problems.md)**

:   提出等变 flow matching 框架，结合 symmetric coupling 策略，用生成式 AI 建模对称性破缺分岔问题中的多模态概率分布，在物理系统（屈曲梁、Allen-Cahn 方程）上显著优于确定性模型和 VAE。

**[Evaluating the Evaluators: Metrics for Compositional Text-to-Image Generation](image_generation/evaluating_the_evaluators_metrics_for_compositional_text-to-image_generation.md)**

:   系统评估了 12 种文本-图像组合对齐指标与人类判断的一致性，发现没有单一指标在所有组合任务上一致表现最优，VQA 指标并非总是最好的，embedding 类指标（ImageReward、HPS）在特定类别上更强。

**[EVODiff: Entropy-aware Variance Optimized Diffusion Inference](image_generation/evodiff_entropy-aware_variance_optimized_diffusion_inference.md)**

:   从信息论角度分析扩散模型推理过程，提出通过优化条件方差来减少条件熵的 EVODiff 方法，在不修改模型的前提下显著加速采样并提升生成质量。

**[Evolve to Inspire: Novelty Search for Diverse Image Generation](image_generation/evolve_to_inspire_novelty_search_for_diverse_image_generation.md)**

:   提出 Wander 框架，基于新颖性搜索（novelty search）和 LLM 驱动的 prompt 进化，从单个文本提示出发生成高度多样化的图像集合，在 Vendi Score 上超越现有进化式 prompt 优化基线。

**[Exploring Semantic-constrained Adversarial Example with Instruction Uncertainty Reduction](image_generation/exploring_semantic-constrained_adversarial_example_with_instruction_uncertainty_.md)**

:   提出多维度指令不确定性缩减框架 InSUR，通过 ResAdv-DDIM 采样器稳定对抗优化方向、上下文编码的攻击场景约束、以及基于 WordNet 的语义抽象评估，首次实现了从自然语言指令生成 2D/3D 语义约束对抗样本（SemanticAE）。

**[Exploring Variational Graph Autoencoders for Distribution Grid Data Generation](image_generation/exploring_variational_graph_autoencoders_for_distribution_grid_data_generation.md)**

:   探索变分图自编码器（VGAE）生成合成配电网拓扑的能力，评估四种解码器架构在两个数据集上的表现，揭示 VGAE 在小型同质网络上效果良好但在大型异质网络上面临挑战。

**[FairImagen: Post-Processing for Bias Mitigation in Text-to-Image Models](image_generation/fairimagen_post-processing_for_bias_mitigation_in_text-to-image_models.md)**

:   提出 FairImagen 后处理去偏框架，通过在 CLIP prompt 嵌入空间应用 FairPCA 投影去除人口统计信息，结合经验噪声注入和跨人口统计联合去偏，在不重训模型的前提下显著提升文本到图像生成的公平性。

**[FALCON: Few-step Accurate Likelihoods for Continuous Flows](image_generation/falcon_few-step_accurate_likelihoods_for_continuous_flows.md)**

:   提出 FALCON，通过混合训练目标（flow matching + 平均速度损失 + 可逆性正则化）使连续归一化流在少步采样下仍能提供足够精确的似然估计，从而实现比传统 CNF 快两个数量级的 Boltzmann 采样。

**[Fast Data Attribution for Text-to-Image Models](image_generation/fast_data_attribution_for_text-to-image_models.md)**

:   将慢而准确的 unlearning-based 数据归因方法蒸馏为一个可快速检索的特征嵌入空间，在 Stable Diffusion 级别模型上实现比现有方法快 2,500× ~ 400,000× 的数据归因。

**[Fast Solvers for Discrete Diffusion Models: Theory and Applications of High-Order Algorithms](image_generation/fast_solvers_for_discrete_diffusion_models_theory_and_applications_of_high-order.md)**

:   为离散扩散模型推理首次提出高阶数值求解器（θ-RK-2 和 θ-Trapezoidal），在 KL 散度意义下证明二阶收敛，在文本和图像生成任务上以同等计算预算获得更好的样本质量。

**[FerretNet: Efficient Synthetic Image Detection via Local Pixel Dependencies](image_generation/ferretnet_efficient_synthetic_image_detection_via_local_pixel_dependencies.md)**

:   基于 Markov Random Field 理论提出局部像素依赖（LPD）特征表示，结合仅 1.1M 参数的轻量 FerretNet 网络，仅在 4 类 ProGAN 数据上训练即在 22 个生成模型上达到 97.1% 平均准确率。

**[Flatten Graphs as Sequences: Transformers are Scalable Graph Generators](image_generation/flatten_graphs_as_sequences_transformers_are_scalable_graph_generators.md)**

:   提出 AutoGraph，通过分段欧拉邻域路径（SENT）将图无损展平为 token 序列，直接用 decoder-only Transformer 建模，实现比扩散模型快 100× 的图生成速度，同时在合成和分子基准上达到 SOTA。

**[Flattening Hierarchies with Policy Bootstrapping](image_generation/flattening_hierarchies_with_policy_bootstrapping.md)**

:   提出 Subgoal Advantage-Weighted Policy Bootstrapping（SAW），通过优势加权的重要性采样对子目标条件策略进行 bootstrapping，将层级 RL 的长距离推理能力蒸馏到一个扁平策略中，无需生成式子目标模型。

**[Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators](image_generation/flex-judge_text-only_reasoning_unleashes_zero-shot_multimodal_evaluators.md)**

:   提出 Flex-Judge，仅用 1K 条纯文本推理数据微调多模态大模型，即可零样本泛化到图像/视频/音频/分子等多模态评判任务，性能媲美甚至超越 GPT-4o 等商业 API 和大规模标注训练的专用评估器。

**[Flow Matching Neural Processes](image_generation/flow_matching_neural_processes.md)**

:   提出 FlowNP，将 flow matching 引入神经过程框架，通过 transformer 预测目标点的流速度场实现对条件分布的并行采样，在 1D GP、图像和气象数据三大基准上全面超越现有 NP 方法。

**[FocalCodec: Low-Bitrate Speech Coding via Focal Modulation Networks](image_generation/focalcodec_low-bitrate_speech_coding_via_focal_modulation_networks.md)**

:   提出 FocalCodec——基于 Focal Modulation 的低比特率语音编解码器，使用**单个二值码本**将语音压缩至 0.16–0.65 kbps，在语音重合成、语音转换和多项下游任务中达到与多码本 SOTA 方法可比甚至更优的性能。

**[FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency](image_generation/freqpolicy_efficient_flow-based_visuomotor_policy_via_frequency_consistency.md)**

:   首次在 flow-based 视觉运动策略中引入频域一致性约束，利用 DCT 变换将动作块的速度场投影到频域并施加自适应频率分量损失，实现了高质量一步动作生成（93.5 Hz），在仿真和真实机器人任务中均优于现有一步生成方法。

**[From Cradle to Cane: A Two-Pass Framework for High-Fidelity Lifespan Face Aging](image_generation/from_cradle_to_cane_a_two-pass_framework_for_high-fidelity_lifespan_face_aging.md)**

:   提出 Cradle2Cane 两阶段人脸老化框架：第一阶段通过自适应噪声注入（AdaNI）实现精准年龄控制，第二阶段通过 SVR-ArcFace 和 Rotate-CLIP 双身份嵌入（IDEmb）强化身份一致性，在全寿命跨度（0-80岁）人脸老化中实现年龄精度与身份保持的最优平衡。

**[GeneMAN: Generalizable Single-Image 3D Human Reconstruction from Multi-Source Human Data](image_generation/geneman_generalizable_single-image_3d_human_reconstruction_from_multi-source_hum.md)**

:   GeneMAN 提出一种**无需人体参数模型(如 SMPL)**的通用单图 3D 人体重建框架，通过在大规模多源人体数据上训练人体专属的 2D/3D 扩散先验模型，结合几何初始化-雕刻流水线与多空间纹理精炼，实现了对野外图片中不同体型比例、复杂姿态与个人物品的高保真 3D 人体重建。

**[Generative Model Inversion Through the Lens of the Manifold Hypothesis](image_generation/generative_model_inversion_through_the_lens_of_the_manifold_hypothesis.md)**

:   从流形几何视角揭示生成式模型逆向攻击 (MIA) 的本质是通过将损失梯度投影到生成器切空间实现隐式去噪，提出梯度-流形对齐假说（对齐越高→模型越脆弱）并设计无需训练的 AlignMI 方法在多个 SOTA 攻击上取得一致且显著的提升。

**[GenIR: Generative Visual Feedback for Mental Image Retrieval](image_generation/genir_generative_visual_feedback_for_mental_image_retrieval.md)**

:   提出 GenIR，一种利用文本到图像扩散模型生成"合成视觉反馈"的多轮交互式图像检索框架，将系统对用户查询的理解显式可视化，使用户能直观地识别差异并迭代改进查询，在 Mental Image Retrieval (MIR) 任务上大幅超越纯文本反馈方法。

**[Georemover Removing Objects And Their Causal Visual Artifacts](image_generation/georemover_removing_objects_and_their_causal_visual_artifacts.md)**

:   提出几何感知的两阶段框架 GeoRemover，将目标移除解耦为几何移除（深度域）与外观渲染（RGB域），通过修改场景几何表示来隐式消除被移除物体的阴影和反射等因果视觉伪影。

**[Gradient Variance Reveals Failure Modes in Flow-Based Generative Models](image_generation/gradient_variance_reveals_failure_modes_in_flow-based_generative_models.md)**

:   本文通过分析 CFM 损失的梯度方差（gradient variance），揭示了 Rectified Flow 在确定性插值下会不可避免地记忆训练配对而非学习最优传输映射，并证明引入随机性（stochastic interpolant）可打破该记忆化通道、恢复泛化能力。

**[GraLoRA: Granular Low-Rank Adaptation for Parameter-Efficient Fine-Tuning](image_generation/gralora_granular_low-rank_adaptation_for_parameter-efficient_fine-tuning.md)**

:   提出 GraLoRA——将 LoRA 的权重更新矩阵分割为 $k^2$ 个独立子块、每块配独立低秩适配器，在不增加参数量和计算量的前提下将有效秩从 $r$ 提升至 $kr$，解决 LoRA 在高秩下因梯度纠缠导致的性能退化问题，在代码生成上 Pass@1 最高提升 +8.5%。

**[Graph-based Neural Space Weather Forecasting](image_generation/graph-based_neural_space_weather_forecasting.md)**

:   提出基于图神经网络的空间天气神经模拟器，在 Vlasiator 混合 Vlasov 模拟数据上训练，实现确定性和概率性自回归预测近地空间状态，速度比原始模拟快 100 倍以上，并通过隐变量生成集合预报来量化预测不确定性。

**[Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges](image_generation/grasp2grasp_vision-based_dexterous_grasp_translation_via_schrödinger_bridges.md)**

:   提出将跨手形态的视觉灵巧抓取迁移建模为 Schrödinger Bridge 问题，通过在潜空间中学习得分与流匹配（[SF]²M），并设计物理感知的最优传输代价函数（位姿/接触图/力旋量空间/雅可比可操作性），在无需配对数据的条件下实现不同机械手之间抓取意图的分布级迁移。

**[GSPN-2: Efficient Parallel Sequence Modeling](image_generation/gspn-2_efficient_parallel_sequence_modeling.md)**

:   GSPN-2 通过算法-系统联合重设计（单 kernel 融合、紧凑通道传播、共享内存优化），将 GSPN-1 的 2D 空间传播加速最高 40×，在 ImageNet 分类和文本到图像生成中达到 Transformer 级精度且计算成本显著更低。

**[Guided Diffusion Sampling on Function Spaces with Applications to PDEs](image_generation/guided_diffusion_sampling_on_function_spaces_with_applications_to_pdes.md)**

:   提出 **FunDPS（Function-space Diffusion Posterior Sampling）**，在函数空间中训练无条件扩散模型，推理时通过梯度引导实现 plug-and-play 的 PDE 逆问题后验采样；理论上将 Tweedie 公式推广到无穷维 Banach 空间，实验上在 5 个 PDE 任务中仅用 3% 观测即可获得比 DiffusionPDE 平均高 32% 的精度并减少 4 倍采样步数。

**[GuideFlow3D: Optimization-Guided Rectified Flow For Appearance Transfer](image_generation/guideflow3d_optimization-guided_rectified_flow_for_appearance_transfer.md)**

:   提出 GuideFlow3D，一种无需训练的 3D 外观迁移框架，通过在预训练 rectified flow 模型的采样过程中交替注入可微引导损失（部件感知外观损失 + 自相似性损失），实现几何差异显著的物体间鲁棒的纹理与几何细节迁移。

**[Head Pursuit: Probing Attention Specialization in Multimodal Transformers](image_generation/head_pursuit_probing_attention_specialization_in_multimodal.md)**

:   用信号处理中的Simultaneous Orthogonal Matching Pursuit (SOMP)算法分解注意力头在unembedding矩阵上的稀疏表示，揭示注意力头的语义特化现象（如政治/国籍/月份/数字等），仅编辑1%的头即可可靠地抑制或增强特定概念——在语言和视觉-语言模型上均验证有效。

**[Hephaestus: Mixture Generative Modeling with Energy Guidance for Large-scale QoS Degradation](image_generation/hephaestus_mixture_generative_modeling_with_energy_guidance_for_large-scale_qos_.md)**

:   提出 Hephaestus 三阶段生成框架（Forge-Morph-Refine），结合预测路径加压算法、能量引导的混合 CVAE 和潜在空间 RL 优化，用于大规模网络 QoS 降级问题的求解。

**[Hierarchical Koopman Diffusion: Fast Generation with Interpretable Diffusion Trajectory](image_generation/hierarchical_koopman_diffusion_fast_generation_with_interpretable_diffusion_traj.md)**

:   基于 Koopman 算子理论，将扩散模型的非线性去噪动力学提升到线性 Koopman 空间，通过层次化分解实现一步采样，同时保留中间生成状态的可解释性和可控性。

**[High-order Equivariant Flow Matching for Density Functional Theory Hamiltonian Prediction](image_generation/high-order_equivariant_flow_matching_for_density_functional_theory_hamiltonian_p.md)**

:   提出 QHFlow，首次将条件 flow matching 引入密度泛函理论（DFT）哈密顿矩阵预测任务，通过高阶 SE(3) 等变向量场和对称性感知先验分布，在 MD17 上将哈密顿预测误差降低 73%，并可作为 SCF 初始化加速 DFT 计算达 54%。

**[How to Build a Consistency Model: Learning Flow Maps via Self-Distillation](image_generation/how_to_build_a_consistency_model_learning_flow_maps_via_self-distillation.md)**

:   提出统一的自蒸馏（Self-Distillation）框架来直接学习 flow map（即 consistency model 的一般化形式），通过 tangent condition 将任意蒸馏方案转化为无需预训练教师的直接训练算法，并导出三大算法族（Eulerian / Lagrangian / Progressive），其中 Lagrangian 方法避免了空间梯度和自举引导，训练最稳定、性能最优。

**[Image Super-Resolution with Guarantees via Conformalized Generative Models](image_generation/image_super-resolution_with_guarantees_via_conformalized_generative_models.md)**

:   基于共形预测（Conformal Prediction）技术，为生成式图像超分辨率模型构建二值"置信度掩码"，能可靠地标识生成图像中可信赖的区域，并提供严格的统计保证。

**[ImageSentinel: Protecting Visual Datasets from Unauthorized Retrieval-Augmented Image Generation](image_generation/imagesentinel_protecting_visual_datasets_from_unauthorized_retrieval-augmented_i.md)**

:   提出 ImageSentinel 框架，通过合成与私有数据集视觉一致的哨兵图像（sentinel images）并绑定随机字符检索键，实现对检索增强图像生成（RAIG）系统未授权使用私有数据集的可靠检测——仅需 3–10 次查询即可达到接近 100% 的 AUC。

**[Improved Training Technique for Shortcut Models (iSM)](image_generation/improved_training_technique_for_shortcut_models.md)**

:   针对 Shortcut Models 的五大性能瓶颈（指导累积、固定引导、频率偏差、自一致性偏离、弯曲轨迹），提出 iSM 统一训练框架，通过内禀引导、多级小波损失、缩放最优传输和双 EMA 策略，在 ImageNet 256×256 上实现单步 FID 5.27、四步 FID 2.05 的大幅提升。

**[Improving Posterior Inference of Galaxy Properties with Image-Based Conditional Flow Matching](image_generation/improving_posterior_inference_of_galaxy_properties_with_image-based_conditional_.md)**

:   提出基于条件流匹配（CFM）的框架，将星系图像的形态学信息与测光数据联合建模，显著提升星系物理属性（恒星质量、恒星形成率、金属丰度、尘埃消光等）的后验推断精度。

**[In-Context Edit Enabling Instructional Image Editing With In-Context Generation ](image_generation/in-context_edit_enabling_instructional_image_editing_with_in-context_generation_.md)**

:   ICEdit 提出一种基于大规模 Diffusion Transformer (DiT) 的上下文编辑范式，通过 in-context prompt + 最小化 LoRA-MoE 微调 + VLM 早期筛选推理时缩放，仅用 0.1% 训练数据即达到 SOTA 编辑性能。

**[Increasing the Utility of Synthetic Images through Chamfer Guidance](image_generation/increasing_the_utility_of_synthetic_images_through_chamfer_guidance.md)**

:   提出 Chamfer Guidance——一种免训练的推理时引导方法，利用少量真实样本作为参照，通过 Chamfer 距离同时优化合成图像的质量（fidelity）和多样性（diversity），在 ImageNet-1k 上仅用 32 张真实图片即可达到 97.5% Precision 和 92.7% Coverage，并在下游分类器训练中带来最高 16% 的准确率提升。

**[Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing](image_generation/inference-time_scaling_for_flow_models_via_stochastic_generation_and_rollover_bu.md)**

:   提出针对 Flow 模型的推理时扩展方法：通过 ODE→SDE 转换引入随机性以启用粒子采样，利用线性→VP 插值变换扩大搜索空间，并设计 Rollover Budget Forcing (RBF) 策略自适应分配计算预算，在组合文本生成图像和数量感知生成任务上显著超越所有现有方法。

**[InfinityStar: Unified Spacetime AutoRegressive Modeling for Visual Generation](image_generation/infinitystar_unified_spacetime_autoregressive_modeling_for_v.md)**

:   提出 InfinityStar，首个能生成工业级 720p 视频的纯离散自回归模型，通过时空金字塔建模统一 T2I/T2V/I2V/交互式长视频生成，VBench 83.74 超越 HunyuanVideo，推理速度比扩散模型快 10-32×。

**[Information-Theoretic Discrete Diffusion](image_generation/information-theoretic_discrete_diffusion.md)**

:   将连续扩散中经典的 I-MMSE 恒等式推广到离散域，建立 I-MDSE 和 I-MDCE 关系——证明 DSE/DCE 损失不仅是变分上界而是对数似然的**精确分解**，并由此推导出 time-free 公式、条件似然估计和耦合似然比估计器，在 LLaDA 等大模型上验证了低方差和 OOD 检测能力。

**[Information Theoretic Learning for Diffusion Models with Warm Start](image_generation/information_theoretic_learning_for_diffusion_models_with_warm_start.md)**

:   提出将经典 KL 散度-Fisher 信息关系推广到任意各向同性噪声扰动的似然估计框架，结合 warm-start 噪声注入和重要性采样，消除训练-测试差距并实现更紧的似然上界，在 ImageNet 多分辨率上达到 SOTA NLL。

**[Is Artificial Intelligence Generated Image Detection a Solved Problem?](image_generation/is_artificial_intelligence_generated_image_detection_a_solved_problem.md)**

:   提出 AIGIBench 综合基准，通过四大任务（多源泛化、多退化鲁棒性、数据增强敏感性、测试预处理影响）系统评估 11 个 SOTA 检测器，揭示现有 AIGI 检测方法在真实场景下性能严重下降，表明该问题远未解决。

**[ItDPDM: Information-Theoretic Discrete Poisson Diffusion Model](image_generation/itdpdm_information-theoretic_discrete_poisson_diffusion_model.md)**

:   提出 ItDPDM（信息论离散泊松扩散模型），通过泊松噪声信道和泊松重建损失（PRL）实现非负离散数据的精确似然估计，避免了 ELBO 近似和 dequantization，在合成数据及 CIFAR-10 和 MIDI 音乐上取得优于现有离散扩散模型的似然估计。

**[KLASS: KL-Guided Fast Inference in Masked Diffusion Models](image_generation/klass_kl-guided_fast_inference_in_masked_diffusion_models.md)**

:   提出 KLASS（KL-Adaptive Stability Sampling），一种无需训练的采样方法，利用 token 级别的 KL 散度和置信度来识别稳定 token 并行解码，在掩码扩散模型上实现最高 2.78× 加速且不损失甚至提升生成质量。

**[Knowledge Distillation Detection for Open-weights Models](image_generation/knowledge_distillation_detection_for_open-weights_models.md)**

:   提出知识蒸馏检测任务，通过无数据输入合成和统计评分框架，判断一个开放权重的学生模型是否由特定教师模型蒸馏而来。

**[LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss](image_generation/lineas_end-to-end_learning_of_activation_steering_with_a_distributional_loss.md)**

:   提出 LinEAS（Linear End-to-end Activation Steering），通过端到端优化跨层仿射变换映射，利用 1D Wasserstein 分布损失进行全局激活值对齐，仅需 32 个无配对样本即可高效控制 LLM 毒性和 T2I 模型概念生成。

**[MagCache: Fast Video Generation with Magnitude-Aware Cache](image_generation/magcache_fast_video_generation_with_magnitudeaware_cache.md)**

:   发现视频扩散模型中连续时间步残差输出的幅度比(magnitude ratio)遵循统一的单调递减规律（跨模型、跨prompt稳定），提出MagCache基于此规律自适应跳过冗余时间步并复用缓存，仅需1个样本校准即可在Open-Sora/CogVideoX/Wan 2.1/HunyuanVideo上实现2.1-2.68×加速，视觉保真度全面超越现有方法。

**[OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](image_generation/omnisync_towards_universal_lip_synchronization_via_diffusion.md)**

:   OmniSync提出了一种基于Diffusion Transformer的通用唇形同步框架，通过无掩码训练范式、基于Flow Matching的渐进噪声初始化和动态时空CFG三大创新，在真实视频和AI生成视频上都大幅超越先前方法，尤其在风格化角色的唇形同步上达到87.78%成功率（之前最佳67.78%）。

**[On Optimal Steering to Achieve Exact Fairness](image_generation/on_optimal_steering_to_achieve_exact_fairness.md)**

:   本文定义了"理想分布"——使任意代价敏感风险下的 Bayes 最优分类器都满足精确公平性的数据分布，并提出通过 KL 散度最小化寻找最近理想分布的优化框架，为公平预处理和 LLM 表示引导提供了可证明的公平性保证。

**[PhysCtrl: Generative Physics for Controllable and Physics-Grounded Video Generation](image_generation/physctrl_generative_physics_for_controllable_and_physicsgrou.md)**

:   提出 PhysCtrl，通过生成式物理网络学习 4 种材质（弹性体、沙子、橡皮泥、刚体）的物理动力学分布，以 3D 点轨迹表示物理运动，结合 I2V 模型实现物理参数和力可控的视频生成。

**[Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection](image_generation/physics-driven_spatiotemporal_modeling_for_ai-generated_video_detection.md)**

:   提出基于物理守恒定律的AI生成视频检测范式，定义归一化时空梯度（NSG）统计量来捕获空间概率梯度与时间密度变化的比率，利用预训练扩散模型估计NSG并通过MMD进行检测，在Recall上超越SOTA 16%、F1超越10.75%。

**[Remasking Discrete Diffusion Models with Inference-Time Scaling](image_generation/remasking_discrete_diffusion_models_with_inference-time_scaling.md)**

:   提出 ReMDM 采样器，通过在生成过程中允许已解码 token 被重新掩码（remask），赋予离散掩码扩散模型迭代纠错能力，实现推理时计算缩放，在文本、图像和分子设计任务上显著提升采样质量。

**[Safe-Sora: Safe Text-to-Video Generation via Graphical Watermarking](image_generation/safesora_safe_texttovideo_generation_via_graphical_watermark.md)**

:   Safe-Sora 首次将**图形水印**（如logo图像）直接嵌入到视频生成管线中，通过分层粗到细自适应匹配将水印patch分配到视觉最相似的帧和区域，并设计3D小波变换增强Mamba架构实现时空融合，在视频质量（FVD 3.77 vs 次优154.35）和水印保真度上大幅超越所有基线。

**[Scalable, Explainable and Provably Robust Anomaly Detection with One-Step Flow Matching](image_generation/scalable_explainable_and_provably_robust_anomaly_detection_with_one-step_flow_ma.md)**

:   提出 TCCM（Time-Conditioned Contraction Matching），一种受 flow matching 启发的表格数据半监督异常检测方法，通过学习将正常数据收缩到原点的时间条件速度场，仅需单步前向推理即可计算异常分数，在 ADBench 47 个数据集上取得 AUROC 和 AUPRC 双第一，推理速度比 DTE 快 1573 倍。

**[Scaling Offline RL via Efficient and Expressive Shortcut Models](image_generation/scaling_offline_rl_via_efficient_and_expressive_shortcut_models.md)**

:   提出 SORL，利用 shortcut models 的自一致性实现离线 RL 中高效一阶段训练与可变推理步数的策略优化，同时支持推理时的顺序和并行扩展。

**[Schrödinger Bridge Matching for Tree-Structured Costs and Entropic Wasserstein Barycentres](image_generation/schrödinger_bridge_matching_for_tree-structured_costs_and_entropic_wasserstein_b.md)**

:   将Iterative Markovian Fitting (IMF)程序推广到树结构Schrödinger Bridge问题，提出TreeDSBM算法，在Wasserstein重心计算中将IMF迭代与不动点迭代优雅合并，仅需廉价的bridge-matching步骤即可高效求解。

**[Semantic Surgery: Zero-Shot Concept Erasure in Diffusion Models](image_generation/semantic_surgery_zero-shot_concept_erasure_in_diffusion_models.md)**

:   提出Semantic Surgery，一种无需重训练的零样本推理时概念擦除框架，通过在扩散过程之前对文本嵌入进行校准向量减法，结合Co-Occurrence Encoding处理多概念擦除和视觉反馈环路解决潜在概念持久性问题，在物体/NSFW/风格/名人擦除任务上全面超越SOTA。

**[System-Embedded Diffusion Bridge Models](image_generation/system-embedded_diffusion_bridge_models.md)**

:   提出System-embedded Diffusion Bridge Models（SDB），将已知的线性测量系统直接嵌入矩阵值SDE的系数中，实现了对值域空间去噪和零空间信息合成的分离控制，在多种逆问题上取得一致性提升并展现出强大的系统失配鲁棒性。

**[Understanding Representation Dynamics of Diffusion Models via Low-Dimensional Models](image_generation/understanding_representation_dynamics_of_diffusion_models_via_low-dimensional_mo.md)**

:   在低秩高斯混合（MoLRG）数据模型下，理论证明了扩散模型表示质量随噪声水平呈单峰动态的现象源于去噪强度与类别区分度的权衡，并实证发现单峰动态的出现可作为模型泛化能力的可靠指标。

**[Watermarking Autoregressive Image Generation](image_generation/watermarking_autoregressive_image_generation.md)**

:   首次将 LLM 水印技术（KGW green/red scheme）适配到自回归图像生成模型的 token 层，识别并解决了关键挑战——反向循环一致性（RCC）不足，通过 tokenizer-detokenizer 微调和水印同步层实现了鲁棒的、具有理论保证的图像水印检测。

**[Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training](image_generation/why_diffusion_models_dont_memorize_the_role_of_implicit_dynamical_regularization.md)**

:   通过数值实验和理论分析揭示扩散模型训练中存在两个关键时间尺度——泛化时间 $\tau_{\text{gen}}$ 和记忆化时间 $\tau_{\text{mem}}$，后者随训练集大小 $n$ 线性增长而前者保持恒定，由此产生的隐式动力学正则化使模型即使在高度过参数化情况下也能通过早停避免记忆化。

**[Why Diffusion Models Don't Memorize: The Role of Implicit Regularization](image_generation/why_diffusion_models_dont_memorize_the_role_of_implicit_regularization.md)**

:   本文从数值实验和理论分析两个层面揭示扩散模型训练中存在**隐式动态正则化**机制：生成高质量样本的时间尺度 τ_gen 与出现记忆化的时间尺度 τ_mem 之间的间隔随训练集大小 n 线性增长，为"早停"提供了理论支撑。

---

## 💬 LLM / NLP { #llm_nlp }

**[AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play](llm_nlp/acesearcher_bootstrapping_reasoning_and_search_for_llms_via_reinforced_self-play.md)**

:   提出 AceSearcher——一种协作式自我博弈框架，让单个 LLM 同时扮演**问题分解者**（将复杂查询拆解为子问题引导检索）和**求解者**（整合检索上下文生成答案），通过 SFT + 迭代 DPO 两阶段训练，仅用最终答案作为奖励信号，在 10 个数据集上平均 EM 提升 7.6%，32B 模型匹配 DeepSeek-V3（<5% 参数）。

**[Active Slice Discovery in Large Language Models](llm_nlp/active_slice_discovery_in_large_language_models.md)**

:   提出 **Active Slice Discovery** 问题框架，将主动学习引入 LLM 错误切片发现，利用不确定性采样 + LLM 内部表征（原始 embedding 或 SAE 特征）在仅使用 2-10% 标注的情况下达到接近全标注的切片检测精度。

**[AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners](llm_nlp/adastar_adaptive_data_sampling_for_training_self-taught_reasoners.md)**

:   发现 STaR（自我教学推理器）的随机数据采样导致观测训练频率严重不平衡（简单题过度训练、难题训练不足），提出 AdaSTaR——通过自适应多样性采样（优先欠训练样本）和自适应课程采样（根据模型强度调节难度），在 6 个基准上全部取得最高准确率同时减少 58.6% 训练 FLOPs。

**[AI Progress Should Be Measured by Capability-Per-Resource, Not Scale Alone: A Framework for Gradient-Guided Resource Allocation in LLMs](llm_nlp/ai_progress_should_be_measured_by_capability-per-resource_not_scale_alone_a_fram.md)**

:   本文以 position paper 的形式挑战"规模至上主义"，提出以**能力-每-资源（Capability-Per-Resource, CPR）**取代单纯的规模扩张来衡量 AI 进步，并给出一套基于梯度引导的资源分配理论框架——通过发布"梯度蓝图"元数据，使下游适配者仅微调高影响力参数子集即可在资源占用大幅降低的同时保持接近全参数微调的性能。

**[Are Language Models Efficient Reasoners? A Perspective from Logic Programming](llm_nlp/are_language_models_efficient_reasoners_a_perspective_from_logic_programming.md)**

:   从逻辑编程角度提出评估 LLM 推理效率（而非仅正确性）的框架——通过 verbalized logic program 将自然语言证明映射到逻辑程序证明，发现当前 LLM 在含无关公理的数学题中不仅准确率下降，且推理过程严重低效（超过一半的推理步骤是不必要的）。

**[ARECHO: Autoregressive Evaluation via Chain-Based Hypothesis Optimization for Speech Multi-Metric Estimation](llm_nlp/arecho_autoregressive_evaluation_via_chain-based_hypothesis_optimization_for_spe.md)**

:   ARECHO 将语音多指标评估建模为链式自回归 token 预测任务——设计统一的语音信息 token 化管线处理 87 个异质指标（数值/类别/有界/无界），通过动态分类链显式捕捉指标间依赖关系（如可懂度-自然度相关性），配合两步置信度导向解码减少误差传播，在增强/生成/噪声三类语音评估中全面超越 UniVERSA 基线（Avg Test MSE 23.26 vs 96.99，-76%）。

**[AstroVisBench: A Code Benchmark for Scientific Computing and Visualization in Astronomy](llm_nlp/astrovisbench_a_code_benchmark_for_scientific_computing_and_visualization_in_ast.md)**

:   AstroVisBench 构建了首个评估 LLM 天文科学计算和可视化能力的代码基准——从 110 个 Jupyter Notebook 提取 864 个任务（处理+可视化），设计双重评估管线（执行式变量检查 + VLM-as-Judge 可视化评分，与专家 Spearman ρ=0.822），评测 8 个 SOTA 模型后发现 Gemini 2.5 Pro 最佳但无错误率仅 15.7%，FileNotFoundError 占 43% 错误。

**[ARC-JSD: Attributing Response to Context via Jensen-Shannon Divergence Driven Mechanistic Study](llm_nlp/attributing_response_to_context_a_jensen-shannon_divergence_driven_mechanistic_s.md)**

:   ARC-JSD 提出基于 Jensen-Shannon 散度的 RAG 上下文归因方法——通过比较有/无特定上下文句子时模型输出分布的 JSD 差异，无需微调/梯度计算即可定位回答所依赖的上下文，计算效率比 baseline 快 3 倍，Top-1 归因准确率平均提升 10.7%，并通过 Logit Lens 揭示归因相关的注意力头集中在高层。

**[Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in LLMs](llm_nlp/auto-search_and_refinement_an_automated_framework_for_gender_bias_mitigation_in_.md)**

:   提出 FaIRMaker 框架，通过"自动搜索+精化"范式先用梯度优化找到去偏见触发词（Fairwords），再训练 seq2seq 模型将其转化为可读指令，在开源和闭源 LLM 上有效缓解性别偏见同时保持甚至提升任务性能。

**[Belief-Calibrated Multi-Agent Consensus Seeking for Complex NLP Tasks](llm_nlp/belief-calibrated_multi-agent_consensus_seeking_for_complex_nlp_tasks.md)**

:   提出 Belief-Calibrated Consensus Seeking (BCCS) 框架，通过引入信念（belief）校准的共识判断、冲突感知的协作者分配和领导者选择三个模块，让多智能体系统在复杂NLP任务上达成更稳定的共识，在 MATH 和 MMLU 上的困难任务分别提升 2.23% 和 3.95%。

**[Benchmarking Large Language Models for Zero-Shot and Few-Shot Phishing URL Detection](llm_nlp/benchmarking_large_language_models_for_zero-shot_and_few-shot_phishing_url_detec.md)**

:   在统一的零样本和少样本 prompt 框架下系统评估 GPT-4o、Claude-3.7 和 Grok-3-Beta 三个商用 LLM 在钓鱼 URL 检测任务上的表现，发现少样本 prompt 可显著提升所有模型性能，Grok-3-Beta 在平衡数据集上取得最佳 F1（0.9399），但不同模型在精度-召回率权衡上呈现差异化行为模式。

**[Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits](llm_nlp/beyond_components_singular_vector-based_interpretability_of_transformer_circuits.md)**

:   提出基于SVD奇异向量的方向级可解释性框架，通过对注意力头和MLP的增广矩阵统一SVD分解+可学习对角掩码（KL+L₁），发现单组件内存在正交低秩子函数叠加——IOI任务仅需~9%方向即可KLD=0.21复现模型行为。

**[Beyond the Singular: Revealing the Value of Multiple Generations in Benchmark Evaluation](llm_nlp/beyond_the_singular_revealing_the_value_of_multiple_generations_in_benchmark_eva.md)**

:   将LLM基准评测形式化为层级统计模型，理论证明多次随机生成（k>1）能降低benchmark分数估计方差，并引入prompt级难度指标$\mathbb{P}(\text{correct})$和数据地图用于基准质量控制。

**[Beyond The Surface Enhancing Llm-As-A-Judge Alignment With Human Via Internal Re](llm_nlp/beyond_the_surface_enhancing_llm-as-a-judge_alignment_with_human_via_internal_re.md)**

:   提出LAGER框架，通过聚合LLM中间层到最终层的score token logits并计算期望分数，无需微调模型即可将LLM评判与人类评分的对齐度提升最高7.5%，且不需要思维链推理步骤就能匹配或超过推理类方法。

**[Beyond Token Probes Hallucination Detection Via Activation Tensors With Act-Vit](llm_nlp/beyond_token_probes_hallucination_detection_via_activation_tensors_with_act-vit.md)**

:   将LLM的全部隐层激活组织为"激活张量"（层×token×隐维度），类比图像用ViT处理，设计ACT-ViT架构支持跨LLM联合训练，在15个LLM-数据集组合上一致超越传统probing方法，并展现出对未见数据集和未见LLM的强零样本/少样本迁移能力。

**[Bigram Subnetworks Mapping To Next Tokens In Transformer Language Models](llm_nlp/bigram_subnetworks_mapping_to_next_tokens_in_transformer_language_models.md)**

:   通过连续稀疏化在Transformer语言模型中找到仅包含~10M参数的bigram子网络，它们集中在第一个MLP层，足以复现bigram预测（$r>0.95$），且被消融后模型性能大幅下降，证明这些子网络是语言模型中既必要又充分的最小next-token预测电路。

**[Born a Transformer – Always a Transformer? On the Effect of Pretraining on Architectural Abilities](llm_nlp/born_a_transformer_--_always_a_transformer_on_the_effect_of_pretraining_on_archi.md)**

:   通过系统性地研究检索和复制任务家族，揭示了大规模预训练会为Transformer引入方向性偏置（右/前向优于左/后向），但无法克服非唯一任务上的根本架构限制；微调可消除方向偏置但不能突破架构表达力边界。

**[Breaking The Frozen Subspace Importance Sampling For Low-Rank Optimization In Ll](llm_nlp/breaking_the_frozen_subspace_importance_sampling_for_low-rank_optimization_in_ll.md)**

:   发现GaLore等低秩优化方法的主导子空间在预训练中会"冻结"（相邻子空间重叠度趋近1），导致权重更新卡在固定低秩子空间中；提出SARA（重要性采样子空间选择），按奇异值权重随机采样奇异向量构建子空间，证明收敛性的同时将低秩优化器与全秩Adam的性能差距缩小最高46%。

**[Bridging Human And Llm Judgments Understanding And Narrowing The Gap](llm_nlp/bridging_human_and_llm_judgments_understanding_and_narrowing_the_gap.md)**

:   提出Bridge统计框架，通过序数logistic回归建模人类和LLM评判之间的潜在关系，以少量人类标签改善LLM评判的校准和对齐，同时支持对系统性偏差的正式统计检验。

**[Broken Tokens: Your Language Model Can Secretly Handle Non-Canonical Tokenization](llm_nlp/broken_tokens_your_language_model_can_secretly_handle_non-canonical_tokenization.md)**

:   揭示 LLM 能秘密处理非标准分词（如将"Hello"拆为"He"+"llo"而非标准的"Hello"整词token）——即使输入的 token 序列与训练时不同，模型表现出惊人的鲁棒性，且这种能力来自嵌入空间中子词嵌入的线性组合近似整词嵌入的特性。

**[C²Prompt: Class-aware Client Knowledge Interaction for Federated Continual Learning](llm_nlp/c2prompt_class-aware_client_knowledge_interaction_for_federated_continual_learni.md)**

:   针对联邦持续学习中prompt通信时的类级知识不一致问题，提出C²Prompt方法，通过局部类分布补偿（LCDC）和类感知prompt聚合（CPA）两个机制显式增强跨客户端的类级知识一致性，在ImageNet-R上Avg准确率达87.20%，超出SOTA Powder 2.51%。

**[Can Large Language Models Master Complex Card Games?](llm_nlp/can_large_language_models_master_complex_card_games.md)**

:   系统评估LLM在8种复杂卡牌游戏上的学习能力，发现通过高质量游戏数据的SFT，LLM可以接近强游戏AI的水平，并能同时掌握多个游戏，但通用能力会下降（可通过混入通用指令数据缓解）。

**[CAT: Circular-Convolutional Attention for Sub-Quadratic Transformers](llm_nlp/cat_circular-convolutional_attention_for_sub-quadratic_transformers.md)**

:   本文提出CAT（Circular-convolutional Attention），通过FFT计算循环卷积将Self-Attention复杂度从O(N²)降至O(N log N)，同时保持完整的softmax机制和全局注意力。

**[CBMAS: Cognitive Behavioral Modeling via Activation Steering](llm_nlp/cbmas_cognitive_behavioral_modeling_via_activation_steering.md)**

:   CBMAS 提出一个连续激活干预诊断框架，将传统“前后对比式”认知偏差分析扩展为可解释的干预轨迹分析，通过 alpha 强度扫描、logit-lens 偏置曲线与层位敏感性分析，揭示 LLM 行为翻转临界点与跨层演化机制。

**[Characterizing the Expressivity of Fixed-Precision Transformer Language Models](llm_nlp/characterizing_the_expressivity_of_fixed-precision_transformer_language_models.md)**

:   精确刻画了固定精度、严格未来掩码、软注意力、无位置编码的 Transformer 的表达能力——恰好等价于仅含过去算子的线性时态逻辑 LTL[P]，并将其与偏序确定有限自动机 (PODFA)、$\mathcal{R}$-trivial 幺半群统一起来。

**[CodeAssistBench (CAB): Dataset & Benchmarking for Multi-turn Chat-Based Code Assistance](llm_nlp/codeassistbench_cab_dataset_benchmarking_for_multi-turn_chat-based_code_assistan.md)**

:   提出 CodeAssistBench (CAB)，第一个评估多轮、项目级编程辅助的全自动 Benchmark，从 GitHub Issues 自动构建 3,286 个真实编程求助场景，涵盖 7 种语言 214 个仓库，揭示 SOTA 模型在 StackOverflow 问题上 70-83% 但在 post-cutoff 仓库上仅 7-16% 的巨大鸿沟。

**[ComPO: Preference Alignment via Comparison Oracles](llm_nlp/compo_preference_alignment_via_comparison_oracles.md)**

:   针对DPO中噪声偏好对（preferred和dispreferred响应相似）导致的似然位移和冗长问题，提出基于比较oracle的零阶偏好对齐方法ComPO，将数据分为干净/噪声子集，用DPO处理干净数据、用ComPO提取噪声数据中的信号，在AlpacaEval 2等benchmark上持续提升LC win rate。

**[Composing Linear Layers from Irreducibles](llm_nlp/composing_linear_layers_from_irreducibles.md)**

:   利用Clifford代数，将线性层表示为二向量（bivector）的组合——即旋量（rotor）的三明治乘积——仅需 $O(\log^2 d)$ 参数即可替代 $d \times d$ 密集矩阵，应用于LLM注意力层的Q/K/V投影时性能接近原始模型和强基线。

**[ConfTuner: Training Large Language Models to Express Their Confidence Verbally](llm_nlp/conftuner_training_large_language_models_to_express_their_confidence_verbally.md)**

:   ConfTuner 提出 tokenized Brier score 损失函数（理论证明为 proper scoring rule），仅需 2000 个样本 + 4 分钟 LoRA 微调即可让 LLM 输出校准的语言化置信度（如"我80%确定"），ECE 最大降低 60.9%，支持自我纠错和模型级联等下游应用。

**[CoRe: Benchmarking LLMs' Code Reasoning Capabilities through Static Analysis Tasks](llm_nlp/core_benchmarking_llms_code_reasoning_capabilities_through_static_analysis_tasks.md)**

:   提出 CoRe，一个包含 12,553 个人工验证任务实例的高质量 benchmark，通过数据依赖、控制依赖和信息流三类静态分析基础任务，直接评估 LLM 的代码语义推理能力，揭示模型在 trace 生成和源枚举等需要多步推理的任务上仍严重不足。

**[Cultural Alien Sampler: Open-ended Art Generation Balancing Originality and Coherence](llm_nlp/cultural_alien_sampler_open-ended_art_generation_balancing_originality_and_coher.md)**

:   提出Cultural Alien Sampler (CAS)——用两个GPT-2模型分别建模"概念一致性"和"文化典型性"，通过选择高一致性但低文化典型性的概念组合来生成原创且和谐的艺术创意，在人类评估中接近艺术专业学生水平并远超GPT-4o。

**[DATE-LM: Benchmarking Data Attribution Evaluation for Large Language Models](llm_nlp/date-lm_benchmarking_data_attribution_evaluation_for_large_language_models.md)**

:   DATE-LM是首个统一、应用驱动的LLM数据归因基准，涵盖数据选择、毒性过滤、事实归因三大应用，通过公开排行榜促进可复现和公平的方法比较。

**[DCAD-2000: A Multilingual Dataset across 2000+ Languages with Data Cleaning as Anomaly Detection](llm_nlp/dcad-2000_a_multilingual_dataset_across_2000_languages_with_data_cleaning_as_ano.md)**

:   构建覆盖2282种语言、46.72TB文本的多语言数据集DCAD-2000，提出将数据清洗重构为异常检测问题的语言无关框架，通过8维统计特征+Isolation Forest动态过滤噪声数据，在多个多语言benchmark上验证效果，尤其对低资源语言提升显著。

**[Decoupled Entropy Minimization](llm_nlp/decoupled_entropy_minimization.md)**

:   将经典熵最小化（EM）解耦为两个对立部分——Cluster Aggregation Driving Factor (CADF，奖励主导类别)和 Gradient Mitigation Calibrator (GMC，惩罚高置信类别)，揭示了经典 EM 的两个固有缺陷（reward collapse 和 easy-class bias），提出 AdaDEM 通过归一化奖励和边际熵校准来修复这些问题，在半监督学习、域适应、强化学习等多任务上显著提升。

**[Deep Learning for Continuous-Time Stochastic Control with Jumps](llm_nlp/deep_learning_for_continuous-time_stochastic_control_with_jumps.md)**

:   提出两种基于模型的深度学习算法（GPI-PINN 和 GPI-CBU）来求解含跳跃的有限时域连续时间随机控制问题，通过迭代训练策略网络和价值网络，避免了状态动力学的离散化和模拟，在高维场景中表现出色。

**[Demystifying Language Model Forgetting With Low-Rank Example Associations](llm_nlp/demystifying_language_model_forgetting_with_low-rank_example_associations.md)**

:   发现LLM微调后上游样本遗忘与新学任务之间的关联矩阵具有低秩结构（rank-3即$R^2>0.69$），利用矩阵补全预测未见任务导致的遗忘，指导选择性回放以减轻遗忘。

**[Detecting High-Stakes Interactions with Activation Probes](llm_nlp/detecting_high-stakes_interactions_with_activation_probes.md)**

:   用线性激活探针（在 LLM 内部表示上训练的轻量分类器）检测用户的"高风险交互"，在合成数据上训练后跨 6 个真实数据集 AUROC 达 0.88-0.92，匹敌 8-12B 微调 LLM但计算成本低 6 个数量级，级联架构（探针初筛+LLM 精判）进一步超越单独使用任一方法。

**[Disaggregation Reveals Hidden Training Dynamics: The Case of Agreement Attraction](llm_nlp/disaggregation_reveals_hidden_training_dynamics_the_case_of_agreement_attraction.md)**

:   通过将聚合的语法评测指标**分解**到实验条件层面并追踪训练过程中的变化，发现语言模型的语法学习并非渐进单调的，而是经历了一系列**隐藏的突破阶段**——先学习词频偏好、再学习局部上下文（n-gram），最后逐步掌握更远距离的语法依赖关系。

**[Do Different Prompting Methods Yield a Common Task Representation in Language Models?](llm_nlp/do_different_prompting_methods_yield_a_common_task_representation_in_language_mo.md)**

:   本文扩展函数向量方法至指令提示，发现演示和指令诱发的任务表示主要不同，仅部分重叠，解释了为何结合两者效果更优。

**[Do Language Models Use Their Depth Efficiently?](llm_nlp/do_language_models_use_their_depth_efficiently.md)**

:   通过因果干预、残差流分析和跨模型线性映射，证明当前 LLM 后半部分层不参与组合式计算，仅迭代细化输出概率分布，深层模型只是把浅层模型的计算"展延"到更多层。

**[Does Object Binding Naturally Emerge in Large Pretrained Vision Transformers?](llm_nlp/does_object_binding_naturally_emerge_in_large_pretrained_vision_transformers.md)**

:   通过定义 IsSameObject 谓词并设计二次探针，证明大规模预训练 ViT（尤其是 DINO、CLIP）自然涌现了目标绑定能力，该信号编码在低维子空间中并主动引导注意力机制，挑战了认知科学界认为 ViT 缺乏绑定能力的观点。

**[Don't Be Lazy: CompleteP Enables Compute-Efficient Deep Transformers](llm_nlp/dont_be_lazy_completep_enables_compute-efficient_deep_transformers.md)**

:   CompleteP 参数化（α=1）是唯一同时实现深度方向超参转移和完全特征学习的方案，在深模型上相比 μP 节省 12-34% FLOPs。

**[Emergence of Linear Truth Encodings in Language Models](llm_nlp/emergence_of_linear_truth_encodings_in_language_models.md)**

:   提出 **Truth Co-occurrence Hypothesis (TCH)**——真实陈述倾向于与其他真实陈述共现——并通过一个最简单的单层 Transformer 玩具模型，端到端地展示了线性真值子空间如何通过两阶段训练动态（先记忆 → 后编码真值）自然涌现，为理解 LLM 中广泛报告的线性真值表示提供了首个机制性解释。

**[EnCompass: Enhancing Agent Programming with Search Over Program Execution Paths](llm_nlp/encompass_enhancing_agent_programming_with_search_over_program_execution_paths.md)**

:   提出 Probabilistic Angelic Nondeterminism (PAN) 编程模型及 EnCompass Python 框架，将 agent 的核心工作流逻辑与推理时搜索策略解耦，程序员只需在 LLM 调用处加 `branchpoint()` 标记，即可用几行参数切换 best-of-N、beam search、tree search 等策略，代码修改量减少 3-6x。

**[Enhancing Multilingual LLM Pretraining with Model-Based Data Selection](llm_nlp/enhancing_multilingual_llm_pretraining_with_model-based_data_selection.md)**

:   提出一套透明、简洁、高效的多语言模型驱动数据筛选框架，利用 FastText 和 Transformer（XLM-RoBERTa）嵌入分类器识别结构化且知识丰富的样本，在 FineWeb-2 数据集上仅用 15% 的 token 即可匹配基线 MMLU 分数，并将该框架扩展至 20 种语言并公开发布了精炼的预训练数据集。

**[Enhancing Training Data Attribution with Representational Optimization](llm_nlp/enhancing_training_data_attribution_with_representational_optimization.md)**

:   提出 AirRep（Attentive Influence Ranking Representation），一种基于表示学习的训练数据归因方法，通过可训练编码器和注意力池化机制，在推理效率比梯度方法快约 80 倍的同时，达到甚至超越 SOTA 梯度方法的归因精度。

**[EvaLearn: Quantifying the Learning Capability and Efficiency of LLMs via Sequential Problem Solving](llm_nlp/evalearn_quantifying_the_learning_capability_and_efficiency_of_llms_via_sequenti.md)**

:   提出 EvaLearn 基准，通过**序列化问题求解**范式评估 LLM 的学习能力和学习效率，揭示静态能力强的模型不一定具备更强的学习潜力。

**[Evaluating Multiple Models Using Labeled and Unlabeled Data](llm_nlp/evaluating_multiple_models_using_labeled_and_unlabeled_data.md)**

:   提出 **SSME (Semi-Supervised Model Evaluation)**，利用少量标注数据和大量未标注数据，通过半监督混合模型估计多个分类器联合分布 $P(y, \mathbf{s})$，实现精确的分类器性能评估，误差降低至仅用标注数据的 1/5。

**[EvoRefuse: Evolutionary Prompt Optimization for Evaluation and Mitigation of LLM Over-Refusal](llm_nlp/evorefuse_evolutionary_prompt_optimization_for_evaluation_and_mitigation_of_llm_.md)**

:   提出 EvoRefuse——用进化搜索（变异/重组 + ELBO 适应度 + 模拟退火）生成语义无害但能可靠触发 LLM 拒绝的"伪恶意"指令，比最强基线的拒绝触发率高 85.34%，并用生成的数据进行 SFT/DPO 微调，将过度拒绝降低 29.85%-45.96%。

**[Exploiting Vocabulary Frequency Imbalance in Language Model Pre-training](llm_nlp/exploiting_vocabulary_frequency_imbalance_in_language_model_pre-training.md)**

:   通过控制实验揭示大词表提升语言模型性能的根本机制：**扩大词表降低分词文本的 Kolmogorov 复杂度，利用词频不平衡让高频词损失大幅下降，驱动全局交叉熵下降和下游任务提升**。

**[Gemstones: A Model Suite for Multi-Faceted Scaling Laws](llm_nlp/gemstones_a_model_suite_for_multi-faceted_scaling_laws.md)**

:   Gemstones开源4000+检查点数据集（至2B参数），系统研究宽度-深度-训练代币在缩放律中的影响，揭示缩放律对设计选择的高度敏感性。

**[GeoCAD: Local Geometry-Controllable CAD Generation with Large Language Models](llm_nlp/geocad_local_geometry-controllable_cad_generation_with_large_language_models.md)**

:   提出 GeoCAD，首个实现局部几何可控 CAD 生成的方法，通过互补标注策略为局部零件生成几何指令，并微调 LLM 实现根据用户文本指令精确修改 CAD 模型的局部部分。

**[Global Minimizers of Sigmoid Contrastive Loss](llm_nlp/global_minimizers_of_sigmoid_contrastive_loss.md)**

:   首次在实践相关的 N≫d 区间严格刻画了 Sigmoid 对比损失（SigLIP）在可训练温度和偏置下的全局最小值几何结构，提出了 (m, b_rel)-Constellation 这一新型组合对象，并用其解释了 SigLIP 的检索成功、模态间隙现象，以及提出了显式 relative bias 参数化改进训练动态。

**[Hierarchical Retrieval: The Geometry and a Pretrain-Finetune Recipe](llm_nlp/hierarchical_retrieval_the_geometry_and_a_pretrain-finetune_recipe.md)**

:   研究双编码器（Dual Encoder）在层次化检索（Hierarchical Retrieval）中的可行性，理论证明嵌入维度只需与层次深度线性、文档数对数增长即可求解，并发现"远距离丢失"现象后提出预训练-微调策略，在 WordNet 上将远距离召回率从 19% 提升至 76%。

**[How Do Transformers Learn Implicit Reasoning?](llm_nlp/how_do_transformers_learn_implicit_reasoning.md)**

:   通过符号环境的精细控制研究，本文发现多跳隐式推理会经历记忆→分布内泛化→跨分布泛化三阶段，关键机制是中间实体表示在余弦空间的聚类。

**[HybridNorm: Towards Stable and Efficient Transformer Training via Hybrid Normalization](llm_nlp/hybridnorm_towards_stable_and_efficient_transformer_training_via_hybrid_normaliz.md)**

:   提出 HybridNorm 混合归一化策略——注意力模块用 QKV 归一化解耦梯度、FFN 用 Post-Norm 增强正则化，在 550M-7B 规模上同时获得 Pre-Norm 的训练稳定性和 Post-Norm 的泛化性能，7B 模型下游任务平均提升 2.45%。

**[Hyperparameter Transfer Enables Consistent Gains Of Matrix-Preconditioned Optimi](llm_nlp/hyperparameter_transfer_enables_consistent_gains_of_matrix-preconditioned_optimi.md)**

:   研究矩阵预条件优化器（Shampoo/SOAP/Muon）的超参数随模型宽度和深度的缩放规则（基于 μP），发现正确的超参缩放是实现一致加速的关键：使用 μP + 1/width weight decay，三者在 190M 到 1.4B 参数的 Llama 模型上一致实现约 1.4× 加速。

**[In-Context Learning of Linear Dynamical Systems with Transformers: Approximation Bounds and Depth-Separation](llm_nlp/in-context_learning_of_linear_dynamical_systems_with_transformers_approximation_.md)**

:   分析了线性 Transformer 在噪声线性动力系统上的 ICL 近似能力：$O(\log T)$ 深度可达到 $O(\log T / T)$ 测试误差（接近最小二乘估计器），而单层线性 Transformer 存在不可消除的下界——揭示了非 IID 数据下的深度分离现象。

**[Ineq-Comp: Benchmarking Human-Intuitive Compositional Reasoning in Automated Theorem Proving on Inequalities](llm_nlp/ineq-comp_benchmarking_human-intuitive_compositional_reasoning_in_automated_theo.md)**

:   提出 Ineq-Comp 基准，通过对简单不等式种子问题施加人类直觉可轻松处理的组合变换（变量复制、代数重写），揭示当前 LLM 形式化定理证明器在组合推理上的根本性缺陷——即使 DeepSeek-Prover-V2-7B 也有 20%+ 的性能下降。

**[Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale](llm_nlp/language_model_behavioral_phases_are_consistent_across_archi.md)**

:   论文在 Transformer、Mamba、RWKV，不同数据集与参数规模（14M 到 12B）上系统分析 1400+ checkpoints，发现语言模型预训练中存在高度一致的行为阶段；词级行为变化最多可由 unigram 频率、n-gram 概率、语义相似度三类简单启发式解释（最高约 98% 方差）。

**[Large Language Models Miss the Multi-Agent Mark](llm_nlp/large_language_models_miss_the_multi-agent_mark.md)**

:   Position paper 指出当前 MAS LLMs 在四个方面违背了传统多智能体系统（MAS）的基本原则：LLM 缺乏原生社会行为、环境设计以 LLM 为中心、缺少异步协调和标准通信协议、涌现行为缺乏量化评估，并为每个问题提出研究方向。

**[LCDB 1.1: A Database Illustrating Learning Curves Are More Ill-Behaved Than Previously Thought](llm_nlp/lcdb_11_a_database_illustrating_learning_curves_are_more_ill-behaved_than_previo.md)**

:   构建了大规模高分辨率学习曲线数据库 LCDB 1.1，证明样本学习曲线的"病态行为"（非单调、非凸）比此前认为的普遍两倍，约 15% 的曲线显著不良，且特征缩放难以修复。

**[Learning the Wrong Lessons: Syntactic-Domain Spurious Correlations in Language Models](llm_nlp/learning_the_wrong_lessons_syntactic-domain_spurious_correlations_in_language_mo.md)**

:   揭示 LLM 学会了句法模板（PoS n-gram）与领域之间的虚假关联，导致跨域性能骤降，甚至可利用此关联绕过安全拒绝机制（refusal bypass），在 OLMo-2 上将拒绝率从 40% 降至 2.5%。

**[Leveraging Importance Sampling to Detach Alignment Modules from Large Language Models](llm_nlp/leveraging_importance_sampling_to_detach_alignment_modules_from_large_language_m.md)**

:   提出 Residual Alignment Model (RAM)，将 LLM 对齐过程形式化为重要性采样，将大模型分解为冻结的 Proposal Module 和可训练的小型 Residual Aligner，以不到 1/8 参数实现可比甚至超越全参数 SFT/DPO 的对齐效果，同时解决了首 token 延迟问题。

**[Leveraging Robust Optimization for LLM Alignment under Distribution Shifts](llm_nlp/leveraging_robust_optimization_for_llm_alignment_under_distribution_shifts.md)**

:   提出 DoRA（Distribution-aware optimization for Robust Alignment），通过训练分布分类器为每个样本分配校准权重，结合 KL-DRO 框架最小化最坏情况损失，以模型无关的即插即用方式提升多种对齐算法在分布偏移下的鲁棒性，在 DPO/RRHF/LIRE 等基线上一致提升性能。

**[Linear Transformers Implicitly Discover Unified Numerical Algorithms](llm_nlp/linear_transformers_implicitly_discover_unified_numerical_algorithms.md)**

:   训练线性 Transformer 执行矩阵块补全任务后，通过权重代数分析发现模型在三种完全不同的计算约束（集中式、分布式、计算受限）下隐式收敛到同一个双行迭代更新规则 EAGLE，该规则具有二阶收敛性且依赖条件数仅为对数级别。

**[LLM Probing with Contrastive Eigenproblems: Improving Understanding and Applicability of CCS](llm_nlp/llm_probing_with_contrastive_eigenproblems_improving_understanding_and_applicabi.md)**

:   本文对无监督探测方法 CCS（Contrast-Consistent Search）进行了深入分析，提出将 CCS 重新表述为特征值问题（Contrastive Eigenproblems），获得闭式解和可解释的特征值，避免了 CCS 对随机初始化的敏感性，并自然扩展到多变量设置。

**[LTD-Bench: Evaluating Large Language Models by Letting Them Draw](llm_nlp/ltd-bench_evaluating_large_language_models_by_letting_them_draw.md)**

:   LTD-Bench 通过让 LLM 画画（生成点阵或代码绘图）来评估其空间推理能力，将抽象的评分指标转化为直观可视的输出，揭示了当前先进 LLM 在建立语言与空间概念双向映射方面的严重不足。

**[Memory Mosaics at Scale](llm_nlp/memory_mosaics_at_scale.md)**

:   Memory Mosaics v2 将关联存储网络扩展至 10B 参数、1T token 训练规模，在新任务学习和上下文学习上显著超越同规模甚至 8T token 训练的 Transformer。

**[MergeBench: A Benchmark for Merging Domain-Specialized LLMs](llm_nlp/mergebench_a_benchmark_for_merging_domain-specialized_llms.md)**

:   MergeBench 是首个全面评估大规模领域特化 LLM 合并的基准套件，覆盖 Llama 和 Gemma 系列最大 9B 模型、五大任务领域和八种合并方法，从多任务性能、遗忘、运行效率三个维度提供系统化评估和实用指南。

**[MetaMind: Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems](llm_nlp/metamind_modeling_human_social_thoughts_with_metacognitive_multi-agent_systems.md)**

:   提出 MetaMind——一个受心理学元认知理论启发的多智能体框架，通过 ToM Agent（心理状态假设生成）、Moral Agent（社会规范约束精炼）和 Response Agent（响应生成与自我验证）三阶段协作，显著提升 LLM 的社会推理能力，在多个社会智能基准上达到 SOTA 并首次接近人类水平。

**[Mind the Gap: Removing the Discretization Gap in Differentiable Logic Gate Networks](llm_nlp/mind_the_gap_removing_the_discretization_gap_in_differentiable_logic_gate_networ.md)**

:   提出 Gumbel Logic Gate Networks (Gumbel LGNs)，通过在逻辑门选择中注入 Gumbel 噪声并使用直通估计器 (ST estimator)，将可微逻辑门网络的离散化差距减少 98%，训练速度提升 4.5 倍，未使用神经元比例降为 0%。

**[MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](llm_nlp/mitra_an_ai_assistant_for_knowledge_retrieval_in_physics_collaborations.md)**

:   提出 MITRA，一个面向大型物理实验协作（如 CERN CMS）的本地化 RAG 系统，采用两层向量数据库架构（摘要库 + 全文库）和完全本地部署策略，在语义检索任务上显著优于传统关键词搜索（BM25），Precision@1 从 0.13 提升至 0.75。

**[MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research](llm_nlp/mlr-bench_evaluating_ai_agents_on_open-ended_machine_learning_research.md)**

:   提出 MLR-Bench，一个包含 201 个开放式 ML 研究任务的综合基准，配套 MLR-Judge（LLM 评审框架）和 MLR-Agent（模块化研究代理），发现当前最先进的编码代理在约 80% 的情况下会生成伪造或未验证的实验结果，揭示了 AI 自动化科学研究的核心瓶颈。

**[MonarchAttention: Zero-Shot Conversion to Fast, Hardware-Aware Structured Attention](llm_nlp/monarchattention_zero-shot_conversion_to_fast_hardware-aware_structured_attentio.md)**

:   提出 MonarchAttention，利用 Monarch 矩阵的结构化特性，通过 softmax 变分形式的交替优化，实现 $\Theta(N\sqrt{N}d)$ 复杂度的注意力近似，无需额外训练即可零样本替换预训练 Transformer 的注意力层，同时在 GPU 上相比 FlashAttention-2 实现 1.4×–8.2× 的加速。

**[Monte Carlo Expected Threat (MOCET) Scoring](llm_nlp/monte_carlo_expected_threat_mocet_scoring.md)**

:   提出 MOCET（Monte Carlo Expected Threat）评分框架，通过将 LLM 生成的生物武器制造协议分解为逐步 Bernoulli 试验，结合 k-NN 语义嵌入的成功概率估计和蒙特卡洛模拟，生成可解释的、可自动化的威胁量化指标，用于衡量 LLM 在生物安全领域的真实世界风险。

**[MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery](llm_nlp/moose-chem2_exploring_llm_limits_in_fine-grained_scientific_hypothesis_discovery.md)**

:   将细粒度科学假设生成形式化为组合优化问题，提出层次启发式搜索（HHS）——利用 LLM 的成对比较作为梯度信号在假设空间中导航，层次化抽象平滑奖励景观减少局部最优陷阱，在 2024 年后化学论文 51 篇的专家标注 benchmark 上 Soft Recall 从 19.99% 提升到 40.35%。

**[msf-CNN: Patch-based Multi-Stage Fusion with Convolutional Neural Networks for TinyML](llm_nlp/msf-cnn_patch-based_multi-stage_fusion_with_convolutional_neural_networks_for_ti.md)**

:   提出 msf-CNN，一种基于有向无环图（DAG）最短路径算法的多阶段 patch-based 融合优化技术，通过高效搜索 CNN 的最优融合配置，在各种微控制器（ARM Cortex-M、RISC-V、ESP32）上实现比现有方法（MCUNetV2、StreamNet）减少 50%–87% 的峰值 RAM 使用，同时保持可控的计算开销。

**[MuRating: A High Quality Data Selecting Approach to Multilingual Large Language Model Pretraining](llm_nlp/murating_a_high_quality_data_selecting_approach_to_multilingual_large_language_m.md)**

:   提出 MuRating，一个可扩展的多语言数据选择框架：先通过配对比较聚合多个英文数据质量评分器，再借助翻译将质量信号迁移到 17 种语言，训练出语言无关的多语言质量评估模型，在 1.2B 和 7B 规模 LLM 预训练中取得了持续的性能提升。

**[Nemotron-CLIMB: CLustering-based Iterative Data Mixture Bootstrapping for Language Model Pre-training](llm_nlp/nemotron-climb_clustering-based_iterative_data_mixture_bootstrapping_for_languag.md)**

:   NVIDIA 提出 CLIMB 框架，通过嵌入聚类 + 迭代自举搜索自动发现最优预训练数据混合比例，在 1B 模型上超过 Llama-3.2-1B 达 2.0%，并发布了 1.2T token 的 ClimbLab 语料库和 400B token 的 ClimbMix 高质量数据集。

**[Nemotron-Flash: Towards Latency-Optimal Hybrid Small Language Models](llm_nlp/nemotron-flash_towards_latency-optimal_hybrid_small_language_models.md)**

:   Nemotron-Flash 通过系统优化深宽比、进化搜索混合算子组合（DeltaNet+Mamba2+Attention）以及权重归一化训练，构建延迟最优的小语言模型家族，相比 Qwen3-1.7B/0.6B 分别实现 1.3×/1.9× 延迟下降与 +5.5% 平均准确率提升。

**[On Evaluating LLM Alignment by Evaluating LLMs as Judges](llm_nlp/on_evaluating_llm_alignment_by_evaluating_llms_as_judges.md)**

:   本文系统研究了 LLM 的生成能力与评估能力之间的一致性（GE-consistency），发现两者在强偏好预言机下高度相关（Spearman ρ=0.96），据此提出 AlignEval 基准——通过评估 LLM 作为评判者的能力来衡量其对齐水平，无需 LLM-as-Judge 直接评估模型输出，与 AlpacaEval/Arena-Hard 相当甚至更优。

**[On the Role of Hidden States of Modern Hopfield Network in Transformer](llm_nlp/on_the_role_of_hidden_states_of_modern_hopfield_network_in_transformer.md)**

:   本文突破现代 Hopfield 网络（MHN）与 Transformer 对应关系的绝热近似限制，发现保留 MHN 的隐状态动力学会在自注意力层中引入跨层注意力分数传播机制（Modern Hopfield Attention, MHA），不增加训练参数即可系统性改善 ViT 和 GPT-2 的性能，并从理论和实验上证明 MHA 有效缓解了深层 Transformer 的 rank collapse 问题。

**[Opinion Maximization in Social Networks by Modifying Internal Opinions](llm_nlp/opinion_maximization_in_social_networks_by_modifying_internal_opinions.md)**

:   本文研究社交网络中通过修改 k 个关键节点的内部意见来最大化整体意见的优化问题，提出了两种基于采样的近似算法（随机游走和森林采样）以及一种基于异步更新的精确算法 MIS，后者在理论上保证收敛到最优解，并在数千万节点的真实网络上展示了卓越的效率与精度。

**[OptiTree: Hierarchical Thoughts Generation with Tree Search for LLM Optimization Modeling](llm_nlp/optitree_hierarchical_thoughts_generation_with_tree_search_for_llm_optimization_.md)**

:   提出 OptiTree，通过构建建模树（modeling tree）组织运筹优化问题的层次化分类与建模思维，利用树搜索将复杂问题自适应分解为更简单的子问题序列，显著提升 LLM 在优化建模任务上的准确率（在多个困难基准上提升超过 10%）。

**[PaTH Attention: Position Encoding via Accumulating Householder Transformations](llm_nlp/path_attention_position_encoding_via_accumulating_householder_transformations.md)**

:   提出 PaTH（Position encoding via accumulating Householder Transformations），一种数据依赖的乘法位置编码方案，通过累积 Householder 变换替代 RoPE 的静态旋转矩阵，在理论表达力和实际语言建模性能上均优于 RoPE。

**[PluralisticBehaviorSuite: Stress-Testing Multi-Turn Adherence to Custom Behavioral Policies](llm_nlp/pluralistic_behavior_suite_stress-testing_multi-turn_adherence_to_custom_behavio.md)**

:   提出 PBSuite，一个包含 300 个行业定制行为策略和动态多轮对抗评估框架的评测套件，揭示了主流 LLM 在单轮设置下合规率高（违规 <4%），但在多轮对抗交互中合规性急剧下降（违规高达 84%）。

**[Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity](llm_nlp/polar_sparsity_high_throughput_batched_llm_inferencing_with_scalable_contextual_.md)**

:   揭示了 LLM 推理中稀疏性的"极性转移"现象——MLP 层稀疏性随 batch 增大而消失，而 attention head 稀疏性保持稳定且与 batch 无关，据此设计了 Selective Head Attention 及对应 GPU kernel，在大 batch 推理中实现高达 2.2x 的端到端加速。

**[Post Hoc Regression Refinement via Pairwise Rankings](llm_nlp/post_hoc_regression_refinement_via_pairwise_rankings.md)**

:   提出 RankRefine，一种模型无关的后处理回归改进方法，通过将基础回归器的预测与基于成对排序的估计进行逆方差加权融合，在无需重训练的情况下显著降低预测误差，仅需 20 次成对比较和通用 LLM 即可实现分子性质预测中高达 10% 的 MAE 相对减少。

**[Power Lines: Scaling Laws for Weight Decay and Batch Size in LLM Pre-training](llm_nlp/power_lines_scaling_laws_for_weight_decay_and_batch_size_in_llm_pre-training.md)**

:   提出了一套针对 LLM 预训练中权重衰减 $\lambda$ 和批大小 $B$ 的幂律缩放定律（power laws），通过 AdamW 时间尺度 $\tau$ 的概念统一了超参数缩放关系，使得在大规模训练前即可准确预测最优超参数。

**[PRESTO: Preimage-Informed Instruction Optimization for Prompting Black-Box LLMs](llm_nlp/presto_preimage-informed_instruction_optimization_for_prompting_black-box_llms.md)**

:   提出 PRESTO 框架，利用白盒 LLM 中 soft prompt 到 instruction 的 many-to-one 映射关系（preimage 结构），通过 score sharing、preimage-based initialization 和 score consistency regularization 三大组件，在相同查询预算下等效获得 14 倍的标注数据量，显著提升黑盒 LLM 的指令优化效率。

**[Probabilistic Token Alignment for Large Language Model Fusion](llm_nlp/probabilistic_token_alignment_for_large_language_model_fusion.md)**

:   将 LLM 融合中的 token 对齐问题重新建模为最优传输（Optimal Transport）问题，用动态 token 配对 + Sinkhorn 算法实现"软"概率对齐取代传统硬映射，在 6 大基准 78 个任务上相比 FuseLLM 平均提升 +1.72%，同时在困难任务上大幅缓解性能退化（从 -13.04% 降至 -4.07%）。

**[Quantifying Climate Policy Action and Its Links to Development Outcomes: A Cross-National Data-Driven Analysis](llm_nlp/quantifying_climate_policy_action_and_its_links_to_development_outcomes_a_cross-.md)**

:   构建了从 NLP 文本分类到计量经济分析的跨国气候政策分析框架：利用多语言 DistilBERT 对气候政策文档自动分类（Mitigation / Adaptation / DRM / Loss & Damage），再与世界银行发展指标做固定效应面板回归，揭示不同类型气候政策与发展结果的关联。

**[Reliable Decision Making via Calibration Oriented Retrieval Augmented Generation](llm_nlp/reliable_decision_making_via_calibration_oriented_retrieval_augmented_generation.md)**

:   提出 CalibRAG 框架，通过训练一个温度条件化的 forecasting function 来确保 RAG 辅助决策过程中的置信度校准，不仅改善校准质量还提升了准确率。

**[Reparameterized LLM Training via Orthogonal Equivalence Transformation](llm_nlp/reparameterized_llm_training_via_orthogonal_equivalence_transformation.md)**

:   提出 POET 训练框架，通过将权重矩阵重参数化为"两个可学习正交矩阵 × 固定随机权重"的形式来保持谱性质不变，实现更稳定的训练和更好的泛化，且比 AdamW 更节省参数。

**[Rethinking Residual Distribution in Locate-then-Edit Model Editing](llm_nlp/rethinking_residual_distribution_in_locate-then-edit_model_editing.md)**

:   揭示 locate-then-edit 模型编辑中残差分配（residual distribution）机制引入的权重偏移误差会随分配距离、batch 大小和编辑序列长度增长，提出 BLUE（Boundary Layer UpdatE）策略仅更新首尾关键层，平均提升 35.59%。

**[Retrieval is Not Enough: Enhancing RAG Reasoning through Test-Time Critique and Optimization](llm_nlp/retrieval_is_not_enough_enhancing_rag_reasoning_through_test-time_critique_and_o.md)**

:   提出 AlignRAG 框架，将 RAG 重新定义为"检索增强推理"，通过训练专用 Critic Language Model (CLM) 在测试时迭代批评和修正推理过程，解决推理与检索证据之间的错位问题，8B CLM 在 OOD 任务上超越 72B 标准 CLM。

**[Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models](llm_nlp/retrospective_incontext_learning_for_temporal_credit_assignm.md)**

:   论文提出 RICL（Retrospective In-Context Learning），利用 LLM 的预训练知识把环境中的稀疏奖励回溯性转化为稠密 advantage supervision，再结合在线策略迭代框架 RICOL，在 BabyAI 四个场景中以更高样本效率达到与传统在线 RL 相当的收敛表现，展示了 LLM 在 temporal credit assignment 上的潜力。

**[Scalable Fingerprinting of Large Language Models](llm_nlp/scalable_fingerprinting_of_large_language_models.md)**

:   提出 Perinucleus 采样方法生成可扩展的 LLM 指纹，能在 Llama-3.1-8B 上嵌入 24,576 个指纹（比现有方法多两个数量级）且不损害模型能力，并通过理论和实验证明大规模指纹是抵御共谋攻击的关键。

**[Scaling Embedding Layers in Language Models](llm_nlp/scaling_embedding_layers_in_language_models.md)**

:   提出Scone方法，通过为高频n-gram学习上下文化的嵌入（用独立Transformer模型训练），在推理时将这些嵌入卸载到主存/SSD，实现"训练时用更多计算但推理时不增加加速器资源"的新缩放范式，1B参数模型超越1.9B基线。

**[Scaling Up Active Testing to Large Language Models](llm_nlp/scaling_up_active_testing_to_large_language_models.md)**

:   通过三项关键简化——用 in-context learning 构建固定代理模型、使用小代理模型评估大目标模型、无需目标模型预测进行数据采集——将 active testing 扩展到 LLM，风险估计误差比随机采样降低 25%-80%。

**[SIMU: Selective Influence Machine Unlearning](llm_nlp/simu_selective_influence_machine_unlearning.md)**

:   提出 SIMU 两阶段框架：先通过梯度聚合识别编码遗忘集信息的关键 MLP 神经元，再仅对这些神经元进行二阶（Sophia）优化遗忘，在保持遗忘效果的同时大幅提升模型原有能力的保留。

**[Sloth: Scaling Laws for LLM Skills to Predict Multi-Benchmark Performance Across Families](llm_nlp/sloth_scaling_laws_for_llm_skills_to_predict_multi-benchmark_performance_across_.md)**

:   提出Skills Scaling Laws (Sloth)，通过假设LLM性能由低维潜在技能（如推理、指令遵循）驱动，利用benchmark间的相关性构建跨模型家族的缩放定律，用少量家族数据即可预测大模型在多个benchmark上的表现。

**[Small Language Models as Compiler Experts: Auto-Parallelization for Heterogeneous Systems](llm_nlp/small_language_models_as_compiler_experts_auto-parallelization_for_heterogeneous.md)**

:   系统评估了三个小于 1.5B 参数的语言模型（gemma3、llama3.2、qwen2.5）在编译器自动并行化任务上的能力，使用六种推理策略在 11 个真实世界内核上实现平均 6.81x 加速、峰值 43.25x，证明小模型可作为强大的编译器优化推理引擎。

**[Solving Inequality Proofs with Large Language Models](llm_nlp/solving_inequality_proofs_with_large_language_models.md)**

:   提出 IneqMath（首个大规模奥林匹克级不等式 benchmark），将不等式证明定义为两个可自动验证的子任务（界估计与关系预测），并开发五模块 LLM-as-Judge 框架，发现即便 o1 在逐步推理审查下整体准确率也不到 10%。

**[SPACE: Noise Contrastive Estimation Stabilizes Self-Play Fine-Tuning for Large Language Models](llm_nlp/space_noise_contrastive_estimation_stabilizes_self-play_fine-tuning_for_large_la.md)**

:   提出 Space（Self-PlAy via Noise Contrastive Estimation），将噪声对比估计引入自对弈微调，通过独立优化真实和合成样本的绝对奖励值（而非相对差距），从根本上解决了 SPIN 等方法的不稳定收敛问题，并提供可证明的稳定收敛保证。

**[Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning](llm_nlp/sparse_mezo_less_parameters_for_better_performance_in_zeroth-order_llm_fine-tuni.md)**

:   提出 Sparse MeZO（S-MeZO），通过观察到零阶梯度噪声对大权重影响更严重，选择性地仅对小权重进行零阶优化扰动和更新，在不增加内存开销的前提下实现了显著的性能提升（RTE 上 +9%）和收敛加速（3.5x）。

**[Spectral Conditioning of Attention Improves Transformer Performance](llm_nlp/spectral_conditioning_of_attention_improves_transformer_performance.md)**

:   理论分析了 Transformer 注意力层 Jacobian 的条件数受 Query/Key/Value 矩阵条件数控制，提出谱调节注意力（Spectral Conditioned Attention），通过向 Q/K/V 矩阵添加固定校正项降低条件数，作为即插即用模块在图像分类、目标检测、NLP 等多任务上一致提升性能。

**[Stop DDoS Attacking the Research Community with AI-Generated Survey Papers](llm_nlp/stop_ddos_attacking_the_research_community_with_ai-generated_survey_papers.md)**

:   这篇立场论文以"综述论文 DDoS 攻击"为隐喻，通过定量分析 arXiv 2020-2024 年间 10,063 篇 CS 综述论文，揭示 AI 生成综述的爆炸式增长趋势和质量问题，提出规范 AI 辅助综述写作和建设"动态活综述"的愿景。

**[Strassen Attention, Split VC Dimension and Compositionality in Transformers](llm_nlp/strassen_attention_split_vc_dimension_and_compositionality_in_transformers.md)**

:   提出 Splitting VC 维度理论工具证明了单层 softmax Transformer（即使无限精度）在组合推理任务上的根本限制，并设计了具有亚立方时间复杂度的 Strassen 注意力机制来突破这些限制。

**[Superposition Yields Robust Neural Scaling](llm_nlp/superposition_yields_robust_neural_scaling.md)**

:   揭示表示叠加（superposition）是神经缩放定律的核心驱动力：在强叠加区间，损失**通用地**与模型维度成反比（$L \propto 1/m$），且该行为与数据频率分布的具体形式无关，这与实际 LLM 的缩放行为一致。

**[Synergy over Discrepancy: A Partition-Based Approach to Multi-Domain LLM Fine-Tuning](llm_nlp/synergy_over_discrepancy_a_partition-based_approach_to_multi-domain_llm_fine-tun.md)**

:   提出基于分区的多阶段微调框架，通过策略性地将多个域划分为子集（阶段），在最大化域间协同的同时最小化负迁移，并推导了新的泛化界来理论支撑该分区策略。

**[System Prompt Optimization with Meta-Learning](llm_nlp/system_prompt_optimization_with_meta-learning.md)**

:   提出双层系统提示优化问题并设计 MetaSPO 元学习框架，通过外循环优化跨任务泛化的系统提示、内循环优化任务特定的用户提示，使优化后的系统提示在 14 个未见任务上显著超越基线。

**[Teaming LLMs to Detect and Mitigate Hallucinations](llm_nlp/teaming_llms_to_detect_and_mitigate_hallucinations.md)**

:   提出 Consortium Consistency 方法，将单模型一致性方法（Self-Consistency 和 Semantic Entropy）扩展到多模型协作设置，通过聚合多个异构 LLM 的响应来实现更可靠的幻觉检测和缓解，同时降低推理成本。

**[The Curse of Depth in Large Language Models](llm_nlp/the_curse_of_depth_in_large_language_models.md)**

:   揭示 Pre-LN Transformer 中输出方差指数增长导致深层退化为恒等映射的根本原因，提出无参数的 LayerNorm Scaling（LNS）策略——仅在 LayerNorm 后乘以 $1/\sqrt{\ell}$，将方差从指数增长压缩为多项式增长，在 130M-7B 全规模上稳定改进困惑度 5-8%。

**[The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?](llm_nlp/the_non-linear_representation_dilemma_is_causal_abstraction_enough_for_mechanist.md)**

:   证明了当因果抽象（causal abstraction）中的对齐映射不受线性约束时，任意神经网络都可以被映射到任意算法，使得因果抽象变得平凡而无信息量，由此提出"非线性表示困境"——在对齐映射的复杂度与准确度之间缺乏原则性的权衡方式。

**[The Rise of Parameter Specialization for Knowledge Storage in Large Language Models](llm_nlp/the_rise_of_parameter_specialization_for_knowledge_storage_in_large_language_mod.md)**

:   系统分析 20 个开源 LLM，发现更强的模型在 MLP 参数向量中展现出更高的知识特化程度（Parameter Specialization），即相似知识倾向于集中编码到少数参数向量中，并通过因果实验验证该特化程度与模型知识任务性能之间存在因果关系。

**[The Trilemma of Truth in Large Language Models](llm_nlp/the_trilemma_of_truth_in_large_language_models.md)**

:   提出 sAwMIL（稀疏感知多实例学习）三类探测框架，结合 MIL 和保形预测，将 LLM 内部激活分类为 true/false/neither，揭示真假信号并非简单的双向对称编码，而是跨越多维子空间的分布式表征。

**[Thought Communication in Multiagent Collaboration](llm_nlp/thought_communication_in_multiagent_collaboration.md)**

:   提出 ThoughtComm 框架，通过建立隐变量生成模型并提供可辨识性理论保证，让多个 LLM 智能体直接交换潜在"思想"（latent thoughts）而非自然语言，实现超越语言瓶颈的"心灵感应"式协作。

**[Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training](llm_nlp/through_the_river_understanding_the_benefit_of_schedule-free_methods_for_languag.md)**

:   从 River-Valley 损失景观的几何视角深入分析 Schedule-Free (SF) 优化器，揭示 SF-AdamW 在不需要学习率衰减或权重平均的情况下自动沿"河流"方向优化，并提出改进变体解决动量敏感性和大批量训练的局限性。

**[Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs](llm_nlp/triplets_better_than_pairs_towards_stable_and_effective_self-play_fine-tuning_fo.md)**

:   提出 T-SPIN（三元组自博弈微调），在 SPIN 基础上引入"历史优势"（proto-synthetic 响应作为锚点）和熵约束实现无参考策略训练，解决了 SPIN 迭代中的优化不稳定和训练-生成不对齐两大问题，仅用 25% 标注数据即可媲美全量 SFT。

**[Understanding And Enhancing Mask-Based Pretraining Towards Universal Representat](llm_nlp/understanding_and_enhancing_mask-based_pretraining_towards_universal_representat.md)**

:   用高维线性回归理论精确刻画了 mask-based pretraining 中掩码率对测试风险的影响（偏差-方差分解），揭示了最优掩码率依赖于任务和模型大小，并据此提出 R2MAE（随机随机掩码），在视觉、语言、DNA、单细胞模型上一致超越固定掩码率。

**[Unifying Attention Heads and Task Vectors via Hidden State Geometry in In-Context Learning](llm_nlp/unifying_attention_heads_and_task_vectors_via_hidden_state_geometry_in_in-contex.md)**

:   本文提出基于隐状态几何（可分离性+对齐性）的统一框架，将ICL的两大解释路线——注意力头（PTH/IH）和任务向量——联系起来，揭示ICL在分类任务中的两阶段机制：早期层通过PTH建立可分离性，后期层通过IH改善与标签unembedding方向的对齐性。

**[Valid Inference with Imperfect Synthetic Data](llm_nlp/valid_inference_with_imperfect_synthetic_data.md)**

:   提出基于广义矩估计（GMM）的无超参数框架，将 LLM 生成的不完美合成数据与真实数据结合进行统计有效推断，当合成数据残差与真实数据残差相关时可显著降低估计方差，且在最坏情况下（合成数据完全无信息）也不会损害估计质量。

**[ValuePilot: A Two-Phase Framework for Value-Driven Decision-Making](llm_nlp/valuepilot_a_two-phase_framework_for_value-driven_decision-making.md)**

:   提出 ValuePilot 两阶段框架，通过数据集生成工具包（DGT）构建价值标注场景，再用决策模块（DMM）结合用户个性化价值偏好进行多准则决策，在与人类决策对齐方面超过 GPT-5 等强基线。

**[What Happens During the Loss Plateau? Understanding Abrupt Learning in Transformers](llm_nlp/what_happens_during_the_loss_plateau_understanding_abrupt_learning_in_transforme.md)**

:   系统研究 Transformer 训练中的"突变学习"现象，揭示 loss 平台期内模型已学会部分解、同时表现出输出重复偏差和表示坍缩，并证明注意力图的缓慢学习是关键瓶颈，相关发现在 Pythia/OLMo 等 LLM 预训练早期也得到验证。

**[What One Cannot, Two Can: Two-Layer Transformers Provably Represent Induction Heads on Any-Order Markov Chains](llm_nlp/what_one_cannot_two_can_two-layer_transformers_provably_represent_induction_head.md)**

:   理论证明两层单头 Transformer 足以表示任意 $k$ 阶马尔可夫过程的条件 $k$-gram 模型（即 $k$ 阶 induction head），给出了 Transformer 深度与马尔可夫阶数关系的最紧已知刻画，关键在于利用 MLP 中的 ReLU 和 LayerNorm 非线性来补偿减少的层数。

**[Worse than Zero-shot? A Fact-Checking Dataset for Evaluating the Robustness of RAG Against Misleading Retrievals](llm_nlp/worse_than_zero-shot_a_fact-checking_dataset_for_evaluating_the_robustness_of_ra.md)**

:   提出 RAGuard 基准数据集，首次系统评估 RAG 系统对误导性检索内容的鲁棒性。通过从 Reddit 构建包含支持性、误导性和无关文档的真实检索语料库，揭示所有测试的 LLM-RAG 系统在面对误导性检索时表现**比零样本基线更差**，而人类标注者能保持一致判断。

**[Writing in Symbiosis: Mapping Human Creative Agency in the AI Era](llm_nlp/writing_in_symbiosis_mapping_human_creative_agency_in_the_ai_era.md)**

:   通过对 5 万+文档的纵向语料分析，提出"双轨演化"假说——LLM 时代人类写作在主题上趋同、风格上结构性分化，并发现三种作者适应策略原型（Adopters/Resistors/Pragmatists）。

**[Yggdrasil: 桥接动态投机和静态运行时的延迟最优树型LLM解码](llm_nlp/yggdrasil_bridging_dynamic_speculation_and_static_runtime_for_latency-optimal_tr.md)**

:   通过等增长树(EGT)草稿算法和延迟感知目标，实现动态投机与静态图编译的兼容，配合前向执行阶段重叠，在A100上达3.98×加速。

**[Your Pre-trained LLM is Secretly an Unsupervised Confidence Calibrator](llm_nlp/your_pre-trained_llm_is_secretly_an_unsupervised_confidence_calibrator.md)**

:   发现 LLM 后训练（SFT/RLHF/DPO）破坏了预训练模型的置信度校准，提出 DACA 方法利用预训练模型的良好校准性，仅在预测一致样本上对齐置信度，实现无标签的后训练模型校准，ECE 最高改善 15.08%。

**[Zero-Shot Performance Prediction for Probabilistic Scaling Laws](llm_nlp/zero-shot_performance_prediction_for_probabilistic_scaling_laws.md)**

:   将 NLP 学习曲线预测建模为多任务学习问题，利用潜变量多输出高斯过程（MaGP）捕捉数据集中的双层层次结构和任务间相关性，实现学习曲线的零样本预测，并通过蒙特卡洛模拟推导概率化的 Scaling Laws。

---

## 🧩 多模态 VLM { #multimodal_vlm }

**[A Frustratingly Simple Yet Highly Effective Attack Baseline: Over 90% Success Rate Against the Strong Black-box Models of GPT-4.5/4o/o1](multimodal_vlm/a_frustratingly_simple_yet_highly_effective_attack_baseline.md)**

:   提出 M-Attack，通过对对抗图像做随机裁剪后与目标图像在嵌入空间做局部对齐（而非传统的全局对齐），配合多模型集成，使得生成的对抗扰动具有丰富的局部语义细节，在 GPT-4.5/4o/o1 等商业黑盒 LVLM 上实现超过 90% 的目标攻击成功率，大幅超越所有已有方法。

**[A Multimodal Benchmark for Framing of Oil & Gas Advertising and Potential Greenwashing Detection](multimodal_vlm/a_multimodal_benchmark_for_framing_of_oil_gas_advertising_an.md)**

:   构建了首个面向石油天然气行业视频广告的多模态框架分析基准数据集（706个视频，覆盖Facebook和YouTube两个平台，13种框架类型），用于评估VLM在检测企业"洗绿"宣传中的能力，发现GPT-4.1在环境信息检测上可达79% F1但在绿色创新识别上仅46% F1。

**[AC-LoRA: (Almost) Training-Free Access Control-Aware Multi-Modal LLMs](multimodal_vlm/aclora_almost_trainingfree_access_controlaware_multimodal_ll.md)**

:   设计AC-LoRA系统，通过为不同权限数据集维护独立的LoRA适配器，并基于查询相似度和用户权限进行检索+无训练合并，实现企业级LLM聊天机器人的强信息隔离保证。

**[ACT as Human: Multimodal Large Language Model Data Annotation with Critical Thinking](multimodal_vlm/act_as_human_multimodal_large_language_model_data_annotation.md)**

:   提出ACT（Annotation with Critical Thinking）流水线，先用MLLM批量标注数据，再用另一个MLLM作为"批评者"识别可能的错误标注，仅让人类审核被标记的样本，在减少70-90%人工标注成本的同时将性能差距控制在<2%。

**[AdaLRS: Loss-Guided Adaptive Learning Rate Search for Efficient Foundation Model Pretraining](multimodal_vlm/adalrs_lossguided_adaptive_learning_rate_search_for_efficien.md)**

:   提出AdaLRS，一种即插即用的在线学习率搜索算法，通过监控损失下降速度（loss velocity）来自适应调整学习率，将学习率超参搜索的成本从多次独立训练降低到单次训练，实现~50%的训练成本节省。

**[Adapting Vision-Language Models for Evaluating World Models](multimodal_vlm/adapting_visionlanguage_models_for_evaluating_world_models.md)**

:   提出UNIVERSE框架，通过仅微调PaliGemma 2的投影头（0.07%参数）和优化数据混合策略，实现对游戏世界模型rollout的高效视觉语言评估，在动作/角色识别任务上以极低成本接近完整微调的性能。

**[ADMN: A Layer-Wise Adaptive Multimodal Network for Dynamic Input Noise and Compute Resources](multimodal_vlm/admn_a_layerwise_adaptive_multimodal_network_for_dynamic_inp.md)**

:   提出 ADMN（Adaptive Depth Multimodal Network），通过两阶段训练——(1) Multimodal LayerDrop 微调使 backbone 适应任意层配置，(2) QoI感知控制器动态分配层预算给各模态——在严格计算约束下根据每个模态的信息质量(QoI)自适应分配层数，匹配全量模型精度同时减少 75% FLOPs 和 60% 延迟。

**[Advancing Compositional Awareness in CLIP with Efficient Fine-Tuning](multimodal_vlm/advancing_compositional_awareness_in_clip_with_efficient_fin.md)**

:   提出 CLIC（Compositionally-aware Learning in CLIP），通过拼接图像对 + 跨图词汇交换生成 hard negatives + 多正样本训练的策略，在仅微调文本编码器的情况下同时提升 CLIP 的组合推理能力和检索性能，在 SugarCrepe++ 上取得 CLIP 类模型 SOTA。

**[AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models](multimodal_vlm/affordbot_3d_fine-grained_embodied_reasoning_via_multimodal_large_language_model.md)**

:   提出细粒度 3D 具身推理任务（预测可操作元素的空间位置+运动类型+运动轴），通过将 3D 点云渲染为环视图并投影 affordance 候选，结合定制的 CoT 推理范式指导 MLLM 实现 SOTA，AP25 达 23.3%。

**[Aligning by Misaligning: Boundary-aware Curriculum Learning for Multimodal Alignment](multimodal_vlm/aligning_by_misaligning_boundaryaware_curriculum_learning_fo.md)**

:   提出 BACL（Boundary-Aware Curriculum with Local Attention），通过可学习的边界感知负样本采样器（由易到难课程学习）+ 对比局部注意力损失（定位 token 级 mismatch），在 LAION-400M 上为 CLIP 带来 +32% R@1 提升，并在四个大规模基准上取得 SOTA。

**[AntiGrounding: Lifting Robotic Actions into VLM Representation Space for Decision Making](multimodal_vlm/antigrounding_lifting_robotic_actions_into_vlm_representatio.md)**

:   提出 AntiGrounding，逆转传统指令 grounding 过程——不是将语言映射到动作空间，而是将候选机器人动作"提升"到 VLM 表示空间（通过多视角轨迹渲染 + 结构化 VQA），实现零样本闭环机器人轨迹合成。

**[Approximate Domain Unlearning for Vision-Language Models](multimodal_vlm/approximate_domain_unlearning_for_visionlanguage_models.md)**

:   提出 Approximate Domain Unlearning (ADU) 新任务，通过 Domain Disentangling Loss (DDL) 和 Instance-wise Prompt Generator (InstaPG) 两个模块，让预训练 VLM 选择性遗忘指定域（如插画、素描）的识别能力，同时保持其他域（如真实照片）的分类精度，在四个多域数据集上大幅超越所有基线。

**[Balanced Token Pruning: Accelerating Vision Language Models Beyond Local Optimization](multimodal_vlm/balanced_token_pruning_accelerating_vision_language_models_b.md)**

:   提出 Balanced Token Pruning (BTP)，通过在浅层优先多样性剪枝、深层优先注意力剪枝的分阶段策略，联合优化局部输出一致性和全局表示质量，在仅保留 22% 视觉 token 的情况下保持原模型 98% 的性能。

**[Benchmarking Retrieval-Augmented Multimodal Generation for Document Question Answering](multimodal_vlm/benchmarking_retrievalaugmented_multimodal_generation_for_do.md)**

:   提出 MMDocRAG 基准（4055 个专家标注的 QA 对），系统评估了 60 个 VLM/LLM 和 14 个检索器在多模态文档检索增强生成中的引用选择和交错图文回答能力，揭示当前最强模型 GPT-4.1 的 Quote Selection F1 仅 70.2%，微调可显著提升性能。

**[Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging](multimodal_vlm/better_tokens_for_better_3d_advancing_vision-language_modeling_in_3d_medical_ima.md)**

:   提出 BTB3D，一种基于因果卷积编解码器 + 3D Haar 小波压缩 + 三阶段渐进训练的 3D CT tokenizer，在放射报告生成和文本条件 CT 合成两大下游任务上大幅刷新 SOTA，证明"更好的 token 比更大的语言模型更重要"。

**[Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability](multimodal_vlm/beyond_greedy_exits_improved_early_exit_decisions_for_risk_control_and_reliabili.md)**

:   UAT（Unsupervised Adaptive Thresholding）为早退 DNN 设计了可靠性函数来评估中间层输出质量，并用多臂赌博机（MAB）算法在推理时动态学习最优退出阈值，实现 1.7-2.1× 加速且性能损失 <2%，同时对分布偏移鲁棒。

**[Bias in the Picture: Benchmarking VLMs with Social-Cue News Images and LLM-as-Judge](multimodal_vlm/bias_in_the_picture_benchmarking_vlms_with_social-cue_news_images_and_llm-as-jud.md)**

:   构建 1,343 个新闻图片-问答对的偏见评估基准，标注年龄/性别/种族/职业等人口统计属性，用 GPT-4o 作为评判员（LLM-as-judge）评估 15 个 VLM 在开放式问答中的偏见表现，发现高忠实度不等于低偏见，且性别和职业偏见尤为严重。

**[BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning](multimodal_vlm/bioclip_2_emergent_properties_from_scaling_hierarchical_contrastive_learning.md)**

:   BioCLIP 2 在 TreeOfLife-200M（2.14 亿图像/95.2 万物种）上用层级对比学习训练 ViT-L，零样本物种识别比 BioCLIP 提升 18%，并发现规模化带来的涌现性质——嵌入自动编码生态关系（如达尔文雀喙大小排列）且种内变异与种间差异正交。

**[BLINK-Twice: You See But Do You Observe? A Reasoning Benchmark on Visual Perception](multimodal_vlm/blink-twice_you_see_but_do_you_observe_a_reasoning_benchmark_on_visual_perceptio.md)**

:   提出视觉中心推理 benchmark BLINK-Twice（345 张视觉挑战图 + 103 个对抗样本 + 896 个 VQA + 1725 个推理步骤标注），通过 7 类视觉错觉场景评估 MLLM "看到但未观察到"的推理能力，发现最强模型 Gemini-2.5 Pro 的 G-Acc 仅 26.9%，多轮图像观察和主动视觉交互是提升方向。

**[Breaking the Compression Ceiling: Data-Free Pipeline for Ultra-Efficient Delta Compression](multimodal_vlm/breaking_the_compression_ceiling_data-free_pipeline_for_ultra-efficient_delta_co.md)**

:   提出 UltraDelta——首个无数据 delta 权重压缩流水线，通过方差引导的混合稀疏分配、分布感知压缩和迹范数引导缩放三个组件，在 LLM/NLP/视觉/多模态模型上实现最高 224× 的超高压缩比且性能不降甚至超越微调模型。

**[BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models](multimodal_vlm/bridgevla_input-output_alignment_for_efficient_3d_manipulation_learning_with_vis.md)**

:   提出 BridgeVLA，通过将 3D 点云投影为多视角 2D 图像并以 2D 热力图作为中间表示来对齐输入输出空间，实现了高效且有效的 3D 机器人操作学习。

**[Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning](multimodal_vlm/can_llms_reason_over_non-text_modalities_in_a_training-free_manner_a_case_study_.md)**

:   提出 In-Context Representation Learning（ICRL），首个训练无关框架，将非文本模态基础模型（FM）的表征注入纯文本 LLM 进行少样本推理，通过 PCA 文本注入和最优传输嵌入对齐两种策略实现跨模态知识利用。

**[Can Multi-Modal LLMs Provide Live Step-by-Step Task Guidance?](multimodal_vlm/can_multi-modal_llms_provide_live_step-by-step_task_guidance.md)**

:   提出 Qualcomm Interactive Cooking 基准和 LiveMamba 模型，首次系统评估多模态 LLM 在实时流式视频中提供分步任务指导（包括指令下发、完成检测和错误反馈）的能力。

**[CAPability: A Comprehensive Visual Caption Benchmark for Evaluation](multimodal_vlm/capability_a_comprehensive_visual_caption_benchmark_for_eval.md)**

:   构建 CAPability——11K 标注的图片/视频描述评估基准，从 6 个视角 12 个维度评估 VLM 的描述能力，引入 KT（know-but-cannot-tell）指标衡量 VLM 在 QA 中已知但描述中遗漏的信息差距。

**[Causal-LLaVA: Causal Disentanglement for Mitigating Hallucination in Multimodal Large Language Models](multimodal_vlm/causalllava_causal_disentanglement_for_mitigating_hallucinat.md)**

:   揭示 MLLM 中物体幻觉的表示层根因——数据集共现偏差导致的语义纠缠，提出双路因果解纠缠框架（Causal-Driven Projector + Causal Intervention Module），通过后门调整在 projector 和最终 Transformer 层分离共现物体表示，使 MME-Perception 提升 22.6%。

**[ChartMuseum: Testing Visual Reasoning Capabilities of Large Vision-Language Models](multimodal_vlm/chartmuseum_testing_visual_reasoning_capabilities_of_large_v.md)**

:   构建ChartMuseum——一个包含1,162个专家标注问题的图表QA benchmark，专门评估LVLM的复杂视觉和文本推理能力。与现有图表benchmark（前沿模型接近饱和）不同，ChartMuseum揭示了巨大的模型-人类性能差距：人类93%准确率 vs Gemini-2.5-Pro仅63.0% vs 最佳开源Qwen2.5-VL-72B仅38.5%，且所有模型在视觉推理重的问题上掉点35-55%。

**[CHOICE: Benchmarking the Remote Sensing Capabilities of Large Vision-Language Models](multimodal_vlm/choice_benchmarking_the_remote_sensing_capabilities_of_large_vision-language_mod.md)**

:   提出 CHOICE，一个面向遥感领域的大规模多层级 VLM 基准，包含 10,507 道全新采集题目，覆盖感知与推理 2 大维度、6 个子维度、23 个叶任务，首次实现对 VLM 遥感能力的系统化与客观化评估。

**[CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization](multimodal_vlm/coido_efficient_data_selection_for_visual_instruction_tuning_via_coupled_importa.md)**

:   提出 CoIDO，一个双目标优化数据选择框架，通过联合优化数据重要性和多样性，仅用 20% 随机数据训练轻量评分器，即可从 LLaVA-665K 中选出 20% 子集达到全量微调 98.2% 的性能，同时计算开销为所有方法最低。

**[Context Informs Pragmatic Interpretation in Vision-Language Models](multimodal_vlm/context_informs_pragmatic_interpretation_in_vision-language_models.md)**

:   通过迭代参考游戏（iterated reference games）系统评估 VLM 的语用推理能力，发现模型在无上下文时表现远逊于人类，但在获得相关对话历史后能快速学习达到约 80% 准确率，揭示了 VLM 对上下文信息的强烈依赖性。

**[Continual Multimodal Contrastive Learning](multimodal_vlm/continual_multimodal_contrastive_learning.md)**

:   首次形式化定义持续多模态对比学习(CMCL)问题——按顺序在不同模态对数据上训练而不忘记之前的对齐，提出Dual-sided Null Space (DNS)方法将新梯度投影到不影响旧知识的子空间，在7个数据集11个训练步骤上一致优于现有持续学习基线。

**[CovMatch: Cross-Covariance Guided Multimodal Dataset Distillation with Trainable Text Encoder](multimodal_vlm/covmatch_crosscovariance_guided_multimodal_dataset_distillat.md)**

:   提出 CovMatch，通过将多模态对比学习的双层优化简化为跨协方差矩阵对齐的闭式解，首次实现图文双编码器的联合优化进行多模态数据集蒸馏，仅用 500 个合成图文对在 Flickr30K 上获得 38.4 平均检索精度（+6.8% 超越 SOTA LoRS），在极端数据高效场景下大幅超越冻结文本编码器的方法。

**[CyIN: Cyclic Informative Latent Space for Bridging Complete and Incomplete Multimodal Learning](multimodal_vlm/cyin_cyclic_informative_latent_space_for_bridging_complete_and_incomplete_multim.md)**

:   提出 CyIN 框架，通过 token 级和 label 级信息瓶颈（IB）构建信息化潜空间，结合循环跨模态翻译重建缺失信息，在单一统一模型中同时优化完整和不完整多模态学习。

**[DanmakuTPPBench: A Multi-modal Benchmark for Temporal Point Process Modeling and Understanding](multimodal_vlm/danmakutppbench_a_multimodal_benchmark_for_temporal_point_pr.md)**

:   论文提出首个面向多模态 Temporal Point Process 的系统 benchmark：一方面构建来自 Bilibili 弹幕视频的时间戳-文本-视频联合事件数据集 DanmakuTPP-Events，另一方面通过多智能体 LLM/MLLM pipeline 构建复杂时序推理问答集 DanmakuTPP-QA，系统揭示当前 TPP 模型与 MLLM 在多模态事件动态理解上的明显短板。

**[Don't Just Chase "Highlighted Tokens" in MLLMs: Revisiting Visual Holistic Context Retention](multimodal_vlm/dont_just_chase_highlighted_tokens_in_mllms_revisiting_visual_holistic_context_r.md)**

:   提出 HoloV，一个即插即用的视觉 token 剪枝框架，通过在不同空间裁剪区域自适应分配剪枝预算，保留全局视觉上下文而非仅保留注意力高亮 token，在 LLaVA-1.5 上剪枝 88.9% token 仍保留 95.8% 原始性能。

**[DOTA: Distributional Test-Time Adaptation of Vision-Language Models](multimodal_vlm/dota_distributional_testtime_adaptation_of_visionlanguage_mo.md)**

:   提出 DOTA（DistributiOnal Test-time Adaptation），不再简单缓存测试样本，而是**持续估计测试数据流的底层分布**，通过贝叶斯定理计算后验概率实现自适应，解决了缓存容量有限导致的灾难性遗忘问题，在多个分布偏移基准上达到 SOTA。

**[DynamicVL: Benchmarking MLLMs for Dynamic City Understanding](multimodal_vlm/dynamicvl_benchmarking_multimodal_large_language_models_for_dynamic_city_underst.md)**

:   提出 DVL-Suite 框架，包含 DVL-Bench 基准和 DVL-Instruct 指令微调数据集，覆盖 42 座美国城市、14,871 张高分辨率多时相遥感影像，系统评估 18 个 MLLM 在长期城市动态理解上的能力，并开发了 DVLChat 基线模型。

**[Efficient Vision-Language Reasoning via Adaptive Token Pruning](multimodal_vlm/efficient_vision-language_reasoning_via_adaptive_token_pruning.md)**

:   提出 Adaptive Token Pruning (ATP)，一种免训练的即插即用模块，通过融合 ViT CLS 注意力（模态内显著性）和 CLIP 文本-图像相似度（模态间相关性）来筛选最有信息量的视觉 token，在 VQA/GQA/COCO Captioning 上以约 40% FLOPs 降低和 1.5 倍加速换取不到 1% 的精度损失。

**[ElasticMM: Efficient MLLM Serving with Elastic Multimodal Parallelism](multimodal_vlm/elasticmm_efficient_multimodal_llms_serving_with_elastic_multimodal_parallelism.md)**

:   提出弹性多模态并行（EMP）范式和 ElasticMM 系统，通过模态感知负载均衡和弹性分区调度将多模态推理的不同阶段解耦到独立实例，相比 vLLM TTFT 降低最高 4.2 倍、吞吐量提升 3.2-4.5 倍。

**[READ: Enhancing Compositional Reasoning in CLIP via Reconstruction and Alignment of Text Descriptions](multimodal_vlm/enhancing_compositional_reasoning_in_clip_via_reconstruction.md)**

:   提出 READ 微调方法，通过两个辅助目标——(1) token-level 重建（冻结解码器从文本嵌入重建替代描述）和 (2) sentence-level 对齐（强制改述的嵌入一致）——增强 CLIP 文本编码器的组合推理能力，在 5 个组合推理基准上达到 SOTA（超 NegCLIP 4.5%，超 FSC-CLIP 4.1%）。

**[Enhancing Outcome Reward-Based RL Training of MLLMs with Self-Consistency Sampling](multimodal_vlm/enhancing_the_outcome_reward-based_rl_training_of_mllms_with_self-consistency_sa.md)**

:   针对多模态多选题中"结果奖励 RL 训练导致不忠实推理轨迹"的问题，提出 Self-Consistency Sampling (SCS)，通过截断-重采样和视觉扰动获得一致性奖励来惩罚虚假推理，搭载 RLOO 后在六个基准上平均提升 7.7 个百分点。

**[Enhancing Vision-Language Model Reliability with Uncertainty-Guided Dropout Decoding](multimodal_vlm/enhancing_visionlanguage_model_reliability_with_uncertaintyg.md)**

:   提出Dropout Decoding——量化视觉token的认知不确定性(epistemic uncertainty)，选择性遮掩高不确定性token，通过集成多个遮掩后的解码结果做多数投票，无需训练即在InstructBLIP上CHAIR_I降低16%、CHAIR_S降低12%。

**[Evaluating Multimodal Large Language Models on Core Music Perception Tasks](multimodal_vlm/evaluating_multimodal_large_language_models_on_core_music_perception_tasks.md)**

:   本文通过三项核心音乐感知任务（切分节奏评分、移调检测、和弦辨识）系统性评估了多模态LLM在音频与MIDI两种输入下的表现，揭示了模型在符号推理上接近理想但在音频感知上存在显著缺陷的关键差距。

**[ExGra-Med: Extended Context Graph Alignment for Medical Vision-Language Models](multimodal_vlm/exgra-med_extended_context_graph_alignment_for_medical_vision-language_models.md)**

:   ExGra-Med 提出了一种多图对齐（multi-graph alignment）框架，通过联合对齐图像、指令响应和扩展上下文描述在潜空间中的图结构关系，仅用10%预训练数据即可匹配 LLaVA-Med 的100%数据性能，并在多个医学VQA任务上超越现有SOTA。

**[Explaining Similarity in Vision-Language Encoders with Weighted Banzhaf Interactions](multimodal_vlm/explaining_similarity_in_vision-language_encoders_with_weighted_banzhaf_interact.md)**

:   FIxLIP 提出基于加权 Banzhaf 交互指数的博弈论框架，统一分解视觉-语言编码器（如 CLIP、SigLIP-2）的相似度预测为一阶token归因和二阶跨模态/模态内交互，在效率和忠实度上均超越现有一阶归因方法。

**[FineGRAIN: Evaluating Failure Modes of Text-to-Image Models with Vision Language Model Judges](multimodal_vlm/finegrain_evaluating_failure_modes_of_text-to-image_models_with_vision_language_.md)**

:   FineGRAIN 提出了一个结构化的联合评测框架，通过定义27种细粒度失败模式和利用 VLM+LLM agentic pipeline 来同时评估文本到图像模型的 prompt 遵循能力和视觉语言模型的图像理解能力，揭示了两类模型在特定任务上的系统性缺陷。

**[First SFT, Second RL, Third UPT: Continual Improving Multi-Modal LLM Reasoning via Unsupervised Post-Training](multimodal_vlm/first_sft_second_rl_third_upt_continual_improving_multi-modal_llm_reasoning_via_.md)**

:   提出 MM-UPT 框架，在 SFT 和 RL 之后引入第三阶段"无监督后训练"，通过多数投票作为伪奖励信号结合 GRPO 实现 MLLM 的自我改进，在 MathVista 上将 Qwen2.5-VL-7B 从 66.3% 提升至 72.9%。

**[FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models](multimodal_vlm/flexac_towards_flexible_control_of_associative_reasoning_in_multimodal_large_lan.md)**

:   FlexAC 发现 MLLM 的联想推理行为主要编码在中间层，通过从幻觉响应中提取引导向量并在推理时注入中间层表示，实现忠实性与创造力的灵活调控——幻觉率降低 29%(CHAIR)，创造力提升 5.8×(Creation-MMBench)，且无需训练。

**[FlowCut: Rethinking Redundancy via Information Flow for Efficient Vision-Language Models](multimodal_vlm/flowcut_rethinking_redundancy_via_information_flow_for_effic.md)**

:   从信息流（Information Flow）视角重新理解VLM中视觉token的冗余性：发现CLS token是信息中继站、冗余渐进式涌现、单层单标准评分不够可靠，提出FlowCut——基于信息流感知的多标准累积重要性剪枝框架，在LLaVA-1.5-7B上以88.9%的token减少率超越SOTA 1.6%，在LLaVA-NeXT-7B上超越4.3%。

**[FOCUS: Internal MLLM Representations for Efficient Fine-Grained Visual Question Answering](multimodal_vlm/focus_internal_mllm_representations_for_efficient_fine-grained_visual_question_a.md)**

:   提出 FOCUS，一种无需训练的视觉裁剪方法，利用 MLLM 内部 KV-cache 中 value 特征的余弦相似度构建目标相关性图，高效定位问题相关的图像区域，在细粒度 VQA 上实现与 SOTA 可比的精度，同时计算效率提升 3-6.5 倍。

**[ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](multimodal_vlm/forcevla_enhancing_vla_models_with_a_force-aware_moe_for_contact-rich_manipulati.md)**

:   提出 ForceVLA，在 VLA 框架中将 6 轴力/力矩传感引入为一等模态，通过 FVLMoE（力感知混合专家）模块在动作解码阶段动态融合视觉-语言嵌入与实时力反馈，在 5 项接触密集操作任务上平均成功率提升 23.2%，个别任务达 80%。

**[FractalBench: Diagnosing Visual-Mathematical Reasoning Through Recursive Program Synthesis](multimodal_vlm/fractalbench_diagnosing_visual-mathematical_reasoning_through_recursive_program_.md)**

:   提出 FractalBench，一个通过分形图像程序合成诊断 MLLM 视觉-数学推理能力的 benchmark：12 种经典分形、610 张测试图、4 个 MLLM，揭示 76% 的代码能执行但仅 4% 视觉正确，暴露了模型在递归抽象能力上的根本缺陷。

**[From Flat to Hierarchical: Extracting Sparse Representations with Matching Pursuit](multimodal_vlm/from_flat_to_hierarchical_extracting_sparse_representations_with_matching_pursui.md)**

:   提出 MP-SAE，将经典 Matching Pursuit 算法展开为 SAE 的序列化编码器，通过残差引导的贪心特征选择实现条件正交性，能捕捉标准 SAE 无法发现的层次结构、非线性可及和跨模态特征，并天然支持推理时自适应稀疏度调节。

**[GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images](multimodal_vlm/gem_empowering_mllm_for_grounded_ecg_understanding_with_time_series_and_images.md)**

:   提出 GEM，首个统一 ECG 时间序列、12 导联 ECG 图像和文本的多模态大语言模型，通过双编码器框架、跨模态对齐和知识引导的指令数据生成，实现了基于可量化生理特征的接地心电图诊断，诊断准确率提升 7.4%，可解释性提升 22.7%，接地能力提升 25.3%。

**[Generalized Contrastive Learning for Universal Multimodal Retrieval](multimodal_vlm/generalized_contrastive_learning_for_universal_multimodal_re.md)**

:   提出 Generalized Contrastive Learning (GCL)——在 mini-batch 内对所有 6 种模态对组合（image↔text, image↔image+text, text↔image+text）执行对比学习，无需构建新的三元组数据集，仅用现有图文对即可在 M-BEIR 上将 VISTA 的平均检索精度从 21.18 提升到 34.06（+60.8%），在 MMEB 的 text→image+text 任务上从 10.1% 提升到 31.1%。

**[Generate, but Verify: Reducing Hallucination in Vision-Language Models with Retrospective Resampling](multimodal_vlm/generate_but_verify_reducing_hallucination_in_visionlanguage.md)**

:   提出REVERSE框架——首次在单一VLM内统一了生成、验证和纠正三个阶段：通过引入<SPAN>、</CN>（置信）、</UN>（不置信）三个特殊token训练幻觉感知模型，推理时当</UN>概率超过阈值就回溯到上一个</CN>重新生成，在CHAIR-MSCOCO上降低12%、HaloQuest上降低34%的幻觉率。

**[GeoRanker: Distance-Aware Ranking for Worldwide Image Geolocalization](multimodal_vlm/georanker_distance-aware_ranking_for_worldwide_image_geolocalization.md)**

:   提出 GeoRanker，一种距离感知排序框架，利用大视觉语言模型建模查询-候选之间的空间关系，通过多阶距离损失实现全球图像地理定位的 SOTA。

**[GLSim: Detecting Object Hallucinations in LVLMs via Global-Local Similarity](multimodal_vlm/glsim_detecting_object_hallucinations_in_lvlms_via_globalloc.md)**

:   提出 GLSim，一种无训练的物体幻觉检测框架，结合图像-文本间的全局和局部嵌入相似度信号来判断 LVLM 生成的物体是否为幻觉，显著超越仅使用全局或局部信号的方法。

**[GoalLadder: Incremental Goal Discovery with Vision-Language Models](multimodal_vlm/goalladder_incremental_goal_discovery_with_vision-language_models.md)**

:   提出 GoalLadder，利用 VLM 渐进式发现并排序候选目标状态，结合 ELO 评分系统抵抗噪声反馈，在学习的嵌入空间中定义距离奖励，仅凭单条语言指令就能训练 RL 智能体达到约 95% 的成功率。

**[Guiding Cross-Modal Representations with MLLM Priors via Preference Alignment](multimodal_vlm/guiding_cross-modal_representations_with_mllm_priors_via_preference_alignment.md)**

:   提出 MAPLE 框架，利用现成 MLLM 的内在模态对齐能力自动构建偏好数据，通过 Relative Preference Alignment（RPA）损失引导跨模态表示学习，在细粒度检索任务上取得显著提升。

**[HAWAII: Hierarchical Visual Knowledge Transfer for Efficient VLM](multimodal_vlm/hawaii_hierarchical_visual_knowledge_transfer_for_efficient_vision-language_mode.md)**

:   提出 Hawaii 框架，通过混合 LoRA 适配器（MoLA）和分层知识蒸馏（HKD），将多个视觉专家的知识蒸馏到单个视觉编码器中，在不增加推理成本的前提下显著提升 VLM 的视觉理解能力。

**[HermesFlow: Seamlessly Closing the Gap in Multimodal Understanding and Generation](multimodal_vlm/hermesflow_seamlessly_closing_the_gap_in_multimodal_understanding_and_generation.md)**

:   首次揭示统一多模态大模型中理解能力普遍强于生成能力的现象，提出 HermesFlow 框架，通过同源偏好数据构建配对理解-生成偏好对，利用 Pair-DPO 和自博弈迭代优化，在不引入外部高质量数据的情况下同步提升理解与生成能力并缩小两者差距。

**[Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems](multimodal_vlm/hierarchical_self-attention_generalizing_neural_attention_mechanics_to_multi-sca.md)**

:   从熵最小化第一性原理推导出层次化自注意力（HSA）机制，为嵌套信号（多模态、多尺度数据）提供理论最优的注意力计算方法，并证明 HSA 是在保持层次约束下最接近标准 Softmax 注意力的 KL 散度最优解。

**[HoPE: Hybrid of Position Embedding for Long Context Vision-Language Models](multimodal_vlm/hope_hybrid_of_position_embedding_for_long_context_visionlan.md)**

:   提出 HoPE（Hybrid of Position Embedding），通过混合频率分配策略和动态时间缩放机制改进 VLM 中的位置编码，解决 RoPE 在长视频等长上下文多模态场景中无法可靠捕捉时空语义相似性的问题，在四个长视频基准上一致超越现有方法。

**[iFinder: Structured Zero-Shot VLM Grounding for Dash-Cam Video Reasoning](multimodal_vlm/ifinder_structured_zero-shot_vision-based_llm_grounding_for_dash-cam_video_reaso.md)**

:   提出 iFinder，一个模块化免训练框架，将行车记录仪视频解耦为感知（结构化场景表示）与推理（LLM），通过层级数据结构和三块式提示策略使 LLM 获得可解释的时空推理能力，在四个驾驶视频基准上零样本超越端到端 V-VLM，事故推理准确率提升高达 39%。

**[Intervene-All-Paths: Unified Mitigation of LVLM Hallucinations across Alignment Formats](multimodal_vlm/intervene-all-paths_unified_mitigation_of_lvlm_hallucinations_across_alignment_f.md)**

:   提出 AllPath，一个基于 Transformer 因果架构的多路径幻觉干预框架，首次发现 LVLM 的幻觉不来自单一因果路径而是 image-to-input-text、image-to-output-text、text-to-text 三条路径的交互，并且模型会根据问答对齐格式自适应选择不同路径；通过为每条路径设计轻量级关键 head 识别方法并自适应干预，在 POPE、MCQ-POPE、CHAIR、MME 四个不同格式 benchmark 上一致降低幻觉。

**[JailBound: Jailbreaking Internal Safety Boundaries of Vision-Language Models](multimodal_vlm/jailbound_jailbreaking_internal_safety_boundaries_of_vision-language_models.md)**

:   受 Eliciting Latent Knowledge (ELK) 框架启发，首次揭示 VLM 在 fusion layer 潜空间中存在可近似的安全决策边界，提出 JailBound 两阶段攻击框架（Safety Boundary Probing + Safety Boundary Crossing），通过联合优化图像和文本对抗扰动跨越该边界，在白盒和黑盒场景分别达到 94.32% 和 67.28% 平均攻击成功率，显著超越 SOTA。

**[Learning Shared Representations from Unpaired Data](multimodal_vlm/learning_shared_representations_from_unpaired_data.md)**

:   提出 SUE (Spectral Universal Embedding)，首次证明几乎完全依赖非配对数据即可学习跨模态共享表示：通过独立的频谱嵌入从各模态随机游走中提取模态不变的"通用"结构，再用极少量配对样本（~100对）做 CCA 线性对齐 + MMD 非线性微调，在检索上超越使用同等配对数的对比学习 250%+。

**[Learning to Instruct for Visual Instruction Tuning](multimodal_vlm/learning_to_instruct_for_visual_instruction_tuning.md)**

:   提出 L2T（Learning to Instruct），仅通过将训练损失扩展到指令序列（不再只在回答上计算 loss）来改善视觉指令调优——无额外数据和几乎零计算开销，在 16 个多模态基准上获得高达 9% 的相对提升，captioning 提升 18%，同时缓解幻觉。

**[Learning to Steer: Input-dependent Steering for Multimodal LLMs](multimodal_vlm/learning_to_steer_input-dependent_steering_for_multimodal_llms.md)**

:   针对现有模型引导(steering)方法使用固定方向向量无法适配不同输入的局限，提出 L2S (Learn-to-Steer)：先通过输入特定的对比提示生成理想的引导向量（P2S），再训练一个轻量 2 层 MLP 从输入上下文预测该向量，以极低开销实现了输入依赖的行为引导，在安全执行和幻觉缓解两个应用上显著优于静态 steering 基线。

**[MemEIC: A Step Toward Continual and Compositional Knowledge Editing](multimodal_vlm/memeic_a_step_toward_continual_and_compositional_knowledge_editing.md)**

:   提出 MemEIC 框架，通过外部双模态检索记忆 + 内部模态分离 LoRA 适配器 + 仿脑 Knowledge Connector 三层架构，实现大视觉语言模型的持续、组合式知识编辑，在新提出的 CCKEB 基准上大幅超越现有方法。

**[MERIT: Multilingual Semantic Retrieval with Interleaved Multi-Condition Query](multimodal_vlm/merit_multilingual_semantic_retrieval_with_interleaved_multi-condition_query.md)**

:   提出首个多语言交错多条件语义检索数据集 MERIT（320K queries, 135K products, 5种语言, 7大品类），揭示现有检索模型仅关注全局语义而忽略条件细节的瓶颈，并设计 Coral 微调框架通过嵌入重建+对比学习将检索性能提升 45.9%。

**[Metacognitive Sensitivity for Test-Time Dynamic Model Selection](multimodal_vlm/metacognitive_sensitivity_for_test-time_dynamic_model_selection.md)**

:   借鉴人类认知科学中的元认知灵敏度（meta-d'）概念，提出一种测试时动态模型选择框架：用 meta-d' 量化模型"知道自己知不知道"的能力，结合即时置信度构成上下文向量，通过 contextual bandit 在线选择最优模型，在多数据集上超越单模型性能。

**[MIDAS: Misalignment-based Data Augmentation Strategy for Imbalanced Multimodal Learning](multimodal_vlm/midas_misalignment-based_data_augmentation_strategy_for_imbalanced_multimodal_le.md)**

:   首次提出将跨模态不对齐样本作为有监督训练信号（而非噪声/干扰）来缓解多模态学习中的模态不平衡问题，设计 MIDAS 数据增强框架：通过置信度标注不对齐样本 + 弱模态加权 + 难样本加权三重机制，在四个多模态分类基准上显著超越现有方法。

**[Mint: A Simple Test-Time Adaptation of Vision-Language Models against Common Corruptions](multimodal_vlm/mint_a_simple_testtime_adaptation_of_visionlanguage_models_a.md)**

:   发现 CLIP 在图像损坏下的性能退化根源在于**嵌入方差坍缩**——类内与类间方差同步缩小导致嵌入空间判别性丧失；提出 Mint，通过最大化伪标签类间方差（PL-inter）在线修复嵌入几何，仅凭均值累加器和梯度累加器两个极简组件即可在 BS=1 的在线场景下稳定提升 CLIP 在多种损坏基准上的分类精度，同时比最强 baseline 快 45 倍。

**[MIRAGE: A Benchmark for Multimodal Information-Seeking and Reasoning in Agriculture](multimodal_vlm/mirage_a_benchmark_for_multimodal_information-seeking_and_reasoning_in_agricultu.md)**

:   MIRAGE 是首个基于真实农业专家咨询对话（35,000+条）构建的多模态基准，评估视觉语言模型在领域级实体识别、因果推理和"澄清还是回答"决策方面的能力，揭示了即使 GPT-4.1 识别准确率也仅 43.9% 的严峻挑战。

**[MM-OPERA: Benchmarking Open-ended Association Reasoning for Large Vision-Language Models](multimodal_vlm/mm-opera_benchmarking_open-ended_association_reasoning_for_large_vision-language.md)**

:   提出 MM-OPERA，一个包含 11,497 实例的开放式联想推理基准，通过远程物品关联（RIA）和上下文关联（ICA）两大任务评估 LVLM 的关联推理能力，配套设计了 LLM-as-a-Judge 评分策略和过程奖励评估方法，揭示当前最强 LVLM 仍显著落后于人类。

**[MME-VideoOCR: Evaluating OCR-Based Capabilities of Multimodal LLMs in Video Scenarios](multimodal_vlm/mme-videoocr_evaluating_ocr-based_capabilities_of_multimodal_llms_in_video_scena.md)**

:   提出 MME-VideoOCR，一个包含 25 个任务、44 个场景、1464 个视频和 2000 个人工标注 QA 对的视频 OCR 综合评估基准，涵盖文本识别、理解和推理三个层次。评估 18 个 SOTA MLLM 揭示最强模型（Gemini-2.5 Pro）仅达 73.7%，跨帧理解任务低至 25% 以下。

**[MMLongBench: Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly](multimodal_vlm/mmlongbench_benchmarking_longcontext_visionlanguage_models_e.md)**

:   构建首个全面的长上下文视觉语言模型（LCVLM）评估基准 MMLongBench——13,331 个样本覆盖 5 类下游任务、混合图像类型、5 级标准化输入长度（8K-128K tokens），评估 46 个模型后发现单任务性能是整体能力的弱代理，且强推理能力与长上下文性能正相关。

**[MMPerspective: Do MLLMs Understand Perspective? A Comprehensive Benchmark for Perspective Perception, Reasoning, and Robustness](multimodal_vlm/mmperspective_do_mllms_understand_perspective_a_comprehensive_benchmark_for_pers.md)**

:   首个系统评估多模态大语言模型 (MLLMs) 透视理解能力的基准，包含10个任务、3个维度、2711张图像和5083个问答对，揭示了43个SOTA模型在透视推理和鲁棒性方面的显著不足。

**[MoniTor: Exploiting Large Language Models with Instruction for Online Video Anomaly Detection](multimodal_vlm/monitor_exploiting_large_language_models_with_instruction_for_online_video_anoma.md)**

:   提出 MoniTor，一个基于记忆的在线评分队列方案，利用 LLM 进行免训练的在线视频异常检测（VAD），通过双层记忆机制、行为预测和标准评分队列引导 LLM 实现实时异常识别。

**[Multimodal Bandits: Regret Lower Bounds and Optimal Algorithms](multimodal_vlm/multimodal_bandits_regret_lower_bounds_and_optimal_algorithms.md)**

:   针对奖励函数至多有 $m$ 个极值的多模态多臂赌博机问题，提出首个计算可行的算法求解 Graves-Lai 优化问题，实现渐近最优的遗憾界，并证明局部搜索策略是次优的。

**[Multimodal Negative Learning](multimodal_vlm/multimodal_negative_learning.md)**

:   提出多模态负学习（MNL）范式，通过让强势模态引导弱势模态抑制非目标类别（而非强制对齐目标类别），稳定决策空间并保留模态特有信息，理论上收紧了多模态融合的鲁棒性下界。

**[Nautilus: A Large Multimodal Model for Underwater Scene Understanding](multimodal_vlm/nautilus_a_large_multimodal_model_for_underwater_scene_understanding.md)**

:   构建了首个支持八种水下场景理解任务的大型多模态模型 Nautilus，通过物理先验驱动的视觉特征增强（VFE）模块显式修复水下图像退化，提升 LMM 在水下环境中的鲁棒性。

**[NaViL: Rethinking Scaling Properties of Native Multimodal Large Language Models under Data Constraints](multimodal_vlm/navil_rethinking_scaling_properties_of_native_multimodal_large_language_models_u.md)**

:   本文系统研究了在数据约束条件下原生多模态大语言模型(Native MLLM)的设计空间与缩放特性，发现视觉编码器与LLM之间存在正相关的最优缩放关系，并基于此提出了NaViL模型，仅用约6亿预训练图文对即可达到顶级MLLM的竞争性性能。

**[NeedleInATable: Exploring Long-Context Capability of Large Language Models towards Long-Structured Tables](multimodal_vlm/needleinatable_exploring_long-context_capability_of_large_language_models_toward.md)**

:   提出 NeedleInATable (NIAT) 基准，将表格中每个单元格视为"针"，评估 LLM 对长结构化表格的细粒度感知能力，揭示现有模型在复杂下游任务上的高分可能依赖数据捷径而非真正的表格理解。

**[Omni-Mol: Multitask Molecular Model for Any-to-Any Modalities](multimodal_vlm/omni-mol_multitask_molecular_model_for_any-to-any_modalities.md)**

:   提出 Omni-Mol，一个基于多模态 LLM 的统一分子理解与生成框架，通过构建 142 万样本的指令微调数据集、Gradient Adaptive LoRA (GAL) 和 Mixture-of-GAL-Experts (MoGE) 架构，首次在单一模型中统一学习 16 个分子任务（Mol2Mol/Mol2Text/Mol2Num/Text2Mol），以仅 2.2B 参数在 13 个任务上达到 SOTA。

**[On the Value of Cross-Modal Misalignment in Multimodal Representation Learning](multimodal_vlm/on_the_value_of_cross-modal_misalignment_in_multimodal_representation_learning.md)**

:   提出潜变量模型将跨模态失配形式化为选择偏差和扰动偏差两种机制，理论证明MMCL学到的表征恰好捕获与两种偏差无关的不变语义子集，统一了"失配有害/有益"两种对立观点。

**[Partial Information Decomposition via Normalizing Flows in Latent Gaussian Distributions](multimodal_vlm/partial_information_decomposition_via_normalizing_flows_in_latent_gaussian_distr.md)**

**[Praxis-VLM: Vision-Grounded Decision Making via Text-Driven Reinforcement Learning](multimodal_vlm/praxisvlm_visiongrounded_decision_making_via_textdriven_rein.md)**

:   发现VLM的决策推理能力可以与视觉感知解耦——用文本描述替代图像时决策性能不降反升，据此提出Praxis-VLM：在纯文本场景上用GRPO训练决策推理能力，然后零样本迁移到视觉输入推理，在VIVA/PCA-Bench/EgoNormia三个决策benchmark上超越SFT基线且泛化性更强。

**[PrefixKV: Adaptive Prefix KV Cache is What Vision Instruction-Following Models Need for Efficient Generation](multimodal_vlm/prefixkv_adaptive_prefix_kv_cache_is_what_vision_instruction.md)**

:   提出 PrefixKV，将 LVLM 各层 KV 缓存大小的确定转化为搜索最优全局前缀配置的问题，通过二分搜索找到信息保留阈值实现自适应逐层 KV 保留，在 20% 压缩率下仍保持接近原模型性能，提供 1.8× 推理加速。

**[Rethinking Multimodal Learning from the Perspective of Mitigating Classification Ability Disproportion](multimodal_vlm/rethinking_multimodal_learning_from_the_perspective_of_mitig.md)**

:   提出"**分类能力不均衡**"视角理解多模态学习中的模态不平衡，设计 Sustained Boosting 算法（共享编码器 + 多可配置分类器，同时优化分类和残差误差）配合自适应分类器分配（ACA），理论证明跨模态 gap loss 以 $\mathcal{O}(1/T)$ 收敛，在 CREMAD 等 6 个数据集上大幅超越 SOTA。

**[RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](multimodal_vlm/roborefer_towards_spatial_referring_with_reasoning_in_vision-language_models_for.md)**

:   提出 **RoboRefer**，一个 3D 感知的推理型 VLM，通过 **SFT + RFT** 两阶段训练策略（含度量敏感的过程奖励函数），在空间指代任务中实现精确的单步空间理解和多步空间推理，在 RefSpatial-Bench 上超越 Gemini-2.5-Pro 达 17.4%。

**[Sherlock: Self-Correcting Reasoning in Vision-Language Models](multimodal_vlm/sherlock_selfcorrecting_reasoning_in_visionlanguage_models.md)**

:   首个系统研究VLM推理自纠正能力的框架：发现现有推理VLM几乎不能自纠正（<10%出现aha moment），提出Sherlock三阶段训练框架（SFT冷启动→离线轨迹级偏好学习→在线自我迭代）仅用20K标注数据超越使用100K-260K数据的LLaVA-CoT/Mulberry/LlamaV-o1。

**[Sparse Autoencoders Learn Monosemantic Features in Vision-Language Models](multimodal_vlm/sparse_autoencoders_learn_monosemantic_features_in_visionlan.md)**

:   将Sparse Autoencoder (SAE)从LLM可解释性扩展到VLM领域，提出MonoSemanticity Score (MS)量化视觉神经元的单义性，发现SAE能将VLM中多义的神经元分解为单义特征，且可直接通过操控单个SAE神经元来steering LLaVA的输出（插入或抑制概念），无需修改LLM。

**[SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning](multimodal_vlm/srpo_enhancing_multimodal_llm_reasoning_via_reflection-aware_reinforcement_learn.md)**

:   提出 SRPO（Self-Reflection enhanced reasoning with Group Relative Policy Optimization），一个两阶段反思感知 RL 框架：第一阶段用大模型生成反思数据做 SFT cold-start，第二阶段设计反思感知奖励函数在 GRPO 中强化简洁有效的自我反思能力，在 MathVista/MathVision/MMMU-Pro 等多模态推理基准上以 7B/32B 模型显著超越同规模 SOTA。

**[Systematic Reward Gap Optimization for Mitigating VLM Hallucinations](multimodal_vlm/systematic_reward_gap_optimization_for_mitigating_vlm_hallucinations.md)**

:   提出 Topic-level Preference Rewriting（TPR），通过 topic 级别的细粒度语义控制系统性优化偏好数据中的 reward gap 配置，结合课程学习策略逐步提高负样本难度，在多个幻觉基准上实现约 93% 的幻觉减少。

**[The Illusion of Progress? A Critical Look at Test-Time Adaptation for Vision-Language Models](multimodal_vlm/the_illusion_of_progress_a_critical_look_at_testtime_adaptat.md)**

:   提出TTA-VLM benchmark，在统一实验条件下评估8种episodic和7种online测试时适应(TTA)方法在15个数据集上的表现，发现三个令人意外的结论：(1) 现有TTA方法相比早期TPT基线提升有限；(2) TTA与训练时微调方法协作效果差；(3) 准确率提升以牺牲校准、OOD检测和鲁棒性为代价。

**[The Narrow Gate: Localized Image-Text Communication in Native Multimodal Models](multimodal_vlm/the_narrow_gate_localized_imagetext_communication_in_native.md)**

:   发现原生多模态VLM（如Chameleon、Emu3）中图像到文本的跨模态信息传递竟然集中在单一的end-of-image [EOI] token上（"narrow gate"机制），而非原生VLM（如LLaVA）则通过多个图像token分布式传递信息；删除[EOI]的attention可导致native模型性能崩溃，而修改[EOI]表示可精确控制模型的语义输出。

**[To Think or Not To Think: A Study of Explicit Thinking in Rule-Based Visual Reinforcement Fine-Tuning](multimodal_vlm/think_or_not_think_a_study_of_explicit_thinking_in_rule-based_visual_reinforceme.md)**

:   系统研究了基于规则的强化微调（RFT）中显式思维过程的必要性，发现视觉感知任务中"不思考"的RFT（No-Thinking-RFT）往往优于传统的"先思考再回答"策略，并提出了自适应思维方法让模型根据自身能力和任务复杂度决定是否思考。

**[TRoVe: Discovering Error-Inducing Static Feature Biases in Temporal Vision-Language Models](multimodal_vlm/trove_discovering_errorinducing_static_feature_biases_in_tem.md)**

:   TRoVe 提出一个自动化诊断框架，用于发现 temporal VLM 在时序理解任务中错误依赖的静态特征偏置；它通过从验证集提取候选静态特征，并同时评估这些特征对错误率的影响与模型对其依赖程度，在 101 个带偏置真值标注的 temporal VLM 上较最强基线提升 28.6%，还能进一步辅助 test-time 改善模型表现。

**[Unveiling Chain of Step Reasoning for Vision-Language Models with Fine-grained Rewards](multimodal_vlm/unveiling_chain_of_step_reasoning_for_visionlanguage_models.md)**

:   提出Chain-of-Step (CoS)推理框架：将VLM的推理链分解为结构化步骤（Name+Thought+Reflection），训练Process Reward Model (PRM)提供步骤级精细奖励，通过迭代DPO和step-level beam search显著提升VLM推理能力——在InternVL-2.5-MPO-8B上平均提升4.0%达到73.4%，并揭示"对VLM而言推理质量比长度更重要"。

**[VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](multimodal_vlm/vagen_reinforcing_world_model_reasoning_for_multi-turn_vlm_agents.md)**

:   提出VAGEN框架，通过将VLM智能体的推理过程结构化为StateEstimation和TransitionModeling来构建内部世界模型，结合WorldModeling Reward和Bi-Level GAE实现高效的多轮RL训练，使3B模型（0.82）超越GPT-5（0.75）和Gemini 2.5 Pro（0.67）。

**[VIPAMIN: Visual Prompt Initialization via Embedding Selection and Subspace Expansion](multimodal_vlm/vipamin_visual_prompt_initialization_via_embedding_selection_and_subspace_expans.md)**

:   提出VIPAMIN——一种零额外参数的视觉prompt初始化策略，通过注意力引导的语义匹配（Matching）和正交子空间注入（Orthogonalizing）两个模块，解决自监督VPT中prompt注意力均匀化和子空间坍塌两大失效模式，仅需单次前向传播即在24个视觉任务上刷新SOTA。

**[Visual Instruction Bottleneck Tuning](multimodal_vlm/visual_instruction_bottleneck_tuning.md)**

:   首次将信息瓶颈（IB）原理应用于多模态大语言模型的端到端指令微调，提出Visual Instruction Bottleneck Tuning（Vittle），在LLM内部插入轻量瓶颈层学习最小充分表征，在30种分布偏移场景下一致提升鲁棒性，同时不牺牲标准基准性能。

**[VL-SAE: Interpreting and Enhancing Vision-Language Alignment with a Unified Concept Set](multimodal_vlm/vlsae_interpreting_and_enhancing_visionlanguage_alignment_wi.md)**

:   提出VL-SAE，一种带有距离编码器和模态特定解码器的稀疏自编码器，将视觉和语言表示的语义映射到统一概念集，从而解释和增强VLM的视觉-语言对齐机制，在零样本分类平均提升0.6-0.9%，在POPE幻觉消除上超越专用方法VCD。

**[VT-FSL: Bridging Vision and Text with LLMs for Few-Shot Learning](multimodal_vlm/vt-fsl_bridging_vision_and_text_with_llms_for_few-shot_learning.md)**

:   提出VT-FSL框架，通过跨模态迭代提示（CIP）联合利用类名和支持图像驱动LLM生成精确文本描述并零样本合成语义一致图像，再通过核化体积对比学习（CGA）实现全局非线性跨模态对齐，在10个少样本学习基准上平均提升4.2%分类准确率。

**[STRUCTURE: With Limited Data for Multimodal Alignment, Let the Structure Guide You](multimodal_vlm/with_limited_data_for_multimodal_alignment_let_the_structure_guide_you.md)**

:   提出 STRUCTURE 正则化和基于表示相似度的层选择策略，仅用少量配对数据（数万对，不到常规方法的1%）即可实现冻结单模态基础模型的高质量跨模态对齐，在24个零样本分类和检索基准上平均提升51.6%和91.8%。

---

## 📦 模型压缩 { #model_compression }

**[3DID: Direct 3D Inverse Design for Aerodynamics with Physics-Aware Optimization](model_compression/3did_direct_3d_inverse_design_for_aerodynamics_with_physics-aware_optimization.md)**

:   提出 3DID 框架，通过学习物理-几何统一的三平面隐空间表示 + 目标梯度引导扩散采样 + 拓扑保持精炼的两阶段策略，从随机噪声开始直接在完整 3D 空间中进行逆向设计，在车辆气动外形优化上，模拟阻力（Sim-Drag）相比最优基线降低 13.6%。

**[4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming](model_compression/4dgcpro_efficient_hierarchical_4d_gaussian_compression_for_p.md)**

:   提出层级化的4D高斯压缩框架4DGCPro，通过感知加权的层级高斯表示、运动感知自适应分组和端到端熵优化训练，在单一模型内实现多码率渐进式体积视频流媒体，可在移动设备上实时解码和渲染，RD性能超越现有SOTA。

**[A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](model_compression/a-thought_efficient_reasoning_via_bidirectional_compression_for_low-resource_set.md)**

:   提出 A*-Thought——基于 A* 搜索算法的 CoT 压缩框架，通过双向重要性评分（BIS）衡量每个推理步骤对问题和答案的相关性，结合路径级 A* 搜索在指数级搜索空间中高效找到最紧凑的推理路径，在 512 token 预算下将 QwQ-32B 准确率提升 2.39 倍，在 4096 token 预算下减少约 50% 输出 token 且几乎不损失准确率。

**[A Granular Study of Safety Pretraining under Model Abliteration](model_compression/a_granular_study_of_safety_pretraining_under_model_abliteration.md)**

:   本文系统地研究了 model abliteration（一种推理时激活空间编辑攻击）对不同数据驱动安全预训练阶段的影响，发现仅依赖 refusal 训练的安全机制极易被攻破，而 **组合多种安全信号**（safe-only 过滤 + 改写 + metatag + refusal）可使安全行为分散到更广泛的表征空间、从而更难被单一方向投影移除。

**[A is for Absorption: Studying Feature Splitting and Absorption in Sparse Autoencoders](model_compression/a_is_for_absorption_studying_feature_splitting_and_absorption_in_sparse_autoenco.md)**

:   发现并系统研究了 SAE 中的"特征吸收"现象：看似单义的 SAE latent 会在特定 token 上不激活，其特征方向被更具体的子 latent "吸收"，这是层级特征+稀疏性损失的必然结果，对 SAE 用于可靠解释 LLM 构成根本挑战。

**[A Partition Cover Approach for Tokenization](model_compression/a_partition_cover_approach_to_tokenization.md)**

:   将分词（tokenization）问题重新建模为**分区覆盖（partition cover）**优化问题，证明其为NP-hard，并提出多项式时间的贪心算法GreedTok，在压缩率和1B参数LLM预训练下游任务上均优于BPE。

**[A Token is Worth over 1,000 Tokens: Efficient Knowledge Distillation through Low-Rank Clone](model_compression/a_token_is_worth_over_1000_tokens_efficient_knowledge_distillation_through_low-r.md)**

:   提出 Low-Rank Clone (LRC)，通过可学习低秩投影矩阵将 teacher 权重压缩为 student 权重（软剪枝），同时对齐 attention 和 FFN 的中间激活（激活克隆），仅用 20B tokens 训练的 1.7B 模型即超过用 36T tokens 训练的 Qwen3-1.7B（64.98 vs 63.17），实现 **1000 倍训练效率提升**。

**[Accurate and Efficient Low-Rank Model Merging in Core Space](model_compression/accurate_and_efficient_low-rank_model_merging_in_core_space.md)**

:   提出 Core Space Merging 框架——通过在低秩 LoRA 矩阵的公共参考基空间中进行模型合并，**无信息损失**地将合并操作从 $m \times n$ 全尺寸空间压缩到 $Tr \times Tr$ 紧凑空间（$T$ 为任务数，$r$ 为 LoRA 秩），在 Llama 3 8B 上达到 SOTA 合并精度同时计算成本降低数个数量级。

**[Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs](model_compression/adaptive_kernel_design_for_bayesian_optimization_is_a_piece_of_cake_with_llms.md)**

:   提出 CAKE (Context-Aware Kernel Evolution)，利用 LLM 作为遗传算法的交叉和变异算子，在贝叶斯优化过程中自适应地生成和进化 GP 核函数表达式，结合 BAKER 排序机制平衡模型拟合（BIC）与期望改进（EI），在超参数优化、控制器调参和光子芯片设计等任务上持续超越固定核和自适应核基线。

**[Adaptive Originality Filtering: Rejection-Based Prompting and RiddleScore for Culturally Grounded Multilingual Riddle Generation](model_compression/adaptive_originality_filtering_rejection_based_prompting_and_riddlescore_for_cul.md)**

:   提出 Adaptive Originality Filtering (AOF)——一种基于语义拒绝采样的提示策略，通过 MiniLM 嵌入的余弦相似度过滤重复/模板化输出，强制 LLM 生成更新颖、多样且文化匹配的多语言谜语；同时提出 RiddleScore 复合评估指标（Novelty + Diversity + Fluency + Alignment），与人类评分相关性达 $\rho=0.83$。

**[Adaptive Prediction-Powered AutoEval with Reliability and Efficiency Guarantees](model_compression/adaptive_predictionpowered_autoeval_with_reliability_and_eff.md)**

:   提出R-AutoEval+，通过e-value赌注算法自适应调整对合成数据（LLM评判器）的依赖权重，首次同时提供有限样本可靠性保证和可证明的采样效率改善，在GSM8K上比纯真实数据方法节省87个token。

**[Adaptive Stochastic Coefficients for Accelerating Diffusion Sampling](model_compression/adaptive_stochastic_coefficients_for_accelerating_diffusion_sampling.md)**

:   通过理论分析 ODE 和 SDE 求解器的互补弱点（ODE 积累不可消除的梯度误差，SDE 在少步时离散化误差放大），提出 AdaSDE——在每个去噪步引入可学习随机系数 $\gamma_i$ 控制噪声注入强度，通过轻量蒸馏优化，在 5 NFE 下实现 CIFAR-10 FID 4.18、FFHQ FID 8.05 的 SOTA。

**[AdmTree: Compressing Lengthy Context with Adaptive Semantic Trees](model_compression/admtree_compressing_lengthy_context_with_adaptive_semantic_trees.md)**

:   提出 AdmTree——一种自适应层次化上下文压缩框架,通过信息密度驱动的动态分段构建叶 gist token，再用二叉语义树底向上聚合实现多粒度语义保留，解决了显式方法丢失局部细节和隐式方法位置偏差的双重问题,在 LongBench 上比 SOTA 基线 Activation Beacon 高 10%+。

**[AI-Generated Video Detection via Perceptual Straightening](model_compression/ai-generated_video_detection_via_perceptual_straightening.md)**

:   提出 ReStraV 方法，基于"感知拉直"假说（真实视频在神经表示空间形成更直的轨迹），利用 DINOv2 特征空间中的时间曲率和步距统计量训练轻量分类器检测 AI 生成视频，在 VidProM 上达到 97.17% 准确率和 98.63% AUROC，推理仅需 ~48ms。

**[AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise](model_compression/autodiscovery_open-ended_scientific_discovery_via_bayesian_surprise.md)**

:   AutoDiscovery 提出用贝叶斯惊奇度（Bayesian Surprise）作为开放式科学发现的客观奖励信号——通过 LLM 采样估计先验/后验信念分布的 KL 散度，配合 MCTS+渐进展宽在假设空间中探索，在 21 个真实数据集上比贪心/束搜索产生 5-29% 更多的惊奇发现，人类评估确认贝叶斯惊奇度与专家"惊讶感"的一致性（0.67）远超 LLM 自身评估的"新颖性"和"有用性"。

**[AutoJudge: Judge Decoding Without Manual Annotation](model_compression/autojudge_judge_decoding_without_manual_annotation.md)**

:   AutoJudge 自动化了 Judge Decoding 中"重要 token"的标注——通过半贪心搜索替换不匹配 token 并检查答案是否改变来标注重要性，训练逻辑回归分类器预测 token 重要性，使投机解码每轮接受 40+ token（vs 标准 ~20），在 GSM8K 上加速 1.5× 且准确率损失 <1%。

**[BaRISTA: Brain-Scale Informed Spatiotemporal Representation of Human Intracranial EEG](model_compression/barista_brain_scale_informed_spatiotemporal_representation_of_human_intracranial.md)**

:   BaRISTA 系统探索 iEEG Transformer 的空间编码尺度（电极/脑区/脑叶），发现脑区级编码 + 空间掩码重建在语言任务解码上达 86.2% AUC（vs PopT 79.5%），编码尺度选择的影响 > 掩码策略选择，且跨被试泛化性好。

**[Benford's Curse: Tracing Digit Bias to Numerical Hallucination in LLMs](model_compression/benfords_curse_tracing_digit_bias_to_numerical_hallucination_in_llms.md)**

:   本文发现 LLM 的数值幻觉根源于预训练语料中符合 Benford 定律的数字频率分布——数字 1 出现概率 ~30% 而数字 9 仅 ~5%，这种偏差被 FFN 后期层的特定"数字选择性神经元"内化，提出数字选择性分数（DSC）定位偏差神经元并通过剪枝 0.01% 的神经元修正 1.36-3.49% 的错误预测。

**[Better Estimation of the Kullback-Leibler Divergence Between Language Models](model_compression/better_estimation_of_the_kullback--leibler_divergence_between_language_models.md)**

:   提出 KL 散度的 Rao-Blackwell 化 Monte Carlo 估计器——在每个位置对下一个 token 的分布求精确 KL（而非只用采样的 token），理论证明无偏且方差严格不超过标准 MC 估计器，零额外计算开销，在 RLHF 情感控制任务中使训练更稳定、模型更频繁出现在 Pareto 前沿（78%）。

**[Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning](model_compression/beyond_accuracy_dissecting_mathematical_reasoning_for_llms_u.md)**

:   提出 SPARKLE 三轴分析框架（计划执行、知识整合、子问题分解）细粒度剖析 RL 如何改变 LLM 推理行为，发现 RL 主要增强了知识整合能力和计划灵活性而非计划执行能力，并提出 SparkleRL-PSS 多阶段 RL 训练 pipeline 通过 partial step scaffolding 有效利用难题数据。

**[Beyond Higher Rank: Token-wise Input-Output Projections for Efficient Low-Rank Adaptation](model_compression/beyond_higher_rank_token-wise_input-output_projections_for_efficient_low-rank_ad.md)**

:   TopLoRA 从输入-输出投影角度分析 LoRA 的表达能力，发现所有 token 共享同一投影矩阵是关键瓶颈，提出通过可学习的 token 级对角矩阵 $\Sigma_X$ 动态调整 LoRA 权重（$\Delta W_X = B\Sigma_X A$），在不增加秩的前提下实现细粒度适配，跨任务一致优于 LoRA 2-3%。

**[Beyond Random: Automatic Inner-Loop Optimization in Dataset Distillation](model_compression/beyond_random_automatic_inner-loop_optimization_in_dataset_distillation.md)**

:   提出 AT-BPTT（自适应截断 BPTT），将 DNN 训练分为早/中/晚三阶段并自适应调整截断策略和窗口大小，在 CIFAR-10/100/Tiny-ImageNet/ImageNet-1K 上平均提升 3-17%，同时实现 3.9× 加速和 63% 内存节省。

**[Bézier Splatting for Fast and Differentiable Vector Graphics Rendering](model_compression/bezier_splatting_for_fast_and_differentiable_vector_graphics_rendering.md)**

:   Bézier Splatting 将 Gaussian Splatting 框架与 Bézier 曲线结合，沿曲线均匀采样 2D Gaussian 点，通过 α-blending 渲染实现可微矢量图形，前向 30× / 反向 150× 加速（相比 DiffVG），同时保持或超越 LIVE 等方法的图像质量。

**[Binary Quadratic Quantization: Beyond First-Order Quantization for Real-Valued Matrix Compression](model_compression/binary_quadratic_quantization_beyond_first-order_quantization_for_real-valued_ma.md)**

:   BQQ 提出二次二值量化——用二值矩阵的乘积（而非线性组合）表示权重矩阵，突破传统一阶量化的表达能力限制，通过扩展 AMFD（退火均场下降）到 PUBO 问题求解混合整数优化，在 2-bit 无数据 ViT 量化上实现从 10.83% 到 58.25% 的准确率飞跃。

**[BioBench: A Blueprint to Move Beyond ImageNet for Scientific ML Benchmarks](model_compression/biobench_a_blueprint_to_move_beyond_imagenet_for_scientific_ml_benchmarks.md)**

:   提出 BioBench——一个统一 9 个生态视觉任务、4 个分类界、6 种图像模态、310 万张图像的基准，证明 ImageNet top-1 准确率仅解释 34% 的生态任务方差，在 >75% 精度的前沿模型中 30% 的排名是错误的。

**[C-LoRA: Contextual Low-Rank Adaptation for Uncertainty Estimation in Large Language Models](model_compression/c-lora_contextual_low-rank_adaptation_for_uncertainty_estimation_in_large_langua.md)**

:   提出 C-LoRA，通过引入轻量级上下文模块使 LoRA 低秩矩阵的分布依赖于输入数据，实现样本级的异方差不确定性估计，在少样本微调场景中显著改善校准质量。

**[CAS-Spec: Cascade Adaptive Self-Speculative Decoding for On-the-Fly Lossless Inference Acceleration of LLMs](model_compression/casspec_cascade_adaptive_selfspeculative_decoding_for_onthef.md)**

:   CAS-Spec 通过 Dynamically Switchable Inference Acceleration (DSIA) 策略（如不同程度的 layer sparsity）从目标模型自身构建多级 draft 模型层级，配合 Dynamic Tree Cascade (DyTC) 算法基于在线 acceptance rate 和延迟预测自适应路由 draft 模型和分配 draft 长度，在完全 training-free 的条件下实现 1.1×-2.3× 的无损推理加速，DyTC 比 cascade 和 tree baseline 分别提升 47% 和 48%。

**[ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](model_compression/chunkkv_semanticpreserving_kv_cache_compression_for_efficien.md)**

:   ChunkKV 将 KV cache 压缩的基本单元从离散 token 提升为语义 chunk（连续 token 组），通过 chunk 级 attention score 聚合来选择保留哪些语义完整的片段，并利用 chunk 带来的高跨层索引相似性实现 layer-wise index reuse，在 10% 压缩率下比 SnapKV/PyramidKV 提升最高 8.7%，吞吐量提升 26.5%。

**[CodeGEMM: A Codebook-Centric Approach to Efficient GEMM in Quantized LLMs](model_compression/codegemm_a_codebook-centric_approach_to_efficient_gemm_in_quantized_llms.md)**

:   提出 CodeGEMM，一种以 codebook 为中心的 GEMM kernel，通过预计算 centroid 与 activation 的内积并缓存为 Psumbook，替代传统反量化流程，在 2-bit 量化 LLM 上实现 1.83×（8B）到 8.93×（70B）的端到端加速。

**[Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers](model_compression/compress_gather_and_recompute_reforming_long-context_processing_in_transformers.md)**

:   提出 REFORM 推理框架，通过"压缩—检索—重算"三阶段流水线高效处理超长上下文（百万级 token），在 RULER 和 BABILong 上相比最强基线分别提升 52% 和 34%，同时降低 30% 推理时间和 5% 峰值显存。

**[ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts](model_compression/conceptscope_characterizing_dataset_bias_via_disentangled_visual_concepts.md)**

:   提出 ConceptScope 框架，利用在视觉基础模型表征上训练的稀疏自编码器（SAE）自动发现和量化数据集中的视觉概念偏差，无需人工标注即可将概念分类为 target / context / bias 三类。

**[Conditional Distribution Compression via the Kernel Conditional Mean Embedding](model_compression/conditional_distribution_compression_via_the_kernel_conditional_mean_embedding.md)**

:   首次提出针对**条件分布**（而非联合分布）的压缩算法，利用核条件均值嵌入（KCME）定义新度量 AMCMD，并设计线性时间算法 ACKIP 构建保留条件分布统计特性的压缩数据集。

**[Correlation Dimension of Auto-Regressive Large Language Models](model_compression/correlation_dimension_of_auto-regressive_large_language_models.md)**

:   引入源于分形几何的**相关维数（correlation dimension）**作为衡量自回归语言模型感知文本复杂度的指标，揭示了传统 perplexity 无法捕捉的长程结构特性，可检测幻觉和退化文本。

**[Curiosity-driven RL for Symbolic Equation Solving](model_compression/curiosity-driven_rl_for_symbolic_equation_solving.md)**

:   将好奇心驱动探索（RND、ICM 等）与基于表达式树的图动作空间结合，使 PPO 智能体能够求解包含根号、指数和三角函数的非线性方程，超越了此前仅限于线性方程的 RL 方法。

**[Curvature Tuning: Provable Training-free Model Steering From a Single Parameter](model_compression/curvature_tuning_provable_training-free_model_steering_from_a_single_parameter.md)**

:   提出 Curvature Tuning（CT），通过在激活函数中注入单个超参数 $\beta$ 来可证明地调节模型决策边界的曲率，无需修改权重即可提升泛化和鲁棒性，同时作为微调方法参数量远少于 LoRA rank 1。

**[Data Efficient Adaptation in Large Language Models via Continuous Low-Rank Fine-Tuning](model_compression/data_efficient_adaptation_in_large_language_models_via_continuous_low-rank_fine-.md)**

:   提出 DEAL 框架，通过小波核特征过滤保留 LoRA 低秩矩阵中的历史知识核心特征，结合受控知识更新模块和非对称正则化，实现 LLM 在小样本持续微调中学新不忘旧。

**[Dataset Distillation for Pre-Trained Self-Supervised Vision Models](model_compression/dataset_distillation_for_pre-trained_self-supervised_vision_models.md)**

:   提出 Linear Gradient Matching 方法，为预训练自监督视觉模型蒸馏合成数据集：每类仅需一张合成图就能训练出接近全数据集表现的线性分类器，且蒸馏图像可跨模型架构迁移。

**[DeepTraverse: A Depth-First Search Inspired Network for Algorithmic Visual Understanding](model_compression/deeptraverse_a_depth-first_search_inspired_network_for_algorithmic_visual_unders.md)**

:   受深度优先搜索（DFS）算法启发，设计了 DeepTraverse 视觉骨干网络，通过参数共享的递归探索模块和自适应通道校准模块，在极少参数下实现高竞争力的图像分类性能。

**[DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method](model_compression/deltaflow_an_efficient_multi-frame_scene_flow_estimation_method.md)**

:   提出 DeltaFlow (ΔFlow)，通过体素帧间差分（Δ scheme）提取运动线索，实现特征尺寸不随帧数增长的多帧场景流估计，在 Argoverse 2/Waymo/nuScenes 上达到 SOTA 且比次优多帧方法快 2 倍。

**[Dense Backpropagation Improves Training for Sparse Mixture-of-Experts](model_compression/dense_backpropagation_improves_training_for_sparse_mixture-of-experts.md)**

:   提出 Default MoE 方法，用指数移动平均（EMA）近似非激活 expert 的输出，使 MoE router 获得稠密梯度更新，在不显著增加计算开销的情况下提升稀疏 MoE 的训练性能。

**[Dependency Parsing is More Parameter-Efficient with Normalization](model_compression/dependency_parsing_is_more_parameter-efficient_with_normalization.md)**

:   揭示依存句法/语义分析中 biaffine scoring 缺乏归一化导致模型过参数化，通过简单的 $1/\sqrt{d}$ 缩放即可在减少高达 85% BiLSTM 参数的同时匹配甚至超越原始性能。

**[Deterministic Continuous Replacement: Fast and Stable Module Replacement in Pretrained Transformers](model_compression/deterministic_continuous_replacement_fast_and_stable_module_replacement_in_pretr.md)**

:   DCR 通过确定性退火权重 α(t) 混合 teacher 和 student 模块输出，消除了随机门控（如 BERT-of-Theseus）带来的梯度方差，在冷启动模块替换场景下实现更快收敛和更强的特征对齐。

**[Disentangling Latent Shifts of In-Context Learning with Weak Supervision](model_compression/disentangling_latent_shifts_of_in-context_learning_with_weak_supervision.md)**

:   WILDA 将 ICL 视为弱监督信号，用 teacher-student 框架将示例引发的潜在偏移编码进轻量 LoRA 适配器，实现无需重复 prompting 的高效推理，且 student 通过伪标签修正和覆盖扩展超越 teacher（弱到强泛化）。

**[DisMo: Disentangled Motion Representations for Open-World Motion Transfer](model_compression/dismo_disentangled_motion_representations_for_openworld_moti.md)**

:   DisMo 通过双流架构（运动提取器 + 帧生成器）和图像空间重建目标，从原始视频中学习与外观、姿态、类别无关的抽象运动表征，实现跨类别/跨视角的开放世界运动迁移，并在零样本动作分类上大幅超越 V-JEPA 等视频表征模型。

**[DP-LLM: Runtime Model Adaptation with Dynamic Layer-wise Precision Assignment](model_compression/dp-llm_runtime_model_adaptation_with_dynamic_layer-wise_precision_assignment.md)**

:   DP-LLM 发现每层的量化敏感度在解码步间动态变化，提出基于 relative error 的动态逐层精度选择机制，在运行时根据输入为每层分配精度（h-bit 或 l-bit），实现了优于静态混合精度的性能-延迟权衡。

**[DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning](model_compression/dragon_guard_llm_unlearning_in_context_via_negative_detection_and_reasoning.md)**

:   DRAGON 提出无需微调基座模型的系统性 LLM 遗忘框架：通过双层检测模块识别需遗忘的 prompt，再由专门微调的 guard 模型生成 CoT 推理指令实现上下文干预，在保持模型通用能力的同时有效删除隐私/有害知识。

**[DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs](model_compression/duogpt_training-free_dual_sparsity_through_activation-aware_pruning_in_llms.md)**

:   提出 DuoGPT，一种将激活稀疏（activation sparsity）重新解释为动态结构化权重稀疏、并与非结构化权重剪枝相结合的双稀疏（dual-sparse）框架，通过扩展 OBC 框架引入激活感知校准和稠密模型输出残差修正项，在不需要重训练的情况下实现 LLM 解码阶段的显著加速与内存节省。

**[Elastic ViTs from Pretrained Models without Retraining](model_compression/elastic_vits_from_pretrained_models_without_retraining.md)**

:   SnapViT 提出一种后训练结构化剪枝方法：结合自监督梯度的局部 Hessian 和进化算法估计的全局跨模块相关性，无需重训练或标签即可在一次运行中生成连续稀疏度的弹性 ViT 子网络，在 A100 上仅需不到 5 分钟。

**[EMLoC: Emulator-based Memory-efficient Fine-tuning with LoRA Correction](model_compression/emloc_emulator-based_memory-efficient_fine-tuning_with_lora_correction.md)**

:   EMLoC 通过对原始模型做 activation-aware SVD 构建轻量级 emulator 进行 LoRA 微调，并提出 LoRA 校正算法弥补 emulator 与原模型的不对齐，使得微调内存开销降至与推理持平，在单张 24GB GPU 上即可微调 38B 模型。

**[Enhancing Semi-supervised Learning with Zero-shot Pseudolabels](model_compression/enhancing_semi-supervised_learning_with_zero-shot_pseudolabels.md)**

:   ZeroMatch 提出两阶段框架将基础模型的零样本伪标签与半监督学习相结合：先用知识蒸馏初始化学生模型，再以辅助 KD loss 防止灾难性遗忘的方式执行 SSL 训练，在 6 个视觉/NLP 基准上一致超越标准 SSL 和零样本增强方法。

**[Exact Expressive Power of Transformers with Padding](model_compression/exact_expressive_power_of_transformers_with_padding.md)**

:   本文精确刻画了带 padding 的 Transformer 的表达能力：固定深度 + 多项式 padding 恰好等于 $\mathsf{FO}$-uniform $\mathsf{TC}^0$，进一步结合 $O(\log^d n)$ looping 恰好等于 $\mathsf{FO}$-uniform $\mathsf{TC}^d$，polylog looping 收敛到 $\mathsf{NC}$，为 padding/looping 作为可并行推理时计算提供了完整理论基础。

**[ExPO: Unlocking Hard Reasoning with Self-Explanation-Guided Reinforcement Learning](model_compression/expo_unlocking_hard_reasoning_with_self-explanation-guided_reinforcement_learnin.md)**

:   提出 Self-Explanation Policy Optimization (ExPO)，一种通过让模型在给定正确答案条件下自主生成推理链（self-explanation）作为正样本的模块化框架，解决 GRPO 等 RL 后训练方法在困难推理任务上因缺乏有效正样本而无法学习（分布锐化）的根本问题——ExPO 生成的自解释样本既在当前策略分布内（in-distribution），又能提供正向学习信号，可无缝集成到 DPO 和 GRPO 中。

**[Eyes Wide Open: Ego Proactive Video-LLM for Streaming Video](model_compression/eyes_wide_open_ego_proactive_videollm_for_streaming_video.md)**

:   定义"第一视角流式视频主动理解"新任务——给定ego-streaming视频，AI助手在恰当时机主动回答多样化、随事件演变的问题，同时保持感知与推理的同步。提出ESTP-Bench评估框架、ESTP-F1指标，以及含数据引擎、多阶段训练和主动动态压缩的完整技术pipeline（VideoLLM-EyeWO），在ESTP-Bench上比最强baseline MiniCPM-V高11.8%。

**[FALQON: Accelerating LoRA Fine-tuning with Low-Bit Floating-Point Arithmetic](model_compression/falqon_accelerating_lora_fine-tuning_with_low-bit_floating-point_arithmetic.md)**

:   FALQON 通过将 LoRA 适配器直接融合 (meld) 到 FP8 量化的骨干权重中，消除了单独 LoRA 路径引入的小矩阵量化开销，结合高效梯度计算和行级代理更新机制，实现了相比现有量化 LoRA 方法约 3 倍的训练加速。

**[Fantastic Features and Where to Find Them: A Probing Method to Combine Features from Multiple Foundation Models](model_compression/fantastic_features_and_where_to_find_them_a_probing_method_to_combine_features_f.md)**

:   提出 ComBo，一种基于 probing 的轻量级 adapter，通过仿射投影压缩多个冻结基础模型多层激活，再用小型 transformer 融合，无需反向传播即可高效整合多模型互补表征，在 VTAB-1k 上超越先前 probing 方法并匹配蒸馏方法。

**[FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed](model_compression/fastdinov2_frequency_based_curriculum_learning_improves_robustness_and_training_.md)**

:   提出 FastDINOv2，一种两阶段频率课程学习策略：先用低分辨率图像训练 75% epochs 学习低频特征以加速收敛，再用全分辨率+高斯噪声 patching 训练 25% epochs 平衡频率偏置，实现 1.6× 加速、2.25× FLOPs 节省，同时增强鲁棒性。

**[FastLongSpeech: Enhancing Large Speech-Language Models for Efficient Long-Speech Processing](model_compression/fastlongspeech_enhancing_large_speech-language_models_for_efficient_long-speech_.md)**

:   提出 FastLongSpeech，通过迭代融合策略压缩冗余语音表征和动态压缩训练转移短语音能力到长语音场景，使 LSLM 无需长语音训练数据即可高效处理长语音，在长语音 QA 上实现最优性能且推理效率提升 70%。

**[FiRA: Can We Achieve Full-Rank Training of LLMs Under Low-Rank Constraint?](model_compression/fira_can_we_achieve_full-rank_training_of_llms_under_low-rank_constraint.md)**

:   提出 Fira，首个在低秩约束下实现全秩训练（全秩梯度+全秩权重）的 LLM 训练框架，通过观察到低秩与全秩训练中优化器的缩放因子高度相似，用低秩缩放因子近似校正子空间外梯度，配合 norm-growth limiter 防止 loss spike，在预训练和微调中均超越 LoRA 和 GaLore。

**[FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts](model_compression/flylora_boosting_task_decoupling_and_parameter_efficiency_via_implicit_rank-wise.md)**

:   FlyLoRA 受飞蝇嗅觉回路启发，将 LoRA 的下投影矩阵 $A$ 替换为冻结的稀疏随机投影，通过 top-$k$ 激活值选择实现隐式 rank-wise MoE 路由，在消除路由参数的同时减少任务内干扰，并利用随机投影的近正交性天然支持多任务模型合并。

**[Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models](model_compression/gated_integration_of_low-rank_adaptation_for_continual_learning_of_large_languag.md)**

:   提出 GainLoRA，为持续学习中每个新任务的 LoRA 分支引入**门控模块**生成自适应集成系数，通过正交约束使新分支对旧任务的输出趋近于零，从而有效缓解灾难性遗忘。

**[Geometric Data Valuation via Leverage Scores](model_compression/geometric_data_valuation_via_leverage_scores.md)**

:   提出基于**统计杠杆分数（leverage scores）**的几何数据估值方法，作为 Data Shapley 值的高效代理，满足对称性、效率性和虚拟玩家等公理，并通过 ridge leverage 扩展解决维度饱和问题，提供 $O(\varepsilon)$ 近似最优的理论保证。

**[GoRA: Gradient-Driven Adaptive Low Rank Adaptation](model_compression/gora_gradient-driven_adaptive_low_rank_adaptation.md)**

:   提出 GoRA，利用**预计算梯度信息**在训练前同时完成自适应秩分配和权重初始化——基于参数敏感度分配各层 rank，用梯度伪逆初始化 $B$ 矩阵使初始输出近似一步梯度下降，统一解决 LoRA 的两大瓶颈。

**[Graph Your Own Prompt](model_compression/graph_your_own_prompt.md)**

:   提出图一致性正则化（GCR）框架，通过在网络任意深度插入无参数的图一致性层（GCL），将中间特征的关系图与基于预测的类感知语义图对齐，以自我提示的方式促进语义一致的特征学习，在不修改架构和不增加参数的前提下提升分类泛化性能。

**[GraphKeeper: Graph Domain-Incremental Learning via Knowledge Disentanglement and Preservation](model_compression/graphkeeper_graph_domain-incremental_learning_via_knowledge_disentanglement_and_.md)**

:   提出 GraphKeeper 框架应对**图域增量学习（Graph Domain-IL）**中的灾难性遗忘，通过域特异性 LoRA 参数隔离 + 领域内/间解耦 + 基于岭回归的无偏差知识保存三组件，比次优方法提升 6.5%-16.6%，且可无缝集成图基础模型。

**[GraSS: Scalable Data Attribution with Gradient Sparsification and Sparse Projection](model_compression/grass_scalable_data_attribution_with_gradient_sparsification_and_sparse_projecti.md)**

:   提出 GraSS 与 FactGraSS 两阶段梯度压缩算法，利用逐样本梯度的固有稀疏性实现**亚线性**时间与空间复杂度（$O(k')$），在十亿参数模型上比 SOTA 基线 LoGra 快 **165%**，同时保持数据归因质量。

**[Graver: Generative Graph Vocabularies for Robust Graph Foundation Models Fine-tuning](model_compression/graver_generative_graph_vocabularies_for_robust_graph_foundation_models_fine-tun.md)**

:   提出 Graver 框架，通过 ego-graph 解耦提取可迁移子图词汇、graphon 专家建模词汇分布、MoE-CoE 路由选择性增强 support 样本，解决 GFM 少样本微调中因结构不匹配导致的不稳定性问题。

**[H-SPLID: HSIC-based Saliency Preserving Latent Information Decomposition](model_compression/h-splid_hsic-based_saliency_preserving_latent_information_decomposition.md)**

:   提出 H-SPLID，通过将隐空间显式分解为**显著（任务相关）**和**非显著（任务无关）**两个子空间，结合 HSIC 正则化实现信息压缩，证明预测偏差上界受显著子空间维度和 HSIC 控制，在无对抗训练条件下显著提升对非显著区域扰动的鲁棒性。

**[Hankel Singular Value Regularization for Highly Compressible State Space Models](model_compression/hankel_singular_value_regularization_for_highly_compressible_state_space_models.md)**

:   通过在训练中正则化 SSM 层的 **Hankel 奇异值核范数**促使其快速衰减，使训练后模型可用平衡截断压缩至原始阶数的 **10%** 而保持精度，并利用旋转矩阵块对角参数化将 Gramian 计算从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(n^2)$。

**[Heterogeneous Adversarial Play in Interactive Environments](model_compression/heterogeneous_adversarial_play_in_interactive_environments.md)**

:   提出 **HAP（Heterogeneous Adversarial Play）**，将教师-学生交互形式化为极小极大博弈：教师网络自动生成针对学生弱点的挑战任务，学生策略不断适应进化，形成无需手工设计的自适应课程——在多任务 RL 环境中超越 SOTA 基线，且生成的课程对人类学习者同样有效。

**[Homogeneous Keys, Heterogeneous Values: Exploiting Local KV Cache Asymmetry for Long-Context LLMs](model_compression/homogeneous_keys_heterogeneous_values_exploiting_local_kv_cache_asymmetry_for_lo.md)**

:   发现 LLM 注意力机制中一个被忽视的**局部 Key-Value 不对称性**——相邻 Key 具有同质性（相似注意力权重），而相邻 Value 呈异质分布——据此提出 **AsymKV** 无训练压缩框架：基于同质性合并 Key + 基于基数归一化的**无损** Value 表示，在 LongBench 上超越 H2O 达 **5 分**。

**[Hyperbolic Dataset Distillation](model_compression/hyperbolic_dataset_distillation.md)**

:   提出 HDD 方法，首次将双曲空间引入数据集蒸馏，通过在 Lorentz 双曲空间中匹配原始和合成数据的 Riemannian 质心来替代欧氏空间的分布匹配，利用双曲几何的层级加权特性让"更具代表性"的底层样本获得更高权重，在多个数据集上持续提升 DM/IDM 基线准确率。

**[Hyperbolic Fine-Tuning for Large Language Models](model_compression/hyperbolic_fine-tuning_for_large_language_models.md)**

:   发现 LLM token 嵌入具有幂律分布和树状双曲结构，据此提出 HypLoRA——在 Lorentz 双曲流形上直接执行低秩适配（避免切空间映射的相消效应），在算术推理和常识推理任务上相比标准 LoRA 取得显著提升（如 Qwen2.5-7B 上 M.AVG +7.5%）。

**[Infrequent Exploration in Linear Bandits](model_compression/infrequent_exploration_in_linear_bandits.md)**

:   提出 INFEX 框架，按给定调度表在探索步执行基线算法（如 LinUCB/LinTS）、其余时刻贪心选臂，证明只要探索次数超过 $\omega(\log T)$ 即可达到与全时刻探索相同的多项对数 regret，同时大幅降低计算开销（80%-99% 时间步为贪心）。

**[Jet-Nemotron: Efficient Language Model with Post Neural Architecture Search](model_compression/jet-nemotron_efficient_language_model_with_post_neural_architecture_search.md)**

:   NVIDIA 提出 PostNAS 流水线——从预训练全注意力模型出发，冻结 MLP 权重，通过四步搜索（全注意力层放置→线性注意力块选择→新注意力块 JetBlock 设计→硬件感知超参搜索）得到混合架构 Jet-Nemotron，2B 模型在 MMLU-Pro 上超越 Qwen3-1.7B 同时生成吞吐提升 47×。

**[KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments](model_compression/keydiff_key_similarity-based_kv_cache_eviction_for_long-context_llm_inference_in.md)**

:   提出 KeyDiff——一种无需注意力分数的 KV cache 驱逐策略，通过保留与其他 key 余弦相似度最低（即几何上最独特）的 key 来维护 cache，在严格内存约束的逐块推理场景下以 8K cache 在 LongBench 上仅损失 ≤0.04% 精度，同时端到端推理延迟减少最高 30%。

**[KINDLE: Knowledge-Guided Distillation for Prior-Free Gene Regulatory Network Inference](model_compression/kindle_knowledge-guided_distillation_for_prior-free_gene_regulatory_network_infe.md)**

:   提出 KINDLE 三阶段框架，通过知识蒸馏将先验引导的教师模型中学到的基因调控知识迁移到无先验的学生模型，在不依赖任何外部先验知识的情况下实现了基因调控网络（GRN）推断的 SOTA 性能。

**[Knowing When to Stop: Efficient Context Processing via Latent Sufficiency Signals](model_compression/knowing_when_to_stop_efficient_context_processing_via_latent_sufficiency_signals.md)**

:   本文提出 dynamic context cutoff，通过探测 Transformer 特定注意力头中编码的"信息充分性信号"，训练轻量分类器判断模型何时已获取足够上下文，实现提前终止处理，在6个QA数据集上平均提高3.4%准确率同时减少1.33×token消耗。

**[KTAE: A Model-Free Algorithm to Key-Tokens Advantage Estimation in Mathematical Reasoning](model_compression/ktae_a_model-free_algorithm_to_key-tokens_advantage_estimation_in_mathematical_r.md)**

:   KTAE 提出了一种不依赖额外模型的 token 级优势估计算法，通过 Fisher 精确检验和信息增益量化每个 token 与正确推理结果的统计关联，将细粒度 token 重要性叠加到 GRPO/DAPO 的 rollout 级优势上，在5个数学推理基准上超越基线并显著缩短生成长度。

**[Latent Principle Discovery for Language Model Self-Improvement](model_compression/latent_principle_discovery_for_language_model_self-improvement.md)**

:   STaPLe 提出后验正则化的蒙特卡洛 EM 算法，让 7-8B 小模型自行发现指导自我修正的"原则"（latent principle），通过迭代发现-学习循环实现自我改进，在 AlpacaEval 上提升 8-10% 胜率、MT-Bench 平均提升 +0.3，并可通过聚类压缩至可解释的 constitution。

**[LayerIF: Estimating Layer Quality for Large Language Models using Influence Functions](model_compression/layerif_estimating_layer_quality_for_large_language_models_using_influence_funct.md)**

:   LayerIF 提出用影响函数（Influence Functions）逐层量化 LLM 的训练质量，通过聚合各层的正向影响分数得到数据驱动的层重要性估计，并将其应用于 LoRA-MoE 专家分配和层级稀疏剪枝两个下游任务，在 Mistral-7B 和 Gemma-7B 上分别获得 1.61% 和 0.90% 的准确率提升。

**[Learning Grouped Lattice Vector Quantizers for Low-Bit LLM Compression](model_compression/learning_grouped_lattice_vector_quantizers_for_low-bit_llm_compression.md)**

:   GLVQ 提出为 LLM 权重的每个分组学习专属的格（lattice）码本（由可学习生成矩阵定义），配合分组特异的 μ-law companding 变换适应重尾分布，在 2-bit 量化下 Llama-2-70B 的 Wikitext-2 困惑度达到 3.36，大幅领先 QuIP#（3.91）和 QTIP（3.78）。

**[Learning Task-Agnostic Representations through Multi-Teacher Distillation](model_compression/learning_task-agnostic_representations_through_multi-teacher_distillation.md)**

:   提出基于互信息最大化的任务无关多教师蒸馏框架，通过高斯核估计教师嵌入的条件分布来训练学生模型，使其在不依赖任何下游任务标签的情况下学到高信息密度的通用表示，在文本、视觉和分子建模三个领域均取得了同体量最优性能。

**[Learning to Better Search with Language Models via Guided Reinforced Self-Training](model_compression/learning_to_better_search_with_language_models_via_guided_reinforced_self-traini.md)**

:   提出 Guided-ReST，通过将最优解作为子目标逐步融入模型自生成的搜索轨迹中，生成高质量训练数据并蒸馏更高效的搜索策略，在Countdown和代码自修复任务上显著提升搜索效率和准确率。

**[Learning to Factorize and Adapt: A Versatile Approach Toward Universal Spatio-Temporal Foundation Models](model_compression/learning_to_factorize_and_adapt_a_versatile_approach_toward_universal_spatio-tem.md)**

:   提出 FactoST-v2，一个因式分解的时空基础模型框架，将通用时间预训练与领域特定空间适配解耦，以线性复杂度实现跨领域零样本/少样本/全样本时空预测。

**[Linear Attention for Efficient Bidirectional Sequence Modeling](model_compression/linear_attention_for_efficient_bidirectional_sequence_modeling.md)**

:   提出 Lion 框架，首次系统地将线性 Transformer 扩展到双向序列建模，统一了全线性注意力、双向 RNN 和分块并行三种等价表示，在图像分类和 MLM 任务上训练速度比 SSM 快达 10 倍且性能可比 softmax Transformer。

**[LittleBit: Ultra Low-Bit Quantization via Latent Factorization](model_compression/littlebit_ultra_low-bit_quantization_via_latent_factorization.md)**

:   提出 LittleBit 框架，通过低秩潜空间矩阵分解 + 二值化 + 多尺度补偿机制，实现低至 0.1 BPW（每权重比特）的极端 LLM 压缩，将 Llama2-13B 压缩到不足 0.9GB，在子1比特领域大幅超越 STBLLM。

**[LT-Soups: Bridging Head and Tail Classes via Subsampled Model Soups](model_compression/lt-soups_bridging_head_and_tail_classes_via_subsampled_model_soups.md)**

:   提出 LT-Soups，一个两阶段模型融合框架，通过在不同不平衡比例的子采样数据上训练多个模型并进行权重平均，在长尾分布的全频谱上实现头部类和尾部类的均衡性能。

**[Matryoshka Pilot: Learning to Drive Black-Box LLMs with LLMs](model_compression/matryoshka_pilot_learning_to_drive_black-box_llms_with_llms.md)**

:   提出 Matryoshka Pilot (M-Pilot)，用轻量级白盒 LLM 作为控制器，通过生成中间引导（任务分解、高层计划、用户画像）来驱动黑盒 LLM 在推理、规划和个性化等复杂长程任务上的性能，并通过迭代 DPO 实现自我改进。

**[Memory-Efficient Training with In-Place FFT Implementation](model_compression/memory-efficient_training_with_in-place_fft_implementation.md)**

:   提出 rdFFT——首个真正原地（in-place）的实数域快速傅里叶变换框架，通过隐式复数编码方案消除中间缓冲区，实现训练时零额外内存开销的 FFT/IFFT 计算，内存效率最高提升 1500 倍以上。

**[ModHiFi: Identifying High Fidelity Predictive Components for Model Modification](model_compression/modhifi_identifying_high_fidelity_predictive_components_for_model_modification.md)**

:   提出 Subset Fidelity 度量和 ModHiFi 框架，通过理论证明 Lipschitz 连续网络的局部重构误差线性上界全局误差，无需训练数据、损失函数或梯度，仅用合成数据即可识别模型中的高保真 (HiFi) 组件，统一实现结构化剪枝和类别遗忘两大任务。

**[Multi-Task Vehicle Routing Solver via Mixture of Specialized Experts under State-Decomposable MDP](model_compression/multi-task_vehicle_routing_solver_via_mixture_of_specialized_experts_under_state.md)**

:   提出 **State-Decomposable MDP (SDMDP)** 框架将多种 VRP 变体重新表述为基础状态空间的笛卡尔积，再通过 **Mixture-of-Specialized-Experts Solver (MoSES)** 用专用 LoRA 专家实现基础策略的潜在空间复用，高效处理 16 种 VRP 变体。

**[Optimizing Distributional Geometry Alignment with Optimal Transport for Generative Dataset Distillation](model_compression/optimizing_distributional_geometry_alignment_with_optimal_transport_for_generati.md)**

:   将数据集蒸馏重新表述为最优传输（OT）距离最小化问题，通过三阶段（OT引导扩散采样、标签-图像对齐软重标注、OT logit匹配）实现细粒度分布几何对齐，在ImageNet-1K IPC=10上比之前SOTA提升至少4%。

**[Preserving LLM Capabilities through Calibration Data Curation: From Analysis to Optimization](model_compression/preserving_llm_capabilities_through_calibration_data_curation_from_analysis_to_o.md)**

:   系统研究了校准数据的组成特性（序列长度/样本量/来源/格式）和领域对应关系对LLM压缩后能力保持的影响，发现激活空间中的代表性和多样性是数据质量的本质决定因素，并据此提出三阶段校准数据策展框架COLA。

**[RCCDA: Adaptive Model Updates in the Presence of Concept Drift under a Constrained Resource Budget](model_compression/rccda_adaptive_model_updates_in_the_presence_of_concept_drift_under_a_constraine.md)**

:   提出 RCCDA，一种基于 Lyapunov 漂移惩罚框架的轻量级模型更新策略，在数据分布随时间漂移（concept drift）场景下，仅利用历史推理损失信息和可调阈值，就能贪心最优地决定何时重训模型，同时可证明地满足严格资源预算约束。

**[RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models](model_compression/reflora_refactored_low-rank_adaptation_for_efficient_fine-tuning_of_large_models.md)**

:   RefLoRA 通过在每次迭代中选择最优的低秩分解形式（最小化损失上界），解决了 LoRA 因分解不唯一性导致的权重更新不一致和不平衡问题，在几乎不增加计算开销的前提下加速收敛并提升微调性能。

**[Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA](model_compression/robust_federated_finetuning_of_llms_via_alternating_optimization_of_lora.md)**

:   提出 RoLoRA，通过交替优化 LoRA 的 down-projection (A) 和 up-projection (B) 矩阵，解决联邦学习中 LoRA 聚合不精确和表达力受限的问题，在 RoBERTa-Large 和 Llama-2-7B 上显著优于 FedAVG of LoRA 和 FFA-LoRA。

**[SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism](model_compression/shap_meets_tensor_networks_provably_tractable_explanations_with_parallelism.md)**

:   本文首次为张量网络（Tensor Networks）提供可证明精确的 SHAP 解释计算框架，证明张量列车（Tensor Train）结构下 SHAP 可在多对数时间内并行计算（NC² 复杂度），并通过归约揭示二值化神经网络中**宽度而非深度**才是 SHAP 计算的核心瓶颈。

**[Single-Teacher View Augmentation: Boosting Knowledge Distillation via Angular Diversity](model_compression/single-teacher_view_augmentation_boosting_knowledge_distillation_via_angular_div.md)**

:   提出Angular-KD，通过在单个教师模型上附加多个轻量线性分支并引入两种角度多样性损失（约束型视角间角度多样性损失和视角内角度多样性损失），从单教师生成多样化监督信号，以低成本替代多教师蒸馏方案，在多个KD基准上取得SOTA表现。

**[Spark Transformer: Reactivating Sparsity in FFN and Attention](model_compression/spark_transformer_reactivating_sparsity_in_ffn_and_attention.md)**

:   提出 Spark Transformer 架构，通过 Statistical Top-k 算子在 FFN 和注意力机制中同时实现高水平激活稀疏性（FFN 仅 8% 神经元激活、每个 token 最多关注 256 个 token），在保持与 Gemma-2 相当质量的同时实现 2.5× FLOPs 降低和高达 1.79× 的推理加速。

**[Specialization after Generalization: Towards Understanding Test-Time Training in Foundation Models](model_compression/specialization_after_generalization_towards_understanding_test-time_training_in_.md)**

:   提出"泛化之后特化"框架，基于线性表示假设（LRH）从理论和实验两方面解释了测试时训练（TTT）在分布内数据上的有效性：基础模型全局欠参数化导致概念叠加干扰，TTT通过局部特化将模型容量重新分配给与测试任务相关的少数概念，从而在不增加模型规模的情况下提升预测性能。

**[SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assemblies](model_compression/symphony_synergistic_multi-agent_planning_with_heterogeneous_language_model_asse.md)**

:   提出 SYMPHONY，一个基于 MCTS 的多智能体规划框架，通过异构 LLM 池的多样性驱动搜索、UCB 自适应调度、熵调制置信度评估和池级记忆共享，显著提升了 LLM 规划的多样性和效率。

**[The Graphon Limit Hypothesis: Understanding Neural Network Pruning via Infinite Width Analysis](model_compression/the_graphon_limit_hypothesis_understanding_neural_network_pruning_via_infinite_w.md)**

:   提出"Graphon极限假说"：当网络宽度趋于无穷时，不同剪枝方法产生的二值掩码序列在cut距离下收敛到各自独特的graphon极限，并在此基础上推导出Graphon NTK来分析稀疏网络训练动态，从理论层面解释了为什么不同剪枝方法在相同稀疏度下表现迥异。

**[Tighter CMI-Based Generalization Bounds via Stochastic Projection and Quantization](model_compression/tighter_cmi-based_generalization_bounds_via_stochastic_projection_and_quantizati.md)**

:   通过在 CMI（条件互信息）框架中引入**随机投影**和**有损压缩**，推导出更紧的泛化界，解决了经典 CMI 界在 SCO 反例上失效的问题，并证明记忆化对良好泛化并非必要。

**[Transformer Key-Value Memories Are Nearly as Interpretable as Sparse Autoencoders](model_compression/transformer_key-value_memories_are_nearly_as_interpretable_as_sparse_autoencoder.md)**

:   系统比较了Transformer前馈层（FF）的键值记忆特征与稀疏自编码器（SAE）学到的特征的可解释性，发现两者在现有评测指标上表现相当，FF-KV在某些方面甚至更优，质疑了SAE作为特征发现工具的必要性。

---

## 🎮 强化学习 { #reinforcement_learning }

**[A Generalized Bisimulation Metric of State Similarity between Markov Decision Processes: From Theoretical Propositions to Applications](reinforcement_learning/a_generalized_bisimulation_metric_of_state_similarity_betwee.md)**

:   将传统只能在单个MDP内度量状态相似性的bisimulation metric (BSM)推广到跨MDP场景，提出广义双模拟度量(GBSM)，严格证明了对称性、跨MDP三角不等式和同状态距离上界三个基本度量性质，并在策略迁移、状态聚合和基于采样的估计三个应用中推导出比标准BSM更紧的误差界和闭式样本复杂度。

**[A Near-optimal, Scalable and Parallelizable Framework for Stochastic Bandits Robust to Adversarial Corruptions and Beyond](reinforcement_learning/a_nearoptimal_scalable_and_parallelizable_framework_for_stoc.md)**

:   提出 BARBAT 框架，改进了经典的 BARBAR 算法，通过固定 epoch 长度和逐 epoch 调整失败概率，将对抗腐蚀下随机多臂老虎机的 regret 从 $O(\sqrt{K}C)$ 降至近最优的 $O(C)$（消除了 $\sqrt{K}$ 因子），并成功扩展到多智能体、图老虎机、组合半老虎机和批量老虎机等多种场景。

**[A Theory of Multi-Agent Generative Flow Networks](reinforcement_learning/a_theory_of_multi-agent_generative_flow_networks.md)**

:   提出多智能体生成流网络（MA-GFlowNets）的理论框架，证明了"局部-全局原理"——联合流函数可分解为各智能体独立流的乘积形式，设计了四种算法（CFN/IFN/JFN/CJFN），其中 JFN 和 CJFN 实现中心化训练+去中心化执行（CTDE），在 Hyper-Grid 和 StarCraft 环境中超越 RL 和 MCMC 方法。

**[A Unifying View of Linear Function Approximation in Off-Policy RL Through Matrix Splitting and Preconditioning](reinforcement_learning/a_unifying_view_of_linear_function_approximation_in_offpolic.md)**

:   将线性函数逼近下的TD、FQI和PFQI统一为求解同一线性系统的迭代方法（仅预条件子不同），首次引入矩阵分裂理论来分析它们的收敛性，给出了各算法收敛的充要条件，并揭示了TD收敛不一定意味着FQI收敛（反之亦然）。

**[Act to See, See to Act: Diffusion-Driven Perception-Action Interplay for Adaptive Policies](reinforcement_learning/act_to_see_see_to_act_diffusion-driven_perception-action_interplay_for_adaptive_.md)**

:   提出 DP-AG（Action-Guided Diffusion Policy），通过将扩散策略的噪声预测的 Vector-Jacobian Product (VJP) 作为结构化随机力驱动隐观测特征在扩散步骤间动态演化，并用循环一致对比损失闭合感知-动作环路，在 Push-T 上提升 6%、Dynamic Push-T 上提升 13%、真实 UR5 机器人上成功率提升 23%+。

**[Actor-Free Continuous Control via Structurally Maximizable Q-Functions](reinforcement_learning/actorfree_continuous_control_via_structurally_maximizable_qf.md)**

:   提出Q3C（Q-learning for Continuous Control with Control-points），一种无actor的纯基于值函数的连续控制方法，通过控制点插值逼近任意形状的Q函数，在复杂（非凸、受限）Q函数景观中显著优于actor-critic方法。

**[Adaptive Cooperative Transmission Design For Ultra-Reliable Low-Latency Communic](reinforcement_learning/adaptive_cooperative_transmission_design_for_ultra-reliable_low-latency_communic.md)**

:   提出 DRL-CoLA 算法，用双 Agent DQN 分别在源节点和中继节点上自适应配置 5G NR 传输参数（numerology、mini-slot、MCS），在两跳中继系统中仅用本地 CSI 即可达到接近全局 CSI 最优的 URLLC 可靠性。

**[Adaptive Neighborhood-Constrained Q Learning for Offline Reinforcement Learning](reinforcement_learning/adaptive_neighborhoodconstrained_q_learning_for_offline_rein.md)**

:   提出 ANQ（Adaptive Neighborhood-constrained Q learning），在离线 RL 中引入基于优势函数的自适应邻域约束，在密度约束（过于保守）和支持约束（需精确建模行为策略）之间找到灵活的中间方案，通过双层优化框架实现高效 Q 学习，在 D4RL 基准上达到 SOTA。

**[Adaptively Coordinating with Novel Partners via Learned Latent Strategies](reinforcement_learning/adaptively_coordinating_with_novel_partners_via_learned_latent_strategies.md)**

:   提出 TALENTS 框架，通过 VAE 学习潜在策略空间 + K-Means 聚类发现策略类型 + Fixed-Share 遗憾最小化算法在线推断队友类型，实现对未知人类/智能体队友的零样本实时适应协作。

**[ALINE: Joint Amortization for Bayesian Inference and Active Data Acquisition](reinforcement_learning/aline_joint_amortization_for_bayesian_inference_and_active_data_acquisition.md)**

:   ALINE 提出统一的分摊贝叶斯推断和主动数据获取框架，用 Transformer 架构 + RL 训练，使模型能同时策略性地选择最有信息量的数据点并即时完成后验推断，还支持灵活地针对特定参数子集或预测目标进行数据获取。

**[FastSVERL: Approximating Shapley Explanations in Reinforcement Learning](reinforcement_learning/approximating_shapley_explanations_in_reinforcement_learning.md)**

:   提出 FastSVERL——首个针对 RL 的可扩展 Shapley 值近似方法，用参数化模型分摊计算成本，解决 RL 特有的时序依赖、off-policy 数据和策略演化等挑战，为 RL 决策提供原则性的特征归因解释。

**[Automaton Constrained Q-Learning](reinforcement_learning/automaton_constrained_q-learning.md)**

:   ACQL 将安全 RL 和目标条件 RL 提升到 LTL（线性时序逻辑）任务类——用自动机编码时序目标进展和非平稳安全约束，结合目标条件值学习（+HER密集化奖励）和基于 Hamilton-Jacobi 可达性的安全约束，在连续控制任务上显著超越现有 LTL RL 方法，并在 6-DOF 机械臂上成功部署。

**[BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](reinforcement_learning/beast_efficient_tokenization_of_b-splines_encoded_action_sequences_for_imitation.md)**

:   BEAST 用 B 样条曲线参数化动作序列——通过岭回归估计控制点并均匀量化为固定长度 token，实现 20× token 压缩（100 步→5 token）、数学保证的动作块间 $C^0$ 连续过渡，在 LIBERO-Long 上成功率排名第 1（86.4%），推理吞吐量 617 Hz（比 π₀ 快 2.14×、比 OpenVLA 快 101×）。

**[Behavior Injection: Preparing Language Models for Reinforcement Learning](reinforcement_learning/behavior_injection_preparing_language_models_for_reinforcement_learning.md)**

:   揭示 LLM 对 RL 微调响应不一致的根本原因——通过 per-step influence 分析发现 RL 效果取决于（1）rollout 准确率分布（中等最优）和（2）数据 co-influence 强度，提出 BRIDGE 在 SFT 阶段注入探索/利用行为，使后续 RL 增益从 6% 提升到 46.6%。

**[Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](reinforcement_learning/beyond_the_8020_rule_highentropy_minority_tokens_drive_effec.md)**

:   从 token 熵模式的全新视角分析 RLVR，发现 CoT 推理中仅约 20% 的高熵"分叉 token"决定推理方向，仅在这些 token 上做梯度更新即可匹配甚至大幅超越全量更新（Qwen3-32B 上 AIME'25 +11.04），揭示 RLVR 本质是优化推理决策点。

**[Blending Complementary Memory Systems in Hybrid Quadratic-Linear Transformers](reinforcement_learning/blending_complementary_memory_systems_in_hybrid_quadratic-linear_transformers.md)**

:   提出混合二次-线性 Transformer（HQLT），将 KV-memory（softmax attention，精确检索但二次复杂度）与 FW-memory（DeltaNet/线性 attention，线性复杂度但检索粗糙）融合为互补记忆系统，比较三种混合策略（延迟流式/延迟分块/同步），在 340M 和 1.3B 参数规模的语言建模、检索、算法推理和 RL 任务上验证同步混合最优。

**[Bootstrap Off-policy with World Model (BOOM)](reinforcement_learning/bootstrap_off-policy_with_world_model.md)**

:   提出 BOOM 框架，通过 bootstrap 循环将在线规划器（MPPI）与 off-policy 策略学习紧密结合：策略初始化规划器，规划器反过来通过无似然对齐损失（likelihood-free alignment）引导策略改进，配合 soft Q-weighted 机制优先学习高回报行为，在高维连续控制任务上取得 SOTA。

**[Bootstrap Off-policy with World Model](reinforcement_learning/boundary-to-region_supervision_for_offline_safe_reinforcement_learning.md)**

:   提出 BOOM 框架，通过 bootstrap 对齐回路将在线规划器的高质量动作蒸馏到策略网络，使用 likelihood-free 的前向 KL 散度和软 Q 加权机制，有效缓解规划器与策略之间的 actor divergence 问题，在高维连续控制任务上取得 SOTA。

**[Certifying Stability of Reinforcement Learning Policies using Generalized Lyapunov Functions](reinforcement_learning/certifying_stability_of_reinforcement_learning_policies_using_generalized_lyapun.md)**

:   提出 Generalized Lyapunov Function 方法，通过将 RL 值函数与神经网络残差项结合，并用多步加权下降条件替代经典的逐步严格下降要求，实现对 RL 策略的稳定性认证。

**[Checklists Are Better Than Reward Models For Aligning Language Models](reinforcement_learning/checklists_are_better_than_reward_models_for_aligning_langua.md)**

:   提出 Reinforcement Learning from Checklist Feedback (RLCF)，将指令分解为动态生成的 yes/no checklist，结合 AI judge 和代码验证器逐项评分后做 DPO 训练，在 5 个 benchmark 上一致性提升 Qwen2.5-7B-Instruct，是唯一在所有 benchmark 上都有正收益的方法（FollowBench +4pt, InFoBench +6pt, Arena-Hard +3pt）。

**[Communicating Plans, Not Percepts: Scalable Multi-Agent Coordination with Embodied World Models](reinforcement_learning/communicating_plans_not_percepts_scalable_multi-agent_coordination_with_embodied.md)**

:   提出基于轻量世界模型的"意图通信"架构，通过生成并共享未来轨迹计划来实现多智能体协调，在可扩展性和性能上全面超越端到端涌现通信方案。

**[Comparing Uniform Price and Discriminatory Multi-Unit Auctions through Regret Minimization](reinforcement_learning/comparing_uniform_price_and_discriminatory_multi-unit_auctions_through_regret_mi.md)**

:   从在线学习和遗憾最小化框架出发，系统比较统一价格拍卖与歧视性拍卖的学习难度，证明两种格式在最坏情况下遗憾率相同，但特定结构条件下统一价格拍卖允许更快的学习速率。

**[Complexity Scaling Laws for Neural Models using Combinatorial Optimization](reinforcement_learning/complexity_scaling_laws_for_neural_models_using_combinatorial_optimization.md)**

:   以旅行商问题（TSP）为案例，研究固定模型容量下问题复杂度（解空间大小、表示空间维度）与模型性能之间的可预测缩放规律，揭示了 RL 和 SFT 在组合优化中的系统性性能趋势。

**[Computational Hardness of Reinforcement Learning with Partial $q^\pi$-Realizability](reinforcement_learning/computational_hardness_of_reinforcement_learning_with_partial_qπ-realizability.md)**

:   引入"部分 $q^\pi$-可实现性"概念，证明在此设定下使用贪心策略集时学习近优策略是 NP-hard 的，使用 softmax 策略集时在 rETH 假设下需要指数时间，弥合了 $q^*$-可实现性和 $q^\pi$-可实现性之间的理论空白。

**[Confounding Robust Deep Reinforcement Learning: A Causal Approach](reinforcement_learning/confounding_robust_deep_reinforcement_learning_a_causal_approach.md)**

:   基于部分辨识（partial identification）理论扩展 DQN，提出 Causal DQN 从含有未观测混淆因子的离线数据中学习鲁棒策略——通过优化最坏情况下的价值函数下界来获得安全策略，在 12 个混淆 Atari 游戏中一致性地超越标准 DQN。

**[Continual Knowledge Adaptation for Reinforcement Learning](reinforcement_learning/continual_knowledge_adaptation_for_reinforcement_learning.md)**

:   提出 CKA-RL，为每个任务维护知识向量（task-specific knowledge vector），通过 softmax 加权的动态知识适配和自适应知识合并机制，在三个持续 RL 基准上实现 4.20% 的整体性能提升和 8.02% 的前向迁移提升。

**[Convergence Theorems for Entropy-Regularized and Distributional Reinforcement Learning](reinforcement_learning/convergence_theorems_for_entropy-regularized_and_distributional_reinforcement_le.md)**

:   提出 **温度解耦策略（temperature decoupling gambit）**，证明在熵正则化强化学习中，通过解耦评估温度和行为温度，可以在温度趋于零时保证策略和回报分布收敛到一个可解释的、保持多样性的最优策略。

**[CORE: Constraint-Aware One-Step Reinforcement Learning for Simulation-Guided Neural Network Accelerator Design](reinforcement_learning/core_constraint-aware_one-step_reinforcement_learning_for_simulation-guided_neur.md)**

:   提出 CORE（Constraint-aware One-step REinforcement learning），一种无 critic 的单步 RL 框架，通过结构化分布采样、scaling-graph 解码器和约束感知的 reward shaping 来高效探索 DNN 加速器的硬件-映射联合设计空间，在 7 个 DNN 模型上取得至少 15× 的 latency 改善。

**[Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation](reinforcement_learning/decoderhybriddecoder_architecture_for_efficient_reasoning_wi.md)**

:   SambaY 提出 Gated Memory Unit（GMU）用于跨层共享 SSM 的 token 混合表示，将 YOCO 的 cross-decoder 中一半的 cross-attention 层替换为轻量级 GMU，在保持线性预填充复杂度和长上下文检索能力的同时，大幅提升解码效率——最终产品 Phi4-mini-Flash-Reasoning (3.8B) 在推理任务上超越 Phi4-mini-Reasoning，且在 2K 提示 + 32K 生成场景下实现高达 10× 的解码吞吐提升。

**[Deep RL Needs Deep Behavior Analysis: Exploring Implicit Planning by Model-Free Agents](reinforcement_learning/deep_rl_needs_deep_behavior_analysis_exploring_implicit_planning_by_model-free_a.md)**

:   提出 ForageWorld 自然觅食环境和神经科学启发的行为分析框架，揭示无模型 RNN-based DRL 智能体通过涌现动力学展现出结构化的类规划行为——无需显式记忆模块或世界模型。

**[DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning](reinforcement_learning/deepdiver_adaptive_search_intensity_scaling_via_open-web_reinforcement_learning.md)**

:   提出 DeepDiver，一个 RL 驱动的搜索推理框架，在真实开放网络环境中训练 LLM 的信息寻求能力，催生"搜索强度缩放"（SIS）涌现行为——7B 模型在知识密集任务上可媲美 671B 的 DeepSeek-R1。

**[DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning](reinforcement_learning/discover_automated_curricula_for_sparse-reward_reinforcement_learning.md)**

:   提出 DISCOVER，一种面向稀疏奖励长视野 RL 的目标选择策略，通过同时平衡可达性（achievability）、新颖性（novelty）和相关性（relevance）来生成指向目标任务的课程，理论上证明达到目标的步数与目标距离线性相关（而非搜索空间体积），在高维导航和操作任务中显著超越先前 SOTA 探索策略。

**[Dynamic Regret Reduces to Kernelized Static Regret](reinforcement_learning/dynamic_regret_reduces_to_kernelized_static_regret.md)**

:   将动态遗憾最小化问题重新建模为再生核希尔伯特空间(RKHS)中的静态遗憾问题，通过精心设计平移不变核实现最优路径长度依赖 $\widetilde{\mathcal{O}}(\sqrt{MP_TT})$，且天然不需要时间范围先验知识。

**[Dynamics-Aligned Latent Imagination in Contextual World Models for Zero-Shot Generalization](reinforcement_learning/dynamics-aligned_latent_imagination_in_contextual_world_models_for_zero-shot_gen.md)**

:   在 DreamerV3 架构中引入自监督上下文编码器 DALI，从交互历史中推断潜在环境参数（如重力、摩擦力），在 cMDP 基准上无需重训练即可实现零样本泛化，在外推任务上比 ground-truth context-aware 基线高出最多 96.4%。

**[EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](reinforcement_learning/egobridge_domain_adaptation_for_generalizable_imitation_from_egocentric_human_da.md)**

:   提出 EgoBridge 框架，利用最优传输(OT)在策略潜在空间中对齐人类和机器人数据的联合分布（特征+动作），结合动态时间规整(DTW)构建伪配对，实现从第一人称人类数据到机器人的跨具身知识迁移，在真实世界任务中绝对成功率提升达 44%。

**[Empirical Study on Robustness and Resilience in Cooperative Multi-Agent Reinforcement Learning](reinforcement_learning/empirical_study_on_robustness_and_resilience_in_cooperative_multi-agent_reinforc.md)**

:   通过 82,620 次大规模实验系统性研究合作多智能体 RL 中的鲁棒性和弹性，揭示超参数调优比算法选择更重要，并发现参数共享、GAE、PopArt 等常见做法在不确定性下反而有害，提出一套实用的超参数建议。

**[Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering](reinforcement_learning/enhancing_interpretability_in_deep_reinforcement_learning_through_semantic_clust.md)**

:   提出语义聚类模块(SCM)，将特征降维网络(FDR)与改进的 VQ-VAE 在线聚类相结合，无缝集成到 DRL 训练流程中，解决了 t-SNE 可视化不稳定的问题，揭示 DRL 内在具有基于语义的动态聚类特性。

**[Establishing Linear Surrogate Regret Bounds for Convex Smooth Losses via Convolutional Fenchel–Young Losses](reinforcement_learning/establishing_linear_surrogate_regret_bounds_for_convex_smooth_losses_via_convolu.md)**

:   通过构造基于卷积负熵（convolutional negentropy）的 Fenchel–Young 损失，首次证明凸且光滑的代理损失可以同时拥有线性代理遗憾界，打破了此前社区认为光滑性与线性遗憾率不可兼得的固有认知。

**[EvoLM: In Search of Lost Language Model Training Dynamics](reinforcement_learning/evolm_in_search_of_lost_language_model_training_dynamics.md)**

:   系统训练 100+ 个 1B/4B 参数的 LM（从零开始），透明地研究预训练→续训→SFT→RL 各阶段的训练动态，揭示过度训练的递减收益、灾难性遗忘的缓解策略、以及 SFT/RL 配置的复杂权衡。

**[Exploration via Feature Perturbation in Contextual Bandits](reinforcement_learning/exploration_via_feature_perturbation_in_contextual_bandits.md)**

:   提出特征扰动（Feature Perturbation）作为上下文 bandit 的新型随机探索策略：直接在特征输入上注入噪声，而非扰动参数或奖励，从而在广义线性 bandit 中实现 $\tilde{O}(d\sqrt{T})$ 最优遗憾界，首次消除了随机化算法相较确定性方法的 $\sqrt{d}$ 因子劣势。

**[Exploration with Foundation Models: Capabilities, Limitations, and Hybrid Approaches](reinforcement_learning/exploration_with_foundation_models_capabilities_limitations_and_hybrid_approache.md)**

:   系统评测 LLM/VLM 在经典 RL 探索任务（bandit、Gridworld、Atari）上的零样本能力，发现 VLM 存在"知行差距"（knowing-doing gap）——高层推理正确但低层控制失败，并提出简单的 VLM-RL 混合框架在理想条件下可显著加速学习。

**[Extending NGU to Multi-Agent RL: A Preliminary Study](reinforcement_learning/extending_ngu_to_multi-agent_rl_a_preliminary_study.md)**

:   将单智能体 NGU（Never Give Up）算法扩展至多智能体环境，通过共享回放缓冲区、共享新颖性信号和异构 β 参数三个设计维度的系统消融，发现 NGU + 共享经验池组合在 PettingZoo simple_tag 追捕任务中显著优于多智能体 DQN 基线。

**[FedRAIN-Lite: Federated Reinforcement Algorithms for Improving Idealised Numerical Weather and Climate Models](reinforcement_learning/fedrain-lite_federated_reinforcement_algorithms_for_improving_idealised_numerica.md)**

:   提出 FedRAIN-Lite 联邦强化学习框架，将 RL 智能体分配到不同纬度带学习局部气候参数化策略并定期全局聚合，在层次化理想能量平衡模型上验证 DDPG 在热带和中纬度区域可将面积加权 RMSE 降低 50% 以上，为 RL 扩展到全尺度 GCM 提供了可行路径。

**[Feel-Good Thompson Sampling for Contextual Bandits: a Markov Chain Monte Carlo Showdown](reinforcement_learning/feel-good_thompson_sampling_for_contextual_bandits_a_markov_chain_monte_carlo_sh.md)**

:   首次系统性实证评估 Feel-Good Thompson Sampling (FG-TS) 及其平滑变体 SFG-TS 在近似后验下的表现，横跨线性/逻辑/神经三类上下文赌博机设置和十四个基准，发现 FG-TS 在精确后验场景（线性/逻辑）下优于标准 TS，但在神经赌博机中反而退化，揭示了乐观偏差与采样噪声之间的关键权衡。

**[Finite-Sample Analysis of Policy Evaluation for Robust Average Reward Reinforcement Learning](reinforcement_learning/finite-sample_analysis_of_policy_evaluation_for_robust_average_reward_reinforcem.md)**

:   首次给出鲁棒平均奖励 MDP 策略评估的有限样本复杂度分析：通过构造精巧的半范数证明鲁棒 Bellman 算子具有收缩性质，结合截断 Multi-Level Monte Carlo 估计器实现有限期望样本复杂度，最终达到阶最优的 $\tilde{\mathcal{O}}(\epsilon^{-2})$ 样本复杂度。

**[Forecasting in Offline Reinforcement Learning for Non-stationary Environments](reinforcement_learning/forecasting_in_offline_reinforcement_learning_for_non-stationary_environments.md)**

:   提出 Forl 框架，将条件扩散模型生成的多模态候选状态与零样本时序基础模型的偏移预测通过维度最近匹配（DCM）融合，在测试时无需重训练即可应对观测函数随 episode 非平稳变化的离线 RL 部署场景，在 D4RL 标准基准上平均提升数十分。

**[Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds](reinforcement_learning/foundation_models_as_world_models_a_foundational_study_in_text-based_gridworlds.md)**

:   系统性评估了基础模型（LLM）作为零样本世界模型（FWM）和直接决策智能体（FA）在文本网格世界中的表现，揭示了两种策略在确定性/随机性环境中的互补优势。

**[Generalized Linear Bandits: Almost Optimal Regret with One-Pass Update](reinforcement_learning/generalized_linear_bandits_almost_optimal_regret_with_one-pass_update.md)**

:   提出GLB-OMD算法，首次在广义线性赌博机（GLB）问题中同时实现近似最优遗憾界 $\mathcal{O}(\log T\sqrt{T/\kappa_*})$ 和每轮 $\mathcal{O}(1)$ 的时间/空间复杂度，核心技术是基于混合损失（mix loss）为在线镜像下降（OMD）估计量构建紧致置信集。

**[Generalizing Verifiable Instruction Following](reinforcement_learning/generalizing_verifiable_instruction_following.md)**

:   引入IFBench基准评估精确指令遵循的泛化能力，证明当前SOTA模型严重过拟合于IFEval的25种约束模板，并提出IF-RLVR训练方法（基于GRPO + 可验证奖励）显著提升域内外指令遵循性能。

**[Global Convergence for Average Reward Constrained MDPs with Primal-Dual Actor-Critic](reinforcement_learning/global_convergence_for_average_reward_constrained_mdps_with_primal-dual_actor_cr.md)**

:   提出Primal-Dual Natural Actor-Critic（PDNAC）算法，首次在一般参数化策略下的平均奖励约束MDP中实现 $\tilde{\mathcal{O}}(1/\sqrt{T})$ 的全局收敛率和约束违反率，匹配理论下界。

**[Gradient-Variation Online Adaptivity for Accelerated Optimization with Hölder Smoothness](reinforcement_learning/gradient-variation_online_adaptivity_for_accelerated_optimization_with_hölder_sm.md)**

:   在 Hölder 光滑函数类上实现梯度变差自适应的在线学习算法，其 regret 在光滑和非光滑极端之间平滑插值；通过在线到批量转换，首次为强凸优化提供在光滑情形下加速、非光滑情形下近优的通用方法。

**[Greedy Algorithm for Structured Bandits: A Sharp Characterization of Asymptotic Success / Failure](reinforcement_learning/greedy_algorithm_for_structured_bandits_a_sharp_characterization_of_asymptotic_s.md)**

:   本文对结构化 bandit 问题中的贪心算法（Greedy）进行了完整的理论刻画，提出 self-identifiability 作为贪心算法能否获得 sublinear regret 的充要条件，并将结论推广到上下文 bandit 及一般交互决策框架 DMSO。

**[Horizon Reduction Makes RL Scalable](reinforcement_learning/horizon_reduction_makes_rl_scalable.md)**

:   本文通过大规模实验（最高 10 亿转移数据）揭示离线 RL 的可扩展性瓶颈源于决策时域过长（curse of horizon），并证明通过 n-step 回报和层次策略等时域缩减技术可显著提升扩展性，进而提出了简洁有效的 SHARSA 方法。

**[Human-Inspired Multi-Level Reinforcement Learning](reinforcement_learning/human-inspired_multi-level_reinforcement_learning.md)**

:   本文提出 RbRL-KL，在 rating-based RL 基础上增加 KL 散度驱动的策略损失项，利用不同评分等级的失败经验以不同权重推开当前策略，在 6 个 DeepMind Control 环境中超越标准 RbRL。

**[Hybrid Latent Reasoning via Reinforcement Learning](reinforcement_learning/hybrid_latent_reasoning_via_reinforcement_learning.md)**

:   HRPO 提出混合潜在推理策略优化：通过可学习的门控机制将前一步的隐藏状态表示逐步融入到采样的 token embedding 中，使 LLM 在推理阶段同时利用离散 token 和连续潜在表示，无需 CoT 标注即可通过 RL 训练，在知识密集型和 STEM 推理任务上均超越 PPO/GRPO 等基线。

**[Improved Regret and Contextual Linear Extension for Pandora's Box and Prophet Inequality](reinforcement_learning/improved_regret_and_contextual_linear_extension_for_pandoras_box_and_prophet_ine.md)**

:   本文针对在线 Pandora's Box 问题提出新算法，将 regret 从 $\widetilde{O}(n\sqrt{T})$ 改进到 $\widetilde{O}(\sqrt{nT})$（匹配下界），并首次提出 contextual linear 扩展实现 $\widetilde{O}(nd\sqrt{T})$ regret。

**[Improved Regret Bounds for GP-UCB in Bayesian Optimization](reinforcement_learning/improved_regret_bounds_for_gaussian_process_upper_confidence_bound_in_bayesian_o.md)**

:   本文证明 GP-UCB 在贝叶斯设定下可达 $\widetilde{O}(\sqrt{T})$ 高概率 regret（Matern 核满足光滑条件时）和 $O(\sqrt{T \ln^2 T})$（SE 核），弥合了 GP-UCB 已有上界与最优上界间的差距。

**[Improving Planning and MBRL with Temporally-Extended Actions](reinforcement_learning/improving_planning_and_mbrl_with_temporally-extended_actions.md)**

:   本文提出在 shooting-based 规划和 MBRL 中将动作持续时间作为额外优化变量，配合 MAB 自动选择持续时间范围，在多个环境中显著加速规划并解决标准方法无法解决的困难任务。

**[Improving Retrieval-Augmented Generation through Multi-Agent Reinforcement Learning](reinforcement_learning/improving_retrieval-augmented_generation_through_multi-agent_reinforcement_learn.md)**

:   将复杂 RAG 流水线中的多个组件（Query Rewriter、Selector、Generator）建模为协作多智能体系统，使用 MAPPO 算法进行联合优化，以最终答案的 F1 分数作为共享奖励，在多个 QA 基准上超越现有单模块优化方法。

**[Incremental Sequence Classification with Temporal Consistency](reinforcement_learning/incremental_sequence_classification_with_temporal_consistency.md)**

:   将强化学习中时序差分（TD）学习的思想引入序列分类任务，提出 TC-$\lambda$ 损失函数，通过要求相邻时间步的预测分布满足时序一致性条件来训练增量式序列分类器，在文本分类和 LLM 验证任务上均优于标准交叉熵方法。

**[Inner Speech as Behavior Guides: Steerable Imitation of Diverse Behaviors for Human-AI Coordination](reinforcement_learning/inner_speech_as_behavior_guides_steerable_imitation_of_diverse_behaviors_for_hum.md)**

:   受维果茨基内心语言理论启发，提出 MIMIC 框架，利用语言作为感知与动作之间的中介表征，通过 VLM 提供语言脚手架训练 CVAE 生成内心语言，再以扩散策略在条件化于内心语言的情况下生成多样且可控的行为。

**[Interactive and Hybrid Imitation Learning: Provably Beating Behavior Cloning](reinforcement_learning/interactive_and_hybrid_imitation_learning_provably_beating_behavior_cloning.md)**

:   当标注成本按**状态**而非轨迹计量时，证明交互式方法 Stagger 在 $\mu$-可恢复条件下可证明地超越 Behavior Cloning（次优性 $O(\mu H \log B / N)$ vs $O(RH \log B / CN)$，$\mu \ll R$ 时优势显著）；进一步提出混合 IL 算法 Warm-Stagger，结合离线数据和交互标注，在特定 MDP 上实现两种数据源的严格互补优势。

**[Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems](reinforcement_learning/inverse_optimization_latent_variable_models_for_learning_costs_applied_to_route_.md)**

:   提出 IO-LVM（Inverse Optimization Latent Variable Model），用 VAE 式编码器映射观测的 COP 解到潜在成本空间，通过 Fenchel-Young 损失和黑盒求解器（Dijkstra/TSP solver）在解码端保证可行性，无需 agent 标签即可从路径数据中学到成本函数的分布，成功不可监督地分离不同 agent 的导航偏好。

**[Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification](reinforcement_learning/kimina_lean_server_a_high-performance_lean_server_for_large-scale_verification.md)**

:   提出Kimina Lean Server——一个面向大规模强化学习训练的高性能Lean 4验证服务器，通过服务端并行化和LRU缓存机制实现1.5-2倍的速度提升，已用于训练SOTA定理证明模型Kimina-Prover。

**[Knowledge-based Visual Question Answer with Multimodal Processing, Retrieval and Filtering](reinforcement_learning/knowledge-based_visual_question_answer_with_multimodal_processing_retrieval_and_.md)**

:   提出 Wiki-PRF，一套三阶段（处理-检索-过滤）的多模态 RAG 框架，通过强化学习训练 VLM 自主调用视觉工具和过滤检索结果，在 E-VQA 和 InfoSeek 上达到 SOTA。

**[Last Iterate Convergence In Monotone Mean Field Games](reinforcement_learning/last_iterate_convergence_in_monotone_mean_field_games.md)**

:   在非严格单调平均场博弈(MFG)中，提出基于 KL 散度的近端点(PP)方法实现渐近最后迭代收敛(LIC)，并证明正则化镜像下降(RMD)以指数速率收敛到正则化均衡，两者结合的 APP 算法在标准基准上可靠收敛到非正则化均衡。

**[Learning from Demonstrations via Capability-Aware Goal Sampling](reinforcement_learning/learning_from_demonstrations_via_capability-aware_goal_sampling.md)**

:   提出Cago方法，通过动态追踪智能体在专家演示轨迹上的达成能力，自适应采样处于能力边界的中间目标，构建隐式课程引导长视野稀疏奖励任务学习。

**[Learning in Stackelberg Mean Field Games: A Non-Asymptotic Analysis](reinforcement_learning/learning_in_stackelberg_mean_field_games_a_non-asymptotic_analysis.md)**

:   提出首个具有非渐近收敛保证的单循环Actor-Critic算法AC-SMFG，用于求解Stackelberg平均场博弈（SMFG），收敛速率达到 $\widetilde{\mathcal{O}}(k^{-1/2})$。

**[Learning Interestingness in Automated Mathematical Theory Formation](reinforcement_learning/learning_interestingness_in_automated_mathematical_theory_formation.md)**

:   提出 Fermat——一个将数学理论形成建模为 MDP 的强化学习环境，以及 EvoAbstract——一个带抽象学习的 LLM 驱动进化算法，用于自动合成数学对象的"兴趣度"度量函数，在初等数论和有限域上显著超越硬编码基线。

**[Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling](reinforcement_learning/learning_memory-enhanced_improvement_heuristics_for_flexible_job_shop_scheduling.md)**

:   提出 MIStar——首个基于深度强化学习 (DRL) 的改进型启发式框架，用于求解柔性作业车间调度问题 (FJSP)。核心创新包括有向异构析取图表示、记忆增强异构图神经网络 (MHGNN) 和并行贪心搜索策略，在合成数据和公开 benchmark 上全面超越手工改进启发式和 SOTA 构造型 DRL 方法。

**[Massively Parallel Imitation Learning of Mouse Forelimb Musculoskeletal Reaching Dynamics](reinforcement_learning/massively_parallel_imitation_learning_of_mouse_forelimb_musculoskeletal_reaching.md)**

:   基于 MIMIC-MJX 平台构建小鼠前肢肌肉骨骼模拟学习流水线，通过 JAX 加速的大规模并行 PPO（120 万步/秒）训练物理感知模仿学习策略，证明控制成本正则化能使模拟肌肉活动更好地预测真实 EMG 信号，并用基于 Takens 定理的非线性动力学方法从关节运动学预测肌肉激活。

**[Mean-Field Sampling for Cooperative Multi-Agent Reinforcement Learning](reinforcement_learning/mean-field_sampling_for_cooperative_multi-agent_reinforcement_learning.md)**

:   提出 SUBSAMPLE-MFQ 算法，通过从 $n$ 个智能体中随机采样 $k$ 个进行均场 Q 学习，将多智能体强化学习的样本复杂度从 $\text{poly}(n)$ 降低到 $\text{poly}(k)$，且性能差距仅为 $\tilde{O}(1/\sqrt{k})$（与 $n$ 无关），当 $k = O(\log n)$ 时实现相对均场 MARL 的指数加速。

**[Multi-Agent Collaboration via Evolving Orchestration](reinforcement_learning/multi-agent_collaboration_via_evolving_orchestration.md)**

:   提出"木偶师"(Puppeteer)式多 Agent 协作范式——一个中心化编排器通过 RL 学习在每个推理步骤动态选择激活哪个 Agent，在封闭域和开放域任务上同时提升性能和效率，并发现演化后的拓扑趋向更紧凑的环形结构。

**[Multi-Objective Reinforcement Learning with Max-Min Criterion: A Game-Theoretic Approach](reinforcement_learning/multi-objective_reinforcement_learning_with_max-min_criterion_a_game-theoretic_a.md)**

:   将max-min多目标强化学习重新表述为两人零和正则化连续博弈，提出ERAM/ARAM算法，利用镜像下降实现简洁的闭式权重更新，保证全局最后迭代收敛，在交通信号控制等任务中显著优于已有方法。

**[NoisyRollout: Reinforcing Visual Reasoning with Data Augmentation](reinforcement_learning/noisyrollout_reinforcing_visual_reasoning_with_data_augmenta.md)**

:   提出NoisyRollout，一种简单有效的数据增强方法——在VLM的RL训练中混合使用干净图像和适度扭曲图像的生成轨迹，通过注入感知多样性促进策略探索和鲁棒推理，配合噪声退火调度，零额外计算成本实现5个域外推理benchmark上的开源RL模型SOTA。

**[Non-convex Entropic Mean-Field Optimization via Best Response Flow](reinforcement_learning/non-convex_entropic_mean-field_optimization_via_best_response_flow.md)**

:   将Best Response Flow从凸函数泛函优化扩展到非凸情形，证明在充分大的熵正则化下，BR算子在 $L^1$-Wasserstein距离下成为压缩映射，保证非凸目标的唯一全局最小值存在性及指数收敛。

**[Optimizing the Unknown: Black Box Bayesian Optimization with Energy-Based Model and Reinforcement Learning](reinforcement_learning/optimizing_the_unknown_black_box_bayesian_optimization_with_energy-based_model_a.md)**

:   提出REBMBO框架，将高斯过程（局部建模）、能量模型EBM（全局探索）和PPO强化学习（多步前瞻）统一为贝叶斯优化闭环，在高维/多峰黑盒优化中显著优于传统BO方法。

**[Parameter Efficient Fine-tuning via Explained Variance Adaptation](reinforcement_learning/parameter_efficient_fine-tuning_via_explained_variance_adaptation.md)**

:   提出 Explained Variance Adaptation (EVA)，通过对激活向量进行增量 SVD 来初始化 LoRA 矩阵，可证明地最大化期望梯度信号，并结合自适应秩分配机制在语言生成/理解、图像分类、强化学习等多领域建立了精度-效率的新 Pareto 前沿。

**[Qimeng-Salv Signal-Aware Learning For Verilog Code Generation](reinforcement_learning/qimeng-salv_signal-aware_learning_for_verilog_code_generation.md)**

:   从部分正确的Verilog模块中提取信号级正确实现用于信号感知DPO训练，使7B模型在RTLLM v1.1上达到671B DeepSeek-v3的水平（62.6% pass@1）。

**[Reasoning Gym: Reasoning Environments for Reinforcement Learning with Verifiable Rewards](reinforcement_learning/reasoning_gym_reasoning_environments_for_reinforcement_learning_with_verifiable_.md)**

:   发布Reasoning Gym库，包含100+可验证推理任务的过程生成环境，支持动态难度调整和无限数据生成，可用于RLVR训练和推理评估。

**[Reinforcement Learning for Long-Horizon Multi-Turn Search Agents](reinforcement_learning/reinforcement_learning_for_long-horizon_multi-turn_search_agents.md)**

:   展示 RL 训练的 14B 参数搜索 agent 在法律文档检索任务上通过多轮交互可以超越 frontier 模型（85% vs GPT o3 的 81%），关键在于精心设计的分段奖励结构和允许长 horizon 多轮交互。

**[Retrosynthesis Planning Via Worst-Path Policy Optimisation In Tree-Structured Md](reinforcement_learning/retrosynthesis_planning_via_worst-path_policy_optimisation_in_tree-structured_md.md)**

:   将逆合成规划重新建模为树结构MDP中的最差路径优化问题，用自模仿学习确保所有合成路线都能终止于可购买的起始材料。

**[RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning](reinforcement_learning/rl_tango_reinforcing_generator_and_verifier_together_for_lan.md)**

:   Tango 提出一种交替 RL 训练生成器和验证器的框架——验证器是生成式过程级 LLM（用自然语言逐步评判），仅用结果级正确性奖励训练（无需步骤标注），通过与生成器的共进化相互增强——在 7B/8B 级别模型上达到SOTA，AIME 2025 准确率相对 vanilla GRPO 提升 100%。

**[Sample-Efficient Tabular Self-Play for Offline Robust Reinforcement Learning](reinforcement_learning/sample-efficient_tabular_self-play_for_offline_robust_reinforcement_learning.md)**

:   提出 RTZ-VI-LCB 算法用于离线鲁棒两人零和 Markov 博弈（RTZM G），通过乐观鲁棒值迭代 + Bernstein 风格惩罚，实现近最优样本复杂度 $O(C_r^* \cdot H^4 \cdot S \cdot (A+B) / \varepsilon^2)$，较此前最优结果 $O(H^5 \cdot S^2 \cdot AB / \varepsilon^2)$ 在状态空间和动作空间依赖上均有显著改善。

**[Ensemble++: Scalable Exploration via Ensemble](reinforcement_learning/scalable_exploration_via_ensemble.md)**

:   提出 Ensemble++，通过共享因子矩阵的增量更新机制，仅需 $\Theta(d\log T)$ 的集成大小即可实现与精确 Thompson Sampling 相当的遗憾界，并自然扩展到非线性/神经网络场景。

**[Solving Neural Min-Max Games: The Role of Architecture, Initialization & Dynamics](reinforcement_learning/solving_neural_min-max_games_the_role_of_architecture_initialization_dynamics.md)**

:   首次为两层神经网络参数化的零和博弈提供收敛保证，证明在适当过参数化、随机初始化和交替梯度下降上升（AltGDA）下，能以高概率收敛到 $\epsilon$-近似纳什均衡。

**[Structured Reinforcement Learning for Combinatorial Decision-Making](reinforcement_learning/structured_reinforcement_learning_for_combinatorial_decision-making.md)**

:   提出 Structured Reinforcement Learning (SRL)，将组合优化求解器作为可微层嵌入 actor-critic 的 actor 中，通过 Fenchel-Young 损失 + 高斯扰动实现端到端梯度传播，纯在线学习、无需专家数据，在6个工业级组合决策问题上匹配模仿学习、超越无结构 RL 最高 92%。

**[SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](reinforcement_learning/swe-rl_advancing_llm_reasoning_via_reinforcement_learning_on_open_software_evolu.md)**

:   首次将强化学习 (RL) 应用于真实世界软件工程任务（GitHub PR/Issue 修复），仅用基于规则的序列相似度奖励训练 Llama-3.3-70B，在 SWE-bench Verified 上达到 41.0% 解决率（中等规模模型 SOTA），且 RL 训练仅在 issue-solving 数据上进行，却涌现出在代码推理、数学、通用语言理解等域外任务上的泛化推理能力。

**[Temporal-Difference Variational Continual Learning](reinforcement_learning/temporal-difference_variational_continual_learning.md)**

:   提出TD-VCL目标函数，将变分持续学习（VCL）中的学习目标重新表示为多个过去后验估计的加权组合，揭示了与强化学习中时序差分（TD）方法的深层联系，通过"分散"正则化压力有效缓解了近似误差的逐步累积问题。

**[The Burden of Interactive Alignment with Inconsistent Preferences](reinforcement_learning/the_burden_of_interactive_alignment_with_inconsistent_preferences.md)**

:   将用户与参与度驱动算法的交互建模为多领导者-单跟随者 Stackelberg 博弈，证明存在关键的前瞻视野阈值：超过该阈值的用户可实现对齐，否则反被算法对齐；同时证明引入低成本信号（如额外点击）可大幅降低对齐负担。

**[Tractable Multinomial Logit Contextual Bandits with Non-Linear Utilities](reinforcement_learning/tractable_multinomial_logit_contextual_bandits_with_non-linear_utilities.md)**

:   首次为MNL上下文赌博机问题在非线性效用函数（含神经网络）下设计了**计算可行**且**统计最优**的算法ONL-MNL，在不依赖NTK假设的情况下达到$\widetilde{\mathcal{O}}(\sqrt{T})$的遗憾上界。

**[Training Language Models to Reason Efficiently](reinforcement_learning/training_language_models_to_reason_efficiently.md)**

:   通过在 RL 奖励中加入长度惩罚项——正确回答的奖励乘以 $(1 - \alpha \cdot \sigma(\text{norm\_len}))$，用单一超参数 $\alpha$ 控制 token-准确率权衡曲线，仅 100 步 RL 训练即可让 7B 推理模型减少 50% token 使用量而准确率仅下降 <5%。

**[Zero-Shot Context Generalization in Reinforcement Learning from Few Training Contexts](reinforcement_learning/zero-shot_context_generalization_in_reinforcement_learning_from_few_training_con.md)**

:   提出 Context-Enhanced Bellman Equation (CEBE) 和 Context Sample Enhancement (CSE) 方法，通过利用环境动力学和奖励函数对上下文参数的一阶导数信息，在仅训练于单一上下文的情况下实现对未见上下文的零样本泛化。

**[Zeroth-Order Optimization Finds Flat Minima](reinforcement_learning/zeroth-order_optimization_finds_flat_minima.md)**

:   首次从理论上证明标准零阶优化（两点梯度估计）具有隐式正则化效果——收敛到Hessian迹最小的平坦极小值（flat minima），在凸且充分光滑条件下给出了$T = \mathcal{O}(d^4/\epsilon^2)$的收敛复杂度保证。

---

## 💡 LLM 推理 { #llm_reasoning }

**[AbbIE: Autoregressive Block-Based Iterative Encoder for Efficient Sequence Modeling](llm_reasoning/abbie_autoregressive_block-based_iterative_encoder_for_efficient_sequence_modeli.md)**

:   提出 AbbIE，一种将 decoder-only Transformer 的中间层（Body）进行递归迭代的架构，只需训练时用 2 次迭代，推理时即可通过增加迭代次数实现 upward generalization，在语言建模困惑度和 zero-shot ICL 任务上均超过标准 Transformer，且可作为标准 Transformer 的 drop-in 替代。

**[Adaptive Dual Reasoner: Large Reasoning Models Can Think Efficiently by Hybrid Reasoning](llm_reasoning/adaptive_dual_reasoner_large_reasoning_models_can_think_efficiently_by_hybrid_re.md)**

:   提出 Adaptive Dual Reasoner (ADR)——让推理模型在 fast thinking（简单推理步骤压缩）和 slow thinking（复杂推理步骤保留深度）之间动态切换，通过 SFT 冷启动 + EHPO（熵引导混合策略优化）训练，在数学推理基准上准确率提升最高 6.1% 同时推理 token 减少 49.5%-59.3%。

**[Are Large Reasoning Models Good Translation Evaluators? Analysis and Performance Boost](llm_reasoning/are_large_reasoning_models_good_translation_evaluators_analysis_and_performance_.md)**

:   首次系统分析了大推理模型（LRM）在机器翻译MQM评估中的行为，发现LRM存在"过度思考"、评分高估和材料选择依赖模型规模等问题，并提出ThinMQM方法通过训练合成人类评分轨迹来校准LRM思维过程，将思维预算减少约35倍同时提升评估性能（7B模型提升+8.7相关性分数）。

**[ARM: Adaptive Reasoning Model](llm_reasoning/arm_adaptive_reasoning_model.md)**

:   ARM 通过让模型自适应地选择四种推理格式（直接回答、短CoT、代码、长CoT），配合改进的 Ada-GRPO 训练算法解决 format collapse 问题，在保持与纯长CoT模型持平的准确率的同时平均节省 ~30% token，最多节省 ~70%。

**[Atom of Thoughts for Markov LLM Test-Time Scaling](llm_reasoning/atom_of_thoughts_for_markov_llm_testtime_scaling.md)**

:   提出 Atom of Thoughts (AoT)，将 LLM 推理建模为马尔可夫链，每个状态是与原问题答案等价但复杂度递减的自包含子问题，通过 DAG 分解+收缩的两阶段转移机制消除历史依赖，可与 ToT/反思等方法无缝集成，在数学/代码/多跳QA等6个benchmark上全面领先现有推理框架。

**[Auditing Meta-Cognitive Hallucinations in Reasoning Large Language Models](llm_reasoning/auditing_meta-cognitive_hallucinations_in_reasoning_large_language_models.md)**

:   系统性审计推理大模型（RLLM）中幻觉的产生与传播机制，发现长 CoT 中的反思（reflection）会通过元认知偏差放大幻觉而非纠正它，即使在幻觉源头进行干预也难以改变最终结果（chain disloyalty），揭示现有幻觉检测方法在多步推理场景下严重不足。

**[Base Models Know How to Reason, Thinking Models Learn When](llm_reasoning/base_models_know_how_to_reason_thinking_models_learn_when.md)**

:   通过无监督 SAE 聚类发现 thinking model 的推理机制分类，然后用 steering vector 在基座模型上激活这些潜在推理能力，混合模型恢复高达 91% 的 thinking-base 性能差距（无需权重更新），证明基座模型已具备推理能力，thinking model 只是学会了"何时"部署它们。

**[Beyond Chemical QA: Evaluating LLM's Chemical Reasoning with Modular Chemical Operations](llm_reasoning/beyond_chemical_qa_evaluating_llms_chemical_reasoning_with_modular_chemical_oper.md)**

:   提出 ChemCoTBench，首个评估 LLM 化学推理能力的 CoT 基准，将复杂化学问题分解为模块化的化学操作（加/删/替换官能团），配合 22,000 条专家标注的 CoT 数据集（ChemCoTDataset），系统性评估了推理型和非推理型 LLM 在分子理解/编辑/优化/反应预测上的能力。

**[Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers](llm_reasoning/causal_head_gating_a_framework_for_interpreting_roles_of_attention_heads_in_tran.md)**

:   提出 Causal Head Gating (CHG)，通过对 Transformer 的每个 attention head 学习一个可微门控系数并结合正/负正则化，将 head 分为促进（facilitating）、干扰（interfering）、无关（irrelevant）三类，无需人工标签或 prompt 模板即可发现因果子电路，并扩展为对比 CHG 以分离 ICL 和指令遵循的独立电路。

**[Clip-and-Verify: Linear Constraint-Driven Domain Clipping for Accelerating Neural Network Verification](llm_reasoning/clip-and-verify_linear_constraint-driven_domain_clipping_for_accelerating_neural.md)**

:   提出Clip-and-Verify框架，通过利用线性界传播产生的约束来裁剪输入空间和收紧中间层界，包含完全裁剪（坐标上升求解对偶问题）和松弛裁剪（收缩输入盒）两种GPU高效算法，最多减少96%的BaB子问题数量，是VNN-COMP 2025获胜验证器的核心组件。

**[Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning](llm_reasoning/co-evolving_llm_coder_and_unit_tester_via_reinforcement_learning.md)**

:   提出CURE框架，通过单元测试生成器与代码生成器的相互监督和共同进化，在无需ground-truth代码的情况下显著提升LLM代码生成能力。

**[Cognitive Mirrors: Exploring the Diverse Functional Roles of Attention Heads in LLM Reasoning](llm_reasoning/cognitive_mirrors_exploring_the_diverse_functional_roles_of_attention_heads_in_l.md)**

:   提出CogQA基准数据集和多类probing框架，系统分析LLM中注意力头的认知功能特化现象，发现认知头具有稀疏性、普遍性和层级化功能组织特征，去除认知头显著降低推理性能，增强则提升准确率。

**[Controlling Thinking Speed in Reasoning Models](llm_reasoning/controlling_thinking_speed_in_reasoning_models.md)**

:   通过表示工程（Representation Engineering）从 LRM 的隐藏空间中提取控制快/慢思考转换的 steering vector，结合基于层间 logit 散度的实时推理难度估计，实现无需训练的自适应推理速度调节，在 4 个 LRM 上平均提升 +1.3% 准确率并减少 -8.6% token 使用。

**[Cooperative Retrieval-Augmented Generation for Question Answering: Mutual Information Exchange and Ranking by Contrasting Layers](llm_reasoning/cooperative_retrieval-augmented_generation_for_question_answering_mutual_informa.md)**

:   提出CoopRAG框架，通过问题展开、基于检索器层对比的重排、以及推理链补全，实现检索器与LLM的双向合作，在多跳QA上超越HippoRAG2 5.3%，单跳QA上提升35.2%。

**[CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring](llm_reasoning/cot_redhanded_stress_testing_chainofthought_monitoring.md)**

:   在 AI Control 框架下系统评估了 Chain-of-Thought 监控的有效性：发现 CoT 监控在检测微妙破坏行为上比仅监控 action 更有效（+10pp），但在检测明显破坏行为时反而更差（-25pp，因为推理中的伪合理化会欺骗监控），提出 hybrid 监控协议（独立评分 CoT 和 action 后加权）在所有场景下一致优于两种单一监控，检测率提升 2 倍。

**[Curriculum Abductive Learning](llm_reasoning/curriculum_abductive_learning.md)**

:   提出 Curriculum Abductive Learning (C-ABL)，通过将知识库按依赖结构分割为子知识库并渐进式引入训练，大幅缩小 ABL 的 abduction 搜索空间，显著提升训练稳定性、收敛速度和最终精度。

**[Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences](llm_reasoning/deep_value_benchmark_measuring_whether_models_generalize_deep_values_or_shallow_.md)**

:   提出 Deep Value Benchmark (DVB)，通过"先混淆后解混淆"的实验设计，测量 LLM 是学习了深层人类价值观还是仅记住了表层偏好模式，发现所有模型的深层价值泛化率 (DVGR) 仅为 0.30，远低于随机水平。

**[DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization](llm_reasoning/disco_reinforcing_large_reasoning_models_with_discriminative_constrained_optimiz.md)**

:   分析 GRPO 目标函数，揭示其固有的难度偏差（对过难/过易问题赋予过低权重）和熵不稳定性问题，提出基于判别学习的 DisCO 框架，通过无裁剪评分函数、平方铰链约束优化和 DRO 处理不平衡 rollout，在 1.5B 模型上平均超过 GRPO 7%、超过 DAPO 6%。

**[Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](llm_reasoning/does_thinking_more_always_help_mirage_of_test-time_scaling_in_reasoning_models.md)**

:   通过系统实验揭示 LRM 测试时扩展（反复 "Wait" 提示延长推理）的性能呈先升后降的非单调趋势，用概率模型证明这种"提升"只是方差增大导致的海市蜃楼而非真正推理能力提升，并提出 parallel thinking 策略在相同 token 预算下准确率提升最高 22%。

**[DreamPRM: Domain-Reweighted Process Reward Model for Multimodal Reasoning](llm_reasoning/dreamprm_domain-reweighted_process_reward_model_for_multimodal_reasoning.md)**

:   提出 DreamPRM，通过双层优化自动学习多模态推理数据集的域权重，解决 PRM 训练中的数据质量不均衡问题，在 MathVista 排行榜上以 o4-mini 模型达到 85.2% 的 top-1 准确率。

**[GPO: Learning from Critical Steps to Improve LLM Reasoning](llm_reasoning/gpo_learning_from_critical_steps_to_improve_llm_reasoning.md)**

:   GPO 通过蒙特卡洛模拟估计推理轨迹中每一步的优势函数，识别出"关键步骤"（模型犯错的转折点），然后从关键步骤重置并重新采样轨迹用于训练，可以即插即用地提升 PPO、DPO、KTO、SimPO、ORPO 等多种优化算法在推理任务上的表现。

**[I-RAVEN-X: Benchmarking Generalization and Robustness of Analogical and Mathematical Reasoning in Large Language and Reasoning Models](llm_reasoning/i-raven-x_benchmarking_generalization_and_robustness_of_analogical_and_mathemati.md)**

:   提出 I-RAVEN-X，一个增强版的符号化推理基准，通过增加操作数复杂度、属性范围和感知不确定性来评估 LLM 和 LRM 的类比推理与数学推理的泛化能力和鲁棒性，发现 LRM 在确定性推理上显著优于 LLM，但在不确定性推理下性能急剧下降。

**[Inference-Time Chain-of-Thought Pruning with Latent Informativeness Signals](llm_reasoning/inference-time_chain-of-thought_pruning_with_latent_informativeness_signals.md)**

:   提出 KAPPA (KL-Adjusted Pruned Path Algorithm)，利用 KL 散度、置信度和熵三个无需额外训练的信号对 Best-of-N 采样的推理分支进行渐进式剪枝，在保持准确率的同时实现最高 60% 峰值内存和 90% token 生成量的削减。

**[笔记1: CoT是幻觉吗？数据分布角度](llm_reasoning/is_chain-of-thought_reasoning_of_llms_a_mirage_a_data_distribution_lens.md)**

:   通过构建完全可控的抽象环境DataAlchemy，本文揭示CoT推理是一种幻觉——其有效性完全由训练数据分布主导，在分布外场景表现极其脆弱。

**[Know What You Don't Know: Uncertainty Calibration of Process Reward Models](llm_reasoning/know_what_you_dont_know_uncertainty_calibration_of_process_reward_models.md)**

:   本文提出了一种基于分位数回归的PRM校准方法，使PRM输出的分数更准确地反映LLM实际推理成功概率，并基于校准后的PRM设计了实例自适应推理时缩放（IAS）策略，在保持准确率的同时显著降低推理成本。

**[Large Language Models Can Learn and Generalize Steganographic Chain-of-Thought under Process Supervision](llm_reasoning/large_language_models_can_learn_and_generalize_steganographic_chain-of-thought_u.md)**

:   证明 LLM 在 RL 训练中受到 CoT 过程监督（惩罚特定字符串出现）时，会自发学会隐写术（steganography）——用替代编码隐藏被禁止的推理步骤，且这种编码是因果性的（load-bearing）并能泛化到训练中从未见过的字符串。

**[Latent Chain-of-Thought for Visual Reasoning](llm_reasoning/latent_chain-of-thought_for_visual_reasoning.md)**

:   将视觉CoT推理重新建模为后验推断问题，提出基于摊销变分推断(AVI)的LaCoT训练框架——包含参考引导GFlowNet微调(RGFN)、token级奖励近似和贝叶斯推理缩放(BiN)——在Qwen2.5-VL 3B/7B上比GRPO高出10.6%，在7个视觉推理基准上达到开源SOTA。

**[Let LRMs Break Free from Overthinking via Self-Braking Tuning](llm_reasoning/let_lrms_break_free_from_overthinking_via_self-braking_tuning.md)**

:   提出 Self-Braking Tuning (SBT) 框架，通过识别推理轨迹中的过度思考模式并构造自适应长度训练数据，使大型推理模型（LRM）学会自主判断何时停止推理，在数学推理任务上减少 30%-60% token 消耗的同时保持精度。

**[Let Me Think! A Long Chain-of-Thought Can Be Worth Exponentially Many Short Ones](llm_reasoning/let_me_think_a_long_chainofthought_can_be_worth_exponentiall.md)**

:   本文从理论和实验两方面证明：存在推理任务（图连通性问题），其中一条长 CoT（顺序缩放）的能力等价于指数多条短 CoT（并行缩放）——即将 CoT 长度减少一点点，就需要指数级增加并行采样数才能达到同等准确率。

**[LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](llm_reasoning/limopro_reasoning_refinement_for_efficient_and_effective_test-time_scaling.md)**

:   提出PIR（基于困惑度的重要性精炼）框架，将LRM蒸馏的推理链分为"渐进推理"和"功能性步骤"（验证/多方法验证/纠错）两类，仅裁剪低PIR值的功能性步骤而完整保留渐进推理骨架，使微调后的模型在AIME/AMC/GPQA上准确率提升0.9%-6.6%同时token减少3%-41%，效率最高提升71%。

**[Lost in Transmission: When and Why LLMs Fail to Reason Globally](llm_reasoning/lost_in_transmission_when_and_why_llms_fail_to_reason_globally.md)**

:   提出有界注意力前缀预言机(BAPO)计算框架，将LLM的注意力头建模为有限带宽通信信道，证明图可达性等全局推理问题是BAPO-hard的（需超常数带宽），且CoT可将任何BAPO-hard问题转化为BAPO-easy问题，实验在GPT-4o/Claude/Gemini上验证理论预测。

**[Many LLMs Are More Utilitarian Than One](llm_reasoning/many_llms_are_more_utilitarian_than_one.md)**

:   在6个LLM上实验发现，多智能体集体讨论道德困境时会产生与人类群体类似的"功利主义增强"（Utilitarian Boost）——集体比个体更倾向接受为"多数人利益"伤害少数人，但LLM产生此效应的机制与人类不同（人类因结果敏感度增强，LLM则因规范敏感度降低或公正性增强等多种模式），且可通过模型异质性和提示多样性缓解。

**[Mind the Gap: Bridging Thought Leap for Improved Chain-of-Thought Tuning](llm_reasoning/mind_the_gap_bridging_thought_leap_for_improved_chain-of-thought_tuning.md)**

:   本文首次系统性地定义了 CoT 推理链中的"思维跳跃"(Thought Leap)现象，提出 CoT-Bridge 模型自动检测并补全推理链中被省略的中间步骤，在 NuminaMath 上最高提升 +5.87%，并可作为即插即用模块增强蒸馏和 RL 流程。

**[On Learning Verifiers and Implications to Chain-of-Thought Reasoning](llm_reasoning/on_learning_verifiers_and_implications_to_chain-of-thought_reasoning.md)**

:   从PAC学习角度系统研究CoT验证器的可学习性，在不同验证目标下给出样本复杂度的上下界，并揭示验证与生成之间的有趣计算关系。

**[One Token Embedding Is Enough to Deadlock Your Large Reasoning Model](llm_reasoning/one_token_embedding_is_enough_to_deadlock_your_large_reasoning_model.md)**

:   本文提出 Deadlock Attack，通过优化单个对抗性 token embedding 并以后门方式植入 LRM，使模型在推理时陷入永久思考循环（无限生成 "Wait"、"But" 等过渡词），在 4 个 LRM 和 3 个数学推理 benchmark 上实现 100% 攻击成功率，且对正常输入几乎无性能影响。

**[OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](llm_reasoning/os-harm_a_benchmark_for_measuring_safety_of_computer_use_agents.md)**

:   本文提出 OS-Harm，首个面向通用计算机使用 Agent（非仅浏览器）的安全性 benchmark，覆盖用户恶意使用、Prompt 注入攻击、模型自身失误三类风险共 150 个任务，评测发现前沿模型（o4-mini、Claude 3.7 Sonnet、Gemini 2.5 Pro 等）普遍直接服从有害指令（最高 70% 不安全率），且对基础 prompt 注入有 20% 的服从率。

**[ProofSketch: Efficient Verified Reasoning for Large Language Models](llm_reasoning/proofsketch_efficient_verified_reasoning_for_large_language_models.md)**

:   提出 ProofSketch 框架，通过符号闭包前向推理+短sketch生成+形式验证的多阶段pipeline，在降低token用量的同时提供逻辑推理的形式化正确性保证。

**[Provable Scaling Laws for the Test-Time Compute of Large Language Models](llm_reasoning/provable_scaling_laws_for_the_testtime_compute_of_large_lang.md)**

:   提出两种具有可证明缩放律的测试时计算算法——Knockout（淘汰赛式：生成多个候选再两两比较淘汰）和 League（联赛式：用平均胜率选最优候选），证明在 LLM 生成正确解概率 >0 且比较能力优于随机的极弱假设下，失败概率随测试时计算增加呈指数或幂律衰减，且仅需黑盒 LLM 无需额外验证器。

**[Re-FORC: Adaptive Reward Prediction for Efficient Chain-of-Thought Reasoning](llm_reasoning/re-forc_adaptive_reward_prediction_for_efficient_chain-of-thought_reasoning.md)**

:   提出Re-FORC，一个轻量级adapter在CoT推理过程中实时预测未来期望奖励 $\psi(t|x,z,\pi)$，将推理计算分配建模为Pandora's box问题，实现自适应早停（节省26%计算）、模型+计算联合选择（同等计算下+4%准确率或同等准确率-55%计算）和测试时计算伸缩（+11%准确率），且用户可通过代价系数 $\lambda$ 在推理时自由调控精度-效率权衡，无需重训。

**[RealMath: A Continuous Benchmark for Evaluating Language Models on Research-Level Mathematics](llm_reasoning/realmath_a_continuous_benchmark_for_evaluating_language_models_on_research-level.md)**

:   提出 RealMath，一个从 arXiv 论文和 Math StackExchange 中自动提取可验证数学问题的**可持续刷新**基准，用于评估 LLM 在真实研究级数学任务上的能力。

**[ReasonFlux-PRM: Trajectory-Aware PRMs for Long Chain-of-Thought Reasoning in LLMs](llm_reasoning/reasonfluxprm_trajectoryaware_prms_for_long_chainofthought_r.md)**

:   ReasonFlux-PRM 发现现有 PRM 无法有效评估推理模型的中间思考轨迹（trajectory），提出融合步骤级对齐/质量/连贯性分数和轨迹级模板引导奖励的 trajectory-aware PRM，在离线数据选择（SFT +12.1%）、在线 RL 奖励（+4.5%）和测试时 Best-of-N 缩放（+6.3%）三个场景中均显著优于包括 Qwen2.5-Math-PRM-72B 在内的强基线。

**[Reasoning by Superposition: A Theoretical Perspective on Chain of Continuous Thought](llm_reasoning/reasoning_by_superposition_a_theoretical_perspective_on_chain_of_continuous_thou.md)**

:   本文从理论上证明了连续思维链（Coconut）在有向图可达性问题上的表达优势：两层Transformer使用D步连续思维即可解决直径为D的图可达性问题，而离散CoT需要O(n²)步，其核心机制是连续思维向量以"叠加态"同时编码多条搜索前沿，实现隐式并行BFS。

**[Reasoning Models Better Express Their Confidence](llm_reasoning/reasoning_models_better_express_their_confidence.md)**

:   系统性证明推理模型（extended CoT）比非推理模型具有显著更优的置信度校准能力，并揭示"慢思考"行为（探索替代方案、回溯、验证）是校准提升的根本来源。

**[Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models](llm_reasoning/reasoning_models_hallucinate_more_factuality-aware_reinforcement_learning_for_la.md)**

:   揭示了RL训练的推理模型（如DeepSeek-R1）比非推理模型产生更多幻觉，从理论上分析了三个根因（高方差梯度、熵约束、伪局部最优），并提出FSPO算法通过步级事实性验证调整token级advantage，在减少幻觉的同时保持甚至提升推理能力。

**[Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling](llm_reasoning/rethinking_optimal_verification_granularity_for_compute-efficient_test-time_scal.md)**

:   提出 Variable Granularity Search (VG-Search)，通过可调的验证粒度参数 $g$ 统一 Beam Search 和 Best-of-N，发现传统每步验证是次优的，自适应调整 $g$ 可在提升准确率3%+的同时减少52%+的计算量。

**[SafePath: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment](llm_reasoning/safepath_preventing_harmful_reasoning_in_chain-of-thought_via_early_alignment.md)**

:   提出 SafePath，仅在推理开始处微调 8 个 token 的"Safety Primer"（"Let's think about safety first"），即可有效引导 LRM 走向安全推理路径，在 DeepSeek-R1-Distill 上减少 90% 有害输出且仅需 Direct Refusal 1/296 的训练计算量。

**[Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding](llm_reasoning/sampling-efficient_test-time_scaling_self-estimating_the_best-of-n_sampling_in_e.md)**

:   提出 Self-Truncation Best-of-N (ST-BoN) 解码方法，通过理论证明早期隐状态一致性可预测最终一致性，在生成早期就识别并截断次优样本，实现降低80%+内存和50%延迟的同时保持BoN性能。

**[Scalable Best-of-N Selection for Large Language Models via Self-Certainty](llm_reasoning/scalable_best-of-n_selection_for_large_language_models_via_self-certainty.md)**

:   提出Self-Certainty度量，利用LLM输出的token概率分布量化模型信心，在无需额外奖励模型的情况下实现可扩展的Best-of-N选择，性能媲美或超越基于奖励模型的方法。

**[scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery](llm_reasoning/scpilot_large_language_model_reasoning_toward_automated_single-cell_analysis_and.md)**

:   提出 scPilot 框架和 scBench 基准，让LLM直接在单细胞RNA-seq数据上进行"组学原生推理"（读取标记基因→提出假设→调用工具验证→迭代修正），实现细胞类型标注准确率提升11%、轨迹推断graph-edit distance降低30%。

**[Segment Policy Optimization: Effective Segment-Level Credit Assignment in RL for Large Language Models](llm_reasoning/segment_policy_optimization_effective_segment-level_credit_assignment_in_rl_for_.md)**

:   提出SPO框架，采用段级（而非令牌级或轨迹级）的advantage估计，通过新颖的蒙特卡洛方法和树形采样，在短CoT和长CoT场景下分别超越PPO和GRPO 6-12和7-11个百分点。

**[笔记8：PolyMath - 多语言背景下的数学推理评估](llm_reasoning/self-evaluating_llms_for_multi-step_tasks_stepwise_confidence_estimation_for_fai.md)**

:   PolyMath构建的18语言、4难度级、500问题数学推理基准揭露：(1)推理性能跨语言差异达10分，(2)推理模型输入-输出语言一致性低且可能影响性能，(3)思考长度在语言间显著不一致，为多语言推理研究提供新视角。

**[Simulating Society Requires Simulating Thought](llm_reasoning/simulating_society_requires_simulating_thought.md)**

:   本文提出从"行为主义"模式转向"认知建模"范式，通过 GenMinds 框架用因果信念图建模 LLM Agent 的内部推理过程，并设计 RECAP 基准从可追溯性、人口统计敏感性和干预一致性三维度评估推理保真度。

**[SLAyiNG: Towards Queer Language Processing](llm_reasoning/slaying_towards_queer_language_processing.md)**

:   构建了首个显式标注的酷儿俚语（queer slang）数据集 SLAyiNG，包含 695 个术语和近 20 万条使用实例，并通过人机标注一致性实验（Krippendorff's α=0.746）表明推理模型可用于预筛选但仍需社区驱动的专家标注。

**[Smaller Models, Smarter Rewards: A Two-Sided Approach to Process and Outcome Rewards](llm_reasoning/smaller_models_smarter_rewards_a_two-sided_approach_to_process_and_outcome_rewar.md)**

:   将 Phi-4 系列小模型（3.8B/14B）的最后一层替换为回归头并微调，使其同时具备 ORM（结果奖励）和 PRM（过程奖励）能力，在代码生成任务上通过选择最优 rollout 实现 20%+ 的 pass@k 提升。

**[SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search](llm_reasoning/solverllm_leveraging_test-time_scaling_for_optimization_problem_via_llm-guided_s.md)**

:   无需训练，通过 MCTS 引导 LLM 生成 6 元素优化表述并转化为求解器代码，在 NL4Opt 上达 97.0%（vs OptiMUS 78.8%），超越微调方法且跨域泛化强。

**[SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models](llm_reasoning/sprint_enabling_interleaved_planning_and_parallelized_execution_in_reasoning_mod.md)**

:   通过将长链式推理轨迹重组为交替的规划-并行执行阶段，Sprint 使推理模型在保持准确率的同时，将长推理链的顺序 token 数减少高达 39%（OOD 任务上最高 65%），实现推理过程的动态并行化。

**[SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction](llm_reasoning/sql-of-thought_multi-agentic_text-to-sql_with_guided_error_correction.md)**

:   提出 SQL-of-Thought——一个多智能体 Text-to-SQL 框架，将任务分解为 schema linking → 子问题识别 → CoT 查询计划生成 → SQL 生成 → 基于 31 类错误分类法的引导修正循环，用 Claude 3 Opus 在 Spider 上达到 91.59% 执行准确率，比此前最佳 Chase SQL（87.6%）提升近 4 个百分点。

**[SQL-R1: Training Natural Language to SQL Reasoning Model By Reinforcement Learning](llm_reasoning/sql-r1_training_natural_language_to_sql_reasoning_model_by_reinforcement_learnin.md)**

:   首次系统地将 GRPO 强化学习应用于 NL2SQL 任务，通过四层递进式奖励函数和 200K 冷启动 + 5K 复杂样本 RL 训练策略，7B 模型在 Spider 和 BIRD 上分别达到 88.7% 和 66.6%，超越 GPT-4 同规模模型。

**[Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](llm_reasoning/stop_summation_minform_credit_assignment_is_all_process_rewa.md)**

:   PURE 发现 PRM 导致 reward hacking 的根本原因是 RL 中标准的 sum-form 信用分配（$V(s) = \sum \gamma^t r_t$），并提出 min-form 替代方案（$V(s) = \min_{t' \geq t} r_{t'}$），通过将价值函数限制为未来奖励的最小值而非累积和，显著缓解 reward hacking——仅用 30% 训练步数就达到与规则奖励方法相当的推理性能。

**[The Hawthorne Effect in Reasoning Models: Evaluating and Steering Test Awareness](llm_reasoning/the_hawthorne_effect_in_reasoning_models_evaluating_and_steering_test_awareness.md)**

:   首次系统量化推理型LLM的"测试感知"(Hawthorne效应)：当模型察觉自己在被评估时会改变行为，论文通过线性探针定位感知激活并进行参数编辑引导，揭示测试感知对安全对齐的显著且方向不一致的影响。

**[The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity](llm_reasoning/the_illusion_of_thinking_understanding_the_strengths_and_limitations_of_reasonin.md)**

:   通过可控拼图环境系统揭示大型推理模型（LRMs）的三阶段行为：低复杂度不如标准 LLM、中等复杂度显著优于、高复杂度完全崩溃(0%)，且反直觉地在崩溃时减少思考 token，证实当前 LRMs 并未发展出真正泛化的推理能力。

**[The Impact of Quantization on Large Reasoning Model Reinforcement Learning](llm_reasoning/the_impact_of_quantization_on_large_reasoning_model_reinforcement_learning.md)**

:   系统实验发现在大推理模型的 RL 训练中，量化感知训练（QAFT/STE）会损害推理能力，而训练后量化（PTQ）和 QLoRA 即使在 4-bit 精度下也能很好地保持推理性能，为实践者提供了"先全精度 RL、再 PTQ 量化"的推荐路线。

**[The Virtues of Brevity: Avoid Overthinking in Parallel Test-Time Reasoning](llm_reasoning/the_virtues_of_brevity_avoid_overthinking_in_parallel_test-time_reasoning.md)**

:   证明选择最短答案是一个简单但有效的Best-of-N启发式方法，通过避免过度思考regime大幅降低计算成本，性能与自一致性可比或更优，在推理模型中表现特别突出。

**[ThinkSound: Chain-of-Thought Reasoning in Multimodal Large Language Models for Audio Generation and Editing](llm_reasoning/thinksound_chain-of-thought_reasoning_in_multimodal_large_language_models_for_au.md)**

:   提出三阶段交互式视频转音频框架 ThinkSound，通过 MLLM 生成结构化 CoT 推理来指导统一的音频生成基础模型，在 VGGSound 和 MovieGen Audio 基准上达到 SOTA，同时支持对象级精细化和自然语言指令编辑。

**[TIME: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios](llm_reasoning/time_a_multilevel_benchmark_for_temporal_reasoning_of_llms_i.md)**

:   TIME 提出一个面向真实世界时序推理的多层级 benchmark，覆盖 38,522 个 QA、3 个子数据集与 11 个细粒度子任务，系统刻画 LLM 在高密度时间信息、快速事件变化和复杂社会时序依赖下的推理能力，并分析了 test-time scaling 对 temporal reasoning 的实际影响。

**[Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties](llm_reasoning/topology_of_reasoning_understanding_large_reasoning_models_through_reasoning_gra.md)**

:   提出"推理图"概念——通过对 LLM 隐藏状态聚类构建有向图，从环路密度、直径和小世界指标三个图论维度分析大推理模型（如 DeepSeek-R1 蒸馏系列），发现推理模型的推理图具有显著更多环路（~5/样本）、更大直径和更强小世界特性（~6倍），且这些特性随任务难度和模型规模增长。

**[Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](llm_reasoning/towards_thinking-optimal_scaling_of_test-time_compute_for_llm_reasoning.md)**

:   揭示了过度延长 CoT 长度会损害 LLM 推理性能，并提出 Thinking-Optimal Scaling (TOPS) 策略，让模型为每道题选择最短正确响应进行自我提升，在效果和效率上同时优于现有蒸馏方法。

**[Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](llm_reasoning/transformers_provably_learn_chain-of-thought_reasoning_with_length_generalizatio.md)**

:   从优化理论角度证明了一层 Transformer 通过梯度下降在合成状态追踪任务上能学会 CoT 推理并实现长度泛化，首次为常数深度 Transformer 学习 $\mathsf{NC}^1$-complete 问题（超越之前局限于 $\mathsf{TC}^0$ 的理论）提供了收敛保证。

**[TTS-VAR: A Test-Time Scaling Framework for Visual Auto-Regressive Generation](llm_reasoning/tts-var_a_test-time_scaling_framework_for_visual_auto-regressive_generation.md)**

:   提出 TTS-VAR——首个针对 Visual Auto-Regressive (VAR) 模型的测试时扩展框架，将图像生成建模为路径搜索问题，通过自适应递减批量 + 早期聚类多样性搜索 + 后期重采样潜力选择，在 Infinity 2B 上将 GenEval 分数从 0.69 提升到 0.75（+8.7%），N=2 即超越 Best-of-N 的 N=8 效果。

**[Two-Stage Learning of Stabilizing Neural Controllers via Zubov Sampling and Iterative Domain Expansion](llm_reasoning/two-stage_learning_of_stabilizing_neural_controllers_via_zubov_sampling_and_iter.md)**

:   提出两阶段训练框架——先用 Zubov 采样 + 动态域扩展估计吸引域（ROA），再用 CEGIS 反例精炼——联合学习神经网络控制器和 Lyapunov 函数，ROA 体积比基线大 5 到 $1.5 \times 10^5$ 倍，验证速度比 dReal 快 40-10000 倍。

**[Unlabeled Data Can Provably Enhance In-Context Learning of Transformers](llm_reasoning/unlabeled_data_can_provably_enhance_in-context_learning_of_transformers.md)**

:   提出增强型ICL框架，在prompt中同时包含少量标记样本和大量无标记样本，理论证明多层Transformer通过CoT可模拟EM算法从无标记数据中提取信息，将分类excess risk从 $\mathcal{O}(1/\sqrt{N})$ 改进到 $\mathcal{O}(1/\sqrt{N + \text{poly}(M)})$。

**[Unlocking Multimodal Mathematical Reasoning via Process Reward Model](llm_reasoning/unlocking_multimodal_mathematical_reasoning_via_process_reward_model.md)**

:   提出URSA三阶段框架，依次构建百万级多模态CoT数据(MMathCoT-1M)训练基座、双视角过程监督数据(DualMath-1.1M)训练PRM、以及PS-GRPO算法将PRM融入在线RL，8B模型在6个数学基准上平均超越GPT-4o 2.7%。

**[笔记6：Self-Evaluating LLMs - 多步任务的步级置信度估计](llm_reasoning/value-guided_search_for_efficient_chain-of-thought_reasoning.md)**

:   本文扩展置信度估计到多步任务，证明步级评估相比整体评估能更有效地检测推理失败，相对整体评估在CoQA上AUC-ROC提升15%，为多步推理系统的可信部署提供实用框架。

**[Visual Thoughts: A Unified Perspective of Understanding Multimodal Chain-of-Thought](llm_reasoning/visual_thoughts_a_unified_perspective_of_understanding_multi.md)**

:   首次从统一视角揭示多模态CoT工作的核心机制——"视觉思维"(Visual Thoughts)：MCoT通过将视觉信息缓存为中间推理步骤来增强LVLM推理，类似于计算机系统中的cache vs外部存储；定义了四种视觉思维表达形式（自然语言/结构化语言/编辑图像/生成图像），发现其有效性取决于表达的清晰性和简洁性。

---

## 🏥 医学图像 { #medical_imaging }

**[3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](medical_imaging/3drad_a_comprehensive_3d_radiology_medvqa_dataset_with_multi.md)**

:   提出 3D-RAD——首个大规模3D医学VQA基准，包含170K条CT影像问答数据，覆盖六类临床任务（含创新性的多时相诊断任务），并配套136K训练集，揭示了现有VLM在3D时序推理上的严重不足。

**[A Novel Approach to Classification of ECG Arrhythmia Types with Latent ODEs](medical_imaging/a_novel_approach_to_classification_of_ecg_arrhythmia_types_with_latent_odes.md)**

:   将 Latent ODE 编码器与梯度提升决策树结合，构建端到端 ECG 心律失常分类流水线，在 360Hz→45Hz 降采样下 AUC-ROC 仅从 0.984 降至 0.976，展示了对低采样率的鲁棒性。

**[A Unified Solution to Video Fusion: From Multi-Frame Learning to Benchmarking](medical_imaging/a_unified_solution_to_video_fusion_from_multi-frame_learning_to_benchmarking.md)**

:   提出首个统一视频融合框架 UniVF（基于多帧学习 + 光流特征 warping + 时序一致性损失），并构建首个覆盖四大融合任务（多曝光、多焦点、红外-可见光、医学）的视频融合基准 VF-Bench，在全部子任务上取得 SOTA。

**[A Variational Manifold Embedding Framework for Nonlinear Dimensionality Reduction](medical_imaging/a_variational_manifold_embedding_framework_for_nonlinear_dimensionality_reductio.md)**

:   提出一种变分流形嵌入框架，将降维问题形式化为最优嵌入映射的优化问题（最小化先验分布与数据分布pullback之间的KL散度），在理论上统一了PCA与非线性降维方法，并利用变分法（Euler-Lagrange方程）和Noether定理为最优嵌入提供了可解释性约束。

**[AANet: Virtual Screening under Structural Uncertainty via Alignment and Aggregation](medical_imaging/aanet_virtual_screening_under_structural_uncertainty_via_alignment_and_aggregati.md)**

:   针对现实药物发现中蛋白质 holo 结构不可用的问题，提出 AANet——通过三模态对比学习（配体-holo pocket-检测cavity）对齐表征并用交叉注意力聚合多个候选结合位点，在 apo/predicted 蛋白质结构上的盲筛性能远超 SOTA（DUD-E 上 EF1% 从 11.75 提升至 37.19）。

**[Active Target Discovery under Uninformative Prior: The Power of Permanent and Transient Memory](medical_imaging/active_target_discovery_under_uninformative_prior_the_power_of_permanent_and_tra.md)**

:   提出 EM-PTDM 框架，受神经科学双记忆系统启发，利用预训练扩散模型作为"永久记忆"并结合基于 Doob's h-transform 的轻量"瞬时记忆"模块，在**无领域先验数据**的条件下实现高效的主动目标发现，理论保证先验单调改进。

**[Amortized Active Generation of Pareto Sets](medical_imaging/amortized_active_generation_of_pareto_sets.md)**

:   提出 A-GPS 框架，通过学习 Pareto 集的条件生成模型实现在线离散黑箱多目标优化——用非支配类概率估计器（CPE）作为 PHVI 的隐式估计替代显式超体积计算，并通过偏好方向向量实现摊还式后验偏好条件化（无需重新训练），在合成基准和蛋白质设计任务上展示了优越的样本效率。

**[AQuaMaM: An Autoregressive Quaternion Manifold Model for Rapidly Estimating Complex Protein Structures](medical_imaging/aquamam_an_autoregressive_quaternion_manifold_model_for_rapidly_estimating_compl.md)**

:   AQuaMaM 提出基于四元数流形的自回归蛋白质结构预测模型——将蛋白质骨架的旋转表示为四元数（在 $S^3$ 流形上），用自回归方式沿序列逐步预测每个残基的局部坐标系旋转，实现比 AlphaFold 快数个量级的结构估计。

**[Atomic Diffusion Models for Small Molecule Structure Elucidation from NMR Spectra](medical_imaging/atomic_diffusion_models_for_small_molecule_structure_elucidation_from_nmr_spectr.md)**

:   提出 ChefNMR，首个基于 3D 原子扩散模型的端到端框架，仅从 1D NMR 光谱和化学式直接预测未知小分子（尤其是复杂天然产物）的分子结构，在合成和实验数据集上均达到 SOTA。

**[GraphFLA: Augmenting Biological Fitness Prediction Benchmarks with Landscape Features](medical_imaging/augmenting_biological_fitness_prediction_benchmarks_with_landscapes_features_fro.md)**

:   GraphFLA 是一个高效的适应度景观分析框架——计算 20 个生物学意义的景观特征（粗糙度/上位性/可导航性/中性），在 5300+ 真实景观（ProteinGym/RNAGym/CIS-BP）上揭示模型性能高度依赖景观拓扑，如 VenusREM 在高可导航性景观上优于 ProSST 但在高上位性景观上弱于后者，处理百万突变体仅需 20 秒（vs MAGELLAN 5 小时）。

**[Autoencoding Random Forests](medical_imaging/autoencoding_random_forests.md)**

:   RFAE 首次为随机森林构建了原则性的编码-解码框架——利用 RF 核的正定性和普适性进行扩散映射谱分解得到低维编码，通过 k-NN 回归在叶节点空间中解码回原始特征，在 20 个表格数据集上重建质量排名 1.80（大幅优于 TVAE 3.38、AE 3.27），并成功应用于 MNIST 重建和 scRNA-seq 批次效应去除。

**[BarcodeMamba+: Advancing State-Space Models for Fungal Biodiversity Research](medical_imaging/barcodemamba_advancing_state-space_models_for_fungal_biodiversity_research.md)**

:   BarcodeMamba+ 是用于真菌 DNA 条形码分类的基础模型——基于状态空间模型架构，采用预训练+微调范式利用部分标注数据，结合层次标签平滑、加权损失和多头输出增强真菌分类（93%样本种级未标注），在所有分类层级上超越现有方法。

**[CrossNovo: Bidirectional Representations Augmented Autoregressive Biological Sequence Generation](medical_imaging/bidirectional_representations_augmented_autoregressive_biological_sequence_gener.md)**

:   CrossNovo 融合自回归（AR）和非自回归（NAR）解码器，通过共享谱编码器 + 重要性退火 + 梯度阻断知识蒸馏，让 NAR 的双向全局理解增强 AR 的序列生成能力，在 9-Species 基准上氨基酸精度达 0.811（+2.6%）、肽段召回 0.654（+5.3%）。

**[Brain-Tuning Improves Generalizability And Efficiency Of Brain Alignment In Spee](medical_imaging/brain-tuning_improves_generalizability_and_efficiency_of_brain_alignment_in_spee.md)**

:   提出 Multi-brain-tuning 方法，通过联合多个被试的 fMRI 数据微调预训练语音模型，将脑对齐所需数据量降低 5 倍，同时脑对齐度提升最高 50%，并可泛化到全新被试和数据集。

**[Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens](medical_imaging/brain_harmony_a_multimodal_foundation_model_unifying_morphology_and_function_int.md)**

:   首个统一脑结构形态（T1 sMRI）与功能动态（fMRI）的多模态脑基础模型，通过几何谐波预对齐和时序自适应 Patch Embedding（TAPE）将高维神经影像压缩为紧凑的 1D token 表示，在神经发育/退行性疾病诊断和认知预测任务上全面超越先前方法。

**[Bridging Graph and State-Space Modeling for Intensive Care Unit Length of Stay Prediction](medical_imaging/bridging_graph_and_state-space_modeling_for_intensive_care_unit_length_of_stay_p.md)**

:   提出 S2G-Net，将 Mamba 状态空间模型的时序编码与多视图图神经网络（GraphGPS）进行双路融合，用于 ICU 住院时长（LOS）预测，在 MIMIC-IV 数据集上全面超越序列模型、图模型和混合基线。

**[Care-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson's Disease Gait Assessment](medical_imaging/care-pd_a_multi-site_anonymized_clinical_dataset_for_parkinsons_disease_gait_ass.md)**

:   发布 Care-PD——目前最大的面向帕金森病步态分析的多站点匿名 3D 网格数据集（9 个队列、8 个临床中心、362 名受试者、8477 段步行），并在 UPDRS 步态评分和运动预训练任务上提供系统性 benchmark，证明在 Care-PD 上微调可将 MPJPE 从 60.8mm 降至 7.5mm，F1 提升 17 个百分点。

**[CGBench: Benchmarking Language Model Scientific Reasoning for Clinical Genetics Research](medical_imaging/cgbench_benchmarking_language_model_scientific_reasoning_for_clinical_genetics_r.md)**

:   提出 CGBench，一个基于 ClinGen 专家标注的临床遗传学 benchmark，从变异和基因策展角度评估 LLM 的科学文献推理能力，涵盖证据评分、证据验证和实验证据提取三个任务，发现推理模型在细粒度任务上表现最佳但在高层判断上不如非推理模型。

**[CodeCrash: Exposing LLM Fragility to Misleading Natural Language in Code Reasoning](medical_imaging/codecrash_exposing_llm_fragility_to_misleading_natural_language_in_code_reasonin.md)**

:   提出 CodeCrash 压力测试框架，通过功能等价的结构扰动和误导性自然语言注入（注释/print/暗示），系统评估 17 个 LLM 的代码推理鲁棒性，揭示模型平均性能下降 23.2%，CoT 仅能挽回至 13.8%，并首次发现大推理模型（LRM）中的 "Reasoning Collapse" 现象。

**[Compressing Biology: Evaluating the Stable Diffusion VAE for Phenotypic Drug Discovery](medical_imaging/compressing_biology_evaluating_the_stable_diffusion_vae_for_phenotypic_drug_disc.md)**

:   首次系统评估 Stable Diffusion VAE（SD-VAE）在 Cell Painting 显微镜图像上的重建质量，发现 SD-VAE 在像素级和生物信号层面均能良好保留表型信息（FR 几乎无下降），且通用特征提取器 InceptionV3 在检索任务上与领域专用模型 OpenPhenom 持平甚至更优。

**[ConfRover: Simultaneous Modeling of Protein Conformation and Dynamics via Autoregression](medical_imaging/confrover_simultaneous_modeling_of_protein_conformation_and_dynamics_via_autoreg.md)**

:   ConfRover 提出自回归框架将蛋白质 MD 轨迹分解为逐帧条件生成 $p(\mathbf{x}^{1:L}) = \prod_l p(\mathbf{x}^l | \mathbf{x}^{<l})$，通过编码器 + 因果 Transformer + SE(3) 扩散解码器的模块化架构，首次在单一模型中统一轨迹模拟、时间无关构象采样和构象插值三大任务，在 ATLAS 数据集上全面超越 MDGen。

**[Convolutional Monge Mapping between EEG Datasets to Support Independent Component Labeling](medical_imaging/convolutional_monge_mapping_between_eeg_datasets_to_support_independent_componen.md)**

:   本文扩展 CMMN（Convolutional Monge Mapping Normalization）方法，提出通道平均 PSD + $\ell_1$ 归一化质心和 subject-to-subject 匹配两种策略，生成单一时域滤波器实现不同通道数的 EEG 数据集间域适应，在独立成分（IC）脑/非脑分类中 F1 从 0.77 提升至 0.84，超越 ICLabel（0.88→0.91）。

**[CureAgent: A Training-Free Executor-Analyst Framework for Clinical Reasoning](medical_imaging/cureagent_a_training-free_executor-analyst_framework_for_clinical_reasoning.md)**

:   CureAgent 提出 Executor-Analyst 协作框架，将精确工具调用（TxAgent/Llama-8B 做 Executor）与高层临床推理（Gemini 2.5 做 Analyst）解耦，配合分层集成（Stratified Ensemble）的 Late Fusion 拓扑保留证据多样性，在 CURE-Bench 上达到 83.8% 准确率（无需端到端微调），揭示了上下文-性能悖论和动作空间维度灾难两个关键 scaling 发现。

**[CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays](medical_imaging/cxreasonbench_a_benchmark_for_evaluating_structured_diagnostic_reasoning_in_ches.md)**

:   提出 CheXStruct + CXReasonBench，一个基于胸部X光的结构化诊断推理评估框架，通过多路径、多阶段评估揭示现有 LVLM 在中间推理步骤上的严重不足。

**[DCA: Graph-Guided Deep Embedding Clustering for Brain Atlases](medical_imaging/dca_graph-guided_deep_embedding_clustering_for_brain_atlases.md)**

:   DCA（Deep Cluster Atlas）提出图引导深度嵌入聚类框架，结合预训练 Swin-UNETR 的体素级时空嵌入和 KNN 图空间正则化，通过 KL 散度对齐软分配与图谱聚类辅助标签，生成功能一致且空间连续的个性化脑图谱，在 HCP 数据集上同态性提升 98.8%、轮廓系数提升 29%，并在自闭症诊断、认知解码等下游任务中超越现有图谱。

**[De novo generation of functional terpene synthases using TpsGPT](medical_imaging/de_novo_generation_of_functional_terpene_synthases_using_tpsgpt.md)**

:   TpsGPT 通过在 79K 萜烯合酶（TPS）序列上微调蒸馏版 ProtGPT2 Tiny（38.9M 参数），生成 28K 候选序列，经多阶段过滤（困惑度/pLDDT/EnzymeExplorer/CLEAN/InterPro/Foldseek）筛选出 7 条进化距离远（<60% 序列相似度）但结构保守的从头 TPS 序列，湿实验验证其中 2 条具有 TPS 酶活性——以不到 $200 GPU 成本实现功能酶从头设计。

**[Demo: Generative AI helps Radiotherapy Planning with User Preference](medical_imaging/demo_generative_ai_helps_radiotherapy_planning_with_user_preference.md)**

:   提出 Flexible Dose Proposer (FDP)，通过两阶段训练框架（VQ-VAE 预训练 + 多条件编码）实现基于滑块的用户偏好交互式 3D 剂量分布预测，并集成到 Eclipse 临床治疗计划系统中，在头颈部癌症放疗场景中超越 Varian RapidPlan。

**[Demo: Guide-RAG: Evidence-Driven Corpus Curation for Retrieval-Augmented Generation in Long COVID](medical_imaging/demo_guide-rag_evidence-driven_corpus_curation_for_retrieval-augmented_generatio.md)**

:   系统评估了六种 RAG 语料库配置用于长新冠（Long COVID）临床问答，发现将临床指南与高质量系统综述结合的 GS-4 配置在 faithfulness、relevance 和 comprehensiveness 三维度上一致优于单指南和大规模文献库方案，并提出 Guide-RAG 框架和 LongCOVID-CQ 评估数据集。

**[DermaCon-IN: A Multi-concept Annotated Dermatological Image Dataset of Indian Skin Disorders](medical_imaging/dermacon-in_a_multi-concept_annotated_dermatological_image_dataset_of_indian_ski.md)**

:   构建了 DermaCon-IN——首个以印度肤色为主的密集标注皮肤病图像数据集（5,450 张 / 3,002 患者 / 245 种诊断），提供三级层次诊断标签、47 个病灶描述符和 49 个解剖位置标注，并用 CNN/ViT/概念瓶颈模型进行基准评测。

**[DesignX: Human-Competitive Algorithm Designer for Black-Box Optimization](medical_imaging/designx_human-competitive_algorithm_designer_for_black-box_optimization.md)**

:   提出 DesignX，首个统一学习算法工作流生成和超参数动态控制两个子任务的自动算法设计框架，通过双 Transformer 智能体在 10k 合成问题上大规模预训练，在合成测试集和蛋白质对接/AutoML/UAV 路径规划等真实场景中超越人类手工设计的优化器。

**[DIsoN: Decentralized Isolation Networks for Out-of-Distribution Detection in Medical Imaging](medical_imaging/dison_decentralized_isolation_networks_for_out-of-distribution_detection_in_medi.md)**

:   提出 Decentralized Isolation Networks (DIsoN)，通过训练二分类器将测试样本从训练数据中"隔离"来检测 OOD，并通过去中心化参数交换实现在不共享数据的情况下利用训练数据信息，在 4 个医学影像数据集 12 个 OOD 检测任务上取得 SOTA。

**[Ditch the Denoiser: Emergence of Noise Robustness in Self-Supervised Learning from Data Curriculum](medical_imaging/ditch_the_denoiser_emergence_of_noise_robustness_in_self-supervised_learning_fro.md)**

:   提出一种全自监督的噪声鲁棒表示学习框架，通过"去噪→噪声"的数据课程学习策略 + 去噪教师正则化，使 DINOv2 等 SSL 模型在推理时无需去噪器即可直接处理噪声输入，在 ImageNet-1k 极端高斯噪声下线性探测精度提升 4.8%。

**[Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](medical_imaging/doctor_approved_generating_medically_accurate_skin_disease_images_through_ai-exp.md)**

:   提出 MAGIC 框架，通过将皮肤科专家定义的临床检查清单转化为 MLLM（如 GPT-4o）可执行的评估反馈，利用 DPO 或奖励模型微调扩散模型，生成临床准确的皮肤病图像用于数据增强，在 20 类皮肤病分类任务上提升 +9.02%，少样本场景提升 +13.89%。

**[Domain-Adaptive Transformer for Data-Efficient Glioma Segmentation in Sub-Saharan MRI](medical_imaging/domain-adaptive_transformer_for_data-efficient_glioma_segmentation_in_sub-sahara.md)**

:   提出 SegFormer3D+，一种面向撒哈拉以南非洲异质 MRI 数据的域自适应 Transformer 架构，通过直方图匹配、影像组学分层采样、频率感知双路径编码器和双注意力机制，在仅 60 例标注数据微调下实现胶质瘤分割 mean Dice 0.81，超越 nnU-Net +2.5%。

**[Dual Mixture-of-Experts Framework for Discrete-Time Survival Analysis](medical_imaging/dual_mixture-of-experts_framework_for_discrete-time_survival_analysis.md)**

:   提出双混合专家（Dual MoE）框架用于离散时间生存分析，结合特征编码器 MoE（建模患者亚组异质性）与风险网络 MoE（捕获时间动态），在 METABRIC 和 GBSG 乳腺癌数据集上提升 time-dependent C-index 最高 0.04。

**[DyG-Mamba: Continuous State Space Modeling on Dynamic Graphs](medical_imaging/dyg-mamba_continuous_state_space_modeling_on_dynamic_graphs.md)**

:   DyG-Mamba 将连续状态空间模型（SSM）引入动态图学习，设计时间跨度感知的连续 SSM——用 Ebbinghaus 遗忘曲线启发的指数衰减函数建模不规则时间间隔，配合谱范数约束的输入依赖参数实现 Lipschitz 鲁棒性，在 12 个动态图基准上平均排名 2.42（vs DyGFormer 2.92），且保持 $O(bdL)$ 线性复杂度。

**[EDBench: Large-Scale Electron Density Data for Molecular Modeling](medical_imaging/edbench_large-scale_electron_density_data_for_molecular_modeling.md)**

:   构建了目前最大规模的电子密度（ED）数据集 EDBench（330 万分子，基于 B3LYP/6-31G** DFT 计算），并设计了涵盖预测、检索、生成三类任务的 ED 基准评估体系，首次系统评估了深度学习模型对电子密度的理解和利用能力。

**[Efficient Adaptive Experimentation with Noncompliance](medical_imaging/efficient_adaptive_experimentation_with_noncompliance.md)**

:   提出 AMRIV——首个面向带非依从性（noncompliance）的自适应实验的半参数高效、多重鲁棒的ATE估计器，结合方差最优的工具变量分配策略和序贯推断保证。

**[EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis](medical_imaging/endobench_a_comprehensive_evaluation_of_multi-modal_large_language_models_for_en.md)**

:   提出 EndoBench，首个覆盖 4 种内窥镜场景、12 项临床任务、5 级视觉提示粒度的综合 MLLM 评估基准，包含 6,832 个经临床验证的 VQA 对，对 23 个 MLLM 的评估显示商用模型整体领先但仍落后人类专家。

**[Energy Matching: Unifying Flow Matching and Energy-Based Models for Generative Modeling](medical_imaging/energy_matching_unifying_flow_matching_and_energy-based_models_for_generative_mo.md)**

:   提出 Energy Matching，通过学习一个时间无关的标量势能场统一流匹配与能量模型：远离数据流形时沿最优传输路径高效传输，靠近流形时过渡为 Boltzmann 平衡分布以建模似然，在 CIFAR-10 上 FID 3.34 大幅超越现有 EBM（>50%提升）。

**[Ewc-Guided Diffusion Replay For Exemplar-Free Continual Learning In Medical Imag](medical_imaging/ewc-guided_diffusion_replay_for_exemplar-free_continual_learning_in_medical_imag.md)**

:   提出将类条件 DDPM 扩散重放与弹性权重巩固（EWC）相结合的无样本持续学习框架，在 MedMNIST v2（8 个 2D/3D 任务）和 CheXpert 上实现了 AUROC 0.851，相比 DER++ 遗忘率降低超 30%，接近联合训练上界（0.869），同时完全无需存储患者原始数据。

**[Exploring and Leveraging Class Vectors for Classifier Editing](medical_imaging/exploring_and_leveraging_class_vectors_for_classifier_editing.md)**

:   提出 Class Vector（类向量），通过计算预训练与微调模型在潜空间中类别质心的差异来捕获类别级适应，利用线性和独立性两个性质，通过简单向量算术实现分类器编辑（遗忘、环境适应、对抗防御），无需重训练即可完成潜空间注入，或用 <1.5K 参数在 1.5 秒内完成权重空间映射。

**[FairGRPO: Fair Reinforcement Learning for Equitable Clinical Reasoning](medical_imaging/fairgrpo_fair_reinforcement_learning_for_equitable_clinical_reasoning.md)**

:   提出 FairGRPO，一种层级式公平强化学习算法，通过自适应重要性加权（基于群体表示量和任务难度）解决临床 AI 中的人群表现差异问题，在 7 个临床数据集（280K样本，5种模态）上将预测平价降低 27.2%、F1 提升 12.49%，并发布首个公平性优化的临床 VLLM——FairMedGemma-4B。

**[Faithful Summarization of Consumer Health Queries: A Cross-Lingual Framework with LLMs](medical_imaging/faithful_summarization_of_consumer_health_queries_a_cross-lingual_framework_with.md)**

:   提出结合 TextRank 抽取式句子选择和医学命名实体识别 (NER) 来引导 LLM 生成忠实医学摘要的框架，在英文 MeQSum 和孟加拉语 BanglaCHQ-Summ 数据集上通过微调 LLaMA-2-7B 实现质量和忠实性的一致提升，SummaC 达 0.57，人工评估 82% 摘要保留关键医学信息。

**[Fapex Fractional Amplitude-Phase Expressor For Robust Cross-Subject Seizure Pred](medical_imaging/fapex_fractional_amplitude-phase_expressor_for_robust_cross-subject_seizure_pred.md)**

:   提出 FAPEX 框架，通过可学习的分数阶神经帧算子 (FrNFO) 实现自适应时频分解，结合幅度-相位交叉编码和空间相关性聚合，在 12 个跨物种、跨模态的癫痫预测基准上全面超越 33 个基线方法。

**[Far from the Shallow: Brain-Predictive Reasoning Embedding through Residual Disentanglement](medical_imaging/far_from_the_shallow_brain-predictive_reasoning_embedding_through_residual_disen.md)**

:   提出残差解纠缠方法，将 LLM 隐藏状态分离为词汇、句法、语义、推理四个近正交嵌入，用于预测颅内 ECoG 脑信号，发现推理信号在时间上（~350-400ms）和空间上（超越经典语言区扩展至视觉皮层）均具有独立的神经特征，揭示了 LLM 与人脑间的推理计算对齐。

**[Few-Shot Learning from Gigapixel Images via Hierarchical Vision-Language Alignment and Modeling](medical_imaging/few-shot_learning_from_gigapixel_images_via_hierarchical_vision-language_alignme.md)**

:   提出 HiVE-MIL，一个层级视觉-语言 MIL 框架，通过构建统一异构图建模跨尺度层级关系（5× 和 20×）和同尺度多模态对齐，配合文本引导的动态过滤机制和层级对比损失，在 TCGA 肺/乳腺/肾癌三个数据集的 16-shot 设置下全面超越已有方法，Macro F1 最高提升 4.1%。

**[FGBench: A Dataset and Benchmark for Molecular Property Reasoning at Functional Group-Level](medical_imaging/fgbench_a_dataset_and_benchmark_for_molecular_property_reasoning_at_functional_g.md)**

:   FGBench 构建了首个官能团级分子属性推理基准（625K QA 对，覆盖 245 个官能团），通过相似分子配对 + AccFG 标注 + 重建验证确保数据质量，揭示即使 o3-mini 在交互任务上也仅 69.3%，化学专用模型（ChemLLM）甚至仅 23.3%。

**[FireGNN: Neuro-Symbolic Graph Neural Networks with Trainable Fuzzy Rules for Interpretable Medical Image Classification](medical_imaging/firegnn_neuro-symbolic_graph_neural_networks_with_trainable_fuzzy_rules_for_inte.md)**

:   提出 FireGNN，首次将可训练模糊规则嵌入 GNN 前向传播中，利用节点度、聚类系数和标签一致性三个拓扑描述子实现内生可解释的医学图像分类，在 5 个 MedMNIST 数据集和 MorphoMNIST 上取得优于标准 GCN/GAT/GIN 及辅助任务方法的性能。

**[Flow Density Control: Generative Optimization Beyond Entropy-Regularized Fine-Tuning](medical_imaging/flow_density_control_generative_optimization_beyond_entropy-regularized_fine-tun.md)**

:   提出 Flow Density Control（FDC），将预训练流/扩散模型的微调从 KL 正则期望奖励最大化推广到**任意分布效用函数 + 任意散度正则**的通用框架，通过将非线性目标分解为一系列线性微调子任务实现，并提供收敛保证。

**[FOXES: A Framework For Operational X-ray Emission Synthesis](medical_imaging/foxes_a_framework_for_operational_x-ray_emission_synthesis.md)**

:   提出 FOXES，一个基于 Vision Transformer 的框架，将太阳多通道 EUV 观测图像翻译为软 X 射线（SXR）通量，整体 Pearson 相关达到 0.982，为远端太阳耀斑检测和更完整的耀斑目录构建奠定基础。

**[Fractional Diffusion Bridge Models](medical_imaging/fractional_diffusion_bridge_models.md)**

:   提出分数扩散桥模型（FDBM），将分数布朗运动（fBM）引入生成扩散桥框架，通过 Hurst 指数 $H$ 控制轨迹的粗糙度和长程依赖性，在蛋白质构象预测和图像翻译任务上超越布朗运动基线。

**[From Black Box to Biomarker: Sparse Autoencoders for Interpreting Speech Models of Parkinson's Disease](medical_imaging/from_black_box_to_biomarker_sparse_autoencoders_for_interpreting_speech_models_o.md)**

:   将大语言模型可解释性研究中的稀疏自编码器（SAE）技术适配到语音帕金森病检测系统中，提出 Mask-based SAE 解决小数据集限制，发现模型预测主要基于低能量区域的频谱通量和频谱平坦度，并进一步揭示这些特征与 MRI 壳核体积显著相关，建立了从模型内部表征到临床生物标志物的桥梁。

**[Generating Multi-Table Time Series EHR from Latent Space with Minimal Preprocessing](medical_imaging/generating_multi-table_time_series_ehr_from_latent_space_with_minimal_preprocess.md)**

:   提出 RawMed——首个以最小有损预处理合成多表时序 EHR 原始数据的框架：将事件文本化 → Residual Quantization 压缩至离散潜空间 → 自回归 Transformer 建模时序动态，在保真度、临床效用和隐私保护上全面超越现有基线。

**[Generative Distribution Embeddings: Lifting Autoencoders to the Space of Distributions for Multiscale Representation Learning](medical_imaging/generative_distribution_embeddings_lifting_autoencoders_to_the_space_of_distribu.md)**

:   提出生成分布嵌入（GDE），将自编码器提升到分布空间——编码器作用于样本集合，解码器替换为条件生成模型，学习分布级别的表示，并在6个计算生物学任务上验证有效性。

**[Generative Modeling of Full-Atom Protein Conformations using Latent Diffusion on Graph Embeddings](medical_imaging/generative_modeling_of_full-atom_protein_conformations_using_latent_diffusion_on.md)**

:   提出 **LD-FPG** 框架，使用 Chebyshev 图神经网络将蛋白质全原子 MD 轨迹编码到低维潜在空间，再用 DDPM 在该空间中生成新的构象集合体（ensemble），首次实现了包含侧链所有重原子的蛋白质构象生成。

**[GFlowNets for Learning Better Drug-Drug Interaction Representations](medical_imaging/gflownets_for_learning_better_drug-drug_interaction_representations.md)**

:   针对药物-药物相互作用（DDI）预测中严重的类别不平衡问题，本文提出将 GFlowNet 与变分图自编码器（VGAE）结合，通过奖励引导的生成采样为稀有交互类型生成合成样本，从而增强模型在罕见但临床关键的交互类型上的预测能力。

**[H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis](medical_imaging/h-ddx_a_hierarchical_evaluation_framework_for_differential_diagnosis.md)**

:   H-DDx 提出基于 ICD-10 分类层级的鉴别诊断评估框架——将预测和真实诊断扩展到祖先节点后计算层级 F1（HDF1），奖励"临床相关的近似正确"而非仅精确匹配，评估 22 个 LLM 后发现领域特化模型（MediPhi）在 HDF1 上从第 20 名升至第 2 名（Top-5 指标完全遮蔽其优势）。

**[ImageNet-trained CNNs are not biased towards texture: Revisiting feature reliance through controlled suppression](medical_imaging/imagenet-trained_cnns_are_not_biased_towards_texture_revisiting_feature_reliance.md)**

:   通过系统化的特征抑制框架（而非冲突选择实验）重新评估 CNN 的特征依赖性，发现 CNN 并非天然偏向纹理，而是主要依赖局部形状特征；且不同领域（CV/MI/RS）的特征依赖模式显著不同。

**[Interpreting GFlowNets for Drug Discovery: Extracting Actionable Insights for Medicinal Chemistry](medical_imaging/interpreting_gflownets_for_drug_discovery_extracting_actionable_insights_for_med.md)**

:   为 SynFlowNet（基于合成反应模板的 GFlowNet）构建了一套多层次可解释性工具包，整合梯度显著性、反事实扰动、稀疏自编码器（SAE）和基序探针，揭示模型内部表征如何编码药物化学相关的理化性质和官能团信息。

**[Is Sequence Information All You Need for Bayesian Optimization of Antibodies?](medical_imaging/is_sequence_information_all_you_need_for_bayesian_optimization_of_antibodies.md)**

:   本文系统比较了序列信息和结构信息在抗体贝叶斯优化中的作用，发现通过蛋白质语言模型（pLM）软约束，纯序列方法可以匹配结构方法的性能，质疑了结构信息在抗体贝叶斯优化中的必要性。

**[Iterative Foundation Model Fine-Tuning on Multiple Rewards](medical_imaging/iterative_foundation_model_fine-tuning_on_multiple_rewards.md)**

:   提出 IterativeRS（迭代 Rewarded Soups），通过在多目标专家策略的独立微调和策略合并之间交替迭代，统一了奖励组合和专家合并两类方法，在小分子设计、DNA 序列生成和文本摘要任务上均优于 MORLHF 和 Rewarded Soups。

**[JanusDNA: A Powerful Bi-directional Hybrid DNA Foundation Model](medical_imaging/janusdna_a_powerful_bi-directional_hybrid_dna_foundation_model.md)**

:   提出JanusDNA，首个双向DNA基础模型，结合Mamba-Attention-MoE混合架构和Janus Modeling训练范式，以自回归的训练效率实现双向理解，在多个基因组基准上达到SOTA。

**[LoMix: Learnable Weighted Multi-Scale Logits Mixing for Medical Image Segmentation](medical_imaging/lomix_learnable_weighted_multi-scale_logits_mixing_for_medical_image_segmentatio.md)**

:   LoMix 提出通过组合突变模块（CMM）生成多尺度 logits 的"突变体"——4 种融合算子（加法/乘法/拼接/注意力加权）× 所有子集组合——配合 NAS 风格的 Softplus 可学习权重自动平衡各 logits 的贡献，在 Synapse 8 器官分割上 DICE 从 80.9% 提升到 85.1%（+4.2%），5% 训练数据下提升 +9.23%。

**[PatientSim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions](medical_imaging/patientsim_a_persona-driven_simulator_for_realistic_doctor-patient_interactions.md)**

:   提出PatientSim——基于真实MIMIC临床数据和四维人格轴（性格、语言能力、病史记忆水平、认知混乱程度）的LLM患者模拟器，生成37种独特人格组合，在8个LLM上评估事实准确性和人格一致性，由4名临床专家验证平均质量得分3.89/4。

**[Posterior Sampling by Combining Diffusion Models with Annealed Langevin Dynamics](medical_imaging/posterior_sampling_by_combining_diffusion_models_with_annealed_langevin_dynamics.md)**

:   提出将扩散模型与退火 Langevin 动力学结合的算法，仅需 $L^4$ 精度的 score 估计即可在（局部）对数凹分布下实现多项式时间的后验采样，首次为带暖启动的逆问题求解提供理论保障。

**[QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](medical_imaging/qoq-med_building_multimodal_clinical_foundation_models_with_domain-aware_grpo_tr.md)**

:   QoQ-Med 构建了覆盖 9 个临床模态（1D ECG + 6 类 2D 影像 + 2 类 3D 扫描）的多模态临床基础模型，提出域感知相对策略优化（DRPO）——通过层级温度缩放（域间 × 域内 K-means 聚类）解决模态/难度不平衡问题，在 261 万指令调优对上训练后平均 F1 达 0.295（vs GRPO 0.193，+52.8%），8 个模态中 6 个最优。

**[Random Search Neural Networks for Efficient and Expressive Graph Learning](medical_imaging/random_search_neural_networks_for_efficient_and_expressive_graph_learning.md)**

:   提出随机搜索神经网络（RSNN），用随机深度优先搜索（DFS）替代随机游走来采样图结构，在稀疏图上仅需$O(\log|V|)$次搜索即可实现完整边覆盖，配合通用序列模型可达到通用逼近能力，在分子和蛋白质基准上以最多16倍更少的采样量持续超越RWNN。

**[Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry](medical_imaging/riemannian_flow_matching_for_brain_connectivity_matrices_via_pullback_geometry.md)**

:   提出DiffeoCFM，利用全局微分同胚诱导的拉回度量，将黎曼流形上的条件流匹配等价转化为欧几里得空间中的标准CFM，实现对脑连接矩阵（SPD/相关矩阵）的高效生成，同时严格保持流形约束，在3个fMRI和2个EEG数据集上达到SOTA。

**[SpecMER: Fast Protein Generation with K-mer Guided Speculative Decoding](medical_imaging/specmer_fast_protein_generation_with_k-mer_guided_speculative_decoding.md)**

:   SpecMER 将投机解码引入蛋白质序列生成，用 K-mer 引导的批量选择策略从 draft 模型的多个候选中选取最符合进化保守性的序列供 target 模型验证，在保持分布一致性的同时实现 24-32% 加速，且生成序列的 NLL 和 pLDDT 结构置信度显著优于无引导的 baseline。

**[STAMP: Spatial-Temporal Adapter with Multi-Head Pooling](medical_imaging/stamp_spatial-temporal_adapter_with_multi-head_pooling.md)**

:   STAMP 为时间序列基础模型（TSFM）设计了仅 750K 参数的轻量空间-时间适配器，通过三组位置编码（token/空间/时间）+ 交叉 GMLP 混合 + 多头注意力池化，使冻结的 TSFM（如 MOMENT 385M）在 8 个 EEG 数据集上与 29M 参数的 EEG 专用模型（CBraMod）竞争或超越，在 BCIC-IV-2a 上 Kappa 比 CBraMod 高 193%。

**[The Biased Oracle: Assessing LLMs' Understandability and Empathy in Medical Diagnoses](medical_imaging/the_biased_oracle_assessing_llms_understandability_and_empathy_in_medical_diagno.md)**

:   系统评估 GPT-4o 和 Claude-3.7 在医疗诊断沟通中的可读性和共情能力，发现两者均产生超标的阅读难度（9-13 年级 vs 推荐的 6-8 年级），情感共情随诊断类型和患者教育水平显著变化，且 LLM-as-Judge 存在严重自我偏见（GPT 对自身共情评分膨胀 ~0.3 分）。

**[Uncertainty-Aware Multi-Objective Reinforcement Learning-Guided Diffusion Models for 3D De Novo Molecular Design](medical_imaging/uncertainty-aware_multi-objective_reinforcement_learning-guided_diffusion_models.md)**

:   提出不确定性感知的多目标强化学习框架，引导 3D 分子扩散模型（EDM）同时优化药物相关性（QED）、合成可及性（SAS）和结合亲和力（binding affinity），通过代理模型的预测不确定性动态塑造奖励函数，在三个基准数据集上一致超越基线，并通过分子动力学模拟和 ADMET 验证候选分子的药物潜力。

---

## 🛡️ AI 安全 { #ai_safety }

**[A Set of Generalized Components to Achieve Effective Poison-only Clean-label Backdoor Attacks with Collaborative Sample Selection and Triggers](ai_safety/a_set_of_generalized_components_to_achieve_effective_poison-only_clean-label_bac.md)**

:   提出一组通用化组件（Component A/B/C），通过充分挖掘样本选择与触发器之间的双向协作关系，同时提升 Poison-only Clean-label 后门攻击的攻击成功率（ASR）和隐蔽性，并在多种攻击类型上展现了良好的泛化能力。

**[Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning](ai_safety/adaptive_lora_experts_allocation_and_selection_for_federated_fine-tuning.md)**

:   提出 FedLEASE——解决联邦 LoRA 微调中两个关键问题：(1) 用 LoRA B 矩阵相似度聚类自动确定最优专家数量和分配，(2) 用扩展路由空间（$2M-1$ 维）实现自适应 top-M 专家选择（每个客户端自动决定用几个专家），在 GLUE 上比最强基线平均提升 5.53%。

**[Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text](ai_safety/adversarial_paraphrasing_a_universal_attack_for_humanizing_ai-generated_text.md)**

:   提出 Adversarial Paraphrasing——一种无需训练的通用攻击框架，在逐 token 改写时利用 AI 文本检测器的反馈信号选择"最像人写"的 token，使改写后的 AI 文本在 8 种检测器上平均 T@1%F 下降 87.88%，且具有跨检测器的强迁移性。

**[AI Should Sense Better, Not Just Scale Bigger: Adaptive Sensing as a Paradigm Shift](ai_safety/ai_should_sense_better_not_just_scale_bigger_adaptive_sensin.md)**

:   提出"自适应感知"作为AI发展的范式级转变——受生物感觉系统启发，主张在传感器层面动态调整输入参数（如曝光、增益、多模态配置），而非仅靠扩大模型规模来应对分布偏移，实证表明5M参数的EfficientNet-B0通过自适应感知可超越632M参数的OpenCLIP-H。

**[ALMGuard: Safety Shortcuts and Where to Find Them as Guardrails for Audio-Language Models](ai_safety/almguard_safety_shortcuts_and_where_to_find_them_as_guardrails_for_audio-languag.md)**

:   首个针对音频语言模型（ALM）越狱攻击的防御框架——发现对齐过的 ALM 存在可被激活的潜在安全快捷路径（safety shortcuts），通过 Mel 梯度稀疏掩码（M-GSM）定位关键频率段，施加快捷路径激活扰动（SAP），将平均攻击成功率从 41.6% 降至 4.6%，同时几乎不影响正常任务性能。

**[Benchmarking is Broken — Don't Let AI be its Own Judge](ai_safety/benchmarking_is_broken_--_dont_let_ai_be_its_own_judge.md)**

:   系统性批评当前 AI 基准评估的根本缺陷——数据污染（MMLU 45%+ 重叠）、选择性报告、缺乏监考——并提出 PeerBench 方案：借鉴高考/GRE 的监考范式，用滚动更新的保密题库 + 同行评审质量控制 + 声誉加权评分 + 加密承诺机制构建下一代 AI 评估基础设施。

**[Beyond Last-Click: An Optimal Mechanism for Ad Attribution](ai_safety/beyond_last-click_an_optimal_mechanism_for_ad_attribution.md)**

:   从博弈论角度分析广告归因中 Last-Click 机制的策略操纵漏洞——平台可以通过篡改时间戳获取不公正的归因信用，提出 Peer-Validated Mechanism（PVM）——每个平台的信用仅取决于其他平台的报告（类比同行评审），理论证明 PVM 是占优策略激励兼容（DSIC）且在同质设置下最优，准确率从 34% 提升到 75%（2 平台）。

**[Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks Against LLMs](ai_safety/bits_leaked_per_query_information-theoretic_bounds_on_adversarial_attacks_agains.md)**

:   将 LLM 对抗攻击建模为信息通道问题——定义每次查询的"泄漏比特数" $I(Z;T)$ 为攻击目标属性 $T$ 与可观测信号 $Z$ 的互信息，证明攻击达到误差 $\varepsilon$ 所需最少查询数为 $\log(1/\varepsilon)/I(Z;T)$，在 7 个 LLM 上验证：暴露 answer tokens 需 ~1000 次查询，加 logits 降到 ~100 次，加思维链降到 ~几十次，为透明性-安全性权衡提供首个原则性标尺。

**[Boosting Adversarial Transferability with Spatial Adversarial Alignment](ai_safety/boosting_adversarial_transferability_with_spatial_adversarial_alignment.md)**

:   提出 Spatial Adversarial Alignment (SAA)，通过空间感知对齐和对抗感知对齐两个模块微调代理模型，使其特征与见证模型对齐，从而显著提升对抗样本的跨架构迁移性（CNN→ViT 迁移率提升 25-39%）。

**[Bridging Symmetry and Robustness: On the Role of Equivariance in Enhancing Adversarial Robustness](ai_safety/bridging_symmetry_and_robustness_on_the_role_of_equivariance_in_enhancing_advers.md)**

:   通过在 CNN 中嵌入旋转等变（P4群）和尺度等变卷积层，提出 Parallel 和 Cascaded 两种对称性感知架构，无需对抗训练即可显著提升对抗鲁棒性，并从 CLEVER 框架出发理论证明等变架构能压缩假设空间、正则化梯度、收紧认证鲁棒性界。

**[Causally Reliable Concept Bottleneck Models](ai_safety/causally_reliable_concept_bottleneck_models.md)**

:   提出 C2BM（Causally reliable Concept Bottleneck Models），将概念瓶颈（concept bottleneck）按照因果图结构化组织，通过结合观测数据与背景知识自动学习因果关系，在保持分类精度的同时显著提升因果可靠性、干预响应和公平性。

**[Collective Narrative Grounding: Community-Coordinated Data Contributions to Improve Local AI Systems](ai_safety/collective_narrative_grounding_community-coordinated_data_contributions_to_impro.md)**

:   提出 Collective Narrative Grounding 协议，通过参与式工坊收集社区叙事并结构化为"叙事单元"，用 RAG 管道将本地知识注入 LLM 问答系统，在 LocalBench 上发现 76.7% 的错误可由本地叙事直接修复，GPT-5 在参与式 QA 集上仅 21% 正确率凸显了本地知识鸿沟。

**[Contextual Integrity in LLMs via Reasoning and Reinforcement Learning](ai_safety/contextual_integrity_in_llms_via_reasoning_and_reinforcement_learning.md)**

:   提出 CI-RL 框架，通过 Chain-of-Thought 推理提示 + GRPO 强化学习，用仅约 700 个合成样本训练 LLM 理解"上下文完整性"（contextual integrity），在 PrivacyLens 基准上将隐私泄露率降低最高 40%，且小模型训练后可超越更大基线模型。

**[CoreGuard: Safeguarding Foundational Capabilities of LLMs Against Model Stealing in Edge Deployment](ai_safety/coreguard_safeguarding_foundational_capabilities_of_llms_against_model_stealing_.md)**

:   提出 CoreGuard，通过行置换（row permutation）锁定 Transformer 线性层权重 + 列置换传播协议（propagation protocol）将 TEE 授权次数降至 1 次，以极低计算和通信开销保护边缘部署 LLM 的基础能力不被模型窃取攻击利用。

**[Cost Efficient Fairness Audit Under Partial Feedback](ai_safety/cost_efficient_fairness_audit_under_partial_feedback.md)**

:   在部分反馈（partial feedback）设定下，提出了一套包含新颖成本模型的公平性审计框架，分别在黑盒与混合模型两种场景给出近最优审计算法，审计成本比自然基线降低约 50%。

**[CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming](ai_safety/cpret_a_dataset_benchmark_and_model_for_retrieval_in_competitive_programming.md)**

:   针对竞赛编程中重复/相似题目泛滥导致比赛不公平及 LLM 评测分数虚高的问题，构建了包含四种检索任务的大规模基准 CPRet，并提出 Group-InfoNCE 损失训练的专用检索模型 CPRetriever，在所有任务上超越 20+ 现有嵌入模型，同时揭示了题目相似性对 LiveCodeBench 评测的系统性偏差。

**[CryptoMoE: Privacy-Preserving and Scalable Mixture of Experts Inference via Balanced Expert Routing](ai_safety/cryptomoe_privacy-preserving_and_scalable_mixture_of_experts_inference_via_balan.md)**

:   首个支持 MoE 架构 LLM 隐私推理的框架 CryptoMoE，通过平衡专家路由隐藏路由信息、置信度感知调度协议和批量密文矩阵乘法协议，相比 dense baseline 实现 2.8~3.5× 延迟降低和 2.9~4.3× 通信量降低，准确率损失仅 0.8%。

**[CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D](ai_safety/ctrl-alt-deceit_sabotage_evaluations_for_automated_ai_rd.md)**

:   扩展 MLE-Bench 构建了 20 个代码破坏(code-sabotage)任务和 sandbagging 评测，发现前沿 AI agent 能在完成正常 ML 工程任务的同时成功植入后门等破坏，且在部分情况下逃避 LM monitor 的检测。

**[DeepPersona: A Generative Engine for Scaling Deep Synthetic Personas](ai_safety/deeppersona_a_generative_engine_for_scaling_deep_synthetic_personas.md)**

:   提出 DeepPersona——一个两阶段分类引导的合成人格生成引擎：先从真实用户-ChatGPT 对话中挖掘构建 8000+ 节点的人类属性分类树，再通过渐进式属性采样生成平均 200+ 结构化属性的叙事完整人格，在个性化 QA 准确率上提升 11.6%，社会调查模拟偏差缩小 31.7%。

**[DESIGN: Encrypted GNN Inference via Server-Side Input Graph Pruning](ai_safety/design_encrypted_gnn_inference_via_server-side_input_graph_pruning.md)**

:   提出 DESIGN 框架，在全同态加密(FHE)下通过服务器端输入图剪枝和自适应多项式激活度分配两阶段优化，相比 SEAL 基线加速 FHE GNN 推理约 2× 并维持有竞争力的准确率。

**[DictPFL: Efficient and Private Federated Learning on Encrypted Gradients](ai_safety/dictpfl_efficient_and_private_federated_learning_on_encrypted_gradients.md)**

:   提出 DictPFL 框架，通过将模型权重分解为静态字典+可训练查找表，并结合加密感知剪枝，在联邦学习中实现全梯度同态加密保护的同时，将通信开销降低 402–748 倍、训练速度提升 28–65 倍，运行时间仅为明文 FL 的 2 倍以内。

**[Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming](ai_safety/differential_privacy_for_euclidean_jordan_algebra_with_applications_to_private_s.md)**

:   提出了基于 Euclidean Jordan Algebra (EJA) 的通用 Gaussian 隐私机制，并在此基础上设计了首个差分隐私的 Symmetric Cone Programming (SCP) 求解算法，解决了 Hsu et al. (ICALP 2014) 提出的关于差分隐私半定规划的重要开放问题。

**[Differentially Private Bilevel Optimization: Efficient Algorithms with Near-Optimal Rates](ai_safety/differentially_private_bilevel_optimization_efficient_algorithms_with_near-optim.md)**

:   本文系统研究差分隐私 (DP) 下的双层优化问题，在凸情形下通过指数机制和正则化指数机制给出近紧的上下界（匹配单层 DP-ERM 最优率），在非凸情形下提出二阶 DP 方法实现不依赖内层维度的 SOTA 收敛率。

**[Differentially Private Federated Low Rank Adaptation Beyond Fixed-Matrix](ai_safety/differentially_private_federated_low_rank_adaptation_beyond_fixed-matrix.md)**

:   提出FedASK框架，通过**双阶段sketching流水线**（randomized SVD启发），首次在差分隐私下实现联邦LoRA中**两个低秩矩阵A和B的同步有效更新**，在Llama-2 7B/13B上MMLU提升最高11.5%，GSM8K提升46%。

**[Differentially Private High-dimensional Variable Selection via Integer Programming](ai_safety/differentially_private_high-dimensional_variable_selection_via_integer_programmi.md)**

:   本文提出两种纯差分隐私的稀疏变量选择方法 (top-R 和 mistakes)，利用现代混合整数规划 (MIP) 技术高效探索非凸目标景观，在高维设置（p 达 10000）下实现 SOTA 支撑集恢复率，同时提供理论恢复保证。

**[Distributional Adversarial Attacks and Training in Deep Hedging](ai_safety/distributional_adversarial_attacks_and_training_in_deep_hedging.md)**

:   本文首次将分布对抗攻击引入深度对冲框架，提出基于 Wasserstein 球的可计算对抗训练方法（WPGD 和 WBPGD），显著提升了对冲策略在分布偏移和真实市场数据下的鲁棒性与样本外表现。

**[Distributive Fairness in Large Language Models: Evaluating Alignment with Human Values](ai_safety/distributive_fairness_in_large_language_models_evaluating_alignment_with_human_v.md)**

:   本文系统评估多个 SOTA LLM（GPT-4o、Claude-3.5S、Llama3-70b、Gemini-1.5P）在非策略性资源分配任务中的分配公平性偏好，发现 LLM 与人类存在显著偏差：LLM 偏好效率和无嫉妒性 (EF) 而忽视人类更看重的公平性/平等性 (EQ)，但在选择题模式下 GPT-4o 和 Claude 能正确识别公平方案。

**[DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm](ai_safety/dna-detectllm_unveiling_ai-generated_text_via_a_dna-inspired_mutation-repair_par.md)**

:   本文提出 DNA-DetectLLM，一种受 DNA 突变修复机制启发的零样本 AI 文本检测方法，通过构造理想 AI 序列并量化将输入文本修复到该序列的累积难度作为检测信号，在多个基准数据集上取得 AUROC 相对提升 5.55%、F1 提升 2.08% 的 SOTA 效果。

**[Dual-Flow: Transferable Multi-Target, Instance-Agnostic Attacks via In-the-wild Cascading Flow Optimization](ai_safety/dual-flow_transferable_multi-target_instance-agnostic_attacks_via_in-the-wild_ca.md)**

:   本文提出 Dual-Flow 框架，利用预训练扩散模型的正向 ODE 流和微调 LoRA 速度函数的逆向流进行多目标实例无关对抗攻击，通过级联分布偏移训练策略显著提升迁移攻击成功率（从 Inc-v3 到 Res-152 成功率提升 34.58%），在防御模型上也表现出强鲁棒性。

**[Efficient Fairness-Performance Pareto Front Computation](ai_safety/efficient_fairness-performance_pareto_front_computation.md)**

:   提出 MIFPO 方法，无需训练复杂的公平表示模型即可高效计算公平性-性能 Pareto 前沿，通过理论分析将问题化简为紧凑的离散凹优化问题。

**[Efficient Verified Machine Unlearning for Distillation](ai_safety/efficient_verified_machine_unlearning_for_distillation.md)**

:   提出 PURGE 框架，通过教师-学生 constituent mapping 和增量式多教师蒸馏策略，将 SISA 的验证式遗忘扩展到知识蒸馏场景，在教师端遗忘时仅需部分重训学生模型，实现至少 $N\times$ 的加速。

**[Enabling Differentially Private Federated Learning for Speech Recognition: Benchmarks, Adaptive Optimizers and Gradient Clipping](ai_safety/enabling_differentially_private_federated_learning_for_speech_recognition_benchm.md)**

:   首次为端到端ASR建立FL+DP的实用基准，通过**逐层裁剪（per-layer clipping）**结合**LAMB优化器**的层级梯度归一化，在强隐私保证下实现仅1.3%~4.6%的WER绝对退化。

**[Enhancing CLIP Robustness via Cross-Modality Alignment](ai_safety/enhancing_clip_robustness_via_crossmodality_alignment.md)**

:   提出COLA——一个training-free的框架，通过将对抗扰动后的图像特征投影到文本特征张成的子空间来消除非语义噪声，再用最优传输(OT)在分布层面细粒度对齐图文特征，在14个零样本分类基准上平均提升6.7%的对抗鲁棒准确率，同时维持干净样本性能。

**[Enhancing Graph Classification Robustness with Singular Pooling](ai_safety/enhancing_graph_classification_robustness_with_singular_pooling.md)**

:   首次系统分析 flat pooling（Sum/Avg/Max）对图分类对抗鲁棒性的影响，推导各自的对抗风险上界，并提出 RS-Pool——利用节点嵌入矩阵的主奇异向量构建图级表示，在不牺牲 clean accuracy 的前提下显著提升对抗鲁棒性。

**[Environment Inference for Learning Generalizable Dynamical System](ai_safety/environment_inference_for_learning_generalizable_dynamical_system.md)**

:   提出 DynaInfer 框架，通过分析固定神经网络的预测误差来推断未标注轨迹的环境标签，实现无环境标签条件下的动态系统泛化学习，在 ODE/PDE 系统上性能匹配甚至超越 Oracle（已知标签）。

**[Evaluating the Promise and Pitfalls of LLMs in Hiring Decisions](ai_safety/evaluating_the_promise_and_pitfalls_of_llms_in_hiring_decisions.md)**

:   在约 10,000 个真实招聘候选人-职位配对上系统评测了 GPT-4o/4.1、Claude 3.5、Gemini 2.5、Llama 3.1/4、DeepSeek R1 等主流 LLM 的招聘匹配表现，发现专用领域模型 Match Score 在准确性（AUC 0.85 vs 0.77）和公平性（种族 IR 0.957 vs ≤0.809）上全面优于通用 LLM。

**[Exploring the Limits of Strong Membership Inference Attacks on Large Language Models](ai_safety/exploring_the_limits_of_strong_membership_inference_attacks_on_large_language_mo.md)**

:   首次将强成员推断攻击（LiRA）扩展到10M~1B参数的GPT-2规模LLM，训练超过4000个参考模型，揭示四个关键发现：强MIA可以在LLM上成功但效果有限（AUC<0.7），且大量个体样本决策在训练随机性下**与抛硬币无法区分**。

**[Factor Decorrelation Enhanced Data Removal from Deep Predictive Models](ai_safety/factor_decorrelation_enhanced_data_removal_from_deep_predictive_models.md)**

:   提出 DecoRemoval 框架，通过判别性保持的因子去相关（基于随机傅里叶特征的空间映射+自适应权重）和平滑损失扰动两大模块，在不重训的前提下实现数据移除，尤其在分布外（OOD）场景下显著优于现有方法。

**[Fair Minimum Labeling: Efficient Temporal Network Activations for Reachability and Equity](ai_safety/fair_minimum_labeling_efficient_temporal_network_activations_for_reachability_an.md)**

:   本文提出公平最小标注（FML）问题，旨在设计最小代价的时序边激活方案，使网络中各节点组均有足够的时序路径可达性以满足公平覆盖要求；证明该问题是 NP-hard 且难以近似，并基于概率树嵌入给出匹配下界的近似算法。

**[Fair Representation Learning With Controllable High Confidence Guarantees Via Ad](ai_safety/fair_representation_learning_with_controllable_high_confidence_guarantees_via_ad.md)**

:   提出 FRG（Fair Representation learning with high-confidence Guarantees），首个允许用户指定公平性阈值 $\varepsilon$ 和置信水平 $1-\delta$ 的公平表征学习框架：通过 VAE 候选选择 + 对抗推断最大化协方差 + Student's t-检验构造高置信上界，保证对**任意**下游模型和任务，$\Delta_{DP} \leq \varepsilon$ 以至少 $1-\delta$ 概率成立。

**[FairContrast: Enhancing Fairness through Contrastive Learning and Customized Augmentation](ai_safety/faircontrast_enhancing_fairness_through_contrastive_learning_and_customized_augm.md)**

:   FairContrast 提出一种面向表格数据的公平对比学习框架，通过策略性的正对样本选择（将优势组有利结果样本与对应弱势组样本配对），结合有监督或自监督对比损失与交叉熵损失的端到端训练，在不引入额外公平约束损失的前提下显著降低了预测偏差，且精度损失极小。

**[Fairness-Regularized Online Optimization with Switching Costs](ai_safety/fairness-regularized_online_optimization_with_switching_costs.md)**

:   提出 FairOBD 算法，首次在平滑在线凸优化中同时处理**长期公平性正则项**和**切换代价**，通过引入辅助变量分解长期公平代价并用镜像下降更新对偶变量，证明了渐近竞争比保证。

**[Fairness under Competition](ai_safety/fairness_under_competition.md)**

:   本文首次研究竞争环境下多个公平分类器的联合公平性问题，理论证明即使每个分类器都满足 Equal Opportunity (EO)，生态系统可能仍然不公平，且对偏差分类器进行公平性调整反而可能降低生态系统公平性。

**[FedFACT: A Provable Framework for Controllable Group-Fairness Calibration in Federated Learning](ai_safety/fedfact_a_provable_framework_for_controllable_group-fairness_calibration_in_fede.md)**

:   提出FedFACT框架，通过刻画联邦学习下的**贝叶斯最优公平分类器**结构，将公平联邦学习分别在训练中（in-processing）化归为**个性化代价敏感学习**、在训练后（post-processing）化归为**双层优化**，首次实现多类别场景下全局公平性与局部公平性的可控协调，并提供收敛及泛化保证。

**[FedRW: Efficient Privacy-Preserving Data Reweighting for Enhancing Federated Learning of Language Models](ai_safety/fedrw_efficient_privacy-preserving_data_reweighting_for_enhancing_federated_lear.md)**

:   FedRW 提出首个无需可信第三方的联邦学习隐私保护软去重框架，通过安全多方计算获取全局样本频率并进行频率感知的样本加权，在预处理上实现最高 28.78× 加速，在模型性能上实现约 11.42% 的 perplexity 改善。

**[FedSVD: Adaptive Orthogonalization for Private Federated Learning with LoRA](ai_safety/fedsvd_adaptive_orthogonalization_for_private_federated_learning_with_lora.md)**

:   FedSVD 提出通过 SVD 对 LoRA 矩阵进行全局重参数化，在每轮通信后用聚合的 BA 乘积的右奇异向量更新 A 矩阵，避免 DP-SGD 下的二次噪声放大同时保持 A 的自适应能力，在多个 NLU 基准上一致超越固定 A 的基线。

**[Flux Efficient Descriptor-Driven Clustered Federated Learning Under Arbitrary Di](ai_safety/flux_efficient_descriptor-driven_clustered_federated_learning_under_arbitrary_di.md)**

:   提出Flux——基于描述符驱动聚类的联邦学习框架，通过提取隐私保护的客户端数据描述符（分布统计量的矩近似）和无监督密度聚类，自动处理四种分布偏移（特征/标签/P(Y|X)/P(X|Y)），在CheXpert医疗数据集上测试时精度比最佳基线高14.6pp。

**[ForensicHub: A Unified Benchmark & Codebase for All-Domain Fake Image Detection and Localization](ai_safety/forensichub_a_unified_benchmark_codebase_for_all-domain_fake_image_detection_and.md)**

:   ForensicHub 提出首个统一所有域（Deepfake/IMDL/AIGC/文档篡改）的假图检测与定位基准平台，包含 4 个任务、23 个数据集、42 个模型、6 个骨干网络和 11 个 GPU 加速评估指标，通过模块化架构和适配器设计打破领域孤岛，并进行了 16 种跨域评估得出 8 条关键洞察。

**[Geo-Sign: Hyperbolic Contrastive Regularisation for Geometrically Aware Sign Language Translation](ai_safety/geo-sign_hyperbolic_contrastive_regularisation_for_geometrically_aware_sign_lang.md)**

:   Geo-Sign 提出将骨架特征投影到 Poincaré 球模型的双曲空间中，通过双曲对比损失正则化 mT5 语言模型，使其感知手语运动的层次结构，仅用骨架数据就在 CSL-Daily 上超越了基于 RGB 的 SOTA 方法（BLEU-4 +1.81, ROUGE-L +3.03）。

**[HealthSLM-Bench: Benchmarking Small Language Models for Mobile and Wearable Healthcare Monitoring](ai_safety/healthslm-bench_benchmarking_small_language_models_for_mobile_and_wearable_healt.md)**

:   首个系统评估小语言模型 (SLMs, 1-4B参数) 在移动与可穿戴健康监测任务上表现的基准，覆盖zero-shot/few-shot/指令微调三种范式，并在iPhone上验证了端侧部署的可行性。

**[Impact of Dataset Properties on Membership Inference Vulnerability of Deep Transfer Learning](ai_safety/impact_of_dataset_properties_on_membership_inference.md)**

:   本文理论推导并实验验证了深度迁移学习中成员推理攻击（MIA）脆弱性与每类样本数之间的幂律关系 $\log(\text{tpr}-\text{fpr}) = -\beta_S \log(S) - \beta_0$，发现增加数据量可降低平均和最坏情况脆弱性，但保护最脆弱样本需要极大量数据。

**[Impact of Dataset Properties on Membership Inference Vulnerability of Deep Transfer Learning](ai_safety/impact_of_dataset_properties_on_membership_inference_vulnerability_of_deep_trans.md)**

:   从理论和实验两方面揭示深度迁移学习中成员推断攻击 (MIA) 脆弱性与每类样本数之间存在幂律关系：随着每类样本数 $S$ 增加，MIA 优势按 $S^{-1/2}$ 下降，但保护最脆弱样本所需的数据量极大，凸显了差分隐私形式化保障的不可替代性。

**[Incentivizing Time-Aware Fairness in Data Sharing](ai_safety/incentivizing_time-aware_fairness_in_data_sharing.md)**

:   提出了一个时间感知的数据共享框架，设计了新的激励机制（F6-F8）和两种奖励方案（时间感知奖励累计和时间感知数据估值），保证早加入协作的参与方能获得更高价值的奖励，同时兼顾公平性和个体理性。

**[Influence Functions for Edge Edits in Non-Convex Graph Neural Networks](ai_safety/influence_functions_for_edge_edits_in_non-convex_graph_neural_networks.md)**

:   提出适用于非凸 GNN 的边编辑影响函数，通过 proximal Bregman 响应函数放松凸性假设，并同时考虑参数偏移和消息传播两方面的影响，支持边的删除和插入。

**[InvisibleInk: High-Utility and Low-Cost Text Generation with Differential Privacy](ai_safety/invisibleink_high-utility_and_low-cost_text_generation_with_differential_privacy.md)**

:   提出 InvisibleInk 框架，通过差分裁剪（DClip）隔离敏感信息和 Top-$k^+$ 截断采样两项创新，将差分隐私长文本生成的计算成本降低 8 倍以上，首次实现不到非隐私生成 4-8 倍开销的高质量隐私文本生成。

**[It's Complicated: The Relationship of Algorithmic Fairness and Non-Discrimination Provisions for High-Risk Systems in the EU AI Act](ai_safety/its_complicated_the_relationship_of_algorithmic_fairness_and_non-discrimination_.md)**

:   系统分析了欧盟 AI 法案（EU AI Act）中高风险系统的非歧视条款与机器学习算法公平性概念之间的关系，指出两者存在显著脱节并提出未来标准化方向。

**[Keep It Real: Challenges in Attacking Compression-Based Adversarial Purification](ai_safety/keep_it_real_challenges_in_attacking_compression-based_adversarial_purification.md)**

:   本文系统评估了基于图像压缩的对抗净化防御，发现重建图像的"真实感"（realism）是提升防御鲁棒性的关键因素——高真实感压缩模型在面对强自适应攻击时仍能保持显著鲁棒性，而这并非源于梯度掩蔽。

**[LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory](ai_safety/llm_strategic_reasoning_agentic_study_through_behavioral_gam.md)**

:   论文不再把大模型战略推理简单等同于“是否接近纳什均衡”，而是基于 behavioral game theory 构建评测框架，区分真实推理能力与上下文因素，系统测评 22 个 LLM 的互动决策行为，发现模型规模并不决定战略水平，CoT 提升也并非普遍有效，同时暴露出显著的人口属性偏置。

**[Locally Optimal Private Sampling: Beyond the Global Minimax](ai_safety/locally_optimal_private_sampling_beyond_the_global_minimax.md)**

:   在本地差分隐私（LDP）下的采样问题中，提出**局部minimax**框架，利用公共数据分布 $P_0$ 定义的邻域约束，推导出闭式最优采样器，在理论和实验上均**一致优于全局minimax采样器**。

**[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](ai_safety/machine_unlearning_doesnt_do_what_you_think_lessons_for_generative_ai_policy_and.md)**

:   系统性论证"机器遗忘"（machine unlearning）并非万能方案，识别出遗忘动机与可行实现之间的五大根本错配（mismatches），为 ML 研究者和政策制定者提供严谨的分析框架。

**[Matchings Under Biased and Correlated Evaluations](ai_safety/matchings_under_biased_and_correlated_evaluations.md)**

:   在两机构稳定匹配模型中引入评估相关性参数 $\gamma$（机构间评分的对齐程度），分析偏差 $\beta$ 和相关性 $\gamma$ 如何联合影响弱势群体的代表性比率，证明即使轻微的相关性损失也可导致代表性急剧下降，并提出公平性干预策略的 Pareto 前沿。

**[Mitigating Privacy-Utility Trade-off in Decentralized Federated Learning via f-Differential Privacy](ai_safety/mitigating_privacy-utility_trade-off_in_decentralized_federated_learning_via_f-d.md)**

:   提出基于 f-DP 框架的两种去中心化联邦学习隐私记账方法——PN-f-DP 和 Sec-f-LDP，通过更精细的假设检验隐私度量，一致性地获得比 Rényi DP 更紧的隐私界，从而在相同隐私保证下减少噪声注入、提升模型效用。

**[Nearly-Linear Time Private Hypothesis Selection with the Optimal Approximation Factor](ai_safety/nearly-linear_time_private_hypothesis_selection_with_the_optimal_approximation_f.md)**

:   首次提出在中心差分隐私模型下同时实现近线性时间复杂度和最优近似因子 $\alpha=3$ 的假设选择算法，解决了Bun等人（NeurIPS 2019）提出的开放问题。

**[OmniFC: Rethinking Federated Clustering via Lossless and Secure Distance Reconstruction](ai_safety/omnifc_rethinking_federated_clustering_via_lossless_and_secure_distance_reconstr.md)**

:   提出 OmniFC，一个模型无关的联邦聚类框架：通过 Lagrange 编码计算在有限域上精确重建全局成对距离矩阵，任意集中式聚类方法（K-Means/谱聚类/DBSCAN/层次聚类等）可直接在其上运行，仅需一轮通信，天然抵抗 Non-IID，在 7 个数据集上全面超越 k-FED/MUFC/FedSC 等专用方法。

**[On the Hardness of Conditional Independence Testing In Practice](ai_safety/on_the_hardness_of_conditional_independence_testing_in_practice.md)**

:   系统分析了基于核的条件独立性（CI）检验在实践中失败的根本原因：条件均值嵌入的估计误差是导致Type-I错误膨胀的核心因素，同时揭示了选择条件核$k_C$对检验功效至关重要但会加剧假阳性的内在张力。

**[On the Robustness of Verbal Confidence of LLMs in Adversarial Attacks](ai_safety/on_the_robustness_of_verbal_confidence_of_llms_in_adversarial_attacks.md)**

:   首次系统研究 LLM 语言化置信度（verbal confidence）在对抗攻击下的鲁棒性，提出基于扰动和越狱的攻击框架，揭示攻击可导致置信度下降最高 30%、答案翻转率高达 100%，且现有防御策略基本无效。

**[On the Sample Complexity of Differentially Private Policy Optimization](ai_safety/on_the_sample_complexity_of_differentially_private_policy_optimization.md)**

:   首次系统性研究差分隐私（DP）约束下策略优化的样本复杂度，提出统一的元算法框架，分析DP-PG、DP-NPG和DP-REBEL三种隐私策略优化算法，证明隐私代价通常仅作为样本复杂度的低阶项出现。

**[Provable Watermarking for Data Poisoning Attacks](ai_safety/provable_watermarking_for_data_poisoning_attacks.md)**

:   本文提出两种可证明的水印方案（后投毒水印和投毒并行水印），为数据投毒攻击提供透明性声明机制，理论证明在特定水印长度条件下可同时保证水印可检测性和投毒有效性。

**[Reconstruction and Secrecy under Approximate Distance Queries](ai_safety/reconstruction_and_secrecy_under_approximate_distance_queries.md)**

:   在近似距离查询模型下，通过学习理论视角研究重建博弈（reconstruction game），证明了最优重建误差等于Chebyshev半径的几何特征刻画，并对欧氏凸空间的伪有限性给出了完整分类。

**[The Unseen Threat Residual Knowledge In Machine Unlearning Under Perturbed Sampl](ai_safety/the_unseen_threat_residual_knowledge_in_machine_unlearning_under_perturbed_sampl.md)**

:   发现机器遗忘的关键安全漏洞：即使遗忘后的模型在统计意义上与重训练模型不可区分，对遗忘样本施加微小对抗扰动后，遗忘模型仍能正确识别而重训练模型则失败——揭示了"残余知识"这一新型隐私风险。提出 RURK 微调策略，通过惩罚对扰动遗忘样本的正确预测来消除残余知识，在 CIFAR-10 和 ImageNet-100 上有效抑制 11 种遗忘方法的残余知识。

**[Understanding and Improving Adversarial Robustness of Neural Probabilistic Circuits](ai_safety/understanding_and_improving_adversarial_robustness_of_neural_probabilistic_circu.md)**

:   理论分析神经概率电路（NPC）的对抗鲁棒性仅取决于属性识别模型而与概率电路无关，并提出 RNPC 通过类级推理集成方式实现可证明的鲁棒性提升，在保持良性准确率的同时显著增强对抗鲁棒性。

---

## 📐 优化/理论 { #optimization }

**[A Single-Loop First-Order Algorithm for Linearly Constrained Bilevel Optimization](optimization/a_single-loop_first-order_algorithm_for_linearly_constrained_bilevel_optimizatio.md)**

:   针对下层问题带耦合线性约束的双层优化问题，提出单循环一阶算法 SFLCB，通过罚函数 + 增广拉格朗日重构消除 Hessian 依赖，将迭代复杂度从 $O(\epsilon^{-3}\log(\epsilon^{-1}))$ 改进至 $O(\epsilon^{-3})$。

**[A Theoretical Study on Bridging Internal Probability and Self-Consistency for LLM Reasoning](optimization/a_theoretical_study_on_bridging_internal_probability_and_sel.md)**

:   提出首个针对基于采样的测试时缩放方法的理论框架，将推理误差分解为估计误差和模型误差，揭示了Self-Consistency收敛慢、Perplexity模型误差大的局限，并提出RPC方法融合两者优势，在7个基准上以50%的采样成本达到同等推理性能。

**[A Unified Approach to Submodular Maximization Under Noise](optimization/a_unified_approach_to_submodular_maximization_under_noise.md)**

:   本文提出一个统一的元算法框架，可以将任何满足"鲁棒性"条件的精确子模最大化算法作为黑盒，自动转换为在持久噪声值预言机下保持近似比的算法，首次覆盖了非单调子模函数的拟阵约束和无约束情形。

**[A Unified Stability Analysis of SAM vs SGD: Role of Data Coherence and Emergence of Simplicity Bias](optimization/a_unified_stability_analysis_of_sam_vs_sgd_role_of_data_cohe.md)**

:   通过线性稳定性分析框架，证明了"平坦极小值⇒好泛化"和"SGD偏好简单函数"是同一枚硬币的两面——数据一致性(coherence)同时控制着两者，且SAM通过更严格的稳定性条件进一步放大了简单性偏好。

**[Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization](optimization/adaptive_algorithms_with_sharp_convergence_rates_for_stochas.md)**

:   首次为随机层次化优化（极小极大和双层优化）提供自适应且sharp的收敛保证，通过动量归一化技术和新型自适应参数选择，在无需事先知道噪声大小的情况下实现最优收敛率Õ(1/√T + √σ̄/T^{1/4})。

**[An Adaptive Algorithm for Bilevel Optimization on Riemannian Manifolds](optimization/an_adaptive_algorithm_for_bilevel_optimization_on_riemannian_manifolds.md)**

:   AdaRHD 是首个无需预知问题参数（强凸常数、Lipschitz 界、流形曲率）的黎曼双层优化自适应算法——通过逆累计梯度范数策略自适应选择步长，在三阶段框架中逐步求解下层问题/线性系统/上层更新，收敛速率 $O(1/\epsilon)$ 匹配非自适应方法，对初始步长选择鲁棒性远超 RHGD。

**[Asymptotically Stable Quaternionic Hopfield Structured Neural Network with Supervised Projection-based Manifold Learning](optimization/asymptotically_stable_quaternion-valued_hopfield-structured_neural_network_with_.md)**

:   提出四元数值监督学习 Hopfield 结构神经网络 (QSHNN)，通过周期性投影策略保持权重矩阵的四元数结构一致性，并基于 Lyapunov 理论证明了不动点的存在唯一性和渐近稳定性，轨迹曲率有界保证机器人路径规划的平滑性。

**[Auto-Compressing Networks](optimization/auto-compressing_networks.md)**

:   Auto-Compressing Networks（ACN）用长程前向连接（所有层输出直接汇聚到最终输出）替代短残差连接，使得梯度的 Direct Gradient 成分远强于 Forward Gradient，隐式地将信息压缩到早期层——ViT 仅需 6 层达到标准 12 层性能，BERT 节省 75% 层数，还额外获得噪声鲁棒性（+6.4%）和持续学习抗遗忘（-18%）。

**[AutoOpt: A Dataset and a Unified Framework for Automating Optimization Problem Solving](optimization/autoopt_a_dataset_and_a_unified_framework_for_automating_optimization_problem_so.md)**

:   AutoOpt 构建了首个优化问题图像到代码的端到端框架——11554 张优化公式图像（手写+印刷）的 AutoOpt-11k 数据集 + M1 混合编码器（ResNet+Swin→mBART）图像转 LaTeX（BLEU 96.70）+ M2 DeepSeek-Coder LaTeX 转 PYOMO + M3 双层分解求解器，框架级成功率 94.20%。

**[Better NTK Conditioning: A Free Lunch from ReLU Nonlinear Activation in Wide Neural Networks](optimization/better_ntk_conditioning_a_free_lunch_from_relu_nonlinear_activation_in_wide_neur.md)**

:   证明 ReLU 激活函数对宽神经网络有一个此前未被注意的"免费"益处：(a) 在模型梯度特征空间中产生更好的数据分离（相似输入的角度在梯度空间中被放大），(b) 由此导致 NTK 矩阵条件数严格减小（相比线性网络）。深度进一步放大此效应——在无限宽然后无限深的极限下，所有数据对在梯度空间中等角分离（~75.5°），NTK 条件数收敛到仅依赖数据量 $n$ 的固定值 $(n+4)/3$。

**[Brain-like Variational Inference](optimization/brain-like_variational_inference.md)**

:   提出 FOND 框架（Free energy Online Natural-gradient Dynamics），从自由能最小化的第一原理推导出脉冲神经网络推断动力学，并实现 iPVAE（迭代泊松 VAE），在重建-稀疏性权衡、生物合理性和 OOD 泛化上优于标准 VAE 和预测编码模型。

**[Composing Global Solutions to Reasoning Tasks via Algebraic Objects in Neural Nets](optimization/composing_global_solutions_to_reasoning_tasks_via_algebraic_objects_in_neural_ne.md)**

:   提出 CoGS 框架，证明二层二次激活网络在 Abelian 群乘法推理任务上的权重空间具有半环代数结构，损失函数中的 Sum Potential 是环同态映射，由此可从仅满足部分损失的局部解通过环加法和环乘法代数地组合出全局最优解，约 95% 的梯度下降解与理论构造精确匹配。

**[Composing Global Solutions to Reasoning Tasks via Algebraic Objects in Neural Nets](optimization/constrained_network_slice_assignment_via_large_language_models.md)**

:   揭示两层二次激活网络在 Abelian 群推理任务上训练时权重空间具有半环代数结构，提出 CoGS 框架通过环运算将部分解组合为全局最优解，约 95% 梯度下降解与理论构造精确匹配。

**[Contribution of Task-Irrelevant Stimuli to Drift of Neural Representations](optimization/contribution_of_task-irrelevant_stimuli_to_drift_of_neural_representations.md)**

:   理论证明在线学习中任务无关刺激的统计特性（方差和维度）是表示漂移的重要驱动因素，在 Oja 规则、Similarity Matching、自编码器和监督两层网络中均观察到漂移率 $D \propto \lambda_\perp^2 (n-m)$，且学习噪声诱导的漂移具有各向异性几何特征，与高斯突触噪声的各向同性漂移定性不同。

**[Covariances for Free: Exploiting Mean Distributions for Training-free Federated Learning](optimization/covariances_for_free_exploiting_mean_distributions_for_training-free_federated_l.md)**

:   提出 FedCOF，仅利用客户端上传的类均值（class means）即可在服务器端无偏估计类协方差矩阵，从而在零训练、极低通信开销的条件下初始化全局分类器，性能媲美甚至超越需要传输二阶统计量的 Fed3R。

**[DartQuant: Efficient Rotational Distribution Calibration for LLM Quantization](optimization/dartquant_efficient_rotational_distribution_calibration_for_llm_quantization.md)**

:   DartQuant 提出基于分布校准的旋转矩阵优化方法，通过 Whip 损失将激活值分布推向均匀分布以减少量化误差，并用 QR-Orth 替代昂贵的流形优化器，在 70B 模型上实现 47× 加速和 10× 内存节省，首次在单张 3090 GPU 上完成大模型旋转校准。

**[Deep Taxonomic Networks for Unsupervised Hierarchical Prototype Discovery](optimization/deep_taxonomic_networks_for_unsupervised_hierarchical_prototype_discovery.md)**

:   Deep Taxonomic Networks 提出一种基于完全二叉树混合高斯先验的深度潜变量模型，通过变分推断自动从无标签数据中发现层次化分类体系和各级原型聚类，无需预设类别数量，并在多个数据集上大幅超越 TreeVAE 等基线。

**[Do Neural Networks Need Gradient Descent to Generalize? A Theoretical Study](optimization/do_neural_networks_need_gradient_descent_to_generalize_a_theoretical_study.md)**

:   本文在矩阵分解（神经网络理论的经典测试平台）上证明了 Guess & Check（随机抽参数直到拟合训练集）的泛化能力随宽度增加而退化（首次证明存在 G&C 可证明劣于梯度下降的典范情况），但随深度增加而改善，揭示了宽度和深度对泛化的截然不同作用。

**[Doubly Robust Alignment for Large Language Models](optimization/doubly_robust_alignment_for_large_language_models.md)**

:   DRPO 借鉴因果推断中的双重稳健估计方法，提出一种偏好优化算法，当偏好模型或参考策略任一正确指定时即可保持一致性，在理论和实验上均优于 PPO/DPO 及其变体。

**[DynaAct: Large Language Model Reasoning with Dynamic Action Spaces](optimization/dynaact_large_language_model_reasoning_with_dynamic_action_spaces.md)**

:   DynaAct 将 LLM 推理中的动作空间构建建模为子集选择问题，通过兼顾效用和多样性的子模函数在每步动态构建紧凑动作空间，在 6 个基准上显著优于 rStar、RAP 等方法，MATH-500 上比 rStar 高 6.8%。

**[Effective Policy Learning for Multi-Agent Online Coordination Beyond Submodular Objectives](optimization/effective_policy_learning_for_multi-agent_online_coordination_beyond_submodular_.md)**

:   提出 MA-SPL 和 MA-MPL 两个多智能体在线协调算法，通过"基于策略的连续扩展"技术突破次模性限制，首次在次模和弱次模目标函数上均实现最优 $(1 - c/e)$ 近似比，支持时变目标和仅局部反馈的实际约束。

**[Efficient Adaptive Federated Optimization](optimization/efficient_adaptive_federated_optimization.md)**

:   FedAda2/FedAda2++ 提出在联邦学习中实现高效的服务器-客户端联合自适应优化：客户端本地预条件器从零初始化（无需服务器传输），并可选地用 SM3 等内存高效优化器压缩本地统计量，在理论上保持与完整联合自适应相同的 $O(T^{-1/2})$ 收敛率，实测通信成本与 FedAvg 一致。

**[Efficient Federated Learning against Byzantine Attacks and Data Heterogeneity via Aggregating Normalized Gradients](optimization/efficient_federated_learning_against_byzantine_attacks_and_data_heterogeneity_vi.md)**

:   提出 Fed-NGA 算法，通过对客户端上传的梯度做归一化后加权平均来实现聚合，以 $\mathcal{O}(pM)$ 的极低时间复杂度同时抵御 Byzantine 攻击与数据异质性，并在非凸损失函数下首次证明了特定温和条件下的零最优性间隙收敛。

**[Emergence and Scaling Laws in SGD Learning of Shallow Neural Networks](optimization/emergence_and_scaling_laws_in_sgd_learning_of_shallow_neural_networks.md)**

:   本文对浅层神经网络在线 SGD 学习加法模型（多个单指标函数叠加）的过程进行了精确分析，证明了每个教师神经元的学习呈现尖锐相变（emergence），而大量相变曲线的叠加自然产生平滑的幂律 scaling law。

**[Escaping Saddle Points without Lipschitz Smoothness: The Power of Nonlinear Preconditioning](optimization/escaping_saddle_points_without_lipschitz_smoothness_the_power_of_nonlinear_preco.md)**

:   本文提出统一的充分条件连接 $(L_0,L_1)$-光滑性与各向异性光滑性两种广义光滑框架，证明非线性预条件梯度法（含梯度裁剪）在此放松条件下保持鞍点规避性质，并给出扰动变体以多项对数维数依赖达到二阶稳定点。

**[Evaluating LLMs for Combinatorial Optimization: One-Phase and Two-Phase Heuristics for 2D Bin-Packing](optimization/evaluating_llms_for_combinatorial_optimization_one-phase_and_two-phase_heuristic.md)**

:   本文提出一个结合 LLM 与进化算法的系统性评估框架，用于评估 LLM 在 2D 装箱问题上生成和优化启发式算法的能力，GPT-4o 在 2 轮迭代内即达到最优解，将平均箱数从 16 降至 15，空间利用率从 0.76-0.78 提升至 0.83。

**[Exact and Linear Convergence for Federated Learning under Arbitrary Client Participation is Attainable](optimization/exact_and_linear_convergence_for_federated_learning_under_arbitrary_client_parti.md)**

:   本文引入随机矩阵和时变图作为建模工具，将联邦学习的客户端参与和本地更新过程统一为矩阵乘法形式，并提出 FOCUS 算法（基于 push-pull 策略），在**任意客户端参与**和数据异构下首次实现精确收敛与线性收敛速率。

**[Exploring Landscapes for Better Minima along Valleys](optimization/exploring_landscapes_for_better_minima_along_valleys.md)**

:   本文提出优化器适配器"E"，通过在梯度更新中加入梯度差分的指数移动平均 $\mathbf{a}_k = \text{EMA}(\mathbf{g}_k - \mathbf{g}_{k-1})$ 使优化器能在到达局部极小值后继续沿损失景观的"山谷"探索更低更平坦的极小值，适配后的 ALTO 在大批量训练中平均提升 2.5% 测试准确率。

**[Extragradient Method for $(L_0, L_1)$-Lipschitz Root-finding Problems](optimization/extragradient_method_for_l_0_l_1-lipschitz_root-finding_problems.md)**

:   本文在 $\alpha$-对称 $(L_0,L_1)$-Lipschitz 条件下（放松经典 $L$-Lipschitz 假设）为 extragradient (EG) 方法提出自适应步长策略 $\gamma_k = 1/(c_0 + c_1\|F(x_k)\|^\alpha)$，建立了强单调（线性收敛）、单调（次线性收敛）和 weak Minty（局部收敛）三类根问题的首个完整收敛保证。

**[FedRTS: Federated Robust Pruning via Combinatorial Thompson Sampling](optimization/fedrts_federated_robust_pruning_via_combinatorial_thompson_sampling.md)**

:   将联邦动态剪枝重新建模为组合多臂赌博机(CMAB)问题，提出基于 Thompson Sampling 的拓扑调整机制 TSAdj，通过概率性决策替代确定性决策来获得更鲁棒的稀疏模型拓扑，同时显著降低通信开销。

**[Finite-Time Analysis of Stochastic Nonconvex Nonsmooth Optimization on the Riemannian Manifolds](optimization/finite-time_analysis_of_stochastic_nonconvex_nonsmooth_optimization_on_the_riema.md)**

:   提出 Riemannian Online to NonConvex (RO2NC) 算法及其零阶版本 ZO-RO2NC，首次为黎曼流形上完全非光滑非凸随机优化建立了 $O(\delta^{-1}\epsilon^{-3})$ 的有限时间样本复杂度保证，匹配欧几里德最优结果。

**[From Average-Iterate to Last-Iterate Convergence in Games: A Reduction and Its Applications](optimization/from_average-iterate_to_last-iterate_convergence_in_games_a_reduction_and_its_ap.md)**

:   提出 A2L (Average to Last-iterate) 黑箱规约，对效用函数关于自身策略和对手联合策略均线性的博弈，能将任意非耦合学习动力学的平均迭代转换为新动力学的末迭代，由此在多人零和多矩阵博弈中取得 $O(\log d / T)$ 梯度反馈和 $\tilde{O}(d^{1/5}T^{-1/5})$ bandit 反馈的 SOTA last-iterate 收敛率。

**[From Information to Generative Exponent: Learning Rate Induces Phase Transitions in SGD](optimization/from_information_to_generative_exponent_learning_rate_induces_phase_transitions_.md)**

:   系统刻画了在学习高斯单指标模型时，学习率如何在"information exponent 主导"和"generative exponent 主导"两个样本复杂度体制之间引发相变，并提出了一种新的逐层交替 SGD 算法，无需复用样本即可突破 CSQ 下界。

**[From Linear to Nonlinear: Provable Weak-to-Strong Generalization through Feature Learning](optimization/from_linear_to_nonlinear_provable_weak-to-strong_generalization_through_feature_.md)**

:   本文首次在非线性特征学习设定（线性 CNN → 两层 ReLU CNN）下严格分析了 weak-to-strong 泛化现象，揭示了数据匮乏和数据丰富两种机制下的不同行为：前者通过良性过拟合实现泛化（或因有害过拟合失败），后者通过早停的标签纠正实现泛化（但过训练会退化）。

**[Functional Scaling Laws in Kernel Regression: Loss Dynamics and Learning Rate Schedules](optimization/functional_scaling_laws_in_kernel_regression_loss_dynamics_and_learning_rate_sch.md)**

:   在幂律核回归模型中建立了 Functional Scaling Law (FSL)，通过引入"内在时间"概念统一刻画任意学习率调度下的完整 loss 轨迹，并推导出常数/指数衰减/WSD 三种调度在数据受限和计算受限条件下的显式 scaling 关系，理论解释了 WSD 优于纯衰减的经验现象。

**[Generalization or Hallucination? Understanding Out-of-Context Reasoning in Transformers](optimization/generalization_or_hallucination_understanding_out-of-context_reasoning_in_transf.md)**

:   本文论证 LLM 的泛化能力和幻觉产生源于同一机制——脱语境推理（OCR），并在单层注意力模型上理论证明：分解参数化 $(W_O, W_V)$ 因梯度下降的核范数隐式偏差而能执行 OCR，而合并参数化 $W_{OV}$ 因 Frobenius 范数偏差而不能，且 OCR 是样本高效的（仅需 $m_{\text{train}}>0$）。

**[Gradient Descent As Loss Landscape Navigation A Normative Framework For Deriving](optimization/gradient_descent_as_loss_landscape_navigation_a_normative_framework_for_deriving.md)**

:   提出统一框架将各种学习规则（momentum、Adam、自然梯度等）推导为损失景观上的最优导航策略，不同度量和目标自然导出不同的优化器。

**[Implicit Bias of Spectral Descent and Muon on Multiclass Separable Data](optimization/implicit_bias_of_spectral_descent_and_muon_on_multiclass_separable_data.md)**

:   本文首次完整刻画了归一化最速下降（NSD）和归一化动量最速下降（NMD）在多分类线性可分数据上的隐式偏差：这些算法以 $\mathcal{O}(1/\sqrt{t})$ 的速率收敛到相应 $p$-范数的最大 margin 解，涵盖 Spectral Descent（谱范数）和 Muon 作为特例，并扩展至 Adam（max-范数 margin）。

**[Improving the Straight-Through Estimator with Zeroth-Order Information](optimization/improving_the_straight-through_estimator_with_zeroth-order_information.md)**

:   本文提出 FOGZO（First-Order-Guided Zeroth-Order Gradient Descent），将 STE 梯度作为偏置源注入零阶梯度估计中，在保留 STE 的计算效率的同时利用零阶信息纠正 STE 的偶发错误方向，仅多 2 次前向传播即在 DeiT、ResNet、LLaMA 上实现 1-22 点的精度/困惑度改善。

**[In Search of Adam's Secret Sauce](optimization/in_search_of_adams_secret_sauce.md)**

:   本文通过训练 1500+ 语言模型的大规模实验发现：(1) Signum 虽能缩小 96% 的 SGD-Adam 差距，但仍比 Adam 慢 25%；(2) 设 $\beta_1 = \beta_2$ 是 Adam 的近最优简化；(3) 在 $\beta_1 = \beta_2 = \beta$ 下 Adam 可被重新解读为基于在线高斯变分推断估计梯度均值和方差的信噪比自适应 Signum。

**[Isotropic Noise in Stochastic and Quantum Convex Optimization](optimization/isotropic_noise_in_stochastic_and_quantum_convex_optimization.md)**

:   本文引入各向同性随机梯度预言机（ISGO）概念——噪声在每个方向上都以高概率有界——并设计随机切平面算法达到 $\tilde{O}(R^2\sigma_I^2/\epsilon^2 + d)$ 的查询复杂度，较 SGD 在某些参数区间改进 $d$ 倍，作为推论获得了 sub-exponential 噪声下的新 SOTA 复杂度，并通过量子各向同性化子程序改进了量子随机凸优化的维度依赖。

**[Kernel Learning with Adversarial Features: Numerical Efficiency and Adaptive Regularization](optimization/kernel_learning_with_adversarial_features_numerical_efficiency_and_adaptive_regu.md)**

:   提出在再生核希尔伯特空间（RKHS）中将对抗扰动从输入空间转移到特征空间的新范式，使内层最大化可精确求解，并通过迭代加权核岭回归高效优化，同时自适应正则化无需调参即可匹配交叉验证性能。

**[Large Language Bayes](optimization/large_language_bayes.md)**

:   将 LLM 和概率编程语言（PPL/Stan）数学地"胶合"成联合分布 $p(z,x,m|t) = p(m|t)_{\text{LLM}} \cdot p(z,x|m)_{\text{PPL}}$，用户只需提供非形式化的问题描述和数据，系统自动从 LLM 采样候选形式模型、做贝叶斯推断、通过边际似然加权平均，无需用户编写概率模型。

**[Large Stepsizes Accelerate Gradient Descent for Regularized Logistic Regression](optimization/large_stepsizes_accelerate_gradient_descent_for_regularized_logistic_regression.md)**

:   证明了在线性可分数据上对 $\ell_2$ 正则化逻辑回归使用大步长 GD（进入 Edge of Stability 区间），可将步复杂度从经典的 $\widetilde{O}(\kappa)$ 加速到 $\widetilde{O}(\sqrt{\kappa})$，在小正则化下匹配 Nesterov 动量的加速率。

**[Layer-wise Update Aggregation with Recycling for Communication-Efficient Federated Learning](optimization/layer-wise_update_aggregation_with_recycling_for_communication-efficient_federat.md)**

:   提出 FedLUAR：基于梯度-权重比的层级优先级度量选择低优先级层复用上一轮梯度（而非丢弃），在仅 17% 通信开销下保持与 FedAvg 几乎相同的精度。

**[Learning at the Speed of Physics: Equilibrium Propagation on Oscillator Ising Machines](optimization/learning_at_the_speed_of_physics_equilibrium_propagation_on_oscillator_ising_mac.md)**

:   首次将 Equilibrium Propagation（EP）完整映射到振荡器 Ising Machine（OIM）硬件上，利用 GHz 物理动力学实现无反向传播的局部学习，在 MNIST/Fashion-MNIST 上达到 97.2%/88.0% 精度，并展示在参数量化和噪声下的鲁棒性。

**[Learning from Interval Targets](optimization/learning_from_interval_targets.md)**

:   研究仅有区间标签（上下界）的回归问题，建立了基于假设类平滑性的非渐进泛化界（不依赖小 ambiguity degree 假设），并提出 minmax 学习框架利用平滑约束限制最坏情况标签，在 18 个真实数据集上显著优于无约束方法。

**[Learning Orthogonal Multi-Index Models A Fine-Grained Information Exponent Analy](optimization/learning_orthogonal_multi-index_models_a_fine-grained_information_exponent_analy.md)**

:   证明正交多索引模型 $f_*(\mathbf{x}) = \sum_{k=1}^P \phi(\mathbf{v}_k^* \cdot \mathbf{x})$ 可通过两阶段在线 SGD 以 $\tilde{O}(dP^{L-1})$ 样本复杂度学习（$L$ 为链接函数最低高阶 Hermite 阶），远优于仅用最低阶信息的 $\tilde{O}(Pd^{L-1})$——关键在于先用 2 阶项恢复子空间，再用 $L$ 阶项恢复方向，联合利用不同阶的 Hermite 分量。

**[Learning Parameterized Skills from Demonstrations](optimization/learning_parameterized_skills_from_demonstrations.md)**

:   提出 DEPS，一种端到端从专家示范中发现参数化技能的算法，通过三层层次策略（离散技能选择→连续参数选择→底层动作）和信息瓶颈设计，学习可解释且可泛化的技能抽象，在LIBERO和MetaWorld上显著优于基线。

**[Learning Provably Improves the Convergence of Gradient Descent](optimization/learning_provably_improves_the_convergence_of_gradient_descent.md)**

:   首次严格证明了基于unrolling的Learn to Optimize (L2O)框架（Math-L2O）的训练收敛性，利用NTK理论建立了线性收敛速率，并提出确定性初始化策略确保L2O可证明地改善梯度下降算法的收敛性能，实验验证相比标准GD提升超50%的最优性。

**[Learning Reconfigurable Representations for Multimodal Federated Learning with Missing Data](optimization/learning_reconfigurable_representations_for_multimodal_federated_learning_with_m.md)**

:   提出 PEPSY 框架，通过学习客户端侧的嵌入控制来编码数据缺失模式，将全局聚合表示重新配置为适应各客户端本地上下文的数据完整特征，在多模态联邦学习中处理模态缺失和特征缺失两类问题。

**[Learning Single-Index Models via Harmonic Decomposition](optimization/learning_single-index_models_via_harmonic_decomposition.md)**

:   提出以球谐函数（spherical harmonics）代替 Hermite 多项式作为单指标模型（SIM）的自然基底，利用旋转对称性刻画任意球对称输入分布下学习 SIM 的样本与计算复杂度，构造了两族最优估计器（张量展开 + 在线 SGD），并揭示了高斯情形之外出现的样本-运行时间权衡现象。

**[Learning Sparse Approximate Inverse Preconditioners for Conjugate Gradient Solvers on GPUs](optimization/learning_sparse_approximate_inverse_preconditioners_for_conjugate_gradient_solve.md)**

:   提出一种基于图神经网络（GNN）的稀疏近似逆（SPAI）预条件子学习方法，利用 SPAI 的局部性与 GNN 消息传递的天然兼容性，并引入尺度不变损失函数（SAI loss），在 GPU 上实现 40%-53% 的求解时间缩减（68%-113% 加速）。

**[Learning Theory for Kernel Bilevel Optimization](optimization/learning_theory_for_kernel_bilevel_optimization.md)**

:   首次为核双层优化（KBO）建立了有限样本泛化界，证明目标函数值和梯度的插入估计误差均以$\mathcal{O}(1/\sqrt{m}+1/\sqrt{n})$的参数速率一致收敛，并将该理论应用于双层梯度下降算法的统计精度分析。

**[Learning to Insert for Constructive Neural Vehicle Routing Solver](optimization/learning_to_insert_for_constructive_neural_vehicle_routing_solver.md)**

:   提出 L2C-Insert，首个基于学习的插入式构造范式用于神经组合优化，通过允许在部分解的任意合法位置插入节点（而非仅追加到末尾），显著提升 TSP/CVRP 的构造质量和灵活性。

**[MDNS: Masked Diffusion Neural Sampler via Stochastic Optimal Control](optimization/mdns_masked_diffusion_neural_sampler_via_stochastic_optimal_control.md)**

:   提出 Masked Diffusion Neural Sampler (MDNS)，基于连续时间马尔可夫链（CTMC）的随机最优控制理论，通过对齐路径测度来训练离散神经采样器，在状态空间基数高达 $10^{122}$ 的 Ising/Potts 模型上准确采样，大幅超越现有学习型基线。

**[Memory-Augmented Potential Field Theory: A Framework for Adaptive Control in Non-Convex Domains](optimization/memory-augmented_potential_field_theory_a_framework_for_adaptive_control_in_non-.md)**

:   提出记忆增强势场理论（MAPFT），在随机最优控制中维护一个动态记忆模块来检测并编码状态空间的拓扑特征（局部最小值、低梯度区等），通过动态修改价值函数景观实现非凸环境下的自适应控制，在 Humanoid-v4 等任务上比最优 RL 方法（SAC）提升 27% 累积奖励，且局部最优逃逸率从 ~30% 提升到 ~72%。

**[MESS+: Dynamically Learned Inference-Time LLM Routing in Model Zoos with Service Level Guarantees](optimization/mess_dynamically_learned_inference-time_llm_routing_in_model_zoos_with_service_l.md)**

:   MESS+是首个成本最优的LLM路由框架，通过在线学习请求满足度预测和虚拟队列约束，动态选择模型同时保证SLA合规，相比现有方法实现平均2倍成本节省。

**[Online Two-Stage Submodular Maximization](optimization/online_two-stage_submodular_maximization.md)**

:   首次提出在线两阶段子模最大化（O2SSM）问题，针对加权阈值势函数（WTP）设计了 RAOCO 算法，通过分数松弛+随机管道舍入实现多项式时间运行下的次线性 $(1-1/e)^2$-regret 保证，同时改进了离线问题的近似比。

**[Optimality and NP-Hardness of Transformers in Learning Markovian Dynamical Functions](optimization/optimality_and_np-hardness_of_transformers_in_learning_markovian_dynamical_funct.md)**

:   从优化理论角度分析 Transformer 学习马尔可夫动态函数的 ICL 能力：推导单层线性自注意力的全局最优解（闭式表达），证明从扩展参数空间恢复 Transformer 参数是 NP-hard 的，并揭示多层 LSA 等价于预条件多目标优化。

**[Optimistic Online-to-Batch Conversions for Accelerated Convergence and Universality](optimization/optimistic_online-to-batch_conversions_for_accelerated_convergence_and_universal.md)**

:   提出乐观在线到批量（O2B）转换框架，将乐观性从在线算法中释放到转换机制本身，使简单的在线梯度下降就能实现 $O(T^{-2})$ 加速收敛率，并首次通过 O2B 转换实现强凸光滑目标的最优收敛，同时达到对光滑性的通用性。

**[Quantitative Convergence of Trained Single Layer Neural Networks to Gaussian Processes](optimization/quantitative_convergence_of_trained_single_layer_neural_networks_to_gaussian_pro.md)**

:   为梯度下降训练的浅层神经网络提供了在任意正训练时间 $t \geq 0$ 下向高斯过程收敛的显式定量上界，证明了二次Wasserstein距离以 $O(\log n_1 / n_1)$ 的速率多项式衰减。

**[Streaming Federated Learning with Markovian Data](optimization/streaming_federated_learning_with_markovian_data.md)**

:   首次严格分析了非凸目标函数下具有马尔可夫数据流的流式联邦学习，证明 Minibatch SGD、Local SGD 和 Local SGD-M 均能实现与客户端数成反比的样本复杂度（线性加速），且 Local SGD-M 无需异质性假设即可匹配 Minibatch SGD 的通信复杂度。

**[Understanding the Generalization of Stochastic Gradient Adam in Learning Neural Networks](optimization/understanding_the_generalization_of_stochastic_gradient_adam_in_learning_neural_.md)**

:   首次理论分析 mini-batch Adam 的泛化行为，证明大 batch Adam/AdamW 即使带 weight decay 也收敛到高测试误差的解，而小 batch 版本通过随机梯度的隐式正则化 + weight decay 的显式正则化可实现近零测试误差，且 Adam 的有效 weight decay 上界严格小于 AdamW。

**[Unveiling the Power of Multiple Gossip Steps: A Stability-Based Generalization Analysis in Decentralized Training](optimization/unveiling_the_power_of_multiple_gossip_steps_a_stability-based_generalization_an.md)**

:   本文首次从算法稳定性角度分析去中心化 SGD（DSGD）中多步 Gossip 通信（MGS）的泛化效果，证明 MGS 以指数速率减少优化误差从而收紧泛化界，但即使 Gossip 步数趋于无穷也无法完全弥合与中心化训练的泛化差距。

---

## 🧊 3D 视觉 { #3d_vision }

**[3D-Agent: Tri-Modal Multi-Agent Collaboration for Scalable 3D Object Annotation](3d_vision/3d-agenttri-modal_multi-agent_collaboration_for_scalable_3d_object_annotation.md)**

:   提出 Tri-MARF 三模态多智能体框架，通过 VLM 标注 Agent（多视角多候选描述）+ 信息聚合 Agent（BERT 聚类 + CLIP 加权 + UCB1 多臂赌博机选择）+ 点云门控 Agent（Uni3D 文本-点云对齐过滤幻觉），实现 CLIPScore 88.7（超越人类标注 82.4）、吞吐量 12k 物体/小时，已标注约 200 万 3D 模型。

**[3D Visual Illusion Depth Estimation](3d_vision/3d_visual_illusion_depth_estimation.md)**

:   揭示了3D视觉错觉（如墙面彩绘、屏幕重播、镜面反射等）会严重欺骗现有SOTA单目和双目深度估计方法，构建了包含约3k场景/200k图像的大规模数据集，并提出基于VLM常识推理的单目-双目自适应融合框架，在各类错觉场景下达到SOTA。

**[Anti-Aliased 2D Gaussian Splatting](3d_vision/anti-aliased_2d_gaussian_splatting.md)**

:   提出 AA-2DGS，通过世界空间平坦平滑核和物体空间 Mip 滤波器两个互补机制，解决 2D Gaussian Splatting 在不同采样率下渲染时的严重锯齿问题，在保持 2DGS 几何精度优势的同时显著提升多尺度渲染质量。

**[ARMesh: Autoregressive Mesh Generation via Next-Level-of-Detail Prediction](3d_vision/armesh_autoregressive_mesh_generation_via_next-level-of-detail_prediction.md)**

:   提出将 3D mesh 生成建模为"由粗到精"的逐级细化过程（next-level-of-detail prediction），通过反转广义网格简化算法（GSlim）获得渐进式细化序列，再用 Transformer 自回归学习，从单个点开始逐步增加几何与拓扑细节生成完整网格。

**[Atlasgs Atlanta-World Guided Surface Reconstruction With Implicit Structured Gau](3d_vision/atlasgs_atlanta-world_guided_surface_reconstruction_with_implicit_structured_gau.md)**

:   提出 AtlasGS，通过将 Atlanta-world 结构先验引入隐式结构化高斯表示（implicit-structured Gaussians），在室内和城市场景中实现平滑且保留高频细节的高质量表面重建，全面超越已有隐式和显式方法。

**[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](3d_vision/becominglit_relightable_gaussian_avatars_with_hybrid_neural_shading.md)**

:   提出 BecomingLit，基于 3D Gaussian 原语和混合神经着色（neural diffuse BRDF + 解析 Cook-Torrance specular）从低成本 light stage 多视角序列重建可重光照、实时渲染的高保真头部 avatar，并发布了新的公开 OLAT 人脸数据集。

**[Can LLMs Write Faithfully? An Agent-Based Evaluation of LLM-generated Islamic Content](3d_vision/can_llms_write_faithfully_an_agent-based_evaluation_of_llm-generated_islamic_con.md)**

:   提出双Agent（定量+定性）评估框架，从神学准确性、引用完整性和文体恰当性三个维度系统评估 GPT-4o、Ansari AI 和 Fanar 在伊斯兰内容生成任务上的忠实度，发现即使最优模型也在引用可靠性上存在显著不足。

**[Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations](3d_vision/concerto_joint_2d-3d_self-supervised_learning_emerges_spatial_representations.md)**

:   Concerto 将 3D 点云模态内自蒸馏与 2D-3D 跨模态联合嵌入预测相结合，以极简设计让单一点云编码器（PTv3）涌现出超越 2D/3D 单模态甚至两者拼接的空间表征，在多个 3D 场景理解基准上刷新 SOTA（ScanNet 语义分割 80.7% mIoU）。

**[Copresheaf Topological Neural Networks: A Generalized Deep Learning Framework](3d_vision/copresheaf_topological_neural_networks_a_generalized_deep_learning_framework.md)**

:   本文提出 Copresheaf Topological Neural Networks (CTNNs)，基于代数拓扑中的余预层（copresheaf）概念，在组合复形（combinatorial complex）上定义方向性、异质的消息传递机制，统一了 CNN、GNN、Transformer、Sheaf Neural Networks 和拓扑神经网络等多种深度学习架构，并在物理模拟、图分类和高阶复形分类任务上超越传统基线。

**[CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning](3d_vision/cosmobench_a_multiscale_multiview_multitask_cosmology_benchmark_for_geometric_de.md)**

:   提出 CosmoBench——目前最大的宇宙学几何深度学习基准，包含 3.4 万点云和 2.5 万有向树，覆盖多尺度、多视角、多任务，并揭示简单线性模型有时能超越大型 GNN。

**[Cue3D: Quantifying the Role of Image Cues in Single-Image 3D Generation](3d_vision/cue3d_quantifying_the_role_of_image_cues_in_single-image_3d_generation.md)**

:   提出 Cue3D——首个模型无关的框架，通过系统性扰动 6 种图像线索（光照/纹理/轮廓/透视/边缘/局部连续性）量化其对单图 3D 生成的影响，在 7 个 SOTA 方法上揭示：形状意义而非纹理决定泛化性，光照比纹理更重要，模型过度依赖轮廓——为更透明、鲁棒的 3D 生成指明方向。

**[D$^2$USt3R: Enhancing 3D Reconstruction for Dynamic Scenes](3d_vision/d2ust3r_enhancing_3d_reconstruction_for_dynamic_scenes.md)**

:   提出 Static-Dynamic Aligned Pointmap (SDAP) 表示，将静态和动态区域的 3D 对齐统一建模，使 DUSt3R 系列方法能够在动态场景中实现准确的稠密三维重建与对应关系估计。

**[DGH: Dynamic Gaussian Hair](3d_vision/dgh_dynamic_gaussian_hair.md)**

:   提出 Dynamic Gaussian Hair (DGH)，一个数据驱动的 coarse-to-fine 框架，通过体素隐式变形模型学习头发动力学，并结合柱状 Gaussian 表示与曲率混合策略实现动态头发的逼真新视角渲染。

**[DualFocus: Depth from Focus with Spatio-Focal Dual Variational Constraints](3d_vision/dualfocus_depth_from_focus_with_spatio-focal_dual_variational_constraints.md)**

:   提出 DualFocus，通过空间变分约束（利用焦距相关梯度模式区分深度边缘与纹理伪影）和焦距变分约束（强制单峰单调的对焦概率分布）双重约束，实现从焦距堆栈中鲁棒精确的深度估计。

**[Dynamic Gaussian Splatting from Defocused and Motion-blurred Monocular Videos](3d_vision/dynamic_gaussian_splatting_from_defocused_and_motion-blurred_monocular_videos.md)**

:   提出统一框架，通过可学习模糊核卷积联合建模散焦模糊和运动模糊，结合动态高斯致密化策略和未见视角约束，从模糊单目视频中实现高质量动态 3DGS 新视角合成。

**[DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation](3d_vision/dynarend_learning_3d_dynamics_via_masked_future_rendering_for_robotic_manipulati.md)**

:   提出 DynaRend，通过掩码重建和未来预测两个互补目标，利用可微体渲染在 triplane 表征上联合学习 3D 几何、语义和动态信息，预训练后可高效迁移到下游机器人操控任务。

**[E-MoFlow: Learning Egomotion and Optical Flow from Event Data via Implicit Regularization](3d_vision/e-moflow_learning_egomotion_and_optical_flow_from_event_data_via_implicit_regula.md)**

:   提出 E-MoFlow，通过将光流建模为隐式神经表示、自运动建模为连续样条，并利用微分几何约束联合优化两者，在无监督范式下实现事件数据的 6-DoF 自运动和稠密光流联合估计。

**[EA3D: Online Open-World 3D Object Extraction from Streaming Videos](3d_vision/ea3d_online_open-world_3d_object_extraction_from_streaming_videos.md)**

:   提出 EA3D（ExtractAnything3D），一个在线开放世界 3D 物体提取框架，通过知识集成特征图、在线视觉里程计和循环联合优化，从流式视频中同时进行几何重建和全面场景理解。

**[EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes](3d_vision/eag3r_event-augmented_3d_geometry_estimation_for_dynamic_and_extreme-lighting_sc.md)**

:   EAG3R 将事件相机的异步事件流融入 MonST3R 点图重建框架，通过 Retinex 增强模块 + SNR 感知融合机制 + 事件光度一致性损失，在极端低光动态场景下实现鲁棒的深度估计、位姿跟踪和 4D 重建，零样本迁移夜间场景即可大幅超越 RGB-only 方法。

**[EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting](3d_vision/ef-3dgs_event-aided_free-trajectory_3d_gaussian_splatting.md)**

:   EF-3DGS 首次将事件相机引入自由轨迹场景重建，通过事件生成模型（EGM）重建帧间潜在图像做连续监督、对比度最大化（CMax）结合线性事件模型（LEGM）挖掘运动信息校准位姿，以及光度 BA + Fixed-GS 策略解决颜色不一致问题，在高速场景下 PSNR 提升 3dB、ATE 降低 40%。

**[ELECTRA: A Cartesian Network for 3D Charge Density Prediction with Floating Orbitals](3d_vision/electra_a_cartesian_network_for_3d_charge_density_prediction_with_floating_orbit.md)**

:   ELECTRA 提出用可学习的浮动轨道（Floating Orbitals）表示电子电荷密度，通过 Cartesian 张量等变网络预测轨道位置、权重和协方差矩阵，结合对称性打破机制和去偏层，在 QM9 基准上达到 SOTA 精度同时推理速度快 170 倍，并能将 DFT 自洽场迭代减少 50%。

**[EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](3d_vision/enerverse_envisioning_embodied_future_space_for_robotics_manipulation.md)**

:   EnerVerse 是一个生成式机器人基础模型，通过 chunk-wise 自回归视频扩散 + 稀疏上下文记忆 + 多视角生成先验构建 4D 具身空间，结合 4DGS 数据飞轮缩小 Sim2Real 差距，最终通过策略头将 4D 世界表示转化为物理动作，在 LIBERO 基准上达到 SOTA。

**[EUGens: Efficient, Unified, and General Dense Layers](3d_vision/eugens_efficient_unified_and_general_dense_layers.md)**

:   EUGens 提出一类新的高效稠密层，利用随机特征（Random Features）将全连接前馈层的推理复杂度从二次降到线性，统一了已有的高效 FFL 扩展，在 LLM 预训练、ViT 图像分类、NeRF/iSDF 三维重建等任务中实现高达 27% 加速和 30% 参数压缩，且支持无需反向传播的层级知识蒸馏。

**[Evaluation of Vision-LLMs in Surveillance Video](3d_vision/evaluation_of_vision-llms_in_surveillance_video.md)**

:   提出一个无训练的两阶段框架，利用小型 Vision-LLM 生成视频文本描述 + NLI 分类器零样本评分，系统评估了提示策略和隐私保护滤镜对监控视频异常行为识别的影响。

**[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](3d_vision/every_camera_effect_every_time_all_at_once_4d_gaussian_ray_tracing_for_physics-b.md)**

:   提出 4D Gaussian Ray Tracing (4D-GRT)，将 4D Gaussian Splatting 与物理光线追踪结合，从多视角视频重建动态场景后，以可控参数生成鱼眼畸变、景深模糊、卷帘快门等物理精确的相机效果视频数据。

**[Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation](3d_vision/fin3r_fine-tuning_feed-forward_3d_reconstruction_models_via_monocular_knowledge_.md)**

:   提出 Fin3R，通过冻结 decoder 并用带重归一化的 LoRA 适配器对 encoder 进行单目知识蒸馏微调，以统一且轻量的方式提升 DUSt3R/MASt3R/CUT3R/VGGT 等前馈式 3D 重建模型的几何精度和鲁棒性。

**[FlareX: A Physics-Informed Dataset for Lens Flare Removal via 2D Synthesis and 3D Rendering](3d_vision/flarex_a_physics-informed_dataset_for_lens_flare_removal_via_2d_synthesis_and_3d.md)**

:   提出 FlareX 数据集，通过参数化模板创建、基于光照定律的 2D 合成和基于物理引擎的 3D 渲染三个阶段生成物理真实的镜头光晕数据，训练的模型在真实世界测试集上显著超越此前所有数据集。

**[Flux4D: Flow-based Unsupervised 4D Reconstruction](3d_vision/flux4d_flow-based_unsupervised_4d_reconstruction.md)**

:   提出 Flux4D，一个无监督且可泛化的 4D 动态驾驶场景重建框架，通过前馈网络直接预测 3D 高斯及其运动速度，仅用光度损失和静态偏好正则化实现大规模场景重建，在 PandaSet 和 Waymo 上超越所有无监督方法并接近有监督方法的性能。

**[Frequency Matters: When Time Series Foundation Models Fail Under Spectral Shift](3d_vision/frequency_matters_when_time_series_foundation_models_fail_under_spectral_shift.md)**

:   揭示时间序列基础模型（TSFM）在工业场景中泛化失败的关键原因——频谱偏移（downstream 数据主频与预训练数据不重叠），通过工业级手游玩家参与预测任务和受控合成实验验证了这一假说。

**[From Objects to Anywhere: A Holistic Benchmark for Multi-level Visual Grounding in 3D Scenes](3d_vision/from_objects_to_anywhere_a_holistic_benchmark_for_multi-level_visual_grounding_i.md)**

:   提出 Anywhere3D-Bench，首个涵盖区域/空间/物体/部件四个层级的 3D 视觉定位基准，揭示即使最强的 Gemini-2.5-Pro 和 o3 在空间级任务上仅达约 30% 准确率、部件级约 40%，远低于人类的 95%。

**[From Pixels To Views Learning Angular-Aware And Physics-Consistent Representatio](3d_vision/from_pixels_to_views_learning_angular-aware_and_physics-consistent_representatio.md)**

:   提出XLFM-Former用于扩展光场显微镜(XLFM)的3D重建：构建首个XLFM-Zebrafish标准化基准，设计Masked View Modeling (MVM-LF)自监督预训练学习角度先验，引入光学渲染一致性损失(ORC Loss)确保物理可信性，PSNR较SOTA提升7.7%（54.04 vs 50.16 dB）。

**[From Programs to Poses: Factored Real-World Scene Generation via Learned Program Libraries](3d_vision/from_programs_to_poses_factored_real-world_scene_generation_via_learned_program_.md)**

:   提出 FactoredScenes，将真实世界 3D 场景生成分解为五步因式分解——从合成数据学布局程序库、LLM 生成场景程序、执行程序获得轴对齐布局、程序条件化层次姿态预测、物体检索放置，在卧室上 FID 改善 38.3%、KID 改善 80.4%，人类仅 67% 能区分生成与真实 ScanNet。

**[Fully Dynamic Algorithms for Chamfer Distance](3d_vision/fully_dynamic_algorithms_for_chamfer_distance.md)**

:   提出首个全动态 Chamfer 距离维护算法，将问题归约为近似最近邻（ANN）查询，实现 $(1+\epsilon)$ 近似且更新时间 $\tilde{O}(\epsilon^{-d})$，大幅突破了静态重算的线性时间下界，在真实数据集上误差 <10% 且速度比朴素方法快数个数量级。

**[Galactification: Painting Galaxies onto Dark Matter Only Simulations Using a Transformer-Based Model](3d_vision/galactification_painting_galaxies_onto_dark_matter_only_simulations_using_a_tran.md)**

:   提出一个多模态 Transformer 编解码框架，以廉价的暗物质 N-body 模拟的密度场和速度场为输入，自回归生成星系目录（位置 + 物理属性），在多种统计指标上忠实再现流体动力学模拟结果，计算加速约 100 倍。

**[GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies](3d_vision/gaudp_reinventing_multi-agent_collaboration_through_gaussian-image_synergy_in_di.md)**

:   提出 GauDP，通过从多智能体的去中心化 RGB 观测中构建全局一致的 3D 高斯场，并将高斯属性动态分配回各智能体的局部视角，实现可扩展的、感知增强的多智能体协作模仿学习。

**[Gaussian-Augmented Physics Simulation and System Identification with Complex Colliders](3d_vision/gaussian-augmented_physics_simulation_and_system_identification_with_complex_col.md)**

:   提出 AS-DiffMPM，一种支持任意形状刚体碰撞体的可微物质点法（MPM）框架，结合多种新视角合成方法实现从视觉观测中估计物体物理参数的系统辨识。

**[Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span](3d_vision/gaze_beyond_the_frame_forecasting_egocentric_3d_visual_span.md)**

:   提出 EgoSpanLift 方法，将第一人称 2D 注视预测提升到 3D 空间，构建多层级体积视觉跨度表示，结合 3D U-Net 和单向 Transformer 实现对未来 3D 视觉关注区域的预测。

**[GeoComplete: Geometry-Aware Diffusion for Reference-Driven Image Completion](3d_vision/geocomplete_geometry-aware_diffusion_for_reference-driven_image_completion.md)**

:   提出 GeoComplete，通过将投影点云作为几何条件注入双分支扩散模型，并结合 target-aware masking 策略，实现几何一致的参考驱动图像补全，PSNR 提升 17.1%。

**[GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction](3d_vision/geosvr_taming_sparse_voxels_for_geometrically_accurate_surface_reconstruction.md)**

:   提出基于稀疏体素的显式表面重建框架 GeoSVR，通过体素不确定性深度约束和稀疏体素表面正则化，在几何精度、细节保留和重建完整性方面全面超越现有基于 3DGS 和 SDF 的方法。

**[GOATex: Geometry & Occlusion-Aware Texturing](3d_vision/goatex_geometry_occlusion-aware_texturing.md)**

:   GOATex 提出首个遮挡感知的 3D 网格纹理生成框架，通过基于光线投射的 hit level 分层机制将网格分解为由外到内的可见性层，配合法线翻转和残差面聚类的两阶段可见性控制策略以及基于可见性权重的 UV 空间融合，实现了对外表面和被遮挡内表面的高质量纹理生成。

**[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](3d_vision/haif-gs_hierarchical_and_induced_flow-guided_gaussian_splatting_for_dynamic_scen.md)**

:   HAIF-GS 提出基于稀疏运动锚点的动态 3DGS 框架，通过锚点过滤器区分动静区域、自监督诱导场景流引导时序一致变形、以及分层锚点加密捕捉精细非刚性运动，在 NeRF-DS 和 D-NeRF 基准上取得 SOTA 渲染质量。

**[High Resolution UDF Meshing via Iterative Networks](3d_vision/high_resolution_udf_meshing_via_iterative_networks.md)**

:   本文提出首个针对无符号距离场（UDF）的迭代式网格化方法，通过多轮次前向传播逐步将邻域信息传播到局部体素的伪符号预测中，有效解决了高分辨率下神经 UDF 噪声导致的表面空洞和不连续问题，在多个数据集上显著优于现有单遍方法。

**[How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?](3d_vision/how_many_tokens_do_3d_point_cloud_transformer_architectures_really_need.md)**

:   本文系统性地揭示了 3D 点云 Transformer（如 PTv3、Sonata）中存在 90-95% 的 token 冗余，并提出 gitmerge3D——一种全局信息感知的图 token 合并方法，通过能量分数自适应合并策略实现了高达 5.3× FLOPs 降低和 6.4× 显存节省而几乎不损失精度。

**[Hybrid Physical-Neural Simulator for Fast Cosmological Hydrodynamics](3d_vision/hybrid_physical-neural_simulator_for_fast_cosmological_hydrodynamics.md)**

:   提出一种混合物理-神经宇宙学模拟器，用可微分粒子网格（PM）方法处理引力动力学，用物理约束的神经网络参数化气体的有效压力场，仅需单次参考模拟即可训练，在场级别和统计量级别均优于 EGD 基线。

**[HyPlaneHead: Rethinking Tri-plane-like Representations in Full-Head Image Synthesis](3d_vision/hyplanehead_rethinking_tri-plane-like_representations_in_full-head_image_synthes.md)**

:   系统分析了 tri-plane 类表征在 3D 感知头部合成中的三大问题（镜像伪影、不均匀映射、特征穿透），提出 hy-plane 混合表征（平面+球面）结合 unify-split 策略和近等面积映射，在全头图像合成中达到 SOTA。

**[HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis](3d_vision/hyrf_hybrid_radiance_fields_for_memory-efficient_and_high-quality_novel_view_syn.md)**

:   提出混合辐射场（HyRF），将紧凑的显式高斯体（仅存储8个参数）与解耦的网格神经场相结合，在实现 20× 模型压缩的同时达到 SOTA 渲染质量和实时性能。

**[IBGS: Image-Based Gaussian Splatting](3d_vision/ibgs_image-based_gaussian_splatting.md)**

:   提出基于图像的高斯泼溅方法（IBGS），通过从邻近训练图像中学习颜色残差来增强标准3DGS的渲染质量，在不增加存储开销的前提下显著提升高频细节和视角依赖效果的建模能力。

**[IndEgo: A Dataset of Industrial Scenarios and Collaborative Work for Egocentric Assistants](3d_vision/indego_a_dataset_of_industrial_scenarios_and_collaborative_work_for_egocentric_a.md)**

:   提出IndEgo——首个面向真实工业场景的大规模多模态第一人称视觉数据集，包含3,460段自我中心录像（约197小时）和1,092段外部视角录像（约97小时），覆盖装配/拆卸、物流、检修、木工等五大类任务及协作场景，并建立了错误检测、推理问答和协作理解三项基准。

**[Instant Video Models: Universal Adapters for Stabilizing Image-Based Networks](3d_vision/instant_video_models_universal_adapters_for_stabilizing_image-based_networks.md)**

:   提出一类通用的稳定化适配器（Stabilization Adapters），可插入几乎任何图像模型架构中，通过冻结基础网络仅训练适配器参数，配合统一的精度-稳定性-鲁棒性损失函数，使帧级模型获得视频时序一致性和腐蚀鲁棒性。

**[Jasmine Harnessing Diffusion Prior For Self-Supervised Depth Estimation](3d_vision/jasmine_harnessing_diffusion_prior_for_self-supervised_depth_estimation.md)**

:   首次将Stable Diffusion视觉先验引入自监督单目深度估计：提出Mix-Batch Image Reconstruction避免自监督噪声损坏SD先验，设计Scale-Shift GRU桥接SD的尺度偏移不变性(SSI)与自监督的尺度不变性(SI)深度，在KITTI上AbsRel达0.102且泛化性强。

**[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS](3d_vision/langsplatv2_high-dimensional_3d_language_gaussian_splatting_with_450_fps.md)**

:   通过将每个3D高斯视为全局字典上的稀疏编码，LangSplatV2用稀疏系数场替代重量级解码器，实现476.2 FPS的高维特征溅射和384.6 FPS的3D开放词汇查询，较LangSplat加速47倍。

**[Modeling Microenvironment Trajectories on Spatial Transcriptomics with NicheFlow](3d_vision/modeling_microenvironment_trajectories_on_spatial_transcriptomics_with_nicheflow.md)**

:   NicheFlow是一种基于Flow Matching的生成模型，将细胞微环境表示为点云，通过Variational Flow Matching和最优传输联合建模细胞状态与空间坐标的时间演化，在胚胎发育、脑发育和衰老数据集上显著优于单细胞级别的轨迹推断方法。

**[Multi-Scale Finetuning for Encoder-based Time Series Foundation Models](3d_vision/multi-scale_finetuning_for_encoder-based_time_series_foundation_models.md)**

:   提出 MSFT（Multi-Scale FineTuning），通过因果分析揭示 naive 微调忽略尺度混淆问题，设计多尺度建模框架对 encoder-based 时间序列基础模型进行高效微调，显著超越 naive 微调和从头训练的 SOTA 方法。

**[Object-Centric Representation Learning For Enhanced 3D Semantic Scene Graph Pred](3d_vision/object-centric_representation_learning_for_enhanced_3d_semantic_scene_graph_pred.md)**

:   通过实证分析揭示物体特征可区分性是 3D 场景图谓词预测的关键瓶颈（物体分类错误导致 92%+ 的谓词错误），提出独立对比预训练的物体编码器（3D-2D-Text 三模态对齐）+ 几何正则化关系编码器 + 双向边门控 GNN，在 3DSSG 上 Object R@1 59.53%、Predicate R@50 91.40% 均达新 SOTA。

**[OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects](3d_vision/onlinesplatter_pose-free_online_3d_reconstruction_for_free-moving_objects.md)**

:   提出 OnlineSplatter，一个无需相机位姿、深度先验或全局优化的前馈式在线3D重建框架，通过双键记忆模块（外观-几何潜在键 + 方向键）实现自由移动物体的恒定时间增量重建。

**[SingRef6D: Monocular Novel Object Pose Estimation with a Single RGB Reference](3d_vision/singref6d_monocular_novel_object_pose_estimation_with_a_single_rgb_reference.md)**

:   提出SingRef6D，一个仅需单张RGB参考图像的轻量级6D位姿估计流水线，通过token-scaler微调Depth-Anything v2实现鲁棒深度预测，并引入深度感知匹配增强LoFTR的空间推理能力，在透明/反光物体场景中大幅超越现有方法。

**[SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation](3d_vision/sofar_language-grounded_orientation_bridges_spatial_reasoning_and_object_manipul.md)**

:   提出"语义朝向"(Semantic Orientation)概念，用自然语言描述物体方向（如 USB 的"插入方向"、杯子的"把手方向"），构建 OrienText300K 大规模数据集训练 PointSO 模型实现零样本朝向预测，并集成为 SoFar 系统实现 6-DoF 场景理解与机器人操作。

**[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian Splatting](3d_vision/temporal_smoothness-aware_rate-distortion_optimized_4d_gaussian_splatting.md)**

:   提出首个端到端率失真（RD）优化的 4D 高斯泼溅压缩框架，通过 Haar 小波变换利用动态点轨迹的时序平滑先验，在 Ex4DGS 基础上实现高达 91× 的压缩率（平均模型仅约原始 1.1%），同时保持合理的渲染质量和灵活的率-质量权衡控制。

**[TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning](3d_vision/tirex_zero-shot_forecasting_across_long_and_short_horizons_with_enhanced_in-cont.md)**

:   提出基于xLSTM的预训练时间序列预测模型TiRex，通过连续片段掩码（CPM）策略和数据增强技术，在GiftEval和Chronos-ZS两大标准基准上以仅35M参数全面超越Chronos Bolt（200M）、TimesFM（500M）等大模型，同时在短期和长期零样本预测中均达到SOTA。

---

## ⚡ LLM 效率 { #llm_efficiency }

**[3-Model Speculative Decoding (PyramidSD)](llm_efficiency/3model_speculative_decoding.md)**

:   在标准的draft-target两模型推测解码的中间插入一个"qualifier"模型，构成三层金字塔式解码架构（PyramidSD），利用模型家族天然的熵梯度来分级过滤token，以模糊接受准则放宽匹配阈值，实现最高1.91×的速度提升（在RTX 4090上达到124 tok/s）。

**[A Multi-Task Benchmark for Abusive Language Detection in Low-Resource Settings](llm_efficiency/a_multitask_benchmark_for_abusive_language_detection_in_lowr.md)**

:   针对低资源语言 Tigrinya，构建了首个大规模多任务基准数据集 TiALD（13,717条YouTube评论，涵盖滥用检测、情感分析、主题分类三任务），并证明小型微调模型在低资源场景下显著优于GPT-4o等前沿LLM（F1: 86.67% vs 79.31%）。

**[A Stochastic Differential Equation Framework for Multi-Objective LLM Interactions](llm_efficiency/a_stochastic_differential_equation_framework_for_multi-objective_llm_interaction.md)**

:   将 LLM 迭代交互中的多目标优化建模为 SDE（漂移-扩散过程），通过干扰矩阵量化目标间的耦合模式，通过特征值谱分析策略收敛行为，在代码生成（安全性、效率、功能性三目标）上验证了不同策略的收敛率（0.33-1.29）和可预测性（$R^2$ 达 0.74）。

**[A Unified Framework for Establishing the Universal Approximation of Transformer-Type Architectures](llm_efficiency/a_unified_framework_for_establishing_the_universal_approxima.md)**

:   本文建立了一个统一的理论框架来证明各类Transformer架构的万能逼近性(UAP)，将UAP归结为两个可验证条件——前馈层的非线性仿射不变性和注意力层的token可区分性——并利用解析性假设将后者简化为仅需检验两样本情形。

**[Advancing Expert Specialization for Better MoE](llm_efficiency/advancing_expert_specialization_for_better_moe.md)**

:   通过正交性损失（减少专家间投影重叠）和方差损失（增大路由分数差异）双目标优化，在不修改 MoE 架构的前提下将专家重叠减少 45%、路由方差提升 150%，11 个基准任务平均提升 23.79%，同时完全保持负载均衡。

**[Approximately Aligned Decoding](llm_efficiency/approximately_aligned_decoding.md)**

:   提出 Approximately Aligned Decoding (AprAD)，一种利用投机解码（speculative decoding）中的前缀选择算法来实现LLM受约束生成的方法——在遇到约束违反时，既不像约束生成那样仅回退一步（导致极端概率放大），也不像ASAp那样完全重新采样（计算成本过高），而是通过投机采样智能选择回退位置，在输出分布失真和计算效率之间取得良好平衡。

**[Constant Bit-Size Transformers Are Turing Complete](llm_efficiency/constant_bit-size_transformers_are_turing_complete.md)**

:   首次证明常数 bit 精度、固定参数数量的 Transformer（仅允许上下文窗口增长）是图灵完备的，并建立了精确的复杂度等价关系 WINDOW[s(n)] = SPACE[s(n)]，表明扩展上下文窗口——而非模型尺寸——已足以实现通用计算。

**[Critical Batch Size Revisited: A Simple Empirical Approach to Large-Batch Language Model Training](llm_efficiency/critical_batch_size_revisited_a_simple_empirical_approach_to_large-batch_languag.md)**

:   提出 branched training 方法直接实证测量临界 batch size (CBS)，发现 CBS 在训练早期快速增长后趋于平稳且不依赖模型规模，据此设计 batch size warmup 策略以 43% 更少的梯度步数达到同等甚至更优的训练 loss。

**[Deep Compositional Phase Diffusion for Long Motion Sequence Generation](llm_efficiency/deep_compositional_phase_diffusion_for_long_motion_sequence_generation.md)**

:   提出 Compositional Phase Diffusion 框架，在 ACT-PAE 建立的频域相位空间中用 SPDM 和 TPDM 分别处理语义对齐和过渡连续性，实现长程组合式动作序列生成，在 BABEL-TEACH 上达到 SOTA。

**[Dense Associative Memory with Epanechnikov Energy](llm_efficiency/dense_associative_memory_with_epanechnikov_energy.md)**

:   提出基于 Epanechnikov 核的 log-sum-ReLU（LSR）能量函数替代传统的 log-sum-exp（LSE），在 Dense Associative Memory 中首次实现了"精确记忆所有模式 + 同时涌现新的创造性局部极小"的共存，且保持指数级记忆容量。

**[DICE: Discrete Interpretable Comparative Evaluation with Probabilistic Scoring for RAG](llm_efficiency/dice_discrete_interpretable_comparative_evaluation_with_probabilistic_scoring_fo.md)**

:   提出 DICE 框架，通过两阶段评估（证据耦合深度分析 + 概率化 {A,B,Tie} 打分）和瑞士赛制锦标赛实现 RAG 系统的可解释、鲁棒、高效评估，在中文金融 QA 数据集上达到 85.7% 人类专家一致率，远超 RAGAS（45.7%）。

**[DISC: Dynamic Decomposition Improves LLM Inference Scaling](llm_efficiency/disc_dynamic_decomposition_improves_llm_inference_scaling.md)**

:   DISC 提出了一种动态分解算法，在推理时根据每一步的 z-score（采样奖励的标准化最大值）自动、递归地调整推理步骤的粒度——困难步骤分更细、简单步骤一步跨过——可以即插即用地与贪心搜索、Beam Search、MCTS 结合，在 APPS、MATH、LiveCodeBench 上以更少的 token 预算达到更高的 pass@k。

**[Document Summarization with Conformal Importance Guarantees](llm_efficiency/document_summarization_with_conformal_importance_guarantees.md)**

:   首次将Conformal Prediction应用于文档摘要，通过校准句子重要性分数的阈值，为抽取式摘要提供用户可控的覆盖率($1-\alpha$)和召回率($\beta$)的严格统计保证，方法模型无关且仅需小规模校准集。

**[Dynamics of Spontaneous Topic Changes in Next Token Prediction with Self-Attention](llm_efficiency/dynamics_of_spontaneous_topic_changes_in_next_token_prediction_with_self-attenti.md)**

:   从理论和实验两方面研究自注意力模型中"自发主题切换"的动力学机制，证明在单层 self-attention 模型中：(1) 混合主题训练保持原主题的 token 优先级顺序；(2) 主题切换仅在低优先级 token 数量超过高优先级 token 时发生；(3) 更长输入和更模糊主题不会增加切换概率——与人类认知相反。

**[Edit Less Achieve More Dynamic Sparse Neuron Masking For Lifelong Knowledge Edit](llm_efficiency/edit_less_achieve_more_dynamic_sparse_neuron_masking_for_lifelong_knowledge_edit.md)**

:   提出 NMKE 框架，通过神经元级归因发现 knowledge-general 和 knowledge-specific 两类知识神经元，并结合熵引导的动态稀疏 mask，实现精准神经元级知识编辑，在 5000 步连续编辑后仍保持高编辑成功率和模型通用能力。

**[Efficient Training-Free Online Routing for High-Volume Multi-LLM Serving](llm_efficiency/efficient_training-free_online_routing_for_high-volume_multi-llm_serving.md)**

:   提出首个无需训练的在线 LLM 路由算法 PORT，通过近似最近邻搜索估计查询特征，并在少量初始查询上一次性优化对偶变量作为路由权重，在有限 token 预算下实现接近离线最优 ($1-o(1)$ 竞争比) 的路由性能，平均较基线提升 3.55× 性能、1.85× 成本效率和 4.25× 吞吐量。

**[Exploring the Translation Mechanism of Large Language Models](llm_efficiency/exploring_the_translation_mechanism_of_large_language_models.md)**

:   提出 subspace-intervened path patching 方法对 LLM 翻译机制进行精细因果分析，发现翻译由不到 5% 的稀疏 attention head 驱动——分为 source head、indicator head、positional head 三类功能角色，MLP 将其特征整合为以英语为中心的中间表示，仅微调 64 个关键 head 即可匹配全参数微调性能。

**[Frequency-Aware Token Reduction for Efficient Vision Transformer](llm_efficiency/frequency-aware_token_reduction_for_efficient_vision_transformer.md)**

:   从频域视角提出 frequency-aware token reduction，将 token 分为高频（HF）和低频（LF）两组，选择性保留 HF token 并将 LF token 聚合为 DC token，在缓解 rank collapse 的同时减少 ViT 的计算量，在 30% token 减少率下多个模型上超越现有 SOTA。

**[From Shortcut to Induction Head: How Data Diversity Shapes Algorithm Selection in Transformers](llm_efficiency/from_shortcut_to_induction_head_how_data_diversity_shapes_algorithm_selection_in.md)**

:   通过严格的理论分析证明了预训练数据的多样性（由"max-sum ratio"刻画）决定了单层Transformer学到的是可泛化的induction head还是无法OOD泛化的位置捷径，并给出了使模型学会induction head的最优预训练分布。

**[Hardware-Aligned Hierarchical Sparse Attention For Efficient Long-Term Memory Ac](llm_efficiency/hardware-aligned_hierarchical_sparse_attention_for_efficient_long-term_memory_ac.md)**

:   提出层次化稀疏注意力（HSA）及 RAMba 架构，通过两阶段 token-to-chunk 相关性学习与硬件对齐 kernel 设计，让 Mamba 获得高效长程随机访问能力，仅在 4K 上下文预训练即可在 64M passkey retrieval 上达到 100% 准确率。

**[Hierarchical Balance Packing: Towards Efficient Supervised Fine-tuning for Long-Context LLM](llm_efficiency/hierarchical_balance_packing_towards_efficient_supervised_fine-tuning_for_long-c.md)**

:   提出层次均衡打包（HBP）方法，通过多级打包分组、均衡批处理、自适应序列并行和稳定损失归一化，解决长短上下文混合 SFT 中的注意力计算不均衡和通信浪费问题，在 DeepSeek-V2 (236B) 上实现 2.4× 训练加速且性能无损。

**[HiFi-RAG: Hierarchical Content Filtering and Two-Pass Generation for Open-Domain RAG](llm_efficiency/hifi-rag_hierarchical_content_filtering_and_two-pass_generation_for_open-domain_.md)**

:   通过分离轻量级 Flash 模型的过滤能力与 Pro 模型的推理能力，构建多阶段管道（查询优化→分层过滤→两阶段生成→引文验证），在 MMU-RAGent 竞赛中实现 SOTA 性能。

**[HyGen: Efficient LLM Serving via Elastic Online-Offline Request Co-location](llm_efficiency/hygen_efficient_llm_serving_via_elastic_online-offline_request_co-location.md)**

:   HyGen是干扰感知LLM推理系统，通过延迟预测和虚拟队列调度实现在线离线工作负载的弹性共置，保证SLO同时获得3.87-5.84倍吞吐改进。

**[Improving Perturbation-based Explanations by Understanding the Role of Uncertainty Calibration](llm_efficiency/improving_perturbation-based_explanations_by_understanding_the_role_of_uncertain.md)**

:   揭示了不确定性校准（模型置信度与实际准确率的对齐）与扰动式可解释性方法质量之间的根本联系，证明模型在扰动输入下的误校准直接损害全局和局部解释质量，并提出 ReCalX 通过扰动级别自适应温度缩放显著改善解释的鲁棒性和保真度。

**[L-MTP: Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models](llm_efficiency/l-mtp_leap_multi-token_prediction_beyond_adjacent_context_for_large_language_mod.md)**

:   L-MTP 在多token预测（MTP）基础上引入跳跃机制，预测非相邻位置的token（如位置1,3,5,7而非1,2,3,4），通过"后向查找"解码策略复用先前预测填补空隙，在3B-12B模型上实现22%推理加速的同时保持或提升任务性能。

**[Learning in Compact Spaces with Approximately Normalized Transformer](llm_efficiency/learning_in_compact_spaces_with_approximately_normalized_transformer.md)**

:   提出 anGPT（近似归一化 Transformer），利用高维空间中向量范数的集中现象，用简单标量乘法替代逐层精确归一化，在消除权重衰减和学习率预热的同时实现了相比 GPT+（含 QK-norm）40% 的收敛加速，仅增加 3% 运行时开销。

**[Long-Context Modeling with Dynamic Hierarchical Sparse Attention for On-Device LLMs](llm_efficiency/long-context_modeling_with_dynamic_hierarchical_sparse_attention_for_on-device_l.md)**

:   提出动态分层稀疏注意力 (DHSA)，通过自适应 chunk 分割 + chunk 级相似度预测 + 上采样到 token 级的分层框架，在不重训基座模型的前提下将密集注意力替换为稀疏注意力，在 Gemma2/3 上实现与密集注意力同等精度、20-60% prefill 延迟降低和 35% 峰值内存节省。

**[LooGLE v2: Are LLMs Ready for Real World Long Dependency Challenges?](llm_efficiency/loogle_v2_are_llms_ready_for_real_world_long_dependency_challenges.md)**

:   构建覆盖法律/金融/游戏/代码四大真实领域、长度16K-2M token的长依赖推理基准LooGLE v2，设计10类领域特定任务共1,934个QA实例，评估10个LLM发现最强模型GPT-4.1仅59.2%，揭示当前LLM在真实长依赖场景下的根本不足。

**[MEMOIR: Lifelong Model Editing with Minimal Overwrite and Informed Retention for LLMs](llm_efficiency/memoir_lifelong_model_editing_with_minimal_overwrite_and_informed_retention_for_.md)**

:   提出MEMOIR框架，通过在FFN层引入零初始化的残差记忆矩阵，利用基于TopHash的稀疏掩码将每次编辑限制在记忆参数的不同子集上，推理时通过掩码重叠率识别相关编辑并条件性激活知识，在15000次连续编辑下仍保持可靠性、泛化性和局部性的最优平衡。

**[Minimizing False-Positive Attributions in Explanations of Non-Linear Models](llm_efficiency/minimizing_false-positive_attributions_in_explanations_of_non-linear_models.md)**

:   针对非线性模型的XAI解释中抑制变量(suppressor variable)导致的假阳性归因问题，提出PatternLocal方法，将局部判别式代理模型权重转换为生成式表示，在XAI-TRIS基准、MRI人工病灶和EEG运动想象三个数据集上显著减少了假阳性特征归因。

**[MIR-Bench: Can Your LLM Recognize Complicated Patterns via Many-Shot In-Context Reasoning?](llm_efficiency/mir-bench_can_your_llm_recognize_complicated_patterns_via_many-shot_in-context_r.md)**

:   提出 MIR-Bench，首个大规模多样化的 many-shot 上下文推理基准，通过从编程题中自动生成输入输出对来测试 LLM 的模式识别能力，发现 LLM 在 many-shot 场景下存在注意力分散导致的性能饱和现象，且转导推理普遍优于归纳推理。

**[Mozart: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures](llm_efficiency/mozart_modularized_and_efficient_moe_training_on_35d_wafer-scale_chiplet_archite.md)**

:   提出 Mozart 算法-硬件协同设计框架，通过专家聚类分配、细粒度流式调度和 3.5D 晶粒架构（NoP-Tree + 分层存储），在三个 MoE-LLM 上实现 1.9× 以上的训练加速。

**[Not All Splits Are Equal: Rethinking Attribute Generalization Across Unrelated Categories](llm_efficiency/not_all_splits_are_equal_rethinking_attribute_generalization_across_unrelated_ca.md)**

:   本文首次系统评估了属性预测任务中训练/测试划分策略对泛化性能的影响,提出了基于 LLM 语义分组、嵌入相似度、嵌入聚类和超类标签的四种渐进式难度划分方案,发现无监督聚类划分在不依赖标注的情况下实现了与真值超类划分相当的去泄漏效果,同时保留了更好的预测性能。

**[Obliviator Reveals the Cost of Nonlinear Guardedness in Concept Erasure](llm_efficiency/obliviator_reveals_the_cost_of_nonlinear_guardedness_in_concept_erasure.md)**

:   提出Obliviator——一种基于RKHS中HSIC最小化的后处理概念擦除方法，通过两步迭代优化逐步变形特征空间，首次实现对非线性对抗者的完全防护，同时量化了非线性防护的效用-擦除代价（utility-erasure trade-off），在多个PLM和数据集上显著优于现有方法。

**[On the Entropy Calibration of Language Models](llm_efficiency/on_the_entropy_calibration_of_language_models.md)**

:   系统研究语言模型的熵校准问题（生成文本的熵是否匹配在人类文本上的 log loss），发现由于数据分布的幂律特性（$\alpha \approx 1$），误差积累随模型规模的改善极为缓慢（scaling exponent $\approx -0.05$），并从理论上证明了在多项式时间内可以在不牺牲多样性的前提下校准熵。

**[On the Expressive Power of Mixture-of-Experts for Structured Complex Tasks](llm_efficiency/on_the_expressive_power_of_mixture-of-experts_for_structured_complex_tasks.md)**

:   首次系统分析 MoE 在结构化复杂任务上的表达能力：证明浅层 MoE 可在低维流形上克服维度诅咒（近似速率由内在维度 $d$ 而非环境维度 $D$ 决定），深层 MoE 通过 $E$ 专家 × $L$ 层的分层组合可高效近似有 $E^L$ 段的分段函数，远超朴素上界 $LE$。

**[One Prompt Fits All: Universal Graph Adaptation for Pretrained Models](llm_efficiency/one_prompt_fits_all_universal_graph_adaptation_for_pretrained_models.md)**

:   理论证明表示级图提示（representation-level prompt）本质等价于线性探针，据此提出 UniPrompt——基于可学习 kNN 拓扑提示图的输入级方法，通过 bootstrapping 策略融合提示图和原图，在同域和跨域 few-shot 节点分类中一致超越现有图提示学习方法。

**[ParallelPrompt: Extracting Parallelism from Large Language Model Queries](llm_efficiency/parallelprompt_extracting_parallelism_from_large_language_model_queries.md)**

:   构建了首个查询内并行（intra-query parallelism）基准数据集ParallelPrompt，包含37000+条真实用户提示的结构化分解标注，证明约10%的用户查询包含可并行的潜在结构，并行执行可实现最高5.7×的延迟加速且质量损失有限。

**[Plasticity as the Mirror of Empowerment](llm_efficiency/plasticity_as_the_mirror_of_empowerment.md)**

:   本文提出**广义有向信息（GDI）**作为度量智能体可塑性（plasticity）的信息论工具，揭示可塑性是赋权（empowerment）的"镜像"——两者使用相同度量、仅方向相反，并证明了两者之间存在严格的张力约束（tension bound）。

**[Scale-invariant Attention](llm_efficiency/scale-invariant_attention.md)**

:   借鉴自然图像的尺度不变性，提出对 attention logits 做位置相关的乘性缩放和加性偏移变换，使注意力在不同 token 范围上的总权重和稀疏度满足尺度不变性，从而实现从短序列训练到长序列推理的零样本泛化（4k→64k 仅需一个超参数 $\tau$）。

**[Silent Tokens, Loud Effects: Padding in LLMs](llm_efficiency/silent_tokens_loud_effects_padding_in_llms.md)**

:   系统性研究了padding token在未被正确掩码时对LLM的影响，发现即使少量padding也会漂移隐层表示、降低生成质量、不可预测地改变偏见，而128个padding token可将Llama-3.1-8B的有害提示攻击成功率从8%飙升到77.5%，本质上实现了jailbreak。

**[SkyLadder: Better and Faster Pretraining via Context Window Scheduling](llm_efficiency/skyladder_better_and_faster_pretraining_via_context_window_scheduling.md)**

:   通过上下文窗口短到长的渐进式调度策略 SkyLadder，在固定计算量下实现更优的预训练效率（节省 22% 训练时间）和更好的模型性能（+3.7%），反驳了"长上下文=好性能"的业界信念。

**[SPARTA Alignment: Collectively Aligning Multiple Language Models through Combat](llm_efficiency/sparta_alignment_collectively_aligning_multiple_language_models_through_combat.md)**

:   让多个LLM组成"斯巴达部落"互相竞技和互评，通过声誉加权的判断聚合生成偏好对，再用DPO迭代训练所有模型，在12个任务中的10个上超越Self-Rewarding等自对齐基线，平均提升7%。

**[Structure-Aware Spectral Sparsification via Uniform Edge Sampling](llm_efficiency/structure-aware_spectral_sparsification_via_uniform_edge_sampling.md)**

:   本文证明在具有良好聚类结构的图上（结构比 Υ(k) 足够大），**均匀边采样**即可保留谱聚类所需的谱子空间结构，无需昂贵的有效电阻预计算——这是首个关于均匀采样保持结构的可证明保证。

**[上下文学习中的技术债务：长序列中的递减效率](llm_efficiency/technical_debt_in_in-context_learning_diminishing_efficiency_in_long_context.md)**

:   揭示ICL作为学习算法在少射大样本制度下存在本质低效：少射ICL样本复杂度接近贝叶斯最优(1.1×)，而多射时恶化至1.45×，信息论分析证明此低效来自非递减过剩风险。

**[Tensor Product Attention Is All You Need](llm_efficiency/tensor_product_attention_is_all_you_need.md)**

:   通过上下文张量分解将 Q/K/V 表示为低秩因子的加权和，将 KV 缓存压缩至原来的 1/10~1/16，同时在验证损失和下游任务精度上超越标准 MHA/MQA/GQA/MLA。

**[The Emergence of Sparse Attention: Impact of Data Distribution and Benefits of Repetition](llm_efficiency/the_emergence_of_sparse_attention_impact_of_data_distribution_and_benefits_of_re.md)**

:   通过理论分析和受控实验研究 sparse attention 的涌现机制，揭示涌现时间遵循关于序列长度和维度的幂律关系 $T_\epsilon \propto \sqrt{d} \cdot T$，并发现 in-context 和 cross-sample 两种数据重复策略都能加速涌现，为理解 LLM 能力涌现提供了统一的 sparse attention 视角。

**[The PokeAgent Challenge: Competitive and Long-Context Learning at Scale](llm_efficiency/the_pokeagent_challenge_competitive_and_long-context_learning_at_scale.md)**

:   提出 PokéAgent Challenge，一个基于宝可梦对战和RPG速通的双赛道大规模AI基准，通过NeurIPS 2025竞赛验证了专家RL方法远超通用LLM方法，并揭示宝可梦对战衡量的能力与现有49个LLM基准近乎正交。

**[Tiled Flash Linear Attention: More Efficient Linear RNN and xLSTM Kernels](llm_efficiency/tiled_flash_linear_attention_more_efficient_linear_rnn_and_xlstm_kernels.md)**

:   提出 TFLA（Tiled Flash Linear Attention）算法，通过二层序列并行化和 tiling 优化，实现高效的线性 RNN/mLSTM 内核，相比 FlashAttention 3 和 Mamba 2 获得显著墙钟加速（训练 >2x vs Mamba 2），同时保持等价的模型精度。

**[Towards Interpretability Without Sacrifice: Faithful Dense Layer Decomposition with Mixture of Decoders](llm_efficiency/towards_interpretability_without_sacrifice_faithful_dense_layer_decomposition_wi.md)**

:   提出 Mixture of Decoders (MxD)，将 LLM 的 MLP 层分解为数万个稀疏激活的专家子层（layer-level sparsity），每个专家通过 Hadamard 乘积张量分解实现满秩线性变换，在稀疏性-准确性权衡上显著优于 Transcoders，同时保持可解释性。

**[UMoE: Unifying Attention and FFN with Shared Experts](llm_efficiency/umoe_unifying_attention_and_ffn_with_shared_experts.md)**

:   通过重新表述多头注意力机制，揭示其与 FFN 共有的"两层矩阵乘法"结构，据此提出 UMoE 统一架构——在注意力和 FFN 层使用相同设计的专家并支持参数共享，在 Base(134M) 和 Large(1.1B) 模型上均优于现有 FFN-MoE 和 Attention-MoE 基线。

**[Unmasking Covid-19 Vulnerability In Nigeria Mapping Risks Beyond Urban Hotspots](llm_efficiency/unmasking_covid-19_vulnerability_in_nigeria_mapping_risks_beyond_urban_hotspots.md)**

:   本文针对尼日利亚各州构建了一个综合 COVID-19 脆弱性风险评分体系,整合人口密度、贫困、医疗可及性和年龄风险四个维度,并通过 GIS 地图可视化热点区域,为公共卫生资源分配提供数据驱动的决策工具。

**[Vocabulary Customization For Efficient Domain-Specific Llm Deployment](llm_efficiency/vocabulary_customization_for_efficient_domain-specific_llm_deployment.md)**

:   提出一种保证不增加任何输入 token 数的词表扩展算法，通过向预训练 LLM 的 tokenizer 添加领域特定 token，在电商场景实现输入序列缩短 20%、推理吞吐量提升 20-30%，且不损失模型质量。

**[ZeroS: Zero-Sum Linear Attention for Efficient Transformers](llm_efficiency/zeros_zero-sum_linear_attention_for_efficient_transformers.md)**

:   通过移除 softmax 的零阶均匀项 $1/t$，构建零和权重的线性注意力机制 ZeroS，突破凸组合只能做加法混合的限制，支持单层内的差分/对比操作，在保持 $O(Nd^2)$ 线性复杂度的同时，在多个序列建模基准上匹配甚至超越标准 softmax 注意力。

---

## 🦾 LLM Agent { #llm_agent }

**[A-MEM: Agentic Memory for LLM Agents](llm_agent/a-mem_agentic_memory_for_llm_agents.md)**

:   提出 A-Mem，一种受 Zettelkasten 启发的 LLM Agent 智能记忆系统，每条记忆自动生成结构化笔记（关键词/标签/上下文描述），动态建立记忆间链接，并在新记忆加入时触发旧记忆的演化更新，在 LoCoMo 长对话 QA 上显著超越 MemGPT 等基线。

**[A Differentiable Model of Supply-Chain Shocks](llm_agent/a_differentiable_model_of_supply-chain_shocks.md)**

:   本文用 JAX 实现了一个可微分的供应链 Agent-Based Model（ABM），通过 GPU 并行化和自动微分实现了比传统无梯度方法快 3 个数量级的贝叶斯参数校准，为大规模供应网络建模打开了可能性。

**[A Self-Improving Coding Agent](llm_agent/a_selfimproving_coding_agent.md)**

:   提出SICA（Self-Improving Coding Agent），一个能自主编辑自身代码库来提升性能的编程Agent——消除了meta-agent和target-agent的区分，通过迭代式自我改进在SWE-Bench Verified子集上从17%提升到53%。

**[Adaptive Cooperative Transmission Design for URLLC via Deep Reinforcement Learning](llm_agent/adaptive_cooperative_transmission_design_for_ultra-reliable_low-latency_communic.md)**

:   针对两跳协作中继通信中的URLLC难题，提出DRL-CoLA算法：将每跳传输参数配置建模为MDP，用双agent DQN在仅观测本地CSI和ARQ反馈下学习分布式时延感知传输策略，接近全局最优可靠性。

**[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](llm_agent/agentauditor_humanlevel_safety_and_security_evaluation_for_l.md)**

:   提出 AgentAuditor，一个通用的无训练记忆增强推理框架，使 LLM 评估者能模拟人类专家评估 agent 的安全与安全性——通过自适应提取结构化语义特征并生成CoT推理轨迹构建经验记忆，多阶段上下文感知 RAG 检索相关经验指导新案例评估，在自建的 ASSEBench（2293条记录×15类風险×29场景）上达到人类水平准确率。

**[AgentChangeBench: A Multi-Dimensional Evaluation Framework for Goal-Shift Robustness](llm_agent/agentchangebench_a_multi-dimensional_evaluation_framework_for_goal-shift_robustn.md)**

:   AgentChangeBench 是首个系统评估 LLM agent 在对话中途目标切换时适应能力的 benchmark：315 基础任务 × 9 变体 = 2835 序列，覆盖 3 个企业领域（银行/零售/航空）和 5 种 user persona，引入 GSRT（目标切换恢复时间）等 4 个互补指标，揭示高 pass@k 掩盖的效率和鲁棒性差距——如 GPT-4o 航空恢复率 92.2% 但零售冗余率达 89.1%。

**[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](llm_agent/agentdam_privacy_leakage_evaluation_for_autonomous_web_agent.md)**

:   提出 AgentDAM，首个在真实 Web 环境中端到端评估 AI Agent 数据最小化能力的基准，包含 246 个跨 Reddit/GitLab/Shopping 的任务，发现 GPT-4o 等主流模型在无缓解措施时隐私泄露率高达 36-46%，而 CoT 隐私提示可将泄露率降至 6-8%。

**[Agentic NL2SQL to Reduce Computational Costs](llm_agent/agentic_nl2sql_to_reduce_computational_costs.md)**

:   提出 Datalake Agent，一个基于交互循环的 agentic NL2SQL 系统，通过分层的信息获取策略（GetDBDescription -> GetTables -> GetColumns -> DBQueryFinalSQL）让 LLM 按需请求数据库 schema 信息而非一次性接收全部，在 319 张表的场景下将 token 使用量减少 87%、成本降低 8 倍，同时在复杂查询上保持更好的性能。

**[Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](llm_agent/agentic_plan_caching_test-time_memory_for_fast_and_cost-efficient_llm_agents.md)**

:   提出 Agentic Plan Caching (APC)——从 agent 执行日志中提取结构化计划模板，通过关键词匹配缓存命中后用小模型适配复用，平均降低 50.31% 成本和 27.28% 延迟，同时保持 96.61% 的最优准确率。

**[AgentMisalignment: Measuring the Propensity for Misaligned Behaviour in LLM-Based Agents](llm_agent/agentmisalignment_measuring_the_propensity_for_misaligned_behaviour_in_llm-based.md)**

:   提出 AgentMisalignment 基准套件，包含 9 个现实场景评估任务，测量 LLM Agent 在非恶意指令下 **自发偏离** 部署者意图的倾向（而非能力），发现更强的模型倾向于更高的错误对齐，且人格提示（persona prompt）有时比模型选择本身对错误对齐行为的影响更大。

**[AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks](llm_agent/agenttts_large_language_model_agent_for_testtime_computeopti.md)**

:   提出 AgentTTS，一个用 LLM agent 自动搜索多阶段复杂任务中**测试时计算最优缩放策略**（模型选择+预算分配）的框架，通过迭代反馈驱动的交互显著提升搜索效率和性能。

**[Are Large Language Models Sensitive to the Motives Behind Communication?](llm_agent/are_large_language_models_sensitive_to_the_motives_behind_communication.md)**

:   系统评估 LLM 对通信动机的敏感性（motivational vigilance）——在控制实验中 LLM 能像人类一样折扣有偏见信源的建议（与理性模型相关系数 r>0.78），但在真实场景（YouTube 赞助广告）中表现大幅下降（r<0.2），通过简单的 prompt steering 可部分恢复。

**[Attractive Metadata Attack: Inducing LLM Agents to Invoke Malicious Tools](llm_agent/attractive_metadata_attack_inducing_llm_agents_to_invoke_malicious_tools.md)**

:   AMA（Attractive Metadata Attack）证明仅通过精心设计恶意工具的元数据（名称、描述、参数模式），不需要提示注入或模型内部访问，就能诱导 LLM Agent 以 81-95% 的成功率调用攻击者工具并泄露隐私，同时几乎不影响原始任务完成（98%+），且现有防御（审计器、提示重写）效果有限。

**[Automated Composition of Agents: A Knapsack Approach for Agentic Component Selection](llm_agent/automated_composition_of_agents_a_knapsack_approach_for_agentic_component_select.md)**

:   将 Agent 组件选择问题形式化为在线背包问题，提出 Composer Agent 框架：通过沙盒实测（而非静态语义检索）评估组件真实能力，结合 ZCL 在线算法在预算约束下动态选取最优组件组合，单 Agent 工具选择成功率提升最高 31.6%，多 Agent 子代理选择成功率从 37% 跃升至 87%。

**[VeriMaAS: Automated Multi-Agent Workflows for RTL Design](llm_agent/automated_multi-agent_workflows_for_rtl_design.md)**

:   VeriMaAS 提出自动组合 agent 工作流的框架用于 RTL 代码生成——关键创新是将 HDL 工具的形式化验证反馈直接整合到工作流生成中，无需梯度更新或长推理链，在 pass@k 上超过微调基线 5-7%，且训练样本需求降低一个量级。

**[Benchmarking Agentic Systems in Automated Scientific Information Extraction with ChemX](llm_agent/benchmarking_agentic_systems_in_automated_scientific_information_extraction_with.md)**

:   构建 ChemX——10 个由领域专家手工标注和验证的多模态化学数据提取基准数据集，涵盖纳米材料和小分子两大领域，系统评估了 ChatGPT Agent、SLM-Matrix、FutureHouse、nanoMINER 等 SOTA Agent 系统以及 GPT-5/GPT-5 Thinking 等前沿 LLM；提出的单 Agent 方法通过结构化文档预处理（marker-pdf → Markdown → LLM 提取）在纳米酶数据集上达到 F1=0.61，超越所有通用多 Agent 系统，同时揭示了化学信息提取仍存在 SMILES 解析失败、术语歧义等系统性挑战。

**[BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](llm_agent/btlui_blinkthinklink_reasoning_model_for_gui_agent.md)**

:   提出"Blink-Think-Link"（BTL）脑启发框架模拟人类与GUI交互的认知过程——分解为Blink（快速注意力检测，类似眼跳）、Think（高级推理决策，类似认知规划）、Link（生成可执行命令，类似动作选择）三个生物合理阶段，配合自动化Blink数据标注和首个基于规则的过程+结果复合奖励机制，BTL-UI在静态GUI理解和动态交互任务上均达competitive性能。

**[CAM: A Constructivist View of Agentic Memory for LLM-Based Reading Comprehension](llm_agent/cam_a_constructivist_view_of_agentic_memory_for_llm-based_reading_comprehension.md)**

:   受皮亚杰建构主义理论启发，提出CAM——一种具有结构性（层次化schema）、灵活性（重叠聚类的同化）和动态性（增量适应）三大特征的智能体记忆系统，在6个长文本阅读理解任务上全面超越RAPTOR、GraphRAG等基线。

**[ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions](llm_agent/contextagent_context-aware_proactive_llm_agents_with_open-world_sensory_percepti.md)**

:   提出 ContextAgent，首个利用可穿戴设备多模态感知（视频+音频+通知）来理解用户意图并主动提供工具增强服务的 LLM Agent 框架，同时构建了包含 1000 个样本的 ContextAgentBench 基准，在主动预测准确率和工具调用上分别提升 8.5% 和 6.0%。

**[CORE: Full-Path Evaluation of LLM Agents Beyond Final State](llm_agent/core_full-path_evaluation_of_llm_agents_beyond_final_state.md)**

:   提出CORE框架：用确定有限自动机（DFA）编码Agent任务的合法工具调用路径，引入5个互补指标（路径正确性、顺序正确性、前缀危险性、有害调用率、效率）从全路径而非仅终态评估Agent行为，揭示了传统终态评估中不可见的安全和效率差异。

**[Crucible: Quantifying the Potential of Control Algorithms through LLM Agents](llm_agent/crucible_quantifying_the_potential_of_control_algorithms_through_llm_agents.md)**

:   首次提出"调优潜能"（Tuning Potential）概念并给出形式化度量，通过 LLM Agent 模拟不同能力水平的开发者对控制算法进行参数调优和逻辑级改进，在 ABR 任务上相比贝叶斯优化提升 44.1%，CartPole 上 Bang-bang 从 34→500 达到 DQN 水平。

**[Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](llm_agent/debate_or_vote_which_yields_better_decisions_in_multi-agent_large_language_model.md)**

:   通过理论和实验证明，多智能体辩论（MAD）的性能提升主要来自多数投票（ensembling）而非辩论本身——辩论过程构成 martingale（期望不变），即辩论不系统性地提升正确率，并基于此理论提出通过偏向正确信号来改进 MAD。

**[Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding](llm_agent/deep_video_discovery_agentic_search_with_tool_use_for_longfo.md)**

:   提出 DVD（Deep Video Discovery）agent，将长视频理解建模为多步信息搜索问题：先将长视频构建为多粒度结构化数据库（全局摘要 + clip 级字幕嵌入 + 帧级像素），再提供三种搜索工具（Global Browse / Clip Search / Frame Inspect），由 reasoning LLM 通过 observe-reason-act 循环自主编排搜索轨迹，在 LVBench 达 74.2%（超先前 SOTA MR.Video 13.4 pp），加字幕 76.0%。

**[DefenderBench: A Toolkit for Evaluating Language Agents in Cybersecurity Environments](llm_agent/defenderbench_a_toolkit_for_evaluating_language_agents_in_cybersecurity_environm.md)**

:   提出 DefenderBench，一个开源模块化工具包，用于在攻防和知识理解三类网络安全任务上系统评估 LLM Agent 的能力，覆盖网络入侵模拟、恶意内容检测、代码漏洞检测/修复、CTI 知识问答五大场景，基准测试显示 Claude-3.7-sonnet 综合最强（81.65 分）。

**[Distilling LLM Agent into Small Models with Retrieval and Code Tools](llm_agent/distilling_llm_agent_into_small_models_with_retrieval_and_co.md)**

:   提出 Agent Distillation 框架，将 LLM agent 的完整 reason-act-observe 交互行为（而非静态 CoT）蒸馏到 0.5B-7B 小模型中，配合 first-thought prefix 提升教师轨迹质量和 self-consistent action generation 提升推理鲁棒性，使小模型达到比其大 2-4× 的 CoT 蒸馏模型的性能。

**[DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](llm_agent/drift_dynamic_rulebased_defense_with_injection_isolation_for.md)**

:   提出 DRIFT 系统级 Agent 安全框架，通过 Secure Planner（预规划函数轨迹+参数检查表）、Dynamic Validator（基于 Read/Write/Execute 权限的动态策略更新）和 Injection Isolator（从 memory stream 中检测并屏蔽注入指令）三层防御，在 AgentDojo 上将 ASR 从 30.7% 降至 1.3%，同时比 CaMeL 提升 20.1% utility。

**[Enhancing Demand-Oriented Regionalization with Agentic AI and Local Heterogeneous Data for Adaptation Planning](llm_agent/enhancing_demand-oriented_regionalization_with_agentic_ai_and_local_heterogeneou.md)**

:   本文提出一个基于 Agentic AI 的规划支持系统，通过 LLM 智能体引导非技术用户进行数据驱动的需求导向区域化（demand-oriented regionalization），核心算法为 RepSC-SOM（带代表性初始化的空间约束自组织映射），支持人机协作迭代优化区域划分，用于灾害风险管理和气候适应规划。

**[EU-Agent-Bench: Measuring Illegal Behavior of LLM Agents Under EU Law](llm_agent/eu-agent-bench_measuring_illegal_behavior_of_llm_agents_under_eu_law.md)**

:   提出 EU-Agent-Bench，首个基于欧盟法律框架的可验证智能体基准，通过 600 个良性用户请求测试 LLM 智能体的工具调用是否违反欧盟法规，发现即使最佳模型（Gemini 2.5 Flash）的合法率也仅约 55%，揭示了当前对齐技术与法律可靠性之间的巨大鸿沟。

**[Evaluating LLMs in Open-Source Games](llm_agent/evaluating_llms_in_open-source_games.md)**

:   通过开源游戏（智能体提交程序而非原始行动）这一新范式，系统评估 LLM 在战略推理、互相学习和合作博弈中的能力，发现 LLM 可自动发现近似程序平衡。

**[Generative AI Agents for Controllable and Protected Content Creation](llm_agent/generative_ai_agents_for_controllable_and_protected_content_creation.md)**

:   提出一个多智能体生成框架，通过 Director/Planner、Generator、Reviewer、Integration 和 Protection 五个专业化智能体的协作，结合人在环反馈，统一解决生成内容的可控性和版权保护问题。

**[Ground-Compose-Reinforce: Grounding Language in Agentic Behaviours using Limited Data](llm_agent/ground-compose-reinforce_grounding_language_in_agentic_behaviours_using_limited_.md)**

:   提出 Ground-Compose-Reinforce (GCR)，一个端到端的神经符号框架，通过少量标注轨迹（仅350条）学习原子命题的接地语义（Ground），将其通过 Reward Machine 组合成复杂任务规范（Compose），然后用自生成的稠密奖励训练 RL 智能体（Reinforce），无需手工奖励函数即可引出分布外的复杂行为。

**[Group-in-Group Policy Optimization for LLM Agent Training](llm_agent/groupingroup_policy_optimization_for_llm_agent_training.md)**

:   GiGPO 通过在 GRPO 的 episode 级分组内嵌套 step 级分组（利用跨轨迹的重复环境状态作为 anchor state），实现了无需额外 rollout 和 critic 模型的细粒度 credit assignment，在 ALFWorld 上比 GRPO 提升 >12%，WebShop 上提升 >9%。

**[Hogwild! Inference: Parallel LLM Generation via Concurrent Attention](llm_agent/hogwild_inference_parallel_llm_generation_via_concurrent_attention.md)**

:   提出 Hogwild! Inference——一种无需预定义协作框架的并行 LLM 推理协议，多个 LLM 实例通过共享的并发 KV 缓存实时同步，利用 RoPE 位置编码避免重计算，在数学推理和编程任务上以更少的串行步骤达到更高精度。

**[It's LIT! Reliability-Optimized LLMs with Inspectable Tools](llm_agent/its_lit_reliability-optimized_llms_with_inspectable_tools.md)**

:   通过为每个外部工具定义可靠性/可调试性成本函数，引导 LLM 在多候选方案中选择成本最低（最透明可审计）的工具调用路径，在 61/65 测试场景中提升可解释性的同时保持甚至提升任务准确率。

**[Lessons Learned: A Multi-Agent Framework for Code LLMs to Learn and Improve](llm_agent/lessons_learned_a_multi-agent_framework_for_code_llms_to_learn_and_improve.md)**

:   提出 LessonL 框架，使多个小 LLM 智能体通过相互学习的"课程"(lesson)对成功和失败案例进行反思，协同优化代码性能，3 个 7B-14B 模型组合达到 GPT-4o 甚至接近 o3 的代码优化效果。

**[LLM Agent Communication Protocol (LACP) Requires Urgent Standardization: A Telecom-Inspired Protocol is Necessary](llm_agent/llm_agent_communication_protocol_lacp_requires_urgent_standardization_a_telecom-.md)**

:   这篇 position paper 指出当前 LLM Agent 通信的碎片化生态类似早期网络的"协议战争"，提出受电信标准化启发的三层协议 LACP（语义层、事务层、传输层），强调安全内建、事务完整性和语义互操作性对多智能体系统至关重要。

**[LLM Agents for Knowledge Discovery in Atomic Layer Processing](llm_agent/llm_agents_for_knowledge_discovery_in_atomic_layer_processing.md)**

:   通过让 LLM Agent 控制模拟化学反应器（黑盒函数），证明 Agent 能在无先验知识下通过试错探索、发现并总结未知化学系统的规则，揭示了 Agent 进行开放式科学发现的能力与局限。

**[MAT-Agent: Adaptive Multi-Agent Training Optimization](llm_agent/mat-agent_adaptive_multi-agent_training_optimization.md)**

:   提出 MAT-Agent，一个由四个自主 agent（分别负责数据增强、优化器、学习率调度、损失函数）组成的多智能体框架，在训练过程中动态调整训练配置，用 DQN 学习策略以替代传统静态超参配置，在多标签图像分类任务上实现了 SOTA。

**[MLRC-Bench: Can Language Agents Solve Machine Learning Research Challenges?](llm_agent/mlrc-bench_can_language_agents_solve_machine_learning_research_challenges.md)**

:   基于真实 ML 会议竞赛构建动态基准 MLRC-Bench，评估 LLM Agent 提出和实现新颖研究方法的能力，发现最强 Agent（Gemini）仅达人类顶级方案 9.3% 的相对改进，且提供 AI/人类想法并不能一致改善实现质量。

**[Orchestration Framework for Financial Agents: From Algorithmic Trading to Agentic Trading](llm_agent/orchestration_framework_for_financial_agents_from_algorithmic_trading_to_agentic.md)**

:   提出 FinAgent 编排框架，将传统算法交易系统的各组件映射为 AI 智能体（规划器、编排器、Alpha/风控/组合/回测/执行/审计/记忆智能体），使用 MCP 协议进行控制通信、A2A 协议进行智能体间通信，在股票和 BTC 交易任务上验证了可行性。

**[Out of Control -- Why Alignment Needs Formal Control Theory (and an Alignment Control Stack)](llm_agent/out_of_control_--_why_alignment_needs_formal_control_theory_and_an_alignment_con.md)**

:   本文是一篇 position paper，主张将形式化最优控制理论作为 AI 对齐研究的核心工具，并提出"对齐控制栈"(Alignment Control Stack, ACS)——一个从物理硬件层到社会治理层的十层分层框架，用于系统地组织和分析不同对齐方法的测量、控制与互操作性。

**[Panda Towards Generalist Video Anomaly Detection Via Agentic Ai Engineer](llm_agent/panda_towards_generalist_video_anomaly_detection_via_agentic_ai_engineer.md)**

:   提出 PANDA，一个基于 MLLM 的 Agentic AI 工程师框架，通过自适应场景感知策略规划、目标驱动启发式推理、工具增强自反思和链式记忆四大能力，实现无需训练和人工干预的通用视频异常检测。

**[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](llm_agent/rd-agent-quant_a_multi-agent_framework_for_data-centric_factors_and_model_joint_.md)**

:   提出 R&D-Agent(Q)，一个数据驱动的多智能体框架，通过五个协作模块（Specification、Synthesis、Implementation、Validation、Analysis）自动化量化策略的因子挖掘与模型创新联合优化，在真实股票市场上以不到 $10 的成本实现约 2× 于传统因子库的年化收益。

**[Shapecraft Llm Agents For Structured Textured And Interactive 3D Modeling](llm_agent/shapecraft_llm_agents_for_structured_textured_and_interactive_3d_modeling.md)**

:   提出基于图结构程序化形状表示（GPS）的多 Agent 框架 ShapeCraft，通过 Parser-Coder-Evaluator 三个 LLM Agent 协作，将自然语言分解为结构化子任务图，迭代生成可编辑、可动画的带纹理 3D 资产。

**[SuffixDecoding: Extreme Speculative Decoding for Emerging AI Applications](llm_agent/suffixdecoding_extreme_speculative_decoding_for_emerging_ai_applications.md)**

:   利用后缀树缓存长序列，通过自适应推测长度实现 5.3 倍加速，特别针对 Agent 场景中高度可预测的重复推理任务。

**[T1: A Tool-Oriented Conversational Dataset for Multi-Turn Agentic Planning](llm_agent/t1_a_tool-oriented_conversational_dataset_for_multi-turn_agentic_planning.md)**

:   构建 T1 数据集——13.5K 多轮对话覆盖 9 个领域（4 单领域 + 5 跨领域）、14 个工具，聚焦工具间依赖和动态重规划，并提出 T1-Agent（代码生成 + 缓存机制）作为基线系统；实验发现 SFT 后的 Llama 8B 在 Tool Call F1 上达 87.17%，超越未微调的 70B 模型，但仍落后于 GPT-5/o3 等闭源模型。

**[TAI3: Testing Agent Integrity in Interpreting User Intent](llm_agent/tai3_testing_agent_integrity_in_interpreting_user_intent.md)**

:   提出 TAI3，一个以 API 为中心的 LLM Agent 意图完整性压力测试框架，通过语义分区（Semantic Partitioning）将自然语言输入空间组织为结构化测试网格，再利用意图保持变异（Intent-Preserving Mutation）和策略记忆（Strategy Memory）高效暴露 Agent 在执行用户任务时的意图理解错误。

**[The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement](llm_agent/the_lighthouse_of_language_enhancing_llm_agents_via_critique-guided_improvement.md)**

:   提出 CGI（Critique-Guided Improvement）双角色框架，训练专门的 Critic 模型为 Actor Agent 提供结构化自然语言反馈（判别+修正建议），并通过迭代动作精炼让 Actor 学会利用这些反馈，在 WebShop/ScienceWorld/TextCraft 三个环境中平均得分 74.20%，超越 GPT-4o（45.46%）和 Iterative SFT（58.21%）。

**[Traj-CoA: Patient Trajectory Modeling via Chain-of-Agents for Lung Cancer Risk Prediction](llm_agent/traj-coa_patient_trajectory_modeling_via_chain-of-agents_for_lung_cancer_risk_pr.md)**

:   提出Traj-CoA多agent框架，通过chain-of-agents架构配合EHRMem长期记忆模块对长且噪声的纵向EHR进行时序推理，在零样本肺癌风险预测任务中（5年EHR数据，最高160k tokens）超越ML/DL/BERT/LLM等多类基线。

**[TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration](llm_agent/trajagent_an_llm-agent_framework_for_trajectory_modeling_via_large-and-small_mod.md)**

:   首个 LLM 代理框架自动处理轨迹建模全流程，通过 UniEnv 统一接口和协作学习双层优化（LLM 推理 + 小模型训练），性能相比基线最高提升 69.91%。

**[Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](llm_agent/web-shepherd_advancing_prms_for_reinforcing_web_agents.md)**

:   提出首个针对网页导航的过程奖励模型 Web-Shepherd，通过检查清单分解任务目标为可评估的子目标，3B/8B 模型在轨迹准确率上碾压 GPT-4o（85% vs 10%），同时成本仅为 1/10，使网页 Agent 的强化学习和推理时搜索变得实际可行。

**[What AI Speaks for Your Community: Polling AI Agents for Public Opinion on Data Center Projects](llm_agent/what_ai_speaks_for_your_community_polling_ai_agents_for_public_opinion_on_data_c.md)**

:   提出基于LLM的AI agent民意调研框架，通过人口统计合成虚拟居民agent对数据中心项目进行大规模低成本民调，跨模型跨地区实验表明agent意见与真实民调在主题上高度一致。

**[Zero-Shot Large Language Model Agents for Fully Automated Radiotherapy Treatment Planning](llm_agent/zero-shot_large_language_model_agents_for_fully_automated_radiotherapy_treatment.md)**

:   提出一种基于 LLM Agent 的零样本 (zero-shot) 放射治疗自动计划工作流，LLM 直接与商业治疗计划系统 (Eclipse TPS) 交互，通过迭代提取剂量-体积直方图 (DVH) 和目标函数损失并推理约束调整策略，在 20 例头颈癌 IMRT 病例上实现了与临床手动计划相当甚至更优的剂量分布质量。

---

## ⚖️ 对齐 / RLHF { #llm_alignment }

**[A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs](llm_alignment/a_systematic_evaluation_of_preference_aggregation_in_federated_rlhf_for_pluralis.md)**

:   提出一种自适应 Alpha 聚合策略，在联邦 RLHF 框架中根据各用户群体的历史对齐表现动态调整奖励权重，从而在多元偏好对齐中同时实现高公平性和强对齐性能。

**[Alignment of Large Language Models with Constrained Learning](llm_alignment/alignment_of_large_language_models_with_constrained_learning.md)**

:   将LLM对齐形式化为约束优化问题（最大化主要奖励同时满足次要效用约束如安全性），提出基于拉格朗日对偶的迭代方法交替更新LLM策略和对偶变量，理论上刻画了分布空间与LLM参数空间之间的原对偶间隙和最优性间隙，证明方法可以找到近最优约束LLM策略。

**[Ask a Strong LLM Judge when Your Reward Model is Uncertain](llm_alignment/ask_a_strong_llm_judge_when_your_reward_model_is_uncertain.md)**

:   提出基于不确定性的路由框架，用SNGP对pairwise reward model做不确定性量化，将高认知不确定性的样本路由到强LLM judge（DeepSeek-R1），在仅调用9.2%~42.5% judge的成本下显著超越随机路由的准确率，且有效改善下游在线RLHF对齐效果。

**[Attack via Overfitting: 10-shot Benign Fine-tuning to Jailbreak LLMs](llm_alignment/attack_via_overfitting_10-shot_benign_fine-tuning_to_jailbreak_llms.md)**

:   提出两阶段微调攻击：第一阶段用10个问题配相同拒绝答案使LLM过拟合到窄最优解（尖锐loss landscape），第二阶段用相同10个问题配正常答案触发灾难性遗忘——安全对齐被"忘掉"，仅用完全良性数据即达94.84%越狱成功率，与恶意微调（97.25%）相当且完全绕过审核模型。

**[Can DPO Learn Diverse Human Values? A Theoretical Scaling Law](llm_alignment/can_dpo_learn_diverse_human_values_a_theoretical_scaling_law.md)**

:   建立了 DPO 在多元人类价值设定下的理论泛化框架——通过分析有限梯度步后 reward margin 的动态轨迹，证明了每种价值所需样本量必须随价值类别数 $K$ 对数增长（$Q = \Theta(\log K)$）才能维持泛化性能，揭示了对齐多元化社会价值的统计代价。

**[Capturing Individual Human Preferences with Reward Features](llm_alignment/capturing_individual_human_preferences_with_reward_features.md)**

:   提出奖励特征模型（RFM）：学习共享奖励特征 $\phi_\theta(x,y)$，每个用户通过线性权重 $\mathbf{w}_h$ 组合这些特征得到个性化奖励 $r_h = \langle \phi_\theta, \mathbf{w}_h \rangle$，并首次给出多评价者偏好学习的PAC泛化界，证明增加评价者数 $m$ 比增加每人样本数 $n$ 更有效，仅30个样本即可快速适应新用户。

**[Concept-Level Explainability for Auditing & Steering LLM Responses](llm_alignment/concept-level_explainability_for_auditing_steering_llm_responses.md)**

:   提出 ConceptX，一种基于概念级（而非 token 级）Shapley 归因的 LLM 可解释性方法，通过语义相似度而非 token 重合度来衡量输入概念对输出的影响，可用于审计偏见和通过 prompt 编辑引导 LLM 输出，在越狱防御中将攻击成功率从 0.463 降至 0.242。

**[Deep Research Brings Deeper Harm](llm_alignment/deep_research_brings_deeper_harm.md)**

:   揭示 Deep Research (DR) 智能体的严重安全隐患——即使底层 LLM 能正确拒绝有害请求，部署为 DR 智能体后仍能生成详细专业的危险报告；提出 Plan Injection 和 Intent Hijack 两种针对性越狱方法，以及 DeepREJECT 评估指标，在 6 个 LLM 上验证了 DR 智能体系统性地削弱了对齐机制。

**[DeepVideo-R1: Video Reinforcement Fine-Tuning via Difficulty-aware Regressive GRPO](llm_alignment/deepvideor1_video_reinforcement_finetuning_via_difficultyawa.md)**

:   探索GRPO在VideoLLM中的应用，发现"安全门依赖"和"优势消失"两个阻碍有效学习的问题，提出Reg-GRPO（将GRPO loss重建为直接回归优势值的任务，消除clipping/min等安全门操作）和难度感知数据增强策略，在多个视频推理benchmark上显著提升性能。

**[DenseDPO: Fine-Grained Temporal Preference Optimization for Video Diffusion Models](llm_alignment/densedpo_finegrained_temporal_preference_optimization_for_vi.md)**

:   提出 DenseDPO，通过三个创新解决视频扩散模型 DPO 训练的根本缺陷：(1) 从 GT 视频加噪去噪构造对齐的视频对消除运动偏差，(2) 在短时间片段而非整个视频上标注偏好提供更密集的学习信号，(3) 用 GPT 等 VLM 自动标注片段级偏好取代人工标注。仅用 1/3 标注数据即大幅提升运动生成质量。

**[Diffusion Model as a Noise-Aware Latent Reward Model for Step-Level Preference Optimization](llm_alignment/diffusion_model_as_a_noiseaware_latent_reward_model_for_step.md)**

:   提出 Latent Reward Model (LRM) 和 Latent Preference Optimization (LPO)，将预训练扩散模型本身复用为噪声感知的潜空间奖励模型，在噪声潜在空间直接进行步级偏好优化，相比 Diffusion-DPO 实现 10-28× 训练加速，相比 SPO 实现 2.5-3.5× 加速。

**[DP²O-SR: Direct Perceptual Preference Optimization for Real-World Image Super-Resolution](llm_alignment/dp2o-sr_direct_perceptual_preference_optimization_for_real-world_image_super-res.md)**

:   提出 DP²O-SR 框架，利用扩散模型固有的随机性生成多样化超分辨率输出，通过混合感知奖励构建偏好对，并设计层次化偏好优化（HPO）策略自适应加权训练对，在无需人工标注的前提下显著提升真实世界图像超分辨率的感知质量。

**[From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring](llm_alignment/from_judgment_to_interference_early_stopping_llm_harmful_outputs_via_streaming_c.md)**

:   提出 Streaming Content Monitor (SCM)——首个原生支持部分检测的流式有害内容监控器，通过 FineHarm 数据集（29K 样本含 token 级标注）和层次一致性感知学习，平均仅需看到 18% 的 response tokens 即可达到 0.95+ macro F1，实现对 LLM 有害输出的实时早停。

**[g-DPO: Scalable Preference Optimization for Protein Language Models](llm_alignment/g-dpo_scalable_preference_optimization_for_protein_language_models.md)**

:   针对蛋白质语言模型（PLM）应用 DPO 时偏好对数量随样本数二次增长导致训练不可扩展的问题，提出 g-DPO 框架：(1) 通过序列空间 union mask 聚类剪枝冗余偏好对，保留局部邻域中信息量更大的比较；(2) 利用共享 union mask 的分组似然摊销，一次前向传播同时计算组内所有序列的 log-likelihood。在三个蛋白质工程任务上，g-DPO 保持与标准 DPO 统计上不可区分的 in silico 和 in vitro 性能，同时实现 1.7-5.4× 的训练加速。

**[Gasp Efficient Black-Box Generation Of Adversarial Suffixes For Jailbreaking Llm](llm_alignment/gasp_efficient_black-box_generation_of_adversarial_suffixes_for_jailbreaking_llm.md)**

:   提出GASP框架，通过训练专用的SuffixLLM生成可读的对抗后缀，利用潜在贝叶斯优化（LBO）在连续嵌入空间中高效搜索并用ORPO迭代微调生成器，在完全黑盒设置下实现高攻击成功率且生成的后缀保持人类可读性。

**[Generalizing while Preserving Monotonicity in Comparison-based Preference Learning Models](llm_alignment/generalizing_while_preserving_monotonicity_in_comparison-based_preference_learni.md)**

:   提出 **Linear GBT with Diffusion Prior**，一类在保证**单调性**（偏好比较后被偏好方的分数不会反常下降）的同时能**泛化到未比较数据**的偏好学习模型，首次正面回答了"泛化与单调性能否兼得"的核心问题。

**[Greedy Sampling Is Provably Efficient For Rlhf](llm_alignment/greedy_sampling_is_provably_efficient_for_rlhf.md)**

:   证明了在KL正则化的RLHF设置下，直接使用经验估计的贪心采样（无需构建乐观/悲观估计）就能在在线和离线两种设置中实现$O(\log T)$遗憾界和$O(\varepsilon^{-1})$样本复杂度，这是首次在一般偏好模型下达到这些阶数。

**[GVPO: Group Variance Policy Optimization for Large Language Model Post-Training](llm_alignment/gvpo_group_variance_policy_optimization_for_large_language_model_post-training.md)**

:   通过将 KL 约束奖励最大化的解析解融入梯度权重（零和权重消除配分函数），设计了比 GRPO 更稳定的 LLM 后训练方法 GVPO，在 AIME 上达到 20.72%（GRPO 14.79%），并证明具有唯一全局最优解。

**[HelpSteer3-Preference: Open Human-Annotated Preference Data across Diverse Tasks and Languages](llm_alignment/helpsteer3-preference_open_human-annotated_preference_data_across_diverse_tasks_.md)**

:   NVIDIA 发布的 40K+ 开源人工标注偏好数据集，覆盖通用/STEM/代码/多语言（13 种语言），训练的奖励模型在 RM-Bench 上达 82.4%（+10%），CC-BY-4.0 许可对商业友好。

**[Human-assisted Robotic Policy Refinement via Action Preference Optimization](llm_alignment/human-assisted_robotic_policy_refinement_via_action_preference_optimization.md)**

:   提出 Action Preference Optimization (APO)，通过人机协作框架收集交互轨迹，利用基于前景理论的二元期望信号和自适应重加权方法对 VLA 模型进行偏好对齐优化，使其能从失败中学习并持续迭代改进。

**[IF-GUIDE: Influence Function-Guided Detoxification of LLMs](llm_alignment/if-guide_influence_function-guided_detoxification_of_llms.md)**

:   提出 IF-Guide，利用影响函数在 token 粒度识别训练数据中的有毒内容，并通过惩罚式训练目标在预训练/微调阶段主动抑制模型学习有毒行为，显著优于 DPO 和 RAD 等被动对齐方法。

**[Improving Consistency in Retrieval-Augmented Systems with Group Similarity Rewards](llm_alignment/improving_consistency_in_retrieval-augmented_systems_with_group_similarity_rewar.md)**

:   提出 Con-RAG 框架，通过 Paraphrased Set GRPO (PS-GRPO) 在语义等价查询的多次生成之间计算组相似度奖励，训练 RAG 系统的生成器在释义输入下产生信息一致的输出，无需显式真实标签监督即可同时提升一致性和准确性。

**[Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay](llm_alignment/improving_data_efficiency_for_llm_reinforcement_fine-tuning_through_difficulty-t.md)**

:   提出两种互补技术提升 LLM 强化微调（GRPO）的数据效率：(1) DOTS——基于注意力机制预测自适应难度，优先选择中等难度问题以最大化梯度信号；(2) Rollout Replay——复用近期 rollout 降低每步计算开销。两者结合在 6 个模型-数据集组合上平均减少 40.7% 训练时间。

**[Inference-time Alignment in Continuous Space](llm_alignment/inference-time_alignment_in_continuous_space.md)**

:   提出 Simple Energy Adaptation (SEA)，将推理时对齐从"离散空间搜索"范式转变为"连续空间优化"范式，通过在连续 logit 空间上进行基于梯度的 Langevin 采样来逼近 RLHF 最优策略，在 AdvBench 上相对最优基线提升 77.51%，在 MATH 上提升 16.36%。

**[Jailbreak-Zero: A Path to Pareto Optimal Red Teaming for Large Language Models](llm_alignment/jailbreak-zero_a_path_to_pareto_optimal_red_teaming_for_large_language_models.md)**

:   提出基于策略（而非示例）的 LLM 红队评估框架和 Jailbreak-Zero 方法，通过简单的大规模并行采样策略（无需人工越狱策略），在 HarmBench 上对 GPT-4o 和 Claude 3.5 分别达到 99.5% 和 96.0% 的攻击成功率，同时通过微调实现覆盖率、多样性和保真度三个目标的 Pareto 最优。

**[KL Penalty Control via Perturbation for Direct Preference Optimization](llm_alignment/kl_penalty_control_via_perturbation_for_direct_preference_optimization.md)**

:   提出 ε-DPO，通过观察训练时扰动 β 后 logit 作为偏好模型的单调性，实现实例级自适应 KL 惩罚控制，无需额外计算开销即可显著超越 DPO 及大多数直接对齐算法，在 AlpacaEval 2 上达到 46.4% LC win rate（DPO 仅 40.3%）。

**[LASeR: Learning to Adaptively Select Reward Models with Multi-Armed Bandits](llm_alignment/laser_learning_to_adaptively_select_reward_models_with_multi-armed_bandits.md)**

:   将多个奖励模型（RM）的选择建模为上下文多臂老虎机（LinUCB）问题，在迭代 LLM 训练中自适应地为每个 batch 选择最合适的 RM，在推理、指令跟随和长上下文任务上以 2-3 倍效率优势全面超越 RM 集成和单 RM 基线。

**[Limited Preference Data? Learning Better Reward Model with Latent Space Synthesis](llm_alignment/limited_preference_data_learning_better_reward_model_with_latent_space_synthesis.md)**

:   提出 LENS 框架，通过在 LLM 嵌入的潜在空间中利用 VAE 合成偏好数据对，绕过昂贵的文本生成过程，以极低计算成本（模型缩小 16000 倍、生成速度提升 18 倍）显著提升 reward model 性能。

**[LLM Safety Alignment is Divergence Estimation in Disguise](llm_alignment/llm_safety_alignment_is_divergence_estimation_in_disguise.md)**

:   建立统一理论框架证明 RLHF/DPO/KTO/BCO 等对齐方法本质上是在估计安全分布 $\mathcal{D}^+$ 与不安全分布 $\mathcal{D}^-$ 之间的散度，由此解释了对齐后隐空间分离现象，并提出基于 KL 散度的 KLDO 对齐方法，在 5 个模型上实现最佳鲁棒性。

**[LongVPO: From Anchored Cues to Self-Reasoning for Long-Form Video Preference Optimization](llm_alignment/longvpo_from_anchored_cues_to_selfreasoning_for_longform_vid.md)**

:   提出 LongVPO，一个两阶段 DPO 框架使短上下文 VLM 无需长视频标注即可理解超长视频——阶段1通过锚定短片段构造偏好数据解决位置偏差问题，阶段2通过递归描述+多段推理任务培养跨片段推理能力，仅用 16K 合成样本即超越 SOTA 开源模型。

**[Mechanism Design for LLM Fine-tuning with Multiple Reward Models](llm_alignment/mechanism_design_for_llm_fine-tuning_with_multiple_reward_models.md)**

:   将多方偏好聚合的 RLHF 微调建模为机制设计问题，证明了在社会福利最大化训练规则下各方有动机虚报偏好，并通过扩展 VCG 支付机制实现了占优策略激励相容（DSIC），确保各方如实报告偏好。

**[Mitigating Hallucination Through Theory-Consistent Symmetric Multimodal Preference Optimization](llm_alignment/mitigating_hallucination_through_theory-consistent_symmetric_multimodal_preferen.md)**

:   提出 SymMPO（对称多模态偏好优化），通过对比图像的对称配对偏好学习和偏好边际一致性正则化，解决了现有视觉增强型 DPO 方法中目标函数不严格和间接偏好监督两大局限，在五个幻觉评测基准上取得了一致的性能提升。

**[Multi-Environment POMDPs: Discrete Model Uncertainty Under Partial Observability](llm_alignment/multi-environment_pomdps_discrete_model_uncertainty_under_partial_observability.md)**

:   系统研究了多环境 POMDP（ME-POMDP）——一类共享状态/动作/观测空间但转移、观测和奖励函数可任意不同的 POMDP 集合，目标是找到在最坏情况环境下最大化奖励的鲁棒策略。通过引入对抗信念 POMDP（AB-POMDP）统一建模，并证明其与单侧部分可观测随机博弈（POSG）的等价关系，提出精确（值迭代 + LP）和近似（AB-HSVI）算法。

**[On Extending Direct Preference Optimization to Accommodate Ties](llm_alignment/on_extending_direct_preference_optimization_to_accommodate_ties.md)**

:   将 DPO 中的 Bradley-Terry 偏好模型替换为 Rao-Kupper 和 Davidson 扩展，使偏好优化能够显式建模"平局"数据，避免丢弃模糊偏好对，在翻译和数学推理上获得更好的正则化和性能。

**[ORPO-Distill: Mixed-Policy Preference Optimization for Cross-Architecture LLM Distillation](llm_alignment/orpo-distill_mixed-policy_preference_optimization_for_cross-architecture_llm_dis.md)**

:   提出 ORPO-Distill，将跨架构 LLM 知识蒸馏重新定义为偏好优化问题：使用教师模型生成正样本推理链、学生模型生成负样本推理链，通过 ORPO 对比损失训练，并引入混合策略（mixed-policy）更新学生负样本，在 5 个 QA 基准上一致超越黑盒 KD 基线。

**[PolyJuice Makes It Real: Black-Box, Universal Red Teaming for Synthetic Image Detectors](llm_alignment/polyjuice_makes_it_real_black-box_universal_red_teaming_for_synthetic_image_dete.md)**

:   提出 PolyJuice，首个面向合成图像检测器（SID）的黑盒、图像无关的红队方法，通过在 T2I 模型潜空间中发现并利用"真实感方向"，以通用方式引导生成图像欺骗检测器，成功率高达 84%。

**[Position: The Complexity of Perfect AI Alignment -- Formalizing the RLHF Trilemma](llm_alignment/position_the_complexity_of_perfect_ai_alignment_--_formalizing_the_rlhf_trilemma.md)**

:   形式化提出 RLHF 对齐三难困境：证明没有任何 RLHF 系统能同时实现价值多元代表性、多项式可计算性和对抗鲁棒性——三者至多满足其二，当前实践通过牺牲代表性换取可计算性。

**[Preference Optimization by Estimating the Ratio of the Data Distribution](llm_alignment/preference_optimization_by_estimating_the_ratio_of_the_data_distribution.md)**

:   将 DPO 重新解释为似然比估计（ratio matching）问题，基于 Bregman 散度框架提出 BPO（Bregman Preference Optimization），包含 DPO 为特例的广义损失函数族，并设计了 SBA（Scaled Basu's Power Divergence）实例，在 Llama-3-8B 上实现 55.9% AlpacaEval2 length-controlled win rate 的 SOTA。

**[Provably Efficient Online RLHF with One-Pass Reward Modeling](llm_alignment/provably_efficient_online_rlhf_with_one-pass_reward_modeling.md)**

:   提出一种基于 online mirror descent（OMD）的 one-pass reward modeling 方法，消除了 online RLHF 中需要存储历史数据并重新从头优化的计算瓶颈，实现每次迭代 $\mathcal{O}(1)$ 的时间和存储复杂度，同时在统计效率上也优于 MLE 方法。

**[Rectifying Shortcut Behaviors in Preference-based Reward Learning](llm_alignment/rectifying_shortcut_behaviors_in_preference-based_reward_learning.md)**

:   提出 PRISM（Preference-based Reward Invariance for Shortcut Mitigation），将 reward hacking 统一建模为 shortcut learning 问题，通过群不变核（group-invariant kernels）和随机特征映射近似来同时缓解多种 spurious correlation（冗长性、谄媚、语气等），在 out-of-distribution 偏好数据和下游策略模型上一致提升表现。

**[Reinforcement Learning Finetunes Small Subnetworks in Large Language Models](llm_alignment/reinforcement_learning_finetunes_small_subnetworks_in_large_language_models.md)**

:   RL 微调 LLM 时实际上只更新了 5%-30% 的参数（稀疏子网络），且该子网络在不同种子、数据和算法间具有高度一致性，仅微调子网络即可复现完整微调的模型性能甚至参数值。

**[Robust LLM Alignment via Distributionally Robust Direct Preference Optimization](llm_alignment/robust_llm_alignment_via_distributionally_robust_direct_preference_optimization.md)**

:   通过分布鲁棒优化（DRO）框架提出 WDPO（Wasserstein）和 KLDPO（KL散度）两种鲁棒 DPO 变体，解决用户偏好分布转移导致的对齐失败问题，提供 $O(n^{-1/4})$ 收敛保证，在多维对齐任务和 OpenLLM 榜单上显著优于标准 DPO。

**[SafePTR: Token-Level Jailbreak Defense in Multimodal LLMs via Prune-then-Restore Mechanism](llm_alignment/safeptr_token-level_jailbreak_defense_in_multimodal_llms_via_prune-then-restore_.md)**

:   通过分析多模态 LLM 中有害 token 的传播机制，发现不到 1% 的 token 在早期-中间层引发越狱行为，由此提出无需训练的 SafePTR 框架，在脆弱层剪枝有害 token 并在后续层恢复良性特征，显著提升安全性而不牺牲任务性能。

**[SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](llm_alignment/safevla_towards_safety_alignment_of_vision-language-action_model_via_constrained.md)**

:   首次系统性地将安全强化学习（SafeRL）的 CMDP 框架应用于视觉-语言-动作模型（VLA）的安全对齐，通过建模-激发-约束-保证四阶段集成安全方法（ISA），在移动操作任务上实现 83.58% 的安全违规成本下降同时保持任务性能（+3.85%）。

**[Self-alignment of Large Video Language Models with Refined Regularized Preference Optimization](llm_alignment/self-alignment_of_large_video_language_models_with_refined_regularized_preferenc.md)**

:   提出 RRPO（Refined Regularized Preference Optimization），通过子序列级细粒度奖励和 token 级 KL 正则化替代 DPO 的响应级奖励，结合自对齐数据生成框架，在视频理解任务上减少幻觉、提升时间推理能力。

**[Short-length Adversarial Training Helps LLMs Defend Long-length Jailbreak Attacks](llm_alignment/short-length_adversarial_training_helps_llms_defend_long-length_jailbreak_attack.md)**

:   理论证明并实验验证：防御长度 $\Theta(M)$ 的后缀越狱攻击，只需要在长度 $\Theta(\sqrt{M})$ 的对抗后缀上做对抗训练即可，即"短对抗训练防长越狱"——在5个主流LLM上，20 token 对抗训练可将 120 token 越狱成功率降低至少 30%。

**[Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning](llm_alignment/simplicity_prevails_rethinking_negative_preference_optimization_for_llm_unlearni.md)**

:   发现 NPO（负偏好优化）中的参考模型偏差导致遗忘数据的优化功率分配不均和早期梯度权重平滑失效，提出 SimNPO 通过去除参考模型依赖并采用长度归一化奖励，在 TOFU 上将 FQ 从 0.79 提升至 0.99，在所有基准上一致优于 NPO。

**[Strategyproof Reinforcement Learning from Human Feedback](llm_alignment/strategyproof_reinforcement_learning_from_human_feedback.md)**

:   首次从机制设计角度研究 RLHF 中多标注者策略性操纵问题，证明了策略防操纵（strategyproofness）与政策对齐之间存在根本性权衡，并提出 Pessimistic Median of MLEs 算法实现近似策略防操纵。

**[T-SHIRT: Token-Selective Hierarchical Data Selection for Instruction Tuning](llm_alignment/t-shirt_token-selective_hierarchical_data_selection_for_instruction_tuning.md)**

:   提出 T-SHIRT 数据选择框架，通过 Selective IFD（仅考虑有信息量的 token）和分层选择策略（偏好邻域一致性高的样本），用 5% 数据微调即可超越全量数据训练，同时仅需 GPT-2 和单 GPU 40 分钟完成选择。

**[Towards Understanding Safety Alignment: A Mechanistic Perspective from Safety Neurons](llm_alignment/towards_understanding_safety_alignment_a_mechanistic_perspective_from_safety_neu.md)**

:   通过机制可解释性视角发现 LLM 中约 5% 的稀疏"安全神经元"，仅修补（patching）这些神经元的激活即可恢复 90% 以上的安全性能，并从神经元重叠角度解释了 alignment tax 现象。

**[Trajectory Bellman Residual Minimization: A Simple Value-Based Method for LLM Reasoning](llm_alignment/trajectory_bellman_residual_minimization_a_simple_value-based_method_for_llm_rea.md)**

:   TBRM 通过最小化轨迹级贝尔曼残差，将 LLM 输出 logits 视为隐式 Q 值，仅需每个 prompt 一次前向采样即可训练，复杂度远低于 PPO/GRPO 但数学推理性能相当或更优。

**[What Makes a Reward Model a Good Teacher? An Optimization Perspective](llm_alignment/what_makes_a_reward_model_a_good_teacher_an_optimization_perspective.md)**

:   从优化理论角度证明：奖励模型的准确率（accuracy）不足以衡量其作为 RLHF "教师"的质量——即使完美准确的奖励模型，如果诱导的奖励方差（reward variance）过低，也会导致 RLHF 目标函数景观平坦，使 policy gradient 优化极慢；不同的语言模型需要不同的奖励模型。

---

## 🧑 人体理解 { #human_understanding }

**[A Differential and Pointwise Control Approach to Reinforcement Learning](human_understanding/a_differential_and_pointwise_control_approach_to_reinforceme.md)**

:   将RL问题通过连续时间控制的微分对偶形式重新表述，利用哈密顿结构嵌入物理先验，提出dfPO算法实现逐点策略优化，在科学计算任务（曲面建模、网格控制、分子动力学）上以更少样本超越12个RL基线。

**[A Practical Guide for Incorporating Symmetry in Diffusion Policy](human_understanding/a_practical_guide_for_incorporating_symmetry_in_diffusion_policy.md)**

:   本文提出了一套将对称性融入扩散策略的实用指南——通过不变性表征（相对轨迹动作 + 手眼感知）、等变视觉编码器和 Frame Averaging 三种简单方法，在 MimicGen 12 个任务上达到了接近甚至超越完全等变扩散策略的性能，同时实现复杂度大幅降低。

**[A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees](human_understanding/a_regularized_newton_method_for_nonconvex_optimization_with.md)**

:   提出一类基于当前与历史梯度构造的新型正则化器，结合带负曲率监测的共轭梯度法求解正则化Newton方程，在不需要Hessian Lipschitz常数先验知识的自适应框架下，首次同时实现了$O(\epsilon^{-3/2})$最优全局迭代复杂度和二次局部收敛速率。

**[A Simple Linear Patch Revives Layer-Pruned Large Language Models](human_understanding/a_simple_linear_patch_revives_layerpruned_large_language_mod.md)**

:   提出 LinearPatch，一种即插即用的轻量修补技术，通过在剪枝界面插入一个融合了 Hadamard 变换（压制 token 级outlier）和通道缩放（对齐通道幅度）的对称矩阵，有效弥合层剪枝后的激活幅度失配问题，在 LLaMA-3-8B 上剪掉 5/32 层后仍保留 94.15% 性能（无训练），加上 30 分钟蒸馏可达 95.16%。

**[Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference](human_understanding/ada-kv_optimizing_kv_cache_eviction_by_adaptive_budget_allocation_for_efficient_.md)**

:   发现现有 KV cache 驱逐方法对所有注意力头均匀分配预算忽略了头间注意力集中度的巨大差异,提出 Ada-KV——首个 head-wise 自适应预算分配策略,将稀疏头的预算重新分配给分散头,理论证明最小化驱逐损失上界,在 29 个数据集上即插即用地提升现有方法。

**[Agint: Agentic Graph Compilation for Software Engineering Agents](human_understanding/agint_agentic_graph_compilation_for_software_engineering_age.md)**

:   提出 Agint，一个将自然语言意图编译为类型化、效果感知的DAG（有向无环图）的 agentic 图编译器，通过六层类型地板（TEXT→TYPED→SPEC→STUB→SHIM→PURE）渐进式精化自然语言为可执行代码，支持中间表示可执行、混合JIT运行时和Unix风格的可组合工具链。

**[BEDLAM 2.0: Synthetic Humans and Cameras in Motion](human_understanding/bedlam20_synthetic_humans_and_cameras_in_motion.md)**

:   BEDLAM 数据集的重大升级版，新增多样化相机运动（合成+手持+头戴设备捕获）、更广的焦距范围（14-400mm）、更多样化体型/发型/鞋子/服装，总计 27K 序列 8M+ 帧，显著提升世界坐标 3D 人体估计的精度。

**[Breaking The Gradient Barrier Unveiling Large Language Models For Strategic Clas](human_understanding/breaking_the_gradient_barrier_unveiling_large_language_models_for_strategic_clas.md)**

:   提出 GLIM（Gradient-free Learning In-context Method），首次利用 LLM 的 In-Context Learning 机制隐式模拟策略分类中的双层优化（特征操纵 + 决策规则优化），无需微调即可在大规模数据上高效完成策略分类任务。

**[BubbleFormer: Forecasting Boiling with Transformers](human_understanding/bubbleformer_forecasting_boiling_with_transformers.md)**

:   提出 BubbleFormer，基于分解时空轴注意力的 Transformer 架构用于预测沸腾动力学——包括难以预测的自主气泡成核事件，配合 BubbleML 2.0 数据集（160+ 高保真仿真），在多种流体、几何和壁面条件下实现准确的沸腾时空过程预测。

**[Consistent Supervised-Unsupervised Alignment for Generalized Category Discovery](human_understanding/consistent_supervised-unsupervised_alignment_for_generalized_category_discovery.md)**

:   提出 NC-GCD 框架，通过预分配固定的 Equiangular Tight Frame (ETF) 原型为已知类和新类建立统一优化目标，结合语义一致性匹配器 (SCM) 稳定跨迭代伪标签分配，在 6 个 GCD 基准上显著提升新类发现精度。

**[Counteractive RL: Rethinking Core Principles for Efficient and Scalable Deep Reinforcement Learning](human_understanding/counteractive_rl_rethinking_core_principles_for_efficient_and_scalable_deep_rein.md)**

:   CoAct TD Learning 颠覆 ε-greedy 的随机探索范式——以概率 ε 选择最小化 $Q(s,a)$ 的动作（而非随机动作）来获取高时间差分信号，理论证明其产生更大 TD 误差，在 Atari 100K 上实现 248% 性能提升，仅需改动 2 行代码且零额外计算。

**[CPEP: Contrastive Pose-EMG Pre-training Enhances Gesture Generalization on EMG Signals](human_understanding/cpep_contrastive_pose-emg_pre-training_enhances_gesture_generalization_on_emg_si.md)**

:   提出 CPEP 框架，通过对比学习将低质量 EMG 信号表征与高质量手部姿态表征对齐，使 EMG 编码器获得姿态感知能力，首次实现从 EMG 信号零样本识别未见手势，分布内手势分类提升 21%、未见手势分类提升 72%。

**[Cycle-Sync: Robust Global Camera Pose Estimation through Enhanced Cycle-Consistent Synchronization](human_understanding/cycle-sync_robust_global_camera_pose_estimation_through_enhanced_cycle-consisten.md)**

:   提出 Cycle-Sync 全局相机位姿估计框架，通过将消息传递最小二乘 (MPLS) 扩展到相机位置估计、引入 Welsch 型鲁棒损失和环一致性加权，在无需 bundle adjustment 的情况下超越了包括完整 SfM pipeline（含 BA）在内的所有基线方法。

**[Data-Juicer 2.0: Cloud-Scale Adaptive Data Processing for and with Foundation Models](human_understanding/data-juicer_20_cloud-scale_adaptive_data_processing_for_and_with_foundation_mode.md)**

:   Data-Juicer 2.0 是面向基础模型的云规模多模态数据处理系统，150+ 跨文本/图像/视频/音频算子，支持自适应分布式执行（Ray/MaxCompute），在 10000+ CPU 核心上高效处理 TB 级数据，已广泛应用于阿里云 PAI 等产品。

**[Decomposition of Small Transformer Models](human_understanding/decomposition_of_small_transformer_models.md)**

:   将 Stochastic Parameter Decomposition (SPD) 扩展到 Transformer，设计适用于序列数据的因果重要性函数和新损失函数，在玩具 induction head 上恢复期望两步电路，在 GPT-2-small 上定位到"高尔夫""篮球"等可解释概念对应的 rank-1 参数子空间。

**[Devfd Developmental Face Forgery Detection By Learning Shared And Orthogonal Lor](human_understanding/devfd_developmental_face_forgery_detection_by_learning_shared_and_orthogonal_lor.md)**

:   提出 DevFD——一种发展式 MoE 架构，用共享 Real-LoRA 建模真实人脸共性、正交 Fake-LoRA 序列逐步建模新伪造类型，并通过将正交梯度集成到正交损失中缓解灾难性遗忘，在持续学习人脸伪造检测中达到最高准确率和最低遗忘率。

**[Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework](human_understanding/discovering_transformer_circuits_via_a_hybrid_attribution_and_pruning_framework.md)**

:   提出混合归因与剪枝框架 HAP，先用快速的边归因修补（EAP）筛选高潜力子图，再在缩小后的搜索空间上运行精确的边剪枝（EP），在 GPT-2 Small 的 IOI 任务上比纯 EP 快 46% 且保持相当的电路忠实度，同时成功保留了 EAP 单独使用时会遗漏的 S-inhibition 头。

**[Distillation Robustifies Unlearning](human_understanding/distillation_robustifies_unlearning.md)**

:   揭示了"蒸馏能使遗忘变得鲁棒"的核心发现——将遗忘后的模型蒸馏到随机初始化的学生网络中能有效丢弃潜在能力，并基于此提出UNDO方法（Unlearn-Noise-Distill-on-Outputs），通过对遗忘模型权重加噪再蒸馏，建立了计算量与鲁棒性之间的可调权衡，在合成任务和WMDP基准上接近从头重训的黄金标准。

**[Distribution Learning Meets Graph Structure Sampling](human_understanding/distribution_learning_meets_graph_structure_sampling.md)**

:   本文建立了高维概率图模型 PAC 学习与图结构高效计数/采样之间的新联系，利用在线学习框架（EWA/RWM）将指数级专家集合的维护问题转化为 DAG 结构的加权采样问题，首次给出了弦图骨架贝叶斯网络的高效 agnostic 学习算法，并将树结构分布的样本复杂度从 O(nk³/ε) 改进到最优的 O(nk²/ε)。

**[Emergent World Beliefs: Exploring Transformers in Stochastic Games](human_understanding/emergent_world_beliefs_exploring_transformers_in_stochastic_games.md)**

:   将LLM涌现世界模型的研究从完全信息游戏（Othello、国际象棋）扩展到不完全信息领域（德州扑克），通过在PHH格式扑克数据上预训练GPT-2并探测其内部激活，证明模型不仅学习了确定性特征（牌型识别~98%准确率），还自发发展了对随机性特征（胜率/equity，相关系数0.59）的内部表示。

**[Evolutionary Learning in Spatial Agent-Based Models for Physical Climate Risk Assessment](human_understanding/evolutionary_learning_in_spatial_agent-based_models_for_physical_climate_risk_as.md)**

:   提出一种整合地理空间气候灾害数据与进化学习机制的Agent-Based Model（ABM），在包含商品-制造-零售三级供应链的简化经济网络上，通过RCP8.5洪水投影模拟2025-2100年的经济响应，证明了进化自适应机制使企业在气候压力下维持显著更高的生产、资本、流动性和就业水平，同时揭示了传统资产级评估无法捕捉的供应链系统性风险。

**[Exploration of Incremental Synthetic Non-Morphed Images for Single Morphing Attack Detection](human_understanding/exploration_of_incremental_synthetic_non-morphed_images_for_single_morphing_atta.md)**

:   系统研究了在单图像变形攻击检测（S-MAD）训练中增量引入合成非变形人脸图像的效果，发现适量的合成数据（~75%增量）可提升跨数据集泛化能力（EER从6.17%降至6.10%），但过度使用或仅用合成数据会导致性能严重退化（EER升至~38%）。

**[Face-Human-Bench: A Comprehensive Benchmark of Face and Human Understanding for Multi-modal Assistants](human_understanding/face-human-bench_a_comprehensive_benchmark_of_face_and_human_understanding_for_m.md)**

:   提出 Face-Human-Bench，首个系统评估多模态大模型人脸与人体理解能力的基准，包含三级能力分类体系（2个L1 × 10个L2 × 18个L3），开发集与测试集各 1800 题，支持中英双语，评测 25 个主流 MLLM 并揭示其与专家模型的显著差距。

**[FACE: A General Framework for Mapping Collaborative Filtering Embeddings into LLM Tokens](human_understanding/face_a_general_framework_for_mapping_collaborative_filtering_embeddings_into_llm.md)**

:   FACE 提出将协同过滤（CF）嵌入通过解纠缠投影 + 残差量化映射为 LLM 预训练 token（描述符），再用对比学习对齐语义，无需微调 LLM 即可实现 CF 嵌入的语义解读和推荐性能增强。

**[FACE: Faithful Automatic Concept Extraction](human_understanding/face_faithful_automatic_concept_extraction.md)**

:   提出 FACE 框架，在非负矩阵分解 (NMF) 中加入 KL 散度正则项，约束概念重建后的激活值保持与原始模型预测一致，从而提取真正忠实于模型决策过程的概念解释，在 ImageNet/COCO/CelebA 上全面超越 CRAFT 和 ICE。

**[Faster Algorithms for Structured John Ellipsoid Computation](human_understanding/faster_algorithm_for_structured_john_ellipsoid_computation.md)**

:   针对对称凸多面体 $P = \{x \in \mathbb{R}^d : -\mathbf{1}_n \leq Ax \leq \mathbf{1}_n\}$ 的 John 椭球计算问题，提出两个快速算法：基于 sketching 的近输入稀疏度算法 $\widetilde{O}(\text{nnz}(A) + d^\omega)$ 每次迭代，和基于树宽的算法 $O(n\tau^2)$ 每次迭代，均显著优于已有最优 $O(nd^2)$。

**[FirstAidQA: A Synthetic Dataset for First Aid and Emergency Response in Low-Connectivity Settings](human_understanding/firstaidqa_a_synthetic_dataset_for_first_aid_and_emergency_response_in_low-conne.md)**

:   构建 FirstAidQA，一个包含 5500 条合成急救问答对的数据集，基于认证急救教材用 ChatGPT-4o-mini 生成，经人工验证，旨在支撑低连接/离线环境下急救 AI 系统的微调训练。

**[GraphChain: Large Language Models for Large-scale Graph Analysis via Tool Chaining](human_understanding/graphchain_large_language_models_for_large-scale_graph_analysis_via_tool_chainin.md)**

:   提出 GraphChain 框架，通过渐进式图蒸馏（RL驱动的工具链序列生成）和结构感知测试时自适应（基于图拓扑指纹的轻量适配器），使 LLM 能像人类探索未知环境一样，通过动态工具链序列逐步分析大规模图数据，平均准确率 84.7% 超越最优基线 20.7%，可扩展至 20 万节点。

**[GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](human_understanding/gui-rise_structured_reasoning_and_history_summarization_for_gui_navigation.md)**

:   提出 GUI-Rise 框架，通过结构化推理（进度估计 + 决策推理）、动作预测和历史摘要三个子任务的联合设计，结合 GRPO 强化学习与历史摘要奖励，显著提升 GUI 导航智能体在跨域场景下的泛化能力。

**[HOI-Dyn: Learning Interaction Dynamics for Human-Object Motion Diffusion](human_understanding/hoi-dyn_learning_interaction_dynamics_for_human-object_motion_diffusion.md)**

:   将人体-物体交互（HOI）生成建模为 Driver-Responder 系统，通过轻量级 Transformer 交互动力学模型显式预测物体对人体动作的响应，利用残差动力学损失在训练时增强因果一致性，同时保持推理效率。

**[Human-Machine Ritual: Synergic Performance through Real-Time Motion Recognition](human_understanding/human-machine_ritual_synergic_performance_through_real-time_motion_recognition.md)**

:   提出一种轻量级实时动作识别系统，利用可穿戴 IMU 传感器 + MiniRocket 时序分类器实现 <50ms 延迟的舞者特定动作识别（96.05% 准确率），通过"具身记忆映射"将舞者的个人动作-声音关联编码到系统中，构建了一种尊重人体表达深度的人机协作表演范式。

**[In-Context Compositional Learning via Sparse Coding Transformer](human_understanding/in-context_compositional_learning_via_sparse_coding_transformer.md)**

:   受稀疏编码启发，将 Transformer 注意力机制重新解释为在编码字典和解码字典上的投影，通过稀疏系数显式表示组合规则，并利用提升方案（lifting scheme）将上下文任务的组合规则迁移到目标任务。

**[Incentivizing Reasoning For Advanced Instruction-Following Of Large Language Mod](human_understanding/incentivizing_reasoning_for_advanced_instruction-following_of_large_language_mod.md)**

:   提出 RAIF，通过 RL+规则中心奖励培养 LLM 在复杂指令（含 And/Chain/Selection/Nested 组合约束）下的深度推理能力：发现 vanilla CoT 对指令跟随有负面影响（因 LLM 只会浅层复述指令），设计 superior CoT enforcement（样本级对比过滤无效推理）+ 行为克隆控制分布偏移，1.5B 模型匹配 8B 性能，7 个 benchmark 平均提升 11.74%。

**[K-DeCore: Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning](human_understanding/k-decore_facilitating_knowledge_transfer_in_continual_structured_knowledge_reaso.md)**

:   提出 K-DeCore 框架，通过知识解耦将结构化知识推理分为任务无关的 schema 过滤和任务特定的 query 构建两阶段，配合双视角记忆构建和结构引导的伪数据合成策略，在固定参数量下实现跨异构 SKR 任务的有效知识迁移。

**[Learning Dense Hand Contact Estimation from Imbalanced Data](human_understanding/learning_dense_hand_contact_estimation_from_imbalanced_data.md)**

:   提出 HACO 框架，通过平衡接触采样（BCS）解决类别不平衡和顶点级类别平衡损失（VCB Loss）解决空间不平衡，首次在 14 个数据集（65.5 万图像）上训练稠密手部接触估计模型，在多种交互场景下达到 SOTA。

**[Learning From Design Procedure To Generate CAD Programs for Data Augmentation](human_understanding/learning_from_design_procedure_to_generate_cad_programs_for_data_augmentation.md)**

:   提出一种受工业设计流程启发的CAD程序数据增强范式，通过向LLM提供参考曲面程序和设计流程描述来引导生成包含B-Spline有机形状的CAD程序，显著缩小了公开CAD数据集与工业级设计在几何复杂度上的差距。

**[Learning Skill-Attributes for Transferable Assessment in Video](human_understanding/learning_skill-attributes_for_transferable_assessment_in_video.md)**

:   提出CrossTrainer方法，通过发现跨运动通用的技能属性（如平衡、控制、手部定位）作为中间表示，训练多模态语言模型从视频中生成可操作反馈和水平评估，在跨运动零样本迁移中相对SOTA提升高达60%。

**[Learning to Watermark: A Selective Watermarking Framework for Large Language Models via Multi-Objective Optimization](human_understanding/learning_to_watermark_a_selective_watermarking_framework_for_large_language_mode.md)**

:   提出LTW（Learning to Watermark）框架，使用一个轻量级选择器网络基于句子嵌入、token熵和当前水印比例来自适应决定何时施加水印，通过多目标优化（MGDA）在可检测性和文本质量之间达到Pareto最优，在不降低检测性能的前提下显著提升水印文本质量。

**[LUMIA: A Handheld Vision-to-Music System for Real-Time, Embodied Composition](human_understanding/lumia_a_handheld_vision-to-music_system_for_real-time_embodied_composition.md)**

:   提出Lumia——一个手持相机式设备，通过GPT-4 Vision分析拍摄画面生成结构化提示，再由Stable Audio合成音乐循环段，实现从视觉到音乐的实时、具身化即兴创作工作流。

**[Mapping Faithful Reasoning in Language Models](human_understanding/mapping_faithful_reasoning_in_language_models.md)**

:   提出Concept Walk框架，通过将推理模型每步的残差流激活投影到从对比数据学到的概念方向上，追踪内部概念表示在推理过程中的演化轨迹，以此区分CoT链是真正参与计算的还是仅为事后合理化的装饰性输出。

**[MDReID: Modality-Decoupled Learning for Any-to-Any Multi-Modal Object Re-Identification](human_understanding/mdreid_modality-decoupled_learning_for_any-to-any_multi-modal_object_re-identifi.md)**

:   提出MDReID框架，通过将模态特征解耦为模态共享（modality-shared）和模态特有（modality-specific）两部分，实现任意模态组合下的目标重识别（any-to-any ReID），在模态匹配和模态不匹配场景下均大幅超越现有方法。

**[Mingle: Mixture of Null-Space Gated Low-Rank Experts for Test-Time Continual Model Merging](human_understanding/mingle_mixture_of_null-space_gated_low-rank_experts_for_test-time_continual_mode.md)**

:   提出测试时持续模型合并(TTCMM)新范式及Mingle框架，通过低秩专家混合架构和自适应零空间约束门控机制，在测试时利用少量无标签样本实现模型动态合并，在多个基准上以7-9%的优势超越SOTA，同时将遗忘降至接近零。

**[Mixing Expert Knowledge: Bring Human Thoughts Back to the Game of Go](human_understanding/mixing_expert_knowledge_bring_human_thoughts_back_to_the_game_of_go.md)**

:   提出 LoGos，通过混合领域专家数据（围棋）与通用长 CoT 推理数据进行冷启动微调 + GRPO 强化学习，使通用 LLM 在围棋中达到职业棋手水平的同时保持优秀的通用推理能力。

**[MOSPA: Human Motion Generation Driven by Spatial Audio](human_understanding/mospa_human_motion_generation_driven_by_spatial_audio.md)**

:   首次提出空间音频驱动的人体运动生成：构建 SAM 数据集（9+ 小时 Ambisonics 空间音频-运动配对数据），设计 MOSPA 扩散模型框架融合空间位置信息 + 语义音频特征，在 VR/游戏/辅助技术等方面有应用前景。

**[Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model](human_understanding/neural_collapse_in_cumulative_link_models_for_ordinal_regression_an_analysis_wit.md)**

:   将Neural Collapse (NC)理论扩展到基于累积链接模型(CLM)的序数回归(OR)任务中，在无约束特征模型(UFM)框架下证明了Ordinal Neural Collapse (ONC)的三个标志性质：类内均值坍缩(ONC1)、特征坍缩到一维子空间(ONC2)、以及潜变量按类别顺序排列(ONC3)，并在零正则极限下揭示了潜变量与阈值之间的简洁几何关系。

**[Policy Compatible Skill Incremental Learning via Lazy Learning Interface](human_understanding/policy_compatible_skill_incremental_learning_via_lazy_learning_interface.md)**

:   提出SIL-C框架，通过双向惰性学习接口(bilateral lazy learning interface)实现技能增量学习中的技能-策略兼容性，使增量更新的技能能直接提升下游策略性能而无需重训练或结构调整。

**[SpecAttn: Speculating Sparse Attention](human_understanding/specattn_speculating_sparse_attention.md)**

:   SpecAttn 提出一种无需训练的方法，利用投机解码中草稿模型已计算的注意力权重来预测验证模型的重要 token，通过 KL 散度层映射 + 免排序 top-p 核选择 + 动态 KV 缓存剪枝，实现 78.4% 的 KV 缓存访问减少，困惑度仅增加 15.29%，显著优于现有稀疏注意力方法。

**[SPROD: Spurious-Aware Prototype Refinement for Reliable Out-of-Distribution Detection](human_understanding/spurious-aware_prototype_refinement_for_reliable_out-of-distribution_detection.md)**

:   SPROD 是一种后置（post-hoc）OOD 检测方法，专门应对训练数据中的虚假相关——通过将每个类别的原型细分为"正确分类"和"误分类"子组（后者共享虚假特征），配合 K-means 式精炼和距离式（生成式）评分，在 5 个虚假相关 OOD 基准上平均 AUROC 85.1%（+4.8% vs 次优 KNN），FPR@95 49.0%（-9.3% vs 次优）。

**[Stochastic Momentum Methods for Non-smooth Non-Convex Finite-Sum Coupled Compositional Optimization](human_understanding/stochastic_momentum_methods_for_non-smooth_non-convex_finite-sum_coupled_composi.md)**

:   针对非光滑非凸有限和耦合复合优化 (FCCO) 问题，提出两种随机动量方法 SONEX（单循环）和 ALEXR2（双循环），通过外层 Moreau 包络平滑和嵌套平滑技术将迭代复杂度从 $O(1/\epsilon^6)$ 改进至 $O(1/\epsilon^5)$，并在非凸不等式约束优化中取得同等最优复杂度。

---

## 🎬 视频理解 { #video_understanding }

**[A Little Depth Goes a Long Way: The Expressive Power of Log-Depth Transformers](video_understanding/a_little_depth_goes_a_long_way_the_expressive_power_of_logde.md)**

:   本文证明了将 Transformer 的深度从常数增长到 Θ(log n) 就能解锁识别正则语言和图连通性这两类固定深度 Transformer 无法表达的问题，且深度扩展比宽度（需超多项式增长）和 CoT 步数（需超对数增长）都更高效。

**[AdaVideoRAG: Omni-Contextual Adaptive Retrieval-Augmented Efficient Long Video Understanding](video_understanding/adavideorag_omnicontextual_adaptive_retrievalaugmented_effic.md)**

:   提出 AdaVideoRAG，通过轻量级意图分类器将查询按难度路由到三级检索路径（无检索/朴素检索/图检索），结合全知识索引模块（caption+ASR+OCR+视觉+知识图谱）实现长视频理解的效率-精度最优平衡，在 MLVU 上为 Qwen2.5-VL-7B 带来 39.8% 提升。

**[Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](video_understanding/adversarial_locomotion_and_motion_imitation_for_humanoid_policy_learning.md)**

:   ALMI提出上下半身对抗训练框架：下半身策略在上半身动作干扰下学习鲁棒运动，上半身策略在下半身运动干扰下学习精确动作模仿，通过迭代对抗训练收敛到Nash均衡，实现Unitree H1-2真实机器人的稳定全身协调控制。

**[Agentic Persona Control and Task State Tracking for Realistic User Simulation](video_understanding/agentic_persona_control_and_task_state_tracking_for_realistic_user_simulation_in.md)**

:   提出三 agent 协作框架用于逼真的用户模拟——User Agent（协调）+ State Tracking Agent（结构化任务状态）+ Message Attributes Generation Agent（基于 persona 和状态的行为属性控制），在餐厅点餐场景中综合仿真质量（CRRS）提升 102.6%，persona 保持度 +19.9%，行为自然度 +284.5%，且核心发现：无状态感知的行为控制导致 BVS=0（完全刚性）。

**[CleverBirds: A Multiple-Choice Benchmark for Fine-grained Human Knowledge Tracing](video_understanding/cleverbirds_a_multiple-choice_benchmark_for_fine-grained_human_knowledge_tracing.md)**

:   发布 CleverBirds——超大规模细粒度视觉知识追踪基准，包含 4万+用户的 1700万+多选题交互（覆盖 10000+鸟类物种），展示了追踪细粒度视觉专家技能发展的挑战性，为 KT 方法提供了前所未有的视觉领域评测平台。

**[Cloud4D: Estimating Cloud Properties at a High Spatial and Temporal Resolution](video_understanding/cloud4d_estimating_cloud_properties_at_a_high_spatial_and_temporal_resolution.md)**

:   首个基于地面多视角相机的学习框架，通过单应性引导的2D-to-3D Transformer重建四维（3D空间+时间）云液态水含量分布，在25m空间/5s时间分辨率下实现了相对雷达<10%的误差，比卫星观测提升了一个数量级的时空分辨率。

**[ConViS-Bench: Estimating Video Similarity Through Semantic Concepts](video_understanding/convis-bench_estimating_video_similarity_through_semantic_concepts.md)**

:   提出基于语义概念的视频相似度估计任务 ConViS 及配套 benchmark ConViS-Bench（610对视频、16领域、5概念），系统评测了10+主流模型在概念条件下的视频比较能力，揭示当前模型在时序结构和空间语境理解上的显著短板。

**[Deceptron Learned Local Inverses For Fast And Stable Physics Inversion](video_understanding/deceptron_learned_local_inverses_for_fast_and_stable_physics_inversion.md)**

:   提出 Deceptron 双向模块，通过学习可微分前向代理的局部逆映射并引入 Jacobian Composition Penalty (JCP)，在求解物理逆问题时将输出空间的残差拉回输入空间，实现类 Gauss-Newton 的预条件梯度更新，迭代次数大幅减少（Heat-1D 约 20 倍加速）。

**[DeltaProduct: Improving State-Tracking in Linear RNNs via Householder Products](video_understanding/deltaproduct_improving_state-tracking_in_linear_rnns_via_householder_products.md)**

:   提出 DeltaProduct，通过将 DeltaNet 的单步梯度下降扩展至每个 token 的多步梯度下降，使状态转移矩阵成为 $n_h$ 个广义 Householder 变换的乘积，实现了表达力与效率之间的可调平衡，显著提升了状态跟踪能力和长度外推性能。

**[Dense SAE Latents Are Features, Not Bugs](video_understanding/dense_sae_latents_are_features_not_bugs.md)**

:   本文系统研究了稀疏自编码器(SAE)中频繁激活的"dense latents"，证明它们不是训练噪声，而是语言模型残差流中固有的密集子空间的反映，并提出了一套包含位置追踪、上下文绑定、零空间、字母、词性和PCA等六类dense latent的分类体系。

**[DSAS: A Universal Plug-and-Play Framework for Attention Optimization in Multi-Document Question Answering](video_understanding/dsas_a_universal_plug-and-play_framework_for_attention_optimization_in_multi-doc.md)**

:   提出Dual-Stage Adaptive Sharpening (DSAS)，一个无需训练的即插即用注意力优化框架，通过Contextual Gate Weighting (CGW)增强关键段落对问题和目标位置的注意力、通过Reciprocal Attention Suppression (RAS)抑制关键与无关段落间的信息交换，在多文档QA上平均F1提升达4.2%。

**[egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-World Tasks](video_understanding/egoemotion_egocentric_vision_and_physiological_signals_for_emotion_and_personali.md)**

:   提出egoEMOTION——首个结合第一人称视觉（Meta Project Aria眼镜）与生理信号的情感与人格识别数据集，涵盖43名被试、50+小时录制、16种任务，发现第一人称视觉信号（尤其眼动特征）在真实场景情感预测中优于传统生理信号。

**[Empower Words: DualGround for Structured Phrase and Sentence-Level Temporal Grounding](video_understanding/empower_words_dualground_for_structured_phrase_and_sentencel.md)**

:   论文指出现有视频时序定位模型在跨模态注意力中往往过度依赖句末 [EOS] token 的全局语义、忽视词级局部信号，提出 DualGround 双分支架构，将句子级全局语义与短语级局部语义显式解耦建模，在 QVHighlights 和 Charades-STA 上实现 Moment Retrieval 与 Highlight Detection 的 SOTA。

**[Enhancing Temporal Understanding in Video-LLMs through Stacked Temporal Attention in Vision Encoders](video_understanding/enhancing_temporal_understanding_in_videollms_through_stacke.md)**

:   提出 STAVEQ2，在 Vision Encoder 中堆叠参数高效的时序注意力模块（STA），解决现有 Video-LLM 在细粒度时序理解（如区分"从左到右拉"和"从右到左拉"）上的根本性架构缺陷，在 VITATECS/MVBench/Video-MME 上提升最高 5.5%。

**[FastVID: Dynamic Density Pruning for Fast Video Large Language Models](video_understanding/fastvid_dynamic_density_pruning_for_fast_video_large_languag.md)**

:   提出 FastVID，通过动态时序分割 (DySeg) + 密度空时剪枝 (STPrune) 从时间和视觉两个维度系统性消除视频 token 冗余，在 LLaVA-OneVision-7B 上剪掉 90.3% 视频 token 后仍保留 98% 精度，LLM prefill 阶段加速 7.1×。

**[Fixed-Point RNNs: Interpolating from Diagonal to Dense](video_understanding/fixed-point_rnns_interpolating_from_diagonal_to_dense.md)**

:   提出 Fixed-Point RNN 框架，将稠密线性 RNN 参数化为对角线性 RNN 的不动点，通过迭代次数在对角（高效）与稠密（表达力强）之间动态插值，首次在状态跟踪（$A_5$/$S_5$）和拷贝任务上同时取得最优结果。

**[Force Prompting: Video Generation Models Can Learn and Generalize Physics-based Control Signals](video_understanding/force_prompting_video_generation_models_can_learn_and_generalize_physics-based_c.md)**

:   提出Force Prompting，将物理力（局部点力和全局风力）作为视频生成模型的控制信号，仅用~15K合成训练视频（Blender旗帜和滚球）和单日4xA100训练，即可在多样真实场景图像上展现跨物体/材质/几何的惊人泛化，包括初步的质量理解能力。

**[Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation](video_understanding/foresight_adaptive_layer_reuse_for_accelerated_and_highquali.md)**

:   提出 Foresight，一种训练无关的自适应层复用框架，通过动态 MSE 阈值决策在 DiT 去噪过程中哪些层可复用缓存、哪些需重新计算，在 OpenSora/Latte/CogVideoX 上实现最高 1.63× 端到端加速且保持视频质量。

**[GeoDynamics: A Geometric State-Space Neural Network for Understanding Brain Dynamics on Riemannian Manifolds](video_understanding/geodynamics_a_geometric_state-space_neural_network_for_understanding_brain_dynam.md)**

:   提出GeoDynamics，将经典状态空间模型(SSM)从欧几里得空间推广到对称正定(SPD)流形，通过加权Frechet均值聚合和正交群平移实现流形上的状态演化，在脑连接组（AD/PD/ASD早期诊断）和人体动作识别上均取得SOTA。

**[Grounding Foundational Vision Models with 3D Human Poses for Robust Action Recognition](video_understanding/grounding_foundational_vision_models_with_3d_human_poses_for_robust_action_recog.md)**

:   提出一种融合 V-JEPA 2 视觉上下文特征与 CoMotion 3D 骨骼姿态数据的 cross-attention 多模态架构，在标准及高遮挡动作识别基准上优于单模态基线。

**[In the Eye of MLLM: Benchmarking Egocentric Video Intent Understanding with Gaze-Guided Prompting](video_understanding/in_the_eye_of_mllm_benchmarking_egocentric_video_intent_understanding_with_gaze-.md)**

:   提出 EgoGazeVQA——首个利用注视（gaze）信号评估 MLLM 对第一人称视频中用户意图理解能力的基准，并设计三种 gaze-guided prompting 策略显著提升模型表现。

**[InFlux: A Benchmark for Self-Calibration of Dynamic Intrinsics of Video Cameras](video_understanding/influx_a_benchmark_for_self-calibration_of_dynamic_intrinsics_of_video_cameras.md)**

:   提出首个包含逐帧动态相机内参真值的真实视频基准 InFlux（386 视频、143K+ 标注帧），通过镜头元数据到内参的查找表（LUT）实现精确标注，并揭示现有内参预测方法在动态内参场景下表现不佳。

**[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](video_understanding/kungfubot_physics-based_humanoid_whole-body_control_for_learning_highly-dynamic_.md)**

:   提出 PBHC 框架，通过物理感知运动处理流水线和自适应跟踪因子的双层优化，使人形机器人（Unitree G1）学会功夫、舞蹈等高动态全身动作，跟踪误差显著优于现有方法并成功实机部署。

**[Lattice Boltzmann Model for Learning Real-World Pixel Dynamicity](video_understanding/lattice_boltzmann_model_for_learning_real-world_pixel_dynamicity.md)**

:   受流体力学中格子玻尔兹曼方法启发，提出 LBM（Lattice Boltzmann Model）用于在线实时像素跟踪，将视频像素建模为流体格子并通过碰撞-流式过程求解运动状态，以 18M 参数实现 SOTA 在线跟踪性能且可在边缘设备上实时运行。

**[LeMiCa: Lexicographic Minimax Path Caching for Efficient Diffusion-Based Video Generation](video_understanding/lemica_lexicographic_minimax_path_caching_for_efficient_diffusion-based_video_ge.md)**

:   提出 LeMiCa，一种免训练的扩散视频生成加速框架，将缓存调度建模为有向无环图上的字典序极小极大路径优化问题，通过全局误差控制实现速度和质量的双重提升（Latte 上 2.9× 加速，Open-Sora 上 LPIPS 低至 0.05）。

**[Less is More but Where: Dynamic Token Compression via LLM-Guided Keyframe Prior](video_understanding/less_is_more_but_where_dynamic_token_compression_via_llm-guided_keyframe_prior.md)**

:   提出 DyToK，一种无需训练的视频 token 动态压缩方法，利用 VLLM 深层注意力中固有的 query 条件关键帧先验，为不同帧自适应分配 token 预算，实现即插即用式的效率-精度最优权衡。

**[Less is More: Local Intrinsic Dimensions of Contextual Language Models](video_understanding/less_is_more_local_intrinsic_dimensions_of_contextual_language_models.md)**

:   提出利用上下文 token 嵌入的局部内在维度（Local Intrinsic Dimension, LID）来无监督监测 LLM 训练动态——维度下降预示泛化改善，维度上升预示过拟合——在对话状态跟踪、grokking、情感识别等任务上验证了这一几何信号的实用性。

**[LiveStar: Live Streaming Assistant for Real-World Online Video Understanding](video_understanding/livestar_live_streaming_assistant_for_real-world_online_video_understanding.md)**

:   提出 LiveStar，一个始终在线的直播流视频理解助手，通过 Streaming Causal Attention Masks (SCAM) 训练策略和 Streaming Verification Decoding (SVeD) 推理框架，实现自适应响应时机判断，在 OmniStar 基准上语义正确性提升 19.5%，时间偏差降低 18.1%。

**[MimeQA: Towards Socially-Intelligent Nonverbal Foundation Models](video_understanding/mimeqa_towards_socially-intelligent_nonverbal_foundation_models.md)**

:   构建首个基于哑剧视频的非语言社交推理基准 MimeQA，包含101个视频和806个QA对，覆盖三层问题层次（具象识别→场景理解→全局推理），揭示当前VideoLLMs在非语言社交理解上的严重不足（20-30% vs 人类86%）。

**[MUVR: A Multi-Modal Untrimmed Video Retrieval Benchmark with Multi-Level Visual Correspondence](video_understanding/muvr_a_multi-modal_untrimmed_video_retrieval_benchmark_with_multi-level_visual_c.md)**

:   提出 MUVR 基准，面向长视频平台的多模态未剪辑视频检索任务，设计了以视频为中心的多模态查询格式（视频+文本+标签+掩码）和六级视觉对应匹配准则，包含 53K 视频和 1050 个查询，系统评估了检索模型和 MLLM 的局限性。

**[Neural Stochastic Flows: Solver-Free Modelling and Inference for SDE Solutions](video_understanding/neural_stochastic_flows_solver-free_modelling_and_inference_for_sde_solutions.md)**

:   提出 Neural Stochastic Flows（NSF），通过条件归一化流直接学习 SDE 的转移分布 $p(x_t \mid x_s)$，在架构上约束满足随机流性质（恒等、Markov、Chapman-Kolmogorov），实现了无需数值求解器的单步采样，在远距时间点上加速高达两个数量级。

**[NeuroPath: Neurobiology-Inspired Path Tracking and Reflection for Semantically Coherent Retrieval](video_understanding/neuropath_neurobiology-inspired_path_tracking_and_reflection_for_semantically_co.md)**

:   受神经生物学中海马体位置细胞导航与记忆巩固机制启发，提出 NeuroPath——一个基于语义路径追踪的 RAG 框架，通过 LLM 驱动的目标导向路径构建和后检索补全策略，在多跳问答任务上实现 recall@2 平均 16.3% 和 recall@5 平均 13.5% 的提升。

**[Open-World Drone Active Tracking with Goal-Centered Rewards](video_understanding/open-world_drone_active_tracking_with_goal-centered_rewards.md)**

:   提出首个开放世界无人机主动跟踪基准 DAT（24 个城市级场景、高保真动力学仿真），以及基于目标中心奖励函数和课程学习的强化学习跟踪方法 GC-VAT，在仿真器上达到约 72% 的跟踪成功率。

**[Part-Aware Bottom-Up Group Reasoning for Fine-Grained Social Interaction Detection](video_understanding/part-aware_bottom-up_group_reasoning_for_fine-grained_social_interaction_detecti.md)**

:   提出一种部位感知的自底向上群组推理框架，通过姿态引导的身体部位特征增强和基于相似度的个体关联来推断社交群组和细粒度交互，在 NVI 和 Café 数据集上达到新 SOTA。

**[Revisiting Bi-Linear State Transitions in Recurrent Neural Networks](video_understanding/revisiting_bi-linear_state_transitions_in_recurrent_neural_networks.md)**

:   系统性地重新审视 RNN 中的双线性状态转移（隐状态与输入的乘法交互），理论证明双线性 RNN 可模拟任意有限状态机，并展示其在去除加性项后形成了一个从对角到全结构的自然表达力层次，揭示了 Mamba 等流行线性 RNN 处于该层次最低端。

**[Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models](video_understanding/structured_sparse_transition_matrices_to_enable_state_tracking_in_state-space_mo.md)**

**[TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs](video_understanding/tempsampr1_effective_temporal_sampling_with_reinforcement_fi.md)**

:   提出 TempSamp-R1，针对视频时序定位任务改进 GRPO 强化微调框架，通过 off-policy 时间精确引导 + 非线性软优势计算 + 混合 CoT 训练，在 Charades-STA/ActivityNet/QVHighlights 上分别提升 +2.7%/+5.3%/+3.0%。

**[Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task](video_understanding/toolaugmented_spatiotemporal_reasoning_for_streamlining_vide.md)**

:   论文为复杂 VideoQA 提出一套轻量但可扩展的 Video Toolkit，并设计 STAR（Spatiotemporal Reasoning Framework）来调度时间工具与空间工具的调用顺序，逐步定位视频关键区域，显著增强 GPT-4o 的时空推理能力，在 VideoMME 上提升 8.2%，在 LongVideoBench 上提升 4.6%。

**[Two Causally Related Needles in a Video Haystack](video_understanding/two_causally_related_needles_in_a_video_haystack.md)**

:   提出CAUSAL2NEEDLES benchmark评估VLM的长视频双针(2-needle)因果推理能力：需要从视频两个不同位置提取因果关联的事件信息并联合推理，利用"桥接实体"迫使模型先理解结果再追溯原因，揭示即使GPT-4o在2-needle因果问题上仅达13.4%的Both准确率（vs人类79.3%）。

**[VideoLucy: Deep Memory Backtracking for Long Video Understanding](video_understanding/videolucy_deep_memory_backtracking_for_long_video_understanding.md)**

:   提出VideoLucy框架，通过层次化记忆结构和基于Agent的迭代回溯机制，模拟人类从粗到细的回忆过程，在多个长视频理解基准上大幅超越现有方法，甚至超过GPT-4o等商业模型。

**[VDRP: Visual Diversity and Region-aware Prompt Learning for Zero-shot HOI Detection](video_understanding/visual_diversity_and_region-aware_prompt_learning_for_zero-shot_hoi_detection.md)**

:   提出 VDRP 框架，通过视觉多样性感知的 prompt 学习（注入组级方差 + 高斯扰动）和区域感知的 prompt 增强（基于 LLM 生成的区域概念检索），解决零样本 HOI 检测中类内视觉多样性和类间视觉纠缠两大挑战。

**[VMDT: Decoding the Trustworthiness of Video Foundation Models](video_understanding/vmdt_decoding_the_trustworthiness_of_video_foundation_models.md)**

:   提出 VMDT（Video-Modal DecodingTrust），首个统一评估 T2V 和 V2T 视频基础模型在安全、幻觉、公平、隐私和对抗鲁棒性五个维度上可信度的基准平台，涵盖 7 个 T2V 和 19 个 V2T 模型的大规模评测，揭示了模型规模与可信度之间的复杂关系。

**[Web-Scale Collection of Video Data for 4D Animal Reconstruction](video_understanding/web-scale_collection_of_video_data_for_4d_animal_reconstruction.md)**

:   提出一个全自动化的大规模视频数据采集管线，从 YouTube 挖掘并处理得到 30K 动物视频（2M帧），建立首个 4D 四足动物重建基准 Animal-in-Motion（230序列/11K帧），并提出 4D-Fauna 基线方法实现序列级优化的无模型 4D 重建。

---

## 🕸️ 图学习 { #graph_learning }

**[BLISS: Bandit Layer Importance Sampling Strategy for Efficient Training of Graph Neural Networks](graph_learning/bliss_bandit_layer_importance_sampling_strategy_for_efficient_training_of_graph_.md)**

:   提出 BLISS，将 GNN 的层级邻居采样建模为多臂老虎机问题，用 EXP3 算法动态调整每条边的采样概率，根据邻居对节点表示的方差贡献作为奖励信号，在 GCN 和 GAT 上维持或超越全批次训练精度。

**[Deliberation on Priors: Trustworthy Reasoning of LLMs on Knowledge Graphs](graph_learning/deliberation_on_priors_trustworthy_reasoning_of_large_language_models_on_knowled.md)**

:   提出 Deliberation over Priors（DP）框架，通过渐进式知识蒸馏（SFT + KTO 偏好优化）提升关系路径生成的忠实度，并通过约束引导的内省-回溯机制保障推理可靠性，在 ComplexWebQuestions 上 H@1 提升 16.5%，且 LLM 调用次数仅为 2.9 次（ToG 需 22.6 次）。

**[Diagnosing and Addressing Pitfalls in KG-RAG Datasets: Toward More Reliable Benchmarking](graph_learning/diagnosing_and_addressing_pitfalls_in_kg-rag_datasets_toward_more_reliable_bench.md)**

:   系统审计16个KGQA数据集发现平均事实正确率仅57%（WebQSP 52%，MetaQA 20%），提出KGQAGen框架——通过LLM引导的子图扩展+SPARQL自动验证构建高质量多跳QA数据集KGQAGen-10k（96.3%准确率），揭示KG-RAG的主要瓶颈在检索而非推理。

**[Disentangling Hyperedges through the Lens of Category Theory](graph_learning/disentangling_hyperedges_through_the_lens_of_category_theory.md)**

:   首次从范畴论视角分析超边解耦，基于自然性条件导出"因子表示一致性"标准（聚合后解耦 vs 解耦后聚合应一致），提出 Natural-HNN 模型在6个癌症分型数据集上全面超越14个baseline（BRCA F1 从75.7%提升至80.4%），并能100%正确捕获基因通路的功能上下文。

**[DuetGraph: Coarse-to-Fine Knowledge Graph Reasoning with Dual-Pathway Global-Local Fusion](graph_learning/duetgraph_coarse-to-fine_knowledge_graph_reasoning_with_dual-pathway_global-loca.md)**

:   DuetGraph 提出双通路（消息传递 + 全局注意力）并行融合模型与粗到精推理优化策略，通过分离而非堆叠局部/全局信息处理来缓解 KG 推理中的分数过平滑问题，在归纳与传导推理任务上取得 SOTA，MRR 最高提升 8.7%、训练加速 1.8×。

**[Dynamic Bundling with Large Language Models for Zero-Shot Inference on Text-Attributed Graphs](graph_learning/dynamic_bundling_with_large_language_models_for_zero-shot_inference_on_text-attr.md)**

:   DENSE 提出"文本捆绑"策略，将拓扑/语义相近的节点文本打包后查询 LLM 获取 bundle 级别标签，再用 entropy-based 和 ranking-based 损失监督 GNN 训练，并动态精炼 bundle 排除噪声节点，在 10 个 TAG 数据集上零样本推理全面超越 GPT-4o 和图基础模型。

**[Elastic Weight Consolidation for Knowledge Graph Continual Learning: An Empirical Evaluation](graph_learning/elastic_weight_consolidation_for_knowledge_graph_continual_learning_an_empirical.md)**

:   本文在 FB15k-237 上系统评估了弹性权重固化（EWC）对 TransE 知识图谱嵌入持续学习的效果，发现 EWC 将灾难性遗忘从 12.62% 降至 6.85%（减少 45.7%），并揭示了任务划分策略（基于关系 vs 随机）对遗忘度量的显著影响（9.8 个百分点差异）。

**[FALCON: An ML Framework for Fully Automated Layout-Constrained Analog Circuit Design](graph_learning/falcon_an_ml_framework_for_fully_automated_layout-constrained_analog_circuit_des.md)**

:   FALCON 提出端到端的模拟/RF 电路自动化设计框架，通过 MLP 拓扑选择 + 边中心 GNN 性能预测 + 可微版图约束梯度推理三阶段流水线，在 100 万级 Cadence 仿真数据集上实现 >99% 拓扑选择准确率、<10% 性能预测误差，单实例推理不到 1 秒。

**[From Sequence to Structure: Uncovering Substructure Reasoning in Transformers](graph_learning/from_sequence_to_structure_uncovering_substructure_reasoning_in_transformers.md)**

:   本文通过实证和理论分析揭示 decoder-only Transformer 如何从文本序列中理解图结构，提出"诱导子图过滤"（ISF）解释子结构逐层识别机制，并扩展到 LLM 验证一致性、复合图推理（Thinking-in-Substructures）和属性图（分子图）子结构提取。

**[Generative Graph Pattern Machine](graph_learning/generative_graph_pattern_machine.md)**

:   提出 Generative Graph Pattern Machine (G2PM)，一种完全无消息传递的生成式 Transformer 图预训练框架：通过随机游走将图实例（节点/边/图）tokenize 为子结构序列，以 Masked Substructure Modeling 目标进行自监督预训练，在节点/链接/图分类及跨域迁移任务上全面超越现有图预训练方法，并展现出类似 NLP/CV 的模型和数据双重扩展性。

**[Geometric Imbalance in Semi-Supervised Node Classification](graph_learning/geometric_imbalance_in_semi-supervised_node_classification.md)**

:   首次形式化定义了半监督节点分类中的"几何不平衡"概念——消息传递在类别不平衡图上导致少数类节点在黎曼流形嵌入空间中产生几何歧义，并提出 UNREAL 框架，通过双路径伪标签对齐、节点重排序和几何歧义样本丢弃三个模块系统性缓解该问题。

**[GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation](graph_learning/gfm-rag_graph_foundation_model_for_retrieval_augmented_generation.md)**

:   提出首个图基础模型驱动的检索增强生成框架 GFM-RAG，通过 query-dependent GNN 在知识图谱上进行单步多跳推理，仅 8M 参数即可在未见数据集上零样本泛化，在多跳QA检索任务上大幅超越 SOTA。

**[GnnXemplar: Exemplars to Explanations -- Natural Language Rules for Global GNN Interpretability](graph_learning/gnnxemplar_exemplars_to_explanations_--_natural_language_rules_for_global_gnn_in.md)**

:   提出GnnXemplar框架，基于认知科学的样例理论（Exemplar Theory），通过在GNN嵌入空间中选取代表性节点（exemplar）并利用LLM迭代生成自然语言布尔规则，实现大规模图上节点分类GNN的全局可解释性。

**[Graph Neural Networks for Efficient AC Power Flow Prediction in Power Grids](graph_learning/graph_neural_networks_for_efficient_ac_power_flow_prediction_in_power_grids.md)**

:   将电力网络建模为图结构（母线为节点、输电线为边），探索 GCN、GAT、SAGEConv 和 GraphConv 四种 GNN 架构预测 AC 潮流解（电压幅值和相角），在 IEEE 14/30/57/118 母线测试系统上展示了 GNN 可高效替代传统 Newton-Raphson 求解器。

**[Graph Neural Networks for Interferometer Simulations](graph_learning/graph_neural_networks_for_interferometer_simulations.md)**

:   首次将图神经网络应用于光学干涉仪仿真，通过 GATv2 + KAN 架构预测 LIGO 干涉仪中的电磁场功率和空间强度分布，实现比标准仿真软件（FINESSE）快 815 倍的推理速度，同时保持较好的物理精度。

**[Graph Persistence goes Spectral](graph_learning/graph_persistence_goes_spectral.md)**

:   提出 SpectRe——将图拉普拉斯谱信息融入持续同调（PH）图的新拓扑描述符，证明其表达力严格强于 PH 和谱信息单独使用，建立了局部稳定性理论，在合成和真实数据集上提升 GNN 的图分类能力。

**[Graphfaas Serverless Gnn Inference For Burst-Resilient Real-Time Intrusion Detec](graph_learning/graphfaas_serverless_gnn_inference_for_burst-resilient_real-time_intrusion_detec.md)**

:   提出GraphFaaS，基于Serverless的GNN推理架构用于突发负载下的实时入侵检测：时间局部性图构建+频率过滤+贪心图分区实现延迟降低85%、变异系数降低64%同时保持准确率。

**[GraphTOP: Graph Topology-Oriented Prompting for Graph Neural Networks](graph_learning/graphtop_graph_topology-oriented_prompting_for_graph_neural_networks.md)**

:   提出首个图拓扑导向的 prompting 框架 GraphTOP，通过将 topology-oriented prompting 建模为边重连问题并用 Gumbel-Softmax 松弛到连续空间，在 5 个数据集 4 种预训练策略下超越 6 个基线方法。

**[Heterogeneous Swarms: Jointly Optimizing Model Roles and Weights for Multi-LLM Systems](graph_learning/heterogeneous_swarms_jointly_optimizing_model_roles_and_weights_for_multi-llm_sy.md)**

:   提出Heterogeneous Swarms算法，将多LLM系统建模为有向无环图（DAG），通过粒子群优化（PSO）联合优化模型角色（图结构）和模型权重，在12个任务上平均超越17个基线18.5%。

**[Making Classic GNNs Strong Baselines Across Varying Homophily: A Smoothness-Generalization Perspective](graph_learning/making_classic_gnns_strong_baselines_across_varying_homophily_a_smoothness-gener.md)**

:   从理论上揭示了 GNN 消息传递中平滑性（smoothness）与泛化性（generalization）之间的两难困境，提出 IGNN 框架通过三个简约设计原则（分离邻域变换、感知聚合、邻域关系学习）缓解该困境，在 30 个基线中表现最优且具备跨同质/异质图的通用性。

**[Moscat: Mixture of Scope Experts at Test for Generalizing Deeper GNNs](graph_learning/mixture_of_scope_experts_at_test_generalizing_deeper_graph_neural_networks_with_.md)**

:   通过 PAC-Bayes 界证明 GNN 深度变化导致不同同质性子群间的泛化偏好漂移，提出 Moscat——后处理注意力门控模型，在测试时自适应组合不同深度的独立训练 GNN 专家。

**[Nonlinear Laplacians: Tunable Principal Component Analysis under Directional Prior Information](graph_learning/nonlinear_laplacians_tunable_principal_component_analysis_under_directional_prio.md)**

:   提出非线性Laplacian谱算法，通过在观测矩阵 $\bm{Y}$ 上添加由度数向量经非线性函数 $\sigma$ 变换后得到的对角矩阵，将谱信息与方向先验信息融合，在稀疏偏向PCA问题中显著降低信号检测阈值（从 $\beta^*=1$ 降至约 $0.76$）。

**[OCN: Effectively Utilizing Higher-Order Common Neighbors for Better Link Prediction](graph_learning/ocn_effectively_utilizing_higher-order_common_neighbors_for_better_link_predicti.md)**

:   揭示高阶公共邻居（CN）在链接预测中的冗余和过平滑问题，提出正交化（Gram-Schmidt 去除阶间线性相关）+ 归一化（除以路径数，广义资源分配启发式）解决方案，在 7 个数据集上平均提升 HR@100 7.7%，DDI 数据集上提升 13.3%。

**[Over-squashing in Spatiotemporal Graph Neural Networks](graph_learning/over-squashing_in_spatiotemporal_graph_neural_networks.md)**

:   首次形式化时空图神经网络(STGNN)中的 over-squashing 问题，揭示了因果卷积中反直觉的"时间远处偏好"现象（最早时间步对最终表示影响最大），并证明 time-and-space 和 time-then-space 架构在信息瓶颈上等价，为使用计算高效的 TTS 架构提供理论支持。

**[PKD: Preference-driven Knowledge Distillation for Few-shot Node Classification](graph_learning/preference-driven_knowledge_distillation_for_few-shot_node_classification.md)**

:   PKD 框架协同 LLM 和多 GNN 教师做文本属性图少样本节点分类——GNN 偏好节点选择器（GNS）用 KL 散度不确定性选择需要 LLM 标注的节点，节点偏好 GNN 选择器（NGS）用 RL 为每个节点匹配最优 GNN 教师，在 9 个数据集上一致 SOTA（Cornell 87% vs 基线 59-82%）。

**[Principled Data Augmentation for Learning to Solve Quadratic Programming Problems](graph_learning/principled_data_augmentation_for_learning_to_solve_quadratic_programming_problem.md)**

:   提出基于KKT系统仿射变换的原则性数据增强框架，为线性规划(LP)和二次规划(QP)的MPNN学习优化(L2O)任务生成保最优性的增强实例，并结合对比学习预训练，在数据稀缺和OOD泛化场景下大幅提升性能。

**[Relieving the Over-Aggregating Effect in Graph Transformers](graph_learning/relieving_the_over-aggregating_effect_in_graph_transformers.md)**

:   发现了 Graph Transformer 中的 over-aggregating 现象——大量节点以近均匀注意力分数被聚合导致关键信息被稀释，提出 Wideformer 通过分割聚合+引导注意力来缓解，作为即插即用模块在 13 个数据集上一致提升骨干模型性能。

**[S'MoRE: Structural Mixture of Residual Experts for Parameter-Efficient LLM Fine-tuning](graph_learning/smore_structural_mixture_of_residual_experts_for_parameter-efficient_llm_fine-tu.md)**

:   提出S'MoRE框架，将低秩残差专家组织成多层树状结构，通过层次化路由为每个token构建定制化的"残差树"，在与LoRA相当的参数量下实现指数级增长的结构灵活性，显著提升LLM微调效果。

**[TAMI: Taming Heterogeneity in Temporal Interactions for Temporal Graph Link Prediction](graph_learning/tami_taming_heterogeneity_in_temporal_interactions_for_temporal_graph_link_predi.md)**

:   首次系统识别时序图交互中的异质性问题（交互间隔呈幂律分布），提出TAMI框架包含对数时间编码(LTE)和链接历史聚合(LHA)两个模块，可无缝集成到现有TGNN中，在16个数据集上持续提升链接预测性能，最高提升87.05%。

**[The Underappreciated Power of Vision Models for Graph Structural Understanding](graph_learning/the_underappreciated_power_of_vision_models_for_graph_structural_understanding.md)**

:   揭示视觉模型（ResNet/ViT/Swin等）在图结构理解方面被严重低估的能力——通过将图渲染为图像并用视觉编码器处理，在全局拓扑感知和跨尺度泛化上显著优于GNN，并提出GraphAbstract benchmark系统评估这一发现。

**[Uniedit A Unified Knowledge Editing Benchmark For Large Language Models](graph_learning/uniedit_a_unified_knowledge_editing_benchmark_for_large_language_models.md)**

:   构建UniEdit——基于25个开放域知识的统一LLM知识编辑基准，提出邻域多跳链采样(NMCS)算法评估编辑的波纹效应。

**[Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with LLMs](graph_learning/unifying_text_semantics_and_graph_structures_for_temporal_text-attributed_graphs.md)**

:   提出 Cross 框架——用 LLM 在策略采样的时间点上动态总结节点邻域的语义演变（Temporal Reasoning Chain），然后通过语义-结构协同编码器双向融合文本语义和图结构时序信息，在时序链接预测上平均 MRR 提升 24.7%，工业数据（微信）上 AUC 提升 3.7%。

**[Wavy Transformer](graph_learning/wavy_transformer.md)**

:   揭示了Transformer注意力层本质上等价于完全图上的图神经扩散过程，并基于二阶波动方程提出Wavy Transformer，通过能量守恒特性缓解深层Transformer的过平滑问题，在NLP、CV和稀疏图任务上均取得一致性提升。

**[What Expressivity Theory Misses: Message Passing Complexity for GNNs](graph_learning/what_expressivity_theory_misses_message_passing_complexity_for_gnns.md)**

:   批判 GNN 的二值表达力理论无法解释实际性能差异，提出 MPC——基于概率性 lossyWL 的连续、任务特定复杂度度量，与准确率的 Spearman 相关性达 -1（传统 WLC 恒为零），成功解释了 GCN+虚拟节点为何在长程任务上优于更高表达力的高阶模型。

**[When No Paths Lead to Rome: Benchmarking Systematic Neural Relational Reasoning](graph_learning/when_no_paths_lead_to_rome_benchmarking_systematic_neural_relational_reasoning.md)**

:   提出NoRA benchmark，系统性地打破现有关系推理benchmark中"推理可归约为路径组合"的假设，引入非路径推理、歧义事实和多关系等挑战，揭示包括o3在内的所有现有模型在off-path推理上的根本缺陷。

---

## 📈 时间序列 { #time_series }

**[A Graph Neural Network Approach for Localized and High-Resolution Temperature Forecasting](time_series/a_graph_neural_network_approach_for_localized_and_high-resolution_temperature_fo.md)**

:   提出一种 GCN-GRU 混合框架用于社区尺度（2.5km）高分辨率温度预报（1-48小时），在加拿大西南安大略三个区域上验证，最大区域平均 MAE 1.93°C、48h MAE 2.93°C，探索了 ClimateBERT 语言模型嵌入作为标准化输入的方案，为数据稀缺的全球南方地区提供可迁移的轻量级预报框架。

**[Abstain Mask Retain Core: Time Series Prediction by Adaptive Masking Loss with Representation Consistency](time_series/abstain_mask_retain_core_time_series_prediction_by_adaptive.md)**

:   揭示了时间序列预测中"适当截断历史数据反而提升精度"的反直觉现象（冗余特征学习问题），基于信息瓶颈理论提出AMRC方法，通过自适应掩码损失和表征一致性约束来抑制冗余特征学习，作为模型无关的训练框架在多种架构上显著提升性能。

**[AERO: A Redirection-Based Optimization Framework Inspired by Judo for Robust Probabilistic Forecasting](time_series/aero_a_redirection-based_optimization_framework_inspired_by_judo_for_robust_prob.md)**

:   AERO 提出受柔道"借力重定向"启发的优化框架，通过梯度投影、能量守恒和干扰预测将对抗性扰动重定向为有利优化方向，在概率太阳能价格预测上展示更稳定的收敛。

**[AttentionPredictor: Temporal Patterns Matter for KV Cache Compression](time_series/attentionpredictor_temporal_patterns_matter_for_kv_cache_com.md)**

:   首个基于学习的 KV Cache 压缩方法，通过轻量级时空卷积模型预测下一 token 的注意力分数来动态识别关键 token，实现 13× KV cache 压缩和 5.6× cache offloading 加速，显著优于静态方法。

**[Benchmarking Probabilistic Time Series Forecasting Models on Neural Activity](time_series/benchmarking_probabilistic_time_series_forecasting_models_on_neural_activity.md)**

:   首次系统评测 12 个概率时间序列预测模型在小鼠皮层钙成像数据上的表现，发现 PatchTST 一致最优（信息性预测窗口达 1.5 秒），零样本基础模型（Chronos）完全失败但微调后竞争力强，揭示神经活动的内在可预测性上限约 1.5 秒。

**[Causal Masking on Spatial Data: An Information-Theoretic Case for Learning Spatial Datasets with Unimodal Language Models](time_series/causal_masking_on_spatial_data_an_information-theoretic_case_for_learning_spatia.md)**

:   证明在空间数据（国际象棋棋盘FEN状态）上直接应用因果掩蔽训练单模态LLM，其表现优于先将数据线性化为序列（PGN棋步）后再应用因果掩蔽——FEN+因果掩蔽的Llama 1.3B达到~2630 Elo，而PGN+因果仅~2130 Elo。

**[CausalDynamics: A Large-Scale Benchmark for Structural Discovery of Dynamical Causal Models](time_series/causaldynamics_a_large-scale_benchmark_for_structural_discovery_of_dynamical_cau.md)**

:   提出 CausalDynamics——迄今最大规模的动力系统因果发现 benchmark（14000+ 图、5000 万+ 样本），涵盖从 3 维混沌 ODE/SDE 到层级耦合系统再到拟真气候模型的三层渐进复杂度体系，并全面评估了 10 种 SOTA 因果发现算法，揭示当前深度学习方法在高维非线性动力系统上的不足。

**[Channel Matters: Estimating Channel Influence for Multivariate Time Series](time_series/channel_matters_estimating_channel_influence_for_multivariate_time_series.md)**

:   提出 Channel-wise Influence (ChInf)——首个能量化多变量时间序列中不同通道对模型性能影响的影响函数方法，将 TracIn 从整体样本级分解到通道级，衍生出通道级异常检测和通道剪枝两个应用，在 5 个异常检测基准上排名第一。

**[Connecting the Dots: A ML Ready Dataset for Ionospheric Forecasting](time_series/connecting_the_dots_a_machine_learning_ready_dataset_for_ionospheric_forecasting.md)**

:   构建了首个ML-ready电离层预测数据集，整合SDO、太阳风、地磁指数和TEC观测等多源异构数据为统一的时间-空间结构，并基准测试了多种时空ML架构用于TEC预测。

**[Demandcast Global Hourly Electricity Demand Forecasting](time_series/demandcast_global_hourly_electricity_demand_forecasting.md)**

:   构建DemandCast——覆盖56个国家(2000-2025)的XGBoost全球小时电力需求预测框架，融合ERA5温度/GDP/人口等特征，归一化目标（年度分数）+时间分割评估，MAPE 9.2%。

**[Diffusion Transformers as Open-World Spatiotemporal Foundation Models](time_series/diffusion_transformers_as_open-world_spatiotemporal_foundation_models.md)**

:   提出 UrbanDiT，首个基于 Diffusion Transformer 的开放世界城市时空基础模型，通过统一的 prompt learning 框架整合异构数据类型（grid/graph）和多种任务（预测/插值/外推/填补），在多城市多场景下实现 SOTA 性能并展现强大的 zero-shot 泛化能力。

**[EcoCast: Spatio-Temporal Model for Continual Biodiversity Forecasting](time_series/ecocast_a_spatio-temporal_model_for_continual_biodiversity_and_climate_risk_fore.md)**

:   提出EcoCast，基于Transformer的时空模型，整合Sentinel-2、ERA5和GBIF数据进行近期物种分布预测，配合EWC持续学习机制，在非洲鸟类分布预测上F1从0.31提升至0.65。

**[Exploring Neural Granger Causality with xLSTMs: Unveiling Temporal Dependencies in Complex Data](time_series/exploring_neural_granger_causality_with_xlstms_unveiling_temporal_dependencies_i.md)**

:   提出 GC-xLSTM，利用 xLSTM 架构结合新颖的动态稀疏优化策略，在多变量时间序列中挖掘 Granger 因果关系，在多个数据集上取得 SOTA 性能。

**[Fern: Chaining Spectral Pearls — Ellipsoidal Forecasting Beyond Trajectories for Time Series](time_series/friren_beyond_trajectories_--_a_spectral_lens_on_time.md)**

:   提出 Fern (Forecasting with Ellipsoidal RepresentatioN)，通过逐 patch 的椭球体传输（旋转-缩放-平移）替代传统轨迹预测，在混沌系统上大幅超越基线，并在标准 LTSF 基准上保持竞争力。

**[How Foundational are Foundation Models for Time Series Forecasting?](time_series/how_foundational_are_foundation_models_for_time_series_forecasting.md)**

:   通过合成数据与真实电力消耗数据的系统性实验，揭示时间序列基础模型(TSFM)的零样本泛化能力高度依赖于预训练数据分布，在领域偏移场景下仅49.5K参数的轻量专用模型SAMFormer从头训练即可超越500M+参数的微调TimesFM。

**[How Patterns Dictate Learnability in Sequential Data](time_series/how_patterns_dictate_learnability_in_sequential_data.md)**

:   提出基于预测信息（predictive information）的信息论框架来量化序列数据中时间模式的强度，推导出将预测信息与最小可达风险联系起来的理论界，从而区分"模型不够好"还是"数据本身就不可预测"。

**[Improving Time Series Forecasting via Instance-aware Post-hoc Revision (PIR)](time_series/improving_time_series_forecasting_via_instance-aware_post-hoc_revision.md)**

:   PIR 提出实例感知的事后修正框架——通过不确定性估计识别预测失败实例，用局部修正（协变量+外生变量 Transformer）和全局修正（检索相似训练实例加权平均）的残差组合，作为即插即用模块使 SparseTSF MSE 降低 25.87%，PatchTST 降低 8.99%。

**[IonCast: A Deep Learning Framework for Forecasting Ionospheric Dynamics](time_series/ioncast_a_deep_learning_framework_for_forecasting_ionospheric_dynamics.md)**

:   提出 IonCast 框架，基于 GraphCast 启发的图神经网络架构，融合多源异构物理驱动数据，实现全球总电子含量（TEC）的高精度时空预测。

**[IonCast: A Deep Learning Framework for Forecasting Ionospheric Dynamics](time_series/ioncast_a_deep_learning_framework_for_forecasting_ionospheric_total_electron_con.md)**

:   提出IonCast框架，包含基于GraphCast的GNN模型和ConvLSTM基线，融合多源异构空间天气数据（TEC图、太阳风、地磁指数、轨道力学等）进行全球电离层总电子含量（TEC）的时空预测，在地磁风暴条件下优于持续性基线和IRI经验模型。

**[Learning Time-Scale Invariant Population-Level Neural Representations](time_series/learning_time-scale_invariant_population-level_neural_representations.md)**

:   提出时间尺度增强预训练（TSAP）策略，通过在预训练阶段引入多种时间窗口长度的数据增强，使群体级神经信号基础模型对输入时间尺度具有不变性，在匹配和未见时间尺度上均显著提升解码性能。

**[Learning with Calibration: Exploring Test-Time Computing of Spatio-Temporal Forecasting](time_series/learning_with_calibration_exploring_test-time_computing_of_spatio-temporal_forec.md)**

:   提出 ST-TTC，一种轻量级测试时计算范式，通过频域相位-幅值校准器和闪电梯度更新机制，在推理阶段实时修正时空预测中的周期性偏差，无需修改骨干网络即可一致性提升多种模型性能。

**[Martingale Score: An Unsupervised Metric for Bayesian Rationality in LLM Reasoning](time_series/martingale_score_an_unsupervised_metric_for_bayesian_rationality_in_llm_reasonin.md)**

:   提出 Martingale Score 作为无监督度量指标，基于贝叶斯统计中的鞅性质(Martingale property)来量化 LLM 推理过程中的信念固化(belief entrenchment)现象，发现该现象普遍存在且与准确率下降显著相关。

**[Neural MJD: Neural Non-Stationary Merton Jump Diffusion for Time Series Prediction](time_series/neural_mjd_neural_non-stationary_merton_jump_diffusion_for_time_series_predictio.md)**

:   提出 Neural MJD，用神经网络参数化非平稳 Merton 跳跃扩散模型，将预测建模为 SDE 仿真问题，结合时变 Itô 扩散（捕获连续漂移）和时变复合 Poisson 过程（建模突变跳跃），配合似然截断和 Euler-Maruyama with Restart 求解器实现可扩展学习与推理。

**[Physics-informed Reduced Order Modeling of Time-dependent PDEs via Differentiable Solvers](time_series/physics-informed_reduced_order_modeling_of_time-dependent_pdes_via_differentiabl.md)**

:   提出Φ-ROM框架，将可微分PDE求解器嵌入非线性降阶模型的训练过程中，通过求解器反馈直接约束潜在空间动态，使模型在泛化到未见参数/初始条件、长时间外推、稀疏观测数据恢复等方面显著优于纯数据驱动ROM和其他物理信息方法。

**[PlanU: Large Language Model Reasoning through Planning under Uncertainty](time_series/planu_large_language_model_reasoning_through_planning_under_uncertainty.md)**

:   提出PlanU——一种在MCTS中用分位数分布建模节点回报、并通过Upper Confidence Bounds with Curiosity (UCC)分数平衡探索与利用的LLM决策方法，首次系统性地同时处理LLM不确定性和环境不确定性，在多个随机环境基准上显著优于现有方法。

**[RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting](time_series/rivermamba_a_state_space_model_for_global_river_discharge_and_flood_forecasting.md)**

:   首个能在 0.05°（~5.5km）全球网格上做 7 天河流流量预报的深度学习模型——用空间填充曲线将 3D 时空点序列化后输入双向 Mamba block，结合 ECMWF HRES 气象预报，在 1.5-500 年重现期洪水检测上 F1 =0.459 超越 LSTM（0.358）和物理模型 GloFAS。

**[Scalable Signature Kernel Computations for Long Time Series via Local Neumann Series Expansions](time_series/scalable_signature_kernel_computations_for_long_time_series_via_local_neumann_se.md)**

:   提出 PowerSig，通过自适应截断的局部 Neumann 级数展开高效计算签名核（signature kernel），将内存从 $O(\ell^2)$ 降到 $O(\ell P)$，使签名核可扩展到单GPU上百万级长度的时间序列。

**[ScatterAD: Temporal-Topological Scattering Mechanism for Time Series Anomaly Detection](time_series/scatterad_temporal-topological_scattering_mechanism_for_time_series_anomaly_dete.md)**

:   提出"散射性"（scattering）作为异常检测的新归纳偏置——异常样本在高维表示空间中比正常样本分布更分散，通过双编码器（时间+拓扑）+ 超球面散射中心约束 + 对比融合学习时拓扑联合表示，在 6 个工业 IoT 数据集上 15/24 设置取得最佳。

**[Statistical Guarantees for High-Dimensional Stochastic Gradient Descent](time_series/statistical_guarantees_for_high-dimensional_stochastic_gradient_descent.md)**

:   将高维非线性时间序列的耦合技术引入在线学习，首次为常数学习率 SGD 及其 Ruppert-Polyak 平均变体在高维（$\ell^s$ 和 $\ell^\infty$ 范数下）提供了严格的矩收敛界和高概率集中界。

**[Strap Spatio-Temporal Pattern Retrieval For Out-Of-Distribution Generalization](time_series/strap_spatio-temporal_pattern_retrieval_for_out-of-distribution_generalization.md)**

:   提出 StRap，一个检索增强的时空模式学习框架，通过构建空间/时间/时空三维模式库并在推理时检索相似模式注入模型，在流式时空图 OOD 任务上平均提升 7.17%。

**[Structured Temporal Causality for Interpretable Multivariate Time Series Anomaly Detection](time_series/structured_temporal_causality_for_interpretable_multivariate_time_series_anomaly.md)**

:   提出OracleAD框架，通过为每个变量学习因果嵌入（LSTM编码+注意力池化）并构建稳定潜在结构（SLS）来建模正常状态下的变量间关系，结合预测误差和SLS偏离的双重评分机制实现可解释的多变量时间序列异常检测与根因定位。

**[Synthetic Series-Symbol Data Generation For Time Series Foundation Models](time_series/synthetic_series-symbol_data_generation_for_time_series_foundation_models.md)**

:   提出 Series-Symbol (S²) 数据生成机制和 SymTime 基础模型，通过符号表达式与时序数据的双模态对比学习预训练，在纯合成数据上训练即可在 5 大时序分析任务上与真实数据预训练的基础模型竞争。

**[Syntsbench Rethinking Temporal Pattern Learning In Deep Learning Models For Time](time_series/syntsbench_rethinking_temporal_pattern_learning_in_deep_learning_models_for_time.md)**

:   提出 SynTSBench，一个基于合成数据的时序预测模型评估框架，通过可编程特征配置（趋势/周期/噪声/依赖/多变量）和理论最优基准，系统揭示当前深度学习模型在各类时序模式上的能力边界。

**[Time-IMM: A Dataset and Benchmark for Irregular Multimodal Multivariate Time Series](time_series/time-imm_a_dataset_and_benchmark_for_irregular_multimodal_multivariate_time_seri.md)**

:   构建 Time-IMM 数据集——首个按因果机制分类不规则性的多模态多变量时序 benchmark（9 种不规则类型分为触发/约束/伪影三大类，9 个数据集），配套 IMM-TSF 预测库支持异步多模态融合，实验表明显式建模多模态在不规则时序上平均降低 MSE 6.71%，最高达 38.38%。

**[xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories](time_series/xlstm-mixer_multivariate_time_series_forecasting_by_mixing_via_scalar_memories.md)**

:   提出 xLSTM-Mixer，首次将扩展长短期记忆网络（sLSTM）与混合架构（Mixer）结合，通过时间混合、联合时间-变量混合和多视角混合三阶段架构实现多变量长期时间序列预测的 SOTA 性能，同时保持极低的内存占用。

---

## 🚗 自动驾驶 { #autonomous_driving }

**[3EED: Ground Everything Everywhere in 3D](autonomous_driving/3eed_ground_everything_everywhere_in_3d.md)**

:   提出 3EED——首个大规模多平台（车、无人机、四足机器人）、多模态（LiDAR+RGB）室外 3D 视觉定位基准，包含超 12.8 万目标和 2.2 万语言描述，规模是现有室外数据集的 10 倍；同时设计了跨平台对齐、多尺度采样和尺度自适应融合的基线方法，揭示了跨平台 3D grounding 的巨大性能差距。

**[AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead](autonomous_driving/aha_predicting_what_matters_next_online_highlight_detection.md)**

:   提出 AHA，一个自回归高光检测框架，在**不访问未来帧**的情况下根据自然语言任务描述实时预测每帧视频的相关性——利用多模态视觉语言模型+轻量解耦头+Dynamic SinkCache实现无限长度流媒体的恒定内存推理，在TVSum上超越离线全上下文方法+5.9% mAP、在Mr. Hisum上+8.3% mAP。

**[AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](autonomous_driving/autovla_a_vision-language-action_model_for_end-to-end_autonomous_driving_with_ad.md)**

:   提出AutoVLA——基于Qwen2.5-VL-3B的端到端自动驾驶VLA模型，将连续轨迹离散化为物理action tokens嵌入语言模型词表，支持fast/slow thinking双模式推理，通过GRPO强化微调同时提升10.6%性能和66.8%推理效率，在NAVSIM和Bench2Drive上达SOTA。

**[Availability-aware Sensor Fusion via Unified Canonical Space](autonomous_driving/availability-aware_sensor_fusion_via_unified_canonical_space.md)**

:   提出 ASF（Availability-aware Sensor Fusion），通过统一规范投影（UCP）将 Camera/LiDAR/4D Radar 特征映射到共享空间 + 跨传感器沿 patch 交叉注意力（CASAP，复杂度 $O(N_qN_s)$ 而非 $O(N_qN_sN_p)$）自动适配可用传感器 + 传感器组合损失（SCL）覆盖所有 7 种组合，在 K-Radar 上 AP_3D 73.6%（超 SOTA 20.1%），传感器故障时性能仅降 1.7%。

**[BayesG: Bayesian Ego-Graph Inference for Networked Multi-Agent Reinforcement Learning](autonomous_driving/bayesian_ego-graph_inference_for_networked_multi-agent_reinforcement_learning.md)**

:   BayesG 让网络化 MARL 中的每个 agent 通过贝叶斯变分推断学习其局部通信图的动态结构——用 Gumbel-Softmax 采样边掩码、ELBO 目标联合优化策略和图结构，在 167 agent 的纽约交通场景中奖励比最佳 baseline 高 50%+。

**[Causality Meets Locality: Provably Generalizable and Scalable Policy Learning for Networked Systems](autonomous_driving/causality_meets_locality_provably_generalizable_and_scalable_policy_learning_for.md)**

:   提出 GSAC 框架，将因果表示学习与元 Actor-Critic 结合，通过从网络 MARL 中学习稀疏因果掩码构建近似紧凑表示 (ACR) 实现可扩展性，通过域因子条件化策略实现跨域泛化，给出了因果恢复、收敛和自适应间隙的有限样本保证。

**[Chronograph A Real-World Graph-Based Multivariate Time Series Dataset](autonomous_driving/chronograph_a_real-world_graph-based_multivariate_time_series_dataset.md)**

:   提出 ChronoGraph——首个同时包含多元时间序列、显式服务依赖图和事件标签的真实世界微服务数据集（6个月 / ~700服务 / 5维指标 / 8005时间步），基准测试表明现有预测和异常检测方法在长期预测和拓扑感知方面均存在较大提升空间。

**[Continuous Simplicial Neural Networks](autonomous_driving/continuous_simplicial_neural_networks.md)**

:   提出 COSIMO，首个基于偏微分方程（PDE）的连续单纯形神经网络，通过在 Hodge Laplacian 上定义热扩散动力学实现连续信息流，比离散 SNN 具有更好的稳定性和过平滑控制能力。

**[CuMoLoS-MAE: A Masked Autoencoder for Remote Sensing Data Reconstruction](autonomous_driving/cumolos-mae_a_masked_autoencoder_for_remote_sensing_data_reconstruction.md)**

:   提出 CuMoLoS-MAE，一种结合课程掩码策略和 Monte Carlo 随机集成的 Masked Autoencoder，用于遥感大气廓线数据的高保真重建与逐像素不确定性量化。

**[CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation](autonomous_driving/cymbadiff_structured_spatial_diffusion_for_sketch-based_3d_semantic_urban_scene_.md)**

:   提出首个"草图→3D户外语义场景"生成任务与基准数据集 SketchSem3D，并设计 CymbaDiff（Cylinder Mamba Diffusion）去噪网络，通过柱坐标扫描+笛卡尔扫描的双路 Mamba 块实现结构化空间建模，在 FID 上比 3D Latent Diffusion 低 75%、比 3D DiT 低 71%。

**[DBLoss: Decomposition-based Loss Function for Time Series Forecasting](autonomous_driving/dbloss_decomposition-based_loss_function_for_time_series_forecasting.md)**

:   提出 DBLoss——一种基于指数移动平均分解的通用损失函数，在预测窗口内将预测值与真实值分别分解为季节和趋势分量并分开计算损失，可即插即用替换 MSE 为任意深度学习预测模型带来一致性提升，在 8 个基准数据集 × 8 个 SOTA 模型上全面验证有效性。

**[DINO-Foresight: Looking into the Future with DINO](autonomous_driving/dino-foresight_looking_into_the_future_with_dino.md)**

:   提出 DINO-Foresight，在视觉基础模型（VFM）的语义特征空间中预测未来帧特征演化，通过自监督 Masked Feature Transformer 预测 DINOv2 多层特征的 PCA 压缩表示，搭配即插即用的 task-specific heads，单一模型同时完成语义分割、实例分割、深度估计和表面法线预测四项任务，大幅超越 VISTA 世界模型且推理快 100 倍。

**[DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving](autonomous_driving/drivedpo_policy_learning_via_safety_dpo_for_end-to-end_autonomous_driving.md)**

:   提出DriveDPO两阶段框架——先通过统一策略蒸馏将人类模仿相似度与规则安全分数融合为单一监督分布，再用Safety DPO构建"看似human-like但不安全 vs 既human-like又安全"的轨迹偏好对进行策略微调——在NAVSIM上达PDMS 90.0新SOTA。

**[Extremely Simple Multimodal Outlier Synthesis for Out-of-Distribution Detection and Segmentation](autonomous_driving/extremely_simple_multimodal_outlier_synthesis_for_out-of-distribution_detection_.md)**

:   提出 Feature Mixing——一种极其简单的多模态异常值合成方法，从两种模态的特征中随机交换 $N$ 个维度即可生成 OOD 样本用于训练正则化，理论上保证合成异常值位于 ID 分布的低似然区域且偏移有界，在 8 个数据集 4 种模态上达到 SOTA 且比 NP-Mix 快 10×~370×。

**[Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling](autonomous_driving/flow_matching-based_autonomous_driving_planning_with_advanced_interactive_behavi.md)**

:   提出 Flow Planner——通过细粒度轨迹 token 化、交互增强时空融合架构和 flow matching + classifier-free guidance 三项协同创新，在 nuPlan Val14 上首次作为纯学习方法突破 90 分大关（90.43），在交互密集的 interPlan 基准上比 Diffusion Planner 高 8.92 分。

**[Future-Aware End-to-End Driving: Bidirectional Modeling of Trajectory Planning and Scene Evolution](autonomous_driving/future-aware_end-to-end_driving_bidirectional_modeling_of_trajectory_planning_an.md)**

:   提出 SeerDrive，通过双向建模场景演化与轨迹规划（未来感知规划 + 迭代交互），在 NAVSIM 和 nuScenes 上取得 SOTA。

**[FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](autonomous_driving/futuresightdrive_thinking_visually_with_spatiotemporal_cot_f.md)**

:   FutureSightDrive 认为自动驾驶 VLA 的文本 CoT 会把关键视觉时空信息压缩丢失，提出“视觉时空 CoT”范式：先让模型以 world model 方式生成融合未来背景、车道线和 3D 目标框的统一未来帧，再将该 imagined scene 作为推理中介供 inverse-dynamics 规划器生成轨迹，从而显著提升轨迹精度、降低碰撞并改善场景理解。

**[GSAlign: Geometric and Semantic Alignment Network for Aerial-Ground Person Re-Identification](autonomous_driving/gsalign_geometric_and_semantic_alignment_network_for_aerial-ground_person_re-ide.md)**

:   提出 GSAlign 框架，通过可学习薄板样条变换 (LTPS) 和动态对齐模块 (DAM) 分别解决空地行人重识别中几何畸变与语义不对齐问题，在 CARGO 数据集空地协议上 mAP 提升 +18.8%、Rank-1 提升 +16.8%。

**[HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning](autonomous_driving/holollm_multisensory_foundation_model_for_language-grounded_human_sensing_and_re.md)**

:   提出 HoloLLM，首次将 LiDAR、红外、毫米波雷达、WiFi 等稀有传感模态接入多模态大语言模型（MLLM），通过 Universal Modality-Injection Projector（UMIP）在数据稀缺条件下实现传感模态与文本的高效对齐，在人体动作问答和描述任务上较现有 MLLM 提升约 30%。

**[How Different from the Past? Spatio-Temporal Time Series Forecasting with Self-Supervised Deviation Learning](autonomous_driving/how_different_from_the_past_spatio-temporal_time_series_forecasting_with_self-su.md)**

:   提出 ST-SSDL 框架，通过自监督偏差学习（SSDL）捕捉当前输入与历史模式之间的动态偏差，利用可学习原型离散化隐空间并以对比损失+偏差损失实现相对距离一致性，在六个时空基准上取得 SOTA。

**[L2RSI: Cross-View LiDAR-Based Place Recognition for Large-Scale Urban Scenes via Remote Sensing Imagery](autonomous_driving/l2rsi_cross-view_lidar-based_place_recognition_for_large-scale_urban_scenes_via_.md)**

:   提出 L2RSI，首个利用高分辨率遥感影像实现超大规模（100km²）城市场景 LiDAR 位置识别的框架，通过语义对比学习对齐 LiDAR BEV 与遥感语义空间，并引入时空粒子估计（STPE）聚合连续查询的时空信息，在 100km² 范围内 Top-1 精度达 83.27%。

**[LabelAny3D: Label Any Object 3D in the Wild](autonomous_driving/labelany3d_label_any_object_3d_in_the_wild.md)**

:   提出 LabelAny3D，一个基于分析合成（analysis-by-synthesis）的自动 3D 标注流水线，从单目图像重建完整 3D 场景以获取高质量 3D 包围框标注；基于此构建了 COCO3D 基准，覆盖 80 类日常物体，在开放词汇单目 3D 检测上显著提升性能。

**[Layer-wise Modality Decomposition for Interpretable Multimodal Sensor Fusion](autonomous_driving/layer-wise_modality_decomposition_for_interpretable_multimodal_sensor_fusion.md)**

:   提出 LMD（Layer-Wise Modality Decomposition），一种事后、模型无关的可解释性方法，通过逐层线性化神经网络操作将多模态融合模型的预测精确分解为各传感器模态的贡献，首次实现了自动驾驶感知模型中对单个输入模态的预测归因，并在 camera-radar、camera-LiDAR、camera-radar-LiDAR 多种融合设置下验证了有效性。

**[FlowScene: Learning Temporal 3D Semantic Scene Completion via Optical Flow Guidance](autonomous_driving/learning_temporal_3d_semantic_scene_completion_via_optical_flow_guidance.md)**

:   提出 FlowScene，利用光流引导时序特征聚合并结合遮挡掩码进行体素细化，在仅使用2帧历史输入的条件下，在 SemanticKITTI 和 SSCBench-KITTI-360 基准上达到 SOTA（mIoU 17.70 / 20.81）。

**[Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation](autonomous_driving/leveraging_depth_and_language_for_open-vocabulary_domain-generalized_semantic_se.md)**

:   提出Vireo框架，首次将开放词汇语义分割（OVSS）和域泛化语义分割（DGSS）统一到单阶段框架中，通过GeoText Query融合深度几何特征与语言线索，在极端环境和未见类别上均实现SOTA表现。

**[Model-Based Policy Adaptation for Closed-Loop End-to-End Autonomous Driving](autonomous_driving/model-based_policy_adaptation_for_closed-loop_end-to-end_autonomous_driving.md)**

:   提出 MPA 框架，通过 3DGS 仿真生成反事实轨迹数据，训练扩散策略适配器和多原则 Q 值模型，在推理时引导预训练 E2E 驾驶模型提升闭环场景下的安全性和泛化能力。

**[Neurosymbolic Diffusion Models](autonomous_driving/neurosymbolic_diffusion_models.md)**

:   本文提出神经符号扩散模型（NeSyDM），通过将离散掩码扩散模型与符号程序结合，突破了传统神经符号预测器中概念条件独立假设的限制，在保持可扩展性的同时建模概念间依赖关系和不确定性，在视觉推理和自动驾驶任务上取得了 SOTA 准确率和校准性能。

**[Regret Lower Bounds for Decentralized Multi-Agent Stochastic Shortest Path Problems](autonomous_driving/regret_lower_bounds_for_decentralized_multi-agent_stochastic_shortest_path_probl.md)**

:   本文首次为去中心化多智能体随机最短路径问题（Dec-MASSP）在线性函数逼近设定下建立了 $\Omega(\sqrt{K})$ 的 regret 下界，通过构造难以学习的实例族并利用对称性论证识别最优策略结构，证明了该下界与已有上界在 episode 数 $K$ 上达到匹配。

**[SDTagNet: Leveraging Text-Annotated Navigation Maps for Online HD Map Construction](autonomous_driving/sdtagnet_leveraging_text-annotated_navigation_maps_for_online_hd_map_constructio.md)**

:   提出 SDTagNet，首次通过 BERT 编码 OpenStreetMap 文本标注（路名/车道数/单行道等）并用点级图 Transformer 编码所有 SD 地图元素（点/线/关系），在远距离 HD 地图构建上相比无先验方法提升 +5.9 mAP（+45%），超越已有 SD 地图先验方法 +3.2 mAP（+20%）。

**[SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration](autonomous_driving/simworld-robotics_synthesizing_photorealistic_and_dynamic_urban_environments_for.md)**

:   提出 SimWorld-Robotics (SWR)，一个基于 Unreal Engine 5 的大规模城市仿真平台，支持程序化生成无限逼真城市环境，并以此构建了多模态导航（SimWorld-MMNav）和多机器人搜索（SimWorld-MRS）两个新 benchmark，揭示了当前 VLM 在户外城市任务中的严重能力缺陷。

**[Towards Foundational LiDAR World Models with Efficient Latent Flow Matching](autonomous_driving/towards_foundational_lidar_world_models_with_efficient_latent_flow_matching.md)**

:   本文提出首个**可迁移的 LiDAR 世界模型**，通过 Swin Transformer VAE 实现 192× 高压缩比（SOTA 重建精度）、条件流匹配（CFM）替代扩散模型实现 SOTA 语义占据预测（仅需前人 4.38% FLOPs），并在三种域迁移任务中以 5% 标注数据超越 OccWorld 全量训练。

**[TranSUN: A Preemptive Paradigm to Eradicate Retransformation Bias Intrinsically from Regression Models in Recommender Systems](autonomous_driving/transun_a_preemptive_paradigm_to_eradicate_retransformation_bias_intrinsically_f.md)**

:   针对推荐系统中变换 MSE 回归模型的逆变换偏差（retransformation bias）问题，提出先发制人（preemptive）的 TranSUN 方法，通过联合学习辅助分支显式建模偏差，在训练阶段即从模型内部消除偏差，具有理论无偏保证和良好收敛性，并已部署在淘宝首页猜你喜欢的商品和短视频推荐场景。

**[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](autonomous_driving/unifying_appearance_codes_and_bilateral_grids_for_driving_scene_gaussian_splatti.md)**

:   提出多尺度双边网格金字塔统一全局外观编码和像素级双边网格——3 级层级（粗→中→细）分别捕捉全局/区域/像素级光度变化，通过亮度引导的切片-融合管线和自适应正则化解决驾驶场景 3DGS 的光度不一致问题，Waymo 上 Chamfer Distance 比 OmniRe 改善 28.2%。

---

## 🤖 机器人/具身智能 { #robotics }

**[A Snapshot of Influence: A Local Data Attribution Framework for Online Reinforcement Learning](robotics/a_snapshot_of_influence_a_local_data_attribution_framework_f.md)**

:   首次将数据归因（data attribution）引入在线强化学习，提出局部归因框架量化每条训练记录对策略更新的贡献，并基于此设计了迭代影响力过滤算法（IIF），在经典RL基准和LLM的RLHF上均显著提升了样本效率和最终性能。

**[Adaptive Frontier Exploration on Graphs with Applications to Network-Based Disease Testing](robotics/adaptive_frontier_exploration_on_graphs_with_applications_to_network-based_disea.md)**

:   提出 Adaptive Frontier Exploration on Graphs (AFEG) 问题框架，设计基于 Gittins index 的策略，在图是森林时可证明最优，在实际性传播疾病检测网络上仅测试一半人口即可检出几乎全部 HIV 感染者，大幅超越贪心和 DQN 等基线。

**[AutoToM: Scaling Model-based Mental Inference via Automated Agent Modeling](robotics/autotom_scaling_model-based_mental_inference_via_automated_agent_modeling.md)**

:   AutoToM 实现完全自动化的基于模型的心智理论推理——自动提出 agent 模型（贝叶斯网络结构）并进行贝叶斯逆规划，通过推理不确定性迭代调整模型（添加心智变量/扩展时间步），在5个 ToM benchmark 上超越 SOTA LLM 和推理模型，且产生类人的置信度估计。

**[Beyond Parallelism: Synergistic Computational Graph Effects in Multi-Head Attention](robotics/beyond_parallelism_synergistic_computational_graph_effects_in_multi-head_attenti.md)**

:   将多头注意力重新建模为共享汇节点的多个前馈 DAG 系统，理论证明多头可通过跨头路径实现协同效应——降低混合时间(mixing time)并放大 minimax 保真度(fidelity)，在序列操作任务上实验验证了该效应。

**[Bridging Embodiment Gaps: Deploying Vision-Language-Action Models on Soft Robots](robotics/bridging_embodiment_gaps_deploying_vision-language-action_models_on_soft_robots.md)**

:   首次在柔性连续体机械臂上部署 VLA 模型（OpenVLA-OFT 和 π₀），发现开箱即用的策略因构型不匹配完全失败，但通过针对性微调可弥合刚性-柔性的 embodiment gap，使柔性机器人在操作任务上达到与刚性 UR5 相当的成功率——证明 VLA + 柔性机器人可实现安全的人机交互。

**[C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](robotics/c-nav_towards_self-evolving_continual_object_navigation_in_open_world.md)**

:   提出 C-Nav 框架，通过**双路径抗遗忘**（特征蒸馏 + 特征回放）和**自适应经验选择**（LOF 异常检测选关键帧），让导航智能体在不断学习新物体类别时避免灾难性遗忘，在 4 种架构上均超越全量数据回放基线。

**[Can Agents Fix Agent Issues](robotics/can_agents_fix_agent_issues.md)**

:   AgentIssue-Bench(50个bug任务)评估SE代理解决LLM代理bug的能力，仅0.67%-4.67%解决率。

**[CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification](robotics/cogvla_cognition-aligned_vision-language-action_model_via_instruction-driven_rou.md)**

:   提出 CogVLA——模仿人类多模态认知的三阶段 VLA 架构：(1) EFA-Routing 将视觉 token 压缩至 25%；(2) LFP-Routing 裁剪 50% 的 LLM 无关 token；(3) V-L-A 耦合注意力保持语义一致性——在 LIBERO 上达 97.4% 成功率，训练成本降 2.5×，推理延迟降 2.8×。

**[C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](robotics/coopera_continual_open-ended_human-robot_assistance.md)**

:   提出 C-Nav 持续目标导航框架，通过**双路径抗遗忘机制**（特征蒸馏 + 特征回放）和**基于 LOF 的自适应经验选择**，使导航智能体在增量学习新物体类别时有效避免灾难性遗忘，在 4 种主流架构和 2 个数据集上均超越全量数据回放基线。

**[DexFlyWheel: A Scalable Self-Improving Data Generation Framework for Dexterous Manipulation](robotics/dexflywheel_a_scalable_and_self-improving_data_generation_framework_for_dexterou.md)**

:   提出 DexFlyWheel，一个从单个人类示教出发、通过 IL + 残差 RL + 数据增强组成的自改进循环逐步扩展数据多样性的灵巧操作数据生成框架，在 4 个任务上生成 2000+ 示教，策略平均成功率 81.9%，真实世界迁移成功率 78.3%。

**[DynaNav: Dynamic Feature and Layer Selection for Efficient Visual Navigation](robotics/dynanav_dynamic_feature_and_layer_selection_for_efficient_visual_navigation.md)**

:   提出 DynaNav，通过可训练的硬特征选择器和基于贝叶斯优化的 early-exit 机制，根据场景复杂度动态调整特征与层的使用，在视觉导航中实现 2.26× FLOPs 降低、42.3% 推理时间减少，同时保持甚至提升导航性能。

**[EfficientNav: Towards On-Device Object-Goal Navigation with Navigation Map Caching and Retrieval](robotics/efficientnav_towards_on-device_object-goal_navigation_with_navigation_map_cachin.md)**

:   通过离散内存缓存（KV cache分组独立计算+选择性加载）、注意力驱动聚类（LLM浅层attention指导分组）和语义感知检索（CLIP+背包问题适配不同内存预算），首次在Jetson Orin上用LLaMA-3.2-11b实现零样本ObjNav，比GPT-4基线提升11.1% SR且实时延迟降低6.7×。

**[EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT](robotics/egothinker_unveiling_egocentric_reasoning_with_spatiotempora.md)**

:   针对第一人称视频推理中“主体不可见、意图隐含、交互细粒度”的挑战，EgoThinker 提出时空 CoT 监督与两阶段训练（SFT + RFT），并构建 EgoRe-5M 大规模 egocentric QA 数据，显著提升 MLLM 在自我中心视频推理与时空定位任务上的表现。

**[Enginuity: Building an Open Multi-Domain Dataset of Complex Engineering Diagrams](robotics/enginuity_building_an_open_multi-domain_dataset_of_complex_engineering_diagrams.md)**

:   提出 Enginuity——首个大规模开放多领域工程图数据集（50K+ 标注图），涵盖层级组件关系与连接语义，旨在突破当前 AI 无法理解工程图中视觉-结构知识的瓶颈。

**[Explaining and Mitigating Crosslingual Tokenizer Inequities](robotics/explaining_and_mitigating_crosslingual_tokenizer_inequities.md)**

:   系统训练约 7000 个单语分词器覆盖 97 种语言，首次证明即使控制训练数据量、词表大小和算法后，不同语言间仍存在显著的 token premium 差异；进一步识别出词表大小和预分词策略是关键因素，并提出"最优词表大小"和 SuperBPE 两种缓解方案。

**[FALCON: Fine-grained Activation Manipulation by Contrastive Orthogonal Unalignment for Large Language Model](robotics/falcon_fine-grained_activation_manipulation_by_contrastive_orthogonal_unalignmen.md)**

:   提出 FALCON——基于表示引导的 LLM 遗忘框架，利用互信息进行参数选择、对比机制实现精细知识分离、梯度正交投影解决遗忘-保留冲突，在有害知识/版权/实体遗忘任务上全面超越现有方法。

**[Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training](robotics/generalizable_domain_adaptation_for_sim-and-real_policy_co-training.md)**

:   提出基于不平衡最优运输（UOT）的模拟-真实策略联合训练框架，通过对观察-动作联合分布进行对齐（而非仅对齐观察边际分布），结合时间对齐采样策略处理数据不平衡，在机器人操纵任务上实现30%的OOD泛化提升。

**[Harnessing the Computation Redundancy in ViTs to Boost Adversarial Transferability](robotics/harnessing_the_computation_redundancy_in_vits_to_boost_adversarial_transferabili.md)**

:   深入挖掘 ViT 中数据级和模型级的计算冗余，提出注意力稀疏化、注意力头置换、干净 token 正则化、Ghost MoE 多样化和鲁棒化 token 五种技术，结合在线学习策略动态选择操作，在 ImageNet-1K 上以 86.9% 平均 fooling rate 大幅超越所有基线。

**[HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data](robotics/himacon_discovering_hierarchical_manipulation_concepts_from_unlabeled_multi-moda.md)**

:   提出自监督框架从无标注多模态机器人演示中学习层级操作概念，通过跨模态相关性网络和多时域子目标预测器组织表示，增强模仿学习策略在新物体、新障碍和新环境下的泛化能力。

**[Knolling Bot: Teaching Robots the Human Notion of Tidiness](robotics/knolling_bot_teaching_robots_the_human_notion_of_tidiness.md)**

:   提出基于 Transformer + GMM 的自监督学习框架，让机器人从 240 万组整理示范中学习"整洁"的抽象概念，以自回归方式预测物体目标位置，实现桌面物体的美观且紧凑的自动整理（knolling），并支持基于用户偏好（颜色/类别/大小）生成多样化整理方案。

**[LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](robotics/labutopia_high-fidelity_simulation_and_hierarchical_benchmark_for_scientific_emb.md)**

:   提出 LabUtopia——面向科学实验室的高保真仿真与层级基准套件，包含支持化学反应建模的 LabSim 仿真器、可程序化生成实验室场景的 LabScene、以及从原子操作到长程移动操纵的五级 LabBench 基准，揭示现有模仿学习方法在长程实验流程和物体泛化方面的显著瓶颈。

**[LatentGuard: Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation](robotics/latentguard_controllable_latent_steering_for_robust_refusal_of_attacks_and_relia.md)**

:   提出 LatentGuard 三阶段框架，通过行为级对齐微调 + 结构化 VAE 监督潜空间 + 潜空间维度操控，实现对 LLM 拒绝行为的可解释、可控制调节，在抵御对抗攻击的同时保持对正常查询的响应能力。

**[Learning Spatial-Aware Manipulation Ordering](robotics/learning_spatial-aware_manipulation_ordering.md)**

:   提出 OrderMind 统一框架，通过空间上下文编码器和时序优先级结构化模块直接从 RGB-D 图像学习杂乱场景中物体的操作顺序，利用 VLM 蒸馏生成训练标注，在仿真和真实环境中均显著优于 VLM 基线，且支持实时推理（5.6 FPS，轻量版 21.3 FPS）。

**[LLM World Models Are Mental: Output Layer Evidence of Brittle World Model Use in LLM Mechanical Reasoning](robotics/llm_world_models_are_mental_output_layer_evidence_of_brittle_world_model_use_in_.md)**

:   借鉴认知科学的心理模型研究方法，通过滑轮系统的TikZ代码表示测试LLM的力学推理能力，发现LLM能近似估计机械优势并区分功能/非功能系统（Study 1&2），但在精细结构连接推理上完全失败（Study 3），表明LLM的"世界模型"存在但脆弱。

**[Manipulating Feature Visualizations With Gradient Slingshots](robotics/manipulating_feature_visualizations_with_gradient_slingshots.md)**

:   提出梯度弹弓攻击，通过利用分布外梯度轨迹操纵神经网络特征可视化结果，无需修改模型参数，揭示特征可视化作为解释性工具的脆弱性。

**[MindForge: Empowering Embodied Agents with Theory of Mind for Lifelong Cultural Learning](robotics/mindforge_empowering_embodied_agents_with_theory_of_mind_for_lifelong_cultural_l.md)**

:   MindForge 为 LLM 驱动的具身智能体引入显式的心智理论（ToM）表征、自然语言通信和多组件记忆系统，使开源 LLM 智能体通过与专家协作对话（无需梯度更新）大幅提升任务完成率，在 Minecraft 中比 Voyager 多获得 3× 科技树里程碑和 2.3× 独特物品。

**[MineAnyBuild: Benchmarking Spatial Planning for Open-world AI Agents](robotics/mineanybuild_benchmarking_spatial_planning_for_openworld_ai.md)**

:   基于 Minecraft 构建空间规划基准 MineAnyBuild，要求 AI Agent 根据多模态指令生成可执行的建筑蓝图矩阵，包含 4000 个任务和 500+ 建筑/装饰资产，从空间理解、空间推理、创造力和空间常识四个维度系统评估 MLLM 的空间规划能力，揭示即便 GPT-4o 整体得分仅 41.02/100，开源模型更差。

**[MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents](robotics/mip_against_agent_malicious_image_patches_hijacking_multimod.md)**

:   揭示针对多模态OS Agent的新型攻击向量——Malicious Image Patches (MIPs)：在屏幕截图中嵌入人类不可察觉的对抗性扰动图像块，当OS Agent截屏时自动触发恶意行为（如数据泄露、内存溢出），且可跨用户指令、屏幕布局和屏幕解析器泛化，甚至具备"计算机蠕虫"般的自传播潜力。

**[mmWalk: Towards Multi-modal Multi-view Walking Assistance](robotics/mmwalk_towards_multi-modal_multi-view_walking_assistance.md)**

:   mmWalk 构建了首个面向视障人群步行辅助的多模态多视角数据集（CARLA 仿真器生成 62K 帧/559K 全景图 + 69K VQA 对），基准测试发现 SOTA VLM 在风险评估和导航地标识别等安全关键任务上表现不足（最优仅 55.21%），微调后在真实数据集上泛化提升 16.7%。

**[SegMASt3R: Geometry Grounded Segment Matching](robotics/segmast3r_geometry_grounded_segment_matching.md)**

:   SegMASt3R 在预训练 MASt3R 3D 基础模型上添加轻量分割特征头和可微 Sinkhorn 匹配层，利用 3D 几何先验实现极端视角变化（达 180°）下的鲁棒语义段匹配，AUPRC 在 135-180° 基线上达 83.6%（vs SAM2 的 17%）。

**[Talk2Event: Grounded Understanding of Dynamic Scenes from Event Cameras](robotics/talk2event_grounded_understanding_of_dynamic_scenes_from_event_cameras.md)**

:   Talk2Event 提出首个大规模事件相机视觉定位基准（30,690 条标注表达式 + 四种定位属性），并设计 EventRefer 框架通过混合事件-属性专家（MoEE）动态融合外观/状态/观察者关系/物体间关系特征，在纯事件、纯帧和融合三种设置下均超越现有方法。

**[Toward Engineering AGI: Benchmarking the Engineering Design Capabilities of LLMs](robotics/toward_engineering_agi_benchmarking_the_engineering_design_capabilities_of_llms.md)**

---

## 🎵 音频/语音 { #audio_speech }

**[A Controllable Examination for Long-Context Language Models](audio_speech/a_controllable_examination_for_longcontext_language_models.md)**

:   提出LongBioBench，通过生成虚构传记作为可控的needle和haystack，构建满足"无缝上下文、可控设置、可靠评估"三大原则的长上下文LLM评估框架，测试18个模型后揭示当前LCLM在检索能力尚可的情况下推理和可信性仍有显著短板。

**[A TRIANGLE Enables Multimodal Alignment Beyond Cosine Similarity](audio_speech/a_triangle_enables_multimodal_alignment_beyond_cosine_simila.md)**

:   TRIANGLE提出用三模态嵌入向量端点构成的三角形面积作为相似度度量，替代传统的两两余弦相似度，实现视频-音频-文本的联合对齐，在视频检索任务上比VAST提升最高9个R@1点。

**[Accelerate Creation of Product Claims Using Generative AI](audio_speech/accelerate_creation_of_product_claims_using_generative_ai.md)**

:   开发 Claim Advisor 平台，利用 LLM 的 in-context learning 和 LoRA 微调加速消费品产品宣称的搜索、生成、优化和排序，通过模仿 MaxDiff 研究方法论让微调的 Phi-3 14B 模型在宣称排序上超越 GPT-4o（仅用 1 个示例 vs GPT 的 100 个示例），三轮迭代后 100% 的生成宣称达到"高吸引力"级别。

**[AdaptDel: Adaptable Deletion Rate Randomized Smoothing for Certified Robustness](audio_speech/adaptdel_adaptable_deletion_rate_randomized_smoothing_for_ce.md)**

:   提出AdaptDel方法，将随机平滑(randomized smoothing)中的固定删除率扩展为**自适应删除率**，根据输入长度等属性动态调整删除概率，在编辑距离攻击下实现认证鲁棒性的巨大提升（认证区域基数提升最高30个数量级）。

**[Associative Syntax and Maximal Repetitions Reveal Context-Dependent Complexity in Animal Vocalizations](audio_speech/associative_syntax_and_maximal_repetitions_reveal_context-dependent_complexity_i.md)**

:   提出基于"关联句法"和"最大重复"的信息论框架分析动物发声序列的结构复杂度，发现动物发声（如鲸鱼歌声）展现出上下文依赖的复杂句法结构，超越了简单的马尔可夫假设。

**[AudSemThinker: Enhancing Audio-Language Models through Reasoning over Semantics of Sound](audio_speech/audsemthinker_enhancing_audio-language_models_through_reasoning_over_semantics_o.md)**

:   AudSemThinker 为音频语言模型引入结构化语义推理框架——定义 9 类声音语义描述符（谁/什么/如何/何时/何地等），在 Qwen2.5-Omni-7B 上通过 SFT + GRPO（含可验证奖励和长度约束）训练产生 \<think\>\<semantic_elements\>\<answer\> 三阶段输出，MMAU 基准达 66.70%（超越 Audio-Reasoner 61.71% 和 Qwen2.5-Omni 65.60%）。

**[Benchmarking Egocentric Multimodal Goal Inference for Assistive Wearable Agents](audio_speech/benchmarking_egocentric_multimodal_goal_inference_for_assist.md)**

:   Meta 提出 WAGIBench，一个针对可穿戴辅助智能体的多模态目标推断基准，包含 348 名参与者的 3,477 条第一视角录制（29小时），涵盖视觉/音频/数字/纵向四种模态，人类准确率 93% vs 最佳 VLM 84%（MCQ），生成式评估中模型仅 55% 时间产生相关目标，揭示了当前 VLM 在实际可穿戴场景中的显著差距。

**[BNMusic: Blending Environmental Noises into Personalized Music](audio_speech/bnmusic_blending_environmental_noises_into_personalized_music.md)**

:   提出 BNMusic，一个两阶段框架将环境噪声融合到个性化生成音乐中：第一阶段通过 mel-spectrogram 的 outpainting + inpainting 生成与噪声节奏对齐的音乐，第二阶段利用听觉掩蔽理论自适应放大音乐信号以降低噪声感知，无需额外训练，在 EPIC-SOUNDS 和 ESC-50 上显著优于 baseline。

**[Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation](audio_speech/can_llms_outshine_conventional_recommenders_a_comparative_evaluation.md)**

:   提出 RecBench 综合评估框架，在5个领域数据集上系统对比17个LLM与10个传统DLRM，发现LLM推荐器在CTR任务上AUC提升最高5%、在序列推荐上NDCG@10提升最高170%，但推理速度慢10-1000倍，而传统DLRM结合LLM语义嵌入（LLM-for-RS）可以20倍更快的速度达到LLM约95%的性能，是当前最具工业可行性的方案。

**[DeepASA: An Object-Oriented Multi-Purpose Network for Auditory Scene Analysis](audio_speech/deepasa_an_object-oriented_multi-purpose_network_for_auditory_scene_analysis.md)**

:   提出 DeepASA，一个面向对象的多任务统一架构，通过 object-oriented processing 和 chain-of-inference 机制在单一模型中同时完成多通道声源分离（MIMO）、去混响、声事件检测（SED）、音频分类和到达方向估计（DoAE），在多个空间音频基准上达到 SOTA。

**[E-BATS: Efficient Backpropagation-Free Test-Time Adaptation for Speech Foundation Models](audio_speech/e-bats_efficient_backpropagation-free_test-time_adaptation_for_speech_foundation.md)**

:   提出首个面向语音基础模型的无反向传播测试时自适应框架 E-BATS，通过轻量级 prompt 自适应、多尺度损失函数和测试时 EMA 机制，在保持高精度的同时实现 2.0×–6.4× 的 GPU 显存节省。

**[E2E-VGuard: Adversarial Prevention for Production LLM-based End-To-End Speech Synthesis](audio_speech/e2e-vguard_adversarial_prevention_for_production_llm-based_end-to-end_speech_syn.md)**

:   针对基于 LLM 的端到端语音合成中的声音克隆威胁，提出 E2E-VGuard 主动防御框架，通过编码器集成扰动音色、对抗样本干扰 ASR 发音识别、以及心理声学模型保证不可感知性，在 19 个 TTS 模型和 7 个 ASR 系统上验证了有效性。

**[Echoes of Humanity: Exploring the Perceived Humanness of AI Music](audio_speech/echoes_of_humanity_exploring_the_perceived_humanness_of_ai_music.md)**

:   通过随机对照交叉试验(RCCT)和混合方法内容分析，系统研究听众区分AI生成音乐(AIM)与人类创作音乐的能力，发现随机配对时听众无法区分（准确率≈随机猜测），但相似配对时显著提升至66%，且声音/技术/人声线索是成功区分的关键因素。

**[Efficient Speech Language Modeling via Energy Distance in Continuous Latent Space](audio_speech/efficient_speech_language_modeling_via_energy_distance_in_continuous_latent_spac.md)**

:   提出 SLED，将语音波形编码为连续潜在表示序列，在连续空间中通过 energy distance 目标进行自回归建模，避免了离散化信息损失和 RVQ 所需的复杂层级架构，同时实现高效的零样本与流式语音合成。

**[Embedding Alignment in Code Generation for Audio](audio_speech/embedding_alignment_in_code_generation_for_audio.md)**

:   提出双 MLP + InfoNCE 对比学习框架，将代码嵌入（distilroberta-base）和音频嵌入（wav2vec2）对齐到共享空间，使 LLM 代码生成流程无需编译执行即可从代码推断音乐相似性，CKA 从 0.090 提升至 0.590。

**[Ethics Statements in AI Music Papers: The Effective and the Ineffective](audio_speech/ethics_statements_in_ai_music_papers_the_effective_and_the_ineffective.md)**

:   对 AI 音乐领域论文中伦理声明（ethics statements）的使用现状进行系统审查，发现绝大多数伦理声明未被有效利用，并提出面向会议与研究者的改进建议。

**[EuroSpeech: A Multilingual Speech Corpus](audio_speech/eurospeech_a_multilingual_speech_corpus.md)**

:   提出可扩展的开源 pipeline，从 22 个欧洲议会录音中自动构建 EuroSpeech 数据集——61K 小时、覆盖 22 种语言的高质量语音-文本对齐数据，其中 19 种语言超 1K 小时，微调 Whisper 后平均 WER 降低 41.8%。

**[Generating Physically Sound Designs from Text and a Set of Physical Constraints](audio_speech/generating_physically_sound_designs_from_text_and_a_set_of_physical_constraints.md)**

:   提出 TIDES 框架，将预训练文本-图像模型（CLIP）的视觉引导与可微有限元物理仿真器结合，通过联合优化视觉相似度损失和结构合规性损失，从文本描述和物理约束出发生成既满足工程性能要求又具备文本指定特征的承载结构设计，并通过 3D 打印三点弯曲实验验证了方法的有效性。

**[Instance-Specific Test-Time Training for Speech Editing in the Wild](audio_speech/instance-specific_test-time_training_for_speech_editing_in_the_wild.md)**

:   提出面向野外语音编辑的实例特定测试时训练方法：在推理前利用未编辑区域的真实声学特征做直接监督、编辑区域通过时长约束和音素预测辅助损失做间接监督，对模型进行实例级自适应微调，有效缓解编辑边界的带宽不连续问题，并支持通过 mask 长度调整精确控制语速，在野外 benchmark 上主客观评估均超越现有系统。

**[Latent Space Factorization in LoRA](audio_speech/latent_space_factorization_in_lora.md)**

:   提出 FVAE-LoRA，在 LoRA 框架中引入具有双潜空间的 VAE，通过新型 ELBO 目标将任务相关特征 ($\mathbf{z}_1$) 与残差信息 ($\mathbf{z}_2$) 显式分解，在文本、图像、音频任务上一致优于标准 LoRA。

**[LeVo: High-Quality Song Generation with Multi-Preference Alignment](audio_speech/levo_high-quality_song_generation_with_multi-preference_alignment.md)**

:   提出 LeVo 歌曲生成框架，通过语言模型并行建模混合 token 和双轨 token 以兼顾人声-伴奏和谐性和音质，并创新性地引入基于 DPO 的多偏好对齐方法提升音乐性和指令跟随能力。

**[LeVo: High-Quality Song Generation with Multi-Preference Alignment](audio_speech/levo_high-quality_song_generation_with_multi-processing_refined_supervision.md)**

:   LeVo 提出一种基于语言模型的歌曲生成框架，通过并行预测混合 token 和双轨 token 来同时优化人声-伴奏和谐度与音质，并引入基于 DPO 的多偏好对齐方法提升音乐性和指令跟随能力，在学术方法中全面领先且接近工业系统水平。

**[MEGADance: Mixture-of-Experts Architecture for Genre-Aware 3D Dance Generation](audio_speech/megadance_mixture-of-experts_architecture_for_genre-aware_3d_dance_generation.md)**

:   提出 MEGADance，首个基于混合专家 (MoE) 架构的音乐驱动 3D 舞蹈生成方法，通过将编舞一致性解耦为"舞蹈通用性"（Universal Expert）和"风格特异性"（Specialized Expert），配合 FSQ 量化和 Mamba-Transformer 混合骨干网络，实现了 SOTA 的舞蹈质量和强风格可控性。

**[Multi-head Temporal Latent Attention](audio_speech/multi-head_temporal_latent_attention.md)**

:   MTLA 在 MLA 低秩潜在维度压缩基础上，用超网络动态融合时序相邻的 KV 向量，实现 KV 缓存在特征维度和时序维度的双重压缩，配合 stride-aware 因果 mask 保证训练-推理一致性，在语音翻译等任务上达到 4.29× 加速和 6.58× 内存降低，质量持平甚至略优于标准 MHA。

**[Perceptually Aligning Representations of Music via Noise-Augmented Autoencoders](audio_speech/perceptually_aligning_representations_of_music_via_noise-augmented_autoencoders.md)**

:   证明在自编码器训练中对潜变量加噪（noise-augmented latent training）配合感知损失，能使编码空间形成"感知层次结构"——感知最显著的音乐特征（如音高）编码在最粗粒度的潜在结构中，而次要特征（如音色细节）编码在细粒度结构中。这种对齐改善了潜在扩散解码下的音乐惊奇感估计和 EEG 脑响应预测。

**[SAND-Math: Using LLMs to Generate Novel, Difficult and Useful Mathematics Questions and Answers](audio_speech/sand-math_using_llms_to_generate_novel_difficult_and_useful_mathematics_question.md)**

:   提出 SAND-Math，一个无需种子数据集的全自动合成数学问题生成管线，通过 Difficulty Hiking 系统性提升题目难度，仅 500 道增强 LIMO 基线即可在 AIME25 上提升 4.39pp。

**[Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI Models in Sound Localization](audio_speech/seeing_sound_hearing_sight_uncovering_modality_bias_and_conflict_of_ai_models_in.md)**

:   系统性地揭示了AI声源定位(SSL)模型存在严重视觉偏见——在视听冲突时降到随机水平，提出神经科学启发的EchoPin模型（HRTF滤波+耳蜗图+立体声），在AudioCOCO数据集上大幅超越现有方法并展现出类人的水平>垂直定位精度偏差。

**[Sound Logical Explanations for Mean Aggregation Graph Neural Networks](audio_speech/sound_logical_explanations_for_mean_aggregation_graph_neural_networks.md)**

:   针对使用均值聚合函数的 GNN（MAGNN，即非负权重的 mean-GNN），证明了能够作为其 sound 解释的单调逻辑规则的精确类别，并构造了一个一阶逻辑的受限片段来解释任意 MAGNN 预测，实验表明限制非负权重不显著影响性能且能有效提取 sound 规则。

**[AVRobustBench: Benchmarking the Robustness of Audio-Visual Recognition Models at Test-Time](audio_speech/textttavrobustbench_benchmarking_the_robustness_of_audio-visual_recognition_mode.md)**

:   提出 AVRobustBench，首个系统评估音视频模型在 **双模态共现关联腐蚀** 下测试时鲁棒性的基准，包含 4 个数据集 × 75 种腐蚀，并提出基于低熵样本筛选的 TTA 方法 AV2C。

**[The Impact of Scaling Training Data on Adversarial Robustness](audio_speech/the_impact_of_scaling_training_data_on_adversarial_robustness.md)**

:   系统评估 36 个 SOTA 视觉模型在 6 类黑盒攻击下的鲁棒性，发现攻击成功率(ASR)随数据量和模型规模按对数律下降，但 **数据质量和模型规模比数据量本身更关键**。

**[WhAM: Towards A Translative Model of Sperm Whale Vocalization](audio_speech/wham_towards_a_translative_model_of_sperm_whale_vocalization.md)**

:   提出 WhAM（Whale Acoustics Model），首个基于 Transformer 的抹香鲸 coda 生成模型，通过微调 VampNet 实现声学翻译、合成生成与下游分类的三合一能力。

---

## 🎯 目标检测 { #object_detection }

**[All You Need is One: Capsule Prompt Tuning with a Single Vector](object_detection/all_you_need_is_one_capsule_prompt_tuning_with_a_single_vector.md)**

:   提出 Capsule Prompt-Tuning (CaPT)，发现现有 task-aware soft prompts 实际上与输入 tokens 缺乏交互（"attention 孤岛"），而将 instance-aware 信息融入单个 capsule prompt 可以作为"attention anchor"激活对关键结构信息的注意力，以极低参数量（如 Llama3.2-1B 上仅 0.003% 参数）实现超越多 prompt 方法的性能。

**[Angular Constraint Embedding via SpherePair Loss for Constrained Clustering](object_detection/angular_constraint_embedding_via_spherepair_loss_for_constrained_clustering.md)**

:   提出 SpherePair loss，在角度空间（而非欧氏空间）中学习约束聚类的表示，通过余弦相似度编码 pairwise 约束，避免了端到端 DCC 方法对 anchor 的依赖和欧氏嵌入中正负对距离平衡的困难，无需预知聚类数目即可实现 SOTA 的约束聚类性能。

**[Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector](object_detection/any_large_language_model_can_be_a_reliable_judge_debiasing_w.md)**

:   提出 Reasoning-based Bias Detector（RBD）作为 LLM 评判器的即插即用去偏模块——通过外部检测 4 种评估偏见（冗长/位置/从众/情感），生成带推理链的结构化反馈引导评判器自我纠正，RBD-8B 在 8 个 LLM 评判器上平均提升准确率 18.5%、一致性 10.9%。

**[Ascent Fails to Forget](object_detection/ascent_fails_to_forget.md)**

:   挑战了机器遗忘领域的常见信念，证明梯度上升（gradient ascent）基于的无约束优化方法在遗忘/保留集之间存在统计依赖时会系统性失败——遗忘集指标的降低不可避免地损害整体测试性能，logistic 回归示例甚至展示了遗忘过程使模型比原始模型更远离 oracle 的灾难性情况。

**[Automated Detection of Visual Attribute Reliance with a Self-Reflective Agent](object_detection/automated_detection_of_visual_attribute_reliance_with_a_self-reflective_agent.md)**

:   提出一个自反思 agent 框架，通过迭代的假设生成-测试-验证-反思循环来自动检测视觉模型中的属性依赖（如 CLIP 识别 teacher 依赖教室背景、YOLOv8 检测行人依赖人行横道），在 130 个注入已知属性依赖的模型 benchmark 上显示自反思显著提升检测准确性。

**[BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes](object_detection/burstdeflicker_a_benchmark_dataset_for_flicker_removal_in_dynamic_scenes.md)**

:   提出首个面向多帧闪烁去除（MFFR）的大规模 benchmark 数据集 BurstDeflicker，包含基于 Retinex 的合成数据、真实静态数据和绿幕动态数据三个互补子集，系统解决了动态场景下闪烁-干净图像对难以获取的核心瓶颈。

**[CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection](object_detection/cq-dino_mitigating_gradient_dilution_via_category_queries_for_vast_vocabulary_ob.md)**

:   针对大规模类别（>10K）目标检测中分类头的正梯度稀释和难负样本梯度稀释问题，提出 CQ-DINO：用可学习类别查询替代分类头，通过图像引导的 Top-K 类别选择将负空间缩小 100 倍，在 V3Det（13204 类）上超越前 SOTA 2.1% AP，同时保持 COCO 竞争力。

**[BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes](object_detection/delving_into_cascaded_instability_a_lipschitz_continuity_view_on_image_restorati.md)**

:   提出首个面向动态场景的多帧去闪烁（MFFR）基准数据集 BurstDeflicker，通过 Retinex 合成、真实静态采集与绿幕合成三种互补策略构建大规模训练/测试数据，显著提升闪烁去除模型在真实动态场景中的泛化能力。

**[DetectiumFire: A Comprehensive Multi-modal Dataset Bridging Vision and Language for Fire Understanding](object_detection/detectiumfire_a_comprehensive_multi-modal_dataset_bridging_vision_and_language_f.md)**

:   DetectiumFire 构建了最大的多模态火灾理解数据集——14.5K 真实图像 + 2.5K 视频 + 8K 合成图像 + 12K RLHF 偏好对，低重复率（0.03 PHash vs D-Fire 0.15），配合 4 级严重性分类标准和详细场景描述，微调 YOLOv11m 达 mAP 43.74，微调 LLaMA-3.2-11B 火灾严重性分类 83.84%。

**[DETree: DEtecting Human-AI Collaborative Texts via Tree-Structured Hierarchical Representation Learning](object_detection/detree_detecting_human-ai_collaborative_texts_via_tree-structured_hierarchical_r.md)**

:   提出 DETree 框架，通过构建层次亲和树（HAT）建模不同人机协作文本生成过程之间的层次关系，并设计树结构对比损失（TSCL）对齐表示空间，在混合文本检测和 OOD 场景下取得了显著优势。

**[Diffusion-Classifier Synergy: Reward-Aligned Learning via Mutual Boosting Loop for FSCIL](object_detection/diffusion-classifier_synergy_reward-aligned_learning_via_mutual_boosting_loop_fo.md)**

:   提出 Diffusion-Classifier Synergy (DCS) 框架，通过在扩散模型和分类器之间建立互相增强的闭环，利用多层次奖励函数（特征级+logits级）引导扩散模型生成对分类器最有益的图像，在 FSCIL 基准上取得 SOTA。

**[DitHub: A Modular Framework for Incremental Open-Vocabulary Object Detection](object_detection/dithub_a_modular_framework_for_incremental_openvocabulary_ob.md)**

:   提出 DitHub，借鉴版本控制系统（Git）思想构建开放词汇目标检测的模块化适配框架——将不同领域的高效适配模块（LoRA）作为"分支"管理，支持按需获取（fetch）和合并（merge），在 ODinW-13 上达到 SOTA，首次系统性研究目标检测中适配模块的组合特性。

**[Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable](object_detection/dual_data_alignment_makes_ai-generated_image_detector_easier_generalizable.md)**

:   提出 Dual Data Alignment (DDA)，通过像素域和频域双重对齐生成训练用合成图像，消除数据集偏置导致的虚假相关性，使检测器仅学习伪造相关特征，在11个基准上平均准确率达到90.7%，大幅超越现有方法。

**[Dynamic Features Adaptation in Networking: Toward Flexible Training and Explainable Inference](object_detection/dynamic_features_adaptation_in_networking_toward_flexible_training_and_explainab.md)**

:   提出 DAFI（Drift-Aware Feature Importance）算法，利用分布漂移检测动态切换 SHAP/MDI 两种特征重要性方法，结合自适应随机森林（ARF）实现通信网络场景下特征动态增加时的灵活训练与高效可解释推理。

**[FlexEvent: Towards Flexible Event-Frame Object Detection at Varying Operational Frequencies](object_detection/flexevent_towards_flexible_event-frame_object_detection_at_varying_operational_f.md)**

:   提出 FlexEvent 框架，通过自适应事件-图像融合模块 FlexFuse 和频率自适应微调机制 FlexTune，实现事件相机在不同操作频率下的灵活目标检测，在 20Hz 到 180Hz 范围内保持鲁棒性能，显著超越现有方法。

**[Generalizable Insights for Graph Transformers in Theory and Practice](object_detection/generalizable_insights_for_graph_transformers_in_theory_and_practice.md)**

:   提出 Generalized-Distance Transformer (GDT)，一种基于标准注意力（无需修改注意力机制）的图 Transformer 架构，理论证明其表达力等价于 GD-WL 算法，并通过覆盖 800 万图/2.7 亿 token 的大规模实验首次建立了 PE 表达力的细粒度经验层次，在 few-shot 迁移设置下无需微调即可超越 SOTA。

**[InstanceAssemble: Layout-Aware Image Generation via Instance Assembling Attention](object_detection/instanceassemble_layoutaware_image_generation_via_instance_a.md)**

:   提出InstanceAssemble，通过实例组装注意力机制（instance-assembling attention）实现layout条件的精确控制——支持bbox位置控制和多模态内容控制（文本+视觉内容），作为轻量LoRA模块适配到现有DiT模型，同时提出DenseLayout benchmark（5K图像90K实例）和Layout Grounding Score评估指标。

**[M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization](object_detection/m-grpo_stabilizing_self-supervised_reinforcement_learning_for_large_language_mod.md)**

:   针对自监督强化学习中 LLM 策略崩溃和熵崩溃问题，提出动量锚定的 GRPO（M-GRPO）框架和基于 IQR 的低熵轨迹过滤方法，实现稳定训练和 SOTA 性能。

**[M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization](object_detection/m-grpo_stabilizing_self-supervised_reinforcement_learning_for_multimodal_underst.md)**

:   针对自监督强化学习（SS-RLVR）在长期训练中普遍出现的"策略崩溃"问题，提出 M-GRPO：通过动量模型提供稳定的伪标签目标 + 基于四分位距（IQR）的低熵轨迹过滤防止熵崩溃，在无标注 MATH 数据集上训练 Qwen3-4B-Base，最终 checkpoint 即超越 SRT 手动选取的最佳 checkpoint，AIME24 +2.92%、GPQA +5.05%。

**[MSTAR: Box-Free Multi-Query Scene Text Retrieval with Attention Recycling](object_detection/mstar_box-free_multi-query_scene_text_retrieval_with_attention_recycling.md)**

:   提出 MSTAR，首个无需边界框标注的多查询场景文本检索方法，通过渐进式视觉嵌入（PVE）逐步将注意力从显著区域转移到不显著区域，结合风格感知指令和多实例匹配模块，实现了对单词、短语、组合和语义四种查询类型的统一检索，并构建了首个多查询文本检索基准 MQTR。

**[OverLayBench: A Benchmark for Layout-to-Image Generation with Dense Overlaps](object_detection/overlaybench_a_benchmark_for_layout-to-image_generation_with_dense_overlaps.md)**

:   OverLayBench 构建了首个聚焦密集重叠场景的 Layout-to-Image 基准（4052 样本 + OverLayScore 难度指标），揭示 SOTA 方法在复杂重叠下 mIoU 从 71%→54% 急剧退化，提出 Amodal Mask 监督在重叠 IoU 上提升 15.9%。

**[PandaPose: 3D Human Pose Lifting from a Single Image via Propagating 2D Pose Prior to 3D Anchor Space](object_detection/pandapose_3d_human_pose_lifting_from_a_single_image_via_propagating_2d_pose_prio.md)**

:   提出 PandaPose，通过将 2D 姿态先验传播到 3D 锚点空间作为统一中间表示，结合自适应关节级 3D 锚点设置和关节级深度分布估计，实现对遮挡和 2D 姿态误差鲁棒的单帧 3D 人体姿态提升。

**[Preference Learning with Lie Detectors can Induce Honesty or Evasion](object_detection/preference_learning_with_lie_detectors_can_induce_honesty_or_evasion.md)**

:   系统研究了将谎言检测器（lie detector）整合到LLM偏好学习标注流程中的效果（SOLiD框架），发现训练后模型是变得诚实还是学会规避检测取决于三个关键因素：探索程度（GRPO vs DPO）、检测器准确率（TPR）和KL正则化强度。

**[Rectified-CFG++ for Flow Based Models](object_detection/rectified-cfg_for_flow_based_models.md)**

:   针对Rectified Flow模型中标准CFG导致的离流形漂移问题，提出Rectified-CFG++——一种自适应预测-校正引导策略，通过条件流预测+时间调度插值校正替代外推式引导，在Flux/SD3/SD3.5/Lumina等大规模模型上全面超越标准CFG。

**[SAFE: Multitask Failure Detection for Vision-Language-Action Models](object_detection/safe_multitask_failure_detection_for_vision-language-action_models.md)**

:   SAFE 发现 VLA 模型的内部特征空间存在跨任务一致的"失败区域"，据此训练轻量 MLP/LSTM 失败检测器，配合功能保形预测（FCP）做阈值校准，在未见任务上达 78% ROC-AUC，计算开销 <1%，大幅优于 token 不确定性和一致性检测方法。

**[Sample Complexity of Distributionally Robust Average-Reward Reinforcement Learning](object_detection/sample_complexity_of_distributionally_robust_average-reward_reinforcement_learni.md)**

:   首次为分布鲁棒平均奖励强化学习（DR-AMDP）建立了有限样本收敛保证，提出两种算法（折扣归约法和锚定法），在KL和$f_k$-散度不确定集下均达到$\widetilde{O}(|S||A|t_{\mathrm{mix}}^2\varepsilon^{-2})$的近最优样本复杂度。

**[Test-Time Adaptive Object Detection with Foundation Model](object_detection/test-time_adaptive_object_detection_with_foundation_model.md)**

:   提出无需源域数据的开放词汇测试时自适应目标检测框架（TTAOD），通过多模态 Prompt Tuning + Mean-Teacher + 实例动态记忆（IDM）+ 记忆增强/幻觉策略，在 Pascal-C 上 AP50 达 56.2%（+11.0 vs SOTA），在 13 个跨域数据集上一致有效。

**[The Complexity of Finding Local Optima in Contrastive Learning](object_detection/the_complexity_of_finding_local_optima_in_contrastive_learning.md)**

:   证明对比学习中寻找局部最优是计算困难的：离散三元组最大化问题是 PLS-hard（即使 $d=1$），连续三元组损失最小化是 CLS-hard，意味着（在标准假设下）不存在多项式时间算法找到局部最优。

**[XIFBench: Evaluating Large Language Models on Multilingual Instruction Following](object_detection/xifbench_evaluating_large_language_models_on_multilingual_instruction_following.md)**

:   提出XIFBench——首个系统评估LLM多语言指令遵循能力的约束驱动基准，包含558条指令（0-5个约束，5大类21维度）×6种语言（高/中/低资源），并引入英语需求锚定评估协议，实现94.7%的跨语言评估一致性。

---

## ✂️ 语义分割 { #segmentation }

**[Alligat0R: Pre-Training through Covisibility Segmentation for Relative Camera Pose Regression](segmentation/alligat0r_pre-training_through_co-visibility_segmentation_for_relative_camera_po.md)**

:   用共视性分割（covisibility segmentation）替代 CroCo 的跨视图补全作为双目视觉预训练任务，对每个像素预测"共视/遮挡/视野外"三类标签，在低重叠场景下显著超越 CroCo，RUBIK 基准总体成功率 60.3% 排第一。

**[ARGenSeg: Image Segmentation with Autoregressive Image Generation Model](segmentation/argenseg_image_segmentation_with_autoregressive_image_generation_model.md)**

:   提出ARGenSeg——首个利用自回归图像生成范式实现图像分割的统一MLLM框架，让模型直接输出visual tokens并通过VQ-VAE解码为分割mask，无需额外分割头，搭配next-scale prediction并行生成策略实现4×加速，在RefCOCO/+/g上以更少训练数据超越SOTA。

**[Attention (as Discrete-Time Markov) Chains](segmentation/attention_as_discrete-time_markov_chains.md)**

:   将 softmax 归一化后的注意力矩阵重新解读为离散时间 Markov 链（DTMC）的转移概率矩阵，提出多跳注意力（Multi-Bounce）和 TokenRank（稳态分布，类似 PageRank）来捕获间接注意力路径和全局 token 重要性，在 ImageNet 分割上达 94.29% mAP，并增强 Self-Attention Guidance 的图像生成质量。

**[ConnectomeBench: Can LLMs Proofread the Connectome?](segmentation/connectomebench_can_llms_proofread_the_connectome.md)**

:   提出 ConnectomeBench，首个评估多模态 LLM 在连接组校对（片段识别、分裂错误修正、合并错误检测）三项关键任务上能力的标准化基准；o4-mini 在分裂修正多选任务达 85%，但合并错误检测仍显著落后于人类专家。

**[COS3D: Collaborative Open-Vocabulary 3D Segmentation](segmentation/cos3d_collaborative_open-vocabulary_3d_segmentation.md)**

:   提出COS3D协作式开放词汇3D分割框架，在3D Gaussian Splatting中同时维护instance field（学习清晰边界）和language field（学习语义），通过两阶段训练实现Ins2Lang映射，推理时Language→Instance prompt精化实现互补协作，在LeRF数据集上mIoU达50.76%，大幅超越Dr.Splat（43.58%）。

**[Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning](segmentation/fast_and_fluent_diffusion_language_models_via_convolutional_decoding_and_rejecti.md)**

:   通过卷积解码归一化（替代硬半自回归分块）和基于规则的拒绝微调 R2FT，在 128 步推理下实现与 512+ 步相当的扩散语言模型生成质量，达到 DLM 领域 SOTA。

**[Fast Foreground-Aware Diffusion With Accelerated Sampling Trajectory For Segment](segmentation/fast_foreground-aware_diffusion_with_accelerated_sampling_trajectory_for_segment.md)**

:   提出 FAST，一个面向分割的工业异常合成框架，通过前景感知重建模块（FARM）和异常感知加速采样（AIAS）在仅 10 步去噪下生成高质量合成异常，在 MVTec-AD 上 mIoU 达 76.72%，超越所有先前方法。

**[FineRS: Fine-grained Reasoning and Segmentation of Small Objects with Reinforcement Learning](segmentation/finers_fine-grained_reasoning_and_segmentation_of_small_objects_with_reinforceme.md)**

:   提出 FineRS 两阶段 MLLM 强化学习框架（全局语义探索 GSE → 局部感知精化 LPR），通过 locate-informed retrospective reward 耦合两阶段，在自建 FineRS-4k UAV 高分辨率数据集上实现超小目标的推理与分割，gIoU 达 55.1%（超 Seg-Zero† 8.5%），同时支持 VQA（MVQA 83.3%）。

**[GTPBD: A Fine-Grained Global Terraced Parcel and Boundary Dataset](segmentation/gtpbd_a_fine-grained_global_terraced_parcel_and_boundary_dataset.md)**

:   构建首个全球性细粒度梯田地块与边界数据集GTPBD，包含47,537张高分辨率影像（0.5-0.7m）和超20万个人工标注地块，提供三级标签支持语义分割、边缘检测、地块提取和无监督域适应四项任务，并在20种方法上进行全面基准评测。

**[HAODiff: Human-Aware One-Step Diffusion via Dual-Prompt Guidance](segmentation/haodiff_human-aware_one-step_diffusion_via_dual-prompt_guidance.md)**

:   提出HAODiff，一种人体感知的单步扩散模型，通过三分支双提示引导（DPG）生成自适应正负提示对，结合显式人体运动模糊（HMB）退化管线和分类器自由引导（CFG），在人体图像复原任务上大幅超越现有SOTA方法。

**[HopaDIFF: Holistic-Partial Aware Fourier Conditioned Diffusion for Referring Human Action Segmentation in Multi-Person Scenarios](segmentation/hopadiff_holistic-partial_aware_fourier_conditioned_diffusion_for_referring_huma.md)**

:   首次提出指称人体动作分割(RHAS)任务——通过文本描述定位多人视频中特定个体并做帧级动作分割。构建了包含133部电影、137个动作类别、33小时视频的RHAS133数据集，并提出基于全局-局部感知傅里叶条件扩散的HopaDIFF框架，在多种评估设置下显著超越现有基线。

**[HumanCrafter: Synergizing Generalizable Human Reconstruction and Semantic 3D Segmentation](segmentation/humancrafter_synergizing_generalizable_human_reconstruction_and_semantic_3d_segm.md)**

:   提出HumanCrafter——首个统一单图3D人体重建与人体部位语义分割的前馈框架，通过人体几何先验引导的Transformer聚合多视角特征，结合DINOv2自监督语义先验构建3D特征场，在2K2K和THuman2.1上同时超越现有3D重建和分割SOTA。

**[InstructSAM: A Training-Free Framework for Instruction-Oriented Remote Sensing Object Recognition](segmentation/instructsam_a_training-free_framework_for_instruction-oriented_remote_sensing_ob.md)**

:   定义指令导向目标计数/检测/分割(InstructCDS)新任务，构建EarthInstruct遥感基准（覆盖开放词汇/开放端/开放子类三种设置），提出InstructSAM——无需训练的框架：LVLM解析指令+计数、SAM2生成掩码提议、CLIP计算相似度，通过二进制整数规划(BIP)在计数约束下实现掩码-标签最优匹配，推理时间近乎恒定且优于专用基线。

**[Interpreting ResNet-based CLIP via Neuron-Attention Decomposition](segmentation/interpreting_resnet-based_clip_via_neuron-attention_decomposition.md)**

:   提出神经元-注意力分解方法解释CLIP-ResNet：将模型输出分解为神经元与注意力池化头的成对贡献路径，发现这些neuron-head对可用单一方向近似、具有稀疏性且捕获子概念，并将其应用于免训练语义分割（PASCAL Context上mIoU 26.2%，超MaskCLIP 15%）和数据集分布偏移监测。

**[LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation](segmentation/langhops_language_grounded_hierarchical_open-vocabulary_part_segmentation.md)**

:   提出LangHOPS，首个基于多模态大语言模型（MLLM）的开放词汇物体-部件实例分割框架，在语言空间中建立object-part层次关系，利用MLLM的知识和推理能力链接多粒度概念，在PartImageNet上以56.9% AP超越SOTA 5.5%，跨数据集设置超4.8%。

**[Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks](segmentation/mars-bench_a_benchmark_for_evaluating_foundation_models_for_mars_science_tasks.md)**

:   本文提出 Mars-Bench——首个面向火星科学任务的综合基准，涵盖20个数据集（分类/分割/目标检测三大任务类型），系统评估了 ImageNet 预训练模型、地球观测基础模型和视觉语言模型在火星数据上的表现，发现当前通用模型在火星领域仍有明显不足，呼吁开发火星专用基础模型。

**[Mechanistic Interpretability of RNNs Emulating Hidden Markov Models](segmentation/mechanistic_interpretability_of_rnns_emulating_hidden_mar.md)**

:   训练 vanilla RNN 复现 HMM 的发射统计，然后通过反向工程揭示 RNN 实现离散随机状态转换的机制：噪声驱动的轨道动力学 + "kick 神经元"触发的快速转换，本质是自诱导随机共振（SISR），该动力学基元可组合复用以模拟更复杂的离散潜在结构。

**[Mechanistic Interpretability of RNNs Emulating Hidden Markov Models](segmentation/mechanistic_interpretability_of_rnns_emulating_hidden_markov_models.md)**

:   训练vanilla RNN复现隐马尔可夫模型（HMM）的发射统计量，然后通过逆向工程揭示RNN利用噪声维持的轨道动力学、"kick neuron"电路和自致随机共振机制来实现离散随机状态转换的计算原理。

**[MultiHuman-Testbench: Benchmarking Image Generation for Multiple Humans](segmentation/multihuman-testbench_benchmarking_image_generation_for_multiple_humans.md)**

:   提出 MultiHuman-Testbench，首个系统性评估多人图像生成的基准，包含 1800 个测试样本配对 5550 张人脸图像，以及基于匈牙利匹配的身份相似度等多维度评估指标，并提出区域隔离和隐式匹配技术提升现有方法性能。

**[OmniSegmentor: A Flexible Multi-Modal Learning Framework for Semantic Segmentation](segmentation/omnisegmentor_a_flexible_multi-modal_learning_framework_for_semantic_segmentatio.md)**

:   OmniSegmentor 构建了含 5 种视觉模态的大规模 ImageNeXt 数据集（1.2M 样本），提出随机选择补充模态与 RGB 对齐的高效预训练策略，首次实现灵活的多模态预训练-微调流水线，在 6 个多模态语义分割基准上刷新 SOTA。

**[Panoptic Captioning An Equivalence Bridge For Image And Text](segmentation/panoptic_captioning_an_equivalence_bridge_for_image_and_text.md)**

:   提出 Panoptic Captioning 新任务，追求图像的"最小文本等价"——生成包含所有实体、位置、属性、关系和全局状态的全面描述，13B 模型配合解耦学习即超越 78B 开源和 GPT-4o 等商业模型。

**[PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding](segmentation/partonomy_large_multimodal_models_with_part-level_visual_understanding.md)**

:   提出 Partonomy 部件级分割 benchmark（862 部件标签/534 物体标签）和 Plum 模型（用 span 标记替代 [SEG] token + mask 反馈循环），发现 SOTA 分割 LMM 在部件理解上仅 5.9% gIoU，Plum 通过避免分布偏移和利用历史预测显著提升。

**[HCLFuse: Revisiting Generative Infrared and Visible Image Fusion Based on Human Cognitive Laws](segmentation/revisiting_generative_infrared_and_visible_image_fusion_based_on_human_cognitive.md)**

:   HCLFuse 基于信息瓶颈原理和最优传输理论进行模态对齐，设计变分瓶颈编码器（VBE）+ 物理引导条件扩散模型，融合热传导/结构保持/物理一致性三种约束到扩散过程中，在 MSRS 数据集上梯度指标 AG 提升 69.87%，空间频率 SF 提升 39.41%。

**[Robust Ego-Exo Correspondence with Long-Term Memory](segmentation/robust_ego-exo_correspondence_with_long-term_memory.md)**

:   提出LM-EEC，基于SAM 2的自中心-外中心(ego-exo)视频跨视角目标分割框架，通过Memory-View MoE自适应融合记忆特征与跨视角特征，配合双记忆库压缩策略保持长期信息，在EgoExo4D基准上大幅超越现有方法（Ego2Exo IoU 54.98 vs 38.26）。

**[Robust Egocentric Referring Video Object Segmentation Via Dual-Modal Causal Inte](segmentation/robust_egocentric_referring_video_object_segmentation_via_dual-modal_causal_inte.md)**

:   提出CERES框架，通过双模态因果干预解决自中心指代视频分割(Ego-RVOS)中的鲁棒性问题：对语言偏见用后门调整（消除目标-动作频率偏差），对视觉混淆用前门调整（以深度信息引导视觉中介变量聚合），在VISOR/VOST/VSCOS上达到SOTA。

**[Towards Robust Pseudo-Label Learning In Semantic Segmentation An Encoding Perspe](segmentation/towards_robust_pseudo-label_learning_in_semantic_segmentation_an_encoding_perspe.md)**

:   提出 ECOCSeg，用纠错输出码（ECOC）替代 one-hot 编码来表示伪标签，将 N 类分类分解为 K 个二分类子任务，通过 bit 级去噪和可靠位挖掘生成更鲁棒的伪标签，在 UDA 和 SSL 分割任务上一致提升。

---

## 🔄 自监督/表示学习 { #self_supervised }

**[A Unified Reasoning Framework for Holistic Zero-Shot Video Anomaly Analysis](self_supervised/a_unified_reasoning_framework_for_holistic_zeroshot_video_an.md)**

:   提出一个完全零样本、无需训练的视频异常分析框架，通过Intra-Task Reasoning（置信度门控的自我精化）和Inter-Task Chaining（从时序检测到空间定位到语义理解的级联prompt传递），在4个benchmark上全面超越先前零样本方法4-6% AUC。

**[Adv-SSL: Adversarial Self-Supervised Representation Learning with Theoretical Guarantees](self_supervised/adv-ssl_adversarial_self-supervised_representation_learning_with_theoretical_gua.md)**

:   提出 Adv-SSL，通过将协方差正则项的 Frobenius 范数重写为 minimax 对偶形式，消除了 Barlow Twins 等方法中样本级风险的有偏估计问题，在不增加额外计算成本的前提下显著提升下游分类性能，并给出端到端的理论收敛保证。

**[BrainOmni: A Brain Foundation Model for Unified EEG and MEG Signals](self_supervised/brainomni_a_brain_foundation_model_for_unified_eeg_and_meg_signals.md)**

:   提出 BrainOmni——首个统一 EEG 和 MEG 的脑信号基础模型，通过 BrainTokenizer（含物理传感器编码器）将异构脑电/脑磁信号离散化为统一 token，再用 Criss-Cross Transformer 进行自监督掩码预测预训练，在阿尔茨海默病检测上提升 11.7 个百分点，并实现对完全未见设备的零样本重建泛化。

**[Chain-of-Retrieval Augmented Generation (CoRAG)](self_supervised/chain-of-retrieval_augmented_generation.md)**

:   提出 CoRAG 框架，通过拒绝采样自动生成中间检索链（子查询→子答案），微调 LLM 学习迭代检索和推理，并支持多种测试时解码策略（贪心 / Best-of-N / 树搜索）灵活扩展计算量，在多跳 QA 上 EM 提升 26+ 点，KILT 基准 9/10 任务达到 SOTA。

**[Connecting Jensen-Shannon and Kullback-Leibler Divergences: A New Bound for Representation Learning](self_supervised/connecting_jensenshannon_and_kullbackleibler_divergences_a_n.md)**

:   推导了一般情况下 KL 散度关于 JS 散度的新的紧致可计算下界，证明最大化 JSD 目标等价于最大化互信息的一个下界，为判别式学习在 MI 基础表示学习中的使用提供了理论基础，并在 MI 估计和 Information Bottleneck 中验证了其紧致性和实用性。

**[Continuous Subspace Optimization for Continual Learning (CoSO)](self_supervised/continuous_subspace_optimization_for_continual_learning.md)**

:   提出 CoSO 框架，通过从每步梯度的 SVD 动态导出连续子空间（而非 LoRA 的固定子空间），结合历史任务正交投影防止干扰和 Frequent Directions 高效聚合梯度信息，在 ImageNet-R 20 任务上以 78.19% 最终准确率超越最佳 baseline 2.77 个百分点。

**[Contrastive Representations for Temporal Reasoning](self_supervised/contrastive_representations_for_temporal_reasoning.md)**

:   论文研究能否用纯表示学习替代显式搜索来承担部分时序推理，指出标准 temporal contrastive learning 容易抓住伪特征而失去时序结构，进一步提出 CRTR（Combinatorial Representations for Temporal Reasoning），通过特制负采样从理论上去除伪特征，学到同时编码感知与时序结构的表示，在 Sokoban 和 Rubik's Cube 上取得强结果，甚至可在不依赖外部搜索算法的情况下求解任意初始魔方状态。

**[DataRater: Meta-Learned Dataset Curation](self_supervised/datarater_meta-learned_dataset_curation.md)**

:   提出 DataRater，一个基于元梯度（meta-gradient）的数据价值评估框架，通过元学习自动为每个训练数据点打分并过滤低质量数据，在多个预训练数据集上实现最高 46.6% 的净计算量节省，且在 400M 内部模型上训练的 DataRater 可直接泛化到 50M–1B 规模的 LLM 训练中。

**[Deep Modularity Networks with Diversity-Preserving Regularization](self_supervised/deep_modularity_networks_with_diversity-preserving_regularization.md)**

:   在 Deep Modularity Networks (DMoN) 基础上引入三项多样性保持正则化（距离、方差、熵），显式促进特征空间中的簇间分离和分配多样性，在特征丰富的图数据集上显著提升聚类质量。

**[FaCT: Faithful Concept Traces for Explaining Neural Network Decisions](self_supervised/fact_faithful_concept_traces_for_explaining_neural_network_decisions.md)**

:   提出 FaCT，一种结合 B-cos 变换和稀疏自编码器 (SAE) 的内在可解释模型，能够**忠实地**将模型预测分解为概念贡献（Logit = $\sum$ 概念贡献），并将每个概念忠实地可视化到输入像素级别（概念激活 = $\sum$ 像素贡献），同时提出基于 DINOv2 的 C²-score 用于评估概念一致性。

**[Foundation Cures Personalization Improving Personalized Models Prompt Consistenc](self_supervised/foundation_cures_personalization_improving_personalized_models_prompt_consistenc.md)**

:   提出 FreeCure，一个 training-free 框架，通过发掘个性化模型中隐藏的 foundation model 知识来修复 prompt consistency 退化问题，同时保持 identity fidelity。

**[Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition](self_supervised/foundation_models_for_scientific_discovery_from_paradigm_enhancement_to_paradigm.md)**

:   提出三阶段框架（元科学整合→混合人机共创→自主科学发现）来描绘基础模型正推动科学范式从工具增强向范式转型演变的图景，并系统综述了 FM 在实验/理论/计算/数据四大科学范式中的整合应用。

**[Hybrid Autoencoders for Tabular Data: Leveraging Model-Based Augmentation in Low-Label Settings](self_supervised/hybrid_autoencoders_for_tabular_data_leveraging_model-based_augmentation_in_low-.md)**

:   提出 TANDEM（Tree-And-Neural Dual Encoder Model），一种混合自编码器架构，通过联合训练神经网络编码器和遗忘软决策树（OSDT）编码器，并引入样本级随机门控网络作为可学习的数据增强，在低标签表格数据场景下实现了超越强基线（包括树模型和深度学习方法）的性能。

**[Implicit Modeling for Transferability Estimation of Vision Foundation Models](self_supervised/implicit_modeling_for_transferability_estimation_of_vision_foundation_models.md)**

:   提出隐式可迁移性建模（ITM）框架，通过隐变量z隐式编码模型-任务对的迁移能力，结合分治变分近似（DVA）高效模拟嵌入空间演化，在10个下游任务和10个多样化预训练模型上的加权Kendall tau_w从此前最优的0.45提升至0.61。

**[Know Thyself by Knowing Others: Learning Neuron Identity from Population Context](self_supervised/know_thyself_by_knowing_others_learning_neuron_identity_from_population_context.md)**

:   提出NuCLR自监督框架，通过对比学习对群体神经活动中同一神经元的不同时间窗口拉近、不同神经元推远，学习包含群体上下文的神经元级表征，在细胞类型和脑区解码上达到新SOTA，并首次展示了跨动物零样本泛化和数据缩放规律。

**[Long-Tailed Recognition via Information-Preservable Two-Stage Learning](self_supervised/long-tailed_recognition_via_information-preservable_two-stage_learning.md)**

:   提出信息保持的两阶段学习框架：第一阶段用 Balanced Negative Sampling (BNS) 基于互信息最大化学习有效且可分的特征空间，第二阶段用 Information-Preservable DPP (IP-DPP) 采样数学上信息量最大的样本来纠正多数类偏向的决策边界，在多个长尾数据集上取得 SOTA。

**[Manifolds and Modules: How Function Develops in a Neural Foundation Model](self_supervised/manifolds_and_modules_how_function_develops_in_a_neural_foundation_model.md)**

:   从计算神经科学视角"打开黑箱"分析 SOTA 神经活动基础模型 (FNN)，通过构建解码流形和编码流形发现其各处理模块（编码器、循环、读出）展现出质性不同的表征结构，且与生物视觉系统存在关键差异。

**[Minimal Semantic Sufficiency Meets Unsupervised Domain Generalization](self_supervised/minimal_semantic_sufficiency_meets_unsupervised_domain_generalization.md)**

:   MS-UDG 在无类别标签和域标签的条件下，通过信息解纠缠模块（IDM）将表征分解为语义和变异成分，配合最小语义充分性优化模块（SROM）最大化语义信息同时最小化变异干扰，在 PACS 上达 72.89% 准确率（+1.5% vs CycleMAE），理论证明最小充分语义表征最小化下游贝叶斯错误率。

**[Sciarena An Open Evaluation Platform For Non-Verifiable Scientific Literature-Gr](self_supervised/sciarena_an_open_evaluation_platform_for_non-verifiable_scientific_literature-gr.md)**

:   构建SciArena——社区驱动的科学文献基础模型开放评估平台，支持47个模型和20K+偏好投票，同时发布SciArena-Eval元基准评估自动评估系统判断能力。

**[Self-Supervised Contrastive Learning is Approximately Supervised Contrastive Learning](self_supervised/self-supervised_contrastive_learning_is_approximately_supervised_contrastive_lea.md)**

:   从理论上证明自监督对比学习（DCL）近似等价于一种有监督对比损失（NSCL），两者差距以 $O(1/C)$ 速度随类别数增加而消失；进一步证明 NSCL 全局最优解满足 Neural Collapse（增强坍缩 + 类内坍缩 + Simplex ETF），并提出基于方向性 CDNV 的更紧的 few-shot 误差界。

**[STaRFormer: Semi-Supervised Task-Informed Representation Learning via Dynamic Attention-Based Regional Masking](self_supervised/starformer_semi-supervised_task-informed_representation_learning_via_dynamic_att.md)**

:   提出 STaRFormer，通过动态注意力区域掩码（DAReM）识别任务关键区域并施加掩码扰动，配合批内+类内半监督对比学习将任务信息嵌入潜在表示，在 56 个数据集（含非平稳、不规则采样、分类/异常检测/回归）上全面超越 SOTA。

**[T-REGS: Minimum Spanning Tree Regularization for Self-Supervised Learning](self_supervised/t-regs_minimum_spanning_tree_regularization_for_self-supervised_learning.md)**

:   提出 T-REGS——一种基于最小生成树(MST)长度最大化的自监督学习正则化框架，理论证明可同时防止维度坍缩并促进表示分布均匀性，在紧致黎曼流形上成立，实验在标准 JE-SSL 基准上验证了有效性。

**[TabArena: A Living Benchmark for Machine Learning on Tabular Data](self_supervised/tabarena_a_living_benchmark_for_machine_learning_on_tabular_data.md)**

:   提出 TabArena，首个持续维护的"活跃"表格数据基准系统，从 1053 个数据集中精选 51 个、纳入 16 个模型，通过大规模实验（约 2500 万次模型训练）发现：后验集成下深度学习模型已追平甚至超越 GBDT，表格基础模型在小数据上表现突出，跨模型集成可进一步推进 SOTA。

**[Tabstar A Tabular Foundation Model For Tabular Data With Text Fields](self_supervised/tabstar_a_tabular_foundation_model_for_tabular_data_with_text_fields.md)**

:   提出 TabSTAR，一个专为含文本字段的表格数据设计的基础模型：通过解冻文本编码器（e5-small-v2）端到端优化文本表征 + 目标感知 token 注入分类目标语义信息 + 无数据集特定参数的架构实现跨数据集迁移学习，在 350 个数据集上预训练后，分类任务上 14 个数据集中 12 个超越 CatBoost-Tuned（4h 调参），8/11 超越 TabPFN-v2。

---

## 🔗 因果推理 { #causal_inference }

**[A Principle of Targeted Intervention for Multi-Agent Reinforcement Learning](causal_inference/a_principle_of_targeted_intervention_for_multi-agent_reinforcement_learning.md)**

:   提出基于多智能体影响图（MAIDs）的**目标干预范式（Targeted Intervention）**，通过仅对单个目标智能体施加**预策略干预（Pre-Strategy Intervention, PSI）**，引导整个多智能体系统收敛到满足额外期望结果的优选Nash均衡，无需对所有智能体进行全局干预。

**[An Analysis of Causal Effect Estimation Using Outcome Invariant Data Augmentation](causal_inference/an_analysis_of_causal_effect_estimation_using_outcome_invariant_data_augmentatio.md)**

:   分析"结果不变数据增强"在因果效应估计中的作用——当增强操作不改变结果变量的条件分布时，可以在不引入偏差的条件下有效减少选择偏差，且在特定条件下可证明提升估计精度。

**[Bi-Level Decision-Focused Causal Learning for Large-Scale Marketing Optimization](causal_inference/bi-level_decision-focused_causal_learning_for_large-scale_marketing_optimization.md)**

:   提出 Bi-DFCL，通过双层优化框架联合利用观测数据和 RCT 实验数据来训练营销资源分配模型：上层用 RCT 数据的无偏决策损失端到端训练 Bridge Network 来动态纠正下层在观测数据上的偏差，同时设计了基于原始问题的可微代理决策损失（PPL/PIFD）和隐式微分算法，解决了传统两阶段方法的预测-决策不一致和偏差-方差困境。已在美团大规模在线部署。

**[Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features](causal_inference/causality-induced_positional_encoding_for_transformer-based_representation_learn.md)**

:   CAPE 通过从表格数据中学习特征间的因果DAG结构，将其嵌入双曲空间生成因果感知的旋转位置编码（RoPE），使 Transformer 能处理非序列但因果相关的特征数据，在多组学数据的下游任务上显著提升性能。

**[Characterization and Learning of Causal Graphs from Hard Interventions](causal_inference/characterization_and_learning_of_causal_graphs_from_hard_interventions.md)**

:   首次系统分析硬干预（hard interventions）在含隐变量因果发现中的理论优势，提出广义do-演算（4条规则）和孪生增强MAG图表示，给出 $\mathcal{I}$-Markov 等价类的充要图条件，并设计可证明正确的FCI变体学习算法；实验表明硬干预比软干预将等价类缩小37-57%。

**[Conformal Prediction for Causal Effects of Continuous Treatments](causal_inference/conformal_prediction_for_causal_effects_of_continuous_treatments.md)**

:   首次为连续处理变量（如药物剂量）的因果效应构建共形预测区间，通过倾向性偏移参数化和分位数回归，在已知/未知倾向性两种场景下均提供有限样本 $1-\alpha$ 覆盖保证。

**[Counterfactual Reasoning For Steerable Pluralistic Value Alignment Of Large Lang](causal_inference/counterfactual_reasoning_for_steerable_pluralistic_value_alignment_of_large_lang.md)**

:   提出COUPLE框架，通过构建结构因果模型（SCM）建模多维价值观的依赖关系与优先级，并利用反事实推理实现LLM对任意细粒度多元价值目标的可控对齐。

**[Cyclic Counterfactuals under Shift–Scale Interventions](causal_inference/cyclic_counterfactuals_under_shift-scale_interventions.md)**

:   为含有反馈循环的循环结构因果模型(cyclic SCM)建立了移位-缩放(shift-scale)干预下的反事实推断理论框架，证明了全局收缩条件下唯一可解性、干预复合封闭性，以及反事实泛函的sub-Gaussian集中不等式。

**[Demystifying Spectral Feature Learning For Instrumental Variable Regression](causal_inference/demystifying_spectral_feature_learning_for_instrumental_variable_regression.md)**

:   推导了谱特征学习在工具变量(IV)回归中的泛化界，根据谱对齐和特征值衰减率将性能分为"好/坏/丑"三类，并提出数据驱动的诊断方法。

**[Differentiable Structure Learning And Causal Discovery For General Binary Data](causal_inference/differentiable_structure_learning_and_causal_discovery_for_general_binary_data.md)**

:   提出基于多元伯努利分布（MVB）的通用可微结构学习框架，不假设特定数据生成过程，能捕获二值离散变量间的任意高阶依赖关系，并证明在一般设定下DAG不可识别但可恢复最小等价类（Markov等价类）。

**[Do-Pfn In-Context Learning For Causal Effect Estimation](causal_inference/do-pfn_in-context_learning_for_causal_effect_estimation.md)**

:   提出 Do-PFN，将 Prior-data Fitted Networks (PFN) 扩展到因果效应估计，在大量合成 SCM 数据上预训练 Transformer 进行 in-context 因果推理，仅需观测数据即可预测干预分布（CID）和 CATE，无需因果图知识或不混杂假设，在合成和半合成实验中表现出色。

**[Domain-Adapted Granger Causality For Real-Time Cross-Slice Attack Attribution In](causal_inference/domain-adapted_granger_causality_for_real-time_cross-slice_attack_attribution_in.md)**

:   提出一种面向6G网络切片的域适应Granger因果框架，将增强型Granger因果检验与网络资源争用建模相结合，实现实时跨切片攻击归因，在1100个攻击场景上达到89.2%准确率和87ms响应时间，显著超越现有统计、深度学习和因果发现方法。

**[Dynamic Causal Discovery In Alzheimers Disease Through Latent Pseudotime Modelli](causal_inference/dynamic_causal_discovery_in_alzheimers_disease_through_latent_pseudotime_modelli.md)**

:   将 BN-LTE（贝叶斯网络+潜在时间嵌入）应用于 ADNI 真实 AD 数据，推断随疾病伪时间演变的动态因果图，伪时间预测诊断 AUC 0.82 远超年龄 0.59，并揭示了新型生物标志物 NfL/GFAP 与传统 AD 标志物之间的动态因果关系。

**[Few-Shot Knowledge Distillation of LLMs With Counterfactual Explanations](causal_inference/few-shot_knowledge_distillation_of_llms_with_counterfactual_explanations.md)**

:   提出 CoD（Counterfactual-explanation-infused Distillation），通过将反事实解释注入少样本训练集来精确映射 teacher 决策边界，在 6 个数据集上仅用 8–512 样本即显著超越标准蒸馏方法。

**[From Black-box to Causal-box: Towards Building More Interpretable Models](causal_inference/from_black-box_to_causal-box_towards_building_more_interpretable_models.md)**

:   提出"因果可解释性"（causal interpretability）的形式化定义，证明黑盒模型和概念瓶颈模型均不满足该性质，给出完整的图判据确定哪些模型架构能一致地回答反事实问题，揭示了因果可解释性与预测精度之间的根本性权衡。

**[GST-UNet: A Neural Framework for Spatiotemporal Causal Inference with Time-Varying Confounding](causal_inference/gst-unet_a_neural_framework_for_spatiotemporal_causal_inference_with_time-varyin.md)**

:   提出 GST-UNet，将 U-Net 时空编码器与迭代 G-computation 相结合，从**单条时空观测轨迹**中估计位置特异性的条件平均潜在结果 (CAPO)，可同时处理干扰（interference）、空间混杂、时间延续和时变混杂，并在加州山火烟雾对呼吸系统住院率的因果分析中验证了实用价值。

**[It's Hard to Be Normal: The Impact of Noise on Structure-agnostic Estimation](causal_inference/its_hard_to_be_normal_the_impact_of_noise_on_structure-agnostic_estimation.md)**

:   证明 Double Machine Learning (DML) 在高斯处理噪声下是极小极大最优的（$O(\epsilon^2 + n^{-1/2})$），但在非高斯噪声下变得次优；提出 Agnostic Cumulant-based Estimation (ACE) 利用高阶累积量达到 $r$ 阶不敏感性 $O(\epsilon^r + n^{-1/2})$。

**[LLM Interpretability with Identifiable Temporal-Instantaneous Representation](causal_inference/llm_interpretability_with_identifiable_temporal-instantaneous_representation.md)**

:   本文提出了一种面向 LLM 高维激活空间的可辨识时序因果表示学习框架，通过线性化公式同时建模时间延迟和瞬时因果关系，在保留理论可辨识性保证的同时解决了现有 CRL 方法无法扩展到 LLM 维度的计算瓶颈。

**[Performative Validity of Recourse Explanations](causal_inference/performative_validity_of_recourse_explanations.md)**

:   本文形式化分析了追索权解释（recourse explanations）的"表演性"效应——当大量被拒申请者按照追索建议行动时，集体行为会引发数据分布偏移并使模型更新后追索失效，并证明了只有基于因果变量的改进型追索（ICR）才能在广泛条件下保持"表演性有效性"。

**[Practical do-Shapley Explanations with Estimand-Agnostic Causal Inference](causal_inference/practical_do-shapley_explanations_with_estimand-agnostic_causal_inference.md)**

:   提出 Estimand-Agnostic（EA）方法和 Frontier-Reducibility Algorithm（FRA）来高效计算因果 Shapley 值（do-SV），通过训练单个 SCM 学习观测分布即可回答任意可辨识的因果查询，并通过联盟约减将计算量降低约 90%。

**[Revealing Multimodal Causality with Large Language Models](causal_inference/revealing_multimodal_causality_with_large_language_models.md)**

:   提出 MLLM-CD，首个面向多模态非结构化数据的因果发现框架，通过对比因子发现识别跨模态因果变量，结合统计因果结构推断，并利用 MLLM 的世界知识生成多模态反事实样本来迭代消除结构歧义，在合成和真实数据集上均显著优于现有方法。

**[Root Cause Analysis of Outliers with Missing Structural Knowledge](causal_inference/root_cause_analysis_of_outliers_with_missing_structural_knowledge.md)**

:   提出仅用**边际异常分数**即可做根因分析的两个简单高效算法——已知因果图时用 SMOOTH TRAVERSAL（沿因果路径找分数跳变最大的节点），未知因果图时用 SCORE ORDERING（按分数排序取 top-k），在 polytree 结构下给出非参数概率保证，仅需单个异常样本即可工作。

**[Transferring Causal Effects Using Proxies](causal_inference/transferring_causal_effects_using_proxies.md)**

:   提出基于代理变量（proxy）的多域因果效应迁移方法，在目标域仅观测到代理变量 W 的条件下，利用多源域数据识别并估计目标域中含未观测混淆因子的干预分布，给出两种一致性估计器及渐近置信区间。

---

## 🖼️ 图像恢复 { #image_restoration }

**[Adaptive Discretization for Consistency Models](image_restoration/adaptive_discretization_for_consistency_models.md)**

:   提出ADCM框架，将一致性模型(CM)的离散化步长选择形式化为约束优化问题，通过Gauss-Newton方法得到解析解，在局部一致性（可训练性）和全局一致性（稳定性）之间自适应平衡，以仅4%的额外计算开销实现显著的训练效率提升和FID改善。

**[Audio Super-Resolution With Latent Bridge Models](image_restoration/audio_super-resolution_with_latent_bridge_models.md)**

:   提出 AudioLBM，在波形隐空间中用桥模型实现 LR-to-HR latent-to-latent 音频超分，配合频率感知训练和级联设计，LSD 平均改善 21.5%，首次实现 any-to-192kHz 音频超分。

**[DenoiseRotator: Enhance Pruning Robustness for LLMs via Importance Concentration](image_restoration/denoiserotator_enhance_pruning_robustness_for_llms_via_importance_concentration.md)**

:   提出 DenoiseRotator，在剪枝前通过可学习正交变换最小化参数重要性分数的信息熵，将重要性集中到少数参数上，使 LLaMA3-70B 在 2:4 半结构化稀疏下困惑度退化缩小 58%（8.1→3.4），可即插即用组合 Magnitude/Wanda/SparseGPT。

**[DynaGuide: Steering Diffusion Policies with Active Dynamic Guidance](image_restoration/dynaguide_steering_diffusion_polices_with_active_dynamic_guidance.md)**

:   提出 DynaGuide，在推理时通过外部潜在动力学模型对预训练扩散策略施加 classifier guidance，无需修改策略权重即可引导机器人朝向任意正/负目标，在 CALVIN 仿真上平均成功率 70%，真实机器人达 80%。

**[Enhancing Infrared Vision: Progressive Prompt Fusion Network and Benchmark](image_restoration/enhancing_infrared_vision_progressive_prompt_fusion_network_and_benchmark.md)**

:   针对热红外(TIR)图像中低对比度、模糊、噪声等多种退化耦合的问题，提出基于双提示融合的渐进式网络PPFN和选择性渐进训练策略SPT，并构建首个大规模多场景TIR基准数据集HM-TIR，在复合退化场景下PSNR提升8.76%。

**[FIPER: Factorized Features for Robust Image Super-Resolution and Compression](image_restoration/fiper_factorized_features_for_robust_image_super-resolution_and_compression.md)**

:   提出 Factorized Features 统一表示——将图像分解为可学习的非均匀基与空间变化系数，配合锯齿坐标变换和多频调制，在 4× 超分辨率上 PSNR 相对提升 204.4%（HAT-L-F vs SwinIR），在图像压缩上 BD-rate 相比 VTM 降低 21.09%。

**[GC4NC: A Benchmark Framework for Graph Condensation on Node Classification with New Insights](image_restoration/gc4nc_a_benchmark_framework_for_graph_condensation_on_node_classification_with_n.md)**

:   提出 GC4NC——首个系统化的图凝缩（Graph Condensation）评估基准框架，跨 8 个维度（性能/效率/隐私保护/去噪/NAS有效性/可迁移性等）统一评估多种图凝缩方法，发现轨迹匹配方法最优、无结构方法效率最高，并在 1000x 压缩下图凝缩显著优于图像凝缩。

**[Implicit Augmentation from Distributional Symmetry in Turbulence Super-Resolution](image_restoration/implicit_augmentation_from_distributional_symmetry_in_turbulence_super-resolutio.md)**

:   本文揭示湍流的统计各向同性本身就是一种隐式数据增强，使得标准CNN在超分辨率任务中无需显式旋转增强或等变架构即可部分习得旋转等变性，并展示了等变误差的尺度依赖性与Kolmogorov局部各向同性假说一致。

**[Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Learnable Linear Extrapolation](image_restoration/improving_diffusion-based_inverse_algorithms_under_few-step_constraint_via_learn.md)**

:   提出 Learnable Linear Extrapolation (LLE)——用可学习的线性组合系数将当前和历史 clean data estimate 组合，以增强任何符合 Sampler-Corrector-Noiser 范式的扩散逆问题算法在少步（3-5步）下的表现，仅需 50 个样本、几分钟训练，跨 9+ 算法 × 5 个任务一致提升。

**[Latent Harmony: Synergistic Unified UHD Image Restoration via Latent Space Regularization and Controllable Refinement](image_restoration/latent_harmony_synergistic_unified_uhd_image_restoration_via_latent_space_regula.md)**

:   提出 Latent Harmony 两阶段框架，通过潜在空间正则化构建泛化性 VAE（LH-VAE），并引入高频引导的可控 LoRA 微调机制，在保持结构完整性的同时实现 UHD 图像多退化类型统一修复的保真度-感知质量灵活权衡。

**[Latent Harmony: Synergistic Unified UHD Image Restoration via Latent Space Regularization and Controllable Refinement](image_restoration/latent_harmony_synergistic_unified_uhd_image_restoration_with_pre-trained_diffus.md)**

:   提出 Latent Harmony 两阶段框架，通过潜在空间正则化构建退化鲁棒的 LH-VAE，再用高频引导的 LoRA 微调分别优化编码器（保真度）和解码器（感知质量），实现 UHD 全能图像复原中泛化-重建-感知三重权衡的统一解决方案。

**[Learning Cocoercive Conservative Denoisers via Helmholtz Decomposition for Poisson Inverse Problems](image_restoration/learning_cocoercive_conservative_denoisers_via_helmholtz_decomposition_for_poiss.md)**

:   提出共循环保守(CoCo)去噪器概念，通过广义Helmholtz分解设计新的训练策略——Hamiltonian正则化促进保守性 + 谱正则化促进共循环性——使去噪器成为隐式弱凸先验的近端算子，从而在Poisson逆问题（光子受限去卷积、低剂量CT等）中实现有收敛保证且性能优越的PnP方法。

**[Luminance-Aware Statistical Quantization: Unsupervised Hierarchical Learning for Illumination Enhancement](image_restoration/luminance-aware_statistical_quantization_unsupervised_hierarchical_learning_for_.md)**

:   提出 LASQ 框架，将低光图像增强重新定义为基于分层亮度分布的统计采样过程，利用自然亮度转换中固有的幂律分布特性，通过 MCMC 采样生成层次化亮度适配算子，嵌入扩散模型前向过程实现无监督增强，无需正常光照参考即可工作。

**[Map Estimation With Denoisers Convergence Rates And Guarantees](image_restoration/map_estimation_with_denoisers_convergence_rates_and_guarantees.md)**

:   证明了一个简单的 MMSE 去噪器迭代平均算法（与 Cold Diffusion 等实践方法密切相关）在对数凹先验假设下可证明收敛到负对数先验的近端算子，收敛速率为 Õ(1/k)，为一类经验上成功但缺乏理论保证的去噪方法提供了严格的理论基础，并将其嵌入近端梯度下降框架解决 MAP 估计问题。

**[Mro Enhancing Reasoning In Diffusion Language Models Via Multi-Reward Optimizati](image_restoration/mro_enhancing_reasoning_in_diffusion_language_models_via_multi-reward_optimizati.md)**

:   MRO通过多奖励优化捕获扩散语言模型内/间序列token相关性，加速DLM推理同时保持性能。

**[Rethinking Circuit Completeness in Language Models: AND, OR, and ADDER Gates](image_restoration/rethinking_circuit_completeness_in_language_models_and_or_and_adder_gates.md)**

:   系统引入AND、OR、ADDER三种逻辑门来分解语言模型电路，揭示电路不完整性主要源于OR门的遗漏，提出结合noising和denoising干预的框架来完整恢复三种逻辑门，同时保证忠实度和完整性。

**[Rethinking Nighttime Image Deraining Via Learnable Color Space Transformation](image_restoration/rethinking_nighttime_image_deraining_via_learnable_color_space_transformation.md)**

:   提出CST-Net用于夜间图像去雨：基于夜间雨在Y通道（亮度）上比RGB更显著的观察，设计可学习颜色空间转换器(CSC)在YCbCr空间去雨，配合隐式光照引导模块(IIG)和新构建的光照感知合成数据集HQ-NightRain，在多个基准上达到SOTA。

**[Scsplit Bringing Severity Cognizance To Image Decomposition In Fluorescence Micr](image_restoration/scsplit_bringing_severity_cognizance_to_image_decomposition_in_fluorescence_micr.md)**

:   提出 scSplit，通过引入混合比例感知的归一化模块（SCIN）和回归网络（Reg），使基于 InDI 的迭代图像分解方法能够感知荧光显微镜图像中两种结构叠加的严重程度，在5个公开数据集上统一解决图像分离和渗透去除两个任务。

**[Spend Wisely: Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping](image_restoration/spend_wisely_maximizing_post-training_gains_in_iterative_synthetic_data_bootstra.md)**

:   首次从理论上分析了迭代合成数据自举训练中的预算分配问题，证明恒定策略无法高概率收敛，而指数增长策略在最坏情况下优于多项式策略，并在图像去噪（DPM）和数学推理（LLM）实验中验证了该结论。

**[Spiking Meets Attention Efficient Remote Sensing Image Super-Resolution With Att](image_restoration/spiking_meets_attention_efficient_remote_sensing_image_super-resolution_with_att.md)**

:   提出 SpikeSR，首个基于注意力脉冲神经网络(SNN)的遥感图像超分辨率框架，通过脉冲注意力块(SAB)结合混合维度注意力(HDA)和可变形相似度注意力(DSA)，在 AID/DOTA/DIOR 上达到 SOTA 性能同时保持高计算效率。

**[The Effect Of Optimal Self-Distillation In Noisy Gaussian Mixture Model](image_restoration/the_effect_of_optimal_self-distillation_in_noisy_gaussian_mixture_model.md)**

:   用统计物理replica方法分析噪声高斯混合模型上的自蒸馏，证明硬伪标签的去噪是性能提升主因，CIFAR-10实验验证。

**[Video Killed the Energy Budget: Characterizing the Latency and Power Regimes of Open T2V Models](image_restoration/video_killed_the_energy_budget_characterizing_the_latency_and_power_regimes_of_o.md)**

:   对开源T2V模型进行系统性延迟与能耗分析：建立了基于FLOP的compute-bound理论模型，验证了WAN2.1-T2V的二次空间/时间缩放和线性去噪步数缩放规律，并横向对比7个T2V模型发现能耗差异达3000倍（AnimateDiff 0.14Wh vs WAN2.1-14B 415Wh）。

---

## 🧮 科学计算 { #scientific_computing }

**[Bayesian Surrogates for Risk-Aware Pre-Assessment of Aging Bridge Portfolios](scientific_computing/bayesian_surrogates_for_risk-aware_pre-assessment_of_aging_bridge_portfolios.md)**

:   提出基于贝叶斯神经网络（BNN）的代理模型，用于替代昂贵的非线性有限元分析（NLFEA），实现对老化桥梁组合的快速、不确定性感知的结构安全预评估，在真实铁路案例中为单座桥梁节省约37万美元。

**[Collapsing Taylor Mode Automatic Differentiation](scientific_computing/collapsing_taylor_mode_automatic_differentiation.md)**

:   提出 Taylor mode 自动微分的"折叠"(collapsing)优化技术，通过重写计算图将导数求和操作向上传播，大幅加速 PDE 算子（如 Laplacian、一般线性 PDE 算子）的计算，实现速度优于嵌套反向传播同时保持前向模式的低内存优势。

**[DeltaPhi: Physical States Residual Learning for Neural Operators in Data-Limited PDE Solving](scientific_computing/deltaphi_physical_states_residual_learning_for_neural_operators_in_data-limited_.md)**

:   提出 DeltaPhi 框架：不直接学习 PDE 的输入→输出映射，而是学习**相似物理状态之间的残差**，利用物理系统稳定性实现隐式数据增强，在数据稀缺场景下显著提升各类神经算子的性能。

**[Eddyformer Accelerated Neural Simulations Of Three-Dimensional Turbulence At Sca](scientific_computing/eddyformer_accelerated_neural_simulations_of_three-dimensional_turbulence_at_sca.md)**

:   提出 EddyFormer，一种基于谱元法 (SEM) 的 Transformer 架构，将流场分解为 LES（大尺度）和 SGS（小尺度）两路并行流，在 256³ 分辨率 3D 湍流上达到 DNS 级精度且加速 30 倍，并在未见的 4× 更大域上泛化良好。

**[Enforcing Governing Equation Constraints in Neural PDE Solvers via Training-free Projections](scientific_computing/enforcing_governing_equation_constraints_in_neural_pde_solvers_via_training-free.md)**

:   提出两种无需训练的后处理投影方法（非线性LBFGS优化和局部线性化投影），将神经PDE求解器的输出投影到满足控制方程约束的可行流形上，在Lorenz/KS/Navier-Stokes上大幅降低约束违反并提升精度，且效果显著优于physics-informed训练。

**[F-Adapter: Frequency-Adaptive Parameter-Efficient Fine-Tuning in Scientific Machine Learning](scientific_computing/f-adapter_frequency-adaptive_parameter-efficient_fine-tuning_in_scientific_machi.md)**

:   本文首次系统研究了科学机器学习中预训练大型算子模型(LOM)的参数高效微调(PEFT)，发现 LoRA 在傅里叶层中存在深度放大的近似误差下界，而 Adapter 保留了通用逼近能力；据此提出频率自适应 Adapter（F-Adapter），按频谱能量分配 Adapter 容量，在 3D Navier-Stokes 预测任务上仅调参不到 2% 即达到 SOTA。

**[From Black Hole to Galaxy: Neural Operator Framework for Accretion and Feedback Dynamics](scientific_computing/from_black_hole_to_galaxy_neural_operator_framework_for_accretion_and_feedback_d.md)**

:   提出基于 Neural Operator 的「子网格黑洞」模型，学习小尺度 (GR)MHD 时间演化算子，替代手工闭合规则嵌入多层级直接数值模拟框架，首次实现吸积驱动反馈的内禀变异性捕获，加速比达 $\sim 10^5$ 倍。

**[From Images To Physics Probabilistic Inference Of Galaxy Parameters And Emission](scientific_computing/from_images_to_physics_probabilistic_inference_of_galaxy_parameters_and_emission.md)**

:   提出 VAE–Normalizing Flow 混合框架，从 SDSS gri 图像和测光数据出发，以概率方式联合推断星系物理参数（恒星质量、SFR、红移、气相金属丰度、中心黑洞质量）和发射线流量（Hα、Hβ、[N II]、[O III]），速度比 SED 拟合快 100 倍以上且提供校准良好的后验分布。

**[GyroSwin: 5D Surrogates for Gyrokinetic Plasma Turbulence Simulations](scientific_computing/gyroswin_5d_surrogates_for_gyrokinetic_plasma_turbulence_simulations.md)**

:   首次提出可扩展的5D神经网络代理模型 GyroSwin，将 Swin Transformer 扩展至5维回旋动力学相空间，通过交叉注意力实现3D↔5D交互、通道式模态分离捕获带状流，在等离子体湍流模拟中实现比传统准线性方法更高的精度，且比数值求解器（GKW）快3个数量级。

**[Hamiltonian Neural PDE Solvers through Functional Approximation](scientific_computing/hamiltonian_neural_pde_solvers_through_functional_approximation.md)**

:   基于 Riesz 表示定理，用可学习核积分（Integral Kernel Functional）近似无限维 Hamiltonian 泛函，通过自动微分获取泛函导数，实现保能量的神经 PDE 求解器（HNS），在 1D/2D PDE 上展现出优越的稳定性和泛化能力。

**[Inc An Indirect Neural Corrector For Auto-Regressive Hybrid Pde Solvers](scientific_computing/inc_an_indirect_neural_corrector_for_auto-regressive_hybrid_pde_solvers.md)**

:   提出间接神经校正器(INC)，将学习到的校正项嵌入PDE的右端项（而非直接修改状态），理论证明误差放大降低$\mathcal{O}(\Delta t^{-1}+L)$倍，在6个PDE系统（1D混沌到3D湍流）上大幅改善长期轨迹性能（R²提升达158.7%），实现最高330×加速。

**[Integration Matters for Learning PDEs with Backward SDEs](scientific_computing/integration_matters_for_learning_pdes_with_backward_sdes.md)**

:   揭示了标准 BSDE 方法性能不如 PINNs 的根本原因是 Euler-Maruyama 积分引入的不可消除离散化偏差，提出基于 Stratonovich 形式的 Heun-BSDE 方法彻底消除该偏差，在高维 PDE 上与 PINNs 竞争。

**[Multi-Trajectory Physics-Informed Neural Networks for HJB Equations with Hard-Zero Terminal Inventory: Optimal Execution on Synthetic & SPY Data](scientific_computing/multi-trajectory_physics-informed_neural_networks_for_hjb_equations_with_hard-ze.md)**

:   针对最优交易执行中 HJB 方程的硬零终端库存约束（$X_T=0$），提出 Multi-Trajectory PINN (MT-PINN)，通过基于轨迹展开的终端损失与 $\lambda$-curriculum 训练策略，在合成数据和 SPY 实盘回测中显著优于 vanilla PINN，终端库存违规率大幅降低。

**[Neural Emulator Superiority: When Machine Learning for PDEs Surpasses its Training Data](scientific_computing/neural_emulator_superiority_when_machine_learning_for_pdes_surpasses_its_trainin.md)**

:   挑战了"神经 PDE 模拟器精度受限于训练数据（数值求解器）精度"的传统认知，发现并严格定义了 **emulator superiority** 现象——仅在低精度求解器数据上训练的神经网络，在以高精度参考解评估时竟能超越其训练求解器本身。

**[Neuro-Spectral Architectures for Causal Physics-Informed Networks](scientific_computing/neuro-spectral_architectures_for_causal_physics-informed_networks.md)**

:   NeuSA 将经典谱方法与 Neural ODE 结合，先将 PDE 投影到谱基（Fourier）上得到 ODE 系统，再用 NODE 学习动力学演化，从架构层面解决了传统 PINN 的谱偏差和因果性问题，在波动方程/Burgers方程/sine-Gordon方程上误差比 baseline 低 1-2 个数量级且训练更快。

**[From Images to Physics: Probabilistic Inference of Galaxy Parameters and Emission Lines via VAE–Normalizing Flows](scientific_computing/one-shot_transfer_learning_for_nonlinear_pdes_with_perturbative_pinns.md)**

:   提出 VAE–Normalizing Flow 两阶段概率推断框架，仅从 SDSS 星系图像和测光数据即可快速推断恒星质量、SFR、红移、黑洞质量、金属丰度及发射线通量，精度超越现有非光谱方法且比 SED 拟合快 100 倍以上。

**[Physics-Guided Machine Learning For Uncertainty Quantification In Turbulence Mod](scientific_computing/physics-guided_machine_learning_for_uncertainty_quantification_in_turbulence_mod.md)**

:   提出混合 ML–EPM 框架：用轻量 CNN 学习从 RANS 湍流动能场到 DNS 真值的修正映射，以此调制特征空间扰动法（EPM）的扰动幅度，在保持物理一致性的前提下将湍流模型不确定性估计的误差降低 1–2 个数量级。

**[Physics-Informed Neural Networks with Fourier Features and Attention-Driven Decoding](scientific_computing/physics-informed_neural_networks_with_fourier_features_and_attention-driven_deco.md)**

:   提出 Spectral PINNsformer (S-Pformer)，用 Fourier 特征嵌入替换 PINNsformer 的编码器，结合仅解码器 Transformer 架构，在减少 18.6% 参数量的同时在多个 PDE benchmark 上取得更优性能，有效缓解了频谱偏置问题。

**[Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon](scientific_computing/stable_minima_of_relu_neural_networks_suffer_from_the_curse_of_dimensionality_th.md)**

:   本文研究了两层过参数化 ReLU 网络中稳定极小值（flat minima）的泛化性质，证明虽然平坦性确实蕴含泛化，但其收敛速率随输入维度指数级恶化（即存在维度灾难），与不受维度灾难影响的低范数解（weight decay）形成指数级分离；并揭示了"neural shattering"现象作为高维失败的几何机制。

**[Symbolic Regression Is All You Need: From Simulations to Scaling Laws in Binary Neutron Star Mergers](scientific_computing/symbolic_regression_is_all_you_need_from_simulations_to_scaling_laws_in_binary_n.md)**

:   利用符号回归（Symbolic Regression）从数值相对论模拟数据中自动发现双中子星并合后吸积盘质量的解析标定关系，所得紧凑表达式在预测精度、泛化能力和可解释性上全面超越文献中已有的经验拟合公式。

**[The Primacy of Magnitude in Low-Rank Adaptation](scientific_computing/the_primacy_of_magnitude_in_low-rank_adaptation.md)**

:   揭示 LoRA 中权重更新幅度（magnitude）是性能的根本驱动因素，统一了学习率、缩放因子和初始化策略对 LoRA 的影响机制，并提出 LoRAM——一种基于确定性正交基和幅度缩放的高效初始化方法，无需 SVD 即可匹敌甚至超越谱初始化方法。

**[Towards Universal Neural Operators Through Multiphysics Pretraining](scientific_computing/towards_universal_neural_operators_through_multiphysics_pretraining.md)**

:   提出基于 adapter 的多物理场预训练框架，通过将 lifting/projection 层作为问题特定适配器、冻结共享的核积分算子层，实现跨 PDE 问题的迁移学习，显著降低微调成本并提升泛化能力。

---

## ⚛️ 物理学 { #physics }

**[Astroco Self-Supervised Conformer-Style Transformers For Light-Curve Embeddings](physics/astroco_self-supervised_conformer-style_transformers_for_light-curve_embeddings.md)**

:   提出 AstroCo，一种将 Conformer（注意力 + 深度可分离卷积 + 门控）引入天文不规则光变曲线的自监督编码器，在 MACHO 数据集上重建误差比 Astromer v1/v2 降低 61-70%，少样本分类 macro-F1 提升约 7%。

**[Encoding and Understanding Astrophysical Information in Large Language Model-Generated Summaries](physics/encoding_and_understanding_astrophysical_information_in_large_language_model-gen.md)**

:   探究LLM嵌入是否能编码从X射线天文观测导出的物理量（硬度比、幂律指数、变异性），发现结构化prompt设计可将物理属性聚类纯度提升5.9%-57.5%，稀疏自编码器揭示LLM通过识别天体类型来推断未显式给出的物理参数。

**[Exoplanet Formation Inference Using Conditional Invertible Neural Networks](physics/exoplanet_formation_inference_using_conditional_invertible_neural_networks.md)**

:   用条件可逆神经网络（cINN）训练于15,777颗合成行星数据，从观测量（行星质量、轨道距离）快速推断行星形成参数（盘质量、湍流α、尘气比），实现比物理模型快~10⁶倍的概率性参数回溯，并证明多行星系统数据比单行星数据更鲁棒。

**[FAIR Universe HiggsML Uncertainty Dataset and Competition](physics/fair_universe_higgsml_uncertainty_dataset_and_competition.md)**

:   提供2.8亿模拟LHC碰撞事件的标准化数据集和竞赛平台，包含6种参数化系统偏差（探测器校准+背景成分）及不对称覆盖惩罚评估指标，要求参赛者为Higgs信号强度$\mu$估计鲁棒的68.27%置信区间，优胜方案通过无聚焦替代建模实现比传统binned方法窄约20%的置信区间。

**[Feat Free Energy Estimators With Adaptive Transport](physics/feat_free_energy_estimators_with_adaptive_transport.md)**

:   提出 FEAT 框架，基于随机插值学习自适应传输，通过 escorted Jarzynski 等式和 Crooks 定理提供一致、最小方差的自由能差估计器，统一了平衡与非平衡方法。

**[From Simulations to Surveys: Domain Adaptation for Galaxy Observations](physics/from_simulations_to_surveys_domain_adaptation_for_galaxy_observations.md)**

:   构建从模拟星系（TNG50）到真实巡天观测（SDSS）的域适应 pipeline，通过特征级对齐（欧几里得距离 + 最优传输 + top-$k$ 软匹配损失）和可训练权重调度，将星系形态分类的目标域准确率从 46.8%（无适应）提升到 87.3%，Macro F1 从 0.298 提升到 0.626。

**[Knowledge is Overrated: A Zero-Knowledge ML and Cryptographic Hashing-Based Framework for Verifiable, Low Latency Inference at the LHC](physics/knowledge_is_overrated_a_zero-knowledge_machine_learning_and_cryptographic_hashi.md)**

:   提出PHAZE框架，利用密码学哈希（Rabin指纹）和零知识机器学习（zkML）实现LHC触发器级别的可验证早退出推理，理论延迟降至~152-253ns量级，同时内建异常检测能力。

**[Latent Representation Learning In Heavy-Ion Collisions With Maskpoint Transforme](physics/latent_representation_learning_in_heavy-ion_collisions_with_maskpoint_transforme.md)**

:   将掩码点云 Transformer 自编码器引入重离子碰撞分析，通过自监督预训练+监督微调的两阶段范式，学习到比 PointNet 更强的非线性潜在表征（PC1 分布重叠从 2.42% 降至 0.27%），为 QGP 性质研究提供了通用特征学习框架。

**[Multi-Modal Masked Autoencoders for Galaxy Evolution and Cosmology](physics/multi-modal_masked_autoencoders_for_learning_image-spectrum_associations_for_gal.md)**

:   将多模态掩码自编码器 (MMAE) 应用于星系图像和光谱的联合重建，构建了 134,533 个星系的图像+光谱数据集，实现了光谱和图像的交叉重建以及仅从图像的红移回归，$\sigma_{\text{NMAD}} = 0.016$ 优于 AstroCLIP。

**[Neural Deprojection of Galaxy Stellar Mass Profiles](physics/neural_deprojection_of_galaxy_stellar_mass_profiles.md)**

:   用神经网络解决星系恒星质量轮廓的去投影问题——从 2D 投影光度轮廓恢复 3D 空间质量分布，替代传统的 Abel 反演解析方法，在处理噪声数据和复杂轮廓时更鲁棒且更快。

**[POLARIS: A High-contrast Polarimetric Imaging Benchmark Dataset for Exoplanetary Disk Representation Learning](physics/polaris_a_high-contrast_polarimetric_imaging_benchmark_dataset_for_exoplanetary_.md)**

:   构建首个系外行星偏振成像ML基准数据集POLARIS（921张VLT/SPHERE/IRDIS偏振图像+75,910张预处理曝光），提出Diff-SimCLR框架（扩散模型增强对比学习），在参考星vs目标星分类任务上达到93%准确率，仅需<10%手动标注。

**[Quantum Doubly Stochastic Transformers](physics/quantum_doubly_stochastic_transformers.md)**

:   提出 QDSFormer，用变分量子电路（QontOT）替换 ViT 中的 softmax 生成双随机注意力矩阵，在多个小规模图像识别任务上超越标准 ViT 和 Sinkformer，并显著稳定训练。

**[Simulation-Based Inference for Neutrino Interaction Model Parameter Tuning](physics/simulation-based_inference_for_neutrino_interaction_model_parameter_tuning.md)**

:   首次将基于仿真的推断（SBI）应用于中微子相互作用模型参数调优，使用神经后验估计（NPE）从200K个GENIE模拟的58-bin直方图中学习4个物理参数的后验分布，在MicroBooNE Tune的mock数据上准确恢复了真实参数值。

**[The Pareto Frontier of Resilient Jet Tagging](physics/the_pareto_frontier_of_resilient_jet_tagging.md)**

:   系统评估LHC射流标记任务中多种架构（DNN/PFN/EFN/ParT）的AUC-鲁棒性权衡，揭示更复杂模型虽AUC更高但对蒙特卡洛模型依赖性更强，构建Pareto前沿并通过案例研究证明低鲁棒性分类器即使校准后仍在下游参数估计中产生偏差。

**[The Platonic Universe: Do Foundation Models See the Same Sky?](physics/the_platonic_universe_do_foundation_models_see_the_same_sky.md)**

:   在天文学场景下验证柏拉图表征假说（PRH）：使用JWST、HSC、Legacy Survey和DESI光谱数据，测量6种基础模型（ViT/ConvNeXt/DINOv2/IJEPA/AstroPT/Specformer）的表征对齐度，发现模态内和跨模态MKNN分数随模型规模一致增加（p=3.31×10⁻⁵），支持不同架构和模态向共享表征收敛的假说。

**[TITAN: A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE](physics/titan_a_trajectory-informed_technique_for_adaptive_parameter_freezing_in_large-s.md)**

:   提出TITAN框架，用深度学习模型预测VQE中的"冻结参数"（训练过程中始终不活跃的参数），在初始化阶段即冻结40-60%参数，实现最高3倍收敛加速和40-60%电路评估量减少，在30量子比特的分子系统上匹配或超越基线精度。

**[Toward Complete Merger Identification at Cosmic Noon with Deep Learning](physics/toward_complete_merger_identification_at_cosmic_noon_with_deep_learning.md)**

:   在 IllustrisTNG50 模拟生成的模拟 HST CANDELS 图像上训练 ResNet18，首次证明深度学习可以在高红移 $1<z<1.5$ 下成功识别包括小质量比合并（minor merger, $\mu \geq 1/10$）和低质量星系（$M_\star > 10^8 M_\odot$）在内的星系合并，总体准确率约 73%，并通过 Grad-CAM 和 UMAP 深入分析了模型行为。

**[Transfer Learning Beyond the Standard Model](physics/transfer_learning_beyond_the_standard_model.md)**

:   研究从标准宇宙学模型（ΛCDM）预训练的神经网络能否迁移到超越标准模型的场景（大质量中微子、修改引力、原初非高斯性），发现dummy node架构可将模拟需求降低一个数量级，但当参数存在强物理简并（如σ₈-Mν）时会出现负迁移。

**[Tropical Attention Neural Algorithmic Reasoning For Combinatorial Algorithms](physics/tropical_attention_neural_algorithmic_reasoning_for_combinatorial_algorithms.md)**

:   提出 Tropical Attention，将注意力机制提升到热带射影空间中进行分段线性推理，在组合算法的 OOD 泛化上大幅超越 softmax 基线，同时推理速度快 3-9 倍、参数少 ~20%。

**[Unsupervised Discovery Of High-Redshift Galaxy Populations With Variational Auto](physics/unsupervised_discovery_of_high-redshift_galaxy_populations_with_variational_auto.md)**

:   用变分自编码器(VAE)对 2743 条 JWST 高红移($z>4$)星系光谱进行无监督聚类，发现 12 个不同的天体物理类别，使已知的后星暴星系、Lyman-α 发射星系、极端发射线星系、Little Red Dots 等稀有种群数量翻倍。

**[Why Is Attention Sparse In Particle Transformer](physics/why_is_attention_sparse_in_particle_transformer.md)**

:   分析 Particle Transformer (ParT) 在jet tagging中出现的二值化稀疏attention现象：稀疏性来自attention机制本身而非物理启发的interaction矩阵，但两者对性能都不可或缺。

---

## 🎁 推荐系统 { #recommender }

**[ASAP: An Agentic Solution to Auto-Optimize Performance of Large-Scale LLM Training](recommender/asap_an_agentic_solution_to_auto-optimize_performance_of_large-scale_llm_trainin.md)**

:   ASAP 是一个多 Agent 系统（Coordinator + Analyzer + Proposal），自动化诊断大规模 LLM 分布式训练的瓶颈类型（计算/内存/通信）并提出 sharding 配置方案，在 3 个实验场景中均匹配人类专家方案，实现最高 2.58× 吞吐量提升。

**[Balancing Performance and Costs in Best Arm Identification](recommender/balancing_performance_and_costs_in_best_arm_identification.md)**

:   提出将最优臂识别（BAI）从固定预算/固定置信度框架重新定义为"误识别概率/简单遗憾 + 采样成本"的风险泛函最小化问题，推导出含相变现象的下界（差距过小时最优策略是直接猜），设计 DBCARE 算法在动态预算下达到对数因子内最优。

**[EMPATHIA: Multi-Faceted Human-AI Collaboration for Refugee Integration](recommender/empathia_multi-faceted_human-ai_collaboration_for_refugee_integration.md)**

:   提出EMPATHIA多Agent框架，基于Kegan建构性发展理论，通过情感/文化/伦理三个专业化Agent的选择器-验证器协商评估难民安置建议，在6,359名难民的真实数据上达到87.4%收敛率和92.1%文化专家同意率。

**[Estimating Hitting Times Locally At Scale](recommender/estimating_hitting_times_locally_at_scale.md)**

:   提出两种局部（亚线性）算法估计图上的命中时间——基于相遇时间的 Algorithm 1 和基于谱截断的 Algorithm 3，无需全图访问仅通过以 $u,v$ 为中心的短随机游走完成估计，在合成和真实图上相对误差 <1.4%，并证明了游走采样的最优样本复杂度下界。

**[Inference-Time Reward Hacking in Large Language Models](recommender/inference-time_reward_hacking_in_large_language_models.md)**

:   本文从数学上证明了推理时对齐方法（如 BoN）在优化代理奖励时不可避免地会出现 reward hacking（真实奖励先升后降），提出了 Best-of-Poisson (BoP) 采样方法近似最优 KL-奖励折中分布，并设计了 HedgeTune 算法通过一维寻根找到最优推理时参数，在数学推理和人类偏好场景中有效缓解 reward hacking。

**[Measuring What Matters: Construct Validity in Large Language Model Benchmarks](recommender/measuring_what_matters_construct_validity_in_large_language_model_benchmarks.md)**

:   本文由29位专家对445篇LLM benchmark论文进行系统性综述，从构念效度 (construct validity) 角度审视现有LLM评测基准在现象定义、任务设计、评分指标和结论声明方面的不足，并提出8条改进建议。

**[MMPB: It's Time for Multi-Modal Personalization](recommender/mmpb_its_time_for_multi-modal_personalization.md)**

:   提出首个 VLM 个性化评测基准 MMPB，包含 111 个可个性化概念、10k+ 图文问答对和 15 种任务类型，评测了 23 个 VLM 后发现即使最强的 GPT-4o 在个性化任务上也表现不佳，揭示了 VLM 在偏好推理、视觉线索利用和安全对齐与个性化的冲突等方面的重大局限。

**[NeurIPS Should Lead Scientific Consensus on AI Policy](recommender/neurips_should_lead_scientific_consensus_on_ai_policy.md)**

:   本文是一篇立场论文，主张 NeurIPS 应主动承担 AI 政策领域的科学共识形成角色，借鉴 IPCC（政府间气候变化专门委员会）在气候科学中的成功经验，填补当前 AI 政策领域共识机制的空白。

**[Overcoming Sparsity Artifacts In Crosscoders To Interpret Chat-Tuning](recommender/overcoming_sparsity_artifacts_in_crosscoders_to_interpret_chat-tuning.md)**

:   识别Crosscoder L1训练中的稀疏性伪影导致虚假模型特定潜变量归因，提出BatchTopK损失+Latent Scaling揭示真正的chat特定概念。

**[PAC-Bayes Bounds for Multivariate Linear Regression and Linear Autoencoders](recommender/pac-bayes_bounds_for_multivariate_linear_regression_and_linear_autoencoders.md)**

:   本文将PAC-Bayes泛化界从单输出线性回归推广到**多变量线性回归**，并进一步适配到推荐系统中的**线性自编码器（LAE）**，通过理论方法将计算复杂度从O(n⁴)降到O(n³)，实验证明该界是紧的且与Recall@K、NDCG@K等实际指标高度相关。

**[Position: Towards Bidirectional Human-AI Alignment](recommender/position_towards_bidirectional_human-ai_alignment.md)**

:   本文提出**双向人机对齐（Bidirectional Human-AI Alignment）**框架，从系统综述400+篇论文出发，论证AI对齐不应仅是单向地"让AI对齐人类"，还应包括"让人类适应AI"这一被严重忽视的方向，并识别了当前研究的关键缺口。

**[Radial Neighborhood Smoothing Recommender System](recommender/radial_neighborhood_smoothing_recommender_system.md)**

:   提出 Radial Neighborhood Estimator (RNE)，通过将隐空间距离用观测矩阵的行/列 L2 范数近似估计，构建同时包含重叠和部分重叠用户-物品对的径向邻域，用局部核回归做平滑插补，在理论保证和实验中均优于传统协同过滤和矩阵分解方法，并天然缓解冷启动问题。

**[The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems](recommender/the_more_you_automate_the_less_you_see_hidden_pitfalls_of_ai_scientist_systems.md)**

:   本文系统性地识别了当前 AI 科学家系统的四种方法论陷阱（不当基准选择、数据泄漏、指标误用、事后选择偏差），通过精心设计的合成任务 SPR 对 Agent Laboratory 和 The AI Scientist v2 进行受控实验，发现两个系统均存在不同程度的问题，并证明审计 trace log + 代码比仅审查最终论文的检测准确率高 27 个百分点（82% vs 55%）。

**[Think before Recommendation: Autonomous Reasoning-enhanced Recommender](recommender/think_before_recommendation_autonomous_reasoning-enhanced_recommender.md)**

:   提出 RecZero（纯 RL 范式）和 RecOne（SFT+RL 混合范式），抛弃传统的 teacher-student 蒸馏方法，用 GRPO 强化学习直接训练单个 LLM 自主发展推理能力进行评分预测，通过结构化 "Think-before-Recommendation" 模板引导分步推理（分析用户→分析物品→匹配→评分），在 4 个数据集上显著超越现有基线。

**[Transformer Copilot: Learning from The Mistake Log in LLM Fine-tuning](recommender/transformer_copilot_learning_from_the_mistake_log_in_llm_fine-tuning.md)**

:   提出 Transformer Copilot 框架，在 LLM 微调过程中系统记录"错误日志"(Mistake Log)，训练一个辅助 Copilot 模型学习 Pilot 的错误模式，推理时通过 logits 修正提升生成质量，在 12 个基准上最高提升 34.5%。

**[VisualLens: Personalization through Task-Agnostic Visual History](recommender/visuallens_personalization_through_task-agnostic_visual_history.md)**

:   提出VisualLens框架，利用用户日常拍摄的与任务无关的视觉历史(task-agnostic visual history)，通过频谱用户画像(spectrum user profile)和多模态大模型实现跨领域个性化推荐，在新建的Google Review-V和Yelp-V数据集上Hit@3超越GPT-4o 2-5%。

**[Who You Are Matters: Bridging Topics and Social Roles via LLM-Enhanced Logical Recommendation](recommender/who_you_are_matters_bridging_topics_and_social_roles_via_llm-enhanced_logical_re.md)**

:   提出 TagCF 框架，通过 MLLM 提取用户角色标签和物品话题标签，再用 LLM 推理构建 U2I/I2U 逻辑图（用户角色与物品类型的因果关联），辅以标签编码器、对比学习增强和逻辑推理评分三种集成策略增强推荐，在亿级用户的工业在线A/B测试中互动指标提升0.946%、多样性提升0.102%，离线实验NDCG@10提升8.06%。

**[Wide-Horizon Thinking and Simulation-Based Evaluation for Real-World LLM Planning with Multifaceted Constraints](recommender/wide-horizon_thinking_and_simulation-based_evaluation_for_real-world_llm_plannin.md)**

:   提出 MAoP（Multiple Aspects of Planning）框架赋予 LLM "宽视野思维"能力，通过策略师预规划与路由机制并行整合多方面约束，配合 Travel-Sim 因果模拟评估基准，在旅行规划任务上大幅超越 CoT/分解方法，蒸馏后 3B 模型 PER 达 66.9%。

---

## 📡 信号/通信 { #signal_comm }

**[Angular Steering: Behavior Control via Rotation in Activation Space](signal_comm/angular_steering_behavior_control_via_rotation_in_activation_space.md)**

:   提出 Angular Steering，将 LLM 激活引导统一建模为固定 2D 子空间中的旋转操作，提供连续、细粒度、范数保持的行为控制，统一了现有的激活加法和方向消融方法，在多个 LLM 家族（3B-14B）上实现鲁棒的行为控制。

**[Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](signal_comm/artificial_hivemind_the_open-ended_homogeneity_of_language_models_and_beyond.md)**

:   构建了 Infinity-Chat 数据集（26K 开放式真实用户查询 + 31,250 条人类标注），揭示了 LM 在开放式生成中的"Artificial Hivemind"效应——模型内重复和模型间同质化严重，并发现 Reward Model 和 LM Judge 在个体偏好差异大的样本上校准失败。

**[Bispectral OT: Dataset Comparison using Symmetry-Aware Optimal Transport](signal_comm/bispectral_ot_dataset_comparison_using_symmetry-aware_optimal_transport.md)**

:   提出 Bispectral Optimal Transport (BOT)，将离散最优传输中的代价矩阵从原始像素距离替换为 bispectrum（群 Fourier 不变量）距离，使得传输计划在保持信号结构的同时精确消除群作用（如旋转）带来的变异，在旋转变换的 MNIST 等数据集上将类别保持准确率从 33% 提升至 84%。

**[ConTextTab: A Semantics-Aware Tabular In-Context Learner](signal_comm/contexttab_a_semantics-aware_tabular_in-context_learner.md)**

:   提出 ConTextTab，将语义理解融入 table-native ICL 框架，用数据类型特定嵌入并在大规模真实世界表格数据上训练，在语义丰富的 CARTE benchmark 上设立新 SOTA。

**[Contrastive Consolidation of Top-Down Modulations Achieves Sparsely Supervised Continual Learning](signal_comm/contrastive_consolidation_of_top-down_modulations_achieves_sparsely_supervised_c.md)**

:   提出 Task-Modulated Contrastive Learning (TMCL)，受大脑新皮层自顶向下调制启发，在持续学习中通过 affine modulation 集成稀疏标签信息（仅需 1% 标签），再利用对比学习将调制信息固化到前馈权重中，在 class-incremental 和迁移学习上超越无监督和有监督基线。

**[Don't Let It Fade: Preserving Edits in Diffusion Language Models via Token Timestep Allocation](signal_comm/dont_let_it_fade_preserving_edits_in_diffusion_language_mode.md)**

:   提出 Token Timestep Allocation (TTA-Diffusion)，通过为每个 token 分配独立的去噪时间步来解决扩散语言模型中 classifier guidance 导致的 update-forgetting 问题，实现可控文本生成的稳定性和效率大幅提升。

**[Estimation of Stochastic Optimal Transport Maps](signal_comm/estimation_of_stochastic_optimal_transport_maps.md)**

:   提出随机最优传输映射的新评价指标 $\mathcal{E}_p$（优化间隙+可行性间隙），发展了高效估计器，达到近优有限样本风险界 $\tilde{O}(n^{-1/(d+2p)})$，且仅需最小假设，是首个通用的（可能随机的）OT 映射估计理论。

**[Feature-aware Modulation for Learning from Temporal Tabular Data](signal_comm/feature-aware_modulation_for_learning_from_temporal_tabular_data.md)**

:   提出特征感知时间调制机制，通过基于时间上下文的可学习 Yeo-Johnson 变换动态调整特征分布（均值、标准差、偏度），实现跨时间语义对齐。

**[Masked Symbol Modeling for Demodulation of Oversampled Baseband Communication Signals](signal_comm/masked_symbol_modeling_for_demodulation_of_oversampled_baseband_communication_si.md)**

:   提出 Masked Symbol Modeling，将 BERT 的掩码预测范式应用于通信物理层，将脉冲成形引起的符号间贡献视为上下文信息，训练 Transformer 在干净信号上学习波形结构，推理时通过上下文恢复被冲激噪声破坏的符号。

**[Memory-Integrated Reconfigurable Adapters (MIRA)](signal_comm/memory-integrated_reconfigurable_adapters_a_unified_framework_for_settings_with_.md)**

:   提出 MIRA，将 Hopfield 联想记忆与 LoRA adapter 结合，在共享 backbone 的每个 ViT 层上存储 adapter 权重更新为 value、事后学习的 key 检索，统一处理域泛化、类增量学习和域增量学习，在多个设置下达到 SoTA。

**[Multi-Modal Masked Autoencoders for Galaxy Evolution and Cosmology](signal_comm/multi-modal_masked_autoencoders_for_learning_image-spectrum_associations_for_gal.md)**

:   将多模态掩码自编码器 (MMAE) 应用于星系图像和光谱的联合重建，构建了 134,533 个星系的图像+光谱数据集，实现了光谱和图像的交叉重建以及仅从图像的红移回归，$\sigma_{\text{NMAD}} = 0.016$ 优于 AstroCLIP。

**[Perturbation Bounds for Low-Rank Inverse Approximations under Noise](signal_comm/perturbation_bounds_for_low-rank_inverse_approximations_under_noise.md)**

:   首次给出在加性噪声下低秩逆近似 $\|(\tilde{A}^{-1})_p - A_p^{-1}\|$ 的非渐近谱范数扰动界，利用轮廓积分技术得到依赖特征间隙、谱衰减和噪声对齐的锐界，比经典全逆界改进高达 $\sqrt{n}$ 倍。

**[The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning](signal_comm/the_surprising_effectiveness_of_negative_reinforcement_in_llm_reasoning.md)**

:   揭示RLVR中负强化（仅惩罚错误）的効果超出预期，通过梯度分析说明其保持输出多样性和推理能力的机制，并提出改进的加权REINFORCE算法。

---

## ✍️ 文本生成 { #nlp_generation }

**[Bayesian Evaluation of Large Language Model Behavior](nlp_generation/bayesian_evaluation_of_large_language_model_behavior.md)**

:   提出基于 Beta-Binomial 贝叶斯模型的 LLM 行为评估框架，通过对每个 prompt 的随机生成结果建模 $\theta_m$ 后验分布，量化评估指标的统计不确定性，并引入 Thompson sampling 等序贯采样策略以更少的 API 调用获得更窄的置信区间。

**[Efficient Pre-Training of LLMs via Topology-Aware Communication Alignment on More Than 9600 GPUs](nlp_generation/efficient_pre-training_of_llms_via_topology-aware_communication_alignment_on_mor.md)**

:   提出 Arnold 调度系统，通过将 LLM 训练的通信模式（DP/PP group）与数据中心物理网络拓扑对齐，在模拟中将通信组最大跨度减少 1.67x，在 9600+ GPU 生产级训练中端到端性能提升 10.6%。

**[How Does Sequence Modeling Architecture Influence Base Capabilities of Pre-trained Language Models?](nlp_generation/how_does_sequence_modeling_architecture_influence_base_capabilities_of_pre-train.md)**

:   通过"限定领域预训练 + OOD 测试"的评估框架揭示 Mamba/RWKV 等 stateful 架构存在基础能力退化，并归纳出关键设计原则——"全序列任意选择能力"（full-sequence visibility + real relation calculation + non-uniform distribution），用极简的 Top-1 Element/Chunk Selection 架构验证该原则可恢复至接近 Transformer 的基础能力。

**[KScope: A Framework for Characterizing the Knowledge Status of Language Models](nlp_generation/kscope_a_framework_for_characterizing_the_knowledge_status_of_language_models.md)**

:   提出LLM知识状态的五分类法（一致正确/冲突正确/缺失/冲突错误/一致错误）和KScope层次化统计检验框架，通过重复采样+多步假设检验精确刻画LLM对给定问题的知识模式结构，并系统研究上下文如何更新各状态，发现受约束的上下文摘要+增强可信度平均提升4.3%的知识更新成功率。

**[Learning to Solve Complex Problems via Dataset Decomposition](nlp_generation/learning_to_solve_complex_problems_via_dataset_decomposition.md)**

:   提出Decomp方法，利用教师模型将复杂数学题按推理步骤递归分解为更简单的子问题，构建概念依赖图量化难度，再按从易到难的课程顺序训练学生模型——Qwen2.5-1.5B在MATH-500上达51.6%（超MuggleMath用147K数据的50.4%），Qwen3-4B在AIME2025仅用385样本达16.7%（超Qwen2.5-72B的15%）。

**[MaintainCoder: Maintainable Code Generation Under Dynamic Requirements](nlp_generation/maintaincoder_maintainable_code_generation_under_dynamic_requirements.md)**

:   首次系统定义并解决 LLM 代码生成的**可维护性**问题，同时贡献基准和方法：MaintainBench 通过 4 种需求变化模式 + 动态指标评测代码在需求演化下的可维护性；MaintainCoder 将 Waterfall 模型、设计模式与 6 个专业化 Agent 结合，动态可维护性指标提升 60%+，且初始代码正确性也一并提高。

**[Precise Information Control in Long-Form Text Generation](nlp_generation/precise_information_control_in_long-form_text_generation.md)**

:   提出Precise Information Control (PIC)任务——要求LLM生成的长文严格基于给定声明集合（不遗漏不添加），构建PIC-Bench评测8个任务发现SOTA模型70%以上生成包含忠实性幻觉，通过弱监督偏好数据构建+DPO训练的PIC-LM将8B模型F1从69.1%提升至91.0%。

**[Program Synthesis via Test-Time Transduction](nlp_generation/program_synthesis_via_test-time_transduction.md)**

:   提出 SYNTRA 框架，将程序合成重新定义为转导式学习——在测试时利用可见的 test inputs 和 LLM 的判断来迭代消除不一致的候选程序假设，通过 greedy maximin 算法最小化 LLM 查询次数，在 4 个 benchmark 上准确率提升最高达 196%。

**[SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents](nlp_generation/swe-rebench_an_automated_pipeline_for_task_collection_and_decontaminated_evaluat.md)**

:   构建全自动化流水线从 GitHub 持续挖掘真实软件工程交互任务，生成 21,000+ 可执行 Python 任务的 SWE-rebench 数据集和去污染 benchmark，揭示部分模型在 SWE-bench Verified 上的性能存在污染膨胀问题（如 DeepSeek-V3 在 SWE-bench 上 39.7% vs SWE-rebench 上 21.3%）。

**[Time Travel is Cheating: Going Live with DeepFund for Real-Time Fund Investment Benchmarking](nlp_generation/time_travel_is_cheating_going_live_with_deepfund_for_real-time_fund_investment_b.md)**

:   提出 DeepFund——首个实时基金投资 benchmark 工具，通过多智能体架构（Financial Planner + Analyst Team + Portfolio Manager）连接实时股市数据，避免传统回测中 LLM "时间旅行"导致的信息泄露问题。在 24 个交易日的实盘测试中，9 个旗舰 LLM 只有 Grok 3 实现盈利，揭示了当前 LLM 在主动基金管理中的重大局限。

**[URLs Help, Topics Guide: Understanding Metadata Utility in LLM Training](nlp_generation/urls_help_topics_guide_understanding_metadata_utility_in_llm_training.md)**

:   系统评估了三类元数据（URL、质量分数、主题/格式域信息）作为预训练上下文的效果：发现只有 URL 能加速训练（100B token 用 60B 即达到相同下游性能），且仅在长 prompt（5-shot）下有效；质量分数和主题域信息不加速训练但可用于 classifier-free guidance 实现可控生成。

---

## 📖 NLP 理解 { #nlp_understanding }

**[AgentiQL: An Agent-Inspired Multi-Expert Framework for Text-to-SQL Generation](nlp_understanding/agentiql_an_agent-inspired_multi-expert_framework_for_text-to-sql_generation.md)**

:   提出 AgentiQL，一个多专家 agent 框架用于 Text-to-SQL：reasoning agent 分解问题为子问题，coding agent 生成子查询，refinement 步骤校正列选择，adaptive router 在基线解析器和模块化 pipeline 之间智能路由，使用 14B 开源模型达到 86.07% EX（Spider），接近 GPT-4 SOTA(89.65%)。

**[Creativity or Brute Force? Using Brainteasers as a Window into the Problem-Solving Abilities of Large Language Models](nlp_understanding/creativity_or_brute_force_using_brainteasers_as_a_window_into_the_problem-solvin.md)**

:   构建Braingle Brainteaser基准（242数学+236逻辑谜题），系统评估LLM在脑筋急转弯上的推理策略——发现模型有时能产生创造性洞察式解法，但也常在有巧妙解法可用时退回暴力穷举，且自纠错能力有限、将叙事→数学格式翻译可小幅提升性能。

**[Efficient Semantic Uncertainty Quantification in Language Models via Diversity-Steered Sampling](nlp_understanding/efficient_semantic_uncertainty_quantification_in_language_models_via_diversity-s.md)**

:   提出 diversity-steered sampling 框架：在解码时注入基于 NLI 的语义相似度惩罚来驱动生成语义多样化的样本，并用重要性加权+控制变量纠正偏差降低方差，在仅 16 个样本下即可准确估计 LLM 的语义熵（偶然不确定性）和互信息（认知不确定性）。

**[Generalization Error Analysis for Selective State-Space Models Through the Lens of Attention](nlp_understanding/generalization_error_analysis_for_selective_state-space_models_through_the_lens_.md)**

:   将选择性SSM（Mamba）展开为注意力形式，利用覆盖数技术推导出受连续时间状态矩阵谱横断面$s_{\mathbf{A}}$控制的泛化界——$s_{\mathbf{A}}<0$时泛化界与序列长度无关，$s_{\mathbf{A}}\geq0$时指数增长，并证明这种依赖不可消除。

**[How Data Mixing Shapes In-Context Learning: Asymptotic Equivalence for Transformers with MLPs](nlp_understanding/how_data_mixing_shapes_in-context_learning_asymptotic_equivalence_for_transforme.md)**

:   在高维渐近框架下证明了带非线性MLP头的Transformer在ICL误差上等价于结构化多项式预测器，揭示了非线性MLP对非线性任务的增益机制，以及多源数据混合中低噪声和结构化协方差是高质量数据源的关键特征。

**[Planning without Search: Refining Frontier LLMs with Offline Goal-Conditioned RL](nlp_understanding/planning_without_search_refining_frontier_llms_with_offline_goal-conditioned_rl.md)**

:   提出PNLC方法，通过训练轻量级目标条件价值函数作为"自然语言评论家"，在推理步骤层面引导LLM智能体进行多轮规划和自我精化，无需直接微调或推理时搜索，在Web导航、社交推理、劝服等复杂交互任务上显著超越现有方法且推理速度快8-10倍。

**[Retrieval-Augmented Generation for Reliable Interpretation of Radio Regulations](nlp_understanding/retrieval-augmented_generation_for_reliable_interpretation_of_radio_regulations.md)**

:   针对无线电法规这一法律敏感的高风险领域，设计了专用 RAG 管道并构建了首个 ITU 无线电法规多选题评估集，检索准确率达 97%，在 GPT-4o 上实现 +11.9% 的问答准确率提升，远超直接将文档塞入 prompt 的方式。

**[SeCon-RAG: A Two-Stage Semantic Filtering and Conflict-Free Framework for Trustworthy RAG](nlp_understanding/secon-rag_a_two-stage_semantic_filtering_and_conflict-free_framework_for_trustwo.md)**

:   提出 SeCon-RAG 两阶段防御框架，第一阶段用聚类+语义图联合过滤毒化文档，第二阶段在推理时做冲突感知过滤，在5个LLM和3个QA数据集上全面超越现有RAG防御方法，在100%投毒率下仍保持高准确率和极低攻击成功率。

**[Text-to-Code Generation for Modular Building Layouts in Building Information Modeling](nlp_understanding/text-to-code_generation_for_modular_building_layouts_in_building_information_mod.md)**

:   提出 Text2MBL 框架，将自然语言描述转化为可执行的 BIM 代码（而非坐标序列），通过面向对象的代码架构和 LLM 微调实现模块化建筑布局的自动生成，在几何一致性上比坐标驱动方法提升 10%+ IoU。

**[The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation](nlp_understanding/the_atlas_of_in-context_learning_how_attention_heads_shape_in-context_retrieval_.md)**

:   通过 AttnLRP 归因方法系统解剖 LLM 在 in-context retrieval augmented QA 中的内部机制，发现三类功能特化的注意力头——Task heads（中间层，解析指令/问题）、Retrieval heads（后层，逐字复制上下文答案）、Parametric heads（编码参数化知识），并通过 Function Vector 注入和来源追踪探针验证其功能，在 Llama-3.1/Mistral/Gemma 上 ROC AUC ≥94%。

**[Weak-to-Strong Generalization under Distribution Shifts](nlp_understanding/weak-to-strong_generalization_under_distribution_shifts.md)**

:   发现朴素的弱到强泛化 (weak-to-strong generalization) 在分布偏移下会失败（强模型表现甚至不如弱监督者），提出 RAVEN 框架通过动态学习弱模型的最优组合权重来实现鲁棒的弱到强泛化，在 OOD 任务上超越基线 30%+。

---

## 🛰️ 遥感 { #remote_sensing }

**[C3PO: Cross-View Cross-Modality Correspondence by Pointmap Prediction](remote_sensing/c3po_cross-view_cross-modality_correspondence_by_pointmap_prediction.md)**

:   构建了包含 90K 地面照片-平面图对（597 个场景、153M 像素级对应和 85K 相机位姿）的 C3 数据集，揭示现有对应模型在跨视角跨模态（如地面照片 vs. 平面图）场景下的局限性，通过在该数据上训练可将最佳方法的 RMSE 降低 34%。

**[ChA-MAEViT: Unifying Channel-Aware Masked Autoencoders and Multi-Channel Vision Transformers for Improved Cross-Channel Learning](remote_sensing/chamaevit_unifying_channelaware_masked_autoencoders_and_mult.md)**

:   提出 ChA-MAEViT，通过动态通道-patch 联合掩码、记忆 token、混合 token 融合和通道感知解码器四个策略增强多通道成像（MCI）中的跨通道交互学习，在卫星和显微镜数据集上超越 SOTA MCI-ViT 方法 3.0-21.5%。

**[GeoLink: Empowering Remote Sensing FM with OpenStreetMap Data](remote_sensing/geolink_empowering_remote_sensing_foundation_model_with_openstreetmap_data.md)**

:   提出GeoLink，首个将OSM矢量数据直接融入遥感基础模型的框架，通过异构GNN编码OSM数据+多粒度跨模态对比/一致性学习+掩码高效预训练，在127万样本对上预训练后显著提升遥感和地理任务。

**[GreenHyperSpectra: Multi-Source Hyperspectral Dataset for Vegetation Traits](remote_sensing/greenhyperspectra_a_multi-source_hyperspectral_dataset_for_global_vegetation_tra.md)**

:   构建GreenHyperSpectra——14万+样本的多源高光谱植被数据集（跨地面/机载/星载传感器），框架化半/自监督方法用于多输出植被性状回归，在标签稀缺场景下显著超越监督基线。

**[Mass Conservation on Rails: PIML of Ice Flow Vector Fields](remote_sensing/mass_conservation_on_rails_--_rethinking_physics-informed_learning_of_ice_flow_v.md)**

:   对比硬约束（dfNN）、软约束（PINN）和无约束NN在南极冰流通量插值上的表现，通过流函数的辛梯度精确保证无散度的dfNN最优，结合方向引导进一步提升。

**[OrbitZoo: Real Orbital Systems Challenges for RL](remote_sensing/orbitzoo_real_orbital_systems_challenges_for_reinforcement_learning.md)**

:   构建OrbitZoo，基于工业标准库Orekit的多智能体RL环境，支持碰撞规避和协同机动，经Starlink真实数据验证MAPE仅0.16%。

**[OrthoLoC: UAV 6-DoF Localization Using Orthographic Geodata](remote_sensing/ortholoc_uav_6-dof_localization_and_calibration_using_orthographic_geodata.md)**

:   提出OrthoLoC——首个大规模UAV-正射影像配对数据集（16,425张，47地点，19城市），用于6-DoF定位和标定评估，AdHoP技术匹配精度提升95%、平移误差降低63%。

**[RSCC: Large-Scale Remote Sensing Change Caption Dataset for Disasters](remote_sensing/rscc_a_large-scale_remote_sensing_change_caption_dataset_for_disaster_events.md)**

:   提出RSCC数据集——62,351对灾前/灾后遥感图像配以丰富变化描述文本，覆盖地震/洪水/野火等，填补灾害相关双时相图像-文本缺口。

**[Scaling Image Geo-Localization to Continent Level](remote_sensing/scaling_image_geo-localization_to_continent_level.md)**

:   混合方法结合分类学习的原型和航拍图像嵌入，在覆盖西欧43.3万平方公里上实现200m内68%+、100m内59.2%的定位率，首次在大陆规模实现此精度。

---

## 🔎 AIGC 检测 { #aigc_detection }

**[ASCIIBench: Evaluating Language-Model-Based Understanding of Visually-Oriented Text](aigc_detection/asciibench_evaluating_language-model-based_understanding_of_visually-oriented_te.md)**

:   提出 ASCIIBench，首个用于评估 LLM 对 ASCII 艺术的生成和分类能力的基准数据集（5,315 张 ASCII 图像，752 类），发现当前 LLM 在需要空间/位置推理的 ASCII 任务上仍有显著局限，且 CLIP 嵌入在大多数 ASCII 类别上的区分能力接近随机水平。

**[Classical Planning with LLM-Generated Heuristics: Challenging the State of the Art with Python Code](aigc_detection/classical_planning_with_llm-generated_heuristics_challenging_the_state_of_the_ar.md)**

:   让 LLM 为经典规划问题生成 Python 启发式函数代码，从 n 个候选中选最优，在 IPC 2023 基准上用纯 Python 规划器超越了 C++ 实现的 SOTA 启发式（如 hFF），且保证所有计划正确。

**[CLAWS: Creativity Detection for LLM-Generated Solutions Using Attention Window of Sections](aigc_detection/clawscreativity_detection_for_llm-generated_solutions_using_attention_window_of_.md)**

:   提出 CLAWS，通过分析 LLM 在生成数学解答时对不同 prompt 区段的注意力权重分布，无需人工评估即可将生成内容分类为"创造性"、"典型"或"幻觉"三类。

**[DuoLens: A Framework for Robust Detection of Machine-Generated Multilingual Text and Code](aigc_detection/duolens_a_framework_for_robust_detection_of_machine-generated_multilingual_text_.md)**

:   提出 DuoLens，一种基于 CodeBERT + CodeBERTa 双编码器融合的 AI 生成内容检测框架，在多语言文本（8 种语言）和源代码（7 种编程语言）检测上以极低计算成本（延迟降低 8-12×，VRAM 降低 3-5×）实现 AUROC 0.97-0.99，远超 GPT-4o 等大模型。

**["Jutters"](aigc_detection/jutters.md)**

:   通过荷兰传统"jutters"（海岸拾荒者）的隐喻，构建了一个融合真实海滩碎片与AI生成图像/视频的沉浸式装置艺术，引导参观者以拾荒者心态反思如何对待AI生成内容。

**[Reasoning Compiler: LLM-Guided Optimizations for Efficient Model Serving](aigc_detection/reasoning_compiler_llm-guided_optimizations_for_efficient_model_serving.md)**

:   提出 Reasoning Compiler，将编译器优化建模为序列决策过程，用 LLM 作为上下文感知提案引擎 + MCTS 平衡探索/利用，在 5 个代表性 benchmark 和 5 个硬件平台上实现平均 5.0× 加速且采样效率比 TVM 进化搜索提升 10.8×。

**[Synthesizing Performance Constraints for Evaluating and Improving Code Efficiency](aigc_detection/synthesizing_performance_constraints_for_evaluating_and_improving_code_efficienc.md)**

:   提出Wedge框架——通过LLM合成性能刻画约束（performance-characterizing constraints）指导约束感知模糊测试，生成能暴露代码性能瓶颈的压力测试输入，构建PerfForge基准，使LLM代码优化器（如Effi-Learner）多减24% CPU指令。

---

## 🌍 地球科学 { #earth_science }

**[A Probabilistic U-Net Approach to Downscaling Climate Simulations](earth_science/a_probabilistic_unet_approach_to_downscaling_climate_simulat.md)**

:   将医学图像分割中的概率U-Net迁移到气候降尺度任务，通过变分隐空间建模不确定性，并系统比较了四种训练目标函数在捕捉极端事件与细尺度空间变异性方面的权衡。

**[Adaptive Online Emulation for Accelerating Complex Physical Simulations](earth_science/adaptive_online_emulation_for_accelerating_complex_physical_simulations.md)**

:   提出 Adaptive Online Emulation (AOE)，在物理模拟执行过程中动态训练 ELM 神经网络代理模型替代昂贵计算组件，无需离线预训练，在系外行星大气模拟上实现 11.1× 加速（91% 时间节省）且精度损失仅 ~0.01%。

**[ControlFusion: A Controllable Image Fusion Framework with Language-Vision Degradation Prompts](earth_science/controlfusion_a_controllable_image_fusion_framework_with_language-vision_degrada.md)**

:   提出 ControlFusion，一种基于语言-视觉退化提示的可控红外-可见光图像融合框架，通过物理驱动的退化成像模型模拟复合退化，并用 prompt-modulated 网络动态恢复+融合，在真实世界和复合退化场景下全面超越 SOTA。

**[Predicting Public Health Impacts of Electricity Usage](earth_science/predicting_public_health_impacts_of_electricity_usage.md)**

:   提出 HealthPredictor，一个将电力消费端到端映射到公共健康损害（以 $/MWh 计量）的 AI 流水线，包含燃料组合预测、空气质量转换和健康影响评估三个模块，健康驱动优化比燃料组合驱动基线显著降低健康影响预测误差，并在电动汽车充电调度案例中实现 24-42% 的健康损害减少。

**[Reasoning With a Star: A Heliophysics Dataset and Benchmark for Agentic Scientific Reasoning](earth_science/reasoning_with_a_star_a_heliophysics_dataset_and_benchmark_for_agentic_scientifi.md)**

:   提出 Reasoning With a Star (RWS)，一个源自 NASA 太阳物理暑期学校问题集的 158 道科学推理 benchmark（含数值/符号/文本三类答案），配合 unit-aware 评分器，比较了四种多 agent 协调模式（HMAW/PACE/PHASE/SCHEMA），发现没有单一模式在所有任务上占优——系统工程启发的 SCHEMA 在需要严格约束验证的任务上最强。

---

## 📂 其他 { #others }

**[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](others/4dgt_learning_a_4d_gaussian_transformer_using_realworld_mono.md)**

:   提出4DGT——一种基于4D高斯的Transformer模型，完全在真实世界单目带位姿视频上训练，以前馈方式在几秒内完成动态场景重建，显著优于同类前馈网络，并达到与优化类方法可比的精度。

**[A Cramér–von Mises Approach to Incentivizing Truthful Data Sharing](others/a_cramrvon_mises_approach_to_incentivizing_truthful_data_sha.md)**

:   提出一种基于 Cramér-von Mises 两样本检验统计量的激励机制，在贝叶斯和无先验两种设定下均能证明"如实提交数据"构成（近似）Nash 均衡，同时鼓励参与者提交更多真实数据，且不依赖对数据分布的强假设（如高斯、伯努利）。

**[A Differentiable Model Of Supply-Chain Shocks](others/a_differentiable_model_of_supply-chain_shocks.md)**

:   用 JAX 实现可微分的供应链 Agent-Based Model（~1000 家企业），通过 GPU 并行化 + 自动微分实现比传统 ABC 快 3 个数量级的贝叶斯参数校准，为全球供应链网络的冲击传播建模铺平道路。

**[A Generalized Label Shift Perspective for Cross-Domain Gaze Estimation](others/a_generalized_label_shift_perspective_for_crossdomain_gaze_e.md)**

:   本文将跨域视线估计(CDGE)问题建模为广义标签偏移(GLS)问题，指出现有域不变表示学习方法在标签偏移存在时理论上不充分，提出基于截断高斯分布的连续重要性重加权和概率感知条件算子差异(PCOD)来联合纠正标签偏移和条件偏移，在多个backbone上平均降低误差12%~27%。

**[A High-Dimensional Statistical Method for Optimizing Transfer Quantities in Multi-Source Transfer Learning](others/a_highdimensional_statistical_method_for_optimizing_transfer.md)**

:   提出基于K-L散度和高维统计分析的理论框架，用于确定多源迁移学习中每个源任务的最优样本迁移数量，避免"用所有源数据"带来的负迁移问题，在DomainNet和Office-Home上超过SOTA 1.0-1.5%的同时减少47.85%的样本使用量和35.19%的训练时间。

**[A Reliable Cryptographic Framework for Empirical Machine Unlearning Evaluation](others/a_reliable_cryptographic_framework_for_empirical_machine_unl.md)**

:   将机器遗忘的评估问题建模为密码学博弈（unlearning sample inference game），通过定义adversary的"advantage"来衡量遗忘质量，克服了传统MIA准确率作为评估指标的多种缺陷（不以retrain为零基准、对数据划分敏感、对MIA选择敏感），并提出SWAP test作为高效的实用近似方案。

**[A Standardized Benchmark for Multilabel Antimicrobial Peptide Classification](others/a_standardized_benchmark_for_multilabel_antimicrobial_peptide_classification.md)**

:   提出 **ESCAPE**——首个标准化的多标签抗菌肽分类基准，整合 27 个公开数据库共 80,000+ 肽段，并设计基于双分支 Transformer + 双向交叉注意力的 Baseline 模型，在 mAP 上相对第二名提升 2.56%。

**[A Sustainable AI Economy Needs Data Deals That Work for Generators](others/a_sustainable_ai_economy_needs_data_deals_that_work_for_gene.md)**

:   本文通过分析73个公开数据交易案例，揭示了ML价值链中的"经济数据处理不等式"——从原始数据到模型权重再到合成输出，每一步都提炼了技术信号但剥夺了数据生成者的经济权益，并提出EDVEX框架来构建更公平的数据交换市场。

**[A Theoretical Framework for Grokking: Interpolation followed by Riemannian Norm Minimisation](others/a_theoretical_framework_for_grokking_interpolation_followed_by_riemannian_norm_m.md)**

:   本文从纯优化角度严格证明了 grokking 现象的成因：带小 weight decay 的梯度流在 $\lambda\to 0$ 极限下呈现两阶段动力学——先快速收敛到训练损失的临界流形 $\mathcal{M}$，再在 $t\approx 1/\lambda$ 时沿流形做黎曼梯度流以最小化 $\ell_2$ 范数，从而延迟实现泛化。

**[A Unified Framework for Provably Efficient Algorithms to Estimate Shapley Values](others/a_unified_framework_for_provably_efficient_algorithms_to_estimate_shapley_values.md)**

:   提出统一框架将 KernelSHAP、LeverageSHAP 等 Shapley 值估计器纳入随机草图（sketching）视角，首次为 KernelSHAP 提供非渐近理论保证，并通过算法改进（Poisson 近似等）将方法扩展到 CIFAR-10 等高维数据集。

**[A Unified Framework for Variable Selection in Model-Based Clustering with Missing Not at Random](others/a_unified_framework_for_variable_selection_in_modelbased_clu.md)**

:   提出了一个统一框架（SelvarMNARz），在高斯混合模型聚类中同时完成变量选择和MNAR（Missing Not At Random）缺失数据建模，通过两阶段策略（LASSO排序 + BIC角色分配）实现高维场景下的高效推理，并给出了可辨识性和选择一致性的理论保证。

**[Active Measurement: Efficient Estimation at Scale](others/active_measurement_efficient_estimation_at_scale.md)**

:   提出Active Measurement框架，结合AI检测器的自适应重要性采样和迭代人工标注，实现大规模科学测量（如鸟类计数、疟疾检测）的无偏估计，将原始检测器3.78的误差率降至0.06，同时提供理论保证的置信区间。

**[AcuRank: 不确定性感知的自适应计算重排序](others/acurank_uncertainty-aware_adaptive_computation_for_listwise_reranking.md)**

:   通过基于TrueSkill模型的不确定性估计，动态调整重排序子集大小和验证范围，在实现更优精度效率权衡的同时避免过度计算。

**[AdaptGrad: Adaptive Sampling to Reduce Noise](others/adaptgrad_adaptive_sampling_to_reduce_noise.md)**

:   通过卷积公式视角首次理论分析了SmoothGrad的噪声来源（越界采样），提出AdaptGrad方法通过概率界约束采样范围来抑制噪声，在不增加计算开销的前提下提升梯度显著性图的质量。

**[Adaptive Data Analysis for Growing Data](others/adaptive_data_analysis_for_growing_data.md)**

:   首次为动态/增长数据场景下的自适应数据分析提供泛化界，允许分析者根据当前数据规模和历史查询结果自适应地调度统计查询，在数据不断积累时获得更紧的准确性保证。

**[Additive Models Explained: A Computational Complexity Approach](others/additive_models_explained_a_computational_complexity_approach.md)**

:   对广义可加模型（GAM）的多种解释类型（充分理由、对比解释、Shapley值等）进行系统的计算复杂度分析，揭示了GAM的可解释性代价高度依赖于输入域类型、组件模型类型和任务类型（回归vs分类），某些看似"可解释"的设定实际上是NP-Hard甚至#P-Hard。

**[Addressing Mark Imbalance In Integrationfree Neural Marked T](others/addressing_mark_imbalance_in_integrationfree_neural_marked_t.md)**

:   论文针对现实事件流中常见的 mark 类别长尾失衡问题，提出基于先验归一化概率的阈值学习策略，并设计 integration-free 的神经 MTPP 架构，先预测 mark 再预测 time，在避免昂贵数值积分的同时显著提升稀有事件的 mark 与到达时间预测性能。

**[Adjoint Schrödinger Bridge Sampler](others/adjoint_schrödinger_bridge_sampler.md)**

:   提出 Adjoint Schrödinger Bridge Sampler (ASBS)，通过将 Schrödinger Bridge 问题重新解释为随机最优控制问题，消除了先前扩散采样器的 memoryless 条件限制，支持任意源分布（如高斯、谐波先验），使用可扩展的 matching 目标无需重要性权重估计，在多粒子能量函数和分子构象生成上全面超越先前方法。

**[ADPretrain: Advancing Industrial Anomaly Detection via Anomaly Representation Pretraining](others/adpretrain_advancing_industrial_anomaly_detection_via_anomaly_representation_pre.md)**

:   首次提出面向工业异常检测的专用表示预训练框架 ADPretrain，通过角度和范数导向的对比损失在大规模异常检测数据集 RealIAD 上学习残差特征表示，替换五种主流嵌入式 AD 方法的原始特征后在五个数据集、五个骨干网络上取得一致性提升。

**[Aggregation Hides OOD Generalization Failures from Spurious Correlations](others/aggregation_hides_out-of-distribution_generalization_failures_from_spurious_corr.md)**

:   揭示 OOD 泛化 benchmark 中"聚合掩蔽"现象——aggregate 评估显示 accuracy-on-the-line（ID 与 OOD 准确率正相关），但 OODSelect 方法可从同一 OOD 数据中找到大规模语义连贯子集（最高达 75%），这些子集上 ID 越高 OOD 反而越低（Pearson R 低至 -0.92），证明虚假相关的危害被聚合评估系统性隐藏。

**[Alias-Free ViT: Fractional Shift Invariance via Linear Attention](others/alias-free_vit_fractional_shift_invariance_via_linear_attention.md)**

:   提出Alias-Free ViT，通过两个关键组件实现Vision Transformer对整数和亚像素平移的鲁棒性：(1) 抗混叠下采样和非线性层设计，(2) 基于交叉协方差的线性注意力（shift-equivariant），在图像分类中保持竞争力的同时显著提升对抗性平移鲁棒性。

**[Alternating Gradient Flows: A Theory of Feature Learning in Two-layer Neural Networks](others/alternating_gradient_flows_a_theory_of_feature_learning_in_two-layer_neural_netw.md)**

:   提出交替梯度流（AGF）理论框架解释神经网络的逐步"鞍到鞍"特征学习动力学——将训练建模为休眠神经元的效用最大化和活跃神经元的代价最小化的交替过程，统一了对角线性网络、注意力模型和模块加法的特征选择分析，预测与实际梯度流高度一致。

**[An Analysis of Concept Bottleneck Models: Measuring, Understanding, and Mitigating Noisy Annotations](others/an_analysis_of_concept_bottleneck_models_measuring_understanding_and_mitigating_.md)**

:   首次系统研究噪声概念标注对 CBM 的影响——发现即使中等噪声也同时损害预测性能、可解释性和干预效果，识别出"脆弱概念"子集是性能下降的主因，提出训练阶段用 SAM 稳定脆弱概念学习 + 推断阶段用预测熵排序仅校正最不确定概念的两阶段缓解框架。

**[An Empirical Investigation of Neural ODEs and Symbolic Regression for Dynamical Systems](others/an_empirical_investigation_of_neural_odes_and_symbolic_regression_for_dynamical_.md)**

:   系统实证研究 Neural ODE 和符号回归（SR）在动力系统建模中的组合使用：NODE 可以在动态相似条件下外推到新边界条件，SR 可以从有噪声数据中恢复控制方程，且用 NODE 训练数据（仅 10% 原始数据）生成的数据也能让 SR 恢复大部分方程。

**[EPHAD: An Evidence-Based Post-Hoc Adjustment Framework for Anomaly Detection Under Data Contamination](others/an_evidence-based_post-hoc_adjustment_framework_for_anomaly_detection_under_data.md)**

:   EPHAD 提出一种测试时后处理框架来修正在被污染数据上训练的异常检测模型——在不接触训练流程/数据的前提下，用多模态基础模型（CLIP）或经典方法（LOF）等"证据"在测试时调整模型输出，在 8 个视觉+26 个表格 AD 数据集上有效提升性能。

**[Are Pixel-Wise Metrics Reliable For Sparse-View Computed Tomography Reconstructi](others/are_pixel-wise_metrics_reliable_for_sparse-view_computed_tomography_reconstructi.md)**

:   揭示 PSNR/SSIM 等像素级指标无法反映稀疏视图 CT 重建中解剖结构完整性（相关性仅 0.16-0.30），提出基于自动分割的解剖感知指标（NSD/clDice）和 CARE 框架——在扩散模型训练中加入分割引导损失，大器官结构完整性提升 32%、血管提升 36%。

**[Asymmetric Duos: Sidekicks Improve Uncertainty](others/asymmetric_duos_sidekicks_improve_uncertainty.md)**

:   Asymmetric Duos（AD）将一个大模型与一个小"sidekick"配对——通过温度加权的 logit 平均融合两者预测，在仅增加 10-20% FLOPs 的条件下达到接近 5× 深度集成的不确定性估计质量，RN50 AD（5% FLOPs 额外开销）在 AUROC/AURC/SAC@98 上接近 m=5 深度集成（400% 额外 FLOPs）。

**[AutoSciDACT: Automated Scientific Discovery through Contrastive Embedding and Hypothesis Testing](others/autoscidact_automated_scientific_discovery_through_contrastive_embedding_and_hyp.md)**

:   提出 AutoSciDACT 管线：先用有监督对比学习将高维科学数据压缩到 4 维嵌入空间，再用 NPLM（New Physics Learning Machine）似然比检验对嵌入空间中的分布偏差进行统计量化，在天文、粒子物理、病理、图像和合成数据集上以 ≤1% 的信号注入比例实现 ≥3σ 发现。

**[AVerImaTeC: A Dataset for Automatic Verification of Image-Text Claims with Evidence from the Web](others/averimatec_a_dataset_for_automatic_verification_of_image-text_claims_with_eviden.md)**

:   AVerImaTeC 构建了首个带完整证据标注的图文事实核查数据集——1297 条真实图文声明 + 5 阶段标注流水线（提取→QA 推理→充分性检查→迭代精炼→二次检查）+ 时间约束证据（防止时间泄露），基线系统在有 ground truth 证据时准确率 82%，但自动检索证据后降至 15-25%，揭示了图文核查的巨大挑战。

**[Beyond Benign Overfitting in Nadaraya-Watson Interpolators](others/beyond_benign_overfitting_in_nadaraya-watson_interpolators.md)**

:   通过调节 Nadaraya-Watson 插值器中的单一带宽参数 $\beta$，精确刻画了从灾难性过拟合（$\beta < d$）→ 良性过拟合（$\beta = d$）→ 温和过拟合（$\beta > d$）的完整相变谱，证明高估数据内禀维度比低估更安全。

**[Brain-Like Processing Pathways Form in Models With Heterogeneous Experts](others/brain-like_processing_pathways_form_in_models_with_heterogeneous_experts.md)**

:   在异构 Mixture-of-Experts 模型中，异构专家并不会自动形成处理通路；本文提出三个受大脑启发的归纳偏置（路由代价、任务表现缩放、专家 Dropout），使模型形成类似大脑"皮层-皮层下"动态通路的 Mixture-of-Pathways 架构。

**[CLIMB: Class-Imbalanced Learning Benchmark on Tabular Data](others/climb_class-imbalanced_learning_benchmark_on_tabular_data.md)**

:   提出 Climb——迄今最全面的表格数据类别不平衡学习基准，涵盖 73 个真实数据集和 29 种 CIL 算法，通过大规模实验揭示了朴素重平衡往往无效、集成方法至关重要、数据质量比不平衡本身更影响性能等实用洞察。

**[Computable Universal Online Learning](others/computable_universal_online_learning.md)**

:   在 universal online learning 框架中引入可计算性约束，证明了"数学上可学习"不等于"可用计算机程序实现的可学习"，并给出了 agnostic 和 proper 变体下可计算学习的精确刻画。

**[Conformal Online Learning Of Deep Koopman Linear Embeddings](others/conformal_online_learning_of_deep_koopman_linear_embeddings.md)**

:   提出 COLoKe 框架，将 conformal prediction 重新解读为模型一致性诊断工具，仅在 Koopman 模型的预测误差超过动态校准阈值时才触发参数更新，从而实现对非线性动力系统的高效在线 Koopman 线性嵌入学习。

**[Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization](others/conformal_prediction_in_the_loop_a_feedback-based_uncertainty_model_for_trajecto.md)**

:   提出 Feedback-Based Conformal Prediction (Fb-CP) 框架，将已执行轨迹的信息反馈给 CP 以动态调整预测区域大小，在缩减时域轨迹优化中同时保证覆盖率和显著提升轨迹性能。

**[Contextual Dynamic Pricing with Heterogeneous Buyers](others/contextual_dynamic_pricing_with_heterogeneous_buyers.md)**

:   首次系统研究买家类型异质（$K_\star$ 种未知类型）的上下文动态定价问题，提出基于乐观后验采样 (OPS) 的算法实现 $\tilde{O}(K_\star\sqrt{dT})$ 遗憾界（对 $d$ 和 $T$ 最优），并在非上下文情形通过方差感知自适应离散化算法 ZoomV 实现 $\tilde{O}(\sqrt{K_\star T})$ 最优遗憾。

**[Continuous Thought Machines](others/continuous_thought_machines.md)**

:   提出 Continuous Thought Machine (CTM)，通过私有参数化的 Neuron-Level Models (NLMs) 产生神经元级时间动力学，并以神经同步矩阵作为核心潜在表征，在迷宫求解、ImageNet 分类、奇偶校验等任务上展现复杂推理、自适应计算和可解释注意力行为。

**[Coreset for Robust Geometric Median: Eliminating Size Dependency on Outliers](others/coreset_for_robust_geometric_median_eliminating_size_dependency_on_outliers.md)**

:   首次消除鲁棒几何中位数 coreset 大小对异常值数 $m$ 的依赖：在 $n \geq 4m$ 条件下，$d=1$ 时实现最优 coreset 大小 $\tilde{\Theta}(\varepsilon^{-1/2} + \frac{m}{n}\varepsilon^{-1})$，高维时实现 $\tilde{O}(\varepsilon^{-2}\min\{\varepsilon^{-2}, d\})$，核心技术是新颖的**非逐分量误差分析**。

**[Coresets for Clustering Under Stochastic Noise](others/coresets_for_clustering_under_stochastic_noise.md)**

:   首次系统研究噪声数据下 $(k,z)$-聚类 coreset 构造问题，提出新的代理误差度量 $\mathsf{Err}_\alpha$ 替代传统 $\mathsf{Err}$，在温和数据假设下实现 coreset 大小缩减 $\text{poly}(k)$ 倍、质量保证收紧 $\text{poly}(k)$ 倍，并设计噪声感知的 cluster-wise 采样算法。

**[Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning](others/cost-sensitive_freeze-thaw_bayesian_optimization_for_efficient_hyperparameter_tu.md)**

:   CFBO 将用户定义的效用函数（成本 vs 性能的权衡）引入冻结-解冻贝叶斯优化框架，结合自适应停止准则和基于 LC mixup 的迁移学习，在多保真度 HPO 基准上实现了成本-性能最优权衡。

**[Deep Continuous-Time State-Space Models for Marked Event Sequences](others/deep_continuous-time_state-space_models_for_marked_event_sequences.md)**

:   S2P2 将线性 Hawkes 过程与深度状态空间模型结合，通过堆叠多层隐式线性 Hawkes (LLH) 层 + 非线性激活构建高表达力的连续时间 MTPP 模型，利用并行扫描实现线性复杂度和亚线性时间，在 8 个真实数据集上平均提升 33% 预测似然。

**[Deep Legendre Transform](others/deep_legendre_transform.md)**

:   DLT 利用凸共轭的隐式 Fenchel 表示 $f^*(\nabla f(x)) = \langle x, \nabla f(x) \rangle - f(x)$ 将凸共轭计算转化为标准回归问题，避免求解 max/min-max 优化，且能提供后验误差估计，结合 KAN 还可获得精确解析解。

**[Depth-Bounds for Neural Networks via the Braid Arrangement](others/depth-bounds_for_neural_networks_via_the_braid_arrangement.md)**

:   本文证明了在 $\mathcal{B}_d^0$-conforming 约束下，ReLU 网络精确表示 $\max\{0, x_1, \ldots, x_d\}$ 需要 $\Omega(\log \log d)$ 层——这是首个不限制权重的非常数深度下界；同时证明 rank-(3,2) maxout 网络可以计算 7 个数的最大值，说明标准上界不紧。

**[Depth-Supervised Fusion Network for Seamless-Free Image Stitching](others/depth-supervised_fusion_network_for_seamless-free_image_stitching.md)**

:   DSFN 提出深度一致性约束的无缝图像拼接方法：通过深度感知的两阶段变换估计解决大视差对齐，软缝合区域扩散实现自然融合，结合重参数化策略提升效率，在 UDIS-D 和 IVSD 数据集上全面超越 SOTA。

**[Directional Non-Commutative Monoidal Structures for Compositional Embeddings in Machine Learning](others/directional_non-commutative_monoidal_structures_for_compositional_embeddings_in_.md)**

:   提出一种基于方向性非交换幺半群算子的代数框架，为多维组合嵌入提供统一数学基础，将 SSM 递归、Transformer 自注意力和 RoPE 位置编码统一为特例。

**[Distributional Autoencoders Know the Score](others/distributional_autoencoders_know_the_score.md)**

:   本文为 Distributional Principal Autoencoder (DPA) 提供了精确的理论保证：证明了最优编码器的等值面几何与数据分布的 score 函数之间的闭合形式关系，并证明了超出流形维度的潜在分量与数据条件独立，从而统一了分布学习与内在维度发现两个长期目标。

**[Distributionally Robust Feature Selection](others/distributionally_robust_feature_selection.md)**

:   本文提出一种模型无关的分布鲁棒特征选择方法，通过向协变量注入可控高斯噪声实现离散选择的连续松弛，并优化 Bayes 最优预测器的条件方差，使选出的特征子集能在多个子群体上同时训练出高质量下游模型。

**[Double Descent Meets Out-of-Distribution Detection: Theoretical Insights and Empirical Analysis](others/double_descent_meets_out-of-distribution_detection_theoretical_insights_and_empi.md)**

:   本文首次揭示 post-hoc OOD 检测中存在 double descent 现象——OOD 检测性能随模型宽度在插值阈值附近出现谷值后再次上升，通过随机矩阵理论提供理论解释，并提出基于 Neural Collapse 的 NC1 判据来识别最佳模型复杂度区间。

**[DPA: A One-Stop Metric to Measure Bias Amplification in Classification Datasets](others/dpa_a_one-stop_metric_to_measure_bias_amplification_in_classification_datasets.md)**

:   本文提出 Directional Predictability Amplification (DPA)，一种基于可预测性的偏差放大度量指标，是唯一同时满足方向性、适用于平衡/非平衡数据集、能正确识别正负偏差放大的一站式指标，通过测量模型偏差与数据集偏差的相对变化来量化偏差放大程度。

**[Dynamic Algorithm for Explainable k-medians Clustering under lp Norm](others/dynamic_algorithm_for_explainable_k-medians_clustering_under_lp_norm.md)**

:   本文提出首个适用于一般 $\ell_p$ 范数的可解释 k-medians 聚类算法，实现 $\tilde{O}(p(\log k)^{1+1/p-1/p^2})$ 近似比（改进了 p=2 的已知最优界），并给出首个动态版本：在中心集合的插入/删除下，以 $O(d \log^3 k)$ 摊还更新时间和 $O(\log k)$ 重分配次数维护可解释聚类。

**[Efficient Parametric SVD of Koopman Operator for Stochastic Dynamical Systems](others/efficient_parametric_svd_of_koopman_operator_for_stochastic_dynamical_systems.md)**

:   提出基于 low-rank approximation (LoRA) 的目标函数来学习随机动力系统 Koopman 算子的 top-k 奇异函数，完全避免了 VAMPnet/DPNet 中数值不稳定的矩阵分解操作，且梯度天然无偏。

**[Emergency Response Measures for Catastrophic AI Risk](others/emergency_response_measures_for_catastrophic_ai_risk.md)**

:   本文分析了如何将前沿安全政策（Frontier Safety Policies, FSPs）模型整合到中国四阶段应急响应框架中，以应对来自先进AI系统的灾难性风险（如大规模杀伤性武器扩散、失控事件等）。

**[Empowering Decision Trees via Shape Function Branching](others/empowering_decision_trees_via_shape_function_branching.md)**

:   提出 Shape Generalized Tree (SGT)，在决策树每个内部节点使用可学习的轴对齐形状函数替代传统线性阈值分裂，以更紧凑的树结构捕捉非线性特征效应，同时保持可解释性。

**[Enhancing Sample Selection Against Label Noise by Cutting Mislabeled Easy Examples](others/enhancing_sample_selection_against_label_noise_by_cutting_mislabeled_easy_exampl.md)**

:   发现并定义了误标注易学样本（Mislabeled Easy Examples, MEEs）——被模型早期训练即正确预测为错误标签的样本对泛化伤害最大，并提出 Early Cutting 方法利用模型后期状态重新校准早期置信子集来过滤MEEs。

**[Equivariance by Contrast: Identifiable Equivariant Embeddings from Unlabeled Finite Group Actions](others/equivariance_by_contrast_identifiable_equivariant_embeddings_from_unlabeled_fini.md)**

:   提出 Equivariance by Contrast (EbC)，一种仅用编码器的方法，从观测对 $(\mathbf{y}, g \cdot \mathbf{y})$ 中联合学习等变嵌入空间和隐式群表示，使有限群作用在潜空间中对应可逆线性映射，并提供可辨识性理论保证。

**[Evaluating In Silico Creativity: An Expert Review of AI Chess Compositions](others/evaluating_in_silico_creativity_an_expert_review_of_ai_chess_compositions.md)**

:   使用生成式神经网络（自回归Transformer、离散扩散、MaskGit）+强化学习生成国际象棋谜题，通过奖励函数筛选具有唯一解和反直觉性的谜题，并邀请三位世界级国际象棋专家评审AI生成谜题的创造力和美学品质。

**[EvoBrain: Dynamic Multi-Channel EEG Graph Modeling for Time-Evolving Brain Networks](others/evobrain_dynamic_multi-channel_eeg_graph_modeling_for_time-evolving_brain_networ.md)**

:   提出 EvoBrain——首次从理论上证明 **显式动态图建模** 优于隐式静态图、**time-then-graph** 架构表达力严格优于其他两种动态 GNN 范式(graph-then-time / time-and-graph)，并据此设计双流 Mamba + Laplacian PE 增强的 GCN 模型，在 TUSZ 和 CHB-MIT 数据集的癫痫检测与早期预测任务上取得 AUROC 提升 23%、F1 提升 30% 的显著效果，同时训练速度比 SOTA 快 17 倍。

**[Evolutionary Prediction Games](others/evolutionary_prediction_games.md)**

:   提出"演化预测博弈"框架，用演化博弈论分析预测算法与用户群体之间的反馈循环，揭示理想学习器导致竞争排斥（强者生存），而实际学习器（有限数据/代理损失/过参数化）反而能促成群体间的稳定共存与互利共生。

**[Exact Learning of Arithmetic with Differentiable Agents](others/exact_learning_of_arithmetic_with_differentiable_agents.md)**

:   提出可微有限状态转换器（DFST），一种图灵完备且端到端可微的模型族，在 2D 符号网格上通过观察专家算术计算的中间步骤（Policy-Trajectory Observations）训练，仅用 20 个样本（最长 3 位数加法）即可完美泛化到 3850 位二进制加法、2450 位十进制加法，未发现任何错误。

**[Exploiting Task Relationships in Continual Learning via Transferability-Aware Task Embeddings](others/exploiting_task_relationships_in_continual_learning_via_transferability-aware_ta.md)**

:   提出基于 H-score 可迁移性度量的任务嵌入（H-embedding），并将其嵌入超网络框架，通过在嵌入空间中显式建模任务间关系来指导持续学习中的参数生成，在 rehearsal-free 设定下取得 SOTA 最终准确率。

**[Faithful Group Shapley Value](others/faithful_group_shapley_value.md)**

:   提出 Faithful Group Shapley Value (FGSV)，唯一满足含"忠实性"在内五条公理的组级数据估值方法，有效防御"空壳公司攻击"（通过拆分子组不当膨胀估值），并设计了 $O(n \cdot \text{Poly}(\log n))$ 复杂度的高效近似算法。

**[Final-Model-Only Data Attribution with a Unifying View of Gradient-Based Methods](others/final-model-only_data_attribution_with_a_unifying_view_of_gradient-based_methods.md)**

:   明确提出"仅有最终模型"(FiMO)的训练数据归因设定，将问题从"贡献度"重构为"敏感性"度量，提出 further training 作为金标准，并统一推导出多种梯度方法（Grad-Dot、影响函数、TRAK、DataInf 等）均为 further training 的不同阶近似。

**[Finding Structure In Continual Learning](others/finding_structure_in_continual_learning.md)**

:   提出基于Douglas-Rachford Splitting (DRS)的持续学习优化框架，将稳定性与可塑性解耦为两个独立的近端子问题，并结合Rényi散度替代KL散度实现更鲁棒的先验对齐，从而在无需回放缓冲区或额外模块的条件下有效缓解灾难性遗忘。

**[FlashMD: Long-Stride, Universal Prediction of Molecular Dynamics](others/flashmd_long-stride_universal_prediction_of_molecular_dynamics.md)**

:   提出 FlashMD，基于 GNN 直接预测分子动力学轨迹的位置与动量跨步演化，实现比传统 MD 积分器大 1–2 个数量级的时间步长跨越，并在架构中融入哈密顿动力学约束，推广到任意热力学系综和通用化学体系。

**[Flatness is Necessary, Neural Collapse is Not: Rethinking Generalization via Grokking](others/flatness_is_necessary_neural_collapse_is_not_rethinking_generalization_via_grokk.md)**

:   利用 grokking（延迟泛化）作为因果探针，证明 **relative flatness 是泛化的（潜在）必要条件**，而 neural collapse 虽常伴随泛化出现，但并非必要——它只是通往 flatness 的一条路径。

**[FlowMoE: 分布式MoE训练的可扩展流水线调度框架](others/flowmoe_a_scalable_pipeline_scheduling_framework_for_distributed_mixture-of-expe.md)**

:   通过统一的流水线调度和优先级驱动的all-reduce张量分块，实现MHA、门控、专家计算和A2A/all-reduce通信的完全重叠，训练时间减少13-57%。

**[Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards](others/fostering_the_ecosystem_of_ai_for_social_impact_requires_expanding_and_strengthe.md)**

:   本文主张 AI for Social Impact (AISI) 领域的学术生态需要双轨改革：拓宽"影响力"的定义以认可非部署/非方法创新的贡献，同时对已部署系统采用因果推断级别的严格评估标准。

**[FSNet: Feasibility-Seeking Neural Network for Constrained Optimization with Guarantees](others/fsnet_feasibility-seeking_neural_network_for_constrained_optimization_with_guara.md)**

:   提出 FSNet 框架，将**可微的可行性求解步骤**集成到神经网络中，通过最小化约束违反的无约束优化来保证约束满足，同时支持端到端训练，在凸/非凸、光滑/非光滑问题上均显著快于传统求解器且保持可行性。

**[Gaussian Process Upper Confidence Bound Achieves Nearly-Optimal Regret in Noise-Free Gaussian Process Bandits](others/gaussian_process_upper_confidence_bound_achieves_nearly-optimal_regret_in_noise-.md)**

:   本文证明 GP-UCB 在 noise-free GP bandit 问题中可达到 nearly-optimal regret，首次在 SE 核下实现 $O(1)$ 常数累积遗憾、在 Matérn 核（$d < \nu$）下实现 $O(1)$ 累积遗憾，弥合了 GP-UCB 理论与实践之间的长期差距。

**[Generalized Linear Mode Connectivity for Transformers](others/generalized_linear_mode_connectivity_for_transformers.md)**

:   提出统一对称性框架（置换、半置换、正交、可逆变换四级层次），首次在 Vision Transformer 和 GPT-2 上实现零/近零 barrier 的线性模式连通性（LMC），并扩展至多模型融合与异构宽度对齐。

**[Geometric Priors for Generalizable World Models via Vector Symbolic Architecture](others/geometric_priors_for_generalizable_world_models_via_vector_symbolic_architecture.md)**

:   提出将 Vector Symbolic Architecture (VSA) 中的 Fourier Holographic Reduced Representation (FHRR) 作为几何先验引入世界模型，通过 element-wise 复数乘法建模状态转移，在离散 GridWorld 上实现 87.5% 的 zero-shot 泛化准确率和 4 倍于 MLP 的噪声鲁棒性。

**[Gradient-Weight Alignment as a Train-Time Proxy for Generalization in Classification Tasks](others/gradient-weight_alignment_as_a_train-time_proxy_for_generalization_in_classifica.md)**

:   提出 Gradient-Weight Alignment (GWA)，通过量化每个训练样本梯度与模型权重的方向一致性（cosine similarity），在训练过程中无需验证集即可准确预测泛化性能、确定最佳早停时机，并定位有影响力的训练样本。

**[Graph Alignment via Birkhoff Relaxation](others/graph_alignment_via_birkhoff_relaxation.md)**

:   本文首次为图对齐问题的 Birkhoff 松弛（将排列矩阵约束松弛为双随机矩阵约束）提供了理论保证，在高斯 Wigner 模型下证明了最优解的相变行为：当噪声 $\sigma = o(n^{-1})$ 时松弛解接近真实排列，当 $\sigma = \Omega(n^{-0.5})$ 时松弛解远离真实排列。

**[Harnessing Feature Resonance under Arbitrary Target Alignment for Out-of-Distribution Node Detection](others/harnessing_feature_resonance_under_arbitrary_target_alignment_for_out-of-distrib.md)**

:   发现 Feature Resonance 现象——优化已知 ID 节点表征时未知 ID 节点的表征变化显著大于 OOD 节点，且该现象与标签无关，据此提出无需多类标签的图 OOD 节点检测框架 RSL，在 13 个数据集上达到 SOTA。

**[Improving Forecasts of Suicide Attempts for Patients with Little Data](others/improving_forecasts_of_suicide_attempts_for_patients_with_little_data.md)**

:   提出 Latent Similarity Gaussian Process (LSGP)，将患者嵌入连续隐空间以捕获异质性，使数据稀少的患者能从相似患者"借用"预测趋势，从而改进基于 EMA 数据的自杀未遂预测。

**[笔记2：PRM必要吗？RL隐式诱导PRM能力](others/is_prm_necessary_problem-solving_rl_implicitly_induces_prm_capability_in_llms.md)**

:   令人惊讶地，纯RL训练无需显式PRM监督即可诱发出强大的过程理解能力，且现有PRMs在SOTA模型上甚至不如简单多数投票有效。

**[Learning Dynamics of RNNs in Closed-Loop Environments](others/learning_dynamics_of_rnns_in_closed-loop_environments.md)**

:   从数学理论上揭示了 RNN 在闭环（agent-环境交互）与开环（监督学习）训练下呈现根本不同的学习动力学，闭环学习遵循三阶段过程，由短期策略改进与长期稳定性之间的竞争驱动。

**[Learning Generalizable Shape Completion with SIM(3) Equivariance](others/learning_generalizable_shape_completion_with_sim3_equivariance.md)**

:   提出首个 SIM(3) 等变形状补全网络 SIMECO，通过特征规范化→相似不变几何推理→变换恢复的三阶段模块设计，在去偏评估协议下超越所有增广和等变基线，KITTI 上 MMD 降低 17%、OmniObject3D 上 CD-$\ell_1$ 降低 14%，且在更严格协议下仍优于竞争者在其偏向性设置下的表现。

**[Learning non-equilibrium diffusions with Schrödinger bridges: from exactly solvable to simulation-free](others/learning_non-equilibrium_diffusions_with_schrödinger_bridges_from_exactly_solvab.md)**

:   将Schrödinger桥问题从布朗运动参考过程推广到多变量Ornstein-Uhlenbeck（mvOU）参考过程，推导高斯情形精确解，并提出无模拟的mvOU-OTFM算法处理一般分布。

**[Look-Ahead Reasoning on Learning Platforms](others/look-ahead_reasoning_on_learning_platforms.md)**

:   在学习平台的用户-算法交互中形式化 level-$k$ 前瞻推理，证明个体自私的高阶推理只加速收敛但不改变均衡（无长期收益），而集体协调的收益由学习者-用户效用函数的对齐程度决定，提供了刻画协调收益上界的理论框架。

**[MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision](others/maszero_designing_multiagent_systems_with_zero_supervision.md)**

:   MAS-ZERO 是首个推理时自动 MAS 设计框架，通过 meta-agent 迭代设计、批评和改进 MAS 配置（包括任务分解和 sub-MAS 分配），无需验证集和训练，在推理（+16.69%）、编程（+16.66%）和搜索代理（+5.45%）任务上均超越手动和自动 MAS baseline，同时保持 Pareto 最优的准确率-成本权衡。

**[MoESD: 揭示稀疏MoE推理中投机解码的潜力](others/moesd_unveil_speculative_decodings_potential_for_accelerating_sparse_moe.md)**

:   揭示投机解码在中等批大小下对MoE比对稠密模型更有效，通过目标效率指标捕捉系统级瓶颈，建立可靠的性能建模，达到2.29×加速。

**[Neural Collapse under Gradient Flow on Shallow ReLU Networks for Orthogonally Separable Data](others/neural_collapse_under_gradient_flow_on_shallow_relu_networks_for_orthogonally_se.md)**

:   首次证明在正交可分数据上，两层ReLU网络的梯度流（GF）在小初始化下可证收敛到Neural Collapse（NC）解，揭示了GF隐式偏置（早期神经元对齐+渐近最大间隔偏置）在促进NC出现中的关键作用。

**[On the Surprising Effectiveness of Large Learning Rates under Standard Width Scaling](others/on_the_surprising_effectiveness_of_large_learning_rates_under_standard_width_sca.md)**

:   揭示在标准参数化(SP)下，cross-entropy 损失函数使得"不稳定"区间实际分为灾难性不稳定和受控发散两个子区间：在受控发散区间（学习率 $\eta_n = \Theta(n^{-1/2})$）logits 发散但梯度和激活保持稳定，从而首次为 SP 提供了一个实用的、具有特征学习能力的无穷宽极限。

**[OrbitZoo: Real Orbital Systems Challenges for RL](others/orbitzoo_real_orbital_systems_challenges_for_reinforcement_learning.md)**

:   构建OrbitZoo，基于工业标准库Orekit的多智能体RL环境，支持碰撞规避和协同机动，经Starlink真实数据验证MAPE仅0.16%。

**[OrthoLoC: UAV 6-DoF Localization Using Orthographic Geodata](others/ortholoc_uav_6-dof_localization_and_calibration_using_orthographic_geodata.md)**

:   提出OrthoLoC——首个大规模UAV-正射影像配对数据集（16,425张，47地点，19城市），用于6-DoF定位和标定评估，AdHoP技术匹配精度提升95%、平移误差降低63%。

**[笔记7：价值引导搜索 - 高效链式思考推理](others/polymath_evaluating_mathematical_reasoning_in_multilingual_contexts.md)**

:   提出Value-Guided Search(VGS)——通过token级价值模型指导块级束搜索，无需预定义"步骤"，相对多数投票在竞赛数学上准确度提升+14.5%，同时推理计算效率提升30%，超越现有PRM方案。

**[笔记5：ReSearch - 学习通过搜索推理](others/research_learning_to_reason_with_search_for_llms_via_reinforcement_learning.md)**

:   ReSearch框架将搜索操作嵌入推理链中作为第一类原语，通过GRPO强化学习自动学习何时何如搜索，无需任何推理步骤的监督标注，在多跳QA任务上相对基线平均提升15.81%。

**[Sample-Adaptivity Tradeoff in On-Demand Sampling](others/sample-adaptivity_tradeoff_in_on-demand_sampling.md)**

:   系统研究了按需采样（on-demand sampling）中样本复杂度与自适应轮次之间的权衡关系，在可实现设定下证明 $r$ 轮算法的最优样本复杂度为 $dk^{\Theta(1/r)}/\varepsilon$，在不可知设定下提出仅需 $\widetilde{O}(\sqrt{k})$ 轮即可达近最优样本复杂度的LazyHedge算法，并引入OODS抽象框架建立了近紧的轮次复杂度下界。

**[Transfer Learning for Benign Overfitting in High-Dimensional Linear Regression](others/transfer_learning_for_benign_overfitting_in_high-dimensional_linear_regression.md)**

:   提出两步式Transfer MNI方法，在高维过参数化线性回归中通过"保留目标信号+零空间迁移源知识"机制增强良性过拟合的泛化能力，刻画了模型偏移和协变量偏移下的非渐近excess risk，并发现了"免费午餐"协变量偏移区间。

**[笔记4：WebThinker - 赋予推理模型深度研究能力](others/webthinker_empowering_large_reasoning_models_with_deep_research_capability.md)**

:   WebThinker赋予大型推理模型(LRM)自主的网络搜索与导航能力，通过Think-Search-Draft策略实现推理、信息采集与报告生成的无缝交织，经RL优化后在复杂推理与科学报告生成任务上超越o1与Gemini。
