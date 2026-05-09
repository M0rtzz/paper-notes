---
title: >-
  [论文解读] Enhancing SAM with Efficient Prompting and Preference Optimization for Semi-supervised Medical Image Segmentation
description: >-
  [CVPR 2025][LLM对齐][SAM] 本文提出一种增强 SAM 的半监督医学图像分割框架，通过 BiomedCLIP、VQA 和 GPT-4 生成无监督提示替代专家标注，并引入 DPO 启发的偏好对齐策略在无标注数据上进一步优化模型，在低标注场景下显著超越 SOTA。
tags:
  - CVPR 2025
  - LLM对齐
  - SAM
  - 直接偏好优化
  - 半监督分割
  - 视觉语言提示
  - 医学影像
---

# Enhancing SAM with Efficient Prompting and Preference Optimization for Semi-supervised Medical Image Segmentation

**会议**: CVPR 2025  
**arXiv**: [2503.04639](https://arxiv.org/abs/2503.04639)  
**代码**: 无  
**领域**: LLM对齐  
**关键词**: SAM, 直接偏好优化, 半监督分割, 视觉语言提示, 医学影像

## 一句话总结

本文提出一种增强 SAM 的半监督医学图像分割框架，通过 BiomedCLIP、VQA 和 GPT-4 生成无监督提示替代专家标注，并引入 DPO 启发的偏好对齐策略在无标注数据上进一步优化模型，在低标注场景下显著超越 SOTA。

## 研究背景与动机

**领域现状**：SAM 等基础模型在医学影像分割中展现了强大的迁移能力，但仍依赖专家提供的几何提示（点、框），且需要大量标注数据进行微调。

**现有痛点**：(1) 现有的 SAM 变体（如 SAM-Med2D、Self-Prompt SAM）虽减少了推理时的专家干预，但训练仍需大量标注；(2) 主动学习和 human-in-the-loop 方法需要持续的人工参与和复杂的领域知识；(3) 基于奖励函数的 RLHF 方法需要单独训练奖励模型，无法端到端训练。

**核心矛盾**：医学影像标注成本极高，但基础模型的微调仍强依赖标注数据。现有的无监督提示方法缺乏充足的语义、位置和形状信息。

**本文目标**：(1) 设计无需专家干预的综合性无监督提示策略；(2) 在少量标注数据微调后，利用无标注数据通过偏好对齐继续提升性能。

**切入角度**：将 LLM 领域的 DPO 技术迁移到分割任务，通过虚拟标注者的简单评分/排名来模拟人类反馈，避免显式奖励建模。

**核心 idea**：用 BiomedCLIP + VQA + GPT-4 生成融合语义、位置和通用信息的无监督提示，再通过 DPO 启发的损失函数在无标注数据上对齐分割质量偏好。

## 方法详解

### 整体框架

输入图像同时送入 SAM-Med2D 编码器、BiomedCLIP 和 MedVInT（VQA）。BiomedCLIP 生成显著性图并提取边界框作为视觉提示，MedVInT 和 GPT-4 生成文本提示描述目标区域的形状和位置。所有提示经 prompt encoder 编码后与图像特征一起送入 mask decoder 生成分割图。

训练分两阶段：第一阶段用 10% 标注数据微调提示模块；第二阶段在剩余无标注数据上通过 DPO 偏好对齐策略继续训练 decoder。

### 关键设计

1. **无监督多模态提示生成**:

    - 功能：替代专家提供的几何提示，为 SAM 提供丰富的语义和空间信息
    - 核心思路：BiomedCLIP 对图像-文本对（如"chest x-ray"）生成 gScoreCAM 显著性图，经 CRF 后处理得到粗分割掩码，提取边界框作为视觉提示；MedVInT 回答关于器官/病灶形状和位置的问题，GPT-4 提供疾病/器官的通用描述，两者拼接作为文本提示
    - 设计动机：单一信息源不足以引导高质量分割，融合语义（CLIP）、位置形状（VQA）和通用知识（GPT-4）可提供更强的监督信号

2. **DPO 启发的偏好对齐模块**:

    - 功能：在无标注数据上利用虚拟偏好反馈继续优化分割模型
    - 核心思路：对每张图像通过不同阈值（0.3、0.4、0.5、0.6）从输出概率图生成 4 个分割候选，根据与 GT 的 IoU 分为四档评分（<0.4, 0.4-0.55, 0.55-0.7, >0.7）。将标准 DPO 损失扩展为多候选版本：$\mathcal{L} = -\log\sigma(\beta_1 \log\frac{\pi_\psi(Y_1|I)}{\pi_{fine}(Y_1|I)} + \beta_2 \log\frac{\pi_\psi(Y_2|I)}{\pi_{fine}(Y_2|I)} - \beta_2 \log\frac{\pi_\psi(Y_3|I)}{\pi_{fine}(Y_3|I)} - \beta_1 \log\frac{\pi_\psi(Y_4|I)}{\pi_{fine}(Y_4|I)})$，其中 $\beta_1=1, \beta_2=0.5$
    - 设计动机：避免训练单独的奖励模型，直接用偏好排序优化策略；4 个候选的分级权重设计让模型同时学会"什么是好的分割"和"什么是差的分割"

3. **半监督训练策略**:

    - 功能：最大化利用少量标注数据和大量无标注数据
    - 核心思路：第一阶段用 10% 标注数据、focal loss + Dice loss（20:1权重）微调全部组件 15 epoch；第二阶段用 DPO 损失在无标注数据上训练 30 epoch，学习率 1e-4 每 10 epoch 减半
    - 设计动机：GT 不直接参与第二阶段训练，仅被动用于生成偏好评分，使得该阶段本质上是半监督的

### 损失函数 / 训练策略

第一阶段使用 focal loss + Dice loss 加权组合（20:1）进行有监督微调。第二阶段使用扩展的 DPO 损失函数，对 4 个候选分别加权奖励或惩罚，$\beta_1=1$ 用于最好和最差候选，$\beta_2=0.5$ 用于中间候选。

## 实验关键数据

### 主实验

| 数据集 | 指标 | 本文(10%+10%无标注) | SAM-Med2D(20%) | nnU-Net(20%) | 提升(vs SAM-Med2D) |
|--------|------|-----|----------|------|------|
| Chest X-ray | Dice | 78.87 | 67.81 | 60.97 | +11.06 |
| Breast USD | Dice | 75.88 | - | - | - |
| AMOS-CT | mDice | 77.69 | 66.57 | 65.21 | +11.12 |

50%数据设置下本文达到 Dice 89.68（X-ray）、88.15（Breast）、84.30（AMOS-CT），接近全监督版本。

### 消融实验

| 配置 | Chest X-ray Dice | 说明 |
|------|---------|------|
| Full model (10%+10%) | 78.87 | 完整模型 |
| w/o Alignment | 75.60 | 去掉DPO对齐，掉3.27% |
| w/o Alignment - VQA | 73.35 | 再去掉VQA |
| w/o Alignment - VQA - GPT4 | 72.76 | 仅CLIP提示 |
| Only GPT4 text | 57.02 | 仅文本，无视觉提示 |

| 偏好策略 | AMOS-CT mDice | 说明 |
|---------|--------------|------|
| Ranking | 77.69 | 候选排名（最优） |
| Rating | 77.23 | 候选评分 |
| Best candidate only | 75.01 | 仅最佳候选反传 |

### 关键发现

- BiomedCLIP 视觉提示贡献最大（+15.74 Dice），VQA 和 GPT-4 各贡献约 0.6-1%
- DPO 偏好对齐在 10% 无标注数据上提升 3.27%，随着无标注数据增加收益更大
- Ranking 策略略优于 Rating，两者都显著优于仅用最佳候选的策略
- 在低数据场景（10-20%）优势最为明显，50% 数据时接近全监督性能

## 亮点与洞察

- **DPO 到视觉任务的成功迁移**：将 NLP 中的 DPO 技术适配到像素级分割任务，通过多候选阈值采样模拟偏好数据，设计巧妙且实现简洁
- **三源融合的无监督提示**：综合 CLIP 语义、VQA 定位和 LLM 先验，是目前最全面的无监督医学分割提示策略
- **虚拟标注者设计**：用 IoU 分档模拟人类评分，既利用了 GT 信息又不直接用于监督，是半监督的合理折中

## 局限与展望

- GT 仍间接用于生成偏好评分，完全无 GT 场景下需要其他质量评估方式
- 仅在 2D 分割上验证，3D 体积分割的扩展有待探索
- BiomedCLIP 显著性图质量直接影响提示质量，对某些复杂病灶可能不够精准
- 可考虑结合主动学习策略，用偏好对齐筛选出最有价值的样本进行标注

## 相关工作与启发

- **vs MedCLIP-SAM**: 仅用 CLIP 生成无监督提示作为伪标签，缺乏位置/形状信息；本文增加 VQA 和 GPT-4 补充多维度信息
- **vs Self-Prompt SAM**: 推理时自提示但训练仍需全监督；本文训练阶段也大幅降低标注需求
- **vs RLHF-based methods**: 需训练单独的奖励模型；本文用 DPO 直接优化，更简洁高效

## 评分

- 新颖性: ⭐⭐⭐⭐ DPO 迁移到分割有新意，但多模态提示融合的创新性有限
- 实验充分度: ⭐⭐⭐⭐ 三个数据集三种模态，消融充分
- 写作质量: ⭐⭐⭐⭐ 结构清晰，动机推导合理
- 价值: ⭐⭐⭐⭐ 对低标注医学分割有实际价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2025\] Do We Really Need Curated Malicious Data for Safety Alignment in Multi-Modal LLMs?](do_we_really_need_curated_malicious_data_for_safety_alignment_in_multi-modal_lar.md)
- [\[CVPR 2025\] Boost Your Human Image Generation Model via Direct Preference Optimization](boost_your_human_image_generation_model_via_direct_preference_optimization.md)
- [\[CVPR 2025\] InPO: Inversion Preference Optimization with Reparametrized DDIM for Efficient Diffusion Model Alignment](inpo_inversion_preference_optimization_with_reparametrized_ddim_for_efficient_di.md)
- [\[CVPR 2025\] PhysMoDPO: Physically-Plausible Humanoid Motion with Preference Optimization](physmodpo_physically-plausible_humanoid_motion_with_preference_optimization.md)
- [\[CVPR 2025\] Calibrated Multi-Preference Optimization for Aligning Diffusion Models](capo_multi_preference.md)

</div>

<!-- RELATED:END -->
