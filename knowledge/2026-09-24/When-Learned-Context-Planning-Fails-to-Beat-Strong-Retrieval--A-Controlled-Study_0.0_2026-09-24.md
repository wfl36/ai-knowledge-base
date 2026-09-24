# When Learned Context Planning Fails to Beat Strong Retrieval: A Controlled Study of Planning, Routing, and Reranking for Long-Context QA

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-24  
**来源：** rss  

## 项目描述
arXiv:2609.26976v1 Announce Type: new Abstract: Learned context planning selects evidence atoms before an answer model reasons over them. We test whether this learned selection improves long-context multiple-choice QA after strong retrieval, routing, budgeted-selector, and reranking controls. Our primary diagnostic uses all 503 LongBench-v2 MCQ questions with Qwen2.5-7B-Instruct. The planner is SFT-trained on outcome-selected traces from 140 training and 28 development questions; because the 503-question analysis includes those questions, it is partly transductive. At an 18k-character budget, anchored hybrid retrieval reaches 36.18% accuracy and BM25 reaches 35.98%, while the best direct planner-guided method reaches 34.19%. On the untouched 152-question test split, anchored hybrid remains higher (42.11% versus 36.84%). Leakage-safe routers cannot convert a large oracle gap. Under tight budgets, the best planner is ahead by only 0.40 points at 6k and loses at 9k; planner-guided reranking has a +1.79-point estimate at 6k with a paired interval crossing zero and ties the control at 9k. Packing-order and score-flatness analyses did not identify a stable mechanism. Under this setup, learned planning is a weak relevance signal rather than a replacement for strong retrieval.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.26976
