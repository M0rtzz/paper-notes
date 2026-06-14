---
title: >-
  [论文解读] RaPA: Enhancing Transferable Targeted Attacks via Random Parameter Pruning
description: >-
  [CVPR 2026][AI安全][定向迁移攻击] RaPA 发现现有定向迁移攻击的对抗扰动过度依赖代理模型里少数关键参数，于是在每步优化时对参数做随机剪枝（DropConnect），等价于给损失加一项"重要性均衡正则"，从而打散依赖、显著提升跨架构（尤其 CNN→Transformer）的定向攻击成功率。
tags:
  - "CVPR 2026"
  - "AI安全"
  - "定向迁移攻击"
  - "对抗样本"
  - "随机参数剪枝"
  - "自集成"
  - "重要性正则"
---

# RaPA: Enhancing Transferable Targeted Attacks via Random Parameter Pruning

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Su_RaPA_Enhancing_Transferable_Targeted_Attacks_via_Random_Parameter_Pruning_CVPR_2026_paper.html)  
**代码**: [https://github.com/molarsu/RaPA](https://github.com/molarsu/RaPA)  
**领域**: AI安全 / 对抗攻击迁移  
**关键词**: 定向迁移攻击, 对抗样本, 随机参数剪枝, 自集成, 重要性正则

## 一句话总结
RaPA 发现现有定向迁移攻击的对抗扰动过度依赖代理模型里少数关键参数，于是在每步优化时对参数做随机剪枝（DropConnect），等价于给损失加一项"重要性均衡正则"，从而打散依赖、显著提升跨架构（尤其 CNN→Transformer）的定向攻击成功率。

## 研究背景与动机

**领域现状**：迁移式黑盒攻击只在一个白盒代理模型上生成对抗样本，再拿去骗不可见的目标模型。相比无定向攻击，**定向**迁移攻击（要把图分类到指定错误类别）成功率（ASR）一直低得多。主流提升手段有三类：输入变换（DI/RDI/Admix/CFM/FTM 等做多样化变换抑制过拟合）、梯度稳定（MI/SI 等加动量或多尺度），以及自集成（从单个代理模型造出多个变体，如 Ghost Network、MUP、SE-ViT）。

**现有痛点**：尽管 CFM、FTM 把 ASR 推到了新高，定向迁移成功率仍然偏低，对抗样本"白盒强、黑盒弱"——在代理模型上很灵，换个架构就失效。这些方法都在输入空间或特征空间做文章，没人追问到底是模型的什么导致了过拟合。

**核心矛盾**：作者通过一个 pilot study 发现了一个被忽视的根因——对抗扰动**过度集中依赖代理模型中极少数"关键参数"**。这些参数来自特定训练方案/数据/架构，换一个参数配置不同的目标模型就对不上，相当于扰动学到了一批"捷径参数"。

**本文目标**：在不显著增加计算的前提下，打散这种对少数参数的强依赖，让扰动的重要性更均匀地分布到全部参数上，从而更好地迁移。

**切入角度**：既然直接屏蔽"最重要参数"既要算二阶导（昂贵）又会让代理模型能力骤降（生成的样本连原模型都骗不了），那不如**随机**剪枝——便宜，且在期望意义上恰好起到均衡重要性的作用。

**核心 idea**：每步优化对代理模型参数做伯努利随机掩码（DropConnect），用多个掩码变体的平均梯度更新对抗样本；理论上证明它等价于在原损失上加一项重要性惩罚，逼扰动不再依赖少数参数。

## 方法详解

### 整体框架
RaPA 要解决的是定向迁移攻击的过拟合根因——扰动死死依赖代理模型里少数高重要性参数。它的整条逻辑是"先诊断、再开方"：先用一个 pilot study 量化出"剪掉最重要的 0.5% 参数 ASR 暴跌、剪掉最不重要的 0.5% 几乎无影响"这一现象，坐实过度依赖确实存在；再针对它提出随机参数剪枝，并从二阶 Taylor 展开证明随机掩码在期望意义上等价于一个让各参数贡献均等的正则项。

落到执行上，RaPA 不改对抗样本的优化主框架，而是嵌进每一步迭代：在第 $t$ 步，对选中的线性层与归一化层独立采样伯努利随机掩码、生成代理模型的多个剪枝变体，每个变体过一遍前向反向得到一个梯度，把 $S$ 个变体的梯度平均后再用 MI-TI 等迭代方法更新对抗样本并投影回 $\epsilon$-球。因为掩码逐层、逐步都重新采样，等于每步都在一组语义一致但参数各异的"自集成"模型上求共识方向，天然比依赖单一参数配置更可迁移。它是 training-free、跨架构、即插即用的——可以直接套在现有任意输入变换/梯度稳定方法之上。

> RaPA 本质是一个作用在参数层面的随机正则/自集成机制，而非多阶段流水线，故不画框架图，用下面的诊断—机制—落地三步讲清。

### 关键设计

**1. 诊断：对抗扰动过度依赖少数关键参数**

要对症下药，先得证明病灶存在。作者借用 Optimal Brain Damage（OBD）的敏感度分析，定义参数 $\theta_i$ 的重要性 $I(\theta_i)=\frac{\partial^2 L(f(x_{adv}))}{\partial \theta_i^2}\times \theta_i^2$（二阶导乘参数平方，近似"删掉该参数损失会变多少"）。据此把代理模型参数分成"最重要 0.5%"和"最不重要 0.5%"两组，分别剪掉后看 ASR。结果很尖锐：在 ResNet-50 上，剪掉最重要的 0.5% 让 ASR 暴跌 **46% 以上**（RaPA 自身从 98.2 跌到 64.5，而 DI 等基线跌到 16–37），而剪掉最不重要的 0.5% 几乎无影响。这直接证明现有方法生成的对抗样本高度依赖那一小撮关键参数——这正是它们换架构就失效的根因，也指明了"打散依赖"这条改进路径。

**2. 随机参数剪枝 ≡ 重要性均衡正则**

诊断之后的直觉做法是"每步屏蔽最重要参数"，但这既要算二阶导（对全部参数太贵），屏蔽后代理模型能力又会骤降到连自己都骗不了。RaPA 换成**随机**剪枝绕开这两个坑。定义随机二值掩码 $M\in\{0,1\}^{|\theta|}$，每位独立服从 $M_i\sim\text{Bernoulli}(1-p)$（$p$ 为掩码概率），前向用的参数变成 $M\odot\theta$。关键是对随机掩码取期望、做二阶 Taylor 展开后：

$$\mathbb{E}_M[L(f(x_{adv};M\odot\theta))]\approx L(f(x_{adv};\theta))+\frac{p(1-p)}{2}\sum_i \frac{\partial^2 L(f(x_{adv};\theta))}{\partial\theta_i^2}\theta_i^2$$

第一项是原损失，第二项恰好正比于全部参数的重要性 $I(\theta_i)$ 之和——也就是一项**重要性惩罚**。每步重采样掩码去最小化这个目标，等价于逼对抗样本把重要性摊薄到所有参数上，不让任何少数参数独大，于是天然更鲁棒、更可迁移。这一步把"随机剪枝"和"诊断里发现的过度依赖"在数学上严丝合缝地接上了。

**3. 用 DropConnect 落地到线性层与归一化层，并做多变体自集成**

随机参数剪枝在形式上等同于训练里的 DropConnect。作者观察到 DropConnect 主要在**线性层**上有效，因此把它施加到线性层的权重与偏置、以及归一化层的变换参数（缩放/平移）——这两类层在含 Transformer 的主流架构里都普遍存在，保证跨架构通用。对线性层 $W\in\mathbb{R}^{d_{in}\times d_{out}}$、$b$，分别采样 $M_w\sim\text{Bernoulli}(1-p_w)$、$M_b\sim\text{Bernoulli}(1-p_b)$，得 $W_M=M_w\odot W$、$b_M=M_b\odot b$，归一化层同理；实现上简单取 $p_w=p_b=p$。每步做 $S$ 次推理、每次重采样掩码，就得到 $S$ 个"语义一致但参数各异"的变体，平均其梯度更新对抗样本——这天然是一种自集成。相比 Ghost Network（只扰动残差跳连）、MUP/DWP（按固定指标剪不重要参数）这些确定性或局部的扰动，RaPA 逐层逐步的随机性引入了更强的多样性，用 Gini 系数衡量参数重要性分布也最均匀（见实验）。

### 损失函数 / 训练策略
RaPA 不训练任何东西（training-free），只在攻击优化里改梯度估计。沿用 $\ell_\infty$ 约束、$\epsilon=16/255$、步长 $\alpha=2/255$、Logit loss 作目标；每步对 $S$ 个剪枝变体求平均梯度后用 MI-TI 更新。DropConnect 概率 $p$ 按代理模型微调：ResNet-50 取 0.05、Inception-v3 取 0.02、DenseNet-121 取 0.04、ViT 取 0.01、CLIP 取 0.03，默认对所有线性层与归一化层施加。

## 实验关键数据

数据集为 ImageNet-Compatible（NIPS 2017 攻击挑战官方集，自带定向标签），代理模型涵盖 CNN（RN50/Incv3/DN121 等）与 Transformer（ViT），目标模型 16 个（含 CLIP 跨模态），主实验 $S=5$。

### 主实验

| 迁移设置 | 代理模型 | 之前SOTA(ASR%) | RaPA(ASR%) | 提升 |
|----------|----------|----------------|------------|------|
| CNN→Transformer（5 目标，最难） | ResNet-50 | 33.3 (FTM) | 45.0 | +11.7 |
| CNN→Transformer | DenseNet-121 | 22.8 (FTM) | 40.3 | +17.5 |
| →CNN（10 目标） | Inception-v3 | 54.9 (CFM) | 68.0 | +13.1 |
| →CNN（10 目标） | ViT | 40.1 (CFM) | 51.2 | +11.1 |

最难的 CNN→Transformer 迁移上 RaPA 把平均 ASR 从 33.3% 提到 45.0%；对强防御 ensIR、HGD，RaPA 比次优分别高 **29.4%** 和 **10.5%**。

### 消融实验

| 配置 | 平均ASR(%)（16 目标，RN50 代理） | 说明 |
|------|--------------------------------|------|
| BN + FC 层（推荐） | 72.4 | 与理论分析一致，最优 |
| 仅 BN 层 | 72.1 | 已接近最优 |
| 仅 Conv 层 | 65.1 | Conv 权重更稀疏、受过度依赖影响小 |
| 全部层 | 69.2 | 也优于所有基线 |
| 仅 FC 层 | 41.1 | RN50 只有单个 FC 层，多样性不足 |

剪枝概率 $p$：在 16 目标上均值 ASR 66.3%、标准差 5.9%，$p=0.05$ 峰值 72.4%；$p\in[0.03,0.07]$ 稳定超基线 2% 以上。

### 关键发现
- **DropConnect 该打在线性/归一化层**：BN+FC 组合最好（72.4%），印证第 3 点的实现选择；纯 Conv 层效果差，因 Conv 权重稀疏、本就不太受"过度依赖"困扰。
- **Gini 系数最低**：RaPA 的参数重要性分布全层平均 Gini 仅 0.08（CFM 0.19、DI 0.32），定量证明它确实把重要性摊平了。
- **越加算力收益越大**：把迭代数 300→500、每步推理 $S$ 1→5，平均 ASR 提升 15.9%，是所有方法里 scaling 收益最高的，说明随机自集成能持续吃进更多计算预算。
- **对 $p$ 不敏感**：在 0.03–0.07 区间都稳定超基线，超参好调。

## 亮点与洞察
- **"随机剪枝≡重要性正则"的等价证明**：把一个工程化的随机掩码用二阶 Taylor 展开接到一个可解释的正则项上，既给了方法理论根基，也解释了为什么有效——这是全文最"啊哈"的一步。
- **诊断驱动方法**：先用 OBD 重要性 + 剪枝实验坐实"过度依赖少数参数"这一根因，再针对性开方，比单纯堆 trick 更有说服力。
- **即插即用 + training-free**：作为参数层面的随机化，可叠加在任意现有输入变换/梯度稳定攻击之上，迁移性好的思路也可借鉴到其他需要"抑制对单一子结构依赖"的鲁棒性/泛化问题。

## 局限与展望
- DropConnect 概率 $p$ 仍需按代理模型逐个微调，缺乏自适应选取机制。
- 理论等价基于二阶 Taylor 近似且 $p$ 较小（$\mathbb{E}[M_i]\approx 1$），$p$ 偏大时近似是否成立未深入讨论。
- 主要验证在分类任务的定向迁移攻击；对检测/分割等其他任务、以及防御方更新后的有效性还需进一步检验。
- 作为提升攻击迁移性的工作，其价值更在于揭示模型脆弱性、推动防御研究，实际部署需注意伦理与安全边界。

## 相关工作与启发
- **vs CFM / FTM（输入/特征变换）**: 它们在输入或特征空间做多样化以抑制过拟合，RaPA 转到**参数空间**找根因（过度依赖少数参数），二者正交、可叠加，RaPA 在多数设置下反超它们。
- **vs Ghost Network / MUP / DWP（自集成/确定性剪枝）**: Ghost 只扰残差跳连、MUP/DWP 按固定指标剪不重要参数，都是确定性或局部扰动；RaPA 逐层逐步随机剪枝引入更强多样性，Gini 更低、ASR 大幅领先。
- **vs SE-ViT（ViT 专用自集成）**: SE-ViT 专为 Transformer 代理设计，但即便用 ViT 作代理，RaPA 的 ASR 仍高于它。

## 评分
- 新颖性: ⭐⭐⭐⭐ 从参数依赖这一新视角切入，并给出随机剪枝≡重要性正则的等价证明
- 实验充分度: ⭐⭐⭐⭐⭐ 16 目标模型、CNN/Transformer/CLIP 全覆盖，含防御、消融与 scaling 分析
- 写作质量: ⭐⭐⭐⭐ 诊断→理论→实现逻辑清晰，pilot study 很有说服力
- 价值: ⭐⭐⭐⭐ training-free 即插即用，对理解模型脆弱性与推动防御有参考意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] VCP-Attack: Visual-Contrastive Projection for Transferable Black-Box Targeted Attacks on Large Vision-Language Models](vcp-attack_visual-contrastive_projection_for_transferable_black-box_targeted_att.md)
- [\[CVPR 2026\] AdvFM: Lookahead Flow-Matching Velocity-Field Attacks for Imperceptible and Transferable Adversarial Examples](advfm_lookahead_flow-matching_velocity-field_attacks_for_imperceptible_and_trans.md)
- [\[ECCV 2024\] CLIP-Guided Generative Networks for Transferable Targeted Adversarial Attacks](../../ECCV2024/ai_safety/clip-guided_generative_networks_for_transferable_targeted_adversarial_attacks.md)
- [\[CVPR 2026\] When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models](when_robots_obey_the_patch_universal_transferable_patch_attacks_on_vision-langua.md)
- [\[CVPR 2026\] Roots Beneath the Cut: Uncovering the Risk of Concept Revival in Pruning-Based Unlearning for Diffusion Models](roots_beneath_the_cut_uncovering_the_risk_of_concept_revival_in_pruning-based_un.md)

</div>

<!-- RELATED:END -->
