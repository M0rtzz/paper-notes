---
title: >-
  [论文解读] Visual Autoregressive Modeling for Instruction-Guided Image Editing
description: >-
  [ICLR 2026][图像生成][视觉自回归] VAREdit将指令引导图像编辑重构为next-scale预测问题，提出Scale-Aligned Reference (SAR)模块解决最细尺度条件与粗目标特征间的尺度不匹配，在EMU-Edit和PIE-Bench上GPT-Balance分数超越最强扩散基线64.9%和45.3%，512×512编辑仅需1.2秒。
tags:
  - ICLR 2026
  - 图像生成
  - 视觉自回归
  - 图像编辑
  - 多尺度预测
  - 尺度对齐参考
  - 指令引导
---

# Visual Autoregressive Modeling for Instruction-Guided Image Editing

**会议**: ICLR 2026  
**arXiv**: [2508.15772](https://arxiv.org/abs/2508.15772)  
**代码**: https://github.com/HiDream-ai/VAREdit  
**领域**: 图像编辑  
**关键词**: 视觉自回归, 图像编辑, 多尺度预测, 尺度对齐参考, 指令引导

## 一句话总结
VAREdit将指令引导图像编辑重构为next-scale预测问题，提出Scale-Aligned Reference (SAR)模块解决最细尺度条件与粗目标特征间的尺度不匹配，在EMU-Edit和PIE-Bench上GPT-Balance分数超越最强扩散基线64.9%和45.3%，512×512编辑仅需1.2秒。

## 研究背景与动机

**领域现状**：指令引导图像编辑主导方法基于扩散模型（InstructPix2Pix, UltraEdit等），通过通道拼接源图和目标图训练。AnySD、OmniGen等进一步扩展，但均受扩散范式的固有限制。

**现有痛点**：(1) 扩散模型的全局去噪过程将编辑区域与整幅图像上下文纠缠，导致意外修改（spurious modifications）；(2) 多步去噪计算成本高，限制实时应用；(3) 早期AR编辑尝试（training-free）缺乏任务特定知识，显著落后于扩散方法。

**核心矛盾**：AR模型的因果组合机制天然适合编辑（保留不变区域+精确修改编辑区域），但将VAR的多尺度生成适配到编辑任务面临尺度不匹配挑战。

**本文要解决什么**：如何将VAR范式有效应用于指令引导图像编辑，解决源图条件化中的尺度不匹配问题？

**切入角度**：通过系统分析全尺度模型的注意力模式，发现第一层自注意力需要尺度对齐的参考，后续层只需最细尺度条件。

**核心idea一句话**：仅在第一个自注意力层注入尺度对齐的源参考（通过下采样最细尺度特征生成），其余层使用最细尺度条件，兼顾全局布局和局部细节。

## 方法详解

### 整体框架
基于预训练VAR模型（Infinity），输入源图像经共享VQ编码器得到多尺度残差，文本指令经编码器映射。模型自回归生成目标残差 $\mathbf{R}_{1:K}^{(tgt)}$：$p(\mathbf{R}_{1:K}^{(tgt)} | \mathbf{I}^{(src)}, \mathbf{t}) = \prod_{k=1}^K p(\mathbf{R}_k^{(tgt)} | \mathbf{F}_{1:k-1}^{(tgt)}, \mathbf{F}_K^{(src)}, \mathbf{t})$

### 关键设计

1. **源图条件化策略分析**:

    - 全尺度条件：prepend所有尺度源token→计算量二次增长 $O(n^2)$，可能引入冗余
    - 最细尺度条件：仅用 $\mathbf{F}_K^{(src)}$→计算高效但存在尺度不匹配（细粒度信息无法指导粗尺度预测）

2. **尺度依赖性分析（关键发现）**:

    - 在全尺度训练模型上分析自注意力热图
    - **第一层**：注意力广泛分布，聚焦对应和所有更粗的源尺度→负责全局布局
    - **后续层**：注意力高度局部化，呈对角线结构→负责局部细化
    - 结论：第一层需要尺度对齐参考，后续层仅需最细尺度即可

3. **Scale-Aligned Reference (SAR)模块**:

    - 对最细尺度特征下采样生成各尺度参考：$\mathbf{F}_k^{(ref)} = \text{Down}(\mathbf{F}_K^{(src)}, (h_k, w_k))$
    - 仅在第一个自注意力层，预测scale $k$ 时拼接对应尺度参考：
   $\hat{\mathbf{O}}_k^{(tgt)} = \text{Softmax}\left(\frac{\mathbf{Q}_k^{(tgt)} [\mathbf{K}_k^{(ref)\top}, \mathbf{K}_{1:k}^{(tgt)\top}]}{\sqrt{d}}\right) \cdot [\mathbf{V}_k^{(ref)\top}, \mathbf{V}_{1:k}^{(tgt)\top}]^\top$
    - 其余层仍使用最细尺度条件+因果目标历史

4. **文本条件化**:

    - 文本编码为token嵌入，pooled表示作为 $\tilde{\mathbf{F}}_0^{(tgt)}$（启动token）
    - 文本token嵌入用于交叉注意力的key/value矩阵
    - 源token通过2D-RoPE位置偏移 $\Delta=(64,64)$ 与目标token区分

### 训练策略
- 初始化自Infinity预训练权重
- VAREdit-2B：256×256（8k iter）→512×512（7k iter）两阶段
- VAREdit-8B：512×512直接训练60k iter
- 优化bitwise分类器损失
- 推理：CFG $\eta=4$，logits温度 $\tau=0.5$

## 实验关键数据

### EMU-Edit和PIE-Bench

| 方法 | 大小 | EMU-Edit GPT-Bal. | PIE-Bench GPT-Bal. | 时间 |
|------|------|-------------------|--------------------|----|
| InstructPix2Pix | 1.1B | 2.923 | 4.034 | 3.5s |
| UltraEdit | 7.7B | 4.541 | 5.580 | 2.6s |
| OmniGen | 3.8B | 4.666 | 3.498 | 16.5s |
| ICEdit | — | 4.786 | — | — |
| **VAREdit-2B** | **2B** | **7.074** | **7.609** | **0.7s** |
| **VAREdit-8B** | **8B** | **7.892** | **8.105** | **1.2s** |

### 前沿方法对比

| 方法 | 大小 | EMU-Edit GPT-Bal. | PIE-Bench GPT-Bal. |
|------|------|-------------------|-------------------|
| GPT-4o-Image | — | 8.549 | 8.616 |
| Step1X-Edit | — | 7.378 | 7.488 |
| Qwen-Image-Edit | 20B | 8.087 | 8.272 |
| **VAREdit-8B** | **8B** | **7.892** | **8.105** |

### 关键发现
- GPT-Balance超过最强基线ICEdit 64.9%（EMU-Edit）和最强UltraEdit 45.3%（PIE-Bench）
- VAREdit-2B仅0.7秒完成编辑，比UltraEdit快3.7倍
- 在GPT-Suc.≥9的高质量编辑子集上，VAREdit的GPT-Over.也最高——真正做到"编得准+保留好"
- SAR模块消融：去掉SAR后GPT-Bal.显著下降，验证了尺度对齐的必要性
- 开源方法中仅次于Qwen-Image-Edit (20B)，但后者模型大2.5倍

## 亮点与洞察
- **范式转换**：首次将VAR的next-scale预测成功应用于图像编辑，证明AR在编辑任务上相比扩散有本质优势
- **注意力分析驱动的设计**：SAR不是凭直觉设计，而是通过系统分析全尺度模型的注意力模式得出，方法论值得借鉴
- **效率优势显著**：AR的单步生成比扩散的多步去噪天然更快，1.2秒完成高质量编辑
- **GPT-Balance指标的重要性**：揭示OmniGen等方法通过"不编辑"获得高GPT-Over.的策略，GPT-Bal.更全面

## 局限性 / 可改进方向
- 依赖VQ tokenizer的重建质量，精细纹理可能有损失
- 当前最大512×512分辨率，高分辨率编辑待扩展
- SAR中的下采样操作可能丢失重要空间信息
- 可以探索将SAR推广到视频编辑的时空多尺度场景

## 相关工作与启发
- **vs InstructPix2Pix范式**：通道拼接+扩散的根本问题是全局去噪导致纠缠，VAREdit的因果机制天然避免
- **vs EditAR**：遵循vanilla next-token预测，有结构退化风险；VAREdit使用next-scale预测
- **vs Infinity**：VAREdit继承其多尺度残差量化器和位编码分类器，在此基础上适配编辑任务

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ VAR首次用于编辑+SAR的设计来自深入分析，创新性强
- 实验充分度: ⭐⭐⭐⭐⭐ 四个基准、多种对比、消融、效率分析全面
- 写作质量: ⭐⭐⭐⭐⭐ 从动机到分析到设计的逻辑严密，注意力热图可视化出色
- 价值: ⭐⭐⭐⭐⭐ 开辟VAR编辑新方向，性能和效率双优
