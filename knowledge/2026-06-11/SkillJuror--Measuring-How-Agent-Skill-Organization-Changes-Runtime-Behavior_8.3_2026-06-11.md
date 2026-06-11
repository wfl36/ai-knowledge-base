# SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 大模型, Agent技能, 评估基准, 论文, 框架  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11543v1 Announce Type: new Abstract: Agent Skills augment large language model (LLM) agents with procedural knowledge at inference time, but current benchmarks rarely distinguish what a Skill says from how it is organized. We study this distinction through Progressive Disclosure, where a concise root file points agents to supporting resources on demand, and compare it with a normalized flat baseline. We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed. In an 82-task SkillsBench study, Progressive Disclosure changes runtime behavior before aggregate outcomes: distinct Skill resources touched per trajectory rise from 1.18 to 3.85, and effective uptake events rise from 1.33 to 3.92. It also yields 17 additional verifier-passing trials out of 410 matched trials (+4.1%) over the normalized flat baseline. The benefit is task-dependent. Progressive Disclosure helps when supporting resources guide implementation, checking, or repair, but is weaker when success hinges on exact output conventions, numerical thresholds, or long artifact-generation pipelines. These results show that Skill organization is not mere presentation: it can change how agents search and apply procedural knowledge, while outcome gains depend on whether the exposed resources are actionable for the task. Code is available at https://github.com/zhiyuchen-ai/skill-juror.

## 综合总结
本文提出SkillJuror框架，研究了Agent技能的组织方式如何影响其运行时行为。通过对比‘渐进式披露’（按需加载支持资源）与扁平化基线，发现技能组织方式不仅显著改变了Agent搜索和应用过程知识的行为轨迹（资源触及和吸收事件大幅增加），还能带来4.1%的通过率提升。研究进一步指出，渐进式披露在需要指导实现、检查或修复的任务中效果显著，而在依赖精确输出约定或长生成管道的任务中较弱。该研究为Agent技能的编写与组织提供了重要的实证依据和评估工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文触及了Agent领域常被忽视的重要问题：技能的‘组织方式’而非仅仅是‘内容’如何影响Agent的运行时行为。通过引入‘渐进式披露’与扁平化基线进行对比，并提出SkillJuror评估框架，研究设计严谨（控制任务知识变量、匹配多次试验、轨迹证据分析）。结论深入揭示了技能组织对Agent搜索和应用过程知识的深层影响，并细致分析了其在不同任务类型上的适用边界，具有较好的理论深度和实证价值。

### 实用性 (评分: 8.0/10)
对Agent开发者和提示词工程师具有极高的实践指导意义。研究不仅验证了‘渐进式披露’（按需调用子技能）作为一种技能编写范式的有效性，还明确了其最佳适用场景（指导实现、检查、修复）与局限（精确输出约定、长生成管道）。这为实际项目中如何结构化地设计和管理Agent技能库提供了清晰的范式参考，且作者开源了代码，落地借鉴性强。

### 社区活跃度 (评分: 8.5/10)
Agent的技能管理与行为优化是当前大模型社区的前沿热点。该论文作为arXiv最新发布的研究，由知名高校团队贡献，开源了评估框架与基准，具有很高的时效性和学术可信度。其关于‘技能组织方式改变运行时行为’的结论，对当前Agent框架的设计理念具有启发和纠偏作用，有望引发社区对Agent技能编排范式的进一步探讨。

## 项目链接
https://arxiv.org/abs/2606.11543
