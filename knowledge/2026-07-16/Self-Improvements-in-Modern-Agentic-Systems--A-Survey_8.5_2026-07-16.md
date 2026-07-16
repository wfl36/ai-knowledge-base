# Self-Improvements in Modern Agentic Systems: A Survey

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 自我改进, 大模型, 系统架构, 综述  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13104v1 Announce Type: new Abstract: Self-improving autonomous agents are moving from research prototypes to deployed systems. The primary goal is controllable evolution, or adaptation, from experience with minimal or even no human input. This survey frames modern self-improving agents as adaptive systems that convert experience into accumulated capability gains. We offer a system-level framework that represents a modern agent as a configuration coupling a foundation model with an operational scaffold of prompts, memory, tools, and control logic. Within this framework, self-improvement is formalized as a self-induced update operator that obtains and commits updates to model parameters or scaffold components. We organize prior work by update target and by the signals that drive change, then review applications and discuss evaluation, before closing with open problems and future directions. For convenience, we track technical updates on https://github.com/selfimproving-agent/awesome-Self-Improving-Agents.

## 综合总结
本文是一篇关于现代智能体系统自我改进的综述。作者将自我改进智能体视为将经验转化为累积能力增益的自适应系统，提出了一个系统级框架，将Agent解构为'基础模型+操作脚手架（提示、记忆、工具、控制逻辑）'的配置。在此框架下，自我改进被形式化为获取并提交更新的'自诱导更新算子'。文章按更新目标和驱动信号对现有工作进行了分类梳理，并回顾了应用、评估方法及未来方向，为构建可控演化的自主智能体提供了清晰的理论与工程指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了一个系统级框架，将Agent解构为'基础模型+操作脚手架'，并将自我改进形式化为'自诱导更新算子'，对更新目标（模型参数或脚手架组件）和驱动信号进行了严谨的分类与抽象，展现了较高的理论深度和系统性洞见。

### 实用性 (评分: 8.0/10)
提出的框架直接映射了当前Agent工程实践中的核心模块（提示、记忆、工具等），为开发者设计可自我演进的Agent架构提供了清晰的分类指导和形式化参考，且附带了持续更新的GitHub资源，落地指导性强。

### 社区活跃度 (评分: 9.0/10)
自我改进Agent是当前AI领域的核心前沿热点，时效性极高；作者团队包含Jürgen Schmidhuber等知名学者，权威性强；该综述填补了该领域系统性梳理的空白，预计将在社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2607.13104
