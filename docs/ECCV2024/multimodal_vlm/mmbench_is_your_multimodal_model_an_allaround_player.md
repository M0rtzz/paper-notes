---
title: >-
  [论文解读] MMBench: Is Your Multi-modal Model an All-Around Player?
description: >-
  [ECCV 2024][多模态][VLM评测] 提出MMBench——一个系统设计的双语多模态评测基准，包含3000+多选题覆盖20个能力维度，并引入CircularEval策略和LLM辅助选项匹配，实现对VLM的鲁棒、细粒度评估。
tags:
  - ECCV 2024
  - 多模态
  - VLM评测
  - 多选题基准
  - CircularEval
  - 多模态VLM
  - 能力维度
---

# MMBench: Is Your Multi-modal Model an All-Around Player?

**会议**: ECCV 2024  
**arXiv**: [2307.06281](https://arxiv.org/abs/2307.06281)  
**代码**: [https://github.com/open-compass/VLMEvalKit](https://github.com/open-compass/VLMEvalKit)  
**领域**: 多模态VLM  
**关键词**: VLM评测, 多选题基准, CircularEval, 双语评测, 能力维度

## 一句话总结

提出MMBench——一个系统设计的双语多模态评测基准，包含3000+多选题覆盖20个能力维度，并引入CircularEval策略和LLM辅助选项匹配，实现对VLM的鲁棒、细粒度评估。

## 研究背景与动机

1. **领域现状**：大型视觉语言模型（VLM）近年取得显著进展，GPT-4V、Gemini-Pro-V、LLaVA等展现了令人印象深刻的多模态感知与推理能力。
2. **现有痛点**：传统基准如VQAv2、COCO Caption虽然提供定量指标，但存在假阴性问题（如"bicycle"和"bike"不匹配），且缺乏细粒度能力分析；而主观评测如OwlEval依赖人工标注，不可扩展且存在显著偏差。
3. **核心矛盾**：客观评测缺乏全面性和细粒度，主观评测缺乏可复现性和可扩展性，两种方法都无法满足当前VLM评估的需求。
4. **本文要解决什么**：设计一个系统性的客观评测基准，能够对VLM进行鲁棒、全面且细粒度的评估。
5. **切入角度**：采用多选题形式统一评测框架，设计层次化能力分类体系，并引入LLM辅助选项提取和CircularEval策略解决评测鲁棒性问题。
6. **核心idea一句话**：通过精心设计的多选题基准、LLM辅助匹配和循环评估策略，实现对VLM的系统性、鲁棒性客观评测。

## 方法详解

### 整体框架

MMBench是一个系统设计的多模态客观评测基准，包含三个核心组件：(1) 层次化能力分类体系，将评测维度分为3级共20个叶子能力；(2) 精心策划的多选题数据集，覆盖多种来源和能力类型；(3) 鲁棒评测流程，结合LLM选项提取和CircularEval策略。

### 关键设计

**1. 层次化能力分类体系**
- 做什么：将VLM的能力组织为3级层次结构，L-1分为感知(Perception)和推理(Reasoning)，L-2有6个子能力，L-3有20个叶子能力
- 核心思路：参照人类认知的感知-推理二分框架，从粗到细定义评测维度
- 设计动机：细粒度分析可以精确定位VLM的强弱项，为后续优化提供方向指引

**2. 数据收集与质量控制**
- 做什么：收集3217道多选题，每道题包含图像、问题、选项和答案四元组
- 核心思路：通过志愿者从公共数据集和互联网收集，80%以上来自互联网，采用双重质量控制机制
- 设计动机：第一个机制用"多数投票"检测纯文本可解题目（若半数以上LLM仅凭文本就能答对则剔除）；第二个机制检测错误样本（若所有VLM都答错则人工审查）

**3. LLM辅助选项提取**
- 做什么：利用GPT-4将VLM的自由形式预测匹配到预定义选项
- 核心思路：先尝试启发式匹配提取选项标签，失败后调用GPT-4进行语义匹配
- 设计动机：不同VLM的指令遵循能力差异巨大（VisualGLM仅65%匹配率），GPT-4匹配与人类评估的一致率达91.5%

**4. CircularEval策略**
- 做什么：对每道题多次推理（打乱选项顺序），只有全部尝试都正确才算通过
- 核心思路：通过排列选项顺序，检验VLM是否真正理解问题而非猜测
- 设计动机：消除VLM对特定选项位置的偏好，使评测结果更鲁棒，更能体现模型间的性能差异

**5. 双语版本(MMBench-CN)**
- 做什么：将英文版本通过GPT-4翻译为中文，人工校验
- 核心思路：保留专有名词和符号不翻译，确保中英对齐
- 设计动机：支持在双语环境下对VLM进行等价比较

### 损失函数 / 训练策略

MMBench本身是评测基准而非训练方法，不涉及训练损失。评测流程分为：(1) 开发集/测试集4:6划分；(2) 测试集答案保密，需提交到评测服务器获取结果；(3) 评测代码已集成到VLMEvalKit中。

## 实验关键数据

### 主实验

| 模型 | 整体 (test) | Perception | Reasoning |
|------|------------|------------|-----------|
| GPT-4v | 77.0 | 78.5 | 73.6 |
| Gemini-Pro-V | 73.6 | - | - |
| InternLM-XComposer-VL | 74.4 | - | - |
| LLaVA-v1.5-13B | 67.7 | - | - |
| mPLUG-Owl2 | 66.0 | - | - |
| CogVLM-Chat | 65.8 | - | - |
| Qwen-VL-Chat | 61.8 | - | - |

### 消融实验

| 评估方式 | 说明 |
|---------|------|
| 启发式匹配 | 部分模型匹配率低至65%，导致评估不准确 |
| +GPT-4匹配 | 与人类评测一致率91.5%，显著提升准确性 |
| 单次评估 vs CircularEval | CircularEval更鲁棒，能更有效区分模型间差异 |

### 关键发现

1. 指令遵循能力与多模态理解能力并不相关——OpenFlamingo v2指令遵循最强但整体性能最差
2. 选项分布分析显示VLM存在位置偏好：部分模型倾向于选择特定位置的选项
3. GPT-4V在大多数能力维度上领先，但在某些细粒度能力（如空间推理）上仍有提升空间
4. 中英文版本的性能差异揭示了VLM的跨语言泛化能力差异

## 亮点与洞察

- **CircularEval设计巧妙**：通过打乱选项排列检验模型是否真正理解，而非位置猜测，这在QA评测中是重要创新
- **质量控制的双重机制**：纯文本可解检测+全错检测，确保了benchmark的有效性
- **LLM作为评测工具**：用GPT-4做选项提取，开创了用LLM辅助VLM评测的范式
- **系统性评测思维**：从数据收集、能力分类到评测策略的全链路设计，为后续评测基准提供了方法论参考

## 局限性 / 可改进方向

1. 多选题形式本身有局限，无法评估开放式生成能力
2. 依赖GPT-4进行选项匹配，引入了对商业模型的依赖
3. 能力分类体系可能不够全面，未覆盖所有视觉语言能力
4. 数据集规模虽大但仍有限，某些能力维度的样本可能不足以做出可靠结论
5. 评测成本较高（CircularEval需要多次推理），大规模评测时间开销大

## 相关工作与启发

- **MME**：较小规模的多维度VLM评测，MMBench在规模和评测策略上有显著提升
- **OwlEval/LVLM-eHub**：主观评测方法，MMBench用客观方法解决了可复现性问题
- **VLMEvalKit**：MMBench的评测代码已集成，为社区提供了标准化工具
- **启发**：高质量的评测基准对领域发展的推动力不亚于新模型——好的评测是改步

## 评分

- **新颖性**: ⭐⭐⭐⭐ (CircularEval和LLM辅助匹配是重要创新)
- **技术深度**: ⭐⭐⭐⭐ (评测方法论设计系统、严谨)
- **实验充分性**: ⭐⭐⭐⭐⭐ (21个模型的全面评测，多维度分析)
- **写作质量**: ⭐⭐⭐⭐ (结构清晰，论证充分)
- **影响力**: ⭐⭐⭐⭐⭐ (已成为VLM评测的主要基准之一)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?](mathverse_does_your_multimodal_llm_truly_see_the_diagrams_in.md)
- [\[ECCV 2024\] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)
- [\[ECCV 2024\] Large Motion Model for Unified Multi-Modal Motion Generation](large_motion_model_for_unified_multi-modal_motion_generation.md)
- [\[ECCV 2024\] m&m's: A Benchmark to Evaluate Tool-Use for Multi-step Multi-modal Tasks](m_ampmaposs_a_benchmark_to_evaluate_tool-use_for_multi-step_multi-modal_tasks.md)
- [\[ECCV 2024\] ShareGPT4V: Improving Large Multi-Modal Models with Better Captions](sharegpt4v_improving_large_multi-modal_models_with_better_captions.md)

</div>

<!-- RELATED:END -->
