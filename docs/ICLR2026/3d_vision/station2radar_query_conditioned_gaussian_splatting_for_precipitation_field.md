---
title: >-
  [论文解读] Station2Radar: Query-Conditioned Gaussian Splatting for Precipitation Field
description: >-
  [ICLR 2026][3D视觉][降水场生成] 提出QCGS(Query-Conditioned Gaussian Splatting)——首个将气象站观测+卫星图像融合生成降水场的框架(无需雷达)：关键洞察→传统高斯加权插值=高斯溅射的特例→QCGS学习自适应高斯参数+选择性只渲染降水区域→比传统网格化降水产品RMSE降低50%+→分辨率灵活/实时生成。
tags:
  - ICLR 2026
  - 3D视觉
  - 降水场生成
  - 高斯溅射
  - 查询条件
  - 气象站+卫星融合
  - 无雷达
---

# Station2Radar: Query-Conditioned Gaussian Splatting for Precipitation Field

**会议**: ICLR 2026  
**arXiv**: [2603.00418](https://arxiv.org/abs/2603.00418)  
**领域**: 气象AI/3D表示  
**关键词**: 降水场生成, 高斯溅射, 查询条件, 气象站+卫星融合, 无雷达

## 一句话总结

提出QCGS(Query-Conditioned Gaussian Splatting)——首个将气象站观测+卫星图像融合生成降水场的框架(无需雷达)：关键洞察→传统高斯加权插值=高斯溅射的特例→QCGS学习自适应高斯参数+选择性只渲染降水区域→比传统网格化降水产品RMSE降低50%+→分辨率灵活/实时生成。

## 研究背景与动机

**领域现状**：降水预测→雷达精度高but覆盖有限/昂贵; 气象站→精确but稀疏; 卫星→密集but无法直接反演降水量。

**现有痛点**：
   - (1) 雷达覆盖地理受限→全球大片区域无雷达
   - (2) 统计插值(Barnes/Kriging)→模糊锐利边界→对站密度敏感
   - (3) Sat2Radar→固定分辨率+大偏差
   - (4) 融合方法→固定网格→不支持分辨率灵活

**切入角度**：高斯加权插值≡高斯溅射→但可学习参数→从卫星+站点上下文条件化。

## 方法详解

### 核心洞察

传统插值: $f_{GW}(x) = \frac{\sum K_\sigma(x-\mu_i)y_i}{\sum K_\sigma(x-\mu_j)}$ → 固定高斯核
高斯溅射: $f_{GS}(x) = \sum a_i K_{\Sigma_i}(x-\mu_i)$ → 可学习振幅+各向异性协方差

→ 传统插值是GS的特例(固定等向核)

### QCGS三组件

1. **雷达点提议网络**：
    - 从卫星图像→识别降水支撑位置
    - 只在降水区域放置高斯→非降水区域不计算→高效

2. **INR参数预测网络**：
    - 对每个提议点→预测高斯参数(位置/振幅/协方差)
    - 条件：卫星上下文+附近站点观测

3. **选择性渲染**：
    - 只渲染被查询的降水区域→与标准GS(渲染全图)不同
    - 大幅减少计算→降水通常只覆盖部分区域

### 分辨率灵活

- 连续场表示→可在任意分辨率查询→不限于固定网格

## 实验关键数据

| 方法 | RMSE↓ | 分辨率灵活 | 需雷达 |
|------|-------|----------|--------|
| 传统网格化 | 基线 | 否 | 否 |
| Sat2Radar | 中 | 否 | 否(但训练需) |
| **QCGS** | **-50%+** | **是** | **否** |

### 关键发现

- 50%+ RMSE改善→非常显著→降水是高影响天气变量
- 各向异性高斯→比等向→能更好表示锐利降水边界
- 选择性渲染→只在降水区域计算→非降水区域(通常>70%面积)完全跳过
- 跨空间/时间尺度→性能一致

## 亮点与洞察

- **"气象插值=高斯溅射"的重新认识**→简单但深刻→将60年的气象方法和最新3D表示连接。
- **无雷达生成降水场**→巨大实用意义→全球大量地区无雷达覆盖。
- **选择性渲染**→GS的改进→不只是气象→任何稀疏信号场景都适用。
- **连续分辨率**→用户可在任意尺度查询→比固定网格灵活得多。


## 局限性 / 可改进方向

- We introduced Query-Conditioned Gaussian Splatting (QCGS), a framework for generating high-quality precipitation fields from sparse and heterogeneous observations.

- By treating each observation as a Gaussian kernel and conditioning splatting on satellite imagery, QCGS selectively renders rainfall regions, reducing computation while preserving sharp boundaries.

- The integration of Implicit Neural Representations further enables resolution-free parameterization and improved generalization across regions and seasons.

- Extensive experiments indicate that QCGS reduces representativeness errors, reconstructs rainfall even in gauge-sparse settings, and produces resolution-flexible fields that align closely with radar observations.

- These outputs are valuable not only for data assimilation but also as high-quality training data for data-driven forecasting, bridging the gap between point-based and gridded products.


## 相关工作与启发

- **vs Neural Representations**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs Gaussian Splatting**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs NeRF**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs GaussianImage**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 高斯溅射用于气象场生成的首次探索+查询条件化
- 实验充分度: ⭐⭐⭐⭐ 多时空尺度+与基准产品对比
- 写作质量: ⭐⭐⭐⭐⭐ 核心洞察阐述清晰
- 价值: ⭐⭐⭐⭐⭐ 对气象AI有直接实用影响
