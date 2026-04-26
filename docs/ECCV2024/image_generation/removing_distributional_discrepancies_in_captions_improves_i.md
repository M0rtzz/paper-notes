---
title: >-
  [论文解读] Removing Distributional Discrepancies in Captions Improves Image-Text Alignment
description: >-
  [ECCV 2024][图像生成][图文对齐] 发现训练图文对齐模型时正负caption之间存在被忽视的数据集级别分布偏差（如GPT生成负样本时倾向用elephant替换giraffe），提出用纯文本分类器过滤高置信样本来消除偏差，结合替换型+交换型两类负样本微调LLaVA-1.5，在Winoground、SeeTRUE等多个基准上大幅超越现有方法。
tags:
  - ECCV 2024
  - 图像生成
  - 图文对齐
  - 负样本生成
  - 分布偏差
  - LLaVA
  - 组合理解
---

# Removing Distributional Discrepancies in Captions Improves Image-Text Alignment

**会议**: ECCV 2024  
**arXiv**: [2410.00905](https://arxiv.org/abs/2410.00905)  
**代码**: https://yuheng-li.github.io/LLaVA-score/ (有)  
**领域**: 多模态VLM  
**关键词**: 图文对齐, 负样本生成, 分布偏差, LLaVA, 组合理解

## 一句话总结
发现训练图文对齐模型时正负caption之间存在被忽视的数据集级别分布偏差（如GPT生成负样本时倾向用elephant替换giraffe），提出用纯文本分类器过滤高置信样本来消除偏差，结合替换型+交换型两类负样本微调LLaVA-1.5，在Winoground、SeeTRUE等多个基准上大幅超越现有方法。

## 研究背景与动机
1. **领域现状**：自动评估图文对齐对数据清洗和T2I/I2T模型评估至关重要。CLIP score是最常用指标，但CLIP等模型对组合推理（如"horse eating grass" vs "grass eating horse"）理解能力不足。
2. **现有痛点**：(1) 训练对齐模型的标准方法是生成负样本caption，但仅保证单实例级别语法正确是不够的；(2) 已有方法（如NegCLIP随机打乱词序、VQ2用GPT生成）忽视了正负caption之间的分布级别偏差；(3) 模型可能仅凭文本偏差做预测而不看图像。
3. **关键发现**：用纯文本分类器（无图像输入）就能以很高准确率区分正负caption！例如COCO中"giraffe"在正样本中frequent，但GPT生成负样本时常用"elephant"替换→模型学到"包含elephant的=负样本"。
4. **核心矛盾**：数据偏差使图文对齐模型退化为"文本模式判别器"，无法真正学习跨模态对齐。
5. **核心idea**：(1) 生成混合类型负样本（替换+交换）增加多样性；(2) 训练文本-only分类器检测偏差→移除高置信样本→消除分布差异。

## 方法详解

### 整体框架
1. 正样本：COCO数据集的image-caption pairs
2. 负样本生成：GPT生成两类（替换型+交换型）
3. 偏差过滤：N-fold交叉验证训练BERT文本分类器→移除top-k%高置信正确预测样本
4. 模型训练：用过滤后数据微调LLaVA-1.5，prompt格式"Does this image match the following caption? Answer Yes or No directly."

### 关键设计

1. **混合类型负样本生成**：
    - **替换策略**：GPT识别caption关键组件并替换为合理替代品
     - 例如："a broken down stop sign" → "a brand new stop sign"
     - 增强模型的**识别能力**——区分被替换的元素
    - **交换策略**：GPT提取关键组件后重组为语义不同的新句子
     - 例如："an airplane is flying in the blue sky" → "a blue airplane is flying in the sky"
     - 增强模型的**推理能力**——元素相同但关系变化
    - 两类负样本互补：替换型考验感知，交换型考验推理

2. **分布偏差检测与消除**：
    - 做什么：训练纯文本二分类器，仅用文本（不看图像）区分正负caption
    - 关键发现：分类器竟然能高准确率区分！→说明正负caption分布有可利用的偏差
    - 解决方案：N-fold交叉验证（N=5），每折留出1/N作测试集→训练BERT分类器→对测试集中高置信正确预测的top-k%样本移除（正负样本各移除k%）
    - k=30%, N=5
    - 本质目标：最大化文本信息的熵——使正负caption在文本域上不可区分

3. **LLaVA-1.5的对齐评分器改造**：
    - 原始LLaVA是文本生成模型→改造为评分器
    - 提取"Yes"和"No"的logits，得到对齐分数：e^P(Yes) / (e^P(Yes) + e^P(No))
    - 用过滤后数据微调，标签"Yes"对应正样本，"No"对应负样本

### 损失函数 / 训练策略
- LLaVA-1.5微调：标准语言建模交叉熵loss
- 配置：batch size 64，8×A100，1 epoch，lr=2e-6
- 过滤参数：k=30%，N=5
- 还验证了BLIP2 Q-former + ITM head的微调，证明方法的通用性

## 实验关键数据

### 主实验

| 方法 | Winoground(image/text/group) | SeeTRUE DrawBench | SugarCrepe replace | SugarCrepe swap |
|------|----------------------------|-------------------|-------------------|-----------------|
| CLIP-ViT-L | 10.5/28.5/7.75 | 61.4 | 79.4 | 61.4 |
| NegCLIP | 11.75/30.75/8.25 | 63.2 | 85.3 | 75.3 |
| BLIP2-ITM | 24.25/41.75/19.0 | 60.8 | 88.9 | 83.9 |
| Image-Reward | 15.25/43.0/12.75 | 70.4 | 88.2 | 81.0 |
| VisualGPT | 37.0/44.25/27.5 | 77.0 | 88.2 | 87.1 |
| VQ2 (PaLI) | 42.25/47.0/30.5 | 82.6 | - | - |
| LLaVA-1.5 zero-shot | 38.5/52.0/30.5 | - | - | - |
| **LLaVA-score (Ours)** | **51.5/58.25/40.0** | **86.2** | **94.3** | **92.8** |

### 消融实验

| 设计选项 | 效果 |
|---------|------|
| 仅替换型负样本 | 效果有限 |
| 仅交换型负样本 | 效果有限 |
| 替换+交换 | 互补提升 |
| 无偏差过滤 | 显著下降（模型依赖文本偏差） |
| 过滤k=10%/20%/30%/40% | k=30%最优 |
| 对其他方法也有偏差 | DAC等方法同样存在分布偏差 |

### 关键发现
1. LLaVA-score在Winoground group score达到40.0%，远超曾经SOTA的VQ2的30.5%
2. 未微调的LLaVA-1.5 zero-shot已经是第二好的方法——验证了VLM内在的强对齐能力
3. 分布偏差是普遍问题——不仅限于本文方法，NegCLIP、DAC等用其他规则/模型生成负样本同样存在
4. 偏差过滤在几乎所有设置中都带来一致性提升
5. 该方法也能提升BLIP2的对齐性能，证明了通用性
6. 在T2I图像排序任务中也表现出色——可用于评估生成模型

## 亮点与洞察
1. **发现被忽视的新问题**：数据集级别的正负分布偏差——此前关注的是实例级别的质量
2. **简洁有效的解决方案**：用纯文本分类器检测偏差→高置信样本移除，原理清晰实用
3. **训练数据的通用性**：方法不依赖特定模型，可应用于LLaVA、BLIP2等多种VLM
4. **可视化直觉**：Figure 4清晰展示了分布偏差的实例（giraffe→elephant、surfing的正样本偏向性），说服力强

## 局限性 / 可改进方向
1. k值（过滤比例）的选择仍需手动调节
2. 过滤后数据量减少可能影响某些场景的训练充分性
3. 主要在COCO上构建训练数据，数据集特定的偏差可能无法完全泛化
4. GPT生成负样本的成本较高
5. 文本分类器本身可能引入新的偏差

## 相关工作与启发
- **NegCLIP**：随机打乱词序生成负样本→被发现正负caption语法就可区分
- **DAC/SugarCrepe**：用语法和常识模型过滤不合理负样本→仍有分布偏差
- **VQ2**：分解为QA对评估→不够end-to-end
- **启发**：其他需要正负样本对训练的任务（检索、对比学习）是否也存在类似的分布偏差？

## 评分
- 新颖性：⭐⭐⭐⭐⭐ （发现并解决了一个被忽视的基本问题）
- 技术深度：⭐⭐⭐ （方法本身简单，但问题发现有洞察力）
- 实验充分性：⭐⭐⭐⭐⭐ （多基准、多基线、充分消融）
- 实用价值：⭐⭐⭐⭐ （图文对齐评估的实用工具）
- 写作质量：⭐⭐⭐⭐⭐ （问题阐述极好，figure说服力强）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] LCM-Lookahead for Encoder-based Text-to-Image Personalization](lcm-lookahead_for_encoder-based_text-to-image_personalization.md)
- [\[ECCV 2024\] Latent Guard: a Safety Framework for Text-to-Image Generation](latent_guard_a_safety_framework_for_text-to-image_generation.md)
- [\[ECCV 2024\] Powerful and Flexible: Personalized Text-to-Image Generation via Reinforcement Learning](powerful_and_flexible_personalized_text-to-image_generation_via_reinforcement_le.md)
- [\[ECCV 2024\] LivePhoto: Real Image Animation with Text-guided Motion Control](livephoto_real_image_animation_with_text-guided_motion_control.md)
- [\[ECCV 2024\] MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed Precision Quantization](mixdq_memory-efficient_few-step_text-to-image_diffusion_models_with_metric-decou.md)

<!-- RELATED:END -->
