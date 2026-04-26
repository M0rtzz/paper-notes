---
title: >-
  [论文解读] CLAP: Isolating Content from Style Through Contrastive Learning with Augmented Prompts
description: >-
  [ECCV 2024][多模态][CLIP] 从因果生成模型视角出发，提出CLAP（Contrastive Learning with Augmented Prompts），通过文本增强（而非图像增强）在预训练CLIP的特征空间中解耦内容与风格信息，以极低训练成本（<1小时）显著提升CLIP在零样本/少样本分类和对抗鲁棒性上的表现。
tags:
  - ECCV 2024
  - 多模态
  - CLIP
  - 内容风格解耦
  - 因果表征学习
  - 数据增强
  - 鲁棒性
---

# CLAP: Isolating Content from Style Through Contrastive Learning with Augmented Prompts

**会议**: ECCV 2024  
**arXiv**: [2311.16445](https://arxiv.org/abs/2311.16445)  
**代码**: https://github.com/YichaoCai1/CLAP (有)  
**领域**: 多模态VLM  
**关键词**: CLIP, 内容风格解耦, 因果表征学习, 数据增强, 鲁棒性

## 一句话总结
从因果生成模型视角出发，提出CLAP（Contrastive Learning with Augmented Prompts），通过文本增强（而非图像增强）在预训练CLIP的特征空间中解耦内容与风格信息，以极低训练成本（<1小时）显著提升CLIP在零样本/少样本分类和对抗鲁棒性上的表现。

## 研究背景与动机
1. **领域现状**：CLIP等视觉语言模型通过对比学习获得了出色的泛化特征，但学到的特征将内容（content）和风格（style）信息混合在一起。
2. **现有痛点**：(1) CLIP容易依赖虚假相关性（spurious correlations），即利用风格信息来预测标签；(2) 对输入文本prompt高度敏感——不同prompt格式导致零样本性能波动大；(3) 分布偏移和对抗攻击下性能下降——因为风格信息在不同环境中变化。
3. **理论基础**：因果表征学习理论[von Kügelgen 2021]表明，数据增强可以视为对潜在风格变量的软干预（soft intervention），保持内容不变而改变风格。通过对比学习可以将不变的内容信息从可变的风格信息中分离出来。
4. **核心洞察**：文本数据因其高语义性和逻辑结构，比图像数据更容易实现针对性的风格修改。例如把"a photo of a dog"改成"a sketch of a dog"在文本域很容易，但在图像域很难。
5. **核心idea**：利用模板化prompt增强作为文本域的"风格干预"，在CLIP冻结特征空间上训练轻量解耦网络，分离内容特征。

## 方法详解

### 整体框架
分两条技术路线，最终CLAP（文本增强方案）优于Im.Aug（图像增强方案）：

**Im.Aug路径**：生成合成图像数据集→图像增强（裁剪+颜色扰动）→冻结CLIP图像编码器→训练解耦网络（InfoNCE损失）
**CLAP路径**：构建模板化文本prompt数据集→prompt增强（删除属性词/交换词序）→冻结CLIP文本编码器→训练解耦网络→推理时将解耦网络同时应用于图像和文本编码器

### 关键设计

1. **因果生成模型**：
    - 图像和文本共享潜在空间，包含内容变量c和风格变量s
    - s := g_s(c)，x := g_x(c,s)，t := g_t(c,s)，y := g_y(c)
    - 标签y仅由内容c决定，风格s不予决定→分离内容即消除虚假相关
    - 图像和文本共享同一潜在空间→文本域的风格干预等价于图像域的

2. **Prompt增强技术**：
    - 模板格式："a [art style] [image type] of a [object size] [object color] [class]"
    - 5种增强：OSD（删除物体大小）、OCD（删除物体颜色）、ITD（删除图像类型）、ASD（删除艺术风格）、SPO（交换词序）
    - 每种增强精确删除一个风格属性而不影响内容（类名）
    - 比图像增强更精准：图像masking可能损坏内容或风格变化不充分

3. **解耦网络结构**：
    - 残差MLP：主干分支（SiLU激活 + 正常初始化线性层 + 零初始化线性层）+ shortcut
    - 零初始化确保训练从预训练特征空间出发（灵感来自ControlNet的zero-conv）
    - 推理时引入标量参数α调节解耦强度
    - 极其轻量——仅两层MLP，不影响推理速度

4. **CLAP损失函数**：
    - 双项InfoNCE：ℒ(f_c∘f_t*; {t_i, t̃_i}) + λ·ℒ(f_c∘f_t*; {t_i^c, t̃_i})
    - 第二项用类名作anchor提升样本稀缺时的区分度
    - λ平衡两项贡献

### 损失函数 / 训练策略
- **Im.Aug**：InfoNCE损失在图像编码器上训练解耦网络
- **CLAP**：双项InfoNCE损失在文本编码器上训练解耦网络
- 训练数据：合成prompt文本（无需真实图像！），每类480个prompt
- 训练时间：PACS/VLCS约11分钟，DomainNet约47分钟（单3090 GPU）
- 推理：解耦网络同时接在图像编码器和文本编码器后面

## 实验关键数据

### 主实验（零样本分类，各域平均top-1准确率%）

| Prompt格式 | 方法 | PACS | VLCS | OfficeHome | DomainNet | 总均 |
|-----------|------|------|------|-----------|-----------|------|
| ZS(C) | CLIP | 95.7 | 76.4 | 79.8 | 57.8 | 77.4 |
|  | Im.Aug | 96.5 | 79.5 | 77.0 | 51.5 | 76.1 |
|  | **CLAP** | **97.2** | **82.6** | **81.0** | **58.7** | **79.9** |
| ZS(PC) | CLIP | 96.1 | 82.4 | 82.5 | 57.7 | 79.7 |
|  | **CLAP** | **97.2** | **83.4** | **83.0** | **59.0** | **80.7** |
| ZS(NC) | CLIP | - | - | - | - | 基线 |
|  | **CLAP** | - | - | - | - | 提升最显著 |

### 消融实验

| 增强组合 | 效果 |
|---------|------|
| 仅OSD | 有效但不充分 |
| 仅OCD | 有效但不充分 |
| 全部5种增强 | 最优 |
| 无λ正则项 | 少类别数据集下降 |
| α=0.5 vs 1.0 vs 2.0 | 需要按数据集调节 |

### 关键发现
1. CLAP在所有4个数据集上一致性超越CLIP和Im.Aug，而Im.Aug在50%的情况下反而降低了性能
2. CLAP对动态噪声prompt（ZS(NC)）的鲁棒性提升最为显著——evidence内容解耦有效消除了prompt敏感性
3. 文本增强比图像增强更有效——因为文本增强可以精确修改风格因素而保持内容
4. CLAP在few-shot线性探测和对抗攻击防御中也表现出一致性提升
5. 训练完全不需要真实图像——仅用模板化prompt文本即可

## 亮点与洞察
1. **理论驱动的实用方法**：将因果表征学习的理论成果落地到CLIP实践中
2. **文本增强优于图像增强**：反直觉但合理——文本的结构化特性使得"精确改变风格"更容易实现
3. **极低训练成本**：无需图像数据，仅用文本prompt，单GPU几十分钟完成训练
4. **即插即用**：解耦网络极轻量（两层MLP），不修改CLIP架构，不影响推理速度
5. **零初始化设计**：从预训练特征空间出发训练，避免了破坏已学表征

## 局限性 / 可改进方向
1. 模板化prompt的多样性有限（固定的颜色×尺寸×类型×风格），可能无法覆盖所有风格因素
2. α参数需要按数据集手动调节
3. 理论上要求所有风格因素都变化才能完全解耦，但实践中是否满足难以验证
4. 仅在分类任务上验证，未测试检索、生成等其他下游任务
5. 合成数据的域偏置可能影响泛化

## 相关工作与启发
- **CoOp/CoCoOp**：prompt learning方法关注任务特定prompt，CLAP从表征解耦角度改进CLIP
- **von Kügelgen et al. (2021)**：因果表征学习理论基础，证明增强+对比学习可以识别内容变量
- **ControlNet**：零初始化设计的灵感来源
- **启发**：对其他预训练模型（如BLIP-2、LLaVA），是否也可以通过文本增强解耦来提升鲁壒性？

## 评分
- 新颖性：⭐⭐⭐⭐ （文本增强解耦内容的视角新颖）
- 技术深度：⭐⭐⭐⭐ （因果理论→实用方法的完整链条）
- 实验充分性：⭐⭐⭐⭐ （零样本/少样本/对抗攻击多维评估）
- 实用价值：⭐⭐⭐⭐⭐ （训练成本极低、即插即用）
- 写作质量：⭐⭐⭐⭐ （理论和实践衔接流畅）

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] SpLIP: Elevating All Zero-Shot Sketch-Based Image Retrieval Through Multimodal Prompt Learning](elevating_all_zeroshot_sketchbased_image_retrieval_through_m.md)
- [\[ECCV 2024\] Bad Students Make Great Teachers: Active Learning Accelerates Large-Scale Visual Understanding](classact_active_learning.md)
- [\[ECCV 2024\] Meta-Prompting for Automating Zero-shot Visual Recognition with LLMs](metaprompting_for_automating_zeroshot_visual_recognitio.md)
- [\[ECCV 2024\] X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs](xformer_unifying_contrastive_and_reconstruction_learning_for.md)
- [\[ECCV 2024\] AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_vision-language_models_for_city-wide_image_address_locali.md)

<!-- RELATED:END -->
