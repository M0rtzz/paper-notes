---
description: "【论文笔记】QuadGPT: Native Quadrilateral Mesh Generation with Autoregressive Models 论文解读 | ICLR 2026 | arXiv 2509.21420 | 四边形网格 | 提出QuadGPT——首个端到端自回归生成原生四边形网格的框架：设计统一tokenization处理三角形/四边形混合拓扑(三角形面用padding统一为四顶点)，采用Hourglass Transformer压缩面序列+截断序列训练支持高面数网格，引入tDPO(截断DPO)强化学习微调奖励结构化边环形成，在几何精度和拓扑质量上显著超越三角形→四边形转换流水线。"
tags:
  - ICLR 2026
---

# QuadGPT: Native Quadrilateral Mesh Generation with Autoregressive Models

**会议**: ICLR 2026  
**arXiv**: [2509.21420](https://arxiv.org/abs/2509.21420)  
**代码**: 无  
**领域**: 3D生成/网格生成  
**关键词**: 四边形网格, 自回归生成, 混合拓扑, 强化学习微调, 端到端

## 一句话总结

提出QuadGPT——首个端到端自回归生成原生四边形网格的框架：设计统一tokenization处理三角形/四边形混合拓扑(三角形面用padding统一为四顶点)，采用Hourglass Transformer压缩面序列+截断序列训练支持高面数网格，引入tDPO(截断DPO)强化学习微调奖励结构化边环形成，在几何精度和拓扑质量上显著超越三角形→四边形转换流水线。

## 研究背景与动机

1. **领域现状**：四边形网格是3D内容创建的行业标准(游戏/影视)→确保建模效率/变形稳定性/动画就绪。现有生成方法→自回归仅生成三角形网格→通过后处理合并为四边形→拓扑差。

2. **现有痛点**：
   - (1) 等值面提取(Marching Cubes)→密集无结构三角形→不适合生产
   - (2) 十字场引导(cross-field)→需要干净输入+多阶段pipeline→不鲁棒
   - (3) 自回归三角形(MeshAnything/BPT/Mesh-RFT)→拓扑好但只能三角形
   - (4) 三角形→四边形转换→破坏自然边流(edge flow)+引入伪影

3. **切入角度**：直接生成四边形→不经过三角形中间步→端到端学习。

## 方法详解

### 统一混合拓扑tokenization

- 专业网格通常是四边形为主+少量三角形
- 三角形面：3顶点→padding一个重复顶点→统一为4顶点表示
- 面序列：顺序排列所有面→每面4个顶点坐标

### Hourglass Transformer

- 面序列→先压缩面级信息→再压缩顶点级信息
- 分层架构→处理长序列(高多边形网格)
- 截断序列训练→支持分段训练→高面数可行

### tDPO (截断直接偏好优化)

- 标准DPO→在完整序列上比较偏好对
- 问题：网格序列很长→完整序列DPO不可行
- tDPO：在截断序列上做DPO→专门评估和比较截断片段
- 奖励：边环(edge loop)形成质量→四边形网格的关键拓扑特征
- 结构化edge flow→专业资产的标志

## 实验关键数据

### Toys4K数据集

| 方法 | 几何精度(CD↓) | 拓扑质量 | 四边形比例 |
|------|-------------|---------|----------|
| MeshAnything+转换 | 中 | 差(破碎) | ~70% |
| BPT+转换 | 中 | 差(伪影) | ~75% |
| TriGPT+转换 | 较好 | 中 | ~80% |
| **QuadGPT** | **最好** | **最好** | **~95%** |

### Hunyuan3D dense mesh

- 硬表面(道具)和软表面(角色)都表现好
- 生产级质量→具有干净边流

### 关键发现

- 原生四边形 >> 三角形转换→拓扑质量差距巨大(Figure 2)
- tDPO的边环奖励→+15%拓扑质量提升→RL对网格质量很重要
- Hourglass压缩→比flat Transformer效率高3x→使高面数可行
- 截断训练→1万面网格的训练成为可能

## 亮点与洞察

- **"首个原生四边形网格生成"**：之前所有自回归方法=三角形→QuadGPT填补了关键gap→桥接生成AI和工业需求。
- **padding统一三角形/四边形**：看似简单→但巧妙解决了混合拓扑的序列化问题→使统一的自回归框架成为可能。
- **tDPO的网格质量奖励**：DPO通常用于语言/图像→这里用于网格拓扑→跨域RL application。
- **从数字到生产**：QuadGPT生成的网格→可直接用于游戏制作→不需要专业3D艺术家retopologize。


## 局限性 / 可改进方向

- We present QuadGPT, the first autoregressive framework that directly generates native quadrilateral and mixed-element meshes.

- It achieves state-of-the-art results in generative meshing, setting a new standard for both geometric fidelity and topological quality.

- Our scalable, neural-first approach departs from previous triangle-based methods and conversion pipelines, which rely on heuristic post-processing to approximate quad topology.

- By leveraging a unified serialization scheme and a novel topology-aware fine-tuning stage (tDPO), QuadGPT directly optimizes for global structure, making it well-suited for the automated creation of production-ready 3D assets.

- 6 Ethics Statement

This work introduces QuadGPT, an autoregressive framework for direct generation of production-ready, quad-dominant meshes.


## 相关工作与启发

- **vs Marching Cubes**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs MeshGPT**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐ 首个原生四边形自回归生成+tDPO网格RL
- 实验充分度: ⭐⭐⭐⭐ Toys4K+Hunyuan3D+详细对比
- 写作质量: ⭐⭐⭐⭐ 工业动机清晰
- 价值: ⭐⭐⭐⭐⭐ 对3D内容创建pipeline有直接工业影响
