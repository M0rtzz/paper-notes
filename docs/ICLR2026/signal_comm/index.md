---
title: >-
  ICLR2026 信号/通信方向 8篇论文解读
description: >-
  8篇ICLR2026 信号/通信方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🔬 ICLR2026** · 共 **8** 篇

**[Deterministic Bounds And Random Estimates Of Metric Tensors On Neuromanifolds](deterministic_bounds_and_random_estimates_of_metric_tensors_on_neuromanifolds.md)**

:   本文通过分析低维概率分布核空间的Fisher信息矩阵(FIM)谱性质，为神经网络参数空间(神经流形)上的度量张量建立了确定性上下界，并基于Hutchinson迹估计器引入了一族有界方差的无偏随机估计方法，仅需单次反向传播即可高效计算。

**[Fasa Frequency-Aware Sparse Attention](fasa_frequency-aware_sparse_attention.md)**

:   发现 RoPE 注意力在频率块(FC)级别存在功能稀疏性——仅不到 1% 的"主导 FC"就能近似完整注意力头的 token 选择行为。据此设计无需训练的 FASA 框架，通过两阶段策略（主导 FC 预测 token 重要性 → 仅对重要 token 做完整注意力）实现 8× 内存压缩和 2.6× 推理加速且几乎无质量损失。

**[Group Representational Position Encoding](group_representational_position_encoding.md)**

:   提出 GRAPE 框架，基于群作用（group actions）统一了 Transformer 中乘法型（RoPE）和加法型（ALiBi/FoX）两大位置编码家族，证明 RoPE 和 ALiBi 是其精确特例，并提出路径积分加法变体 GRAPE-AP 在下游任务上超越现有方法。

**[Learning Molecular Chirality Via Chiral Determinant Kernels](learning_molecular_chirality_via_chiral_determinant_kernels.md)**

:   提出手性行列式核(ChiDeK)来编码 SE(3) 不变的手性矩阵，首次在 GNN 框架中统一处理中心手性和轴向手性，结合交叉注意力传播立体化学信息，在新构建的轴向手性基准上准确率提升 >7%。

**[Multi-Agent Design Optimizing Agents With Better Prompts And Topologies](multi-agent_design_optimizing_agents_with_better_prompts_and_topologies.md)**

:   深入分析多智能体系统中 prompt 和拓扑设计的影响，发现 prompt 优化是最关键的设计因素（仅优化 prompt 的单 Agent 即可超越复杂多 Agent 拓扑），提出 Mass 三阶段框架（block-level prompt → topology → workflow-level prompt）在 8 个 benchmark 上取得 SOTA。

**[Multi-Modal Data Spectrum Multi-Modal Datasets Are Multi-Dimensional](multi-modal_data_spectrum_multi-modal_datasets_are_multi-dimensional.md)**

:   大规模实证研究揭示23个VQA基准中存在严重的单模态依赖问题——许多为消除文本偏差而设计的基准反而引入了图像偏差，模型利用单模态捷径而非真正的跨模态推理。

**[Robust Preference Alignment Via Directional Neighborhood Consensus](robust_preference_alignment_via_directional_neighborhood_consensus.md)**

:   提出Robust Preference Selection (RPS)，一种无需重训练的推理时偏好对齐增强方法，通过从目标偏好的局部邻域采样多个候选方向并生成响应、再根据原始偏好选择最优响应，在OOD偏好上相比基线达到最高69%的胜率。

**[Spectrum Tuning Post-Training For Distributional Coverage And In-Context Steerab](spectrum_tuning_post-training_for_distributional_coverage_and_in-context_steerab.md)**

:   揭示RLHF/DPO等后训练会损害模型的上下文可操控性(in-context steerability)、输出覆盖率和分布对齐，提出Spectrum Suite评测框架和Spectrum Tuning方法，首次在后训练阶段改善分布对齐能力。
