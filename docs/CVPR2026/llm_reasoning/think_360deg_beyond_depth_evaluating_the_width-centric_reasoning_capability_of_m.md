---
title: >-
  [论文解读] Think 360°: Beyond Depth — Evaluating the Width-centric Reasoning Capability of MLLMs
description: >-
  [CVPR 2026][LLM推理][多模态推理] 作者提出 Think360°，一个把"推理宽度"（广度搜索、多约束剪枝、回溯）作为与"推理深度"（长链顺序推理）正交维度的多模态基准——精选 1200+ 道跨域高质量题目，并设计一套 Tree-of-Thought 评测协议同时量化宽度与深度准确率，对 12 大系列 30+ MLLM 的测评显示：当前模型能做长链深推、却普遍不擅长"宽搜索 + 深链"结合的洞察式推理。
tags:
  - "CVPR 2026"
  - "LLM推理"
  - "多模态推理"
  - "推理宽度"
  - "Tree-of-Thought 评测"
  - "MLLM benchmark"
  - "宽度 vs 深度"
---

# Think 360°: Beyond Depth — Evaluating the Width-centric Reasoning Capability of MLLMs

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Think_360deg_Beyond_Depth_Evaluating_the_Width-centric_Reasoning_Capability_of_CVPR_2026_paper.html)  
**代码**: 待确认（论文称将开源于 "Think360"）  
**领域**: LLM推理 / 多模态评测基准  
**关键词**: 多模态推理、推理宽度、Tree-of-Thought 评测、MLLM benchmark、宽度 vs 深度

## 一句话总结
作者提出 Think360°，一个把"推理宽度"（广度搜索、多约束剪枝、回溯）作为与"推理深度"（长链顺序推理）正交维度的多模态基准——精选 1200+ 道跨域高质量题目，并设计一套 Tree-of-Thought 评测协议同时量化宽度与深度准确率，对 12 大系列 30+ MLLM 的测评显示：当前模型能做长链深推、却普遍不擅长"宽搜索 + 深链"结合的洞察式推理。

## 研究背景与动机

**领域现状**：当下衡量推理强弱的"金标准"几乎都押在 chain-of-thought 的长度上——无论是 test-time scaling、SFT 还是 RL 对齐，主流叙事都是"推得越长越强"。多模态数学/逻辑基准（MathVision、MathVerse、MathVista、OlympiadBench 等）也沿着难度（K12→研究生→奥赛）、任务覆盖、模态三个轴不断加码。

**现有痛点**：这些基准共享一个隐藏的单一轴——它们几乎只考察**推理深度**（一条链能延伸多远），偏向"单调推理"：结论随前提逐步扩展，主要挑战是"找到相关知识"。但人类解题很少靠线性演绎一条道走到黑，而是在解空间里 360° 多向探索：从思维锚点向不同方向分叉、剪掉死路、绕回来重访其他假设、把零碎线索重组，直到顿悟。

**核心矛盾**：把"推理能力"等同于"链长"，实际上把两个正交维度混为一谈——**深度**（无矛盾地跟随一条长序列推理链）和**宽度**（系统地在多个相互竞争的假设间分支、回溯、选择性剪枝后收敛）。只测深度会高估那些"会算但不会试错"的模型。

**本文目标**：构造一个显式聚焦推理宽度、同时仍能量化深度的多模态基准，并回答：模型能否 ❶ 系统地试错探索解空间、❷ 同时处理多个约束高效剪枝不可行分支、❸ 把零散线索统一成连贯答案——且全程要在语言和视觉上联合推理。

**切入角度**：作者从神经网络的"深 vs 宽"做类比——深度=层叠的顺序特征抽象，宽度=并行通路捕捉多样表示；并把 shortcut/dropout、金字塔特征、反向传播分别类比为推理中的剪枝、分治、回溯。沿这个类比，宽度推理对应 trial-and-error 的广度优先搜索。

**核心 idea**：用"宽度（trial-and-error / 多约束剪枝 / 回溯）"这一被忽视的维度补全推理评测，并用 Tree-of-Thought 把模型回答拆成树，分别在"同层兄弟节点"上算宽度、在"最长路径"上算深度。

## 方法详解

