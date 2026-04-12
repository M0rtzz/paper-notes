---
title: >-
  [论文解读] GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction
description: >-
  [ICML2025][自动驾驶][逆强化学习] 提出 GoIRL，首次将最大熵 IRL 框架与向量化场景表示结合的轨迹预测方法，通过 feature adaptor 将车道图特征聚合到网格空间实现 IRL 兼容，结合层级参数化轨迹生成器和 MCMC 概率融合，在 Argoverse 和 nuScenes 上达 SOTA。
tags:
  - ICML2025
  - 自动驾驶
  - 逆强化学习
  - 轨迹预测
  - 多模态
  - 最大熵IRL
  - 向量化表示
---

# GoIRL: Graph-Oriented Inverse Reinforcement Learning for Multimodal Trajectory Prediction

**会议**: ICML2025  
**arXiv**: [2506.21121](https://arxiv.org/abs/2506.21121)  
**代码**: 待确认  
**领域**: autonomous_driving  
**关键词**: 逆强化学习, 轨迹预测, 多模态, 最大熵IRL, 向量化表示

## 一句话总结

提出 GoIRL，首次将最大熵 IRL 框架与向量化场景表示结合的轨迹预测方法，通过 feature adaptor 将车道图特征聚合到网格空间实现 IRL 兼容，结合层级参数化轨迹生成器和 MCMC 概率融合，在 Argoverse 和 nuScenes 上达 SOTA。

## 研究背景与动机

- **行为克隆局限**：分布偏移（covariate shift）导致对 OOD 场景泛化差
- **模态坍塌**：监督学习用单一 GT 轨迹训练导致多模态捕获不足
- **IRL 优势**：奖励驱动范式＋最大熵原则天然处理不确定性和泛化
- **现有 IRL 瓶颈**：仅支持栅格化表示→信息损失→性能落后于向量化监督模型

## 方法详解

### 两阶段架构

1. **策略推断**：向量化编码→Feature Adaptor→网格化→MaxEnt IRL→策略
2. **轨迹生成**：MCMC采样多模态路径→层级生成→Bézier曲线参数化→精细化

### Feature Adaptor

- 将图卷积提取的车道图特征按物理坐标分配到网格单元
- CNN 降采样减小状态空间维度→可行的 IRL 计算

### MaxEnt IRL

$$P(\hat{\tau}|\mathcal{C}) \propto \exp\left(\sum_{s \in \hat{\tau}} \mathcal{R}(s)\right)$$

通过近似值迭代获得 soft-optimal 策略

### 层级轨迹生成

- **粗粒度**：Bézier 曲线控制点递归预测
- **细粒度**：精细化模块利用完整轨迹检索局部上下文特征
- **概率融合**：MCMC 分布 + 分类概率的混合

## 实验关键数据

### Argoverse

| 方法 | minADE↓ | minFDE↓ | MR↓ |
|---|---|---|---|
| QCNet | 较好 | 较好 | 较好 |
| MTR | 较好 | 较好 | 较好 |
| **GoIRL** | **最优** | **最优** | **最优** |

### nuScenes

- 同样达到或超越 SOTA

### 泛化实验

- 可行驶区域变化场景：GoIRL 明显优于监督模型
- 验证了 IRL 的 reward-driven 泛化优势

### 消融

- Feature adaptor 移除→性能显著下降
- MCMC 概率融合→MR 改善
- 精细化模块→ADE/FDE 改善

## 亮点与洞察

1. **首次 MaxEnt IRL + 向量化表示**：Feature Adaptor 打破了 IRL 的栅格化限制
2. **泛化优势显著**：奖励驱动范式在 OOD 场景不依赖数据分布
3. **MCMC 概率融合**增强了模态置信度
4. 奖励分布作为可解释中间表示可服务下游规划

## 局限性 / 可改进方向

- IRL 内循环的计算开销仍较大（近似值迭代 $N$ 步）
- 网格分辨率受限，精细路径信息可能丢失
- 离散动作空间（9方向+停止）的粒度限制精度
- Feature Adaptor 的聚合方式（最近邻分配）可能对稀疏区域不够精确

## 相关工作与启发

- Ziebart et al. (2008) MaxEnt IRL：最大熵 IRL 理论基础
- Liang et al. (2020) LaneGCN：车道图卷积编码器
- Guo et al. (2022) PGP：栅格化 IRL 轨迹预测
- Deo & Trivedi (2020)：plans-to-trajectories 方法
- 启发：IRL 在预测领域有重新崛起的潜力，向量化表示是关键突破口

## 评分

⭐⭐⭐⭐ — 将 IRL 现代化的重要一步，Feature Adaptor 打通向量化表示与IRL的壁垒，泛化实验令人印象深刻


## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
