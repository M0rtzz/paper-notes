---
title: >-
  ACL2025 LLM效率方向 30篇论文解读
description: >-
  30篇ACL2025 LLM效率方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM效率

**💬 ACL2025** · 共 **30** 篇

**[Adaptive Grouped Pe Context Window](adaptive_grouped_pe_context_window.md)**

:   提出 AdaGroPE（Adaptive Grouped Positional Encoding），一种无需训练的即插即用方法，通过让位置复用次数随距离递增式增长、并根据输入序列长度动态调整位置编码映射，将 LLM 上下文窗口外推到远超预训练长度，在多个 benchmark 上达到 SOTA 甚至超过原生长上下文模型。

**[Clasp Self Speculative Decoding](clasp_self_speculative_decoding.md)**

:   CLaSp 提出一种无需训练的自推测解码方法，通过动态规划算法在每个验证步骤后根据上下文动态调整跳层策略，利用上一次验证的完整隐状态作为目标来选择最优跳层集合，在 LLaMA3 系列上实现 1.3-1.7× 加速且不改变生成分布。

**[Cnnsum Exploring Long-Context Summarization With Large Language Models In Chines](cnnsum_exploring_long-context_summarization_with_large_language_models_in_chines.md)**

:   构建了 CNNSum——基于中文小说的多尺度长文本摘要基准（695 样本，16k-128k tokens），通过人工标注确保质量，系统测评了 20+ 个 LLM，发现高级 LLM 倾向生成主观评述导致摘要模糊、小模型性价比更高、Base 版微调效果优于 Chat 版，且用短文本数据微调即可显著提升长文本摘要能力。

**[Design Choices For Extending The Context Length Of Visual Language Models](design_choices_for_extending_the_context_length_of_visual_language_models.md)**

:   系统性地探索了将现有视觉语言模型（VLM）的上下文窗口扩展到128K的设计空间，从数据配方、位置编码扩展到上下文利用三个维度提出最佳实践，并提出 M-RoPE++ 和混合分辨率训练两项技术，构建的 Giraffe 模型在长上下文 VLM 中达 SOTA。

**[Dynamic Chunking And Selection For Reading Comprehension Of Ultra-Long Context I](dynamic_chunking_and_selection_for_reading_comprehension_of_ultra-long_context_i.md)**

:   提出 Dynamic Chunking and Selection (DCS)，通过基于语义相似度的动态分块和问题感知分类器的块选择，解决长文本固定分块导致的语义断裂问题，在 12 个长文本 QA 数据集上以 Llama3 为基座实现 single-hop 平均 35.50（+28.6%）和 multi-hop 平均 29.07（+20.0%）的提升，且在 256k token 输入下保持鲁棒。

**[Efficient Many-Shot In-Context Learning With Dynamic Block-Sparse Attention](efficient_many-shot_in-context_learning_with_dynamic_block-sparse_attention.md)**

:   提出 Dynamic Block-Sparse Attention (DBSA)，一种无需训练的推理框架，通过结构化块稀疏注意力编码和动态检索 KV 缓存，在多示例上下文学习中实现接近微调的推理延迟，同时保持 >95% 的最佳方法准确率。

**[Entailment-Preserving First-Order Logic Representations In Natural Language Enta](entailment-preserving_first-order_logic_representations_in_natural_language_enta.md)**

:   形式化定义了蕴含保持一阶逻辑表示（EPF）任务及无参考评价指标（EPR系列），提出迭代learning-to-rank训练方法，通过BRIO损失优化T5模型的NL→FOL翻译，使其生成的FOL表示能被自动定理证明器验证蕴含关系，在三个数据集上EPR提升1.8-2.7%、EPR@16提升17.4-20.6%。

**[Focusllm Precise Understanding Of Long Context By Dynamic Condensing](focusllm_precise_understanding_of_long_context_by_dynamic_condensing.md)**

:   提出FocusLLM框架，通过将长文本分块并为每块注入动态提示（dynamic prompt），用可训练的候选token浓缩各块的关键信息，再通过并行解码机制聚合到本地上下文中生成下一个token，仅用8K训练长度和0.5B训练预算即可扩展LLaMA-2到400K上下文，在LongBench和∞-Bench上超越所有基线。

**[Gigachat Family Efficient Russian Language Modeling Through Mixture Of Experts A](gigachat_family_efficient_russian_language_modeling_through_mixture_of_experts_a.md)**

:   介绍 GigaChat 系列——首个从头为俄语设计并预训练的 MoE 架构 LLM 家族，包含 20B 总参数/3.3B 激活参数的基座和指令微调模型，在俄语 benchmark 上达到同规模 SOTA，训练速度是同量级 dense 模型的 2 倍，推理延迟降低 40%。

