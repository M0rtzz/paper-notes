---
title: >-
  [论文解读] Addressing Text Embedding Leakage in Diffusion-based Image Editing
description: >-
  [ICCV 2025][图像生成][attribute leakage] 提出ALE框架，通过对象限制嵌入(ORE)解耦EOS token的语义纠缠、区域引导混合交叉注意力掩码(RGB-CAM)约束空间注意力、背景混合(BB)保留未编辑区域，系统性解决扩散模型文本图像编辑中的属性泄漏问题，并建立了ALE-Bench评估基准。
tags:
  - ICCV 2025
  - 图像生成
  - attribute leakage
  - 扩散模型
  - EOS embedding
  - 注意力机制
  - multi-object editing
---

# Addressing Text Embedding Leakage in Diffusion-based Image Editing

**会议**: ICCV 2025  
**arXiv**: 无  
**代码**: [GitHub](https://github.com/mtablo/ALE_Edit_page)  
**领域**: 图像编辑 / 扩散模型  
**关键词**: attribute leakage, diffusion image editing, EOS embedding, cross-attention masking, multi-object editing

## 一句话总结

提出ALE框架，通过对象限制嵌入(ORE)解耦EOS token的语义纠缠、区域引导混合交叉注意力掩码(RGB-CAM)约束空间注意力、背景混合(BB)保留未编辑区域，系统性解决扩散模型文本图像编辑中的属性泄漏问题，并建立了ALE-Bench评估基准。

## 研究背景与动机

基于扩散模型的文本图像编辑虽然进步显著，但仍面临严重的属性泄漏(attribute leakage)问题：编辑目标对象时意外影响了不相关区域。作者将泄漏分为两类：(1) 目标外泄漏(TEL)——目标对象的属性影响非目标区域；(2) 目标内泄漏(TIL)——一个目标对象的属性影响另一个目标对象。根本原因在于自回归文本编码器（如CLIP）的EOS(End-of-Sequence) token不加区分地聚合了提示中所有token的信息，导致通过cross-attention层时属性在空间上无差别扩散。现有方法试图通过操纵注意力图来约束编辑效果，但未从根源解决EOS嵌入纠缠问题。

## 方法详解

### 整体框架

ALE是一个无需微调(tuning-free)的图像编辑框架，基于双分支(dual-branch)扩散模型架构。框架由三个互补组件组成：ORE处理文本嵌入层面的纠缠，RGB-CAM处理空间注意力层面的泄漏，BB处理背景保护。三者缺一不可——单独使用BB只能防TEL不能防TIL，单独使用ORE+RGB-CAM能减少TIL但不能保护背景。

### 关键设计

1. **对象限制嵌入(ORE)**: 为提示中的每个目标对象分配独立的、语义隔离的文本嵌入，避免不同对象属性在EOS token中混合。具体做法是对每个对象单独运行文本编码器生成嵌入，而非将所有对象放在同一提示中，从根源切断EOS token的语义纠缠。

2. **区域引导混合交叉注意力掩码(RGB-CAM)**: 利用分割掩码约束cross-attention，使每个对象的注意力仅限于其指定区域。通过将分割掩码与注意力图混合，防止属性在空间上的不当扩散，实现精确的区域级编辑。

3. **背景混合(BB)**: 通过将源图像的latent与编辑后的latent在非编辑区域进行混合，保留非目标区域的结构完整性和外观一致性，有效防止目标外泄漏。

### 损失函数 / 训练策略

ALE是无需训练的方法，直接在推理阶段通过修改扩散采样过程实现。支持Prompt-to-Prompt等现有编辑管线作为基础架构。

## 实验关键数据

### 主实验

| 方法 | TELS↓ | TILS↓ | Structure Dist↓ | PSNR↑ | SSIM↑ |
|------|-------|-------|-----------------|-------|-------|
| P2P | 21.52 | 17.26 | 0.1514 | 11.15 | 0.5589 |
| MasaCtrl | 20.18 | 16.74 | 0.0929 | 14.99 | 0.7346 |
| InfEdit | 19.59 | 16.69 | 0.0484 | 16.74 | 0.7709 |
| **ALE** | **16.03** | **15.28** | **0.0167** | **30.04** | **0.9228** |

ALE在所有指标上大幅领先，PSNR从次优的16.74提升到30.04，SSIM从0.77提升到0.92。

### 消融实验

- BB单独使用：解决TEL但无法解决TIL
- ORE + RGB-CAM：减少TIL但无法保护背景(TEL仍存在)
- 完整ALE(BB + ORE + RGB-CAM)：同时消除TEL和TIL
- 不同编辑对象数(1/2/3)和编辑类型(颜色/材质/物体)下均保持稳健

### 关键发现

- EOS token是属性泄漏的根本原因，而非仅仅是注意力图问题
- 多对象编辑比单对象编辑更容易出现泄漏，但ALE在3对象编辑时性能甚至优于1对象
- 组合编辑类型(如颜色+物体)的泄漏最严重，ALE仍能有效控制

## 亮点与洞察

- 问题分析深入——准确定位EOS嵌入纠缠为属性泄漏的根本原因
- ALE-Bench评估基准和TELS/TILS指标填补了多对象编辑评估的空白
- 无需训练的方法，可以即插即用到各种基于扩散模型的编辑框架中
- 背景保护效果极其优秀(PSNR 30.04 vs 16.74)

## 局限与展望

- 目前仅支持局部、相对简单的变换（颜色/材质/物体替换），不支持风格迁移、姿态变化等非刚性变换
- ALE-Bench仅包含20张精心挑选的图像，泛化性有待验证
- 需要分割掩码作为输入（RGB-CAM依赖），增加了使用门槛
- 编辑时需对每个对象单独编码（ORE），多对象时计算开销线性增长

## 相关工作与启发

- Prompt-to-Prompt、MasaCtrl、InfEdit等tuning-free编辑方法是主要对比基线
- EOS token语义纠缠问题可能也存在于其他使用CLIP文本编码器的生成任务中
- 区域级编辑控制的思路可迁移到视频编辑、3D编辑等领域

## 评分

- 新颖性: ⭐⭐⭐⭐ — 对EOS嵌入泄漏的分析深刻且原创
- 技术深度: ⭐⭐⭐⭐ — 三组件互补设计逻辑严密
- 实验充分性: ⭐⭐⭐⭐ — 新基准+新指标+全面对比+消融
- 写作质量: ⭐⭐⭐⭐⭐ — 问题定义清晰，可视化出色
- 实用价值: ⭐⭐⭐⭐ — 无需训练，直接可用，效果显著

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] ALE: Attribute-Leakage-free Editing for Text-based Image Editing](ale_attribute_leakage_free_editing.md)
- [\[ICCV 2025\] Exploring Multimodal Diffusion Transformers for Enhanced Prompt-based Image Editing](exploring_multimodal_diffusion_transformers_for_enhanced_prompt-based_image_edit.md)
- [\[ICCV 2025\] CoMPaSS: Enhancing Spatial Understanding in Text-to-Image Diffusion Models](compass_enhancing_spatial_understanding_in_text-to-image_diffusion_models.md)
- [\[ICCV 2025\] Text Embedding Knows How to Quantize Text-Guided Diffusion Models](text_embedding_knows_how_to_quantize_text-guided_diffusion_models.md)
- [\[ICCV 2025\] Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation](dense2moe_restructuring_diffusion_transformer_to_moe_for_efficient_text-to-image.md)

</div>

<!-- RELATED:END -->
