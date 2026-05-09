---
title: >-
  [论文解读] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?
description: >-
  [ECCV 2024][多模态][数学推理评测] 提出MathVerse——一个专门评估MLLM视觉数学推理能力的基准，通过将每道题转化为6个版本（从文本主导到纯视觉），揭示大多数MLLM严重依赖文本提示而非真正理解数学图表，并提出CoT评估策略进行细粒度推理过程评分。
tags:
  - ECCV 2024
  - 多模态
  - 多模态VLM
  - 视觉数学
  - 文本冗余
  - CoT评估
  - 多模态理解
---

# MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math?

**会议**: ECCV 2024  
**arXiv**: [2403.14624](https://arxiv.org/abs/2403.14624)  
**代码**: [https://mathverse-cuhk.github.io](https://mathverse-cuhk.github.io)  
**领域**: 多模态VLM  
**关键词**: 数学推理评测, 视觉数学, 文本冗余, CoT评估, 多模态理解

## 一句话总结

提出MathVerse——一个专门评估MLLM视觉数学推理能力的基准，通过将每道题转化为6个版本（从文本主导到纯视觉），揭示大多数MLLM严重依赖文本提示而非真正理解数学图表，并提出CoT评估策略进行细粒度推理过程评分。

## 研究背景与动机

1. **领域现状**：MLLM的数学推理能力备受关注，已有GeoQA（几何）、MathVista（广泛数学任务）和MMMU（大学级多学科）等基准进行评估。
2. **现有痛点**：(a) 现有基准的文本问题中包含大量与图表重复的描述性信息（文本冗余），MLLM可能仅靠读文本就能答题而不真正看图；(b) 仅以最终答案对错评判太粗糙，忽略了中间推理质量的差异；(c) MathVista包含大量非核心数学任务（19/28为外围任务），MMMU的大学难度可能因知识门槛限制了推理评估。
3. **核心矛盾**：评测MLLM的"视觉数学推理"能力，但问题文本本身就提供了足够信息绕过视觉理解——导致评测结果不能反映真实的多模态理解水平。
4. **本文要解决什么**：设计一个能真正检验MLLM是否读懂了数学图表的评测基准，并提供细粒度的推理过程评估。
5. **切入角度**：系统化地将问题文本中的信息按重要性分三类（描述信息、隐含属性、必要条件），逐步去除文本信息并将其视觉化到图表中。
6. **核心idea一句话**：通过创建同一道题的6个多模态信息版本并进行CoT推理评估，揭示MLLM是否真正利用了视觉信息做数学推理。

## 方法详解

### 整体框架

MathVerse包含2612道高质量视觉数学题，每道转化为6个版本（15K+ test samples），覆盖平面几何、立体几何和函数三大主题。评测由两部分组成：(1) 基于六版本对比的视觉理解评估；(2) 基于GPT-4(V)的CoT推理评估策略。

### 关键设计

**1. 问题文本的三类信息定义**
- 做什么：将问题文本按对解题的重要性分为三类
- 核心思路：
    - 描述信息(DI)：直接可从图中观察到的——基本图形组成、空间排列、标注实体
    - 隐含属性(IP)：需要更高级视觉感知的——平行垂直关系、相似全等、函数类型/周期性
    - 必要条件(EC)：特定数值/代数测量——角度值、边长、函数表达式，这些不可能从图中推导
- 设计动机：DI是明确的冗余信息，IP考验视觉理解深度，EC是解题的不可或缺条件

**2. 六个版本的问题设计**
- 做什么：专家标注员将每道题转化为6个版本
- 核心思路：
    - (1) Text-dominant：保留全部文本（DI+IP+EC+问题）
    - (2) Text-lite：去除DI → 检验MLLM能否从图中获取基本描述
    - (3) Text-only：去除图表 → 对照组，检验文本够不够解题
    - (4) Vision-intensive：去除DI和IP → 高度依赖视觉理解
    - (5) Vision-dominant：去除DI和EC、EC标注到图中 → 必须从图中识别数值
    - (6) Vision-only：纯视觉 → 极限测试
- 设计动机：渐进式信息转移，逐步迫使MLLM更多依赖视觉输入

**3. CoT评估策略**
- 做什么：用GPT-4(V)进行两阶段推理过程评估
- 核心思路：
    - Phase 1 关键步骤提取：用GPT-4（仅文本版）从MLLM输出中提取N个关键推理步骤，**故意不输入原题和答案**以避免GPT-4自身答题偏向
    - Phase 2 多步评分：用GPT-4V（多模态版）评估每个步骤的正确性（0/1），提供详细错误分析
    - 最终分数 = 0.7×(平均步骤分) + 0.3×(最终答案分)
- 设计动机：不预定义标准推理模板（因为不同题可能有不同解法，不同模型推理长度不一），自适应提取每个模型独特的推理路径

### 损失函数 / 训练策略

MathVerse是评测基准，不涉及训练。数据构建流程：
- 750题来自GeoQA + 119题GEOS + 507题Geometry3K + 370题新收集(平面几何)
- 332题立体几何 + 534题函数(新收集)
- 专家审校确保答案正确、问答一致、类别相关

## 实验关键数据

### 主实验

| 模型 | All | Text-dom | Text-lite | Text-only | Vision-int | Vision-dom | Vision-only |
|------|-----|----------|-----------|-----------|------------|------------|-------------|
| GPT-4V | 最优 | 最优 | 最优 | 高 | 最优 | 最优 | 最优 |
| Qwen-VL-Max | 中等 | 中等 | 低 | **高于Text-lite 5.1%** | 低 | 低 | 最低 |
| InternLM-XC2 | 中等 | 中等 | 低 | **高于Text-lite 5.6%** | 低 | 低 | 最低 |

### 消融实验

| 评估方式 | 说明 |
|---------|------|
| Accuracy only | 粗粒度，忽略推理质量差异 |
| CoT评估 | 细粒度，可区分推理过程质量 |
| 去冗余文本 | 大多数MLLM性能大幅下降 |
| 去图表 | 部分MLLM性能反而上升 |

### 关键发现

1. **震撼发现**：Qwen-VL-Max和InternLM-XComposer2在去掉图表后准确率反而上升5%+，说明其视觉编码能力不仅无助于数学推理，反而起到了干扰作用
2. GPT-4V和ShareGPT4V是少数能在视觉增强版本中保持或提升性能的模型，展示了相对更好的图表理解能力
3. 从Text-dom到Vision-only，所有模型性能都大幅下降，说明当前MLLM的视觉数学理解能力普遍不足
4. CoT评估揭示的中间推理质量差异被二值评估完全忽略——有些模型推理过程正确但最终答案错误
5. **视觉数学理解是当前MLLM的最大短板**，比推理能力本身更关键

## 亮点与洞察

- **六版本设计的巧妙性**：通过信息的渐进转移，精确定位MLLM在视觉理解链条中的断点
- **Text-only对照组的设计**：直接暴露了文本冗余问题——如果去掉图反而更好，说明模型根本没在看图
- **CoT评估的自适应性**：不预设标准答案步骤，适应不同模型的推理风格和长度
- **问题定义的深刻性**："MLLM是否真正看懂了图？"这个问题触及了多模态评测的根本

## 局限性 / 可改进方向

1. 六版本的标注依赖专家，成本高且难以大规模扩展
2. CoT评估依赖GPT-4V，GPT-4V本身在函数图表识别上也不够稳定
3. 仅覆盖高中数学三个主题，更多学科（如统计、概率）待扩展
4. Vision-only版本将所有信息渲染到图中可能引入排版困难和信息密度问题
5. 评估成本较高（需多次调用GPT-4/GPT-4V）

## 相关工作与启发

- **MathVista**：广泛的数学评测但包含大量外围任务，MathVerse专注于核心数学推理
- **MMMU**：大学级多学科评测，MathVerse避免了过高的知识门槛
- **GeoQA/Geometry3K**：几何专项评测，MathVerse扩展到立体几何和函数
- **启发**：评测基准的设计不仅要问"模型能不能做"，更要问"模型是不是用了正确的方式来做"——这个方法论对所有多模态评测都有指导意义

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ (六版本信息转移方案极具创意)
- **技术深度**: ⭐⭐⭐⭐ (CoT评估策略设计严谨)
- **实验充分性**: ⭐⭐⭐⭐⭐ (多模型×多版本×CoT全面评测)
- **写作质量**: ⭐⭐⭐⭐⭐ (问题定义深刻，图表说明直观)
- **影响力**: ⭐⭐⭐⭐⭐ (揭示了MLLM数学视觉理解的关键短板)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](mathverse_does_your_multi-modal_llm_truly_see_the_diagrams_in_visual_math_proble.md)
- [\[ECCV 2024\] MMBench: Is Your Multi-modal Model an All-Around Player?](mmbench_is_your_multimodal_model_an_allaround_player.md)
- [\[ECCV 2024\] m&m's: A Benchmark to Evaluate Tool-Use for Multi-step Multi-modal Tasks](m_ampmaposs_a_benchmark_to_evaluate_tool-use_for_multi-step_multi-modal_tasks.md)
- [\[ECCV 2024\] ShareGPT4V: Improving Large Multi-modal Models with Better Captions](sharegpt4v_improving_large_multimodal_models_with_better_cap.md)
- [\[ECCV 2024\] Large Motion Model for Unified Multi-Modal Motion Generation](large_motion_model_for_unified_multi-modal_motion_generation.md)

</div>

<!-- RELATED:END -->
