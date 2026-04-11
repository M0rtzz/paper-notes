---
description: "【论文笔记】Reasoning Limitations of Multimodal Large Language Models. A Case Study of Bongard Problems 论文解读 | ICML2025 | arXiv 2411.01173 | abstract visual reasoning | 系统评估了 8 个 MLLM 在 Bongard Problems 上的抽象视觉推理能力，并引入 Bongard-RWR 数据集（合成概念的真实图像版本），揭示 MLLM 在合成 BP 上表现极差并非因领域差异，而是其固有的抽象推理局限。"
tags:
  - ICML2025
---

# Reasoning Limitations of Multimodal Large Language Models. A Case Study of Bongard Problems

**会议**: ICML2025  
**arXiv**: [2411.01173](https://arxiv.org/abs/2411.01173)  
**代码**: [GitHub](https://github.com/pavonism/bongard-rwr)  
**领域**: multimodal_vlm  
**关键词**: abstract visual reasoning, Bongard Problems, MLLM evaluation, few-shot learning, concept-based reasoning

## 一句话总结
系统评估了 8 个 MLLM 在 Bongard Problems 上的抽象视觉推理能力，并引入 Bongard-RWR 数据集（合成概念的真实图像版本），揭示 MLLM 在合成 BP 上表现极差并非因领域差异，而是其固有的抽象推理局限。

## 研究背景与动机
- Bongard Problems (BPs) 是抽象视觉推理（AVR）的经典测试：左右各6张图，需发现区分两侧的概念规则并用自然语言描述
- BP 结合了感知（从图像中提取概念）和认知（跨上下文推理），是少样本学习设定（每侧仅6样本）
- 随着 MLLM（如 GPT-4o、Gemini、Claude）的发展，测试其 AVR 能力变得重要
- **关键问题**：MLLM 在真实世界 BP（如 Bongard-HOI）上有一定成功，但在合成 BP 上几乎完全失败——这是因为合成领域本身，还是推理能力不足？

## 方法详解

### 解题策略设计
提出 6 种面向 MLLM 的 BP 解题策略：
1. **Direct**：直接给整个矩阵图，要求生成答案
2. **Descriptive**：逐图描述后汇总推理
3. **Descriptive-iterative**：迭代式描述，同一侧共享上下文
4. **Contrastive**：成对对比左右对应图像的差异
5. **Contrastive-iterative**：迭代式对比
6. **Direct 变体**：在描述/对比后额外提供完整矩阵图

### 评估设置
- **自然语言生成**：模型生成概念描述，用 MLLM 集成判断是否与 ground truth 匹配
- **二分类**：Ground-Truth 验证、Incorrect Label 检测、Images-to-Sides 分配

### Bongard-RWR 数据集
- 用 GPT-4o 将前100个合成 BP 概念翻译为真实世界描述
- 用 Pexels API 搜索匹配图像，经 GPT-4o 筛选
- 最终获得 60 个实例：12 全自动、24 半自动调整、24 全手工制作
- 支持直接对比合成 vs 真实场景下同一概念的 MLLM 表现

## 实验关键数据

| 模型 | 合成BP (Direct/De/Co) | HOI (Di/De/Co) | RWR (Di/De/Co) |
|------|----------------------|----------------|----------------|
| GPT-4o | 17/17/10 | 35/42/18 | 5/8/2 (共60) |
| Claude 3.5 | 13/19/15 | 5/44/13 | 1/13/2 |
| Gemini 1.5 | 7/21/17 | 23/40/15 | 3/7/1 |
| InternVL2-8B | 0/0/0 | 12/2/2 | 0/0/0 |
| LLaVA-1.6 | 0/1/0 | 5/4/1 | 0/0/0 |

- **人类基准**：Bongard-RWR 上平均正确 39.2/60（65%）
- **最佳 MLLM**：Claude 3.5 Descriptive 策略仅 13/60（21.7%）
- 合成 BP 上所有模型表现极差（≤21/100），开源模型几乎为零
- Bongard-RWR 与合成 BP 表现高度一致，说明问题并非领域导致

## 亮点与洞察
- **Bongard-RWR 是关键贡献**：首次实现合成 vs 真实的受控对比，证实推理能力是瓶颈
- **策略对比揭示 MLLM 特性**：Descriptive 策略普遍最佳，说明逐图分析 > 直接整体推理
- **Ground-Truth 验证有趣发现**：模型能验证正确答案（~80%准确率），但不能自主发现答案
- **人类 vs MLLM 差距巨大**：人类 65% vs MLLM 最高 21.7%，且人类也觉得 RWR 不容易
- 开源模型在 AVR 上完全失败，说明该能力并非简单 scaling 可获得

## 局限性 / 可改进方向
- Bongard-RWR 仅覆盖前 100 个合成 BP 中的 60 个
- 人类基准仅有有限参与者，信度可进一步提升
- 未测试最新的推理增强 MLLM（如 GPT-4o + CoT、o1）
- 评估依赖 MLLM 集成判断答案匹配，可能引入偏差
- 仅二分类设置中的 Images-to-Sides 能客观评估，其他设置依赖语义匹配
- 数据集的自动化生成流程中有人工调整步骤，不完全可重现
- 分析集中在结果层面，缺乏对 MLLM 推理过程的深入分析

## 相关工作与启发
- **Bongard-LOGO**（Nie et al., 2020）：合成 BP 的 meta-learning benchmark
- **Bongard HOI/OpenWorld**（Jiang et al., 2022; Wu et al., 2024）：真实世界 BP
- **Wüst et al. (2024)**：并行工作，也测试 MLLM 解合成 BP
- **ARC**（Chollet, 2019）：另一抽象推理基准
- 启发：MLLM 的视觉推理能力远未达到人类水平，概念形成+少样本推理是核心瓶颈

## 评分
- 新颖性: ⭐⭐⭐⭐ (Bongard-RWR 数据集+系统策略设计)
- 实验充分度: ⭐⭐⭐⭐⭐ (8模型×4数据集×6策略×3设置)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，分析深入)
- 价值: ⭐⭐⭐⭐ (揭示MLLM的根本推理局限)

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
