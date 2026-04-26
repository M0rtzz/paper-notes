---
title: >-
  [论文解读] Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task
description: >-
  [NeurIPS 2025][视频理解][视频问答] 本文提出 STAR 框架，通过构建包含 22 个工具的视频分析工具箱，让 LLM 交替调用时间和空间工具渐进式定位视频中的 3D 关注区域（3D RoI），在 VideoMME 上提升 8.2%、LongVideoBench 上提升 4.6%。
tags:
  - NeurIPS 2025
  - 视频理解
  - 视频问答
  - 工具增强
  - 时空推理
  - MLLM
  - 渐进式定位
---

# Tool-Augmented Spatiotemporal Reasoning for Streamlining Video Question Answering Task

**会议**: NeurIPS 2025  
**arXiv**: [2512.10359](https://arxiv.org/abs/2512.10359)  
**代码**: [GitHub](https://github.com/fansunqi/VideoTool)  
**领域**: 视频理解 / LLM Agent  
**关键词**: 视频问答, 工具增强, 时空推理, MLLM, 渐进式定位

## 一句话总结
本文提出 STAR 框架，通过构建包含 22 个工具的视频分析工具箱，让 LLM 交替调用时间和空间工具渐进式定位视频中的 3D 关注区域（3D RoI），在 VideoMME 上提升 8.2%、LongVideoBench 上提升 4.6%。

## 研究背景与动机
1. **领域现状**: VideoQA 的两种主流方案——Video-LLM 需处理大量帧导致低效；工具增强 LLM 存在工具单一、调度不足等问题。
2. **现有痛点**: 现有工具增强方法：(1) 工具仅覆盖单一维度（时间或空间），(2) 工具数量与多样性不平衡，(3) 缺乏有效调度策略导致工具链混乱。
3. **核心矛盾**: 需要同时建模帧内空间关系和跨帧时间动态，但现有方法做不到。
4. **本文目标**: 构建全面的视频工具箱并设计交替时空推理框架。
5. **切入角度**: 将视频关键区域定位视为 3D RoI 的渐进缩小过程。
6. **核心 idea**: 时空交错工具链——交替使用时间工具缩小时间范围和空间工具缩小空间范围。

## 方法详解

### 整体框架
视频工具箱（22 个工具：时间工具 + 空间工具 + 通用工具）→ STAR 框架（交替调用时空工具）→ LLM 最终推理回答。

### 关键设计
1. **视频工具箱（22 个工具）**:
    - 时间工具: 关键帧搜索（AKeyS）、时间定位（temporal grounding）、自适应帧采样、场景切割等
    - 空间工具: YOLO-World 目标检测、Grounding DINO 目标定位、Patch Zoomer 区域放大、图像裁剪、OCR 等
    - 通用工具: VQA、图像描述、视频摘要等
    - 设计原则: 时空分离、自然语言接口（如 bbox 转文本描述）、段/帧双粒度
2. **STAR 框架（时空推理）**:
    - 功能: LLM 自主交替调用时空工具实现渐进式 3D RoI 定位
    - 核心思路: 先用时间工具缩小时间范围→再用空间工具缩小空间范围→再缩小时间→...直到定位到回答问题所需的关键区域
    - 特性: 自主性（LLM 自主决策）、适应性（根据视频长度/内容调整）、渐进性（从少量帧开始逐步扩展）
3. **工具链策略对比**: 时空交错 > 时空分离 > 快捷方式。交错策略确保时空推理互相反馈。

### 损失函数 / 训练策略
- 无需训练，纯推理框架
- 增强 GPT-4o 作为核心推理引擎
- 工具基于 YOLO-World、Grounding DINO 等轻量模型
- 渐进式帧处理减少计算成本

## 实验关键数据

| 基准 | STAR + GPT-4o | GPT-4o (32帧) | Qwen-VL-7B | 提升 |
|------|-------------|-------------|-----------|------|
| VideoMME | +8.2% | baseline | 对比模型 | 超越 7B VLLM |
| LongVideoBench | +4.6% | baseline | - | 显著提升 |
| EgoSchema | 最优 | - | - | 帧效率最高 |

### 关键发现
- 时空交错工具链 > 时空分离工具链 > 工具链快捷方式
- 随帧数增加，STAR 精度持续提升且效率最高
- 空间工具（目标检测+放大）对细粒度空间问题帮助最大

### 工具箱分类详情

| 工具类型 | 数量 | 代表工具 |
|---------|------|--------|
| 时间工具 | 7 | AKeyS, 时间定位, 场景切割 |
| 空间工具 | 8 | YOLO-World, Grounding DINO, Patch Zoomer |
| 通用工具 | 7 | VQA, 图像描述, 视频摘要 |

### 工具链策略对比

| 策略 | VideoMME | LongVideoBench | 帧效率 |
|------|---------|---------------|-------|
| 时空交错 | **最优** | **最优** | **最高** |
| 时空分离 | -3.1% | -2.8% | 中等 |
| 快捷方式 | -5.4% | -4.9% | 最低 |


## 亮点与洞察
- 22 个工具的即插即用设计使系统高度可扩展
- 渐进式 3D RoI 定位是直觉清晰的视频理解范式
- 轻量工具增强 GPT-4o 超越专用 Video-LLM
- 工具链可视化展示了推理过程的可解释性

## 局限与展望
- 依赖 GPT-4o 作为推理引擎，成本较高，难以规模化部署。
- 工具调用增加总推理时间，每次工具调用引入额外延迟。
- 工具间的错误可能级联传播，早期错误可能导致整个推理链失败。
- 未与 RL 微调方法（如 TempSamp-R1）对比，无法判断与端到端方法的优劣。
- 22个工具的维护和更新成本较高，工具质量参差不齐。
- 对于需要音频理解的视频问答任务，当前工具箱缺少音频分析工具。
- 工具链的最大长度未控制，可能导致过长的推理链增加成本和错误率。
- 渐进式3D RoI定位在极短视频（<5秒）中可能过度处理，引入不必要的计算开销。

## 相关工作与启发
- **vs DoraemonGPT**: DoraemonGPT 用 SQL 查询工具输出数据库，常失败；STAR 更可靠
- **vs VideoAgent**: VideoAgent 主要用时间维度工具，STAR 同时覆盖时空
- **vs Video-LLM (Qwen-VL)**: STAR 用轻量工具增强 GPT-4o 超越专用模型


### 补充讨论
- 该方法的核心创新点在于将问题从一个维度转化到多个维度进行分析，提供了更全面的理解视角。
- 实验设计覆盖了多种场景和基线对比，结果在统计上显著。
- 方法的模块化设计使其易于扩展到相关任务和新的数据集。
- 代码/数据的开源对社区复现和后续研究有重要价值。
- 与同期工作相比，本文在问题定义的深度和实验分析的全面性上更具优势。
- 论文的写作逻辑清晰，从问题定义到方法设计到实验验证形成了完整的闭环。
- 方法的计算开销合理，在实际应用中具有可部署性。
- 未来工作可以考虑与更多模态（如音频、3D点云）的融合。
- 在更大规模的数据和模型上验证方法的可扩展性是重要的后续方向。

## 评分
- 新颖性: ⭐⭐⭐⭐ 时空交错工具链框架设计新颖
- 实验充分度: ⭐⭐⭐⭐ 多基准评估，工具链策略对比
- 写作质量: ⭐⭐⭐⭐ 图示清晰，工具分类合理
- 价值: ⭐⭐⭐⭐ 对视频分析助手和工具学习都有参考价值

<!-- RELATED:START -->

## 相关论文

- [\[NeurIPS 2025\] EgoGazeVQA: Egocentric Gaze-Guided Video Question Answering Benchmark](egogazevqa_egocentric_gaze_guided_video_question_answering.md)
- [\[NeurIPS 2025\] VGEnt: Graph-Based Retrieval-Reasoning-Augmented Generation for Long Video Understanding](vgent_graph-based_retrieval-reasoning-augmented_generation_for_long_video_unders.md)
- [\[NeurIPS 2025\] VideoLucy: Deep Memory Backtracking for Long Video Understanding](videolucy_deep_memory_backtracking_for_long_video_understanding.md)
- [\[NeurIPS 2025\] Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models](structured_sparse_transition_matrices_to_enable_state_tracking_in_state-space_mo.md)
- [\[NeurIPS 2025\] DSAS: A Universal Plug-and-Play Framework for Attention Optimization in Multi-Document Question Answering](dsas_a_universal_plug-and-play_framework_for_attention_optimization_in_multi-doc.md)

<!-- RELATED:END -->
