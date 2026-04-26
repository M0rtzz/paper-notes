---
title: >-
  [论文解读] LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation
description: >-
  [ICCV 2025][图像分割][二分图像分割] 提出LawDIS，一种基于Stable Diffusion的语言-窗口双控可控二分图像分割框架，在宏观模式下通过语言提示指导目标分割，在微观模式下通过可变尺寸窗口精细化局部细节，在DIS5K上全面超越11种SOTA方法。
tags:
  - ICCV 2025
  - 图像分割
  - 二分图像分割
  - 扩散模型
  - 语言控制
  - 窗口细化
  - 高分辨率分割
---

# LawDIS: Language-Window-based Controllable Dichotomous Image Segmentation

**会议**: ICCV 2025  
**arXiv**: [2508.01152](https://arxiv.org/abs/2508.01152)  
**代码**: https://github.com/XinyuYanTJU/LawDIS (有)  
**领域**: 分割  
**关键词**: 二分图像分割, 扩散模型, 语言控制, 窗口细化, 高分辨率分割

## 一句话总结

提出LawDIS，一种基于Stable Diffusion的语言-窗口双控可控二分图像分割框架，在宏观模式下通过语言提示指导目标分割，在微观模式下通过可变尺寸窗口精细化局部细节，在DIS5K上全面超越11种SOTA方法。

## 研究背景与动机

二分图像分割（Dichotomous Image Segmentation, DIS）旨在从高分辨率图像中精确分割前景目标，要求捕捉物体的精细结构和内部细节，是3D重建、图像编辑、AR等应用的基础。

现有DIS方法的局限：

1. **语义模糊性**：当图像中存在多个前景实体时，判别式方法（per-pixel分类）无法让用户指定要分割哪个目标
2. **分辨率受限**：多数方法通过下采样到1024px来处理高分辨率图像，但无限放大输入计算不可行
3. **缺乏局部细化能力**：一些方法（如MVANet）将图像切成固定大小patch，但在推理时遇到不同patch大小就会失败
4. **无交互性**：现有方法输出固定结果，用户无法根据需求调整

**核心思路**：将DIS重新定义为基于潜在扩散模型（Latent Diffusion Model）的图像条件mask生成任务，天然支持各种用户控制信号的接入。

## 方法详解

### 整体框架

LawDIS基于Stable Diffusion v2，通过一个**模式切换器（Mode Switcher）**支持两种控制模式：

- **宏观模式（Macro Mode）**：语言控制分割——用户输入语言提示指定要分割的目标
- **微观模式（Micro Mode）**：窗口控制细化——用户指定局部窗口区域进行精细化

两种模式可独立运行或联合使用。

### 关键设计

**1. 生成式范式（Generative Formulation）**

将DIS建模为条件去噪扩散：对分割mask的潜在表示做前向加噪和反向去噪
- 输入图像x通过VAE编码为潜在表示作为条件
- 分割mask编码后加噪，由UNet预测噪声
- 使用TCD（Trajectory Consistency Distillation）调度器实现单步去噪，大幅提升效率

**2. 模式切换器（Mode Switcher）**

- 一维向量通过位置编码后加到扩散模型的时间嵌入上
- 不同值激活不同模式（宏观或微观）
- 训练时两种模式联合优化同一个UNet

**3. 语言控制分割（宏观模式）**

- 语言提示由VLM生成或用户自定义
- 通过CLIP编码为控制嵌入，通过cross-attention注入UNet
- 损失函数为标准扩散去噪目标

**4. 窗口控制细化（微观模式）**

- 从初始分割结果中裁剪不满意区域作为refine窗口
- 关键创新：**用初始分割的局部mask（而非高斯噪声）作为扩散起点**，间接传递全局上下文
- 使用空提示，裁剪的局部patch上采样到模型输入尺寸
- 细化结果替换回初始分割图的对应位置

**5. VAE Decoder微调**

- 冻结VAE Encoder和UNet，仅微调Decoder
- 添加Encoder-Decoder跳跃连接
- 输出通道从3改为1（用于mask），权重通过通道平均初始化

### 损失函数 / 训练策略

- UNet训练：L_u = L_macro + L_micro（联合训练）
- VAE Decoder训练：L_d = L_wbce + L_wiou（wBCE + wIoU）
- UNet训练30K iterations，VAE Decoder训练6K iterations
- batch size=32，Adam optimizer，lr=3e-5
- 所有输入统一resize到1024x1024
- 使用DDPM 1000步训练UNet，TCD单步调度训练Decoder

## 实验关键数据

### 主实验

DIS5K测试集（DIS-TE，2000张图），与11种方法对比：

| 方法 | F_beta_w | F_beta_mx | MAE | S_alpha | E_phi_mn |
|------|----------|-----------|-----|---------|----------|
| BiRefNet'24 | 0.858 | 0.896 | 0.035 | 0.901 | 0.934 |
| MVANet'24 | 0.862 | 0.907 | 0.034 | 0.909 | 0.938 |
| **Ours-S (仅语言)** | 0.898 | 0.929 | 0.027 | 0.925 | 0.955 |
| **Ours-R (语言+窗口)** | **0.908** | **0.932** | **0.024** | **0.926** | **0.959** |

在DIS-TE1上，Ours-S比MVANet的F_beta_w提升6.6%，Ours-R提升7.0%。

### 消融实验

DIS-TE4子集上的消融：

| 配置 | F_beta_mx | MAE | S_alpha | E_phi_mn |
|------|-----------|-----|---------|----------|
| Baseline (vanilla SD) | 0.904 | 0.047 | 0.904 | 0.916 |
| w/o micro训练 | 0.912 | 0.037 | 0.909 | 0.943 |
| w/o VAE Decoder微调 | 0.919 | 0.040 | 0.915 | 0.933 |
| **Full Ours-S** | **0.926** | **0.032** | **0.920** | **0.955** |

微观模式效果（DIS-TE4）：

| 配置 | F_beta_w | MAE | BIoU_m | HCE |
|------|----------|-----|--------|------|
| Ours-S (baseline) | 0.890 | 0.032 | 0.795 | 2481 |
| 从噪声初始化 | -4.7% | +1.9% | -7.1% | -863 |
| 自动窗口选择 | +1.7% | -0.5% | +2.9% | -767 |
| 半自动窗口选择 | **+2.0%** | **-0.6%** | **+3.2%** | **-871** |

### 关键发现

1. 从扩散潜在表示初始化比从噪声初始化好得多（F_beta_w差4.7%），证明从初始分割传递全局上下文是必要的
2. 联合训练两种模式比单独训练宏观模式更好（互相增强几何表示能力）
3. VAE Decoder微调是必要的——不微调时MAE从0.032上升到0.040
4. 即使完全自动的窗口选择也能有效改善分割质量，用户交互不是必须的
5. 语言提示在训练和测试时都使用效果最好

## 亮点与洞察

- **将DIS从判别式重新定义为生成式任务**，开辟了全新的方法论路径
- **模式切换器的设计极其优雅**：仅一个一维向量就能控制同一UNet在两种模式间切换
- **用初始分割结果而非噪声初始化微观模式的扩散过程**，是传递跨尺度上下文的关键技巧
- 语言控制让DIS首次具备了**交互性和个性化能力**
- TCD单步去噪使得基于扩散的方法在效率上实用化

## 局限性 / 可改进方向

1. 依赖VLM生成语言提示，提示质量直接影响分割效果
2. 微观模式需要用户或自动算法选择窗口位置，增加了交互复杂度
3. 基于Stable Diffusion v2的架构，模型参数量大、推理仍比判别式方法慢
4. 统一resize到1024x1024处理可能在超高分辨率图像上损失细节
5. DIS5K benchmark仅225个语义类别，更广泛场景下的泛化性待验证

## 相关工作与启发

- GenPercept也将扩散模型用于密集预测，但采用确定性单步范式；LawDIS保持了扩散过程并引入双控机制
- MVANet通过patch切分处理高分辨率，但缺乏对不同patch size的适应性；LawDIS的窗口细化天然支持任意尺寸
- 模式切换器的设计思路可以推广到其他需要多粒度控制的视觉生成任务

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 将DIS重定义为条件扩散生成，双控模式设计原创性强
- 实验充分度: ⭐⭐⭐⭐⭐ — DIS5K全面对比11种方法，消融详尽，定性对比清晰
- 写作质量: ⭐⭐⭐⭐ — 方法描述清楚，图示直观
- 价值: ⭐⭐⭐⭐⭐ — 为DIS引入交互性和可控性，开辟新方向，刷新全指标SOTA

<!-- RELATED:START -->

## 相关论文

- [\[ICCV 2025\] VSC: Visual Search Compositional Text-to-Image Diffusion Model](vsc_visual_search_compositional_text-to-image_diffusion_model.md)
- [\[ICCV 2025\] Exploring Probabilistic Modeling Beyond Domain Generalization for Semantic Segmentation](exploring_probabilistic_modeling_beyond_domain_generalization_for_semantic_segme.md)
- [\[ICCV 2025\] SPADE: Spatial-Aware Denoising Network for Open-vocabulary Panoptic Scene Graph Generation](spade_spatial-aware_denoising_network_for_open-vocabulary_panoptic_scene_graph_g.md)
- [\[ICCV 2025\] Can Generative Geospatial Diffusion Models Excel as Discriminative Geospatial Foundation Models?](can_generative_geospatial_diffusion_models_excel_as_discriminative_geospatial_fo.md)
- [\[ICCV 2025\] UniGlyph: Unified Segmentation-Conditioned Diffusion for Precise Visual Text Synthesis](uniglyph_unified_segmentation-conditioned_diffusion_for_precise_visual_text_synt.md)

<!-- RELATED:END -->
