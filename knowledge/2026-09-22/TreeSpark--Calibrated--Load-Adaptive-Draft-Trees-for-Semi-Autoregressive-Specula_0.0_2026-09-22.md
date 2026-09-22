# TreeSpark: Calibrated, Load-Adaptive Draft Trees for Semi-Autoregressive Speculative Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.22098v1 Announce Type: new Abstract: Speculative decoding accelerates language-model inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Recent block drafters make drafting nearly free: a single backbone pass emits an entire block of draft tokens. Draft trees promise a further gain -- several alternative continuations verified in one target forward -- but existing constructions rank candidates by per-position marginals that ignore which parent a candidate extends, so on semi-autoregressive drafters wider trees mostly add mis-ranked nodes; and a tree of fixed size ignores how much speculation each decoding round, and each serving load, can support. We introduce TreeSpark, which reads a parent-conditioned distribution from the drafter's existing Markov head at negligible cost, calibrates it into an edge-acceptance estimate, and lets path survival govern everything else: best-first expansion, per-round stopping, and a load-adaptive serving policy. Sampling siblings without replacement, with matching residuals in recursive rejection, keeps decoding lossless at any temperature. Adaptive trees improve on matched fixed budgets at every temperature; against a tuned chain on the same drafter, TreeSpark accepts 15-25% more draft tokens per round and decodes 8-14% faster in single-request wall-clock, and under rising load it gracefully shrinks the tree back to the chain. Code and artifacts: https://github.com/PopSoda2002/TreeSpark

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22098
