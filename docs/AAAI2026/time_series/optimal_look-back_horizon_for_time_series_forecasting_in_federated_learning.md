# Optimal Look-back Horizon for Time Series Forecasting in Federated Learning

**会议**: AAAI2026
**arXiv**: [2511.12791](https://arxiv.org/abs/2511.12791)
**代码**: 无
**领域**: time_series
**关键词**: time series forecasting, federated learning, look-back horizon, intrinsic space, Bayesian loss

## 一句话总结
提出联邦学习场景下时间序列预测的最优 look-back horizon 理论框架：通过 Synthetic Data Generator (SDG) 建模 non-IID 客户端数据，构建 intrinsic representation space，证明预测损失可分解为 Bayesian loss（随 $H$ 递减并饱和）和 approximation loss（随 $H$ 递增），最优 horizon $H^*$ 为 Bayesian loss 开始饱和的最小值。

## 研究背景与动机
Look-back horizon（回看窗口长度 $H$）是时间序列预测的核心超参数，直接影响模型复杂度和预测精度。

现有不足：
- 传统方法（ARIMA 用 AIC/BIC）有强线性假设，现代深度模型（LSTM、Transformer）仅靠交叉验证经验调参
- Shi et al. (2024) 提出的 scaling law 理论假设集中式 IID 数据，不适用于联邦学习场景
- 联邦学习中数据分散、non-IID、异构，全局固定 $H$ 可能与各客户端局部动态不匹配

核心问题：如何在联邦学习的 non-IID 环境下，为时间序列预测提供有理论保证的自适应 horizon 选择准则？

## 方法详解

### Synthetic Data Generator (SDG)
对客户端 $k$ 的观测值建模为加性结构：
$$\hat{x}_{f,t,k} = \sum_{j=1}^{J} A_{f,j,k} \sin\left(\frac{2\pi t}{T_{f,j,k}} + \theta_{f,j,k}\right) + \sum_{i=1}^{p} \phi_{k,i} x_{f,t-i,k} + \beta_{f,k} t + \epsilon_{f,t,k}$$
包含季节性（多正弦分量）、AR 依赖、线性趋势和高斯噪声，并通过仿射变换模拟 feature skew。

### Intrinsic Space 构建
五步变换将 non-IID 时间序列映射到 intrinsic space：
1. 客户端级归一化消除 feature skew
2. 窗口展平为固定长度向量
3. 全局协方差矩阵特征分解
4. 基于 SDG 估计 intrinsic dimension：$d_{I,k}(H) \approx F \cdot (\min\{H, \ell_{AR,k}\} + g_k(H) + 1)$
5. 投影到主成分空间

满足 6 个结构假设：紧致性、bi-Lipschitz 连续性、维度单调饱和等。

### Loss 分解
**Theorem 1 (Federated Loss Decomposition)**：
$$L(H,S;m) = L_{Bayes}(H,S) + L_{approx}(H,S;m)$$
- **Bayesian loss**：不可约误差，随 $H$ 递减（更多历史改善季节性/趋势识别），最终饱和
- **Approximation loss**：模型有限容量 + 有限样本导致的误差，随 $H$ 递增（intrinsic dimension 增大、有效样本减少）

**Theorem 2**：Bayesian loss 进一步分解为 AR、seasonal、trend 三个分量。

**Theorem 3**：Approximation loss 有 intrinsic-dimension 相关上界：
$$L_{approx}^{(k)} \lesssim (K_2^2 d_{I,k}^2)^{\frac{d_{I,k}}{4+d_{I,k}}} + \left(\frac{d_{I,k} H}{D_k}\right)^{\frac{4}{4+d_{I,k}}}$$

### 最优 Horizon
**Theorem 4 (Unimodality)**：总损失关于 $H$ 是单峰函数，最小值在 smallest sufficient horizon：
$$H_k^*(\delta) = \min\{H : |\Delta L_{Bayes}^{(k)}(H)| \le \delta\}$$

**Corollary 1**：可通过季节覆盖率 $\tau$ 实际计算：$H_k^*(\delta) = \max\{\ell_{AR,k}, T_k^{(\tau)}\}$

联邦聚合使用 weighted trimmed mean 对各客户端最优 horizon 做鲁棒汇总。

## 实验关键数据

- **SDG 验证**：在 Jena 2020 气温数据上，合成数据与真实数据在均值差 ($3.6 \times 10^{-3}$)、ACF $L^2$ gap ($3.7 \times 10^{-6}$)、PSD gap ($8.2 \times 10^{-3}$) 上高度一致
- 本文为理论工作，核心贡献是可证明的最优 horizon 定理而非实验 benchmark

## 亮点
- **首个联邦 TSF 的 horizon 选择理论**：将 Shi et al. 的 centralized IID 理论扩展到 federated non-IID 场景
- **严格的 loss 分解与单峰性证明**：Bayesian loss 递减饱和 + approximation loss 递增 → 总 loss 单峰，最优 horizon 有明确定义
- **可解释的 horizon 计算**：通过 AR memory $\ell_{AR,k}$ 和季节覆盖 $T_k^{(\tau)}$ 直接计算，无需 grid search
- **鲁棒联邦聚合**：weighted trimmed mean 避免极端客户端主导全局 horizon

## 局限性 / 可改进方向
- SDG 模型为加性结构，无法处理 regime switching、非线性季节性、跨特征交互等复杂模式
- 假设局部平稳和稳定 AR 结构，在 long-memory 或 near-unit-root 序列上可能不适用
- 联邦场景下全局协方差估计需要安全聚合机制，隐私问题未深入讨论
- 重叠窗口的独立性近似可能高估有效样本量
- 缺少大规模实证实验验证理论预测与实际最优 horizon 的吻合度

## 评分
- 新颖性: ⭐⭐⭐⭐ — 首次为联邦 TSF 的 horizon 选择提供理论基础，填补重要空白
- 实验充分度: ⭐⭐⭐ — 理论贡献突出但实验验证偏弱，仅有 SDG 验证
- 写作质量: ⭐⭐⭐⭐ — 数学推导严谨，定理结构清晰
- 价值: ⭐⭐⭐⭐ — 为联邦时序预测的模型设计提供了原则性指导


