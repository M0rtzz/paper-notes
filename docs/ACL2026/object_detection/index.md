---
title: >-
  ACL2026 目标检测方向 18篇论文解读
description: >-
  18篇ACL2026 目标检测论文解读，主题涵盖：本文提出锚定循环生成（ACG）范式、提出AnchorMem记忆框架、提出 AHD（Anchor-based等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**💬 ACL2026** · **18** 篇论文解读

**[Anchored Cyclic Generation: A Novel Paradigm for Long-Sequence Symbolic Music Generation](anchored_cyclic_generation_a_novel_paradigm_for_long-sequence_symbolic_music_gen.md)**

:   本文提出锚定循环生成（ACG）范式，通过在自回归过程中用已确认的音乐内容作为锚点来校准生成方向，有效缓解长序列符号音乐生成中的误差累积问题，并构建了层次化框架Hi-ACG实现从全局到局部的音乐生成。

**[AnchorMem: Anchored Facts with Associative Contexts for Building Memory in Large Language Models](anchormem_anchored_facts_with_associative_contexts_for_building_memory_in_large_.md)**

:   提出AnchorMem记忆框架，受普鲁斯特现象启发，将检索单元（原子事实）与生成上下文（原始交互）解耦，通过关联事件图连接碎片化记忆，在LoCoMo基准上大幅超越A-Mem、Mem0等现有记忆系统。

**[Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models](breaking_block_boundaries_anchor-based_history-stable_decoding_for_diffusion_lar.md)**

:   提出 AHD（Anchor-based History-stable Decoding），一种无需训练的即插即用动态解码策略，通过动态锚点回溯历史轨迹判定扩散LLM中跨块稳定token，实现早期解锁，在BBH上减少80%解码步数的同时提升3.67%性能。

**[Debating the Unspoken: Role-Anchored Multi-Agent Reasoning for Half-Truth Detection](debating_the_unspoken_role-anchored_multi-agent_reasoning_for_half-truth_detecti.md)**

:   提出RADAR框架，通过角色锚定（政客 vs 科学家）的多智能体辩论来检测基于遗漏上下文的半真半假信息，配合双阈值自适应早停机制，在噪声检索条件下一致超越单智能体和传统多智能体基线。

**[E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition](e2e-gmner_end-to-end_generative_grounded_multimodal_named_entity_recognition.md)**

:   提出E2E-GMNER，首个将实体识别、语义分类、视觉定位和隐式知识推理统一在单一多模态大语言模型中的端到端GMNER框架，通过CoT推理自适应判断视觉/知识线索的可用性，并引入高斯风险感知框扰动（GRBP）提升生成式框预测的鲁棒性。

**[Evaluating Memory Capability in Continuous Lifelog Scenario](evaluating_memory_capability_in_continuous_lifelog_scenario.md)**

:   本文提出LifeDialBench，一个评估连续生活日志场景下记忆能力的基准（含7天真实数据的EgoMem和1年模拟的LifeMem），引入在线评估协议确保时间因果性，反直觉地发现简单RAG基线一致优于复杂记忆系统。

**[Evolutionary Negative Module Pruning for Better LoRA Merging](evolutionary_negative_module_pruning_for_better_lora_merging.md)**

:   提出 ENMP 方法，通过进化搜索策略发现并剪除 LoRA 合并中降低性能的"负面模块"，作为即插即用的增强手段，在 NLP 和视觉领域全面提升现有合并算法的效果。

**[GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR](geora_geometry-aware_low-rank_adaptation_for_rlvr.md)**

:   本文提出 GeoRA，一种专为强化学习可验证奖励（RLVR）设计的低秩适配方法，通过构建几何约束矩阵（融合谱先验和欧几里得先验）提取 RL 更新子空间的主方向进行 SVD 初始化，同时冻结残差矩阵作为结构锚，在 1.5B-32B 参数的 Qwen/Llama 模型上，数学、医学和代码 RLVR 任务中一致超越 LoRA、PiSSA、MiLoRA 等基线，且具备更强的域外泛化和更少的能力遗忘。

**[GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization](gigacheck_detecting_llm-generated_content_via_object-centric_span_localization.md)**

:   提出 GigaCheck，一个双策略框架：文档级使用微调 LLM 进行分类，片段级创新地将 AI 生成文本片段视为"目标"，用 DETR-like 架构实现端到端的字符级定位。

**[HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents](higmem_a_hierarchical_and_llm-guided_memory_system_for_long-term_conversational_.md)**

