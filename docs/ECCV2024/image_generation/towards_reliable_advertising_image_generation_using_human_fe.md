---
title: >-
  [论文解读] Towards Reliable Advertising Image Generation Using Human Feedback
description: >-
  [ECCV 2024][图像生成][广告图像生成] 针对电商广告图像生成中大量不可用图像（空间不匹配、尺寸不匹配、不显著、形状幻觉）的问题，构建了百万级RF1M数据集训练多模态检测网络RFNet，并提出基于RFNet反馈微调扩散模型的RFFT方法（含Consistent Condition正则化），将可用率从约50%提升至接近100%且不损失美观性。
tags:
  - ECCV 2024
  - 图像生成
  - 广告图像生成
  - 扩散模型
  - 人类反馈
  - 质量检测
  - 电商
---

# Towards Reliable Advertising Image Generation Using Human Feedback

**会议**: ECCV 2024  
**arXiv**: [2408.00418](https://arxiv.org/abs/2408.00418)  
**代码**: https://github.com/ZhenbangDu/Reliable_AD (有)  
**领域**: 多模态VLM  
**关键词**: 广告图像生成, Diffusion Model, 人类反馈, 质量检测, 电商

## 一句话总结
针对电商广告图像生成中大量不可用图像（空间不匹配、尺寸不匹配、不显著、形状幻觉）的问题，构建了百万级RF1M数据集训练多模态检测网络RFNet，并提出基于RFNet反馈微调扩散模型的RFFT方法（含Consistent Condition正则化），将可用率从约50%提升至接近100%且不损失美观性。

## 研究背景与动机
1. **领域现状**：电商场景下，自动生成有吸引力的广告图像是刚需。利用Stable Diffusion + ControlNet生成与产品匹配的背景已展现潜力。
2. **现有痛点**：(1) 生成模型频繁产出低质量广告图像（空间不匹配、尺寸不匹配、产品不突出、形状幻觉），误导消费者；(2) 大量人工检查筛选成本高昂；(3) 可用图像比例低，限制了生成模型在广告领域的大规模应用。
3. **核心矛盾**：生成模型能制作精美背景但无法保证产品在背景中的"可用性"。需要可靠的检测+生成改进的端到端方案。
4. **核心idea**：构建RFNet模拟人类检查员→回环生成（Recurrent Generation）提高可用数量→用RFNet反馈微调扩散模型（RFFT）从根本上提高生成质量。

## 方法详解

### 整体框架
三段式方案：(1) 构建RF1M数据集（105万张人工标注的生成广告图像）；(2) 训练RFNet多模态检测网络，自动判断生成图像是否可用；(3) 用RFNet反馈信号通过RFFT微调ControlNet，并引入Consistent Condition正则化防止美观度崩塌。

### 关键设计

1. **RF1M数据集**：
    - 做什么：构建百万级广告图像可用性数据集
    - 规模：1,058,230张生成广告图像，每张含生成图、透明背景产品图、prompt、深度图、显著性图、产品标题
    - 标注类别：Available、Space Mismatch（产品与背景空间关系不当）、Size Mismatch（产品尺寸与背景不匹配）、Indistinctiveness（产品不突出）、Shape Hallucination（背景错误扩展产品形状）
    - 亮点：多模态设计，数据来自JD.com实际产品，线上A/B测试CTR提升2.2%

2. **RFNet多模态检测网络**：
    - 做什么：融合多模态信息自动判断广告图像可用性
    - 输入：产品原图、生成广告图、深度图、显著性图、产品标题
    - 核心架构：Feature Filter Module(FFM)用cross-attention融合产品图像特征和文本特征→self-attention层融合所有模态特征→全连接分类器
    - 设计动机：单一模态不足以判断所有失败类型，深度图帮助判断空间关系，显著性图帮助判断产品突出程度，产品标题帮助识别产品属性

3. **Consistent Condition正则化**：
    - 做什么：解决RFFT微调过程中背景美观度崩塌的问题
    - 核心问题：直接用RFNet反馈梯度微调扩散模型，模型会学会生成重复简单的背景（可用率达99.8%但丑陋）；KL正则化与反馈梯度方向对抗，类似adversarial training
    - 解决方案：CC正则化保持条件输入的一致性，不约束生成分布与参考分布相同，而是约束对同一条件的输出保持稳定，避免了KL正则化的对抗性
    - 效果：在提高可用率的同时保持图像美观性

### 损失函数 / 训练策略
- **RFNet**：标准交叉熵分类损失，在RF1M上训练
- **RFFT**：选择DDIM去噪过程最后10步中随机一步，生成预测图像→RFNet评估→反馈损失 F_AC = -1/N Σ y_d·log(ô_i) 反传至ControlNet
- **总损失**：RFFT loss + CC正则化项

## 实验关键数据

### 主实验

| 模型 | Precision | Recall | F1 | AP |
|------|-----------|--------|-----|-----|
| ResNet50 | 74.87 | 73.66 | 74.26 | 77.29 |
| ResNeXt50 | 77.73 | 76.88 | 77.30 | 79.62 |
| HRNet | 72.89 | 73.12 | 73.01 | 73.07 |
| ViT | 75.59 | 78.33 | 76.93 | 79.31 |
| **RFNet (Ours)** | **86.45** | **85.23** | **85.83** | **87.58** |

### 消融实验

| 模态组合 | AP |
|---------|-----|
| 生成图+深度+显著+标题 | 81.17 |
| 产品图+深度+显著+标题 | 82.06 |
| 产品图+生成图+显著+标题 | 85.31 |
| 全部模态（RFNet） | 87.58 |

### 关键发现
1. RFNet的F1 score达85.83%，远超单模态方法，多模态融合有效
2. 回环生成（Recurrent Generation）配合RFNet可将可用率从~50%大幅提升
3. RFFT+CC正则化可在保持美观性的前提下从根本上提高生成可用率
4. 线上A/B测试（6000万曝光）CTR提升2.2%，验证了实际商业价值
5. KL正则化在此场景下不如CC正则化——与反馈梯度产生adversarial效应

## 亮点与洞察
1. **端到端闭环**：检测→反馈→生成改进的完整闭环，从"事后检查"到"事前预防"
2. **百万级数据集**：RF1M是目前最大规模的广告图像可用性数据集，标注体系完善
3. **CC正则化的洞察**：识别了KL正则化在反馈微调中的对抗本质，提出了更适合的替代方案
4. **工程落地价值**：在JD.com实际部署并验证了CTR提升

## 局限性 / 可改进方向
1. 标注类别固定为5类，可能无法覆盖所有失败模式
2. RFNet依赖辅助模型生成深度图和显著性图，增加了系统复杂度
3. RFFT仅微调ControlNet，未探索对基础扩散模型的微调效果
4. 数据集偏向JD.com产品风格，泛化到其他电商平台的效果待验证

## 相关工作与启发
- **DDPO/DPOK**：基于强化学习的扩散模型人类反馈对齐，本文用更直接的梯度回传方式
- **ReFL/DRaFT**：直接微调扩散模型的先驱，本文针对广告场景的特殊性（美观vs可用paradox）提出创新
- **ControlNet**：条件控制扩散模型的核心组件，本文在此基础上进行RFFT微调
- **Stable Diffusion Inpainting**：生成广告背景的基础技术，inpainting保持产品区域不变
- **启发**：CC正则化思路可推广到其他需要平衡"目标优化"和"多样性保持"的场景（如RLHF中的reward hacking问题）

## 评分
- 新颖性：⭐⭐⭐⭐ （CC正则化思路巧妙）
- 技术深度：⭐⭐⭐⭐ （多模态融合+反馈微调）
- 实验充分性：⭐⭐⭐⭐ （含线上A/B测试）
- 实用价值：⭐⭐⭐⭐⭐ （已在JD.com部署，CTR+2.2%）
- 写作质量：⭐⭐⭐⭐ （结构清晰，问题描述直观）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Realistic Human Motion Generation with Cross-Diffusion Models](realistic_human_motion_generation_with_cross-diffusion_models.md)
- [\[ECCV 2024\] DiffiT: Diffusion Vision Transformers for Image Generation](diffit_diffusion_vision_transformers_for_image_generation.md)
- [\[ECCV 2024\] Text2Place: Affordance-aware Text Guided Human Placement](text2place_affordance-aware_text_guided_human_placement.md)
- [\[ECCV 2024\] Learning Semantic Latent Directions for Accurate and Controllable Human Motion Prediction](learning_semantic_latent_directions_for_accurate_and_controllable_human_motion_p.md)
- [\[ECCV 2024\] Generating Human Interaction Motions in Scenes with Text Control](generating_human_interaction_motions_in_scenes_with_text_control.md)

<!-- RELATED:END -->
