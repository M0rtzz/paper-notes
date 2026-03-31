# PYRA: Parallel Yielding Re-Activation for Training-Inference Efficient Task Adaptation

**会议**: ECCV 2024  
**arXiv**: [2403.09192](https://arxiv.org/abs/2403.09192)  
**代码**: [GitHub](https://github.com/THU-MIG/PYRA)  
**领域**: 模型压缩/高效推理  
**关键词**: PEFT, token merging, training-inference efficiency, ViT, task adaptation

## 一句话总结
提出PYRA方法同时实现训练高效和推理高效的任务适配，通过并行生成通道和token维度的自适应调制权重，在token合并前对特征进行re-activation校准，在ViT-L/16上1.7×加速仅掉0.1%精度、3×加速下消除"逆向压缩"现象。

## 研究背景与动机

1. **领域现状**：大规模ViT的下游适配面临训练开销和推理效率两大挑战。PEFT（LoRA等）解决训练效率但不降推理成本；模型压缩解决推理效率但需大量重训。
2. **现有痛点**：简单组合PEFT+Token Merging（如LoRA+ToMe）在低压缩率下性能略降，高压缩率（>3×）下出现"逆向压缩"——压缩后大模型性能不如直接用小模型。
3. **核心矛盾**：PEFT只微调少量参数，对数据分布的感知力有限；token合并造成信息损失，有限参数无法弥补。
4. **本文要解决什么**：提出"训练-推理高效任务适配"新范式——用极少可训练参数适配同时获得推理加速。
5. **切入角度**：在token合并前对被合并token做自适应特征调制，补偿合并造成的信息损失。
6. **核心idea一句话**：用两个轻量可学习向量并行生成通道维和token维的调制权重，通过sigmoid re-activation策略校准token特征。

## 方法详解

### 整体框架
在ViT每个block的MHSA前进行token合并。PYRA在合并前插入调制：(1) 构建信息矩阵 $M_{info}^l = \text{LN}(M_s^l + M_t^l)$；(2) 两个向量 $W_r^l, W_D^l$ 并行生成通道权重和token权重；(3) 双重sigmoid re-activation调制；(4) 调制后平均池化合并。

### 关键设计

1. **并行生成自适应权重（Parallel Yielding）**
   - 做什么：解耦生成通道维 $\delta_D^l \in \mathbb{R}^{D \times 1}$ 和token维 $\delta_r^l \in \mathbb{R}^{1 \times r}$ 的调制权重
   - 核心思路：$\delta_D^l = M_{info}^l W_r^l$，$\delta_r^l = W_D^l M_{info}^l$，两路平行计算
   - 设计动机：低秩解耦让每个方向各自感知数据分布，参数极少（2个向量/层）

2. **Re-Activation调制策略**
   - 做什么：两重sigmoid门控+残差连接实现稳定的特征调制
   - 核心思路：$\hat{M}_s^l = 2\sigma(\hat{\delta}_D^l) \odot M_s^l$，然后 $M_s^l \leftarrow M_s^l + (2\sigma(\hat{\delta}_r^l)-1) \odot \hat{M}_s^l$
   - 设计动机：sigmoid约束权重范围；两重调制+残差使低秩分解等效于更高秩表达；$W_D^l$ 初始化为0保证初始恒等

3. **仅调制源token**
   - 做什么：只调制pair中的源token $M_s^l$，不动目标token $M_t^l$
   - 核心思路：源token互不重复，但目标token可能共享同一个token
   - 设计动机：避免对共享目标token的冲突修改，保持并行一致性

### 损失函数 / 训练策略
标准交叉熵，仅训练LoRA+每层2个调制向量，backbone冻结。

## 实验关键数据

### 主实验

| 方法 | 加速比 | VTAB-1K Acc | 可训练参数 |
|------|--------|------------|----------|
| LoRA | 1.0× | 73.6 | 0.29M |
| ToMe+LoRA | 1.7× | 72.9 | 0.29M |
| **PYRA** | **1.7×** | **73.5** | 0.30M |
| ToMe+LoRA | 3.0× | 67.2 | 0.29M |
| **PYRA** | **3.0×** | **71.8** | 0.30M |

### 消融实验

| 配置 | 1.7× | 3.0× | 说明 |
|------|------|------|------|
| 基线 | 72.9 | 67.2 | ToMe+LoRA |
| +仅 $\delta_D$ | 73.2 | 69.5 | 通道调制 |
| +仅 $\delta_r$ | 73.1 | 69.1 | token调制 |
| +双维并行 | **73.5** | **71.8** | 完整PYRA |

### 关键发现
- 1.7×下PYRA仅掉0.1%，3.0×下提升4.6%消除逆向压缩
- 双维调制互补，缺任一维掉2%+
- 跨backbone（ViT-B/L、DeiT-B）稳定有效

## 亮点与洞察
- **"训练-推理高效"新范式**：不是简单组合PEFT+压缩，而是专门设计适配机制弥合信息损失
- **极简参数**：每层仅增2个向量，通过re-activation实现高阶调制
- **"逆向压缩"概念**：首次量化高压缩率下大模型不如小模型的现象

## 局限性 / 可改进方向
- 仅在分类任务验证，检测/分割效果未知
- token合并配对策略沿用ToMe，可能非最优
- 固定每层压缩率，未做层自适应搜索

## 相关工作与启发
- **vs ToMe+LoRA**: 基线方案，PYRA高压缩率提升4.6%
- **vs DiffRate**: 搜索层级最优压缩率，但需更多训练
- **vs SSF**: 做全局scaling/shifting，PYRA做合并粒度局部调制

## 评分
- 新颖性: ⭐⭐⭐⭐ 训练-推理高效范式+re-activation设计新颖
- 实验充分度: ⭐⭐⭐⭐ VTAB-1K 19任务+多backbone+消融全面
- 写作质量: ⭐⭐⭐⭐ 问题定义清晰，逆向压缩概念准确
- 价值: ⭐⭐⭐⭐ 对大模型实际部署有直接价值
