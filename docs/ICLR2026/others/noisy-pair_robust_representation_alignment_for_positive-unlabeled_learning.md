---
description: "【论文笔记】Noisy-Pair Robust Representation Alignment for Positive-Unlabeled Learning 论文解读 | ICLR 2026 | arXiv 2510.01278 | PU学习 | 提出NcPU框架解决PU学习中判别性表示学习的瓶颈：(1) NoiSNCL噪声对鲁棒的非对比损失使clean pair梯度主导训练；(2) PhantomGate伪标签消歧提供保守负标签。两者在EM框架下迭代互利，在CIFAR-100上将差距（vs 监督学习）从14.26%缩至接近0。"
tags:
  - ICLR 2026
---

# Noisy-Pair Robust Representation Alignment for Positive-Unlabeled Learning

**会议**: ICLR 2026  
**arXiv**: [2510.01278](https://arxiv.org/abs/2510.01278)  
**代码**: https://github.com/Hengwei-Zhao96/NcPU  
**领域**: 其他 / 半监督学习  
**关键词**: PU学习, 非对比表示学习, 噪声对鲁棒, 伪标签消歧, EM框架

## 一句话总结
提出NcPU框架解决PU学习中判别性表示学习的瓶颈：(1) NoiSNCL噪声对鲁棒的非对比损失使clean pair梯度主导训练；(2) PhantomGate伪标签消歧提供保守负标签。两者在EM框架下迭代互利，在CIFAR-100上将差距（vs 监督学习）从14.26%缩至接近0。

## 研究背景与动机
PU学习只有有限正样本和大量无标签数据，需要训练二分类器。SOTA PU方法在复杂数据集上与监督学习差距极大（如CIFAR-100上14.26%），瓶颈在于无法从不可靠监督中学到判别性表示。

t-SNE可视化清晰显示：LaGAM和HolisticPU学到的特征中正/负类严重重叠，而监督学习的特征分离清晰。核心挑战是"噪声对"问题——伪标签不准导致被错误认为同类的样本对被拉近，破坏表示空间。

创新点：非对比表示学习只拉近同类（不推远异类），天然减少噪声对的影响。但标准非对比损失中噪声对的梯度仍主导训练（因为它们对的距离大→梯度大）。NoiSNCL通过取sqrt改变了梯度-距离关系，让clean pair主导。

## 方法详解

### 整体框架
NoiSNCL（提供判别性表示）+ PLD（提供更准确的伪标签）→ 两者在EM框架下迭代互利。

### 关键设计

1. **NoiSNCL**：$\tilde{L}_r = 2\sqrt{1 - \langle \tilde{q}_i, \tilde{k}_j \rangle}$。关键性质：clean pair（已对齐→余弦相似度高）的梯度大于noisy pair（未对齐→相似度低）的梯度。这与标准非对比损失相反。

2. **PhantomGate**：通过自适应阈值τ将可信的负样本标为[0,1]^T，不确定的样本保持prototype-based更新。Regret机制：误标的样本可以恢复更新。SAT自适应阈值随训练进展自动升高。

3. **EM理论联系**：E-step=伪标签分配，M-step=NoiSNCL最小化≈最大化likelihood下界。Thm 1在vMF分布假设下证明了等价性。

### 损失函数 / 训练策略
总损失 L = L_ce(P) + L_ce(U) + w_r · NoiSNCL。w_r=50。所有momentum超参=0.99。BYOL式target network做动量更新。

## 实验关键数据

### 主实验
| 方法 | CIFAR-10 OA | CIFAR-100 OA | STL-10 OA | ABCD F1 | 需辅助信息 |
|------|------------|-------------|-----------|---------|----------|
| nnPU | 87.29 | 68.06 | 75.10 | 85.21 | π_p |
| HolisticPU | 88.84 | 71.62 | 72.55 | 85.77 | 负样本 |
| LaGAM | 89.57 | 76.49 | 76.26 | - | 负样本 |
| **NcPU** | **92.03** | **82.55** | **82.01** | **89.91** | **无** |
| Supervised | 95.14 | 82.98 | 85.38 | 93.66 | 全标签 |

### 消融实验
| 配置 | CIFAR-10 OA | 说明 |
|------|------------|------|
| CE only (baseline) | 60.45 | 无表示学习 |
| +标准SupNCL | 87.50 | 噪声对主导 |
| +NoiSNCL | **91.03** | 噪声对鲁棒 |
| +NoiSNCL+PLD | **92.03** | 伪标签+表示迭代互利 |

### 关键发现
- NcPU在CIFAR-100上(82.55 vs 82.98 supervised)几乎消除了与监督学习的差距——PU学习的重大突破。
- NoiSNCL单独就能使简单PU方法达到competitive性能——表示学习是关键瓶颈。
- 灾后建筑损伤评估(ABCD/xBD)上展示了实际应用价值。
- 不需要辅助负样本或预估class prior——实用性更强。

## 亮点与洞察
- 梯度分析精确揭示了噪声对主导训练的机制，sqrt变换的解决方案简洁有效。
- EM框架的理论解释为NoiSNCL和PLD的协同提供了原理性保证。
- 从14.26%差距到<1%差距，是PU学习领域的显著进步。

## 局限性 / 可改进方向
- vMF分布假设可能在某些数据上不精确。
- 仅在图像分类验证，NLP/图数据的适用性待探索。
- w_r=50的选择对不同数据集的敏感性未充分分析。

## 相关工作与启发
- 与DistPU、LaGAM等SOTA互补，揭示了表示学习瓶颈。
- NoiSNCL的设计思路可能对其他噪声标签学习问题有启发。

## 评分
- 新颖性: ⭐⭐⭐⭐ 噪声对鲁棒的非对比损失设计新颖
- 实验充分度: ⭐⭐⭐⭐⭐ 多数据集+消融+实际应用
- 写作质量: ⭐⭐⭐⭐ 理论推导清晰
- 价值: ⭐⭐⭐⭐ PU学习的重要进展
