---
title: >-
  [论文解读] TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding
description: >-
  [ICLR 2026][多模态][表格理解] 提出TableDART——通过轻量MLP门控网络(2.59M参数)动态选择最优模态路径(文本/图像/融合)的表格理解框架：复用预训练单模态模型(冻结)→每个query-table对动态路由→融合时用LLM agent仲裁/综合两路输出→训练高效(仅训练门控)→7个基准SOTA超最强基线平均4.02%。
tags:
  - ICLR 2026
  - 多模态
  - 表格理解
  - 动态路由
  - 多模态融合
  - 门控网络
  - LLM Agent
---

# TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding

**会议**: ICLR 2026  
**arXiv**: [2509.14671](https://arxiv.org/abs/2509.14671)  
**代码**: [GitHub](https://github.com/xiaobo-xing/TableDART)  
**领域**: 表格理解/多模态路由  
**关键词**: 表格理解, 动态路由, 多模态融合, 门控网络, LLM Agent

## 一句话总结
提出TableDART——通过轻量MLP门控网络(2.59M参数)动态选择最优模态路径(文本/图像/融合)的表格理解框架：复用预训练单模态模型(冻结)→每个query-table对动态路由→融合时用LLM agent仲裁/综合两路输出→训练高效(仅训练门控)→7个基准SOTA超最强基线平均4.02%。

## 研究背景与动机

**领域现状**：表格理解→Table-as-Text(LLM线性化→丢结构)→Table-as-Image(VLM截图→弱语义)→Table-as-Multimodality(两者融合→但静态不灵活)。

**现有痛点**：
   - (1) 静态双模态→每个query都用两路→冗余→甚至冲突(文本行序敏感 vs 图像置换不变)
   - (2) MLLM微调→计算代价极高→即使PEFT也不scalable
   - (3) 不是所有query都需要两路→简单query单路足够

**切入角度**：动态路由→轻量门控→每个实例选最优路径→复用已有单模态专家。

## 方法详解

### 五大组件

1. **Table-as-Text模型$\mathcal{M}_t$**：LLM处理线性化表格
2. **Table-as-Image模型$\mathcal{M}_v$**：VLM处理表格截图
3. **Query嵌入模型**：文本嵌入编码查询
4. **门控网络**(2.59M参数,唯一可训练部分)：
    - 输入：query嵌入
    - 输出：3路概率(Text-only/Image-only/Fusion)
    - 选择最高概率路径

5. **LLM Agent**(融合时)：
    - 仲裁者：选择两路中更好的输出
    - 救援者：综合两路推理→生成改进的答案

### 训练效率
- 所有LLM/VLM冻结→仅训练2.59M门控网络
- vs MLLM微调→计算代价低几个数量级

## 实验关键数据

### 7个基准(WTQ/WikiSQL/TabFact等)
| 方法 | 平均准确率 | 训练成本 |
|------|----------|---------|
| TableLlama(文本) | 中 | 全微调 |
| Table-LLaVA(图像) | 中 | 全微调 |
| HIPPO(MLLM融合) | 较好 | MLLM微调 |
| **TableDART** | **+4.02%** | **仅2.59M** |

### 路由分析
- ~35%查询→Text-only足够(简单查找)
- ~25%查询→Image-only更好(布局依赖)
- ~40%查询→需要Fusion(复杂推理)
- 门控学到的分布→具有可解释性

### 关键发现
- 动态路由→避免冲突→比静态双路好3-5%
- LLM Agent融合→比简单拼接/平均好→因为可以推理
- 门控在未见数据集上泛化→路由策略可迁移
- 2.59M训练→极低成本→可以快速适应新场景

## 亮点与洞察
- **"路由>融合"**：不是简单合并两路→而是智能选择→避免了冲突信号。
- **2.59M的极端效率**：vs 数十亿参数的MLLM微调→效率差3个数量级→但效果更好。
- **复用已有模型**：不训练新模型→组合现有最佳→工程实用。
- **LLM作为仲裁者**：不只是选择→还能"两面看"后综合→比任何自动方法更灵活。

## 评分
- 新颖性: ⭐⭐⭐⭐ 动态多模态路由+LLM Agent融合
- 实验充分度: ⭐⭐⭐⭐⭐ 7基准+路由分析+泛化
- 写作质量: ⭐⭐⭐⭐ 框架描述清晰
- 价值: ⭐⭐⭐⭐⭐ 对表格理解有实际推动+模式可推广
