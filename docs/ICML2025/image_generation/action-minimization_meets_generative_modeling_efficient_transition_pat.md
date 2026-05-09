---
title: >-
  [论文解读] Action-Minimization Meets Generative Modeling: Efficient Transition Path Sampling with the Onsager-Machlup Functional
description: >-
  [ICML 2025][图像生成][transition path sampling] 将预训练扩散/flow matching模型的score函数解释为随机动力学的漂移项，通过最小化Onsager-Machlup (OM)作用量泛函实现零样本转移路径采样，无需任务特定训练即可在分子系统上高效生成多样且物理真实的转移路径。
tags:
  - ICML 2025
  - 图像生成
  - transition path sampling
  - Onsager-Machlup
  - 扩散模型
  - flow matching
  - molecular dynamics
  - score function
  - zero-shot
---

# Action-Minimization Meets Generative Modeling: Efficient Transition Path Sampling with the Onsager-Machlup Functional

**会议**: ICML 2025  
**arXiv**: [2504.18506](https://arxiv.org/abs/2504.18506)  
**代码**: 无  
**领域**: 科学计算/分子模拟/生成模型  
**关键词**: transition path sampling, Onsager-Machlup, diffusion models, flow matching, molecular dynamics, score function, zero-shot  

## 一句话总结

将预训练扩散/flow matching模型的score函数解释为随机动力学的漂移项，通过最小化Onsager-Machlup (OM)作用量泛函实现零样本转移路径采样，无需任务特定训练即可在分子系统上高效生成多样且物理真实的转移路径。

## 研究背景与动机

转移路径采样（Transition Path Sampling, TPS）是统计力学中的核心挑战：给定能量景观上的两个稳定构型（如蛋白质折叠的起始与终止态），寻找连接它们的高概率路径。其难点在于能量壁垒造成稀有事件与系统最快动力学运动之间的时间尺度差异巨大。

现有ML方法的局限性：
- 传统方法（伞形采样、metadynamics）依赖手工定义的集体变量（CV），在过渡态附近定义合适的CV非常困难
- 打靶法（shooting method）采样慢、拒绝率高、需要昂贵的MD模拟
- 现有ML方法（强化学习、可微模拟、h-transform学习）需要针对每个新系统重新进行昂贵的训练，无法利用大规模预训练模型和已有数据

核心洞察：原子级生成模型（扩散模型、flow matching）可以生成无偏的独立构型样本，但由于训练时使用的是不相关的状态，尚未被直接用于TPS。本文发现，这些模型的学习score函数天然诱导了一组随机朗之万动力学，可以通过OM作用量来评估路径概率——这提供了一种优雅的"后训练"方法来复用生成模型进行TPS。

## 方法详解

### 整体框架

方法分三步：
1. **初始路径猜测**：在生成模型的潜在空间level $\tau_{\text{initial}}$ 进行线性插值（而非在配置空间直线插值，因为物理构型在高度非凸的低维流形上）
2. **OM作用量优化**：固定端点，通过梯度下降最小化离散化OM作用量，整条轨迹并行优化
3. **解码**（可选）：若在潜在空间优化，则通过去噪过程解码回配置空间

关键优势：模型参数 $\theta^*$ 在整个优化过程中完全冻结，无需任何微调或重训练。

### 关键设计1：从生成模型到随机动力学的桥梁

核心理论贡献是建立了预训练生成模型的score函数与Onsager-Machlup路径概率之间的联系。对于满足常方差SDE的动力学：

$$d\mathbf{x} = \frac{1}{\zeta}\mathbf{\Phi}(\mathbf{x})dt + \sqrt{2D}\,d\mathbf{W}_t$$

路径概率可用OM作用量的指数形式表达：$P(\mathbf{x}(\cdot)) \propto e^{-S[\mathbf{x}(\cdot)]}$。离散化OM作用量包含三项：

$$S = \frac{1}{2D}\sum_{i=0}^{L-1}\left[\underbrace{\frac{1}{2\Delta t}\|\mathbf{x}^{(i+1)}-\mathbf{x}^{(i)}\|^2}_{A:\text{平滑性}} + \underbrace{\frac{\Delta t}{2\zeta^2}\|\mathbf{\Phi}(\mathbf{x}^{(i)})\|^2}_{B:\text{低漂移范数}} + \underbrace{\frac{D\Delta t}{\zeta}\nabla\cdot\mathbf{\Phi}(\mathbf{x}^{(i)})}_{C:\text{凸性/稳定性}}\right]$$

- **项A**鼓励路径点之间平滑过渡
- **项B**鼓励路径经过低漂移范数区域（平衡点或鞍点）
- **项C**鼓励路径处于漂移散度低的区域（能量景观凸区域，动力学更稳定）

对于扩散模型，通过迭代去噪-加噪过程构造代理SDE，在连续极限下得到：

$$d\mathbf{x} = \mathbf{s}_\theta(\mathbf{x}, \tau)dt + \sqrt{2}\,d\mathbf{W}_t$$

其中 $\mathbf{s}_\theta \approx \nabla \log p_\tau(\mathbf{x})$ 即学习到的score函数。当数据服从Boltzmann分布时，score直接对应原子力场：$\mathbf{s}_{\theta^*}(\mathbf{x}, \tau=0) \approx -\nabla U(\mathbf{x}) / (k_BT)$。

### 关键设计2：扩展到Flow Matching

对于flow matching模型，推导了从学习的速度场 $u_{\theta^*}$ 提取score的公式：

$$\mathbf{s}_\theta^{\mathrm{FM}}(\mathbf{x}, \tau) = \frac{\alpha_\tau}{\dot{\sigma}_\tau \sigma_\tau \alpha_\tau - \dot{\alpha}_\tau \sigma_\tau^2}\left(\frac{\dot{\alpha}_\tau}{\alpha_\tau}\mathbf{x} - u_{\theta^*}(\mathbf{x}, \tau)\right)$$

其中 $\alpha_\tau, \sigma_\tau$ 定义了flow的插值曲线。这使得OM优化框架可以直接复用任意flow matching模型，大幅扩展了方法的适用范围。

### 关键设计3：散度项的高效计算

OM作用量中的散度项 $\nabla \cdot \mathbf{s}_\theta$ 计算代价高（需对每个维度求导），作者使用Hutchinson估计器进行无偏近似，避免了逐维度计算的开销。在低扩散系数 $D$ 的极限下，散度项可忽略，得到截断OM作用量。

## 实验关键数据

### 表1：丙氨酸二肽上OM优化与传统方法的效率对比

| 方法 | 是否需要CV | 力场评估次数/路径 | 运行时间/路径 |
|------|-----------|------------------|-------------|
| MCMC (Two-Way Shooting) | 否 | ≥ 1B | ≥ 100小时 |
| Metadynamics | 是 | 1M | 10小时 |
| **OM Opt. (扩散模型, 本文)** | **否** | **10K** | **50分钟** |

OM优化比传统打靶法减少了约5个数量级的力场/score函数评估次数。

### 表2：快速折叠蛋白的MSM评估（5种蛋白平均，扩散+flow matching）

| 指标 | OM优化 | 无偏MD (1μs) | 无偏MD (50μs) | 无偏MD (100μs) |
|------|--------|-------------|--------------|---------------|
| 有效路径比例 ↑ | **最高** | 低 | 中 | 中高 |
| 转移负对数似然 ↓ | **最低** | 高 | 中高 | 中 |
| Jensen-Shannon散度 ↓ | 与50μs MD相当 | 高 | 中 | **最低** |

OM优化在有效路径比例和转移似然两个指标上超过所有长度的无偏MD模拟（最长100μs），JSD与50μs MD持平。

### 四肽泛化实验

在100个训练中未见过的四肽序列上，OM优化的MSM指标与50-100ns MD模拟相当，计算成本却低得多，表明方法具有零样本泛化能力。

## 关键发现

1. **零样本TPS可行**：预训练生成模型无需任何TPS特定训练即可用于路径采样，且产生物理真实路径
2. **效率优势显著**：丙氨酸二肽上比metadynamics减少100倍评估次数，比打靶法减少10万倍
3. **温度可调**：通过改变扩散系数 $D$（与温度成正比），可控制路径穿越的能量壁垒高度——高温路径穿越更高壁垒
4. **对稀疏数据鲁棒**：即使去除99%的过渡态数据重训模型，OM优化仍能采样合理路径
5. **反应速率估计**：Müller-Brown势上估计反应速率 $1.3\times10^{-5}$，真值 $5.4\times10^{-5}$，数量级正确
6. **flow matching同样适用**：推导了从flow matching提取score的通用公式，验证了方法的模型无关性

## 亮点与洞察

- **理论优雅**：OM泛函作为随机力学中最小作用量原理的随机版本，将经典物理直觉与现代生成模型自然连接。三项分解（平滑性+低漂移+凸性）提供了清晰的物理解释
- **范式转变**：从"为每个任务训练专用模型"转向"复用大规模预训练模型"，与NLP/CV领域的发展趋势一致。随着原子级生成模型持续scaling，OM-TPS的价值将同步增长
- **去噪-加噪作为SDE**：迭代去噪-加噪过程（而非标准去噪采样过程）才是正确的代理SDE，这个洞察是非平凡的——标准去噪过程在不同时间步优化不同的似然
- **路径多样性免费获取**：通过随机编码/解码过程自然产生多样路径，无需额外采样策略

## 局限性

1. **不保证完整后验采样**：无法证明采样了路径的完整后验分布（传统打靶法和h-transform方法可以）
2. **依赖score质量**：方法的物理真实性取决于预训练模型的score估计精度，对训练数据覆盖不足的区域可能不准确
3. **仅验证了较小系统**：最大实验为四肽（约80个原子），对蛋白质折叠等大规模系统的有效性尚未验证
4. **离散化误差**：OM作用量使用离散化形式，路径分辨率受限于离散步数 $L$
5. **物理参数选择**：$\tau_{\text{opt}}$、$\Delta t$、$D$ 等超参数需要针对不同系统调整

## 相关工作与启发

- **Arts et al. (2023)**: 首次建立扩散模型与力场的联系（score≈force），本文在此基础上进一步构建了路径概率的完整框架
- **Jing et al. (2024b)**: 直接在轨迹上学习生成模型（DiffTraj），是complementary的方法——DiffTraj学习轨迹分布，OM-TPS复用构型分布模型
- **Du et al. (2024)**: h-transform学习方法可证明采样后验，但需要任务特定训练
- **启发**：OM作用量优化可推广到非物理领域（图像、视频、音频）作为通用的流形插值机制

## 评分

| 维度 | 分数 | 说明 |
|------|------|------|
| 新颖性 | 9/10 | 首次将OM泛函与生成模型score系统连接，实现零样本TPS |
| 理论深度 | 9/10 | 从SDE到OM作用量到score函数的推导链完整优雅 |
| 实验充分度 | 7/10 | 覆盖2D势、丙氨酸二肽、快速折叠蛋白、四肽，但系统规模偏小 |
| 实用价值 | 8/10 | 随着预训练模型scaling可直接受益，但大系统验证仍需 |
| 写作质量 | 8/10 | 结构清晰，物理直觉与数学推导平衡良好 |
| **总分** | **8/10** | 理论深刻且实用前景明确的工作，是生成模型与物理模拟交叉方向的重要进展 |

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] ETTA: Elucidating the Design Space of Text-to-Audio Models](etta_elucidating_the_design_space_of_text-to-audio_models.md)
- [\[ICML 2025\] Generative Audio Language Modeling with Continuous-Valued Tokens and Masked Next-Token Prediction](generative_audio_language_modeling_with_continuous-valued_tokens_and_masked_next.md)
- [\[ICML 2025\] DDIS: When Model Knowledge Meets Diffusion Model — Diffusion-assisted Data-free Image Synthesis](when_model_knowledge_meets_diffusion_model_diffusion-assisted_data-free_image_sy.md)
- [\[ICML 2025\] IMPACT: Iterative Mask-based Parallel Decoding for Text-to-Audio Generation with Diffusion Modeling](impact_iterative_mask-based_parallel_decoding_for_text-to-audio_generation.md)
- [\[ICML 2025\] Zero-Shot Adaptation of Parameter-Efficient Fine-Tuning in Diffusion Models](zero-shot_adaptation_of_parameter-efficient_fine-tuning_in_diffusion_models.md)

</div>

<!-- RELATED:END -->
