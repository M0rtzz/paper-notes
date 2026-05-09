---
title: >-
  [论文解读] FinPercep-RM: A Fine-grained Reward Model and Co-evolutionary Curriculum for RL-based Real-world Super-Resolution
description: >-
  [CVPR 2026][图像恢复][强化学习超分辨率] 提出 FinPercep-RM 细粒度感知奖励模型，通过预测全局质量分数和感知退化图来空间定位缺陷，配合协同进化课程学习策略平衡训练稳定性和奖励鲁棒性，有效抑制 RL-based 真实世界超分辨率中的奖励黑客问题。
tags:
  - CVPR 2026
  - 图像恢复
  - 图像复原
  - 奖励模型
  - 细粒度感知
  - 奖励黑客
  - 课程学习
---

# FinPercep-RM: A Fine-grained Reward Model and Co-evolutionary Curriculum for RL-based Real-world Super-Resolution

**会议**: CVPR 2026  
**arXiv**: [2512.22647](https://arxiv.org/abs/2512.22647)  
**代码**: [https://github.com/lyd-2022/FinPercep-RM](https://github.com/lyd-2022/FinPercep-RM)  
**领域**: 图像修复 / 超分辨率  
**关键词**: 强化学习超分辨率, 奖励模型, 细粒度感知, 奖励黑客, 课程学习

## 一句话总结

提出 FinPercep-RM 细粒度感知奖励模型，通过预测全局质量分数和感知退化图来空间定位缺陷，配合协同进化课程学习策略平衡训练稳定性和奖励鲁棒性，有效抑制 RL-based 真实世界超分辨率中的奖励黑客问题。

## 研究背景与动机

1. **领域现状**：基于扩散模型的 Real-ISR 方法利用强大的生成先验合成丰富纹理，RLHF 被用于进一步优化感知质量。
2. **现有痛点**：典型 IQA 模型（CLIP-IQA、MANIQA）仅输出全局分数，对局部细粒度失真不敏感——微妙伪影获得虚假高奖励（奖励黑客），生成结果出现局部伪影和不真实的"绘画感"外观。
3. **核心矛盾**：简单全局 IQA 奖励稳定但收敛到次优解（黑客），FinPercep-RM 鲁棒但空间复杂的奖励信号导致策略学习不稳定——稳定性与鲁棒性的两难。
4. **本文目标**：设计既能诊断"哪里有缺陷"又能评估"质量多好"的奖励模型，并解决训练不稳定问题。
5. **切入角度**：编码器-解码器架构同时输出全局分数和退化热图，课程学习渐进引入复杂奖励。
6. **核心 idea**：将全局分数与退化图耦合——全局分数通过退化图调制计算，使其对局部缺陷天然敏感。

## 方法详解

### 整体框架

生成器产出超分图像 → FinPercep-RM 评估（全局分数 + 退化图） → 奖励信号引导生成器策略更新。CCL 机制控制奖励模型从简单到复杂渐进演化。

### 关键设计

1. **FinPercep-RM 编码器-解码器架构**:

    - 功能：同时预测全局质量分数和空间退化图
    - 核心思路：编码器（IQA 骨干如 CLIP-IQA）提取多尺度特征 $\{f_i\}_{i=1}^N$，解码器通过上采样和跨层融合重建感知退化图 $M_{\text{fg-pdm}} \in [0,1]$。全局分数通过退化图调制最深层特征计算：$S_{\text{fgc-global}} = \text{MLP}(f_N \odot \text{interpolate}(M_{\text{fg-pdm}}))$。
    - 设计动机：将全局分数和退化图耦合确保分数对局部缺陷敏感。退化图使奖励具有空间诊断能力。

2. **FGR-30k 数据集**:

    - 功能：提供训练 FinPercep-RM 的细粒度退化标注
    - 核心思路：收集多个 Real-ISR 模型的输出 $I_{SR}$，通过区域交换策略在 $I_{GT}$ 和 $I_{SR}$ 之间"植入"局部缺陷。使用随机掩码和 SAM 语义掩码。退化图 GT 由像素级 L1 差异和 DINOv3 特征级余弦距离融合生成：$M_{gt} = \text{Normalize}(\alpha \cdot \text{Diff}_{\text{pixel}} + (1-\alpha) \cdot \text{Diff}_{\text{feat}})$。
    - 设计动机：现有 IQA 数据集缺乏空间退化标注。合成样本包含真实 SR 模型产生的伪影，确保训练信号与实际应用场景一致。

3. **协同进化课程学习（CCL）**:

    - 功能：平衡训练稳定性和奖励鲁棒性
    - 核心思路：双路协同演化：(1) 奖励模型渐进扩展——从简单全局 IQA 模型 $RM_0$ 开始，逐步引入解码器参数，演化为完整 FinPercep-RM $RM_N$；(2) 生成器课程协同——初始用全局奖励稳定收敛，渐进过渡到更严格的 FinPercep-RM 版本。
    - 设计动机：直接使用完整 FinPercep-RM 导致策略梯度振荡和收敛失败。由易到难设计确保早期稳定收敛，后期精细优化。

### 损失函数 / 训练策略

FinPercep-RM 训练：$\mathcal{L}_{total} = \lambda_{map} \mathcal{L}_{map} + \lambda_{rank} \mathcal{L}_{rank} + \lambda_{align} \mathcal{L}_{align}$。其中热图损失（L1）、三元组排序损失（hinge）和锚点对齐损失（防止分数漂移）。

## 实验关键数据

### 主实验

| 数据集/方法 | LPIPS↓ | MUSIQ↑ | MANIQA↑ | ClipIQA↑ |
|------------|--------|--------|---------|----------|
| SUPIR baseline | 0.452 | 65.67 | 0.629 | 0.572 |
| SUPIR w/ IQA | 0.465 | 64.89 | 0.612 | 0.589 |
| SUPIR w/ Ours | 0.428 | 67.23 | 0.648 | 0.586 |

### 消融实验

| 配置 | 效果 | 说明 |
|------|------|------|
| 标准 IQA 奖励 | 收敛快但黑客 | 全局指标高但局部伪影明显 |
| FinPercep-RM 无 CCL | 不稳定振荡 | 鲁棒但无法收敛 |
| FinPercep-RM + CCL | 稳定最优收敛 | 两者兼得 |

### 关键发现

- 标准 IQA 奖励导致明显的奖励黑客现象——全局分数上升但视觉质量下降
- FinPercep-RM 的用户研究与人类判断高度一致
- CCL 是关键——无 CCL 的 FinPercep-RM 训练曲线严重振荡

## 亮点与洞察

- **诊断式奖励模型**：不仅评估"多好"还诊断"哪里差"，是 RLHF 在 ISR 中的重要突破
- **全局-局部耦合设计**：通过退化图调制全局分数，优雅地解决了单纯全局评分的盲区
- **数据构建巧妙**：区域交换 + 双层差异融合的合成策略简洁有效

## 局限与展望

- 缓存内容仅包含部分实验结果，完整消融可能更丰富
- 编码器-解码器增加推理开销，可能不适合实时应用
- CCL 的阶段划分和过渡时机需要手动调优
- FGR-30k 数据集的合成策略可能无法覆盖所有类型的伪影
- 未来可探索将诊断式奖励模型推广到视频超分等任务

## 相关工作与启发

- **vs 直接 IQA 奖励**: IQA 仅全局评分导致奖励黑客，FinPercep-RM 具备空间诊断
- **vs 大规模 IQA 模型**: 大规模 IQA（如 Q-Align）有一定细粒度感知但计算成本不适合迭代训练

## 评分

- 新颖性: ⭐⭐⭐⭐ 首次系统性地解决 Real-ISR 中的奖励黑客问题，诊断式奖励模型概念新颖
- 实验充分度: ⭐⭐⭐ 缓存内容有限，但核心消融清晰，多个 ISR 模型验证
- 写作质量: ⭐⭐⭐⭐ 动机通过图示阐释非常直观，训练曲线对比有说服力
- 价值: ⭐⭐⭐⭐ 为 RL-based 图像修复提供了重要的方法论贡献，CCL 策略可迁移到其他 RLHF 场景

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset](toward_real-world_infrared_image_super-resolution_a_unified_autoregressive_frame.md)
- [\[CVPR 2026\] Beyond Ground-Truth: Leveraging Image Quality Priors for Real-World Image Restoration](beyond_ground-truth_leveraging_image_quality_priors_for_real-world_image_restora.md)
- [\[CVPR 2026\] TM-BSN: Triangular-Masked Blind-Spot Network for Real-World Self-Supervised Image Denoising](tm-bsn_triangular-masked_blind-spot_network_for_real-world_self-supervised_image.md)
- [\[CVPR 2026\] UCAN: Unified Convolutional Attention Network for Expansive Receptive Fields in Lightweight Super-Resolution](ucan_unified_convolutional_attention_lightweight_sr.md)
- [\[CVPR 2026\] Towards Universal Computational Aberration Correction in Photographic Cameras: A Comprehensive Benchmark Analysis](unicac_universal_computational_aberration_correction_benchmark.md)

</div>

<!-- RELATED:END -->
