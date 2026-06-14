---
title: >-
  [论文解读] ReBaPL: Repulsive Bayesian Prompt Learning
description: >-
  [CVPR 2026][多模态VLM][提示学习] ReBaPL 把 CLIP 的 prompt 学习从"找一个最优解"改成"用循环式 SGHMC 从后验里采一组多样的好 prompt"，并在表征空间用 MMD/Wasserstein 度量加一个"排斥力"防止采样塌缩到单一模式，从而以即插即用的方式给任意 MLE prompt 学习方法（MaPLe、MMRL）加上贝叶斯外壳，显著改善 base-to-novel、跨数据集与域泛化。
tags:
  - "CVPR 2026"
  - "多模态VLM"
  - "提示学习"
  - "贝叶斯推断"
  - "SGHMC"
  - "排斥力"
  - "后验采样"
  - "泛化"
---

# ReBaPL: Repulsive Bayesian Prompt Learning

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Bendou_ReBaPL_Repulsive_Bayesian_Prompt_Learning_CVPR_2026_paper.html)  
**代码**: https://github.com/SigmaNova/ReBaPL  
**领域**: 多模态VLM  
**关键词**: prompt 学习, 贝叶斯推断, SGHMC, 排斥力, 后验采样, 泛化

## 一句话总结
ReBaPL 把 CLIP 的 prompt 学习从"找一个最优解"改成"用循环式 SGHMC 从后验里采一组多样的好 prompt"，并在表征空间用 MMD/Wasserstein 度量加一个"排斥力"防止采样塌缩到单一模式，从而以即插即用的方式给任意 MLE prompt 学习方法（MaPLe、MMRL）加上贝叶斯外壳，显著改善 base-to-novel、跨数据集与域泛化。

## 研究背景与动机
**领域现状**：CLIP 这类视觉-语言模型靠 prompt 学习做少样本适配——不微调整个模型，只学连续 prompt 向量。从只学文本端的 CoOp/CoCoOp，到同时在图文两端多层插可学 token 并用耦合函数对齐的多模态 prompt 学习（MaPLe、MMRL、VaMP），精度不断提升。

**现有痛点**：标准 prompt 学习靠最大似然估计（MLE）优化，**极易过拟合**训练类，导致对分布外（OOD）样本和未见类泛化差。CoOp 尤其严重；正则化方法（PromptSRC、ProDA）能缓解，但它们仍把学习导向**单一最优解流形**，无法刻画 prompt 后验里潜在的多模态结构。

**核心矛盾**：prompt 损失地形里存在**很多训练损失相当、但泛化能力差异很大**的解。只盯着一个点估计（哪怕加正则）会错过那些泛化更好的"其他模式"。

**本文目标**：不去求单点解，而是去**刻画整个 prompt 后验分布** $p(\omega\mid\mathcal{D})$，并尽可能覆盖其多个高密度模式，从而在不过拟合 base 类的前提下提升对 novel 类的泛化。

**切入角度**：已有贝叶斯 prompt 学习（多用单峰高斯变分近似，如 VaMP）或确定性粒子法（APP 用 SVGD）都受限——要么单峰、要么粒子交互昂贵。作者改用**基于采样的 MCMC**（SGHMC）来表示后验，并加循环调度 + 排斥力来主动探索多模态。

**核心 idea**：循环式随机梯度哈密顿蒙特卡洛（rcSGHMC）= 哈密顿动力学 + 循环学习率（交替探索/采样）+ 表征空间排斥力，且做成**可套在任何 MLE prompt 学习方法之上的即插即用贝叶斯扩展**。

## 方法详解

