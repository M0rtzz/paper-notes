# When Agents Persuade: Propaganda Generation and Mitigation in LLMs

**会议**: ICLR 2026  
**arXiv**: [2603.04636](https://arxiv.org/abs/2603.04636)  
**领域**: AI安全/宣传检测  
**关键词**: 宣传生成, 修辞技术, LLM安全, ORPO微调, 内容审核

## 一句话总结
系统研究LLM能否生成宣传内容→训练宣传检测器(F1=0.98)+修辞技术检测器(6种技术,平均F1=0.82)→发现LLM被prompting时会广泛使用宣传修辞(name-calling/loaded language/appeal to fear等)→SFT/DPO/ORPO三种微调方法可显著减少宣传生成→ORPO最有效。

## 研究背景与动机

**领域现状**：LLM→已证明能说服人→但是通过什么修辞技术说服的？→如何缓解？

**现有痛点**：
   - (1) 之前研究→只关注"是否说服"→不分析"如何说服"(用了哪些修辞技术)
   - (2) 宣传比虚假信息更微妙→cherry-pick事实+情感操纵→难检测
   - (3) Agent系统→可放大宣传→自动规模化操纵

**切入角度**：(1)检测宣传性质; (2)解析修辞技术; (3)微调缓解。

## 方法详解

### 检测模型
1. **宣传/非宣传分类器**: QProp+PTC数据训练→F1=0.98
2. **修辞技术检测器**: 6种技术→PTC数据→平均F1=0.82
   - Name-calling, Loaded language, Appeal to fear, Flag-waving, Exaggeration, Causal oversimplification

### 宣传生成实验
- 选择论题→prompting GPT-4o/Llama-3.1/Mistral生成宣传
- 用检测器分析生成内容的宣传性和修辞技术使用

### 微调缓解
- SFT: 直接微调减少宣传生成
- DPO: 偏好优化(宣传=不偏好)
- ORPO: Odds Ratio偏好优化

## 实验关键数据

| LLM | 宣传检出率 | 主要技术 |
|-----|----------|---------|
| GPT-4o | 高 | Loaded language, Name-calling |
| Llama-3.1 | 高 | Appeal to fear, Flag-waving |
| Mistral | 高 | Exaggeration |

### 微调缓解效果
| 方法 | 宣传生成减少 |
|------|-----------|
| SFT | 显著 |
| DPO | 显著 |
| **ORPO** | **最显著** |

### 关键发现
- 所有测试LLM→被prompting时都能生成宣传→频繁使用多种修辞技术
- Loaded language→最常用技术(跨所有模型)
- ORPO→最有效的缓解方案→可能因为直接优化odds ratio

## 亮点与洞察
- **"如何说服>是否说服"**：之前只知道LLM能说服→现在知道用了什么修辞技术→更actionable。
- **修辞技术=宣传的构建块**：宣传不是整体→由具体技术组成→解构后可以针对性防御。
- **ORPO的实用性**：比DPO更有效的对齐→对安全训练有直接指导。

## 评分
- 新颖性: ⭐⭐⭐⭐ 首次系统分析LLM的宣传修辞技术+微调缓解
- 实验充分度: ⭐⭐⭐⭐ 3 LLM+检测器+3微调方法
- 写作质量: ⭐⭐⭐⭐ 清晰实用
- 价值: ⭐⭐⭐⭐ 对AI安全和内容审核直接有用
