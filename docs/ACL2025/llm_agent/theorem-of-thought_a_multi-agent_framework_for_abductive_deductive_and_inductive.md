# Theorem-of-Thought: A Multi-Agent Framework for Abductive, Deductive, and Inductive Reasoning in Language Models

**会议**: ACL 2025  
**arXiv**: [2506.07106](https://arxiv.org/abs/2506.07106)  
**代码**: https://github.com/KurbanIntelligenceLab/theorem-of-thought (有)  
**领域**: LLM Agent  
**关键词**: 多智能体推理, 演绎推理, 归纳推理, 溢因推理, 贝叶斯信念传播

## 一句话总结
将推理建模为三个并行 agent（溢因、演绎、归纳），各自生成推理链并转化为形式化推理图(FRG)，通过 NLI 引导的贝叶斯信念传播评估内部一致性，选择得分最高的推理图作为最终答案，在 WebOfLies 和 MultiArith 上一致超越 CoT/SC 基线。

## 研究背景与动机

1. **领域现状**：CoT 和 SC 使用单一推理范式，但复杂问题可能需要不同类型的推理（溢因/演绎/归纳）。
2. **核心 idea**：三种推理范式并行生成，用形式化一致性评分而非多数投票选择最佳。

## 方法详解

### 关键设计
1. **三 agent 并行推理**：溢因 agent 生成最佳解释、演绎 agent 生成严格推导、归纳 agent 生成模式归纳
2. **形式化推理图 (FRG)**：将每条推理链转化为包含前提、推理步骤和结论的有向图
3. **NLI 引导的贝叶斯信念传播**：用自然语言推理(NLI)模型评估节点间的逻辑一致性，通过信念传播计算每个 FRG 的整体一致性得分

## 实验关键数据
- WebOfLies（符号推理）和 MultiArith（数值推理）上一致超越 CoT、SC、CoT-Decoding
- 产生可解释且逻辑接地的推理链

## 亮点与洞察
- **多范式推理+形式化验证**是一个有前景的方向，不同于多数投票的“统计聚合”，本文做“逻辑聚合”
- 贝叶斯信念传播提供了形式化的一致性评估机制

## 局限性 / 可改进方向
- 仅在 2 个 benchmark 上验证
- NLI 模型的质量直接影响一致性评分

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 三范式推理+形式化验证的组合非常新颖
- 实验充分度: ⭐⭐⭐ 只有 2 个数据集
- 写作质量: ⭐⭐⭐⭐ 框架描述清晰
- 价值: ⭐⭐⭐⭐ 对推理范式设计有启发
