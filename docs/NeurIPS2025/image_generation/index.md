<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**🧠 NeurIPS2025** · 共 **136** 篇

**[70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float (DFloat11)](70_size_100_accuracy_lossless_llm_compression_for_efficient.md)**

:   DFloat11 利用 BFloat16 权重中指数位（exponent）的低熵特性，通过 Huffman 编码将 LLM/扩散模型无损压缩至原始大小的约 70%（等效 ~11 bit），并设计了层次化查找表和两阶段 GPU kernel 实现高效在线解压，使 Llama 3.1 405B 可在单节点 8×80GB GPU 上无损推理。

**[A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](a_closer_look_at_model_collapse_from_a_generalization-to-memorization_perspectiv.md)**

:   发现扩散模型在自消耗循环（用生成数据训练下一代模型）中存在从"泛化"到"记忆"的转变过程，揭示训练集熵与模型泛化能力的强线性相关性（Pearson r=0.91），并提出基于熵的数据选择策略（Greedy Selection / Threshold Decay Filter）有效减缓该转变，在 CIFAR-10 accumulate 范式下第 8 轮 FID 从 75.7 降至 44.7。

**[A Connection Between Score Matching and Local Intrinsic Dimension](a_connection_between_score_matching_and_local_intrinsic_dimension.md)**

:   证明去噪得分匹配损失（denoising score matching loss）的下界恰好是数据流形的局部固有维度（LID），从而将 DSM loss 本身作为一个高效的 LID 估计器——无需梯度计算或多次前向传播，在 Stable Diffusion 3.5 上内存占用仅为 FLIPD 的 60%，且量化后估计更稳定。

**[A Data-Driven Prism: Multi-View Source Separation with Diffusion Model Priors](a_data-driven_prism_multi-view_source_separation_with_diffusion_model_priors.md)**

:   提出 DDPRISM 方法，利用多视图观测中不同线性变换的结构性差异，在 EM 框架下为每个未知源学习独立的扩散模型先验，无需预先获得任何单独的源样本即可完成源分离和后验采样，在合成问题和真实星系观测上超越现有方法。

**[A Diffusion Model for Regular Time Series Generation from Irregular Data with Completion and Masking](a_diffusion_model_for_regular_time_series_generation_from_irregular_data_with_co.md)**

:   提出两步框架从不规则采样时序数据生成规则时序：先用 TST 自编码器补全缺失值构造"自然邻域"，再在视觉扩散模型中用 masking 策略仅在观测像素上计算损失，避免对补全值的过度依赖，在判别分数上平均改善 70%，训练速度提升 6.5 倍。

**[A Gradient Flow Approach to Solving Inverse Problems with Latent Diffusion Models](a_gradient_flow_approach_to_solving_inverse_problems_with_latent_diffusion_model.md)**

:   提出 DWGF（Diffusion-regularized Wasserstein Gradient Flow），将隐空间扩散模型的后验采样问题严格形式化为 KL 散度在 Wasserstein-2 空间上的正则化梯度流，推导出隐空间中的 ODE 系统用于求解图像逆问题，在 FFHQ-512 上的修复和超分辨率任务中 PSNR 大幅超越基线。

**[Accelerating Parallel Diffusion Model Serving with Residual Compression](accelerating_parallel_diffusion_model_serving_with_residual_compression.md)**

:   提出 CompactFusion 框架，通过残差压缩（仅传输相邻去噪步骤间的激活差异而非完整激活）来消除并行扩散推理中的通信冗余，在 4×L20 上实现 3.0× 加速且生成质量远优于 DistriFusion，在模拟以太网带宽下实现 6.7× 加速，甚至在 100× 压缩下仍优于 DistriFusion。

**[AccuQuant: Simulating Multiple Denoising Steps for Quantizing Diffusion Models](accuquant_simulating_multiple_denoising_steps_for_quantizing.md)**

:   提出AccuQuant，一种用于扩散模型的训练后量化（PTQ）方法，通过在校准过程中显式模拟多个去噪步骤来最小化量化误差的累积效应，并通过新型目标函数将内存复杂度从O(n)降至O(1)。

**[Adapting Speech Language Model to Singing Voice Synthesis](adapting_speech_language_model_to_singing_voice_synthesis.md)**

:   将 1.7B 参数的 TTS 预训练 Speech Language Model 适配到歌声合成（SVS）任务，通过乐谱 tokenization + multi-stream LM 预测 + conditional flow matching 精修 + vocoder，仅用 135 小时合成歌声数据达到与专用 SVS 系统可比的性能。

**[ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering](alebench_a_benchmark_for_longhorizon_objectivedriven_algorit.md)**

:   提出 ALE-Bench，首个面向分数制算法工程竞赛（AtCoder Heuristic Contest）的 AI 基准，评估 LLM 和 Agent 在 NP-hard 优化问题上的长时间迭代改进能力，发现当前最强模型（o3-high）仅达人类平均水平，且在问题一致性和长时间改进方面与人类专家差距显著。

**[Aligning Compound AI Systems via System-level DPO](aligning_compound_ai_systems_via_system-level_dpo.md)**

:   将复合 AI 系统建模为 DAG，提出 SysDPO 框架将 DPO 扩展到多组件联合对齐，通过 DAG 分解将系统级偏好转化为可端到端优化的损失函数，理论证明了 β-完美对齐保证，在 LLM+扩散模型和 LLM+LLM 系统上显著提升协作质量。

**[Aligning Text to Image in Diffusion Models is Easier Than You Think](aligning_text_to_image_in_diffusion_models_is_easier_than_you_think.md)**

:   提出 SoftREPA——一种轻量级对比微调策略，通过引入可学习 soft text token（不到 1M 参数）在冻结的预训练 T2I 扩散模型上进行对比学习，显式提高文本和图像表征的互信息，在 SD1.5/SDXL/SD3 上显著提升文本-图像对齐质量，且适用于图像生成和图像编辑任务。

**[Amortized Sampling with Transferable Normalizing Flows](amortized_sampling_with_transferable_normalizing_flows.md)**

:   提出 Prose——一个 285M 参数的全原子可迁移归一化流，基于 TarFlow 架构训练在 21,700 个短肽 MD 轨迹上（总计 4.3ms 模拟时长），实现对任意短肽系统的零样本无相关性提议采样，在能量评估预算相同时超越 MD 基线，生成速度比之前的可迁移玻尔兹曼生成器 (TBG) 快 4000 倍。

**[AugGen: Synthetic Augmentation using Diffusion Models Can Improve Recognition](auggen_synthetic_augmentation_using_diffusion_models_can_imp.md)**

:   提出AugGen——一种自包含（self-contained）的合成数据增强方法：利用扩散模型的条件向量插值（$c^* = \alpha c_i + \beta c_j$）实现类间混合生成，无需外部数据或模型即可为人脸识别提供1-12%的性能提升，等效于1.7倍真实数据量，IR50+AugGen甚至超越IR101 real-only。

**[Autoregressive Adversarial Post-Training for Real-Time Interactive Video Generation](autoregressive_adversarial_posttraining_for_realtime_interac.md)**

:   提出 AAPT（Autoregressive Adversarial Post-Training），将预训练的潜在视频扩散模型转化为实时交互式视频生成器——每帧仅需单次神经网络前向传播（1NFE），自回归逐帧生成，8B 模型在单张 H100 上以 24fps 流式生成 736×416 视频，最长可达一分钟（1440帧）。

**[BADiff: Bandwidth Adaptive Diffusion Model](badiff_bandwidth_adaptive_diffusion_model.md)**

