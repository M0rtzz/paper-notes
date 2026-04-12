---
title: >-
  [论文解读] GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model
description: >-
  [ICML2025][3D视觉][参数高效微调] 提出 GAPrompt，面向预训练 3D 视觉模型的几何感知点云提示方法，通过 Point Prompt、Point Shift Prompter 和 Prompt Propagation 三组件利用几何线索增强适配能力，仅用 2.19% 可训练参数达到接近全量微调的性能。
tags:
  - ICML2025
  - 3D视觉
  - 参数高效微调
  - 点云
  - 几何感知
  - 提示学习
---

# GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model

**会议**: ICML2025  
**arXiv**: [2505.04119](https://arxiv.org/abs/2505.04119)  
**代码**: [GAPrompt](https://github.com/zhoujiahuan1991/ICML2025-GAPrompt)  
**领域**: 3d_vision  
**关键词**: 参数高效微调, 点云, 几何感知, 提示学习, 3D视觉

## 一句话总结

提出 GAPrompt，面向预训练 3D 视觉模型的几何感知点云提示方法，通过 Point Prompt、Point Shift Prompter 和 Prompt Propagation 三组件利用几何线索增强适配能力，仅用 2.19% 可训练参数达到接近全量微调的性能。

## 研究背景与动机

- **3D 预训练模型**（Point-MAE/Point-FEMAE）全量微调昂贵且有遗忘风险
- **2D PEFT 方法迁移困难**：点云的稀疏性和不规则性使随机初始化的 token prompt 难以对齐
- **现有 3D PEFT 方法**（IDPT/DAPT/Point-PEFT）聚焦 token 特征，忽略点云固有几何信息
- **核心问题**：如何在 PEFT 中显式利用点云的几何信息？

## 方法详解

### Point Prompt（点云提示）

- 引入可学习点云作为辅助输入 → 与原始点云一起编码
- 显式引导模型捕获细粒度几何细节
- 与 token prompt 互补：前者在输入空间操作，后者在 token 空间

### Point Shift Prompter（点偏移提示器）

- 轻量网络从原始点云提取全局形状特征
- 根据形状特征生成 instance-specific 的点偏移
- 实现几何感知的输入级增强
- 全局形状特征还用于增强 prompt token

### Prompt Propagation（提示传播）

- 将 Point Shift Prompter 提取的形状信息注入模型的特征提取过程
- 在每个 Transformer 层之间传播几何信息
- 增强模型对几何特征的持续感知能力

### 训练策略

- 冻结预训练骨干网络
- 仅训练 Point Prompt + Point Shift Prompter + Prompt Propagation（总计 2.19% 参数）

## 实验关键数据

### ScanObjectNN 分类（最难变体 PB_T50_RS）

| 方法 | 可训练参数 | Accuracy |
|---|---|---|
| Full FT | 100% | 基准线 |
| IDPT | 较高 | 接近 FT |
| DAPT | 中等 | 较好 |
| **GAPrompt** | **2.19%** | **超越/持平 FT** |

### ModelNet40 分类

- GAPrompt 超越所有 PEFT 方法，接近 full FT
- 在 Point-MAE 和 Point-FEMAE 两个骨干上一致有效

### 少样本分类

- 5-way 10-shot / 10-way 10-shot 场景均表现最优

### 消融实验

| 组件 | 移除后效果 |
|---|---|
| Point Prompt | 下降 |
| Point Shift Prompter | 显著下降 |
| Prompt Propagation | 中等下降 |
| 全部移除 | 退化到基线 PEFT |

- 三组件协同效果最佳
- Point Shift Prompter 贡献最大（几何信息核心来源）

## 亮点与洞察

1. **几何感知是3D PEFT的关键**：Token-level 操作不足以捕获点云几何
2. **Point Prompt 直接在输入空间操作**：比 token prompt 更自然地利用 3D 结构
3. **Instance-specific 调整**：通过 Point Shift 实现每个实例的适配性增强
4. **极低参数量**（2.19%）即可匹配甚至超越全量微调

## 局限性 / 可改进方向

- Point Shift Prompter 的网络结构较简单，更复杂的几何编码可能更好
- 未在 3D 检测/分割等下游任务上验证
- 对预训练模型类型的依赖性需评估

## 相关工作与启发

- Jia et al. (2022) VPT：Visual Prompt Tuning
- Zha et al. (2023) IDPT：3D 动态 prompt
- Zhou et al. (2024) DAPT：动态 adapter
- 启发：几何感知提示方法可推广到其他 3D 任务

## 评分

⭐⭐⭐⭐ — 设计简洁优雅，几何感知思路对 3D PEFT 有重要启示，参数效率极高

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
