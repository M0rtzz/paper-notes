---
title: >-
  [论文解读] UniCode: Learning a Unified Codebook for Multimodal Large Language Models
description: >-
  [ECCV 2024][多模态][统一码本] 提出UniCode，通过语言驱动的迭代训练范式学习一个统一码本，使LLM的词表可同时量化视觉和文本信号，无需额外对齐模块即可实现多模态理解与生成，并引入上下文图像解压缩任务提升生成质量。
tags:
  - ECCV 2024
  - 多模态
  - 统一码本
  - 视觉量化
  - 多模态生成
  - 图像解压缩
  - 视觉指令微调
---

# UniCode: Learning a Unified Codebook for Multimodal Large Language Models

**会议**: ECCV 2024  
**arXiv**: [2403.09072](https://arxiv.org/abs/2403.09072)  
**代码**: 无  
**领域**: 多模态VLM  
**关键词**: 统一码本, 视觉量化, 多模态生成, 图像解压缩, 视觉指令微调

## 一句话总结

提出UniCode，通过语言驱动的迭代训练范式学习一个统一码本，使LLM的词表可同时量化视觉和文本信号，无需额外对齐模块即可实现多模态理解与生成，并引入上下文图像解压缩任务提升生成质量。

## 研究背景与动机

1. **领域现状**：当前MLLM主要通过轻量级投影模块（如MLP）将视觉特征映射到LLM文本空间，在多模态理解上表现优异，但本质上仍限于文本生成，无法生成图像等非语言内容。
2. **现有痛点**：扩展LLM码本以加入视觉token（如Unified-IO 2）虽可行，但面临模态间巨大鸿沟、参数膨胀和codebook collapse问题；使用冻结LLM码本做视觉量化（如LQAE）则重建质量差。
3. **核心矛盾**：视觉量化需要专用码本以保证重建质量，但专用码本与LLM词表不兼容；而LLM词表虽可解释性强但不适合直接做视觉量化。
4. **本文要解决什么**：能否学习一个统一码本，同时高效量化视觉和文本信号，不需要额外的视觉-文本对齐模块。
5. **切入角度**：在视觉tokenizer和LLM之间交替训练，用指数移动平均将LLM码本渐进融入视觉量化码本。
6. **核心idea一句话**：通过语言驱动的迭代训练使视觉量化码本收敛到LLM词表空间，实现真正的统一码本。

## 方法详解

### 整体框架

UniCode基于VQ-VAE视觉tokenizer和LLM构建，去掉了传统MLLM中的多模态投影模块。两阶段训练：Stage I学习统一码本（交替训练视觉tokenizer和LLM），Stage II多模态指令微调（冻结视觉编解码器，微调LLM）。

### 关键设计

**1. 失败方案分析**
- 做什么：作者先尝试了两种朴素方案并分析失败原因
- 核心思路：
    - 冻结LLM码本：视觉tokenizer无法在固定码本上获得好的重建质量，尤其对堆叠量化更严重
    - 双交替训练：每步直接用对方的码本替换自己的，但视觉的码本变化速率远大于LLM，导致LLM能力损坏
- 设计动机：这两个失败方案清晰地揭示了码本同步的核心挑战

**2. 语言驱动迭代训练**
- 做什么：用EMA(指数移动平均)平滑地将LLM码本融入视觉tokenizer
- 核心思路：C' = λC + (1-λ)I·Z（正常EMA更新），定期用C' = λC + (1-λ)C_L替换（将LLM码本注入）
- 设计动机：EMA保证码本变化平稳，LLM梯度不受视觉更新干扰，视觉码本渐进收敛到LLM空间。关键——不让视觉更新反向影响LLM

**3. 堆叠量化支持**
- 做什么：支持HQ(层次量化)和RQ(残差量化)等堆叠量化方法
- 核心思路：将图像压缩为D层码图，每个位置的最终嵌入是D层量化向量的聚合（HQ用拼接，RQ用累加）
- 设计动机：堆叠量化大幅减少视觉token数量（降低特征分辨率），使LLM在有限token长度内处理完整图像

**4. 上下文图像解压缩任务**
- 做什么：设计新的预训练任务——给LLM压缩后的量化嵌入Z^，让它生成完整的多层码图M^
- 核心思路：将图像分为T段，构造多轮对话格式：压缩嵌入→完整码序列的in-context learning
- 设计动机：堆叠量化导致聚合嵌入与LLM词嵌入不完全对齐，解压缩任务迫使LLM学习理解压缩视觉表示

**5. 多模态指令微调扩展**
- 做什么：将text-to-image数据（CC3M）转化为指令-答案格式，与VQA数据混合训练
- 核心思路：统一码本使图像token直接对应LLM词表中的entry，图像生成变成token序列预测
- 设计动机：传统MLLM的指令微调仅覆盖文本生成，UniCode通过统一码本自然支持图像生成指令

### 损失函数 / 训练策略

- Stage I：视觉tokenizer用图像重建损失训练（LCS-558K数据），LLM用预训练文本数据。交替训练，EMA同步码本
- Stage II：冻结编解码器，微调LLM，用Mixed-665K + CC3M + 图像解压缩数据，负对数似然损失
- 无多模态对齐阶段——这是与LLaVA等方法的关键区别

## 实验关键数据

### 主实验

| 方法 | 范式 | VQAv2 | GQA | 图像生成FID |
|------|------|-------|-----|-----------|
| LLaVA | vis enc+text tok | 78.5 | 62.0 | - |
| SEED-LLaMA | vis tok+text tok | - | - | 有 |
| **UniCode** | **unified tok** | **对标** | **对标** | **有（更轻量）** |

### 消融实验

| 码本学习策略 | 重建质量 | LLM保留 |
|------------|---------|---------|
| 冻结LLM码本 | 差 | ✓ |
| 双交替训练 | 中 | 损坏 |
| 语言驱动迭代(ours) | 好 | ✓ |

| 组件 | 效果 |
|------|------|
| 无解压缩任务 | 生成质量显著下降 |
| 有解压缩任务 | 生成质量提升 |
| HQ量化 | 减少token数，质量可接受 |

### 关键发现

1. **统一码本可行**：视觉和文本可以共享同一码本，且不需要额外对齐模块
2. 语言驱动迭代训练的关键是"不让视觉更新污染LLM"——单向注入而非双向同步
3. 图像解压缩任务对弥补堆叠量化导致的信息损失至关重要
4. 使用显著更少的参数和训练数据（vs Emu的10亿参数视觉编码器+8000万样本），UniCode达到了可比性能
5. 统一码本使得多模态I/O变成了纯粹的序列建模问题

## 亮点与洞察

- **码本统一的哲学**：与其在LLM外面"接"视觉模块，不如从词表层面统一——这可能是MLLM的终极形态
- **反向思考**："不让视觉影响LLM"比"双向同步"更好，说明当前阶段保护LLM能力比适应视觉更重要
- **解压缩任务的巧妙**：将堆叠量化的信息瓶颈转化为学习机会
- **极致简洁**：去掉多模态投影模块后，架构前所未有地轻量

## 局限性 / 可改进方向

1. 图像生成质量仍不如专用模型（如DALL-E），统一码本在视觉保真度上有天然局限
2. 视觉重建在极细节区域（如文字、小物体）的质量有待提升
3. 仅在LCS-558K上训练视觉tokenizer，更大规模数据可能进一步提升
4. 当前码本大小受限于LLM词表（通常32K-64K），可能不够表达复杂视觉内容
5. 尚未在视频等更复杂模态上验证

## 相关工作与启发

- **VQ-VAE/RQ-VAE**：视觉量化基础工作，UniCode将其与LLM词表统一
- **LQAE**：用冻结BERT码本做视觉量化，但效果不佳，UniCode的迭代方案更好
- **Emu/Unified-IO 2**：扩展码本的方案，需要海量资源，UniCode更高效
- **启发**：模态统一可能不在特征空间而在"符号"空间——token化是通向统一的关键路径

## 评分

- **新颖性**: ⭐⭐⭐⭐⭐ (统一码本+语言驱动迭代是全新范式)
- **技术深度**: ⭐⭐⭐⭐ (失败方案分析深入，解决方案优雅)
- **实验充分性**: ⭐⭐⭐⭐ (理解+生成+重建多维度验证)
- **写作质量**: ⭐⭐⭐⭐ (动机阐述清晰，范式对比图示直观)
- **影响力**: ⭐⭐⭐⭐ (指向MLLM统一I/O的可能方向)

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] GENIXER: Empowering Multimodal Large Language Model as a Powerful Data Generator](genixer_empowering_multimodal_large_language_model_as_a_powe.md)
- [\[ECCV 2024\] UMBRAE: Unified Multimodal Brain Decoding](umbrae_unified_multimodal_brain_decoding.md)
- [\[ECCV 2024\] Uni3DL: Unified Model for 3D and Language Understanding](uni3dl_a_unified_model_for_3d_vision-language_understanding.md)
- [\[ECCV 2024\] Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](groma_localized_visual_tokenization_for_grounding_multimodal.md)
- [\[ECCV 2024\] FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](freemotion_mocapfree_human_motion_synthesis_with_multimodal_.md)

<!-- RELATED:END -->
