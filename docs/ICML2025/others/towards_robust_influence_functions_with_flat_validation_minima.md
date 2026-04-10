# Towards Robust Influence Functions with Flat Validation Minima

## 元信息
- **会议**: ICML 2025
- **arXiv**: [2505.19097](https://arxiv.org/abs/2505.19097)
- **代码**: [GitHub](https://github.com/Virusdoll/IF-FVM)
- **领域**: 可解释AI / 训练数据影响
- **关键词**: 影响函数, 平坦极小值, SAM, 噪声标签检测, 数据影响

## 一句话总结
揭示影响函数(IF)在含噪数据上失效的根因在于验证损失的尖锐性而非参数估计精度，提出基于平坦验证极小值的新IF估计形式。

## 研究背景与动机
- 影响函数估计训练样本对模型预测的影响：$\mathcal{I}(z_{\text{tr}}; z_{\text{val}}) = g_{z_{\text{val}}}^\top H_{\text{tr}}^{-1} g_{z_{\text{tr}}}$
- 在含噪数据上表现差，且一阶/二阶参数变化近似均如此
- 现有研究聚焦于Hessian逆近似精度，忽略了损失变化估计的问题
- 关键洞察：尖锐验证极小值区域中，即使参数变化预测完美，IF仍不准确

## 方法详解

### 1. 影响估计误差上界（Theorem 3.2）
$$\mathcal{E}(\mathcal{I}) \leq \exp\left(-\frac{2\mu^2}{\hat{R}_{\text{val}}^\gamma(\theta)^2}\right)$$
其中 $\hat{R}_{\text{val}}^\gamma(\theta) = \max_{\|\Delta\| \leq \gamma} \hat{R}_{\text{val}}(\theta+\Delta)$

→ 误差由**验证集风险及其尖锐度**共同控制

### 2. 从ERM到SAM
求解平坦验证极小值：$\tilde{\theta} = \arg\min_\theta \hat{R}_{\text{val}}^\gamma(\theta)$
使用Sharpness-Aware Minimization (SAM)

### 3. 标准IF在平坦极小值上失效
原因两点：
- 收敛模型梯度趋近零 → $\mu \to 0$ → 上界失效
- 参数变化估计与平坦极小值的对齐不当

### 4. 新IF形式
- 使用**二阶近似**替代一阶（缓解梯度消失）
- 设计针对平坦极小值的**参数变化估计方法**
- 在SAM训练过的验证集极小值上计算影响

## 实验

### 噪声标签检测（CIFAR-10N "worst"）
| 方法 | AUC |
|------|-----|
| 标准IF (LiSSA) | 随验证精度变化 |
| 标准IF (TracIn) | 同上 |
| 标准IF + SAM | 退化 |
| **本文IF + SAM** | 持续改善 |

标准IF在SAM优化时AUC反而下降（Figure 3a），本文IF在SAM下持续上升。

### 核心观察
- IF性能与验证集准确率高度相关（Figure 2）
- 标准IF在SAM调优过程中，干净样本的影响值趋向零（Figure 3b）
- 本文IF保持有效区分度

## 亮点
- 颠覆了"IF失败源于Hessian逆不准确"的传统认知
- 建立了IF误差与验证风险尖锐度的理论联系
- 提出的新IF形式直接面向噪声数据场景设计
- 理论与实验高度一致

## 局限性
- SAM训练验证集增加额外计算成本
- 上界中 $\mu$ 的经验估计可能不稳定
- 对非噪声数据场景的改善程度待验证
- 二阶IF形式比一阶更复杂，可能限制大规模应用

## 评分
⭐⭐⭐⭐ 识别了被忽视的核心失败模式，理论分析与实验诊断配合精准，为IF的实际应用提供了关键改进。