### 整体框架
Think360° 不是一个新模型，而是"一套数据 + 一套评测协议"。整条工作分两块：(1) **基准构建**——从竞赛/教材/已有 benchmark/在线益智游戏四类来源收集 1200+ 道题，经"粗筛 + 人工精筛"两级质量过滤，再针对证明题和游戏题做重写标注，使答案可客观验证；(2) **评测协议**——除常规 pass@1 外，提出 Tree-of-Thought 评测（ToT-Eval）：用 GPT-4o 把模型的完整回答抽成层次树，逐节点判对错后，分别按"同层兄弟节点平均组准确率"算宽度分、按"最长路径准确率"算深度分；同时记录推理时间与 token 消耗以分析效果-效率权衡。最终对 12 大系列、30+ MLLM 跨难度档/题型/能力做全面测评。这是纯 benchmark/评测协议工作，方法侧没有可画 pipeline 的可训练模块，故不配框架图。

### 关键设计

**1. 把"推理宽度"形式化为与深度正交的评测维度**

痛点在于：现有基准把推理能力坍缩成"链长"，无法暴露模型"只会顺推、不会横向试错"的短板。作者明确给出两个正交定义——**深度**：无矛盾地跟随一条长序列推理链的能力；**宽度**：在收敛前系统地通过分支（branching）、回溯（backtracking）、选择性剪枝（pruning）来穿越多个相互竞争假设的能力。三种宽度子模式（试错探索、多约束并行剪枝、零散线索归并）被进一步对应到认知技能：Branch-and-Bound、Hypothesize-and-Test、Divide-and-Conquer、Trial-and-Error、Perceive-and-Comprehend。这套定义让"宽度"从一个含糊直觉变成可统计、可按题型归类的量化对象——Tab.2 显示，已有基准里"宽度型题"占比普遍 <12%（MathVision ~11.5%、MathVista ~2.7%、MathVerse ~1.3%），而 Think360° 做到 ~100%、且唯一带宽度 taxonomy。

**2. 三阶段基准构建管线：让"难且可验证"的宽度题成规模**

宽度型好题天然稀缺且难标注：竞赛/教材题多是证明题、常缺高质量配图；在线益智游戏题没有预设问题和答案。作者用三阶段管线把它们"驯化"成可客观评测的条目。① **种子收集**：四类来源（数学/逻辑竞赛如 ARML、HMMT；教材例习题；已有 benchmark；在线益智/IQ 游戏），各有特性需差异化处理。② **粗到细质量过滤**：粗筛用静态关键词匹配（如 "maximum/minimum"、"possible ways"，作者发现这类词与 LRM 的 "Aha moment" 相关）+ GPT-4o 做 LLM-as-Judge 按所需认知能力打分；细筛靠人工 double-check 保证质量与多样性并标记需重绘的图。③ **标注与重写**：对证明题（来源❶❷），从原证明过程中抽取易验证的数值关系/特定结论，重新设计成保持答案可靠又能客观判分的题；对游戏题（来源❹），用初始游戏截图当图像条件、枚举每格可能状态作为候选答案、设计指向特定位置的问题（如"A 格是黑还是白"）。这套流程把"难验证的开放题"系统转成"可自动判分的题"，是宽度基准能规模化的前提。

**3. Tree-of-Thought 双维评测协议（ToT-Eval）：同一棵树上分别量宽度与深度**

只看最终答案的 outcome-based 匹配分（GPT-4o-mini 先抽答案，再"正则匹配优先、失配才上 LLM-as-judge"两段式打二元分）无法区分"宽推 vs 深推"。ToT-Eval 分两步：① **树构建**——给定题目和模型完整回答，用 GPT-4o 逐字抽取关键推理步并组织成层次树，其中父子关系表示顺序推理依赖（深度）、同层兄弟节点表示对替代方案的并行探索（宽度）。② **深度/宽度打分**——再用 GPT-4o 判每个节点是否逻辑自洽、事实正确、且正确扎根于父节点与题面；判完所有节点后，**宽度分 = 各组（同层兄弟）平均组准确率**（Avg. Group Acc.），**深度分 = 平均最长路径准确率**（Avg. Longest Path Acc.）。这样同一棵思维树既能反映"模型敢不敢、会不会铺开多条路并剪枝"（宽），又能反映"单条链能不能稳稳推到底"（深），把过去混在一起的两件事拆开度量。

