---
title: >-
  [论文解读] Multimodal Continual Instruction Tuning with Dynamic Gradient Guidance
description: >-
  [CVPR 2026][多模态VLM][多模态持续指令微调] 把多模态持续指令微调（MCIT）中的灾难性遗忘重新定义为「新任务训练时缺失了旧任务梯度」，DGG 用「当前参数指向旧任务最优参数的方向向量」近似旧任务梯度、与有限重放缓冲的真实梯度相加、再用伯努利采样动态调控更新频率，**不扩展模型**就在 VQAv2 / UCIT 上取得 SOTA。
tags:
  - "CVPR 2026"
  - "多模态VLM"
  - "多模态持续指令微调"
  - "灾难性遗忘"
  - "梯度近似"
  - "重放"
  - "伯努利采样"
---

# Multimodal Continual Instruction Tuning with Dynamic Gradient Guidance

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Multimodal_Continual_Instruction_Tuning_with_Dynamic_Gradient_Guidance_CVPR_2026_paper.html)  
**代码**: https://github.com/lisongze/DGG  
**领域**: 多模态VLM / 持续学习  
**关键词**: 多模态持续指令微调, 灾难性遗忘, 梯度近似, 重放, 伯努利采样

## 一句话总结
把多模态持续指令微调（MCIT）中的灾难性遗忘重新定义为「新任务训练时缺失了旧任务梯度」，DGG 用「当前参数指向旧任务最优参数的方向向量」近似旧任务梯度、与有限重放缓冲的真实梯度相加、再用伯努利采样动态调控更新频率，**不扩展模型**就在 VQAv2 / UCIT 上取得 SOTA。

## 研究背景与动机

**领域现状**：多模态大语言模型（MLLM）经大规模预训练 + 指令微调后，常需在新指令数据集上持续微调（MCIT）。主流 MCIT 方法多基于 LLaVA + LoRA，借助 Mixture-of-Experts（MoE）或 prompt 调优捕获任务专属知识（CoIN、CL-MoE、HiDE、DISCO、ModalPrompt）。

**现有痛点**：(1) 这类「学任务专属组件」的做法**不可避免地导致模型扩展**，在训练和推理阶段都带来额外参数存储与计算开销；(2) 不扩展模型的正则化方法（如 SEFE 的 RegLoRA）虽能约束参数更新保留旧知识，但大多用**静态正则项**，整个学习过程固定不变，难以适应不断演化的优化地形。

**核心矛盾**：要么扩模型换记忆（代价是膨胀），要么用静态正则（代价是不灵活）。能否在**不扩展模型**的前提下，用**动态**的方式巩固旧任务记忆？

**本文目标**：在不增加任何模型组件的情况下，提供一种随训练过程动态调整、且能与重放结合的旧知识保持机制。

**切入角度**：作者给灾难性遗忘换了个视角——联合训练所有任务的损失满足可加性 $L(\theta;T_1\cup T_2)=L(\theta;T_1)+L(\theta;T_2)$，梯度也可加 $\nabla L(\theta;T_1\cup T_2)=\nabla L(\theta;T_1)+\nabla L(\theta;T_2)$。持续学习到 $T_2$ 时旧任务 $T_1$ 的数据不可得，于是**缺了 $\nabla L(\theta;T_1)$ 这一项**，梯度下降只能收敛到新任务最优、而非联合最优 $\theta^*_{1:2}$，这正是遗忘的来源。

**核心 idea**：把「保持旧知识」重述为「近似缺失的旧任务梯度」问题——用「当前参数 → 旧任务最优参数」的方向向量去近似 $\nabla L(\theta;T_1)$，补回那一项缺失梯度。

## 方法详解

