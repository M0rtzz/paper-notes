---
title: >-
  ACL2025 社会计算方向 23篇论文解读
description: >-
  23篇ACL2025 社会计算方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 👥 社会计算

**💬 ACL2025** · 共 **23** 篇

**[A Survey On Proactive Defense Strategies Against Misinformation In Large Languag](a_survey_on_proactive_defense_strategies_against_misinformation_in_large_languag.md)**

:   系统综述 LLM 主动防御错误信息的策略——提出"三支柱"框架：(1) 知识可信度（训练数据质量+知识编辑+RAG）, (2) 推理可靠性（自对齐+解码策略）, (3) 输入鲁棒性（对抗攻击防御+输入净化）。127 种技术的分类映射，48 项基准研究的元分析显示主动防御比传统检测方法提升 42-63%。

**[Banstereoset A Dataset To Measure Stereotypical Social Biases In Llms For Bangla](banstereoset_a_dataset_to_measure_stereotypical_social_biases_in_llms_for_bangla.md)**

:   构建 BanStereoSet，一个包含 1194 条填空式样本、覆盖 9 类偏见（种族/性别/宗教/职业/美貌/年龄/种姓/地区等）的孟加拉语刻板印象偏见数据集，用于评估多语言 LLM 在孟加拉语中的社会偏见，发现 GPT-4o 偏见最高，Mistral 最低。

**[Biasguard A Reasoning-Enhanced Bias Detection Tool For Large Language Models](biasguard_a_reasoning-enhanced_bias_detection_tool_for_large_language_models.md)**

:   提出 BiasGuard，通过显式推理公平性规范来检测 LLM 输出偏见：第一阶段用教师模型生成推理轨迹做 SFT 初始化，第二阶段用 DPO 强化推理质量，在 5 个数据集上超越分类器和 LLM-as-Judge 方法且降低过度公平误判。

**[Can Community Notes Replace Professional Fact-Checkers](can_community_notes_replace_professional_fact-checkers.md)**

:   通过大规模分析 Twitter/X 的 Community Notes 数据（66.4 万条），发现社区笔记对专业事实核查的依赖远超此前报告（至少 5-7%），证明高质量社区审核离不开专业事实核查，尤其在涉及阴谋论和更广泛虚假叙事的高风险内容上。

**[Conspiracy Theories And Where To Find Them On Tiktok](conspiracy_theories_and_where_to_find_them_on_tiktok.md)**

:   首个TikTok阴谋论系统性分析：通过官方API收集美国150万条长视频，利用标签富集和远程监督识别阴谋论内容（每月约1000条新视频），评估TikTok创作者激励计划的影响，并测试开源LLM（Llama3、Mistral、Gemma）在基于音频转录的阴谋论检测上的效果（精确率高达96%但整体水平与微调RoBERTa相当）。

**[Detection Of Human And Machine-Authored Fake News In Urdu](detection_of_human_and_machine-authored_fake_news_in_urdu.md)**

:   本文提出了乌尔都语四分类假新闻检测任务（人类假/人类真/机器假/机器真），构建了首个乌尔都语机器生成新闻数据集，并提出层次化检测方法将四分类分解为机器文本检测和假新闻检测两个子任务，在域内和跨域设置中均优于基线。

**[Explicit Vs Implicit Investigating Social Bias In Large Language Models Through ](explicit_vs_implicit_investigating_social_bias_in_large_language_models_through_.md)**

:   借鉴社会心理学中隐式联想测验（IAT）和自我报告评估（SRA），提出自反思评估框架系统研究 LLM 的显式和隐式偏见，发现 LLM 与人类一样存在显式-隐式偏见不一致——显式偏见轻微但隐式偏见强烈，且模型越大/对齐训练越多，这种不一致越严重。

**[Exploring Multimodal Challenges In Toxic Chinese Detection Taxonomy Benchmark An](exploring_multimodal_challenges_in_toxic_chinese_detection_taxonomy_benchmark_an.md)**

:   这篇工作把中文毒性文本中的“形、音、义混合扰动”系统化为 3 类 8 种策略，构建了大规模扰动基准 CNTP，并证明当前中美主流 LLM 在这类中文多模态毒性检测上都明显不稳，而小样本 ICL / SFT 虽能抬高检出率，却容易把正常内容一起误杀。

**[Exploring The Impact Of Instruction-Tuning On Llms Susceptibility To Misinformat](exploring_the_impact_of_instruction-tuning_on_llms_susceptibility_to_misinformat.md)**

:   首次系统研究指令微调如何影响 LLM 对虚假信息的易感性，发现指令微调使模型从偏信 assistant-role 转变为偏信 user-role，当虚假信息以独立 user-turn 呈现时易感性最高，揭示了指令微调的"副作用"。

**[Fairsteer Inference Time Debiasing For Llms With Dynamic Activation Steering](fairsteer_inference_time_debiasing_for_llms_with_dynamic_activation_steering.md)**

:   提出 FairSteer，一种推理时去偏框架，通过轻量线性分类器检测激活中的偏见信号，再用对比 prompt 对计算的去偏转向向量（DSV）动态调整隐藏层激活，无需重训即可在多任务上有效缓解 LLM 的社会偏见。

**[Gg-Bbq German Gender Bias Benchmark For Question Answering](gg-bbq_german_gender_bias_benchmark_for_question_answering.md)**

