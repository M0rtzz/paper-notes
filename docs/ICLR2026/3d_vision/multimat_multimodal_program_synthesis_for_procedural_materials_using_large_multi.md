---
title: >-
  [论文解读] MultiMat: Multimodal Program Synthesis for Procedural Materials using Large Multimodal Models
description: >-
  [ICLR 2026][3D视觉][程序化材质] 提出MultiMat——首个利用大型多模态模型(LMM)进行程序化材质合成的框架,在生成过程中同时处理文本程序表示和中间节点的视觉渲染结果,配合约束树搜索推理算法确保生成图的静态正确性,在产级程序化材质上的无条件和条件合成均显著优于纯文本基线。
tags:
  - ICLR 2026
  - 3D视觉
  - 程序化材质
  - 节点图
  - 多模态生成
  - 约束树搜索
  - Substance Designer
---

# MultiMat: Multimodal Program Synthesis for Procedural Materials using Large Multimodal Models

**会议**: ICLR 2026  
**arXiv**: [2509.22151](https://arxiv.org/abs/2509.22151)  
**代码**: 无  
**领域**: 3D视觉/程序合成  
**关键词**: 程序化材质, 节点图, 多模态生成, 约束树搜索, Substance Designer

## 一句话总结

提出MultiMat——首个利用大型多模态模型(LMM)进行程序化材质合成的框架,在生成过程中同时处理文本程序表示和中间节点的视觉渲染结果,配合约束树搜索推理算法确保生成图的静态正确性,在产级程序化材质上的无条件和条件合成均显著优于纯文本基线。

## 研究背景与动机

1. **领域现状**：程序化材质(如Substance Designer)用节点图定义PBR材质→参数化/分辨率无关/可编辑。创建节点图需要专业训练→对新手门槛高。神经程序合成(MatFormer, VLMaterial)尝试自动化。

2. **现有痛点**：
   - (1) 现有方法将节点图纯作为文本程序生成→忽略了节点图本质上是视觉-空间的
   - (2) 无视觉反馈→模型需纯靠文本推理复杂空间关系和视觉效果→随复杂度增长越来越难
   - (3) 生成的程序可能有结构错误(无效连接/类型不匹配)

3. **切入角度**：模拟人类艺术家工作流→在生成过程中提供中间节点的视觉渲染→多模态(视觉+文本)反馈循环。

## 方法详解

### 多模态程序合成

1. **视觉-文本表示**：
   - 每个生成步骤→当前节点图的中间状态被渲染为图像
   - 图像+文本程序前缀→一起送入LMM
   - LMM看到"当前材质看起来像什么"→决定下一步生成什么

2. **训练数据**：
   - 新收集的产级程序化材质数据集
   - 每个材质→序列化为节点添加序列+每步中间渲染

3. **约束树搜索推理**：
   - 保证静态正确性(有效连接/类型匹配/DAG结构)
   - 高效导航程序空间→避免无效生成

### 多模态反馈的优势

- 无条件生成：LMM"看到"中间结果→更好的材质质量和多样性
- 条件生成(逆渲染)：给定目标图像→LMM生成匹配的节点图
- 实时验证：每步检查生成的节点是否有意义

## 实验关键数据

| 方法 | 视觉质量(FID↓) | 保真度(LPIPS↓) | 结构有效率 |
|------|---------------|---------------|----------|
| MatFormer | 基线 | 基线 | ~85% |
| VLMaterial | 较好 | 较好 | ~90% |
| **MultiMat** | **最好** | **最好** | **~99%** |

### 任务对比

| 任务 | MultiMat vs 纯文本 |
|------|-------------------|
| 无条件生成 | 更多样+质量更高 |
| 条件合成(逆渲染) | 更高保真度 |
| 参数化控制 | 保持完整参数化能力 |

### 关键发现

- 视觉反馈在复杂材质(>10节点)上优势最大→简单材质差异小
- 约束树搜索将结构有效率从~90%提升到~99%
- LMM利用中间渲染的证据：注意力在中间图像上有明确pattern

## 亮点与洞察

- **"模拟人类工作流"**：人类艺术家通过视觉界面创建节点图→MultiMat首次让AI也"看着做"→比纯文本推理更自然。
- **中间状态可视化的信息量**：中间渲染不是noise→而是关键的推理线索→告诉模型"到目前为止材质像什么→接下来需要什么"。
- **约束搜索=程序验证**：不是后验检查而是生成时约束→保证每步都合法→避免了大量无效尝试。
- **与Agent范式的关系**：MultiMat可看作一个在材质设计环境中的Agent→有观察(渲染)/行动(添加节点)/反馈(视觉验证)循环。


## 局限性 / 可改进方向

- We present MultiMat, a multimodal program synthesis framework and model
suite that generates procedural materials by incorporating visual feedback
throughout the generation process.

- Our key insight is that procedural material
graphs are inherently visual-spatial programs, and treating them as such leads
to substantial improvements over text-only approaches.

- By conditioning on
visual intermediate states—either interleaved with text (mixed conditioning)
or as complete graph visualizations (graph conditioning)—our models achieve
consistent improvements over text-only baselines.

- Our incremental tree search
algorithm further enhances generation efficiency by validating nodes as they
are created and backtracking upon errors.

- While we demonstrate MultiMat specifically for procedural material synthesis, we hope its general principles
will inspire further research at the intersection of computer graphics, program
synthesis, and multimodal AI.


## 相关工作与启发

- **vs JavaScript**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 多模态程序合成用于材质生成的首次尝试
- 实验充分度: ⭐⭐⭐⭐ 无条件+条件+消融+与SOTA对比
- 写作质量: ⭐⭐⭐⭐ 图示清晰直观
- 价值: ⭐⭐⭐⭐ 对3D内容创建的自动化有实际推动
