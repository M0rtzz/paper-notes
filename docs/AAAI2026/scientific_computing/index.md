<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧮 科学计算

**🤖 AAAI2026** · 共 **3** 篇

**[PhysicsCorrect: A Training-Free Approach for Stable Neural PDE Simulations](physicscorrect_a_training-free_approach_for_stable_neural_pde_simulations.md)**

:   提出 PhysicsCorrect，一种无需训练的校正框架，通过将 PDE 残差校正建模为线性化逆问题并预计算伪逆缓存，在推理时以 <5% 计算开销实现最高 100× 误差降低，适用于 FNO/UNet/ViT 等任意预训练神经算子。

**[Pimrl Physics-Informed Multi-Scale Recurrent Learning For Burst-Sampled Spatiote](pimrl_physics-informed_multi-scale_recurrent_learning_for_burst-sampled_spatiote.md)**

:   提出 PIMRL 框架，针对 burst 采样（短段高频+长间隔）的稀疏时空数据，结合宏观尺度潜空间推理和微观尺度物理校正的双模块架构，通过跨尺度消息传递融合信息，在 5 个 PDE 基准上将误差最多降低 80%。

**[Scientific Knowledge-Guided Machine Learning for Vessel Power Prediction: A Comparative Study](scientific_knowledge-guided_machine_learning_for_vessel_power_prediction_a_compa.md)**

:   提出物理基线+数据驱动残差的混合建模框架，将海试功率曲线（螺旋桨定律 $P=cV^n$）作为基线，用 XGBoost/NN/PINN 学习残差修正，在稀疏数据区域显著提升外推稳定性和物理一致性。
