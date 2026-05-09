---
title: >-
  [论文解读] A2P: Anomaly to Prompt for Forecasting Future Anomalies in Time Series
description: >-
  [ICML2025][时间序列][异常预测] 提出A2P框架解决"异常预测(AP)"新任务——预测未来哪些时间点会发生异常，通过Anomaly-Aware Forecasting让预测模型学习异常关系+Synthetic Anomaly Prompting用可学习prompt模拟多样异常模式。
tags:
  - ICML2025
  - 时间序列
  - 异常预测
  - Anomaly-Aware Forecasting
  - 提示学习
  - 异常合成
---

# A2P: Anomaly to Prompt for Forecasting Future Anomalies in Time Series

**会议**: ICML2025  
**arXiv**: [2506.23596](https://arxiv.org/abs/2506.23596)  
**代码**: [GitHub - A2P](https://github.com/KU-VGI/AP)  
**领域**: 时间序列  
**关键词**: 异常预测, 时间序列, Anomaly-Aware Forecasting, Prompt Pool, 异常合成

## 一句话总结
提出A2P框架解决"异常预测(AP)"新任务——预测未来哪些时间点会发生异常，通过Anomaly-Aware Forecasting让预测模型学习异常关系+Synthetic Anomaly Prompting用可学习prompt模拟多样异常模式。

## 研究背景与动机

### 核心矛盾

**核心矛盾**：- AD：检测过去信号中的异常点
- AP：预测未来信号中何时会出现异常
AP更具实际价值但几乎未被探索。

### 朴素组合失败

简单将预测模型+检测模型串联会失败：预测模型用正常信号训练，会平滑掉异常特征，使检测模型无法识别。

### A2P的目标

让预测模型学会保留（甚至生成）异常特征，使后续检测成为可能。

## 方法详解

### Anomaly-Aware Forecasting (AAF)
预训练异常感知网络学习"某时间点异常概率"：
- 学习异常信号的关系模式
- 让预测网络理解异常的存在
- 解决"预测模型平滑掉异常"的根本问题

### Synthetic Anomaly Prompting (SAP)
用可学习Anomaly Prompt Pool(APP)增强检测：
- 每个prompt是"将正常信号变为异常"的指令
- 信号自适应prompt调优
- 专用损失引导prompt学习异常特征
- 增加了训练信号的多样性

### 共享骨干架构
预测和检测共用一个backbone：
- 学习统一表示
- 减少模型数量
- 提升整体效率和性能

## 实验关键数据

### 异常预测 vs 异常检测 对比

| 方法 | AD F1(过去信号) | AP F1(预测信号) |
|------|---------------|----------------|
| 预测+检测串联 | 高 | 低(失败) |
| **A2P** | 高 | **高** |

### 多数据集AP结果

| 数据集 | SOTA AD方法做AP | A2P |
|--------|---------------|-----|
| MBA | 低(~30%) | **75%+** |
| SMD | 低(~25%) | **68%+** |
| PSM | 低(~20%) | **62%+** |

### 消融实验

| 配置 | AP F1 |
|------|------|
| 仅预测+检测 | 30% |
| +AAF | 55% |
| +SAP | 52% |
| +AAF+SAP(A2P) | **75%** |

### 关键发现
1. AAF和SAP两个组件互补，缺一不可
2. 朴素串联方法在AP上几乎完全失败
3. Prompt Pool的多样性对检测鲁棒性至关重要
4. 共享骨干比分离模型更高效且更好
5. 在多种未来长度设置上一致有效

## 亮点与洞察

1. AP是一个清晰且重要的新任务定义。
2. 对"预测模型平滑掉异常"的诊断非常精准。
3. 可学习Anomaly Prompt Pool的设计优雅——无需人工定义异常模式。
4. 共享骨干的统一架构简化了系统设计。
5. 对医疗预警和工业预测性维护有直接应用价值。

## 局限与展望 / 可改进方向

1. AP任务的标准化评估协议仍需社区共识。
2. 预测窗口越长AP越难——极长预测的效果不确定。
3. Prompt数量是需要调优的超参。
4. 对新型异常模式的泛化能力未充分测试。
5. 因果解释（为什么会异常）不在框架范围内。

## 相关工作与启发

- 与Jhin et al.(2023)的区别：它们只能检测"即将到来"的异常，不能精确定位时间点。
- 与You et al.(2024)的区别：本文更系统地定义和解决AP任务。
- 启发：Prompt Pool思路可推广到其他需要合成少数类样本的场景。

## 评分
- 新颖性: 5.0/5 — 首个系统性AP框架
- 实验充分度: 4.5/5 — 多数据集多消融
- 写作质量: 4.5/5
- 价值: 5.0/5 — 新任务+实用解决方案

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] When Will It Fail?: Anomaly to Prompt for Forecasting Future Anomalies in Time Series](when_will_it_fail_anomaly_to_prompt_for_forecasting_future_anomalies_in_time_ser.md)
- [\[ICML 2025\] LightGTS: A Lightweight General Time Series Forecasting Model](lightgts_a_lightweight_general_time_series_forecasting_model.md)
- [\[ICML 2025\] Winner-takes-all for Multivariate Probabilistic Time Series Forecasting](winner-takes-all_for_multivariate_probabilistic_time_series_forecasting.md)
- [\[ICML 2025\] KAN-AD: Time Series Anomaly Detection with Kolmogorov-Arnold Networks](kan-ad_time_series_anomaly_detection_with_kolmogorov-arnold_networks.md)
- [\[ICML 2025\] Causality-Aware Contrastive Learning for Robust Multivariate Time-Series Anomaly Detection](causality-aware_contrastive_learning_for_robust_multivariate_time-series_anomaly.md)

</div>

<!-- RELATED:END -->
