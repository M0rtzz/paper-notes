---
description: "【论文笔记】Johnson-Lindenstrauss Lemma Beyond Euclidean Geometry 论文解读 | NEURIPS2025 | arXiv 2510.22401 | Johnson-Lindenstrauss | 将经典 Johnson-Lindenstrauss 引理从欧氏空间推广到任意 symmetric hollow dissimilarity 矩阵，通过 pseudo-Euclidean 空间和 generalized power distance 两条互补路线，给出与数据偏离欧氏几何程度挂钩的 fine-grained 误差保证。"
tags:
  - NEURIPS2025
---

# Johnson-Lindenstrauss Lemma Beyond Euclidean Geometry

**会议**: NEURIPS2025  
**arXiv**: [2510.22401](https://arxiv.org/abs/2510.22401)  
**代码**: [GitHub](https://anonymous.4open.science/r/Non-Euclidean-Johnson-Lindenstrauss-1673)  
**领域**: others  
**关键词**: Johnson-Lindenstrauss, dimensionality reduction, non-Euclidean geometry, pseudo-Euclidean space, power distance  

## 一句话总结

将经典 Johnson-Lindenstrauss 引理从欧氏空间推广到任意 symmetric hollow dissimilarity 矩阵，通过 pseudo-Euclidean 空间和 generalized power distance 两条互补路线，给出与数据偏离欧氏几何程度挂钩的 fine-grained 误差保证。

## Problem

经典 JL 引理是欧氏空间降维的基石——随机线性投影可将 $n$ 个点从 $\mathbb{R}^d$ 映射到 $\mathbb{R}^m$（$m = O(\log n / \varepsilon^2)$），同时以 $(1 \pm \varepsilon)$ 倍数保持所有 pairwise 距离。但其适用有两个硬性前提：(1) 数据在高维欧氏空间中；(2) 坐标可用。

现实中大量相似性度量是**非欧氏甚至非度量的**：Minkowski 距离、cosine similarity、Hamming 距离、Jaccard index、KL divergence 等。心理学研究也表明人类相似性判断不满足度量公理。此外推荐系统等场景中，pairwise dissimilarity 矩阵比高维坐标更易获取。

已知在 $\ell_1$、$\ell_p$ 和 nuclear norm 下，常数失真的降维目标维度必须是 $n$ 的多项式量级，不可能达到 JL 式的 $O(\log n)$。这些 lower bound 表明：对非欧数据做 worst-case 的对数维度保证是不可能的。

**核心问题**：对一般的 symmetric hollow dissimilarity 矩阵，能否应用 JL 变换并给出随非欧偏离程度优雅退化的误差分析？

## Core Idea

提出两条互补思路：

1. **Pseudo-Euclidean 路线**：利用任何 symmetric hollow 矩阵都可以嵌入 pseudo-Euclidean 空间 $\mathbb{R}^{p,q}$ 的事实，对 $p$-part 和 $q$-part 分别做 JL 投影，误差由 Euclidean norm 与 $(p,q)$-norm 之比 $C_{ij}$ 控制——衡量每对点偏离欧氏几何的程度。

2. **Generalized Power Distance 路线**：证明任何 symmetric hollow 矩阵可写为等半径加权点集的 generalized power distance 矩阵，半径 $r = \sqrt{|e_n|}/2$（$e_n$ 为 Gram 矩阵最小特征值）。对 ball center 施加标准 JL 投影即可获得 $(1 \pm \varepsilon)$ 乘法近似加 $4\varepsilon r^2$ 加法误差。

当数据恰好为欧氏数据时，$C_{ij} = 1$（路线一退化为经典 JL）、$r = 0$（路线二退化为经典 JL）。

## Method

### 1. Pseudo-Euclidean JL Transform

**坐标恢复**：给定 $n \times n$ dissimilarity 矩阵 $D$，计算 Gram 矩阵 $B = -CDC/2$（$C = I - \frac{1}{n}\mathbf{1}_n \mathbf{1}_n^T$ 为 centering matrix）。对 $B$ 做特征分解，设 $p$ 个非负特征值和 $q$ 个负特征值（$p + q = n$），恢复 $\mathbb{R}^{p,q}$ 中的坐标：

$$
X = (x_1, \cdots, x_n) = \mathrm{Diag}(\sqrt{|\lambda_1|}, \cdots, \sqrt{|\lambda_n|}) \cdot U^T
$$

使得 $D_{ij} = (x_i - x_j)^T \Lambda (x_i - x_j) = \langle x_i - x_j, x_i - x_j \rangle_{p,q}$。

**JL 投影**：对 $p$-part 和 $q$-part 各自独立施加标准 JL 随机投影 $f_p$、$f_q$，目标维度 $p', q' = O(\log n / \varepsilon^2)$。

**Theorem 2.3 (Fine-grained JL)：**

$$
(1 - \varepsilon \cdot C_{ij}) \|x_i - x_j\|_{p,q}^2 \leq \|f(x_i) - f(x_j)\|_{p',q'}^2 \leq (1 + \varepsilon \cdot C_{ij}) \|x_i - x_j\|_{p,q}^2
$$

其中 $C_{ij} = \left|\frac{\|x_i - x_j\|_E^2}{\|x_i - x_j\|_{p,q}^2}\right|$。关键洞察：误差不是 uniform 的 $\varepsilon$，而是逐对地由 $C_{ij}$ 调控。当坐标从同一分布采样且 $q < \frac{C-1}{C+1} p$ 时，$C_{ij}$ 以高概率有常数上界，可恢复经典 $(1 \pm \varepsilon)$ 保证 (Theorem 2.6)。

### 2. Power Distance JL Transform

**核心代数结构 (Lemma 3.1)**：任意 symmetric hollow 矩阵 $D$ 可分解为

$$
D = E + 4r^2(I - J)
$$

其中 $E$ 是欧氏距离矩阵，$J = \mathbf{1}_n \mathbf{1}_n^T$，$r = \sqrt{|e_n|}/2$。这意味着 $D$ 是 $n$ 个等半径 $r$ 的加权点的 generalized power distance 矩阵：

$$
D_{ij} = \|p_i - p_j\|_E^2 - 4r^2
$$

**几何解释**：Generalized power distance 衡量两个相离圆的内公切线段长度平方。经典 power of a point 由 Steiner 1826 年引入；本文将其推广到两个圆之间的距离。Casey 定理和 Ptolemy 不等式在此设置下仍然成立，为距离几何提供了额外结构约束。

**统计解释**：两个 Gaussian 分布 $\mathcal{N}(\mu_x, \sigma_x)$ 与 $\mathcal{N}(\mu_y, \sigma_y)$ 的 silhouette coefficient 恰好等于 $\|\mu_x - \mu_y\|^2 - (\sigma_x + \sigma_y)^2$，即 generalized power distance。因此 $r$ 可解释为数据中固有的不确定性/噪声水平，与先前文献"非欧性主要源于测量噪声"的观点一致。

**Theorem 3.3 (Power-distance JL)：** 对 ball center $\{p_i\}$ 施加标准 JL 投影 $f: \mathbb{R}^n \to \mathbb{R}^m$，$m = O(\log n / \varepsilon^2)$：

$$
(1 - \varepsilon) D_{ij} - 4\varepsilon r^2 \leq \hat{D}_{ij} \leq (1 + \varepsilon) D_{ij} + 4\varepsilon r^2
$$

**下界**：推广 [LN17] 的技术，证明达到上述近似保证的目标维度下界为 $\Omega(\log n / \varepsilon^2)$，与上界匹配——即该保证在维度上是最优的。

### 计算流程

1. 输入 $n \times n$ symmetric hollow dissimilarity 矩阵 $D$
2. SVD 分解 Gram 矩阵 $B = -CDC/2$，$O(n^3)$ 时间
3. 坐标恢复：按特征值正负分离为 $(p,q)$ 坐标 / 计算 $r$ 和欧氏 center 坐标
4. 随机投影到 $O(\log n / \varepsilon^2)$ 维
5. 输出低维 dissimilarity 矩阵供下游任务使用

可用 Landmark MDS 加速 SVD 步骤；若坐标来自 representation learning 模块可跳过坐标恢复。

## Experiments

### 数据集

| 数据集 | 大小 | 负特征值数 | 是否度量 |
|--------|------|-----------|----------|
| Simplex (合成) | 1000 | 900 | ✗ |
| Ball (合成) | 1000 | 887 | ✗ |
| Brain (基因组) | 130 | 53 | ✗ |
| Breast (基因组) | 151 | 59 | ✗ |
| Renal (基因组) | 143 | 57 | ✗ |
| MNIST (图像) | 1000 | 454 | ✓ |
| CIFAR-10 (图像) | 1000 | 399 | ✓ |
| Email (图) | 986 | 465 | ✓ |
| Facebook (图) | 4039 | 1566 | ✓ |
| MOOC (图) | 7047 | 268 | ✓ |

### 基线

经典 JL transform（直接对原始坐标做随机投影）。

### 评估指标

- **Relative error**：$\max_{i,j} |D_{ij} - \hat{D}_{ij}|/D_{ij}$（worst-case / average / median）
- **下游 $k$-Means 聚类代价**

## Results

### 理论验证

- **Pseudo-Euclidean JL**：$\varepsilon = 0.5$、目标维度取 $2\log n / \varepsilon^2$ 时，近似比绝大部分落在 $(1 \pm \varepsilon \cdot C_{ij})$ 预测范围内。目标维度翻倍（80→160）后违规比例从 12.01% 降至 4.62%。
- **Power Distance JL**：残差加法误差远低于理论上界 $4\varepsilon r^2$（以 $r/100$ 为尺度绘图仍全部满足），说明理论上界非常宽松。

### Relative Error 对比

| 方法 | 基因组 | 图像 | 图数据 |
|------|--------|------|--------|
| JL | 极大 ($10^{9}\sim10^{12}$)，图像为 inf | 中等 | 中等 |
| JL-PE | **基因组最优** (avg 1.15~8.16) | 中等 | 略差 |
| JL-Power | 基因组较差 | **最优** (avg 1.47/1.61) | **最优** (avg 1.32~2.04) |

- JL-PE 在基因组数据（强非欧、非度量）上大幅领先
- JL-Power 在其余 7 个数据集上表现最优
- 经典 JL 在图像数据上出现 inf（不同图像被投到同一点）

### $k$-Means 聚类

两种方法在绝大多数数据集上优于经典 JL。Brain 上 JL-PE 代价 3.13 vs JL 的 728.00；Breast 上 JL-Power 12.53 vs JL 827.69。仅 Facebook 上 JL-Power 略差于 JL。

## Limitations

1. **两条路线之间缺乏理论联系**：无法形式化说明何时该用哪条路线
2. **缺乏 pseudo-Euclidean 路线的下界**：fine-grained JL 保证没有匹配的 lower bound
3. **计算复杂度**：坐标恢复需 $O(n^3)$ SVD，大规模数据不实际
4. **实验规模有限**：最大数据集仅 7047 点
5. **与现代 ML pipeline 集成**：尚未展示与 representation learning / transformer 的实际结合

## My Notes

- **理论意义深远**：JL 引理推广到任意 symmetric dissimilarity 是降维理论的重要进展。两条路线各有独立的几何/统计解释，思路极为优雅
- **Generalized power distance 视角新颖**：将非欧性理解为"数据带有不确定性半径"，与 silhouette coefficient 的联系意外且自然，可能启发新的鲁棒距离度量设计
- **与 Minkowski 空间 / Lorentz 空间的关系**：pseudo-Euclidean 空间 $\mathbb{R}^{p,q}$ 涵盖 Minkowski 时空和双曲空间（hyperboloid 模型），暗示在 hyperbolic representation learning 中有直接应用
- **与 transformer attention 的联系**：bilinear form 与 scaled dot-product attention 的对应关系值得深挖——若能在 attention 层做 non-Euclidean JL compression，可能在长序列推理效率上有突破
- **Casey 定理 / Ptolemy 不等式的引入**是降维领域少见的几何工具，可能启发新方法
- **实用性**：$O(n^3)$ SVD 是瓶颈，但 Landmark MDS 或与 learned representation 结合可缓解

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ — 两条路线均为全新理论贡献，将 JL 引理推广到非欧非度量设置
- 实验充分度: ⭐⭐⭐ — 10 个数据集覆盖合成/基因/图像/图，但规模有限且下游任务仅测 k-Means
- 写作质量: ⭐⭐⭐⭐ — 理论推导清晰，几何直觉好，但符号较多
- 价值: ⭐⭐⭐⭐ — 理论扎实的降维推广，与 representation learning 整合潜力大
