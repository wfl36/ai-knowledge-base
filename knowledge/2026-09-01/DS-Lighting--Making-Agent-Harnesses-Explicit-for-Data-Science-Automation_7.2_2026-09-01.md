# DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation

**评分：** 7.2  
**状态：** 正常  
**标签：** Agent, 数据科学自动化, 评测基准, 工程实践, 论文  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28590v1 Announce Type: new Abstract: Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Existing data-science agents often leave this harness implicit, making results difficult to reproduce, compare, and attribute across heterogeneous tasks. We introduce DS-Lighting, a unified harness toolkit that makes harness design explicit for data-science automation. DS-Lighting decomposes the harness into four reusable layers: data, workflow, execution, and evaluation, and represents diverse agents as executable operator programs that support both predefined pipelines and adaptive search. We further integrate multiple open-source data-science benchmarks into an MLE-Bench-style task format, enabling controlled comparison under a shared task interface, sandboxed runtime, and metric protocol. Experiments across agents, harnesses, models, and ablations show that explicit harness design improves reproducibility, comparability, and reliability, while reducing avoidable system-level failures in end-to-end data-science workflows. Our code is available at https://github.com/usail-hkust/dslighting

## 综合总结
DS-Lighting 提出了一种面向数据科学自动化 LLM Agent 的统一 harness 工具包，将隐式的 agent 执行框架显式分解为数据、工作流、执行、评估四层，并以可执行操作程序统一表征不同 agent，同时整合多源 benchmark 为 MLE-Bench 风格接口。论文主要贡献在于提升端到端数据科学工作流的复现性、可比性与可靠性，减少系统级失败，实验较为系统。整体属于系统与工程层面的贡献，适合 Agent 框架设计与评测方向的研究者参考，但缺乏深层的算法或理论突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
论文提出 DS-Lighting，将数据科学 Agent 的 harness 显式分解为数据、工作流、执行、评估四层，并将其表示为可执行的操作程序，支持预定义管线与自适应搜索。技术贡献在于提出统一的 harness 抽象和 MLE-Bench 风格的任务接口，提升异构任务的复现性与可比较性。整体思路清晰，但核心创新更多在于系统层面的整合与工程框架，而非算法或理论突破，深度有限。

### 实用性 (评分: 7.5/10)
该工作对从事数据科学自动化和 LLM Agent 研究的从业者具有较高参考价值：提供统一的 harness 工具包、可复用的四层架构、以及基于多个开源 benchmark 的标准化评测协议，便于研究者对比不同 agent、harness 和模型组合。代码开源降低了上手门槛，适合用于 Agent 工程实践与评测研究。不过其面向的仍是相对窄的数据科学自动化场景，通用性受限。

### 社区活跃度 (评分: 7.0/10)
话题契合当前 LLM Agent 与自动化数据科学的研究热点，arxiv ID 显示为 2026 年新发布，时效性较好。来源为 arXiv 论文，作者来自 HKUST，具备一定学术可信度。开源代码仓库的发布有助于社区传播。但缺少顶会正式发表信息与广泛引用数据，影响力尚待验证。

## 项目链接
https://arxiv.org/abs/2608.28590
