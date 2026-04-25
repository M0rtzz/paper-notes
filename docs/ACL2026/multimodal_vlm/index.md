---
title: >-
  ACL2026 多模态VLM方向 16篇论文解读
description: >-
  16篇ACL2026 多模态VLM论文解读，主题涵盖：提出GPRO框架，通过元推理控制器在每个token、提出 AICA-Bench，一个涵盖情感理解（EU、定义了"基于自然语言指令在用户自定义模板上进行动态等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态VLM

**💬 ACL2026** · **16** 篇论文解读

**[Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](addressing_overthinking_in_large_vision-language_models_via_gated_perception-rea.md)**

:   提出GPRO框架，通过元推理控制器在每个token生成步动态路由计算到三条路径（快速/感知重检/推理反思），解决LVLM的过度思考问题，同时提升精度和效率。

**[AICA-Bench: Holistically Examining the Capabilities of VLMs in Affective Image Content Analysis](aica-bench_holistically_examining_the_capabilities_of_vlms_in_affective_image_co.md)**

:   提出 AICA-Bench，一个涵盖情感理解（EU）、情感推理（ER）和情感引导内容生成（EGCG）三个维度的综合基准，评估 23 个 VLM 后发现模型存在强度校准失败和描述浅薄两大缺陷，并提出 GAT Prompting 训练无关框架来缓解这些问题。

**[Automatic Slide Updating with User-Defined Dynamic Templates and Natural Language Instructions](automatic_slide_updating_with_user-defined_dynamic_templates_and_natural_languag.md)**

:   定义了"基于自然语言指令在用户自定义模板上进行动态幻灯片更新"的新任务，构建了包含 20,036 个指令-执行三元组的 DynaSlide 基准，并提出了 SlideAgent 作为强参考基线。

**[Benchmarking Deflection and Hallucination in Large Vision-Language Models](benchmarking_deflection_and_hallucination_in_large_vision-language_models.md)**

:   提出 VLM-DeflectionBench，一个包含 2775 个样本的多模态基准，通过四种评估场景（参数化/Oracle/现实/对抗）系统性地评估大型视觉语言模型在证据不足或误导时的拒答（deflection）vs 幻觉（hallucination）行为，实验覆盖 20 个 SOTA LVLM，发现几乎所有模型都无法在噪声证据下可靠拒答。

**[CogGen: A Cognitively Inspired Recursive Framework for Deep Research Report Generation](coggen_a_cognitively_inspired_recursive_framework_for_deep_research_report_gener.md)**

:   CogGen 提出一个模拟人类认知写作过程的多智能体递归框架，通过宏观认知循环实现全局重构、微观认知循环实现并行章节精炼、抽象视觉表示（AVR）实现文本-图表的语义级协同规划，在 OWID 基准上达到人类专家水平并超越 Gemini Deep Research。

**[Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games](collaborative_multi-agent_scripts_generation_for_enhancing_imperfect-information.md)**

:   提出一个协作式多智能体框架用于自动生成高质量剧本杀游戏脚本和训练数据，通过两阶段训练策略（CoT 微调 + GRPO 强化学习配合 ScoreAgent 奖励塑形）增强 VLM 在不完全信息下的多跳推理能力，在 WhodunitBench 上显著提升 VLM 的叙事推理、事实提取和欺骗抵御能力。

**[Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](don39t_act_blindly_robust_gui_automation_via_action-effect_verification_and_self.md)**

:   本文提出VeriGUI框架，通过Thinking-Verification-Action-Expectation（TVAE）闭环推理机制和两阶段训练管线（Robust SFT + GRPO），让GUI Agent能够验证每步操作是否成功并在失败时自我纠正，在3B和7B规模上均显著优于基线。

**[Dynamic Emotion and Personality Profiling for Multimodal Deception Detection](dynamic_emotion_and_personality_profiling_for_multimodal_deception_detection.md)**

