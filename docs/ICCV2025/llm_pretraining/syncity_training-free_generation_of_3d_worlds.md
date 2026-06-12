---
title: >-
  [论文解读] SynCity: Training-Free Generation of 3D Worlds
description: >-
  [ICCV 2025][预训练][3D世界生成] SynCity 提出了一种无需训练/优化的方法，通过精心设计的 prompt engineering 策略组合预训练的语言模型、2D图像生成器和3D生成器（TRELLIS），以 tile-by-tile 的方式自回归生成大规模、高质量、可自由导航的3D世界。
tags:
  - "ICCV 2025"
  - "预训练"
  - "3D世界生成"
  - "训练免微调"
  - "Tile-based生成"
  - "3D Gaussian Splatting"
  - "提示学习"
---

# SynCity: Training-Free Generation of 3D Worlds

**会议**: ICCV 2025  
**arXiv**: [2503.16420](https://arxiv.org/abs/2503.16420)  
**代码**: 无  
**领域**: 3D场景生成 / 模型压缩  
**关键词**: 3D世界生成, 训练免微调, Tile-based生成, 3D Gaussian Splatting, Prompt Engineering

## 一句话总结

SynCity 提出了一种无需训练/优化的方法，通过精心设计的 prompt engineering 策略组合预训练的语言模型、2D图像生成器和3D生成器（TRELLIS），以 tile-by-tile 的方式自回归生成大规模、高质量、可自由导航的3D世界。

## 研究背景与动机

- **3D世界生成的需求**：视频游戏、VR、特效和仿真等场景需要大量3D内容，手工创建成本极高，自动化生成可显著降低负担。
- **现有方法的局限**：
    - **基于图像的方法**（如 DreamFusion、Text2Room）：依赖2D图像生成器逐步重建场景，但难以在大场景中保持一致的3D结构，通常只能生成"3D气泡"（bubble），无法自由行走。
    - **3D生成方法**（如 BlockDiffusion、LT3SD）：直接生成3D表示，可保证几何一致性，但受限于3D训练数据，生成质量和多样性不足，且无法利用2D生成器的艺术表现力。
    - **程序化方法**：领域特定且单调（如地形、城市布局）。
- **核心动机**：结合3D生成器的几何精度与2D图像生成器的艺术表现力，实现大规模、高质量的3D世界生成，且无需重新训练任何模型。

## 方法详解

### 整体框架

SynCity 将3D世界结构化为 $W \times H$ 的网格（grid），每个 tile 代表场景的一个局部区域。世界以 tile-by-tile 的方式逐步生成，每个新 tile 在已有场景上下文中生成并融合。整体流程包括四个步骤：语言提示扩展 → 2D图像生成 → 3D重建 → 3D融合。

### 关键设计

1. **语言模型提示（LLM Prompting）**：
    - 将高层文本描述 $p_0$ 通过 ChatGPT o3-mini-high 扩展为每个 tile 的具体文本提示 $p_{xy}$ 和全局风格提示 $p_\star$。
    - 设计动机：LLM 可理解复杂场景描述，自动分配每个 tile 的内容（如建筑、桥梁、树木），实现细粒度控制。

2. **2D图像生成器提示（2D Generator Prompting）**：
    - 使用 Flux ControlNet 作为2D inpainter，为每个 tile 生成等轴测（isometric）视角的2D图像。
    - **关键技巧**：通过构造 base image $B$（灰色方形底座的等轴测视图）和 inpainting mask $M$（底座上方的立方体区域）来"框定"生成结果，确保视角稳定且适合后续3D重建。
    - **上下文感知**：对于非首个 tile，将已生成的3D世界渲染为上下文图像，并修改 mask 避免覆盖已有 tile，从而保证相邻 tile 之间的外观一致性。
    - **高遮挡处理**：渲染时裁剪可能遮挡新 tile 的高大结构，确保地面连续性。

3. **3D生成器提示与后处理（3D Generator Prompting）**：
    - 使用 TRELLIS（image-to-3D生成器）将2D tile 图像重建为3D Gaussian Splats。
    - **前景提取与 Rebasing**：从生成的2D图像中提取新 tile 区域（使用 rembg + alpha matting），然后在底部添加一个略大的灰色底座（rebasing），为3D生成器提供"框架"，确保生成的 tile 具有规则的方形底面。
    - **几何验证**：通过启发式方法验证3D重建质量，检查 tile 的几何占据区域是否为正方形、底面是否完整，若不满足则重新生成。
    - **后处理**：裁剪底座、重缩放至单位大小、重定向以匹配2D图像提示。

4. **3D融合（3D Blending）**：
    - 直接拼接 tile 时，边界可能不匹配（TRELLIS 重建不精确 + 单视角限制）。
    - **2D融合**：将两个相邻 tile 并排放置，渲染前视图，然后用 Flux 对中间区域 inpainting，生成平滑过渡的图像。
    - **3D潜在空间融合**：在 TRELLIS 的潜在空间中，将两个 tile 的 latent 拼接，对中间区域重新去噪，仅在第二阶段（higher resolution, $R=64$）进行，保持其余区域固定。
    - **潜在空间上采样**：裁剪底座后 latent 分辨率不一致，提出新的上采样方案：先上采样占据体积，然后用多视角条件去噪重建纹理细节（优于简单插值）。

### 损失函数 / 训练策略

本方法为 **training-free**（无需训练），所有组件均使用预训练模型：
- 语言模型：ChatGPT o3-mini-high
- 2D生成器：Flux ControlNet Inpainting
- 3D生成器：TRELLIS
- 核心创新在于 prompt engineering 和后处理策略的设计。

## 实验关键数据

### 主实验 (表格)

| 评价维度 | SynCity Win Rate (%) |
|:---|:---:|
| Overall | 90.9 |
| Geometry | 81.8 |
| Exploration | 90.9 |
| Diversity | 90.9 |
| Realism | 86.4 |

*与 BlockFusion 的人类偏好对比（n=22），SynCity 在所有维度上均大幅领先。*

### 消融实验 (表格)

| 消融项 | Base Area | Squareness ↑ | Completeness ↑ |
|:---|:---:|:---:|:---:|
| No Rebasing | 2271 | 0.92 | 0.73 |
| Ours (with Rebasing) | 4096 | 1.00 | 1.00 |

*Rebasing 对 tile 几何质量至关重要：确保底面完全正方形且边界完整。*

| 上采样方法 | LPIPS ↓ | SSIM ↑ | FID ↓ | KID ↓ |
|:---|:---:|:---:|:---:|:---:|
| Naive upsampling | 0.5914 | 0.3093 | 200.5 | 0.243 |
| Ours (single frame) | 0.3517 | 0.5149 | 111.6 | 0.069 |
| Ours (multi frame) | 0.3212 | 0.5312 | 89.1 | 0.051 |

*提出的多帧条件潜在空间上采样方案在所有感知指标上显著优于朴素插值。*

### 关键发现

- **2D上下文至关重要**：移除邻居 tile 上下文后，各 tile 独立采样，物体相对尺度不一致（如建筑大小差异明显）。
- **Rebasing 必不可少**：无 rebasing 时 TRELLIS 生成的 tile 底面不规则、边界不完整，导致拼接困难。
- **3D Blending 消除边界伪影**：不做3D融合时 tile 之间存在明显的不连续性。
- **直接生成大场景不可行**：用 Flux 生成整个大场景图像再交给 TRELLIS 重建，无论精确还是抽象的 prompt 都无法有效控制布局。

## 亮点与洞察

- **完全 training-free**：仅通过精巧的 prompt engineering 和后处理组合多个预训练模型，无需任何微调或优化。这体现了"如何更好地使用现有模型"的研究思路。
- **Tile-based 世界构建**：借鉴游戏设计中的等轴测 tile 思想，将复杂的大规模场景生成分解为可控的局部生成问题。
- **3D潜在空间融合**：在 TRELLIS 的潜在空间中进行 inpainting，相比纯2D融合更能保证3D一致性。
- **可自由导航**：生成的世界足够大且3D一致，可进行非平凡的导航轨迹探索，不像其他方法限于"3D气泡"。

## 局限与展望

- **Tile 结构较为刚性**：固定的网格划分限制了布局灵活性，未来可考虑随机平移/缩放 tile。
- **依赖 TRELLIS 的重建精度**：TRELLIS 不能精确重建输入图像，且单视角输入对背面控制有限。
- **缺乏定量评价**：主要依赖人类偏好实验（n=22，规模较小），缺少自动化的大规模定量评价。
- **可扩展性未充分验证**：论文主要展示中小规模网格（如 3×3），是否能扩展到非常大的世界仍需验证。
- **如有3D场景级训练数据**：微调部分组件可能进一步提升质量并简化对齐/rebasing步骤。

## 相关工作与启发

- **与 BlockFusion 的对比**：BlockFusion 直接学习3D扩散模型生成 mesh block，但需领域特定3D数据且只能生成无纹理 mesh。SynCity 通过2D生成器弥补了这一不足。
- **与 WonderWorld / LucidDreamer 的区别**：这些方法基于图像外推，难以保持大范围3D一致性。SynCity 利用3D生成器天然约束几何。
- **启发**：Prompt engineering 在组合多个预训练模型时的巨大潜力；等轴测视角作为2D→3D转换的有效中间表示。

## 评分

- **新颖性**: ⭐⭐⭐⭐ 首次将 object-level 3D生成器用于场景生成，tile-based 框架和融合策略设计新颖
- **实验充分度**: ⭐⭐⭐ 消融实验充分，但定量评价较少，人类评价规模有限
- **写作质量**: ⭐⭐⭐⭐ 论文结构清晰，方法描述详细，图示直观
- **价值**: ⭐⭐⭐⭐ training-free 大规模3D世界生成具有很高的实用价值和启发意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[NeurIPS 2025\] Through the River: Understanding the Benefit of Schedule-Free Methods for Language Model Training](../../NeurIPS2025/llm_pretraining/through_the_river_understanding_the_benefit_of_schedule-free_methods_for_languag.md)
- [\[NeurIPS 2025\] Deep Compositional Phase Diffusion for Long Motion Sequence Generation](../../NeurIPS2025/llm_pretraining/deep_compositional_phase_diffusion_for_long_motion_sequence_generation.md)
- [\[CVPR 2025\] ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model](../../CVPR2025/llm_pretraining/scamo_exploring_the_scaling_law_in_autoregressive_motion_generation_model.md)
- [\[CVPR 2025\] Seeing What Matters: Empowering CLIP with Patch Generation-to-Selection](../../CVPR2025/llm_pretraining/seeing_what_matters_empowering_clip_with_patch_generation-to-selection.md)
- [\[CVPR 2025\] Improving Autoregressive Visual Generation with Cluster-Oriented Token Prediction](../../CVPR2025/llm_pretraining/improving_autoregressive_visual_generation_with_cluster-oriented_token_predictio.md)

</div>

<!-- RELATED:END -->
