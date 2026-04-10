<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🧪 ICML2025** · 共 **4** 篇

**[Eigenspectrum Analysis Of Neural Networks Without Aspect Ratio Bias](eigenspectrum_analysis_of_neural_networks_without_aspect_ratio_bias.md)**

:   论文提出 FARMS（Fixed-Aspect-Ratio Matrix Subsampling），通过固定长宽比子矩阵采样来消除权重特征谱分析中的长宽比偏差，从而显著提升基于 HT-SR 的分层学习率分配与模型剪枝效果。

**[Fourier Position Embedding: Enhancing Attention's Periodic Extension for Length Generalization](fourier_position_embedding_enhancing_attentions_periodic_extension_for_length_ge.md)**

:   从离散信号处理角度揭示RoPE通过隐式非均匀DFT实现周期注意力，发现线性层/激活函数和不充分训练的频率分量会破坏周期性，提出FoPE用傅里叶级数建模+零化有害频率分量来改善长度泛化。

**[Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](reward-augmented_data_enhances_direct_preference_alignment_of_llms.md)**

:   提出一种**奖励增强的数据重标注方法**，通过将偏好对条件化于奖励分数构建扩增数据集，使DPO能感知回复质量全谱，缓解高质量rejected回复被遗忘和低质量chosen回复被盲目学习的问题，在多个基准上一致性大幅提升DPO性能。

**[SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator](sepllm_accelerate_large_language_models_by_compressing_one_segment_into_one_sepa.md)**

:   SepLLM 发现分隔符 token（标点等）在注意力中占据主导地位，提出将文本段信息压缩到分隔符 token 中，通过数据依赖的稀疏注意力掩码仅保留 Initial + Separator + Neighboring tokens 的 KV cache，实现 50%+ 的 KV cache 压缩且性能几乎无损。
