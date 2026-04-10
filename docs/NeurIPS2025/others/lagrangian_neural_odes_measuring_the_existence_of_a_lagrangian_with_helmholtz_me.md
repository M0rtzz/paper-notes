# Lagrangian neural ODEs: Measuring the existence of a Lagrangian with Helmholtz metrics

**会议**: NEURIPS 2025  
**arXiv**: [2510.06367](https://arxiv.org/abs/2510.06367)  
**代码**: https://github.com/luwo9/LagrangianNeuralODEs  
**领域**: 其他  
**关键词**: Neural ODE, Lagrangian mechanics, Helmholtz conditions, physics-informed learning, Euler-Lagrange equations  
## Problem

Neural ODE 是一种强大的机器学习工具，能够从数据中学习动力学系统的 ODE $\dot{s} = h_\theta(t, s)$。然而，**并非所有 ODE 都具有物理意义**——物理学中最基本的原理之一是 stationary action principle（稳态作用量原理），要求系统轨迹满足 Euler-Lagrange 方程。标准 Neural ODE 没有任何机制来保证学到的 ODE 是 Euler-Lagrange 方程，因此可能学到非物理的解。

核心问题包括两方面：

1. **判别问题**：给定一个 ODE $\ddot{x} = f(t, x, \dot{x})$，如何**可微地量化**它与 Euler-Lagrange 方程的接近程度？
2. **学习问题**：如何让 Neural ODE 在训练过程中被引导收敛到真正的 Euler-Lagrange 方程，同时不增加推理成本？

## Core Idea

本文的核心贡献是 **Helmholtz metrics**——一种基于 Helmholtz 条件的可微度量，用于衡量给定 ODE 是否来源于 Lagrangian。具体来说：

- **Helmholtz 条件** 是经典力学中判断 ODE 是否来自 Lagrangian 的充要条件
- 作者将这些条件转化为一个可以通过神经网络优化的损失函数 $\mathcal{L}_H$
- 将该度量作为 **regularization** 加入 second-order Neural ODE 的训练中，形成 **Lagrangian Neural ODE**
- 关键优势：推理时完全零额外开销（Helmholtz metrics 仅在训练时使用）

与 Lagrangian Neural Networks (LNNs) 相比，本方法可视为 **逆向方法**：LNNs 直接预测 Lagrangian 再推导 ODE，而本文直接学 ODE 再检验其是否满足 Lagrangian 结构。

## Method

### Second-order Neural ODE

系统建模为二阶 ODE：

$$\frac{d}{dt}\binom{x}{v} = \binom{v}{f_{\theta_1}(t, x, \dot{x})}, \quad v_0 = \text{NN}_{\theta_3}(x_0)$$

其中 $f_{\theta_1}$ 直接建模加速度 $\ddot{x}$，初始速度 $v_0$ 由额外网络从初始位置 $x_0$ 学习。训练时仅需位置数据 $x(t)$。

### Helmholtz Conditions 与 Helmholtz Metrics

给定 ODE $\ddot{x} = f(t, x, \dot{x})$，定义辅助量：

$$\Phi = \frac{1}{2}\frac{d}{dt}\frac{\partial f}{\partial \dot{x}} - \frac{\partial f}{\partial x} - \left(\frac{1}{2}\frac{\partial f}{\partial \dot{x}}\right)^2$$

ODE 来自 Lagrangian 当且仅当存在非奇异对称矩阵 $g$ 满足三个 Helmholtz 条件：

1. $g\Phi = (g\Phi)^\top$（对称性条件）
2. $\frac{dg}{dt} + \frac{1}{2}(\frac{\partial f}{\partial \dot{x}})^\top g + \frac{1}{2}g\frac{\partial f}{\partial \dot{x}} = 0$（演化条件）
3. $\frac{\partial g}{\partial \dot{x}} = (\frac{\partial g}{\partial \dot{x}})^\top$（速度对称性条件）

若满足，$g$ 即为 Lagrangian 的 Hessian。

### 可微化实现

将 $g$ 用神经网络 $g_{\theta_2}$ 参数化，通过最小化残差的 MSE 来学习：

$$\mathcal{L}_H = \text{MSE}\left(\sum_i \mathcal{R}_i\right)$$

关键技术细节：

- **对称性**：$g_{\theta_2}$ 的输出强制对称
- **非奇异性**：用最小绝对特征值 $\lambda_{\min} = \|g\|_{-2}$ 归一化残差，避免网络通过学习小特征值来"作弊"降低残差
- **数值稳定性**：$g_{\theta_2}$ 输出经 $\sinh$ 变换以处理可能的指数行为
- **梯度裁剪**：将 $\|\nabla_{\theta_1} \mathcal{L}_H\|$ 裁剪到 $c_1 \approx 0.05$，确保训练初期以数据主导

### 总损失函数

$$\mathcal{L}_{\text{tot}} = \mathcal{L}_R + \mathcal{L}_H$$

其中 $\mathcal{L}_R$ 是标准回归损失（MSE），$\mathcal{L}_H$ 是 Helmholtz metric 正则项。采用 progressive time step inclusion 避免局部最小值。

## Training/Inference

**训练配置**：

- 网络结构：$f_{\theta_1}$（1层×16神经元），$g_{\theta_2}$（2层×64神经元），$\text{NN}_{\theta_3}$（3层×16神经元）
- 激活函数：Softplus（保证导数光滑，Helmholtz 条件需要）
- 优化器：RAdam，batch size 128
- 学习率：$10^{-4} \leq \text{lr}_0 \leq 10^{-1}$，plateau 时衰减
- 训练数据：6000 条带 5% 噪声的轨迹
- 框架：PyTorch + torchdiffeq

**推理**：仅使用 $f_{\theta_1}$ 和 $\text{NN}_{\theta_3}$，$g_{\theta_2}$ 不参与推理，因此 **零额外推理开销**。

## Experiments

### 实验 1：解析 ODE 上的 Helmholtz Metrics

在已知解析表达式的系统上验证 Helmholtz metrics 的判别能力：

- **2D 阻尼振荡器**（damped oscillator）：有/无阻尼
- **Kepler 问题**（行星运动）：不同偏心率
- **两个非 Lagrangian ODE**：作为反例

### 实验 2：Lagrangian Neural ODE 在数据上的表现

在阻尼振荡器上对比三种设置：

- **(i)** 无正则化的 baseline Neural ODE
- **(ii)** 有正则化但无时间依赖（不存在 Lagrangian）
- **(iii)** 有正则化且有时间依赖（存在 Lagrangian）

训练参数：$n_{\text{periods}} = 3$，$\gamma = 0.5\omega$，$n_t = 30$ 个等间距时间点。

### 实验 3：定量改进评估

训练 40 个模型（正则化 vs 未正则化），在无阻尼振荡器上进行 Welch's t-test，评估 $x$、$\dot{x}$、$\ddot{x}$ 的 MSE，包括外推到两倍训练时间区间。

## Results

### Helmholtz Metrics 判别能力

- **Lagrangian 系统**（Kepler、无阻尼振荡器）：$\mathcal{L}_H$ 显著下降，表明成功找到满足条件的 $g$
- **非 Lagrangian 系统**：$\mathcal{L}_H$ 仅微小改善，正确识别无 Lagrangian
- **阻尼振荡器**（$\gamma \neq 0$）：仅当允许 $g = g(t, x, \dot{x})$ 时有解，与理论一致
- **Kepler 问题**：学到的 $g$ 与解析 Hessian 的中位相对误差为 $3.7 \times 10^{-4}$（20th–80th 百分位：$1.1 \times 10^{-4}$ – $1.6 \times 10^{-3}$）

### Lagrangian Neural ODE 训练效果

- 设置 (iii)（存在 Lagrangian）：$\mathcal{L}_R$ 收敛到与 baseline (i) 相同水平，Helmholtz 正则化不降低拟合质量
- 设置 (ii)（不存在 Lagrangian）：$\mathcal{L}_R$ 显著更差，可用于判别系统是否有 Lagrangian

### 定量改进（MSE ratio $R$）

- 位置 $x$：正则化后 MSE 有显著改善
- 速度 $\dot{x}$ 和加速度 $\ddot{x}$：改善更加显著
- **外推性能**：在两倍训练时间区间内，正则化模型显著优于 baseline
- 所有改善均通过 Welch's t-test 统计显著

## Limitations

1. **实验规模有限**：仅在 toy systems（振荡器、Kepler）上验证，缺乏复杂真实系统的测试
2. **缺少与 LNNs/HNNs 的定量对比**：作者明确指出与 Lagrangian Neural Networks 和 Hamiltonian Neural Networks 的全面比较仍在进行中
3. **高维扩展性未验证**：仅测试了 2D 系统，高维系统中 Helmholtz 条件的计算开销和有效性未知
4. **正则化强度调节**：梯度裁剪阈值 $c_1 \approx 0.05$ 和学习率的选择需要手动调节，缺乏自适应机制
5. **Lagrangian 恢复不完整**：只能恢复 Lagrangian 的 Hessian $g$，而非完整的 Lagrangian 函数
6. **非 Lagrangian 系统的判别阈值**：没有给出明确的判别阈值，判断是否存在 Lagrangian 仍依赖于定性的收敛行为观察

## My Notes

**创新点评价**：这篇文章的核心想法非常优雅——将经典力学中的 Helmholtz 条件（一个存在性判据）转化为可微的 metric 用于正则化。这是 physics-informed ML 中一条比较新颖的路线，不同于 LNNs/HNNs 的"by construction"策略，而是采用"by regularization"策略，灵活性更强。

**方法论亮点**：
- 用最小特征值归一化残差来避免 $g$ 的退化解，这个技巧很关键且设计精巧
- 零推理开销是重要的实际优势，因为 LNNs 需要在推理时计算 Euler-Lagrange 方程的自动微分

**局限性思考**：
- 目前验证仅限于简单 toy systems，距离实际应用（如分子动力学、天体力学模拟）还有距离
- 与 LNNs 的对比缺失是较大遗憾，论文读起来更像一个 workshop paper 或 extended abstract

**潜在延伸方向**：
- 将 Helmholtz metrics 扩展到 PDE（偏微分方程）系统
- 与 Neural Operator 结合用于场论中的变分问题
- 利用 Helmholtz metric 的收敛/不收敛性作为 **系统是否封闭** 的自动检测器

## 评分

- 新颖性: ⭐⭐⭐⭐ — Helmholtz 条件的可微化和正则化应用是新颖方向
- 实验充分度: ⭐⭐ — 仅 toy systems，缺少与主要 baseline 的定量对比
- 写作质量: ⭐⭐⭐⭐ — 数学推导清晰，物理直觉解释到位
- 价值: ⭐⭐⭐ — 方法优雅但实验验证不足，需更多后续工作支撑
