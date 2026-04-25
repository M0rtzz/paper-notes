---
title: >-
  ACL2026 音频/语音方向 21篇论文解读
description: >-
  21篇ACL2026 音频/语音论文解读，主题涵盖：本文提出 Affectron 框架、首次全面探索Mamba架构作为语音自监督学习（SS、形式化定义 RAG 系统的"软失败"威胁（生成流畅等，每篇含核心思想与方法详解。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎵 音频/语音

**💬 ACL2026** · **21** 篇论文解读

**[Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations](affectron_emotional_speech_synthesis_with_affective_and_contextually_aligned_non.md)**

:   本文提出 Affectron 框架，通过情感驱动的 Top-K NV 匹配和情感感知的 Top-K 路由两个训练时增强策略，在小规模开源解耦语料上实现了多样且情感对齐的非语言发声（如笑声、叹息）合成，显著超越了基于纯语言预训练的 VoiceCraft 基线。

**[An Exploration of Mamba for Speech Self-Supervised Models](an_exploration_of_mamba_for_speech_self-supervised_models.md)**

:   首次全面探索Mamba架构作为语音自监督学习（SSL）基础模型的潜力，发现Mamba-based HuBERT在长上下文ASR、流式ASR和因果设置的probing任务中优于Transformer，同时保持线性时间复杂度。

**[Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](beyond_explicit_refusals_soft-failure_attacks_on_retrieval-augmented_generation.md)**

:   形式化定义 RAG 系统的"软失败"威胁（生成流畅但无信息量的回答），提出 DEJA 黑箱进化攻击框架，通过对抗性文档诱导模型利用安全对齐机制产生模棱两可的回答，SASR 超过 79% 且高度隐蔽。

**[Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](beyond_transcription_unified_audio_schema_for_perception-aware_audiollms.md)**

:   揭示当前 AudioLLM 的感知弱点源于 ASR 中心的训练范式（系统性抑制副语言和非语言信息），提出 Unified Audio Schema（UAS）将音频信息结构化为转录、副语言和非语言事件三个维度的 JSON 格式，在 MMSU 基准上感知精度提升 10.9% 同时保持推理能力。

**[Computational Narrative Understanding for Expressive Text-to-Speech](computational_narrative_understanding_for_expressive_text-to-speech.md)**

:   本文从有声书虚构作品中提取角色直接引语，构建了大规模表达性语音数据集 LibriQuote（5.3K 小时引语 + 12.7K 小时叙述），并用语音动词和副词伪标签标注说话风格，实验表明在 flow-matching 模型上微调可同时提升表达性和可懂度，且 LibriQuote-test 构成了一个具有挑战性的表达性 TTS 基准。

**[Curing "Miracle Steps" in LLM Mathematical Reasoning with Rubric Rewards](curing_miracle_steps_in_llm_mathematical_reasoning_with_rubric_rewards.md)**

:   本文发现当前 LLM 数学推理中存在大量"Miracle Steps"——推理链中凭空跳跃到正确答案的现象，并提出 Rubric Reward Model (RRM)，一种基于问题特定评分标准的过程奖励函数，在 RL 训练中显著减少 Miracle Steps 71% 并将 AIME2024 的 Verified Pass@1024 从 26.7% 提升至 62.6%。

**[Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models](do_we_need_distinct_representations_for_every_speech_token_unveiling_and_exploit.md)**

:   本文通过逐层oracle干预实验揭示了大语音语言模型（LSLM）中语音token表示的结构化冗余层次——浅层编码必要声学细节而深层极度冗余——并提出Affinity Pooling这一免训练的基于相似度的token合并机制，在减少27.48% FLOPs的同时保持竞争力的准确率。

**[SEPT: Semantically Expanded Prompt Tuning for Audio-Language Models](generalizable_prompt_tuning_for_audio-language_models_via_semantic_expansion.md)**

:   SEPT 通过利用 LLM 生成语义邻居并设计带边距约束的语义扩展损失来正则化提示嵌入空间，显著缓解了音频语言模型（ALM）提示调优中的 Base-New Tradeoff 问题，建立了 ALM 提示泛化的首个系统性评估基准。

**[HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](halluaudio_a_comprehensive_benchmark_for_hallucination_detection_in_large_audio-.md)**

:   本文提出 HalluAudio，首个大规模跨领域（语音/环境声/音乐）的音频幻觉检测基准，包含 5000+ 人工验证的 QA 对和系统化的对抗性提示设计，通过多维指标（准确率/幻觉率/Yes-No偏差/拒绝率/错误类型）评估主流 LALM，揭示了当前模型在声学锚定、时间推理和音乐属性理解方面的显著缺陷。

**[Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages](hard_to_be_heard_phoneme-level_asr_analysis_of_phonologically_complex_low-resour.md)**

:   本文对两种音系极端复杂的低资源濒危东高加索语言（Archi和Rutul）进行音素级ASR分析，发现音素识别准确率与训练频率呈S型学习曲线关系，许多归因于音系复杂性的错误实际上更多源于数据稀缺。

