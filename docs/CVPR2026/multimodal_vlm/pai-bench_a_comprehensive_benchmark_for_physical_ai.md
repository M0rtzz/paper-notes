---
title: >-
  [论文解读] PAI-Bench: A Comprehensive Benchmark for Physical AI
description: >-
  [CVPR 2026][多模态VLM][Physical AI] PAI-Bench 把「物理 AI 所需的预测与感知能力」拆成视频生成、条件视频生成、视频理解三条赛道，用 2808 个真实世界样本和任务对齐的指标系统评测 15 个视频生成模型与 16 个多模态大模型，结论是：当前视频生成模型画面逼真但守不住物理规律，MLLM 的物理理解远落后于人类。
tags:
  - "CVPR 2026"
  - "多模态VLM"
  - "Physical AI"
  - "视频生成评测"
  - "视频理解"
  - "世界模型"
  - "可控生成"
---

# PAI-Bench: A Comprehensive Benchmark for Physical AI

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_PAI-Bench_A_Comprehensive_Benchmark_For_Physical_AI_CVPR_2026_paper.html)  
**代码**: https://github.com/SHI-Labs/physical-ai-bench  
**领域**: 多模态VLM  
**关键词**: Physical AI、视频生成评测、视频理解、世界模型、可控生成

## 一句话总结
PAI-Bench 把「物理 AI 所需的预测与感知能力」拆成视频生成、条件视频生成、视频理解三条赛道，用 2808 个真实世界样本和任务对齐的指标系统评测 15 个视频生成模型与 16 个多模态大模型，结论是：当前视频生成模型画面逼真但守不住物理规律，MLLM 的物理理解远落后于人类。

## 研究背景与动机
**领域现状**：「物理 AI」（Physical AI）希望模型能感知真实世界、预测真实世界的动态演化，进而支撑机器人、自动驾驶等具身应用。这套能力可拆成两半：**感知**（理解视频里正在发生什么物理事件）主要靠多模态大模型（MLLM），**预测**（forecast 下一帧/下一步会怎样）主要靠视频生成模型（VGM）——后者被隐式训练去「预测未来帧」，因此被寄望为学习物理规律的世界模型。

**现有痛点**：两侧的评测都没踩到「物理 AI」这个点上。MLLM 的主流 benchmark 评的是 OCR、数学题、日常感知这类偏抽象/通用的能力，它们在专门的物理场景里到底行不行无人系统衡量过；VGM 的主流 benchmark（VBench、EvalCrafter 等）评的是美学质量和时序一致性，几乎不查「生成的视频符不符合物理常识」。更糟的是这些 benchmark 高度割裂——要么只测预测、要么只测感知，且没有任何 benchmark 系统评测「条件可控生成」对控制信号的忠实度。

**核心矛盾**：物理 AI 需要预测+感知一体化地落到真实物理场景上，而现有评测既不统一、又不物理、还不真实（很多用合成/玩具场景）。视觉保真度高 ≠ 物理可信度高，这两件事被现有指标混为一谈。

**本文目标**：建一个统一、真实、物理对齐的 benchmark，一次覆盖视频生成、条件视频生成、视频理解，并为每条赛道配上能反映「物理合理性」而非单纯画质的指标。

**切入角度**：所有评测都锚定在「真实采集的视频 + 物理上有意义的任务」上（如行车记录仪、机器人操作、第一视角），覆盖自动驾驶、机器人、工业、人类活动、物理常识等子域；并把「画质」与「物理合理性」拆成两个独立分数分别打。

**核心 idea**：用三轨（生成 / 条件生成 / 理解）+ 双分数（Quality Score 管画质、Domain Score 管物理合理性）的设计，把物理 AI 的预测与感知能力放在同一把尺子下系统体检。

## 方法详解
PAI-Bench 不是一个模型，而是一套评测协议 + 数据集。它把物理 AI 的能力检验拆成三条互补赛道，统一遵循「真实视频 + 物理任务」的构建原则，总计 2808 个高质量样本。下面分别讲清每条赛道测什么、数据怎么造、用什么指标打分。

### 整体框架
三条赛道各对应物理 AI 的一个能力维度：

- **PAI-Bench-G（视频生成）**：测「预测」。给文本/首帧让 VGM 生成视频，既看画质（Quality Score）又看物理合理性（Domain Score）。
- **PAI-Bench-C（条件视频生成）**：进一步测「预测」中的可控性。给定模糊/边缘/深度/分割等控制信号，看条件 VGM 生成的视频是否忠实于控制信号、画质如何、在相同条件下能否产出多样结果。
- **PAI-Bench-U（视频理解）**：测「感知」。给真实视频 + 选择题，看 MLLM 能否做物理常识推理与具身推理。

