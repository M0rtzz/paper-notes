---
title: >-
  [论文解读] Winner of CVPR2026 NTIRE Challenge on Image Shadow Removal: Semantic and Geometric Guidance for Shadow Removal via Cascaded Refinement
description: >-
  [CVPR 2026 Workshop (NTIRE)][图像恢复][阴影去除] 基于 OmniSR 构建三级级联精炼 pipeline，结合冻结 DINOv2 语义特征与单目深度/法线几何引导，通过收缩约束损失稳定多阶段训练，在 NTIRE 2026 阴影去除挑战赛中获得第一名。
tags:
  - CVPR 2026 Workshop (NTIRE)
  - 图像恢复
  - 阴影去除
  - 级联精炼
  - 语义引导
  - 几何引导
  - 渐进式修复
---

# Winner of CVPR2026 NTIRE Challenge on Image Shadow Removal: Semantic and Geometric Guidance for Shadow Removal via Cascaded Refinement

**会议**: CVPR 2026 Workshop (NTIRE)  
**arXiv**: [2604.16177](https://arxiv.org/abs/2604.16177)  
**代码**: 无  
**领域**: 图像修复  
**关键词**: 阴影去除, 级联精炼, 语义引导, 几何引导, 渐进式修复

## 一句话总结

基于 OmniSR 构建三级级联精炼 pipeline，结合冻结 DINOv2 语义特征与单目深度/法线几何引导，通过收缩约束损失稳定多阶段训练，在 NTIRE 2026 阴影去除挑战赛中获得第一名。

## 研究背景与动机

**领域现状**：图像阴影去除是底层视觉中的重要任务，近年来方法逐步从手工光照模型演进到基于 Transformer 的端到端修复系统，如 ShadowFormer、HomoFormer、OmniSR 等，其中 OmniSR 通过结合 RGB 外观与语义和几何辅助信息取得了良好效果。

**现有痛点**：即便是强力的单阶段系统如 OmniSR，在一次前向传播后仍会残留颜色偏移、光照偏差和边界伪影。单次推理无法完全消除复杂场景中的阴影效应，特别是在纹理丰富区域和阴影边界处。

**核心矛盾**：阴影去除本质上更适合被视为渐进精炼而非一次性预测问题。单阶段方法尝试一步到位地分离光照变化和固有外观，但这在复杂场景中往往力不从心。

**本文目标**：(1) 将 OmniSR 扩展为多阶段级联精炼架构；(2) 设计稳定多阶段训练的损失函数；(3) 利用跨数据集渐进式预训练来提高泛化性。

**切入角度**：作者观察到阴影去除的后续阶段可以纠正前序预测的残余误差，类似于逆问题中的迭代修复思路。

**核心 idea**：用三阶段直接精炼级联替代单次前向传播，每个阶段接收上一阶段的输出并进一步修正残余伪影，辅以收缩约束确保误差单调递减。

## 方法详解

### 整体框架

给定一张带阴影的 RGB 图像 $\boldsymbol{x}$，系统首先从原始输入中一次性提取冻结的 DINOv2 语义特征 $S(\boldsymbol{x})$ 和基于单目深度的几何特征 $G(\boldsymbol{x})$（深度通道 + 表面法线），然后将这些辅助信号与图像一起送入三个级联的 OmniSR 阶段。第一阶段直接处理原始输入，后续阶段依次处理前一阶段的输出，最终输出 $\hat{\boldsymbol{y}}^{(3)}$ 作为去阴影结果。

### 关键设计

1. **语义与几何引导复用机制**:

    - 功能：为修复网络提供场景级别的语义理解和空间结构约束
    - 核心思路：使用冻结 DINOv2 ViT-L/14 提取四层中间特征图，投影后在瓶颈层融合，并在 1/4 和 1/8 分辨率的深层 Transformer 块中注入。深度使用 Depth Anything V2 估计，归一化后与 RGB 拼接形成 RGB-D 输入，同时将深度衍生的点云图和法线注入深层块
    - 设计动机：语义特征帮助区分投射阴影与固有暗色材质，几何特征防止外观修正跨越不一致的场景区域传播。一次计算、所有阶段复用，避免重复推理

2. **收缩约束多阶段监督**:

    - 功能：确保级联各阶段的重建误差单调递减
    - 核心思路：定义阶段误差 $d_k = \|\hat{\boldsymbol{y}}^{(k)} - \boldsymbol{y}^*\|_2$，收缩损失 $\mathcal{L}_{\text{contraction}} = \sum_{k=2}^{K} [d_k - \text{sg}(d_{k-1})]_+$，其中 $\text{sg}$ 为 stop-gradient 算子。只惩罚误差增大的情况，不强制固定衰减速率
    - 设计动机：多阶段训练容易不稳定，后阶段可能反而恶化结果。收缩约束让前一阶段的误差作为固定参考，仅约束当前阶段不能比前一阶段更差

3. **跨数据集渐进式预训练策略**:

    - 功能：从不完美对齐数据中学习鲁棒先验，再逐步适配到精确对齐数据
    - 核心思路：Phase 1 在 WSRD（近似对齐）上训练 500 epochs 单阶段模型；Phase 2 迁移到 WSRD+（精确对齐）扩展为两阶段训练 1500 epochs；Phase 3 再扩展为三阶段并在 WSRD+ 2026 上做 100 epochs 微调，最终用 5 个 checkpoint 做预测平均
    - 设计动机：不完美对齐的数据反而提供了鲁棒性训练信号，模型学会对空间偏移和边界不精确性的容忍

### 损失函数 / 训练策略

总损失包含五项：MSE 重建损失 + LPIPS 感知损失（主项）+ Hessian 结构一致性 + 阶段监督损失（中间输出直接监督）+ 收缩损失。使用 AdamW 优化器，余弦退火学习率调度，最终用 5 个时间点 checkpoint 的预测均值作为集成输出。

## 实验关键数据

### 主实验

| 数据集 | 指标 | 本文 | 第二名(RAS) | 第三名(SNU-ISPL-B) |
|--------|------|------|------------|-------------------|
| WSRD+ 2026 Test | PSNR↑ | **26.68** | 26.14 | 25.94 |
| WSRD+ 2026 Test | SSIM↑ | **0.874** | 0.866 | 0.867 |
| WSRD+ 2026 Test | LPIPS↓ | **0.058** | 0.071 | 0.085 |
| WSRD+ 2026 Test | FID↓ | **26.14** | 30.47 | 28.05 |

### 消融实验

| 配置 | PSNR | SSIM | LPIPS |
|------|------|------|-------|
| 1 stage | 27.077 | 0.873 | 0.0605 |
| 2 stages | 27.274 | 0.877 | 0.0599 |
| 3 stages (Full) | **27.356** | 0.877 | 0.0631 |
| w/o 收缩损失 | 27.173 | 0.877 | 0.0608 |
| w/o DINOv2 引导 | 25.859 | 0.871 | 0.0711 |
| w/o 深度+法线 | 27.105 | 0.876 | 0.0634 |

### 关键发现

- DINOv2 语义引导是最重要的组件，去除后 PSNR 下降 1.5 dB
- 三阶段是最佳配置，进一步增加阶段数收益递减甚至恶化 LPIPS
- 收缩损失主要起稳定化正则作用，去除后 PSNR 下降但 LPIPS 略有改善，说明它倾向于保真度而非感知锐度

## 亮点与洞察

- 将阴影去除建模为迭代精炼而非一次性预测，这种视角与逆问题求解中的 plug-and-play 思路一脉相承。收缩约束损失的设计特别优雅——只惩罚"变差"而不强制"变好的速度"
- 不完美对齐数据的"优势"利用思路很有启发：通常被视为噪声的空间错位反而可以作为数据增强的一种形式，增强模型的鲁棒性
- 74.3M 参数量在竞赛方案中属于轻量级（第二名 RAS 用了 1500M，第四名 APRIL-AIGC 用了 9105M），说明精巧的设计可以弥补规模差距

## 局限与展望

- 作为竞赛方案，高度针对 WSRD+ 数据集优化，对 in-the-wild 阴影的泛化性存疑
- 三阶段推理增加了约 3 倍计算量，实时应用受限
- 集成策略（5 个 checkpoint 平均）进一步增加了推理成本
- 改进方向：可探索自适应级联深度（简单阴影用少阶段、复杂阴影用多阶段）以提升效率

## 相关工作与启发

- **vs OmniSR（单阶段）**: 本文直接基于 OmniSR 扩展为三阶段，证明了多阶段精炼在阴影去除中的有效性
- **vs 扩散模型方案（RAS/APRIL-AIGC）**: 竞赛中的二三名使用了大型扩散模型作为去阴影的第一阶段，本文方案则完全基于修复架构，参数量小一到两个数量级但性能更优

## 评分

- 新颖性: ⭐⭐⭐ 方法组合已有组件为主，创新在于系统性工程设计
- 实验充分度: ⭐⭐⭐⭐ 有竞赛排名验证，消融全面
- 写作质量: ⭐⭐⭐⭐ 结构清晰，实验描述详尽
- 价值: ⭐⭐⭐⭐ 提供了阴影去除领域多阶段精炼的最佳实践参考

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2025\] Detail-Preserving Latent Diffusion for Stable Shadow Removal](../../CVPR2025/image_restoration/detail-preserving_latent_diffusion_for_stable_shadow_removal.md)
- [\[CVPR 2026\] NTIRE 2026 The Second Challenge on Day and Night Raindrop Removal for Dual-Focused Images](ntire_2026_raindrop_removal_challenge.md)
- [\[CVPR 2026\] NTIRE 2026 The 3rd RAIM Challenge: AI Flash Portrait (Track 3)](ntire_2026_ai_flash_portrait_challenge.md)
- [\[CVPR 2026\] Flickerformer: A Duet of Periodicity and Directionality for Burst Flicker Removal](it_takes_two_a_duet_of_periodicity_and_directionality_for_burst_flicker_removal.md)
- [\[ICLR 2026\] Mechanism of Task-oriented Information Removal in In-context Learning](../../ICLR2026/image_restoration/mechanism_of_task-oriented_information_removal_in_in-context_learning.md)

<!-- RELATED:END -->
