---
description: "【论文笔记】PPE: Positional Preservation Embedding for Token Compression in Multimodal Large Language Models 论文解读 | ICLR 2026 | arXiv 2510.22936 | Token压缩 | 提出PPE(位置保持嵌入)，在MLLM视觉token合并时将多个原始位置ID编码到单个压缩token的不同维度段中（利用RoPE/M-RoPE维度独立性），无参数且即插即用，90%压缩率下在MMBench/TextVQA/VideoMME上比先前方法提升2-5%。"
tags:
  - ICLR 2026
---

# PPE: Positional Preservation Embedding for Token Compression in Multimodal Large Language Models

**会议**: ICLR 2026  
**arXiv**: [2510.22936](https://arxiv.org/abs/2510.22936)  
**代码**: [GitHub](https://github.com/MouxiaoHuang/PPE)  
**领域**: 多模态VLM/效率  
**关键词**: Token压缩, 位置编码, RoPE, MLLM效率, 时空保持

## 一句话总结
提出PPE(位置保持嵌入)，在MLLM视觉token合并时将多个原始位置ID编码到单个压缩token的不同维度段中（利用RoPE/M-RoPE维度独立性），无参数且即插即用，90%压缩率下在MMBench/TextVQA/VideoMME上比先前方法提升2-5%。

## 研究背景与动机

1. **领域现状**：MLLM的视觉token冗余→token合并/剪枝减少序列长度。但压缩后位置信息丢失→空间布局和时序连续性破坏→布局敏感任务(计数/时序定位)性能下降。

2. **现有痛点**：(1) ChatUniVi随机化合并token的位置ID→丢失原始布局；(2) PACT只保留聚类中心的ID→每个合并token只有一个位置→信息不足。

3. **切入角度**：RoPE的旋转编码在每个维度上独立→同一token的不同维度可以编码不同位置→将维度分成K组→每组编码一个被合并token的位置ID→单个压缩token携带多个位置。

## 方法详解

### PPE核心公式
$\hat{m}_d = m_{k,d}, \quad d = (k-1)\frac{D}{K}+1 \ldots k\frac{D}{K}$

→ 维度 $D$ 被分成 $K$ 组，第 $k$ 组编码第 $k$ 个被合并token的位置ID

### M-RoPE扩展
对3D视频(时间+高度+宽度)，每个维度段内进一步分K组→三维度各自保持多位置

### 级联压缩
- PPE支持多层级逐步压缩→每层进一步合并+PPE重编码→高压缩率不丢失位置

### 关键特性
- 零参数→不增加任何可训练参数
- 即插即用→可嵌入任何token合并框架

## 实验关键数据

| 方法 | 90%压缩 MMBench | TextVQA | VideoMME |
|------|---------------|---------|---------|
| ChatUniVi | 基线 | 基线 | 基线 |
| PACT | + | + | + |
| **+PPE** | **+2-5%** | **+2-5%** | **+2-5%** |

### 关键发现
- PPE在布局敏感任务(TextVQA/计数)上提升最大→位置保持正是这些任务需要的
- 级联压缩时PPE优势更大→多级压缩下位置信息累积丢失更严重→PPE缓解
- 90%压缩率下仍保持>90%位置ID→大部分空间结构保留

## 亮点与洞察
- **利用RoPE的维度独立性**：RoPE每个维度的旋转独立→维度不需要全编码同一位置→自然支持"一个token多个位置"。
- **"首个"位置保持方案**：之前没人系统性地解决token合并中位置丢失的问题→PPE填补了这个空白。
- **级联压缩的自然扩展**：PPE的设计让多级压缩只是递归应用→简洁通用。

## 评分
- 新颖性: ⭐⭐⭐⭐ 利用RoPE维度独立性做位置保持是新颖思路
- 实验充分度: ⭐⭐⭐⭐ 图像+视频+多基准验证
- 写作质量: ⭐⭐⭐⭐ 方法描述清晰，图示直观
- 价值: ⭐⭐⭐⭐ 对MLLM效率优化有直接实用价值
