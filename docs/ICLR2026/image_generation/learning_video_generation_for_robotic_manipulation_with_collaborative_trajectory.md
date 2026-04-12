---
title: >-
  [论文解读] Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control
description: >-
  [ICLR 2026][图像生成][轨迹控制视频生成] 提出 RoboMaster，通过协作轨迹（collaborative trajectory）将机械臂与物体的交互过程分解为前交互、交互和后交互三阶段，配合外观和形状感知的物体表示，实现高质量轨迹控制的机器人操作视频生成。
tags:
  - ICLR 2026
  - 图像生成
  - 轨迹控制视频生成
  - 协作轨迹
  - 机器人操作
  - 交互建模
  - 逆动力学
---

# Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control

**会议**: ICLR 2026  
**arXiv**: [2506.01943](https://arxiv.org/abs/2506.01943)  
**代码**: [项目页](https://fuxiao0719.github.io/projects/robomaster/)  
**领域**: 视频生成 / 机器人操作  
**关键词**: 轨迹控制视频生成, 协作轨迹, 机器人操作, 交互建模, 逆动力学

## 一句话总结
提出 RoboMaster，通过协作轨迹（collaborative trajectory）将机械臂与物体的交互过程分解为前交互、交互和后交互三阶段，配合外观和形状感知的物体表示，实现高质量轨迹控制的机器人操作视频生成。

## 研究背景与动机
- 可扩展机器人学习需要大量高质量演示数据，但真实数据采集成本高
- 视频生成可作为模拟器合成训练数据，但现有轨迹控制方法（Tora、DragAnything）独立建模各物体运动
- 独立轨迹在交互区域导致特征纠缠：重叠区域的特征融合失败（如苹果消失），生成质量下降
- 逆动力学模型从低质量交互视频提取的动作不可靠，限制下游策略学习

## 方法详解

### 整体框架
RoboMaster 基于 CogVideoX-5B，输入为初始帧、文本提示、物体 mask 和协作轨迹，输出操作视频。核心是将统一轨迹分解为三个交互阶段，每个阶段由主导物体引导。

### 关键设计

1. **协作轨迹分解**: 将交互过程分解为三个子阶段：
   - 前交互 $\mathcal{C}_1$：机械臂 $\mathbf{o}_d$ 运动，物体 $\mathbf{o}_s$ 静止，用 $\mathbf{v}_d$ 引导
   - 交互 $\mathcal{C}_2$：用物体轨迹 $\mathbf{v}_s$ 引导（物体运动隐式同步机械臂）
   - 后交互 $\mathcal{C}_3$：机械臂完成撤离，再用 $\mathbf{v}_d$ 引导
   总分布分解为：$p_\theta(\mathbf{x}_1|\mathbf{I},\mathbf{c},\mathbf{v}_d,\mathcal{C}_1) \cdot p_\theta(\mathbf{x}_2|\ldots,\mathcal{C}_2) \cdot p_\theta(\mathbf{x}_3|\ldots,\mathcal{C}_3)$

2. **物体表征**: 结合外观和形状的圆柱体表示。通过 VAE 编码器将初始帧投射到潜在空间，用 mask 采样有效像素并池化得到物体嵌入 $\tilde{\mathbf{v}}$，然后在每个时间步以轨迹点为中心、mask 面积为半径构造圆柱体 $\mathbf{v} \in \mathbb{R}^{c \times h \times w}$。

3. **运动注入模块**: 协作轨迹潜在表示 $\mathbf{V}$ 经零初始化 2D 空间卷积和 1D 时间卷积编码，通过加法注入 DiT block 的隐状态：$\mathbf{h} = \mathbf{h} + \text{norm}(\tilde{\mathbf{V}}) + \tilde{\mathbf{V}}$

### 损失函数 / 训练策略
标准去噪损失：
$$\mathcal{L}(\boldsymbol{\theta}) = \mathbb{E}_{\mathbf{x},\mathbf{c},\boldsymbol{\epsilon},\mathbf{I},\mathbf{M}_d,\mathbf{M}_s,\mathcal{C},t}\left[\|\boldsymbol{\epsilon} - \hat{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t,\mathbf{c},\mathbf{M}_d,\mathbf{M}_s,\mathcal{C},t)\|_2^2\right]$$
在 8×A800 GPU 上训练 30K 步，DiT LR=2e-5，运动注入器 LR=1e-4。

## 实验关键数据

### 主实验（Bridge 数据集）
| 方法 | FVD↓ | PSNR↑ | SSIM↑ | TrajError_robot↓ | TrajError_obj↓ | 用户偏好% |
|------|------|-------|-------|-----------------|----------------|----------|
| IRASim | 159.04 | 20.88 | 0.782 | 19.25 | 34.39 | 6.45 |
| DragAnything | 158.42 | 21.13 | 0.792 | 18.97 | 27.41 | 12.90 |
| Tora | 152.28 | 21.24 | 0.788 | 18.14 | 26.43 | 17.74 |
| **RoboMaster** | **147.31** | **21.55** | **0.803** | **16.47** | **24.16** | **45.16** |

### 机器人动作规划（RLBench + SIMPLER 成功率）
| 方法 | pick up cup | put knife | open microwave | close box | pick coke can |
|------|-------------|-----------|----------------|-----------|---------------|
| OpenVLA | 0.55 | 0.46 | 0.35 | 0.45 | 0.59 |
| Tora | 0.79 | 0.82 | 0.61 | 0.72 | 0.89 |
| **RoboMaster** | **0.83** | 0.76 | 0.54 | **0.79** | **0.91** |

### 关键发现
- RoboMaster 在 8/10 任务上超越 Tora，验证了准确交互建模→更可靠动作标签的假设
- 用户偏好研究中 45.16% 首选 RoboMaster（vs Tora 17.74%）
- 物体轨迹误差从独立轨迹的 31.41（点表示）降至 24.16（mask 表示+协作轨迹）
- 对不完美输入（mask 稀疏度 90%、轨迹偏差 20%、prompt 错误 40%）鲁棒

## 亮点与洞察
- 从"分解物体"转为"分解交互过程"是关键洞察，巧妙避免了重叠区域的特征混淆
- 协作轨迹设计简化了用户标注：只需定义分阶段轨迹而非完整的双轨迹
- mask-based 物体表征比 point-based 更鲁棒，同时保持身份一致性
- 贡献了 21K 高质量视频-轨迹配对数据集

## 局限性 / 可改进方向
- 应用于域外输入时可能产生不完整或扭曲的物体
- 当前仅在 2D 像素空间操作，缺乏深度感知的 3D 控制
- 泛化到不同机器人形态仍有挑战
- 需要手动指定交互阶段的时间边界

## 相关工作与启发
- IRASim、DragAnything、Tora 等轨迹控制方法的局限性驱动本工作
- Cosmos-Predict2.5 的动作条件视频生成验证了 inverse dynamics 的有效性
- 为视频world model在机器人学习中的应用提供了更可靠的数据生成方案

## 技术细节补充
- 基于 CogVideoX-5B 架构，480×640 分辨率，37 帧
- AdamW 优化器，DiT LR=2e-5，motion injector LR=1e-4，batch=16
- 推理使用 50 DDIM 步和 CFG=6.0
- 贡献了 21K Bridge 视频-轨迹配对数据集
- 逆动力学模型为每个任务收集 300 视频-动作样本训练
- 额外微调 Cosmos-Predict2.5-2B/robot/action-cond 验证预测动作的有效性
- 覆盖 9 种操作技能：move, pick, open, close, upright, topple, pour, wipe, fold
- 使用 Grounded-SAM 或用户画笔工具获取 object mask
- 轨迹标注可用交互式界面分阶段完成，比全长双轨迹更直观
- 运动注入模块使用零初始化卷积确保初始阶段不干扰预训练模型
- 基于 Franka 和 Google Robot 两种机器人形态验证
- TesserAct（4D方法）在多数任务上表现不如纯 2D 方法，可能因训练数据不足
- 对 prompt 错误的鲁棒性：40% prompt 被替换后仍保留 96.54% PSNR
- 在 SIMPLER 基准上超越 OpenVLA，证明视频生成作为数据增强的有效性

## 评分
- 新颖性: ⭐⭐⭐⭐ 协作轨迹分解思路巧妙实用，但技术组件相对标准
- 实验充分度: ⭐⭐⭐⭐⭐ 涵盖视觉质量、轨迹精度、下游机器人规划、消融、用户研究
- 写作质量: ⭐⭐⭐⭐ 动机清晰，对比充分
- 价值: ⭐⭐⭐⭐ 对机器人操作的视频模拟训练具有直接应用价值
