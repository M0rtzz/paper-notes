---
title: >-
  [论文解读] Training-free Motion Factorization for Compositional Video Generation
description: >-
  [图像生成] 提出一种无需训练的运动分解框架，将复杂场景运动拆分为静止、刚性运动和非刚性运动三类，通过结构化运动推理 (SMR) 消除提示语义歧义，再借助解耦运动引导 (DMG) 模块分别约束各类运动的生成，实现多实例多运动类别的组合视频合成。
tags:
  - 图像生成
---

# Training-free Motion Factorization for Compositional Video Generation

| 属性 | 值 |
|------|------|
| 会议 | CVPR2026 |
| arXiv | [2603.09104](https://arxiv.org/abs/2603.09104) |
| 代码 | 即将开源 |
| 领域 | 图像生成 (视频生成) |
| 关键词 | 组合视频生成, 运动分解, 无训练, 扩散模型, 运动引导 |

## 一句话总结

提出一种无需训练的运动分解框架，将复杂场景运动拆分为静止、刚性运动和非刚性运动三类，通过结构化运动推理 (SMR) 消除提示语义歧义，再借助解耦运动引导 (DMG) 模块分别约束各类运动的生成，实现多实例多运动类别的组合视频合成。

## 研究背景与动机

组合视频生成 (Compositional Video Generation, CVG) 旨在根据复杂用户提示合成包含多实例、多运动类别的视频。尽管商用视频生成模型已广泛部署，其核心问题在于：

**运动语义歧义**：直接从用户提示生成边界框序列容易产生断裂的运动路径和异常的尺寸变化，因为自然语言本身具有模糊性。
**运动引导粗糙**：现有方法对所有实例施加统一的扩散引导，无法区分静止、刚体平移、非刚体形变等不同运动类型，导致生成的运动过于同质化。
**LLM 辅助的局限**：LLM 生成的运动规划缺乏结构化建模来处理多实例间复杂交互关系。

现有 CVG 框架（如 LVD、VideoDirectorGPT）虽然通过 LLM 规划边界框序列来控制运动轨迹，但忽略了运动类别的多样性。本文从"运动类别"视角切入，将复杂运动分解为三类基元并分别建模。

## 方法详解

### 整体框架

本文框架遵循 **"先规划后生成" (Planning before Generation)** 的范式，由两个级联模块组成：

1. **结构化运动推理 (Structured Motion Reasoning, SMR)**：将用户提示解析为运动图，推理出每个实例的逐帧边界框序列，形成空间-时间布局。
2. **解耦运动引导 (Disentangled Motion Guidance, DMG)**：在视频扩散模型的采样过程中，针对三类运动分别施加专用引导分支，优化注意力图来控制视频嵌入更新。

空间-时间布局的生成形式化为：

$$\{\mathcal{B}_1, \mathcal{B}_2, \dots, \mathcal{B}_F\} = \text{LLM}(\mathcal{R}; C)$$

其中 $\mathcal{R}$ 为结构化运动图，$C$ 为用户提示，$F$ 为视频帧数。

生成阶段的视频嵌入更新（以 3D U-Net 架构为例）通过梯度优化实现：

$$\mathbf{z}_{1:F}^{t-1} \leftarrow \mathbf{z}_{1:F}^{t} - \nabla \mathcal{L}$$

$$\mathcal{L} = 1 - \frac{\beta}{P} \sum (\mathbf{A} \odot (\mathcal{G}_m + \mathcal{G}_r + \mathcal{G}_{nr}))$$

其中 $\mathbf{A}$ 为注意力图，$P$ 为像素数，$\beta$ 为引导因子。$\mathcal{G}_m$、$\mathcal{G}_r$、$\mathcal{G}_{nr}$ 分别对应静止、刚性、非刚性运动的引导掩码。

对于 DiT 架构，则直接修改注意力得分：

$$\mathbf{A} = \text{Softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top (1 + \beta \odot (\mathcal{G}_m + \mathcal{G}_r + \mathcal{G}_{nr}))}{\sqrt{d}}\right)$$

### 模块一：结构化运动推理 (SMR)

SMR 模块的目标是将语义模糊的用户提示转化为结构化表示，推理出每个实例的运动规律。

**运动图构建**：将每个实例表示为图的节点，标注运动属性和运动类别标签。运动属性通过识别与实例关联的动词或谓语短语解析得到。有向边编码实例间的空间关系（如 "next to"、"on top of"）和动态交互（如 "pass by"、"move toward"）。形式化为 $\mathcal{R} = (\mathcal{V}, \mathcal{E})$。

**空间-时间布局推理**：根据运动类别分别推理边界框序列：

