---
title: >-
  [论文解读] STRIDE: Subset-Free Functional Decomposition for XAI in Tabular Settings
description: >-
  [ICLR 2026][人体理解][功能分解] 提出STRIDE——在RKHS中通过递归核中心化实现无需子集枚举的正交功能分解，从标量归因升级到完整功能成分f_S(x_S)，揭示特征如何交互而非仅什么重要，10个表格数据集中位加速3.0x(vs TreeSHAP)、均值R2=0.93，首创成分手术隔离量化单一交互的性能影响。
tags:
  - ICLR 2026
  - 人体理解
  - 功能分解
  - RKHS
  - 特征交互
  - 正交分解
  - 核方法
  - TreeSHAP
  - 成分手术
---

# STRIDE: Subset-Free Functional Decomposition for XAI in Tabular Settings

**会议**: ICLR 2026  
**arXiv**: [2509.09070](https://arxiv.org/abs/2509.09070)  
**领域**: 可解释AI/表格数据  
**关键词**: 功能分解, RKHS, 特征交互, 正交分解, 核方法, TreeSHAP, 成分手术

## 一句话总结
提出STRIDE——在RKHS中通过递归核中心化实现无需子集枚举的正交功能分解，从标量归因升级到完整功能成分f_S(x_S)，揭示特征如何交互而非仅什么重要，10个表格数据集中位加速3.0x(vs TreeSHAP)、均值R2=0.93，首创成分手术隔离量化单一交互的性能影响。

## 研究背景与动机

**领域现状**：现有XAI方法(SHAP/LIME/IG)以标量归因表示特征重要性→丢失非线性交互结构；Shapley值需枚举2^d子集→不可行。

**现有痛点**：
   - (1) 标量无法区分synergy与redundancy→知道什么重要但不知如何运作
   - (2) KernelSHAP近似仍昂贵；TreeSHAP仅限树模型
   - (3) 核Sobol指数仅全局分析；Lengerich et al.仅限树集成
   - (4) 缺乏同时做实例级+模型无关+高效的功能分解方法

**切入角度**：RKHS中递归中心化核→解析计算正交功能成分→无需枚举。

## 方法详解

### 整体框架
将模型函数f分解为正交成分之和f=Sum_S f_S(x_S)，每个f_S仅依赖子集S，所有f_S在L2(mu)下互相正交，分解唯一。

### 关键设计

1. **递归核中心化**：

    - 中心化核K_S^(c)=K_S-Sum_{R subset S}K_R^(c)（Mobius反演）
    - Lemma 2：中心化核在任意组成维度积分为零→保证正交
    - Theorem 1：不同子集的中心化核函数在L2中正交

2. **解析投影**：

    - f_S(x_S)=<f, K_S^(c)(dot,x_S)>由再生核性质得到
    - Proposition 1：f=Sum_S f_S唯一分解→无需枚举2^d子集
    - 可聚合为Shapley兼容标量：phi_i(x)=Sum_{S ni i}(1/|S|)f_S(x_S)

3. **成分手术(Component Surgery)**：

    - 识别最有影响力的交互成分f_{ij}→从预测中移除→测量性能变化
    - 回答交互是统计伪迹还是模型逻辑的承重部分
    - California Housing移除最强交互→R2下降0.023+-0.004

### 训练策略
- 积分用经验平均近似；投影数值计算
- 核选择+低秩截断+正则化
- MacBook Air M1 8GB无GPU

## 实验关键数据

### 主实验(10个数据集，mean over 10 seeds)

| 数据集 | d | STRIDE(s) | TreeSHAP(s) | 加速 | R2 | Spearman |
|--------|---|-----------|-------------|------|-----|----------|
| YearPrediction | 90 | 72.6 | 169.0 | 2.3x | 0.808 | 0.549 |
| German Credit | 57 | 0.131 | 0.240 | 1.9x | 0.958 | 0.862 |
| Breast Cancer | 30 | 0.069 | 0.038 | 0.6x | 0.999 | 0.728 |
| Credit Default | 23 | 1.609 | 11.679 | **7.3x** | 0.988 | 0.930 |
| Online Shoppers | 25 | 1.039 | 3.914 | 3.8x | 0.965 | 0.920 |
| Heart Disease | 13 | 0.030 | 0.048 | 1.6x | 0.999 | 0.929 |
| California | 8 | 0.550 | 5.331 | **9.7x** | 0.932 | 0.952 |
| Abalone | 10 | 0.418 | 1.084 | 2.6x | 0.958 | 0.881 |
| Wine Quality | 11 | 0.624 | 1.848 | 3.0x | 0.903 | 0.821 |
| Diabetes | 10 | 0.041 | 0.116 | 3.0x | 0.993 | 0.779 |

### 消融/案例分析
- **成分手术**：移除Longitude x Population交互→测试R2降0.023+-0.004→非伪迹
- **协同-冗余热图**：Lat-Lon冗余(蓝)；Lon x Pop正协同(红)→完美匹配领域知识
- **What-if**：增大MedInc→Lat/Lon依赖降低→模型学到位置是收入代理

### 关键发现
- 中位加速3.0x(最高9.7x California)
- R2范围0.808-0.999均值约0.93→高保真
- 全局排名与TreeSHAP高度一致(多数Spearman>0.85)
- 弱信号(YearPrediction)一致性低(0.55)→归因本身不稳定

## 亮点与洞察
- **范式转换**：从什么重要到如何交互→功能视图严格泛化标量归因
- **成分手术**：首次量化单一交互对黑盒性能的直接因果影响
- **模型无关+实例级**：post-hoc→适用于任何表格模型
- **理论严谨**：正交性+唯一性+L2收敛→不仅是经验方法

## 局限性
- 限于表格数据+随机森林→深度学习模型和GPU未验证
- 高阶交互高效求解需进一步探索
- 核/低秩超参需数据驱动自动选择
- 小数据集上TreeSHAP更快(Breast Cancer 0.6x)

## 相关工作与启发
- Hoeffding ANOVA分解→STRIDE的L2正交基础
- TreeSHAP→强基线但限于树；KernelSHAP→通用但慢+标量
- KAN→内置可解释但非post-hoc
- 启发：功能分解可扩展到视觉/NLP更深层调试

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ RKHS正交功能分解+成分手术
- 技术深度: ⭐⭐⭐⭐⭐ Hilbert空间理论严谨
- 实验充分度: ⭐⭐⭐⭐ 10个数据集多维度评估
- 实用性: ⭐⭐⭐⭐ 表格可解释AI直接实用
- 综合: ⭐⭐⭐⭐⭐ XAI从标量到功能的概念飞跃
