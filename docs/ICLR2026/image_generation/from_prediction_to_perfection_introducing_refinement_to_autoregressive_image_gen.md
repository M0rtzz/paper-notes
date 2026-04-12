---
title: >-
  [论文解读] From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation
description: >-
  [ICLR 2026][图像生成][自回归] 提出TensorAR——将标准AR图像生成从"next-token prediction"升级为"next-tensor prediction"：每步预测一组重叠的连续token(tensor),相邻tensor的重叠区域使后续预测可以修正先前输出,引入离散扩散噪声机制解决训练时的信息泄漏问题,作为即插即用扩展兼容现有AR模型(LlamaGen/Janus-Pro),在class-to-image和text-to-image任务上一致提升质量。
tags:
  - ICLR 2026
  - 图像生成
  - 自回归
  - 精修
  - tensor预测
  - 离散扩散噪声
  - 即插即用
---

# From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation

**会议**: ICLR 2026  
**arXiv**: [2505.16324](https://arxiv.org/abs/2505.16324)  
**代码**: 无  
**领域**: 图像生成/自回归  
**关键词**: 自回归, 精修, tensor预测, 离散扩散噪声, 即插即用

## 一句话总结
提出TensorAR——将标准AR图像生成从"next-token prediction"升级为"next-tensor prediction"：每步预测一组重叠的连续token(tensor),相邻tensor的重叠区域使后续预测可以修正先前输出,引入离散扩散噪声机制解决训练时的信息泄漏问题,作为即插即用扩展兼容现有AR模型(LlamaGen/Janus-Pro),在class-to-image和text-to-image任务上一致提升质量。

## 研究背景与动机

1. **领域现状**：AR模型(LlamaGen/VAR/MAR)在图像生成中日益强大→但有根本限制：一旦生成就无法修正→早期token的错误累积影响全局。

2. **现有痛点**：
   - (1) 标准AR：左到右严格序列→无法回头修正→错误累积
   - (2) 扩散集成(DART)：改变训练目标(分类→回归)→难与LLM统一
   - (3) 掩码AR(MaskGIT/MAR)：需要改架构(双向注意力)→不兼容GPT-style
   - (4) 上述方法都改变了标准AR范式→阻碍多模态集成

3. **切入角度**：能否在不改架构/训练范式的情况下让AR模型具备修正能力？→答案：预测重叠tensor。

## 方法详解

### 核心思想：Next-Tensor Prediction

- 每步预测k个连续token组成的tensor(而非单个token)
- 相邻tensor重叠→后一步的前几个token与前一步的后几个token重叠
- 重叠token→后续预测自然修正→迭代精修

### 训练挑战：信息泄漏

- 朴素训练：输入ground-truth tensor→模型可以直接复制重叠token→不学习有意义的因果依赖
- **解决方案：离散tensor噪声**
   - 基于离散扩散理论→对输入tensor注入分类噪声
   - 不同token position不同噪声水平→模拟内部渐进去噪
   - 模型被迫学习真正的生成→而非复制

### 架构组件(轻量)

- **Input Encoder**：包装原始embedding层→残差设计→处理tensor输入
- **Output Decoder**：包装原始线性层→残差设计→输出tensor
- 两者都用残差→更好利用预训练模型→快速收敛

### 即插即用特性
- 不改基础Transformer架构(仍是decoder-only)
- 不改训练目标(仍是分类loss)
- 兼容任何GPT-style AR模型→直接加上input encoder + output decoder

## 实验关键数据

### Class-to-Image (ImageNet 256×256)
| 方法 | FID↓ | 说明 |
|------|------|------|
| LlamaGen-L | 基线 | 标准AR |
| LlamaGen-XL | 较好 | 更大模型 |
| **TensorAR-L** | **更好** | 同参数量更好 |
| **TensorAR-XL** | **最好** | 一致提升 |

### Text-to-Image (Janus-Pro-7B)
| 方法 | GenEval | 说明 |
|------|---------|------|
| Janus-Pro-7B | 基线 | 标准AR |
| **TensorAR** | **+3-5%** | 指令跟随能力提升 |

### 质量-延迟权衡
- TensorAR虽然每步预测更多token→但步数减少→总延迟相当/更少
- 质量更好+延迟不增→帕累托优势

### 关键发现
- 精修主要改善早期token→因为早期token最容易出错
- 噪声水平是关键超参→太少→信息泄漏; 太多→学不到
- 残差设计对利用预训练至关重要→无残差→收敛慢+性能差
- 跨模型规模一致提升→从小到大都work(Figure 2)

## 亮点与洞察
- **"精修而非重新生成"**：AR模型首次具备修正前序预测的能力→类似人类创作"草稿→修改"的过程。
- **离散扩散作为噪声机制**：巧妙地将离散扩散的噪声过程用于解决训练问题→而非用于生成本身。
- **即插即用的实际价值**：不需要重新训练基础模型→加几个轻量组件→任何AR模型都能受益。
- **与Diffusion的哲学对比**：Diffusion=全局迭代精修; TensorAR=局部滑动精修→同样的精修思想但在AR框架内实现。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ Next-tensor预测+离散噪声的组合创新且优雅
- 实验充分度: ⭐⭐⭐⭐ class-to-image+text-to-image+多规模+消融
- 写作质量: ⭐⭐⭐⭐⭐ 核心思想解释清晰，图示直观
- 价值: ⭐⭐⭐⭐⭐ 对AR图像生成范式有重要推进
