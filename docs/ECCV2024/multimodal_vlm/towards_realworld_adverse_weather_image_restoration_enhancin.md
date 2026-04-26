---
title: >-
  [论文解读] Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models
description: >-
  [ECCV 2024][多模态][恶劣天气图像复原] 提出WResVLM半监督框架，利用VLM评估图像清晰度和提供语义信息，通过伪标签选择+天气prompt学习增强清晰度、VLM描述引导的语义正则化增强语义，首次有效地将合成数据训练的复原模型泛化到真实恶劣天气场景。
tags:
  - ECCV 2024
  - 多模态
  - 恶劣天气图像复原
  - 半监督学习
  - 视觉-语言模型
  - 去雨/去雾/去雪
  - 伪标签
---

# Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models

**会议**: ECCV 2024  
**arXiv**: [2409.02101](https://arxiv.org/abs/2409.02101)  
**代码**: 有（GitHub）  
**领域**: 多模态VLM  
**关键词**: 恶劣天气图像复原, 半监督学习, 视觉-语言模型, 去雨/去雾/去雪, 伪标签

## 一句话总结
提出WResVLM半监督框架，利用VLM评估图像清晰度和提供语义信息，通过伪标签选择+天气prompt学习增强清晰度、VLM描述引导的语义正则化增强语义，首次有效地将合成数据训练的复原模型泛化到真实恶劣天气场景。

## 研究背景与动机
1. **领域现状**：恶劣天气图像复原（去雨/去雾/去雪）在合成数据上取得了长足进步，All-in-One方法（TransWeather、WeatherDiff等）用单模型处理多种天气。但这些方法在真实场景中效果有限。
2. **现有痛点**：(1) 合成与真实数据的域差距导致泛化能力弱——合成雨/雾/雪难以模拟真实世界的复杂性；(2) 现有方法只关注视觉清晰度，忽略了语义上下文的恢复，对下游高层任务帮助有限；(3) 真实恶劣天气图像没有配对的干净ground truth，无法直接用于监督训练。
3. **核心矛盾**：要在真实数据上训练复原模型，需要某种形式的监督信号。VLM经过大规模训练见过大量天气场景，具备评估天气相关图像质量的能力，可以作为"裁判官"提供监督。
4. **本文要解决什么？** (1) 利用VLM评估图像清晰度来指导真实数据上的伪标签选择；(2) 利用VLM生成的描述来增强复原图像的语义质量；(3) 设计有效的训练策略实现迭代提升。
5. **切入角度**：VLM同时具备两种能力——(a) 低层次的天气场景感知能力（判断图像是否清晰）；(b) 高层次的语义理解能力（描述场景内容和天气状况）。利用这两种能力分别增强clearness和semantics。
6. **核心idea一句话**：用VLM作为"裁判"选伪标签和"导师"提供语义描述，在无配对GT的真实天气图像上训练复原模型。

## 方法详解

### 整体框架
半监督学习框架：有标签的合成数据提供 $\mathcal{L}_{sup}$，无标签的真实数据通过VLM辅助提供4种无监督损失——伪标签损失 $\mathcal{L}_{ps}$、天气prompt学习损失 $\mathcal{L}_{wpl}$、语义正则化损失 $\mathcal{L}_{sem}$、特征相似性损失 $\mathcal{L}_{feat}$。总损失 $\mathcal{L} = \mathcal{L}_{sup} + w_1\mathcal{L}_{ps} + w_2\mathcal{L}_{wpl} + w_3\mathcal{L}_{sem} + w_4\mathcal{L}_{feat}$。

### 关键设计

1. **VLM-based图像评估与伪标签选择**：
    - 做什么：用VLM对复原图像的天气相关质量打分，选择最佳复原结果作为伪标签
    - 核心思路：设计天气相关的质量问询模板给VLM，将VLM在五个评分词（excellent/good/fair/poor/bad）上的logit通过softmax转为数值评分 $r^{vlm} = \sum_{i=1}^5 i \times p_i$
    - 设计动机：传统IQA（NIMA、MUSIQ）只评估一般技术质量（噪声、模糊），不能区分天气退化。VLM训练中见过大量天气场景，能更好判断"可见度"

2. **天气Prompt学习（Weather Prompt Learning）**：
    - 做什么：学习CLIP中的天气概念embedding，引导复原模型生成"看起来晴天"的图像
    - 核心思路：(1) 学习4个天气prompt embedding $t_c, t_r, t_h, t_s$（clear/rain/haze/snow），固定CLIP参数，用分类loss在真实天气图像上学习；(2) 复原时最大化预测图像与clear prompt的CLIP相似度 $\mathcal{L}_{wpl} = \frac{e^{cos(\mathcal{E}_I(\hat{y}), \mathcal{E}_T(t_c))}}{\sum_t e^{cos(\mathcal{E}_I(\hat{y}), \mathcal{E}_T(t))}}$
    - 设计动机：手写prompt（"rainy"）不够鲁棒，学习得到的prompt embedding能更精准区分天气类型，作为可微分的优化目标引导复原

3. **描述辅助的语义增强（Description-assisted Semantic Enhancement）**：
    - 做什么：利用VLM为每张图生成天气描述，通过修改天气词保留语义词来提供正/负文本对，引导复原保持语义
    - 核心思路：(1) LLaVA生成负描述 $d_{neg}$（含天气信息）如"A person walking in heavy rain..."；(2) LLaMA转换为正描述 $d_{pos}$（去除天气、保留语义）如"The weather looks good. A person walking..."；(3) 语义损失最大化复原图与 $d_{pos}$ 的CLIP相似度 $\mathcal{L}_{sem}$
    - 设计动机：weather prompt是通用的天气概念，description是image-specific的语义约束。两者互补——prompt保证"像晴天"，description保证"保留场景语义"

4. **训练策略（伪标签初始化 + 迭代更新）**：
    - 做什么：用多个现有复原方法的结果初始化伪标签数据库，多轮迭代训练
    - 核心思路：初始化时使用多个VLM专家投票选最佳复原结果；训练分4轮，每轮1个VLM做在线评估，轮间用全套VLM做全局评估更新
    - 设计动机：单一VLM可能有偏好偏差，多VLM集成更稳健；迭代更新让伪标签和prompt逐步改善

### 损失函数 / 训练策略
权重 $w_1=0.5, w_2=0.2, w_3=0.05, w_4=0.2$。使用MSBDN作为backbone。每轮40k迭代，4轮共160k迭代。伪标签用mean-teacher在线更新。

## 实验关键数据

### 主实验

| 方法 | Rain MUSIQ↑ | Haze MUSIQ↑ | Snow MUSIQ↑ | Overall MUSIQ↑ |
|------|------------|------------|------------|---------------|
| Restormer | 54.69 | 53.27 | 61.18 | 56.38 |
| TransWeather | 51.06 | 46.27 | 59.38 | 52.24 |
| PromptIR | 53.48 | 53.88 | 60.86 | 56.07 |
| DA-CLIP | 52.98 | 53.23 | 60.57 | 55.59 |
| **Ours** | **59.80** | **56.09** | **62.12** | **59.34** |

### 消融实验

| 配置 | MUSIQ↑ | CLIP-IQA↑ | VLM-Vis↑ |
|------|--------|-----------|----------|
| $\mathcal{L}_{sup}$ only | 53.41 | 0.388 | 0.343 |
| + $\mathcal{L}_{ps}$ | 54.08 | 0.396 | 0.354 |
| + VLM评估 $r^{vlm}$ | 56.68 | 0.429 | 0.366 |
| + 伪标签初始化 | 57.34 | 0.425 | 0.370 |
| + $\mathcal{L}_{wpl}$ | 58.13 | 0.437 | 0.376 |
| + $\mathcal{L}_{sem}$ | 58.91 | 0.445 | 0.381 |
| + 迭代更新 | **59.34** | **0.456** | **0.387** |

### 关键发现
- VLM-based评估选择的伪标签比传统IQA（NIMA、MUSIQ）选择的质量更高，训练效果更好
- 天气prompt学习和语义增强各自独立贡献显著（+0.79和+0.78 MUSIQ），且互补
- 用户研究中本方法在visibility和quality两个维度均领先
- 语义正则可以帮助VLM检测到微妙的天气残留（如"foggy"或"overcast"），进一步改善伪标签和训练
- 即使用较简单的MSBDN backbone，通过VLM辅助的半监督学习也远超在合成数据上训练的Restormer等强基线

## 亮点与洞察
- **VLM作为"天气裁判"的角色极为自然**：VLM在海量天气图像上训练，天然具备判断"图像是否清晰"的能力。将这种能力转化为可微分的训练信号是巧妙的工程设计。
- **描述的正负转换是一个精妙的技术**：同一场景的负描述（有天气词）和正描述（无天气词、保留语义），为复原模型提供了"保持什么、去除什么"的精确指导。
- **迭代自增强的训练策略**：初始伪标签→训练复原模型→更好的伪标签→更好的模型，形成正反馈循环。多VLM集成避免了单一偏差。

## 局限性 / 可改进方向
- 大型VLM的使用增加了计算开销，限制了实际部署速度
- 伪标签quality的上限受限于初始复原方法的结果
- 仅验证了MSBDN一种backbone，更强的backbone（如Restormer、NAFNet）可能获得更大提升
- 对混合天气条件（同时有雨和雾）的处理能力待验证

## 相关工作与启发
- **vs TransWeather/WeatherDiff**：这些方法在合成数据上训练，在真实数据上泛化差。本方法通过半监督学习直接在真实数据上训练。
- **vs DA-CLIP**：DA-CLIP也用CLIP但仅做退化信息学习，未利用VLM评估和语义增强。本方法更全面利用VLM能力。
- **vs PromptIR**：PromptIR用prompt预测退化类型，但仍在合成数据上训练。本方法的weather prompt学习直接在真实数据上做CLIP空间的优化。

## 评分
- 新颖性: ⭐⭐⭐⭐ VLM辅助的半监督天气复原框架是新颖的范式
- 实验充分度: ⭐⭐⭐⭐ 三种天气、多种指标、用户研究、详细消融
- 写作质量: ⭐⭐⭐⭐ 框架清晰，组件动机合理
- 价值: ⭐⭐⭐⭐ 首次有效解决了天气复原的真实场景泛化问题

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_vision-language_models_for_city-wide_image_address_locali.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)
- [\[ECCV 2024\] Attention Prompting on Image for Large Vision-Language Models](attention_prompting_on_image_for_large_vision-language_models.md)
- [\[ECCV 2024\] FlexAttention for Efficient High-Resolution Vision-Language Models](flexattention_for_efficient_highresolution_visionlanguage_mo.md)
- [\[ECCV 2024\] CAT: Enhancing Multimodal Large Language Model to Answer Questions in Dynamic Audio-Visual Scenarios](cat_enhancing_multimodal_large_language_model_to_answer_questions_in_dynamic_aud.md)

<!-- RELATED:END -->
