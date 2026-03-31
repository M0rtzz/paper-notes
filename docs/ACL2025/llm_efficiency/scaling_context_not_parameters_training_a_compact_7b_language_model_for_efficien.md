# MegaBeam: Scaling Context, Not Parameters

**会议**: ACL 2025  
**arXiv**: [2505.08651](https://arxiv.org/abs/2505.08651)  
**代码**: https://huggingface.co/aws-prototyping/MegaBeam-Mistral-7B-512k (有)  
**领域**: LLM效率 / 长上下文  
**关键词**: 长上下文扩展, 7B模型, RoPE调参, 512K, 继续预训练

## 一句话总结
提出四阶段继续预训练策略将 Mistral-7B 的上下文长度扩展到 512K，7B 模型在 RULER-128K 上超越 GPT-4-1106 和 Llama-3.1-70B，是首个在 512K BABILong 上不用 RAG 就达到 35% 的开源模型。

## 研究背景与动机

1. **领域现状**：长上下文 LLM 是当前重要方向，但大多数高性能长上下文模型参数量巨大（70B+）。
2. **现有痛点**：将 7B 模型上下文从 32K 扩展到 512K 面临三大工程挑战——RoPE theta 校准、bfloat16 在极长位置的精度问题、XLA 编译器内存预分配。
3. **核心矛盾**：是否必须用大模型才能做好长上下文？小模型 + 长上下文是否可行？
4. **本文要解决什么**：用最少计算量（≤2B tokens）将 7B 模型扩展到 512K 上下文。
5. **核心 idea**：四阶段继续预训练 + 工程优化（RoPE theta 渐进调整/float32 RoPE/XLA chunk 调优）。

## 方法详解

### 四阶段训练
1. **Phase 1**：1.2B tokens（长文档，300K/600K 序列）
2. **Phase 2**：RoPE $\theta$ 从 25M 调到 75M，0.18B tokens@600K
3. **Phase 3**：0.2B tokens 平衡 80K/256K/512K 序列
4. **Phase 4**：22M 合成长上下文 QA 对做 SFT

### 工程关键
- float32 RoPE 必须（bfloat16 在长位置丢失数字精度）
- XLA chunk size 调优（更大 chunk 反而减少 186GB 预分配内存）

## 实验关键数据

| 模型 | RULER-128K Overall |
|------|-------------------|
| GPT-4-1106 | ~80% |
| Llama-3.1-70B | ~80% |
| **MegaBeam-7B** | **~85%** |
| BABILong-512K | **35%** (唯一开源) |

## 亮点与洞察
- **7B 超越 70B 在长上下文上**：证明"上下文长度 vs 参数量"的 tradeoff 中上下文可能更重要
- **仅 2B tokens 扩展**：极高计算效率
- **工程经验宝贵**：RoPE 精度、XLA 内存等问题的解决方案对社区有直接价值

## 局限性
- 多事实推理（QA2/QA3）性能显著下降
- 单/双事实任务 32K→512K 保持 >85%，但复杂推理退化

## 评分
- 新颖性: ⭐⭐⭐ 方法是已知技术的工程组合，但极限扩展有价值
- 实验充分度: ⭐⭐⭐⭐ RULER + BABILong + MMLU
- 写作质量: ⭐⭐⭐⭐ 工程细节详实
- 价值: ⭐⭐⭐⭐⭐ 开源 512K 7B 模型 + 详细训练配方
