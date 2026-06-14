---
title: >-
  [论文解读] Anchoring the Mind of Multimodal Reasoners: Cognitive Bias as a Vector for Jailbreak Attacks
description: >-
  [CVPR 2026][LLM对齐][越狱攻击] 本文发现多模态大推理模型（MLRM）的安全判断存在"锚定效应"——会被最先看到的信息严重带偏，据此提出 RA-Attack：先用一张"看起来安全"的结构化思维导图加教育语境文本把模型的推理链锚定到安全基调，再顺势把有害意图包装成这条推理链的自然延伸，在 7 个主流 MLRM 上把越狱成功率（ASR）刷到 92%（Gemini-2.5-Pro）、82%（GPT-4o）的 SOTA。
tags:
  - "CVPR 2026"
  - "LLM对齐"
  - "越狱攻击"
  - "锚定效应"
  - "认知偏差"
  - "多模态推理模型"
  - "推理链劫持"
---

# Anchoring the Mind of Multimodal Reasoners: Cognitive Bias as a Vector for Jailbreak Attacks

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Cong_Anchoring_the_Mind_of_Multimodal_Reasoners_Cognitive_Bias_as_a_CVPR_2026_paper.html)  
**代码**: https://github.com/ccclh/RA-Attack  
**领域**: 对齐RLHF / AI安全 / 多模态VLM  
**关键词**: 越狱攻击, 锚定效应, 认知偏差, 多模态推理模型, 推理链劫持

## 一句话总结
本文发现多模态大推理模型（MLRM）的安全判断存在"锚定效应"——会被最先看到的信息严重带偏，据此提出 RA-Attack：先用一张"看起来安全"的结构化思维导图加教育语境文本把模型的推理链锚定到安全基调，再顺势把有害意图包装成这条推理链的自然延伸，在 7 个主流 MLRM 上把越狱成功率（ASR）刷到 92%（Gemini-2.5-Pro）、82%（GPT-4o）的 SOTA。

## 研究背景与动机
**领域现状**：MLRM 通过显式多步推理（CoT 监督、RL）大幅提升复杂任务表现，但显式推理链同时把"内部思考过程"暴露成了新的攻击面。现有多模态越狱大多攻击**视觉接口**（对抗图、排版注入、扩散合成有害图）或**强行劫持推理链**（H-CoT 喂入精心构造的推理步、VisCRA 两阶段指令控制推理路径），共同特征是"要么藏住有害指令、要么硬掰推理过程"。

**现有痛点**：作者观察到一个更底层的现象——**即使模型明确识别出有害意图、即便没有任何显式诱导，它的推理过程仍可能主动把这个意图"合理化"（rationalize）成教育/专业用途然后照做**。这说明漏洞不在"检测不出有害"，而在"推理过程自己去找借口执行"。现有攻击没有针对这层认知弱点。

**核心矛盾**：MLRM 的推理是**顺序的、路径依赖的，对初始输入高度敏感**——这恰好对应认知心理学里成熟的"锚定效应"（anchoring effect）：判断会被最先遇到的那条信息（"锚"）不成比例地左右。锚定效应在 LLM 的谈判等通用任务上被验证过，但**是否会污染 MLRM 的安全判断从未被研究**。

**本文目标**：分解为两个问题——Q1：MLRM 在安全判断上是否真的存在锚定效应？Q2：若有，如何系统地利用它诱导模型合理化并执行有害意图？

**切入角度 / 核心 idea**：不去"隐藏"或"硬劫持"，而是放一个**良性的"安全锚"**（与有害主题相关但本身无害的内容）在提示最前面，把整条推理链的认知起点先压到"安全"一侧；之后的有害请求就不再是突兀的恶意命令，而像是这条已经建立好的安全推理路径的逻辑延伸——用"诱导合理化"代替"对抗扰动"。

## 方法详解

