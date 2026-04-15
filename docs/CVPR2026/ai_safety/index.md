---
title: >-
  CVPR2026 AI安全方向 18篇论文解读
description: >-
  18篇CVPR2026 AI安全方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI安全

**📷 CVPR2026** · 共 **18** 篇

**[A Unified Perspective On Adversarial Membership Manipulation In Vision Models](a_unified_perspective_on_adversarial_membership_manipulation_in_vision_models.md)**

:   首次揭示视觉模型成员推断攻击(MIA)面临的对抗性成员操纵漏洞——不可感知扰动可将非成员伪造为成员欺骗审计，发现伪造成员的梯度范数塌缩特征签名，并提出基于梯度几何的检测策略和对抗鲁棒推断框架。

**[All Vehicles Can Lie Efficient Adversarial Defense In Fully Untrusted-Vehicle Co](all_vehicles_can_lie_efficient_adversarial_defense_in_fully_untrusted-vehicle_co.md)**

:   提出 Pseudo-Random Bayesian Inference (PRBI) 框架，在**所有车辆均不可信**的协同感知场景中，利用帧间时序一致性作为自参考信号，通过伪随机分组 + 贝叶斯推断，仅需平均 2.5 次验证/帧即可高效识别并排除恶意车辆，检测精度恢复至攻击前的 79.4%–86.9%。

**[Computation And Communication Efficient Federated Unlearning Via On-Server Gradi](computation_and_communication_efficient_federated_unlearning_via_on-server_gradi.md)**

:   提出 FOUL 框架，通过"学习阶段解耦因果/非因果特征 + 遗忘阶段服务器端梯度冲突匹配"两阶段策略，在不访问客户端数据的前提下实现高效且低通信开销的联邦遗忘。

**[Domain-Skewed Federated Learning With Feature Decoupling And Calibration](domain-skewed_federated_learning_with_feature_decoupling_and_calibration.md)**

:   提出 F²DC 框架，通过域特征解耦器（DFD）和域特征校正器（DFC）将联邦学习中客户端的局部特征分离为域鲁棒特征和域相关特征，并对域相关特征进行校准以挽救被丢弃的类别信息，配合域感知聚合策略，在三个多域数据集上一致超越 SOTA。

**[Editing Physiological Signals In Videos Using Latent Representations](editing_physiological_signals_in_videos_using_latent_representations.md)**

:   提出PhysioLatent框架，将输入面部视频编码到3D VAE潜空间，与目标心率CLIP文本嵌入融合，通过AdaLN增强的时空融合层捕捉rPPG时间相干性，结合FiLM调制解码器和微调输出层实现精确心率修改，在保持PSNR 38.96dB/SSIM 0.98的视觉质量下达到10 bpm MAE的心率调制精度。

**[Fecalfed Privacy-Preserving Poultry Disease Detection Via Federated Learning](fecalfed_privacy-preserving_poultry_disease_detection_via_federated_learning.md)**

:   提出 FecalFed 隐私保护联邦学习框架，首先通过双哈希去重清理公开禽类粪便数据集中 46.89% 的重复污染并发布 8,770 张清洁基准数据集 poultry-fecal-fl，随后在 Dirichlet α=0.5 的高度非 IID 条件下验证：FedAdam + Swin-Small 可将单农场训练崩溃的 64.86% 准确率恢复至 90.31%，仅比中心化上界 95.10% 低 4.79%；边缘优化的 Swin-Tiny（28M 参数）仍达 89.74%，为农场端部署提供高效可行方案。

**[Fedafd Multimodal Federated Learning Via Adversarial Fusion And Distillation](fedafd_multimodal_federated_learning_via_adversarial_fusion_and_distillation.md)**

:   提出 FedAFD 框架，通过双层对抗对齐、粒度感知特征融合和相似度引导的集成蒸馏三阶段设计，在多模态联邦学习中同时提升异构客户端和服务器的模型性能。

**[Federated Active Learning Extreme Noniid](federated_active_learning_extreme_noniid.md)**

:   系统分析全局类不平衡与客户端异构性对联邦主动学习中 query model 选择的影响，归纳出3个核心 Observation，据此提出 FairFAL——自适应选择 query model + 原型引导伪标签 + 两阶段不确定性-多样性平衡采样的类公平 FAL 框架，在5个基准数据集上一致超越所有基线。

**[Federated Active Learning Under Extreme Non-Iid And Global Class Imbalance](federated_active_learning_under_extreme_non-iid_and_global_class_imbalance.md)**

