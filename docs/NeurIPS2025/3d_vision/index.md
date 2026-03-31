<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D 视觉

**🧠 NeurIPS2025** · 共 **46** 篇

**[3D-Agent: Tri-Modal Multi-Agent Collaboration for Scalable 3D Object Annotation](3d-agenttri-modal_multi-agent_collaboration_for_scalable_3d_object_annotation.md)**

:   提出 Tri-MARF 三模态多智能体框架，通过 VLM 标注 Agent（多视角多候选描述）+ 信息聚合 Agent（BERT 聚类 + CLIP 加权 + UCB1 多臂赌博机选择）+ 点云门控 Agent（Uni3D 文本-点云对齐过滤幻觉），实现 CLIPScore 88.7（超越人类标注 82.4）、吞吐量 12k 物体/小时，已标注约 200 万 3D 模型。

**[3D Visual Illusion Depth Estimation](3d_visual_illusion_depth_estimation.md)**

:   揭示了3D视觉错觉（如墙面彩绘、屏幕重播、镜面反射等）会严重欺骗现有SOTA单目和双目深度估计方法，构建了包含约3k场景/200k图像的大规模数据集，并提出基于VLM常识推理的单目-双目自适应融合框架，在各类错觉场景下达到SOTA。

**[Anti-Aliased 2D Gaussian Splatting](anti-aliased_2d_gaussian_splatting.md)**

:   提出 AA-2DGS，通过世界空间平坦平滑核和物体空间 Mip 滤波器两个互补机制，解决 2D Gaussian Splatting 在不同采样率下渲染时的严重锯齿问题，在保持 2DGS 几何精度优势的同时显著提升多尺度渲染质量。

**[ARMesh: Autoregressive Mesh Generation via Next-Level-of-Detail Prediction](armesh_autoregressive_mesh_generation_via_next-level-of-detail_prediction.md)**

:   提出将 3D mesh 生成建模为"由粗到精"的逐级细化过程（next-level-of-detail prediction），通过反转广义网格简化算法（GSlim）获得渐进式细化序列，再用 Transformer 自回归学习，从单个点开始逐步增加几何与拓扑细节生成完整网格。

**[Atlasgs Atlanta-World Guided Surface Reconstruction With Implicit Structured Gau](atlasgs_atlanta-world_guided_surface_reconstruction_with_implicit_structured_gau.md)**

:   提出 AtlasGS，通过将 Atlanta-world 结构先验引入隐式结构化高斯表示（implicit-structured Gaussians），在室内和城市场景中实现平滑且保留高频细节的高质量表面重建，全面超越已有隐式和显式方法。

**[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](becominglit_relightable_gaussian_avatars_with_hybrid_neural_shading.md)**

:   提出 BecomingLit，基于 3D Gaussian 原语和混合神经着色（neural diffuse BRDF + 解析 Cook-Torrance specular）从低成本 light stage 多视角序列重建可重光照、实时渲染的高保真头部 avatar，并发布了新的公开 OLAT 人脸数据集。

**[Can LLMs Write Faithfully? An Agent-Based Evaluation of LLM-generated Islamic Content](can_llms_write_faithfully_an_agent-based_evaluation_of_llm-generated_islamic_con.md)**

:   提出双Agent（定量+定性）评估框架，从神学准确性、引用完整性和文体恰当性三个维度系统评估 GPT-4o、Ansari AI 和 Fanar 在伊斯兰内容生成任务上的忠实度，发现即使最优模型也在引用可靠性上存在显著不足。

**[Concerto: Joint 2D-3D Self-Supervised Learning Emerges Spatial Representations](concerto_joint_2d-3d_self-supervised_learning_emerges_spatial_representations.md)**

:   Concerto 将 3D 点云模态内自蒸馏与 2D-3D 跨模态联合嵌入预测相结合，以极简设计让单一点云编码器（PTv3）涌现出超越 2D/3D 单模态甚至两者拼接的空间表征，在多个 3D 场景理解基准上刷新 SOTA（ScanNet 语义分割 80.7% mIoU）。

**[Copresheaf Topological Neural Networks: A Generalized Deep Learning Framework](copresheaf_topological_neural_networks_a_generalized_deep_learning_framework.md)**

