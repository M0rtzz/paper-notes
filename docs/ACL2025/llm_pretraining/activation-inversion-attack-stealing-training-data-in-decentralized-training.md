---
title: >-
  [论文解读] Stealing Training Data from Large Language Models in Decentralized Training through Activation Inversion Attack
description: >-
  [ACL 2025][去中心化训练] 本文首次提出针对去中心化训练的激活反转攻击（AIA），通过构建影子数据集训练攻击模型，恶意阶段可以从传输的激活值中重建训练数据，在 GPT2-XL 上实现了 62% 的邮件地址窃取准确率。
tags:
  - ACL 2025
  - 去中心化训练
  - LLM预训练
  - 激活反转
  - 数据泄露
  - 管道并行
---

# Stealing Training Data from Large Language Models in Decentralized Training through Activation Inversion Attack

**会议**: ACL 2025  
**arXiv**: [2502.16086](https://arxiv.org/abs/2502.16086)  
**代码**: 无  
**领域**: LLM预训练  
**关键词**: 去中心化训练, 隐私攻击, 激活反转, 数据泄露, 管道并行

## 一句话总结

本文首次提出针对去中心化训练的激活反转攻击（AIA），通过构建影子数据集训练攻击模型，恶意阶段可以从传输的激活值中重建训练数据，在 GPT2-XL 上实现了 62% 的邮件地址窃取准确率。

## 研究背景与动机

1. **领域现状**：去中心化训练（基于管道并行）是降低 LLM 训练资源门槛的重要框架，但其安全性研究主要集中在容错和模型收敛攻击，隐私风险被忽视。
2. **现有痛点**：现有攻击研究要么需要控制整个模型（不现实），要么关注联邦学习中的梯度泄露（不适用于管道并行），要么假设攻击者可以篡改传输值（容易被检测）。
3. **核心矛盾**：去中心化训练中恶意阶段只能访问部分模型和传输的激活值/梯度，但传统的隐私攻击需要完整模型或完整梯度。
4. **本文目标**：在不干扰训练过程（避免被检测）的前提下，仅通过传输的激活值重建训练数据。
5. **切入角度**：预训练模型和微调模型在早期层的激活值高度相似（余弦相似度接近100%），这意味着可以用预训练模型的激活构建影子数据集。
6. **核心 idea**：用公开的预训练模型生成影子激活-文本配对，训练生成式攻击模型学习"激活→文本"的逆映射。

## 方法详解

### 整体框架

AIA 分两步：(1) 影子数据集构建——用预训练模型（作为影子模型）在公开文本上生成激活值，构建（激活, 文本）配对；(2) 攻击模型训练——用影子数据集训练一个解码器模型，学习从激活值生成文本。推理时，将受害者训练过程中传输的激活值输入攻击模型即可重建训练数据。

### 关键设计

1. **影子数据集构建**:

    - 功能：创建用于训练攻击模型的（激活值, 文本）配对
    - 核心思路：直接从 HuggingFace 下载与受害者模型同架构的预训练模型作为影子模型，用公开数据集（如WikiText）前向传播获取指定层的激活值。关键观察：预训练模型和微调模型在相同数据上的早期层激活余弦相似度接近100%，后期层也保持50%以上。
    - 设计动机：攻击者无法访问受害者的训练数据，但预训练模型的泛化性保证了激活的稳定性，无需额外训练影子模型。

2. **攻击模型设计**:

    - 功能：学习从激活值到文本的逆映射
    - 核心思路：攻击模型与受害者模型架构相同（如都是GPT2风格），由若干解码器层和 lm_head 组成，但去掉了 embedding 层——直接以激活值为输入。使用 teacher forcing 训练标准语言模型损失：$L = -\sum_{k=1}^{N}\log P(y_k|x_1, ..., x_{k-1})$。
    - 设计动机：架构一致性是攻击成功的关键——实验表明使用不同架构（如 Mistral 或 Qwen2.5）的攻击模型困惑度飙升到数千，几乎完全失效。

3. **诚实但好奇的威胁模型**:

    - 功能：定义攻击场景的现实约束
    - 核心思路：攻击者控制管道中的一个阶段，正常参与训练（不被检测），只被动记录接收到的激活值。攻击者知道受害者模型的架构但不知道训练数据。
    - 设计动机：这比篡改型攻击更难被发现，更贴近实际场景。

### 损失函数 / 训练策略

- 攻击模型：标准自回归语言模型损失（teacher forcing）
- 受害者模型微调 5 个 epoch（故意过拟合以最大化特征差距），分 6 个管道阶段

## 实验关键数据

### 主实验

| 模型 | 数据集 | PPL | ROUGE-1 | ROUGE-L | BLEU-4 | COS |
|------|-------|-----|---------|---------|--------|-----|
| GPT2-XL | PIIs | 3.73 | 0.84 | 0.84 | 0.59 | 0.89 |
| GPT2-XL | OpenWebText | 3.09 | 0.95 | 0.95 | 0.77 | 0.94 |
| Bloom-7B1 | PIIs | 14.82 | 0.80 | 0.80 | 0.47 | 0.89 |
| LLaMA3-8B | PIIs | 7.36 | 0.80 | 0.79 | 0.54 | 0.77 |

### 隐私泄露实验

| 模型 | 方法 | 手机号ASR | 邮箱ASR |
|------|------|----------|---------|
| GPT2-XL | True-Prefix | 0% | 4% |
| GPT2-XL | SPT | 0% | 2% |
| **GPT2-XL** | **AIA** | **25%** | **55%** |
| **Bloom-7B1** | **AIA** | **42%** | **62%** |

### 关键发现

- 攻击效果与层数位置高度相关：越靠近输入层攻击越成功，越靠近输出层攻击效果下降
- 攻击效果与模型大小无关——从355M到7B参数的模型上表现稳定
- 攻击模型必须与受害者模型架构一致，否则几乎完全失效
- 生日和职业的恢复率接近100%，而比特币地址和UUID等长随机序列恢复率较低

## 亮点与洞察

- **首次揭示去中心化训练中的隐私泄露风险**：这是一个重要的安全发现，随着去中心化训练的普及，这类攻击的现实威胁会越来越大。
- **预训练-微调激活相似性**是攻击的核心利用点：这个观察不仅对攻击有用，也说明了微调对模型内部表示的影响比想象中更小。
- 攻击无需干扰训练过程，"诚实但好奇"的威胁模型使攻击几乎不可能被检测。

## 局限与展望

- 攻击模型必须与受害者模型架构完全一致，限制了攻击的通用性
- 生成的文本在大小写、特殊字符、低频词等方面仍有错误
- 仅测试了微调场景，预训练阶段的激活变化更大，攻击效果可能下降
- 需要开发有效的防御措施（如差分隐私、激活扰动等）

## 相关工作与启发

- **vs 深度梯度泄露**：在联邦学习中有效，但去中心化训练中每个阶段只有部分梯度，难以直接应用
- **vs 嵌入反转攻击**：假设可以访问完整训练好的模型，AIA 只需要传输的中间激活
- **vs True-Prefix/SPT攻击**：需要已训练好的完整模型来提示，AIA 在训练过程中就能窃取数据

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首次识别去中心化训练中的隐私攻击面，攻击方法新颖且实用
- 实验充分度: ⭐⭐⭐⭐ 多模型多数据集测试，消融分析全面
- 写作质量: ⭐⭐⭐⭐ 威胁模型清晰，图示直观
- 价值: ⭐⭐⭐⭐⭐ 重要的安全发现，对去中心化训练社区有警示意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ACL 2025\] Retrofitting Large Language Models with Dynamic Tokenization](retrofitting_large_language_models_with_dynamic_tokenization.md)
- [\[ACL 2025\] Pre-Training Curriculum for Multi-Token Prediction in Language Models](pre-training_curriculum_for_multi-token_prediction_in_language_models.md)
- [\[ACL 2025\] AsyncLM: Efficient and Adaptive Async Pre-training of Language Models](asynclm_efficient_and_adaptive_async_pre-training_of_language_models.md)
- [\[ACL 2025\] Large Vocabulary Size Improves Large Language Models](large_vocabulary_size_improves_large_language_models.md)
- [\[ACL 2025\] Data-Constrained Synthesis of Training Data for De-Identification](data-constrained_synthesis_of_training_data_for_de-identification.md)

</div>

<!-- RELATED:END -->
