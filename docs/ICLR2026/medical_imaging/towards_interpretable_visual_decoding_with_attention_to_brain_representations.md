---
title: >-
  [论文解读] Towards Interpretable Visual Decoding with Attention to Brain Representations
description: >-
  [医学图像] 提出 NeuroAdapter，一个端到端的脑活动视觉解码框架，通过交叉注意力直接将 fMRI 信号接入潜在扩散模型，跳过中间特征空间，并通过 IBBI 可解释性框架分析各脑区对图像生成的贡献。
tags:
  - 医学图像
---

# Towards Interpretable Visual Decoding with Attention to Brain Representations

- **会议**: ICLR 2026
- **arXiv**: [2509.23566](https://arxiv.org/abs/2509.23566)
- **代码**: [GitHub](https://github.com/kriegeskorte-lab/NeuroAdapter)
- **领域**: 脑机接口 / 视觉解码 / 医学影像
- **关键词**: fMRI, Visual Decoding, Latent Diffusion, Cross-Attention, Brain-Computer Interface, Interpretability

## 一句话总结

提出 NeuroAdapter，一个端到端的脑活动视觉解码框架，通过交叉注意力直接将 fMRI 信号接入潜在扩散模型，跳过中间特征空间，并通过 IBBI 可解释性框架分析各脑区对图像生成的贡献。

## 研究背景与动机

现有的从脑活动重建视觉刺激的方法通常采用两阶段流水线：(1) 将 fMRI 映射到中间特征空间（如 CLIP/DINO 嵌入）；(2) 用这些嵌入引导生成模型重建图像。这种方法存在两个问题：

**信息瓶颈**：中间表示空间可能丢失脑活动中的信息
**可解释性差**：中间映射遮蔽了不同脑区对最终重建的贡献

作者提出直接用脑活动作为扩散模型的条件输入，既保持了重建质量，又使得脑区贡献可追溯。

## 方法详解

### 整体框架 (NeuroAdapter)

基于 IP-Adapter 架构，将预训练的 Stable Diffusion 模型通过交叉注意力机制对 fMRI 特征进行条件化：

1. **脑区分割**：使用 Schaefer 分区将皮层分为 500 个脑区/半球，选择 SNR 最高的 $p=200$ 个脑区
2. **脑区线性映射**：每个脑区 $P_i$ 通过独立投影矩阵 $w \in \mathbb{R}^{v_{max} \times f}$ 映射为 fMRI token 嵌入 $E \in \mathbb{R}^{n \times p \times f}$
3. **潜在扩散条件化**：替换 U-Net 的交叉注意力层为 IP-Adapter 风格模块，使模型直接关注 fMRI token

### 关键设计

**fMRI Token Dropout**：训练时随机丢弃脑区 token，dropout 概率 $r \sim \mathcal{U}(0,1)$，生成二值掩码 $M \in \{0,1\}^{n \times p \times 1}$，增强鲁棒性。

**Min-SNR 损失加权**：降低高 SNR（简单步）的权重，保持低 SNR（困难步）的权重，平衡扩散过程各步的训练信号。

**脑编码器选择**：推理时生成多个候选图像，用脑编码器预测候选图像的 fMRI 响应，选择与真实 fMRI 相关性最高的图像。

### IBBI 可解释性框架

**Image-Brain BI-directional 框架**提供两个互补视角：

**脑导向视图**：聚合注意力权重得到脑区贡献向量：

$$B_j^{(t)} = \frac{1}{H \sum_{\ell=1}^L q^\ell} \sum_{\ell=1}^L \sum_{h=1}^H \sum_{i=1}^{q^\ell} A_{i,j}^{(\ell,h,t)}$$

其中 $\sum_{j=1}^p B_j^{(t)} = 1$，表示各脑区在时间步 $t$ 的相对贡献。

**图像导向视图**：对给定 ROI $\mathcal{R}$，池化注意力得到空间注意力图：

$$m_{\mathcal{R}}^{(\ell,t)}(i) = \frac{1}{H} \frac{1}{|\mathcal{R}|} \sum_{h=1}^H \sum_{j \in \mathcal{R}} A_{i,j}^{(\ell,h,t)}$$

上采样到图像分辨率后得到 ROI 注意力图 $I_{\mathcal{R}}^{(t)}$，展示特定脑区在图像空间中的关注区域。

## 实验

### 数据集

| 数据集 | 描述 | 特点 |
|--------|------|------|
| NSD | 7T-fMRI, 8 受试者, 10K 图像 | 主评估数据集 |
| NSD-Imagery | 心理意象任务 | 测试泛化能力 |
| Deeprecon | 1200 训练 + 90 测试图像 | 训练/测试类别不重叠 |

### 主要结果

在 8 个图像质量指标上的评估（相对于 ImageNet 检索基线的提升）：
- **高层语义指标**（CLIP, Incep, Eff, SwAV）: 与现有方法（MindEye1, DREAM等）相当甚至超越
- **低层指标**（PixCorr, SSIM）: 略逊于带 VDVAE 路径的 Brain Diffuser，但去掉 VDVAE 后性能相当

### 解码动态分析

利用 IBBI 框架的发现：
- **高级视觉区域**（如 FFA, PPA）在扩散过程中贡献更大
- 面部 ROI 的注意力精确定位到图像中的人脸区域
- 场景 ROI 覆盖广泛背景区域
- 早期去噪步的注意力分散，后期集中到相关区域

### 因果扰动分析

- 遮蔽低级 ROI 不影响语义内容
- 遮蔽高级 ROI 完全改变生成图像

## 亮点

1. **端到端架构**：首次直接用 fMRI 条件化扩散模型，无需中间表示空间
2. **双向可解释性**：IBBI 框架同时提供脑区→图像和图像→脑区的分析视角
3. **脑区粒度条件化**：每个脑区作为独立 token，自然支持 ROI 级别的分析
4. **跨数据集泛化**：在心理意象（NSD-Imagery）和类别不重叠（Deeprecon）设置下均有效

## 局限性

1. 扩散模型的随机性导致生成图像质量变异大
2. 低层视觉特征重建不如使用 VDVAE 等专门路径的方法
3. 依赖脑编码器进行图像选择，引入额外计算开销
4. 仅在有限受试者上验证，泛化性有待进一步确认
5. 交叉注意力的可解释性仍是近似的，非严格因果分析

## 相关工作

- **两阶段解码**：Brain Diffuser (Ozcelik & VanRullen, 2023), MindEye1 (Scotti et al., 2023), DREAM (Xia et al., 2024) 通过 CLIP/DINO 嵌入引导 SD
- **单阶段解码**：DynaDiff (Careil et al., 2025) 使用 LoRA 微调处理动态 fMRI
- **编码模型可解释性**：Adeli et al. (2025) 用 Transformer 脑编码器的注意力图路由视觉特征

## 评分

- **创新性**: ⭐⭐⭐⭐ — 端到端方法和双向可解释性框架是重要贡献
- **实用性**: ⭐⭐⭐ — 脑解码仍处于研究阶段，实际应用有限
- **清晰度**: ⭐⭐⭐⭐ — 方法描述清晰，可解释性分析详细
- **意义**: ⭐⭐⭐⭐ — 为神经科学和脑解码提供了新的可解释性工具
