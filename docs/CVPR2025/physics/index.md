---
title: >-
  CVPR2025 物理/科学计算论文汇总 · 4篇论文解读
description: >-
  4篇CVPR2025的物理/科学计算方向论文解读，涵盖模型压缩、扩散模型、多模态等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2025"
  - "物理/科学计算"
  - "论文解读"
  - "论文笔记"
  - "模型压缩"
  - "扩散模型"
  - "多模态"
item_list:
  - u: "accurate_differential_operators_for_hybrid_neural_fields/"
    t: "Accurate Differential Operators for Hybrid Neural Fields"
  - u: "atp_adaptive_threshold_pruning_for_efficient_data_encoding_in_quantum_neural_net/"
    t: "ATP: Adaptive Threshold Pruning for Efficient Data Encoding in Quantum Neural Networks"
  - u: "difffno_diffusion_fourier_neural_operator/"
    t: "DiffFNO: Diffusion Fourier Neural Operator"
  - u: "towards_faithful_multimodal_concept_bottleneck_models/"
    t: "Towards Faithful Multimodal Concept Bottleneck Models"
item_total: 4
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚛️ 物理/科学计算

**📷 CVPR2025** · **4** 篇论文解读

📌 **同领域跨会议浏览：** [🧪 ICML2026 (24)](../../ICML2026/physics/index.md) · [📷 CVPR2026 (5)](../../CVPR2026/physics/index.md) · [🔬 ICLR2026 (14)](../../ICLR2026/physics/index.md) · [🤖 AAAI2026 (14)](../../AAAI2026/physics/index.md) · [🧠 NeurIPS2025 (54)](../../NeurIPS2025/physics/index.md) · [📹 ICCV2025 (2)](../../ICCV2025/physics/index.md)

**[Accurate Differential Operators for Hybrid Neural Fields](accurate_differential_operators_for_hybrid_neural_fields.md)**

:   揭示混合神经场（如 Instant NGP）中自动微分产生的梯度和曲率存在严重高频噪声问题，提出基于局部多项式拟合的后处理微分算子和自监督微调方法，将梯度误差降低 4 倍、曲率误差降低 4 倍，在渲染和物理模拟中显著消除伪影。

**[ATP: Adaptive Threshold Pruning for Efficient Data Encoding in Quantum Neural Networks](atp_adaptive_threshold_pruning_for_efficient_data_encoding_in_quantum_neural_net.md)**

:   提出 ATP（Adaptive Threshold Pruning），在量子数据编码前自适应地剪除低信息量的数据特征，通过 L-BFGS-B 优化阈值，在 MNIST/FashionMNIST/CIFAR/PneumoniaMNIST 四个数据集的二分类任务上取得最高准确率的同时显著降低纠缠熵。

**[DiffFNO: Diffusion Fourier Neural Operator](difffno_diffusion_fourier_neural_operator.md)**

:   提出 DiffFNO，将加权傅里叶神经算子（WFNO）与扩散框架结合用于任意尺度超分辨率，通过模式再平衡（Mode Rebalancing）保留关键高频分量，门控融合机制融合频域和空间域特征，自适应步长 ODE 求解器加速推理，在多个基准上超越现有方法 2-4 dB PSNR。

**[Towards Faithful Multimodal Concept Bottleneck Models](towards_faithful_multimodal_concept_bottleneck_models.md)**

:   提出 f-CBM，一个基于 CLIP 的忠实多模态 Concept Bottleneck Model 框架，通过可微分的 leakage 损失和 Kolmogorov-Arnold Network 预测头联合解决概念检测准确性和信息泄漏问题，在任务精度、概念检测和 leakage 三者间达到最优权衡。
