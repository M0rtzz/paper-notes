---
title: >-
  [论文解读] Fourier Angle Alignment for Oriented Object Detection in Remote Sensing
description: >-
  [CVPR 2026][目标检测][旋转目标检测] 利用傅里叶旋转等变性在频域估计并对齐目标方向，提出 FAAFusion（解决 Neck 层方向不一致）和 FAA Head（解决检测头分类-回归任务冲突）两个即插即用模块，在 DOTA 和 HRSC2016 上达到新 SOTA。
tags:
  - CVPR 2026
  - 目标检测
  - 旋转目标检测
  - 傅里叶变换
  - 方向对齐
  - 特征融合
  - 遥感
---

# Fourier Angle Alignment for Oriented Object Detection in Remote Sensing

**会议**: CVPR 2026  
**arXiv**: [2602.23790](https://arxiv.org/abs/2602.23790)  
**代码**: https://github.com/gcy0423/Fourier-Angle-Alignment (有)  
**领域**: 遥感 / 目标检测  
**关键词**: 旋转目标检测, 傅里叶变换, 方向对齐, 特征融合, 遥感

## 一句话总结

利用傅里叶旋转等变性在频域估计并对齐目标方向，提出 FAAFusion（解决 Neck 层方向不一致）和 FAA Head（解决检测头分类-回归任务冲突）两个即插即用模块，在 DOTA 和 HRSC2016 上达到新 SOTA。

## 研究背景与动机

遥感图像中的目标方向任意，旋转目标检测 (ROD) 需同时预测类别和方向角。现有方法从旋转敏感卷积、backbone 修改、角度回归损失等入手，但存在两个被忽视的核心瓶颈：

**Neck 层方向不一致 (Directional Incoherence)**：FPN 高层特征语义强但方向模糊（低频），低层特征边缘清晰方向精确（高频），简单相加导致方向信号冲突
**检测头任务冲突 (Task Conflict)**：分类需旋转不变特征，回归需旋转敏感特征，单一 RoI 特征无法同时满足

核心洞察：**傅里叶旋转等变性**——空间域信号旋转 phi，频谱也精确旋转 phi。可在频域可靠估计目标主方向并显式对齐。

## 方法详解

### 整体框架

FAA 含两个即插即用模块：FAAFusion 嵌入 FPN 解决方向不一致；FAA Head 替换检测头解决任务冲突。两者共享傅里叶角度估计核心。

### 关键设计

1. **傅里叶角度估计 (Fourier Angle Estimation)**

    - 做什么：从频域估计特征图主方向
    - 核心思路：2D DFT -> 中心化 -> 极坐标能量谱 -> 径向求和得角度能量分布 -> 取最大值
    - 数学基础：矩形目标功率谱中主谱方向垂直于长轴（sinc 函数衰减差异）
    - 设计动机：利用傅里叶旋转等变性，物理可解释性强

2. **FAAFusion（方向一致特征融合）**

    - 做什么：替换 FPN 逐元素加法，对齐高低层特征方向后融合
    - 核心思路：高层上采样 -> 1x1 卷积+unfold 提取局部特征 -> 估计低层主方向 -> 旋转高层对齐 -> fold+三路相加
    - 设计动机：低层方向精确（高频边缘），以其为基准对齐高层模糊方向

3. **FAA Head（方向感知检测头）**

    - 做什么：预对齐 RoI 特征到规范方向，解耦分类和回归
    - 核心思路：估计主方向旋转到 0 度得 F_inv -> 残差 F_final = F_inv + F_roi -> 两层 FC -> 分类回归
    - 设计动机：F_inv 旋转不变利于分类，F_roi 保留方向敏感信息利于回归

### 损失函数 / 训练策略

Oriented R-CNN 标准损失，AdamW (wd 0.05)，DOTA lr 0.0001，HRSC lr 0.0004，batch 2，单卡 RTX 3090。DOTA 16 epochs，HRSC 36 epochs。

## 实验关键数据

### 主实验

| 数据集 | 方法 | Backbone | mAP | 提升 |
|--------|------|----------|-----|------|
| DOTA-v1.0 | LSKNet | LSKNet-S | 77.49% | - |
| DOTA-v1.0 | **LSKNet+ours** | LSKNet-S | **78.49%** | +1.00% |
| DOTA-v1.0 | **S-RCNN+ours** | StripNet-S | **78.72%** | +0.63% (新SOTA) |
| DOTA-v1.5 | PKINet | PKINet-S | 71.47% | - |
| DOTA-v1.5 | **LSKNet+ours** | LSKNet-S | **72.28%** | +2.02% (新SOTA) |
| HRSC2016 | O-RCNN | ResNet50 | 64.77 | - |
| HRSC2016 | **O-RCNN+ours** | ResNet50 | **66.94** | +2.17% |

### 消融实验

| FAAFusion | FAA Head | Params | GFLOPs | mAP |
|-----------|----------|--------|--------|-----|
| No | No | 30.98M | 173.68G | 77.49% |
| No | Yes | 48.35M | 177.15G | 78.27% (+0.78%) |
| Yes | No | - | - | 77.91% (+0.42%) |
| Yes | Yes | 48.34M | 176.57G | **78.49%** (+1.00%) |

### 关键发现

- 两模块互补：FAAFusion +0.42%，FAA Head +0.78%，组合 +1.00%
- 三个 backbone 上一致有效，证明即插即用
- DOTA-v1.5 提升更显著（+2.02%），小目标方向对齐尤为重要
- HRSC2016 船舶检测提升最大（+2.17%），高长宽比目标频域方向估计优势明显

## 亮点与洞察

- 频域角度切入旋转目标检测非常新颖，物理可解释性强
- FAAFusion 以低层精确方向为基准对齐高层模糊方向，直觉精准
- FAA Head 残差设计简洁有效
- 即插即用可集成到任何 FPN+检测头框架

## 局限性 / 可改进方向

- 参数增加较多（O-RCNN 41M->63M），可考虑更轻量设计
- 假设目标为矩形，不规则形状可能不适用
- 仅在 Oriented R-CNN 框架验证
- unfold/fold 在高分辨率特征图上开销可能较大

## 相关工作与启发

- 与 FreqFusion 不同：后者分解高低频组件，FAA 直接利用旋转等变性
- ReDet 更重的旋转等变 backbone 方案，FAA 更轻量灵活
- 频域方向估计可扩展到实例分割、姿态估计

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 频域旋转等变性切入旋转目标检测，理论清晰视角全新
- 实验充分度: ⭐⭐⭐⭐ 三个数据集三个 backbone，消融完整
- 写作质量: ⭐⭐⭐⭐ 理论推导详尽，问题定义清晰
- 价值: ⭐⭐⭐⭐⭐ 即插即用+一致提升+物理可解释
