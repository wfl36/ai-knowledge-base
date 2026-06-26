# Knowledge-augmented Agentic AI for Mental Health Medication Information Seeking

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 知识图谱, 医疗AI, 药物警戒, 大模型, 多智能体  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26205v1 Announce Type: new Abstract: Patients increasingly seek medication information online, yet safety knowledge for psychiatric drugs is split between regulatory adverse-event records, which are authoritative but abstract, and patient narratives, which are experience-near but unvalidated. Integrating them without conflating evidence and anecdote is especially consequential in psychiatry, where poorly contextualised information can amplify fear, nocebo responses, and non-adherence. Here we develop a provenance-aware, knowledge-graph-based multi-agent framework unifying 466,525 Reddit posts, 60,782 WebMD reviews, and twenty years of U.S. FDA Adverse Event Reporting System records for nine antidepressants. A large-language-model entity-recognition pipeline benchmarked against physician annotations reached highest F1 scores of 0.969 for medications and 0.973 for conditions. The two community platforms were far more concordant with each other (overlap up to a Jaccard similarity of 0.905) than with regulatory reports, indicating that patient-generated data form a partly independent safety signal. For sertraline, many adverse events appeared in community sources hundreds of days before the corresponding FDA date. A Neo4j knowledge graph grounded in ATC-N, ICD-10, and MedDRA vocabularies preserves provenance, keeping every claim traceable and regulatory facts distinct from patient experience. These results establish source-aware integration as a route to more auditable psychiatric medication information, with usefulness and patient benefit to be tested prospectively.

## 综合总结
本文提出了一种溯源感知的基于知识图谱的多智能体框架，旨在解决精神科药物信息在权威监管记录与患者叙述间的割裂问题。该框架整合了Reddit、WebMD的海量患者生成数据与20年的FDA不良事件记录，利用LLM实体识别流水线（F1分数最高达0.973）提取信息，并基于Neo4j和标准医学词汇表构建知识图谱，严格区分并保留数据溯源。研究发现社区平台数据与官方报告存在显著差异，且部分不良事件在社区出现早于FDA数百天，为精神科药物的安全监测提供了独立且早期的预警信号，为构建更可审计的医疗信息AI系统提供了新路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了溯源感知的多智能体框架，创新性地将大语言模型实体识别与知识图谱结合，解决了精神科药物信息中权威监管数据与患者叙述的割裂问题。LLM实体识别在医生标注的基准下取得了极高的F1分数（药物0.969，疾病0.973），技术指标优异。基于Neo4j和标准医学词汇表（ATC-N, ICD-10, MedDRA）构建的知识图谱有效保留了数据溯源，论证严谨，且发现了社区不良事件信号早于FDA数百天的重要洞见。

### 实用性 (评分: 8.0/10)
对医疗健康、药物警戒和患者信息系统具有极高的落地参考价值。基于Neo4j和标准医学术语体系的设计使其具备良好的工程可接入性，能够指导药企、监管机构或医疗平台构建更安全、可审计的药物信息检索系统。但摘要末尾指出其临床有用性和患者获益仍需前瞻性测试，距离最终医疗场景应用尚有验证距离。

### 社区活跃度 (评分: 8.5/10)
精神心理健康与药物安全是当前社会高度关注的话题，结合社交媒体与官方数据的AI研究极具时效性和现实意义。研究团队基于海量真实世界数据（46万+Reddit帖子、6万+WebMD评论及20年FDA记录），且与医生标注进行严格对齐，来源权威可信。发现社区数据作为独立安全信号甚至早于官方预警的结论，在医疗AI和信息学领域具有较强的影响力和话题性。

## 项目链接
https://arxiv.org/abs/2606.26205
