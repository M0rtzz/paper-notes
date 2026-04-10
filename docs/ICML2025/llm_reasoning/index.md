<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💡 LLM 推理

**🧪 ICML2025** · 共 **16** 篇

**[A Reasoning-Based Approach to Cryptic Crossword Clue Solving](a_reasoning-based_approach_to_cryptic_crossword_clue_solving.md)**

:   提出三阶段LLM推理pipeline（答案候选生成→wordplay解释→Python形式化验证），使用开源9B模型在Cryptonite密码填字谜数据集上实现新SOTA，关键创新在于将wordplay推理形式化为可执行Python代码并通过带hints的verifier迭代修正。

**[Ad-Hoc Human-AI Coordination Challenge (AH2AC2)](ad-hoc_human-ai_coordination_challenge.md)**

:   提出 AH2AC2 挑战——基于 Hanabi 合作卡牌游戏，通过行为克隆+正则化强化学习构建人类代理智能体，并开源有限人类数据集，为 Human-AI 临时协作研究提供标准化、可复现的评估框架。

**[AdaDecode: Accelerating LLM Decoding with Adaptive Layer Parallelism](adadecode_accelerating_llm_decoding_with_adaptive_layer_parallelism.md)**

:   AdaDecode 通过在中间层训练轻量级 LM Head 实现高置信度的 token 早期预测，将后续层的 KV cache 计算延迟并行化执行，在保证与标准自回归解码完全一致输出的同时，实现最高 1.73× 的解码吞吐量加速。

**[AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](adaptivestep_automatically_dividing_reasoning_step_through_model_confidence.md)**

:   提出 AdaptiveStep，基于模型预测下一个 token 的置信度自动划分推理步骤，替代传统基于规则（如换行符）的粗粒度划分方式，训练出的 PRM (ASPRM) 在数学推理和代码生成任务上达到 SOTA 的 Best-of-N 性能，且数据构建成本降低超 30%。

**[Adversarial Manipulation of Reasoning Models using Internal Representations](adversarial_manipulation_of_reasoning_models_using_internal_representations.md)**

:   本文发现推理模型（如 DeepSeek-R1-Distill-Llama-8B）在 CoT 生成阶段存在一个线性"谨慎方向"（caution direction），通过消融该方向可有效越狱模型，揭示了 CoT 本身是对抗攻击的新靶点。

**[Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](evaluating_judges_as_evaluators_the_jetts_benchmark_of_llm-as-judges_as_test-tim.md)**

:   本文提出 JETTS 基准，系统评估 LLM-judge 在 test-time scaling 场景（response reranking、step-level beam search、critique-based refinement）中作为评估器的表现，发现 judge 在 reranking 中与 outcome reward model 竞争力相当但在 beam search 中显著弱于 process reward model，且自然语言 critique 目前无法有效引导生成器改进。

**[FMC: Formalization of Natural Language Mathematical Competition Problems](fmc_formalization_of_natural_language_mathematical_competition_problems.md)**

:   本文提出基于 LLM 错误反馈的全自动形式化流水线，将自然语言数学竞赛题转化为 Lean 形式化表示，构建了包含 3,922 道自然语言与 9,787 条 Lean 形式化对齐的奥赛级数据集 FMC，并验证了其作为自动定理证明基准的价值。

**[Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](improving_rationality_in_the_reasoning_process_of_language_models_through_self-p.md)**

:   本文提出 Critic-Discernment Game（CDG），通过自博弈语言游戏让 LLM 与"有帮助的批评者"和"误导性批评者"互动，用 ReST 强化学习联合优化三个角色，无需人类或更强模型的监督即可显著提升 LLM 对自身推理过程的理性理解，在数学推理、逐步错误检测、自我纠错和长链推理四个任务上均取得一致提升。

**[No Soundness in the Real World: On the Challenges of the Verification of Deployed Neural Networks](no_soundness_in_the_real_world_on_the_challenges_of_the_verification_of_deployed.md)**

:   本文证明所有当前最先进的神经网络验证器都只提供"理论健全性"（约束全精度输出）而非"实际健全性"（约束部署环境中的浮点输出），并通过构造环境敏感的对抗性后门网络，实证验证了所有测试验证器均可被欺骗。

**[On the Power of Context-Enhanced Learning in LLMs](on_the_power_of_context-enhanced_learning_in_llms.md)**

:   本文形式化定义了"上下文增强学习"（context-enhanced learning），证明在简化设定下它比标准学习的样本效率**指数级更高**，并在机制层面揭示其优势来源于更精确的梯度学习信号。

**[One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL](one_missing_piece_for_open-source_reasoning_models_a_dataset_to_mitigate_cold-st.md)**

:   提出 Long CoT Collection——一个由短CoT LLM（如GPT-4o）标注的100K长链推理数据集，通过从o1提取推理流程（reasoning flow）作为间接引导，使短CoT模型也能生成高质量长推理链，从而有效缓解开源推理模型在强化学习阶段的冷启动问题，初始化后的模型在RLVR中获得2-3倍的性能提升。

**[PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation](pcot_persuasion-augmented_chain_of_thought_for_detecting_fake_news_and_social_me.md)**

:   提出 PCoT（Persuasion-Augmented Chain of Thought），通过两阶段推理——先让 LLM 识别文本中的说服策略，再将说服分析结果注入虚假信息检测推理——在零样本设置下，跨 5 个 LLM 和 5 个数据集平均提升 F1 约 15%。

**[ProofCompass: Enhancing Specialized Provers with LLM Guidance](proofcompass_enhancing_specialized_provers_with_llm_guidance.md)**

:   ProofCompass 提出一种无需额外训练的混合方法，用通用 LLM 为专业定理证明器（如 DeepSeek-Prover-v1.5-RL）提供自然语言证明策略和中间引理选择，在 miniF2F 上用 25 倍少的尝试次数超越了基线性能（54.9% → 55.3%）。

**[Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](rethinking_external_slow-thinking_from_snowball_errors_to_probability_of_correct.md)**

:   本文从信息论视角系统分析了 LLM 推理中的"雪球误差"现象，建立了雪球误差与推理正确概率之间的理论联系，证明了外部慢思考方法（如 BoN、MCTS）本质上是通过扩展搜索宽度来缓解误差累积，并在理论和实验上证明了方法效果主要取决于总推理代价和奖励函数可靠性，而非搜索框架本身。

**[Towards Better Chain-of-Thought: A Reflection on Effectiveness and Faithfulness](towards_better_chain-of-thought_a_reflection_on_effectiveness_and_faithfulness.md)**

:   本文从有效性（effectiveness）和忠实性（faithfulness）两个维度系统分析了 CoT 的性能影响因素，发现问题难度、信息增益和信息流是影响 CoT 有效性的关键因子，而不忠实 CoT 的根因在于模型在预测答案时绕过 CoT 直接从问题中召回了正确信息，并据此提出 QUIRE 方法同时提升 CoT 的有效性和忠实性。

**[Training Software Engineering Agents and Verifiers with SWE-Gym](training_software_engineering_agents_and_verifiers_with_swe-gym.md)**

:   本文提出 SWE-Gym——首个用于训练软件工程 Agent 的环境，包含来自 11 个开源 Python 仓库的 2438 个真实任务实例，通过在 SWE-Gym 上进行拒绝采样微调训练 SWE Agent 和 Verifier，在 SWE-Bench Verified/Lite 上最终达到 32.0%/26.0% 的解决率，创造了开源权重 SWE Agent 的新 SOTA。
