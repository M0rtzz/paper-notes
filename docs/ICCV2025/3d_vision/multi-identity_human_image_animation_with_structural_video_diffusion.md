---
description: "【论文笔记】Multi-identity Human Image Animation with Structural Video Diffusion 论文解读 | ICCV 2025 | arXiv 2504.04126 | 人体视频生成 | 提出Structural Video Diffusion,通过身份特定嵌入和RGB-深度-法线联合学习,首次实现多身份人体视频生成中的外观一致性保持和3D感知的人-物交互建模。"
tags:
  - ICCV 2025
---

# Multi-identity Human Image Animation with Structural Video Diffusion

**会议**: ICCV 2025  
**arXiv**: [2504.04126](https://arxiv.org/abs/2504.04126)  
**代码**: [GitHub](https://github.com/)  
**领域**: 3D视觉  
**关键词**: 人体视频生成, 多身份, 视频扩散, 深度/法线, 人-物交互

## 一句话总结

提出Structural Video Diffusion,通过身份特定嵌入和RGB-深度-法线联合学习,首次实现多身份人体视频生成中的外观一致性保持和3D感知的人-物交互建模。

## 研究背景与动机

人体图像动画在影视、游戏等领域应用广泛。现有方法(Animate Anyone, MagicAnimate等)在**单人场景**表现良好,但在多身份场景下严重失效:

1. **外观一致性丧失** — 无法将正确的人物外观与对应姿态关联
2. **人-物交互建模差** — 物体模糊、漂浮或消失
3. **缺乏3D空间关系** — 没有机制理解遮挡和相对距离

根本原因:缺乏细粒度身份控制和3D空间关系建模机制。

## 方法详解

### ID-Specific Embedding

引入 $N$ 个可学习ID嵌入 $\mathbf{E}_{query} \in \mathbb{R}^{N \times C}$,类似DETR的检测token。

对每帧 $f$,将跟踪掩码 $\mathbf{M}^f$ 转换为空间ID嵌入图 $\mathbf{E}^f \in \mathbb{R}^{H \times W \times C}$:将第n个人对应的空间位置填充第n行嵌入。

通过零初始化卷积以ControlNet方式注入:$\widetilde{\mathbf{x}}_t = \mathbf{x}_t + \text{zero\_conv}(\mathbf{E})$

### 潜在结构视频扩散

联合预测RGB、深度和表面法线:

**多模态去噪UNet**: 复制conv_in/conv_out和首/末层,中间层共享
**多模态参考UNet**: 同样复制初始下采样层处理参考图像的三模态

训练目标:
$$\mathcal{L}(\boldsymbol{\theta}) = \mathbb{E}\left[\|\mathbf{v}_{\mathbf{x}^t_{rgb}} - \widehat{\mathbf{v}}_{\theta,rgb}\|_2^2 + \|\mathbf{v}_{\mathbf{x}^t_{depth}} - \widehat{\mathbf{v}}_{\theta,depth}\|_2^2 + \|\mathbf{v}_{\mathbf{x}^t_{normal}} - \widehat{\mathbf{v}}_{\theta,normal}\|_2^2\right]$$

法线监督仅限人体掩码内(Sapiens法线估计器仅在人体上有效)。

### 数据集:Multi-HumanVid

扩展HumanVid,新增25K视频,包含丰富的多人和人-物交互场景。标注包括:
- 相机参数(TRAM估计)
- 人体姿态(ViTPose)
- 深度(DepthCrafter)
- 表面法线(Sapiens)
- 跟踪掩码(Grounding-DINO + SAM2)

## 实验

### 与SOTA方法对比(多身份测试集)

| 方法 | SSIM↑ | PSNR↑ | LPIPS↓ | FVD↓ | FID↓ |
|------|-------|-------|--------|------|------|
| MimicMotion | 0.628 | 19.878 | 0.258 | 1042.6 | 59.11 |
| CamAnimate | 0.649 | 19.552 | 0.265 | 982.1 | 54.09 |
| **Ours** | **0.691** | **20.685** | **0.233** | **878.2** | **30.57** |

### 消融实验

| 方法 | SSIM↑ | PSNR↑ | FID↓ |
|------|-------|-------|------|
| Baseline | 0.649 | 19.552 | 54.09 |
| + ID-embedding | 0.686 | 20.374 | 33.75 |
| + Multi-modality | 0.668 | 20.139 | 47.67 |
| + Both | **0.691** | **20.685** | **30.57** |

### 模态消融

| 模态 | SSIM↑ | PSNR↑ | FID↓ |
|------|-------|-------|------|
| RGB-only | 0.686 | 20.374 | 33.75 |
| + Depth | **0.691** | **20.685** | **30.57** |
| + Normal | 0.639 | 19.037 | 60.58 |
| + Depth&Normal | 0.643 | 19.664 | 56.78 |

### 关键发现

1. ID嵌入和结构学习各自贡献显著,结合后FID从54降到31
2. **深度比法线贡献更大** — 法线估计质量不足反而引入噪声
3. 用户研究中91.25%偏好本方法
4. 支持跨身份运动迁移应用

## 亮点与洞察

1. **首次多身份人体交互视频生成** — 开创性工作
2. **几何信息作为输出而非输入** — 避免了帧级深度/法线标注的不现实需求
3. **ID嵌入的DETR式设计** — 优雅地解决了多人外观-姿态关联问题
4. **深度/法线提供隐式3D感知** — 无需显式3D建模

## 局限性

- 受限于SD1.5基础模型,视觉质量有限
- 法线估计质量不足限制了法线模态的贡献
- 计算资源限制未在更大模型(HunyuanVideo)上验证

## 相关工作

- **单人动画**: Animate Anyone, MagicAnimate, Champ, CamAnimate
- **视频扩散**: AnimateDiff, SVD
- **数据集**: HumanVid, TikTok, BEDLAM

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ (多身份+结构化视频扩散的首创)
- 技术深度: ⭐⭐⭐⭐ (ID嵌入+多模态分支设计合理)
- 实验充分度: ⭐⭐⭐⭐ (消融充分,用户研究完整)
- 实用价值: ⭐⭐⭐⭐ (多人视频生成需求旺盛)
