# Information Discernment in Large Language Models

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 对齐, RAG, 评估基准, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19355v1 Announce Type: new Abstract: LLMs are increasingly used with external knowledge sources like the internet. Do they weigh information appropriately -- updating more for reliable sources (source discernment) and more when claims bring priors closer to the truth (truth discernment)? We formalize this as information discernment and introduce Learn2Discern (L2D), an experimental framework and benchmark grounded in three normative axioms with interpretable metrics. To establish external validity, a pre-registered, quota-matched user study (n=299) confirms that real LLM users endorse all three axioms and report that violations reduce their trust and usage intent. Across 13 models and nearly 670K trials, we find consistent failures across both dimensions: models perform near chance on source and truth discernment, rely on source popularity twice as much as source reliability, and update roughly equally whether a claim improves or worsens their position relative to the ground truth. Models integrate external knowledge most effectively on datasets where their priors are already the most accurate. Newer and larger models improve truth discernment but not source discernment, a blind spot that model complexity does not address. We identify simple inference-time interventions that improve both forms of discernment. We release our dataset and survey as a testbed for a core alignment property that scales in importance as LLMs replace traditional search.

## 综合总结
本文提出“信息辨别”概念及L2D评估框架，揭示了当前大模型在处理外部知识时存在严重缺陷：过度依赖信息源流行度而非可靠性，且无法区分信息对真相的改善或恶化作用。规模扩大无法解决来源辨别盲点，但推理时干预可有效改善。该研究为RAG和联网大模型的对齐与安全提供了重要基准和干预思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文形式化提出了“信息辨别”概念，将其分解为来源辨别和真相辨别，并基于三大规范公理构建了Learn2Discern (L2D)框架与基准。通过近67万次试验和299人用户研究，严谨地揭示了当前LLM在信息辨别上的系统性失败：模型表现接近随机，过度依赖来源流行度而非可靠性，且对改善或恶化先验真相的信息无差别更新。规模扩大仅改善真相辨别而无法解决来源辨别盲点，但研究发现了有效的推理时干预方法。

### 实用性 (评分: 8.5/10)
对构建RAG和联网Agent系统具有极高的实践指导意义。研究明确指出了LLM在处理外部知识时的“重流行度、轻可靠性”缺陷，提醒从业者在系统设计中不能盲目依赖模型自身的判断。提出的推理时干预方法为改善模型信息筛选能力提供了直接可操作的落地方案。

### 社区活跃度 (评分: 9.0/10)
研究切中当前LLM替代传统搜索趋势下的核心安全与对齐痛点，时效性极强。论文来自知名学术团队，采用预注册用户研究确保了外部效度，数据集和基准的开源将为社区评估LLM信息辨别能力提供标准测试床，具有广泛影响力。

## 项目链接
https://arxiv.org/abs/2607.19355
