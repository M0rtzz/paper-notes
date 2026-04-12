---
title: >-
  [论文解读] Sharp Monocular View Synthesis in Less Than a Second
description: >-
  [ICLR 2026][3D视觉][单目视图合成] 提出SHARP——从单张照片在不到1秒内通过单次前馈回归度量3D高斯表示→支持100+FPS实时高分辨率渲染→在多个数据集上零样本泛化LPIPS降低25-34%/DISTS降低21-43%/合成速度比扩散方法快1000倍，设定了单目视图合成的新SOTA。
tags:
  - ICLR 2026
  - 3D视觉
  - 单目视图合成
  - 3D高斯
  - 前馈
  - 度量尺度
  - 实时渲染
---

# Sharp Monocular View Synthesis in Less Than a Second

**会议**: ICLR 2026  
**arXiv**: [2512.10685](https://arxiv.org/abs/2512.10685)  
**代码**: [GitHub](https://github.com/apple/ml-sharp)  
**领域**: 3D视觉/视图合成  
**关键词**: 单目视图合成, 3D高斯, 前馈, 度量尺度, 实时渲染

## 一句话总结

提出SHARP——从单张照片在不到1秒内通过单次前馈回归度量3D高斯表示→支持100+FPS实时高分辨率渲染→在多个数据集上零样本泛化LPIPS降低25-34%/DISTS降低21-43%/合成速度比扩散方法快1000倍，设定了单目视图合成的新SOTA。

## 研究背景与动机

1. **领域现状**：从单张照片合成附近视角→AR/VR应用核心。现有方法：(1)多图+逐场景优化(NeRF/3DGS)→慢; (2)扩散方法→质量好but秒级合成→不够交互。

2. **现有痛点**：
   - (1) 前馈3D单目方法→保真度不如扩散方法
   - (2) 扩散方法→合成时间秒/分钟级→不支持交互浏览
   - (3) 度量尺度→多数方法不输出绝对尺度→不能与物理设备耦合

3. **切入角度**：极致工程的前馈→规模+精心设计=超越所有先前方法→速度和质量双赢。

## 方法详解

### SHARP架构

- 输入：单张照片
- 输出：度量3D高斯表示(带绝对尺度)
- 过程：单次前馈→<1秒(A100)

### 关键组件

1. **高分辨率3D高斯回归网络**：
   - 多模块但端到端训练
   - 回归每个像素的高斯参数(位置/方向/尺度/颜色/透明度)

2. **精心设计的损失配置**：
   - 优先合成视图精度
   - 正则化去除常见伪影

3. **学习深度调整模块**：
   - 训练时→真实深度估计可能不准
   - 学习额外调整层→缓解深度误差对视图合成监督的影响

4. **度量尺度**：
   - 输出绝对尺度→支持与AR/VR头显的物理相机耦合

### 渲染

- 3D高斯表示→rasterization→100+ FPS高分辨率渲染

## 实验关键数据

### 零样本跨数据集(ScanNet++/RealEstate10k/ACID)

| 方法 | LPIPS↓ | DISTS↓ | 合成时间 |
|------|--------|--------|---------|
| Flash3D | 基线 | 基线 | ~0.3s |
| Gen3C(扩散) | 较好 | 较好 | ~60s |
| ViewCrafter(扩散) | 好 | 好 | ~30s |
| **SHARP** | **-25~34%** | **-21~43%** | **<1s** |

### 关键发现

- SHARP在保真度上超越扩散方法→同时快1000x→帕累托前沿
- 零样本泛化→未见数据集上依然SOTA→规模训练的泛化优势
- 度量尺度→准确耦合物理设备→AR/VR可用
- 视觉质量→锐利细节+精细结构→比"模糊"的前馈方法好很多

## 亮点与洞察

- **"规模+工程=SOTA"**：没有革命性架构创新→但规模+精心设计→超越所有方法→工程的力量。
- **"<1秒+100FPS"的实用意义**：个人照片3D化→浏览→发送给好友→<1秒生成+实时渲染→用户体验可行。
- **前馈>>扩散(在此任务上)**：视图合成≠图像生成→不需要创造新内容→只需几何准确→前馈天然更合适。
- **Apple的工程品质**：代码开源→可复现→工业级质量。


## 局限性 / 可改进方向

- We presented SHARP, an approach to real-time photorealistic rendering of nearby views from a single photograph.

- SHARP synthesizes a 3D Gaussian representation via a single forward pass through a neural network in less than a second on a standard GPU.

- This 3D representation can then be rendered in real time at high resolution from nearby views.

- Our experiments demonstrate that SHARP delivers state-of-the-art image fidelity for nearby view synthesis, outperforming recent approaches that are in some cases two to three orders of magnitude more computationally intensive.

- One clear opportunity for future work is to extend the methodology to support photorealistic synthesis of faraway views without compromising the fidelity of nearby views or the benefits of fast interactive synthesis.


## 相关工作与启发

- **vs Williams**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs QuickTime VR**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs Depth Images**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

- **vs View Synthesis**: 本文在此基础上提出了不同的技术路线，在关键指标上取得了改进。

## 评分

- 新颖性: ⭐⭐⭐ 技术创新适中但工程集成excellent
- 实验充分度: ⭐⭐⭐⭐⭐ 多数据集+多度量+与扩散/前馈全对比
- 写作质量: ⭐⭐⭐⭐ 清晰展示了关键设计选择
- 价值: ⭐⭐⭐⭐⭐ 对单目3D视图合成有SOTA级贡献+实际可部署
