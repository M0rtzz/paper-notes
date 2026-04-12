---
title: >-
  CVPR2025 多模态VLM方向 14篇论文解读
description: >-
  14篇CVPR2025 多模态VLM方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态VLM

**📷 CVPR2025** · 共 **14** 篇

**[4D Langsplat 4D Language Gaussian Splatting Via Multimodal Large Language Models](4d_langsplat_4d_language_gaussian_splatting_via_multimodal_large_language_models.md)**

:   提出4D LangSplat，通过多模态大语言模型生成逐物体视频caption来构建4D语言场，结合状态可变形网络建模语义的时间连续演变，首次实现动态场景中时间敏感和时间无关的开放词汇查询。

**[A Closed-Form Solution For Debiasing Vision-Language Models With Utility Guarant](a_closed-form_solution_for_debiasing_vision-language_models_with_utility_guarant.md)**

:   提出一个 training-free、data-free 的 VLM 去偏方法，通过在 cross-modal 空间中推导闭式解，实现 Pareto-optimal 的公平性与效用保持，在零样本分类、text-to-image 检索和生成三个下游任务中全面超越已有方法。

**[Active Data Curation Effectively Distills Large-Scale Multimodal Models](active_data_curation_effectively_distills_large-scale_multimodal_models.md)**

:   提出 ACID（主动数据筛选即隐式蒸馏）和 ACED（结合显式蒸馏），证明用大模型作为参考来主动筛选训练数据是一种比传统知识蒸馏更有效的多模态模型压缩方式，两者互补结合后在 27 个零样本任务上以更少推理 FLOPs 达到 SOTA。

**[Beyond Final Answers Crystal Benchmark For Transparent Multimodal Reasoning Eval](beyond_final_answers_crystal_benchmark_for_transparent_multimodal_reasoning_eval.md)**

:   提出 CRYSTAL benchmark（6372 实例），通过 Match F1 和 Ordered Match F1 两个指标在中间推理步骤层面评估 MLLM，揭示了普遍的 cherry-picking 行为和推理顺序混乱问题，并提出 CPR-Curriculum 训练策略改善推理质量。

**[Continual Learning With Vision-Language Models Via Semantic-Geometry Preservatio](continual_learning_with_vision-language_models_via_semantic-geometry_preservatio.md)**

:   提出 SeGP-CL 框架，通过对抗性锚点（DPGD）精准探测新旧任务语义边界的脆弱区域，结合跨模态几何蒸馏（ACGD）和文本语义正则化（TSGR）保护 VLM 的跨模态几何结构，在五个持续学习 benchmark 上达到 SOTA。

**[Espire A Diagnostic Benchmark For Embodied Spatial Reasoning Of Vision-Language ](espire_a_diagnostic_benchmark_for_embodied_spatial_reasoning_of_vision-language_.md)**

:   提出 Espire，一个基于仿真环境的具身空间推理诊断基准，将 VLM 评估分解为定位和执行两阶段，通过全生成式范式系统评估 VLM 在多种空间推理维度和粒度上的能力。

**[Forensiczip More Tokens Are Better But Not Necessary In Forensic Vision-Language](forensiczip_more_tokens_are_better_but_not_necessary_in_forensic_vision-language.md)**

:   发现语义驱动的视觉 token 剪枝会丢弃 forensic 证据（篡改痕迹在低显著性区域），提出 ForensicZip 用 Birth-Death 最优传输量化帧间物理不连续性 + 高频先验保留取证信号，在 10% token 保留率下实现 2.97x 加速、90%+ FLOPs 降低且性能不降。

**[Hificl High-Fidelity In-Context Learning For Multimodal Tasks](hificl_high-fidelity_in-context_learning_for_multimodal_tasks.md)**

:   通过对 attention 公式的精确分解，揭示 ICL 的效果本质上是 query-dependent 的标准自注意力输出与上下文 value 的动态混合，据此提出直接参数化"虚拟 KV 对"（低秩分解）来高保真模拟 ICL，仅 2.2M 参数即超越 MimIC/LoRA，且训练快 7.5 倍。

**[Mastering Negation Boosting Grounding Models Via Grouped Opposition-Based Learni](mastering_negation_boosting_grounding_models_via_grouped_opposition-based_learni.md)**

:   构建首个包含正负语义描述的视觉定位数据集 D-Negation，并提出 Grouped Opposition-Based Learning (GOBL) 微调机制，通过对立语义约束显著增强 grounding 模型对否定语义的理解能力。

**[Multimodal Ocr Parse Anything From Documents](multimodal_ocr_parse_anything_from_documents.md)**

:   提出 Multimodal OCR (MOCR) 范式，将文档中的文本和图形（图表、图标、UI 等）统一解析为结构化文本表示（包括 SVG 代码），3B 模型在 olmOCR-Bench 上达到 83.9 SOTA，图形解析超越 Gemini 3 Pro。

**[Revisiting Model Stitching In The Foundation Model Era](revisiting_model_stitching_in_the_foundation_model_era.md)**

:   系统研究异构 Vision Foundation Model（如 CLIP、DINOv2、SigLIP 2）之间的 stitchability，发现用 Final Feature Matching 预训练 stitch layer 可实现可靠拼接，并提出 VFM Stitch Tree 架构实现多 VFM 的高效共享。

**[Spatial Reasoning Is Not A Free Lunch A Controlled Study On Llava](spatial_reasoning_is_not_a_free_lunch_a_controlled_study_on_llava.md)**

:   通过在 LLaVA 框架中系统替换图像编码器（CLIP/SigLIP/SigLIP2/AIMv2）和引入 2D-RoPE 位置编码，发现 VLM 的空间推理能力主要由编码器的训练目标决定，指望仅靠 2D 位置结构改善空间理解是不够的。

**[Test-Time Attention Purification For Backdoored Large Vision Language Models](test-time_attention_purification_for_backdoored_large_vision_language_models.md)**

:   CleanSight 发现 LVLM 后门攻击的机制不在像素层面而在注意力层面——触发器通过"注意力窃取"（trigger token 抢夺 text token 的注意力）来激活后门，据此提出了一种免训练、即插即用的 test-time 防御方法：通过检测跨模态注意力比例异常来识别中毒输入，再通过剪枝高注意力视觉 token 来中和后门，ASR 降至接近 0% 且几乎不影响模型性能。

**[Topo-R1 Detecting Topological Anomalies Via Vision-Language Models](topo-r1_detecting_topological_anomalies_via_vision-language_models.md)**

:   发现现有 VLM（包括 GPT-5.2、Gemini-2.5）在拓扑异常检测上几乎为零（F1@0.5 < 1.5%），提出 Topo-R1 框架通过 SFT + GRPO（含拓扑感知复合 reward，集成 type-aware Hungarian matching + clDice）赋予 VLM 拓扑感知能力，最佳 F1@0.5 达 45.2%。
