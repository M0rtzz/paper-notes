---
description: "【论文笔记】zip2zip: Inference-Time Adaptive Tokenization via Online Compression 论文解读 | NeurIPS 2025 | arXiv 2506.01084 | 自适应分词 | 提出 zip2zip，通过将 LZW 在线压缩算法集成到 LLM 推理流程中，实现推理时动态扩展词表生成\"超级Token\"（hypertokens），将输入输出序列长度缩减 15-40%，端到端延迟降低最高 40%。"
tags:
  - NeurIPS 2025
---

# zip2zip: Inference-Time Adaptive Tokenization via Online Compression

**会议**: NeurIPS 2025  
**arXiv**: [2506.01084](https://arxiv.org/abs/2506.01084)  
**代码**: https://github.com/epfl-dlab/zip2zip  
**领域**: 模型压缩  
**关键词**: 自适应分词, LZW压缩, 超级Token, 推理加速, 词表扩展

## 一句话总结
提出 zip2zip，通过将 LZW 在线压缩算法集成到 LLM 推理流程中，实现推理时动态扩展词表生成"超级Token"（hypertokens），将输入输出序列长度缩减 15-40%，端到端延迟降低最高 40%。

## 研究背景与动机
1. **领域现状**：LLM 使用静态 BPE 分词器，词表在通用语料上优化，面对代码/生物医学/多语言等领域分词效率差 2-3 倍
2. **现有痛点**：简单扩大词表收益递减且可能损害性能；为每个领域维护独立分词器不可扩展
3. **核心 idea**：推理时用 LZW 算法在线合并高频共现 Token 为 hypertoken，动态嵌入层计算新 Token 的表示

## 方法详解

### 关键设计
1. **LZW 分词器**：在基础 BPE Token 流上增量构建码本，合并高频 Token 对为 hypertoken，最大合并长度 M=3
2. **动态嵌入层（Hyper-Encoder）**：两层 Transformer encoder 将 M 个基础 Token 嵌入映射为一个 hypertoken 嵌入；嵌入可缓存
3. **压缩空间语言建模**：在 LZW 压缩后的序列上做因果语言建模训练，模型同时学会输入和输出 hypertoken
4. **辅助重建损失**：autoencoder 风格的损失确保 hypertoken 可以无损恢复原始 Token
5. **理论保证**：证明无损压缩下熵不变（Theorem 2.1），即最优模型性能理论上不受影响

### 训练策略
仅需 10 GPU-hours 用 LoRA 微调 Phi-3-4B；100M Token 训练数据即可。

## 实验关键数据

### Token效率提升

| 领域 | Llama-3 基础 | +zip2zip | 提升 |
|------|-------------|---------|------|
| 代码 | 4.1 bytes/tok | 6.1 | +48.8% |
| 数学 | 2.7 | 4.1 | +51.9% |
| 聊天 | 5.1 | 6.8 | +33.3% |

### 下游任务性能
| 模型 | 方法 | HellaSwag | ARC-C | MMLU |
|------|------|-----------|-------|------|
| Phi-3.5-4B | 基线 | 53.3 | 55.9 | 50.8 |
| Phi-3.5-4B | zip2zip | 52.6 | 55.4 | 49.2 |

### 关键发现
- 性能几乎无损（-0.7~-1.6%），但序列长度减少 15-40%
- 代码领域 hypertoken 比例高达 40%，多数对应语义有意义的单元（如"torch"、"Attention"）
- 端到端延迟降低最高 40%，因为减少了自回归解码步数

## 亮点与洞察
- **LZW 的在线性质**让 hypertoken 在创建后的下一步就可使用——这是 BPE 等离线方法做不到的
- 熵不变定理为"压缩不损性能"提供了理论支撑
- 方法可以无缝集成到 HuggingFace Transformers

## 局限性
- 当前 M=3 限制了压缩率上限；hypertoken 嵌入质量依赖 hyper-encoder 的表达能力
- 在对话场景中效果不如结构化文本（代码/数学）显著

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ LZW+LLM 的在线自适应分词首创
- 实验充分度: ⭐⭐⭐⭐ 多模型/多领域/效率分析完整
- 写作质量: ⭐⭐⭐⭐⭐ 概念清晰，图示直观
- 价值: ⭐⭐⭐⭐⭐ 实用价值极高，即插即用