### 整体框架
ReBaPL 不改底层 prompt 学习方法的网络结构，而是替换它的"优化过程"。把多模态 prompt 学习的 MAP 估计 $\omega^*_{\text{MAP}}=\arg\max_\omega \log p(\omega)+\sum_i p(y_i\mid u_i,\omega)$ 看成一次点估计，ReBaPL 转而从后验 $p(\omega\mid\mathcal{D})\propto p(\mathcal{D}\mid\omega)p(\omega)$ 里**采一组样本** $\{\omega^{(c)}_{k,T}\}$（$\omega$ 含所有可学 prompt 与耦合函数参数），最后对这组样本做集成预测 $p(y\mid x)=\sum_{c,k}\gamma_{c,k}\,p(y\mid x,\omega^{(c)}_{k,T})$（均匀权 $\gamma_{c,k}=(CK)^{-1}$）。采样过程用 rcSGHMC（Algorithm 1）：按余弦调度循环更新步长，每个循环内前一段是**探索阶段**（不注噪、靠哈密顿动力学快速跨越损失地形找新模式）、后一段是**采样阶段**（注入噪声、在模式附近采高质量样本）；同时让当前循环的样本被上一循环样本**排斥**，避免重复落进同一模式。这是个针对优化/采样动力学的改进，没有新增可画成 pipeline 的模块分支，故不配框架图。

### 关键设计

**1. 循环式 SGHMC：交替"探索新模式"和"在模式里采样"**

针对"只收敛到单一解流形"的痛点，作者用 SGHMC（带动量 $r$ 和摩擦项 $\alpha$ 的随机梯度采样器）替代普通梯度优化，并叠加 Zhang 等人的循环调度。步长 $\eta_t$ 用余弦调度循环升降；每个循环 $c$ 内按平衡参数 $\beta$ 切两段：探索阶段（$\frac{t}{T}\le\beta$）不注噪，让动量驱动样本快速跨越地形、发现新模式；采样阶段（$\frac{t}{T}>\beta$）才注入 $\sqrt{2(\alpha-\hat\gamma)\eta_t}\,\xi_t$ 噪声，在已发现的模式附近采样。更新形如

$$r^{(c)}_{k,t+1}=(1-\alpha)r^{(c)}_{k,t}-\eta_t\nabla\tilde U(\omega^{(c)}_{k,t})+\mathbb{I}_{t/T>\beta}\sqrt{2(\alpha-\hat\gamma)\eta_t}\,\xi_t,$$

其中 $\tilde U$ 是 mini-batch 估计的势能（负对数似然）。这样既有 mini-batch 的计算效率，又有动量带来的快速地形探索能力。

**2. 表征空间的排斥力：用 MMD/Wasserstein 推开"功能上相似"的 prompt**

