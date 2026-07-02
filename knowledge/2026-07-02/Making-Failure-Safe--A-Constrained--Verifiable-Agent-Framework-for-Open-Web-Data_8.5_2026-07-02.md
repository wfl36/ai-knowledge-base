# Making Failure Safe: A Constrained, Verifiable Agent Framework for Open-Web Data Collection

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 数据收集, 代码生成, 工程可靠性, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00035v1 Announce Type: new Abstract: LLMs and agents can generate web scrapers from natural-language requirements, but direct generation remains unreliable because of dependency errors, broken selectors, schema mismatches, and heterogeneous page structures. We propose a constrained, verifiable agent framework that shifts LLM output from free-form code to typed JSON collector configurations, combining a six-type collector taxonomy, template and utility-function constraints, static Airflow DAG execution, rule-based quality checking, and structured feedback correction. Experiments on 138 tasks show that the taxonomy supports description-based requirement typing, while confirming that stable instantiation requires completing source, field, and execution constraints beyond the initial description. On 80 independently source-verified tasks, the framework runs with zero execution-stage LLM tokens and the lowest average wall-clock time, trading moderate one-shot quality for a reusable, deterministic, and verifiable execution path suited to repeated scheduled collection. These results position the framework as a reusable, low-cost, and verifiable execution path for repeated open-web data collection.

## 综合总结
该论文提出一种受限且可验证的Agent框架，用于开放网页数据收集。通过将LLM输出从自由代码转为受限的JSON配置，结合收集器分类法、模板约束、静态Airflow DAG执行和规则校验，解决了传统生成式爬虫的不可靠问题。实验表明，该框架在执行阶段实现零LLM token消耗和最低耗时，以适度的单次质量换取了高可复用性、确定性和可验证性，非常适合重复性定时数据采集任务。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出将LLM输出从自由生成代码转变为受限的JSON配置，结合六种收集器分类法、模板约束、静态Airflow DAG执行和规则校验，有效解决了Agent生成爬虫的不确定性和依赖错误问题。论证严谨，实验设计合理，体现了从“端到端生成”向“受限生成+确定性执行”的深刻认知转变。

### 实用性 (评分: 9.0/10)
对数据工程从业者具有极高的参考价值。框架采用Airflow DAG、JSON配置和规则校验等成熟工程组件，牺牲适度的单次生成质量换取可复用性和确定性，非常符合工业界对定时、重复数据抓取的实际需求，落地路径清晰，适用范围明确。

### 社区活跃度 (评分: 8.0/10)
Agent的安全性与可靠性是当前AI社区的核心痛点，该论文紧扣热点。基于arXiv发表，具备学术可信度。其“受限Agent”的理念契合行业从Demo走向生产的趋势，有望在数据工程和Agent框架圈层产生积极影响。

## 项目链接
https://arxiv.org/abs/2607.00035