| 运动类型 | 布局更新规则 |
|---|---|
| 静止 | $\mathcal{B}_f(v_n) = \mathcal{B}_1(v_n)$，所有帧保持不变 |
| 刚性运动 | $\mathcal{B}_f(v_n) = \mathcal{B}_{f-1}(v_n) + \vec{u}_{v_n} + \frac{1}{2}\vec{a}_{v_n}$，基于速度和加速度做匀变速更新 |
| 非刚性运动 | $\mathcal{B}_f(v_n) = \mathcal{B}_{f-1}(v_n) + \Delta_f(v_n)$，通过边界级位移向量建模不对称形变 |

其中刚性运动的速度和加速度由滑动窗口内的历史运动和运动图中的动作线索共同预测。非刚性运动的边界位移向量 $\Delta_f(v_n)$ 则利用运动图中隐式捕获的局部形变信息推理。

### 模块二：解耦运动引导 (DMG)

DMG 模块包含三个专用引导分支，分别处理不同运动类型：

**分支 1：参考帧条件引导 (Reference Conditioned Guidance, RCG)**

针对静止实例，锚定像素特征到一个稳定的参考帧以保持跨帧外观一致性。参考帧 $f^*$ 通过最小帧间特征差异准则选取：

$$f^* = \arg\min_f \sum_{f'=1}^F D(\varphi(\mathbf{z}_f^t), \varphi(\mathbf{z}_{f'}^t))$$

引导掩码定义为：

$$\mathcal{G}_m[x,y,f,f'](v_n) = \mathbb{1}(f' = f^* \ \& \ (x,y) \in \mathcal{B}(v_n))$$

即只允许各帧与参考帧交互，抑制静态区域的闪烁伪影。

**分支 2：几何不变性引导 (Geometric Invariance Guidance, GIG)**

针对刚性运动实例，通过帧无关的形状模板约束几何一致性。具体步骤：

1. 对边界框区域做 $k$-means 聚类分离前景/背景，得到粗糙前景掩码。
2. 通过逐像素投票 (pixelwise consensus) 生成形状模板，再反向变换到每帧得到几何对齐掩码 $\mathcal{M}_f(v_n)$。
3. 利用帧间边界框中心距离计算位移惩罚因子：

$$\Gamma[f,f'] = \exp(-\alpha \cdot \|\mathbf{C}_f - \mathbf{C}_{f'}\|_2) + 1$$

最终引导掩码为：

$$\mathcal{G}_r(v_n) = \mathcal{M}(v_n) \cdot \mathcal{M}(v_n)^\top \odot \Gamma$$

**分支 3：空间形变引导 (Spatial Deformation Guidance, SDG)**

针对非刚性运动实例，最小化感知形变与边界框诱导形变之间的逐像素差异。

感知形变 $\mathcal{D}_{perc}$ 通过在扩散特征空间中做逐帧最近邻搜索获得：

