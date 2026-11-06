# The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-06  
**来源：** rss  

## 项目描述
arXiv:2611.06989v1 Announce Type: new Abstract: Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what did this order, claim, or case cost in AI?) cannot be answered from billing data, because providers never see enterprise transaction boundaries. The FinOps Open Cost and Usage Specification (FOCUS) gives billing data one schema across providers but remains settlement-grain even as it adds AI token and requester attribution. We formalize this grain mismatch, derive seven requirements, and propose the Two-Ledger Model: a settlement ledger of FOCUS-conformant billing data joined to an attribution ledger of invocation-grain usage records built on OpenTelemetry GenAI telemetry. A layered correlation spine (trace context, A2A/MCP metadata, business-key correlation, probabilistic matching) assigns each record to its business transaction with recorded method and confidence; a versioned rate card prices usage in near real time; period reconciliation ties both ledgers to the invoice, and the unexplained residual identifies shadow AI. Costs are reported per order, claim, or outcome with agentic cost metrics. A simulation with known ground truth shows the spine sustaining cost coverage above 99% as trace propagation falls to zero, the reconciliation residual recovering planted unmetered spend within 0.24 percentage points while flagging provider billing errors, and mid-flight gating cutting p99 transaction cost by up to 61% at a 2-4% false-pause rate. We propose the attribution ledger as an invocation-grain FOCUS profile for standardization.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.06989
