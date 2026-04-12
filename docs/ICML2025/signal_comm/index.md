---
title: >-
  ICML2025 信号/通信方向 5篇论文解读
description: >-
  5篇ICML2025 信号/通信方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🧪 ICML2025** · 共 **5** 篇

**[Eigenspectrum Analysis Of Neural Networks Without Aspect Ratio Bias](eigenspectrum_analysis_of_neural_networks_without_aspect_ratio_bias.md)**

:   论文提出 FARMS（Fixed-Aspect-Ratio Matrix Subsampling），通过固定长宽比子矩阵采样来消除权重特征谱分析中的长宽比偏差，从而显著提升基于 HT-SR 的分层学习率分配与模型剪枝效果。

**[Fourier Position Embedding Enhancing Attentions Periodic Extension For Length Ge](fourier_position_embedding_enhancing_attentions_periodic_extension_for_length_ge.md)**

:   从离散信号处理角度揭示RoPE通过隐式非均匀DFT实现周期注意力，发现线性层/激活函数和不充分训练的频率分量会破坏周期性，提出FoPE用傅里叶级数建模+零化有害频率分量来改善长度泛化。

**[Large Language Model Llm-Enabled In-Context Learning For Wireless Network Optimi](large_language_model_llm-enabled_in-context_learning_for_wireless_network_optimi.md)**

:   提出基于 LLM 上下文学习（In-context Learning）的基站功率控制算法，通过自然语言任务描述和经验池驱动的示例选择，在不更新模型参数的条件下达到接近传统深度强化学习的性能。

**[Reward-Augmented Data Enhances Direct Preference Alignment Of Llms](reward-augmented_data_enhances_direct_preference_alignment_of_llms.md)**

:   提出一种**奖励增强的数据重标注方法**，通过将偏好对条件化于奖励分数构建扩增数据集，使DPO能感知回复质量全谱，缓解高质量rejected回复被遗忘和低质量chosen回复被盲目学习的问题，在多个基准上一致性大幅提升DPO性能。

**[Sepllm Accelerate Large Language Models By Compressing One Segment Into One Sepa](sepllm_accelerate_large_language_models_by_compressing_one_segment_into_one_sepa.md)**

:   SepLLM 发现分隔符 token（标点等）在注意力中占据主导地位，提出将文本段信息压缩到分隔符 token 中，通过数据依赖的稀疏注意力掩码仅保留 Initial + Separator + Neighboring tokens 的 KV cache，实现 50%+ 的 KV cache 压缩且性能几乎无损。
