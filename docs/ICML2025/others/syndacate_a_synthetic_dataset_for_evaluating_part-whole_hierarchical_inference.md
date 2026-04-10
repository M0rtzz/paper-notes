# SynDaCaTE: A Synthetic Dataset for Evaluating Part-Whole Hierarchical Inference

## 元信息
- **会议**: ICML 2025 (MOSS Workshop)
- **arXiv**: [2506.17558](https://arxiv.org/abs/2506.17558)
- **代码**: [GitHub](https://github.com/jakelevi1996/syndacate-public)
- **领域**: 计算机视觉 / 归纳偏置
- **关键词**: 胶囊网络, 部分-整体层次, 合成数据集, SetTransformer, 归纳偏置

## 一句话总结
提出SynDaCaTE合成数据集用于评估部分-整体层次推断能力，揭示CapsNet瓶颈在于图像到部件推断，且SetTransformer是部件到整体推断的强基线。

## 研究背景与动机
- 部分-整体层次是人类视觉系统的核心能力，胶囊网络声称能学习这种层次
- 但缺乏ground-truth部件信息，无法验证模型是否真正学到了层次推断
- 需要一个控制变量的合成数据集来解耦"图像→部件"和"部件→整体"两个子任务

## 方法详解

### Mereological Inference框架
将部分-整体推断分解为：
1. **Image-to-Parts**：从图像推断部件集合 $\mathcal{P}$
2. **Parts-to-Wholes**：从部件集合推断整体集合 $\mathcal{W}$

### SynDaCaTE数据集
- 3类对象：线段、字符、单词（21种类型）
- 每个对象有类别标签 + 姿态向量（位置/大小/旋转等）
- 可控参数生成多种任务：ImToClass、ImToParts、PartsToChars、PartsToClass等
- 60k训练/10k测试

### 模型对比
- CapsNet (Sabour et al., 2017)
- 现代化CNN（CoordConv + ReZero + 深度可分离卷积）
- SetTransformer（置换等变自注意力）
- DeepSetToSet、MLP基线

## 实验

### 关键发现

**发现1：CapsNet瓶颈在Image-to-Parts**
| 输入 | CNN | CapsNet |
|------|-----|---------|
| 图像(ImToClass) | 更高精度 | 低精度 |
| 预训练部件编码 | 相近 | 相近 |

给定部件信息后两者持平→CapsNet的弱点不在Parts-to-Wholes

**发现2：SetTransformer是Parts-to-Wholes的强基线**
| 模型 | PartsToChars MSE (depth=4) |
|------|--------------------------|
| SetTransformer | **最低（>10×优势）** |
| DeepSetToSet | 中等 |
| Element-wise MLP | 高 |
| Flattened MLP | 最高 |

且≥2层自注意力是关键——增加宽度无帮助。

**发现3：部件信息提升数据效率**
使用ground-truth部件的PartsToClass任务中，SetTransformer在极小数据集上即达高精度。

## 亮点
- 首次通过控制实验精确定位CapsNet的瓶颈
- 数据集设计精巧：可分离地评估两个子任务
- 发现SetTransformer需要≥2层注意力才生效（与Induction Heads现象呼应）
- 对归纳偏置设计提供了新方向

## 局限性
- 合成数据过于简单（线段/字符），与自然图像差距大
- 仅评估了一种CapsNet变体
- Parts-to-Wholes任务假设已知部件，但实际中部件提取是主要挑战
- Workshop paper，篇幅有限，消融不够充分

## 评分
⭐⭐⭐ 虽为workshop paper但洞察有价值，通过简洁的实验设计得出了关于CapsNet和SetTransformer的清晰结论。
