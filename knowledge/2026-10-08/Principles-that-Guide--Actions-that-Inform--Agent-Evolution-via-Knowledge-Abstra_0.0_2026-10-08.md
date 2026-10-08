# Principles that Guide, Actions that Inform: Agent Evolution via Knowledge Abstraction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-08  
**来源：** rss  

## 项目描述
arXiv:2610.06964v1 Announce Type: new Abstract: Large language model (LLM) agents have demonstrated strong capabilities in interactive environments, yet their ability to continually evolve from experience remains limited. Although fine-tuning enables adaptation, its dependence on parameter access and high computational costs restrict its flexibility, especially for large-scale and closed-source LLMs. External memory offers an alternative by allowing agents to accumulate experience without modifying model parameters. However, existing methods mainly focus on experience representation and organization, while the acquired knowledge remains tightly coupled with specific tasks and contexts, limiting generalization. A key challenge is how to transform concrete interactions into abstract and reusable knowledge that guides future decisions beyond individual experiences. To address this challenge, we propose SAGA (\underline{\textbf{S}}elf-evolving \underline{\textbf{A}}gents through Experience-\underline{\textbf{G}}rounded \underline{\textbf{A}}bstraction), a framework for experience-grounded knowledge abstraction and utilization in LLM agents. SAGA progressively transforms interaction trajectories into episodic descriptions, reusable procedures, and principles with explicit applicability conditions, while maintaining links to execution evidence. Retrieved principles are instantiated into task-specific guidance and used to refine candidate actions through corrective feedback and resampling. This creates an execution--abstraction feedback loop, where accumulated knowledge guides future interactions and new experiences continuously update hierarchical memory. Experiments on ScienceWorld and ALFWorld demonstrate improved task performance, with ablation studies highlighting the importance of contextual instantiation and action regulation for leveraging principle-level knowledge.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.06964
