# EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**代码**: 待确认
**领域**: 3d_vision
**关键词**: event camera, 3D geometry estimation, low-light, pointmap, dynamic reconstruction

## 一句话总结

EAG3R 将事件相机的异步事件流融入 MonST3R 点图重建框架，通过 Retinex 增强 + SNR 感知融合 + 事件光度一致性损失，在极端低光动态场景下实现鲁棒的深度估计、位姿跟踪和 4D 重建。

## 背景与动机

- DUSt3R/MonST3R 利用 Transformer 直接回归稠密 pointmap 实现 pose-free 三维重建，但完全依赖 RGB 图像
- 在夜间驾驶等极端低光 + 快速运动场景下，RGB 图像严重欠曝/模糊，导致特征退化、光流估计失? EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**代??
**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**??*arXiv**: [2512.00771]?*代码**: 待确认
**领域**: 3d_vision
**关键词*?*领域**: 3d_visio??**关键词**: even???## 一句话总结

EAG3R 将事件相机的异步事件流融入 MonST3R 点图重建框架???
EAG3R 将事件???
## 背景与动机

- DUSt3R/MonST3R 利用 Transformer 直接回归稠密 pointmap 实现 pose-free 三维重建，但完全依赖 RGB 图像
- 在夜间驾驶等极端低光 + 快速运动场景下，RGB 图像严重欠曝/模糊，}}^
- DUSt3R/MonST3R\te- 在夜间驾驶等极端低光 + 快速运动场景下，RGB 图像严重欠曝/模糊，导致特征退化、光流估 =
**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**代??
**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**??*arXiv**: [2512.00771]?*代砼?高 SNR → 图像可靠?*代??
**会议**: NeurIPS 2025
**arXiv**: [2512.0077??**会议? **arXiv**: [2512.00771]ma**??*arXiv**: [2512.00771]?*代码**: 待确认
rmer ?*领域**: 3d_vision
**关键词*?*领域**: 3vt}**关键?1}^4$
- 从
EAG3R 将事件相机的异步事件流融入 MonST3R 点图重建框架?}^tEAG3R 将事件???
## 背景与动机

- DUSt3R/MonST3R 利用 Transformer ??# 背景与动机t},l} = \text{CrossAtt- 在夜?ext{evt},l}^t,\; K=F_{\text{img},l}^t,\; V=F_{\text{img},l}^t)$$

图像编码器保持冻结，仅训练事件 A- DUSt3R/MonST3R\te- 在夜间驾驶?合

将图像最终特征与事件最终特征按 SNR 权**会议**: NeurIPS 2025
**arXiv**: [2512.00771](https://arxiv.org/abs/2512.00771)
**代??
**会议**: NeurIPS 2025
**arXiv**: [2512.00771] (**arXiv**: [2512.00771]\text{snr}}^t))$$

高 SNR 区域偏重图像特征，低 SN**会讟?*arXiv**: [2512.00771]??**??*arXiv**: [2512.00771]?*代砼?高 SNR → 图僦?*会议**: NeurIPS 2025
**arXiv**: [2512.0077??**会议? **arXiv**: [251 ?*arXiv**: [2512.0077???mer ?*领域**: 3d_vision
**关键词*?*领域**: 3vt}**关键?1}^4$
- 从
EAG3R 将事件相机的异x_j,y_j) \in \mathcal{P}_m} p_j \delta(u - u_j)$
- **来自图像梯度+运?AG3**## 背景与动机

- DUSt3R/MonST3R 利用 Transformer ??# 背景与动机t},l} = \text{CrossA{\
- DUSt3R/MonST3R\De
图像编码器保持冻结，仅训练事件 A- DUSt3R/MonST3R\te- 在夜间驾驶?合

