<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**🧠 NeurIPS2025** · 共 **20** 篇

**[All You Need is One: Capsule Prompt Tuning with a Single Vector](all_you_need_is_one_capsule_prompt_tuning_with_a_single_vector.md)**

:   提出 Capsule Prompt-Tuning (CaPT)，发现现有 task-aware soft prompts 实际上与输入 tokens 缺乏交互（"attention 孤岛"），而将 instance-aware 信息融入单个 capsule prompt 可以作为"attention anchor"激活对关键结构信息的注意力，以极低参数量（如 Llama3.2-1B 上仅 0.003% 参数）实现超越多 prompt 方法的性能。

**[Angular Constraint Embedding via SpherePair Loss for Constrained Clustering](angular_constraint_embedding_via_spherepair_loss_for_constrained_clustering.md)**

:   提出 SpherePair loss，在角度空间（而非欧氏空间）中学习约束聚类的表示，通过余弦相似度编码 pairwise 约束，避免了端到端 DCC 方法对 anchor 的依赖和欧氏嵌入中正负对距离平衡的困难，无需预知聚类数目即可实现 SOTA 的约束聚类性能。

**[Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector](any_large_language_model_can_be_a_reliable_judge_debiasing_w.md)**

:   提出 Reasoning-based Bias Detector（RBD）作为 LLM 评判器的即插即用去偏模块——通过外部检测 4 种评估偏见（冗长/位置/从众/情感），生成带推理链的结构化反馈引导评判器自我纠正，RBD-8B 在 8 个 LLM 评判器上平均提升准确率 18.5%、一致性 10.9%。

**[Ascent Fails to Forget](ascent_fails_to_forget.md)**

:   挑战了机器遗忘领域的常见信念，证明梯度上升（gradient ascent）基于的无约束优化方法在遗忘/保留集之间存在统计依赖时会系统性失败——遗忘集指标的降低不可避免地损害整体测试性能，logistic 回归示例甚至展示了遗忘过程使模型比原始模型更远离 oracle 的灾难性情况。

**[Automated Detection of Visual Attribute Reliance with a Self-Reflective Agent](automated_detection_of_visual_attribute_reliance_with_a_self-reflective_agent.md)**

:   提出一个自反思 agent 框架，通过迭代的假设生成-测试-验证-反思循环来自动检测视觉模型中的属性依赖（如 CLIP 识别 teacher 依赖教室背景、YOLOv8 检测行人依赖人行横道），在 130 个注入已知属性依赖的模型 benchmark 上显示自反思显著提升检测准确性。

**[BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes](burstdeflicker_a_benchmark_dataset_for_flicker_removal_in_dynamic_scenes.md)**

:   提出首个面向多帧闪烁去除（MFFR）的大规模 benchmark 数据集 BurstDeflicker，包含基于 Retinex 的合成数据、真实静态数据和绿幕动态数据三个互补子集，系统解决了动态场景下闪烁-干净图像对难以获取的核心瓶颈。

**[CQ-DINO: Mitigating Gradient Dilution via Category Queries for Vast Vocabulary Object Detection](cq-dino_mitigating_gradient_dilution_via_category_queries_for_vast_vocabulary_ob.md)**

:   针对大规模类别（>10K）目标检测中分类头的正梯度稀释和难负样本梯度稀释问题，提出 CQ-DINO：用可学习类别查询替代分类头，通过图像引导的 Top-K 类别选择将负空间缩小 100 倍，在 V3Det（13204 类）上超越前 SOTA 2.1% AP，同时保持 COCO 竞争力。

**[BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes](delving_into_cascaded_instability_a_lipschitz_continuity_view_on_image_restorati.md)**

:   提出首个面向动态场景的多帧去闪烁（MFFR）基准数据集 BurstDeflicker，通过 Retinex 合成、真实静态采集与绿幕合成三种互补策略构建大规模训练/测试数据，显著提升闪烁去除模型在真实动态场景中的泛化能力。

**[DetectiumFire: A Comprehensive Multi-modal Dataset Bridging Vision and Language for Fire Understanding](detectiumfire_a_comprehensive_multi-modal_dataset_bridging_vision_and_language_f.md)**

:   DetectiumFire 构建了最大的多模态火灾理解数据集——14.5K 真实图像 + 2.5K 视频 + 8K 合成图像 + 12K RLHF 偏好对，低重复率（0.03 PHash vs D-Fire 0.15），配合 4 级严重性分类标准和详细场景描述，微调 YOLOv11m 达 mAP 43.74，微调 LLaMA-3.2-11B 火灾严重性分类 83.84%。

**[DETree: DEtecting Human-AI Collaborative Texts via Tree-Structured Hierarchical Representation Learning](detree_detecting_human-ai_collaborative_texts_via_tree-structured_hierarchical_r.md)**

