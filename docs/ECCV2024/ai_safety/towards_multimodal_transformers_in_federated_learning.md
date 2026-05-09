---
title: >-
  [论文解读] Towards Multi-modal Transformers in Federated Learning
description: >-
  [ECCV 2024][AI安全][联邦学习] 首次探索Transformer架构在转移式多模态联邦学习中的应用，提出FedCola框架，通过互补式本地训练（利用跨模态Transformer blocks）和协作式服务器聚合（选择性聚合self-attention层），在保护数据隐私的前提下有效训练多模态Transformer。
tags:
  - ECCV 2024
  - AI安全
  - 联邦学习
  - Transformer
  - 跨模态知识迁移
  - 模态互补
  - 协作聚合
---

# Towards Multi-modal Transformers in Federated Learning

**会议**: ECCV 2024  
**arXiv**: [2404.12467](https://arxiv.org/abs/2404.12467)  
**代码**: [https://github.com/imguangyu/FedCola](https://github.com/imguangyu/FedCola)  
**领域**: AI安全  
**关键词**: 联邦学习, 多模态Transformer, 跨模态知识迁移, 模态互补, 协作聚合

## 一句话总结
首次探索Transformer架构在转移式多模态联邦学习中的应用，提出FedCola框架，通过互补式本地训练（利用跨模态Transformer blocks）和协作式服务器聚合（选择性聚合self-attention层），在保护数据隐私的前提下有效训练多模态Transformer。

## 研究背景与动机
1. **领域现状**：多模态Transformer在集中训练中取得了突破性进展，但其训练需要大量高质量数据，而这些数据常分散在不同机构中且受隐私法规保护，形成"数据孤岛"。联邦学习提供了不直接访问原始数据的分布式训练范式。
2. **现有痛点**：(1) 现有多模态联邦学习要求客户端拥有配对的多模态数据，排除了仅有单一模态的客户端；(2) 跨模态客户端之间存在modality gap（不同模态间）和in-modality gap（同模态不同目标间）；(3) 现有方法（如CreamFL）依赖公共数据集做知识蒸馏，不符合隐私要求。
3. **核心矛盾**：单模态客户端有大量可用数据但无法参与多模态训练，多模态客户端有配对数据但数量有限。如何在仅传递模型参数的约束下，让单模态知识惠及多模态模型？
4. **本文要解决什么？** (1) 让持有未配对单模态数据的客户端参与多模态联邦训练；(2) 缩小跨模态gap和模态内gap；(3) 仅通过模型参数而非公共数据实现跨模态知识共享。
5. **切入角度**：利用Transformer的统一架构——不同模态共享相同的transformer block结构，跨模态的本地数据可以通过另一模态的transformer blocks编码。
6. **核心idea一句话**：利用Transformer跨模态的架构统一性，在本地训练时混入其他模态的模型权重做互补学习，在服务器聚合时选择性共享self-attention层做协作聚合。

## 方法详解

### 整体框架
系统由图像客户端、文本客户端和图像-文本多模态客户端组成。每轮联邦学习中：(1) 服务器下发全局模型；(2) 单模态客户端做互补本地训练（下载另一模态的transformer blocks做MoE式混合）；(3) 多模态客户端做标准跨模态检索训练；(4) 服务器先做模态内聚合，再做协作聚合（仅共享self-attention层）。

### 关键设计

1. **互补式本地训练（Complementary Local Training）**：
    - 做什么：让单模态客户端在本地训练时利用其他模态的模型知识
    - 核心思路：下载另一模态的transformer blocks，为每个线性层引入可学习gate $g$（初始化为0），输出为 $W_{local}x + g \cdot W_{out}x$。训练后计算等价权重 $W_{local} + g \cdot W_{out}$ 上传，通信成本不增加
    - 设计动机：由于Transformer block架构统一，图像的token化数据可以通过文本模态的blocks编码（反之亦然），gate机制让模型自适应学习跨模态知识的贡献度

2. **协作式聚合（Collaborative Aggregation）**：
    - 做什么：在不同模态类型间共享通用知识，同时保持各自任务特定知识
    - 核心思路："聚合+分离"策略——同模态的不同客户端类型（如图像客户端和多模态客户端的视觉部分）仅在self-attention层做加权聚合，MLP层保持各自独立。$\Omega^{attn}_{i,j} = \frac{n_i}{n_i+n_j}I$ 当 $\mathcal{M}(i)=\mathcal{M}(j)$
    - 设计动机：self-attention编码token间关系，蕴含更通用的知识；MLP适配本地目标，包含任务特定知识。选择性聚合实现了"取通用、保特定"

3. **补偿方案（Compensation Scheme）**：
    - 做什么：修复聚合/不聚合层之间的系数不对齐
    - 核心思路：将未协作层的更新系数缩放到与self-attention层相同的水平，避免层级和模态级别的不一致
    - 设计动机：直接选择性缩放会破坏同一客户端不同层之间训练产生的coherence

### 损失函数 / 训练策略
单模态客户端用交叉熵分类损失，多模态客户端用对比检索损失。默认30轮通信，每轮5个本地epoch，25%客户端参与率，Dirichlet α=0.5做non-IID数据分区。使用ImageNet预训练ViT-Small作为backbone。

## 实验关键数据

### 主实验

| 方法 | Flickr10k | COCO | 类型 |
|------|-----------|------|------|
| FedAvg | 81.08 | 95.42 | 单模态FL |
| CreamFL | 74.83 | 95.26 | 多模态FL (需公共数据) |
| FedIoT | 85.51 | 98.40 | 多模态FL |
| **FedCola** | **91.96** | **105.10** | 多模态FL (无需公共数据) |

### 消融实验

| 配置 | R@1_sum | 说明 |
|------|---------|------|
| FedAvg baseline | 81.08 | 无跨模态协作 |
| + Collaborative Aggregation (CA) | 88.70 | self-attention共享有效 |
| + CA + Compensation (CP) | 90.09 | 消除不对齐 |
| + CA + CP + Complementary Local (CL) | **91.96** | 完整FedCola |

### 关键发现
- FedCola在所有FL设置下（默认、更高异质性、更低参与率、不平衡客户端数）均显著优于其他方法
- 文本客户端的Shapley贡献值（6.14）>图像客户端（4.74），表明文本知识对多模态模型更有价值
- 互补训练中仅使用self-attention层做跨模态即可获得最佳性能-通信成本trade-off
- 增加单模态数据集数量可持续提升多模态性能（0→1→2数据集：81.08→91.96→93.25）
- 域间差距过大时FedCola仍领先但绝对性能下降

## 亮点与洞察
- **Transformer统一架构的FL新用法**：利用不同模态的Transformer blocks共享相同结构这一特性，实现了仅通过模型参数就能跨模态传递知识，无需公共数据或数据共享，真正满足隐私约束。
- **Gate机制+权重压缩的通信设计**：gate初始化为0保证初始不影响本地训练，训练后合并为等价权重使上传量不增加——简单但极为实用。
- **Shapley值分析提供了联邦公平性的视角**：量化每类客户端的贡献，为联邦学习中的激励机制和利润分配提供了依据。

## 局限性 / 可改进方向
- 大域间差距下性能下降明显（医学图像vs COCO），跨域协作的有效性需进一步研究
- 未处理系统异质性（不同客户端计算能力不同）
- 仅测试了视觉-语言两种模态，未扩展到音频、视频等更多模态
- 协作聚合目前仅限于同模态间，跨模态聚合的可能性未探索

## 相关工作与启发
- **vs CreamFL**：CreamFL依赖公共数据集做知识蒸馏，限制了应用场景。FedCola无需任何公共数据，仅通过模型参数实现知识迁移。
- **vs FedIoT**：FedIoT扩展FedAvg做多模态聚合但在大域差距下挣扎。FedCola通过互补训练+选择性聚合更稳健。
- **vs FedAvg/FedProx**：这些单模态FL baseline在Transformer下表现不错（ViT的鲁棒性），但FedCola抓住了多模态协作的额外收益。

## 补充说明
- Gate初始化为0保证不改变原始模型行为，训练中自适应学习跨模态贡献度
- 补偿方案确保聚合后不同层的更新系数一致，避免训练不稳定
- 仅共享self-attention最有效，共享整个block或MLP效果更差
- 跨模态客户端的补偿公式保证了数据量加权的一致性
- 下载成本可通过仅下载attention层（而非全部blocks）进一步降低
- 可扩展到3+个单模态数据集，性能持续提升（93.25 with 2 datasets）
- Dirichlet α=0.1（高异质性）下FedCola仍领先，展示了强鲁棒性
- 理论分析提供了收敛保证条件

## 评分
- 新颖性: ⭐⭐⭐⭐ 首次系统研究Transformer在多模态FL中的应用，框架设计有创新
- 实验充分度: ⭐⭐⭐⭐⭐ 多设置、多域差距、公平性分析、scalability分析，非常全面
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰、理论有收敛保证
- 价值: ⭐⭐⭐⭐ 对大规模多模态模型的联邦训练具有开创性意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Fisher Calibration for Backdoor-Robust Heterogeneous Federated Learning](fisher_calibration_for_backdoor-robust_heterogeneous_federated_learning.md)
- [\[ECCV 2024\] Unveiling Privacy Risks in Stochastic Neural Networks Training: Effective Image Reconstruction from Gradients](unveiling_privacy_risks_in_stochastic_neural_networks_training_effective_image_r.md)
- [\[ECCV 2024\] RingID: Rethinking Tree-Ring Watermarking for Enhanced Multi-Key Identification](ringid_rethinking_tree-ring_watermarking_for_enhanced_multi-key_identification.md)
- [\[ICLR 2026\] Co-LoRA: Collaborative Model Personalization on Heterogeneous Multi-Modal Clients](../../ICLR2026/ai_safety/co-lora_collaborative_model_personalization_on_heterogeneous_multi-modal_clients.md)
- [\[ECCV 2024\] Noise-Assisted Prompt Learning for Image Forgery Detection and Localization](noise-assisted_prompt_learning_for_image_forgery_detection_and_localization.md)

</div>

<!-- RELATED:END -->
