---
title: >-
  CVPR2025 LLM评测方向 11篇论文解读
description: >-
  11篇CVPR2025 LLM评测方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📊 LLM评测

**📷 CVPR2025** · **11** 篇论文解读

**[Comfybench Benchmarking Llm-Based Agents In Comfyui For Autonomously Designing C](comfybench_benchmarking_llm-based_agents_in_comfyui_for_autonomously_designing_c.md)**

:   ComfyBench 提出了首个评估LLM Agent在ComfyUI中自主设计协作AI系统能力的综合性Benchmark（200个任务、3205个节点文档、20个课程工作流），并提出ComfyAgent框架通过代码化工作流表示和多Agent协作，达到了与o1-preview相当的解决率，但在创意任务上仅解决15%，揭示了LLM Agent在自主系统设计上的巨大差距。

**[Context-Cir Learning From Concepts In Text For Composed Image Retrieval](context-cir_learning_from_concepts_in_text_for_composed_image_retrieval.md)**

:   提出 ConText-CIR 框架，通过 Text Concept-Consistency 损失让文本修改中的名词短语更好地关注查询图像的相关部分，配合合成数据生成管线，在多个 CIR 基准上取得 SOTA。

**[Do Imagenet-Trained Models Learn Shortcuts The Impact Of Frequency Shortcuts On ](do_imagenet-trained_models_learn_shortcuts_the_impact_of_frequency_shortcuts_on_.md)**

:   提出层次化频率捷径搜索方法（HFSS），首次在ImageNet-1K规模上高效发现CNN和Transformer学到的频率捷径（仅5%频率即可正确分类），揭示频率捷径在保留纹理的OOD测试中反而有益但在风格化测试（IN-R/IN-S）上有害，指出现有OOD评估框架忽视了频率捷径的影响。

**[Dual Consolidation For Pre-Trained Model-Based Domain-Incremental Learning](dual_consolidation_for_pre-trained_model-based_domain-incremental_learning.md)**

:   提出Duct方法，通过表征合并（累加任务向量构建统一嵌入空间）和分类器合并（利用类别语义信息通过最优传输估计旧域分类器权重），在预训练模型基础上实现无样本存储的域增量学习，在四个基准上以1~7%的优势超越SOTA。

**[Erase Diffusion Empowering Object Removal Through Calibrating Diffusion Pathways](erase_diffusion_empowering_object_removal_through_calibrating_diffusion_pathways.md)**

:   本文提出EraDiff，通过链式校正优化范式（CRO）建立从"含物体"到"纯背景"的渐进扩散路径，并用自校正注意力机制（SRA）在采样时抑制伪影，使扩散模型真正理解"擦除意图"，在OpenImages V5上取得SOTA的Local FID（3.799），在复杂真实场景中显著优于SD2-Inpaint和LaMa。

**[Event Ellipsometer Event-Based Mueller-Matrix Video Imaging](event_ellipsometer_event-based_mueller-matrix_video_imaging.md)**

:   首个实现 30fps 视频级穆勒矩阵成像的系统——用事件相机捕捉快速旋转 QWP 产生的光强调制，将事件时间差映射到穆勒矩阵比值，通过 SVD 估计+时空传播重建物理有效的穆勒矩阵视频。

**[Gradient-Guided Annealing For Domain Generalization](gradient-guided_annealing_for_domain_generalization.md)**

:   提出GGA方法，在训练早期通过模拟退火搜索参数空间中梯度跨域对齐的点（最小化域间梯度余弦相似度的最小值），引导模型在优化初期找到域不变特征的起始点，从而在无需数据增强的情况下提升域泛化性，可与现有DG方法组合获得显著提升。

**[Lotus Large-Scale Machine Unlearning With A Taste Of Uncertainty](lotus_large-scale_machine_unlearning_with_a_taste_of_uncertainty.md)**

:   提出 LoTUS，用 logits 温度调节+Gumbel-Softmax 平滑遗忘样本的预测，通过动态温度调度收敛到"遗忘集准确率=未见集准确率"的目标——在 ImageNet-1K 大规模设置中高效遗忘（ViT 上 Avg Gap 0.0150），且提出 RF-JSD 免重训评估指标（与 JSD Pearson 相关 0.92）。

**[Out Of Sight Out Of Mind Evaluating State Evolution In Video World Models](out_of_sight_out_of_mind_evaluating_state_evolution_in_video_world_models.md)**

:   StEvo-Bench 提出了一个评估视频世界模型"不可观测状态演化"能力的 benchmark——测试当物理过程不被观察时（相机移开/遮挡/关灯），世界模型能否继续正确推理状态变化，结果发现当前所有前沿模型（Veo 3、Sora 2 Pro 等）的任务成功率均低于 10%，揭示了"眼不见，心不在"的严重缺陷。

**[Potential Field Based Deep Metric Learning](potential_field_based_deep_metric_learning.md)**

:   提出 PFML，用物理势能场概念替代传统的 tuple mining 进行度量学习——每个样本在嵌入空间中创建连续的引力场（同类）和斥力场（异类），具有距离衰减特性（远处交互力弱），在 Cars-196 上 R@1 达 92.7%（前 SOTA 89.6%）。

**[Traf-Align Trajectory-Aware Feature Alignment For Asynchronous Multi-Agent Perce](traf-align_trajectory-aware_feature_alignment_for_asynchronous_multi-agent_perce.md)**

:   提出TraF-Align框架，通过预测特征级目标轨迹来学习特征的流动路径，生成沿时间排列的采样点将当前时刻query引导至相关历史特征，解决异步多智能体感知中的时空失配问题。
