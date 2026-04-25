---
title: >-
  CVPR2025 LLM/NLP方向 19篇论文解读
description: >-
  19篇CVPR2025 LLM/NLP论文解读，主题涵盖：提出 ALBM 模型，用属性化的类特定概念空间（A、从理论上揭示线性注意力性能不及 Softmax、提出 vHeat 视觉 backbone，将图像等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM/NLP

**📷 CVPR2025** · **19** 篇论文解读

**[Attribute-formed Class-specific Concept Space: Endowing Language Bottleneck Model with Better Interpretability and Scalability](attribute-formed_class-specific_concept_space_endowing_language_bottleneck_model.md)**

:   提出 ALBM 模型，用属性化的类特定概念空间（ACCS）取代现有语言瓶颈模型的类共享概念空间，避免虚假线索推理问题并支持跨类泛化，配合视觉属性提示学习（VAPL）提取细粒度属性特征，在 9 个 few-shot 基准上全面超越现有可解释分类方法。

**[Breaking the Low-Rank Dilemma of Linear Attention](breaking_the_low-rank_dilemma_of_linear_attention.md)**

:   从理论上揭示线性注意力性能不及 Softmax 注意力的根本原因是输出特征的低秩问题，提出秩增强线性注意力（RALA），通过增强 KV 缓存秩和输出特征秩两种互补策略，在保持线性复杂度的同时追平甚至超越 Softmax 注意力的表现。

**[Building Vision Models upon Heat Conduction](building_vision_models_upon_heat_conduction.md)**

:   提出 vHeat 视觉 backbone，将图像 patch 建模为热源，利用物理热传导方程通过 DCT/IDCT 变换实现 $O(N^{1.5})$ 复杂度的信息传播，在 ImageNet-1K 上以 3 倍吞吐量和 80% 更少 GPU 显存达到 84.0% top-1 准确率。

**[Chat-based Person Retrieval via Dialogue-Refined Cross-Modal Alignment](chat-based_person_retrieval_via_dialogue-refined_cross-modal_alignment.md)**

:   本文提出基于对话的行人检索（ChatPR）新范式，构建了首个对话-图像配对数据集ChatPedes，并设计了DiaNA框架通过自适应属性精炼器实现对话与图像间的细粒度跨模态对齐，显著优于传统单句文本检索方法。

**[ComRoPE: Scalable and Robust Rotary Position Embedding Parameterized by Trainable Commuting Angle Matrices](comrope_rotary_position.md)**

:   本文提出ComRoPE，通过将RoPE推广为由可训练交换角矩阵参数化的旋转位置编码，理论证明了角矩阵的成对交换性是RoPE满足相对位置依赖性的充要条件，在ImageNet-1K上比SOTA方法LieRE提升1.6%（训练分辨率）和2.9%（更高分辨率）。

**[ComRoPE: Scalable and Robust Rotary Position Embedding Parameterized by Trainable Commuting Angle Matrices](comrope_scalable_and_robust_rotary_position_embedding_parameterized_by_trainable.md)**

:   ComRoPE将RoPE从固定的2D旋转矩阵推广到SO(n)群的更大子群，证明交换性是保持相对位置鲁棒性的充要条件，提出AP和LD两种可训练参数化方案，在ImageNet分类（+1.6%）、COCO检测（+0.2 AP）上均优于LieRE。

**[LLM4SVG: Empowering LLMs to Understand and Generate Complex Vector Graphics](empowering_llms_to_understand_and_generate_complex_vector_graphics.md)**

:   提出 LLM4SVG 框架，通过定义 55 个可学习的 SVG 语义 token 替代原始 XML 标签，结合 250K 高质量 SVG 和 580K 指令数据的 SVGX-SFT 数据集进行两阶段指令微调，使 GPT-2、Phi-2、Falcon 等开源 LLM 能高质量理解和生成复杂矢量图形，GPT-2 XL 版本达 FID 64.11、CLIPScore 0.3496，大幅超越 GPT-4o（127.78 FID）和所有现有 SVG 生成方法。

**[Exposure-slot: Exposure-centric Representations Learning with Slot-in-Slot Attention](exposure-slot_exposure-centric_representations_learning_with_slot-in-slot_attent.md)**

:   本文提出Exposure-slot框架，将Slot Attention算法扩展为层次化的slot-in-slot结构，通过可学习的曝光prompt引导特征聚类，实现以曝光为中心的区域感知表征学习，在欠曝/过曝图像矫正任务上取得SOTA性能。

**[Guiding Human-Object Interactions with Rich Geometry and Relations](guiding_human-object_interactions_with_rich_geometry_and_relations.md)**

