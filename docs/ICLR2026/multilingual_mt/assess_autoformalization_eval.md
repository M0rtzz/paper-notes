---
title: >-
  [论文解读] ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity
description: >-
  [ICLR 2026][自动形式化] 本文提出 ASSESS 框架和 TransTED Similarity 指标，通过将形式语句解析为操作符树并在树编辑距离中融入语义变换，实现了自动形式化语句相似度的 SOTA 评估（70.16% 准确率、0.35 Kappa），并发布了包含 1247 对专家标注的 EPLA 基准。
tags:
  - ICLR 2026
  - 自动形式化
  - 形式语句相似度
  - 树编辑距离
  - 语义变换
  - Lean定理证明
---

# ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity

**会议**: ICLR 2026  
**arXiv**: [2509.22246](https://arxiv.org/abs/2509.22246)  
**代码**: [GitHub](https://github.com/XiaoyangLiu-sjtu/ASSESS)  
**领域**: 多语言翻译  
**关键词**: 自动形式化, 形式语句相似度, 树编辑距离, 语义变换, Lean定理证明

## 一句话总结
本文提出 ASSESS 框架和 TransTED Similarity 指标，通过将形式语句解析为操作符树并在树编辑距离中融入语义变换，实现了自动形式化语句相似度的 SOTA 评估（70.16% 准确率、0.35 Kappa），并发布了包含 1247 对专家标注的 EPLA 基准。

## 研究背景与动机

1. **领域现状**: 自动形式化（将自然语言数学命题转为 Lean 等形式语言）快速发展，但评估指标严重滞后。

2. **现有痛点**: 字符串方法（BLEU）忽视语义，$a+b$ 和 $b+a$ 被判为不同；证明方法在证明失败时无法提供梯度化反馈；LLM-as-Judge 成本高且不可复现。

3. **核心矛盾**: 需要一个同时捕获语义等价和结构相似的自动评估指标。

4. **本文目标**: 设计可复现、仅需 CPU 的评估指标，平衡语义和结构信息。

5. **切入角度**: 利用 Lean 语言服务器将形式语句解析为操作符树（OPT），在树编辑距离中引入语义变换。

6. **核心 idea**: TransTED = TED + 语义变换搜索，将逻辑等价的表达式视为距离为 0。

## 方法详解

### 整体框架
两阶段框架：(1) 用 Lean Language Server 解析形式语句为操作符树；(2) 用启发式搜索应用语义变换（tactic commands），最小化变换后的树编辑距离。

### 关键设计

1. **TED Similarity（基线指标）**:
    - 功能: 量化两个形式语句的结构对应度
    - 核心思路: 解析为 OPT（操作符为内部节点、操作数为叶节点），计算标准树编辑距离并归一化：$sim_{TED}(T_1,T_2) = 1 - d_{TED}(T_1,T_2) / \max(|T_1|,|T_2|)$
    - 设计动机: 树结构天然编码运算符优先级和层次关系

2. **TransTED Similarity（核心指标）**:
    - 功能: 在 TED 基础上融入语义变换
    - 核心思路: 将两个语句用等号连接构造等式，应用 Lean tactic（rw?、congrArg、ext 等）进行变换搜索，以 TED 作为启发式优先选择减小距离的变换。终止条件：证明成功（距离=0）、节点限制或时间限制
    - 设计动机: 定理 1 证明满足 TED 上界约束和变换单调性约束的最大伪度量唯一存在

3. **EPLA 基准数据集**:
    - 功能: 评估形式语句相似度指标的可靠基准
    - 核心思路: 用 4 个翻译器（Herald、Goedel-Formalizer、Gemini-2.5-Pro、Qwen3-Max）自动形式化 miniF2F-test 和 ProofNet-test，编译过滤后由 7 位专家标注语义可证性和结构相似性
    - 设计动机: 现有基准仅提供粗粒度二值标签，无法评估细粒度指标性能

### 损失函数 / 训练策略
- 无需训练，纯推理方法
- 搜索参数：rw? top-5 建议，最大树大小 32，搜索超时 10 分钟
- 仅需 CPU 即可运行，不依赖 GPU

## 实验关键数据

### 主实验

| 基准 | 指标 | TransTED | BEq (证明) | BLEU | Majority Voting |
|------|------|----------|-----------|------|-----------------|
| EPLA-miniF2F | Accuracy | **70.16%** | 59.45% | 68.96% | 46.93% |
| EPLA-miniF2F | Kappa | **0.35** | 0.29 | 0.26 | 0.14 |
| EPLA-ProofNet | Accuracy | **67.31%** | 60.34% | 57.21% | 54.57% |
| EPLA-ProofNet | Kappa | **0.30** | 0.28 | 0.18 | 0.12 |

### 消融实验

| 配置 | EPLA-miniF2F Kappa | 说明 |
|------|-------------------|------|
| TransTED | 0.35 | 语义变换提升 |
| TED only | 0.31 | 纯结构无法区分语义等价 |

### 关键发现
- 证明方法（BEq）精度高但召回低（假阴性多），TransTED 平衡更好
- rw? 和 norm_cast 使用频率最高但采纳率低，forall_congr 和 propext 采纳率高
- TransTED 在阈值选择上稳定性远优于 BLEU
- 在EPLA-ProofNet上同样取得最佳结果（67.31%准确率/0.30 Kappa），证明跨数据集的泛化性
- TED单独使用时Kappa为0.31，加入语义变换后提升至0.35，验证了变换组件的关键作用

## 亮点与洞察
- 将定理证明器的 tactic 作为评估指标中的语义变换操作，巧妙连接证明与评估
- 理论框架（伪度量空间 + 最大约束优化）为 TransTED 提供了数学基础
- EPLA 基准采用三分类标注（可证性 × 变换前/后相似性），比二值标签更精细
- 仅用 CPU 可复现，对资源受限场景友好
- TransTED的计算过程完全确定性，与LLM-as-Judge的随机性形成鲜明对比

## 局限与展望
- 搜索受限于有限的 tactic 集合，可能遗漏某些语义等价情况
- 搜索超时/节点限制导致计算的是 TransTED 的上界而非精确值
- 仅支持 Lean 4，未扩展到 Isabelle、Coq 等其他形式化语言
- EPLA 规模仍然有限（1247 对），更大规模基准有待构建
- tactic库的扩展可能进一步提升TransTED的语义覆盖率
- 对于非数学领域的形式化语句（如程序验证），方法的适用性有待评估

## 相关工作与启发
- **vs BLEU**: BLEU 完全忽视数学语义，$a+b$ vs $b+a$ 被判不同
- **vs BEq/Definitional Equality**: 依赖定理证明器，失败时无法提供任何反馈
- **vs LLM-as-Judge**: TransTED 完全可复现且无需 GPU
- **vs GTED**: GTED 仅支持变量重命名变换，TransTED 支持更丰富的证明变换
- TransTED的成功证明了在评估指标中融入领域特定的语义操作的价值
- 与证明方法互补使用可获得更全面的评估结果
- 操作符树解析依赖Lean Language Server的可用性和稳定性
- 未来可尝试将方法扩展到Isabelle和Coq等其他形式化语言
- 将TransTED与神经网络结合学习更优的变换搜索策略是一个有前景的方向

## 评分
- 新颖性: ⭐⭐⭐⭐ 将 tactic 引入评估指标的树编辑距离是创新设计
- 实验充分度: ⭐⭐⭐⭐ 多基线对比、消融、tactic 使用分析
- 写作质量: ⭐⭐⭐⭐⭐ 理论与实验结合紧密，图表清晰
- 价值: ⭐⭐⭐⭐ 对自动形式化社区提供了急需的评估工具

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ICLR 2026\] Multilingual Routing in Mixture-of-Experts](multilingual_routing_in_mixture-of-experts.md)
- [\[ICLR 2026\] Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity](prior-based_noisy_text_data_filtering_fast_and_strong_alternative_for_perplexity.md)
- [\[ICLR 2026\] ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality](atlas_adaptive_transfer_scaling_laws_for_multilingual_pretraining_finetuning_and.md)
- [\[ICML 2025\] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment](../../ICML2025/multilingual_mt/kelps_a_framework_for_verified_multi-language_autoformalization_via_semantic-syn.md)
- [\[ICLR 2026\] SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs](sasft_sparse_autoencoder-guided_supervised_finetuning_to_mitigate_unexpected_cod.md)

</div>

<!-- RELATED:END -->
