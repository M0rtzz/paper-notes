---
title: >-
  CVPR2026 联邦学习论文汇总 · 4篇论文解读
description: >-
  4篇CVPR2026的联邦学习方向论文解读，涵盖联邦学习、个性化生成、对齐/RLHF、扩散模型等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2026"
  - "联邦学习"
  - "论文解读"
  - "论文笔记"
  - "个性化生成"
  - "对齐/RLHF"
  - "扩散模型"
item_list:
  - u: "fully_decentralized_certified_unlearning/"
    t: "Fully Decentralized Certified Unlearning"
  - u: "gdfa_geometry-driven_federated_unlearning_with_directional_task_vector_alignment/"
    t: "GDFA: Geometry-Driven Federated Unlearning with Directional Task Vector Alignment"
  - u: "hilora_hierarchical_low-rank_adaptation_for_personalized_federated_learning/"
    t: "HiLoRA: Hierarchical Low-Rank Adaptation for Personalized Federated Learning"
  - u: "personalized_federated_training_of_diffusion_models_with_privacy_guarantees/"
    t: "Personalized Federated Training of Diffusion Models with Privacy Guarantees"
item_total: 4
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🤝 联邦学习

**📷 CVPR2026** · **4** 篇论文解读

🔥 **高频主题：** 联邦学习 ×3 · 个性化生成 ×2

**[Fully Decentralized Certified Unlearning](fully_decentralized_certified_unlearning.md)**

:   针对"无中心协调者的去中心化网络"这一被忽视的场景，本文提出 RR-DU——一个随机游走式的认证遗忘算法：只在发起删除的客户端上对遗忘集做带噪投影梯度上升、其余客户端继续做无噪下降，配合子采样高斯噪声和信任域投影，证明了 $(\varepsilon,\delta)$ 网络遗忘证书、收敛性与删除容量边界，且噪声不随遗忘集大小 $m$ 增长，在图像分类上把后门攻击成功率压到随机猜测水平同时保住干净精度。

**[GDFA: Geometry-Driven Federated Unlearning with Directional Task Vector Alignment](gdfa_geometry-driven_federated_unlearning_with_directional_task_vector_alignment.md)**

:   GDFA 把"联邦遗忘"重新理解成一个**损失曲面几何**问题：先用扰动把全局模型迁到平坦极小值区，再让相关客户端在遗忘数据上生成任务向量、只保留**方向一致（符号共识）**的分量做反向聚合，从而在 Non-IID 场景下精确擦除目标客户端知识，同时几乎不损失保留任务精度。

**[HiLoRA: Hierarchical Low-Rank Adaptation for Personalized Federated Learning](hilora_hierarchical_low-rank_adaptation_for_personalized_federated_learning.md)**

:   HiLoRA 把每个客户端的 LoRA 更新拆成"根—簇—叶"三层正交子空间，分别承载全局共识、子群共性与客户端个性，再配上一个基于 LoRA 子空间相似度的自适应聚类，在 CIFAR-100 与 DomainNet 上同时把个性化和对新客户端的泛化都做到 SOTA。

**[Personalized Federated Training of Diffusion Models with Privacy Guarantees](personalized_federated_training_of_diffusion_models_with_privacy_guarantees.md)**

:   PFDM 把扩散模型的反向去噪过程拆成"客户端私有去噪器 + 服务器共享去噪器"两块，客户端只上传经裁剪并前向加噪后的数据，从而对每个数据点给出形式化的本地差分隐私（LDP）保证；共享模型只见加噪数据、单独无法复现任何客户端样本，而协同又能显著提升少数类/欠表示类的生成质量。
