---
title: >-
  [论文解读] Exploring Pre-trained Text-to-Video Diffusion Models for Referring Video Object Segmentation
description: >-
  [ECCV 2024][视频生成] VD-IT首次探索预训练T2V扩散模型（ModelScopeT2V）在视频理解任务中的应用，通过Text-Guided Image Projection和Video-specific Noise Prediction设计，从固定T2V模型中提取语义对齐、时序一致的视频特征，在Referring VOS任务上超越传统判别式backbone。
tags:
  - ECCV 2024
  - 视频生成
  - Text-to-Video扩散模型
  - 时序一致性
  - 视频理解
  - 特征提取
---

# Exploring Pre-trained Text-to-Video Diffusion Models for Referring Video Object Segmentation

**会议**: ECCV 2024  
**arXiv**: [2403.12042](https://arxiv.org/abs/2403.12042)  
**代码**: [https://github.com/buxiangzhiren/VD-IT](https://github.com/buxiangzhiren/VD-IT)  
**领域**: 视频生成  
**关键词**: 文本引导视频物体分割, Text-to-Video扩散模型, 时序一致性, 视频理解, 特征提取

## 一句话总结

VD-IT首次探索预训练T2V扩散模型（ModelScopeT2V）在视频理解任务中的应用，通过Text-Guided Image Projection和Video-specific Noise Prediction设计，从固定T2V模型中提取语义对齐、时序一致的视频特征，在Referring VOS任务上超越传统判别式backbone。

## 研究背景与动机

1. **领域现状**：Referring Video Object Segmentation（R-VOS）是根据自然语言描述在视频中分割特定物体的任务。现有方法以SgMg等为代表，使用判别式预训练的Video Swin Transformer作为视频backbone，再与文本驱动的mask decoder联合微调。

2. **现有痛点**：(1) 判别式预训练（如分类任务）的视频backbone在时序一致性方面表现不佳，光照变化等因素导致跨帧特征不稳定；(2) backbone需要联合微调，增加计算成本且可能破坏预训练知识；(3) 判别式特征缺乏文本语义对齐能力。

3. **核心矛盾**：R-VOS需要同时满足时序一致性（同一物体跨帧特征稳定）和空间精度（精细mask边界），但判别式backbone在这两方面存在trade-off。

4. **本文要解决什么？** 验证T2V生成模型学到的表示是否天然具备语义对齐和时序一致性，并设计专门框架将其用于视频理解。

5. **切入角度**：秉持"What I cannot create, I do not understand"的原则——能基于文本生成时序一致视频的模型，必然包含足够的视频理解知识。T2V模型用全局文本作为条件指导帧生成，天然保证了时序语义一致性。

6. **核心idea一句话**：固定预训练T2V扩散模型作为特征提取器，通过同时使用文本和图像token作为条件提取兼具时序一致性和细节丰富性的视频特征。

## 方法详解

### 整体框架

VD-IT分两部分：(1) 视频特征提取——将视频帧和referring text输入固定的T2V扩散模型（ModelScopeT2V），通过一步低噪声前向+UNet前传提取多尺度视频特征；(2) Mask预测头——从文本提取instance query，与视频特征融合生成最终分割mask。

### 关键设计

1. **Text-Guided Image Projection**:
    - 做什么：同时使用referring text和每帧视觉token作为T2V模型的条件prompt
    - 核心思路：CLIP视觉模型提取每帧的visual token，T2V文本编码器提取referring text token。用text-guided交叉注意力将文本语义注入视觉token：$p_{ve,t} = MLP(p_e + Softmax(\frac{p_e W^Q (p_{v,t} W^K)^T}{\sqrt{d_k}}) p_{v,t} W^V)$
    - 设计动机：只用文本prompt（VD-T）缺乏细粒度实例信息导致mask边界粗糙；只用视觉token（VD-I）会引入语义噪声导致实例混淆。结合两者，文本确保时序语义一致，视觉token提供实例细节

2. **Video-specific Noise Prediction**:
    - 做什么：预测视频相关的噪声替代标准高斯噪声，保留特征保真度
    - 核心思路：将视频latent送入卷积层后归一化生成预测噪声：$n_t = (f_{n,t} W^N - \mu(f_{n,t} W^N)) / (\sigma(f_{n,t} W^N) + \epsilon)$，然后将这个去相关噪声以最小强度（step=0）添加到视频latent
    - 设计动机：标准高斯噪声会模糊关键细节且与视频内容不相关。预测视频相关噪声既满足扩散模型输入要求，又最大程度保留原始视频信号

3. **Mask预测头**:
    - 做什么：从文本中匹配实例，与视频特征融合生成分割mask
    - 核心思路：可学习instance query与RoBERTa提取的文本特征做交叉注意力得到实例表示；通过Deformable Transformer编码器-解码器与多尺度视频特征融合；最终通过bbox头+分类头+动态卷积mask头输出预测
    - 设计动机：遵循query-based分割范式，与提取的视频特征格式兼容

### 损失函数 / 训练策略

使用Dice loss + Focal loss用于mask，Focal loss用于分类置信度，L1 + GIoU loss用于bbox。固定T2V模型参数，只训练Image Projection模块、噪声预测模块和mask预测头。2块A100训练9个epoch。

## 实验关键数据

### 主实验

| 方法 | Backbone | Ref-YouTube-VOS J&F | Ref-DAVIS17 J&F |
|------|----------|---------------------|-----------------|
| SgMg | V-Swin | 61.6 | 63.3 |
| OnlineRefer | V-Swin | 62.9 | 64.8 |
| **VD-IT** | **T2V Diffusion** | **64.8** | **69.4** |

### 消融实验

| 配置 | Ref-YouTube J&F | 说明 |
|------|----------------|------|
| VD-T (只用文本) | 59.2 | 低层特征缺细节 |
| VD-I (只用图像) | 62.1 | 实例混淆问题 |
| VD-IT (文本+图像) | 64.8 | 兼具两者优势 |
| VD-IT w/ Gaussian噪声 | 62.8 | 细节模糊 |
| VD-IT w/ 预测噪声 | **64.8** | 保真度更高 |

### 关键发现

- **T2V扩散特征的时序一致性显著优于判别式backbone**：K-Means聚类可视化表明V-Swin特征受光照影响变化剧烈，而VD-IT特征跨帧高度一致
- **文本条件是时序一致性的关键**：VD-I（无文本）特征虽然细节丰富但存在实例混淆，加入文本后VD-IT显著改善
- **生成模型的去噪能力增强了鲁棒性**：扩散模型天然的去噪特性使其特征对光照变化和相机运动更鲁棒
- **不能简单替换backbone**：直接使用T2V模型不做任何设计无法超过现有方法，Text-Guided Projection和Noise Prediction是关键

## 亮点与洞察

- **生成模型用于理解任务的成功范例**："能创造即能理解"的假设在视频领域得到初步验证，T2V模型的视觉表示具有优于判别式模型的时序一致性
- **Image-Text联合投影设计精巧**：文本提供语义指导确保时序匹配，图像token提供实例细节，两者互补
- **视频特定噪声预测**：简单但有效，只需一个带归一化的线性层就能显著提升特征质量

## 局限性 / 可改进方向

- T2V模型体积大（ModelScopeT2V的UNet），推理开销比V-Swin更大
- 只在R-VOS任务上验证，需要扩展到更多视频理解任务（如VOS、视频问答等）
- 固定T2V模型不微调可能限制上限，探索高效微调策略（如LoRA）可能进一步提升
- 可以尝试更新更强的T2V模型（如Sora架构）

## 相关工作与启发

- **vs SgMg**: SgMg用V-Swin微调后做分割，VD-IT用固定T2V扩散模型提取特征，后者时序一致性更好
- **vs VPD/ODISE等图像扩散理解工作**: 它们探索T2I扩散模型做图像理解，VD-IT首次将思路扩展到T2V+视频理解
- 这一思路可以推广到所有需要时序一致特征的视频任务

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首次探索T2V扩散模型做视频理解，假设新颖且得到验证
- 实验充分度: ⭐⭐⭐⭐ 四个benchmark全面验证+深入特征分析
- 写作质量: ⭐⭐⭐⭐ 分析从VD-T到VD-I到VD-IT的递进逻辑清晰
- 价值: ⭐⭐⭐⭐⭐ 开辟了生成式视频模型用于理解任务的新方向

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] FreeInit: Bridging Initialization Gap in Video Diffusion Models](freeinit_bridging_initialization_gap_in_video_diffusion.md)
- [\[ECCV 2024\] Kalman-Inspired Feature Propagation for Video Face Super-Resolution](kalman-inspired_feature_propagation_for_video_face_super-resolution.md)
- [\[ECCV 2024\] Evaluating Text-to-Visual Generation with Image-to-Text Generation](evaluating_text-to-visual_generation_with_image-to-text_generation.md)
- [\[ECCV 2024\] VFusion3D: Learning Scalable 3D Generative Models from Video Diffusion Models](vfusion3d_learning_scalable_3d_generative_models_from_video_diffusion_models.md)
- [\[ECCV 2024\] SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](sv3d_novel_multi-view_synthesis_and_3d_generation_from_a_single_image_using_late.md)

</div>

<!-- RELATED:END -->
