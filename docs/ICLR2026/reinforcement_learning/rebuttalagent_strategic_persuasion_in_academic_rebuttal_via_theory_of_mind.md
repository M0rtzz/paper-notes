---
description: "【论文笔记】RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind 论文解读 | ICLR 2026 | arXiv 2601.15715 | 学术rebuttal | 提出RebuttalAgent——首个将心智理论(ToM)融入学术rebuttal的框架：通过ToM-Strategy-Response三阶段(建模审稿人心理状态→制定说服策略→生成证据基础响应)，用RebuttalBench(7万+样本)做SFT+自奖励RL训练，开发Rebuttal-RM评估器(10万+样本,超越GPT-4.1的人类一致性)→平均超越基础模型18.3%,与SOTA闭源模型可比。"
tags:
  - ICLR 2026
---

# RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind

**会议**: ICLR 2026  
**arXiv**: [2601.15715](https://arxiv.org/abs/2601.15715)  
**代码**: [GitHub](https://github.com/Zhitao-He/RebuttalAgent)  
**领域**: LLM Agent/学术写作  
**关键词**: 学术rebuttal, 心智理论, 策略说服, 自奖励RL, 审稿人建模

## 一句话总结
提出RebuttalAgent——首个将心智理论(ToM)融入学术rebuttal的框架：通过ToM-Strategy-Response三阶段(建模审稿人心理状态→制定说服策略→生成证据基础响应)，用RebuttalBench(7万+样本)做SFT+自奖励RL训练，开发Rebuttal-RM评估器(10万+样本,超越GPT-4.1的人类一致性)→平均超越基础模型18.3%,与SOTA闭源模型可比。

## 研究背景与动机

1. **领域现状**：AI辅助研究workflow各阶段(文献综述→实验→论文)→但rebuttal阶段几乎未被探索。Rebuttal本质是信息不对称下的策略沟通(博弈论)。

2. **现有痛点**：
   - (1) 现有方法(SFT)→模仿表面语言模式→缺乏战略深度
   - (2) 不能进行视角转换→不理解审稿人的知识背景/偏见/核心关切
   - (3) 何时让步/何时坚持/何时提供新证据→需要策略推理

3. **切入角度**：ToM=建模他人心理状态→审稿人画像→指导策略→证据基础响应。

## 方法详解

### TSR三阶段框架

1. **T (Theory of Mind)**：宏观审稿人意图+微观评论属性→多维审稿人画像
2. **S (Strategy)**：基于画像→制定目标评论的行动计划(让步/反驳/重新架构)
3. **R (Response)**：基于策略+检索证据→生成有说服力的响应

### RebuttalBench数据集
- 7万+高质量样本→critique-and-refine pipeline→多个教师模型
- 每个样本含完整TSR链

### 训练：SFT + 自奖励RL
- SFT：教模型基础ToM+策略推理
- RL：自奖励机制→无需外部奖励模型→可扩展

### Rebuttal-RM评估器
- 基于Qwen3-8B → 10万+多源rebuttal数据训练
- 与人类偏好一致性 > GPT-4.1

## 实验关键数据

| 方法 | 自动指标提升 | 人类评估 |
|------|-----------|---------|
| 基础模型 | 基线 | 基线 |
| SFT-only | +10% | 中 |
| **RebuttalAgent** | **+18.3%** | **≈SOTA闭源** |

### 关键发现
- ToM阶段是关键→消融后性能显著下降→证明审稿人建模很重要
- 策略阶段→决定何时让步何时坚持→影响说服力
- 自奖励RL→比纯SFT更好→因为探索了更多说服策略
- Rebuttal-RM→比GPT-4.1更一致→验证了专门化评估器的价值

## 亮点与洞察
- **"Rebuttal=不完全信息博弈"**：不是技术辩论→而是策略沟通→ToM是自然框架。
- **"首个学术rebuttal AI"**：填补了研究workflow中的最后一块空白。
- **自奖励的可扩展性**：不需要人类标注奖励→模型自己评估自己→可持续改进。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ ToM+学术rebuttal的首次结合
- 实验充分度: ⭐⭐⭐⭐ 自动+人类评估+消融
- 写作质量: ⭐⭐⭐⭐⭐ 博弈论动机令人信服
- 价值: ⭐⭐⭐⭐ 对学术社区有直接实用价值
