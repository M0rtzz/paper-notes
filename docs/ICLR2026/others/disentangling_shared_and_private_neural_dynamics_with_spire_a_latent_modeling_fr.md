# Disentangling Shared and Private Neural Dynamics with SPIRE: A Latent Modeling Framework for Deep Brain Stimulation

**会议**: ICLR2026  
**arXiv**: [2510.25023](https://arxiv.org/abs/2510.25023)  
**代码**: [GitHub](https://github.com/Rahil-Soroush/spire-iclr2026)  
**领域**: others  
**关键词**: latent variable model, shared-private disentanglement, deep brain stimulation, multi-region neural dynamics, autoencoder  

## 一句话总结
提出 SPIRE（Shared–Private Inter-Regional Encoder），一种深度多编码器自编码器，将多脑区神经记录分解为跨区域共享和区域专属的潜在子空间，仅在基线数据上训练即可揭示深脑刺激（DBS）引发的网络级动态重组。

## 背景与动机
- 运动障碍（如肌张力障碍、帕金森病）涉及基底神经节-丘脑-皮层回路的功能失调，DBS 是有效的临床干预手段，但其网络级机制仍不清楚
- 现有 DBS 分析多聚焦于局部特征（频谱功率、诱发电位），但越来越多证据表明 DBS 会重塑跨区域动态
- 经典潜变量模型（GPFA、CCA）假设线性关系；DLAG 虽能分解 shared/private 但限于线性高斯框架且主要用于 spike 数据
- 多模态模型（SharedAE、MMVAE）对齐共享空间但并非为颅内刺激记录设计
- **核心缺口**：缺少一个非线性、能显式分解 shared vs. private 动态的框架，适用于人类 LFP 数据在外部扰动下的分析

## 核心问题
如何从多脑区颅内记录中非线性地分解出跨区域共享动态与区域专属动态，并利用这种分解揭示 DBS 刺激如何系统性重组脑区间的协调模式？

## 方法详解

### 模型架构
- **双潜空间自编码器**：每个脑区 $r$ 配备独立的 encoder-decoder 对
- **编码器**：GRU 编码器处理多通道输入 $x^{(r)} \in \mathbb{R}^{B \times T \times C_r}$，生成隐状态 $h^{(r)}$，经线性投影分别得到共享潜变量 $z_{\text{sh}}^{(r)}$ 和专属潜变量 $z_{\text{pr}}^{(r)}$
- **解码器**：将共享和专属潜变量拼接后重建原始信号 $\hat{x}^{(r)} = f_{\text{dec}}^{(r)}([z_{\text{sh}}^{(r)}, z_{\text{pr}}^{(r)}])$

### 跨区域对齐机制
- 使用轻量级线性映射 $M^{(s \to r)}$（初始化为单位矩阵）和深度一维卷积 ConvAlign（初始化为脉冲响应）进行时空对齐
- ConvAlign 为每个共享潜变量维度维护一个滤波器，容许小的相位偏移
- 映射是有方向性的（$s \to r$ 与 $r \to s$ 独立学习），无需对称

### 多目标训练损失
总损失包含 9 项，平衡三大目标：

1. **重建**：$\mathcal{L}_{\text{rec}}$（自身 shared+private 重建）、$\mathcal{L}_{\text{cross}}$（跨区域 shared 重建）、$\mathcal{L}_{\text{self}}$（仅自身 shared 重建）
2. **对齐**：$\mathcal{L}_{\text{align}}$ 使用 VICReg 方差-不变性-协方差正则化来对齐不同区域的 shared 潜变量
3. **解缠**：$\mathcal{L}_{\text{orth}}$ 惩罚 shared 与 private 的交叉协方差；方差守卫 $\mathcal{L}_{\text{var-sh}}, \mathcal{L}_{\text{var-pr}}$ 防止退化解
4. **对齐模块正则**：$\mathcal{L}_{\text{mapid}}$ 将线性映射偏向单位矩阵；$\mathcal{L}_{\text{align-reg}}$ 将 ConvAlign 滤波器正则化为脉冲状

### 训练策略
- 仅在 off-stimulation 基线数据上训练，建立内在协调的参考框架
- 在 DBS 条件下进行推理，观察刺激如何重组潜在空间
- 使用 GRU encoder-decoder、Adam 优化器、早停、梯度裁剪、混合精度训练

## 实验关键数据

### 合成数据验证
- 三个合成数据集（D0/D1/D2），从线性到非线性畸变到时变延迟逐步递增复杂度
- 每个数据集 100 trials × 250 时间步（0.5s@500Hz），3 shared + 3 private 维度
- **D1（非线性）**：SPIRE 的 CCA 相关性为 (0.92, 0.91, 0.71) vs. DLAG 的 (0.86, 0.79, 0.60)
- SPIRE 在恢复 private 潜变量方面统计显著优于 DLAG（$p < 0.05$）
- 在非线性（D1）和时变延迟（D2）条件下，SPIRE 对 shared 潜变量的恢复也优于 DLAG

### 人类 DBS 记录
- **数据**：10 名肌张力障碍儿科患者的颅内 LFP，电极覆盖 GPi 和 STN，17 个半球
- 刺激条件：GPi 85/185/250 Hz、STN 85/185 Hz 及 off-stimulation
- 信号降采样至 500 Hz，50 Hz 低通滤波去除高频刺激伪影

### 解缠验证
- shared GPi/STN 子空间的 CCA 中位数接近 1.0（高度一致）
- shared 与 private 子空间间 CCA 仅 0.55–0.65（有效解缠）
- 完整潜空间重建误差中位数：GPi 0.00211, STN 0.000983（接近零误差）
- 仅用 private 重建误差大幅增加（GPi 0.544, STN 0.391）

### 刺激频率解码
- 随机森林分类器从 shared 潜变量解码刺激频率的准确率显著高于 private 潜变量（$p < 0.001$）
- GPi-shared 和 STN-shared 解码准确率无显著差异，说明 shared 空间编码了跨区域泛化的刺激签名

### 与基线方法对比
- SPIRE 在 GPi 和 STN 的重建误差上均低于 SharedAE 和 MMVAE
- DLAG 在真实颅内数据上无法收敛（高斯过程优化数值不稳定）

## 亮点
- **首个非线性 shared-private 分解框架**用于多区域颅内记录，填补了线性模型与实际非线性神经数据间的鸿沟
- **训练范式巧妙**：仅在基线数据训练建立参考框架，再在刺激数据上推理观察重组，避免刺激伪影污染模型
- **VICReg 对齐 + 正交解缠 + ConvAlign 时间对齐**的组合损失设计精巧，各项正则化都有明确物理含义
- 首次在儿科 DBS 数据上展示共享潜变量编码频率依赖的网络重组，支持 DBS 的分布式网络调制理论

## 局限性 / 可改进方向
- 仅限较短时间尺度刺激，未验证长期慢性刺激效果
- 仅使用 LFP 信号，未整合 spike 数据或其他模态
- 缺少概率性目标函数（如 VAE）来量化不确定性
- 目前仅验证双区域（GPi-STN），尚未扩展到皮层、丘脑等更多区域
- 共享潜变量维度是"统计抽象"，赋予精确生物物理含义需要额外实验验证
- 样本量较小（10 名患者，17 个半球），泛化性有待更大规模数据验证

## 与相关工作的对比
| 方法 | 非线性 | Shared/Private 分解 | 适用 LFP | DBS 场景 |
|------|--------|---------------------|----------|----------|
| GPFA / CCA | ✗ | ✗ | ✓ | ✗ |
| DLAG | ✗ | ✓ | ✗（主要用于 spike） | ✗（数值不稳定） |
| SharedAE | ✓ | 部分（无时间分辨率） | ✗ | ✗ |
| MMVAE | ✓ | ✗（无显式解缠） | ✗ | ✗ |
| LFADS | ✓ | ✗（统一潜空间） | ✓ | ✗ |
| **SPIRE** | **✓** | **✓** | **✓** | **✓** |

## 启发与关联
- 训练于基线、推理于扰动的范式具有通用性，可应用于其他"控制 vs 处理"场景下的多视角动态系统分析
- shared-private 解缠思想可迁移到多模态 AI 模型中，如视觉-语言模型中分解模态共享与模态专属表示
- ConvAlign 的轻量时间对齐模块是处理跨区域/跨模态时间偏移的简洁方案，可借鉴到视频理解或多传感器融合任务

## 评分
- 新颖性: ⭐⭐⭐⭐ — 首个将非线性 shared-private 分解应用于人类颅内 DBS 记录的框架
- 实验充分度: ⭐⭐⭐⭐ — 合成基准+真实临床数据+多基线对比+消融，但样本量偏小
- 写作质量: ⭐⭐⭐⭐ — 结构清晰，图表丰富，损失函数定义完整
- 价值: ⭐⭐⭐⭐ — 对计算神经科学和 DBS 临床机制理解有实质贡献
