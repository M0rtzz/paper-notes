---
title: >-
  CVPR2026 LLM安全方向 9篇论文解读
description: >-
  9篇CVPR2026 LLM安全论文解读，主题涵盖：提出 EMIMC 框架，受大脑海马-前额叶协作记忆、系统研究 VLM 微调到自动驾驶场景时的灾难性遗忘、提出 DAMP（深度感知投影调制）等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔒 LLM安全

**📷 CVPR2026** · **9** 篇论文解读

**[Association and Consolidation: Evolutionary Memory-Enhanced Incremental Multi-View Clustering](association_and_consolidation_evolutionary_memory-enhanced_incremental_multi-vie.md)**

:   提出 EMIMC 框架，受大脑海马-前额叶协作记忆机制启发，通过 Rapid Associative Module (正交映射保证可塑性)、Cognitive Forgetting Module (幂律衰减模拟遗忘曲线) 和 Knowledge Consolidation Module (时序张量低秩分解提炼长期记忆) 三模块协同，解决增量多视图聚类中的稳定性-可塑性困境。

**[The Blind Spot of Adaptation: Quantifying and Mitigating Forgetting in Fine-tuned Driving Models](blind_spot_of_adaptation_quantifying_and_mitigating_forgetting_in_fine_tuned_driving_models.md)**

:   系统研究 VLM 微调到自动驾驶场景时的灾难性遗忘问题，构建 180K 场景大规模基准 FidelityDrivingBench，并提出 Drive Expert Adapter (DEA) 通过提示空间路由在不腐蚀基础参数的前提下增强驾驶任务性能。

**[DAMP: Class Unlearning via Depth-Aware Removal of Forget-Specific Directions](damp_class_unlearning_via_depth_aware_removal_of_forget_specific_directions.md)**

:   提出 DAMP（深度感知投影调制），一种一次性闭式权重手术方法用于类遗忘，通过在每个网络阶段的编辑空间中移除遗忘类特有方向来实现选择性遗忘，深度感知缩放规则确保浅层保守编辑、深层强力编辑。

**[Designing to Forget: Deep Semi-parametric Models for Unlearning](designing_to_forget_deep_semi-parametric_models_for_unlearning.md)**

:   提出"Designing to Forget"理念，设计了一族深度半参数模型 (SPM)，在推理时通过简单删除训练样本即可实现遗忘（无需修改模型参数），在 ImageNet 分类上将与重训基线的预测差距减少 11%，遗忘速度提升 10 倍以上。

**[Elastic Weight Consolidation Done Right for Continual Learning](elastic_weight_consolidation_done_right_for_continual_learning.md)**

:   本文从梯度视角系统分析了 EWC 及其变体在权重重要性估计上的根本缺陷（EWC 的梯度消失和 MAS 的冗余保护），并提出了一个极其简单的 Logits Reversal 操作来修正 Fisher 信息矩阵的计算，在无样例类增量学习和多模态持续指令微调任务上大幅超越原始 EWC 及其所有变体。

**[Learning from Oblivion: Predicting Knowledge-Overflowed Weights via Retrodiction of Forgetting](learning_from_oblivion_predicting_knowledge_overflowed_weights_via_retrodiction_.md)**

:   提出KNOW prediction：通过在逐步缩小的数据子集上sequential fine-tuning诱导结构化遗忘过程，收集权重转变轨迹，然后用meta-learned hyper-model（KNOWN）反转forgetting方向，预测"仿佛在更大数据集上训练"的虚拟知识增强权重。跨多数据集(CIFAR/ImageNet/PACS等)和多架构(ResNet/PVTv2/DeepLabV3+)持续超越naive fine-tuning及多种weight prediction基线，在图像分类、语义分割、图像描述、域泛化等下游任务上均有显著提升。

**[⊘ Source Models Leak What They Shouldn't ↛: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization](oslash_source_models_leak_what_they_shouldnt_nrightarrow_unlearning_zero-shot_tr.md)**

:   发现无源域自适应（SFDA）方法会不经意地将源域独有类别的知识泄漏到目标域（零样本迁移现象），提出 SCADA-UL 框架通过对抗生成遗忘样本和重缩放标签策略，在域自适应过程中同时完成类别遗忘，达到接近从头训练的遗忘效果。

**[Select, Hypothesize and Verify: Towards Verified Neuron Concept Interpretation](select_hypothesize_and_verify_towards_verified_neuron_concept_interpretation.md)**

:   提出 SIEVE（Select–Hypothesize–Verify）框架，通过筛选高激活样本、生成概念假设、再用文生图验证的闭环流程来解释神经元功能，生成的概念激活对应神经元的概率约为现有 SOTA 的 1.5 倍。

**[SineProject: Machine Unlearning for Stable Vision–Language Alignment](sineproject_machine_unlearning_for_stable_vision_language_alignment.md)**

:   针对多模态大模型（MLLM）在机器遗忘过程中投影层 Jacobian 严重病态导致视觉-语言对齐漂移的问题，提出 SineProject——通过对投影层权重施加正弦调制（sin(ΔW)）来约束参数范围至 [-1,1]，从而将 Jacobian 条件数降低 3-4 个数量级，在完全遗忘目标知识的同时将良性查询误拒率（SARR）降低 15%。
