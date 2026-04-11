# How Many Domains Suffice for Domain Generalization? A Tight Characterization via the Domain Shattering Dimension

**会议**: NeurIPS2025  
**arXiv**: [2506.16704](https://arxiv.org/abs/2506.16704)  
**作者**: Cynthia Dwork, Lunjia Hu, Han Shao (Harvard University)
**代码**: 无（纯理论工作）  
**领域**: others  
**关键词**: domain generalization, learning theory, domain shattering dimension, VC dimension, PAC learning, sample complexity

## 一句话总结

提出 **domain shattering dimension** 这一新组合度量，紧致地刻画了 domain generalization 所需的 domain 数量（domain sample complexity），并建立其与经典 VC dimension 之间的精确定量关系，证明 PAC 可学习性蕴含 domain generalization 可学习性。

---

## Problem

Domain generalization 的核心问题：给定一个 domain 族 $\mathcal{G}$（即数据分布集合），学习器需要从中随机采样多少个 domain、收集数据后训练出一个模型，使其在**所有**（包括未见过的）domain 上都表现良好？

本文关注的是更高层级的 **domain sample complexity**——需要观测多少个 domain 才能泛化到未见 domain。这与传统 PAC learning 中关注单个 domain 上需要多少数据点的 sample complexity 形成对比，可以看作 sample complexity 的 "meta" 版本。

**关键假设**：存在一个 "universal hypothesis" $h^\star \in \mathcal{H}$，其在所有 domain 上误差不超过某阈值 $\tau$（如 0.3），即 $\max_{\mathcal{D} \in \mathcal{G}} \mathrm{err}_\mathcal{D}(h^\star) \leq \tau$。除此之外**不假设 domain 之间有任何结构化关系**（不假设相似性、因果结构、混合系数约束等），这使得模型非常通用。

**学习目标**：输出假设 $h$ 使得对 meta-distribution $\mathcal{P}$ 采样的新 domain $\mathcal{D}$，以高概率满足 $\mathrm{err}_\mathcal{D}(h) \leq \tau$。注意这是要求在**几乎所有** domain 上同时达标，而非平均误差低——平均误差 0.25 可能意味着 3/4 domain 误差为 0 但 1/4 domain 完全预测错误。

---

## Core Idea

### 为什么已有度量不够？

自然的想法是分析误差函数类 $\{\mathrm{err}_\cdot(h) : h \in \mathcal{H}\}$ 的 fat-shattering dimension，但这会**高估** domain sample complexity。原因是 fat-shattering dimension 允许不同 domain 使用不同阈值，且在所有阈值上取最大值。例如即使在目标阈值 $\tau$ 处 domain sample complexity 很小，fat-shattering dimension 可能在另一个阈值 $\tau'$ 处很大。

### Domain Shattering Dimension

核心贡献是引入 **domain shattering dimension** $\mathrm{Gdim}(\mathcal{H}, \mathcal{G}, \tau, \alpha)$：

一个 domain 子集 $S \subseteq \mathcal{G}$ 被 $\mathcal{H}$ 在阈值 $\tau$ 处以 margin $\alpha$ **shatter**，当且仅当对 $S$ 的**每个子集** $E$，都存在 $h_E \in \mathcal{H}$ 使得：

- 对 $\mathcal{D} \in E$：$\mathrm{err}_\mathcal{D}(h_E) < \tau - \alpha$（好的 domain 误差明显低于阈值）
- 对 $\mathcal{D} \in S \setminus E$：$\mathrm{err}_\mathcal{D}(h_E) > \tau$（坏的 domain 误差超过阈值）

关键区别：要求**统一固定**的阈值 $\tau$，而非 fat-shattering 中允许逐 domain 选择不同阈值。这使得 domain shattering dimension 精确捕捉 $\mathcal{H}$ 与 $\mathcal{G}$ 之间的**交互复杂度**——即使两者各自复杂，只要复杂性集中在 input space 的不同子集上，domain sample complexity 可以很小。

---

## Method

### 算法：Min-Max ERM

给定 $n$ 个 i.i.d. 采样的训练 domain $G = \{\mathcal{D}_1, \ldots, \mathcal{D}_n\}$，算法返回：

$$\hat{h} = \arg\min_{h \in \mathcal{H}} \max_{\mathcal{D} \in G} \widehat{\mathrm{err}}_\mathcal{D}(h)$$

其中 $\widehat{\mathrm{err}}_\mathcal{D}(h)$ 是基于每个 domain 上 $O\!\left(\frac{\mathrm{VCdim}(\mathcal{H}) + \log(n/\delta)}{\varepsilon^2}\right)$ 个数据点估计的经验误差。

**为什么不用标准 ERM？** 标准 ERM 最小化全体训练数据的总误差，可能选到在一半 domain 上误差为 0、另一半上误差高达 0.5 的假设。Min-Max ERM 通过优化**最坏 domain** 上的表现解决这一问题。

### 上界证明核心思路 (Theorem 4.1)

1. 将每个 $h \in \mathcal{H}$ 映射为 **partial concept** $f_h : \mathcal{G} \to \{0, 1, \bot\}$：误差 $> \tau$ 标 1，$< \tau - \alpha$ 标 0，介于两者之间标 $\bot$
2. 新 partial concept class $\mathcal{F}$ 的 VC dimension 恰好等于 domain shattering dimension $d$
3. 利用 Alon et al. (2022) 的 **generalized Sauer-Shelah-Perles lemma**（partial concept class 版本），通过 symmetrization trick 建立 uniform convergence bound

### 下界证明核心思路 (Theorem 4.4)

通过构造扩展 domain 族 $\mathcal{G}' = \mathcal{G} \cup \{\mathcal{D}_0, \mathcal{D}_1', \ldots, \mathcal{D}_d'\}$，其中 $\mathcal{D}_i' = (1-\lambda)\mathcal{D}_0 + \lambda(\neg \mathcal{D}_i)$ 是零误差分布与标签翻转分布的混合。巧妙之处在于：扩展后 domain shattering dimension 不变（可互相替换 $\mathcal{D}_i$ 和 $\mathcal{D}_i'$），同时创造了 domain 之间的 overlap，使学习器无法走捷径。通过随机 bit string 构造 $2^d$ 个不可区分情形，证明 $\Omega(d/n)$ 的误差下界不可避免。

---

## Experiments

本文为纯理论工作，主要结果均为定理证明，无实验部分。核心理论结果如下。

### 主定理——上界 (Theorem 4.1)

$$\mathrm{Er}_{\mathcal{P},\tau}(\hat{h}) \leq O\!\left(\frac{d \log^2 n + \log(1/\delta)}{n}\right)$$

其中 $d = \mathrm{Gdim}(\mathcal{H}, \mathcal{G}, \tau, \alpha)$。

### 主定理——下界 (Theorem 4.4)

$$\gamma = \Omega\!\left(\min\!\left\{1,\; \frac{d + \log(1/\delta)}{n}\right\}\right)$$

上下界匹配至 polylogarithmic factor ($\log^2 n$)。

### VC Dimension 关系 (Theorems 5.1 & 5.2)

$$\mathrm{Gdim}(\mathcal{H}, \mathcal{G}, \tau, \alpha) = \Theta\!\left(\mathrm{VCdim}(\mathcal{H}) \cdot \log(1/\alpha)\right)$$

这意味着：当 margin $\alpha$ 固定时，domain shattering dimension 线性受控于 VC dimension；当 $\alpha \to 0$ 时可以任意大于 VC dimension。最重要的推论是 **PAC 可学习性蕴含 domain generalization 可学习性**。

### 与 Domain Adaptation 的联系 (Theorem 6.1)

当 $\mathcal{G}$ 在 refined $(\mathcal{H}, \tau)$-divergence 度量下有有限 $\alpha/2$-cover 时，domain shattering dimension 不超过 cover size。特别地，当所有 domain 足够相似（cover size 为 1）时，只需采样一个 domain 即可泛化。

---

## Results

1. **Domain shattering dimension 紧致刻画 domain sample complexity**：上下界仅差 $O(\log^2 n)$ factor
2. **与 VC dimension 的精确关系**：$\mathrm{Gdim} = \Theta(\mathrm{VCdim} \cdot \log(1/\alpha))$
3. **与 domain adaptation 的联系**：当 $(\mathcal{H}, \tau)$-divergence 覆盖数有限时，domain shattering dimension 也有限
4. **算法通用性**：Min-Max ERM 可直接推广到多分类和回归任务（Remark 4.2）
5. **Partial concept 的 uniform convergence**：Lemma 4.2 作为独立结果可能有其他应用

---

## Limitations

1. **上下界存在 gap**：上界保证误差阈值 $\tau$，下界针对略低的 $\tau' \in (\tau - \alpha, \tau)$，且下界需要对 $\mathcal{G}$ 做轻微扩展
2. **计算可行性未解决**：domain shattering dimension 的计算复杂度类似 VC dimension，通常是 NP-hard 的，论文未给出估计方法
3. **假设类 $\mathcal{H}$ 需预先给定**：如何从候选假设类集合中选择最优的 $\mathcal{H}$ 是开放问题
4. **未利用 unlabeled data**：若允许在测试 domain 上使用无标签数据修改假设，是否能突破下界？作为 open question 提出
5. **对 "universal hypothesis" 的存在性假设**：需要 $\mathcal{H}$ 中存在跨所有 domain 表现良好的假设，实践中可能不总成立

---

## My Notes

**理论意义**：这是 domain generalization 理论基础的重要工作。与之前大多需要假设 domain 间有某种关系（相似性、因果结构、混合系数约束）的工作不同，本文只假设存在 universal hypothesis，就能给出 tight characterization。Domain shattering dimension 优雅地捕捉了 $\mathcal{H}$ 与 $\mathcal{G}$ 的交互——即使两者各自复杂，只要复杂性集中在 input space 的不同子集上，domain sample complexity 可以很小。

**技术亮点**：

- **Partial concept class 的使用**非常巧妙——将实值误差函数问题转化为三值标签问题（0/1/$\bot$），从而可以利用成熟的 VC theory 工具
- **下界构造**中标签翻转 + 混合分布的技巧保持 domain shattering dimension 不变，同时创造 domain 间的 overlap，防止学习器利用 marginal distribution 的不同走捷径
- **与 VC dimension 关系的证明**中用 dimension reduction + probabilistic method 构造代表性数据集的技巧简洁有力

**与 multi-distribution learning 的区别**：一个重要概念区分——multi-distribution learning 关注在 **observed domain** 上学好（focus on sample complexity），本文关注泛化到 **unobserved domain**（focus on domain sample complexity）。

**实践启示**：虽然是纯理论工作，Min-Max ERM 在大规模假设类上的计算可行性不明，但理论上认清了 "需要多少 domain" 这个基本问题的答案量级，为实践中的数据收集策略提供了指导。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ (全新组合度量 + tight characterization)
- 实验充分度: N/A (纯理论)
- 写作质量: ⭐⭐⭐⭐⭐ (严谨清晰，动机从医疗场景引入非常到位)
- 推荐值: ⭐⭐⭐⭐⭐ (domain generalization 理论基础的里程碑)
