# Towards Proactive Detection of User-Side Implicit Conflicts in Human-LLM Dialogue

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19155v1 Announce Type: new Abstract: In Human-LLM dialogue, follow-up user utterances may implicitly conflict with earlier intents, leading the LLM to misinterpret user needs and generate inappropriate responses. A reliable dialogue system should proactively detect user-side conflicts before generating a response and seek clarification when necessary. However, prior work has largely focused on LLM-side conflicts, leaving user-side conflicts underexplored. To fill this gap, we construct UC-Bench, a human-annotated benchmark for evaluating user-side conflict detection. Preliminary experiments show that existing LLMs struggle with this task, especially when conflicts arise from implicit incompatibilities grounded in dialogue history. To improve lightweight LLMs with limited training data, we investigate data synthesis for user-side conflict detection. Existing synthesis methods do not explicitly model the implicit incompatibilities between historical and current user utterances, making it difficult to capture the evolution of conflicts and to generate reliably labeled implicit conflict samples. We propose SynUC, a constraint-guided synthesis method that represents user-side conflicts in a constraint space and uses the SPEAKING framework to guide traceable constraint transformations. Applying SynUC to WildChat, we construct UC-Data, a user-side conflict training set containing 2,487 samples. On UC-Bench, Qwen3.5-4B trained on UC-Data outperforms larger general-purpose LLMs such as Claude Opus 4.8, as well as the same backbone trained on data synthesized by existing methods.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19155
