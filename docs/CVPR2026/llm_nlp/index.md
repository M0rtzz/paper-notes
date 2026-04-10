<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**📷 CVPR2026** · 共 **18** 篇

**[As Language Models Scale, Low-order Linear Depth Dynamics Emerge](as_language_models_scale_loworder_linear_depth_dyn.md)**

:   将 Transformer 的逐层前向传播视为离散时间动力系统，发现 32 维低阶线性代理（LLV）可精确复现完整模型的层级灵敏度曲线，且该线性可辨识性随模型规模单调增强。

**[Composing Concepts from Images and Videos via Concept-prompt Binding](composing_concepts_from_images_and_videos_via_concept-prompt_binding.md)**

:   提出 Bind & Compose (BiCo)，一种one-shot方法，通过层次化binder结构将视觉概念绑定到prompt token，并通过token组合实现图像-视频概念的灵活组合，在概念一致性、prompt保真度和运动质量上全面超越前作。

**[Cross-Scale Pansharpening via ScaleFormer and the PanScale Benchmark](cross-scale_pansharpening_via_scaleformer_and_the_panscale_benchmark.md)**

:   提出首个跨尺度全色锐化数据集PanScale和评测基准PanScale-Bench，以及ScaleFormer框架——将分辨率变化重新解释为序列长度变化，通过Scale-Aware Patchify分桶采样+解耦空间-序列建模+RoPE实现跨尺度泛化。

**[Defending Unauthorized Model Merging via Dual-Stage Weight Protection](defending_unauthorized_model_merging_via_dual-stage_weight_protection.md)**

:   提出 MergeGuard，一种主动式双阶段权重保护框架：Stage 1通过L2正则化分散任务关键权重，Stage 2注入结构化扰动破坏合并兼容性，在保持保护模型<1.5%性能损失的同时使合并模型精度下降高达90%。

**[EVATok: 自适应长度视频Tokenization用于高效视觉自回归生成](evatok_adaptive_length_video_tokenization_for_eff.md)**

:   提出EVATok框架——通过最优token分配估计+轻量路由器+自适应tokenizer训练的三步流程，让视频tokenizer按片段复杂度自适应分配token长度，在UCF-101上节省24.4%+ token同时达到SOTA生成质量。

**[Geometry-Guided Camera Motion Understanding in VideoLLMs](geometry-guided_camera_motion_understanding_in_videollms.md)**

:   本文揭示了 VideoLLM 在细粒度相机运动原语（pan/tilt/dolly等）识别上几乎等于随机猜测，构建了 CameraMotionDataset（12K 段 × 15 种原子运动）和 CameraMotionVQA benchmark，并提出通过冻结 3DFM（VGGT）提取几何相机线索 + 轻量时序分类器 + structured prompting 注入的 model-agnostic 方案来弥补这一能力缺口。

**[Geometry-Guided Camera Motion Understanding in VideoLLMs](geometryguided_camera_motion_understanding_in_vide.md)**

:   通过 benchmarking-diagnosis-injection 框架系统揭示 VideoLLM 的相机运动盲区，并利用冻结 3DFM (VGGT) 提取几何线索 + 轻量时序分类器 + 结构化提示注入，无需微调即可显著提升 VideoLLM 的细粒度相机运动理解。

**[GUIDE: Guided Updates for In-context Decision Evolution in LLM-Driven Spacecraft Operations](guide_guided_updates_for_in-context_decision_evolution_in_llm-driven_spacecraft_.md)**

:   提出GUIDE框架，利用LLM的in-context学习能力为航天器自主操作提供引导式决策进化，通过结构化的上下文信息和反馈机制让LLM在无需微调的情况下逐步改善航天任务规划和故障诊断决策的质量。

**[Hier-COS: Making Deep Features Hierarchy-aware via Composition of Orthogonal Subspaces](hier-cos_making_deep_features_hierarchy-aware_via_composition_of_orthogonal_subs.md)**

:   提出 Hier-COS 框架，通过为层次树中每个节点分配正交基向量，构造理论上保证层次一致性的层次感知向量空间(HAVS)，首次统一了"层次感知细粒度分类"和"层次多级分类"，同时提出新评估指标HOPS，在4个数据集上全面超越SOTA。

