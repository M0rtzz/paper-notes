---
title: >-
  [论文解读] Unleashing Video Language Models for Fine-grained HRCT Report Generation
description: >-
  [CVPR 2026][医学图像][CT报告生成] 提出 AbSteering 框架，通过异常中心的 Chain-of-Thought 训练和基于 DPO 的细粒度异常辨别，将通用视频语言模型（如 Qwen2.5-VL、InternVL3）适配到 HRCT 报告生成任务，以低成本超越专门的 CT 基础模型。
tags:
  - CVPR 2026
  - 医学图像
  - CT报告生成
  - 视频语言模型
  - Chain-of-Thought
  - DPO
  - 异常检测
---

# Unleashing Video Language Models for Fine-grained HRCT Report Generation

**会议**: CVPR 2026  
**arXiv**: [2603.12469](https://arxiv.org/abs/2603.12469)  
**arXiv**: [2603.12469](https://arxiv.org/abs/2603.12469)  
**代码**: 无  
**领域**: 医学图像  
**关键词**: CT报告生成, 视频语言模型, Chain-of-Thought, DPO, 异常检测  

## 一句话总结

提出 AbSteering 框架，通过异常中心的 Chain-of-Thought 训练和基于 DPO 的细粒度异常辨别，将通用视频语言模型（如 Qwen2.5-VL、InternVL3）适配到 HRCT 报告生成任务，以低成本超越专门的 CT 基础模型。

## 研究背景与动机

- **HRCT 报告生成挑战**：HRCT 包含数百层切片，病变稀疏、细微、多样，正常解剖结构占主导，使得异常识别极为困难
- **现有方法局限**：
  1. 早期方法将 CT 压缩为低维表示后复用 X-ray 报告生成器，信息损失严重
  2. 专用 CT 基础模型（RadFM, CT-CHAT, M3D）需要大量 CT 数据从头训练/微调，成本高
  3. 现有方法在长尾异常的细粒度识别上仍然薄弱
- **关键洞察**：
  1. HRCT 体积可以自然视为"视频般的切片序列"
  2. VideoLM 架构（时空 tokenization + 3D 注意力）与 CT 基础模型本质相似
  3. 差异不在架构而在训练数据：VideoLM 缺乏医学领域知识
- **核心问题**：能否通过高效的领域适配让通用 VideoLM 超越专用 CT 基础模型？

## 方法详解

### 整体框架：AbSteering（两阶段）

**Stage 1：异常中心的 Chain-of-Thought 训练**

1. 将原始报告标准化为统一的 (区域: 异常) 模板，覆盖 10 个解剖区域
2. 使用 GPT-4o 将报告按解剖区域分类，人工校验
3. CoT 训练：模型先生成异常检测列表 $R_{AB}$，再生成完整报告 $R_{Full}$

$$\mathcal{L}_{gen} = -\sum_{t=1}^{T} \log P(y_t | x, y_{<t}), \quad Y = [R_{AB}; R_{Full}]$$

强制模型在生成最终报告前先完成临床推理。

**Stage 2：基于 DPO 的细粒度异常辨别**

1. 构造硬负样本：GPT-4o 将真实异常替换为同一解剖区域内临床易混淆的异常
2. DPO 优化：让模型偏好正确报告 $y_w = R_{AB}$，排斥篡改报告 $y_l = R_{AB\_Fake}$

$$\mathcal{L}_{\text{DPO}} = \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x,v)}{\pi_{\text{ref}}(y_w|x,v)} - \beta \log \frac{\pi_\theta(y_l|x,v)}{\pi_{\text{ref}}(y_l|x,v)} \right)$$

### 数据集构建

CT-RATE-AB：基于 CT-RATE 数据集（25,692 次非造影胸部 CT），将每个 CT 转为 240 帧 480×480 MP4，帧率 18fps。训练集 46,717 扫描，验证集 3,039 扫描。

## 实验关键数据

### 主实验：CT-RATE 基准

| 方法 | CE Micro F1 | CE Macro F1 | CE Weighted F1 |
|------|------------|------------|---------------|
| CT2Rep | 14.10 | 10.65 | 11.35 |
| M3D-8B | 35.69 | 26.74 | 33.13 |
| CT-CHAT | 30.08 | 21.66 | 28.35 |
| InternVL3-8B | 44.45 | 38.91 | 43.28 |
| **InternVL3-AbSteer** | **54.55** | **47.66** | **52.80** |
| Qwen2.5-VL-AbSteer | 45.99 | 37.90 | 44.05 |

InternVL3-AbSteer 在所有临床效能指标上显著超越专用 CT 基础模型。

### 关键发现

1. **通用 VideoLM 可迁移**：未经 steering 的 InternVL3 已经可与 M3D-8B 持平
2. **AbSteering 大幅提升**：InternVL3 经 AbSteering 后 Macro F1 从 38.91→47.66（+22.5%）
3. **超越专用基础模型**：无需从头训练 CT 特定编码器

### 消融实验

1. **CoT vs DPO**：CoT 大幅提升 recall，DPO 进一步提升 precision 并抑制幻觉
2. **视频预训练重要**：从头训练导致急剧性能下降；冻结编码器即已足够，LoRA 微调无额外增益
3. **LLM 规模**：3B→7B 有提升，7B→32B 反而下降，瓶颈在视觉-文本对齐而非 LLM 容量

## 亮点与洞察

1. **跨模态迁移范式**：证明通用视频预训练的时空推理能力可高效迁移到 3D 医学影像
2. **两阶段方法设计精巧**：CoT 解决异常召回问题，DPO 解决细粒度辨别和幻觉问题
3. **实用性强**：相比从头训练 CT 基础模型，仅需少量标注和两阶段微调
4. **数据贡献**：CT-RATE-AB 结构化数据集有助于社区

## 局限性

- 仅在 CT-RATE 单一数据集上验证，未覆盖腹部/头颅 CT 等其他部位
- 依赖 GPT-4o 进行报告结构化和硬负样本构造，引入额外成本和潜在偏差
- CT 转 MP4 的预处理损失了 HU 值精度
- 32B 模型性能下降暗示当前方案在更大规模上可能遇到瓶颈

## 评分

| 维度 | 评分 |
|------|------|
| 新颖性 | ⭐⭐⭐⭐ |
| 实验 | ⭐⭐⭐⭐ |
| 写作 | ⭐⭐⭐⭐ |
| 价值 | ⭐⭐⭐⭐ |