:   系统研究了联邦主动学习中查询模型选择问题，发现类别平衡采样是性能关键因素，并提出 FairFAL 框架，通过自适应模型选择、原型引导伪标签和不确定性-多样性平衡采样实现公平高效的联邦主动学习。

**[Fedre A Representation Entanglement Framework For Model-Heterogeneous Federated ](fedre_a_representation_entanglement_framework_for_model-heterogeneous_federated_.md)**

:   提出 FedRE 框架，通过"纠缠表示"（entangled representation）——将每个客户端的所有局部表示用归一化随机权重聚合为单一跨类别表示，实现模型异构联邦学习中性能、隐私保护和通信开销的三方平衡。

**[Generative Adversarial Perturbations With Cross-Paradigm Transferability On Loca](generative_adversarial_perturbations_with_cross-paradigm_transferability_on_loca.md)**

:   提出首个跨范式（密度图 + 点回归）对抗攻击框架 CrowdGen，利用轻量级 UNet 生成器和多任务损失（logit 抑制 + 密度抑制 + GradCAM 引导 + 频域约束），在保持视觉隐蔽性（~19dB PSNR）的同时实现对七个 SOTA 人群计数模型的高迁移率（TR 最高 1.69），攻击 MAE 平均提升 7 倍。

**[Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Langua](multi-paradigm_collaborative_adversarial_attack_against_multi-modal_large_langua.md)**

:   提出 MPCAttack 框架，联合跨模态对齐、多模态理解和视觉自监督三种学习范式的特征表示，通过多范式协同优化策略生成高迁移性对抗样本，在开源和闭源 MLLM 上均取得 SOTA 攻击效果。

**[Pinpoint Evaluation Of Composed Image Retrieval With Explicit Negatives Multi-Im](pinpoint_evaluation_of_composed_image_retrieval_with_explicit_negatives_multi-im.md)**

:   提出 PinPoint 基准，包含 7,635 个查询和 329K 人工验证的相关性判断，通过显式负样本、多图像查询、释义变体和人口统计元数据四个维度，揭示了现有 CIR 方法在假阳性抑制、语言鲁棒性和多图像推理上的严重缺陷，并提出基于 MLLM 的无训练重排方法作为改进基线。

**[Proxyfl A Proxy-Guided Framework For Federated Semi-Supervised Learning](proxyfl_a_proxy-guided_framework_for_federated_semi-supervised_learning.md)**

:   提出 ProxyFL 框架，利用分类器权重作为统一代理 (proxy) 同时缓解联邦半监督学习中的外部异质性（跨客户端分布差异）和内部异质性（标注/未标注数据分布不匹配），在多个数据集上显著超越现有 FSSL 方法。

**[Rethinking Vlms For Image Forgery Detection And Lo](rethinking_vlms_for_image_forgery_detection_and_lo.md)**

:   揭示VLM天然偏向语义合理性而非真实性（CLIP对伪造图像余弦相似度达96-99%），提出IFDL-VLM将检测定位与语言解释解耦为两阶段，先用ViT+SAM做检测定位再将mask作为VLM辅助输入增强可解释性，在9个基准上全面达到SOTA。

**[Rethinking Vlms For Image Forgery Detection And Localization](rethinking_vlms_for_image_forgery_detection_and_localization.md)**

:   提出 IFDL-VLM 框架，发现 VLM 固有的语义合理性偏向（而非真实性）会阻碍伪造检测性能，因此将检测/定位与语言解释解耦为两阶段优化，并利用定位掩码作为 VLM 的辅助输入增强可解释性，在 9 个基准上全面达到 SOTA。

**[Towards Highly Transferable Vision-Language Attack Via Semantic-Augmented Dynami](towards_highly_transferable_vision-language_attack_via_semantic-augmented_dynami.md)**

:   提出 SADCA（语义增强动态对比攻击），通过动态对比交互机制和语义增强模块，迭代地破坏对抗图像与文本之间的跨模态语义一致性，显著提升对视觉语言预训练模型（VLP）的对抗可迁移性，在跨模型和跨任务攻击中均超越现有 SOTA 方法。

**[V-Attack Targeting Disentangled Value Features For Controllable Adversarial Atta](v-attack_targeting_disentangled_value_features_for_controllable_adversarial_atta.md)**

:   发现 ViT 中 Value 特征相比 Patch 特征具有更解耦的局部语义表示，提出 V-Attack 通过自增强 Value 特征 + 文本引导语义操控实现精确可控的 LVLM 局部语义攻击，ASR 平均提升 36%。
