---
description: "【论文笔记】pySpatial: Generating 3D Visual Programs for Zero-Shot Spatial Reasoning 论文解读 | ICLR 2026 | arXiv 2603.00905 | 视觉编程 | 提出pySpatial——视觉编程框架让MLLM通过生成Python代码调用3D空间工具(重建/相机恢复/新视角渲染)实现零样本3D空间推理：将2D输入转化为可探索的3D场景→MLLM在结构化3D表示上显式推理而非隐式想象,在MindCube上超越GPT-4.1-mini 12.94%,并成功用于真实室内四足机器人导航。"
tags:
  - ICLR 2026
---

# pySpatial: Generating 3D Visual Programs for Zero-Shot Spatial Reasoning

**会议**: ICLR 2026  
**arXiv**: [2603.00905](https://arxiv.org/abs/2603.00905)  
**代码**: [项目页面](https://pySpatial.github.io)  
**领域**: 3D空间推理/视觉编程  
**关键词**: 视觉编程, 3D重建, 空间推理, 零样本, 机器人导航

## 一句话总结
提出pySpatial——视觉编程框架让MLLM通过生成Python代码调用3D空间工具(重建/相机恢复/新视角渲染)实现零样本3D空间推理：将2D输入转化为可探索的3D场景→MLLM在结构化3D表示上显式推理而非隐式想象,在MindCube上超越GPT-4.1-mini 12.94%,并成功用于真实室内四足机器人导航。

## 研究背景与动机

1. **领域现状**：MLLM在感知和2D推理上表现好→但3D空间推理(深度/视角变换/多视角关系)仍很弱→接近随机猜测级别。

2. **现有痛点**：
   - (1) MLLM训练数据缺少显式3D监督→无法学习可靠的语言-3D对应
   - (2) 现有方法(如认知地图)依赖MLLM隐式"想象"→有限且不可靠
   - (3) 单视角空间理解方法不处理多视角推理
   - (4) 需要微调→不能即插即用

3. **切入角度**：不让MLLM隐式推理3D→而是显式构建3D场景→让MLLM在3D场景上操作→视觉编程。

## 方法详解

### pySpatial框架

```
图像序列 + 语言查询 → MLLM生成Python代码 → 调用空间工具 → 获得3D视觉证据 → MLLM基于证据回答
```

### 空间工具API

1. **3D重建**：DUSt3R/VGGT等前馈3D重建→从稀疏视角恢复场景几何
2. **相机位姿恢复**：估计每个视角的相机参数
3. **新视角渲染**：在重建场景中从任意视角渲染
4. **相机变换**：平移/旋转/视角切换

### 工作流示例
查询："从视角3背后看有什么？"
```python
scene = reconstruct_3d(images)
camera = get_camera_pose(scene, view=3)
camera_behind = rotate_camera(camera, 180)
novel_view = render_view(scene, camera_behind)
answer = describe(novel_view)
```

### 关键特性
- **零样本**：无需微调→即插即用
- **可解释**：生成的代码可阅读→推理过程透明
- **通用**：适用于开源和闭源MLLM

## 实验关键数据

### MindCube基准(多视角空间推理)
| 方法 | 准确率 | 说明 |
|------|--------|------|
| GPT-4.1-mini直接 | ~40% | 隐式推理 |
| 认知地图(2D) | ~45% | 2D想象 |
| **pySpatial+GPT-4.1-mini** | **~53%** | +12.94% |
| **pySpatial+GPT-4o** | **更高** | 更强基座模型 |

### Omni3D-Bench
- pySpatial同样超越所有MLLM基线

### 真实世界室内导航
- 四足机器人使用pySpatial生成的路线规划
- 成功穿越复杂室内环境(多房间/走廊/障碍)

### 关键发现
- 显式3D推理>>隐式想象→差距巨大
- 新视角渲染是最有用的工具→揭示遮挡区域
- 生成的代码质量→与查询复杂度正相关→MLLM能组合工具
- 开源MLLM也能受益→但效果弱于GPT-4o

## 亮点与洞察
- **"用工具的AI > 用想象力的AI"**：在3D空间推理上→让MLLM用3D工具远好于让它"想象"→工具增强是正确方向。
- **视觉编程的3D扩展**：VisProg/ViperGPT用于2D→pySpatial首次用于3D空间推理→自然且强大的扩展。
- **真实机器人部署**：不只是学术基准→在真实四足机器人上验证→bridging simulation-to-real。
- **"3D重建天然是空间推理工具"**：DUSt3R等的能力被重新定位→不只是重建→而是MLLM的空间推理基础设施。

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 3D视觉编程框架的首次系统实现
- 实验充分度: ⭐⭐⭐⭐ 两个基准+真实机器人+定性分析
- 写作质量: ⭐⭐⭐⭐⭐ 框架清晰示例直观
- 价值: ⭐⭐⭐⭐⭐ 对MLLM空间推理有范式级推动
