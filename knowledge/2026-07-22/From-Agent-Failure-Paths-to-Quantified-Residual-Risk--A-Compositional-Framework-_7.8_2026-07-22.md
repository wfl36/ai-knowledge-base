# From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI

**评分：** 7.8  
**状态：** 正常  
**标签：** Agent, AI安全, 风险评估, 具身智能, 形式化验证, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18243v1 Announce Type: new Abstract: Agentic AI is crossing trust boundaries faster than current risk models can represent. Existing approaches provide one of two partial views. They either describe failure mechanisms without producing a transferable residual-risk estimate, or they produce a risk estimate while treating the internal failure path as a black box. We couple those two views by proposing CPSAINT, a seven-layer integrity decomposition over Physical state, Sensors, Data, Compute, Actuators, Environment, and Time, paired with FRIESA-K, a residual-risk functional that maps each failure path to a quantified risk instance. FRIESA-K grounds the resistance term K in a controlled absorbing Markov model so that control effectiveness is derived from state dynamics rather than assigned as an informal score. The result is a concise mechanism-to magnitude pipeline for resilient agentic and embodied AI. We report governance observability through a separate additive penalty instead of inserting governance as a new variable in the resistance functional. We formalize structural composability linking valid failure paths to well-defined risk instances and show the framework on two contrasting scenarios a hard real-time warehouse robot and a governance-instrumented financial-services agent. Across both cases, the same layer grammar, variable semantics, and dynamic-resistance construction remain intact. Thus, we obtain a compact kernel that supports cross-domain reasoning, explicit assumptions, and quantitatively grounded formalism of composable trust.

## 综合总结
本文针对Agentic AI跨越信任边界时的风险评估难题，指出当前方法在故障机制描述与风险量化估计上的割裂。为此，提出了CPSAINT七层完整性分解框架与FRIESA-K剩余风险泛函，通过受控吸收马尔可夫模型将故障路径精确映射为量化风险实例，实现了从机制到量化的闭环。同时，框架通过加法惩罚处理治理可观测性，并在硬实时仓库机器人与治理型金融Agent两个跨域场景中验证了其结构可组合性与通用性，为构建可组合信任的弹性Agentic AI提供了坚实的量化形式化基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在Agentic AI的风险评估领域展现了较高的新颖性与研究深度。针对现有方法在故障机制描述与风险量化估计上的割裂，创新性地提出了CPSAINT七层完整性分解框架与FRIESA-K剩余风险泛函，实现了从故障机制到量化风险的映射。技术亮点在于使用受控吸收马尔可夫模型来推导控制有效性K，取代了传统非正式的评分方式，并形式化了结构可组合性，论证严谨，具备较强的理论深度。

### 实用性 (评分: 7.0/10)
对从事高可靠性Agent（如具身智能、金融AI）开发的工程师和架构师具有较高的参考价值。CPSAINT的七层分解可直接作为系统安全架构的审查清单，但在实际工程落地中，FRIESA-K所需的马尔可夫模型参数获取与计算复杂度可能构成挑战，需要进一步的工程化简与工具支持才能广泛指导日常开发实践。

### 社区活跃度 (评分: 8.0/10)
Agentic AI的安全与信任边界是当前AI领域的热点与痛点，话题时效性极高。该论文提出的形式化风险量化框架直击行业痛点（黑盒风险与机制脱节），来源为arXiv学术论文，具备较高的学术可信度。若其跨域通用性得到更多验证，有望在AI安全治理与评估社区产生显著影响力。

## 项目链接
https://arxiv.org/abs/2607.18243
