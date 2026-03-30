<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**📷 CVPR2025** · 共 **4** 篇

**[A Closed-Form Solution for Debiasing Vision-Language Models with Utility Guarantees Across Modalities and Tasks](a_closed-form_solution_for_debiasing_vision-language_models_with_utility_guarant.md)**

:   提出一个 training-free、data-free 的 VLM 去偏方法，通过在 cross-modal 空间中推导闭式解，实现 Pareto-optimal 的公平性与效用保持，在零样本分类、text-to-image 检索和生成三个下游任务中全面超越已有方法。

**[Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation](beyond_final_answers_crystal_benchmark_for_transparent_multimodal_reasoning_eval.md)**

:   提出 CRYSTAL benchmark（6372 实例），通过 Match F1 和 Ordered Match F1 两个指标在中间推理步骤层面评估 MLLM，揭示了普遍的 cherry-picking 行为和推理顺序混乱问题，并提出 CPR-Curriculum 训练策略改善推理质量。

**[Continual Learning with Vision-Language Models via Semantic-Geometry Preservation](continual_learning_with_vision-language_models_via_semantic-geometry_preservatio.md)**

:   提出 SeGP-CL 框架，通过对抗性锚点（DPGD）精准探测新旧任务语义边界的脆弱区域，结合跨模态几何蒸馏（ACGD）和文本语义正则化（TSGR）保护 VLM 的跨模态几何结构，在五个持续学习 benchmark 上达到 SOTA。

**[CleanSight: Test-Time Attention Purification for Backdoored Large Vision Language Models](test-time_attention_purification_for_backdoored_large_vision_language_models.md)**

:   CleanSight 发现 LVLM 后门攻击的机制不在像素层面而在注意力层面——触发器通过"注意力窃取"（trigger token 抢夺 text token 的注意力）来激活后门，据此提出了一种免训练、即插即用的 test-time 防御方法：通过检测跨模态注意力比例异常来识别中毒输入，再通过剪枝高注意力视觉 token 来中和后门，ASR 降至接近 0% 且几乎不影响模型性能。
