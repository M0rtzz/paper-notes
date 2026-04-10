<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**🤖 AAAI2026** · 共 **50** 篇

**[Aligning the True Semantics: Constrained Decoupling and Distribution Sampling for Cross-Modal Alignment](aligning_the_true_semantics_constrained_decoupling_and_distr.md)**

:   提出 CDDS 算法，通过双路径 UNet 将嵌入解耦为语义和模态分量，并利用分布采样方法间接实现跨模态语义对齐，避免直接调整嵌入导致的分布扭曲，在 Flickr30K 和 MS-COCO 上超越 SOTA 6.6%~14.2%。

**[anyECG-chat: A Generalist ECG-MLLM for Flexible ECG Input and Multi-Task Understanding](anyecg-chat_a_generalist_ecg-mllm_for_flexible_ecg_input_and.md)**

:   构建anyECG数据集（含报告生成、波形定位、多ECG比较三大任务）并提出anyECG-chat模型，通过动态ECG输入机制支持变长/少导联/多ECG输入，采用三阶段课程学习训练，在报告生成的OOD泛化、秒级异常波形定位和多ECG对比分析上全面超越现有ECG-MLLM。

**["Are We Done Yet?": A Vision-Based Judge for Autonomous Task Completion of Computer Use Agents](are_we_done_yet_a_vision-based_judge_for_autonomous_task_completion_of_computer_.md)**

:   提出基于 VLM 的自主任务完成评估框架，通过截图+任务描述判断 CUA 是否完成任务，并将评估反馈回传给 Agent 实现自我纠正，在 macOS 环境上达到 73% 评估准确率和 27% 的任务成功率相对提升。

**[AStar: Boosting Multimodal Reasoning with Automated Structured Thinking](astar_boosting_multimodal_reasoning_with_automated_structure.md)**

:   提出AStar，一种training-free的多模态推理范式，通过从500个种子样本中构建高层"thought cards"推理模板库，在推理时自适应检索最优模板引导MLLM结构化推理，7B模型在MathVerse上达53.9%准确率（超越GPT-4o的50.2%），仅需50分钟预处理时间且无需训练。

**[BiPrompt: Bilateral Prompt Optimization for Visual and Textual Debiasing in Vision-Language Models](biprompt_bilateral_prompt_optimization_for_visual_and_textual_debiasing_in_visio.md)**

:   提出 BiPrompt，一种双边 prompt 优化框架，在测试时同时缓解 CLIP 等 VLM 中视觉侧（结构化注意力擦除）和文本侧（平衡 prompt 归一化）的虚假偏差，无需重训练即可提升 OOD 鲁棒性。

**[BOFA: Bridge-Layer Orthogonal Low-Rank Fusion for CLIP-Based Class-Incremental Learning](bofa_bridge-layer_orthogonal_low-rank_fusion_for_clip-based_.md)**

:   提出BOFA框架，仅微调CLIP已有的跨模态投影层（bridge-layer），通过正交低秩融合（Orthogonal Low-Rank Fusion）将参数更新约束在与旧任务特征正交的低秩"安全子空间"中，配合跨模态混合原型分类器，在不增加任何额外参数和推理开销的前提下实现了SOTA的无样本存储类增量学习。

**[Branch, or Layer? Zeroth-Order Optimization for Continual Learning of Vision-Language Models](branch_or_layer_zeroth-order_optimization_for_continual_lear.md)**

:   本文系统探索了零阶（ZO）优化在基于PEFT的视觉-语言持续学习（VLCL）中的应用，发现全ZO替换会导致训练不稳定，提出从分支级（branch-wise）到层级（layer-wise）的渐进式ZO-FO混合策略，并基于视觉模态方差更大的理论发现提出MoZO策略（梯度符号归一化+视觉扰动约束），在四个benchmark上达到SOTA。

**[Bridging Modalities via Progressive Re-alignment for Multimodal Test-Time Adaptation (BriMPR)](bridging_modalities_via_progressive_re-alignment_for_multimo.md)**

:   提出 BriMPR 框架，通过"分而治之"策略将多模态测试时自适应(MMTTA)分解为多个单模态特征对齐子问题，先用 prompt tuning 校准各模态全局特征分布实现初始跨模态语义对齐，再通过跨模态掩码嵌入重组和实例级对比学习精细化对齐。

**[Bridging the Copyright Gap: Do Large Vision-Language Models Recognize and Respect Copyrighted Content?](bridging_the_copyright_gap_do_large_vision-language_models_r.md)**

