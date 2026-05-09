---
title: >-
  [论文解读] Teaching Tailored to Talent: Adverse Weather Restoration via Prompt Pool and Depth-Anything Constraint
description: >-
  [ECCV 2024][其他] 提出 T3-DiffWeather，采用 prompt pool 自主组合子 prompt 构建天气退化信息，结合 Depth-Anything 约束的通用 prompt 提供场景信息，以对比 prompt 损失约束两类 prompt，在恶劣天气图像恢复任务上仅用 WeatherDiffusion 十分之一的采样步数达到 SOTA。
tags:
  - ECCV 2024
  - 其他
  - 扩散模型
  - 提示学习
  - Depth-Anything
  - 对比学习
---

# Teaching Tailored to Talent: Adverse Weather Restoration via Prompt Pool and Depth-Anything Constraint

**会议**: ECCV 2024  
**arXiv**: [2409.15739](https://arxiv.org/abs/2409.15739)  
**代码**: [https://ephemeral182.github.io/T3-DiffWeather](https://ephemeral182.github.io/T3-DiffWeather)  
**领域**: 其他  
**关键词**: 恶劣天气图像恢复, 扩散模型, Prompt Pool, Depth-Anything, 对比学习

## 一句话总结

提出 T3-DiffWeather，采用 prompt pool 自主组合子 prompt 构建天气退化信息，结合 Depth-Anything 约束的通用 prompt 提供场景信息，以对比 prompt 损失约束两类 prompt，在恶劣天气图像恢复任务上仅用 WeatherDiffusion 十分之一的采样步数达到 SOTA。

## 研究背景与动机

### 领域现状

**领域现状**：天气组合的复杂性**: 真实世界中天气退化呈现不可预测的组合，现有方法难以自适应处理

### 现有痛点

**现有痛点**：现有方法的不足**:

### 核心矛盾

**核心矛盾**：单一天气模型无法泛化到其他天气类型

### 解决思路

**解决思路**：共享 prompt 方案不考虑退化间的差异和共性

### 补充说明

**补充说明**：WeatherDiffusion 仅用退化图像作条件，信息不够丰富且需要大量采样步数

### 补充说明

**补充说明**：关键洞察**: 退化具有可区分的特征（图像残差）；不同天气间既有共性（低对比度、雾化遮蔽）又有差异（形状、尺度）；干净背景在不同天气下共享共性

## 方法详解

### 整体框架

T3-DiffWeather 的核心是"因材施教"——为不同退化和背景提供定制化的 prompt 条件:
1. **Prompt Pool**: 自主组合子 prompt 构建实例级天气 prompt
2. **General Prompts**: 受 Depth-Anything 约束，提供场景感知信息
3. **Contrastive Prompt Loss**: 约束两类 prompt 的表示
4. **残差学习**: 扩散模型的重建目标从干净图像改为退化残差($r_d = x - y$)

### 关键设计

1. **Prompt Pool 天气表示**:
    - 维护 N 个子 prompt 及对应的 learnable key
    - 输入退化残差嵌入 $\mathcal{F}_e$ 后取均值作为 query
    - 计算 query 与所有 key 的余弦相似度，选择 top-k 子 prompt 拼接为天气 prompt
    - 实现了实例级自适应组合——共享子 prompt 捕获共性，独特子 prompt 捕获差异

2. **Depth-Anything 约束的通用 prompt**:
    - **观察**: Depth-Anything 对恶劣天气退化几乎免疫，其中间特征具有出色的场景鲁棒性
    - 冻结 Depth-Anything 提取特征 $\mathcal{F}_d$
    - 通用 prompt 作 Query，Depth-Anything 特征作 Key/Value 进行交叉注意力
    - 获得场景感知的通用 prompt $\mathcal{P}_{gd}$ 引导背景重建

3. **对比 Prompt 损失**:
    - 天气 prompt 和通用 prompt 互为负样本（设计动机不同）
    - 通用 prompt 的 key 与 Depth-Anything 特征均值互为正样本
    - 无需额外构造负样本或依赖预训练网络映射到特征空间

### 损失函数 / 训练策略

$$\mathcal{L}_{total} = \lambda_1 \mathcal{L}_{res} + \lambda_2 \mathcal{L}_{cp} + \lambda_3 ||(r_d^{sample} + y) - x||_{psnr} + \lambda_4 \mathcal{L}_{cp}^{sample}$$

- $\mathcal{L}_{res}$: 残差噪声估计损失（主损失）
- $\mathcal{L}_{cp}$: 对比 prompt 损失
- 训练时额外进行采样过程以获得重建损失和采样阶段的对比损失
- Prompt 通过 cross-attention 嵌入扩散网络的 latent 层

## 实验关键数据

### 主实验 (All-in-One 天气恢复)

T3-DiffWeather 在多个合成和真实世界数据集上达到 SOTA，且采样步数仅为 WeatherDiffusion 的 **1/10**。

（由于论文中详细数据表在未读取的部分，以下为论文中强调的关键点）:
- 在各类恶劣天气基准上达到 SOTA
- 采样步数显著减少（比 WeatherDiffusion 少约 10 倍）
- 在真实世界数据集上泛化良好

### 消融实验

- Prompt Pool vs 共享 prompt: prompt pool 允许实例级自适应组合，性能更优
- Depth-Anything 约束 vs 无约束: DA 约束显著提升背景重建质量
- 对比 prompt 损失: 进一步提升两类 prompt 的表示质量
- t-SNE 可视化: 天气 prompt 在不同天气类型间形成清晰但有重叠的聚类，符合预期

### 关键发现

- **子 prompt 频率分析**: 不同天气类型自适应选择不同子 prompt 组合，相似天气（如 rain 和 raindrop）共享更多子 prompt
- **Depth-Anything 的鲁棒性**: 对退化图像估计的深度图几乎不受天气影响，其中间特征是理想的场景先验
- **残差学习优于直接学习**: 退化残差比干净图像更容易建模，且能更清晰地表示退化特征

## 亮点与洞察

1. **"因材施教"类比**: 将 prompt learning 比作个性化教学——不同退化需要不同的知识组合，同时共享基础知识
2. **首次利用 Depth-Anything 约束图像恢复**: 发现并利用了 Depth-Anything 对天气退化的免疫性
3. **自然的负样本设计**: 两类 prompt 因设计动机不同自然互为负样本，简化了对比学习
4. **实用效率**: 大幅降低扩散模型在图像恢复中的采样步数

## 局限与展望 / 可改进方向

- Prompt pool 的大小 N 和 top-k 选择需要超参数搜索
- Depth-Anything 特征提取增加了计算开销
- 对比 prompt 损失的有效性依赖于两类 prompt 的设计确实正交
- 未讨论对极端退化（如暴雪+浓雾叠加）的处理能力
- 可进一步探索将天气 prompt 与其他图像恢复任务结合

## 相关工作与启发

- 相比 PromptIR 的共享 prompt，prompt pool 允许更灵活的退化表示
- Depth-Anything 作为通用场景先验的思路可推广到其他低级视觉任务
- "退化残差学习"在扩散模型中的应用值得在其他恢复任务中验证

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ — Prompt pool + DA 约束 + 对比损失的组合很有创意
- **技术深度**: ⭐⭐⭐⭐ — 设计动机清晰，各组件相互支撑
- **实验质量**: ⭐⭐⭐⭐ — 多基准覆盖，含可视化分析
- **实用性**: ⭐⭐⭐⭐ — 效率提升显著，有实际应用价值
- **综合推荐**: ⭐⭐⭐⭐

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Active Generation for Image Classification](active_generation_for_image_classification.md)
- [\[ECCV 2024\] ET: The Exceptional Trajectories - Text-to-Camera-Trajectory Generation with Character Awareness](et_the_exceptional_trajectories_text-to-camera-trajectory_generation_with_charac.md)
- [\[ECCV 2024\] Shifted Autoencoders for Point Annotation Restoration in Object Counting](shifted_autoencoders_for_point_annotation_restoration_in_object_counting.md)
- [\[ECCV 2024\] Functional Transform-Based Low-Rank Tensor Factorization for Multi-Dimensional Data Recovery](functional_transform-based_low-rank_tensor_factorization_for_multi-dimensional_d.md)
- [\[ECCV 2024\] Event-based Mosaicing Bundle Adjustment](event-based_mosaicing_bundle_adjustment.md)

</div>

<!-- RELATED:END -->