### 一个例子：俄罗斯方块式三联骨牌题
以一道"8 格宽屏、用直线三联骨牌(triomino)能否在角落留下恰好一个方块"的题为例：模型回答被 ToT-Eval 抽成树——根下先分出"屏宽分析/单格策略/奇偶性考量/可能网格尺寸"等**兄弟节点**（这一层的覆盖广度=宽度信号），其中"可能网格尺寸"又向下展开 3/6/9 格的子推理（父子链=深度信号），最终汇到结论节点 "Answer: yes"。逐节点判分后，同层兄弟的平均正确率给出宽度分、根到结论的最长正确路径给出深度分。这个例子直观说明：一个答案对的模型，可能宽度分高（探索全面）但深度分被某条错链拖低，反之亦然。

## 实验关键数据

### 基准统计与对比

| 维度 | Think360° |
|------|-----------|
| 总题量 | 1225（testmini 740, 60%）|
| 答案类型 | 自由作答 83.1%（数值 54.3% / 结构 37.0% / 公式 5.2%）、选择题 16.9% |
| 难度档 | Easy 10.4% / Basic 22.2% / Medium 33.6% / Hard 23.9% / Olympiad 9.9%（近似钟形）|
| 认知技能 / 题型 | 5 类认知技能、6 类题型（均为非互斥多标签）|

| 基准 | 宽度型题占比 | 带宽度 taxonomy | 难度层级 |
|------|-------------|-----------------|----------|
| MathVista | ~2.7% | ✗ | K-12 |
| MathVerse | ~1.3% | ✗ | K-12 |
| MathVision | ~11.5% | ✗ | K-12/大学 |
| OlympiadBench | ~1.7% | ✗ | 竞赛 |
| **Think360°（本文）** | **~100%** | **✓** | K-12/大学/竞赛 |

> 指标说明：**pass@1** = 单次作答的 outcome 匹配准确率；**ToT 宽度准确率** = 同层兄弟节点的平均组准确率；**ToT 深度准确率** = 平均最长正确路径准确率；同时记录推理时间(s)与 token 消耗用于效果-效率权衡分析。

### 主测评（pass@1 ALL，节选）

| 模型 | 类型 | ALL Acc./% | 备注 |
|------|------|-----------|------|
| Gemini-2.5-pro | 闭源 | 46.0 | 全场最高 |
| o3 | 闭源 | 42.3 | 闭源第二梯队 |
| o4-mini | 闭源 | 42.1 | — |
| Gemini-2.5-flash-thinking | 闭源 | 38.3 | — |
| o1 | 闭源 | 36.8 | — |
| Claude-3.7-Sonnet-Thinking | 闭源 | 35.5 | — |
| GPT-4o | 闭源 | 16.0 | 非思考型明显偏低 |
| GLM-4.1V-Thinking | 开源 9B | 22.6 | 开源最佳 |
| Kimi-VL-Instruct | 开源 16A3B | 10.1 | — |
| LLaVA-OneVision | 开源 7B | 8.3 | — |
| Llama-3.2-Vision-Instruct | 开源 11B | 7.1 | 垫底 |

### 关键发现
- **天花板很低**：即便最强的 Gemini-2.5-pro 也只有 46.0%、o3 42.3%，说明宽度推理对当前 MLLM 是真短板，远未饱和。
- **思考型 >> 非思考型**：o 系列、Gemini-thinking、Claude-thinking 显著高于 GPT-4o/Gemini-flash 等非思考变体；Doubao-thinking(34.7) 对比其 nothinking(32.8) 也印证 test-time 推理有用，但代价是 token 与时间剧增（o3 单题 ~6300 token、~261s）。
- **Branch-and-Bound 最难**：在五类认知技能分列中，Branch-and-Bound（需要系统枚举+剪枝）几乎所有模型得分最低（如 GPT-4o 仅 9.9%），最能暴露"宽搜索 + 多约束剪枝"的缺失。
- **开源-闭源鸿沟大**：开源最佳 GLM-4.1V(22.6) 不及多数闭源思考型一半；小模型在宽度题上几近随机水平。
- **深链 ≠ 会宽搜**：作者强调当前模型能在常识/通用 VQA 上表现强，但难以把"深序列思维链"与"宽探索搜索"结合做真正的洞察式推理——这是 benchmark 想敲打的核心结论。

