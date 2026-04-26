---
title: >-
  [论文解读] LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings
description: >-
  [CVPR 2026][医学图像][手术数据集] 构建了当前最大的开放手术视频数据集 LEMON（4194 视频、938 小时、35 种术式），并提出基于增强知识蒸馏的基础模型 LemonFM，在手术阶段识别、工具检测、动作识别和语义分割四项下游任务上全面超越现有方法。
tags:
  - CVPR 2026
  - 医学图像
  - 手术数据集
  - 基础模型
  - 自监督学习
  - 数据清洗管道
  - 知识蒸馏
---

# LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings

**会议**: CVPR 2026  
**arXiv**: [2503.19740](https://arxiv.org/abs/2503.19740)  
**代码**: [https://github.com/visurg-ai/LEMON](https://github.com/visurg-ai/LEMON)  
**领域**: 医学图像 / 手术视觉  
**关键词**: 手术数据集, 基础模型, 自监督学习, 数据清洗管道, 知识蒸馏

## 一句话总结

构建了当前最大的开放手术视频数据集 LEMON（4194 视频、938 小时、35 种术式），并提出基于增强知识蒸馏的基础模型 LemonFM，在手术阶段识别、工具检测、动作识别和语义分割四项下游任务上全面超越现有方法。

## 研究背景与动机

1. **领域现状**：传统手术数据集通常少于 100 个视频和 30 小时，导致模型泛化性差。自监督学习虽减少了对标注数据的依赖，但缺乏大规模高质量手术数据。
2. **现有痛点**：GenSurgery 和 SurgeNetXL 虽扩大了规模，但缺乏数据清洗步骤，混入了非手术内容（会议演讲、患者证词等）导致噪声特征。
3. **核心矛盾**：手术数据受隐私法规和标注成本限制，如何利用公开可用的在线视频构建高质量大规模数据集。
4. **本文目标**：设计系统化的数据清洗管道从 YouTube 视频中策展高质量手术数据集。
5. **切入角度**：多阶段自动化清洗（分类→剪裁→预处理→标注）+ 人工质控。
6. **核心 idea**：增强知识蒸馏方法利用跨患者外观相似性和相邻帧运动不变性来学习更好的手术视觉表征。

## 方法详解

### 整体框架

数据方面：YouTube 视频收集 → 故事板分类 → 帧级分类与剪裁 → 非手术内容消除 → 标注验证。模型方面：基于 DINO 框架的增强知识蒸馏，ConvNeXt-L 骨干。

### 关键设计

1. **多阶段数据清洗管道**:

    - 功能：从 18K 原始视频中策展出 4194 个高质量手术视频
    - 核心思路：(1) 视频级：用故事板分类器（ResNet18）过滤非手术视频；(2) 帧级：训练帧分类器定位手术内容起止，剪裁前后非手术片段，丢弃手术帧占比 <90% 的视频；(3) 区域级：训练 YOLOv8 检测并遮蔽帧内非手术区域（UI 元素、Logo 等）。
    - 设计动机：每层过滤使用独立模型并经人工验证，实现视频级 100% 精确率和帧级 >99.9% 精确率。

2. **增强知识蒸馏方法**:

    - 功能：学习对微小运动和跨患者外观变化不变的手术表征
    - 核心思路：在 DINO 的 student-teacher 框架基础上引入额外监督信号 $W_i$。$W_i$ 由两张图像组成，优先从同类术式其他视频中检索外观相似帧（余弦距离 < 3× 相邻帧距离），不足时用时间相邻帧补充。损失函数为 $\mathcal{L} = -\sum_i \sum_{u \in U_i} \sum_{v \in V_i \cup W_i} P_t(z|u) \log P_s(z|v)$。
    - 设计动机：标准 DINO 仅学习同一图像不同增强的不变性，增强蒸馏额外引入跨患者和跨帧的不变性。

3. **视频分类模型 LemonFM-Vid**:

    - 功能：利用 LemonFM 帧嵌入进行视频级术式分类
    - 核心思路：基于帧的典型性（typicality，K-NN 距离的倒数）加权聚合帧嵌入得到视频嵌入 $v_e = \sum_j \omega_j \phi_j$，再用单层 MLP 分类。
    - 设计动机：手术流程本地化于特定身体区域，特征性场景可与术式关联。

### 损失函数 / 训练策略

DINO 交叉熵损失 + 增强数据对。8 × V100 GPU 训练 60 epoch。

## 实验关键数据

### 主实验

| 任务/数据集 | 指标 | LemonFM | SurgeNetXL (之前SOTA) | 提升 |
|------------|------|---------|----------------------|------|
| AutoLaparo 阶段识别 | Jaccard | 64.8 | 55.1 | +9.7pp |
| Cholec80 阶段识别 | Jaccard | 85.1 | 72.0 | +13.1pp |
| Cholec80 工具检测 | mAP | 93.7 | 86.5 | +7.2pp |
| GraSP 工具检测 | mAP | 94.4 | 83.8 | +10.6pp |
| CholecT50 动作识别 | mAP | 61.9 | 57.5 | +4.4pp |
| CholecSeg8k 语义分割 | mDice | 81.3 | 69.0 | +12.3pp |

### 消融实验

| 配置 | AutoLaparo (F1) | CholecSeg8k (mDice) | 说明 |
|------|----------------|---------------------|------|
| ImageNet 预训练 | 53.0 | 64.4 | 通用预训练 |
| Cholec80 (51h) | 46.9 | 64.1 | 小规模手术数据 |
| LEMON (未清洗) | 61.4 | 67.4 | 无清洗管道 |
| LEMON (清洗) | 65.9 | 68.7 | 清洗提升 +4.5pp |
| LEMON + 增强蒸馏 | 66.9 | 71.9 | 完整模型 |

### 关键发现

- 数据清洗管道贡献显著：F1 提升 4.5pp，mDice 提升 1.3pp
- ConvNeXt 优于 ViT，尤其在分割任务上（+10.7pp mDice），因卷积归纳偏置保留细粒度手术细节
- 仅用 50% 标注数据微调的 LemonFM 仍超越所有 100% 数据的基础模型
- 判别式预训练（DINO 系列）显著优于生成式预训练（MAE 系列）

## 亮点与洞察

- **数据规模的质量保证**：从 18K 原始视频策展到 4194 个高质量视频的严格管道，实现前所未有的规模与质量平衡
- **跨患者增强蒸馏**：利用同类术式不同患者的视频学习外观不变性，巧妙利用了术式标注
- **全面基准**：在 6 个数据集 4 个任务上提供完整评估，建立了手术视觉基础模型的标准

## 局限与展望

- 数据来源为 YouTube 公开视频，虽有伦理考量但仍存在潜在争议
- 术式分类 mAP 仅 57.8%，解剖相邻术式间存在显著混淆
- 未来将开发手术专用视频基础模型

## 相关工作与启发

- **vs Endo-FM**: Endo-FM 用私有数据训练，限制可复现性；LEMON 完全开源
- **vs EndoViT**: EndoViT 合并多个小型公开数据集，规模和性能远不如 LEMON
- **vs SurgeNetXL**: SurgeNetXL 缺乏数据清洗，LEMON 的清洗管道带来显著提升

## 评分

- 新颖性: ⭐⭐⭐⭐ 增强蒸馏设计新颖，数据清洗管道系统化
- 实验充分度: ⭐⭐⭐⭐⭐ 6 数据集 4 任务 + 低数据量实验 + 交叉验证 + 全面消融
- 写作质量: ⭐⭐⭐⭐⭐ 结构清晰，细节充分
- 价值: ⭐⭐⭐⭐⭐ 数据集和模型都将成为手术视觉领域的重要基础资源

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision](learning_generalizable_3d_medical_image_representations_from_mask-guided_self-su.md)
- [\[CVPR 2026\] Focus-to-Perceive Representation Learning: A Cognition-Inspired Hierarchical Framework for Endoscopic Video Analysis](focus-to-perceive_representation_learning_a_cognition-inspired_hierarchical_fram.md)
- [\[CVPR 2026\] Benchmarking Endoscopic Surgical Image Restoration and Beyond](benchmarking_endoscopic_surgical_image_restoration_and_beyond.md)
- [\[CVPR 2026\] Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](developing_foundation_models_for_universal_segment.md)
- [\[CVPR 2026\] MIL-PF: Multiple Instance Learning on Precomputed Features for Mammography Classification](mil-pf_multiple_instance_learning_on_precomputed_features_for_mammography_classi.md)

<!-- RELATED:END -->
