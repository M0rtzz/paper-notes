---
title: >-
  ICLR2026 对话系统方向 4篇论文解读
description: >-
  4篇ICLR2026 对话系统方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🗣️ 对话系统

**🔬 ICLR2026** · 共 **4** 篇

**[Aqua Toward Strategic Response Generation For Ambiguous Visual Questions](aqua_toward_strategic_response_generation_for_ambiguous_visual_questions.md)**

:   提出 AQuA，首个按模糊度细粒度分级（4 级）的视觉问答数据集（7.2K 样本），为每级定义最优回应策略（直接回答/推断/列举/请求澄清），发现 GPT-5 和 Gemini 在模糊 VQA 上都过度自信地直接回答，通过 SFT+GRPO 训练的 3B 模型反而能超越闭源大模型的策略适应能力。

**[Non-Collaborative User Simulators For Tool Agents](non-collaborative_user_simulators_for_tool_agents.md)**

:   提出四类非协作用户行为模拟框架（不可用服务/跑题/不耐烦/不完整表述），在MultiWOZ和τ-bench上揭示SOTA工具Agent在面对非协作用户时性能显著下降（平均-29% tangential模式），暴露了幻觉增加和对话崩溃的系统性弱点。

**[Rein Conversational Error Recovery With Reasoning Inception](rein_conversational_error_recovery_with_reasoning_inception.md)**

:   提出 Reasoning Inception（ReIn），一种无需修改模型参数或系统提示的测试时干预方法，通过外部 inception 模块检测对话错误并将恢复计划注入任务 agent 的推理链中，在多种错误场景下显著提升对话任务完成率，且可泛化至未见错误类型。

**[Understanding Language Prior Of Lvlms By Contrasting Chain-Of-Embedding](understanding_language_prior_of_lvlms_by_contrasting_chain-of-embedding.md)**

:   通过对比有/无视觉输入的逐层隐藏表征（chain-of-embedding），发现LVLM中存在一个"视觉整合点"(VIP)层，并据此提出Total Visual Integration (TVI)指标来量化语言先验的强度。
