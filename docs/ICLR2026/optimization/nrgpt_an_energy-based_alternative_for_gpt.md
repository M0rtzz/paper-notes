---
title: >-
  [论文解读] NRGPT: An Energy-based Alternative for GPT
description: >-
  [ICLR 2026][优化][能量基模型] 提出NRGPT(eNeRgy-GPT)——将GPT设定与能量基模型(EBM)框架统一的最小修改方案：设计能量函数使推理过程成为tokens在能量landscape上的探索,证明某些条件下此探索等价于梯度下降(虽然非梯度下降不一定最差),在Shakespeare/ListOPS/OpenWebText上验证可行性,观察到可能更抗过拟合的特性。
tags:
  - ICLR 2026
  - 优化
  - 能量基模型
  - GPT
  - 自回归
  - 梯度下降推理
  - 布朗运动
---

# NRGPT: An Energy-based Alternative for GPT

**会议**: ICLR 2026  
**arXiv**: [2512.16762](https://arxiv.org/abs/2512.16762)  
**代码**: 无  
**领域**: 语言模型架构/能量模型  
**关键词**: 能量基模型, GPT, 自回归, 梯度下降推理, 布朗运动

## 一句话总结
提出NRGPT(eNeRgy-GPT)——将GPT设定与能量基模型(EBM)框架统一的最小修改方案：设计能量函数使推理过程成为tokens在能量landscape上的探索,证明某些条件下此探索等价于梯度下降(虽然非梯度下降不一定最差),在Shakespeare/ListOPS/OpenWebText上验证可行性,观察到可能更抗过拟合的特性。

## 研究背景与动机

**领域现状**：GPT→标准自回归→next-token prediction。EBM→通过能量函数定义模型→低能量=合理样本。两者看似完全不同但隐含深层联系(ICL≈梯度下降等暗示)。

**现有痛点**：
   - (1) GPT和EBM之间的联系→仍不明确→无法互相借鉴
   - (2) Energy Transformer→为BERT-like掩码补全设计→不适用于GPT的序列移位设定
   - (3) Von Oswald/Ahn等工作→仅考虑线性Transformer(无softmax)→过度简化
   - (4) 如何在不改变训练范式的情况下让GPT具有EBM的优势(可解释性/对齐)？

**切入角度**：最小修改GPT→使推理(前向传播)成为tokens在能量landscape上的迭代更新→统一两个框架。

## 方法详解

### NRGPT设计

**核心思想**：每个token有自己的能量landscape→依赖于其他tokens的状态→推理=每个token在其能量landscape上迭代更新

**能量函数**：
- 每个token t 的能量由注意力得分和MLP的交互定义
- $E_t = E_{attn}(h_t, H_{<t}) + E_{mlp}(h_t)$
- 其中$h_t$是token t的隐藏状态

**更新规则**：
- $h_t^{(k+1)} = h_t^{(k)} - \eta \nabla_{h_t} E_t(h_t^{(k)}, H)$
- 多次应用NRGPT块→tokens迭代演化
- 输入序列[x_1,...,x_T]→演化为[x_2,...,x_{T+1}]

### 变体
- 基础：固定学习率η
- 可学习η：每层学习更新率
- +LayerNorm/RMSNorm：增加归一化

### 关键理论
- **定理**：在某些条件下(无RMSNorm/LayerNorm)，NRGPT的前向传播严格等价于能量函数的梯度下降
- 但实验表明：非严格梯度下降的版本(有Norm)性能可能更好→打破严格GD不一定坏

### 训练
- 标准自回归训练(next-token prediction)→不改变训练方式
- 仅推理时解释为能量探索→训练是标准的

## 实验关键数据

### Shakespeare字符级语言建模
| 方法 | BPC↓ | 说明 |
|------|------|------|
| 标准GPT | 基线 | 自回归 |
| **NRGPT** | **竞争力** | 能量基 |

### ListOPS(嵌套代数推理)
| 任务 | NRGPT | GPT | 说明 |
|------|-------|-----|------|
| 算术 | ≈ | 基线 | |
| min/max | ≈ | 基线 | |
| 嵌套组合 | **更好** | 基线 | 迭代推理优势 |

### OpenWebText语言建模
- NRGPT在OWT上可行→PPL竞争力
- 观察：更长训练→NRGPT过拟合更慢→可能有正则化效果

### 关键发现
- NRGPT≈GPT在标准基准→但有EBM的理论优势
- 严格梯度下降不是最优→有Norm的版本更好→虽然破坏GD但实用
- 抗过拟合→仅在很长训练才过拟合→能量landscape提供隐式正则
- 可学习η→每层不同更新率→适应不同抽象级别

## 亮点与洞察
- **"GPT ∩ EBM"的最小统一**：不是用EBM替代GPT→而是证明GPT可以被解释为EBM→完全统一。
- **推理=能量下降**：前向传播=tokens在能量landscape上下降→赋予了推理过程物理含义。
- **正则化效果**：能量landscape的结构→可能提供比标准dropout/weight decay更自然的正则化。
- **Alignment的潜力**：能量函数→可以加正则项→为模型对齐提供新工具(论文讨论但未实验)。
- **挑战"GD最优"**：理论上推理=GD→但实验显示非GD更好→引发关于EBM推理的深层思考。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 首次将GPT设定cast为well-defined的EBM
- 实验充分度: ⭐⭐⭐ Shakespeare+ListOPS+OWT→但规模有限
- 写作质量: ⭐⭐⭐⭐⭐ 理论和实验的平衡excellent
- 价值: ⭐⭐⭐⭐ 对理解Transformer和EBM的联系有根本性贡献
