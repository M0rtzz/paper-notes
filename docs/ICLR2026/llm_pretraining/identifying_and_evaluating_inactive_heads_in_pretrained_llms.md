---
title: >-
  [论文解读] Identifying and Evaluating Inactive Heads in Pretrained LLMs
description: >-
  [ICLR 2026][注意力头] 系统评估 12 种评分函数来识别 LLM 中不活跃的注意力头，发现平均头输出范数（Avg Head Output Norm）比传统注意力权重指标更能模型无关地识别不活跃头；14 个模型上验证平均超过 12% 的头可被置零而保持 MMLU 精度在 1% 以内。
tags:
  - ICLR 2026
  - 注意力头
  - 不活跃头
  - 注意力汇聚
  - 评分函数
  - 模型分析
  - Transformer
---

# Identifying and Evaluating Inactive Heads in Pretrained LLMs

**会议**: ICLR 2026  
**arXiv**: [2504.03889](https://arxiv.org/abs/2504.03889)  
**代码**: [GitHub](https://github.com/psandovalsegura/inactive-heads)  
**领域**: llm_nlp  
**关键词**: 注意力头, 不活跃头, 注意力汇聚, 评分函数, 模型分析, Transformer  

## 一句话总结

系统评估 12 种评分函数来识别 LLM 中不活跃的注意力头，发现平均头输出范数（Avg Head Output Norm）比传统注意力权重指标更能模型无关地识别不活跃头；14 个模型上验证平均超过 12% 的头可被置零而保持 MMLU 精度在 1% 以内。

## 研究背景与动机

注意力机制是 Transformer 的基石，但已有研究发现一些注意力头会出现**注意力汇聚（attention sinks）**——第一个 token 获得最多注意力，尽管语义重要性有限。

**现有工作局限**：
- Guo et al. (2024a) 仅基于**注意力权重**判断"dormant heads"
- 假设：头主要关注首 token 且首 token value 接近零 -> 头输出接近零
- 忽略了：头可能关注多个 value 近零的 token，或注意力看似活跃但输出很小

**关键问题**：不活跃注意力头到底有多普遍？不同"不活跃"定义给出不同答案。

## 方法详解

### 整体框架

1. **定义评分函数**：12 种函数衡量注意力权重、value 向量和头输出
2. **阈值分类**：设阈值分为"可能不活跃"和"活跃"
3. **模型干预验证**：置零头输出，在 MMLU 上评估

### 关键设计

**12 种评分函数**三大类（各 2 基本 + 2 层归一化）：

**注意力权重类**：
1. Avg Weight of First Token (AWFT)：首 token 平均权重 > tau
2. Avg Entropy of Query Distributions (AEQD)：查询分布平均熵 < tau

**Value 向量类**：
3. First Token Value Vector Norm (FTVVN)：首 token value 范数 < tau
4. Avg Value Vector Norm (AVVN)：平均 value 范数 < tau

**头输出类**：
5. Last Token Head Output Norm (LTHON)：末 token 头输出范数 < tau
6. Avg Head Output Norm (AHON)：平均头输出范数 < tau

每种有层归一化版本 (LN)，除以同层其他头平均得分。AHON (LN) 阈值 tau=0.1 表示输出范数低于层平均 10% 的头被认为不活跃。

**阈值选择**：MMLU 输入上计算 CDF，取 p 分位数（p=0..30），最多置零 30%。

### 模型干预

**动态剪枝**：每次前向传播根据评分和阈值构建布尔矩阵，True 的头输出被置零。评估 MMLU 5-shot 准确率。

## 实验关键数据

### 主实验

**14 模型可置零头比例**（表2，MMLU 精度在基线 1% 内）：

| 模型 | AWFT (%) | 最佳函数 (%) | 最佳 |
|------|----------|-------------|------|
| Llama-3.1-8B | 8.56 | **17.11 (+8.55)** | AHON (LN) |
| Llama-3.1-8B-Inst | 1.01 | **10.97 (+9.95)** | AHON (LN) |
| OLMo-2-7B | 0.42 | **8.34 (+7.93)** | AHON (LN) |
| OLMo-2-7B-Inst | 1.46 | **19.54 (+18.07)** | AHON (LN) |
| OLMo-2-7B-DPO | 2.14 | **20.60 (+18.46)** | AHON (LN) |
| Qwen2.5-0.5B | 7.43 | **14.42 (+6.99)** | LTHON (LN) |
| Qwen2.5-7B | 1.25 | **7.54 (+6.29)** | AHON (LN) |
| **平均** | **4.61** | **12.18 (+7.56)** | — |

AHON (LN) 在 8/14 模型排名第 1，13/14 前 3。AWFT 仅识别 4.61%，遗漏 7.56%。

### 消融 / 稳定性

**差异性**（IoU 分析）：最大 IoU=0.58，AWFT 与其他 Precision<0.19——不同函数识别不同头。

**跨数据集**（OLMo-2-7B-Inst）：AWFT 阈值不稳定（0.077 vs 0.265），AHON (LN) 稳定（0.435-0.473）。

**微调影响**（Wasserstein 距离）：SFT/DPO/RLHF 对评分分布几乎无影响。**微调保留注意力头行为**。

**模型规模**（Qwen2.5，0.5B-14B）：0.5B-7B 相似，14B 出现显著不同行为。

### 关键发现

1. **看输出非权重**：头输出范数才是不活跃性真正指标
2. **>12% 可安全移除**：远高于 AWFT 估计的 ~5%
3. **模型无关性**：AHON (LN) 跨 3 模型家族一致有效
4. **微调影响微乎其微**：注意力行为预训练后基本固定

## 亮点与洞察

1. **简洁有力**：简单阈值评分即可有效识别不活跃头
2. **深刻洞察**：注意力看似"沉睡"不等于输出为零；反之看似活跃输出可能很小
3. **全面实验**：14 模型 x 12 函数 x 多阈值 x 3 基准
4. **动态剪枝**：按输入动态识别，比永久剪枝更灵活
5. **实践启示**：为 KV 缓存压缩、推理加速提供更好的头识别方法

## 局限性 / 可改进方向

1. **仅关注理解非加速**：未实现实际推理加速
2. **MLP 未分析**：注意力后 MLP 也可能逐 token 不活跃
3. **缺 GQA 分析**：现代模型共享 KV 头影响判断
4. **置零 vs 移除**：置零不等于移除参数
5. **任务有限**：主要 MMLU，生成任务上不活跃头可能不同

## 相关工作与启发

- **Dormant Attention** [Guo et al., 2024a]：仅注意力权重——不够
- **Voita/Michel (2019)**：MT 头剪枝——本文扩展到 LLM
- **Attention Sinks** [Xiao et al., 2024]：首 token 聚集——本文系统量化
- **StreamingLLM**：利用 sink 做长序列——本文提供更好识别
- **ScissorHands** [Liu et al., 2023]：KV 压缩——本文评分可作更好指标

## 评分

| 维度 | 评分 |
|------|------|
| 理论深度 | ⭐⭐⭐ |
| 新颖性 | ⭐⭐⭐⭐ |
| 实验充分性 | ⭐⭐⭐⭐⭐ |
| 写作质量 | ⭐⭐⭐⭐ |
| 实用价值 | ⭐⭐⭐⭐ |
| 总体评价 | ⭐⭐⭐⭐ |
