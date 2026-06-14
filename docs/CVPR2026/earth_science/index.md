---
title: >-
  CVPR2026 地球科学论文汇总 · 3篇论文解读
description: >-
  3篇CVPR2026的地球科学方向论文解读，涵盖异常检测、多模态等方向。覆盖该方向前沿研究进展与技术创新，每篇含一句话总结、核心思想、方法详解、实验结果与局限性分析，5分钟读懂一篇论文核心思想，助你快速跟进AI领域最新研究动态、学术前沿趋势与核心技术突破。
tags:
  - "CVPR2026"
  - "地球科学"
  - "论文解读"
  - "论文笔记"
  - "异常检测"
  - "多模态"
item_list:
  - u: "geochemad_benchmarking_unsupervised_geochemical_anomaly_detection_for_mineral_ex/"
    t: "GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration"
  - u: "meteorpred_a_meteorological_multimodal_large_model_and_dataset_for_severe_weathe/"
    t: "MeteorPred: A Meteorological Multimodal Large Model and Dataset for Severe Weather Event Prediction"
  - u: "sigma_a_physics-based_benchmark_for_gas_chimney_understanding_in_seismic_images/"
    t: "SIGMA: A Physics-Based Benchmark for Gas Chimney Understanding in Seismic Images"
item_total: 3
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🌍 地球科学

**📷 CVPR2026** · **3** 篇论文解读

📌 **同领域跨会议浏览：** [🧪 ICML2026 (1)](../../ICML2026/earth_science/index.md) · [🤖 AAAI2026 (2)](../../AAAI2026/earth_science/index.md) · [🧠 NeurIPS2025 (6)](../../NeurIPS2025/earth_science/index.md) · [📷 CVPR2025 (1)](../../CVPR2025/earth_science/index.md) · [🎞️ ECCV2024 (1)](../../ECCV2024/earth_science/index.md)

**[GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration](geochemad_benchmarking_unsupervised_geochemical_anomaly_detection_for_mineral_ex.md)**

:   提出 GeoChemAD 开源基准数据集和 GeoChemFormer 框架，通过空间上下文学习与元素依赖建模实现无监督地球化学异常检测，在8个子集上平均 AUC 达到 0.7712。

**[MeteorPred: A Meteorological Multimodal Large Model and Dataset for Severe Weather Event Prediction](meteorpred_a_meteorological_multimodal_large_model_and_dataset_for_severe_weathe.md)**

:   本文构建了首个大规模灾害天气预警多模态数据集 MP-Bench（42 万对 ERA5 气象场+预警文本），并提出能直接吃 4D 气象张量的多模态大模型 MMLM——通过三个分别作用于时间、空间、垂直气压层的即插即用融合模块，把高维气象数据对齐到 LLM 生成自然语言预警。

**[SIGMA: A Physics-Based Benchmark for Gas Chimney Understanding in Seismic Images](sigma_a_physics-based_benchmark_for_gas_chimney_understanding_in_seismic_images.md)**

:   本文提出首个带真值标注的物理合成地震图像数据集 SIGMA——用波动方程正演+逆时偏移把含气烟囱的速度模型转成地震图像，同时给出像素级气烟囱掩码（用于检测）和"退化—干净"配对图（用于增强），并在两类任务上 benchmark 多个基线，揭示现有方法在该数据上集体吃力。
