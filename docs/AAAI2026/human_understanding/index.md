<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🤖 AAAI2026** · 共 **16** 篇

**[10 Open Challenges Steering the Future of Vision-Language-Action Models](10_open_challenges_steering_the_future_of_vision-language-ac.md)**

:   一篇针对Vision-Language-Action(VLA)模型的综述/展望论文，系统梳理了VLA领域的10大开放挑战（多模态感知、鲁棒推理、数据质量、评估、跨机器人泛化、效率、全身协调、安全、多智能体、人机协作）以及4大新兴趋势（层次化规划、空间理解、世界动力学建模、数据合成），为VLA研究指明方向。

**[AHAN: Asymmetric Hierarchical Attention Network for Identical Twin Face Verification](ahan_asymmetric_hierarchical_attention_network_for_identical.md)**

:   针对同卵双胞胎人脸验证这一极端细粒度识别挑战，提出 AHAN 多流架构，通过层次交叉注意力 (HCA) 对语义面部区域做多尺度分析、面部不对称注意力模块 (FAAM) 捕获左右脸差异签名、以及双胞胎感知配对交叉注意力 (TA-PWCA) 训练正则化，在 ND_TWIN 数据集上将双胞胎验证精度从 88.9% 提升至 92.3%（+3.4%）。

**[Anti-adversarial Learning: Desensitizing Prompts for Large Language Models](anti-adversarial_learning_desensitizing_prompts_for_large_la.md)**

:   提出 PromptObfus，通过"反对抗学习"思路将用户 prompt 中的敏感词替换为语义不同但不影响任务输出的词，从而在不降低远端 LLM 任务表现的前提下彻底消除显式隐私泄露，并将隐式隐私推理攻击成功率降低 62.70%。

**[Authority Backdoor: A Certifiable Backdoor Mechanism for Authoring DNNs](authority_backdoor_a_certifiable_backdoor_mechanism_for_authoring_dnns.md)**

:   提出 Authority Backdoor，将硬件指纹作为后门触发器嵌入 DNN，使模型仅在授权设备上正常工作，并通过随机平滑实现可认证鲁棒性，抵御自适应触发器逆向攻击。

**[Auto-PRE: An Automatic and Cost-Efficient Peer-Review Framework for Language Generation Evaluation](auto-pre_an_automatic_and_cost-efficient_peer-review_framework_for_language_gene.md)**

:   提出 Auto-PRE 框架，通过自动资格考试从一致性、相关性、自信度三个维度筛选合格的 LLM 评估者，在无需人工标注的前提下实现了 SOTA 评估性能并大幅降低成本。

**[Behavior Tokens Speak Louder: Disentangled Explainable Recommendation with Behavior Vocabulary](behavior_tokens_speak_louder_disentangled_explainable_recommendation_with_behavi.md)**

:   提出 BEAT 框架，通过向量量化自编码将用户/物品的行为表征离散化为可解释的 behavior tokens，结合多层级语义监督将协同过滤信号对齐到冻结 LLM 的语义空间，实现零样本可解释推荐。

**[Bias Association Discovery Framework for Open-Ended LLM Generations](bias_association_discovery_framework_for_open-ended_llm_generations.md)**

:   提出偏见关联发现框架 BADF，通过分析 LLM 开放式故事生成中的叙事内容，系统性地提取人口统计身份与描述性概念之间的已知和未知偏见关联，突破了以往依赖预定义偏见概念的局限。

**[Can LLMs Truly Embody Human Personality? Analyzing AI and Human Behavior Alignment in Dispute Resolution](can_llms_truly_embody_human_personality_analyzing_ai_and_human_behavior_alignmen.md)**

:   提出首个系统对比框架，在配对的冲突调解场景中直接比较人类与人格提示LLM的策略行为差异，发现LLM在人格-行为映射上与人类存在显著偏差，挑战了"人格提示即可代理人类行为"的假设。

