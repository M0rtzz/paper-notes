<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**📷 CVPR2026** · 共 **22** 篇

**[Addressing Data Scarcity in 3D Trauma Detection through Self-Supervised and Semi-Supervised Learning with Vertex Relative Position Encoding](addressing_data_scarcity_in_3d_trauma_detection_th.md)**

:   在仅206例标注CT中，通过patch-based MIM预训练3D U-Net + VDETR顶点RPE + 半监督一致性正则化的两阶段框架，将3D创伤检测mAP@0.50从26.36%提升至56.57%（验证集），同时冻结编码器的7类分类达94.07%准确率。

**[Addressing Data Scarcity in 3D Trauma Detection through Self-Supervised and Semi-Supervised Learning with Vertex Relative Position Encoding](addressing_data_scarcity_in_3d_trauma_detection_through_self-supervised_and_semi.md)**

:   提出两阶段标签高效框架：先用 patch-based MIM 在1,206个无标注CT上自监督预训练3D U-Net编码器，再用VDETR+3D顶点相对位置编码做3D损伤检测，配合Mean Teacher半监督一致性正则化利用2,000个无标注体数据，仅用144个有标注样本即实现56.57% val mAP@0.50（比纯监督提升115%）。

**[Bd-Merging Bias-Aware Dynamic Model Merging With Evidence-Guided Contrastive Lea](bd-merging_bias-aware_dynamic_model_merging_with_evidence-guided_contrastive_lea.md)**

:   提出 BD-Merging 框架，通过 Dirichlet 证据建模 + 邻域差异分数（ADS）+ 差异感知对比学习，训练去偏路由器来自适应分配模型合并权重，显著提升合并模型在测试时分布偏移和未见任务上的鲁棒性与泛化能力。

**[BoSS: A Best-of-Strategies Selector as an Oracle for Deep Active Learning](boss_a_best-of-strategies_selector_as_an_oracle_for_deep_active_learning.md)**

:   提出 BoSS——一种可扩展的 oracle 策略选择框架：在每轮主动学习中，并行运行多种查询策略在随机子池上生成候选 batch，通过冻结 backbone 仅重训最后一层快速评估每个候选 batch 的性能增益，选出最优 batch，从而量化现有 AL 策略与理论最优之间的差距。

**[BoSS: A Best-of-Strategies Selector as an Oracle for Deep Active Learning](boss_a_bestofstrategies_selector_as_an_oracle_for.md)**

:   提出BoSS，一种通过集成多个选择策略生成候选批次、冻结backbone仅重训最后一层来快速评估性能增益、然后选取最优批次的可扩展Oracle策略，揭示当前SOTA主动学习策略在大规模多类数据集上距离最优仍有显著差距。

**[D2Dewarp: Dual Dimensions Geometric Representation Learning Based Document Image Dewarping](d2dewarp_dual_dimensions_geometric_representation_learning_based_document_image_.md)**

:   提出 D2Dewarp——首个从水平和垂直双维度学习文档几何表示的去畸变方法：UNet 双解码器分别预测水平线（文档/表格/文本行的上下边界）和垂直线（左右边界），HV Fusion Module 通过混合注意力交叉融合两个方向的特征，并构建了包含 114K 张图的 DocDewarpHV 数据集提供双维度标注。

**[DiverseDiT: Towards Diverse Representation Learning in Diffusion Transformers](diversedit_towards_diverse_representation_learning_in_diffusion_transformers.md)**

:   通过系统分析发现 DiT 各 block 间的表示多样性是有效学习的关键因素，提出 DiverseDiT：用长残差连接多样化输入 + 表示多样性损失显式促进 block 间特征差异化，无需外部引导模型即可加速收敛并提升生成质量。

**[LaS-Comp: Zero-shot 3D Completion with Latent-Spatial Consistency](las-comp_zero-shot_3d_completion_with_latent-spatial_consistency.md)**

:   提出 LaS-Comp，一种零样本、类别无关的 3D 形状补全框架，通过 Explicit Replacement Stage 在空间域注入已知几何 + Implicit Alignment Stage 在隐空间梯度优化边界一致性，桥接了预训练 3D 基础模型的隐空间与空间域之间的 gap，在多种部分观测模式下达到 SOTA。

**[MapGCLR: Geospatial Contrastive Learning of Representations for Online Vectorized HD Map Construction](mapgclr_geospatial_contrastive_learning_of_represe.md)**

:   提出 MapGCLR, 通过利用多次行驶轨迹在地理空间上的自然重叠作为对比学习信号, 预训练 BEV 特征表示, 在 Argoverse 2 上以仅 5% 标注数据实现 +42% 的相对 mAP 提升.

**[MapGCLR: Geospatial Contrastive Learning of Representations for Online Vectorized HD Map Construction](mapgclr_geospatial_contrastive_learning_of_representations_for_online_vectorized.md)**

:   MapGCLR 提出基于地理空间对比学习的半监督训练方案：利用同一地点多次驾驶经过产生的 BEV 特征网格的地理空间重叠关系，构建 InfoNCE 对比损失强制 BEV 特征空间的地理一致性，在 Argoverse 2 上仅用 5% 标注数据即达到 18.9 mAP（纯监督基线 13.3），相对提升 42%，效果几乎等于将标注数据量翻倍。