:   本文提出 Copresheaf Topological Neural Networks (CTNNs)，基于代数拓扑中的余预层（copresheaf）概念，在组合复形（combinatorial complex）上定义方向性、异质的消息传递机制，统一了 CNN、GNN、Transformer、Sheaf Neural Networks 和拓扑神经网络等多种深度学习架构，并在物理模拟、图分类和高阶复形分类任务上超越传统基线。

**[CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning](cosmobench_a_multiscale_multiview_multitask_cosmology_benchmark_for_geometric_de.md)**

:   提出 CosmoBench——目前最大的宇宙学几何深度学习基准，包含 3.4 万点云和 2.5 万有向树，覆盖多尺度、多视角、多任务，并揭示简单线性模型有时能超越大型 GNN。

**[Cue3D: Quantifying the Role of Image Cues in Single-Image 3D Generation](cue3d_quantifying_the_role_of_image_cues_in_single-image_3d_generation.md)**

:   提出 Cue3D——首个模型无关的框架，通过系统性扰动 6 种图像线索（光照/纹理/轮廓/透视/边缘/局部连续性）量化其对单图 3D 生成的影响，在 7 个 SOTA 方法上揭示：形状意义而非纹理决定泛化性，光照比纹理更重要，模型过度依赖轮廓——为更透明、鲁棒的 3D 生成指明方向。

**[D$^2$USt3R: Enhancing 3D Reconstruction for Dynamic Scenes](d2ust3r_enhancing_3d_reconstruction_for_dynamic_scenes.md)**

:   提出 Static-Dynamic Aligned Pointmap (SDAP) 表示，将静态和动态区域的 3D 对齐统一建模，使 DUSt3R 系列方法能够在动态场景中实现准确的稠密三维重建与对应关系估计。

**[DGH: Dynamic Gaussian Hair](dgh_dynamic_gaussian_hair.md)**

:   提出 Dynamic Gaussian Hair (DGH)，一个数据驱动的 coarse-to-fine 框架，通过体素隐式变形模型学习头发动力学，并结合柱状 Gaussian 表示与曲率混合策略实现动态头发的逼真新视角渲染。

**[DualFocus: Depth from Focus with Spatio-Focal Dual Variational Constraints](dualfocus_depth_from_focus_with_spatio-focal_dual_variational_constraints.md)**

:   提出 DualFocus，通过空间变分约束（利用焦距相关梯度模式区分深度边缘与纹理伪影）和焦距变分约束（强制单峰单调的对焦概率分布）双重约束，实现从焦距堆栈中鲁棒精确的深度估计。

**[Dynamic Gaussian Splatting from Defocused and Motion-blurred Monocular Videos](dynamic_gaussian_splatting_from_defocused_and_motion-blurred_monocular_videos.md)**

:   提出统一框架，通过可学习模糊核卷积联合建模散焦模糊和运动模糊，结合动态高斯致密化策略和未见视角约束，从模糊单目视频中实现高质量动态 3DGS 新视角合成。

**[DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation](dynarend_learning_3d_dynamics_via_masked_future_rendering_for_robotic_manipulati.md)**

:   提出 DynaRend，通过掩码重建和未来预测两个互补目标，利用可微体渲染在 triplane 表征上联合学习 3D 几何、语义和动态信息，预训练后可高效迁移到下游机器人操控任务。

**[E-MoFlow: Learning Egomotion and Optical Flow from Event Data via Implicit Regularization](e-moflow_learning_egomotion_and_optical_flow_from_event_data_via_implicit_regula.md)**

:   提出 E-MoFlow，通过将光流建模为隐式神经表示、自运动建模为连续样条，并利用微分几何约束联合优化两者，在无监督范式下实现事件数据的 6-DoF 自运动和稠密光流联合估计。

**[EA3D: Online Open-World 3D Object Extraction from Streaming Videos](ea3d_online_open-world_3d_object_extraction_from_streaming_videos.md)**

:   提出 EA3D（ExtractAnything3D），一个在线开放世界 3D 物体提取框架，通过知识集成特征图、在线视觉里程计和循环联合优化，从流式视频中同时进行几何重建和全面场景理解。

**[EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes](eag3r_event-augmented_3d_geometry_estimation_for_dynamic_and_extreme-lighting_sc.md)**

