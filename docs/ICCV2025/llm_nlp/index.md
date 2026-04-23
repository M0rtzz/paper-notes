---
title: >-
  ICCV2025 LLM/NLP方向 5篇论文解读
description: >-
  5篇ICCV2025 LLM/NLP论文解读，主题涵盖：提出Analytic Subspace、提出Analytic Subspace、提出 VA-GPT，一个面向视频异常事件理解的多模等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM/NLP

**📹 ICCV2025** · **5** 篇论文解读

**[Any-SSR: How Recursive Least Squares Works in Continual Learning of Large Language Models](any-ssr_how_recursive_least_squares_works_in_continual_learning_of_large_languag.md)**

:   提出Analytic Subspace Routing（Any-SSR）框架，通过为每个任务分配独立的LoRA子空间消除任务间干扰，并利用递归最小二乘（RLS）闭式解训练一个零遗忘的解析路由器，实现LLM的无回放持续学习。

**[Any-SSR: How Recursive Least Squares Works in Continual Learning of Large Language Models](any_ssr_how_recursive_least_squares_works_in_continual_learning_of_large_language_models.md)**

:   提出Analytic Subspace Routing (Any-SSR)，为每个新任务分配独立的LoRA子空间以消除知识干扰，同时使用基于递归最小二乘(RLS)闭式解的分析路由器动态选择子空间，在理论上保证不遗忘先前任务知识，实现LLM的无重放持续学习。

**[VA-GPT: Aligning Effective Tokens with Video Anomaly in Large Language Models](va_gpt_aligning_effective_tokens_video_anomaly.md)**

:   提出 VA-GPT，一个面向视频异常事件理解的多模态大模型，通过空间有效token选择(SETS)和时间有效token生成(TETG)两个模块，让MLLM在空间和时间维度上精准对齐异常相关信息，在域内和跨域异常检测基准上均达到SOTA。

**[VIM: Versatile Interactive Motion-Language Model](vim_versatile_interactive_motion_language_model.md)**

:   提出 VIM，首个能在统一框架内同时理解和生成双人交互运动与文本的多模态大模型，配合82.7K多轮交互运动指令数据集 Inter-MT²，支持文本到运动、运动到文本、反应生成、运动编辑和运动推理等多种任务。

**[Zeroth-Order Fine-Tuning of LLMs in Random Subspaces](zeroth-order_fine-tuning_of_llms_in_random_subspaces.md)**

:   提出 SubZero（random Subspace Zeroth-order），通过逐层低秩扰动在随机子空间中估计梯度，显著降低零阶优化的梯度方差和角度误差，以接近推理的内存开销实现 LLM 的高效微调。
