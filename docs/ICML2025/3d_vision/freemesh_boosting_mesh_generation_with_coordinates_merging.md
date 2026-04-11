---
description: "【论文笔记】FreeMesh: Boosting Mesh Generation with Coordinates Merging 论文解读 | ICML2025 | arXiv 2505.13573 | 网格生成 | 提出 Per-Token-Mesh-Entropy（PTME）度量免训练评估网格 tokenizer 质量，并引入基于 BPE 的坐标合并技术（RMC）进一步压缩网格序列，在 MeshXL/MeshAnythingV2/EdgeRunner 上验证了压缩率和生成质量的同步提升。"
tags:
  - ICML2025
---

# FreeMesh: Boosting Mesh Generation with Coordinates Merging

**会议**: ICML2025  
**arXiv**: [2505.13573](https://arxiv.org/abs/2505.13573)  
**代码**: 待确认  
**领域**: 3d_vision  
**关键词**: 网格生成, 坐标合并, Token化, 自回归, 信息熵

## 一句话总结

提出 Per-Token-Mesh-Entropy（PTME）度量免训练评估网格 tokenizer 质量，并引入基于 BPE 的坐标合并技术（RMC）进一步压缩网格序列，在 MeshXL/MeshAnythingV2/EdgeRunner 上验证了压缩率和生成质量的同步提升。

## 研究背景与动机

- **自回归网格生成**：MeshGPT/MeshXL 等将 3D 网格序列化为 token 序列用 Transformer 生成
- **缺乏 tokenizer 评估指标**：只能通过昂贵训练间接评估，没有理论评估方法
- **序列过长**：坐标级表示导致序列冗长，限制可生成的最大面片数
- **高频重复模式**：序列化后坐标序列存在大量重复模式，可进一步压缩

## 方法详解

### Per-Token-Mesh-Entropy (PTME)

$$\text{PTME} = H(X) \times CR$$

其中 $H(X)$ 为 token 序列的信息熵，$CR$ 为压缩率（相对于原始坐标序列的长度比）

- PTME 越低 → 序列越易学习 → tokenizer 越好
- **免训练评估**：仅需统计 token 频率即可

### Rearrange & Merge Coordinates (RMC)

1. **重排列（Rearrange）**：对坐标序列进行规则化重排，使高频模式更集中
2. **合并（Merge）**：使用 SentencePiece/BPE 学习子词词汇表，将高频坐标模式合并为新 token
3. **扩充词汇表**：通过增大 vocab 大小压缩更多坐标，降低 PTME

### 管线

原始网格 → 选择 tokenizer（RAW/AMT/EDR）→ 重排列 → BPE 合并 → 训练自回归生成模型

### 与现有 tokenizer 的兼容性

- **MeshXL (RAW)**：9 坐标/面 → RMC 后 ~6 token/面
- **MeshAnythingV2 (AMT)**：~4.5 坐标/面 → RMC 后 ~3.3 token/面
- **EdgeRunner (EDR)**：~4 坐标/面 → RMC 后最优 **21.2% 压缩率**

## 实验关键数据

### 压缩率对比

| Tokenizer | 原始压缩率 | + MC | + RMC |
|---|---|---|---|
| RAW | 100% | 无改善 | 显著降低 |
| AMT | ~50% | 轻微 | 进一步降低 |
| EDR | ~45% | 轻微 | **21.2%** |

### 生成质量（7-bit 离散化，Objaverse）

- RMC 在所有 tokenizer 上提升了可生成的最大面片数
- 几何细节保留更好，拓扑质量更高
- PTME 与实际训练效果高度正相关 → 验证了度量的有效性

### 消融

- 仅 Merge（无 Rearrange）：PTME 反而未降低
- Rearrange 是 Merge 有效的前提条件
- 词汇表大小增大→PTME 持续降低→生成面片数持续增多

## 亮点与洞察

1. **PTME**：首个网格 tokenizer 的免训练理论评估指标
2. **坐标合并**：借用 NLP 子词分词思想到 3D 网格
3. **即插即用**：适用于任何坐标级网格 tokenizer
4. **21.2% 压缩率**创纪录

## 局限性 / 可改进方向

- BPE 合并是离散操作，可能丢失部分几何语义连续性
- 词汇表过大可能导致 embedding 层参数膨胀
- PTME 作为理论指标的上界精度待进一步验证
- 合并后 token 的语义可解释性下降

## 相关工作与启发

- Siddiqui et al. (2023) MeshGPT：VQ-VAE + Transformer 开创者
- Chen et al. (2024a) MeshXL：坐标级直接生成基线
- Tang et al. (2024a) EdgeRunner：边级压缩
- Chen et al. (2024c) MeshAnythingV2：邻接网格 tokenization
- Sennrich et al. (2016) BPE：NLP 子词分词，本文灵感来源

## 评分

⭐⭐⭐⭐ — PTME 度量和坐标合并思路简洁有效，跨领域方法迁移巧妙，NLP 中 BPE 理念在 3D 中的成功应用


## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
