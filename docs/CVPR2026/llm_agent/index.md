<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🦾 LLM Agent

**📷 CVPR2026** · 共 **9** 篇

**[GUI-CEval: A Hierarchical and Comprehensive Chinese Benchmark for Mobile GUI Agents](gui-ceval_a_hierarchical_and_comprehensive_chinese_benchmark_for_mobile_gui_agen.md)**

:   提出 GUI-CEval，首个面向中文移动端 GUI Agent 的综合评测基准，覆盖 201 个主流中文 App、4 种设备类型，采用"基础能力+应用能力"两层结构从感知、规划、反思、执行、评估五个维度进行细粒度诊断，在 20 个代表性模型上的实验揭示当前模型在反思和自我评估方面仍有明显短板。

**[HATS: Hardness-Aware Trajectory Synthesis for GUI Agents](hats_hardnessaware_trajectory_synthesis_gui_agent.md)**

:   提出HATS框架，通过定义动作的"语义模糊度"作为难度信号，以难度驱动探索+对齐引导修复的闭环管线合成高质量GUI轨迹数据，显著提升agent泛化能力。

**[Nerfify: A Multi-Agent Framework for Turning NeRF Papers into Code](nerfify_a_multi-agent_framework_for_turning_nerf_papers_into_code.md)**

:   提出 Nerfify，通过上下文无关文法(CFG)约束、图思维链(GoT)代码合成、组合式引用恢复和视觉反馈四阶段，将NeRF论文自动转化为可训练的Nerfstudio插件，在30篇论文基准上达到100%可执行率（通用基线仅5%），视觉质量在专家实现的±0.5dB PSNR内。

**[Realm An Mllm-Agent Framework For Open World 3D Reasoning Segmentation And Editi](realm_an_mllm-agent_framework_for_open_world_3d_reasoning_segmentation_and_editi.md)**

:   提出 REALM 框架，通过 MLLM agent 对 3D 高斯泼溅(3DGS)渲染的视图进行推理分割，设计全局-局部空间接地策略(GLSpaG)聚合多视角MLLM推理结果，在隐式指令下的3D分割中大幅超越现有方法（LERF上mIoU 92.88% vs 基线44.82%），并支持3D编辑。

**[REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting](realm_mllm_agent_3d_reasoning_gaussian.md)**

:   提出 REALM，一个基于 MLLM-Agent 的开放世界 3D 推理分割框架，利用 3DGS 渲染新视角供 MLLM 理解复杂指令，通过全局到局部空间定位策略实现精确 3D 分割——无需 3D 特定后训练即可处理隐式推理指令，并支持物体移除、替换和风格迁移等 3D 交互任务。

**[Sceneassistant A Visual Feedback Agent For Open-Vocabulary 3D Scene Generation](sceneassistant_a_visual_feedback_agent_for_open-vocabulary_3d_scene_generation.md)**

:   提出 SceneAssistant，通过为VLM agent提供完整的原子操作API集（13种动作涵盖物体管理、6-DoF操作、相机控制）和纯视觉反馈闭环，实现开放词汇的文本到3D场景生成，在人类评估中布局正确性和物体质量均大幅优于Holodeck和SceneWeaver。

**[SceneAssistant: A Visual Feedback Agent for Open-Vocabulary 3D Scene Generation](sceneassistant_a_visual_feedback_agent_for_openvoc.md)**

:   提出基于视觉反馈的VLM agent框架，通过14个完备Action API让VLM在ReAct闭环中迭代优化3D场景布局，无需预定义空间关系模板，在人类评估中Layout得分7.600（vs SceneWeaver 5.800），Human Preference 65%。

**[Think, Then Verify: A Hypothesis-Verification Multi-Agent Framework for Long Video Understanding](think_then_verify_a_hypothesis-verification_multi-agent_framework_for_long_video.md)**

:   提出 VideoHV-Agent，将长视频问答重新建模为"假设-验证"过程：Thinker 将答案选项改写为可测试假设，Judge 提取区分性线索，Verifier 在视频中定位证据进行验证，Answer 综合证据给出最终答案，在 EgoSchema/NextQA/IntentQA 三个基准上取得 SOTA，同时推理效率优于现有 Agent 方法。

**[Watch and Learn: Learning to Use Computers from Online Videos](watch_and_learn_computer_use_from_videos.md)**

:   提出 Watch & Learn 框架, 通过逆动力学模型 (IDM) 将 YouTube 教程视频自动转化为可执行的 UI 轨迹数据 (53K+ 轨迹, 免去人工标注), 基于此数据增强 CUA 能力, 在 OSWorld 上让 Qwen 2.5VL-7B 提升 +11.1%, UI-TARS-1.5-7B 提升 +3.8%.
