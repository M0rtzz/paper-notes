---
title: >-
  [论文解读] U2Flow: Uncertainty-Aware Unsupervised Optical Flow Estimation
description: >-
  [CVPR 2026][视频理解][光流估计] U2Flow是首个联合估计光流和逐像素不确定性的循环无监督框架，通过基于增强一致性的解耦不确定性学习和不确定性引导的双向光流融合，在KITTI和Sintel上实现无监督SOTA。
tags:
  - CVPR 2026
  - 视频理解
  - 光流估计
  - 不确定性估计
  - 无监督学习
  - 循环网络
  - 增强一致性
---

# U2Flow: Uncertainty-Aware Unsupervised Optical Flow Estimation

**会议**: CVPR 2026  
**arXiv**: [2604.10056](https://arxiv.org/abs/2604.10056)  
**代码**: [https://github.com/sunzunyi/U2FLOW](https://github.com/sunzunyi/U2FLOW)  
**领域**: 视频理解/光流估计  
**关键词**: 光流估计, 不确定性估计, 无监督学习, 循环网络, 增强一致性

## 一句话总结

U2Flow是首个联合估计光流和逐像素不确定性的循环无监督框架，通过基于增强一致性的解耦不确定性学习和不确定性引导的双向光流融合，在KITTI和Sintel上实现无监督SOTA。

## 研究背景与动机

**领域现状**：基于全对相关的深度循环模型（如RAFT）在全监督下达到SOTA，但获取大规模精确的光流标注成本高昂，推动了无监督研究。

**现有痛点**：(1) 无监督模型在遮挡、无纹理区域和大位移下产生不准确估计，这些误差对下游任务是灾难性的；(2) 不确定性估计在无监督设置下严重不足——缺乏直接监督信号且不清楚如何有效利用不确定性改进光流。

**核心矛盾**：模型不仅需要预测运动是什么，还需要量化对预测的信心——但在没有真值的情况下如何教会模型评估自己的可靠性？

**本文目标**：在纯自监督框架中实现光流和不确定性的联合估计，并用不确定性反馈改进光流。

**切入角度**：利用模型在数据增强下的预测不一致性作为不确定性的自监督信号。

**核心idea**：当模型在不同扰动下给出不一致的预测时，暴露了低置信度区域——这种不一致性本身就是不确定性的强信号。

## 方法详解

### 整体框架

继承RAFT的核心设计（特征提取→4D相关体→循环更新），新增不确定性估计头和不确定性感知精炼模块。训练使用光度损失+平滑性损失+基于增强一致性的不确定性损失。推理时利用不确定性引导的双向光流融合提升鲁棒性。

### 关键设计

1. **解耦不确定性学习策略**:

    - 功能：在无真值条件下生成不确定性监督信号
    - 核心思路：初始前向得到光流估计 $\mathbf{F}_{1\to 2}$，对图像施加强外观/空间增强得到 $(\hat{I}_1, \hat{I}_2)$，重新估计光流 $\hat{\mathbf{F}}'_{1\to 2}$。两者差异 $\hat{D}^{(k)} = \|\hat{\mathbf{F}} - \hat{\mathbf{F}}'^{(k)}\|_1$ 作为不确定性目标。使用Laplace似然MLE目标：$\tilde{\ell}_{unc} = \sqrt{2}\exp(-\frac{1}{2}\alpha^{(k)})\hat{D}^{(k)} + \frac{1}{2}\alpha^{(k)}$，其中 $\alpha = \log\sigma^2$。关键是将 $\hat{D}$ 从计算图detach，防止梯度泄漏
    - 设计动机：与监督方法将不确定性和光流耦合在单一MLE目标不同，解耦设计避免了不确定性损失干扰光流估计

2. **不确定性感知精炼模块**:

    - 功能：利用预测的不确定性引导光流迭代精炼
    - 核心思路：将不确定性权重 $\mathbf{s}^{(k)} = \phi(-\alpha^{(k)})$ 与光流特征逐元素相乘生成缩放特征 $\tilde{\mathbf{f}}^{(k)} = \mathbf{f}^{(k)} \odot \mathbf{s}^{(k)*}$。然后拼接原始特征、缩放特征和不确定性map，通过卷积头输出光流残差
    - 设计动机：高不确定性区域的特征应被抑制以减少其对精炼的负面影响

3. **不确定性引导的双向光流融合**:

    - 功能：利用前向和后向光流的不确定性互相纠正
    - 核心思路：在前向和后向光流的不确定性map之间选择更可靠的方向进行融合，替代传统的基于遮挡掩码的策略。不确定性map能更准确地识别高误差区域
    - 设计动机：传统遮挡掩码是二值的且不够精确，连续的不确定性值提供更精细的可靠性指示

### 损失函数 / 训练策略

总损失 = 光度损失(census+SSIM+L1) + 边缘感知平滑性损失 + 不确定性引导区域平滑性损失 + 增强一致性不确定性损失。KITTI上额外使用不确定性引导的单应性平滑损失。

## 实验关键数据

### 主实验

| 数据集 | 指标 | U2Flow | 之前无监督SOTA | 提升 |
|--------|------|--------|---------------|------|
| KITTI 2015 | Fl-all | SOTA | - | 显著 |
| Sintel Clean | EPE | SOTA | - | 显著 |
| Sintel Final | EPE | SOTA | - | 显著 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 无不确定性估计 | 精度下降 | 基线RAFT |
| 无解耦设计 | 训练不稳定 | 梯度泄漏 |
| 无不确定性精炼 | 精度下降 | 未利用不确定性 |
| 无双向融合 | 遮挡区域差 | 传统掩码不如不确定性 |
| 完整U2Flow | 最优 | 所有组件协同 |

### 关键发现

- 解耦设计对训练稳定性至关重要——detach操作防止不确定性损失干扰光流分支
- 不确定性map比传统前后一致性遮挡掩码更准确地标识高误差区域
- 不确定性引导的区域平滑性在KITTI上效果显著（平面刚性运动场景）

## 亮点与洞察

- **"模型自我评估"范式**：在无真值条件下通过增强一致性让模型自己暴露不确定区域，设计巧妙
- **解耦设计的重要性**：将不确定性学习与光流回归显式分离，避免了耦合目标的不稳定性
- **不确定性作为通用信号**：不仅用于最终输出，还在训练中动态调节损失权重和精炼过程

## 局限与展望

- 增强一致性策略假设增强是合理的，极端增强可能产生噪声监督
- KITTI上的单应性平滑损失依赖平面刚性假设，泛化性有限
- 不确定性标定的绝对准确性未验证（无真值对比）

## 相关工作与启发

- **vs ARFlow**: ARFlow用增强实现知识蒸馏但不估计不确定性，U2Flow将增强一致性用于不确定性学习
- **vs ProbFlow**: ProbFlow使用变分推理联合估计但需要监督，U2Flow实现了无监督的联合估计

## 评分

- 新颖性: ⭐⭐⭐⭐ 无监督联合光流-不确定性估计的首次实现
- 实验充分度: ⭐⭐⭐⭐ KITTI+Sintel双基准+详细消融
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰
- 价值: ⭐⭐⭐⭐ 不确定性估计对安全关键应用有重要意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] Unsupervised Joint Learning of Optical Flow and Intensity with Event Cameras](../../ICCV2025/video_understanding/unsupervised_joint_learning_of_optical_flow_and_intensity_with_event_cameras.md)
- [\[CVPR 2026\] Enhancing Accuracy of Uncertainty Estimation in Appearance-based Gaze Tracking with Probabilistic Evaluation and Calibration](enhancing_accuracy_of_uncertainty_estimation_in_appearance-based_gaze_tracking_w.md)
- [\[CVPR 2025\] DPFlow: Adaptive Optical Flow Estimation with a Dual-Pyramid Framework](../../CVPR2025/video_understanding/dpflow_adaptive_optical_flow_estimation_with_a_dual-pyramid_framework.md)
- [\[CVPR 2026\] LAOF: Robust Latent Action Learning with Optical Flow Constraints](laof_robust_latent_action_learning_with_optical_flow_constraints.md)
- [\[CVPR 2025\] EDCFlow: Exploring Temporally Dense Difference Maps for Event-based Optical Flow Estimation](../../CVPR2025/video_understanding/edcflow_exploring_temporally_dense_difference_maps_for_event-based_optical_flow_.md)

</div>

<!-- RELATED:END -->
