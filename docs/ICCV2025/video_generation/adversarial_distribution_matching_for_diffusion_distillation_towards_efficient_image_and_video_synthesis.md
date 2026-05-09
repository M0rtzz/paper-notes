---
title: >-
  [论文解读] Adversarial Distribution Matching for Diffusion Distillation Towards Efficient Image and Video Synthesis
description: >-
  [ICCV 2025][扩散模型] 提出对抗式分布匹配(ADM)框架，用基于扩散模型的判别器以隐式、数据驱动的方式对齐真假分数估计器的潜在预测，取代DMD中预定义的KL散度，结合对抗蒸馏预训练(ADP)形成DMDX管线，在SDXL一步生成上超越DMD2，并扩展到SD3和CogVideoX视频生成。
tags:
  - ICCV 2025
  - 扩散模型
  - adversarial training
  - distribution matching
  - 视频生成
  - score distillation
---

# Adversarial Distribution Matching for Diffusion Distillation Towards Efficient Image and Video Synthesis

**会议**: ICCV 2025  
**arXiv**: 无  
**代码**: 无  
**领域**: 图像/视频生成 / 扩散模型蒸馏  
**关键词**: diffusion distillation, adversarial training, distribution matching, one-step generation, score distillation

## 一句话总结

提出对抗式分布匹配(ADM)框架，用基于扩散模型的判别器以隐式、数据驱动的方式对齐真假分数估计器的潜在预测，取代DMD中预定义的KL散度，结合对抗蒸馏预训练(ADP)形成DMDX管线，在SDXL一步生成上超越DMD2，并扩展到SD3和CogVideoX视频生成。

## 研究背景与动机

分布匹配蒸馏(DMD)是将预训练扩散模型压缩为高效少步生成器的有力方法，但其依赖逆KL散度最小化存在模式坍塌(mode collapse)风险——零强制特性使模型聚焦于少数主导模式。DMD2通过GAN正则化器缓解但未从根本解决问题。作者提出核心问题：**能否绕过预定义散度的限制，开发一种学习隐式、数据驱动差异度量的框架？** 此外，一步蒸馏面临梯度爆炸/消失的更高风险，作者将其归因于学生-教师分布支撑集重叠不足（而非仅仅是假分数估计器的近似误差），因此需要更好的初始化。

## 方法详解

### 整体框架

DMDX统一管线包含两阶段：(1) 对抗蒸馏预训练(ADP)——用合成ODE对数据和混合判别器（潜在空间+像素空间）预训练生成器，提供良好初始化；(2) ADM微调——用基于扩散模型的判别器以对抗方式对齐真假分数估计器的PF-ODE预测，替代DMD损失实现分布匹配。

### 关键设计

1. **对抗式分布匹配(ADM)**: 判别器Dτ由冻结的教师扩散模型+多个可训练头组成。给定生成器输出x̂₀的加噪样本xₜ，不再像DMD那样让分数估计器求解到端点x₀，而是解PF-ODE到(t-Δt)，得到真/假样本x_{t-Δt}^{real/fake}作为分数预测送入判别器。使用Hinge损失交替训练生成器和判别器。关键创新是保留了时间步信息（与分数蒸馏一致），同时判别器能随训练过程自适应调整差异度量——早期关注全局差异，后期关注局部细粒度差异。

2. **对抗蒸馏预训练(ADP)**: 从教师模型离线收集ODE对，用线性插值构造加噪样本，预测目标改为ODE对的速度。使用混合判别器——潜在空间判别器（教师模型初始化）和像素空间判别器（SAM视觉编码器初始化），λ₁=0.85, λ₂=0.15。采用立方时间步调度偏向高噪声水平以鼓励探索新模式，判别器使用均匀时间步以捕捉不同尺度的特征。

3. **ADM与ADP的本质区别**: ADM属于分数蒸馏——监督整个概率流在不同噪声水平的匹配；ADP属于对抗蒸馏——仅关心t=0时的干净数据分布。ADP通过各向同性高斯噪声人为创造支撑集重叠区域，使判别更困难、梯度更平滑，为ADM微调提供稳定初始化。

### 损失函数 / 训练策略

