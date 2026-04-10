# Towards Attributions of Input Variables in a Coalition

## 元信息
- **会议**: ICML 2025
- **arXiv**: [2309.13411](https://arxiv.org/abs/2309.13411)
- **代码**: 无
- **领域**: 可解释AI / 归因方法
- **关键词**: Shapley值, AND-OR交互, 联盟归因, 归因冲突, 博弈论

## 一句话总结
从AND-OR交互的角度揭示联盟归因与个体变量归因之间的冲突本质，定义了正式的联盟归因指标并提出三种评估联盟忠实度的度量。

## 研究背景与动机
- 归因方法的基本挑战：如何划分输入变量？取像素还是区域？取词还是token？
- **归因冲突**：联盟 $S$ 的归因 $\varphi(S) \neq \sum_{i \in S} \phi(i)$
- 现有方法（Faith-Shap等）通过工程方法强行消除冲突，缺乏理论解释
- 需要理解冲突的数学根源，而非消除它

## 方法详解

### 1. Shapley值的交互分解（Theorem 3.2）
$$\phi(i) = \sum_{S \subseteq N, i \in S} \frac{1}{|S|}[I_{\text{and}}(S) + I_{\text{or}}(S)]$$
Shapley值是将AND-OR交互效应均匀分配给参与变量的结果。

### 2. 联盟归因定义（Eq. 6）
$$\varphi(S) = \sum_{T \supseteq S} \frac{|S|}{|T|}[I_{\text{and}}(T) + I_{\text{or}}(T)]$$
仅包含完全涵盖联盟 $S$ 的交互 $T \supseteq S$。

### 3. 冲突的根源（Theorem 3.4）
$$\sum_{i \in S} \phi(i) = \underbrace{\varphi(S)}_{\text{shared}} + \underbrace{\sum_{\substack{T: T\cap S \neq \emptyset \\ T\cap S \neq S}} \frac{|T\cap S|}{|T|}[I_{\text{and}}(T)+I_{\text{or}}(T)]}_{\text{conflict}}$$

冲突来自仅包含联盟 $S$ 部分（而非全部）变量的交互。

### 4. 无冲突条件（Corollary 3.5）
若DNN不编码仅含 $S$ 部分变量的交互，则 $\varphi(S) = \sum_{i \in S} \phi(i)$。

### 5. 联盟忠实度度量（三种度量）
基于冲突项大小评估联盟划分的合理性。

## 实验

### 验证实验
| 验证内容 | 误差量级 |
|---------|---------|
| Theorem 3.6逼近 $\phi(i)$ | $\sim 10^{-7}$ |
| Corollary 3.8逼近 $v(N)$ | $\sim 10^{-7}$ |

### 应用场景
- **合成数据**：验证理论正确性
- **NLP**：token分组为word的联盟忠实度与人类直觉一致
- **图像分类**：像素区域联盟评估
- **围棋**：棋子组合的联盟归因与围棋定式理解一致

## 亮点
- 首次从数学上清晰解释归因冲突的本质原因
- 联盟归因满足匿名性、对称性、可加性、dummy、效率五大公理
- 与Shapley值完全兼容：单变量联盟退化为Shapley值
- 围棋应用展示了发现新定式解读的潜力

## 局限性
- AND-OR交互的提取依赖LASSO优化，有近似误差
- 交互数量指数级增长，实际计算受限于变量数
- 联盟忠实度度量的实用决策阈值缺乏指导
- 仅在相对小规模模型上验证

## 评分
⭐⭐⭐⭐ 理论贡献扎实，首次揭示归因冲突的交互根源，为输入变量划分问题提供了原则性指导。
