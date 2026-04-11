---
description: "【论文笔记】Retaining Suboptimal Actions to Follow Shifting Optima in Multi-Agent RL 论文解读 | ICLR 2026 | arXiv 2602.17062 | 多Agent RL | 提出S2Q解决合作MARL中值函数最优点在训练中漂移→次优收敛：逐步学习K个sub-value函数保留替代高价值动作+Softmax行为策略持续探索→最优变化时快速适应，SMAC Hard+和GRF上一致超越基线。"
tags:
  - ICLR 2026
---

# Retaining Suboptimal Actions to Follow Shifting Optima in Multi-Agent RL

**会议**: ICLR 2026  
**arXiv**: [2602.17062](https://arxiv.org/abs/2602.17062)  
**代码**: [GitHub](https://github.com/hyeon1996/S2Q)  
**领域**: 多Agent RL/值分解  
**关键词**: 多Agent RL, 值分解, 次优动作保留, Softmax行为策略, S2Q, CTDE

## 一句话总结
提出S2Q解决合作MARL中值函数最优点在训练中漂移→次优收敛：逐步学习K个sub-value函数保留替代高价值动作+Softmax行为策略持续探索→最优变化时快速适应，SMAC Hard+和GRF上一致超越基线。

## 研究背景与动机

1. **领域现状**：CTDE下值分解(QMIX/WQMIX)是合作MARL核心。QMIX单调性约束确保IGM但限制表达。

2. **现有痛点**：
   - (1) QMIX单调性→无法表示非单调值函数
   - (2) WQMIX用无约束Q*改进但仍依赖单一最优→最优漂移时无法适应
   - (3) 大联合动作空间ε-greedy→联合探索概率指数衰减
   - (4) 替代高价值动作信息被丢弃后无法恢复

3. **切入角度**：显式保留次优动作→值函数景观变化时可利用→快速适应。

## 方法详解

### 整体框架
S2Q在WQMIX上训练K+1个sub-value函数：Q_0=Q_tot选最优，Q_k选第k次优(抑制前k-1个)。Softmax行为策略在候选间采样。

### 关键设计

1. **逐步学习(Eq.2)**：Q_k的TD目标抑制前k-1已识别动作的值→自然学到下一个。Theorem 4.1保证alpha足够大时Q_k准确选第k次优联合动作。

2. **Softmax行为策略(Eq.4)**：P_t=Softmax(Q*(s,tau,a_k*)/T)→先采样k→用ε-greedy执行Q_k→围绕有前途次优探索。T=0.1最优。

3. **训练时通信协调**：Encoder-Decoder: z_t=E(tau), (s_hat,P_hat)=D(z)→agent同步采样同一k。**评估时不需通信**→Q_0的greedy即可。

### 训练策略
- Q*按WQMIX目标训练；{Q_k}按抑制目标训练；最优K=2,T=0.1

## 实验关键数据

### SMAC-Hard+(6场景)+GRF(2场景)
- S2Q一致超越QMIX/WQMIX/DOP/FOP/PAC/RiskQ/MARR/MASIA
- 6h_vs_8z和3s5z_vs_3s6z上优势最显著(探索密集型)

### SMAC-Comm(4通信任务)
- S2Q-Comm在5z_vs_1ul和bane_vs_hM大幅领先
- vs QMIX-Comm→提升来自次优学习非仅通信

### 组件消融(Table 1, SMAC-Hard+平均胜率)

| 方法 | 胜率(%) |
|------|---------|
| S2Q | **73.43+-5.29** |
| S2Q_oracle | 77.47+-4.32 |
| S2Q_no_soft | 55.17+-6.71 |
| S2Q_random | 48.05+-9.37 |
| S2Q_independent | 46.22+-8.20 |
| QMIX | 43.94+-10.06 |

### 超参(Figure 8)
- K={0,1,2,3}: K=2最优(~70%), K=0失败, K=3方差大
- T={0.01,0.1,0.2,1.0}: T=0.1最优, S2Q对T不太敏感

### 关键发现
- S2Q_no_soft(55) vs S2Q(73)→Softmax执行是核心(仅保留不够要执行)
- S2Q_random(48) vs S2Q(73)→按Q*优先级远优于均匀
- S2Q_independent(46)→不协调→崩塌→通信协调必要
- 轨迹：6h_vs_8z中move→hit转变→S2Q检测shift并快速适应
- SMACv2/SMAC-Hard(混合对手)中S2Q也一致最优→随机性鲁棒

## 亮点与洞察
- **次优保留**：显式track多候选→不丢弃信息→最优漂移可切换
- **Softmax替代ε-greedy**：围绕有前途动作探索→指数衰减问题优雅解决
- **评估无需通信**：Q_0足够→通信仅训练时协调→实用优势
- **理论保证**：Theorem 4.1精确保证次优识别→非纯启发式
- **通用性**：可搭配VDN/QPLEX等其他CTDE方法

## 局限性
- 多sub-value网络增加计算/内存(分析表明开销适中)
- 温度T需调(但分析表明不敏感)
- 主要SMAC/GRF验证→更复杂环境待测
- K值选择需人工设定→自适应K未探索
- 当前的suppression常数alpha需足够大→过大可能导致数值不稳定
- sub-value函数共享同一mixing架构→更灵活的架构设计未探索
- 在连续动作空间环境中的扩展性未验证

## 相关工作与启发
- WQMIX→Q*改进但仍单最优→S2Q扩展
- 探索方法(RND/ICM→单agent)→S2Q用次优保留做多agent探索
- 通信方法(MASIA/NDQ/CAMA)→S2Q通信为可选插件
- 启发：动态环境中保留多元策略候选比单最优追踪更鲁棒
- 启发：Softmax行为策略的思想可推广到其他探索与利用问题

## 评分
- 新颖性: ⭐⭐⭐⭐ 次优保留+Softmax行为的新颖组合
- 技术深度: ⭐⭐⭐⭐ 理论保证+完整算法框架
- 实验充分度: ⭐⭐⭐⭐⭐ SMAC/GRF/SMACv2+全面消融
- 实用性: ⭐⭐⭐⭐ 评估无通信+可搭其他CTDE
- 综合: ⭐⭐⭐⭐ 合作MARL的实用改进+理论支撑
