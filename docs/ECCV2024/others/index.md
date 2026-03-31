<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📂 其他

**🎞️ ECCV2024** · 共 **11** 篇

**[A Closer Look at GAN Priors: Exploiting Intermediate Features for Enhanced Model Inversion Attacks](a_closer_look_at_gan_priors_exploiting_intermediate_features.md)**

:   提出 IF-GMI，将预训练 StyleGAN2 的生成器拆解为多个 block，在中间特征层逐层优化（配合 $\ell_1$ 球约束防止图像崩塌），把模型反演攻击的搜索空间从潜码扩展到中间特征，在 OOD 场景下攻击准确率提升高达 38.8%。

**[A Framework for Efficient Model Evaluation through Stratification, Sampling, and Estimation](a_framework_for_efficient_model_evaluation_through_stratific.md)**

:   提出一个统计框架，通过分层（stratification）、采样设计（sampling）和估计器（estimation）三个组件的协同设计，在仅标注少量测试样本的情况下精确估计CV模型准确率，最高可实现10倍的效率增益（即用1/10的标注量达到同等精度）。

**[A High-Quality Robust Diffusion Framework for Corrupted Dataset](a_highquality_robust_diffusion_framework_for_corrupted_datas.md)**

:   提出 RDUOT 框架，首次将非平衡最优传输(UOT)融入扩散模型(DDGAN)中，通过学习 $q(x_0|x_t)$ 而非 $q(x_{t-1}|x_t)$ 来有效过滤训练数据中的离群值，在污染数据集上实现鲁棒生成的同时，在干净数据集上也超越了 DDGAN 基线。

**[ABC Easy as 123: A Blind Counter for Exemplar-Free Multi-Class Class-Agnostic Counting](abc_easy_as_123_a_blind_counter_for_exemplar-free_multi-class_class-agnostic_cou.md)**

:   提出首个无需样例图像即可同时计数图像中多类未知物体的方法ABC123，通过ViT回归多通道密度图+匈牙利匹配训练+SAM示例发现机制，在自建合成数据集MCAC上大幅超越需要样例的方法，且能泛化到FSC-147真实数据集。

**[Action2Sound: Ambient-Aware Generation of Action Sounds from Egocentric Videos](action2sound_ambientaware_generation_of_action_sounds_from_e.md)**

:   提出 AV-LDM，通过在训练时引入同一视频不同时间段的音频作为环境音条件，隐式解耦前景动作声和背景环境音，结合检索增强生成(RAG)在推理时选择合适的环境音条件，在 Ego4D 和 EPIC-KITCHENS 上大幅超越已有方法。

**[Active Generation for Image Classification](active_generation_for_image_classification.md)**

:   ActGen将主动学习思想引入扩散模型数据增强，通过识别分类器的错分样本并以注意力掩码引导+梯度对抗引导生成"难样本"，仅用10%的合成数据量即超越了此前需要近等量合成数据的方法，在ImageNet上ResNet-50获得+2.26%的精度提升。

**[Adaptive High-Frequency Transformer for Diverse Wildlife Re-Identification](adaptive_highfrequency_transformer_for_diverse_wildlife_reid.md)**

:   提出自适应高频Transformer（AdaFreq），通过频域混合增强、目标感知的高频token动态选择、特征均衡损失三大策略，将高频信息（毛皮纹理、轮廓边缘等）统一用于多种野生动物的重识别，在8个跨物种数据集上超越现有ReID方法。

**[Bidirectional Uncertainty-Based Active Learning For Open-Set Annotation](bidirectional_uncertainty-based_active_learning_for_open-set_annotation.md)**

:   提出 BUAL 框架，通过 Random Label Negative Learning 将未知类样本推向高置信区域、已知类样本推向低置信区域，结合双向不确定性采样策略，在开放集场景下有效选出高信息量的已知类样本。

**[Cross-Domain Learning for Video Anomaly Detection with Limited Supervision](cross-domain_learning_for_video_anomaly_detection_with_limited_supervision.md)**

:   提出弱监督跨域学习（CDL）框架，通过不确定性驱动的伪标签机制将无标注外部视频整合到训练中，显著提升视频异常检测的跨域泛化能力。

**[DC-Solver: Improving Predictor-Corrector Diffusion Sampler via Dynamic Compensation](dc-solver_improving_predictor-corrector_diffusion_sampler_via_dynamic_compensati.md)**

:   提出 DC-Solver，通过动态补偿（Dynamic Compensation）缓解 predictor-corrector 扩散采样器中的 misalignment 问题，仅需 10 个数据点即可优化补偿比率，并通过级联多项式回归（CPR）实现对未见 NFE/CFG 配置的即时泛化。

**[Teaching Tailored to Talent: Adverse Weather Restoration via Prompt Pool and Depth-Anything Constraint](teaching_tailored_to_talent_adverse_weather_restoration.md)**

:   提出 T3-DiffWeather，采用 prompt pool 自主组合子 prompt 构建天气退化信息，结合 Depth-Anything 约束的通用 prompt 提供场景信息，以对比 prompt 损失约束两类 prompt，在恶劣天气图像恢复任务上仅用 WeatherDiffusion 十分之一的采样步数达到 SOTA。