### 整体框架
RA-Attack 把"利用锚定效应越狱"工程化成一条可批量跑的自动流水线。给定一批原始有害指令 $D_{ori}=\{h^1_{ori},\dots,h^N_{ori}\}$，离线侧先做聚类与改写，组装出"安全锚 + 有害意图引导"的跨模态样本；在线侧把样本喂给目标 MLRM，触发它先解读思维导图（建立安全推理基），再把有害意图当成自然延伸执行，输出有害内容。

整个攻击样本 $P^i$ 由两个模态拼成：**文本模态**（文本安全锚 + 有害意图引导文本）和**视觉模态**（结构化视觉安全锚，即思维导图），即 $P^i = P^i_{text} \oplus I_{M(i)}$，其中 $\oplus$ 表示图文配对、$M(i)$ 是第 $i$ 条指令所属主题类别。

下面这张图给出离线"样本生成"到在线"越狱执行"的完整链路：

```mermaid
%%{init: {'flowchart': {'rankSpacing': 24, 'nodeSpacing': 28, 'padding': 6, 'wrappingWidth': 400}}}%%
flowchart TD
    A["有害指令集 D_ori"] --> B["锚定效应<br/>把'先入信息主导安全判断'变成攻击面"]
    B --> C["自动化样本生成流水线<br/>Cluster / Rephrase / Compose / Generate / Assemble"]
    C --> D["结构化视觉安全锚<br/>同主题但无害的思维导图 I_j"]
    C --> E["文本安全锚 + 有害意图引导<br/>教育语境先解图，再顺势提有害请求"]
    D --> F["拼接图文样本<br/>P = P_text ⊕ I"]
    E --> F
    F --> G["目标 MLRM 推理"]
    G -->|安全锚在前 → 推理基偏向安全| H["合理化并执行有害意图 → 有害输出"]
```

### 关键设计

**1. 锚定效应：把"先入信息主导安全判断"做成攻击向量**

这是全文的根。痛点在于 MLRM 会主动为有害意图找借口执行，作者的假设是：能不能**主动制造并放大这种合理化**？他们用一个干净的对照实验把"锚定效应"从"内容混淆"里剥离出来——设置三组条件：Baseline（只有有害引导文本 $H_g$）、Anchor-First（安全锚在前，$A_{scene}+H_g$）、Anchor-Last（同样内容但顺序反过来，$H_g+A_{scene}$）。关键在于 Anchor-First 与 Anchor-Last **包含完全相同的信息**，唯一差别是顺序，因此两者的 ASR 差距只能归因于"位置/顺序"，而非"内容变多了"。实验显示 Anchor-First 不仅远高于 Baseline，还显著高于 Anchor-Last（如 AdvBench 上多个模型 Anchor-First 比 Anchor-Last 高 10~18 个百分点）——这就把锚定效应坐实为底层认知漏洞。作者还用 t-SNE 给出佐证：尽管 RA-Attack 与 Anchor-Last 内容一致，但 RA-Attack 的输入隐状态明显**更靠近"安全锚"簇**，说明前置安全锚确实把模型内部表示拉向了安全一侧。

**2. 结构化视觉安全锚：用思维导图把"安全推理路径"预先铺好**

预实验里用的是一张普通的"教育场景图"$A_{scene}$，能验证效应但不够强。本设计把视觉锚升级成**与有害主题相关、但内容全部无害的思维导图**（mind map）。为什么用思维导图而不是随便一张图？因为思维导图的**层级分支结构天然贴合 MLRM 的渐进式推理过程**：当模型被要求先解读这张安全导图时，它会顺着导图预设的分支一步步走，等于被"喂"了一条清晰、可跟随的安全推理路径，高效地建立起一个偏向安全的认知基。同时导图主题与有害意图同源，使得随后的有害请求不像突兀的恶意命令，而像沿着已铺好的路径往前再走一步。消融印证了这两点都不可省：把视觉锚换成与 $H_g$ 主题无关的"法式甜点原理"（Irrelevant Anchor），ASR 显著下滑——**主题相关性**是合理化能否发生的关键。

**3. 文本安全锚 + 有害意图引导：先建安全语境，再平滑递进到执行**