**[MINE-JEPA: In-Domain Self-Supervised Learning for Mineral Exploration](mine-jepa_in-domain_self-supervised_learning_for_mine-like_object_classification.md)**

:   提出 Mine-JEPA，首个面向侧扫声纳（SSS）水雷分类的域内自监督学习流水线——基于 SIGReg 正则化损失、声纳适配增强策略和 ImageNet 初始化，仅用 1,170 张未标注声纳图像预训练即超越了在 17 亿图像上预训练的 DINOv3 基础模型。

**[Missing No More: Dictionary-Guided Cross-Modal Image Fusion under Missing Infrared](missing_no_more_dictionary-guided_cross-modal_image_fusion_under_missing_infrare.md)**

:   提出首个在系数域（而非像素域）进行红外缺失条件下跨模态融合的框架：通过共享卷积字典建立 IR-VIS 统一原子空间，在系数域完成 VIS→IR 推理和自适应融合，配合冻结 LLM 提供弱语义先验进行热信息补全，在仅输入可见光图像的条件下达到接近双模态融合方法的性能。

**[Representation Learning for Spatiotemporal Physical Systems](representation_learning_for_spatiotemporal_physica.md)**

:   通过在三个PDE物理系统（活性物质、剪切流、Rayleigh-Bénard对流）上对比JEPA、VideoMAE、MPP和DISCO，发现隐空间预测方法(JEPA)在物理参数估计任务上全面优于像素级预测方法(MAE/自回归模型)，MSE平均改善30-50%。

**[Representation Learning for Spatiotemporal Physical Systems](representation_learning_for_spatiotemporal_physical_systems.md)**

:   在三个 PDE 物理系统上系统对比 JEPA、VideoMAE、自回归基础模型(MPP)和算子学习(DISCO) 四种范式，发现隐空间预测目标(JEPA)在物理参数估计下游任务上全面优于像素级预测方法，MSE 相对改善 28-51%，且数据效率更高。

**[SpHOR: A Representation Learning Perspective on Open-set Recognition](sphor_a_representation_learning_perspective_on_ope.md)**

:   提出SpHOR两阶段解耦训练框架：Stage 1通过正交标签嵌入+球面约束（vMF分布）+Mixup/Label Smoothing做专为OSR设计的表征学习，Stage 2冻结特征训练分类器——在Semantic Shift Benchmark上OSCR/AUROC最高提升5.1%/5.2%，同时引入Angular Separability和Norm Separability两个新度量。

**[SpHOR: A Representation Learning Perspective on Open-set Recognition for Identifying Unknown Classes in Deep Neural Networks](sphor_a_representation_learning_perspective_on_open-set_recognition_for_identify.md)**

:   提出 SpHOR，一种两阶段解耦训练的开放集识别方法，通过球面表示学习（vMF 分布）、正交标签嵌入和 Mixup/Label Smoothing 集成，显式塑造特征空间以更好地分离已知/未知类别，在 Semantic Shift Benchmark 上取得最高 5.1% 的 OSCR 提升。

**[TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction](talo_pushing_3d_vision_foundation_models_towards_globally_consistent_online_reco.md)**

:   提出 TALO，一种基于 Thin Plate Spline 的高自由度对齐框架，通过全局传播控制点和点无关的子图配准设计，纠正 3D 视觉基础模型在在线重建中的空间变化不一致性，兼容多种基础模型和相机配置，在 Waymo/nuScenes 数据集上显著降低轨迹误差。

**[TeFlow: Enabling Multi-frame Supervision for Self-Supervised Feed-forward Scene Flow Estimation](teflow_enabling_multi-frame_supervision_for_self-supervised_feed-forward_scene_f.md)**

:   通过教师-学生框架将多帧观测的丰富监督信号蒸馏到前馈场景流网络中，解决自监督场景流中单对帧监督不足的问题

**[Text-Phase Synergy Network with Dual Priors for Unsupervised Cross-Domain Image Retrieval](text-phase_synergy_network_with_dual_priors_for_unsupervised_cross-domain_image_.md)**

:   利用文本语义先验和相位结构先验的协同实现无监督跨域图像检索

**[TrackMAE: Video Representation Learning via Track, Mask, and Predict](trackmae_video_representation_learning_via_track_mask_and_predict.md)**

:   在masked video modeling（MVM）框架中引入显式的运动信号：使用CoTracker3提取点轨迹作为额外的重建目标，并设计运动感知遮掩策略，联合学习空间重建和运动预测，在运动敏感基准（SSv2、FineGym）上显著超越现有视频自监督方法。

**[Vision Transformers Need More Than Registers](vision_transformers_need_more_than_registers.md)**

:   这篇论文认为 ViT 在标签监督、文本监督和自监督下普遍存在的 dense feature 伪影，本质上不是单纯的 high-norm token 问题，而是模型在粗粒度监督和全局注意力共同作用下学会了用背景 patch 充当全局语义捷径；作者据此提出 LaSt-ViT，用频域稳定性引导的选择性聚合替代原始 CLS 聚合，在 12 个基准上稳定改善定位、分割和开放词汇任务。

**[Vision Transformers Need More Than Registers](vit_need_more_than_registers.md)**

:   系统揭示ViT注意力伪影的根因是"惰性聚合"——全局注意力+粗粒度语义监督驱动模型用语义无关的背景patch作为全局语义的捷径表示，提出选择性patch特征集成方案在12个基准上跨三种监督范式一致提升性能。
