---
title: >-
  [论文解读] PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs
description: >-
  [CVPR 2026][多模态VLM][Video LLM] PAS 把 Video LLM 时间编码的不稳定诊断成"对一条带高频纹波的逆傅里叶时间核采样"，提出免训练的多头反相相位平滑——给不同注意力头的 query 加上小幅相反的时间相位偏移再正常聚合，相当于做一次受控滑动平均把纹波抹平，在九个视频基准上稳定涨点且几乎零额外开销。
tags:
  - "CVPR 2026"
  - "多模态VLM"
  - "Video LLM"
  - "M-RoPE"
  - "时间编码"
  - "相位平滑"
  - "免训练"
---

# PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs

**会议**: CVPR 2026  
**论文**: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_PAS_A_Training-Free_Stabilizer_for_Temporal_Encoding_in_Video_LLMs_CVPR_2026_paper.html)  
**代码**: https://github.com/Bowen-Sun-0728/PAS  
**领域**: 多模态VLM / 视频理解  
**关键词**: Video LLM, M-RoPE, 时间编码, 相位平滑, 免训练

## 一句话总结
PAS 把 Video LLM 时间编码的不稳定诊断成"对一条带高频纹波的逆傅里叶时间核采样"，提出免训练的多头反相相位平滑——给不同注意力头的 query 加上小幅相反的时间相位偏移再正常聚合，相当于做一次受控滑动平均把纹波抹平，在九个视频基准上稳定涨点且几乎零额外开销。

## 研究背景与动机

**领域现状**：Video LLM 普遍把为文本设计的旋转位置编码 RoPE 推广成多模态版本 M-RoPE，沿时间轴 T、高 H、宽 W 三个维度各分配一组频率线给视频 token 编码位置。

**现有痛点**：作者观察到一个反直觉的脆弱性——帧采样的微小变化（帧率、采样偏移）会翻转注意力分布，让本该被关注的关键帧被抑制、不相关帧反而被放大，进而传播成下游错误（论文 Figure 1 给了真实失败例）。这不是随机噪声，而是时间编码本身的结构性问题。

**核心矛盾**：沿时间轴的 M-RoPE 等价于给一组固定时间频率线，每条线对注意力 logit 贡献一个周期项。把这些线做逆傅里叶变换得到的时间核 $m(\Delta t)$ 在"帧尺度"上天然带纹波（这是频谱本身的性质，不是稀疏采样的副作用）。纹波意味着相邻帧被乘上差异很大的调制因子，于是注意力到底由"内容相似度"还是"恰好落在哪个时间间隔"主导，变得不可控。

**本文目标**：在不重训、不改 token 预算、不改位置编码结构的前提下，把这条时间核抹平，让注意力重新回到内容主导、对小幅时间扰动稳健。

**切入角度**：既然问题是"在略有差异的时滞处采样同一条带纹波的核"，那自然的解法就是"对邻近时滞做平均"——这正是信号处理里滑动平均滤波器抑制高频纹波的思路。

**核心 idea**：给不同注意力头的 query 施加小幅、相反的时间相位偏移，让每个头观察到该核在略微平移后的版本；标准的多头聚合就充当了一次"时间上的滑动平均"，抹平高频纹波而保留低频趋势。

## 方法详解

### 整体框架
PAS（Phase Aggregated Smoothing）是一个推理期插件，核心是先用傅里叶视角把问题讲清，再用一个极简机制把核抹平。整条逻辑链是：**M-RoPE 旋转后的注意力 logit ≈ 内容内积 × 时间核 $\mathrm{Re}\{m(\Delta t)\}$（相位调制视角）→ 核越平滑、注意力对时滞越稳（Lipschitz 稳定性）→ 给各头分配相反的小相位偏移再聚合 = 对核做受控滑动平均（抹平纹波）→ 只要满足 Nyquist，每个头的可恢复频谱在时移下不变（只改"怎么采样"，不改"编了什么")**。

具体到一次前向：在每个注意力层算出标准的 Q/K/V 之后，把 query 头按 K 个相位组划分，给第 $h$ 组的 query 在**时间半维**上施加一个温和的相位算子 $\Gamma_{\delta_h}$（仅作用于视频 token，空间维不动），随后照常做多头注意力与聚合。整个方法不引入新参数、不改 tokenization、不增加 token，作者实测吞吐 $(76.8\pm4.0)\times10^3$ tokens/s 与原始 backbone 的 $(77.2\pm3.1)\times10^3$ 在方差内无法区分。