**[How Hypocritical Is Your LLM Judge? Listener–Speaker Asymmetries in the Pragmatic Competence of Large Language Models](how_hypocritical_is_your_llm_judge_listener-speaker_asymmetries_in_the_pragmatic.md)**

:   本文通过三个语用任务（虚假预设、反预设、演绎推理）系统对比 14 个 LLM 作为"语用听者"（判断语用适当性）和"语用说者"（生成语用适当的语言）的表现，发现普遍存在的听者-说者不对称：多数模型作为判断者远优于生成者，且项目级分析表明正确判断不能可靠预测成功生成。

**[Jamendo-MT-QA: A Benchmark for Multi-Track Comparative Music Question Answering](jamendo-mt-qa_a_benchmark_for_multi-track_comparative_music_question_answering.md)**

:   构建 Jamendo-MT-QA，一个包含 36,519 个比较问答对（覆盖 12,173 个音轨对）的多音轨比较音乐问答基准，首次系统评估音频-语言模型在跨音轨比较推理上的能力，揭示现有模型在句子级比较生成上的显著不足。

**[Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective](learning_invariant_modality_representation_for_robust_multimodal_learning_from_a.md)**

:   本文提出 CmIR（因果模态不变表示学习），基于因果推理理论将每种模态显式解纠缠为因果不变表示和环境特定虚假表示，通过不变性约束+互信息约束+重建约束的优雅目标函数确保不变表示具有跨环境的稳定预测关系，在多模态情感/幽默/讽刺检测上取得 SOTA，尤其在 OOD 和噪声场景下表现突出。

**[Multimodal In-Context Learning for ASR of Low-Resource Languages](multimodal_in-context_learning_for_asr_of_low-resource_languages.md)**

:   系统研究多模态上下文学习（MICL）能否使语音 LLM 学习未见过的濒危语言，并提出基于 MICL 的假设选择系统，结合声学模型与语音 LLM 的互补优势，在三种濒危语言上显著提升 ASR 性能。

**[Music Audio-Visual Question Answering Requires Specialized Multimodal Designs](music_audio-visual_question_answering_requires_specialized_multimodal_designs.md)**

:   本文作为音乐视听问答（Music AVQA）领域首篇综合综述，系统分析了数据集演进和方法设计，论证了专门的输入处理、时空架构设计和音乐领域知识对该任务至关重要，通用多模态模型不足以应对音乐表演的独特挑战。

**[Pseudo2Real: Task Arithmetic for Pseudo-Label Correction in Automatic Speech Recognition](pseudo2real_task_arithmetic_for_pseudo-label_correction_in_automatic_speech_reco.md)**

:   本文提出 Pseudo2Real，一种参数空间校正方法，通过在源域中计算真实标签模型与伪标签模型的权重差得到"校正向量"，将其应用于目标域伪标签微调模型以纠正系统性伪标签偏差，在 AfriSpeech-200 的十种非洲口音上最高实现 35% 相对 WER 降低。

**[Retrieving to Recover: Towards Incomplete Audio-Visual Question Answering via Semantic-consistent Purification](retrieving_to_recover_towards_incomplete_audio-visual_question_answering_via_sem.md)**

:   本文提出R2ScP框架，将AVQA中缺失模态处理范式从传统的生成式补全转变为基于检索的恢复，通过跨模态检索和上下文感知自适应净化机制消除检索噪声，在模态不完整场景下显著提升了问答性能。

**[StressTest: Can YOUR Speech LM Handle the Stress?](stresstest_can_your_speech_lm_handle_the_stress.md)**

:   提出 StressTest 基准评估语音语言模型（SLMs）对句子重音含义的理解能力，发现现有模型几乎无法基于重音模式推理说话者意图，并通过合成数据管线 Stress-17k 训练的 StresSLM 在重音检测和推理任务上大幅超越前沿模型。

**[TellWhisper: Tell Whisper Who Speaks When](tellwhisper_tell_whisper_who_speaks_when.md)**

:   本文提出TellWhisper，通过设计时间-说话人感知的旋转位置编码（TS-RoPE）将说话人身份和时间信息统一编码到语音编码器的自注意力中，配合双曲空间说话人日志模型（Hyper-SD），实现了对"谁在何时说了什么"的联合建模，在多说话人ASR任务上取得最优性能。

**[Temporal Contrastive Decoding: A Training-Free Method for Large Audio-Language Models](temporal_contrastive_decoding_a_training-free_method_for_large_audio-language_mo.md)**

:   提出 TCD，一种无训练的推理时解码方法：通过对比原始音频和时间模糊慢速路径的 logits 差异，配合稳定性引导的模糊窗口和不确定性门控，使统一音频语言模型更好地利用瞬态声学线索，在 MMAU 和 AIR-Bench 上一致提升。

**[Towards Fine-Grained and Multi-Granular Contrastive Language-Speech Pre-training](towards_fine-grained_and_multi-granular_contrastive_language-speech_pre-training.md)**

:   本文提出FCaps大规模数据集（47k小时语音、19M细粒度标注）和CLSP对比学习模型，通过端到端标注管线和细粒度多粒度对比监督，实现了首个能统一表征全局和细粒度语音风格的语音-文本对齐模型。
