---
title: >-
  [论文解读] Learning Trimodal Relation for Audio-Visual Question Answering with Missing Modality
description: >-
  [ECCV 2024][图像生成][音视觉问答] 提出面向音视觉问答（AVQA）的缺失模态处理框架，通过Relation-aware Missing Modal生成器利用三模态关系召回缺失信息，再通过Audio-Visual Relation-aware扩散模型增强特征表示，即使缺少一个模态也能准确回答问题。
tags:
  - ECCV 2024
  - 图像生成
  - 音视觉问答
  - 缺失模态
  - 扩散模型
  - 三模态关系
  - 伪特征生成
---

# Learning Trimodal Relation for Audio-Visual Question Answering with Missing Modality

**会议**: ECCV 2024  
**arXiv**: [2407.16171](https://arxiv.org/abs/2407.16171)  
**代码**: [https://github.com/VisualAIKHU/Missing-AVQA](https://github.com/VisualAIKHU/Missing-AVQA)  
**领域**: 图像生成  
**关键词**: 音视觉问答, 缺失模态, 扩散模型, 三模态关系, 伪特征生成

## 一句话总结
提出面向音视觉问答（AVQA）的缺失模态处理框架，通过Relation-aware Missing Modal生成器利用三模态关系召回缺失信息，再通过Audio-Visual Relation-aware扩散模型增强特征表示，即使缺少一个模态也能准确回答问题。

## 研究背景与动机
1. **领域现状**：AVQA任务需要整合视觉、音频和文本三种模态来回答问题。MUSIC-AVQA、PSTP-Net等方法在完整输入下取得了不错效果。
2. **现有痛点**：(1) 现有AVQA方法完全依赖输入模态的完整性，设备故障或数据传输错误导致某一模态缺失时性能急剧下降；(2) 现有的缺失模态处理方法主要处理一对一的模态对，忽略了不同模态间的相互依赖关系；(3) AVQA需要根据问题上下文灵活生成缺失模态的伪特征，现有方法做不到。
3. **核心矛盾**：AVQA需要视听推理跨多种上下文回答问题，但缺失模态的恢复不能仅靠单一模态——需要理解三模态关联并根据问题语境灵活应对。
4. **本文要解决什么？** (1) 利用现有两种模态的关系来召回第三种缺失模态；(2) 增强伪特征与真实特征的质量；(3) 使现有AVQA网络在缺失模态下仍能准确作答。
5. **切入角度**：模拟人类认知心理学中的音视觉整合能力——看到钢琴画面可以回忆其声音，听到钢琴声可以想象其画面。
6. **核心idea一句话**：用三模态关系驱动的slot-based生成器召回缺失模态伪特征，再用音视觉关系感知的扩散模型增强特征质量。

## 方法详解

### 整体框架
框架包含三个组件：(1) RMM生成器——利用两种可用模态的关系生成缺失模态的伪特征；(2) AVR扩散模型——将伪特征与真实特征联合增强；(3) AVQA骨干网络——使用增强后的特征回答问题。训练时同时考虑音频缺失和视觉缺失两种场景。

### 关键设计

1. **Relation-aware Missing Modal (RMM) 生成器**：
    - 做什么：利用两种可用模态关联，为缺失模态生成伪特征
    - 核心思路：每种模态有 $L$ 个可学习slot向量 $\textbf{G}^v, \textbf{G}^a, \textbf{G}^t$。以音频缺失为例，计算视觉addressing vector $a^v_i$ 和文本addressing vector $a^t_i$，通过元素乘+softmax得到联合addressing vector $a^{vt}_i = \text{softmax}(a^v_i \circ a^t_i)$，最后加权聚合音频slot：$f^{a_p}_i = \sum_j a^{vt}_{ij} \cdot \textbf{G}^a_j$
    - 设计动机：slot-based设计允许灵活的关联学习；三模态addressing捕捉视觉-文本的联合关系来定位最相关的音频slot，比单模态关联更精准

2. **RMMR损失（Relation-aware Missing Modal Recalling Loss）**：
    - 做什么：引导伪特征逼近真实特征
    - 核心思路：$\mathcal{L}_{rmmr} = \mathcal{L}_a + \mathcal{L}_v = \frac{1}{N}\sum \|f^a - f^{a_p}\|^2_2 + \frac{1}{N}\sum \|f^v - f^{v_p}\|^2_2$
    - 设计动机：确保RMM生成器在推理时输出有语义的伪特征

3. **Audio-Visual Relation-aware (AVR) 扩散模型**：
    - 做什么：通过扩散过程联合增强音频和视觉特征的表示
    - 核心思路：将音频和视觉特征拼接为 $f^{av}$，进行DDPM前向（加噪）和反向（去噪）过程。训练时用真实特征学习增强能力，推理时将伪特征+真实特征送入获得增强representation
    - 设计动机：扩散过程中两种模态特征自然交互，利用互补信息相互增强；且反向过程可以"修复"伪特征中的噪声

4. **AVE损失（Audio-Visual Enhancing Loss）**：
    - 做什么：训练扩散模型的标准去噪目标
    - 核心思路：$\mathcal{L}_{ave} = \mathbb{E}_{\epsilon \sim \mathcal{N}(0,I)}[\|\hat{\epsilon}_\theta(f^{av}_t, t) - \epsilon\|^2_2]$

### 损失函数 / 训练策略
总损失 $\mathcal{L}_{Total} = \mathcal{L}_{avqa} + \lambda_1 \mathcal{L}_{rmmr} + \lambda_2 \mathcal{L}_{ave}$，其中 $\lambda_1 = \lambda_2 = 1$。$\mathcal{L}_{avqa}$ 包含三个交叉熵项（完整输入、音频缺失、视觉缺失）。扩散模型默认10个时间步。训练在单卡RTX 4090上完成。

## 实验关键数据

### 主实验

| 方法 | 场景 | Audio Q. Avg | Visual Q. Avg | AV Q. Avg | All Avg |
|------|------|-------------|--------------|-----------|---------|
| AVST | 视觉缺失 | 65.56 | 56.45 | 58.38 | 59.14 |
| AVST+**Ours** | 视觉缺失 | **74.18** | **68.04** | **65.99** | **67.98** |
| AVST | 音频缺失 | 38.76 | 31.27 | 38.44 | 36.60 |
| AVST+**Ours** | 音频缺失 | **74.30** | **73.49** | **66.44** | **69.71** |

### 消融实验

| 配置 | All Avg (音频缺失) | 说明 |
|------|-------------------|------|
| 仅AVQA backbone | 36.60 | 无缺失处理 |
| + RMM生成器 | 63.12 | 伪特征召回有效 |
| + RMM + AVR扩散 | 69.71 | 扩散增强进一步提升 |
| RMM w/o trimodal | 58.45 | 单模态关联不如三模态 |

### 关键发现
- 音频缺失比视觉缺失对AVQA的影响更大（36.60 vs 59.14），本方法在音频缺失场景下提升最为显著（+33.11%）
- 方法可以无缝集成到多种现有AVQA网络（AVSD、Pano-AVQA、AVST、PSTP-Net），具有良好的通用性
- 三模态关联驱动的伪特征生成显著优于一对一的伪特征方法（如ActionMAE、ShaSpec）
- AVR扩散模型不仅增强伪特征，也增强了真实特征的表示
- 在AVQA和MUSIC-AVQA两个数据集上均表现最佳

## 亮点与洞察
- **三模态关联的slot-based设计非常优雅**：通过视觉和文本的addressing vector的元素乘来定位音频slot，自然地捕捉了"问题引导的跨模态关联"，比简单concat或attention更有效。
- **扩散模型用于特征增强而非生成**：将扩散模型从图像生成迁移到特征空间的增强是一个有趣的应用。拼接两种模态特征后做扩散-去噪，让互补信息自然交互。
- **实验设计周到**：同时考虑音频缺失和视觉缺失，且验证了在4种不同AVQA架构上的通用性，增强了结果可信度。

## 局限性 / 可改进方向
- 假设同一时间只有一种模态缺失，未处理音视觉同时缺失的极端情况
- 扩散模型的时间步数（10步）增加了推理延迟
- RMM生成器的slot数量L=75是超参数，对不同数据集可能需要调整
- 未与prompt-based或adapter-based方法对比

## 相关工作与启发
- **vs ActionMAE**：ActionMAE仅通过掩码自编码器生成单一模态的伪特征，未考虑交叉模态依赖。本文通过三模态关联和扩散增强远超其效果。
- **vs ShaSpec**：ShaSpec提取共享和模态特定特征但不能根据问题上下文灵活生成。本文的addressing机制实现了问题感知的缺失召回。
- **vs 知识蒸馏方法**：需要教师-学生训练，限制了灵活性。本文的方法端到端训练且无需额外教师模型。

## 补充说明
- 在AVQA数据集上的评估覆盖了9种问题类型（Used/When/Before等）
- 三种模态生成器共享权重，训练时同时覆盖音频和视觉缺失场景
- 扩散模型时间步T=10，在推理效率和特征增强效果间取得平衡
- 方法也适用于其他多模态缺失场景（如自动驾驶的LiDAR/Camera缺失）

## 评分
- 新颖性: ⭐⭐⭐⭐ 三模态关联驱动的缺失模态处理+扩散增强是新颖组合
- 实验充分度: ⭐⭐⭐⭐ 两个数据集、四种骨干、完整消融、与多种方法对比
- 写作质量: ⭐⭐⭐⭐ 条理清晰，认知心理学类比易于理解
- 价值: ⭐⭐⭐⭐ 对多模态系统的鲁棒性有重要意义

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Mutual Learning for Acoustic Matching and Dereverberation via Visual Scene-driven Diffusion](mutual_learning_for_acoustic_matching_and_dereverberation_via_visual_scene-drive.md)
- [\[ECCV 2024\] WebRPG: Automatic Web Rendering Parameters Generation for Visual Presentation](webrpg_automatic_web_rendering_parameters_generation_for_visual_presentation.md)
- [\[ECCV 2024\] Learning Differentially Private Diffusion Models via Stochastic Adversarial Distillation](learning_differentially_private_diffusion_models_via_stochastic_adversarial_dist.md)
- [\[ECCV 2024\] Powerful and Flexible: Personalized Text-to-Image Generation via Reinforcement Learning](powerful_and_flexible_personalized_text-to-image_generation_via_reinforcement_le.md)
- [\[ECCV 2024\] Ponymation: Learning Articulated 3D Animal Motions from Unlabeled Online Videos](ponymation_learning_articulated_3d_animal_motions_from_unlabeled_online_videos.md)

</div>

<!-- RELATED:END -->