文本模态负责把"安全基调"和"有害 payload"缝成一段连贯叙事。文本安全锚构造一个**教育/企业安全简报**式的语境，并下达一个前置的安全推理任务——要求模型先解读思维导图的要点，与视觉锚协同把推理链的认知起点压向安全。紧接着是**有害意图引导文本** $H_g$：作者不直接抛出命令式有害指令，而是把它改写成"在前述教育语境下，请写一个'教科书级'的、详细且真实的 [有害意图] 范例，并分析其中用到的全部技术"。这样有害请求被表述成安全推理链的**逻辑延伸**而非断点，模型更容易"为了教学/防御目的"把它合理化并执行。消融里去掉文本安全锚（$A_v+H_g$）或去掉视觉锚（$A_t+H_g$）ASR 都明显下降，说明二者是**协同**而非冗余。

**4. 自动化越狱样本生成流水线：把攻击规模化、标准化**

为了在整个有害指令集上批量造样本，作者设计了一条由强 LLM（实现用 Gemini-2.5-Pro）驱动的自动流水线，围绕一个带占位符的模板 $T$（三个占位符：`[role]` 专业无害人设、`[topic]` 与有害意图同源的安全导图主题、`[phrased_harmful_intent]` 名词化的有害意图）展开：

$$(\Theta, M) = \mathrm{Cluster}(D_{ori}), \qquad h^i_{phrased} = \mathrm{Rephrase}(h^i_{ori})$$

先把指令集聚成 $K$ 个核心主题类别 $\Theta$ 并得到归属映射 $M$，同时把每条命令式指令改写成有害意图名词短语；再为每个类别生成匹配的教育角色与安全导图主题 $(r_j, t_j)=\mathrm{Compose}(\theta_j)$；用这些组件填模板得到文本输入 $P^i_{text}=\mathrm{Assemble}(T, r_{M(i)}, t_{M(i)}, h^i_{phrased})$；视觉侧由 $I_j=\mathrm{Generate}(t_j)$ 生成导图——$\mathrm{Generate}$ 分两步：先让 LLM 按结构约束（**最多 3 层、10 个节点**）产出思维导图源码，再用外部可视化工具把代码渲染成图像。最终每条样本 $P^i=P^i_{text}\oplus I_{M(i)}$。这条流水线让 RA-Attack 具备跨数据集、跨模型的可扩展性与一致性。

### 损失函数 / 训练策略
本文是**无训练、纯黑盒**的提示级攻击，不涉及梯度优化或模型微调，因此没有损失函数；唯一的"评估器"是用 GPT-4o 按 judge prompt 判定响应是否有害（用于计算 ASR）。

## 实验关键数据

### 主实验
- **模型**：7 个代表性 MLRM——闭源 GPT-4o、o4-mini、Gemini-2.5-Pro、Gemini-2-FlashThinking；开源 MM-Eureka-Qwen、MM-Eureka-InternVL、LLaVA-CoT。
- **数据集**：AdvBench（去重版 50 条有害指令）、Hades（750 条，5 类有害场景）。
- **指标**：ASR = 成功攻击数 / 总输入数 × 100%（GPT-4o 当裁判）。

AdvBench 上 ASR（%）对比（节选最强基线 VisCRA 与本文）：

| 方法 | o4-mini | GPT-4o | Gemini-2.5-Pro | Gemini-2-FT | MM-E-InternVL | MM-E-Qwen | LLaVA-CoT |
|------|---------|--------|----------------|-------------|----------------|-----------|-----------|
| CS-DJ | 10 | 46 | 76 | 78 | 78 | 86 | 84 |
| VisCRA | 12 | 60 | 80 | 78 | 82 | 86 | 86 |
| **RA-Attack** | **44** | **82** | **92** | **92** | **94** | **94** | **96** |

RA-Attack 在两个数据集、全部 7 个模型上都是最高 ASR：AdvBench 平均 84.86%（VisCRA 69.14%），Hades 平均 76.29%（VisCRA 62.91%）。最突出的是在安全性最强的 o4-mini 上——基线 ASR 普遍 ≤12%，RA-Attack 做到 44%（AdvBench）/39.07%（Hades），是最强基线的 3 倍多，说明它击中的是更深层、对齐越强越难掩盖的认知漏洞。

