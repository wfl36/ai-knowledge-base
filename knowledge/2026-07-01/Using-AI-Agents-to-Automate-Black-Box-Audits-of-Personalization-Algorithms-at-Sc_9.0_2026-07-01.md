# Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale

**评分：** 9.0  
**状态：** 正常  
**标签：** Agent, 算法审计, 个性化推荐, 反事实分析, 社交媒体, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30801v1 Announce Type: new Abstract: Personalization algorithms determine what content users encounter on online platforms. Auditing these systems is difficult because independent auditors have only black-box access to the algorithms, while personalization depends on users' attributes, behavior, and evolving interaction histories. Existing auditing methods face a tradeoff: studies with real users capture realistic behavior but are costly and hard to control, whereas sock-puppet audits scale more easily but often rely on scripted behavior that limits realism. Beyond this, both approaches struggle to decouple user attributes from user behavior, limiting our ability to causally understand personalization. To address this gap, we introduce a framework for black-box audits of personalization algorithms using generative AI agents as behavioral engines for synthetic accounts. Each agent is instantiated with a fixed persona, grounded in demographic and political survey data, and interacts with a platform's content by reasoning about it and choosing actions. Because behavior is fixed within each persona while platform-visible signals such as age, gender, or location can be experimentally perturbed, our design enables counterfactual auditing of how platforms respond to user attributes. As a case study, we deploy 1,120 agents on X shortly after the 2024 U.S. election, spanning 14 personas and three counterfactual conditions, collecting over 200,000 content exposures. We find that X's algorithmic feed amplifies toxic, polarizing, political, and right-leaning content relative to the chronological feed, with amplification varying sharply by user ideology. Counterfactual analyses show that demographic signals affect content delivery in persona-dependent ways: pooled effects are largely null, while subgroup-level effects vary in direction and magnitude. Our work establishes GenAI-based agents as a new tool for algorithmic auditing.

## 综合总结
本文提出了一种基于生成式AI代理的黑盒个性化算法审计框架，通过为合成账户赋予固定角色并实验性扰动平台可见信号，解决了传统审计中属性与行为难以解耦的问题，实现了反事实审计。研究在2024年美国大选后于X平台部署1120个代理，发现X算法显著放大了有毒、极化和右倾内容，且人口统计信号的影响在亚组层面存在异质性。该工作确立了GenAI代理作为算法审计新工具的地位。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
创新性地引入生成式AI代理作为行为引擎，解决了传统黑盒审计中用户属性与行为难以解耦的痛点，首次实现了可扩展的反事实算法审计。方法论严谨，实验规模大（1120个代理，超20万次曝光），不仅验证了框架的有效性，还揭示了亚组层面异质性等细致结论，研究深度与新颖性极高。

### 实用性 (评分: 8.5/10)
为独立审计员和监管机构提供了一套可操作的黑盒审计框架，能够有效评估社交媒体个性化推荐算法的偏见与影响。尽管部署大规模LLM代理存在一定的工程与API调用成本，且可能面临平台的反自动化对抗，但整体框架对指导算法合规与透明化实践具有极高的参考价值。

### 社区活跃度 (评分: 9.5/10)
话题极具时效性与社会影响力（针对2024美国大选后X平台的算法审计），直击社交媒体极化、信息茧房等热点问题。作者团队包含Aleksander Madry等学术界权威，来源可信度极高，研究成果对政策制定者、平台方及公众均有重要启示。

## 项目链接
https://arxiv.org/abs/2606.30801