:   首次系统评估 LVLM 在多模态上下文中对版权内容的识别和遵守能力，构建了 50,000 对多模态查询-内容的大规模 benchmark，发现 11/12 个 SOTA LVLM 即使面对明确版权声明也无法有效拒绝侵权请求，并提出 CopyGuard 工具增强框架将侵权拒绝率从 ~3% 提升至 ~62%。

**[Concept-RuleNet: Grounded Multi-Agent Neurosymbolic Reasoning in Vision Language Models](concept-rulenet_grounded_multi-agent_neurosymbolic_reasoning.md)**

:   提出Concept-RuleNet——一个三智能体协作的神经符号推理框架，通过从训练图像中提取视觉概念来条件化符号生成和规则构建，解决了现有方法（如Symbol-LLM）仅依赖标签导致的符号幻觉和不代表性问题，在5个OOD基准上平均提升~5%准确率，幻觉符号减少达50%。

**[Concepts from Representations: Post-hoc Concept Bottleneck Models via Sparse Decomposition of Visual Representations](concepts_from_representations_post-hoc_concept_bottleneck_models_via_sparse_deco.md)**

:   提出 PCBM-ReD，通过从预训练视觉编码器中自动提取概念、MLLM 标注/过滤、重建引导选择，再利用 CLIP 视觉-文本对齐将图像表示稀疏分解为概念嵌入的线性组合，构建事后概念瓶颈模型，在 11 个分类任务上达到 SOTA 精度且保持可解释性。

**[Conditional Information Bottleneck for Multimodal Fusion: Overcoming Shortcut Learning in Sarcasm Detection](conditional_information_bottleneck_for_multimodal_fusion_overcoming_shortcut_lea.md)**

:   揭示多模态讽刺检测中三类捷径学习问题（角色标签偏见、罐头笑声标签泄漏、情感不一致捷径）并重构了无捷径的 MUStARD++R 数据集，提出基于条件信息瓶颈的多模态融合框架 MCIB，通过压缩主模态冗余同时保留辅助模态的互补信息来实现有效融合。

**[CreBench: Human-Aligned Creativity Evaluation from Idea to Process to Product](crebench_human-aligned_creativity_evaluation_from_idea_to_process_to_product.md)**

:   提出 CreBench，一个覆盖创意想法→创作过程→创意产品三个维度、12个细粒度指标的多模态创造力评估基准，配套构建 CreMIT（2.2K样本、79.2K人工评价、4.7M指令）并微调出 CreExpert，在创造力评估上显著优于 GPT-4V 和 Gemini-Pro-Vision。

**[Cross-modal Prompting for Balanced Incomplete Multi-modal Emotion Recognition](cross-modal_prompting_for_balanced_incomplete_multi-modal_emotion_recognition.md)**

:   提出 Cross-modal Prompting (ComP) 方法，通过渐进式提示生成+跨模态知识传播+动态调度器来解决不完整多模态情感识别中的模态不平衡问题，在 4 个数据集、 7 种缺失率下均达到 SOTA。

**[Cross-modal Proxy Evolving for OOD Detection with Vision-Language Models](cross-modal_proxy_evolving_for_ood_detection_with_vision-lan.md)**

:   提出 CoEvo，一个 training-free 和 annotation-free 的 test-time 框架，通过双向 sample-conditioned 的文本/视觉 proxy 协同演化机制动态更新正负代理缓存，在 ImageNet-1K 上比最强负标签基线 AUROC 提升 1.33%、FPR95 降低 45.98%（从 18.92% 降至 10.22%），实现 SOTA 的 zero-shot OOD 检测。

**[Cross-Modal Unlearning via Influential Neuron Path Editing in Multimodal Large Language Models](cross-modal_unlearning_via_influential_neuron_path_editing_i.md)**

:   提出 MIP-Editor，通过跨层梯度积分（文本）和 Fisher 积分（视觉）定位多模态大语言模型中编码待遗忘知识的**影响力神经元路径**，再用基于路径的表示误导（RMisU）编辑这些神经元，在 MLLMU-Bench 上实现最高 87.75% 的遗忘率和 54.26% 的通用知识保留提升。

**[CrossCheck-Bench: Diagnosing Compositional Failures in Multimodal Conflict Resolution](crosscheck-bench_diagnosing_compositional_failures_in_multim.md)**

