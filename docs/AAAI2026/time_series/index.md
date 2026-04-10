<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📈 时间序列

**🤖 AAAI2026** · 共 **18** 篇

**[A Unified Shape-Aware Foundation Model for Time Series Classification](a_unified_shape-aware_foundation_model_for_time_series_class.md)**

:   提出 UniShape——一个面向时间序列分类的基础模型，通过 shape-aware adapter 自适应聚合多尺度判别性子序列（shapelet），并结合原型对比预训练在实例和 shape 两个层面学习可迁移的 shapelet 表示，在 128 个 UCR 数据集上以 3.1M 参数达到 SOTA（平均准确率 87.08%），同时提供良好的分类可解释性。

**[AirDDE: Multifactor Neural Delay Differential Equations for Air Quality Forecasting](airdde_multifactor_neural_delay_differential_equations_for_air_quality_forecasti.md)**

:   首个将神经延迟微分方程（NDDE）引入空气质量预测的框架，通过记忆增强注意力模块和物理引导的延迟演化函数，对污染物连续时间传播中的延迟效应进行建模，在三个数据集上平均 MAE 降低 8.79%。

**[Beyond Observations Reconstruction Error-Guided Irregularly Sampled Time Series ](beyond_observations_reconstruction_error-guided_irregularly_sampled_time_series_.md)**

:   提出 iTimER，利用模型自身的重建误差分布作为学习信号——从观测点估计误差分布后采样生成未观测时刻的伪观测值，通过 Wasserstein 距离对齐观测/伪观测区域的误差分布 + 对比学习，在不规则采样时序的分类、插值、预测任务上全面超越 SOTA。

**[C3Rl Rethinking The Combination Of Channel-Independence And Channel-Mixing From ](c3rl_rethinking_the_combination_of_channel-independence_and_channel-mixing_from_.md)**

:   提出 C3RL，基于 SimSiam 对比学习框架将通道独立（CI）和通道混合（CM）策略视为同一数据的两个转置视图构建正样本对，通过孪生网络联合表示学习和预测学习，将 CI 模型的最佳性能率从 43.6% 提升到 81.4%，CM 模型从 23.8% 提升到 76.3%。

**[Coherent Multi-Agent Trajectory Forecasting in Team Sports with CausalTraj](coherent_multi-agent_trajectory_forecasting_in_team_sports_with_causaltraj.md)**

:   提出CausalTraj——一种时序因果、基于似然的多智能体轨迹预测模型，通过逐步自回归建模智能体间时空交互，在NBA、篮球和橄榄球数据集上实现了联合指标（minJADE/minJFDE）的最优结果，同时保持有竞争力的单智能体精度。

**[Cometnet Contextual Motif-Guided Long-Term Time Series Forecasting](cometnet_contextual_motif-guided_long-term_time_series_forecasting.md)**

:   提出 CometNet，通过从完整历史序列中提取循环出现的"上下文 motif"构建 motif 库，再用 motif 引导的 MoE 架构动态关联当前窗口与相关motif进行预测，突破了有限回看窗口的感受野瓶颈，在8个数据集上显著超越 TimeMixer++、iTransformer 等 SOTA。

**[Counterfactual Explainable AI (XAI) Method for Deep Learning-Based Multivariate Time Series Classification](counterfactual_explainable_ai_xai_method_for_deep_learning-based_multivariate_ti.md)**

:   提出 CONFETTI，一种面向多变量时间序列（MTS）分类的多目标反事实解释方法，通过结合类激活图（CAM）引导的子序列提取与 NSGA-III 多目标优化，在预测置信度、稀疏性和接近度三个目标间实现最优平衡，在 7 个 UEA 数据集上全面超越现有方法。

**[Deepboots Dual-Stream Residual Boosting For Drift-Resilient Time-Series Forecast](deepboots_dual-stream_residual_boosting_for_drift-resilient_time-series_forecast.md)**

:   提出 DeepBooTS，通过偏差-方差分解理论证明加权集成可降低方差从而缓解概念漂移，设计双流残差递减 boosting 架构，每个 block 的输出修正前一个 block 的残差，在多个数据集上平均提升 15.8%。

**[Finding Time Series Anomalies using Granular-ball Vector Data Description](finding_time_series_anomalies_using_granular-ball_vector_data_description.md)**

:   提出 Granular-ball One-Class Network (GBOC)，通过在潜在空间中自适应构建密度引导的粒球向量数据描述 (GVDD)，取代传统聚类或单一超球体假设，实现对时间序列正常行为的灵活建模和鲁棒异常检测。

**[IdealTSF: Can Non-Ideal Data Contribute to Enhancing Time Series Forecasting?](idealtsf_can_non-ideal_data_contribute_to_enhancing_the_performance_of_time_seri.md)**

