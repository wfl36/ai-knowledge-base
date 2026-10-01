# TomasuLLM: Out-of-Order Speculative Execution for LLM Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-01  
**来源：** rss  

## 项目描述
arXiv:2609.38201v1 Announce Type: new Abstract: Long-running tools can dominate coding-agent latency: compilers, test suites, and repository commands take seconds to minutes while the agent idles. This observation stall presents the same tension that drove out-of-order processors -- asequential interface hides work that can be predicted and started early, but a speculative result may become visible only after it and every earlier step have been validated. We present TomasuLLM, a runtime that executes agent tool calls out of trajectory order while preserving task-execution correctness. It drafts future actions, runs them in isolated copy-on-write sandboxes, traces their dependencies and effects, and commits results in trajectory order only after validation against committed state. Across three benchmarks spanning sub-second to minutes-long tool calls, TomasuLLM improves the reported benchmark means and scales with tool latency: 1.31x on 100 SWE-bench Verified tasks, 1.35x on 28 Terminal-Bench 2.0 tasks, and 1.27x matched progress on 18 SWE-Marathon sessions. Across 4,010 audited commit-validation records, it produces zero false accepts.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.38201