**[Gradot Offsite Tuning](gradot_offsite_tuning.md)**

:   从优化理论角度首次系统分析 Offsite-tuning 问题，提出梯度保持压缩分数（GCS），并基于此设计了 GradOT 方法，对 MHA 使用动态秩分解（DRD）、对 MLP 使用选择性通道剪枝（SCP），在免训练条件下同时实现性能保持和隐私保护。

**[Kv Latent Cache Reduction](kv_latent_cache_reduction.md)**

:   提出KV-Latent范式，通过对KV头的维度进行降采样将其映射到潜空间，仅需不到1%预训练量的额外训练即可恢复性能，在LLaMA-3-8B上KV Cache减少50%（dqk=dvo=64→50%缓存），同时TTFT延迟降低8%。

**[Ladm Long Context Data](ladm_long_context_data.md)**

:   提出 LADM 框架，利用注意力机制的内在检索能力来度量长上下文数据中的跨 span 依赖关系，从大规模预训练语料中高效筛选高质量长上下文训练数据，仅用 1B token 持续预训练即可显著提升多种 LLM 的长上下文能力。

**[Literary Evidence Retrieval Via Long-Context Language Models](literary_evidence_retrieval_via_long-context_language_models.md)**

:   将 RELiC 数据集改造为长上下文文学证据检索 benchmark（292 个高质量样本），要求模型在完整小说文本（45k-125k tokens）中为文学评论找到缺失引用；Gemini Pro 2.5 以 62.5% 准确率首次超越人类专家（55%），但最佳开源模型 DeepSeek-R1 仅 29.1%，揭示了闭源/开源模型在解释性推理上的巨大鸿沟。

**[Longreward Improving Long-Context Large Language Models With Ai Feedback](longreward_improving_long-context_large_language_models_with_ai_feedback.md)**

:   提出 LongReward，利用现成LLM从帮助性、逻辑性、忠实性和完整性四个维度为长上下文模型回复自动打分，结合DPO实现长上下文SFT模型的进一步提升。

**[Longsafety Evaluating Long-Context Safety Of Large Language Models](longsafety_evaluating_long-context_safety_of_large_language_models.md)**

:   提出LongSafety——首个专门针对开放式长上下文任务的LLM安全评估基准，包含7类安全问题和6种任务类型共1,543个测试用例，揭示大多数模型安全率低于55%，且短上下文安全能力无法迁移到长上下文场景。

**[Many Shot Attacks Long Context](many_shot_attacks_long_context.md)**

:   系统分析 Many-Shot Jailbreaking（MSJ）攻击的关键因素，发现上下文长度是攻击成功的决定性因素，而内容的有害性、主题、格式几乎不重要——即使重复安全内容、随机无意义文本（Lorem Ipsum）都能在长上下文下突破模型安全对齐。

**[Mitigating Posterior Salience Attenuation In Long-Context Llms With Positional C](mitigating_posterior_salience_attenuation_in_long-context_llms_with_positional_c.md)**

:   发现长上下文LLM中的后验显著性衰减（PSA）现象——gold token的显著性随上下文增长而下降但仍保持高排名，由此提出无需训练的位置对比解码（PCD）方法，通过对比长距离感知注意力和局部感知注意力的logits来放大长距离信号，在多个长上下文基准上取得SOTA。

**[Native Sparse Attention](native_sparse_attention.md)**

:   DeepSeek提出NSA——一种原生可训练的稀疏注意力机制，通过"压缩+选择+滑动窗口"的层次化稀疏策略和硬件对齐的Triton kernel设计，在27B参数模型上实现了超越Full Attention的性能，同时在64k序列上获得前向9倍、解码11.6倍的加速。

**[Neko Cross-Modality Post-Recognition Error Correction With Tasks-Guided Mixture-](neko_cross-modality_post-recognition_error_correction_with_tasks-guided_mixture-.md)**

:   提出 NeKo，使用任务引导的 Mixture-of-Experts 语言模型进行跨模态后识别纠错（ASR/ST/OCR/TEC），通过将每个专家指派给特定任务的数据集实现专业化，在 Open ASR Leaderboard 上达到 SOTA，零样本下超越 GPT-3.5 和 Claude-3.5。

**[On Many-Shot In-Context Learning For Long-Context Evaluation](on_many-shot_in-context_learning_for_long-context_evaluation.md)**

:   深入研究 many-shot ICL 用于长上下文语言模型评估，提出 Sample Learning Ratio 指标区分 SSL 和 ASL 任务，构建 ManyICLBench 基准全面评测 12 个 LCLM。

