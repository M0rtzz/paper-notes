---
title: >-
  [论文解读] SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation
description: >-
  [ICLR 2026][3D视觉][结构化3D场景] 提出SceneTransporter——用最优传输(OT)引导组合latent扩散实现单图结构化3D场景生成：通过去偏聚类探查揭示部件级生成器在open-world场景中失败的原因(缺乏分配约束)→将结构化生成重新建模为全局关联分配问题→在去噪循环中求解熵OT目标→(1)OT计划门控交叉注意力实现排他性一对一路由(防止特征纠缠) (2)竞争性传输鼓励相似patch分组+边缘正则化确保清晰边界→显著提升实例级一致性和几何保真度。
tags:
  - ICLR 2026
  - 3D视觉
  - 结构化3D场景
  - 最优传输
  - 组合扩散
  - 实例分离
  - 交叉注意力门控
---

# SceneTransporter: Optimal Transport-Guided Compositional Latent Diffusion for Single-Image Structured 3D Scene Generation

**会议**: ICLR 2026  
**arXiv**: [2602.22785](https://arxiv.org/abs/2602.22785)  
**代码**: [项目页面](https://2019epwl.github.io/SceneTransporter/)  
**领域**: 3D视觉/结构化场景生成  
**关键词**: 结构化3D场景, 最优传输, 组合扩散, 实例分离, 交叉注意力门控

## 一句话总结

提出SceneTransporter——用最优传输(OT)引导组合latent扩散实现单图结构化3D场景生成：通过去偏聚类探查揭示部件级生成器在open-world场景中失败的原因(缺乏分配约束)→将结构化生成重新建模为全局关联分配问题→在去噪循环中求解熵OT目标→(1)OT计划门控交叉注意力实现排他性一对一路由(防止特征纠缠) (2)竞争性传输鼓励相似patch分组+边缘正则化确保清晰边界→显著提升实例级一致性和几何保真度。

## 研究背景与动机

**领域现状**：3D场景生成→多数方法产出无结构的整体mesh→下游任务(材质/物理/编辑)需要实例级分离。"分而治之"(分割→各自生成→拼装)→脆弱/遮挡处理差。端到端组合生成(部件级latent token)→对象级有效但open-world场景失败。

**现有痛点**：
   - (1) **结构性错分(Structural Mispartition)**：语义实例无法形成不相交的部分
   - (2) **几何冗余(Geometric Redundancy)**：多个latent竞争描述同一区域
   - (3) 缺乏全局分配约束→图像patch到部件token的映射混乱

**切入角度**：去偏聚类探查→诊断问题; 最优传输→提供全局最优的patch-token分配。

## 方法详解

### 诊断：去偏聚类探查

- 用CCA分析组合DiT的交叉注意力→发现patch到token的分配缺乏结构
- 根本原因：无约束的软注意力→多个patch映射到同一token/同一patch映射到多个token

### OT引导关联分配

**在去噪循环的每步：**

1. **定义OT问题**：
   - 源分布：L个图像patch特征
   - 目标分布：N×K个部件latent tokens
   - 代价矩阵：patch-token相似度
   - 求解熵OT→得到传输计划T*

2. **OT计划门控交叉注意力**：
   - 用T*门控原始交叉注意力→强制排他路由
   - 每个patch只贡献给一个部件token→防止纠缠

3. **边缘正则化分配代价**：
   - 在图像边缘处增加分配代价→阻止跨边缘分配
   - 促进相邻非边缘patch分配到同一token→形成连贯结构

## 实验关键数据

### Open-world 3D场景生成

| 方法 | 实例一致性 | 几何保真度 | 冗余 |
|------|----------|----------|------|
| MIDI(多实例注意力) | 中 | 中 | 严重 |
| PartGen(部件级) | 较好(物体) | 较好 | 中 |
| **SceneTransporter** | **最好** | **最好** | **极少** |

### 消融

| 组件 | 贡献 |
|------|------|
| 无OT(原始注意力) | 基线(严重错分) |
| +OT门控 | 大幅改善(排他路由) |
| +边缘正则化 | 进一步改善(清晰边界) |

### 关键发现

- OT门控→解决了结构性错分→最大贡献
- 边缘正则化→解决了跨物体的patch混合→边界清晰
- 传输计划的可视化→清晰显示patch分组→可解释

## 亮点与洞察

- **"分配问题"的精确诊断**：不是生成模型不够强→而是分配机制缺约束→去偏聚类探查精确定位问题。
- **OT的天然适切性**：OT本质是"最优分配"→patch到token的映射就是分配问题→数学上完美匹配。
- **在去噪循环内求解OT**：不是后处理→而是融入生成过程→生成时就保证结构正确。
- **从物体到场景的scale-up**：之前的组合生成仅对物体有效→SceneTransporter首次拓展到open-world场景。


## 局限性 / 可改进方向

- In this paper, we introduced SceneTransporter, a novel framework for structured 3D scene generation from a single image.

- By reframing the task as a global correlation assignment problem and solving it with an Optimal Transport layer, our method imposes powerful structural constraints directly on the generative process, effectively resolving the critical issues of structural
mispartition and geometric
redundancy found in existing models.

- Experimental results demonstrate that our method achieves state-of-the-art performance, generating complex open-world scenes with significantly improved geometric fidelity and instance-level coherence.

- Acknowledgments

This work is supported by the National Science and Technology Major Project of the Ministry of Science and Technology of China (No.

- 2025ZD1206301), the National Natural Science Foundation of China (No.


## 相关工作与启发

- **vs Radiance Fields**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs Gaussian Splatting**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ OT引导组合3D扩散的首次探索+分配问题的精确诊断
- 实验充分度: ⭐⭐⭐⭐ 开放世界场景+详细消融+可视化
- 写作质量: ⭐⭐⭐⭐⭐ 诊断→建模→解决的逻辑完美
- 价值: ⭐⭐⭐⭐⭐ 对结构化3D生成有根本性贡献
