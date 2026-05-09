---
title: >-
  [论文解读] LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News
description: >-
  [ICLR 2026][LLM Agent][LLM Web Search] 提出 LiveNewsBench，一个定期更新的、基于新鲜新闻事件自动生成 QA 对的基准，用于评估 LLM 代理式网页搜索能力，有效隔离了模型内部记忆与真实搜索能力。
tags:
  - ICLR 2026
  - LLM Agent
  - LLM Web Search
  - Benchmark
  - Agentic Search
  - 新闻问答
  - 多跳搜索
---

# LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News

**会议**: ICLR 2026  
**arXiv**: [2602.13543](https://arxiv.org/abs/2602.13543)  
**代码**: [livenewsbench.com](https://livenewsbench.com)  
**领域**: LLM Agent  
**关键词**: LLM Web Search, Benchmark, Agentic Search, 新闻问答, 多跳搜索  

## 一句话总结

提出 LiveNewsBench，一个定期更新的、基于新鲜新闻事件自动生成 QA 对的基准，用于评估 LLM 代理式网页搜索能力，有效隔离了模型内部记忆与真实搜索能力。

## 研究背景与动机

当前评估 LLM 搜索能力面临一个核心困难：**如何将外部搜索的贡献与模型内部记忆的世界知识区分开来**。由于 SOTA LLM 在海量文本上预训练，它们已经编码了大量事实知识。当基准使用静态问题时，模型可能仅靠记忆就能正确回答，而非真正依赖搜索。

现有基准的三大缺陷：

1. **学术推理基准**（如 HLE）：主要测量领域知识和推理能力，而非搜索行为本身。例如 GPT-5 启用搜索后在 HLE 上仅从 24.8% 提升到 30.7%
2. **静态事实 QA 基准**（如 SimpleQA、BrowseComp、TriviaQA）：模型无需搜索即可达到高准确率（SimpleQA 62.5%，TriviaQA 82.9%），无法有效评估搜索能力
3. **时间敏感 QA 基准**（如 FreshQA、SealQA）：虽然答案会变化，但问题固定不变，强模型常通过推理或部分记忆就能回答
4. **Deep Research 基准**：使用主观评价标准（完整性、洞察力等），缺乏可验证的事实性答案

## 方法详解

### 整体框架

LiveNewsBench 的自动化数据构建流程包含两个主要组件：

1. **新闻文章检索**：从 Wikipedia 当前事件存档获取种子新闻事件，通过搜索引擎检索相关文章
2. **QA 对生成**：从文章集群中生成问答对，经过自动化和人工验证

### 关键设计

**新闻检索流程**：

- 从 Wikipedia Current Events Archive 收集全球重大新闻事件作为种子
- 用 GPT-4.1 将事件摘要改写为搜索查询
- 通过 Brave Search API 检索相关新闻 URL，限制约 100 家知名媒体的白名单
- 设定 14 天时间窗口（事件前 3 天到后 11 天）
- 通过 archive.today 下载存档版本确保稳定性和可重现性
- 用 GPT-4.1 验证文章与事件的相关性，过滤后每个事件平均 5.3 篇文章

**QA 对生成与验证**：

- 使用 GPT-5.1 Thinking 从文章集群生成 QA 对，要求引用多篇文章（多跳）
- **自一致性过滤**：将问题和文章独立提供给 GPT-5.1 推导答案，仅保留两次答案一致的 QA 对
- **指南遵守验证**：用改写后的指南再次请 GPT-5.1 验证 QA 对是否符合所有标准
- **人工验证子集**：原作者审核 QA 对，约拒绝 15% 通过自动验证的样本；独立 NLP 研究者验证达 92% 一致率

**数据划分**：基于新闻事件日期进行时间序列划分——过去两个月为测试集（340 样本），第三个月为验证集（170 样本），更早的为训练集（600+）。人工验证子集包含 200 个样本。

### 评估框架

采用自定义 ReAct 风格代理框架，支持三种动作：

- **Search**：发出搜索查询，返回 top-10 结果（标题、URL、摘要）
- **Visit**：访问搜索结果中的网页，返回全文
- **Finish & Answer**：产出最终答案

标准配置：最多 5 次搜索查询、5 次网页访问。

## 实验关键数据

### 主实验：无互联网对比

| 模型 | LiveNewsBench (%) | FreshQA (%) | SealQA-Hard (%) |
|------|:-:|:-:|:-:|
| GPT-5.2 | 21.5 | 72.2 | 31.9 |
| Gemini 3 Pro | 20.5 | 74.3 | 46.5 |
| GPT-4.1 | 14.0 | 65.7 | 26.8 |
| Claude 4.5 Sonnet | 13.0 | 70.8 | 23.2 |
| DeepSeek V3.2 Thinking | 10.0 | 61.0 | 31.5 |

SOTA 模型在 FreshQA/SealQA 上无搜索即可达到 60-74% 准确率，但在 LiveNewsBench 上仅 10-21.5%，说明本基准有效抵抗记忆化。

### 搜索代理评估（人工验证测试集）

| 方法 | 推理模型 | 搜索次数 | 访问次数 | 准确率 |
|------|:-:|:-:|:-:|:-:|
| DeepSeek V3.2 Thinking | ✓ | 3.3±1.3 | 2.6±1.4 | **84.5%** |
| DeepSeek V3.2 (No Think) | ✗ | 3.4±1.2 | 2.6±1.3 | 83.0% |
| Claude Sonnet 4.5 | ✗ | 2.9±1.1 | 1.3±1.3 | 82.0% |
| GPT-5.2 | ✓ | 2.9±1.1 | 1.8±1.3 | 74.0% |
| GPT-5.2 Official API | ✓ | N/A | N/A | **90.0%** |
| Llama 3.1 8B | ✗ | 3.9±1.1 | 0.3±1.0 | 11.0% |

### 消融实验：搜索预算影响

| 模型 | Budget=1 | Budget=3 | Budget=5 | Budget=7 | 提升(1→7) |
|------|:-:|:-:|:-:|:-:|:-:|
| DeepSeek V3.2 Thinking | 48.5% | 80.5% | 84.5% | 84.5% | +36.0% |
| DeepSeek V3.2 (No Think) | 20.0% | 79.0% | 83.0% | 84.5% | +64.5% |
| Claude Sonnet 4.5 | 53.5% | 79.0% | 82.0% | 67.0% | +13.5% |
| GPT-5.2 | 62.5% | 72.5% | 74.0% | 74.5% | +12.0% |

### 关键发现

1. **记忆化有限**：关闭搜索后准确率下降 17%-74.5%（绝对值），证明基准对搜索能力的有效测量
2. **多跳特性明确**：搜索预算从 1 增到 7 时，所有模型均有显著提升，开源模型受益更大
3. **工具调用能力影响显著**：Kimi K2 Thinking 44% 的样本无法正确调用搜索工具，而 Claude/DeepSeek 仅 0.5%
4. **模型更依赖搜索摘要而非全文**：所有模型搜索次数均超过网页访问次数
5. **搜索实现影响性能**：GPT-5.2 官方 API 比本地框架高 16%，但 Claude API 反而低 42%

## 亮点与洞察

- **自动化管线的可扩展性**：整个构建成本约 $700，承诺每季度更新，解决了传统基准依赖人工标注的瓶颈
- **记忆-搜索解耦**：通过使用训练截止日期之后的新闻事件，有效分离了模型内部知识和搜索行为
- **强区分度**：准确率范围从 11% 到 90%，对不同模型和搜索框架有很强的区分力
- **训练数据潜力**：提供大规模开源训练集，适合用 RLVR 训练代理式搜索模型

## 局限性 / 可改进方向

1. 尽管使用新鲜新闻，SOTA 模型仍可通过世界知识和推理猜对部分问题（3.5%-21.5%），完全消除记忆化仍困难
2. 仅关注简短事实性答案，未覆盖需要长篇研究报告的场景
3. 依赖 Wikipedia Current Events Archive 作为种子，可能遗漏非重大但有评估价值的事件
4. 评估成本仍然较高（需调用搜索 API 和 LLM），限制了大规模评估
5. 未来计划扩展到时间敏感问题（答案随事件发展而变化）

## 相关工作与启发

- **与 RealTimeQA 的区别**：RealTimeQA 虽也定期更新，但每次仅约 10 个样本且来自手动策划
- **与 BrowseComp 的互补**：BrowseComp 是静态的但测试浏览能力，LiveNewsBench 是动态的但测试搜索能力
- **对 RLVR 训练的启发**：提供的大规模训练集可用于训练代理式搜索模型的强化学习
- **搜索代理设计启示**：不同模型在工具调用可靠性上差异巨大，这是搜索代理性能的重要瓶颈

## 评分

- **新颖性**: ⭐⭐⭐⭐ — 首个同时满足定期更新、自动化生成、抗记忆化、客观评估的搜索基准
- **技术深度**: ⭐⭐⭐ — 管线设计精巧但技术贡献偏工程
- **实验充分度**: ⭐⭐⭐⭐⭐ — 覆盖 13 个模型、多种搜索预算、全面消融分析
- **写作质量**: ⭐⭐⭐⭐ — 结构清晰，实验呈现详尽
- **实用性**: ⭐⭐⭐⭐⭐ — 填补了搜索评估的重要空白，对社区有直接价值
- **综合评分**: ⭐⭐⭐⭐ (8/10)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains](mc-search_evaluating_and_enhancing_multimodal_agentic_search_with_structured_lon.md)
- [\[ICLR 2026\] ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](st-webagentbench_a_benchmark_for_evaluating_safety_and_trustworthiness_in_web_ag.md)
- [\[ICLR 2026\] OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](openagentsafety_a_comprehensive_framework_for_evaluating_real-world_ai_agent_saf.md)
- [\[ICLR 2026\] FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](fingertip_20k_a_benchmark_for_proactive_and_personalized_mobile_llm_agents.md)
- [\[ICLR 2026\] Judge Reliability Harness: Stress Testing the Reliability of LLM Judges](judge_reliability_harness_stress_testing_the_reliability_of_llm_judges.md)

</div>

<!-- RELATED:END -->
