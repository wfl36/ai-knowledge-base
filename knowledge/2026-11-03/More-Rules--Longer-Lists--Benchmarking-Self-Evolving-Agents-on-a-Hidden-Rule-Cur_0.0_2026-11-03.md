# More Rules, Longer Lists? Benchmarking Self-Evolving Agents on a Hidden-Rule Curriculum

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.40758v1 Announce Type: new Abstract: Self-evolving agents rewrite a persistent state from feedback, but it is largely untested whether this lets them learn a rule nobody told them. An agent can also pass by writing down each correction as an exception, and its list then grows with every new rule. We introduce CLR-Bench, a Curriculum of Latent Rules benchmark. Each chain adds one hidden rule per level on top of the earlier ones. A rule acts on an opaque label that stands for a named grouping published on the Web, such as the founding members of an airline alliance. The task gives one example value, practice feedback reveals one more member and one non-member, and the test checks unseen members and similar non-members. Probes certify that the base model knows the members of each grouping and does not guess it without feedback, and that the evidence identifies the grouping once labels are read as named groupings. An automated pipeline builds chains from a new data domain, and we release 20 chains over 10 domains. We evaluate six recent self-evolution methods. With the certifying model they barely learn. The best gain at most 5 points over a frozen agent and exclude only 6-12% of the unseen members from the count, fewer than the 20% reached by simply keeping the raw practice history. A fixed lesson that states the named-grouping convention lifts the same methods by 14.5 to 16.5 points. Their states hold the revealed member in 75-98% of cases and almost never the class name, and when practice exposes a member the list misses, they add that member to the list. With the stronger GPT-6-Sol, ACE and Dynamic Cheatsheet learn from feedback alone. They reach 78% accuracy and solve 59-60% of the single cells, against 53% and 8% with the certifying model, and they surpass the raw history. CLR-Bench therefore measures how well an agent learns, and this ability differs across models.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.40758
