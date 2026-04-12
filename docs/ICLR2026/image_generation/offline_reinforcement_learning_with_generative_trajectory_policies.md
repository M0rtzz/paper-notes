---
title: >-
  [论文解读] Offline Reinforcement Learning with Generative Trajectory Policies
description: >-
  [ICLR 2026][图像生成][生成轨迹策略] 提出 Generative Trajectory Policy (GTP)，通过学习 ODE 完整解映射统一扩散、流匹配和一致性模型，配合分数近似和值驱动引导两项关键适配技术，在 D4RL 上达到 SOTA。
tags:
  - ICLR 2026
  - 图像生成
  - 生成轨迹策略
  - ODE 解映射
  - 一致性模型
  - 流匹配
  - D4RL
---

# Offline Reinforcement Learning with Generative Trajectory Policies

**会议**: ICLR 2026  
**arXiv**: [2510.11499](https://arxiv.org/abs/2510.11499)  
**代码**: 随论文附带  
**领域**: 离线强化学习 / 生成策略  
**关键词**: 生成轨迹策略, ODE 解映射, 一致性模型, 流匹配, D4RL

## 一句话总结

提出 Generative Trajectory Policy (GTP)，通过学习 ODE 完整解映射统一扩散、流匹配和一致性模型，配合分数近似和值驱动引导两项关键适配技术，在 D4RL 上达到 SOTA。

## 研究背景与动机

- 离线 RL 中生成式策略的核心矛盾：**表达力 vs 效率**
  - 扩散策略：强表达力但采样慢（需数百步迭代）
  - 一致性策略：快速单步生成但性能退化
- **关键洞察**：扩散、流匹配、一致性模型等可统一为连续时间 ODE 的解映射学习

## 方法详解

### 统一 ODE 框架

现代生成模型的底层 ODE：$\frac{d\boldsymbol{x}_t}{dt} = f(\boldsymbol{x}_t, t)$

流映射：$\Phi(\boldsymbol{x}_t, t, s) = \boldsymbol{x}_t + \int_t^s f(\boldsymbol{x}_\tau, \tau) d\tau$

重参数化函数：$\phi(\boldsymbol{x}_t, t, s) = \boldsymbol{x}_t + \frac{t}{t-s}\int_t^s f(\boldsymbol{x}_\tau, \tau) d\tau$

两个基本训练目标：

1. **瞬时流损失**（局部锚定）：$\lim_{s \to t} \phi(\boldsymbol{x}_t, t, s) = \boldsymbol{x}_t - tf(\boldsymbol{x}_t, t)$
2. **轨迹一致性损失**（全局连贯）：$\Phi(\boldsymbol{x}_t, t, s) \approx \Phi(\Phi(\boldsymbol{x}_t, t, u), u, s)$

### 关键适配 1：分数近似

**问题**：自引用监督导致计算昂贵且训练不稳定（类似 TD 学习的恶性循环）

**解决方案**：用闭式代理 $\tilde{f}(\boldsymbol{x}_t, t) = (\boldsymbol{x}_t - \boldsymbol{x})/t$ 替换学习的分数函数

**Theorem 1**：实用训练损失与理想损失之间的差异为 $O(h^p)$（$h$ 为步长，$p$ 为求解器阶数），且中间点可一步得到：$\boldsymbol{x}_u = \boldsymbol{x} + u \cdot \boldsymbol{z}$

### 关键适配 2：值驱动引导

**Theorem 2**：KL 正则化策略优化的最优解为 $\pi^*(a|s) \propto \pi_{BC}(a|s) \exp(\eta A(s,a))$

加权生成训练目标：

$$\max_\theta \mathbb{E}_{(s,a) \sim \mathcal{D}} [\exp(\eta A(s,a)) \cdot \ell_{\text{gen}}(\pi_\theta; a|s)]$$

实际实现中使用截断归一化优势权重：$w(s,a) = \exp\left(\eta \cdot \frac{\max(0, A(s,a))}{\text{std}(A) + \epsilon}\right)$

### GTP Actor-Critic 训练

- **Actor**：$\mathcal{L}_{\text{actor}} = \mathcal{L}_{\text{Consistency}} + \lambda_{\text{Flow}} \cdot \mathcal{L}_{\text{Flow}}$
- **Critic**：双 Q 网络 + EMA 目标网络
- **推理**：从高斯噪声出发，$K$ 步迭代 $a_{t_{i+1}} = \Phi_\theta(s, a_{t_i}, t_i, t_{i+1})$

## 实验关键数据

### D4RL 行为克隆性能

| 任务 | BC | D-BC | C-BC | GTP-BC |
|------|------|------|------|--------|
| halfcheetah-m | 42.6 | 45.4 | 31.0 | **48.6** |
| hopper-m | 52.9 | 65.3 | 71.7 | **83.7** |
| hopper-mr | 18.1 | 67.3 | 99.7 | **100.5** |
| **Gym 平均** | - | 76.3 | 69.7 | **82.3** |
| **AntMaze 平均** | - | 28.3 | 44.1 | **66.3** |

### D4RL 离线 RL 性能（部分关键任务）

| 任务 | IDQL | Diff-QL | CPQL | GTP |
|------|------|---------|------|-----|
| antmaze-large-play | 47.5 | 46.4 | 49.4 | **100.0** |
| antmaze-large-diverse | 45.9 | 36.0 | 42.0 | **100.0** |
| antmaze-ultra-play | 30.3 | 4.8 | 36.9 | **38.9** |

### 关键发现

1. GTP-BC 在纯行为克隆下已大幅超越扩散和一致性策略（AntMaze 平均: 66.3 vs 44.1）
2. 完整 GTP 在多个 AntMaze 任务上达到满分（100.0），远超先前方法
3. 使用 5 步采样即可达到高性能，解决了效率-表达力权衡
4. 分数近似消除了多步 ODE 积分的需求，训练稳定且高效

## 亮点与洞察

1. **统一视角深刻**：将扩散、流匹配、一致性模型等统一为 ODE 解映射学习
2. **理论基础扎实**：两个定理分别为分数近似和值引导提供了严格保证
3. **工程实用性强**：分数近似将训练从多步 ODE 求解简化为一步扰动
4. **性能显著提升**：在最具挑战性的 AntMaze 任务上取得突破性结果

## 局限性

- 需要与 critic 联合训练，增加了整体训练复杂度
- 分数近似的 $O(h^p)$ 界可能在极端步长下不够紧
- 仅在 D4RL 标准基准上验证，真实机器人环境未测试
- 超参数（$\lambda_{\text{Flow}}$, $\eta$, 采样步数 $K$）的选择可能影响性能

## 相关工作

- **生成策略**：Diffuser, Diffusion-QL, CPQL
- **一致性模型**：Consistency Models, CTM
- **离线 RL**：IQL, TD3+BC, AWAC

## 评分

- 新颖性：⭐⭐⭐⭐⭐ — 统一框架和 GTP 范式具有原创性
- 技术深度：⭐⭐⭐⭐⭐ — 理论推导严谨，定理证明完整
- 实验完整性：⭐⭐⭐⭐ — 全面的基准测试和消融分析
- 实用价值：⭐⭐⭐⭐ — AntMaze 满分成绩令人印象深刻