光循环采样还可能反复落进相近模式，所以作者在循环之间加一个排斥力：当前循环样本 $\{\omega^{(c)}_{k,t}\}$ 被上一循环样本 $\{\omega^{(c-1)}_{\ell,T}\}$ 推开。排斥来自一个势函数 $V(\omega,\omega')=\frac{1}{d_\Pi(\omega,\omega')^2+\epsilon}$，力 $F(\omega,\omega')=-\nabla_\omega V$——参数越相似势越大、推力越强。关键创新在于**不在权重空间直接比参数**（权重空间有置换不变性、数据稀缺，几何很难刻画），而是比"两组参数诱导出的表征分布"之间的距离：$d_\Pi(\omega,\omega')=d_{\mathcal{P}(U)}(U_\omega,U_{\omega'})$，其中 $U_\omega=\{u_{\omega,i}\}$ 是一个 mini-batch 图像在该 prompt 下的表征集合，$d_{\mathcal{P}(U)}$ 取 MMD 或 Wasserstein 距离。这等于按 prompt 的**功能相似性**（产生的表征像不像）来排斥，鼓励探索功能上真正不同的模式。因为度量在 mini-batch（约 32 样本）上算，$O(n^2)$/$O(n^3)$ 的开销可忽略。

**3. 即插即用的贝叶斯扩展 + 样本集成推理**

和先前贝叶斯 prompt 方法（VaMP 单峰高斯变分、APP 确定性 SVGD）不同，ReBaPL 不绑定特定网络，而是把上述 rcSGHMC 当成一个**替换 MLE 优化器的训练算法**，可套在任何基于 MLE 的 prompt 学习方法之上。论文实测把它分别套在 MaPLe 和 MMRL 上。训练结束得到 $C\times K$ 组参数样本，推理时对它们做均匀加权集成；这 $C\times K$ 个模型的前向是"embarrassingly parallel"，额外开销小。这种模块化让任何现有方法都能低成本获得贝叶斯式的后验刻画与泛化收益。

> ⚠️ 部分公式中的希腊字母/符号在缓存文本里有 OCR 噪声（如摩擦项、噪声估计项），细节以原文 Algorithm 1 与 Eq.(16) 为准。

## 实验关键数据

统一 16-shot 设置，三套协议：base-to-novel 类泛化、跨数据集迁移、域泛化。底座方法 MaPLe / MMRL，各自加 ReBaPL。对比 CLIP、CoOp、CoCoOp、APP、PromptSRC 等。

### 主实验
Base-to-Novel（11 数据集平均，Base/Novel/HM 准确率，HM 为调和平均，越高越好）：

| 方法 | Base | Novel | HM |
|------|------|-------|----|
| CLIP | 69.34 | 74.22 | 71.70 |
| PromptSRC* | 84.93 | 74.49 | 78.61 |
| MaPLe* | 82.03 | 75.03 | 78.37 |
| MaPLe* + ReBaPL | 83.28 | 76.08 | **79.52** (+1.15) |
| MMRL* | 85.54 | 76.52 | 80.59 |
| MMRL* + ReBaPL | 85.74 | 77.44 | **81.38** (+0.79) |

加 ReBaPL 后两个底座的 Base 与 Novel 多数都涨，HM 分别提升 +1.15 / +0.79；在 FGVCAircraft、EuroSAT、DTD 等难数据集上 Novel 涨幅尤其大（如 MMRL+ReBaPL 在 EuroSAT Novel +6.43）。

跨数据集迁移（ImageNet 训练 → 10 个目标集，平均准确率）：MMRL+ReBaPL 取得最高 **67.62%**（+0.75），MaPLe+ReBaPL 66.77%（+1.14），其中 EuroSAT 目标涨幅高达 +5.20 / +3.14。域泛化（ImageNet → V2/Sketch/A/R）四个 OOD 变体上 ReBaPL 一致改善，MaPLe+ReBaPL 在 ImageNet-A 最佳、MMRL+ReBaPL 在源域 ImageNet 最高。

### 消融实验
排斥力与概率度量选择（11 数据集平均，Base/Novel/HM，Tab.4）：

| 配置 | Base | Novel | HM |
|------|------|-------|----|
| MaPLe（底座） | 82.03 | 75.03 | 78.37 |
| + ReBaPL（无排斥） | 83.39 | 75.47 | 78.93 |
| + ReBaPL（Wasserstein） | 83.39 | 75.86 | 79.44 |
| + ReBaPL（MMD） | 83.28 | 76.08 | **79.52** |

### 关键发现
- **采样本身就有收益，排斥力专攻 novel**：即使去掉排斥（纯循环 SGHMC），HM 也比 MaPLe 高（78.93 vs 78.37），说明"从后验采样而非点估计"已带来增益；再加排斥力主要把 **Novel 准确率**进一步推高（75.47→76.08），印证"更彻底地探索后验地形 → 更好泛化"的核心主张。
- **对度量选择鲁棒**：Wasserstein 与 MMD 的 HM 仅差 0.08%，远小于相对 MaPLe 约 1% 的整体提升，说明方法不挑概率度量。
- **难数据集/OOD 收益最大**：EuroSAT、FGVCAircraft、ImageNet-A/Sketch 这类分布差异大的场景涨幅最明显，符合"贝叶斯后验刻画改善 OOD 泛化"的预期。

## 亮点与洞察
- **在表征空间而非权重空间施加排斥**：绕开了权重空间置换不变性与数据稀缺的难题，用"prompt 诱导的表征分布距离"刻画功能相似性——这个把多样性约束搬到函数空间的想法很可迁移（如贝叶斯神经网络集成、深度集成的多样化）。
- **即插即用的贝叶斯外壳**：把"探索后验"做成可套在任意 MLE prompt 方法上的优化器替换，不改网络结构就拿到泛化收益，工程上极友好；MaPLe/MMRL 都受益验证了通用性。
- **循环调度把"探索 vs 采样"显式解耦**：探索阶段不注噪靠动量跨地形、采样阶段注噪采样，这种相位切换是它能稳定发现多模式的关键，比单峰变分更贴近真实多模态后验。

## 局限与展望
- 训练得到 $C\times K$ 个样本模型，虽推理可并行，但**显存/存储成本**随样本数线性增长，正文未给出与单模型的资源开销正面对比。
- 概率度量仅试了 MMD 与 Wasserstein；作者把 Sinkhorn 散度、信息论度量等列为未来工作，当前选择略显有限。
- 循环数 $C$、探索比例 $\beta$、排斥强度 $\zeta$ 等超参需人工设定；作者也承认应做"按收敛诊断/后验多样性自适应调整循环数"的机制。
- ⚠️ 未与 VaMP 直接对比（因其代码未公开），多模态贝叶斯 prompt 方法之间的横向比较不完整。

## 相关工作与启发
- **vs APP（SVGD 粒子法）**：APP 用确定性的 Stein 变分梯度下降让一组粒子交互逼近多模；ReBaPL 用高效 MCMC（SGHMC）采样表示后验，并把排斥放到表征空间，作者称能更丰富地刻画各模式周围高密度区。
- **vs VaMP（变分多模态）**：VaMP 用单峰高斯变分近似后验、做实例级不确定性 prompt；ReBaPL 不受单峰限制，靠采样 + 排斥覆盖多模态。
- **vs PromptSRC / ProDA（正则化 MLE）**：它们仍是把学习导向单一解流形的点估计 + 正则；ReBaPL 直接刻画后验分布，从根上解决"错过其他泛化更好模式"的问题。
- **vs MaPLe / MMRL（底座）**：二者是被扩展对象——ReBaPL 不替换它们的图文耦合结构，只替换优化方式，因而能即插即用地在其上叠加贝叶斯收益。

## 评分
- 新颖性: ⭐⭐⭐⭐ 把循环 SGHMC + 表征空间排斥引入 prompt 后验采样，并做成即插即用，组合新颖。
- 实验充分度: ⭐⭐⭐⭐ 三套协议 × 11 数据集 + 两个底座 + 度量消融，较充分；缺资源开销与 VaMP 直接对比。
- 写作质量: ⭐⭐⭐⭐ 背景（prompt 学习/贝叶斯/概率度量）铺垫扎实；部分采样公式符号偏密。
- 价值: ⭐⭐⭐⭐ 给 prompt 学习提供了一个通用、可叠加的贝叶斯泛化增强范式，落地门槛低。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] BiomedCCPL: Causal Conditional Prompt Learning for Biomedical Vision-Language Models](biomedccpl_causal_conditional_prompt_learning_for_biomedical_vision-language_mod.md)
- [\[CVPR 2026\] Controllable Federated Prompt Learning at Test Time](controllable_federated_prompt_learning_at_test_time.md)
- [\[CVPR 2026\] Noise-Aware Few-Shot Learning through Bi-directional Multi-View Prompt Alignment](noise-aware_few-shot_learning_through_bi-directional_multi-view_prompt_alignment.md)
- [\[CVPR 2026\] STAR: Test-Time Adaptation Can Enhance Universal Prompt Learning for Vision-Language Models](star_test-time_adaptation_can_enhance_universal_prompt_learning_for_vision-langu.md)
- [\[ICCV 2025\] Calibrating MLLM-as-a-Judge via Multimodal Bayesian Prompt Ensembles](../../ICCV2025/multimodal_vlm/calibrating_mllm-as-a-judge_via_multimodal_bayesian_prompt_ensembles.md)

</div>

<!-- RELATED:END -->
