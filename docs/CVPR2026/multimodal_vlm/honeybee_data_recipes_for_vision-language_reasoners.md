---
title: >-
  [论文解读] HoneyBee: Data Recipes for Vision-Language Reasoners
description: >-
  [CVPR 2026][多模态VLM][VLM reasoning] 系统研究视觉语言推理数据集的构建原则——上下文来源策略、数据干预（图像描述辅助信号+纯文本推理）、多维度数据扩展——并据此构建 250 万样本的 HoneyBee CoT 推理数据集…
tags:
  - "CVPR 2026"
  - "多模态VLM"
  - "VLM reasoning"
  - "data curation"
  - "chain-of-thought"
  - "test-time scaling"
  - "data recipes"
---

# HoneyBee: Data Recipes for Vision-Language Reasoners

**会议**: CVPR 2026  
**arXiv**: [2510.12225](https://arxiv.org/abs/2510.12225)  
**作者**: Hritik Bansal, Devendra Singh Sachan, Kai-Wei Chang, Aditya Grover, Gargi Ghosh, Wen-tau Yih, Ramakanth Pasunuru (Meta AI, UCLA)
**代码**: [facebookresearch/HoneyBee_VLM](https://github.com/facebookresearch/HoneyBee_VLM)  
**数据**: [facebook/HoneyBee](https://huggingface.co/datasets/facebook/HoneyBee)
**领域**: 多模态VLM  
**关键词**: VLM reasoning, data curation, chain-of-thought, test-time scaling, data recipes

## 一句话总结

系统研究视觉语言推理数据集的构建原则——上下文来源策略、数据干预（图像描述辅助信号+纯文本推理）、多维度数据扩展——并据此构建 250 万样本的 HoneyBee CoT 推理数据集，训练的 3B VLM 在 MathVerse 上超越 SOTA 7.8%，同时提出降低 73% 解码成本的测试时扩展策略。

## 研究背景与动机

近期 VLM 推理能力快速提升，但构建高质量视觉语言推理训练数据集的核心原则仍不清楚。现有工作主要关注模型架构和训练策略，而数据层面的系统性研究严重不足。

**现有问题**：
- **数据构建缺乏理论指导**：不同上下文来源（图像+问题的组合方式）对 VLM 推理能力的影响未被系统研究
- **数据干预效果不明**：图像描述、纯文本推理数据等辅助信号是否有效、如何整合，缺乏定量分析
- **扩展维度不清晰**：增加图像数量、每图问题数、每问 CoT 数各自的边际收益不明确
- **推理成本高昂**：长 CoT 生成带来的解码成本问题亟需解决方案

**核心目标**：通过控制变量实验，揭示 VL 推理数据构建的关键原则，并据此构建高质量大规模数据集。

## 方法详解

### 整体框架

HoneyBee 不是提一个新模型，而是系统回答"视觉语言推理的训练数据到底该怎么造"。作者用一套严格的控制变量实验，沿三条轴线拆解数据构建的影响——图像-问题对从哪来（上下文来源）、CoT 解答里加什么辅助信号（数据干预）、往哪个方向堆量（扩展维度）——再把结论落成一个大规模数据集。最终产物 HoneyBee 含 250 万条 CoT 推理样本、覆盖 35 万个唯一图像-问题对，CoT 由 Llama-4 Scout 生成，每条样本含图像、问题、以及"caption + 推理过程 + `\boxed{}` 最终答案"格式的解答；用它训练的 3B PLM 在 MathVerse 上反超同量级 SOTA 7.8%。

### 关键设计

**1. 上下文来源：图像-问题对从哪来，决定推理能学成什么样**

同样一批图像，配上不同来源的问题，训出来的推理能力差别很大。作者比较三种来源：OpenThoughts3（已有的文本推理问题集，配图扩为视觉推理 `q_source='OpenThoughts3'`）、ViRL（ViRL39K 里天然的图像-问题对 `q_source='ViRL'`）、自生成（用 ViRL 的图、由 Llama-4 Scout 生成新问题 `q_source='Ours'`）。关键发现：三种来源的混合比例显著影响最终性能，**ViRL 图像配 LLM 生成的新问题效果最佳**。

**2. 数据干预：给 CoT 装上"视觉锚点"**

长 CoT 如果一上来就纯文本推理，容易与图像脱节。HoneyBee 在 CoT 解答里引入两种辅助信号：一是**图像描述辅助**——由 Llama-4 Scout 生成描述、用 `<caption>` 和 `</caption>` 标签包裹后拼到 CoT 前部，让模型先"看懂"图再推理；二是**纯文本推理混入**——在训练数据里混不含图像的推理样本。两种干预均带来显著增益，caption 起到"视觉锚点"作用、让 CoT 更好地关联图像内容，而纯文本推理说明推理能力有一定的模态无关性、能跨模态迁移。

**3. 多维数据扩展：三个方向各自加量且能叠加**

该往哪里堆数据？作者系统探索三个扩展维度的边际收益：图像数量（唯一图多少）、每图问题数（同一图生成多少不同问题）、每问 CoT 数（同一图-问对生成多条不同推理路径）。关键发现：三个维度的扩展都持续提升推理能力、且效果可叠加，不存在明显的 diminishing returns，这指导了大规模数据集该往哪三个方向同时扩。

**4. 测试时扩展：提前终止的一致性投票，省 73% 解码**

长 CoT 生成的解码成本很高。HoneyBee 提出一种推理时策略：生成多条候选 CoT、通过一致性投票选最终答案，并加上提前终止机制——当已有足够多的候选达成一致就停止生成。这样在准确率不降的前提下减少 73% 的解码成本。

## 实验关键数据

### 评估设置
- **基座模型**：Perception-LM (PLM)，规模覆盖 1B / 3B / 8B
- **评测基准**：10 个 VL 推理数据集，包括 MathVerse、MathVista、OlympiadBench、GeoQA、MMMU 等
- **对比方法**：ViRL-tuned PLM（base）、OpenThoughts3-tuned 模型、以及同尺寸 SOTA 模型

### Table 1: 数据干预消融实验（PLM-3B，准确率 %）

| 数据配置 | MathVerse | MathVista | OlympiadBench | 平均 |
|---|---|---|---|---|
| Base (ViRL only) | 41.2 | 52.3 | 18.7 | 37.4 |
| + OT3 问题混入 | 48.6 | 56.1 | 22.4 | 42.4 |
| + Image Caption 辅助 | 54.3 | 59.8 | 25.1 | 46.4 |
| + Text-Only 推理混入 | 57.1 | 61.5 | 27.3 | 48.6 |
| + 多 CoT 扩展 | 60.8 | 63.2 | 29.6 | 51.2 |
| HoneyBee (全部策略) | **66.0** | **65.7** | **32.4** | **54.7** |

每一步干预均带来增益，全部组合后 MathVerse 提升 **24.8%**（绝对值）。

### Table 2: 与 SOTA 模型的对比（准确率 %）

| 模型 | 参数量 | MathVerse | MathVista | MMMU | GeoQA | 平均 |
|---|---|---|---|---|---|---|
| InternVL2-2B | 2B | 28.4 | 46.3 | 36.1 | 55.2 | 41.5 |
| Qwen2-VL-2B | 2B | 31.2 | 47.8 | 37.4 | 56.8 | 43.3 |
| PLM-1B (Base) | 1B | 25.7 | 42.1 | 33.2 | 50.4 | 37.9 |
| PLM-1B + HoneyBee | 1B | **45.3** | **55.6** | **41.8** | **62.1** | **51.2** |
| Qwen2-VL-7B | 7B | 52.1 | 58.4 | 46.3 | 65.7 | 55.6 |
| InternVL2-8B | 8B | 54.3 | 60.2 | 48.1 | 67.3 | 57.5 |
| PLM-3B (Base) | 3B | 41.2 | 52.3 | 39.6 | 58.3 | 47.9 |
| PLM-3B + HoneyBee | 3B | **66.0** | **65.7** | **49.2** | **71.4** | **63.1** |
| PLM-8B + HoneyBee | 8B | **72.1** | **70.3** | **54.7** | **76.2** | **68.3** |

PLM-3B + HoneyBee 在 MathVerse 上超越同参数量 SOTA **7.8%**，PLM-1B + HoneyBee 甚至超越更大的 InternVL2-2B 和 Qwen2-VL-2B。

## 亮点与洞察

- **数据工程 > 模型工程**：3B 模型通过数据策略超越 7-8B 级别的 SOTA，证明数据质量和构建策略的重要性远超参数量
- **图像描述作为"认知桥梁"**：在 CoT 前嵌入 caption 让模型先建立视觉理解再推理，这一简单干预带来持续显著增益，揭示了视觉定基 (visual grounding) 在推理中的关键作用
- **多维度扩展正交互补**：图像数、问题数、CoT 数三个维度的扩展效果可叠加，不存在明显的 diminishing returns，指导了大规模数据集的构建方向
- **测试时扩展的效率化**：提前终止的一致性投票策略在保持准确率的同时降低 73% 解码成本，具有很高的实用价值
- **纯文本推理的跨模态迁移**：混入无图像的文本推理数据能提升视觉推理性能，说明推理能力具有一定的模态无关性

## 局限性

- **数据集许可限制**：HoneyBee 使用 CC-BY-NC 和 Llama 4 License，商业使用受限；且模型命名需包含"Llama"前缀
- **依赖强 LLM 生成 CoT**：CoT 由 Llama-4 Scout 生成，质量上限受限于教师模型能力，可能继承其推理错误
- **评测覆盖偏数学**：10 个评测集以数学和科学推理为主，对常识推理、空间推理等能力覆盖不足
- **模型限定 PLM 系列**：实验主要在 Perception-LM 上验证，其他架构的适用性需进一步确认
- **扩展成本**：250 万条 CoT 的生成需要大量 Llama-4 Scout 推理算力，复现成本较高
- **未开源训练模型**：仅开源数据集和评测代码，未开源训练后的 VLM checkpoint

## 相关工作

- **VL 推理数据集**：ViRL（39K 视觉推理数据）、OpenThoughts3（文本推理数据）、ShareGPT4V（图像描述数据）→ HoneyBee 整合并扩展了这些来源，首次系统研究混合策略
- **CoT 蒸馏**：使用强模型（GPT-4、Llama-4）生成 CoT 训练弱模型，已被 NovaStar、Vision-G1 等工作采用 → HoneyBee 进一步研究 CoT 的多样性和描述辅助的效果
- **测试时扩展 (TTS)**：Best-of-N、多数投票、过程奖励模型等 → HoneyBee 提出提前终止策略降低成本
- **数据配方研究**：Scaling Data-Constrained LLMs（文本领域）、DataComp（多模态预训练）→ HoneyBee 将数据配方研究拓展到 VL 推理微调阶段

## 评分

- 新颖性: ⭐⭐⭐⭐ — 首次系统研究 VL 推理数据的构建原则，三维度分析框架清晰且实验设计严谨
- 实验充分度: ⭐⭐⭐⭐⭐ — 10 个评测集、三种模型规模、大量消融实验，控制变量设计优秀
- 写作质量: ⭐⭐⭐⭐ — 结构清晰，洞察提炼到位，32 页内容详实
- 价值: ⭐⭐⭐⭐⭐ — 数据方法论贡献突出，250 万开源数据集实用性强，对 VLM 推理研究有直接指导意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2026\] Breaking Dual Bottlenecks: Evolving Unified Multimodal Models into Self-Adaptive Interleaved Visual Reasoners](../../ICML2026/multimodal_vlm/breaking_dual_bottlenecks_evolving_unified_multimodal_models_into_self-adaptive_.md)
- [\[CVPR 2025\] Synthetic Data is an Elegant GIFT for Continual Vision-Language Models](../../CVPR2025/multimodal_vlm/synthetic_data_is_an_elegant_gift_for_continual_vision-language_models.md)
- [\[ACL 2025\] SpaRE: Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data](../../ACL2025/multimodal_vlm/spare_enhancing_spatial_reasoning_in_vision-language_models_with_synthetic_data.md)
- [\[CVPR 2025\] It's a (Blind) Match! Towards Vision-Language Correspondence without Parallel Data](../../CVPR2025/multimodal_vlm/its_a_blind_match_towards_vision-language_correspondence_without_parallel_data.md)
- [\[CVPR 2026\] CRIT: Graph-Based Automatic Data Synthesis to Enhance Cross-Modal Multi-Hop Reasoning](crit_graph-based_automatic_data_synthesis_to_enhance_cross-modal_multi-hop_reaso.md)

</div>

<!-- RELATED:END -->
