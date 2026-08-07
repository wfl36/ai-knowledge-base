# SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-07  
**来源：** rss  

## 项目描述
arXiv:2608.05212v1 Announce Type: new Abstract: Deep search agents tackle challenging questions through long-horizon web interactions, a process that is both complex and fragile: small reasoning errors may propagate through long, noisy trajectories into fluent but incorrect answers. Diagnosing such failures is difficult, requiring the manual inspection of extremely long execution traces, which could be beyond human capacity. We therefore introduce SearchAuditBench, a benchmark that evaluates whether LLM auditors can localize, attribute, and repair these failures, thereby reducing the human burden. SearchAuditBench comprises 1,243 failed trajectories, averaging 73.1 messages and 65.1K tokens, collected from eight open-weight models on five deep-search benchmarks, each expert-annotated with the critical error step, a search-specific root cause, and a reference repair with grading rubrics. We further propose SearchAuditor, a multi-perspective auditing framework that effectively localizes, attributes, and repairs search-agent failures through evidence-grounded adjudication. Experimental results show that even the strongest baseline, when powered by a frontier model like GPT-5.5, attains only a 26.6% end-to-end pass rate. In contrast, our SearchAuditor consistently outperforms all baselines across different frontier models, achieving an end-to-end pass rate of 32.3%, and resuming failed runs with its repairs enables agents to better recover from errors.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.05212
