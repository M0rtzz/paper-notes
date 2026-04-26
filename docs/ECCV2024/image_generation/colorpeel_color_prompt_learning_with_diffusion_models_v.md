---
title: >-
  [论文解读] ColorPeel: Color Prompt Learning with Diffusion Models via Color and Shape Disentanglement
description: >-
  [ECCV 2024][图像生成][扩散模型] 提出 ColorPeel，通过在目标颜色的基础几何体上联合学习颜色和形状 token 来实现颜色与形状解耦，使 T2I 扩散模型能精确生成用户指定 RGB 颜色的物体。
tags:
  - ECCV 2024
  - 图像生成
  - 扩散模型
  - 颜色提示学习
  - 文生图个性化
  - 颜色-形状解耦
  - 注意力机制
---

# ColorPeel: Color Prompt Learning with Diffusion Models via Color and Shape Disentanglement

**会议**: ECCV 2024  
**arXiv**: [2407.07197](https://arxiv.org/abs/2407.07197)  
**代码**: https://moatifbutt.github.io/colorpeel/  
**领域**: LLM/NLP  
**关键词**: 扩散模型, 颜色提示学习, 文生图个性化, 颜色-形状解耦, Cross-Attention对齐

## 一句话总结

提出 ColorPeel，通过在目标颜色的基础几何体上联合学习颜色和形状 token 来实现颜色与形状解耦，使 T2I 扩散模型能精确生成用户指定 RGB 颜色的物体。

## 研究背景与动机

- **语言描述颜色的局限**: 语言以离散方式表示颜色，即使精确颜色名（如"beige"）也涵盖宽广的色彩范围，无法精确对应用户期望的 RGB 值
- **个性化方法的失败**: 现有 T2I 个性化方法（TI, DreamBooth, Custom Diffusion）直接从纯色图片学习时无法正确解耦颜色和形状，导致颜色混淆
- **RGB 直接输入无效**: SD 模型无法理解 RGB 三元组或十六进制颜色代码的文本输入

## 方法详解

### 整体框架

1. 给定用户指定的 RGB 值，自动生成一组基础几何体（2D: 圆、方、六边形、三角形；3D: 球、柱、六棱体、立方体、锥体）
2. 为每个形状和颜色分配独立的可学习 token（$s_i^*$ 和 $c^*$）
3. 使用 Custom Diffusion 基线进行联合优化，同时学习颜色 token 和形状 token
4. 应用 Cross-Attention Alignment (CAA) 损失促进颜色和形状注意力对齐

### 关键设计

- **颜色-形状解耦**: 同一颜色搭配至少两种不同形状，使模型能够"类比"出颜色的本质属性。训练 prompt 格式: "A photo of $s_i^*$ shape in $c^*$ color"
- **Cross-Attention Alignment (CAA) 损失**: 对齐颜色和形状 token 的交叉注意力图，用余弦相似度约束两者关注相同的空间区域，防止注意力泄漏到背景
- **3D 形状优于 2D**: 3D 形状经历物理变换（阴影、光照），生成的颜色 prompt 更接近真实场景

### 损失函数 / 训练策略

$$\mathcal{V}^* = \arg\min_{\mathcal{V}} \mathbb{E}[\mathcal{L}_{rec} + \lambda \cdot \mathcal{L}_{caa}]$$

- $\mathcal{L}_{rec}$: 标准 LDM 重建损失
- $\mathcal{L}_{caa} = 1 - \cos(\mathcal{A}_t^{c^*}, \mathcal{A}_t^{s^*})$: CAA 损失（$\lambda=0.2$ 为最优）
- 粗粒度颜色: 1500 步；细粒度颜色: 6000 步

## 实验关键数据

### 主实验

| 方法 | ΔE↓ | ΔE_ch↓ | MAE(rgb) 10%↓ | MAE(Hue) 100%↓ | 训练时间(min) |
|------|-----|--------|-------------|----------------|-----------|
| SD | 47.45 | 41.55 | 12.89 | 86.38 | - |
| Rich-Text | 36.62 | 32.48 | 9.91 | 93.51 | - |
| TI | 48.98 | 44.29 | 15.22 | 90.88 | 118 |
| DreamBooth | 50.71 | 46.29 | 14.75 | 88.72 | 56 |
| Custom Diffusion | 48.47 | 42.23 | 13.43 | 78.43 | 24 |
| **ColorPeel (3D)** | **21.39** | **16.51** | **4.36** | **21.35** | 19 |
| **ColorPeel (2D)** | **20.45** | **15.29** | **4.83** | **21.46** | - |

### 消融实验 (λ 值)

| λ | ΔE↓ | ΔE_Ch↓ | MAE(Hue) 100%↓ |
|---|-----|--------|----------------|
| 0.0 (= CD) | 48.47 | 42.23 | 78.43 |
| 0.2 (最优) | **21.39** | **16.51** | **21.35** |
| 1.0 | 24.43 | 18.64 | 34.35 |

### 关键发现

- ColorPeel 在所有颜色度量上大幅超越所有基线方法（ΔE 降低约 55%）
- 用户研究: 15 名参与者在 2AFC 实验中显著偏好 ColorPeel（Thurstone Case V z-score 最高）
- 去掉 CAA 损失后模型无法正确解耦颜色和形状，生成不一致的颜色

## 亮点与洞察

1. **首次系统化解决颜色提示学习问题**: 填补了 T2I 模型精确颜色控制的空白
2. **颜色插值**: 已学习的颜色 token 支持线性插值，可以无需训练生成中间颜色
3. **泛化能力**: ColorPeel 框架可扩展到纹理和材质学习
4. **注意力泄漏分析**: 通过可视化 cross-attention maps 揭示了个性化方法中的注意力泄漏问题

## 局限性 / 可改进方向

- 颜色空间极其广阔，当前单独训练每种颜色的方式不够高效
- 未显式分解反射率和光照，在特殊光照场景下可能受限
- 训练仍需 19 分钟/颜色，未来可探索颜色网格 token 插值减少训练需求
- 仅基于 SD v1.4 验证，对 SDXL 等更大模型的兼容性未验证

## 相关工作与启发

- 与 Break-a-Scene、Concept Decomposition 等多概念提取方法不同，ColorPeel 专注于抽象属性（颜色）的提取
- CAA 损失可推广到其他需要属性解耦的场景（如纹理、材质、光照等）
- 对 T2I 模型的可控性研究提供了新视角：从离散语义控制到连续属性控制

## 补充说明

- 2D 和 3D 几何体训练的效果差异不大（ΔE: 20.45 vs 21.39），但 3D 几何体在 MAE(Hue) 上更优
- 训练仅需约 19 分钟/颜色（比 TI 的 118 分钟快 6 倍）
- 支持与 P2P (Prompt-to-Prompt) 结合进行图像编辑
- 颜色不会过拟合——颜色本质上是抽象属性，与 SD 的先验知识对齐

## 评分

- **新颖性**: ⭐⭐⭐⭐ — 颜色提示学习是有实际价值的新任务
- **技术深度**: ⭐⭐⭐☆ — 方法相对简洁，核心在于解耦思路和 CAA 损失
- **实验质量**: ⭐⭐⭐⭐ — 定量评估全面，含用户研究
- **实用性**: ⭐⭐⭐⭐ — 对设计、时尚等领域有直接应用价值
- **综合推荐**: ⭐⭐⭐⭐

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers](difftracker_texttoimage_diffusion_models_are_unsupervised_tr.md)
- [\[ECCV 2024\] Source Prompt Disentangled Inversion for Boosting Image Editability with Diffusion Models](source_prompt_disentangled_inversion_for_boosting_image_editability_with_diffusi.md)
- [\[ECCV 2024\] ShapeFusion: A 3D Diffusion Model for Localized Shape Editing](shapefusion_a_3d_diffusion_model_for_localized_shape_editing.md)
- [\[ECCV 2024\] Learning Differentially Private Diffusion Models via Stochastic Adversarial Distillation](learning_differentially_private_diffusion_models_via_stochastic_adversarial_dist.md)
- [\[ECCV 2024\] Unveiling Advanced Frequency Disentanglement Paradigm for Low-Light Image Enhancement](unveiling_advanced_frequency_disentanglement_paradigm_for_low-light_image_enhanc.md)

<!-- RELATED:END -->