:   本文提出 HiGMem，一个两层事件-对话轮记忆系统，通过让 LLM 先浏览事件摘要再预测哪些细粒度对话轮值得读取，在 LoCoMo10 基准上以少一个数量级的检索量达到了五类问题中四类的最优 F1。

**[RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](racer_retrieval-augmented_contextual_rapid_speculative_decoding.md)**

:   RACER 提出了一种无需训练的推测解码方法，将基于检索的精确模式匹配与基于 logits 的未来预测统一起来，通过 copy-logit 策略构建 Logits Tree、LRU 驱逐的 AC 自动机构建 Retrieval Tree，在多个基准上实现了超过 2 倍的推理加速。

**[Retrievals Can Be Detrimental: Unveiling the Backdoor Vulnerability of Retrieval-Augmented Diffusion Models](retrievals_can_be_detrimental_unveiling_the_backdoor_vulnerability_of_retrieval-.md)**

:   提出 BadRDM，首个针对检索增强扩散模型（RDM）的后门攻击框架，通过恶意对比学习微调检索器建立触发词到毒性代理图像的捷径，在类条件和 T2I 两种任务中分别达到 90.9% 和 96.4% 攻击成功率，同时保持良性生成质量。

**[SOCIA-EVO: Automated Simulator Construction via Dual-Anchored Bi-Level Optimization](socia-evo_automated_simulator_construction_via_dual-anchored_bi-level_optimizati.md)**

:   本文提出 SOCIA-EVO，一种将自动化模拟器构建重新定义为双锚进化过程的 LLM 智能体框架，通过静态蓝图（Blueprint）锚定经验约束、双层优化解耦结构修正与参数校准、自我策划的策略剧本（Playbook）管理修复假说并通过执行反馈进行贝叶斯加权检索，在用户建模、口罩佩戴扩散和个人出行三个模拟任务上显著超越 Reflexion、G-SIM 等基线。

**[StructMem: Structured Memory for Long-Horizon Behavior in LLMs](structmem_structured_memory_for_long-horizon_behavior_in_llms.md)**

:   StructMem 提出了一种结构增强的层次化记忆框架，通过事件级双视角提取和跨事件语义整合，在 LoCoMo 长对话基准上实现 SOTA 性能（76.82%），同时大幅降低 token 消耗（1.94M vs. 图记忆的 35.8M）和 API 调用次数。

**[TEMA: Anchor the Image, Follow the Text for Multi-Modification Composed Image Retrieval](tema_anchor_the_image_follow_the_text_for_multi-modification_composed_image_retr.md)**

:   本文提出 TEMA（Text-oriented Entity Mapping Architecture），首个面向多修改文本的组合图像检索（CIR）框架，通过 MMT 解析助手（PA）增强修改实体覆盖、实体映射模块（EM）解决子句-实体对齐问题，并构建了 M-FashionIQ 和 M-CIRR 两个多修改基准数据集，在原始和多修改场景中均取得最优性能。

**[Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement](toward_consistent_world_models_with_multi-token_prediction_and_latent_semantic_e.md)**

:   从理论上分析了多 Token 预测（MTP）如何通过梯度耦合机制诱导表示收缩性从而促进信念状态的涌现，但同时揭示了 MTP 的"结构性幻觉"问题（隐空间中的非法捷径），并提出 LSE-MTP 框架通过隐一致性损失和语义锚定损失将预测锚定到真实隐状态轨迹，在合成图和真实曼哈顿出租车导航上显著改善路径合法性和鲁棒性。

**[Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations](two_pathways_to_truthfulness_on_the_intrinsic_encoding_of_llm_hallucinations.md)**

:   本文发现 LLM 内部编码真实性信号存在两条不同的信息通路：Question-Anchored（依赖问题到回答的信息流）和 Answer-Anchored（从生成答案本身提取自包含证据），两者与知识边界紧密关联，并据此提出 Mixture-of-Probes 和 Pathway Reweighting 两种通路感知的幻觉检测方法，AUC 提升达 10%。

**[When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated Text Detection](when_personalization_tricks_detectors_the_feature-inversion_trap_in_machine-gene.md)**

:   揭示了个性化场景下 MGT 检测器的"特征反转陷阱"——通用域中区分人写文本和机器文本的特征在个性化域中发生反转，导致检测器性能骤降甚至翻转，并提出 StyloCheck 框架通过量化检测器对反转特征的依赖程度来预测跨域性能变化，预测相关性达 0.85 以上。
