# From Question-First to Analyst-First: Domain-Expert Skills and Verified Knowledge Compilation for Proactive Enterprise Analytics

**评分：** 6.6  
**状态：** 正常  
**标签：** Agent, 数据分析, 企业BI, 系统架构, 工程实践, RAG, 知识编译  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28594v1 Announce Type: new Abstract: Conversational analytics systems assume the user already has a well-formed question, leaving a non-expert facing a blank query box on an unfamiliar enterprise schema. Commercial 'proactive' tools narrow this gap only by detecting statistical anomalies over analyst-curated metric layers, and academic next-question recommenders depend on query logs that a fresh dataset lacks. We describe a production analytics system that inverts the interaction model from question-first to analyst-first through two coupled architectural ideas. First, a pluggable domain-expert 'skill' abstraction: a folder-based, database-free subject-matter pack (a manifest, per-stage prompt facets, keyword-routed references, report templates, and optional compute) auto-selected per (client, dataset) by deterministic schema matching and spliced as a cross-cutting concern into every stage of an agentic pipeline, the schema explorer, and the report engines, degrading to a strict no-op when absent. Because a skill is a self-contained folder resolved deterministically, the catalogue is open-ended: an extensible marketplace of domain experts. Second, an offline knowledge-compilation loop: an agent probes the dataset's parquet via DuckDB (zero load on production), runs critic-gated per-table convergence with self-healing retries, and data-validates joins by value overlap, producing durable schema knowledge that drives standing expert reports whose every published metric is re-verified by re-executing its evidence SQL, plus suggested questions that mirror the report agenda. These close a proactive loop: reports surface numbers, the numbers seed questions, and a click launches a verified deep dive, all before the query box is used. We give a formal model and report illustrative single-tenant evidence. We make no user-study or benchmark claims; the contribution is the architecture and its defensibility.

## 综合总结
本文提出'分析师优先'的企业对话分析架构,核心包含两个创新:一是可插拔的领域专家技能抽象(文件夹式主题包,跨阶段注入agent pipeline);二是离线知识编译循环(DuckDB零负载探查+critic门控收敛+值重叠join验证),产出standing expert reports和suggested questions,实现查询框使用前的主动分析闭环。架构思想新颖,工程设计考虑成熟,但属于系统层面的整合创新而非算法/理论突破,且缺乏用户研究与基准验证,影响说服力与社区影响力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.2/10)
论文提出了两个耦合的架构创新:'领域专家技能'抽象(基于文件夹、无数据库的主题包)和'离线知识编译循环'(通过DuckDB探测parquet数据,critic门控的逐表收敛,自愈重试,基于值重叠的数据验证join)。'分析师优先'的交互模型反转具有较强的设计新颖性,formal model的提供增加了理论严谨性。但整体属于系统架构层面的工程整合创新,缺乏新的算法或理论突破,核心技术组件(DuckDB、critic-gated、自愈重试)均沿用既有技术栈,新颖性主要体现在组合方式与系统设计上。

### 实用性 (评分: 7.0/10)
对数据分析师、企业BI团队、数据平台工程师具有较高参考价值。'pluggable skill'抽象、离线知识编译、standing expert reports、verified deep dive等设计模式可直接借鉴到企业数据分析产品中。明确的工程取舍(零生产负载的DuckDB探查、schema匹配降级为no-op、self-healing retries)展示了生产环境的设计考量。但作者明确声明'no user-study or benchmark claims',且只给出'single-tenant illustrative evidence',实际效果与泛化性未得到验证,落地参考价值因此受限。

### 社区活跃度 (评分: 5.5/10)
话题契合'Agentic AI'与'企业数据分析'两大热点,arxiv ID格式(2608.28594)显示发布时间标注为2026年9月,属于未来时间戳,可能为预印本或标注异常,影响时效性可信度。作者明确不进行用户研究或基准测试,论文贡献定位为架构与可辩护性,社区影响力与传播潜力受限。缺少基准数据集对比和用户实验,在学术社区的标准评价体系中说服力有限。

## 项目链接
https://arxiv.org/abs/2608.28594