$$\mathcal{N}(i,j) = \arg\min_{(i',j')} \|\varphi(\mathbf{z}_f^t)_{i,j} - \varphi(\mathbf{z}_{f'}^t)_{i',j'}\|_2$$

$$\mathcal{D}_{perc}[i,j] = \mathcal{N}(i,j) - (i,j)$$

边界框诱导形变 $\mathcal{D}_{box}$ 通过边界框四角位移 $\mathbf{d}_k$ 做双线性插值得到：

$$\mathcal{D}_{box}[i,j] = \text{Interp}(\{\mathbf{d}_k\}_{k=1}^4, (i,j))$$

形变惩罚因子和最终掩码为：

$$\Lambda[i,j] = \exp(-\alpha \cdot (\mathcal{D}_{perc}[i,j] - \mathcal{D}_{box}[i,j])) + 1$$

$$\mathcal{G}_{nr} = (\mathcal{M}(v_n) \cdot \mathcal{M}(v_n)^\top) \odot \Lambda$$

核心思想是将跨帧形变视为多对多像素对应问题，利用扩散特征空间中 RGB 层面的对应关系来正则化非刚性变形。

## 实验

### 数据集与评估指标

作者从 MSR-VTT 和 Panda-70M 中筛选真实世界视频描述，按四种语言模式（并列结构、数量词、集合名词、交互动词）分类，构建了 **CVGBench-m**（1665 样本）和 **CVGBench-p**（994 样本）两个基准。评估涵盖 Subject Consistency、Background Consistency、Temporal Flickering、Motion Smoothness、Dynamic Degree 五个维度。

### 主实验结果

| 方法 | Subject Cons. | Background Cons. | Temporal Flicker. | Motion Smooth. | Dynamic Deg. |
|------|:---:|:---:|:---:|:---:|:---:|
| VideoCrafter-v2.0 | 97.68% | 97.28% | 96.28% | 98.16% | 33.11% |
| + BoxDiff | 97.42% | 96.93% | 96.33% | 98.25% | 38.31% |
| + A&R | 97.48% | 97.05% | 96.43% | 98.27% | 38.40% |
| + Vico | 97.72% | 97.43% | 96.68% | 98.35% | 40.00% |
| **+ Ours** | **98.40%** | **98.11%** | **97.39%** | **98.63%** | **82.21%** |
| CogVideoX-2B | 91.33% | 92.78% | 95.01% | 96.88% | 87.80% |
| + R&P | 91.00% | 90.85% | 95.07% | 96.96% | 91.02% |
| **+ Ours** | **98.27%** | **97.73%** | **98.25%** | **98.74%** | **96.00%** |

Dynamic Degree 提升最为显著——VideoCrafter 基线上从 33.11% 到 82.21%（+49.1%），CogVideoX 基线上从 91.02% 到 96.00%（+4.98%），说明框架成功生成了大幅度多样化运动。

### 消融实验

**DMG 三分支消融**（CogVideoX-2B 基线，CVGBench-m）：

| RCG | GIG | SDG | Subject Cons. | Background Cons. | Dynamic Deg. |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ✗ | ✗ | ✗ | 91.00% | 90.85% | 91.02% |
| ✓ | ✗ | ✗ | 95.98% | 96.03% | 92.16% |
| ✗ | ✓ | ✗ | 96.21% | 96.07% | 92.77% |
| ✗ | ✗ | ✓ | 96.13% | 96.14% | 93.57% |
| ✓ | ✓ | ✗ | 97.19% | 96.91% | 94.56% |
| ✓ | ✓ | ✓ | **98.27%** | **97.73%** | **96.00%** |

三个分支逐步叠加带来持续增益。SDG 单独使用时 Dynamic Degree 提升最大（+2.55%），表明非刚性形变引导对大幅运动合成贡献最大。RCG 和 GIG 对跨帧一致性贡献更突出。

**SMR 模块消融**：去掉 SMR 后 Subject Consistency 从 98.27% 降至 93.16%，Dynamic Degree 从 96.00% 降至 88.21%，验证了运动图结构化推理在消除语义歧义方面的关键作用。

**LLM 规模消融**：LLaMA-70B 显著优于 LLaMA-8B，在 VideoCrafter 基线上 Dynamic Degree 从 75.34% 提升到 82.21%，说明更强的语言模型能更准确地推理逐帧形状和位置。

### 关键发现

- R&P 方法以帧独立方式解决语义泄漏，但忽略跨帧一致性，有时反而损害 Subject/Background Consistency。
- 本框架对 3D U-Net 和 DiT 两种架构均有效，具有良好的模型无关性。
- 非刚性运动引导对视频动态度的贡献最为显著（VideoCrafter 基线上 SDG 单独贡献 +27.81% Dynamic Degree）。

## 亮点

- **运动分解思想新颖**：首次将组合视频中的运动分解为静止/刚性/非刚性三类基元并分别建模，填补了现有 CVG 方法忽视运动多样性的空白。
- **无需训练**：整个框架 training-free，可即插即用到现有扩散模型架构上。
- **架构无关**：同时在 3D U-Net 和 DiT 两种主流架构上验证有效，通用性强。
- **结构化推理消除歧义**：运动图中间表示有效桥接了自然语言和空间-时间布局，显著优于直接 prompt-to-motion 方案。
- **数学建模严谨**：三个引导分支各有物理含义——RCG 保外观一致、GIG 保几何不变、SDG 保形变合理。

## 局限

- **无法处理罕见语义**：如 "Dendroid" 等稀有概念不在基线模型特征空间中，框架无法弥补底层模型的知识缺失。
- **情感线索难以建模**：生成视频缺乏清晰的面部表情来传达 "sad" 等情感，因为视频生成模型倾向于忽略提示中的形容词/副词。
- **依赖 LLM 推理质量**：运动图构建和布局推理严重依赖 LLM 能力，8B 模型效果明显差于 70B，推理成本较高。
- **运动类别固定为三类**：将所有运动归为三类可能过于粗粒度，旋转运动、弹性运动等细粒度类别未覆盖。
- **缺少相机运动建模**：当前框架不处理全局视角变化，作者自己也将其列为 future work。

## 评分

| 维度 | 评分 |
|------|:---:|
| 新颖性 | ⭐⭐⭐⭐ |
| 技术深度 | ⭐⭐⭐⭐ |
| 实验充分度 | ⭐⭐⭐⭐ |
| 写作质量 | ⭐⭐⭐⭐ |
| 实用性 | ⭐⭐⭐⭐ |
| 综合 | ⭐⭐⭐⭐ |
