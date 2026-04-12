---
title: >-
  ICCV2025 LLM推理方向 4篇论文解读
description: >-
  4篇ICCV2025 LLM推理方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💡 LLM推理

**📹 ICCV2025** · 共 **4** 篇

**[Corvid Improving Multimodal Large Language Models Towards Ch](corvid_improving_multimodal_large_language_models_towards_ch.md)**

:   提出Corvid，通过混合视觉编码器+GateMixer连接器增强视觉表示、MCoT-Instruct-287K高质量CoT指令数据集+两阶段CoT训练增强推理能力、以及推理时自验证策略避免过度/不足推理，在数学推理和科学问题解决上超越同规模o1-like MLLM。

**[Corvid Improving Multimodal Large Language Models Towards Chain-Of-Thought Reaso](corvid_improving_multimodal_large_language_models_towards_chain-of-thought_reaso.md)**

:   提出 Corvid，通过混合视觉编码器 + GateMixer 连接器 + 高质量 CoT 数据集 + 推理时自验证策略，全面提升 MLLM 的链式推理能力，在数学推理和科学问题求解上超越同参数量级的开源模型。

**[Unsupervised Visual Chain-Of-Thought Reasoning Via Preference Optimization](unsupervised_visual_chain-of-thought_reasoning_via_preference_optimization.md)**

:   提出UV-CoT框架，通过自动生成偏好数据和改进的Score-DPO损失函数，在不需要人工标注bounding box的情况下实现图像级链式思维（Visual CoT）推理，在6个基准上超越有监督的Visual-CoT方法。

**[Video-T1 Test-Time Scaling For Video Generation](video-t1_test-time_scaling_for_video_generation.md)**

:   将LLM中的测试时缩放(TTS)思想迁移到视频生成领域，将TTS重新定义为从高斯噪声空间到目标视频分布的搜索问题，提出Tree-of-Frames (ToF)搜索算法实现高效的推理时计算扩展，在VBench上持续稳定提升各类视频生成模型的质量。
