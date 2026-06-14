---
title: >-
  CVPR2026 预训练论文汇总 · 4篇论文解读
description: >-
  4篇CVPR2026的预训练方向论文解读，涵盖少样本学习等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2026"
  - "预训练"
  - "论文解读"
  - "论文笔记"
  - "少样本学习"
item_list:
  - u: "evidential_transformation_network_post_hoc_uncertainty_estimation/"
    t: "Evidential Transformation Network: Turning Pretrained Models into Evidential Models for Post-hoc Uncertainty Estimation"
  - u: "linking_modality_isolation_in_heterogeneous_collaborative_perception/"
    t: "Linking Modality Isolation in Heterogeneous Collaborative Perception"
  - u: "unlocking_pre-trained_weights_parameter_inheritance_for_zero-shot_initialization/"
    t: "Unlocking Pre-trained Weights: Parameter Inheritance for Zero-Shot Initialization"
  - u: "watch_and_learn_learning_to_use_computers_from_online_videos/"
    t: "Watch and Learn: Learning to Use Computers from Online Videos"
item_total: 4
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📚 预训练

**📷 CVPR2026** · **4** 篇论文解读

📌 **同领域跨会议浏览：** [🧪 ICML2026 (22)](../../ICML2026/llm_pretraining/index.md) · [💬 ACL2026 (12)](../../ACL2026/llm_pretraining/index.md) · [🔬 ICLR2026 (25)](../../ICLR2026/llm_pretraining/index.md) · [🤖 AAAI2026 (9)](../../AAAI2026/llm_pretraining/index.md) · [🧠 NeurIPS2025 (51)](../../NeurIPS2025/llm_pretraining/index.md) · [📹 ICCV2025 (9)](../../ICCV2025/llm_pretraining/index.md)

**[Evidential Transformation Network: Turning Pretrained Models into Evidential Models for Post-hoc Uncertainty Estimation](evidential_transformation_network_post_hoc_uncertainty_estimation.md)**

:   本文提出 Evidential Transformation Network (ETN)，一个轻量级后置模块，通过在 logit 空间学习样本相关的仿射变换，将预训练分类器或 LLM 转化为证据模型，以最小的计算开销实现可靠的不确定性估计。

**[Linking Modality Isolation in Heterogeneous Collaborative Perception](linking_modality_isolation_in_heterogeneous_collaborative_perception.md)**

:   提出 CodeAlign 框架，通过码本构建离散代码空间和跨模态 Feature-Code-Feature (FCF) 翻译，首次解决异构协同感知中不同模态从未在训练数据中共现的"模态隔离"问题，仅需 HEAL 8% 训练参数、通信量降低 1024 倍，同时达到 SOTA 感知性能。

**[Unlocking Pre-trained Weights: Parameter Inheritance for Zero-Shot Initialization](unlocking_pre-trained_weights_parameter_inheritance_for_zero-shot_initialization.md)**

:   PITH 用图超网络给目标网络动态生成「投影矩阵」，把预训练大模型的内部权重直接投影到任意尺寸的目标 ViT 上完成初始化，使得初始化后的网络无需任何训练就能直接用——在 ImageNet-1K 上 ViT-Base 零样本精度 53.35%，比上一代 SOTA（TAL）高 6.54%。

**[Watch and Learn: Learning to Use Computers from Online Videos](watch_and_learn_learning_to_use_computers_from_online_videos.md)**

:   提出 Watch & Learn (W&L) 框架，通过逆动力学模型 (IDM) 将互联网上的人类计算机操作视频自动转化为可执行的 UI 轨迹数据，生成 53K+ 高质量轨迹，作为 ICL 示例或 SFT 训练数据显著提升各类 CUA 性能。
