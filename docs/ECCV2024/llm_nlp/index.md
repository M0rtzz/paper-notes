<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**🎞️ ECCV2024** · 共 **16** 篇

**[AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection](adaclip_adapting_clip_with_hybrid_learnable_prompts_for_zero.md)**

:   在CLIP中同时引入静态（全局共享）和动态（逐图生成）两种可学习提示，用辅助异常检测数据训练后，在14个工业+医学异常检测数据集上实现零样本SOTA，核心在于"任务级+实例级"双层自适应的混合提示设计。

**[ColorMNet: A Memory-based Deep Spatial-Temporal Feature Propagation Network for Video Colorization](colormnet_a_memory-based_deep_spatial-temporal_feature_propagation_network_for_v.md)**

:   提出 ColorMNet，一种基于记忆机制的时空特征传播网络，通过预训练大视觉模型引导的特征提取（PVGFE）、基于记忆的特征传播（MFP）和局部注意力（LA）三个模块，在显著降低 GPU 显存消耗（仅需 1.9G）的同时实现了优于 SOTA 的视频上色效果。

**[Dataset Growth](dataset_growth.md)**

:   提出 InfoGrowth，一种高效的在线数据清洗与选择算法，通过噪声检测+信息增益计算+采样策略，使数据集在持续增长过程中保持清洁性与多样性，实现 2-4 倍数据效率提升。

**[Deep Cost Ray Fusion for Sparse Depth Video Completion](deep_cost_ray_fusion_for_sparse_depth_video_completion.md)**

:   本文提出 RayFusion 框架，通过在 cost volume 上沿射线方向施加 self-attention 和 cross-attention 实现时序融合，以仅 1.15M 参数在 KITTI、VOID、ScanNetV2 三个数据集上全面超越或持平 SOTA 稀疏深度补全方法。

**[FunQA: Towards Surprising Video Comprehension](funqa_towards_surprising_video_comprehension.md)**

:   构建了大规模反直觉视频问答基准 FunQA（4.3K 视频、312K QA 对），覆盖幽默/创意/魔术三类令人惊讶的视频，并提出 FunMentor 智能体通过多轮对话增强 VLM 的反常识推理能力。

**[Grounding Language Models for Visual Entity Recognition](grounding_language_models_for_visual_entity_recognition.md)**

:   提出 AutoVER——首个将多模态大语言模型（MLLM）应用于大规模视觉实体识别的方法，通过将检索能力集成到 MLLM 内部，结合对比训练和前缀树约束解码，在 Oven-Wiki 基准上大幅超越 PaLI-17B 等先前方法。

**[On the Utility of 3D Hand Poses for Action Recognition](on_the_utility_of_3d_hand_poses_for_action_recognition.md)**

:   提出 HandFormer，一种高效多模态 Transformer，通过密集采样的 3D 手部姿态与稀疏采样的 RGB 帧相结合，以远低于现有方法的计算量实现了手-物交互动作识别 SOTA。

**[OneRestore: A Universal Restoration Framework for Composite Degradation](onerestore_a_universal_restoration_framework_for_composite_degradation.md)**

:   提出 OneRestore，一种基于 Transformer 的通用图像复原框架，通过场景描述符引导的交叉注意力机制和复合退化复原损失，能在单一模型中自适应地处理低光照、雾、雨、雪及其任意组合的复合退化场景，并支持文本/视觉双模式的可控复原。

**[Prompting Language-Informed Distribution for Compositional Zero-Shot Learning](prompting_language-informed_distribution_for_compositional_zero-shot_learning.md)**

:   本文提出 PLID 方法，利用 LLM 生成的句子级类别描述构建语言知识驱动的高斯分布，配合视觉-语言原语分解和随机 logit 融合，在组合零样本学习（CZSL）任务上取得 SOTA。

**[PromptIQA: Boosting the Performance and Generalization for No-Reference Image Quality Assessment via Prompts](promptiqa_boosting_the_performance_and_generalization_for_no-reference_image_qua.md)**

:   提出 PromptIQA，通过少量"图像-分数对"（ISP）作为 prompt 的方式，使 NR-IQA 模型训练完成后无需微调即可自适应适配新的质量评估需求，在 12 个数据集、5 类 IQA 任务上均达到 SOTA 性能和泛化能力。

**[Reprojection Errors as Prompts for Efficient Scene Coordinate Regression](reprojection_errors_as_prompts_for_efficient_scene_coordinate_regression.md)**

:   本文提出 EGFS（Error-Guided Feature Selection）机制，利用低重投影误差区域作为 SAM 的 point prompts 扩展为语义掩码，迭代地筛选可靠训练样本，在 Cambridge Landmarks 和 Indoor6 数据集上以更小模型和更少训练时间超越现有无 3D 信息依赖的 SCR 方法。

**[Rotary Position Embedding for Vision Transformer](rotary_position_embedding_for_vision_transformer.md)**

:   系统研究将大语言模型中的旋转位置编码（RoPE）扩展到 2D 视觉 Transformer，提出 RoPE-Mixed（混合可学习频率）变体，在多分辨率分类、目标检测和语义分割上均带来显著且接近零额外计算的性能提升。

**[SIGMA: Sinkhorn-Guided Masked Video Modeling](sigma_sinkhorn-guided_masked_video_modeling.md)**

:   本文提出 SIGMA，通过引入投影网络将 masked video modeling 的重建目标从像素级升级为可学习的深层特征聚类分配，利用 Sinkhorn 算法的最优传输实施高熵正则化避免坍缩，在 10 个数据集 3 个 benchmark 上全面超越 VideoMAE 等 SOTA 方法。

**[VisFocus: Prompt-Guided Vision Encoders for OCR-Free Dense Document Understanding](visfocus_promptguided_vision_encoders_for_ocrfree_dense.md)**

:   提出 VisFocus，通过在视觉编码器的 patch merging 层引入 prompt 感知的 ViLMA 层，并设计 LMPM 预训练任务，使 OCR-Free 文档理解模型能聚焦于与用户查询相关的文本区域，在多个文档 VQA 基准上达到同规模 SOTA。

**[When Do We Not Need Larger Vision Models?](when_do_we_not_need_larger_vision_models.md)**

:   提出 Scaling on Scales (S2)，通过让预训练的冻结小模型在多个图像尺度上运行（而非增大模型参数），即可超越更大模型在分类、分割、深度估计、MLLM 和机器人操控等任务上的表现。

**[Zero-Shot Object Counting with Good Exemplars (VA-Count)](zeroshot_object_counting_with_good_exemplars.md)**

:   提出 VA-Count，一种基于视觉关联的零样本物体计数框架，通过 Grounding DINO 驱动的样例增强模块和对比学习噪声抑制模块，为任意类别建立高质量样例与图像间的鲁棒视觉关联。