:   构建CrossCheck-Bench——首个专注于多模态矛盾检测与解决的诊断基准，包含15K QA对、3层推理复杂度和7种原子能力，发现13个SOTA VLM从感知匹配到逻辑矛盾检测性能一致下降，CoT/SoM等提示策略收效甚微，仅交错符号推理+视觉grounding的方法才有稳定提升。

**[CrossVid: A Comprehensive Benchmark for Evaluating Cross-Video Reasoning in Multimodal Large Language Models](crossvid_a_comprehensive_benchmark_for_evaluating_cross-vide.md)**

:   提出首个系统评估多模态大语言模型（MLLM）跨视频推理（Cross-Video Reasoning, CVR）能力的综合基准CrossVid，涵盖4个维度10个任务、5,331个视频和9,015个QA对，实验揭示当前最佳模型Gemini-2.5-Pro仅达50.4%准确率，远低于人类89.2%。

**[Difference Vector Equalization for Robust Fine-tuning of Vision-Language Models](difference_vector_equalization_for_robust_fine-tuning_of_vis.md)**

:   提出DiVE方法，通过约束预训练和微调模型嵌入之间的"差异向量"在各样本间保持相等，从而在CLIP微调过程中保持嵌入空间的几何结构，同时在ID、OOD、零样本三个指标上取得全面优于现有方法的结果（零样本平均提升8+点）。

**[DisCode: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning](discode_distribution-aware_score_decoder_for_robust_automatic_evaluation_of_imag.md)**

:   提出 DISCODE，一种免微调的测试时自适应解码器，通过引入高斯先验分布最小化 ATT 损失，使 LVLM 生成的图像描述评估分数更鲁棒地对齐人类判断，并构建了覆盖六个视觉域的 MCEval 基准。

**[DR.Experts: Differential Refinement of Distortion-Aware Experts for Blind Image Quality Assessment](drexperts_differential_refinement_of_distortion-aware_experts_for_blind_image_qu.md)**

:   提出DR.Experts框架，利用DA-CLIP获取失真类型先验，通过差分精炼注意力机制（DSDM）将失真注意力与语义注意力分离以纯化失真特征，再通过动态失真加权模块（DDWM）按感知影响自适应加权各类失真特征，在5个BIQA基准上达到SOTA。

**[EM-KD: Distilling Efficient Multimodal Large Language Model with Unbalanced Vision Tokens](em-kd_distilling_efficient_multimodal_large_language_model_w.md)**

:   提出EM-KD框架，通过Hungarian算法解决teacher-student间视觉token数量不平衡问题，结合视觉语义蒸馏(VSD)和视觉-语言亲和力蒸馏(VLAD)将vanilla teacher的知识迁移到高效student MLLM，在11个benchmark上以144 token/patch达到50.4均分，超越576 token的LLaVA-NeXT(49.4)同时推理速度提升近2倍。

**[Exo2Ego: Exocentric Knowledge Guided MLLM for Egocentric Video Understanding](exo2ego_exocentric_knowledge_guided_mllm_for_egocentric_vide.md)**

:   提出 Exo2Ego 框架，通过学习外中心(第三人称)与自中心(第一人称)域之间的映射关系，将 MLLM 中丰富的外中心知识迁移到自中心视频理解，结合新构建的 110万同步 ego-exo clip-text 对数据集 Ego-ExoClip 和 60万指令微调数据集 EgoIT，在 8 个自中心视频基准上取得了领先的开源模型性能。

**[Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration](filter_correlate_compress_training-free_token_reduction_for_.md)**

:   提出FiCoCo三阶段框架（Filter-Correlate-Compress），通过集成视觉感知+语义感知冗余度量筛选丢弃token，利用token间相关性自适应回收信息，实现training-free的MLLM加速。在LLaVA-NeXT上达14.7×FLOPs压缩同时保留93.6%性能，在5种MLLM架构上全面超越FastV、SparseVLM等SOTA。

**[FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models](ft-ncfm_an_influence-aware_data_distillation_framework_for_efficient_vla_models.md)**

:   提出 FT-NCFM 框架，通过因果归因（Fact-Tracing）评估样本价值并引导对抗式 NCFM 过程合成高信息密度核心集，仅用 5% 合成数据即可达到全量训练 85-90% 的性能，训练时间减少 80% 以上。

**[Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models](global_compression_commander_plug-and-play_inference_acceler.md)**

