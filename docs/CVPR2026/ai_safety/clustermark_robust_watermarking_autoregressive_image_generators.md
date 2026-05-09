---
title: >-
  [论文解读] ClusterMark: Towards Robust Watermarking for Autoregressive Image Generators with Visual Token Clustering
description: >-
  [CVPR 2026][AI安全][自回归图像生成] 提出基于视觉 Token 聚类的水印方法 ClusterMark，通过将相似 Token 分配到同一颜色集（红/绿），大幅提升自回归图像生成模型水印在图像扰动下的鲁棒性，同时保持图像质量和快速验证。
tags:
  - CVPR 2026
  - AI安全
  - 自回归图像生成
  - 水印
  - 视觉Token聚类
  - 鲁棒性
  - KGW水印
---

# ClusterMark: Towards Robust Watermarking for Autoregressive Image Generators with Visual Token Clustering

**会议**: CVPR 2026  
**arXiv**: [2508.06656](https://arxiv.org/abs/2508.06656)  
**代码**: [https://github.com/lukovnikov/ClusterMark](https://github.com/lukovnikov/ClusterMark)  
**领域**: AI 安全 / 图像水印  
**关键词**: 自回归图像生成, 水印, 视觉Token聚类, 鲁棒性, KGW水印

## 一句话总结

提出基于视觉 Token 聚类的水印方法 ClusterMark，通过将相似 Token 分配到同一颜色集（红/绿），大幅提升自回归图像生成模型水印在图像扰动下的鲁棒性，同时保持图像质量和快速验证。

## 研究背景与动机

1. **领域现状**：生成内容水印是应对 AI 滥用的关键工具。扩散模型的生成中嵌入水印已有成熟研究，但自回归（AR）图像模型的水印研究尚处于早期。
2. **现有痛点**：直接将 LLM 的 KGW 水印迁移到 AR 图像模型可行但不鲁棒——验证时需将图像重新编码为 Token，图像扰动导致 Token 重建不准确，水印检测率大幅下降。
3. **核心矛盾**：VQ-VAE 的量化过程使得即使微小扰动也可能产生完全不同的 Token，而 KGW 方案中相似 Token 被随机分配到红/绿集，导致重建 Token 的颜色判定不稳定。
4. **本文目标**：设计对图像扰动鲁棒的 AR 图像模型水印方案。
5. **切入角度**：将码本中嵌入空间相近的 Token 聚类到同一组，使绿/红集划分在聚类级别而非 Token 级别进行。
6. **核心 idea**：扰动后的图像虽然 Token 可能变化，但大概率落入同一聚类，从而保持颜色集判定的稳定性。

## 方法详解

### 整体框架

生成前：对码本 Token 用 k-means 聚类。生成时：基于前一 Token 的聚类（而非 Token 本身）计算哈希，将聚类而非单个 Token 划分为绿/红集，偏置 logits 使模型偏好绿色 Token。验证时：编码图像为 Token，计算绿色 Token 比例，进行单侧二项检验。

### 关键设计

1. **基于聚类的绿/红集划分**:

    - 功能：提升水印对图像扰动的鲁棒性
    - 核心思路：用 k-means 将码本 $\mathbb{V}$ 聚为 $k$ 个聚类 $(C_1, ..., C_k)$。哈希基于聚类索引而非 Token 索引：$o_i = \text{hash}(\kappa, c(q_{i-1}))$。绿集为聚类的并集：$G_i = \bigcup_{C_i \in G_i^{\text{cluster}}} C_i$。
    - 设计动机：扰动后 Token 虽可能变化但大概率落入同一聚类（因为聚类基于码本向量欧氏距离），颜色判定稳定。

2. **Token/聚类分类器微调**:

    - 功能：进一步提升扰动下的 Token 重建准确性
    - 核心思路：复制 VQ-VAE 编码器并添加分类输出层，用对抗性扰动增强的未水印图像训练。Token 分类器预测原始 Token 索引，聚类分类器直接预测聚类索引。
    - 设计动机：标准 VQ-VAE 编码器在扰动图像上的 Token 重建不够准确，微调版本可学会"撤销"扰动的影响。

3. **前缀调优**:

    - 功能：选择最优哈希前缀以避免假阳性
    - 核心思路：某些前缀 $\kappa$ 在包含大面积均匀区域的图像上会产生异常高的绿色 Token 比例，导致假阳性。通过在多个 $\kappa$ 值中选择最佳来缓解。
    - 设计动机：低聚类数量时此问题更严重，因为特定聚类转换模式更容易在均匀区域产生偏误。

### 损失函数 / 训练策略

Token 分类器训练：CE 损失 + 扰动增强的未水印图像。聚类分类器：CE 损失预测聚类索引。30 epoch，线性增长扰动强度。

## 实验关键数据

### 主实验

| 模型/方法 | Clean AUC/TPR | JPEG20 | 高斯模糊 | 椒盐噪声 | 重生成 |
|-----------|-------------|--------|---------|---------|-------|
| 无聚类 (baseline) | 1.0/0.999 | 0.692 | 0.068 | 0.069 | 0.710 |
| 聚类 k=64 | 1.0/1.0 | 0.956 | 0.663 | 0.402 | 0.972 |
| +聚类分类器 | 1.0/1.0 | 0.893 | 0.925 | 0.999 | 0.935 |

### 消融实验

| 配置 | JPEG | 高斯噪声 | 说明 |
|------|------|---------|------|
| k=8 | 最高鲁棒 | 最高鲁棒 | 但 FID 下降明显，方差大 |
| k=64 | 高鲁棒 | 良好 | 最佳质量-鲁棒性平衡 |
| k=128 | 中等 | 中等 | 接近无聚类 |
| δ=5 vs δ=2 | 显著更好 | 显著更好 | 更强偏置=更强水印 |
| γ=0.25 vs 0.5 | 显著更好 | 更好 | 更小绿集=更强信号 |

### 关键发现

- 聚类即使在无训练设定下也大幅提升鲁棒性，尤其对 JPEG 压缩和重生成攻击
- 聚类分类器最有效解决椒盐噪声问题（从 40.2% → 99.9% TPR）
- 验证速度极快（~12ms/图），比扩散模型水印快数个数量级

## 亮点与洞察

- **训练无关的基线即有效**：仅通过 k-means 聚类就能大幅提升鲁棒性，实现极其简洁
- **聚类级别哈希**：将哈希从 Token 级提升到聚类级是关键创新，使水印对 Token 级扰动具有天然容错
- **实用验证效率**：验证时间与轻量级后处理水印方案可比（~12ms），远快于扩散模型水印

## 局限与展望

- 对旋转和裁剪等几何变换仍然脆弱，需要图像同步层辅助
- 聚类减少了有效码本大小，k 值过低时图像质量会下降
- 目前仅在从左到右顺序解码的 AR 模型上验证

## 相关工作与启发

- **vs IndexMark**: IndexMark 将相似 Token 配对但分到不同颜色集，ClusterMark 将相似 Token 放入同一颜色集
- **vs WMAR**: WMAR 同时微调 VAE 解码器增加复杂度，ClusterMark 不修改解码器更简洁

## 评分

- 新颖性: ⭐⭐⭐⭐ 聚类级别水印是简洁而有效的创新
- 实验充分度: ⭐⭐⭐⭐⭐ 三个模型 + 多种扰动 + 全面消融 + 运行时间对比
- 写作质量: ⭐⭐⭐⭐ 结构清晰，算法伪代码完整
- 价值: ⭐⭐⭐⭐ AR 图像模型水印的实用解决方案

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] RecoverMark: Robust Watermarking for Localization and Recovery of Manipulated Faces](recovermark_robust_watermarking_for_localization_and_recovery_of_manipulated_fac.md)
- [\[CVPR 2026\] AdvMark: Decoupling Defense Strategies for Robust Image Watermarking](decoupling_defense_strategies_for_robust_image_watermarking.md)
- [\[CVPR 2026\] Tutor-Student Reinforcement Learning: A Dynamic Curriculum for Robust Deepfake Detection](tutor-student_reinforcement_learning_a_dynamic_curriculum_for_robust_deepfake_de.md)
- [\[AAAI 2026\] Robust Watermarking on Gradient Boosting Decision Trees](../../AAAI2026/ai_safety/robust_watermarking_on_gradient_boosting_decision_trees.md)
- [\[CVPR 2026\] FedAFD: Multimodal Federated Learning via Adversarial Fusion and Distillation](fedafd_multimodal_federated_learning_via_adversarial_fusion_and_distillation.md)

</div>

<!-- RELATED:END -->
