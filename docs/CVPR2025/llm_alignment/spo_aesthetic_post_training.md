---
title: >-
  [论文解读] Aesthetic Post-Training Diffusion Models from Generic Preferences with Step-by-step Preference Optimization
description: >-
  [CVPR 2025][LLM对齐][偏好优化] 本文提出逐步偏好优化（SPO），通过在每个去噪步骤独立地从共享噪声中采样候选池并用步感知偏好模型选出胜负对，使扩散模型聚焦于细粒度的美学细节而非布局差异，在使用通用偏好数据的情况下显著提升了生成图像的美学质量。
tags:
  - CVPR 2025
  - LLM对齐
  - 偏好优化
  - 扩散模型
  - 图像美学
  - DPO
  - 后训练
---

# Aesthetic Post-Training Diffusion Models from Generic Preferences with Step-by-step Preference Optimization

**会议**: CVPR 2025  
**arXiv**: [2406.04314](https://arxiv.org/abs/2406.04314)  
**代码**: https://github.com/RockeyCoss/SPO  
**领域**: 扩散模型  
**关键词**: 偏好优化, 扩散模型, 图像美学, DPO, 后训练

## 一句话总结
本文提出逐步偏好优化（SPO），通过在每个去噪步骤独立地从共享噪声中采样候选池并用步感知偏好模型选出胜负对，使扩散模型聚焦于细粒度的美学细节而非布局差异，在使用通用偏好数据的情况下显著提升了生成图像的美学质量。

## 研究背景与动机
1. **领域现状**：文本到图像扩散模型已广泛使用DPO进行后训练对齐，以提升生成图像的整体质量（包括提示对齐和美学）。
2. **现有痛点**：现有DPO方法将偏好标签从最终干净图像直接传播到整个生成轨迹的所有中间步骤，这种策略存在两个核心问题——通用偏好标签混合了布局和美学意见，且两条轨迹间的中间样本差异巨大难以聚焦细节。
3. **核心矛盾**：通用偏好数据中的"好"图像往往是因为布局正确而被偏好，但其局部细节（如纹理、色彩）可能反而不如"差"图像，导致美学偏好与通用偏好发生冲突。收集专门的美学偏好数据成本极高。
4. **本文目标**：在不额外标注美学偏好数据的前提下，设计一种能聚焦于图像细粒度美学细节的偏好优化方法。
5. **切入角度**：作者观察到在同一噪声潜变量出发、仅经过一两步去噪后，不同候选样本之间的差异很小且主要集中在细节层面——这些细微差异恰恰反映了美学质量的差别。
6. **核心idea**：抛弃两条轨迹的偏好传播范式，改为在每个去噪步骤独立采样候选池，用步感知偏好模型在线评估并选出胜负对，通过累积每一步的细微改善来显著提升整体美学质量。

## 方法详解

### 整体框架
输入为文本提示和高斯噪声 → 在每个去噪步骤 $t$，从共享噪声 $\boldsymbol{x}_t$ 出发采样 $k$ 个候选 $\{\boldsymbol{x}_{t-1}^1, ..., \boldsymbol{x}_{t-1}^k\}$ → 步感知偏好模型（SPM）对候选打分并选出最佳和最差作为胜负对 → 用修改后的DPO损失优化扩散模型 → 随机选择一个候选初始化下一步 → 重复直到完成所有步骤。

### 关键设计

1. **步感知偏好模型（Step-aware Preference Model, SPM）**:

    - 功能：对中间噪声状态下的候选样本进行质量评估，输出质量分数。
    - 核心思路：基于CLIP构建，以PickScore初始化后在Pick-a-Pic V1数据集上微调。关键改进是引入时间步条件——通过时间条件自适应LayerNorm修改CLIP视觉编码器，并利用DDIM直接从噪声样本预测 $\hat{\boldsymbol{x}}_0$ 以减少与训练数据的域差距。打分公式为 $\hat{p}_w = \frac{\exp(\tau \cdot f_{\text{CLIP-V}}(\boldsymbol{x}_t^w, t) \cdot f_{\text{CLIP-T}}(c))}{\sum \exp(...)}$。
    - 设计动机：现有偏好模型只能评估干净图像，无法处理中间噪声状态。SPM解决了这个问题，使得在任意时间步都能进行质量比较。

2. **随机初始化策略（Random Selection）**:

    - 功能：从候选池中随机选择一个样本初始化下一步去噪。
    - 核心思路：不选最佳而随机选择，确保每个胜负对都来自同一噪声潜变量，因此差异仅在细粒度细节。当时间步 $t > \kappa$ 时（噪声过大），使用标准采样流程，仅在 $t \leq \kappa$ 时启用候选池采样。
    - 设计动机：如果总选最佳，会导致轨迹偏移，破坏训练稳定性；随机选择保持了探索多样性。

3. **多步偏好优化（Multi-step SPO, MSPO）**:

    - 功能：为SDXL等强模型扩展SPO，增大候选间差异以产生更清晰的偏好信号。
    - 核心思路：对每个候选不只做一步去噪，而是执行多步（$j$ 步）后再用SPM评估，从而放大候选间的差异，避免差异过小导致的模糊偏好信号。
    - 设计动机：SDXL模型能力更强，单步去噪产生的差异太小，SPM难以可靠区分，多步扩展解决了这一问题。

### 损失函数 / 训练策略
SPO的目标函数与标准DPO类似，但关键区别在于胜负对是在线从同一 $\boldsymbol{x}_t$ 采样得到的：
$$\mathcal{L}(\theta) = -\mathbb{E}_{t, c, \boldsymbol{x}_T}\left[\log\sigma\left(\beta\log\frac{p_\theta(\boldsymbol{x}_{t-1}^w|c,t,\boldsymbol{x}_t)}{p_{\text{ref}}(\boldsymbol{x}_{t-1}^w|c,t,\boldsymbol{x}_t)} - \beta\log\frac{p_\theta(\boldsymbol{x}_{t-1}^l|c,t,\boldsymbol{x}_t)}{p_{\text{ref}}(\boldsymbol{x}_{t-1}^l|c,t,\boldsymbol{x}_t)}\right)\right]$$
训练使用Pick-a-Pic V1的4k文本提示（不使用图像），候选池大小为 $k$ 个样本。使用4×A100 GPU，SD-1.5微调12h、SDXL微调29.5h，SPM训练分别8h和29h。

## 实验关键数据

### 主实验

| 模型 | PickScore | HPSV2 | ImageReward | Aesthetic |
|------|-----------|-------|-------------|-----------|
| SDXL (Vanilla) | 21.95 | 26.95 | 0.5380 | 5.950 |
| Diffusion-DPO-SDXL | 22.64 | 29.31 | 0.9436 | 6.015 |
| MAPO-SDXL | 22.11 | 28.22 | 0.7165 | 6.096 |
| **SPO-SDXL** | **23.06** | **31.80** | **1.0803** | **6.364** |

### 消融实验

| 配置 | PickScore | Aesthetic | 说明 |
|------|-----------|-----------|------|
| Full SPO | 23.06 | 6.364 | 完整模型 |
| w/o SPM (用PickScore) | 22.71 | 6.152 | SPM贡献显著 |
| 选最佳初始化 (非随机) | 22.84 | 6.210 | 随机选择更优 |
| 单步 (无MSPO) | 22.65 | 6.098 | MSPO对SDXL重要 |

### 关键发现
- SPO收敛速度远快于Diffusion-DPO，因为逐步设计提供了更准确的偏好信号。总训练GPU小时仅为DPO的4.9%（SDXL：29.5h vs 4800h）。
- SPO在不牺牲图像-文本对齐（GenEval提升+1.77%）的前提下显著提升了美学分数。
- 人类评估中SPO-SDXL以约72%的胜率优于SDXL原版，以约63%胜率优于Diffusion-DPO-SDXL。
- SPO是隐式的美学优化器——通过SPM从通用数据中蒸馏出美学偏好。
- 时间步范围分析：[0-750]最优，[0-250]和[250-500]都很重要（[250-500]是细节精修的关键区间），而[750-1000]噪声过大无助益。
- 候选池大小$k=4$最优——$k$过大时最差样本质量低于平均，"push away"效果减弱。MSPO内步数$j=4$最优，$j\to\infty$退化为Diffusion-DPO。

## 亮点与洞察
- **逐步偏好优化的思想非常巧妙**：通过确保胜负对来自同一噪声潜变量，自动过滤掉布局差异，只留下细节差异——这是一种优雅的"免费"美学偏好数据构造方式。
- **随机初始化的反直觉设计**：不选最佳而是随机选择，既保持了训练稳定性又维持了足够的探索性。选最佳或最差都会导致训练偏向特定轨迹，损害泛化。
- **可迁移思路**：这种"在中间状态比较细粒度差异"的思路可以迁移到其他需要细粒度控制的生成任务，如视频生成的帧级质量优化。
- **泛化到文本生成**：SPO-SDXL的LoRA权重可直接嫁接到Glyph-ByT5-SDXL，在保持文本生成能力的同时提升图像美学（纹理更丰富、色彩更鲜艳）。

## 局限与展望
- SPO不适用于Flow Matching模型（如SD3、Flux），因为SPO要求中间步骤的随机性，而Flow Matching是确定性的。
- SPO专注于美学提升，对图像-文本对齐改善有限（GenEval仅+1.77%，低于Diffusion-DPO）。
- 只使用了众包数据，未涉及主观、文化、政治等美学维度。
- 未来可探索将SPO扩展到Flow Matching框架，或结合更细粒度的美学维度控制。
- 候选池采样的计算开销随候选数 $k$ 线性增长，大 $k$ 值会显著增加训练时间。
- SPM模型的训练依赖Pick-a-Pic数据集的偏好分布，可能在特定风格或领域的图像上表现不佳。
- SPM中引入时间步条件自适应LayerNorm修改CLIP视觉编码器，并利用DDIM直接从噪声样本预测$\hat{\boldsymbol{x}}_0$以减少与训练数据的域差距。
- 当$\kappa=750$时效果最佳，即仅在时间步[0-750]范围内使用SPO，跳过噪声最大的[750-1000]阶段。

## 相关工作与启发
- **vs Diffusion-DPO**: DPO将最终图像偏好直接传播到所有中间步，布局差异主导训练信号；SPO在每一步独立评估，聚焦细节。
- **vs D3PO**: D3PO虽然在线生成对但仍采用轨迹级别偏好传播，无法聚焦细粒度差异。
- **vs DDPO/ReFL**: 这些方法使用奖励模型梯度但仍是轨迹级别优化，SPO的逐步设计更精细。

## 评分

### 实现细节
SD-1.5和SDXL双平台验证。4×A100 GPU。候选池$k=4$，MSPO内步数$j=4$。
SPM基于PickScore初始化，在Pick-a-Pic V1上微调，引入时间步条件自适应LayerNorm。
- 新颖性: ⭐⭐⭐⭐ 逐步偏好优化思路新颖，但核心仍是DPO变体
- 实验充分度: ⭐⭐⭐⭐⭐ SD-1.5和SDXL双平台验证，多指标+人类评估，消融全面
- 写作质量: ⭐⭐⭐⭐⭐ 问题动机清晰，图示直观，逻辑链完整
- 价值: ⭐⭐⭐⭐ 对扩散模型美学提升有实用价值，但不适用于最新的Flow Matching模型

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2025\] Curriculum Direct Preference Optimization for Diffusion and Consistency Models](curriculum_direct_preference_optimization_for_diffusion_and_consistency_models.md)
- [\[CVPR 2025\] InPO: Inversion Preference Optimization with Reparametrized DDIM for Efficient Diffusion Model Alignment](inpo_inversion_preference_optimization_diffusion_alignment.md)
- [\[CVPR 2025\] Calibrated Multi-Preference Optimization for Aligning Diffusion Models](capo_multi_preference.md)
- [\[NeurIPS 2025\] Diffusion Model as a Noise-Aware Latent Reward Model for Step-Level Preference Optimization](../../NeurIPS2025/llm_alignment/diffusion_model_as_a_noiseaware_latent_reward_model_for_step.md)
- [\[NeurIPS 2025\] Rethinking Direct Preference Optimization in Diffusion Models](../../NeurIPS2025/llm_alignment/rethinking_direct_preference_optimization_in_diffusion_models.md)

<!-- RELATED:END -->