> 本方法是"单一机制 + 理论分析"，不是多阶段串行 pipeline，核心在频域的矩阵/相位运算，用框架图反而画不清，故不配流程图，用公式说明。

### 关键设计

**1. 相位调制视角：把时间不稳定性诊断成"对一条带纹波的时间核采样"**

这是全文的诊断基石，也是后续机制能成立的前提。RoPE 在每个二维子空间用相位 $e^{j\omega_i s}$ 旋转 query/key，定义内容项 $C_i:=z_i w_i^*$（与位移无关），则旋转后的 logit 只依赖相对位移 $\Delta$：$\langle\tilde q,\tilde k\rangle(\Delta)=\mathrm{Re}\big[\sum_i C_i e^{j\omega_i\Delta}\big]$。作者证明（Theorem 1）当频率线数 $m$ 大、各线能量近似均匀时，这个和会向其平均模式集中，于是 logit 可近似分离成"纯内容内积"乘一个标量时间核：

$$\langle\tilde q,\tilde k\rangle(\Delta)\approx\langle q,k\rangle\cdot\mathrm{Re}\{m(\Delta)\},\qquad m(\Delta):=\tfrac{1}{m}\sum_{i=0}^{m-1}e^{j\omega_i\Delta}.$$

关键洞察在于 $m(\Delta)$ 是一堆余弦的平均，在帧尺度上**内禀地带纹波**——所以微小的时滞变化 $\delta t$ 就能让调制因子大幅摆动，把内容主导的注意力扭成"时机主导"。这一步把一个含糊的"Video LLM 对采样敏感"现象，精确刻画成"对一条不平滑的核采样"，从而把解法指向"抹平核"。

**2. 多头反相相位平滑：用受控滑动平均抹平纹波**

针对设计 1 暴露的纹波，PAS 不去改频谱，而是借多头聚合做"邻近时滞平均"。给 $H$ 个头分配小幅时移 $\{\delta_h\}$ 和归一化权重 $\{a_h\}$（$\sum_h a_h=1$），聚合后的有效调制为 $m_{\mathrm{eff}}(\Delta t)=\sum_h a_h\, m(\Delta t+\delta_h)$。作者证明（Theorem 3）这个加权平均的均方局部变差不超过原核，即 $V_\varepsilon(m_{\mathrm{eff}})\le V_\varepsilon(m)$，且只要相位不全相同就严格更小；在频域上等价于把线谱乘以聚合核 $K(\omega)=\sum_h a_h e^{j\omega\alpha\delta_h}$，其模 $|K(\omega)|\le1$，当各头相位足够分散时对非零频率严格衰减——也就是高频纹波被压、低频趋势被留。

配合 Theorem 2 的 Lipschitz 稳定性（核越平滑、logit 随 $\delta t$ 至多线性变化：$|A(\Delta t+\delta t)-A(\Delta t)|\le|\langle q,k\rangle|\,L_m|\delta t|$，$L_m$ 是核的最大局部斜率），整条因果链闭合：**多相位平均 ⇒ 更平滑的 $m_{\mathrm{eff}}$ ⇒ 注意力对相位更稳**。"相反/对称"的偏移设计正是为了让相位充分分散、把 $|K(\omega)|$ 压到最低。

**3. 只动 Query 的时间半维 + Nyquist 保真：保证"只改采样方式，不改编码内容"**

一个自然的担忧是：加相位偏移会不会破坏 RoPE 本来编的位置语义？作者用傅里叶的基本事实回答——时移只改相位、不改幅度谱。Theorem 4 证明：在固定窗、满足 Nyquist 带限的前提下，给某个头加时移 $\delta$ 后，其 $N$ 点 DFT 只被逐 bin 的相位因子 $e^{j\theta_k(\delta)}$ 调制，幅度 $|X_\delta[k]|=|X[k]|$ 完全不变；同时只要 $\delta_{\max}-\delta_{\min}\le\Delta$，各头之间的帧/bin 离散顺序也不会被打乱。因此平滑只在"标准多头聚合之后"才涌现，每个头自己编的频谱原封不动。

