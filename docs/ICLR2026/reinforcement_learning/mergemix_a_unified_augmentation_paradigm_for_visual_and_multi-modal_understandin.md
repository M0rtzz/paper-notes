---
title: >-
  [论文解读] MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding
description: >-
  [ICLR 2026][Mixup增强] 提出MergeMix统一训练范式，通过Token Merge生成注意力感知的混合图像作为偏好对中的"输者"，用混合比作为软偏好margin通过mixed SimPO损失优化，在SFT和RL之间找到效率-对齐性-稳定性的平衡点，在图像分类和MLLM基准上均达到SOTA。
tags:
  - ICLR 2026
  - Mixup增强
  - Token Merge
  - 偏好对齐
  - MLLM
  - SimPO
---

# MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding

**会议**: ICLR 2026  
**arXiv**: [2510.23479](https://arxiv.org/abs/2510.23479)  
**代码**: [GitHub](https://github.com/JinXins/MergeMix)  
**领域**: 多模态VLM/数据增强  
**关键词**: Mixup增强, Token Merge, 偏好对齐, MLLM, SimPO

## 一句话总结
提出MergeMix统一训练范式，通过Token Merge生成注意力感知的混合图像作为偏好对中的"输者"，用混合比作为软偏好margin通过mixed SimPO损失优化，在SFT和RL之间找到效率-对齐性-稳定性的平衡点，在图像分类和MLLM基准上均达到SOTA。

## 研究背景与动机

**领域现状**：MLLM对齐分SFT（需标注+缺偏好建模）和RL（需奖励模型+不稳定）两条路线。偏好优化(DPO等)通过构建偏好对桥接两者，但如何高质量构建偏好对是核心问题。

**现有痛点**：(1) SeVa用随机增强(RandomCrop)构建"输者"→增强质量不可控→"输者"可能太差或太好；(2) DPO的margin是固定的→无法与数据质量关联；(3) 现有Mixup方法要么基于显著性（慢）要么随机（效果不稳）。

**切入角度**：Token Merge天然产出注意力聚类信息→用作Mixup的掩码→混合比与合并比关联→混合图像质量可控→混合比自然作为偏好margin。

## 方法详解

### 两个场景

1. **MergeMix用于图像分类**：ToMe编码器→注意力恢复→TopK掩码→混合图像+重缩放标签→分类训练

2. **MergeMix用于MLLM对齐**：
   - 构建偏好对：原始图像=Winner，MergeMix混合图像=Loser
   - 软偏好margin：混合比 $\lambda$ 作为margin（混合越多→Loser越差→margin越大）
   - Mixed SimPO损失：$\mathcal{L} = -\log\sigma(\pi_\theta(y^+|x) - \pi_\theta(y^-|\hat{x}) - \hat{\lambda} \cdot \gamma)$

### 关键设计
- Bipartite Soft Matching做token合并→全局最优配对→比贪心TopK保持更多空间关系
- 注意力恢复函数将合并后的注意力图恢复到原始分辨率→保留上下文连续性
- 混合比λ自然与Mixup信息量关联→无需额外奖励模型

## 实验关键数据

### 图像分类 (DeiT-Small)
| 方法 | CIFAR-100 | ImageNet | 训练时间 |
|------|----------|---------|---------|
| CutMix | 基线 | 基线 | 基线 |
| AutoMix | 好 | 好 | 慢 |
| **MergeMix** | **最优** | **最优** | **高效** |

### MLLM基准 (LLaVA-7B)
| 方法 | VQA | MMBench | POPE | 说明 |
|------|-----|---------|------|------|
| SFT基线 | 基线 | 基线 | 基线 | 无偏好 |
| SeVa(DPO) | + | + | + | 随机增强 |
| **MergeMix** | **++** | **++** | **++** | 可控增强+软margin |

### 关键发现
- MergeMix在图像分类和MLLM对齐上都优于现有方法→统一范式有效
- 软偏好margin比固定margin更稳定→数据依赖的margin让优化更自适应
- MergeMix的MLLM校准性更好→来自混合比与优化目标的直接关联

## 亮点与洞察
- **SFT和RL的桥接**：不需要奖励模型（RL的代价），也不只是拟合参考答案（SFT的局限）→用数据增强构建偏好对，用混合比控制偏好强度。
- **Token Merge的创造性复用**：本来是加速推理的技术→被用作注意力感知的图像混合掩码生成器。
- **混合比=偏好强度**的优雅关联：混合程度直接对应信息损失程度→自然指示"输者"有多差。

## 局限性 / 可改进方向
- ToMe编码器需要额外前向传播→虽比AutoMix快但不是零成本
- 仅在LLaVA上验证→更强基座模型(Qwen-VL等)效果未知
- 混合只在图像模态做→文本侧的增强未考虑

## 评分
- 新颖性: ⭐⭐⭐⭐ Token Merge+Mixup+偏好对齐的三位一体设计新颖
- 实验充分度: ⭐⭐⭐⭐ 图像分类+MLLM双场景验证
- 写作质量: ⭐⭐⭐⭐ 分类和MLLM两条线清晰
- 价值: ⭐⭐⭐⭐ 为MLLM偏好对齐提供了高效低成本方案
