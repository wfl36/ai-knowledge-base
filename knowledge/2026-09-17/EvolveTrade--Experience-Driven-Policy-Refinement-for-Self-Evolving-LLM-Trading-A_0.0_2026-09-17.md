# EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17632v1 Announce Type: new Abstract: Large language model (LLM) trading agents can combine market data, news, and executable analysis, but their behavior is often controlled by static hand-written tool-use policies that are fixed before deployment. This limits their ability to adapt how they gather evidence, invoke tools, verify signals, and manage risk under changing market regimes. We introduce EvolveTrade, a self-evolving framework that treats the system prompt of a tool-using trading agent as a text-parameterized policy. After each update interval, a Policy Agent revises this policy using accumulated decision traces and realized portfolio feedback, while keeping the backbone LLM fixed. The updated policy is then used for the next batch of trading decisions, enabling the agent to refine its information-acquisition and portfolio-construction procedure over time. Experiments across multiple market regimes and two LLM backbones show that EvolveTrade often improves Sharpe Ratio and Cumulative Return over fixed-policy LLM baselines, achieving the improved SR and CR in most evaluated settings. Behavioral analyses further show that self-evolved policies increase code-mediated analysis and activate regime-relevant computations; case-level policy-to-return attributions trace how policy-induced allocation changes contribute to realized return differences. These results suggest that adapting the reusable procedure governing tool use is a key direction for building more robust LLM trading agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17632
