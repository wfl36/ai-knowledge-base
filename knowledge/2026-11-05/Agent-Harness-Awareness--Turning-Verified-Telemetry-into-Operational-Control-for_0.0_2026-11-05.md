# Agent Harness Awareness: Turning Verified Telemetry into Operational Control for Tool-Using Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05391v1 Announce Type: new Abstract: Tool descriptions tell an agent what an action can do, but they do not necessarily reveal whether that action is healthy or suitable at the moment of use. Execution harnesses often possess this information through monitors, traces, and recent failures while the model choosing the next action does not. We call this gap operational blindness. We introduce Agent Harness Awareness, a trust-separated design in which the host supplies a small, fresh, verified state snapshot before a consequential action while retaining measurement, enforcement, evaluation, and final dispatch authority. We test its tools-and-network instance with ToolRoute, a controlled isolation benchmark that holds the task and candidate semantics constant and varies the operational information available to the model. In a 216-decision ablation across GPT-5.6 Sol, Claude Sonnet 5, and Gemini 3.7 Flash, verified tool-health state reduced mean observable policy regret by 96.9% against a same-shape neutral control (4,252 ms to 131 ms) and raised single-dispatch completion from 69.4% to 95.8%. In a separate 27-decision end-to-end replication with live local TCP/HTTP execution, OpenTelemetry client spans, and Toxiproxy-injected faults, verified state reduced mean regret from 8,956 ms to 0 ms (zero excess observable operational cost) and completed the live action in 9/9 model-by-fault cases versus 5/9 for the neutral control. These studies establish the tools-and-network instance of Agent Harness Awareness: selected host telemetry materially improves pre-dispatch operational choice. Runtime state, hardware pressure, economics, retry-aware recovery, and heterogeneous selection remain open empirical extensions of the same architecture.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05391