:   提出GlobalCom²，一个**即插即用、无需训练**的token压缩框架，专为动态裁剪（dynamic cropping）结构的高分辨率VLM设计：利用全局缩略图（thumbnail）作为"指挥官"引导局部裁剪区域（crop）的差异化压缩，在压缩90%视觉token的同时保持>90%原始性能。

**[Graph-of-Mark: Promote Spatial Reasoning in Multimodal Language Models with Graph-Based Visual Prompting](graph-of-mark_promote_spatial_reasoning_in_multimodal_langua.md)**

:   提出 Graph-of-Mark (GoM)，一种无需训练的像素级视觉提示方法，通过在输入图像上直接叠加深度感知的场景图（包含节点和有向边），显式编码物体间的空间关系，使多模态语言模型在 VQA 和定位任务中的零样本空间推理准确率最高提升 11 个百分点。

**[Harnessing Vision-Language Models for Time Series Anomaly Detection](harnessing_vision-language_models_for_time_series_anomaly_detection.md)**

:   提出两阶段零样本时序异常检测框架：ViT4TS 用轻量 ViT 对时序折线图做多尺度 cross-patch 匹配定位候选异常区间，VLM4TS 用 GPT-4o 结合全局时序上下文验证和精炼检测结果，在 11 个 benchmark 上 F1-max 超最优 baseline 24.6%，token 用量仅为现有 LLM 方法的 1/36。

**[HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection](headhunt-vad_hunting_robust_anomaly-sensitive_heads_in_mllm_.md)**

:   提出HeadHunt-VAD，不用MLLM的文本输出，而是直接从冻结MLLM中"猎取"一小批对异常敏感且跨prompt鲁棒的注意力头，配合轻量逻辑回归scorer，在仅用1%数据、零微调的条件下，在UCF-Crime(87.03% AUC)和XD-Violence(82.63% AP)上达到tuning-free方法SOTA。

**[HiMo-CLIP: Modeling Semantic Hierarchy and Monotonicity in Vision-Language Alignment](himo-clip_modeling_semantic_hierarchy_and_monotonicity_in_vi.md)**

:   提出 HiMo-CLIP，通过对文本嵌入做 batch 内 PCA 分解（HiDe）提取多粒度语义成分，配合双分支单调性感知对比损失（MoLo），在不修改编码器的前提下让 CLIP 学会"文本越完整、对齐分数越高"的语义单调性，在长文本检索上显著超越现有方法。

**[InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration](inex_hallucination_mitigation_via_introspection_and_cross-mo.md)**

:   提出 InEx 框架，通过内部自省推理（TVER 驱动的不确定性感知视觉增强）和外部跨模态多智能体协作（文本自反思 + 图像编辑验证 + 视觉自反思）迭代验证和修正 MLLM 输出，在 POPE 上提升 8.9%，在多个幻觉和通用 benchmark 上持续超越 OPERA/VCD/ICD。

**[Information Theoretic Optimal Surveillance for Epidemic Prevalence in Networks](information_theoretic_optimal_surveillance_for_epidemic_prevalence_in_networks.md)**

:   本文首次提出以互信息作为优化准则的流行病监测框架 TestPrev，旨在选择网络中的最优节点子集以最大化与疾病流行度分布的互信息，从而提供传统方法无法给出的暴发规模分布级别洞察，并证明了其 NP-hard 性质，设计了贪心算法 GreedyMI 在合成与真实网络上优于基线方法。

**[LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction](llm-cas_dynamic_neuron_perturbation_for_real-time_hallucinat.md)**

:   LLM-CAS 首次将 LLM 实时幻觉纠正建模为层次强化学习（HRL）问题，训练 RL Agent 在推理时动态选择最优的神经元扰动策略（高层选择功能网络类别，低层选择扰动类型和幅度），结合自适应掩码+因果追踪精确定位目标神经元，在 StoryCloze 上提升 10.98%，超越 ITI/CAA/SADI 等静态/动态基线。

**[MCMoE: Completing Missing Modalities with Mixture of Experts for Incomplete Multimodal Action Quality Assessment](mcmoe_completing_missing_modalities_with_mixture_of_experts_for_incomplete_multi.md)**

:   本文首次探索不完整多模态动作质量评估问题，提出 MCMoE 框架，利用自适应门控模态生成器（AGMG）补全缺失模态，并通过混合专家（MoE）动态融合单模态和跨模态联合表示，在单阶段训练中统一学习，在三个公开 AQA 基准上的完整和不完整场景中均达到 SOTA，且参数量仅 4.90M。

