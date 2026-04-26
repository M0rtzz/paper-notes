---
title: >-
  [论文解读] HumanVBench: Probing Human-Centric Video Understanding in MLLMs with Automatically Synthesized Benchmarks
description: >-
  [CVPR 2026][视频理解][以人为中心的视频理解] 提出 HumanVBench，一个包含 16 个细粒度任务的视频基准，通过两个自动化管道（视频标注+干扰项生成）系统评估 MLLM 的以人为中心视频理解能力，揭示了当前模型在情感感知和语音-视觉对齐方面的显著不足。
tags:
  - CVPR 2026
  - 视频理解
  - 以人为中心的视频理解
  - 多模态大模型评测
  - 自动基准构建
  - 情感感知
  - 语音视觉对齐
---

# HumanVBench: Probing Human-Centric Video Understanding in MLLMs with Automatically Synthesized Benchmarks

**会议**: CVPR 2026  
**arXiv**: [2412.17574](https://arxiv.org/abs/2412.17574)  
**代码**: [https://github.com/datajuicer/data-juicer/tree/HumanVBench](https://github.com/datajuicer/data-juicer/tree/HumanVBench)  
**领域**: 视频理解 / 多模态评测  
**关键词**: 以人为中心的视频理解, 多模态大模型评测, 自动基准构建, 情感感知, 语音视觉对齐

## 一句话总结

提出 HumanVBench，一个包含 16 个细粒度任务的视频基准，通过两个自动化管道（视频标注+干扰项生成）系统评估 MLLM 的以人为中心视频理解能力，揭示了当前模型在情感感知和语音-视觉对齐方面的显著不足。

## 研究背景与动机

1. **领域现状**：视频 MLLM 快速发展，但现有基准主要评估通用内容理解，缺乏对情感、行为、跨模态对齐等以人为中心能力的细粒度评估。
2. **现有痛点**：情感基准仅做离散分类，动作基准忽略情感状态和说话人识别；语音-视觉同步几乎未被系统评估。
3. **核心矛盾**：人类轻易检测音视频不匹配，但模型在说话人识别和唇音对齐上严重不足。
4. **本文目标**：构建系统评估 MLLM 以人为中心基础感知能力的基准。
5. **切入角度**：两个自动化管道大幅减少人工标注，同时利用模型错误生成高质量干扰项。
6. **核心 idea**：将模型诱导的错误转化为语义合理的干扰项，既保证题目难度又减少人工投入。

## 方法详解

### 整体框架

两条核心管道：(1) 以人为中心的视频标注管道：利用 20+ SOTA 算子产生密集多模态标注；(2) 含干扰项的 QA 合成管道：生成高质量选择题并利用多模型集成的错误答案作为干扰项。最终基准包含 2475 道题覆盖 16 个任务。

### 关键设计

1. **以人为中心的视频标注管道**:

    - 功能：从原始视频自动生成密集、细粒度的以人为中心标注
    - 核心思路：首先进行人物追踪（video_human_tracks_extraction）得到可靠的人物轨迹和计数。然后从轨迹中提取人口统计信息、外观描述、面部表情描述。音频方面进行活跃说话人检测、ASR 转录、语音情感识别和声学特征分析。
    - 设计动机：通过集成多个任务特定算子实现自动化，避免大规模人工标注。

2. **含干扰项的 QA 合成管道**:

    - 功能：生成语义合理且具有区分性的选择题
    - 核心思路：多个 MLLM（Gemini、VideoLLaMA3、ShareGPT4Video）分别生成候选答案，通过偏好投票排序。最高票作为正确答案，其他错误答案因反映典型模型错误而被保留为干扰项。若语义不足则 LLM 引入任务特定扰动。
    - 设计动机：保留模型常犯错误作为干扰项既保证合理性又增加难度。约 72% 题目无需人工修正。

3. **16 个细粒度任务设计**:

    - 功能：全面评估以人为中心的视频理解能力
    - 核心思路：分为内在情感（情感识别、情感时序分析、态度识别、情感强度对比）和外在表现（人物识别4任务、行为分析4任务、语音-视觉对齐4任务），共 16 个任务。
    - 设计动机：覆盖从基础感知到高级推理的完整评估层级。

### 损失函数 / 训练策略

基准构建，无训练。通过答案泄露检测（无视觉输入测试）移除约 6% 频繁正确的题目。

## 实验关键数据

### 主实验

| 模型 | 情感 | 人物识别 | 行为 | 语音-视觉 | 总体 |
|------|------|---------|------|----------|------|
| Gemini-2.5-Pro | 52.9 | 83.5 | 70.7 | 86.5 | 73.4 |
| Qwen-VL3 (7B) | 43.2 | 67.6 | 54.3 | 48.3 | 53.4 |
| GPT-5 | 46.8 | 69.5 | 67.3 | - | - |
| 人类 (研究生) | 84.6 | 88.5 | 87.0 | 94.4 | 88.6 |

### 消融实验

| 配置 | 关键指标 | 说明 |
|------|---------|------|
| ER 无需编辑率 | 81% | 效率增益 5.3× |
| ETA 无需编辑率 | 83% | 效率增益 5.9× |
| 平均无需编辑率 | 72.3% | 平均效率增益 3.6× |

### 关键发现

- 情感感知是所有模型的共同短板，即使 Gemini-2.5-Pro 也仅 52.9%，远低于人类 84.6%
- 说话人采样帧中"张嘴"动作被模型频繁误判为"惊讶"情绪
- 语音-视觉对齐：开源 audio-visual 模型大多表现接近随机，唯有 Gemini 系列表现突出
- Qwen2.5-Omni 在 SCM（语音内容匹配）上达 71.8%，在纯音频任务上有独特优势

## 亮点与洞察

- **模型驱动的基准构建**：将人类角色从手动创建转变为高效验证，效率提升 3.6×
- **管道的可泛化性**：通过替换检测器即可适配非人类领域（宠物属性识别、车辆追踪等）
- **揭示关键差距**：量化了情感感知和唇音对齐两个被忽视领域的模型-人类差距

## 局限与展望

- 视频来源有限（主要来自 Pexels 和 MF2 电影），场景多样性可进一步扩展
- 音频标注模型的系统性偏差可能影响部分题目质量
- 16 个任务聚焦基础感知层，未涵盖更高级的社交智能推理

## 相关工作与启发

- **vs Video-MME**: Video-MME 涵盖通用视频理解但仅 1% 题目涉及情感，HumanVBench 100% 以人为中心
- **vs Social-IQ**: Social-IQ 混合感知和高级推理，HumanVBench 聚焦基础感知层以提供更纯粹的诊断

## 评分

- 新颖性: ⭐⭐⭐⭐ 自动化管道设计和干扰项生成策略新颖
- 实验充分度: ⭐⭐⭐⭐⭐ 30 个模型全面评测，分析深入
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图表丰富
- 价值: ⭐⭐⭐⭐⭐ 填补了以人为中心视频理解评测的空白

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] SlotVTG: Object-Centric Adapter for Generalizable Video Temporal Grounding](slotvtg_object-centric_adapter_for_generalizable_video_temporal_grounding.md)
- [\[CVPR 2026\] Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning](learning_to_assist_physics-grounded_human-human_control_via_multi-agent_reinforc.md)
- [\[CVPR 2026\] Reconstruction-Guided Slot Curriculum: Addressing Object Over-Fragmentation in Video Object-Centric Learning](reconstruction-guided_slot_curriculum_addressing_object_over-fragmentation_in_vi.md)
- [\[CVPR 2026\] VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning](videochatm1_collaborative_policy_planning_for_vide.md)
- [\[CVPR 2026\] StreamingTOM: Streaming Token Compression for Efficient Video Understanding](streamingtom_streaming_token_compression_video.md)

<!-- RELATED:END -->