:   本文提出ROG框架，通过在物体网格上采样富含几何信息的关键点构建交互距离场（IDF），并利用基于扩散的关系模型在推理时引导运动生成模型产生关系感知且语义对齐的人物-物体交互动作，在FullBodyManipulation数据集上显著超越SOTA。

**[Imagine and Seek: Improving Composed Image Retrieval with an Imagined Proxy](imagine_and_seek_improving_composed_image_retrieval_with_an_imagined_proxy.md)**

:   提出IP-CIR方法，通过大语言模型生成"想象中的目标图像描述"作为代理，将组合图像检索(CIR)转化为标准图像检索问题，在CIRR和FashionIQ等基准上达到零样本SOTA。

**[Learning Textual Prompts for Open-World Semi-Supervised Learning](learning_textual_prompts_for_open-world_semi-supervised_learning.md)**

:   本文提出了一种针对开放世界半监督学习（OWSSL）的新方法，通过全局-局部文本提示学习策略增强图文对齐效果，并设计前向-反向策略降低无标签样本中图文匹配的噪声，在多个细粒度数据集上显著超越SOTA。

**[Let Samples Speak: Mitigating Spurious Correlation by Exploiting the Clusterness](let_samples_speak_mitigating_spurious_correlation_by_exploiting_the_clusterness_.md)**

:   提出NSF方法，通过利用样本在特征空间中的聚类特性自动识别依赖虚假特征的样本组，无需组标注即可训练出对虚假相关性鲁棒的分类器，最差组准确度显著超越ERM基线。

**[Rethinking Spiking Self-Attention Mechanism: Implementing a-XNOR Similarity Calculation in Spiking Transformers](rethinking_spiking_self-attention_mechanism_implementing_a-xnor_similarity_calcu.md)**

:   本文深入分析了点积在脉冲查询-键对中因大量"非脉冲事件"导致相似度度量失效的根本原因，提出专为脉冲序列设计的a-XNOR相似度度量，将非脉冲对的相关性重定义为特定值a，在多种脉冲Transformer架构和数据集上显著提升性能。

**[Robust Message Embedding via Attention Flow-Based Steganography](robust_message_embedding_via_attention_flow-based_steganography.md)**

:   本文提出RMSteg（Robust Message Steganography）框架，首次将Transformer注意力机制集成到归一化流网络中（AttnFlow），配合可逆QR码转换和可逆Token融合模块，实现了高质量、高容量且鲁棒的消息-图像隐写，隐写图像即使经过打印-拍照等极端扭曲仍可准确解码。

**[SEC-Prompt: SEmantic Complementary Prompting for Few-Shot Class-Incremental Learning](sec-promptsemantic_complementary_prompting_for_few-shot_class-incremental_learni.md)**

:   提出 SEC-Prompt（SEmantic Complementary Prompt）框架，学习两组语义互补的提示——判别性提示（D-Prompt）和非判别性提示（ND-Prompt），通过自适应查询机制协同工作，分别强化类间区分和促进新类泛化，在三个基准数据集上取得 SOTA 性能。

**[Spiking Transformer with Spatial-Temporal Attention](spiking_transformer_with_spatial-temporal_attention.md)**

:   将空间-时间注意力机制融入脉冲Transformer架构，通过时空解耦的注意力设计和脉冲驱动的自注意机制，在保持SNN能效优势的同时缩小与ANN的性能差距，在多个视觉基准上达到SNN SOTA。

**[STAA-SNN: Spatial-Temporal Attention Aggregator for Spiking Neural Networks](staa-snn_spatial-temporal_attention_aggregator_for_spiking_neural_networks.md)**

:   通过在SNN中集成全局上下文自注意(GC)、位置编码(PE)、步骤注意(SA)和时间步随机退出(TSRD)四大模块，STAA-SNN在CIFAR-10/100和ImageNet上达到97.14%/82.05%/70.40%的SNN SOTA性能。

**[Test-Time Visual In-Context Tuning](test-time_visual_in-context_tuning.md)**

:   本文提出VICT（Visual In-Context Tuning），通过翻转任务提示和测试样本的角色并利用循环一致性损失，在测试时对视觉上下文学习模型（如Painter）进行单样本自适应，显著提升其在分布偏移下的泛化能力。

**[The Change You Want To Detect: Semantic Change Detection In Earth Observation With Hybrid Data Generation](the_change_you_want_to_detect_semantic_change_detection_in_earth_observation_wit.md)**

:   本文提出HySCDG（Hybrid Semantic Change Detection Data Generation），一种混合数据生成流水线，结合真实超高分辨率（VHR）遥感影像和图像inpainting技术生成大规模语义变化检测训练数据，在简洁的架构设计下实现了强大的时间和空间泛化能力。