:   本文指出现有欺骗检测数据集仅提供受试者级别的情感/人格标签（同一人所有样本共用标签），提出样本级动态标注方案和可靠性加权多模态融合框架 Rel-DDEP，在欺骗检测 F1 上提升 2.53%，情感检测提升 2.66%，人格检测提升 9.30%。

**[Efficient Inference for Large Vision-Language Models: Bottlenecks, Techniques, and Prospects](efficient_inference_for_large_vision-language_models_bottlenecks_techniques_and_.md)**

:   本文提出一个系统性的LVLM推理效率分类体系，围绕编码-预填充-解码三阶段推理流水线分析瓶颈，揭示了"视觉token主导"导致的系统性效率屏障，并梳理了从信息密度塑形、长上下文注意力管理到内存带宽突破的完整优化技术图谱。

**[Enhancing Multimodal Large Language Models for Ancient Chinese Character Evolution Analysis via Glyph-Driven Fine-Tuning](enhancing_multimodal_large_language_models_for_ancient_chinese_character_evoluti.md)**

:   本文构建了一个包含11个任务、13万+实例的古汉字演变分析基准，评估了19个MLLM后发现现有模型在字形级识别和演变推理上能力有限，并提出字形驱动对比微调框架GEVO，在2B模型上实现全任务提升。

**[FineSteer: A Unified Framework for Fine-Grained Inference-Time Steering in Large Language Models](finesteer_a_unified_framework_for_fine-grained_inference-time_steering_in_large_.md)**

:   FineSteer 将推理时转向分解为两个互补阶段：子空间引导的条件转向（SCS）决定"何时转向"——用 IR 查询子空间的能量比做门控；混合转向专家（MoSE）决定"如何转向"——通过注意力门控网络动态聚合原型专家+残差精炼生成查询特异性转向向量，在安全和真实性 benchmark 上超越 SOTA。

**[From Heads to Neurons: Causal Attribution and Steering in Multi-Task Vision-Language Models](from_heads_to_neurons_causal_attribution_and_steering_in_multi-task_vision-langu.md)**

:   提出 HONES 框架，通过先定位任务关键注意力头再以其为条件引导 FFN 神经元归因，实现了多任务 VLM 中跨异构任务的统一、无梯度的神经元级因果分析和轻量级任务性能提升。

**[Mitigating Hallucinations in Large Vision-Language Models without Performance Degradation](mitigating_hallucinations_in_large_vision-language_models_without_performance_de.md)**

:   本文提出 MPD 框架，通过语义感知正交子空间投影分离幻觉成分，并仅选择性更新与幻觉最相关的少量参数，在减少 23.4% 幻觉的同时保持 97.4% 的通用生成能力，不引入额外推理开销。

**[OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Models](omibench_benchmarking_olympiad-level_multi-image_reasoning_in_large_vision-langu.md)**

:   本文提出 OMIBench——首个面向奥赛级多图推理的大规模基准，涵盖生物、化学、数学、物理四学科超 1000 道竞赛题，发现即使最强 LVLM（Gemini-3-Pro）也仅达约 50% 准确率，比单图基准下降超 25%。

**[Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval](omni-embed-audio_leveraging_multimodal_llms_for_robust_audio-text_retrieval.md)**

:   本文提出 OEA（Omni-Embed-Audio），利用多模态 LLM 作为统一编码器构建检索导向的音频-文本嵌入空间，并引入 User-Intent Queries（UIQ）基准和硬负例区分指标（HNSR/TFR），发现 LLM 主干在 T2T 检索（+22%）和硬负例区分（+4.3%p HNSR@10）上显著优于 CLAP 系列方法。

**[SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models](safetyalfred_evaluating_safety-conscious_planning_of_multimodal_large_language_m.md)**

:   本文提出 SafetyALFRED 基准，在 ALFRED 具身任务中引入六类厨房安全隐患，揭示了多模态大语言模型在静态 QA 中能识别危险（最高 92%）但在具身规划中却难以主动缓解危险（<60%）的严重对齐差距，倡导从 QA 评估范式转向具身安全评估。