:   EAG3R 将事件相机的异步事件流融入 MonST3R 点图重建框架，通过 Retinex 增强 + SNR 感知融合 + 事件光度一致性损失，在极端低光动态场景下实现鲁棒的深度估计、位姿跟踪和 4D 重建。

**[EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting](ef-3dgs_event-aided_free-trajectory_3d_gaussian_splatting.md)**

:   EF-3DGS 首次将事件相机引入自由轨迹场景重建，通过事件生成模型（EGM）重建帧间潜在图像做连续监督、对比度最大化（CMax）结合线性事件模型（LEGM）挖掘运动信息校准位姿，以及光度 BA + Fixed-GS 策略解决颜色不一致问题，在高速场景下 PSNR 提升 3dB、ATE 降低 40%。

**[ELECTRA: A Cartesian Network for 3D Charge Density Prediction with Floating Orbitals](electra_a_cartesian_network_for_3d_charge_density_prediction_with_floating_orbit.md)**

:   ELECTRA 提出用可学习的浮动轨道（Floating Orbitals）表示电子电荷密度，通过 Cartesian 张量等变网络预测轨道位置、权重和协方差矩阵，结合对称性打破机制和去偏层，在 QM9 基准上达到 SOTA 精度同时推理速度快 170 倍，并能将 DFT 自洽场迭代减少 50%。

**[EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](enerverse_envisioning_embodied_future_space_for_robotics_manipulation.md)**

:   EnerVerse 是一个生成式机器人基础模型，通过 chunk-wise 自回归视频扩散 + 稀疏上下文记忆 + 多视角生成先验构建 4D 具身空间，结合 4DGS 数据飞轮缩小 Sim2Real 差距，最终通过策略头将 4D 世界表示转化为物理动作，在 LIBERO 基准上达到 SOTA。

**[EUGens: Efficient, Unified, and General Dense Layers](eugens_efficient_unified_and_general_dense_layers.md)**

:   EUGens 提出一类新的高效稠密层，利用随机特征（Random Features）将全连接前馈层的推理复杂度从二次降到线性，统一了已有的高效 FFL 扩展，在 LLM 预训练、ViT 图像分类、NeRF/iSDF 三维重建等任务中实现高达 27% 加速和 30% 参数压缩，且支持无需反向传播的层级知识蒸馏。

**[Evaluation of Vision-LLMs in Surveillance Video](evaluation_of_vision-llms_in_surveillance_video.md)**

:   提出一个无训练的两阶段框架，利用小型 Vision-LLM 生成视频文本描述 + NLI 分类器零样本评分，系统评估了提示策略和隐私保护滤镜对监控视频异常行为识别的影响。

**[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](every_camera_effect_every_time_all_at_once_4d_gaussian_ray_tracing_for_physics-b.md)**

:   提出 4D Gaussian Ray Tracing (4D-GRT)，将 4D Gaussian Splatting 与物理光线追踪结合，从多视角视频重建动态场景后，以可控参数生成鱼眼畸变、景深模糊、卷帘快门等物理精确的相机效果视频数据。

**[Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation](fin3r_fine-tuning_feed-forward_3d_reconstruction_models_via_monocular_knowledge_.md)**

:   提出 Fin3R，通过冻结 decoder 并用带重归一化的 LoRA 适配器对 encoder 进行单目知识蒸馏微调，以统一且轻量的方式提升 DUSt3R/MASt3R/CUT3R/VGGT 等前馈式 3D 重建模型的几何精度和鲁棒性。

**[FlareX: A Physics-Informed Dataset for Lens Flare Removal via 2D Synthesis and 3D Rendering](flarex_a_physics-informed_dataset_for_lens_flare_removal_via_2d_synthesis_and_3d.md)**

:   提出 FlareX 数据集，通过参数化模板创建、基于光照定律的 2D 合成和基于物理引擎的 3D 渲染三个阶段生成物理真实的镜头光晕数据，训练的模型在真实世界测试集上显著超越此前所有数据集。

**[Flux4D: Flow-based Unsupervised 4D Reconstruction](flux4d_flow-based_unsupervised_4d_reconstruction.md)**

