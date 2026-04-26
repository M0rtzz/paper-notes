---
title: >-
  [论文解读] Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search
description: >-
  [CVPR 2026][LLM Agent][长视频理解] 提出 HAVEN 框架，通过音视频实体一致性和层次化视频索引（全局-场景-片段-实体四层），配合智能体搜索机制在 LVBench 上达到 84.1% 准确率，尤其在推理类别达 80.1%。
tags:
  - CVPR 2026
  - LLM Agent
  - 长视频理解
  - 音视频实体一致性
  - 层次化索引
  - 智能体搜索
  - 说话人识别
---

# Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search

**会议**: CVPR 2026  
**arXiv**: [2601.13719](https://arxiv.org/abs/2601.13719)  
**代码**: 无  
**领域**: 视频理解 / 长视频  
**关键词**: 长视频理解, 音视频实体一致性, 层次化索引, 智能体搜索, 说话人识别

## 一句话总结

提出 HAVEN 框架，通过音视频实体一致性和层次化视频索引（全局-场景-片段-实体四层），配合智能体搜索机制在 LVBench 上达到 84.1% 准确率，尤其在推理类别达 80.1%。

## 研究背景与动机

1. **领域现状**：长视频理解面临极长上下文窗口挑战。RAG 方法和智能体框架虽有进展，但存在信息碎片化和全局连贯性丧失问题。
2. **现有痛点**：现有检索驱动方法基于孤立信号（片段级字幕）检索，碎片化或冗余证据严重削弱全局叙事连贯性。缺乏层次化视频表征使智能体缺少多层推理所需的结构化上下文。
3. **核心矛盾**：简单数据库（帧、字幕、实体）需要大量迭代检索才能恢复跨片段连续性，引入不必要的复杂度和计算成本。
4. **本文目标**：从碎片化检索转向连贯的结构化理解。
5. **切入角度**：利用说话人识别作为实体一致性的强信号——说话人身份在视觉线索退化时（遮挡、视角变化等）仍保持信息量。
6. **核心 idea**：音视频实体一致性 + 四层层次化索引 + 目标驱动的智能体搜索。

## 方法详解

### 整体框架

离线构建四层数据库 $\mathcal{D} = \{\tilde{\mathcal{C}}, \tilde{\mathcal{E}}, \tilde{\mathcal{S}}, \tilde{\mathcal{G}}\}$（片段、实体、场景、全局），在线时智能体通过 think-act-observe 循环在层次间导航检索和推理。

### 关键设计

1. **音视频实体一致性**:

    - 功能：维护跨时间和跨模态的实体语义一致性
    - 核心思路：用 WhisperX 进行 ASR 和说话人分割，获得时间戳化的转录和一致的说话人标签。实体提取后进行两阶段合并：(1) 嵌入聚类形成候选组；(2) LLM 审核每个聚类进行规范化或拆分。当多个片段共享同一说话人标签时，优先合并对应的角色实体。
    - 设计动机：说话人身份在视觉线索退化（遮挡、镜头切换、外观变化）时仍然可靠，可作为跨片段实体关联的"粘合剂"。

2. **四层层次化数据库**:

    - 功能：支持多粒度的灵活检索
    - 核心思路：(1) 片段层：30秒固定窗口，包含文本描述和视觉嵌入；(2) 实体层：规范化实体及其关联片段的重新描述；(3) 场景层：LLM 自适应聚合语义相关片段为场景摘要；(4) 全局层：从场景集生成全局摘要。
    - 设计动机：不同查询类型需要不同粒度的信息——"视频讲什么"需要全局，"12:00发生了什么"需要片段级。

3. **多粒度工具集的智能体搜索**:

    - 功能：查询驱动的自适应多层检索和推理
    - 核心思路：五个工具：全局场景浏览 $T_{scene}$、片段字幕搜索 $T_{caption}$、片段视觉搜索 $T_{visual}$、实体搜索 $T_{entity}$、检查工具 $T_{inspect}$（含文本和视觉两种模式）。智能体初始化为全局摘要，多轮迭代中动态选择工具。
    - 设计动机：低成本文本检索优先，高成本视觉检查仅在需要时使用。

### 损失函数 / 训练策略

纯推理框架，无训练。数据库离线构建，推理时智能体在线搜索。

## 实验关键数据

### 主实验

| 方法 | LVBench 总体 | 推理类别 |
|------|-------------|---------|
| HAVEN (2fps) | 84.1 | 80.1 |
| DVD w/ subtitle | 76.0 | 68.7 |
| Seed1.5-VL-200B | 64.6 | 63.7 |
| OpenAI o3 | 57.1 | 50.8 |

### 消融实验

| 配置 | LVBench 总体 | 说明 |
|------|-------------|------|
| 完整 HAVEN | 84.1 | 最优 |
| 无音频实体一致性 | 下降 | 实体碎片化 |
| 无层次化索引 | 下降 | 检索效率低 |

### 关键发现

- 在最具挑战性的推理类别上 80.1%，大幅超越 DVD（68.7%）
- 说话人身份是关键——Figure 3 展示外观剧变的角色通过说话人标签正确关联
- 2fps 帧率下性能从 81.0 提升到 84.1，更密集采样提供更多视觉证据

## 亮点与洞察

- **说话人身份作为跨模态粘合剂**：优雅地利用了音频信号中被忽视的说话人一致性
- **离线-在线解耦**：层次化数据库离线构建，推理时仅需轻量工具调用
- **实用性强**：对话密集内容（纪录片、剧集、vlog）特别有效

## 局限与展望

- 依赖 ASR 和说话人分割的准确性，在嘈杂音频环境下可能退化
- 30秒固定片段划分可能不适合所有视频类型
- 缓存内容有限，更多实验细节待查阅完整论文
- 数据库构建的计算成本和存储开销未详细分析

## 相关工作与启发

- **vs DVD**: DVD 用简单数据库需大量迭代，HAVEN 用层次化数据库减少迭代次数
- **vs VideoRAG**: VideoRAG 依赖图语义检索但缺乏层次结构

## 评分

- 新颖性: ⭐⭐⭐⭐ 音视频实体一致性和说话人身份利用是新颖贡献，层次化索引设计系统
- 实验充分度: ⭐⭐⭐ 缓存有限，LVBench 结果突出但其他基准结果不完整
- 写作质量: ⭐⭐⭐⭐ 框架图清晰，案例分析直观，方法描述有条理
- 价值: ⭐⭐⭐⭐ 长视频理解的实用框架，说话人身份利用思路可迁移到其他多模态场景

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] HAVEN: Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search](haven_hierarchical_long_video_understanding_with_audiovisual_entity_cohesion.md)
- [\[CVPR 2026\] Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding](think_then_verify_a_hypothesis-verification_multi-agent_framework_for_long_video.md)
- [\[CVPR 2026\] WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](worldmm_dynamic_multimodal_memory_agent_for_long_video_reasoning.md)
- [\[CVPR 2026\] ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search](argos_agentic_multi_camera_person_search.md)
- [\[CVPR 2026\] GUI-CEval: A Hierarchical and Comprehensive Chinese Benchmark for Mobile GUI Agents](gui-ceval_a_hierarchical_and_comprehensive_chinese_benchmark_for_mobile_gui_agen.md)

<!-- RELATED:END -->
