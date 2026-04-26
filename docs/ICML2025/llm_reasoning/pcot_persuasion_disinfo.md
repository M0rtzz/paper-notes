---
title: >-
  [论文解读] PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation
description: >-
  [ICML 2025][LLM推理][虚假信息检测] 本文提出 PCoT（说服增强链式思维）方法，通过两阶段推理——先让 LLM 识别文本中的说服策略，再利用该分析进行虚假信息检测——在五个数据集和五个 LLM 上实现平均 15% 的 F1 提升，并发布了两个新的后知识截止期虚假信息数据集。
tags:
  - ICML 2025
  - LLM推理
  - 虚假信息检测
  - 说服技术
  - 链式思维
  - 零样本分类
  - 大语言模型
---

# PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation

**会议**: ICML 2025  
**arXiv**: [2506.06842](https://arxiv.org/abs/2506.06842)  
**代码**: [GitHub](https://github.com/ArkadiusDS/PCoT)  
**领域**: NLP 理解 / AI 安全  
**关键词**: 虚假信息检测, 说服技术, 链式思维, 零样本分类, 大语言模型

## 一句话总结
本文提出 PCoT（说服增强链式思维）方法，通过两阶段推理——先让 LLM 识别文本中的说服策略，再利用该分析进行虚假信息检测——在五个数据集和五个 LLM 上实现平均 15% 的 F1 提升，并发布了两个新的后知识截止期虚假信息数据集。

## 研究背景与动机

1. **领域现状**: 虚假信息检测是数字通信时代的关键问题。传统监督方法依赖人工标注数据，泛化能力有限；零样本 LLM 检测方法正在兴起但效果不稳定。

2. **现有痛点**: 直接使用 LLM 进行零样本虚假信息检测效果有限，模型缺乏对说服和操纵策略的深入理解。

3. **核心矛盾**: 虚假信息常与说服技术共存，但现有检测方法未利用这一关键线索。

4. **本文目标**: 设计一种通用的零样本方法，通过说服知识注入提升 LLM 的虚假信息检测能力。

5. **切入角度**: 心理学研究表明，教人识别说服谬误能帮助区分真假新闻。

6. **核心 idea**: 将说服技术识别作为推理的中间步骤，为虚假信息检测提供结构化的分析依据。

## 方法详解

### 整体框架
PCoT 采用两阶段流水线：Stage 1 用 LLM 识别文本中的 6 种说服策略并生成解释；Stage 2 将说服分析结果注入虚假信息检测提示，进行最终的二分类判断。

### 关键设计

1. **说服检测阶段（Stage 1）**:
    - 功能: 多标签识别 6 种说服策略
    - 核心思路: 设计 DMT（Detailed Multitask）提示，注入 6 种说服策略（攻击声誉、辩护、简化、转移注意力、号召、操纵性措辞）的定义和子技术描述，让 LLM 同时识别所有策略并生成解释
    - 设计动机: 详细说服知识注入比简单策略名列举提升 9% 的检测 F1；多任务单次调用优于逐策略多次调用

2. **虚假信息检测阶段（Stage 2）**:
    - 功能: 基于说服分析进行虚假信息二分类
    - 核心思路: 将 Stage 1 的说服分析结果 $A_T$（包含每种策略的标签和解释）注入检测提示，LLM 综合文本内容和说服分析做出判断
    - 设计动机: 两阶段比单阶段同时完成说服分析和检测提升 7%，结构化推理更有效

3. **后知识截止期数据集**:
    - 功能: 确保在完全未见数据上的评估可靠性
    - 核心思路: 发布 MultiDis（~2000 篇跨主题新闻，专家三轮标注，86.78% 首轮一致率）和 EUDisinfo（~400 篇英文文章）两个 2024 年后的数据集
    - 设计动机: 现有数据集可能与 LLM 预训练数据重叠，无法可靠评估零样本能力

### 损失函数 / 训练策略
- 纯推理方法，无需训练，所有模型设置 temperature=0
- 评估使用 F1 分数 + McNemar 检验
- 5 个 LLM：GPT-4o Mini、Llama 3.1 8B、Claude 3 Haiku、Llama 3.3 70B、Gemini 1.5 Flash

## 实验关键数据

### 主实验

| 数据集类别 | 指标 | PCoT | Base | 提升 |
|-----------|------|------|------|------|
| Overall (5 datasets) | Avg F1 | 0.815 | 0.711 | +15% |
| Articles | Avg F1 | 0.842 | 0.715 | +18% |
| Posts | Avg F1 | 0.758 | 0.700 | +8% |
| Post-Cutoff (新数据) | Avg F1 | 0.838 | 0.721 | +16% |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| PCoT 两阶段 | F1 0.815 | 最优 |
| PCoT 单阶段 | F1 0.765 | 同时完成两任务效果差 |
| PCoT base version (无策略详情) | F1 ~0.79 | 仅一般性说服概念也有帮助 |
| 有说服的子集 | F1 0.847 | 说服存在时提升更大 |
| 无说服的子集 | F1 0.392 | 说明说服分析是核心驱动力 |

### 关键发现
- 92% 的虚假信息包含至少一种说服策略，72% 的可靠信息也包含
- 与虚假信息最相关的 4 种策略：攻击声誉、简化、转移注意力、操纵性措辞
- PCoT 甚至让 Llama 3.1 8B 超越 o1-mini 和 o3-mini 的零样本检测效果
- 长文章比短社媒帖子的提升更显著（18% vs 8%）
- DMT提示（含详细策略描述）比简单策略名列举提升约9%的检测F1
- 两阶段流水线比单阶段同时完成说服分析和检测的方案提升约7%，结构化推理更有效

## 亮点与洞察
- 将心理学研究成果（说服识别提升媒体素养）转化为 LLM 提示工程方法
- MultiDis 数据集的三轮专家标注流程设计严谨，可作为标注方法论参考
- 小模型 + PCoT 超越推理大模型（o3-mini），说明领域知识注入比模型规模更重要
- 说服策略分析提供了可解释的中间推理，增强了检测的透明度
- 后知识截止期数据集确保了评估不受预训练数据泄漏影响，设计严谨

## 局限与展望
- 依赖 LLM 的说服策略识别准确性，识别错误可能传播到检测阶段
- 两阶段推理增加了推理成本（每条文本需要两次 LLM 调用）
- 未探索多语言场景（仅评估英文）
- 社交媒体短帖的提升相对有限，可能需要额外的上下文信息
- 对抗性内容（故意规避说服模式的虚假信息）的鲁棒性未被充分评估
- 可探索多语言场景下说服策略识别的迁移性
- 与事实核查工具的结合可以进一步提升检测准确率

## 相关工作与启发
- **vs Z-CoT**: PCoT 通过结构化说服分析而非通用"逐步思考"指令引导推理
- **vs DeF-SpeC**: DeF-SpeC 强调演绎/归纳推理，PCoT 注入领域特定的说服知识
- **vs 监督 BERT**: PCoT 零样本表现接近或超越微调模型，且泛化性更强

## 评分
- 新颖性: ⭐⭐⭐⭐ 将说服理论引入 LLM 虚假信息检测是新颖角度
- 实验充分度: ⭐⭐⭐⭐⭐ 5 个 LLM、5 个数据集、多维分析
- 写作质量: ⭐⭐⭐⭐ 结构完整，实验设计严谨
- 价值: ⭐⭐⭐⭐ 对虚假信息检测和 LLM 提示工程都有实际价值

<!-- RELATED:START -->

## 相关论文

- [\[ICML 2025\] Towards Better Chain-of-Thought: A Reflection on Effectiveness and Faithfulness](quire_better_cot.md)
- [\[ICML 2025\] AdaDecode: Accelerating LLM Decoding with Adaptive Layer Parallelism](adadecode_accelerating_llm_decoding_with_adaptive_layer_parallelism.md)
- [\[ICML 2025\] Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](improving_rationality_in_the_reasoning_process_of_language_models_through_self-p.md)
- [\[ICML 2025\] Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](rethinking_external_slow-thinking_from_snowball_errors_to_probability_of_correct.md)
- [\[ICML 2025\] No Soundness in the Real World: On the Challenges of the Verification of Deployed Neural Networks](no_soundness_in_the_real_world_on_the_challenges_of_the_verification_of_deployed.md)

<!-- RELATED:END -->
