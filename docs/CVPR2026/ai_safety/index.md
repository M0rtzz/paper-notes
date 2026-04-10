<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**📷 CVPR2026** · 共 **22** 篇

**[A Unified Perspective on Adversarial Membership Manipulation in Vision Models](a_unified_perspective_on_adversarial_membership_manipulation_in_vision_models.md)**

:   首次揭示视觉模型成员推断攻击(MIA)面临的对抗性成员操纵漏洞——不可感知扰动可将非成员伪造为成员欺骗审计，发现伪造成员的梯度范数塌缩特征签名，并提出基于梯度几何的检测策略和对抗鲁棒推断框架。

**[All Vehicles Can Lie: Efficient Adversarial Defense in Fully Untrusted-Vehicle Collaborative Perception via Pseudo-Random Bayesian Inference](all_vehicles_can_lie_efficient_adversarial_defense_in_fully_untrusted-vehicle_co.md)**

:   提出 Pseudo-Random Bayesian Inference (PRBI) 框架，在**所有车辆均不可信**的协同感知场景中，利用帧间时序一致性作为自参考信号，通过伪随机分组 + 贝叶斯推断，仅需平均 2.5 次验证/帧即可高效识别并排除恶意车辆，检测精度恢复至攻击前的 79.4%–86.9%。

**[Computation and Communication Efficient Federated Unlearning via On-server Gradient Conflict Mitigation and Expression](computation_and_communication_efficient_federated_unlearning_via_on-server_gradi.md)**

:   提出 FOUL 框架，通过"学习阶段解耦因果/非因果特征 + 遗忘阶段服务器端梯度冲突匹配"两阶段策略，在不访问客户端数据的前提下实现高效且低通信开销的联邦遗忘。

**[Domain-Skewed Federated Learning with Feature Decoupling and Calibration](domain-skewed_federated_learning_with_feature_decoupling_and_calibration.md)**

:   提出 F²DC 框架，通过域特征解耦器（DFD）和域特征校正器（DFC）将联邦学习中客户端的局部特征分离为域鲁棒特征和域相关特征，并对域相关特征进行校准以挽救被丢弃的类别信息，配合域感知聚合策略，在三个多域数据集上一致超越 SOTA。

**[Editing Away the Evidence: Diffusion-Based Image Manipulation and the Failure Modes of Robust Watermarking](editing_away_the_evidence_diffusion-based_image_manipulation_and_the_failure_mod.md)**

:   本文从理论和实验两方面统一分析了非对抗性扩散编辑如何无意中破坏鲁棒隐形水印，推导了水印 SNR 衰减和互信息衰减的界，并在指令编辑、拖拽编辑、无训练合成等场景下验证了水印恢复的系统性失效。

**[Editing Away the Evidence: Diffusion-Based Image Manipulation and the Failure Modes of Robust Watermarking](editing_away_the_evidence_diffusionbased_image_man.md)**

:   本文从理论和实验两方面系统分析了扩散编辑（instruction/drag/composition）如何非对抗性地破坏鲁棒隐形水印，推导出 SNR 衰减和互信息下界，揭示常规后处理鲁棒性不能推广到生成式变换。

**[Editing Physiological Signals in Videos Using Latent Representations](editing_physiological_signals_in_videos_using_latent_representations.md)**

:   提出面向视频生理信号(心率)编辑的学习框架——在3D VAE潜空间中融合视频编码和目标心率文本嵌入，通过可训练时空融合层(AdaLN)捕捉rPPG时间相干性+FiLM解码器调制实现精确心率修改，视觉质量保持PSNR 38.96dB/SSIM 0.98的同时心率调制误差10 bpm MAE，可用于面部视频的心率匿名化或合成带指定心率的视频。

**[FecalFed: Privacy-Preserving Poultry Disease Detection via Federated Learning](fecalfed_privacy-preserving_poultry_disease_detection_via_federated_learning.md)**

:   提出 FecalFed 框架，通过联邦学习实现隐私保护的禽类疾病分类：首先清理公开数据集中 46.89% 的重复污染，发布 8,770 张去重数据集 poultry-fecal-fl，然后在高度非 IID 条件下验证联邦学习可将单农场训练的 64.86% 准确率恢复至 90.31%，接近中心化训练的 95.10%。

**[FedAFD: Multimodal Federated Learning via Adversarial Fusion and Distillation](fedafd_multimodal_federated_learning_via_adversarial_fusion_and_distillation.md)**

:   提出 FedAFD 框架，通过双层对抗对齐、粒度感知特征融合和相似度引导的集成蒸馏三阶段设计，在多模态联邦学习中同时提升异构客户端和服务器的模型性能。

**[Federated Active Learning Under Extreme Non-IID and Global Class Imbalance](federated_active_learning_extreme_noniid.md)**

:   系统分析全局类不平衡与客户端异构性对联邦主动学习中 query model 选择的影响，发现类平衡采样能力是性能的最一致预测因子，据此提出 FairFAL——自适应选择 query model + 原型引导伪标签 + 不确定性-多样性平衡采样的类公平 FAL 框架。

**[Federated Active Learning Under Extreme Non-IID and Global Class Imbalance](federated_active_learning_under_extreme_non-iid_and_global_class_imbalance.md)**

:   系统研究了联邦主动学习中查询模型选择问题，发现类别平衡采样是性能关键因素，并提出 FairFAL 框架，通过自适应模型选择、原型引导伪标签和不确定性-多样性平衡采样实现公平高效的联邦主动学习。

