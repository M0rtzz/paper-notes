# Generalization Bounds for Semi-supervised Matrix Completion with Distributional Side Information

**会议**: AAAI 2026  
**arXiv**: [2511.13049](https://arxiv.org/abs/2511.13049)  
**代码**: 待确认  
**领域**: recommender  
**关键词**: matrix completion, semi-supervised learning, generalization bounds, implicit feedback, low-rank subspace  

## 一句话总结
提出半监督矩阵补全的理论框架：假设采样分布 $P$ 与真实矩阵 $G$ 共享低秩子空间，利用大量无标签隐式反馈估计子空间、少量有标签显式反馈恢复矩阵，证明泛化误差可分解为两个独立项 $\widetilde{O}(\sqrt{(m+n)r/M} + \sqrt{dr/N})$。

## 背景与动机
- 矩阵补全（MC）是推荐系统的核心问题，但现有理论均假设所有观测样本都带有标签
- 实际中大量 implicit feedback（点击/购买/浏览）容易获取但无评分标签，而 explicit feedback（1-5星评分）稀缺
- 需要一个半监督学习框架同时利用大量无标签交互和少量有标签评分
- Inductive MC（IMC）假设 side information 矩阵 $X, Y$ 已知，但实践中需从数据估计

## 核心问题
在推荐系统中，能否利用大量无标签的用户-物品交互（隐式反馈）来大幅降低对有标签评分数据（显式反馈）的需求？如何建立理论保证？

## 方法详解

### 整体框架
提出 DAMC（Distributionally Aware Matrix Completion）算法，两阶段流程：
1. **子空间估计**：用 $M$ 个无标签样本构造经验分布矩阵 $\mathcal{H}$，做截断 SVD 得到 $X = \sqrt{m/d} \cdot U$, $Y = \sqrt{n/d} \cdot V$
2. **矩阵恢复**：以估计的 $X, Y$ 为 side information，在 $N$ 个有标签样本上做带 nuclear norm 约束的 IMC: $\min_{\|\underline{M}\|_* \leq \mathcal{M}} \frac{1}{N} \sum l((X\underline{M}Y^\top)_{\xi_o}, \tilde{G}_o)$

### 关键设计
1. **共享子空间假设**（Assumption 2）：$P$ 和 $G$ 共享行/列子空间，$G = U^* \underline{M}^* [V^*]^\top$
2. **误差分解定理**（Theorem 1）：泛化 gap 分解为三项——子空间估计误差 $O(\sqrt{(m+n)r/M})$、矩阵恢复误差 $O(\sqrt{dr/N})$、交叉项 $O(\sqrt{\Gamma(m+n)r/(MN)})$
3. **样本复杂度**：仅需 $\widetilde{O}((m+n)r)$ 无标签样本 + $\widetilde{O}(dr)$ 有标签样本，后者远小于传统 MC 的 $\widetilde{O}((m+n)r)$
4. **技术工具**：结合矩阵扰动理论（spectral perturbation bounds）和经典 IMC 泛化界

## 实验关键数据
**合成实验**：$200 \times 200$ 矩阵，$d=r=4$，验证泛化误差确实可分解为两个独立项的叠加（散点图高度相关）

**真实数据（RMSE，去除 90% 标签）**：

| 数据集 | UserKNN | SoftImpute | IGMC | DAMC |
|--------|---------|------------|------|------|
| ML-100K | 1.168 | 1.419 | 1.117 | **1.006** |
| Douban | 0.964 | 1.847 | 0.871 | **0.832** |
| Yelp | 1.223 | 3.269 | 1.203 | **1.129** |

- 当 $p=0.9$（去除 90% 评分）时 DAMC 仍表现优异，而 SoftImpute 等基线接近随机

## 亮点
- 首个将隐式反馈建模为采样分布并与显式反馈共享子空间的矩阵补全理论工作
- 证明了误差的可加性分解，理论清晰优美
- 实验验证了理论预测：合成数据上误差确实独立可分解
- 实际意义重大：少量评分 + 大量点击数据即可有效推荐，呼应工业实践

## 局限性 / 可改进方向
- Assumption 7（采样概率上界 $\Gamma$）较强，放松此假设是重要方向
- 均匀边际分布假设（Assumption 4）在真实推荐系统中常不满足
- 实验中用非线性 autoencoder 替代 SVD 但理论未覆盖此设置
- 未考虑 MNAR（Missing Not At Random）场景下的扩展
- 真实数据规模较小（ML-100K），未在大规模数据集上验证

## 与相关工作的对比
- **经典 MC**（Foygel et al.）：需 $\widetilde{O}((m+n)r)$ 有标签样本，无法利用无标签数据
- **IMC**（Jain & Dhillon）：假设 side information 已知，本文从无标签数据估计
- **MNAR MC**（Ma & Chen）：关注非均匀采样下的 Frobenius 误差和 inverse propensity，与本文 i.i.d. excess risk 设置不同
- **DAMC**：首个在 MC 中引入半监督学习并给出泛化界的工作

## 启发与关联
- 隐式反馈包含子空间信息的假设为推荐系统中"点击数据有价值"提供了理论支撑
- 两阶段方法（无监督子空间+有监督补全）可推广到其他半监督矩阵学习问题
- 与 contrastive learning 结合可能进一步增强子空间估计的鲁棒性

## 评分
- 新颖性: ⭐⭐⭐⭐
- 实验充分度: ⭐⭐⭐
- 写作质量: ⭐⭐⭐⭐
- 价值: ⭐⭐⭐⭐
