---
title: >-
  CVPR2026 AIGC检测论文汇总 · 8篇论文解读
description: >-
  8篇CVPR2026的 AIGC 检测方向论文解读，涵盖推理、机器人、多模态等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2026"
  - "AIGC 检测"
  - "论文解读"
  - "论文笔记"
  - "推理"
  - "机器人"
  - "多模态"
item_list:
  - u: "fine-grained_image_aesthetic_assessment_learning_discriminative_scores_from_rela/"
    t: "Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks"
  - u: "frame_forensic_routing_and_adaptive_multi-path_evidence_fusion_for_image_manipul/"
    t: "FRAME: Forensic Routing and Adaptive Multi-path Evidence Fusion for Image Manipulation Detection"
  - u: "inconsistency-aware_multimodal_schrodinger_bridge_for_deepfake_localization/"
    t: "Inconsistency-aware Multimodal Schrodinger Bridge for Deepfake Localization"
  - u: "learning_forgery-aware_lip_representations_without_forgery_priors/"
    t: "Learning Forgery-Aware Lip Representations Without Forgery Priors"
  - u: "locate-then-examine_grounded_region_reasoning_improves_detection_of_ai-generated/"
    t: "Locate-Then-Examine: Grounded Region Reasoning Improves Detection of AI-Generated Images"
  - u: "ppm-clip_probabilistic_prompt_modeling_for_generalizable_ai-generated_image_dete/"
    t: "PPM-CLIP: Probabilistic Prompt Modeling for Generalizable AI-Generated Image Detection"
  - u: "quality-aware_calibration_for_ai-generated_image_detection_in_the_wild/"
    t: "Quality-Aware Calibration for AI-Generated Image Detection in the Wild"
  - u: "realign_generalizable_image_forgery_detection_via_reasoning-aligned_representati/"
    t: "ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation"
item_total: 8
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔎 AIGC 检测

**📷 CVPR2026** · **8** 篇论文解读

📌 **同领域跨会议浏览：** [🧪 ICML2026 (7)](../../ICML2026/aigc_detection/index.md) · [💬 ACL2026 (16)](../../ACL2026/aigc_detection/index.md) · [🔬 ICLR2026 (6)](../../ICLR2026/aigc_detection/index.md) · [🤖 AAAI2026 (2)](../../AAAI2026/aigc_detection/index.md) · [🧠 NeurIPS2025 (9)](../../NeurIPS2025/aigc_detection/index.md) · [💬 ACL2025 (15)](../../ACL2025/aigc_detection/index.md)

🔥 **高频主题：** 推理 ×2

**[Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks](fine-grained_image_aesthetic_assessment_learning_discriminative_scores_from_rela.md)**

:   定义"细粒度图像美学评估"新任务，构建含32,217张图像/10,028个系列的FGAesthetics基准，提出FGAesQ模型：通过差异保留Tokenization（DiffToken）+ 对比文本辅助对齐（CTAlign）+ 排序感知回归（RankReg）从相对排序中学习判别性审美评分，在细粒度场景准确率0.779的同时保持粗粒度SRCC 0.770。

**[FRAME: Forensic Routing and Adaptive Multi-path Evidence Fusion for Image Manipulation Detection](frame_forensic_routing_and_adaptive_multi-path_evidence_fusion_for_image_manipul.md)**

:   FRAME 把一堆传统取证算法（ELA、DCT、噪声、CFA、copy-move 等）组织成一个"取证 supernet"，对每张待检图像用 GNN 预测器挑出最合适的若干条"分析路径"并把它们的证据图融合，从而避免"单一检测器不通用 + 固定融合稀释信号"的老问题，在多个跨域测试集上同时把检测 AUC 和像素级定位刷到优于固定组合和端到端深度模型。

**[Inconsistency-aware Multimodal Schrodinger Bridge for Deepfake Localization](inconsistency-aware_multimodal_schrodinger_bridge_for_deepfake_localization.md)**

:   IaMSB 把音视频深度伪造的「时间区间定位」重新表述成一个薛定谔桥（Schrödinger Bridge）生成问题——用桥的传输代价直接读出跨模态一致性分数，再据此把计算步数非对称地分配给更可疑的那个模态，从而在严格 IoU（AP@0.95）上比现有方法高 3~10%。

**[Learning Forgery-Aware Lip Representations Without Forgery Priors](learning_forgery-aware_lip_representations_without_forgery_priors.md)**

:   针对说话人认证系统被个性化"说话人脸生成"(TFG)伪造攻破的问题，本文提出一个**只用真实视频训练、完全不依赖任何伪造样本**的检测器：靠真帧混合伪造 + 非对称对比 + 高斯正则把真实唇动特征压成一个紧致球面，把球外一切（伪造和冒名者）当离群点，在 8 种现代伪造、10 个 SOTA 对比下把错误率压低 10% 以上。

**[Locate-Then-Examine: Grounded Region Reasoning Improves Detection of AI-Generated Images](locate-then-examine_grounded_region_reasoning_improves_detection_of_ai-generated.md)**

:   LTE 让视觉语言模型先"全局扫描定位可疑区域"再"放大裁剪复核给出最终判定"，把一次性分类升级为两阶段的区域接地（region-grounded）推理，并配套构建带框级标注与取证解释的 TRACE 数据集，在准确率、鲁棒性和可解释性上同时获得提升。

**[PPM-CLIP: Probabilistic Prompt Modeling for Generalizable AI-Generated Image Detection](ppm-clip_probabilistic_prompt_modeling_for_generalizable_ai-generated_image_dete.md)**

:   PPM-CLIP 把"判别一条静态决策边界"的 AIGC 检测范式换成"生成式概率推理"——用归一化流为每张图生成一族自适应 prompt（多个假设），再对全部假设的余弦相似度取平均消噪做判定，并配一个频域引导的 patch 对比学习让 CLIP 编码器盯住高频伪造痕迹，在 Ojha / GenImage / DRCT 上的跨生成器泛化显著超过 SOTA。

**[Quality-Aware Calibration for AI-Generated Image Detection in the Wild](quality-aware_calibration_for_ai-generated_image_detection_in_the_wild.md)**

:   针对同一张图在网络传播中产生的多个画质各异的"近重复版本"，本文提出 QuAD：用无参考 IQA 估计每个版本的画质，再用画质作条件对取证检测器的 logit 做高斯校准并加权融合，让低画质版本少说话、高画质版本多说话，平均把六个 SOTA 检测器的平衡准确率提升约 8 个百分点。

**[ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation](realign_generalizable_image_forgery_detection_via_reasoning-aligned_representati.md)**

:   ReAlign 先用 GRPO 训出一个会"讲理由"的多模态大模型 AIGI-R1，再把它生成的推理文本作为"桥梁"，通过对比学习把推理文本空间蒸馏进一个轻量 CLIP 检测器，让小模型同时继承大模型的跨域泛化和语义错误敏感性，推理时只用图像编码器即可，在 AIGCDetectBenchmark / AIGI-Holmes / 自建 UltraSynth-10k 上都拿到 SOTA（mAcc 96.14% / 99.44% / 97.09%）。
