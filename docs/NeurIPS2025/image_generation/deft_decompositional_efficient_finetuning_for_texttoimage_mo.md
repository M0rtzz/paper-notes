# DEFT: Decompositional Efficient Fine-Tuning for Text-to-Image Models

**会议**: NeurIPS 2025  
**arXiv**: [2509.22793](https://arxiv.org/abs/2509.22793)  
**代码**: 有（DEFT GitHub）  
**领域**: 图像生成 / 模型压缩  
**关键词**: 高效微调, T2I, LoRA变体, 子空间分解, 个性化生成  

## 一句话总结
提出DEFT——将权重更新分解为两个可训练矩阵的组合：(1)低秩子空间的正交投影和(2)子空间内的低秩调整，相比LoRA在T2I个性化中CLIP-T从0.341提升到0.361（DreamBench+），在统一模型上实现风格迁移和条件生成的SOTA。

## 背景与动机
T2I模型的高效微调需要平衡三个目标：(1) 对齐目标分布（如个性化新概念）；(2) 保持指令遵循能力；(3) 维持编辑灵活性。LoRA通过低秩矩阵注入适应新任务但不控制更新的方向；PaRa通过正交投影约束更新方向但缺乏灵活性。

## 核心问题
如何设计一种既能控制微调方向又保持灵活调整能力的高效微调方法？

## 方法详解

### 整体框架
DEFT将权重更新分解为：W_total = (I - PP^T)W_0 + PR，其中P定义子空间（正交投影消除不相关方向），R提供子空间内的灵活调整。

### 关键设计

1. **双组件分解**: 
   - **(I-PP^T)W_0**: 投影到P的正交补空间——移除W_0中不需要的成分
   - **PR**: 在P定义的子空间内注入任务特定的适应——扩展列空间
   - 如果col(P) ⊄ col(W_0)，适配后的列空间被扩展，允许学习新方向

2. **多种分解策略**: 支持QR分解、截断SVD、低秩矩阵分解(LRMF)、非负矩阵分解(NMF)、特征分解等

3. **与LoRA/PaRa的关系**:
   - LoRA: W' = W + BA（只做加法更新，不控制方向）
   - PaRa: W' = W - QQ^T W（只做投影减法，缺乏灵活调整）  
   - DEFT: W' = (I-PP^T)W + PR（投影+调整，两者都有）

## 实验关键数据

**DreamBench+ 个性化（CLIP-T↑）**:

| 方法 | CLIP-T |
|------|--------|
| Textual Inversion | 0.302 |
| DreamBooth | 0.323 |
| DreamBooth LoRA | 0.341 |
| PaRa | 0.354 |
| **DEFT** | **0.361** |

**VisualCloze统一生成**: Canny Edge条件下DEFT的CLIP-Score 95.78 vs OmniGen 95.45，DINOv2 一致性90.65 vs 87.60；风格迁移Image Score 0.69（SOTA）

### 消融实验要点
- **分解方法**: QR分解最优，SVD次之
- **Rank选择**: rank=32是效率和效果的最佳均衡
- **DEFT vs LoRA**: DEFT在保留模型编辑能力方面显著优于LoRA（减少过拟合）
- **多概念组合**: DEFT支持多概念个性化生成，减少概念间干扰

## 亮点
- **理论清晰**: 从线性代数的列空间扩展角度解释为什么DEFT优于LoRA/PaRa
- **通用性强**: 从SD v1.5到SDXL到OmniGen统一模型都适用
- **任务覆盖广**: 个性化、风格迁移、条件生成、多概念组合、场景适应

## 局限性 / 可改进方向
- 两个可训练矩阵P和R比LoRA的AB多了投影计算开销
- 仅在扩散模型上验证，AR图像生成模型未测试
- P矩阵的初始化策略对效果影响大但缺乏自动选择机制

## 与相关工作的对比
- **vs LoRA**: DEFT通过正交投影控制更新方向，减少过拟合、保持编辑性
- **vs PaRa**: DEFT多了PR调整项，列空间可扩展而非仅收缩
- **vs Custom Diffusion**: Custom Diffusion微调特定层，DEFT更灵活且参数更少

## 启发与关联
- DEFT的分解思路可以推广到VLM的高效微调——如BranchLoRA的非对称设计可以借鉴DEFT的子空间投影
- 与L4Q（QAT+LoRA融合）结合：在量化环境下使用DEFT替代LoRA可能获得更好的微调效果

## 评分
- 新颖性: ⭐⭐⭐⭐ 双组件分解idea清晰，有数学基础
- 实验充分度: ⭐⭐⭐⭐ DreamBench+/VisualCloze/InsDet多数据集验证
- 写作质量: ⭐⭐⭐⭐ Figure 2的三种方法对比图直观
- 价值: ⭐⭐⭐⭐ T2I高效微调领域的实用改进
