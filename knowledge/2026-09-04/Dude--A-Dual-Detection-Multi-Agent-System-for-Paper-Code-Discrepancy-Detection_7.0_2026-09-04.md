# Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection

**评分：** 7.0  
**状态：** 正常  
**标签：** Agent, 多智能体系统, 论文代码差异检测, 代码智能, AI4Science, 论文  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.03416v1 Announce Type: new Abstract: LLM-empowered paper-code discrepancy detection has received growing concern since the scaling of research submissions exceeds the manual review capability. However, the limited context capacity and one-sided discrepancy detection of existing single-agent LLM paradigms lead to an inferior recall performance in detecting discrepancies. In this paper, we propose Dude, the first Dual-Detection Multi-Agent System for paper-code discrepancy detection. We discover that the granularity asymmetry of the paper-language and code-language introduces over-interpretation and over-reporting challenges in a multi-agent system design for discrepancy detection, resulting in increasing false positives. To address this, we propose a granularity-aligned negotiation and a two-stage salience-filtering mechanism in Dude, which effectively prevents agents from falsely reporting discrepancies. Experimental results in real-world paper-code discrepancy datasets showcase Dude's significant recall and precision improvement by up to 22.8%, increasing F1 score by up to 18.7% compared to baseline methods.

## 综合总结
Dude提出了首个用于论文-代码差异检测的双检测多智能体系统，通过粒度对齐协商与两阶段显著性过滤机制，有效解决了多智能体场景下的过度报告问题，在真实数据集上取得了显著的召回率与精度提升。该工作将多智能体协作范式引入学术代码审查领域，具有较好的创新性和实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
文章针对论文与代码之间的差异检测问题，提出了一种双检测多智能体系统Dude，识别了多智能体设计中因论文语言与代码语言的粒度不对称导致的过度解读和过度报告问题，并提出粒度对齐协商机制与两阶段显著性过滤机制来抑制误报。方法上具有较好的问题洞察力，将单智能体扩展为多智能体协同并引入粒度对齐思路，体现了一定的技术创新性，但在多智能体系统的底层机制设计、理论分析深度上仍有提升空间。

### 实用性 (评分: 7.0/10)
Dude系统直接面向学术论文代码审查场景，具有较强的实际应用价值，22.8%的召回率提升和18.7%的F1提升幅度对从业者具有参考意义。该方案可作为论文复现性检查、代码审计工具的参考架构，落地门槛适中。但论文主要聚焦在差异检测本身，对工程部署细节、与现有CI/CD流程集成的讨论相对有限。

### 社区活跃度 (评分: 6.5/10)
论文于2026年9月发布在arXiv上，时间较新，关注LLM驱动的论文-代码差异检测这一较新颖且实用的话题，符合当前AI4Science和代码智能的研究热点。作者团队有多位研究者参与，来源可信度尚可。但目前仅发布了v1版本，未公布代码链接（基于摘要判断），社区影响力和后续验证仍有待观察。

## 项目链接
https://arxiv.org/abs/2609.03416
