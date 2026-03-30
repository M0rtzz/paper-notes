<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧮 科学计算

**🧠 NeurIPS2025** · 共 **10** 篇

**[Bayesian Surrogates for Risk-Aware Pre-Assessment of Aging Bridge Portfolios](bayesian_surrogates_for_risk-aware_pre-assessment_of_aging_bridge_portfolios.md)**

:   提出基于贝叶斯神经网络（BNN）的代理模型，用于替代昂贵的非线性有限元分析（NLFEA），实现对老化桥梁组合的快速、不确定性感知的结构安全预评估，在真实铁路案例中为单座桥梁节省约37万美元。

**[Collapsing Taylor Mode Automatic Differentiation](collapsing_taylor_mode_automatic_differentiation.md)**

:   提出 Taylor mode 自动微分的"折叠"(collapsing)优化技术，通过重写计算图将导数求和操作向上传播，大幅加速 PDE 算子（如 Laplacian、一般线性 PDE 算子）的计算，实现速度优于嵌套反向传播同时保持前向模式的低内存优势。

**[DeltaPhi: Physical States Residual Learning for Neural Operators in Data-Limited PDE Solving](deltaphi_physical_states_residual_learning_for_neural_operators_in_data-limited_.md)**

:   提出 DeltaPhi 框架：不直接学习 PDE 的输入→输出映射，而是学习**相似物理状态之间的残差**，利用物理系统稳定性实现隐式数据增强，在数据稀缺场景下显著提升各类神经算子的性能。

**[Eddyformer Accelerated Neural Simulations Of Three-Dimensional Turbulence At Sca](eddyformer_accelerated_neural_simulations_of_three-dimensional_turbulence_at_sca.md)**

:   提出 EddyFormer，一种基于谱元法 (SEM) 的 Transformer 架构，将流场分解为 LES（大尺度）和 SGS（小尺度）两路并行流，在 256³ 分辨率 3D 湍流上达到 DNS 级精度且加速 30 倍，并在未见的 4× 更大域上泛化良好。

**[Enforcing Governing Equation Constraints in Neural PDE Solvers via Training-free Projections](enforcing_governing_equation_constraints_in_neural_pde_solvers_via_training-free.md)**

:   提出两种无需训练的后处理投影方法（非线性LBFGS优化和局部线性化投影），将神经PDE求解器的输出投影到满足控制方程约束的可行流形上，在Lorenz/KS/Navier-Stokes上大幅降低约束违反并提升精度，且效果显著优于physics-informed训练。

**[F-Adapter: Frequency-Adaptive Parameter-Efficient Fine-Tuning in Scientific Machine Learning](f-adapter_frequency-adaptive_parameter-efficient_fine-tuning_in_scientific_machi.md)**

:   本文首次系统研究了科学机器学习中预训练大型算子模型(LOM)的参数高效微调(PEFT)，发现 LoRA 在傅里叶层中存在深度放大的近似误差下界，而 Adapter 保留了通用逼近能力；据此提出频率自适应 Adapter（F-Adapter），按频谱能量分配 Adapter 容量，在 3D Navier-Stokes 预测任务上仅调参不到 2% 即达到 SOTA。

**[Inc An Indirect Neural Corrector For Auto-Regressive Hybrid Pde Solvers](inc_an_indirect_neural_corrector_for_auto-regressive_hybrid_pde_solvers.md)**

:   提出间接神经校正器(INC)，将学习到的校正项嵌入PDE的右端项（而非直接修改状态），理论证明误差放大降低$\mathcal{O}(\Delta t^{-1}+L)$倍，在6个PDE系统（1D混沌到3D湍流）上大幅改善长期轨迹性能（R²提升达158.7%），实现最高330×加速。

**[Integration Matters for Learning PDEs with Backward SDEs](integration_matters_for_learning_pdes_with_backward_sdes.md)**

:   揭示了标准 BSDE 方法性能不如 PINNs 的根本原因是 Euler-Maruyama 积分引入的不可消除离散化偏差，提出基于 Stratonovich 形式的 Heun-BSDE 方法彻底消除该偏差，在高维 PDE 上与 PINNs 竞争。

**[Neuro-Spectral Architectures for Causal Physics-Informed Networks](neuro-spectral_architectures_for_causal_physics-informed_networks.md)**

:   NeuSA 将经典谱方法与 Neural ODE 结合，先将 PDE 投影到谱基（Fourier）上得到 ODE 系统，再用 NODE 学习动力学演化，从架构层面解决了传统 PINN 的谱偏差和因果性问题，在波动方程/Burgers方程/sine-Gordon方程上误差比 baseline 低 1-2 个数量级且训练更快。

**[Stable Minima of ReLU Neural Networks Suffer from the Curse of Dimensionality: The Neural Shattering Phenomenon](stable_minima_of_relu_neural_networks_suffer_from_the_curse_of_dimensionality_th.md)**

:   本文研究了两层过参数化 ReLU 网络中稳定极小值（flat minima）的泛化性质，证明虽然平坦性确实蕴含泛化，但其收敛速率随输入维度指数级恶化（即存在维度灾难），与不受维度灾难影响的低范数解（weight decay）形成指数级分离；并揭示了"neural shattering"现象作为高维失败的几何机制。
