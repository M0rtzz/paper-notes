---
description: "【论文笔记】Vision Function Layer in Multimodal LLMs 论文解读 | NeurIPS 2025 | arXiv 2509.24791 | MLLM可解释性 | 发现 MLLM 中视觉相关的功能解码分布在特定的窄层中（视觉功能层/VFL），不同功能呈现一致的层级模式（识别→计数→定位→OCR），并据此设计了 VFL-LoRA 和 VFL-select 方法。"
tags:
  - NeurIPS 2025
---

# Vision Function Layer in Multimodal LLMs

**会议**: NeurIPS 2025  
**arXiv**: [2509.24791](https://arxiv.org/abs/2509.24791)  
**代码**: https://github.com/ChengShiest/Vision-Function-Layer  
**领域**: 多模态VLM  
**关键词**: MLLM可解释性, 视觉功能层, Token交换, LoRA微调, 数据选择

## 一句话总结
发现 MLLM 中视觉相关的功能解码分布在特定的窄层中（视觉功能层/VFL），不同功能呈现一致的层级模式（识别→计数→定位→OCR），并据此设计了 VFL-LoRA 和 VFL-select 方法。

## 研究背景与动机
1. **领域现状**：MLLM 的内部视觉处理机制是"黑箱"——我们不知道不同层对不同视觉任务的具体贡献
2. **现有痛点**：现有研究只给出粗略结论（"浅层提取视觉特征，深层做推理"），缺乏精细的功能定位框架
3. **核心创新**：提出 Visual Token Swapping 框架——在指定层交换两张图的视觉 KV cache，观察输出变化率来定位功能层

## 方法详解

### 关键设计
1. **Vision Token Swapping**：构造仅单一视觉属性不同的图像对，在第 k 层交换视觉 Token 的 KV cache，如果输出变化说明第 k 层对该功能重要
2. **Vision Token Dropping**：渐进式从第 k 层开始丢弃所有视觉 Token，观察在通用 VQA 基准上的性能衰减

### 核心发现（Qwen2.5-VL-7B, 28层）
- **识别(Recognition)**：峰值在浅层(0-10)，分布式影响
- **计数(Counting)**：峰值在第12层(87.4%)
- **定位(Grounding)**：峰值在第18层(100%)
- **OCR**：峰值在深层第22层(92.8%)
- 这个顺序与人类行为一致：先认、再数、再定位、最后读文字

### 应用
1. **VFL-LoRA**：只对与训练数据功能对齐的 VFL 层做 LoRA，用 1/3 参数达到 full-LoRA 性能且减少域外函数遗忘
2. **VFL-select**：分析去掉特定 VFL 后训练数据上的性能差异，自动按功能分类数据，实现用 20% 数据达到 98% 性能

## 实验关键数据

### VFL-LoRA vs Full-LoRA

| 方法 | 参数量 | 域内性能 | 域外泛化 |
|------|--------|---------|---------|
| Full-LoRA | 100% | 基准 | 有遗忘 |
| VFL-LoRA | ~33% | **持平** | **更好** |

### VFL-select vs 人类专家数据选择
- VFL-select 超越人类专家的数据选择，20% 数据达到 98% 全数据性能

## 亮点与洞察
- **视觉功能层的层级顺序跨模型一致**——从 LLaVA 到 Qwen 系列都遵循相同模式，说明这是 MLLM 的内在结构
- **Token Swapping 比 probing 更精确**——直接因果性干预而非相关性分析
- 实际应用价值极高：VFL-LoRA 和 VFL-select 可直接用于降低微调成本

## 局限性
- 简单功能（识别/计数）的定位比复杂推理功能（数学/逻辑）更清晰
- 功能层可能在不同数据分布下有细微偏移

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ Token Swapping 分析框架和 VFL 概念都是首创
- 实验充分度: ⭐⭐⭐⭐⭐ 多模型多任务+两个实际应用
- 写作质量: ⭐⭐⭐⭐⭐ 发现清晰，应用直接
- 价值: ⭐⭐⭐⭐⭐ 对 MLLM 的理解和使用都有深远影响
