---
title: >-
  [论文解读] Elysium: Exploring Object-Level Perception in Videos via MLLM
description: >-
  [ECCV 2024][多模态VLM][MLLM] 提出Elysium，首个端到端可训练的多模态大语言模型系统化处理视频目标级任务（如目标跟踪），构建了百万级ElysiumTrack-1M视频数据集支持SOT/RSOT/Video-REG三类任务，并设计T-Selector token压缩网络在保持性能的同时大幅减少视觉token消耗。
tags:
  - ECCV 2024
  - 多模态VLM
  - MLLM
  - 视频目标跟踪
  - 目标级感知
  - Token压缩
  - 大规模视频数据集
---

# Elysium: Exploring Object-Level Perception in Videos via MLLM

**会议**: ECCV 2024  
**arXiv**: [2403.16558](https://arxiv.org/abs/2403.16558)  
**代码**: [https://github.com/Hon-Wong/Elysium](https://github.com/Hon-Wong/Elysium)  
**领域**: 多模态VLM  
**关键词**: MLLM, 视频目标跟踪, 目标级感知, Token压缩, 大规模视频数据集

## 一句话总结
提出Elysium，首个端到端可训练的多模态大语言模型系统化处理视频目标级任务（如目标跟踪），构建了百万级ElysiumTrack-1M视频数据集支持SOT/RSOT/Video-REG三类任务，并设计T-Selector token压缩网络在保持性能的同时大幅减少视觉token消耗。

## 研究背景与动机
1. **领域现状**：MLLM在静态图像的目标级任务（目标检测、图像grounding）上已展现出色能力，但在视频目标级任务（如目标跟踪）上研究严重不足。
2. **两大核心挑战**：
    - **挑战一：训练数据稀缺**：现有跟踪数据集规模太小（如LaSOT仅1.4K轨迹），无法支撑MLLM所需的大规模预训练
    - **挑战二：计算负担**：处理多帧视频中的大量视觉token会爆满LLM的上下文窗口
3. **视频任务粒度分类**：
    - 视频级：VideoQA、Video Caption（融合所有帧的全局信息）
    - 帧级：Video Grounding、Dense Captioning（区分每帧）
    - **目标级**：SOT、MOT、VOS（需要跨帧定位和追踪特定物体）——粒度最细、最具挑战
4. **核心idea**：构建百万级数据集 + 设计token压缩网络 → 让MLLM具备视频目标级感知能力

## 方法详解

### 整体框架
Elysium = CLIP-ViT-L（视觉编码器）+ T-Selector（token压缩器）+ Vicuna（LLM）。每帧图像经CLIP编码后，T-Selector压缩视觉token数量（按α比例保留最重要的），压缩后token附带时间戳送入LLM。任务以指令格式表达，输出以文本形式给出坐标。

### 关键设计

1. **ElysiumTrack-1M数据集构建**：
    - 来源：WebVid-10M视频数据集
    - 构建流程两步走：
     - Step 1：用spaCy解析视频caption为名词短语→Grounding DINO在首帧/中帧/末帧定位→保留置信度>0.6的pairs
     - Step 2：用MixFormer从首帧bbox开始跟踪→保留全帧置信度>0.8的轨迹→Kalman Filter过滤异常漂移→IoU验证（中帧和末帧IoU>0.3）
    - 最终规模：127万条名词-轨迹对，每条含物体描述
    - 比现有最大跟踪数据集TrackingNet（3万轨迹）大40倍+

2. **RSOT和Video-REG新任务定义**：
    - **RSOT（Referring Single Object Tracking）**：仅通过语言描述定位和跟踪视频中的特定物体（不用初始bbox）
    - **Video-REG（Video Referring Expression Generation）**：给定物体坐标，生成描述该物体的自然语言（需跨帧时间感知——当前帧物体可能被遮挡但其他帧可识别）

3. **T-Selector token压缩网络**：
    - 动机：视频包含大量冗余信息，需要压缩视觉token以处理更多帧
    - 核心思路：Gating MLP + Softmax → KeepTopK选择分数最高的k=αN个token → MLP变换到LLM维度
    - 与传统cross-attention或concatenation融合不同，T-Selector在空间维度做选择性保留而非融合
    - 关键：空间维度融合会导致性能急剧下降，而选择性保留可以很好地平衡token数量和性能
    - 压缩比α可调（0到1之间）

4. **输入输出格式设计**：
    - 每帧视觉token附带时间戳（区分帧）
    - 坐标表示：[x1,y1,x2,y2]范围[0,100)，用逗号分隔无空格
    - 比Shikra的浮点坐标格式（28 tokens/坐标）节省一半token（13 tokens/坐标）

### 损失函数 / 训练策略
- **两阶段训练**：
    - Stage 1 预训练：仅图像数据训练，先冻结ViT+LLM仅训练T-Selector（LLaVA-558K），再全参数端到端训练（混合图像数据，32 GPU，30K步）
    - Stage 2 微调：高质量图像数据+视频数据（VideoChat+ElysiumTrack-1M），32 GPU，22K步
    - 视频训练：随机采样2~8帧（间隔1~60），最后2K步扩展到32帧
- **推理策略**：
    - 视频>32帧时分clip处理，每clip 8帧，前后clip重叠1帧以传递跟踪状态
    - 这模拟了传统SOT中的模板更新策略

## 实验关键数据

### 主实验

| 任务 | 模型 | 分辨率 | Token数/图 | 关键指标 |
|------|------|--------|-----------|---------|
| RefCOCO val | Shikra-7B | 224 | 256 | 87.01 |
| RefCOCO val | Shikra-13B | 224 | 256 | 87.83 |
| RefCOCO val | MiniGPT-v2* | 448 | 256 | 88.69 |
| RefCOCO val | **Elysium** | 336 | 可调 | 竞争性 |

| 任务 | 数据集 | 指标 |
|------|--------|------|
| SOT | ElysiumTrack-1M | Success/Precision |
| RSOT | ElysiumTrack-1M | Success/Precision |
| Video-REG | ElysiumTrack-1M | Meteor/CIDEr |

### 消融实验

| 组件 | 影响 |
|------|------|
| T-Selector vs Cross-Attention | T-Selector显著更优 |
| T-Selector vs Concatenation | T-Selector更优 |
| 压缩比α（0.25/0.5/0.75/1.0） | α=0.5~0.75为最佳平衡点 |
| 有/无时间戳 | 时间戳对帧区分至关重要 |
| 帧数2~8 vs 32 | 更多帧提升跟踪上下文 |
| 坐标格式（紧凑vs Shikra式） | 紧凑格式节省~50% token |

### 关键发现
1. ElysiumTrack-1M的127万轨迹是现有最大跟踪数据集的40倍+，证明了从网络视频自动构建大规模跟踪数据的可行性
2. T-Selector的选择性保留优于空间融合——说明token选择比token混合更适合保留帧内空间信息
3. 端到端MLLM处理目标跟踪是可行的——无需外部专家模型或手工参数调整
4. RSOT任务（纯语言驱动跟踪）开辟了跟踪与语言交互的新方向
5. 紧凑坐标格式大幅节省token，对多帧视频处理至关重要

## 亮点与洞察
1. **开拓性工作**：首次系统性地将MLLM能力扩展到视频目标级任务
2. **大规模数据集**：ElysiumTrack-1M的构建流水线（spaCy+GroundingDINO+MixFormer+过滤）可复用
3. **T-Selector设计哲学**："选择"优于"融合"——视频中不是所有空间位置都同等重要
4. **新任务定义**：RSOT和Video-REG填补了跟踪与语言交叉领域的空白
5. **实用的token效率**：紧凑坐标+T-Selector使多帧视频处理成为可能

## 局限性 / 可改进方向
1. 仅实现了单目标跟踪（SOT/RSOT），多目标跟踪（MOT）和视频分割（VOS/RVOS）留作future work
2. ElysiumTrack-1M基于MixFormer跟踪器生成→继承了其跟踪偏差和错误
3. 分clip推理时误差可能累积
4. 图像分辨率仅336×336，高分辨率下效果待验证
5. 与专业跟踪器（如MixFormer本身）相比，MLLM的跟踪精度仍有差距

## 相关工作与启发
- **Shikra/MiniGPT-v2**：图像目标级MLLM先驱，Elysium扩展到视频
- **VideoChat**：视频级MLLM，但不做目标级任务
- **MixFormer**：高性能跟踪器，用于ElysiumTrack-1M数据构建
- **启发**：MLLM的统一框架是否能在一个模型中同时处理视频理解+目标跟踪+生成任务？

## 评分
- 新颖性：⭐⭐⭐⭐⭐ （首创视频目标级MLLM + 两个新任务）
- 技术深度：⭐⭐⭐⭐ （数据集构建+T-Selector+训练策略完整）
- 实验充分性：⭐⭐⭐⭐ （多任务评估、详细消融）
- 实用价值：⭐⭐⭐⭐ （数据集和代码开源，社区价值大）
- 写作质量：⭐⭐⭐⭐ （结构清晰，任务定义明确）

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] LEGO: Learning EGOcentric Action Frame Generation via Visual Instruction Tuning](lego_learning_egocentric_action_frame_generation_via_visual_instruction_tuning.md)
- [\[ECCV 2024\] MotionChain: Conversational Motion Controllers via Multimodal Prompts](motionchain_conversational_motion_controllers_via_multimodal_prompts.md)
- [\[ECCV 2024\] MarvelOVD: Marrying Object Recognition and Vision-Language Models for Robust Open-Vocabulary Object Detection](marvelovd_marrying_object_recognition_and_visionlanguage_mod.md)
- [\[ECCV 2024\] Zero-shot Object Counting with Good Exemplars (VA-Count)](zero-shot_object_counting_with_good_exemplars.md)
- [\[ECCV 2024\] FreeMotion: MoCap-Free Human Motion Synthesis with Multimodal Large Language Models](freemotion_mocapfree_human_motion_synthesis_with_multimodal_.md)

</div>

<!-- RELATED:END -->
