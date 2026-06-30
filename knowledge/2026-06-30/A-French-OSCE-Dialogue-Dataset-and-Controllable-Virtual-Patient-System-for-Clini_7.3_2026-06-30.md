# A French OSCE Dialogue Dataset and Controllable Virtual Patient System for Clinical Training

**评分：** 7.3  
**状态：** 正常  
**标签：** 大模型, Agent, 医疗, 医学教育, 数据集, 论文, 工程实践  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28526v1 Announce Type: new Abstract: The clinical and communication skills of medical students are commonly assessed through Objective Structured Clinical Examinations (OSCEs), which consist of brief scenario-driven simulations of doctor-patient interactions. However, training is often limited by the low availability of human standardized patients, motivating the development of realistic virtual patients (VPs). To address this gap, we introduce a French OSCE dialogue dataset comprising 240 student-patient training interactions. We build upon it a controllable LLM-based pipeline to generate synthetic OSCE dialogues. The pipeline integrates modular components, such as retrieval-based grounding and a reflection loop, to ensure patient fidelity, coherence, and realism. Additionally, we propose a multi-level evaluation framework assessing patient simulation quality, student performance, and linguistic quality, using an LLM-as-a-Judge approach. Experiments suggest that controllability modules generally improve patient fidelity and student evaluation consistency. Finally, we implement an interactive prototype in which students can practice with a VP and receive automatic feedback.

## 综合总结
本文针对医学OSCE考试中标准化病人稀缺的痛点，发布了包含240个交互的法语OSCE对话数据集，并构建了一个可控的LLM虚拟病人生成管线。该管线集成检索式grounding与反思循环以保障虚拟病人的保真度与连贯性，同时提出基于LLM-as-a-Judge的多级评估框架。实验表明可控性模块有效提升了模拟质量，最终实现了一个可供学生交互练习并获取自动反馈的虚拟病人原型系统，对医学教育AI落地具有重要参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
技术方案采用了当前主流的LLM应用范式（RAG+Reflection+LLM-as-a-Judge），将其创新性地组合应用于医学OSCE虚拟病人场景。通过引入检索式grounding和反思循环模块增强了生成的可控性与保真度，并设计了多级评估框架。论证有实验支撑，但底层算法缺乏颠覆性突破，且数据集规模（240个交互）相对较小，整体属于扎实的应用层组合创新。

### 实用性 (评分: 8.5/10)
对医学教育从业者具有极高的落地参考价值。标准化病人稀缺是临床训练的长期痛点，本文提供的从数据集构建、可控生成管线到自动评估及交互原型的完整方案，可直接指导虚拟病人系统的开发。其技术架构（RAG+Reflection+LLM Judge）不仅适用于法语OSCE场景，也可泛化至其他语言、医疗场景甚至更广泛的角色扮演训练领域。

### 社区活跃度 (评分: 6.5/10)
LLM在垂直领域（尤其是医疗与教育）的应用及Agent角色扮演是当前AI社区的热点话题，时效性强。文章发布于arXiv，作者具有学术背景，可信度中等偏上。但由于聚焦于法语OSCE数据集，受众相对小众，可能在一定程度上限制了其在全球医学AI社区的即时广泛影响力。

## 项目链接
https://arxiv.org/abs/2606.28526