:   提出 BADiff——首个带宽自适应扩散模型，通过将目标熵约束作为条件嵌入扩散反向过程，配合可微熵正则化损失和自适应停止策略，使模型根据实时带宽动态调整生成质量并自适应提前终止采样，在保持感知质量的同时减少计算开销，从根本上避免了传统"高质量生成→后压缩"流程中的压缩伪影和计算浪费。

**[Balanced Conic Rectified Flow](balanced_conic_rectified_flow.md)**

:   针对 k-rectified flow 中 reflow 步骤导致的分布漂移问题，提出 conic reflow：利用真实图像的反演噪声及其 Slerp 扰动构成锥形监督轨迹，大幅减少所需 fake pair 数量的同时获得更优的生成质量和更直的 ODE 路径。

**[Beyond Masked and Unmasked: Discrete Diffusion Models via Partial Masking](beyond_masked_and_unmasked_discrete_diffusion_models_via_par.md)**

:   提出 Prime（Partial masking scheme），突破 Masked Diffusion Model 的二元状态（mask/unmask）限制，引入中间态（部分观测的 token 信息），减少冗余计算并实现更细粒度的去噪过程，在文本生成上 PPL 15.36 超越自回归模型（17.54）和标准 MDM（21.52），在图像生成上取得 CIFAR-10 FID 3.26。

**[BitMark: Watermarking Bitwise Autoregressive Image Generative Models](bitmark_watermarking_bitwise_autoregressive_image_generative_models.md)**

:   提出 BitMark——首个针对比特级自回归图像生成模型（Infinity、Instella）的水印方案，在生成过程中通过对 logit 加偏置将 bit 序列引向"绿色列表"，实现可靠检测（z-test）、高图像保真度（FID 几乎不变）、对多种攻击的鲁棒性和放射性（训练在水印图上的下游模型也带有水印），为防止模型坍缩提供了关键工具。

**[Blameless Users in a Clean Room: Defining Copyright Protection for Generative Models](blameless_users_in_a_clean_room_defining_copyright_protection_for_generative_mod.md)**

:   重建生成模型可证明版权保护的理论基础——证明现有的 Near Access-Freeness (NAF) 定义不能防止逐字复制（"被污染"），提出"无辜用户"(blameless) 框架和净室版权保护 ($(\kappa,\beta)$-clean) 定义，其中用户在反事实"净室设置"中不会复制则在真实世界中也不太可能复制，并证明差分隐私训练在"黄金数据集"假设下蕴含净室版权保护。

**[Blind Strong Gravitational Lensing Inversion: Joint Inference of Source and Lens Mass with Score-Based Models](blind_strong_gravitational_lensing_inversion_joint_inference_of_source_and_lens_.md)**

:   首次将 score-based 生成模型先验应用于强引力透镜的盲反演——联合推断背景源天体形态和透镜质量分布参数，通过将 GibbsDDRM 扩展到连续时间域实现采样，重建残差与观测噪声一致，透镜参数边际后验无系统偏差。

**[BlurDM: A Blur Diffusion Model for Image Deblurring](blurdm_a_blur_diffusion_model_for_image_deblurring.md)**

:   提出 BlurDM，将运动模糊的物理形成过程（连续曝光导致渐进模糊累积）集成到扩散模型——双扩散前向（同时加噪声+模糊）+ 双去噪去模糊反向，作为隐空间先验生成器一致性增强 4 种去模糊方法在 4 个数据集上的效果，GoPro 平均 +0.31 dB，RealBlur-J 平均 +0.78 dB，仅增加 ~4 GFLOPs 和 ~9ms。

**[BlurGuard: A Simple Approach for Robustifying Image Protection Against AI-Powered Edit](blurguard_a_simple_approach_for_robustifying_image_protection_against_ai-powered.md)**

:   提出 BlurGuard——在生成对抗扰动之前先对图像做轻度模糊预处理，使扰动更鲁棒地抵御 JPEG 压缩、高斯噪声等后处理操作，从而更有效地保护图像不被 Stable Diffusion 等 AI 编辑工具篡改，在保护成功率上比不模糊基线提升 20%+。

**[BoltzNCE: Learning Likelihoods for Boltzmann Generation with Stochastic Interpolants](boltznce_learning_likelihoods_for_boltzmann_generation_with_stochastic_interpola.md)**

:   BoltzNCE 用 Score Matching + InfoNCE 混合训练 Energy-Based Model 来近似 Boltzmann Generator 的似然，避免了昂贵的 Jacobian trace 计算，在丙氨酸二肽构象生成上实现 100× 推理加速且自由能误差仅 0.02 $k_BT$。

**[Boosting Generative Image Modeling via Joint Image-Feature Synthesis](boosting_generative_image_modeling_via_joint_imagefeature_sy.md)**

:   提出 Latent-Semantic Diffusion，让扩散模型联合生成 VAE 低级图像 latent 和 DINO 高级语义特征，通过最小修改标准 DiT 实现生成质量和训练效率的显著提升，并解锁 Representation Guidance 推理策略。

