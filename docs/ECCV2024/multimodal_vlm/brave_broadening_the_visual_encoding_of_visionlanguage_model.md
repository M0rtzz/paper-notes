---
title: >-
  [论文解读] BRAVE: Broadening the Visual Encoding of Vision-Language Models
description: >-
  [ECCV 2024][多模态][视觉编码器融合] 通过系统benchmarking发现没有单一视觉编码器在所有VLM任务上最优，提出BRAVE方法用Multi-Encoder Querying Transformer（MEQ-Former）将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在多个captioning和VQA基准上达到SOTA。
tags:
  - ECCV 2024
  - 多模态
  - 视觉编码器融合
  - 多编码器
  - Q-Former
  - 多模态VLM
  - 视觉幻觉
---

# BRAVE: Broadening the Visual Encoding of Vision-Language Models

**会议**: ECCV 2024  
**arXiv**: [2404.07204](https://arxiv.org/abs/2404.07204)  
**代码**: [https://brave-vlms.epfl.ch](https://brave-vlms.epfl.ch)  
**领域**: 多模态VLM  
**关键词**: 视觉编码器融合, 多编码器, Q-Former, 视觉语言模型, 视觉幻觉

## 一句话总结
通过系统benchmarking发现没有单一视觉编码器在所有VLM任务上最优，提出BRAVE方法用Multi-Encoder Querying Transformer（MEQ-Former）将多个冻结编码器的特征融合为紧凑表示，以仅116M可训练参数在多个captioning和VQA基准上达到SOTA。

## 研究背景与动机
1. **领域现状**：VLM通常由视觉编码器（如CLIP）和语言模型组成，通过bridging网络连接。当前主流方法仅使用单一视觉编码器，在scaling方面主要集中在语言模型侧。
2. **现有痛点**：(1) CLIP等编码器存在"视觉盲区"——对某些视觉差异完全无法区分；(2) 单一编码器的归纳偏置限制了VLM的视觉理解广度；(3) 不同编码器在不同任务上各有优劣，没有"万能"编码器。
3. **核心矛盾**：机器学习中已知单一表示难以覆盖所有泛化需求，但如何高效组合多个异构编码器（不同架构、训练数据、模型大小）的特征是一个非平凡的工程和算法挑战。
4. **本文要解决什么？** (1) 系统评估不同视觉编码器对VLM任务的影响；(2) 设计高效的多编码器特征融合方法；(3) 用最少的可训练参数实现最大的视觉理解提升。
5. **切入角度**：从"scale the vision axis"的角度出发——相比scaling LM（10B+参数），scaling视觉编码器（多种bias组合）是一个低成本高回报的方向。
6. **核心idea一句话**：用MEQ-Former将5个不同bias的冻结编码器的特征重采样为固定长度的紧凑表示，作为soft visual prompt送入冻结LM，实现视觉能力的全面拓宽。

## 方法详解

### 整体框架
输入图片经过5个冻结视觉编码器（EVA-CLIP-g、CLIP-L/14、SILC-G/16、ViT-e、DINOv2-L/14）分别提取特征，线性投影到统一维度后序列拼接（1223×1408），由MEQ-Former通过cross-attention重采样为160×768的固定表示，再线性投影为LM的soft visual prompt。LM使用冻结的FlanT5-XL。

### 关键设计

1. **系统化的视觉编码器Benchmarking**：
    - 做什么：在统一框架下评估8个视觉编码器对VLM任务的影响
    - 核心思路：固定Q-Former和LM，只改变视觉编码器，在COCO captioning、VQAv2、OKVQA、GQA和MMVP上评估
    - 关键发现：(a) 不同编码器性能接近但各有优势领域；(b) MMVP对所有编码器都难（<27.3%）；(c) 编码器训练数据分布影响大于模型大小

2. **Multi-Encoder Querying Transformer（MEQ-Former）**：
    - 做什么：将任意数量编码器的特征融合为紧凑的固定长度表示
    - 核心思路：使用32×5=160个可学习query，加上text prompt tokens，通过12层Transformer的cross-attention与拼接后的多编码器特征交互。特征不加encoder-specific embedding，让MEQ-Former自行学习区分
    - 设计动机：(1) 重采样避免了多编码器特征拼接导致的quadratic自注意力开销；(2) 固定长度输出使不同编码器组合间公平比较；(3) 充当"bottleneck"有效压缩（14×压缩率）
    - 与Q-Former的区别：多编码器泛化版本，116M参数vs Q-Former的188M

3. **单阶段预训练 + Encoder Dropout**：
    - 做什么：简化训练流程并增强鲁棒性
    - 核心思路：跳过BLIP-2的两阶段预训练，直接用captioning目标训练MEQ-Former。训练时以20%概率随机mask各编码器的特征
    - 设计动机：encoder dropout作为正则化，防止MEQ-Former只关注某单一编码器的特征，确保多编码器的互补利用

### 损失函数 / 训练策略
预训练用100M WebLI图文对的captioning目标。下游captioning仅微调MEQ-Former，VQA微调MEQ-Former + LM。可选高分辨率微调（336×336）。总可训练参数仅116M（约占总10.3B参数的1%）。

## 实验关键数据

### 主实验

| 方法 | 可训练参数 | COCO CIDEr | NoCaps CIDEr | VQAv2 | OKVQA | GQA | MMVP |
|------|----------|------------|-------------|-------|-------|-----|------|
| PaLI-17B | 16.9B | **149.1** | 127.0 | **84.3** | 64.5 | - | - |
| InstructBLIP | 188M | - | 121.9 | - | 55.5 | 49.5 | 16.7 |
| LLaVA-1.5 | 13B | - | - | 80.0 | - | 63.3 | 24.7 |
| **BRAVE** | 116M | 148.0 | **127.6** | 82.5 | **66.0** | **66.3** | **42.0** |

### 消融实验

| 配置 | COCO Cap. | VQAv2 | OKVQA | 说明 |
|------|-----------|-------|-------|------|
| A0 (Full BRAVE) | 147.0 | 81.8 | 65.7 | 完整模型 |
| A1 (冻结LM for VQA) | - | 78.6 | 57.5 | LM微调对VQA很重要 |
| A3 (无encoder dropout) | 145.3 | 81.3 | 66.0 | dropout对captioning有帮助 |
| A8 (FlanT5-L替代XL) | 142.5 | 79.9 | 65.5 | LM规模也重要 |

### 关键发现
- BRAVE在MMVP上从24.7%（LLaVA-1.5）提升到42.0%，大幅减少了CLIP盲区问题
- 在NoCaps out-domain测试集上表现最优，说明多编码器增强了对novel类别的泛化
- 移除最多2个编码器后性能优雅降级，超过2个后严重下降——编码器间有冗余但也有独特贡献
- MEQ-Former vs Q-Former Ensemble：MEQ-Former用更少参数（116M vs 605M）获得更好性能
- 编码器注意力分数随任务自适应变化——MEQ-Former学会了根据任务类型选择性关注不同编码器

## 亮点与洞察
- **"Scale the vision axis"的新视角**：以往VLM研究主要在LM侧做scaling（模型更大、数据更多），本文证明在视觉侧做scaling（更多编码器、更多bias）也有巨大潜力，且参数效率更高。
- **编码器benchmarking具有参考价值**：对8个编码器的统一评估揭示了出人意料的发现——OpenCLIP比CLIP大得多但在多个任务上更差，DINOv2虽无文本监督但在VLM中也能发挥作用。
- **MMVP上的耀眼提升**：42% vs 24.7%是巨大进步，因为MMVP专门测试CLIP盲区，多编码器组合自然弥补了单一编码器的视觉缺陷。

## 局限性 / 可改进方向
- 5个编码器的推理成本较高（需要运行5个ViT），未来可探索编码器蒸馏或动态选择
- 仅在FlanT5-XL上验证，未测试更大的LM（如LLaMA-13B）
- 预训练数据仅100M，PaLI用1.6B——数据scaling可能进一步提升
- 视觉编码器的选择是手工指定的，可探索自动化的编码器选择策略

## 相关工作与启发
- **vs BLIP-2**：BLIP-2用单编码器Q-Former做特征重采样，BRAVE是其多编码器泛化版本，且参数更少（116M vs 188M）。
- **vs LLaVA/PaLI**：这些方法微调整个LM（10B+参数），BRAVE仅训练1%参数就获得竞争力甚至更好的结果。
- **vs I-MoF (Tong et al.)**：同样尝试多编码器，但I-MoF用简单融合且需要更多参数。BRAVE的MEQ-Former实现了更高效的融合。

## 补充说明
- 5个编码器覆盖了所有主流训练目标（ITC、MIM、Classification、LGC）和数据集
- MEQ-Former将1223×1408的拼接特征压缩为160×768，14倍压缩率
- 预训练时encoder dropout概率20%，防止过度依赖单一编码器
- 编码器特征不加位置编码或encoder-specific标记，让模型自行学习区分
- FlanT5-XL to FlanT5-L切换仅损失约2 CIDEr，说明视觉侧scaling的性价比更高
- POPE基准上BRAVE达87.6%，减少视觉幻觉效果显著
- LoRA微调LM可补偿70%的full fine-tuning性能差距，参数量仅十分之一

## 评分
- 新颖性: ⭐⭐⭐⭐ 多编码器VLM的系统研究和MEQ-Former设计有原创性
- 实验充分度: ⭐⭐⭐⭐⭐ 8个编码器benchmarking + 广泛的downstream评估 + 详细消融
- 写作质量: ⭐⭐⭐⭐⭐ 逻辑清晰，从benchmarking到方法设计层层递进
- 价值: ⭐⭐⭐⭐⭐ 对VLM社区具有实用指导意义，scale vision axis的理念值得推广

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] X-Former: Unifying Contrastive and Reconstruction Learning for MLLMs](x-former_unifying_contrastive_and_reconstruction_learning_for_mllms.md)
- [\[ECCV 2024\] IVTP: Instruction-Guided Visual Token Pruning for Large Vision-Language Models](ivtp_instruction-guided_visual_token_pruning_for_large_vision-language_models.md)
- [\[ECCV 2024\] Quantized Prompt for Efficient Generalization of Vision-Language Models](quantized_prompt_for_efficient_generalization_of_vision-language_models.md)
- [\[ECCV 2024\] REVISION: Rendering Tools Enable Spatial Fidelity in Vision-Language Models](revision_rendering_tools_enable_spatial_fidelity_in_vision-language_models.md)
- [\[ECCV 2024\] NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](navgpt-2_unleashing_navigational_reasoning_capability_for_large_vision-language_.md)

</div>

<!-- RELATED:END -->
