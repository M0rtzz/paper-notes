# Team Anotheroption at SemEval-2025 Task 8: Bridging the Gap Between Open-Source and Proprietary LLMs in Table QA

**会议**: ACL 2025  
**arXiv**: 无  
**代码**: 无  
**领域**: LLM / NLP  

## 一句话总结
提出一种混合 LLM 管道系统，通过 Text-to-SQL/Code 生成、RAG 检索、自纠错机制和 LLM Orchestrator 协调多个开源模型，在 SemEval-2025 Task 8（表格问答）中达到 80% 准确率（Top-13/38），开源模型组合（88%）超越 GPT-4o 单模型（74%）。

## 背景与动机
1. **表格问答需求广泛**：通过自然语言查询结构化数据在金融、医疗、商业等领域有广泛应用，但将自然语言转化为可执行操作仍是重大挑战。
2. **开源与闭源差距**：GPT-4o 等闭源模型在表格 QA 上表现优异，但开源模型长期落后，限制了可复现性和部署灵活性。
3. **单模型能力有限**：不同类型问题（数值计算 vs 语义理解）适合不同解题路径（SQL/Python vs 端到端），单一模型和方法难以全面覆盖。
4. **真实数据挑战多**：DataBench 数据集保留了真实世界噪声（缺失值、emoji、缩写列名等），对系统鲁棒性要求极高。
5. **代码生成易出错**：LLM 生成的 SQL/Python 代码常有聚合逻辑错误、类型操作错误和参数遗漏等问题，需要纠错机制。
6. **长上下文问题**：端到端模型面临"大海捞针"困境，完整表格上下文过长导致遗漏关键信息或产生幻觉。

## 方法详解
### 整体架构
系统包含两条并行路径——**Code-based** 和 **End-to-End**，最终由 Orchestrator 仲裁：

### 1. Text-to-SQL 模块
- 使用 Codestral 和 Qwen Coder 2.5-32B 生成 SQL 查询。
- 通过 RAG 注入相关行数据和建议列名，丰富 prompt 上下文。
- 查询在 SQLite（通过 SQLAlchemy）内存数据库上执行。

### 2. Pandas Code 生成模块
- 同样使用 Codestral 和 Qwen Coder 生成 Python/Pandas 代码。
- 在沙箱环境中执行（带超时保护），记录执行状态和错误信息。

### 3. RAG 检索增强
- 为相关列创建句子嵌入并存储索引。
- 查询时检索语义最相似的 Top-3 行，注入 LLM 上下文，解决数据大小写/格式不匹配问题。

### 4. 自纠错机制
- 当 SQL/Python 执行失败时，将 schema、错误信息与原始问题回传 LLM 重新生成。

### 5. End-to-End 模块
- 使用 MiniMax-01 将表格转 Markdown，LLM 直接回答问题。
- 擅长需要语义理解的问题（如"标题是否涉及 communication"）。

### 6. LLM Orchestrator
- Llama 3.3-70B Instruct 作为仲裁者，从多个候选答案中选择最可能正确的。
- 不能自行生成答案，仅在已有候选中选择。

### 7. 辅助技术
- **列预测**：LLM 预选相关列，减少上下文长度。
- **列名解释**：将缩写列名重命名为可读形式（如 DMC → Duff Moisture Code）。

## 实验关键数据

### 表1：开源模型赛道官方排名

| 排名 | 团队 | 准确率 (%) |
|:--:|:--|:--:|
| 1 | TeleAI | 95.02 |
| 2 | SRPOL AIS | 89.66 |
| **13** | **anotheroption** | **80.08** |
| baseline | stable-code-3b-GGUF | 26.00 |

- 在 38 支参赛队中排名 Top-13，比 baseline 高 54 个百分点。
- 在含闭源模型的全局排名中位列 Top-20/53，仅使用开源模型。

### 表2：开发集消融实验结果

| 配置 | 准确率 (%) |
|:--|:--:|
| Codestral Python only | 72 |
| Codestral Python + Reformulation | 68 |
| Codestral Python + SQL | 84 |
| MiniMax E2E only | 54 |
| MiniMax E2E + Reformulation | 52 |
| Codestral + Qwen Coder Python (w/ orchestrator) | 88 |
| **Full pipeline (w/ orchestrator)** | **88** |
| GPT-4o (w/o orchestrator) | 74 |
| GPT-4o (w/ pipeline) | 87 |

- 开源组合（88%）超越 GPT-4o 单模型（74%），证明编排多模型可弥补单模型不足。
- 问题改写（Reformulation）反而降低准确率，因错误会在管道起点传播且无恢复机制。
- SQL 能力加入后准确率从 72% 提升至 84%，互补效应显著。

### Orchestrator 决策分析
- 63.4% 为一致性确认（所有候选答案相同）。
- 14.6% 过滤逻辑缺陷答案，12.2% 拒绝格式不匹配答案，9.8% 裁决分歧答案。

## 亮点
- **开源超闭源**：通过多模型编排，开源 LLM 组合在开发集上达到 88%，超越 GPT-4o（74%），具有实际参考价值。
- **模块化设计**：SQL/Python/E2E 三路径互补，Orchestrator 仲裁，架构灵活且每个组件可独立替换。
- **详尽的消融实验**：逐步添加组件展示每部分贡献，为实践者提供清晰的设计指导。
- **失败模式分析深入**：将代码生成错误细分为语法错误（聚合/类型/参数）和逻辑错误（语义偏差/边界情况），便于针对性改进。

## 局限性 / 可改进方向
- 所有候选答案均错误时 Orchestrator 无法补救，系统无兜底机制。
- 检索依赖嵌入语义匹配，当查询用词与表格数据偏差大时效果受限。
- 自纠错机制实际效果有限——因多 Agent 并行，几乎总有至少一个可运行方案，自纠错很少被触发。
- 问题改写的负面效果仅在多模型场景下验证，缺少单模型场景的对比实验。
- Emoji 处理为手工规则（替换为 hash），缺乏通用解决方案。
- 未探索动态路径选择（自动判断 SQL/Python/E2E 哪条路径最适合当前问题）。

## 与相关工作的对比
- **FeTaQA / ChartQA / OpenWikiTable**：前期表格 QA 数据集，DataBench 更贴近真实世界噪声和多样性。
- **Text-to-SQL 方法（Zhong et al.）**：传统单路径生成，本文扩展为 SQL+Python+E2E 多路径并结合 Orchestrator。
- **Chain-of-Thought (Wei et al.)**：本文使用 CoT 引导推理，但发现过度改写问题反而有害。
- **RAG (Gao et al.)**：本文将 RAG 应用于表格行检索而非传统文档检索，解决数据格式不匹配问题。
- **Self-correction (Deng et al.)**：虽引入但实际触发率低，多 Agent 策略在一定程度上替代了自纠错的必要性。

## 评分
- 新颖性: ⭐⭐⭐ — 组件均为已知技术的组合，但多模型 Orchestrator 编排思路在表格 QA 中有实用创新
- 实验充分度: ⭐⭐⭐⭐ — 消融实验全面，错误分析详细，开源 vs 闭源对比有说服力
- 写作质量: ⭐⭐⭐ — 结构清晰但部分描述冗余，图表较多但正文叙述可更精炼
- 价值: ⭐⭐⭐ — 作为 SemEval 系统报告提供了实用的工程经验，开源超闭源的结论对社区有参考价值