:   提出 DETree 框架，通过构建层次亲和树（HAT）建模不同人机协作文本生成过程之间的层次关系，并设计树结构对比损失（TSCL）对齐表示空间，在混合文本检测和 OOD 场景下取得了显著优势。

**[Diffusion-Classifier Synergy: Reward-Aligned Learning via Mutual Boosting Loop for FSCIL](diffusion-classifier_synergy_reward-aligned_learning_via_mutual_boosting_loop_fo.md)**

:   提出 Diffusion-Classifier Synergy (DCS) 框架，通过在扩散模型和分类器之间建立互相增强的闭环，利用多层次奖励函数（特征级+logits级）引导扩散模型生成对分类器最有益的图像，在 FSCIL 基准上取得 SOTA。

**[DitHub: A Modular Framework for Incremental Open-Vocabulary Object Detection](dithub_a_modular_framework_for_incremental_openvocabulary_ob.md)**

:   提出 DitHub，借鉴版本控制系统（Git）思想构建开放词汇目标检测的模块化适配框架——将不同领域的高效适配模块（LoRA）作为"分支"管理，支持按需获取（fetch）和合并（merge），在 ODinW-13 上达到 SOTA，首次系统性研究目标检测中适配模块的组合特性。

**[Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable](dual_data_alignment_makes_ai-generated_image_detector_easier_generalizable.md)**

:   提出 Dual Data Alignment (DDA)，通过像素域和频域双重对齐生成训练用合成图像，消除数据集偏置导致的虚假相关性，使检测器仅学习伪造相关特征，在11个基准上平均准确率达到90.7%，大幅超越现有方法。

**[Dynamic Features Adaptation in Networking: Toward Flexible Training and Explainable Inference](dynamic_features_adaptation_in_networking_toward_flexible_training_and_explainab.md)**

:   提出 DAFI（Drift-Aware Feature Importance）算法，利用分布漂移检测动态切换 SHAP/MDI 两种特征重要性方法，结合自适应随机森林（ARF）实现通信网络场景下特征动态增加时的灵活训练与高效可解释推理。

**[Generalizable Insights for Graph Transformers in Theory and Practice](generalizable_insights_for_graph_transformers_in_theory_and_practice.md)**

:   提出 Generalized-Distance Transformer (GDT)，一种基于标准注意力（无需修改注意力机制）的图 Transformer 架构，理论证明其表达力等价于 GD-WL 算法，并通过覆盖 800 万图/2.7 亿 token 的大规模实验首次建立了 PE 表达力的细粒度经验层次，在 few-shot 迁移设置下无需微调即可超越 SOTA。

**[InstanceAssemble: Layout-Aware Image Generation via Instance Assembling Attention](instanceassemble_layoutaware_image_generation_via_instance_a.md)**

:   提出InstanceAssemble，通过实例组装注意力机制（instance-assembling attention）实现layout条件的精确控制——支持bbox位置控制和多模态内容控制（文本+视觉内容），作为轻量LoRA模块适配到现有DiT模型，同时提出DenseLayout benchmark（5K图像90K实例）和Layout Grounding Score评估指标。

**[OverLayBench: A Benchmark for Layout-to-Image Generation with Dense Overlaps](overlaybench_a_benchmark_for_layout-to-image_generation_with_dense_overlaps.md)**

:   OverLayBench 构建了首个聚焦密集重叠场景的 Layout-to-Image 基准（4052 样本 + OverLayScore 难度指标），揭示 SOTA 方法在复杂重叠下 mIoU 从 71%→54% 急剧退化，提出 Amodal Mask 监督在重叠 IoU 上提升 15.9%。

**[SAFE: Multitask Failure Detection for Vision-Language-Action Models](safe_multitask_failure_detection_for_vision-language-action_models.md)**

:   SAFE 发现 VLA 模型的内部特征空间存在跨任务一致的"失败区域"，据此训练轻量 MLP/LSTM 失败检测器，配合功能保形预测（FCP）做阈值校准，在未见任务上达 78% ROC-AUC，计算开销 <1%，大幅优于 token 不确定性和一致性检测方法。

**[Test-Time Adaptive Object Detection with Foundation Model](test-time_adaptive_object_detection_with_foundation_model.md)**

:   提出无需源域数据的开放词汇测试时自适应目标检测框架（TTAOD），通过多模态 Prompt Tuning + Mean-Teacher + 实例动态记忆（IDM）+ 记忆增强/幻觉策略，在 Pascal-C 上 AP50 达 56.2%（+11.0 vs SOTA），在 13 个跨域数据集上一致有效。

**[The Complexity of Finding Local Optima in Contrastive Learning](the_complexity_of_finding_local_optima_in_contrastive_learning.md)**

:   证明对比学习中寻找局部最优是计算困难的：离散三元组最大化问题是 PLS-hard（即使 $d=1$），连续三元组损失最小化是 CLS-hard，意味着（在标准假设下）不存在多项式时间算法找到局部最优。