**[Hier-COS: Making Deep Features Hierarchy-aware via Composition of Orthogonal Subspaces](hiercos_making_deep_features_hierarchyaware_via_co.md)**

:   提出Hier-COS框架，为层次标签树中的每个节点分配正交基向量，通过子空间组合（祖先基+自身基+后代基）构建层次感知向量空间（HAVS），理论保证特征空间的距离结构与层次树一致，同时提出HOPS评估指标解决现有层次化评估指标的排列不变性缺陷。

**[IAPL: Generalizable AI-Generated Image Detection via Image-Adaptive Prompt Learning](iapl_aigenerated_image_detection_adaptive_prompt.md)**

:   针对 AI 生成图像检测中现有方法难以泛化到未见生成器的问题，提出图像自适应提示学习（IAPL），在推理时根据每张测试图像动态调整输入到视觉编码器的 prompt——通过条件信息学习器提取伪造特征条件和测试时自适应 token 优化，在 UniversalFakeDetect 和 GenImage 数据集上分别达到 95.61% 和 96.7% 的 SOTA 平均准确率。

**[Noise-Aware Few-Shot Learning through Bi-directional Multi-View Prompt Alignment](noiseaware_fewshot_learning_through_bidirectional.md)**

:   提出NA-MVP框架，通过双向（clean+noise-aware）多视图prompt设计配合非平衡最优传输（UOT）实现细粒度patch-to-prompt对齐，并用经典OT对识别出的噪声样本做选择性标签修正，在噪声小样本学习场景下持续超越SOTA。

**[PhysVid: Physics Aware Local Conditioning for Generative Video](physvid_physics_aware_local_conditioning_for_generative_video_models.md)**

:   提出 PhysVid，一种物理感知的局部条件化方案——将视频分为时间片段（chunk），由 VLM 为每个 chunk 标注物理现象描述，通过 chunk 级交叉注意力注入生成模型；推理时引入"负物理提示"（反事实引导）引导生成远离物理违规，在 VideoPhy 上将物理常识分数提升约 33%。

**[Residual SODAP: Residual Self-Organizing Domain-Adaptive Prompting with Structural Knowledge Preservation for Continual Learning](residual_sodap_residual_self-organizing_domain-adaptive_prompting_with_structura.md)**

:   提出 Residual SODAP 框架，通过 α-entmax 稀疏提示选择+残差聚合、无数据统计蒸馏+伪特征回放、提示使用模式漂移检测，以及不确定性加权多损失平衡，联合解决提示端表征适应和分类器端知识保持问题，在医学域增量学习上达到 SOTA。

**[Residual SODAP: Residual Self-Organizing Domain-Adaptive Prompting with Structural Knowledge Preservation for Continual Learning](residual_sodap_residual_selforganizing_domainadapt.md)**

:   提出Residual SODAP框架，在无任务ID、无数据存储的域增量学习中，联合解决表示适应（α-entmax稀疏prompt选择+残差聚合）和分类器保持（统计伪特征重放+知识蒸馏），在DR、皮肤癌和CORe50三个基准上达到SOTA。

**[SketchDeco: Training-Free Latent Composition for Precise Sketch Colourisation](sketchdeco_training-free_latent_composition_for_precise_sketch_colourisation.md)**

:   提出SketchDeco，一种无需训练的线稿上色方法，通过全局-局部两阶段策略将区域蒙版和调色板作为精确控制信号，利用扩散模型反演和自注意力注入在隐空间中实现区域精准着色与全局和谐过渡，在消费级GPU上15-20步即可完成。

**[VecGlypher: Unified Vector Glyph Generation with Language Models](vecglypher_unified_vector_glyph_generation_with_language_models.md)**

:   提出VecGlypher——首个统一文本和图像引导的矢量字形生成语言模型，通过两阶段训练(大规模SVG语法学习+专家标注对齐)直接自回归生成可编辑SVG路径，无需光栅中间步骤或向量化后处理。

**[WeaveTime: 流式视频LLM的帧级逐步记忆](weavetime_streaming_video_llm_memory.md)**

:   诊断出Video-LLM的核心缺陷"时间无感"——把视频当无序图像集处理，产生时序模糊和历史/当前混淆两类失效，提出WeaveTime通过轻量时序重建目标获得顺序感知能力+Past-Current动态焦点缓存实现高效流式推理，在流式基准上一致提升。