### 整体框架
DGG 不改动 MLLM 结构（LLaVA-7B + LoRA），只在**优化层面**做文章。在学习任务序列 $\{T_1,\dots,T_T\}$ 时，每到新任务 $T_t$，模型本可计算当前任务（含重放缓冲）的真实梯度 $\nabla L(\theta;T_t\cup M)$，但缺失旧任务梯度。DGG 做三件事：(1) 用「当前参数 $\theta$ 指向此前累计最优参数 $\theta^*_{1:t-1}$」的方向向量近似旧任务梯度 $\hat g$（梯度引导）；(2) 把 $\hat g$ 与重放缓冲 $M$ 的真实梯度相加，得到更准的旧任务梯度近似；(3) 用伯努利采样以概率 $\alpha$ 决定每步是否注入 $\hat g$，在稳定性（记旧）与可塑性（学新）间动态权衡。整个方法是对优化器梯度的「即插即用」修改（见原文 Algorithm 1），不引入新参数。本方法是纯优化层面的梯度近似 + 调控，并非多阶段管线，故不画框架图。

### 关键设计

**1. 梯度引导近似：用「指向旧任务最优参数的方向向量」补回缺失的旧任务梯度**

直接缓存少量旧样本重放是常见做法，但缓冲样本少、无法代表 $T_1$ 整个数据分布在梯度下降全过程中的期望梯度，导致近似偏向当前任务、记旧能力有限。作者的洞察是：在学习 $T_1$ 时，梯度下降最终收敛到 $\theta^*_1=\arg\min_\theta L(\theta;T_1)$，因此**「指向 $\theta^*_1$ 的方向」在某种程度上反映了整个优化轨迹的期望梯度方向**。据此，学习 $T_2$ 时用 $\theta-\theta^*_1$ 近似 $\nabla L(\theta;T_1)$。但纯方向向量幅值可能过大，于是用当前任务梯度幅值做**尺度归一**：
$$\hat g=\begin{cases}\dfrac{\theta-\theta^*_{1:t-1}}{\|\theta-\theta^*_{1:t-1}\|}\cdot\|\nabla L(\theta;T_t)\|, & \text{若 }\|\theta-\theta^*_{1:t-1}\|>\|\nabla L(\theta;T_t)\|\\[2mm] \theta-\theta^*_{1:t-1}, & \text{否则}\end{cases}$$
即只有当方向向量范数超过当前梯度范数时才缩放到与之匹配，否则直接用原向量。对 $t\ge 2$ 的后续任务，把所有旧任务视为一个联合任务，用持续累计的最优参数 $\theta^*_{1:t-1}$ 计算 $\hat g$。这一设计的关键是**用参数空间几何（到旧最优的位移）替代不可得的旧数据梯度**，无需保存旧任务完整数据。

**2. 与重放缓冲融合：方向近似 + 真实梯度互补，按分布差异自动分工**

$\hat g$ 是几何近似、重放梯度 $\nabla L(\theta;M)$ 是真实但稀疏的采样，二者互补：
$$\nabla L(\theta;T_1)\approx \hat g+\nabla L(\theta;M),\qquad \nabla L(\theta;\textstyle\bigcup_{i=1}^t T_i)\approx \hat g+\nabla L(\theta;T_t\cup M).$$
有意思的是两者的相对重要性**随数据分布差异自动切换**：实验发现，在同域的 VQAv2（10 个子任务都来自同一视觉域）上 $\hat g$ 占主导，仅靠 $\hat g$ 无重放就能达到 64.61% FAA、超过最强 baseline；而在跨 6 个差异巨大数据集的 UCIT 上重放更重要，仅靠 $\hat g$（53.71%）反不如仅靠重放（57.13%）。作者解释：分布偏移大时，「到旧最优的方向」与真实旧梯度的吻合度下降，$\hat g$ 近似精度受损，从而更依赖重放——但 $\hat g$ 仍保留有价值的梯度信息（UCIT 上二者结合后大幅提升）。

**3. 伯努利采样的动态梯度更新：随机调控 $\hat g$ 注入频率，平衡稳定性与可塑性**

把 $\hat g$ 每步都注入会让模型过度偏向旧任务、削弱学新能力（可塑性）。作者引入参数为 $\alpha$ 的伯努利随机变量 $B(\alpha)$，每个优化步采样一次决定是否注入旧任务梯度：
$$\nabla L\big(\theta;\textstyle\bigcup_{i=1}^t T_i\big)=\begin{cases}\hat g+\nabla L(\theta;T_t\cup M), & B(\alpha)=1\\ \nabla L(\theta;T_t\cup M), & B(\alpha)=0\end{cases}$$
$\alpha$ 直接控制「记旧 vs 学新」的天平：$\alpha$ 越大、$\hat g$ 注入越频繁、旧任务精度越高但新任务精度下降。这种随机注入既模拟了 mini-batch 梯度下降固有的随机性，又避免模型过拟合到旧知识。算法实现极简（Algorithm 1）：采样到 1 时遍历各参数、对有梯度的参数加上（缩放后的）方向向量即可。

