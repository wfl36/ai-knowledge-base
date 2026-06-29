# When Does Personality Composition Matter for Multi-Agent LLM Teams?

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, Agent, 多智能体, 性格提示, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27443v1 Announce Type: new Abstract: Personality prompting shapes how large language models communicate, yet whether these behavioral shifts affect objective task outcomes remains under-explored. Prior work shows that agents prompted with low agreeableness produce adversarial language, while those prompted with high agreeableness become cooperative, but the relationship between communication style and task performance has not been systematically examined across multiple domains. In this work, we investigate whether personality composition matters for multi-agent team performance by manipulating personality traits across frontier LLMs on three task domains: structured coding, open-ended research collaboration, and competitive bargaining. We find that personality effects depend critically on task structure. In coding tasks, low agreeableness leads to large communication shifts that have little effect on milestone completion. In open-ended collaboration and bargaining, the same manipulation substantially degrades performance. We discuss implications for multi-agent system design and the limits of personality manipulation.

## 综合总结
本文研究了性格提示在多智能体LLM团队中的作用，发现性格对任务表现的影响严重依赖于任务结构：在结构化编程任务中，低宜人性虽改变沟通方式但不影响任务完成；而在开放式合作与竞争性谈判中，低宜人性会显著降低性能。该研究为多智能体系统的性格工程与架构设计提供了重要的实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
系统性地探究了性格提示对多智能体LLM团队任务表现的影响，跨越结构化编程、开放式合作和竞争性谈判三个领域进行实验，论证严谨。研究打破了性格提示仅改变沟通风格或必然影响性能的片面认知，揭示了性格效应受任务结构制约的深层规律，具有较高的研究深度与新颖性。

### 实用性 (评分: 8.5/10)
对多智能体系统开发者具有直接的实践指导价值。明确指出在结构化任务（如编程）中性格设定的容错率高，无需过度优化性格提示；而在合作与谈判任务中需严格把控性格特征（如避免低宜人性），能有效帮助从业者避免无效的性格工程，优化系统设计策略。

### 社区活跃度 (评分: 8.0/10)
聚焦多智能体与性格提示这一当前AI领域热点，话题时效性极强；作者团队包含知名学者Huan Liu，依托arXiv平台发布，来源权威可信，对多智能体系统设计社区具有较好的启发与影响力。

## 项目链接
https://arxiv.org/abs/2606.27443