三轨的样本全部来自真实世界采集（公开数据集 + 网络），并横跨自动驾驶、机器人、工业、人类、物理常识、第一视角等子域。整套评测的价值落点是一张「现状地图」：把 15 个 VGM、4 个条件 VGM（5 种控制配置）、16 个 MLLM 放进来体检，量出当前系统离真正的物理 AI 还差多远。

> 这是一篇 benchmark 论文，没有可训练的 pipeline——核心在「赛道怎么设计、数据怎么造、指标怎么定」，因此不画框架图，下面用关键设计逐条讲清。

### 关键设计

**1. 三轨统一设计：把预测与感知一次性收进同一把尺子**

物理 AI 真正需要的是「看懂当下 + 预测未来」一体化的能力，但旧 benchmark 要么只评 VGM 的画质、要么只评 MLLM 的问答，互不通气。PAI-Bench 用 G/C/U 三轨把它们焊在一起：G 与 C 都落在「预测」（VGM 作为世界模型 forecast 未来帧），U 落在「感知」（MLLM 理解视频里的物理事件）。三轨共享同一套构建原则——视频必须是真实采集（如行车记录仪），任务必须物理上有意义，子域必须覆盖具身/自驾/工业/第一视角等实际应用。如表 1 所示，相比 EvalCrafter、VBench、EgoSchema、VideoMME 等只覆盖单一能力或单一子域的 benchmark，PAI-Bench 是首个在「视频生成 + 条件生成 + 视频理解 + 全部物理子域」八个维度上全部打勾的工作，2808 个样本也兼顾了规模与质量。

**2. Quality Score 与 Domain Score 双分数：把「画得像」和「合物理」拆开打**

VGM 评测最大的陷阱是「画面逼真」被当成「物理正确」。PAI-Bench-G 把这两件事拆成两个独立分数。**Quality Score** 沿用 VBench/VBench++ 的 8 个指标（主体一致性 SC、背景一致性 BC、运动平滑 MS、美学质量 AQ、成像质量 IQ、整体一致性 OC、I2V 主体 IS、I2V 背景 IB），衡量画质与文本对齐。**Domain Score** 才是物理合理性的核心：先对真实视频用 Qwen2.5-VL-72B 做高保真字幕 + 人工校正，再基于物理本体论生成 QA 对（5636 条、覆盖 6 个子域），然后让 Qwen3-VL-235B-A22B 作为 judge，拿这些 QA 去「考」生成出来的视频，Domain Score 就是 judge 在这套 QA 上的回答准确率——它量的是「生成视频有没有遵守这些被 QA 编码进去的物理与语义约束」。这种 MLLM-as-judge + 任务对齐 QA 的设计，让物理合理性变成可量化、可对比的标量，而不是靠人主观感受。论文还用 arena 人类两两对比 + ELO 验证了指标与人类偏好的一致性，整体 Pearson 相关系数 $r=0.918$。

**3. 条件赛道 PAI-Bench-C：首个系统评测「控制信号忠实度」的设置**

随着 VGM 越来越多地用深度图、边缘、分割等多模态信号做引导生成，「生成结果到底听不听控制信号的话」成了实用关键，却没有任何 benchmark 系统测过。PAI-Bench-C 定义了理想可控生成的三条标准并各配指标：**忠实度**用一套投影-比对的保真指标——把生成视频投回对应模态空间（用 Blur Kernel / Canny / Video-Depth-Anything / GroundingDINO+SAM2 提取），再和 ground-truth 控制信号比相似度，得到 Blur SSIM↑、Edge F1↑、Depth si-RMSE↓、Mask mIoU↑；**画质**用 DOVER；**多样性**用 LPIPS。数据上从 AgiBot（机器人）、OpenDV（自驾）、Ego-Exo-4D（第一视角）各采 200 段共 600 视频，并为每段视频生成 1 条原始 caption + 5 条「换掉主导物体、场景连贯但内容新颖」的 caption，专门支撑多样性评测。

**4. PAI-Bench-U 双能力本体 + 去偏设计：让「看视频答题」真考物理理解**

视频理解 benchmark 的老毛病是「不看视频也能答」——模型靠语言先验或单帧静态偏置就能猜对。PAI-Bench-U 从两头治这个病。**能力本体**上，它把物理理解拆成两类：① 物理常识推理（Space 管空间关系/交互、Time 管时序与因果、Physical World 管物体状态与违反物理的情形），共 604 QA / 426 视频；② 具身推理（Predicting Action Effects——任务完成判定 + 下一步动作预测；Adherence to Physical Constraints——动作可行性 affordance），共 610 QA / 601 视频，源自 RoboVQA、RoboFail、BridgeData、AgiBot、HoloAssist 及自有 AV 数据。**去偏**上，论文用「改变输入帧数」做诊断（图 7）：0 帧（纯文本）时模型掉到随机猜水平，证明题目无法靠语言先验答对；1 帧 vs 32 帧之间有显著差距，证明题目必须依赖时序上下文、单帧静态信息不够。这两条共同保证 U 赛道的分数确实来自视觉+时序理解。

