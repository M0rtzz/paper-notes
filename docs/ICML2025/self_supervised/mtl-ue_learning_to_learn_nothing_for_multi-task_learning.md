---
title: >-
  [论文解读] MTL-UE: Learning to Learn Nothing for Multi-Task Learning
description: >-
  [ICML2025][自监督学习][不可学习样本] 提出 MTL-UE，首个针对多任务学习数据的不可学习样本框架，通过编码器-解码器注入类别先验嵌入并结合任务内/任务间嵌入正则化，有效保护 MTL 和 STL 模型免受未授权训练。
tags:
  - ICML2025
  - 自监督学习
  - 不可学习样本
  - 多任务学习
  - 数据保护
  - 投毒攻击
  - 类别嵌入
---

# MTL-UE: Learning to Learn Nothing for Multi-Task Learning

**会议**: ICML2025  
**arXiv**: [2505.05279](https://arxiv.org/abs/2505.05279)  
**代码**: 待确认  
**领域**: self_supervised  
**关键词**: 不可学习样本, 多任务学习, 数据保护, 投毒攻击, 类别嵌入

## 一句话总结

提出 MTL-UE，首个针对多任务学习数据的不可学习样本框架，通过编码器-解码器注入类别先验嵌入并结合任务内/任务间嵌入正则化，有效保护 MTL 和 STL 模型免受未授权训练。

## 研究背景与动机

- **隐私保护需求**：大模型时代数据爬取引发隐私关切
- **UE 基本思想**：加不可见扰动使模型学虚假特征而非真实特征
- **MTL 场景被忽视**：现有 UE 仅针对单任务，MTL 数据集（如 CelebA 40 属性）缺乏方案
- **关键发现**：代理依赖 UE 因逐样本优化导致类内方差不可控；Patch-based 方法随任务数增多失效

## 方法详解

### 框架

- **编码器** $E$：提取输入图像隐表示 $z$
- **类别嵌入**：每任务每类独立嵌入 $\{e_i^k\}$，维度为 $d_e$
- **解码器** $D$：将 $[z, e_{y^1}^1,\ldots,e_{y^K}^K]$ 拼接后生成扰动
- **约束**：$\delta=\text{Clip}(D(\cdot),-\epsilon,\epsilon)$，通常 $\epsilon=8/255$
- **搜索空间缩减**：从像素级搜索 $\|\delta\|_\infty\leq\epsilon$ 缩减到解码器输出空间

### 嵌入正则化

**Intra-task ER**：同任务不同类嵌入最小化余弦相似度，增大类间距离

$$\mathcal{L}_{Intra}=\frac{2}{\sum_k C_k(C_k-1)}\sum_k\sum_{m<n}\cos(e_m^k,e_n^k)$$

**Inter-task ER**：不同任务嵌入几何独立，减少冗余、降低耦合、提高可解释性

$$\mathcal{L}_{Inter}=\frac{1}{\sum_{k<l}C_kC_l}\sum_{k<l}\sum_m\sum_n|\cos(e_m^k,e_n^l)|$$

### 总损失

$$\mathcal{L}=\mathcal{L}_b(F',x+\delta,y)+\lambda_1\mathcal{L}_{Intra}+\lambda_2\mathcal{L}_{Inter}$$

### 即插即用 + 稠密预测扩展

- 可接入 EM/TAP/SEP 等任意代理依赖型 UE 方法
- 对稠密标签用嵌入模块 $\mathcal{E}^k$ 映射标签图为嵌入
- 对 NYUv2（语义分割/深度估计/法线估计）同样有效
- 支持部分保护：选择性地使部分任务不可学习，其余正常学习

## 实验关键数据

### CelebA（40 任务，ResNet-18）

| 方法 | MTL Avg↓ | STL Avg↓ |
|---|---|---|
| Clean | 91.11 | 90.35 |
| AR (Patch) | 73.12 | 84.41 |
| MTL-UE+EM | 显著降低 | 显著降低 |

- 类内标准差：MTL-UE 实现最低
- 5 种 backbone、5 种 MTL 策略一致有效
- 支持部分保护

## 亮点与洞察

1. 首次系统研究 MTL 数据保护问题，填补重要空白
2. 生成器结构天然降低类内方差 → UE 有效性的关键
3. 即插即用框架设计，可与任意代理依赖型 UE 方法结合
4. 从分类扩展到稠密预测，覆盖 MTL 主要任务类型
5. Intra-ER 和 Inter-ER 的嵌入正则化有清晰的几何直觉

## 局限性 / 可改进方向

- 需要代理 MTL 模型进行优化
- 对抗训练等防御的鲁棒性待评估
- 任务间标签组合爆炸通过嵌入缓解但未根本解决
- 编码器-解码器架构的容量可能限制对高分辨率图像的效果
- 嵌入维度对性能的影响需更多分析

## 相关工作与启发

- Huang et al. (2021) EM：UE 开创工作
- Sandoval-Segura et al. (2022) AR：无代理 UE
- Yu et al. (2024a)：类内方差理论分析
- Fowl et al. (2021) TAP：对抗扰动作为 UE
- Kendall et al. (2018)：MTL 不确定性加权
- 启发：嵌入注入可推广到更多可控扰动场景

## 评分

⭐⭐⭐⭐ — 问题新颖，实验充分，即插即用框架设计精巧，首个MTL数据保护系统化研究

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
