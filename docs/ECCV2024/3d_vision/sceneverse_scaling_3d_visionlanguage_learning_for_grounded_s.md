---
title: >-
  [论文解读] SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding
description: >-
  [ECCV 2024][3D视觉][3D视觉语言] 提出SceneVerse——首个百万级3D视觉语言数据集（68K场景+250万语言描述），通过结合人工标注和基于场景图的自动生成pipeline构建多粒度描述，并设计GPS预训练框架实现多层次场景-文本对齐，在3D grounding和QA基准上达到SOTA。
tags:
  - ECCV 2024
  - 3D视觉
  - 3D视觉语言
  - 数据扩展
  - 场景图
  - 预训练
  - 3D grounding
---

# SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding

**会议**: ECCV 2024  
**arXiv**: [2401.09340](https://arxiv.org/abs/2401.09340)  
**代码**: [https://scene-verse.github.io](https://scene-verse.github.io)  
**领域**: 3D视觉  
**关键词**: 3D视觉语言, 数据扩展, 场景图, 预训练, 3D grounding

## 一句话总结

提出SceneVerse——首个百万级3D视觉语言数据集（68K场景+250万语言描述），通过结合人工标注和基于场景图的自动生成pipeline构建多粒度描述，并设计GPS预训练框架实现多层次场景-文本对齐，在3D grounding和QA基准上达到SOTA。

## 研究背景与动机

1. **领域现状**：2D视觉语言领域因大规模数据和对比预训练取得巨大成功（CLIP等），但3D场景理解的语言grounding仍处于初期阶段。
2. **现有痛点**：(a) 3D数据收集依赖扫描设备，远比2D昂贵，现有数据集仅限数千场景；(b) 3D场景包含大量物体实例、丰富属性和复杂空间关系，需要的语言描述量远超2D；(c) 缺乏统一的预训练框架来整合多层次的3D-语言对齐。
3. **核心矛盾**：3D grounding需要丰富的空间关系描述和精确的物体级标注，但人工标注成本极高，自动生成的描述又往往质量不足。
4. **本文要解决什么**：通过系统性的数据扩展和统一预训练，打破3D视觉语言学习的数据和方法瓶颈。
5. **切入角度**：利用3D场景图的结构化表示作为中间桥梁，结合LLM自动生成多粒度语言描述。
6. **核心idea一句话**：数据扩展+统一预训练是3D-VL成功的关键路径，场景图+LLM是实现大规模高质量数据的可扩展方案。

## 方法详解

### 整体框架

SceneVerse = 数据集 + GPS预训练框架。数据集统一了7个来源的3D场景（真实+合成），包含三种粒度的语言描述：场景描述（全局）、物体描述（属性）和物体引用（空间关系）。GPS通过多层级对比对齐在SceneVerse上预训练。

### 关键设计

**1. 3D场景统一策略**
- 做什么：整合ScanNet、ARKitScenes、HM3D、3RScan、MultiScan（真实）+ Structured3D、ProcTHOR（合成），共68,406场景
- 核心思路：统一预处理——房间分割、点采样、轴对齐、归一化、语义标签对齐。每个扫描表示为P∈R^{N×8}（3D坐标+RGB+实例ID+语义标签）
- 设计动机：单个数据集规模不够，统一后数量级提升；合成数据作为可扩展的补充来源

**2. 人工标注引用表达**
- 做什么：96,863条新标注的上下文丰富的物体引用描述
- 核心思路：标注员在3D场景中为单个物体写20字以上的独特引用文。每条引用经两名独立审校员验证（需在3D场景中准确定位目标物体）
- 设计动机：高质量的人工标注作为ground truth基准，覆盖ARKitScenes、HM3D、MultiScan三个数据集

**3. 基于场景图的自动语言生成**
- 做什么：从3D场景图出发，用模板+LLM生成三种粒度的描述
- 核心思路：
    - 物体描述：多视角图像→BLIP2生成初始描述→CLIP筛选最高质量→LLM精炼总结
    - 物体引用：从场景图提取空间关系三元组(target,relation,anchor)→设计多种模板（主动/被动/倒装）→LLM改写增加自然度
    - 场景描述：随机采样场景图子集→连同物体属性和房间类型→提示LLM生成全局描述
- 设计动机：模板保证描述的准确性和全面性，LLM提升自然度和多样性

**4. GPS预训练框架**
- 做什么：多层级场景-文本对比对齐
- 核心思路：
    - 物体级对齐：物体点云特征与对应描述的对比学习
    - 场景级对齐：聚合场景内物体特征与场景描述的对比学习
    - 引用级对齐：物体特征与引用描述中物体位置的对比学习
- 设计动机：不需要辅助损失（如检测/分割损失），纯对比对齐就足够，保持框架简洁

### 损失函数 / 训练策略

- 多层级对比损失：InfoNCE变体，同时在物体级、场景级和引用级对齐
- Transformer-based架构处理点云和文本
- 预训练后可在下游任务（grounding、QA）上微调
- 数据总量：250万场景-语言对

## 实验关键数据

### 主实验

| 方法 | ScanRefer Acc@0.25 | ScanRefer Acc@0.5 | ScanQA | SQA3D |
|------|-------------------|-------------------|--------|-------|
| 之前SOTA | 基线 | 基线 | 基线 | 基线 |
| **GPS (SceneVerse)** | **新SOTA** | **新SOTA** | **新SOTA** | **新SOTA** |

### 消融实验

| 数据规模 | Grounding性能 |
|---------|--------------|
| ScanNet only | 基线 |
| + 合成数据 | 显著提升 |
| + 多源真实数据 | 再提升 |
| 全部SceneVerse | 最优 |

| 语言类型 | 贡献 |
|---------|------|
| 仅人工标注 | 基于有限但高质量 |
| + 模板生成 | 显著提升（覆盖更多空间关系） |
| + LLM改写 | 进一步提升（更自然的表达） |
| 全部 | 最优 |

### 关键发现

1. **数据扩展效果普遍**：不仅GPS受益，其他模型在3D语义分割等任务上也因更多数据而性能提升
2. 合成数据（Structured3D等）虽然视觉逼真度有限，但在预训练中仍有显著贡献
3. LLM改写后的描述vs模板描述：改写版本性能更优，说明语言自然度对预训练很重要
4. GPS在zero-shot迁移中展现了涌现能力——无需微调即可在新场景中进行基本的grounding
5. 多层级对齐（场景+物体+引用）均不可或缺，去掉任何一级都导致性能下降

## 亮点与洞察

- **数据规模是王道**：2D-VL的成功经验（大规模数据+对比预训练）在3D场景中同样有效
- **场景图作为桥梁**：结构化中间表示使得大规模高质量语言生成成为可能
- **人工+自动的互补**：9.7万条人工标注确保质量基准，210万条自动生成覆盖规模
- **合成数据的价值**：即使不完美的合成场景也能为预训练提供有价值的空间关系学习信号
- **zero-shot涌现**：预训练后的GPS展示了在未见场景中的基本grounding能力

## 局限性 / 可改进方向

1. 自动生成的描述质量虽有LLM改写，但仍不如人工标注精确
2. 合成场景虽然补充了数量，但与真实场景存在domain gap
3. GPS的架构相对简单（纯对比学习），可能在需要推理的任务上有局限
4. 当前仅关注室内场景，室外大规模场景的扩展有待研究
5. 场景图构建本身依赖现有标注，全自动的端到端pipeline仍有改进空间

## 相关工作与启发

- **ScanRefer/ReferIt3D**：3D引用表达数据集，SceneVerse在规模上提升数量级
- **LEO/3D-LLM**：3D多任务学习方法，SceneVerse提供更大规模的数据基础
- **Cap3D**：3D物体级描述数据集，SceneVerse扩展到场景级
- **启发**：3D-VL的瓶颈在数据而非方法——当数据量足够时，简单的对比预训练就能取得优异效果

## 评分

- **新颖性**: ⭐⭐⭐⭐ (数据构建范式和GPS框架有价值)
- **技术深度**: ⭐⭐⭐⭐ (多层级对齐设计合理，数据生成pipeline完善)
- **实验充分性**: ⭐⭐⭐⭐⭐ (多任务评测+数据扩展分析+zero-shot验证)
- **写作质量**: ⭐⭐⭐⭐ (数据统计和对比表格详尽)
- **影响力**: ⭐⭐⭐⭐⭐ (为3D-VL领域提供重要的数据基础设施)

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] WaSt-3D: Wasserstein-2 Distance for Scene-to-Scene Stylization on 3D Gaussians](wast-3d_wasserstein-2_distance_for_scene-to-scene_stylization_on_3d_gaussians.md)
- [\[ECCV 2024\] Zero-Shot Multi-Object Scene Completion](zero-shot_multi-object_scene_completion.md)
- [\[ECCV 2024\] Vista3D: Unravel the 3D Darkside of a Single Image](vista3d_unravel_the_3d_darkside_of_a_single_image.md)
- [\[ECCV 2024\] Transferable 3D Adversarial Shape Completion using Diffusion Models](transferable_3d_adversarial_shape_completion_using_diffusion_models.md)
- [\[ECCV 2024\] TPA3D: Triplane Attention for Fast Text-to-3D Generation](tpa3d_triplane_attention_for_fast_text-to-3d_generation.md)

</div>

<!-- RELATED:END -->
