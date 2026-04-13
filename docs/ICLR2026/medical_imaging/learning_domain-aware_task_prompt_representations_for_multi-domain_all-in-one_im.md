---
title: >-
  [论文解读] Learning Domain-Aware Task Prompt Representations for Multi-Domain All-in-One Image Restoration
description: >-
  [ICLR 2026][医学图像][多域图像复原] 提出DATPRL-IR——首个多域全能图像复原方法：通过双提示池设计(任务提示池编码跨任务知识+域提示池从MLLM蒸馏域先验)和提示组合机制(PCM)为每个输入图像动态组合实例级域感知任务提示表示，一个模型统一处理自然场景/医学影像/遥感三域的多种退化任务，显著超越单域SOTA。
tags:
  - ICLR 2026
  - 医学图像
  - 多域图像复原
  - 双提示池
  - 域感知
  - MLLM蒸馏
  - 自适应门控融合
---

# Learning Domain-Aware Task Prompt Representations for Multi-Domain All-in-One Image Restoration

**会议**: ICLR 2026  
**arXiv**: [2603.01725](https://arxiv.org/abs/2603.01725)  
**代码**: [GitHub](https://github.com/GuangluDong0728/DATPRL-IR)  
**领域**: 图像复原/多域统一  
**关键词**: 多域图像复原, 双提示池, 域感知, MLLM蒸馏, 自适应门控融合

## 一句话总结
提出DATPRL-IR——首个多域全能图像复原方法：通过双提示池设计(任务提示池编码跨任务知识+域提示池从MLLM蒸馏域先验)和提示组合机制(PCM)为每个输入图像动态组合实例级域感知任务提示表示，一个模型统一处理自然场景/医学影像/遥感三域的多种退化任务，显著超越单域SOTA。

## 研究背景与动机

**领域现状**：全能图像复原(AiOIR)用单模型处理多种退化(去噪/超分/去雨)。现有方法仅关注单一图像域(自然/医学/遥感)。

**现有痛点**：
   - (1) 单域AiOIR扩展到多域→学习难度剧增
   - (2) 现有方法关注区分不同任务→忽略任务间共性
   - (3) 不考虑不同域之间的差异和联系
   - (4) 各域分别训练→资源浪费

**切入角度**：利用跨任务和跨域的共享知识降低学习难度→双prompt pool设计。

## 方法详解

### 双提示池架构

1. **任务提示池(TP Pool)**：
   - N_t个key-value对→隐式编码任务相关知识
   - 编码器中间特征→投影为query→检索top-k最相关task prompt
   - PCM组合：softmax加权聚合→实例级任务表示PR_t
   - 联合训练→学习任务特有知识同时允许跨任务共享

2. **域提示池(DP Pool)**：
   - N_d个key-value对→存储域相关知识
   - 浅层特征→投影为domain query→检索top-k
   - **MLLM域先验蒸馏**：LLaVA生成多角度描述(内容/颜色/亮度/相机)→CLIP编码→对齐损失训练domain prompts
   - PCM组合→域表示PR_d

3. **域感知任务表示**：
   - PR_t + PR_d → cross-attention → PR_dt
   - 自适应门控融合(AGF)：每层学习α_l控制backbone特征vs prompt贡献比

### 提示池正则化
- 多样性正则：prompt间余弦相似度不超过阈值
- 熵正则：鼓励均衡使用所有prompt（避免少数prompt被过度选择）

### 训练与推理
- 训练：LLaVA+CLIP提供域先验
- 推理：不需要LLaVA/CLIP→零额外推理开销

## 实验关键数据

### 多域全能复原(自然+医学+遥感)
| 方法 | 自然域 | 医学域 | 遥感域 | 说明 |
|------|-------|-------|-------|------|
| PromptIR(单域) | 好 | 差(不适配) | 差 | 仅自然域训练 |
| 多域PromptIR | 中 | 中 | 中 | 无域感知 |
| **DATPRL-IR** | **最好** | **最好** | **最好** | 域感知 |

### 关键发现
- 域提示池的贡献→跨域性能提升2-3dB PSNR
- MLLM蒸馏 vs 无蒸馏→域感知更准确→特别在域混淆任务上
- PCM vs 直接拼接→PCM更灵活→每个样本有不同的prompt权重
- AGF的层级自适应→浅层更多backbone信息、深层更多prompt引导

## 亮点与洞察
- **"首个多域AiOIR"**：从单域到多域是重要的范式扩展→一个模型替代三个。
- **MLLM作为域知识源**：不用MLLM做复原→而是蒸馏其域理解能力到compact prompts→零推理开销。
- **双提示池的正交设计**：任务知识和域知识分开存储/分开检索→然后交叉融合→比单一prompt pool更精细。
- **"灰度+人体器官=医学, 鸟瞰+建筑=遥感"**：组合域特征→类似人类的域识别方式。

## 评分
- 新颖性: ⭐⭐⭐⭐ 首个MD-AiOIR+双提示池+MLLM蒸馏
- 实验充分度: ⭐⭐⭐⭐⭐ 三域×多任务×多SOTA对比+消融
- 写作质量: ⭐⭐⭐⭐ 动机清晰框架完整
- 价值: ⭐⭐⭐⭐ 对统一图像复原有实际推动
