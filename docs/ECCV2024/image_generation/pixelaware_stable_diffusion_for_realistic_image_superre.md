---
title: >-
  [论文解读] Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization
description: >-
  [ECCV 2024][图像生成][扩散模型] 提出像素感知稳定扩散（PASD）网络，通过像素感知交叉注意力（PACA）在潜空间中实现像素级结构保持，配合退化移除模块和可调噪声调度，统一解决真实图像超分辨率和个性化风格迁移两大任务。
tags:
  - ECCV 2024
  - 图像生成
  - 扩散模型
  - 真实图像超分辨率
  - 像素感知
  - 图像风格化
  - ControlNet
---

# Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization

**会议**: ECCV 2024  
**arXiv**: [2308.14469](https://arxiv.org/abs/2308.14469)  
**代码**: https://github.com/yangxy/PASD/  
**领域**: LLM/NLP  
**关键词**: 扩散模型, 真实图像超分辨率, 像素感知, 图像风格化, ControlNet

## 一句话总结

提出像素感知稳定扩散（PASD）网络，通过像素感知交叉注意力（PACA）在潜空间中实现像素级结构保持，配合退化移除模块和可调噪声调度，统一解决真实图像超分辨率和个性化风格迁移两大任务。

## 研究背景与动机

- **Real-ISR 的核心挑战**：如何在保持像素级结构忠实度的同时生成感知真实的细节
- **现有方案不足**：
    - GAN 方法：容易产生不自然伪影，生成细节有限
    - ControlNet：适合边缘/分割等语义级条件，但**无法实现像素级控制**（输出与输入结构不一致）
    - DiffBIR/StableSR：使用 VAE 编解码器的跳跃连接传递细节，但需要在图像空间额外训练，限制了在潜空间任务（如风格化）的应用
- **本文目标**：在潜空间内实现像素级感知，无需跳跃连接

## 方法详解

### 整体框架

PASD = 预训练 Stable Diffusion（冻结）+ 退化移除模块 + ControlNet + PACA（像素感知交叉注意力）+ ANS（可调噪声调度）+ 高层信息提取

### 关键设计

**1. 像素感知交叉注意力（PACA）** ⭐核心贡献
- 问题：ControlNet 的零卷积连接（简单相加）无法传递像素级精确信息
- PACA 方案：将 UNet 特征 x 和 ControlNet 特征 y reshape 后，以 y 作为 context 进行交叉注意力
  $PACA(Q,K,V) = Softmax(\frac{QK^T}{\sqrt{d}}) \cdot V$
  其中 Q=to_q(x'), K=to_k(y'), V=to_v(y')
- 由于 y' 未经 VAE Encoder 转换，保留了原始图像结构
- 长度 h×w = 潜在特征的所有像素位置 → 实现像素级控制

**2. 退化移除模块**
- 金字塔网络提取 1/2, 1/4, 1/8 多尺度特征
- 中间监督：每个尺度都有 toRGB 层重建 HQ 图像，L1 损失强制逼近 GT
- 目的：提取"干净"特征，减轻扩散模块处理退化图像的负担

**3. 可调噪声调度（ANS）**
- 背景：SD 的训练噪声调度在终端时间步仍有残留信号（非零 SNR），导致训练-测试不一致
- 解决方案：在初始噪声中混入 LQ 图像潜在表示作为信号补偿
  $z_N = \sqrt{\bar{\alpha}_a \bar{\alpha}_N} z_{LR} + \sqrt{1 - \bar{\alpha}_a \bar{\alpha}_N} z''$
- 通过 $\bar{\alpha}_a \in [0,1]$ 控制残留信号强度，提供感知-保真度的灵活权衡

**4. 高层信息提取**
- 使用 ResNet（分类）+ YOLO（检测）+ BLIP（描述）提取 LQ 图像的语义信息
- CLIP 编码器转换为特征，作为扩散过程的额外语义控制
- 负提示词："noisy", "blurry", "low resolution" 用于 classifier-free guidance

### 损失函数 / 训练策略

- 扩散损失：$\mathcal{L}_{DF-\epsilon}$（标准 ε-prediction L2 损失）
- 退化移除损失：$\mathcal{L}_{DR}$（多尺度 L1 重建损失）
- 总损失：$\mathcal{L} = \mathcal{L}_{DF-\epsilon} + \gamma \mathcal{L}_{DR}$，γ=1
- 冻结所有 SD 参数，仅训练新增模块
- 50% 概率用 null-text 替代文本提示
- 训练 500K 迭代，8× V100，lr=5e-5

## 实验关键数据

### 主实验（Real-ISR 定量评估）

| 方法 | DIV2K FID↓ | DISTS↓ | QAlign↑ | RealSR FID↓ | DRealSR FID↓ |
|------|-----------|--------|---------|-------------|-------------|
| RealESRGAN | 68.65 | 0.2092 | 4.246 | 67.02 | 23.18 |
| StableSR | 50.94 | 0.2191 | 3.650 | 109.11 | 17.68 |
| DiffBIR | 57.72 | 0.1785 | 4.310 | 55.17 | 16.82 |
| SeeSR | 47.33 | 0.1959 | 4.315 | 58.32 | 16.22 |
| **PASD** | **50.78** | **0.1778** | **4.318** | **47.34** | **14.20** |

### 风格化实验

- 用户研究中 PASD 在 Real-ISR、卡通化、旧照片修复三任务上均获得最高偏好率
- 仅替换基础模型即可实现不同风格输出，无需收集配对训练数据

### 关键发现

- PACA 有效解决了 ControlNet 的结构不一致问题（Fig.1 对比）
- PASD 在 DRealSR 上 FID 14.20，显著领先第二名 SeeSR 的 16.22
- ANS 提供了灵活的感知-保真度权衡：$\bar{\alpha}_a$ 越小 → 越多随机性 → 感知质量更高但保真度更低
- 高层信息（分类+检测+描述）的联合使用比 null-text 明显更好
- 替换基础模型即可做风格化是强大的工程优势

## 亮点与洞察

1. **PACA 的优雅设计**：在潜空间实现像素级控制，避免了跳跃连接的额外图像空间训练限制
2. **退化移除+扩散的解耦**思路清晰：前者专注恢复"干净"结构，后者专注生成真实细节
3. **通用性强**：同一模型支持超分辨率、卡通化、旧照片修复，仅需切换基础模型
4. ANS 提供了可控的质量调节手段，适合不同应用需求

## 局限性 / 可改进方向

- 推理速度受限于扩散采样步数（通常 20-50 步）
- PACA 的 h×w 长度交叉注意力在高分辨率时计算量较大
- 风格化结果的质量取决于社区共享的个性化模型
- 对极度退化的输入（如极低分辨率、严重压缩）仍可能出现内容偏差

## 相关工作与启发

- ControlNet 提供了条件控制框架基础，PACA 在其上实现了像素级增强
- DiffBIR/StableSR 的跳跃连接启发了寻找更灵活替代方案的需求
- 可启发：PACA 可推广到视频超分辨率、医学图像增强等需要严格结构保持的任务

## 评分

- 新颖性：⭐⭐⭐⭐（PACA + ANS + 统一框架）
- 技术深度：⭐⭐⭐⭐
- 实验充分度：⭐⭐⭐⭐⭐（超分+风格化+旧照片+用户研究）
- 写作质量：⭐⭐⭐⭐
- 综合推荐：⭐⭐⭐⭐

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] XPSR: Cross-modal Priors for Diffusion-based Image Super-Resolution](xpsr_crossmodal_priors_for_diffusionbased_image_superresolut.md)
- [\[ECCV 2024\] OmniSSR: Zero-shot Omnidirectional Image Super-Resolution using Stable Diffusion Model](omnissr_zero-shot_omnidirectional_image_super-resolution_using_stable_diffusion_.md)
- [\[ECCV 2024\] You Only Need One Step: Fast Super-Resolution with Stable Diffusion via Scale Distillation](you_only_need_one_step_fast_super-resolution_with_stable_diffusion_via_scale_dis.md)
- [\[ECCV 2024\] AdaDiffSR: Adaptive Region-Aware Dynamic Acceleration Diffusion Model for Real-World Image Super-Resolution](adadiffsr_adaptive_region-aware_dynamic_acceleration_diffusion_model_for_real-wo.md)
- [\[ECCV 2024\] DCDM: Diffusion-Conditioned-Diffusion Model for Scene Text Image Super-Resolution](dcdm_diffusion-conditioned-diffusion_model_for_scene_text_image_super-resolution.md)

<!-- RELATED:END -->
