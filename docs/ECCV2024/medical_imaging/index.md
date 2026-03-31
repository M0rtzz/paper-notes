<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🎞️ ECCV2024** · 共 **10** 篇

**[Adaptive Correspondence Scoring for Unsupervised Medical Image Registration](adaptive_correspondence_scoring_for_unsupervised_medical_ima.md)**

:   针对医学图像无监督配准中噪声、遮挡等干扰因素导致的虚假重建误差问题，提出了一个自适应对应关系评分框架（AdaCS），通过学习像素级的对应置信度图来重新加权误差残差，以即插即用方式一致提升三种主流配准架构在三个数据集上的性能。

**[Alternate Diverse Teaching for Semi-supervised Medical Image Segmentation](alternate_diverse_teaching_for_semi-supervised_medical_image_segmentation.md)**

:   提出 AD-MT（Alternate Diverse Mean Teacher），通过随机周期性交替更新两个教师模型 + 基于熵的冲突调和策略，在半监督医学分割中解决 confirmation bias 问题，在 ACDC/LA/Pancreas 上全面超越 SOTA。

**[Architecture-Agnostic Untrained Network Priors for Image Reconstruction with Frequency Regularization](architecture-agnostic_untrained_network_priors_for_image_reconstruction_with_fre.md)**

:   提出三种与架构无关的频率正则化技术（带宽受限输入、带宽可控上采样、Lipschitz 正则化卷积层），统一解决 untrained network prior 的架构敏感性、过拟合和运行效率问题，在 MRI 重建任务中显著缩小不同架构间的性能差距。

**[CardiacNet: Learning to Reconstruct Abnormalities for Cardiac Disease Assessment from Echocardiogram Videos](cardiacnet_learning_to_reconstruct_abnormalities_for_cardiac_disease_assessment_.md)**

:   提出基于重建的心脏疾病评估框架 CardiacNet，通过 Consistency Deformation Codebook (CDC) 和 Consistency Deformation Discriminator (CDD) 学习正常与异常心脏超声视频之间的结构和运动差异，在射血分数预测、肺动脉高压和房间隔缺损分类三个任务上达到 SOTA。

**[Chameleon: A Data-Efficient Generalist for Dense Visual Prediction in the Wild](chameleon_a_data-efficient_generalist_for_dense_visual_prediction_in_the_wild.md)**

:   提出 Chameleon，一个基于 meta-learning 和 token matching 的数据高效视觉通才模型，仅需几十张标注图像即可适应全新的密集预测任务（包括医学图像、视频、3D 等），在六个下游基准上显著超越现有通才方法。

**[GTP-4o: Modality-Prompted Heterogeneous Graph Learning for Omni-modal Biomedical Representation](gtp4o_modalityprompted_heterogeneous_graph_learning_for.md)**

:   提出 GTP-4o，一种基于模态提示的异构图学习框架，通过异构图嵌入、图提示补全缺失模态、知识引导的层级聚合，实现基因组学-病理图像-细胞图-文本等多种临床模态的统一表示学习。

**[Improving Medical Multi-modal Contrastive Learning with Expert Annotations](improving_medical_multimodal_contrastive_learning_with_exper.md)**

:   提出eCLIP，通过引入放射科医生的眼动热力图（eye-gaze heatmap）作为专家标注，利用热力图处理器和mixup增强策略扩充高质量正样本对，有效缓解医学CLIP中的"模态间隙"问题，在零样本推理、线性探测、跨模态检索和RAG报告生成等任务上取得一致性提升。

**[Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification](pathologyknowledge_enhanced_multiinstance_prompt_learni.md)**

:   提出 PEMP——病理知识增强的多实例提示学习框架，将视觉和文本病理先验（典型 patch/slide 示例 + 语言描述）注入 CLIP 的提示中，在 patch 和 slide 两个层级进行对比学习，显著提升少样本全切片图像（WSI）分类性能。

**[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](textttnephi_neural_deformation_fields_for_approximately_diff.md)**

:   NePhi用隐式神经网络（SIREN）替代传统的体素化形变场来表示配准变换，通过编码器预测latent code + 可选的测试时优化实现快速且近似微分同胚的医学图像配准，在多分辨率设置下与SOTA精度相当但内存降低5倍。

**[TIP: Tabular-Image Pre-training for Multimodal Classification with Incomplete Data](tip_tabularimage_pretraining_for_multimodal_classification_w.md)**

:   提出TIP框架，通过掩码表格重建、图像-表格匹配和对比学习三个自监督任务，在表格数据不完整的条件下学习鲁棒的多模态表示，在自然图像和医学图像分类任务上超越现有方法。
