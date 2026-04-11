---
description: "【论文笔记】Universal Retrieval for Multimodal Trajectory Modeling 论文解读 | ICML2025 | arXiv 2506.22056 | trajectory retrieval | 首次提出多模态轨迹检索（Multimodal Trajectory Retrieval）任务，构建统一代理轨迹数据集 UATD 和 GAE-Bench 基准，并提出基于 VLM 的 GAE-Retriever 框架，在轨迹级检索上显著优于基线。"
tags:
  - ICML2025
  - 多模态
  - 对比学习
---

# Universal Retrieval for Multimodal Trajectory Modeling

**会议**: ICML2025  
**arXiv**: [2506.22056](https://arxiv.org/abs/2506.22056)  
**代码**: 待确认  
**领域**: multimodal_vlm  
**关键词**: trajectory retrieval, GUI agents, multimodal embedding, contrastive learning, VLM

## 一句话总结
首次提出多模态轨迹检索（Multimodal Trajectory Retrieval）任务，构建统一代理轨迹数据集 UATD 和 GAE-Bench 基准，并提出基于 VLM 的 GAE-Retriever 框架，在轨迹级检索上显著优于基线。

## 研究背景与动机
- 轨迹数据（人机交互中的状态-动作序列）在 GUI agent、数据回放、策略学习中价值巨大
- 现有方法仅用文本特征做相似性搜索，忽略了多模态信号（截图、UI布局等）
- **核心问题**：如何系统地建模和检索多模态轨迹数据？缺乏统一格式、标准基准和专门的检索模型
- 轨迹数据天然具有时序关系（temporal）和语义关系（semantic），需同时建模这两类关联

## 方法详解

### 1. 统一代理轨迹数据集 UATD
- 整合 5 个开源 GUI agent 数据源：Mind2Web、AutoWebGLM、WebArena、WebLINX、GUIAct
- 统一轨迹表示：$\tau = (s_1, a_1, s_2, a_2, \ldots, s_n, a_n)$，状态用截图 + 文本描述，动作用操作/目标/值三元组
- 总计 7,747 个人工标注演示、82,793 个状态

### 2. GAE-Bench 基准
- 定义 6 类 12 个子任务的检索对：
  - 文本→轨迹、文本→状态、轨迹→轨迹、轨迹→状态、状态→轨迹、状态→状态
- 时序检索：给前半段，检索后半段（及其逆）
- 语义检索：给指令，检索语义相似轨迹（silver trajectory）
- 总计 714,628 个正样本对
- GAE-Bench-lite：限制轨迹长度 ≤10 步，含 514,956 训练样本

### 3. GAE-Retriever
- 基于 VLM2Vec + Qwen2-VL backbone
- **Token Selection**：从多截图轨迹中选择关键 token 减少计算
- **GradCache**：梯度缓存机制支持大 batch 对比学习（有限 GPU 内存下处理高分辨率轨迹截图）
- 对比学习目标：InfoNCE loss，in-batch 负采样

### 损失函数
$$\mathcal{L} = -\log \frac{\exp(\text{sim}(q, d^+)/\tau)}{\sum_{j}\exp(\text{sim}(q, d_j)/\tau)}$$

## 实验关键数据

| 模型类型 | 平均 Recall@1 | 平均 Recall@5 | 平均 Recall@10 |
|----------|-------------|-------------|--------------|
| CLIP-based | 低 | 低 | 低 |
| VLM backbone | 中等 | 中等 | 中等 |
| GAE-Retriever | **最优** | **最优** | **最优** |

- GAE-Retriever 相比最佳基线平均提升 10.22 个百分点
- 跨 5 个数据源一致优于多模态 backbone 模型、通用检索模型和轨迹规划模型
- 在 OOD（跨数据源）设置下仍保持优势

## 亮点与洞察
- **开创性任务定义**：首次系统定义多模态轨迹检索，建立完整的数据-基准-方法体系
- **12种提取模式全面**：覆盖时序+语义、不同粒度（状态/轨迹/子轨迹）的检索关系
- **VLM > CLIP**：VLM 在处理任意长度多模态输入上天然优于 CLIP-based 模型
- **实用价值高**：可直接支持 in-context learning、世界模型、轨迹回放等下游应用
- Token selection 机制有效平衡了高分辨率截图处理与计算效率

## 局限性 / 可改进方向
- 仅在 GUI 环境验证，embodied/机器人场景的轨迹检索待探索
- 依赖预训练 VLM 的视觉理解能力，对 GUI 之外的视觉观察可能需要适配
- Silver trajectory 的自动生成质量影响语义检索基准的准确性
- GAE-Bench-lite 的轨迹长度限制（≤10步）可能不代表更长轨迹场景
- 检索结果如何集成到下游 agent 决策系统中尚未深入探讨
- 对非英语 GUI 和移动端场景的泛化能力未验证
- 对比学习的温度参数 τ 和 batch size 对结果影响的消融有限

## 相关工作与启发
- **VLM2Vec**（Jiang et al., 2025）：VLM 用于通用检索的 backbone
- **Mind2Web**（Deng et al., 2023）：Web 导航基准
- **AGUVIS**（Xu et al., 2024）：统一 GUI 视觉表示
- **ShowUI**（Lin et al., 2024）：统一动作空间定义
- 启发：将"轨迹"作为一等公民进行表示学习是 agent 智能的重要基础设施

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ (开创性任务定义+完整体系)
- 实验充分度: ⭐⭐⭐⭐ (5 个数据源+多基线对比)
- 写作质量: ⭐⭐⭐⭐ (结构化清晰，数据集描述详尽)
- 价值: ⭐⭐⭐⭐⭐ (为 agent trajectory 研究奠定基础设施)

## 评分
- 新颖性: 待评
- 实验充分度: 待评
- 写作质量: 待评
- 价值: 待评
