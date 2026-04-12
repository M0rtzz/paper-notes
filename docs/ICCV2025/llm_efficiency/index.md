---
title: >-
  ICCV2025 LLM效率方向 8篇论文解读
description: >-
  8篇ICCV2025 LLM效率方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM效率

**📹 ICCV2025** · 共 **8** 篇

**[Asynchronous Event Error-Minimizing Noise For Safeguarding Event Dataset](asynchronous_event_error-minimizing_noise_for_safeguarding_event_dataset.md)**

:   提出首个面向异步事件数据的不可学习样本生成方法（UEvs），设计了事件误差最小化噪声（E²MN）及自适应投影机制，使事件数据集在保持合法使用功能的同时阻止未授权模型从中学习。

**[Layertracer Cognitive-Aligned Layered Svg Synthesis Via Diffusion Transformer](layertracer_cognitive-aligned_layered_svg_synthesis_via_diffusion_transformer.md)**

:   LayerTracer 提出首个基于 Diffusion Transformer（DiT）的认知对齐分层 SVG 生成框架：通过构建 2 万+ 设计师操作序列数据集，训练 DiT 生成模拟设计师工作流程的多阶段光栅化蓝图，再通过逐层矢量化和路径去重转换为干净可编辑的分层 SVG；同时支持文本驱动生成和图像到分层 SVG 的转换。

**[Mixant Observation-Dependent Memory Propagation For Stochastic Dense Action Anti](mixant_observation-dependent_memory_propagation_for_stochastic_dense_action_anti.md)**

:   提出 MixANT，通过混合专家方法为 Mamba 的遗忘门（A 矩阵）引入输入依赖性，动态选择上下文相关的 A 矩阵控制时序记忆传播，在 50Salads、Breakfast 和 Assembly101 三个密集动作预测数据集上全面超越 SOTA。

**[Ock Unsupervised Dynamic Video Prediction With Object-Centric Kinematics](ock_unsupervised_dynamic_video_prediction_with_object-centric_kinematics.md)**

:   提出 OCK（Object-Centric Kinematics），在以对象为中心的视频预测中引入显式的运动学属性（位置、速度、加速度）作为 Slot 表示的补充，通过 Joint-OCK 和 Cross-OCK 两种 Transformer 变体融合外观与运动信息，在复杂合成和真实场景中显著提升动态视频预测质量。

**[Phatnet A Physics-Guided Haze Transfer Network For Domain-Adaptive Real-World Im](phatnet_a_physics-guided_haze_transfer_network_for_domain-adaptive_real-world_im.md)**

:   提出物理引导的雾迁移网络PHATNet，通过将大气散射模型（ASM）扩展到潜空间来解耦和迁移雾模式，生成域自适应的微调数据集，使去雾模型在测试时有效适应未见过的真实世界雾场景。

**[Rectifying Magnitude Neglect In Linear Attention](rectifying_magnitude_neglect_in_linear_attention.md)**

:   揭示 Linear Attention 完全忽略 Query 幅值信息导致注意力分数分布与 Softmax Attention 显著偏离，提出 Magnitude-Aware Linear Attention (MALA)，通过引入缩放因子 β 和偏移项 γ 使线性注意力恢复幅值感知能力，在分类、检测、分割、NLP、语音、图像生成等任务上全面超越现有方法。

**[Streammind Unlocking Full Frame Rate Streaming Video Dialogue Through Event-Gate](streammind_unlocking_full_frame_rate_streaming_video_dialogue_through_event-gate.md)**

:   StreamMind 提出"事件门控 LLM 调用"范式替代现有的"逐帧 LLM 调用"，通过在视频编码器和 LLM 之间插入认知门控网络（Cognition Gate），仅在查询相关事件发生时才调用 LLM，配合基于状态空间方法的事件保持特征提取器（EPFE）实现常量感知成本，在单张 A100 上达到 **100 fps** 的流式视频处理速度。

**[Stroke2Sketch Harnessing Stroke Attributes For Training-Free Sketch Generation](stroke2sketch_harnessing_stroke_attributes_for_training-free_sketch_generation.md)**

:   提出 Stroke2Sketch，一个无训练的参考式素描生成框架，通过跨图像笔触注意力（CSA）、指导性注意力模块（DAM）和语义保持模块（SPM）三个模块协同工作，在预训练扩散模型中实现精细的笔触属性迁移与内容结构保持。
