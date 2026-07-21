# PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection

**评分：** 9.3  
**状态：** 正常  
**标签：** 多智能体, 安全, 提示注入, LLM, 规划, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16199v1 Announce Type: new Abstract: Multi-agent LLM systems increasingly rely on a Planner to decompose goals into sub-task sequences that downstream Executor and Critic agents execute and audit. We identify the planning phase as a critical attack surface: a single injection into the Planner's context achieves cascade amplification, corrupting all downstream sub-tasks simultaneously. We introduce PlanFlip, a framework comprising four planning-phase prompt injection attacks -- GoalSubstitution (PF-1), PriorityInversion (PF-2), ContextPollution (PF-3), and RoleConfusion (PF-4) -- each disguised as plausible tool outputs to evade keyword filters. Evaluating nine frontier LLMs across 3,479 episodes, we uncover three findings: (1) capability amplifies vulnerability -- GPT-5 achieves the highest attack success rate (ASR = 0.68), contradicting the assumption that stronger models are inherently more secure; (2) homogeneous pipelines exhibit a correlated-agent blind spot -- GPT-4o and Llama-3.3-70B show ASR near 0 yet Stealth = 1.00 and StepShift > 0, with attacks restructuring plans while the same-backbone Critic reports alignment (two independent judges confirm -0.20 to -0.32 semantic deviation, r = 0.943); (3) reasoning-augmented models resist injections -- DeepSeek-R1 achieves StepShift = 0.00 across all attacks. We propose GoalAnchorCheck (D1) and CrossAgentConsensus (D2), achieving detection rates up to 1.00 and outperforming same-backbone baselines in 15 of 16 cells. Our key insight: heterogeneous model diversity is a security prerequisite for multi-agent systems; redundancy within a homogeneous backbone provides no protection against planning-phase attacks.

## 综合总结
本文提出PlanFlip框架，针对多智能体LLM系统的规划阶段进行提示注入攻击，通过伪装成工具输出实现四种攻击（目标替换、优先级反转、上下文污染、角色混淆）。实验表明：1) 模型能力越强越脆弱（GPT-5 ASR最高）；2) 同构多智能体存在盲点，同源Critic无法检测隐蔽的语义偏移；3) 推理增强模型（如DeepSeek-R1）具有强抗性。作者提出两种防御机制并证实有效，核心洞见指出异构模型多样性是多智能体系统安全的必要前提，同构冗余无法防御规划阶段的级联攻击。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
创新性地将多智能体系统的攻击面聚焦于“规划阶段”，揭示了单点注入导致级联失效的放大效应。提出的四种攻击手法隐蔽性高，实验设计严谨，通过引入独立裁判验证了同源Critic的检测盲区。三大发现（能力放大脆弱性、同构盲点、推理增强抗性）深刻且反直觉，论证极具深度。

### 实用性 (评分: 9.0/10)
对构建多智能体系统的工程实践具有极高的指导价值。明确指出了当前流行的“同构模型冗余”设计在安全性上的无效性，强制要求架构师采用异构模型组合。提出的GoalAnchorCheck和CrossAgentConsensus防御策略可直接落地于主流Agent框架，显著提升系统鲁棒性。

### 社区活跃度 (评分: 9.5/10)
话题极具时效性和热度，直击当前大模型多智能体应用落地的核心安全痛点。测试涵盖了GPT-5、DeepSeek-R1等前沿模型，引发对“越强越不安全”悖论的广泛关注，对AI安全社区和Agent开发者具有强烈的警示和影响力。

## 项目链接
https://arxiv.org/abs/2607.16199
