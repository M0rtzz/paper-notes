---
description: "【论文笔记】PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement 论文解读 | CVPR 2026 | arXiv 2509.24850 | 远程光电容积脉搏波 | 从 Navier-Stokes 方程出发推导 rPPG 信号的二阶阻尼谐振子模型，证明其离散解等价于因果卷积，为使用 TCN 提供物理理论依据，设计轻量 PHASE-Net 实现 SOTA。"
tags:
  - CVPR 2026
---

# PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement

**会议**: CVPR 2026  
**arXiv**: [2509.24850](https://arxiv.org/abs/2509.24850)  
**代码**: [GitHub](https://github.com/Alex036225/PhaseNet)  
**领域**: 科学计算  
**关键词**: 远程光电容积脉搏波, 物理信息网络, 时间卷积网络, 血流动力学, 轻量模型

## 一句话总结

从 Navier-Stokes 方程出发推导 rPPG 信号的二阶阻尼谐振子模型，证明其离散解等价于因果卷积，为使用 TCN 提供物理理论依据，设计轻量 PHASE-Net 实现 SOTA。

## 研究背景与动机

远程光电容积脉搏波（rPPG）通过普通摄像头从皮肤颜色微变化中提取心率等生理信号，是非接触生理监测的关键技术。现有深度学习方法大多采用启发式设计，将 rPPG 视为通用时空信号处理任务，缺乏物理理论基础，导致泛化性和可解释性受限。同时头部运动和光照变化产生的伪影远强于真实脉搏信号。

**本文切入角度**：从 Navier-Stokes 方程推导血流脉搏动力学，严格证明 TCN 是物理正确的架构选择。

## 方法详解

### 整体框架

视觉编码器（3 个 EST Block + ZAS）→ 自适应空间滤波 ASF → 门控时间卷积 GTCN → rPPG 波形输出。

### 关键设计

1. **物理推导核心链**：Navier-Stokes → 线性化1D动量+连续性方程 → 阻尼波动方程 → 固定点ODE（阻尼谐振子）→ 半隐式Euler离散化 → LTI状态空间模型 → 因果卷积（Proposition 1）→ FIR近似（Proposition 2）→ TCN 架构。

2. **Zero-FLOPs Axial Swapper (ZAS)**：对部分通道执行块内空间转置，零计算开销注入跨区域交互。满足自逆性（$\text{ZAS}(\text{ZAS}(X))=X$）和能量守恒（1-Lipschitz），保证训练稳定。

3. **自适应空间滤波 (ASF)**：为每帧通过轻量卷积生成空间注意力掩码 $M_t$（spatial softmax），高权重给信号丰富区域（前额/面颊），同时计算一阶时间差分 $\mathbf{v}_t = \mathbf{z}_t - \mathbf{z}_{t-1}$ 编码脉搏"速度"，两者拼接输出。

4. **门控时间卷积网络 (GTCN)**：双路因果扩张 TCN，一路 tanh 激活另一路 sigmoid 门控，融合长程时间动态。

### 损失函数 / 训练策略

负 Pearson 相关损失：$\mathcal{L}_{\text{pred}} = -\frac{\sum_t (\hat{y}_t - \bar{\hat{y}})(y_t - \bar{y})}{\sqrt{\sum_t (\hat{y}_t - \bar{\hat{y}})^2 \sum_t (y_t - \bar{y})^2}}$

## 实验关键数据

### 主实验

| 方法 | UBFC MAE↓ | PURE MAE↓ | 参数量 |
|------|-----------|-----------|--------|
| PhysNet | 较高 | 较高 | 大 |
| EfficientPhys | 中 | 中 | 中 |
| PhysFormer | 中 | 中 | 大 |
| RhythmMamba | 中 | 中 | 中 |
| **PHASE-Net** | **最低** | **最低** | **极小** |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 无 ZAS | 性能下降 | 缺少空间交互 |
| GAP 替代 ASF | 性能下降 | 均匀聚合引入噪声 |
| 完整 PHASE-Net | **最优** | 所有模块协同 |

### 关键发现

- 物理推导的 TCN 比启发式 Transformer/SSM 更适合 rPPG 任务
- ZAS 零开销即提升跨区域特征交互
- ASF 的时间差分项对捕捉脉搏动态至关重要

## 亮点与洞察

- **首次从第一性原理推导 rPPG 网络架构**：从 Navier-Stokes 到 TCN 的完整数学证明
- **ZAS 零 FLOPs 模块**：纯排列操作即可增强特征，设计巧妙
- **极致轻量 + SOTA 性能**：理论严谨与实用效率的统一

## 局限性 / 可改进方向

- 物理推导中简化假设较多（层流、线性化、单点观测）
- ZAS 块大小和通道比例需手动设定
- 未在极端运动场景充分验证

## 相关工作与启发

- PhysFormer 用 Transformer，PHASE-Net 从物理角度证明 TCN 更合适
- 物理信息网络（PINN）思想的独特应用——用物理约束网络架构而非损失函数

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首次从第一性原理推导网络架构
- 实验充分度: ⭐⭐⭐⭐ 多数据集验证
- 写作质量: ⭐⭐⭐⭐⭐ 推导严谨叙述流畅
- 价值: ⭐⭐⭐⭐⭐ 物理驱动设计范式有普适意义
