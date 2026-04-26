---
title: >-
  [论文解读] AutoQD: Automatic Discovery of Diverse Behaviors with Quality-Diversity Optimization
description: >-
  [ICLR 2026][质量多样性优化] 本文提出 AutoQD，利用策略占据测度（occupancy measure）的随机傅里叶特征嵌入自动生成行为描述符，无需手工设计即可在连续控制任务中发现多样化高质量策略，并在 6 个标准环境中证明了有效性。
tags:
  - ICLR 2026
  - 质量多样性优化
  - 行为描述符
  - 占据测度
  - 随机傅里叶特征
  - 策略嵌入
---

# AutoQD: Automatic Discovery of Diverse Behaviors with Quality-Diversity Optimization

**会议**: ICLR 2026  
**arXiv**: [2506.05634](https://arxiv.org/abs/2506.05634)  
**代码**: [GitHub](https://github.com/conflictednerd/autoqd-code)  
**领域**: 强化学习  
**关键词**: 质量多样性优化, 行为描述符, 占据测度, 随机傅里叶特征, 策略嵌入

## 一句话总结
本文提出 AutoQD，利用策略占据测度（occupancy measure）的随机傅里叶特征嵌入自动生成行为描述符，无需手工设计即可在连续控制任务中发现多样化高质量策略，并在 6 个标准环境中证明了有效性。

## 研究背景与动机

1. **领域现状**: Quality-Diversity (QD) 优化旨在发现既高性能又行为多样的策略集合，已在机器人运动、游戏生成等领域取得成功。

2. **现有痛点**: QD 算法严重依赖手工设计的行为描述符（如双足机器人的脚接触模式），需要大量领域知识，且预定义的多样性维度可能遗漏有趣的行为变体。

3. **核心矛盾**: 现有无监督 QD 方法（如 AURORA）使用自编码器重建状态来学习行为空间，但缺乏与策略行为的理论联系。RL 中的技能发现方法（如 DIAYN）需预设技能数量且不优化任务奖励。

4. **本文目标**: 提供一种理论有据的方法自动生成行为描述符，无需领域知识或预设技能数量。

5. **切入角度**: 在标准假设下，策略与其占据测度（occupancy measure）存在一一对应关系，因此占据测度是策略行为的完整刻画。

6. **核心 idea**: 用随机傅里叶特征嵌入占据测度，使嵌入距离近似 MMD 距离，再通过 PCA 降维得到行为描述符。

## 方法详解

### 整体框架
输入为 MDP 环境，输出为包含多样高质量策略的 archive。流程：收集策略轨迹→用随机傅里叶特征嵌入策略→加权 PCA 降维为低维行为描述符→CMA-MAE 进行 QD 优化→周期性更新描述符。

### 关键设计

1. **策略嵌入（Policy Embedding via RFF）**:
    - 功能: 将策略映射到欧氏空间，使距离反映行为差异
    - 核心思路: 定义 D 维随机特征映射 $\phi(s,a) = \sqrt{2/D}[\cos(\mathbf{w}_1^T[s;a]+b_1),...,\cos(\mathbf{w}_D^T[s;a]+b_D)]$，策略嵌入 $\psi^\pi = \frac{1}{n}\sum_j(1-\gamma)\sum_t\gamma^t\phi(s_t^j,a_t^j)$。定理证明 $\|\psi^{\pi_1}-\psi^{\pi_2}\| \approx MMD(\rho^{\pi_1},\rho^{\pi_2})$ 以高概率成立
    - 设计动机: MMD 配合高斯核是占据测度空间上的合法度量，RFF 提供计算高效的有限维近似

2. **行为描述符提取（cwPCA）**:
    - 功能: 将高维嵌入降至 k 维行为描述符
    - 核心思路: 对 archive 中策略嵌入进行加权 PCA（按 fitness 加权），使更好策略对主成分方向有更大影响。再做校准使投影落在 [-1,1] 范围内
    - 设计动机: 偏向高质量策略的行为变异探索；PCA 捕获最显著的行为差异维度

3. **迭代算法（AutoQD）**:
    - 功能: 交替进行 QD 优化和描述符更新
    - 核心思路: 在更新调度时间点重新计算 archive 中所有策略嵌入，更新仿射变换参数 $\mathbf{A},\mathbf{b}$，然后继续 CMA-MAE 优化
    - 设计动机: 随着探索进行，行为空间的主要变异方向可能改变，需要动态更新

### 损失函数 / 训练策略
- 黑盒优化：CMA-MAE（无梯度）
- 策略参数化：Toeplitz 矩阵减少参数量
- 核宽度 σ 使用中位数启发式
- 嵌入维度 D 设为与状态-动作维度相关的适当大小

## 实验关键数据

### 主实验

| 环境 | 指标 | AutoQD | RegularQD (手工) | 最佳基线 | 
|------|------|--------|-----------------|---------|
| Ant | GT QD (×10⁴) | **361.43** | 182.58 | 19.24 |
| HalfCheetah | GT QD (×10⁴) | **30.78** | 24.91 | 11.38 |
| Hopper | qVS | **1.94** | 1.35 | 1.81 |
| Swimmer | VS | **16.92** | 4.67 | 7.21 |
| BipedalWalker | GT QD (×10⁴) | **6.09** | 1.81 | 3.36 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 无 fitness 加权 PCA | 性能下降 | 低质量策略干扰主成分方向 |
| 不同 k 值 | k=2 通常最优 | 更高维度 archive 难以填充 |

### 关键发现
- AutoQD 在 6 个环境中的 5 个上超越手工描述符方法
- HalfCheetah 和 Walker2d 上表现略弱，因发现了"滑行"等低奖励但多样的行为
- 适应性实验：改变摩擦/质量时，AutoQD 的策略集保持更高鲁棒性- 在Ant环境中的GT QD指标达到361.43（×10⁴），远超手工描述符的182.58，显示了自动描述符的巨大优势
- 无fitness加权的PCA导致低质量策略干扰主成分方向，证实了cwPCA设计的必要性

## 亮点与洞察
- 理论严谨：从占据测度到 MMD 到 RFF 的数学推导链完整
- 自动发现的行为描述符可能揭示手工描述符遗漏的有趣行为变体
- 与 CMA-MAE 的结合使得方法可扩展到连续高维行为空间
- 策略嵌入技术可复用于模仿学习、逆强化学习等其他场景
- 占据测度作为策略行为的完整刻画这一理论基础，为方法提供了比AURORA等基于自编码器的方法更强的理论保证

## 局限与展望
- 高随机性环境中准确估计策略嵌入需要大量轨迹
- 低维行为描述符可能导致探索集中在简单稳定行为上
- 核带宽固定，动态调整可能在不同学习阶段更好捕获行为差异
- 未与梯度 QD 方法（PGA-MAP-Elites、PPGA）结合
- 轨迹数量对嵌入质量的影响的理论下界在实践中可能偏严格，实际所需轨迹数可能更少
- 在高维状态-动作空间（如人形机器人控制）上的可扩展性有待验证
- 描述符更新频率的选择对最终多样性有显著影响，但缺乏自动调整策略

## 相关工作与启发
- **vs AURORA**: AURORA 用自编码器学习状态表征作为描述符，缺乏与策略行为的理论联系
- **vs DIAYN**: DIAYN 最大化技能-状态互信息，需预设技能数且不考虑任务奖励
- **vs DvD-ES**: DvD-ES 通过随机状态下的动作差异刻画策略，缺乏 AutoQD 的理论保证
- 占据测度的理论基础为QD优化提供了比启发式方法更稳固的根基
- 在机器人运动生成和游戏场景设计等下游应用中有直接价值
- 与RL中的内在动机探索方法的关系值得进一步探索
- 可探索在非平稳环境中动态更新行为描述符的策略

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 占据测度嵌入作为行为描述符是理论优美的创新
- 实验充分度: ⭐⭐⭐⭐ 6 个环境 5 个基线 3 个指标
- 写作质量: ⭐⭐⭐⭐ 理论与实验结合紧密
- 价值: ⭐⭐⭐⭐ 对 QD 优化和开放式学习有重要推动

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] Post-training Large Language Models for Diverse High-Quality Responses](post-training_large_language_models_for_diverse_high-quality_responses.md)
- [\[ICLR 2026\] SUSD: Structured Unsupervised Skill Discovery through State Factorization](susd_structured_unsupervised_skill_discovery_through_state_factorization.md)
- [\[ICLR 2026\] AutoTool: Automatic Scaling of Tool-Use Capabilities in RL via Decoupled Entropy Constraints](autotool_scaling_tool_use.md)
- [\[ICLR 2026\] Rethinking Policy Diversity in Ensemble Policy Gradient in Large-Scale Reinforcement Learning](rethinking_policy_diversity_in_ensemble_policy_gradient_in_large-scale_reinforce.md)
- [\[ICLR 2026\] Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity](whatever_remains_must_be_true_filtering_drives_reasoning_in_llms_shaping_diversi.md)

<!-- RELATED:END -->
