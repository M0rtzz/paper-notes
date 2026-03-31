# Masking in Multi-hop QA: How LMs Perform with Context Permutation

**会议**: ACL 2025  
**arXiv**: [2505.11754](https://arxiv.org/abs/2505.11754)  
**代码**: https://github.com/hwy9855/MultiHopQA-Reasoning  
**领域**: LLM/NLP  
**关键词**: multi-hop QA, causal mask, attention, document permutation, encoder-decoder

## 一句话总结
系统分析因果掩码对 LLM 多跳 QA 的影响，发现 encoder-decoder（Flan-T5 770M）零样本多跳性能优于 decoder-only（Qwen 7B），且 prefix mask 可提升 decoder-only 的多跳推理能力 5.1%。

## 研究背景与动机

1. **领域现状**：RAG 中多跳 QA 需跨多文档综合信息，因果掩码限制前面 token 看到后面内容。
2. **现有痛点**：Lost in the middle 问题在多跳场景更严重，因果掩码可能是结构性瓶颈。
3. **核心矛盾**：因果掩码是否是 decoder-only LLM 多跳推理的结构性限制？
4. **本文要解决什么？** 通过文档排列实验和注意力分析系统回答此问题。
5. **切入角度**：三种排列维度（顺序/距离/完整性）+ 因果 vs 双向注意力对比。
6. **核心idea一句话**：金文档顺序与推理链一致时性能最佳，双向注意力缓解因果掩码限制。

## 方法详解

### 整体框架
三种 LM 家族（Flan-T5 / Qwen / Llama）x 三种文档排列维度 x 因果 vs prefix mask + 注意力权重分析。

### 关键设计

1. **三种排列维度**
   - 金文档顺序（正向/反向）：与推理链方向一致 vs 相反
   - 金文档距离（紧密/分散）：测试位置效应
   - 金文档完整性（完整/去除第一跳）：测试参数知识依赖

2. **Prefix Mask 实验**
   - 将因果 mask 替换为 prefix mask（输入双向注意力，生成仍因果）
   - 设计动机：测试双向编码是否改善多跳推理

3. **注意力分析**
   - 分组注意力权重（Grouped Attention Weight）量化文档块间注意力分布
   - 信息贡献分数（IC Score）度量各文档对预测的影响

## 实验关键数据

### 主实验 -- 零样本 vs 微调
| 模型 | 零样本 | 微调后 |
|------|--------|--------|
| Flan-T5 Large (770M) | **高** | 高 |
| Qwen 2.5 7B | 低 | 高 |
| Llama 3.1 8B | 低 | 中 |

### 文档顺序影响
| 顺序 | 效果 |
|------|------|
| 正向（与推理链一致）| 最佳 |
| 反向 | 显著下降 |

### Prefix Mask 效果
| 配置 | Qwen 7B |
|------|--------|
| 因果 mask | 28.6% |
| Prefix mask (启发式) | **33.7%** |

### 关键发现
- 小 encoder-decoder > 大 decoder-only 在零样本多跳 QA 上成立
- 金文档顺序与推理链一致时所有模型均最佳
- Prefix mask 提升 decoder-only 性能 5.1%
- 注意力峰值与答案正确性相关：正确回答时注意力更集中
- 去除第一跳文档影响有限：部分依赖参数知识

## 亮点与洞察
- 小 encoder-decoder > 大 decoder-only 挑战越大越好的默认假设
- 注意力峰值启发式是免训练的性能提升方法

## 局限性 / 可改进方向
- 仅测试 2 跳 QA，更多跳数未验证
- 改进方向：自适应注意力模式、多跳感知训练

## 相关工作与启发
- **vs Lost in the Middle**：本文扩展到多跳场景
- **vs BehnamGhader et al.**：他们用双向注意力做嵌入，本文用于多跳 QA

## 评分
- 新颖性: ⭐⭐⭐⭐ 系统分析因果掩码对多跳 QA 影响
- 实验充分度: ⭐⭐⭐⭐⭐ 三种模型 x 三种排列 x 注意力
- 写作质量: ⭐⭐⭐⭐ 分析深入
- 价值: ⭐⭐⭐⭐ 对 RAG 架构选择有直接指导