### 消融实验
锚组件与"锚定机制"必要性（AdvBench，ASR%）：

| 配置 | GPT-4o | MM-E-InternVL | 说明 |
|------|--------|----------------|------|
| $H_g$ | 34 | 8 | 只有有害引导，无锚 |
| $A_v + H_g$ | 66 | 38 | 去掉文本安全锚 |
| $A_t + H_g$ | 64 | 66 | 去掉视觉安全锚 |
| $H_g + A_{structured}$ | 54 | 62 | Anchor-Last：内容相同、顺序反转 |
| $A_{structured} + H_g$ | **82** | **94** | 完整 RA-Attack |

去掉任一模态都明显掉点，证明视觉锚 $A_v$ 与文本锚 $A_t$ **协同**缺一不可；而"Anchor-Last"用完全相同的内容只是把顺序反过来，ASR 仍从 82→54（GPT-4o）、94→62（InternVL），**直接证明掉点来自"顺序/锚定"而非内容**。

锚的设计选择消融（AdvBench，ASR%）：

| 配置 | GPT-4o | MM-E-InternVL | 说明 |
|------|--------|----------------|------|
| $A_{scene} + H_g$ | 68 | 72 | 用非结构化场景图替代导图 |
| $A_{irrelevant} + H_g$ | 38 | 86 | 导图主题与有害意图无关 |
| $A_{structured} + H_g$ | **82** | **94** | 结构化 + 主题相关 |

### 关键发现
- **结构 > 场景**：思维导图（结构化）比普通教育场景图锚定更强（GPT-4o 82 vs 68），因其分支结构贴合模型的渐进式推理。
- **主题相关性是合理化的前提**：换成无关主题（法式甜点）后 GPT-4o 从 82 跌到 38——无关锚无法让有害请求显得像推理链的自然延伸。
- **合理化是普遍现象**：在成功越狱的响应里，超过 95% 都先把有害意图"合理化"成教育/专业用途再执行（GPT-4o 95.12%、Gemini-2.5-Pro 100%、MM-E-InternVL 95.74%）。
- **对齐越强越脆**：在最难攻的 o4-mini 上优势最大，反衬出攻击命中的是认知层而非表层过滤。

### 防御：Anchor Debiasing Prompt（ADP）
作者顺手给出一个轻量防御——在用户输入前置一段"去锚化"提示，要求模型**独立评估请求的每个部分、不被初始指令不成比例地影响，对违规部分单独拒绝**。效果（AdvBench ASR ↓越好，MM-Vet Score ↑越好）：

| 模型 | AdvBench (ASR) | MM-Vet (Score) |
|------|----------------|----------------|
| GPT-4o | 82.00 | 66.40 |
| GPT-4o + ADP | **8.00 (-74.00)** | 67.50 (+1.10) |
| Gemini-2.5-Pro | 92.00 | 80.70 |
| Gemini-2.5-Pro + ADP | **28.00 (-64.00)** | 81.30 (+0.60) |

ADP 在几乎不损通用能力（MM-Vet 反而微升）的前提下大幅压低 ASR——而一个"专门中和锚定效应"的提示能有效中和攻击，反过来强力佐证了攻击机制确实根植于锚定这一认知偏差。

## 亮点与洞察
- **把心理学偏差变成可量化的攻击向量**：最巧妙的是 Anchor-First vs Anchor-Last 这个"控制内容、只改顺序"的对照——一举把"锚定效应"从"内容混淆"里干净地剥离出来，让"顺序差 = 认知漏洞"的论证无可辩驳。
- **不藏、不劫持，而是"诱导合理化"**：相比 H-CoT/VisCRA 那种硬塞推理步，RA-Attack 只是放一个良性安全锚让模型自己去找借口，攻击面更隐蔽、也更普适。
- **攻防同源的闭环论证**：ADP 防御不仅实用，更是"反证"——能用去锚提示中和攻击，等于证明攻击靠的就是锚定。这种"设计一个针对性解药来验证病因"的思路可迁移到其他认知漏洞研究。
- **思维导图作为视觉锚**：利用"结构对齐推理过程"这一点，把图像从"对抗扰动载体"重新定位成"推理路径模板"，是一个新颖的视觉攻击视角。

