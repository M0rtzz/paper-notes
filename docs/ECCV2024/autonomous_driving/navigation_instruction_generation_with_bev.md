---
title: >-
  [论文解读] Navigation Instruction Generation with BEV Perception and Large Language Models
description: >-
  [ECCV 2024][自动驾驶][Navigation Instruction Generation] 提出 BEVInstructor，将鸟瞰图 (BEV) 特征融入多模态大语言模型 (MLLM) 用于导航指令生成，通过 Perspective-BEV 视觉编码、参数高效 prompt tuning 和实例引导的迭代精化，在室内外多个数据集上全面超越 SOTA。
tags:
  - ECCV 2024
  - 自动驾驶
  - Navigation Instruction Generation
  - BEV Perception
  - 多模态
  - 提示学习
  - Iterative Refinement
---

# Navigation Instruction Generation with BEV Perception and Large Language Models

**会议**: ECCV 2024  
**arXiv**: [2407.15087](https://arxiv.org/abs/2407.15087)  
**代码**: https://github.com/FanScy/BEVInstructor (有)  
**领域**: Agent  
**关键词**: Navigation Instruction Generation, BEV Perception, Multi-Modal LLM, Prompt Tuning, Iterative Refinement

## 一句话总结

提出 BEVInstructor，将鸟瞰图 (BEV) 特征融入多模态大语言模型 (MLLM) 用于导航指令生成，通过 Perspective-BEV 视觉编码、参数高效 prompt tuning 和实例引导的迭代精化，在室内外多个数据集上全面超越 SOTA。

## 研究背景与动机

1. **领域现状**：导航指令生成要求具身智能体将导航路线描述为自然语言指令，对人机交互、盲人辅助导航和机器人协作至关重要。
2. **现有痛点**：现有方法直接将 2D 透视观察序列映射为路线描述，忽略了 3D 环境的几何信息和物体语义。通用 MLLM 在零样本设置下难以理解导航轨迹的空间上下文。
3. **核心矛盾**：导航指令需要对 3D 物理世界的全面理解（几何+语义），但现有视觉表征仅提供 2D 信息。大模型强大但无法直接适配具身导航特定需求。
4. **本文要解决什么**：将 3D 场景理解集成到 MLLM 中，生成高质量导航指令。
5. **切入角度**：引入 BEV 特征编码 3D 几何和物体语义，与透视特征融合后作为 MLLM 的视觉 prompt，通过参数高效微调适配。
6. **核心 idea 一句话**：BEV 编码 3D 几何 + 透视特征融合 + MLLM prompt tuning + 实例引导迭代精化 = 高质量导航指令。

## 方法详解

### 整体框架

BEVInstructor 处理导航轨迹的多视角图像序列：(1) Perspective-BEV Visual Encoder 融合 BEV 和透视特征；(2) Perspective-BEV Prompt Tuning 参数高效地将融合特征注入 LLaMA；(3) Instance-Guided Iterative Refinement 先生成地标 draft 再精化完整指令。

### 关键设计

1. **BEV Embedding（BEV 嵌入）**
    - **做什么**：从多视角图像中重建 3D BEV 表征。
    - **核心思路**：BEV 编码器为 BEV 平面（15×15）上每个位置的 query 分配 3D 参考点，通过可变形注意力从多视角图像特征中采样聚合。引入深度一致性权重 $w_{k,n}^c$ 区分不同深度的参考点。BEV 编码器在 3D 检测监督下训练后冻结。
    - **设计动机**：BEV 编码了 2D 透视特征无法捕获的 3D 几何结构和物体空间关系。

2. **Perspective-BEV Fusion（透视-BEV 融合）**
    - **做什么**：融合互补的 BEV 和透视特征。
    - **核心思路**：用 6 层标准 Transformer $\mathcal{F}^o$ 做 BEV→透视交叉注意力融合，再用 8 层轻量 Transformer $\mathcal{Q}$ 通过 $N_q=10$ 个可学习查询将 BEV 网格映射为固定数量 token。
    - **设计动机**：透视特征提供丰富视觉细节，BEV 特征提供 3D 几何，两者互补。直接输入所有 BEV token 会导致 MLLM 计算爆炸。

3. **Perspective-BEV Prompt Tuning（参数高效微调）**
    - **做什么**：将融合的视觉嵌入作为 prompt 注入 LLaMA 进行参数高效适配。
    - **核心思路**：$N_p$ 个可学习 prompt 嵌入与视觉嵌入拼接后注入 LLaMA 最后 $N_a=31$ 层。在自注意力部分用 zero-initialized attention 控制视觉 prompt 的影响；在线性层部分引入可学习 scale 向量。总新增参数仅占模型 7.2%。
    - **设计动机**：冻结 MLLM 主体避免灾难性遗忘，仅微调少量参数实现导航场景适配。

4. **Instance-Guided Iterative Refinement（实例引导迭代精化）**
    - **做什么**：模仿人类先构思地标再组织语言的路线描述方式。
    - **核心思路**：两阶段生成——(Stage 1) 根据轨迹视觉 prompt 生成地标 token 序列 $\mathcal{X}^I$；(Stage 2) 将地标 draft 纳入条件，生成完整指令 $\mathcal{X}$。多轮精化逐步提升质量。
    - **设计动机**：认知科学研究表明关键地标在人类路线描述中至关重要；两阶段生成分解问题降低难度。

### 损失函数 / 训练策略

- **BEV 编码器训练**：$\ell_1$ 损失 + CE 损失在 3D 检测上监督，训练后冻结
- **指令生成训练**：自回归 CE 损失 + 地标预测 CE 损失联合优化
- **优化器**：AdamW, lr=1e-4, batch=8, 20K iterations
- **训练规模**：冻结 6.68B 参数，仅训练 < 500M 参数（7.2%）
- **设备**：2x NVIDIA A40 GPU

## 实验关键数据

### 主实验

R2R Val Unseen 指令生成对比：

| 方法 | SPICE↑ | CIDEr↑ | Meteor↑ |
|------|--------|--------|---------|
| BT-speaker | 0.178 | 0.391 | 0.209 |
| CCC-speaker | 0.183 | 0.401 | 0.226 |
| Lana | 0.194 | 0.419 | 0.219 |
| **BEVInstructor** | **0.208** | **0.449** | **0.230** |

REVERIE Val Unseen：

| 方法 | SPICE↑ | CIDEr↑ | Meteor↑ |
|------|--------|--------|---------|
| Lana | 0.108 | 0.406 | 0.237 |
| **BEVInstructor** | **0.159** | **0.489** | **0.267** |

UrbanWalk 室外测试：SPICE 0.679 vs 0.566（+11.3%），Bleu-4 0.575 vs 0.450（+12.5%）

### 消融实验

R2R Val Unseen 消融：

| Perspective | BEV | Fusion | Refinement | SPICE↑ | CIDEr↑ |
|-------------|-----|--------|------------|--------|--------|
| ✔ | | | | 0.154 | 0.209 |
| | ✔ | | | 0.172 | 0.281 |
| ✔ | ✔ | | | 0.180 | 0.342 |
| ✔ | ✔ | ✔ | | 0.198 | 0.425 |
| ✔ | ✔ | ✔ | ✔ | 0.208 | 0.449 |

### 关键发现

- BEV 特征单独使用 (SPICE 0.172) 已优于透视特征 (0.154)，证明 3D 几何信息的价值
- 融合模块贡献最大提升（CIDEr +0.083），说明两种视角互补性强
- 迭代精化进一步提升 SPICE +0.010，生成的指令包含更多关键地标
- 室外场景提升最大（SPICE +11.3%），BEV 在复杂几何场景更具优势

## 亮点与洞察

- **BEV 用于指令生成的首次探索**：将自动驾驶的 BEV 感知引入室内导航指令生成
- **参数效率极高**：仅 7.2% 可训练参数即可实现全面 SOTA
- **跨域通用性**：室内 (R2R, REVERIE) 和室外 (UrbanWalk) 均有效
- **认知科学启发**：实例引导精化模拟人类描述路线的认知过程

## 局限性 / 可改进方向

- BEV 编码器需要 3D 检测数据预训练，增加了数据需求
- 15×15 的 BEV 分辨率对大场景可能不足
- 迭代精化增加推理时间
- 未与最新的视觉-语言大模型（如 GPT-4V）进行对比

## 相关工作与启发

- 将自动驾驶 BEV 感知 (BEVFormer, BEVDet) 迁移到具身导航是有趣的跨领域应用
- 与 Lana (CVPR23) 同为 MLLM 用于指令生成，但 BEV 融合是关键区别
- Prompt tuning + zero-initialized attention 的参数高效方案可推广到其他多模态适配场景
- 启发：3D 感知能力是提升 MLLM 具身应用效果的关键

## 评分

- ⭐⭐⭐⭐ 新颖性：BEV + MLLM 的组合新颖，迭代精化设计有认知科学支撑
- ⭐⭐⭐⭐⭐ 实验充分度：3 个数据集、多指标、完整消融、定性分析
- ⭐⭐⭐⭐ 写作质量：方法描述系统完整，但公式偏多
- ⭐⭐⭐⭐ 价值：为导航指令生成引入 3D 感知的新范式，跨域效果好

<!-- RELATED:START -->

## 相关论文

- [\[ECCV 2024\] H-V2X: A Large Scale Highway Dataset for BEV Perception](h-v2x_a_large_scale_highway_dataset_for_bev_perception.md)
- [\[ECCV 2024\] Optimizing Diffusion Models for Joint Trajectory Prediction and Controllable Generation](optimizing_diffusion_models_for_joint_trajectory_prediction_and_controllable_gen.md)
- [\[ECCV 2024\] Adaptive Human Trajectory Prediction via Latent Corridors](adaptive_human_trajectory_prediction_via_latent_corridors.md)
- [\[ECCV 2024\] OccGen: Generative Multi-modal 3D Occupancy Prediction for Autonomous Driving](occgen_generative_multi-modal_3d_occupancy_prediction_for_autonomous_driving.md)
- [\[ECCV 2024\] Neural Volumetric World Models for Autonomous Driving](neural_volumetric_world_models_for_autonomous_driving.md)

<!-- RELATED:END -->
