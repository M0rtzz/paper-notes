---
title: >-
  [论文解读] RedSage: A Cybersecurity Generalist LLM
description: >-
  [ICLR 2026][AI安全][网络安全LLM] 构建了完整的网络安全LLM pipeline：11.8B token的领域持续预训练 + 266K样本的agentic augmented SFT + 30K MCQ+240开放问答的综合评测基准RedSage-Bench，8B模型在多个网络安全benchmarks上达SOTA。
tags:
  - ICLR 2026
  - AI安全
  - 网络安全LLM
  - continual pretraining
  - agentic augmentation
  - 安全评测
  - RedSage-Bench
---

# RedSage: A Cybersecurity Generalist LLM

**会议**: ICLR 2026  
**arXiv**: [2601.22159](https://arxiv.org/abs/2601.22159)

**代码**: 有 (开源数据+模型+代码)

**领域**: AI安全 / 网络安全  
**关键词**: 网络安全LLM, continual pretraining, agentic augmentation, 安全评测, RedSage-Bench

## 一句话总结

构建了完整的网络安全LLM pipeline：11.8B token的领域持续预训练 + 266K样本的agentic augmented SFT + 30K MCQ+240开放问答的综合评测基准RedSage-Bench，8B模型在多个网络安全benchmarks上达SOTA。

## 研究背景与动机

网络安全威胁日趋复杂——APT攻击、漏洞管理、事件响应等任务需要高度专业知识。全球网络安全人才缺口达数百万。现有网络安全LLM存在三个主要短板：(1) 大多只做单一训练阶段（如仅预训练或仅SFT）；(2) SFT数据量极小（PRIMUS仅835样本）；(3) 评测基准覆盖不全——缺乏工具使用能力评测和开放问答质量评估。

本文的目标是构建一个全面的、开放的网络安全LLM系统，同时解决数据、训练和评测三方面的不足。核心区别在于：结合大规模持续预训练（11.7B tokens）+ 高质量agentic augmented SFT（266K samples）+ 完整评测（知识+技能+工具+质量评分）。

## 方法详解

### 整体框架

(1) CyberFineWeb：从FineWeb过滤网络安全文本+30%通用知识replay → (2) RedSage-Seed：28,637高质量策展样本 → (3) Agentic augmentation生成266K SFT对话 → (4) RedSage-Bench评测。

### 关键设计

1. **CyberFineWeb预训练语料**：用 ModernBERT-base 训练二分类器过滤 FineWeb → 125M文档(89.8B tokens) → 混合30% FineWeb-Edu防遗忘 → MinHash-LSH去重 → 按时间分块训练+early stopping → 最终13M文档(11.7B tokens)。

2. **RedSage-Seed策展**：三类高质量来源——Knowledge(MITRE ATT&CK/CWE/OWASP等)、Skills(HackTricks/渗透测试writeups)、Tools(CLI cheatsheets/Kali Linux文档)。28,637样本 + 459K非分类文档。

3. **Agentic Augmentation Pipeline**：将策展的资源通过LLM代理转化为多轮expert-assistant对话，模拟真实的网络安全工作流。生成267K SFT样本（知识67K + 技能96K + 工具104K）。

4. **RedSage-Bench**：30K MCQ覆盖Knowledge/Skills/Tools + 240开放问答 + 质量LLM-judge评分。首个同时评估知识、技能和工具使用的网络安全基准。

### 损失函数 / 训练策略

基于 Llama-3.1-8B 做 continual pretraining（标准CLM loss）+ SFT（对话格式的CE loss）+ DPO对齐（开源偏好数据）。

## 实验关键数据

### 主实验

| 基准 | RedSage-8B | Foundation-Sec-8B | PRIMUS | Llama-3.1-8B |
|------|-----------|------------------|--------|-------------|
| SecEval | **最优** | 次优 | - | 基线 |
| CyberBench | **最优** | 次优 | 次优 | 基线 |
| General Benchmarks | **改善** | - | 微降 | 基线 |

### 消融实验

| 组件 | 效果 | 说明 |
|------|------|------|
| 去掉 continual PT | 显著下降 | 领域知识基础 |
| 去掉 agentic augmentation | 技能/工具能力下降 | 对话质量的关键 |
| 去掉 FineWeb-Edu replay | 通用能力退化 | 防遗忘必需 |
| 去掉 DPO | 开放问答质量下降 | 对齐重要 |

### 关键发现

- 大规模持续预训练(11.7B tokens)是性能提升的基础，仅SFT不够。

- Agentic augmentation比手工策展的SFT数据效果更好——模拟了真实工作流。

- 通用能力不降反升——30% replay ratio有效防止catastrophic forgetting。

- 在工具使用评测上RedSage大幅领先（因为其他基准根本不评测这个维度）。

- 开源策略（数据+模型+代码+评测）本身就是重要贡献。

## 亮点与洞察

- 全栈开源的网络安全LLM——数据、模型、代码、评测基准全部公开，填补了领域空白。

- Agentic augmentation将静态文档转化为动态对话的方法论有通用价值。

- RedSage-Bench是首个覆盖知识+技能+工具的综合网络安全评测。

## 局限性 / 可改进方向

- 8B参数限制了复杂推理能力，70B版本可能更优。

- 工具使用评测仍限于CLI命令，真实CTF场景的交互式评测未覆盖。

- 网络安全知识更新快，模型的时效性维护是持续挑战。

- 安全风险：开源网络安全LLM可能被恶意利用。

## 相关工作与启发

- 与 Foundation-Sec-8B(Cisco)、PRIMUS(Trend Micro)、SecGemini(Google) 形成对比。

- 开源和全面的策略可能加速整个网络安全AI社区的发展。

## 评分

- 新颖性: ⭐⭐⭐⭐ 全栈pipeline+agentic augmentation

- 实验充分度: ⭐⭐⭐⭐ 多基准评测+消融

- 写作质量: ⭐⭐⭐⭐ 结构清晰
- 价值: ⭐⭐⭐⭐⭐ 开源贡献极大