ADM使用Hinge GAN损失对齐PF-ODE预测；ADP使用混合Hinge损失（潜在+像素空间）。ADP采用立方生成器时间步调度+均匀判别器时间步调度。SDXL一步蒸馏：先ADP预训练再ADM微调，总GPU时间少于DMD2。

## 实验关键数据

### 主实验

| 模型 | 方法 | NFE | FID↓ | CLIP Score↑ | GenEval |
|------|------|-----|------|-------------|---------|
| SDXL | 基线(50步) | 50 | - | - | - |
| SDXL | DMD2 | 1 | 对比基线 | 对比基线 | 对比基线 |
| SDXL | **DMDX** | **1** | **优于DMD2** | **优于DMD2** | **优于DMD2** |
| SD3-Medium | ADM | 8步 | 新基准 | - | - |
| SD3.5-Large | ADM | 多步 | 新基准 | - | - |
| CogVideoX-2B | ADM | 8步 | VBench 79.86 | - | - |
| CogVideoX-5B | ADM | 8步 | VBench 82.06 | - | - |

DMDX在一步SDXL上达到50步基线的竞争性保真度(50×加速)。

### 消融实验

- DMD损失在ADM训练过程中自然下降，验证了判别器隐式涵盖逆KL散度的假设
- 混合判别器(潜在+像素)优于单一判别器
- 立方时间步调度有效提升模式多样性
- ADP预训练对一步蒸馏至关重要，提供更好的支撑集重叠

### 关键发现

- 一步蒸馏的核心瓶颈不是假分数估计器误差，而是学生-教师分布支撑集重叠不足
- 可学习判别器能隐式近似任意非线性函数来度量分布差异，比预定义散度更灵活
- ADM可直接扩展到视频生成(CogVideoX)，说明方法的通用性
- 良好初始化后，TTUR(两时间尺度更新规则)对最终性能影响有限

## 亮点与洞察

- 用对抗方式替代预定义散度进行分数蒸馏，思路清晰且理论有深度
- ADP+ADM两阶段管线设计合理，解决了一步蒸馏的初始化难题
- 首次将分数蒸馏扩展到视频扩散模型(CogVideoX)
- 混合判别器(潜在+像素空间)的设计可借鉴到其他GAN训练场景

## 局限与展望

- 方法仍需两阶段训练（预训练+微调），流程较复杂
- 判别器使用冻结教师模型作为backbone，内存开销大
- 仅在Stable Diffusion系列和CogVideoX上验证，未测试其他架构
- 像素空间判别器使用SAM编码器，引入了额外依赖

## 相关工作与启发

- DMD/DMD2是最直接的基线和改进对象
- ADD(对抗扩散蒸馏)、SDXL-Lightning等对抗方法提供了重要参考
- Rectified Flow的ODE对收集策略被ADP借鉴
- 分数蒸馏到对抗蒸馏的统一视角有理论贡献

## 评分

- 新颖性: ⭐⭐⭐⭐ — 对抗式分数蒸馏的思路新颖
- 技术深度: ⭐⭐⭐⭐⭐ — 理论分析扎实，ADM/ADP区别讨论深入
- 实验充分性: ⭐⭐⭐⭐ — 图像+视频、多模型验证
- 写作质量: ⭐⭐⭐⭐ — 动机清晰，理论推导完整
- 实用价值: ⭐⭐⭐⭐ — 50×加速且质量保持，实际价值高

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] FVGen: Accelerating Novel-View Synthesis with Adversarial Video Diffusion Distillation](fvgen_accelerating_novel-view_synthesis_with_adversarial_video_diffusion_distill.md)
- [\[ICCV 2025\] Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis](causal-entity_reflected_egocentric_traffic_accident_video_synthesis.md)
- [\[ICCV 2025\] DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation](dh-facevid-1k_a_large-scale_high-quality_dataset_for_face_video_generation.md)
- [\[ICCV 2025\] ReCamMaster: Camera-Controlled Generative Rendering from A Single Video](recammaster_camera-controlled_generative_rendering_from_a_single_video.md)
- [\[ICCV 2025\] X-Dancer: Expressive Music to Human Dance Video Generation](x-dancer_expressive_music_to_human_dance_video_generation.md)

</div>

<!-- RELATED:END -->
