---
title: >-
  [论文解读] PAS: Prelim Attention Score for Detecting Object Hallucinations in Large Vision-Language Models
description: >-
  [CVPR 2026][幻觉检测][物体幻觉检测] 本文发现 LVLM 产生物体幻觉时往往"无视图像、转而依赖自己已经生成的前文 token（prelim）"，据此提出免训练、无需额外前向的 Prelim Attention Score（PAS）——直接把对 prelim token 的注意力权重求和当作幻觉分数，在多模型多数据集上取得 SOTA 的物体幻觉检测效果。
tags:
  - "CVPR 2026"
  - "幻觉检测"
  - "物体幻觉检测"
  - "LVLM"
  - "注意力"
  - "互信息"
  - "免训练"
---

# PAS: Prelim Attention Score for Detecting Object Hallucinations in Large Vision-Language Models

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Hoang_PAS_Prelim_Attention_Score_for_Detecting_Object_Hallucinations_in_Large_CVPR_2026_paper.html)  
**代码**: https://github.com/lanl/pas  
**领域**: 多模态VLM  
**关键词**: 物体幻觉检测, LVLM, 注意力, 互信息, 免训练

## 一句话总结
本文发现 LVLM 产生物体幻觉时往往"无视图像、转而依赖自己已经生成的前文 token（prelim）"，据此提出免训练、无需额外前向的 Prelim Attention Score（PAS）——直接把对 prelim token 的注意力权重求和当作幻觉分数，在多模型多数据集上取得 SOTA 的物体幻觉检测效果。

## 研究背景与动机
**领域现状**：大视觉-语言模型（LVLM）在描述图像时常出现"物体幻觉"——说出图里根本不存在的物体。要在没有标注、没有外部裁判模型的现实场景里实时拦截这种错误，主流做法是**免训练、免参考**的内省式检测：只用模型自己的输入/输出和内部状态（logits、隐状态、注意力）算一个分数，再用阈值 $\tau$ 判幻觉。

**现有痛点**：这些方法几乎都把注意力聚焦在"信息量最大"的 image token 上——logits 类方法用得最少（性能最差）；表示类方法（IC、GLSim）用 Logit Lens 把图像隐状态映射到词表去查"图-物兼容性"；注意力类方法（如 SVAR）用图像注意力比例。它们共同**忽略了一个低信息量的来源：已经生成的前缀输出 token（作者称之为 prelim）**，因为直觉上 prelim 信息少、又是模型自己生成的不可靠内容，看起来不值得用。

**核心矛盾**：作者反过来想——正因为 prelim 不可靠，**如果模型在生成一个物体时高度依赖 prelim 而非图像，这本身就是"不可信"的信号**。自注意力的 softmax 约束使 $s_{\text{BOS}}+s_{\text{img}}+s_{\text{ins}}+s_{\text{prel}}=1$，"图像注意力低"只是症状，"prelim 注意力高"才是模型切换到不可靠生成模式的更直接证据。

**本文目标**：(1) 用信息论形式化"prelim 依赖 ↔ 幻觉"这一假设并验证；(2) 设计一个高效到可在推理时实时计算的检测分数。

**切入角度**：观察到幻觉 token 的 prelim 注意力显著高于真实 token（Fig. 3a），且这种相关性与"图像注意力"恰好相反——高 prelim 注意力 → 更可能幻觉。

**核心 idea**：用"对 prelim token 的注意力权重之和"直接当幻觉分数，替代昂贵的互信息估计。

## 方法详解

### 整体框架
本文把物体幻觉检测拆成"投资—假设/验证—检测"三步。先把 LVLM 的自回归生成形式化：在位置 $k$ 生成物体 token $y_k$ 时，它的概率依赖输入 $x=(v,t)$（图像 token $v$、指令 token $t$）和前文 $y_{<k}$（即 prelim）。作者提出假设 H1：**若 $y_k$ 的生成高度依赖 prelim 而非图像，则很可能是幻觉**。这一假设有两条落地路径：一条是**理论严格但昂贵**的互信息检测器 $D_{\text{MI}}$，需要边缘化图像、对每个输入多跑 $L$ 次前向；另一条是**高效实用**的注意力分数 PAS，只用推理时本就算好的注意力权重、零额外前向。两条路径都能得到有效检测器，从而互相印证 H1，而 PAS 因为又快又准成为最终方法。

