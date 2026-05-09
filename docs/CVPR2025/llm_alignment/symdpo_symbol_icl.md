---
title: >-
  [论文解读] SymDPO: Boosting In-Context Learning of Large Multimodal Models with Symbol Demonstration Direct Preference Optimization
description: >-
  [CVPR 2025][LLM对齐][上下文学习] 本文提出SymDPO，通过将多模态上下文示例中的文本答案替换为无语义关联的随机符号，迫使大多模态模型必须真正理解视觉信息才能正确回答，从而解决了LMM在上下文学习中忽视视觉信息、过度依赖文本模式的问题。
tags:
  - CVPR 2025
  - LLM对齐
  - 上下文学习
  - 多模态大模型
  - 偏好优化
  - 符号替换
  - 视觉理解
---

# SymDPO: Boosting In-Context Learning of Large Multimodal Models with Symbol Demonstration Direct Preference Optimization

**会议**: CVPR 2025  
**arXiv**: [2411.11909](https://arxiv.org/abs/2411.11909)  
**代码**: [https://github.com/APiaoG/SymDPO](https://github.com/APiaoG/SymDPO)  
**领域**: LLM对齐  
**关键词**: 上下文学习, 多模态大模型, 偏好优化, 符号替换, 视觉理解

## 一句话总结
本文提出SymDPO，通过将多模态上下文示例中的文本答案替换为无语义关联的随机符号，迫使大多模态模型必须真正理解视觉信息才能正确回答，从而解决了LMM在上下文学习中忽视视觉信息、过度依赖文本模式的问题。

## 研究背景与动机
1. **领域现状**：大型多模态模型（LMM）已展现出上下文学习（ICL）能力，能通过少量多模态示例完成任务，但其ICL表现主要依赖文本模式。
2. **现有痛点**：LMM在ICL场景中存在"视觉上下文忽视"问题——用空白图替换示例中的图像甚至去掉图像，性能反而不降反升，说明模型并未有效利用视觉信息。
3. **核心矛盾**：现有DPO方法缺乏专门针对多模态上下文指令跟随的机制，且在VQA任务中许多问题仅凭文本就能回答，难以构建有效区分视觉依赖的偏好数据。
4. **本文目标**：设计一种方法强制LMM在ICL中依赖视觉信息，建立图像内容与答案之间的真实映射关系。
5. **切入角度**：如果将ICL示例中的文本答案替换为无意义符号，模型就无法通过文本模式猜答案，必须通过理解图像来建立符号与答案的映射。
6. **核心idea**：使用符号替换构建DPO训练数据，让正确答案是与示例图像内容匹配的符号，错误答案是不匹配的符号或文本。

## 方法详解

### 整体框架
VQA数据集 → 构建ICL格式数据（示例+查询）→ 构建标准DPO数据（正确vs错误答案）→ 符号替换生成SymDPO数据（5种配置）→ 使用DPO损失训练LMM → 增强的ICL能力。数据来源包括GQA（问答）、VQAv2（视觉问答）和ImageNet（分类），按任务类型分组确保示例中至少包含两种不同答案。

### 关键设计

1. **ICL数据构建**:

    - 功能：将VQA数据组织为ICL格式，确保示例间有足够的答案多样性。
    - 核心思路：从GQA、VQAv2、ImageNet等数据集收集图像-问题-答案三元组，按任务类型分组（如是否问题、颜色问题等），构建为 $D_1, D_2, ..., D_N, F$ 的ICL格式，确保示例中至少包含两种不同答案。
    - 设计动机：需要保证模型不能简单通过多数投票猜答案，必须理解每个示例的视觉内容。

2. **符号替换策略（Symbol Substitution）**:

    - 功能：将ICL示例中的文本答案替换为无语义关联的符号字符串。
    - 核心思路：将示例 $D_i = \{I_i, Q_i, A_i\}$ 转化为 $\dot{D}_i = \{I_i, Q_i, S_i\}$，其中 $S_i$ 是与答案无关的随机符号（如"rhondda"替代"narrow"）。查询的正确答案为对应符号 $S_k$（与某个示例答案匹配的符号），错误答案为其他符号或无关文本。
    - 设计动机：剥离文本语义信息后，模型必须通过理解图像内容来建立图像→符号的映射，才能回答正确。

3. **五种SymDPO数据配置**:

    - 功能：通过多种配置增加训练数据多样性，全面提升模型的多模态理解。
    - 核心思路：包括是否擦除示例中的问题、rejected答案是语义相关还是另一个符号等不同组合，最终数据集保持各类型均衡比例。
    - 设计动机：不同配置从不同角度强制模型利用视觉信息，提高泛化能力。

### 损失函数 / 训练策略
使用标准DPO损失：$\mathcal{L}_S(\pi_\theta; \pi_{ref}) = -\mathbb{E}_{(x,y_w,y_l)\sim\mathcal{D}_S}\log\sigma\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)$，其中输入 $x = \{q, I, C\}$ 包含问题、图像和符号化的上下文。在COCO Caption和Flickr 30K上报告CIDEr分数，在VQAv2、OK-VQA和TextVQA上报告Accuracy。

## 实验关键数据

### 主实验

| 模型 | 方法 | COCO (CIDEr) | Flickr (CIDEr) | VQAv2 (Acc) | OK-VQA (Acc) |
|------|------|-------------|----------------|-------------|-------------|
| OF-3B (4-shot) | Base | 82.7 | 59.1 | 45.7 | 30.6 |
| OF-3B (4-shot) | +SymDPO | **87.4** (+4.7) | **61.2** (+2.1) | **46.2** (+0.5) | **31.6** (+1.0) |
| OF-3B (4-shot) | +General DPO | 83.5 (+0.8) | 60.0 (+0.9) | 46.0 (+0.3) | 30.7 (+0.1) |
| OF-3B (8-shot) | +SymDPO | **91.2** (+3.4) | **65.3** (+4.6) | **46.5** (+0.6) | **32.7** (+1.2) |

### 消融实验

| 配置 | COCO (CIDEr) | VQAv2 (Acc) | 说明 |
|------|-------------|-------------|------|
| SymDPO (全部5种) | 87.4 | 46.2 | 完整模型 |
| 仅配置1 (基础符号) | 85.8 | 45.9 | 单一配置效果弱 |
| 仅General DPO | 83.5 | 46.0 | 无符号替换效果差 |
| Video DPO | 82.5 | 45.5 | 视频DPO对ICL无效 |

### 关键发现
- SymDPO在所有模型架构（OpenFlamingo、IDEFICS等）和所有shot数上均一致性提升。
- 随着shot数增加，SymDPO的提升更加显著（IDEFICS-9B: 4-shot +3.5→8-shot +6.8→16-shot +8.2 CIDEr），说明它真正增强了ICL能力。
- 通用DPO仅带来微小提升（+0.2~0.8），Video DPO和MIA-DPO也无显著改善，证明符号替换策略是核心贡献。
- SymDPO使模型在替换示例图像为空白后性能显著下降，说明模型确实学会了利用视觉信息。
- 实现细节：从VQAv2、GQA、ImageNet训练集构建87.2万数据项，随机选1万样本经GPT-4v增强后训练。学习率5e-6线性退火，8×A100训练约1小时。

## 亮点与洞察
- **符号替换的思路极其巧妙**：通过一个简单的数据构造技巧，就解决了LMM忽视视觉信息的顽疾。核心洞察是"如果文本本身没有语义，模型就必须看图"。
- **可迁移到其他多模态任务**：任何需要模型真正理解视觉内容的场景，都可以用类似的符号替换策略来强制视觉对齐。
- **验证方法直观**：通过对比"去图"前后的性能差异来验证模型是否真正使用了视觉信息，是一个好的评估范式。
- **与其他DPO方法的对比清晰**：Video DPO面向视频语义对齐、MIA-DPO面向多图指令对齐，两者都未解决ICL场景的视觉忽视问题，仅带来微小提升（+0.1~0.7），而SymDPO在IDEFICS-9B 16-shot上达+8.2 CIDEr。

## 局限与展望
- 仅在VQA和Image Captioning任务上验证，未涉及更复杂的推理任务。
- 符号替换可能在答案空间非常大的开放式问题上效果减弱。
- 训练数据构建依赖于有明确答案分类的VQA数据集。
- 未来可探索在视频理解、多轮对话等更复杂场景中的应用。
- 5种数据配置的最优比例选择缺乏理论指导，当前采用均匀比例可能非最优。
- 符号替换策略要求ICL示例中至少包含两种不同答案，对单答案类型的任务不适用。
- 对于32-shot等超多示例场景，符号数量剧增可能超出模型的上下文理解能力，需要探索符号数量与ICL示例数的最优关系。
- 验证方法（去图对比）本身假设模型在训练前不利用视觉信息，但某些VQA问题本身就不需要图像即可回答。

## 相关工作与启发
- **vs General DPO**: 通用DPO不特别强调视觉信息，SymDPO通过符号替换专门强制视觉依赖。
- **vs MIA-DPO**: MIA-DPO也针对ICL但侧重于示例选择策略，仅带来+0.1~0.7提升，SymDPO从数据表示角度解决问题，提升+3.5~8.2。
- **vs Flamingo系列**: Flamingo通过大规模交错数据预训练获得ICL能力，但仍存在视觉忽视问题，SymDPO可以作为后训练补丁。
- **vs MMICL**: MMICL在多图多轮场景中也面临视觉忽视，SymDPO的符号化策略有望迁移到此场景中。
- **vs Symbol Tuning**: Symbol Tuning直接用符号替换做SFT但不构建偏好对，效果显著弱于SymDPO的DPO范式。

## 评分

### 实现细节
基于Open-Flamingo和IDEFICS模型，从87.2万数据中选1万样本训练。
学习率5e-6线性退火，8×A100 GPU训练约1小时。
使用GPT-4v增强选定样本的数据质量。
- 新颖性: ⭐⭐⭐⭐ 符号替换策略新颖且直觉清晰
- 实验充分度: ⭐⭐⭐⭐ 多模型(OF-3B/9B, IDEFICS-9B)多benchmark(5个)验证，4/8/16/32 shot全面测试
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰，方法描述详细
- 价值: ⭐⭐⭐⭐ 对提升LMM的ICL视觉理解有实用价值

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2025\] Curriculum Direct Preference Optimization for Diffusion and Consistency Models](curriculum_direct_preference_optimization_for_diffusion_and_consistency_models.md)
- [\[CVPR 2025\] Calibrated Multi-Preference Optimization for Aligning Diffusion Models](capo_multi_preference.md)
- [\[CVPR 2025\] Debiasing Multimodal Large Language Models via Noise-Aware Preference Optimization](debiasing_multimodal_large_language_models_via_noise-aware_preference_optimizati.md)
- [\[CVPR 2025\] Aesthetic Post-Training Diffusion Models from Generic Preferences with Step-by-step Preference Optimization](spo_aesthetic_post_training.md)
- [\[CVPR 2025\] InPO: Inversion Preference Optimization with Reparametrized DDIM for Efficient Diffusion Model Alignment](inpo_inversion_preference_optimization_with_reparametrized_ddim_for_efficient_di.md)

</div>

<!-- RELATED:END -->
