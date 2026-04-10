<!-- 由 src/gen_stubs.py 自动生成 -->
# Expert-Guided Prompting and Retrieval-Augmented Generation for Emergency Medical Service Question Answering

**会议**: AAAI2026  
**arXiv**: [2511.10900](https://arxiv.org/abs/2511.10900)  
**代码**: [EMSQA](https://uva-dsa.github.io/EMSQA)  
**领域**: medical_imaging  
**关键词**: RAG, chain-of-thought, emergency medical services, question answering, domain expertise  

## 一句话总结
构建了首个 EMS 领域多选问答数据集 EMSQA（24.3K 题），并提出 Expert-CoT + ExpertRAG 框架，通过注入 subject area 和 certification level 等专业属性引导 LLM 推理和检索，最高带来 4.59% 的准确率提升。

## 背景与动机
- LLM 在医学 QA 上表现不错，但忽略了领域专业属性（如临床 subject area、认证等级）
- 现有 medical MCQA 数据集（MedQA、MedMCQA）只覆盖单一认证等级，缺乏结构化的 expertise 标注
- 通用的 CoT 和 RAG 策略没有利用到问题的领域上下文信息
- EMS 领域缺少公开可用的 QA 数据集和领域知识库

## 核心问题
如何将医疗从业者的领域专业知识（subject area + certification level）显式注入 LLM 的推理和检索过程，提升 EMS 问答的准确率？

## 方法详解

### 整体框架
三阶段：(1) 数据集与知识库构建 → (2) 专业属性分类器 Filter → (3) Expert-CoT + ExpertRAG 推理

### 关键设计
1. **EMSQA 数据集**：24.3K 多选题，覆盖 10 个 subject area（trauma、airway、cardiology 等）和 4 个认证等级（EMR→EMT→AEMT→Paramedic），配有 40K 文档的知识库和 400 万条患者记录
2. **Filter 分类器**：基于 LoRA 微调的轻量级 LLM，用两个分类 head 联合预测 subject area（multi-label, BCE）和 certification level（multi-class, CE），损失为 $\mathcal{L} = w_{sub} \cdot \text{BCE}(p_i^{sub}, y_i^{sub}) + w_{lvl} \cdot \text{CE}(p_i^{lvl}, y_i^{lvl})$
3. **Expert-CoT**：将预测的 subject area $\hat{s}_i$ 和 certification level $\hat{l}_i$ 注入 prompt，引导模型从特定领域视角进行 step-by-step 推理
4. **ExpertRAG**：三种检索策略
   - **Global**：从全部 KB/PR 检索（baseline）
   - **Filter then Retrieve (FTR)**：先按 subject area 过滤，再检索
   - **Retrieve then Filter (RTF)**：先检索大候选集，再按 subject area 过滤

## 实验关键数据

| 方法 | Public Acc | Private Acc |
|------|-----------|------------|
| Qwen3-32B 0-shot | 83.55 | 85.11 |
| Qwen3-32B CoT | 84.96 | 88.78 |
| Qwen3-32B Expert-CoT (Filter) | **85.57** | **89.50** |
| OpenAI-o3 0-shot | 92.39 | — |

| RAG 方法 | Public Acc | Private Acc |
|---------|-----------|------------|
| Qwen3-4B CoT (no RAG) | 72.35 | 70.58 |
| Qwen3-4B Global (CoT) | 78.12 | 75.46 |
| ExpertRAG-Filter RTF + Expert-CoT | **82.71** | **80.05** |
| 改进幅度 vs Global | +4.59 | +4.59 |

- Expert-CoT 比 vanilla CoT 最高提升 2.05%
- ExpertRAG + Expert-CoT 比标准 RAG 最高提升 4.59%
- 32B 模型 + expertise augmentation 通过了所有 NREMT 模拟认证考试

## 亮点
1. **首个 EMS MCQA 基准**：填补了 EMS 领域 QA 数据集的空白，标注了 subject area 和 certification level
2. **结构化 expertise 注入**：将专业属性作为显式信号引导推理和检索，思路简洁有效
3. **端到端框架**：Filter → Expert-CoT → ExpertRAG 形成完整 pipeline
4. **多源知识库**：整合教材、视频、指南、flashcards 和真实患者记录

## 局限性 / 可改进方向
- Filter 分类器准确率有限（subject area miF ≈ 80%），误分类会传播到后续模块
- 仅用 Qwen3-4B 做 RAG 实验，未在更大模型上验证 ExpertRAG 效果
- 数据集部分来自收费网站，仅开放了公开部分
- 知识库缺少 certification level 标注，限制了更精细化的检索
- 仅评估多选题，未扩展到开放式问答或临床决策场景

## 与相关工作的对比
- vs **MedRAG**：MedRAG 使用通用医学语料，EMSQA 使用领域对齐的 KB，ExpertRAG 在 Public Acc 上高约 8%
- vs **i-MedRAG**：i-MedRAG 通过迭代 query 改写提升，而 ExpertRAG 通过 subject area 过滤提升，路径不同
- vs **Self-BioRAG**：Self-BioRAG 在 EMSQA 上表现较差（55.71%），说明通用 bio 域 RAG 不适用于 EMS
- vs **MedQA/MedMCQA**：EMSQA 覆盖多认证等级并配有结构化 KB，是更完整的评测框架

## 启发与关联
- 将领域 expertise 作为显式条件注入 prompt/retrieval 的思路具有通用性，可迁移到法律、金融等其他专业领域
- Subject area 分类 + 分区检索的策略比全局检索更高效更准确，在构建 domain-specific RAG 时值得借鉴
- Filter 的多任务训练（subject area + level 联合预测）是轻量化且实用的设计

## 评分
- 新颖性: ⭐⭐⭐ — 核心思路是把 expertise 注入 CoT/RAG，idea 直觉但系统性好
- 实验充分度: ⭐⭐⭐⭐ — 多模型、多 RAG baseline 对比，含认证考试实测
- 写作质量: ⭐⭐⭐⭐ — 图表清晰，数据集构建过程详细
- 价值: ⭐⭐⭐⭐ — 数据集本身有持续价值，框架可推广