**[Ref-Long Benchmarking The Long-Context Referencing Capability Of Long-Context La](ref-long_benchmarking_the_long-context_referencing_capability_of_long-context_la.md)**

:   提出 Ref-Long benchmark，从"引用定位"（给定 key 识别哪些文档引用了它并返回索引）这一被忽视的维度评估长上下文模型，包含 3 个子集（合成→真实）共 4300 个任务；发现即使 GPT-4o 在 Multi-Hard-24K 上 ExAcc 仅 19%，远低于人类 92%，且 prompt 工程和专项微调均无法根本解决该问题。

**[Refreshkv Updating Small Kv Cache During Long-Form Generation](refreshkv_updating_small_kv_cache_during_long-form_generation.md)**

:   提出RefreshKV推理方法，通过在生成过程中周期性地在全KV缓存注意力和小KV缓存注意力之间交替，并基于全注意力步的注意力模式动态更新小KV缓存，在不永久丢弃任何token的前提下，实现与驱逐式方法相当的加速且大幅提升长文本生成任务性能。

**[Robust Utility-Preserving Text Anonymization Based On Large Language Models](robust_utility-preserving_text_anonymization_based_on_large_language_models.md)**

:   提出RUPTA框架，通过隐私评估器、效用评估器和优化器三个LLM组件协同工作，迭代编辑文本以实现防御LLM重识别攻击的同时保留下游任务效用，并通过DPO蒸馏将匿名化能力迁移到轻量模型。

**[Sam Decoding Speculative Decoding Via Suffix Automaton](sam_decoding_speculative_decoding_via_suffix_automaton.md)**

:   提出SAM-Decoding，利用后缀自动机（Suffix Automaton）对通用文本语料和当前文本序列进行最长后缀匹配来高效生成推测解码的草稿，平均O(1)时间复杂度，在Spec-Bench上比现有检索式方法快18%+，并可与EAGLE-2等方法互补组合进一步提速3.28%-11.13%。

**[Scaling Context Not Parameters Training A Compact 7B Language Model For Efficien](scaling_context_not_parameters_training_a_compact_7b_language_model_for_efficien.md)**

:   提出 MegaBeam-Mistral-7B，一个支持 512K token 上下文长度的 7B 语言模型，通过四阶段渐进式训练、RoPE theta 调优、bfloat16 精度修复和 XLA 编译器内存优化等工程实践，使紧凑型模型在长上下文任务上达到甚至超越大参数模型（如 Llama-3.1-70B、GPT-4）的性能。

**[Sliding Windows Full Ranking](sliding_windows_full_ranking.md)**

:   本文系统研究了长上下文LLM在段落排序中的应用，提出用 full ranking（一次性排序所有段落）替代传统滑动窗口策略，并设计了多轮滑动窗口标签构造方法和重要性感知损失函数来微调 full ranking 模型，在效率提升约30-65%的同时实现了排序效果的全面超越。

**[Smarter Better Faster Longer A Modern Bidirectional Encoder For Fast Memory Effi](smarter_better_faster_longer_a_modern_bidirectional_encoder_for_fast_memory_effi.md)**

:   提出 ModernBERT，将现代 LLM 架构优化（RoPE、GeGLU、交替局部/全局注意力、unpadding）系统性地引入 encoder-only 模型，在 2T token 上训练并原生支持 8192 上下文长度，在分类和检索任务上全面超越 BERT/RoBERTa/DeBERTaV3，同时推理速度和显存效率大幅领先。

**[Spindlekv Layered Kv Cache](spindlekv_layered_kv_cache.md)**

:   SpindleKV 提出分层处理 KV cache 压缩的策略——深层使用注意力驱动的 token eviction（利用稀疏注意力），浅层使用基于相似性学习的 codebook 替换（利用 token 间高相似度），并解决了 GQA 兼容性问题，实现 50% KV cache 缩减而不损失性能。

**[Train Long Context Effectively](train_long_context_effectively.md)**

:   本文系统研究了如何通过持续预训练和监督微调（SFT）有效训练长上下文语言模型，提出了包括数据配比、训练长度缩放等一系列关键发现，最终训练出的 ProLong-8B 模型仅用 Llama-3.1 5% 的长上下文训练数据量即在 128K 长度上达到同规模最优性能。

**[What Are The Essential Factors In Crafting Effective Long Context Multi-Hop Inst](what_are_the_essential_factors_in_crafting_effective_long_context_multi-hop_inst.md)**

:   提出多智能体交互式多跳生成（MIMG）框架，通过质量验证、单跳问题生成、多问题采样和多跳合并四个模块，系统性地合成高质量长上下文多跳指令数据，训练后模型平均提升7.54%，甚至超越更大规模人工标注数据集。