### 关键设计

**1. Prelim 过度依赖假设与互信息检测器（H1）：把"无视图像"翻译成可度量的量**

针对"图像注意力低只是症状、抓不到根因"的痛点，作者用条件互信息把 H1 写成可计算的判据。设 $Y_k$ 是位置 $k$ 待预测 token 的随机变量，若它在给定 prelim 与指令后**不再依赖图像 $v$**，则 $y_k$ 很可能是幻觉。于是定义检测器

$$D_{\text{MI}}(y_k,y,x) = -I(v;Y_k\mid y_{<k},t),\qquad I(v;Y_k\mid y_{<k},t)=H(Y_k\mid y_{<k},t)-H(Y_k\mid y_{<k},x).$$

难点在于 $\Pr(Y_k\mid y_{<k},t)$（"只给 prelim、不给图像时的预测"）在 LVLM 里拿不到，作者用对一组参考图像 $\mathcal I$ 求平均来近似边缘化：$\Pr(y\mid y_{<k},t)=\mathbb E_{I\sim\mathcal I}[\Pr(y\mid y_{<k},(I,t))]$。$\mathcal I$ 按数据集每个物体类各采一张含该类的图，使 $|\mathcal I|=$ 类别数。这一支证明了 H1 在理论上成立，但每个输入要多跑 $|\mathcal I|+1$ 倍前向，不实用——它的价值是**为 PAS 提供理论背书**。

**2. Prelim Attention Score（PAS）：把注意力权重直接当幻觉分数**

由于 $D_{\text{MI}}$ 的边缘化估计既慢又有噪声，作者改用注意力机制做等价但廉价的度量。在解码器自注意力里，token 间唯一的信息交换路径就是注意力，因此"对某类 token 的注意力权重之和"恰好量化了该类对当前 token 生成的影响。令 $s_{\text{prel}}$ 为 prelim token 到 $y_k$ 的注意力权重和，PAS 直接定义为

$$D_{\text{PAS}}(y_k,y,x)=s_{\text{prel}}(y_k,y,x)=\frac{1}{H}\sum_{h=1}^{H}\sum_{j=m+1}^{k-1}A^{(l,h)}(k,j),$$

其中 $A^{(l,h)}(k,j)$ 是第 $l$ 层第 $h$ 个头里 token $j$ 对物体 token $y_k$ 的注意力，$H$ 为头数，$m$ 为输入长度。它无需任何额外前向、可在推理途中"顺手"算出。和 $D_{\text{MI}}$ 比，PAS 直接测量"当前这一个具体输入"的内部信息依赖，而非依赖在有限参考集上的噪声估计，因此**反而更准**（见实验）——这是"理论指路、廉价实现却更强"的关键。

**3. 层选择与多头平均：用第 0 层、对所有头取平均**

PAS 用哪一层的注意力很关键。作者按 Fig. 5 的逐层 AUROC 消融，发现**第一层（layer 0）效果最好**，并与"早期层负责聚合信息、后期层负责加工信息"的已有解释吻合——幻觉与否在信息聚合阶段就已显现。多头方面，为简单起见对一层内所有头取平均（沿用 SVAR 设定）；虽有工作指出挑选头子集可能更优，但会引入额外复杂度与验证成本，作者留作未来工作。这一设计让 PAS 落到一个无超参挑选负担的默认配置：**layer 0 + 全头平均**。

### 损失函数 / 训练策略
本方法完全**免训练**：不改模型、不微调、不引外部裁判，只在推理时读取注意力权重计算 $s_{\text{prel}}$，再以阈值 $\tau$ 判定 $D_{\text{PAS}}(y_k)\ge\tau$ 为幻觉，可实时过滤与干预。

