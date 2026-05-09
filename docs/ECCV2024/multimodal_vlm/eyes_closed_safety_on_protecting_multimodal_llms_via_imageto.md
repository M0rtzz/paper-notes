---
title: >-
  [论文解读] Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation
description: >-
  [ECCV 2024][多模态][MLLM安全] 发现MLLM虽易受图像输入的越狱攻击但具备内省能力（能检测自身不安全回复）、且去除图像后安全机制恢复，据此提出ECSO——通过自检不安全回复后将图像转为query-aware文本描述来恢复预对齐LLM的固有安全机制，无需额外训练即可大幅提升安全性。
tags:
  - ECCV 2024
  - 多模态
  - 多模态VLM
  - 越狱攻击防护
  - 图像到文本转换
  - 训练无关方法
  - 安全对齐
---

# Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation

**会议**: ECCV 2024  
**arXiv**: [2403.09572](https://arxiv.org/abs/2403.09572)  
**代码**: [https://gyhdog99.github.io/projects/ecso/](https://gyhdog99.github.io/projects/ecso/)  
**领域**: 多模态VLM  
**关键词**: MLLM安全, 越狱攻击防护, 图像到文本转换, 训练无关方法, 安全对齐

## 一句话总结
发现MLLM虽易受图像输入的越狱攻击但具备内省能力（能检测自身不安全回复）、且去除图像后安全机制恢复，据此提出ECSO——通过自检不安全回复后将图像转为query-aware文本描述来恢复预对齐LLM的固有安全机制，无需额外训练即可大幅提升安全性。

## 研究背景与动机
1. **领域现状**：MLLM（如LLaVA、Qwen-VL等）在视觉理解上取得突破，它们建立在已经进行安全对齐的LLM之上。但引入图像输入后，MLLM变得容易被恶意查询诱导生成有害内容。
2. **现有痛点**：(1) 重新做RLHF/SFT安全对齐成本高且需要精心设计红队查询；(2) 手工制作系统提示（"你不能做X"）对新攻击无效；(3) 外部安全检测器需要额外训练和大量数据。
3. **核心矛盾**：LLM已经过安全对齐，但图像特征的引入改变了嵌入空间分布，"压制"了安全机制。问题是：能否把已有的安全机制"激活"，而非从头重新训练？
4. **本文要解决什么？** (1) 验证MLLM是否仍保留原LLM的安全能力；(2) 设计无训练的保护策略利用这些残存的安全能力；(3) 在保持实用性的同时提升安全性。
5. **切入角度**：两个关键观察——(a) 去掉图像后MLLM的harmless rate从~20%恢复到~100%；(b) MLLM虽会生成不安全回复，但能以>95%准确率判断自身回复是否安全。
6. **核心idea一句话**：先让MLLM自检回复安全性，若不安全则将图像转为query-aware文本描述后重新作答（"闭眼"激活LLM安全机制）。

## 方法详解

### 整体框架
ECSO包含4个步骤：(1) 正常生成初始回复 $\tilde{y} = F_\theta(v, x)$；(2) 自检回复安全性 $s = F_\theta(v, P_{det}(x, \tilde{y}))$；(3) 若不安全，做query-aware图像到文本转换 $c = F_\theta(v, P_{trans}(x))$；(4) 去除图像，用文本描述重新生成安全回复 $y = F_\theta(\text{null}, P_{gen}(c, x))$。

### 关键设计

1. **有害内容自检（Step 2）**：
    - 做什么：利用MLLM判断自身初始回复是否安全
    - 核心思路：设计detection prompt模板包装原始query和初始回复，让同一MLLM做安全/不安全二分类
    - 设计动机：Figure 2显示LLaVA-1.5-7B和ShareGPT4V-7B自检准确率>95%，且此能力不受图像输入影响。安全判别（discrimination）天然比安全生成（generation）容易
    - 关键：即使在图像存在时自检也很准确，不像安全生成那样被图像"压制"

2. **Query-aware图像到文本转换（Step 3）**：
    - 做什么：将图像信息转化为与原始问题相关的文本描述
    - 核心思路：prompt模板 $P_{trans}$ 包含原始问题，指示MLLM生成与问题相关的图像描述。这样caption保留了回答问题所需的关键信息
    - 设计动机：通用caption可能遗漏回答问题的关键细节。例如问"哪只大象在前面"需要caption提到位置关系，但通用描述可能不会提及

3. **去图像安全回复生成（Step 4）**：
    - 做什么：用文本描述替代图像，让MLLM（退化为纯LLM）重新回答
    - 核心思路：$y = F_\theta(\text{null}, P_{gen}(c, x))$，在prompt中加入"HARMLESS and ETHICAL"关键词进一步强调安全
    - 设计动机：去除图像后，嵌入空间恢复到LLM预对齐状态，安全机制自然恢复。图像中的恶意内容（如OCR文字、SD生成的误导图）转化为文本后暴露给安全LLM处理

### 损失函数 / 训练策略
**完全无需训练**。仅通过精心设计的prompt模板实现三步推理。此外，作者展示ECSO可作为数据引擎生成SFT安全对齐数据——收集ECSO的安全回复用于微调MLLM。

## 实验关键数据

### 主实验

| 攻击类型 | LLaVA-1.5-7B Direct | LLaVA-1.5-7B + ECSO | 提升 |
|---------|---------------------|---------------------|------|
| SD (图像) | 85.0% | 95.4% | +10.4 |
| OCR (文字图) | 31.7% | 90.3% | **+42.2** |
| SD+OCR | 32.1% | 86.4% | **+37.6** |
| VLSafe | 19.4% | 90.7% | **+71.3** |

### 消融实验

| 配置 | Harmless Rate (SD+OCR) | 说明 |
|------|----------------------|------|
| Direct | 32.1% | 无保护 |
| ECSO (完整) | 86.4% | 完整方法 |
| ECSO但保留图像 | ~48% | 图像存在时安全机制仍被压制 |
| 无query-aware caption | MME-P降0.23% | 通用caption遗漏关键信息 |
| 跳过step 3&4直接拒绝 | MME -18点 | 降低实用性 |

### 关键发现
- 去除图像是ECSO有效的关键：保留图像的情况下即使做了caption和重新回答，harmless rate仍显著低于去图像的情况
- ECSO在utility基准上几乎无损：MME-P/MME-C/MM-Vet/MMBench上误分类率仅0.08%-4.59%
- 对OCR攻击的防护效果最好（+42.2%），因为文字转为文本后被安全LLM直接识别为恶意内容
- 在5个不同MLLM上均有效（LLaVA-1.5、ShareGPT4V、mPLUG-Owl2、Qwen-VL-Chat、InternLM-XComposer）
- ECSO的harmless rate甚至超过Text-Only上限，因为prompt中的"HARMLESS and ETHICAL"进一步强化了安全意识

## 亮点与洞察
- **两个关键观察极具价值**：(1) MLLM的安全判别能力不受图像影响（>95%准确率）；(2) 去除图像可恢复安全机制。这两个发现本身就值得单独成文。
- **训练无关的设计让方法极为灵活**：无需任何额外训练数据或模型修改，可即插即用到任何MLLM上。这对需要快速部署安全防护的场景极有价值。
- **"闭眼"比喻贴切且有洞察力**：图像输入像打开了一扇不安全的窗口，"闭眼"关掉这个窗口、用文本"回忆"图像内容来恢复安全——简单但深刻。

## 局限性 / 可改进方向
- 对抗性图像攻击（gradient-based adversarial images）的鲁棒性未评估
- query-aware caption仍可能遗漏回答问题的关键视觉信息
- 增加了2-3次额外推理步骤，延迟增加
- 自检准确率非100%，可能存在false negative（漏检不安全回复）和false positive（误报安全query）

## 相关工作与启发
- **vs Pi et al. (RLHF-V)**：需要额外训练检测器和detoxifier，数据密集型。ECSO无需任何训练。
- **vs Chen et al. (Self-Moderation)**：仅通过指令让MLLM安全回答，但图像存在时仍失效。ECSO通过去除图像彻底解决这一问题。
- **vs Wang et al. (Safety Steering Vector)**：仅从文本角度调整激活，无法检测图像中的不安全意图。ECSO通过I2T转换统一处理文本和图像恶意。

## 补充说明
- ECSO可作为安全SFT数据引擎：收集不安全query的ECSO安全回复用于微调MLLM
- VLSafe数据集特点：恶意意图在文本而非图像中，图像是辅助性的
- MM-SafetyBench覆盖8个恶意场景（非法活动、仇恨言论、恶意软件等）
- Qwen-VL-Chat exception：即使有图像也有较高harmless rate，说明不同model alignment程度不同
- 去除图像后LLM的「分布恢复」是ECSO有效的根本原因
- 加入"HARMLESS and ETHICAL"关键词可进一步提升安全性（甚至超过text-only上限）

## 评分
- 新颖性: ⭐⭐⭐⭐⭐ 关键观察新颖、方法设计巧妙简洁、"闭眼安全"概念独创
- 实验充分度: ⭐⭐⭐⭐⭐ 5个MLLM、3种攻击类型、utility验证、详细消融
- 写作质量: ⭐⭐⭐⭐⭐ 观察→insight→方法逻辑链完美，图表信息量大
- 价值: ⭐⭐⭐⭐⭐ 实用性极强，对MLLM安全部署有直接帮助

<!-- RELATED:START -->

<div class="related-papers" markdown="1">

## 相关论文

- [\[ECCV 2024\] Merlin: Empowering Multimodal LLMs with Foresight Minds](merlin_empowering_multimodal_llms_with_foresight_minds.md)
- [\[ECCV 2024\] AddressCLIP: Empowering Vision-Language Models for City-wide Image Address Localization](addressclip_empowering_vision-language_models_for_city-wide_image_address_locali.md)
- [\[ECCV 2024\] Towards Real-World Adverse Weather Image Restoration: Enhancing Clearness and Semantics with Vision-Language Models](towards_real-world_adverse_weather_image_restoration_enhancing_clearness_and_sem.md)
- [\[ECCV 2024\] MotionChain: Conversational Motion Controllers via Multimodal Prompts](motionchain_conversational_motion_controllers_via_multimodal_prompts.md)
- [\[ECCV 2024\] UMBRAE: Unified Multimodal Brain Decoding](umbrae_unified_multimodal_brain_decoding.md)

</div>

<!-- RELATED:END -->