### 损失函数 / 训练策略
基座 LLaVA-7B + LoRA 指令微调。VQAv2：LoRA rank 128，每任务缓存 0.5k 重放样本，全程 $\alpha=0.2$；任务序列为 Recognition→Location→Judge→Commonsense→Count→Action→Color→Type→Subcategory→Causal。UCIT：LoRA rank 48，每任务缓存 2k 重放样本，按任务设置 $\alpha$（ArxivQA 0.1 / VizWiz 0.1 / IconQA 0.05 / CLEVR 0.05 / Flickr30k 0.1）。

## 实验关键数据

### 主实验
两个 MCIT 数据集，指标为**最终平均准确率 FAA**（按各任务实际测试样本数加权，$\text{FAA}=\sum_i \frac{|T_i|}{|T_{1:T}|}a^T_i$，其中 $a^T_i$ 是学完最后任务后第 $i$ 个任务的准确率）。MultiTask（联合训练）为性能上界，所有 baseline 用 MCITlib 框架评测。

| 数据集 | MultiTask（上界） | 最强 baseline | DGG（本文） | 较最强 baseline |
|--------|-------------------|----------------|--------------|------------------|
| VQAv2（10 子任务，同域） | 66.26 | SEFE 63.57 | **65.17** | +1.60 |
| UCIT（6 数据集，强分布偏移） | 74.78 | DISCO 69.66 | **73.82** | +4.16 |

DGG 与上界差距极小（VQAv2 仅 1.09、UCIT 仅 0.96），且在 Recognition (55.55)、Commonsense (76.12)、Type (61.19) 等子任务上甚至超过 MultiTask 上界；尤为关键的是**多数 baseline 用 MoE 扩展模型，而 DGG 完全不扩展**，在优化层面解决问题。

### 消融实验
拆解两个核心操作（梯度缩放、伯努利采样），数据为 FAA（%）。⚠️ 注意：VQAv2 上的后续消融均采用 $\hat g$-only 设定（不含重放 $M$），故下表 VQAv2 完整值为 64.61 而非主表的 65.17。

| 配置 | VQAv2 | UCIT | 说明 |
|------|-------|------|------|
| 完整（缩放 + 伯努利） | 64.61 | 73.82 | full（VQAv2 为 ĝ-only） |
| 去梯度缩放 | 64.01（↓0.60） | 65.24（↓8.58） | 直接用未缩放方向向量 |
| 去伯努利采样 | 62.75（↓1.86） | 59.02（↓14.80） | 每步都注入 $\hat g$ |

另有梯度近似消融（原文 Figure 3）：VQAv2 上 $\hat g$-only 即达 64.61、远超 M-only（1k 样本仅 57.73）；UCIT 上 M-only（0.5k）57.13 反超 $\hat g$-only 53.71。

### 关键发现
- **伯努利采样比梯度缩放更关键**：去掉伯努利在 UCIT 上掉 14.80、VQAv2 掉 1.86，均大于去缩放的影响——随机调控注入频率对避免「过度记旧」至关重要。
- **两个操作在强分布偏移场景影响更大**：UCIT（跨域）上去缩放掉 8.58、去伯努利掉 14.80，远高于同域 VQAv2 的 0.60 / 1.86，说明分布差异越大、对精细梯度调控越敏感。
- **$\hat g$ 与重放的主次随分布切换**：同域看 $\hat g$、跨域看重放，且二者结合总优于单用，验证了「几何近似 + 真实采样互补」的设计动机。
- **$\alpha$ 调节可塑性—稳定性**：$\alpha$ 增大时旧任务精度升、新任务精度降；VQAv2 上 $\alpha=0.2$、UCIT 上 $\alpha=0.05$ 附近 FAA 最优，过小的 $\alpha$ 会一致地损害旧任务稳定性。