## 实验关键数据

> 评测指标说明：**AUROC**（检测分数对"真实/幻觉"二分类的 ROC 曲线下面积，越高越好，免去选阈值）；物体 token 用 CHAIR 式字符串匹配（对照图像已知物体列表）来界定真实/幻觉。模型用 LLaVA-1.5-7B、MiniGPT-4、Shikra（均 7B），数据集为 MSCOCO（80 类，采 5000 张）与 Pascal VOC（20 类，5823 张），贪心解码、max new tokens=512。

### 主实验
PAS 与各类免训练免参考基线在 6 个"模型×数据集"组合上的检测 AUROC（%）：

| 方法 | 类型 | LLaVA MSCOCO | LLaVA VOC | MiniGPT MSCOCO | Shikra MSCOCO | 平均 |
|------|------|------|------|------|------|------|
| NLL | logits | 56.5 | 64.0 | 62.1 | 54.3 | 62.2 |
| Entropy | logits | 71.7 | 64.3 | 69.8 | 71.4 | 67.4 |
| IC | 表示 | 75.1 | 64.6 | 76.4 | 76.0 | 71.9 |
| GLSim | 表示 | 64.1 | 69.4 | 63.6 | 67.8 | 65.6 |
| SVAR | 注意力(图像) | 81.5 | 82.9 | **88.0** | 71.9 | 80.3 |
| **PAS（本文）** | 注意力(prelim) | **84.2** | **85.1** | 85.6 | **84.5** | **85.0** |

PAS 平均 85.0%，超过所有基线；最强对手 SVAR 同为纯注意力方法但盯图像 token，在 Shikra 上明显落后（71.9 vs 84.5）。同时 PAS 的显存开销（18GB）与 SVAR 持平，比隐状态类 GLSim（19GB）/IC（30GB）更省，每样本额外显存比 GLSim 少约 33%。

### 消融实验
不同 token 类型注意力分数的检测能力（平均 AUROC %），以及 $D_{\text{MI}}$ 各 $\Delta$ 变体对比：

| 配置 | 平均 AUROC | 说明 |
|------|-----------|------|
| Prelim（layer 0，即 PAS） | **84.8** | 本文默认 |
| Instruction（layer 0） | 84.7 | 与 prelim 高度相关，故也很强 |
| Image（layer 0） | 82.1 | 即 SVAR 类信号，弱于 prelim |
| BOS（layer 0） | 83.1 | — |
| Entropy diff（$D_{\text{MI}}$ 式 4） | 74.5 | 互信息变体，慢且较弱 |
| KL div（式 8） | 80.2 | 互信息变体 |
| Logit diff（式 9） | 82.2 | 互信息最优变体，仍逊于 PAS |

### 关键发现
- **prelim 注意力是比图像注意力更强的信号**：同在 layer 0，$s_{\text{prel}}$（84.8）> $s_{\text{img}}$（82.1）。作者解释"低图像注意力是症状，高 prelim 注意力是模型切入不可靠模式的更直接证据"。⚠️ 指令注意力（84.7）几乎一样强，作者归因于 softmax 约束导致 prelim 与指令注意力高度相关，并非独立的理论信号。
- **简单 PAS 反超理论严格的互信息检测器**：PAS（85.0）> 最优 $D_{\text{MI}}$ 变体 Logit diff（82.2），且零额外前向；原因是 PAS 直接读当前输入的内部依赖，避开了对参考集边缘概率的噪声估计。
- **对解码策略鲁棒**：在 LLaVA-1.5-7B/MSCOCO 上，PAS 在贪心/beam/top-k/nucleus 四种解码下分别为 84.2/84.0/83.5/84.0，始终领先 SVAR（81.5/81.3/79.9/80.4），说明实用性不挑解码方式。

