# Seduced by the Narrative: Assessing Rule Adherence in Semi-Open Textual Sandboxes

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, Agent, 安全/对齐, 推理, 多智能体, 论文, 基准测试  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02802v1 Announce Type: new Abstract: As LLMs are increasingly deployed as autonomous adjudicators in semi-open textual game environments, robust rule adherence becomes critical when user intent conflicts with system rules. However, these models are trained to be helpful and compliant, leaving them vulnerable to a class of attacks we term \textit{Rhetorical Injection}, where adversarial users exploit narrative framing techniques such as pseudo-logical reasoning and authoritative coercion to bypass adjudication logic. We present CoC-Seduce, a multi-agent adversarial benchmark built on Tabletop Role-Playing Game (TRPG) mechanics, an ideal instantiation of semi-open environments where rules are explicit for adjudication, yet interaction remains entirely in natural language. Three frontier models, i.e., GPT-5.4, Claude Sonnet 4.6, Gemini 3.5 Flash, serve as adversarial generators producing 5,376 samples across 4 world settings and 16 skill categories. We then benchmark 20 target adjudicators against this corpus. Evaluation across 20 models reveals that neither model scale nor explicit reasoning mechanisms reliably confer adjudication robustness, with \textsc{Pseudo-Logic} emerging as the dominant attack vector and cross-cultural settings exposing systematic knowledge gaps across all evaluated families. Project page: https://github.com/answerrtx/CoC-Seduce

## 综合总结
本文针对LLM在半开放文本沙盒中作为裁决者时易受用户叙事诱导而违背规则的问题，提出了“修辞注入”攻击范式。作者构建了基于TRPG的多智能体对抗基准CoC-Seduce，利用前沿模型生成了5376个对抗样本并对20个目标模型进行评估。研究发现，模型规模和显式推理机制并不能提升规则遵循的鲁棒性，伪逻辑是最主要的攻击向量，且跨文化场景暴露了系统性的知识缺口。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了“修辞注入”这一新型攻击范式，揭示了LLM在叙事框架下易受伪逻辑和权威胁迫影响而违背系统规则的脆弱性。构建了基于TRPG机制的多智能体对抗基准CoC-Seduce，通过大规模样本和前沿模型评估，严谨论证了模型规模与显式推理机制无法保证规则遵循的鲁棒性，并发现了跨文化场景下的系统性知识缺口，研究深度与新颖性俱佳。

### 实用性 (评分: 8.5/10)
对开发LLM裁判、游戏AI及自动化规则执行系统的从业者具有高参考价值。明确指出了“伪逻辑”为最有效的攻击向量，提示开发者在系统设计时需针对性增强对叙事性诱导的防御，尤其在跨文化和多语言部署场景下需填补知识对齐缺口，具备极强的实践指导意义。

### 社区活跃度 (评分: 8.5/10)
紧扣当前LLM Agent安全与对齐的前沿热点，测试对象涵盖GPT-5.4等最新前沿模型，具有极高的时效性。研究开源了基准数据集与项目代码，对LLM在半开放环境中的可信部署具有显著的警示与推动作用，来源与结果均具较高权威性与影响力。

## 项目链接
https://arxiv.org/abs/2607.02802
