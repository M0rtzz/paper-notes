<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧮 科学计算

**🤖 AAAI2026** · 共 **4** 篇

**[Just Few States are Enough: Randomized Sparse Feedback for Stability of Dynamical Systems](just_few_states_are_enough_randomized_sparse_feedback_for_stability_of_dynamical.md)**

:   提出随机稀疏反馈控制框架：控制器在每个时间步仅访问状态向量的随机子集，通过 LMI 联合设计反馈增益矩阵和 Bernoulli 稀疏化参数，在保证渐近均方稳定性（AMSS）的同时最小化所需传感器数量，实验中仅用 0.3% 的状态分量即可达到与全状态反馈可比的性能。

**[PhysicsCorrect: A Training-Free Approach for Stable Neural PDE Simulations](physicscorrect_a_training-free_approach_for_stable_neural_pde_simulations.md)**

:   提出 PhysicsCorrect，一种无需训练的校正框架，通过将 PDE 残差校正建模为线性化逆问题并预计算伪逆缓存，在推理时以 <5% 计算开销实现最高 100× 误差降低，适用于 FNO/UNet/ViT 等任意预训练神经算子。

**[Pimrl Physics-Informed Multi-Scale Recurrent Learning For Burst-Sampled Spatiote](pimrl_physics-informed_multi-scale_recurrent_learning_for_burst-sampled_spatiote.md)**

:   提出 PIMRL 框架，针对 burst 采样（短段高频+长间隔）的稀疏时空数据，结合宏观尺度潜空间推理和微观尺度物理校正的双模块架构，通过跨尺度消息传递融合信息，在 5 个 PDE 基准上将误差最多降低 80%。

**[Scientific Knowledge-Guided Machine Learning for Vessel Power Prediction: A Comparative Study](scientific_knowledge-guided_machine_learning_for_vessel_power_prediction_a_compa.md)**

:   提出物理基线+数据驱动残差的混合建模框架，将海试功率曲线（螺旋桨定律 $P=cV^n$）作为基线，用 XGBoost/NN/PINN 学习残差修正，在稀疏数据区域显著提升外推稳定性和物理一致性。
