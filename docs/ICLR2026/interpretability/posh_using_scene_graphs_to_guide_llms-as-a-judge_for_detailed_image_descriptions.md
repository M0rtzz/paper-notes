---
title: >-
  [论文解读] PoSh: Using Scene Graphs To Guide LLMs-as-a-Judge For Detailed Image Descriptions
description: >-
  [ICLR 2026][图像描述评估] 提出PoSh评估指标，用场景图作为结构化评分标准引导LLM-as-Judge对详细图像描述进行细粒度错误定位（属性/关系误附着），配合DOCENT艺术品详细描述基准（1750专家描述+900细粒度人工判断），在人类判断相关性上超越GPT-4o-as-Judge且完全开源可复现。
tags:
  - ICLR 2026
  - 图像描述评估
  - 场景图
  - LLM-as-Judge
  - 细粒度错误
  - 辅助文本
---

# PoSh: Using Scene Graphs To Guide LLMs-as-a-Judge For Detailed Image Descriptions

**会议**: ICLR 2026  
**arXiv**: [2510.19060](https://arxiv.org/abs/2510.19060)  
**代码**: [GitHub](https://github.com/amith-ananthram/posh)  
**领域**: 多模态评估  
**关键词**: 图像描述评估, 场景图, LLM-as-Judge, 细粒度错误, 辅助文本

## 一句话总结
提出PoSh评估指标，用场景图作为结构化评分标准引导LLM-as-Judge对详细图像描述进行细粒度错误定位（属性/关系误附着），配合DOCENT艺术品详细描述基准（1750专家描述+900细粒度人工判断），在人类判断相关性上超越GPT-4o-as-Judge且完全开源可复现。

## 研究背景与动机

**领域现状**：VLM能生成详细图像描述，但评估方法落后。标准指标(CIDEr/SPICE)设计用于短文本，LLM-as-Judge不可复现且缺乏可解释性。

**现有痛点**：(1) 长描述中属性/关系误附着是常见错误(如"倒水的男人"被描述为"中央的男人")→现有指标不敏感；(2) 粗粒度分数无法定位具体错误→迭代改进需要昂贵的人工检查；(3) 闭源LLM评估不可复现。

**切入角度**：场景图将描述降维为视觉组件(实体+属性+关系)→作为LLM-Judge的结构化评分标准→每个错误定位到具体文本段→聚合为可解释的粗粒度分数。

## 方法详解

### PoSh流程
1. 从生成描述和参考描述分别提取场景图
2. 场景图作为结构化rubric引导LLM识别每个entity/attribute/relation的错误
3. 错误产出两类：mistakes(生成中错误的)+omissions(生成中遗漏的)
4. 聚合为粗粒度分数(mistakes score + omissions score + overall)

### DOCENT基准
- 1750幅艺术品(National Gallery of Art)+专家撰写辅助文本
- 900份VLM生成描述的人工判断(细粒度+粗粒度)，来自艺术史学生
- 平均描述251词/161个视觉组件→远超其他基准

## 实验关键数据

| 指标 | Spearman ρ vs 人类 | 可复现 | 可解释 |
|------|------------------|--------|--------|
| CIDEr/SPICE | 低 | ✓ | ✗ |
| GPT-4o-as-Judge | 中 | ✗ | ✗ |
| LLaVA-Critic | 中 | ✓ | ✗ |
| **PoSh** | **+0.05 vs 最强** | **✓** | **✓** |

### 关键发现
- PoSh作为奖励函数优于SFT→可直接驱动描述生成改进
- 在CapArena(网络图片)上同样有效→对图像类型鲁棒
- 场景图保留了属性/关系的附着结构→比忽略附着的SPICE更准确
- 基础模型在DOCENT艺术品上挣扎→复杂场景动态是新挑战

## 亮点与洞察
- **场景图作为结构化rubric**：比直接让LLM评分更可靠——场景图将"评什么"具体化为一组可检查的视觉组件。
- **细粒度→粗粒度的可解释性**：知道总分不够→需要知道哪些实体的哪些属性错了→PoSh提供这种诊断。
- **DOCENT的社会价值**：辅助文本生成(alt-text)对残障人士的网络可及性至关重要→艺术品的复杂视觉需要更好的描述→PoSh推动这一方向。

## 评分
- 新颖性: ⭐⭐⭐⭐ 场景图+LLM-Judge的结合及DOCENT基准
- 实验充分度: ⭐⭐⭐⭐ DOCENT+CapArena+奖励函数验证
- 写作质量: ⭐⭐⭐⭐⭐ 社会动机清晰，技术方案优雅
- 价值: ⭐⭐⭐⭐ 对详细图像描述评估有直接实用价值