### 数据集构建
三轨数据均采「MLLM 初标 + 人工精修」两阶段：G 轨用 Qwen2.5-VL-72B 生成字幕与候选 QA、再人工校正，得 1044 个视频-prompt 对 + 5636 QA（6 子域）；C 轨从三个真实数据集各采 200 段、用 modality-specific 模型抽控制信号、并改写出新颖 caption；U 轨先收 1000+ 视频标 5737 题、严格复审后精炼到 604 高质量 QA，具身部分再标 610 QA。总计 2808 个评测样本。

## 实验关键数据

### 主实验
**PAI-Bench-G（15 个 VGM，越高越好；Quality 满分参照真实源视频 78.0，Domain 源视频 89.8）**：

| 模型 | Overall | Domain Score | Quality Score |
|------|---------|--------------|---------------|
| Source Videos（真实） | 83.9 | 89.8 | 78.0 |
| Veo3（闭源） | 82.2 | 86.8 | 77.6 |
| Wan2.2-I2V-A14B（开源最佳） | 82.3 | 87.1 | 77.5 |
| Cosmos-Predict2.5-2B | 81.4 | 84.9 | 78.0 |
| DynamiCrafter（弱基线） | 68.3 | 63.0 | 73.7 |

关键反差：多数领先 VGM 的 Quality Score 已逼近甚至追平真实源视频（~78），但 Domain Score 全部低于真实视频的 89.8——画面够逼真，物理合理性却普遍掉队。

**PAI-Bench-U（16 个 MLLM，越高越好）**：

| 模型 | Overall | Common Sense Avg. | Embodied Avg. |
|------|---------|-------------------|---------------|
| Human | 93.2 | 93.6 | 95.5 |
| Qwen3-VL-235B-A22B（最佳） | 64.7 | 64.9 | 64.4 |
| GPT-5 | 61.8 | 63.9 | 59.7 |
| Qwen2.5-VL-72B | 60.8 | 58.6 | 63.0 |
| Random Guess | 37.0 | 38.9 | 35.2 |

所有模型（最高 64.7）距人类 93.2 都有近 30 个点的鸿沟；且闭源不必然领先——开源的 Qwen3-VL-235B 反超 GPT-5。

### 消融/分析实验
**PAI-Bench-C：控制信号配置对比（Cosmos-Transfer2.5-2B 为例）**

| 控制信号 | Edge F1 ↑ | Mask mIoU ↑ | Quality ↑ | Diversity ↑ |
|----------|-----------|-------------|-----------|-------------|
| Blur 单信号 | 0.26 | 0.75 | 8.77 | 0.18 |
| Edge 单信号 | 0.39 | 0.74 | 8.05 | 0.36 |
| Seg 单信号 | 0.13 | 0.71 | 7.87 | 0.44 |
| All（多信号融合） | 0.45 | 0.77 | 9.24 | 0.13 |

**U 轨去偏诊断（不同输入帧数，准确率 %）**

| 配置 | Qwen3-VL-8B | GPT-5 | 说明 |
|------|-------------|-------|------|
| #frames=0（纯文本） | 39.3 | 37.3 | 掉到随机猜水平 → 无语言先验泄漏 |
| #frames=1 | 43.3 | 52.1 | 单帧不够 |
| #frames=32 | 47.9 | 68.2 | 必须依赖时序上下文 |

### 关键发现
- **画质 ≠ 物理**：VGM 的 Quality Score 已追平真实视频，但 Domain Score 全员落后于真实视频 89.8，说明「守物理规律」才是世界模型当前的硬瓶颈。
- **多信号优于单信号**：C 轨里 All 条件画质最高（Quality 9.24），实用启示是与其喂一段模糊/带噪的视频，不如先抽出互补控制信号再融合重建出高质量视频。
- **分割信号反而最不忠实**：用 Seg 当控制信号时 Mask mIoU 最低，作者归因于 SAM2 等分割模型产出的 mask 时序一致性差（偶发漏掉物体），监督信号本身最噪。
- **指标与人对齐**：Quality/Domain 分数与人类 ELO 偏好的整体 Pearson 相关达 0.918，佐证双分数设计有效。
- **MLLM 物理理解远未及格**：最强模型仅 64.7 vs 人类 93.2，且物理 AI 显然还没成为主流 MLLM 的数据/优化重点（闭源不占优）。