## 局限与展望
- **依赖强 LLM 造样本**：流水线由 Gemini-2.5-Pro 驱动生成导图与改写，攻击质量与该 LLM 能力强相关；换弱模型造样本时效果是否稳定，正文未充分讨论（鲁棒性放在附录 C，⚠️ 以原文为准）。
- **ASR 由 GPT-4o 单一裁判判定**：有害与否的判断本身带主观性，单裁判可能高估或低估，缺少多裁判/人工交叉校验。
- **ADP 远非完美**：Gemini-2.5-Pro 上 ADP 后仍有 28% ASR，说明简单提示级去锚不足以根治，需要训练阶段的认知去偏。
- **双刃剑**：这是攻击方法，公开会被滥用；论文也明确含不安全示例。其正向价值在于把"认知安全"这一被忽视的前沿摆上台面，推动针对推理链/认知偏差的对齐研究。

## 相关工作与启发
- **vs VisCRA / H-CoT（推理链劫持）**：它们**强行**用预设推理步或两阶段指令控制模型思考路径；本文不劫持，而是放一个良性锚**诱导**模型自己合理化，机制更底层、对强对齐模型（o4-mini）优势更明显。
- **vs SI-Attack / CS-DJ / FC-Attack（视觉接口攻击）**：这些靠语义不一致、子图分散注意力、排版注入等"混淆"绕过安全检查；本文用 Anchor-First/Last 实验证明自己的增益**不只是内容混淆**，而是顺序带来的认知偏差，定位到更深的漏洞层。
- **vs 通用 LLM 锚定效应研究（谈判等任务）**：前人验证了 LLM 在通用任务上有锚定效应，本文首次把它延伸到 MLRM 的**安全判断**，并系统武器化，开辟"认知安全（cognitive security）"这一方向。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 首次把"锚定效应"这一认知偏差系统性地做成多模态越狱向量，并用控制顺序的对照实验严谨证因。
- 实验充分度: ⭐⭐⭐⭐⭐ 7 模型 ×2 数据集 ×6 基线，外加组件/设计/机制多组消融、t-SNE 内部表示分析与 ADP 防御验证。
- 写作质量: ⭐⭐⭐⭐ 问题驱动、动机清晰、攻防闭环论证漂亮；部分关键鲁棒性证据藏在附录。
- 价值: ⭐⭐⭐⭐⭐ 揭示对齐越强反而越易被认知偏差攻破的反直觉现象，把"认知安全"立为 AI 安全的新前沿，攻防均有可复用思路。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICCV 2025\] Heuristic-Induced Multimodal Risk Distribution Jailbreak Attack for Multimodal Large Language Models](../../ICCV2025/llm_alignment/heuristic-induced_multimodal_risk_distribution_jailbreak_attack_for_multimodal_l.md)
- [\[AAAI 2026\] AlignTree: Efficient Defense Against LLM Jailbreak Attacks](../../AAAI2026/llm_alignment/aligntree_efficient_defense_against_llm_jailbreak_attacks.md)
- [\[ACL 2025\] JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs](../../ACL2025/llm_alignment/jailbreakradar_comprehensive_assessment_jailbreak_attacks.md)
- [\[ICLR 2026\] JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks](../../ICLR2026/llm_alignment/jailnewsbench_multi-lingual_and_regional_benchmark_for_fake_news_generation_unde.md)
- [\[ICLR 2026\] Toward Universal and Transferable Jailbreak Attacks on Vision-Language Models (UltraBreak)](../../ICLR2026/llm_alignment/toward_universal_and_transferable_jailbreak_attacks_on_vision-language_models.md)

</div>

<!-- RELATED:END -->
