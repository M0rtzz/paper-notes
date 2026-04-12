---
title: >-
  CVPR2026 信号/通信方向 4篇论文解读
description: >-
  4篇CVPR2026 信号/通信方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**📷 CVPR2026** · 共 **4** 篇

**[Actta Rethinking Test-Time Adaptation Via Dynamic Activation](actta_rethinking_test-time_adaptation_via_dynamic_activation.md)**

:   提出AcTTA框架，首次将激活函数作为测试时适应(TTA)的可学习组件，通过参数化的激活中心偏移 $c$ 和非对称梯度缩放 $\lambda_{pos}, \lambda_{neg}$ 替代或增强传统归一化层适应，在CIFAR-10/100-C和ImageNet-C上一致超越所有归一化基TTA方法，并支持10倍大的学习率。

**[Chartnet A Million-Scale High-Quality Multimodal Dataset For Robust Chart Unders](chartnet_a_million-scale_high-quality_multimodal_dataset_for_robust_chart_unders.md)**

:   发布 ChartNet——150 万规模的高质量多模态图表数据集，通过代码引导合成管线生成包含图像-代码-数据表-文本-推理QA 的对齐五元组，在图表理解和推理任务上显著提升 VLM 性能，小模型微调后超越 GPT-4o。

**[Dual-Imbalance Continual Learning For Real-World Food Recognition](dual-imbalance_continual_learning_for_real-world_food_recognition.md)**

:   提出 DIME 框架，通过类别计数引导的光谱适配器合并和秩自适应阈值调制机制，在双重不平衡（类内长尾分布 + 步间类别数不均匀）的持续学习场景下，在四个长尾食物数据集上持续超越 baseline 3% 以上。

**[Faar Efficient Frequency-Aware Multi-Task Fine-Tuning Via Automatic Rank Selecti](faar_efficient_frequency-aware_multi-task_fine-tuning_via_automatic_rank_selecti.md)**

:   提出 FAAR，一种频率感知的多任务参数高效微调方法，通过 Performance-Driven Rank Shrinking (PDRS) 为每个任务和层动态选择最优秩，并设计 Task-Spectral Pyramidal Decoder (TS-PD) 利用 FFT 频率信息增强空间感知和跨任务一致性，以传统微调 1/9 的参数量实现更优性能。
