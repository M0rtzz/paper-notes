---
title: >-
  [论文解读] Scaling RL to Long Videos
description: >-
  [NeurIPS 2025][视频理解][强化学习] 提出 LongVILA-R1 全栈框架，通过构建 104K 长视频推理数据集、两阶段 CoT-SFT + RL 训练流水线、以及高效的多模态强化学习序列并行 (MR-SP) 系统，将 VLM 的推理能力扩展到长视频（最高支持 8192 帧），在 VideoMME 上达到 65.1%/71.1%。
tags:
  - NeurIPS 2025
  - 视频理解
  - 强化学习
  - long video reasoning
  - sequence parallelism
  - VLM
  - chain-of-thought
---

# Scaling RL to Long Videos

**会议**: NeurIPS 2025  
**arXiv**: [2507.07966](https://arxiv.org/abs/2507.07966)  
**代码**: [GitHub](https://github.com/NVlabs/Long-RL)  
**领域**: Video Understanding  
**关键词**: reinforcement learning, long video reasoning, sequence parallelism, VLM, chain-of-thought

## 一句话总结

提出 LongVILA-R1 全栈框架，通过构建 104K 长视频推理数据集、两阶段 CoT-SFT + RL 训练流水线、以及高效的多模态强化学习序列并行 (MR-SP) 系统，将 VLM 的推理能力扩展到长视频（最高支持 8192 帧），在 VideoMME 上达到 65.1%/71.1%。

## 研究背景与动机

长视频理解需要超越简单识别的推理能力——包括时序推理、空间追踪、目标推理和叙事理解。但目前面临两大瓶颈：

**数据缺口**：不同于数学/代码推理有丰富的结构化数据，长视频推理标注涉及复杂的时空动态、目标和叙事元素，标注成本极高
**训练基础设施瓶颈**：RL 应用于长视频时计算负担极重——数百到数千帧的视频需要巨大的显存和更长的 rollout 时间，现有 RL 框架（如 R1-V、EasyR1）无法处理

## 方法详解

### 整体框架

LongVILA-R1 包含三个核心组件：
- **LongVideo-Reason 数据集**：104K 高质量长视频 QA 对，含推理标注
- **两阶段训练流水线**：Stage-1 CoT-SFT 热启动 + Stage-2 GRPO 强化学习
- **MR-SP 训练系统**：多模态强化学习序列并行，解决长视频 RL 的计算瓶颈

### 关键设计

1. **LongVideo-Reason 数据构建**：

    - 从 Shot2Story 数据集筛选 18K 长视频，加入 2K 额外高分辨率视频
    - 先将视频切成 ~10 秒片段，用 NVILA-8B 生成每段字幕
    - 将所有片段字幕输入 DeepSeek-R1-671B，生成跨越整个视频内容的 Question-Reasoning-Answer 三元组
    - 覆盖四类推理：时序推理、目标/意图推理、空间推理、情节/叙事推理
    - 数据过滤：用 LongVILA 推理 10 次，过滤掉太简单或太难的问题，保留中等难度样本以保证 GRPO 有有意义的 advantage 信号
    - 36K 用于 CoT-SFT，68K + 额外 102K 开源数据用于 RL

2. **两阶段训练**：

    - **Stage-1 (CoT-SFT)**：用 36K 高质量 CoT 数据做 SFT，格式为 `<think></think><answer></answer>`，为模型注入基本推理和指令跟随能力
    - **Stage-2 (GRPO)**：标准 GRPO 框架，组大小 $G=8$，使用基于规则的奖励（格式+准确率），优化目标：
    $\mathcal{J}(\theta) = \mathbb{E}_{q,\{o_i\}} \left[ \frac{1}{G} \sum_{i=1}^{G} \min\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip}(\cdot) A_i\right) - \beta D_{KL} \right]$

3. **MR-SP 多模态强化序列并行**：

    - **Stage 1 - 并行编码与嵌入复用**：视频帧均匀分配到多 GPU，各 GPU 独立编码后 all-gather 聚合。关键优化：编码结果缓存复用，一次编码供 8~16 次 rollout 使用
    - **Stage 2 - 序列并行预填充**：聚合后的嵌入先 padding 到统一长度，再均匀分片到各 GPU，实现 policy 和 reference 模型的并行预填充
    - 解决核心痛点：避免长视频的重复编码开销和单 GPU 显存溢出