**[Multi-Faceted Attack: Exposing Cross-Model Vulnerabilities in Defense-Equipped Vision-Language Models](multi-faceted_attack_exposing_cross-model_vulnerabilities_in_defense-equipped_vi.md)**

:   提出多面攻击框架MFA，通过注意力转移攻击(ATA)突破对齐、对抗签名绕过内容审核、视觉编码器攻击覆写系统提示三个维度，系统性暴露配备多层防御的VLM（含GPT-4o/Gemini等商业模型）的安全漏洞，总体攻击成功率达58.5%。

**[Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports From Scratch with Agentic Framework](multimodal_deepresearcher_generating_text-chart_interleaved_.md)**

:   提出 Multimodal DeepResearcher，一个四阶段 Agent 框架从零生成图文交替研究报告：通过形式化可视化描述（FDV）让 LLM 学习和生成多样化图表，结合 Actor-Critic 迭代精炼机制（LLM生成D3.js代码→浏览器渲染→多模态LLM评审），在自建 MultimodalReportBench 上达到 82% 整体胜率（Claude 3.7），人类评估 100% 胜率。

**[Panda: Test-Time Adaptation with Negative Data Augmentation](panda_test-time_adaptation_with_negative_data_augmentation.md)**

:   提出 Panda，通过负数据增强（patch 打乱重组）生成保留 corruption 但破坏语义的图像，用其特征偏移原始嵌入以抑制 corruption 引起的预测偏差，以极低开销（<10%）即插即用提升各类 TTA 方法的鲁棒性。

**[PET2Rep: Towards Vision-Language Model-Driven Automated Radiology Report Generation for Positron Emission Tomography](pet2rep_towards_vision-language_model-drived_automated_radiology_report_generati.md)**

:   本文提出 PET2Rep，首个专用于正电子发射断层扫描（PET）放射报告生成的大规模基准数据集（565例全身 PET/CT 图像-报告对），并设计了 PET 临床效能（CE）评估指标，对 30 个前沿通用和医疗专用 VLM 进行系统评估，发现当前 SOTA VLM 在 PET 报告生成任务上表现不佳，甚至无法超越简单的模板基线。

**[PlantTraitNet: An Uncertainty-Aware Multimodal Framework for Global-Scale Plant Trait Inference from Citizen Science Data](planttraitnet_an_uncertainty-aware_multimodal_framework_for_global-scale_plant_t.md)**

:   本文提出 PlantTraitNet，一个多模态、多任务、不确定性感知的深度学习框架，利用公民科学平台（iNaturalist、Pl@ntNet）的弱监督植物照片，结合图像特征（DINOv2）、深度先验（Depth-Anything-V2）和地理空间先验（Climplicit），同时预测四种关键植物性状（株高、叶面积、比叶面积、叶氮含量），生成的全球性状图在与 sPlotOpen 植被调查数据的基准测试中一致优于现有全球性状产品。

**[ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models](recad_reinforcement_learning_enhanced_parametric_cad_model_generation_with_visio.md)**

:   提出 ReCAD 框架，通过将 CAD 脚本重写为参数化代码进行 SFT，再利用 GRPO 强化学习与分层基元课程学习策略，使 VLM 能从文本或图像输入生成高精度、可编辑的参数化 CAD 模型，在分布内和分布外设置上均大幅超越现有方法。

**[Rethinking Visual Token Reduction in LVLMs under Cross-Modal Misalignment](rethinking_visual_token_reduction_in_lvlms_under_cross-modal_misalignment.md)**

:   揭示了 LVLM 中文本引导视觉token重要性评估的三种跨模态失配问题（因果、语义、空间），提出 VisionDrop——一个仅依赖视觉自注意力的免训练渐进式token剪枝框架，跨视觉编码器和 LLM 解码器多阶段压缩，在保留 5.6% token 时仍能维持 91%+ 原始性能。

**[RMAdapter: Reconstruction-based Multi-Modal Adapter for Vision-Language Models (Oral)](rmadapter_reconstructionbased_multimodal_adapter_for_visionlanguage.md)**

:   提出 RMAdapter，一种双分支适配器架构：在标准 adapter 的适应分支旁增加重建分支（类 AutoEncoder），通过共享下投影层和逐层本地重建损失，在 CLIP 少样本微调中实现任务特定适应与通用知识保持的最佳平衡，在 Base-to-Novel 泛化、跨数据集和领域泛化三个任务上全面超越 SOTA（含 Prompt-based 方法）。

