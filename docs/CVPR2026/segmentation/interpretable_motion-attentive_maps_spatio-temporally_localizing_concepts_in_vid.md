---
title: >-
  [论文解读] I'm a Map! Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers
description: >-
  [CVPR 2026][图像分割][Transformer] 提出 GramCol 和 IMAP 两种无需训练/梯度的方法，利用 Video DiT 内部特征为任意文本概念（尤其是运动概念）生成可解释的时空显著性图，并在运动定位和零样本视频语义分割上取得 SOTA。
tags:
  - CVPR 2026
  - 图像分割
  - Transformer
  - 可解释显著性图
  - 运动定位
  - 零样本视频语义分割
  - 注意力机制分析
---

# I'm a Map! Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers

**会议**: CVPR 2026  
**arXiv**: [2603.02919](https://arxiv.org/abs/2603.02919)  
**代码**: [有](https://github.com/youngjun-jun/IMAP)  
**领域**: 语义分割 / 视频可解释性  
**关键词**: Video Diffusion Transformer, 可解释显著性图, 运动定位, 零样本视频语义分割, 注意力机制分析

## 一句话总结

提出 GramCol 和 IMAP 两种无需训练/梯度的方法，利用 Video DiT 内部特征为任意文本概念（尤其是运动概念）生成可解释的时空显著性图，并在运动定位和零样本视频语义分割上取得 SOTA。

## 研究背景与动机

**Video DiT 的黑箱问题**：视频扩散 Transformer（CogVideoX、HunyuanVideo 等）能从文本描述生成高质量视频，但其内部如何将运动词汇转化为视频的时间动态机制仍不清楚，亟需可解释性分析工具。

**现有可解释性工作局限于图像域**：ConceptAttention 等方法仅能对图像 DiT 提供空间分割的显著性图，无法处理视频的时间维度，也不能解释运动相关的行为。

**时间特征研究局限于帧间动态**：DiTFlow 和 DiffTrack 等工作聚焦于跨帧注意力的光流或时间对应关系，但对 Video DiT 如何理解文本中的运动描述并生成对应时间动态缺乏探索。

**跨模态相似度的固有缺陷**：直接计算视觉 token 与文本 token 的相似度（如 ConceptAttention）会因跨模态特征空间差异产生不可靠的激活图，不同注意力头表现不一致。

**运动概念的时间定位需求**：运动是物体的时间移动，理想的运动显著性图应同时回答"何时运动"和"哪个物体运动"，这需要同时具备空间和时间定位能力。

**计算效率要求**：Video DiT 具有 L 层 × T 时间步 × 多头注意力的庞大特征空间，全部聚合既冗余又低效，需要高效的特征选择策略。

## 方法详解

### 整体框架

整个流程分为三步：（1）分析对象选择——确定有效的时间步和层；（2）GramCol 空间定位——为任意文本概念生成逐帧显著性图；（3）Motion Head 选择 + IMAP——对运动概念额外筛选运动相关的注意力头，获得时空定位图。整个流程无需任何训练、梯度计算或参数更新。

### 关键设计

**1. 分析对象选择（Subject of Analysis）**

- **时间步筛选**：丢弃早期（高噪声）时间步，因为此阶段特征语义不可解，且易出现记忆化现象（如水印）。
- **层选择**：将注意力权重矩阵视为离散时间马尔科夫链的状态转移矩阵，以注意力矩阵第二大特征值 $\lambda_2$ 的头均值作为层选择标准。$\lambda_2$ 越大的层，提取的特征越清晰、语义越丰富。CogVideoX 阈值设为 0.7，HunyuanVideo 设为 0.75。

**2. GramCol 空间定位**

- **QK-Matching 得到文本代理 token**：对每帧 $f_i$ 和概念 token $c$，找到与该概念注意力得分最大的视觉 token 作为文本代理 token（text-surrogate）：$s_{f_i}^c = \arg\max_p (\text{row}_p(\mathbf{q}_{f_i}) \mathbf{k}_c^\top)$。实验表明该峰值位置的定位精度达 0.9544。
- **Gram 矩阵列提取**：计算视觉 token 嵌入的 Gram 矩阵 $\mathbf{G} = \mathbf{h}_x \mathbf{h}_x^\top$，取第 $s_{f_i}^c$ 列作为显著性图。由于 Gram 矩阵编码视觉 token 间的相似度，与代理 token 语义相似的区域会得到大的正值，天然具备正向高亮特性。
- **自适应与无竞争**：每帧、每头独立选择代理 token，自动适应时间运动变化；不依赖 softmax 归一化的概念列表，单一概念也能生成完整显著性图，避免了概念间竞争问题。

**3. Motion Head 选择与 IMAP**

- **运动头识别**：运动引起帧间差异，因此将每帧的视觉 token 视为一个聚类，用 Calinski-Harabasz 指数（CHI）度量帧间 token 嵌入的分离程度。CHI 越高的注意力头，其特征的帧间差异越大，运动定位能力越强。实验验证 CHI 与运动定位分数（MLS）的 Pearson 相关系数达 0.60。
- **逐层 Top-k 选择**：对每层选 CHI 最高的 top-5 个头，仅保留其视觉 token 嵌入 $\hat{\mathbf{h}}_x$ 计算 GramCol，避免存储所有头的特征。
- **IMAP 聚合**：在选定时间步、层和运动头上求 GramCol 均值，得到最终的可解释运动注意力图：$\text{IMAP}(c_m) = \frac{1}{|\mathcal{T}||\mathcal{L}||\hat{\mathcal{H}}|} \sum_{t,l,\hat{\eta}} \text{GramCol}(\hat{\mathbf{G}}, c_m)$。

### 损失函数/训练策略

本方法完全免训练（training-free）、免梯度（gradient-free），不涉及任何损失函数或优化过程。所有操作均在预训练 Video DiT 的推理过程中完成，仅需提取中间特征进行轻量计算。对于已有视频，可通过加噪-去噪（re-noising and denoising）以零样本方式获取显著性图。

## 实验关键数据

### 主实验

**运动定位基准**（504 视频，150 种运动类型，源自 MeViS 训练集）：

| 方法 | 骨干网络 | SL | TL | PR | SS | OBJ | Avg. |
|------|----------|------|------|------|------|------|------|
| ViCLIP | ViT-H | 0.33 | 0.17 | 0.35 | 0.29 | 0.28 | 0.28 |
| DAAM | VideoCrafter2 | 0.36 | 0.17 | 0.38 | 0.32 | 0.35 | 0.32 |
| Cross Attention | CogVideoX-5B | 0.41 | 0.27 | 0.43 | 0.34 | 0.33 | 0.36 |
| ConceptAttention | CogVideoX-5B | 0.50 | 0.32 | 0.51 | 0.47 | 0.47 | 0.45 |
| **IMAP** | **CogVideoX-5B** | **0.68** | **0.48** | **0.69** | **0.61** | **0.64** | **0.62** |
| Cross Attention | HunyuanVideo | 0.39 | 0.25 | 0.41 | 0.36 | 0.34 | 0.35 |
| **IMAP** | **HunyuanVideo** | **0.60** | **0.41** | **0.62** | **0.50** | **0.62** | **0.55** |

**零样本视频语义分割**（VSPW 验证集，343 视频，124 类别）：

| 方法 | 骨干网络 | mIoU | mVC8 | mVC16 |
|------|----------|------|------|-------|
| EmerDiff | SD 2.1 | 43.4 | 68.9 | 64.3 |
| VidSegDiff | SVD | 53.2 | 89.3 | 88.0 |
| Cross Attention | CogVideoX-5B | 16.8 | 71.5 | 59.1 |
| ConceptAttention | CogVideoX-5B | 25.0 | 80.4 | 72.1 |
| **GramCol (Ours)** | **CogVideoX-5B** | **28.9** | 75.2 | 66.0 |
| GramCol + AnyUp | CogVideoX-5B | **30.1** | 77.9 | 70.1 |

### 消融实验

CogVideoX-5B 上的组件消融：

| 配置 | SL | TL | PR | SS | OBJ | Avg. |
|------|------|------|------|------|------|------|
| Cross Attention（基线） | 0.41 | 0.27 | 0.43 | 0.34 | 0.33 | 0.36 |
| ConceptAttention w/ softmax | 0.50 | 0.32 | 0.51 | 0.47 | 0.47 | 0.45 |
| GramCol（全层） | 0.45 | 0.30 | 0.47 | 0.41 | 0.42 | 0.41 |
| + 层选择 | 0.47 | 0.34 | 0.48 | 0.48 | 0.50 | 0.46 |
| + 运动头选择 | 0.53 | 0.34 | 0.55 | 0.46 | 0.48 | 0.47 |
| **+ 两者（IMAP）** | **0.68** | **0.48** | **0.69** | **0.61** | **0.64** | **0.62** |
| IMAP w/ softmax | 0.61 | 0.55 | 0.62 | 0.58 | 0.66 | 0.60 |

### 关键发现

- IMAP 在 CogVideoX-5B 上的运动定位平均分 0.62，比 ConceptAttention 的 0.45 高出 37.8%，尤其在时间定位（TL）上从 0.32 提升到 0.48。
- GramCol 不加任何选择策略（0.41）即已超过所有不带 softmax 的基线方法，证明了 Gram 矩阵列作为显著性图的有效性。
- 层选择和运动头选择各自贡献约 +5% 和 +1% 的平均提升，两者结合后产生显著的协同效应（0.41 → 0.62）。
- 零样本分割中 GramCol mIoU 28.9，超过 ConceptAttention 的 25.0，证明了空间定位能力的通用性。
- QK-Matching 峰值位置的前景/背景定位准确率高达 0.9544，验证了文本代理 token 策略的可靠性。

## 亮点与洞察

- **核心创新点**：用 Gram 矩阵列（同模态相似度）替代跨模态点积，巧妙规避了视觉-文本特征空间异质性问题，天然保证正向高亮的可解释性。
- **运动头发现**：首次通过聚类分离度指标（CHI）量化地识别 Video DiT 中的运动相关注意力头，揭示了多头注意力在时空维度上的功能分化。
- **全自动、轻量级**：不需要训练、梯度计算或人工选择参数，文本代理 token 和运动头均自动选取，Gram 矩阵列只需取一列，计算开销极小。
- **通用性强**：适用于联合注意力（CogVideoX）和交叉注意力架构，可处理运动和非运动概念，并支持对已有视频零样本推理。

## 局限性

- 零样本视频分割 mIoU（30.1）与专用模型（DVIS++ 63.8、VidSegDiff 60.6）差距较大，当前主要价值在可解释性而非分割性能。
- 视频一致性（mVC）指标偏低（77.9 vs 专用模型的 90+），帧间显著性图的时间平滑性有待改进。
- 依赖 $\lambda_2$ 阈值和 top-k 头数等超参数，不同模型需要手动设定（如 CogVideoX 用 0.7，HunyuanVideo 用 0.75）。
- 评估指标 MLS 依赖 LLM（o3-pro）打分，可能引入主观性偏差。
- IMAP w/ softmax 在部分指标上有提升但帧间一致性下降，说明概念竞争问题并未完全解决。

## 相关工作

- **ConceptAttention**（ICML 2025）：用图像 DiT 的概念流生成显著性图，但仅限空间分割且依赖 softmax 概念竞争。本文的 GramCol 通过同模态 Gram 矩阵和自适应代理 token 解决了这两个问题。
- **DAAM**：利用 U-Net 交叉注意力图生成词级归因图，但在 Video DiT 上表现不佳（Avg. 0.32）。
- **DiTFlow / DiffTrack**：分别利用跨帧注意力做运动迁移和时间对应，关注帧间视觉 token 动态而非文本到运动的映射机制。
- **TokenRank**：将注意力图解释为马尔科夫链的转移矩阵，本文借鉴其 $\lambda_2$ 指标用于层选择。
- **Video DiT 注意力稀疏化**：SparseViDiT 等工作发现空间头和时间头的区分，本文进一步细化为"运动头"并用 CHI 量化。

## 评分

- 新颖性: ⭐⭐⭐⭐ — Gram 矩阵列作为显著性图的思路新颖，运动头的 CHI 量化识别有创见
- 实验充分度: ⭐⭐⭐⭐ — 三种 Video DiT、运动定位和零样本分割双任务评估、完整消融，但 MLS 依赖 LLM 评估有局限
- 写作质量: ⭐⭐⭐⭐ — 逻辑清晰，从空间到时空逐步推进，图表丰富
- 价值: ⭐⭐⭐⭐ — 为理解 Video DiT 内部运动生成机制提供了可解释工具，开源代码可复现