## 亮点与洞察
- **维度补全的视角很"啊哈"**：把"推理强=链长"这一隐含假设显式拆成深/宽两个正交轴，并用神经网络的深宽类比串起来（shortcut↔剪枝、反传↔回溯、金字塔↔分治），让一个直觉变成可测量的评测维度。
- **ToT-Eval 是可复用的评测 trick**：把"看最终答案对错"升级为"把回答抽成思维树、同层算宽度、最长路算深度"，这套协议不依赖特定数据，可迁移去诊断任何长 CoT 模型"到底是宽不够还是深不够"。
- **数据驯化方法可借鉴**：把"难验证的证明题/无答案的游戏题"通过"抽可验证数值关系 / 截图当图 + 枚举状态作候选"转成可自动判分题，是把宽度型难题规模化的实用工程经验。
- **关键词×Aha moment 的观察**：用 "maximum/minimum、possible ways" 这类词做粗筛、并与 LRM 的 Aha moment 关联，给"如何高效挖掘宽度型题"提供了一个低成本启发式。

## 局限与展望
- **重度依赖 LLM-as-Judge**：树构建、节点判分、答案抽取全用 GPT-4o / GPT-4o-mini，评测稳定性与公平性受裁判模型能力与偏置影响（尤其判被测的同源闭源模型时）。⚠️ 树的抽取/判分提示词细节以原文附录为准。
- **跨模型横向比有 caveat**：思考型模型 token/时间预算远高于非思考型，ALL 准确率直接比大小并不完全对等，需结合效果-效率曲线看。
- **宽度/深度分的绝对值依赖树结构**：同一回答抽成的树形状会影响宽/深分，协议对抽树一致性较敏感。
- **可改进方向**：把 ToT-Eval 用作训练信号（如对宽度分做 RL 奖励）、扩充非数学/逻辑域的宽度题、引入多裁判投票降低单裁判偏置。

## 相关工作与启发
- **vs MathVision / MathVerse / MathVista**：它们做更全面的多模态数学评测，但偏单调推理（结论随前提扩展、主挑战是找知识），宽度型题占比极低且无宽度 taxonomy；本文专门从"宽度"切入，宽度题占比 ~100%。
- **vs CLEVR / GQA**：早期组合视觉推理基准聚焦组合性视觉推理，缺多模态数学能力评测；本文覆盖 K12-大学-竞赛全谱且强调试错/回溯。
- **vs 仅看 pass@1 的评测**：本文用 ToT-Eval 把"答案对错"细化为宽/深双维过程分，能区分"答对但靠运气/单链"与"系统宽搜后收敛"，诊断粒度更细。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 把被忽视的"推理宽度"显式形式化并配套 ToT 双维评测，视角新且填补空白。
- 实验充分度: ⭐⭐⭐⭐⭐ 12 系列 30+ 模型、跨难度/题型/认知技能全面测评，并给出效果-效率分析与错误案例。
- 写作质量: ⭐⭐⭐⭐ 类比与定义清晰，但部分构建/评测细节散落附录、正文符号略密。
- 价值: ⭐⭐⭐⭐ 给"长 CoT 是否等于强推理"提供了可量化的反例与诊断工具，对推理评测社区有参考价值。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[NeurIPS 2025\] VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning](../../NeurIPS2025/llm_reasoning/videorft_incentivizing_video_reasoning_capability_in_mllms_via_reinforced_fine-t.md)
- [\[AAAI 2026\] Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented LLM Reasoning](../../AAAI2026/llm_reasoning/beyond_react_a_planner-centric_framework_for_complex_tool-au.md)
- [\[CVPR 2026\] Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization](revisiting_the_necessity_of_lengthy_chain-of-thought_in_vision-centric_reasoning.md)
- [\[CVPR 2026\] Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models](think-as-you-see_streaming_chain-of-thought_reasoning_for_large_vision-language_.md)
- [\[CVPR 2026\] Improving Vision-language Models with Perception-centric Process Reward Models](improving_vision-language_models_with_perception-centric_process_reward_models.md)

</div>

<!-- RELATED:END -->
