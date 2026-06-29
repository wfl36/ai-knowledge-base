# Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents

**评分：** 8.5  
**状态：** 正常  
**标签：** Web Agent, 评估基准, 韩语NLP, 信息抽取, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27595v1 Announce Type: new Abstract: Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. I introduce \textsc{Ko-WideSearch}, a Korean breadth-search benchmark built by an automated synthesize-and-verify pipeline. Each task names a set-parent entity -- a TV season, a dynasty, a league, an administrative region, an election -- and asks for its full membership plus a per-item attribute table, graded by Item-, Column-, and Row-F1. It spans 228 tables over 190 entities and sixteen categories across three difficulty tiers, set by two structural knobs I dial independently -- table width and a 2-D composite key -- so cross-product membership climbs from 0\% to 100\% across the tiers. A single normalization-aware comparator is shared between gold construction and grading, so stable date and count columns are not over-dropped on formatting alone. Across twenty web agents, the failure is consistent: agents recover the set but not the rows (e.g.\ Item-F1 92.8 against Row-F1 53.7), accuracy falls steadily as the knobs harden, and neither more search nor more spend closes the gap. Broken down by cell, the hard part is finding the right value, not formatting it: open-ended free-text cells fail most, while cells with a standard answer such as a date or a name usually come out right.

## 综合总结
本文提出Ko-WideSearch，首个针对韩语Web Agent广度搜索能力的基准测试，旨在评估Agent穷举封闭集并填充属性的能力。研究通过自动化管道构建了多难度级别的任务，实验表明当前20个主流Web Agent在属性填充上表现糟糕（Item-F1与Row-F1差距巨大），且增加搜索量或成本无法弥补该缺陷，揭示了Agent在处理开放式自由文本信息时的核心短板。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文指出现有Web Agent基准过度关注深度搜索而忽视广度搜索（穷举封闭集及属性填充），尤其在非英语场景下。作者提出Ko-WideSearch基准，通过自动化综合与验证管道构建，利用表宽度和二维复合键独立控制难度，并引入归一化感知比较器解决格式误判。实验深刻揭示了当前Agent的核心缺陷：能枚举集合但难以准确填充行属性（Item-F1 92.8 vs Row-F1 53.7），且开放式自由文本单元格是主要失败点，增加搜索量或成本无法弥补该差距。

### 实用性 (评分: 8.0/10)
为Web Agent开发者提供了一个全新的评估维度和具体测试集，帮助定位Agent在广度搜索和属性填充上的短板。自动化的基准构建流程和细粒度的F1评估指标（Item/Column/Row-F1）具有较高工程参考价值，可直接指导Agent检索和信息抽取模块的优化，但受限于韩语环境，对非韩语开发者的直接落地适用性稍弱。

### 社区活跃度 (评分: 8.5/10)
Web Agent是当前AI应用的热点领域，该研究填补了非英语广度搜索评估的空白，来源为arXiv学术论文，具有较高的权威性。其揭示的'Agent能找集合但找不全属性'的现象对社区有较强的警示和启发作用，对推动Agent从单点检索向复杂穷举演进具有显著的时效性和影响力。

## 项目链接
https://arxiv.org/abs/2606.27595
