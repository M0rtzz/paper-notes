<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎯 目标检测

**🎞️ ECCV2024** · 共 **15** 篇

**[A New Dataset and Framework for Real-World Blurred Images Super-Resolution](a_new_dataset_and_framework_for_real-world_blurred_images_super-resolution.md)**

:   针对现有盲超分方法在处理含模糊（散焦/运动模糊）图像时过度纹理化、破坏模糊区域感知质量的问题，构建了包含近3000张模糊图像的ReBlurSR数据集，并提出PBaSR框架，通过双分支解耦训练（CDM）和基于权重插值的跨分支融合（CFM），在不增加任何推理开销的前提下，同时提升模糊图像和普通图像的超分效果，LPIPS提升0.02~0.10。

**[Adaptive Bounding Box Uncertainties via Two-Step Conformal Prediction](adaptive_bounding_box_uncertainties_via_twostep_conformal_pr.md)**

:   提出两步共形预测框架为多类目标检测的边界框生成带理论覆盖率保证的自适应不确定性区间——第一步用共形分类集处理类别误判风险，第二步用集成/分位数回归等方法构建自适应于目标尺寸的边界框预测区间，在COCO/Cityscapes/BDD100k上达到约90%目标覆盖率且区间实际可用。

**[AFreeCA: Annotation-Free Counting for All](afreeca_annotation-free_counting_for_all.md)**

:   利用 Stable Diffusion 生成合成排序/计数数据，通过先学排序再学计数的两阶段策略 + 密度引导的图像分块，实现了首个适用于任意类别物体的无标注计数方法，在人群计数上超越已有无监督方法。

**[AFreeCA: Annotation-Free Counting for All](afreeca_annotationfree_counting_for_all.md)**

:   利用潜在扩散模型（LDM）生成合成计数和排序数据，提出首个可适用于任意物体类别的无监督计数方法，无需任何人工标注即可实现准确计数。

**[BAM-DETR: Boundary-Aligned Moment Detection Transformer for Temporal Sentence Grounding in Videos](bam-detr_boundary-aligned_moment_detection_transformer_for_temporal_sentence_gro.md)**

:   提出边界对齐的时刻检测 Transformer（BAM-DETR），用 anchor-boundary 三元组 $(p, d_s, d_e)$ 替代传统的 center-length 二元组 $(c, l)$ 来建模时刻，配合双路径解码器和基于质量的排序机制，有效解决了中心模糊导致的定位不精确问题。

**[Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](be_yourself_bounded_attention_for_multi-subject_text-to-image_generation.md)**

:   提出 Bounded Attention，一种无需训练的注意力约束方法，通过在去噪过程中限制 cross-attention 和 self-attention 的信息流动来解决多主体文本到图像生成中的语义泄漏问题。

**[Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](be_yourself_bounded_attention_for_multisubject_texttoimage_g.md)**

:   Be Yourself深入分析了扩散模型中Cross-Attention和Self-Attention导致的多主体语义泄漏问题，提出Bounded Attention机制，通过在去噪过程中限制不同主体间的信息流动来生成语义独立的多主体图像，免训练即可生成5+个语义相似主体。

**[Bridge Past and Future: Overcoming Information Asymmetry in Incremental Object Detection](bridge_past_and_future_overcoming_information_asymmetry_in_incremental_object_de.md)**

:   提出 Bridge Past and Future (BPF) 方法，通过伪标签桥接过去阶段、注意力机制排除未来潜在物体，并结合双教师蒸馏（Distillation with Future），解决增量目标检测中跨阶段信息不对称导致的优化目标不一致问题。

**[Can OOD Object Detectors Learn from Foundation Models?](can_ood_object_detectors_learn_from_foundation_models.md)**

:   SyncOOD 提出一种自动化数据策展方法，利用 LLM 想象语义新颖的 OOD 概念，通过 Stable Diffusion Inpainting 在 ID 图像上进行区域级编辑合成场景级 OOD 样本，再经 SAM 精炼框和特征相似度过滤后训练轻量 MLP 分类器，在多个 OOD 检测基准上以极少量合成数据大幅超越 SOTA。

**[DAMSDet: Dynamic Adaptive Multispectral Detection Transformer](damsdet_dynamic_adaptive_multispectral_detection_transformer_with_competitive_qu.md)**

:   DAMSDet 提出一种基于 DETR 架构的动态自适应红外-可见光目标检测方法，通过模态竞争 Query 选择（为每个目标动态选择主导模态特征作为初始 query）和多光谱可变形交叉注意力（在多语义层级上自适应采样和聚合双模态特征），同时解决互补信息融合和模态未对齐两大挑战，在 4 个公开数据集上显著超越 SOTA。

**[Efficient Inference of Vision Instruction-Following Models with Elastic Cache](efficient_inference_of_vision_instruction-following_models_with_elastic_cache.md)**

:   Elastic Cache 提出一种针对多模态指令遵循模型的 KV Cache 管理方法，在指令编码阶段采用基于重要性的 cache 合并策略（而非丢弃），在输出生成阶段采用固定点淘汰策略，以"一个序列、两种策略"实现任意加速比的高效推理，在 KV Cache 预算仅 0.2 时实现 78% 的实际速度提升且保持生成质量。

**[GRA: Detecting Oriented Objects Through Group-Wise Rotating and Attention](gra_detecting_oriented_objects_through_group-wise_rotating_and_attention.md)**

:   提出轻量级的 Group-wise Rotating and Attention (GRA) 模块，通过将卷积核分组旋转并施加分组空间注意力，在参数量减少近 50% 的同时超越了此前 SOTA 方法 ARC，在 DOTA-v2.0 上取得新的最优性能。

**[LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer](layoutdetr_detection_transformer_is_a_good_multimodal_layout.md)**

:   将版式设计问题重新构建为基于背景图像的目标检测问题，提出LayoutDETR框架，利用DETR的transformer编解码器结构结合GAN/VAE生成先验，以多模态前景元素（图像+文本）为输入，生成考虑背景语义的排版布局，在公开基准和自建广告横幅数据集上均达到SOTA。

**[Towards Natural Language-Guided Drones: GeoText-1652 Benchmark with Spatial Relation Matching](towards_natural_languageguided_drones_geotext1652_bench.md)**

:   构建 GeoText-1652 多视角自然语言引导地理定位基准数据集（276K text-bbox 对），提出利用区域级空间关系匹配（grounding loss + spatial loss）进行精细化文本-图像跨模态检索的方法，实现自然语言控制无人机导航。

**[Tracking Meets LoRA: Faster Training, Larger Model, Stronger Performance](tracking_meets_lora_faster_training_larger_model_strong.md)**

:   首次将 LoRA 引入视觉目标跟踪领域，通过解耦位置编码和设计 MLP-only 头网络，使大规模 ViT 模型（最大 ViT-g）在实验室级资源下实现高效训练和 SOTA 跟踪性能。
