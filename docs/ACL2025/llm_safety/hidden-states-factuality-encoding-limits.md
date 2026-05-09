---
title: >-
  [论文解读] Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs
description: >-
  [ACL 2025][事实性编码] 本文挑战了先前关于 LLM 隐藏状态能编码事实性信息的研究结论，通过构建更真实和更具挑战性的数据集（基于困惑度的负采样 + QA导出的LLM生成事实），发现先前结论在更真实的场景下难以泛化。
tags:
  - ACL 2025
  - 事实性编码
  - 隐藏状态
  - 探针分类器
  - 数据集真实性
  - LLM安全
---

# Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs

**会议**: ACL 2025  
**arXiv**: [2505.16520](https://arxiv.org/abs/2505.16520)  
**代码**: GitHub Repository（论文中提供）  
**领域**: LLM安全  
**关键词**: 事实性编码, 隐藏状态, 探针分类器, 数据集真实性, LLM内部表示

## 一句话总结

本文挑战了先前关于 LLM 隐藏状态能编码事实性信息的研究结论，通过构建更真实和更具挑战性的数据集（基于困惑度的负采样 + QA导出的LLM生成事实），发现先前结论在更真实的场景下难以泛化。

## 研究背景与动机

1. **领域现状**：近期研究表明 LLM 在生成虚假陈述时内部状态编码了事实性信息，可以训练探针分类器（如 SAPLMA）来区分真假。
2. **现有痛点**：先前研究使用的数据集包含过于明显的错误陈述（如"斑马用飞行移动"），与 LLM 实际生成的细微错误不匹配，泛化性存疑。
3. **核心矛盾**：如果假陈述过于荒谬，探针可能只是学到了"罕见/异常模式"而非真正的事实性编码。
4. **本文目标**：用更真实的数据集重新检验 LLM 隐藏状态的事实性编码能力。
5. **切入角度**：(1) 基于困惑度的负采样生成更合理的假陈述；(2) 从QA数据集中采样LLM实际生成的真假事实。
6. **核心 idea**：先前的积极结论可能部分来自数据集的缺陷，更真实的评估揭示了事实性编码的局限性。

## 方法详解

### 整体框架

复现 SAPLMA 方法论，然后引入两种新的数据集构建策略来测试泛化性。

### 关键设计

1. **困惑度负采样**: 替换真陈述的关键词时，选择困惑度接近原句的替换词（而非随机替换），生成更合理的假陈述。
2. **QA导出数据集**: 用QA数据集提问LLM，正确回答标为True，错误回答标为False——这些是LLM实际会生成的事实。

### 损失函数 / 训练策略

SAPLMA 探针：3层 MLP (256→128→64→sigmoid)，在LLM不同层的激活上训练。

## 实验关键数据

### 主实验

先前结论在原始数据上可复现，但在更真实的数据集上泛化困难。

### 关键发现

- 困惑度负采样的数据集上探针性能下降
- QA导出的LLM生成数据集上泛化最具挑战性
- 中间层的激活通常比最后一层更有信息量

### 数据集对比

| 数据集类型 | 探针AUROC | 说明 |
|-----------|----------|------|
| 原始(荒谬假陈述) | ~0.85 | 可复现先前结论 |
| 困惑度负采样 | ~0.65 | 显著下降 |
| QA导出(LLM生成) | ~0.58 | 最具挑战 |
| 混合数据集 | ~0.62 | 平均效果 |

### 各层探针性能

| 层位置 | 原始数据AUROC | 困惑度数据AUROC |
|--------|-------------|---------------|
| 早期(0-25%) | 0.62 | 0.54 |
| 中期(25-50%) | **0.78** | **0.63** |
| 中后期(50-75%) | 0.75 | 0.60 |
| 最后(75-100%) | 0.68 | 0.55 |


## 亮点与洞察

- 对热门研究方向的严谨质疑，强调数据集真实性对研究结论的决定性影响。
- 提供了更严格的评估方法论，对后续事实性研究有指导意义。

## 局限与展望

- 仅测试了两个开源LLM（OPT-6.7b和Llama 2-7b），更大更强模型上的结论可能不同
- 未探索更复杂的探针架构（如attention-based探针、多层融合探针、对比学习探针）
- 困惑度负采样策略可能引入自身偏差——低困惑度不一定等于语义上合理的替换
- 二分类任务可能过于简单，细粒度的事实性评估（如幻觉严重程度）未覆盖
- 需要更多模型和更多类型的事实性数据来建立更稳健的结论
- 未讨论不同层对事实性编码的差异（仅复现了多层结果）

## 相关工作与启发

- **vs Azaria & Mitchell (2023)**: 原始SAPLMA工作在简单数据集上得出积极结论，本文用更真实的数据集挑战了其泛化性
- **vs Chen et al. (2024)**: 也研究LLM内部的事实性表示，但数据集设计可能同样存在过于简单的问题
- **vs 探针可解释性研究**: 补充了对探针泛化性的重要讨论——在训练分布上有效不代表对真实场景有效
- **vs RATE-FT (同会议)**: 两篇工作互相呼应——内部状态不可靠（本文），需要微调等更强方法（RATE-FT）


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。
- 可以考虑将该方法与强化学习结合，实现端到端的优化。
- 跨领域迁移是一个值得探索的方向——方法的通用性需要更多验证。
- 对于边缘计算和移动端部署场景，方法的轻量化版本值得研究。

## 评分

- 新颖性: ⭐⭐⭐⭐ 质疑热门研究方向的勇气+更严格的评估方法
- 实验充分度: ⭐⭐⭐ 模型范围有限
- 写作质量: ⭐⭐⭐⭐ 逻辑清晰
- 价值: ⭐⭐⭐⭐ 对事实性编码研究有重要的方法论警示

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] ComparisonQA: Evaluating Factuality Robustness of LLMs Through Knowledge Frequency Control and Uncertainty](comparisonqa_evaluating_factuality_robustness_of_llms_through_knowledge_frequenc.md)
- [\[ACL 2025\] Real-time Factuality Assessment from Adversarial Feedback](real-time_factuality_assessment_from_adversarial_feedback.md)
- [\[ACL 2025\] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](monitoring_decoding_mitigating_hallucination_via_evaluating_the_factuality_of_pa.md)
- [\[ACL 2025\] Ewe: Improving Factuality with Explicit Working Memory](improving_factuality_with_explicit_working_memory.md)
- [\[ACL 2025\] ArgHiTZ at ArchEHR-QA 2025: A Two-Step Divide and Conquer Approach to Patient Question Answering for Top Factuality](arghitz_at_archehr-qa_2025_a_two-step_divide_and_conquer_approach_to_patient_que.md)

</div>

<!-- RELATED:END -->