## 亮点与洞察
- **「遗忘 = 缺失梯度」的重述很提神**：把灾难性遗忘从「权重被覆盖」的模糊叙事，精确化为「联合梯度里缺了 $\nabla L(\theta;T_1)$ 这一可加项」，于是问题自然转成「如何近似这一项」，方法与诊断一一对应。
- **用参数空间几何代替不可得的数据梯度**：方向向量 $\theta-\theta^*_{1:t-1}$ 把「到旧最优的位移」当作「旧梯度期望方向」的代理，只需保存旧任务最优参数（而非数据），存储成本极低，且与重放天然互补。
- **不扩展模型却逼近联合上界**：在 MoE 当道的 MCIT 领域，DGG 证明纯优化层面的梯度调控就能把与 MultiTask 上界的差距压到 ~1%，对部署友好（无推理期膨胀），这一「优化级而非架构级」思路可迁移到其他持续学习任务。

## 局限与展望
- **依赖「旧任务最优参数」的可得性与代表性**：$\hat g$ 的质量取决于 $\theta^*_{1:t-1}$ 是否真为旧任务最优；若旧任务本身欠拟合或最优解漂移，方向近似会失真。强分布偏移（UCIT）下 $\hat g$ 精度明显下降即是佐证。
- **超参 $\alpha$ 需按任务调**：UCIT 上不同任务用了不同 $\alpha$（0.05~0.1），且敏感性分析显示 $\alpha$ 影响显著，跨数据集迁移可能需要重新搜参。
- **仍需重放缓冲**：跨域场景下重放是主力（UCIT 每任务存 2k 样本），并非完全免存储；隐私/存储受限场景下可用性待验证。
- 仅在 LLaVA-7B + LoRA、两个 MCIT 数据集上验证，对更大模型、更长任务序列或全参微调的可扩展性尚未给出。

## 相关工作与启发
- **vs MoE 类（CL-MoE / HiDE / DISCO）**：它们用专家/路由学任务专属知识，记忆强但**扩展模型**、训练推理都增开销；DGG 不加任何组件，在优化层面解决遗忘，架构保持紧凑。
- **vs 正则化类（SEFE / RegLoRA）**：SEFE 用静态正则约束关键权重更新；DGG 的梯度引导可视作一种**动态正则项**，随训练过程调整、并能与重放融合，适应演化的优化地形。
- **vs 纯重放（replay-based）**：纯重放受缓冲规模限制、近似有偏向当前任务；DGG 用 $\hat g$ 补上几何方向信息，在同域场景甚至无需重放即超过最强 baseline。

## 评分
- 新颖性: ⭐⭐⭐⭐ 「遗忘=缺失梯度」重述 + 参数空间方向向量近似旧梯度，视角新且落地简洁
- 实验充分度: ⭐⭐⭐⭐ 两数据集、组件/缓冲/序列/超参多维消融充分，但任务序列与基座规模仍有限
- 写作质量: ⭐⭐⭐⭐ 从梯度可加性推导到近似与调控逻辑清晰，Figure 1/2 直观
- 价值: ⭐⭐⭐⭐ 提供不扩展模型即逼近联合上界的优化级 MCIT 方案，部署友好、开源可复现

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Towards Dynamic Modality Alignment in Multimodal Continual Learning](towards_dynamic_modality_alignment_in_multimodal_continual_learning.md)
- [\[CVPR 2026\] Harmonious Parameter Adaptation in Continual Visual Instruction Tuning for Safety-Aligned MLLMs](harmonious_parameter_adaptation_in_continual_visual_instruction_tuning_for_safet.md)
- [\[ACL 2025\] Enhancing Multimodal Continual Instruction Tuning with BranchLoRA](../../ACL2025/multimodal_vlm/branchlora_continual_instruction.md)
- [\[CVPR 2026\] Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models](octopus_history-free_gradient_orthogonalization_for_continual_learning_in_multim.md)
- [\[ICML 2025\] Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](../../ICML2025/multimodal_vlm/dynamic_mixture_of_curriculum_lora_experts_for_continual_multimodal_instruction_.md)

</div>

<!-- RELATED:END -->
