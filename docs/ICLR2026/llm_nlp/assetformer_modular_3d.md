---
title: >-
  [论文解读] AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer
description: >-
  [ICLR 2026][LLM/NLP][模块化3D资产] 本文提出 AssetFormer，一个基于自回归 Transformer 的模块化 3D 资产生成框架，通过设计图遍历 token 排序、token 集建模和 SlowFast 解码策略，从文本描述生成由离散基元组合的高质量建筑资产，并构建了首个大规模真实模块化 3D 数据集（16k 真实 + 4k 合成样本）。
tags:
  - ICLR 2026
  - LLM/NLP
  - 模块化3D资产
  - Transformer
  - 用户生成内容
  - token排序
  - 推测解码
---

# AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer

**会议**: ICLR 2026  
**arXiv**: [2602.12100](https://arxiv.org/abs/2602.12100)  
**代码**: [GitHub](https://github.com/Advocate99/AssetFormer)  
**领域**: 3D 视觉 / 图像生成  
**关键词**: 模块化3D资产, 自回归Transformer, 用户生成内容, token排序, 推测解码

## 一句话总结
本文提出 AssetFormer，一个基于自回归 Transformer 的模块化 3D 资产生成框架，通过设计图遍历 token 排序、token 集建模和 SlowFast 解码策略，从文本描述生成由离散基元组合的高质量建筑资产，并构建了首个大规模真实模块化 3D 数据集（16k 真实 + 4k 合成样本）。

## 研究背景与动机

1. **领域现状**: 3D 生成方法使用体素、点云、神经场、mesh 等表征，在游戏行业的专业生产和 UGC 场景中面临质量不足、文件过大、非专业用户难以使用等问题。

2. **现有痛点**: 传统 3D 生成方法输出密集 mesh，难以直接集成到游戏引擎；模块化 3D 资产缺乏公开训练数据；已有 mesh 生成方法（MeshGPT）需要复杂图编码器。

3. **核心矛盾**: 游戏行业广泛使用模块化设计（CSG 原理），但自动化模块化资产生成几乎未被研究。

4. **本文目标**: 构建能从文本描述自动生成模块化 3D 资产的框架。

5. **切入角度**: 模块化资产天然是离散元素序列（每个基元有类别、旋转、位置属性），非常适合自回归建模。

6. **核心 idea**: 将 3D 模块化资产视为有序 token 序列，用图遍历确定最优排序，Decoder-only Transformer 进行 next-token prediction。

## 方法详解

### 整体框架
输入为文本描述，通过 FLAN-T5 编码后投影为 token。模型基于 Llama 架构（312M 参数），联合词表包含 25 种基元类别 + 4 种旋转 + 3 维位置 = 214 tokens。输出为 token 序列，解码为 3D 基元参数后在游戏引擎中渲染。

### 关键设计

1. **Token 集建模（Token Set Modeling）**:
    - 功能: 处理混合词表的 next-token prediction
    - 核心思路: 将基元的 5 个属性 $(c, r, x_0, x_1, x_2)$ 的各自有限离散值合并为联合词表 $\mathcal{V}$。推理时按属性周期过滤无效 logits 并重归一化
    - 设计动机: 直接用联合词表避免了多阶段解码，保持模型简洁

2. **Token 重排序（Token Re-Ordering）**:
    - 功能: 为 3D 基元确定最优排列顺序
    - 核心思路: 从资产底角出发，使用 DFS/BFS 图遍历所有基元，生成排列 $\mathcal{A} = \{\tau_0, ..., \tau_{n-1}\}$。DFS 略优于 BFS 和随机排序
    - 设计动机: 3D 资产不像文本有天然顺序，DFS 保证局部连通性同时维持全局从底到顶

3. **SlowFast 解码**:
    - 功能: 加速推理而不损失质量
    - 核心思路: 使用小模型（AssetFormer-S, 87M）快速预测简单 token，大模型（AssetFormer-B, 312M）处理复杂 token。适配投机解码算法并加入 token 类型过滤
    - 设计动机: 模块化资产中许多位置遵循常见模式，可由小模型高效预测

### 损失函数 / 训练策略
- 标准交叉熵损失，next-token prediction
- CFG (Classifier-Free Guidance) scale=2.0，训练时 10% 随机丢弃条件
- Top-k 采样 (k=10)，temperature=0.7
- 数据集：16k 真实样本（在线 UGC 平台）+ 4k PCG 合成样本

## 实验关键数据

### 主实验

| 方法 | FID ↓ | CLIP ↑ |
|------|-------|--------|
| PCG (算法生成) | 108.476 | 0.319 |
| AssetFormer + Greedy | 63.351 | 0.319 |
| AssetFormer + Beam | 63.333 | 0.321 |
| AssetFormer + Top-K | **55.186** | 0.320 |
| 真实数据 | / | 0.322 |

### 消融实验

| 配置 | FID ↓ | 说明 |
|------|-------|------|
| Raw Order | 65.215 | 无排序导致孤立部件 |
| RAR (随机排列) | 83.561 | 图像领域的随机化策略在 3D 中不适用 |
| BFS | 61.620 | 有效但略逊于 DFS |
| DFS | **55.186** | 最优排序 |
| 仅合成数据 | 113.560 | 多样性不足 |
| 仅真实数据 | 63.381 | 缺少结构化基础 |
| 混合数据 | **55.186** | 两类数据互补 |

### 关键发现
- Top-k 采样在质量和多样性间取得最佳平衡
- DFS 排序优于 BFS 和随机排序，保证局部连通性
- 合成数据和真实数据互补：合成提供结构化基础，真实提供多样性
- SlowFast 解码加速 47% (80.62→119.02 token/s) 且几乎无质量损失

## 亮点与洞察
- 首次将自回归 Transformer 应用于模块化 3D 资产生成
- 模块化表征的关键优势：无损离散化、文件小、易集成游戏引擎、纹理映射简单
- 与 MeshGPT 等密集 mesh 方法形成互补：模块化适合建筑类规则资产
- 数据收集策略值得借鉴：真实 UGC 平台数据 + PCG 合成 + GPT-4o 标注

## 局限与展望
- 仅支持文本输入，未探索图像条件生成
- 固定离散词表，难以适应变化的设计空间
- 仅验证建筑类资产，未扩展到家具、车辆等其他模块化类别
- 纹理处理留给后处理，未端到端建模

## 相关工作与启发
- **vs MeshGPT**: MeshGPT 生成密集 mesh，AssetFormer 生成模块化资产，两者互补
- **vs Hunyuan3D**: 原生 3D 生成方法在建筑内部结构上表现差，watertight 预处理丢失模块信息
- **vs PCG**: PCG 需要精心设计算法，AssetFormer 是数据驱动的，可从文本控制生成

## 评分
- 新颖性: ⭐⭐⭐⭐ 模块化 3D 资产的自回归生成是新方向
- 实验充分度: ⭐⭐⭐⭐ 多消融分析，与多种方法对比
- 写作质量: ⭐⭐⭐⭐ 实践导向，工业应用价值明确
- 价值: ⭐⭐⭐⭐ 对游戏 UGC 和 3D 内容创作有直接应用价值

<!-- RELATED:START -->

## 相关论文

- [\[ICLR 2026\] Trapped by simplicity: When Transformers fail to learn from noisy features](trapped_by_simplicity_when_transformers_fail_to_learn_from_noisy_features.md)
- [\[ICLR 2026\] ELLMob: Event-Driven Human Mobility Generation with Self-Aligned LLM Framework](ellmob_event-driven_human_mobility_generation_with_self-aligned_llm_framework.md)
- [\[ICLR 2026\] DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-size Canvas](dreamon_diffusion_language_models_for_code_infilling_beyond_fixed-size_canvas.md)
- [\[ICLR 2026\] d²Cache: Accelerating Diffusion-Based LLMs via Dual Adaptive Caching](d2cache_accelerating_diffusion-based_llms_via_dual_adaptive_caching.md)
- [\[ICLR 2026\] Compositional-ARC: Assessing Systematic Generalization in Abstract Spatial Reasoning](compositional-arc_assessing_systematic_generalization_in_abstract_spatial_reason.md)

<!-- RELATED:END -->