**[CCFQA: A Benchmark for Cross-Lingual and Cross-Modal Speech and Text Factuality Evaluation](ccfqa_a_benchmark_for_cross-lingual_and_cross-modal_speech_and_text_factuality_e.md)**

:   提出 CCFQA，一个覆盖 8 种语言、包含 14,400 条平行语音-文本事实问答样本的跨语言跨模态基准，用于系统评估多模态大语言模型在不同语言和输入模态下的事实一致性，并提出基于英语桥接的 few-shot 迁移策略 LLM-SQA。

**[CLIP-FTI: Fine-Grained Face Template Inversion via CLIP-Driven Attribute Conditioning](clip-fti_fine-grained_face_template_inversion_via_clip-driven_attribute_conditio.md)**

:   首次利用 CLIP 提取面部细粒度语义属性嵌入来辅助人脸模板反演（FTI），通过跨模态特征交互网络将泄露模板与属性嵌入融合并投影到 StyleGAN 潜空间，生成身份一致且属性细节更丰富的人脸图像，在识别准确率、属性相似度和跨模型攻击迁移性上均超越 SOTA。

**[CLIPPan: Adapting CLIP as A Supervisor for Unsupervised Pansharpening](clippan_adapting_clip_as_a_supervisor_for_unsupervised_pansharpening.md)**

:   提出 CLIPPan，通过轻量微调 CLIP 使其理解多光谱/全色/高分辨率多光谱图像类型及全色锐化过程，然后利用 Wald 协议等文本提示作为语义监督信号，实现无需地面真值的全分辨率无监督全色锐化，可作为即插即用模块兼容任意全色锐化骨干网络。

**[CoordAR: One-Reference 6D Pose Estimation of Novel Objects via Autoregressive Coordinate Map Generation](coordar_one-reference_6d_pose_estimation_of_novel_objects_via_autoregressive_coo.md)**

:   提出 CoordAR，将单参考视图 6D 位姿估计中的 3D-3D 对应关系建模为离散 token 的自回归生成问题，通过坐标图 token 化、模态解耦编码和自回归 Transformer 解码器，在多个基准上显著超越现有单视图方法，并对对称、遮挡等挑战场景展现强鲁棒性。

**[DEIG: Detail-Enhanced Instance Generation with Fine-Grained Semantic Control](deig_detail-enhanced_instance_generation_with_fine-grained_semantic_control.md)**

:   提出 DEIG，一个面向细粒度多实例图像生成的框架，通过实例细节提取器（IDE）将 LLM 编码器的高维嵌入蒸馏为紧凑的实例感知表示，并用细节融合模块（DFM）的实例掩码注意力防止属性泄漏，在多属性（颜色+材质+纹理）复合描述的生成任务上大幅超越现有方法。

**[Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment](dexterous_manipulation_transfer_via_progressive_kinematic-dynamic_alignment.md)**

:   提出 PKDA 框架，通过渐进式运动学-动力学对齐，将人手操作视频自动转化为多指灵巧手的高质量操作轨迹，平均迁移成功率达 73%。

**[Distributionally Robust Online Markov Game with Linear Function Approximation](distributionally_robust_online_markov_game_with_linear_function_approximation.md)**

:   本文研究具有线性函数近似的在线分布鲁棒马尔可夫博弈，首次识别了该设定下的学习困难性，并提出 DR-CCE-LSI 算法，在特定特征映射条件下实现了关于特征维度 $d$ 的极小极大最优样本复杂度。

**[RENEW: Risk- and Energy-Aware Navigation in Dynamic Waterways](renew_risk-_and_energy-aware_navigation_in_dynamic_waterways.md)**

:   提出 RENEW 全局路径规划器，为水面自主航行器 (ASV) 在动态水流 (洋流) 环境中引入统一的风险感知和能量感知策略，通过自适应不可导航区域识别、最佳努力应急策略和基于约束 Delaunay 三角化的分层架构实现安全高效导航，应急碰撞测试中实现零碰撞。
