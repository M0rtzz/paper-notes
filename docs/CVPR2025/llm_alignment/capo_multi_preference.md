---
title: >-
  [论文解读] Calibrated Multi-Preference Optimization for Aligning Diffusion Models
description: >-
  [CVPR 2025][LLM对齐][偏好优化] 本文提出CaPO（校准偏好优化），通过奖励校准（近似期望胜率）和基于Pareto前沿的样本对选择策略，在无需人类标注数据的情况下有效整合多个奖励模型信号来对齐文本到图像扩散模型，在GenEval和T2I-Compbench上持续超越DPO等方法。
tags:
  - CVPR 2025
  - LLM对齐
  - 偏好优化
  - 扩散模型
  - 奖励校准
  - 多目标优化
  - Pareto前沿
---

# Calibrated Multi-Preference Optimization for Aligning Diffusion Models

**会议**: CVPR 2025  
**arXiv**: [2502.02588](https://arxiv.org/abs/2502.02588)  
**代码**: [https://kyungmnlee.github.io/capo.github.io/](https://kyungmnlee.github.io/capo.github.io/)  
**领域**: 扩散模型  
**关键词**: 偏好优化, 扩散模型, 奖励校准, 多目标优化, Pareto前沿

## 一句话总结
本文提出CaPO（校准偏好优化），通过奖励校准（近似期望胜率）和基于Pareto前沿的样本对选择策略，在无需人类标注数据的情况下有效整合多个奖励模型信号来对齐文本到图像扩散模型，在GenEval和T2I-Compbench上持续超越DPO等方法。

## 研究背景与动机
1. **领域现状**：T2I扩散模型的后训练对齐方法（如Diffusion-DPO）已取得成功，但依赖昂贵的人类标注偏好数据集。使用奖励模型替代人类偏好是一个可行方向。
2. **现有痛点**：现有偏好优化方法仅考虑简单的成对偏好分布，无法充分利用奖励信号中的丰富信息；多奖励场景下不同奖励间的不一致性（如美学vs文本对齐）难以处理。
3. **核心矛盾**：直接优化奖励值容易导致奖励过拟合（reward hacking）；多个奖励模型的评分范围和分布不同，简单加权和无法达到Pareto最优。
4. **本文目标**：设计一种能从多个奖励模型获取校准信号、避免奖励过优化、实现Pareto最优的扩散模型对齐方法。
5. **切入角度**：将奖励值转换为"期望胜率"——一种归一化的、跨奖励一致的度量；使用非支配排序选择Pareto前沿样本对。
6. **核心idea**：奖励校准（期望胜率近似）+ Pareto前沿选择 + 回归损失匹配校准奖励差值。

## 方法详解

### 整体框架
预训练扩散模型 + 提示集 → 生成N个图像/提示 → 多个奖励模型打分 → 成对比较计算校准奖励（近似胜率）→ 单奖励：best-of-N/worst-of-N选择对；多奖励：非支配排序选择Pareto前沿 → CaPO回归损失训练。

### 关键设计

1. **奖励校准（Calibrated Rewards）**:

    - 功能：将原始奖励值转换为归一化的期望胜率，消除不同奖励模型间的量纲不一致。
    - 核心思路：对每个样本 $i$，计算其与所有其他 $N-1$ 个样本的成对胜率平均值：$R_{\text{ca}}(\mathbf{x}_i, \mathbf{c}) = \frac{1}{N-1}\sum_{j \neq i}\sigma(R(\mathbf{x}_i, \mathbf{c}) - R(\mathbf{x}_j, \mathbf{c}))$。当 $N$ 足够大时，这近似于样本对预训练模型的期望胜率 $\mathbb{P}(\mathbf{x} \succ p_{\text{ref}}|\mathbf{c})$。
    - 设计动机：Bradley-Terry模型的原始奖励值不直接衡量样本质量好坏，且不同奖励模型的值域不同。胜率提供了统一的[0,1]范围度量。

2. **CaPO损失函数**:

    - 功能：使用回归损失匹配扩散模型隐式奖励差与校准奖励差。
    - 核心思路：$\mathcal{L}_{\text{CaPO}} = \mathbb{E}_{t,\epsilon}[(R_{\text{ca}}(\mathbf{x}^+) - R_{\text{ca}}(\mathbf{x}^-) - \beta(R_\theta(\mathbf{x}_t^+) - R_\theta(\mathbf{x}_t^-)))^2]$。这是IPO的推广——IPO固定 $\Delta R = 1$，CaPO使用动态目标值，使模型按实际偏好差异调整学习幅度。
    - 设计动机：DPO的sigmoid损失只关心偏好方向（谁更好），CaPO的回归损失还关心偏好程度（好多少），减少过优化风险。

3. **基于Pareto前沿的样本对选择（Frontier-based Rejection Sampling）**:

    - 功能：在多奖励场景下选择能推动模型向Pareto最优方向发展的训练样本对。
    - 核心思路：使用非支配排序算法找到上层和下层Pareto前沿。正样本从上层Pareto集合采样（在所有奖励维度都不被其他样本支配），负样本从下层集合采样。多个校准奖励取平均作为优化目标。
    - 设计动机：简单加权和无法处理奖励间的冲突（如美学↑但对齐↓），Pareto选择自然平衡多个目标。

### 损失函数 / 训练策略
使用CaPO回归损失（Eq.8）。提出单调损失加权 $w_t = \sigma(-\lambda_t + b)$，对高噪声步给予更大权重（最优$b=1.5$）。适用于SDXL和SD3-Medium。无需人类标注数据，训练数据完全由预训练模型生成。使用DiffusionDB 100K提示，每提示生成N=16图像，DDIM采样器50步（SDXL guidance=7.5，SD3-M flow DPM-solver guidance=5.0）。

## 实验关键数据

### 主实验（单奖励）

| 方法 | MPS Win% | VQA Win% | VILA Win% |
|------|---------|---------|----------|
| DPO (SDXL) | 58.5 | 49.3 | 61.7 |
| IPO (SDXL) | 56.8 | 50.1 | 64.1 |
| **CaPO (SDXL)** | **61.1** | **49.7** | **64.9** |

### 主实验（多奖励）

| 方法 | MPS Score | VQA Score | VILA Score |
|------|-----------|-----------|------------|
| SDXL Baseline | 11.30 | 0.826 | 5.953 |
| DPO (SUM) | 11.48 | 0.829 | 6.193 |
| **CaPO (FRS)** | **11.57** | **0.832** | **6.385** |

### 消融实验

| 配置 | MPS Win% | 说明 |
|------|---------|------|
| CaPO (full) | 61.1 | 完整方法 |
| w/o 校准 (原始奖励) | 57.2 | 校准贡献+3.9% |
| CaPO + DPO损失 | 58.8 | 回归损失优于sigmoid |
| 加权和 (非Pareto) | 59.5 | Pareto选择更优 |

### 关键发现
- CaPO在单奖励和多奖励设置下都持续超越DPO和IPO。
- 奖励校准显著减少了奖励过优化问题，模型在各维度表现更均衡。
- Pareto前沿选择在多奖励场景下比加权和和模型汤（Rewarded Soups）都更有效。
- 回归损失比sigmoid/hinge损失更稳定，因为它考虑了偏好的程度信息。
- CaPO成功应用于SD3-Medium（flow matching模型），GenEval从0.68提升至0.71，证明了方法的通用性。
- 与Diffusion-DPO（人类标注Pick-a-Pic数据集训练）对比：CaPO在相同58K提示下严格更优（PickScore 22.83 vs 22.71, MPS 11.71 vs 11.59, VILA 6.141 vs 6.049）。
- 损失加权消融：sigmoid加权（b=1.5）显著优于常数加权，高噪声步给予更大权重有助于学习。

## 亮点与洞察
- **奖励校准思路优雅**：将奖励转化为期望胜率，不仅统一了量纲，还天然对齐了Bradley-Terry模型的偏好假设。
- **Pareto选择的创新应用**：将多目标优化中的Pareto最优概念引入偏好对选择，是一种自然且有效的解决方案。
- **可迁移到LLM对齐**：奖励校准和Pareto前沿选择的思路可直接迁移到LLM的多维度RLHF对齐。
- **SDXL和SD3-M双平台验证**：CaPO-SDXL GenEval从0.55提升至0.59，CaPO-SD3-M GenEval从0.68提升至0.71。使用DiffusionDB 100K提示，每提示生成N=16图像（N=16在计算成本与性能间最优）。

## 局限与展望
- 需要从预训练模型生成大量样本（N个/提示），计算成本不低。
- 校准质量依赖于N的大小，N太小时近似不准确。
- 仅在T2I任务上验证，未扩展到视频生成等任务。
- 奖励模型本身的偏差会通过校准过程传递到训练中，当奖励模型系统性地偏向某种风格时可能导致模式坍缩。
- Pareto前沿选择在奖励维度超过3个时计算复杂度快速增长，可扩展性有待验证。
- 回归损失的目标值依赖于校准奖励差的准确估计，在样本量不足时可能引入噪声。
- 使用三个互补奖励模型：MPS（通用人类偏好）、VQAscore（CLIP-FlanT5-XXL视觉问答评估图像-文本对齐）、VILA（基于AVA数据集的图像美学评估）。

## 相关工作与启发
- **vs Diffusion-DPO**: DPO需要人类标注数据且仅支持单奖励，CaPO免人类标注且支持多奖励。
- **vs SPO**: SPO逐步优化聚焦美学细节，CaPO从奖励校准角度全局优化。
- **vs Rewarded Soups**: Soups在模型权重空间插值，CaPO在训练阶段就实现多目标平衡。

## 评分
- 新颖性: ⭐⭐⭐⭐ 奖励校准+Pareto选择组合新颖
- 实验充分度: ⭐⭐⭐⭐⭐ 单/多奖励、SDXL/SD3双平台、多基准验证
- 写作质量: ⭐⭐⭐⭐ 理论推导清晰，方法描述系统
- 价值: ⭐⭐⭐⭐⭐ 解决了多奖励对齐的实际问题，方法通用且有效

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2025\] Curriculum Direct Preference Optimization for Diffusion and Consistency Models](curriculum_direct_preference_optimization_for_diffusion_and_consistency_models.md)
- [\[CVPR 2025\] Aesthetic Post-Training Diffusion Models from Generic Preferences with Step-by-step Preference Optimization](spo_aesthetic_post_training.md)
- [\[CVPR 2025\] InPO: Inversion Preference Optimization with Reparametrized DDIM for Efficient Diffusion Model Alignment](inpo_inversion_preference_optimization_diffusion_alignment.md)
- [\[ICML 2025\] ADHMR: Aligning Diffusion-based Human Mesh Recovery via Direct Preference Optimization](../../ICML2025/llm_alignment/adhmr_aligning_diffusion-based_human_mesh_recovery_via_direct_preference_optimiz.md)
- [\[NeurIPS 2025\] Rethinking Direct Preference Optimization in Diffusion Models](../../NeurIPS2025/llm_alignment/rethinking_direct_preference_optimization_in_diffusion_models.md)

</div>

<!-- RELATED:END -->
