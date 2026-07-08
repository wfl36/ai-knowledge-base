# How Personas Can Influence Agents to Play Split or Steal

**评分：** 7.0  
**状态：** 正常  
**标签：** Agent, 人格设定, 博弈论, 社交困境, 大语言模型, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05398v1 Announce Type: new Abstract: Personas are often employed to guide large language model agents, yet their effectiveness in shaping strategic behavior in social dilemma settings remains uncertain. To address this, we examined the impact of persona prompts in an iterated Split or Steal game where persona-driven agents interacted with a Virtual Human (VH) controlled by a fixed prompt. Agents were instantiated from four open models (Ministral 3:3b, phi4:14b, Gemma3:12b, and Gemma4:e4b) at two temperature settings (0.3 and 0.7) and deterministic decision with zero temperature, while the VH was powered by GPT 4.1 mini. Across 160 sessions of 15 rounds each conducted in European Portuguese, mutual Split outcomes dominated (roughly 74 percent of rounds), with exploitation occurring in fewer than 11 percent of rounds. Model choice significantly influenced behavior: phi4 and Ministral 3:3b remained consistently cooperative across temperatures, whereas Gemma3:12b and Gemma4:e4b exhibited more varied strategies and outcomes. Analyses based on Big Five personality traits indicated that Prosocial and Principled personas were most consistently cooperative, while Analytical personas were more likely to exploit the VH. Topic analysis revealed that friendship-related dialogue aligns with Split decisions, whereas money and vengeance-related content is more prevalent in Steal outcomes; sentiment labels were predominantly neutral or happy and provided limited additional explanatory value. These findings characterize the interaction between persona prompts and model differences in repeated trust games and serve as a baseline for planned virtual reality studies involving human participants interacting with an embodied VH.

## 综合总结
本文系统研究了人格设定在重复“平分或偷窃”博弈中对LLM Agent策略行为的影响。实验基于四个开源模型与GPT-4.1 mini驱动的虚拟人进行交互，发现模型选择对行为影响显著，亲社会和原则性人格更倾向于合作，而分析型人格更易背叛。对话主题分析显示友谊与合作相关，金钱和复仇与背叛相关。该研究为理解Persona与模型差异在信任博弈中的交互作用提供了基线，对多Agent系统设计具有参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
研究设计较为严谨，通过控制变量（多模型、多温度、多轮次博弈）系统探究了Persona对LLM Agent在社交困境中的策略影响。结合大五人格特质和对话主题/情感分析，揭示了不同人格（如亲社会vs分析型）和模型架构在合作/背叛行为上的显著差异。但研究更偏向行为学现象观察与统计相关性分析，缺乏对模型内在决策机制的深度剖析，技术深度属于中等偏上。

### 实用性 (评分: 6.5/10)
对多Agent系统设计、游戏NPC行为塑造及虚拟人交互具有直接的参考价值，尤其是如何利用Persona提示词引导Agent的合作或竞争策略。然而，实验场景（Split or Steal）相对简化，且结论高度依赖特定的开源模型版本，在复杂真实商业场景中的泛化能力和落地指导性存在一定局限。

### 社区活跃度 (评分: 7.5/10)
Agent行为学与人格化提示词是当前AI社区的热门探索方向。论文发布于arXiv，作者具备学术背景，可信度良好。研究引入了较新的模型（如GPT-4.1 mini、Gemma系列）进行实验，且为后续VR环境人类与虚拟人交互提供了基线，具备较好的时效性和领域内影响力。

## 项目链接
https://arxiv.org/abs/2607.05398
