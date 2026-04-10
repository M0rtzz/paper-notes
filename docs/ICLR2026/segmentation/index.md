<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✂️ 语义分割

**🔬 ICLR2026** · 共 **12** 篇

**[AMLRIS: Alignment-aware Masked Learning for Referring Image Segmentation](amlris_alignment-aware_masked_learning_for_referring_image_segmentation.md)**

:   提出对齐感知遮蔽学习(AML)策略，通过量化视觉-语言 patch 级对齐度并过滤低对齐像素，让 RIS 模型在训练时聚焦可靠区域，无需架构改动即在 RefCOCO 全部 8 个 split 上达到 SOTA。

**[ByteFlow: Language Modeling through Adaptive Byte Compression without a Tokenizer](byteflow_language_modeling_through_adaptive_byte_compression_without_a_tokenizer.md)**

:   提出 ByteFlow Net，一种无需分词器的分层字节级语言模型，利用信息论中的编码率(coding rate)自适应地将原始字节流压缩为语义单元，在预训练损失和下游任务上超越 BPE 基线和已有字节级架构。

**[Efficient-SAM2: Accelerating SAM2 with Object-Aware Visual Encoding and Memory Retrieval](efficient-sam2_accelerating_sam2_with_object-aware_visual_encoding_and_memory_re.md)**

:   发现 SAM2 存在类似生物视觉的稀疏感知模式（解码器聚焦前景但编码器广泛计算、记忆帧中仅少量 token 有效且显著性时间一致），据此提出 Efficient-SAM2，通过对象感知的稀疏窗口路由（SWR）和稀疏记忆检索（SMR）消除冗余计算，在 SAM2.1-L 上实现 1.68× 端到端加速且仅损失 1% 精度。

**[Locality-Attending Vision Transformer](locality-attending_vision_transformer.md)**

:   提出 LocAt，一个轻量级 ViT 插件，通过可学习高斯核调制自注意力偏向局部邻域(GAug)和无参数的 Patch 表征精炼(PRR)，在不改变训练范式的前提下为 ViT 带来 6%+ 的分割性能提升且不牺牲分类精度。

**[RegionReasoner: Region-Grounded Multi-Round Visual Reasoning](regionreasoner_region-grounded_multi-round_visual_reasoning.md)**

:   提出 RegionReasoner，一个基于强化学习的多轮视觉推理框架，通过引用标注奖励和全局-局部一致性奖励，使推理轨迹必须显式引用参考区域坐标并保持语义连贯，在新构建的 RegionDial-Bench 上显著提升多轮定位和分割精度。

**[Revisiting [CLS] and Patch Token Interaction in Vision Transformers](revisiting_cls_and_patch_token_interaction_in_vision_transformers.md)**

:   深入分析Vision Transformer中[CLS]全局token和patch局部token之间的交互摩擦，发现归一化层隐式地区分了两类token，提出在归一化层和早期QKV投影中引入专门化处理路径，仅增加8%参数即实现分割性能提升超2 mIoU，同时保持分类精度。

**[Target-Aware Video Diffusion Models](target-aware_video_diffusion_models.md)**

:   提出 target-aware 视频扩散模型，仅需一张输入图像和目标物体的分割 mask，即可生成演员与指定目标交互的视频；核心创新是引入 [TGT] 特殊 token 并设计选择性交叉注意力损失，使模型关注目标的空间位置，在目标对齐和视频质量上全面超越基线。

**[Thicker and Quicker: A Jumbo Token for Fast Plain Vision Transformers](thicker_and_quicker_a_jumbo_token_for_fast_plain_vision_transformers.md)**

:   本文提出 Jumbo 方法：将 ViT 的 CLS token 扩展为 $J$ 倍宽度，在注意力前拆分为 $J$ 个与 patch 等宽的 token 参与自注意力，注意力后重新拼接并经过专用的宽 FFN 处理——以极低的计算开销显著增加全局建模容量，使 plain ViT 在高速推理场景下超越专用高效架构（EfficientViT、SHViT、MobileNetV4），同时保留 ViT 的所有架构优势。

**[TRACE: Your Diffusion Model is Secretly an Instance Edge Detector](trace_your_diffusion_model_is_secretly_an_instance_edge_detector.md)**

:   发现文本到图像扩散模型的自注意力图在去噪过程特定时间步隐式编码了实例边界信息，提出 TRACE 框架通过实例涌现点(IEP)和注意力边界散度(ABDiv)提取这些边界，并蒸馏为单步边缘检测器，在无监督实例分割和弱监督全景分割上大幅超越已有方法。

**[Universal Multi-Domain Translation via Diffusion Routers](universal_multi-domain_translation_via_diffusion_routers.md)**

:   提出 Diffusion Router (DR)，一个统一的扩散模型框架，仅用 $K-1$ 个与中心域配对的数据集，通过单个噪声预测网络配合源域/目标域标签条件化，实现任意 $K$ 个域之间的间接和直接翻译，并提出 Tweedie 精炼采样降低计算成本。

**[VINCIE: Unlocking In-context Image Editing from Video](vincie_unlocking_in-context_image_editing_from_video.md)**

:   提出 VINCIE，首次仅从视频数据学习上下文图像编辑能力——将视频标注为交错多模态序列，设计三个代理任务(次帧预测/当前分割/次帧分割预测)，在多轮编辑 benchmark 上达到 SOTA，展现了视频数据作为编辑训练源的可扩展性。

**[VIRTUE: Visual-Interactive Text-Image Universal Embedder](virtue_visual-interactive_text-image_universal_embedder.md)**

:   提出 VIRTUE，将分割模型 SAM2 与 VLM 结合构建视觉交互式通用嵌入器，支持用户通过点/框/掩码指定兴趣区域产生实体级+全局级联合嵌入，并构建百万级 SCaR 基准评估视觉交互检索能力，在 36 个 MMEB 任务（+3.1%-8.5%）和 5 个 SCaR 任务（+15.2%-20.3%）上均达到 SOTA。
