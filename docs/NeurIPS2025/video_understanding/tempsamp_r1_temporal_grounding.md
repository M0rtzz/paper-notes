---
title: >-
  [论文解读] TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs
description: >-
  [NeurIPS 2025][视频理解][视频时间定位] 本文提出 TempSamp-R1，一个混合策略强化微调框架，通过将高质量离策略（ground truth）引导融入 GRPO 的在策略采样，并设计非线性软优势估计稳定训练，在视频时间定位任务上实现 SOTA（Charades-STA R1@0.7: 52.9%，ActivityNet R1@0.5: 56.0%）。
tags:
  - NeurIPS 2025
  - 视频理解
  - 视频时间定位
  - 强化学习微调
  - GRPO
  - 混合策略采样
  - 链式思维
---

# TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs

**会议**: NeurIPS 2025  
**arXiv**: [2509.18056](https://arxiv.org/abs/2509.18056)  
**代码**: [GitHub](https://github.com/HVision-NKU/TempSamp-R1)  
**领域**: 视频理解  
**关键词**: 视频时间定位, 强化学习微调, GRPO, 混合策略采样, 链式思维

## 一句话总结
本文提出 TempSamp-R1，一个混合策略强化微调框架，通过将高质量离策略（ground truth）引导融入 GRPO 的在策略采样，并设计非线性软优势估计稳定训练，在视频时间定位任务上实现 SOTA（Charades-STA R1@0.7: 52.9%，ActivityNet R1@0.5: 56.0%）。

## 研究背景与动机

1. **领域现状**: MLLM 在通用视频理解上表现出色，但在时间定位（temporal grounding）任务上仍面临挑战，需精确理解长视频中的时空关系。

2. **现有痛点**: SFT 方法过拟合于静态时间戳标注，缺乏灵活的时间推理能力。GRPO 在策略采样在大时间搜索空间中效率低，难以找到时间精确的解。

3. **核心矛盾**: GRPO 仅利用 ground truth 计算 IoU 奖励，未将其作为动态学习资源；且离策略解的高奖励导致优势估计偏差。

4. **本文目标**: 设计更稳定高效的 RL 微调框架，充分利用标注信息指导策略学习。

5. **切入角度**: 将 ground truth 作为离策略解直接参与策略优化，但需解决奖励分布偏差问题。

6. **核心 idea**: 混合策略采样 + 非线性软优势估计 + 混合 CoT 训练。

## 方法详解

### 整体框架
基于 Qwen2.5-VL-7B，每个问题生成 G-1 个在策略采样 + 1 个离策略解（ground truth），通过软优势估计模块计算优势值，用于稳定的策略优化。

### 关键设计

1. **混合策略采样（Mix-policy Sampling）**:
    - 功能: 提供时间精确的引导解
    - 核心思路: 对每个查询，从当前策略采样 G-1 个解，加入 1 个 ground truth 作为离策略解，联合归一化计算优势值
    - 设计动机: 纯在策略采样在大时间搜索空间中难以产生高 IoU 解，ground truth 提供精确时间引导

2. **非线性软优势估计**:
    - 功能: 解决离策略高奖励导致的优势偏差
    - 核心思路: 对奖励施加非对称变换：$\tilde{r}_i = \tau + \alpha_1 \cdot \ln((r_i - \tau) + 1)$ 当 $r_i \geq \tau$，指数扩展低奖励区间。压缩接近最优解的优势差，放大次优解间的差距
    - 设计动机: 直接使用离策略奖励会使所有在策略解获得负优势，抑制有效探索

3. **混合 CoT 训练**:
    - 功能: 单一模型同时支持 CoT 和非 CoT 推理
    - 核心思路: 两阶段训练——初始化阶段训练无推理直接回答，后续添加格式奖励鼓励 \<Think\> 推理步骤
    - 设计动机: Charades-STA 和 ActivityNet 受益于 CoT，QVHighlights 受益于直接预测；混合模式互补

### 损失函数 / 训练策略
- IoU 奖励: $R_{IoU}$ 基于预测与 GT 时间区间的交并比
- 时间戳匹配奖励: $R_{ts} = \lambda_{rec} \cdot F2 + \lambda_{score} \cdot \frac{1}{1+WMSE}$
- 格式奖励: 正则表达式验证 \<Think\>...\</Think\>\<Answer\>...\</Answer\> 结构
- 训练: 4 × A100，每 GPU batch=1，G=4（3 在策略 + 1 离策略）
- 两阶段训练：初始化阶段训练无推理直接回答，后续添加格式奖励鼓励推理步骤。视频帧率固定 2 FPS

## 实验关键数据

### 主实验

| 数据集 | 指标 | TempSamp-R1 | TimeZero | VideoChat-R1 | 提升 |
|--------|------|-------------|----------|-------------|------|
| Charades-STA | R1@0.7 | **52.9%** | 47.9% | 50.2% | +2.7% |
| ActivityNet | R1@0.5 | **56.0%** | 47.3% | - | +8.7% |
| QVHighlights | mAP | **30.0%** | - | - | +3.0% |

### 消融实验

| 配置 | mIoU | 说明 |
|------|------|------|
| SFT only | 20.6 | 基线 |
| GRPO only | 30.7 | 纯在策略 |
| TempSamp-R1 | **34.7** | 混合策略+软优势 |

### 关键发现
- 混合 CoT 模式选择最优（CoT vs 非CoT）可进一步提升 4%+ mIoU
- 少样本场景下表现仍稳健
- 非线性奖励整形在 ActivityNet 等搜索空间大的数据集上效果尤为显著
- 少样本实验：仅50个训练视频TempSamp-R1达mIoU 44.7%（SFT 41.9%），500个视频达R1@0.5 64.0%（SFT 51.4%，GRPO 55.3%），训练时间218分钟（GRPO 338分钟）
- 优势整形消融：直接注入GT奖励（Mixed-policy）R1@0.5降至63.0%（分布偏移+多样性下降），Reward downscaling 70.3%，Advantage anchoring 70.7%，非线性整形最优72.1%
- 偏度分析：GRPO持续负偏（低奖励解主导），Mixed-policy高正偏（过度依赖高奖励解），非线性整形维持近零偏度，确保稳定优化
- 跨域泛化：Charades-STA训练→ActivityNet测试，TempSamp-R1比GRPO提升+4.0% mIoU和+4.7% R1@0.5

## 亮点与洞察
- 巧妙地将 ground truth 从"评估工具"转变为"学习资源"
- 非线性优势估计的非对称设计适用于任何包含高质量外部解的 RL 场景
- 混合 CoT 训练让单一模型适应不同复杂度的查询
- 方法简洁，仅需在 GRPO 基础上做小改动
- 采样数消融：仅2个在策略采样+1个离策略时，R1@0.7已从GRPO的34.4%提升至44.6%（+10.2%），效果最大。随着采样数增加到4/6/8，差距缩小但TempSamp-R1始终领先

## 局限与展望
- 依赖 ground truth 作为离策略引导，无标注场景不适用
- 非线性变换的阈值 τ 和系数需要手动调整
- 未探索与更大模型（如 72B）的结合
- 视频帧率固定为 2 FPS，更高帧率可能改善性能
- 奖励分布分析：GRPO在ActivityNet上展现低中位数+高方差，TempSamp-R1中位数显著提升且方差减小，说明混合策略能持续找到高质量解

## 相关工作与启发
- **vs TimeZero**: TimeZero 纯 GRPO 在策略采样，TempSamp-R1 加入离策略引导。ActivityNet R1@0.5: TempSamp-R1 56.0% vs TimeZero 47.3%（+8.7%）。
- **vs VideoChat-R1**: VideoChat-R1 关注奖励函数设计，TempSamp-R1 关注采样策略优化。Charades-STA R1@0.7: TempSamp-R1 52.9% vs VideoChat-R1 50.2%（+2.7%）。
- **vs iMOVE (SFT)**: SFT 方法过拟合时间戳，TempSamp-R1 通过 RL 学会灵活推理

## 评分

### 实现细节
基于Qwen2.5-VL-7B，4×A100训练，每GPU batch=1。
G=4（3在策略+1离策略），视频帧率2 FPS。
- 新颖性: ⭐⭐⭐⭐ 混合策略 + 软优势估计是有效的 RL 改进
- 实验充分度: ⭐⭐⭐⭐ 3 个数据集全面对比
- 写作质量: ⭐⭐⭐⭐ 方法动机和设计逻辑清晰
- 价值: ⭐⭐⭐⭐ 对视频时间定位和 RL 微调都有参考价值

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] Seeing the Arrow of Time in Large Multimodal Models](seeing_the_arrow_of_time_in_large_multimodal_models.md)
- [\[NeurIPS 2025\] DualGround: Structured Phrase and Sentence-Level Temporal Grounding](dualground_phrase_temporal.md)
- [\[NeurIPS 2025\] Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models](structured_sparse_transition_matrices_to_enable_state_tracking_in_state-space_mo.md)
- [\[NeurIPS 2025\] When One Moment Isn't Enough: Multi-Moment Retrieval with Cross-Moment Interactions](when_one_moment_isnt_enough_multi-moment_retrieval_with_cross-moment_interaction.md)
- [\[NeurIPS 2025\] Enhancing Temporal Understanding in Video-LLMs through Stacked Temporal Attention in Vision Encoders](enhancing_temporal_understanding_in_videollms_through_stacke.md)

<!-- RELATED:END -->
