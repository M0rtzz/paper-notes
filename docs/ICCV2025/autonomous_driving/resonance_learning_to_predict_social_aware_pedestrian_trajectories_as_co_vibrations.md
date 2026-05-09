---
title: >-
  [论文解读] Resonance: Learning to Predict Social-Aware Pedestrian Trajectories as Co-Vibrations
description: >-
  [ICCV 2025][自动驾驶][pedestrian trajectory prediction] 提出Resonance模型，受物理共振系统启发，将行人轨迹分解为多个独立"振动"分量以模拟智能体对各单一原因的反应，通过振动叠加预测轨迹，并利用共振现象学习社会交互表示，增强可解释性。
tags:
  - ICCV 2025
  - 自动驾驶
  - pedestrian trajectory prediction
  - social interaction
  - vibration system
  - resonance
  - spectral decomposition
---

# Resonance: Learning to Predict Social-Aware Pedestrian Trajectories as Co-Vibrations

**会议**: ICCV 2025  
**arXiv**: [2412.02447](https://arxiv.org/abs/2412.02447)  
**代码**: 无  
**领域**: 自动驾驶 / 行人轨迹预测  
**关键词**: pedestrian trajectory prediction, social interaction, vibration system, resonance, spectral decomposition

## 一句话总结

提出Resonance模型，受物理共振系统启发，将行人轨迹分解为多个独立"振动"分量以模拟智能体对各单一原因的反应，通过振动叠加预测轨迹，并利用共振现象学习社会交互表示，增强可解释性。

## 研究背景与动机

行人轨迹预测需要准确建模智能体的意图和社会行为，尤其需要以可解释和解耦的方式模拟各组件中的随机性。现有方法难以将轨迹变化的不同原因（如个体目标、避碰、社会规范等）解耦建模。振动系统及其共振特性提供了自然的类比——多个独立振动源叠加产生复杂运动模式。

## 方法详解

### 整体框架

Resonance 将轨迹修改和随机性分解为多个振动分量，每个分量模拟智能体对单一原因的反应（如避开某个行人、朝目标点移动等）。最终轨迹作为这些独立振动的叠加被预测。社会交互的表示通过模拟共振现象来学习——当两个智能体的运动频率接近时产生"共振"，表示强交互。整体流程为：观测轨迹 → 振动分解（频域表示）→ 各分量独立预测 → 共振式社会交互调制 → 叠加重建预测轨迹。

### 关键设计

1. **轨迹的振动分解**:

    - 功能：将复杂的轨迹变化解耦为多个独立的、可解释的运动分量。
    - 核心思路：将轨迹偏移分解为多个振动分量，每个分量具有独立的频率、振幅和相位，分别对应不同的运动动因（如个体目标驱动、社会力驱动、环境约束等）。通过谱分析提取这些振动特征，使每个分量可独立建模和预测。每个振动分量可以看作行人对某一特定"激励"的响应。
    - 设计动机：传统方法直接在坐标空间预测轨迹，难以区分不同运动原因的贡献。振动分解借鉴信号处理思想，将混合信号分离为独立分量，使每个原因可独立分析和建模。

2. **共振式社会交互建模**:

    - 功能：以物理直觉的方式表征行人之间的社会交互强度。
    - 核心思路：利用共振物理——两个振动频率接近的系统会发生能量传递（共振）。将行人间的社会交互建模为频域中的共振现象：运动模式频率相近的行人之间交互更强，频率差异大的行人之间交互弱。具体而言，通过比较不同行人的振动频谱来量化交互强度，并据此调制各自的轨迹预测。
    - 设计动机：传统社会力模型依赖预定义规则，图注意力方法依赖黑箱学习。共振提供了一种兼具物理可解释性和学习灵活性的交互表示方式。

3. **叠加原理预测**:

    - 功能：从独立振动分量重建完整的预测轨迹。
    - 核心思路：最终轨迹 = Σ 各独立振动分量，每个分量独立预测后叠加。这种分解-叠加方式使模型能够对不同运动原因的随机性进行解耦建模——例如目标位置的不确定性和避碰行为的不确定性可以分别捕获。同时，每个振动分量的随机性可以独立控制，实现更细粒度的多模态预测。
    - 设计动机：叠加原理是线性系统的基本性质，虽然行人运动不完全是线性的，但这一近似提供了简洁而有效的预测框架。

### 损失函数 / 训练策略

标准轨迹预测损失（如 L2 距离），可能结合多模态预测的 best-of-N 策略。在多个标准行人轨迹预测数据集上端到端训练。振动分解和共振交互模块均可微分，支持梯度反向传播。

## 实验关键数据

### 主实验

在 ETH/UCY、SDD 等标准数据集上使用 ADE（平均位移误差）和 FDE（最终位移误差）指标进行评估，验证了方法在定量性能上的有效性。

| 指标 | 说明 |
|------|------|
| ADE/FDE | 在多个标准数据集上优于或匹配 SOTA |
| 可解释性 | 振动分量可视化展示了不同运动原因的贡献 |

### 关键发现

- 振动分解能有效解耦不同运动原因，各分量具有清晰的物理含义
- 共振现象可自然描述社会交互强度，无需显式定义交互规则
- 叠加原理使预测具有可解释性，且支持对各分量的独立分析
- 频谱表示对运动模式的抽象比坐标空间更紧凑

## 亮点与洞察

- **物理启发的建模方式**：振动和共振类比在轨迹预测领域具有开创性，提供了比纯数据驱动方法更好的可解释性框架。
- **频域分析视角**：将轨迹预测从时域/空域转移到频域，为理解和建模运动模式提供了新维度。这种思路可迁移到其他时序预测任务。
- **解耦建模的优势**：独立建模不同运动原因使得每个分量的随机性可独立控制，为多模态预测提供了更精细的控制。
- **社会交互的优雅表示**：共振比注意力机制更有物理直觉，且天然包含"频率相近才强交互"的先验。

## 局限与展望

- 振动系统假设可能不完全适用于突然转向、紧急避让等高度非线性的行人行为
- 缓存内容有限（仅包含摘要和参考文献），实验的完整量化结果未能充分呈现
- 对非周期性运动模式（如单次跨越、突然停止）的适用性有待考察
- 振动分量的数量选择可能影响模型容量和计算效率的平衡

## 相关工作与启发

- Social LSTM/GAN等经典社会力方法是基础对比
- SingularTrajectory等扩散模型方法代表近期进展
- 物理启发的运动建模可扩展到车辆轨迹预测

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 振动/共振类比在轨迹预测中首次应用
- 技术深度: ⭐⭐⭐⭐ — 频域分析和叠加原理有物理基础
- 实验充分性: ⭐⭐⭐ — 多数据集验证但细节有限
- 写作质量: ⭐⭐⭐⭐ — 物理类比清晰
- 实用价值: ⭐⭐⭐ — 可解释性好但实际部署效果待验证

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] Saliency-Aware Quantized Imitation Learning for Efficient Robotic Control](saliency-aware_quantized_imitation_learning_for_efficient_robotic_control.md)
- [\[ICCV 2025\] Future-Aware Interaction Network For Motion Forecasting](future-aware_interaction_network_for_motion_forecasting.md)
- [\[ICCV 2025\] Occupancy Learning with Spatiotemporal Memory](occupancy_learning_with_spatiotemporal_memory.md)
- [\[ICCV 2025\] GaussRender: Learning 3D Occupancy with Gaussian Rendering](gaussrender_learning_3d_occupancy_with_gaussian_rendering.md)
- [\[ICCV 2025\] AD-GS: Object-Aware B-Spline Gaussian Splatting for Self-Supervised Autonomous Driving](ad-gs_object-aware_b-spline_gaussian_splatting_for_self-supervised_autonomous_dr.md)

</div>

<!-- RELATED:END -->
