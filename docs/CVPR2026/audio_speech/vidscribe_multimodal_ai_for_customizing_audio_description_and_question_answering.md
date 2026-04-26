---
title: >-
  [论文解读] ViDscribe: Multimodal AI for Customizing Audio Description and Question Answering in Online Videos
description: >-
  [CVPR 2026][语音][音频描述] ViDscribe 是一个基于 Web 的平台，利用多模态大语言模型(Gemini 3 Pro)为盲人和低视力(BLV)用户提供可定制的 AI 生成音频描述(AD)和交互式视觉问答(VQA)功能，支持任意 YouTube 视频，通过为期一周的纵向用户研究验证了定制化 AD 在有效性、享受度和沉浸感方面均优于默认 AD。
tags:
  - CVPR 2026
  - 语音
  - 音频描述
  - 视频无障碍
  - 多模态大语言模型
  - 用户定制化
  - 视觉问答
---

# ViDscribe: Multimodal AI for Customizing Audio Description and Question Answering in Online Videos

**会议**: CVPR 2026  
**arXiv**: [2603.14662](https://arxiv.org/abs/2603.14662)  
**代码**: https://vidscribe.org/  
**领域**: 其他 / 无障碍AI  
**关键词**: 音频描述, 视频无障碍, 多模态大语言模型, 用户定制化, 视觉问答

## 一句话总结

ViDscribe 是一个基于 Web 的平台，利用多模态大语言模型(Gemini 3 Pro)为盲人和低视力(BLV)用户提供可定制的 AI 生成音频描述(AD)和交互式视觉问答(VQA)功能，支持任意 YouTube 视频，通过为期一周的纵向用户研究验证了定制化 AD 在有效性、享受度和沉浸感方面均优于默认 AD。

## 研究背景与动机

1. **领域现状**：音频描述是帮助 BLV 用户理解视频视觉内容的关键辅助技术。传统人工 AD 制作昂贵、耗时且需要专业知识，导致绝大多数在线视频缺乏描述。近年来 MLLM 的进步使自动 AD 生成成为可能。
2. **现有痛点**：现有 AI-AD 系统采用"一刀切"策略，不适应 BLV 用户的多样化需求和偏好；评估通常在受控的短期实验室环境中进行，缺乏纵向使用数据。
3. **核心矛盾**：BLV 用户的需求因视力程度、观看场景和内容类型而异，但现有系统无法动态调整描述策略。
4. **本文目标**：构建支持用户定制和交互式问答的 AI-AD 平台，并通过纵向研究验证其价值。
5. **切入角度**：提供六种定制选项（频率、长度、重点、主观性、颜色、自由文本）和实时 VQA 功能。
6. **核心 idea**：将 MLLM 的能力转化为可控参数，让 BLV 用户根据个人偏好调整 AD 生成策略。

## 方法详解

### 整体框架

ViDscribe 使用 React 前端 + AWS Lambda 后端，核心引擎为 Gemini 3 Pro MLLM。用户粘贴 YouTube URL，选择定制设置后系统自动生成同步 AD。AD 时机通过音频分析自动确定，描述内容由 MLLM 根据定制参数生成。界面兼容屏幕阅读器和键盘控制。

### 关键设计

1. **六维定制控制**:

    - 功能：满足 BLV 用户的多样化需求
    - 核心思路：(A) 频率——每 8/15/30 秒插入一次描述；(B) 长度——滑块控制 15-100 词/条；(C) 重点——通用/角色/环境/教学内容；(D) 主观性——客观事实描述 vs 主观解读；(E) 颜色——是否描述颜色属性；(F) 自由文本——用户自定义指令。所有设置转化为 prompt 参数条件化 AD 生成
    - 设计动机：先前研究和 BLV 社区反馈表明，不同用户在不同场景下需要不同类型的描述

2. **自适应 AD 生成**:

    - 功能：在合适的时间点生成符合用户偏好的描述
    - 核心思路：分两步——(a) AD 时机模块：提取音频，分析静音、无语音片段和场景变化三种信号，选择信号重叠的自然停顿点插入描述，递归分割过长间隔；(b) 描述生成模块：使用 Gemini 3 Pro，提供视频、时间戳、用户定制设置和 42 条 AD 指南，生成个性化描述
    - 设计动机：好的 AD 不仅要内容正确，还要在合适的时间点出现，不打断对话

3. **交互式 VQA**:

    - 功能：允许用户在播放过程中随时提问获取额外视觉信息
    - 核心思路：用户按快捷键暂停，通过打字或语音输入问题（如"谁刚进入房间？"），系统将问题、当前时间戳、视频 AD 和代表性帧发送给 Gemini 3 Pro 生成上下文感知回答，通过文本转语音播放
    - 设计动机：被动描述无法覆盖所有信息，VQA 让用户能主动获取缺失细节

### 损失函数 / 训练策略

无需训练，完全基于 Gemini 3 Pro 的零样本推理能力。

## 实验关键数据

### 主实验（纵向用户研究）

| 指标 (5分制) | 默认AD | 定制AD | 提升 |
|-------------|--------|--------|------|
| 有效性 | 4.00 | 4.32 | +0.32 |
| 享受度 | 3.45 | 3.97 | +0.52 |
| 沉浸感 | 3.72 | 4.06 | +0.34 |
| VQA 帮助程度 | - | 3.46 | - |
| SUS 可用性 | - | 70.6 | >68 基准 |

定制 AD 在所有维度上优于默认 AD，享受度提升最大。

### 消融实验（定制偏好分析）

| 定制类型 | 最常选择 | 占比 |
|---------|---------|------|
| 频率 | 8秒(频繁) | 54.9% |
| 长度 | 26-50词(中等) | 49.0% |
| 重点 | 通用内容 | 52.9% |
| 主观性 | 客观描述 | 72.5% |
| 颜色 | 包含颜色 | 80.4% |

### 关键发现

- 63% 的视频使用了定制设置，说明 BLV 用户确实需要且愿意使用定制功能
- 随时间推移，用户偏好向更短、更低频的描述转变，反映了使用熟练后的偏好演化
- VQA 共收到 66 个问题，最常见的是询问角色身份和场景细节
- 6/8 参与者表示会向 BLV 朋友推荐 ViDscribe
- VQA 评分略低(3.46)，部分因为当前实现仅使用当前帧及附近帧回答

## 亮点与洞察

- **纵向真实场景研究**：首次在为期一周的真实使用场景中评估 AI-AD 定制和 VQA，而非短期实验室实验
- **定制偏好的时间演化**：发现用户偏好随使用时间变化，这对自适应系统设计有指导意义
- **完整的可部署系统**：不仅是方法论贡献，还是一个可实际使用的无障碍工具

## 局限与展望

- 样本量小(8人)，未做统计显著性检验
- VQA 仅使用当前帧附近信息，无法回答需要全视频理解的问题
- 定制设置需要手动调整，未来可自动学习用户偏好
- 描述质量受 Gemini 3 Pro 的能力限制
- 未来可加入用户偏好记忆和跨会话学习

## 相关工作与启发

- **vs YouDescribe**: YouDescribe 依赖志愿者人工描述，无法扩展；ViDscribe 自动生成
- **vs NarrationBot**: NarrationBot 生成固定描述，无定制化
- **vs DescribePro**: DescribePro 辅助人工描述者，ViDscribe 完全自动化

## 评分

- 新颖性: ⭐⭐⭐ 系统集成为主，技术创新有限
- 实验充分度: ⭐⭐⭐ 纵向研究设计好但样本量小
- 写作质量: ⭐⭐⭐⭐ 用户研究描述详细
- 价值: ⭐⭐⭐⭐ 对无障碍社区有实际意义

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Tri-Subspaces Disentanglement for Multimodal Sentiment Analysis](tri-subspaces_disentanglement_for_multimodal_sentiment_analysis.md)
- [\[CVPR 2026\] UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark](unim_a_unified_any-to-any_interleaved_multimodal_benchmark.md)
- [\[CVPR 2026\] Team LEYA in 10th ABAW Competition: Multimodal Ambivalence/Hesitancy Recognition Approach](team_leya_in_10th_abaw_competition_multimodal_ambivalencehesitancy_recognition_a.md)
- [\[CVPR 2026\] Semantic Audio-Visual Navigation in Continuous Environments](semantic_audio-visual_navigation_in_continuous_environments.md)
- [\[CVPR 2026\] OmniSonic: Towards Universal and Holistic Audio Generation from Video and Text](omnisonic_towards_universal_and_holistic_audio_generation_from_video_and_text.md)

<!-- RELATED:END -->
