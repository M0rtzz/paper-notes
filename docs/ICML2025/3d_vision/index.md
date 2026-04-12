---
title: >-
  ICML2025 3D视觉方向 12篇论文解读
description: >-
  12篇ICML2025 3D视觉方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧊 3D视觉

**🧪 ICML2025** · 共 **12** 篇

**[Evomesh Adaptive Physical Simulation With Hierarchical Graph Evolutions](evomesh_adaptive_physical_simulation_with_hierarchical_graph_evolutions.md)**

:   EvoMesh 提出一种全可微的层次图演化框架，通过各向异性消息传递（AMP）和基于 Gumbel-Softmax 的可微节点选择（DiffSELECT），根据物理输入自适应构建随时间演化的多尺度图层次结构，在五个物理仿真基准上平均超越固定层次方法约 20%。

**[Flowdrag 3D-Aware Drag-Based Image Editing With Mesh-Guided Deformation Vector F](flowdrag_3d-aware_drag-based_image_editing_with_mesh-guided_deformation_vector_f.md)**

:   提出 FlowDrag，通过从图像构建 3D 网格并利用 SR-ARAP 变形传播拖拽信息生成 2D 向量流场，解决了现有 drag-based 编辑方法的几何不一致性问题。

**[Freemesh Boosting Mesh Generation With Coordinates Merging](freemesh_boosting_mesh_generation_with_coordinates_merging.md)**

:   提出 Per-Token-Mesh-Entropy（PTME）度量免训练评估网格 tokenizer 质量，并引入基于 BPE 的坐标合并技术（RMC）进一步压缩网格序列，在 MeshXL/MeshAnythingV2/EdgeRunner 上验证了压缩率和生成质量的同步提升。

**[Gaprompt Geometry-Aware Point Cloud Prompt For 3D Vision Model](gaprompt_geometry-aware_point_cloud_prompt_for_3d_vision_model.md)**

:   提出 GAPrompt，面向预训练 3D 视觉模型的几何感知点云提示方法，通过 Point Prompt、Point Shift Prompter 和 Prompt Propagation 三组件利用几何线索增强适配能力，仅用 2.19% 可训练参数达到接近全量微调的性能。

**[High Dynamic Range Novel View Synthesis With Single Exposure](high_dynamic_range_novel_view_synthesis_with_single_exposure.md)**

:   首次提出仅使用单曝光LDR图像进行HDR新视角合成（HDR-NVS）的问题设定，并设计了一个基于相机成像原理的元算法框架Mono-HDR-3D，通过LDR→HDR颜色转换器（L2H-CC）和HDR→LDR闭环转换器（H2L-CC）实现无HDR监督下的HDR场景建模。

**[Physicsnerf Physics-Guided 3D Reconstruction From Sparse Views](physicsnerf_physics-guided_3d_reconstruction_from_sparse_views.md)**

:   PhysicsNeRF 提出了一个基于物理先验的稀疏视角 NeRF 框架，通过深度排序、跨视角一致性、稀疏性正则和渐进训练四种互补约束，在仅 8 个视角下实现 21.4 dB 的 PSNR，并对稀疏视角下过拟合的本质进行了深入的理论分析。

**[Probabilistic Interactive 3D Segmentation With Hierarchical Neural Processes](probabilistic_interactive_3d_segmentation_with_hierarchical_neural_processes.md)**

:   提出 NPISeg3D，基于层级神经过程（Hierarchical NPs）的概率性交互式 3D 分割框架，通过场景级和物体级隐变量结构增强少样本泛化，同时提供可靠的不确定性估计。

**[Refersplat Referring Segmentation In 3D Gaussian Splatting](refersplat_referring_segmentation_in_3d_gaussian_splatting.md)**

:   ReferSplat 提出了 Referring 3D Gaussian Splatting Segmentation（R3DGS）新任务，通过构建 3D Gaussian Referring Fields、位置感知跨模态交互模块和 Gaussian-Text 对比学习，实现了基于自然语言描述在 3DGS 场景中分割目标物体（包括遮挡/不可见物体），在新构建的 Ref-LERF 数据集和开放词汇分割基准上取得 SOTA。

**[Se3-Equivariant Diffusion Policy In Spherical Fourier Space](se3-equivariant_diffusion_policy_in_spherical_fourier_space.md)**

:   提出 Spherical Diffusion Policy（SDP），通过将状态、动作和去噪过程嵌入球面傅里叶空间实现端到端 SE(3) 等变的闭环操作策略，在 20 个仿真和 5 个真机任务上大幅超越基线。

**[Tackling View-Dependent Semantics In 3D Language Gaussian Splatting](tackling_view-dependent_semantics_in_3d_language_gaussian_splatting.md)**

:   提出LaGa解决3D高斯场景理解中被忽视的"视角依赖语义"问题：通过3D场景分解建立跨视角语义连接，用自适应聚类+重加权构建视角聚合语义表示，在LERF-OVS上mIoU超前SOTA+18.7%。

**[Thickness-Aware E3-Equivariant 3D Mesh Neural Networks](thickness-aware_e3-equivariant_3d_mesh_neural_networks.md)**

:   提出 T-EMNN，通过引入厚度感知的消息传递机制和基于 PCA 的数据驱动坐标系，在保持表面网格计算效率的同时建模对立面之间的厚度交互，实现 E(3)-等变/不变的节点级 3D 形变预测。

**[Vtgaussian-Slam Rgbd Slam For Large Scale Scenes With Splatting View-Tied 3D Gau](vtgaussian-slam_rgbd_slam_for_large_scale_scenes_with_splatting_view-tied_3d_gau.md)**

:   提出视图绑定3D高斯（View-Tied 3D Gaussians），将高斯绑定到深度像素上并简化为球形，大幅节省存储开销，配合仅优化最近视图相关高斯的tracking/mapping策略，实现面向大规模场景的可扩展RGBD SLAM系统。
