---
title: >-
  [论文解读] Token Warping Helps MLLMs Look from Nearby Viewpoints
description: >-
  [CVPR2026][多模态][视点变换] 探索在token级别而非像素级别进行视点变换，发现反向token warping能使MLLM可靠地从临近视点推理，效果超趇像素级warping、空间微调模型和生成式warping方法。
tags:
  - CVPR2026
  - 多模态
  - 视点变换
  - Token Warping
  - 空间推理
  - 心理意象
  - 三维理解
---

# Token Warping Helps MLLMs Look from Nearby Viewpoints

**会议**: CVPR2026  
**arXiv**: [2604.02870](https://arxiv.org/abs/2604.02870)  
**代码**: [token-warping-mllm.github.io](https://token-warping-mllm.github.io/)  
**领域**: 多模态VLM  
**关键词**: 视点变换, Token Warping, 空间推理, 心理意象, 三维理解

## 一句话总结
探索在token级别而非像素级别进行视点变换，发现反向token warping能使MLLM可靠地从临近视点推理，效果超趇像素级warping、空间微调模型和生成式warping方法。

## 研究背景与动机
MLLM在视觉推理上表现优秀，但对视点变化极其脆弱。现有解决思路均有缺陷：
- **像素级warping**：对深度误差极度敏感，产生严重几何畸变和语义退化
- **3D感知微调**(SpatialReasoner, VLM-3R)：特定训练后改善有限
- **生成式方法**：使用扩散模型合成目标视点图像，但可能引入幻觉

关键洞察：认知科学中的心理意象理论指出，人类视角变换依赖部件级结构描述而非像素级的精确重建。ViT的image token正好在这个粒度上——比物体级更细致，比像素级更鲁棒。

## 方法详解

### 整体框架
给定源视点图像+深度+相机参数+目标位姿，将token warping而非像素宣渲应用于视点变换，然后用warped token回答关于目标视点的问题。

### 关键设计

1. **Token对位置扰动的鲁棒性验证**：
   - 将每个patch的中心位置添加高斯扰动，模拟 warping引入的位置误差
   - 发现MLLM对位置扰动极其鲁棒，即使偏移接近patch大小仍能保持识别能力
   - 相比之下，像素级基线在相同扰动下大幅退化

2. **前向vs反向Token Warping**：
   - **前向warping**：将源视点token投影到目标视点 → 产生不规则、稀疏的token分布，这是MLLM的分布外输入
   - **反向warping**：在目标视点定义密集规则网格，向源图像检索对应token → 保持整齐的网格分布，性能更优

3. **获取策略**：
   - **最近获取**：先计算所有源视点token，然后为每个目标位置分配最近的预计算token
   - **自适应获取**：直接在映射位置重新切片patch，精度更高但计算量更大

### 损失函数 / 训练策略
完全免训练，仅需推理时的轻量级warping计算。

## 实验关键数据

### 主实验
| 方法 | ViewBench-Text(5-15%) | ViewBench-Shape(5-15%) | 说明 |
|------|---------------------|----------------------|------|
| SpatialReasoner | 46.73 | 33.72 | 空间微调专用模型 |
| VLM-3R | 63.82 | 49.22 | 3D感知特征 |
| Backward Token Warping | 最优 | 最优 | 免训练方法 |

### 消融实验
| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 前向 vs 反向warping | 反向显著更优 | 规则网格很关键 |
| 最近获取 vs 自适应获取 | 自适应略优 | 但最近获取已很强 |
| 像素warping vs token warping | token显著更优 | 核心发现 |
| GT深度 vs 预测深度 | 差距小 | token warping对深度噪声鲁棒 |

### 关键发现
- 反向token warping超趇所有基线，包括专门进行空间微调的模型
- 比像素warping超趇扩散生成方法，且计算量微小
- MLLM对token位置扰动的鲁棒性是意外的发现
- 使用预测深度vs GT深度的差距较小，实用性强

## 亮点与洞察
- 从认知科学角度切入，将mental imagery理论与ViT的patch token联系起来，角度新颖
- 实验设计巧妙：position noise sensitivity test提供了有力的理论支撑
- 反向warping保持目标视点的规则网格这一点至关重要——MLLM训练时只见过密集规则的token网格
- 完全免训练，可直接应用于任何ViT-based MLLM

## 局限性 / 可改进方向
- 限于临近视点，大角度视点变化会导致大量遮挡和可见性变化
- 依赖深度估计，对无深度的场景不可用
- ViewBench基准较新，规模和多样性可进一步扩展
- 声明了多视点场景的潜力但未实验探索

## 相关工作与启发
- COMFORT发现MLLM无法采纳他人视角，本文给出了新解决思路
- SpatialReasoner和VLM-3R通过训练解决，本文用免训练的warping达到更好效果
- 对embodied AI的视觉感知有直接应用价值

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 从mental imagery角度切入token warping，视角独特
- 实验充分度: ⭐⭐⭐⭐ 多维度对比+新基准+鲁棒性测试
- 写作质量: ⭐⭐⭐⭐⭐ 从动机到实验的叙事流畅自然
- 价值: ⭐⭐⭐⭐ 免训练+轻量级，对视点感知研究有重要参考

## 补充说明
- ViewBench包含三类任务：Text（位置关系描述）、Shape（形状描述）、Object（物体属性）
- View Overlap指源视图和目标视图的重叠比例，分5-15%/15-25%/25-35%三档
- 实验主要基于Qwen2.5-VL进行，同时比较了SpatialReasoner、VLM-3R、ViLaSR等专用模型
- 深度图使用Depth Anything V2预测，也对比了GT深度
- 反向warping通过从深度图构建3D代理网格并进行射线投射来实现
- 最大位移值在20像素级别时token表示仍稳定，超过19像素才出现可见性能下降
