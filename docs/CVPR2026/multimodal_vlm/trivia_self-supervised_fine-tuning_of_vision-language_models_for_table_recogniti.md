---
description: "【论文笔记】TRivia: Self-supervised Fine-tuning of Vision-Language Models for Table Recognition 论文解读 | CVPR2026 | arXiv 2512.01248 | 表格识别 | 提出TRivia，一种基于GRPO的自监督微调框架，使VLM能开源、从无标注表格图像中学习表格识别，产出的TRivia-3B超越Gemini 2.5 Pro和MinerU2.5。"
tags:
  - CVPR2026
---

# TRivia: Self-supervised Fine-tuning of Vision-Language Models for Table Recognition

**会议**: CVPR2026  
**arXiv**: [2512.01248](https://arxiv.org/abs/2512.01248)  
**代码**: [github.com/HKU-TASR/TRivia](https://github.com/HKU-TASR/TRivia)  
**领域**: 多模态VLM  
**关键词**: 表格识别, 自监督微调, GRPO, 强化学习, 无标注数据

## 一句话总结
提出TRivia，一种基于GRPO的自监督微调框架，使VLM能开源、从无标注表格图像中学习表格识别，产出的TRivia-3B超越Gemini 2.5 Pro和MinerU2.5。

## 研究背景与动机
表格识别(TR)是文档解析的核心组件，需将表格图像转换为HTML/Markdown等结构化格式。当前局面：
- **商业模型**（Gemini 2.5 Pro）：凭借海量人力和计算资源达到前沿，但馬隐私问题
- **开源模型**：受限于标注数据规模，远落后于商业模型
- **数据获取困境**：合成数据缺乏多样性，人工标注昂贵，蒸馏伪标签受限20模型性能上限

核心问题：能否利用无标注的真实表格图像来突破标注数据的性能上限？

## 方法详解

### 整体框架
两阶段：(1)准备阶段——从无标注图像中构建QA监督信号；(2)训练阶段——用GRPO和QA奖励微调VLM。

### 关键设计

1. **Table QA驱动的GRPO训练**：
   - 为每张表格图像生成R个识别结果
   - 每个结果与QA对配对，用LLM回答问题
   - 奖励: $\text{Reward}(o_j) = \frac{1}{|QA|}\sum F1(M_{LLM}(q;o_j), a)$
   - 关键洞察：表格QA作为TR的代理任务，能正确回答问题意味着识别结果充分保留了文本和结构信息

2. **Response-Consistency Sampling**：
   - 不是所有无标注样本都同等有用
   - 对每张图像生成K个识别结果，计算配对TEDS相似度
   - $\text{Consistency}(I) = \frac{2}{K^2-K}\sum_{i<j} \text{TEDS}(o_i, o_j)$
   - 低一致性 = 高响应多样性 = 更有价值的GRPO训练样本

3. **Attention-Guided 多样化QA生成**：
   - 利用VLM的注意力机制确定每个QA的视觉来源
   - $\text{VS}((q,a); I, M_{QA}) = \{v | A_{M_{QA}}(v|a) > \tau_A\}$
   - 贪心选择视觉源重叠最小的QA对，确保覆盖表格不同区域
   - 有效性交叉验证：仅保留有图像时能正确回答的QA

### 损失函数 / 训练策略
TRivia-3B三阶段训练：
1. OTSL语法预热（700K, 仅微调语言模型）
2. 标注数据监督微调（确立性能上限）
3. TRivia自监督微调（突破上限）

## 实验关键数据

### 主实验
| 模型 | PubTabNet TEDS | OmniDocBench TEDS | CC-OCR TEDS | OCRBench TEDS |
|------|---------------|------------------|------------|---------------|
| UniTable | 86.44 | 82.76 | 57.84 | 67.73 |
| Qwen2.5-VL-72B | 84.39 | 87.85 | 81.22 | 81.33 |
| Gemini 2.5 Pro | - | 强 | 强 | 强 |
| MinerU2.5 | - | ~90 | ~80 | ~84 |
| TRivia-3B | 最优 | 最优 | 最优 | 最优 |

### 消融实验
| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 无非法样本过滤 | 训练不稳定 | 零奖励样本会抬高有效响应的相对优势 |
| 无注意力引导 | QA覆盖不充分 | 多次采样产生重叠QA |
| 无一致性采样 | 训练效率低 | 等价地处理所有样本有浪费 |

### 关键发现
- 3B开源模型通过无标注数据自监督微调超趇了Gemini 2.5 Pro和GPT-5
- 自监督微调突破了监督微调的性能天花板，证明无标注数据的价值
- Response-consistency sampling显著提升了GRPO训练的效率
- 非法样本过滤对训练稳定性至关重要

## 亮点与洞察
- 核心思想精彩：用下游任务(QA)的表现作为上游任务(TR)的奖励，不需要显式标注
- Attention-guided QA生成是巧妙的设计：利用VLM自身的注意力确保多样性
- OTSL格式比HTML更紧凑，减少了token数和结构预测复杂度
- 结果印证了scaling law在数据质量维度的重要性

## 局限性 / 可改进方向
- QA生成依赖教师模型的质量，教师模型的偏差会传播
- Response-consistency sampling离线执行，未实现在线自适应
- GRPO训练计算量大（每张图片需多次生成）
- OTSL格式相比HTML可读性较差

## 相关工作与启发
- TDATR等都依赖标注数据，TRivia开辟了无标注学习的新道路
- MinerU2.5采用蒸馏策略但受限于教师模型天花板，TRivia突破了这一限制
- QA作为代理奖励的思路可推广到其他结构化预测任务

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 无标注数据+RL的新范式突破标注数据天花板
- 实验充分度: ⭐⭐⭐⭐ 多基准对比+完整消融
- 写作质量: ⭐⭐⭐⭐ 动机清晰，每个组件有明确动机
- 价值: ⭐⭐⭐⭐⭐ 3B开源模型超趇商业系统，实用价值极高