**[Breaking AR's Sampling Bottleneck: Provable Acceleration via Diffusion Language Models](breaking_ars_sampling_bottleneck_provable_acceleration_via_d.md)**

:   从信息论角度为扩散语言模型建立收敛保证，证明采样误差（KL散度）随迭代次数T成反比衰减且与token间互信息线性相关，关键证明了T<L（迭代次数可少于序列长度L）时仍可生成高质量样本，从理论上打破了自回归模型需要L步的基本采样瓶颈，并建立了匹配的上下界证明分析的紧致性。

**[CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop](cadmorph_geometry-driven_parametric_cad_editing_via_a_plan-generate-verify_loop.md)**

:   提出 CADMorph，一个迭代式 plan–generate–verify 框架，利用预训练的 Parameter-to-Shape (P2S) 扩散模型和 Masked-Parameter-Prediction (MPP) 大语言模型协同工作，在无需三元组训练数据的情况下实现几何驱动的参数化 CAD 编辑。

**[CAMILA: Context-Aware Masking for Image Editing with Language Alignment](camila_contextaware_masking_for_image_editing_with_language.md)**

:   提出 CAMILA，一种上下文感知的图像编辑方法，能够判断用户指令是否在当前图像上下文中可行，仅执行可行的编辑指令而忽略不可执行的指令，在单指令和多指令编辑场景中均优于现有方法。

**[CaMiT: A Time-Aware Car Model Dataset for Classification and Generation](camit_a_time-aware_car_model_dataset_for_classification_and_generation.md)**

:   提出 CaMiT 数据集（787K 标注 + 5.1M 无标注汽车图像，2005–2023），系统研究细粒度视觉类别的时间漂移问题，并在静态预训练、时间增量预训练、时间增量分类器学习和时间感知图像生成四个场景下提供 benchmark。

**[Can Knowledge-Graph-based Retrieval Augmented Generation Really Retrieve What You Need?](can_knowledge-graph-based_retrieval_augmented_generation_really_retrieve_what_yo.md)**

:   提出 GraphFlow 框架，将知识图谱上的检索建模为 GFlowNet 的流匹配问题，通过详细平衡目标和局部探索策略联合训练检索策略与流估计器，在 STaRK 基准上检索准确率和多样性均超越 GPT-4o 约 10%。

**[CDFlow: Building Invertible Layers with Circulant and Diagonal Matrices](cdflow_building_invertible_layers_with_circulant_and_diagonal_matrices.md)**

:   提出 CDFlow，利用循环矩阵和对角矩阵的交替乘积构造可逆线性层，将参数复杂度从 $\mathcal{O}(n^2)$ 降至 $\mathcal{O}(mn)$，矩阵逆复杂度从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(mn\log n)$，对数行列式从 $\mathcal{O}(n^3)$ 降至 $\mathcal{O}(mn)$，在密度估计和周期性数据建模上超越同类方法。

**[Composite Flow Matching for Reinforcement Learning with Shifted-Dynamics Data](composite_flow_matching_for_reinforcement_learning_with_shifted-dynamics_data.md)**

:   提出 CompFlow，通过复合流匹配架构（在离线流输出分布上构建在线流）估计离线-在线环境间的动态差异（Wasserstein 距离），并结合高动态差异区域的主动探索策略，在 27 个动态偏移 RL 任务中平均回报超越最强基线 14.2%。

**[Composition and Alignment of Diffusion Models using Constrained Learning](composition_and_alignment_of_diffusion_models_using_constrai.md)**

:   提出统一的约束学习框架来处理扩散模型的对齐（alignment）和组合（composition），将多奖励对齐形式化为 KL 散度最小化+奖励约束，将模型组合形式化为 minimax KL 散度问题，通过拉格朗日对偶的原-对偶训练算法求解，相比传统加权方法更可解释且避免了手动调权。

**[Conditional Panoramic Image Generation via Masked Autoregressive Modeling](conditional_panoramic_image_generation_via_masked_autoregres.md)**

:   提出PAR（Panoramic AutoRegressive model），首次用掩码自回归建模统一文本到全景图和全景图外延两大任务，通过循环平移一致性损失和双空间循环填充解决ERP全景图的边界不连续问题，在Matterport3D上取得37.37 FID，同时展示出良好的可扩展性和零样本泛化能力。

**[Constrained Discrete Diffusion](constrained_discrete_diffusion.md)**

:   提出 CDD（Constrained Discrete Diffusion），将可微约束优化投影算子嵌入离散扩散模型的去噪过程中，无需重训练即可在采样时强制满足序列级约束，在毒性文本生成、分子设计和指令遵循三类任务上实现零约束违反。

**[Contextual Thompson Sampling via Generation of Missing Data](contextual_thompson_sampling_via_generation_of_missing_data.md)**

:   提出 Generative Thompson Sampling (TS-Gen)，将上下文老虎机中的不确定性建模为缺失数据而非未知参数，通过生成模型对缺失结果做自回归填充来实现 Thompson 采样，建立了与离线预测损失直接挂钩的遗憾界。

**[Continuous Diffusion Model for Language Modeling](continuous_diffusion_model_for_language_modeling.md)**

:   提出一种面向离散语言建模的连续扩散框架，将离散扩散过程与统计流形上的连续流联系起来，并通过径向对称的 simulation-free 训练机制与降维技巧，显著提升扩散语言模型性能，接近自回归模型。

**[Continuous Uniqueness and Novelty Metrics for Generative Modeling of Inorganic Crystals](continuous_uniqueness_and_novelty_metrics_for_generative_modeling_of_inorganic_c.md)**

:   针对无机晶体生成模型评估中广泛使用的离散距离函数 (StructureMatcher) 的四大缺陷，提出基于 Magpie 指纹（成分）和 AMD 向量（结构）的连续距离函数，实现更可靠的 uniqueness 和 novelty 度量。

**[CORAL: Disentangling Latent Representations in Long-Tailed Diffusion](coral_disentangling_latent_representations_in_longtailed_dif.md)**

:   论文系统分析长尾数据下扩散模型尾部类别生成质量下降的根因，指出 U-Net 瓶颈潜表示发生“头类-尾类子空间重叠”导致特征借用，并提出 CORAL 对比式潜空间对齐正则，显著提升尾类样本的多样性与视觉质量。

**[Co-Reinforcement Learning for Unified Multimodal Understanding and Generation](coreinforcement_learning_for_unified_multimodal_understandin.md)**

:   提出CoRL框架——通过"统一RL→精细RL"两阶段GRPO训练策略，在不依赖额外监督数据的情况下，让统一多模态模型(ULM)的理解和生成能力协同进化，在Janus-Pro-1.5B上取得生成+7%、理解+23%的平均提升。

**[Counterfactual Identifiability via Dynamic Optimal Transport](counterfactual_identifiability_via_dynamic_optimal_transport.md)**

:   利用动态最优传输 (dynamic OT) 理论，首次解决了高维多变量 Markovian SCM 中反事实的可辨识性问题——证明 OT flow 机制产生唯一的单调保序反事实传输映射，并扩展至非 Markovian 设置（IV/BC/FC 准则）。

**[Coupling Generative Modeling and an Autoencoder with the Causal Bridge](coupling_generative_modeling_and_an_autoencoder_with_the_causal_bridge.md)**

:   在存在未观测混淆因子的因果推断中，提出将生成模型与自编码器耦合来提升因果桥函数 (causal bridge) 的估计质量——通过共享编码器在处理/控制/结果变量间传递统计强度，并将框架扩展到生存分析。

**[Cross-fluctuation Phase Transitions Reveal Sampling Dynamics in Diffusion Models](cross-fluctuation_phase_transitions_reveal_sampling_dynamics_in_diffusion_models.md)**

:   借鉴统计物理中的涨落理论（fluctuation theory），提出了一种通过 **交叉涨落（cross-fluctuation）** 检测扩散模型采样过程中离散相变的框架，从而在无需重新训练的情况下加速采样、改进条件生成、提升零样本分类和风格迁移。

**[Decomate: Leveraging Generative Models for Co-Creative SVG Animation](decomate_leveraging_generative_models_for_co-creative_svg_animation.md)**

:   提出 Decomate 交互系统，利用多模态大语言模型 (MLLM) 将非结构化 SVG 图形自动分解为语义组件，设计师通过自然语言为各组件指定动画行为，系统生成可生产的 HTML/CSS/JS 动画代码，支持迭代协作创作。

**[DEFT: Decompositional Efficient Fine-Tuning for Text-to-Image Models](deft_decompositional_efficient_finetuning_for_texttoimage_mo.md)**

:   提出DEFT——将权重更新分解为两个可训练矩阵的组合：(1)低秩子空间的正交投影和(2)子空间内的低秩调整，相比LoRA在T2I个性化中CLIP-T从0.341提升到0.361（DreamBench+），在统一模型上实现风格迁移和条件生成的SOTA。

**[Denoising Weak Lensing Mass Maps with Diffusion Model and Generative Adversarial Network](denoising_weak_lensing_mass_maps_with_diffusion_model_and_generative_adversarial.md)**

:   将扩散模型（DM）应用于弱引力透镜质量图去噪任务，与 GAN（pix2pix）在相同实验设置下进行系统性对比，证明 DM 在训练稳定性、多样本平均鲁棒性和多种统计量重建精度上全面优于 GAN。

**[Detecting Generated Images by Fitting Natural Image Distributions](detecting_generated_images_by_fitting_natural_image_distributions.md)**

:   提出一致性验证框架 ConV，利用自然图像流形与生成图像之间的几何差异，通过两个梯度正交的函数实现无需训练的生成图像检测，并引入 Normalizing Flow 增强版 F-ConV 进一步放大流形偏差。

**[Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model](detection_and_simulation_of_urban_heat_islands_using_a_fine-tuned_geospatial_fou.md)**

:   提出一套利用微调地理空间基础模型（Granite-GFM）的完整工作流，涵盖城市热岛效应的实证量化、未来气候情景下的温度外推预测，以及通过卫星图像 inpainting 模拟城市绿化降温效果。

**[DEXTER: Diffusion-Guided EXplanations with TExtual Reasoning for Vision Models](dexter_diffusion-guided_explanations_with_textual_reasoning_for_vision_models.md)**

:   提出 DEXTER，一个无需数据的框架，通过优化文本提示驱动扩散模型生成最大化目标分类器激活的图像，再用 LLM 对合成样本进行推理，生成全局性、可读的文本解释，实现模型行为的偏差发现和全局解释。

**[DiCo: Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling](dico_revitalizing_convnets_for_scalable_and_efficient_diffus.md)**

:   重新发掘卷积网络在扩散模型中的潜力——发现预训练DiT的全局自注意力主要捕获局部模式（冗余），提出用标准ConvNet模块+紧凑通道注意力构建纯卷积扩散模型DiCo，在ImageNet-256上以2.05 FID超越DiT-XL/2且速度快2.7倍。

**[Diff-ICMH: Harmonizing Machine and Human Vision in Image Compression with Generative Prior](diff-icmh_harmonizing_machine_and_human_vision_in_image_compression_with_generat.md)**

:   提出 Diff-ICMH，一种基于扩散模型的生成式图像压缩框架，通过语义一致性损失（SC loss）保持语义完整性，通过标签引导模块（TGM）激活生成先验，以单一编解码器和码流同时服务 10+ 种智能任务和人类视觉感知，无需任何任务特定适配。

**[DiffEye: Diffusion-Based Continuous Eye-Tracking Data Generation Conditioned on Natural Images](diffeye_diffusion-based_continuous_eye-tracking_data_generation_conditioned_on_n.md)**

:   提出 DiffEye，首个基于扩散模型直接利用原始眼动轨迹数据、以自然图像为条件生成连续且多样化眼动轨迹的框架，同时引入对应位置嵌入 (CPE) 对齐注视空间与图像语义空间。

**[Diffusion-Based Electromagnetic Inverse Design of Scattering Structured Media](diffusion-based_electromagnetic_inverse_design_of_scattering_structured_media.md)**

:   提出基于条件扩散模型的电磁逆设计框架，从目标微分散射截面 (DSCS) 直接生成介电球超表面几何结构，绕过昂贵的迭代优化，并自然处理逆问题的非唯一性，性能优于 CMA-ES 进化优化且速度快数个数量级。

**[Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation](diffusion-driven_progressive_target_manipulation_for_source-free_domain_adaptati.md)**

:   提出 DPTM 框架，利用潜在扩散模型对不可信目标样本进行语义变换，生成伪目标域并通过渐进式重建机制迭代缩小与真实目标域的差距，在大域偏移场景下比现有 SFDA SOTA 提升高达 18.6%。

**[Diffusion Adaptive Text Embedding for Text-to-Image Diffusion Models](diffusion_adaptive_text_embedding_for_texttoimage_diffusion.md)**

:   发现T2I扩散模型中固定的text embedding在不同时间步是次优的，提出DATE——在推理时动态更新text embedding以最大化mean predicted image与文本的对齐评分（如CLIP Score/ImageReward），无需训练，可即插即用到任何扩散模型和采样器中，在多概念生成和图像编辑中一致提升text-image对齐。

**[Diffusion Classifiers Understand Compositionality, but Conditions Apply](diffusion_classifiers_understand_compositionality_but_condit.md)**

:   全面研究零样本扩散分类器在组合理解任务上的判别能力：覆盖3个扩散模型(SD 1.5/2.0/3-m)×10个数据集×30+任务，引入Self-Bench诊断基准（用扩散模型自己生成的图像消除域差异），发现扩散分类器确实理解组合性但受域差距和时间步加权影响——"条件适用"。

**[Diffusion Generative Modeling on Lie Group Representations](diffusion_generative_modeling_on_lie_group_representations.md)**

:   提出在李群**表示空间**（而非李群本身）上构建扩散过程的新理论框架，通过广义分数匹配将非阿贝尔李群的弯曲动力学映射到欧几里得空间中，实现无模拟训练的李群扩散模型，并证明标准分数匹配是其平移群的特例。

**[Diffusion Models Meet Contextual Bandits](diffusion_models_meet_contextual_bandits.md)**

:   将预训练扩散模型作为上下文赌博机 (contextual bandits) 问题中动作参数的表达性先验，提出 diffusion Thompson Sampling (dTS) 算法，通过高效的层次化后验近似实现快速更新与采样，在大动作空间下显著优于传统方法。

**[Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation](distilled_decoding_2_onestep_sampling_of_image_autoregressiv.md)**

:   提出 Distilled Decoding 2 (DD2)，通过条件分数蒸馏损失将图像自回归模型压缩为单步生成器，在 ImageNet-256 上 FID 仅从 3.40 增至 5.43，比 DD1 的 one-step 差距缩小 67%，训练加速 12.3×。

**[DOVE: Efficient One-Step Diffusion Model for Real-World Video Super-Resolution](dove_efficient_one-step_diffusion_model_for_real-world_video_super-resolution.md)**

:   提出 DOVE，基于 CogVideoX 预训练视频生成模型，通过两阶段潜空间-像素空间训练策略和高质量 HQ-VSR 数据集实现单步推理的视频超分辨率，比多步扩散方法快 28 倍且性能相当或更优。

**[Dynamic Diffusion Schrödinger Bridge in Astrophysical Observational Inversions](dynamic_diffusion_schrödinger_bridge_in_astrophysical_observational_inversions.md)**

:   提出 Astro-DSB，一种基于 Diffusion Schrödinger Bridge 的天文物理反问题建模方法，直接学习观测量到真实物理分布的概率映射，训练成本仅为条件 DDPM 的 25%，且在分布外（OOD）测试中展现出显著的泛化优势，并成功应用于 Taurus B213 真实观测数据。

**[EditInfinity: Image Editing with Binary-Quantized Generative Models](editinfinity_image_editing_with_binary-quantized_generative_models.md)**

:   提出 EditInfinity，首次将经典"图像反演-图像编辑"范式应用于二值量化自回归生成模型 Infinity，利用量化表示可获取精确中间监督的优势实现高精度图像反演，配合分段线性平滑核实现高保真编辑效果，在 PIE-Bench 上全面超越扩散模型基线。

**[EEGReXferNet: A Lightweight Gen-AI Framework for EEG Subspace Reconstruction via Cross-Subject Transfer Learning and Channel-Aware Embedding](eegrexfernet_a_lightweight_gen-ai_framework_for_eeg_subspace_reconstruction_via_.md)**

:   提出 EEGReXferNet，一种轻量级生成式 AI 框架，通过邻域通道感知输入选择、频带特定子窗口卷积编解码、动态滑窗隐空间和参考统计量缩放，在跨被试迁移学习设置下实现 EEG 子空间重建，参数减少约 45%、推理延迟 <1ms，同时保持 PSD 相关性 $\geq 0.95$ 和谱图 RV 系数 $\geq 0.85$。

**[Efficient Rectified Flow for Image Fusion](efficient_rectified_flow_for_image_fusion.md)**

:   提出 RFfusion，首次将 Rectified Flow 引入图像融合任务，实现无需额外训练的单步采样，同时设计面向融合的两阶段 VAE 训练策略，在速度和质量上全面超越现有扩散融合方法。

**[Elucidated Rolling Diffusion Models for Probabilistic Forecasting of Complex Dynamics](elucidated_rolling_diffusion_models_for_probabilistic_forecasting_of_complex_dyn.md)**

:   提出 ERDM，首次将滚动扩散（Rolling Diffusion）框架与 EDM 的原则性设计（噪声调度、预条件化、Heun 采样器）成功统一，通过渐进噪声调度显式建模不确定性增长，在 Navier-Stokes 和 ERA5 天气预报任务上显著优于自回归 EDM 基线。

**[Emergence and Evolution of Interpretable Concepts in Diffusion Models](emergence_and_evolution_of_interpretable_concepts_in_diffusi.md)**

:   首次将 Sparse Autoencoders (SAEs) 系统性地应用于多步扩散模型 (Stable Diffusion v1.4)，揭示了图像构图在第一步反向扩散就已涌现、风格概念在中期阶段形成的时间演化规律，并据此设计了时间自适应的因果干预技术。

**[Encoder-Decoder Diffusion Language Models for Efficient Training and Inference](encoder-decoder_diffusion_language_models_for_efficient_training_and_inference.md)**

:   提出 E2D2，一种面向离散扩散语言模型的编码器-解码器架构，通过轻量解码器迭代去噪、大型编码器定期更新表征，同时实现更快推理（~3× vs MDLM）和更高效的 block diffusion 训练（FLOPs 减半）。

**[Energy Loss Functions for Physical Systems](energy_loss_functions_for_physical_systems.md)**

:   提出基于物理能量的损失函数框架，通过反向 KL 散度与玻尔兹曼分布推导出以成对距离为基础的能量差损失，天然满足 SE(d) 不变性，在分子生成和自旋基态预测中显著优于 MSE 和交叉熵损失。

**[Enhancing Diffusion Model Guidance through Calibration and Regularization](enhancing_diffusion_model_guidance_through_calibration_and_regularization.md)**

:   针对分类器引导扩散模型中分类器过度自信导致梯度消失的问题，提出两类互补方案：(1) Smooth ECE 校准损失微调分类器，FID 改善 ~3%；(2) 基于 f-散度的正则化采样引导（RKL/FKL/JS），无需重训练即在 ImageNet 128×128 上达到 FID 2.13。

**[Entropy Rectifying Guidance for Diffusion and Flow Models](entropy_rectifying_guidance_for_diffusion_and_flow_models.md)**

:   提出 Entropy Rectifying Guidance (ERG)，通过操控注意力层的 Hopfield 能量景观（温度缩放、步长调整）来获取弱预测信号，替代传统 CFG 中的无条件预测，在文本到图像、类条件和无条件生成中同时提升质量、多样性和一致性。

**[Epistemic Uncertainty for Generated Image Detection](epistemic_uncertainty_for_generated_image_detection.md)**

:   提出 WePe（Weight Perturbation），通过对预训练视觉大模型（DINOv2）施加权重扰动来估计认识不确定性（epistemic uncertainty），利用自然图像与 AI 生成图像在不确定性空间的差异实现检测，无需训练即可使用。

**[Equivariant Flow Matching for Symmetry-Breaking Bifurcation Problems](equivariant_flow_matching_for_symmetry-breaking_bifurcation_problems.md)**

:   提出等变 flow matching 框架，结合 symmetric coupling 策略，用生成式 AI 建模对称性破缺分岔问题中的多模态概率分布，在物理系统（屈曲梁、Allen-Cahn 方程）上显著优于确定性模型和 VAE。

**[Evaluating the Evaluators: Metrics for Compositional Text-to-Image Generation](evaluating_the_evaluators_metrics_for_compositional_text-to-image_generation.md)**

:   系统评估了 12 种文本-图像组合对齐指标与人类判断的一致性，发现没有单一指标在所有组合任务上一致表现最优，VQA 指标并非总是最好的，embedding 类指标（ImageReward、HPS）在特定类别上更强。

**[EVODiff: Entropy-aware Variance Optimized Diffusion Inference](evodiff_entropy-aware_variance_optimized_diffusion_inference.md)**

:   从信息论角度分析扩散模型推理过程，提出通过优化条件方差来减少条件熵的 EVODiff 方法，在不修改模型的前提下显著加速采样并提升生成质量。

**[Evolve to Inspire: Novelty Search for Diverse Image Generation](evolve_to_inspire_novelty_search_for_diverse_image_generation.md)**

:   提出 Wander 框架，基于新颖性搜索（novelty search）和 LLM 驱动的 prompt 进化，从单个文本提示出发生成高度多样化的图像集合，在 Vendi Score 上超越现有进化式 prompt 优化基线。

**[Exploring Semantic-constrained Adversarial Example with Instruction Uncertainty Reduction](exploring_semantic-constrained_adversarial_example_with_instruction_uncertainty_.md)**

:   提出多维度指令不确定性缩减框架 InSUR，通过 ResAdv-DDIM 采样器稳定对抗优化方向、上下文编码的攻击场景约束、以及基于 WordNet 的语义抽象评估，首次实现了从自然语言指令生成 2D/3D 语义约束对抗样本（SemanticAE）。

**[Exploring Variational Graph Autoencoders for Distribution Grid Data Generation](exploring_variational_graph_autoencoders_for_distribution_grid_data_generation.md)**

:   探索变分图自编码器（VGAE）生成合成配电网拓扑的能力，评估四种解码器架构在两个数据集上的表现，揭示 VGAE 在小型同质网络上效果良好但在大型异质网络上面临挑战。

**[FairImagen: Post-Processing for Bias Mitigation in Text-to-Image Models](fairimagen_post-processing_for_bias_mitigation_in_text-to-image_models.md)**

:   提出 FairImagen 后处理去偏框架，通过在 CLIP prompt 嵌入空间应用 FairPCA 投影去除人口统计信息，结合经验噪声注入和跨人口统计联合去偏，在不重训模型的前提下显著提升文本到图像生成的公平性。

**[FALCON: Few-step Accurate Likelihoods for Continuous Flows](falcon_few-step_accurate_likelihoods_for_continuous_flows.md)**

:   提出 FALCON，通过混合训练目标（flow matching + 平均速度损失 + 可逆性正则化）使连续归一化流在少步采样下仍能提供足够精确的似然估计，从而实现比传统 CNF 快两个数量级的 Boltzmann 采样。

**[Fast Data Attribution for Text-to-Image Models](fast_data_attribution_for_text-to-image_models.md)**

:   将慢而准确的 unlearning-based 数据归因方法蒸馏为一个可快速检索的特征嵌入空间，在 Stable Diffusion 级别模型上实现比现有方法快 2,500× ~ 400,000× 的数据归因。

**[Fast Solvers for Discrete Diffusion Models: Theory and Applications of High-Order Algorithms](fast_solvers_for_discrete_diffusion_models_theory_and_applications_of_high-order.md)**

:   为离散扩散模型推理首次提出高阶数值求解器（θ-RK-2 和 θ-Trapezoidal），在 KL 散度意义下证明二阶收敛，在文本和图像生成任务上以同等计算预算获得更好的样本质量。

**[FerretNet: Efficient Synthetic Image Detection via Local Pixel Dependencies](ferretnet_efficient_synthetic_image_detection_via_local_pixel_dependencies.md)**

:   基于 Markov Random Field 理论提出局部像素依赖（LPD）特征表示，结合仅 1.1M 参数的轻量 FerretNet 网络，仅在 4 类 ProGAN 数据上训练即在 22 个生成模型上达到 97.1% 平均准确率。

**[Flatten Graphs as Sequences: Transformers are Scalable Graph Generators](flatten_graphs_as_sequences_transformers_are_scalable_graph_generators.md)**

:   提出 AutoGraph，通过分段欧拉邻域路径（SENT）将图无损展平为 token 序列，直接用 decoder-only Transformer 建模，实现比扩散模型快 100× 的图生成速度，同时在合成和分子基准上达到 SOTA。

**[Flattening Hierarchies with Policy Bootstrapping](flattening_hierarchies_with_policy_bootstrapping.md)**

:   提出 Subgoal Advantage-Weighted Policy Bootstrapping（SAW），通过优势加权的重要性采样对子目标条件策略进行 bootstrapping，将层级 RL 的长距离推理能力蒸馏到一个扁平策略中，无需生成式子目标模型。

**[Flex-Judge: Text-Only Reasoning Unleashes Zero-Shot Multimodal Evaluators](flex-judge_text-only_reasoning_unleashes_zero-shot_multimodal_evaluators.md)**

:   提出 Flex-Judge，仅用 1K 条纯文本推理数据微调多模态大模型，即可零样本泛化到图像/视频/音频/分子等多模态评判任务，性能媲美甚至超越 GPT-4o 等商业 API 和大规模标注训练的专用评估器。

**[Flow Matching Neural Processes](flow_matching_neural_processes.md)**

:   提出 FlowNP，将 flow matching 引入神经过程框架，通过 transformer 预测目标点的流速度场实现对条件分布的并行采样，在 1D GP、图像和气象数据三大基准上全面超越现有 NP 方法。

**[FocalCodec: Low-Bitrate Speech Coding via Focal Modulation Networks](focalcodec_low-bitrate_speech_coding_via_focal_modulation_networks.md)**

:   提出 FocalCodec——基于 Focal Modulation 的低比特率语音编解码器，使用**单个二值码本**将语音压缩至 0.16–0.65 kbps，在语音重合成、语音转换和多项下游任务中达到与多码本 SOTA 方法可比甚至更优的性能。

**[FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency](freqpolicy_efficient_flow-based_visuomotor_policy_via_frequency_consistency.md)**

:   首次在 flow-based 视觉运动策略中引入频域一致性约束，利用 DCT 变换将动作块的速度场投影到频域并施加自适应频率分量损失，实现了高质量一步动作生成（93.5 Hz），在仿真和真实机器人任务中均优于现有一步生成方法。

**[From Cradle to Cane: A Two-Pass Framework for High-Fidelity Lifespan Face Aging](from_cradle_to_cane_a_two-pass_framework_for_high-fidelity_lifespan_face_aging.md)**

:   提出 Cradle2Cane 两阶段人脸老化框架：第一阶段通过自适应噪声注入（AdaNI）实现精准年龄控制，第二阶段通过 SVR-ArcFace 和 Rotate-CLIP 双身份嵌入（IDEmb）强化身份一致性，在全寿命跨度（0-80岁）人脸老化中实现年龄精度与身份保持的最优平衡。

**[GeneMAN: Generalizable Single-Image 3D Human Reconstruction from Multi-Source Human Data](geneman_generalizable_single-image_3d_human_reconstruction_from_multi-source_hum.md)**

:   GeneMAN 提出一种**无需人体参数模型(如 SMPL)**的通用单图 3D 人体重建框架，通过在大规模多源人体数据上训练人体专属的 2D/3D 扩散先验模型，结合几何初始化-雕刻流水线与多空间纹理精炼，实现了对野外图片中不同体型比例、复杂姿态与个人物品的高保真 3D 人体重建。

**[Generative Model Inversion Through the Lens of the Manifold Hypothesis](generative_model_inversion_through_the_lens_of_the_manifold_hypothesis.md)**

:   从流形几何视角揭示生成式模型逆向攻击 (MIA) 的本质是通过将损失梯度投影到生成器切空间实现隐式去噪，提出梯度-流形对齐假说（对齐越高→模型越脆弱）并设计无需训练的 AlignMI 方法在多个 SOTA 攻击上取得一致且显著的提升。

**[GenIR: Generative Visual Feedback for Mental Image Retrieval](genir_generative_visual_feedback_for_mental_image_retrieval.md)**

:   提出 GenIR，一种利用文本到图像扩散模型生成"合成视觉反馈"的多轮交互式图像检索框架，将系统对用户查询的理解显式可视化，使用户能直观地识别差异并迭代改进查询，在 Mental Image Retrieval (MIR) 任务上大幅超越纯文本反馈方法。

**[Georemover Removing Objects And Their Causal Visual Artifacts](georemover_removing_objects_and_their_causal_visual_artifacts.md)**

:   提出几何感知的两阶段框架 GeoRemover，将目标移除解耦为几何移除（深度域）与外观渲染（RGB域），通过修改场景几何表示来隐式消除被移除物体的阴影和反射等因果视觉伪影。

**[Gradient Variance Reveals Failure Modes in Flow-Based Generative Models](gradient_variance_reveals_failure_modes_in_flow-based_generative_models.md)**

:   本文通过分析 CFM 损失的梯度方差（gradient variance），揭示了 Rectified Flow 在确定性插值下会不可避免地记忆训练配对而非学习最优传输映射，并证明引入随机性（stochastic interpolant）可打破该记忆化通道、恢复泛化能力。

**[GraLoRA: Granular Low-Rank Adaptation for Parameter-Efficient Fine-Tuning](gralora_granular_low-rank_adaptation_for_parameter-efficient_fine-tuning.md)**

:   提出 GraLoRA——将 LoRA 的权重更新矩阵分割为 $k^2$ 个独立子块、每块配独立低秩适配器，在不增加参数量和计算量的前提下将有效秩从 $r$ 提升至 $kr$，解决 LoRA 在高秩下因梯度纠缠导致的性能退化问题，在代码生成上 Pass@1 最高提升 +8.5%。

**[Graph-based Neural Space Weather Forecasting](graph-based_neural_space_weather_forecasting.md)**

:   提出基于图神经网络的空间天气神经模拟器，在 Vlasiator 混合 Vlasov 模拟数据上训练，实现确定性和概率性自回归预测近地空间状态，速度比原始模拟快 100 倍以上，并通过隐变量生成集合预报来量化预测不确定性。

**[Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges](grasp2grasp_vision-based_dexterous_grasp_translation_via_schrödinger_bridges.md)**

:   提出将跨手形态的视觉灵巧抓取迁移建模为 Schrödinger Bridge 问题，通过在潜空间中学习得分与流匹配（[SF]²M），并设计物理感知的最优传输代价函数（位姿/接触图/力旋量空间/雅可比可操作性），在无需配对数据的条件下实现不同机械手之间抓取意图的分布级迁移。

**[GSPN-2: Efficient Parallel Sequence Modeling](gspn-2_efficient_parallel_sequence_modeling.md)**

:   GSPN-2 通过算法-系统联合重设计（单 kernel 融合、紧凑通道传播、共享内存优化），将 GSPN-1 的 2D 空间传播加速最高 40×，在 ImageNet 分类和文本到图像生成中达到 Transformer 级精度且计算成本显著更低。

**[Guided Diffusion Sampling on Function Spaces with Applications to PDEs](guided_diffusion_sampling_on_function_spaces_with_applications_to_pdes.md)**

:   提出 **FunDPS（Function-space Diffusion Posterior Sampling）**，在函数空间中训练无条件扩散模型，推理时通过梯度引导实现 plug-and-play 的 PDE 逆问题后验采样；理论上将 Tweedie 公式推广到无穷维 Banach 空间，实验上在 5 个 PDE 任务中仅用 3% 观测即可获得比 DiffusionPDE 平均高 32% 的精度并减少 4 倍采样步数。

**[GuideFlow3D: Optimization-Guided Rectified Flow For Appearance Transfer](guideflow3d_optimization-guided_rectified_flow_for_appearance_transfer.md)**

:   提出 GuideFlow3D，一种无需训练的 3D 外观迁移框架，通过在预训练 rectified flow 模型的采样过程中交替注入可微引导损失（部件感知外观损失 + 自相似性损失），实现几何差异显著的物体间鲁棒的纹理与几何细节迁移。

**[Head Pursuit: Probing Attention Specialization in Multimodal Transformers](head_pursuit_probing_attention_specialization_in_multimodal.md)**

:   用信号处理中的Simultaneous Orthogonal Matching Pursuit (SOMP)算法分解注意力头在unembedding矩阵上的稀疏表示，揭示注意力头的语义特化现象（如政治/国籍/月份/数字等），仅编辑1%的头即可可靠地抑制或增强特定概念——在语言和视觉-语言模型上均验证有效。

**[Hephaestus: Mixture Generative Modeling with Energy Guidance for Large-scale QoS Degradation](hephaestus_mixture_generative_modeling_with_energy_guidance_for_large-scale_qos_.md)**

:   提出 Hephaestus 三阶段生成框架（Forge-Morph-Refine），结合预测路径加压算法、能量引导的混合 CVAE 和潜在空间 RL 优化，用于大规模网络 QoS 降级问题的求解。

**[Hierarchical Koopman Diffusion: Fast Generation with Interpretable Diffusion Trajectory](hierarchical_koopman_diffusion_fast_generation_with_interpretable_diffusion_traj.md)**

:   基于 Koopman 算子理论，将扩散模型的非线性去噪动力学提升到线性 Koopman 空间，通过层次化分解实现一步采样，同时保留中间生成状态的可解释性和可控性。

**[High-order Equivariant Flow Matching for Density Functional Theory Hamiltonian Prediction](high-order_equivariant_flow_matching_for_density_functional_theory_hamiltonian_p.md)**

:   提出 QHFlow，首次将条件 flow matching 引入密度泛函理论（DFT）哈密顿矩阵预测任务，通过高阶 SE(3) 等变向量场和对称性感知先验分布，在 MD17 上将哈密顿预测误差降低 73%，并可作为 SCF 初始化加速 DFT 计算达 54%。

**[How to Build a Consistency Model: Learning Flow Maps via Self-Distillation](how_to_build_a_consistency_model_learning_flow_maps_via_self-distillation.md)**

:   提出统一的自蒸馏（Self-Distillation）框架来直接学习 flow map（即 consistency model 的一般化形式），通过 tangent condition 将任意蒸馏方案转化为无需预训练教师的直接训练算法，并导出三大算法族（Eulerian / Lagrangian / Progressive），其中 Lagrangian 方法避免了空间梯度和自举引导，训练最稳定、性能最优。

**[Image Super-Resolution with Guarantees via Conformalized Generative Models](image_super-resolution_with_guarantees_via_conformalized_generative_models.md)**

:   基于共形预测（Conformal Prediction）技术，为生成式图像超分辨率模型构建二值"置信度掩码"，能可靠地标识生成图像中可信赖的区域，并提供严格的统计保证。

**[ImageSentinel: Protecting Visual Datasets from Unauthorized Retrieval-Augmented Image Generation](imagesentinel_protecting_visual_datasets_from_unauthorized_retrieval-augmented_i.md)**

:   提出 ImageSentinel 框架，通过合成与私有数据集视觉一致的哨兵图像（sentinel images）并绑定随机字符检索键，实现对检索增强图像生成（RAIG）系统未授权使用私有数据集的可靠检测——仅需 3–10 次查询即可达到接近 100% 的 AUC。

**[Improved Training Technique for Shortcut Models (iSM)](improved_training_technique_for_shortcut_models.md)**

:   针对 Shortcut Models 的五大性能瓶颈（指导累积、固定引导、频率偏差、自一致性偏离、弯曲轨迹），提出 iSM 统一训练框架，通过内禀引导、多级小波损失、缩放最优传输和双 EMA 策略，在 ImageNet 256×256 上实现单步 FID 5.27、四步 FID 2.05 的大幅提升。

**[Improving Posterior Inference of Galaxy Properties with Image-Based Conditional Flow Matching](improving_posterior_inference_of_galaxy_properties_with_image-based_conditional_.md)**

:   提出基于条件流匹配（CFM）的框架，将星系图像的形态学信息与测光数据联合建模，显著提升星系物理属性（恒星质量、恒星形成率、金属丰度、尘埃消光等）的后验推断精度。

**[In-Context Edit Enabling Instructional Image Editing With In-Context Generation ](in-context_edit_enabling_instructional_image_editing_with_in-context_generation_.md)**

:   ICEdit 提出一种基于大规模 Diffusion Transformer (DiT) 的上下文编辑范式，通过 in-context prompt + 最小化 LoRA-MoE 微调 + VLM 早期筛选推理时缩放，仅用 0.1% 训练数据即达到 SOTA 编辑性能。

**[Increasing the Utility of Synthetic Images through Chamfer Guidance](increasing_the_utility_of_synthetic_images_through_chamfer_guidance.md)**

:   提出 Chamfer Guidance——一种免训练的推理时引导方法，利用少量真实样本作为参照，通过 Chamfer 距离同时优化合成图像的质量（fidelity）和多样性（diversity），在 ImageNet-1k 上仅用 32 张真实图片即可达到 97.5% Precision 和 92.7% Coverage，并在下游分类器训练中带来最高 16% 的准确率提升。

**[Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing](inference-time_scaling_for_flow_models_via_stochastic_generation_and_rollover_bu.md)**

:   提出针对 Flow 模型的推理时扩展方法：通过 ODE→SDE 转换引入随机性以启用粒子采样，利用线性→VP 插值变换扩大搜索空间，并设计 Rollover Budget Forcing (RBF) 策略自适应分配计算预算，在组合文本生成图像和数量感知生成任务上显著超越所有现有方法。

**[InfinityStar: Unified Spacetime AutoRegressive Modeling for Visual Generation](infinitystar_unified_spacetime_autoregressive_modeling_for_v.md)**

:   提出 InfinityStar，首个能生成工业级 720p 视频的纯离散自回归模型，通过时空金字塔建模统一 T2I/T2V/I2V/交互式长视频生成，VBench 83.74 超越 HunyuanVideo，推理速度比扩散模型快 10-32×。

**[Information-Theoretic Discrete Diffusion](information-theoretic_discrete_diffusion.md)**

:   将连续扩散中经典的 I-MMSE 恒等式推广到离散域，建立 I-MDSE 和 I-MDCE 关系——证明 DSE/DCE 损失不仅是变分上界而是对数似然的**精确分解**，并由此推导出 time-free 公式、条件似然估计和耦合似然比估计器，在 LLaDA 等大模型上验证了低方差和 OOD 检测能力。

**[Information Theoretic Learning for Diffusion Models with Warm Start](information_theoretic_learning_for_diffusion_models_with_warm_start.md)**

:   提出将经典 KL 散度-Fisher 信息关系推广到任意各向同性噪声扰动的似然估计框架，结合 warm-start 噪声注入和重要性采样，消除训练-测试差距并实现更紧的似然上界，在 ImageNet 多分辨率上达到 SOTA NLL。

**[Is Artificial Intelligence Generated Image Detection a Solved Problem?](is_artificial_intelligence_generated_image_detection_a_solved_problem.md)**

:   提出 AIGIBench 综合基准，通过四大任务（多源泛化、多退化鲁棒性、数据增强敏感性、测试预处理影响）系统评估 11 个 SOTA 检测器，揭示现有 AIGI 检测方法在真实场景下性能严重下降，表明该问题远未解决。

**[ItDPDM: Information-Theoretic Discrete Poisson Diffusion Model](itdpdm_information-theoretic_discrete_poisson_diffusion_model.md)**

:   提出 ItDPDM（信息论离散泊松扩散模型），通过泊松噪声信道和泊松重建损失（PRL）实现非负离散数据的精确似然估计，避免了 ELBO 近似和 dequantization，在合成数据及 CIFAR-10 和 MIDI 音乐上取得优于现有离散扩散模型的似然估计。

**[KLASS: KL-Guided Fast Inference in Masked Diffusion Models](klass_kl-guided_fast_inference_in_masked_diffusion_models.md)**

:   提出 KLASS（KL-Adaptive Stability Sampling），一种无需训练的采样方法，利用 token 级别的 KL 散度和置信度来识别稳定 token 并行解码，在掩码扩散模型上实现最高 2.78× 加速且不损失甚至提升生成质量。

**[Knowledge Distillation Detection for Open-weights Models](knowledge_distillation_detection_for_open-weights_models.md)**

:   提出知识蒸馏检测任务，通过无数据输入合成和统计评分框架，判断一个开放权重的学生模型是否由特定教师模型蒸馏而来。

**[LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss](lineas_end-to-end_learning_of_activation_steering_with_a_distributional_loss.md)**

:   提出 LinEAS（Linear End-to-end Activation Steering），通过端到端优化跨层仿射变换映射，利用 1D Wasserstein 分布损失进行全局激活值对齐，仅需 32 个无配对样本即可高效控制 LLM 毒性和 T2I 模型概念生成。

**[MagCache: Fast Video Generation with Magnitude-Aware Cache](magcache_fast_video_generation_with_magnitudeaware_cache.md)**

:   发现视频扩散模型中连续时间步残差输出的幅度比(magnitude ratio)遵循统一的单调递减规律（跨模型、跨prompt稳定），提出MagCache基于此规律自适应跳过冗余时间步并复用缓存，仅需1个样本校准即可在Open-Sora/CogVideoX/Wan 2.1/HunyuanVideo上实现2.1-2.68×加速，视觉保真度全面超越现有方法。

**[OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](omnisync_towards_universal_lip_synchronization_via_diffusion.md)**

:   OmniSync提出了一种基于Diffusion Transformer的通用唇形同步框架，通过无掩码训练范式、基于Flow Matching的渐进噪声初始化和动态时空CFG三大创新，在真实视频和AI生成视频上都大幅超越先前方法，尤其在风格化角色的唇形同步上达到87.78%成功率（之前最佳67.78%）。

**[On Optimal Steering to Achieve Exact Fairness](on_optimal_steering_to_achieve_exact_fairness.md)**

:   本文定义了"理想分布"——使任意代价敏感风险下的 Bayes 最优分类器都满足精确公平性的数据分布，并提出通过 KL 散度最小化寻找最近理想分布的优化框架，为公平预处理和 LLM 表示引导提供了可证明的公平性保证。

**[PhysCtrl: Generative Physics for Controllable and Physics-Grounded Video Generation](physctrl_generative_physics_for_controllable_and_physicsgrou.md)**

:   提出 PhysCtrl，通过生成式物理网络学习 4 种材质（弹性体、沙子、橡皮泥、刚体）的物理动力学分布，以 3D 点轨迹表示物理运动，结合 I2V 模型实现物理参数和力可控的视频生成。

**[Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection](physics-driven_spatiotemporal_modeling_for_ai-generated_video_detection.md)**

:   提出基于物理守恒定律的AI生成视频检测范式，定义归一化时空梯度（NSG）统计量来捕获空间概率梯度与时间密度变化的比率，利用预训练扩散模型估计NSG并通过MMD进行检测，在Recall上超越SOTA 16%、F1超越10.75%。

**[Remasking Discrete Diffusion Models with Inference-Time Scaling](remasking_discrete_diffusion_models_with_inference-time_scaling.md)**

:   提出 ReMDM 采样器，通过在生成过程中允许已解码 token 被重新掩码（remask），赋予离散掩码扩散模型迭代纠错能力，实现推理时计算缩放，在文本、图像和分子设计任务上显著提升采样质量。

**[Safe-Sora: Safe Text-to-Video Generation via Graphical Watermarking](safesora_safe_texttovideo_generation_via_graphical_watermark.md)**

:   Safe-Sora 首次将**图形水印**（如logo图像）直接嵌入到视频生成管线中，通过分层粗到细自适应匹配将水印patch分配到视觉最相似的帧和区域，并设计3D小波变换增强Mamba架构实现时空融合，在视频质量（FVD 3.77 vs 次优154.35）和水印保真度上大幅超越所有基线。

**[Scalable, Explainable and Provably Robust Anomaly Detection with One-Step Flow Matching](scalable_explainable_and_provably_robust_anomaly_detection_with_one-step_flow_ma.md)**

:   提出 TCCM（Time-Conditioned Contraction Matching），一种受 flow matching 启发的表格数据半监督异常检测方法，通过学习将正常数据收缩到原点的时间条件速度场，仅需单步前向推理即可计算异常分数，在 ADBench 47 个数据集上取得 AUROC 和 AUPRC 双第一，推理速度比 DTE 快 1573 倍。

**[Scaling Offline RL via Efficient and Expressive Shortcut Models](scaling_offline_rl_via_efficient_and_expressive_shortcut_models.md)**

:   提出 SORL，利用 shortcut models 的自一致性实现离线 RL 中高效一阶段训练与可变推理步数的策略优化，同时支持推理时的顺序和并行扩展。

**[Schrödinger Bridge Matching for Tree-Structured Costs and Entropic Wasserstein Barycentres](schrödinger_bridge_matching_for_tree-structured_costs_and_entropic_wasserstein_b.md)**

:   将Iterative Markovian Fitting (IMF)程序推广到树结构Schrödinger Bridge问题，提出TreeDSBM算法，在Wasserstein重心计算中将IMF迭代与不动点迭代优雅合并，仅需廉价的bridge-matching步骤即可高效求解。

**[Semantic Surgery: Zero-Shot Concept Erasure in Diffusion Models](semantic_surgery_zero-shot_concept_erasure_in_diffusion_models.md)**

:   提出Semantic Surgery，一种无需重训练的零样本推理时概念擦除框架，通过在扩散过程之前对文本嵌入进行校准向量减法，结合Co-Occurrence Encoding处理多概念擦除和视觉反馈环路解决潜在概念持久性问题，在物体/NSFW/风格/名人擦除任务上全面超越SOTA。

**[System-Embedded Diffusion Bridge Models](system-embedded_diffusion_bridge_models.md)**

:   提出System-embedded Diffusion Bridge Models（SDB），将已知的线性测量系统直接嵌入矩阵值SDE的系数中，实现了对值域空间去噪和零空间信息合成的分离控制，在多种逆问题上取得一致性提升并展现出强大的系统失配鲁棒性。

**[Understanding Representation Dynamics of Diffusion Models via Low-Dimensional Models](understanding_representation_dynamics_of_diffusion_models_via_low-dimensional_mo.md)**

:   在低秩高斯混合（MoLRG）数据模型下，理论证明了扩散模型表示质量随噪声水平呈单峰动态的现象源于去噪强度与类别区分度的权衡，并实证发现单峰动态的出现可作为模型泛化能力的可靠指标。

**[Watermarking Autoregressive Image Generation](watermarking_autoregressive_image_generation.md)**

:   首次将 LLM 水印技术（KGW green/red scheme）适配到自回归图像生成模型的 token 层，识别并解决了关键挑战——反向循环一致性（RCC）不足，通过 tokenizer-detokenizer 微调和水印同步层实现了鲁棒的、具有理论保证的图像水印检测。

**[Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training](why_diffusion_models_dont_memorize_the_role_of_implicit_dynamical_regularization.md)**

:   通过数值实验和理论分析揭示扩散模型训练中存在两个关键时间尺度——泛化时间 $\tau_{\text{gen}}$ 和记忆化时间 $\tau_{\text{mem}}$，后者随训练集大小 $n$ 线性增长而前者保持恒定，由此产生的隐式动力学正则化使模型即使在高度过参数化情况下也能通过早停避免记忆化。

**[Why Diffusion Models Don't Memorize: The Role of Implicit Regularization](why_diffusion_models_dont_memorize_the_role_of_implicit_regularization.md)**

:   本文从数值实验和理论分析两个层面揭示扩散模型训练中存在**隐式动态正则化**机制：生成高质量样本的时间尺度 τ_gen 与出现记忆化的时间尺度 τ_mem 之间的间隔随训练集大小 n 线性增长，为"早停"提供了理论支撑。
