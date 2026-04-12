---
title: >-
  NeurIPS2025 对话系统方向 5篇论文解读
description: >-
  5篇NeurIPS2025 对话系统方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🗣️ 对话系统

**🧠 NeurIPS2025** · 共 **5** 篇

**[Aclora Almost Trainingfree Access Controlaware Multimodal Ll](aclora_almost_trainingfree_access_controlaware_multimodal_ll.md)**

:   设计AC-LoRA系统，通过为不同权限数据集维护独立的LoRA适配器，并基于查询相似度和用户权限进行检索+无训练合并，实现企业级LLM聊天机器人的强信息隔离保证。

**[Bridging Human And Llm Judgments Understanding And Narrowing The Gap](bridging_human_and_llm_judgments_understanding_and_narrowing_the_gap.md)**

:   提出Bridge统计框架，通过序数logistic回归建模人类和LLM评判之间的潜在关系，以少量人类标签改善LLM评判的校准和对齐，同时支持对系统性偏差的正式统计检验。

**[Hygen Efficient Llm Serving Via Elastic Online-Offline Request Co-Location](hygen_efficient_llm_serving_via_elastic_online-offline_request_co-location.md)**

:   HyGen是干扰感知LLM推理系统，通过延迟预测和虚拟队列调度实现在线离线工作负载的弹性共置，保证SLO同时获得3.87-5.84倍吞吐改进。

**[Metamind Modeling Human Social Thoughts With Metacognitive Multi-Agent Systems](metamind_modeling_human_social_thoughts_with_metacognitive_multi-agent_systems.md)**

:   提出 MetaMind——一个受心理学元认知理论启发的多智能体框架，通过 ToM Agent（心理状态假设生成）、Moral Agent（社会规范约束精炼）和 Response Agent（响应生成与自我验证）三阶段协作，显著提升 LLM 的社会推理能力，在多个社会智能基准上达到 SOTA 并首次接近人类水平。

**[Sciarena An Open Evaluation Platform For Non-Verifiable Scientific Literature-Gr](sciarena_an_open_evaluation_platform_for_non-verifiable_scientific_literature-gr.md)**

:   构建SciArena——社区驱动的科学文献基础模型开放评估平台，支持47个模型和20K+偏好投票，同时发布SciArena-Eval元基准评估自动评估系统判断能力。