## 亮点与洞察
- **逆向利用"垃圾信息"**：别人都嫌 prelim 信息少而丢弃，本文恰恰把"模型多看了垃圾信息"当成不可信的报警器——视角转换很漂亮，是典型的"换个符号就发现新信号"。
- **理论与工程双轨**：先用条件互信息把假设写死、证明它对，再退化成一个零成本的注意力求和。理论那一支即便不用也不浪费，它让"为什么 PAS 有效"站得住脚。
- **可迁移的判别原则**：把"模型对不可靠输入来源的依赖度"作为幻觉/错误信号的思路，可推广到纯文本 LLM 的事实性检测、RAG 中"模型是否真的看了检索证据"等场景——只要找到对应的"prelim 注意力"代理量即可。

## 局限与展望
- 作者承认：多头处理只做了简单平均，挑选头子集可能更优但未做；互信息那一支因 $L+1$ 倍前向不实用，只作理论验证。
- ⚠️ 自评局限：检测与缓解是互补的，PAS 只做**检测**不做缓解，落地仍需配合干预策略；且 prelim 与指令注意力的强相关说明该信号未必是"纯粹"的 prelim 效应，理论解释有一定模糊性。
- 实验仅在 7B 级 LLaVA/MiniGPT/Shikra 上充分展开（更大模型放在附录），且只覆盖 MSCOCO/Pascal VOC 两个目标-存在型数据集，对开放词表、长描述、细粒度属性幻觉的适用性待验证。
- 改进方向：把 PAS 与 mitigation 方法串成"检测—干预"闭环；探索按头/按层学习加权的 prelim 注意力，进一步拉开与图像注意力的区分度。

## 相关工作与启发
- **vs SVAR（注意力·图像）**：两者都纯用注意力，但 SVAR 量化对图像 token 的依赖（低 → 幻觉），PAS 量化对 prelim 的依赖（高 → 幻觉）。本文实证二者虽因 softmax 约束相关却不冗余，prelim 信号更直接、更准（85.0 vs 80.3）。
- **vs IC / GLSim（表示类）**：它们用 Logit Lens 把图像隐状态映射到词表查图-物兼容，依赖隐状态、显存更高（IC 30GB），且仍聚焦图像；PAS 只用注意力权重、更省更快，平均 AUROC 也更高。
- **vs NLL / Entropy（logits 类）**：仅凭输出 logits 的不确定性，用的信息最少、性能最差（62–67）；本文表明引入被忽视的 prelim 注意力能大幅提升。
- **vs mitigation 路线（VCD/OPERA 等）**：那些方法改输入/解码以减少幻觉，与本文的检测目标互补——检测不直接消幻觉，但能为干预提供实时定位信号。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ "prelim 注意力即幻觉信号"是被前人系统忽略的新视角，理论+工程双证。
- 实验充分度: ⭐⭐⭐⭐ 三模型两数据集四解码策略覆盖扎实，但更大模型与更丰富幻觉类型仅在附录/未覆盖。
- 写作质量: ⭐⭐⭐⭐ 从假设到验证到落地逻辑清晰，公式与图表支撑到位。
- 价值: ⭐⭐⭐⭐ 免训练、零额外开销、可实时，工程落地价值高，但仅检测、需配缓解。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models](hulluedit_single-pass_evidence-consistent_subspace_editing_for_mitigating_halluc.md)
- [\[CVPR 2026\] First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models](first_logit_boosting_visual_grounding_method_to_mitigate_object_hallucination_in.md)
- [\[CVPR 2026\] Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](same_attention_different_truths_put_logit-lens_over_visual_attention_to_detect_a.md)
- [\[ACL 2025\] Retrieval Visual Contrastive Decoding to Mitigate Object Hallucinations in Large Vision-Language Models](../../ACL2025/hallucination/retrieval_visual_contrastive_decoding_to_mitigate_object_hallucinations_in_large.md)
- [\[ICML 2026\] Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucination Detector for Multimodal Large Language Models](../../ICML2026/hallucination/instruction_lens_score_your_instruction_contributes_a_powerful_object_hallucinat.md)

</div>

<!-- RELATED:END -->
