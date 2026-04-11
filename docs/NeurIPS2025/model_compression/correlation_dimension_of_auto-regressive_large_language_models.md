---
description: "【论文笔记】Correlation Dimension of Auto-Regressive Large Language Models 论文解读 | NeurIPS 2025 | arXiv 2510.21258 | 相关维数 | 引入源于分形几何的**相关维数（correlation dimension）**作为衡量自回归语言模型感知文本复杂度的指标，揭示了传统 perplexity 无法捕捉的长程结构特性，可检测幻觉和退化文本。"
tags:
  - NeurIPS 2025
---

# Correlation Dimension of Auto-Regressive Large Language Models

**会议**: NeurIPS 2025  
**arXiv**: [2510.21258](https://arxiv.org/abs/2510.21258)  
**代码**: 无  
**领域**: model_compression  
**关键词**: 相关维数, 分形几何, 语言模型评估, 自回归模型, 文本复杂度

## 一句话总结

引入源于分形几何的**相关维数（correlation dimension）**作为衡量自回归语言模型感知文本复杂度的指标，揭示了传统 perplexity 无法捕捉的长程结构特性，可检测幻觉和退化文本。

## 研究背景与动机

大语言模型（LLM）在低 perplexity 下仍然会出现重复、不连贯和幻觉等问题，说明 perplexity 仅衡量局部预测准确度，忽略了长程结构复杂性。现有评估指标分为两类：
1. **局部指标**（如 n-gram 频率）：可解释但缺乏语义深度
2. **全局指标**（如平均 perplexity）：全面但难以解释

两者之间存在断层，急需一种能**桥接微观（token 级）和宏观（长程结构）**视角的指标。相关维数来源于动力系统理论，量化自相似性——复杂系统跨尺度不变模式的基本特征。

## 方法详解

### 整体框架

在自回归 LLM 中，文本被表示为 next-token 对数概率向量序列。通过计算这些向量间的欧氏距离来定义 recurrence（回归），进而估计相关维数。

### 关键设计

**相关维数定义**：给定无穷序列 $\{x_t\}_{t=1}^\infty$，相关积分 $S(\varepsilon)$ 定义为距离小于 $\varepsilon$ 的点对频率：

$$S(\varepsilon) = \lim_{t \to \infty} \frac{2}{t(t-1)} \sum_{1 \leq i < j \leq t} \mathbf{1}\{\|x_i - x_j\| < \varepsilon\}$$

相关维数 $d$ 是 $S(\varepsilon)$ 关于 $\varepsilon$ 的幂律缩放指数：

$$S(\varepsilon) \propto \varepsilon^d \quad \text{as} \quad \varepsilon \to 0$$

**对数概率向量表示**：时刻 $t$ 处的表示为：

$$x_t(\omega) = \log P_\theta(\omega_t = \omega | \omega_{t-c}, \cdots, \omega_{t-1}), \quad \forall \omega \in \Omega$$

其中 $\Omega$ 为词表，默认上下文长度 $c = \infty$。

**文本跳跃（Textual Skips）**：若两个状态 $x_t$ 和 $x_s$ 接近，则文本段 $[s, t)$ 可被省略而不显著改变后续生成。这种 recurrence 在多尺度上出现——从局部单词跳跃到全局句子级跳跃。

### 损失函数

本文不涉及训练，相关维数是一个纯推理时计算的诊断指标。计算开销仅略高于 perplexity 计算，可集成到 vLLM 等推理框架中。

## 实验关键数据

### 主实验

**多模型相关维数收敛**（Stanford Encyclopedia of Philosophy 数据集）：

| 模型 | 参数量 | Perplexity | 相关维数 |
|------|--------|-----------|---------|
| GPT-2 Small | 124M | 高 | ~8.5 |
| GPT-2 XL | 1.5B | 中 | ~7.5 |
| Pythia-12B | 12B | 低 | ~6.5 |
| OpenLLaMA-13B | 13B | 低 | ~6.5 |
| Falcon3 | — | 低 | ~6.5 |
| Mamba | — | 低 | ~6.5 |

随着 perplexity 下降，相关维数收敛到约 6.5，且跨架构（Transformer、Mamba）一致。

**复杂度谱**：
- 随机打乱文本：相关维数 > 10
- 自然语言文本：~6-7
- 编程语言（Python/Java/C）：~5
- Polya urn 自增强过程：< 2

### 消融实验

- 时延嵌入（$k > 1$）与单步对数概率（$k = 1$）的相关维数无显著差异，说明单步概率已编码充分的长程信息
- 上下文窗口限制实验：随着上下文长度缩短，相关维数降低，反映模型对长程依赖的感知减弱
- 模型量化（降至 4-bit）后相关维数保持稳定

### 关键发现

1. **预训练三阶段**：相关维数揭示了预训练过程中三个不同阶段——初始学习、结构涌现、稳定化——这在 perplexity 曲线中不可见
2. **幻觉指示**：在知识密集型文本上，不同模型的相关维数出现显著分歧，而高分歧与幻觉倾向正相关
3. **退化检测**：可检测多种退化形式——重复（低维数）、不连贯（高维数）、平淡（低维数）

## 亮点与洞察

1. **理论优雅**：首次将分形几何中的相关维数应用于 LLM 行为分析，建立了从 token 级回归到全局文本复杂度的统一框架
2. **实用性强**：计算开销极低，可在推理时直接集成，不需要参考文本
3. 发现单步 next-token 概率已隐含编码长程结构信息，与知识蒸馏中的观察呼应
4. 跨架构适用（Transformer + Mamba），跨语言一致

## 局限性

- 相关维数依赖模型质量，模型不够好时度量的是"模型感知的复杂度"而非文本本身的复杂度
- 稀有 token 的对数概率变化大但对 loss 贡献小，可能影响相关维数估计
- 未直接与人类评估对齐，作为评估指标的自洽性需更多验证

## 相关工作与启发

- 与 alabdulmohsin2024fractal 的分形维数方法相比，本文度量的是**生成过程的回归结构**而非预测误差序列的长程依赖
- 与 Zipf 定律等统计自相似现象形成互补视角
- 启发思考：相关维数能否用于指导采样策略选择（如何时切换 nucleus/beam search）

## 评分

- ⭐ 新颖性: 5/5 — 将分形几何引入 LLM 分析，视角独特且理论扎实
- ⭐ 实验充分度: 4/5 — 多模型多数据集验证充分，但缺乏与人类评估的对齐实验
- ⭐ 写作质量: 5/5 — 兼顾数学严谨性和直觉解释，图表出色
- ⭐ 价值: 4/5 — 开辟了 LLM 评估的新方向，实际应用仍需探索
