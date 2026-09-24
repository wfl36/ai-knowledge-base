# Silent Failures in Agent-Tool Interaction: An Audit of ToolUniverse

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-24  
**来源：** rss  

## 项目描述
arXiv:2609.26836v1 Announce Type: new Abstract: Agentic AI systems are increasingly adopting automated pipelines that integrate multiple tools. While prior research and benchmarks have studied about task success and task completion of these agentic systems, the research about agent to tool interaction, specifically in biology agentic workflow is limited. This study investigates specific failures in agent to tool interaction where a tool invocation appears successful, some or all of the information or functionality from the tool via API/ wrapper is incomplete or missing and there are no communications / notifications to the user or the agent about such missing information. We call this a silent failures as the user or the agents are not aware that such failure has occurred. For the purposes of this study we developed an audit mechanism to identify such silent failures in Agent to tool interaction, by examining 15 scientific tools (and their associated API documentation and tool documentations) integrated within ToolUniverse environment (ToolUniverse serves as our experimental environment rather than the object of the study itself). We structure our study around 7 failure locus characterising where the failure occurs in the chain. We observed 91 failures (manually validated post LLM based candidate discovery and automated testing), most frequent of them being missing data or fields and inconsistencies in search, filtering or ranking criteria. Most of the 91 failures occurred in API layer (51) or wrapper layer (25), with a potential of silent failure amplification downstream. The results show that silent failures originate upstream of the event and propagate downstream into apparently valid scientific outputs. We propose a concept of contextual reliability to handle such failures and suggest mechanisms for testing, disclosing, monitoring, and measuring such failures across the agent-tool interaction pipeline.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.26836