## 亮点与洞察
- **「双分数」是这篇最值得借鉴的设计**：把容易被刷高的画质指标与真正难的物理合理性指标解耦，避免「画得越漂亮分越高」的虚假繁荣——任何生成式评测都可以借这个思路把「表观质量」与「任务正确性」分开打。
- **Domain Score = 任务对齐 QA + MLLM-as-judge**：把「物理合理性」这种难以直接量化的东西，转译成「judge 在一组预先编码了物理约束的 QA 上的准确率」，既可量化又可解释，复用性强。
- **用帧数消融做去偏诊断很巧**：0 帧→随机、1 帧 vs 32 帧拉开差距，两条曲线同时证明「答案来自视觉 + 时序」，这是验证视频 benchmark 是否「真考视频」的好范式，可直接迁移到其他视频理解 benchmark 的质检。
- **投影-比对式忠实度指标**：把生成视频投回控制信号所在模态空间再比相似度，给「可控生成听不听话」提供了一套可操作的量化协议。

## 局限与展望
- 作者把全文定位为「现状体检」，并未提出改进生成/理解模型的方法——benchmark 揭示了差距但不负责弥合。
- Domain Score 依赖 MLLM judge（Qwen3-VL-235B），judge 自身的物理理解上限会传导为评测上限；当被评 MLLM 与 judge 同源时还可能存在偏好耦合 ⚠️（论文用人类 ELO 对齐做了部分缓解）。
- C 轨的忠实度指标依赖深度/分割/边缘提取器（Video-Depth-Anything、SAM2、Canny 等），这些提取器本身的误差会混入分数——「分割信号最不忠实」的结论一定程度上也受 SAM2 时序抖动影响，是评测工具而非纯模型能力的反映。
- U 轨为去偏统一用选择题，便于自动判分但限制了开放式生成/解释能力的评测；2808 样本相对真实物理世界的长尾仍偏小，部分子域（如工业）样本量明显少于自驾/机器人。
- 可改进方向：把双分数推广到「物理一致性的时序定位」（哪一帧开始违反物理）、引入与被评模型异源的 judge、补充开放式因果解释题。

## 相关工作与启发
- **vs VBench / EvalCrafter**：它们只评 VGM 的画质与时序一致性，PAI-Bench 在沿用其 8 个画质指标的同时，额外引入 Domain Score 专测物理合理性，并把评测扩到条件生成与理解两条赛道。
- **vs PhyGenBench / IntPhys2**：同样关注物理合理性，但前者只覆盖生成、样本规模小（160 / 1070），PAI-Bench 用 2808 真实样本同时覆盖生成+条件生成+理解与全部物理子域。
- **vs EgoSchema / VideoMME / CausalVQA**：这些是纯视频理解 benchmark，缺物理接地与去偏诊断；PAI-Bench-U 用物理本体论组织题目并用帧数消融证明「真考视觉+时序」。
- **启发**：当一个领域同时有「生成侧」和「理解侧」两类模型时，把它们放进同一套真实数据 + 任务对齐指标下统一体检，比各自为政的 benchmark 更能暴露系统性差距；「双分数解耦表观质量与任务正确性」是可复用的评测设计范式。

## 评分
- 新颖性: ⭐⭐⭐⭐ 首个统一覆盖视频生成/条件生成/理解的物理 AI benchmark，双分数与条件忠实度评测是实打实的新设置。
- 实验充分度: ⭐⭐⭐⭐⭐ 评了 15 VGM + 4 条件 VGM×5 配置 + 16 MLLM，并有人类 ELO 对齐、帧数去偏诊断等多角度分析。
- 写作质量: ⭐⭐⭐⭐ 三轨结构清晰、指标定义明确，图表充分；个别指标计算细节放到补充材料略影响自洽。
- 价值: ⭐⭐⭐⭐⭐ 给物理 AI 的预测与感知能力提供了统一可比的尺子，明确指出「画质达标但物理不达标、MLLM 远逊人类」两大缺口，对世界模型与具身方向有直接指导价值。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] PhyCritic: Multimodal Critic Models for Physical AI](phycritic_multimodal_critic_models_for_physical_ai.md)
- [\[CVPR 2026\] QUANTIPHY: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models](quantiphy_a_quantitative_benchmark_evaluating_physical_reasoning_abilities_of_vi.md)
- [\[CVPR 2026\] IPR-1: Interactive Physical Reasoner](ipr-1_interactive_physical_reasoner.md)
- [\[CVPR 2026\] LifeEval: A Multimodal Benchmark for Assistive AI in Egocentric Daily Life Tasks](lifeeval_a_multimodal_benchmark_for_assistive_ai_in_egocentric_daily_life_tasks.md)
- [\[AAAI 2026\] VP-Bench: A Comprehensive Benchmark for Visual Prompting in Multimodal Large Language Models](../../AAAI2026/multimodal_vlm/vp-bench_a_comprehensive_benchmark_for_visual_prompting_in_m.md)

</div>

<!-- RELATED:END -->
