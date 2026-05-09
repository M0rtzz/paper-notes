---
title: >-
  [论文解读] Enhancing Visual Representation with Textual Semantics: Textual Semantics-Powered Prototypes for Heterogeneous Federated Learning
description: >-
  [CVPR 2026][优化][联邦原型学习] 提出 FedTSP，利用预训练语言模型（PLM）从文本模态构建语义丰富的原型，在异构联邦学习中保持类别间语义关系，通过可学习提示弥合模态鸿沟，显著提升模型性能并加速收敛。
tags:
  - CVPR 2026
  - 优化
  - 联邦原型学习
  - 预训练语言模型
  - 语义关系保持
  - 异构联邦学习
  - 跨模态对齐
---

# Enhancing Visual Representation with Textual Semantics: Textual Semantics-Powered Prototypes for Heterogeneous Federated Learning

**会议**: CVPR 2026  
**arXiv**: [2503.13543](https://arxiv.org/abs/2503.13543)  
**代码**: [https://github.com/XinghaoWu/FedTSP](https://github.com/XinghaoWu/FedTSP)  
**领域**: 优化  
**关键词**: 联邦原型学习, 预训练语言模型, 语义关系保持, 异构联邦学习, 跨模态对齐

## 一句话总结

提出 FedTSP，利用预训练语言模型（PLM）从文本模态构建语义丰富的原型，在异构联邦学习中保持类别间语义关系，通过可学习提示弥合模态鸿沟，显著提升模型性能并加速收敛。

## 研究背景与动机

1. **领域现状**：联邦原型学习（FedPL）通过共享全局原型来对齐客户端表征以缓解数据异构性，原型质量直接影响性能。
2. **现有痛点**：AlignFed、FedNH 等方法追求最大化类间原型距离（均匀分布在超球面），但这破坏了类别间的语义关系。例如，"马"和"狗"应比"马"和"卡车"更相似。
3. **核心矛盾**：增大原型距离虽增强类别区分，但不可避免地破坏了语义结构，而语义结构对模型泛化至关重要。
4. **本文目标**：构建既保持语义关系又有足够区分性的原型。
5. **切入角度**：利用 PLM 编码的丰富语义知识来构建原型，将语义结构"注入"联邦学习。
6. **核心 idea**：用 LLM 生成类别描述，PLM 编码为文本原型，可学习提示弥合图像-文本模态鸿沟。

## 方法详解

### 整体框架

Step 0: 服务器用 LLM 生成类别描述并用 PLM 编码为嵌入。Step 1-4 循环：客户端计算图像原型→服务器用可学习提示更新文本原型→服务器对齐文本和图像原型→分发文本原型给客户端用于本地对齐训练。

### 关键设计

1. **LLM 生成多视角提示**:

    - 功能：为每个类别生成细粒度文本描述以丰富语义上下文
    - 核心思路：模板 "A photo of {CLASS}: {description}"，每个类别生成 $k=3$ 个覆盖不同方面的描述。文本编码器处理后平均得到类别文本原型 $\bar{P}_c^T$。
    - 设计动机：单纯类名（"apple"）存在歧义且语义信息不足；多视角描述帮助编码器捕捉更细粒度的语义区分。

2. **可学习提示的模态对齐**:

    - 功能：弥合 PLM 与客户端图像模型之间的模态鸿沟
    - 核心思路：在文本嵌入序列中插入 $m$ 个可学习向量 $v_c$，替换前 $m$ 个 token 嵌入。每个类别的 $k$ 个提示共享同一组可学习提示。服务器聚合客户端图像原型后，通过对比损失 $\mathcal{L}_S$ 更新可学习提示使文本原型对齐图像原型。
    - 设计动机：PLM 未见过图像数据，直接用其特征作原型会存在模态鸿沟。可学习提示使文本原型适应客户端视觉任务。

3. **基于对比学习的语义传递**:

    - 功能：将原型的语义关系传递给客户端模型
    - 核心思路：客户端用对比学习损失对齐本地特征与文本原型：$\mathcal{R} = -\log \frac{\exp(\cos(f_i(x), \mathcal{P}_y^T)/\tau)}{\sum_c \exp(\cos(f_i(x), \mathcal{P}_c^T)/\tau)}$。温度参数 $\tau$ 使模型关注相对排名而非绝对值。
    - 设计动机：L2 对齐优化绝对相似度，会误导模型认为不相关类也相似。对比学习优化相对排名，自然保留语义结构。

### 损失函数 / 训练策略

客户端损失 = CE 损失 + $\lambda$ × 对比对齐损失。服务器侧用对比损失训练可学习提示 $E_s$ 轮。

## 实验关键数据

### 主实验

| 数据集 | 指标 | FedTSP-CLIP | FedTGP (之前SOTA) | 提升 |
|--------|------|-------------|-------------------|------|
| CIFAR-10 (α=0.1) | Acc | 87.34 | 85.73 | +1.61 |
| CIFAR-100 (α=0.1) | Acc | 45.61 | 41.37 | +4.24 |
| Tiny-ImageNet (α=0.1) | Acc | 34.82 | 31.16 | +3.66 |

### 消融实验

| 配置 | CIFAR-10 | CIFAR-100 | 说明 |
|------|----------|-----------|------|
| FedTSP-CLIP | 87.34 | 45.61 | CLIP 编码器 |
| FedTSP-BERT | 87.52 | 46.08 | BERT 编码器也有效 |
| 不使用 LLM 描述 | 下降明显 | - | LLM 描述至关重要 |

### 关键发现

- 在强数据异构（α=0.1）下提升最显著，说明文本原型对异构数据分布偏移更鲁棒
- BERT（未见过图像）也能有效工作，证明框架不依赖视觉-语言预训练
- Top-5 准确率提升更大，说明即使误分类也更可能分到语义相关类

## 亮点与洞察

- **语义结构保持的量化**：用 Spearman 相关系数和语义间隔两个指标量化原型的语义质量
- **框架无关性**：不依赖 CLIP，BERT 等纯文本模型也能工作
- **隐私保护扩展**：设计了差分隐私变体，对文本嵌入加噪以保护类名隐私

## 局限与展望

- 当前仅在图像分类任务上验证，未扩展到检测或分割
- LLM 生成描述的质量依赖具体类别，对细粒度类别可能不够精确
- 可学习提示的数量 $m$ 需要调优
- 当前仅支持分类任务，扩展到检测分割需要额外设计

## 相关工作与启发

- **vs AlignFed**: AlignFed 均匀分布原型，FedTSP 保持语义结构
- **vs FedTGP**: FedTGP 用可训练原型追求最大分离，忽略语义关系
- **vs CLIP-FL**: CLIP-FL 微调 CLIP 用于推理，FedTSP 将语义知识迁移到轻量客户端模型

## 评分

- 新颖性: ⭐⭐⭐⭐ 首次将文本语义引入联邦原型学习，跨模态知识迁移思路新颖
- 实验充分度: ⭐⭐⭐⭐ 多数据集、多异构设置、隐私扩展全面，消融系统化
- 写作质量: ⭐⭐⭐⭐⭐ 动机通过可视化阐释非常清晰，语义对齐和间隔量化指标设计巧妙
- 价值: ⭐⭐⭐⭐ 语义保持原型的思路有广泛迁移价值，可推广到其他需要跨模态知识传递的场景

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] The Power of Decaying Steps: Enhancing Attack Stability and Transferability for Sign-based Optimizers](the_power_of_decaying_steps_enhancing_attack_stability_and_transferability_for_s.md)
- [\[CVPR 2026\] SCOPE: Semantic Coreset with Orthogonal Projection Embeddings for Federated Learning](scope_semantic_coreset_with_orthogonal_projection.md)
- [\[CVPR 2026\] Dynamic Momentum Recalibration in Online Gradient Learning](dynamic_momentum_recalibration_in_online_gradient_learning.md)
- [\[CVPR 2026\] OTPrune: Distribution-Aligned Visual Token Pruning via Optimal Transport](otprune_distribution-aligned_visual_token_pruning_via_optimal_transport.md)
- [\[CVPR 2026\] BlazeFL: Fast and Deterministic Federated Learning Simulation](blazefl_fast_and_deterministic_federated_learning_simulation.md)

</div>

<!-- RELATED:END -->
