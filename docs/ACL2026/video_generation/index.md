---
title: >-
  ACL2026 视频生成方向 3篇论文解读
description: >-
  3篇ACL2026 视频生成论文解读，主题涵盖：提出 Local Optimization +、提出 OSCBench——首个专门评估文生视频模型、提出 VideoRepair，首个免训练等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎬 视频生成

**💬 ACL2026** · **3** 篇论文解读

**[Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](accelerating_training_of_autoregressive_video_generation_models_via_local_optimi.md)**

:   提出 Local Optimization + Representation Continuity (ReCo) 训练策略，通过在局部窗口内优化并约束隐状态的平滑过渡，实现自回归视频生成模型训练速度提升 2 倍且不牺牲生成质量。

**[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](oscbench_benchmarking_object_state_change_in_text-to-video_generation.md)**

:   提出 OSCBench——首个专门评估文生视频模型中物体状态变化（OSC）能力的基准，基于烹饪场景构建 1,120 条提示覆盖常规/新颖/组合三类场景，揭示即使最强 T2V 模型在 OSC 准确率上也仅达 0.786。

**[Self-Correcting Text-to-Video Generation with Misalignment Detection and Localized Refinement](self-correcting_text-to-video_generation_with_misalignment_detection_and_localiz.md)**

:   提出 VideoRepair，首个免训练、模型无关的文本到视频自校正框架，通过 MLLM 检测细粒度文本-视频不对齐，保留正确区域并选择性修复问题区域，在 EvalCrafter 和 T2V-CompBench 上跨四种 T2V 骨干模型一致提升对齐质量。