:   提出 IdealTSF 框架，通过三阶段渐进式设计——负样本预训练（用稳定分布+多尺度噪声+结构删除模拟非理想数据）、正样本训练（混合平滑插值修复数据）、ECOS 优化器（对抗扰动引导到平坦极值）——使基础 attention 模型在含噪声/缺失的时序数据上获得约 10% 的性能提升。

**[Interpreting Fedspeak with Confidence: A LLM-Based Uncertainty-Aware Framework Guided by Monetary Policy Transmission Paths](interpreting_fedspeak_with_confidence_a_llm-based_uncertainty-aware_framework_gu.md)**

:   提出基于 LLM 的 uncertainty-aware 框架解读 Fedspeak（美联储语言）：通过货币政策传导路径的领域推理增强输入，引入 dynamic uncertainty decoding 模块量化预测置信度（Perceptual Uncertainty = Environmental Ambiguity × Cognitive Risk），在 FOMC 政策立场分析任务上达到 SOTA。

**[Loretta A Low Resource Framework To Poison Continuous Time Dynamic Graphs](loretta_a_low_resource_framework_to_poison_continuous_time_dynamic_graphs.md)**

:   提出 LoReTTA，一种无需代理模型的两阶段对抗投毒攻击框架：先通过 16 种时序重要性度量稀疏化高影响力边，再用保度数负采样算法替换对抗边，在 4 个数据集 × 4 个 TGNN 模型上平均降低 29.47% 性能，同时逃避 4 种异常检测系统且抵御 4 种防御方法。

**[M2Fmoe Multi-Resolution Multi-View Frequency Mixture-Of-Experts For Extreme-Adap](m2fmoe_multi-resolution_multi-view_frequency_mixture-of-experts_for_extreme-adap.md)**

:   提出 M2FMoE，通过傅里叶和小波双视角的频域混合专家建模常规与极端模式，结合跨视角共享频段分割器对齐两域语义、多分辨率自适应融合捕获多尺度信息、时序门控整合长短期特征，在 5 个水文极端事件数据集上无需极端事件标签即超越所有 SotA（含使用标签的方法），平均 RMSE 提升 22.3%。

**[Mask the Redundancy: Evolving Masking Representation Learning for Multivariate Time-Series Clustering](mask_the_redundancy_evolving_masking_representation_learning_for_multivariate_ti.md)**

:   提出 EMTC 框架，通过 Importance-aware Variate-wise Masking (IVM) 动态屏蔽冗余时间戳，结合 Multi-Endogenous Views (MEV) 多视图生成与 cluster-guided contrastive learning，在 15 个 MTS 聚类基准上平均 F1 提升 4.85%。

**[Optimal Look-back Horizon for Time Series Forecasting in Federated Learning](optimal_look-back_horizon_for_time_series_forecasting_in_federated_learning.md)**

:   提出联邦学习场景下时间序列预测的最优 look-back horizon 理论框架：通过 Synthetic Data Generator (SDG) 建模 non-IID 客户端数据，构建 intrinsic representation space，证明预测损失可分解为 Bayesian loss（随 $H$ 递减并饱和）和 approximation loss（随 $H$ 递增），最优 horizon $H^*$ 为 Bayesian loss 开始饱和的最小值。

**[SELDON: Supernova Explosions Learned by Deep ODE Networks](seldon_supernova_explosions_learned_by_deep_ode_networks.md)**

:   提出SELDON，一种结合masked GRU-ODE编码器、隐式Neural ODE传播器和可解释高斯基函数解码器的连续时间VAE，用于稀疏、不规则采样的天文光变曲线预测，在仅观测20%数据时即可超越基线方法做出准确的多波段通量预测。

**[Sonnet Spectral Operator Neural Network For Multivariable Time Series Forecastin](sonnet_spectral_operator_neural_network_for_multivariable_time_series_forecastin.md)**

:   提出 Sonnet，通过可学习小波变换将输入映射到时频域，引入基于谱相干性的多变量注意力（MVCA）建模变量间依赖关系，并利用 Koopman 算子进行稳定的时间演化预测，在 47 个预测任务中的 34 个取得最优，平均 MAE 降低 2.2%。

**[Urban Incident Prediction with Graph Neural Networks: Integrating Government Ratings and Crowdsourced Reports](urban_incident_prediction_with_graph_neural_networks_integrating_government_rati.md)**

:   提出 URBAN（多视图多输出GNN模型），联合利用稀疏但无偏的政府检查评级数据和密集但有偏的众包报告数据来预测城市事件的真实潜在状态，在纽约市960万+报告和100万+检查数据上验证，预测相关性比仅用报告数据高5.3倍。
