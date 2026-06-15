# TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with Business Intelligence Dashboards

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, BI, 数字孪生, LLM应用, 数据分析, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13731v1 Announce Type: new Abstract: Business intelligence (BI) increasingly combines dashboard interaction with LLM-based assistance, but these two modes often fall out of sync during multi-step analysis. As users switch between direct dashboard manipulation and natural-language queries, it becomes difficult to preserve a consistent analytical state across filters, hierarchies, metrics, and chart context. We present TwinBI, an agentic digital-twin framework that couples an LLM-based agent system with an executable BI dashboard state. TwinBI unifies conversational interaction, dashboard manipulation, semantic grounding, and provenance tracking through a shared analytical state reconstructed from a unified interaction log. It also exposes artifacts such as schema views, SQL, logs, and an /insights command for state-grounded analytical summaries. We evaluate TwinBI in two complementary ways. In a controlled A/B benchmark with the same backbone agent, TwinBI improves exact-match accuracy from 43.3% to 63.3%, partial-credit accuracy from 48.3% to 70.8%, and substantially reduces timeout rate from 40.0% to 10.0% relative to Dashboard alone. In a usability study, participants benefited from the integrated dashboard-and-chat workflow, with high task accuracy, moderate workload, and favorable ratings for state-aware interaction mechanisms. These results suggest that TwinBI improves both agent-level analytical reliability and user-facing analytical support by turning visible dashboard state into richer actionable context. Our dataset and source code are available at: https://github.com/simonjisu/TwinBI

## 综合总结
TwinBI 提出了一种代理数字孪生框架，通过统一交互日志重建共享分析状态，解决了 BI 仪表盘与 LLM 交互中的状态不同步问题。实验显示其显著提升了分析准确率并大幅降低了超时率，且已开源，对智能数据分析的工程落地具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
将数字孪生概念引入 BI 与 LLM Agent 的交互中，创新性地提出通过统一交互日志重建共享分析状态，解决了多步分析中对话与仪表盘状态割裂的核心痛点。A/B 测试数据详实，超时率从40%降至10%以及准确率的显著提升，有力论证了方法的严谨性和有效性。

### 实用性 (评分: 9.0/10)
BI 与 LLM 结合是极具商业价值的落地场景，TwinBI 解决了实际产品中常见的交互状态不同步问题。其暴露的 SQL、Schema 等中间产物及开源代码，对 BI SaaS 开发者和 Agent 构建者具有极高的工程参考价值，可快速应用于现有数据分析系统的智能化改造。

### 社区活跃度 (评分: 8.5/10)
论文发布于 arXiv，时间极新（2026年），紧扣 LLM+Agent+BI 的行业热点。开源代码和数据集提升了成果的可信度和社区复现性，为数据分析和智能体交互领域提供了有价值的实践基准和关注点。

## 项目链接
https://arxiv.org/abs/2606.13731
