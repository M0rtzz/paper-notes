---
title: >-
  [论文解读] Traffic Scene Generation from Natural Language Description for Autonomous Vehicles with Large Language Model
description: >-
  [CVPR 2026][自动驾驶][文本到交通场景生成] 提出 TTSG 模块化框架，利用 LLM 将自由文本描述转化为可执行的交通场景，通过提示分析、道路检索、智能体规划和新颖的计划感知道路排名算法生成多样化场景，在 SafeBench 上实现最低平均碰撞率 3.5%。
tags:
  - CVPR 2026
  - 自动驾驶
  - 文本到交通场景生成
  - 大语言模型
  - 安全场景
  - 道路排名
---

# Traffic Scene Generation from Natural Language Description for Autonomous Vehicles with Large Language Model

**会议**: CVPR 2026  
**arXiv**: [2409.09575](https://arxiv.org/abs/2409.09575)  
**代码**: [https://basiclab.github.io/TTSG](https://basiclab.github.io/TTSG)  
**领域**: 自动驾驶 / 场景生成  
**关键词**: 文本到交通场景生成, 大语言模型, 自动驾驶, 安全场景, 道路排名

## 一句话总结

提出 TTSG 模块化框架，利用 LLM 将自由文本描述转化为可执行的交通场景，通过提示分析、道路检索、智能体规划和新颖的计划感知道路排名算法生成多样化场景，在 SafeBench 上实现最低平均碰撞率 3.5%。

## 研究背景与动机

1. **领域现状**：交通场景数据集（nuScenes、Waymo）提供了丰富的驾驶日志，但受限于安全和可控性。CARLA 和 MetaDrive 等模拟器虽可定制场景，但依赖随机采样或轨迹回放。
2. **现有痛点**：LCTGen、ChatScene 等方法要么需要结构化输入无法处理自由文本，要么需要用户手动指定出生点和地图位置，且忽略了环境条件（信号灯、天气等）。
3. **核心矛盾**：如何从非结构化自然语言直接生成空间有效、语义连贯的交通布局，同时不依赖预定义路线或出生点。
4. **本文目标**：无训练的模块化框架，直接从自然语言生成现实交通场景。
5. **切入角度**：将 LLM 用作受控管道中的通用规划器，而非端到端生成器。
6. **核心 idea**：计划感知道路排名算法确保智能体动作与道路几何的一致性。

## 方法详解

### 整体框架

五阶段管道：(1) 提示分析：LLM 解析用户输入为结构化元素；(2) 道路检索：从预建图中检索候选道路；(3) 智能体规划：LLM 规划多智能体行为；(4) 道路排名：评估道路与智能体计划的兼容性；(5) 场景生成：渲染为可执行交通场景。

### 关键设计

1. **道路图构建与智能体集**:

    - 功能：编码道路网络信息以支持自动出生点选择
    - 核心思路：将 CARLA 地图转为 OpenDRIVE 格式，解析信号灯、静态物体、交叉口、车道配置等特征，组织为图结构。智能体集支持9种类型。
    - 设计动机：图结构支持高效查询道路连接关系，实现无需预定义几何的灵活场景生成。

2. **计划感知道路排名算法**:

    - 功能：从候选道路中选择最适合智能体计划的道路
    - 核心思路：对每条候选道路，检查其是否满足每个智能体的条件（转向权限、道路类型、长度等），用指示函数累加得分：$r^* = \arg\max_{r \in R_c} \sum_{a \in A} \mathbf{1}_{\{\text{match}(r,a)\}}$。同分时随机选择以保证多样性。
    - 设计动机：先前方法随机选路忽略了转向权限和出生点充足性等关键因素。

3. **提示分析与序列事件支持**:

    - 功能：将自由文本分解为结构化组件并支持多阶段场景
    - 核心思路：LLM 将输入分解为所需信号、物体和智能体配置。支持序列事件通过迭代规划——前一事件的最终位置作为后续事件的起始点。
    - 设计动机：替代 CoT 方法以显著减少 token 使用量同时保持可比的规划质量。

### 损失函数 / 训练策略

无训练框架，使用 GPT-4o 作为默认 LLM。每阶段后有格式验证，不合格时重新提交。

## 实验关键数据

### 主实验

| 场景 | 指标 | TTSG | ChatScene (之前SOTA) | 提升 |
|------|------|------|---------------------|------|
| 直行障碍 | 碰撞率↓ | 0.021 | 0.030 | -0.009 |
| 变道 | 碰撞率↓ | 0.085 | 0.110 | -0.025 |
| 无保护左转 | 碰撞率↓ | 0.000 | 0.100 | -0.100 |
| 平均 | 碰撞率↓ | 0.035 | 0.080 | -0.045 |

### 消融实验

| 配置 | Agent Acc | Road Acc | 说明 |
|------|-----------|----------|------|
| w/ analysis+CoT | 0.975 | 0.940 | 最优但 token 多 |
| w/ analysis (默认) | 0.925 | 0.875 | 性能可比，token 少 |
| w/o analysis | 0.833 | 0.775 | 显著下降 |
| w/ road ranking | SA=0.800 | - | 场景准确率提升 |
| w/o road ranking | SA=0.560 | - | 下降明显 |

### 关键发现

- 道路排名策略将场景准确率从 56% 提升到 80%
- 驾驶描述模型训练后 CIDEr 指标提升超 30 分
- 开源模型 Gemma3-12B 也能有效支持框架

## 亮点与洞察

- **无训练设计**：整个管道不需要任何模型训练，仅依赖 LLM 的推理能力
- **排名策略简洁有效**：用简单的指示函数匹配替代复杂的优化过程
- **跨 LLM 泛化**：框架在多种开源和闭源 LLM 上都表现稳定

## 局限与展望

- 涉及精确时机控制的场景（如行人突然冲出）准确率较低
- 目前限于 CARLA 模拟器，未扩展到其他平台
- 未来计划扩展到全新交通物体的生成

## 相关工作与启发

- **vs ChatScene**: ChatScene 需手动指定出生点，TTSG 自动选择；TTSG 还支持环境条件和序列事件
- **vs LCTGen**: LCTGen 需结构化输入，TTSG 处理自由文本

## 评分

- 新颖性: ⭐⭐⭐⭐ 计划感知道路排名是新颖贡献
- 实验充分度: ⭐⭐⭐⭐ SafeBench 验证+多 LLM 泛化+消融全面
- 写作质量: ⭐⭐⭐⭐ 结构清晰，图示丰富
- 价值: ⭐⭐⭐⭐ 实用价值高，可直接用于自动驾驶系统测试

<!-- RELATED:START -->

## 相关论文

- [\[CVPR 2026\] Learning Vision-Language-Action World Models for Autonomous Driving](vla_world_learning_vision_language_action_world_models_for_autonomous_driving.md)
- [\[CVPR 2026\] NoRD: A Data-Efficient Vision-Language-Action Model that Drives without Reasoning](nord_a_data-efficient_vision-language-action_model_that_drives_without_reasoning.md)
- [\[CVPR 2026\] Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving](drive_my_way_preference_alignment_of_vision-language-action_model_for_personaliz.md)
- [\[CVPR 2026\] SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](searchad_large-scale_rare_image_retrieval_dataset_for_autonomous_driving.md)
- [\[CVPR 2026\] MeanFuser: Fast One-Step Multi-Modal Trajectory Generation and Adaptive Reconstruction via MeanFlow for End-to-End Autonomous Driving](meanfuser_fast_one-step_multi-modal_trajectory_generation_and_adaptive_reconstru.md)

<!-- RELATED:END -->
