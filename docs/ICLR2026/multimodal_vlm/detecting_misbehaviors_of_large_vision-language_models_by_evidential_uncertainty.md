# Detecting Misbehaviors of Large Vision-Language Models by Evidential Uncertainty Quantification

**会议**: ICLR2026  
**arXiv**: [2602.05535](https://arxiv.org/abs/2602.05535)  
**代码**: 待确认  
**领域**: 多模态VLM  
**关键词**: LVLM uncertainty, evidential reasoning, Dempster-Shafer, misbehavior detection, hallucination

## 一句话总结
提出 EUQ（Evidential Uncertainty Quantification），基于 Dempster-Shafer 证据理论将 LVLM 的认识不确定性分解为冲突（CF，内部矛盾）和无知（IG，信息缺失），单次前向传播即可检测幻觉、越狱、对抗攻击和 OOD 失败四类错误行为，AUROC 相对提升最高 10.5%。

## 研究背景与动机

1. **领域现状**：LVLM 在困难/分布外输入下会产生幻觉、越狱响应、对抗脆弱性和 OOD 失败等错误行为。现有不确定性量化方法多关注总体预测不确定性。
2. **现有痛点**：(a) 贝叶斯方法计算成本太高无法应用于 LVLM；(b) 采样方法（语义熵等）需多次推理；(c) 现有方法无法区分不确定性的来源——是内部矛盾还是知识缺失。
3. **核心洞察**：幻觉主要源于高内部冲突（模型同时有支持和反对的证据），OOD 失败源于高无知（缺乏相关知识）。
4. **核心idea**：从 LVLM output head 的 pre-logits 特征中提取正/负证据，用 Dempster 规则融合后分别计算冲突和无知。

## 方法详解

### 整体框架
LVLM 单次前向推理 → 提取 output head 的 pre-logits 特征 $\mathbf{Z}$ → 最小承诺原则计算证据权重 $\mathbf{E}$ → 分解为正（支持）/负（反对）证据 → Dempster 融合 → 输出冲突 CF 和无知 IG。

### 关键设计

1. **证据权重闭式估计（Lemma 1）**:
   - 用仿射变换 $\mathbf{E} = \mathbf{A} \odot \mathbf{Z}^\top + \mathbf{B}$ 从 pre-logits 构造证据
   - 最小承诺原则约束下闭式解 $\mathbf{A}^* = W - \mu_0(W)$
   - 分解为 $\mathbf{E}^+$（支持）和 $\mathbf{E}^-$（反对）

2. **Dempster 融合计算 CF 和 IG**:
   - CF = 正负证据间的冲突度 $\kappa$（高 CF = 模型内部矛盾）
   - IG = 融合后分配给全集 $\mathcal{H}$ 的质量（高 IG = 模型缺乏知识）
   - 完全无需训练，单次前向传播

3. **Misbehavior-Bench**:
   - 涵盖 4 类错误行为：幻觉、越狱、对抗攻击、OOD 失败
   - 评估 4 个 SOTA LVLM：DeepSeek-VL2-Tiny、Qwen2.5-VL-7B、InternVL2.5-8B、MoF-7B

## 实验关键数据

### 主实验（AUROC）

| 方法 | 幻觉 | 越狱 | 对抗 | OOD | 说明 |
|------|------|------|------|-----|------|
| Token Entropy | 基线 | 基线 | 基线 | 基线 | 总体不确定性 |
| Semantic Entropy | 中等 | 中等 | 中等 | 中等 | 需多采样 |
| **EUQ-CF** | **+10.4%** | 高 | 高 | 中等 | 检测幻觉最佳 |
| **EUQ-IG** | 中等 | 高 | 高 | **+7.5%** | 检测 OOD 最佳 |

### 关键发现
- **幻觉 ↔ 高冲突**：模型有矛盾的内部证据→产生幻觉
- **OOD ↔ 高无知**：缺乏相关知识→无法处理分布外输入
- **层级动态分析**：CF 和 IG 在不同层表现不同，中间层某些层可区分全部 4 类错误

## 亮点与洞察
- **首次在 LVLM 中分解认识不确定性为冲突和无知**——提供可解释的错误行为诊断
- **训练无关+单次前向传播**——极低计算成本，可直接部署
- **证据论 × LLM 的新颖结合**——Dempster-Shafer 理论在大模型中找到自然应用

## 局限性 / 可改进方向
- 仅使用 output head 特征，未利用中间层的丰富信息
- 证据权重的闭式解依赖线性投影假设
- 目前是检测而非修复——检测到不确定性后如何改善输出是下一步

## 相关工作与启发
- **vs Semantic Entropy**：需多次采样+外部模型评估等价语义。EUQ 单次前向即可
- **vs Verbalized Confidence**：依赖模型元认知能力（不可靠）。EUQ 从特征直接提取
- **vs Evidential Deep Learning**：需要训练。EUQ 完全无需训练

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 首次将证据理论的 CF/IG 分解应用于 LVLM 错误检测
- 实验充分度: ⭐⭐⭐⭐⭐ 4 模型 × 4 类错误 × 多基线，层级分析有深度
- 写作质量: ⭐⭐⭐⭐ 理论推导严谨，可视化有帮助
- 价值: ⭐⭐⭐⭐⭐ 对 LVLM 可信度和安全部署有直接实用价值
