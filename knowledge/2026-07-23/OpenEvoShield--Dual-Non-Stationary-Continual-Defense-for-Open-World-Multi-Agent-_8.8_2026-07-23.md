# OpenEvoShield: Dual Non-Stationary Continual Defense for Open-World Multi-Agent System Attacks

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 大模型安全, 多智能体系统, 持续学习, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19351v1 Announce Type: new Abstract: LLM-based multi-agent systems (LLM-MAS) are increasingly deployed in safety-critical applications, where adversaries inject malicious instructions through inter-agent communication to propagate harmful behaviors. Unlike static threats, these attacks are doubly dynamic: adversaries refine injection strategies against deployed defenses while normal-agent behavior drifts with system expansion. Existing defenses treat deployment as a closed-world problem and degrade rapidly once either distribution shifts beyond training coverage. We propose OpenEvoShield, a co-evolutionary continual defense framework for LLM-MAS. An asymmetric rate controller (M1) decouples fast attack-side and slow normal-side learning rates from dual drift signals. A normal-boundary updater (M2) maintains a dynamic behavioral boundary at the slow rate, while an EWC-regularized policy ensemble (M3) fast-adapts without catastrophic forgetting. An energy-based multi-granularity detector (M4) fuses node-, subgraph-, and graph-level evidence to classify novel attacks as out-of-distribution. Experiments over 100 deployment rounds across five benchmarks and four MAS topologies show that OpenEvoShield outperforms static and continual baselines, detecting most previously unseen attacks while keeping false positive rates low.

## 综合总结
本文针对LLM多智能体系统在开放世界中面临的“双重动态”攻击（攻击策略演化与正常行为漂移）导致传统静态防御失效的问题，提出协同演化持续防御框架OpenEvoShield。该框架通过非对称速率控制器解耦快慢漂移，利用EWC正则化实现无灾难遗忘的快速适应，并结合基于能量的多粒度检测器识别未知攻击。实验证明其在多基准和拓扑下显著优于现有基线，为LLM-MAS的开放世界安全提供了突破性的动态防御范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
针对LLM多智能体系统（LLM-MAS）中攻击策略与正常行为双重动态漂移的痛点，提出协同演化的持续防御框架OpenEvoShield。技术设计精巧且新颖，通过非对称速率控制器（M1）解耦快慢漂移，结合EWC正则化策略集成（M3）解决快速适应与灾难性遗忘的矛盾，并引入基于能量的多粒度检测器（M4）识别分布外未知攻击。论证严谨，实验覆盖5个基准与4种拓扑的100轮部署，技术深度与问题定义的突破性显著。

### 实用性 (评分: 8.5/10)
对LLM-MAS安全从业者与工程师具有极高的落地参考价值。框架的模块化设计（M1-M4）为构建动态防御系统提供了清晰的工程实现路径，能够直接指导开放环境下Agent系统的安全防护升级。但持续学习与多粒度图级检测机制在实际部署中可能带来一定的计算与系统监控开销，需根据具体业务场景进行工程权衡。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前大模型Agent从封闭静态测试走向开放动态部署的核心安全瓶颈。随着LLM-MAS在关键领域的应用，开放世界下的动态攻防是社区亟待解决的焦点。该研究将持续学习与多智能体安全结合，切中行业痛点，预计将在AI安全与Agent社区产生重要影响力。

## 项目链接
https://arxiv.org/abs/2607.19351
