---
title: >-
  [论文解读] FineXtrol: Controllable Motion Generation via Fine-Grained Text
description: >-
  [AAAI2026][人体理解][motion generation] 提出 FineXtrol 框架，使用带时间标注的细粒度文本描述作为控制信号，结合层次化对比学习增强 text encoder 的判别力，实现对特定身体部位在指定时间区间内的精确动作生成控制。
tags:
  - AAAI2026
  - 人体理解
  - motion generation
  - fine-grained control
  - 对比学习
  - 扩散模型
  - ControlNet
---

<!-- 由 src/gen_stubs.py 自动生成 -->
# FineXtrol: Controllable Motion Generation via Fine-Grained Text

**会议**: AAAI2026  
**arXiv**: [2511.18927](https://arxiv.org/abs/2511.18927)  
**代码**: 待确认  
**领域**: human_understanding  
**关键词**: motion generation, fine-grained control, contrastive learning, diffusion model, ControlNet  

## 一句话总结
提出 FineXtrol 框架，使用带时间标注的细粒度文本描述作为控制信号，结合层次化对比学习增强 text encoder 的判别力，实现对特定身体部位在指定时间区间内的精确动作生成控制。

## 背景与动机
- Text-to-motion 生成领域对精确可控性的需求日益增长
- 已有方法两类缺陷：
  - LLM 扩展描述（如 CoMo）：扩展文本与 ground-truth motion 不严格对齐，缺乏显式时间线索
  - 空间坐标控制（如 OmniControl）：需要用户提供 3D 坐标序列，计算开销大且不直观
- 通用 text encoder（CLIP、T5）对细粒度动作描述的嵌入判别力不足

## 核心问题
如何用文本（而非坐标）作为控制信号，实现对人体动作在时空两个维度上的精细控制，同时保持用户友好性和计算效率？

## 方法详解

### 整体框架
采用 ControlNet 范式的双分支 diffusion 结构：
- **下分支**：冻结的 MDM（Motion Diffusion Model），从粗粒度文本 $\boldsymbol{p}$ 生成 motion
- **上分支**：MDM 的可训练副本，接收细粒度文本控制信号 $\boldsymbol{c}$，通过 conditional feature adaptation 注入控制
- 两分支通过零初始化线性层连接：$\boldsymbol{h}_l^{\text{out}} = \boldsymbol{h}_l^{\text{ori}} + \mathcal{P}_l(\boldsymbol{h}_l^{\text{ctrl}})$

### 关键设计：层次化对比学习
针对细粒度文本控制信号的三层信息结构，进行渐进式 T5 encoder 训练：
1. **Sentence-level**: 用 DeepSeek-V2 改写句子构建正样本对，区分不同身体部位动作描述
2. **Snippet-level**: 随机替换/打乱单时间段内的句子，增强对段内句序的鲁棒性
3. **Sequence-level**: 对各时间段应用 snippet 级增强但保持时间顺序，增强时间感知能力

训练目标为 InfoNCE loss：$\mathcal{L}_i = -\log \frac{\exp(\text{sim}(z_i,z_j)/\tau)}{\sum_{k=1}^{2N} \mathbb{1}_{[k\neq i]} \exp(\text{sim}(z_i,z_k)/\tau)}$

## 实验关键数据

| 方法 | 控制信号 | FID ↓ | R-Top3 ↑ | 推理时间(s) | 参数量 |
|------|---------|-------|----------|------------|--------|
| OmniControl | 坐标 | 0.255 | 0.680 | 168.51 | 48.79M |
| InterControl | 坐标 | 0.209 | 0.684 | 159.72 | 42.00M |
| CoMo | 文本 | 0.347 | 0.625 | - | - |
| **FineXtrol** | **文本** | **0.245** | **0.685** | **128.57** | **23.39M** |

- Cross body part 控制：FineXtrol FID=0.351，OmniControl 大幅退化至 0.624
- User study：78.79%（无控制信号）和 74.24%（有控制信号）用户偏好 FineXtrol

## 亮点
- 文本控制信号既用户友好又计算高效，避免了坐标转换的巨大开销
- 层次化对比学习精准匹配了控制信号的三层语义结构
- 参数量仅 23.39M（最少），推理速度 128.57s（最快）
- 多部位联合控制时性能衰减极小，鲁棒性强

## 局限性 / 可改进方向
- 仅在 HumanML3D 上评估，数据集覆盖范围有限
- 细粒度文本依赖 FineMotion 标注，获取成本不低
- 6 部位粒度（head/body/四肢）仍较粗，未覆盖手指等精细部位
- 未与最新 text-to-motion 基线（如 MoMask）在控制场景下对比

## 与相关工作的对比
| 维度 | FineXtrol | OmniControl | CoMo |
|------|-----------|-------------|------|
| 控制信号 | 细粒度文本 + 时间区间 | 3D 坐标序列 | LLM 扩展文本 |
| 时间控制 | ✓ 显式 | 隐式 | ✗ |
| 用户友好 | ✓ | ✗ | ✓ |
| 多部位控制 | 鲁棒 | 退化严重 | 退化 |
| Text encoder | 层次化对比学习增强 | N/A | 原始 CLIP |

## 启发与关联
- ControlNet 范式不局限于图像，在 motion 领域同样有效
- 文本控制优于坐标控制的关键在于灵活性和可扩展性
- 层次化对比学习的思路可迁移到其他需要细粒度文本理解的任务

## 评分
- 新颖性: ⭐⭐⭐⭐ — 细粒度时间感知文本控制 + 层次化对比学习
- 实验充分度: ⭐⭐⭐ — 实验全面但仅限 HumanML3D 单数据集
- 写作质量: ⭐⭐⭐⭐ — 动机清晰，方法描述完整
- 价值: ⭐⭐⭐⭐ — 为 motion 控制生成提供了实用高效的新范式
