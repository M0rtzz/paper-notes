---
description: "【论文笔记】Hierarchical Reinforcement Learning with Uncertainty-Guided Diffusional Subgoals 论文解读 | ICML2025 | arXiv 2505.21750 | 层次强化学习 | 提出 HIDI 框架，以条件扩散模型建模子目标分布，并引入高斯过程 (GP) 先验进行不确定性正则化与子目标选择，在长时域连续控制任务上显著超越现有层次强化学习方法。"
tags:
  - ICML2025
---

# Hierarchical Reinforcement Learning with Uncertainty-Guided Diffusional Subgoals

**会议**: ICML2025  
**arXiv**: [2505.21750](https://arxiv.org/abs/2505.21750)  
**代码**: 待确认  
**领域**: 图像生成 / 强化学习  
**关键词**: 层次强化学习, 扩散模型, 高斯过程, 子目标生成, 不确定性量化, 连续控制

## 一句话总结

提出 HIDI 框架，以条件扩散模型建模子目标分布，并引入高斯过程 (GP) 先验进行不确定性正则化与子目标选择，在长时域连续控制任务上显著超越现有层次强化学习方法。

## 研究背景与动机

层次强化学习 (HRL) 将复杂决策分解为多层时间抽象，高层策略生成子目标 (subgoal) 引导低层策略执行。核心难点在于：

1. **非平稳性**：低层策略持续更新，导致高层过去经验中的子目标失效，HIRO 等方法通过 hindsight relabeling 缓解但效率有限
2. **子目标空间过大**：HRAC、HIGL 等通过约束子目标空间改善，但难以扩展到复杂环境
3. **缺乏不确定性建模**：传统 actor-critic 高层策略无法量化子目标预测的置信度，难以在探索与利用间取得平衡

本文的动机是用扩散模型直接建模状态条件子目标分布，替代基于 TD 学习的确定性策略，同时用 GP 提供显式不确定性量化来正则化扩散过程。

## 方法详解

### 整体框架：HIDI

HIDI 采用两层策略结构（同 HIRO）：高层策略 $\pi_h(g|s)$ 每 $k$ 步生成子目标，低层策略 $\pi_l(a|s,g)$ 每步执行动作。关键创新在于高层策略的建模方式。

### 1. 扩散子目标生成

将高层策略建模为条件扩散模型的逆过程：

$$\pi_{\theta_h}^h(g|s) \coloneqq p_{\theta_h}(g^{0:N}|s) = \mathcal{N}(g^N; 0, I) \prod_{i=1}^{N} p_{\theta_h}(g^{i-1}|g^i, s)$$

逆扩散去噪步骤采用噪声预测网络：

$$g^{i-1} = \frac{1}{\sqrt{\alpha_i}} \left( g^i - \frac{\beta_i}{\sqrt{1-\bar{\alpha}_i}} \epsilon_{\theta_h}(g^i, s, i) \right) + \sqrt{\beta_i} \epsilon$$

扩散损失为标准 DDPM 目标：

$$\mathcal{L}_{dm}(\theta_h) = \mathbb{E}_{i,\epsilon,(s,g)\sim\mathcal{D}_h} \left[ \| \epsilon - \epsilon_{\theta_h}(\sqrt{\bar{\alpha}_i} g + \sqrt{1-\bar{\alpha}_i} \epsilon, s, i) \|^2 \right]$$

其中 $\mathcal{D}_h$ 为 relabeled 高层经验回放缓冲区。

### 2. GP 不确定性正则化

在子目标函数上放置零均值 GP 先验，使用 RBF 核：

$$K(s_i, s_j) = \gamma^2 \exp\left[ -\frac{1}{2\ell^2} \sum_{d=1}^{D} (s_i^{(d)} - s_j^{(d)})^2 \right]$$

GP 正则化损失为负对数边际似然：

$$\mathcal{L}_{gp} = \mathbb{E}_{s,g} \left[ -\frac{1}{2} g^\top (K_N + \sigma^2 I)^{-1} g - \frac{1}{2} \log |K_N + \sigma^2 I| - \frac{N}{2} \log 2\pi \right]$$

采用稀疏 GP（$M \ll N$ 个诱导点）将计算复杂度从 $O(N^3)$ 降至 $O(NM^2)$。

**关键理论**（Proposition 3.2）：GP 梯度按不确定性加权：

$$\nabla_{\theta_h} L_{gp} = \mathbb{E}_{s,\epsilon'} \left[ \left( \frac{g - \mu_*(s)}{\sigma_*^2(s)} \right)^\top \nabla_{\theta_h} g \right]$$

即在 GP 置信度高（$\sigma_*^2$ 小）的状态区域施加更强的梯度压力，引导扩散模型向可靠子目标靠拢。

### 3. 子目标选择策略

结合扩散模型采样与 GP 预测均值的混合选择：

$$g_* = \begin{cases} \mu_*, & \text{概率 } \varepsilon \\ g \sim \pi_{\theta_h}(g|s_*), & \text{概率 } 1 - \varepsilon \end{cases}$$

默认 $\varepsilon = 0.1$，即 90% 用扩散模型采样、10% 用 GP 均值。

### 4. 总损失函数

$$\pi_h = \arg\min_{\theta_h} \underbrace{\mathcal{L}_{dm}(\theta_h)}_{\text{扩散}} + \psi \underbrace{\mathcal{L}_{gp}(\theta_h, \theta_{gp})}_{\text{GP正则}} + \eta \underbrace{\mathcal{L}_{dpg}(\theta_h)}_{\text{RL目标}}$$

其中 RL 目标为：$\mathcal{L}_{dpg}(\theta_h) = -\mathbb{E}_{s\sim\mathcal{D}_h, g^0\sim\pi_{\theta_h}} [Q_h(s, g^0)]$

超参数：$\psi = 10^{-3}$，$\eta = 5$，扩散步数 $N = 5$。

## 实验关键数据

### 实验设置

- **环境**：基于 MuJoCo 的 8 个连续控制任务（Reacher、Pusher、Point Maze、Ant Maze U/W-shape、Ant Fall、Ant FourRooms），含随机噪声变体
- **基线**：HLPS、SAGA、HIGL、HRAC、HIRO
- **评估**：10 次独立实验的平均成功率与 95% 置信区间

### 主要结果

| 对比维度 | 结果 |
|---------|------|
| vs 所有基线 | HIDI 在所有任务上一致超越，学习稳定性、样本效率、渐近性能均最优 |
| 扩散子目标（Baseline→HIDI-B） | 性能提升 ~15% |
| GP 正则化（HIDI-B→HIDI-A） | 样本效率提升 ~15%，性能提升 ~16% |
| 子目标选择（HIDI-A→HIDI） | 性能提升 ~7%-8% |
| 随机环境 | 在 Stochastic Ant Maze 等任务上优势更显著 |
| 子目标可达性 | 生成子目标与实际到达子目标的距离最小 |

### 消融分析

| 超参数 | 最优值 | 影响 |
|--------|--------|------|
| 扩散步数 $N$ | 5 | 3→7 表达能力递增，$N=5$ 平衡性能与计算 |
| 选择概率 $\varepsilon$ | 0.1 | 过大 (0.25) 导致不稳定，过小 (0.05) 收益减少 |
| RL 权重 $\eta$ | 5 | 增大加速早期训练，后期收敛 |
| GP 权重 $\psi$ | $10^{-3}$ | 过大限制扩散灵活性，过小退化为无 GP 版本 |

## 亮点与洞察

1. **扩散模型首次用于在线 HRL 子目标生成**：不同于离线 RL 中的扩散策略，本文在在线 off-policy HRL 中验证了扩散模型建模多模态子目标分布的优越性
2. **GP + 扩散的互补设计精巧**：GP 提供结构化先验和不确定性量化，扩散模型保证表达能力，两者在理论和实验上均形成有效互补
3. **理论保证充分**：提供了 GP 正则化引导子目标对齐的定理（Theorem 3.1）、梯度加权命题（Proposition 3.2）、单步遗憾界（Theorem 3.3）和策略改进保证（Proposition 3.4）
4. **子目标可达性可视化直观**：生成子目标与实际到达子目标的对比图清晰展示了方法优势，HIDI 的 gap 最小

## 局限性 / 可改进方向

1. **计算开销**：扩散模型的多步去噪 + GP 推理增加了高层决策延迟，尽管 $N=5$ 较小但仍比单步策略慢
2. **仅验证连续控制**：实验局限于 MuJoCo 导航/机械臂任务，缺少视觉输入丰富的高维环境实验（仅有简单 Image 变体）
3. **GP 稀疏近似的局限**：诱导点数量 $M$ 的选择和更新策略未深入讨论，对超大规模回放缓冲区的扩展性存疑
4. **与离线扩散 RL 的关系**：未与 Diffusion-QL 等在相同设置下对比，难以量化在线 vs 离线扩散策略的差异
5. **名称与领域分类**：虽然使用了扩散模型但本文核心贡献在 HRL/连续控制，与图像生成领域关联较弱

## 相关工作与启发

- **HIRO/HRAC/HIGL**：经典子目标空间约束方法，本文在此基础上用生成模型替代确定性策略
- **SAGA**：用 GAN 生成子目标，但存在训练不稳定和模式坍缩问题，HIDI 的扩散模型更稳定
- **Diffusion-QL**：离线 RL 中的扩散策略，证明扩散模型适合建模复杂动作分布，启发本文将其引入 HRL
- **HLPS**：同组前作，用 GP 学习子目标潜在空间，本文进一步将 GP 作为扩散模型的正则化先验

## 评分

- 新颖性: ⭐⭐⭐⭐ (扩散+GP 用于在线 HRL 子目标生成是新颖组合)
- 实验充分度: ⭐⭐⭐⭐ (8 个环境 + 丰富消融 + 理论分析，但缺视觉丰富任务)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，理论与实验结合好)
- 价值: ⭐⭐⭐⭐ (对 HRL 社区有实质贡献，扩散模型在 RL 中的应用值得关注)
