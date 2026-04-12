---
title: >-
  ACL2025 AIGC检测方向 11篇论文解读
description: >-
  11篇ACL2025 AIGC检测方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔎 AIGC检测

**💬 ACL2025** · 共 **11** 篇

**[A Rose By Any Other Name Llm-Generated Explanations Are Good Proxies For Human E](a_rose_by_any_other_name_llm-generated_explanations_are_good_proxies_for_human_e.md)**

:   研究 LLM 生成的解释能否替代昂贵的人工解释来近似 NLI 的人工判断分布（HJD）——发现在提供人工标签的条件下，LLM 生成的解释与人工解释在近似 HJD 方面效果相当（"名字不重要，玫瑰依然芬芳"），且方法可推广到无人工解释的数据集和域外测试集。

**[Aigt Social Media Monitoring](aigt_social_media_monitoring.md)**

:   首次大规模量化社交媒体上 AI 生成文本(AIGT)的占比变化——收集 Medium/Quora/Reddit 上 240 万帖子，构建 AIGTBench 训练最佳检测器 OSM-Det，发现 2022-2024 年间 Medium 和 Quora 的 AIGT 占比从~2% 飙升至~37-39%，而 Reddit 仅从 1.3% 增至 2.5%。

**[Chatgpt User Ai Text Detection](chatgpt_user_ai_text_detection.md)**

:   通过 1,740 条标注实验发现，经常使用 LLM 进行写作任务的人类标注者可以极高精度（5人投票仅错 1/300）检测 AI 生成文本，即使面对改写和人性化逃逸策略也显著优于大多数自动检测器。

**[Greater Adversarial Mgt Detection](greater_adversarial_mgt_detection.md)**

:   提出 GREATER 对抗训练框架，同步训练对抗攻击器（Greater-A）和 MGT 检测器（Greater-D），对抗器通过代理模型梯度识别关键 token 并在嵌入空间扰动生成对抗样本，检测器从课程式对抗样本中学习泛化防御，在 16 种攻击下 ASR 降至 5.53%（SOTA 为 6.20%），攻击效率比 SOTA 快 4 倍。

**[Haco-Det A Study Towards Fine-Grained Machine-Generated Text Detection Under Hum](haco-det_a_study_towards_fine-grained_machine-generated_text_detection_under_hum.md)**

:   提出人机共创场景下的细粒度MGT检测任务和数据集HACo-Det，通过多轮LLM改写构建了11,200篇带词级别标注的共创文本，将7种主流检测器适配到词级/句级任务后发现：微调方法（DeBERTa）远优于基于度量的方法，但整体检测水平仍远未解决该问题。

**[Learning To Rewrite Generalized Llm-Generated Text Detection](learning_to_rewrite_generalized_llm-generated_text_detection.md)**

:   提出Learning2Rewrite（L2R）框架，通过微调LLM的改写模型来放大人写文本和AI生成文本在改写编辑距离上的差异，从而实现跨领域高度泛化的AI文本检测——在21个独立领域上平均AUROC达0.9009，域外测试超越RAIDAR达4.67%、超越直接分类微调达51.35%。

**[Llm Vs Human Formal Syntax](llm_vs_human_formal_syntax.md)**

:   首次使用形式句法理论（HPSG）系统比较六个 LLM 生成的纽约时报风格文本与真实人类撰写的 NYT 文本，发现 LLM 和人类写作在 HPSG 语法类型分布上存在系统性差异，揭示了 LLM 句法行为与人类的本质不同。

**[Low-Perplexity Llm-Generated Sequences And Where To Find Them](low-perplexity_llm-generated_sequences_and_where_to_find_them.md)**

:   提出系统化 pipeline 分析 LLM 生成的低困惑度序列（token 预测概率 ≥0.9）并追溯到训练数据来源，发现 30-60% 的低困惑度片段无法匹配训练数据，将可匹配片段分为四种记忆行为类别。

**[Multisocial Mgt Detection](multisocial_mgt_detection.md)**

:   构建首个多语言(22种语言)、多平台(5个社交媒体)、多生成器(7个LLM)的社交媒体机器生成文本检测基准 MultiSocial（47万文本），填补了社交媒体短文本+非英语场景下 MGT 检测研究的空白，发现微调检测器可在社交媒体文本上有效训练且训练平台选择很重要。

**[Reliably Bounding False Positives A Zero-Shot Machine-Generated Text Detection F](reliably_bounding_false_positives_a_zero-shot_machine-generated_text_detection_f.md)**

:   提出基于多尺度保形预测（MCP）的零样本机器生成文本检测框架，通过文本长度感知的分组分位数计算，在严格约束假阳性率（FPR）上界的同时显著提升检测性能，并构建了覆盖15个领域、22个LLM的大规模双语基准数据集RealDet。

**[Who Writes What Ai Detection](who_writes_what_ai_detection.md)**

:   揭示作者的社会语言学属性（性别、CEFR水平、学科领域、语言环境）会系统性地影响AI生成文本检测器的准确率，其中语言水平和语言环境的偏差最为显著且一致，提出了基于多因素WLS+ANOVA的偏差量化框架。
