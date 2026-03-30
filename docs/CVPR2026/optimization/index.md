<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📐 优化/理论

**📷 CVPR2026** · 共 **5** 篇

**[Dynamic Momentum Recalibration in Online Gradient Learning](dynamic_momentum_recalibration_in_online_gradient_learning.md)**

:   从信号处理视角揭示固定动量系数在偏差-方差权衡上的固有缺陷，提出SGDF优化器，通过在线计算最优时变增益（基于最小均方误差原则）动态平衡梯度估计的噪声抑制和信号保持，在多种视觉任务上超越SGD动量和Adam变体。

**[Fed-ADE: Adaptive Learning Rate for Federated Post-adaptation under Distribution Shift](fed-ade_adaptive_learning_rate_for_federated_post-adaptation_under_distribution_.md)**

:   提出 Fed-ADE 框架，通过 uncertainty dynamics estimation 和 representation dynamics estimation 两个轻量级分布漂移信号，为每个客户端在每个时间步自适应调整学习率，实现联邦部署后无监督适应。

**[OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport](otprune_distribution-aligned_visual_token_pruning_via_optimal_transport.md)**

:   将视觉 token 裁剪建模为最优传输（OT）下的分布对齐问题，通过最小化完整与裁剪后 token 集合间的 2-Wasserstein 距离，以 Gaussian 代理 + log-det 子模目标 + 贪心 Cholesky 选择实现 training-free、$O(mk^2)$ 复杂度的高效裁剪，在 11 个多模态基准上取得 SOTA 精度-效率折中。

**[SCOPE: Semantic Coreset with Orthogonal Projection Embeddings for Federated Learning](scope_semantic_coreset_with_orthogonal_projection.md)**

:   提出SCOPE——一个无需训练的联邦coreset选择框架，利用冻结VLM(MobileCLIP)的正交投影嵌入计算三个标量语义指标(表示性/多样性/边界接近度)，实现全局感知的两阶段剪枝，在CIFAR-10/Tiny-ImageNet/UHCS上通信带宽降128-512倍的同时超越全数据训练。

**[UniFusion: A Unified Image Fusion Framework with Robust Representation and Source-Aware Preservation](unifusion_a_unified_image_fusion_framework_with_robust_representation_and_source.md)**

:   提出 UniFusion 统一图像融合框架，利用 DINOv3 自监督语义先验构建跨模态共享特征空间，通过重建对齐机制保留源图信息，并以双层优化策略解耦重建与融合目标，在红外-可见光、多曝光、多焦点、医学图像等多任务上均达到 SOTA。