**[SafeR-CLIP: Mitigating NSFW Content in Vision-Language Models While Preserving Pre-Trained Knowledge](safer-clip_mitigating_nsfw_content_in_vision-language_models_while_preserving_pr.md)**

:   提出SafeR-CLIP框架，通过近邻感知重定向（将不安全嵌入重定向到语义最近的安全目标而非固定配对）和相对跨模态重定向损失（仅以不安全表示作为负样本而非随机批内负样本），在保持安全性的同时将零样本分类精度比Safe-CLIP恢复8.0%。

**[SDEval: Safety Dynamic Evaluation for Multimodal Large Language Models](sdeval_safety_dynamic_evaluation_for_multimodal_large_language_models.md)**

:   提出 SDEval，首个面向 MLLM 安全性的动态评估框架，通过文本动态（同义替换/多语混合/CoT 注入等）、图像动态（空间/颜色变换/扩散生成）和文本-图像交互动态三类策略，从静态 benchmark 可控生成不同复杂度的新样本，缓解数据泄露并暴露模型安全短板。

**[Soft Filtering: Guiding Zero-Shot Composed Image Retrieval with Prescriptive and Proscriptive Prompts](soft_filtering_guiding_zero-shot_composed_image_retrieval_with_prescriptive_and_.md)**

:   提出 SoFT，一个无需训练的即插即用重排序模块，利用多模态 LLM 从参考图像和修改文本中提取"必须包含"（prescriptive）和"必须避免"（proscriptive）双重文本约束，对零样本组合图像检索的候选结果进行软过滤重排序，同时构建了多目标三元组数据集流水线以改善评估。

**[TOFA: Training-Free One-Shot Federated Adaptation for Vision-Language Models](tofa_training-free_one-shot_federated_adaptation_for_vision-language_models.md)**

:   提出TOFA框架，在联邦学习场景下通过层次贝叶斯模型学习个性化视觉prototype分布 + 全局对齐的LLM文本增强 + 自适应模态融合，实现无需训练、仅一轮通信的CLIP高效适配，在9个数据集上超越one-shot基线甚至部分多轮训练方法。

**[Towards a Rigorous Understanding of the Population Dynamics of the NSGA-III: Tight Runtime Bounds](towards_a_rigorous_understanding_of_the_population_dynamics_of_the_nsga-iii_tigh.md)**

:   本文首次为 NSGA-III 在经典双目标 OneMinMax 基准上建立了紧致运行时界 $\Theta(n^2 \ln n / \mu)$，揭示了 NSGA-III 的种群动态特性，并证明其在适当种群规模下优于 NSGA-II。

**[URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding](urag_unified_retrieval_and_generation_in_multimodal_llms_for.md)**

:   URaG 发现 MLLM 处理长文档时存在类人的"粗到细"推理模式（浅层注意力均匀分散、深层集中于证据页），基于此洞察在第 6 层插入轻量跨模态检索模块（仅占参数 0.05%），选取 Top-5 相关页面丢弃其余内容，实现 SOTA 性能的同时减少 44-56% 计算量。

**[VipAct: Visual-Perception Enhancement via Specialized VLM Agent Collaboration and Tool-use](vipact_visual-perception_enhancement_via_specialized_vlm_age.md)**

:   VipAct 提出了一个多Agent协作框架，通过编排器Agent（任务分析+规划+协调）、专用Agent（描述/比较/视觉提示解读）和视觉专家模型（深度估计/目标检测/分割等）三层协作，显著提升 VLM 在细粒度视觉感知任务上的表现，在 Blink 上从 63.74% (zero-shot GPT-4o) 提升到 73.79%。

**[VP-Bench: A Comprehensive Benchmark for Visual Prompting in Multimodal Large Language Models](vp-bench_a_comprehensive_benchmark_for_visual_prompting_in_m.md)**

:   VP-Bench 提出了首个系统评估 MLLM 视觉提示（Visual Prompt）理解能力的两阶段 Benchmark：Stage 1 用 30K+ 图像覆盖 8 种 VP 形状×355 种属性组合评测 VP 感知能力，Stage 2 评测 VP 对 6 个下游任务的实际效果。在 28 个 MLLM 上的评测揭示了 VP 形状选择对性能的关键影响。