:   提出 Flux4D，一个无监督且可泛化的 4D 动态驾驶场景重建框架，通过前馈网络直接预测 3D 高斯及其运动速度，仅用光度损失和静态偏好正则化实现大规模场景重建，在 PandaSet 和 Waymo 上超越所有无监督方法并接近有监督方法的性能。

**[Frequency Matters: When Time Series Foundation Models Fail Under Spectral Shift](frequency_matters_when_time_series_foundation_models_fail_under_spectral_shift.md)**

:   揭示时间序列基础模型（TSFM）在工业场景中泛化失败的关键原因——频谱偏移（downstream 数据主频与预训练数据不重叠），通过工业级手游玩家参与预测任务和受控合成实验验证了这一假说。

**[From Objects to Anywhere: A Holistic Benchmark for Multi-level Visual Grounding in 3D Scenes](from_objects_to_anywhere_a_holistic_benchmark_for_multi-level_visual_grounding_i.md)**

:   提出 Anywhere3D-Bench，首个涵盖区域/空间/物体/部件四个层级的 3D 视觉定位基准，揭示即使最强的 Gemini-2.5-Pro 和 o3 在空间级任务上仅达约 30% 准确率、部件级约 40%，远低于人类的 95%。

**[From Pixels To Views Learning Angular-Aware And Physics-Consistent Representatio](from_pixels_to_views_learning_angular-aware_and_physics-consistent_representatio.md)**

:   提出XLFM-Former用于扩展光场显微镜(XLFM)的3D重建：构建首个XLFM-Zebrafish标准化基准，设计Masked View Modeling (MVM-LF)自监督预训练学习角度先验，引入光学渲染一致性损失(ORC Loss)确保物理可信性，PSNR较SOTA提升7.7%（54.04 vs 50.16 dB）。

**[From Programs to Poses: Factored Real-World Scene Generation via Learned Program Libraries](from_programs_to_poses_factored_real-world_scene_generation_via_learned_program_.md)**

:   提出 FactoredScenes，将真实世界 3D 场景生成分解为五步因式分解——从合成数据学布局程序库、LLM 生成场景程序、执行程序获得轴对齐布局、程序条件化层次姿态预测、物体检索放置，在卧室上 FID 改善 38.3%、KID 改善 80.4%，人类仅 67% 能区分生成与真实 ScanNet。

**[Fully Dynamic Algorithms for Chamfer Distance](fully_dynamic_algorithms_for_chamfer_distance.md)**

:   提出首个全动态 Chamfer 距离维护算法，将问题归约为近似最近邻（ANN）查询，实现 $(1+\epsilon)$ 近似且更新时间 $\tilde{O}(\epsilon^{-d})$，大幅突破了静态重算的线性时间下界，在真实数据集上误差 <10% 且速度比朴素方法快数个数量级。

**[Galactification: Painting Galaxies onto Dark Matter Only Simulations Using a Transformer-Based Model](galactification_painting_galaxies_onto_dark_matter_only_simulations_using_a_tran.md)**

:   提出一个多模态 Transformer 编解码框架，以廉价的暗物质 N-body 模拟的密度场和速度场为输入，自回归生成星系目录（位置 + 物理属性），在多种统计指标上忠实再现流体动力学模拟结果，计算加速约 100 倍。

**[GauDP: Reinventing Multi-Agent Collaboration through Gaussian-Image Synergy in Diffusion Policies](gaudp_reinventing_multi-agent_collaboration_through_gaussian-image_synergy_in_di.md)**

:   提出 GauDP，通过从多智能体的去中心化 RGB 观测中构建全局一致的 3D 高斯场，并将高斯属性动态分配回各智能体的局部视角，实现可扩展的、感知增强的多智能体协作模仿学习。

**[Gaussian-Augmented Physics Simulation and System Identification with Complex Colliders](gaussian-augmented_physics_simulation_and_system_identification_with_complex_col.md)**

:   提出 AS-DiffMPM，一种支持任意形状刚体碰撞体的可微物质点法（MPM）框架，结合多种新视角合成方法实现从视觉观测中估计物体物理参数的系统辨识。

**[Gaze Beyond the Frame: Forecasting Egocentric 3D Visual Span](gaze_beyond_the_frame_forecasting_egocentric_3d_visual_span.md)**