将图像最终特征与事件最终特征按 SNR 权**会议cal
将图像最终特征与事件最终特征按 SNR 权**会议**: NeurIPS 2025
**arXivL_{\mathcal{P}_m}\|} - \frac{\Delta \hat{L}_{\mathcal{P}_m}(u)}{\|\Delta \hat{L}_**代??
**会议**: NeurIPS 2025
**arXiv**: [2512.0077??*
在 MonS**arXiv**: [2512.00771]??高 SNR 区域偏重图像特征，???失：

$$\mathcal{L}_{\te**arXiv**: [2512.0077??**会议? **arXiv**: [251 ?*arXiv**: [2512.0077???mer ?*领域**: 3d_vision
**关键词*?*领域**: 3vt}**关键?1}^4$
- 从
EL}**关键词*?*领域**: 3vt}**关键?1}^4$
- 从
EAG3R 将事件相机的异x_j,y_j) \in \mathcal ? 从
EAG3R 将事件相机的异x_j,y_j) \inVSEAG3ut- **来自图像梯度+运?AG3**## 背景与动机

- DUSt3R/MonST3R 利??
- DUSt3R/MonST3R 利用 Transformer ??# 背景与1-3- DUSt3R/MonST3R\De
图像编码器保持冻结，仅训练事件 A- DUSt3R/Mig图像编码器保--
将图像最终特征与事件最终特征按 SNR ?R | 0.407 | 0.393 | 0.463 | 0.335 |
将图像最终特征与事件最终特征按 SNR 权**会议**) **arXivL_{\mathcal{P}_m}\|} - \fra| **EAG3R** | **0.353** | **0.491** | **0.28**会议**: NeurIPS 2025
**arXiv**: [2512.0077??*
在 MonS**arXiv**: [2512.00771]??高 SNR 区?A**arXiv**: [2512.0077??
|在 --|---------|--------
$$\mathcal{L}_{\te**arXiv**: [2512.0077??*09 |
| MonST3R | 0.559 | 0.626 | 0.733 |
| MonST3R (Finetune) | 0.580 | 0.467 | 0.402 |
| **EAG3R** | **0.482** | **0.428** | **0.409** |

### 消融实验（Ni- 从
EL}**兰计）

| 配置 | Abs Rel↓ | ?L}*25- 从
EAG3R 将事件相机的异x_j,y_j) \in \melEAG3| EAG3R 将事件相+ Event | 0.297 | 0.518 |
| + Event + 
- DUSt3R/MonST3R 利??
- DUSt3R/MonST3R 利用 Transformer ??# 背景与1-3- DUSt3R/MonST3R\De
??- DUSt3R/MonST3R 利??图像编码器保持冻结，仅训练事件 A- DUSt3R/Mig图像编码????图像最终特征与事件最终特征按 SNR ?R | 0.407 | 0.393 | 0.463 ??将图像最终特征与事件最终特征按 SNR 权**会议**) **arXivL_{\mathcal{P}??*arXiv**: [2512.0077??*
在 MonS**arXiv**: [2512.00771]??高 SNR 区?A**arXiv**: [2512.0077??
|在 --|---------|--------
$$\mathcal{L}_{\te**arXiv**: [2512.0077??*??件相机硬件要求限制了实际部署范围
- 未讨论事件与 RGB 时间对齐的鲁棒性问题
- 全局优化中 H| MonST3R | 0.559 | 0.626 | 0.733 |
| MonST3?? MonST3R (F相关工作的对比

-| **EAG3nST3R**: EAG3R 增加事件模态，在
### 消融实验（Ni- 从
EL}**兰计）

| ?R**: 后者通过注意力做
| 配置 | A???AG3R 将事件相机的异x_j,y_j)??| + Event + 
- DUSt3R/MonST3R 利??
- DUSt3R/MonST3R 利用 Transformer ??# 背景与1-3- D??- DUSt3R/Mo v- DUSt3R/MonST3R 利?:??- DUSt3R/MonST3R 利??图像编码器保持冻结，仅训练事?S在 MonS**arXiv**: [2512.00771]??高 SNR 区?A**arXiv**: [2512.0077??
|在 --|---------|--------
$$\mathcal{L}_{\te**arXiv**: [2512.0077??*??件相机硬件要求限制了实际部署范围
- 未讨论事件与 RGB 时间对齐的鲁棒性问题
- 全局优化中 H| MonST3R | 0.559 | 0.62??|在 --|---------|-机引入 pointmap 重建范式
- ⭐ 实验充分度$$\mathcal{L}_{\te*EC 一个数据集，消融详细但场景有限
- ⭐ 写作质量: 4/5 — 方法描述清晰，公- 全局优化中 H| MonST3R | 0.559 | 0.626 | 0.733 |3D| Mo知有显著实用价值
