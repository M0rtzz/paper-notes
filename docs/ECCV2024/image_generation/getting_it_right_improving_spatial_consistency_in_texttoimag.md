---
title: >-
  [论文解读] Getting it Right: Improving Spatial Consistency in Text-to-Image Models
description: >-
  [ECCV 2024][图像生成][文本生成图像] 发现现有VL数据集严重缺乏空间关系描述（如left/right/above/behind出现率极低），构建了首个空间聚焦的大规模数据集SPRIGHT（600万张图像重描述），仅用0.25%数据微调即可提升22%空间一致性得分，用<500张多物体图像微调达到T2I-CompBench空间SOTA 0.2133。
tags:
  - ECCV 2024
  - 图像生成
  - 文本生成图像
  - 空间关系
  - 数据集
  - 扩散模型
  - 图像描述
---

# Getting it Right: Improving Spatial Consistency in Text-to-Image Models

**会议**: ECCV 2024  
**arXiv**: [2404.01197](https://arxiv.org/abs/2404.01197)  
**代码**: https://spright-t2i.github.io/ (有)  
**领域**: 多模态VLM  
**关键词**: 文本生成图像, 空间关系, 数据集, Stable Diffusion, 图像描述

## 一句话总结
发现现有VL数据集严重缺乏空间关系描述（如left/right/above/behind出现率极低），构建了首个空间聚焦的大规模数据集SPRIGHT（600万张图像重描述），仅用0.25%数据微调即可提升22%空间一致性得分，用<500张多物体图像微调达到T2I-CompBench空间SOTA 0.2133。

## 研究背景与动机
1. **领域现状**：Stable Diffusion、DALL-E 3等T2I扩散模型可生成高质量逼真图像，但在空间关系一致性上表现糟糕——给定描述空间关系的prompt，生成图像往往不符合描述。
2. **现有痛点**：(1) T2I模型在"left of"、"above"、"behind"等空间关系prompt上频繁失败；(2) 现有VL数据集中空间词汇极度匮乏——COCO中"left"仅出现在0.16%的caption中，"above"仅0.61%；(3) 训练数据中缺少空间描述导致模型根本没学会空间概念。
3. **核心矛盾**：空间介词在英语中是高频词汇，但在VL数据集中近乎缺失。标注者倾向描述"what"而非"where"。
4. **核心idea**：(1) 创建空间聚焦的大规模数据集来填补数据瓶颈；(2) 发现用含多物体图像微调效果最佳——多物体=更多空间关系。

## 方法详解

### 整体框架
1. **SPRIGHT数据集构建**：用LLaVA-1.5-13B重新描述600万张图像，prompt引导生成空间聚焦的描述
2. **高效微调**：用SPRIGHT的小子集微调Stable Diffusion
3. **分析实验**：探索caption长度、空间vs通用caption、CLIP层激活、物体数量等因素的影响

### 关键设计

1. **SPRIGHT数据集**：
    - 规模：约600万张图像，来自CC-12M（230万）、Segment Anything（350万）、COCO（4万）、LAION-Aesthetics（5万）
    - 生成工具：LLaVA-1.5-13B
    - 空间关系覆盖率大幅提升：
     - "left"：COCO 0.16% → SPRIGHT 26.80%
     - "right"：COCO 0.47% → SPRIGHT 23.48%
     - "above"：COCO 0.61% → SPRIGHT 21.25%
     - "behind"：COCO 1.09% → SPRIGHT 21.13%
    - 三维评估：自动评估+人类评估+空间关系覆盖率统计

2. **多物体图像优先策略**：
    - 关键发现：训练在**物体数量多**的图像上效果显著更好
    - 仅用<500张多物体图像微调就达到SOTA
    - 原因分析：多物体=更多空间关系→模型学会生成更多物体→位置关系更准确
    - 解决了VISOR指出的核心问题——T2I模型常遗漏空间prompt中的物体

3. **caption质量评估流水线**：
    - 自动指标：空间词汇覆盖率
    - 语义相似度：SPRIGHT caption与ground truth的CLIP相似度
    - 人类评估：Amazon MTurk标注验证caption质量

### 损失函数 / 训练策略
- 基线模型：Stable Diffusion v1.5 / v2.1
- 微调方法：标准diffusion训练loss
- 训练数据量对比：
    - 0.25% SPRIGHT（~15K图像）：空间一致性+22%且FID/CMMD也改善
    - <500张多物体图像：空间SOTA成绩
- 额外发现：混合空间caption和通用caption比纯空间caption更好

## 实验关键数据

### 主实验

| 模型配置 | T2I-CompBench Spatial Score | FID改善 | CMMD改善 |
|---------|---------------------------|---------|---------|
| SD v1.5 baseline | ~0.15 | - | - |
| + 0.25% SPRIGHT | 0.15 → +22% | -31.04% | -29.72% |
| + <500多物体图像 | **0.2133 (SOTA)** | 改善 | 改善 |
| SD v2.1 baseline | ~0.15 | - | - |
| + SPRIGHT微调 | 显著提升 | 改善 | 改善 |

### 消融实验

| 因素 | 发现 |
|------|------|
| 长caption vs 短caption | 长caption更好但存在trade-off |
| 空间caption vs 通用caption | 混合最优 |
| 物体数量少 vs 多 | 多物体显著更优 |
| CLIP编码器层分析 | 不同层对空间词的响应不同 |
| 有/无否定词训练 | 否定词训练有帮助 |
| 注意力图分析 | SPRIGHT微调后attention map改善 |

### 关键发现
1. **数据瓶颈论**：空间关系理解不足的根因在数据而非模型——COCO中空间词出现率不到1%
2. **少量数据大幅提升**：仅0.25%的SPRIGHT数据就带来22%空间改善+FID/CMMD都更好
3. **多物体是关键**：<500张多物体图像 > 全量数据中随机采样，物体数量是最重要的训练信号
4. **空间提升不牺牲质量**：FID和CMMD同时改善，非此消彼长
5. **CLIP层分析**：空间词在CLIP不同层有不同的激活模式——为理解T2I空间编码提供了新视角

## 亮点与洞察
1. **问题定位精准**：从数据角度cut through——不是模型不行，是训练数据不教
2. **SPRIGHT数据集价值**：首个空间聚焦的600万级VL数据集，社区基础设施贡献
3. **极高数据效率**：<500张图像达到SOTA——证明关键在"对的数据"而非"多的数据"
4. **多物体洞察**：物体数量与空间理解的正相关关系是实用的选数据准则
5. **全面分析**：不仅提出方法，还提供了大量额外分析（层分析、否定词、长短caption等）

## 局限性 / 可改进方向
1. SPRIGHT caption由LLaVA-1.5生成，继承了LLaVA的偏差和幻觉
2. 仅在Stable Diffusion上验证，未测试DALL-E 3、Imagen等其他架构
3. 空间关系仅考虑2D图像平面，3D空间关系（如"in front of"的深度关系）更具挑战
4. <500张多物体图像的选择标准需要更明确的定义
5. LAION数据集的安全审查可能影响SPRIGHT的部分数据可用性

## 相关工作与启发
- **RECAP/PixArt-Alpha**：也用合成caption提升T2I质量，但关注细节描述而非空间关系
- **VISOR**：系统揭示T2I空间理解失败，SPRIGHT提供数据层面的解决方案
- **GLIGEN/SpaText**：通过额外条件控制实现空间布局，SPRIGHT通过数据改善更优雅
- **启发**：VL数据集中还有哪些语言维度被严重低估？计数？时间关系？

## 评分
- 新颖性：⭐⭐⭐⭐ （数据瓶颈视角+多物体洞察）
- 技术深度：⭐⭐⭐ （方法本身较直接——重caption+微调）
- 实验充分性：⭐⭐⭐⭐⭐ （极其全面的分析和消融）
- 实用价值：⭐⭐⭐⭐⭐ （600万级数据集+即用的微调方案）
- 写作质量：⭐⭐⭐⭐⭐ （数据分析清晰，发现有洞察力）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers](difftracker_texttoimage_diffusion_models_are_unsupervised_tr.md)
- [\[ECCV 2024\] NeuSDFusion: A Spatial-Aware Generative Model for 3D Shape Completion, Reconstruction, and Generation](neusdfusion_a_spatial-aware_generative_model_for_3d_shape_completion_reconstruct.md)
- [\[ECCV 2024\] MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model](motionlcm_real-time_controllable_motion_generation_via_latent_consistency_model.md)
- [\[ECCV 2024\] TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering](textdiffuser-2_unleashing_the_power_of_language_models_for_text_rendering.md)
- [\[ECCV 2024\] LCM-Lookahead for Encoder-based Text-to-Image Personalization](lcm-lookahead_for_encoder-based_text-to-image_personalization.md)

<!-- RELATED:END -->
