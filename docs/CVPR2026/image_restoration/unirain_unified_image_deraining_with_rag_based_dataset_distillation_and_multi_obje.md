---
title: >-
  [论文解读] UniRain: Unified Image Deraining with RAG-based Dataset Distillation and Multi-objective Reweighted Optimization
description: >-
  [CVPR 2026][图像恢复][统一去雨] 提出UniRain统一去雨框架，通过RAG驱动的数据蒸馏从公开数据集中筛选高质量样本，并在非对称MoE架构中引入多目标重加权优化策略平衡不同雨退化类型的学习，在日间/夜间雨条纹/雨滴四种场景中达到SOTA。
tags:
  - CVPR 2026
  - 图像恢复
  - 统一去雨
  - RAG数据蒸馏
  - 多目标优化
  - MoE架构
  - 雨条纹/雨滴
---

# UniRain: Unified Image Deraining with RAG-based Dataset Distillation and Multi-objective Reweighted Optimization

**会议**: CVPR 2026  
**arXiv**: [2603.03967](https://arxiv.org/abs/2603.03967)  
**代码**: [GitHub](https://github.com/QianfengY/UniRain)  
**领域**: 图像修复 / 去雨  
**关键词**: 统一去雨, RAG数据蒸馏, 多目标优化, MoE架构, 雨条纹/雨滴

## 一句话总结

提出UniRain统一去雨框架，通过RAG驱动的数据蒸馏从公开数据集中筛选高质量样本，并在非对称MoE架构中引入多目标重加权优化策略平衡不同雨退化类型的学习，在日间/夜间雨条纹/雨滴四种场景中达到SOTA。

## 研究背景与动机

现有去雨方法通常针对特定雨退化类型设计，无法跨场景泛化。实现统一去雨面临两大挑战：

1. **混合数据集质量不均**：直接合并所有公开合成/真实去雨数据集（超200万对），各数据集在背景质量、分辨率、雨形成模式上差异巨大，低质量数据引入错误监督信号
2. **多类型优化不平衡**：不同雨退化类型（日间雨条纹/雨滴、夜间雨条纹/雨滴）难度不同、收敛速度不同，统一训练导致模型偏向简单类型而忽视困难类型

## 方法详解

### 整体框架

公开去雨数据集 → RAG数据蒸馏（检索真实参考+VLM集成投票评估质量）→ 蒸馏后的高质量混合数据集 → Soft-MoE编码器 + Hard-MoE解码器 → 多目标重加权优化动态平衡各类型损失 → 输出去雨图像。

### 关键设计

1. **RAG驱动的数据蒸馏**:
    - 功能：从大规模公开数据集中筛选可靠训练样本
    - 核心思路：检索阶段——构建真实雨图数据库，对查询图像进行三层次相似度匹配（CLIP文本语义→CLIP视觉特征→SSIM结构）检索最相关真实雨参考；生成阶段——将查询图+检索参考+提示模板送入3个VLM进行质量评估，多数投票决定是否保留
    - 设计动机：真实雨图作为参考帮助VLM判断合成数据是否逼真

2. **多目标重加权优化**:
    - 功能：动态平衡不同雨类型的训练
    - 核心思路：滑动窗口内对各类型损失做线性回归估计收敛斜率α → 类型平衡分数TBS（收敛慢的权重大）+ 类型稳定分数TSS（发散的权重小）+ 自适应因子AF（训练早期TBS主导，后期TSS主导）→ 动态损失权重
    - 设计动机：单一优化目标导致模型偏向夜间雨条纹（简单）而忽视日间雨滴（困难）

3. **非对称MoE架构**:
    - 功能：编码器协作保留多样退化线索，解码器精准重建细节
    - 核心思路：Soft-MoE编码器（所有专家连续加权组合）+ Hard-MoE解码器（Top-k路由激活最相关专家）
    - 设计动机：编码需要全面的特征融合，解码需要专注的精细重建

### 损失函数 / 训练策略

- L1重建损失 + 感知损失，由多目标重加权策略动态加权各雨类型
- 收敛斜率估计窗口N内线性回归，TBS/TSS/AF三指标协同
- VLM集成：InternVL2.5-8B + LLaVA-NeXT-7B + MobileVLM-3B多数投票

## 实验关键数据

### 主实验（提出的RainRAG基准）

| 方法 | DRS PSNR | DRD PSNR | NRS PSNR | NRD PSNR | 平均PSNR |
|------|----------|----------|----------|----------|----------|
| Restormer | 28.45 | 23.36 | 33.92 | 25.85 | 27.89 |
| MSDT | 28.60 | 23.31 | 34.56 | 25.28 | 27.94 |
| UniRain | 29.58 | 24.71 | 35.23 | 26.21 | 28.93 |

### 消融实验

| 配置 | 平均PSNR | 说明 |
|------|----------|------|
| 直接合并训练 | 27.55 | 数据质量不均干扰 |
| + RAG蒸馏 | 28.32 | 高质量数据提升 |
| + MoE | 28.61 | 非对称专家帮助 |
| + 多目标优化 | 28.93 | 平衡各类型最终 |

### 关键发现

- RAG蒸馏从200万+图像对中筛选出约70万高质量样本，蒸馏比约35%
- 多目标优化显著缩小各雨类型间的性能差距
- Soft-MoE编码器+Hard-MoE解码器的非对称组合优于对称设计
- 真实场景评估中UniRain的视觉质量一致性最好

## 亮点与洞察

- 首次将RAG思路引入低级视觉的数据筛选，用检索增强VLM的质量评估能力
- 多目标重加权的TBS/TSS/AF三指标设计完整，从收敛速度和稳定性两方面平衡
- 统一四种雨退化类型的实用价值高
- 数据蒸馏pipeline可迁移到其他图像修复任务

## 局限与展望

- VLM质量评估的准确性仍有限，可能错误保留/丢弃样本
- 四种雨类型的划分较粗，未覆盖雾、雪等其他天气退化
- MoE的专家数量和Top-k值的选择需要手动调优
- 未与最新的大规模修复模型（如DiffIR等扩散方法）对比

## 相关工作与启发

- **vs Restormer/MSDT**: 单一退化类型训练，跨场景泛化差；UniRain统一处理四种类型
- **vs URIR**: 最早的统一去雨方法但仅在驾驶场景；UniRain覆盖更多场景
- **vs ReFIR**: RAG用于图像修复推理阶段；UniRain的RAG用于数据筛选训练阶段

## 评分

- 新颖性: ⭐⭐⭐⭐ RAG数据蒸馏+多目标优化的组合在去雨领域新颖
- 实验充分度: ⭐⭐⭐⭐ 自建基准+多个公开数据集，消融完整
- 写作质量: ⭐⭐⭐⭐ 动机图直观，方法描述清晰，公式详细
- 价值: ⭐⭐⭐⭐ 为统一图像修复提供了数据蒸馏和平衡优化的实用方案

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] EVLF: Early Vision-Language Fusion for Generative Dataset Distillation](evlf_early_vision-language_fusion_for_generative_dataset_distillation.md)
- [\[CVPR 2026\] Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset](toward_real-world_infrared_image_super-resolution_a_unified_autoregressive_frame.md)
- [\[CVPR 2026\] UniBlendNet: Unified Global, Multi-Scale, and Region-Adaptive Modeling for Ambient Lighting Normalization](uniblendnet_unified_global_multi_scale_and_region_adaptive_modeling_for_ambient_lighting_normalization.md)
- [\[CVPR 2026\] RAR: Restore, Assess, Repeat - A Unified Framework for Iterative Image Restoration](rar_restore_assess_repeat_a_unified_framework_for_iterative_image_restoration.md)
- [\[CVPR 2026\] UCAN: Unified Convolutional Attention Network for Expansive Receptive Fields in Lightweight Super-Resolution](ucan_unified_convolutional_attention_network_for_expansive_receptive_fields_in_l.md)

<!-- RELATED:END -->
