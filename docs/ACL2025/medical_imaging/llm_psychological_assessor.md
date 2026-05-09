---
title: >-
  [论文解读] Are LLMs Effective Psychological Assessors? Leveraging Adaptive RAG for Interpretable Mental Health Screening
description: >-
  [ACL 2025][心理健康筛查] 本文提出基于自适应RAG的心理问卷引导筛查框架，通过检索用户Reddit帖子并让LLM代替用户填写标准化心理问卷（BDI-II等），在无需训练数据的情况下匹配或超越SOTA监督方法的抑郁筛查性能，并扩展到其他心理健康状况。
tags:
  - ACL 2025
  - 心理健康筛查
  - 医学图像
  - 自适应RAG
  - 心理问卷
  - 社交媒体
---

# Are LLMs Effective Psychological Assessors? Leveraging Adaptive RAG for Interpretable Mental Health Screening

**会议**: ACL 2025  
**arXiv**: [2501.00982](https://arxiv.org/abs/2501.00982)  
**代码**: [https://github.com/Fede-stack/Adaptive-RAG-for-Psychological-Assessment](https://github.com/Fede-stack/Adaptive-RAG-for-Psychological-Assessment)  
**领域**: 医学图像  
**关键词**: 心理健康筛查, LLM评估, 自适应RAG, 心理问卷, 社交媒体

## 一句话总结
本文提出基于自适应RAG的心理问卷引导筛查框架，通过检索用户Reddit帖子并让LLM代替用户填写标准化心理问卷（BDI-II等），在无需训练数据的情况下匹配或超越SOTA监督方法的抑郁筛查性能，并扩展到其他心理健康状况。

## 研究背景与动机
1. **领域现状**：标准化心理问卷（如BDI-II）是心理健康评估的核心工具，社交媒体数据为大规模筛查提供了丰富来源。
2. **现有痛点**：(1)直接用LLM分类难以匹配监督方法；(2)黑盒分类缺乏可解释性；(3)传统问卷需要专业人员面对面施测，不可扩展。
3. **核心矛盾**：社交媒体语言与临床诊断标准之间存在语义鸿沟；LLM难以直接将非结构化文本映射到诊断类别。
4. **本文目标**：让LLM像心理评估员一样，通过填写标准化问卷来进行可解释的心理健康筛查。
5. **切入角度**：将复杂的诊断任务分解为结构化的问卷项目评估——每个问卷项目对应一个子任务。
6. **核心idea**：自适应RAG检索相关帖子 + LLM逐项填写心理问卷 + 标准化评分。

## 方法详解

### 整体框架
用户Reddit帖子集 → 对每个帖子和每个问卷项目选项计算嵌入 → 自适应检索最相关帖子 → LLM根据检索到的帖子预测问卷项目得分 → 汇总得分 → 严重程度分级。

### 关键设计
1. **自适应RAG**: 自动为每个问卷项目确定需要检索的最优帖子数量，适应内容的语义密度和相关性。

2. **问卷引导分解**: 将抑郁/自伤/饮食障碍/病态赌博等复杂诊断分解为标准化问卷的逐项评估，每项有临床验证的评分标准。

3. **多LLM对比**: 测试6种LLM（Qwen 2.5 70B、DeepSeek V3、Phi-3系列、Claude、GPT-4o-mini）在不同提示策略下的表现。

### 损失函数 / 训练策略
完全无监督，无需训练数据。使用eRisk 2019/2020数据集评估。

## 实验关键数据

| 方法 | BDI-II RMSE | 分类准确率 | 说明 |
|------|------------|-----------|------|
| SOTA监督方法 | 基线 | 基线 | 需训练数据 |
| **aRAG + LLM** | **匹配/超越** | **匹配/超越** | 零训练数据 |
| 直接LLM提示 | 差 | 差 | 无问卷引导 |

### 关键发现
- Qwen 2.5 70B在BDI-II RMSE上最低（约4.2），接近人类评估员水平。
- 自适应RAG比固定数量检索平均提升8.3%的预测准确率。
- 不同问卷项目的预测难度差异很大——与社交功能相关的项目最难预测。

### 跨病种评估

| 心理健康状况 | 问卷 | 最佳模型 | 最佳表现 |
|------------|------|---------|--------|
| 抑郁症 | BDI-II | Qwen 2.5 70B | 匹配SOTA |
| 自伤行为 | SIQ | Claude-3.5 | 超越SOTA |
| 饮食障碍 | EAT-26 | Claude-3.5 | 接近SOTA |
| 病态赌博 | SOGS | GPT-4o-mini | 接近SOTA |

- 问卷引导比直接提示LLM进行筛查效果显著更好。
- 无监督方法在BDI-II预测上匹配或超越需要训练数据的SOTA方法。
- 成功扩展到自伤、饮食障碍、病态赌博筛查，证明通用性。
- 闭源LLM（Claude、GPT-4o-mini）通常优于开源模型。

## 亮点与洞察
- **将临床评估实践引入计算方法**：不发明新指标，而是让AI使用人类已验证的临床工具——这种"工具复用"思路在AI临床应用中非常明智。
- **可解释性优势**：每个预测都可追溯到具体问卷项目和支持帖子，比黑盒分类更适合临床场景。
- **跨病种泛化**：只需更换问卷即可评估不同心理健康状况，展示了框架的通用性。
- **无监督匹配有监督**：在BDI-II预测上匹配或超越需要训练数据的SOTA方法，突破了无监督方法的性能上限。

## 局限与展望
- 虚拟评估员假设用户帖子充分反映心理状态，但用户可能选择性分享，导致信息不完整。
- 隐私和伦理问题需要关注——未经同意分析用户心理健康状态引发伦理争议。
- 问卷项目的语义可能与社交媒体语言不完全匹配，如临床术语与网络语言的语义鸿沟。
- eRisk数据集可能存在样本偏差，不完全代表更广泛的社交媒体用户群体。
- LLM对不同文化背景用户的心理状态理解可能有偏差（如东亚文化中抱怨的含蓄表达）。
- 问卷项目的固定评分范围（如BDI-II的0-3分）可能不足以捕捉微妙的心理状态变化。
- 未探索时序变化分析——用户心理状态可能随时间波动，单次评估可能不够。
- 闭源LLM（Claude、GPT-4o-mini）通常优于开源模型，但依赖闭源API引发可复现性和成本问题。

## 相关工作与启发
- **vs MENTALBERT/LMHS**: 这些有监督方法需要大量标注数据，aRAG方法完全无监督且可解释。
- **vs 直接提示LLM**: 直接让LLM判断用户是否抑郁效果很差；问卷引导分解显著提升性能。
- **vs 内容分析方法**: 传统方法用关键词匹配检测心理健康信号，aRAG通过语义理解捕捉更微妙的表达。
- **vs CLPsych共享任务**: 共享任务用序列分类，本文用问卷评分回归，提供了更细粒度的严重度评估。


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
- 长期评估和用户研究可以提供更全面的方法评价。
- 与人类专家的对比分析可以更好地定位方法的优劣势。
- 在对抗场景下的鲁棒性测试是实际部署前的必要步骤。
- 可解释性分析有助于理解方法成功和失败的原因。
- 多语言和多文化背景下的适用性值得关注。

## 评分
- 新颖性: ⭐⭐⭐⭐ 问卷引导LLM心理评估的思路新颖
- 实验充分度: ⭐⭐⭐⭐ 多LLM多问卷评估
- 写作质量: ⭐⭐⭐⭐ 研究问题清晰
- 价值: ⭐⭐⭐⭐⭐ 对数字心理健康有重要实用意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] Are LLMs Effective Psychological Assessors? Leveraging Adaptive RAG for Interpretable Mental Health Screening through Psychometric Practice](are_llms_effective_psychological_assessors_leveraging_adaptive_rag_for_interpret.md)
- [\[ACL 2025\] KokoroChat: A Japanese Psychological Counseling Dialogue Dataset Collected via Role-Playing by Trained Counselors](kokorochat_a_japanese_psychological_counseling_dialogue.md)
- [\[ACL 2025\] Improving Automatic Evaluation of LLMs in Biomedical Relation Extraction via LLMs-as-the-Judge](biore_llm_judge_evaluation.md)
- [\[ACL 2025\] Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications](omni_rag_medical.md)
- [\[ACL 2025\] AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](afrimed_qa_pan_african.md)

</div>

<!-- RELATED:END -->
