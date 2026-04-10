# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

**会议**: CVPR2026  
**arXiv**: [2512.14698](https://arxiv.org/abs/2512.14698)  
**代码**: [timelens-arc-lab.github.io](https://timelens-arc-lab.github.io/)  
**领域**: 多模态VLM  
**关键词**: 视频时间定位, 数据质量, 强化学习, RLVR, 基准修复

## 一句话总结
系统调查构建MLLM视频时间定位(VTG)能力的关键因素，揭示现有基准严重的质量问题，提出TimeLens-Bench和TimeLens-100K高质量数据，并通过thinking-free RLVR训练策略在开源模型中达到超越GPT-5的性能。

## 研究背景与动机
MLLM的"when"理解能力远落后于"what"。VTG是建立MLLM时间感知的关键任务，但存在两个核心问题：

1. **数据质量问题**：现有VTG基准（Charades-STA、ActivityNet、QVHighlights）存在大量错误：多次出现的事件、不存在的事件、重复查询、模糊查询、不准确的时间标注
2. **算法设计空白**：现有VTG研究在时间戳编码、训练策略等设计空间缺乏统一的最佳实践

关键发现：在修复基准后模型排名发生剧烈变化，证明之前的评估标准不可靠。

## 方法详解

### 整体框架
沿两个维度展开：数据质量（基准诊断→修复→可靠评估）+ 算法设计（时间编码→训练策略→优化方法）。

### 关键设计

1. **TimeLens-Bench（基准修复）**：
   - 定义严格的标注标准：查询清晰性、事件存在性、查询唯一性、避免信息泄漏、标注精确性、标注完整性
   - diagnose-then-refine工作流：同一标注员检测错误并修正
   - 交叉验证质量控制

2. **TimeLens-100K（训练数据）**：
   - 自动化重标注流程产生大规模高质量训练数据

3. **算法设计发现**：
   - 时间表示：交错文本编码(interleaved textual encoding)优于更复杂的替代方案
   - 训练范式：VTG本质是感知任务，纯thinking-free RLVR效果最佳（不需要CoT）
   - RLVR训练诀窍：(1)奖励平台期早停(early stopping) + (2)基于难度的数据采样

### 损失函数 / 训练策略
RLVR训练，奖励基于时间段IoU的可验证奖励。不使用Chain-of-Thought。

## 实验关键数据

### 主实验
| 模型 | Charades-TimeLens mIoU | ActivityNet-TimeLens mIoU | QVHighlights-TimeLens mIoU |
|------|---------------------|-------------------------|---------------------------|
| GPT-5 | 40.5 | 42.9 | 56.8 |
| Gemini-2.5-Pro | 52.8 | 58.1 | 70.4 |
| TimeLens-7B | 竞争性 | 竞争性 | 竞争性 |
| TimeLens-8B | SOTA | SOTA（超GPT-5） | SOTA |

### 消融实验
| 配置 | 关键指标 | 说明 |
|------|---------|------|
| 原始 vs 修复基准 | 排名剧变 | 证明旧基准不可靠 |
| SFT vs RLVR | RLVR更优 | VTG是感知任务 |
| Thinking vs Thinking-free RLVR | Thinking-free更优 | CoT对VTG无益 |
| 早停+难度采样 | 训练效率和性能均提升 | RLVR的实用经验 |

### 关键发现
- 现有VTG基准错误率惊人地高（Charades-STA重复查询问题尤为严重）
- 在修复基准上，开源模型与商业模型的对比结果完全不同
- Thinking-free RLVR的发现反直觉但经实验验证：VTG不需要推理过程
- TimeLens-8B（基于Qwen3-VL-8B）超趇GPT-5和Gemini-2.5-Flash

## 亮点与洞察
- “不是新方法而是必要的基线"的定位诚实且有价值
- 数据质量工作巨大：三个基准的完整重标注，包含严格的交叉验证
- "VTG是感知而非推理"的发现对社区有重要启示
- RLVR经验（早停+难度采样）具有广泛参考价值

## 局限性 / 可改进方向
- 重标注工作需大量人工参与，可扩展性有限
- Thinking-free RLVR可能不适用于更复杂的时序推理任务
- 模型基于Qwen2.5-VL/Qwen3-VL，所发现的最佳实践对其他基座的迁移性待验证

## 相关工作与启发
- Time-R1、VideoChat-R1等RLVR方法在TimeLens-Bench上表现明显不如TimeLens
- 与TRACE等专门模型对比，TimeLens基于更强基座且数据质量更高
- 经验可迁移到其他需要精确时间感知的任务

## 评分
- 新颖性: ⭐⭐⭐ 方法本身是增量式的，价值在于系统性
- 实验充分度: ⭐⭐⭐⭐⭐ 数据重标注+算法设计空间探索极其彻底
- 写作质量: ⭐⭐⭐⭐⭐ 结构清晰，每个发现都有充分证据
- 价值: ⭐⭐⭐⭐⭐ 基准修复和最佳实践对社区极其有用

## 补充说明
- TimeLens-7B基于Qwen2.5-VL-7B，TimeLens-8B基于Qwen3-VL-8B
- 在Charades-STA数据集中发现大量重复查询描述同一事件的问题
- ActivityNet Captions中存在不存在的事件和信息泄露问题
- 标注团队经过严格培训和试标注筛选，手册和界面均在附录公开
- 评估使用R1@0.3/0.5/0.7和mIoU四个指标
- Gemini-2.5-Pro在修复后的基准上表现最强（mIoU: 52.8/58.1/70.4）
