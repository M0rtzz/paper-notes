---
title: >-
  ACL2025 MoE / 混合专家方向4篇论文解读
description: >-
  4篇ACL2025的 MoE / 混合专家方向论文解读，涵盖 LLM、压缩/编码、模型压缩等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧠 MoE / 混合专家

**💬 ACL2025** · **4** 篇论文解读

📌 **同领域跨会议浏览：** [🔬 ICLR2026 (1)](../../ICLR2026/moe/) · [🧠 NeurIPS2025 (1)](../../NeurIPS2025/moe/)

🔥 **高频主题：** LLM ×2

**[DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts](dive_moe_reconstruction.md)**

:   提出 DIVE，一种将 Dense LLM 重构为 MoE 架构的方法，核心洞察是不同领域的校准数据集会让结构化剪枝产生不同的剪枝结果，利用这种多样性构建领域特异的专家，配合高效的两阶段重训练（router dense训练 + expert LoRA稀疏训练），在仅调不到 1% 参数的情况下实现优于现有剪枝和 MoE 重构方法的效果。

**[EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](eac_moe_expert_aware_compression.md)**

:   EAC-MoE 深入分析 MoE 模型的专家选择特性，提出两个互补模块——量化时通过逐层校准路由器缓解 expert-shift 问题（QESC），推理时基于专家选择频率动态剪枝不重要专家（PESF），在 4 个 MoE 模型上实现显著的内存压缩和推理加速且精度损失极小。

**[GigaChat Family: Efficient Russian Language Modeling Through Mixture of Experts Architecture](gigachat_family_efficient_russian_language_modeling_through_mixture_of_experts_a.md)**

:   介绍 GigaChat 系列——首个从头为俄语设计并预训练的 MoE 架构 LLM 家族，包含 20B 总参数/3.3B 激活参数的基座和指令微调模型，在俄语 benchmark 上达到同规模 SOTA，训练速度是同量级 dense 模型的 2 倍，推理延迟降低 40%。

**[STUN: Structured-Then-Unstructured Pruning for Scalable MoE Pruning](stun_moe_pruning.md)**

:   STUN 提出"先结构化后非结构化"的两阶段 MoE 剪枝范式：第一阶段利用路由权重的行为相似性聚类冗余专家，以 $O(1)$ GPU 前向传播完成专家级剪枝；第二阶段在剩余专家内做非结构化权重剪枝，两者协同在 480B Snowflake Arctic 上以 40% 稀疏度几乎无性能损失。