:   将英语BBQ偏见基准数据集的性别子集翻译为德语，经人工审校后创建GG-BBQ德语性别偏见评估基准，揭示了机器翻译在性别偏见评估数据集构建中的局限性，并评估了多个德语LLM的偏见表现。

**[Hateday Global Hate Speech](hateday_global_hate_speech.md)**

:   HateDay 构建了首个全球代表性仇恨言论数据集——24 万条随机采样的 Twitter 推文覆盖 8 种语言和 4 个英语国家，揭示了学术数据集大幅高估了检测模型在真实场景中的表现，尤其对非欧洲语言检测能力极差。

**[How Does Misinformation Affect Large Language](how_does_misinformation_affect_large_language.md)**

:   构建了目前最大的误信息评估基准 MisBench（1034 万条误信息），从知识冲突类型和文本风格两个维度系统分析 LLM 对误信息的行为和偏好，并提出 RtD 方法结合外部知识源提升误信息检测能力。

**[Implihatevid Video Hate](implihatevid_video_hate.md)**

:   首次提出视频中隐性仇恨言论检测任务，构建2009个视频的ImpliHateVid数据集，并设计两阶段对比学习框架融合文本、图像、音频三模态特征。

**[Is Llm An Overconfident Judge Unveiling The Capabilities Of Llms In Detecting Of](is_llm_an_overconfident_judge_unveiling_the_capabilities_of_llms_in_detecting_of.md)**

:   系统评估了多个 LLM 在攻击性语言检测中面对标注分歧时的表现，发现 LLM 在标注者高度一致的样本上表现优异（GPT-4o F1 85.24%）但在低一致度样本上骤降至 57.06%，且模型对不确定样本表现出严重的过度自信；进一步通过 few-shot 和指令微调实验证明，在训练中引入分歧样本可同时提升检测准确率和人-AI 对齐度。

**[Llm Label Propagation](llm_label_propagation.md)**

:   提出 GLPN-LLM 框架，通过 mask-based 全局标签传播机制有效整合 LLM 生成的伪标签，解决了 LLM 伪标签直接组合效果不佳的问题，在 Twitter/PHEME/Weibo 三个数据集上全面超越 SOTA。

**[Llm Personalized Disinformation](llm_personalized_disinformation.md)**

:   系统评估了 6 个主流 LLM 生成个性化虚假信息的能力，发现大多数 LLM 能生成高质量个性化虚假新闻，且个性化请求反而降低了安全过滤器的触发率（相当于一种 jailbreak），同时轻微降低了机器生成文本的可检测性。

**[Mdit-Bench Evaluating The Dual-Implicit Toxicity In Large Multimodal Models](mdit-bench_evaluating_the_dual-implicit_toxicity_in_large_multimodal_models.md)**

:   提出"双模态隐式毒性"(dual-implicit toxicity)概念——仅当结合图文两个模态时才能被识别的偏见与歧视，构建了包含317K问题、12类23子类的MDIT-Bench基准，并通过长上下文越狱揭示了主流多模态大模型中大量可被激活的隐藏毒性。

**[Measuring Social Biases In Masked Language Models By Proxy Of Prediction Quality](measuring_social_biases_in_masked_language_models_by_proxy_of_prediction_quality.md)**

:   提出了注意力加权的预测质量代理度量 Δpa 和 CRRA，在迭代掩码实验（IME）下评估 MLM 的社会偏见，并引入模型比较函数 BSRT 来估计重训练引入的偏见，发现所提方法比 CSPS、AUL、AULA 等现有方法更准确、更敏感。

**[Silencing Empowerment Allowing Bigotry Auditing The Moderation Of Hate Speech On](silencing_empowerment_allowing_bigotry_auditing_the_moderation_of_hate_speech_on.md)**

:   对 Twitch 平台的自动化内容审核工具 AutoMod 进行大规模审计，发送超过 10.7 万条消息，发现 AutoMod 在最严格设置下仅能标记 22% 的仇恨内容，高度依赖侮辱性词汇作为检测信号，同时错误屏蔽高达 89.5% 的教育性/赋权性内容。

**[State Toxicn A Benchmark For Span-Level Target-Aware Toxicity Extraction In Chin](state_toxicn_a_benchmark_for_span-level_target-aware_toxicity_extraction_in_chin.md)**

:   构建了首个中文 span 级仇恨言论检测数据集 STATE ToxiCN（8029 条帖子、9533 个四元组标注），提出 Target-Argument-Hateful-Group 四元组标注体系，并首次建立了中文仇恨俚语标注词典（830 条），系统评估了多种 LLM 在 span 级中文仇恨言论检测上的能力。

**[Taz2024Full Analysing German Newspapers For Gender Bias And Discrimination Acros](taz2024full_analysing_german_newspapers_for_gender_bias_and_discrimination_acros.md)**

:   本文发布了 taz2024full——迄今最大的公开德语报纸语料库（180 万篇文章，1980-2024 年），并通过可扩展的分析管道展示了四十多年来德语新闻报道中性别表征的演变趋势。

**[Translate With Care Addressing Gender Bias Neutrality And Reasoning In Large Lan](translate_with_care_addressing_gender_bias_neutrality_and_reasoning_in_large_lan.md)**

:   提出 Translate-with-Care (TWC) 数据集（3,950 条跨 6 种无性别语言的翻译挑战），系统揭示 GPT-4、Google Translate 等模型在无性别→有性别语言翻译中的性别偏见和推理错误，并通过微调 mBART-50 在偏见消除和翻译准确率上大幅超越闭源 LLM。