**[FedRE: A Representation Entanglement Framework for Model-Heterogeneous Federated Learning](fedre_a_representation_entanglement_framework_for_model-heterogeneous_federated_.md)**

:   提出 FedRE 框架，通过"纠缠表示"（entangled representation）——将每个客户端的所有局部表示用归一化随机权重聚合为单一跨类别表示，实现模型异构联邦学习中性能、隐私保护和通信开销的三方平衡。

**[Generative Adversarial Perturbations with Cross-paradigm Transferability on Localized Crowd Counting](generative_adversarial_perturbations_with_cross-paradigm_transferability_on_loca.md)**

:   提出首个跨范式（密度图 + 点回归）对抗攻击框架 CrowdGen，利用轻量级 UNet 生成器和多任务损失（logit 抑制 + 密度抑制 + GradCAM 引导 + 频域约束），在保持视觉隐蔽性（~19dB PSNR）的同时实现对七个 SOTA 人群计数模型的高迁移率（TR 最高 1.69），攻击 MAE 平均提升 7 倍。

**[Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Language Models](multi-paradigm_collaborative_adversarial_attack_against_multi-modal_large_langua.md)**

:   提出 MPCAttack 框架，联合跨模态对齐、多模态理解和视觉自监督三种学习范式的特征表示，通过多范式协同优化策略生成高迁移性对抗样本，在开源和闭源 MLLM 上均取得 SOTA 攻击效果。

**[PinPoint: Evaluation of Composed Image Retrieval with Explicit Negatives, Multi-Image Queries, and Paraphrase Testing](pinpoint_evaluation_of_composed_image_retrieval_with_explicit_negatives_multi-im.md)**

:   提出 PinPoint 基准，包含 7,635 个查询和 329K 人工验证的相关性判断，通过显式负样本、多图像查询、释义变体和人口统计元数据四个维度，揭示了现有 CIR 方法在假阳性抑制、语言鲁棒性和多图像推理上的严重缺陷，并提出基于 MLLM 的无训练重排方法作为改进基线。

**[ProxyFL: A Proxy-Guided Framework for Federated Semi-Supervised Learning](proxyfl_a_proxy-guided_framework_for_federated_semi-supervised_learning.md)**

:   提出 ProxyFL 框架，利用分类器权重作为统一代理 (proxy) 同时缓解联邦半监督学习中的外部异质性（跨客户端分布差异）和内部异质性（标注/未标注数据分布不匹配），在多个数据集上显著超越现有 FSSL 方法。

**[Rethinking VLMs for Image Forgery Detection and Localization](rethinking_vlms_for_image_forgery_detection_and_lo.md)**

:   揭示VLM的语义合理性偏差(semantic plausibility bias)会妨碍伪造检测，提出IFDL-VLM将检测/定位与语言解释生成解耦为两阶段：先用ViT+SAM专做检测定位，再将定位mask作为VLM辅助输入增强可解释性，在9个基准上全面SOTA。

**[Rethinking VLMs for Image Forgery Detection and Localization](rethinking_vlms_for_image_forgery_detection_and_localization.md)**

:   提出 IFDL-VLM 框架，发现 VLM 固有的语义合理性偏向（而非真实性）会阻碍伪造检测性能，因此将检测/定位与语言解释解耦为两阶段优化，并利用定位掩码作为 VLM 的辅助输入增强可解释性，在 9 个基准上全面达到 SOTA。

**[SineProject: Machine Unlearning for Stable Vision–Language Alignment](sineproject_machine_unlearning_for_stable_vision_language_alignment.md)**

:   针对多模态大模型（MLLM）在机器遗忘过程中投影层 Jacobian 严重病态导致视觉-语言对齐漂移的问题，提出 SineProject——通过对投影层权重施加正弦调制（sin(ΔW)）来约束参数范围至 [-1,1]，从而将 Jacobian 条件数降低 3-4 个数量级，在完全遗忘目标知识的同时将良性查询误拒率（SARR）降低 15%。

**[SLICE: Semantic Latent Injection via Compartmentalized Embedding for Image Watermarking](slice_semantic_latent_injection_via_compartmentali.md)**

:   提出SLICE框架，将图像语义解耦为四个因子（主体/环境/动作/细节），各自锚定到扩散模型初始噪声的不同空间分区，实现细粒度语义感知水印——不仅能检测篡改，还能精确定位被篡改的语义因子，且完全无需训练。

**[Towards Highly Transferable Vision-Language Attack via Semantic-Augmented Dynamic Contrastive Interaction](towards_highly_transferable_vision-language_attack_via_semantic-augmented_dynami.md)**

:   提出 SADCA（语义增强动态对比攻击），通过动态对比交互机制和语义增强模块，迭代地破坏对抗图像与文本之间的跨模态语义一致性，显著提升对视觉语言预训练模型（VLP）的对抗可迁移性，在跨模型和跨任务攻击中均超越现有 SOTA 方法。

**[V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs](v-attack_targeting_disentangled_value_features_for_controllable_adversarial_atta.md)**

:   发现 ViT 中 Value 特征相比 Patch 特征具有更解耦的局部语义表示，提出 V-Attack 通过自增强 Value 特征 + 文本引导语义操控实现精确可控的 LVLM 局部语义攻击，ASR 平均提升 36%。