工程上这条设计落成三点约束：$\Gamma_\delta$ 只作用于**时间半维**（空间编码完全不碰）；只对**视频 token**生效（右对齐 mask 锁定 video span）；hook 点放在 base 位置编码施加到 Q 之后，且兼容 MHA/GQA（沿每头维度广播偏移）。开销上 PAS 只在 Q 的时间半维做一次逐 token 线性变换，额外代价 $C_{\mathrm{PAS}}/C_{\mathrm{attn}}\le p_t S_v/S^2$（$p_t$ 为受影响半维占比），在 $S$ 数百到数千时基本可忽略。

### 损失函数 / 训练策略
PAS 是**免训练**的推理期插件，没有任何训练目标或微调。唯一的"超参"是相位组数 $K$ 与各组偏移 $\{\delta_h\}$（以 bin 为单位，$\phi=1.0$ 等于平移一个 bin）。论文给的默认配置极简：$K=2$，两组偏移取 $[0,0.5]$，对所有 backbone 直接即插即用。

## 实验关键数据

> 自定义口径：**bin** 指采样器+合并器产出的一个视频 token（沿时间把一桶相邻帧合并）；**matched token budget** 指所有方法每段视频的视频 token 总数对齐，确保涨点来自机制而非更多 token。Acc 为分类准确率，Macro-F1 为类别宏平均 F1。

### 主实验
backbone 为 Qwen2.5-VL-7B-Instruct，与两个免训练基线 SlowFast-LLaVA、TS-LLaVA 在对齐 token 预算下比较，并测 PAS 叠加在它们之上的效果。

| 数据集 / 指标 | Default backbone | SlowFast-LLaVA | TS-LLaVA | PAS (本文) | SlowFast+PAS |
|--------------|------------------|----------------|----------|-----------|--------------|
| 20BN-Jester (Acc) | 16.0 | 14.9 | 15.4 | 18.3 | **19.6** |
| Kinetics-700 (Acc) | 44.9 | 45.1 | 44.7 | 48.2 | **49.8** |
| MVBench (Acc) | 67.2 | 69.2 | 67.8 | 69.5 | **71.0** |
| TempCompass (Overall) | 71.5 | 73.5 | 71.4 | 73.3 | **73.9** |
| EgoSchema (Acc) | 63.5 | 63.6 | 65.8 (TS) | 63.9 | 64.1 |
| MMBench-Video (0–3) | 1.71 | 1.76 | 1.70 | 1.78 | **1.81** |

PAS 单独使用即在动作识别（相位敏感）类基准上稳定优于 backbone，并在 20BN-Jester、Kinetics-700 取得单模型最佳；叠加到 SlowFast-LLaVA / TS-LLaVA 上能进一步把上限抬高，说明它与多速率、缩略图等正交方案可叠乘。

### 消融 / 分析实验
PAS 没有可去除的"模块"，作者的核心验证来自参数扫描与采样率消融——它们直接检验"涨点是否真的来自抹平时间核"。

| 分析维度 | 设置 | 关键发现 |
|---------|------|---------|
| 偏移幅度 $\Delta$（$K{=}2$） | 扫 $0.0\!\to\!1.0$ | 三个运动密集集在 $\Delta\in[0.3,0.8]$ 稳定显著涨点，存在宽平台；$\Delta{\approx}0.5$ 为跨数据集稳妥默认 |
| 采样率 $r$ | 采样帧/总帧 $\in[0,1]$ | $r$ 越低（稀疏采样）增益越大，$r$ 高时与 backbone 统计上无法区分——符合 Theorem 2 |
| Nyquist 与否 | Breakfast 子采样（sub-Nyquist） | 欠采样下混叠限制收益，提升窗口更窄、绝对增益更小——符合 Theorem 4 |
| 推理开销 | A100 80G, matched seq | $(76.8\pm4.0)$ vs $(77.2\pm3.1)\times10^3$ tokens/s，统计上无差别 |

### 关键发现
- 增益最大处恰在**稀疏采样 / 低帧率**场景——此时时间核被稀疏地探到、相邻 bin 的相位差大、纹波最伤注意力，正是 PAS 滑动平均最能补的地方；采样越密，核被天然平滑，PAS 余地越小。
- 偏移幅度存在**宽平台**（0.3–0.8 都好），说明方法对超参不敏感、无需逐数据集调参，$K=2$+$[0,0.5]$ 是可直接复用的默认。
- 三条定理与三组实验（偏移扫描、采样率、Nyquist）一一呼应，是少见的"理论预测—实验验证"严丝合缝的工作。

