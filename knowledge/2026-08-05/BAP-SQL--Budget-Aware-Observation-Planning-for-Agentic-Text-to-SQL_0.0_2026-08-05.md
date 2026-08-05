# BAP-SQL: Budget-Aware Observation Planning for Agentic Text-to-SQL

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02876v1 Announce Type: new Abstract: Tool-using agents do not merely consume observations: their actions determine what arrives next. In agentic text-to-SQL, a broad query can spend context and database work before useful evidence appears, while post-hoc compression cannot recover omitted rows or expended work. We present BAP-SQL, which treats observation formation as a budget-control stage: it estimates query risk, rewrites SQL when useful, and delegates hard limits to an independent runtime shield. Across general 4B, specialized FINER-SQL 4B, and 7B backbones, BAP-SQL improves tight-budget success. On the primary BIRD-derived setting, it gains 3.4/3.6 percentage points over matched SFT while using 4.5/5.0% fewer tokens. Matched retraining and task-level transfer associate the gain with policy-visible planning and budget-sensitive rescue. The benefit attenuates as model capability and budget increase, reverses at the loosest setting, and does not reduce database work.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02876