:   提出 EgoSpanLift 方法，将第一人称 2D 注视预测提升到 3D 空间，构建多层级体积视觉跨度表示，结合 3D U-Net 和单向 Transformer 实现对未来 3D 视觉关注区域的预测。

**[GeoComplete: Geometry-Aware Diffusion for Reference-Driven Image Completion](geocomplete_geometry-aware_diffusion_for_reference-driven_image_completion.md)**

:   提出 GeoComplete，通过将投影点云作为几何条件注入双分支扩散模型，并结合 target-aware masking 策略，实现几何一致的参考驱动图像补全，PSNR 提升 17.1%。

**[GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction](geosvr_taming_sparse_voxels_for_geometrically_accurate_surface_reconstruction.md)**

:   提出基于稀疏体素的显式表面重建框架 GeoSVR，通过体素不确定性深度约束和稀疏体素表面正则化，在几何精度、细节保留和重建完整性方面全面超越现有基于 3DGS 和 SDF 的方法。

**[GOATex: Geometry & Occlusion-Aware Texturing](goatex_geometry_occlusion-aware_texturing.md)**

:   GOATex 提出首个遮挡感知的 3D 网格纹理生成框架，通过基于光线投射的 hit level 分层机制将网格分解为由外到内的可见性层，配合法线翻转和残差面聚类的两阶段可见性控制策略以及基于可见性权重的 UV 空间融合，实现了对外表面和被遮挡内表面的高质量纹理生成。

**[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](haif-gs_hierarchical_and_induced_flow-guided_gaussian_splatting_for_dynamic_scen.md)**

:   HAIF-GS 提出基于稀疏运动锚点的动态 3DGS 框架，通过锚点过滤器区分动静区域、自监督诱导场景流引导时序一致变形、以及分层锚点加密捕捉精细非刚性运动，在 NeRF-DS 和 D-NeRF 基准上取得 SOTA 渲染质量。

**[High Resolution UDF Meshing via Iterative Networks](high_resolution_udf_meshing_via_iterative_networks.md)**

:   本文提出首个针对无符号距离场（UDF）的迭代式网格化方法，通过多轮次前向传播逐步将邻域信息传播到局部体素的伪符号预测中，有效解决了高分辨率下神经 UDF 噪声导致的表面空洞和不连续问题，在多个数据集上显著优于现有单遍方法。

**[How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?](how_many_tokens_do_3d_point_cloud_transformer_architectures_really_need.md)**

:   本文系统性地揭示了 3D 点云 Transformer（如 PTv3、Sonata）中存在 90-95% 的 token 冗余，并提出 gitmerge3D——一种全局信息感知的图 token 合并方法，通过能量分数自适应合并策略实现了高达 5.3× FLOPs 降低和 6.4× 显存节省而几乎不损失精度。

**[Hybrid Physical-Neural Simulator for Fast Cosmological Hydrodynamics](hybrid_physical-neural_simulator_for_fast_cosmological_hydrodynamics.md)**

:   提出一种混合物理-神经宇宙学模拟器，用可微分粒子网格（PM）方法处理引力动力学，用物理约束的神经网络参数化气体的有效压力场，仅需单次参考模拟即可训练，在场级别和统计量级别均优于 EGD 基线。

**[Jasmine Harnessing Diffusion Prior For Self-Supervised Depth Estimation](jasmine_harnessing_diffusion_prior_for_self-supervised_depth_estimation.md)**

:   首次将Stable Diffusion视觉先验引入自监督单目深度估计：提出Mix-Batch Image Reconstruction避免自监督噪声损坏SD先验，设计Scale-Shift GRU桥接SD的尺度偏移不变性(SSI)与自监督的尺度不变性(SI)深度，在KITTI上AbsRel达0.102且泛化性强。

**[Object-Centric Representation Learning For Enhanced 3D Semantic Scene Graph Pred](object-centric_representation_learning_for_enhanced_3d_semantic_scene_graph_pred.md)**

:   通过实证分析揭示物体特征可区分性是 3D 场景图谓词预测的关键瓶颈（物体分类错误导致 92%+ 的谓词错误），提出独立对比预训练的物体编码器（3D-2D-Text 三模态对齐）+ 几何正则化关系编码器 + 双向边门控 GNN，在 3DSSG 上 Object R@1 59.53%、Predicate R@50 91.40% 均达新 SOTA。