## 亮点与洞察
- **把一个工程现象升格成可证明的频域问题**：从"Video LLM 对采样敏感"到"对一条带纹波的逆傅里叶核采样"，再到三条定理串成的稳定性保证，诊断与解法逻辑闭环，读完很有"啊哈"感。
- **零成本即插即用**：不重训、不改 token、不动空间编码，只在 Q 的时间半维加相位再正常聚合，吞吐几乎不变——这种"白嫖式"鲁棒性升级对落地极友好。
- **可迁移的思路**：把"多头聚合"重新解释成"对位置核的滑动平均"这一视角，可能迁移到其它用 RoPE/相对位置编码的长序列或多模态场景，凡是位置核带纹波的地方都可借相位多样化来稳。

## 局限与展望
- **依赖 Nyquist 假设**：理论保证（频谱不变、只改采样）建立在时间采样满足 Nyquist 带限上；一旦严重欠采样（sub-Nyquist，如 Breakfast 子采样），分数延迟不再是全通、保证失效，收益也被混叠吃掉。
- **增益场景有偏**：方法在稀疏采样/低帧率下收益最大，密集采样时与 backbone 无统计差异——意味着对已经高帧率、强时序建模的设置帮助有限。
- **验证集中在 7B + Qwen2.5-VL**：主实验只在单一 backbone 上做，跨模型规模、跨不同 M-RoPE 频率分配方案的普适性还需更多验证（⚠️ 论文未给跨 backbone 的大规模结果）。
- 改进方向：自适应地按估计的局部核斜率 $L_m$ 决定偏移幅度与组数，而非固定 $K{=}2,\Delta{=}0.5$，或与采样率联合优化。

## 相关工作与启发
- **vs SlowFast-LLaVA / TS-LLaVA**: 它们用双路（慢/快）或缩略图+轻采样在输入侧扩大时间覆盖来抗稀疏采样；PAS 不改输入、不加 token，而是在注意力内部用单次前向覆盖多个时间相位。两者正交，可叠加（表中 SlowFast+PAS 进一步涨点）。
- **vs 推理期多遍重采样策略**: 传统做法靠对多个重采样偏移做预测平均来稳，但成倍增加延迟；PAS 把"多相位覆盖"压进单次前向的多头里，几乎零额外开销。
- **vs 视觉特定的 2D/3D RoPE 设计**: 那条线关注轴耦合与频率分配的表达力；PAS 聚焦绝对时间编码的**鲁棒性**，从傅里叶/相位稳定性角度切入，问题定位不同。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 把多头聚合重释为对位置核的滑动平均、并用三条定理严格支撑，视角与解法都很新。
- 实验充分度: ⭐⭐⭐⭐ 九基准 + 偏移/采样率消融与理论一一对应，但只在单一 7B backbone 上验证，跨模型普适性证据偏少。
- 写作质量: ⭐⭐⭐⭐⭐ 诊断—理论—机制—实验逻辑链清晰，定理与实验呼应紧密。
- 价值: ⭐⭐⭐⭐ 免训练、零开销、即插即用，对低帧率/稀疏采样的 Video LLM 落地价值高，但密集采样场景收益有限。

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[CVPR 2026\] Pointing at Parts: Training-Free Few-Shot Grounding in Multimodal LLMs](pointing_at_parts_training-free_few-shot_grounding_in_multimodal_llms.md)
- [\[CVPR 2026\] TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs](timelens_rethinking_video_temporal_grounding_with_multimodal_llms.md)
- [\[CVPR 2026\] STiTch: Semantic Transition and Transportation in Collaboration for Training-Free Zero-Shot Composed Image Retrieval](stitch_semantic_transition_and_transportation_in_collaboration_for_training-free.md)
- [\[CVPR 2026\] DRS-GUI: Dynamic Region Search for Training-Free GUI Grounding](drs-gui_dynamic_region_search_for_training-free_gui_grounding.md)
- [\[NeurIPS 2025\] Training-free Online Video Step Grounding](../../NeurIPS2025/multimodal_vlm/training-free_online_video_step_grounding.md)

</div>

<!-- RELATED:END -->
