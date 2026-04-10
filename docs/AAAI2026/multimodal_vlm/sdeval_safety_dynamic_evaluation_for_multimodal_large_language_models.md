# SDEval: Safety Dynamic Evaluation for Multimodal Large Language Models

**会议**: AAAI2026
**arXiv**: [2508.06142](https://arxiv.org/abs/2508.06142)
**代码**: [hq-King/SDEval](https://github.com/hq-King/SDEval)
**领域**: multimodal_vlm
**关键词**: MLLM safety, dynamic evaluation, data contamination, jailbreak, benchmark

## 一句话总结
提出 SDEval，首个面向 MLLM 安全性的动态评估框架，通过文本动态（同义替换/多语混合/CoT 注入等）、图像动态（空间/颜色变换/扩散生成）和文本-图像交互动态三类策略，从静态 benchmark 可控生成不同复杂度的新样本，缓解数据泄露并暴露模型安全短板。

## 研究背景与动机
- **数据泄露**：现有安全 benchmark（MLLMGuard、MMSafetyBench 等）基于公开数据集构建，极可能被纳入 MLLM 训练集，评测结果的可信度存疑
- **静态固定**：人工构建的 benchmark 复杂度固定，无法跟上 MLLM 能力的快速迭代
- **攻击演进**：新型 jailbreak 方法不断涌现，但评测基准未同步更新
- 已有动态评估（DyVal）仅面向能力评测的选择题，不适用于开放式安全评估

## 方法详解

### 文本动态 (Text Dynamics)
模拟真实用户规避审查的行为，6 种策略：
1. **Word Replacement**：同义词/上下文近义词替换（≤5 个词）
2. **Sentence Paraphrasing**：保持核心含义，改写句式
3. **Adding Descriptions**：添加相关/无关描述分散模型注意力
4. **Making Typos**：重复字母、拼写错误、特殊字符替换
5. **Linguistic Mix**：中英俄法日韩多语混合
6. **Chain-of-Thought**：添加 "answer step by step" 引导逐步推理

### 图像动态 (Image Dynamics)
- **基础增强**：空间变换（随机 padding 10-20% + 翻转）、颜色变换（颜色反转 + 椒盐噪声）
- **生成与编辑**：GPT-4o 生成 caption → Stable-Diffusion-3.5-Large 重新生成图像；ICEdit 进行目标插入、文字插入、风格迁移
- **验证器**：GPT-4o 校验生成图像与原图的语义一致性

### 文本-图像交互动态 (Text-Image Dynamics)
- **Text-to-Image**：文本动态 → 提取安全关键词 → 扩散模型生成新图像
- **Image-to-Text**：图像动态 → GPT-4o 生成安全中心 caption → 拼入原文本
- **跨模态 Jailbreak**：FigStep（将文本提示转为图像内排版文字）、HADES（将文本中不安全词提取并注入图像）

## 实验关键数据

评测 17 个 MLLM（含 GPT-4o、Claude-4-Sonnet、o3、InternVL-3-78B 等），基于 MLLMGuard 和 VLSBench 两个安全 benchmark。

### Table 1: Dynamic MLLMGuard 结果（ASD↓ / PAR↑）

| 模型 | ASD Avg (Δ vs vanilla) | PAR Avg (Δ vs vanilla) |
|---|---|---|
| GPT-4o | 32.78 (+3.56↑) | 24.71 (-15.67↓) |
| Claude-4-Sonnet | 25.42 (+1.93↑) | 51.89 (-4.48↓) |
| InternVL-3-78B | 39.34 (**+9.24↑**) | 21.40 (**-17.64↓**) |
| Qwen-VL-2.5-7B | 40.17 (+13.71↑) | 33.96 (-10.08↓) |
| DeepSeek-VL | 44.31 (+6.78↑) | 11.91 (-10.78↓) |

- InternVL-3-78B 安全性下降最严重（ASD +9.24%），说明大模型并不天然更安全
- Claude-4-Sonnet 在 PAR 上仍最高（51.89%），整体鲁棒性最强

### Table 2: Dynamic VLSBench 安全率

| 模型 | Vanilla Safety | Dynamic Safety | Δ |
|---|---|---|---|
| GPT-4o | 58.50 | 52.83 | -5.67 |
| InternVL-3-78B | 13.79 | 8.52 | **-5.27** |
| LLaVA-V1.5-13B | 8.65 | 4.28 | -4.17 |

## 亮点
- **首个安全动态评估框架**：三类动态策略可无限生成新变体，从根本上缓解数据泄露问题
- **通用性强**：可应用于安全 benchmark（MLLMGuard/VLSBench）和能力 benchmark（MMBench/MMVet），能力评测上还表现出抗饱和效果
- **策略设计贴近真实攻击**：Typo、多语混合、FigStep 等均模拟真实用户的 jailbreak 行为
- **能力-安全平衡分析**：揭示多数模型在安全维度比能力维度更不稳定

## 局限性
- 文本动态依赖 GPT-4o 生成，引入额外成本和 GPT-4o 自身偏差
- 图像生成依赖 Stable Diffusion 3.5，生成质量可能影响评测公平性
- 验证器基于 GPT-4o 判断语义一致性，缺乏更客观的自动化指标
- 动态策略的组合空间巨大，论文未充分探索不同策略组合的交互效应
- 仅评测英文+中文安全维度，未涵盖更多语言

## 评分
- 新颖性: ⭐⭐⭐⭐ — 安全动态评估的定位清晰有价值，三类动态策略设计系统
- 实验充分度: ⭐⭐⭐⭐⭐ — 17 模型 × 2 安全 benchmark + 2 能力 benchmark，覆盖面广
- 写作质量: ⭐⭐⭐⭐ — 框架图清晰，但表格信息密度高
- 价值: ⭐⭐⭐⭐ — 为 MLLM 安全评估提供可持续演进的评测范式