### 损失函数 / 训练策略

- 奖励函数：基于规则的准确率奖励 + 格式奖励
- Advantage 归一化：$A_i = (r_i - \text{mean}) / \text{std}$
- 数据过滤对 GRPO 至关重要：如果所有 rollout 都正确或都错误，advantage 为 0，梯度消失

## 实验关键数据

### 主实验

| 模型 | VideoMME (w/o sub.) | VideoMME (w/ sub.) | LongVideo-Reason-eval |
|------|--------------------|--------------------|----------------------|
| LongVILA-7B | 60.1 | 65.1 | 62.7 |
| LongVILA-R1-7B | **65.1** (+5.0) | **71.1** (+6.0) | **72.0** (+9.3) |
| Video-R1-7B | 61.4 | - | 68.1 |
| Gemini-1.5-Pro | 75.0 | 81.3 | 69.3 |
| GPT-4o | 71.9 | 77.2 | - |

LongVILA-R1-7B 在自建 LongVideo-Reason-eval 上以 72.0% 超越 Video-R1 (68.1%) 和 Gemini-1.5-Pro (69.3%)。

### 消融实验

| 配置 | CoT-SFT | RL | LongVideo-Reason-eval 准确率 |
|------|---------|-----|---------------------------|
| LongVILA-1.5B 基线 | ✗ | ✗ | ~55% |
| 仅 CoT-SFT (Ours) | ✓ | ✗ | ~62% |
| 仅 CoT-SFT (Others) | O | ✗ | ~58% |
| CoT-SFT + RL | ✓ | ✓ | **64.3%** |
| 跳过 CoT-SFT，直接 RL | ✗ | ✓ | 下降 |

### 关键发现

- **帧数 scaling**：推理能力随输入帧数一致提升。LongVILA-R1-1.5B 从 16 帧到 512 帧持续改善；而不带 RL 的 LongVILA-1.5B 在 256 帧时触顶、512 帧时反而下降
- **MR-SP 效率**：在 512 帧上实现 2.1× 加速，在 1024 帧时避免 OOM（baseline 直接 OOM）
- **数据质量关键**：自建数据集的 CoT-SFT 明显优于使用其他数据集
- **CoT-SFT 热启动必要**：跳过 SFT 直接 RL 导致性能下降

## 亮点与洞察

- 首个将 RL 推理训练系统性扩展到长视频的工作，涵盖数据、算法和系统三个层面
- MR-SP 的视频嵌入缓存复用策略很实用——一个训练步 8-16 次 rollout，节省 8-16 倍视觉编码成本
- 数据过滤策略（过滤太简单和太难的样本）对 GRPO 收敛至关重要，这一经验可推广到其他 RL 训练
- 在 8×A100 单节点上支持 3600 帧（1小时视频）的 RL 训练

## 局限性 / 可改进方向

- 自建 benchmark LongVideo-Reason-eval 规模较小（1K 样本），评估稳定性有待验证
- 数据构建依赖 NVILA-8B 和 DeepSeek-R1-671B，成本约 80K H100 GPU 小时，可复现性受限
- 开放式问题的奖励函数设计仍依赖规则匹配，不够灵活
- 尚未探索与 DPO 等偏好优化方法的结合

## 相关工作与启发

- 与 Video-R1 的关系：Video-R1 使用 T-GRPO 但仅处理 16 帧短视频；LongVILA-R1 将其扩展到数千帧
- 与 DeepSeek-R1 的关系：借鉴其 GRPO 算法和数据过滤策略，并通过 MR-SP 使其适配多模态长上下文
- 启发：RL + 推理的 scaling law 在视频领域同样成立——更多帧 = 更好推理，但需要配套的系统支撑

## 评分
- 新颖性: ⭐⭐⭐⭐ 系统性解决方案（数据+训练+系统），单点创新有限但整合出色
- 实验充分度: ⭐⭐⭐⭐ 多基准评估，消融设计合理，但自建 benchmark 的可信度待验证
- 写作质量: ⭐⭐⭐⭐ 结构完整，系统设计描述清晰
- 价值: ⭐⭐⭐⭐⭐ 全栈开源（代码+模型+数据+训练系统），对社区价值很高
