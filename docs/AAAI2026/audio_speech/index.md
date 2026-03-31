<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎵 音频/语音

**🤖 AAAI2026** · 共 **13** 篇

**[DeepDebater: A Superpersuasive Autonomous Policy Debating System](a_superpersuasive_autonomous_policy_debating_system.md)**

:   提出 DeepDebater，首个能参与并赢得完整美式政策辩论赛的自主多 Agent 系统——层级式 Agent 工作流分工完成论证构建（正方 Advantage/反方 DA+CP+K），基于 OpenDebateEvidence 300 万张证据卡做检索增强，辅以 GPT-4o TTS 语音合成和 EchoMimic 数字人动画，在专家评估和模拟对局中全面超越人类编写的案例。

**[AHAMask: Reliable Task Specification for Large Audio Language Models without Instructions](ahamask_reliable_task_specification_for_large_audio_language.md)**

:   通过对大音频语言模型（LALM）Transformer 骨干中的注意力头进行二值掩码（AHAMask），无需文本指令即可可靠触发特定声学任务功能，同时揭示了 LALM 内部存在"声学功能通路"。

**[Aligning Generative Music AI with Human Preferences: Methods and Challenges](aligning_generative_music_ai_with_human_preferences_methods_and_challenges.md)**

:   综述/立场论文，系统梳理偏好对齐技术在音乐生成中的三条路线——MusicRL（大规模 RLHF，~30 万偏好对）、DiffRhythm+（扩散模型多偏好 DPO）、Text2midi-InferAlign（推理时树搜索，CLAP +29.4%），深入分析音乐领域独有的对齐挑战（多尺度时间连贯性、和声一致性、文化主观性、评估悖论），并给出未来路线图。

**[Cross-Space Synergy: A Unified Framework for Multimodal Emotion Recognition in Conversation](cross-space_synergy_a_unified_framework_for_multimodal_emotion_recognition_in_co.md)**

:   提出 Cross-Space Synergy（CSS）框架，通过表示空间的协同多项式融合（SPF）和梯度空间的 Pareto 梯度调节器（PGM）双管齐下，同时解决多模态对话情感识别中融合表达力不足和多目标梯度冲突两大难题。

**[DeformTrace: A Deformable State Space Model with Relay Tokens for Temporal Forgery Localization](deformtrace_a_deformable_state_space_model_with_relay_tokens_for_temporal_forger.md)**

:   提出 DeformTrace，将可变形动态感受野和中继令牌机制引入状态空间模型，结合 Transformer 的全局建模与 SSM 的高效推理，实现时序伪造定位的 SOTA 精度与显著效率提升。

**[Do LLMs Feel? Teaching Emotion Recognition with Prompts, Retrieval, and Curriculum Learning](do_llms_feel_teaching_emotion_recognition_with_prompts_retrieval_and_curriculum_.md)**

:   提出 PRC-Emo 框架，通过显式/隐式情感提示、专用检索库和课程学习策略三位一体地提升 LLM 在对话情感识别（ERC）任务上的表现，在 IEMOCAP 和 MELD 两个基准上取得 SOTA。

**[DualSpeechLM: Towards Unified Speech Understanding and Generation via Dual Speech Token Modeling](dualspeechlm_towards_unified_speech_understanding_and_generation_via_dual_speech.md)**

:   提出 DualSpeechLM 框架，通过理解驱动语音分词器（USTokenizer）提取高层语义 token 作为 LLM 输入、声学 token 作为输出，在一个端到端框架中同时优化语音理解和生成能力。

**[End-to-end Contrastive Language-Speech Pretraining Model For Long-form Spoken Question Answering](end-to-end_contrastive_language-speech_pretraining_model_for_long-form_spoken_qu.md)**

:   提出 CLSR，一种端到端对比式语言-语音检索器，通过将声学表示先转换为 text-like representation 再与文本对齐，高效地从长音频中提取与问题相关的片段，为下游 LALM 的长语音问答提供 RAG 支持。

**[Generalizing Analogical Inference from Boolean to Continuous Domains](generalizing_analogical_inference_from_boolean_to_continuous_domains.md)**

:   从基础理论层面重新审视类比推理：首先构造反例证明布尔域上经典泛化界失效，然后提出基于参数化广义均值的统一类比推理框架，将离散分类扩展到连续回归域。

**[GOMPSNR: Reflourish the Signal-to-Noise Ratio Metric for Audio Generation Tasks](gompsnr_reflourish_the_signal-to-noise_ratio_metric_for_audio_generation_tasks.md)**

:   通过引入全方位相位导数（omnidirectional phase derivatives）替换瞬时相位来重构 SNR 指标，提出 GOMPSNR 作为更可靠的音频质量评估指标，并衍生出一系列新的损失函数显著提升神经声码器性能。

**[Hearing More with Less: Multi-Modal Retrieval-and-Selection Augmented Conversational LLM-Based ASR](hearing_more_with_less_multi-modal_retrieval-and-selection_augmented_conversatio.md)**

:   提出多模态检索与选择方法 MARS，从对话历史中检索并筛选与当前语音最相关的上下文，仅用 1.5K 小时训练数据即超越使用 179K 小时数据的 SOTA 系统。

**[Hpsu A Benchmark For Human-Level Perception In Real-World Spoken Speech Understa](hpsu_a_benchmark_for_human-level_perception_in_real-world_spoken_speech_understa.md)**

:   提出 HPSU 基准，包含 20,000+ 中英文专家标注样本和 16 项任务，系统评估 Speech LLM 在真实口语场景下的深层感知与推理能力，发现最强模型（Gemini 2.5 Pro，62.6%）与人类表现（87.3%）仍有巨大差距。

**[Let the Model Learn to Feel: Mode-Guided Tonality Injection for Symbolic Music Emotion Recognition](let_the_model_learn_to_feel_mode-guided_tonality_injection_f.md)**

:   通过 MoGE 诊断策略系统发现 MIDIBERT 未有效编码调式-情感关联，提出 MoFi 注入框架通过 FiLM 机制将大调/小调先验注入 MIDIBERT 第 1 层（诊断确定的最弱情感信息层），在 EMOPIA 上准确率 75.2%（+11.8%），VGMIDI 上 59.1%（+11.8%），F1 提升 12.3%/15.5%。
