---
title: >-
  [论文解读] Training Flexible Models of Genetic Variant Effects from Functional Annotations using Accelerated Linear Algebra
description: >-
  [ICML 2025][医学图像][全基因组关联分析] DeepWAS利用LD矩阵的带状近似做mini-batch训练 + Woodbury恒等式重参数化使矩阵良条件化 + 迭代线性代数算法（CG+SLQ）GPU加速，首次实现在百万变异规模上用大规模神经网络（5200万参数Transformer）优化完整边际似然来预测基因变异效应，核心发现是更大模型仅在全似然训练下才带来提升而在摘要统计量训练下反而退步。
tags:
  - ICML 2025
  - 医学图像
  - 全基因组关联分析
  - 功能注释
  - 经验贝叶斯
  - 加速线性代数
  - 连锁不平衡
---

# Training Flexible Models of Genetic Variant Effects from Functional Annotations using Accelerated Linear Algebra

**会议**: ICML 2025  
**arXiv**: [2506.19598](https://arxiv.org/abs/2506.19598)  
**代码**: [GitHub](https://github.com/AlanNawzadAmin/DeepWAS)  
**领域**: 计算遗传学 / 机器学习  
**关键词**: 全基因组关联分析, 功能注释, 经验贝叶斯, 加速线性代数, 连锁不平衡

## 一句话总结

DeepWAS利用LD矩阵的带状近似做mini-batch训练 + Woodbury恒等式重参数化使矩阵良条件化 + 迭代线性代数算法（CG+SLQ）GPU加速，首次实现在百万变异规模上用大规模神经网络（5200万参数Transformer）优化完整边际似然来预测基因变异效应，核心发现是更大模型仅在全似然训练下才带来提升而在摘要统计量训练下反而退步。

## 研究背景与动机

**领域现状**：全基因组关联分析（GWAS）使用数十万个体的基因型和表型数据建模，通过功能基因组注释（DNA可及性、蛋白结合、保守分数等）构建"功能信息先验"预测哪些变异更可能影响表型。标准模型为贝叶斯线性模型 $y=X^\top\beta+\epsilon$，$\beta_m \sim \mathcal{N}(0, f_m)$，其中 $f_m=f_\theta(C_m)$ 从注释预测。

**现有痛点**：训练 $f_\theta$ 的核心瓶颈在于连锁不平衡（LD）——相邻变异高度相关，边际似然（Eqn 2: $\hat\beta \sim \mathcal{N}(0, RF_\theta R + \sigma_N^2 R)$）涉及大型LD矩阵 $R$ 的求逆和对数行列式，复杂度 $O(M^3)$（$M$为变异数，百万级）。现有方法两个妥协：(1) 只用简单参数化模型（常数或线性 $f_\theta$）；(2) 拟合摘要统计量（LD score regression, LDSR）而非完整似然。

**核心矛盾**：更灵活的模型（如NN）理论上能更好地从功能注释预测变异效应，但训练需要优化完整似然（需求解大矩阵），计算上不可行。用LDSR训练大模型反而比小模型差——增加容量无法弥补信息损失。

**本文要解决什么？** (1) 高效计算包含LD矩阵的边际似然及梯度；(2) 在百万变异规模上训练大规模神经网络先验。

**切入角度**：从GP文献借鉴迭代线性代数加速技术，利用LD矩阵的带状结构做mini-batch，利用Woodbury恒等式将病态矩阵转化为良条件矩阵加速迭代求解。

**核心idea一句话**：大模型只有在优化完整似然时才有效——而DeepWAS通过加速线性代数首次使这成为可能。

## 方法详解

### 整体框架

模型假设 $\hat\beta \sim \mathcal{N}(0, RF_\theta R + \sigma_N^2 R)$，其中 $R$ 是公开的LD矩阵，$\hat\beta$ 是公开的关联统计量，$F_\theta = \text{diag}(f_\theta(C_m))$ 是由神经网络从功能注释预测的效应先验。训练目标：最大化边际似然 $-\frac{1}{2}\hat\beta^\top A_\theta^{-1}\hat\beta - \frac{1}{2}\log|A_\theta|$，其中 $A_\theta = RF_\theta R + \sigma_N^2 R$。挑战在于 $A_\theta$ 是百万级矩阵。

### 关键设计

1. **LD矩阵带状近似 + Mini-batch训练**

    - 功能：将全基因组似然分解为可独立计算的窗口，支持SGD
    - 核心思路：利用LD的局部性（远距离变异几乎不相关），将 $R$ 近似为带状矩阵（带宽100万位置）。全基因组似然分解为约2700个窗口的独立似然之和（Eqn 5）。每步只需对窗口 $(i)$ 及其邻域 $(i)^+$ 的约 $10^4$ 个变异计算 $f_\theta$。有趣的是，极端情况下（窗口=1）退化为LDSR（Eqn 4），说明LDSR是完全忽略变异间相关性的特例
    - 设计动机：避免每步计算全部百万变异的 $f_\theta$，使大NN可行

2. **Woodbury重参数化 + 迭代线性代数**

    - 功能：将需要求逆的病态矩阵转化为良条件矩阵，使迭代算法快速收敛
    - 核心思路：$A_\theta$ 通常奇异且病态。用Woodbury恒等式重写为：$(A_\theta^{(i)})^{-1} = \frac{1}{\sigma_N^2}R^\dagger - L^\top F_\theta^{1/2}(I+\frac{1}{\sigma_N^2}F_\theta^{1/2}WF_\theta^{1/2})^{-1}F_\theta^{1/2}L$，其中 $R^\dagger, L, W$ 不依赖 $\theta$ 可预计算。核心矩阵 $B_\theta = I + \frac{1}{\sigma_N^2}F_\theta^{1/2}WF_\theta^{1/2}$ 严格正定且良条件（因为 $\sigma_N^{-2}F_\theta \approx N/M < 1$）。用共轭梯度法（CG）求 $B_\theta^{-1}$，随机Lanczos求积（SLQ）计算 $\log|B_\theta|$，复杂度 $O(M_i^2 K)$，$K \ll M_i$
    - 设计动机：直接Cholesky $O(M_i^3)$太慢且可能奇异。即使用迭代算法，$A_\theta$的病态导致收敛极慢。$B_\theta$的良条件性使CG几步收敛。配合GPU（vs之前的CPU）进一步加速

3. **大规模功能注释 + Transformer-CNN混合架构**

    - 功能：从丰富的基因组功能信息灵活地预测变异效应先验
    - 核心思路：收集165维功能注释（ENCODE结合位点、FANTOM增强子、PhyloP/phastCons保守分数等）在每个变异周围 $w=256$ 位点的窗口内取值，加上9维编码区突变效应预测。模型 $f_{\theta,m} = (\text{freq}_m(1-\text{freq}_m))^{0.7} \cdot \text{NN}_\theta(C_{\text{func},m}, C_{\text{pred},m})$。NN采用改编自Enformer的Transformer-CNN混合架构，参数量3.9M到52M可调。使用CoLA库实现自动微分
    - 设计动机：之前方法只用少量特征的窗口平均值，丢失分辨率。频率缩放因子 $(\text{freq}(1-\text{freq}))^\alpha$ 编码了稀有变异可能效应更大的生物学先验

### 损失函数 / 训练策略

最大化分窗口边际似然，SGD每步采样一个窗口。梯度通过CoLA库的CG/SLQ隐式微分计算。GPU训练（A100），设置CG相对容差 $10^{-6}$，SLQ 100个采样。

## 实验关键数据

### 半合成数据（真实LD + 合成效应）

| 模型 | 训练方法 | $f_\theta$ 恢复误差↓ |
|------|---------|---------------------|
| 常数 | LDSR | 高 |
| 线性 | LDSR | 中 |
| Transformer(52M) | LDSR | 中（未改善） |
| 常数 | DeepWAS | 较低 |
| 线性 | DeepWAS | 低 |
| **Transformer(52M)** | **DeepWAS** | **最低** |

### UK Biobank 表型预测（held-out chr 6,7,8 似然改善）

| 模型 | 方法 | 身高 | BMI | 哮喘 |
|------|------|------|-----|------|
| 常数 $f$ | 基准 | 基线 | 基线 | 基线 |
| 线性 $f$ | LDSR | 提升 | 提升 | 小幅提升 |
| Transformer | LDSR | ≈线性 | **下降** | ≈线性 |
| 线性 $f$ | DeepWAS | 提升 | 提升 | 小幅提升 |
| **Transformer** | **DeepWAS** | **最大提升** | **最大提升** | **最大提升** |

### 消融实验

| 消融因素 | 影响 | 说明 |
|---------|------|------|
| LD窗口 1M→100K | 严重下降 | 更多变异相关信息需保留 |
| 特征窗口 w=256→16 | 下降 | 更大空间上下文有益 |
| 移除保守分数特征 | 下降 | PhyloP/phastCons是关键特征 |
| 模型参数 52M→3.9M | 下降 | 更大模型确实有效（在全似然下） |

### 关键发现

- **核心发现：大模型只在全似然训练下有效**——用LDSR训练Transformer时BMI预测反而比线性模型差（过拟合噪声），但DeepWAS下Transformer大幅超越所有小模型
- LDSR本质上是窗口=1的特例，丢失变异间相关信息→模型容量增加只是拟合噪声
- 计算加速效果显著：$B_\theta$上GPU迭代 vs $A_\theta$上CPU Cholesky 快一个数量级（Fig.2）
- 三个表型提升幅度与SNP遗传率一致——身高(>50%)提升最大，哮喘(10-16%)提升最小

## 亮点与洞察

- **"大模型只在全似然下有效"是深刻的方法论洞察**——这是一个通用教训：当训练目标（摘要统计量）丢失关键结构信息（变异间相关性）时，增加模型容量无法弥补。只有在信息保留完整的目标（全似然）下，灵活性才能转化为预测力。这对GP、VAE等领域也有启示
- **跨领域技术迁移的典范**：从GP借鉴迭代算法、从Enformer借鉴架构、Woodbury恒等式定制优化LD矩阵结构——每一步都利用了问题特有结构，比通用方法（如Nyström预条件）更高效

## 局限性 / 可改进方向

- 仅验证了正态先验下的线性模型 $y=X^\top\beta+\epsilon$，非正态先验或非线性模型留待未来
- 仅在欧洲裔人群（UK Biobank）上验证，跨人群泛化未知
- 带状近似对远距离LD（trans-chromosomal效应）处理不足
- 与最新多基因风险评分方法（PRS-CS、LDpred2）的下游预测对比缺失
- 保守地使用了较少的公开表型数据，更大规模数据可能进一步提升

## 相关工作与启发

- **vs S-LDSC (Finucane et al., 2015)**：线性 $f_\theta$ + LDSR（窗口=1的DeepWAS特例），无法利用更大模型
- **vs PolyFun (Li et al., 2024)**：广义线性模型 + 近似 $R^{-1}$，DeepWAS用精确 $R$ + 迭代算法
- **vs GPyTorch (Gardner et al., 2018)**：DeepWAS直接借鉴CG+SLQ技术，但Woodbury重参数化是针对LD矩阵的定制优化
- **启发**：快速线性代数是大规模贝叶斯推断的通用加速器；LD矩阵的带状结构暗示其他领域中类似结构（如时空相关矩阵）也可利用同样策略

## 评分

- 新颖性: ⭐⭐⭐⭐ 跨领域技术迁移+关键方法论洞察，但核心算法组件(CG/SLQ/Woodbury)并非原创
- 实验充分度: ⭐⭐⭐⭐ 半合成+真实数据+消融全面，但仅三个表型和单一人群
- 写作质量: ⭐⭐⭐⭐⭐ 从背景到方法的叙事流畅，核心发现呈现极其清晰
- 价值: ⭐⭐⭐⭐⭐ 对计算遗传学有直接推动，"大模型需要好损失"的结论有跨领域通用性

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICML 2025\] CFP-Gen: Combinatorial Functional Protein Generation via Diffusion Language Models](cfp-gen_combinatorial_functional_protein_generation_via_diffusion_language_model.md)
- [\[ICML 2025\] Steering Protein Language Models](steering_protein_language_models.md)
- [\[ICML 2025\] PolyConf: Unlocking Polymer Conformation Generation through Hierarchical Generative Models](polyconf_unlocking_polymer_conformation_generation_through_hierarchical_generati.md)
- [\[ICML 2025\] DeepSeq: High-Throughput Single-Cell RNA Sequencing Data Labeling via Web Search-Augmented Agentic Generative AI Foundation Models](deepseq_high-throughput_single-cell_rna_sequencing_data_labeling_via_web_search-.md)
- [\[ICML 2025\] Neural Stochastic Differential Equations on Compact State Spaces: Theory, Methods and Applications](neural_stochastic_differential_equations_on_compact_state_spaces_theory_methods_.md)

</div>

<!-- RELATED:END -->
