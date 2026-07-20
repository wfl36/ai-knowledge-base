# EpiNarrate: Agentic Generation of Grounded Narratives from Epidemiological Scenario Projections

**评分：** 7.7  
**状态：** 正常  
**标签：** Agent, 推理, 数据分析, 科学计算, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15544v1 Announce Type: new Abstract: Generation of clear and accessible public health narratives is critical for communicating complex epidemiological projections to policymakers and the general public at large. Such narratives require more than simply reporting numbers: projections must be contextualized and quantitatively grounded across multiple dimensions. Further, projections are often derived from large ensemble datasets which combine intervention assumptions, geographic and demographic strata, outcomes, time horizons, and uncertainty quantiles. However, directly using large language models (LLMs) to summarize and contextualize such data often leads to inconsistencies, omissions, and fragile behavior. We introduce an agentic framework (EpiNarrate) for public health report generation that separates structured numerical reasoning from natural-language generation. The framework first extracts scenario axes and organizes them into a partial-order schema, enabling systematic traversal of the underlying multidimensional space. It then constructs an augmented dataset and derives valid quantitative statements through a comparison grammar that enforces semantic and arithmetic consistency. To balance coverage and non-redundancy, we introduce an interestingness-driven selection mechanism based on maximum-entropy principles. Experiments on the COVID-19 Scenario Modeling Hub demonstrate that our model produces narratives with improved factual grounding and broader coverage of salient epidemiological patterns, while preserving the style of expert-written reports.

## 综合总结
本文提出EpiNarrate智能体框架，用于从多维流行病学预测数据中自动生成事实依据充分的公共卫生叙事。该框架将数值推理与文本生成解耦，通过偏序模式遍历情景、比较语法保证定量一致性，并利用最大熵选择机制平衡覆盖率与冗余度。基于COVID-19数据的实验表明，该方法能生成事实准确、覆盖广泛的报告，有效克服了LLM直接处理复杂数据易出错的缺陷。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出EpiNarrate智能体框架，创新性地将结构化数值推理与自然语言生成解耦，通过偏序模式组织多维情景，利用比较语法确保算术和语义一致性，并引入基于最大熵原理的有趣度驱动选择机制。该设计有效解决了LLM直接处理多维集合数据时易产生幻觉、不一致和遗漏的问题，技术路径清晰，方法论与算法设计具有较好的深度和严谨性。

### 实用性 (评分: 7.5/10)
该框架对公共卫生和流行病学领域的从业者具有很高的实际参考价值，能自动化生成高质量、定量准确的预测报告，辅助政策制定。其核心思想（数值与文本解耦、比较语法推理）具备较强的泛化能力，可迁移至金融分析、气象预测等多维复杂数据的自动报告生成场景。

### 社区活跃度 (评分: 7.5/10)
项目结合了当前热门的Agent架构与大模型应用，聚焦公共卫生这一高社会价值领域，契合AI for Science的发展趋势。作者团队包含流行病学与计算科学领域的知名学者，成果发布于arXiv，具备较高的权威性与可信度，话题时效性强。

## 项目链接
https://arxiv.org/abs/2607.15544
