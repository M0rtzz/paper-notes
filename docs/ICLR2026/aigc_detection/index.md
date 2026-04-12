---
title: >-
  ICLR2026 AIGC检测方向 5篇论文解读
description: >-
  5篇ICLR2026 AIGC检测方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔎 AIGC检测

**🔬 ICLR2026** · 共 **5** 篇

**[Calibrating Verbalized Confidence With Self-Generated Distractors](calibrating_verbalized_confidence_with_self-generated_distractors.md)**

:   提出 DiNCo（Distractor-Normalized Confidence）方法，让 LLM 自动生成"合理但错误"的干扰选项，然后在干扰选项集合上归一化置信度分数，实现跨难度级别的置信度校准，在 TriviaQA 上以 95.2% 均衡准确率和仅 3.5% 人类介入率实现可靠的自动决策。

**[Clarc Cc Benchmark For Robust Code Search](clarc_cc_benchmark_for_robust_code_search.md)**

:   构建首个可编译的 C/C++ 代码检索基准 CLARC（6717 查询-代码对），自动化 pipeline 从 GitHub 提取代码并用 LLM+假设检验生成/验证查询；覆盖标准/匿名化/汇编/WebAssembly 四种检索场景，揭示现有代码嵌入模型过度依赖词汇特征（匿名化后 NDCG@10 从 0.89 降至 0.67）且在二进制级别检索上严重不足。

**[Death Of The Novelty Beyond N-Gram Novelty As A Metric For Textual Creativity](death_of_the_novelty_beyond_n-gram_novelty_as_a_metric_for_textual_creativity.md)**

:   通过 26 位专业作家对 8618 条表达的 close reading 标注，揭示 n-gram 新颖度不足以衡量文本创造力——约 91% 的高 n-gram 新颖表达并不被认为具有创造性，且开源 LLM 中高 n-gram 新颖度与低语用合理性负相关。

**[Dmap A Distribution Map For Text](dmap_a_distribution_map_for_text.md)**

:   提出 DMAP，将文本通过语言模型的 token 概率映射到 [0,1] 单位区间上的样本，理论证明纯采样文本产生均匀分布，由此可用统计检验分析生成参数（如 top-k）、检测机器生成文本、揭示后训练的统计指纹。

**[Policon Evaluating Llms On Achieving Diverse Political Consensus Objectives](policon_evaluating_llms_on_achieving_diverse_political_consensus_objectives.md)**

:   基于欧洲议会2009-2022年2225条高质量审议记录构建PoliCon基准，评估LLM在不同投票机制、权力结构和政治目标下起草共识决议的能力。结果显示前沿模型在简单多数任务表现尚可，但在2/3多数和安全议题上显著不足。
