<!-- 由 src/gen_stubs.py 自动生成 -->
# Janus-Pro-R1: Advancing Collaborative Visual Comprehension and Generation via Reinforcement Learning

**会议**: NEURIPS2025  
**arXiv**: [2506.01480](https://arxiv.org/abs/2506.01480)  
**代码**: [项目主页](https://janus-pro-r1.github.io)  
**领域**: image_generation  
**关键词**: MLLM, 视觉生成, 强化学习, Chain-of-Thought, Aha Moment, 图像编辑, GRPO  

## 一句话总结

提出两阶段训练范式（SFT + RL），让 MLLM 的视觉理解与生成能力协同进化，构建真正的视觉生成 CoT 并触发 Aha Moment，将文生图升级为迭代自省过程，同时解锁统一图像生成（含图像编辑）。

## Problem

当前统一理解与生成的 MLLM（如 Janus-Pro）存在一个根本问题：**视觉理解和视觉生成两种能力基本独立**，只是共享参数以减少冗余，并没有真正协同。具体表现为：

1. 视觉理解无法提升视觉生成质量——LLM 强大的推理机制没有被充分整合到图像生成中
2. 即便是 SOTA 的 Janus-Pro，基本文生图仍不尽如人意，且只能接受纯文本输入
3. 现有将 CoT 引入视觉生成的工作（如 MINT、GOT）中的 CoT 只是强制性的文字规划，并非模型自发的深度推理

核心问题：**能否让视觉理解与生成真正协同，将推理机制融入视觉生成？**

## Core Idea

实现理解-生成协同后可带来三大革命性收益：

1. **真正的 Chain-of-Thought**：模型在统一 next-token prediction 框架下，自发地将理解和生成交织形成图文交错的推理链
2. **解锁 Aha Moment**：生成初始图像后，模型利用理解能力反思当前生成，发现错误后重新生成——实现自我纠错
3. **统一图像生成**：不仅增强 text-to-image，还能灵活处理图像编辑等复杂场景

## Method

### 整体框架

两阶段训练：**SFT（监督微调）** 赋予基础能力 → **RL（强化学习）** 激发全部潜力。

### Stage 1: Supervised Fine-Tuning

将视觉生成 CoT 分解为三个子任务，通过混合训练让模型掌握基础能力：

**数据准备**：利用 Qwen 生成 200K prompts，用 FLUX 和 Janus-Pro 生成图像，InternVL2.5-26B 评估语义一致性得分 $\mathcal{S} \in [0,1]$。

**Task-I: Text-to-Image Generation**
- 选取 $\mathcal{S} \geq 0.8$ 的高质量图文对做标准 T2I 训练
- 目标函数：$p(y^{\mathcal{I}}) = \sum_{j} \log P_\theta(y_j | y_{<j}, \mathcal{P})$

**Task-II: Self-evaluation of Text-Image Consistency**
- 训练模型判断给定图像是否与文本语义一致，并给出理由
- 构造前序 context：选取 $\mathcal{S} < 0.5$ 的图像作为之前的错误生成
- 随机选取正例（$\mathcal{S} \geq 0.7$）和负例（$\mathcal{S} < 0.5$）作为待评估目标

**Task-III: Image Regeneration**
- 训练模型在前序错误生成（$\mathcal{S} < 0.5$）及其自我反思的 context 下，重新生成正确图像（$\mathcal{S} \geq 0.8$）

**混合训练比例**：Task-I : Task-II : Task-III = 0.2 : 0.3 : 0.5。SFT 阶段设 $t=3$（Task-II）和 $t=2$（Task-III），即允许最多生成三张图像（一次 T2I + 两次再生成）。

**编码器选择**：Janus-Pro 有两种图像编码器——理解编码器（SIGLIP）和生成编码器（VQ tokenizer）。Task-II 的输入图像用理解编码器编码，Task-III 的输入图像用生成编码器编码。Task-I 和 Task-III 中，每个 prompt 有 10% 概率被替换为 [PAD] tokens（用于 classifier-free guidance）。

通过混合训练，模型学会在当前 context 下整合不同子任务，探索连贯的视觉生成推理链，获得触发 Aha Moment 的基础能力。

### Stage 2: Reinforcement Learning

将图像生成建模为 long token-level Markov decision process，使用 **GRPO** 算法，无需 ground-truth 图像。

**Bi-Level QA-based Rewards**（使用 InternVL2.5-26B 作为 reward model）：

- **Generation Reward** $R^{Gen}$：评估最终生成图像的语义一致性。允许最多 $T$ 轮生成，在第 $K$ 轮确定正确，第 $K$ 轮图像获得更大权重：

$$R^{Gen} = \sum_{i=1}^{K-1} R^{QA}(\mathcal{I}^i) + (T - K + 1) \times R^{QA}(\mathcal{I}^K)$$

- **Comprehension Reward** $R^{Comp}$：评估模型自我评估的准确性。衡量模型的 self-evaluation 与 reward model 评分之间的差距：

$$R^{Comp} = \sum_{i=1}^{K} (1 - |R^{QA}(\mathcal{I}^i) - SE(\mathcal{I}^i)|) \times T/K$$

**Policy Gradient**：给定 prompt，从 old policy 采样 $G$ 个初始图像，评估后进入多轮生成-自评-再生成循环。计算 group-relative advantage 后通过 clipped objective 更新策略，加入 KL 散度约束保持训练稳定性。

**RL 训练稳定性技巧**：
- 使用 Linear + Cosine 组合学习率调度器：LR 从 peak（6e-6）快速线性降到 convert LR（2e-6），然后沿 cosine 逐渐衰减
- reward 曲线急剧下降时：将 LR 减半或减至 2/3 后恢复训练
- reward 曲线缓慢下降时（说明较弱的 reference model 限制了改进）：要么减小 $\beta$ 权重，要么将 reference model 更新为当前模型
- 总训练 3000 步，group size=7，$\beta=0.05$，32 张 A800 GPU

### Stage 3: 扩展到图像编辑

内省式文生图本质上是理解与生成的协同——图像编辑同样需要理解编辑指令、生成新图像、且保持未编辑区域不变。因此只需进一步教模型**保持细节**即可。

图像编辑也采用 SFT + RL 两阶段：
- **SFT**：从 UltraEdit 和 AnyEdit 收集编辑数据，用 InternVL2.5-26B 进行数据清洗——只保留 $S^{psv} \geq 0.7$ 且 $S^{flw} \geq 0.7$ 的样本。训练时指令有 10% 概率被 drop 为 [PAD]（用于 CFG）
- **RL**：设计两个 QA-based rewards：
  - **Following score** $R^{flw} \in [0,1]$：是否准确执行编辑请求
  - **Preserving score** $R^{psv} \in [0,1]$：未编辑区域保持程度
  - 最终 reward：$R^{edit} = 0.5 \times R^{flw} + R^{psv}$（$R^{flw}$ 权重较小是为了优先增强局部保真能力；若 $R^{flw}$ 权重过小，模型倾向直接输出原图以获得高 reward）
  - Group size=8，batch size=128，总训练 2.2K 步

## Training/Inference

### 训练配置

| 超参数 | SFT (T2I) | RL (T2I) | SFT (编辑) | RL (编辑) |
|--------|-----------|----------|-----------|----------|
| Peak LR | 2e-5 | 6e-6 | 2e-5 | 1e-5 |
| Batch size | 128 | 128 | 128 | 128 |
| Group size | — | 7 | — | 8 |
| Training Steps | 50K | 3K | 40K | 2.2K |
| 资源 | 8×A800 | 32×A800 | 8×A800 | 32×A800 |

- **Backbone**：Janus-Pro-7B
- **Reward Model**：InternVL2.5-26B（QA-based 评分）
- **SFT 数据**：200K prompts（80K 短描述 + 120K 长描述），每个 prompt 用 FLUX + Janus-Pro-1B/7B 生成 $M=18$ 张图像
- **RL 算法**：GRPO（Group Relative Policy Optimization），KL 散度约束 $\beta=0.05$
- **长 prompt 的 reward 计算**：受 Davidsonian Scene Graph 启发，先将 prompt 分解为语义 tuple（属性、空间关系等），生成对应 yes/no 问题，然后 reward model 对每个问题 VQA 评分，取平均作为一致性分数

### 推理细节

- 模型交替使用 image head（预测 576 个 visual tokens）和 text head（评估语义一致性）
- 最多允许 3 轮生成（1 次 T2I + 2 次再生成）
- Text token sampling: $topk=50$；Visual token sampling: $topk=4096$
- 使用 classifier-free guidance，guidance scale=5.0（T2I）/ 4.0（编辑）
- 理解阶段用 SIGLIP 编码器，生成阶段用 VQ 编码器
- **关键发现**：SFT 阶段数据质量（高阈值筛选 $\mathcal{S} \geq 0.8$）比数量更重要

## Experiments

### Text-to-Image Generation

在 GenEval、T2I-CompBench、DPG-Bench 三个基准上评测：

| 方法 | GenEval Overall | T2I-CompBench Avg | DPG-Bench |
|------|----------------|-------------------|-----------|
| Janus-Pro-7B | 0.80 | — | 84.17 |
| FLUX.1-dev | 0.66 | — | 83.79 |
| GPT-4o | 0.85 | — | — |
| **Janus-Pro-R1 (w/ Aha)** | **0.86** | **72.7** | **85.57** |
| Janus-Pro-R1 (w/o Aha) | 0.83 | 70.3 | 85.02 |

- 相比 backbone Janus-Pro-7B：GenEval +7.5%，T2I-CompBench +47.0%，DPG-Bench +1.7%
- GenEval 超过 GPT-4o（0.86 vs 0.85）
- 一致性超过同类 CoT 方法（MINT、GOT、T2I-R1）

### Image Editing（PIE-Bench）

| 方法 | Structure Dist↓ | PSNR↑ | LPIPS↓ | CLIP Whole↑ |
|------|----------------|-------|--------|-------------|
| EditAR | 39.43 | 21.32 | 117.15 | 24.87 |
| Janus-Pro-Edit | 49.44 | 20.50 | 131.76 | 24.16 |
| **Janus-Pro-R1-Edit** | **35.87** | **22.81** | **114.96** | **24.78** |

在保真度与可编辑性之间取得了优于开源模型的平衡，部分指标甚至超过 Gemini-2.0。

### Image Semantic Evaluator

| 方法 | GenEval 一致率 | GPT-4o 推理可靠性评分 |
|------|---------------|---------------------|
| Janus-Pro-7B | 72.3% | 76.9 |
| InternVL2.5-8B | 79.0% | 92.2 |
| **Janus-Pro-R1** | **81.1%** | **91.1** |

Janus-Pro-R1 作为 reward model 时，能进一步提升其他 backbone 模型的 RL 训练效果，优于 InternVL2.5-8B。

## Results

关键结论：

1. **SFT 模仿，RL 泛化**：SFT 仅赋予子技能的模仿能力，性能提升有限；RL 使模型从模仿进化到真正推理，GenEval 大幅提升（0.81→0.86）
2. **子任务协同效应**：Task-I（生成）与 Task-II+III（自评+再生成）混合训练优于单独训练
3. **模型规模效应**：1B 模型无法有效处理视觉生成 CoT 的深度推理，Aha Moment 甚至损害 1B 模型的初始生成能力——体现 scaling law
4. **反事实生成**：RL 模型能识别"方形苹果"等反事实 prompt 的语义不匹配并纠正，而 SFT 模型不能
5. **理解能力提升**：RL 训练不仅增强生成，还显著提升视觉理解能力——初步验证了真正统一的可能性

## Limitations

1. **计算资源受限**：关于 RL 是否能解锁真正统一的理解与生成的结论，仅基于简单生成任务和语义对齐评估任务，实验不够充分
2. **模型规模要求高**：1B 模型无法获益于该训练范式，需要 7B 以上模型——视觉生成 CoT 的深度推理比语言推理需要更大参数量
3. **多轮生成的推理开销**：Aha Moment 机制每轮需解码 576 visual tokens + 文本评估，最多 3 轮迭代，推理时间约为单次生成的 2-3 倍
4. **Reward model 依赖**：训练和评估都依赖 InternVL2.5-26B 作为 QA-based reward model，受其能力天花板限制；reward hacking 风险未被充分讨论
5. **图像编辑能力有限**：目前只展示了基础的指令编辑，未涉及更复杂的统一生成场景（如 inpainting、style transfer）
6. **SFT 数据构造复杂**：需要多个外部模型（Qwen、FLUX、Janus-Pro、InternVL）配合生成训练数据，pipeline 繁重
7. **RL 训练不稳定**：论文坦承训练中常遇 reward 曲线下降，需要手动调整 LR 和 $\beta$——说明当前 RL for visual generation 的训练范式尚不成熟

## My Notes

- 核心贡献在于将 DeepSeek-R1 的 Aha Moment 思想迁移到视觉生成领域，理念优雅且直观
- "SFT memorizes, RL generalizes" 的发现与 LLM reasoning 领域的观察高度一致，增强了该范式的可信度
- Bi-level reward 设计巧妙：generation reward 关注输出质量，comprehension reward 关注自评准确性，两者缺一不可
- 反事实生成实验（方形苹果）非常直观地展示了 RL 带来的真正推理能力
- 1B 模型失败的发现很有启发——视觉生成的深度推理可能比语言推理需要更大的模型容量
- RL 训练不稳定性问题值得关注：需要手动调 LR 和 $\beta$，说明 visual generation RL 的自动化训练还有很大空间
- 长 prompt 的 reward 计算（先分解为语义 tuple 再逐一 VQA）与 Davidsonian Scene Graph 思路一致，比直接打分更鲁棒
- 编辑任务 reward 中 $R^{flw}$ 权重设为 0.5（而非 1.0）的 trade-off 值得关注——保真性优先于编辑性是合理的工程选择
- 潜在的后续方向：(1) 用更强的 reward model 或 self-rewarding 替代外部评估器；(2) 将 Aha Moment 机制扩展到视频生成（同组已有 [Lin et al.] 探索物理视频生成的 RL）；(3) 探索更高效的推理策略减少多轮开销；(4) 自动化 RL 训练稳定性（自适应 LR/reference model 更新）

## 评分
- 新颖性: ⭐⭐⭐⭐ (将 RL reasoning 的 Aha Moment 迁移到视觉生成，方向新颖)
- 实验充分度: ⭐⭐⭐⭐ (多基准多维度评测，含消融和深度分析)
- 写作质量: ⭐⭐⭐⭐ (结构清晰，故事线完整)
- 价值: ⭐⭐⭐⭐ (为统一 MLLM 的理解-生成协同指明了可行路径)
